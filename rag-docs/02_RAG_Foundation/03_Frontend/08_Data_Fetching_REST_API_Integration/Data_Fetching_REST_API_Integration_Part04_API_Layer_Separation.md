# Data Fetching & REST API Integration Part04 - API Layer Separation

---

# 1. API Layer Separation Overview

## 1.1 API Layer Separation 기본 개념

### [개념]

API Layer Separation은 Component 내부에서 직접 HTTP Request를 작성하지 않고, API 요청 함수를 별도 파일과 계층으로 분리하는 설계 방식이다.

Frontend Agent는 API 연동 코드를 생성할 때 Component, API Function, Axios Instance, Type Definition, Custom Hook의 역할을 분리해야 한다.

기본 구조:

```text
Component
→ Custom Hook
→ API Function
→ Axios Instance
→ Backend REST API
→ Response DTO
→ UI State
```

---

### [핵심]

API Layer Separation 핵심 키워드:

- API Layer
- API Function
- Axios Instance
- publicApi
- authApi
- Custom Hook
- Query Hook
- Request DTO
- Response DTO
- Params Type
- API Module
- Domain API File
- Component Separation
- URL Path
- HTTP Method
- Request Body
- Query Parameter
- Response Mapping
- Error Mapping

API Layer 목적:

- Component에서 API URL 제거
- HTTP Method 중복 제거
- Header 처리 중복 제거
- Response Mapping 기준 통일
- Error Handling 기준 통일
- 도메인별 API 함수 관리
- 테스트 가능성 향상
- 유지보수성 향상
- Backend API 명세 변경 대응 용이

---

### [실무]

2026 실무 기준에서 API 요청은 Component 내부에 직접 작성하지 않는 것이 좋다.

권장 흐름:

```text
User Action
→ Component Event Handler
→ API Function or Custom Hook 호출
→ publicApi / authApi 선택
→ Backend API Request
→ Response DTO Mapping
→ Loading / Error / Empty / Success UI 처리
```

권장 폴더 구조:

```text
src
├ api
│  ├ axiosInstance.js
│  ├ festivalApi.js
│  ├ reviewApi.js
│  ├ notificationApi.js
│  └ authApi.js
├ hooks
│  ├ useFestivals.js
│  ├ useFestivalDetail.js
│  └ useReviews.js
├ types
│  ├ festivalTypes.ts
│  ├ reviewTypes.ts
│  └ apiTypes.ts
├ pages
└ components
```

실무 기준:

- API URL은 api 파일에서 관리
- Component는 API 경로를 직접 알지 않음
- 인증 필요 여부에 따라 `publicApi` / `authApi` 선택
- API 함수 이름은 도메인 동작 중심
- Response Wrapper 처리 기준 통일
- Loading / Error / Empty UI는 Component 또는 Hook에서 처리
- TanStack Query 사용 시 API 함수는 `queryFn` / `mutationFn`으로 재사용

---

### [FAQ]

Q. API Layer Separation이 뭐야?
A. Component에서 직접 API 요청을 작성하지 않고 api 파일, custom hook, query hook 등으로 역할을 분리하는 방식이다.

Q. API 함수를 왜 분리해?
A. Component가 URL, Method, Header 세부사항에 의존하지 않게 하고 재사용성과 테스트 가능성을 높이기 위해서다.

Q. Component 안에서 axios를 직접 호출하면 안 돼?
A. 작은 실습은 가능하지만 API가 많아질수록 중복, 경로 오류, 에러 처리 불일치가 커진다.

Q. API Layer Separation의 최종 목적은 뭐야?
A. Frontend Agent가 Backend API 명세를 안정적인 API 함수와 UI 연결 구조로 변환하게 만드는 것이다.

---

# 2. API Function Separation Rules

## 2.1 API Function 분리 기준

### [개념]

API Function은 특정 Backend API Endpoint를 호출하는 함수다.

하나의 API Function은 하나의 도메인 동작을 표현해야 한다.

예:

```text
getFestivals
getFestivalDetail
searchFestivals
createReview
updateReview
deleteReview
markNotificationRead
```

---

### [핵심]

API Function이 담당하는 것:

- URL Path
- HTTP Method
- Query Parameter
- Path Variable
- Request Body
- Request Header
- Axios Instance 선택
- Response DTO 반환
- Response Wrapper Unwrapping
- 기본 Error 전달

API Function이 담당하지 않는 것:

- 화면 렌더링
- Loading UI 표시
- Error UI 표시
- Form 입력 관리
- Component State 상세 관리
- Routing 처리
- 사용자 이벤트 직접 처리

---

### [실무]

기본 API Function 예:

```javascript
import { publicApi, authApi } from "./axiosInstance";

export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}

export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}

export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

Wrapper unwrap 기준 적용 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

API 함수 작성 Flow:

```text
Read Backend API Spec
→ Determine publicApi or authApi
→ Determine Method
→ Build URL Path
→ Attach params or body
→ Return Response DTO
→ Export API Function
```

주의:

- API 함수에서 Component State를 직접 변경하지 않음
- API 함수 이름은 실제 도메인 동작을 반영
- API 함수마다 unwrap 기준을 섞지 않음
- Backend DTO 변경 시 API 함수 반환 구조도 확인
- Path Variable 값 검증 기준 필요

---

### [FAQ]

Q. API 함수는 뭘 담당해?
A. URL, Method, params, body, instance 선택, response mapping 같은 API 요청 세부사항을 담당한다.

Q. API 함수에서 setState를 해도 돼?
A. 권장하지 않는다. API 함수는 데이터를 반환하고 상태 변경은 Component나 Hook에서 처리하는 것이 좋다.

Q. API 함수에서 response.data.data까지 반환해도 돼?
A. 가능하다. 다만 프로젝트 전체에서 wrapper 처리 기준을 일관되게 정해야 한다.

Q. API 함수 하나가 여러 API를 호출해도 돼?
A. 단순 API 함수는 하나의 endpoint를 담당하는 것이 좋고, 복합 흐름은 service hook이나 use case 함수로 분리할 수 있다.

---

# 3. Domain API File Rules

## 3.1 도메인별 API 파일 분리

### [개념]

Domain API File은 특정 도메인 Resource와 관련된 API Function을 모아둔 파일이다.

예:

```text
festivalApi.js
reviewApi.js
notificationApi.js
authApi.js
userApi.js
```

---

### [핵심]

도메인 분리 기준:

- Resource 기준
- Feature 기준
- Backend Controller 기준
- 화면 기능 기준
- 인증 도메인 기준
- API 응집도 기준

파일 예:

| 파일                 | 역할                        |
| -------------------- | --------------------------- |
| `festivalApi.js`     | 축제 목록, 상세, 검색, 필터 |
| `reviewApi.js`       | 리뷰 목록, 작성, 수정, 삭제 |
| `notificationApi.js` | 알림 목록, 읽음 처리        |
| `authApi.js`         | 로그인, 회원가입, 로그아웃  |
| `userApi.js`         | 내 정보, 프로필 수정        |

---

### [실무]

`festivalApi.js` 예:

```javascript
import { publicApi } from "./axiosInstance";

