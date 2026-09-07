# JavaScript Foundation Part09 - Module, Error Handling, and Browser Debugging

---

# 1. Module

## 1.1 Module Concept

### [개념]

Module은 JavaScript 코드를 파일 단위로 분리하고 필요한 값만 export / import 해서 사용하는 구조다.

Frontend JavaScript에서는 API 함수, Utility 함수, Validation 함수, Constant, Component Logic을 파일별로 분리하기 위해 Module을 사용한다.

예:

```javascript
export function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}
```

다른 파일에서 import:

```javascript
import { formatPrice } from "./format.js";
```

---

### [핵심]

- Module
- ES Module
- export
- import
- named export
- default export
- file separation
- reusable code
- API module
- utility module
- constants module
- dependency management
- Frontend Architecture

---

### [실무]

2026 실무 기준에서 Frontend Agent는 Module을 단순 문법이 아니라 코드 책임 분리 기준으로 이해해야 한다.

Module 분리 대상:

- API Request Function
- API Response Normalize Function
- Validation Function
- Format Function
- Constant
- Error Message
- UI Utility
- Event Handler Helper
- Domain API Layer

예시 구조:

```text
src/
├ api/
│ ├ festivalApi.js
│ └ reviewApi.js
├ utils/
│ ├ format.js
│ └ validation.js
├ constants/
│ └ apiConstants.js
└ pages/
  └ FestivalPage.js
```

주의:

- 한 파일에 모든 로직을 넣지 않는다.
- Module 이름은 책임이 드러나야 한다.
- 순환 참조를 피한다.
- import 경로 오타를 주의한다.
- default export와 named export를 혼용할 때 팀 컨벤션을 따른다.
- React 전환 시 Component, Hook, API, Utility 분리가 중요해진다.

---

### [FAQ]

Q. Module이 뭐야?
A. JavaScript 코드를 파일 단위로 분리하고 필요한 값만 export / import 해서 사용하는 구조다.

Q. Module을 쓰는 이유는 뭐야?
A. 코드 책임을 분리하고 재사용성과 유지보수성을 높이기 위해 사용한다.

Q. Frontend에서 Module은 어디에 많이 써?
A. API 함수, 유틸 함수, 검증 함수, 상수, 화면 로직 분리에 많이 사용한다.

Q. Module 분리에서 가장 중요한 기준은 뭐야?
A. 파일 하나가 하나의 명확한 책임을 갖도록 분리하는 것이다.

---

# 2. ES Module Syntax

## 2.1 export Rules

### [개념]

`export`는 현재 Module의 값, 함수, 객체, class를 다른 Module에서 사용할 수 있게 내보내는 문법이다.

JavaScript ES Module에서는 named export와 default export를 사용할 수 있다.

예:

```javascript
export const DEFAULT_PAGE_SIZE = 20;

export function normalizeKeyword(keyword) {
  return keyword.trim();
}
```

---

### [핵심]

- export
- named export
- default export
- reusable function
- constant export
- API function export
- module public API
- file boundary

---

### [실무]

named export는 여러 값을 명확한 이름으로 내보낼 때 사용한다.

```javascript
export function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}

export function validateRating(rating) {
  return rating >= 1 && rating <= 5;
}
```

상수 export:

```javascript
export const API_BASE_URL = "/api";
export const DEFAULT_IMAGE_URL = "/default.png";
```

주의:

- export할 값은 외부에서 재사용할 필요가 있어야 한다.
- 내부에서만 쓰는 helper는 export하지 않는다.
- export 이름은 역할이 명확해야 한다.
- 너무 많은 값을 한 파일에서 export하면 책임이 흐려질 수 있다.
- API 함수와 UI 함수 export를 섞지 않는다.

---

### [FAQ]

Q. export는 뭐야?
A. 현재 Module의 값을 다른 Module에서 사용할 수 있도록 내보내는 문법이다.

Q. 모든 함수를 export해야 해?
A. 아니다. 다른 파일에서 사용할 필요가 있는 함수만 export한다.

Q. 내부 helper 함수도 export해야 해?
A. 외부 재사용이 없다면 export하지 않고 파일 내부에 둔다.

Q. 상수도 export할 수 있어?
A. 가능하다. API URL, 기본 이미지 경로, page size 같은 상수를 export할 수 있다.

---

## 2.2 import Rules

### [개념]

`import`는 다른 Module에서 export한 값, 함수, 객체를 현재 Module로 가져오는 문법이다.

예:

```javascript
import { validateKeyword } from "./validation.js";
```

---

### [핵심]

- import
- named import
- default import
- relative path
- module path
- dependency
- file extension
- import order
- unused import

---

### [실무]

named import 예:

```javascript
import { validateKeyword, validateRating } from "../utils/validation.js";
```

상수 import:

```javascript
import { DEFAULT_IMAGE_URL } from "../constants/apiConstants.js";
```

API 함수 import:

```javascript
import { searchFestivals } from "../api/festivalApi.js";
```

주의:

- import 이름은 export 이름과 일치해야 한다.
- 경로 오타를 주의한다.
- 사용하지 않는 import는 제거한다.
- 순환 import를 만들지 않는다.
- import 순서는 팀 컨벤션을 따른다.
- bundler 환경에 따라 파일 확장자 생략 가능 여부가 다를 수 있다.

---

### [FAQ]

Q. import는 뭐야?
A. 다른 Module에서 export한 값을 현재 Module로 가져오는 문법이다.

Q. import 이름은 마음대로 바꿀 수 있어?
A. named import는 기본적으로 export 이름과 일치해야 한다. alias를 사용할 수는 있다.

Q. 사용하지 않는 import는 놔둬도 돼?
A. 제거하는 것이 좋다. lint 경고와 코드 혼란을 줄일 수 있다.

Q. import 경로 오류는 어디서 확인해?
A. 개발 서버 오류, Console, bundler error, IDE 경고에서 확인할 수 있다.

---

# 3. Named Export and Default Export

## 3.1 Named Export Rules

### [개념]

Named Export는 이름이 있는 여러 값을 하나의 Module에서 export하는 방식이다.

import할 때는 같은 이름을 중괄호 안에 작성한다.

예:

```javascript
export function formatDate(dateText) {
  return new Date(dateText).toLocaleDateString("ko-KR");
}

export function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}
```

import:

```javascript
import { formatDate, formatPrice } from "./format.js";
```

---

### [핵심]

- named export
- named import
- multiple exports
- explicit name
- refactor friendly
- utility module
- API module

---

### [실무]

Utility Module에는 named export가 적합하다.

예:

```javascript
export function normalizeFestivalList(responseBody) {
  const content = responseBody?.data?.content;

  return Array.isArray(content) ? content : [];
}

export function normalizeFestivalDetail(responseBody) {
  return responseBody?.data ?? null;
}
```

장점:

- import할 값이 명확하다.
- 여러 함수를 한 파일에서 관리하기 쉽다.
- 자동완성 및 refactor에 유리하다.
- 사용하지 않는 export를 추적하기 쉽다.

주의:

- export 이름 변경 시 import도 함께 변경해야 한다.
- 너무 많은 named export는 파일 책임 과다 신호일 수 있다.
- 같은 의미의 함수명을 여러 Module에서 중복하지 않는다.

---

### [FAQ]

Q. Named Export는 뭐야?
A. 이름이 있는 여러 값을 하나의 Module에서 export하는 방식이다.

Q. Named Export는 import할 때 어떻게 써?
A. `import { name } from "./module.js";` 형식으로 가져온다.

Q. Utility 함수에는 Named Export가 좋아?
A. 여러 유틸 함수를 명확한 이름으로 가져올 수 있어 적합하다.

Q. Named Export 이름을 바꾸면 어떻게 돼?
A. 해당 export를 import하는 코드도 함께 수정해야 한다.

---

## 3.2 Default Export Rules

### [개념]

Default Export는 Module에서 기본값 하나를 export하는 방식이다.

하나의 Module에 하나의 default export만 사용할 수 있다.

예:

```javascript
export default function requestJson(url, options = {}) {
  return fetch(url, options);
}
```

import:

```javascript
import requestJson from "./requestJson.js";
```

---

### [핵심]

- default export
- single default value
- default import
- module main value
- naming flexibility
- convention caution

---

### [실무]

Default Export는 파일의 대표 값이 하나일 때 사용할 수 있다.

예:

```javascript
const festivalApi = {
  fetchList() {
    return requestJson("/api/festivals");
  },

  fetchDetail(festivalId) {
    return requestJson(`/api/festivals/${festivalId}`);
  },
};

export default festivalApi;
```

주의:

- import 이름을 자유롭게 지을 수 있어 이름 불일치가 생길 수 있다.
- 팀 컨벤션이 named export 위주라면 default export를 줄인다.
- 하나의 파일에 default export와 named export를 혼용하면 혼란이 생길 수 있다.
- React Component 파일에서는 default export를 쓰는 팀도 많다.
- API / Utility Layer에서는 named export를 선호하는 경우도 많다.

---

### [FAQ]

Q. Default Export는 뭐야?
A. Module에서 기본값 하나를 export하는 방식이다.

