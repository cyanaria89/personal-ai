# SSR Thymeleaf Part02 - Template Syntax

---

# 1. Thymeleaf Template Syntax

## 1.1 Thymeleaf Standard Attributes

### [개념]

Thymeleaf Standard Attributes는 서버에서 HTML Template을 렌더링할 때 사용하는 `th:*` 속성이다.

`th:*` 속성은 Browser가 실행하는 속성이 아니라, 서버의 Thymeleaf Template Engine이 처리한 뒤 최종 HTML로 변환된다.

```text
HTML Template
+ th:* Attribute
+ Model Attribute
→ Thymeleaf Template Engine
→ Final HTML Response
```

---

### [핵심]

- Thymeleaf는 서버 Template Engine이다.
- `th:*` 속성은 서버 렌더링 시 처리된다.
- Browser는 처리 완료된 HTML만 받는다.
- `th:text`는 Text Rendering에 사용한다.
- `th:utext`는 Unescaped Text Rendering에 사용한다.
- `th:if`는 Conditional Rendering에 사용한다.
- `th:unless`는 Negative Conditional Rendering에 사용한다.
- `th:each`는 Iteration Rendering에 사용한다.
- `th:href`는 Link Rendering에 사용한다.
- `th:src`는 Resource URL Rendering에 사용한다.
- `th:classappend`는 조건부 CSS Class 추가에 사용한다.

---

### [실무]

기본 Template 구조:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
  <head>
    <title th:text="${pageTitle}">Default Title</title>
  </head>
  <body>
    <h1 th:text="${heading}">Default Heading</h1>
  </body>
</html>
```

권장 작성 흐름:

```text
Static Prototype HTML 작성
→ xmlns:th 선언
→ th:* 속성 추가
→ Model Attribute 이름 확인
→ 서버 렌더링 결과 검증
```

주의:

- `xmlns:th` 선언을 권장한다.
- `th:*` 속성은 서버 렌더링 과정에서 처리된다.
- Template은 정적 HTML로도 구조를 이해할 수 있게 작성하는 것이 좋다.
- Template에는 복잡한 Business Logic을 넣지 않는다.

---

### [FAQ]

Q. Thymeleaf `th:*` 속성은 어디서 실행되는가?

A.
서버에서 실행된다.
Browser는 Thymeleaf 처리 후 완성된 HTML을 받는다.

Q. Thymeleaf Template에 `xmlns:th`를 꼭 써야 하는가?

A.
권장한다.
IDE 자동완성, 정적 검수, Template 가독성에 도움이 된다.

Q. `th:*` 속성이 Browser에 그대로 보이는가?

A.
일반적으로 보이지 않는다.
서버 렌더링 과정에서 처리된다.

Q. Template에 Business Logic을 작성해도 되는가?

A.
권장하지 않는다.
Service에서 처리하고 Template은 Rendering에 집중한다.

---

# 2. Text Rendering

## 2.1 th:text

### [개념]

`th:text`는 Thymeleaf에서 HTML Element의 Text Content를 렌더링하는 Standard Attribute이다.

`th:text`는 HTML Escaping을 적용하여 XSS 위험을 줄인다.

```html
<span th:text="${user.name}">Default Name</span>
```

Rendering 결과:

```html
<span>kim</span>
```

---

### [핵심]

- `th:text`는 Element Body Text를 대체한다.
- `${...}` Variable Expression을 자주 사용한다.
- HTML Escaping이 적용된다.
- 사용자 입력값 출력에는 `th:text` 사용을 권장한다.
- 기본 HTML Text는 Static Prototype 용도로 남길 수 있다.
- `th:text`는 SSR 보안 기본 출력 방식이다.

---

### [실무]

Controller:

```java
@GetMapping("/profile")
public String profile(Model model) {
    model.addAttribute("username", "kim");
    return "users/profile";
}
```

Template:

```html
<p th:text="${username}">default username</p>
```

Final HTML:

```html
<p>kim</p>
```

사용자 입력값 출력:

```html
<p th:text="${comment.content}">comment</p>
```

권장:

```text
User Input
→ th:text 사용
→ HTML Escaping 적용
→ XSS 위험 감소
```

---

### [FAQ]

Q. `th:text`는 무엇인가?

A.
HTML 요소의 Text Content를 서버에서 대체하는 Thymeleaf 속성이다.

Q. 사용자 입력값 출력에는 `th:text`와 `th:utext` 중 무엇을 쓰는가?

A.
기본적으로 `th:text`를 사용한다.
Escaping이 적용되어 XSS 위험을 줄일 수 있다.

Q. `th:text`가 있으면 기존 태그 내부 텍스트는 어떻게 되는가?

A.
렌더링 시 `th:text` 결과로 대체된다.
기존 텍스트는 정적 Prototype 용도이다.

---

## 2.2 th:utext

### [개념]

`th:utext`는 Unescaped Text를 출력하는 Thymeleaf Attribute이다.

HTML 태그를 문자열이 아니라 실제 HTML Markup으로 렌더링한다.

```html
<div th:utext="${notice.content}">notice</div>
```

---

### [핵심]

- `th:utext`는 HTML Escaping을 하지 않는다.
- HTML 태그를 실제 Markup으로 출력한다.
- XSS 위험이 있다.
- 사용자 입력값에는 사용하지 않는 것이 원칙이다.
- 관리자 검수 완료 HTML, Sanitizing 완료 Content에만 제한적으로 사용한다.
- 코드 리뷰에서 `th:utext`는 보안 검수 대상이다.

---

### [실무]

위험한 예:

```html
<div th:utext="${userInput}">content</div>
```

권장 예:

```html
<div th:text="${userInput}">content</div>
```

제한적 허용 예:

```text
Admin이 작성한 공지 HTML
→ Server-side Sanitizing
→ th:utext 제한 사용
```

검수 기준:

```text
th:utext 발견
→ 데이터 출처 확인
→ 사용자 입력 여부 확인
→ Sanitizing 여부 확인
→ XSS 위험 판단
```

---

### [FAQ]

Q. `th:utext`는 무엇인가?

A.
Escaping 없이 HTML을 출력하는 Thymeleaf 속성이다.

Q. `th:utext`를 왜 조심해야 하는가?

A.
HTML과 Script가 그대로 렌더링될 수 있어 XSS 위험이 있다.

Q. `th:utext`는 언제 사용할 수 있는가?

A.
Sanitizing이 완료된 신뢰 가능한 HTML Content에 제한적으로 사용할 수 있다.

---

# 3. Conditional Rendering

## 3.1 th:if

### [개념]

`th:if`는 조건이 참일 때만 HTML Element를 렌더링하는 Thymeleaf Attribute이다.

```html
<p th:if="${user != null}" th:text="${user.name}">username</p>
```

---

### [핵심]

- `th:if` 조건이 `true`이면 Element가 출력된다.
- 조건이 `false`이면 Element 자체가 제거된다.
- 로그인 여부, 권한 여부, 데이터 존재 여부 처리에 자주 사용한다.
- Null Check에 자주 사용된다.
- 복잡한 조건식은 Template보다 Controller / Service에서 계산하는 것이 좋다.
- 권한 판단은 Template 조건만으로 끝내지 않는다.

---

### [실무]

로그인 사용자 표시:

```html
<div th:if="${loginUser != null}">
  <span th:text="${loginUser.name}">username</span>
