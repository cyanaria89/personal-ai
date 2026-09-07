# Data Fetching & REST API Integration Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Data Fetching & REST API Integration Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Frontend와 Backend REST API 연동 기준 제공
- fetch / Axios 사용 기준 제공
- API 요청 / 응답 흐름 이해 지원
- API Layer 분리 기준 제공
- Server State와 Client State 구분 지원
- Loading / Error / Empty / Success UI 처리 기준 제공
- Query Parameter / Path Variable / Request Body 처리 지원
- 인증 토큰 포함 요청 기준 제공
- Axios Instance 설계 기준 제공
- TanStack Query 적용 기준 제공
- API Error Handling 기준 제공
- Pagination / Infinite Scroll 연동 기준 제공
- API 응답 DTO와 Frontend Type 연결 지원

---

### [핵심]

우선순위:

1. REST API Integration
2. API Request Flow
3. fetch
4. Axios
5. Axios Instance
6. API Layer Separation
7. Request Params
8. Request Body
9. Response DTO Mapping
10. Loading State
11. Error State
12. Empty State
13. Server State
14. TanStack Query
15. Auth Token Header
16. Pagination
17. Infinite Scroll
18. API Troubleshooting

---

### [실무]

2026 실무 기준에서 Data Fetching & REST API Integration 문서는 단순 fetch 사용법 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- Backend API 명세를 기준으로 Frontend API 함수 작성
- Axios Instance 분리
- Public API / Auth API 구분
- Authorization Header 처리
- Query Parameter 구성
- Path Variable URL 생성
- Request Body DTO 작성
- Response DTO Type 정의
- Loading / Error / Empty 상태 처리
- API 실패 메시지 처리
- Pagination / Slice 응답 처리
- TanStack Query 적용 여부 판단
- API 경로 충돌과 CORS 문제 분석
- Network 탭 기반 디버깅 수행

---

### [FAQ]

Q. Data Fetching 문서는 State Management와 뭐가 달라?

A.
State Management는 상태를 어디에 둘지 판단하는 문서이고 Data Fetching은 서버 API 요청, 응답, 캐싱, 에러 처리, UI 상태 연결에 집중한다.

Q. Data Fetching에서 가장 중요한 기준은 뭐야?

A.
API Layer 분리, 요청/응답 타입, loading/error/empty 상태, 인증 헤더, 서버 상태 관리, 오류 디버깅이다.

Q. API 호출 코드는 Component 안에 써도 돼?

A.
간단한 실습은 가능하지만 실무에서는 api 함수, custom hook, TanStack Query 등으로 분리하는 것이 유지보수에 좋다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Data Fetching & REST API Integration 문서는 Frontend와 Backend API 연동에 필요한 범위를 포함한다.

포함 범위:

- REST API Overview
- HTTP Method
- GET / POST / PUT / PATCH / DELETE
- URL Path
- Path Variable
- Query Parameter
- Request Body
- Request Header
- Response Body
- Status Code
- JSON
- fetch API
- Axios
- Axios Instance
- Axios Interceptor Basics
- API Layer Separation
- Public API / Authenticated API
- Authorization Header
- Bearer Token
- Refresh Token Flow Basics
- CORS Basics
- Same Origin Policy Basics
- Environment Variable
- Base URL
- Loading State
- Error State
- Empty State
- Success State
- Server State
- TanStack Query Basics
- useQuery
- useMutation
- Query Key
- Invalidation
- Pagination
- Infinite Scroll
- File Upload Basics
- API Response Mapping
- DTO Type Definition
- Network Debugging
- API Troubleshooting

---

### [핵심]

반드시 포함:

- API 요청은 UI Component에서 직접 남발하지 않음
- API 요청 함수는 api layer로 분리 가능
- 인증이 필요한 요청과 공개 요청을 구분
- Query Parameter와 Path Variable을 구분
- Request Body는 POST / PUT / PATCH 중심
- Response DTO를 Frontend Type으로 명확히 표현
- Loading / Error / Empty / Success 상태를 분리
- Server State는 일반 Client State와 분리
- TanStack Query는 Server State 캐싱에 적합
- Network 탭으로 실제 요청 / 응답을 검증
- CORS와 인증 헤더 문제를 구분

---

### [실무]

Data Fetching은 React Router / State Management 이후 Backend API와 연결하는 단계에서 사용한다.

실무 연결:

```text
React Component Design
→ React Router
→ State Management
→ Data Fetching & REST API Integration
→ Authentication Frontend Flow
→ Error Handling & Loading UX
→ Frontend Testing
```

---

### [FAQ]

Q. Axios와 fetch를 둘 다 다뤄?

A.
기본 fetch와 실무에서 많이 쓰는 Axios를 모두 다룬다. 프로젝트 기준에 따라 하나로 통일한다.

Q. TanStack Query를 필수로 써야 해?

A.
필수는 아니다. API 데이터 캐싱, refetch, mutation, pagination 관리가 복잡해질 때 검토한다.

Q. WebSocket도 여기서 다뤄?

A.
아니다. WebSocket / SSE / 실시간 통신은 Realtime Communication Domain Rules에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

Data Fetching & REST API Integration 문서에서는 실시간 통신과 고급 서버 상태 관리 심화를 제외한다.

제외 범위:

- WebSocket 심화
- Server-Sent Events 심화
- GraphQL 심화
- Apollo Client 심화
- Relay 심화
- gRPC Web
- Offline Sync 심화
- Background Sync
- Service Worker Cache 심화
- Advanced TanStack Query 심화
- Complex Optimistic Update
- Full Authentication Architecture
- OAuth2 전체 인증 흐름 심화
- Security Token Storage 심화
- Backend API 설계 심화
- API Gateway / BFF Architecture 심화

---

### [핵심]

제외 이유:

- Data Fetching Foundation 범위 초과
- Authentication / Realtime / Advanced Server State 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- REST API 연동 실무 기본기에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
Data Fetching & REST API Integration
→ Authentication Frontend Flow
→ Realtime Communication
→ Advanced TanStack Query
→ Frontend Architecture
→ API Design
```

---

### [FAQ]

Q. OAuth2 로그인 전체 흐름도 여기서 다뤄?

A.
아니다. Authorization Header와 인증 요청 기초는 포함하지만 OAuth2 심화는 Authentication Frontend Flow 문서에서 다룬다.

Q. GraphQL도 여기서 다뤄?

A.
아니다. 이 문서는 REST API Integration 중심이다.

Q. WebSocket 채팅 API도 여기서 다뤄?

A.
아니다. 실시간 채팅은 Realtime Communication 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Data Fetching & REST API Integration RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 API 연동 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 Data Fetching 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Data Fetching 문서에는 요청 흐름과 오류 검증을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- API 요청 흐름 → [Flow]
- Axios Instance 설계 → [예제], [Best Practice]
- Error Handling → [Troubleshooting]
- Pagination 처리 → [Flow], [예제]
- TanStack Query 적용 → [Comparison], [주의]
- CORS / 401 / 403 문제 → [Troubleshooting]

---

### [실무]

예시:

```md
### [Flow]

User Action
→ API Function Call
→ HTTP Request
→ Backend Response
→ Response Mapping
→ State / Query Cache Update
→ UI Render
```

---

### [FAQ]

Q. Data Fetching 문서에 Troubleshooting이 중요한 이유는?

A.
API 연동은 CORS, 401, 403, 404, JSON 파싱, baseURL, token header, response shape 오류가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
fetch vs Axios, Path Variable vs Query Parameter, Client State vs Server State, useEffect Fetch vs TanStack Query처럼 선택 기준이 필요한 경우에 사용한다.

---

# 4. REST API Integration Rules

## 4.1 REST API Basics

### [개념]

REST API는 HTTP Method와 URL을 사용해 Backend Resource를 조회, 생성, 수정, 삭제하는 API 설계 방식이다.

Frontend는 REST API를 호출해 서버 데이터를 받아 화면에 표시한다.

---

### [핵심]

반드시 설명:

- HTTP Method
- URL Path
- Resource
- Request Header
- Request Body
- Query Parameter
- Path Variable
- Response Body
- Status Code
- JSON
- DTO

HTTP Method 기준:

| Method | 목적      | 예                  |
| ------ | --------- | ------------------- |
| GET    | 조회      | 축제 목록 조회      |
| POST   | 생성      | 리뷰 작성           |
| PUT    | 전체 수정 | 회원 정보 전체 수정 |
| PATCH  | 부분 수정 | 알림 읽음 처리      |
| DELETE | 삭제      | 찜 취소             |

---

### [실무]

REST API 연동 Flow:

```text
Frontend Event
→ API Function
→ HTTP Request
→ Backend Controller
→ Service / DB
→ Response DTO
→ Frontend State Update
→ UI Render
```

예:

```text
GET /api/festivals?keyword=flower
→ 축제 목록 조회
```

```text
GET /api/festivals/1
→ 축제 상세 조회
```

```text
POST /api/reviews
→ 리뷰 작성
```

---

### [FAQ]

Q. REST API는 Frontend에서 왜 알아야 해?

A.
Frontend가 어떤 URL, Method, Parameter, Body, Header로 요청해야 하는지 알아야 Backend와 정상 연동할 수 있기 때문이다.

Q. GET과 POST 차이는?

A.
GET은 데이터 조회에 사용하고 POST는 새로운 데이터 생성이나 명령성 요청에 사용한다.

Q. Response DTO는 뭐야?

A.
Backend가 Frontend에 응답으로 내려주는 데이터 구조다.

---

## 4.2 API Request Flow

### [개념]

API Request Flow는 사용자의 행동이나 화면 진입에 따라 Frontend가 Backend API를 호출하고 응답을 UI에 반영하는 흐름이다.

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
- Refresh Button Click
- Login Success
- Route Param Change

---

### [실무]

목록 조회 Flow:

```text
FestivalListPage Mount
→ Read Search Params
→ Call getFestivals(params)
→ Set Loading
→ Receive Festival Page Response
→ Render FestivalList
→ Empty State if no content
```

작성 요청 Flow:

```text
ReviewForm Submit
→ Validate Content
→ Call createReview(body)
→ Success
→ Reset Form
→ Refetch Review List
→ Show Success Message
```

주의:

- 요청 전 입력값 검증
- 중복 제출 방지
- 실패 시 사용자 메시지 제공
- 성공 후 필요한 데이터 갱신
- Component unmount 후 setState 주의
- 서버 응답 shape 확인

---

### [FAQ]

Q. API 호출은 언제 발생해?

A.
화면 진입, 사용자 클릭, Form 제출, 검색 조건 변경, 페이지 번호 변경 같은 Trigger에서 발생한다.

Q. API 요청 전에는 뭘 확인해야 해?

A.
필수 입력값, 인증 필요 여부, URL path, query parameter, request body, token header를 확인해야 한다.

---

# 5. fetch and Axios Rules

## 5.1 fetch Rules

### [개념]

fetch는 브라우저가 제공하는 기본 HTTP 요청 API다.

외부 라이브러리 없이 API 요청을 보낼 수 있다.

---

### [핵심]

반드시 포함:

- fetch
- Promise
- async / await
- response.ok
- response.json
- headers
- method
- body
- JSON.stringify
- try / catch

---

### [실무]

GET 예:

```javascript
async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

