# JavaScript Foundation Part04 - Function, Scope, and Closure

---

# 1. Function

## 1.1 Function Concept

### [개념]

Function은 재사용 가능한 코드 블록이다.

JavaScript Function은 입력값을 받아 처리하고 결과를 반환하거나, 특정 동작을 수행한다.

Frontend JavaScript에서는 Function을 UI Logic, Event Handling, API Request, Data Processing, Form Validation에 사용한다.

예:

```javascript
function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}
```

---

### [핵심]

- Function
- Function Declaration
- Function Expression
- Arrow Function
- Parameter
- Argument
- Return
- Default Parameter
- Callback Function
- Pure Function
- UI Logic
- API Logic
- Data Processing
- Event Handler

---

### [실무]

2026 실무 기준에서 Function은 단순 문법 단위가 아니라 Frontend Logic을 역할별로 분리하는 기본 단위다.

Function 작성 기준:

- 하나의 Function은 하나의 책임
- 입력과 출력 명확화
- 의미 있는 함수명 사용
- UI Logic과 Data Processing 분리
- API Request Function 분리
- Form Validation Function 분리
- 복잡한 조건식 Function 분리
- Side Effect 최소화
- 테스트 가능한 형태로 작성

권장:

```javascript
function isActiveFestival(festival) {
  return festival.status === "ACTIVE";
}

function getFestivalTitle(festival) {
  return festival?.title ?? "제목 없음";
}
```

비권장:

```javascript
function doSomething(data) {
  console.log(data);
  fetch("/api/festivals");
  document.querySelector(".title").textContent = data.title;
}
```

Frontend Agent는 Function을 통해 코드 검색성, 재사용성, Review 가능성을 높여야 한다.

---

### [FAQ]

Q. Function이 뭐야?
A. 재사용 가능한 JavaScript 코드 블록이다.

Q. Function은 왜 분리해?
A. 반복 로직을 줄이고, 테스트와 유지보수를 쉽게 하기 위해 분리한다.

Q. Frontend에서 Function은 어디에 사용돼?
A. UI 상태 계산, 이벤트 처리, API 요청, 응답 데이터 가공, Form Validation에 사용된다.

Q. 좋은 Function의 기준은 뭐야?
A. 하나의 책임을 가지고, 입력과 출력이 명확하며, 이름만 봐도 목적을 알 수 있는 Function이다.

---

# 2. Function Declaration

## 2.1 Function Declaration Rules

### [개념]

Function Declaration은 `function` 키워드로 이름 있는 함수를 선언하는 방식이다.

예:

```javascript
function formatDate(dateText) {
  return new Date(dateText).toLocaleDateString("ko-KR");
}
```

Function Declaration은 hoisting 대상이므로 선언 위치보다 위에서 호출할 수 있다.

---

### [핵심]

- Function Declaration
- named function
- hoisting
- reusable logic
- function name
- parameter
- return
- declaration before use recommended

---

### [실무]

Function Declaration은 명확한 이름을 가진 재사용 로직에 적합하다.

권장 예:

```javascript
function normalizeKeyword(keyword) {
  return keyword.trim();
}

function isValidKeyword(keyword) {
  return normalizeKeyword(keyword).length > 0;
}
```

API Response Mapping:

```javascript
function normalizeFestivalResponse(response) {
  return response?.data?.content ?? [];
}
```

주의:

- hoisting에 의존해 선언 전 호출하는 방식은 지양
- Function 이름은 동사 또는 동사구로 작성
- 함수 내부 책임을 과도하게 늘리지 않기
- API 호출, DOM 조작, 데이터 가공을 한 함수에 섞지 않기
- Review Agent는 함수명과 실제 동작이 일치하는지 확인

권장 흐름:

```text
Input
→ Validate
→ Process
→ Return
```

---

### [FAQ]

Q. Function Declaration이 뭐야?
A. `function` 키워드로 이름 있는 함수를 선언하는 방식이다.

Q. Function Declaration은 hoisting돼?
A. 된다. 하지만 실무에서는 선언 위치를 명확히 두고 사용하는 것이 좋다.

Q. Function 이름은 어떻게 지어야 해?
A. `formatDate`, `isValidKeyword`, `normalizeResponse`처럼 목적이 드러나는 이름이 좋다.

Q. Function Declaration은 언제 적합해?
A. 재사용되는 명확한 로직이나 유틸성 함수에 적합하다.

---

# 3. Function Expression

## 3.1 Function Expression Rules

### [개념]

Function Expression은 함수를 값처럼 변수에 할당하는 방식이다.

예:

```javascript
const formatDate = function (dateText) {
  return new Date(dateText).toLocaleDateString("ko-KR");
};
```

Function Expression은 변수 선언 방식에 따라 hoisting 동작이 달라진다.

---

### [핵심]

- Function Expression
- anonymous function
- named function expression
- variable assignment
- const function
- callback
- hoisting caution
- function as value

---

### [실무]

Function Expression은 함수를 값으로 다루거나 callback으로 전달할 때 사용할 수 있다.

예:

```javascript
const isActiveFestival = function (festival) {
  return festival.status === "ACTIVE";
};
```

하지만 짧은 callback이나 간단한 함수 표현은 Arrow Function을 더 자주 사용한다.

```javascript
const isActiveFestival = (festival) => festival.status === "ACTIVE";
```

주의:

- `const`에 할당한 Function Expression은 초기화 전 사용할 수 없음
- anonymous function은 stack trace에서 추적성이 낮을 수 있음
- 함수 이름이 필요하면 Function Declaration 또는 named function expression 고려
- Review Agent는 선언 전 사용 여부를 확인해야 함

비권장:

```javascript
console.log(formatTitle("Festival"));

const formatTitle = function (title) {
  return title.trim();
};
```

권장:

```javascript
const formatTitle = function (title) {
  return title.trim();
};

console.log(formatTitle("Festival"));
```

---

### [FAQ]

Q. Function Expression이 뭐야?
A. 함수를 변수에 값처럼 할당하는 방식이다.

Q. Function Expression은 선언 전에 사용할 수 있어?
A. `const`나 `let`에 할당한 경우 초기화 전 사용할 수 없다.

Q. Function Expression과 Function Declaration 차이는?
A. Function Declaration은 이름 있는 함수 선언이고 hoisting되며, Function Expression은 함수를 변수에 할당하는 방식이다.

Q. Function Expression은 언제 써?
A. 함수를 값처럼 다루거나 callback으로 전달할 때 사용할 수 있다.

