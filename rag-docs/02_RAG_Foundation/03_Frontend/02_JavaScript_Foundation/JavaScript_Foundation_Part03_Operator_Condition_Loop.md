# JavaScript Foundation Part03 - Operator, Condition, and Loop

---

# 1. Operator

## 1.1 Operator Concept

### [개념]

Operator는 값을 계산하거나 비교하거나 논리 판단을 수행하는 기호다.

JavaScript Operator는 Frontend Logic에서 조건 판단, UI 상태 계산, API 응답 가공, Form Validation에 사용된다.

예:

```javascript
const totalPrice = price * count;
const isValid = keyword.trim().length > 0;
const displayName = user?.name ?? "Guest";
```

---

### [핵심]

- Operator
- Arithmetic Operator
- Assignment Operator
- Comparison Operator
- Logical Operator
- Strict Equality
- Ternary Operator
- Optional Chaining
- Nullish Coalescing
- Frontend Logic
- UI Condition
- Validation

---

### [실무]

2026 실무 기준에서 Operator는 단순 계산보다 Frontend 상태 판단과 데이터 방어에 중요하다.

Frontend Agent는 Operator를 아래 작업에 활용해야 한다.

- 입력값 유효성 검증
- 버튼 disabled 조건 계산
- 로그인 여부 판단
- API 응답 기본값 처리
- null / undefined 방어
- 목록 Empty State 판단
- 조건부 메시지 생성
- React Conditional Rendering 준비

예:

```javascript
const canSubmit = keyword.trim().length > 0 && !loading;
const imageUrl = festival?.imageUrl ?? "/default.png";
const buttonText = loading ? "처리 중..." : "검색";
```

주의:

- `==` 대신 `===` 사용
- `!=` 대신 `!==` 사용
- `||` 기본값 처리 시 `0`, `false`, `""` 덮어쓰기 주의
- null / undefined만 기본값 처리하려면 `??` 사용
- 복잡한 조건식은 의미 있는 변수나 함수로 분리

---

### [FAQ]

Q. Operator가 뭐야?
A. 값을 계산하거나 비교하거나 논리 판단을 수행하는 JavaScript 기호다.

Q. Frontend에서 Operator는 어디에 많이 쓰여?
A. 입력 검증, UI 상태 계산, API 응답 기본값 처리, 조건부 렌더링 로직에 많이 사용된다.

Q. 실무에서 가장 중요한 Operator 기준은 뭐야?
A. `===`, `!==`, `?.`, `??`, `&&`, 삼항 연산자를 안전하고 명확하게 사용하는 것이다.

---

# 2. Arithmetic Operator

## 2.1 Arithmetic Operator Rules

### [개념]

Arithmetic Operator는 숫자 값을 계산하는 연산자다.

주요 연산자는 `+`, `-`, `*`, `/`, `%`, `**`다.

예:

```javascript
const totalPrice = price * count;
const remainder = page % pageSize;
```

---

### [핵심]

- Arithmetic Operator
- addition
- subtraction
- multiplication
- division
- remainder
- exponentiation
- number
- NaN
- numeric string caution
- price
- count
- page

---

### [실무]

Frontend에서 Arithmetic Operator는 금액, 개수, 페이지, 평점, 진행률 계산에 사용된다.

예:

```javascript
const totalCount = reviewCount + commentCount;
const totalPage = Math.ceil(totalItems / pageSize);
const discountPrice = price - discountAmount;
```

입력값 계산 전 숫자 변환:

```javascript
const count = Number(countInput.value);
const totalPrice = unitPrice * count;
```

주의:

- input value는 string일 수 있다.
- 숫자 변환 실패 시 `NaN` 발생 가능
- `+`는 문자열 연결에도 사용됨
- 계산 전 타입을 명확히 확인
- 금액 계산은 표시 포맷과 실제 값 구분

비권장:

```javascript
const totalPrice = priceInput.value + 1000;
```

권장:

```javascript
const price = Number(priceInput.value);
const totalPrice = price + 1000;
```

---

### [FAQ]

Q. Arithmetic Operator는 뭐야?
A. 숫자 값을 계산하는 연산자다.

Q. JavaScript에서 + 연산자는 항상 숫자 덧셈이야?
A. 아니다. 문자열이 포함되면 문자열 연결로 동작할 수 있다.

Q. input 값으로 계산할 때 주의할 점은?
A. input value는 문자열일 수 있으므로 Number로 명시적 변환 후 계산해야 한다.

Q. NaN은 왜 발생해?
A. 숫자로 변환할 수 없는 값을 계산하거나 변환할 때 발생할 수 있다.

---

# 3. Assignment Operator

## 3.1 Assignment Operator Rules

### [개념]

Assignment Operator는 변수에 값을 할당하거나 기존 값을 갱신하는 연산자다.

주요 연산자는 `=`, `+=`, `-=`, `*=`, `/=`다.

예:

```javascript
let currentPage = 1;

currentPage += 1;
```

---

### [핵심]

- Assignment Operator
- assignment
- reassignment
- increment
- decrement
- mutable variable
- let
- state update caution
- value change tracking

---

### [실무]

Assignment Operator는 값 변경이 필요한 경우에만 사용한다.

적합한 예:

```javascript
let currentPage = 1;

function moveNextPage() {
  currentPage += 1;
}
```

누적 계산:

```javascript
let total = 0;

for (const price of prices) {
  total += price;
}
```

주의:

- `const` 변수에는 재할당 불가
- `let` 변경 지점이 많으면 디버깅 어려움
- 객체와 배열 내부 변경은 원본 변경을 유발할 수 있음
- React State 전환 시 직접 할당이 아니라 setter 또는 immutable update 필요
- Review Agent는 불필요한 reassignment를 검토해야 함

비권장:

```javascript
let status = "READY";

status = "LOADING";
status = "SUCCESS";
status = "DONE";
```

권장:

```javascript
function getRequestStatus({ loading, error }) {
  if (loading) {
    return "LOADING";
  }

  if (error) {
    return "ERROR";
  }

  return "SUCCESS";
}
```

---

### [FAQ]

Q. Assignment Operator는 뭐야?
A. 변수에 값을 할당하거나 기존 값을 갱신하는 연산자다.

