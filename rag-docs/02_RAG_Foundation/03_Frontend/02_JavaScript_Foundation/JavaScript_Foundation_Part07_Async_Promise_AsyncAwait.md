# JavaScript Foundation Part07 - Async JavaScript, Promise, and async await

---

# 1. Async JavaScript

## 1.1 Async JavaScript Concept

### [개념]

Async JavaScript는 시간이 걸리는 작업을 기다리는 동안 전체 코드 실행을 멈추지 않고 처리하는 JavaScript 비동기 처리 방식이다.

Frontend JavaScript에서는 API 요청, 파일 읽기, timer, 사용자 Event, 네트워크 응답 처리에서 비동기 흐름이 자주 발생한다.

예:

```javascript
console.log("start");

setTimeout(() => {
  console.log("async task");
}, 1000);

console.log("end");
```

실행 순서:

```text
start
→ end
→ async task
```

---

### [핵심]

- Async JavaScript
- asynchronous
- synchronous
- non-blocking
- Event Loop
- Callback
- Promise
- async
- await
- Fetch API
- API Request
- loading state
- error state
- execution order

---

### [실무]

2026 실무 기준에서 Frontend Agent는 비동기 흐름을 API 연동과 UI 상태 처리 중심으로 이해해야 한다.

Async JavaScript 실무 사용처:

- Fetch API 요청
- 서버 응답 대기
- 로그인 / 회원가입 요청
- 검색 결과 조회
- 이미지 업로드
- Timer 처리
- Debounce 처리
- Loading UI 표시
- Error UI 표시
- 중복 요청 방지

비동기 UI Flow:

```text
User Action
→ Event Handler
→ Loading State true
→ Async API Request
→ Success or Error
→ UI Update
→ Loading State false
```

주의:

- 비동기 작업은 즉시 결과를 반환하지 않는다.
- API 응답 전 데이터를 사용하면 undefined 오류가 발생할 수 있다.
- loading / error / empty / success 상태를 구분해야 한다.
- async function은 항상 Promise를 반환한다.
- await 누락은 실행 순서 오류를 만들 수 있다.

---

### [FAQ]

Q. Async JavaScript가 뭐야?
A. 시간이 걸리는 작업을 기다리는 동안 전체 코드 실행을 멈추지 않고 처리하는 JavaScript 비동기 방식이다.

Q. Frontend에서 비동기는 어디에 많이 쓰여?
A. API 요청, 사용자 Event 처리, Timer, 파일 업로드, Loading UI 처리에 많이 쓰인다.

Q. 비동기 처리가 어려운 이유는 뭐야?
A. 코드 작성 순서와 실제 완료 순서가 다를 수 있기 때문이다.

Q. API 응답 전 데이터를 쓰면 어떤 문제가 생겨?
A. 데이터가 undefined이거나 비어 있어 화면 오류나 Cannot read properties of undefined 오류가 발생할 수 있다.

---

# 2. Synchronous and Asynchronous

## 2.1 Synchronous Rules

### [개념]

Synchronous는 코드가 작성된 순서대로 하나씩 실행되는 방식이다.

앞 코드가 끝나야 다음 코드가 실행된다.

예:

```javascript
const title = "Festival";

console.log(title);
console.log("done");
```

---

### [핵심]

- Synchronous
- sequential execution
- blocking
- execution order
- simple flow
- immediate result
- JavaScript call stack

---

### [실무]

동기 코드는 실행 흐름이 단순하다.

적합한 작업:

- 변수 계산
- 문자열 처리
- 배열 변환
- 객체 Mapping
- Validation
- UI 상태 계산

예:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}

const isValid = validateKeyword("festival");
```

주의:

- 오래 걸리는 작업을 동기로 처리하면 UI가 멈출 수 있다.
- API 요청은 동기 결과처럼 바로 사용할 수 없다.
- 비동기 함수 결과는 await 또는 then으로 처리해야 한다.

---

### [FAQ]

Q. Synchronous가 뭐야?
A. 코드가 작성된 순서대로 하나씩 실행되는 방식이다.

Q. 동기 코드는 어디에 적합해?
A. Validation, 데이터 변환, UI 상태 계산처럼 즉시 처리 가능한 작업에 적합하다.

Q. 오래 걸리는 작업을 동기로 처리하면 어떻게 돼?
A. Browser UI가 멈추거나 사용자 경험이 나빠질 수 있다.

---

## 2.2 Asynchronous Rules

### [개념]

Asynchronous는 시간이 걸리는 작업을 요청한 뒤, 완료될 때까지 기다리는 동안 다음 코드가 계속 실행될 수 있는 방식이다.

예:

```javascript
console.log("before");

fetch("/api/festivals");

console.log("after");
```

`fetch` 요청은 비동기로 처리되며, 응답이 오기 전에 다음 코드가 실행될 수 있다.

---

### [핵심]

- Asynchronous
- non-blocking
- delayed result
- callback
- Promise
- async await
- API response
- pending state
- execution order

---

### [실무]

비동기 작업은 완료 시점에 맞춰 결과를 처리해야 한다.

비권장:

```javascript
const response = fetch("/api/festivals");

console.log(response.data);
```

권장:

```javascript
const response = await fetch("/api/festivals");
const data = await response.json();

console.log(data);
```

주의:

- Promise 결과는 바로 값이 아니다.
- await 없이 결과를 사용하면 Promise 객체가 나올 수 있다.
- 비동기 결과를 화면에 표시하려면 loading과 error 상태가 필요하다.
- 여러 요청의 완료 순서가 요청 순서와 다를 수 있다.
- 중복 요청과 race condition을 고려해야 한다.

---

### [FAQ]

Q. Asynchronous가 뭐야?
A. 시간이 걸리는 작업을 요청한 뒤 결과를 나중에 처리하는 방식이다.

Q. fetch 결과를 바로 data처럼 쓸 수 있어?
A. 아니다. fetch는 Promise를 반환하므로 await 또는 then으로 처리해야 한다.

Q. 비동기 작업이 완료되기 전에 다음 코드가 실행돼?
A. 그렇다. 그래서 실행 순서와 완료 순서를 구분해야 한다.

---

# 3. Event Loop

## 3.1 Event Loop Concept

### [개념]

Event Loop는 JavaScript가 비동기 작업의 callback 실행 순서를 관리하는 동작 모델이다.

JavaScript는 기본적으로 한 번에 하나의 작업을 실행하지만, Browser가 Timer, Event, Network 같은 비동기 작업을 처리하고 완료된 작업을 Queue에 넣는다.

Event Loop는 Call Stack이 비면 Queue의 작업을 실행한다.

---

### [핵심]

- Event Loop
- Call Stack
- Task Queue
- Microtask Queue
- Callback
- Promise
- Timer
- Browser API
- execution order
- async order

---

### [실무]

Frontend Agent는 Event Loop를 깊은 엔진 수준보다 실행 순서 이해 용도로 다룬다.

기본 Flow:

```text
Call Stack
→ Browser Async API
→ Task Queue or Microtask Queue
→ Event Loop
→ Callback Execution
```

예:

```javascript
console.log("A");

setTimeout(() => {
  console.log("B");
}, 0);

Promise.resolve().then(() => {
  console.log("C");
});

