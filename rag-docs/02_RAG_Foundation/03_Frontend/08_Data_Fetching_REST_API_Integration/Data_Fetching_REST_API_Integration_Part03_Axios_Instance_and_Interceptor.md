# Data Fetching & REST API Integration Part03 - Axios Instance and Interceptor

---

# 1. Axios Instance Overview

## 1.1 Axios Instance 기본 개념

### [개념]

Axios Instance는 `axios.create()`로 생성하는 공통 HTTP Client 객체다.

baseURL, timeout, default headers, request interceptor, response interceptor 같은 공통 설정을 하나의 Instance에 모아 API 요청 기준을 통일한다.

Frontend Agent는 API 함수 작성 시 직접 `axios.get()`을 남발하지 않고, 프로젝트 기준에 맞는 Axios Instance를 선택해야 한다.

기본 구조:

```text
axios.create()
→ publicApi / authApi 생성
→ API Function에서 Instance 사용
→ Request Interceptor 적용
→ HTTP Request
→ Response Interceptor 적용
→ Response DTO 반환
```

---

### [핵심]

Axios Instance 핵심 키워드:

- axios.create
- baseURL
- timeout
- headers
- publicApi
- authApi
- request interceptor
- response interceptor
- Authorization Header
- Bearer Token
- Access Token
- Refresh Token
- Error Handling
- 401 Handling
- 403 Handling
- API Layer
- Environment Variable

Axios Instance 목적:

- baseURL 반복 제거
- timeout 기준 통일
- Authorization Header 공통 처리
- public API / authenticated API 구분
- Response Error Handling 공통화
- API Layer 코드 단순화
- Backend API 경로 관리 기준 통일

---

### [실무]

2026 실무 기준에서 Axios Instance는 Frontend REST API Integration의 기본 인프라로 사용한다.

권장 구조:

```text
src
├ api
│  ├ axiosInstance.js
│  ├ festivalApi.js
│  ├ reviewApi.js
│  ├ notificationApi.js
│  └ authApi.js
├ hooks
├ pages
└ components
```

기본 Axios Instance 예:

```javascript
import axios from "axios";

const baseURL = process.env.REACT_APP_API_BASE_URL;

export const publicApi = axios.create({
  baseURL,
  timeout: 10000,
});

export const authApi = axios.create({
  baseURL,
  timeout: 10000,
});
```

실무 기준:

- API 함수는 `publicApi` 또는 `authApi`를 사용
- Component에서 직접 `axios.create()`하지 않음
- baseURL은 환경변수로 관리
- 인증 Header는 authApi request interceptor에서 처리
- response error는 interceptor 또는 공통 error mapper로 처리
- token refresh 심화는 Authentication Frontend Flow와 연계

---

### [FAQ]

Q. Axios Instance는 뭐야?
A. baseURL, timeout, headers, interceptor 같은 공통 설정을 가진 Axios 객체다.

Q. Axios Instance는 왜 만들어?
A. baseURL, 인증 헤더, timeout, error handling 같은 공통 설정을 반복하지 않기 위해 만든다.

Q. Component마다 axios.create를 해도 돼?
A. 권장하지 않는다. Axios Instance는 api layer에서 공통으로 만들고 재사용하는 것이 좋다.

Q. Axios Instance는 API 함수보다 먼저 만들어야 해?
A. 그렇다. API 함수는 이미 생성된 `publicApi` 또는 `authApi`를 사용해 요청을 보낸다.

---

# 2. Base URL Rules

## 2.1 baseURL 설정 기준

### [개념]

baseURL은 API 요청의 기본 서버 주소다.

Axios Instance에 baseURL을 설정하면 API 함수에서는 resource path만 작성할 수 있다.

예:

```text
baseURL = http://localhost:8080/api
path = /festivals
final URL = http://localhost:8080/api/festivals
```

---

### [핵심]

baseURL 핵심 키워드:

- baseURL
- API Server URL
- Environment Variable
- Development Server
- Production Server
- Proxy
- Relative URL
- Absolute URL
- CORS
- `/api` prefix
- trailing slash

baseURL 기준:

- 개발 / 운영 환경 분리
- 환경변수 사용
- Frontend secret 저장 금지
- `/api` prefix 포함 여부 통일
- path와 baseURL 사이 slash 중복 확인
- 환경변수 변경 후 dev server 재시작

---

### [실무]

CRA 기준:

```javascript
const baseURL = process.env.REACT_APP_API_BASE_URL;
```

Vite 기준:

```javascript
const baseURL = import.meta.env.VITE_API_BASE_URL;
```

Axios Instance 예:

```javascript
export const publicApi = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: 10000,
});
```

`.env` 예:

```env
REACT_APP_API_BASE_URL=http://localhost:8080/api
```