Q. 하나의 파일에 default export를 여러 개 쓸 수 있어?
A. 없다. 하나의 Module에는 default export가 하나만 가능하다.

Q. Default Export는 import 이름을 마음대로 정할 수 있어?
A. 가능하다. 그래서 팀 컨벤션이 중요하다.

Q. Named Export와 Default Export 중 뭐가 좋아?
A. 상황과 팀 컨벤션에 따른다. 여러 유틸 함수는 named export, 대표값 하나는 default export가 적합하다.

---

# 4. Module Architecture

## 4.1 API Module Rules

### [개념]

API Module은 Backend API 호출 함수를 Domain별로 분리한 Module이다.

Frontend Agent는 API endpoint 문자열, Fetch 공통 처리, 인증 Header, Normalize Function을 UI 코드와 분리해야 한다.

---

### [핵심]

- API Module
- festivalApi
- reviewApi
- authApi
- requestJson
- endpoint separation
- fetch wrapper
- domain API layer
- API response normalize
- UI separation

---

### [실무]

API Module 구조 예:

```text
src/
├ api/
│ ├ requestJson.js
│ ├ festivalApi.js
│ ├ reviewApi.js
│ └ authApi.js
```

requestJson:

```javascript
export async function requestJson(url, options = {}) {
  const response = await fetch(url, options);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return await response.json();
}
```

festivalApi:

```javascript
import { requestJson } from "./requestJson.js";

export function fetchFestivalList() {
  return requestJson("/api/festivals");
}

export function fetchFestivalDetail(festivalId) {
  return requestJson(`/api/festivals/${festivalId}`);
}
```

주의:

- API endpoint를 화면 코드에 흩뿌리지 않는다.
- requestJson은 공통 응답 처리만 담당한다.
- Domain API 함수는 endpoint와 Method를 명확히 표현한다.
- 인증 필요 API는 Header 주입 기준을 통일한다.
- Normalize Function은 API Module 내부 또는 별도 mapper Module로 분리할 수 있다.

---

### [FAQ]

Q. API Module은 뭐야?
A. Backend API 호출 함수를 Domain별로 분리한 Module이다.

Q. API Module을 쓰는 이유는 뭐야?
A. endpoint, fetch 옵션, 응답 처리, 오류 처리를 UI 코드와 분리하기 위해서다.

Q. requestJson은 어떤 책임을 가져?
A. fetch 실행, response.ok 확인, 204 처리, JSON parsing 같은 공통 요청 처리를 담당한다.

Q. API endpoint를 화면 코드에 직접 써도 돼?
A. 가능하지만 규모가 커지면 유지보수가 어려우므로 API Module로 분리하는 것이 좋다.

---

## 4.2 Utility Module Rules

### [개념]

Utility Module은 여러 곳에서 재사용되는 순수 함수나 보조 함수를 모아둔 Module이다.

Format, Validation, Mapping, Query 생성, ClassName 병합 같은 로직을 담을 수 있다.

---

### [핵심]

- Utility Module
- pure function
- format
- validation
- mapper
- query builder
- className helper
- reusable logic
- side effect avoidance

---

### [실무]

format.js:

```javascript
export function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}

export function formatDate(dateText) {
  return new Date(dateText).toLocaleDateString("ko-KR");
}
```

validation.js:

```javascript
export function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}

export function validateRating(rating) {
  return rating >= 1 && rating <= 5;
}
```

query.js:

```javascript
export function createQueryString(params) {
  const searchParams = new URLSearchParams();

  Object.entries(params).forEach(([key, value]) => {
    if (value !== null && value !== undefined && value !== "") {
      searchParams.set(key, String(value));
    }
  });

  return searchParams.toString();
}
```

주의:

- Utility Function은 가능하면 Pure Function으로 작성한다.
- DOM 조작, API 호출, localStorage 접근은 Utility에 섞지 않는다.
- 파일 이름은 역할 중심으로 작성한다.
- 너무 많은 유틸을 하나의 file에 모으지 않는다.
- 특정 Domain에만 쓰이는 함수는 Domain Module에 둘 수 있다.

---

### [FAQ]

Q. Utility Module은 뭐야?
A. 여러 곳에서 재사용되는 순수 함수나 보조 함수를 모아둔 Module이다.

Q. Utility Module에는 무엇을 넣어?
A. format, validation, query string 생성, className 병합 같은 재사용 함수를 넣을 수 있다.

Q. Utility Module에 API 호출을 넣어도 돼?
A. 지양한다. API 호출은 API Module에 두는 것이 좋다.

Q. Utility Function은 Pure Function이 좋아?
A. 좋다. 입력과 출력이 명확해야 테스트와 재사용이 쉽다.

---

## 4.3 Constants Module Rules

### [개념]

Constants Module은 여러 파일에서 공통으로 사용하는 변하지 않는 값을 모아두는 Module이다.

API 경로, 기본 이미지, page size, status 값, error message key 등을 관리할 수 있다.

---

### [핵심]

- Constants Module
- constant
- API_BASE_URL
- DEFAULT_IMAGE_URL
- DEFAULT_PAGE_SIZE
- status value
- error message
- magic number removal
- naming convention

---

### [실무]

constants 예:

```javascript
export const API_BASE_URL = "/api";
export const DEFAULT_IMAGE_URL = "/default.png";
export const DEFAULT_PAGE_SIZE = 20;

export const REQUEST_STATUS = {
  IDLE: "IDLE",
  LOADING: "LOADING",
  SUCCESS: "SUCCESS",
  ERROR: "ERROR",
};
```

사용 예:

```javascript
import { DEFAULT_IMAGE_URL } from "../constants/appConstants.js";

const imageUrl = festival.imageUrl ?? DEFAULT_IMAGE_URL;
```

주의:

- 변하지 않는 값만 constants로 분리한다.
- runtime state를 constants에 넣지 않는다.
- 이름은 대문자 snake case를 사용할 수 있다.
- magic number와 magic string을 줄인다.
- 너무 많은 상수를 한 파일에 몰아넣지 않고 domain별 분리 가능하다.

---

### [FAQ]

Q. Constants Module은 뭐야?
A. 여러 파일에서 공통으로 사용하는 변하지 않는 값을 모아두는 Module이다.

Q. Constants Module에는 무엇을 넣어?
A. API base URL, 기본 이미지 경로, page size, status 값 같은 상수를 넣을 수 있다.

Q. runtime state를 constants에 넣어도 돼?
A. 안 된다. constants는 변하지 않는 값만 관리한다.

Q. magic string을 줄이는 이유는 뭐야?
A. 오타와 중복을 줄이고 변경 지점을 한 곳으로 모으기 위해서다.

---

# 5. Error Handling

## 5.1 Error Handling Concept

### [개념]

Error Handling은 코드 실행 중 발생할 수 있는 오류를 감지하고 적절히 처리하는 과정이다.

Frontend JavaScript에서는 API 오류, 입력 오류, JSON 파싱 오류, DOM 접근 오류, 비동기 오류를 구분해서 처리해야 한다.

---

### [핵심]

- Error Handling
- try catch
- throw Error
- Promise rejection
- API error
- validation error
- runtime error
- user message
- developer log
- fallback UI
- loading cleanup

---

### [실무]

Frontend Error Handling Flow:

```text
Error Occurs
→ Catch or Error Boundary
→ Developer Log
→ User Friendly Message
→ Fallback Value or UI
→ Cleanup
```

API Error 처리 예:

```javascript
async function loadFestivals() {
  setLoading(true);
  setError(null);

  try {
    const festivals = await fetchFestivals();
    renderFestivals(festivals);
  } catch (error) {
    console.error("Festival load failed:", error);
    setError("축제 목록을 불러오지 못했습니다.");
  } finally {
    setLoading(false);
  }
}
```

주의:

- catch를 비워두지 않는다.
- 사용자 메시지와 개발자 로그를 구분한다.
- 민감정보를 로그로 출력하지 않는다.
- loading cleanup은 finally에서 처리한다.
- fallback 값을 반환할지 throw할지 정책을 명확히 한다.
- Error Handling은 문제를 숨기는 것이 아니라 안전하게 드러내는 것이다.

---

### [FAQ]

Q. Error Handling이 뭐야?
A. 코드 실행 중 발생할 수 있는 오류를 감지하고 적절히 처리하는 과정이다.

Q. Frontend에서 어떤 오류를 처리해야 해?
A. API 오류, 입력 오류, JSON 파싱 오류, DOM 접근 오류, 비동기 오류를 처리해야 한다.

Q. catch를 비워둬도 돼?
A. 안 된다. 로그, 사용자 메시지, fallback 처리 중 하나는 해야 한다.

Q. Error Handling의 목적은 오류를 숨기는 거야?
A. 아니다. 오류를 안전하게 처리하고 사용자와 개발자에게 필요한 정보를 제공하는 것이다.

---

## 5.2 throw Error Rules

### [개념]

`throw`는 코드 실행 중 Error를 발생시키는 문법이다.

`throw new Error(message)` 형태로 명확한 오류를 만들 수 있다.

예:

```javascript
throw new Error("Festival load failed");
```

---

### [핵심]