POST 예:

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

주의:

- fetch는 HTTP 400 / 500을 자동으로 throw하지 않음
- response.ok 확인 필요
- JSON body 전송 시 Content-Type 설정
- body는 JSON.stringify 필요
- 네트워크 실패와 HTTP 실패 구분
- 공통 설정은 직접 래퍼 함수 필요

---

### [FAQ]

Q. fetch는 404나 500이면 catch로 바로 가?

A.
아니다. 네트워크 오류가 아니면 catch로 바로 가지 않는다. response.ok를 직접 확인해야 한다.

Q. fetch POST에서 body는 왜 JSON.stringify를 해?

A.
JavaScript 객체를 JSON 문자열로 변환해 서버에 보내야 하기 때문이다.

Q. fetch와 Axios 중 뭐가 좋아?

A.
간단한 요청은 fetch로 충분하고, 공통 baseURL, interceptor, 응답 처리, 인증 헤더가 많으면 Axios가 편할 수 있다.

---

## 5.2 Axios Rules

### [개념]

Axios는 HTTP 요청을 쉽게 작성할 수 있는 JavaScript 라이브러리다.

공통 설정, interceptor, JSON 처리, 에러 처리가 편리하다.

---

### [핵심]

반드시 포함:

- axios.get
- axios.post
- axios.put
- axios.patch
- axios.delete
- baseURL
- params
- headers
- data
- response.data
- AxiosError
- interceptor

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

주의:

- Axios는 JSON 변환을 자동 처리
- 응답 데이터는 보통 response.data
- Query Parameter는 params 옵션 사용
- Request Body는 두 번째 인자로 전달
- 공통 설정은 Axios Instance로 분리
- 에러 구조는 AxiosError 기준으로 처리

---

### [FAQ]

Q. Axios에서 query parameter는 어떻게 보내?

A.
`axios.get(url, { params: { keyword: "flower" } })` 형태로 보낸다.

Q. Axios 응답 데이터는 어디에 있어?

A.
보통 `response.data`에 있다.

Q. Axios POST body는 어디에 넣어?

A.
`axios.post(url, requestBody)`처럼 두 번째 인자에 넣는다.

---

## 5.3 fetch vs Axios Comparison

### [개념]

fetch와 Axios는 모두 HTTP 요청을 보내는 도구지만 사용성과 공통 처리 방식이 다르다.

---

### [핵심]

비교:

| 비교        | fetch                 | Axios                     |
| ----------- | --------------------- | ------------------------- |
| 성격        | 브라우저 기본 API     | 외부 라이브러리           |
| JSON 변환   | 직접 처리             | 자동 처리 편리            |
| HTTP Error  | 직접 response.ok 확인 | 에러 처리 상대적으로 편리 |
| Interceptor | 직접 구현 필요        | 제공                      |
| 공통 설정   | wrapper 필요          | instance 제공             |
| 적합        | 단순 요청             | 실무 API Layer            |

---

### [실무]

선택 기준:

```text
간단한 프로젝트 / 의존성 최소화 → fetch
공통 baseURL / token / error handling 필요 → Axios
Server State 캐싱 필요 → TanStack Query + fetch or Axios
```

주의:

- 프로젝트에서 fetch와 Axios를 무분별하게 혼용하지 않음
- API Layer 기준을 통일
- Error Handling 방식 통일
- 인증 Header 처리 방식 통일

---

### [FAQ]

Q. fetch와 Axios를 같이 써도 돼?

A.
가능은 하지만 프로젝트 유지보수를 위해 하나의 API 호출 기준으로 통일하는 것이 좋다.

Q. Axios를 쓰면 TanStack Query를 못 써?

A.
아니다. TanStack Query의 queryFn 내부에서 Axios를 사용할 수 있다.

---

# 6. Axios Instance Rules

## 6.1 Axios Instance Basics

### [개념]

Axios Instance는 baseURL, timeout, headers, interceptor 같은 공통 설정을 가진 Axios 객체다.

반복 설정을 줄이고 API 요청 기준을 통일하기 위해 사용한다.

---

### [핵심]

필수 포함:

- axios.create
- baseURL
- timeout
- headers
- publicApi
- authApi
- interceptor
- Authorization
- Bearer Token
- response error handling

---

### [실무]

기본 예:

```javascript
import axios from "axios";

export const publicApi = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
});

export const authApi = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
});
```

Authorization Header 예:

```javascript
authApi.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
```

권장:

- 공개 API와 인증 API 분리 가능
- baseURL 환경변수 사용
- token header는 interceptor에서 공통 처리
- response error 공통 처리 기준 마련
- API path는 함수에서 관리

---

### [FAQ]

Q. Axios Instance는 왜 만들어?

A.
baseURL, 인증 헤더, timeout, error handling 같은 공통 설정을 반복하지 않기 위해 만든다.

Q. publicApi와 authApi를 나누는 이유는?

A.
인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. Authorization Header는 매 요청마다 직접 넣어야 해?

A.
가능하지만 interceptor에서 공통 처리하는 것이 유지보수에 좋다.

---

## 6.2 Axios Interceptor Rules

### [개념]

Axios Interceptor는 요청이 서버로 가기 전 또는 응답이 Component로 전달되기 전에 공통 로직을 실행하는 기능이다.

---

### [핵심]

사용 대상:

- Authorization Header 추가
- Request Logging
- Response Data Unwrapping
- Common Error Handling
- 401 Handling
- Token Refresh Basics
- Logout Redirect
- Global Loading Basics

---

### [실무]

Response Error 예:

```javascript
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // token expired or unauthenticated
    }

    return Promise.reject(error);
  },
);
```

주의:

- interceptor에서 모든 에러를 삼키지 않음
- 401 / 403 / 500 처리 기준 구분
- token refresh 중 중복 요청 주의
- response.data unwrap 기준을 통일
- interceptor가 너무 많은 책임을 갖지 않도록 주의
- navigation redirect는 React Router와 연결 방식 주의

---

### [FAQ]

Q. Axios Interceptor는 언제 써?

A.
인증 헤더 추가, 공통 에러 처리, 401 처리처럼 모든 요청에 반복되는 로직이 있을 때 사용한다.

Q. Interceptor에서 에러를 처리하고 끝내도 돼?

A.
대부분 Promise.reject로 다시 넘겨 호출부에서도 필요한 UI 처리를 할 수 있게 해야 한다.

Q. 401과 403은 어떻게 달라?

A.
401은 인증되지 않았거나 토큰이 유효하지 않은 경우이고 403은 인증은 되었지만 권한이 없는 경우다.

---

# 7. API Layer Separation Rules

## 7.1 API Function Separation

### [개념]

API Function Separation은 Component 내부에서 직접 HTTP 요청을 작성하지 않고 api 파일의 함수로 분리하는 설계 방식이다.

---

### [핵심]

분리 대상:

- URL path
- HTTP method
- query params
- request body
- response data
- error mapping
- axios instance selection
- DTO type

---

### [실무]

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

권장:

- API 함수 이름은 동작 중심
- get / create / update / delete prefix 사용
- 인증 필요 여부에 따라 instance 선택
- Component는 API URL 상세를 몰라도 되게 함
- Response Type 또는 DTO Type 명확화

---

### [FAQ]

Q. API 함수를 왜 분리해?