---

# 4. Arrow Function

## 4.1 Arrow Function Rules

### [개념]

Arrow Function은 짧은 함수 표현식 문법이다.

예:

```javascript
const getTitle = (festival) => festival.title;
```

Arrow Function은 callback, Array Method, 간단한 로직 표현에 자주 사용된다.

---

### [핵심]

- Arrow Function
- =>
- short syntax
- callback
- lexical this
- no own this
- array method
- implicit return
- explicit return
- hoisting caution

---

### [실무]

Arrow Function은 배열 메서드와 자주 함께 사용한다.

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
const festivalTitles = activeFestivals.map((festival) => festival.title);
```

객체 반환 시 괄호 필요:

```javascript
const festivalCards = festivals.map((festival) => ({
  id: festival.id,
  title: festival.title,
}));
```

여러 줄 로직은 명시적 return 사용:

```javascript
const getDisplayTitle = (festival) => {
  const title = festival?.title?.trim();

  return title || "제목 없음";
};
```

주의:

- Arrow Function은 자체 `this`를 가지지 않는다.
- 객체 method에서 `this`가 필요하면 부적합할 수 있다.
- `const`에 할당한 Arrow Function은 초기화 전 사용할 수 없다.
- 복잡한 로직은 Function Declaration으로 분리할 수 있다.
- callback 내부 return 누락에 주의한다.

---

### [FAQ]

Q. Arrow Function이 뭐야?
A. `=>` 문법을 사용하는 짧은 함수 표현식이다.

Q. Arrow Function은 언제 써?
A. 짧은 callback, Array Method, 간단한 함수 표현에 자주 사용한다.

Q. Arrow Function은 항상 좋은 거야?
A. 아니다. callback에는 편리하지만 `this`가 필요한 객체 method에서는 주의해야 한다.

Q. Arrow Function은 hoisting돼?
A. `const`나 `let`에 할당한 Arrow Function은 변수 초기화 전 사용할 수 없다.

---

## 4.2 Arrow Function and this

### [개념]

Arrow Function은 자체 `this`를 가지지 않고 외부 Scope의 `this`를 사용한다.

이를 lexical this라고 한다.

예:

```javascript
const user = {
  name: "jun",
  sayName: () => {
    console.log(this.name);
  },
};
```

위 예제에서 `this.name`은 의도한 `user.name`을 가리키지 않을 수 있다.

---

### [핵심]

- lexical this
- this binding
- object method caution
- callback this
- event handler caution
- function declaration alternative
- method syntax

---

### [실무]

객체 method에서 `this`가 필요하면 일반 method syntax를 사용한다.

비권장:

```javascript
const user = {
  name: "jun",
  sayName: () => {
    return this.name;
  },
};
```

권장:

```javascript
const user = {
  name: "jun",
  sayName() {
    return this.name;
  },
};
```

Event Handler에서 Arrow Function은 외부 변수를 유지하는 데 자주 사용된다.

```javascript
button.addEventListener("click", () => {
  console.log("clicked");
});
```

주의:

- 객체 method에서 `this`가 필요하면 Arrow Function 지양
- class method, event handler, callback의 `this` 동작 구분 필요
- React Function Component에서는 `this` 사용 빈도가 낮음
- Review Agent는 Arrow Function 내부 `this` 사용을 검토해야 함

---

### [FAQ]

Q. Arrow Function의 this는 어떻게 동작해?
A. 자체 this를 만들지 않고 외부 Scope의 this를 사용한다.

Q. 객체 method에 Arrow Function을 써도 돼?
A. this가 필요 없다면 가능하지만, this가 필요하면 일반 method syntax가 적합하다.

Q. lexical this가 뭐야?
A. 함수가 선언된 외부 Scope의 this를 그대로 사용하는 동작이다.

Q. Review Agent는 Arrow Function에서 무엇을 봐야 해?
A. Arrow Function 내부에서 this를 사용하는지, 해당 this가 의도한 대상인지 확인해야 한다.

---

# 5. Parameter and Argument

## 5.1 Parameter and Argument Rules

### [개념]

Parameter는 Function 정의 시 받는 입력 이름이다.

Argument는 Function 호출 시 실제로 전달하는 값이다.

예:

```javascript
function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}