Q. +=는 언제 써?
A. 기존 값에 새 값을 더해 누적하거나 증가시킬 때 사용한다.

Q. const 변수에 재할당할 수 있어?
A. 없다. const 변수는 재할당할 수 없다.

Q. Assignment Operator를 많이 쓰면 왜 주의해야 해?
A. 값 변경 흐름이 복잡해져 오류 원인 추적이 어려워질 수 있다.

---

# 4. Comparison Operator

## 4.1 Comparison Operator Rules

### [개념]

Comparison Operator는 두 값을 비교해 boolean 결과를 반환하는 연산자다.

주요 연산자는 `===`, `!==`, `>`, `>=`, `<`, `<=`다.

예:

```javascript
const isAdult = age >= 20;
const isSameUser = userId === loginUserId;
```

---

### [핵심]

- Comparison Operator
- boolean result
- strict equality
- ===
- !==
- greater than
- less than
- type check
- condition
- validation

---

### [실무]

실무에서는 `==`와 `!=` 대신 `===`와 `!==`를 사용한다.

권장:

```javascript
const isOwner = post.userId === loginUserId;
const isEmpty = festivals.length === 0;
```

비권장:

```javascript
const isOwner = post.userId == loginUserId;
```

입력값 비교 전 타입 변환:

```javascript
const page = Number(searchParams.get("page") ?? "1");

if (page === 1) {
  loadFirstPage();
}
```

주의:

- URL query parameter는 string으로 들어올 수 있음
- Backend API 응답 id 타입 확인 필요
- 숫자 문자열과 number 비교 주의
- `NaN === NaN`은 false
- `Number.isNaN()` 사용 필요

---

### [FAQ]

Q. Comparison Operator는 뭐야?
A. 두 값을 비교해 true 또는 false를 반환하는 연산자다.

Q. ==와 === 차이는 뭐야?
A. ==는 타입 변환 후 비교하고, ===는 타입과 값을 모두 비교한다.

Q. 실무에서는 ==를 써도 돼?
A. 특별한 이유가 없다면 `===` 사용을 권장한다.

Q. URL parameter와 숫자를 비교할 때 주의할 점은?
A. URL parameter는 문자열일 수 있으므로 Number로 변환 후 비교하는 것이 안전하다.

---

## 4.2 Strict Equality Rules

### [개념]

Strict Equality는 타입과 값을 모두 비교하는 방식이다.

JavaScript에서는 `===`와 `!==`를 사용한다.

예:

```javascript
const isSame = "1" === 1; // false
const isDifferent = "1" !== 1; // true
```

---

### [핵심]

- Strict Equality
- ===
- !==
- no type coercion
- predictable comparison
- Modern JavaScript
- Review Rule
- Type Safety

---

### [실무]

Frontend Agent는 비교 로직에서 Strict Equality를 기본으로 사용해야 한다.

권장:

```javascript
function isActiveStatus(status) {
  return status === "ACTIVE";
}
```

권한 비교:

```javascript
const canEdit = userRole === "ADMIN" || userId === writerId;
```

상태 비교:

```javascript
if (requestStatus === "SUCCESS") {
  renderList();
}
```

Review Agent 기준:

```text
Comparison Review
→ == Usage Check
→ != Usage Check
→ Type Conversion Need Check
→ Strict Equality Refactor
```

---

### [FAQ]

Q. Strict Equality가 뭐야?
A. 타입 변환 없이 값과 타입을 모두 비교하는 방식이다.

Q. JavaScript에서 Strict Equality는 어떤 연산자를 써?
A. `===`와 `!==`를 사용한다.

Q. 왜 Strict Equality를 권장해?
A. 암묵적 타입 변환으로 인한 예측 불가능한 비교 결과를 줄일 수 있기 때문이다.

---

# 5. Logical Operator

## 5.1 Logical Operator Rules

### [개념]

Logical Operator는 여러 조건을 조합하거나 boolean 판단을 수행하는 연산자다.

주요 연산자는 `&&`, `||`, `!`다.

예:

```javascript
const canSubmit = isLoggedIn && keyword.trim().length > 0;
const isGuest = !isLoggedIn;
```

---

### [핵심]

- Logical Operator
- &&
- ||
- !
- boolean logic
- condition combination
- short-circuit
- validation
- UI state
- guard condition

---

### [실무]

Logical Operator는 UI 상태와 Form Validation에 자주 사용된다.

예:

```javascript
const canSubmit = keyword.trim().length > 0 && !loading;
const shouldShowEmpty = !loading && !error && items.length === 0;
```

권한 조건:

```javascript
const canEdit = isAdmin || isOwner;
```

Guard Condition:

```javascript
if (!user) {
  return "Guest";
}
```

주의:

- 복잡한 조건은 변수로 분리
- `||` 기본값은 falsy 전체를 처리함
- `0`, `false`, `""`가 유효하면 `??` 사용 검토
- 중첩 조건은 Guard Clause로 정리
- boolean 변수명은 true 의미가 명확해야 함

비권장:

```javascript
if (!loading && !error && data && data.content && data.content.length > 0) {
  render();
}
```

권장:

```javascript
const items = data?.content ?? [];
const shouldRenderList = !loading && !error && items.length > 0;

if (shouldRenderList) {
  render();
}
```

---

### [FAQ]

Q. Logical Operator는 뭐야?
A. 여러 조건을 조합하거나 boolean 값을 반전하는 연산자다.

Q. &&는 언제 써?
A. 여러 조건이 모두 true일 때만 true가 되어야 하는 경우 사용한다.

Q. ||는 언제 써?
A. 여러 조건 중 하나만 true여도 true가 되어야 하는 경우 사용한다.

Q. !는 언제 써?
A. boolean 값을 반대로 바꾸거나 값이 없는 조건을 판단할 때 사용한다.

---

## 5.2 Short-Circuit Evaluation

### [개념]

Short-Circuit Evaluation은 논리 연산에서 결과가 확정되면 뒤의 표현식을 평가하지 않는 동작이다.

예:

```javascript
const title = festival && festival.title;
```

`festival`이 falsy이면 `festival.title`은 평가되지 않는다.

---

### [핵심]

- Short-Circuit Evaluation
- &&
- ||
- conditional execution
- default value caution
- optional chaining alternative
- null guard
- UI condition