A.
Component가 URL, Method, Header 세부사항에 의존하지 않게 하고 재사용성과 테스트 가능성을 높이기 위해서다.

Q. API 함수 이름은 어떻게 지어?

A.
getFestivals, getFestivalDetail, createReview, updateReview, deleteReview처럼 동작과 리소스가 드러나게 짓는다.

---

## 7.2 API Layer Naming Rules

### [개념]

API Layer Naming은 API 함수, 파일, request / response type 이름을 일관되게 정하는 규칙이다.

---

### [핵심]

Naming 기준:

- getResource
- getResourceDetail
- createResource
- updateResource
- patchResource
- deleteResource
- searchResource
- request dto
- response dto
- params type
- api suffix

---

### [실무]

예:

```text
festivalApi.js
- getFestivals
- getFestivalDetail
- searchFestivals
- getMonthlyFestivals

reviewApi.js
- getReviews
- createReview
- updateReview
- deleteReview
```

TypeScript 예:

```typescript
export type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  page?: number;
  size?: number;
};

export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
};
```

권장:

- Backend DTO 이름과 Frontend Type 이름 매핑 기준 통일
- params / request / response 구분
- 함수 이름에 HTTP Method보다 사용자 의도 반영
- deleteReview처럼 실제 도메인 동작 중심

---

### [FAQ]

Q. API 함수 이름에 fetch를 붙이는 게 좋아?

A.
프로젝트 컨벤션에 따라 가능하지만 getFestivals, createReview처럼 도메인 동작이 드러나는 이름이 더 명확한 경우가 많다.

Q. Request Type과 Response Type은 나눠야 해?

A.
나누는 것이 좋다. 요청과 응답의 필드가 다를 수 있기 때문이다.

---

# 8. Request Data Rules

## 8.1 Path Variable Rules

### [개념]

Path Variable은 URL path 일부에 포함되어 특정 Resource를 식별하는 값이다.

예:

```text
GET /api/festivals/1
```

---

### [핵심]

사용 대상:

- resource id
- user id
- festival id
- review id
- notification id
- nested resource id

---

### [실무]

예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data;
}
```

주의:

- undefined가 URL에 들어가지 않도록 검증
- 숫자 ID는 Number 변환 / validation
- path builder 함수 사용 가능
- URL encoding 필요한 값 주의
- Route Param과 API Path Variable 이름 구분 가능

---

### [FAQ]

Q. Path Variable은 언제 써?

A.
특정 리소스를 식별할 때 사용한다. 예: 축제 상세, 리뷰 삭제, 알림 읽음 처리.

Q. URL에 undefined가 들어가는 이유는?

A.
Route param이나 함수 인자가 undefined인데 검증 없이 문자열 template에 넣었을 가능성이 있다.

---

## 8.2 Query Parameter Rules

### [개념]

Query Parameter는 URL 뒤에 `?key=value` 형태로 붙는 요청 옵션이다.

검색, 필터, 정렬, 페이지네이션에 사용한다.

---

### [핵심]

사용 대상:

- keyword
- region
- theme
- startDate
- endDate
- page
- size
- sort
- targetMonth
- filter
- cursor

---

### [실무]

Axios 예:

```javascript
export async function searchFestivals(params) {
  const response = await publicApi.get("/festivals/search", {
    params,
  });

  return response.data;
}
```

요청 예:

```text
GET /api/festivals/search?keyword=flower&page=0&size=20
```

주의:

- undefined / null param 처리 기준 필요
- 빈 문자열 param 제거 여부 결정
- 배열 param 직렬화 방식 확인
- 날짜 형식 통일
- page index가 0-based인지 1-based인지 확인
- Frontend URL Search Params와 Backend Query Params mapping 확인

---

### [FAQ]

Q. Query Parameter는 언제 써?

A.
검색, 필터, 정렬, 페이지 번호처럼 리소스 조회 옵션을 전달할 때 사용한다.

Q. page는 0부터 시작해 1부터 시작해?

A.
Backend 기준에 따라 다르다. Spring Pageable은 보통 0-based라 Frontend 표시 page와 변환이 필요할 수 있다.

Q. 빈 검색어도 query parameter로 보내야 해?

A.
프로젝트 기준에 따라 다르다. 보통 빈 값은 제거하거나 Backend 기본값을 사용한다.

---

## 8.3 Request Body Rules

### [개념]

Request Body는 POST / PUT / PATCH 요청에서 서버에 전달하는 JSON 데이터다.

---

### [핵심]

사용 대상:

- create request
- update request
- login request
- signup request
- review request
- form submit
- JSON body
- DTO mapping

---

### [실무]

예:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

Request Body 예:

```json
{
  "festivalId": 1,
  "rating": 5,
  "content": "좋았어요"
}
```

주의:

- GET 요청에는 body를 넣지 않음
- Backend DTO 필드명과 일치
- 숫자 / 문자열 타입 확인
- 필수값 검증 후 요청
- 날짜 형식 통일
- PATCH는 부분 수정 의미를 명확히 함

---

### [FAQ]

Q. Request Body는 언제 써?

A.
데이터 생성, 수정, 로그인, 회원가입, 리뷰 작성처럼 서버에 JSON 데이터를 보낼 때 사용한다.

Q. GET 요청에도 body를 넣어도 돼?

A.
권장하지 않는다. 조회 조건은 보통 Query Parameter로 전달한다.

---

## 8.4 Header Rules

### [개념]

Header는 요청이나 응답의 부가 정보를 전달하는 영역이다.

인증 토큰, Content-Type, Accept 같은 값이 Header에 포함된다.

---

### [핵심]

주요 Header:

- Authorization
- Bearer Token
- Content-Type
- Accept
- multipart/form-data
- X-Request-ID basics
- CORS 관련 header

---

### [실무]

Authorization Header 예:

```javascript
config.headers.Authorization = `Bearer ${accessToken}`;
```

JSON Header 예:

```javascript
headers: {
  "Content-Type": "application/json",
}
```

주의:

- Bearer 앞 공백 포함
- token이 null이면 Header 생략
- Content-Type을 잘못 설정하면 Backend 파싱 실패 가능
- multipart/form-data는 브라우저가 boundary를 설정하도록 둠
- 민감한 Header 값 로그 출력 주의

---

### [FAQ]

Q. Authorization Header는 어떤 형식이야?

A.
일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Content-Type은 언제 필요해?

A.
JSON body를 보낼 때 `application/json`을 사용한다. Axios는 자동 처리하는 경우가 많다.

---

# 9. Response Data Rules

## 9.1 Response DTO Mapping Rules

### [개념]

Response DTO Mapping은 Backend 응답 데이터를 Frontend 화면에서 사용할 구조로 해석하거나 변환하는 과정이다.

---

### [핵심]

포함 대상:

- response.data
- ApiResponse wrapper
- content
- page
- slice
- list
- detail
- nullable field
- date string
- enum value
- type mapping

---

### [실무]

Backend 공통 응답 예:

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

Frontend 처리 예:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

주의:

- response.data가 실제 데이터인지 wrapper인지 확인
- data.data 구조 확인
- null 가능 필드 처리
- LocalDateTime 문자열 포맷 처리
- enum 표시명 mapping 필요 가능
- Backend DTO 변경 시 Frontend Type 동기화

---

### [FAQ]

Q. response.data.data는 왜 나와?

A.
Backend가 ApiResponse 같은 공통 wrapper로 응답하면 Axios response.data 안에 다시 data 필드가 있을 수 있다.

Q. Backend 응답 필드명이 바뀌면 어떻게 돼?

A.
Frontend Type과 mapping 함수, Component에서 사용하는 필드명을 함께 수정해야 한다.

---

## 9.2 TypeScript Response Type Rules

### [개념]

TypeScript Response Type은 API 응답 구조를 타입으로 정의해 Frontend에서 안전하게 사용하는 방식이다.

---

### [핵심]

필수 포함:

- Response Type
- Request Type
- Params Type
- ApiResponse Generic
- Page Response Type
- Slice Response Type
- Nullable Field
- Enum Type

---

### [실무]

공통 응답 Type 예:

```typescript
export type ApiResponse<T> = {
  success: boolean;
  message: string;
  data: T;
};
```

목록 응답 Type 예:

```typescript
export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
  averageRating: number | null;
};
```

Slice 응답 Type 예:

```typescript
export type SliceResponse<T> = {
  content: T[];
  number: number;
  size: number;
  first: boolean;
  last: boolean;
  hasNext: boolean;
};
```

주의:

- Backend DTO와 Frontend Type 동기화
- null 가능성 반영
- 날짜는 string으로 받은 뒤 formatting
- enum은 union type으로 표현 가능
- any 남용 금지

---

### [FAQ]

Q. API 응답 타입은 왜 필요해?

A.
응답 구조를 명확히 해 필드 오타와 null 처리 오류를 줄이기 위해 필요하다.

Q. 날짜 타입은 Date로 받아?

A.
JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

---

# 10. UI State Rules

## 10.1 Loading State Rules

### [개념]

Loading State는 API 요청이 진행 중임을 사용자에게 알려주는 상태다.

---

### [핵심]

사용 상황:

- initial loading
- refetch loading
- submit loading
- button disabled
- skeleton UI
- spinner
- pagination loading
- infinite scroll loading

---

### [실무]

기본 예:

```jsx
function FestivalListPage() {
  const [loading, setLoading] = useState(false);

  async function loadFestivals() {
    setLoading(true);

    try {
      await getFestivals();
    } finally {
      setLoading(false);
    }
  }

  return loading ? <p>Loading...</p> : <FestivalList />;
}
```

권장:

- 최초 로딩과 재조회 로딩 구분 가능
- 제출 중 버튼 disabled 처리
- 중복 요청 방지
- 화면이 비는 경우 Skeleton 고려
- loading 상태가 끝나는 finally 처리
- TanStack Query 사용 시 isLoading / isFetching 구분

---

### [FAQ]

Q. Loading State는 왜 필요해?

A.
API 요청 중 사용자에게 진행 상태를 알려주고 중복 클릭이나 빈 화면 혼란을 줄이기 위해 필요하다.

Q. isLoading과 isFetching은 달라?

A.
TanStack Query에서는 최초 로딩과 백그라운드 재조회 상태를 구분할 수 있다.

---

## 10.2 Error State Rules

### [개념]

Error State는 API 요청 실패나 응답 처리 실패를 사용자에게 보여주기 위한 상태다.

---

### [핵심]

처리 대상:

- network error
- 400 validation error
- 401 unauthenticated
- 403 forbidden
- 404 not found
- 409 conflict
- 500 server error
- timeout
- parsing error

---

### [실무]

기본 예:

```jsx
function ErrorMessage({ error }) {
  if (!error) {
    return null;
  }

  return <p role="alert">요청 처리 중 문제가 발생했습니다.</p>;
}
```

권장:

- 사용자 메시지와 개발자 로그 구분
- Status Code별 처리 기준
- 401은 로그인 유도
- 403은 권한 없음 안내
- 404는 리소스 없음 안내
- 500은 서버 오류 안내
- 재시도 버튼 제공 가능
- Error Boundary와 API Error 구분

주의:

- error 객체 전체를 화면에 그대로 노출하지 않음
- 민감한 서버 메시지 노출 주의
- catch에서 에러를 삼키지 않음

---

### [FAQ]

Q. API 에러 메시지는 그대로 보여줘도 돼?

A.
민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. 401과 403은 어떻게 처리해?

A.
401은 로그인 필요 또는 토큰 만료로 처리하고, 403은 권한 없음으로 처리한다.

---

## 10.3 Empty State Rules

### [개념]

Empty State는 API 요청은 성공했지만 표시할 데이터가 없는 상태다.

---

### [핵심]

사용 상황:

- 검색 결과 없음
- 목록 데이터 없음
- 리뷰 없음
- 알림 없음
- 찜 목록 없음
- 방문 기록 없음

---

### [실무]

예:

```jsx
function FestivalList({ festivals }) {
  if (festivals.length === 0) {
    return <EmptyState title="검색 결과가 없습니다." />;
  }

  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

권장:

- Error State와 구분
- 사용자 다음 행동 제공
- 검색 조건 초기화 버튼 제공 가능
- 목록 UI마다 Empty State 기준 통일
- content length 기준 확인

---

### [FAQ]

Q. Empty State와 Error State는 뭐가 달라?

A.
Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. 검색 결과가 없을 때는 에러야?

A.
아니다. 보통 정상 응답이지만 content가 비어 있는 Empty State다.

---

# 11. TanStack Query Rules

## 11.1 TanStack Query Use Criteria

### [개념]

TanStack Query는 Server State를 조회, 캐싱, 갱신, 동기화하기 위한 도구다.

API 데이터가 많고 refetch, cache, stale data 관리가 필요할 때 유용하다.

---

### [핵심]

사용 기준:

- API 데이터 캐싱 필요
- 같은 데이터를 여러 Component에서 사용
- refetch 필요
- pagination / infinite scroll 필요
- mutation 후 목록 갱신 필요
- loading / error 상태 자동 관리 필요
- stale data 관리 필요
- Server State와 Client State 분리 필요

---

### [실무]

useQuery 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Failed to load festivals.</p>;
  }

  return <FestivalList festivals={data ?? []} />;
}
```

권장:

- queryKey는 데이터 식별 기준
- queryFn은 API 함수 사용
- queryKey에 검색 조건 포함
- mutation 성공 후 invalidateQueries
- UI State와 Query State 분리
- Client State 관리 용도로 사용하지 않음

---

### [FAQ]

Q. TanStack Query는 언제 써?

A.
API 데이터 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. TanStack Query는 전역 상태관리 도구야?

A.
일반 Client State 전역 관리 도구라기보다 Server State와 API Cache 관리 도구다.

---

## 11.2 Query Key Rules

### [개념]

Query Key는 TanStack Query가 캐시 데이터를 식별하는 기준이다.

같은 queryKey는 같은 데이터로 취급된다.

---

### [핵심]

필수 포함:

- queryKey
- stable key
- resource name
- params included
- detail id included
- cache identity
- invalidation target

---

### [실무]

목록 Query Key:

```tsx
useQuery({
  queryKey: ["festivals", params],
  queryFn: () => getFestivals(params),
});
```

상세 Query Key:

```tsx
useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});
```

권장:

- 리소스 이름 포함
- 검색 조건 / page / size 포함
- 상세 ID 포함
- queryKey 구조 통일
- invalidate 대상과 queryKey 일치

주의:

- params 객체 안정성 고려
- 같은 데이터를 다른 queryKey로 중복 캐싱하지 않음
- queryKey에 민감정보 넣지 않음

---

### [FAQ]

Q. queryKey에 params를 넣어야 해?

A.
검색 조건이나 페이지 번호가 바뀌면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. queryKey가 틀리면 어떤 문제가 생겨?

A.
캐시가 중복되거나 invalidate가 제대로 되지 않아 화면 데이터가 갱신되지 않을 수 있다.

---

## 11.3 Mutation and Invalidation Rules

### [개념]

Mutation은 서버 데이터를 생성, 수정, 삭제하는 요청이다.

Invalidation은 변경 이후 관련 조회 데이터를 다시 가져오도록 캐시를 무효화하는 작업이다.

---

### [핵심]

사용 대상:

- create review
- update review
- delete review
- like festival
- favorite festival
- mark notification read
- profile update
- login / logout basics

---

### [실무]

예:

```tsx
const queryClient = useQueryClient();