formatPrice(10000);
```

`price`는 Parameter이고, `10000`은 Argument다.

---

### [핵심]

- Parameter
- Argument
- input value
- function call
- default parameter
- validation
- object parameter
- destructuring parameter
- optional value

---

### [실무]

Function의 Parameter는 의미가 명확해야 한다.

권장:

```javascript
function getFestivalDetailUrl(festivalId) {
  return `/festivals/${festivalId}`;
}
```

비권장:

```javascript
function getUrl(id) {
  return `/festivals/${id}`;
}
```

여러 값을 받을 때는 object parameter를 고려한다.

```javascript
function createSearchParams({ keyword, regionCode, page }) {
  return {
    keyword: keyword?.trim() ?? "",
    regionCode,
    page: page ?? 1,
  };
}
```

주의:

- Parameter 개수가 많으면 object parameter 사용 고려
- optional parameter는 기본값 처리
- Function 내부에서 Argument 타입 검증 필요
- API 요청 함수는 필요한 값만 Parameter로 받기
- Review Agent는 Parameter 과다와 의미 없는 이름을 검토해야 함

---

### [FAQ]

Q. Parameter와 Argument 차이는 뭐야?
A. Parameter는 함수 정의의 입력 이름이고, Argument는 함수 호출 시 전달하는 실제 값이다.

Q. Parameter가 많으면 어떻게 해?
A. object parameter로 묶어 의미를 명확하게 만드는 것이 좋다.

Q. Optional Parameter는 어떻게 처리해?
A. default parameter나 nullish coalescing으로 기본값을 지정한다.

Q. Parameter 이름은 어떻게 지어야 해?
A. 함수 내부에서 어떤 값인지 명확히 알 수 있도록 구체적으로 작성한다.

---

# 6. Return

## 6.1 Return Rules

### [개념]

`return`은 Function 실행 결과를 호출한 곳으로 반환하고 Function을 종료한다.

예:

```javascript
function isEmptyList(items) {
  return items.length === 0;
}
```

return이 없으면 Function은 `undefined`를 반환한다.

---

### [핵심]

- return
- return value
- undefined return
- early return
- guard clause
- function output
- predictable result
- pure function

---

### [실무]

Function은 반환값이 명확해야 한다.

권장:

```javascript
function normalizeFestivals(response) {
  return response?.data?.content ?? [];
}
```

Guard Clause:

```javascript
function getDisplayName(user) {
  if (!user) {
    return "Guest";
  }

  return user.name;
}
```

비권장:

```javascript
function normalizeFestivals(response) {
  if (response.data) {
    response.data.content;
  }
}
```

주의:

- return 누락 시 `undefined` 반환
- map callback에서 return 누락 주의
- early return으로 흐름 단순화
- 반환 타입 일관성 유지
- 실패 시 fallback 값 반환 여부 명확히 결정
- API 함수에서 throw와 fallback return 정책 구분

반환 타입 일관성 예:

```javascript
function getItems(response) {
  const items = response?.data?.content;

  if (!Array.isArray(items)) {
    return [];
  }

  return items;
}
```

---

### [FAQ]

Q. return은 뭐야?
A. Function 실행 결과를 호출한 곳으로 돌려주고 Function을 종료하는 문법이다.

Q. return이 없으면 무엇을 반환해?
A. `undefined`를 반환한다.

Q. map callback에서 return을 빼먹으면 어떻게 돼?
A. 새 배열 요소가 undefined가 될 수 있다.

Q. 반환 타입을 일관되게 해야 하는 이유는?
A. 호출하는 쪽에서 결과를 예측하고 안전하게 사용할 수 있기 때문이다.

---

# 7. Default Parameter

## 7.1 Default Parameter Rules

### [개념]

Default Parameter는 Argument가 전달되지 않거나 `undefined`일 때 사용할 기본값을 지정하는 문법이다.

예:

```javascript
function getPageSize(size = 20) {
  return size;
}
```

---

### [핵심]

- Default Parameter
- default value
- undefined
- optional argument
- fallback
- function input safety
- pagination
- search condition

---

### [실무]

Default Parameter는 optional argument가 있는 함수에서 유용하다.

Pagination 예:

```javascript
function createPageRequest(page = 1, size = 20) {
  return {
    page,
    size,
  };
}
```

검색 조건 예:

```javascript
function normalizeKeyword(keyword = "") {
  return keyword.trim();
}
```

주의:

- Default Parameter는 `undefined`일 때 적용
- `null`이 전달되면 기본값이 적용되지 않음
- `0`, `false`, `""`가 유효한 값인지 확인
- optional value가 null일 수 있으면 `??`와 함께 처리
- Parameter 기본값이 복잡하면 함수 내부에서 명확히 처리

예:

```javascript
function normalizePage(page) {
  return page ?? 1;
}
```

---

### [FAQ]

Q. Default Parameter가 뭐야?
A. Argument가 없거나 undefined일 때 사용할 기본값을 지정하는 문법이다.

Q. null이 전달되면 Default Parameter가 적용돼?
A. 아니다. Default Parameter는 undefined일 때 적용된다.

Q. Default Parameter는 언제 써?
A. 검색어, 페이지 번호, 페이지 크기처럼 optional argument가 있는 함수에 사용한다.

Q. null도 기본값 처리하려면 어떻게 해?
A. 함수 내부에서 nullish coalescing `??`를 사용한다.

---

# 8. Callback Function

## 8.1 Callback Function Rules

### [개념]

Callback Function은 다른 함수에 Argument로 전달되어 나중에 실행되는 Function이다.

Array Method, Event Handling, Promise 처리에서 자주 사용된다.

예:

```javascript
const titles = festivals.map((festival) => festival.title);
```

`(festival) => festival.title`은 `map`에 전달된 Callback Function이다.

---

### [핵심]

- Callback Function
- function as argument
- Array Method
- Event Handler
- Promise then
- async callback caution
- return value
- execution timing

---

### [실무]

Frontend에서 Callback Function은 매우 자주 사용된다.

Array Method Callback:

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
```

Event Handler Callback:

```javascript
button.addEventListener("click", () => {
  console.log("clicked");
});
```

Promise Callback:

```javascript
fetch("/api/festivals")
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });
```

주의:

- callback 실행 시점 이해 필요
- map callback은 return 필요
- forEach callback 반환값은 사용되지 않음
- callback 내부 this 주의
- async callback 사용 시 Promise 처리 주의
- callback이 길어지면 별도 Function으로 분리

비권장:

```javascript
const titles = festivals.map((festival) => {
  festival.title;
});
```

권장:

```javascript
const titles = festivals.map((festival) => festival.title);
```

---

### [FAQ]

Q. Callback Function이 뭐야?
A. 다른 함수에 인자로 전달되어 나중에 실행되는 함수다.

Q. Callback은 어디에 많이 쓰여?
A. Array Method, Event Handler, Promise 처리에서 많이 사용된다.

Q. map callback에서 return이 필요한 이유는?
A. map은 callback 반환값으로 새 배열을 만들기 때문이다.

Q. callback이 길어지면 어떻게 해?
A. 별도 이름 있는 Function으로 분리하는 것이 좋다.

---

# 9. Pure Function

## 9.1 Pure Function Rules

### [개념]

Pure Function은 같은 입력에 대해 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 Function이다.

예:

```javascript
function addVat(price) {
  return price * 1.1;
}
```

---

### [핵심]

- Pure Function
- same input same output
- no side effect
- predictable
- testable
- data processing
- UI state calculation
- Review friendly

---

### [실무]

Frontend 데이터 가공과 UI 상태 계산은 Pure Function으로 작성하는 것이 좋다.

예:

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

API 응답 가공:

```javascript
function toFestivalCard(festival) {
  return {
    id: festival.id,
    title: festival.title,
    imageUrl: festival.imageUrl ?? "/default.png",
  };
}
```

장점:

- 테스트 쉬움
- 결과 예측 가능
- Review 용이
- React State 계산과 잘 맞음
- Side Effect 분리 가능

주의:

- DOM 조작, API 호출, console.log는 Side Effect다.
- Pure Function 내부에서 외부 변수를 변경하지 않는다.
- API 호출 Function과 Data Mapping Function을 분리한다.

---

### [FAQ]

Q. Pure Function이 뭐야?
A. 같은 입력에 대해 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Q. Pure Function은 왜 좋아?
A. 테스트, 리뷰, 디버깅이 쉽고 결과를 예측하기 쉽다.

Q. API 호출 함수는 Pure Function이야?
A. 아니다. 네트워크 요청은 Side Effect이므로 Pure Function이 아니다.