</div>
```

데이터 존재 여부:

```html
<p th:if="${festival != null}" th:text="${festival.title}">festival title</p>
```

권장:

```text
복잡한 Business Rule
→ Service 또는 Controller에서 boolean 값 생성
→ Model에 전달
→ Template에서는 단순 조건 사용
```

Controller:

```java
model.addAttribute("canEdit", postPermissionService.canEdit(userId, postId));
```

Template:

```html
<a th:if="${canEdit}" th:href="@{/posts/{id}/edit(id=${post.id})}"> 수정 </a>
```

---

### [FAQ]

Q. `th:if`는 무엇인가?

A.
조건이 참일 때만 Element를 렌더링하는 Thymeleaf 속성이다.

Q. `th:if` 조건이 거짓이면 어떻게 되는가?

A.
해당 Element가 최종 HTML에서 제거된다.

Q. 복잡한 조건식을 Template에 작성해도 되는가?

A.
권장하지 않는다.
Controller나 Service에서 계산 후 boolean Attribute로 전달하는 것이 좋다.

Q. `th:if`로 버튼을 숨기면 권한 검증이 완료되는가?

A.
아니다.
실제 권한 검증은 서버 Security Layer와 Service에서 처리해야 한다.

---

## 3.2 th:unless

### [개념]

`th:unless`는 조건이 거짓일 때만 HTML Element를 렌더링하는 Thymeleaf Attribute이다.

`th:if`의 반대 역할이다.

```html
<p th:unless="${items.isEmpty()}">데이터가 있습니다.</p>
```

---

### [핵심]

- `th:unless`는 조건이 `false`일 때 렌더링한다.
- `th:if="${!condition}"`와 유사하다.
- Empty State, 비로그인 상태, 권한 없음 메시지에 사용할 수 있다.
- 부정 조건이 복잡하면 가독성이 떨어진다.
- 가독성이 떨어지면 `th:if`와 명확한 boolean Attribute를 사용한다.

---

### [실무]

비로그인 상태 표시:

```html
<a th:unless="${loginUser != null}" th:href="@{/login}"> 로그인 </a>
```

목록 없음 처리:

```html
<p th:if="${users.isEmpty()}">사용자가 없습니다.</p>

<table th:unless="${users.isEmpty()}">
  <tr th:each="user : ${users}">
    <td th:text="${user.name}">name</td>
  </tr>
</table>
```

권장:

```text
조건이 명확한 경우
→ th:unless 사용 가능

부정 조건이 중첩되는 경우
→ th:if + 명확한 boolean Attribute 권장
```

---

### [FAQ]

Q. `th:unless`는 무엇인가?

A.
조건이 거짓일 때만 Element를 렌더링하는 Thymeleaf 속성이다.

Q. `th:unless`와 `th:if` 차이는?

A.
`th:if`는 조건이 참일 때 렌더링하고, `th:unless`는 조건이 거짓일 때 렌더링한다.

Q. `th:unless`를 많이 써도 되는가?

A.
가능하지만 부정 조건이 복잡해지면 가독성이 떨어진다.
명확한 boolean Attribute 사용을 권장한다.

---

# 4. Iteration Rendering

## 4.1 th:each

### [개념]

`th:each`는 Collection 데이터를 반복 렌더링하는 Thymeleaf Attribute이다.

목록, 테이블, 카드 리스트, 옵션 목록을 출력할 때 사용한다.

```html
<tr th:each="user : ${users}">
  <td th:text="${user.name}">name</td>
