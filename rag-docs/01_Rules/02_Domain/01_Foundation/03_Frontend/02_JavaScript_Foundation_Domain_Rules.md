# JavaScript Foundation Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

JavaScript Foundation Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- JavaScript 기본 문법 이해
- Browser 기반 동작 이해
- DOM 조작 기초 이해
- Event Handling 이해
- Async / Promise / Fetch 이해
- API 연동 기초 코드 작성 지원
- React 학습 전 JavaScript 기반 지식 제공
- Frontend Logic 구현 지원
- Frontend Debugging 지원
- TypeScript 전환 전 JavaScript Core 개념 정리

---

### [핵심]

우선순위:

1. JavaScript Core Syntax
2. Data Type / Variable
3. Function
4. Array / Object
5. DOM / Event
6. Async JavaScript
7. Fetch API
8. Error Handling
9. Module
10. Frontend Practical Logic
11. React Foundation Readiness

---

### [실무]

2026 실무 기준에서 JavaScript Foundation 문서는 단순 문법 암기 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- UI 이벤트 로직 작성
- API 요청 / 응답 처리
- 배열 / 객체 데이터 가공
- DOM 기반 구조 이해
- React Component 로직 이해
- 비동기 처리 흐름 분석
- JavaScript 오류 원인 분석
- TypeScript 전환 전 기본 문법 기반 확보

---

### [FAQ]

Q. JavaScript Foundation 문서는 사람 공부용 문서야?

A.
아니다. Frontend Agent가 화면 로직, 이벤트 처리, API 연동 코드를 생성하고 검토하기 위한 RAG 문서다.

Q. React를 할 건데 JavaScript Foundation이 왜 필요해?

A.
React Component, State, Event, API 연동은 모두 JavaScript 문법과 비동기 처리 위에서 동작하기 때문이다.

Q. JavaScript Foundation에서 가장 중요한 기준은 뭐야?

A.
변수, 함수, 배열, 객체, DOM, Event, Promise, async/await, Fetch API, Error Handling이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

JavaScript Foundation 문서는 Frontend 기본 로직 구현에 필요한 범위를 포함한다.

포함 범위:

- JavaScript Basic Syntax
- Variable
- Data Type
- Operator
- Condition
- Loop
- Function
- Arrow Function
- Scope
- Hoisting
- Closure Basics
- Array
- Object
- Destructuring
- Spread / Rest
- Template Literal
- Optional Chaining
- Nullish Coalescing
- DOM Selection
- DOM Manipulation
- Event Handling
- Form Handling
- Browser API Basics
- Timer
- JSON
- Fetch API
- Promise
- async / await
- Error Handling
- Module
- Import / Export
- Frontend Debugging
- Clean Code Basics
- React Readiness

---

### [핵심]

반드시 포함:

- JavaScript는 Browser와 Node.js에서 실행되는 언어
- Frontend 문서에서는 Browser JavaScript 중심
- React 이전에 JavaScript 기본 문법 필수
- API Response 처리는 Object / Array 중심
- 비동기 처리는 Promise / async / await 중심
- DOM / Event는 React Event System 이해의 기반
- Module은 파일 분리와 재사용의 기반

---

### [실무]

JavaScript Foundation은 React / TypeScript / API 연동 문서의 기반이다.

실무 연결:

```text
HTML CSS Foundation
→ JavaScript Foundation
→ TypeScript Foundation
→ React Core
→ React Component Design
→ Data Fetching & REST API Integration
```

---

### [FAQ]

Q. JavaScript Foundation에서 Node.js도 깊게 다뤄?

A.
아니다. 이 문서는 Frontend Foundation 문서이므로 Browser JavaScript 중심으로 작성한다.

Q. TypeScript 문법도 여기에 포함해?

A.
아니다. TypeScript는 별도 Domain Rules에서 다룬다. 이 문서는 JavaScript 기본 문법에 집중한다.

Q. React Hook도 여기서 다뤄?

A.
아니다. React Hook은 React Core 또는 React Component Design 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

JavaScript Foundation 문서에서는 고급 Framework와 Runtime 심화를 제외한다.

제외 범위:

- React Core 심화
- React Hook 심화
- TypeScript Type System
- Node.js Backend 심화
- Express / NestJS
- Build Tool 심화
- Vite / Webpack 설정 심화
- Advanced Browser Rendering
- Service Worker 심화
- WebSocket 심화
- WebRTC
- Canvas / WebGL
- Functional Programming 심화
- Design Pattern 심화
- Performance Profiling 심화

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- React / TypeScript / Frontend Architecture 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- JavaScript 기본 문법 중심 유지

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
JavaScript Foundation
→ TypeScript Foundation
→ React Core
→ State Management
→ Frontend Architecture
```

---

### [FAQ]

Q. WebSocket은 여기서 다뤄?

A.
아니다. WebSocket은 실시간 통신 또는 Frontend Advanced 문서에서 다룬다.

Q. JavaScript Design Pattern은 여기서 다뤄?

A.
기초적인 함수 분리와 모듈화만 다루고, Design Pattern 심화는 별도 문서에서 다룬다.

Q. Node.js 서버 코드는 여기서 다뤄?

A.
아니다. Frontend Foundation 목적이므로 Browser JavaScript 중심으로 작성한다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

JavaScript Foundation RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 Frontend 적용 기준
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

Q. 모든 JavaScript 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

JavaScript 문서에는 실무 적용과 검증을 위해 추가 Section을 포함할 수 있다.

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

- 비동기 처리 설명 → [Flow], [예제], [Troubleshooting]
- 배열 / 객체 설명 → [예제], [Comparison]
- DOM / Event 설명 → [Flow], [주의]
- Error Handling 설명 → [Best Practice], [Troubleshooting]
- Scope / Closure 설명 → [개념], [예제], [FAQ]

---

### [실무]

예시:

```md
### [Flow]

User Event
→ Event Handler
→ Data Processing
→ API Request
→ UI Update
```

---

### [FAQ]

Q. JavaScript 문서에 Troubleshooting이 필요한 이유는?

A.
undefined, null, 비동기 순서, fetch 실패, 이벤트 중복 실행 같은 오류가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
var vs let vs const, == vs ===, map vs forEach, Promise vs async/await처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. JavaScript Core Rules

## 4.1 JavaScript Basic Syntax Rules

### [개념]

JavaScript는 웹 브라우저에서 동작하는 대표적인 Frontend Programming Language다.

기본 예:

```javascript
const name = "FestaPick";
const count = 3;