API 함수 예:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}
```

주의:

- CRA는 `REACT_APP_` prefix 필요
- Vite는 `VITE_` prefix 필요
- 환경변수 변경 후 개발 서버 재시작 필요
- Frontend 환경변수는 빌드 결과에 노출됨
- API Secret, Service Secret, Private Key 저장 금지
- 배포 환경 baseURL 확인 필요
- CORS 오류와 baseURL 오류를 구분

---

### [FAQ]

Q. baseURL은 왜 필요해?
A. API 서버 주소를 공통 설정으로 관리해 API 함수마다 전체 URL을 반복하지 않기 위해 필요하다.

Q. CRA에서 환경변수 이름은 어떻게 시작해야 해?
A. Create React App에서는 `REACT_APP_` prefix가 필요하다.

Q. Vite에서 환경변수 이름은 어떻게 시작해야 해?
A. Vite에서는 `VITE_` prefix가 필요하다.

Q. 환경변수를 바꿨는데 적용이 안 돼?
A. 개발 서버를 재시작해야 반영되는 경우가 많다.

---

# 3. Timeout Rules

## 3.1 timeout 설정 기준

### [개념]

timeout은 API 요청이 일정 시간 안에 응답하지 않을 때 요청을 실패 처리하는 기준이다.

Axios Instance에 timeout을 설정하면 모든 요청에 동일한 시간 제한을 적용할 수 있다.

---

### [핵심]

timeout 핵심 키워드:

- timeout
- Request Timeout
- Network Delay
- Server Delay
- AxiosError
- error.code
- ECONNABORTED
- User Message
- Retry
- Loading State

timeout 기준:

- 너무 짧으면 정상 요청도 실패 가능
- 너무 길면 사용자가 오래 기다림
- 사용자 메시지와 개발 로그 구분
- 파일 업로드 / 대용량 요청은 별도 기준 가능
- timeout 발생 시 Loading State 종료 필요

---

### [실무]

기본 timeout 설정:

```javascript
export const publicApi = axios.create({
  baseURL,
  timeout: 10000,
});
```

timeout Error Mapping:

```javascript
export function getApiErrorMessage(error) {
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

실무 처리 Flow:

```text
API Request
→ timeout 초과
→ AxiosError 발생
→ Loading 종료
→ 사용자 메시지 표시
→ 필요 시 재시도 버튼 제공
```

주의:

- timeout은 서버 오류 500과 다름
- CORS Error와 timeout을 혼동하지 않음
- Network 탭에서 요청 상태 확인
- 무한 Loading 방지
- 제출 요청은 timeout 후 중복 제출 방지 기준 필요

---

### [FAQ]

Q. timeout은 왜 설정해?
A. 서버 응답이 너무 오래 걸릴 때 무한 Loading을 방지하고 사용자에게 실패 상태를 보여주기 위해 설정한다.

Q. timeout이 나면 서버가 무조건 죽은 거야?
A. 아니다. 네트워크 지연, 서버 처리 지연, 프록시 문제 등 여러 원인이 가능하다.

Q. timeout과 500 에러는 같아?
A. 다르다. timeout은 응답을 제시간에 받지 못한 것이고 500은 서버가 내부 오류 응답을 보낸 것이다.

Q. timeout 시간은 모든 API에 같아야 해?
A. 기본값은 통일하되 파일 업로드나 대용량 요청은 별도 instance 또는 요청별 설정을 둘 수 있다.

---

# 4. publicApi and authApi Rules

## 4.1 publicApi 기준

### [개념]

`publicApi`는 인증이 필요 없는 공개 API 요청에 사용하는 Axios Instance다.

Authorization Header를 기본으로 포함하지 않는다.

---

### [핵심]

publicApi 사용 대상:

- 공개 목록 조회
- 공개 상세 조회
- 공개 검색
- 공개 필터 조회
- 로그인
- 회원가입
- 비밀번호 찾기
- 이메일 인증 요청
- 비로그인 사용자 접근 가능 API

publicApi 특징:

- Authorization Header 없음
- 인증 상태와 무관하게 호출 가능
- 공개 화면 API에 사용
- 로그인 전 요청에 사용
- CORS와 baseURL 기준은 동일하게 적용

---

### [실무]

publicApi 생성:

```javascript
export const publicApi = axios.create({
  baseURL,
  timeout: 10000,
});
```

공개 목록 조회:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data;
}
```

로그인 요청:

```javascript
export async function login(loginRequest) {
  const response = await publicApi.post("/auth/login", loginRequest);
  return response.data;
}
```

주의:

- 공개 API에 불필요한 token을 보내지 않음
- 로그인 API는 보통 publicApi 사용
- 회원가입 API도 보통 publicApi 사용
- 인증 필요 API를 publicApi로 호출하면 401 발생 가능
- API 명세의 인증 필요 여부를 기준으로 선택

---

### [FAQ]

Q. publicApi는 언제 써?
A. 인증이 필요 없는 목록 조회, 상세 조회, 로그인, 회원가입 같은 요청에 사용한다.

Q. 로그인 API는 publicApi야 authApi야?
A. 로그인 전 요청이므로 보통 publicApi를 사용한다.

Q. publicApi에는 Authorization Header가 없어?
A. 기본적으로 없다. 인증이 필요 없는 요청에 사용하기 때문이다.

Q. publicApi로 인증 API를 호출하면 어떻게 돼?
A. Authorization Header가 없어서 401 인증 실패가 발생할 수 있다.

---

## 4.2 authApi 기준

### [개념]

`authApi`는 로그인한 사용자만 접근할 수 있는 API 요청에 사용하는 Axios Instance다.

Authorization Header에 Bearer Access Token을 포함한다.

---

### [핵심]

authApi 사용 대상:

- 내 정보 조회
- 프로필 수정
- 찜 등록 / 취소
- 좋아요 등록 / 취소
- 리뷰 작성 / 수정 / 삭제
- 알림 조회
- 알림 읽음 처리
- 결제 요청
- 사용자 전용 데이터 조회

authApi 특징:

- Authorization Header 필요
- Bearer Token 사용
- request interceptor로 token 추가
- 401 처리 필요
- 403 처리 필요
- logout / login redirect와 연계 가능

---

### [실무]

authApi 생성:

```javascript
export const authApi = axios.create({
  baseURL,
  timeout: 10000,
});
```

Authorization Header 추가:

```javascript
authApi.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem("accessToken");

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

인증 API 함수:

```javascript
export async function getMyFavorites() {
  const response = await authApi.get("/favorites");
  return response.data;
}
```

리뷰 작성:

```javascript
export async function createReview(requestBody) {
  const response = await authApi.post("/reviews", requestBody);
  return response.data;
}
```

주의:

- token이 없으면 Header를 생략하거나 요청 전 차단
- Bearer prefix와 공백 확인
- token은 localStorage에 있어도 Header에 없으면 401 발생
- 401은 인증 실패 / 토큰 만료
- 403은 인증은 되었지만 권한 부족
- token storage 보안은 Authentication Frontend Flow에서 상세 관리

---

### [FAQ]

Q. authApi는 언제 써?
A. Authorization Header가 필요한 로그인 사용자 전용 API 요청에 사용한다.

Q. Authorization Header 형식은 뭐야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. token은 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. 403이면 로그인 문제야?
A. 대부분 인증은 되었지만 권한이 부족한 경우다.

---

# 5. Request Interceptor Rules

## 5.1 Request Interceptor 기본

### [개념]

Request Interceptor는 API 요청이 서버로 전송되기 전에 실행되는 공통 로직이다.

Authorization Header 추가, Request Logging, 공통 Header 설정에 사용할 수 있다.

---

### [핵심]

Request Interceptor 사용 대상:

- Authorization Header 추가
- Bearer Token 추가
- Request Config 수정
- 공통 Header 설정
- Request Logging
- Locale Header
- Request ID
- token 존재 여부 확인

Request Interceptor 주의:

- token이 없을 때 Header를 잘못 넣지 않음
- 민감 정보 로그 출력 금지
- config를 반드시 return
- 에러 발생 시 Promise.reject
- request interceptor에 너무 많은 책임 부여 금지

---

### [실무]

기본 Request Interceptor:

```javascript
authApi.interceptors.request.use(
  (config) => {
    const accessToken = localStorage.getItem("accessToken");

    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);
```

공통 Accept Header 예:

```javascript
publicApi.interceptors.request.use((config) => {
  config.headers.Accept = "application/json";
  return config;
});
```

Request Debug 주의:

```javascript
authApi.interceptors.request.use((config) => {
  // Authorization Header, token, 개인정보를 console.log로 노출하지 않음
  return config;
});
```

실무 기준:

- authApi에 Authorization Header 추가
- publicApi에는 기본적으로 token을 넣지 않음
- token이 null이면 Authorization Header 생략
- Header 확인은 Network 탭에서 수행
- refresh token 처리 심화는 별도 문서로 분리

---

### [FAQ]

Q. Request Interceptor는 언제 써?
A. Authorization Header 추가처럼 모든 인증 요청에 반복되는 요청 전 처리가 필요할 때 사용한다.

Q. Request Interceptor에서 config를 return해야 해?
A. 해야 한다. return하지 않으면 요청이 정상적으로 진행되지 않을 수 있다.

Q. Interceptor에서 token을 console.log로 찍어도 돼?
A. 권장하지 않는다. Authorization Header와 token은 민감정보이므로 로그 노출을 피해야 한다.

