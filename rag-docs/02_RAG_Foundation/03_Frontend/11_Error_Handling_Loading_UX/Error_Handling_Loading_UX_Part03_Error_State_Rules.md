# Error Handling & Loading UX Part03 - Error State Rules

---

# 1. Error State Overview

## 1.1 Error State Purpose

### [개념]

Error State는 API 요청, 사용자 액션, 화면 렌더링, 라우팅 처리 중 문제가 발생했을 때 사용자에게 실패 상태를 알려주는 UI 상태다.

Error State는 단순히 오류를 출력하는 것이 아니라 오류 종류를 분류하고 사용자에게 가능한 다음 행동을 제공하는 기준이다.

---

### [핵심]

Error State 주요 대상:

- API Error State
- Network Error
- Server Error
- Validation Error
- Authentication Error
- Authorization Error
- Not Found Error
- Conflict Error
- Timeout Error
- Unknown Error
- Render Error
- Route Error

핵심 규칙:

- Error State와 Empty State를 혼동하지 않는다.
- 사용자 메시지와 개발자 로그를 분리한다.
- 서버 내부 오류 원문을 그대로 노출하지 않는다.
- 오류 종류에 따라 UI 위치를 다르게 선택한다.
- 재시도 가능한 오류에는 Retry Action을 제공할 수 있다.
- 인증 오류와 권한 오류를 구분한다.
- API Error와 Render Error를 구분한다.
- Field Error와 Global Error를 구분한다.
- Error Boundary는 API 요청 실패를 처리하지 않는다.

---

### [실무]

2026 실무 기준에서 Error State는 아래 흐름으로 처리한다.

```text
Error 발생
→ Error Type 분류
→ User Message Mapping
→ UI 위치 선택
→ Retry / Redirect / Fallback 선택
→ Developer Log 분리
→ Security Exposure 검토
```

Error State 선택 기준:

| 오류 종류                  | UI 방식                             | 예                       |
| -------------------------- | ----------------------------------- | ------------------------ |
| Network Error              | Page Error / Inline Error + Retry   | 네트워크 연결 확인       |
| 400 / 422 Validation Error | Field Error / Form Alert            | 이메일 형식 오류         |
| 401 Unauthorized           | Login Redirect / Auth Message       | 로그인이 필요합니다      |
| 403 Forbidden              | Forbidden Page / Permission Message | 접근 권한 없음           |
| 404 API Not Found          | Resource Not Found UI               | 축제 정보를 찾을 수 없음 |
| 404 Route Not Found        | NotFoundPage                        | 페이지를 찾을 수 없음    |
| 409 Conflict               | Conflict Message + Refetch          | 이미 처리된 요청         |
| 500 Server Error           | Generic Error + Retry               | 서버 오류                |
| Render Error               | Error Boundary Fallback             | 화면 표시 중 오류        |

---

### [FAQ]

Q. Error State는 뭐야?
A. 요청 실패, 권한 문제, 렌더링 오류처럼 정상 화면을 보여줄 수 없을 때 사용자에게 실패 상태를 알려주는 UI 상태다.

Q. Error State와 Empty State 차이는?
A. Error State는 요청 실패이고 Empty State는 요청 성공 후 데이터가 없는 상태다.

Q. 에러가 나면 alert만 띄워도 돼?
A. 간단한 실습은 가능하지만 실무에서는 오류 위치, 종류, 재시도 가능 여부에 따라 Inline Error, Page Error, Toast, Fallback UI를 구분한다.

Q. 서버 오류 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 포함될 수 있으므로 사용자용 메시지로 변환해야 한다.

---

# 2. API Error State Rules

## 2.1 API Error State Basics

### [개념]

API Error State는 서버 요청이 실패했을 때 사용자에게 요청 실패 상태를 알려주는 UI다.

API Error State는 HTTP Status Code, Error Code, Response Body, Network 상태를 기준으로 사용자 메시지와 후속 액션을 결정한다.

---

### [핵심]

API Error State 처리 대상:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 500 Server Error
- Network Error
- Timeout
- Unknown Error

핵심 규칙:

- API 실패를 빈 배열이나 null 성공처럼 숨기지 않는다.
- HTTP Status Code 기준으로 사용자 메시지를 분리한다.
- 오류 응답 구조를 공통 mapping 함수로 처리한다.
- 화면별 상세 메시지는 override 가능하게 둔다.
- 재시도 가능한 오류에는 Retry Button을 제공한다.
- 서버 stack trace, SQL Error, token 값을 사용자에게 노출하지 않는다.
- Error UI는 실제 refetch 또는 retry 함수와 연결한다.

---

### [실무]

공통 Error State 예:

```tsx
function ErrorState({ message, onRetry }) {
  return (
    <section role="alert">
      <p>{message}</p>
      {onRetry && (
        <button type="button" onClick={onRetry}>
          다시 시도
        </button>
      )}
    </section>
  );
}
```