if (count > 0) {
  console.log(`${name}: ${count}`);
}
```

---

### [핵심]

반드시 포함:

- Statement
- Expression
- Variable
- Data Type
- Operator
- Condition
- Loop
- Function
- Object
- Array
- Module
- Comment
- Semicolon

---

### [실무]

JavaScript 문서는 문법 설명보다 Frontend 사용 예제 중심으로 작성한다.

권장:

- UI 상태 계산
- API Response 가공
- Form 입력 처리
- Event Handler 작성
- 조건부 렌더링 로직 이해
- React 코드로 이어질 수 있는 예제

금지:

- 문법만 장황하게 나열
- 실무 예제 없는 이론 설명
- 오래된 브라우저 호환성 중심 설명
- var 중심 예제
- jQuery 중심 예제

---

### [FAQ]

Q. JavaScript는 어디에서 실행돼?

A.
브라우저와 Node.js에서 실행된다. Frontend Foundation 문서에서는 브라우저 실행 환경을 우선 다룬다.

Q. JavaScript 문법은 React와 연결돼?

A.
연결된다. React Component의 JSX, Event, State Update, API 호출은 JavaScript 문법 기반이다.

---

## 4.2 Variable Rules

### [개념]

Variable은 값을 저장하는 이름이다.

JavaScript에서는 `let`, `const`, `var`로 변수를 선언할 수 있다.

예:

```javascript
const title = "Festival";
let count = 0;

count += 1;
```

---

### [핵심]

필수 포함:

- const
- let
- var
- reassignment
- block scope
- function scope
- hoisting
- temporal dead zone

권장:

- 기본은 `const`
- 값 재할당이 필요하면 `let`
- `var` 사용 지양

---

### [실무]

실무 기준:

```javascript
const userName = "jun";
let currentPage = 1;

currentPage += 1;
```

금지:

```javascript
var userName = "jun";
```

이유:

- `var`는 function scope
- 재선언 가능
- hoisting 혼동 발생
- 유지보수성 저하

---

### [FAQ]

Q. const만 쓰면 돼?

A.
기본은 const를 사용하고, 값 재할당이 필요한 경우에만 let을 사용한다.

Q. var는 왜 피해야 해?

A.
function scope, 재선언, hoisting 때문에 예측하기 어려운 코드가 될 수 있다.

Q. const 객체는 내부 값을 바꿀 수 없어?

A.
const는 변수 재할당을 막는다. 객체나 배열의 내부 값 변경은 가능하다.

---

## 4.3 Data Type Rules

### [개념]

JavaScript Data Type은 값의 종류를 의미한다.

Primitive Type과 Reference Type으로 구분한다.

---

### [핵심]

Primitive Type:

- string
- number
- boolean
- null
- undefined
- symbol
- bigint

Reference Type:

- object
- array
- function

---

### [실무]

API Response와 UI 상태는 대부분 Object / Array로 처리된다.

예:

```javascript
const festival = {
  id: 1,
  title: "Spring Festival",
  active: true,
};

const festivals = [
  { id: 1, title: "Spring Festival" },
  { id: 2, title: "Summer Festival" },
];
```

주의:

- `null`과 `undefined` 구분
- 숫자와 문자열 비교 주의
- 배열도 typeof 결과는 object
- Object / Array는 참조 타입

---

### [FAQ]

Q. null과 undefined 차이는?

A.
undefined는 값이 할당되지 않은 상태이고, null은 의도적으로 값이 없음을 표현한 값이다.

Q. 배열은 JavaScript에서 어떤 타입이야?

A.
배열은 object 타입이다. 배열 여부는 `Array.isArray()`로 확인하는 것이 좋다.

Q. API 응답은 보통 어떤 자료형으로 처리해?

A.
대부분 object와 array 조합으로 처리한다.

---

## 4.4 Operator Rules

### [개념]

Operator는 값을 계산하거나 비교하거나 논리 판단을 수행하는 기호다.

---

### [핵심]

필수 포함:

- Arithmetic Operator
- Assignment Operator
- Comparison Operator
- Logical Operator
- Strict Equality
- Ternary Operator
- Optional Chaining
- Nullish Coalescing

예:

```javascript
const isAdult = age >= 20;
const displayName = user?.name ?? "Guest";
```

---

### [실무]

권장:

- `===` 사용
- `!==` 사용
- `==` 사용 지양
- optional chaining으로 안전한 중첩 접근
- nullish coalescing으로 null / undefined 기본값 처리

주의:

```javascript
const value = user && user.profile && user.profile.name;
```

개선:

```javascript
const value = user?.profile?.name;
```

---

### [FAQ]

Q. ==와 === 차이는?

A.
==는 타입 변환 후 비교하고, ===는 타입과 값을 모두 비교한다. 실무에서는 ===를 권장한다.

Q. optional chaining은 왜 써?

A.
중첩 객체 접근 시 null 또는 undefined로 인한 오류를 줄이기 위해 사용한다.

Q. ??와 || 차이는?

A.
??는 null 또는 undefined일 때만 기본값을 사용하고, ||는 false, 0, 빈 문자열도 기본값으로 처리할 수 있다.

---

# 5. Control Flow Rules

## 5.1 Condition Rules

### [개념]

Condition은 조건에 따라 실행 흐름을 나누는 문법이다.

예:

```javascript
if (isLoggedIn) {
  showProfile();
} else {
  showLoginButton();
}
```

---

### [핵심]

필수 포함:

- if
- else if
- else
- switch
- ternary operator
- truthy
- falsy
- guard clause

---

### [실무]

권장:

```javascript
function getDisplayName(user) {
  if (!user) {
    return "Guest";
  }

  return user.name;
}
```

Guard Clause 장점:

- 중첩 조건 감소
- 읽기 쉬운 흐름
- 예외 상황 먼저 처리
- 함수 책임 명확화

---

### [FAQ]

Q. truthy와 falsy가 뭐야?

A.
조건문에서 true처럼 평가되는 값은 truthy, false처럼 평가되는 값은 falsy다.

Q. JavaScript의 falsy 값은 뭐야?

A.
false, 0, -0, 0n, "", null, undefined, NaN이다.

Q. 삼항 연산자는 언제 써?

A.
짧은 조건부 값 선택에 적합하다. 복잡한 로직은 if문이 더 읽기 쉽다.

---

## 5.2 Loop Rules

### [개념]

Loop는 반복 작업을 처리하는 문법이다.

---

### [핵심]

필수 포함:

- for
- while
- for...of
- for...in
- break
- continue
- Array method

---

### [실무]

배열 데이터 처리에는 Array Method를 우선 고려한다.

권장:

```javascript
const titles = festivals.map((festival) => festival.title);
```

반복문 사용:

```javascript
for (const festival of festivals) {
  console.log(festival.title);
}
```

주의:

- 배열 순회에는 `for...of`
- 객체 key 순회에는 `for...in` 또는 `Object.keys`
- 단순 변환은 `map`
- 필터링은 `filter`
- 누적 계산은 `reduce`

---

### [FAQ]

Q. for문과 map 중 뭐를 써?

A.
새 배열을 만들 목적이면 map을 사용하고, 단순 반복 작업이면 for문이나 for...of를 사용할 수 있다.

Q. for...of와 for...in 차이는?

A.
for...of는 iterable 값 순회에 사용하고, for...in은 객체 key 순회에 사용한다.

---

# 6. Function Rules

## 6.1 Function Basics

### [개념]

Function은 재사용 가능한 코드 블록이다.

예:

```javascript
function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}
```

---

### [핵심]

필수 포함:

- Function Declaration
- Function Expression
- Arrow Function
- Parameter
- Argument
- Return
- Default Parameter
- Callback Function
- Pure Function

---

### [실무]

권장:

- 하나의 함수는 하나의 책임
- 입력과 출력 명확화
- 의미 있는 함수명
- UI 로직과 데이터 가공 로직 분리
- API 호출 함수 분리
- 복잡한 조건은 함수로 분리

예:

```javascript
function isActiveFestival(festival) {
  return festival.status === "ACTIVE";
}
```

---

### [FAQ]

Q. 함수는 왜 분리해?

A.
반복 로직을 줄이고, 테스트와 유지보수를 쉽게 하기 위해 분리한다.

Q. return이 없으면 함수는 뭘 반환해?

A.
명시적인 return이 없으면 undefined를 반환한다.

---

## 6.2 Arrow Function Rules

### [개념]

Arrow Function은 짧은 함수 표현식 문법이다.

예:

```javascript
const getTitle = (festival) => festival.title;
```

---

### [핵심]

반드시 설명:

- 짧은 callback에 자주 사용
- lexical this를 가짐
- function declaration과 this 동작이 다름
- hoisting 방식이 다름
- method 정의에는 주의 필요

---

### [실무]

배열 메서드와 자주 함께 사용한다.

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
const festivalTitles = activeFestivals.map((festival) => festival.title);
```