Q. publicApi에도 token을 넣어야 해?
A. 기본적으로 넣지 않는다. 인증이 필요한 요청은 authApi로 구분하는 것이 명확하다.

---

# 6. Response Interceptor Rules

## 6.1 Response Interceptor 기본

### [개념]

Response Interceptor는 서버 응답이 호출부로 전달되기 전에 실행되는 공통 로직이다.

공통 Error Handling, 401 처리, Response Data Unwrapping, Logging 등에 사용할 수 있다.

---

### [핵심]

Response Interceptor 사용 대상:

- Common Error Handling
- 401 Handling
- 403 Handling
- Token Expired Handling
- Refresh Token Flow Basics
- Logout Redirect
- Response Data Unwrapping
- Response Logging
- Global Error Mapping

Response Interceptor 주의:

- 모든 에러를 삼키지 않음
- `Promise.reject(error)`로 호출부에 전달
- 401 / 403 구분
- token refresh 무한 루프 방지
- response.data unwrap 기준 통일
- 화면별 UI 처리는 Component / hook에서 처리 가능

---

### [실무]

기본 Response Interceptor:

```javascript
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // token expired or unauthenticated
    }

    if (error.response?.status === 403) {
      // forbidden
    }

    return Promise.reject(error);
  },
);
```

Response Data Unwrapping 예:

```javascript
publicApi.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => Promise.reject(error),
);
```

응답을 강제로 `response.data`만 반환하는 방식도 가능하지만 신중해야 한다.

```javascript
publicApi.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error),
);
```

주의:

- `response.data` unwrap을 interceptor에서 하면 API 함수의 반환 타입 기준이 바뀜
- 프로젝트 전체에서 통일하지 않으면 혼란 발생
- TypeScript 사용 시 AxiosResponse 타입과 실제 반환 타입 차이 주의
- 에러를 interceptor에서 처리 후 숨기면 화면 Error State가 동작하지 않음

---

### [FAQ]

Q. Response Interceptor는 언제 써?
A. 401 처리, 공통 에러 처리, 응답 구조 정리처럼 모든 응답에 반복되는 처리가 필요할 때 사용한다.

Q. Interceptor에서 에러를 처리하고 끝내도 돼?
A. 대부분 `Promise.reject(error)`로 다시 넘겨 호출부에서도 필요한 UI 처리를 할 수 있게 해야 한다.

Q. Response Interceptor에서 response.data만 반환해도 돼?
A. 가능하지만 프로젝트 전체 반환 기준이 바뀌므로 반드시 일관되게 적용해야 한다.

Q. 401과 403은 Response Interceptor에서 같이 처리해도 돼?
A. 처리 위치는 같을 수 있지만 의미와 사용자 안내는 구분해야 한다.

---

# 7. Authorization Header Rules

## 7.1 Bearer Token Header 기준

### [개념]

Authorization Header는 인증이 필요한 API 요청에서 사용자의 Access Token을 서버에 전달하는 Header다.

일반적으로 Bearer Token 형식을 사용한다.

형식:

```text
Authorization: Bearer <accessToken>
```

---

### [핵심]

Authorization Header 핵심:

- Authorization
- Bearer Token
- Access Token
- authApi
- Request Interceptor
- 401
- 403
- token expired
- token missing
- invalid token

주의:

- `Bearer` 뒤 공백 필요
- token이 null이면 Header 생략
- token 문자열 앞뒤 공백 제거 검토
- localStorage에 token이 있어도 Header에 없으면 인증 실패
- 민감정보 로그 출력 금지
- CORS 허용 Header에 Authorization 필요

---

### [실무]

Authorization Header 설정:

```javascript
authApi.interceptors.request.use((config) => {
  const accessToken = localStorage.getItem("accessToken");

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

token 유틸 함수 분리:

```javascript
export function getAccessToken() {
  return localStorage.getItem("accessToken");
}
```

적용:

```javascript
authApi.interceptors.request.use((config) => {
  const accessToken = getAccessToken();

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

검증 Flow:

```text
401 발생
→ Network Tab
→ Request Headers
→ Authorization 존재 여부 확인
→ Bearer prefix 확인
→ token 만료 여부 확인
→ Backend Security Log 확인
```

---

### [FAQ]

Q. Authorization Header는 어떤 형식이야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Bearer 뒤에 공백이 꼭 필요해?
A. 필요하다. `Bearer <token>` 형식으로 공백이 포함되어야 한다.

Q. token은 localStorage에 있는데 왜 401이 나?
A. 실제 Request Header에 Authorization이 포함되지 않았거나 token이 만료되었을 수 있다.

Q. Authorization Header가 있으면 무조건 인증돼?
A. 아니다. token이 유효해야 하고 서버가 해당 token을 검증할 수 있어야 한다.

---

# 8. 401 / 403 Handling Rules

## 8.1 401 Handling 기준

### [개념]

401은 인증 실패 상태다.

Access Token이 없거나, 만료되었거나, 잘못되었거나, Authorization Header가 누락된 경우 발생할 수 있다.

---

### [핵심]

401 원인:

- Access Token 없음
- Authorization Header 누락
- Bearer 형식 오류
- token 만료
- token 위조
- refresh 실패
- 로그인하지 않은 사용자

401 처리 기준:

- 로그인 필요 메시지
- token 만료 메시지
- refresh token flow 시도 가능
- refresh 실패 시 logout
- login page redirect 가능
- 기존 사용자 상태 정리

---

### [실무]

401 Response Interceptor 예:

```javascript
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // clear token
      localStorage.removeItem("accessToken");

      // redirect or notify login required
    }

    return Promise.reject(error);
  },
);
```

주의:

- 모든 401에서 무조건 alert 남발 금지
- refresh token flow 사용 시 중복 refresh 방지 필요
- refresh 실패와 access token 만료를 구분
- 요청 재시도 무한 루프 방지
- 상세 구현은 Authentication Frontend Flow 문서로 분리

Debug Flow:

```text
401 발생
→ Authorization Header 확인
→ Bearer prefix 확인
→ token 존재 확인
→ token 만료 확인
→ refresh 가능 여부 확인
→ login redirect 여부 결정
```

---

### [FAQ]

Q. 401은 무슨 뜻이야?
A. 인증되지 않았거나 token이 유효하지 않다는 의미다.

Q. 401이 나오면 무조건 로그아웃해야 해?
A. 프로젝트 기준에 따라 다르다. refresh token flow가 있으면 token 재발급을 먼저 시도할 수 있다.

Q. token이 있는데 401이 나면 뭘 확인해?
A. Authorization Header 포함 여부, Bearer 형식, token 만료 여부, 서버 검증 실패 여부를 확인한다.

Q. 401과 로그인 페이지 이동은 어디서 처리해?
A. Response Interceptor, Auth Hook, Router Guard 등에서 처리할 수 있지만 프로젝트 기준을 통일해야 한다.

---

## 8.2 403 Handling 기준

### [개념]

403은 권한 없음 상태다.

사용자가 인증은 되었지만 해당 Resource나 API에 접근할 권한이 없을 때 발생한다.

---

### [핵심]

403 원인:

- ROLE 불일치
- 관리자 API 접근
- Resource Owner 불일치
- Backend Security 설정
- 권한 정책 불일치
- 인증은 되었지만 인가 실패

403 처리 기준:

- 권한 없음 메시지
- 이전 페이지 이동
- 접근 제한 UI 표시
- 관리자 권한 필요 안내
- 재로그인으로 해결되지 않을 수 있음
- Backend 권한 정책 확인

---

### [실무]

403 처리 예:

```javascript
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 403) {
      // show forbidden message
      // redirect to forbidden page if needed
    }

    return Promise.reject(error);
  },
);
```

Error Message Mapping:

```javascript
export function getApiErrorMessage(error) {
  if (axios.isAxiosError(error)) {
    if (error.response?.status === 403) {
      return "접근 권한이 없습니다.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

주의:

- 403을 401처럼 무조건 logout 처리하지 않음
- 권한 부족은 로그인 상태와 별개
- Frontend Route 접근 가능 여부와 Backend API 권한은 별개
- ROLE_USER / USER naming 불일치 확인
- Resource Owner 검증은 Backend 기준

---

### [FAQ]

Q. 403은 무슨 뜻이야?
A. 인증은 되었지만 해당 API나 Resource에 접근할 권한이 없다는 의미다.

Q. 403이면 다시 로그인하면 해결돼?
A. 항상 그렇지 않다. 권한 자체가 부족하면 다시 로그인해도 해결되지 않는다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증 후 권한 부족이다.

Q. 403은 Frontend에서 막으면 충분해?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 권한 검증은 Backend에서 해야 한다.

---

# 9. Token Refresh Basics

## 9.1 Token Refresh Interceptor 기초

### [개념]

Token Refresh는 Access Token이 만료되었을 때 Refresh Token으로 새 Access Token을 발급받고 원래 요청을 재시도하는 흐름이다.

이 문서에서는 Axios Interceptor에서 고려해야 하는 기초 기준만 다룬다.

상세 구현은 Authentication Frontend Flow Domain Rules에서 관리한다.

---

### [핵심]

Token Refresh Flow:

```text
API Request
→ 401 Token Expired
→ Refresh Request
→ New Access Token
→ Retry Original Request
→ If Refresh Failed
→ Logout / Login Redirect
```

핵심 키워드:

- Access Token
- Refresh Token
- 401
- retry original request
- refresh request
- duplicate refresh prevention
- infinite loop prevention
- logout
- login redirect

주의:

- refresh 요청 자체가 401이면 logout
- 원래 요청 retry는 1회 제한
- refresh 중 중복 요청 처리 필요
- refresh token 저장 위치 보안 검토
- 무한 refresh loop 금지
- refresh endpoint는 publicApi 또는 별도 instance 사용 가능

---

### [실무]

기초 retry flag 예:

```javascript
authApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      // refresh access token
      // originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
      // return authApi(originalRequest);
    }

    return Promise.reject(error);
  },
);
```

기초 Flow:

```text
401 발생
→ originalRequest 확인
→ _retry 여부 확인
→ refresh 요청
→ 새 accessToken 저장
→ originalRequest Authorization Header 갱신
→ 원래 요청 재시도
```

주의:

- 위 코드는 구조 예시이며 완성 구현이 아님
- refresh 중 여러 요청이 동시에 실패하면 큐 처리 필요 가능
- refresh 실패 시 token 제거와 사용자 상태 초기화
- refresh token을 Frontend에서 어디에 저장할지는 보안 요구사항에 따라 결정
- 인증 심화는 Authentication Frontend Flow 문서에서 다룸

---

### [FAQ]

Q. access token이 만료되면 어떻게 해?
A. refresh token으로 새 access token을 요청하고 성공하면 원래 요청을 재시도할 수 있다.

Q. Refresh 요청도 실패하면?
A. 사용자를 logout 처리하고 login 페이지로 이동시키는 기준을 둔다.

Q. Token Refresh를 Response Interceptor에서 구현해도 돼?
A. 가능하지만 중복 refresh, 무한 loop, retry 처리 기준을 신중하게 설계해야 한다.

Q. Token Refresh 상세 구현은 이 문서 범위야?
A. 아니다. 이 문서는 기초 기준만 다루고 상세 인증 흐름은 Authentication Frontend Flow 문서에서 다룬다.

---

# 10. Response Data Unwrapping Rules

## 10.1 Response Unwrapping 기준

### [개념]

Response Data Unwrapping은 Backend 응답 Wrapper에서 실제 data만 꺼내 API 함수나 Component에 전달하는 방식이다.

예:

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

실제 데이터:

```text
response.data.data
```

---

### [핵심]

Unwrapping 위치 선택:

- API 함수에서 unwrap
- Response Interceptor에서 unwrap
- Custom fetcher에서 unwrap
- Component에서 unwrap

권장:

- 프로젝트 전체 기준 통일
- Component에서 wrapper 구조를 반복해서 알지 않게 함
- API 함수 또는 custom fetcher에서 처리 권장
- Interceptor unwrap은 타입 혼란 주의
- Page / Slice 응답의 content 위치 확인

주의:

- `response.data`는 Axios Response Body
- `response.data.data`는 Backend ApiResponse data
- interceptor에서 `response.data`만 반환하면 API 함수 코드 기준 변경
- TypeScript AxiosResponse 타입과 충돌 가능
- Error Response Shape와 Success Response Shape 구분

---

### [실무]

API 함수에서 unwrap:

```javascript
export async function getFestivalDetail(festivalId) {
  const response = await publicApi.get(`/festivals/${festivalId}`);
  return response.data.data;
}
```

목록 content까지 unwrap:

```javascript
export async function getFestivals(params) {
  const response = await publicApi.get("/festivals", { params });
  return response.data.data.content;
}
```

Interceptor에서 unwrap:

```javascript
publicApi.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error),
);
```

Interceptor unwrap 사용 시 API 함수:

```javascript
export async function getFestivalDetail(festivalId) {
  const body = await publicApi.get(`/festivals/${festivalId}`);
  return body.data;
}
```

실무 주의:

```text
Interceptor unwrap 적용 전: response.data.data
Interceptor unwrap 적용 후: body.data
```

프로젝트 중간에 기준이 섞이면 Response Shape Mismatch가 발생한다.

---

### [FAQ]

Q. response.data.data는 왜 나와?
A. Axios의 `response.data` 안에 Backend ApiResponse의 `data` 필드가 다시 있기 때문이다.

Q. Unwrapping은 어디서 하는 게 좋아?
A. API 함수나 custom fetcher에서 일관되게 처리하는 방식이 안전하다.

Q. Interceptor에서 response.data만 반환하면 편하지 않아?
A. 편할 수 있지만 API 함수 반환 타입 기준이 바뀌므로 프로젝트 전체에서 통일해야 한다.

Q. map is not a function은 Unwrapping 문제일 수 있어?
A. 그렇다. 배열이 아니라 wrapper 객체에 `.map()`을 호출하면 발생할 수 있다.

---

# 11. Error Mapping Rules

## 11.1 공통 Error Mapping 기준

### [개념]

Error Mapping은 AxiosError를 사용자에게 보여줄 메시지나 화면 상태로 변환하는 작업이다.

API Error는 상태 코드와 원인에 따라 분류해야 한다.

---

### [핵심]

Error Mapping 대상:

- 400 Bad Request
- 401 Unauthenticated
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 500 Server Error
- Network Error
- Timeout Error
- CORS Error
- Unknown Error

처리 기준:

- 사용자 메시지와 개발 로그 구분
- 서버 원문 메시지 직접 노출 주의
- 401 / 403 구분
- Validation Error는 field별 처리 가능
- Network Error는 연결 문제 안내
- Timeout은 요청 시간 초과 안내

---

### [실무]

공통 Error Mapper:

```javascript
import axios from "axios";