console.log("D");
```

실행 순서:

```text
A
→ D
→ C
→ B
```

주의:

- Promise callback은 일반 timer callback보다 먼저 실행될 수 있다.
- `setTimeout(fn, 0)`도 즉시 실행이 아니다.
- console.log 순서가 작성 순서와 다를 수 있다.
- Event Loop 이해는 async order problem 디버깅에 중요하다.
- 실무 문서에서는 과도한 엔진 내부 설명보다 오류 패턴 중심으로 작성한다.

---

### [FAQ]

Q. Event Loop가 뭐야?
A. JavaScript가 비동기 작업의 callback 실행 순서를 관리하는 동작 모델이다.

Q. setTimeout 0ms는 바로 실행돼?
A. 아니다. 현재 Call Stack이 비고 Queue 순서가 되었을 때 실행된다.

Q. Promise와 setTimeout 중 무엇이 먼저 실행돼?
A. 일반적으로 Promise microtask가 setTimeout task보다 먼저 실행된다.

Q. Event Loop를 왜 알아야 해?
A. 비동기 실행 순서, console.log 순서, API 응답 처리 오류를 이해하는 데 필요하다.

---

# 4. Callback

## 4.1 Callback in Async Rules

### [개념]

Callback은 다른 함수에 전달되어 나중에 실행되는 함수다.

비동기 처리에서는 작업이 끝난 뒤 실행할 로직을 Callback으로 전달할 수 있다.

예:

```javascript
setTimeout(() => {
  console.log("done");
}, 1000);
```

---

### [핵심]

- Callback
- async callback
- later execution
- setTimeout
- Event Handler
- error callback
- callback hell
- execution timing
- nested callback

---

### [실무]

Callback은 Event Handler, Timer, Array Method에서 자주 사용된다.

Timer Callback:

```javascript
setTimeout(() => {
  showMessage("완료되었습니다.");
}, 1000);
```

Event Callback:

```javascript
button.addEventListener("click", () => {
  submitForm();
});
```

주의:

- Callback 실행 시점은 즉시가 아닐 수 있다.
- 중첩 Callback은 가독성을 떨어뜨린다.
- 비동기 에러 처리가 분산될 수 있다.
- API 요청은 Promise 또는 async / await 사용을 권장한다.
- Callback 내부에서 외부 mutable state 참조 시 Closure 문제를 고려한다.

---

### [FAQ]

Q. Callback이 뭐야?
A. 다른 함수에 전달되어 나중에 실행되는 함수다.

Q. 비동기 Callback은 언제 실행돼?
A. Timer 완료, Event 발생, 비동기 작업 완료 같은 시점에 실행된다.

Q. Callback을 많이 중첩하면 왜 안 좋아?
A. 코드 흐름이 복잡해지고 에러 처리가 어려워지기 때문이다.

---

## 4.2 Callback Hell Rules

### [개념]

Callback Hell은 Callback이 여러 단계로 중첩되어 코드 흐름을 읽기 어려워지는 문제다.

예:

```javascript
getUser((user) => {
  getPosts(user.id, (posts) => {
    getComments(posts[0].id, (comments) => {
      console.log(comments);
    });
  });
});
```

---

### [핵심]

- Callback Hell
- nested callback
- readability problem
- error handling problem
- Promise alternative
- async await alternative
- flow flattening

---

### [실무]

Modern JavaScript에서는 Promise와 async / await로 Callback Hell을 줄인다.

개선:

```javascript
async function loadUserComments() {
  const user = await getUser();
  const posts = await getPosts(user.id);
  const comments = await getComments(posts[0].id);

  return comments;
}
```

주의:

- 중첩이 깊어지면 책임 분리가 필요하다.
- 각 비동기 단계의 실패 처리를 명확히 한다.
- 순차 실행이 필요한지 병렬 실행이 가능한지 판단한다.
- 함수 분리와 async / await를 함께 사용한다.

---

### [FAQ]

Q. Callback Hell이 뭐야?
A. Callback이 여러 단계로 중첩되어 코드 흐름을 읽기 어려워지는 문제다.

Q. Callback Hell은 어떻게 줄여?
A. Promise, async / await, 함수 분리를 사용해 흐름을 평평하게 만든다.

Q. 중첩 Callback은 무조건 나빠?
A. 짧은 Event Handler는 괜찮지만, 비동기 단계가 깊어지면 개선이 필요하다.

---

# 5. Promise

## 5.1 Promise Concept

### [개념]

Promise는 비동기 작업의 성공 또는 실패 결과를 나중에 처리하기 위한 JavaScript 객체다.

Promise는 현재 결과가 없더라도 미래의 완료 또는 실패를 표현한다.

상태:

```text
Pending
→ Fulfilled
→ Rejected
```

예:

```javascript
const promise = fetch("/api/festivals");
```

---

### [핵심]

- Promise
- asynchronous result
- pending
- fulfilled
- rejected
- then
- catch
- finally
- chaining
- error handling
- Fetch API
- async await basis

---

### [실무]

Promise는 Fetch API와 async / await의 기반이다.

기본 예:

```javascript
fetch("/api/festivals")
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });
```

주의:

- Promise는 즉시 실제 data가 아니다.
- then은 성공 결과 처리
- catch는 실패 처리
- finally는 성공 / 실패와 관계없이 실행
- Promise chain에서 return 누락 주의
- HTTP 오류는 fetch에서 자동 reject되지 않음
- response.ok 확인 필요

---

### [FAQ]

Q. Promise가 뭐야?
A. 비동기 작업의 완료 또는 실패 결과를 나중에 처리하기 위한 객체다.

Q. Promise 상태는 뭐가 있어?
A. pending, fulfilled, rejected 상태가 있다.

Q. Promise는 바로 결과값이야?
A. 아니다. 미래에 완료될 비동기 결과를 표현하는 객체다.

Q. Promise는 async / await와 관련 있어?
A. 관련 있다. async / await는 Promise 기반 비동기 코드를 읽기 쉽게 작성하는 문법이다.

---

## 5.2 Promise State Rules

### [개념]

Promise State는 Promise의 현재 진행 상태를 의미한다.

상태는 pending, fulfilled, rejected로 구분된다.

- pending: 아직 완료되지 않은 상태
- fulfilled: 성공적으로 완료된 상태
- rejected: 실패한 상태

---

### [핵심]

- Promise State
- pending
- fulfilled
- rejected
- resolved value
- rejection reason
- success handling
- error handling

---

### [실무]

Promise 상태는 직접 바꾸는 것이 아니라 비동기 작업 결과에 따라 결정된다.

예:

```javascript
const request = fetch("/api/festivals");
```

실무 Flow:

```text
API Request
→ Promise pending
→ Response received
→ Promise fulfilled
→ then or await result
```

실패 Flow:

```text
API Request
→ Promise pending
→ Network Error
→ Promise rejected
→ catch or try catch
```

주의:

- Promise가 pending이면 결과를 사용할 수 없다.
- rejected 상태를 처리하지 않으면 unhandled rejection이 발생할 수 있다.
- HTTP 404 / 500은 fetch Promise rejected가 아닐 수 있다.
- 네트워크 오류와 HTTP 오류를 구분해야 한다.

---

### [FAQ]

Q. Promise pending은 뭐야?
A. 비동기 작업이 아직 완료되지 않은 상태다.

Q. Promise fulfilled는 뭐야?
A. 비동기 작업이 성공적으로 완료된 상태다.

Q. Promise rejected는 뭐야?
A. 비동기 작업이 실패한 상태다.

Q. rejected 상태는 어떻게 처리해?
A. catch 또는 async / await의 try / catch로 처리한다.

---

# 6. then catch finally

## 6.1 then Rules

### [개념]

`then`은 Promise가 fulfilled 되었을 때 실행할 callback을 등록하는 메서드다.

예:

```javascript
fetch("/api/festivals").then((response) => {
  return response.json();
});
```

---

### [핵심]

- then
- fulfilled handler
- success callback
- Promise chain
- return value
- response processing
- data handling

---

### [실무]

then chain에서는 다음 then으로 값을 전달하려면 return이 필요하다.

권장:

```javascript
fetch("/api/festivals")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Festival load failed");
    }

    return response.json();
  })
  .then((data) => {
    return data?.content ?? [];
  });
```

주의:

- then callback return 누락 주의
- then chain이 길어지면 async / await로 전환 고려
- response.json()도 Promise를 반환한다.
- fetch HTTP 오류는 response.ok로 직접 확인
- then 내부 throw는 catch로 전달된다.

---

### [FAQ]

Q. then은 뭐야?
A. Promise가 성공했을 때 실행할 callback을 등록하는 메서드다.

Q. then에서 return이 왜 중요해?
A. 다음 then으로 값을 전달하기 위해 필요하다.

Q. response.json()도 Promise야?
A. 맞다. response body를 JSON으로 파싱하는 비동기 작업이다.

---

## 6.2 catch Rules

### [개념]

`catch`는 Promise가 rejected 되었거나 then chain 내부에서 Error가 발생했을 때 실행할 callback을 등록하는 메서드다.

예:

```javascript
fetch("/api/festivals").catch((error) => {
  console.error(error);
});
```

---

### [핵심]

- catch
- rejected handler
- error handling
- network error
- thrown error
- user message
- developer log
- fallback value

---

### [실무]

catch에서는 오류를 무시하지 않는다.

권장:

```javascript
fetch("/api/festivals")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Festival load failed");
    }

    return response.json();
  })
  .catch((error) => {
    console.error("Festival request failed:", error);

    return [];
  });