---

### [실무]

과거에는 short-circuit으로 null 방어를 자주 작성했다.

기존 방식:

```javascript
const title = festival && festival.title;
```

Modern JavaScript 권장:

```javascript
const title = festival?.title ?? "제목 없음";
```

조건부 실행:

```javascript
isLoggedIn && showProfile();
```

주의:

- `&&` 조건부 실행은 간단할 때만 사용
- 복잡한 로직은 if문 사용
- `||` 기본값은 falsy 전체 처리
- optional chaining과 nullish coalescing이 더 명확한 경우가 많음

비권장:

```javascript
const count = response.count || 10;
```

`count`가 0이어도 10으로 바뀔 수 있다.

권장:

```javascript
const count = response.count ?? 10;
```

---

### [FAQ]

Q. Short-Circuit Evaluation이 뭐야?
A. 논리 연산에서 결과가 확정되면 뒤의 표현식을 평가하지 않는 동작이다.

Q. &&로 null 방어를 해도 돼?
A. 가능하지만 Modern JavaScript에서는 optional chaining이 더 명확한 경우가 많다.

Q. `||` 기본값 처리는 언제 위험해?
A. 0, false, 빈 문자열도 기본값으로 덮어쓸 수 있을 때 위험하다.

---

# 6. Ternary Operator

## 6.1 Ternary Operator Rules

### [개념]

Ternary Operator는 조건에 따라 두 값 중 하나를 선택하는 연산자다.

형식:

```javascript
condition ? valueWhenTrue : valueWhenFalse;
```

예:

```javascript
const buttonText = loading ? "처리 중..." : "검색";
```

---

### [핵심]

- Ternary Operator
- conditional value
- simple condition
- UI text
- class name
- display state
- avoid nested ternary
- readability

---

### [실무]

Ternary Operator는 짧은 조건부 값 선택에 적합하다.

UI 문구:

```javascript
const buttonText = loading ? "저장 중..." : "저장";
```

CSS class 선택:

```javascript
const buttonClassName = isActive ? "button active" : "button";
```

상태 메시지:

```javascript
const emptyMessage = items.length === 0 ? "데이터가 없습니다." : "";
```

주의:

- 복잡한 조건은 if문 또는 함수로 분리
- 중첩 삼항 연산자 지양
- 긴 JSX 조건부 렌더링으로 이어질 경우 가독성 저하
- Review Agent는 nested ternary를 검토해야 함

비권장:

```javascript
const message = loading
  ? "로딩"
  : error
    ? "오류"
    : items.length === 0
      ? "없음"
      : "성공";
```

권장:

```javascript
function getListMessage({ loading, error, items }) {
  if (loading) {
    return "로딩";
  }

  if (error) {
    return "오류";
  }

  if (items.length === 0) {
    return "없음";
  }

  return "성공";
}
```

---

### [FAQ]

Q. Ternary Operator는 뭐야?
A. 조건에 따라 두 값 중 하나를 선택하는 연산자다.

Q. 삼항 연산자는 언제 써?
A. 짧고 단순한 조건부 값 선택에 사용한다.

Q. 중첩 삼항 연산자는 왜 피해야 해?
A. 조건 흐름을 읽기 어렵게 만들어 Review와 Debugging이 어려워지기 때문이다.

---

# 7. Optional Chaining

## 7.1 Optional Chaining Rules

### [개념]

Optional Chaining은 객체의 중첩 property에 안전하게 접근하기 위한 연산자다.

값이 `null` 또는 `undefined`이면 오류를 발생시키지 않고 `undefined`를 반환한다.

예:

```javascript
const title = festival?.title;
const regionName = festival?.region?.name;
```

---

### [핵심]

- Optional Chaining
- ?.
- null guard
- undefined guard
- nested object
- API response
- safe access
- Cannot read properties of undefined
- default value

---

### [실무]

API 응답 처리에서 Optional Chaining은 필수적으로 사용된다.

예:

```javascript
const festivals = response?.data?.content ?? [];
const imageUrl = festival?.imageUrl ?? "/default.png";
const writerName = review?.writer?.name ?? "익명";
```

배열 요소 접근:

```javascript
const firstTitle = response?.data?.content?.[0]?.title ?? "제목 없음";
```

주의:

- Optional Chaining은 접근 오류를 막지만 데이터 검증을 대신하지 않는다.
- 값이 없을 때 기본값이 필요하면 `??`와 함께 사용한다.
- 지나치게 긴 optional chaining은 응답 구조 복잡도를 드러낸다.
- API Response Mapping 함수로 분리하는 것이 좋다.

예:

```javascript
function normalizeFestivalResponse(response) {
  return response?.data?.content ?? [];
}
```

---

### [FAQ]

Q. Optional Chaining은 뭐야?
A. 중첩 객체 접근 시 null 또는 undefined로 인한 오류를 줄이는 연산자다.

Q. Optional Chaining은 어떤 기호를 써?
A. `?.`를 사용한다.

Q. Optional Chaining만 쓰면 기본값도 설정돼?
A. 아니다. 기본값이 필요하면 `??`와 함께 사용한다.

Q. Cannot read properties of undefined 오류를 줄이려면 어떻게 해?
A. optional chaining, null check, 기본값 처리를 적용한다.

---

# 8. Nullish Coalescing

## 8.1 Nullish Coalescing Rules

### [개념]

Nullish Coalescing은 값이 `null` 또는 `undefined`일 때만 기본값을 적용하는 연산자다.

기호는 `??`다.

예:

```javascript
const displayName = userName ?? "Guest";
```

---

### [핵심]

- Nullish Coalescing
- ??
- null
- undefined
- default value
- fallback
- 0 valid
- false valid
- empty string caution
- API response default

---

### [실무]

Nullish Coalescing은 API 응답 기본값 처리에 적합하다.

예:

```javascript
const reviewCount = festival.reviewCount ?? 0;
const isFavorite = festival.isFavorite ?? false;
const imageUrl = festival.imageUrl ?? "/default.png";
```

`||`와 비교:

```javascript
const countA = festival.reviewCount || 10;
const countB = festival.reviewCount ?? 10;
```

`reviewCount`가 0일 때:

- `countA`: 10
- `countB`: 0

주의:

- `??`는 null / undefined만 기본값 처리
- `||`는 falsy 값 전체를 기본값 처리
- count, rating, boolean 값에는 `??`가 안전한 경우가 많음
- 빈 문자열도 유효한 값인지 확인 필요

---

### [FAQ]

Q. Nullish Coalescing은 뭐야?
A. 값이 null 또는 undefined일 때만 기본값을 적용하는 연산자다.

Q. `??`와 `||` 차이는 뭐야?
A. `??`는 null 또는 undefined만 처리하고, `||`는 false, 0, 빈 문자열도 기본값으로 처리할 수 있다.

Q. count 기본값에는 `??`가 왜 좋아?
A. count가 0일 때도 유효한 값으로 유지할 수 있기 때문이다.

Q. Optional Chaining과 같이 쓸 수 있어?
A. 가능하다. `response?.data?.content ?? []`처럼 자주 함께 사용한다.

---

# 9. Condition

## 9.1 Condition Concept

### [개념]

Condition은 조건에 따라 실행 흐름을 나누는 문법이다.

JavaScript에서는 `if`, `else if`, `else`, `switch`, ternary operator를 사용한다.

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

- Condition
- if
- else if
- else
- switch
- ternary operator
- truthy
- falsy
- guard clause
- validation
- UI state
- control flow

---

### [실무]

Frontend 조건문은 UI 상태 판단과 사용자 입력 검증에 사용된다.

예:

```javascript
function getDisplayName(user) {
  if (!user) {
    return "Guest";
  }

  return user.name;
}
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

주의:

- 조건문은 명확한 boolean 조건으로 작성
- 중첩 조건은 Guard Clause로 줄이기
- 복잡한 조건식은 변수나 함수로 분리
- truthy / falsy에 의존할 때 유효한 falsy 값 주의
- UI 상태는 loading / error / empty / success 순서로 판단

---

### [FAQ]

Q. Condition은 뭐야?
A. 조건에 따라 실행 흐름을 나누는 문법이다.

Q. JavaScript 조건문에는 무엇이 있어?
A. if, else if, else, switch, ternary operator가 있다.

Q. Frontend 조건문은 어디에 많이 쓰여?
A. 입력 검증, UI 상태 표시, 권한 판단, API 응답 처리에 많이 사용된다.

---

# 10. if / else

## 10.1 if else Rules

### [개념]

`if / else`는 조건이 true인지 false인지에 따라 다른 코드를 실행하는 조건문이다.

예:

```javascript
if (keyword.trim().length === 0) {
  showError("검색어를 입력하세요.");
} else {
  search(keyword);
}
```

---

### [핵심]

- if
- else
- else if
- boolean condition
- validation
- branch
- control flow
- readability
- guard clause

---

### [실무]

`if / else`는 명확한 분기와 예외 처리에 적합하다.

Form Validation:

```javascript
function validateKeyword(keyword) {
  if (keyword.trim().length === 0) {
    return false;
  }

  return true;
}
```

권한 판단:

```javascript
if (!isLoggedIn) {
  redirectToLogin();
} else {
  openFavoriteModal();
}
```

주의:

- `else`가 불필요하면 Guard Clause 사용
- 중첩 if 최소화
- 조건 이름을 명확히 작성
- 조건식이 길면 변수로 분리
- early return으로 흐름 단순화

비권장:

```javascript
function submit(keyword) {
  if (keyword) {
    if (!loading) {
      search(keyword);
    }
  }
}
```

권장:

```javascript
function submit(keyword) {
  if (!keyword.trim()) {
    return;
  }

  if (loading) {
    return;
  }

  search(keyword);
}
```

---

### [FAQ]

Q. if else는 언제 써?
A. 조건에 따라 실행할 코드가 달라질 때 사용한다.

Q. else를 항상 써야 해?
A. 아니다. 예외 상황을 먼저 return하는 Guard Clause가 더 읽기 쉬운 경우가 많다.

Q. 중첩 if는 왜 줄여야 해?
A. 코드 흐름이 복잡해지고 오류 원인 추적이 어려워지기 때문이다.

---

# 11. Guard Clause

## 11.1 Guard Clause Rules

### [개념]

Guard Clause는 예외 상황이나 처리할 필요가 없는 조건을 함수 초반에 먼저 반환하는 방식이다.

중첩 조건문을 줄이고 정상 흐름을 명확하게 만든다.

예:

```javascript
function getDisplayName(user) {
  if (!user) {
    return "Guest";
  }

  return user.name;
}
```

---

### [핵심]

- Guard Clause
- early return
- validation
- exception condition
- nested if reduction
- readability
- function flow
- frontend form handling

---

### [실무]

Frontend Form Handling에서 Guard Clause는 매우 유용하다.

예:

```javascript
async function submitSearch(keyword) {
  const query = keyword.trim();

  if (!query) {
    return [];
  }

  if (loading) {
    return [];
  }

  return await searchFestivals(query);
}
```

API 응답 처리:

```javascript
function normalizeFestivals(response) {
  const content = response?.data?.content;

  if (!Array.isArray(content)) {
    return [];
  }

  return content;
}
```

장점:

- 중첩 조건 감소
- 실패 조건 선처리
- 정상 흐름 명확화
- Review Agent 검토 용이
- 테스트 케이스 작성 용이

---

### [FAQ]

Q. Guard Clause가 뭐야?
A. 예외 상황이나 처리하지 않을 조건을 함수 초반에 먼저 반환하는 방식이다.

Q. Guard Clause를 왜 써?
A. 중첩 조건을 줄이고 정상 흐름을 읽기 쉽게 만들기 위해 사용한다.

Q. Form Validation에도 Guard Clause를 써?
A. 적합하다. 입력값이 비었거나 요청 중이면 초반에 return할 수 있다.

---

# 12. switch

## 12.1 switch Rules

### [개념]

`switch`는 하나의 값이 여러 경우 중 어디에 해당하는지에 따라 실행 흐름을 나누는 조건문이다.

예:

```javascript
switch (status) {
  case "LOADING":
    showLoading();
    break;
  case "ERROR":
    showError();
    break;
  default:
    showContent();
}
```

---

### [핵심]

- switch
- case
- default
- break
- status branching
- enum-like value
- request status
- UI status
- readability

---

### [실무]

`switch`는 상태 값이 여러 개일 때 사용하기 좋다.

UI 상태 메시지:

```javascript
function getStatusMessage(status) {
  switch (status) {
    case "LOADING":
      return "로딩 중입니다.";
    case "ERROR":
      return "오류가 발생했습니다.";
    case "EMPTY":
      return "데이터가 없습니다.";
    case "SUCCESS":
      return "조회 성공";
    default:
      return "알 수 없는 상태입니다.";
  }
}
```

주의:

- `default` 포함
- fall-through 의도 없으면 `break` 또는 `return` 사용
- case 값은 상수화 가능
- 단순 boolean 조건에는 if문이 더 적합
- 복잡한 로직은 별도 함수로 분리

---

### [FAQ]

Q. switch는 언제 써?
A. 하나의 값이 여러 상태 중 하나로 나뉘는 경우 사용한다.

Q. switch에서 default는 왜 필요해?
A. 예상하지 못한 값에 대한 fallback 처리를 위해 필요하다.

Q. switch와 if 중 뭐를 써야 해?
A. 단순 true / false 조건은 if, 여러 고정 상태 값 분기는 switch가 적합하다.

---

# 13. Loop

## 13.1 Loop Concept

### [개념]

Loop는 반복 작업을 처리하는 문법이다.

JavaScript에서는 `for`, `while`, `for...of`, `for...in`과 Array Method를 사용할 수 있다.

Frontend에서는 목록 데이터 처리에 Loop와 Array Method가 자주 사용된다.

---

### [핵심]

- Loop
- for
- while
- for...of
- for...in
- break
- continue
- Array Method
- map
- filter
- reduce
- list processing
- API response list

---

### [실무]

Frontend에서는 배열 데이터 처리에 Array Method를 우선 고려한다.

목록 변환:

```javascript
const titles = festivals.map((festival) => festival.title);
```

반복 실행:

```javascript
for (const festival of festivals) {
  console.log(festival.title);
}
```

주의:

- 새 배열 생성 목적이면 `map`
- 조건 필터링은 `filter`
- 첫 요소 검색은 `find`
- 누적 계산은 `reduce`
- 단순 반복 실행은 `for...of` 또는 `forEach`
- 객체 key 순회는 `Object.keys`, `Object.entries`, `for...in`
- 배열에 `for...in` 사용 지양

---

### [FAQ]

Q. Loop는 뭐야?
A. 같은 작업을 여러 번 반복하기 위한 문법이다.

Q. Frontend에서 Loop는 어디에 많이 쓰여?
A. API 응답 목록 변환, 필터링, 렌더링 데이터 생성에 많이 사용된다.

Q. 배열 처리에는 for문과 Array Method 중 뭐가 좋아?
A. 변환, 필터링, 검색 목적이 명확하면 Array Method를 우선 고려한다.

---

# 14. for Loop

## 14.1 for Loop Rules

### [개념]

`for`문은 반복 횟수가 명확할 때 사용하는 기본 반복문이다.

예:

```javascript
for (let i = 0; i < festivals.length; i += 1) {
  console.log(festivals[i].title);
}
```

---

### [핵심]

- for
- index
- counter
- iteration
- array length
- loop condition
- increment
- break
- continue

---

### [실무]

`for`문은 index가 필요한 반복에 적합하다.

예:

```javascript
for (let index = 0; index < festivals.length; index += 1) {
  const festival = festivals[index];

  console.log(`${index + 1}. ${festival.title}`);
}
```

하지만 단순 배열 변환에는 `map`이 더 명확하다.

비권장:

```javascript
const titles = [];