</tr>
```

---

### [핵심]

- `th:each="item : ${items}"` 형태를 사용한다.
- List, Set, Array, Page Content에 사용할 수 있다.
- 반복 변수는 해당 Element 내부에서 접근 가능하다.
- 반복 상태 변수로 index, count, first, last 등을 사용할 수 있다.
- 목록 데이터 Attribute 이름은 복수형을 권장한다.
- 대량 목록은 서버에서 Pagination 처리 후 렌더링한다.

---

### [실무]

Controller:

```java
@GetMapping("/admin/users")
public String list(Model model) {
    model.addAttribute("users", userService.findAll());
    return "admin/users/list";
}
```

Template:

```html
<table>
  <tr th:each="user : ${users}">
    <td th:text="${user.id}">1</td>
    <td th:text="${user.email}">email</td>
    <td th:text="${user.name}">name</td>
  </tr>
</table>
```

Page Content 반복:

```html
<tr th:each="user : ${users.content}">
  <td th:text="${user.email}">email</td>
</tr>
```

카드 목록:

```html
<div th:each="festival : ${festivals}" class="card">
  <h3 th:text="${festival.title}">festival title</h3>
  <p th:text="${festival.regionName}">region</p>
</div>
```

---

### [FAQ]

Q. Thymeleaf에서 목록 반복은 어떻게 하는가?

A.
`th:each`를 사용한다.

Q. `th:each="user : ${users}"`에서 `user`는 무엇인가?

A.
반복 중 현재 요소를 가리키는 변수이다.

Q. `users`는 어디서 오는가?

A.
Controller에서 `model.addAttribute("users", users)`로 전달한 Model Attribute이다.

Q. Page 객체는 어떻게 반복하는가?

A.
보통 `${users.content}`를 `th:each`로 반복한다.

---

## 4.2 Iteration Status

### [개념]

Iteration Status는 `th:each` 반복 중 현재 위치와 상태를 제공하는 보조 변수이다.

```html
<tr th:each="user, stat : ${users}">
  <td th:text="${stat.count}">1</td>
  <td th:text="${user.name}">name</td>
</tr>
```

---

### [핵심]

- `stat.index`는 0부터 시작한다.
- `stat.count`는 1부터 시작한다.
- `stat.size`는 전체 반복 크기이다.
- `stat.first`는 첫 번째 요소 여부이다.
- `stat.last`는 마지막 요소 여부이다.
- `stat.even`, `stat.odd`는 짝수 / 홀수 상태이다.
- Table Row 번호, 구분자 처리, 조건부 Class 처리에 사용한다.

---

### [실무]

번호 출력:

```html
<tr th:each="user, stat : ${users}">
  <td th:text="${stat.count}">1</td>
  <td th:text="${user.name}">name</td>
</tr>
```

마지막 요소 구분자 제거:

```html
<span th:each="tag, stat : ${tags}">
  <span th:text="${tag.name}">tag</span>
  <span th:unless="${stat.last}">,</span>
</span>
```

조건부 Class:

```html
<tr
  th:each="user, stat : ${users}"
  th:classappend="${stat.odd} ? 'odd-row' : 'even-row'"
>
  <td th:text="${user.name}">name</td>
</tr>
```

---

### [FAQ]

Q. 반복 번호를 1부터 출력하려면 무엇을 쓰는가?

A.
`stat.count`를 사용한다.

Q. 반복 번호를 0부터 출력하려면 무엇을 쓰는가?

A.
`stat.index`를 사용한다.

Q. 마지막 요소인지 확인하려면 무엇을 쓰는가?

A.
`stat.last`를 사용한다.

---

# 5. Link Rendering

## 5.1 th:href And Link Expression

### [개념]

`th:href`는 Thymeleaf에서 동적 링크 URL을 생성하는 Attribute이다.

Link Expression은 `@{}` 문법을 사용한다.

```html
<a th:href="@{/admin/users}">Users</a>
```

---

### [핵심]

- `th:href`는 `href` 속성을 서버에서 대체한다.
- `@{}`는 Link Expression이다.
- Context Path를 자동 반영할 수 있다.
- Path Variable을 표현할 수 있다.
- Query Parameter를 표현할 수 있다.
- 문자열 직접 조합보다 `@{}` 사용을 권장한다.
- Pagination 검색 조건 유지에도 사용한다.

---

### [실무]

고정 URL:

```html
<a th:href="@{/admin/users}">사용자 목록</a>
```

Path Variable:

```html
<a th:href="@{/admin/users/{id}(id=${user.id})}"> 상세 </a>
```

Query Parameter:

```html
<a th:href="@{/admin/users(page=${pageNumber}, keyword=${keyword})}">
  검색 유지
</a>
```

Path Variable + Query Parameter:

```html
<a th:href="@{/admin/users/{id}(id=${user.id}, page=${pageNumber})}"> 상세 </a>
```

---

### [FAQ]

Q. Thymeleaf에서 링크는 어떻게 만든다?

A.
`th:href`와 `@{}` Link Expression을 사용한다.

Q. Path Variable은 어떻게 작성하는가?

A.
`@{/users/{id}(id=${user.id})}` 형태로 작성한다.

Q. Query Parameter는 어떻게 작성하는가?

A.
`@{/users(page=${page}, keyword=${keyword})}` 형태로 작성한다.

Q. 문자열로 URL을 직접 조합해도 되는가?

A.
권장하지 않는다.
`th:href`와 `@{}` 사용을 권장한다.

---

# 6. Resource Rendering

## 6.1 th:src

### [개념]

`th:src`는 Thymeleaf에서 이미지, JavaScript 같은 Resource URL을 동적으로 생성하는 Attribute이다.

```html
<img th:src="@{/images/logo.png}" alt="logo" />
```

---

### [핵심]

- `th:src`는 `src` 속성을 서버에서 대체한다.
- Static Resource 경로는 `@{}` Link Expression을 사용한다.
- Image, JavaScript, iframe 등에 사용할 수 있다.
- Context Path 문제를 줄일 수 있다.
- 직접 `/static/...` 경로를 쓰지 않는다.
- Spring Boot 기본 Static Resource URL에는 `/static`을 포함하지 않는다.

---

### [실무]

이미지:

```html
<img th:src="@{/images/logo.png}" alt="logo" />
```

JavaScript:

```html
<script th:src="@{/js/app.js}"></script>
```

Spring Boot Static Resource 기본 위치:

```text
src/main/resources/static/css
src/main/resources/static/js
src/main/resources/static/images
```

URL Mapping:

```text
static/images/logo.png
→ /images/logo.png