```

주의:

- 빈 catch 금지
- 사용자 메시지와 개발자 로그 구분
- 민감정보 로그 출력 금지
- fallback 값을 반환할지 다시 throw할지 정책 결정
- catch가 모든 오류를 해결한 것처럼 숨기지 않기
- HTTP 오류는 response.ok 확인 후 throw해야 catch에서 처리 가능

---

### [FAQ]

Q. catch는 뭐야?
A. Promise 실패나 then chain 내부 오류를 처리하는 메서드다.

Q. catch를 비워둬도 돼?
A. 안 된다. 최소한 로그 기록, 사용자 메시지, fallback 처리 중 하나는 해야 한다.

Q. fetch 404는 자동으로 catch로 가?
A. 아니다. response.ok 확인 후 throw해야 catch에서 처리할 수 있다.

---

## 6.3 finally Rules

### [개념]

`finally`는 Promise 성공 또는 실패와 관계없이 마지막에 실행되는 callback을 등록하는 메서드다.

Loading State 해제에 자주 사용한다.

예:

```javascript
fetch("/api/festivals").finally(() => {
  setLoading(false);
});
```

---

### [핵심]

- finally
- always execute
- cleanup
- loading state
- request end
- success or error
- duplicate request prevention

---

### [실무]

finally는 loading 해제, UI 정리, 임시 상태 초기화에 적합하다.

예:

```javascript
setLoading(true);

fetch("/api/festivals")
  .then((response) => response.json())
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    setLoading(false);
  });
```

주의:

- finally는 성공 / 실패 모두 실행된다.
- finally에서 반환한 값은 보통 결과 대체용으로 사용하지 않는다.
- loading false 처리는 finally가 안전하다.
- 정리 작업은 finally에 배치한다.
- 오류 처리는 catch에서 수행한다.

---

### [FAQ]

Q. finally는 뭐야?
A. Promise 성공 또는 실패와 관계없이 마지막에 실행되는 메서드다.

Q. finally는 언제 써?
A. loading 해제, 임시 상태 정리, 중복 요청 방지 상태 초기화에 사용한다.

Q. 오류 처리는 finally에서 해?
A. 아니다. 오류 처리는 catch에서 하고 finally는 정리 작업에 사용한다.

---

# 7. Promise Chaining

## 7.1 Promise Chaining Rules

### [개념]

Promise Chaining은 then, catch, finally를 연결해 비동기 작업의 흐름을 순서대로 처리하는 방식이다.

예:

```javascript
fetch("/api/festivals")
  .then((response) => response.json())
  .then((data) => data.content)
  .catch((error) => console.error(error));
```

---

### [핵심]

- Promise Chaining
- then chain
- return value
- sequential async flow
- error propagation
- catch placement
- readability
- async await alternative

---

### [실무]

Promise Chain은 짧은 비동기 처리에는 사용할 수 있다.

권장:

```javascript
function loadFestivals() {
  return fetch("/api/festivals")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Festival load failed");
      }

      return response.json();
    })
    .then((data) => data?.content ?? [])
    .catch((error) => {
      console.error(error);

      return [];
    });
}
```

주의:

- then에서 return 누락 시 다음 then 값이 undefined가 된다.
- chain이 길어지면 async / await로 전환한다.
- catch 위치에 따라 처리 범위가 달라진다.
- 에러를 삼킬지 다시 throw할지 결정한다.
- Promise chain과 async / await를 불필요하게 섞지 않는다.

---

### [FAQ]

Q. Promise Chaining이 뭐야?
A. then, catch, finally를 연결해 비동기 작업 흐름을 처리하는 방식이다.

Q. then에서 return을 빼면 어떻게 돼?
A. 다음 then으로 undefined가 전달될 수 있다.

Q. Promise Chain이 길어지면 어떻게 해?
A. async / await로 바꿔 가독성을 높이는 것이 좋다.

---

# 8. Promise.all

## 8.1 Promise.all Rules

### [개념]

`Promise.all`은 여러 Promise를 병렬로 실행하고 모든 Promise가 fulfilled 되었을 때 결과 배열을 반환한다.

하나라도 rejected 되면 전체가 rejected 된다.

예:

```javascript
const [festivals, reviews] = await Promise.all([
  fetchFestivals(),
  fetchReviews(),
]);
```

---

### [핵심]

- Promise.all
- parallel execution
- multiple requests
- all fulfilled
- fail fast
- result array
- performance
- independent requests

---

### [실무]

서로 독립적인 API 요청은 Promise.all로 병렬 처리할 수 있다.

예:

```javascript
async function loadPageData() {
  const [festivalResponse, reviewResponse] = await Promise.all([
    fetch("/api/festivals"),
    fetch("/api/reviews"),
  ]);

  const [festivalData, reviewData] = await Promise.all([
    festivalResponse.json(),
    reviewResponse.json(),
  ]);

  return {
    festivals: festivalData?.content ?? [],
    reviews: reviewData?.content ?? [],
  };
}
```

주의:

- 요청 간 의존성이 없을 때 사용한다.
- 하나라도 실패하면 전체가 실패한다.
- 각각의 실패를 따로 처리해야 하면 Promise.allSettled 고려
- 결과 배열 순서는 입력 Promise 배열 순서와 같다.
- 너무 많은 요청을 동시에 보내면 서버와 브라우저에 부담이 될 수 있다.

---

### [FAQ]

Q. Promise.all은 언제 써?
A. 서로 독립적인 여러 비동기 작업을 병렬로 처리할 때 사용한다.

Q. Promise.all에서 하나가 실패하면 어떻게 돼?
A. 전체 Promise가 rejected 된다.

Q. Promise.all 결과 순서는 어떻게 돼?
A. 완료 순서가 아니라 입력 Promise 배열의 순서를 따른다.

Q. 순차 실행이 필요한 작업에도 Promise.all을 써도 돼?
A. 아니다. 이전 결과가 다음 요청에 필요하면 await를 순차적으로 사용해야 한다.

---

## 8.2 Promise.allSettled Rules

### [개념]

`Promise.allSettled`는 여러 Promise가 모두 완료될 때까지 기다리고, 각 Promise의 성공 또는 실패 결과를 모두 반환한다.

하나가 실패해도 전체 결과를 받을 수 있다.

예:

```javascript
const results = await Promise.allSettled([fetchFestivals(), fetchReviews()]);
```

---

### [핵심]

- Promise.allSettled
- all completed
- fulfilled result
- rejected result
- partial failure
- independent result handling
- dashboard data
- resilient UI

---

### [실무]

일부 API 실패를 허용하고 가능한 데이터만 표시해야 할 때 유용하다.

예:

```javascript
async function loadDashboardData() {
  const [festivalResult, reviewResult] = await Promise.allSettled([
    fetchFestivals(),
    fetchReviews(),
  ]);

  return {
    festivals:
      festivalResult.status === "fulfilled" ? festivalResult.value : [],
    reviews: reviewResult.status === "fulfilled" ? reviewResult.value : [],
  };
}
```

주의:

- 각 결과의 status를 확인해야 한다.
- 실패 이유는 reason에 들어있다.
- partial error message를 표시할 수 있다.
- 모든 요청이 성공해야 하는 작업에는 Promise.all이 더 적합할 수 있다.
- 오류를 조용히 무시하지 않는다.

---

### [FAQ]

Q. Promise.allSettled는 언제 써?
A. 여러 요청 중 일부 실패를 허용하고 가능한 결과를 모두 처리해야 할 때 사용한다.

Q. Promise.all과 allSettled 차이는 뭐야?
A. Promise.all은 하나라도 실패하면 전체 실패이고, allSettled는 모든 성공 / 실패 결과를 반환한다.

Q. allSettled 결과에서 무엇을 확인해야 해?
A. 각 결과의 status가 fulfilled인지 rejected인지 확인해야 한다.

---

# 9. async / await

## 9.1 async await Concept

### [개념]

async / await는 Promise 기반 비동기 코드를 동기 코드처럼 읽기 쉽게 작성하는 문법이다.

`async` Function 내부에서 `await`를 사용해 Promise 완료를 기다릴 수 있다.

예:

```javascript
async function fetchFestivals() {
  const response = await fetch("/api/festivals");
  const data = await response.json();

  return data;
}
```

---

### [핵심]

- async
- await
- Promise
- async function
- readable async flow
- try catch
- sequential execution
- parallel execution
- loading state
- error state
- Fetch API

---

### [실무]

Frontend Agent는 API 요청 코드에서 async / await를 기본 형식으로 사용할 수 있다.

권장:

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

- async function은 항상 Promise를 반환한다.
- await는 Promise 완료를 기다린다.
- 일반적으로 await는 async function 내부에서 사용한다.
- try / catch로 실패를 처리한다.
- response.ok 확인을 누락하지 않는다.
- loading / error 상태를 함께 고려한다.

---

### [FAQ]

Q. async / await는 뭐야?
A. Promise 기반 비동기 코드를 동기 코드처럼 읽기 쉽게 작성하는 문법이다.

Q. async function은 뭘 반환해?
A. 항상 Promise를 반환한다.

Q. await는 무엇을 해?
A. Promise가 완료될 때까지 기다렸다가 fulfilled 값을 반환한다.

Q. await는 어디서 쓸 수 있어?
A. 일반적으로 async function 내부에서 사용할 수 있다.

---

## 9.2 async Function Rules

### [개념]

`async function`은 항상 Promise를 반환하는 Function이다.

return 값이 일반 값이어도 Promise로 감싸져 반환된다.

예:

```javascript
async function getName() {
  return "jun";
}