const mutation = useMutation({
  mutationFn: createReview,
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ["reviews"] });
  },
});
```

권장:

- mutation 성공 후 관련 query invalidate
- 상세 / 목록 캐시 관계 고려
- 낙관적 업데이트는 신중하게 적용
- 실패 시 사용자 메시지 제공
- 중복 제출 방지
- mutation pending 상태로 버튼 disabled 처리

---

### [FAQ]

Q. mutation 후 목록이 안 바뀌어?

A.
관련 queryKey를 invalidate하지 않았거나 queryKey가 일치하지 않을 수 있다.

Q. invalidateQueries는 왜 써?

A.
서버 데이터가 변경되었으므로 기존 캐시를 무효화하고 최신 데이터를 다시 가져오기 위해 사용한다.

---

# 12. Pagination and Infinite Scroll Rules

## 12.1 Pagination Rules

### [개념]

Pagination은 많은 데이터를 page / size 단위로 나누어 조회하는 방식이다.

---

### [핵심]

필수 포함:

- page
- size
- sort
- totalPages
- totalElements
- content
- Pageable
- Page Response
- 0-based page
- 1-based UI page

---

### [실무]

요청 예:

```javascript
export async function getFestivals({ page, size }) {
  const response = await publicApi.get("/festivals", {
    params: { page, size },
  });

  return response.data;
}
```

Spring Page 응답 예:

```typescript
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

주의:

- Backend page가 0-based인지 확인
- UI page는 1부터 보여줄 수 있음
- 검색 조건 변경 시 page reset
- totalPages 기준으로 다음 버튼 제어
- sort parameter 형식 확인

---

### [FAQ]

Q. Spring Pageable page는 0부터 시작해?

A.
일반적으로 0-based다. UI에서 1부터 보여주면 요청 시 변환이 필요할 수 있다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?

A.
대부분 1페이지 또는 page 0으로 reset하는 것이 좋다.

---

## 12.2 Slice and Infinite Scroll Rules

### [개념]

Slice는 전체 개수보다 다음 페이지 존재 여부를 중심으로 데이터를 조회하는 방식이다.

Infinite Scroll이나 더보기 UI에 적합하다.

---

### [핵심]

필수 포함:

- Slice
- content
- hasNext
- last
- page
- size
- cursor basics
- load more
- infinite scroll
- duplicate prevention

---

### [실무]

Slice 응답 Type 예:

```typescript
export type SliceResponse<T> = {
  content: T[];
  number: number;
  size: number;
  first: boolean;
  last: boolean;
  hasNext: boolean;
};
```

Load More Flow:

```text
Initial Load
→ Render Content
→ User Click More or Scroll Bottom
→ Request Next Page
→ Append Content
→ Stop if hasNext false
```

주의:

- 기존 목록에 새 content append
- 중복 요청 방지
- hasNext / last 기준 통일
- page 증가 타이밍 주의
- 검색 조건 변경 시 목록 초기화
- cursor 기반이면 page 기반과 구분

---

### [FAQ]

Q. Page와 Slice 차이는?

