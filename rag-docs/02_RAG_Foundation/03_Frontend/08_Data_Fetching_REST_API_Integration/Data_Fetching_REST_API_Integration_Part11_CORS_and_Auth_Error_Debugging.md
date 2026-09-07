# Data Fetching & REST API Integration Part11 - CORS and Auth Error Debugging

---

# 1. CORS and Auth Error Overview

## 1.1 CORS / Auth Error 기본 개념

### [개념]

CORS와 Auth Error는 Frontend REST API Integration에서 가장 자주 발생하는 연동 문제다.

CORS는 브라우저의 Cross-Origin 보안 정책 문제이고, Auth Error는 인증 / 인가 / Token / Authorization Header 문제다.

Frontend Agent는 CORS Error, 401 Unauthorized, 403 Forbidden, Preflight 실패, Authorization Header 누락, Token 만료를 구분해야 한다.

기본 구분:

```text
CORS Error
→ Browser 보안 정책
→ Backend CORS 설정 확인

401 Unauthorized
→ 인증 실패
→ Authorization Header / Token 확인

403 Forbidden
→ 인가 실패
→ Role / Permission / Resource Owner 확인
```

---

### [핵심]

핵심 키워드:

- CORS
- Same-Origin Policy
- Origin
- Cross-Origin Request
- Preflight
- OPTIONS
- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Credentials
- Authorization Header
- Bearer Token
- Access Token
- Refresh Token
- 401 Unauthorized
- 403 Forbidden
- Token Expired
- Token Missing
- Role
- Permission
- Resource Owner
- SecurityConfig
- CORS Configuration
- Browser Network Tab

CORS / Auth Error 분석 기준:

```text
Browser Console 확인
→ Network OPTIONS 확인
→ Actual Request 확인
→ Request Headers 확인
→ Authorization Header 확인
→ Status Code 확인
→ Response Body 확인
→ Backend Security / CORS 설정 확인
```

---

### [실무]

2026 실무 기준에서 CORS / Auth Error는 다음 순서로 분석한다.

```text
1. Console에 CORS 메시지가 있는가?
2. Network 탭에 OPTIONS 요청이 있는가?
3. OPTIONS 요청이 성공했는가?
4. 실제 API 요청이 나갔는가?
5. Authorization Header가 포함되었는가?
6. Bearer Token 형식이 맞는가?
7. Status Code가 401인가 403인가?
8. Token이 만료되었는가?
9. 사용자 Role이 API 권한과 맞는가?
10. Backend CORS / Security 설정과 일치하는가?
```

주의:

- Postman 성공은 Browser 성공을 보장하지 않음
- CORS는 Postman에서 재현되지 않을 수 있음
- localStorage token 존재와 Request Header 포함은 다름
- 401과 403은 의미가 다름
- Frontend 권한 체크는 UX용이고 Backend 권한 검증이 최종 기준

---

### [FAQ]

Q. CORS와 Auth Error는 같은 문제야?
A. 아니다. CORS는 브라우저 보안 정책 문제이고 Auth Error는 인증 / 권한 문제다.

Q. Postman에서는 되는데 브라우저에서 안 돼?
A. Postman은 CORS 정책을 적용하지 않으므로 브라우저와 결과가 다를 수 있다.

Q. token이 있는데 401이 나면 뭐부터 봐?
A. Network 탭의 Request Headers에서 Authorization Header가 실제 포함되었는지 확인해야 한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증 실패이고 403은 인증 후 권한 부족이다.

---

# 2. Same-Origin Policy Rules

## 2.1 Same-Origin Policy 기준

### [개념]

Same-Origin Policy는 브라우저가 서로 다른 Origin 간의 요청을 제한하는 보안 정책이다.

Origin은 protocol, host, port 조합으로 결정된다.

Origin 구성:

```text
Origin = protocol + host + port
```

예:

```text
http://localhost:3000
http://localhost:8080
```

위 두 주소는 port가 다르므로 서로 다른 Origin이다.

---

### [핵심]

Origin 판단 기준:

- protocol
- host
- port

같은 Origin 예:

```text
http://localhost:3000/page
http://localhost:3000/login
```

다른 Origin 예:

```text
http://localhost:3000
http://localhost:8080

http://localhost:3000
https://localhost:3000

http://127.0.0.1:3000
http://localhost:3000
```

주의:

- port가 다르면 다른 Origin
- protocol이 다르면 다른 Origin
- localhost와 127.0.0.1도 다른 host로 볼 수 있음
- Browser에서만 CORS 정책이 적용됨
- Server-to-Server 요청에는 일반적으로 Browser CORS가 적용되지 않음

---

### [실무]

React 개발 서버와 Spring Boot 서버 예:

```text
Frontend Dev Server:
http://localhost:3000

Backend API Server:
http://localhost:8080

결과:
Cross-Origin Request
```

Vite 개발 서버 예:

```text
Frontend Dev Server:
http://localhost:5173

Backend API Server:
http://localhost:8080

결과:
Cross-Origin Request
```

기본 해결 방향:

```text
Frontend Origin을 Backend CORS Allowed Origin에 추가
```

주의:

- Frontend에서 header를 추가한다고 CORS가 해결되는 것이 아님
- Backend가 허용 응답 Header를 내려줘야 함
- 개발 proxy와 운영 CORS 설정을 구분
- 배포 후 domain / protocol / port 변경 확인

---

### [FAQ]

Q. Origin은 뭐로 결정돼?
A. protocol, host, port 조합으로 결정된다.

Q. localhost:3000과 localhost:8080은 같은 Origin이야?
A. 아니다. port가 다르므로 다른 Origin이다.

Q. localhost와 127.0.0.1은 같아?
A. 다르게 취급될 수 있다. host 문자열이 다르기 때문이다.

Q. Same-Origin Policy는 왜 있어?
A. 브라우저에서 다른 출처의 리소스 접근을 제한해 보안을 강화하기 위해 있다.

---

# 3. CORS Basic Rules

## 3.1 CORS 기본 기준

### [개념]

CORS는 Cross-Origin Resource Sharing의 약자다.

브라우저가 다른 Origin으로 API 요청을 보낼 때, Backend가 해당 Origin을 허용하는지 확인하는 정책이다.

---

### [핵심]

CORS 관련 Header:

- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Credentials
- Access-Control-Max-Age
- Origin

CORS 허용 대상:

- Origin
- Method
- Header
- Credentials
- Preflight Request

주의:

- CORS는 Browser 정책
- Backend 응답 Header가 중요
- Frontend 코드만으로 근본 해결 불가
- Postman은 CORS를 적용하지 않음
- Authorization Header 사용 시 preflight 발생 가능
- credentials 사용 시 wildcard origin 주의

---

### [실무]

CORS 성공 조건:

```text
Browser Request Origin
→ Backend CORS 설정에 Origin 포함
→ Method 허용
→ Header 허용
→ Credentials 정책 일치
→ Browser가 응답 허용
```

CORS Error 확인 Flow:

```text
Console CORS Error 확인
→ Network OPTIONS 요청 확인
→ Response Headers 확인
→ Access-Control-Allow-Origin 확인
→ Access-Control-Allow-Headers 확인
→ Access-Control-Allow-Methods 확인
```

대표 오류:

```text
No 'Access-Control-Allow-Origin' header is present
```

의미:

```text
Backend가 해당 Origin을 CORS 허용 응답으로 내려주지 않음
```

---

### [FAQ]

Q. CORS는 Frontend에서 해결해?
A. 근본 해결은 Backend CORS 설정에서 한다. Frontend proxy는 개발용 우회 방법일 수 있다.

Q. CORS Error는 왜 Postman에서 안 나?
A. Postman은 브라우저가 아니므로 Same-Origin Policy와 CORS를 적용하지 않는다.

Q. Access-Control-Allow-Origin은 누가 내려줘?
A. Backend 서버가 응답 Header로 내려줘야 한다.

Q. CORS Error는 서버가 죽어서 나는 거야?
A. 아닐 수 있다. 서버는 응답했지만 브라우저가 CORS 정책 때문에 차단했을 수 있다.

---

# 4. Preflight OPTIONS Rules

## 4.1 Preflight 기본

### [개념]

Preflight는 브라우저가 실제 요청을 보내기 전에 `OPTIONS` 요청으로 Backend가 해당 Cross-Origin 요청을 허용하는지 확인하는 과정이다.

Authorization Header, custom header, JSON Content-Type, PUT / PATCH / DELETE 요청 등에서 발생할 수 있다.

---

### [핵심]

Preflight 발생 조건 예:

- Authorization Header 사용
- Content-Type: application/json
- PUT 요청
- PATCH 요청
- DELETE 요청
- custom header 사용
- credentials 사용

Preflight 확인 대상:

- OPTIONS Request
- Origin Header
- Access-Control-Request-Method
- Access-Control-Request-Headers
- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Credentials

주의:

- OPTIONS 요청은 브라우저가 자동으로 보낼 수 있음
- 직접 작성한 API 요청이 아닐 수 있음
- Preflight가 실패하면 실제 API 요청이 나가지 않을 수 있음
- Backend Security가 OPTIONS를 막으면 CORS 실패 가능
- Authorization Header 허용 필요

---

### [실무]

Network 탭에서 확인:

```text
OPTIONS /api/reviews
Request Headers:
Origin: http://localhost:3000
Access-Control-Request-Method: POST
Access-Control-Request-Headers: authorization, content-type
```

정상 응답 예:

```text
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET,POST,PUT,PATCH,DELETE,OPTIONS
Access-Control-Allow-Headers: Authorization,Content-Type
```

문제 예:

```text
OPTIONS 요청 403
→ Backend Security가 OPTIONS 요청을 차단
```

문제 예:

```text
Access-Control-Allow-Headers에 Authorization 없음
→ Authorization Header 포함 요청 차단
```

Debug Flow:

```text
CORS Error
→ OPTIONS 요청 확인
→ OPTIONS Status 확인
→ Allow-Origin 확인
→ Allow-Methods 확인
→ Allow-Headers 확인
→ Backend CORS / Security 설정 확인
```

---

### [FAQ]

Q. OPTIONS 요청은 내가 보낸 거야?
A. 아닐 수 있다. 브라우저가 CORS preflight로 자동 전송한 요청일 수 있다.

Q. Preflight가 실패하면 실제 API 요청도 나가?
A. 대부분 실제 요청이 나가지 않는다.

Q. Authorization Header를 쓰면 Preflight가 발생해?
A. 발생할 수 있다. Backend가 Authorization Header를 허용해야 한다.

Q. OPTIONS가 403이면 뭐가 문제야?
A. Backend Security 설정이 OPTIONS 요청을 차단하거나 CORS 설정이 적용되지 않았을 수 있다.

---

# 5. CORS Header Rules

## 5.1 CORS Response Header 기준

### [개념]

CORS Response Header는 Backend가 브라우저에게 Cross-Origin 요청을 허용한다고 알려주는 Header다.

브라우저는 이 Header를 확인한 뒤 응답을 Frontend JavaScript에 노출할지 결정한다.

---

### [핵심]

주요 CORS Header:

```text
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
Access-Control-Allow-Credentials
Access-Control-Expose-Headers
Access-Control-Max-Age
```

Header 의미:

| Header                           | 의미                            |
| -------------------------------- | ------------------------------- |
| Access-Control-Allow-Origin      | 허용 Origin                     |
| Access-Control-Allow-Methods     | 허용 HTTP Method                |
| Access-Control-Allow-Headers     | 허용 Request Header             |
| Access-Control-Allow-Credentials | Cookie / 인증 정보 허용         |
| Access-Control-Expose-Headers    | JS에서 읽을 수 있는 응답 Header |
| Access-Control-Max-Age           | Preflight cache 시간            |

주의:

- Authorization Header는 Allow-Headers에 포함 필요
- credentials 사용 시 Allow-Credentials 필요
- credentials true와 wildcard origin 조합 주의
- Custom Response Header를 읽으려면 Expose-Headers 필요
- 운영 domain 변경 시 Allow-Origin 업데이트 필요

---

### [실무]

Authorization Header 허용 예:

```text
Access-Control-Allow-Headers: Authorization, Content-Type
```

Credentials 허용 예:

```text
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: http://localhost:3000
```

주의:

```text
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
```

위 조합은 문제가 될 수 있다.

Expose Header 예:

```text
Access-Control-Expose-Headers: Authorization
```

사용 상황:

```text
Backend가 새 Access Token을 Response Header로 내려주고
Frontend가 해당 Header를 읽어야 하는 경우
```

---

### [FAQ]

Q. Authorization Header를 보내려면 CORS에서 뭘 허용해야 해?
A. Access-Control-Allow-Headers에 Authorization이 포함되어야 한다.

Q. credentials true와 wildcard origin을 같이 써도 돼?
A. 일반적으로 문제가 될 수 있다. credentials를 사용하면 구체적인 Origin을 허용해야 한다.

Q. Response Header를 JS에서 읽을 수 없어?
A. Custom Response Header는 Access-Control-Expose-Headers에 포함되어야 읽을 수 있다.

Q. CORS Header는 Frontend가 설정해?
A. 아니다. Backend가 응답 Header로 설정해야 한다.

---

# 6. Development Proxy Rules

## 6.1 개발 Proxy 기준

### [개념]

Development Proxy는 Frontend 개발 서버가 API 요청을 Backend 서버로 대신 전달해 CORS 문제를 우회하는 개발 환경 설정이다.

Proxy는 개발 편의용이며 운영 배포 CORS 설정과는 별개다.

---

### [핵심]

Proxy 목적:

- 개발 중 CORS 우회
- 상대 경로 API 호출
- Frontend dev server에서 Backend로 요청 전달
- local development 편의

주의:

- Proxy는 운영 환경 해결책이 아님
- 운영에서는 Backend CORS 또는 같은 domain 배포 전략 필요
- proxy target 확인
- `/api` prefix rewrite 확인
- baseURL과 proxy 중복 설정 주의
- Network 탭 Request URL이 dev server로 보일 수 있음

---

### [실무]

CRA proxy 예:

```json
{
  "proxy": "http://localhost:8080"
}
```

API 호출:

```typescript
publicApi.get("/api/festivals");
```

Vite proxy 예:

```typescript
export default defineConfig({
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:8080",
        changeOrigin: true,
      },
    },
  },
});
```