const result = getName();
```

`result`는 `"jun"`이 아니라 Promise다.

---

### [핵심]

- async function
- always returns Promise
- return value wrapping
- await result
- asynchronous API function
- error propagation

---

### [실무]

async function 호출 결과는 await로 받아야 한다.

비권장:

```javascript
const festivals = getFestivals();

console.log(festivals.length);
```

권장:

```javascript
const festivals = await getFestivals();

console.log(festivals.length);
```

Event Handler에서 사용:

```javascript
async function handleSearchSubmit(event) {
  event.preventDefault();

  const festivals = await getFestivals();

  renderFestivals(festivals);
}
```

주의:

- async function 반환값은 Promise다.
- 호출하는 쪽에서 await 또는 then 처리 필요
- async function 내부 throw는 rejected Promise가 된다.
- async event handler에는 try / catch 필요
- Review Agent는 async function 결과를 await 없이 사용하는 코드를 검토해야 한다.

---

### [FAQ]

Q. async function은 항상 Promise를 반환해?
A. 맞다. 일반 값을 return해도 Promise로 감싸져 반환된다.

Q. async function 결과를 바로 배열처럼 쓸 수 있어?
A. 아니다. await로 결과를 받은 뒤 사용해야 한다.

Q. async function 내부에서 throw하면 어떻게 돼?
A. rejected Promise가 된다.

---

## 9.3 await Rules

### [개념]

`await`는 Promise가 완료될 때까지 기다린 뒤 fulfilled 값을 반환한다.

await는 비동기 흐름을 읽기 쉽게 만든다.

예:

```javascript
const response = await fetch("/api/festivals");
```

---

### [핵심]

- await
- wait for Promise
- fulfilled value
- sequential execution
- async function required
- response.json
- error handling
- execution pause

---

### [실무]

await는 API 요청과 JSON parsing에 자주 사용한다.

예:

```javascript
async function loadFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Festival load failed");
  }

  const data = await response.json();

  return data?.content ?? [];
}
```

주의:

- await는 Promise 결과를 기다린다.
- response.json()에도 await 필요
- await를 남용하면 독립 요청도 순차 실행되어 느려질 수 있다.
- 병렬 실행 가능한 요청은 Promise.all 고려
- await 누락은 Promise 객체 사용 오류를 만들 수 있다.

비권장:

```javascript
const data = response.json();

console.log(data.content);
```

권장:

```javascript
const data = await response.json();

console.log(data.content);
```

---

### [FAQ]

Q. await는 뭐야?
A. Promise가 완료될 때까지 기다린 뒤 fulfilled 값을 반환하는 문법이다.

Q. response.json에도 await가 필요해?
A. 필요하다. response.json()도 Promise를 반환한다.

Q. await를 많이 쓰면 항상 좋아?
A. 아니다. 독립적인 요청을 순차 await하면 성능이 떨어질 수 있다.

---

# 10. try catch with async await

## 10.1 try catch Rules

### [개념]

try / catch는 실행 중 발생한 Error를 처리하는 문법이다.

async / await에서는 비동기 오류를 처리하기 위해 try / catch를 사용한다.

예:

```javascript
try {
  const data = await getFestivals();
} catch (error) {
  console.error(error);
}
```

---

### [핵심]

- try
- catch
- async error handling
- await error
- throw
- fallback value
- user message
- developer log
- finally
- loading state

---

### [실무]

API 요청 함수 또는 Event Handler에서 try / catch를 사용한다.

예:

```javascript
async function loadFestivals() {
  try {
    const response = await fetch("/api/festivals");

    if (!response.ok) {
      throw new Error("Festival load failed");
    }

    const data = await response.json();

    return data?.content ?? [];
  } catch (error) {
    console.error("Festival load failed:", error);

    return [];
  }
}
```

Event Handler:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  setLoading(true);

  try {
    const result = await submitForm();
    renderSuccess(result);
  } catch (error) {
    console.error(error);
    showError("요청 처리 중 오류가 발생했습니다.");
  } finally {
    setLoading(false);
  }
}
```

주의:

- catch를 비워두지 않는다.
- 사용자 메시지와 개발자 로그를 구분한다.
- 민감정보 로그 출력 금지
- fallback return과 throw 정책을 명확히 한다.
- loading 해제는 finally에서 처리한다.
- response.ok 확인 누락 금지

---

### [FAQ]

Q. async / await에서 에러 처리는 어떻게 해?
A. try / catch를 사용해 비동기 오류를 처리한다.

Q. catch를 비워둬도 돼?
A. 안 된다. 로그 기록, 사용자 메시지, fallback 처리 중 하나는 해야 한다.

Q. finally는 언제 써?
A. loading 해제나 정리 작업처럼 성공 / 실패와 관계없이 실행해야 하는 작업에 사용한다.

Q. 사용자 메시지와 개발자 로그를 왜 구분해?
A. 사용자는 이해 가능한 안내가 필요하고, 개발자는 원인 분석 정보가 필요하기 때문이다.

---

# 11. Sequential and Parallel Execution

## 11.1 Sequential Execution Rules

### [개념]

Sequential Execution은 비동기 작업을 순서대로 하나씩 기다리며 실행하는 방식이다.

이전 결과가 다음 작업에 필요할 때 사용한다.

예:

```javascript
const user = await fetchUser();
const posts = await fetchPosts(user.id);
```

---

### [핵심]

- Sequential Execution
- ordered async flow
- await one by one
- dependency
- previous result required
- slower but necessary
- API sequence

---

### [실무]

순차 실행은 요청 간 의존성이 있을 때 사용한다.

예:

```javascript
async function loadUserFestivalReviews() {
  const user = await fetchCurrentUser();
  const festivals = await fetchFavoriteFestivals(user.id);
  const reviews = await fetchReviewsByFestivals(
    festivals.map((item) => item.id),
  );

  return reviews;
}
```

주의:

- 이전 결과가 필요하지 않으면 병렬 실행을 고려한다.
- 불필요한 순차 await는 성능 저하를 만든다.
- 각 단계의 실패 처리를 고려한다.
- 중간 데이터가 null일 수 있으면 Guard Clause 사용
- Flow를 명확히 작성한다.

---

### [FAQ]

Q. Sequential Execution은 언제 써?
A. 이전 비동기 작업 결과가 다음 작업에 필요할 때 사용한다.

Q. 순차 await는 단점이 뭐야?
A. 독립적인 작업까지 순서대로 기다리면 전체 시간이 길어진다.

Q. 순차 실행에서 주의할 점은?
A. 중간 결과가 null이거나 실패할 수 있으므로 검증과 에러 처리가 필요하다.

---

## 11.2 Parallel Execution Rules

### [개념]

Parallel Execution은 서로 독립적인 비동기 작업을 동시에 시작하고 함께 기다리는 방식이다.

Promise.all을 사용해 구현할 수 있다.

예:

```javascript
const [festivals, reviews] = await Promise.all([
  fetchFestivals(),
  fetchReviews(),
]);
```

---

### [핵심]

- Parallel Execution
- Promise.all
- independent requests
- performance
- concurrent request
- result order
- fail fast
- dashboard data

---

### [실무]

