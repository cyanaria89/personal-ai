# JavaScript Foundation Part01 - Basic Syntax

---

# 1. JavaScript Basic Syntax

## 1.1 JavaScript Foundation Purpose

### [개념]

JavaScript Foundation은 Frontend Agent가 Browser 기반 화면 로직, Event Handling, API 연동, React 전환 전 기본 코드를 생성하고 검토하기 위한 기초 문법 문서다.

이 문서는 사람 학습용 문서가 아니라 AI Agent Retrieval, Code Generation, Review, Debugging을 위한 RAG 문서다.

JavaScript는 Browser와 Node.js에서 실행될 수 있지만, Frontend Foundation 문서에서는 Browser JavaScript를 우선 기준으로 한다.

---

### [핵심]

- JavaScript Foundation
- Frontend JavaScript
- Browser JavaScript
- Basic Syntax
- Statement
- Expression
- Variable
- Data Type
- Function
- Object
- Array
- DOM
- Event Handling
- Promise
- async / await
- Fetch API
- React Foundation Readiness

---

### [실무]

2026 실무 기준에서 JavaScript Foundation은 단순 문법 암기가 아니다.

Frontend Agent는 JavaScript Foundation을 기반으로 아래 작업을 수행해야 한다.

- UI 상태 계산
- 사용자 입력 처리
- Event Handler 작성
- Array / Object 데이터 가공
- API Response 처리
- Fetch API 요청 작성
- 비동기 처리 흐름 분석
- Browser DevTools 기반 오류 분석
- React Component 로직 이해
- TypeScript 전환 전 기본 문법 확보

JavaScript Foundation 문서는 다음 Frontend 문서의 선행 지식이다.

```text
HTML CSS Foundation
→ JavaScript Foundation
→ TypeScript Foundation
→ React Core
→ React Component Design
→ Data Fetching REST API Integration
```

---

### [FAQ]

Q. JavaScript Foundation 문서는 왜 필요해?
A. Frontend Agent가 React 화면 로직, 이벤트 처리, API 연동 코드를 생성하기 전에 JavaScript 기본 문법을 이해해야 하기 때문이다.

Q. 이 문서는 사람 공부용이야?
A. 아니다. AI Agent가 검색, 이해, 코드 생성, 검토, 디버깅에 활용하기 위한 RAG 문서다.

Q. JavaScript Foundation에서 가장 중요한 범위는 뭐야?
A. 변수, 자료형, 조건문, 반복문, 함수, 배열, 객체, DOM, Event, Promise, async / await, Fetch API다.

Q. React를 배울 건데 JavaScript가 왜 중요해?
A. React Component, Event, State Update, API 호출은 모두 JavaScript 문법과 비동기 처리 위에서 동작한다.

---

# 2. JavaScript Execution Environment

## 2.1 Browser JavaScript

### [개념]

Browser JavaScript는 웹 브라우저에서 실행되는 JavaScript다.

Browser JavaScript는 HTML, CSS, DOM, Event, Fetch API와 연결되어 사용자 화면을 동적으로 제어한다.

예:

```javascript
const titleElement = document.querySelector(".page-title");

titleElement.textContent = "Festival List";
```

---

### [핵심]

- Browser JavaScript
- document
- window
- DOM
- Event
- Fetch API
- localStorage
- sessionStorage
- Console
- Network
- Frontend Logic

---

### [실무]

Frontend Agent는 JavaScript를 Browser 중심으로 이해해야 한다.

Browser JavaScript 실무 연결:

```text
User Action
→ Event Handler
→ JavaScript Logic
→ API Request
→ DOM Update or React State Update
→ UI Change
```

주의:

- Browser 코드는 사용자에게 노출될 수 있다.
- 민감정보를 JavaScript 코드에 하드코딩하면 안 된다.
- API Key, JWT, 개인정보를 console.log로 출력하면 안 된다.
- DOM 요소는 null일 수 있으므로 접근 전 확인이 필요하다.
- React에서는 직접 DOM 조작보다 state 기반 렌더링을 우선한다.

---

### [FAQ]