- throw
- Error
- throw new Error
- control flow interruption
- catch
- custom message
- API failure
- validation failure

---

### [실무]

API 실패 시 Error 발생:

```javascript
async function requestJson(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  return await response.json();
}
```

Validation 실패를 Error로 처리하는 경우:

```javascript
function assertValidKeyword(keyword) {
  if (keyword.trim().length === 0) {
    throw new Error("Keyword is required");
  }
}
```

주의:

- 사용자에게 보여줄 메시지와 개발자용 Error message를 구분한다.
- throw 후 현재 함수 실행은 중단된다.
- async function 내부 throw는 rejected Promise가 된다.
- Error message에 민감정보를 넣지 않는다.
- Validation은 return message 방식과 throw 방식 중 정책을 정한다.

---

### [FAQ]

Q. throw는 뭐야?
A. 코드 실행 중 Error를 발생시키는 문법이다.

Q. throw new Error를 쓰는 이유는 뭐야?
A. 명확한 Error 객체와 메시지를 만들어 catch에서 처리하기 위해서다.

Q. async function 내부에서 throw하면 어떻게 돼?
A. rejected Promise가 되어 try / catch 또는 catch로 처리할 수 있다.

Q. Error message에 Token을 넣어도 돼?
A. 안 된다. 민감정보는 Error message나 로그에 포함하지 않는다.

---

## 5.3 try catch finally Rules

### [개념]

`try / catch / finally`는 오류가 발생할 수 있는 코드를 실행하고, 오류 처리와 정리 작업을 수행하는 문법이다.

- try: 오류가 발생할 수 있는 코드
- catch: 오류 처리
- finally: 성공 / 실패와 관계없는 정리 작업

---

### [핵심]

- try
- catch
- finally
- error handling
- cleanup
- loading state
- async await
- fallback
- user message
- developer log

---

### [실무]

비동기 요청 처리:

```javascript
async function submitReview(review) {
  setLoading(true);
  setError(null);

  try {
    const result = await createReview(review);

    showSuccess("리뷰가 등록되었습니다.");

    return result;
  } catch (error) {
    console.error("Review submit failed:", error);
    setError("리뷰 등록 중 오류가 발생했습니다.");

    return null;
  } finally {
    setLoading(false);
  }
}
```

주의:

- try 안에는 실패 가능성이 있는 최소 범위의 코드를 넣는다.
- catch에서 오류를 무시하지 않는다.
- finally에서 loading 해제와 cleanup 처리
- catch에서 fallback을 반환할지 다시 throw할지 결정
- 중첩 try / catch 남용 금지
- 개발자 로그와 사용자 메시지 분리

---

### [FAQ]

Q. try / catch / finally는 뭐야?
A. 오류 발생 가능 코드, 오류 처리, 정리 작업을 분리해 실행하는 문법이다.

Q. finally는 언제 실행돼?
A. 성공과 실패 모두에서 마지막에 실행된다.

Q. loading 해제는 어디에서 하는 게 좋아?
A. finally에서 처리하는 것이 안전하다.

Q. catch에서 오류를 다시 throw해도 돼?
A. 가능하다. 상위 호출자에게 오류 처리를 위임해야 할 때 다시 throw할 수 있다.

---

# 6. Error Classification

## 6.1 Validation Error Rules

### [개념]

Validation Error는 사용자가 입력한 값이 요구 조건을 만족하지 않을 때 발생하는 오류다.

Frontend Validation은 사용자 경험을 개선하지만 Backend Validation을 대체하지 않는다.

---

### [핵심]

- Validation Error
- input validation
- required
- min length
- max length
- number range
- field error
- user message
- frontend validation
- backend validation

---

### [실무]

Validation 함수 예:

```javascript
export function validateReview({ rating, content }) {
  if (rating < 1 || rating > 5) {
    return "평점은 1점 이상 5점 이하로 입력해야 합니다.";
  }

  if (content.trim().length === 0) {
    return "리뷰 내용을 입력하세요.";
  }

  return null;
}
```

처리 예:

```javascript
const errorMessage = validateReview(reviewForm);

if (errorMessage) {
  showError(errorMessage);
  return;
}
```

주의:

- Validation Error는 사용자에게 바로 안내한다.
- Field 단위 오류와 Global 오류를 구분한다.
- Frontend 검증은 UX용이고 Backend 검증은 필수다.
- 민감정보를 오류 메시지에 포함하지 않는다.
- Validation 규칙은 중복되지 않게 관리한다.

---

### [FAQ]

Q. Validation Error는 뭐야?
A. 사용자가 입력한 값이 요구 조건을 만족하지 않을 때 발생하는 오류다.

Q. Frontend Validation만 하면 충분해?
A. 아니다. Backend Validation도 반드시 필요하다.

Q. Validation Error는 사용자에게 보여줘도 돼?
A. 보여줘야 한다. 사용자가 수정할 수 있는 명확한 안내가 필요하다.

Q. Validation 함수는 어떤 값을 반환하는 게 좋아?
A. 오류 메시지 또는 null을 반환하면 처리하기 쉽다.

---

## 6.2 Network Error Rules

### [개념]

Network Error는 네트워크 연결 문제, 서버 연결 실패, CORS 차단, 요청 취소 등으로 API 요청이 정상적으로 완료되지 못한 오류다.

Fetch에서는 Network Error가 Promise rejected로 처리될 수 있다.

---

### [핵심]

- Network Error
- fetch rejection
- offline
- server down
- CORS
- AbortError
- timeout pattern
- retry
- user message

---

### [실무]

Network Error 처리:

```javascript
try {
  const response = await fetch("/api/festivals");
  const data = await response.json();

  return data;
} catch (error) {
  console.error("Network request failed:", error);

  showError("네트워크 연결을 확인해 주세요.");

  return null;
}
```

주의:

- Network Error와 HTTP Error를 구분한다.
- CORS 오류는 Browser에서 Network Error처럼 보일 수 있다.
- AbortError는 일반 오류 메시지로 표시하지 않을 수 있다.
- 서버가 응답한 400 / 500은 response.ok로 처리한다.
- 재시도 버튼을 제공할 수 있다.

---

### [FAQ]

Q. Network Error는 뭐야?
A. 네트워크 연결 문제나 요청 차단으로 API 요청이 정상 완료되지 못한 오류다.

Q. Network Error와 HTTP Error는 같아?
A. 아니다. Network Error는 응답 자체가 실패한 경우이고, HTTP Error는 서버가 오류 status로 응답한 경우다.

Q. CORS 오류도 Network Error처럼 보여?
A. Browser에서는 그렇게 보일 수 있다.

Q. AbortError는 사용자에게 오류로 보여줘야 해?
A. 보통 요청 취소 흐름이면 일반 오류 메시지로 보여주지 않는다.

---

## 6.3 Runtime Error Rules

### [개념]

Runtime Error는 코드 실행 중 발생하는 오류다.

예를 들어 null property 접근, undefined 함수 호출, JSON parse 실패, DOM 요소 null 접근 등이 Runtime Error에 해당한다.

---

### [핵심]

- Runtime Error
- TypeError
- ReferenceError
- SyntaxError
- null access
- undefined access
- JSON parse error
- DOM null error
- defensive coding

---

### [실무]

흔한 Runtime Error:

```javascript
const title = response.data.content[0].title;
```

안전한 접근:

```javascript
const title = response?.data?.content?.[0]?.title ?? "제목 없음";
```

DOM null 접근 방어:

```javascript
const titleElement = document.querySelector(".title");

if (titleElement) {
  titleElement.textContent = "Festival";
}
```

주의:

- optional chaining으로 null 접근 오류를 줄인다.
- Array.isArray로 배열 여부를 확인한다.
- DOM selection 결과는 null일 수 있다.
- JSON.parse는 try / catch로 감싼다.
- ReferenceError는 변수명 오타나 선언 전 사용을 의심한다.

---

### [FAQ]

Q. Runtime Error는 뭐야?
A. 코드 실행 중 발생하는 오류다.

Q. Cannot read properties of undefined 오류는 왜 나?
A. undefined 값에서 property를 읽으려고 했기 때문이다.

Q. DOM 요소 null 오류는 왜 발생해?
A. selector에 맞는 요소가 없거나 DOM 로드 전에 접근했을 수 있다.

Q. Runtime Error를 줄이려면 어떻게 해?
A. null check, optional chaining, Array.isArray, try / catch, 명확한 변수 선언을 사용한다.

---

# 7. User Message and Developer Log

## 7.1 User Message Rules

### [개념]

User Message는 사용자에게 보여주는 오류 또는 안내 문구다.

User Message는 짧고 명확하며 사용자가 다음 행동을 알 수 있어야 한다.

예:

```javascript
showError("축제 목록을 불러오지 못했습니다.");
```

---

### [핵심]

- User Message
- friendly error
- actionable message
- validation message
- API error message
- global message
- field message
- no stack trace
- no sensitive data

---

### [실무]

좋은 사용자 메시지:

```text
검색어를 입력하세요.
축제 목록을 불러오지 못했습니다.
네트워크 연결을 확인해 주세요.
로그인이 필요합니다.
권한이 없습니다.
```