for (let i = 0; i < festivals.length; i += 1) {
  titles.push(festivals[i].title);
}
```

권장:

```javascript
const titles = festivals.map((festival) => festival.title);
```

주의:

- index 변수명 의미 있게 사용
- off-by-one error 주의
- 배열 길이 조건 확인
- 단순 변환은 map 사용
- 원본 배열 변경 여부 확인

---

### [FAQ]

Q. for문은 언제 써?
A. 반복 횟수나 index 제어가 명확히 필요한 경우 사용한다.

Q. 배열 변환에도 for문을 써야 해?
A. 가능하지만 새 배열 변환 목적이면 map이 더 명확한 경우가 많다.

Q. off-by-one error가 뭐야?
A. 반복 시작이나 종료 조건이 하나 차이로 잘못되어 발생하는 오류다.

---

# 15. for...of

## 15.1 for...of Rules

### [개념]

`for...of`는 배열 같은 iterable 값의 요소를 순서대로 순회하는 반복문이다.

예:

```javascript
for (const festival of festivals) {
  console.log(festival.title);
}
```

---

### [핵심]

- for...of
- iterable
- array
- value iteration
- readable loop
- break
- continue
- async caution

---

### [실무]

`for...of`는 배열 요소를 직접 사용해야 할 때 가독성이 좋다.

예:

```javascript
function countActiveFestivals(festivals) {
  let count = 0;

  for (const festival of festivals) {
    if (festival.active) {
      count += 1;
    }
  }

  return count;
}
```

비동기 순차 처리 예:

```javascript
for (const festival of festivals) {
  await sendFestivalLog(festival);
}
```

주의:

- 배열 요소 순회에는 `for...of`
- 객체 key 순회에는 `for...in` 또는 `Object.keys`
- 모든 요소를 순차 await하면 느릴 수 있음
- 병렬 요청이 가능하면 `Promise.all` 검토
- 단순 변환은 `map`이 더 적합할 수 있음

---

### [FAQ]

Q. for...of는 언제 써?
A. 배열 같은 iterable의 요소를 하나씩 직접 순회할 때 사용한다.

Q. for...of와 for...in 차이는 뭐야?
A. for...of는 값 순회, for...in은 객체 key 순회에 사용한다.

Q. 비동기 작업에도 for...of를 쓸 수 있어?
A. 가능하다. 순차 await가 필요할 때 사용할 수 있다.

---

# 16. for...in

## 16.1 for...in Rules

### [개념]

`for...in`은 객체의 enumerable key를 순회하는 반복문이다.

예:

```javascript
for (const key in user) {
  console.log(key, user[key]);
}
```

---

### [핵심]

- for...in
- object key
- enumerable property
- bracket notation
- Object.keys
- Object.entries
- array caution

---

### [실무]

객체 key 순회에는 `Object.keys`, `Object.values`, `Object.entries`를 더 명확하게 사용할 수 있다.

권장:

```javascript
for (const [key, value] of Object.entries(searchCondition)) {
  console.log(key, value);
}
```

비권장:

```javascript
for (const index in festivals) {
  console.log(festivals[index]);
}
```

배열 순회 권장:

```javascript
for (const festival of festivals) {
  console.log(festival.title);
}
```

주의:

- 배열 순회에는 `for...in` 지양
- 객체 key 순회 목적일 때만 사용
- prototype property까지 고려해야 하는 경우 주의
- API 응답 객체 변환에는 `Object.entries`가 더 명확할 수 있음

---

### [FAQ]

Q. for...in은 언제 써?
A. 객체의 key를 순회할 때 사용한다.

Q. 배열 순회에 for...in을 써도 돼?
A. 지양한다. 배열 요소 순회에는 for...of나 Array Method가 적합하다.

Q. Object.entries는 언제 써?
A. 객체의 key와 value를 함께 순회할 때 사용한다.

---

# 17. while

## 17.1 while Rules

### [개념]

`while`문은 조건이 true인 동안 반복 실행하는 반복문이다.

반복 횟수가 명확하지 않고 조건 기반으로 반복할 때 사용한다.

예:

```javascript
let count = 0;