주의:

```text
Frontend Request URL:
http://localhost:5173/api/festivals

Proxy Target:
http://localhost:8080/api/festivals
```

Debug 기준:

```text
개발에서는 proxy로 성공
운영 배포에서 실패
→ 운영 CORS / API baseURL 설정 확인
```

---

### [FAQ]

Q. 개발 Proxy를 쓰면 CORS 설정이 필요 없어?
A. 개발 중에는 우회할 수 있지만 운영에서는 CORS 설정이나 배포 구조를 별도로 맞춰야 한다.

Q. Proxy는 어디서 설정해?
A. CRA는 package.json proxy, Vite는 vite.config의 server.proxy에서 설정할 수 있다.

Q. Proxy를 쓰면 Request URL이 Frontend 서버로 보여?
A. 브라우저 기준으로는 Frontend dev server로 보일 수 있고 dev server가 Backend로 전달한다.

Q. 운영에서도 Vite proxy가 적용돼?
A. 아니다. Vite dev server proxy는 개발 환경용이다.

---

# 7. Authorization Header Rules

## 7.1 Authorization Header 기준

### [개념]

Authorization Header는 인증이 필요한 API 요청에서 Access Token을 Backend에 전달하는 Header다.

JWT 기반 인증에서는 일반적으로 Bearer Token 형식을 사용한다.

형식:

```text
Authorization: Bearer <accessToken>
```

---

### [핵심]

Authorization Header 확인 대상:

- Header 존재 여부
- Bearer prefix
- Bearer 뒤 공백
- Access Token 값
- token 만료 여부
- token 저장 key
- authApi interceptor
- publicApi / authApi 선택
- CORS Allow-Headers

주의:

- localStorage에 token이 있어도 Header에 자동 포함되지 않음
- authApi interceptor가 있어야 자동 추가 가능
- Bearer 형식 오류 시 401 발생 가능
- Authorization Header 사용 시 Preflight 발생 가능
- token 원문 로그 금지

---

### [실무]

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

Network 확인:

```text
Request Headers
Authorization: Bearer eyJhbGciOi...
```

잘못된 예:

```text
Authorization: eyJhbGciOi...
Authorization: BearereyJhbGciOi...
Authorization: Bearer
```

Debug Flow:

```text
401 발생
→ localStorage token 확인
→ authApi 사용 확인
→ Request Headers 확인
→ Bearer 형식 확인
→ CORS Allow-Headers 확인
```

---

### [FAQ]

Q. Authorization Header 형식은 뭐야?
A. `Authorization: Bearer <accessToken>` 형식이다.

Q. localStorage에 token이 있으면 자동으로 전송돼?
A. 아니다. interceptor나 직접 Header 설정이 필요하다.

Q. Bearer 뒤 공백이 중요해?
A. 중요하다. `Bearer <token>` 형식으로 공백이 있어야 한다.

Q. Authorization Header 때문에 CORS가 발생할 수 있어?
A. Authorization Header는 Preflight를 유발할 수 있으므로 Backend CORS에서 허용해야 한다.

---

# 8. publicApi / authApi Selection Rules

## 8.1 API Instance 선택 기준

### [개념]

`publicApi`와 `authApi` 선택 오류는 401과 불필요한 Authorization Header 문제를 유발한다.

Frontend Agent는 API 명세의 인증 필요 여부를 기준으로 Instance를 선택해야 한다.

---

### [핵심]

publicApi 사용 대상:

- 공개 목록 조회
- 공개 상세 조회
- 공개 검색
- 공개 필터 조회
- 로그인
- 회원가입
- 이메일 인증
- 비밀번호 찾기

authApi 사용 대상:

- 내 정보 조회
- 프로필 수정
- 찜 등록 / 취소
- 좋아요 등록 / 취소
- 리뷰 작성 / 수정 / 삭제
- 알림 조회
- 결제 요청
- 사용자 전용 데이터

주의:

- 로그인 요청은 보통 publicApi
- 인증 필요 API를 publicApi로 호출하면 401 가능
- 공개 API를 authApi로 호출하면 불필요한 token 전송 가능
- API 명세 기준으로 선택
- Backend SecurityConfig와 일치 확인

---

### [실무]

publicApi 예:

```typescript
export async function getFestivals(params: FestivalSearchParams) {
  const response = await publicApi.get("/festivals", { params });
  return response.data.data;
}
```

authApi 예:

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

Debug Flow:

```text
401 발생
→ API 명세에서 인증 필요 여부 확인
→ API Function에서 publicApi/authApi 확인
→ Authorization Header 확인
```

---

### [FAQ]

Q. publicApi와 authApi는 어떻게 골라?
A. API 명세에서 인증이 필요하면 authApi, 인증이 필요 없으면 publicApi를 사용한다.

Q. 로그인 API는 authApi야?
A. 보통 로그인 전 요청이므로 publicApi를 사용한다.

Q. 리뷰 작성 API는 authApi야?
A. 일반적으로 로그인 사용자만 작성 가능하므로 authApi를 사용한다.

Q. 공개 API를 authApi로 호출하면 안 돼?
A. 동작할 수도 있지만 불필요하게 token이 전송될 수 있으므로 publicApi와 authApi를 구분하는 것이 좋다.

---

# 9. 401 Unauthorized Deep Debugging Rules

## 9.1 401 심화 분석 기준

### [개념]

401 Unauthorized는 인증이 실패했음을 의미한다.

Token이 없거나, 형식이 틀렸거나, 만료되었거나, Backend에서 검증하지 못할 때 발생한다.

---

### [핵심]

401 원인 분류:

```text
Token Missing
Token Invalid
Token Expired
Token Malformed
Authorization Header Missing
Bearer Prefix Missing
Wrong Storage Key
Wrong API Instance
Refresh Failed
Backend Security Filter Issue
```

확인 대상:

- localStorage / sessionStorage
- cookie
- Authorization Header
- Bearer format
- token expiration
- request interceptor
- response interceptor
- refresh token flow
- Backend auth filter
- SecurityConfig permitAll 여부

주의:

- token 원문을 로그에 남기지 않음
- 401을 무조건 403처럼 처리하지 않음
- token 만료와 token 누락을 구분
- refresh flow 무한 반복 방지
- 인증 상태 UI와 실제 Header 전송 상태 구분

---

### [실무]

401 Debug Checklist:

```md
- [ ] localStorage에 accessToken이 있는가?
- [ ] token 저장 key가 interceptor와 일치하는가?
- [ ] API Function이 authApi를 사용하는가?
- [ ] Request Header에 Authorization이 있는가?
- [ ] Bearer prefix가 있는가?
- [ ] Bearer 뒤 공백이 있는가?
- [ ] token이 만료되지 않았는가?
- [ ] Backend가 해당 API를 인증 필요로 설정했는가?
- [ ] Refresh Token Flow가 있다면 재발급 요청이 성공하는가?
```

401 처리 예:

```typescript
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem("accessToken");
      // login redirect or refresh flow
    }

    return Promise.reject(error);
  },
);
```

주의:

- response interceptor에서 error를 삼키지 않음
- refresh 실패 시 사용자 상태 초기화
- public endpoint에서 401이 나면 Backend Security 설정도 확인
- 로그인 성공 후 token 저장과 이후 요청 Header 연결 확인

