# JavaScript Foundation Part06 - DOM, Event, and Form Handling

---

# 1. DOM

## 1.1 DOM Concept

### [개념]

DOM은 Document Object Model의 약자다.

DOM은 HTML 문서를 JavaScript가 읽고 조작할 수 있는 객체 구조로 표현한 것이다.

Browser JavaScript는 DOM을 통해 화면 요소를 선택하고, 내용을 변경하고, class를 제어하고, 사용자 Event에 반응한다.

예:

```javascript
const titleElement = document.querySelector(".page-title");

titleElement.textContent = "Festival List";
```

---

### [핵심]

- DOM
- Document Object Model
- document
- window
- HTML document
- DOM Tree
- DOM Element
- querySelector
- textContent
- classList
- Event Handling
- Browser JavaScript
- React Foundation

---

### [실무]

2026 실무 기준에서 DOM 조작은 Browser JavaScript의 기본 동작 이해에 필요하다.

Frontend Agent는 DOM을 아래 목적에 사용한다.

- HTML 요소 선택
- 텍스트 변경
- class 추가 / 제거
- 사용자 입력값 읽기
- Event Listener 등록
- Form Submit 처리
- Browser 동작 이해
- React의 state 기반 UI 갱신 원리 이해

DOM 처리 Flow:

```text
HTML Document
→ DOM Tree
→ Element Selection
→ JavaScript Logic
→ DOM Update
→ UI Change
```

주의:

- DOM 요소 선택 결과는 null일 수 있다.
- 요소 접근 전 null check가 필요하다.
- `innerHTML`에 사용자 입력을 직접 넣으면 XSS 위험이 있다.
- React에서는 직접 DOM 조작보다 state / props 기반 렌더링을 우선한다.
- DOM 문서는 React 학습 전 Browser 동작 기반으로 이해한다.

---

### [FAQ]

Q. DOM이 뭐야?
A. HTML 문서를 JavaScript가 읽고 조작할 수 있도록 만든 객체 구조다.

Q. DOM은 왜 필요해?
A. JavaScript가 화면 요소를 선택하고 변경하고 사용자 이벤트에 반응하기 위해 필요하다.

Q. React에서도 DOM을 직접 조작해?
A. 대부분 직접 조작하지 않는다. React에서는 state와 props 기반으로 UI를 갱신한다.

Q. DOM 문서는 React와 관련 있어?
A. 관련 있다. React가 실제로는 Browser DOM 변경을 효율적으로 관리하기 때문이다.

---

# 2. document and window

## 2.1 document Rules

### [개념]

`document`는 현재 웹 페이지의 HTML 문서를 나타내는 Browser 객체다.

JavaScript는 `document`를 통해 DOM 요소를 선택하고 조작한다.

예:

```javascript
const appElement = document.querySelector("#app");
```

---

### [핵심]

- document
- HTML document
- DOM selection
- querySelector
- querySelectorAll
- getElementById
- createElement
- body
- head
- DOM API

---

### [실무]

`document`는 DOM 요소 접근의 시작점이다.

예:

```javascript
const searchForm = document.querySelector(".search-form");
const keywordInput = document.querySelector("#keyword");
const listElement = document.querySelector(".festival-list");
```

주의:

- DOM이 아직 로드되지 않았으면 요소 선택 결과가 null일 수 있다.
- Script 실행 위치와 DOMContentLoaded 시점을 고려한다.
- 선택한 요소는 존재 여부를 확인한 뒤 사용한다.
- React 프로젝트에서는 `document.querySelector`를 남용하지 않는다.
- 직접 DOM 조작이 필요한 경우 목적을 명확히 한다.

안전한 접근:

```javascript
const titleElement = document.querySelector(".page-title");

if (titleElement) {
  titleElement.textContent = "Festival List";
}
```

---

### [FAQ]

Q. document는 뭐야?
A. 현재 웹 페이지의 HTML 문서를 나타내는 Browser 객체다.

Q. document는 어디에 써?
A. DOM 요소를 선택하거나 생성하거나 조작할 때 사용한다.

Q. document.querySelector 결과는 항상 있어?
A. 아니다. 조건에 맞는 요소가 없으면 null을 반환한다.

---

## 2.2 window Rules

### [개념]

`window`는 Browser 환경의 최상위 객체다.

`window`는 현재 브라우저 탭, 화면, URL, 저장소, timer, 전역 객체 접근과 관련된다.

예:

```javascript
console.log(window.location.href);
```

---

### [핵심]

- window
- browser global object
- location
- localStorage
- sessionStorage
- setTimeout
- setInterval
- alert
- resize event
- scroll event

---

### [실무]

`window`는 Browser 환경 기능을 사용할 때 접근한다.

URL 이동:

```javascript
window.location.href = "/login";
```

Timer:

```javascript
const timerId = window.setTimeout(() => {
  console.log("timeout");
}, 1000);
```

Storage:

```javascript
window.localStorage.setItem("theme", "dark");
```

주의:

- Browser 전역 객체에 의존하면 테스트가 어려울 수 있다.
- window에 임의 property를 추가하는 것은 지양한다.
- 민감정보를 localStorage에 저장할 때 주의한다.
- SSR 환경에서는 window가 없을 수 있다.
- React / Next.js 전환 시 window 접근 시점에 주의해야 한다.

---

### [FAQ]

Q. window는 뭐야?
A. Browser 환경의 최상위 전역 객체다.

Q. window는 어디에 사용돼?
A. URL, timer, storage, 화면 크기, scroll 같은 브라우저 기능에 사용된다.

Q. window에 값을 저장해도 돼?
A. 지양한다. 전역 상태 오염과 충돌 위험이 있다.

Q. SSR 환경에서도 window를 바로 쓸 수 있어?
A. 아니다. 서버 환경에는 window가 없을 수 있다.

---

# 3. DOM Selection

## 3.1 querySelector Rules

### [개념]

`querySelector`는 CSS selector와 일치하는 첫 번째 DOM 요소를 반환한다.

조건에 맞는 요소가 없으면 null을 반환한다.

예:

```javascript
const button = document.querySelector(".submit-button");
```

---

### [핵심]

- querySelector
- CSS selector
- first matched element
- null return
- DOM selection
- class selector
- id selector
- element selector
- null check

---

### [실무]

`querySelector`는 단일 요소 선택에 적합하다.

예:

```javascript
const form = document.querySelector(".search-form");
const keywordInput = document.querySelector("#keyword");
const title = document.querySelector("h1");
```

안전한 사용:

```javascript
const button = document.querySelector(".submit-button");

if (!button) {
  throw new Error("Submit button not found");
}

button.textContent = "검색";
```

주의:

- 첫 번째 요소만 반환한다.
- 없으면 null을 반환한다.
- selector 오타를 확인해야 한다.
- 요소가 여러 개면 `querySelectorAll`을 사용한다.
- DOM 로드 시점 이후에 선택해야 한다.
- Review Agent는 null check 없이 DOM property 접근하는 코드를 검토해야 한다.

---

### [FAQ]

Q. querySelector는 뭐야?
A. CSS selector와 일치하는 첫 번째 DOM 요소를 반환하는 메서드다.

Q. querySelector 결과가 없으면 뭐가 나와?
A. null이 반환된다.

Q. querySelector는 여러 요소를 반환해?
A. 아니다. 첫 번째 요소 하나만 반환한다.

Q. querySelector 사용 시 가장 주의할 점은?
A. 결과가 null일 수 있으므로 접근 전 확인해야 한다.

---

## 3.2 querySelectorAll Rules

### [개념]

`querySelectorAll`은 CSS selector와 일치하는 모든 DOM 요소를 NodeList로 반환한다.

예:

```javascript
const buttons = document.querySelectorAll(".filter-button");
```

---

### [핵심]

- querySelectorAll
- CSS selector
- NodeList
- multiple elements
- forEach
- array conversion
- DOM list
- event binding

---

### [실무]

여러 DOM 요소에 동일한 처리를 적용할 때 사용한다.

예:

```javascript
const buttons = document.querySelectorAll(".filter-button");

buttons.forEach((button) => {
  button.addEventListener("click", handleFilterClick);
});
```

Array Method가 필요하면 배열로 변환한다.

```javascript
const buttonList = Array.from(document.querySelectorAll(".filter-button"));

const activeButtons = buttonList.filter((button) =>
  button.classList.contains("active"),
);
```

주의:

- 반환값은 Array가 아니라 NodeList다.
- NodeList는 일부 Array Method를 바로 사용할 수 없다.
- 요소가 없어도 빈 NodeList가 반환된다.
- 반복 Event 등록 시 중복 등록에 주의한다.
- 동적으로 추가된 요소에는 기존 NodeList가 자동 반영되지 않을 수 있다.

---

### [FAQ]

Q. querySelectorAll은 뭐야?
A. CSS selector와 일치하는 모든 DOM 요소를 NodeList로 반환하는 메서드다.

Q. querySelectorAll 결과가 없으면 뭐가 나와?
A. 빈 NodeList가 반환된다.

Q. NodeList는 Array야?
A. 아니다. 필요하면 Array.from으로 배열로 변환할 수 있다.