while (count < 3) {
  count += 1;
}
```

---

### [핵심]

- while
- condition based loop
- repeat until false
- infinite loop caution
- counter update
- break
- polling caution

---

### [실무]

Frontend Foundation에서는 `while` 사용 빈도가 낮다.

적합한 경우:

- 조건이 false가 될 때까지 반복
- 특정 값 탐색
- 단순 알고리즘 처리

주의:

- 종료 조건 누락 시 infinite loop 발생
- UI Thread를 막을 수 있음
- API polling에 무분별한 while 사용 금지
- 반복 횟수가 명확하면 for문 사용
- 배열 처리는 Array Method 우선

비권장:

```javascript
while (true) {
  fetch("/api/status");
}
```

권장:

```javascript
const intervalId = setInterval(checkStatus, 5000);
```

---

### [FAQ]

Q. while은 언제 써?
A. 반복 횟수보다 조건이 더 중요한 경우 사용한다.

Q. while에서 가장 주의할 점은?
A. 종료 조건이 없으면 infinite loop가 발생할 수 있다.

Q. API polling에 while true를 써도 돼?
A. 안 된다. UI를 막거나 과도한 요청을 만들 수 있으므로 timer나 별도 제어 방식을 사용한다.

---

# 18. break and continue

## 18.1 break and continue Rules

### [개념]

`break`는 반복문을 즉시 종료한다.

`continue`는 현재 반복을 건너뛰고 다음 반복으로 넘어간다.

예:

```javascript
for (const festival of festivals) {
  if (!festival.active) {
    continue;
  }

  if (festival.title === "Target Festival") {
    break;
  }
}
```

---

### [핵심]

- break
- continue
- loop control
- early exit
- skip iteration
- search logic
- readability
- guard condition

---

### [실무]

`break`는 원하는 값을 찾으면 반복을 멈출 때 사용한다.

```javascript
let targetFestival = null;

for (const festival of festivals) {
  if (festival.id === targetId) {
    targetFestival = festival;
    break;
  }
}
```

하지만 단순 검색은 `find`가 더 명확하다.

```javascript
const targetFestival =
  festivals.find((festival) => festival.id === targetId) ?? null;
```

`continue`는 처리하지 않을 항목을 건너뛰는 데 사용한다.

```javascript
for (const festival of festivals) {
  if (!festival.active) {
    continue;
  }

  renderFestival(festival);
}
```

주의:

- break / continue가 많으면 흐름 파악 어려움
- 단순 검색은 find 사용
- 단순 필터링은 filter 사용
- 복잡한 반복은 함수로 분리

---

### [FAQ]

Q. break는 뭐야?
A. 반복문을 즉시 종료하는 문법이다.

Q. continue는 뭐야?
A. 현재 반복을 건너뛰고 다음 반복으로 넘어가는 문법이다.

Q. 배열에서 특정 요소를 찾을 때 break를 써야 해?
A. 가능하지만 단순 검색이면 `find`가 더 명확하다.

---

# 19. Array Method as Loop Alternative

## 19.1 Array Method Rules

### [개념]

Array Method는 배열 반복 작업을 목적에 맞는 함수로 처리하는 방식이다.

Frontend에서는 `map`, `filter`, `find`, `reduce`, `some`, `every`, `forEach`가 자주 사용된다.

---

### [핵심]

- Array Method
- map
- filter
- find
- reduce
- some
- every
- forEach
- list transformation
- list filtering
- API response processing
- React list rendering

---

### [실무]

Array Method 선택 기준:

| 목적                     | 권장 메서드           |
| ------------------------ | --------------------- |
| 새 배열 변환             | map                   |
| 조건에 맞는 목록 추출    | filter                |
| 첫 번째 요소 검색        | find                  |
| 누적 계산                | reduce                |
| 하나라도 만족하는지 확인 | some                  |
| 모두 만족하는지 확인     | every                 |
| 반복 실행만 필요         | forEach 또는 for...of |

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

검색:

```javascript
const selectedFestival = festivals.find(
  (festival) => festival.id === selectedId,
);
```

주의:

- `map` callback에서 return 누락 주의
- `forEach`는 새 배열을 반환하지 않음
- `sort`는 원본 배열 변경
- 배열이 아닌 값에 Array Method 호출 금지
- API 응답 목록은 `Array.isArray()` 또는 `?? []`로 방어

---

### [FAQ]

Q. Array Method는 왜 중요해?
A. Frontend API 응답 목록을 변환, 필터링, 검색, 렌더링 데이터로 가공할 때 자주 사용되기 때문이다.

Q. map과 forEach 차이는 뭐야?
A. map은 새 배열을 반환하고 forEach는 반환값 없이 반복 실행만 한다.

Q. filter와 find 차이는 뭐야?
A. filter는 조건에 맞는 모든 요소 배열을 반환하고 find는 첫 번째 요소 하나를 반환한다.

Q. reduce는 언제 써?
A. 배열을 하나의 값으로 누적 계산할 때 사용한다.

---

# 20. Operator, Condition, Loop Common Mistakes

## 20.1 Common Mistakes

### [개념]

Operator, Condition, Loop 실수는 Frontend UI 오류, API 응답 처리 오류, Form Validation 오류로 이어질 수 있다.

Review Agent는 비교 연산, null 방어, 조건 분기, 반복문 목적, 배열 메서드 선택을 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- `==` 사용
- `!=` 사용
- `||`로 0 또는 false 덮어쓰기
- 복잡한 조건식 방치
- 중첩 if 과다
- Guard Clause 미사용
- nested ternary 남용
- switch default 누락
- for loop off-by-one error
- 배열 순회에 for...in 사용
- while 종료 조건 누락
- 배열이 아닌 값에 map 호출
- map callback return 누락
- forEach 결과를 새 배열로 착각
- sort 원본 변경 인지 못함
- API 응답 목록 null 방어 누락

---

### [실무]

Review Flow:

```text
Code Review
→ Comparison Operator Check
→ Strict Equality Check
→ Logical Operator Check
→ Nullish Default Check
→ Condition Complexity Check
→ Guard Clause Check
→ Loop Purpose Check
→ Array Method Selection Check
→ API Response List Safety Check
```

나쁜 예:

```javascript
if (response.data.content.length != 0) {
  const titles = response.data.content.forEach((item) => item.title);
}
```

개선 예:

```javascript
const content = response?.data?.content;
const festivals = Array.isArray(content) ? content : [];