static/js/app.js
→ /js/app.js
```

---

### [FAQ]

Q. Thymeleaf에서 이미지 경로는 어떻게 작성하는가?

A.
`th:src="@{/images/logo.png}"`처럼 작성한다.

Q. Static Resource 경로에 `/static`을 포함하는가?

A.
보통 포함하지 않는다.
`static/images/logo.png`는 URL `/images/logo.png`로 접근한다.

Q. JavaScript 파일 경로는 어떻게 연결하는가?

A.
`<script th:src="@{/js/app.js}"></script>` 형태를 사용한다.

---

## 6.2 th:href For CSS

### [개념]

CSS 파일 연결에는 `th:href`와 Link Expression `@{}`를 사용한다.

```html
<link rel="stylesheet" th:href="@{/css/style.css}" />
```

---

### [핵심]

- CSS는 `link` 태그의 `href` 속성으로 연결한다.
- Thymeleaf에서는 `th:href`를 사용한다.
- Spring Boot 기본 Static Resource는 `/static` 하위 파일을 URL Root 기준으로 제공한다.
- URL에는 `/static`을 포함하지 않는다.
- Context Path를 고려해야 하면 `@{}` 사용이 안전하다.

---

### [실무]

CSS 파일 위치:

```text
src/main/resources/static/css/admin.css
```

Template:

```html
<link rel="stylesheet" th:href="@{/css/admin.css}" />
```

잘못된 예:

```html
<link rel="stylesheet" href="/static/css/admin.css" />
```

올바른 예:

```html
<link rel="stylesheet" th:href="@{/css/admin.css}" />
```

---

### [FAQ]

Q. Thymeleaf에서 CSS는 어떻게 연결하는가?

A.
`<link rel="stylesheet" th:href="@{/css/style.css}">` 형태로 연결한다.

Q. URL에 `/static`을 붙이면 안 되는가?

A.
Spring Boot 기본 설정에서는 붙이지 않는다.
`static/css/style.css`는 `/css/style.css`로 접근한다.

Q. CSS 경로 404가 발생하는 이유는?

A.
Static Resource 위치가 틀렸거나 URL에 `/static`을 잘못 포함했을 수 있다.

---

# 7. Class And Attribute Rendering

## 7.1 th:classappend

### [개념]

`th:classappend`는 기존 CSS Class를 유지하면서 조건에 따라 Class를 추가하는 Thymeleaf Attribute이다.

```html
<li class="nav-item" th:classappend="${active} ? 'active'">Menu</li>
```

---

### [핵심]

- 기존 `class` 값을 유지한다.
- 조건부 Class 추가에 적합하다.
- Menu Active, Validation Error, Row Highlight에 자주 사용한다.
- 전체 Class를 대체하려면 `th:class`를 사용할 수 있다.
- 조건식은 단순하게 유지하는 것이 좋다.
- Validation Error UI 표시와 자주 결합된다.

---

### [실무]

Menu Active:

```html
<a
  class="nav-link"
  th:classappend="${currentMenu == 'users'} ? 'active'"
  th:href="@{/admin/users}"
>
  Users
</a>
```

Validation Error Class:

```html
<input
  class="form-control"
  th:field="*{email}"
  th:classappend="${#fields.hasErrors('email')} ? 'is-invalid'"
/>
```

Table Row Highlight:

```html
<tr
  th:each="order : ${orders}"
  th:classappend="${order.cancelled} ? 'table-danger'"
>
  <td th:text="${order.id}">1</td>
</tr>
```

---

### [FAQ]

Q. `th:classappend`는 무엇인가?

A.
기존 CSS Class를 유지하면서 조건부 Class를 추가하는 Thymeleaf 속성이다.

Q. Validation Error 표시에는 무엇을 사용할 수 있는가?

A.
`th:classappend`와 `#fields.hasErrors()`를 함께 사용할 수 있다.

Q. Class 전체를 바꾸고 싶으면 무엇을 쓰는가?

A.
`th:class`를 사용할 수 있다.

---

## 7.2 th:attr

### [개념]

`th:attr`은 HTML Attribute를 동적으로 설정하는 Thymeleaf Attribute이다.

여러 Attribute를 한 번에 설정할 수 있다.

```html
<button th:attr="data-id=${user.id}, disabled=${user.locked}">Button</button>
```

---

### [핵심]

- HTML Attribute를 동적으로 설정한다.
- `data-*` 속성 설정에 사용할 수 있다.
- 여러 Attribute를 comma로 구분해 설정할 수 있다.
- 전용 Attribute가 있으면 `th:value`, `th:disabled`, `th:checked` 등을 우선 사용한다.
- 복잡한 Attribute 조합은 가독성을 떨어뜨릴 수 있다.

---

### [실무]

Data Attribute:

```html
<button
  type="button"
  th:attr="data-user-id=${user.id}, data-email=${user.email}"
>
  선택
</button>
```

전용 Attribute 권장:

```html
<input th:value="${user.email}" />
```

Boolean Attribute:

```html
<button th:disabled="${!canSubmit}">저장</button>
```