Q. Frontend에서 Pure Function은 어디에 적합해?
A. UI 상태 계산, Form Validation, API Response Mapping, 데이터 변환에 적합하다.

---

# 10. Side Effect

## 10.1 Side Effect Rules

### [개념]

Side Effect는 Function이 반환값 외부에 영향을 주는 동작이다.

예:

- DOM 조작
- API 요청
- console.log
- localStorage 변경
- 전역 변수 변경
- 외부 배열 또는 객체 변경

---

### [핵심]

- Side Effect
- DOM manipulation
- API request
- console.log
- localStorage
- external state mutation
- event handling
- separation
- predictability

---

### [실무]

Frontend에서는 Side Effect와 Pure Logic을 분리해야 한다.

비권장:

```javascript
async function searchAndRender(keyword) {
  const response = await fetch(`/api/festivals?keyword=${keyword}`);
  const data = await response.json();

  document.querySelector(".list").innerHTML = data.content;
}
```

권장:

```javascript
async function fetchFestivals(keyword) {
  const response = await fetch(
    `/api/festivals?keyword=${encodeURIComponent(keyword)}`,
  );

  if (!response.ok) {
    throw new Error("Festival search failed");
  }

  return await response.json();
}

function normalizeFestivals(response) {
  return response?.content ?? [];
}
```

분리 기준:

```text
API Request
→ Response
→ Data Mapping
→ UI Update
```

주의:

- Side Effect가 많으면 테스트와 디버깅이 어려움
- API 호출과 데이터 변환을 분리
- DOM 직접 조작은 React 전환 시 최소화
- 민감정보 console.log 금지
- localStorage 접근은 별도 함수로 분리

---

### [FAQ]

Q. Side Effect가 뭐야?
A. Function이 반환값 외부에 영향을 주는 동작이다.

Q. console.log도 Side Effect야?
A. 맞다. 외부 출력에 영향을 주기 때문에 Side Effect다.

Q. Side Effect를 왜 분리해야 해?
A. 테스트, 디버깅, 코드 리뷰가 쉬워지고 로직 예측 가능성이 높아지기 때문이다.

Q. API 호출과 데이터 가공을 한 함수에 넣어도 돼?
A. 가능하지만 유지보수와 테스트를 위해 분리하는 것이 좋다.

---

# 11. Scope

## 11.1 Scope Concept

### [개념]

Scope는 변수와 Function에 접근할 수 있는 범위다.

JavaScript Scope는 변수 접근 가능 여부와 생명주기를 결정한다.

주요 Scope:

- Global Scope
- Function Scope
- Block Scope
- Lexical Scope

---

### [핵심]

- Scope
- Global Scope
- Function Scope
- Block Scope
- Lexical Scope
- variable access
- variable lifetime
- const
- let
- var
- closure

---

### [실무]

Frontend 코드에서는 Scope를 좁게 유지해야 한다.

권장:

```javascript
function getDisplayTitle(festival) {
  const title = festival?.title ?? "제목 없음";

  return title;
}
```

비권장:

```javascript
let title = "";

function getDisplayTitle(festival) {
  title = festival.title;

  return title;
}
```

Scope 관리 기준:

- 필요한 위치에서 변수 선언
- 전역 변수 최소화
- 함수 내부 변수 우선
- block 내부에서만 쓰는 값은 block 내부 선언
- Event Handler 외부에 불필요한 mutable 상태 두지 않기
- API 응답 데이터는 필요한 Function Scope 안에서 처리

Review Agent는 넓은 Scope의 mutable variable과 불필요한 전역 변수를 검출해야 한다.

---

### [FAQ]

Q. Scope가 뭐야?
A. 변수와 함수에 접근할 수 있는 범위다.

Q. Scope를 좁게 유지하는 이유는?
A. 변수 충돌과 의도하지 않은 값 변경을 줄이기 위해서다.

Q. 전역 변수는 왜 줄여야 해?
A. 여러 함수에서 값이 변경될 수 있어 오류 추적이 어려워지기 때문이다.

Q. Frontend에서 Scope 관리는 왜 중요해?
A. Event Handler, API 응답 처리, React State 전환에서 값 참조 오류를 줄이기 위해 중요하다.

---

# 12. Global Scope

## 12.1 Global Scope Rules

### [개념]

Global Scope는 코드 어디에서나 접근 가능한 최상위 Scope다.

Browser 환경에서 전역 변수는 window 객체와 연결될 수 있다.

예:

```javascript
const appName = "FestaPick";
```

---

### [핵심]

- Global Scope
- global variable
- window
- namespace pollution
- collision
- mutable global state
- avoid global variable
- browser environment

---

### [실무]

Frontend JavaScript에서는 Global Scope 사용을 최소화해야 한다.

비권장:

```javascript
let currentUser = null;
let selectedFestival = null;
let loading = false;
```

권장:

```javascript
function createSearchState() {
  return {
    keyword: "",
    page: 1,
    loading: false,
  };
}
```

주의:

- 전역 변수는 어디서든 변경될 수 있음
- 변수명 충돌 가능
- 테스트와 디버깅 어려움
- Browser 전역 객체 오염 가능
- React 전환 시 전역 mutable state는 상태 관리 문제로 이어짐
- 설정 상수는 별도 constants 파일로 분리 가능

상수 분리 예:

```javascript
export const DEFAULT_PAGE_SIZE = 20;
export const DEFAULT_IMAGE_URL = "/default.png";
```

---

### [FAQ]

Q. Global Scope가 뭐야?
A. 코드 어디에서나 접근 가능한 최상위 Scope다.

Q. 전역 변수는 왜 위험해?
A. 여러 위치에서 변경될 수 있어 값 흐름을 추적하기 어렵고 이름 충돌이 발생할 수 있다.

Q. 모든 전역 값을 없애야 해?
A. 설정 상수처럼 변경되지 않는 값은 별도 constants 파일로 관리할 수 있다.

Q. Browser에서 전역 변수는 어디와 연결될 수 있어?
A. 전역 변수는 window 객체와 연결될 수 있다.

---

# 13. Function Scope

## 13.1 Function Scope Rules

### [개념]

Function Scope는 Function 내부에서 선언된 변수가 해당 Function 안에서만 접근 가능한 범위다.

`var`는 block이 아니라 Function Scope를 가진다.

예:

```javascript
function getMessage() {
  const message = "Hello";

  return message;
}
```

---

### [핵심]