주의:

```javascript
const user = {
  name: "jun",
  sayName: () => {
    console.log(this.name);
  },
};
```

객체 method에서 `this`가 필요한 경우 arrow function은 부적절할 수 있다.

---

### [FAQ]

Q. Arrow Function은 항상 좋은 거야?

A.
아니다. callback에는 편리하지만 this가 필요한 객체 method에서는 주의해야 한다.

Q. Arrow Function은 hoisting돼?

A.
const나 let에 할당한 arrow function은 변수 초기화 전 사용할 수 없다.

---

## 6.3 Scope and Closure Rules

### [개념]

Scope는 변수에 접근할 수 있는 범위다.

Closure는 함수가 외부 Scope의 변수를 기억하는 특성이다.

---

### [핵심]

필수 포함:

- Global Scope
- Function Scope
- Block Scope
- Lexical Scope
- Closure
- let / const block scope
- var function scope

---

### [실무]

Closure 예:

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
```

Closure는 React Hook, Event Handler, Callback 이해에 중요하다.

주의:

- 의도치 않은 외부 변수 참조
- 오래된 상태 값 참조
- 반복문과 closure 혼동
- 메모리 누수 가능성

---

### [FAQ]

Q. Scope가 뭐야?

A.
변수와 함수에 접근할 수 있는 범위다.

Q. Closure가 뭐야?

A.
함수가 생성될 때의 외부 변수 환경을 기억하고 나중에도 접근할 수 있는 특성이다.

Q. Closure는 React와 관련 있어?

A.
관련 있다. Event Handler, Hook, 비동기 callback에서 closure 개념이 자주 등장한다.

---

# 7. Array and Object Rules

## 7.1 Array Rules

### [개념]

Array는 순서가 있는 여러 값을 저장하는 자료구조다.

예:

```javascript
const festivals = ["Spring", "Summer", "Winter"];
```

---

### [핵심]

필수 포함:

- length
- push
- pop
- includes
- find
- filter
- map
- reduce
- sort
- some
- every
- slice
- splice

---

### [실무]

Frontend API Response 처리에서 배열 메서드는 매우 중요하다.

예:

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);

const festivalCards = activeFestivals.map((festival) => ({
  id: festival.id,
  title: festival.title,
  region: festival.region,
}));
```

주의:

- `map`은 새 배열 반환
- `filter`는 조건에 맞는 새 배열 반환
- `find`는 첫 번째 요소 반환
- `sort`는 원본 배열 변경
- `slice`는 원본 유지
- `splice`는 원본 변경

---

### [FAQ]

Q. map과 forEach 차이는?

A.
map은 새 배열을 반환하고 forEach는 반환값 없이 반복 작업만 수행한다.

Q. filter와 find 차이는?

A.
filter는 조건에 맞는 모든 요소 배열을 반환하고 find는 첫 번째 요소 하나를 반환한다.

Q. sort는 원본 배열을 바꿔?

A.
바꾼다. 원본 변경을 피하려면 복사 후 sort를 사용한다.

---

## 7.2 Object Rules

### [개념]

Object는 key-value 구조로 데이터를 저장하는 자료구조다.

예:

```javascript
const user = {
  id: 1,
  name: "jun",
  role: "USER",
};
```

---

### [핵심]

필수 포함:

- property
- method
- dot notation
- bracket notation
- Object.keys
- Object.values
- Object.entries
- Object.assign
- object spread
- nested object
- optional chaining

---

### [실무]

API Response는 대부분 Object와 Array 조합이다.

예:

```javascript
const response = {
  data: {
    content: [
      { id: 1, title: "Festival A" },
      { id: 2, title: "Festival B" },
    ],
  },
};

const festivals = response.data.content;
```

안전한 접근:

```javascript
const festivals = response?.data?.content ?? [];
```

---

### [FAQ]

Q. dot notation과 bracket notation 차이는?

A.
dot notation은 고정 property 접근에 사용하고, bracket notation은 동적 key 접근에 사용한다.

Q. Object.keys는 언제 써?

A.
객체의 key 목록을 배열로 가져와 순회할 때 사용한다.

Q. 중첩 객체 접근 시 오류를 줄이는 방법은?

A.
optional chaining과 nullish coalescing을 함께 사용한다.

---

## 7.3 Destructuring and Spread Rules

### [개념]

Destructuring은 배열이나 객체에서 값을 쉽게 꺼내는 문법이다.

Spread는 배열이나 객체를 펼쳐 복사하거나 병합하는 문법이다.

---

### [핵심]

필수 포함:

- Object Destructuring
- Array Destructuring
- Default Value
- Rest Parameter
- Spread Syntax
- Shallow Copy
- Immutable Update

---

### [실무]

객체 구조 분해:

```javascript
const festival = {
  id: 1,
  title: "Spring Festival",
  region: "Seoul",
};

const { id, title } = festival;
```

배열 복사:

```javascript
const nextFestivals = [...festivals, newFestival];
```

객체 업데이트:

```javascript
const updatedUser = {
  ...user,
  name: "newName",
};
```

주의:

- Spread는 얕은 복사
- 중첩 객체는 내부 참조 공유
- React State Update에서 자주 사용
- 원본 변경 여부 확인 필요

---

### [FAQ]

Q. Spread는 깊은 복사야?

A.
아니다. Spread는 기본적으로 얕은 복사다.

Q. Destructuring은 왜 써?

A.
객체나 배열에서 필요한 값을 간결하게 꺼내기 위해 사용한다.

Q. React에서 Spread가 중요한 이유는?

A.
State를 직접 변경하지 않고 새 객체나 새 배열을 만들 때 자주 사용하기 때문이다.

---

# 8. DOM and Event Rules

## 8.1 DOM Rules

### [개념]

DOM은 HTML 문서를 JavaScript가 조작할 수 있는 객체 구조로 표현한 것이다.

---

### [핵심]

필수 포함:

- document
- window
- querySelector
- querySelectorAll
- getElementById
- textContent
- innerHTML
- classList
- setAttribute
- createElement
- appendChild
- remove

---