Q. 여러 버튼에 이벤트를 등록할 때 querySelectorAll을 써도 돼?
A. 가능하다. 다만 중복 등록과 동적 요소 추가를 주의해야 한다.

---

## 3.3 getElementById Rules

### [개념]

`getElementById`는 지정한 id와 일치하는 DOM 요소를 반환한다.

조건에 맞는 요소가 없으면 null을 반환한다.

예:

```javascript
const keywordInput = document.getElementById("keyword");
```

---

### [핵심]

- getElementById
- id selection
- single element
- null return
- fast selection
- DOM element
- unique id

---

### [실무]

id가 명확한 단일 요소를 선택할 때 사용할 수 있다.

예:

```javascript
const searchInput = document.getElementById("search-keyword");

if (searchInput) {
  searchInput.value = "";
}
```

주의:

- id는 HTML 문서에서 고유해야 한다.
- 결과가 null일 수 있다.
- CSS selector 문법이 아니라 id 문자열만 전달한다.
- `#keyword`가 아니라 `"keyword"`를 전달한다.
- class 기반 선택은 `querySelector`를 사용한다.

---

### [FAQ]

Q. getElementById는 뭐야?
A. 지정한 id와 일치하는 DOM 요소를 반환하는 메서드다.

Q. getElementById에 #을 붙여야 해?
A. 아니다. `getElementById("keyword")`처럼 id 문자열만 전달한다.

Q. getElementById 결과가 없으면 뭐가 나와?
A. null이 반환된다.

---

# 4. DOM Manipulation

## 4.1 textContent Rules

### [개념]

`textContent`는 DOM 요소의 텍스트 내용을 읽거나 변경하는 property다.

HTML로 해석하지 않고 텍스트 그대로 처리한다.

예:

```javascript
titleElement.textContent = "Festival List";
```

---

### [핵심]

- textContent
- text update
- safe text insertion
- no HTML parsing
- XSS prevention
- UI message
- DOM update

---

### [실무]

사용자 입력이나 API 응답 텍스트를 화면에 표시할 때는 `textContent`를 우선 사용한다.

예:

```javascript
function renderTitle(title) {
  const titleElement = document.querySelector(".festival-title");

  if (!titleElement) {
    return;
  }

  titleElement.textContent = title ?? "제목 없음";
}
```

주의:

- HTML 태그를 해석하지 않는다.
- 사용자 입력 출력에는 `innerHTML`보다 안전하다.
- 요소가 null인지 확인한다.
- 텍스트만 변경할 때 적합하다.
- 줄바꿈이나 HTML 구조가 필요하면 별도 DOM 생성 방식을 고려한다.

---

### [FAQ]

Q. textContent는 뭐야?
A. DOM 요소의 텍스트 내용을 읽거나 변경하는 property다.

Q. textContent는 HTML을 해석해?
A. 아니다. 텍스트 그대로 처리한다.

Q. 사용자 입력을 화면에 표시할 때 textContent가 좋은 이유는?
A. HTML로 파싱하지 않아 XSS 위험을 줄일 수 있기 때문이다.

---

## 4.2 innerHTML Rules

### [개념]

`innerHTML`은 DOM 요소 내부의 HTML 문자열을 읽거나 변경하는 property다.

HTML 문자열을 파싱해 DOM으로 반영한다.

예:

```javascript
container.innerHTML = "<p>Festival</p>";
```

---

### [핵심]

- innerHTML
- HTML parsing
- XSS risk
- user input caution
- DOM update
- unsafe insertion
- trusted template only

---

### [실무]

`innerHTML`은 신뢰 가능한 HTML template에만 제한적으로 사용한다.

비권장:

```javascript
container.innerHTML = userInput;
```

권장:

```javascript
const itemElement = document.createElement("li");
itemElement.textContent = userInput;

container.appendChild(itemElement);
```

주의:

- 사용자 입력을 innerHTML에 직접 넣지 않는다.
- API 응답 문자열도 신뢰하지 않는다.
- 악성 script 삽입으로 XSS가 발생할 수 있다.
- 단순 텍스트는 textContent 사용
- 복잡한 DOM은 createElement로 구성
- Review Agent는 innerHTML 사용 위치를 보안 관점에서 검토해야 한다.

---

### [FAQ]

Q. innerHTML은 뭐야?
A. DOM 요소 내부 HTML 문자열을 읽거나 변경하는 property다.

Q. innerHTML은 왜 위험해?
A. 사용자 입력이 HTML로 파싱되면 악성 script가 실행될 수 있어 XSS 위험이 있다.

Q. 사용자 입력을 표시할 때 innerHTML을 써도 돼?
A. 지양한다. textContent나 createElement를 사용하는 것이 안전하다.

Q. Review Agent는 innerHTML에서 무엇을 확인해야 해?
A. 사용자 입력이나 API 응답이 직접 삽입되는지 확인해야 한다.

---

## 4.3 classList Rules

### [개념]

`classList`는 DOM 요소의 CSS class를 추가, 제거, 토글, 확인할 수 있는 property다.

예:

```javascript
button.classList.add("active");
button.classList.remove("disabled");
button.classList.toggle("open");
```

---

### [핵심]

- classList
- add
- remove
- toggle
- contains
- CSS class
- UI state
- active
- hidden
- disabled
- DOM style control

---

### [실무]

`classList`는 UI 상태에 따라 class를 제어할 때 사용한다.

예:

```javascript
function setLoadingState(button, loading) {
  button.classList.toggle("loading", loading);
  button.disabled = loading;
}
```

활성 class 변경:

```javascript
function activateTab(tabElement) {
  tabElement.classList.add("active");
}
```

주의:

- 스타일 직접 변경보다 class 변경을 우선한다.
- `toggle(className, force)` 형태를 사용하면 명확하다.
- 존재하지 않는 요소에 접근하지 않는다.
- class 이름은 CSS와 일치해야 한다.
- React에서는 className을 상태 기반으로 계산하는 방식이 일반적이다.

---

### [FAQ]

Q. classList는 뭐야?
A. DOM 요소의 CSS class를 추가, 제거, 토글, 확인할 수 있는 property다.

Q. classList.toggle은 언제 써?
A. 상태에 따라 class를 켜고 끌 때 사용한다.

Q. classList.contains는 뭐야?
A. 특정 class가 요소에 있는지 boolean으로 확인하는 메서드다.

Q. 스타일을 직접 변경하는 것보다 classList가 좋은 이유는?
A. 스타일 책임을 CSS에 두고 JavaScript는 상태만 제어할 수 있기 때문이다.

---

## 4.4 setAttribute and removeAttribute Rules

### [개념]

`setAttribute`는 DOM 요소의 attribute를 설정하는 메서드다.

`removeAttribute`는 attribute를 제거하는 메서드다.

예:

```javascript
imageElement.setAttribute("alt", "Festival image");
buttonElement.removeAttribute("disabled");
```

---

### [핵심]

- setAttribute
- removeAttribute
- attribute
- alt
- title
- disabled
- aria
- data attribute
- accessibility
- DOM property caution

---

### [실무]

Attribute 제어는 이미지 설명, 접근성, data 속성, 상태 표현에 사용된다.

예:

```javascript
imageElement.setAttribute("src", imageUrl ?? "/default.png");
imageElement.setAttribute("alt", festivalTitle ?? "축제 이미지");
```

접근성 속성:

```javascript
buttonElement.setAttribute("aria-expanded", String(isOpen));
```

주의:

- boolean attribute는 property 제어가 더 명확할 수 있다.
- button disabled는 `button.disabled = true`가 직관적이다.
- alt, aria 속성은 접근성에 중요하다.
- 사용자 입력을 URL attribute에 넣을 때 검증 필요
- 민감정보를 data attribute에 넣지 않는다.

---

### [FAQ]

Q. setAttribute는 뭐야?
A. DOM 요소의 attribute를 설정하는 메서드다.

Q. removeAttribute는 뭐야?
A. DOM 요소의 attribute를 제거하는 메서드다.

Q. button disabled는 setAttribute로만 처리해?
A. 가능하지만 `button.disabled = true`처럼 property로 처리하는 것이 더 명확할 수 있다.

Q. alt 속성은 왜 중요해?
A. 이미지 접근성과 대체 텍스트 제공에 필요하다.

---

## 4.5 createElement and appendChild Rules

### [개념]

`createElement`는 새 DOM 요소를 생성하는 메서드다.

`appendChild`는 생성한 요소를 부모 요소의 자식으로 추가하는 메서드다.

예:

```javascript
const itemElement = document.createElement("li");
itemElement.textContent = "Festival";

listElement.appendChild(itemElement);
```

---

### [핵심]

- createElement
- appendChild
- remove
- DOM creation
- safe rendering
- list rendering
- textContent
- dynamic UI
- XSS prevention

---

### [실무]

동적 목록을 안전하게 생성할 때 사용한다.

예:

```javascript
function createFestivalItem(festival) {
  const itemElement = document.createElement("li");

  itemElement.textContent = festival.title ?? "제목 없음";

  return itemElement;
}

function renderFestivalList(festivals) {
  const listElement = document.querySelector(".festival-list");

  if (!listElement) {
    return;
  }

  listElement.textContent = "";

  festivals.forEach((festival) => {
    listElement.appendChild(createFestivalItem(festival));
  });
}
```

