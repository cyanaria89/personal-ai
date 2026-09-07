# Frontend Testing Part08 - API Mocking

---

# 1. API Mocking Overview

## 1.1 API Mocking Definition

### [개념]

API Mocking은 Frontend 테스트에서 실제 서버를 호출하지 않고 API 응답을 테스트 코드에서 제어하는 방식이다.

Frontend Testing에서 API Mocking은 성공, 실패, 로딩, 빈 데이터, 인증 오류, validation 오류 같은 상황을 안정적으로 재현하기 위해 사용한다.

---

### [핵심]

- API Mocking
- Mock API
- Mock Function
- vi.mock
- jest.mock
- mockResolvedValue
- mockRejectedValue
- Axios Mock
- Fetch Mock
- MSW
- Mock Service Worker
- Success Response
- Error Response
- Empty Response
- Loading State
- Server Validation Error
- Network Error

---

### [실무]

2026 실무 기준에서 Frontend Component Test / Integration Test는 실제 Backend API에 의존하지 않는다.

권장 흐름:

```text
Component render
→ API function mock
→ success / error / empty response 설정
→ user action
→ UI state 검증
```

API Mocking이 필요한 상황:

```text
목록 조회 성공
목록 조회 실패
검색 결과 없음
Form 제출 성공
Form 제출 validation error
401 Unauthorized
403 Forbidden
404 Not Found
500 Server Error
Network Error
요청 중 Loading State
```

실제 API 호출 지양 이유:

```text
서버 상태에 테스트가 의존함
네트워크 상태에 테스트가 의존함
DB 데이터에 테스트가 의존함
테스트 속도가 느려짐
실패 원인이 불명확해짐
```

---

### [FAQ]

Q. API Mocking은 뭐야?
A. 실제 서버를 호출하지 않고 테스트에서 API 응답을 제어하는 방식이다.

Q. Frontend 테스트에서 실제 API를 호출해도 돼?
A. 일반 Component Test와 Integration Test에서는 권장하지 않는다. API 응답은 mock으로 제어한다.

Q. API Mocking이 필요한 이유는 뭐야?
A. 성공, 실패, 로딩, 빈 데이터 같은 상태를 안정적으로 재현하고 테스트를 서버 상태와 분리하기 위해 필요하다.

---

## 1.2 API Mocking Scope

### [개념]

API Mocking Scope는 Frontend 테스트에서 어떤 API 의존성을 mock으로 처리할지 정하는 기준이다.

Component 내부의 API 함수, fetch, axios 요청, server response, network error를 테스트 목적에 맞게 mock 처리한다.

---

### [핵심]

Mock 대상:

- API function
- fetch
- axios instance
- REST endpoint
- server response
- error response
- delay response
- empty response
- auth response
- validation response
- pagination response
- mutation response

Mock 방식:

- API function mock
- axios mock
- fetch mock
- MSW handler
- test server
- fixture response

---

### [실무]

작은 단위 Component Test:

```text
API function mock
→ 간단하고 빠름
→ 특정 함수 응답 제어에 적합
```

Integration style Test:

```text
MSW
→ 실제 HTTP 요청 흐름에 가까움
→ 여러 Component가 같은 API를 공유할 때 적합
```

선택 기준:

```text
API 함수 호출 결과만 제어하면 충분한가?
→ vi.mock / jest.mock

실제 request URL / method / handler 흐름을 검증하고 싶은가?
→ MSW

axios instance interceptor까지 포함하고 싶은가?
→ MSW 또는 axios mock 전략 검토
```

---

### [FAQ]

Q. API function mock과 MSW 중 뭐가 좋아?
A. 작은 단위는 API function mock이 간단하고, 실제 요청 흐름에 가까운 통합 테스트는 MSW가 적합하다.

Q. axios 자체를 mock해야 해?
A. API 함수 레이어가 있다면 보통 API 함수를 mock하는 것이 더 단순하다.

Q. 여러 Component가 같은 API를 호출하면?
A. MSW를 사용하면 실제 endpoint 기준으로 응답을 공유하기 좋다.

---

# 2. API Function Mock Rules

## 2.1 API Function Mock Definition

### [개념]

API Function Mock은 Component가 import해서 사용하는 API 함수를 테스트에서 mock 함수로 대체하는 방식이다.

`vi.mock` 또는 `jest.mock`을 사용해 API 모듈의 함수를 가짜 응답으로 제어한다.

---

### [핵심]

- API function mock
- vi.mock
- jest.mock
- vi.fn
- jest.fn
- mockResolvedValue
- mockRejectedValue
- named export
- default export
- import path match
- mock reset

---

### [실무]

API 함수 예:

```ts
export async function getFestivals() {
  const response = await publicApi.get("/festivals");

  return response.data;
}
```

Vitest mock 예:

```tsx
import { getFestivals } from "../api/festivalApi";

vi.mock("../api/festivalApi", () => ({
  getFestivals: vi.fn(),
}));
```

테스트:

```tsx
test("축제 목록을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- mock 경로와 실제 import 경로 일치
- 테스트마다 mock 초기화
- response shape를 실제 Backend DTO와 맞춤
- success / error / empty case 분리
- UI 결과를 검증

---

### [FAQ]

Q. API Function Mock은 뭐야?
A. Component가 사용하는 API 함수를 테스트에서 가짜 함수로 대체해 응답을 제어하는 방식이다.

Q. vi.mock 경로는 어떻게 써야 해?
A. Component가 실제로 import하는 경로와 일치해야 한다.

Q. mockResolvedValue에는 뭘 넣어?
A. 실제 API 함수가 resolve하는 값과 같은 shape의 mock 데이터를 넣는다.

---

## 2.2 mockResolvedValue Rules

### [개념]

`mockResolvedValue`는 Promise 기반 API 함수가 성공했을 때 반환할 값을 설정하는 mock 방식이다.

API 조회 성공, Form 제출 성공, mutation 성공 상태를 테스트할 때 사용한다.

---

### [핵심]

사용 상황:

- list success
- detail success
- search success
- login success
- create success
- update success
- delete success
- mutation success
- empty success
- pagination success

---

### [실무]

목록 조회 성공:

```tsx
test("축제 목록 조회 성공 시 목록을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
    { festivalId: 2, title: "음악 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
  expect(screen.getByText("음악 축제")).toBeInTheDocument();
});
```

Form 제출 성공:

```tsx
test("리뷰 등록 성공 시 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockResolvedValue({
    reviewId: 1,
    content: "좋았어요",
  });

  render(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

권장:

- 성공 응답 shape를 실제 코드 기준으로 작성
- 비동기 UI는 findBy 사용
- success message / list rendering / redirect 결과 검증
- 단순 API 호출 여부보다 사용자 결과 검증

---

### [FAQ]

Q. mockResolvedValue는 언제 써?
A. API 요청이 성공했을 때의 응답을 테스트에서 제어할 때 사용한다.

Q. 성공 응답 mock은 실제 API와 같아야 해?
A. 가능하면 실제 API 함수가 반환하는 shape와 맞춰야 한다.

Q. 성공 테스트에서 API 함수 호출만 확인하면 돼?
A. 부족할 수 있다. 사용자가 보는 성공 결과까지 검증하는 것이 좋다.

---

## 2.3 mockRejectedValue Rules

### [개념]

`mockRejectedValue`는 Promise 기반 API 함수가 실패했을 때 throw 또는 reject할 error 값을 설정하는 mock 방식이다.

API 실패, validation error, 인증 오류, 서버 오류, 네트워크 오류 테스트에 사용한다.

---

### [핵심]

사용 상황:

- API error
- validation error
- 400 bad request
- 401 unauthorized
- 403 forbidden
- 404 not found
- 409 conflict
- 500 server error
- network error
- timeout
- rejected promise

---

### [실무]

서버 오류 예:

```tsx
test("서버 오류가 발생하면 오류 메시지를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  render(<FestivalListPage />);

  expect(
    await screen.findByText(
      "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
    ),
  ).toBeInTheDocument();
});
```

로그인 실패 예:

```tsx
test("로그인 실패 시 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(login).mockRejectedValue({
    response: {
      status: 401,
      data: {
        message: "Invalid credentials",
      },
    },
  });

  render(<LoginForm />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "wrong-password");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "이메일 또는 비밀번호가 올바르지 않습니다.",
  );
});
```

권장:

- 실제 코드가 참조하는 error shape와 맞춤
- `error.response.status` 사용 여부 확인
- `error.response.data.fieldErrors` 사용 여부 확인
- 서버 내부 메시지 직접 노출 방지
- 실패 후 retry / button enabled 상태 확인 가능

---

### [FAQ]

Q. mockRejectedValue는 언제 써?
A. API 요청 실패나 서버 validation error를 테스트에서 재현할 때 사용한다.

Q. mockRejectedValue 구조는 실제 AxiosError와 같아야 해?
A. 가능하면 실제 코드가 참조하는 `error.response.status`, `error.response.data` 구조와 맞춰야 한다.

Q. error 테스트는 getBy로 확인해도 돼?
A. 비동기 실패 후 표시되는 오류 메시지는 `findBy`를 사용하는 것이 안전하다.

---

## 2.4 Empty Response Mock

### [개념]

Empty Response Mock은 API 요청은 성공했지만 데이터가 없는 상황을 테스트하는 mock이다.

검색 결과 없음, 알림 없음, 리뷰 없음, 찜 목록 없음 같은 Empty State 테스트에 사용한다.

---

### [핵심]

- empty response
- empty array
- null data
- no result
- empty state
- search no result
- no notification
- no review
- no favorite
- success but no data

---

### [실무]

목록 빈 응답:

```tsx
test("축제 목록이 비어 있으면 EmptyState를 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([]);

  render(<FestivalListPage />);

  expect(
    await screen.findByText("표시할 축제가 없습니다."),
  ).toBeInTheDocument();
});
```

검색 결과 없음:

```tsx
test("검색 결과가 없으면 검색 결과 없음 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "없는축제");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("검색 결과가 없습니다.")).toBeInTheDocument();
});
```

권장:

- 성공 응답의 빈 데이터와 error 상태 구분
- empty array / null / undefined 정책 명확화
- EmptyState message 검증
- empty action이 있으면 callback 검증
- loading 중 empty가 먼저 표시되지 않도록 검증 가능

---

### [FAQ]

Q. Empty Response Mock은 뭐야?
A. API 요청은 성공했지만 데이터가 없는 상황을 mock으로 재현하는 것이다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 성공 응답의 빈 데이터이고 Error State는 요청 실패다.

Q. 빈 배열 응답도 테스트해야 해?
A. 중요 화면에서는 해야 한다. 빈 화면 대신 안내 메시지가 표시되는지 확인할 수 있다.

---

# 3. Axios Mock Rules

## 3.1 Axios Error Shape

### [개념]

Axios Error Shape는 axios 요청 실패 시 error 객체가 가지는 구조다.

Frontend 테스트에서 `mockRejectedValue`를 사용할 때 실제 코드가 참조하는 axios error 구조와 mock 구조가 일치해야 한다.

---

### [핵심]

AxiosError 주요 구조:

- error.response
- error.response.status
- error.response.data
- error.response.data.message
- error.response.data.fieldErrors
- error.response.headers
- error.request
- error.message
- network error
- timeout error

---

### [실무]

일반적인 error mock:

```ts
const serverError = {
  response: {
    status: 500,
    data: {
      message: "Internal Server Error",
    },
  },
};
```

field error mock:

```ts
const validationError = {
  response: {
    status: 400,
    data: {
      fieldErrors: {
        email: "이미 사용 중인 이메일입니다.",
      },
    },
  },
};
```

network error mock:

```ts
const networkError = {
  request: {},
  message: "Network Error",
};
```

권장:

- 실제 error handling 코드가 참조하는 key만 mock
- status 기반 분기 테스트
- data.message와 fieldErrors 구분
- network error는 response가 없을 수 있음
- TypeScript에서는 Partial AxiosError factory 사용 가능

---

### [FAQ]

Q. AxiosError mock은 왜 shape가 중요해?
A. 실제 코드가 `error.response.status` 같은 경로를 참조하므로 mock 구조가 다르면 테스트가 실제 오류 처리와 달라진다.

Q. network error에는 response가 있어?
A. 일반적으로 없을 수 있다. response 없이 request 또는 message만 있는 상황을 고려해야 한다.

Q. fieldErrors는 어디에 둬야 해?
A. 프로젝트 error response 규칙에 맞춰 `error.response.data.fieldErrors` 같은 구조로 통일한다.

---

## 3.2 Axios Instance Mock Caution

### [개념]

Axios Instance Mock은 axios instance 자체를 mock하는 방식이다.

API function 레이어가 있는 프로젝트에서는 axios instance보다 API function을 mock하는 방식이 더 단순하고 유지보수에 좋을 수 있다.

---

### [핵심]

주의 대상:

- axios instance mock
- publicApi mock
- authApi mock
- interceptor
- baseURL
- headers
- Authorization
- response unwrap
- import path
- mock adapter
- over mocking

---

### [실무]

API function 레이어가 있는 구조:

```text
Component
→ festivalApi.getFestivals()
→ publicApi.get("/festivals")
```

권장 mock 위치:

```text
Component Test
→ festivalApi.getFestivals mock

API Client Test
→ publicApi / axios instance mock 또는 MSW
```

주의:

```text
Component Test에서 axios instance까지 mock
→ 테스트가 API client 내부 구현에 의존
→ import path mismatch 가능성 증가
→ interceptor 동작과 실제 흐름 차이 발생 가능
```

필요한 경우:

```text
API client 자체를 테스트할 때
interceptor 동작을 검증할 때
Authorization header 추가 로직을 검증할 때
```

---

### [FAQ]

Q. axios instance를 직접 mock해야 해?
A. Component Test에서는 보통 API function을 mock하는 것이 더 단순하다.

Q. axios interceptor 테스트는 어디서 해?
A. API client 또는 integration style test에서 별도로 검증하는 것이 좋다.

Q. axios mock이 적용되지 않으면 뭘 확인해?
A. 실제 import 경로, default/named export, mock 위치, axios instance 참조 경로를 확인한다.

---

# 4. MSW Rules

## 4.1 MSW Definition

### [개념]

MSW(Mock Service Worker)는 실제 네트워크 요청에 가까운 방식으로 API 응답을 mock하는 도구다.

테스트 환경에서는 request handler가 HTTP 요청을 가로채 mock response를 반환한다.

---

### [핵심]

- MSW
- Mock Service Worker
- request handler
- http.get
- http.post
- HttpResponse
- test server
- setupServer
- REST API Mock
- GraphQL Mock
- Integration Style Test
- network-level mock

---

### [실무]

Handler 예:

```ts
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/festivals", () => {
    return HttpResponse.json([{ festivalId: 1, title: "봄꽃 축제" }]);
  }),
];
```

Test server setup 예:

```ts
import { setupServer } from "msw/node";
import { handlers } from "../mocks/handlers";

export const server = setupServer(...handlers);
```

테스트 setup 예:

```ts
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());
```

권장:

- 실제 request URL과 method 기준으로 mock
- 성공 / 실패 / 빈 응답 handler 작성
- 테스트별 override는 server.use 사용
- Backend response shape와 일치
- API function mock보다 실제 요청 흐름에 가까운 테스트에 사용

---

### [FAQ]

Q. MSW는 뭐야?
A. HTTP 요청을 가로채 mock response를 반환하는 API mocking 도구다.

Q. MSW는 언제 써?
A. 여러 Component와 실제 request 흐름에 가까운 Integration Style Test를 작성할 때 유용하다.

Q. MSW와 vi.mock은 뭐가 달라?
A. vi.mock은 함수 자체를 mock하고 MSW는 네트워크 요청 레벨에서 응답을 mock한다.

---

## 4.2 MSW Handler Rules

### [개념]

MSW Handler는 특정 HTTP method와 URL에 대해 어떤 mock response를 반환할지 정의하는 함수다.

Handler는 실제 Backend API endpoint와 response shape를 기준으로 작성한다.

---

### [핵심]

Handler 구성:

- http.get
- http.post
- http.put
- http.patch
- http.delete
- request params
- query params
- request body
- response status
- response json
- delay
- error response

---

### [실무]

GET handler:

```ts
http.get("/api/festivals", () => {
  return HttpResponse.json([{ festivalId: 1, title: "봄꽃 축제" }]);
});
```

POST handler:

```ts
http.post("/api/reviews", async ({ request }) => {
  const body = await request.json();

  return HttpResponse.json(
    {
      reviewId: 1,
      content: body.content,
    },
    { status: 201 },
  );
});
```

Error handler:

```ts
http.get("/api/festivals", () => {
  return HttpResponse.json(
    { message: "Internal Server Error" },
    { status: 500 },
  );
});
```

권장:

- URL / method 정확히 일치
- response status 명시
- request body 필요한 경우 검증 가능
- handler를 도메인별 파일로 분리
- 공통 handler와 테스트별 override 구분

---

### [FAQ]

Q. MSW handler는 어떻게 작성해?
A. HTTP method와 URL을 지정하고 `HttpResponse.json()`으로 mock response를 반환한다.

Q. POST 요청 body도 확인할 수 있어?
A. 가능하다. handler 안에서 `await request.json()`으로 body를 읽을 수 있다.

Q. handler URL이 실제 요청과 다르면 어떻게 돼?
A. 요청이 handler에 매칭되지 않아 테스트가 실패하거나 실제 네트워크 요청처럼 처리될 수 있다.

---

## 4.3 MSW Test Override

### [개념]

MSW Test Override는 기본 handler 대신 특정 테스트에서만 다른 응답을 반환하도록 handler를 재정의하는 방식이다.

`server.use()`를 사용한다.

---

### [핵심]

사용 상황:

- success override
- error override
- empty override
- delay override
- auth error
- validation error
- specific test case
- server.resetHandlers

---

### [실무]

기본 handler가 성공 응답일 때 특정 테스트에서 오류로 변경:

```tsx
test("서버 오류가 발생하면 ErrorState를 표시한다", async () => {
  server.use(
    http.get("/api/festivals", () => {
      return HttpResponse.json(
        { message: "Internal Server Error" },
        { status: 500 },
      );
    }),
  );

  render(<FestivalListPage />);

  expect(
    await screen.findByText("서버 오류가 발생했습니다."),
  ).toBeInTheDocument();
});
```

빈 응답 override:

```tsx
server.use(
  http.get("/api/festivals", () => {
    return HttpResponse.json([]);
  }),
);
```

권장:

- 테스트별 특수 응답은 server.use 사용
- afterEach에서 server.resetHandlers 실행
- override handler는 테스트 의도에 맞게 가까운 위치에 작성
- 기본 handler와 override 충돌 주의

---

### [FAQ]

Q. MSW에서 테스트마다 응답을 다르게 하려면?
A. `server.use()`로 해당 테스트에서만 handler를 override한다.

Q. override handler는 테스트 후 자동으로 사라져?
A. `server.resetHandlers()`를 afterEach에 설정해야 기본 handler로 복구된다.

Q. Empty 응답과 Error 응답을 같은 endpoint로 테스트할 수 있어?
A. 가능하다. 각 테스트에서 server.use로 응답을 다르게 설정한다.

---

## 4.4 MSW vs API Function Mock

### [개념]

MSW와 API Function Mock은 모두 API 응답을 제어하지만 mock 위치가 다르다.

API Function Mock은 함수 레벨 mock이고, MSW는 네트워크 요청 레벨 mock이다.

---

### [핵심]

| 기준                | API Function Mock | MSW                    |
| ------------------- | ----------------- | ---------------------- |
| Mock 위치           | import 함수       | HTTP 요청              |
| 난이도              | 낮음              | 중간                   |
| 속도                | 빠름              | 빠름~중간              |
| 실제 요청 흐름      | 낮음              | 높음                   |
| 여러 Component 공유 | 보통              | 좋음                   |
| endpoint 검증       | 낮음              | 높음                   |
| 추천 상황           | 단일 Component    | Integration Style Test |

---

### [실무]

API Function Mock 적합:

```text
FestivalCard가 찜 API 성공 후 메시지를 표시한다.
LoginForm의 onSubmit 결과를 테스트한다.
작은 단위에서 API 함수 응답만 제어한다.
```

MSW 적합:

```text
FestivalListPage가 실제 get 요청 흐름으로 목록을 표시한다.
LoginPage에서 실제 login endpoint mock과 Auth 흐름을 검증한다.
여러 Component가 같은 endpoint를 공유한다.
```

선택 기준:

```text
테스트가 API 함수 구현에 가까운가?
→ API Function Mock

사용자 흐름과 HTTP 요청 흐름을 함께 보고 싶은가?
→ MSW
```

---

### [FAQ]

Q. API Function Mock과 MSW 중 하나만 써야 해?
A. 아니다. 테스트 목적에 따라 둘 다 사용할 수 있다.

Q. 작은 Component Test에는 뭐가 더 좋아?
A. API Function Mock이 더 단순한 경우가 많다.

Q. Page Integration Test에는 뭐가 더 좋아?
A. 실제 요청 흐름에 가까운 MSW가 적합할 수 있다.

---

# 5. Error Response Mocking

## 5.1 HTTP Status Error Mock

### [개념]

HTTP Status Error Mock은 상태 코드별 오류 응답을 테스트에서 재현하는 방식이다.

401, 403, 404, 409, 500 같은 상태별 UX를 검증할 때 사용한다.

---

### [핵심]

Status별 테스트:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 500 Internal Server Error
- Network Error
- Timeout Error

---

### [실무]

상태 코드별 기대 UI:

```text
400 / 422
→ field error 또는 validation message

401
→ 로그인 필요 메시지 또는 login redirect

403
→ 권한 없음 메시지

404
→ Not Found 메시지

409
→ 중복 / 충돌 메시지

500
→ 서버 오류 fallback message
```

예:

```tsx
test("403 오류이면 권한 없음 메시지를 표시한다", async () => {
  vi.mocked(getAdminData).mockRejectedValue({
    response: {
      status: 403,
    },
  });

  render(<AdminPage />);

  expect(await screen.findByText("접근 권한이 없습니다.")).toBeInTheDocument();
});
```

권장:

- 서비스에서 실제 분기하는 status만 우선 테스트
- 서버 내부 error detail 노출 금지
- status별 ErrorState 문구 구분
- 401은 Auth / Router 테스트와 연결 가능
- network error fallback 별도 테스트

---

### [FAQ]

Q. HTTP status별 error test는 왜 필요해?
A. 상태 코드에 따라 사용자 안내, redirect, retry, 권한 메시지가 달라지기 때문이다.

Q. 모든 status code를 다 테스트해야 해?
A. 아니다. 실제 서비스 코드에서 분기하는 주요 status를 우선 테스트한다.

Q. 500 error는 어떻게 검증해?
A. 서버 내부 상세가 아니라 안전한 fallback message가 표시되는지 확인한다.

---

## 5.2 Server Validation Error Mock

### [개념]

Server Validation Error Mock은 서버가 field 단위 validation 오류를 반환하는 상황을 테스트에서 재현하는 방식이다.

Form 제출 후 중복 이메일, 잘못된 값, 누락된 필드 같은 서버 오류를 검증한다.

---

### [핵심]

- server validation error
- fieldErrors
- 400 error
- 422 error
- duplicate email
- duplicate nickname
- invalid password
- invalid content
- field message
- global message
- AxiosError shape

---

### [실무]

field error mock:

```ts
const validationError = {
  response: {
    status: 400,
    data: {
      fieldErrors: {
        email: "이미 사용 중인 이메일입니다.",
        nickname: "이미 사용 중인 닉네임입니다.",
      },
    },
  },
};
```

테스트:

```tsx
test("서버 validation error를 field error로 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(signup).mockRejectedValue(validationError);

  render(<SignupForm />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("닉네임"), "tester");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "가입하기" }));

  expect(
    await screen.findByText("이미 사용 중인 이메일입니다."),
  ).toBeInTheDocument();
  expect(screen.getByText("이미 사용 중인 닉네임입니다.")).toBeInTheDocument();
});
```

권장:

- Backend error response shape와 일치
- fieldErrors key와 input name 일치 확인
- field error 표시 위치 검증
- global error와 field error 구분
- unknown field error fallback 검토

---

### [FAQ]

Q. Server Validation Error Mock은 뭐야?
A. 서버가 반환한 field validation error를 테스트에서 재현하는 mock이다.

Q. fieldErrors key는 왜 중요해?
A. Frontend가 해당 key를 기준으로 field error를 매핑하기 때문이다.

Q. 서버 validation error를 그대로 표시해도 돼?
A. 정책에 따라 다르지만 사용자 친화적이고 안전한 메시지인지 확인해야 한다.

---

## 5.3 Network Error Mock

### [개념]

Network Error Mock은 서버 응답 자체를 받지 못하는 상황을 테스트에서 재현하는 방식이다.

인터넷 연결 문제, 서버 연결 실패, timeout 같은 상황에 fallback message를 검증한다.

---

### [핵심]

- network error
- timeout
- no response
- error.request
- error.message
- fallback message
- retry button
- offline state
- connection failed

---

### [실무]

API function mock:

```tsx
test("네트워크 오류가 발생하면 fallback 메시지를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    request: {},
    message: "Network Error",
  });

  render(<FestivalListPage />);

  expect(
    await screen.findByText("네트워크 연결을 확인해 주세요."),
  ).toBeInTheDocument();
});
```

MSW network error 개념:

```ts
http.get("/api/festivals", () => {
  return HttpResponse.error();
});
```

권장:

- response가 없는 error 처리 테스트
- retry button 검증
- offline message 검증
- timeout 정책이 있으면 별도 테스트
- network error와 500 error 메시지 구분

---

### [FAQ]

Q. Network Error는 HTTP 500이랑 달라?
A. 다르다. Network Error는 서버 응답을 받지 못한 상황이고 500은 서버가 오류 응답을 반환한 상황이다.

Q. Network Error mock에는 response가 있어?
A. 보통 없을 수 있다. response 없는 error case를 테스트해야 한다.

Q. Network Error UI는 뭘 보여줘야 해?
A. 네트워크 연결 확인, 재시도 버튼 같은 사용자 안내가 적합하다.

---

# 6. Loading and Delay Mocking

## 6.1 Pending Promise Mock

### [개념]

Pending Promise Mock은 API 요청이 끝나지 않은 상태를 만들어 Loading UI를 검증하는 방식이다.

Loading State, submitting state, disabled state 테스트에 사용한다.

---

### [핵심]

- pending promise
- loading state
- submitting state
- disabled button
- spinner
- skeleton
- no resolve
- hang caution
- duplicate submit prevention

---

### [실무]

목록 loading:

```tsx
test("축제 목록을 불러오는 동안 loading 메시지를 표시한다", () => {
  vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

  render(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
});
```

submit loading:

```tsx
test("제출 중에는 버튼을 비활성화한다", async () => {
  const user = userEvent.setup();

  vi.mocked(createReview).mockReturnValue(new Promise(() => {}));

  render(<ReviewForm />);

  await user.click(screen.getByRole("radio", { name: "5점" }));
  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

주의:

```text
pending promise는 resolve되지 않음
→ 테스트 종료 조건을 명확히 해야 함
→ loading UI 확인 후 테스트가 끝나도록 작성
```

---

### [FAQ]

Q. Pending Promise Mock은 언제 써?
A. API 요청 중 loading 상태나 submit 중 disabled 상태를 검증할 때 사용한다.

Q. pending promise 테스트는 위험해?
A. 잘못 작성하면 테스트가 끝나지 않을 수 있다. loading 상태 확인 후 테스트가 종료되도록 작성해야 한다.

Q. loading 테스트에서 findBy를 써야 해?
A. 초기 loading이 즉시 표시되면 getBy를 사용할 수 있다.

---

## 6.2 Delay Response Mock

### [개념]

Delay Response Mock은 API 응답을 지연시켜 loading에서 success 또는 error로 전환되는 흐름을 테스트하는 방식이다.

MSW의 delay 또는 제어 가능한 Promise를 사용할 수 있다.

---

### [핵심]

- delay response
- loading to success
- loading to error
- async transition
- controlled promise
- MSW delay
- fake timer caution
- waitFor
- findBy

---

### [실무]

제어 가능한 Promise 개념:

```ts
function deferred<T>() {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((res) => {
    resolve = res;
  });

  return { promise, resolve };
}
```

테스트:

```tsx
test("loading 후 성공 데이터를 표시한다", async () => {
  const request = deferred<Array<{ festivalId: number; title: string }>>();

  vi.mocked(getFestivals).mockReturnValue(request.promise);

  render(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");

  request.resolve([{ festivalId: 1, title: "봄꽃 축제" }]);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- loading → success 전환 검증
- loading → error 전환 검증
- setTimeout 직접 대기 지양
- fake timer 사용 시 userEvent와 충돌 주의
- findBy로 최종 UI 대기

---

### [FAQ]

Q. Delay Response Mock은 왜 써?
A. loading 상태가 표시된 뒤 success 또는 error UI로 전환되는지 검증하기 위해 사용한다.

Q. setTimeout으로 기다리면 안 돼?
A. 고정 시간 대기는 테스트를 느리고 불안정하게 만들 수 있어 지양한다.

Q. controlled promise는 언제 유용해?
A. 테스트에서 API resolve 시점을 직접 제어하고 싶을 때 유용하다.

---

# 7. Auth API Mocking

## 7.1 Login API Mock

### [개념]

Login API Mock은 로그인 요청 성공 또는 실패 응답을 테스트에서 제어하는 방식이다.

Login Form, Auth State, redirect, global error 테스트에 사용한다.

---

### [핵심]

- login API mock
- accessToken
- refreshToken caution
- user response
- auth state
- login success
- login failure
- 401 unauthorized
- global error
- redirect after login

---

### [실무]

성공 mock:

```tsx
vi.mocked(login).mockResolvedValue({
  accessToken: "test-access-token",
  user: {
    userId: 1,
    email: "test@example.com",
    nickname: "tester",
    role: "ROLE_USER",
  },
});
```

테스트:

```tsx
test("로그인 성공 시 메인 화면으로 이동한다", async () => {
  const user = userEvent.setup();

  vi.mocked(login).mockResolvedValue({
    accessToken: "test-access-token",
    user: {
      userId: 1,
      email: "test@example.com",
      nickname: "tester",
      role: "ROLE_USER",
    },
  });

  renderWithProviders(<LoginPage />, {
    initialEntries: ["/login"],
  });

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(await screen.findByText("로그인되었습니다.")).toBeInTheDocument();
});
```

실패 mock:

```tsx
vi.mocked(login).mockRejectedValue({
  response: {
    status: 401,
  },
});
```

권장:

- 실제 token 사용 금지
- 더미 token 사용
- password는 더미 값 사용
- 성공 시 Auth UI / redirect 결과 검증
- 실패 시 global error 검증
- token 저장 직접 검증보다 사용자 결과 우선

---

### [FAQ]

Q. Login API Mock은 뭘 테스트해?
A. 로그인 성공 응답, 로그인 실패 응답, Auth UI 변화, redirect, 오류 메시지를 테스트한다.

Q. 테스트에 실제 access token을 써도 돼?
A. 안 된다. `test-access-token` 같은 더미 값을 사용한다.

Q. 로그인 실패는 어떤 error로 mock해?
A. 보통 401 Unauthorized 응답을 mock한다.

---

## 7.2 Auth Error Mock

### [개념]

Auth Error Mock은 인증 또는 권한 오류를 테스트에서 재현하는 방식이다.

401 Unauthorized, 403 Forbidden, token 만료, 권한 부족 UI를 검증한다.

---

### [핵심]

- auth error
- 401 Unauthorized
- 403 Forbidden
- token expired
- refresh failed
- login required
- forbidden page
- auth redirect
- role based UI
- protected route

---

### [실무]

401 mock:

```tsx
vi.mocked(getMyPage).mockRejectedValue({
  response: {
    status: 401,
  },
});
```

테스트:

```tsx
test("인증이 만료되면 로그인 필요 메시지를 표시한다", async () => {
  vi.mocked(getMyPage).mockRejectedValue({
    response: {
      status: 401,
    },
  });

  renderWithProviders(<MyPage />, {
    authenticated: true,
  });

  expect(await screen.findByText("로그인이 필요합니다.")).toBeInTheDocument();
});
```

403 mock:

```tsx
vi.mocked(getAdminData).mockRejectedValue({
  response: {
    status: 403,
  },
});
```

권장:

- 401과 403 구분
- 401은 login redirect 또는 login required message
- 403은 forbidden message
- token refresh 실패 정책이 있으면 별도 테스트
- role based UI는 Component / Router Auth Test와 연결

---

### [FAQ]

Q. 401과 403은 어떻게 달라?
A. 401은 인증이 필요하거나 만료된 상태이고, 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Auth Error Mock은 왜 필요해?
A. 인증 만료와 권한 부족 상황에서 사용자에게 올바른 안내를 제공하는지 검증하기 위해 필요하다.

Q. token 만료 테스트에 실제 token이 필요해?
A. 아니다. 상태 코드나 mock error로 재현한다.

---

# 8. Pagination and Search Mocking

## 8.1 Pagination Response Mock

### [개념]

Pagination Response Mock은 page, size, totalElements, hasNext 같은 페이지 응답 구조를 테스트에서 재현하는 방식이다.

Page UI, 더보기, 무한 스크롤, Slice 응답 테스트에 사용한다.

---

### [핵심]

- pagination mock
- page response
- slice response
- content
- page
- size
- totalElements
- totalPages
- hasNext
- nextPage
- load more
- infinite scroll

---

### [실무]

Page response 예:

```ts
const pageResponse = {
  content: [{ festivalId: 1, title: "봄꽃 축제" }],
  page: 0,
  size: 10,
  totalElements: 1,
  totalPages: 1,
};
```

Slice response 예:

```ts
const sliceResponse = {
  content: [{ notificationId: 1, message: "새 알림" }],
  number: 0,
  size: 10,
  hasNext: false,
};
```

테스트:

```tsx
test("다음 페이지가 없으면 더보기 버튼을 표시하지 않는다", async () => {
  vi.mocked(getNotifications).mockResolvedValue({
    content: [{ notificationId: 1, message: "새 알림" }],
    number: 0,
    size: 10,
    hasNext: false,
  });

  render(<NotificationList />);

  expect(await screen.findByText("새 알림")).toBeInTheDocument();
  expect(
    screen.queryByRole("button", { name: "더보기" }),
  ).not.toBeInTheDocument();
});
```

권장:

- Backend pagination shape와 일치
- Page와 Slice 구조 구분
- hasNext true / false 모두 테스트
- load more click 후 추가 응답 테스트
- empty page 테스트

---

### [FAQ]

Q. Pagination Response Mock은 왜 필요해?
A. 목록, 더보기, 무한 스크롤 UI가 페이지 응답에 따라 올바르게 동작하는지 검증하기 위해 필요하다.

Q. Page와 Slice 응답은 달라?
A. 다르다. Page는 totalElements 같은 전체 개수 정보를 포함하고 Slice는 보통 hasNext 중심으로 다음 페이지 여부를 제공한다.

Q. hasNext false는 테스트해야 해?
A. 더보기 버튼 표시 여부에 중요하므로 테스트하는 것이 좋다.

---

## 8.2 Search Response Mock

### [개념]

Search Response Mock은 검색어, 필터, 정렬 조건에 따른 API 응답을 테스트에서 제어하는 방식이다.

검색 결과 표시, 검색 결과 없음, 검색 오류, query param 반영 테스트에 사용한다.

---

### [핵심]

- search mock
- keyword search
- filter search
- query params
- empty result
- search error
- debounced search
- search loading
- reset filter
- sorted result

---

### [실무]

검색 성공:

```tsx
test("검색어로 축제를 검색하면 결과를 표시한다", async () => {
  const user = userEvent.setup();

  vi.mocked(searchFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

검색 결과 없음:

```tsx
vi.mocked(searchFestivals).mockResolvedValue([]);

expect(await screen.findByText("검색 결과가 없습니다.")).toBeInTheDocument();
```

검색 조건 인자 검증:

```tsx
expect(searchFestivals).toHaveBeenCalledWith({
  keyword: "봄꽃",
  region: "seoul",
});
```

권장:

- 검색 성공 / 빈 결과 / 오류 테스트
- 검색 조건이 API 함수에 전달되는지 검증
- 검색 결과 UI 검증
- debounce가 있으면 timer 또는 async 처리 전략 필요
- reset filter 결과 테스트 가능

---

### [FAQ]

Q. Search Response Mock은 뭐야?
A. 검색어와 필터 조건에 따른 API 응답을 테스트에서 제어하는 방식이다.

Q. 검색 조건이 API에 전달되는지도 테스트해야 해?
A. 중요 검색 Form에서는 callback 또는 API 함수 인자 검증이 유용하다.

Q. 검색 결과 없음도 테스트해야 해?
A. 해야 한다. 사용자가 빈 화면 대신 안내 메시지를 볼 수 있어야 한다.

---

# 9. Mock Data Rules

## 9.1 Mock Data Shape Rules

### [개념]

Mock Data Shape는 테스트 mock 데이터가 실제 Backend API 응답 구조와 일치해야 한다는 규칙이다.

Mock shape가 실제와 다르면 테스트는 통과하지만 실제 화면은 실패할 수 있다.

---

### [핵심]

Mock data 기준:

- Backend DTO shape
- field name consistency
- type consistency
- nullable field
- optional field
- enum value
- date string format
- pagination shape
- error response shape
- auth response shape

---

### [실무]

좋은 mock:

```ts
const festivalResponse = {
  festivalId: 1,
  title: "봄꽃 축제",
  regionName: "서울",
  imageUrl: null,
  eventStartDate: "2026-04-01",
  eventEndDate: "2026-04-10",
};
```

나쁜 mock:

```ts
const festivalResponse = {
  id: 1,
  name: "봄꽃 축제",
};
```

문제:

```text
실제 Backend field는 festivalId / title
mock은 id / name
→ 테스트와 실제 API shape 불일치
→ 실제 연동 오류를 놓침
```

권장:

- Backend DTO 기준 mock 작성
- null 가능 field 포함
- enum 값은 실제 값 사용
- date format 실제 API와 일치
- fixture factory 사용 가능

---

### [FAQ]

Q. Mock Data Shape는 왜 중요해?
A. 실제 API와 다른 mock으로 테스트하면 테스트는 통과해도 실제 서비스에서 깨질 수 있기 때문이다.

Q. mock field 이름은 Frontend 편의대로 바꿔도 돼?
A. API response mock은 Backend DTO와 맞추고, View Model 변환은 mapper에서 처리하는 것이 좋다.

Q. null field도 mock에 포함해야 해?
A. 실제로 null이 올 수 있다면 포함해 테스트하는 것이 좋다.

---

## 9.2 Test Data Factory

### [개념]

Test Data Factory는 반복되는 mock 데이터를 생성하는 함수다.

테스트 데이터 중복을 줄이고 기본값을 일관되게 관리할 수 있다.

---

### [핵심]

- test data factory
- fixture factory
- mock builder
- default data
- override
- small fixture
- domain data
- readable test
- avoid over abstraction

---

### [실무]

예:

```ts
function createFestivalResponse(
  override: Partial<FestivalResponse> = {},
): FestivalResponse {
  return {
    festivalId: 1,
    title: "봄꽃 축제",
    regionName: "서울",
    imageUrl: "/festival.png",
    eventStartDate: "2026-04-01",
    eventEndDate: "2026-04-10",
    ...override,
  };
}
```

사용:

```tsx
vi.mocked(getFestival).mockResolvedValue(
  createFestivalResponse({
    title: "음악 축제",
  }),
);
```

권장:

- 도메인별 factory 작성
- 기본값은 정상 케이스
- 테스트별 필요한 field만 override
- 너무 복잡한 factory 지양
- 테스트 의도가 숨겨지지 않게 작성

---

### [FAQ]

Q. Test Data Factory는 언제 써?
A. 같은 도메인 mock 데이터가 여러 테스트에서 반복될 때 사용한다.

Q. factory가 너무 복잡해지면?
A. 테스트 의도를 숨길 수 있으므로 필요한 기본값과 override만 유지한다.

Q. fixture 파일에 큰 데이터를 넣어도 돼?
A. 가능하지만 테스트 가독성을 해치면 작은 데이터로 줄이는 것이 좋다.

---

# 10. Mock Reset Rules

## 10.1 Mock Clear and Reset

### [개념]

Mock Clear and Reset은 테스트 간 mock 호출 기록이나 구현이 섞이지 않도록 초기화하는 작업이다.

API mock은 테스트마다 독립적으로 설정해야 한다.

---

### [핵심]

- vi.clearAllMocks
- vi.resetAllMocks
- jest.clearAllMocks
- jest.resetAllMocks
- mock call history
- mock implementation
- test isolation
- afterEach
- server.resetHandlers
- QueryClient isolation

---

### [실무]

기본 설정:

```ts
afterEach(() => {
  vi.clearAllMocks();
});
```

mock 구현까지 초기화:

```ts
afterEach(() => {
  vi.resetAllMocks();
});
```

MSW:

```ts
afterEach(() => {
  server.resetHandlers();
});
```

구분:

```text
clearAllMocks
→ 호출 기록 초기화

resetAllMocks
→ 호출 기록 + mock implementation 초기화

restoreAllMocks
→ spy 원본 복구
```

권장:

- 테스트마다 mockResolvedValue / mockRejectedValue 명확히 설정
- 이전 테스트의 mock 응답에 의존하지 않음
- MSW handler override 후 resetHandlers 수행
- TanStack Query는 테스트마다 새 QueryClient 생성

---

### [FAQ]

Q. mock clear는 왜 필요해?
A. 이전 테스트의 호출 기록이 다음 테스트에 영향을 주지 않도록 하기 위해 필요하다.

Q. clearAllMocks와 resetAllMocks 차이는 뭐야?
A. clearAllMocks는 호출 기록만 지우고 resetAllMocks는 mock 구현도 초기화한다.

Q. MSW handler도 reset해야 해?
A. 테스트별 override를 사용한다면 afterEach에서 server.resetHandlers를 실행해야 한다.

---

# 11. API Mocking Troubleshooting

## 11.1 Mock Not Working

### [개념]

Mock Not Working은 테스트에서 설정한 mock이 Component의 실제 API 호출에 적용되지 않는 상황이다.

가장 흔한 원인은 import 경로 불일치, default/named export 혼동, mock 위치 오류다.

---

### [핵심]

원인:

- import path mismatch
- vi.mock path mismatch
- default export / named export mismatch
- mock setup order
- actual API called
- axios instance direct call
- MSW handler URL mismatch
- baseURL mismatch
- mock reset timing
- test uses wrong module

---

### [실무]

Debug Flow:

```text
mock 미적용
→ Component의 실제 import 경로 확인
→ vi.mock 경로 확인
→ named/default export 확인
→ API 함수가 mock function인지 확인
→ 실제 네트워크 요청 발생 여부 확인
→ MSW handler URL / method 확인
→ baseURL 포함 여부 확인
```

문제 예:

```tsx
vi.mock("../api/festivalApi", () => ({
  getFestivals: vi.fn(),
}));
```

실제 Component import:

```ts
import { getFestivals } from "@/features/festival/api/festivalApi";
```

경로가 다르면 mock이 적용되지 않을 수 있다.

권장:

- Component import와 mock path 일치
- alias 경로 사용 시 동일 alias 사용
- mock 적용 후 `vi.mocked(getFestivals)` 사용
- 실제 API 호출 로그가 나가는지 확인

---

### [FAQ]

Q. mock을 했는데 실제 API가 호출돼.
A. mock 경로가 실제 import 경로와 다르거나 Component가 다른 API 함수를 사용하고 있을 수 있다.

Q. mockResolvedValue가 적용되지 않아.
A. mock 대상 함수가 실제 호출되는 함수인지, named export와 default export를 혼동하지 않았는지 확인한다.

Q. alias 경로를 쓰면 vi.mock도 alias로 써야 해?
A. 실제 Component가 import하는 경로와 맞추는 것이 안전하다.

---

## 11.2 MSW Handler Not Matching

### [개념]

MSW Handler Not Matching은 Component의 실제 request가 정의된 handler와 매칭되지 않는 상황이다.

URL, method, baseURL, query string, trailing slash 차이를 확인해야 한다.

---

### [핵심]

원인:

- URL mismatch
- method mismatch
- baseURL mismatch
- trailing slash
- query params
- path params
- absolute URL
- relative URL
- handler order
- server.listen 누락
- server reset 문제

---

### [실무]

Debug Flow:

```text
MSW handler 미매칭
→ 실제 요청 URL 확인
→ handler URL 확인
→ HTTP method 확인
→ baseURL 포함 여부 확인
→ query string 처리 확인
→ path parameter 확인
→ server.listen 설정 확인
```

예:

```ts
http.get("/api/festivals", () => {
  return HttpResponse.json([]);
});
```

실제 요청:

```text
http://localhost:8080/api/festivals
```

상황에 따라 absolute URL handler가 필요할 수 있다.

```ts
http.get("http://localhost:8080/api/festivals", () => {
  return HttpResponse.json([]);
});
```

권장:

- 테스트 환경 baseURL 통일
- handler URL과 실제 request URL 일치
- query param은 request.url로 확인
- unhandled request warning 확인
- MSW setup 파일 검증

---

### [FAQ]

Q. MSW handler가 안 잡히면 뭘 확인해?
A. 실제 요청 URL, method, baseURL, trailing slash, query params를 확인한다.

Q. query string까지 handler에 써야 해?
A. 보통 path만 매칭하고 query param은 handler 내부에서 URL로 읽는다.

Q. unhandled request warning은 무시해도 돼?
A. 권장하지 않는다. mock 누락이나 URL 불일치 신호일 수 있다.

---

# 12. API Mocking Security Rules

## 12.1 Mock Data Security

### [개념]

Mock Data Security는 API mock 데이터에 실제 개인정보, token, secret, 운영 URL, 결제 정보가 포함되지 않도록 하는 기준이다.

Frontend 테스트 데이터도 보안 검수 대상이다.

---

### [핵심]

금지 대상:

- real access token
- real refresh token
- real API key
- OAuth secret
- production secret
- personal email
- phone number
- address
- payment card
- real user data
- production URL
- private file content

---

### [실무]

권장:

```ts
const loginResponse = {
  accessToken: "test-access-token",
  user: {
    userId: 1,
    email: "test@example.com",
    nickname: "tester",
    role: "ROLE_USER",
  },
};
```

금지:

```ts
const loginResponse = {
  accessToken: "실제_운영_ACCESS_TOKEN",
  user: {
    email: "real-person-email@example.com",
  },
};
```

권장:

- [test@example.com](mailto:test@example.com) 사용
- test-access-token 사용
- 더미 사용자 데이터 사용
- 운영 API URL mock에 직접 포함 지양
- snapshot에 민감정보 포함 주의

---

### [FAQ]

Q. API mock에 실제 token을 넣어도 돼?
A. 안 된다. 반드시 더미 token을 사용한다.

Q. mock email은 어떻게 써?
A. `test@example.com` 같은 명확한 테스트용 email을 사용한다.

Q. 운영 URL을 테스트 mock에 넣어도 돼?
A. 권장하지 않는다. 테스트 환경 baseURL이나 상대 경로를 사용한다.

---

# 13. API Mocking Anti Pattern

## 13.1 Common API Mocking Anti Patterns

### [개념]

API Mocking Anti Pattern은 테스트가 실제 API 흐름과 다르거나 mock이 불안정해지는 잘못된 작성 방식이다.

Mock은 실제 response shape와 사용자 결과 검증을 중심으로 작성해야 한다.

---

### [핵심]

Anti Pattern:

- 실제 API 호출
- mock path 불일치
- response shape 불일치
- status 없는 error mock
- network error 미고려
- empty response 미테스트
- mock reset 누락
- test 간 mock 공유
- 너무 큰 fixture
- 실제 secret 사용
- API 호출 여부만 검증
- UI 결과 미검증
- MSW handler URL 불일치
- unhandled request 방치

---

### [실무]

나쁜 예:

```tsx
test("API가 호출된다", async () => {
  render(<FestivalListPage />);

  expect(getFestivals).toHaveBeenCalled();
});
```

좋은 예:

```tsx
test("축제 목록 조회 성공 시 축제 제목을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

나쁜 mock:

```ts
mockResolvedValue({ id: 1, name: "축제" });
```

좋은 mock:

```ts
mockResolvedValue({ festivalId: 1, title: "축제" });
```

검수 기준:

```text
실제 API shape와 맞는가?
성공 / 실패 / 빈 상태를 테스트했는가?
사용자 UI 결과를 검증했는가?
mock reset이 되는가?
실제 secret이 없는가?
```

---

### [FAQ]

Q. API Mocking에서 가장 흔한 실수는 뭐야?
A. 실제 API와 다른 response shape를 사용하거나 mock 경로가 실제 import 경로와 다른 경우다.

Q. API 호출 여부만 테스트하면 부족해?
A. 부족하다. API 결과로 사용자에게 보이는 UI를 검증해야 한다.

Q. unhandled request는 무시해도 돼?
A. 권장하지 않는다. mock 누락이나 handler mismatch를 의미할 수 있다.

---

# 14. API Mocking Checklist

## 14.1 API Mocking Checklist

### [개념]

API Mocking Checklist는 API 응답 mock이 실제 API 구조, 테스트 독립성, 사용자 결과 검증 기준을 만족하는지 확인하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] 실제 API 호출을 피했는가?
- [ ] mock 대상이 API function인지 MSW인지 명확한가?
- [ ] mock path가 실제 import path와 일치하는가?
- [ ] success response shape가 실제 API와 일치하는가?
- [ ] error response shape가 실제 error handling 코드와 일치하는가?
- [ ] empty response를 테스트했는가?
- [ ] loading state를 테스트했는가?
- [ ] 주요 HTTP status error를 테스트했는가?
- [ ] network error를 고려했는가?
- [ ] server validation fieldErrors를 테스트했는가?
- [ ] pagination / slice response shape를 맞췄는가?
- [ ] 테스트마다 mock을 clear / reset 하는가?
- [ ] MSW handler override 후 resetHandlers를 수행하는가?
- [ ] 사용자 UI 결과를 검증했는가?
- [ ] 실제 token / secret / 개인정보를 사용하지 않았는가?
```

---

### [실무]

Agent API Mocking Flow:

```text
Identify API Dependency
→ Choose API Function Mock or MSW
→ Create Realistic Mock Response
→ Set Success / Empty / Error Case
→ Render Component
→ Trigger User Action if Needed
→ Wait Async UI with findBy
→ Assert User-visible Result
→ Reset Mock
→ Check Security Data
```

예:

```text
Festival Search Page
→ searchFestivals mock
→ success response
→ empty response
→ 500 error response
→ loading state
→ user searches keyword
→ result / empty / error UI 검증
```

---

### [FAQ]

Q. API Mocking Checklist의 핵심은 뭐야?
A. 실제 API shape와 맞는 mock을 사용하고 사용자 UI 결과를 검증하는 것이다.

Q. API Mocking 작성 전 무엇을 정해야 해?
A. mock 방식, response shape, success/empty/error case, error handling 구조를 정해야 한다.

Q. API Mocking 테스트가 불안정하면 뭘 확인해?
A. mock path, mock reset, async findBy, response shape, MSW handler URL을 확인한다.

---

# 15. Part08 Summary

## 15.1 API Mocking Final Rule

### [개념]

Frontend Testing Part08은 API Mocking의 기준, API function mock, MSW, error response, loading mock, auth mock, pagination mock, mock data 관리 기준을 정의한다.

이 Part의 목적은 Agent가 실제 서버에 의존하지 않고 API 상태를 안정적으로 재현하며 사용자 UI 결과를 검증하게 만드는 것이다.

---

### [핵심]

최종 기준:

- 실제 API 호출 금지
- API Function Mock과 MSW를 목적에 맞게 선택
- mockResolvedValue로 성공 응답 제어
- mockRejectedValue로 실패 응답 제어
- Empty Response Mock으로 EmptyState 검증
- AxiosError shape를 실제 코드와 일치
- MSW handler는 실제 URL / method와 일치
- server.use로 테스트별 응답 override
- HTTP status별 error UX 검증
- Network Error와 Server Error 구분
- Pending Promise로 Loading State 검증
- Auth API mock은 더미 token 사용
- Pagination / Search response shape 일치
- mock data는 Backend DTO와 일치
- 테스트마다 mock reset
- 실제 secret / 개인정보 사용 금지

---

### [실무]

Agent 작업 Flow:

```text
API-dependent Test Request
→ Identify API Layer
→ Choose Mock Strategy
→ Prepare Realistic Mock Data
→ Mock Success / Empty / Error / Loading
→ Render Component with Providers
→ Trigger User Flow
→ Assert Loading / Success / Empty / Error UI
→ Reset Mock State
→ Review Security and Anti Pattern
```

Part09 이후 연결:

```text
Part08 API Mocking
→ Part09 Loading Error Empty
→ Part10 Router Auth Testing
→ Part11 TanStack Query Testing
→ Part12 Accessibility Testing
→ Part13 Snapshot Test Caution
```

---

### [FAQ]

Q. Part08의 최종 목적은 뭐야?
A. Frontend Agent가 실제 서버 없이 API 성공, 실패, 로딩, 빈 상태를 안정적으로 테스트하게 만드는 것이다.

Q. API Mocking에서 가장 중요한 규칙은 뭐야?
A. 실제 API shape와 맞는 mock을 사용하고 사용자에게 보이는 결과를 검증하는 것이다.

Q. Part08 다음에는 어떤 내용이 이어져야 해?
A. Loading, Error, Empty, Success 상태 UI를 구체적으로 검증하는 상태 테스트 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. API Mocking은 뭐야?
A. 실제 서버를 호출하지 않고 테스트에서 API 응답을 제어하는 방식이다.

Q. Frontend 테스트에서 실제 API를 호출해도 돼?
A. 일반 Component Test와 Integration Test에서는 권장하지 않는다. API 응답은 mock으로 제어한다.

Q. API Mocking이 필요한 이유는 뭐야?
A. 성공, 실패, 로딩, 빈 데이터 같은 상태를 안정적으로 재현하고 테스트를 서버 상태와 분리하기 위해 필요하다.

Q. API function mock과 MSW 중 뭐가 좋아?
A. 작은 단위는 API function mock이 간단하고, 실제 요청 흐름에 가까운 통합 테스트는 MSW가 적합하다.

Q. axios 자체를 mock해야 해?
A. API 함수 레이어가 있다면 보통 API 함수를 mock하는 것이 더 단순하다.

Q. API Function Mock은 뭐야?
A. Component가 사용하는 API 함수를 테스트에서 가짜 함수로 대체해 응답을 제어하는 방식이다.

Q. vi.mock 경로는 어떻게 써야 해?
A. Component가 실제로 import하는 경로와 일치해야 한다.

Q. mockResolvedValue는 언제 써?
A. API 요청이 성공했을 때의 응답을 테스트에서 제어할 때 사용한다.

Q. mockResolvedValue에는 뭘 넣어?
A. 실제 API 함수가 resolve하는 값과 같은 shape의 mock 데이터를 넣는다.

Q. mockRejectedValue는 언제 써?
A. API 요청 실패나 서버 validation error를 테스트에서 재현할 때 사용한다.

Q. mockRejectedValue 구조는 실제 AxiosError와 같아야 해?
A. 가능하면 실제 코드가 참조하는 `error.response.status`, `error.response.data` 구조와 맞춰야 한다.

Q. error 테스트는 getBy로 확인해도 돼?
A. 비동기 실패 후 표시되는 오류 메시지는 `findBy`를 사용하는 것이 안전하다.

Q. Empty Response Mock은 뭐야?
A. API 요청은 성공했지만 데이터가 없는 상황을 mock으로 재현하는 것이다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 성공 응답의 빈 데이터이고 Error State는 요청 실패다.

Q. AxiosError mock은 왜 shape가 중요해?
A. 실제 코드가 `error.response.status` 같은 경로를 참조하므로 mock 구조가 다르면 테스트가 실제 오류 처리와 달라진다.

Q. network error에는 response가 있어?
A. 일반적으로 없을 수 있다. response 없는 error case를 테스트해야 한다.

Q. axios instance를 직접 mock해야 해?
A. Component Test에서는 보통 API function을 mock하는 것이 더 단순하다.

Q. axios interceptor 테스트는 어디서 해?
A. API client 또는 integration style test에서 별도로 검증하는 것이 좋다.

Q. MSW는 뭐야?
A. HTTP 요청을 가로채 mock response를 반환하는 API mocking 도구다.

Q. MSW는 언제 써?
A. 여러 Component와 실제 request 흐름에 가까운 Integration Style Test를 작성할 때 유용하다.

Q. MSW와 vi.mock은 뭐가 달라?
A. vi.mock은 함수 자체를 mock하고 MSW는 네트워크 요청 레벨에서 응답을 mock한다.

Q. MSW handler는 어떻게 작성해?
A. HTTP method와 URL을 지정하고 `HttpResponse.json()`으로 mock response를 반환한다.

Q. POST 요청 body도 확인할 수 있어?
A. 가능하다. handler 안에서 `await request.json()`으로 body를 읽을 수 있다.

Q. MSW에서 테스트마다 응답을 다르게 하려면?
A. `server.use()`로 해당 테스트에서만 handler를 override한다.

Q. override handler는 테스트 후 자동으로 사라져?
A. `server.resetHandlers()`를 afterEach에 설정해야 기본 handler로 복구된다.

Q. API Function Mock과 MSW 중 하나만 써야 해?
A. 아니다. 테스트 목적에 따라 둘 다 사용할 수 있다.

Q. 작은 Component Test에는 뭐가 더 좋아?
A. API Function Mock이 더 단순한 경우가 많다.

Q. Page Integration Test에는 뭐가 더 좋아?
A. 실제 요청 흐름에 가까운 MSW가 적합할 수 있다.

Q. HTTP status별 error test는 왜 필요해?
A. 상태 코드에 따라 사용자 안내, redirect, retry, 권한 메시지가 달라지기 때문이다.

Q. 모든 status code를 다 테스트해야 해?
A. 아니다. 실제 서비스 코드에서 분기하는 주요 status를 우선 테스트한다.

Q. 500 error는 어떻게 검증해?
A. 서버 내부 상세가 아니라 안전한 fallback message가 표시되는지 확인한다.

Q. Server Validation Error Mock은 뭐야?
A. 서버가 반환한 field validation error를 테스트에서 재현하는 mock이다.

Q. fieldErrors key는 왜 중요해?
A. Frontend가 해당 key를 기준으로 field error를 매핑하기 때문이다.

Q. Network Error는 HTTP 500이랑 달라?
A. 다르다. Network Error는 서버 응답을 받지 못한 상황이고 500은 서버가 오류 응답을 반환한 상황이다.

Q. Network Error mock에는 response가 있어?
A. 보통 없을 수 있다. response 없는 error case를 테스트해야 한다.

Q. Pending Promise Mock은 언제 써?
A. API 요청 중 loading 상태나 submit 중 disabled 상태를 검증할 때 사용한다.

Q. pending promise 테스트는 위험해?
A. 잘못 작성하면 테스트가 끝나지 않을 수 있다. loading 상태 확인 후 테스트가 종료되도록 작성해야 한다.

Q. Delay Response Mock은 왜 써?
A. loading 상태가 표시된 뒤 success 또는 error UI로 전환되는지 검증하기 위해 사용한다.

Q. setTimeout으로 기다리면 안 돼?
A. 고정 시간 대기는 테스트를 느리고 불안정하게 만들 수 있어 지양한다.

Q. Login API Mock은 뭘 테스트해?
A. 로그인 성공 응답, 로그인 실패 응답, Auth UI 변화, redirect, 오류 메시지를 테스트한다.

Q. 테스트에 실제 access token을 써도 돼?
A. 안 된다. `test-access-token` 같은 더미 값을 사용한다.

Q. 401과 403은 어떻게 달라?
A. 401은 인증이 필요하거나 만료된 상태이고, 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Pagination Response Mock은 왜 필요해?
A. 목록, 더보기, 무한 스크롤 UI가 페이지 응답에 따라 올바르게 동작하는지 검증하기 위해 필요하다.

Q. Page와 Slice 응답은 달라?
A. 다르다. Page는 totalElements 같은 전체 개수 정보를 포함하고 Slice는 보통 hasNext 중심으로 다음 페이지 여부를 제공한다.

Q. Search Response Mock은 뭐야?
A. 검색어와 필터 조건에 따른 API 응답을 테스트에서 제어하는 방식이다.

Q. 검색 결과 없음도 테스트해야 해?
A. 해야 한다. 사용자가 빈 화면 대신 안내 메시지를 볼 수 있어야 한다.

Q. Mock Data Shape는 왜 중요해?
A. 실제 API와 다른 mock으로 테스트하면 테스트는 통과해도 실제 서비스에서 깨질 수 있기 때문이다.

Q. mock field 이름은 Frontend 편의대로 바꿔도 돼?
A. API response mock은 Backend DTO와 맞추고, View Model 변환은 mapper에서 처리하는 것이 좋다.

Q. Test Data Factory는 언제 써?
A. 같은 도메인 mock 데이터가 여러 테스트에서 반복될 때 사용한다.

Q. mock clear는 왜 필요해?
A. 이전 테스트의 호출 기록이 다음 테스트에 영향을 주지 않도록 하기 위해 필요하다.

Q. clearAllMocks와 resetAllMocks 차이는 뭐야?
A. clearAllMocks는 호출 기록만 지우고 resetAllMocks는 mock 구현도 초기화한다.

Q. mock을 했는데 실제 API가 호출돼.
A. mock 경로가 실제 import 경로와 다르거나 Component가 다른 API 함수를 사용하고 있을 수 있다.

Q. MSW handler가 안 잡히면 뭘 확인해?
A. 실제 요청 URL, method, baseURL, trailing slash, query params를 확인한다.

Q. API mock에 실제 token을 넣어도 돼?
A. 안 된다. 반드시 더미 token을 사용한다.

Q. API Mocking에서 가장 흔한 실수는 뭐야?
A. 실제 API와 다른 response shape를 사용하거나 mock 경로가 실제 import 경로와 다른 경우다.

Q. API 호출 여부만 테스트하면 부족해?
A. 부족하다. API 결과로 사용자에게 보이는 UI를 검증해야 한다.

Q. API Mocking Checklist의 핵심은 뭐야?
A. 실제 API shape와 맞는 mock을 사용하고 사용자 UI 결과를 검증하는 것이다.

Q. Part08 API Mocking의 최종 목표는 뭐야?
A. Frontend Agent가 실제 서버 없이 API 성공, 실패, 로딩, 빈 상태를 안정적으로 테스트하게 만드는 것이다.