독립 API 요청은 병렬 실행으로 성능을 개선할 수 있다.

예:

```javascript
async function loadMainPageData() {
  const [bannerData, popularData, nearbyData] = await Promise.all([
    fetchBanners(),
    fetchPopularFestivals(),
    fetchNearbyFestivals(),
  ]);

  return {
    banners: bannerData,
    popularFestivals: popularData,
    nearbyFestivals: nearbyData,
  };
}
```

주의:

- 요청 간 의존성이 없어야 한다.
- 하나라도 실패하면 Promise.all 전체가 실패한다.
- 일부 실패를 허용하려면 Promise.allSettled 고려
- 너무 많은 요청을 동시에 보내지 않는다.
- 결과 순서는 입력 배열 순서와 같다.

---

### [FAQ]

Q. Parallel Execution은 언제 써?
A. 서로 독립적인 비동기 작업을 동시에 처리할 때 사용한다.

Q. 병렬 실행에는 무엇을 써?
A. Promise.all을 주로 사용한다.

Q. 병렬 실행 결과 순서는 완료 순서야?
A. 아니다. Promise 배열에 넣은 입력 순서와 같다.

---

# 12. Loading and Error State

## 12.1 Loading State with Async Rules

### [개념]

Loading State는 비동기 작업 진행 중 여부를 나타내는 상태다.

비동기 요청 중 사용자에게 진행 상태를 보여주고 중복 요청을 방지한다.

예:

```javascript
let loading = false;
```

---

### [핵심]

- loading state
- pending request
- async UI
- duplicate request prevention
- disabled button
- spinner
- finally
- user feedback

---

### [실무]

비동기 요청 Flow:

```text
Before Request
→ loading true
→ await API Request
→ success or error
→ finally
→ loading false
```

예:

```javascript
async function handleSearchSubmit(event) {
  event.preventDefault();

  if (loading) {
    return;
  }

  setLoading(true);

  try {
    const festivals = await searchFestivals(keyword);
    renderFestivals(festivals);
  } catch (error) {
    showError("검색 중 오류가 발생했습니다.");
  } finally {
    setLoading(false);
  }
}
```

주의:

- 요청 시작 전 loading true
- 중복 요청 방지
- 성공 / 실패와 관계없이 loading false
- finally 사용 권장
- loading 중 버튼 disabled
- 화면에 진행 중 상태 표시

---

### [FAQ]

Q. Loading State는 왜 필요해?
A. 비동기 요청 중 사용자에게 진행 상태를 알리고 중복 요청을 막기 위해 필요하다.

Q. loading은 언제 true로 바꿔?
A. API 요청 시작 직전에 true로 바꾼다.

Q. loading은 언제 false로 바꿔?
A. 요청 성공 또는 실패 후 finally에서 false로 바꾸는 것이 안전하다.

Q. loading 중 중복 요청은 어떻게 막아?
A. loading이 true이면 return하거나 버튼을 disabled 처리한다.

---

## 12.2 Error State with Async Rules

### [개념]

Error State는 비동기 작업 실패 상태를 표현하는 UI 상태다.

API 요청 실패, 네트워크 오류, 응답 파싱 실패, 서버 오류 메시지를 사용자에게 안내할 때 사용한다.

---

### [핵심]

- error state
- API error
- network error
- parsing error
- user message
- developer log
- fallback UI
- retry
- error boundary readiness

---

### [실무]

Error State 처리 예:

```javascript
async function loadFestivals() {
  setError(null);
  setLoading(true);

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

- 오류 발생 시 사용자 메시지 표시
- 개발자 로그와 사용자 메시지 구분
- 민감정보 로그 출력 금지
- 재시도 가능 여부 고려
- fallback 값 또는 fallback UI 제공
- HTTP status와 서버 error response 구조 확인

---

### [FAQ]

Q. Error State는 뭐야?
A. 비동기 작업 실패 상태를 사용자에게 표시하기 위한 UI 상태다.

Q. API 오류가 나면 사용자에게 뭘 보여줘야 해?
A. 내부 오류가 아니라 사용자가 이해할 수 있는 짧은 안내 메시지를 보여준다.

Q. 개발자 로그와 사용자 메시지는 왜 구분해?
A. 사용자에게는 안내가 필요하고 개발자에게는 원인 분석 정보가 필요하기 때문이다.

---

# 13. Async Order Problem

## 13.1 Async Order Problem Rules

### [개념]

Async Order Problem은 비동기 작업이 완료되기 전에 데이터를 사용하거나, 여러 비동기 결과의 완료 순서를 잘못 가정해서 발생하는 문제다.

예:

```javascript
const data = fetchFestivals();

console.log(data.content);
```

`fetchFestivals()`가 Promise를 반환하면 `data.content`는 의도대로 동작하지 않는다.

---

### [핵심]

- Async Order Problem
- await missing
- Promise object
- undefined data
- console order
- race condition
- stale data
- loading state
- request order

---

### [실무]

나쁜 예:

```javascript
async function load() {
  const data = fetchFestivals();

  renderFestivals(data);
}
```

좋은 예:

```javascript
async function load() {
  const data = await fetchFestivals();

  renderFestivals(data);
}
```

Debug Flow:

```text
Error Message Check
→ Promise or Actual Data Check
→ await Missing Check
→ Network Response Check
→ Completion Order Check
→ Loading State Check
```

주의:

- async function 호출 결과는 Promise다.
- await 누락 여부 확인
- console.log 순서가 예상과 다를 수 있음
- 빠른 연속 요청은 이전 응답이 나중에 도착할 수 있음
- 최신 요청만 반영해야 하는 UI는 request id 또는 AbortController 고려

---

### [FAQ]

Q. Async Order Problem이 뭐야?
A. 비동기 작업 완료 전에 데이터를 사용하거나 완료 순서를 잘못 가정해 발생하는 문제다.

Q. console.log가 예상보다 먼저 찍히는 이유는?
A. 비동기 작업이 완료되기 전에 다음 코드가 실행되기 때문이다.

Q. async function 결과를 바로 쓰면 왜 Promise가 나와?
A. async function은 항상 Promise를 반환하기 때문이다.

Q. 해결 방법은 뭐야?
A. await 사용, loading state 추가, 요청 완료 후 UI 업데이트를 적용한다.

---

# 14. Race Condition

## 14.1 Race Condition Rules

### [개념]

Race Condition은 여러 비동기 작업의 완료 순서에 따라 결과가 달라지는 문제다.

Frontend에서는 검색어를 빠르게 변경하거나 버튼을 여러 번 클릭할 때 이전 요청이 나중에 도착해 최신 UI를 덮어쓸 수 있다.

---

### [핵심]

- Race Condition
- request order
- response order
- stale response
- latest request only
- duplicate request
- search input
- AbortController
- request id

---

### [실무]

문제 예:

```text
Request A: keyword = "a"
Request B: keyword = "ab"

B response arrives first
→ UI shows "ab"

A response arrives later
→ UI incorrectly shows "a"
```

request id 방식:

```javascript
let latestRequestId = 0;

async function search(keyword) {
  const requestId = latestRequestId + 1;
  latestRequestId = requestId;

  const result = await fetchSearchResult(keyword);

  if (requestId !== latestRequestId) {
    return;
  }

  renderResult(result);
}
```

주의:

- 검색, 자동완성, 필터 변경에서 자주 발생
- 최신 요청만 UI에 반영해야 함
- 중복 submit은 loading으로 차단 가능
- 이전 요청 취소는 AbortController 사용 가능
- Review Agent는 빠른 연속 요청 UI를 검토해야 함

---

### [FAQ]

Q. Race Condition이 뭐야?
A. 여러 비동기 작업의 완료 순서에 따라 결과가 달라지는 문제다.

Q. 검색 UI에서 Race Condition은 어떻게 발생해?
A. 이전 검색 요청이 최신 요청보다 늦게 도착해 최신 결과를 덮어쓸 때 발생한다.

Q. Race Condition은 어떻게 줄여?
A. request id 확인, AbortController, debounce, loading 차단을 사용할 수 있다.

---

# 15. AbortController

## 15.1 AbortController Rules

### [개념]

AbortController는 진행 중인 fetch 요청을 취소할 수 있게 해주는 Browser API다.

검색어 변경, 화면 이동, 최신 요청만 유지해야 하는 상황에서 사용할 수 있다.

예:

```javascript
const controller = new AbortController();

