# JavaScript Foundation Part02 - Variable and Data Type

---

# 1. Variable

## 1.1 Variable Concept

### [개념]

Variable은 값을 저장하고 참조하기 위한 이름이다.

JavaScript에서는 `const`, `let`, `var`를 사용해 변수를 선언할 수 있다.

Frontend JavaScript에서는 기본적으로 `const`를 우선 사용하고, 값 재할당이 필요한 경우에만 `let`을 사용한다.

예:

```javascript
const title = "Spring Festival";
let currentPage = 1;

currentPage += 1;
```

---

### [핵심]

- Variable
- const
- let
- var
- declaration
- assignment
- reassignment
- block scope
- function scope
- hoisting
- temporal dead zone
- naming
- Frontend State Logic

---

### [실무]

2026 실무 기준에서 Frontend JavaScript 변수 선언은 안정성과 예측 가능성을 우선한다.

권장 기준:

- 기본은 `const`
- 재할당이 필요한 경우만 `let`
- `var` 사용 지양
- 의미 있는 변수명 사용
- 축약어 남용 금지
- UI 상태와 API 응답 변수명 구분
- boolean 값은 `is`, `has`, `can`, `should` 접두사 권장

권장:

```javascript
const festivalTitle = "Spring Festival";
const isLoggedIn = true;
const festivals = [];

let currentPage = 1;
```

비권장:

```javascript
var x = "Spring Festival";
var flag = true;
```

Frontend Agent는 변수명을 통해 코드 의도가 검색되고 이해될 수 있도록 작성해야 한다.

---

### [FAQ]

Q. Variable이 뭐야?
A. 값을 저장하고 나중에 참조하기 위한 이름이다.

Q. JavaScript에서는 변수를 어떻게 선언해?
A. `const`, `let`, `var`로 선언할 수 있다.

Q. 실무에서는 어떤 변수 선언을 우선해?
A. 기본은 `const`를 사용하고, 재할당이 필요한 경우에만 `let`을 사용한다.

Q. var는 왜 피해야 해?
A. function scope, 재선언, hoisting 문제로 예측하기 어려운 코드가 될 수 있기 때문이다.

---

# 2. const

## 2.1 const Rules

### [개념]

`const`는 재할당할 수 없는 변수를 선언할 때 사용한다.

`const`로 선언한 변수는 같은 Scope 안에서 다시 값을 할당할 수 없다.

예:

```javascript
const serviceName = "FestaPick";
```

재할당은 불가능하다.

```javascript
const serviceName = "FestaPick";

serviceName = "New Service"; // Error
```

---

### [핵심]

- const
- no reassignment
- block scope
- declaration with initialization
- immutable binding
- object mutation caution
- array mutation caution
- default variable declaration

---

### [실무]

Frontend JavaScript에서는 `const`를 기본 선언 방식으로 사용한다.

이유:

- 의도하지 않은 재할당 방지
- 코드 흐름 예측 가능
- Review Agent가 상태 변경 지점을 쉽게 추적
- 함수형 데이터 처리와 잘 맞음
- React State Update 전환 시 사고방식이 유사함

권장:

```javascript
const userName = "jun";
const maxPageSize = 20;
const apiBaseUrl = "/api/festivals";
```

주의:

`const`는 변수 재할당을 막지만, 객체와 배열의 내부 변경까지 막지는 않는다.

```javascript
const user = {
  id: 1,
  name: "jun",
};

user.name = "newName"; // 가능
```

배열도 내부 변경은 가능하다.

```javascript
const festivals = [];

festivals.push({
  id: 1,
  title: "Spring Festival",
}); // 가능
```

Frontend Agent는 객체와 배열을 다룰 때 원본 변경 여부를 명확히 판단해야 한다.

---

### [FAQ]

Q. const는 어떤 때 써?
A. 재할당하지 않을 값을 선언할 때 사용한다. 실무에서는 기본 변수 선언으로 사용한다.

Q. const 변수는 값을 바꿀 수 없어?
A. 변수 재할당은 불가능하지만 객체나 배열 내부 값 변경은 가능하다.

Q. const 객체는 완전히 불변이야?
A. 아니다. const는 binding 재할당을 막을 뿐 객체 내부 property 변경은 막지 않는다.

Q. const 배열에 push를 할 수 있어?
A. 가능하다. 배열 변수 자체를 다른 배열로 재할당하는 것은 불가능하지만 내부 변경은 가능하다.

---

# 3. let

## 3.1 let Rules

### [개념]

`let`은 재할당이 필요한 변수를 선언할 때 사용한다.

`let`은 block scope를 가지며, 같은 Scope 안에서 재선언할 수 없다.

예:

```javascript
let currentPage = 1;

currentPage += 1;
```

---

### [핵심]

- let
- reassignment
- block scope
- no redeclaration in same scope
- loop variable
- mutable state
- temporary variable

---

### [실무]

`let`은 값이 실제로 바뀌는 경우에만 사용한다.

적합한 경우:

- pagination page 변경
- loop counter
- 조건에 따라 값이 갱신되는 임시 변수
- 누적 계산
- 사용자 입력 후 가공되는 값

예:

```javascript
let currentPage = 1;

function moveNextPage() {
  currentPage += 1;
}
```

조건에 따라 값 변경:

```javascript
let message = "기본 메시지";

if (isLoggedIn) {
  message = "환영합니다.";
}
```

주의:

- 재할당이 필요 없다면 `const`를 사용한다.
- `let`을 남용하면 상태 변경 추적이 어려워진다.
- 여러 곳에서 `let` 값을 변경하면 디버깅이 어려워진다.
- React 코드로 전환할 경우 mutable variable보다 state 관리가 필요할 수 있다.

---

### [FAQ]

Q. let은 언제 써?
A. 값 재할당이 필요한 변수에 사용한다.

Q. const와 let 중 무엇을 먼저 고려해?
A. 먼저 const를 고려하고, 재할당이 필요할 때만 let을 사용한다.

Q. let도 block scope야?
A. 맞다. let은 `{}` block 내부에서만 유효한 block scope를 가진다.