검수 기준:

```text
th:attr 사용
→ 전용 th:* Attribute 존재 여부 확인
→ data-* 목적 여부 확인
→ 복잡도 확인
```

---

### [FAQ]

Q. `th:attr`은 무엇인가?

A.
HTML Attribute를 동적으로 설정하는 Thymeleaf 속성이다.

Q. `value` 설정에도 `th:attr`을 써야 하는가?

A.
보통 `th:value`를 권장한다.

Q. `data-*` 속성은 어떻게 설정하는가?

A.
`th:attr="data-id=${item.id}"` 형태로 설정할 수 있다.

---

# 8. Value And Form Field Attributes

## 8.1 th:value

### [개념]

`th:value`는 HTML `value` Attribute를 동적으로 설정하는 Thymeleaf Attribute이다.

Form Input, Button Value, Option Value, Hidden Input 등에 사용할 수 있다.

```html
<input type="text" th:value="${user.email}" />
```

---

### [핵심]

- `th:value`는 `value` 속성을 대체한다.
- 단순 값 출력용 Input에 사용할 수 있다.
- Form Binding에서는 `th:field`를 우선 사용한다.
- Hidden Input에 자주 사용된다.
- Checkbox / Radio / Select에서는 `th:field` 기반 Binding을 우선 검토한다.

---

### [실무]

단순 Input 값 설정:

```html
<input type="text" th:value="${user.email}" />
```

Hidden Value:

```html
<input type="hidden" name="userId" th:value="${user.id}" />
```

Form Binding 권장:

```html
<form th:object="${userForm}">
  <input type="text" th:field="*{email}" />
</form>
```

선택 기준:

```text
Form Object Binding
→ th:field

단순 출력 / Hidden Value
→ th:value
```

---

### [FAQ]

Q. `th:value`는 무엇인가?

A.
HTML `value` 속성을 서버에서 동적으로 설정하는 Thymeleaf 속성이다.

Q. Form Binding에서는 `th:value`와 `th:field` 중 무엇을 쓰는가?

A.
`th:field`를 우선 사용한다.

Q. Hidden Input에는 무엇을 사용할 수 있는가?

A.
`th:value`를 사용할 수 있다.

---

# 9. Thymeleaf Expressions

## 9.1 Expression Overview

### [개념]

Thymeleaf Expression은 Template에서 Model, Field, Message, Link, Fragment 등에 접근하기 위한 문법이다.

대표 Expression:

```text
${user.name}      → Variable Expression
*{email}          → Selection Expression
#{label.email}    → Message Expression
@{/users}         → Link Expression
~{layout/header}  → Fragment Expression
```

---

### [핵심]

- `${}`는 Model Attribute 접근에 사용한다.
- `*{}`는 Selection Object 내부 Field 접근에 사용한다.
- `#{}`는 Message Resource 접근에 사용한다.
- `@{}`는 URL 생성에 사용한다.
- `~{}`는 Fragment 참조에 사용한다.
- Expression 종류를 혼용하지 않는다.
- Form Binding에서는 `th:object` + `*{}` 조합을 자주 사용한다.

---

### [실무]

Variable Expression:

```html
<span th:text="${user.name}">name</span>
```

Selection Expression:

```html
<form th:object="${userForm}">
  <input th:field="*{email}" />
</form>
```

Message Expression:

```html
<label th:text="#{label.email}">Email</label>
```

Link Expression:

```html
<a th:href="@{/users}">Users</a>
```

Fragment Expression:

```html
<header th:replace="~{fragments/header :: header}"></header>
```

---

### [FAQ]

Q. `${}`는 무엇인가?

A.
Model Attribute에 접근하는 Variable Expression이다.

Q. `*{}`는 무엇인가?

A.
`th:object`로 지정된 Selection Object 내부 Field에 접근하는 Expression이다.

Q. `#{}`는 무엇인가?

A.
Message Resource에 접근하는 Message Expression이다.

Q. `@{}`는 무엇인가?

A.
URL을 생성하는 Link Expression이다.

Q. `~{}`는 무엇인가?

A.
Fragment를 참조하는 Fragment Expression이다.

---

## 9.2 Variable Expression

### [개념]

Variable Expression `${...}`는 Model Attribute에 접근하는 Thymeleaf Expression이다.

```html
<span th:text="${user.name}">name</span>
```

---

### [핵심]

- `${user}`는 Model Attribute `user`에 접근한다.
- `${user.name}`은 `user` 객체의 `name` Property에 접근한다.
- List, DTO, Page, Map에도 접근할 수 있다.
- Null 가능성이 있으면 조건 렌더링을 함께 고려한다.
- Model Attribute 이름과 Template 변수명이 일치해야 한다.

---

### [실무]

Controller:

```java
model.addAttribute("user", userResponse);
```

Template:

```html
<p th:text="${user.email}">email</p>
```

Map 접근:

```html
<span th:text="${stats['totalCount']}">0</span>
```

Null Check:

```html
<p th:if="${user != null}" th:text="${user.name}">name</p>
```

검수 기준:

```text
Template Expression 이름
→ Model Attribute 이름과 일치 여부 확인
```

---

### [FAQ]

Q. `${user.name}`에서 `user`는 어디서 오는가?

A.
Controller에서 Model에 담은 Attribute 이름이다.

Q. `${}`로 Service를 직접 호출해도 되는가?

A.
권장하지 않는다.
Controller에서 필요한 데이터를 준비해 Model에 전달하는 것이 좋다.

Q. `${user.name}`이 출력되지 않는 이유는?

A.
Model에 `user`가 없거나 Property 이름이 다를 수 있다.

---