if (festivals.length === 0) {
  return [];
}

const titles = festivals.map((festival) => festival.title);
```

주의:

- 비교는 `===`, `!==` 사용
- 응답 구조는 optional chaining으로 접근
- 목록은 배열 확인 후 처리
- 새 배열이 필요하면 map 사용
- 조건이 길면 변수 또는 함수로 분리
- 상태 분기는 loading / error / empty / success 순서 고려

---

### [FAQ]

Q. Operator에서 가장 흔한 실수는 뭐야?
A. `==` 사용, `||` 기본값 처리로 0이나 false를 덮어쓰기, 복잡한 조건식을 방치하는 것이다.

Q. Condition에서 가장 흔한 실수는 뭐야?
A. 중첩 if 과다, Guard Clause 미사용, nested ternary 남용, 상태 분기 순서 오류다.

Q. Loop에서 가장 흔한 실수는 뭐야?
A. 배열에 for...in 사용, map return 누락, forEach 반환값 오해, 배열 아닌 값에 map 호출이다.

Q. Review Agent는 무엇을 우선 검토해야 해?
A. Strict Equality, null 방어, 조건 복잡도, Guard Clause, 배열 메서드 선택, API 응답 목록 안전성을 우선 검토해야 한다.

---

# 21. Operator, Condition, Loop Checklist

## 21.1 Document Quality Checklist

### [개념]

Operator, Condition, Loop 문서는 Frontend Agent가 실행 흐름과 데이터 반복 처리를 안전하게 작성하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] Arithmetic Operator 설명이 포함되었는가?
- [ ] Assignment Operator 설명이 포함되었는가?
- [ ] Comparison Operator 설명이 포함되었는가?
- [ ] Strict Equality 기준이 포함되었는가?
- [ ] Logical Operator 설명이 포함되었는가?
- [ ] Short-Circuit Evaluation 주의사항이 포함되었는가?
- [ ] Ternary Operator 사용 기준이 포함되었는가?
- [ ] Optional Chaining 설명이 포함되었는가?
- [ ] Nullish Coalescing 설명이 포함되었는가?
- [ ] Condition 설명이 포함되었는가?
- [ ] if / else 설명이 포함되었는가?
- [ ] Guard Clause 설명이 포함되었는가?
- [ ] switch 사용 기준이 포함되었는가?
- [ ] Loop 설명이 포함되었는가?
- [ ] for / for...of / for...in / while 설명이 포함되었는가?
- [ ] break / continue 설명이 포함되었는가?
- [ ] Array Method 대안 기준이 포함되었는가?
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
→ Operator Rule Check
→ Condition Flow Check
→ Loop and Array Method Check
→ Frontend Practical Example Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part02_Variable_Data_Type
→ JavaScript_Foundation_Part03_Operator_Condition_Loop
→ JavaScript_Foundation_Part04_Function_Scope_Closure
```

---

### [FAQ]

Q. Operator, Condition, Loop 문서 검수에서 가장 중요한 것은 뭐야?
A. Strict Equality, Optional Chaining, Nullish Coalescing, Guard Clause, Array Method 선택 기준, Common Mistakes 포함 여부다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React 조건부 렌더링, 이벤트 처리, 상태 계산, 목록 렌더링은 Operator, Condition, Loop 이해가 기반이다.

Q. 다음 Part와 어떻게 연결돼?
A. Part03은 실행 흐름과 반복 처리 기준을 만들고, Part04는 Function, Scope, Closure로 로직 재사용과 상태 참조를 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. JavaScript Operator가 뭐야?
A. 값을 계산하거나 비교하거나 논리 판단을 수행하는 기호다.

Q. JavaScript Operator는 Frontend에서 어디에 쓰여?
A. 입력 검증, UI 상태 계산, API 응답 기본값 처리, 조건부 렌더링 로직에 쓰인다.

Q. Arithmetic Operator는 뭐야?
A. 숫자 값을 계산하는 연산자다.

Q. JavaScript에서 + 연산자는 항상 숫자 덧셈이야?
A. 아니다. 문자열이 포함되면 문자열 연결로 동작할 수 있다.

Q. input 값으로 계산할 때 주의할 점은?
A. input value는 문자열일 수 있으므로 Number로 명시적 변환 후 계산해야 한다.

Q. Assignment Operator는 뭐야?
A. 변수에 값을 할당하거나 기존 값을 갱신하는 연산자다.

Q. const 변수에 재할당할 수 있어?
A. 없다. const 변수는 재할당할 수 없다.