주의:

- 사용자 입력은 textContent로 삽입한다.
- 반복 DOM 조작이 많으면 성능을 고려한다.
- 기존 목록 초기화 여부를 명확히 한다.
- 요소 생성 함수와 렌더 함수 분리
- React에서는 map 기반 렌더링으로 전환된다.

---

### [FAQ]

Q. createElement는 뭐야?
A. 새 DOM 요소를 생성하는 메서드다.

Q. appendChild는 뭐야?
A. 부모 요소에 자식 요소를 추가하는 메서드다.

Q. createElement가 innerHTML보다 안전한 이유는?
A. 사용자 입력을 textContent로 넣으면 HTML 파싱을 피할 수 있기 때문이다.

Q. 동적 목록 렌더링은 어떻게 구성해?
A. 요소 생성 함수와 목록 렌더 함수를 분리하는 것이 좋다.

---

# 5. Event Handling

## 5.1 Event Handling Concept

### [개념]

Event Handling은 사용자의 클릭, 입력, 제출, 키보드 입력 같은 행동에 반응하는 JavaScript 로직이다.

Browser는 사용자 행동을 Event로 전달하고, JavaScript는 Event Listener를 통해 반응한다.

예:

```javascript
button.addEventListener("click", () => {
  console.log("clicked");
});
```

---

### [핵심]

- Event Handling
- Event
- Event Listener
- addEventListener
- click
- input
- change
- submit
- keydown
- event object
- event.target
- event.currentTarget
- preventDefault
- stopPropagation
- event bubbling
- event delegation

---

### [실무]

Frontend Event Handling Flow:

```text
User Action
→ Browser Event
→ Event Listener
→ Event Handler Function
→ Validation
→ JavaScript Logic
→ UI Update or API Request
```

Event Handler 작성 기준:

- 이름은 `handle` 접두사 사용
- Event 입력 처리
- Validation Function 분리
- API Request Function 분리
- DOM Update 최소화
- Error Handling 고려
- 중복 Event 등록 주의

예:

```javascript
function handleSearchClick() {
  console.log("search clicked");
}

button.addEventListener("click", handleSearchClick);
```

주의:

- Event Listener 중복 등록 주의
- 비동기 Event Handler는 try / catch 고려
- Event Handler에 모든 로직을 넣지 않는다.
- React에서는 Synthetic Event로 이어진다.
- Review Agent는 Event Handler 책임 과다를 검토해야 한다.

---

### [FAQ]

Q. Event Handling이 뭐야?
A. 클릭, 입력, 제출 같은 사용자 행동에 반응하는 JavaScript 로직이다.

Q. Event Listener는 뭐야?
A. 특정 Event가 발생했을 때 실행할 Function을 등록하는 방식이다.

Q. Event Handler 이름은 어떻게 지어?
A. 일반적으로 handleClick, handleSubmit, handleInputChange처럼 handle 접두사를 사용한다.

Q. Event Handler에 모든 로직을 넣어도 돼?
A. 지양한다. 입력 처리, 검증, API 요청, 데이터 가공을 적절히 분리하는 것이 좋다.

---

## 5.2 addEventListener Rules

### [개념]

`addEventListener`는 DOM 요소에 Event Listener를 등록하는 메서드다.

예:

```javascript
button.addEventListener("click", handleClick);
```

---

### [핵심]

- addEventListener
- event type
- event handler
- callback
- click event
- submit event
- input event
- removeEventListener
- duplicate listener caution

---

### [실무]

Event Listener는 요소 존재 확인 후 등록한다.

예:

```javascript
const searchButton = document.querySelector(".search-button");

if (searchButton) {
  searchButton.addEventListener("click", handleSearchClick);
}
```

Form Submit Event:

```javascript
const form = document.querySelector(".search-form");

if (form) {
  form.addEventListener("submit", handleSearchSubmit);
}
```

주의:

- 요소가 null이면 addEventListener 호출 시 오류 발생
- 같은 Listener를 여러 번 등록하면 중복 실행될 수 있음
- 필요 시 removeEventListener로 제거
- anonymous function은 제거하기 어려움
- 동적 요소에는 Event Delegation 고려

remove 예:

```javascript
button.removeEventListener("click", handleClick);
```

---

### [FAQ]

Q. addEventListener는 뭐야?
A. DOM 요소에 특정 Event가 발생했을 때 실행할 Function을 등록하는 메서드다.

Q. addEventListener 전에 무엇을 확인해야 해?
A. 선택한 DOM 요소가 null이 아닌지 확인해야 한다.

Q. Event Listener가 중복 등록되면 어떻게 돼?
A. 같은 Event에서 Handler가 여러 번 실행될 수 있다.

Q. removeEventListener를 쓰려면 무엇이 중요해?
A. 등록할 때 사용한 동일한 Function 참조가 필요하다.

---

# 6. Event Object

## 6.1 Event Object Rules

### [개념]

Event Object는 Event 발생 정보가 담긴 객체다.

Event Handler의 첫 번째 Parameter로 전달된다.

예:

```javascript
function handleClick(event) {
  console.log(event.type);
}
```

---

### [핵심]

- Event Object
- event
- event type
- event.target
- event.currentTarget
- preventDefault
- stopPropagation
- keyboard event
- mouse event
- form event

---

### [실무]

Event Object는 입력값 읽기, 기본 동작 방지, 이벤트 발생 요소 확인에 사용한다.

예:

```javascript
function handleInput(event) {
  const value = event.target.value;

  console.log(value);
}
```

Form Submit:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  const form = event.currentTarget;
  const keyword = form.keyword.value.trim();

  console.log(keyword);
}
```

주의:

- Event Object 이름은 보통 `event` 사용
- `event.target`과 `event.currentTarget` 구분
- Form submit에는 `preventDefault` 필요
- Event Object를 비동기 로직에서 사용할 때 필요한 값만 먼저 추출
- React Synthetic Event와 Browser Native Event 차이를 이후 문서에서 구분

---

### [FAQ]

Q. Event Object가 뭐야?
A. Event 발생 정보가 담긴 객체다.

Q. Event Object는 어디서 받아?
A. Event Handler의 첫 번째 Parameter로 전달된다.

Q. event.target은 뭐야?
A. Event가 실제 발생한 요소다.

Q. event.currentTarget은 뭐야?
A. Event Handler가 등록된 요소다.

---

## 6.2 event.target and event.currentTarget Rules

### [개념]

`event.target`은 Event가 실제 발생한 요소다.

`event.currentTarget`은 Event Handler가 등록된 요소다.

Event Bubbling 상황에서 두 값은 다를 수 있다.

예:

```javascript
function handleClick(event) {
  console.log(event.target);
  console.log(event.currentTarget);
}
```

---

### [핵심]

- event.target
- event.currentTarget
- actual event source
- listener element
- event bubbling
- event delegation
- form handling
- click handling

---

### [실무]

Event Delegation에서는 `event.target`을 사용해 실제 클릭된 요소를 확인한다.

Form Submit에서는 `event.currentTarget`을 사용하면 Handler가 등록된 form을 명확히 참조할 수 있다.

예:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  const form = event.currentTarget;
  const keyword = form.keyword.value.trim();

  search(keyword);
}
```

Event Delegation 예:

```javascript
function handleListClick(event) {
  const button = event.target.closest("[data-festival-id]");

  if (!button) {
    return;
  }

  const festivalId = Number(button.dataset.festivalId);
  selectFestival(festivalId);
}
```

주의:

- target은 자식 요소일 수 있다.
- currentTarget은 Listener가 붙은 요소다.
- target 사용 시 원하는 요소인지 검증해야 한다.
- closest 사용 시 null check 필요
- Form에서는 currentTarget이 더 안전한 경우가 많다.

---

### [FAQ]

Q. event.target과 event.currentTarget 차이는 뭐야?
A. target은 실제 Event가 발생한 요소이고, currentTarget은 Handler가 등록된 요소다.

Q. Event Delegation에서는 무엇을 많이 써?
A. 실제 클릭된 요소 확인이 필요하므로 event.target을 많이 사용한다.

Q. Form submit에서는 무엇이 더 안전해?
A. Handler가 등록된 form을 가리키는 event.currentTarget이 안전한 경우가 많다.

---

# 7. preventDefault and stopPropagation

## 7.1 preventDefault Rules

### [개념]

`preventDefault`는 Browser의 기본 동작을 막는 Event Object 메서드다.

Form Submit의 페이지 새로고침 방지에 자주 사용한다.

예:

```javascript
function handleSubmit(event) {
  event.preventDefault();
}
```

---

### [핵심]

- preventDefault
- default browser behavior
- form submit
- page reload prevention
- link click
- validation
- SPA behavior

---

### [실무]

Form Submit Event에서는 대부분 `preventDefault`를 사용한다.

예:

```javascript
function handleSearchSubmit(event) {
  event.preventDefault();

  const keyword = event.currentTarget.keyword.value.trim();

  if (!keyword) {
    return;
  }

  searchFestivals(keyword);
}
```