fetch("/api/festivals", {
  signal: controller.signal,
});

controller.abort();
```

---

### [핵심]

- AbortController
- abort
- signal
- fetch cancellation
- stale request
- search request
- cleanup
- race condition
- AbortError

---

### [실무]

검색 요청 취소 예:

```javascript
let searchController = null;

async function searchFestivals(keyword) {
  if (searchController) {
    searchController.abort();
  }

  searchController = new AbortController();

  try {
    const response = await fetch(
      `/api/festivals/search?keyword=${encodeURIComponent(keyword)}`,
      {
        signal: searchController.signal,
      },
    );

    if (!response.ok) {
      throw new Error("Search failed");
    }

    return await response.json();
  } catch (error) {
    if (error.name === "AbortError") {
      return null;
    }

    throw error;
  }
}
```

주의:

- abort된 fetch는 AbortError를 발생시킬 수 있다.
- AbortError는 일반 오류 메시지로 표시하지 않을 수 있다.
- 화면 이동이나 컴포넌트 unmount 시 cleanup에 활용 가능
- 모든 비동기 작업이 AbortController를 지원하는 것은 아니다.
- 복잡한 경우 request id 방식과 함께 고려한다.

---

### [FAQ]

Q. AbortController가 뭐야?
A. 진행 중인 fetch 요청을 취소할 수 있게 해주는 Browser API다.

Q. AbortController는 언제 써?
A. 검색어 변경, 화면 이동, 최신 요청만 유지해야 하는 상황에서 사용한다.

Q. abort된 요청은 어떤 오류가 나?
A. 일반적으로 AbortError가 발생할 수 있다.

Q. AbortError는 사용자에게 오류로 보여줘야 해?
A. 보통 사용자가 취소한 흐름이므로 일반 오류 메시지로 표시하지 않는 경우가 많다.

---

# 16. Debounce

## 16.1 Debounce Rules

### [개념]

Debounce는 연속으로 발생하는 Event를 일정 시간 동안 기다렸다가 마지막 Event만 처리하는 기법이다.

검색 입력, 자동완성, resize Event에서 자주 사용한다.

예:

```text
Input a
Input ab
Input abc
→ wait
→ search abc only
```

---

### [핵심]

- Debounce
- input event
- search
- autocomplete
- delay
- timer
- setTimeout
- clearTimeout
- duplicate request reduction
- API request optimization

---

### [실무]

Debounce 함수 예:

```javascript
function debounce(callback, delay) {
  let timerId = null;

  return function debounced(...args) {
    if (timerId) {
      clearTimeout(timerId);
    }

    timerId = setTimeout(() => {
      callback(...args);
    }, delay);
  };
}
```

검색 입력 적용:

```javascript
const handleSearchInput = debounce((event) => {
  const keyword = event.target.value.trim();

  if (!keyword) {
    return;
  }

  searchFestivals(keyword);
}, 300);
```

주의:

- delay는 UX와 API 요청량을 함께 고려한다.
- 입력값이 비어 있으면 요청하지 않는다.
- Event Object를 비동기적으로 오래 참조하지 말고 필요한 값을 먼저 추출할 수 있다.
- 검색 요청 Race Condition도 함께 고려한다.
- React 전환 시 useMemo, useCallback, useEffect cleanup과 연결된다.

---

### [FAQ]

Q. Debounce가 뭐야?
A. 연속 Event 중 마지막 Event만 일정 시간 후 처리하는 기법이다.

Q. Debounce는 언제 써?
A. 검색 입력, 자동완성, resize처럼 Event가 빠르게 반복될 때 사용한다.

Q. Debounce를 쓰는 이유는 뭐야?
A. 불필요한 API 요청과 과도한 연산을 줄이기 위해서다.

---

# 17. Timer

## 17.1 setTimeout Rules

### [개념]

`setTimeout`은 지정한 시간이 지난 뒤 callback을 한 번 실행하는 Timer API다.

예:

```javascript
setTimeout(() => {
  console.log("done");
}, 1000);
```

---

### [핵심]

- setTimeout
- timer
- delayed execution
- callback
- clearTimeout
- debounce
- async order
- one time execution

---

### [실무]

setTimeout은 안내 메시지 지연, debounce, 임시 UI 표시 등에 사용한다.

예:

```javascript
const timerId = setTimeout(() => {
  hideToast();
}, 3000);
```

Timer 취소:

```javascript
clearTimeout(timerId);
```

주의:

- setTimeout은 정확한 시간 보장을 의미하지 않는다.
- 0ms도 즉시 실행이 아니다.
- 필요 없는 timer는 clearTimeout으로 정리한다.
- 컴포넌트 화면 전환 시 cleanup 필요
- Timer callback에서 오래된 상태 참조 주의

---

### [FAQ]

Q. setTimeout은 뭐야?
A. 지정한 시간이 지난 뒤 callback을 한 번 실행하는 Timer API다.

Q. setTimeout 0ms는 즉시 실행돼?
A. 아니다. 현재 실행 중인 코드가 끝난 뒤 Queue 순서에 따라 실행된다.

Q. setTimeout은 어떻게 취소해?
A. clearTimeout(timerId)로 취소한다.

---

## 17.2 setInterval Rules

### [개념]

`setInterval`은 지정한 시간 간격마다 callback을 반복 실행하는 Timer API다.

예:

```javascript
const intervalId = setInterval(() => {
  checkStatus();
}, 5000);
```

---

### [핵심]

- setInterval
- repeated execution
- polling
- clearInterval
- timer cleanup
- interval delay
- duplicate request caution

---

### [실무]

setInterval은 상태 확인, polling, 시간 표시 갱신에 사용할 수 있다.

예:

```javascript
const intervalId = setInterval(() => {
  refreshNotificationCount();
}, 10000);
```

정리:

```javascript
clearInterval(intervalId);
```

주의:

- clearInterval 누락 시 계속 실행될 수 있다.
- API polling은 서버 부담을 고려한다.
- 이전 요청 완료 전 다음 요청이 시작되지 않게 주의한다.
- 화면 이탈 시 interval 정리 필요
- 실시간 통신은 WebSocket 등 다른 방식이 적합할 수 있다.

---

### [FAQ]

Q. setInterval은 뭐야?
A. 지정한 시간 간격마다 callback을 반복 실행하는 Timer API다.

Q. setInterval은 어떻게 멈춰?
A. clearInterval(intervalId)로 멈춘다.

Q. API polling에 setInterval을 써도 돼?
A. 가능하지만 요청 간격, 중복 요청, 서버 부담을 고려해야 한다.

---

# 18. Async Practical Example

## 18.1 Search API Async Example

### [개념]

Async JavaScript 실무 예제는 Event Handler, Loading State, API Request, Error Handling, Race Condition 방어를 함께 포함해야 한다.

검색 API 예제는 Frontend Agent가 비동기 흐름을 코드로 생성하는 기준이다.

---

### [핵심]

- async function
- await
- fetch
- response.ok
- try catch finally
- loading state
- error state
- request id
- Array.isArray
- render result
- user friendly error

---

### [실무]

예:

```javascript
let loading = false;
let latestRequestId = 0;

function setLoading(nextLoading) {
  loading = nextLoading;
}

function setError(message) {
  const errorElement = document.querySelector(".error-message");

  if (errorElement) {
    errorElement.textContent = message ?? "";
  }
}

function renderFestivals(festivals) {
  const listElement = document.querySelector(".festival-list");

  if (!listElement) {
    return;
  }

  listElement.textContent = "";

  festivals.forEach((festival) => {
    const itemElement = document.createElement("li");

    itemElement.textContent = festival.title ?? "제목 없음";

    listElement.appendChild(itemElement);
  });
}

async function fetchFestivalSearch(keyword) {
  const response = await fetch(
    `/api/festivals/search?keyword=${encodeURIComponent(keyword)}`,
  );

  if (!response.ok) {
    throw new Error("Festival search failed");
  }

  const data = await response.json();

  return Array.isArray(data?.content) ? data.content : [];
}