## 9.3 Selection Expression

### [개념]

Selection Expression `*{...}`는 `th:object`로 지정된 객체 내부 Field에 접근하는 Thymeleaf Expression이다.

Form Binding에서 자주 사용한다.

```html
<form th:object="${userForm}">
  <input th:field="*{email}" />
</form>
```

---

### [핵심]

- `*{}`는 Selection Object 기준으로 Field에 접근한다.
- `th:object`가 있어야 의미가 명확하다.
- Form Binding에서 `th:field`와 함께 사용한다.
- `*{email}`은 `${userForm.email}`과 유사하게 동작한다.
- Form Validation Error 표시와 함께 사용된다.
- `th:object` 없이 `*{}` 사용은 오류 가능성이 높다.

---

### [실무]

Controller:

```java
@GetMapping("/users/new")
public String createForm(Model model) {
    model.addAttribute("userForm", new UserForm());
    return "users/create-form";
}
```

Template:

```html
<form th:action="@{/users}" th:object="${userForm}" method="post">
  <input th:field="*{email}" />
  <input th:field="*{name}" />
</form>
```

권장:

```text
Form 입력 화면
→ Model에 Form Object 추가
→ th:object 지정
→ th:field + *{} 사용
```

---

### [FAQ]

Q. `*{email}`은 무엇인가?

A.
`th:object`로 지정된 객체의 `email` Field에 접근하는 Selection Expression이다.

Q. `*{}`는 언제 주로 사용하는가?

A.
Form Binding에서 주로 사용한다.

Q. `th:object` 없이 `*{}`를 써도 되는가?

A.
권장하지 않는다.
Selection Object가 명확하지 않아 Form Binding 오류가 발생하기 쉽다.

---

# 10. Utility Objects

## 10.1 #strings

### [개념]

`#strings`는 Thymeleaf에서 문자열 처리를 지원하는 Utility Object이다.

문자열 포함 여부, 비어 있는지 확인, 기본값 처리 등에 사용할 수 있다.

```html
<span th:text="${#strings.defaultString(user.nickname, 'No Nickname')}">
  nickname
</span>
```

---

### [핵심]

- `#strings`는 문자열 관련 Utility Object이다.
- `isEmpty`, `contains`, `startsWith`, `defaultString` 등을 사용할 수 있다.
- 단순 표시용 문자열 처리에 적합하다.
- 복잡한 문자열 가공은 Controller / Service에서 처리한다.
- Template Logic 과다를 피해야 한다.

---

### [실무]

Default String:

```html
<span th:text="${#strings.defaultString(user.nickname, '미설정')}">
  미설정
</span>
```

Contains:

```html
<span th:if="${#strings.contains(user.email, '@')}"> Valid Email Format </span>
```

권장:

```text
단순 표시용 문자열 처리
→ #strings 사용 가능

Business Rule 포함 문자열 처리
→ Service에서 처리 후 Model 전달
```

---

### [FAQ]

Q. `#strings`는 무엇인가?

A.
Thymeleaf 문자열 처리 Utility Object이다.

Q. 복잡한 문자열 가공을 Template에서 해도 되는가?

A.
권장하지 않는다.
Service나 Controller에서 처리 후 Model로 전달하는 것이 좋다.

Q. 빈 문자열 기본값 표시는 어떻게 하는가?

A.
`#strings.defaultString(value, defaultValue)`를 사용할 수 있다.

---

## 10.2 #temporals

### [개념]

`#temporals`는 Java Time API 객체를 Thymeleaf에서 포맷팅하기 위한 Utility Object이다.

`LocalDate`, `LocalDateTime`, `ZonedDateTime` 같은 날짜 / 시간 출력에 사용한다.

```html
<span th:text="${#temporals.format(user.createdAt, 'yyyy-MM-dd HH:mm')}">
  date
</span>
```

---

### [핵심]

- `#temporals`는 Java Time API용 Date / Time Utility이다.
- `LocalDate`, `LocalDateTime` 포맷팅에 사용한다.
- `#dates`는 legacy `java.util.Date` 계열에 사용한다.
- Spring Boot 3.x / Java 21 기준 `#temporals` 사용을 권장한다.
- 복잡한 시간대 변환은 Service에서 처리하는 것이 좋다.

---

### [실무]

LocalDateTime 출력:

```html
<span th:text="${#temporals.format(order.createdAt, 'yyyy-MM-dd HH:mm')}">
  2026-01-01 10:00
</span>
```

LocalDate 출력:

```html
<span th:text="${#temporals.format(festival.startDate, 'yyyy-MM-dd')}">
  2026-01-01
</span>
```

권장:

```text
Java 21 + Spring Boot 3.x
→ LocalDate / LocalDateTime 사용
→ Template 출력 시 #temporals.format 사용
```

---

### [FAQ]

Q. LocalDateTime은 Thymeleaf에서 어떻게 포맷팅하는가?

A.
`#temporals.format(localDateTime, 'yyyy-MM-dd HH:mm')`을 사용한다.

Q. `#dates`와 `#temporals` 차이는?

A.
`#dates`는 legacy Date 계열, `#temporals`는 Java Time API 계열에 사용한다.

Q. 시간대 변환을 Template에서 처리해도 되는가?

A.
복잡한 시간대 변환은 Service에서 처리하는 것이 좋다.

---

## 10.3 #lists

### [개념]

`#lists`는 Thymeleaf에서 List 관련 처리를 지원하는 Utility Object이다.

목록 비어 있음 확인, 포함 여부 확인, 크기 확인 등에 사용할 수 있다.

```html
<p th:if="${#lists.isEmpty(users)}">사용자가 없습니다.</p>
```