A.
Page는 전체 개수와 totalPages를 제공하고 Slice는 다음 페이지 존재 여부 중심이라 더보기나 무한 스크롤에 적합하다.

Q. Infinite Scroll에서 중복 데이터가 생겨?

A.
page 증가 타이밍, 중복 요청, 검색 조건 변경 시 초기화 누락을 확인해야 한다.

---

# 13. Authentication API Rules

## 13.1 Authenticated Request Rules

### [개념]

Authenticated Request는 로그인한 사용자만 접근할 수 있는 API에 Authorization Header를 포함해 요청하는 방식이다.

---

### [핵심]

필수 포함:

- Authorization Header
- Bearer Token
- accessToken
- refreshToken basics
- authApi
- interceptor
- 401
- 403
- logout
- token expired

---

### [실무]

예:

```javascript
authApi.interceptors.request.use((config) => {
  const accessToken = getAccessToken();

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

인증 필요 API 예:

```javascript
export async function getMyFavorites() {
  const response = await authApi.get("/favorites");
  return response.data;
}
```

주의:

- 공개 API와 인증 API 구분
- token 누락 시 401 가능
- 권한 부족은 403 가능
- token 만료 처리 기준 필요
- logout 시 token과 user state 정리
- Frontend 인증 상태는 UX용이고 Backend 보안 필수

---

### [FAQ]

Q. 인증 필요한 API는 어떻게 구분해?

A.
Authorization Header가 필요한 API는 authApi 같은 인증용 Axios Instance를 사용해 구분할 수 있다.

Q. 401이 나오면 무조건 권한 없음이야?

A.
아니다. 401은 인증 실패나 토큰 만료이고, 권한 부족은 보통 403이다.

---

## 13.2 Token Refresh Basics

### [개념]

Token Refresh는 access token이 만료되었을 때 refresh token으로 새 access token을 발급받는 흐름이다.

이 문서에서는 기초 개념과 주의사항만 다룬다.

---

### [핵심]

Flow:

```text
API Request
→ 401 Token Expired
→ Refresh Request
→ New Access Token
→ Retry Original Request
→ If Refresh Failed
→ Logout / Login Redirect
```

---

### [실무]

주의:

- refresh 중 중복 요청 처리 필요
- refresh 실패 시 logout 처리
- 원래 요청 retry 기준 명확화
- 무한 refresh loop 방지
- refresh token 저장 위치 보안 검토
- 상세 구현은 Authentication Frontend Flow 문서로 분리

---

### [FAQ]

Q. access token이 만료되면 어떻게 해?

A.
refresh token으로 새 access token을 요청하고 성공하면 원래 요청을 재시도할 수 있다.

Q. Refresh 요청도 실패하면?

A.
사용자를 logout 처리하고 login 페이지로 이동시키는 기준을 둔다.

---

# 14. Environment and Base URL Rules

## 14.1 Base URL Rules

### [개념]

Base URL은 API 요청의 기본 서버 주소다.

개발 / 운영 환경에 따라 달라질 수 있으므로 환경변수로 관리한다.

---

### [핵심]

포함 대상:

- baseURL
- environment variable
- development API server
- production API server
- proxy
- relative URL
- absolute URL
- CORS relation

---

### [실무]

Vite 예:

```javascript
const baseURL = import.meta.env.VITE_API_BASE_URL;
```

CRA 예:

```javascript
const baseURL = process.env.REACT_APP_API_BASE_URL;
```

Axios Instance:

```javascript
export const publicApi = axios.create({
  baseURL,
});
```

주의:

- Vite는 `VITE_` prefix 필요
- CRA는 `REACT_APP_` prefix 필요
- 환경변수 변경 후 dev server 재시작 필요
- client에 노출되는 값에 비밀키 저장 금지
- 배포 환경 baseURL 확인
- relative URL 사용 시 proxy / same origin 기준 확인

---

### [FAQ]

Q. 프론트엔드 환경변수에 비밀키를 넣어도 돼?

A.
안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 비밀키 저장에 부적합하다.

Q. 환경변수를 바꿨는데 적용이 안 돼?

A.
개발 서버를 재시작해야 반영되는 경우가 많다.

---

## 14.2 Proxy and CORS Rules

### [개념]

Proxy는 개발 환경에서 Frontend 요청을 Backend로 대신 전달해 CORS 문제를 줄이는 설정이다.

CORS는 브라우저가 다른 Origin 요청을 제한하는 보안 정책이다.

---

### [핵심]

필수 포함:

- Same Origin Policy
- CORS
- Origin
- preflight
- OPTIONS
- Access-Control-Allow-Origin
- credentials
- proxy
- dev server
- backend CORS config

---

### [실무]

CORS 문제 특징:

- Browser Console에 CORS error 표시
- Network 요청이 preflight에서 실패 가능
- Backend 로그에 요청이 다르게 보일 수 있음
- Postman에서는 되는데 Browser에서는 실패 가능

주의:

- CORS는 브라우저 보안 정책
- Frontend 코드만으로 해결 불가한 경우 많음
- Backend CORS 설정 필요
- credentials 사용 시 wildcard origin 주의
- Authorization Header 사용 시 허용 Header 확인
- 개발 proxy와 운영 CORS 정책 구분

---

### [FAQ]

Q. Postman에서는 되는데 브라우저에서는 CORS 에러가 나?

A.
Postman은 브라우저 CORS 정책을 적용하지 않기 때문이다. 브라우저 요청은 Backend CORS 설정이 필요하다.

Q. CORS는 Frontend에서 해결하는 문제야?

A.
대부분 Backend CORS 설정과 배포 구조에서 해결해야 한다. 개발 환경에서는 proxy를 사용할 수 있다.

---

# 15. File Upload Rules

## 15.1 Multipart Upload Basics

### [개념]

Multipart Upload는 이미지나 파일을 서버에 업로드할 때 사용하는 요청 방식이다.

일반 JSON 요청과 다르게 FormData를 사용한다.

---

### [핵심]

필수 포함:

- FormData
- multipart/form-data
- file input
- append
- image upload
- multiple files
- Content-Type caution
- preview
- file size validation

---

### [실무]

예:

```javascript
export async function uploadReviewImage(file) {
  const formData = new FormData();
  formData.append("image", file);

  const response = await authApi.post("/reviews/images", formData);

  return response.data;
}
```

주의:

- FormData 사용 시 Content-Type을 직접 설정하지 않는 편이 안전
- 브라우저가 boundary를 포함해 Content-Type을 설정
- 파일 크기 / 확장자 검증
- 업로드 진행 상태 필요 시 onUploadProgress 검토
- 이미지 미리보기 URL 정리 필요
- Backend field name과 append key 일치

---

### [FAQ]

Q. 파일 업로드는 JSON으로 보내?

A.
일반적으로 FormData와 multipart/form-data를 사용한다.

Q. FormData 보낼 때 Content-Type을 직접 multipart/form-data로 설정해야 해?

A.
대부분 직접 설정하지 않는 것이 좋다. 브라우저나 Axios가 boundary를 포함해 설정하도록 둔다.

---

# 16. Error Handling Rules

## 16.1 API Error Classification

### [개념]

API Error Classification은 에러를 상태 코드와 원인에 따라 분류하는 작업이다.

---

### [핵심]

분류:

| Status        | 의미        | Frontend 처리           |
| ------------- | ----------- | ----------------------- |
| 400           | 잘못된 요청 | 입력값 확인             |
| 401           | 인증 실패   | 로그인 유도 / 토큰 갱신 |
| 403           | 권한 없음   | 권한 없음 안내          |
| 404           | 리소스 없음 | Not Found UI            |
| 409           | 충돌        | 중복 / 상태 충돌 안내   |
| 422           | 검증 실패   | Validation Message 표시 |
| 500           | 서버 오류   | 서버 오류 안내          |
| Network Error | 연결 실패   | 네트워크 안내 / 재시도  |

---

### [실무]

Error Mapping 예:

```typescript
export function getApiErrorMessage(error: unknown): string {
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
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

주의:

- 서버 에러 원문 직접 노출 금지
- validation error는 field별 표시 가능
- 401 / 403 구분
- 네트워크 오류와 서버 응답 오류 구분
- 공통 에러 메시지와 화면별 메시지 분리

---

### [FAQ]

Q. API 에러는 어떻게 분류해?

A.
HTTP Status Code, 서버 응답 메시지, 네트워크 실패 여부를 기준으로 분류한다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?

A.
권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

---

## 16.2 Validation Error Rules

### [개념]

Validation Error는 요청 값이 Backend 검증 조건을 통과하지 못해 발생하는 오류다.

---

### [핵심]

사용 상황:

- signup field error
- login error
- review content error
- rating range error
- required field
- invalid format
- duplicate value
- server validation response

---

### [실무]

응답 예:

```json
{
  "success": false,
  "message": "검증 실패",
  "errors": {
    "email": "이메일 형식이 올바르지 않습니다.",
    "password": "비밀번호는 8자 이상이어야 합니다."
  }
}
```

Frontend 처리 기준:

- field error는 해당 input 근처에 표시
- global error는 form 상단 표시
- 서버 validation과 client validation 메시지 충돌 방지
- submit 실패 후 입력값 유지
- error 초기화 타이밍 명확화

---

### [FAQ]

Q. 서버 Validation Error는 어디에 보여줘?

A.
필드별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

Q. Client 검증이 있는데 Server 검증도 필요해?

A.
필요하다. Client 검증은 UX용이고 실제 데이터 검증은 Backend에서 반드시 수행해야 한다.

---

# 17. Troubleshooting Rules

## 17.1 Network Debugging

### [개념]

Network Debugging은 브라우저 개발자 도구 Network 탭에서 실제 API 요청과 응답을 확인하는 과정이다.

---

### [핵심]

확인 대상:

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
→ Method Check
→ Status Code Check
→ Request Headers Check
→ Request Payload Check
→ Response Body Check
→ Console Error Check
→ Backend Log Check
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

A.
브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Status Code, Payload, Response Body를 확인한다.

Q. JSON을 기대했는데 HTML이 응답돼?

A.
API 요청이 SPA fallback에 걸려 index.html을 받은 경우일 수 있다. 요청 URL과 서버 fallback 설정을 확인한다.

---

## 17.2 CORS Error Troubleshooting

### [개념]

CORS Error는 브라우저가 다른 Origin으로 보내는 요청을 Backend가 허용하지 않을 때 발생하는 문제다.

---

### [핵심]

증상:

- Console CORS policy error
- Preflight request failed
- OPTIONS request failed
- Authorization Header not allowed
- credentials blocked
- Postman에서는 정상
- Browser에서만 실패

원인:

- Backend CORS 설정 없음
- 허용 Origin 불일치
- 허용 Method 누락
- 허용 Header 누락
- credentials 설정 문제
- preflight OPTIONS 처리 문제

해결:

- Backend CORS 설정 확인
- 개발 proxy 사용 가능
- 허용 Origin 정확히 설정
- Authorization Header 허용
- credentials 사용 시 wildcard 금지
- Backend 로그 확인

---

### [FAQ]

Q. CORS 에러는 왜 나?

A.
브라우저가 다른 Origin 요청을 제한하고 Backend가 해당 Origin, Method, Header를 허용하지 않기 때문이다.

Q. Postman에서는 되는데 브라우저에서만 안 돼?

A.
Postman은 CORS 정책을 적용하지 않기 때문이다.

---

## 17.3 401 / 403 Troubleshooting

### [개념]

401 / 403 Troubleshooting은 인증 또는 권한 문제로 API 요청이 실패하는 원인을 분석하는 과정이다.

---

### [핵심]

401 원인:

- access token 없음
- token 만료
- Bearer 형식 오류
- Authorization Header 누락
- 잘못된 token
- refresh 실패

403 원인:

- 로그인은 되었지만 권한 부족
- ROLE 불일치
- Backend Security 설정
- Resource Owner 불일치
- 관리자 API 접근

---

### [실무]

Debug Flow:

```text
Status 401 / 403 확인
→ Authorization Header 확인
→ Bearer prefix 확인
→ Token 존재 확인
→ Token 만료 확인
→ API 권한 요구사항 확인
→ User Role 확인
→ Backend Security Log 확인
```

주의:

- 401과 403을 같은 에러로 처리하지 않음
- token이 localStorage에 있어도 header에 없으면 실패
- ROLE_USER / USER naming 불일치 주의
- Frontend route 접근 가능 여부와 Backend API 권한은 별개

---

### [FAQ]

Q. token은 있는데 401이 나?

A.
Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. 403이면 로그인 문제야?

A.
대부분 인증은 되었지만 권한이 부족한 경우다.

---

## 17.4 404 Troubleshooting

### [개념]

404 Troubleshooting은 요청한 API URL이나 Resource를 서버가 찾지 못하는 문제를 분석하는 과정이다.

---

### [핵심]

원인:

- API URL 오타
- baseURL 오류
- path prefix 누락
- Frontend Route와 API Route 혼동
- Backend Controller path 불일치
- Path Variable undefined
- Resource not found
- HTTP Method 불일치

---

### [실무]

Debug Flow:

```text
Status 404 확인
→ Request URL 확인
→ Method 확인
→ Backend Controller Mapping 확인
→ baseURL 확인
→ path variable 값 확인
→ API prefix 확인
→ Response Body 확인
```

주의:

- `/festival` vs `/festivals` 혼동
- `/api` prefix 누락
- React Router path와 Backend API path 혼동
- GET endpoint에 POST 요청하지 않음
- Resource 404와 Route 404 구분

---

### [FAQ]

Q. API 404가 나면 뭘 확인해?

A.
Request URL, Method, baseURL, API prefix, Path Variable 값, Backend Controller Mapping을 확인한다.

Q. 페이지 이동 404와 API 404는 달라?

A.
다르다. 페이지 이동 404는 React Router 또는 서버 fallback 문제이고 API 404는 Backend endpoint 또는 resource 문제다.

---

## 17.5 Response Shape Mismatch

### [개념]

Response Shape Mismatch는 Frontend가 예상한 응답 구조와 실제 Backend 응답 구조가 달라 발생하는 문제다.

---

### [핵심]

증상:

- Cannot read properties of undefined
- map is not a function
- 화면에 데이터가 안 나옴
- response.data.data 혼동
- content 위치 혼동
- null field 처리 오류

원인:

- ApiResponse wrapper 확인 누락
- Page / Slice content 구조 확인 누락
- 배열을 기대했는데 객체 응답
- 객체를 기대했는데 배열 응답
- null 가능성 미처리
- Backend DTO 변경

---

### [실무]

Debug Flow:

```text
Network Response Body 확인
→ response.data 구조 확인
→ wrapper 여부 확인
→ content 위치 확인
→ TypeScript Type 수정
→ Component 접근 경로 수정
```

예:

```javascript
const response = await publicApi.get("/festivals");
console.log(response.data);
```

주의:

- 실제 응답을 Network 탭에서 확인
- TypeScript Type이 실제 응답과 맞는지 확인
- optional chaining 남용으로 오류를 숨기지 않음
- 빈 배열과 null 구분

---

### [FAQ]

Q. map is not a function 오류는 왜 나?

A.
배열이라고 생각한 값이 실제로는 객체이거나 undefined일 수 있다. 응답 구조와 content 위치를 확인해야 한다.

Q. response.data와 response.data.data가 헷갈려?

A.
Backend 공통 응답 wrapper가 있는지 확인해야 한다. ApiResponse 구조면 실제 데이터가 data 안에 한 번 더 들어갈 수 있다.

---

# 18. Security Rules

## 18.1 Frontend API Security Basics

### [개념]

Frontend API Security는 API 요청 과정에서 민감정보 노출과 잘못된 인증 처리를 줄이기 위한 기본 기준이다.

---

### [핵심]

주의 대상:

- access token
- refresh token
- Authorization Header
- API Key
- environment variable
- localStorage
- XSS
- CSRF basics
- sensitive response
- console logging

---

### [실무]

기준:

- Frontend 환경변수에 비밀키 저장 금지
- token 저장 위치는 보안 요구사항에 따라 결정
- Authorization Header 로그 노출 주의
- 사용자 개인정보 console.log 금지
- 서버 에러 상세 메시지 사용자 노출 주의
- Frontend 권한 체크는 UX용
- Backend 인증/인가가 최종 보안 기준
- API Key가 필요한 외부 서비스는 Backend Proxy 검토

주의:

- React 코드에 secret key 하드코딩 금지
- `.env`에 넣어도 Frontend secret은 안전하지 않음
- localStorage는 XSS에 취약할 수 있음
- 민감 데이터는 최소한만 Store에 보관

---

### [FAQ]

Q. Frontend .env에 API Secret을 넣어도 돼?

A.
안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 비밀키를 넣으면 안 된다.

Q. Frontend에서 권한 체크하면 API가 안전해져?

A.
아니다. Frontend 권한 체크는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

---

# 19. Comparison Rules

## 19.1 Required Comparisons

### [개념]

Data Fetching & REST API Integration 문서는 헷갈리는 API 연동 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- fetch vs Axios
- Axios Instance vs Direct Axios
- publicApi vs authApi
- Path Variable vs Query Parameter
- Query Parameter vs Request Body
- Request Body vs FormData
- Client State vs Server State
- useEffect Fetch vs TanStack Query
- useQuery vs useMutation
- Loading State vs Empty State
- 401 vs 403
- API 404 vs Route 404
- Page vs Slice
- Pagination vs Infinite Scroll
- CORS Error vs Network Error
- Frontend Route vs Backend API Endpoint

---

### [실무]

예시:

| 비교        | Query Parameter     | Request Body           |
| ----------- | ------------------- | ---------------------- |
| 사용 Method | 주로 GET            | POST / PUT / PATCH     |
| 목적        | 조회 조건           | 생성 / 수정 데이터     |
| 예          | keyword, page, size | review content, rating |
| URL 노출    | 노출됨              | URL에 노출되지 않음    |
| 적합        | 검색, 필터, 정렬    | Form 제출, 데이터 변경 |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 API 연동 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Data Fetching 비교 문서에서 가장 중요한 것은?

A.
요청 방식 선택 기준, 상태 처리 기준, 에러 처리 기준, 실제 디버깅 기준을 함께 설명하는 것이다.

---

# 20. Checklist Rules

## 20.1 Data Fetching Checklist

### [개념]

Data Fetching 문서 검수 시 API 연동 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] REST API 기본 개념이 포함되었는가?
- [ ] HTTP Method 기준이 포함되었는가?
- [ ] fetch / Axios 기준이 포함되었는가?
- [ ] Axios Instance 기준이 포함되었는가?
- [ ] Public API / Auth API 구분이 포함되었는가?
- [ ] API Layer 분리 기준이 포함되었는가?
- [ ] Path Variable / Query Parameter / Request Body 차이가 포함되었는가?
- [ ] Header / Authorization 기준이 포함되었는가?
- [ ] Response DTO Mapping 기준이 포함되었는가?
- [ ] TypeScript Response Type 기준이 포함되었는가?
- [ ] Loading / Error / Empty State가 포함되었는가?
- [ ] TanStack Query 적용 기준이 포함되었는가?
- [ ] Query Key / Mutation / Invalidation 기준이 포함되었는가?
- [ ] Pagination / Infinite Scroll 기준이 포함되었는가?
- [ ] CORS / 401 / 403 / 404 Troubleshooting이 포함되었는가?
- [ ] Network Debugging Flow가 포함되었는가?
- [ ] Security 주의사항이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ REST Concept Check
→ Request Type Check
→ API Layer Check
→ Response Mapping Check
→ UI State Check
→ Server State Check
→ Error Handling Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Data Fetching 문서 검수에서 가장 중요한 것은?