Q. let을 많이 쓰면 왜 안 좋아?
A. 값 변경 지점이 많아져 코드 흐름과 오류 원인을 추적하기 어려워질 수 있다.

---

# 4. var

## 4.1 var Avoidance Rules

### [개념]

`var`는 오래된 JavaScript 변수 선언 방식이다.

`var`는 function scope를 가지며, 재선언이 가능하고 hoisting 동작으로 인해 예측하기 어려운 코드가 될 수 있다.

예:

```javascript
var userName = "jun";
var userName = "kim";
```

---

### [핵심]

- var
- function scope
- redeclaration
- hoisting
- avoid var
- unpredictable flow
- legacy JavaScript
- Modern JavaScript

---

### [실무]

Modern JavaScript와 Frontend Foundation 문서에서는 `var` 사용을 지양한다.

`var`를 피해야 하는 이유:

- function scope로 인해 block scope와 다르게 동작
- 같은 Scope에서 재선언 가능
- hoisting으로 선언 전 접근 가능
- 의도하지 않은 값 덮어쓰기 발생 가능
- Review와 Debugging이 어려움

비권장:

```javascript
if (isLoggedIn) {
  var message = "환영합니다.";
}

console.log(message);
```

권장:

```javascript
if (isLoggedIn) {
  const message = "환영합니다.";
  console.log(message);
}
```

Review Agent는 `var` 사용을 발견하면 `const` 또는 `let` 전환을 우선 권장해야 한다.

---

### [FAQ]

Q. var는 왜 피해야 해?
A. function scope, 재선언, hoisting 때문에 예측하기 어려운 코드가 될 수 있기 때문이다.

Q. var를 쓰면 무조건 오류야?
A. 오류는 아니지만 Modern JavaScript 실무에서는 const와 let 사용을 권장한다.

Q. 기존 코드에 var가 있으면 어떻게 해?
A. 재할당 여부를 확인한 뒤 가능하면 const 또는 let으로 전환한다.

Q. RAG 문서 예제에 var를 써도 돼?
A. 비교나 나쁜 예시 목적이 아니라면 사용하지 않는다.

---

# 5. Scope

## 5.1 Block Scope and Function Scope

### [개념]

Scope는 변수에 접근할 수 있는 범위다.

JavaScript 변수 Scope는 선언 방식에 따라 다르게 동작한다.

- `const`: block scope
- `let`: block scope
- `var`: function scope

Block Scope 예:

```javascript
if (isLoggedIn) {
  const message = "환영합니다.";
}

console.log(message); // Error
```

---

### [핵심]

- Scope
- block scope
- function scope
- global scope
- local scope
- const scope
- let scope
- var scope
- variable access

---

### [실무]

Frontend 코드에서는 Scope를 좁게 유지해야 한다.

권장 기준:

- 필요한 위치에서 변수 선언
- 전역 변수 최소화
- 함수 내부 변수 우선
- block 내부에서만 쓰는 값은 block 내부 선언
- API 응답 데이터는 필요한 함수 Scope 안에서 처리
- Event Handler 외부에 불필요한 mutable 상태 두지 않기

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

Review Agent는 불필요한 전역 변수와 넓은 Scope의 mutable variable을 검출해야 한다.

---

### [FAQ]

Q. Scope가 뭐야?
A. 변수와 함수에 접근할 수 있는 범위다.

Q. block scope가 뭐야?
A. `{}` block 내부에서 선언된 변수가 해당 block 안에서만 유효한 범위다.

Q. function scope가 뭐야?
A. 함수 내부에서 선언된 변수가 함수 전체에서 유효한 범위다.

Q. Scope를 좁게 유지하는 이유는?
A. 변수 충돌을 줄이고 값 변경 흐름을 쉽게 추적하기 위해서다.

---

# 6. Hoisting and Temporal Dead Zone

## 6.1 Hoisting

### [개념]

Hoisting은 JavaScript에서 선언이 Scope의 위쪽으로 끌어올려진 것처럼 동작하는 특성이다.

`var`는 hoisting으로 인해 선언 전 접근 시 `undefined`가 될 수 있다.

예:

```javascript
console.log(userName); // undefined

var userName = "jun";
```

---

### [핵심]

- Hoisting
- var hoisting
- function declaration hoisting
- const
- let
- temporal dead zone
- ReferenceError
- declaration
- initialization

---

### [실무]

Frontend Agent는 hoisting에 의존하는 코드를 생성하면 안 된다.

비권장:

```javascript
console.log(currentPage);

var currentPage = 1;
```

권장:

```javascript
const currentPage = 1;

console.log(currentPage);
```

함수 선언은 hoisting될 수 있지만, 실무에서는 호출 위치보다 정의 위치를 명확히 유지하는 것이 좋다.

주의:

- 선언 전 변수 사용 금지
- `var` hoisting에 의존 금지
- function declaration과 function expression의 hoisting 차이 인지
- Review Agent는 선언 전 사용 코드를 검출해야 함

---

### [FAQ]

Q. Hoisting이 뭐야?
A. 변수나 함수 선언이 Scope 위쪽으로 끌어올려진 것처럼 동작하는 JavaScript 특성이다.

Q. var는 선언 전에 접근하면 어떻게 돼?
A. 오류가 아니라 `undefined`가 나올 수 있어 예측하기 어려운 코드가 된다.

Q. hoisting에 의존하는 코드는 좋아?
A. 아니다. 선언 후 사용하는 방식으로 명확하게 작성해야 한다.

---

## 6.2 Temporal Dead Zone

### [개념]

Temporal Dead Zone은 `let`과 `const` 변수가 선언되기 전까지 접근할 수 없는 구간이다.

예:

```javascript
console.log(userName); // ReferenceError

const userName = "jun";
```

---

### [핵심]

- Temporal Dead Zone
- TDZ
- let
- const
- ReferenceError
- declaration before use
- safe variable access

---

### [실무]

Temporal Dead Zone은 선언 전 접근을 방지해 코드 안정성을 높인다.

권장:

```javascript
const userName = "jun";

console.log(userName);
```

비권장:

```javascript
console.log(userName);

let userName = "jun";
```

Review 기준:

```text
Variable Review
→ Declaration Position Check
→ Usage Before Declaration Check
→ const / let TDZ Risk Check
→ Refactor
```

Frontend Agent는 변수 선언 위치를 사용 위치보다 위에 배치해야 한다.

---

### [FAQ]

Q. Temporal Dead Zone이 뭐야?
A. let과 const 변수가 선언되기 전까지 접근할 수 없는 구간이다.

Q. TDZ에서 변수에 접근하면 어떻게 돼?
A. ReferenceError가 발생한다.

Q. TDZ는 왜 있어?
A. 선언 전 변수 사용을 막아 예측 가능한 코드를 만들기 위해서다.

---

# 7. Variable Naming

## 7.1 Naming Rules

### [개념]

Variable Naming은 변수의 목적과 의미를 드러내는 이름을 정하는 규칙이다.

RAG 문서에서는 변수명이 Retrieval, Code Generation, Review 정확도에 영향을 준다.

예:

```javascript
const festivalTitle = "Spring Festival";
const isFavorite = true;
const reviewCount = 12;
```

---

### [핵심]

- variable naming
- camelCase
- meaningful name
- boolean prefix
- is
- has
- can
- should
- count
- list
- response
- request
- data
- DTO mapping

---

### [실무]

JavaScript 변수명은 `camelCase`를 기본으로 한다.

권장 네이밍:

| 목적      | 예시                                          |
| --------- | --------------------------------------------- |
| 문자열    | `festivalTitle`, `userName`                   |
| 숫자      | `reviewCount`, `currentPage`                  |
| boolean   | `isLoggedIn`, `hasNextPage`, `canSubmit`      |
| 배열      | `festivals`, `activeFestivals`, `reviewItems` |
| 객체      | `festival`, `userProfile`, `searchCondition`  |
| API 응답  | `festivalResponse`, `reviewResponse`          |
| 화면 상태 | `loading`, `error`, `emptyMessage`            |

권장:

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
const hasNextPage = pageInfo?.hasNext ?? false;
```

비권장:

```javascript
const arr = [];
const flag = true;
const data1 = {};
```

주의:

- 의미 없는 `data`, `temp`, `arr`, `obj` 남용 금지
- boolean은 true / false 의미가 드러나야 함
- API 원본 데이터와 화면 가공 데이터 이름 구분
- 단수 / 복수 구분
- Backend DTO 필드명과 Frontend 변수명 매핑 일관성 유지

---

### [FAQ]

Q. JavaScript 변수명은 어떤 스타일을 써?
A. 일반적으로 camelCase를 사용한다.

Q. boolean 변수명은 어떻게 짓는 게 좋아?
A. `is`, `has`, `can`, `should` 같은 접두사를 사용해 true / false 의미를 드러내는 것이 좋다.

Q. data라는 변수명은 안 좋아?
A. 단순 예제에서는 가능하지만 실무 코드에서는 의미가 부족하므로 구체적인 이름을 쓰는 것이 좋다.

Q. 배열 변수명은 어떻게 짓는 게 좋아?
A. 여러 개를 의미하도록 복수형이나 목록 의미가 드러나는 이름을 사용한다.

---

# 8. Data Type

## 8.1 Data Type Concept

### [개념]

Data Type은 JavaScript 값의 종류를 의미한다.

JavaScript Data Type은 크게 Primitive Type과 Reference Type으로 구분한다.

Primitive Type은 값 자체를 다루고, Reference Type은 객체 참조를 다룬다.

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

Frontend 주요 타입:

- string
- number
- boolean
- null
- undefined
- object
- array
- function

---

### [실무]

Frontend API Response와 UI 상태는 대부분 Object / Array 조합으로 처리된다.

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

실무 주의:

- `null`과 `undefined`를 구분한다.
- 숫자 문자열과 number를 구분한다.
- API 응답 날짜는 string으로 오는 경우가 많다.
- 배열은 `typeof` 결과가 `"object"`다.
- 배열 여부는 `Array.isArray()`로 확인한다.
- Object / Array는 Reference Type이므로 원본 변경에 주의한다.

---

### [FAQ]

Q. Data Type이 뭐야?
A. JavaScript 값의 종류를 의미한다.

Q. JavaScript의 주요 Data Type은 뭐야?
A. string, number, boolean, null, undefined, object, array, function이 실무에서 자주 사용된다.

Q. API 응답은 보통 어떤 타입으로 처리해?
A. 대부분 object와 array 조합으로 처리한다.

Q. 배열은 JavaScript에서 어떤 타입이야?
A. 배열은 object 타입이며, 배열 여부는 `Array.isArray()`로 확인하는 것이 좋다.

---

# 9. Primitive Type

## 9.1 string

### [개념]

`string`은 문자 데이터를 표현하는 Primitive Type이다.

Frontend에서는 제목, 이름, 검색어, 메시지, 날짜 문자열, URL 등을 표현할 때 사용한다.

예:

```javascript
const title = "Spring Festival";
const keyword = "music";
```

---

### [핵심]

- string
- text
- template literal
- trim
- includes
- startsWith
- endsWith
- toLowerCase
- string comparison
- user input
- API text field

---

### [실무]

문자열은 사용자 입력과 API 응답 처리에서 자주 사용된다.

검색어 처리 예:

```javascript
function normalizeKeyword(keyword) {
  return keyword.trim();
}
```

Template Literal 예:

```javascript
const message = `${userName}님, 환영합니다.`;
```

주의:

- 사용자 입력은 `trim()` 처리
- 빈 문자열 검증 필요
- 숫자처럼 보이는 문자열과 number 구분
- HTML 삽입 시 XSS 주의
- URL query에 넣을 때 `encodeURIComponent()` 사용

예:

```javascript
const query = encodeURIComponent(keyword.trim());
const url = `/api/festivals/search?keyword=${query}`;
```

---

### [FAQ]

Q. string은 언제 써?
A. 제목, 이름, 검색어, 메시지, 날짜 문자열, URL 같은 문자 데이터를 표현할 때 사용한다.

Q. 입력값에 trim을 왜 써?
A. 앞뒤 공백만 입력된 값을 유효한 입력으로 처리하지 않기 위해 사용한다.

Q. Template Literal은 왜 써?
A. 문자열 안에 변수를 간결하게 넣기 위해 사용한다.

Q. URL query에 사용자 입력을 넣을 때 주의할 점은?
A. `encodeURIComponent()`로 인코딩해 특수문자로 인한 오류를 줄여야 한다.

---

## 9.2 number

### [개념]

`number`는 숫자 데이터를 표현하는 Primitive Type이다.

JavaScript의 일반 숫자는 정수와 실수를 모두 `number` 타입으로 다룬다.

예:

```javascript
const reviewCount = 12;
const rating = 4.5;
```

---

### [핵심]

- number
- integer
- float
- NaN
- Number
- parseInt
- parseFloat
- arithmetic
- comparison
- price
- count
- page
- rating

---

### [실무]

Frontend에서 number는 count, page, price, rating, id, coordinate 등에 사용된다.

예:

```javascript
const currentPage = 1;
const pageSize = 20;
const totalCount = 153;
```

문자열 숫자 변환:

```javascript
const page = Number(pageText);
```

주의:

- input value는 기본적으로 string으로 읽힐 수 있다.
- 숫자 변환 실패 시 `NaN`이 될 수 있다.
- 숫자 문자열과 number 비교 주의
- 금액 표시는 `toLocaleString()` 활용 가능
- 좌표, 평점 같은 실수 값은 소수 처리 주의

예:

```javascript
function formatPrice(price) {
  return `${price.toLocaleString()}원`;
}
```

---

### [FAQ]

Q. JavaScript에서 정수와 실수 타입이 따로 있어?
A. 일반 숫자는 모두 number 타입으로 다룬다.

Q. input에서 받은 숫자는 바로 number야?
A. 아니다. 문자열로 읽히는 경우가 많으므로 필요하면 Number로 변환해야 한다.

Q. NaN은 뭐야?
A. Not-a-Number를 의미하며 숫자 변환이나 계산이 실패했을 때 발생할 수 있다.

Q. 금액 표시는 어떻게 처리해?
A. `toLocaleString()`을 사용해 천 단위 구분을 적용할 수 있다.

---

## 9.3 boolean

### [개념]

`boolean`은 `true` 또는 `false` 값을 가지는 Primitive Type이다.

조건 판단, UI 상태, 권한 여부, 로딩 상태를 표현할 때 사용한다.

예:

```javascript
const isLoggedIn = true;
const loading = false;
```

---

### [핵심]

- boolean
- true
- false
- condition
- is
- has
- can
- should
- loading
- error
- disabled
- active
- checked

---

### [실무]

boolean은 UI 조건과 상태 판단에 자주 사용된다.

예:

```javascript
const canSubmit = keyword.trim().length > 0 && !loading;
const isEmpty = festivals.length === 0;
```

UI 상태 판단:

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

boolean 변수명 권장:

- `isLoggedIn`
- `isActive`
- `hasNextPage`
- `canSubmit`
- `shouldShowModal`

주의:

- boolean 이름은 true일 때 의미가 명확해야 한다.
- `flag` 같은 이름은 지양한다.
- 조건식이 복잡하면 의미 있는 변수로 분리한다.

---

### [FAQ]

Q. boolean은 언제 써?
A. true 또는 false로 판단할 수 있는 상태를 표현할 때 사용한다.

Q. boolean 변수명은 어떻게 지어?
A. `is`, `has`, `can`, `should` 같은 접두사를 사용하면 의미가 명확해진다.

Q. loading도 boolean이야?
A. 보통 API 요청 중 여부를 나타내는 boolean 상태로 사용한다.

Q. flag라는 이름은 왜 피하는 게 좋아?
A. true일 때 어떤 의미인지 불명확하기 때문이다.

---

## 9.4 null and undefined

### [개념]

`null`과 `undefined`는 값이 없음을 표현하지만 의미가 다르다.

`undefined`는 값이 할당되지 않은 상태를 의미한다.

`null`은 의도적으로 값이 없음을 표현하는 값이다.

예:

```javascript
let selectedFestival;