---

### [핵심]

- `#lists`는 List 처리 Utility Object이다.
- Empty State 처리에 자주 사용한다.
- `isEmpty`, `contains`, `size` 등을 사용할 수 있다.
- Collection 상태 표시에 적합하다.
- 복잡한 필터링은 Service에서 처리한다.

---

### [실무]

목록 없음:

```html
<p th:if="${#lists.isEmpty(users)}">데이터가 없습니다.</p>
```

목록 있음:

```html
<table th:unless="${#lists.isEmpty(users)}">
  <tr th:each="user : ${users}">
    <td th:text="${user.name}">name</td>
  </tr>
</table>
```

Size 출력:

```html
<span th:text="${#lists.size(users)}">0</span>
```

---

### [FAQ]

Q. List가 비어 있는지 Thymeleaf에서 어떻게 확인하는가?

A.
`#lists.isEmpty(list)`를 사용할 수 있다.

Q. List 크기는 어떻게 출력하는가?

A.
`#lists.size(list)`를 사용할 수 있다.

Q. List 필터링을 Template에서 처리해도 되는가?

A.
권장하지 않는다.
Service에서 필터링 후 Model로 전달하는 것이 좋다.

---

# 11. Common Template Mistakes

## 11.1 Syntax Mistakes

### [개념]

Thymeleaf Syntax Mistake는 Expression 종류, Model Attribute 이름, HTML Attribute 사용 방식이 맞지 않아 발생하는 Template 오류이다.

---

### [핵심]

자주 발생하는 실수:

- `xmlns:th` 누락
- `${}`와 `*{}` 혼용
- `th:object` 없이 `*{}` 사용
- Model Attribute 이름 불일치
- `th:href` 없이 문자열 URL 직접 조합
- Static Resource URL에 `/static` 포함
- `th:utext` 남용
- `th:each` 반복 변수 이름 충돌
- 복잡한 Business Logic을 Template에 작성
- Null Check 없이 Nested Property 접근
- Page 객체 반복 시 `${users}`와 `${users.content}` 혼동

---

### [실무]

잘못된 예:

```html
<form>
  <input th:field="*{email}" />
</form>
```

문제:

```text
th:object 없음
→ Selection Object 불명확
→ Binding 오류 가능
```

올바른 예:

```html
<form th:object="${userForm}">
  <input th:field="*{email}" />
</form>
```

잘못된 예:

```html
<link rel="stylesheet" href="/static/css/admin.css" />
```

올바른 예:

```html
<link rel="stylesheet" th:href="@{/css/admin.css}" />
```

---

### [FAQ]

Q. `*{email}`에서 오류가 나는 이유는?

A.
`th:object`가 없거나 Form Object가 Model에 없을 가능성이 높다.

Q. CSS 파일이 404가 나는 이유는?

A.
URL에 `/static`을 포함했거나 Static Resource 위치가 잘못되었을 수 있다.

Q. Template에서 Business Logic을 많이 작성해도 되는가?

A.
권장하지 않는다.
Business Logic은 Service에서 처리하고 Template은 Rendering에 집중해야 한다.

Q. Page 객체 반복에서 오류가 나는 이유는?

A.
`Page` 자체가 아니라 보통 `${page.content}`를 반복해야 하기 때문이다.

---

# 12. Review Checklist

## 12.1 Template Syntax Review Checklist

### [개념]

Template Syntax Review Checklist는 Thymeleaf Template 문법을 Agent가 검수하기 위한 기준이다.

---

### [핵심]

기본 검수:

- `xmlns:th` 선언 여부
- `th:text` 사용 적절성
- `th:utext` 사용 위험성 확인
- `th:if`, `th:unless` 조건 단순성 확인
- `th:each` 반복 변수 명확성 확인
- `th:href`, `th:src` Link Expression 사용 여부
- Static Resource URL에 `/static` 포함 여부 확인
- Template Business Logic 과다 여부 확인

Expression 검수:

- `${}` Variable Expression 사용 위치 확인
- `*{}` Selection Expression 사용 시 `th:object` 존재 확인
- `#{}` Message Expression 사용 여부 확인
- `@{}` Link Expression 사용 여부 확인
- `~{}` Fragment Expression 사용 여부 확인
- Model Attribute 이름과 Expression 이름 일치 여부 확인

보안 검수:

- 사용자 입력값에 `th:text` 사용 여부
- `th:utext` 데이터 출처 확인
- XSS 위험 확인
- 직접 HTML 삽입 여부 확인
- View Hiding과 Server Authorization 혼동 여부 확인

---

### [실무]

검수 Flow:

```text
Template File 확인
→ xmlns:th 확인
→ Model Attribute 이름 확인
→ Expression 종류 확인
→ Link / Resource 경로 확인
→ th:utext 사용 여부 확인
→ 반복 대상 확인
→ Rendering 결과 예상
```

---

### [FAQ]

Q. Thymeleaf Template 검수에서 가장 먼저 확인할 것은?

A.
`xmlns:th` 선언과 Model Attribute 이름 일치 여부이다.

Q. 보안 관점에서 가장 위험한 Thymeleaf 속성은?

A.
`th:utext`이다.
Escaping 없이 HTML을 출력하기 때문이다.

Q. Static Resource 검수 핵심은?

A.
`/static`을 URL에 포함하지 않고 `@{/css/...}`, `@{/js/...}` 형태를 사용하는지 확인한다.

Q. Expression 검수 핵심은?

A.
`${}`, `*{}`, `#{}`, `@{}`, `~{}`를 목적에 맞게 사용했는지 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Thymeleaf Standard Attributes란?
A. 서버 렌더링 시 HTML을 동적으로 생성하기 위해 사용하는 `th:*` 속성이다.