- Function Scope
- local variable
- var function scope
- function boundary
- variable lifetime
- internal logic
- access limitation

---

### [실무]

Function 내부 변수는 Function 밖에서 접근할 수 없으므로 로직을 안전하게 캡슐화할 수 있다.

권장:

```javascript
function normalizeKeyword(keyword) {
  const query = keyword.trim();

  return query;
}
```

주의:

`var`는 block scope가 아니라 Function Scope다.

```javascript
function getMessage(isLoggedIn) {
  if (isLoggedIn) {
    var message = "환영합니다.";
  }

  return message;
}
```

위 코드는 `if` block 밖에서도 `message` 접근이 가능하다.

권장:

```javascript
function getMessage(isLoggedIn) {
  if (!isLoggedIn) {
    return "로그인이 필요합니다.";
  }

  return "환영합니다.";
}
```

Review Agent는 `var`로 인한 Function Scope 혼동을 검토해야 한다.

---

### [FAQ]

Q. Function Scope가 뭐야?
A. Function 내부에서 선언된 변수가 해당 Function 안에서만 유효한 범위다.

Q. var는 Function Scope야?
A. 맞다. var는 block scope가 아니라 function scope를 가진다.

Q. Function Scope는 왜 유용해?
A. 변수 접근 범위를 제한해 의도하지 않은 변경을 줄일 수 있다.

Q. Function 내부 변수는 밖에서 접근할 수 있어?
A. 일반적으로 접근할 수 없다.

---

# 14. Block Scope

## 14.1 Block Scope Rules

### [개념]

Block Scope는 `{}` block 내부에서 선언된 변수가 해당 block 안에서만 유효한 범위다.

`const`와 `let`은 block scope를 가진다.

예:

```javascript
if (isLoggedIn) {
  const message = "환영합니다.";
  console.log(message);
}
```

---

### [핵심]

- Block Scope
- const
- let
- if block
- for block
- limited access
- safer variable
- var caution

---

### [실무]

Block Scope는 변수의 유효 범위를 좁혀 오류를 줄인다.

권장:

```javascript
if (festival.active) {
  const title = festival.title;
  console.log(title);
}
```

반복문 예:

```javascript
for (const festival of festivals) {
  const title = festival.title;
  console.log(title);
}
```

주의:

- block 내부에서만 필요한 값은 block 내부 선언
- block 밖에서 필요한 값은 return 또는 별도 변수 설계
- `var`는 block scope를 따르지 않음
- `let` 재할당이 필요한지 검토
- block scope를 활용해 변수 충돌 방지

비권장:

```javascript
let title = "";

if (festival.active) {
  title = festival.title;
}
```

권장:

```javascript
if (festival.active) {
  const title = festival.title;
  console.log(title);
}
```

---

### [FAQ]

Q. Block Scope가 뭐야?
A. `{}` block 내부에서 선언된 변수가 해당 block 안에서만 유효한 범위다.

Q. const와 let은 Block Scope야?
A. 맞다. const와 let은 block scope를 가진다.

Q. var도 Block Scope를 가져?
A. 아니다. var는 block scope가 아니라 function scope를 가진다.

Q. Block Scope를 쓰면 뭐가 좋아?
A. 변수 접근 범위를 좁혀 충돌과 의도하지 않은 변경을 줄일 수 있다.

---

# 15. Lexical Scope

## 15.1 Lexical Scope Rules

### [개념]

Lexical Scope는 Function이 어디에서 호출되었는지가 아니라 어디에서 정의되었는지에 따라 Scope가 결정되는 방식이다.

JavaScript는 Lexical Scope를 따른다.

예:

```javascript
const prefix = "Festival";

function getTitle(title) {
  return `${prefix}: ${title}`;
}
```

`getTitle`은 정의된 위치의 외부 변수 `prefix`에 접근할 수 있다.

---

### [핵심]

- Lexical Scope
- static scope
- definition location
- outer scope
- inner function
- closure basis
- variable lookup
- scope chain

---

### [실무]

Lexical Scope는 Closure, Event Handler, Callback 이해의 기반이다.

예:

```javascript
function createFormatter(prefix) {
  return function format(title) {
    return `${prefix}: ${title}`;
  };
}

const formatFestivalTitle = createFormatter("Festival");
```

주의:

- 내부 Function은 외부 Scope 변수에 접근 가능
- 외부 변수 변경 시 내부 Function 결과가 달라질 수 있음
- 비동기 callback에서 오래된 값 참조 주의
- React Hook과 Event Handler의 closure 문제 이해에 중요
- Review Agent는 callback이 외부 mutable variable에 의존하는지 확인해야 함

---

### [FAQ]

Q. Lexical Scope가 뭐야?
A. 함수가 호출된 위치가 아니라 정의된 위치를 기준으로 Scope가 결정되는 방식이다.

Q. JavaScript는 Lexical Scope를 사용해?
A. 맞다. JavaScript는 Lexical Scope를 따른다.

Q. Lexical Scope는 왜 중요해?
A. Closure, Callback, Event Handler, React Hook의 상태 참조를 이해하는 기반이기 때문이다.

Q. 내부 함수는 외부 변수에 접근할 수 있어?
A. 접근할 수 있다. 이것이 Closure의 기반이 된다.

---

# 16. Closure

## 16.1 Closure Concept

### [개념]

Closure는 Function이 생성될 때의 외부 Scope 변수를 기억하고, 나중에도 그 변수에 접근할 수 있는 특성이다.

예:

```javascript
function createCounter() {
  let count = 0;

  return function increase() {
    count += 1;
    return count;
  };
}

const counter = createCounter();

counter();
counter();
```

`increase` Function은 `createCounter` 실행이 끝난 뒤에도 `count`를 기억한다.

---

### [핵심]

- Closure
- outer scope
- inner function
- remembered variable
- lexical environment
- private state
- callback
- event handler
- async callback
- React Hook basis

---

### [실무]

Closure는 Event Handler, Callback, 비동기 로직, React Hook 이해에 중요하다.

Event Handler 예:

```javascript
function createClickHandler(message) {
  return function handleClick() {
    console.log(message);
  };
}

button.addEventListener("click", createClickHandler("clicked"));
```

Private State 예:

```javascript
function createToggle() {
  let active = false;

  return function toggle() {
    active = !active;
    return active;
  };
}
```

주의:

- Closure는 외부 변수를 기억한다.
- 외부 mutable variable에 의존하면 결과 추적이 어려울 수 있다.
- 반복문과 Closure 조합에서 값 참조 오류 발생 가능
- 비동기 callback에서 오래된 상태 값을 참조할 수 있음
- 필요 없는 참조가 유지되면 memory leak 위험이 있다.

---

### [FAQ]

Q. Closure가 뭐야?
A. 함수가 생성될 때의 외부 변수 환경을 기억하고 나중에도 접근할 수 있는 특성이다.

Q. Closure는 언제 발생해?
A. 내부 함수가 외부 함수의 변수에 접근하고, 그 내부 함수가 나중에 실행될 수 있을 때 발생한다.

Q. Closure는 React와 관련 있어?
A. 관련 있다. Event Handler, Hook, 비동기 callback에서 closure 개념이 자주 등장한다.

Q. Closure는 위험해?
A. 자체는 유용하지만 오래된 상태 참조나 불필요한 메모리 참조를 만들 수 있어 주의가 필요하다.

---

## 16.2 Closure Common Pattern

### [개념]

Closure Pattern은 외부 Scope의 값을 기억하는 특성을 활용해 특정 동작을 만드는 방식이다.

대표 패턴:

- Counter
- Factory Function
- Event Handler 생성
- Private State
- Configuration 기억

---

### [핵심]

- Closure Pattern
- Counter
- Factory Function
- Event Handler Factory
- Private State
- Configuration
- reusable function
- state encapsulation

---

### [실무]

Factory Function 예:

```javascript
function createApiUrlBuilder(baseUrl) {
  return function buildUrl(path) {
    return `${baseUrl}${path}`;
  };
}

const buildFestivalApiUrl = createApiUrlBuilder("/api/festivals");
```

Event Handler Factory 예:

```javascript
function createSelectHandler(festivalId) {
  return function handleSelect() {
    console.log(`selected festival id: ${festivalId}`);
  };
}
```

Validation Rule 생성:

```javascript
function createMinLengthValidator(minLength) {
  return function validate(value) {
    return value.trim().length >= minLength;
  };
}

const validateKeyword = createMinLengthValidator(2);
```

주의:

- Closure는 상태를 숨길 수 있지만 과도하게 사용하면 흐름이 복잡해짐
- Factory Function 이름은 create로 시작하면 의미가 명확함
- 외부 mutable variable 변경 여부를 검토
- Review Agent는 Closure가 불필요하게 복잡한지 확인

---

### [FAQ]

Q. Closure Pattern은 언제 써?
A. 특정 설정값이나 상태를 기억하는 함수를 만들 때 사용한다.

Q. Factory Function이 뭐야?
A. 새로운 Function이나 객체를 만들어 반환하는 Function이다.

Q. Closure로 private state를 만들 수 있어?
A. 가능하다. 외부에서 직접 접근할 수 없는 값을 내부 함수가 기억하게 만들 수 있다.

Q. Closure를 많이 쓰면 좋은가?
A. 아니다. 필요한 경우에만 사용하고 흐름이 복잡해지면 단순한 함수 분리를 우선한다.

---

# 17. Function and API Logic

## 17.1 API Function Separation

### [개념]

API Function Separation은 HTTP 요청 함수, 응답 검증 함수, 데이터 변환 함수를 분리하는 방식이다.

Frontend Agent는 API 호출과 화면용 데이터 가공을 한 Function에 모두 넣지 않아야 한다.

---

### [핵심]

- API Function
- fetch
- response.ok
- response.json
- data mapping
- normalize response
- error handling
- separation of concerns
- reusable API logic

---

### [실무]

권장 구조:

```text
API Request Function
→ Response Validation
→ JSON Parse
→ Response Normalize Function
→ UI Logic
```

예:

```javascript
async function fetchFestivals(keyword) {
  const query = encodeURIComponent(keyword.trim());

  const response = await fetch(`/api/festivals/search?keyword=${query}`);

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

  return content;
}
```

호출 예:

```javascript
async function searchFestivals(keyword) {
  const responseBody = await fetchFestivals(keyword);

  return normalizeFestivalList(responseBody);
}
```

주의:

- fetch 함수에서 response.ok 확인
- JSON parsing 실패 가능성 고려
- API 원본 응답과 UI용 데이터 분리
- normalize 함수는 Pure Function으로 작성
- 민감정보 로그 출력 금지
- API URL 생성은 별도 함수로 분리 가능

---

### [FAQ]

Q. API Function을 왜 분리해?
A. 요청, 에러 처리, 응답 가공, UI 로직을 분리해 유지보수와 테스트를 쉽게 하기 위해서다.

Q. normalize 함수는 뭐야?
A. API 응답을 화면에서 사용하기 좋은 형태로 변환하는 Function이다.

Q. response.ok는 어디서 확인해?
A. fetch를 수행하는 API Request Function 안에서 확인하는 것이 좋다.

Q. API 원본 응답을 화면에서 바로 써도 돼?
A. 가능하지만 응답 구조 변경에 취약하므로 Mapping Function으로 분리하는 것이 좋다.

---

# 18. Function and Event Handler

## 18.1 Event Handler Function Rules

### [개념]

Event Handler Function은 클릭, 입력, 제출 같은 사용자 Event에 반응하는 Function이다.

예:

```javascript
function handleSubmit(event) {
  event.preventDefault();
}
```

---

### [핵심]

- Event Handler
- handle prefix
- event object
- preventDefault
- event.target
- input value
- form submit
- validation
- callback
- side effect

---

### [실무]

Event Handler 이름은 일반적으로 `handle` 접두사를 사용한다.

Form Submit 예:

```javascript
function handleSearchSubmit(event) {
  event.preventDefault();

  const form = event.currentTarget;
  const keyword = form.keyword.value.trim();

  if (!keyword) {
    return;
  }

  searchFestivals(keyword);
}
```

Input Change 예:

```javascript
function handleKeywordChange(event) {
  const keyword = event.target.value;

  updateKeyword(keyword);
}
```

작성 기준:

- Event Handler는 Event 입력 처리
- Validation은 별도 Function으로 분리 가능
- API 호출 Function은 별도 분리
- DOM 직접 조작 최소화
- Form 기본 동작 필요 시 `preventDefault`
- event.target과 event.currentTarget 구분

주의:

- Event Handler 안에 모든 로직을 넣지 않기
- 중복 등록 주의
- 비동기 Event Handler는 error handling 필요
- 민감정보 로그 출력 금지
- React 전환 시 Synthetic Event 이해 기반이 됨