export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}

export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}

export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", { params });
  return response.data;
}

export async function getFestivalThemeFilters() {
  const response = await publicApi.get("/festivals/filters/themes");
  return response.data;
}
```

`reviewApi.js` 예:

```javascript
import { publicApi, authApi } from "./axiosInstance";

export async function getReviews(festivalId, params) {
  const response = await publicApi.get(`/festivals/${festivalId}/reviews`, {
    params,
  });

  return response.data;
}

export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}

export async function updateReview(reviewId, requestBody) {
  const response = await authApi.patch(`/reviews/${reviewId}`, requestBody);
  return response.data;
}

export async function deleteReview(reviewId) {
  const response = await authApi.delete(`/reviews/${reviewId}`);
  return response.data;
}
```

주의:

- 도메인 파일이 너무 커지면 feature 단위로 추가 분리
- 파일명과 함수명은 도메인 의미가 드러나게 작성
- Backend Controller path 변경 시 관련 API 파일을 우선 확인
- 같은 함수명을 다른 URL로 중복 선언하지 않음
- default export보다 named export가 추적에 유리한 경우가 많음

---

### [FAQ]

Q. festivalApi.js에는 뭘 넣어?
A. 축제 목록 조회, 상세 조회, 검색, 필터 조회처럼 축제 도메인 API 함수를 넣는다.

Q. reviewApi.js에는 뭘 넣어?
A. 리뷰 목록, 작성, 수정, 삭제 API 함수를 넣는다.

Q. API 파일은 Backend Controller 기준으로 나누면 돼?
A. 가능하다. 다만 Frontend 기능 응집도와 Resource 기준도 함께 고려한다.

Q. API 파일 하나에 모든 API를 넣어도 돼?
A. 권장하지 않는다. 규모가 커질수록 검색성과 유지보수성이 떨어진다.

---

# 4. API Function Naming Rules

## 4.1 API 함수 이름 규칙

### [개념]

API Function Naming은 함수 이름만 보고 어떤 도메인 동작을 수행하는지 알 수 있게 정하는 규칙이다.

HTTP Method보다 사용자 의도와 도메인 동작이 드러나는 이름을 우선한다.

---

### [핵심]

권장 prefix:

- `get`
- `search`
- `create`
- `update`
- `patch`
- `delete`
- `upload`
- `download`
- `login`
- `logout`
- `refresh`
- `mark`
- `toggle`

권장 이름 예:

```text
getFestivals
getFestivalDetail
searchFestivals
createReview
updateReview
deleteReview
toggleFavorite
markNotificationRead
uploadReviewImage
refreshAccessToken
```

비권장 이름 예:

```text
api1
fetchData
callApi
getData
postData
handleApi
festival
request
```

---

### [실무]

도메인 동작 중심 이름:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

검색 함수:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", { params });
  return response.data;
}
```

변경 함수:

```javascript
export async function markNotificationRead(notificationId) {
  const response = await authApi.patch(`/notifications/${notificationId}/read`);
  return response.data;
}
```

상태 토글 함수:

```javascript
export async function toggleFavorite(festivalId) {
  const response = await authApi.post(`/festivals/${festivalId}/favorite`);
  return response.data;
}
```

주의:

- `fetch` prefix는 프로젝트 컨벤션에 따라 가능하지만 도메인 동작이 약할 수 있음
- `getData`처럼 범용 이름은 Retrieval 품질이 낮음
- 함수명과 실제 HTTP Method가 반드시 같을 필요는 없음
- 함수명은 Component와 Hook에서 그대로 검색될 수 있어야 함

---

### [FAQ]

Q. API 함수 이름은 어떻게 지어?
A. getFestivals, getFestivalDetail, createReview, updateReview, deleteReview처럼 동작과 리소스가 드러나게 짓는다.

Q. 함수 이름에 fetch를 붙이는 게 좋아?
A. 프로젝트 컨벤션에 따라 가능하지만 getFestivals, createReview처럼 도메인 동작이 드러나는 이름이 더 명확한 경우가 많다.

Q. postReview보다 createReview가 좋아?
A. HTTP Method보다 도메인 동작을 드러내려면 createReview가 더 명확한 경우가 많다.

Q. toggleFavorite 같은 이름을 써도 돼?
A. API가 실제로 상태를 토글하는 동작이면 가능하다. 명시적으로 addFavorite/removeFavorite로 나누는 방식도 가능하다.

---

# 5. Request Type Separation Rules

## 5.1 Params / Request Body / Path Variable 분리

### [개념]

API Function은 Path Variable, Query Parameter, Request Body를 명확히 분리해서 받아야 한다.

세 요청 데이터는 목적이 다르므로 하나의 객체에 무분별하게 섞지 않는다.

---

### [핵심]

분리 기준:

- Path Variable → 특정 Resource 식별
- Query Parameter → 검색, 필터, 정렬, 페이지네이션
- Request Body → 생성, 수정, 제출 데이터
- Header → 인증, Content-Type, 요청 메타데이터

함수 인자 예:

```text
getFestivalDetail(festivalId)
searchFestivals(params)
createReview(requestBody)
updateReview(reviewId, requestBody)
getReviews(festivalId, params)
```

주의:

- id를 params 객체에 숨기지 않음
- 검색 조건을 body로 보내지 않음
- GET 요청에 body 사용 금지
- Request DTO와 Response DTO 구분
- undefined path variable 방지

---

### [실무]

Path Variable:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

Query Parameter:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", { params });
  return response.data;
}
```

Request Body:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

혼합:

```javascript
export async function updateReview(reviewId, requestBody) {
  const response = await authApi.patch(`/reviews/${reviewId}`, requestBody);
  return response.data;
}
```

중첩 Resource + Pagination:

```javascript
export async function getReviews(festivalId, params) {
  const response = await publicApi.get(`/festivals/${festivalId}/reviews`, {
    params,
  });

  return response.data;
}
```

---

### [FAQ]

Q. Path Variable과 Query Parameter는 함수 인자에서 나눠야 해?
A. 나누는 것이 좋다. Resource 식별값과 조회 조건의 의미가 다르기 때문이다.

Q. updateReview는 인자를 어떻게 받는 게 좋아?
A. `updateReview(reviewId, requestBody)`처럼 식별자와 수정 데이터를 분리하는 것이 명확하다.

Q. getReviews(festivalId, page)은 어떻게 작성해?
A. `getReviews(festivalId, params)` 형태로 festivalId는 Path Variable, page/size는 Query Parameter로 분리한다.

Q. Request Body에 id를 넣어도 돼?
A. Backend 명세에 따라 가능하지만 URL Path로 식별하는 API라면 Path Variable과 Body 역할을 혼동하지 않아야 한다.

---

# 6. Response Mapping Separation Rules

## 6.1 Response Mapping 위치 기준

### [개념]

Response Mapping은 Backend Response Body에서 Frontend가 사용할 데이터를 꺼내거나 변환하는 작업이다.

API Layer는 Response Wrapper, Page Response, Slice Response, Nullable Field를 일관된 기준으로 처리해야 한다.

---

### [핵심]

Response Mapping 위치:

- API Function
- Response Interceptor
- Custom Hook
- Component

권장 우선순위:

```text
API Function에서 기본 unwrap
→ Custom Hook에서 UI에 맞는 가공
→ Component는 최종 데이터 사용
```

Mapping 대상:

- `response.data`
- `response.data.data`
- `content`
- `page`
- `slice`
- `hasNext`
- `totalPages`
- `nullable field`
- `date string`
- `enum value`

주의:

- Component마다 `response.data.data.content` 반복 금지
- Interceptor unwrap 기준 혼용 금지
- Page Response와 Slice Response 구분
- 배열인지 객체인지 확인
- null 가능 필드 처리

---

### [실무]

ApiResponse unwrap:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

Page Response 반환:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data.data;
}
```