나쁜 사용자 메시지:

```text
TypeError: Cannot read properties of undefined
JWT expired at 1730000000
SQL Exception at server stack trace
```

주의:

- 사용자에게 stack trace를 보여주지 않는다.
- 민감정보를 포함하지 않는다.
- Validation Error는 수정 방법을 알려준다.
- API Error는 상황을 짧게 안내한다.
- 동일 오류 메시지는 constants로 관리할 수 있다.

---

### [FAQ]

Q. User Message는 뭐야?
A. 사용자에게 보여주는 오류 또는 안내 문구다.

Q. 사용자에게 stack trace를 보여줘도 돼?
A. 안 된다. 사용자가 이해할 수 있는 짧은 안내 문구를 보여줘야 한다.

Q. 좋은 오류 메시지는 어떤 메시지야?
A. 짧고 명확하며 사용자가 다음 행동을 알 수 있는 메시지다.

Q. 오류 메시지에 Token이나 개인정보를 넣어도 돼?
A. 안 된다. 민감정보는 사용자 메시지에 포함하지 않는다.

---

## 7.2 Developer Log Rules

### [개념]

Developer Log는 개발자가 오류 원인을 분석하기 위해 Console 또는 Logging System에 남기는 정보다.

Frontend에서는 `console.error`, `console.warn`, `console.info`를 상황에 맞게 사용할 수 있다.

예:

```javascript
console.error("Festival load failed:", error);
```

---

### [핵심]

- Developer Log
- console.error
- console.warn
- console.info
- debugging
- error context
- no sensitive data
- production log caution

---

### [실무]

개발자 로그 예:

```javascript
try {
  const festivals = await fetchFestivals();
  renderFestivals(festivals);
} catch (error) {
  console.error("Festival load failed:", error);
  showError("축제 목록을 불러오지 못했습니다.");
}
```

주의:

- 로그에는 오류 맥락을 포함한다.
- 민감정보를 로그에 출력하지 않는다.
- Token, Password, 개인정보, 결제정보 로그 금지
- 운영 환경에서는 불필요한 console.log 제거
- console.error와 사용자 메시지는 역할이 다르다.
- 빈 catch보다 로그와 fallback 처리가 낫다.

---

### [FAQ]

Q. Developer Log는 뭐야?
A. 개발자가 오류 원인을 분석하기 위해 남기는 로그다.

Q. console.error는 언제 써?
A. API 실패, 예외 발생처럼 개발자가 확인해야 하는 오류에 사용한다.

Q. console.log에 Token을 찍어도 돼?
A. 안 된다. Token, Password, 개인정보, 결제정보는 로그에 출력하면 안 된다.

Q. 사용자 메시지와 개발자 로그는 왜 분리해?
A. 사용자는 이해 가능한 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

---

# 8. Browser Debugging

## 8.1 Browser DevTools Concept

### [개념]

Browser DevTools는 Frontend 코드를 디버깅하고 Network 요청, Console 오류, DOM 구조, 저장소 상태를 확인하는 개발 도구다.

Frontend Agent와 Review Agent는 Browser Debugging 절차를 RAG 문서에서 검색할 수 있어야 한다.

---

### [핵심]

- Browser DevTools
- Console Tab
- Network Tab
- Elements Tab
- Application Tab
- Sources Tab
- Debugging
- API Debugging
- DOM Debugging
- Storage Debugging

---

### [실무]

DevTools 주요 탭:

| 탭          | 용도                                      |
| ----------- | ----------------------------------------- |
| Console     | JavaScript 오류, 로그 확인                |
| Network     | API 요청 / 응답 확인                      |
| Elements    | DOM 구조와 CSS 확인                       |
| Application | localStorage, sessionStorage, cookie 확인 |
| Sources     | breakpoint 기반 코드 디버깅               |

Debugging 기본 Flow:

```text
Problem Reproduce
→ Console Error Check
→ Network Request Check
→ DOM / Elements Check
→ State or Storage Check
→ Source Code Trace
→ Fix
→ Retest
```

주의:

- Console 오류만 보지 않는다.
- API 문제는 Network 탭을 반드시 확인한다.
- DOM 문제는 Elements 탭에서 실제 요소를 확인한다.
- Token이나 민감정보 저장 여부는 Application 탭에서 확인한다.
- Sources breakpoint는 실행 흐름 확인에 유용하다.

---

### [FAQ]

Q. Browser DevTools는 뭐야?
A. Frontend 코드를 디버깅하고 요청, DOM, 저장소, 오류를 확인하는 개발 도구다.

Q. API 요청 오류는 어디서 확인해?
A. Network 탭에서 URL, Method, Payload, Status Code, Response Body를 확인한다.

Q. JavaScript 오류는 어디서 확인해?
A. Console 탭에서 확인한다.

Q. DOM 구조와 CSS는 어디서 확인해?
A. Elements 탭에서 확인한다.

---

# 9. Console Debugging

## 9.1 Console Error Rules

### [개념]

Console은 JavaScript 오류, 경고, 개발자 로그를 확인하는 DevTools 탭이다.

Frontend 오류 분석의 시작점이다.

---

### [핵심]

- Console
- console.error
- console.warn
- console.log
- TypeError
- ReferenceError
- SyntaxError
- stack trace
- line number
- debugging

---

### [실무]

Console 확인 기준:

```text
Error Type
→ Error Message
→ File Name
→ Line Number
→ Stack Trace
→ Related Code
→ Reproduce
```

흔한 오류:

```text
TypeError: Cannot read properties of undefined
ReferenceError: variable is not defined
SyntaxError: Unexpected token
```

주의:

- Error Message를 그대로 무시하지 않는다.
- line number 근처 코드를 확인한다.
- minified build에서는 source map 필요 가능
- console.log 남용은 피한다.
- 민감정보 로그 출력 금지
- Console 오류와 Network 오류를 함께 확인한다.

---

### [FAQ]

Q. Console은 어디에 써?
A. JavaScript 오류, 경고, 개발자 로그를 확인할 때 사용한다.

Q. Console Error에서 무엇을 봐야 해?
A. Error type, message, file name, line number, stack trace를 확인한다.

Q. TypeError는 보통 왜 발생해?
A. null 또는 undefined 값에서 property나 method를 사용하려 할 때 자주 발생한다.

Q. ReferenceError는 보통 왜 발생해?
A. 선언되지 않은 변수나 잘못된 이름을 사용했을 때 발생한다.

---

## 9.2 Console Log Rules

### [개념]

Console Log는 코드 실행 중 값과 흐름을 확인하기 위해 사용하는 디버깅 출력이다.

대표적으로 `console.log`, `console.warn`, `console.error`가 있다.

---

### [핵심]

- console.log
- console.warn
- console.error
- debug value
- execution flow
- temporary log
- sensitive data caution
- production cleanup

---

### [실무]

디버깅 로그 예:

```javascript
console.log("search condition:", searchCondition);
console.warn("Empty response content");
console.error("Festival request failed:", error);
```

주의:

- console.log는 임시 디버깅 용도로 사용한다.
- 운영 배포 전 불필요한 log 제거
- Token, Password, 개인정보, 결제정보 출력 금지
- 로그 메시지에는 맥락을 포함한다.
- 객체 전체 출력 시 민감정보 포함 여부 확인
- console.error는 실제 오류에 사용한다.

---

### [FAQ]

Q. console.log는 언제 써?
A. 코드 실행 흐름이나 변수 값을 임시로 확인할 때 사용한다.

Q. console.error는 언제 써?
A. API 실패나 예외처럼 오류 맥락을 남길 때 사용한다.

Q. 운영 코드에 console.log가 남아도 돼?
A. 불필요한 로그는 제거하는 것이 좋다.

Q. console.log에 민감정보를 찍어도 돼?
A. 안 된다. Token, Password, 개인정보, 결제정보는 출력하면 안 된다.

---

# 10. Network Debugging

## 10.1 Network Tab Rules

### [개념]

Network Tab은 Browser에서 발생한 HTTP 요청과 응답을 확인하는 DevTools 탭이다.

API 연동 오류를 분석할 때 가장 중요한 도구다.

---

### [핵심]

- Network Tab
- Request URL
- Request Method
- Status Code
- Query String Parameters
- Request Headers
- Request Payload
- Response Body
- Preview
- Timing
- CORS

---

### [실무]

Network Debugging Flow:

```text
Request Trigger
→ Network Tab
→ Request URL
→ Method
→ Query Parameters
→ Headers
→ Payload
→ Status Code
→ Response Body
→ Frontend Processing
```

확인 항목:

- 요청이 실제로 발생했는가?
- URL이 올바른가?
- Method가 API 스펙과 일치하는가?
- Query Parameter가 올바른가?
- Request Payload가 Backend DTO와 일치하는가?
- Content-Type Header가 맞는가?
- Authorization Header가 포함되었는가?
- Status Code가 무엇인가?
- Response Body 구조가 Normalize Function과 일치하는가?

주의:

- Console만 보고 API 문제를 판단하지 않는다.
- 요청 자체가 없으면 Event Handler나 함수 호출 문제일 수 있다.
- 404는 URL 또는 Backend Routing 문제일 수 있다.
- 400은 Request Body 또는 Validation 문제일 수 있다.
- 401 / 403은 인증 / 권한 문제일 수 있다.
- CORS는 Console과 Network를 함께 확인한다.

---

### [FAQ]

Q. Network Tab은 뭐야?
A. Browser에서 발생한 HTTP 요청과 응답을 확인하는 DevTools 탭이다.

Q. API 요청이 안 되는 것 같으면 무엇부터 봐?
A. Network 탭에서 요청이 실제 발생했는지부터 확인한다.

Q. 400 오류에서는 무엇을 확인해?
A. Request Payload, Query Parameter, Backend DTO 필드명, Validation Error를 확인한다.

Q. 401 오류에서는 무엇을 확인해?
A. Authorization Header, Token 존재 여부, Token 만료 여부를 확인한다.

---

## 10.2 Payload and Response Debugging Rules

### [개념]

Payload and Response Debugging은 Frontend가 서버에 보낸 데이터와 서버가 반환한 데이터를 비교해 API 연동 오류를 찾는 과정이다.

---

### [핵심]

- Payload Debugging
- Response Debugging
- Request Body
- Query Parameter
- DTO field
- Response Structure
- data content
- error body
- normalize function

---

### [실무]

Payload 확인:

```text
Network Tab
→ Request
→ Payload
→ Request Body Field
→ Backend DTO Field
→ Type Check
```

Response 확인:

```text
Network Tab
→ Response
→ data
→ content
→ page info
→ error message
→ Frontend Normalize Function
```

주의:

- Request Body field 이름이 Backend DTO와 맞는지 확인
- number가 string으로 전달되는지 확인
- null / undefined 필드 처리 확인
- Response 구조가 예상과 같은지 확인
- Error Response 구조는 성공 응답과 다를 수 있음
- Normalize Function이 실제 Response와 맞는지 확인

---

### [FAQ]

Q. Payload Debugging은 뭐야?
A. Frontend가 서버에 보낸 Request Body나 Query Parameter를 확인하는 과정이다.

Q. Payload와 Backend DTO를 비교하는 이유는?
A. 필드명이나 타입이 다르면 400 오류나 Validation 오류가 발생할 수 있기 때문이다.

Q. Response Debugging은 뭐야?
A. 서버가 반환한 데이터 구조를 확인하고 Frontend 처리 코드와 맞는지 비교하는 과정이다.

Q. Normalize Function 오류는 어떻게 찾을 수 있어?
A. Network Response Body와 Normalize Function이 접근하는 경로를 비교하면 찾을 수 있다.

---

# 11. Elements Debugging

## 11.1 Elements Tab Rules

### [개념]

Elements Tab은 Browser에 실제 렌더링된 DOM 구조와 CSS 상태를 확인하는 DevTools 탭이다.

DOM 선택 실패, class 적용 오류, layout 문제를 확인할 때 사용한다.

---

### [핵심]

- Elements Tab
- DOM structure
- CSS rule
- class name
- style
- computed style
- selector check
- hidden element
- disabled attribute

---

### [실무]

Elements 확인 항목:

- 실제 DOM 요소가 존재하는가?
- selector와 class 이름이 일치하는가?
- classList 변경이 반영되었는가?
- disabled attribute가 적용되었는가?
- hidden class가 적용되었는가?
- CSS 우선순위 문제는 없는가?
- 텍스트가 textContent로 반영되었는가?

Debug Flow:

```text
Expected UI State
→ Elements Tab
→ DOM Element Exists
→ Class / Attribute Check
→ CSS Rule Check
→ Computed Style Check
→ JavaScript Update Check
```

주의:

- DOM 선택자가 실제 HTML과 일치하는지 확인
- CSS class 오타 확인
- display none, visibility hidden, opacity 확인
- disabled 상태 확인
- React 전환 후에는 직접 DOM 수정이 덮어써질 수 있음

---

### [FAQ]

Q. Elements Tab은 뭐야?
A. 실제 렌더링된 DOM 구조와 CSS 상태를 확인하는 DevTools 탭이다.

Q. DOM 선택 실패는 어디서 확인해?
A. Elements 탭에서 실제 요소와 selector 이름을 확인한다.

Q. class가 적용됐는데 화면이 안 바뀌면 무엇을 봐?
A. CSS rule, 우선순위, computed style, 다른 class 충돌을 확인한다.

Q. 버튼 disabled 상태는 어디서 확인해?
A. Elements 탭에서 disabled attribute나 property 반영 여부를 확인한다.

---

# 12. Application Storage Debugging

## 12.1 localStorage and sessionStorage Debugging Rules

### [개념]

Application Tab은 Browser Storage, Cookie, Cache 등을 확인하는 DevTools 탭이다.

Frontend 인증, theme 설정, 임시 저장 데이터 확인에 사용할 수 있다.

---

### [핵심]

- Application Tab
- localStorage
- sessionStorage
- cookie
- storage debugging
- token storage
- JSON parse
- sensitive data caution
- authentication debugging

---

### [실무]

확인 항목:

- localStorage에 값이 저장되었는가?
- sessionStorage에 값이 저장되었는가?
- key 이름이 올바른가?
- JSON 문자열이 유효한가?
- Token이 저장되어 있는가?
- 만료된 Token이 남아 있는가?
- 로그아웃 시 저장소가 정리되는가?

주의:

- localStorage에 민감정보 저장은 보안 위험이 있다.
- Token 저장 방식은 프로젝트 인증 정책을 따른다.
- JSON.parse 실패 가능성을 고려한다.
- 로그아웃 시 인증 관련 Storage 정리 필요
- Storage 값과 Authorization Header 연결을 확인한다.
- 민감정보를 캡처하거나 공유하지 않는다.

---

### [FAQ]

Q. Application Tab은 어디에 써?
A. localStorage, sessionStorage, cookie 같은 Browser 저장소를 확인할 때 사용한다.

Q. Token 저장 여부는 어디서 확인해?
A. Application 탭의 Storage 영역에서 확인할 수 있다.

Q. localStorage에 Token을 저장해도 안전해?
A. 보안 위험이 있으므로 프로젝트 인증 정책에 따라 신중히 결정해야 한다.

Q. 로그아웃 후 무엇을 확인해야 해?
A. 인증 관련 Storage 값이 정리되었는지 확인해야 한다.

---

# 13. Sources Debugging

## 13.1 Breakpoint Rules

### [개념]

Breakpoint는 JavaScript 실행을 특정 줄에서 멈추고 변수 값과 실행 흐름을 확인하는 디버깅 기능이다.

Sources Tab에서 설정할 수 있다.

---

### [핵심]

- Sources Tab
- breakpoint
- step over
- step into
- step out
- call stack
- scope variables
- execution flow
- debugging

---

### [실무]

Breakpoint Debugging Flow:

```text
Open Sources
→ Set Breakpoint
→ Reproduce Event
→ Pause Execution
→ Check Variables
→ Step Over / Into
→ Check Call Stack
→ Find Cause
```

사용 상황:

- Event Handler가 실행되는지 확인
- API 함수 호출 순서 확인
- 조건문 분기 확인
- 변수 값 변화 확인
- async function 흐름 확인
- return 값 확인

주의:

- minified build에서는 디버깅이 어려울 수 있다.
- 개발 모드와 source map이 필요할 수 있다.
- breakpoint 위치가 실제 실행되는 코드인지 확인
- async function에서는 await 전후 흐름을 구분한다.
- 조건부 breakpoint를 활용할 수 있다.

---

### [FAQ]

Q. Breakpoint는 뭐야?
A. JavaScript 실행을 특정 줄에서 멈추고 상태를 확인하는 디버깅 기능이다.

Q. Breakpoint는 언제 써?
A. Event Handler 실행 여부, 변수 값, 조건 분기, 함수 호출 순서를 확인할 때 사용한다.

Q. Step Over는 뭐야?
A. 현재 줄을 실행하고 다음 줄로 넘어가는 디버깅 동작이다.

Q. Call Stack은 왜 확인해?
A. 어떤 함수 호출 흐름으로 현재 코드에 도달했는지 알 수 있기 때문이다.

---

# 14. Debugging Flow by Symptom

## 14.1 API Not Working Rules

### [개념]

API가 동작하지 않을 때는 Console 오류만 보는 것이 아니라 Event 발생 여부, Network 요청, Status Code, Response Body, Frontend 처리 순서로 확인해야 한다.

---

### [핵심]

- API Not Working
- event trigger
- Network request
- URL check
- Method check
- Payload check
- Status Code
- Response Body
- CORS
- Error Handling

---

### [실무]

확인 Flow:

```text
Button Click or Submit
→ Event Handler 실행 확인
→ API Function 호출 확인
→ Network 요청 발생 확인
→ URL / Method 확인
→ Headers / Payload 확인
→ Status Code 확인
→ Response Body 확인
→ Frontend Normalize 확인
```

상황별 의심:

| 증상             | 우선 확인                                       |
| ---------------- | ----------------------------------------------- |
| 요청이 아예 없음 | Event Handler, addEventListener, preventDefault |
| 404              | URL, Backend Mapping, path variable             |
| 400              | Payload, DTO field, Validation                  |
| 401              | Authorization Header, Token                     |
| 403              | 권한, Role                                      |
| 500              | Backend Error, Request 조건                     |
| CORS             | Backend CORS 설정, Origin, Header               |

주의:

- 요청이 없는 문제와 요청 실패 문제를 구분한다.
- API 함수가 호출되는지 먼저 확인한다.
- Network 탭에서 실제 요청을 기준으로 판단한다.
- Response Body와 Frontend 응답 처리 코드를 비교한다.

---

### [FAQ]

Q. API가 안 될 때 무엇부터 확인해?
A. Event Handler가 실행되는지, Network 요청이 발생하는지부터 확인한다.

Q. Network에 요청이 없으면 무엇을 의심해?
A. Event Listener 등록 실패, selector null, preventDefault 누락, 함수 호출 누락을 의심한다.

Q. 404가 나오면 무엇을 확인해?
A. Request URL, Backend Mapping, Path Variable, API prefix를 확인한다.

Q. 400이 나오면 무엇을 확인해?
A. Request Payload, Query Parameter, Backend DTO 필드명, Validation Error를 확인한다.

---

## 14.2 UI Not Updating Rules

### [개념]

UI가 갱신되지 않는 문제는 데이터가 없는 문제, DOM 선택 실패, 렌더 함수 미호출, class 적용 오류, 비동기 순서 문제로 발생할 수 있다.

---

### [핵심]

- UI Not Updating
- data check
- render function
- DOM selection
- classList
- textContent
- async order
- state update
- React readiness

---

### [실무]

확인 Flow:

```text
Data Exists
→ Render Function Called
→ DOM Element Selected
→ DOM Update Code Runs
→ Elements Tab Check
→ CSS / Class Check
→ Async Order Check
```

DOM 기반 확인:

```javascript
const listElement = document.querySelector(".festival-list");

console.log("listElement:", listElement);
console.log("festivals:", festivals);
```

주의:

- 데이터가 실제로 있는지 확인
- 렌더 함수가 호출되는지 확인
- selector가 실제 DOM과 일치하는지 확인
- DOM 요소가 null인지 확인
- CSS hidden 상태인지 확인
- async 응답 전에 render가 호출되는지 확인

---

### [FAQ]

Q. UI가 안 바뀌면 무엇부터 확인해?
A. 데이터가 있는지, 렌더 함수가 호출되는지, DOM 요소 선택이 성공했는지 확인한다.

Q. DOM 요소가 있는데 화면에 안 보이면 무엇을 봐?
A. CSS class, display, visibility, opacity, computed style을 확인한다.

Q. 데이터는 있는데 목록이 안 나오면 무엇을 의심해?
A. render 함수 미호출, selector 오류, innerHTML/textContent 초기화 문제, Array Method 오류를 의심한다.

---

## 14.3 Undefined Error Rules

### [개념]

Undefined Error는 값이 존재하지 않는데 property나 method에 접근할 때 발생하는 오류다.

대표 오류는 `Cannot read properties of undefined`다.

---

### [핵심]

- Undefined Error
- Cannot read properties of undefined
- optional chaining
- null check
- API response structure
- Array.isArray
- default value
- defensive access

---

### [실무]

문제 코드:

```javascript
const title = response.data.content[0].title;
```

개선:

```javascript
const title = response?.data?.content?.[0]?.title ?? "제목 없음";
```

목록 처리:

```javascript
const content = response?.data?.content;
const festivals = Array.isArray(content) ? content : [];
```

확인 Flow:

```text
Error Line Check
→ Access Target Check
→ API Response Structure Check
→ null / undefined 가능성 확인
→ optional chaining 적용
→ default value 적용
```

주의:

- 응답 구조를 Network 탭에서 확인한다.
- 중첩 property 접근 전 null 가능성을 고려한다.
- 배열인지 확인 후 map / forEach 사용
- 기본값을 설정한다.
- undefined가 발생한 근본 원인을 숨기지 않는다.

---

### [FAQ]

Q. Cannot read properties of undefined는 왜 발생해?
A. undefined 값에서 property나 method를 읽으려고 했기 때문이다.

Q. Undefined Error를 줄이려면 어떻게 해?
A. optional chaining, null check, Array.isArray, 기본값 처리를 사용한다.

Q. API 응답 구조는 어디서 확인해?
A. Network 탭의 Response Body에서 확인한다.

Q. optional chaining만 쓰면 충분해?
A. 오류는 줄일 수 있지만 데이터 구조 검증과 기본값 처리가 함께 필요하다.

---

# 15. Linting and Formatting

## 15.1 ESLint Rules

### [개념]

ESLint는 JavaScript 코드의 오류 가능성, 스타일 위반, 안티패턴을 검사하는 도구다.

Frontend Agent와 Review Agent는 ESLint 경고를 코드 품질 신호로 활용할 수 있다.

---

### [핵심]

- ESLint
- linting
- code quality
- unused variable
- no undef
- no console
- eqeqeq
- no var
- consistent return
- code review

---

### [실무]

ESLint가 잡는 대표 문제:

- 선언하지 않은 변수 사용
- 사용하지 않는 변수
- `==` 사용
- `var` 사용
- return 누락
- dependency 누락
- console 남용
- unreachable code

Review 기준:

```text
ESLint Warning
→ Code Smell Check
→ Actual Bug Risk Check
→ Fix or Intentional Ignore
→ Final Review
```

주의:

- ESLint 경고를 무조건 무시하지 않는다.
- 프로젝트 규칙과 충돌하면 config를 확인한다.
- 불필요한 disable 주석을 남용하지 않는다.
- 자동 수정 가능한 항목은 formatter와 함께 처리한다.
- Review Agent는 lint warning을 우선 검토 신호로 삼는다.

---

### [FAQ]

Q. ESLint는 뭐야?
A. JavaScript 코드의 오류 가능성과 스타일 위반을 검사하는 도구다.

Q. ESLint 경고는 무시해도 돼?
A. 무조건 무시하면 안 된다. 실제 오류 가능성이 있는지 확인해야 한다.

Q. ESLint는 어떤 문제를 잡아?
A. 미선언 변수, 미사용 변수, == 사용, var 사용, return 누락 같은 문제를 잡을 수 있다.

Q. disable 주석을 써도 돼?
A. 필요할 때만 제한적으로 사용하고 이유가 명확해야 한다.

---

## 15.2 Prettier Rules

### [개념]

Prettier는 JavaScript 코드 Formatting을 자동으로 정리하는 도구다.

들여쓰기, 줄바꿈, 따옴표, semicolon 같은 스타일을 일관되게 맞춘다.

---

### [핵심]

- Prettier
- formatting
- code style
- indentation
- line break
- semicolon
- quotes
- consistent style
- auto format

---

### [실무]

Prettier 적용 대상:

- 들여쓰기
- 줄바꿈
- object / array formatting
- function parameter 줄바꿈
- semicolon
- quote style
- trailing comma

주의:

- Formatting 논쟁을 줄인다.
- 코드 의미를 바꾸는 도구가 아니다.
- ESLint와 역할이 다르다.
- 저장 시 자동 format 설정 가능
- 팀 설정을 따른다.
- RAG 문서 예제는 일관된 Formatting을 유지한다.

---

### [FAQ]

Q. Prettier는 뭐야?
A. JavaScript 코드 Formatting을 자동으로 정리하는 도구다.

Q. Prettier와 ESLint 차이는 뭐야?
A. Prettier는 Formatting 중심이고 ESLint는 코드 품질과 오류 가능성 검사 중심이다.

Q. Prettier가 코드 의미를 바꿔?
A. 보통 의미를 바꾸지 않고 표시 형식만 정리한다.

Q. RAG 문서 예제에도 Formatting이 중요해?
A. 중요하다. 일관된 예제는 Retrieval과 코드 생성 품질을 높인다.

---

# 16. Module Error Debugging

## 16.1 Import Export Error Rules

### [개념]

Import Export Error는 Module 간 export 이름, import 경로, default / named export 방식이 맞지 않아 발생하는 오류다.

---

### [핵심]

- Import Error
- Export Error
- named export mismatch
- default export mismatch
- module path error
- file name case
- circular dependency
- build error

---

### [실무]

흔한 오류:

```text
Module has no exported member
Attempted import error
Cannot resolve module
The requested module does not provide an export named
```

확인 Flow:

```text
Error Message
→ Import Statement
→ Export Statement
→ File Path
→ File Name Case
→ Default / Named Export Type
→ Circular Dependency
```

Named Export 확인:

```javascript
export function fetchFestivals() {}
```

올바른 import:

```javascript
import { fetchFestivals } from "./festivalApi.js";
```

Default Export 확인:

```javascript
export default festivalApi;
```

올바른 import:

```javascript
import festivalApi from "./festivalApi.js";
```

주의:

- named export는 중괄호 필요
- default export는 중괄호 없이 import
- 파일명 대소문자 차이는 환경에 따라 오류 발생
- 경로 depth를 정확히 확인
- 순환 참조는 undefined 문제를 만들 수 있음