### [실무]

기본 예:

```javascript
const titleElement = document.querySelector(".page-title");
titleElement.textContent = "Festival List";
```

주의:

- DOM 요소가 null일 수 있음
- innerHTML 사용 시 XSS 주의
- classList로 class 제어
- React에서는 직접 DOM 조작보다 state 기반 렌더링 우선
- DOM 개념은 React 내부 동작 이해에 필요

---

### [FAQ]

Q. DOM이 뭐야?

A.
HTML 문서를 JavaScript가 읽고 조작할 수 있도록 만든 객체 구조다.

Q. querySelector는 뭘 반환해?

A.
조건에 맞는 첫 번째 요소를 반환한다. 없으면 null을 반환한다.

Q. React에서도 DOM 조작을 직접 해?

A.
대부분 직접 조작하지 않는다. React에서는 state와 props 기반으로 UI를 갱신한다.

---

## 8.2 Event Handling Rules

### [개념]

Event Handling은 사용자의 클릭, 입력, 제출 같은 행동에 반응하는 로직이다.

예:

```javascript
const button = document.querySelector(".submit-button");

button.addEventListener("click", () => {
  console.log("clicked");
});
```

---

### [핵심]

필수 포함:

- click
- input
- change
- submit
- keydown
- addEventListener
- event object
- event.target
- preventDefault
- stopPropagation
- event bubbling
- event delegation

---

### [실무]

Form submit 예:

```javascript
const form = document.querySelector(".search-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const keyword = event.target.keyword.value;
  console.log(keyword);
});
```

주의:

- form submit 기본 새로고침 방지
- event target 확인
- 이벤트 중복 등록 주의
- 이벤트 제거 필요 여부 확인
- React Synthetic Event 이해 기반

---

### [FAQ]

Q. preventDefault는 왜 써?

A.
form 제출 시 페이지 새로고침 같은 브라우저 기본 동작을 막기 위해 사용한다.

Q. event.target은 뭐야?

A.
이벤트가 실제 발생한 요소다.

Q. Event Bubbling이 뭐야?

A.
자식 요소에서 발생한 이벤트가 부모 요소 방향으로 전파되는 현상이다.

---

## 8.3 Form Handling Rules

### [개념]

Form Handling은 사용자 입력 값을 읽고 검증하고 제출하는 로직이다.

---

### [핵심]

필수 포함:

- input value
- submit event
- preventDefault
- validation
- trim
- required
- error message
- disabled button
- form data

---

### [실무]

예:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}

const keyword = input.value.trim();

if (!validateKeyword(keyword)) {
  showError("검색어를 입력하세요.");
}
```

Form Handling Flow:

```text
User Input
→ Read Value
→ Trim
→ Validate
→ Show Error or Submit
→ API Request
```

---

### [FAQ]

Q. 입력값에 trim을 왜 써?

A.
앞뒤 공백만 입력된 값을 유효한 입력으로 처리하지 않기 위해 사용한다.

Q. Form 검증은 Frontend만 하면 돼?

A.
아니다. Frontend 검증은 사용자 경험용이고 Backend 검증도 반드시 필요하다.

---

# 9. Async JavaScript Rules

## 9.1 Promise Rules

### [개념]

Promise는 비동기 작업의 성공 또는 실패 결과를 표현하는 객체다.

상태:

```text
Pending
→ Fulfilled
→ Rejected
```

---

### [핵심]

필수 포함:

- Promise
- pending
- fulfilled
- rejected
- then
- catch
- finally
- chaining
- error handling

---

### [실무]

예:

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

- catch 누락 금지
- Promise chain return 누락 주의
- 비동기 실행 순서 이해 필요
- 에러 처리 위치 명확화

---

### [FAQ]

Q. Promise가 뭐야?

A.
비동기 작업의 완료 또는 실패 결과를 나중에 처리하기 위한 객체다.

Q. then과 catch는 뭐야?

A.
then은 성공 결과를 처리하고 catch는 실패 오류를 처리한다.

---

## 9.2 async / await Rules

### [개념]

async / await는 Promise 기반 비동기 코드를 동기 코드처럼 읽기 쉽게 작성하는 문법이다.

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

필수 포함:

- async function
- await
- Promise 반환
- try / catch
- sequential execution
- parallel execution
- loading state
- error state

---

### [실무]

권장 예:

```javascript
async function fetchFestivals() {
  try {
    const response = await fetch("/api/festivals");

    if (!response.ok) {
      throw new Error("Failed to fetch festivals");
    }

    return await response.json();
  } catch (error) {
    console.error(error);
    return [];
  }
}
```

주의:

- async function은 Promise 반환
- await는 async function 내부에서 사용
- try / catch로 실패 처리
- response.ok 확인
- loading / error UI 고려

---

### [FAQ]

Q. async function은 뭘 반환해?

A.
항상 Promise를 반환한다.

Q. await는 어디서 쓸 수 있어?

A.
일반적으로 async function 내부에서 사용한다.

Q. async / await를 쓰면 에러 처리는 어떻게 해?

A.
try / catch를 사용해 비동기 오류를 처리한다.

---

## 9.3 Fetch API Rules

### [개념]

Fetch API는 브라우저에서 HTTP 요청을 보내는 기본 API다.

---

### [핵심]

필수 포함:

- fetch
- GET
- POST
- PUT
- PATCH
- DELETE
- Headers
- JSON body
- response.ok
- response.json
- status code
- error handling

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
async function createReview(review) {
  const response = await fetch("/api/reviews", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(review),
  });

  if (!response.ok) {
    throw new Error("Failed to create review");
  }

  return await response.json();
}
```

주의:

- fetch는 HTTP 에러 상태에서 자동 reject하지 않음
- response.ok 확인 필요
- JSON 전송 시 Content-Type 설정
- body는 JSON.stringify 사용
- 인증 토큰은 Authorization Header에 포함
- 민감정보 로그 출력 금지

---

### [FAQ]

Q. fetch는 404나 500에서 catch로 바로 가?

A.
아니다. 네트워크 오류가 아닌 HTTP 오류 상태는 자동 reject되지 않으므로 response.ok를 확인해야 한다.

Q. POST 요청에서 body에 객체를 바로 넣어도 돼?

A.
안 된다. JSON 전송 시 `JSON.stringify()`로 문자열 변환해야 한다.

Q. API 요청에 JWT는 어디에 넣어?

A.
일반적으로 `Authorization: Bearer token` Header에 넣는다.

---

# 10. JSON and API Data Rules

## 10.1 JSON Rules

### [개념]

JSON은 Frontend와 Backend가 데이터를 주고받을 때 자주 사용하는 텍스트 기반 데이터 형식이다.

---

### [핵심]

필수 포함:

- JSON
- JSON.stringify
- JSON.parse
- object
- array
- API response
- request body
- serialization
- deserialization

---

### [실무]

예:

```javascript
const review = {
  festivalId: 1,
  rating: 5,
  content: "좋아요",
};

const body = JSON.stringify(review);
```

응답 처리:

```javascript
const data = await response.json();
```

주의:

- JSON key는 문자열
- 함수는 JSON에 포함되지 않음
- undefined는 JSON 변환 시 누락될 수 있음
- 날짜 값은 문자열로 전달되는 경우가 많음

---

### [FAQ]

Q. JSON.stringify는 언제 써?

A.
JavaScript 객체를 JSON 문자열로 변환해 API request body로 보낼 때 사용한다.

Q. JSON.parse는 언제 써?

A.
JSON 문자열을 JavaScript 객체로 변환할 때 사용한다.

Q. response.json()은 뭐야?

A.
HTTP 응답 body를 JSON으로 파싱해 JavaScript 객체로 반환하는 메서드다.

---

## 10.2 API Response Processing Rules

### [개념]

API Response Processing은 서버에서 받은 데이터를 화면에 사용하기 좋은 형태로 변환하는 과정이다.

---

### [핵심]

필수 포함:

- response structure
- data
- content
- pagination
- error response
- null handling
- default value
- mapping
- filtering
- sorting

---

### [실무]

예:

```javascript
function normalizeFestivalResponse(response) {
  return response?.data?.content ?? [];
}
```

목록 처리:

```javascript
const activeFestivals = festivals
  .filter((festival) => festival.active)
  .map((festival) => ({
    id: festival.id,
    title: festival.title,
    imageUrl: festival.imageUrl ?? "/default.png",
  }));
```

주의:

- 응답 구조 변경 가능성 고려
- null / undefined 방어
- 빈 배열 기본값 사용
- 화면용 데이터 변환 함수 분리
- API 원본 데이터 직접 변경 금지

---

### [FAQ]

Q. API 응답이 null일 수 있으면 어떻게 해?

A.
optional chaining과 nullish coalescing으로 기본값을 지정한다.

Q. 화면용 데이터 변환 함수는 왜 분리해?

A.
API 구조와 UI 구조를 분리해 유지보수를 쉽게 하기 위해서다.

---

# 11. Module Rules

## 11.1 Module and Import Export Rules

### [개념]

Module은 JavaScript 코드를 파일 단위로 분리하고 재사용하는 방식이다.

---

### [핵심]

필수 포함:

- export
- export default
- named export
- import
- module scope
- file separation
- utility function
- api client
- component logic

---

### [실무]

Named Export 예:

```javascript
export function formatDate(dateText) {
  return new Date(dateText).toLocaleDateString("ko-KR");
}
```

Import 예:

```javascript
import { formatDate } from "./dateUtils";
```

Default Export 예:

```javascript
export default function createApiClient() {
  return {};
}
```

권장 구조:

```text
src
├ api
│  └ festivalApi.js
├ utils
│  └ dateUtils.js
├ constants
│  └ routes.js
└ pages
```

---

### [FAQ]

Q. named export와 default export 차이는?

A.
named export는 이름을 맞춰 import하고, default export는 원하는 이름으로 import할 수 있다.

Q. 유틸 함수는 왜 파일로 분리해?

A.
여러 곳에서 재사용하고 테스트하기 쉽게 만들기 위해 분리한다.

Q. 모든 코드를 한 파일에 작성해도 돼?

A.
작은 예제는 가능하지만 실무 프로젝트에서는 역할별 파일 분리가 필요하다.

---

# 12. Error Handling Rules

## 12.1 JavaScript Error Handling

### [개념]

Error Handling은 코드 실행 중 발생할 수 있는 오류를 처리하는 방식이다.

---

### [핵심]

필수 포함:

- try
- catch
- finally
- throw
- Error object
- custom error message
- async error handling
- API error handling
- user friendly message

---

### [실무]

예:

```javascript
async function loadFestivals() {
  try {
    const festivals = await getFestivals();
    return festivals;
  } catch (error) {
    console.error("Festival load failed:", error);
    return [];
  }
}
```

주의:

- catch에서 오류 무시 금지
- 사용자 메시지와 개발자 로그 구분
- API 에러 응답 구조 확인
- 민감정보 로그 출력 금지
- 비동기 함수는 try / catch 사용
- 실패 시 fallback 값 고려

---

### [FAQ]

Q. catch에서 아무것도 안 해도 돼?

A.
안 된다. 최소한 실패 원인을 기록하거나 사용자에게 적절한 메시지를 제공해야 한다.

Q. throw는 언제 써?

A.
현재 함수에서 처리할 수 없는 오류를 호출한 쪽에서 처리하도록 전달할 때 사용한다.

---

# 13. Browser Debugging Rules

## 13.1 DevTools Debugging

### [개념]

Browser DevTools는 Frontend 코드 실행 상태를 확인하는 기본 도구다.

---

### [핵심]

필수 포함:

- Elements
- Console
- Network
- Sources
- Application
- localStorage
- sessionStorage
- breakpoints
- response status
- request payload

---

### [실무]

Debug Flow:

```text
UI Problem
→ Elements Check
→ Console Error Check
→ Network Request Check
→ Response Body Check
→ JavaScript Logic Check
→ Fix Code
```

API Debug Flow:

```text
Request Trigger
→ Network Tab
→ Request URL
→ Method
→ Headers
→ Payload
→ Status Code
→ Response Body
```

---

### [FAQ]

Q. JavaScript 오류는 어디서 확인해?

A.
브라우저 개발자 도구의 Console 탭에서 확인한다.

Q. API 요청 실패는 어디서 확인해?

A.
Network 탭에서 요청 URL, Method, Header, Payload, Status Code, Response Body를 확인한다.

Q. localStorage 값은 어디서 확인해?

A.
Application 탭에서 localStorage와 sessionStorage를 확인할 수 있다.

---

# 14. Frontend Practical Logic Rules

## 14.1 UI Logic Rules

### [개념]

UI Logic은 사용자 입력, 조건, 데이터 상태에 따라 화면 동작을 결정하는 코드다.

---

### [핵심]

필수 포함:

- loading
- error
- empty state
- success state
- conditional rendering logic
- form validation
- disabled condition
- list rendering
- data formatting

---

### [실무]

상태별 UI 판단 예:

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

실무 Flow:

```text
User Action
→ State Change
→ Data Fetch
→ Loading UI
→ Success / Empty / Error UI
```

---

### [FAQ]

Q. Empty State가 뭐야?

A.
데이터가 없을 때 사용자에게 보여주는 안내 상태다.

Q. Loading State는 왜 필요해?

A.
비동기 요청 중 사용자가 화면이 멈춘 것으로 오해하지 않게 하기 위해 필요하다.

Q. 버튼 disabled 조건은 어디서 계산해?

A.
입력값 유효성, 로딩 여부, 권한 상태 등을 기준으로 별도 함수나 변수로 계산하는 것이 좋다.

---

# 15. Security Rules

## 15.1 Frontend JavaScript Security Basics

### [개념]

Frontend JavaScript는 사용자 브라우저에서 실행되므로 민감정보 보호와 XSS 방어를 고려해야 한다.

---

### [핵심]

필수 포함:

- XSS
- innerHTML caution
- token handling
- localStorage caution
- input validation
- output escaping
- API key exposure
- sensitive log
- HTTPS
- CORS basics

---

### [실무]

주의:

- 사용자 입력을 innerHTML로 직접 삽입 금지
- API Key를 Frontend 코드에 하드코딩 금지
- JWT 로그 출력 금지
- 민감정보 localStorage 저장 주의
- Frontend 검증만 신뢰 금지
- Backend 검증 필수
- 공개 가능한 키와 비밀 키 구분

위험 예:

```javascript
element.innerHTML = userInput;
```

개선 예:

```javascript
element.textContent = userInput;
```

---

### [FAQ]

Q. Frontend 코드에 API Key를 넣어도 돼?

A.
공개되어도 되는 키가 아니라면 넣으면 안 된다. 브라우저 코드는 사용자에게 노출될 수 있다.

Q. innerHTML은 왜 위험해?

A.
사용자 입력이 그대로 들어가면 악성 스크립트가 실행될 수 있어 XSS 위험이 있다.

Q. Frontend 검증만 하면 안전해?

A.
아니다. Frontend 검증은 UX용이고 보안 검증은 Backend에서 반드시 수행해야 한다.

---

# 16. Code Example Rules

## 16.1 Example Style

### [개념]

JavaScript 예제는 짧고 직접적이어야 한다.

목적:

- Retrieval
- Code Generation
- Review
- Debugging
- React 전환 기반 제공

---

### [핵심]

권장:

- 핵심 로직만 포함
- 의미 있는 변수명 사용
- const / let 사용
- 실무형 예제 사용
- 배열 / 객체 / API 중심 예제
- 에러 처리 포함
- 불필요한 boilerplate 제거

금지:

- 긴 전체 프로젝트 코드
- var 중심 예제
- jQuery 예제
- 의미 없는 foo / bar 남용
- catch 비워두기
- API Key 하드코딩 예제
- DOM innerHTML 남용 예제

---

### [실무]

좋은 예:

```javascript
async function searchFestivals(keyword) {
  const query = keyword.trim();

  if (!query) {
    return [];
  }

  const response = await fetch(
    `/api/festivals/search?keyword=${encodeURIComponent(query)}`,
  );

  if (!response.ok) {
    throw new Error("Festival search failed");
  }

  return await response.json();
}
```

---

### [FAQ]

Q. JavaScript 예제 코드는 길수록 좋아?

A.
아니다. RAG 문서에서는 짧고 검색 가능한 실무 예제가 더 좋다.

Q. 예제에 에러 처리를 넣어야 해?

A.
API 호출, JSON 처리, 비동기 로직에는 에러 처리를 포함하는 것이 좋다.

---

# 17. Troubleshooting Rules

## 17.1 Undefined and Null Error

### [개념]

undefined와 null 관련 오류는 JavaScript 실무에서 자주 발생한다.

---

### [핵심]

문제:

- Cannot read properties of undefined
- Cannot read properties of null

원인:

- API 응답 도착 전 접근
- 중첩 객체 key 누락
- DOM 요소 선택 실패
- 초기값 누락
- 비동기 처리 순서 문제

해결:

- optional chaining 사용
- 기본값 지정
- null check
- loading state 처리
- DOM 요소 존재 여부 확인

---

### [실무]

예:

```javascript
const title = festival?.title ?? "제목 없음";
const items = response?.data?.content ?? [];
```

Debug Flow:

```text
Error Message Check
→ Variable Value Check
→ API Response Check
→ Null / Undefined Guard
→ Default Value Apply
```

---

### [FAQ]

Q. Cannot read properties of undefined는 왜 발생해?

A.
undefined인 값에서 property를 읽으려고 할 때 발생한다.

Q. 해결 방법은 뭐야?

A.
optional chaining, null check, 기본값 지정, 비동기 loading 처리로 방어한다.

---

## 17.2 Fetch Error

### [개념]

Fetch Error는 API 요청 과정에서 발생하는 오류다.

---

### [핵심]

문제:

- API 데이터가 안 불러와짐
- 404 / 500 응답 발생
- CORS 오류 발생
- JSON 파싱 오류 발생
- Network Error 발생

원인:

- URL 오타
- HTTP Method 불일치
- Header 누락
- Backend 서버 중단
- CORS 설정 문제
- response.ok 확인 누락
- JSON이 아닌 응답을 JSON으로 파싱

해결:

- Network 탭 확인
- Request URL 확인
- Method 확인
- Status Code 확인
- Response Body 확인
- response.ok 확인
- Content-Type 확인

---

### [실무]

Debug Flow:

```text
Network Tab
→ Request URL
→ Method
→ Headers
→ Payload
→ Status Code
→ Response Body
→ Frontend Error Handling
```

---

### [FAQ]

Q. fetch가 실패했을 때 어디를 봐야 해?

A.
브라우저 개발자 도구 Network 탭에서 URL, Method, Header, Payload, Status Code, Response Body를 확인한다.

Q. CORS 오류는 Frontend에서 고쳐?

A.
대부분 Backend CORS 설정 문제다. Frontend 요청 URL과 Header도 함께 확인해야 한다.

---

## 17.3 Async Order Problem

### [개념]

Async Order Problem은 비동기 작업 완료 전에 데이터를 사용해서 발생하는 문제다.

---

### [핵심]

문제:

- 데이터가 undefined로 출력됨
- API 응답 전 화면이 렌더링됨
- console.log 순서가 예상과 다름
- loading 처리 없이 빈 화면 표시

원인:

- Promise 대기 누락
- await 누락
- 비동기 함수 반환값 오해
- 상태 초기값 누락
- 비동기 실행 순서 오해

해결:

- await 사용
- then chain return 확인
- loading state 추가
- async function 반환값이 Promise임을 인지
- API 완료 후 UI 업데이트

---

### [실무]

나쁜 예:

```javascript
const data = fetchFestivals();
console.log(data);
```

좋은 예:

```javascript
const data = await fetchFestivals();
console.log(data);
```

---

### [FAQ]

Q. console.log가 예상보다 먼저 찍히는 이유는?

A.
비동기 작업이 완료되기 전에 다음 코드가 실행되기 때문이다.

Q. async 함수 결과를 바로 쓰면 왜 Promise가 나와?

A.
async function은 항상 Promise를 반환하기 때문이다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

JavaScript 문서는 헷갈리는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- var vs let vs const
- null vs undefined
- == vs ===
- function declaration vs arrow function
- map vs forEach
- filter vs find
- slice vs splice
- shallow copy vs deep copy
- Promise then/catch vs async/await
- localStorage vs sessionStorage
- textContent vs innerHTML
- event.target vs event.currentTarget
- named export vs default export

---

### [실무]

예시:

| 비교      | map                | forEach                   |
| --------- | ------------------ | ------------------------- |
| 목적      | 새 배열 생성       | 반복 실행                 |
| 반환값    | 새 배열            | undefined                 |
| 원본 변경 | 보통 변경하지 않음 | callback 내용에 따라 가능 |
| 적합      | 데이터 변환        | 로그, 실행, 부수효과      |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. JavaScript 비교 문서에서 가장 중요한 것은?

A.
실무 선택 기준과 오류 가능성을 함께 설명하는 것이다.

---

# 19. Checklist Rules

## 19.1 Document Quality Checklist

### [개념]