Component 사용:

```javascript
const pageData = await getFestivals(params);
setFestivals(pageData.content);
setTotalPages(pageData.totalPages);
```

Custom Hook에서 mapping:

```javascript
export function useFestivalList(params) {
  const [festivals, setFestivals] = useState([]);
  const [pageInfo, setPageInfo] = useState(null);

  async function loadFestivals() {
    const pageData = await getFestivals(params);
    setFestivals(pageData.content);
    setPageInfo({
      page: pageData.number,
      totalPages: pageData.totalPages,
      hasNext: !pageData.last,
    });
  }

  return { festivals, pageInfo, loadFestivals };
}
```

---

### [FAQ]

Q. Response Mapping은 어디서 하는 게 좋아?
A. 기본 unwrap은 API 함수에서 하고, 화면에 맞는 가공은 Custom Hook이나 Component에서 처리하는 방식이 좋다.

Q. Component에서 response.data.data.content를 직접 써도 돼?
A. 가능은 하지만 반복이 많아지고 응답 구조 변경에 취약해진다.

Q. Page Response는 content만 반환하는 게 좋아?
A. 화면에서 totalPages, number, last 등이 필요하면 Page 객체 전체를 반환하는 것이 좋다.

Q. map is not a function은 Response Mapping 문제야?
A. 배열이 아닌 wrapper 객체나 undefined에 `.map()`을 호출한 경우라면 Response Mapping 문제다.

---

# 7. Error Handling Separation Rules

## 7.1 Error Handling 역할 분리

### [개념]

Error Handling Separation은 API 요청 실패를 어느 계층에서 분류하고, 어느 계층에서 사용자 UI로 보여줄지 분리하는 기준이다.

API Layer는 에러를 숨기지 않고 호출부가 처리할 수 있도록 전달해야 한다.

---

### [핵심]

역할 분리:

| 계층              | 역할                               |
| ----------------- | ---------------------------------- |
| Axios Interceptor | 공통 401 / 403 / token 처리        |
| Error Mapper      | status code를 사용자 메시지로 변환 |
| API Function      | 에러를 삼키지 않고 throw           |
| Custom Hook       | loading / error state 관리         |
| Component         | Error UI 표시                      |

주의:

- API 함수에서 에러를 조용히 무시하지 않음
- Interceptor에서 모든 에러를 alert 처리하지 않음
- 사용자 메시지와 개발 로그 구분
- 401과 403 구분
- Validation Error는 field별 처리 가능
- Error State와 Empty State 구분

---

### [실무]

Error Mapper:

```javascript
import axios from "axios";

export function getApiErrorMessage(error) {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

    if (status === 401) {
      return "로그인이 필요합니다.";
    }

    if (status === 403) {
      return "접근 권한이 없습니다.";
    }

    if (status === 404) {
      return "요청한 데이터를 찾을 수 없습니다.";
    }

    if (status && status >= 500) {
      return "서버 오류가 발생했습니다.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Custom Hook에서 Error State 관리:

```javascript
export function useFestivalDetail(festivalId) {
  const [festival, setFestival] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  async function loadFestival() {
    try {
      setLoading(true);
      setErrorMessage("");

      const data = await getFestivalDetail(festivalId);
      setFestival(data);
    } catch (error) {
      setErrorMessage(getApiErrorMessage(error));
    } finally {
      setLoading(false);
    }
  }

  return { festival, loading, errorMessage, loadFestival };
}
```

Component에서 Error UI 표시:

```jsx
if (errorMessage) {
  return <p role="alert">{errorMessage}</p>;
}
```

---

### [FAQ]

Q. API 함수에서 try/catch를 해야 해?
A. 공통 처리가 필요하면 가능하지만 에러를 삼키지 말고 호출부가 Error State를 처리할 수 있게 해야 한다.

Q. Interceptor에서 alert을 띄워도 돼?
A. 남발하면 화면별 UX 제어가 어려워진다. 공통 처리와 화면별 처리를 구분하는 것이 좋다.

Q. Error Mapper는 왜 필요해?
A. Status Code나 AxiosError를 사용자에게 보여줄 안전한 메시지로 변환하기 위해 필요하다.

Q. Empty State와 Error State는 어디서 구분해?
A. API 성공 후 데이터가 비어 있으면 Empty State, 요청 실패면 Error State로 Component나 Hook에서 구분한다.

---

# 8. Custom Hook Separation Rules

## 8.1 Custom Hook과 API Layer

### [개념]

Custom Hook은 API Function과 Component 사이에서 Loading State, Error State, Data State, Event Function을 관리하는 계층이다.

TanStack Query를 사용하지 않는 경우 Custom Hook은 Data Fetching 상태 관리 역할을 수행할 수 있다.

---

### [핵심]

Custom Hook 담당:

- API Function 호출
- loading state
- error state
- data state
- empty 판단
- refetch 함수
- submit handler 보조
- pagination state
- UI에 필요한 derived state

Custom Hook이 직접 담당하지 않는 것:

- JSX 렌더링
- 실제 API URL 작성
- Axios Instance 생성
- Backend DTO 정의
- 전역 인증 정책 전체

---

### [실무]

목록 조회 Hook:

```javascript
export function useFestivals(initialParams) {
  const [params, setParams] = useState(initialParams);
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  async function loadFestivals(nextParams = params) {
    try {
      setLoading(true);
      setErrorMessage("");

      const pageData = await getFestivals(nextParams);
      setFestivals(pageData.content);
    } catch (error) {
      setErrorMessage(getApiErrorMessage(error));
    } finally {
      setLoading(false);
    }
  }

  return {
    params,
    setParams,
    festivals,
    loading,
    errorMessage,
    loadFestivals,
    isEmpty: !loading && festivals.length === 0,
  };
}
```

Component 사용:

```jsx
function FestivalListPage() {
  const { festivals, loading, errorMessage, isEmpty, loadFestivals } =
    useFestivals({ page: 0, size: 20 });

  useEffect(() => {
    loadFestivals();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (errorMessage) {
    return <p role="alert">{errorMessage}</p>;
  }

  if (isEmpty) {
    return <p>검색 결과가 없습니다.</p>;
  }

  return <FestivalList festivals={festivals} />;
}
```

주의:

- Hook 이름은 `use`로 시작
- Hook 안에서 API URL을 직접 작성하지 않음
- API 함수 import 후 호출
- 상태와 이벤트 로직을 Component에서 분리
- 복잡한 server state는 TanStack Query 검토

---

### [FAQ]

Q. Custom Hook은 왜 만들어?
A. API 호출, loading, error, data 상태를 Component에서 분리해 재사용성과 가독성을 높이기 위해 만든다.

Q. Custom Hook에서 axios를 직접 호출해도 돼?
A. 가능은 하지만 API Function을 호출하는 방식이 더 분리도가 좋다.

Q. TanStack Query를 쓰면 Custom Hook이 필요 없어?
A. 필요할 수 있다. Query Hook을 감싸 화면별 파라미터나 derived state를 제공하는 custom hook을 만들 수 있다.

Q. Custom Hook은 JSX를 반환해도 돼?
A. 일반적으로 데이터와 상태, 함수만 반환하고 JSX 렌더링은 Component가 담당한다.

---

# 9. TanStack Query API Layer Rules

## 9.1 Query Function과 API Function 분리

### [개념]

TanStack Query를 사용할 때도 API Function은 별도로 유지한다.

`useQuery`의 `queryFn`과 `useMutation`의 `mutationFn`에서 API Function을 호출한다.

---

### [핵심]

TanStack Query 구조:

```text
API Function
→ Query Function
→ useQuery / useMutation
→ Query Cache
→ Component UI
```

역할:

- API Function: HTTP 요청
- queryFn: API Function 호출
- queryKey: 캐시 식별
- useQuery: 조회 상태 관리
- useMutation: 생성 / 수정 / 삭제 상태 관리
- invalidateQueries: 변경 후 재조회

주의:

- queryFn 내부에 URL을 직접 하드코딩하지 않음
- queryKey에 params / id 포함
- mutation 성공 후 관련 query invalidate
- API Function은 TanStack Query 밖에서도 재사용 가능하게 작성
- queryKey와 API 함수 인자 불일치 주의

---

### [실무]

API Function:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data.data;
}
```

Query Hook:

```javascript
export function useFestivalQuery(params) {
  return useQuery({
    queryKey: ["festivals", params],
    queryFn: () => getFestivals(params),
  });
}
```

Mutation API Function:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data.data;
}
```

Mutation Hook:

```javascript
export function useCreateReviewMutation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createReview,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["reviews"] });
    },
  });
}
```

주의:

- queryKey와 invalidate 대상 일치 필요
- params 객체 안정성 고려
- API Function 반환 구조가 query data 구조가 됨
- Error UI는 TanStack Query의 `error`와 Error Mapper로 처리 가능

---

### [FAQ]

Q. TanStack Query를 쓰면 API Layer가 필요 없어?
A. 아니다. queryFn과 mutationFn에서 재사용할 API 함수가 필요하다.

Q. queryFn 안에 axios 코드를 직접 써도 돼?
A. 가능하지만 API Layer 분리 원칙상 API Function을 호출하는 방식이 좋다.

Q. queryKey에 params를 넣어야 해?
A. 검색 조건이나 페이지 번호가 바뀌면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. mutation 후 목록이 안 바뀌면 뭘 확인해?
A. 관련 queryKey를 invalidate했는지, queryKey가 실제 조회 query와 일치하는지 확인한다.

---

# 10. TypeScript API Layer Rules

## 10.1 Request / Response Type 분리

### [개념]

TypeScript API Layer는 Request Type, Response Type, Params Type, ApiResponse Type을 명확히 분리해 API 함수의 입력과 출력을 안정적으로 관리하는 방식이다.

---

### [핵심]

Type 분리 대상:

- Params Type
- Request Type
- Response Type
- ApiResponse<T>
- PageResponse<T>
- SliceResponse<T>
- Error Response Type
- Nullable Field
- Enum Union Type

기본 원칙:

- Request Type과 Response Type을 분리
- Backend DTO와 Frontend Type 동기화
- null 가능성 반영
- 날짜는 string으로 받은 뒤 변환
- API 함수 반환 타입 명시
- `any` 남용 금지

---

### [실무]

공통 Type:

```typescript
export type ApiResponse<T> = {
  success: boolean;
  message: string;
  data: T;
};

export type PageResponse<T> = {
  content: T[];
  number: number;
  size: number;
  totalPages: number;
  totalElements: number;
  first: boolean;
  last: boolean;
};
```

Festival Type:

```typescript
export type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  page?: number;
  size?: number;
  sort?: string;
};

export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  averageRating: number | null;
};
```

API Function Type:

```typescript
export async function getFestivals(
  params: FestivalSearchParams,
): Promise<PageResponse<FestivalSummaryResponse>> {
  const response = await publicApi.get<
    ApiResponse<PageResponse<FestivalSummaryResponse>>
  >("/festivals", { params });

  return response.data.data;
}
```

Review Request / Response:

```typescript
export type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};

export type ReviewResponse = {
  reviewId: number;
  festivalId: number;
  rating: number;
  content: string;
  createdAt: string;
};
```

---

### [FAQ]

Q. Request Type과 Response Type은 나눠야 해?
A. 나누는 것이 좋다. 요청과 응답의 필드가 다를 수 있기 때문이다.

Q. API 응답 타입은 왜 필요해?
A. 응답 구조를 명확히 해 필드 오타와 null 처리 오류를 줄이기 위해 필요하다.

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. any를 쓰면 안 돼?
A. 임시로는 가능하지만 API Layer에서는 응답 구조 검증과 자동완성을 위해 구체 타입을 사용하는 것이 좋다.

---

# 11. API Layer Folder Structure

## 11.1 폴더 구조 기준

### [개념]

API Layer Folder Structure는 API 요청 함수, Axios Instance, Type, Hook을 어디에 배치할지 정하는 구조다.

구조는 프로젝트 규모와 팀 컨벤션에 따라 달라질 수 있지만 역할 분리는 유지해야 한다.

---

### [핵심]

기본 분리:

- `api`: API Function, Axios Instance
- `hooks`: Custom Hook, Query Hook
- `types`: Request / Response Type
- `utils`: Error Mapper, Param Cleaner
- `components`: UI Component
- `pages`: Page Component

구조 선택 기준:

- 작은 프로젝트 → `src/api` 중심
- 중간 프로젝트 → `api`, `hooks`, `types` 분리
- 큰 프로젝트 → feature-based structure 검토

---

### [실무]

도메인 중심 구조:

```text
src
├ api
│  ├ axiosInstance.ts
│  ├ festivalApi.ts
│  ├ reviewApi.ts
│  └ notificationApi.ts
├ hooks
│  ├ useFestivalQuery.ts
│  ├ useReviewMutation.ts
│  └ useNotificationQuery.ts
├ types
│  ├ apiTypes.ts
│  ├ festivalTypes.ts
│  └ reviewTypes.ts
└ utils
   ├ errorMapper.ts
   └ params.ts