Link 기본 이동 방지:

```javascript
function handleLinkClick(event) {
  event.preventDefault();

  openModal();
}
```

주의:

- 필요한 경우에만 기본 동작을 막는다.
- Form submit 새로고침 방지에 필수적이다.
- 기본 동작을 막으면 대체 동작을 명확히 제공해야 한다.
- 접근성 측면에서 무분별한 기본 동작 차단은 피한다.
- Review Agent는 submit handler에서 preventDefault 누락을 검토해야 한다.

---

### [FAQ]

Q. preventDefault는 뭐야?
A. Browser의 기본 동작을 막는 Event Object 메서드다.

Q. Form submit에서 preventDefault를 왜 써?
A. 페이지 새로고침을 막고 JavaScript 로직으로 제출을 처리하기 위해 사용한다.

Q. preventDefault를 항상 써야 해?
A. 아니다. 기본 동작을 막아야 할 때만 사용한다.

---

## 7.2 stopPropagation Rules

### [개념]

`stopPropagation`은 Event가 부모 요소로 전파되는 것을 막는 메서드다.

Event Bubbling을 중단할 때 사용한다.

예:

```javascript
function handleButtonClick(event) {
  event.stopPropagation();
}
```

---

### [핵심]

- stopPropagation
- event bubbling
- propagation stop
- parent handler
- nested click
- modal
- dropdown
- caution

---

### [실무]

중첩된 클릭 영역에서 부모 Handler 실행을 막아야 할 때 사용한다.

예:

```javascript
function handleCardClick() {
  openDetail();
}

function handleFavoriteClick(event) {
  event.stopPropagation();

  toggleFavorite();
}
```

사용 상황:

- 카드 클릭 내부의 버튼 클릭
- Modal 내부 클릭 시 배경 닫기 방지
- Dropdown 내부 클릭 전파 방지

주의:

- 남용하면 Event 흐름 파악이 어려워진다.
- Event Delegation을 방해할 수 있다.
- 먼저 DOM 구조와 Handler 위치를 검토한다.
- 필요한 위치에만 제한적으로 사용한다.
- Review Agent는 stopPropagation 남용을 검토해야 한다.

---

### [FAQ]

Q. stopPropagation은 뭐야?
A. Event가 부모 요소로 전파되는 것을 막는 메서드다.

Q. stopPropagation은 언제 써?
A. 자식 요소 Event가 부모 Handler까지 실행되면 안 될 때 사용한다.

Q. stopPropagation을 많이 쓰면 왜 안 좋아?
A. Event 흐름이 숨겨져 디버깅이 어려워지고 Event Delegation을 방해할 수 있다.

---

# 8. Event Bubbling and Event Delegation

## 8.1 Event Bubbling Rules

### [개념]

Event Bubbling은 자식 요소에서 발생한 Event가 부모 요소 방향으로 전파되는 현상이다.

예:

```text
Button Click
→ Card
→ List
→ Document
```

---

### [핵심]

- Event Bubbling
- parent propagation
- child event
- click event
- event.target
- event.currentTarget
- stopPropagation
- Event Delegation

---

### [실무]

Event Bubbling은 중첩 UI에서 중요하다.

예:

```javascript
cardElement.addEventListener("click", handleCardClick);
favoriteButton.addEventListener("click", handleFavoriteClick);
```

버튼 클릭 시 카드 클릭 Handler도 실행될 수 있다.

해결:

```javascript
function handleFavoriteClick(event) {
  event.stopPropagation();

  toggleFavorite();
}
```

주의:

- Event Bubbling은 기본 Event 흐름이다.
- 의도하지 않은 부모 Handler 실행 가능
- target과 currentTarget 차이 확인
- stopPropagation은 필요한 경우에만 사용
- Event Delegation은 Bubbling을 활용한다.

---

### [FAQ]

Q. Event Bubbling이 뭐야?
A. 자식 요소에서 발생한 Event가 부모 요소 방향으로 전파되는 현상이다.

Q. 버튼 클릭했는데 카드 클릭도 실행되는 이유는?
A. Event Bubbling으로 자식 버튼 Event가 부모 카드까지 전파되기 때문이다.

Q. Event Bubbling을 막으려면 어떻게 해?
A. 필요한 경우 event.stopPropagation()을 사용한다.

---

## 8.2 Event Delegation Rules

### [개념]

Event Delegation은 여러 자식 요소 각각에 Event Listener를 등록하지 않고, 부모 요소 하나에 Listener를 등록해 Event를 처리하는 방식이다.

Event Bubbling을 활용한다.

예:

```javascript
listElement.addEventListener("click", handleListClick);
```

---

### [핵심]

- Event Delegation
- parent listener
- event bubbling
- dynamic element
- event.target
- closest
- data attribute
- list item
- performance

---

### [실무]

목록 항목이 동적으로 추가되는 경우 Event Delegation이 유용하다.

예:

```javascript
function handleFestivalListClick(event) {
  const button = event.target.closest("[data-festival-id]");

  if (!button) {
    return;
  }

  const festivalId = Number(button.dataset.festivalId);

  openFestivalDetail(festivalId);
}

listElement.addEventListener("click", handleFestivalListClick);
```

장점:

- Listener 개수 감소
- 동적으로 추가된 요소 처리 가능
- 목록 UI에 적합
- 성능과 관리성 개선

주의:

- event.target 검증 필요
- closest 결과 null check 필요
- data attribute 값은 string이므로 변환 필요
- stopPropagation과 충돌할 수 있음
- 복잡한 Delegation은 가독성을 떨어뜨릴 수 있음

---

### [FAQ]

Q. Event Delegation이 뭐야?
A. 부모 요소 하나에 Event Listener를 등록해 자식 요소 Event를 처리하는 방식이다.

Q. Event Delegation은 왜 써?
A. Listener 개수를 줄이고 동적으로 추가된 요소도 처리할 수 있기 때문이다.

Q. Event Delegation에서 event.target은 왜 중요해?
A. 실제 Event가 발생한 자식 요소를 확인해야 하기 때문이다.

Q. data attribute 값은 어떤 타입이야?
A. 문자열이다. 숫자로 필요하면 Number로 변환해야 한다.

---

# 9. Common Event Types

## 9.1 click Event Rules

### [개념]

`click` Event는 사용자가 요소를 클릭했을 때 발생한다.

버튼, 카드, 메뉴, 링크 동작 처리에 자주 사용된다.

예:

```javascript
button.addEventListener("click", handleClick);
```

---

### [핵심]

- click
- button
- link
- card
- menu
- modal
- toggle
- event handler
- user action

---

### [실무]

click Event는 사용자 액션의 대표 Event다.

예:

```javascript
function handleFavoriteClick(event) {
  event.stopPropagation();

  toggleFavorite();
}
```

주의:

- button type을 명확히 지정한다.
- Form 내부 button은 기본 submit 동작 가능
- 중첩 click Event는 Bubbling 고려
- 접근성 측면에서 keyboard 조작도 고려
- 비동기 click handler는 중복 클릭 방지 필요

중복 클릭 방지:

```javascript
function handleSubmitClick() {
  if (loading) {
    return;
  }

  submit();
}
```

---

### [FAQ]

Q. click Event는 언제 발생해?
A. 사용자가 요소를 클릭했을 때 발생한다.

Q. Form 내부 button click에서 주의할 점은?
A. button type이 submit이면 Form submit이 발생할 수 있다.

Q. 중복 클릭은 어떻게 방지해?
A. loading 상태를 확인하거나 버튼 disabled 처리를 적용한다.

---

## 9.2 input and change Event Rules

### [개념]

`input` Event는 입력값이 변경될 때마다 발생한다.

`change` Event는 값 변경이 확정되었을 때 발생한다.

예:

```javascript
inputElement.addEventListener("input", handleInput);
```

---

### [핵심]

- input event
- change event
- text input
- select
- checkbox
- radio
- event.target.value
- validation
- real time input

---

### [실무]

검색어 입력처럼 실시간 반응이 필요하면 `input` Event를 사용한다.

```javascript
function handleKeywordInput(event) {
  const keyword = event.target.value;

  updateKeyword(keyword);
}
```

Select 변경:

```javascript
function handleRegionChange(event) {
  const regionCode = event.target.value;

  updateRegion(regionCode);
}
```

주의:

- input value는 string이다.
- 숫자 입력도 문자열로 읽힐 수 있다.
- 실시간 API 요청은 debounce 고려
- checkbox는 `checked` 사용
- select는 value 확인
- validation과 UI 메시지를 분리한다.

Checkbox 예:

```javascript
function handleAgreeChange(event) {
  const checked = event.target.checked;

  updateAgreeStatus(checked);
}
```

---

### [FAQ]

Q. input Event는 언제 발생해?
A. 입력값이 변경될 때마다 발생한다.

Q. change Event는 언제 발생해?
A. 값 변경이 확정되었을 때 발생한다.

Q. input value는 숫자 입력이면 number야?
A. 아니다. 보통 string으로 읽히므로 필요하면 Number로 변환해야 한다.