---

### [FAQ]

Q. Event Handler Function은 뭐야?
A. 클릭, 입력, 제출 같은 사용자 이벤트에 반응하는 함수다.

Q. Event Handler 이름은 어떻게 지어?
A. 일반적으로 `handleSubmit`, `handleClick`, `handleKeywordChange`처럼 handle 접두사를 사용한다.

Q. preventDefault는 언제 써?
A. form submit의 페이지 새로고침 같은 기본 동작을 막을 때 사용한다.

Q. Event Handler에 모든 로직을 넣어도 돼?
A. 가능하지만 검증, API 호출, 데이터 가공은 별도 함수로 분리하는 것이 좋다.

---

# 19. Function Common Mistakes

## 19.1 Common Mistakes

### [개념]

Function 관련 실수는 Frontend Logic 복잡도, Callback 오류, Scope 오류, Closure 문제로 이어질 수 있다.

Review Agent는 Function 책임, return 누락, callback 사용, this 사용, Scope 참조를 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- 함수 하나에 책임 과다
- 의미 없는 함수명 사용
- Parameter 과다
- return 누락
- map callback return 누락
- Function Declaration hoisting에 의존
- Arrow Function 내부 this 오해
- 객체 method에 Arrow Function 사용 후 this 오류
- callback 실행 시점 오해
- async callback 에러 처리 누락
- Pure Function과 Side Effect 혼합
- API 호출과 데이터 변환 혼합
- 넓은 Scope의 mutable variable 사용
- Closure로 오래된 상태 참조
- Event Handler에 모든 로직 집중

---

### [실무]

Review Flow:

```text
Function Review
→ Function Name Check
→ Single Responsibility Check
→ Parameter Count Check
→ Return Value Check
→ Callback Return Check
→ Arrow Function this Check
→ Scope Dependency Check
→ Pure Function / Side Effect Separation Check
→ API Logic Separation Check
→ Closure Risk Check
```

나쁜 예:

```javascript
const user = {
  name: "jun",
  sayName: () => this.name,
};

const titles = festivals.map((festival) => {
  festival.title;
});
```

개선 예:

```javascript
const user = {
  name: "jun",
  sayName() {
    return this.name;
  },
};

const titles = festivals.map((festival) => festival.title);
```

주의:

- 함수 이름은 동작을 설명해야 함
- return이 필요한 함수는 명확히 return
- callback 내부 return 여부 확인
- Arrow Function의 this 동작 확인
- API 요청과 Mapping은 분리
- Closure가 외부 mutable state에 의존하는지 확인

---

### [FAQ]

Q. Function에서 가장 흔한 실수는 뭐야?
A. 책임 과다, return 누락, callback return 누락, Arrow Function this 오해, API 호출과 데이터 가공 혼합이다.

Q. map callback에서 return을 빼먹으면 어떻게 돼?
A. 결과 배열에 undefined가 들어갈 수 있다.

Q. Arrow Function에서 this 오류는 왜 발생해?
A. Arrow Function은 자체 this를 가지지 않고 외부 Scope의 this를 사용하기 때문이다.

Q. Review Agent는 Function에서 무엇을 우선 검토해야 해?
A. 함수명, 단일 책임, return 값, callback return, this 사용, Scope 의존성, Side Effect 분리를 우선 검토해야 한다.

---

# 20. Function, Scope, Closure Checklist

## 20.1 Document Quality Checklist

### [개념]