const deletedAt = null;
```

---

### [핵심]

- null
- undefined
- no value
- intentional empty
- unassigned
- optional chaining
- nullish coalescing
- default value
- API response
- missing field

---

### [실무]

Frontend API 연동에서는 `null`과 `undefined` 방어가 중요하다.

API 응답 예:

```javascript
const imageUrl = festival.imageUrl ?? "/default.png";
const title = festival?.title ?? "제목 없음";
```

목록 기본값:

```javascript
const festivals = response?.data?.content ?? [];
```

주의:

- `undefined` property 접근 시 오류 발생 가능
- API 응답에서 값이 `null`로 올 수 있음
- 중첩 객체 접근에는 optional chaining 사용
- 기본값 처리에는 nullish coalescing 사용
- `||`는 `0`, `false`, `""`도 기본값으로 처리할 수 있으므로 주의

비권장:

```javascript
const title = response.data.content[0].title;
```

권장:

```javascript
const title = response?.data?.content?.[0]?.title ?? "제목 없음";
```

---

### [FAQ]

Q. null과 undefined 차이는 뭐야?
A. undefined는 값이 할당되지 않은 상태이고 null은 의도적으로 값이 없음을 표현한 값이다.

Q. API 응답이 null일 수 있으면 어떻게 해?
A. optional chaining과 nullish coalescing으로 기본값을 지정한다.

Q. Cannot read properties of undefined 오류는 왜 발생해?
A. undefined인 값에서 property를 읽으려고 할 때 발생한다.

Q. `??`와 `||` 차이는 뭐야?
A. `??`는 null 또는 undefined일 때만 기본값을 사용하고, `||`는 falsy 값 전체를 기본값으로 처리할 수 있다.

---

# 10. Reference Type

## 10.1 object

### [개념]

`object`는 key-value 구조로 데이터를 저장하는 Reference Type이다.

Frontend에서는 사용자 정보, 축제 정보, 검색 조건, API 응답 객체를 표현할 때 사용한다.

예:

```javascript
const festival = {
  id: 1,
  title: "Spring Festival",
  region: "Seoul",
  active: true,
};
```

---

### [핵심]

- object
- key-value
- property
- method
- dot notation
- bracket notation
- nested object
- API response
- optional chaining
- object spread
- reference type

---

### [실무]

API Response는 대부분 object와 array 조합이다.

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
```