Q. Comparison Operator는 뭐야?
A. 두 값을 비교해 true 또는 false를 반환하는 연산자다.

Q. ==와 === 차이는 뭐야?
A. ==는 타입 변환 후 비교하고, ===는 타입과 값을 모두 비교한다.

Q. 실무에서는 ==를 써도 돼?
A. 특별한 이유가 없다면 === 사용을 권장한다.

Q. Strict Equality가 뭐야?
A. 타입 변환 없이 값과 타입을 모두 비교하는 방식이다.

Q. JavaScript에서 Strict Equality는 어떤 연산자를 써?
A. ===와 !==를 사용한다.

Q. Logical Operator는 뭐야?
A. 여러 조건을 조합하거나 boolean 값을 반전하는 연산자다.

Q. &&는 언제 써?
A. 여러 조건이 모두 true일 때만 true가 되어야 하는 경우 사용한다.

Q. ||는 언제 써?
A. 여러 조건 중 하나만 true여도 true가 되어야 하는 경우 사용한다.

Q. !는 언제 써?
A. boolean 값을 반대로 바꾸거나 값이 없는 조건을 판단할 때 사용한다.

Q. Short-Circuit Evaluation이 뭐야?
A. 논리 연산에서 결과가 확정되면 뒤의 표현식을 평가하지 않는 동작이다.

Q. `||` 기본값 처리는 언제 위험해?
A. 0, false, 빈 문자열도 기본값으로 덮어쓸 수 있을 때 위험하다.

Q. Ternary Operator는 뭐야?
A. 조건에 따라 두 값 중 하나를 선택하는 연산자다.

Q. 삼항 연산자는 언제 써?
A. 짧고 단순한 조건부 값 선택에 사용한다.

Q. 중첩 삼항 연산자는 왜 피해야 해?
A. 조건 흐름을 읽기 어렵게 만들어 Review와 Debugging이 어려워지기 때문이다.

Q. Optional Chaining은 뭐야?
A. 중첩 객체 접근 시 null 또는 undefined로 인한 오류를 줄이는 연산자다.

Q. Optional Chaining은 어떤 기호를 써?
A. ?.를 사용한다.

Q. Cannot read properties of undefined 오류를 줄이려면 어떻게 해?
A. optional chaining, null check, 기본값 처리를 적용한다.

Q. Nullish Coalescing은 뭐야?
A. 값이 null 또는 undefined일 때만 기본값을 적용하는 연산자다.

Q. `??`와 `||` 차이는 뭐야?
A. `??`는 null 또는 undefined만 처리하고, `||`는 false, 0, 빈 문자열도 기본값으로 처리할 수 있다.

Q. count 기본값에는 `??`가 왜 좋아?
A. count가 0일 때도 유효한 값으로 유지할 수 있기 때문이다.

Q. Condition은 뭐야?
A. 조건에 따라 실행 흐름을 나누는 문법이다.

Q. JavaScript 조건문에는 무엇이 있어?
A. if, else if, else, switch, ternary operator가 있다.

Q. if else는 언제 써?
A. 조건에 따라 실행할 코드가 달라질 때 사용한다.

Q. Guard Clause가 뭐야?
A. 예외 상황이나 처리하지 않을 조건을 함수 초반에 먼저 반환하는 방식이다.

Q. Guard Clause를 왜 써?
A. 중첩 조건을 줄이고 정상 흐름을 읽기 쉽게 만들기 위해 사용한다.

Q. switch는 언제 써?
A. 하나의 값이 여러 상태 중 하나로 나뉘는 경우 사용한다.

Q. switch에서 default는 왜 필요해?
A. 예상하지 못한 값에 대한 fallback 처리를 위해 필요하다.

Q. Loop는 뭐야?
A. 같은 작업을 여러 번 반복하기 위한 문법이다.

Q. JavaScript 반복문에는 뭐가 있어?
A. for, while, for...of, for...in, Array Method가 있다.

Q. for문은 언제 써?
A. 반복 횟수나 index 제어가 명확히 필요한 경우 사용한다.

Q. for...of는 언제 써?
A. 배열 같은 iterable의 요소를 하나씩 직접 순회할 때 사용한다.

Q. for...in은 언제 써?
A. 객체의 key를 순회할 때 사용한다.

Q. 배열 순회에 for...in을 써도 돼?
A. 지양한다. 배열 요소 순회에는 for...of나 Array Method가 적합하다.

Q. while은 언제 써?
A. 반복 횟수보다 조건이 더 중요한 경우 사용한다.

Q. while에서 가장 주의할 점은?
A. 종료 조건이 없으면 infinite loop가 발생할 수 있다.

Q. break는 뭐야?
A. 반복문을 즉시 종료하는 문법이다.

Q. continue는 뭐야?
A. 현재 반복을 건너뛰고 다음 반복으로 넘어가는 문법이다.

Q. Array Method는 왜 중요해?
A. Frontend API 응답 목록을 변환, 필터링, 검색, 렌더링 데이터로 가공할 때 자주 사용되기 때문이다.

Q. map과 forEach 차이는 뭐야?
A. map은 새 배열을 반환하고 forEach는 반환값 없이 반복 실행만 한다.

Q. filter와 find 차이는 뭐야?
A. filter는 조건에 맞는 모든 요소 배열을 반환하고 find는 첫 번째 요소 하나를 반환한다.

Q. reduce는 언제 써?
A. 배열을 하나의 값으로 누적 계산할 때 사용한다.

Q. Operator에서 가장 흔한 실수는 뭐야?
A. == 사용, || 기본값 처리로 0이나 false를 덮어쓰기, 복잡한 조건식을 방치하는 것이다.

Q. Condition에서 가장 흔한 실수는 뭐야?
A. 중첩 if 과다, Guard Clause 미사용, nested ternary 남용, 상태 분기 순서 오류다.

Q. Loop에서 가장 흔한 실수는 뭐야?
A. 배열에 for...in 사용, map return 누락, forEach 반환값 오해, 배열 아닌 값에 map 호출이다.

Q. JavaScript Foundation Part03 다음에는 무엇을 다뤄야 해?
A. Function, Scope, Closure를 다루는 Part04로 이어지는 것이 좋다.