JavaScript 문서 검수 시 품질 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] JavaScript 기본 문법이 포함되었는가?
- [ ] Variable / Data Type 설명이 포함되었는가?
- [ ] Function / Scope / Closure 설명이 포함되었는가?
- [ ] Array / Object 처리 예제가 포함되었는가?
- [ ] DOM / Event Handling 기초가 포함되었는가?
- [ ] Promise / async / await 설명이 포함되었는가?
- [ ] Fetch API 예제가 포함되었는가?
- [ ] Error Handling 기준이 포함되었는가?
- [ ] Module / Import / Export가 포함되었는가?
- [ ] Browser DevTools Debugging이 포함되었는가?
- [ ] Security 주의사항이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Required Section Check
→ Example Check
→ Async Flow Check
→ API Example Check
→ Error Handling Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. JavaScript 문서 검수에서 가장 중요한 것은?

A.
Core Syntax, Array/Object, Function, Async, Fetch API, Error Handling, FAQ, Retrieval Queries 포함 여부다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

JavaScript Foundation 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- JavaScript
- JavaScript Foundation
- Frontend JavaScript
- Browser JavaScript
- Variable
- const
- let
- var
- Data Type
- null
- undefined
- Function
- Arrow Function
- Scope
- Closure
- Array
- Object
- map
- filter
- find
- reduce
- Destructuring
- Spread
- Rest
- DOM
- Event Handling
- addEventListener
- preventDefault
- Promise
- async
- await
- Fetch API
- JSON
- API Response
- Error Handling
- try catch
- Module
- import
- export
- Browser DevTools
- Frontend Debugging
- React Foundation

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- JavaScript 기본 문법 뭐부터 알아야 해?
- const let var 차이는?
- null undefined 차이는?
- == === 차이는?
- map forEach 차이는?
- filter find 차이는?
- Promise가 뭐야?
- async await 어떻게 써?
- fetch로 API 호출 어떻게 해?
- fetch 404인데 catch 안 타는 이유는?
- Cannot read properties of undefined 오류 왜 나?
- DOM이 뭐야?
- preventDefault 왜 써?
- event.target이 뭐야?
- JavaScript에서 API 응답 어떻게 처리해?
- React 하기 전에 JavaScript 뭐 알아야 해?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 21. Version Rules

## 21.1 Modern JavaScript 기준

### [개념]

JavaScript Foundation 문서는 Modern JavaScript 기준으로 작성한다.

---

### [핵심]

기준:

- ES6+
- const / let
- Arrow Function
- Template Literal
- Destructuring
- Spread / Rest
- Optional Chaining
- Nullish Coalescing
- Promise
- async / await
- Fetch API
- ES Module
- Browser DevTools
- React Readiness

Legacy 제외:

- var 중심 설명
- jQuery 중심 DOM 조작
- XMLHttpRequest 중심 API 호출
- callback hell 중심 예제
- 오래된 브라우저 polyfill 중심 설명
- document.write 사용
- eval 사용

---

### [실무]

실무 기준:

```text
Modern JavaScript
→ API Data Processing
→ Event Handling
→ Async Flow
→ Module Separation
→ React Ready Logic
```

---

### [FAQ]

Q. jQuery도 배워야 해?

A.
기존 프로젝트 유지보수에서는 볼 수 있지만 신규 Frontend Foundation에서는 Modern JavaScript와 React 기반을 우선한다.

Q. XMLHttpRequest도 다뤄야 해?

A.
기초적으로 존재만 알면 충분하고 API 호출 예제는 Fetch API 중심으로 작성한다.

---

# 22. Common Mistakes

## 22.1 JavaScript Common Mistakes

### [개념]