export function getApiErrorMessage(error) {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

    if (error.code === "ECONNABORTED") {
      return "요청 시간이 초과되었습니다.";
    }

    if (!error.response) {
      return "네트워크 연결을 확인해 주세요.";
    }

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

    if (status === 409) {
      return "요청한 작업이 현재 상태와 충돌합니다.";
    }

    if (status === 422) {
      return "입력값을 다시 확인해 주세요.";
    }

    if (status && status >= 500) {
      return "서버 오류가 발생했습니다.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

Component 적용:

```javascript
try {
  const data = await getFestivals(params);
  setFestivals(data.content);
} catch (error) {
  setErrorMessage(getApiErrorMessage(error));
}
```

주의:

- 사용자에게 stack trace 노출 금지
- token, 개인정보, 서버 내부 메시지 노출 금지
- 개발 로그는 별도 로깅 기준 사용
- Error Boundary와 API Error State 구분

---

### [FAQ]

Q. API 에러는 어떻게 분류해?
A. HTTP Status Code, 서버 응답 메시지, 네트워크 실패 여부를 기준으로 분류한다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. Validation Error는 어떻게 처리해?
A. field별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

---

# 12. Axios Instance File Structure

## 12.1 axiosInstance 파일 구조

### [개념]

Axios Instance 파일은 프로젝트의 API 요청 공통 설정을 모아두는 파일이다.

보통 `src/api/axiosInstance.js` 또는 `src/api/axiosInstance.ts`에 작성한다.

---

### [핵심]

파일에 포함할 수 있는 요소:

- axios import
- baseURL
- publicApi
- authApi
- request interceptor
- response interceptor
- token getter
- error handling basics
- export

분리 가능한 요소:

- tokenStorage.js
- errorMapper.js
- authService.js
- refreshToken.js
- apiClient.js

주의:

- 파일 하나에 모든 인증 로직을 과도하게 몰아넣지 않음
- 순환 참조 주의
- Router navigation 직접 호출 시 구조 주의
- token refresh가 복잡하면 별도 모듈화

---

### [실무]

기본 구조:

```javascript
import axios from "axios";

const baseURL = process.env.REACT_APP_API_BASE_URL;

export const publicApi = axios.create({
  baseURL,
  timeout: 10000,
});

export const authApi = axios.create({
  baseURL,
  timeout: 10000,
});

authApi.interceptors.request.use(
  (config) => {
    const accessToken = localStorage.getItem("accessToken");

    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    return config;
  },
  (error) => Promise.reject(error),
);

authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("accessToken");
    }

    return Promise.reject(error);
  },
);
```

API 함수 파일:

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

- Instance 생성 파일과 API 함수 파일 분리
- API 함수는 도메인별 파일로 분리
- 인증 token 관리 유틸은 별도 분리 가능
- Error Mapper는 별도 파일로 분리 가능
- TypeScript 프로젝트는 Response Type과 함께 관리

---

### [FAQ]

Q. axiosInstance.js에는 뭘 넣어?
A. publicApi, authApi, baseURL, timeout, interceptor 같은 공통 요청 설정을 넣는다.

Q. festivalApi.js에는 뭘 넣어?
A. 축제 목록 조회, 상세 조회, 검색 같은 축제 도메인 API 함수를 넣는다.

Q. 모든 API 함수를 axiosInstance.js에 넣어도 돼?
A. 권장하지 않는다. Instance 설정 파일과 도메인 API 함수 파일을 분리하는 것이 유지보수에 좋다.

Q. token 관리 함수는 어디에 둬?
A. 간단하면 axiosInstance 안에 둘 수 있지만, 프로젝트가 커지면 tokenStorage 같은 별도 유틸로 분리한다.

---

# 13. TypeScript Axios Instance Rules

## 13.1 TypeScript 적용 기준

### [개념]

TypeScript에서 Axios Instance를 사용할 때는 Request Type, Response Type, ApiResponse Generic, Page Response Type을 명확히 정의하는 것이 좋다.

API 함수 반환 타입은 실제 unwrap 기준과 일치해야 한다.

---

### [핵심]

TypeScript 핵심 키워드:

- Request Type
- Response Type
- ApiResponse<T>
- PageResponse<T>
- SliceResponse<T>
- AxiosResponse
- AxiosError
- Generic
- nullable field
- enum union type

주의:

- `AxiosResponse<ApiResponse<T>>`와 실제 반환 타입 구분
- interceptor unwrap 사용 시 타입 보정 필요
- `any` 남용 금지
- null 가능성 반영
- Backend DTO 변경 시 Type 동기화

---

### [실무]

공통 ApiResponse Type:

```typescript
export type ApiResponse<T> = {
  success: boolean;
  message: string;
  data: T;
};
```

목록 Response Type:

```typescript
export type FestivalSummaryResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  regionName: string;
};
```

API 함수 Type:

```typescript
export async function getFestivalDetail(
  festivalId: number,
): Promise<FestivalSummaryResponse> {
  const response = await publicApi.get<ApiResponse<FestivalSummaryResponse>>(
    `/festivals/${festivalId}`,
  );

  return response.data.data;
}
```

Page Response Type:

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

Page API 함수:

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

---

### [FAQ]

Q. API 응답 타입은 왜 필요해?
A. 응답 구조를 명확히 해 필드 오타와 null 처리 오류를 줄이기 위해 필요하다.

Q. ApiResponse<T>는 왜 써?
A. Backend 공통 응답 wrapper를 TypeScript Generic으로 표현하기 위해 사용한다.

Q. AxiosResponse 타입을 그대로 반환해도 돼?
A. 가능하지만 Component가 Axios 세부 구조에 의존하므로 API 함수에서 실제 data만 반환하는 방식이 더 깔끔할 수 있다.

Q. interceptor에서 response.data만 반환하면 TypeScript 타입은 어떻게 돼?
A. Axios 기본 타입과 실제 반환값이 달라질 수 있으므로 타입 보정이 필요하다.

---

# 14. Environment Security Rules

## 14.1 Frontend 환경변수 보안 기준

### [개념]

Frontend 환경변수는 빌드 결과에 포함될 수 있으므로 비밀값 저장에 적합하지 않다.

API baseURL처럼 공개되어도 되는 설정값은 가능하지만, secret key는 저장하면 안 된다.

---

### [핵심]

Frontend 환경변수에 가능:

- API baseURL
- public asset URL
- 공개 가능한 client config
- feature flag basics

Frontend 환경변수에 금지:

- API Secret
- Private Key
- Database Password
- OAuth Client Secret
- Admin Token
- Service Account Key
- Refresh Token
- 결제 secret key

주의:

- `.env`에 넣어도 Frontend secret은 안전하지 않음
- React 코드에 secret hardcoding 금지
- 외부 API secret은 Backend Proxy 검토
- token과 개인정보 console.log 금지
- 배포 환경변수도 client bundle 노출 가능성 고려

---

### [실무]

가능한 예:

```env
REACT_APP_API_BASE_URL=https://api.example.com
```

금지 예:

```env
REACT_APP_PAYMENT_SECRET_KEY=secret_xxx
REACT_APP_ADMIN_TOKEN=admin_xxx
```

외부 API Secret이 필요한 경우:

```text
Frontend
→ Backend Proxy API
→ External API with Secret
→ Backend Response
→ Frontend
```

실무 기준:

- Frontend에는 공개 가능한 key만 둠
- Secret이 필요한 API 호출은 Backend에서 처리
- API Key가 공개되어도 되는 종류인지 문서 확인
- 보안 판단이 애매하면 Backend Proxy 우선 검토

---

### [FAQ]

Q. Frontend .env에 API Secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 비밀키를 넣으면 안 된다.

Q. `.env` 파일이면 안전한 거 아니야?
A. Backend 환경변수와 다르다. Frontend 환경변수는 빌드된 JavaScript에 포함될 수 있다.

Q. 외부 API Secret은 어디에 둬야 해?
A. Backend 서버 환경변수에 두고 Frontend는 Backend API를 통해 간접 호출하는 방식이 안전하다.

Q. baseURL은 Frontend 환경변수에 넣어도 돼?
A. 가능하다. baseURL은 보통 공개되어도 되는 설정값이다.

---

# 15. Network Debugging for Axios Instance

## 15.1 Axios Instance 디버깅 기준

### [개념]

Axios Instance 디버깅은 실제 요청에 baseURL, path, params, body, Authorization Header, timeout, response가 의도대로 적용되었는지 확인하는 과정이다.

Network 탭 확인이 우선이다.

---

### [핵심]

확인 대상:

- Request URL
- baseURL 적용 여부
- path 중복 여부
- `/api` prefix 여부
- Request Method
- Query String
- Request Payload
- Authorization Header
- Bearer prefix
- Status Code
- Response Body
- CORS Error
- Timeout Error

---

### [실무]

Debug Flow:

```text
API Problem
→ Network Tab Open
→ Request URL 확인
→ Method 확인
→ Query String 확인
→ Payload 확인
→ Request Headers 확인
→ Authorization Header 확인
→ Status Code 확인
→ Response Body 확인
→ Axios Error Mapping 확인
```

상황별 확인:

```text
401 발생
→ authApi 사용 여부 확인
→ Authorization Header 확인
→ Bearer prefix 확인
→ token 만료 확인
```

```text
404 발생
→ baseURL 확인
→ /api prefix 확인
→ resource path 확인
→ Backend Mapping 확인
```

```text
데이터 undefined
→ response.data 구조 확인
→ ApiResponse wrapper 확인
→ unwrap 기준 확인
```

```text
CORS 발생
→ Browser Console 확인
→ preflight OPTIONS 확인
→ Backend CORS 설정 확인
→ Authorization Header 허용 여부 확인
```

주의:

- Postman 성공과 Browser 성공은 다름
- localStorage token 존재와 Request Header 포함은 다름
- Console 에러만 보지 말고 Network Response Body 확인
- API 요청이 HTML을 받으면 SPA fallback 가능성 확인

---

### [FAQ]

Q. Axios Instance 문제는 어디서 확인해?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 확인한다.

Q. token은 있는데 401이 나면 어디를 봐?
A. Network Request Headers에서 Authorization Header가 실제로 들어갔는지 확인한다.

Q. response.data가 undefined면 뭘 확인해?
A. 실제 Response Body 구조와 ApiResponse wrapper, interceptor unwrap 기준을 확인한다.

Q. Postman에서는 되는데 브라우저에서만 안 돼?
A. CORS, Authorization Header 허용, credentials, Origin 정책 문제일 수 있다.

---

# 16. Common Mistakes

## 16.1 Axios Instance 공통 실수

### [개념]

Axios Instance 실수는 공통 설정, 인증 Header, response unwrap, error handling 기준이 프로젝트 전체에서 통일되지 않아 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Direct Axios와 Axios Instance 혼용
- publicApi / authApi 구분 누락
- 인증 API를 publicApi로 호출
- 공개 API를 authApi로 호출해 불필요한 Header 전송
- baseURL에 `/api` prefix 중복
- path에 `/api` prefix 중복
- 환경변수 prefix 오류
- 환경변수 변경 후 dev server 미재시작
- Authorization Header 누락
- Bearer prefix 누락
- token이 localStorage에 있으면 자동 전송된다고 착각
- interceptor에서 config return 누락
- interceptor에서 error를 삼킴
- response.data unwrap 기준 혼용
- 401과 403을 같은 에러로 처리
- refresh retry 무한 loop
- Frontend .env에 secret key 저장
- Network 탭 확인 없이 코드만 수정

---

### [실무]

문제 해결 우선순위:

```text
1. 사용한 Instance 확인
2. baseURL 확인
3. Request URL 확인
4. Request Method 확인
5. Query String / Payload 확인
6. Authorization Header 확인
7. Status Code 확인
8. Response Body 확인
9. Interceptor 동작 확인
10. Error Mapping 확인
```

문제 예:

```text
문제: 인증 API에서 401 발생
원인: authApi가 아니라 publicApi로 요청
해결: API 함수에서 authApi 사용
```

문제 예:

```text
문제: API URL이 /api/api/festivals로 요청됨
원인: baseURL과 path 양쪽에 /api prefix 포함
해결: baseURL과 API path prefix 기준 통일
```

문제 예:

```text
문제: response.data.data가 undefined
원인: Response Interceptor에서 이미 response.data를 반환하도록 설정
해결: unwrap 기준을 프로젝트 전체에서 통일
```

문제 예:

```text
문제: token은 localStorage에 있는데 Header가 없음
원인: Request Interceptor 미적용 또는 authApi 미사용
해결: authApi interceptor와 API 함수 import 확인
```

---

### [FAQ]

Q. Axios Instance에서 가장 흔한 실수는?
A. publicApi와 authApi를 잘못 선택하거나 response.data unwrap 기준을 혼용하는 것이다.

Q. `/api/api`처럼 URL이 중복되는 이유는?
A. baseURL과 API path 양쪽에 `/api` prefix를 넣었기 때문이다.

Q. token이 localStorage에 있으면 자동으로 Header에 들어가?
A. 아니다. Request Interceptor나 직접 Header 설정이 있어야 Authorization Header에 포함된다.

Q. Interceptor에서 에러를 return만 하면 돼?
A. 보통 `Promise.reject(error)`로 넘겨 호출부에서 Error State를 처리할 수 있게 해야 한다.

---

# 17. Part03 Checklist

## 17.1 Axios Instance and Interceptor 검수 기준

### [개념]

Part03 Axios Instance and Interceptor 문서는 Frontend Agent가 공통 API Client를 설계하고, publicApi / authApi / interceptor / error mapping 기준을 적용할 수 있도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] Axios Instance 기본 개념이 포함되었는가?
- [ ] baseURL 설정 기준이 포함되었는가?
- [ ] 환경변수 기준이 포함되었는가?
- [ ] timeout 기준이 포함되었는가?
- [ ] publicApi 기준이 포함되었는가?
- [ ] authApi 기준이 포함되었는가?
- [ ] Request Interceptor 기준이 포함되었는가?
- [ ] Response Interceptor 기준이 포함되었는가?
- [ ] Authorization Header 기준이 포함되었는가?
- [ ] 401 Handling 기준이 포함되었는가?
- [ ] 403 Handling 기준이 포함되었는가?
- [ ] Token Refresh 기초 기준이 포함되었는가?
- [ ] Response Data Unwrapping 기준이 포함되었는가?
- [ ] Error Mapping 기준이 포함되었는가?
- [ ] axiosInstance 파일 구조가 포함되었는가?
- [ ] TypeScript Axios Instance 기준이 포함되었는가?
- [ ] Frontend 환경변수 보안 기준이 포함되었는가?
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
→ Axios Instance Check
→ baseURL / env Check
→ publicApi / authApi Check
→ Request Interceptor Check
→ Response Interceptor Check
→ Authorization Header Check
→ Error Handling Check
→ Response Unwrap Check
→ Security Check
→ Debugging Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Axios Instance 생성 가능
- publicApi와 authApi 구분 가능
- Authorization Header를 interceptor로 처리 가능
- 401과 403을 구분 가능
- Response unwrap 기준을 통일 가능
- 환경변수와 secret key를 구분 가능
- Network 탭으로 Header / URL / Response 문제를 검증 가능
- Frontend Agent가 안정적인 API Client 코드를 생성 가능

---

### [FAQ]

Q. Part03의 목적은 뭐야?
A. Frontend Agent가 Axios Instance, publicApi, authApi, interceptor, error mapping 기준을 이해하고 공통 API Client를 설계하게 만드는 것이다.

Q. Part03에서 가장 중요한 기준은 뭐야?
A. publicApi / authApi 구분, Authorization Header 처리, response unwrap 기준 통일, 401 / 403 구분이다.

Q. Part03 다음에는 어떤 문서가 이어지면 좋아?
A. API Layer Separation, Request / Response Type Mapping, UI State, TanStack Query 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Axios Instance는 뭐야?
A. baseURL, timeout, headers, interceptor 같은 공통 설정을 가진 Axios 객체다.

Q. Axios Instance는 왜 만들어?
A. baseURL, 인증 헤더, timeout, error handling 같은 공통 설정을 반복하지 않기 위해 만든다.

Q. Component마다 axios.create를 해도 돼?
A. 권장하지 않는다. Axios Instance는 api layer에서 공통으로 만들고 재사용하는 것이 좋다.

Q. Axios Instance는 API 함수보다 먼저 만들어야 해?
A. 그렇다. API 함수는 이미 생성된 `publicApi` 또는 `authApi`를 사용해 요청을 보낸다.

Q. baseURL은 왜 필요해?
A. API 서버 주소를 공통 설정으로 관리해 API 함수마다 전체 URL을 반복하지 않기 위해 필요하다.

Q. CRA에서 환경변수 이름은 어떻게 시작해야 해?
A. Create React App에서는 `REACT_APP_` prefix가 필요하다.

Q. Vite에서 환경변수 이름은 어떻게 시작해야 해?
A. Vite에서는 `VITE_` prefix가 필요하다.

Q. 환경변수를 바꿨는데 적용이 안 돼?
A. 개발 서버를 재시작해야 반영되는 경우가 많다.

Q. timeout은 왜 설정해?
A. 서버 응답이 너무 오래 걸릴 때 무한 Loading을 방지하고 사용자에게 실패 상태를 보여주기 위해 설정한다.

Q. timeout이 나면 서버가 무조건 죽은 거야?
A. 아니다. 네트워크 지연, 서버 처리 지연, 프록시 문제 등 여러 원인이 가능하다.

Q. timeout과 500 에러는 같아?
A. 다르다. timeout은 응답을 제시간에 받지 못한 것이고 500은 서버가 내부 오류 응답을 보낸 것이다.

Q. publicApi는 언제 써?
A. 인증이 필요 없는 목록 조회, 상세 조회, 로그인, 회원가입 같은 요청에 사용한다.

Q. 로그인 API는 publicApi야 authApi야?
A. 로그인 전 요청이므로 보통 publicApi를 사용한다.

Q. publicApi에는 Authorization Header가 없어?
A. 기본적으로 없다. 인증이 필요 없는 요청에 사용하기 때문이다.

Q. publicApi로 인증 API를 호출하면 어떻게 돼?
A. Authorization Header가 없어서 401 인증 실패가 발생할 수 있다.

Q. authApi는 언제 써?
A. Authorization Header가 필요한 로그인 사용자 전용 API 요청에 사용한다.

Q. Authorization Header 형식은 뭐야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. token은 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. 403이면 로그인 문제야?
A. 대부분 인증은 되었지만 권한이 부족한 경우다.

Q. Request Interceptor는 언제 써?
A. Authorization Header 추가처럼 모든 인증 요청에 반복되는 요청 전 처리가 필요할 때 사용한다.

Q. Request Interceptor에서 config를 return해야 해?
A. 해야 한다. return하지 않으면 요청이 정상적으로 진행되지 않을 수 있다.

Q. Interceptor에서 token을 console.log로 찍어도 돼?
A. 권장하지 않는다. Authorization Header와 token은 민감정보이므로 로그 노출을 피해야 한다.

Q. publicApi에도 token을 넣어야 해?
A. 기본적으로 넣지 않는다. 인증이 필요한 요청은 authApi로 구분하는 것이 명확하다.

Q. Response Interceptor는 언제 써?
A. 401 처리, 공통 에러 처리, 응답 구조 정리처럼 모든 응답에 반복되는 처리가 필요할 때 사용한다.

Q. Interceptor에서 에러를 처리하고 끝내도 돼?
A. 대부분 `Promise.reject(error)`로 다시 넘겨 호출부에서도 필요한 UI 처리를 할 수 있게 해야 한다.

Q. Response Interceptor에서 response.data만 반환해도 돼?
A. 가능하지만 프로젝트 전체 반환 기준이 바뀌므로 반드시 일관되게 적용해야 한다.

Q. 401과 403은 Response Interceptor에서 같이 처리해도 돼?
A. 처리 위치는 같을 수 있지만 의미와 사용자 안내는 구분해야 한다.

Q. Bearer 뒤에 공백이 꼭 필요해?
A. 필요하다. `Bearer <token>` 형식으로 공백이 포함되어야 한다.

Q. Authorization Header가 있으면 무조건 인증돼?
A. 아니다. token이 유효해야 하고 서버가 해당 token을 검증할 수 있어야 한다.

Q. 401은 무슨 뜻이야?
A. 인증되지 않았거나 token이 유효하지 않다는 의미다.

Q. 401이 나오면 무조건 로그아웃해야 해?
A. 프로젝트 기준에 따라 다르다. refresh token flow가 있으면 token 재발급을 먼저 시도할 수 있다.

Q. token이 있는데 401이 나면 뭘 확인해?
A. Authorization Header 포함 여부, Bearer 형식, token 만료 여부, 서버 검증 실패 여부를 확인한다.

Q. 401과 로그인 페이지 이동은 어디서 처리해?
A. Response Interceptor, Auth Hook, Router Guard 등에서 처리할 수 있지만 프로젝트 기준을 통일해야 한다.

Q. 403은 무슨 뜻이야?
A. 인증은 되었지만 해당 API나 Resource에 접근할 권한이 없다는 의미다.

Q. 403이면 다시 로그인하면 해결돼?
A. 항상 그렇지 않다. 권한 자체가 부족하면 다시 로그인해도 해결되지 않는다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증 후 권한 부족이다.

Q. 403은 Frontend에서 막으면 충분해?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 권한 검증은 Backend에서 해야 한다.

Q. access token이 만료되면 어떻게 해?
A. refresh token으로 새 access token을 요청하고 성공하면 원래 요청을 재시도할 수 있다.

Q. Refresh 요청도 실패하면?
A. 사용자를 logout 처리하고 login 페이지로 이동시키는 기준을 둔다.

Q. Token Refresh를 Response Interceptor에서 구현해도 돼?
A. 가능하지만 중복 refresh, 무한 loop, retry 처리 기준을 신중하게 설계해야 한다.

Q. Token Refresh 상세 구현은 이 문서 범위야?
A. 아니다. 이 문서는 기초 기준만 다루고 상세 인증 흐름은 Authentication Frontend Flow 문서에서 다룬다.

Q. response.data.data는 왜 나와?
A. Axios의 `response.data` 안에 Backend ApiResponse의 `data` 필드가 다시 있기 때문이다.

Q. Unwrapping은 어디서 하는 게 좋아?
A. API 함수나 custom fetcher에서 일관되게 처리하는 방식이 안전하다.

Q. Interceptor에서 response.data만 반환하면 편하지 않아?
A. 편할 수 있지만 API 함수 반환 타입 기준이 바뀌므로 프로젝트 전체에서 통일해야 한다.

Q. map is not a function은 Unwrapping 문제일 수 있어?
A. 그렇다. 배열이 아니라 wrapper 객체에 `.map()`을 호출하면 발생할 수 있다.

Q. API 에러는 어떻게 분류해?
A. HTTP Status Code, 서버 응답 메시지, 네트워크 실패 여부를 기준으로 분류한다.

Q. API 에러 메시지는 그대로 보여줘도 돼?
A. 민감한 정보가 포함될 수 있으므로 사용자에게 보여줄 메시지와 개발자 로그를 구분하는 것이 좋다.

Q. 500 에러 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 일반 메시지를 보여주고 상세 내용은 개발 로그로 확인한다.

Q. Validation Error는 어떻게 처리해?
A. field별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시하는 것이 좋다.

Q. axiosInstance.js에는 뭘 넣어?
A. publicApi, authApi, baseURL, timeout, interceptor 같은 공통 요청 설정을 넣는다.

Q. festivalApi.js에는 뭘 넣어?
A. 축제 목록 조회, 상세 조회, 검색 같은 축제 도메인 API 함수를 넣는다.

Q. 모든 API 함수를 axiosInstance.js에 넣어도 돼?
A. 권장하지 않는다. Instance 설정 파일과 도메인 API 함수 파일을 분리하는 것이 유지보수에 좋다.

Q. token 관리 함수는 어디에 둬?
A. 간단하면 axiosInstance 안에 둘 수 있지만, 프로젝트가 커지면 tokenStorage 같은 별도 유틸로 분리한다.

Q. API 응답 타입은 왜 필요해?
A. 응답 구조를 명확히 해 필드 오타와 null 처리 오류를 줄이기 위해 필요하다.

Q. ApiResponse<T>는 왜 써?
A. Backend 공통 응답 wrapper를 TypeScript Generic으로 표현하기 위해 사용한다.

Q. AxiosResponse 타입을 그대로 반환해도 돼?
A. 가능하지만 Component가 Axios 세부 구조에 의존하므로 API 함수에서 실제 data만 반환하는 방식이 더 깔끔할 수 있다.

Q. interceptor에서 response.data만 반환하면 TypeScript 타입은 어떻게 돼?
A. Axios 기본 타입과 실제 반환값이 달라질 수 있으므로 타입 보정이 필요하다.

Q. Frontend .env에 API Secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 비밀키를 넣으면 안 된다.

Q. `.env` 파일이면 안전한 거 아니야?
A. Backend 환경변수와 다르다. Frontend 환경변수는 빌드된 JavaScript에 포함될 수 있다.

Q. 외부 API Secret은 어디에 둬야 해?
A. Backend 서버 환경변수에 두고 Frontend는 Backend API를 통해 간접 호출하는 방식이 안전하다.

Q. baseURL은 Frontend 환경변수에 넣어도 돼?
A. 가능하다. baseURL은 보통 공개되어도 되는 설정값이다.

Q. Axios Instance 문제는 어디서 확인해?
A. 브라우저 개발자 도구 Network 탭에서 실제 Request URL, Method, Header, Payload, Status Code, Response Body를 확인한다.

Q. response.data가 undefined면 뭘 확인해?
A. 실제 Response Body 구조와 ApiResponse wrapper, interceptor unwrap 기준을 확인한다.

Q. Postman에서는 되는데 브라우저에서만 안 돼?
A. CORS, Authorization Header 허용, credentials, Origin 정책 문제일 수 있다.

Q. Axios Instance에서 가장 흔한 실수는?
A. publicApi와 authApi를 잘못 선택하거나 response.data unwrap 기준을 혼용하는 것이다.

Q. `/api/api`처럼 URL이 중복되는 이유는?
A. baseURL과 API path 양쪽에 `/api` prefix를 넣었기 때문이다.

Q. token이 localStorage에 있으면 자동으로 Header에 들어가?
A. 아니다. Request Interceptor나 직접 Header 설정이 있어야 Authorization Header에 포함된다.

Q. Interceptor에서 에러를 return만 하면 돼?
A. 보통 `Promise.reject(error)`로 넘겨 호출부에서 Error State를 처리할 수 있게 해야 한다.

Q. Part03 Axios Instance and Interceptor의 목적은 뭐야?
A. Frontend Agent가 Axios Instance, publicApi, authApi, interceptor, error mapping 기준을 이해하고 공통 API Client를 설계하게 만드는 것이다.

Q. Part03 다음에는 어떤 문서가 이어지면 좋아?
A. API Layer Separation, Request / Response Type Mapping, UI State, TanStack Query 순서로 이어지는 것이 좋다.