안전한 접근:

```javascript
const festivals = response?.data?.content ?? [];
```

객체 업데이트:

```javascript
const updatedFestival = {
  ...festival,
  active: false,
};
```

주의:

- object는 Reference Type이다.
- 같은 객체를 참조하면 한쪽 변경이 다른 곳에 영향을 줄 수 있다.
- Spread는 얕은 복사다.
- 중첩 객체는 내부 참조가 공유될 수 있다.
- API 원본 객체를 직접 변경하지 않는 것이 좋다.

---

### [FAQ]

Q. object는 뭐야?
A. key-value 구조로 데이터를 저장하는 JavaScript Reference Type이다.

Q. object property에는 어떻게 접근해?
A. dot notation 또는 bracket notation으로 접근한다.

Q. API 응답은 object야?
A. 대부분 object와 array가 중첩된 구조로 전달된다.

Q. object spread는 깊은 복사야?
A. 아니다. 기본적으로 얕은 복사다.

---

## 10.2 array

### [개념]

`array`는 순서가 있는 여러 값을 저장하는 Reference Type이다.

Frontend에서는 목록 데이터, 검색 결과, 리뷰 목록, 축제 목록을 표현할 때 자주 사용한다.

예:

```javascript
const festivals = [
  { id: 1, title: "Spring Festival" },
  { id: 2, title: "Summer Festival" },
];
```

---

### [핵심]

- array
- ordered list
- length
- map
- filter
- find
- reduce
- sort
- includes
- some
- every
- Array.isArray
- reference type
- list rendering

---

### [실무]

Frontend API Response 처리에서 배열 메서드는 매우 중요하다.

목록 변환:

```javascript
const festivalCards = festivals.map((festival) => ({
  id: festival.id,
  title: festival.title,
  imageUrl: festival.imageUrl ?? "/default.png",
}));
```

조건 필터링:

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
```

배열 여부 확인:

```javascript
const items = Array.isArray(response?.data?.content)
  ? response.data.content
  : [];
```

주의:

- `map`은 새 배열 반환
- `filter`는 조건에 맞는 새 배열 반환
- `find`는 첫 번째 요소 반환
- `sort`는 원본 배열 변경
- `slice`는 원본 유지
- `splice`는 원본 변경
- 배열은 `typeof` 결과가 `"object"`이므로 `Array.isArray()` 사용

---

### [FAQ]

Q. array는 뭐야?
A. 순서가 있는 여러 값을 저장하는 JavaScript Reference Type이다.

Q. 배열 여부는 어떻게 확인해?
A. `Array.isArray()`로 확인하는 것이 좋다.

Q. map과 filter 차이는 뭐야?
A. map은 각 요소를 변환해 새 배열을 만들고, filter는 조건에 맞는 요소만 모아 새 배열을 만든다.

Q. sort는 원본 배열을 바꿔?
A. 바꾼다. 원본 변경을 피하려면 복사 후 sort를 사용한다.

---

## 10.3 function

### [개념]

`function`은 재사용 가능한 코드 블록이며 JavaScript에서는 값처럼 다룰 수 있는 Reference Type이다.

함수는 변수에 할당하거나 다른 함수의 인자로 전달할 수 있다.

예:

```javascript
function formatTitle(title) {
  return title.trim();
}