Q. JavaScript는 어디에서 실행돼?
A. JavaScript는 Browser와 Node.js에서 실행된다. Frontend Foundation에서는 Browser JavaScript를 우선 다룬다.

Q. Browser JavaScript는 무엇을 제어해?
A. HTML 문서, DOM 요소, 사용자 이벤트, API 요청, 브라우저 저장소 등을 제어한다.

Q. Browser JavaScript에서 민감정보를 숨길 수 있어?
A. 어렵다. 브라우저 코드는 사용자에게 노출될 수 있으므로 비밀 키나 민감정보를 포함하면 안 된다.

---

## 2.2 Node.js와 Frontend Foundation 구분

### [개념]

Node.js는 JavaScript를 브라우저 밖에서 실행할 수 있게 하는 Runtime이다.

JavaScript Foundation 문서에서는 Node.js Backend 심화가 아니라 Frontend Browser JavaScript를 우선 다룬다.

---

### [핵심]

- Browser JavaScript
- Node.js
- Runtime
- Frontend Foundation
- Backend JavaScript 제외
- DOM 중심
- Event 중심
- Fetch API 중심

---

### [실무]

Frontend Foundation에서 Node.js는 깊게 다루지 않는다.

구분:

| 구분         | Browser JavaScript  | Node.js                  |
| ------------ | ------------------- | ------------------------ |
| 실행 위치    | 웹 브라우저         | 서버 또는 로컬 런타임    |
| 주요 객체    | window, document    | process, fs              |
| 주요 목적    | UI, Event, API 연동 | 서버, 파일, CLI, Backend |
| 본 문서 기준 | 포함                | 심화 제외                |

Frontend Agent는 Browser JavaScript를 기준으로 DOM, Event, Fetch API, React Ready Logic을 우선 생성해야 한다.

---

### [FAQ]

Q. JavaScript Foundation에서 Node.js도 깊게 다뤄?
A. 아니다. 이 문서는 Frontend Foundation 목적이므로 Browser JavaScript 중심으로 작성한다.

Q. Node.js 문법과 Browser JavaScript 문법은 완전히 달라?
A. 기본 JavaScript 문법은 같지만 사용할 수 있는 API와 실행 환경이 다르다.

Q. Frontend Agent는 어떤 JavaScript를 우선해야 해?
A. Browser JavaScript, DOM, Event, Fetch API, API Response 처리 중심으로 우선해야 한다.

---

# 3. Statement and Expression

## 3.1 Statement

### [개념]

Statement는 JavaScript에서 실행 가능한 명령문이다.

Statement는 변수 선언, 조건문, 반복문, 함수 선언처럼 프로그램의 동작을 구성한다.

예:

```javascript
const title = "Festival";

if (title) {
  console.log(title);
}
```

---

### [핵심]

- Statement
- Declaration
- Assignment
- Condition
- Loop
- Function Declaration
- Execution Flow
- Semicolon

---

### [실무]

JavaScript 문서에서는 Statement를 이론적으로 장황하게 설명하지 않는다.

Frontend 실무에서는 Statement를 아래 흐름으로 이해한다.

```text
Variable Declaration
→ Condition Check
→ Function Call
→ API Request
→ UI Update
```

예:

```javascript
const keyword = input.value.trim();

if (!keyword) {
  showError("검색어를 입력하세요.");
}
```

주의:

- 한 Statement에는 하나의 의도를 담는 것이 좋다.
- 복잡한 조건문은 함수로 분리한다.
- 긴 Statement는 가독성을 떨어뜨린다.
- 불필요한 한 줄 압축 코드는 Review Agent가 지적해야 한다.

---

### [FAQ]

Q. Statement가 뭐야?
A. JavaScript에서 실행되는 하나의 명령문이다.

Q. 변수 선언도 Statement야?
A. 맞다. `const title = "Festival";` 같은 변수 선언도 Statement다.

Q. Statement를 짧게 작성해야 하는 이유는?
A. 코드 생성, 리뷰, 디버깅, 유지보수가 쉬워지기 때문이다.

---