Q. Thymeleaf `th:*` 속성은 어디서 처리되는가?
A. 서버의 Thymeleaf Template Engine에서 처리된다.

Q. `xmlns:th`는 왜 사용하는가?
A. Thymeleaf namespace 선언으로 IDE 자동완성, 정적 검수, Template 가독성에 도움이 된다.

Q. `th:text`는 무엇인가?
A. HTML Element의 Text Content를 Escaping 적용 후 렌더링하는 Thymeleaf 속성이다.

Q. 사용자 입력값 출력에는 어떤 Thymeleaf 속성을 쓰는가?
A. 기본적으로 `th:text`를 사용한다.

Q. `th:utext`는 무엇인가?
A. Escaping 없이 HTML을 출력하는 Thymeleaf 속성이다.

Q. `th:utext`가 위험한 이유는?
A. 사용자 입력값이 HTML 또는 Script로 렌더링되어 XSS가 발생할 수 있기 때문이다.

Q. Thymeleaf 조건 렌더링은 어떻게 하는가?
A. `th:if` 또는 `th:unless`를 사용한다.

Q. `th:if` 조건이 거짓이면 어떻게 되는가?
A. 해당 Element가 최종 HTML에서 제거된다.

Q. `th:unless`는 무엇인가?
A. 조건이 거짓일 때만 Element를 렌더링하는 Thymeleaf 속성이다.

Q. `th:if`로 버튼을 숨기면 권한 검증이 완료되는가?
A. 아니다. 실제 권한 검증은 서버 Security Layer와 Service에서 처리해야 한다.

Q. Thymeleaf 반복 렌더링은 어떻게 하는가?
A. `th:each`를 사용한다.

Q. `th:each="user : ${users}"`는 무슨 뜻인가?
A. Model Attribute `users`를 반복하면서 현재 요소를 `user`로 사용한다는 뜻이다.

Q. Page 객체는 Thymeleaf에서 어떻게 반복하는가?
A. 보통 `${page.content}`를 `th:each`로 반복한다.

Q. Thymeleaf 반복 번호는 어떻게 출력하는가?
A. Iteration Status의 `stat.count` 또는 `stat.index`를 사용한다.

Q. Thymeleaf에서 링크는 어떻게 생성하는가?
A. `th:href`와 `@{}` Link Expression을 사용한다.

Q. Thymeleaf Path Variable 링크는 어떻게 작성하는가?
A. `@{/users/{id}(id=${user.id})}` 형태로 작성한다.

Q. Thymeleaf Query Parameter 링크는 어떻게 작성하는가?
A. `@{/users(page=${page}, keyword=${keyword})}` 형태로 작성한다.

Q. Thymeleaf에서 이미지 경로는 어떻게 작성하는가?
A. `th:src="@{/images/logo.png}"` 형태로 작성한다.

Q. Thymeleaf에서 CSS 경로는 어떻게 작성하는가?
A. `th:href="@{/css/style.css}"` 형태로 작성한다.

Q. Spring Boot Static Resource URL에 `/static`을 포함하는가?
A. 보통 포함하지 않는다. `static/css/style.css`는 `/css/style.css`로 접근한다.

Q. `th:classappend`는 무엇인가?
A. 기존 CSS Class를 유지하면서 조건부 Class를 추가하는 Thymeleaf 속성이다.

Q. `th:attr`은 무엇인가?
A. HTML Attribute를 동적으로 설정하는 Thymeleaf 속성이다.

Q. `th:value`는 무엇인가?
A. HTML `value` 속성을 동적으로 설정하는 Thymeleaf 속성이다.

Q. Form Binding에서는 `th:value`와 `th:field` 중 무엇을 우선 사용하는가?
A. Form Object Binding에서는 `th:field`를 우선 사용한다.

Q. Thymeleaf `${}`는 무엇인가?
A. Model Attribute에 접근하는 Variable Expression이다.

Q. Thymeleaf `*{}`는 무엇인가?
A. `th:object`로 지정된 Selection Object 내부 Field에 접근하는 Selection Expression이다.

Q. Thymeleaf `#{}`는 무엇인가?
A. Message Resource에 접근하는 Message Expression이다.

Q. Thymeleaf `@{}`는 무엇인가?
A. URL을 생성하는 Link Expression이다.

Q. Thymeleaf `~{}`는 무엇인가?
A. Fragment를 참조하는 Fragment Expression이다.

Q. LocalDateTime은 Thymeleaf에서 어떻게 출력하는가?
A. `#temporals.format(localDateTime, 'yyyy-MM-dd HH:mm')`을 사용한다.

Q. List가 비어 있는지 Thymeleaf에서 어떻게 확인하는가?
A. `#lists.isEmpty(list)`를 사용한다.

Q. 문자열 기본값은 Thymeleaf에서 어떻게 처리하는가?
A. `#strings.defaultString(value, defaultValue)`를 사용할 수 있다.

Q. `*{email}` 오류 원인은?
A. `th:object`가 없거나 Form Object가 Model에 없을 가능성이 높다.

Q. CSS 파일 404 원인은?
A. URL에 `/static`을 포함했거나 Static Resource 위치가 잘못되었을 수 있다.

Q. Template에 Business Logic을 넣어도 되는가?
A. 권장하지 않는다. Service에서 처리 후 Model로 전달하는 것이 좋다.

Q. Thymeleaf Template 검수 핵심은?
A. Model Attribute 이름 일치, Expression 종류 적절성, `th:utext` 사용 위험성, Static Resource 경로를 확인하는 것이다.