A.
API 요청 구조, 응답 mapping, loading/error/empty 처리, 인증 헤더, TanStack Query 기준, Troubleshooting 포함 여부다.

---

# 21. Retrieval Optimization Rules

## 21.1 Keyword Rules

### [개념]

Data Fetching & REST API Integration 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Data Fetching
- REST API Integration
- API Request
- API Response
- HTTP Method
- GET
- POST
- PUT
- PATCH
- DELETE
- fetch
- Axios
- Axios Instance
- Axios Interceptor
- publicApi
- authApi
- baseURL
- environment variable
- Query Parameter
- Path Variable
- Request Body
- Request Header
- Authorization Header
- Bearer Token
- Response DTO
- ApiResponse
- Page Response
- Slice Response
- Loading State
- Error State
- Empty State
- Server State
- TanStack Query
- useQuery
- useMutation
- queryKey
- invalidateQueries
- Pagination
- Infinite Scroll
- FormData
- multipart/form-data
- CORS
- 401
- 403
- 404
- Network Debugging
- Response Shape Mismatch

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- API 호출은 어디서 해?
- Axios Instance는 왜 만들어?
- publicApi와 authApi 차이는?
- Query Parameter는 어떻게 보내?
- Path Variable은 어떻게 처리해?
- Request Body는 언제 써?
- response.data.data는 왜 나와?
- Loading State는 어떻게 처리해?
- API Error는 어떻게 처리해?
- TanStack Query는 언제 써?
- queryKey는 어떻게 설계해?
- mutation 후 목록 갱신은 어떻게 해?
- API 401은 왜 나?
- API 403은 왜 나?
- API 404는 왜 나?
- CORS 에러는 어떻게 해결해?
- Network 탭에서 뭘 봐야 해?
- map is not a function은 왜 나?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 22. Version Rules