## 3.2 Expression

### [개념]

Expression은 하나의 값으로 평가되는 코드 조각이다.

예:

```javascript
const total = price * count;
const isValid = keyword.trim().length > 0;
const displayName = user?.name ?? "Guest";
```

`price * count`, `keyword.trim().length > 0`, `user?.name ?? "Guest"`는 모두 Expression이다.

---

### [핵심]

- Expression
- Value
- Evaluation
- Operator
- Function Call
- Boolean Expression
- Ternary Operator
- Optional Chaining
- Nullish Coalescing

---

### [실무]

Frontend 실무에서는 Expression을 UI 상태 계산에 자주 사용한다.

예:

```javascript
const isSubmitDisabled = keyword.trim().length === 0 || loading;
```

조건부 값 선택:

```javascript
const buttonText = loading ? "처리 중..." : "검색";
```

안전한 기본값 처리:

```javascript
const festivals = response?.data?.content ?? [];
```

주의:

- 복잡한 Expression은 변수나 함수로 분리한다.
- 중첩 삼항 연산자는 피한다.
- optional chaining과 nullish coalescing을 사용해 null / undefined 오류를 줄인다.
- UI 조건은 의미 있는 변수명으로 분리한다.

---

### [FAQ]

Q. Expression이 뭐야?
A. 하나의 값으로 평가되는 코드 조각이다.

Q. 조건문 안의 비교식도 Expression이야?
A. 맞다. `age >= 20` 같은 비교식은 boolean 값으로 평가되는 Expression이다.

Q. Expression을 변수로 분리하는 이유는?
A. 조건의 의미가 명확해지고 코드 리뷰와 디버깅이 쉬워지기 때문이다.

---

# 4. Semicolon and Code Style

## 4.1 Semicolon

### [개념]

Semicolon은 JavaScript Statement의 끝을 표시하는 기호다.

JavaScript는 Automatic Semicolon Insertion을 지원하지만, RAG 문서의 예제 코드는 일관성을 위해 Semicolon을 사용하는 방식으로 작성한다.

예:

```javascript
const title = "Festival";
const count = 3;

console.log(title, count);
```

---

### [핵심]

- Semicolon
- Statement End
- Automatic Semicolon Insertion
- Code Style
- Consistency
- Formatting
- Prettier
- ESLint

---

### [실무]

2026 실무 기준에서는 팀 컨벤션과 Formatter 설정을 따른다.

RAG 문서 예제에서는 다음 기준을 권장한다.

- Semicolon 사용
- const / let 사용
- var 사용 지양
- 들여쓰기 2칸
- 의미 있는 변수명 사용
- 불필요한 한 줄 압축 금지
- Prettier / ESLint 기준과 충돌하지 않게 작성

권장:

```javascript
const festivalTitle = "Spring Festival";
const isActive = true;

if (isActive) {
  console.log(festivalTitle);
}
```

비권장:

```javascript
var x = "Spring Festival";
if (x) console.log(x);
```

---

### [FAQ]

Q. JavaScript에서 Semicolon은 꼭 써야 해?
A. 팀 컨벤션에 따라 다르지만 RAG 문서 예제에서는 일관성을 위해 Semicolon 사용을 권장한다.

Q. Automatic Semicolon Insertion이 뭐야?
A. JavaScript 엔진이 필요한 위치에 Semicolon을 자동으로 삽입하는 동작이다.

Q. 예제 코드에서 가장 중요한 스타일 기준은 뭐야?
A. 짧고 직접적이며, const / let을 사용하고, 의미 있는 변수명과 일관된 Formatting을 유지하는 것이다.

---

# 5. Comment Rules

## 5.1 JavaScript Comment

### [개념]

Comment는 코드 실행에 영향을 주지 않는 설명이다.

JavaScript에서는 한 줄 주석과 여러 줄 주석을 사용할 수 있다.

예:

```javascript
// 축제 제목을 화면에 출력한다.
const title = "Spring Festival";

/*
  여러 줄 설명이 필요한 경우
  block comment를 사용할 수 있다.
*/
```

---

### [핵심]