Q. checkbox 값은 value로 읽어?
A. 체크 여부는 event.target.checked로 읽는다.

---

## 9.3 submit Event Rules

### [개념]

`submit` Event는 Form이 제출될 때 발생한다.

검색, 로그인, 회원가입, 리뷰 작성 같은 입력 제출 처리에 사용한다.

예:

```javascript
form.addEventListener("submit", handleSubmit);
```

---

### [핵심]

- submit event
- form
- preventDefault
- validation
- form data
- input value
- API request
- loading state
- error message

---

### [실무]

Form Submit은 기본 새로고침을 막고 JavaScript로 처리한다.

예:

```javascript
function handleSearchSubmit(event) {
  event.preventDefault();

  const form = event.currentTarget;
  const keyword = form.keyword.value.trim();

  if (!keyword) {
    showError("검색어를 입력하세요.");
    return;
  }

  searchFestivals(keyword);
}
```

Submit Flow:

```text
Submit Event
→ preventDefault
→ Read Form Value
→ Trim
→ Validate
→ Loading State
→ API Request
→ Success or Error UI
```

주의:

- `preventDefault` 누락 시 페이지 새로고침 가능
- 입력값 trim 처리
- Frontend Validation은 UX용
- Backend Validation도 필수
- 중복 제출 방지
- 에러 메시지 표시
- API 요청 실패 처리

---

### [FAQ]

Q. submit Event는 언제 발생해?
A. Form이 제출될 때 발생한다.

Q. submit Event에서 preventDefault를 왜 써?
A. 페이지 새로고침을 막고 JavaScript로 제출 처리를 하기 위해 사용한다.

Q. Form Validation은 Frontend만 하면 돼?
A. 아니다. Frontend 검증은 UX용이고 Backend 검증도 반드시 필요하다.

Q. 중복 제출은 어떻게 방지해?
A. loading 상태 확인과 submit button disabled 처리를 적용한다.

---

## 9.4 keydown Event Rules

### [개념]

`keydown` Event는 사용자가 키보드 키를 눌렀을 때 발생한다.

검색 Enter 처리, 단축키, 접근성 보완에 사용할 수 있다.

예:

```javascript
inputElement.addEventListener("keydown", handleKeyDown);
```

---

### [핵심]

- keydown
- keyboard event
- Enter
- Escape
- event.key
- shortcut
- accessibility
- form submit caution

---

### [실무]

Enter 키 검색:

```javascript
function handleKeywordKeyDown(event) {
  if (event.key !== "Enter") {
    return;
  }

  submitSearch();
}
```

Escape 키 Modal 닫기:

```javascript
function handleEscapeKey(event) {
  if (event.key === "Escape") {
    closeModal();
  }
}
```

주의:

- Form 내부 Enter는 submit을 발생시킬 수 있다.
- event.key 기준으로 판단한다.
- 단축키는 입력 중인 요소와 충돌하지 않게 한다.
- 접근성 요구사항을 고려한다.
- 전역 keydown Listener는 제거 시점 관리 필요

---

### [FAQ]

Q. keydown Event는 언제 발생해?
A. 사용자가 키보드 키를 눌렀을 때 발생한다.

Q. Enter 키는 어떻게 확인해?
A. `event.key === "Enter"`로 확인한다.

Q. Escape 키는 어디에 많이 써?
A. Modal, Dropdown, Popup 닫기 동작에 자주 사용한다.

---

# 10. Form Handling

## 10.1 Form Handling Concept

### [개념]

Form Handling은 사용자 입력값을 읽고, 검증하고, 제출하고, 오류를 표시하는 Frontend 로직이다.

로그인, 회원가입, 검색, 리뷰 작성, 필터 설정에서 자주 사용된다.

---

### [핵심]

- Form Handling
- input value
- submit event
- preventDefault
- validation
- trim
- required
- error message
- disabled button
- loading state
- FormData
- API request

---

### [실무]

Form Handling Flow:

```text
User Input
→ Read Value
→ Trim
→ Validate
→ Show Error or Submit
→ API Request
→ Success / Error UI
```

검색 Form 예:

```javascript
function handleSearchSubmit(event) {
  event.preventDefault();

  const form = event.currentTarget;
  const keyword = form.keyword.value.trim();

  if (!validateKeyword(keyword)) {
    showError("검색어를 입력하세요.");
    return;
  }

  searchFestivals(keyword);
}
```

주의:

- 입력값은 trim 처리
- required 조건 명확화
- Frontend Validation과 Backend Validation 분리
- 실패 메시지와 개발자 로그 구분
- submit 중복 방지
- loading / error 상태 관리
- 민감정보 console.log 금지

---

### [FAQ]

Q. Form Handling이 뭐야?
A. 사용자 입력값을 읽고 검증하고 제출하고 오류를 표시하는 Frontend 로직이다.

Q. Form Handling은 어디에 쓰여?
A. 로그인, 회원가입, 검색, 리뷰 작성, 필터 설정에 자주 사용된다.

Q. 입력값에 trim을 왜 써?
A. 앞뒤 공백만 입력된 값을 유효한 입력으로 처리하지 않기 위해 사용한다.

Q. Frontend Validation만 하면 충분해?
A. 아니다. Frontend 검증은 UX용이고 Backend 검증도 반드시 필요하다.

---

# 11. Input Value Handling

## 11.1 Text Input Rules

### [개념]

Text Input Handling은 사용자 입력 문자열을 읽고 정리하고 검증하는 과정이다.

Text Input 값은 보통 `event.target.value` 또는 form 요소에서 읽는다.

예:

```javascript
const keyword = event.target.value;
```

---

### [핵심]

- input value
- string value
- trim
- empty string
- validation
- event.target.value
- controlled input readiness
- search keyword

---

### [실무]

검색어 입력 처리:

```javascript
function normalizeKeyword(keyword) {
  return keyword.trim();
}

function validateKeyword(keyword) {
  return normalizeKeyword(keyword).length > 0;
}
```

Input Event:

```javascript
function handleKeywordInput(event) {
  const keyword = event.target.value;

  updateKeyword(keyword);
}
```

주의:

- input value는 string이다.
- 공백 입력은 trim 후 검증한다.
- 빈 문자열 처리 필요
- 너무 긴 입력 제한 고려
- API query로 보낼 때 encodeURIComponent 사용
- 민감정보 입력값 로그 출력 금지

---

### [FAQ]

Q. input value는 어떻게 읽어?
A. Event Handler에서 `event.target.value`로 읽을 수 있다.

Q. input value는 항상 string이야?
A. 일반적으로 string으로 읽힌다.

Q. 검색어 검증은 어떻게 해?
A. trim 후 길이가 0보다 큰지 확인한다.

Q. 입력값을 API query로 보낼 때 주의할 점은?
A. encodeURIComponent로 인코딩해야 한다.

---

## 11.2 Number Input Rules

### [개념]

Number Input은 숫자 입력 UI지만 JavaScript에서 읽은 value는 문자열일 수 있다.

숫자 계산이나 비교 전에 명시적 변환이 필요하다.

예:

```javascript
const page = Number(event.target.value);
```

---

### [핵심]

- number input
- string value
- Number conversion
- parseInt
- parseFloat
- NaN
- Number.isNaN
- validation
- min
- max

---

### [실무]

숫자 입력 검증:

```javascript
function normalizePage(value) {
  const page = Number(value);

  if (Number.isNaN(page) || page < 1) {
    return 1;
  }

  return page;
}
```

평점 처리:

```javascript
function normalizeRating(value) {
  const rating = Number(value);

  if (Number.isNaN(rating)) {
    return 0;
  }

  return Math.min(Math.max(rating, 0), 5);
}
```

주의:

- number input value도 string으로 읽힐 수 있다.
- 빈 문자열은 Number 변환 시 0이 될 수 있다.
- NaN 검증 필요
- min / max 범위 검증 필요
- 숫자 문자열과 number 비교 주의
- Backend 검증도 필요

---

### [FAQ]

Q. number input value는 number야?
A. 보통 string으로 읽히므로 Number로 명시적 변환해야 한다.

Q. 숫자 변환 실패는 어떻게 확인해?
A. Number.isNaN으로 확인할 수 있다.

Q. 빈 문자열을 Number로 바꾸면 어떻게 될 수 있어?
A. 0으로 변환될 수 있어 별도 검증이 필요하다.

Q. 숫자 입력 검증은 Frontend만 하면 돼?
A. 아니다. Backend에서도 범위와 타입 검증이 필요하다.

---

## 11.3 Checkbox and Radio Rules

### [개념]

Checkbox와 Radio는 선택 상태를 표현하는 Form 요소다.

체크 여부는 `checked` property로 확인한다.

예:

```javascript
const checked = event.target.checked;
```

---

### [핵심]

- checkbox
- radio
- checked
- boolean
- selected option
- agreement
- filter option
- form state
- input change

---

### [실무]

Checkbox 처리:

```javascript
function handleAgreeChange(event) {
  const agreed = event.target.checked;

  updateAgreement(agreed);
}
```

Radio 처리:

```javascript
function handleSortChange(event) {
  const sortType = event.target.value;

  updateSortType(sortType);
}
```