```

Feature 중심 구조:

```text
src
├ features
│  ├ festival
│  │  ├ api
│  │  │  └ festivalApi.ts
│  │  ├ hooks
│  │  │  └ useFestivalQuery.ts
│  │  ├ types
│  │  │  └ festivalTypes.ts
│  │  └ components
│  └ review
│     ├ api
│     ├ hooks
│     ├ types
│     └ components
└ shared
   ├ api
   │  └ axiosInstance.ts
   └ utils
```

선택 기준:

```text
학습 / 소규모 → domain api files
중대형 / 기능 복잡 → feature-based structure
공통 instance / utils → shared 분리
```

주의:

- 구조가 복잡할수록 import 경로 관리 필요
- 중복 API 함수 생성 금지
- API path 기준을 한 곳에서 관리
- 팀원이 쉽게 찾을 수 있는 구조 우선
- RAG 문서에서는 파일 위치와 역할을 명확히 기록

---

### [FAQ]

Q. api 폴더에는 뭘 넣어?
A. Axios Instance와 도메인별 API 요청 함수를 넣는다.

Q. hooks 폴더에는 뭘 넣어?
A. API 함수를 사용하는 custom hook이나 TanStack Query hook을 넣는다.

Q. types 폴더에는 뭘 넣어?
A. Request Type, Response Type, Params Type, ApiResponse Type을 넣는다.

Q. feature-based 구조는 언제 써?
A. 기능이 커지고 도메인별 컴포넌트, API, Hook, Type이 많아질 때 사용한다.

---

# 12. API Path Management Rules

## 12.1 API Path 관리 기준

### [개념]

API Path Management는 Backend Endpoint 경로를 Frontend에서 일관되게 관리하는 기준이다.

경로가 흩어지면 404, `/api/api` 중복, `/festival` vs `/festivals` 혼동이 발생하기 쉽다.

---

### [핵심]

관리 대상:

- baseURL
- `/api` prefix
- resource path
- path variable
- nested path
- query parameter
- trailing slash
- plural naming
- Backend Controller Mapping

주의:

- baseURL과 path에 `/api` 중복 금지
- 단수 / 복수 path 혼동 금지
- Path Variable undefined 방지
- Frontend Route와 Backend API Path 혼동 금지
- API path 상수화 여부는 프로젝트 규모에 따라 결정

---

### [실무]

직접 path 사용:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}
```

path builder 사용:

```javascript
export const festivalPaths = {
  list: "/festivals",
  search: "/festivals/search",
  detail: (festivalId) => `/festivals/${festivalId}`,
  reviews: (festivalId) => `/festivals/${festivalId}/reviews`,
};
```

API 함수 적용:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(festivalPaths.detail(festivalId));
  return response.data;
}
```

Path Variable 검증:

```javascript
function assertRequired(value, name) {
  if (value === undefined || value === null || value === "") {
    throw new Error(`${name} is required`);
  }
}