const normalizeTitle = (title) => title.trim();
```

---

### [핵심]

- function
- function declaration
- function expression
- arrow function
- callback
- return
- parameter
- argument
- reusable logic
- reference type

---

### [실무]

Frontend에서는 function을 UI 로직, API 호출, 데이터 가공, 이벤트 처리에 사용한다.

예:

```javascript
function isActiveFestival(festival) {
  return festival.status === "ACTIVE";
}
```

Callback 예:

```javascript
const activeFestivals = festivals.filter((festival) => festival.active);
```

주의:

- 하나의 함수는 하나의 책임
- 입력과 출력 명확화
- 의미 있는 함수명 사용
- UI 로직과 데이터 가공 로직 분리
- API 호출 함수 분리
- 복잡한 조건은 함수로 분리

---

### [FAQ]

Q. function도 Data Type이야?
A. JavaScript에서 function은 호출 가능한 객체처럼 동작하며 Reference Type으로 볼 수 있다.

Q. 함수는 왜 분리해?
A. 반복 로직을 줄이고 테스트와 유지보수를 쉽게 하기 위해 분리한다.

Q. callback function은 뭐야?
A. 다른 함수에 인자로 전달되어 나중에 실행되는 함수다.

Q. array method에서 arrow function을 자주 쓰는 이유는?
A. 짧은 callback을 간결하게 표현할 수 있기 때문이다.

---

# 11. Type Check

## 11.1 typeof

### [개념]

`typeof`는 값의 타입을 문자열로 반환하는 연산자다.

예:

```javascript
typeof "hello"; // "string"
typeof 123; // "number"
typeof true; // "boolean"
```

---

### [핵심]

- typeof
- type check
- string
- number
- boolean
- undefined
- object
- function
- Array.isArray
- null caution

---

### [실무]

`typeof`는 기본 타입 확인에 사용할 수 있다.

예:

```javascript
function isString(value) {
  return typeof value === "string";
}
```

주의:

```javascript
typeof null; // "object"
typeof []; // "object"
```

배열 확인은 `Array.isArray()`를 사용한다.

```javascript
Array.isArray([]); // true
```

null 확인은 직접 비교한다.

```javascript
value === null;
```

Review Agent는 `typeof value === "object"`만으로 null과 array를 구분하는 코드를 주의해야 한다.

---

### [FAQ]

Q. typeof는 뭐야?
A. 값의 타입을 문자열로 반환하는 JavaScript 연산자다.

Q. typeof null은 뭐가 나와?
A. `"object"`가 나온다. null은 직접 `value === null`로 확인하는 것이 좋다.

Q. 배열은 typeof로 확인하면 돼?
A. 아니다. 배열은 `Array.isArray()`로 확인하는 것이 좋다.

Q. typeof function은 뭐가 나와?
A. `"function"`이 나온다.

---

## 11.2 Array.isArray

### [개념]

`Array.isArray()`는 값이 배열인지 확인하는 메서드다.

`typeof`로 배열을 확인하면 `"object"`가 나오므로 배열 여부 확인에는 `Array.isArray()`를 사용한다.

예:

```javascript
Array.isArray([]); // true
Array.isArray({}); // false
```

---

### [핵심]

- Array.isArray
- array check
- typeof array caution
- API response validation
- fallback empty array

---

### [실무]

API 응답 목록을 처리할 때 배열 검증을 적용할 수 있다.

예:

```javascript
function normalizeList(value) {
  return Array.isArray(value) ? value : [];
}
```

API Response 처리:

```javascript
const content = response?.data?.content;
const festivals = Array.isArray(content) ? content : [];
```

주의:

- 서버 응답 구조가 바뀔 수 있다.
- 목록 데이터가 null일 수 있다.
- 배열이 아닌 값에 map을 호출하면 오류가 발생한다.
- `Array.isArray()`로 방어하면 안전한 list rendering이 가능하다.

---

### [FAQ]

Q. Array.isArray는 언제 써?
A. 값이 배열인지 확인할 때 사용한다.

Q. 배열인데 typeof 결과가 object인 이유는?
A. JavaScript에서 배열은 객체 기반 Reference Type이기 때문이다.

Q. API 응답 목록에 Array.isArray를 쓰는 이유는?
A. 배열이 아닌 값에 map, filter를 호출해 발생하는 오류를 방지하기 위해서다.

---

# 12. Type Conversion

## 12.1 Explicit Conversion

### [개념]

Type Conversion은 값의 타입을 다른 타입으로 변환하는 것이다.

명시적 변환은 개발자가 직접 `String()`, `Number()`, `Boolean()` 등을 사용해 타입을 바꾸는 방식이다.

예:

```javascript
const page = Number("1");
const countText = String(10);
const hasKeyword = Boolean("festival");
```

---

### [핵심]

- Type Conversion
- explicit conversion
- String
- Number
- Boolean
- parseInt
- parseFloat
- NaN
- input value
- query parameter

---

### [실무]

Frontend에서는 사용자 입력과 URL query parameter가 문자열로 들어오는 경우가 많다.

예:

```javascript
const page = Number(searchParams.get("page") ?? "1");
```

숫자 변환 검증:

```javascript
function toValidPage(value) {
  const page = Number(value);

  if (Number.isNaN(page) || page < 1) {
    return 1;
  }

  return page;
}
```

주의:

- `Number("")`는 0이 될 수 있다.
- 숫자 변환 실패는 `NaN`이 될 수 있다.
- input value는 대부분 string으로 처리된다.
- 암묵적 변환에 의존하지 않는다.
- 비교 전에 타입을 맞춘다.

---

### [FAQ]

Q. Type Conversion이 뭐야?
A. 값의 타입을 다른 타입으로 변환하는 것이다.

Q. input value는 숫자로 입력해도 number야?
A. 보통 문자열로 읽히므로 필요하면 명시적으로 Number 변환해야 한다.

Q. Number 변환 실패는 어떻게 확인해?
A. `Number.isNaN()`으로 확인할 수 있다.

Q. 실무에서 명시적 변환이 좋은 이유는?
A. 타입 흐름이 명확해지고 예상하지 못한 비교 오류를 줄일 수 있기 때문이다.

---

## 12.2 Implicit Conversion Caution

### [개념]

Implicit Conversion은 JavaScript가 연산이나 비교 과정에서 자동으로 타입을 변환하는 동작이다.

암묵적 변환은 편리하지만 예측하기 어려운 결과를 만들 수 있다.

예:

```javascript
"1" == 1; // true
"1" + 1; // "11"
"1" - 1; // 0
```

---

### [핵심]

- implicit conversion
- type coercion
- == caution
- === recommended
- string number comparison
- predictable code
- strict equality

---

### [실무]

실무 JavaScript에서는 암묵적 변환에 의존하지 않는다.

비권장:

```javascript
if (page == 1) {
  loadPage();
}
```

권장:

```javascript
if (Number(page) === 1) {
  loadPage();
}
```

비교 기준:

- `===` 사용
- `!==` 사용
- 비교 전 타입 명시적 변환
- API 응답 타입 확인
- URL parameter는 문자열로 간주

Review Agent는 `==`, `!=` 사용을 발견하면 `===`, `!==` 전환을 권장해야 한다.

---

### [FAQ]

Q. Implicit Conversion이 뭐야?
A. JavaScript가 연산이나 비교 중 자동으로 타입을 변환하는 동작이다.

Q. ==와 === 차이는 뭐야?
A. ==는 타입 변환 후 비교하고, ===는 타입과 값을 모두 비교한다.

Q. 실무에서는 ==를 써도 돼?
A. 특별한 이유가 없다면 `===` 사용을 권장한다.

Q. "1" + 1 결과는 뭐야?
A. 문자열 연결로 처리되어 `"11"`이 된다.

---

# 13. Truthy and Falsy

## 13.1 Truthy and Falsy Concept

### [개념]

Truthy는 조건문에서 true처럼 평가되는 값이다.

Falsy는 조건문에서 false처럼 평가되는 값이다.

JavaScript 조건문은 boolean이 아닌 값도 truthy 또는 falsy로 평가한다.

예:

```javascript
if ("festival") {
  console.log("truthy");
}
```

---

### [핵심]

Falsy 값:

- false
- 0
- -0
- 0n
- ""
- null
- undefined
- NaN

Truthy 값:

- non-empty string
- non-zero number
- object
- array
- function

---

### [실무]

Falsy 값은 입력 검증과 조건 처리에서 자주 사용된다.

예:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}
```

주의:

```javascript
if (!value) {
  return "기본값";
}
```

위 코드는 `0`, `false`, `""`, `null`, `undefined`, `NaN`을 모두 같은 방식으로 처리한다.

값이 `0`이나 `false`도 유효할 수 있다면 `??`를 사용한다.