Function, Scope, Closure 문서는 Frontend Agent가 재사용 가능한 로직을 안전하게 작성하고 Callback, Event Handler, React Hook 기반 개념을 이해하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] Function 개념이 포함되었는가?
- [ ] Function Declaration 설명이 포함되었는가?
- [ ] Function Expression 설명이 포함되었는가?
- [ ] Arrow Function 설명이 포함되었는가?
- [ ] Arrow Function this 주의사항이 포함되었는가?
- [ ] Parameter와 Argument 차이가 포함되었는가?
- [ ] Return 설명과 return 누락 주의가 포함되었는가?
- [ ] Default Parameter 설명이 포함되었는가?
- [ ] Callback Function 설명이 포함되었는가?
- [ ] Pure Function 설명이 포함되었는가?
- [ ] Side Effect 설명이 포함되었는가?
- [ ] Scope 개념이 포함되었는가?
- [ ] Global Scope 설명이 포함되었는가?
- [ ] Function Scope 설명이 포함되었는가?
- [ ] Block Scope 설명이 포함되었는가?
- [ ] Lexical Scope 설명이 포함되었는가?
- [ ] Closure 설명이 포함되었는가?
- [ ] API Function Separation 기준이 포함되었는가?
- [ ] Event Handler Function 기준이 포함되었는가?
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
→ Function Rule Check
→ Scope Rule Check
→ Closure Rule Check
→ API Logic Separation Check
→ Event Handler Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part03_Operator_Condition_Loop
→ JavaScript_Foundation_Part04_Function_Scope_Closure
→ JavaScript_Foundation_Part05_Array_Object
```

---

### [FAQ]

Q. Function, Scope, Closure 문서 검수에서 가장 중요한 것은 뭐야?
A. Function 단일 책임, return 명확성, callback 사용, Arrow Function this, Scope 관리, Closure 위험, API Logic 분리 기준이다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React Event Handler, Hook, State Update, Callback, Component Logic은 Function, Scope, Closure 이해가 기반이다.

Q. 다음 Part와 어떻게 연결돼?
A. Part04는 로직 재사용과 Scope 기준을 만들고, Part05는 Array와 Object 데이터 처리를 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Function이 뭐야?
A. 재사용 가능한 코드 블록이다.

Q. Function은 왜 분리해?
A. 반복 로직을 줄이고 테스트와 유지보수를 쉽게 하기 위해 분리한다.

Q. Frontend에서 Function은 어디에 사용돼?
A. UI 상태 계산, 이벤트 처리, API 요청, 응답 데이터 가공, Form Validation에 사용된다.

Q. 좋은 Function의 기준은 뭐야?
A. 하나의 책임을 가지고 입력과 출력이 명확하며 이름만 봐도 목적을 알 수 있는 Function이다.

Q. Function Declaration이 뭐야?
A. function 키워드로 이름 있는 함수를 선언하는 방식이다.

Q. Function Declaration은 hoisting돼?
A. 된다. 하지만 실무에서는 선언 위치를 명확히 두고 사용하는 것이 좋다.

Q. Function Expression이 뭐야?
A. 함수를 변수에 값처럼 할당하는 방식이다.

Q. Function Expression은 선언 전에 사용할 수 있어?
A. const나 let에 할당한 경우 초기화 전 사용할 수 없다.

Q. Arrow Function이 뭐야?
A. `=>` 문법을 사용하는 짧은 함수 표현식이다.

Q. Arrow Function은 언제 써?
A. 짧은 callback, Array Method, 간단한 함수 표현에 자주 사용한다.

Q. Arrow Function은 항상 좋은 거야?
A. 아니다. callback에는 편리하지만 this가 필요한 객체 method에서는 주의해야 한다.

Q. Arrow Function의 this는 어떻게 동작해?
A. 자체 this를 만들지 않고 외부 Scope의 this를 사용한다.

Q. 객체 method에 Arrow Function을 써도 돼?
A. this가 필요 없다면 가능하지만, this가 필요하면 일반 method syntax가 적합하다.

Q. lexical this가 뭐야?
A. 함수가 선언된 외부 Scope의 this를 그대로 사용하는 동작이다.

Q. Parameter와 Argument 차이는 뭐야?
A. Parameter는 함수 정의의 입력 이름이고, Argument는 함수 호출 시 전달하는 실제 값이다.

Q. Parameter가 많으면 어떻게 해?
A. object parameter로 묶어 의미를 명확하게 만드는 것이 좋다.

Q. return은 뭐야?
A. Function 실행 결과를 호출한 곳으로 돌려주고 Function을 종료하는 문법이다.

Q. return이 없으면 무엇을 반환해?
A. undefined를 반환한다.

Q. map callback에서 return을 빼먹으면 어떻게 돼?
A. 새 배열 요소가 undefined가 될 수 있다.

Q. Default Parameter가 뭐야?
A. Argument가 없거나 undefined일 때 사용할 기본값을 지정하는 문법이다.

Q. null이 전달되면 Default Parameter가 적용돼?
A. 아니다. Default Parameter는 undefined일 때 적용된다.

Q. Callback Function이 뭐야?
A. 다른 함수에 인자로 전달되어 나중에 실행되는 함수다.

Q. Callback은 어디에 많이 쓰여?
A. Array Method, Event Handler, Promise 처리에서 많이 사용된다.

Q. map callback에서 return이 필요한 이유는?
A. map은 callback 반환값으로 새 배열을 만들기 때문이다.

Q. Pure Function이 뭐야?
A. 같은 입력에 대해 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 함수다.

Q. Pure Function은 왜 좋아?
A. 테스트, 리뷰, 디버깅이 쉽고 결과를 예측하기 쉽다.

Q. API 호출 함수는 Pure Function이야?
A. 아니다. 네트워크 요청은 Side Effect이므로 Pure Function이 아니다.

Q. Side Effect가 뭐야?
A. Function이 반환값 외부에 영향을 주는 동작이다.

Q. console.log도 Side Effect야?
A. 맞다. 외부 출력에 영향을 주기 때문에 Side Effect다.

Q. Side Effect를 왜 분리해야 해?
A. 테스트, 디버깅, 코드 리뷰가 쉬워지고 로직 예측 가능성이 높아지기 때문이다.

Q. Scope가 뭐야?
A. 변수와 함수에 접근할 수 있는 범위다.

Q. Scope를 좁게 유지하는 이유는?
A. 변수 충돌과 의도하지 않은 값 변경을 줄이기 위해서다.

Q. Global Scope가 뭐야?
A. 코드 어디에서나 접근 가능한 최상위 Scope다.

Q. 전역 변수는 왜 위험해?
A. 여러 위치에서 변경될 수 있어 값 흐름을 추적하기 어렵고 이름 충돌이 발생할 수 있다.

Q. Function Scope가 뭐야?
A. Function 내부에서 선언된 변수가 해당 Function 안에서만 유효한 범위다.

Q. var는 Function Scope야?
A. 맞다. var는 block scope가 아니라 function scope를 가진다.

Q. Block Scope가 뭐야?
A. `{}` block 내부에서 선언된 변수가 해당 block 안에서만 유효한 범위다.

Q. const와 let은 Block Scope야?
A. 맞다. const와 let은 block scope를 가진다.

Q. Lexical Scope가 뭐야?
A. 함수가 호출된 위치가 아니라 정의된 위치를 기준으로 Scope가 결정되는 방식이다.

Q. JavaScript는 Lexical Scope를 사용해?
A. 맞다. JavaScript는 Lexical Scope를 따른다.

Q. Closure가 뭐야?
A. 함수가 생성될 때의 외부 변수 환경을 기억하고 나중에도 접근할 수 있는 특성이다.

Q. Closure는 언제 발생해?
A. 내부 함수가 외부 함수의 변수에 접근하고, 그 내부 함수가 나중에 실행될 수 있을 때 발생한다.

Q. Closure는 React와 관련 있어?
A. 관련 있다. Event Handler, Hook, 비동기 callback에서 closure 개념이 자주 등장한다.

Q. Closure Pattern은 언제 써?
A. 특정 설정값이나 상태를 기억하는 함수를 만들 때 사용한다.

Q. Factory Function이 뭐야?
A. 새로운 Function이나 객체를 만들어 반환하는 Function이다.

Q. API Function을 왜 분리해?
A. 요청, 에러 처리, 응답 가공, UI 로직을 분리해 유지보수와 테스트를 쉽게 하기 위해서다.

Q. normalize 함수는 뭐야?
A. API 응답을 화면에서 사용하기 좋은 형태로 변환하는 Function이다.

Q. Event Handler Function은 뭐야?
A. 클릭, 입력, 제출 같은 사용자 이벤트에 반응하는 함수다.

Q. Event Handler 이름은 어떻게 지어?
A. 일반적으로 handleSubmit, handleClick, handleKeywordChange처럼 handle 접두사를 사용한다.

Q. Function에서 가장 흔한 실수는 뭐야?
A. 책임 과다, return 누락, callback return 누락, Arrow Function this 오해, API 호출과 데이터 가공 혼합이다.

Q. Review Agent는 Function에서 무엇을 우선 검토해야 해?
A. 함수명, 단일 책임, return 값, callback return, this 사용, Scope 의존성, Side Effect 분리를 우선 검토해야 한다.

Q. JavaScript Foundation Part04 다음에는 무엇을 다뤄야 해?
A. Array와 Object를 다루는 Part05로 이어지는 것이 좋다.