export async function getFestivalDetail(festivalId) {
  assertRequired(festivalId, "festivalId");

  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

---

### [FAQ]

Q. API path는 상수로 빼야 해?
A. API가 많고 경로 변경이 잦으면 path builder나 상수화를 고려할 수 있다.

Q. `/api/api`가 생기는 이유는?
A. baseURL과 API path 양쪽에 `/api` prefix를 넣었기 때문이다.

Q. `/festival`과 `/festivals`가 다르면 문제가 돼?
A. 된다. Backend Mapping과 Frontend 요청 URL이 정확히 일치해야 한다.

Q. Path Variable undefined는 어떻게 막아?
A. API 함수 시작 부분에서 필수 인자를 검증하거나 호출부에서 route param을 검증한다.

---

# 13. Params Utility Rules

## 13.1 Query Parameter 유틸 기준

### [개념]

Params Utility는 Query Parameter 객체에서 undefined, null, 빈 문자열 같은 불필요한 값을 제거하거나 변환하는 유틸 함수다.

검색, 필터, 페이지네이션 API에서 유용하다.

---

### [핵심]

처리 대상:

- undefined
- null
- empty string
- empty array
- date format
- page conversion
- boolean filter
- array serialization
- sort parameter

주의:

- false와 0은 유효한 값일 수 있음
- 빈 문자열 제거 여부는 프로젝트 기준 필요
- 날짜 형식은 Backend 기준과 일치
- UI page 1-based와 Backend page 0-based 변환
- 배열 parameter 직렬화 기준 확인

---

### [실무]

기본 cleanParams:

```javascript
export function cleanParams(params) {
  return Object.fromEntries(
    Object.entries(params).filter(([, value]) => {
      return value !== undefined && value !== null && value !== "";
    }),
  );
}
```

0과 false 보존:

```javascript
export function cleanParams(params) {
  return Object.fromEntries(
    Object.entries(params).filter(([, value]) => {
      if (value === undefined || value === null || value === "") {
        return false;
      }

      return true;
    }),
  );
}
```

API 함수 적용:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", {
    params: cleanParams(params),
  });

  return response.data;
}
```

UI page 변환:

```javascript
export function toBackendPage(uiPage) {
  return Math.max(uiPage - 1, 0);
}
```

주의:

- params 유틸이 도메인 의미를 과도하게 알지 않도록 함
- 특수한 필터 변환은 도메인 API 함수에서 처리 가능
- queryKey에도 동일한 params 기준을 적용해야 cache mismatch를 줄일 수 있음

---

### [FAQ]

Q. undefined query parameter는 보내도 돼?
A. 라이브러리 처리 방식에 따라 다르지만 보통 제거하는 것이 안전하다.

Q. 빈 검색어도 query parameter로 보내야 해?
A. 프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

Q. page는 API 함수에서 변환해도 돼?
A. 가능하다. UI page가 1-based이고 Backend가 0-based라면 요청 전 변환 기준을 통일해야 한다.

Q. false나 0도 cleanParams에서 제거해도 돼?
A. 안 된다. false와 0은 유효한 필터 값일 수 있으므로 undefined, null, 빈 문자열과 구분해야 한다.

---

# 14. Validation Before Request Rules

## 14.1 요청 전 검증 기준

### [개념]

Validation Before Request는 API 요청을 보내기 전에 필수 입력값, Path Variable, Request Body, Query Parameter를 확인하는 단계다.

잘못된 요청을 줄이고 API Error를 빠르게 찾기 위해 필요하다.

---

### [핵심]

검증 대상:

- required path variable
- required request body field
- number id
- date format
- rating range
- content length
- file size
- file type
- page range
- login required
- token presence

주의:

- Client Validation은 UX용
- Backend Validation은 반드시 필요
- API 함수에서 최소한의 필수 인자 검증 가능
- Form Validation은 Form Handling 문서와 연계
- 인증 검증은 Authentication Frontend Flow와 연계

---

### [실무]

Path Variable 검증:

```javascript
export function assertRequired(value, fieldName) {
  if (value === undefined || value === null || value === "") {
    throw new Error(`${fieldName} is required`);
  }
}
```

API 함수 적용:

```javascript
export async function getFestivalDetail(festivalId) {
  assertRequired(festivalId, "festivalId");

  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

Request Body 검증 예:

```javascript
export function validateReviewRequest(requestBody) {
  if (!requestBody.festivalId) {
    return "festivalId is required";
  }

  if (requestBody.rating < 1 || requestBody.rating > 5) {
    return "rating must be between 1 and 5";
  }

  if (!requestBody.content?.trim()) {
    return "content is required";
  }

  return "";
}
```

Submit Flow:

```text
Form Submit
→ Client Validation
→ Build Request Body
→ API Function Call
→ Backend Validation
→ Success or Validation Error UI
```

---

### [FAQ]

Q. API 요청 전에 뭘 검증해야 해?
A. 필수 입력값, Path Variable, Request Body 필드, 인증 필요 여부, token 존재 여부를 확인해야 한다.

Q. Client Validation이 있으면 Backend Validation은 없어도 돼?
A. 아니다. Client Validation은 UX용이고 실제 데이터 검증은 Backend에서 반드시 수행해야 한다.

Q. Path Variable 검증은 어디서 해?
A. 호출부에서 route param을 검증하거나 API 함수 시작 부분에서 필수 인자를 검증할 수 있다.

Q. Validation Error는 어디에 보여줘?
A. field별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

---

# 15. API Layer Testing and Review Rules

## 15.1 API Layer 검수 기준

### [개념]

API Layer Testing and Review는 API 함수가 Backend API 명세와 일치하고, 실제 Network Request가 의도대로 나가는지 검증하는 과정이다.

---

### [핵심]

검수 대상:

- API Function Name
- HTTP Method
- Request URL
- baseURL
- Path Variable
- Query Parameter
- Request Body
- Authorization Header
- Response Mapping
- Error Handling
- publicApi / authApi 선택
- TypeScript Type
- Loading / Error 연결

검수 도구:

- Browser Network Tab
- Swagger UI
- Postman
- Backend API Spec
- Console Log
- TypeScript Compiler
- Unit Test
- Mock Service Worker

---

### [실무]

Review Flow:

```text
Backend API Spec 확인
→ API Function Method 확인
→ URL Path 확인
→ publicApi / authApi 확인
→ params / body 확인
→ 실제 Network Request 확인
→ Response Body 확인
→ Mapping 확인
→ UI State 확인
```

API Function 검수 예:

```text
GET /api/festivals/{festivalId}
→ getFestivalDetail(festivalId)
→ publicApi.get(`/festivals/${festivalId}`)
→ response.data.data 반환
```

인증 API 검수 예:

```text
POST /api/reviews
→ createReview(requestBody)
→ authApi.post("/reviews", requestBody)
→ Authorization Header 포함 확인
→ 201 or 200 Response 확인
```

주의:

- Postman 성공과 Browser 성공은 다름
- Browser에서는 CORS와 Authorization Header 확인 필요
- Swagger 명세와 실제 Backend 응답 shape가 다를 수 있음
- Response Mapping은 Network Response Body 기준으로 최종 확인
- API 함수 수정 후 사용하는 Component / Hook 영향 확인

---

### [FAQ]

Q. API Layer 검수는 어떻게 해?
A. Backend API Spec과 API Function을 비교하고 Network 탭에서 실제 URL, Method, Header, Payload, Response Body를 확인한다.

Q. Swagger에서 성공하면 Frontend도 성공이야?
A. 아니다. Browser에서는 CORS, baseURL, Authorization Header, Response Mapping 문제가 추가로 발생할 수 있다.

Q. API 함수 리뷰에서 가장 중요한 것은?
A. Method, URL, params/body, authApi/publicApi 선택, response mapping이 Backend 명세와 일치하는지 확인하는 것이다.

Q. Response Mapping은 무엇을 기준으로 검수해?
A. Network 탭의 실제 Response Body 구조를 기준으로 검수한다.

---

# 16. Common Mistakes

## 16.1 API Layer Separation 공통 실수

### [개념]

API Layer Separation 실수는 API 요청 책임이 Component, Hook, API Function, Axios Instance 사이에 섞이면서 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Component마다 API URL 하드코딩
- API 함수 없이 Component에서 axios 직접 호출
- API 함수에서 setState 직접 호출
- Custom Hook에서 URL과 Method를 직접 작성
- publicApi / authApi 선택 오류
- API 함수 이름이 모호함
- 같은 API 함수 중복 작성
- Request Type과 Response Type 혼동
- Path Variable과 Query Parameter 혼동
- Response Wrapper unwrap 기준 혼용
- Page Response에서 content만 반환해 pageInfo 손실
- Error를 API 함수에서 삼킴
- Interceptor에서 alert 남발
- queryFn에 axios 코드를 직접 하드코딩
- queryKey에 params 누락
- params clean 과정에서 0과 false 제거
- `/api` prefix 중복
- Frontend Route와 Backend API Path 혼동
- Network 탭 확인 없이 구조만 수정

---

### [실무]

문제 예:

```text
문제: 같은 API가 여러 Component에 중복 작성됨
원인: API Layer 분리 누락
해결: 도메인 API 파일에 API Function 생성 후 Component에서 import
```

문제 예:

```text
문제: token이 있는데 401 발생
원인: 인증 API를 publicApi로 호출
해결: authApi 사용 여부와 Authorization Header 확인
```

문제 예:

```text
문제: 검색 결과 page 이동이 이상함
원인: UI page 1-based와 Backend page 0-based 변환 누락
해결: API 요청 전 page 변환 기준 통일
```

문제 예:

```text
문제: map is not a function
원인: API 함수가 Page Response 전체가 아닌 wrapper 객체를 그대로 반환
해결: response.data.data 또는 content 위치 확인 후 mapping 수정
```

문제 해결 Flow:

```text
API Problem
→ API Function 위치 확인
→ Instance 선택 확인
→ Request URL 확인
→ params/body 확인
→ Response Body 확인
→ Mapping 기준 확인
→ Component / Hook 연결 확인
```

---

### [FAQ]

Q. API Layer에서 가장 흔한 실수는?
A. Component에서 API URL을 직접 쓰거나 publicApi와 authApi를 잘못 선택하는 것이다.

Q. API 함수에서 setState를 하면 왜 안 좋아?
A. API 함수가 UI 상태에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

Q. queryFn에 axios 코드를 직접 써도 돼?
A. 가능하지만 API Layer 분리 원칙상 API Function을 호출하는 방식이 더 좋다.

Q. Response Wrapper 기준이 섞이면 어떤 문제가 생겨?
A. 어떤 함수는 response.data를 반환하고 어떤 함수는 response.data.data를 반환해 Component에서 데이터 접근 오류가 발생한다.

---

# 17. Part04 Checklist

## 17.1 API Layer Separation 검수 기준

### [개념]

Part04 API Layer Separation 문서는 Frontend Agent가 Component, API Function, Axios Instance, Custom Hook, Type, Query Hook의 역할을 분리해 REST API Integration 코드를 생성하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] API Layer Separation 개념이 포함되었는가?
- [ ] API Function 분리 기준이 포함되었는가?
- [ ] Domain API File 기준이 포함되었는가?
- [ ] API Function Naming 기준이 포함되었는가?
- [ ] Path Variable / Query Parameter / Request Body 인자 분리 기준이 포함되었는가?
- [ ] Response Mapping 위치 기준이 포함되었는가?
- [ ] Error Handling 역할 분리 기준이 포함되었는가?
- [ ] Custom Hook Separation 기준이 포함되었는가?
- [ ] TanStack Query API Layer 기준이 포함되었는가?
- [ ] TypeScript API Layer 기준이 포함되었는가?
- [ ] API Layer Folder Structure 기준이 포함되었는가?
- [ ] API Path Management 기준이 포함되었는가?
- [ ] Params Utility 기준이 포함되었는가?
- [ ] Validation Before Request 기준이 포함되었는가?
- [ ] API Layer Testing and Review 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ API Layer Role Check
→ API Function Check
→ Domain File Check
→ Naming Check
→ Request Type Check
→ Response Mapping Check
→ Error Handling Check
→ Hook Separation Check
→ TanStack Query Connection Check
→ TypeScript Check
→ Debugging Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Component에서 API URL 제거 가능
- API Function을 도메인별로 분리 가능
- publicApi / authApi 선택 가능
- Params / Body / Path Variable 구분 가능
- Response Mapping 기준을 통일 가능
- Error Handling 역할을 분리 가능
- Custom Hook 또는 TanStack Query Hook과 연결 가능
- Frontend Agent가 유지보수 가능한 API Layer 코드를 생성 가능