## 22.1 Modern Data Fetching 기준

### [개념]

Data Fetching & REST API Integration 문서는 Modern Frontend API 연동 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- Hook 기반 데이터 흐름
- fetch / Axios
- Axios Instance
- TanStack Query
- TypeScript Ready
- REST API 중심
- Server State 분리
- API Layer 분리
- Loading / Error / Empty UI 분리
- Network Debugging 기준

Legacy 제외:

- jQuery AJAX 중심 설명
- XMLHttpRequest 중심 설명
- Component마다 API URL 하드코딩
- 모든 API 데이터를 Redux에 저장하는 방식
- Error 무시
- Loading State 생략
- 인증 Header 매 요청마다 수동 중복 작성
- response shape 확인 없이 접근
- 비밀키를 Frontend 환경변수에 저장

---

### [실무]

실무 기준:

```text
Modern Data Fetching
→ API Layer
→ Axios Instance
→ Type-safe Request / Response
→ Server State Separation
→ Query Cache if Needed
→ Loading / Error / Empty UI
→ Network Debugging
```

---

### [FAQ]

Q. jQuery AJAX를 써야 해?

A.
신규 React 문서에서는 fetch, Axios, TanStack Query 기준으로 작성한다.

Q. 모든 API 데이터를 Redux에 넣는 방식은 좋아?

A.
현대 React에서는 Server State 도구를 고려하는 것이 좋다. API 캐시를 Redux에 직접 모두 저장하면 관리 비용이 커질 수 있다.

---

# 23. Common Mistakes

## 23.1 Data Fetching Common Mistakes

### [개념]