- Comment
- Single Line Comment
- Block Comment
- Intent
- Warning
- TODO
- Code Explanation
- Review Support

---

### [실무]

실무 코드에서 Comment는 코드가 설명하지 못하는 의도를 보완할 때 사용한다.

좋은 Comment:

```javascript
// API 응답이 null인 경우 빈 배열로 처리해 화면 오류를 방지한다.
const festivals = response?.data?.content ?? [];
```

나쁜 Comment:

```javascript
// title 변수 선언
const title = "Festival";
```

Comment 작성 기준:

- 코드 그대로를 반복하지 않는다.
- 의도, 주의사항, 예외 조건을 설명한다.
- 오래된 Comment는 제거한다.
- TODO는 작업 목적이 명확해야 한다.
- 민감정보를 Comment에 남기지 않는다.

---

### [FAQ]

Q. Comment는 많을수록 좋아?
A. 아니다. 코드로 충분히 이해되는 내용은 Comment가 필요 없다.

Q. 좋은 Comment는 뭐야?
A. 코드가 왜 그렇게 작성되었는지, 어떤 예외나 주의가 있는지를 설명하는 Comment다.

Q. Comment에 API Key를 적어도 돼?
A. 안 된다. Comment도 코드와 함께 노출되거나 저장소에 올라갈 수 있다.

---

# 6. Basic Syntax Example

## 6.1 Frontend Basic Logic Example

### [개념]

JavaScript Basic Syntax는 변수 선언, 조건문, 함수, 배열 처리, API 호출 같은 실무 로직으로 연결되어야 한다.

RAG 문서의 예제는 단순 문법보다 Frontend Agent가 실제 코드 생성에 활용할 수 있는 형태를 우선한다.

---

### [핵심]

- const
- let
- if
- function
- array
- object
- map
- filter
- async
- await
- fetch
- error handling
- return
- UI Logic

---

### [실무]

Frontend Basic Logic 예:

```javascript
function normalizeKeyword(keyword) {
  return keyword.trim();
}

function isValidKeyword(keyword) {
  return normalizeKeyword(keyword).length > 0;
}

async function searchFestivals(keyword) {
  const query = normalizeKeyword(keyword);

  if (!isValidKeyword(query)) {
    return [];
  }

  const response = await fetch(
    `/api/festivals/search?keyword=${encodeURIComponent(query)}`,
  );

  if (!response.ok) {
    throw new Error("Festival search failed");
  }

  const data = await response.json();

  return data?.content ?? [];
}
```

이 예제의 목적:

- 입력값 trim
- 유효성 검증
- Guard Clause
- Fetch API 요청
- response.ok 확인
- JSON 응답 처리
- null / undefined 기본값 처리
- API Response를 배열로 반환

---

### [FAQ]

Q. JavaScript 예제는 길수록 좋아?
A. 아니다. RAG 문서에서는 짧고 검색 가능한 실무형 예제가 더 좋다.

Q. Basic Syntax 예제에 API 호출을 넣어도 돼?
A. 가능하다. Frontend Foundation에서는 문법이 실제 API 연동으로 이어지는 예제가 좋다.

Q. 왜 response.ok를 확인해?
A. fetch는 404나 500 같은 HTTP 오류를 자동 reject하지 않기 때문에 직접 확인해야 한다.

Q. 왜 data?.content ?? []를 사용해?
A. API 응답 구조가 없거나 null일 때 빈 배열로 처리해 화면 오류를 방지하기 위해서다.

---

# 7. Basic Syntax Common Mistakes

## 7.1 Common Mistakes

### [개념]

JavaScript Basic Syntax 단계에서 발생하는 실수는 이후 React, API 연동, 상태 관리 오류로 이어질 수 있다.

RAG 문서에서는 자주 발생하는 실수를 명확히 포함해 Review Agent가 검출할 수 있어야 한다.

---

### [핵심]

자주 발생하는 실수:

- var 사용
- 의미 없는 변수명 사용
- == 사용
- Semicolon / Formatting 불일치
- null / undefined 방어 누락
- 조건문 중첩 과다
- 복잡한 Expression 방치
- 함수 책임 과다
- API 응답 구조 확인 없이 접근
- fetch response.ok 확인 누락
- catch 비워두기
- console.log로 민감정보 출력
- Comment에 민감정보 작성
- Browser 코드에 비밀 키 하드코딩

---

### [실무]

Review Agent는 다음 기준으로 Basic Syntax를 검토한다.

```text
Code Review
→ const / let 사용 확인
→ var 사용 여부 확인
→ == 사용 여부 확인
→ null / undefined 방어 확인
→ 함수 책임 확인
→ API 응답 구조 확인
→ response.ok 확인
→ 민감정보 노출 확인
→ Formatting 확인
```

나쁜 예:

```javascript
var data = response.data.content;
console.log(token);
```

개선 예:

```javascript
const festivals = response?.data?.content ?? [];
```

주의:

- `var`는 function scope와 hoisting 문제로 지양한다.
- `==` 대신 `===`를 사용한다.
- API 응답은 항상 null / undefined 가능성을 고려한다.
- 민감정보는 console.log로 출력하지 않는다.
- Browser JavaScript에 비밀 키를 넣지 않는다.

---

### [FAQ]

Q. JavaScript 초보가 가장 많이 하는 실수는 뭐야?
A. var 사용, == 사용, null / undefined 접근, API 응답 구조 오해, fetch 에러 처리 누락이 많다.

Q. Basic Syntax 단계에서 보안도 봐야 해?
A. 봐야 한다. Browser JavaScript는 사용자에게 노출되므로 민감정보 하드코딩과 로그 출력은 금지해야 한다.

Q. Review Agent는 Basic Syntax에서 무엇을 우선 검토해야 해?
A. const / let 사용, strict equality, null 방어, 함수 책임, API 응답 처리, 민감정보 노출 여부를 우선 검토한다.

---

# 8. Basic Syntax Checklist

## 8.1 Document Quality Checklist

### [개념]

JavaScript Basic Syntax 문서는 Frontend Agent가 기본 문법을 검색하고 코드 생성에 활용할 수 있도록 검수되어야 한다.

Checklist는 RAG 문서 품질과 Agent Retrieval 성능을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] JavaScript Foundation 목적이 명확한가?
- [ ] Browser JavaScript 기준이 명확한가?
- [ ] Node.js 심화와 구분되는가?
- [ ] Statement 설명이 포함되었는가?
- [ ] Expression 설명이 포함되었는가?
- [ ] Semicolon / Code Style 기준이 포함되었는가?
- [ ] Comment 사용 기준이 포함되었는가?
- [ ] Frontend 실무 예제가 포함되었는가?
- [ ] Fetch API 연결 가능성이 포함되었는가?
- [ ] null / undefined 방어 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] Review Agent 검토 기준이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?

---

### [실무]

검수 Flow:

```text
Draft
→ MASTER_RAG_RULES Section Check
→ JavaScript Domain Scope Check
→ Frontend Practical Example Check
→ FAQ Check
→ Retrieval Query Check
→ File Connection Check
→ Final Review
```

파일 간 연계:

```text
Master_RAG_Rules
→ JavaScript_Foundation_Domain_Rules
→ JavaScript_Foundation_Part01_Basic_Syntax
→ JavaScript_Foundation_Part02_Variable_Data_Type
```

---

### [FAQ]

Q. Basic Syntax 문서 검수에서 가장 중요한 것은 뭐야?
A. Browser JavaScript 기준, Frontend 실무 예제, FAQ, Retrieval Queries, Common Mistakes 포함 여부다.

Q. 문서가 사람에게 읽기 좋으면 충분해?
A. 아니다. RAG Retrieval, Agent Code Generation, Review 정확도를 우선해야 한다.

Q. 다음 Part와 어떻게 연결돼?
A. Part01은 Basic Syntax 기준을 만들고, Part02는 Variable과 Data Type으로 확장된다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Foundation 문서는 왜 필요해?
A. Frontend Agent가 화면 로직, 이벤트 처리, API 연동 코드를 생성하기 전에 JavaScript 기본 문법을 이해해야 하기 때문이다.