주의:

- checkbox checked는 boolean이다.
- radio value는 string이다.
- 여러 checkbox는 배열 상태로 관리할 수 있다.
- 필수 동의 항목은 submit 전 검증한다.
- label 연결로 접근성을 보완한다.

---

### [FAQ]

Q. checkbox 선택 여부는 어떻게 확인해?
A. `event.target.checked`로 확인한다.

Q. radio 선택 값은 어떻게 읽어?
A. 선택된 radio의 `event.target.value`로 읽는다.

Q. checkbox checked 값은 어떤 타입이야?
A. boolean이다.

Q. 여러 checkbox 선택은 어떻게 관리해?
A. 선택된 id나 value 목록을 배열로 관리할 수 있다.

---

## 11.4 Select Rules

### [개념]

Select는 여러 option 중 하나를 선택하는 Form 요소다.

선택 값은 `value` property로 읽는다.

예:

```javascript
const selectedRegion = event.target.value;
```

---

### [핵심]

- select
- option
- selected value
- change event
- filter
- region code
- category code
- default option
- string value

---

### [실무]

지역 필터 선택:

```javascript
function handleRegionChange(event) {
  const regionCode = event.target.value;

  updateRegionFilter(regionCode);
}
```

기본 option 처리:

```javascript
function normalizeRegionCode(value) {
  return value || null;
}
```

주의:

- select value는 string이다.
- 숫자 code가 필요하면 Number 변환
- 기본 선택값과 전체 선택값 구분
- option value와 label 구분
- Backend API parameter 이름과 일치 확인

---

### [FAQ]

Q. select 값은 어떻게 읽어?
A. `event.target.value`로 읽는다.

Q. select value는 어떤 타입이야?
A. 보통 string이다.

Q. 기본 option은 어떻게 처리해?
A. 빈 문자열을 null이나 기본 조건으로 변환할 수 있다.

---

# 12. Form Validation

## 12.1 Validation Rules

### [개념]

Validation은 입력값이 조건을 만족하는지 확인하는 과정이다.

Frontend Validation은 사용자 경험을 개선하지만 보안 검증을 대체하지 않는다.

예:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}
```

---

### [핵심]

- Validation
- required
- trim
- min length
- max length
- number range
- error message
- frontend validation
- backend validation
- user experience

---

### [실무]

검색어 검증:

```javascript
function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}
```

리뷰 입력 검증:

```javascript
function validateReview({ rating, content }) {
  if (rating < 1 || rating > 5) {
    return "평점은 1점 이상 5점 이하로 입력해야 합니다.";
  }

  if (content.trim().length === 0) {
    return "리뷰 내용을 입력하세요.";
  }

  return null;
}
```

Validation Flow:

```text
Read Input
→ Normalize
→ Validate
→ Return Error Message or null
→ Show Error
→ Submit
```

주의:

- Validation Function은 Pure Function으로 작성
- 오류 메시지는 사용자 친화적으로 작성
- Backend Validation 필수
- 민감정보는 로그 출력 금지
- Validation 규칙은 중복되지 않게 관리

---

### [FAQ]

Q. Validation이 뭐야?
A. 입력값이 조건을 만족하는지 확인하는 과정이다.

Q. Frontend Validation은 왜 필요해?
A. 사용자가 빠르게 오류를 확인하고 수정할 수 있게 하기 위해 필요하다.

Q. Frontend Validation만 하면 보안상 안전해?
A. 아니다. Backend Validation이 반드시 필요하다.

Q. Validation Function은 어떻게 작성하는 게 좋아?
A. 입력을 받아 오류 메시지나 null을 반환하는 Pure Function으로 작성하는 것이 좋다.

---

## 12.2 Error Message Rules

### [개념]

Error Message는 사용자가 입력 오류나 요청 실패 원인을 이해하고 수정할 수 있게 안내하는 문구다.

Frontend에서는 Validation Error와 API Error를 구분해야 한다.

---

### [핵심]

- error message
- validation error
- API error
- user friendly message
- field error
- global error
- empty state
- accessibility
- error display

---

### [실무]

Validation Error:

```javascript
function getKeywordError(keyword) {
  if (keyword.trim().length === 0) {
    return "검색어를 입력하세요.";
  }

  return null;
}
```

Error 표시:

```javascript
function showError(message) {
  const errorElement = document.querySelector(".error-message");

  if (!errorElement) {
    return;
  }

  errorElement.textContent = message ?? "";
}
```

주의:

- 사용자에게 내부 오류 stack trace를 보여주지 않는다.
- 개발자 로그와 사용자 메시지를 구분한다.
- Error Message는 구체적이고 짧게 작성한다.
- 오류 발생 필드 근처에 표시하는 것이 좋다.
- 접근성을 위해 aria 속성 고려 가능
- 민감정보를 Error Message에 포함하지 않는다.

---

### [FAQ]

Q. Error Message는 왜 필요해?
A. 사용자가 무엇을 수정해야 하는지 알 수 있게 하기 위해 필요하다.

Q. Validation Error와 API Error는 같아?
A. 아니다. 입력값 문제와 서버 요청 실패는 구분해서 처리해야 한다.

Q. 사용자에게 stack trace를 보여줘도 돼?
A. 안 된다. 사용자 친화적 메시지를 보여주고 상세 오류는 개발자 로그로 관리한다.

---

# 13. Disabled and Loading State

## 13.1 Disabled Button Rules

### [개념]

Disabled Button은 특정 조건에서 버튼을 비활성화해 잘못된 제출이나 중복 요청을 막는 UI 처리다.

예:

```javascript
submitButton.disabled = true;
```

---

### [핵심]

- disabled button
- canSubmit
- loading
- validation
- duplicate submit prevention
- UI state
- button state
- form UX

---

### [실무]

Submit 가능 여부 계산:

```javascript
function canSubmitForm({ keyword, loading }) {
  return keyword.trim().length > 0 && !loading;
}
```

Button 상태 반영:

```javascript
function updateSubmitButton(button, canSubmit) {
  button.disabled = !canSubmit;
}
```

주의:

- disabled 조건은 별도 변수나 함수로 분리
- loading 중에는 submit 버튼 비활성화
- 입력값이 유효하지 않으면 비활성화
- disabled만으로 Backend 요청 차단을 신뢰하지 않는다.
- 접근성과 안내 메시지 고려

---

### [FAQ]

Q. Disabled Button은 왜 필요해?
A. 유효하지 않은 제출이나 중복 요청을 막기 위해 필요하다.

Q. disabled 조건은 어디서 계산해?
A. 입력값 유효성, loading 상태, 권한 상태를 기준으로 별도 함수나 변수로 계산하는 것이 좋다.

Q. disabled 처리만 하면 보안상 충분해?
A. 아니다. 사용자가 우회할 수 있으므로 Backend 검증도 필요하다.

---

## 13.2 Loading State Rules

### [개념]

Loading State는 비동기 요청이 진행 중인지 나타내는 상태다.

사용자가 화면이 멈춘 것으로 오해하지 않도록 안내하고 중복 요청을 방지한다.

예:

```javascript
let loading = false;
```

---

### [핵심]

- loading state
- pending request
- async UI
- spinner
- disabled button
- duplicate request
- submit state
- API request

---

### [실무]

Submit 중 Loading 처리:

```javascript
async function handleSubmit(event) {
  event.preventDefault();

  if (loading) {
    return;
  }

  loading = true;
  updateLoadingUI(loading);

  try {
    await submitForm();
  } finally {
    loading = false;
    updateLoadingUI(loading);
  }
}
```

주의:

- 요청 시작 시 loading true
- 성공 / 실패와 관계없이 finally에서 loading false
- loading 중 중복 요청 방지
- 버튼 disabled와 연결
- 사용자에게 진행 중 상태 표시
- React 전환 시 useState로 관리

---

### [FAQ]

Q. Loading State는 왜 필요해?
A. 비동기 요청 중 사용자에게 진행 상태를 알리고 중복 요청을 막기 위해 필요하다.

Q. loading은 언제 true로 바꿔?
A. API 요청 시작 직전에 true로 바꾼다.

Q. loading은 언제 false로 바꿔?
A. 요청 성공 또는 실패 후 finally에서 false로 바꾸는 것이 안전하다.

Q. loading 중 버튼은 어떻게 처리해?
A. submit 버튼을 disabled 처리해 중복 요청을 막는다.

---

# 14. FormData

## 14.1 FormData Rules

### [개념]

`FormData`는 Form 입력값을 key-value 형태로 수집하는 Browser API다.

파일 업로드나 Form 전체 값을 수집할 때 사용할 수 있다.

예:

```javascript
const formData = new FormData(formElement);
```

---

### [핵심]

- FormData
- form values
- key-value
- multipart
- file upload
- get
- append
- entries
- submit data
- Browser API

---

### [실무]

Form 값 읽기:

```javascript
function getSearchFormValues(form) {
  const formData = new FormData(form);

  return {
    keyword: String(formData.get("keyword") ?? "").trim(),
    regionCode: String(formData.get("regionCode") ?? ""),
  };
}
```

파일 추가:

```javascript
formData.append("image", file);
```

주의:

- Form 요소에는 name attribute가 필요하다.
- FormData 값은 string 또는 File일 수 있다.
- JSON 전송과 multipart 전송을 구분한다.
- 파일 업로드 시 Content-Type을 직접 설정하지 않는 경우가 많다.
- 민감정보를 로그로 출력하지 않는다.
- FormData를 Object로 변환할 때 타입 처리 필요

---

### [FAQ]

Q. FormData는 뭐야?
A. Form 입력값을 key-value 형태로 수집하는 Browser API다.

Q. FormData는 언제 써?
A. Form 전체 값 수집이나 파일 업로드에 사용한다.

Q. FormData를 쓰려면 input에 무엇이 필요해?
A. name attribute가 필요하다.

Q. FormData 값은 어떤 타입이야?
A. string 또는 File일 수 있다.

---

# 15. DOM Event Form Practical Example

## 15.1 Search Form Example

### [개념]

DOM, Event, Form Handling은 하나의 사용자 흐름으로 연결된다.

검색 Form 예제는 입력값 읽기, 검증, submit 처리, loading 상태, 결과 렌더링을 연결한다.

---

### [핵심]

- DOM selection
- submit event
- preventDefault
- input value
- trim
- validation
- loading state
- API request
- render list
- error message
- safe DOM update

---

### [실무]

예:

```javascript
const form = document.querySelector(".search-form");
const listElement = document.querySelector(".festival-list");
const errorElement = document.querySelector(".error-message");
const submitButton = document.querySelector(".submit-button");