```javascript
const count = response.count ?? 0;
```

주의:

- 빈 문자열은 falsy
- 빈 배열은 truthy
- 빈 객체는 truthy
- `0`이 유효한 값이면 `||` 기본값 처리 주의
- null / undefined만 기본값 처리하려면 `??` 사용

---

### [FAQ]

Q. Truthy와 Falsy가 뭐야?
A. 조건문에서 true처럼 평가되는 값은 truthy, false처럼 평가되는 값은 falsy다.

Q. JavaScript의 Falsy 값은 뭐야?
A. false, 0, -0, 0n, 빈 문자열, null, undefined, NaN이다.

Q. 빈 배열은 falsy야?
A. 아니다. 빈 배열은 truthy다.

Q. 0도 유효한 값이면 기본값 처리를 어떻게 해야 해?
A. `||`보다 `??`를 사용해 null 또는 undefined일 때만 기본값을 적용한다.

---

# 14. Variable and Data Type Common Mistakes

## 14.1 Common Mistakes

### [개념]

Variable과 Data Type 실수는 JavaScript 오류의 주요 원인이다.

Frontend Agent와 Review Agent는 변수 선언, 타입 변환, null 방어, 배열 확인, API 응답 타입을 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- var 사용
- const 대신 let 남용
- 의미 없는 변수명 사용
- boolean 이름 불명확
- null / undefined 혼동
- `==` 사용
- 암묵적 타입 변환 의존
- input value를 number로 착각
- 배열을 typeof로 확인
- typeof null 결과 오해
- API 응답 구조 확인 없이 접근
- 배열이 아닌 값에 map 호출
- object / array 원본 변경 실수
- `||`로 0 또는 false를 덮어씀
- console.log로 민감정보 출력

---

### [실무]

Review Flow:

```text
Variable Review
→ const / let / var Check
→ Naming Check
→ Scope Check
→ Type Check
→ null / undefined Guard Check
→ Array.isArray Check
→ Type Conversion Check
→ Truthy / Falsy Risk Check
→ API Response Safety Check
```

나쁜 예:

```javascript
var data = response.data.content;

if (data) {
  data.map((item) => item.title);
}
```

개선 예:

```javascript
const content = response?.data?.content;
const festivals = Array.isArray(content) ? content : [];

const titles = festivals.map((festival) => festival.title);
```

주의:

- `data` 같은 넓은 이름보다 `festivals`, `reviewItems`처럼 구체적으로 작성한다.
- 배열 메서드 호출 전 배열 여부를 확인한다.
- API 응답은 항상 null / undefined 가능성을 고려한다.
- 숫자 비교 전 타입을 명확히 한다.
- `0`, `false`, `""`가 유효한 값인지 확인한다.

---

### [FAQ]

Q. Variable과 Data Type에서 가장 흔한 실수는 뭐야?
A. var 사용, null / undefined 접근, 암묵적 타입 변환, 배열이 아닌 값에 map 호출, 의미 없는 변수명 사용이다.

Q. API 응답 배열에 바로 map을 써도 돼?
A. 응답 구조가 확실하지 않다면 `Array.isArray()` 또는 기본값 처리 후 사용하는 것이 안전하다.

Q. `||` 기본값 처리는 항상 안전해?
A. 아니다. 0, false, 빈 문자열도 기본값으로 덮어쓸 수 있으므로 null / undefined만 처리하려면 `??`를 사용한다.

Q. Review Agent는 무엇을 우선 확인해야 해?
A. var 사용 여부, 변수명, Scope, null 방어, 타입 변환, 배열 검증, API 응답 안전성을 우선 확인해야 한다.

---

# 15. Variable and Data Type Checklist

## 15.1 Document Quality Checklist

### [개념]