Data Fetching & REST API Integration 문서는 자주 발생하는 API 연동 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

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
- queryKey에 params 누락
- mutation 후 invalidate 누락
- Server State를 전역 Client Store에 중복 저장
- Frontend .env에 secret key 저장
- Network 탭 확인 없이 코드만 수정

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: API 요청했는데 index.html이 응답됨
원인: SPA fallback이 API 요청까지 가로챔
해결: API path를 fallback 대상에서 제외하고 `/api` prefix 기준을 명확히 함
```

---

### [FAQ]

Q. Data Fetching 초보가 가장 많이 하는 실수는?

A.
response.data 구조를 확인하지 않거나, 인증 헤더를 누락하거나, CORS / 404 / API path 문제를 혼동하는 경우가 많다.

Q. API 연동 문제는 어떻게 찾는 게 좋아?

A.
Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 먼저 확인한다.

---

# 24. Final Goal

## 24.1 Domain Final Goal

### [개념]

Data Fetching & REST API Integration RAG 문서는 Frontend Agent가 Backend REST API와 안정적으로 연동하고 요청 / 응답 / 상태 / 오류를 일관되게 처리하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- REST API 구조 이해
- HTTP Method 선택 기준 이해
- fetch / Axios 사용 기준 제공
- Axios Instance 설계
- Public API / Auth API 분리
- API Layer 분리
- Path Variable 처리
- Query Parameter 처리
- Request Body 처리
- Header / Authorization 처리
- Response DTO Mapping
- TypeScript Request / Response Type 작성
- Loading / Error / Empty State 처리
- TanStack Query 적용 판단
- queryKey 설계
- mutation / invalidation 처리
- Pagination / Slice / Infinite Scroll 처리
- File Upload 기초 처리
- CORS / 401 / 403 / 404 Troubleshooting
- Network Debugging 수행
- API Security 기본 주의사항 적용

---

### [실무]

Agent 수행 가능 작업:

```text
User API Integration Request
→ Read Backend API Spec
→ Define API Function
→ Choose publicApi or authApi
→ Build Params / Body / Header
→ Define Response Type
→ Connect Component or Query Hook
→ Handle Loading / Error / Empty
→ Debug Network Issues
→ REST API Integration Output
```

---

### [FAQ]

Q. Data Fetching 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 Backend REST API를 정확히 호출하고 응답 데이터를 안전하게 화면 상태와 연결하며 오류 상황까지 검토하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Authentication Frontend Flow, Form Handling & Validation, Error Handling & Loading UX, Frontend Testing 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Data Fetching 문서는 왜 필요해?
A. Frontend Agent가 Backend REST API를 호출하고 응답 데이터를 화면과 상태에 연결해야 하기 때문이다.

Q. REST API Integration이 뭐야?
A. Frontend가 HTTP Method, URL, Header, Body, Query Parameter를 사용해 Backend API와 데이터를 주고받는 작업이다.

Q. API 호출은 어디서 해?
A. 간단한 경우 Component에서 할 수 있지만 실무에서는 api 함수, custom hook, TanStack Query로 분리하는 것이 좋다.

Q. REST API는 Frontend에서 왜 알아야 해?
A. Frontend가 어떤 URL, Method, Parameter, Body, Header로 요청해야 하는지 알아야 Backend와 정상 연동할 수 있기 때문이다.

Q. GET과 POST 차이는?
A. GET은 데이터 조회에 사용하고 POST는 새로운 데이터 생성이나 명령성 요청에 사용한다.

Q. Request Body는 언제 써?
A. 데이터 생성, 수정, 로그인, 회원가입, 리뷰 작성처럼 서버에 JSON 데이터를 보낼 때 사용한다.

Q. GET 요청에도 body를 넣어도 돼?
A. 권장하지 않는다. 조회 조건은 보통 Query Parameter로 전달한다.

Q. Query Parameter는 언제 써?
A. 검색, 필터, 정렬, 페이지 번호처럼 리소스 조회 옵션을 전달할 때 사용한다.

Q. Path Variable은 언제 써?
A. 특정 리소스를 식별할 때 사용한다. 예: 축제 상세, 리뷰 삭제, 알림 읽음 처리.

Q. Path Variable과 Query Parameter 차이는?
A. Path Variable은 리소스 식별에 사용하고 Query Parameter는 검색, 필터, 정렬 같은 조회 옵션에 사용한다.

Q. URL에 undefined가 들어가는 이유는?
A. Route param이나 함수 인자가 undefined인데 검증 없이 문자열 template에 넣었을 가능성이 있다.

Q. Axios에서 query parameter는 어떻게 보내?
A. `axios.get(url, { params: { keyword: "flower" } })` 형태로 보낸다.

Q. Axios 응답 데이터는 어디에 있어?
A. 보통 `response.data`에 있다.

Q. Axios POST body는 어디에 넣어?
A. `axios.post(url, requestBody)`처럼 두 번째 인자에 넣는다.

Q. fetch는 404나 500이면 catch로 바로 가?
A. 아니다. 네트워크 오류가 아니면 catch로 바로 가지 않는다. response.ok를 직접 확인해야 한다.

Q. fetch POST에서 body는 왜 JSON.stringify를 해?
A. JavaScript 객체를 JSON 문자열로 변환해 서버에 보내야 하기 때문이다.

Q. fetch와 Axios 중 뭐가 좋아?
A. 간단한 요청은 fetch로 충분하고 공통 baseURL, interceptor, 응답 처리, 인증 헤더가 많으면 Axios가 편할 수 있다.

Q. fetch와 Axios를 같이 써도 돼?
A. 가능은 하지만 프로젝트 유지보수를 위해 하나의 API 호출 기준으로 통일하는 것이 좋다.

Q. Axios Instance는 왜 만들어?
A. baseURL, 인증 헤더, timeout, error handling 같은 공통 설정을 반복하지 않기 위해 만든다.

Q. publicApi와 authApi 차이는?
A. publicApi는 인증이 필요 없는 요청, authApi는 Authorization Header가 필요한 요청에 사용한다.

Q. Authorization Header는 어떤 형식이야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Authorization Header는 매 요청마다 직접 넣어야 해?
A. 가능하지만 interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. Axios Interceptor는 언제 써?
A. 인증 헤더 추가, 공통 에러 처리, 401 처리처럼 모든 요청에 반복되는 로직이 있을 때 사용한다.

Q. Interceptor에서 에러를 처리하고 끝내도 돼?
A. 대부분 Promise.reject로 다시 넘겨 호출부에서도 필요한 UI 처리를 할 수 있게 해야 한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증되지 않았거나 토큰이 유효하지 않은 경우이고 403은 인증은 되었지만 권한이 없는 경우다.

Q. API 함수를 왜 분리해?
A. Component가 URL, Method, Header 세부사항에 의존하지 않게 하고 재사용성과 테스트 가능성을 높이기 위해서다.

Q. API 함수 이름은 어떻게 지어?
A. getFestivals, getFestivalDetail, createReview, updateReview, deleteReview처럼 동작과 리소스가 드러나게 짓는다.

Q. Request Type과 Response Type은 나눠야 해?
A. 나누는 것이 좋다. 요청과 응답의 필드가 다를 수 있기 때문이다.

Q. response.data.data는 왜 나와?
A. Backend가 ApiResponse 같은 공통 wrapper로 응답하면 Axios response.data 안에 다시 data 필드가 있을 수 있다.

Q. Backend 응답 필드명이 바뀌면 어떻게 돼?
A. Frontend Type과 mapping 함수, Component에서 사용하는 필드명을 함께 수정해야 한다.

Q. API 응답 타입은 왜 필요해?
A. 응답 구조를 명확히 해 필드 오타와 null 처리 오류를 줄이기 위해 필요하다.

Q. 날짜 타입은 Date로 받아?
A. JSON 응답은 보통 문자열로 받는다. 필요하면 Frontend에서 Date 객체나 formatting 함수로 변환한다.

Q. Loading State는 왜 필요해?
A. API 요청 중 사용자에게 진행 상태를 알려주고 중복 클릭이나 빈 화면 혼란을 줄이기 위해 필요하다.

Q. Empty State와 Error State는 뭐가 달라?
A. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 자체가 실패한 상태다.

Q. 검색 결과가 없을 때는 에러야?
A. 아니다. 보통 정상 응답이지만 content가 비어 있는 Empty State다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. TanStack Query는 언제 써?
A. API 데이터 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. TanStack Query는 전역 상태관리 도구야?
A. 일반 Client State 전역 관리 도구라기보다 Server State와 API Cache 관리 도구다.

Q. queryKey에 params를 넣어야 해?
A. 검색 조건이나 페이지 번호가 바뀌면 다른 데이터이므로 queryKey에 포함해야 한다.

Q. queryKey가 틀리면 어떤 문제가 생겨?
A. 캐시가 중복되거나 invalidate가 제대로 되지 않아 화면 데이터가 갱신되지 않을 수 있다.

Q. mutation 후 목록이 안 바뀌어?
A. 관련 queryKey를 invalidate하지 않았거나 queryKey가 일치하지 않을 수 있다.

Q. invalidateQueries는 왜 써?
A. 서버 데이터가 변경되었으므로 기존 캐시를 무효화하고 최신 데이터를 다시 가져오기 위해 사용한다.

Q. Spring Pageable page는 0부터 시작해?
A. 일반적으로 0-based다. UI에서 1부터 보여주면 요청 시 변환이 필요할 수 있다.

Q. 검색 조건이 바뀌면 page는 어떻게 해?
A. 대부분 1페이지 또는 page 0으로 reset하는 것이 좋다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수와 totalPages를 제공하고 Slice는 다음 페이지 존재 여부 중심이라 더보기나 무한 스크롤에 적합하다.

Q. Infinite Scroll에서 중복 데이터가 생겨?
A. page 증가 타이밍, 중복 요청, 검색 조건 변경 시 초기화 누락을 확인해야 한다.

Q. 인증 필요한 API는 어떻게 구분해?
A. Authorization Header가 필요한 API는 authApi 같은 인증용 Axios Instance를 사용해 구분할 수 있다.

Q. token은 있는데 401이 나?
A. Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. 403이면 로그인 문제야?
A. 대부분 인증은 되었지만 권한이 부족한 경우다.

Q. access token이 만료되면 어떻게 해?
A. refresh token으로 새 access token을 요청하고 성공하면 원래 요청을 재시도할 수 있다.

Q. Refresh 요청도 실패하면?
A. 사용자를 logout 처리하고 login 페이지로 이동시키는 기준을 둔다.

Q. 프론트엔드 환경변수에 비밀키를 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 비밀키 저장에 부적합하다.

Q. 환경변수를 바꿨는데 적용이 안 돼?
A. 개발 서버를 재시작해야 반영되는 경우가 많다.

Q. Postman에서는 되는데 브라우저에서는 CORS 에러가 나?
A. Postman은 브라우저 CORS 정책을 적용하지 않기 때문이다. 브라우저 요청은 Backend CORS 설정이 필요하다.

Q. CORS는 Frontend에서 해결하는 문제야?
A. 대부분 Backend CORS 설정과 배포 구조에서 해결해야 한다. 개발 환경에서는 proxy를 사용할 수 있다.

Q. 파일 업로드는 JSON으로 보내?
A. 일반적으로 FormData와 multipart/form-data를 사용한다.

Q. FormData 보낼 때 Content-Type을 직접 multipart/form-data로 설정해야 해?
A. 대부분 직접 설정하지 않는 것이 좋다. 브라우저나 Axios가 boundary를 포함해 설정하도록 둔다.

Q. API 에러는 어떻게 분류해?
A. HTTP Status Code, 서버 응답 메시지, 네트워크 실패 여부를 기준으로 분류한다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. 서버 Validation Error는 어디에 보여줘?
A. 필드별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

Q. Client 검증이 있는데 Server 검증도 필요해?
A. 필요하다. Client 검증은 UX용이고 실제 데이터 검증은 Backend에서 반드시 수행해야 한다.

Q. API 연동이 안 될 때 제일 먼저 뭘 봐?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Status Code, Payload, Response Body를 확인한다.

Q. JSON을 기대했는데 HTML이 응답돼?
A. API 요청이 SPA fallback에 걸려 index.html을 받은 경우일 수 있다. 요청 URL과 서버 fallback 설정을 확인한다.

Q. CORS 에러는 왜 나?
A. 브라우저가 다른 Origin 요청을 제한하고 Backend가 해당 Origin, Method, Header를 허용하지 않기 때문이다.

Q. API 404가 나면 뭘 확인해?
A. Request URL, Method, baseURL, API prefix, Path Variable 값, Backend Controller Mapping을 확인한다.

Q. 페이지 이동 404와 API 404는 달라?
A. 다르다. 페이지 이동 404는 React Router 또는 서버 fallback 문제이고 API 404는 Backend endpoint 또는 resource 문제다.

Q. map is not a function 오류는 왜 나?
A. 배열이라고 생각한 값이 실제로는 객체이거나 undefined일 수 있다. 응답 구조와 content 위치를 확인해야 한다.

Q. Frontend .env에 API Secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 비밀키를 넣으면 안 된다.

Q. Frontend에서 권한 체크하면 API가 안전해져?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. Data Fetching 초보가 가장 많이 하는 실수는?
A. response.data 구조를 확인하지 않거나, 인증 헤더를 누락하거나, CORS / 404 / API path 문제를 혼동하는 경우가 많다.

Q. API 연동 문제는 어떻게 찾는 게 좋아?
A. Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 먼저 확인한다.

Q. Data Fetching 다음 문서는 뭐가 좋아?
A. Authentication Frontend Flow, Form Handling & Validation, Error Handling & Loading UX, Frontend Testing 순서가 좋다.