---

### [FAQ]

Q. Part04의 목적은 뭐야?
A. Frontend Agent가 Component, API Function, Axios Instance, Hook, Type의 역할을 분리해 유지보수 가능한 API Layer를 만들게 하는 것이다.

Q. Part04에서 가장 중요한 기준은 뭐야?
A. Component에서 API URL을 제거하고, API Function과 Hook, Type, Error Mapping의 역할을 명확히 나누는 것이다.

Q. Part04 다음에는 어떤 문서가 이어지면 좋아?
A. Request / Response DTO Mapping, UI State, TanStack Query, Pagination and Infinite Scroll 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. API Layer Separation이 뭐야?
A. Component에서 직접 API 요청을 작성하지 않고 api 파일, custom hook, query hook 등으로 역할을 분리하는 방식이다.

Q. API 함수를 왜 분리해?
A. Component가 URL, Method, Header 세부사항에 의존하지 않게 하고 재사용성과 테스트 가능성을 높이기 위해서다.

Q. Component 안에서 axios를 직접 호출하면 안 돼?
A. 작은 실습은 가능하지만 API가 많아질수록 중복, 경로 오류, 에러 처리 불일치가 커진다.

Q. API Layer Separation의 최종 목적은 뭐야?
A. Frontend Agent가 Backend API 명세를 안정적인 API 함수와 UI 연결 구조로 변환하게 만드는 것이다.

Q. API 함수는 뭘 담당해?
A. URL, Method, params, body, instance 선택, response mapping 같은 API 요청 세부사항을 담당한다.

Q. API 함수에서 setState를 해도 돼?
A. 권장하지 않는다. API 함수는 데이터를 반환하고 상태 변경은 Component나 Hook에서 처리하는 것이 좋다.

Q. API 함수에서 response.data.data까지 반환해도 돼?
A. 가능하다. 다만 프로젝트 전체에서 wrapper 처리 기준을 일관되게 정해야 한다.

Q. API 함수 하나가 여러 API를 호출해도 돼?
A. 단순 API 함수는 하나의 endpoint를 담당하는 것이 좋고, 복합 흐름은 service hook이나 use case 함수로 분리할 수 있다.

Q. festivalApi.js에는 뭘 넣어?
A. 축제 목록 조회, 상세 조회, 검색, 필터 조회처럼 축제 도메인 API 함수를 넣는다.

Q. reviewApi.js에는 뭘 넣어?
A. 리뷰 목록, 작성, 수정, 삭제 API 함수를 넣는다.

Q. API 파일은 Backend Controller 기준으로 나누면 돼?
A. 가능하다. 다만 Frontend 기능 응집도와 Resource 기준도 함께 고려한다.

Q. API 파일 하나에 모든 API를 넣어도 돼?
A. 권장하지 않는다. 규모가 커질수록 검색성과 유지보수성이 떨어진다.

Q. API 함수 이름은 어떻게 지어?
A. getFestivals, getFestivalDetail, createReview, updateReview, deleteReview처럼 동작과 리소스가 드러나게 짓는다.

Q. 함수 이름에 fetch를 붙이는 게 좋아?
A. 프로젝트 컨벤션에 따라 가능하지만 getFestivals, createReview처럼 도메인 동작이 드러나는 이름이 더 명확한 경우가 많다.

Q. postReview보다 createReview가 좋아?
A. HTTP Method보다 도메인 동작을 드러내려면 createReview가 더 명확한 경우가 많다.

Q. toggleFavorite 같은 이름을 써도 돼?
A. API가 실제로 상태를 토글하는 동작이면 가능하다. 명시적으로 addFavorite/removeFavorite로 나누는 방식도 가능하다.

Q. Path Variable과 Query Parameter는 함수 인자에서 나눠야 해?
A. 나누는 것이 좋다. Resource 식별값과 조회 조건의 의미가 다르기 때문이다.

Q. updateReview는 인자를 어떻게 받는 게 좋아?
A. `updateReview(reviewId, requestBody)`처럼 식별자와 수정 데이터를 분리하는 것이 명확하다.

Q. getReviews(festivalId, page)은 어떻게 작성해?
A. `getReviews(festivalId, params)` 형태로 festivalId는 Path Variable, page/size는 Query Parameter로 분리한다.

Q. Request Body에 id를 넣어도 돼?
A. Backend 명세에 따라 가능하지만 URL Path로 식별하는 API라면 Path Variable과 Body 역할을 혼동하지 않아야 한다.

Q. Response Mapping은 어디서 하는 게 좋아?
A. 기본 unwrap은 API 함수에서 하고, 화면에 맞는 가공은 Custom Hook이나 Component에서 처리하는 방식이 좋다.

Q. Component에서 response.data.data.content를 직접 써도 돼?
A. 가능은 하지만 반복이 많아지고 응답 구조 변경에 취약해진다.

Q. Page Response는 content만 반환하는 게 좋아?
A. 화면에서 totalPages, number, last 등이 필요하면 Page 객체 전체를 반환하는 것이 좋다.

Q. map is not a function은 Response Mapping 문제야?
A. 배열이 아닌 wrapper 객체나 undefined에 `.map()`을 호출한 경우라면 Response Mapping 문제다.