---

### [FAQ]

Q. Import Export Error는 왜 발생해?
A. export 이름, import 방식, 파일 경로, default / named export 방식이 맞지 않을 때 발생한다.

Q. Named Export는 어떻게 import해?
A. 중괄호를 사용해 `import { name } from "./module.js";` 형식으로 import한다.

Q. Default Export는 어떻게 import해?
A. 중괄호 없이 `import name from "./module.js";` 형식으로 import한다.

Q. Cannot resolve module은 무엇을 확인해야 해?
A. 파일 경로, 파일명, 확장자, 대소문자, 실제 파일 존재 여부를 확인해야 한다.

---

# 17. Module Error Handling Debugging Practical Example

## 17.1 API Module Debug Example

### [개념]

Module, Error Handling, Debugging Practical Example은 API Module 분리, Error 처리, Network Debugging, User Message 분리를 함께 보여줘야 한다.

이 예제는 Frontend Agent가 코드 분리와 오류 처리를 함께 생성하는 기준이다.

---

### [핵심]

- API Module
- requestJson
- named export
- import
- try catch finally
- user message
- developer log
- Network debugging
- normalize function

---

### [실무]

requestJson.js:

```javascript
export async function requestJson(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  if (response.status === 204) {
    return null;
  }

  return await response.json();
}
```

festivalApi.js:

```javascript
import { requestJson } from "./requestJson.js";

export function fetchFestivals() {
  return requestJson("/api/festivals");
}

export function searchFestivals(keyword) {
  const params = new URLSearchParams();

  if (keyword?.trim()) {
    params.set("keyword", keyword.trim());
  }

  return requestJson(`/api/festivals/search?${params.toString()}`);
}
```

festivalMapper.js:

```javascript
export function normalizeFestivalList(responseBody) {
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

page.js:

```javascript
import { searchFestivals } from "./api/festivalApi.js";
import { normalizeFestivalList } from "./mapper/festivalMapper.js";

async function handleSearch(keyword) {
  setLoading(true);
  setError("");

  try {
    const responseBody = await searchFestivals(keyword);
    const festivals = normalizeFestivalList(responseBody);

    renderFestivals(festivals);
  } catch (error) {
    console.error("Festival search failed:", error);
    setError("축제 검색 중 오류가 발생했습니다.");
  } finally {
    setLoading(false);
  }
}
```

Debugging 기준:

```text
Import Error
→ export / import 방식 확인

API Error
→ Network Tab URL / Method / Status 확인

Response Mapping Error
→ Response Body와 normalize function 비교

UI Error
→ render function 호출과 DOM selection 확인
```

---

### [FAQ]

Q. API Module 예제에서 requestJson을 분리한 이유는?
A. response.ok, 204 처리, JSON parsing 같은 공통 요청 처리를 재사용하기 위해서다.

Q. normalizeFestivalList를 별도 파일로 분리한 이유는?
A. API 원본 응답과 UI 데이터 구조를 분리하기 위해서다.

Q. API 오류가 발생하면 어디를 확인해야 해?
A. Network 탭에서 URL, Method, Status Code, Response Body를 확인한다.

Q. Module import 오류가 발생하면 무엇을 확인해야 해?
A. export 방식, import 방식, 파일 경로, 파일명 대소문자를 확인해야 한다.

---

# 18. Module Error Debugging Common Mistakes

## 18.1 Common Mistakes

### [개념]

Module, Error Handling, Browser Debugging 실수는 import 실패, API 오류 은폐, 사용자 메시지 부재, Network 분석 누락, 민감정보 노출로 이어질 수 있다.

Review Agent는 export / import 방식, Error 처리, 로그 보안, DevTools 확인 절차를 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- 모든 코드를 한 파일에 작성
- API 함수와 UI 로직 혼합
- Utility Module에 Side Effect 포함
- named export를 default import로 가져옴
- default export를 named import로 가져옴
- import 경로 오타
- 파일명 대소문자 불일치
- 순환 import 발생
- catch 비워두기
- 사용자 메시지 없이 console.error만 출력
- stack trace를 사용자에게 표시
- Token, Password, 개인정보 console.log 출력
- loading cleanup 누락
- Network Tab 확인 없이 추측
- Payload와 Backend DTO 비교 누락
- Response Body와 Normalize Function 비교 누락
- ESLint 경고 무시
- Prettier Formatting 불일치

---

### [실무]

Review Flow:

```text
Module Error Debugging Review
→ File Responsibility Check
→ export / import Check
→ API / UI Separation Check
→ Utility Pure Function Check
→ Error Handling Check
→ User Message Check
→ Developer Log Security Check
→ Loading Cleanup Check
→ DevTools Debug Flow Check
→ ESLint / Prettier Check
```

나쁜 예:

```javascript
import requestJson from "./requestJson.js";

try {
  const data = await requestJson("/api/festivals");
} catch (error) {}
```

개선 예:

```javascript
import { requestJson } from "./requestJson.js";

try {
  const data = await requestJson("/api/festivals");

  renderFestivals(data);
} catch (error) {
  console.error("Festival load failed:", error);
  showError("축제 목록을 불러오지 못했습니다.");
}
```

주의:

- export 방식과 import 방식을 일치시킨다.
- catch를 비워두지 않는다.
- 사용자 메시지와 개발자 로그를 분리한다.
- Network Tab을 기준으로 API 문제를 분석한다.
- 민감정보 로그 출력 금지
- Lint / Formatting 경고를 검토한다.

---

### [FAQ]

Q. Module에서 가장 흔한 실수는 뭐야?
A. named export와 default export를 혼동하거나 import 경로를 잘못 작성하는 것이다.

Q. Error Handling에서 가장 흔한 실수는 뭐야?
A. catch를 비워두거나 사용자 메시지 없이 오류를 숨기는 것이다.

Q. Debugging에서 가장 흔한 실수는 뭐야?
A. Network Tab을 확인하지 않고 Console Error만 보고 추측하는 것이다.

Q. Review Agent는 무엇을 우선 검토해야 해?
A. export / import 일치, API / UI 분리, Error Handling, 민감정보 로그, Network Debug 절차를 우선 검토해야 한다.

---

# 19. Module Error Debugging Checklist

## 19.1 Document Quality Checklist

### [개념]

Module, Error Handling, Browser Debugging 문서는 Frontend Agent가 코드를 파일 단위로 분리하고 오류를 안전하게 처리하며 DevTools 기반으로 문제를 분석하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] Module 개념이 포함되었는가?
- [ ] export 설명이 포함되었는가?
- [ ] import 설명이 포함되었는가?
- [ ] Named Export 설명이 포함되었는가?
- [ ] Default Export 설명이 포함되었는가?
- [ ] API Module 기준이 포함되었는가?
- [ ] Utility Module 기준이 포함되었는가?
- [ ] Constants Module 기준이 포함되었는가?
- [ ] Error Handling 개념이 포함되었는가?
- [ ] throw Error 설명이 포함되었는가?
- [ ] try / catch / finally 설명이 포함되었는가?
- [ ] Validation Error 설명이 포함되었는가?
- [ ] Network Error 설명이 포함되었는가?
- [ ] Runtime Error 설명이 포함되었는가?
- [ ] User Message와 Developer Log 구분이 포함되었는가?
- [ ] Browser DevTools 설명이 포함되었는가?
- [ ] Console Debugging 기준이 포함되었는가?
- [ ] Network Debugging 기준이 포함되었는가?
- [ ] Elements Debugging 기준이 포함되었는가?
- [ ] Application Storage Debugging 기준이 포함되었는가?
- [ ] Sources Breakpoint 설명이 포함되었는가?
- [ ] 증상별 Debugging Flow가 포함되었는가?
- [ ] ESLint 설명이 포함되었는가?
- [ ] Prettier 설명이 포함되었는가?
- [ ] Import Export Error 기준이 포함되었는가?
- [ ] 실무형 Module / Error / Debugging 예제가 포함되었는가?
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
→ Module Syntax Check
→ Architecture Separation Check
→ Error Handling Check
→ User Message / Developer Log Check
→ Debugging Flow Check
→ Lint / Formatting Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part08_Fetch_JSON_API_Response
→ JavaScript_Foundation_Part09_Module_Error_Debugging
→ JavaScript_Foundation_Part10_Practical_Security_Review
```

---

### [FAQ]

Q. Module Error Debugging 문서 검수에서 가장 중요한 것은 뭐야?
A. export / import 일치, 파일 책임 분리, Error Handling, User Message와 Developer Log 분리, Network Debugging 절차다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React 프로젝트의 Component 분리, API Layer, Hook 분리, Error UI, DevTools Debugging의 기반이 된다.

Q. 다음 Part와 어떻게 연결돼?
A. Part09는 코드 분리와 오류 분석 기준을 만들고, Part10은 Practical Logic, Security, Troubleshooting, Review Checklist로 JavaScript Foundation을 마무리한다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Module이 뭐야?
A. 코드를 파일 단위로 분리하고 필요한 값만 export / import 해서 사용하는 구조다.

Q. Module을 쓰는 이유는 뭐야?
A. 코드 책임을 분리하고 재사용성과 유지보수성을 높이기 위해 사용한다.