조회 실패 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, isError, error, refetch } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <FestivalListSkeleton />;
  }

  if (isError) {
    return <ErrorState message={getApiErrorMessage(error)} onRetry={refetch} />;
  }

  if (!data || data.length === 0) {
    return <EmptyState title="축제 정보가 없습니다." />;
  }

  return <FestivalList festivals={data} />;
}
```

권장:

- `isError` 상태를 명확히 렌더링한다.
- `error` 객체는 사용자 메시지로 변환한다.
- Retry Button은 `refetch` 또는 재요청 함수와 연결한다.
- 사용자에게 해결 가능한 액션을 제공한다.
- 개발 로그는 별도로 관리한다.

주의:

- Error State 없이 `console.log(error)`만 남기지 않는다.
- API 실패를 Empty State로 대체하지 않는다.
- Error Message Mapping 없이 서버 message를 그대로 노출하지 않는다.
- Retry Button만 있고 실제 재요청이 연결되지 않으면 안 된다.

---

### [FAQ]

Q. API 에러는 어떻게 보여줘?
A. 사용자가 이해할 수 있는 메시지와 필요한 경우 다시 시도 버튼을 제공한다.

Q. API 실패를 빈 배열로 처리해도 돼?
A. 권장하지 않는다. 실패 상태가 사라져 사용자가 오류를 알 수 없으므로 Error State로 분리해야 한다.

Q. Retry Button은 언제 제공해?
A. 네트워크 오류, 일시적 서버 오류, 조회 실패처럼 재시도 가능성이 있는 오류에 제공한다.

Q. ErrorState 컴포넌트는 공통으로 만들어도 돼?
A. 가능하다. message와 onRetry를 props로 받으면 여러 화면에서 재사용할 수 있다.

---

## 2.2 Error Message Mapping

### [개념]

Error Message Mapping은 API Error 객체, HTTP Status Code, 서버 Error Code를 사용자에게 보여줄 메시지로 변환하는 작업이다.

Error Message Mapping은 화면마다 오류 해석이 달라지는 문제를 줄이고 사용자 메시지 기준을 통일한다.

---

### [핵심]

Mapping 대상:

- HTTP Status Code
- Backend Error Code
- Server Message
- Validation Errors
- Network Error
- Timeout
- Unknown Error
- Field Errors
- Global Error

핵심 규칙:

- 공통 Error Message Mapping 함수를 둔다.
- 서버 message를 항상 그대로 사용하지 않는다.
- 내부 정보가 포함될 수 있는 message는 사용자용 메시지로 변환한다.
- 화면별 문맥 메시지는 override 가능하게 둔다.
- unknown error fallback을 제공한다.
- Validation Error는 Field Error와 Global Error로 분리한다.

---

### [실무]

기본 Mapping 예:

```typescript
export function getApiErrorMessage(error: unknown): string {
  if (axios.isAxiosError(error)) {
    const status = error.response?.status;

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
      return "이미 처리되었거나 현재 상태와 충돌한 요청입니다.";
    }

    if (status === 422) {
      return "입력 값을 다시 확인해 주세요.";
    }

    if (status >= 500) {
      return "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.";
    }
  }

  return "요청 처리 중 문제가 발생했습니다.";
}
```

화면별 override 예:

```typescript
function getFestivalDetailErrorMessage(error: unknown): string {
  if (isNotFoundError(error)) {
    return "축제 정보를 찾을 수 없습니다.";
  }

  return getApiErrorMessage(error);
}
```

권장:

- `getApiErrorMessage` 같은 공통 함수를 둔다.
- 화면별 도메인 메시지는 별도 함수로 감싼다.
- 서버 Error Code가 있다면 Status Code보다 구체적으로 처리할 수 있다.
- 사용자가 수정할 수 있는 메시지와 시스템 오류 메시지를 구분한다.
- 개발 로그에는 원본 error를 남기되 사용자 UI에는 안전한 메시지만 보여준다.

주의:

- `error.message`를 무조건 사용자에게 보여주지 않는다.
- Backend stack trace, SQL Error, 서버 경로를 노출하지 않는다.
- token, password, personal data를 오류 메시지에 포함하지 않는다.
- 모든 오류를 같은 메시지로 처리하면 사용자가 다음 행동을 알기 어렵다.

---

### [FAQ]

Q. 에러 메시지 mapping 함수는 왜 필요해?
A. API 에러 구조를 화면마다 직접 해석하면 중복이 생기고 메시지 기준이 달라질 수 있기 때문이다.

Q. 서버 message를 항상 사용해도 돼?
A. 아니다. 내부 정보가 포함될 수 있으면 사용자용 메시지로 변환해야 한다.

Q. unknown error에는 어떤 메시지를 보여줘?
A. “요청 처리 중 문제가 발생했습니다.” 같은 안전한 fallback 메시지를 제공한다.

Q. 화면별로 다른 에러 메시지를 쓰고 싶으면?
A. 공통 mapping 함수를 기본으로 사용하고 화면별 override 함수를 추가하면 된다.

---

# 3. Network Error Rules

## 3.1 Network Error Basics

### [개념]

Network Error는 서버가 정상적인 HTTP 응답을 주지 못했거나 브라우저가 요청을 완료하지 못한 상태다.

Network Error는 HTTP 400 / 500 응답과 다르며, 응답 객체가 없거나 브라우저 보안 정책에 의해 요청이 차단될 때 발생할 수 있다.

---

### [핵심]

Network Error 원인:

- Internet Disconnected
- Server Down
- DNS Problem
- CORS Failure
- Timeout
- Request Blocked
- Mixed Content
- Wrong BaseURL
- SSL / HTTPS 문제
- Browser Security Policy

핵심 규칙:

- Network Error와 Server Error를 구분한다.
- 사용자가 해결 가능한 메시지를 제공한다.
- Retry Button을 제공할 수 있다.
- CORS Error는 브라우저에서 Network Error처럼 보일 수 있다.
- Postman 성공과 Browser 성공은 다를 수 있다.
- Network 탭에서 status code 존재 여부를 확인한다.
- baseURL, 서버 실행 여부, CORS 설정을 확인한다.

---

### [실무]

UX 기준:

```text
Network Error
→ "네트워크 연결을 확인해 주세요."
→ Retry Button
→ 필요 시 서버 연결 상태 안내
```

Axios 판정 예:

```typescript
function isNetworkError(error: unknown): boolean {
  return axios.isAxiosError(error) && !error.response;
}
```

Network Error 메시지 예:

```typescript
function getNetworkErrorMessage(error: unknown): string {
  if (isNetworkError(error)) {
    return "네트워크 연결을 확인해 주세요.";
  }

  return getApiErrorMessage(error);
}
```

Debug Flow:

```text
Network Error 발생
→ Browser Network 탭 확인
→ 요청 URL 확인
→ status code 존재 여부 확인
→ CORS 메시지 확인
→ baseURL 확인
→ 서버 실행 여부 확인
→ HTTPS / Mixed Content 확인
```

권장:

- `error.response`가 없으면 Network Error 가능성을 확인한다.
- Retry Button을 제공한다.
- 사용자가 해결할 수 있는 메시지와 개발자가 확인할 정보를 분리한다.
- CORS 문제는 서버 설정과 브라우저 콘솔을 함께 확인한다.

주의:

- Network Error를 500 Server Error처럼 처리하지 않는다.
- CORS Error는 Postman에서 재현되지 않을 수 있다.
- 잘못된 baseURL은 사용자 문제가 아니라 설정 문제다.
- 네트워크 문제를 Empty State로 보여주지 않는다.

---

### [FAQ]

Q. Network Error와 500 에러는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

Q. Postman에서는 되는데 브라우저에서는 Network Error가 나?
A. CORS, Mixed Content, 브라우저 보안 정책 문제일 수 있다.

Q. Network Error에는 어떤 메시지를 보여줘?
A. 네트워크 연결을 확인해 달라는 메시지와 다시 시도 버튼을 제공하는 것이 좋다.

Q. CORS Error도 Network Error야?
A. 브라우저에서는 응답 접근이 차단되어 Network Error처럼 보일 수 있다.

---

## 3.2 Timeout Error Rules

### [개념]

Timeout Error는 요청이 정해진 시간 안에 완료되지 않아 실패한 상태다.

Timeout Error는 서버 응답 지연, 네트워크 지연, 외부 API 지연, 잘못된 요청 처리로 발생할 수 있다.

---

### [핵심]

Timeout Error 원인:

- Server Response Delay
- External API Delay
- Network Latency
- Long Query
- Backend Deadlock
- Gateway Timeout
- Client Timeout Limit
- Infinite Pending Request

핵심 규칙:

- Timeout Error는 무한 Loading으로 방치하지 않는다.
- 사용자에게 잠시 후 다시 시도하라는 메시지를 제공한다.
- Retry Action을 제공할 수 있다.
- 요청이 실제로 서버에서 처리되었을 가능성을 고려한다.
- 결제, 삭제, 저장 같은 중요한 요청은 처리 여부 확인이 필요할 수 있다.
- 개발자는 request duration과 endpoint를 로그로 확인한다.

---

### [실무]

UX 기준:

```text
Timeout Error
→ "요청 시간이 초과되었습니다. 잠시 후 다시 시도해 주세요."
→ Retry Button
→ 중요한 요청은 처리 여부 확인 안내
```

Axios timeout 예:

```typescript
const api = axios.create({
  baseURL: "/api",
  timeout: 10000,
});
```

Timeout Mapping 예:

```typescript
function isTimeoutError(error: unknown): boolean {
  return axios.isAxiosError(error) && error.code === "ECONNABORTED";
}
```

주의 요청 예:

```text
결제 요청 Timeout
→ 결제 성공 여부 불확실
→ 결제 내역 조회 또는 서버 상태 확인 필요
→ 단순 재결제 유도 금지
```

권장:

- 일반 조회 Timeout은 Retry Button을 제공한다.
- 중요한 Mutation Timeout은 처리 여부 확인 UX를 제공한다.
- Timeout 후 버튼을 다시 활성화한다.
- Loading 상태를 반드시 종료한다.

주의:

- Timeout을 무한 Loading으로 방치하지 않는다.
- 결제 / 후원 / 삭제 요청은 단순 재시도만 안내하면 중복 처리 위험이 있다.
- Timeout은 Frontend만의 문제가 아닐 수 있다.

---

### [FAQ]

Q. Timeout Error는 뭐야?
A. 요청이 정해진 시간 안에 완료되지 않아 실패한 상태다.

Q. Timeout이 나면 무조건 다시 시도하면 돼?
A. 조회 요청은 재시도가 가능하지만 결제, 삭제, 저장 같은 중요한 요청은 처리 여부 확인이 먼저 필요할 수 있다.

Q. Timeout 후 Loading은 어떻게 해야 해?
A. Loading을 종료하고 Error State 또는 Retry UI를 보여줘야 한다.

Q. Timeout 메시지는 어떻게 쓰면 좋아?
A. “요청 시간이 초과되었습니다. 잠시 후 다시 시도해 주세요.”처럼 사용자에게 다음 행동을 안내하는 문구가 좋다.

---

# 4. HTTP Status Error UX Rules

## 4.1 400 Bad Request UX

### [개념]

400 Bad Request는 요청 형식, 파라미터, 요청 Body가 잘못되었을 때 발생하는 오류다.

Frontend는 400 Error를 사용자가 수정 가능한 입력 오류인지, 개발자가 수정해야 하는 요청 구조 오류인지 구분해야 한다.

---

### [핵심]

400 Error 원인:

- Required Parameter Missing
- Invalid Request Body
- Invalid Query Parameter
- Invalid Date Format
- Invalid Type
- Request Shape Mismatch
- Client Validation 누락
- API Contract 불일치

핵심 규칙:

- 사용자가 수정 가능한 값이면 Field Error 또는 Form Alert로 표시한다.
- 요청 구조 문제이면 개발 로그로 확인한다.
- 사용자에게 내부 API 구조를 노출하지 않는다.
- 입력값은 유지한다.
- Submit Loading을 해제한다.
- 요청 Body와 API 문서 일치 여부를 확인한다.

---

### [실무]

UX 메시지 예:

```text
요청 값을 확인해 주세요.
```

Form 처리 예:

```tsx
if (status === 400) {
  setGlobalError("입력 값을 다시 확인해 주세요.");
}
```

개발 확인 Flow:

```text
400 발생
→ Network Request Payload 확인
→ Query Parameter 확인
→ Backend DTO 필드명 확인
→ Content-Type 확인
→ Validation Response 확인
→ Field Error Mapping 확인
```

권장:

- 사용자가 수정할 수 있는 오류는 구체적으로 안내한다.
- API 요청 구조 오류는 개발자가 확인할 로그로 분리한다.
- 서버 Validation Response가 있으면 Field Error로 연결한다.
- Form 입력값을 지우지 않는다.

주의:

- 400 Error를 무조건 “서버 오류”로 보여주지 않는다.
- Backend DTO와 Frontend request field명이 다르면 400이 발생할 수 있다.
- 날짜 형식, enum 값, 숫자 타입 오류를 확인한다.

---

### [FAQ]

Q. 400 Bad Request는 언제 발생해?
A. 요청 형식, 파라미터, 요청 Body가 잘못되었을 때 발생한다.

Q. 400 Error는 사용자 잘못이야?
A. 항상 그렇지 않다. Frontend 요청 구조나 API Contract 불일치 문제일 수 있다.

Q. 400 Error 메시지는 어떻게 보여줘?
A. 사용자가 수정 가능한 경우 “입력 값을 확인해 주세요.”처럼 안내하고, 필드 오류가 있으면 input 근처에 표시한다.

Q. 400 발생 시 입력값을 지워야 해?
A. 보통 지우지 않는다. 사용자가 수정할 수 있도록 유지하는 것이 좋다.

---

## 4.2 401 Unauthorized UX

### [개념]

401 Unauthorized는 사용자가 인증되지 않았거나 Access Token이 유효하지 않을 때 발생하는 오류다.

401 Error는 로그인 필요, Access Token 만료, Refresh Token 실패, Authorization Header 누락과 연결된다.

---

### [핵심]

401 Error 원인:

- Not Logged In
- Access Token Missing
- Access Token Expired
- Invalid Token
- Authorization Header Missing
- Refresh Token Expired
- Refresh Failed
- Login Failed

핵심 규칙:

- 401과 403을 구분한다.
- Refresh Token Flow가 있으면 먼저 재발급을 시도할 수 있다.
- Refresh 성공 시 원래 요청을 재시도할 수 있다.
- Refresh 실패 시 Auth State를 정리하고 Login Redirect를 수행한다.
- 로그인 실패 401과 세션 만료 401 UX를 구분한다.
- 무조건 alert 반복을 피한다.
- Redirect Loop를 방지한다.

---

### [실무]

401 처리 Flow:

```text
401 발생
→ Refresh Token 존재 여부 확인
→ Refresh 가능하면 Access Token 재발급
→ 재발급 성공
  → 원래 요청 재시도