async function searchFestivals(keyword) {
  const query = keyword.trim();

  if (!query) {
    return;
  }

  const requestId = latestRequestId + 1;
  latestRequestId = requestId;

  setLoading(true);
  setError("");

  try {
    const festivals = await fetchFestivalSearch(query);

    if (requestId !== latestRequestId) {
      return;
    }

    renderFestivals(festivals);
  } catch (error) {
    if (requestId !== latestRequestId) {
      return;
    }

    console.error("Festival search failed:", error);
    setError("검색 중 오류가 발생했습니다.");
  } finally {
    if (requestId === latestRequestId) {
      setLoading(false);
    }
  }
}
```

이 예제의 목적:

- async function 분리
- Fetch API 요청
- response.ok 확인
- JSON parsing
- Array.isArray 방어
- loading 상태 처리
- 사용자 오류 메시지 표시
- request id 기반 Race Condition 방어
- DOM 안전 렌더링
- 민감정보 없는 개발자 로그

---

### [FAQ]

Q. Async Practical Example에서 requestId를 쓰는 이유는?
A. 이전 요청이 나중에 도착해 최신 검색 결과를 덮어쓰는 Race Condition을 막기 위해서다.

Q. finally에서 requestId를 다시 확인하는 이유는?
A. 오래된 요청이 최신 요청의 loading 상태를 잘못 해제하지 않도록 하기 위해서다.

Q. fetchFestivalSearch와 searchFestivals를 나눈 이유는?
A. API 요청 함수와 UI 상태 처리 함수를 분리해 유지보수와 테스트를 쉽게 하기 위해서다.

Q. Array.isArray로 data.content를 확인하는 이유는?
A. 배열이 아닌 값에 forEach나 map을 호출해 발생하는 오류를 방지하기 위해서다.

---

# 19. Async Common Mistakes

## 19.1 Common Mistakes

### [개념]

Async JavaScript 실수는 API 데이터 undefined, Promise 객체 오해, loading 미해제, 중복 요청, 오래된 응답 반영, catch 누락으로 이어질 수 있다.

Review Agent는 await 누락, response.ok 확인, try / catch / finally, Race Condition, loading / error 상태를 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- async function 결과를 await 없이 사용
- Promise를 실제 data로 착각
- response.json() await 누락
- then chain return 누락
- catch 비워두기
- try / catch 누락
- finally 없이 loading 해제 누락
- fetch response.ok 확인 누락
- HTTP 오류와 Network 오류 혼동
- 독립 요청을 불필요하게 순차 await
- 의존 요청을 Promise.all로 병렬 처리
- 빠른 연속 요청 Race Condition 방치
- AbortError를 일반 오류로 표시
- setInterval cleanup 누락
- debounce 없이 입력마다 API 요청
- 민감정보 console.log 출력

---

### [실무]

Review Flow:

```text
Async Review
→ async Function Return Check
→ await Missing Check
→ response.json Await Check
→ response.ok Check
→ try catch Check
→ finally Loading Cleanup Check
→ Promise.all Dependency Check
→ Race Condition Check
→ AbortController Need Check
→ Debounce Need Check
→ Sensitive Log Check
```

나쁜 예:

```javascript
async function load() {
  const response = fetch("/api/festivals");
  const data = response.json();

  render(data.content);
}
```

개선 예:

```javascript
async function load() {
  setLoading(true);

  try {
    const response = await fetch("/api/festivals");

    if (!response.ok) {
      throw new Error("Festival load failed");
    }

    const data = await response.json();
    const festivals = Array.isArray(data?.content) ? data.content : [];

    render(festivals);
  } catch (error) {
    console.error("Festival load failed:", error);
    showError("축제 목록을 불러오지 못했습니다.");
  } finally {
    setLoading(false);
  }
}
```

주의:

- await 누락은 Promise 객체 사용 오류로 이어진다.
- fetch HTTP 오류는 response.ok로 확인한다.
- loading은 finally에서 해제한다.
- 사용자 메시지와 개발자 로그를 구분한다.
- 빠른 입력 검색은 debounce 또는 request cancellation을 고려한다.

---

### [FAQ]

Q. Async JavaScript에서 가장 흔한 실수는 뭐야?
A. await 누락, Promise를 data로 착각, response.ok 확인 누락, catch 누락, loading 해제 누락이다.

Q. response.json await를 빼면 어떻게 돼?
A. 실제 JSON data가 아니라 Promise를 사용하게 되어 오류가 발생할 수 있다.

Q. loading이 계속 true인 이유는 뭐야?
A. 실패 상황에서 loading false 처리가 누락되었거나 finally를 사용하지 않았을 수 있다.

Q. Review Agent는 Async 코드에서 무엇을 우선 확인해야 해?
A. await, response.ok, try / catch / finally, loading 처리, Race Condition, 민감정보 로그를 우선 확인해야 한다.

---

# 20. Async Checklist

## 20.1 Document Quality Checklist

### [개념]

Async JavaScript 문서는 Frontend Agent가 API 요청과 비동기 UI 흐름을 안전하게 구현하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] Async JavaScript 개념이 포함되었는가?
- [ ] Synchronous / Asynchronous 차이가 포함되었는가?
- [ ] Event Loop 기초가 포함되었는가?
- [ ] Callback과 Callback Hell 설명이 포함되었는가?
- [ ] Promise 개념이 포함되었는가?
- [ ] Promise State 설명이 포함되었는가?
- [ ] then / catch / finally 설명이 포함되었는가?
- [ ] Promise Chaining 설명과 return 주의가 포함되었는가?
- [ ] Promise.all 설명이 포함되었는가?
- [ ] Promise.allSettled 설명이 포함되었는가?
- [ ] async / await 설명이 포함되었는가?
- [ ] async function 반환값 규칙이 포함되었는가?
- [ ] await 사용 기준이 포함되었는가?
- [ ] try / catch / finally 비동기 에러 처리가 포함되었는가?
- [ ] Sequential / Parallel Execution 차이가 포함되었는가?
- [ ] Loading State 처리 기준이 포함되었는가?
- [ ] Error State 처리 기준이 포함되었는가?
- [ ] Async Order Problem 설명이 포함되었는가?
- [ ] Race Condition 설명이 포함되었는가?
- [ ] AbortController 설명이 포함되었는가?
- [ ] Debounce 설명이 포함되었는가?
- [ ] Timer 설명이 포함되었는가?
- [ ] 실무형 Async 예제가 포함되었는가?
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
→ Async Flow Check
→ Promise Rule Check
→ async await Rule Check
→ Error Handling Check
→ Loading State Check
→ Race Condition Check
→ Practical Example Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part06_DOM_Event_Form
→ JavaScript_Foundation_Part07_Async_Promise_AsyncAwait
→ JavaScript_Foundation_Part08_Fetch_JSON_API_Response
```

---

### [FAQ]

Q. Async JavaScript 문서 검수에서 가장 중요한 것은 뭐야?
A. await 누락 방지, Promise 처리, response.ok 확인 연결, try / catch / finally, loading / error 상태, Race Condition 방어다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React의 useEffect, Data Fetching, Loading UI, Error UI, Event Handler 비동기 처리의 기반이 된다.

Q. 다음 Part와 어떻게 연결돼?
A. Part07은 비동기 흐름 기준을 만들고, Part08은 Fetch API, JSON, API Response Processing으로 실제 서버 연동을 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. Async JavaScript가 뭐야?
A. 시간이 걸리는 작업을 기다리는 동안 전체 코드 실행을 멈추지 않고 처리하는 JavaScript 비동기 방식이다.

Q. Frontend에서 비동기는 어디에 많이 쓰여?
A. API 요청, 사용자 Event 처리, Timer, 파일 업로드, Loading UI 처리에 많이 쓰인다.

Q. 비동기 처리가 어려운 이유는 뭐야?
A. 코드 작성 순서와 실제 완료 순서가 다를 수 있기 때문이다.

Q. Synchronous가 뭐야?
A. 코드가 작성된 순서대로 하나씩 실행되는 방식이다.

Q. Asynchronous가 뭐야?
A. 시간이 걸리는 작업을 요청한 뒤 결과를 나중에 처리하는 방식이다.

Q. fetch 결과를 바로 data처럼 쓸 수 있어?
A. 아니다. fetch는 Promise를 반환하므로 await 또는 then으로 처리해야 한다.

Q. Event Loop가 뭐야?
A. JavaScript가 비동기 작업의 callback 실행 순서를 관리하는 동작 모델이다.

Q. setTimeout 0ms는 바로 실행돼?
A. 아니다. 현재 Call Stack이 비고 Queue 순서가 되었을 때 실행된다.