Q. Frontend에서 Module은 어디에 많이 써?
A. API 함수, 유틸 함수, 검증 함수, 상수, 화면 로직 분리에 많이 사용한다.

Q. export는 뭐야?
A. 현재 Module의 값을 다른 Module에서 사용할 수 있도록 내보내는 문법이다.

Q. import는 뭐야?
A. 다른 Module에서 export한 값을 현재 Module로 가져오는 문법이다.

Q. Named Export는 뭐야?
A. 이름이 있는 여러 값을 하나의 Module에서 export하는 방식이다.

Q. Named Export는 import할 때 어떻게 써?
A. import { name } from "./module.js"; 형식으로 가져온다.

Q. Default Export는 뭐야?
A. Module에서 기본값 하나를 export하는 방식이다.

Q. 하나의 파일에 default export를 여러 개 쓸 수 있어?
A. 없다. 하나의 Module에는 default export가 하나만 가능하다.

Q. Named Export와 Default Export 중 뭐가 좋아?
A. 상황과 팀 컨벤션에 따른다. 여러 유틸 함수는 named export, 대표값 하나는 default export가 적합하다.

Q. API Module은 뭐야?
A. Backend API 호출 함수를 Domain별로 분리한 Module이다.

Q. API Module을 쓰는 이유는 뭐야?
A. endpoint, fetch 옵션, 응답 처리, 오류 처리를 UI 코드와 분리하기 위해서다.

Q. requestJson은 어떤 책임을 가져?
A. fetch 실행, response.ok 확인, 204 처리, JSON parsing 같은 공통 요청 처리를 담당한다.

Q. Utility Module은 뭐야?
A. 여러 곳에서 재사용되는 순수 함수나 보조 함수를 모아둔 Module이다.

Q. Utility Module에는 무엇을 넣어?
A. format, validation, query string 생성, className 병합 같은 재사용 함수를 넣을 수 있다.

Q. Utility Module에 API 호출을 넣어도 돼?
A. 지양한다. API 호출은 API Module에 두는 것이 좋다.

Q. Constants Module은 뭐야?
A. 여러 파일에서 공통으로 사용하는 변하지 않는 값을 모아두는 Module이다.

Q. Constants Module에는 무엇을 넣어?
A. API base URL, 기본 이미지 경로, page size, status 값 같은 상수를 넣을 수 있다.

Q. Error Handling이 뭐야?
A. 코드 실행 중 발생할 수 있는 오류를 감지하고 적절히 처리하는 과정이다.

Q. Frontend에서 어떤 오류를 처리해야 해?
A. API 오류, 입력 오류, JSON 파싱 오류, DOM 접근 오류, 비동기 오류를 처리해야 한다.

Q. catch를 비워둬도 돼?
A. 안 된다. 로그, 사용자 메시지, fallback 처리 중 하나는 해야 한다.

Q. throw는 뭐야?
A. 코드 실행 중 Error를 발생시키는 문법이다.

Q. throw new Error를 쓰는 이유는 뭐야?
A. 명확한 Error 객체와 메시지를 만들어 catch에서 처리하기 위해서다.

Q. async function 내부에서 throw하면 어떻게 돼?
A. rejected Promise가 되어 try / catch 또는 catch로 처리할 수 있다.

Q. try / catch / finally는 뭐야?
A. 오류 발생 가능 코드, 오류 처리, 정리 작업을 분리해 실행하는 문법이다.

Q. finally는 언제 실행돼?
A. 성공과 실패 모두에서 마지막에 실행된다.

Q. loading 해제는 어디에서 하는 게 좋아?
A. finally에서 처리하는 것이 안전하다.

Q. Validation Error는 뭐야?
A. 사용자가 입력한 값이 요구 조건을 만족하지 않을 때 발생하는 오류다.

Q. Network Error는 뭐야?
A. 네트워크 연결 문제나 요청 차단으로 API 요청이 정상 완료되지 못한 오류다.

Q. Network Error와 HTTP Error는 같아?
A. 아니다. Network Error는 응답 자체가 실패한 경우이고, HTTP Error는 서버가 오류 status로 응답한 경우다.

Q. Runtime Error는 뭐야?
A. 코드 실행 중 발생하는 오류다.

Q. Cannot read properties of undefined 오류는 왜 나?
A. undefined 값에서 property나 method를 읽으려고 했기 때문이다.

Q. User Message는 뭐야?
A. 사용자에게 보여주는 오류 또는 안내 문구다.

Q. 사용자에게 stack trace를 보여줘도 돼?
A. 안 된다. 사용자가 이해할 수 있는 짧은 안내 문구를 보여줘야 한다.

Q. Developer Log는 뭐야?
A. 개발자가 오류 원인을 분석하기 위해 남기는 로그다.

Q. console.error는 언제 써?
A. API 실패나 예외처럼 오류 맥락을 남길 때 사용한다.

Q. console.log에 Token을 찍어도 돼?
A. 안 된다. Token, Password, 개인정보, 결제정보는 로그에 출력하면 안 된다.

Q. Browser DevTools는 뭐야?
A. Frontend 코드를 디버깅하고 요청, DOM, 저장소, 오류를 확인하는 개발 도구다.

Q. JavaScript 오류는 어디서 확인해?
A. Console 탭에서 확인한다.

Q. API 요청 오류는 어디서 확인해?
A. Network 탭에서 URL, Method, Payload, Status Code, Response Body를 확인한다.

Q. DOM 구조와 CSS는 어디서 확인해?
A. Elements 탭에서 확인한다.

Q. Console Error에서 무엇을 봐야 해?
A. Error type, message, file name, line number, stack trace를 확인한다.

Q. TypeError는 보통 왜 발생해?
A. null 또는 undefined 값에서 property나 method를 사용하려 할 때 자주 발생한다.

Q. Network Tab은 뭐야?
A. Browser에서 발생한 HTTP 요청과 응답을 확인하는 DevTools 탭이다.

Q. API 요청이 안 되는 것 같으면 무엇부터 봐?
A. Network 탭에서 요청이 실제 발생했는지부터 확인한다.

Q. 400 오류에서는 무엇을 확인해?
A. Request Payload, Query Parameter, Backend DTO 필드명, Validation Error를 확인한다.

Q. 401 오류에서는 무엇을 확인해?
A. Authorization Header, Token 존재 여부, Token 만료 여부를 확인한다.

Q. Payload Debugging은 뭐야?
A. Frontend가 서버에 보낸 Request Body나 Query Parameter를 확인하는 과정이다.

Q. Response Debugging은 뭐야?
A. 서버가 반환한 데이터 구조를 확인하고 Frontend 처리 코드와 맞는지 비교하는 과정이다.

Q. Elements Tab은 뭐야?
A. 실제 렌더링된 DOM 구조와 CSS 상태를 확인하는 DevTools 탭이다.

Q. Application Tab은 어디에 써?
A. localStorage, sessionStorage, cookie 같은 Browser 저장소를 확인할 때 사용한다.

Q. Breakpoint는 뭐야?
A. JavaScript 실행을 특정 줄에서 멈추고 상태를 확인하는 디버깅 기능이다.

Q. API가 안 될 때 무엇부터 확인해?
A. Event Handler가 실행되는지, Network 요청이 발생하는지부터 확인한다.

Q. UI가 안 바뀌면 무엇부터 확인해?
A. 데이터가 있는지, 렌더 함수가 호출되는지, DOM 요소 선택이 성공했는지 확인한다.

Q. Undefined Error를 줄이려면 어떻게 해?
A. optional chaining, null check, Array.isArray, 기본값 처리를 사용한다.

Q. ESLint는 뭐야?
A. JavaScript 코드의 오류 가능성과 스타일 위반을 검사하는 도구다.

Q. Prettier는 뭐야?
A. JavaScript 코드 Formatting을 자동으로 정리하는 도구다.

Q. Import Export Error는 왜 발생해?
A. export 이름, import 방식, 파일 경로, default / named export 방식이 맞지 않을 때 발생한다.

Q. Cannot resolve module은 무엇을 확인해야 해?
A. 파일 경로, 파일명, 확장자, 대소문자, 실제 파일 존재 여부를 확인해야 한다.

Q. Module에서 가장 흔한 실수는 뭐야?
A. named export와 default export를 혼동하거나 import 경로를 잘못 작성하는 것이다.

Q. Error Handling에서 가장 흔한 실수는 뭐야?
A. catch를 비워두거나 사용자 메시지 없이 오류를 숨기는 것이다.

Q. Debugging에서 가장 흔한 실수는 뭐야?
A. Network Tab을 확인하지 않고 Console Error만 보고 추측하는 것이다.

Q. Review Agent는 Module Error Debugging에서 무엇을 우선 검토해야 해?
A. export / import 일치, API / UI 분리, Error Handling, 민감정보 로그, Network Debug 절차를 우선 검토해야 한다.

Q. JavaScript Foundation Part09 다음에는 무엇을 다뤄야 해?
A. Practical Logic, Security, Troubleshooting, Review Checklist를 다루는 Part10으로 이어지는 것이 좋다.