---

### [FAQ]

Q. 401은 무조건 token이 없다는 뜻이야?
A. 아니다. token이 있어도 만료, 형식 오류, 검증 실패, Header 누락이면 401이 날 수 있다.

Q. 로그인은 성공했는데 다음 요청이 401이야?
A. token 저장, authApi interceptor, Authorization Header 실제 포함 여부를 확인해야 한다.

Q. Refresh Token Flow가 있으면 401이 안 보여야 해?
A. Access Token 만료 시 내부적으로 refresh 후 재시도할 수 있지만 refresh 실패 시 401 처리가 필요하다.

Q. 401을 무조건 logout 처리해도 돼?
A. 프로젝트 기준에 따라 다르다. refresh flow가 있다면 먼저 재발급을 시도할 수 있다.

---

# 10. 403 Forbidden Deep Debugging Rules

## 10.1 403 심화 분석 기준

### [개념]

403 Forbidden은 사용자가 인증되었지만 해당 API나 Resource에 접근할 권한이 없음을 의미한다.

403은 token이 없어서 발생하는 문제가 아니라 권한 정책 문제일 가능성이 높다.

---

### [핵심]

403 원인 분류:

```text
Role Missing
Role Mismatch
Permission Missing
Resource Owner Mismatch
Admin Only API
Method Security Denied
SecurityConfig Rule Denied
Backend Authorization Logic Denied
```

확인 대상:

- 사용자 role
- token claims
- ROLE_USER / USER naming
- ROLE_ADMIN / ADMIN naming
- Backend SecurityConfig
- @PreAuthorize
- Resource Owner
- 작성자 권한
- 관리자 권한
- API 명세 권한 조건

주의:

- 403은 다시 로그인해도 해결되지 않을 수 있음
- 403을 token 만료로 처리하지 않음
- Frontend 버튼 숨김은 UX용
- Backend 권한 검증이 최종 기준
- Resource Owner 정책은 Backend에서 확인

---

### [실무]

403 Debug Checklist:

```md
- [ ] Authorization Header가 있는가?
- [ ] 401이 아니라 403인가?
- [ ] 사용자 role이 API 권한과 맞는가?
- [ ] token claims에 role이 포함되어 있는가?
- [ ] Backend 권한 문자열과 Frontend role 문자열이 일치하는가?
- [ ] Resource owner가 현재 사용자와 일치하는가?
- [ ] 관리자 전용 API를 일반 사용자가 호출한 것은 아닌가?
- [ ] SecurityConfig / @PreAuthorize 조건과 일치하는가?
```

403 사용자 메시지:

```typescript
if (status === 403) {
  return "접근 권한이 없습니다.";
}
```

권한 UI 기준:

```tsx
{
  canEdit && (
    <button type="button" onClick={handleEdit}>
      수정
    </button>
  );
}
```

주의:

- `canEdit`은 UX용
- 사용자가 버튼을 숨겨도 직접 API 호출 가능
- Backend에서 owner / role 검증 필수
- 403 발생 시 logout보다 권한 안내가 적합한 경우가 많음

---

### [FAQ]

Q. 403은 token이 없다는 뜻이야?
A. 아니다. 인증은 되었지만 권한이 부족하다는 뜻이다.

Q. 403이면 다시 로그인하면 해결돼?
A. 권한이 부족한 경우라면 다시 로그인해도 해결되지 않는다.

Q. ROLE_USER와 USER 차이가 문제 될 수 있어?
A. 될 수 있다. Backend 권한 문자열과 token role naming이 맞는지 확인해야 한다.

Q. Frontend에서 수정 버튼을 숨기면 권한 처리가 끝나?
A. 아니다. Backend에서 최종 권한 검증을 해야 한다.

---

# 11. Token Refresh Debugging Rules

## 11.1 Token Refresh 문제 분석

### [개념]

Token Refresh는 Access Token 만료 시 Refresh Token으로 새 Access Token을 발급받고 원래 요청을 재시도하는 흐름이다.

Token Refresh 문제는 401 반복, 무한 재시도, 원래 요청 실패, logout 처리 실패로 나타날 수 있다.

---

### [핵심]

Token Refresh Flow:

```text
API Request
→ 401 Access Token Expired
→ Refresh Request
→ New Access Token
→ Store New Access Token
→ Retry Original Request
→ If Refresh Failed
→ Clear Auth State
→ Redirect Login
```

문제 원인:

- refresh endpoint 오류
- refresh token 없음
- refresh token 만료
- 새 access token 저장 실패
- original request retry 실패
- Authorization Header 갱신 누락
- refresh 요청도 interceptor 대상이 됨
- 무한 retry loop
- 동시 401 요청 queue 처리 누락

주의:

- refresh 요청이 다시 401이면 logout
- original request retry는 1회 제한
- `_retry` flag 필요 가능
- refresh endpoint는 별도 instance 사용 가능
- token 원문 로그 금지
- 인증 심화는 Authentication Frontend Flow 문서와 연계

---

### [실무]

기초 retry flag:

```typescript
authApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      // refresh access token
      // save new access token
      // originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
      // return authApi(originalRequest)
    }

    return Promise.reject(error);
  },
);
```

Debug Checklist:

```md
- [ ] 401 발생 원인이 token 만료인가?
- [ ] refresh 요청이 실제로 나가는가?
- [ ] refresh 요청 URL / Method가 맞는가?
- [ ] refresh 요청에 필요한 credential이 포함되는가?
- [ ] 새 Access Token이 응답으로 내려오는가?
- [ ] 새 Access Token을 저장하는가?
- [ ] originalRequest Header를 갱신하는가?
- [ ] originalRequest를 1회 재시도하는가?
- [ ] refresh 실패 시 logout 처리하는가?
- [ ] 무한 refresh loop가 없는가?
```

---

### [FAQ]

Q. Access Token이 만료되면 어떻게 해?
A. Refresh Token으로 새 Access Token을 요청하고 성공하면 원래 요청을 재시도할 수 있다.

Q. Refresh 요청도 401이면 어떻게 해?
A. Refresh Token도 만료되었거나 유효하지 않을 수 있으므로 logout 처리하고 로그인으로 유도한다.

Q. 무한 refresh loop는 왜 생겨?
A. refresh 요청이나 재시도 요청이 계속 401을 반환하는데 retry 제한이 없으면 발생할 수 있다.

Q. Refresh 심화 구현은 이 문서 범위야?
A. 이 문서는 Debugging 기준이고 상세 인증 흐름은 Authentication Frontend Flow 문서에서 다룬다.

---

# 12. Cookie Credentials Rules

## 12.1 Cookie 기반 인증과 credentials

### [개념]

Cookie 기반 인증은 token을 Authorization Header가 아니라 Cookie로 주고받는 방식이다.

Cross-Origin Cookie 요청에서는 Frontend의 `withCredentials` 또는 `credentials` 설정과 Backend의 CORS credentials 설정이 필요하다.

---

### [핵심]

Axios 설정:

```text
withCredentials: true
```

fetch 설정:

```text
credentials: "include"
```

Backend CORS 필요:

```text
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: 구체적 Origin
```

Cookie 확인 대상:

- Set-Cookie
- HttpOnly
- Secure
- SameSite
- Domain
- Path
- Expires / Max-Age
- credentials include
- withCredentials true

주의:

- credentials true와 wildcard origin 조합 주의
- SameSite=None이면 Secure 필요 가능
- HttpOnly Cookie는 JavaScript에서 읽을 수 없음
- Cookie 인증과 Authorization Header 인증을 혼동하지 않음
- localhost / https 환경 차이 확인

---

### [실무]

Axios credentials:

```typescript
export const authApi = axios.create({
  baseURL,
  timeout: 10000,
  withCredentials: true,
});
```

fetch credentials:

```typescript
await fetch("/api/auth/refresh", {
  method: "POST",
  credentials: "include",
});
```

Cookie Debug Flow:

```text
Login Request
→ Response Headers Set-Cookie 확인
→ Application Tab Cookie 확인
→ 다음 Request에 Cookie 포함 여부 확인
→ Backend CORS credentials 설정 확인
```

주의:

- Authorization Header 기반 JWT와 Cookie 기반 JWT는 처리 방식이 다름
- Refresh Token만 HttpOnly Cookie로 두는 구조 가능
- Frontend에서 HttpOnly Cookie 값을 직접 읽으려 하면 안 됨
- Cookie가 저장되지 않으면 SameSite / Secure / Domain 확인

---

### [FAQ]

Q. Cookie 인증이면 Authorization Header가 필요 없어?
A. 구조에 따라 다르다. Cookie 기반 인증은 Cookie가 인증 정보를 전달할 수 있다.

Q. withCredentials는 언제 써?
A. Cross-Origin 요청에서 Cookie를 포함해야 할 때 Axios에 설정한다.

Q. fetch에서는 credentials를 어떻게 설정해?
A. `credentials: "include"`를 사용한다.

Q. HttpOnly Cookie는 localStorage처럼 읽을 수 있어?
A. 아니다. JavaScript에서 직접 읽을 수 없고 브라우저가 요청에 자동 포함한다.

---

# 13. Auth State Sync Rules

## 13.1 인증 상태 동기화 기준

### [개념]

Auth State Sync는 token 저장 상태, 사용자 로그인 상태, API Header, UI 권한 표시가 서로 일치하도록 관리하는 기준이다.

Frontend에서 로그인 상태라고 표시되더라도 실제 API 요청에 Authorization Header가 없으면 인증 API는 실패한다.

---

### [핵심]

동기화 대상:

- accessToken storage
- refresh token storage
- user profile
- auth context
- auth store
- authApi interceptor
- route guard
- permission UI
- logout state
- query cache

불일치 상황:

- UI는 로그인 상태인데 Header 없음
- token은 있는데 user profile 없음
- user profile은 있는데 token 만료
- logout 후 query cache 남음
- refresh 후 Header에 이전 token 사용
- 다른 탭 logout 반영 안 됨

주의:

- 로그인 성공 후 token 저장과 user state 갱신
- logout 시 token 제거와 user state 초기화
- logout 시 민감 query cache clear
- refresh 성공 후 새 token 사용
- authApi interceptor가 최신 token을 읽는지 확인

---

### [실무]

로그인 성공 Flow:

```text
Login Success
→ Save Access Token
→ Save User Info or Fetch My Profile
→ Auth State Update
→ Authenticated Route Access
→ authApi sends Authorization Header
```

로그아웃 Flow:

```text
Logout
→ Remove Access Token
→ Clear User State
→ Clear Sensitive Query Cache
→ Redirect Public Page
```

Query Cache Clear 예:

```typescript
function logout() {
  localStorage.removeItem("accessToken");
  setUser(null);
  queryClient.clear();
}
```

Debug Flow:

```text
UI 로그인 상태인데 401
→ token storage 확인
→ auth state 확인
→ authApi interceptor 확인
→ Request Header 확인
→ token 만료 확인
```

---

### [FAQ]

Q. UI는 로그인인데 API는 401이야?
A. 실제 Request Header에 Authorization이 없거나 token이 만료되었을 수 있다.

Q. logout할 때 query cache도 지워야 해?
A. 사용자 민감 데이터가 cache에 남을 수 있으므로 clear 또는 관련 query remove를 고려해야 한다.

Q. refresh 후에도 401이 계속 나?
A. 새 access token 저장, original request header 갱신, interceptor가 최신 token을 읽는지 확인해야 한다.

Q. user state와 token은 같은 거야?
A. 아니다. user state는 UI용 사용자 정보이고 token은 API 인증에 사용하는 값이다.

---

# 14. Route Guard and API Auth Rules

## 14.1 Route Guard와 API 권한 구분

### [개념]

Route Guard는 Frontend 화면 접근을 제어하는 UX 장치다.

API Auth는 Backend가 실제 API 요청을 인증 / 인가하는 보안 장치다.

두 개념은 반드시 구분해야 한다.

---

### [핵심]

Route Guard 역할:

- 로그인 필요 페이지 접근 제어
- 권한 없는 메뉴 숨김
- 로그인 페이지 redirect
- 사용자 경험 개선

API Auth 역할:

- 인증 여부 검증
- 권한 검증
- Resource Owner 검증
- 서버 데이터 보호
- 실제 보안 기준

주의:

- Route Guard만으로 보안 완성 불가
- 사용자는 API를 직접 호출할 수 있음
- Backend 권한 검증 필수
- Frontend 권한 체크와 Backend 권한 정책 동기화
- 403은 Backend 인가 실패 결과

---

### [실무]

Route Guard 예:

```tsx
function PrivateRoute({ children }: { children: React.ReactNode }) {
  const { isLoggedIn } = useAuth();

  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

권한 UI 예:

```tsx
{
  user?.role === "ADMIN" && <Link to="/admin">관리자 페이지</Link>;
}
```

API Auth 예:

```typescript
export async function getAdminDashboard() {
  const response = await authApi.get("/admin/dashboard");
  return response.data.data;
}
```

주의:

```text
Frontend에서 admin 링크를 숨겨도
Backend /admin/dashboard API는 반드시 ADMIN 권한 검증 필요
```

---

### [FAQ]

Q. Route Guard만 있으면 보안이 끝나?
A. 아니다. Route Guard는 UX용이고 실제 보안은 Backend API Auth에서 처리해야 한다.

Q. 버튼을 숨기면 API 호출도 막혀?
A. 아니다. 사용자가 직접 API를 호출할 수 있으므로 Backend 검증이 필요하다.

Q. 403은 Route Guard 문제야 API 권한 문제야?
A. 대부분 Backend API 권한 문제다. Route Guard는 사전에 접근을 줄이는 UX 역할이다.

Q. Frontend 권한 체크는 왜 필요해?
A. 사용자가 불가능한 행동을 시도하지 않도록 UI를 정리하는 데 필요하다.

---

# 15. Security Logging Rules

## 15.1 인증 / CORS Debug 로그 보안 기준

### [개념]

CORS와 Auth Debugging 중에는 token, user info, request payload 같은 민감정보가 로그에 노출될 수 있다.

Frontend Agent는 문제 분석 시 필요한 정보만 확인하고 민감정보는 마스킹해야 한다.

---

### [핵심]

로그 금지 대상:

- Access Token 원문
- Refresh Token 원문
- Authorization Header 전체
- Password
- 주민번호 / 민감 개인정보
- 결제 정보
- Cookie 원문
- Private Key
- API Secret

마스킹 가능 정보:

- token prefix 일부
- userId
- role
- status code
- endpoint
- method
- timestamp
- error code

주의:

- console.log로 token 출력 금지
- 오류 보고서에 token 원문 포함 금지
- screenshot에 Authorization Header 노출 주의
- request payload에 개인정보가 있으면 마스킹
- 운영 환경에서 debug log 제거

---

### [실무]

나쁜 예:

```typescript
console.log("token", accessToken);
console.log("headers", config.headers);
```

나은 예:

```typescript
console.log("auth request", {
  url: config.url,
  method: config.method,
  hasAuthorization: Boolean(config.headers.Authorization),
});
```

오류 보고 예:

```md
- Method: POST
- URL: /api/reviews
- Status: 401
- Authorization Header: 존재함
- Token 원문: 공유하지 않음
```

주의:

- 개발 중 임시 로그도 커밋 전 제거
- 브라우저 콘솔 화면 공유 시 token 노출 주의
- 에러 리포트에는 원인 분석에 필요한 최소 정보만 포함

---

### [FAQ]

Q. token을 console.log로 찍어도 돼?
A. 권장하지 않는다. token은 민감정보이므로 로그에 남기지 않아야 한다.

Q. 오류 보고할 때 Authorization Header를 보내야 해?
A. 원문을 보내면 안 된다. Header 존재 여부와 Bearer 형식 여부만 설명하는 것이 좋다.

Q. screenshot에 token이 보이면 문제야?
A. 문제다. token이 노출될 수 있으므로 반드시 가리거나 공유하지 않아야 한다.

Q. 어떤 정보는 공유해도 돼?
A. URL, Method, Status Code, 발생 시각, Header 존재 여부, Response message 정도는 마스킹 후 공유할 수 있다.

---

# 16. CORS / Auth Testing Rules

## 16.1 CORS / Auth Error 테스트 기준

### [개념]

CORS / Auth Testing은 Browser 환경에서 CORS, 401, 403, Token 만료, Header 누락 상황이 의도대로 처리되는지 검증하는 과정이다.

---

### [핵심]

테스트 대상:

- Public API 호출
- Auth API 호출
- Authorization Header 포함 여부
- token 없음
- token 만료
- token 위조
- Role 부족
- Resource Owner 불일치
- CORS 허용 Origin
- CORS 미허용 Origin
- Preflight OPTIONS
- credentials cookie

테스트 도구:

- Browser Network Tab
- DevTools Application Tab
- Backend Log
- Swagger UI
- Postman
- Mock Token
- Expired Token
- Different Role User

주의:

- Browser CORS 테스트는 실제 Browser에서 수행
- Postman으로 CORS 검증 불가
- token 원문 노출 주의
- 테스트 후 localStorage / cookie 정리
- 권한 테스트는 여러 role 계정 필요 가능

---

### [실무]

테스트 시나리오:

```text
Public API
→ token 없이 요청
→ 200 OK 기대
```

```text
Auth API
→ token 없이 요청
→ 401 Unauthorized 기대
```

```text
Auth API
→ 유효 token 포함
→ 200 OK 기대
```

```text
Admin API
→ 일반 USER token 포함
→ 403 Forbidden 기대
```

```text
Authorization Header 포함 요청
→ OPTIONS Preflight 확인
→ Allow-Headers에 Authorization 포함 확인
```

검수 Flow:

```text
Scenario 실행
→ Network Request 확인
→ Header 확인
→ Status Code 확인
→ Response Body 확인
→ UI Error State 확인
→ Backend Log 확인
```

---

### [FAQ]

Q. CORS 테스트는 Postman으로 가능해?
A. 아니다. CORS는 브라우저 정책이므로 실제 Browser에서 확인해야 한다.

Q. 401 테스트는 어떻게 해?
A. token을 제거하거나 만료 token을 사용해 인증 API를 호출한다.

Q. 403 테스트는 어떻게 해?
A. 권한이 부족한 계정으로 권한이 필요한 API를 호출한다.

Q. 테스트 후 뭘 정리해야 해?
A. localStorage token, cookie, test account state, query cache를 정리해야 한다.

---

# 17. Common Mistakes

## 17.1 CORS / Auth Error 공통 실수

### [개념]

CORS / Auth Error 실수는 Browser 정책, Authorization Header, Token 상태, Role 권한을 혼동할 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- CORS를 Frontend 코드만으로 해결하려 함
- Postman 성공을 CORS 성공으로 착각
- OPTIONS 요청을 직접 보낸 요청으로 착각
- Authorization Header를 CORS Allow-Headers에 포함하지 않음
- credentials true와 wildcard origin을 함께 사용
- localStorage token 존재를 Header 전송으로 착각
- Bearer prefix 누락
- Bearer 뒤 공백 누락
- publicApi와 authApi 선택 오류
- 로그인 API를 authApi로 호출
- 인증 API를 publicApi로 호출
- 401과 403 혼동
- 403을 무조건 logout 처리
- Role naming 불일치 미확인
- Route Guard를 보안으로 착각
- Refresh Token 무한 loop
- refresh 후 original request Header 갱신 누락
- Cookie 인증에서 withCredentials 누락
- HttpOnly Cookie를 JS로 읽으려 함
- token 원문을 console.log로 출력
- 오류 보고서에 Authorization Header 원문 포함

---

### [실무]

문제 예:

```text
문제: Postman은 성공하지만 브라우저 실패
원인: Backend CORS 설정에 Origin / Authorization Header 누락
해결: Browser Network OPTIONS와 CORS Response Header 확인
```

문제 예:

```text
문제: 로그인 후 리뷰 작성 401
원인: createReview API가 publicApi 사용
해결: authApi 사용 및 Authorization Header 확인
```

문제 예:

```text
문제: 관리자 페이지 API 403
원인: USER role로 ADMIN API 호출
해결: 사용자 role과 Backend 권한 정책 확인
```

문제 예:

```text
문제: Access Token 만료 후 요청이 무한 반복
원인: refresh retry 제한 없음
해결: _retry flag와 refresh 실패 logout 처리 추가
```

해결 우선순위:

```text
Console CORS Message 확인
→ Network OPTIONS 확인
→ Actual Request 확인
→ Authorization Header 확인
→ Status Code 401/403 확인
→ Token / Role 확인
→ Backend CORS / Security 설정 확인
```

---

### [FAQ]

Q. CORS / Auth Error에서 가장 흔한 실수는?
A. Postman 성공을 Browser 성공으로 착각하거나 token 존재를 Authorization Header 전송으로 착각하는 것이다.

Q. OPTIONS 요청이 실패하면 뭘 봐?
A. Backend CORS 설정, allowed methods, allowed headers, SecurityConfig의 OPTIONS 허용 여부를 확인한다.

Q. 401과 403을 같은 메시지로 처리해도 돼?
A. 권장하지 않는다. 401은 로그인 필요, 403은 권한 없음으로 구분하는 것이 좋다.

Q. token을 로그로 찍으면 왜 안 돼?
A. token이 노출되면 계정 탈취나 API 오용 위험이 생길 수 있다.

---

# 18. Part11 Checklist

## 18.1 CORS and Auth Error Debugging 검수 기준

### [개념]

Part11 CORS and Auth Error Debugging 문서는 Frontend Agent가 CORS, Preflight, Authorization Header, 401, 403, Token Refresh, Cookie Credentials 문제를 구분하고 안전하게 디버깅하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] CORS / Auth Error 기본 개념이 포함되었는가?
- [ ] Same-Origin Policy 기준이 포함되었는가?
- [ ] CORS 기본 기준이 포함되었는가?
- [ ] Preflight OPTIONS 기준이 포함되었는가?
- [ ] CORS Header 기준이 포함되었는가?
- [ ] Development Proxy 기준이 포함되었는가?
- [ ] Authorization Header 기준이 포함되었는가?
- [ ] publicApi / authApi 선택 기준이 포함되었는가?
- [ ] 401 Unauthorized 심화 기준이 포함되었는가?
- [ ] 403 Forbidden 심화 기준이 포함되었는가?
- [ ] Token Refresh Debugging 기준이 포함되었는가?
- [ ] Cookie Credentials 기준이 포함되었는가?
- [ ] Auth State Sync 기준이 포함되었는가?
- [ ] Route Guard와 API Auth 구분이 포함되었는가?
- [ ] Security Logging 기준이 포함되었는가?
- [ ] CORS / Auth Testing 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ CORS Concept Check
→ Same-Origin Check
→ Preflight Check
→ CORS Header Check
→ Authorization Header Check
→ publicApi / authApi Check
→ 401 / 403 Check
→ Token Refresh Check
→ Cookie Credentials Check
→ Auth State Sync Check
→ Security Logging Check
→ Testing Scenario Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- Same-Origin과 CORS 구분 가능
- Preflight OPTIONS 요청 분석 가능
- CORS Response Header 확인 가능
- Authorization Header와 Bearer Token 형식 검증 가능
- publicApi / authApi 선택 오류 분석 가능
- 401과 403 구분 가능
- Token Refresh 오류 분석 가능
- Cookie credentials 이슈 분석 가능
- Route Guard와 Backend API Auth 구분 가능
- token 원문 노출 없이 안전한 디버깅 가능
- Frontend Agent가 CORS / Auth Error를 정확히 진단 가능

---

### [FAQ]

Q. Part11의 목적은 뭐야?
A. Frontend Agent가 CORS, Preflight, Authorization Header, 401, 403, Token Refresh, Cookie Credentials 문제를 구분하고 안전하게 디버깅하게 만드는 것이다.

Q. Part11에서 가장 중요한 기준은 뭐야?
A. Browser Network 탭에서 OPTIONS, Actual Request, Authorization Header, Status Code, Response Body를 구분해 확인하는 것이다.

Q. Part11 다음에는 어떤 문서가 이어지면 좋아?
A. API Testing, Error Handling Architecture, Authentication Frontend Flow, Frontend Build & Deploy API Config 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. CORS와 Auth Error는 같은 문제야?
A. 아니다. CORS는 브라우저 보안 정책 문제이고 Auth Error는 인증 / 권한 문제다.

Q. Postman에서는 되는데 브라우저에서 안 돼?
A. Postman은 CORS 정책을 적용하지 않으므로 브라우저와 결과가 다를 수 있다.

Q. token이 있는데 401이 나면 뭐부터 봐?
A. Network 탭의 Request Headers에서 Authorization Header가 실제 포함되었는지 확인해야 한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증 실패이고 403은 인증 후 권한 부족이다.

Q. Origin은 뭐로 결정돼?
A. protocol, host, port 조합으로 결정된다.

Q. localhost:3000과 localhost:8080은 같은 Origin이야?
A. 아니다. port가 다르므로 다른 Origin이다.

Q. localhost와 127.0.0.1은 같아?
A. 다르게 취급될 수 있다. host 문자열이 다르기 때문이다.

Q. Same-Origin Policy는 왜 있어?
A. 브라우저에서 다른 출처의 리소스 접근을 제한해 보안을 강화하기 위해 있다.

Q. CORS는 Frontend에서 해결해?
A. 근본 해결은 Backend CORS 설정에서 한다. Frontend proxy는 개발용 우회 방법일 수 있다.

Q. CORS Error는 왜 Postman에서 안 나?
A. Postman은 브라우저가 아니므로 Same-Origin Policy와 CORS를 적용하지 않는다.

Q. Access-Control-Allow-Origin은 누가 내려줘?
A. Backend 서버가 응답 Header로 내려줘야 한다.

Q. CORS Error는 서버가 죽어서 나는 거야?
A. 아닐 수 있다. 서버는 응답했지만 브라우저가 CORS 정책 때문에 차단했을 수 있다.

Q. OPTIONS 요청은 내가 보낸 거야?
A. 아닐 수 있다. 브라우저가 CORS preflight로 자동 전송한 요청일 수 있다.

Q. Preflight가 실패하면 실제 API 요청도 나가?
A. 대부분 실제 요청이 나가지 않는다.

Q. Authorization Header를 쓰면 Preflight가 발생해?
A. 발생할 수 있다. Backend가 Authorization Header를 허용해야 한다.

Q. OPTIONS가 403이면 뭐가 문제야?
A. Backend Security 설정이 OPTIONS 요청을 차단하거나 CORS 설정이 적용되지 않았을 수 있다.

Q. Authorization Header를 보내려면 CORS에서 뭘 허용해야 해?
A. Access-Control-Allow-Headers에 Authorization이 포함되어야 한다.

Q. credentials true와 wildcard origin을 같이 써도 돼?
A. 일반적으로 문제가 될 수 있다. credentials를 사용하면 구체적인 Origin을 허용해야 한다.

Q. Response Header를 JS에서 읽을 수 없어?
A. Custom Response Header는 Access-Control-Expose-Headers에 포함되어야 읽을 수 있다.

Q. CORS Header는 Frontend가 설정해?
A. 아니다. Backend가 응답 Header로 설정해야 한다.

Q. 개발 Proxy를 쓰면 CORS 설정이 필요 없어?
A. 개발 중에는 우회할 수 있지만 운영에서는 CORS 설정이나 배포 구조를 별도로 맞춰야 한다.

Q. Proxy는 어디서 설정해?
A. CRA는 package.json proxy, Vite는 vite.config의 server.proxy에서 설정할 수 있다.

Q. Proxy를 쓰면 Request URL이 Frontend 서버로 보여?
A. 브라우저 기준으로는 Frontend dev server로 보일 수 있고 dev server가 Backend로 전달한다.

Q. 운영에서도 Vite proxy가 적용돼?
A. 아니다. Vite dev server proxy는 개발 환경용이다.

Q. Authorization Header 형식은 뭐야?
A. `Authorization: Bearer <accessToken>` 형식이다.

Q. localStorage에 token이 있으면 자동으로 전송돼?
A. 아니다. interceptor나 직접 Header 설정이 필요하다.

Q. Bearer 뒤 공백이 중요해?
A. 중요하다. `Bearer <token>` 형식으로 공백이 있어야 한다.

Q. Authorization Header 때문에 CORS가 발생할 수 있어?
A. Authorization Header는 Preflight를 유발할 수 있으므로 Backend CORS에서 허용해야 한다.

Q. publicApi와 authApi는 어떻게 골라?
A. API 명세에서 인증이 필요하면 authApi, 인증이 필요 없으면 publicApi를 사용한다.

Q. 로그인 API는 authApi야?
A. 보통 로그인 전 요청이므로 publicApi를 사용한다.

Q. 리뷰 작성 API는 authApi야?
A. 일반적으로 로그인 사용자만 작성 가능하므로 authApi를 사용한다.

Q. 공개 API를 authApi로 호출하면 안 돼?
A. 동작할 수도 있지만 불필요하게 token이 전송될 수 있으므로 publicApi와 authApi를 구분하는 것이 좋다.

Q. 401은 무조건 token이 없다는 뜻이야?
A. 아니다. token이 있어도 만료, 형식 오류, 검증 실패, Header 누락이면 401이 날 수 있다.

Q. 로그인은 성공했는데 다음 요청이 401이야?
A. token 저장, authApi interceptor, Authorization Header 실제 포함 여부를 확인해야 한다.

Q. Refresh Token Flow가 있으면 401이 안 보여야 해?
A. Access Token 만료 시 내부적으로 refresh 후 재시도할 수 있지만 refresh 실패 시 401 처리가 필요하다.

Q. 401을 무조건 logout 처리해도 돼?
A. 프로젝트 기준에 따라 다르다. refresh flow가 있다면 먼저 재발급을 시도할 수 있다.

Q. 403은 token이 없다는 뜻이야?
A. 아니다. 인증은 되었지만 권한이 부족하다는 뜻이다.

Q. 403이면 다시 로그인하면 해결돼?
A. 권한이 부족한 경우라면 다시 로그인해도 해결되지 않는다.

Q. ROLE_USER와 USER 차이가 문제 될 수 있어?
A. 될 수 있다. Backend 권한 문자열과 token role naming이 맞는지 확인해야 한다.

Q. Frontend에서 수정 버튼을 숨기면 권한 처리가 끝나?
A. 아니다. Backend에서 최종 권한 검증을 해야 한다.

Q. Access Token이 만료되면 어떻게 해?
A. Refresh Token으로 새 Access Token을 요청하고 성공하면 원래 요청을 재시도할 수 있다.

Q. Refresh 요청도 401이면 어떻게 해?
A. Refresh Token도 만료되었거나 유효하지 않을 수 있으므로 logout 처리하고 로그인으로 유도한다.

Q. 무한 refresh loop는 왜 생겨?
A. refresh 요청이나 재시도 요청이 계속 401을 반환하는데 retry 제한이 없으면 발생할 수 있다.

Q. Refresh 심화 구현은 이 문서 범위야?
A. 이 문서는 Debugging 기준이고 상세 인증 흐름은 Authentication Frontend Flow 문서에서 다룬다.

Q. Cookie 인증이면 Authorization Header가 필요 없어?
A. 구조에 따라 다르다. Cookie 기반 인증은 Cookie가 인증 정보를 전달할 수 있다.

Q. withCredentials는 언제 써?
A. Cross-Origin 요청에서 Cookie를 포함해야 할 때 Axios에 설정한다.

Q. fetch에서는 credentials를 어떻게 설정해?
A. `credentials: "include"`를 사용한다.

Q. HttpOnly Cookie는 localStorage처럼 읽을 수 있어?
A. 아니다. JavaScript에서 직접 읽을 수 없고 브라우저가 요청에 자동 포함한다.

Q. UI는 로그인인데 API는 401이야?
A. 실제 Request Header에 Authorization이 없거나 token이 만료되었을 수 있다.

Q. logout할 때 query cache도 지워야 해?
A. 사용자 민감 데이터가 cache에 남을 수 있으므로 clear 또는 관련 query remove를 고려해야 한다.

Q. refresh 후에도 401이 계속 나?
A. 새 access token 저장, original request header 갱신, interceptor가 최신 token을 읽는지 확인해야 한다.

Q. user state와 token은 같은 거야?
A. 아니다. user state는 UI용 사용자 정보이고 token은 API 인증에 사용하는 값이다.

Q. Route Guard만 있으면 보안이 끝나?
A. 아니다. Route Guard는 UX용이고 실제 보안은 Backend API Auth에서 처리해야 한다.

Q. 버튼을 숨기면 API 호출도 막혀?
A. 아니다. 사용자가 직접 API를 호출할 수 있으므로 Backend 검증이 필요하다.

Q. 403은 Route Guard 문제야 API 권한 문제야?
A. 대부분 Backend API 권한 문제다. Route Guard는 사전에 접근을 줄이는 UX 역할이다.

Q. Frontend 권한 체크는 왜 필요해?
A. 사용자가 불가능한 행동을 시도하지 않도록 UI를 정리하는 데 필요하다.

Q. token을 console.log로 찍어도 돼?
A. 권장하지 않는다. token은 민감정보이므로 로그에 남기지 않아야 한다.

Q. 오류 보고할 때 Authorization Header를 보내야 해?
A. 원문을 보내면 안 된다. Header 존재 여부와 Bearer 형식 여부만 설명하는 것이 좋다.

Q. screenshot에 token이 보이면 문제야?
A. 문제다. token이 노출될 수 있으므로 반드시 가리거나 공유하지 않아야 한다.

Q. 어떤 정보는 공유해도 돼?
A. URL, Method, Status Code, 발생 시각, Header 존재 여부, Response message 정도는 마스킹 후 공유할 수 있다.

Q. CORS 테스트는 Postman으로 가능해?
A. 아니다. CORS는 브라우저 정책이므로 실제 Browser에서 확인해야 한다.

Q. 401 테스트는 어떻게 해?
A. token을 제거하거나 만료 token을 사용해 인증 API를 호출한다.

Q. 403 테스트는 어떻게 해?
A. 권한이 부족한 계정으로 권한이 필요한 API를 호출한다.

Q. 테스트 후 뭘 정리해야 해?
A. localStorage token, cookie, test account state, query cache를 정리해야 한다.

Q. CORS / Auth Error에서 가장 흔한 실수는?
A. Postman 성공을 Browser 성공으로 착각하거나 token 존재를 Authorization Header 전송으로 착각하는 것이다.

Q. OPTIONS 요청이 실패하면 뭘 봐?
A. Backend CORS 설정, allowed methods, allowed headers, SecurityConfig의 OPTIONS 허용 여부를 확인한다.

Q. 401과 403을 같은 메시지로 처리해도 돼?
A. 권장하지 않는다. 401은 로그인 필요, 403은 권한 없음으로 구분하는 것이 좋다.

Q. token을 로그로 찍으면 왜 안 돼?
A. token이 노출되면 계정 탈취나 API 오용 위험이 생길 수 있다.

Q. Part11 CORS and Auth Error Debugging의 목적은 뭐야?
A. Frontend Agent가 CORS, Preflight, Authorization Header, 401, 403, Token Refresh, Cookie Credentials 문제를 구분하고 안전하게 디버깅하게 만드는 것이다.

Q. Part11 다음에는 어떤 문서가 이어지면 좋아?
A. API Testing, Error Handling Architecture, Authentication Frontend Flow, Frontend Build & Deploy API Config 순서로 이어지는 것이 좋다.