JavaScript Foundation 문서는 자주 발생하는 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- var 사용
- == 사용
- null / undefined 혼동
- 배열 원본 변경 실수
- sort 원본 변경 인지 못함
- map과 forEach 혼동
- filter와 find 혼동
- async function이 Promise 반환하는 것 오해
- await 누락
- fetch response.ok 확인 누락
- catch 비워두기
- API 응답 구조 확인 없이 접근
- Cannot read properties of undefined 오류
- DOM 요소 null 확인 누락
- event.preventDefault 누락
- innerHTML에 사용자 입력 삽입
- API Key 하드코딩
- console.log로 민감정보 출력
- 한 파일에 모든 로직 작성
- 함수 책임 과다

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: API 데이터가 undefined
원인: 비동기 응답 전 접근, 응답 구조 오해
해결: await, loading state, optional chaining, 기본값 적용
```

---

### [FAQ]

Q. JavaScript 초보가 가장 많이 하는 실수는?

A.
비동기 처리 오해, null/undefined 접근, 배열 원본 변경, fetch 에러 처리 누락이 많다.

Q. JavaScript 오류는 어떻게 찾는 게 좋아?

A.
Console Error, Network 요청, 변수 값, 비동기 실행 순서, API Response 구조를 순서대로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

JavaScript Foundation RAG 문서는 Frontend Agent가 화면 로직과 API 연동 기초 코드를 정확히 작성하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- JavaScript 기본 문법 이해
- Variable / Data Type 구분
- Condition / Loop 작성
- Function 작성
- Scope / Closure 이해
- Array / Object 데이터 처리
- Destructuring / Spread 사용
- DOM 구조 이해
- Event Handling 작성
- Form Handling 작성
- Promise 이해
- async / await 작성
- Fetch API 요청 작성
- JSON 처리
- API Response 가공
- Error Handling 적용
- Module 분리
- Browser Debugging 수행
- React 학습 전 JavaScript 기반 확보

---

### [실무]

Agent 수행 가능 작업:

```text
User UI Logic Request
→ JavaScript Function
→ Event Handling
→ Data Processing
→ API Request
→ Error Handling
→ React Ready Logic
```

---

### [FAQ]

Q. JavaScript Foundation 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 React 이전 단계의 화면 로직, 이벤트 처리, 비동기 API 연동, 데이터 가공 코드를 안정적으로 생성하고 검토하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
TypeScript Foundation, React Core, React Component Design, Data Fetching & REST API Integration 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Foundation 문서는 왜 필요해?
A. Frontend Agent가 React 화면 로직, 이벤트 처리, API 연동을 만들기 전에 JavaScript 기본 문법을 이해해야 하기 때문이다.

Q. JavaScript 기본 문법 뭐부터 알아야 해?
A. variable, data type, operator, condition, loop, function, array, object, async, fetch를 우선 알아야 한다.

Q. JavaScript는 어디에서 실행돼?
A. 브라우저와 Node.js에서 실행된다. Frontend 문서에서는 브라우저 JavaScript를 우선 다룬다.

Q. const let var 차이는?
A. const는 재할당 불가, let은 재할당 가능, var는 function scope와 hoisting 문제로 사용을 지양한다.

Q. var는 왜 피해야 해?
A. var는 function scope, 재선언, hoisting 때문에 예측하기 어려운 코드가 될 수 있다.

Q. const 객체는 수정할 수 있어?
A. const는 변수 재할당을 막지만 객체 내부 property 변경은 가능하다.

Q. null undefined 차이는?
A. undefined는 값이 할당되지 않은 상태이고 null은 의도적으로 값이 없음을 표현한 값이다.

Q. == === 차이는?
A. ==는 타입 변환 후 비교하고 ===는 타입과 값을 모두 비교한다. 실무에서는 ===를 권장한다.

Q. truthy falsy가 뭐야?
A. 조건문에서 true처럼 평가되는 값은 truthy, false처럼 평가되는 값은 falsy다.

Q. JavaScript falsy 값은 뭐야?
A. false, 0, -0, 0n, 빈 문자열, null, undefined, NaN이다.

Q. optional chaining은 왜 써?
A. 중첩 객체 접근 시 null 또는 undefined로 인한 오류를 줄이기 위해 사용한다.

Q. ??와 || 차이는?
A. ??는 null 또는 undefined일 때만 기본값을 사용하고, ||는 falsy 값 전체를 기본값으로 처리할 수 있다.

Q. function declaration과 arrow function 차이는?
A. function declaration은 hoisting되고 자체 this를 가지며, arrow function은 lexical this를 가진다.

Q. Arrow Function은 언제 써?
A. 짧은 callback, array method, 간단한 함수 표현에 자주 사용한다.

Q. Scope가 뭐야?
A. 변수와 함수에 접근할 수 있는 범위다.

Q. Closure가 뭐야?
A. 함수가 생성될 때의 외부 변수 환경을 기억하고 나중에도 접근할 수 있는 특성이다.

Q. Closure는 React와 관련 있어?
A. 관련 있다. Event Handler, Hook, 비동기 callback에서 closure 개념이 자주 등장한다.

Q. Array map은 언제 써?
A. 배열의 각 요소를 변환해 새 배열을 만들 때 사용한다.

Q. map과 forEach 차이는?
A. map은 새 배열을 반환하고 forEach는 반환값 없이 반복 작업만 수행한다.

Q. filter와 find 차이는?
A. filter는 조건에 맞는 모든 요소 배열을 반환하고 find는 첫 번째 요소 하나를 반환한다.

Q. reduce는 언제 써?
A. 배열을 하나의 값으로 누적 계산할 때 사용한다.

Q. sort는 원본 배열을 바꿔?
A. 바꾼다. 원본 변경을 피하려면 복사 후 sort를 사용한다.

Q. slice와 splice 차이는?
A. slice는 원본을 유지하고 일부를 반환하며, splice는 원본 배열을 변경한다.

Q. Object.keys는 언제 써?
A. 객체의 key 목록을 배열로 가져와 순회할 때 사용한다.

Q. Destructuring은 왜 써?
A. 객체나 배열에서 필요한 값을 간결하게 꺼내기 위해 사용한다.

Q. Spread는 깊은 복사야?
A. 아니다. Spread는 기본적으로 얕은 복사다.

Q. DOM이 뭐야?
A. HTML 문서를 JavaScript가 읽고 조작할 수 있도록 만든 객체 구조다.

Q. querySelector는 뭐야?
A. CSS selector와 일치하는 첫 번째 DOM 요소를 반환하는 메서드다.

Q. querySelector가 null을 반환하는 이유는?
A. 해당 selector와 일치하는 DOM 요소가 없기 때문이다.

Q. Event Handling이 뭐야?
A. 클릭, 입력, 제출 같은 사용자 행동에 반응하는 JavaScript 로직이다.

Q. preventDefault는 왜 써?
A. form 제출 시 페이지 새로고침 같은 브라우저 기본 동작을 막기 위해 사용한다.

Q. event.target은 뭐야?
A. 이벤트가 실제 발생한 요소다.

Q. event.currentTarget은 뭐야?
A. 이벤트 핸들러가 등록된 요소다.

Q. Event Bubbling이 뭐야?
A. 자식 요소에서 발생한 이벤트가 부모 요소 방향으로 전파되는 현상이다.

Q. Promise가 뭐야?
A. 비동기 작업의 완료 또는 실패 결과를 나중에 처리하기 위한 객체다.

Q. Promise 상태는 뭐가 있어?
A. pending, fulfilled, rejected 상태가 있다.

Q. async await는 왜 써?
A. Promise 기반 비동기 코드를 동기 코드처럼 읽기 쉽게 작성하기 위해 사용한다.

Q. async function은 뭘 반환해?
A. 항상 Promise를 반환한다.

Q. await는 어디서 써?
A. 일반적으로 async function 내부에서 Promise 결과를 기다릴 때 사용한다.

Q. fetch로 API 호출 어떻게 해?
A. fetch로 요청을 보내고 response.ok를 확인한 뒤 response.json으로 응답을 파싱한다.

Q. fetch는 404에서 catch로 바로 가?
A. 아니다. HTTP 오류 상태는 자동 reject되지 않으므로 response.ok를 확인해야 한다.

Q. POST 요청에서 JSON body는 어떻게 보내?
A. headers에 Content-Type application/json을 설정하고 body에 JSON.stringify 결과를 넣는다.

Q. API 요청에 JWT는 어디에 넣어?
A. 일반적으로 Authorization Header에 Bearer Token 형식으로 넣는다.

Q. JSON.stringify는 언제 써?
A. JavaScript 객체를 JSON 문자열로 변환해 API request body로 보낼 때 사용한다.

Q. JSON.parse는 언제 써?
A. JSON 문자열을 JavaScript 객체로 변환할 때 사용한다.

Q. API 응답이 null일 수 있으면 어떻게 해?
A. optional chaining과 nullish coalescing으로 기본값을 지정한다.

Q. Cannot read properties of undefined 오류는 왜 발생해?
A. undefined인 값에서 property를 읽으려고 할 때 발생한다.

Q. Cannot read properties of undefined는 어떻게 해결해?
A. optional chaining, null check, 기본값 지정, loading state 처리로 해결한다.

Q. JavaScript 오류는 어디서 확인해?
A. 브라우저 개발자 도구 Console 탭에서 확인한다.

Q. API 요청 실패는 어디서 확인해?
A. Network 탭에서 요청 URL, Method, Header, Payload, Status Code, Response Body를 확인한다.

Q. localStorage와 sessionStorage 차이는?
A. localStorage는 브라우저에 지속 저장되고 sessionStorage는 탭 세션 동안 유지된다.

Q. innerHTML은 왜 위험해?
A. 사용자 입력이 그대로 들어가면 악성 스크립트가 실행될 수 있어 XSS 위험이 있다.

Q. textContent와 innerHTML 차이는?
A. textContent는 텍스트로 처리하고 innerHTML은 HTML로 파싱한다.

Q. Frontend 코드에 API Key를 넣어도 돼?
A. 공개되어도 되는 키가 아니라면 넣으면 안 된다. 브라우저 코드는 사용자에게 노출될 수 있다.

Q. named export와 default export 차이는?
A. named export는 이름을 맞춰 import하고 default export는 원하는 이름으로 import할 수 있다.

Q. React 하기 전에 JavaScript 뭐 알아야 해?
A. const/let, function, array/object, destructuring, spread, event, async/await, fetch, module을 알아야 한다.

Q. JavaScript Foundation 다음 문서는 뭐가 좋아?
A. TypeScript Foundation, React Core, React Component Design, Data Fetching & REST API Integration 순서가 좋다.