Q. JavaScript Basic Syntax는 뭐야?
A. Statement, Expression, Variable, Data Type, Operator, Condition, Loop, Function 같은 기본 문법이다.

Q. JavaScript는 어디에서 실행돼?
A. JavaScript는 Browser와 Node.js에서 실행된다. Frontend Foundation에서는 Browser JavaScript를 우선 다룬다.

Q. Browser JavaScript는 뭐야?
A. 웹 브라우저에서 실행되며 DOM, Event, Fetch API를 사용해 화면과 사용자 동작을 제어하는 JavaScript다.

Q. Node.js도 JavaScript Foundation에서 다뤄?
A. 깊게 다루지 않는다. 이 문서는 Frontend Foundation 목적이므로 Browser JavaScript 중심이다.

Q. Statement가 뭐야?
A. JavaScript에서 실행되는 하나의 명령문이다.

Q. Expression이 뭐야?
A. 하나의 값으로 평가되는 코드 조각이다.

Q. Statement와 Expression 차이는?
A. Statement는 실행 명령이고 Expression은 값으로 평가되는 코드 조각이다.

Q. JavaScript에서 Semicolon은 꼭 필요해?
A. 팀 컨벤션에 따라 다르지만 RAG 예제에서는 일관성을 위해 Semicolon 사용을 권장한다.

Q. Automatic Semicolon Insertion이 뭐야?
A. JavaScript 엔진이 필요한 위치에 Semicolon을 자동으로 삽입하는 동작이다.

Q. JavaScript Comment는 언제 써?
A. 코드가 설명하지 못하는 의도, 예외, 주의사항을 설명할 때 사용한다.

Q. Comment는 많을수록 좋아?
A. 아니다. 코드와 중복되는 Comment는 줄이고 의도와 주의사항 중심으로 작성해야 한다.

Q. JavaScript 기본 예제는 어떻게 작성해야 해?
A. 짧고 직접적이며 const / let, 조건문, 함수, API 응답 처리, 에러 처리를 포함하는 실무형 예제가 좋다.

Q. JavaScript에서 var는 왜 피해야 해?
A. var는 function scope, 재선언, hoisting 문제로 예측하기 어려운 코드가 될 수 있기 때문이다.

Q. == 대신 ===를 쓰는 이유는?
A. ===는 타입과 값을 모두 비교하므로 예측 가능한 비교가 가능하기 때문이다.

Q. API 응답 처리에서 optional chaining은 왜 필요해?
A. 응답 구조가 없거나 null / undefined일 때 property 접근 오류를 줄이기 위해 필요하다.

Q. data?.content ?? []는 왜 써?
A. API 응답에 content가 없을 때 빈 배열을 기본값으로 사용해 화면 오류를 방지하기 위해 쓴다.

Q. fetch에서 response.ok를 확인해야 하는 이유는?
A. fetch는 404나 500 같은 HTTP 오류를 자동 reject하지 않기 때문에 직접 확인해야 한다.

Q. Browser JavaScript에 API Key를 하드코딩해도 돼?
A. 공개되어도 되는 키가 아니라면 안 된다. 브라우저 코드는 사용자에게 노출될 수 있다.

Q. console.log로 JWT를 출력해도 돼?
A. 안 된다. JWT, 개인정보, API Key 같은 민감정보는 로그로 출력하면 안 된다.

Q. Basic Syntax 문서 다음에는 무엇을 다뤄야 해?
A. Variable, Data Type, Operator, Condition, Loop, Function 순서로 확장하는 것이 좋다.

Q. JavaScript Foundation은 React와 어떻게 연결돼?
A. React Component, Event, State Update, API 호출은 JavaScript 문법과 비동기 처리 기반으로 동작한다.

Q. Review Agent는 Basic Syntax에서 무엇을 검토해야 해?
A. const / let 사용, var 사용 여부, strict equality, null 방어, 함수 책임, API 응답 처리, 민감정보 노출 여부를 검토해야 한다.