Q. API 함수에서 try/catch를 해야 해?
A. 공통 처리가 필요하면 가능하지만 에러를 삼키지 말고 호출부가 Error State를 처리할 수 있게 해야 한다.

Q. Interceptor에서 alert을 띄워도 돼?
A. 남발하면 화면별 UX 제어가 어려워진다. 공통 처리와 화면별 처리를 구분하는 것이 좋다.

Q. Error Mapper는 왜 필요해?
A. Status Code나 AxiosError를 사용자에게 보여줄 안전한 메시지로 변환하기 위해 필요하다.

Q. Empty State와 Error State는 어디서 구분해?
A. API 성공 후 데이터가 비어 있으면 Empty State, 요청 실패면 Error State로 Component나 Hook에서 구분한다.

Q. Custom Hook은 왜 만들어?
A. API 호출, loading, error, data 상태를 Component에서 분리해 재사용성과 가독성을 높이기 위해 만든다.

Q. Custom Hook에서 axios를 직접 호출해도 돼?
A. 가능은 하지만 API Function을 호출하는 방식이 더 분리도가 좋다.

Q. TanStack Query를 쓰면 Custom Hook이 필요 없어?
A. 필요할 수 있다. Query Hook을 감싸 화면별 파라미터나 derived state를 제공하는 custom hook을 만들 수 있다.

Q. Custom Hook은 JSX를 반환해도 돼?
A. 일반적으로 데이터와 상태, 함수만 반환하고 JSX 렌더링은 Component가 담당한다.

Q. TanStack Query를 쓰면 API Layer가 필요 없어?
A. 아니다. queryFn과 mutationFn에서 재사용할 API 함수가 필요하다.

Q. queryFn 안에 axios 코드를 직접 써도 돼?
A. 가능하지만 API Layer 분리 원칙상 API Function을 호출하는 방식이 좋다.

Q. queryKey에 params를 넣어야 해?
A. 검색 조건이나 페이지 번호가 바뀌면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. mutation 후 목록이 안 바뀌면 뭘 확인해?
A. 관련 queryKey를 invalidate했는지, queryKey가 실제 조회 query와 일치하는지 확인한다.

Q. Request Type과 Response Type은 나눠야 해?
A. 나누는 것이 좋다. 요청과 응답의 필드가 다를 수 있기 때문이다.

Q. API 응답 타입은 왜 필요해?
A. 응답 구조를 명확히 해 필드 오타와 null 처리 오류를 줄이기 위해 필요하다.

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. any를 쓰면 안 돼?
A. 임시로는 가능하지만 API Layer에서는 응답 구조 검증과 자동완성을 위해 구체 타입을 사용하는 것이 좋다.

Q. api 폴더에는 뭘 넣어?
A. Axios Instance와 도메인별 API 요청 함수를 넣는다.

Q. hooks 폴더에는 뭘 넣어?
A. API 함수를 사용하는 custom hook이나 TanStack Query hook을 넣는다.

Q. types 폴더에는 뭘 넣어?
A. Request Type, Response Type, Params Type, ApiResponse Type을 넣는다.

Q. feature-based 구조는 언제 써?
A. 기능이 커지고 도메인별 컴포넌트, API, Hook, Type이 많아질 때 사용한다.

Q. API path는 상수로 빼야 해?
A. API가 많고 경로 변경이 잦으면 path builder나 상수화를 고려할 수 있다.

Q. `/api/api`가 생기는 이유는?
A. baseURL과 API path 양쪽에 `/api` prefix를 넣었기 때문이다.

Q. `/festival`과 `/festivals`가 다르면 문제가 돼?
A. 된다. Backend Mapping과 Frontend 요청 URL이 정확히 일치해야 한다.

Q. Path Variable undefined는 어떻게 막아?
A. API 함수 시작 부분에서 필수 인자를 검증하거나 호출부에서 route param을 검증한다.

Q. undefined query parameter는 보내도 돼?
A. 라이브러리 처리 방식에 따라 다르지만 보통 제거하는 것이 안전하다.

Q. 빈 검색어도 query parameter로 보내야 해?
A. 프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

Q. page는 API 함수에서 변환해도 돼?
A. 가능하다. UI page가 1-based이고 Backend가 0-based라면 요청 전 변환 기준을 통일해야 한다.

Q. false나 0도 cleanParams에서 제거해도 돼?
A. 안 된다. false와 0은 유효한 필터 값일 수 있으므로 undefined, null, 빈 문자열과 구분해야 한다.

Q. API 요청 전에 뭘 검증해야 해?
A. 필수 입력값, Path Variable, Request Body 필드, 인증 필요 여부, token 존재 여부를 확인해야 한다.

Q. Client Validation이 있으면 Backend Validation은 없어도 돼?
A. 아니다. Client Validation은 UX용이고 실제 데이터 검증은 Backend에서 반드시 수행해야 한다.

Q. Path Variable 검증은 어디서 해?
A. 호출부에서 route param을 검증하거나 API 함수 시작 부분에서 필수 인자를 검증할 수 있다.

Q. Validation Error는 어디에 보여줘?
A. field별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

Q. API Layer 검수는 어떻게 해?
A. Backend API Spec과 API Function을 비교하고 Network 탭에서 실제 URL, Method, Header, Payload, Response Body를 확인한다.

Q. Swagger에서 성공하면 Frontend도 성공이야?
A. 아니다. Browser에서는 CORS, baseURL, Authorization Header, Response Mapping 문제가 추가로 발생할 수 있다.

Q. API 함수 리뷰에서 가장 중요한 것은?
A. Method, URL, params/body, authApi/publicApi 선택, response mapping이 Backend 명세와 일치하는지 확인하는 것이다.

Q. Response Mapping은 무엇을 기준으로 검수해?
A. Network 탭의 실제 Response Body 구조를 기준으로 검수한다.

Q. API Layer에서 가장 흔한 실수는?
A. Component에서 API URL을 직접 쓰거나 publicApi와 authApi를 잘못 선택하는 것이다.

Q. API 함수에서 setState를 하면 왜 안 좋아?
A. API 함수가 UI 상태에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

Q. queryFn에 axios 코드를 직접 써도 돼?
A. 가능하지만 API Layer 분리 원칙상 API Function을 호출하는 방식이 더 좋다.

Q. Response Wrapper 기준이 섞이면 어떤 문제가 생겨?
A. 어떤 함수는 response.data를 반환하고 어떤 함수는 response.data.data를 반환해 Component에서 데이터 접근 오류가 발생한다.

Q. Part04 API Layer Separation의 목적은 뭐야?
A. Frontend Agent가 Component, API Function, Axios Instance, Hook, Type의 역할을 분리해 유지보수 가능한 API Layer를 만들게 하는 것이다.

Q. Part04 다음에는 어떤 문서가 이어지면 좋아?
A. Request / Response DTO Mapping, UI State, TanStack Query, Pagination and Infinite Scroll 순서로 이어지는 것이 좋다.