let loading = false;

function validateKeyword(keyword) {
  return keyword.trim().length > 0;
}

function setError(message) {
  if (!errorElement) {
    return;
  }

  errorElement.textContent = message ?? "";
}

function setLoading(nextLoading) {
  loading = nextLoading;

  if (submitButton) {
    submitButton.disabled = loading;
    submitButton.textContent = loading ? "검색 중..." : "검색";
  }
}

function renderFestivals(festivals) {
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

async function handleSearchSubmit(event) {
  event.preventDefault();

  if (loading) {
    return;
  }

  const formElement = event.currentTarget;
  const keyword = formElement.keyword.value.trim();

  if (!validateKeyword(keyword)) {
    setError("검색어를 입력하세요.");
    return;
  }

  setError("");
  setLoading(true);

  try {
    const response = await fetch(
      `/api/festivals/search?keyword=${encodeURIComponent(keyword)}`,
    );

    if (!response.ok) {
      throw new Error("Festival search failed");
    }

    const data = await response.json();
    const festivals = Array.isArray(data?.content) ? data.content : [];

    renderFestivals(festivals);
  } catch (error) {
    console.error(error);
    setError("검색 중 오류가 발생했습니다.");
  } finally {
    setLoading(false);
  }
}

if (form) {
  form.addEventListener("submit", handleSearchSubmit);
}
```

이 예제의 목적:

- DOM 요소 null 방어
- Form submit 기본 동작 방지
- 입력값 trim
- Validation Function 분리
- Loading State 처리
- Fetch API 요청
- response.ok 확인
- JSON 응답 처리
- Array.isArray 방어
- textContent 기반 안전 렌더링
- Error Message 표시
- finally에서 loading 해제

---

### [FAQ]

Q. Search Form 예제에서 preventDefault는 왜 필요해?
A. Form 제출 시 페이지 새로고침을 막고 JavaScript로 검색을 처리하기 위해 필요하다.

Q. renderFestivals에서 innerHTML 대신 createElement를 쓰는 이유는?
A. 사용자 입력이나 API 응답을 HTML로 파싱하지 않아 XSS 위험을 줄일 수 있기 때문이다.

Q. finally에서 loading을 false로 바꾸는 이유는?
A. 요청 성공과 실패 모두에서 loading 상태를 해제하기 위해서다.

Q. API 응답 목록을 Array.isArray로 확인하는 이유는?
A. 배열이 아닌 값에 forEach나 map을 호출해 발생하는 오류를 방지하기 위해서다.

---

# 16. DOM Event Form Common Mistakes

## 16.1 Common Mistakes

### [개념]

DOM, Event, Form Handling 실수는 화면 동작 오류, submit 새로고침, XSS 위험, 중복 요청, 사용자 입력 처리 오류로 이어질 수 있다.

Review Agent는 DOM null check, innerHTML 사용, Event Handler 책임, preventDefault, input validation, loading 처리를 우선 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- DOM 요소 null check 누락
- selector 오타
- DOM 로드 전 요소 선택
- innerHTML에 사용자 입력 삽입
- addEventListener 중복 등록
- anonymous function으로 removeEventListener 불가
- preventDefault 누락
- event.target / currentTarget 혼동
- stopPropagation 남용
- Event Delegation에서 target 검증 누락
- input value가 string인 점을 잊음
- trim 누락
- checkbox에서 value로 checked 판단
- number input 변환 누락
- Validation 없이 submit
- loading 없이 중복 요청 허용
- Error Message 미표시
- 민감정보 console.log 출력

---

### [실무]

Review Flow:

```text
DOM Event Form Review
→ DOM Selection Check
→ Null Check
→ innerHTML Security Check
→ Event Listener Check
→ preventDefault Check
→ target / currentTarget Check
→ Input Value Type Check
→ Validation Check
→ Loading State Check
→ Error Message Check
→ Sensitive Log Check
```

나쁜 예:

```javascript
document.querySelector(".result").innerHTML = userInput;

form.addEventListener("submit", () => {
  const age = form.age.value;

  submit(age);
});
```

개선 예:

```javascript
const resultElement = document.querySelector(".result");

if (resultElement) {
  resultElement.textContent = userInput;
}

function handleSubmit(event) {
  event.preventDefault();

  const age = Number(event.currentTarget.age.value);

  if (Number.isNaN(age)) {
    showError("나이를 숫자로 입력하세요.");
    return;
  }

  submit(age);
}

form.addEventListener("submit", handleSubmit);
```

주의:

- 사용자 입력은 textContent로 출력
- submit handler는 preventDefault 포함
- 숫자 입력은 Number 변환 후 검증
- Event Handler는 이름 있는 Function으로 분리
- Error Message는 사용자에게 표시
- 민감정보는 로그로 출력하지 않음

---

### [FAQ]

Q. DOM에서 가장 흔한 실수는 뭐야?
A. null check 없이 DOM property에 접근하거나 innerHTML에 사용자 입력을 넣는 것이다.

Q. Event Handling에서 가장 흔한 실수는 뭐야?
A. preventDefault 누락, Event Listener 중복 등록, target과 currentTarget 혼동이다.

Q. Form Handling에서 가장 흔한 실수는 뭐야?
A. trim 누락, 숫자 변환 누락, Validation 누락, loading 없이 중복 요청을 허용하는 것이다.

Q. Review Agent는 무엇을 우선 검토해야 해?
A. DOM null check, innerHTML 보안, preventDefault, 입력값 검증, loading 상태, 민감정보 로그를 우선 검토해야 한다.

---

# 17. DOM Event Form Checklist

## 17.1 Document Quality Checklist

### [개념]

DOM, Event, Form Handling 문서는 Frontend Agent가 Browser 기반 화면 동작과 사용자 입력 처리를 안전하게 구현하도록 지원해야 한다.

Checklist는 RAG Retrieval 품질과 Review Agent 검토 기준을 유지하기 위한 기준이다.

---

### [핵심]

검수 항목:

- [ ] DOM 개념이 포함되었는가?
- [ ] document와 window 설명이 포함되었는가?
- [ ] querySelector 설명과 null check가 포함되었는가?
- [ ] querySelectorAll과 NodeList 설명이 포함되었는가?
- [ ] getElementById 사용 기준이 포함되었는가?
- [ ] textContent 설명과 안전한 출력 기준이 포함되었는가?
- [ ] innerHTML 위험성과 XSS 주의가 포함되었는가?
- [ ] classList 사용 기준이 포함되었는가?
- [ ] setAttribute / removeAttribute 설명이 포함되었는가?
- [ ] createElement / appendChild 설명이 포함되었는가?
- [ ] Event Handling 개념이 포함되었는가?
- [ ] addEventListener 설명과 중복 등록 주의가 포함되었는가?
- [ ] Event Object 설명이 포함되었는가?
- [ ] event.target / event.currentTarget 차이가 포함되었는가?
- [ ] preventDefault 설명이 포함되었는가?
- [ ] stopPropagation 설명과 남용 주의가 포함되었는가?
- [ ] Event Bubbling 설명이 포함되었는가?
- [ ] Event Delegation 설명이 포함되었는가?
- [ ] click / input / change / submit / keydown Event가 포함되었는가?
- [ ] Form Handling Flow가 포함되었는가?
- [ ] Input Value Handling 기준이 포함되었는가?
- [ ] Form Validation 기준이 포함되었는가?
- [ ] Disabled / Loading State 기준이 포함되었는가?
- [ ] FormData 설명이 포함되었는가?
- [ ] 실무형 Search Form 예제가 포함되었는가?
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
→ DOM Selection Check
→ DOM Manipulation Security Check
→ Event Handling Flow Check
→ Form Validation Check
→ Loading State Check
→ Practical Example Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

파일 간 연계:

```text
JavaScript_Foundation_Part05_Array_Object
→ JavaScript_Foundation_Part06_DOM_Event_Form
→ JavaScript_Foundation_Part07_Async_Promise_AsyncAwait
```

---

### [FAQ]

Q. DOM Event Form 문서 검수에서 가장 중요한 것은 뭐야?
A. DOM null check, innerHTML 보안, Event Handler 분리, preventDefault, Form Validation, Loading State, Error Message 처리다.

Q. 이 문서는 React와 어떻게 연결돼?
A. React Event, Form State, Conditional UI, List Rendering, Synthetic Event 이해의 기반이 된다.

Q. 다음 Part와 어떻게 연결돼?
A. Part06은 사용자 입력과 화면 동작 기준을 만들고, Part07은 Async JavaScript, Promise, async / await로 비동기 흐름을 확장한다.

---

# Retrieval Queries

### [FAQ]

Q. DOM이 뭐야?
A. HTML 문서를 JavaScript가 읽고 조작할 수 있도록 만든 객체 구조다.

Q. DOM은 왜 필요해?
A. JavaScript가 화면 요소를 선택하고 변경하고 사용자 이벤트에 반응하기 위해 필요하다.

Q. React에서도 DOM을 직접 조작해?
A. 대부분 직접 조작하지 않는다. React에서는 state와 props 기반으로 UI를 갱신한다.

Q. document는 뭐야?
A. 현재 웹 페이지의 HTML 문서를 나타내는 Browser 객체다.

Q. window는 뭐야?
A. Browser 환경의 최상위 전역 객체다.

Q. querySelector는 뭐야?
A. CSS selector와 일치하는 첫 번째 DOM 요소를 반환하는 메서드다.

Q. querySelector 결과가 없으면 뭐가 나와?
A. null이 반환된다.

Q. querySelectorAll은 뭐야?
A. CSS selector와 일치하는 모든 DOM 요소를 NodeList로 반환하는 메서드다.

Q. NodeList는 Array야?
A. 아니다. 필요하면 Array.from으로 배열로 변환할 수 있다.

Q. getElementById는 뭐야?
A. 지정한 id와 일치하는 DOM 요소를 반환하는 메서드다.

Q. getElementById에 #을 붙여야 해?
A. 아니다. id 문자열만 전달한다.

Q. textContent는 뭐야?
A. DOM 요소의 텍스트 내용을 읽거나 변경하는 property다.

Q. textContent는 HTML을 해석해?
A. 아니다. 텍스트 그대로 처리한다.

Q. innerHTML은 뭐야?
A. DOM 요소 내부 HTML 문자열을 읽거나 변경하는 property다.

Q. innerHTML은 왜 위험해?
A. 사용자 입력이 HTML로 파싱되면 악성 script가 실행될 수 있어 XSS 위험이 있다.

Q. 사용자 입력을 표시할 때 innerHTML을 써도 돼?
A. 지양한다. textContent나 createElement를 사용하는 것이 안전하다.

Q. classList는 뭐야?
A. DOM 요소의 CSS class를 추가, 제거, 토글, 확인할 수 있는 property다.

Q. classList.toggle은 언제 써?
A. 상태에 따라 class를 켜고 끌 때 사용한다.

Q. setAttribute는 뭐야?
A. DOM 요소의 attribute를 설정하는 메서드다.

Q. createElement는 뭐야?
A. 새 DOM 요소를 생성하는 메서드다.

Q. appendChild는 뭐야?
A. 부모 요소에 자식 요소를 추가하는 메서드다.

Q. Event Handling이 뭐야?
A. 클릭, 입력, 제출 같은 사용자 행동에 반응하는 JavaScript 로직이다.

Q. Event Listener는 뭐야?
A. 특정 Event가 발생했을 때 실행할 Function을 등록하는 방식이다.

Q. addEventListener는 뭐야?
A. DOM 요소에 특정 Event가 발생했을 때 실행할 Function을 등록하는 메서드다.

Q. addEventListener 전에 무엇을 확인해야 해?
A. 선택한 DOM 요소가 null이 아닌지 확인해야 한다.

Q. Event Listener가 중복 등록되면 어떻게 돼?
A. 같은 Event에서 Handler가 여러 번 실행될 수 있다.

Q. Event Object가 뭐야?
A. Event 발생 정보가 담긴 객체다.

Q. event.target은 뭐야?
A. Event가 실제 발생한 요소다.

Q. event.currentTarget은 뭐야?
A. Event Handler가 등록된 요소다.

Q. event.target과 event.currentTarget 차이는 뭐야?
A. target은 실제 Event가 발생한 요소이고, currentTarget은 Handler가 등록된 요소다.

Q. preventDefault는 뭐야?
A. Browser의 기본 동작을 막는 Event Object 메서드다.

Q. Form submit에서 preventDefault를 왜 써?
A. 페이지 새로고침을 막고 JavaScript로 제출 처리를 하기 위해 사용한다.

Q. stopPropagation은 뭐야?
A. Event가 부모 요소로 전파되는 것을 막는 메서드다.

Q. Event Bubbling이 뭐야?
A. 자식 요소에서 발생한 Event가 부모 요소 방향으로 전파되는 현상이다.

Q. Event Delegation이 뭐야?
A. 부모 요소 하나에 Event Listener를 등록해 자식 요소 Event를 처리하는 방식이다.

Q. Event Delegation은 왜 써?
A. Listener 개수를 줄이고 동적으로 추가된 요소도 처리할 수 있기 때문이다.

Q. click Event는 언제 발생해?
A. 사용자가 요소를 클릭했을 때 발생한다.

Q. input Event는 언제 발생해?
A. 입력값이 변경될 때마다 발생한다.

Q. change Event는 언제 발생해?
A. 값 변경이 확정되었을 때 발생한다.

Q. submit Event는 언제 발생해?
A. Form이 제출될 때 발생한다.

Q. keydown Event는 언제 발생해?
A. 사용자가 키보드 키를 눌렀을 때 발생한다.

Q. Enter 키는 어떻게 확인해?
A. event.key === "Enter"로 확인한다.

Q. Form Handling이 뭐야?
A. 사용자 입력값을 읽고 검증하고 제출하고 오류를 표시하는 Frontend 로직이다.

Q. Form Handling은 어디에 쓰여?
A. 로그인, 회원가입, 검색, 리뷰 작성, 필터 설정에 자주 사용된다.

Q. input value는 어떻게 읽어?
A. Event Handler에서 event.target.value로 읽을 수 있다.

Q. input value는 항상 string이야?
A. 일반적으로 string으로 읽힌다.

Q. 입력값에 trim을 왜 써?
A. 앞뒤 공백만 입력된 값을 유효한 입력으로 처리하지 않기 위해 사용한다.

Q. number input value는 number야?
A. 보통 string으로 읽히므로 Number로 명시적 변환해야 한다.

Q. checkbox 선택 여부는 어떻게 확인해?
A. event.target.checked로 확인한다.

Q. select 값은 어떻게 읽어?
A. event.target.value로 읽는다.

Q. Validation이 뭐야?
A. 입력값이 조건을 만족하는지 확인하는 과정이다.

Q. Frontend Validation만 하면 보안상 안전해?
A. 아니다. Backend Validation이 반드시 필요하다.

Q. Error Message는 왜 필요해?
A. 사용자가 무엇을 수정해야 하는지 알 수 있게 하기 위해 필요하다.

Q. Disabled Button은 왜 필요해?
A. 유효하지 않은 제출이나 중복 요청을 막기 위해 필요하다.

Q. Loading State는 왜 필요해?
A. 비동기 요청 중 사용자에게 진행 상태를 알리고 중복 요청을 막기 위해 필요하다.

Q. loading은 언제 false로 바꿔?
A. 요청 성공 또는 실패 후 finally에서 false로 바꾸는 것이 안전하다.

Q. FormData는 뭐야?
A. Form 입력값을 key-value 형태로 수집하는 Browser API다.

Q. FormData는 언제 써?
A. Form 전체 값 수집이나 파일 업로드에 사용한다.

Q. DOM에서 가장 흔한 실수는 뭐야?
A. null check 없이 DOM property에 접근하거나 innerHTML에 사용자 입력을 넣는 것이다.

Q. Event Handling에서 가장 흔한 실수는 뭐야?
A. preventDefault 누락, Event Listener 중복 등록, target과 currentTarget 혼동이다.

Q. Form Handling에서 가장 흔한 실수는 뭐야?
A. trim 누락, 숫자 변환 누락, Validation 누락, loading 없이 중복 요청을 허용하는 것이다.

Q. Review Agent는 DOM Event Form에서 무엇을 우선 검토해야 해?
A. DOM null check, innerHTML 보안, preventDefault, 입력값 검증, loading 상태, 민감정보 로그를 우선 검토해야 한다.

Q. JavaScript Foundation Part06 다음에는 무엇을 다뤄야 해?
A. Async JavaScript, Promise, async / await를 다루는 Part07로 이어지는 것이 좋다.