Variable and Data Type 문서는 Frontend Agent가 안전한 변수 선언과 타입 처리를 수행하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] const / let / var 차이가 명확한가?
- [ ] const 우선 사용 기준이 포함되었는가?
- [ ] let 사용 기준이 포함되었는가?
- [ ] var 사용 지양 이유가 포함되었는가?
- [ ] Scope 설명이 포함되었는가?
- [ ] Hoisting 설명이 포함되었는가?
- [ ] Temporal Dead Zone 설명이 포함되었는가?
- [ ] Variable Naming 규칙이 포함되었는가?
- [ ] Primitive Type 설명이 포함되었는가?
- [ ] Reference Type 설명이 포함되었는가?
- [ ] null / undefined 차이가 포함되었는가?
- [ ] typeof 주의사항이 포함되었는가?
- [ ] Array.isArray 사용 기준이 포함되었는가?
- [ ] Type Conversion 주의사항이 포함되었는가?
- [ ] Truthy / Falsy 설명이 포함되었는가?
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
→ Variable Rule Check
→ Data Type Rule Check
→ Frontend API Example Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part01_Basic_Syntax
→ JavaScript_Foundation_Part02_Variable_Data_Type
→ JavaScript_Foundation_Part03_Operator_Condition_Loop
```

---

### [FAQ]

Q. Variable and Data Type 문서 검수에서 가장 중요한 것은 뭐야?
A. const 우선 사용, var 지양, null / undefined 방어, 타입 변환, 배열 검증, API 응답 안전성이다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React State, Props, Event Handler, API Response 처리 모두 JavaScript 변수와 타입 이해가 기반이다.

Q. 다음 Part와 어떻게 연결돼?
A. Part02는 값과 타입 기준을 만들고, Part03은 Operator, Condition, Loop로 실행 흐름을 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Variable이 뭐야?
A. 값을 저장하고 나중에 참조하기 위한 이름이다.

Q. JavaScript 변수는 어떻게 선언해?
A. const, let, var로 선언할 수 있다.

Q. const let var 차이는 뭐야?
A. const는 재할당 불가, let은 재할당 가능, var는 function scope와 hoisting 문제로 사용을 지양한다.

Q. JavaScript에서 기본 변수 선언은 뭐를 써?
A. 기본은 const를 사용하고, 재할당이 필요한 경우에만 let을 사용한다.

Q. const는 언제 써?
A. 재할당하지 않을 값을 선언할 때 사용한다.

Q. const 객체는 수정할 수 있어?
A. const는 변수 재할당을 막지만 객체 내부 property 변경은 가능하다.

Q. const 배열에 push 할 수 있어?
A. 가능하다. 배열 변수 자체를 재할당하는 것은 불가능하지만 내부 변경은 가능하다.

Q. let은 언제 써?
A. 값 재할당이 필요한 변수에 사용한다.

Q. var는 왜 피해야 해?
A. function scope, 재선언, hoisting 때문에 예측하기 어려운 코드가 될 수 있기 때문이다.

Q. Scope가 뭐야?
A. 변수와 함수에 접근할 수 있는 범위다.

Q. block scope가 뭐야?
A. 중괄호 block 내부에서 선언된 변수가 해당 block 안에서만 유효한 범위다.

Q. function scope가 뭐야?
A. 함수 내부에서 선언된 변수가 함수 전체에서 유효한 범위다.

Q. Hoisting이 뭐야?
A. 변수나 함수 선언이 Scope 위쪽으로 끌어올려진 것처럼 동작하는 JavaScript 특성이다.

Q. Temporal Dead Zone이 뭐야?
A. let과 const 변수가 선언되기 전까지 접근할 수 없는 구간이다.

Q. JavaScript 변수명은 어떻게 지어?
A. camelCase를 사용하고 변수의 목적과 의미가 드러나도록 구체적으로 작성한다.

Q. boolean 변수명은 어떻게 지어?
A. is, has, can, should 같은 접두사를 사용해 true / false 의미를 명확히 한다.

Q. data라는 변수명은 안 좋아?
A. 실무에서는 의미가 부족하므로 festivalResponse, activeFestivals처럼 구체적인 이름이 좋다.

Q. JavaScript Data Type은 뭐야?
A. 값의 종류를 의미하며 Primitive Type과 Reference Type으로 구분한다.

Q. JavaScript Primitive Type은 뭐가 있어?
A. string, number, boolean, null, undefined, symbol, bigint가 있다.

Q. JavaScript Reference Type은 뭐가 있어?
A. object, array, function이 있다.

Q. string은 언제 써?
A. 제목, 이름, 검색어, 메시지, 날짜 문자열, URL 같은 문자 데이터를 표현할 때 사용한다.

Q. 입력값에 trim을 왜 써?
A. 앞뒤 공백만 입력된 값을 유효한 입력으로 처리하지 않기 위해 사용한다.

Q. number는 언제 써?
A. count, page, price, rating, id, coordinate 같은 숫자 데이터를 표현할 때 사용한다.

Q. input에서 받은 숫자는 number야?
A. 보통 문자열로 읽히므로 필요하면 Number로 명시적 변환해야 한다.

Q. NaN은 뭐야?
A. Not-a-Number를 의미하며 숫자 변환이나 계산이 실패했을 때 발생할 수 있다.

Q. boolean은 언제 써?
A. true 또는 false로 판단할 수 있는 상태를 표현할 때 사용한다.

Q. null과 undefined 차이는 뭐야?
A. undefined는 값이 할당되지 않은 상태이고 null은 의도적으로 값이 없음을 표현한 값이다.

Q. API 응답이 null일 수 있으면 어떻게 해?
A. optional chaining과 nullish coalescing으로 기본값을 지정한다.

Q. Cannot read properties of undefined 오류는 왜 발생해?
A. undefined인 값에서 property를 읽으려고 할 때 발생한다.

Q. object는 뭐야?
A. key-value 구조로 데이터를 저장하는 JavaScript Reference Type이다.

Q. array는 뭐야?
A. 순서가 있는 여러 값을 저장하는 JavaScript Reference Type이다.

Q. function도 타입이야?
A. JavaScript에서 function은 호출 가능한 객체처럼 동작하며 Reference Type으로 볼 수 있다.

Q. typeof는 뭐야?
A. 값의 타입을 문자열로 반환하는 JavaScript 연산자다.

Q. typeof null은 뭐가 나와?
A. "object"가 나온다. null은 직접 value === null로 확인하는 것이 좋다.

Q. 배열은 typeof로 확인하면 돼?
A. 아니다. 배열은 Array.isArray()로 확인하는 것이 좋다.

Q. Array.isArray는 언제 써?
A. 값이 배열인지 확인할 때 사용한다.

Q. API 응답 목록에 Array.isArray를 왜 써?
A. 배열이 아닌 값에 map이나 filter를 호출해 발생하는 오류를 방지하기 위해서다.

Q. Type Conversion이 뭐야?
A. 값의 타입을 다른 타입으로 변환하는 것이다.

Q. 명시적 타입 변환은 어떻게 해?
A. String(), Number(), Boolean(), parseInt(), parseFloat() 등을 사용한다.

Q. Implicit Conversion이 뭐야?
A. JavaScript가 연산이나 비교 중 자동으로 타입을 변환하는 동작이다.

Q. ==와 === 차이는 뭐야?
A. ==는 타입 변환 후 비교하고, ===는 타입과 값을 모두 비교한다.

Q. 실무에서는 ==를 써도 돼?
A. 특별한 이유가 없다면 === 사용을 권장한다.

Q. Truthy와 Falsy가 뭐야?
A. 조건문에서 true처럼 평가되는 값은 truthy, false처럼 평가되는 값은 falsy다.

Q. JavaScript Falsy 값은 뭐야?
A. false, 0, -0, 0n, 빈 문자열, null, undefined, NaN이다.

Q. 빈 배열은 falsy야?
A. 아니다. 빈 배열은 truthy다.

Q. `??`와 `||` 차이는 뭐야?
A. `??`는 null 또는 undefined일 때만 기본값을 사용하고, `||`는 falsy 값 전체를 기본값으로 처리할 수 있다.

Q. Variable and Data Type에서 가장 흔한 실수는 뭐야?
A. var 사용, null / undefined 접근, 암묵적 타입 변환, 배열이 아닌 값에 map 호출, 의미 없는 변수명 사용이다.

Q. JavaScript Foundation Part02 다음에는 무엇을 다뤄야 해?
A. Operator, Condition, Loop를 다루는 Part03으로 이어지는 것이 좋다.