→ 재발급 실패
  → Auth State Clear
  → Login Redirect
  → "로그인이 필요합니다." 메시지
```

UX 메시지 예:

```text
로그인이 필요합니다.
```

Interceptor 기준 예:

```typescript
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // refresh or redirect logic
    }

    return Promise.reject(error);
  },
);
```

권장:

- Protected Route와 연동한다.
- 세션 만료 메시지를 한 번만 보여준다.
- 원래 접근 위치를 저장해 로그인 후 복귀할 수 있다.
- Refresh 실패 시 local auth state를 정리한다.
- 로그인 실패는 Form Global Error로 처리한다.

주의:

- 401에서 무조건 로그아웃하면 refresh flow가 동작하지 않는다.
- interceptor에서 `Promise.reject(error)`를 누락하면 호출부가 오류를 받지 못한다.
- 401 alert가 요청마다 반복되면 UX가 나빠진다.
- 401과 403을 같은 메시지로 처리하지 않는다.

---

### [FAQ]

Q. 401 Unauthorized는 뭐야?
A. 인증되지 않았거나 Access Token이 유효하지 않을 때 발생하는 오류다.

Q. 401이면 무조건 로그인 페이지로 보내?
A. Refresh Token Flow가 있으면 먼저 재발급을 시도하고 실패 시 로그인 페이지로 이동한다.

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 가능하다. 로그인 실패 401과 기존 인증 만료 401의 UX를 구분해야 한다.

Q. 401과 403 메시지를 같게 해도 돼?
A. 권장하지 않는다. 401은 로그인 필요, 403은 권한 없음으로 구분하는 것이 좋다.

---

## 4.3 403 Forbidden UX

### [개념]

403 Forbidden은 사용자가 인증은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생하는 오류다.

403 Error는 로그인 필요가 아니라 권한 부족 상태다.

---

### [핵심]

403 Error 원인:

- Role Insufficient
- Not Owner
- Admin Only
- Resource Forbidden
- Backend Authorization Failed
- Plan / Subscription 제한
- Feature Permission Denied

핵심 규칙:

- 403에서 기본적으로 logout하지 않는다.
- Login Redirect와 구분한다.
- 권한 없음 메시지를 제공한다.
- Forbidden Page 또는 Inline Permission Message를 사용한다.
- 내부 권한 정책을 과도하게 노출하지 않는다.
- 이전 페이지 이동 또는 메인 이동 액션을 제공할 수 있다.
- Auth State는 유지한다.

---

### [실무]

Forbidden Page 예:

```jsx
function ForbiddenPage() {
  return (
    <main>
      <h1>접근 권한이 없습니다.</h1>
      <p>현재 계정으로는 이 페이지를 이용할 수 없습니다.</p>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

403 처리 기준:

```text
403 발생
→ Auth State 유지
→ 권한 없음 메시지 표시
→ Forbidden Page 이동 가능
→ 이전 페이지 / 메인 이동 제공
```

권장:

- 관리자 전용 페이지 접근 시 Forbidden Page를 보여준다.
- 소유자만 수정 가능한 리소스는 버튼 숨김 또는 권한 없음 메시지를 제공한다.
- API 403 발생 시 사용자에게 권한 부족을 안내한다.
- 상세한 role 정책은 노출하지 않는다.

주의:

- 403에서 로그아웃하지 않는다.
- 403을 401처럼 Login Redirect로 처리하지 않는다.
- “관리자 권한 ROLE_ADMIN이 필요합니다”처럼 내부 role 정책을 그대로 노출하지 않는다.
- 권한 없는 액션 버튼은 사전에 숨기거나 disabled 처리할 수 있다.

---

### [FAQ]

Q. 403 Forbidden은 뭐야?
A. 로그인은 되었지만 해당 리소스나 기능에 접근할 권한이 없는 상태다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 되어 있지만 권한이 부족한 상태이므로 권한 없음 UI를 보여주는 것이 일반적이다.

Q. 403이면 로그인 페이지로 보내야 해?
A. 보통은 권한 없음 페이지나 메시지를 보여주는 것이 더 적절하다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증 필요이고 403은 인증은 되었지만 권한이 없는 상태다.

---

## 4.4 404 Not Found UX

### [개념]

404 Not Found는 요청한 페이지, API Endpoint, 또는 리소스를 찾을 수 없을 때 발생하는 오류다.

Frontend에서는 Route 404와 API Resource 404를 구분해야 한다.

---

### [핵심]

404 Error 구분:

- Route 404
- API Endpoint 404
- Resource Not Found
- Invalid ID
- Deleted Resource
- Wrong Endpoint
- SPA Fallback Problem

핵심 규칙:

- Route 404와 API 404를 구분한다.
- 상세 리소스 없음은 Resource Not Found UI로 처리한다.
- 잘못된 URL은 NotFoundPage로 처리한다.
- API endpoint 오류는 개발자가 URL을 확인한다.
- 메인 이동 또는 목록 이동 액션을 제공한다.
- Network 탭에서 실제 요청 URL을 확인한다.

---

### [실무]

API 404 UX:

```text
GET /festivals/999
→ Resource Not Found
→ "축제 정보를 찾을 수 없습니다."
→ 목록으로 이동 버튼 제공
```

Route 404 UX:

```jsx
function NotFoundPage() {
  return (
    <main>
      <h1>페이지를 찾을 수 없습니다.</h1>
      <p>주소가 잘못되었거나 페이지가 이동되었을 수 있습니다.</p>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

API Resource Not Found 예:

```tsx
function FestivalNotFound() {
  return (
    <section>
      <h2>축제 정보를 찾을 수 없습니다.</h2>
      <Link to="/festivals">축제 목록으로 이동</Link>
    </section>
  );
}
```

권장:

- React Router catch-all route를 구성한다.
- 상세 리소스 404는 해당 상세 화면 안에서 처리할 수 있다.
- API endpoint 404는 baseURL과 path를 확인한다.
- SPA fallback 설정 문제와 API 404를 구분한다.

주의:

- API 404를 무조건 전체 NotFoundPage로 보내지 않는다.
- Route 404와 Resource Not Found의 UX가 다를 수 있다.
- 잘못된 endpoint는 사용자 문제가 아니라 개발 문제다.
- 삭제된 리소스는 친절한 안내가 필요하다.

---

### [FAQ]

Q. 페이지 404와 API 404는 달라?
A. 다르다. 페이지 404는 Route 매칭 실패이고 API 404는 서버 리소스나 endpoint를 찾지 못한 것이다.

Q. 상세 페이지 데이터가 없으면 어떻게 보여줘?
A. 해당 리소스를 찾을 수 없다는 메시지와 목록으로 돌아가는 버튼을 제공하는 것이 좋다.

Q. API 404도 NotFoundPage로 보내?
A. 상황에 따라 다르다. 상세 리소스 없음은 해당 페이지 안에서 Resource Not Found UI를 보여줄 수 있다.

Q. API endpoint 404는 어떻게 확인해?
A. Network 탭에서 요청 URL, baseURL, Backend Controller path를 확인한다.

---

## 4.5 409 Conflict UX

### [개념]

409 Conflict는 요청이 현재 서버 상태와 충돌할 때 발생하는 오류다.

409 Error는 중복 요청, 이미 처리된 요청, 상태 불일치, 버전 충돌에서 사용할 수 있다.

---

### [핵심]

409 Error 사용 상황:

- Duplicate Favorite
- Duplicate Like
- Duplicate Signup Value
- Already Processed Request
- Version Conflict
- Reservation Conflict
- Payment Conflict
- Optimistic UI Conflict

핵심 규칙:

- 사용자에게 책임을 돌리는 문구를 피한다.
- 현재 서버 상태와 UI 상태를 다시 동기화한다.
- 중복 클릭 방지와 함께 처리한다.
- 최신 상태 refetch를 고려한다.
- 이미 처리된 요청이면 현재 상태를 반영한다.
- 결제 / 예약 충돌은 별도 정책이 필요하다.

---

### [실무]

UX 기준:

```text
409 Conflict
→ "이미 처리된 요청입니다."
→ 현재 상태 refetch
→ 버튼 상태 갱신
```

찜 중복 예:

```text
찜 추가 요청
→ 이미 찜한 축제
→ 409
→ 찜 상태를 true로 갱신하거나 상세 정보 refetch
```

Mutation 처리 예:

```tsx
const favoriteMutation = useMutation({
  mutationFn: toggleFavorite,
  onError: (error) => {
    if (isConflictError(error)) {
      queryClient.invalidateQueries({
        queryKey: ["festival-detail", festivalId],
      });
      toast.info("최신 상태를 확인했습니다.");
      return;
    }

    toast.error(getApiErrorMessage(error));
  },
});
```

권장:

- 409 발생 시 서버 최신 상태를 다시 조회한다.
- 중복 처리된 요청이면 UI 상태를 서버 상태에 맞춘다.
- 좋아요 / 찜 버튼은 pending 중 disabled 처리한다.
- 사용자에게 “잘못 눌렀다”는 식의 문구를 피한다.

주의:

- 409를 500처럼 처리하지 않는다.
- 중복 요청 방지를 Frontend에만 의존하지 않는다.
- Optimistic UI 사용 시 rollback 또는 refetch 기준이 필요하다.
- 결제 중 409는 도메인 정책에 따라 신중하게 처리한다.

---

### [FAQ]

Q. 409 Conflict는 언제 발생해?
A. 이미 처리된 요청이거나 서버의 현재 상태와 요청이 충돌할 때 발생한다.

Q. 409가 나면 어떻게 해?
A. 사용자에게 상태 충돌을 안내하고 최신 서버 상태를 다시 조회하는 것이 좋다.

Q. 좋아요 중복 요청에서 409가 나면?
A. 좋아요 상태를 서버 최신 상태와 동기화하거나 refetch하는 것이 좋다.

Q. 409는 사용자 실수라고 말해도 돼?
A. 권장하지 않는다. 이미 처리되었거나 상태가 변경되었다는 중립적인 메시지가 좋다.

---

## 4.6 422 Validation Error UX

### [개념]

422 Unprocessable Entity는 요청 형식은 이해했지만 의미상 검증에 실패했을 때 사용하는 오류다.

422 Error는 Form Field Error와 Global Form Error로 연결되는 경우가 많다.

---

### [핵심]

422 Error 원인:

- Required Missing
- Invalid Format
- Length Violation
- Duplicate Email
- Duplicate Nickname
- Invalid Rating
- Invalid Date Range
- Business Validation Failed
- Field Validation Failed

핵심 규칙:

- Field Error는 input 근처에 표시한다.
- Global Error는 Form 상단 또는 Submit Button 근처에 표시한다.
- 입력값은 유지한다.
- Submit Loading을 해제한다.
- 첫 번째 오류 field로 focus 이동을 고려한다.
- 서버 field error key와 Frontend field name을 매핑한다.

---

### [실무]

Validation Response 예:

```json
{
  "success": false,
  "message": "검증 실패",
  "errors": {
    "email": "이미 사용 중인 이메일입니다.",
    "password": "비밀번호는 8자 이상이어야 합니다."
  }
}
```

Field Error 표시 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  value={values.email}
  onChange={handleChange}
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
{errors.email && (
  <p id="email-error" role="alert">
    {errors.email}
  </p>
)}
```

Global Error 예:

```jsx
function FormAlert({ message }) {
  if (!message) {
    return null;
  }

  return <div role="alert">{message}</div>;
}
```

권장:

- 서버 validation errors를 Form State로 매핑한다.
- 사용자 수정이 필요한 필드 근처에 오류를 보여준다.
- Form 전체 오류는 Form Alert로 분리한다.
- 오류가 있어도 사용자가 입력한 값은 유지한다.
- 접근성을 위해 `aria-invalid`, `aria-describedby`를 사용한다.

주의:

- Field Error를 Toast로만 보여주지 않는다.
- 모든 Validation Error를 Global Error로만 처리하지 않는다.
- 서버 field명과 Frontend input name이 다르면 매핑 오류가 생긴다.
- Validation 실패 후 Form을 reset하지 않는다.

---

### [FAQ]

Q. 422 Validation Error는 뭐야?
A. 요청 형식은 이해했지만 입력값이나 비즈니스 규칙 검증에 실패한 상태다.

Q. Validation Error는 alert로만 보여줘도 돼?
A. 권장하지 않는다. 필드별 오류는 해당 input 근처에 보여주는 것이 사용자가 수정하기 쉽다.

Q. 서버 검증 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. Field Error와 Global Error는 어떻게 나눠?
A. 특정 input 값 문제는 Field Error, Form 전체 문제나 인증 실패는 Global Error로 처리한다.

---

## 4.7 500 Server Error UX

### [개념]

500 Server Error는 서버 내부 오류로 요청 처리가 실패한 상태다.

Frontend는 500 Error 발생 시 내부 상세 정보를 노출하지 않고 일반적인 오류 메시지와 재시도 옵션을 제공한다.

---

### [핵심]

500 Error 원인:

- Backend Exception
- Database Error
- Null Pointer Error
- External API Failure
- Server Configuration Error
- Unexpected Runtime Error
- Internal Logic Error

핵심 규칙:

- 서버 stack trace를 사용자에게 노출하지 않는다.
- 일반적인 서버 오류 메시지를 제공한다.
- 재시도 버튼을 제공할 수 있다.
- 개발 환경에서는 console log로 확인할 수 있다.
- 운영 환경에서는 monitoring 또는 error reporting을 고려한다.
- Frontend 요청 body나 endpoint 오류가 서버 오류를 유발했는지도 확인한다.

---

### [실무]

UX 문구 예:

```text
서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.
```

Error State 예:

```tsx
<ErrorState
  message="서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요."
  onRetry={refetch}
/>
```

Debug Flow:

```text
500 발생
→ Network Response 확인
→ Request Payload 확인
→ Endpoint 확인
→ Backend Log 확인
→ External API 상태 확인
→ 재시도 가능 여부 판단
```

권장:

- 사용자에게 안전한 generic message를 제공한다.
- 조회 요청은 Retry Button을 제공한다.
- 반복 장애는 문의 안내를 제공할 수 있다.
- 요청 body 오류로 500이 발생하는지 확인한다.
- 운영 환경에서는 Sentry / Logging 시스템 연동을 고려한다.

주의:

- stack trace, SQL Error, 서버 경로를 노출하지 않는다.
- 500을 Validation Error처럼 field에 표시하지 않는다.
- 500이 반복되면 사용자가 해결할 수 없는 문제임을 안내한다.
- 중요한 mutation의 500은 처리 여부 확인이 필요할 수 있다.

---

### [FAQ]

Q. 500 Server Error는 뭐야?
A. 서버 내부 오류로 요청 처리가 실패한 상태다.

Q. 500 에러 상세 내용을 사용자에게 보여줘도 돼?
A. 권장하지 않는다. 내부 구현 정보가 노출될 수 있으므로 일반적인 오류 메시지를 보여준다.

Q. 500이 나면 Frontend에서 해결할 수 있어?
A. 대부분 Backend 문제이지만 Frontend 요청 body나 endpoint가 잘못되어 서버 오류를 유발했는지도 확인해야 한다.

Q. 500 Error에는 Retry Button을 제공해도 돼?
A. 조회 요청이나 일시적 서버 오류에는 제공할 수 있다.

---

# 5. Form Error UX Rules

## 5.1 Field Error Rules

### [개념]

Field Error는 특정 input 값에 연결되는 오류 메시지다.

Field Error는 사용자가 어느 값을 수정해야 하는지 바로 알 수 있도록 해당 input 근처에 표시한다.

---

### [핵심]

Field Error 사용 상황:

- Required Error
- Email Format Error
- Password Length Error
- Confirm Password Mismatch
- Rating Range Error
- Duplicate Nickname
- Server Validation Field Error
- Invalid Date Range

핵심 규칙:

- input 근처에 표시한다.
- `aria-invalid`를 적용한다.
- `aria-describedby`로 오류 메시지와 input을 연결한다.
- 오류 문구는 수정 행동을 안내한다.
- 서버 field error와 client field error를 통합한다.
- submit 후 또는 touched 이후 표시 기준을 정한다.
- Field Error를 Toast로만 보여주지 않는다.

---

### [실무]

Field Error 예:

```jsx
<label htmlFor="nickname">닉네임</label>
<input
  id="nickname"
  name="nickname"
  value={values.nickname}
  onChange={handleChange}
  aria-invalid={Boolean(errors.nickname)}
  aria-describedby={errors.nickname ? "nickname-error" : undefined}
/>
{errors.nickname && (
  <p id="nickname-error" role="alert">
    {errors.nickname}
  </p>
)}
```

권장 문구:

```text
나쁨: 오류입니다.
좋음: 닉네임은 2자 이상 입력해 주세요.
```

권장:

- 사용자가 어떻게 수정해야 하는지 알려준다.
- 오류가 있는 필드를 시각적으로 구분한다.
- 색상만으로 오류를 표시하지 않는다.
- 첫 오류 field로 focus 이동을 고려한다.
- 서버 field error key를 Frontend field name에 맞게 변환한다.

주의:

- 모든 field error를 Form 상단에만 몰아넣지 않는다.
- Toast로만 field error를 보여주면 사용자가 수정 위치를 찾기 어렵다.
- 오류 메시지 id 중복을 피한다.
- 클라이언트 검증과 서버 검증 메시지가 충돌하지 않게 한다.

---

### [FAQ]

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Field Error를 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 사용자가 어떤 필드를 수정해야 하는지 알기 어렵다.

Q. Field Error 문구는 어떻게 쓰면 좋아?
A. 사용자가 어떤 값을 어떻게 수정해야 하는지 알 수 있게 구체적으로 작성한다.

Q. Field Error 접근성은 어떻게 처리해?
A. aria-invalid와 aria-describedby를 사용해 input과 오류 메시지를 연결하는 것이 좋다.

---

## 5.2 Global Form Error Rules

### [개념]

Global Form Error는 Form 전체에 해당하는 오류 메시지다.

Global Form Error는 로그인 실패, 권한 문제, 서버 오류, 제출 실패처럼 특정 field 하나로 귀속하기 어려운 오류에 사용한다.

---

### [핵심]

Global Form Error 사용 상황:

- Login Failed
- Signup Failed
- Permission Denied
- Server Unavailable
- Submit Failed
- Duplicate Request
- Unknown Error
- Business Rule Error

핵심 규칙:

- Form 상단 또는 Submit Button 근처에 표시한다.
- Field Error와 구분한다.
- 사용자가 다음 행동을 알 수 있게 한다.
- 서버 내부 메시지를 그대로 노출하지 않는다.
- Submit Loading을 해제한다.
- 재시도 가능성을 표시할 수 있다.
- Form 입력값은 유지한다.

---

### [실무]

Form Alert 예:

```jsx
function FormAlert({ message }) {
  if (!message) {
    return null;
  }

  return <div role="alert">{message}</div>;
}
```

로그인 실패 예:

```tsx
function LoginForm() {
  const [formError, setFormError] = useState("");

  async function handleLogin(values) {
    try {
      await login(values);
    } catch (error) {
      setFormError("이메일 또는 비밀번호를 확인해 주세요.");
    }
  }

  return (
    <form onSubmit={handleSubmit(handleLogin)}>
      <FormAlert message={formError} />
      <LoginFields />
      <button type="submit">로그인</button>
    </form>
  );
}
```

권장:

- 로그인 실패는 보통 Global Form Error로 처리한다.
- 서버 장애는 Form 상단에 안내한다.
- 사용자가 다시 시도할 수 있도록 버튼 상태를 복구한다.
- Form 전체 오류와 Field Error를 함께 표시할 수 있다.

주의:

- 로그인 실패를 password field error로만 표시하면 보안상 정보 추론 문제가 생길 수 있다.
- Global Error를 alert로만 띄우고 화면에 남기지 않으면 사용자가 놓칠 수 있다.
- Submit Loading이 계속 유지되지 않도록 한다.

---

### [FAQ]

Q. Global Form Error는 뭐야?
A. Form 전체에 해당하며 특정 field 하나로 귀속하기 어려운 오류 메시지다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 이메일 형식 오류는 Field Error이고 계정 정보 불일치 같은 인증 실패는 Global Error로 처리하는 경우가 많다.

Q. Global Error는 어디에 보여줘?
A. Form 상단이나 제출 버튼 근처처럼 사용자가 쉽게 인식할 수 있는 위치에 보여준다.

Q. Global Error가 있어도 입력값은 유지해야 해?
A. 보통 유지한다. 사용자가 수정하거나 다시 제출할 수 있어야 한다.

---

# 6. Toast / Alert / Inline Error Rules

## 6.1 Error UI Position Selection

### [개념]

Error UI Position Selection은 오류 종류에 따라 Toast, Alert, Inline Error, Page Error, Modal, Fallback UI 중 적절한 표시 위치를 선택하는 기준이다.

오류는 발생 위치와 사용자가 취해야 할 행동에 따라 UI 위치가 달라져야 한다.

---

### [핵심]

오류 UI 방식:

- Toast
- Alert Box
- Inline Error
- Form Alert
- Page Error
- Modal
- Error Boundary Fallback
- NotFoundPage
- ForbiddenPage

핵심 규칙:

- Field 문제는 Inline Error로 표시한다.
- Form 전체 문제는 Form Alert로 표시한다.
- 짧은 실패 알림은 Toast로 표시할 수 있다.
- 페이지 전체 조회 실패는 Page Error로 표시한다.
- 권한 없음은 Forbidden Page 또는 Permission Message로 표시한다.
- 리소스 없음은 Resource Not Found UI로 표시한다.
- Render Error는 Error Boundary Fallback으로 표시한다.
- 모든 오류를 Toast로만 처리하지 않는다.

---

### [실무]

선택 기준:

```text
Field 문제
→ Inline Error

Form 전체 문제
→ Form Alert

짧은 액션 실패
→ Toast

목록 / 상세 조회 실패
→ Page Error + Retry

권한 없음
→ Forbidden Page / Permission Message

리소스 없음
→ Resource Not Found UI

렌더링 오류
→ Error Boundary Fallback
```

비교:

| 방식         | 사용 상황               | 예                      |
| ------------ | ----------------------- | ----------------------- |
| Toast        | 짧은 성공/실패 알림     | 좋아요 실패             |
| Alert Box    | 화면 내 중요한 안내     | 권한 없음               |
| Inline Error | 특정 field 오류         | 이메일 형식 오류        |
| Form Alert   | Form 전체 오류          | 로그인 실패             |
| Page Error   | 페이지 데이터 조회 실패 | 축제 목록 불러오기 실패 |
| Modal        | 중요한 확인 / 차단      | 삭제 확인               |
| Fallback UI  | 렌더링 오류             | 화면 표시 실패          |

권장:

- 오류 위치는 사용자가 수정해야 하는 위치와 가깝게 둔다.
- Toast는 일시적 정보에 사용한다.
- 중요한 오류는 화면에 남는 UI를 사용한다.
- 사용자 액션이 필요한 오류에는 버튼이나 링크를 제공한다.

주의:

- Field Error를 Toast로만 보여주지 않는다.
- Page Error를 Toast만 띄우고 빈 화면으로 두지 않는다.
- Modal을 오류 안내에 남발하지 않는다.
- Toast에 중요한 정보를 오래 의존하지 않는다.

---

### [FAQ]

Q. 모든 API 에러를 Toast로 처리하면 돼?
A. 아니다. Form field error, page error, permission error처럼 위치가 중요한 오류는 적절한 UI 위치에 표시해야 한다.

Q. Field Error는 왜 Inline으로 보여줘야 해?
A. 사용자가 어떤 필드를 수정해야 하는지 바로 알 수 있기 때문이다.

Q. Page Error는 언제 써?
A. 페이지나 주요 콘텐츠 데이터를 불러오지 못해 정상 화면을 보여줄 수 없을 때 사용한다.

Q. Toast는 언제 쓰는 게 좋아?
A. 저장 실패, 좋아요 실패처럼 짧게 알려도 되는 액션 결과에 적합하다.

---

# 7. Error Boundary Rules

## 7.1 Error Boundary Basics

### [개념]

Error Boundary는 React 렌더링 중 발생한 JavaScript 오류로 인해 전체 앱이 깨지는 것을 막고 Fallback UI를 보여주는 구조다.

Error Boundary는 API 요청 실패 상태와 역할이 다르다.

---

### [핵심]

Error Boundary 처리 대상:

- Render Error
- Lifecycle Error
- Child Component Crash
- Unexpected UI Error
- Component Tree Crash
- Fallback UI
- Error Logging

Error Boundary가 처리하지 못하는 대상:

- Event Handler Error
- Async API Error
- Server Response Error
- Promise Rejection Without Handling
- Validation Error
- Route 404
- Network Error

핵심 규칙:

- Component 렌더링 오류는 Error Boundary로 처리한다.
- API 요청 실패는 Error State로 직접 처리한다.
- Form 검증 실패는 Field Error 또는 Global Error로 처리한다.
- Route 없음은 NotFoundPage로 처리한다.
- 사용자에게 stack trace를 노출하지 않는다.
- Root 단위와 Route 단위 Error Boundary를 고려한다.

---

### [실무]

역할 구분:

```text
Component 렌더링 오류
→ Error Boundary

API 요청 실패
→ Error State

Form 검증 실패
→ Field Error / Global Form Error

Route 없음
→ NotFoundPage

권한 없음
→ ForbiddenPage
```

Fallback UI 예:

```jsx
function FallbackUI({ onReset }) {
  return (
    <main role="alert">
      <h1>문제가 발생했습니다.</h1>
      <p>화면을 표시하는 중 오류가 발생했습니다.</p>
      <button type="button" onClick={onReset}>
        다시 시도
      </button>
    </main>
  );
}
```

권장:

- 앱 전체 Root Error Boundary를 둔다.
- 주요 Route 단위 Error Boundary를 둘 수 있다.
- Fallback UI에는 홈 이동 또는 다시 시도 액션을 제공한다.
- 오류 로깅은 사용자 메시지와 분리한다.
- 운영 환경에서는 stack trace를 사용자에게 보여주지 않는다.

주의:

- Error Boundary가 API Error를 자동으로 잡는다고 착각하지 않는다.
- 이벤트 핸들러 내부 오류는 try/catch 또는 상태 처리로 관리한다.
- 비동기 Promise 오류는 별도로 catch 처리해야 한다.
- Fallback UI도 접근성을 고려한다.

---

### [FAQ]

Q. Error Boundary가 API 에러도 잡아줘?
A. 아니다. API 요청 실패는 Error State로 직접 처리해야 한다.

Q. Error Boundary는 언제 필요해?
A. 예상하지 못한 렌더링 오류로 전체 앱이 깨지는 것을 막고 fallback UI를 보여주기 위해 필요하다.

Q. Error Boundary만 있으면 모든 에러 처리가 끝나?
A. 아니다. API 요청 실패, Form Validation, 인증 오류는 별도로 처리해야 한다.

Q. Fallback UI에는 뭘 넣어야 해?
A. 문제 안내 메시지와 사용자가 할 수 있는 다음 행동을 제공하는 것이 좋다.

---

# 8. Error Security Rules

## 8.1 Error Message Security

### [개념]

Error Message Security는 오류 메시지를 통해 민감한 내부 정보가 사용자에게 노출되지 않도록 하는 기준이다.

Error Message는 사용자에게 필요한 수준의 안내만 제공하고, 개발자 디버깅 정보는 로그 또는 모니터링 시스템으로 분리한다.

---

### [핵심]

노출 주의 정보:

- Stack Trace
- SQL Error
- Server Path
- Token Value
- Password
- Personal Data
- Internal Role Policy
- API Secret
- Infrastructure Detail
- Database Schema
- File System Path

핵심 규칙:

- 사용자 메시지와 개발자 로그를 분리한다.
- 운영 환경에서 stack trace를 노출하지 않는다.
- token, password, personal data를 로그나 UI에 노출하지 않는다.
- 서버 원문 message를 그대로 노출하기 전에 검토한다.
- 403에서 내부 권한 정책을 과도하게 노출하지 않는다.
- Validation Error는 사용자 수정에 필요한 수준만 제공한다.

---

### [실무]

사용자 메시지 예:

```text
요청 처리 중 문제가 발생했습니다.
```

개발자 로그 예:

```text
status=500
endpoint=/api/festivals
errorCode=INTERNAL_SERVER_ERROR
timestamp=2026-07-05T10:00:00
```

나쁜 메시지 예:

```text
SQLSyntaxErrorException: Unknown column users.password_hash in table...
```

좋은 메시지 예:

```text
서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.
```

권장:

- 운영 사용자에게는 안전한 generic message를 제공한다.
- 개발 환경 로그와 사용자 UI를 분리한다.
- Error Code는 사용자에게 보여줄 필요가 있을 때만 제한적으로 사용한다.
- 민감정보가 포함될 수 있는 message는 필터링한다.

주의:

- 서버 원문 message를 Toast로 그대로 띄우지 않는다.
- Authentication Error에서 token 상태를 상세히 노출하지 않는다.
- Authorization Error에서 내부 role 이름을 과도하게 노출하지 않는다.
- Validation Error도 개인정보를 포함하지 않게 한다.

---

### [FAQ]

Q. 서버 에러 원문을 그대로 보여주면 안 되는 이유는?
A. 내부 구조, SQL, 서버 경로, 보안 정보가 노출될 수 있기 때문이다.

Q. 개발자 로그와 사용자 메시지는 왜 나눠?
A. 사용자는 이해 가능한 해결 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

Q. Stack Trace를 사용자에게 보여줘도 돼?
A. 운영 환경에서는 보여주지 않는 것이 좋다.

Q. 403에서 필요한 role 정보를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 권한 정책을 과도하게 노출하지 않는 메시지가 좋다.

---

# 9. Error Troubleshooting Rules

## 9.1 Error Message Not Showing

### [개념]

Error Message Not Showing은 오류가 발생했지만 사용자에게 오류 메시지가 표시되지 않는 문제다.

이 문제는 catch 처리 누락, Error State 조건 오류, interceptor 반환 누락, error 객체 구조 착각에서 자주 발생한다.

---

### [핵심]

주요 원인:

- catch에서 에러를 삼킴
- setError 누락
- Error State 렌더링 조건 오류
- error 객체 구조 착각
- AxiosError Mapping 실패
- TanStack Query isError 미사용
- Form errors key 불일치
- Promise.reject 누락
- interceptor에서 error 반환 누락
- Toast provider 미설정

핵심 규칙:

- catch에서 error를 상태로 연결한다.
- Error UI 렌더링 조건을 확인한다.
- error.response?.data 구조를 확인한다.
- interceptor는 처리 후 Promise.reject를 반환한다.
- Field Error key와 input name을 맞춘다.
- 사용자 메시지 fallback을 제공한다.

---

### [실무]

Debug Flow:

```text
Error 발생
→ catch 진입 확인
→ error 객체 확인
→ message mapping 확인
→ setError 확인
→ Error UI 렌더링 조건 확인
→ role alert 확인
→ interceptor Promise.reject 확인
```

나쁜 예:

```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    showToast("오류가 발생했습니다.");
  },
);
```

문제:

- `Promise.reject(error)`가 없어 호출부가 오류를 인식하지 못할 수 있다.

개선 예:

```typescript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    showToast("오류가 발생했습니다.");
    return Promise.reject(error);
  },
);
```

Form Error Key 확인:

```text
Backend errors.email
→ Frontend input name="email"
→ errors.email 표시
```

권장:

- 오류를 잡았으면 사용자 상태와 연결한다.
- 공통 interceptor와 화면별 error 처리가 충돌하지 않게 한다.
- fallback message를 항상 제공한다.
- Error UI가 실제 DOM에 렌더링되는지 확인한다.

주의:

- catch에서 console.log만 하고 끝내지 않는다.
- interceptor에서 error를 삼키지 않는다.
- error 객체 구조를 추측하지 말고 Network Response를 확인한다.
- Toast만 의존하면 사용자가 놓칠 수 있다.

---

### [FAQ]

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. interceptor에서 에러 처리하면 화면에서는 못 받아?
A. Promise.reject를 반환하지 않으면 호출부가 에러를 인식하지 못할 수 있다.

Q. Form Field Error가 안 보여?
A. 서버 errors key와 Frontend input name이 일치하는지 확인해야 한다.

Q. Error Toast가 안 보여?
A. Toast provider 설정, 호출 위치, error catch 진입 여부를 확인해야 한다.

---

## 9.2 Blank Screen Error Troubleshooting

### [개념]

Blank Screen은 오류 메시지나 로딩 표시 없이 화면이 비어 보이는 문제다.

Blank Screen은 Error State 누락, 렌더링 오류, map on undefined, Route mismatch, CSS 문제에서 자주 발생한다.

---

### [핵심]

주요 원인:

- Loading / Error / Empty 처리 누락
- Runtime Render Error
- map on undefined
- Route Mismatch
- Component return null
- CSS display none
- API Response Shape Mismatch
- Error Boundary 없음
- Conditional Rendering 누락
- Suspense fallback 문제

핵심 규칙:

- Blank Screen 대신 Loading, Error, Empty 중 하나를 보여준다.
- Console Error를 확인한다.
- Network Response를 확인한다.
- Route Match를 확인한다.
- API 응답 구조와 컴포넌트 기대 구조를 비교한다.
- Error Boundary를 적용한다.
- 조건부 렌더링 순서를 확인한다.

---

### [실무]

Debug Flow:

```text
Blank Screen
→ Console Error 확인
→ Network Response 확인
→ Loading State 확인
→ Error State 확인
→ Empty State 확인
→ Route Match 확인
→ Component Return 확인
→ CSS 확인
```

map on undefined 나쁜 예:

```tsx
return (
  <ul>
    {data.items.map((item) => (
      <li key={item.id}>{item.title}</li>
    ))}
  </ul>
);
```

개선 예:

```tsx
const items = data?.items ?? [];

return (
  <ul>
    {items.map((item) => (
      <li key={item.id}>{item.title}</li>
    ))}
  </ul>
);
```

권장:

- API 응답이 예상과 다를 수 있음을 고려한다.
- data 접근 전 null check를 한다.
- Error Boundary를 두어 앱 전체 crash를 방지한다.
- Route fallback을 구성한다.
- CSS로 숨겨진 상태인지 확인한다.

주의:

- 빈 화면은 사용자에게 가장 나쁜 UX 중 하나다.
- 에러를 console에만 남기고 UI를 비워두지 않는다.
- Runtime Error가 발생하면 Error Boundary 없이는 앱 전체가 깨질 수 있다.
- Response shape mismatch는 자주 발생하는 원인이다.

---

### [FAQ]

Q. 화면이 아무것도 안 나와?
A. Console Error, Network Response, Route Match, Loading/Error/Empty 처리, Component return 값을 확인해야 한다.

Q. 빈 화면 대신 뭘 보여줘야 해?
A. 상황에 따라 Loading, Error, Empty, Not Found, Forbidden 같은 상태 UI를 보여줘야 한다.

Q. map on undefined 오류는 어떻게 막아?
A. data가 배열인지 확인하거나 기본값을 안전하게 설정해야 한다.

Q. Error Boundary가 없으면 어떤 문제가 생겨?
A. 렌더링 오류로 전체 앱이 깨지고 사용자에게 빈 화면이 보일 수 있다.

---

# 10. Error State Checklist

## 10.1 Error State Review Checklist

### [개념]

Error State Review Checklist는 화면과 컴포넌트가 오류 상황을 안정적으로 처리하는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Error State와 Empty State를 구분했는가?
- [ ] API Error State가 존재하는가?
- [ ] Error Message Mapping 함수가 존재하는가?
- [ ] 사용자 메시지와 개발자 로그를 분리했는가?
- [ ] 서버 원문 message를 그대로 노출하지 않는가?
- [ ] Network Error와 Server Error를 구분했는가?
- [ ] Timeout Error를 무한 Loading으로 방치하지 않는가?
- [ ] 400 / 422 Validation Error를 Field Error와 연결했는가?
- [ ] 401 Unauthorized와 403 Forbidden을 구분했는가?
- [ ] 404 Route Error와 404 API Error를 구분했는가?
- [ ] 409 Conflict 발생 시 서버 상태와 UI를 동기화하는가?
- [ ] 500 Server Error에 generic message를 제공하는가?
- [ ] Retry 가능한 오류에 Retry Action이 있는가?
- [ ] Retry Button이 실제 refetch와 연결되어 있는가?
- [ ] Field Error를 input 근처에 표시하는가?
- [ ] Global Form Error를 Form 상단 또는 버튼 근처에 표시하는가?
- [ ] 모든 오류를 Toast로만 처리하지 않는가?
- [ ] Error Boundary와 API Error State 역할을 구분했는가?
- [ ] stack trace, SQL Error, token 값이 노출되지 않는가?
- [ ] Error Message Not Showing 가능성을 점검했는가?
- [ ] Blank Screen 가능성을 점검했는가?
```

---

### [실무]

검수 흐름:

```text
Error Scenario 정의
→ Error Type 분류
→ User Message 확인
→ UI 위치 확인
→ Retry / Redirect 확인
→ Accessibility 확인
→ Security Exposure 확인
→ Troubleshooting 가능성 확인
```

화면별 기준:

| 화면           | 필수 Error UX                   |
| -------------- | ------------------------------- |
| 목록 화면      | API Error State + Retry         |
| 상세 화면      | API Error + Resource Not Found  |
| Form 화면      | Field Error + Global Form Error |
| 인증 화면      | 401 처리 + 세션 만료 UX         |
| 권한 페이지    | 403 Forbidden UX                |
| 알 수 없는 URL | Route NotFoundPage              |
| 렌더링 오류    | Error Boundary Fallback         |

---

### [FAQ]

Q. Error State 검수에서 가장 중요한 것은?
A. 오류 종류를 분류하고 사용자에게 안전하고 이해 가능한 메시지와 다음 행동을 제공하는 것이다.

Q. 목록 화면 Error UX는 어떻게 검수해?
A. API 실패 시 Error State가 표시되고 Retry Button이 실제 refetch와 연결되는지 확인한다.

Q. Form 화면 Error UX는 어떻게 검수해?
A. Field Error와 Global Form Error가 구분되고 Submit Loading이 실패 후 해제되는지 확인한다.

Q. Error Security 검수 핵심은?
A. stack trace, SQL Error, token, password, 서버 경로 같은 민감 정보가 사용자에게 노출되지 않는지 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Error Handling & Loading UX Part03은 무엇을 다뤄?
A. API Error State, Error Message Mapping, Network Error, HTTP Status UX, Form Error, Error Boundary, Error Security 기준을 다룬다.

Q. Error State는 뭐야?
A. 요청 실패, 권한 문제, 렌더링 오류처럼 정상 화면을 보여줄 수 없을 때 사용자에게 실패 상태를 알려주는 UI 상태다.

Q. Error State와 Empty State 차이는?
A. Error State는 요청 실패이고 Empty State는 요청 성공 후 데이터가 없는 상태다.

Q. 에러가 나면 alert만 띄워도 돼?
A. 간단한 실습은 가능하지만 실무에서는 오류 위치, 종류, 재시도 가능 여부에 따라 Inline Error, Page Error, Toast, Fallback UI를 구분한다.

Q. API 에러는 어떻게 보여줘?
A. 사용자가 이해할 수 있는 메시지와 필요한 경우 다시 시도 버튼을 제공한다.

Q. API 실패를 빈 배열로 처리해도 돼?
A. 권장하지 않는다. 실패 상태가 사라져 사용자가 오류를 알 수 없으므로 Error State로 분리해야 한다.

Q. Retry Button은 언제 제공해?
A. 네트워크 오류, 일시적 서버 오류, 조회 실패처럼 재시도 가능성이 있는 오류에 제공한다.

Q. ErrorState 컴포넌트는 공통으로 만들어도 돼?
A. 가능하다. message와 onRetry를 props로 받으면 여러 화면에서 재사용할 수 있다.

Q. 에러 메시지 mapping 함수는 왜 필요해?
A. API 에러 구조를 화면마다 직접 해석하면 중복이 생기고 메시지 기준이 달라질 수 있기 때문이다.

Q. 서버 message를 항상 사용해도 돼?
A. 아니다. 내부 정보가 포함될 수 있으면 사용자용 메시지로 변환해야 한다.

Q. unknown error에는 어떤 메시지를 보여줘?
A. “요청 처리 중 문제가 발생했습니다.” 같은 안전한 fallback 메시지를 제공한다.

Q. 화면별로 다른 에러 메시지를 쓰고 싶으면?
A. 공통 mapping 함수를 기본으로 사용하고 화면별 override 함수를 추가하면 된다.

Q. Network Error와 500 에러는 달라?
A. 다르다. Network Error는 응답 자체를 받지 못한 경우이고 500은 서버가 응답한 내부 오류다.

Q. Postman에서는 되는데 브라우저에서는 Network Error가 나?
A. CORS, Mixed Content, 브라우저 보안 정책 문제일 수 있다.

Q. Network Error에는 어떤 메시지를 보여줘?
A. 네트워크 연결을 확인해 달라는 메시지와 다시 시도 버튼을 제공하는 것이 좋다.

Q. CORS Error도 Network Error야?
A. 브라우저에서는 응답 접근이 차단되어 Network Error처럼 보일 수 있다.

Q. Timeout Error는 뭐야?
A. 요청이 정해진 시간 안에 완료되지 않아 실패한 상태다.

Q. Timeout이 나면 무조건 다시 시도하면 돼?
A. 조회 요청은 재시도가 가능하지만 결제, 삭제, 저장 같은 중요한 요청은 처리 여부 확인이 먼저 필요할 수 있다.

Q. Timeout 후 Loading은 어떻게 해야 해?
A. Loading을 종료하고 Error State 또는 Retry UI를 보여줘야 한다.

Q. 400 Bad Request는 언제 발생해?
A. 요청 형식, 파라미터, 요청 Body가 잘못되었을 때 발생한다.

Q. 400 Error는 사용자 잘못이야?
A. 항상 그렇지 않다. Frontend 요청 구조나 API Contract 불일치 문제일 수 있다.

Q. 400 Error 메시지는 어떻게 보여줘?
A. 사용자가 수정 가능한 경우 “입력 값을 확인해 주세요.”처럼 안내하고, 필드 오류가 있으면 input 근처에 표시한다.

Q. 401 Unauthorized는 뭐야?
A. 인증되지 않았거나 Access Token이 유효하지 않을 때 발생하는 오류다.

Q. 401이면 무조건 로그인 페이지로 보내?
A. Refresh Token Flow가 있으면 먼저 재발급을 시도하고 실패 시 로그인 페이지로 이동한다.

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 가능하다. 로그인 실패 401과 기존 인증 만료 401의 UX를 구분해야 한다.

Q. 403 Forbidden은 뭐야?
A. 로그인은 되었지만 해당 리소스나 기능에 접근할 권한이 없는 상태다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 로그인은 되어 있지만 권한이 부족한 상태이므로 권한 없음 UI를 보여주는 것이 일반적이다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증 필요이고 403은 인증은 되었지만 권한이 없는 상태다.

Q. 페이지 404와 API 404는 달라?
A. 다르다. 페이지 404는 Route 매칭 실패이고 API 404는 서버 리소스나 endpoint를 찾지 못한 것이다.

Q. 상세 페이지 데이터가 없으면 어떻게 보여줘?
A. 해당 리소스를 찾을 수 없다는 메시지와 목록으로 돌아가는 버튼을 제공하는 것이 좋다.

Q. API 404도 NotFoundPage로 보내?
A. 상황에 따라 다르다. 상세 리소스 없음은 해당 페이지 안에서 Resource Not Found UI를 보여줄 수 있다.

Q. 409 Conflict는 언제 발생해?
A. 이미 처리된 요청이거나 서버의 현재 상태와 요청이 충돌할 때 발생한다.

Q. 409가 나면 어떻게 해?
A. 사용자에게 상태 충돌을 안내하고 최신 서버 상태를 다시 조회하는 것이 좋다.

Q. 좋아요 중복 요청에서 409가 나면?
A. 좋아요 상태를 서버 최신 상태와 동기화하거나 refetch하는 것이 좋다.

Q. 422 Validation Error는 뭐야?
A. 요청 형식은 이해했지만 입력값이나 비즈니스 규칙 검증에 실패한 상태다.

Q. Validation Error는 alert로만 보여줘도 돼?
A. 권장하지 않는다. 필드별 오류는 해당 input 근처에 보여주는 것이 사용자가 수정하기 쉽다.

Q. 서버 검증 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 오류를 수정할 수 있도록 유지하는 것이 좋다.

Q. Field Error와 Global Error는 어떻게 나눠?
A. 특정 input 값 문제는 Field Error, Form 전체 문제나 인증 실패는 Global Error로 처리한다.

Q. 500 Server Error는 뭐야?
A. 서버 내부 오류로 요청 처리가 실패한 상태다.

Q. 500 에러 상세 내용을 사용자에게 보여줘도 돼?
A. 권장하지 않는다. 내부 구현 정보가 노출될 수 있으므로 일반적인 오류 메시지를 보여준다.

Q. 500이 나면 Frontend에서 해결할 수 있어?
A. 대부분 Backend 문제이지만 Frontend 요청 body나 endpoint가 잘못되어 서버 오류를 유발했는지도 확인해야 한다.

Q. Field Error는 어디에 보여줘?
A. 해당 input 근처에 보여주는 것이 좋다.

Q. Field Error를 Toast로만 보여줘도 돼?
A. 권장하지 않는다. 사용자가 어떤 필드를 수정해야 하는지 알기 어렵다.

Q. Global Form Error는 뭐야?
A. Form 전체에 해당하며 특정 field 하나로 귀속하기 어려운 오류 메시지다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 이메일 형식 오류는 Field Error이고 계정 정보 불일치 같은 인증 실패는 Global Error로 처리하는 경우가 많다.

Q. 모든 API 에러를 Toast로 처리하면 돼?
A. 아니다. Form field error, page error, permission error처럼 위치가 중요한 오류는 적절한 UI 위치에 표시해야 한다.

Q. Page Error는 언제 써?
A. 페이지나 주요 콘텐츠 데이터를 불러오지 못해 정상 화면을 보여줄 수 없을 때 사용한다.

Q. Toast는 언제 쓰는 게 좋아?
A. 저장 실패, 좋아요 실패처럼 짧게 알려도 되는 액션 결과에 적합하다.

Q. Error Boundary가 API 에러도 잡아줘?
A. 아니다. API 요청 실패는 Error State로 직접 처리해야 한다.

Q. Error Boundary는 언제 필요해?
A. 예상하지 못한 렌더링 오류로 전체 앱이 깨지는 것을 막고 fallback UI를 보여주기 위해 필요하다.

Q. Error Boundary만 있으면 모든 에러 처리가 끝나?
A. 아니다. API 요청 실패, Form Validation, 인증 오류는 별도로 처리해야 한다.

Q. 서버 에러 원문을 그대로 보여주면 안 되는 이유는?
A. 내부 구조, SQL, 서버 경로, 보안 정보가 노출될 수 있기 때문이다.

Q. 개발자 로그와 사용자 메시지는 왜 나눠?
A. 사용자는 이해 가능한 해결 안내가 필요하고 개발자는 원인 분석 정보가 필요하기 때문이다.

Q. Stack Trace를 사용자에게 보여줘도 돼?
A. 운영 환경에서는 보여주지 않는 것이 좋다.

Q. API는 실패했는데 에러 메시지가 안 보여?
A. catch에서 에러를 상태로 저장하는지, Error UI 조건이 맞는지, error mapping 함수가 올바른지 확인해야 한다.

Q. interceptor에서 에러 처리하면 화면에서는 못 받아?
A. Promise.reject를 반환하지 않으면 호출부가 에러를 인식하지 못할 수 있다.

Q. Form Field Error가 안 보여?
A. 서버 errors key와 Frontend input name이 일치하는지 확인해야 한다.

Q. 화면이 아무것도 안 나와?
A. Console Error, Network Response, Route Match, Loading/Error/Empty 처리, Component return 값을 확인해야 한다.

Q. 빈 화면 대신 뭘 보여줘야 해?
A. 상황에 따라 Loading, Error, Empty, Not Found, Forbidden 같은 상태 UI를 보여줘야 한다.

Q. map on undefined 오류는 어떻게 막아?
A. data가 배열인지 확인하거나 기본값을 안전하게 설정해야 한다.

Q. Error State 검수에서 가장 중요한 것은?
A. 오류 종류를 분류하고 사용자에게 안전하고 이해 가능한 메시지와 다음 행동을 제공하는 것이다.