Q. Promise와 setTimeout 중 무엇이 먼저 실행돼?
A. 일반적으로 Promise microtask가 setTimeout task보다 먼저 실행된다.

Q. Callback이 뭐야?
A. 다른 함수에 전달되어 나중에 실행되는 함수다.

Q. Callback Hell이 뭐야?
A. Callback이 여러 단계로 중첩되어 코드 흐름을 읽기 어려워지는 문제다.

Q. Callback Hell은 어떻게 줄여?
A. Promise, async / await, 함수 분리를 사용해 흐름을 평평하게 만든다.

Q. Promise가 뭐야?
A. 비동기 작업의 완료 또는 실패 결과를 나중에 처리하기 위한 객체다.

Q. Promise 상태는 뭐가 있어?
A. pending, fulfilled, rejected 상태가 있다.

Q. Promise pending은 뭐야?
A. 비동기 작업이 아직 완료되지 않은 상태다.

Q. Promise fulfilled는 뭐야?
A. 비동기 작업이 성공적으로 완료된 상태다.

Q. Promise rejected는 뭐야?
A. 비동기 작업이 실패한 상태다.

Q. then은 뭐야?
A. Promise가 성공했을 때 실행할 callback을 등록하는 메서드다.

Q. then에서 return이 왜 중요해?
A. 다음 then으로 값을 전달하기 위해 필요하다.

Q. catch는 뭐야?
A. Promise 실패나 then chain 내부 오류를 처리하는 메서드다.

Q. catch를 비워둬도 돼?
A. 안 된다. 로그 기록, 사용자 메시지, fallback 처리 중 하나는 해야 한다.

Q. fetch 404는 자동으로 catch로 가?
A. 아니다. response.ok 확인 후 throw해야 catch에서 처리할 수 있다.

Q. finally는 뭐야?
A. Promise 성공 또는 실패와 관계없이 마지막에 실행되는 메서드다.

Q. finally는 언제 써?
A. loading 해제, 임시 상태 정리, 중복 요청 방지 상태 초기화에 사용한다.

Q. Promise Chaining이 뭐야?
A. then, catch, finally를 연결해 비동기 작업 흐름을 처리하는 방식이다.

Q. then에서 return을 빼면 어떻게 돼?
A. 다음 then으로 undefined가 전달될 수 있다.

Q. Promise.all은 언제 써?
A. 서로 독립적인 여러 비동기 작업을 병렬로 처리할 때 사용한다.

Q. Promise.all에서 하나가 실패하면 어떻게 돼?
A. 전체 Promise가 rejected 된다.

Q. Promise.all 결과 순서는 어떻게 돼?
A. 완료 순서가 아니라 입력 Promise 배열의 순서를 따른다.

Q. Promise.allSettled는 언제 써?
A. 여러 요청 중 일부 실패를 허용하고 가능한 결과를 모두 처리해야 할 때 사용한다.

Q. Promise.all과 allSettled 차이는 뭐야?
A. Promise.all은 하나라도 실패하면 전체 실패이고, allSettled는 모든 성공 / 실패 결과를 반환한다.

Q. async / await는 뭐야?
A. Promise 기반 비동기 코드를 동기 코드처럼 읽기 쉽게 작성하는 문법이다.

Q. async function은 뭘 반환해?
A. 항상 Promise를 반환한다.

Q. await는 무엇을 해?
A. Promise가 완료될 때까지 기다렸다가 fulfilled 값을 반환한다.

Q. await는 어디서 쓸 수 있어?
A. 일반적으로 async function 내부에서 사용할 수 있다.

Q. async function 결과를 바로 배열처럼 쓸 수 있어?
A. 아니다. await로 결과를 받은 뒤 사용해야 한다.

Q. async function 내부에서 throw하면 어떻게 돼?
A. rejected Promise가 된다.

Q. response.json에도 await가 필요해?
A. 필요하다. response.json()도 Promise를 반환한다.

Q. await를 많이 쓰면 항상 좋아?
A. 아니다. 독립적인 요청을 순차 await하면 성능이 떨어질 수 있다.

Q. async / await에서 에러 처리는 어떻게 해?
A. try / catch를 사용해 비동기 오류를 처리한다.

Q. finally는 async / await에서 언제 써?
A. loading 해제나 정리 작업처럼 성공 / 실패와 관계없이 실행해야 하는 작업에 사용한다.

Q. Sequential Execution은 언제 써?
A. 이전 비동기 작업 결과가 다음 작업에 필요할 때 사용한다.

Q. Parallel Execution은 언제 써?
A. 서로 독립적인 비동기 작업을 동시에 처리할 때 사용한다.

Q. 병렬 실행에는 무엇을 써?
A. Promise.all을 주로 사용한다.

Q. Loading State는 왜 필요해?
A. 비동기 요청 중 사용자에게 진행 상태를 알리고 중복 요청을 막기 위해 필요하다.

Q. loading은 언제 true로 바꿔?
A. API 요청 시작 직전에 true로 바꾼다.

Q. loading은 언제 false로 바꿔?
A. 요청 성공 또는 실패 후 finally에서 false로 바꾸는 것이 안전하다.

Q. Error State는 뭐야?
A. 비동기 작업 실패 상태를 사용자에게 표시하기 위한 UI 상태다.

Q. API 오류가 나면 사용자에게 뭘 보여줘야 해?
A. 내부 오류가 아니라 사용자가 이해할 수 있는 짧은 안내 메시지를 보여준다.

Q. Async Order Problem이 뭐야?
A. 비동기 작업 완료 전에 데이터를 사용하거나 완료 순서를 잘못 가정해 발생하는 문제다.

Q. console.log가 예상보다 먼저 찍히는 이유는?
A. 비동기 작업이 완료되기 전에 다음 코드가 실행되기 때문이다.

Q. async function 결과를 바로 쓰면 왜 Promise가 나와?
A. async function은 항상 Promise를 반환하기 때문이다.

Q. Race Condition이 뭐야?
A. 여러 비동기 작업의 완료 순서에 따라 결과가 달라지는 문제다.

Q. 검색 UI에서 Race Condition은 어떻게 발생해?
A. 이전 검색 요청이 최신 요청보다 늦게 도착해 최신 결과를 덮어쓸 때 발생한다.

Q. Race Condition은 어떻게 줄여?
A. request id 확인, AbortController, debounce, loading 차단을 사용할 수 있다.

Q. AbortController가 뭐야?
A. 진행 중인 fetch 요청을 취소할 수 있게 해주는 Browser API다.

Q. AbortController는 언제 써?
A. 검색어 변경, 화면 이동, 최신 요청만 유지해야 하는 상황에서 사용한다.

Q. abort된 요청은 어떤 오류가 나?
A. 일반적으로 AbortError가 발생할 수 있다.

Q. Debounce가 뭐야?
A. 연속 Event 중 마지막 Event만 일정 시간 후 처리하는 기법이다.

Q. Debounce는 언제 써?
A. 검색 입력, 자동완성, resize처럼 Event가 빠르게 반복될 때 사용한다.

Q. Debounce를 쓰는 이유는 뭐야?
A. 불필요한 API 요청과 과도한 연산을 줄이기 위해서다.

Q. setTimeout은 뭐야?
A. 지정한 시간이 지난 뒤 callback을 한 번 실행하는 Timer API다.

Q. setInterval은 뭐야?
A. 지정한 시간 간격마다 callback을 반복 실행하는 Timer API다.

Q. setInterval은 어떻게 멈춰?
A. clearInterval(intervalId)로 멈춘다.

Q. Async JavaScript에서 가장 흔한 실수는 뭐야?
A. await 누락, Promise를 data로 착각, response.ok 확인 누락, catch 누락, loading 해제 누락이다.

Q. response.json await를 빼면 어떻게 돼?
A. 실제 JSON data가 아니라 Promise를 사용하게 되어 오류가 발생할 수 있다.

Q. loading이 계속 true인 이유는 뭐야?
A. 실패 상황에서 loading false 처리가 누락되었거나 finally를 사용하지 않았을 수 있다.

Q. Review Agent는 Async 코드에서 무엇을 우선 확인해야 해?
A. await, response.ok, try / catch / finally, loading 처리, Race Condition, 민감정보 로그를 우선 확인해야 한다.

Q. JavaScript Foundation Part07 다음에는 무엇을 다뤄야 해?
A. Fetch API, JSON, API Response Processing을 다루는 Part08로 이어지는 것이 좋다.
