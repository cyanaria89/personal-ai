# SSR Thymeleaf Part05 - Layout Fragment Static Error

---

# 1. Layout Core

## 1.1 Layout Definition

### [개념]

Layout은 여러 Thymeleaf Template에서 공통으로 사용하는 화면 구조이다.

Header, Footer, Navigation, Sidebar, Script 영역을 Layout 또는 Fragment로 분리하여 중복을 줄인다.

```text
Page Template
→ Common Header
→ Common Navigation
→ Page Content
→ Common Footer
→ Common Scripts
```

---

### [핵심]

- Layout은 공통 화면 구조를 재사용한다.
- Fragment는 Template 일부를 재사용 가능한 조각으로 분리한 것이다.
- Header, Footer, Sidebar, Pagination, Alert, Modal을 Fragment로 분리할 수 있다.
- `th:fragment`로 Fragment를 선언한다.
- `th:replace` 또는 `th:insert`로 Fragment를 포함한다.
- 중복 HTML을 줄이고 유지보수성을 높인다.
- Admin Page / Backoffice에서 Layout 구조가 중요하다.
- 공통 Layout에는 Flash Message, Navigation, Security Menu 영역을 포함할 수 있다.

---

### [실무]

2026 실무 기준 Thymeleaf Layout은 다음 화면에서 자주 사용된다.

- Admin Dashboard
- Backoffice Management Page
- Internal Tool
- Form-heavy CRUD Page
- Error Page
- Login Page
- Legacy SSR Page

권장 구조:

```text
templates/
├ layouts/
│  └ main.html
├ fragments/
│  ├ header.html
│  ├ footer.html
│  ├ sidebar.html
│  ├ pagination.html
│  ├ alert.html
│  └ security.html
├ admin/
│  ├ users/
│  │  ├ list.html
│  │  ├ detail.html
│  │  ├ create-form.html
│  │  └ update-form.html
└ error/
   ├ 403.html
   ├ 404.html
   └ 500.html
```

---

### [FAQ]

Q. Thymeleaf Layout이란?

A.
여러 화면에서 공통으로 사용하는 Header, Footer, Sidebar 같은 구조를 재사용하는 방식이다.

Q. Fragment는 무엇인가?

A.
Template 일부를 재사용 가능한 조각으로 분리한 것이다.

Q. Layout과 Fragment를 사용하는 이유는?

A.
중복 HTML을 줄이고 공통 UI 변경을 쉽게 하기 위해 사용한다.

Q. Admin Page에서 공통화할 영역은?

A.
Header, Sidebar, Footer, Flash Message, Pagination, Security Menu를 공통화할 수 있다.

---

# 2. Fragment Core

## 2.1 th:fragment

### [개념]

`th:fragment`는 Thymeleaf Template에서 재사용 가능한 HTML 조각을 정의하는 Attribute이다.

```html
<header th:fragment="header">
  <h1>Admin</h1>
</header>
```

---

### [핵심]

- `th:fragment`는 Fragment 이름을 선언한다.
- Fragment는 다른 Template에서 참조할 수 있다.
- Header, Footer, Sidebar, Pagination에 자주 사용한다.
- Fragment 이름은 명확하게 작성한다.
- Fragment 파일은 `templates/fragments` 하위에 두는 것을 권장한다.
- Fragment는 독립적으로 이해 가능해야 한다.
- Fragment 내부에 복잡한 Business Logic을 넣지 않는다.

---

### [실무]

Fragment 파일:

```html
<!-- templates/fragments/header.html -->
<header th:fragment="header">
  <nav>
    <a th:href="@{/admin}">Dashboard</a>
    <a th:href="@{/admin/users}">Users</a>
    <a th:href="@{/admin/festivals}">Festivals</a>
  </nav>
</header>
```

참조 방식:

```html
<header th:replace="~{fragments/header :: header}"></header>
```

Fragment Naming 권장:

```text
header
footer
sidebar
pagination
alert
csrf
adminMenu
searchForm
```

---

### [FAQ]

Q. `th:fragment`는 무엇인가?

A.
재사용 가능한 HTML 조각을 정의하는 Thymeleaf Attribute이다.

Q. Fragment 파일은 어디에 두는가?

A.
보통 `templates/fragments` 하위에 둔다.

Q. Fragment 이름은 어떻게 정하는가?

A.
`header`, `footer`, `pagination`처럼 역할이 명확하게 드러나게 정한다.

Q. Fragment 내부에 Service 호출 로직을 넣어도 되는가?

A.
권장하지 않는다. 필요한 데이터는 Controller 또는 공통 Model 처리에서 준비한다.

---

## 2.2 Fragment Expression

### [개념]

Fragment Expression `~{...}`는 Thymeleaf Fragment를 참조하는 Expression이다.

```html
<div th:replace="~{fragments/header :: header}"></div>
```

구조:

```text
~{templatePath :: fragmentName}
```

---

### [핵심]

- Fragment Expression은 `~{}`를 사용한다.
- `fragments/header`는 Template Path이다.
- `header`는 Fragment Name이다.
- Template Path는 `templates` 하위 경로 기준이다.
- `.html` 확장자는 보통 작성하지 않는다.
- Fragment Name과 실제 `th:fragment` 이름이 일치해야 한다.
- Path 앞에 불필요한 `/`를 붙이지 않는다.

---

### [실무]

Header Fragment 참조:

```html
<div th:replace="~{fragments/header :: header}"></div>
```

Footer Fragment 참조:

```html
<div th:replace="~{fragments/footer :: footer}"></div>
```

Sidebar Fragment 참조:

```html
<aside th:replace="~{fragments/sidebar :: sidebar}"></aside>
```

잘못된 예:

```html
<div th:replace="~{/fragments/header.html :: header}"></div>
```

올바른 예:

```html
<div th:replace="~{fragments/header :: header}"></div>
```

---

### [FAQ]

Q. Fragment Expression은 무엇인가?

A.
`~{templatePath :: fragmentName}` 형식으로 Fragment를 참조하는 Thymeleaf Expression이다.

Q. Fragment 참조에 `.html`을 붙이는가?

A.
보통 붙이지 않는다.

Q. Fragment Not Found가 발생하는 이유는?

A.
Template Path 또는 Fragment Name이 실제 파일과 일치하지 않을 가능성이 높다.

Q. Fragment Expression 앞에 `/`를 붙이는가?

A.
일반적으로 붙이지 않는다. `~{fragments/header :: header}` 형태를 권장한다.

---

# 3. th:replace And th:insert

## 3.1 th:replace

### [개념]

`th:replace`는 현재 Element를 Fragment로 완전히 교체하는 Thymeleaf Attribute이다.

```html
<div th:replace="~{fragments/header :: header}"></div>
```

Rendering 결과는 `div`가 사라지고 Fragment의 Root Element로 대체된다.

---

### [핵심]

- `th:replace`는 현재 태그 자체를 Fragment로 교체한다.
- 공통 Header / Footer / Sidebar 포함에 자주 사용한다.
- 불필요한 wrapper 태그를 남기지 않는다.
- Layout 구조를 깔끔하게 유지할 수 있다.
- `th:insert`와 동작이 다르다.
- 공통 영역 대체 목적이면 `th:replace`를 우선 검토한다.

---

### [실무]

Header 포함:

```html
<body>
  <header th:replace="~{fragments/header :: header}"></header>

  <main>
    <h1>사용자 목록</h1>
  </main>

  <footer th:replace="~{fragments/footer :: footer}"></footer>
</body>
```

Fragment:

```html
<header th:fragment="header">
  <nav>
    <a th:href="@{/admin}">Admin</a>
  </nav>
</header>
```

권장 사용:

```text
공통 Header 교체
→ th:replace

공통 Footer 교체
→ th:replace

Sidebar 교체
→ th:replace

CSRF Hidden Input 조각 교체
→ th:replace 가능
```

---

### [FAQ]

Q. `th:replace`는 무엇인가?

A.
현재 Element를 Fragment의 Root Element로 완전히 교체하는 Thymeleaf Attribute이다.

Q. `th:replace`를 쓰면 원래 태그는 남는가?

A.
남지 않는다. Fragment로 교체된다.

Q. Header와 Footer 포함에는 무엇을 많이 사용하는가?

A.
일반적으로 `th:replace`를 많이 사용한다.

---

## 3.2 th:insert

### [개념]

`th:insert`는 현재 Element 내부에 Fragment를 삽입하는 Thymeleaf Attribute이다.

```html
<div th:insert="~{fragments/alert :: alert}"></div>
```

현재 Element는 유지되고 Fragment가 내부에 들어간다.

---

### [핵심]

- `th:insert`는 현재 태그를 유지한다.
- Fragment를 현재 Element 내부에 삽입한다.
- Wrapper 태그가 필요한 경우 사용할 수 있다.
- `th:replace`보다 HTML Depth가 늘어날 수 있다.
- 구조 의도를 명확히 해야 한다.
- Wrapper CSS Class가 중요할 때 사용할 수 있다.

---

### [실무]

Alert Wrapper 유지:

```html
<section class="message-area" th:insert="~{fragments/alert :: alert}"></section>
```

Fragment:

```html
<div th:fragment="alert">
  <p th:if="${message}" th:text="${message}">message</p>
</div>
```

선택 기준:

```text
현재 Element 자체를 교체
→ th:replace

현재 Element 내부에 삽입
→ th:insert

Wrapper CSS Class 유지 필요
→ th:insert 가능
```

---

### [FAQ]

Q. `th:insert`는 무엇인가?

A.
현재 Element 내부에 Fragment를 삽입하는 Thymeleaf Attribute이다.

Q. `th:replace`와 `th:insert` 차이는?

A.
`th:replace`는 현재 Element를 교체하고, `th:insert`는 현재 Element 내부에 Fragment를 넣는다.

Q. Wrapper 태그를 유지하려면 무엇을 쓰는가?

A.
`th:insert`를 사용할 수 있다.

---

# 4. Fragment Parameters

## 4.1 Parameterized Fragment

### [개념]

Parameterized Fragment는 Fragment에 값을 전달하여 재사용성을 높이는 방식이다.

`th:fragment="name(param1, param2)"` 형식으로 Parameter를 선언한다.

```html
<div th:fragment="alert(type, message)">
  <div th:class="'alert alert-' + ${type}" th:text="${message}">message</div>
</div>
```

---

### [핵심]

- Fragment는 Parameter를 받을 수 있다.
- 반복되는 UI Component를 재사용할 때 유용하다.
- Alert, Badge, Pagination, Modal에 사용할 수 있다.
- Parameter 이름은 Fragment 내부 변수로 사용된다.
- 너무 복잡한 Fragment Parameter는 가독성을 떨어뜨린다.
- Parameter 개수와 호출 인자 개수는 일치해야 한다.

---

### [실무]

Alert Fragment:

```html
<!-- templates/fragments/alert.html -->
<div th:fragment="alert(type, message)">
  <div
    th:if="${message}"
    th:class="'alert alert-' + ${type}"
    th:text="${message}"
  >
    message
  </div>
</div>
```

사용:

```html
<div th:replace="~{fragments/alert :: alert('success', ${message})}"></div>
```

Badge Fragment:

```html
<span
  th:fragment="badge(label, type)"
  th:class="'badge badge-' + ${type}"
  th:text="${label}"
>
  badge
</span>
```

사용:

```html
<span th:replace="~{fragments/badge :: badge(${user.role}, 'primary')}"></span>
```

---

### [FAQ]

Q. Fragment에 Parameter를 전달할 수 있는가?

A.
가능하다. `th:fragment="name(param)"` 형식으로 선언한다.

Q. Parameterized Fragment는 언제 사용하는가?

A.
Alert, Badge, Pagination처럼 같은 UI 구조에 값만 달라지는 경우 사용한다.

Q. Fragment Parameter를 많이 늘려도 되는가?

A.
권장하지 않는다. Parameter가 많으면 별도 Template 구조 또는 단순 Page Template 분리를 검토한다.

Q. Fragment Parameter 오류가 나는 이유는?

A.
선언한 Parameter 개수와 호출 시 전달한 인자 개수가 맞지 않을 수 있다.

---

# 5. Layout Patterns

## 5.1 Common Layout Pattern

### [개념]

Common Layout Pattern은 각 Page Template에서 공통 Header, Sidebar, Footer를 포함하는 기본 구조이다.

```text
Page Template
→ Header Fragment
→ Sidebar Fragment
→ Main Content
→ Footer Fragment
```

---

### [핵심]

- 각 Page Template에서 공통 Fragment를 포함한다.
- 구조가 단순하고 이해하기 쉽다.
- Admin Page에 적합하다.
- Layout Dialect 없이도 구현 가능하다.
- 페이지마다 공통 Include가 반복될 수 있다.
- 대규모 화면에서는 Layout Dialect 또는 Decorator Pattern을 검토할 수 있다.

---

### [실무]

Page Template:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
  <head>
    <title>Admin Users</title>
    <link rel="stylesheet" th:href="@{/css/admin.css}" />
  </head>
  <body>
    <header th:replace="~{fragments/header :: header}"></header>

    <div class="layout">
      <aside th:replace="~{fragments/sidebar :: sidebar}"></aside>

      <main>
        <h1>사용자 목록</h1>
      </main>
    </div>

    <footer th:replace="~{fragments/footer :: footer}"></footer>
    <script th:src="@{/js/admin.js}"></script>
  </body>
</html>
```

권장:

```text
소규모 Admin Page
→ Common Fragment Include

대규모 다중 Layout Page
→ Layout Dialect 또는 Layout Template 검토
```

---

### [FAQ]

Q. Common Layout Pattern은 무엇인가?

A.
각 Page Template에서 Header, Sidebar, Footer Fragment를 포함하는 구조이다.

Q. Layout Dialect 없이도 Layout을 만들 수 있는가?

A.
가능하다. `th:replace`와 Fragment만으로 기본 Layout을 만들 수 있다.

Q. Admin Page에는 어떤 Layout 구조가 적합한가?

A.
Header + Sidebar + Main Content + Footer 구조가 자주 사용된다.

---

## 5.2 Admin Layout Pattern

### [개념]

Admin Layout Pattern은 Backoffice 화면에서 공통 Navigation, Sidebar, Content Area, Pagination, Alert를 재사용하는 구조이다.

```text
Admin Page
→ Admin Header
→ Admin Sidebar
→ Flash Message
→ Page Title
→ Search Form
→ Table
→ Pagination
→ Footer
```

---

### [핵심]

- Admin Layout은 CRUD 중심이다.
- List / Detail / Create / Update 화면 구조를 통일한다.
- Search Form과 Pagination을 재사용한다.
- 권한 기반 Menu 표시가 필요할 수 있다.
- Flash Message 영역을 공통화한다.
- Error Message 표시 영역을 일관되게 유지한다.
- CSRF Fragment를 공통화할 수 있다.

---

### [실무]

Admin List Page 구조:

```html
<body>
  <header th:replace="~{fragments/admin-header :: adminHeader}"></header>
  <aside th:replace="~{fragments/admin-sidebar :: adminSidebar}"></aside>

  <main class="admin-content">
    <div th:replace="~{fragments/alert :: alert('success', ${message})}"></div>

    <h1>사용자 관리</h1>

    <form th:action="@{/admin/users}" th:object="${searchForm}" method="get">
      <input th:field="*{keyword}" placeholder="검색어" />
      <button type="submit">검색</button>
    </form>

    <table>
      <tr th:each="user : ${users.content}">
        <td th:text="${user.email}">email</td>
        <td th:text="${user.name}">name</td>
      </tr>
    </table>

    <nav
      th:replace="~{fragments/pagination :: pagination(${users}, '/admin/users')}"
    ></nav>
  </main>
</body>
```

---

### [FAQ]

Q. Admin Layout에서 공통화할 요소는?

A.
Header, Sidebar, Alert, Search Form, Pagination, Footer를 공통화할 수 있다.

Q. Admin Page는 어떤 화면 구조가 많은가?

A.
List, Detail, Create Form, Update Form, Delete Action 구조가 많다.

Q. Flash Message 영역은 어디에 두는가?

A.
공통 Layout의 Content 상단에 두는 것을 권장한다.

---

# 6. Static Resource Core

## 6.1 Static Resource Path

### [개념]

Static Resource는 CSS, JavaScript, Image 같은 정적 파일이다.

Spring Boot 기본 설정에서는 `src/main/resources/static` 하위 파일이 URL Root 기준으로 제공된다.

```text
src/main/resources/static/css/admin.css
→ /css/admin.css

src/main/resources/static/js/admin.js
→ /js/admin.js

src/main/resources/static/images/logo.png
→ /images/logo.png
```

---

### [핵심]

- Static Resource는 `static` 디렉터리 하위에 둔다.
- URL에는 `/static`을 포함하지 않는다.
- Thymeleaf에서는 `@{}` Link Expression 사용을 권장한다.
- CSS는 `th:href`로 연결한다.
- JavaScript와 Image는 `th:src`로 연결한다.
- Context Path 문제를 줄이기 위해 직접 문자열보다 `@{}`를 사용한다.
- Static Resource 404는 파일 위치와 URL Mapping을 함께 확인한다.

---

### [실무]

CSS 연결:

```html
<link rel="stylesheet" th:href="@{/css/admin.css}" />
```

JavaScript 연결:

```html
<script th:src="@{/js/admin.js}"></script>
```

Image 연결:

```html
<img th:src="@{/images/logo.png}" alt="logo" />
```

잘못된 예:

```html
<link rel="stylesheet" href="/static/css/admin.css" />
<script src="/static/js/admin.js"></script>
<img src="/static/images/logo.png" alt="logo" />
```

올바른 예:

```html
<link rel="stylesheet" th:href="@{/css/admin.css}" />
<script th:src="@{/js/admin.js}"></script>
<img th:src="@{/images/logo.png}" alt="logo" />
```

---

### [FAQ]

Q. Spring Boot Static Resource는 어디에 두는가?

A.
`src/main/resources/static` 하위에 둔다.

Q. URL에 `/static`을 포함하는가?

A.
보통 포함하지 않는다. `static/css/admin.css`는 `/css/admin.css`로 접근한다.

Q. Thymeleaf에서 CSS와 JS는 어떻게 연결하는가?

A.
CSS는 `th:href="@{/css/file.css}"`, JS는 `th:src="@{/js/file.js}"`로 연결한다.

---

## 6.2 Static Resource Cache

### [개념]

Static Resource Cache는 CSS, JS, Image 파일을 Browser 또는 CDN에 캐싱하여 성능을 높이는 방식이다.

운영 환경에서는 Versioning 또는 Content Hash 전략을 사용해 Cache 갱신 문제를 줄인다.

```text
/admin.css
→ Browser Cache
→ 파일 변경 후에도 이전 CSS 사용 가능
→ Versioning 필요
```

---

### [핵심]

- Static Resource는 캐싱 대상이다.
- 운영 환경에서는 Cache-Control 정책을 고려한다.
- 파일 변경 시 Browser Cache가 남을 수 있다.
- Version Query 또는 Content Hash를 사용할 수 있다.
- Spring Resource Chain 설정으로 Versioning이 가능하다.
- 개발 중에는 Hard Reload로 확인한다.
- Cache 문제를 Template 경로 문제로 오해하지 않는다.

---

### [실무]

간단한 Version Query:

```html
<link rel="stylesheet" th:href="@{/css/admin.css(v=${appVersion})}" />
```

Resource Chain Version Strategy 예시:

```properties
spring.web.resources.chain.strategy.content.enabled=true
spring.web.resources.chain.strategy.content.paths=/**
```

검수 기준:

```text
CSS 변경 미반영
→ Browser Cache 확인
→ DevTools Disable Cache 확인
→ Resource URL 확인
→ Versioning 적용 여부 확인
```

---

### [FAQ]

Q. CSS를 수정했는데 화면에 반영되지 않는 이유는?

A.
Browser Cache 때문에 이전 CSS가 사용될 수 있다.

Q. Static Resource Cache 문제는 어떻게 줄이는가?

A.
Version Query, Content Hash, Resource Chain Versioning을 사용할 수 있다.

Q. 개발 중 CSS Cache 확인은 어떻게 하는가?

A.
Browser DevTools에서 Disable Cache를 켜고 Hard Reload한다.

---

# 7. Pagination Fragment

## 7.1 Page Based Pagination

### [개념]

Pagination Fragment는 `Page` 객체를 기반으로 목록 화면의 페이지 이동 UI를 재사용하는 Fragment이다.

Admin List Page, Search Result Page에서 반복적으로 사용된다.

```text
Page<UserResponse>
→ Model Attribute: users
→ Pagination Fragment
→ Page Links
```

---

### [핵심]

- Spring Data `Page`는 전체 개수와 전체 페이지 정보를 포함한다.
- Pagination Fragment는 여러 List Page에서 재사용 가능하다.
- 현재 Page, 전체 Page, 이전/다음 여부를 표시한다.
- Search Condition을 Page Link에 유지해야 한다.
- `Pageable` 기반 목록 조회와 함께 사용한다.
- Page Number는 내부적으로 0부터 시작한다.
- 화면에는 `page.number + 1`을 표시한다.

---

### [실무]

Controller:

```java
@GetMapping("/admin/users")
public String list(
        @ModelAttribute("searchForm") UserSearchForm searchForm,
        Pageable pageable,
        Model model
) {
    Page<UserResponse> users = userService.search(searchForm, pageable);

    model.addAttribute("users", users);
    model.addAttribute("searchForm", searchForm);
    return "admin/users/list";
}
```

Pagination Fragment:

```html
<!-- templates/fragments/pagination.html -->
<nav th:fragment="pagination(page, baseUrl)">
  <a
    th:if="${page.hasPrevious()}"
    th:href="@{${baseUrl}(page=${page.number - 1}, size=${page.size})}"
  >
    이전
  </a>

  <span th:text="${page.number + 1}">1</span>
  <span>/</span>
  <span th:text="${page.totalPages}">1</span>

  <a
    th:if="${page.hasNext()}"
    th:href="@{${baseUrl}(page=${page.number + 1}, size=${page.size})}"
  >
    다음
  </a>
</nav>
```

사용:

```html
<nav
  th:replace="~{fragments/pagination :: pagination(${users}, '/admin/users')}"
></nav>
```

주의:

```text
검색 조건 없음
→ Page Link 클릭 시 검색 조건 소실 가능

검색 조건 있음
→ Pagination URL에 keyword, category, status 유지 필요
```

---

### [FAQ]

Q. Pagination Fragment는 무엇인가?

A.
Page 객체를 기반으로 페이지 이동 UI를 재사용하는 Thymeleaf Fragment이다.

Q. Pagination에서 검색 조건을 유지해야 하는 이유는?

A.
다음 페이지로 이동할 때 검색 결과 상태가 유지되어야 하기 때문이다.

Q. Spring Data `Page`와 `Slice` 차이는?

A.
`Page`는 전체 개수와 전체 페이지를 포함하고, `Slice`는 다음 페이지 존재 여부 중심이다.

Q. Page 번호는 0부터 시작하는가?

A.
Spring Data 내부 Page Number는 0부터 시작하고 화면에는 보통 1부터 표시한다.

---

## 7.2 Search Condition Pagination

### [개념]

Search Condition Pagination은 페이지 이동 링크에 검색 조건 Query Parameter를 함께 유지하는 방식이다.

검색 목록에서 Pagination 클릭 시 검색 조건이 사라지지 않도록 한다.

```text
/admin/users?keyword=kim&role=ADMIN&page=0
→ page=1 이동
→ /admin/users?keyword=kim&role=ADMIN&page=1
```

---

### [핵심]

- 검색 조건은 Pagination 링크에 포함해야 한다.
- Query Parameter 이름은 Search Form Field 이름과 일치시키는 것이 좋다.
- `keyword`, `status`, `category`, `region` 같은 조건을 유지한다.
- 민감 정보는 Query Parameter에 넣지 않는다.
- 검색 조건이 많으면 URL 생성 복잡도가 증가한다.
- Fragment Parameter로 searchForm을 전달할 수 있다.

---

### [실무]

User Search Pagination:

```html
<a
  th:if="${users.hasPrevious()}"
  th:href="@{/admin/users(
       page=${users.number - 1},
       size=${users.size},
       keyword=${searchForm.keyword},
       role=${searchForm.role}
   )}"
>
  이전
</a>

<a
  th:if="${users.hasNext()}"
  th:href="@{/admin/users(
       page=${users.number + 1},
       size=${users.size},
       keyword=${searchForm.keyword},
       role=${searchForm.role}
   )}"
>
  다음
</a>
```

검색 Form:

```html
<form th:action="@{/admin/users}" th:object="${searchForm}" method="get">
  <input th:field="*{keyword}" />
  <select th:field="*{role}">
    <option value="">전체</option>
    <option value="USER">USER</option>
    <option value="ADMIN">ADMIN</option>
  </select>
  <button type="submit">검색</button>
</form>
```

---

### [FAQ]

Q. Pagination에서 검색 조건이 사라지는 이유는?

A.
Page Link에 기존 Query Parameter를 포함하지 않았기 때문이다.

Q. 검색 조건은 어디에 유지하는가?

A.
Pagination Link의 Query Parameter에 유지한다.

Q. 검색 조건에 민감 정보를 넣어도 되는가?

A.
안 된다. Query Parameter는 URL에 노출된다.

---

# 8. Error Page Core

## 8.1 Error Page Definition

### [개념]

Error Page는 요청 처리 중 오류가 발생했을 때 사용자에게 보여주는 SSR 화면이다.

대표 Error Page는 400, 403, 404, 500이다.

```text
Exception / Error Status
→ Error Controller or Error View
→ Thymeleaf Error Template
→ HTML Error Response
```

---

### [핵심]

- Error Page는 사용자 안내용 화면이다.
- 내부 서버 정보는 노출하지 않는다.
- Stack Trace를 출력하지 않는다.
- 400은 Bad Request이다.
- 403은 Access Denied이다.
- 404는 Resource Not Found이다.
- 500은 Server Error이다.
- Error Template은 `templates/error` 하위에 두는 것을 권장한다.
- 사용자 행동 안내 링크를 제공한다.

---

### [실무]

권장 구조:

```text
templates/error/
├ 400.html
├ 403.html
├ 404.html
└ 500.html
```

404 Template:

```html
<h1>페이지를 찾을 수 없습니다.</h1>
<p>요청한 페이지가 존재하지 않습니다.</p>
<a th:href="@{/}">홈으로 이동</a>
```

500 Template:

```html
<h1>일시적인 오류가 발생했습니다.</h1>
<p>잠시 후 다시 시도해 주세요.</p>
<a th:href="@{/}">홈으로 이동</a>
```

비권장 출력:

```text
Stack Trace
SQL Error
Internal Class Name
Server File Path
Security Rule Detail
Raw Exception Message
```

---

### [FAQ]

Q. Error Page는 무엇인가?

A.
오류 발생 시 사용자에게 안내를 제공하는 SSR 화면이다.

Q. Error Page에 Stack Trace를 출력해도 되는가?

A.
안 된다. 내부 정보 노출 위험이 있다.

Q. Error Template은 어디에 두는가?

A.
보통 `templates/error` 하위에 둔다.

---

## 8.2 404 Page

### [개념]

404 Page는 요청한 Resource 또는 Page를 찾을 수 없을 때 보여주는 Error Page이다.

SSR Thymeleaf에서는 사용자에게 홈 이동, 목록 이동, 검색 안내를 제공한다.

---

### [핵심]

- 404는 Not Found 상태이다.
- 존재하지 않는 URL, 삭제된 데이터, 잘못된 ID에서 발생할 수 있다.
- 사용자에게 명확한 안내를 제공한다.
- 내부 경로 구조를 과도하게 노출하지 않는다.
- 상세 오류보다 다음 행동을 안내한다.
- Admin Detail 데이터 없음도 404로 처리할 수 있다.

---

### [실무]

404 Template:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
  <body>
    <h1>페이지를 찾을 수 없습니다.</h1>
    <p>요청한 페이지가 존재하지 않거나 이동되었습니다.</p>

    <a th:href="@{/}">홈으로 이동</a>
    <a th:href="@{/admin}">관리자 홈</a>
  </body>
</html>
```

Not Found 예외 처리 예:

```java
@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {

    public ResourceNotFoundException(String message) {
        super(message);
    }
}
```

권장:

```text
사용자 메시지
→ "페이지를 찾을 수 없습니다."

비권장:
→ "com.example.user.UserNotFoundException at UserService..."
```

---

### [FAQ]

Q. 404 Page는 언제 보여주는가?

A.
요청한 URL 또는 데이터가 존재하지 않을 때 보여준다.

Q. 404 Page에 예외 상세를 출력해도 되는가?

A.
권장하지 않는다. 사용자 안내 중심으로 작성한다.

Q. 404 Page에는 어떤 링크를 제공하는가?

A.
홈, 목록, 검색 페이지 링크를 제공할 수 있다.

---

## 8.3 500 Page

### [개념]

500 Page는 서버 내부 오류가 발생했을 때 보여주는 Error Page이다.

Database Error, NullPointerException, External API Error 등 사용자 요청을 정상 처리하지 못한 상황에서 사용된다.

---

### [핵심]

- 500은 Internal Server Error 상태이다.
- 사용자에게 내부 구현 상세를 노출하지 않는다.
- Stack Trace 출력 금지이다.
- 일시적 오류 안내와 재시도 안내를 제공한다.
- 운영 환경에서는 Log와 Monitoring으로 원인을 추적한다.
- 사용자 화면과 개발자 로그를 분리한다.

---

### [실무]

500 Template:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
  <body>
    <h1>일시적인 오류가 발생했습니다.</h1>
    <p>잠시 후 다시 시도해 주세요.</p>

    <a th:href="@{/}">홈으로 이동</a>
  </body>
</html>
```

비권장:

```html
<pre th:text="${trace}">stack trace</pre>
```

운영 기준:

```text
User View
→ 일반 오류 메시지

Server Log
→ Exception Detail

Monitoring
→ Alert / Trace / Metric
```

---

### [FAQ]

Q. 500 Page는 언제 보여주는가?

A.
서버 내부 오류로 요청을 정상 처리하지 못했을 때 보여준다.

Q. 500 Page에 Exception Message를 그대로 보여줘도 되는가?

A.
권장하지 않는다. 내부 정보 노출 위험이 있다.

Q. 500 원인은 어디서 확인하는가?

A.
Server Log, Monitoring, Error Tracking 도구에서 확인한다.

---

# 9. Validation Error Page vs Form Error

## 9.1 Validation Error Rendering Strategy

### [개념]

Validation Error는 별도 Error Page로 보내기보다 사용자가 입력하던 Form View에서 Field Error로 표시하는 것이 기본 전략이다.

```text
Form Validation Fail
→ Same Form View
→ Field Error Rendering
```

---

### [핵심]

- Form Validation Error는 Error Page보다 Form View에서 표시한다.
- `BindingResult`를 유지해야 한다.
- `th:errors`로 Field Error를 출력한다.
- `#fields.hasErrors()`로 Error 상태를 표시한다.
- Redirect하지 않는다.
- 사용자가 입력한 값을 유지한다.
- Business Validation Error도 Form 수정이 가능한 경우 Form View에서 표시한다.

---

### [실무]

잘못된 예:

```java
if (bindingResult.hasErrors()) {
    return "error/400";
}
```

문제:

```text
사용자 입력값 소실
Field Error 표시 불가
사용자 수정 흐름 단절
```

올바른 예:

```java
if (bindingResult.hasErrors()) {
    return "admin/users/create-form";
}
```

Template:

```html
<input th:field="*{email}" />
<p th:errors="*{email}">email error</p>
```

---

### [FAQ]

Q. Validation Error는 Error Page로 보내는가?

A.
보통 보내지 않는다. 사용자가 입력하던 Form View에서 Field Error로 표시한다.

Q. Validation 실패 시 Redirect하면 안 되는 이유는?

A.
BindingResult와 입력값이 사라지기 때문이다.

Q. Validation Error는 Template에서 어떻게 출력하는가?

A.
`th:errors`와 `#fields.hasErrors()`를 사용한다.

---

# 10. Security Fragment

## 10.1 CSRF Fragment

### [개념]

CSRF Fragment는 여러 POST Form에서 반복되는 CSRF Hidden Input을 공통 Fragment로 분리한 것이다.

Spring Security CSRF 보호가 활성화된 SSR Form에서 중복 코드를 줄일 수 있다.

```text
POST Form
→ CSRF Fragment Include
→ Hidden Input Render
→ CSRF Filter 검증
```

---

### [핵심]

- 상태 변경 Form에는 CSRF Token이 필요할 수 있다.
- CSRF Hidden Input은 여러 Form에서 반복된다.
- `th:fragment`로 CSRF Hidden Input을 공통화할 수 있다.
- Fragment 참조 경로와 이름을 통일한다.
- CSRF Fragment를 누락하면 POST 403이 발생할 수 있다.

---

### [실무]

Security Fragment:

```html
<!-- templates/fragments/security.html -->
<input
  th:fragment="csrf"
  type="hidden"
  th:name="${_csrf.parameterName}"
  th:value="${_csrf.token}"
/>
```

Create Form 사용:

```html
<form th:action="@{/admin/users}" method="post">
  <input th:replace="~{fragments/security :: csrf}" />
  <input type="text" name="name" />
  <button type="submit">저장</button>
</form>
```

Delete Form 사용:

```html
<form th:action="@{/admin/users/{id}/delete(id=${user.id})}" method="post">
  <input th:replace="~{fragments/security :: csrf}" />
  <button type="submit">삭제</button>
</form>
```

---

### [FAQ]

Q. CSRF Fragment는 무엇인가?

A.
반복되는 CSRF Hidden Input을 공통 Fragment로 분리한 것이다.

Q. CSRF Fragment는 언제 사용하는가?

A.
생성, 수정, 삭제, 로그아웃처럼 POST Form이 여러 개 있을 때 사용한다.

Q. CSRF Fragment가 없으면 어떻게 되는가?

A.
Spring Security CSRF 보호가 활성화된 경우 POST 요청에서 403이 발생할 수 있다.

---

# 11. Troubleshooting

## 11.1 Layout Fragment Static Error Troubleshooting

### [개념]

Layout, Fragment, Static Resource, Error Page 문제는 Template Path, Fragment Name, Resource URL, Error View 설정 불일치에서 자주 발생한다.

---

### [핵심]

자주 발생하는 문제:

- Fragment Not Found
- Template Not Found
- Static Resource 404
- CSS 변경 미반영
- JavaScript 로드 실패
- Image 로드 실패
- Pagination 검색 조건 소실
- Error Page에 Stack Trace 노출
- Validation Error를 Error Page로 이동
- Layout 중복 Include
- Fragment Parameter 불일치
- CSRF Fragment 누락

---

### [실무]

Fragment Not Found 점검:

```text
Fragment Expression 확인
→ Template Path 확인
→ Fragment File 위치 확인
→ th:fragment 이름 확인
→ `.html` 확장자 작성 여부 확인
→ Parameter 개수 확인
```

Static Resource 404 점검:

```text
File 위치 확인
→ src/main/resources/static 확인
→ URL에 /static 포함 여부 확인
→ th:href / th:src 사용 여부 확인
→ Browser Network 확인
```

CSS 변경 미반영 점검:

```text
Browser Cache 확인
→ Hard Reload
→ DevTools Disable Cache
→ Resource URL 변경 확인
→ Versioning 전략 확인
```

Pagination 조건 소실 점검:

```text
Search Form Field 확인
→ Controller searchForm Model 확인
→ Pagination Link Query Parameter 확인
→ page / size / keyword / status 유지 확인
```

Error Page 점검:

```text
Error Status 확인
→ Error Template 위치 확인
→ 사용자 메시지 확인
→ Stack Trace 노출 여부 확인
→ 홈 / 목록 이동 링크 확인
```

---

### [FAQ]

Q. Fragment Not Found가 발생하는 이유는?

A.
Fragment Template Path 또는 `th:fragment` 이름이 잘못되었을 가능성이 높다.

Q. Static Resource 404가 발생하는 이유는?

A.
파일 위치가 틀렸거나 URL에 `/static`을 잘못 포함했을 수 있다.

Q. Pagination에서 검색 조건이 사라지는 이유는?

A.
Page Link에 검색 조건 Query Parameter를 포함하지 않았기 때문이다.

---

# 12. Common Mistakes

## 12.1 Layout Fragment Static Error Mistakes

### [개념]

Layout Fragment Static Error Mistake는 공통 Template 재사용, 정적 파일 연결, 오류 화면 처리 기준이 일관되지 않아 발생하는 문제이다.

---

### [핵심]

자주 발생하는 실수:

- Fragment 참조에 `.html` 확장자 포함
- Fragment Path 앞에 불필요한 `/` 사용
- `th:fragment` 이름과 참조 이름 불일치
- `th:replace`와 `th:insert` 차이 혼동
- Fragment Parameter 개수 불일치
- Static Resource URL에 `/static` 포함
- CSS / JS를 일반 `href`, `src`로 하드코딩
- Browser Cache 문제를 Template 오류로 착각
- Pagination Link에 검색 조건 누락
- Error Page에 Stack Trace 출력
- 500 Error에서 Raw Exception Message 출력
- Validation Error를 별도 Error Page로 이동
- Admin Layout에 권한별 Menu 제어 누락
- POST Form에서 CSRF Fragment 누락

---

### [실무]

잘못된 Fragment 참조:

```html
<div th:replace="~{/fragments/header.html :: header}"></div>
```

올바른 Fragment 참조:

```html
<div th:replace="~{fragments/header :: header}"></div>
```

잘못된 Static Resource:

```html
<link rel="stylesheet" href="/static/css/admin.css" />
```

올바른 Static Resource:

```html
<link rel="stylesheet" th:href="@{/css/admin.css}" />
```

잘못된 Error Page:

```html
<pre th:text="${trace}">stack trace</pre>
```

올바른 Error Page:

```html
<h1>일시적인 오류가 발생했습니다.</h1>
<p>잠시 후 다시 시도해 주세요.</p>
<a th:href="@{/}">홈으로 이동</a>
```

---

### [FAQ]

Q. Fragment 참조에 `.html`을 붙이면 안 되는가?

A.
보통 붙이지 않는다. `~{fragments/header :: header}` 형태를 권장한다.

Q. Static Resource 경로에 `/static`을 붙이면 안 되는가?

A.
Spring Boot 기본 설정에서는 URL에 `/static`을 포함하지 않는다.

Q. Error Page에 오류 상세를 보여주면 안 되는 이유는?

A.
서버 내부 정보가 노출될 수 있기 때문이다.

---

# 13. Review Checklist

## 13.1 Layout Fragment Static Error Review Checklist

### [개념]

Review Checklist는 Agent가 SSR Thymeleaf Layout, Fragment, Static Resource, Pagination, Error Page를 검수하기 위한 기준이다.

---

### [핵심]

Layout 검수:

- Header / Footer / Sidebar 공통화 여부
- Admin Layout 구조 일관성 여부
- Page Content 영역 명확성 여부
- 중복 HTML 과다 여부
- Flash Message 영역 위치 적절성 여부
- 권한별 메뉴 표시 위치 적절성 여부

Fragment 검수:

- `th:fragment` 이름 명확성
- Fragment 파일 위치 적절성
- `th:replace` / `th:insert` 사용 의도 적절성
- Fragment Expression Path 정확성
- Fragment Parameter 개수 일치 여부
- Fragment가 과도한 Business Logic을 포함하는지 여부
- CSRF Fragment 재사용 여부

Static Resource 검수:

- CSS / JS / Image 파일이 `static` 하위에 있는지 여부
- URL에 `/static`을 포함하지 않았는지 여부
- `th:href`, `th:src`, `@{}` 사용 여부
- CSS Cache 문제 대응 여부
- Resource 404 여부

Pagination 검수:

- `Page` 또는 `Slice` 사용 목적 적절성
- Page Link의 page / size 유지 여부
- 검색 조건 Query Parameter 유지 여부
- 민감 정보 Query Parameter 포함 여부
- Pagination Fragment 재사용 가능성 여부

Error Page 검수:

- 400 / 403 / 404 / 500 Template 존재 여부
- Stack Trace 노출 여부
- Raw Exception Message 노출 여부
- 사용자 안내 메시지 존재 여부
- 홈 / 목록 이동 링크 제공 여부
- Validation Error를 Form View에서 처리하는지 여부

---

### [실무]

검수 Flow:

```text
Layout 구조 확인
→ Fragment Path 확인
→ th:fragment 이름 확인
→ th:replace / th:insert 의도 확인
→ Static Resource URL 확인
→ Pagination Query Parameter 확인
→ CSRF Fragment 확인
→ Error Page 정보 노출 확인
→ Validation Error 처리 위치 확인
```

---

### [FAQ]

Q. Layout 검수 핵심은?

A.
공통 영역 중복 제거, Fragment 재사용, Page Content 구조 일관성을 확인하는 것이다.

Q. Fragment 검수 핵심은?

A.
Template Path, Fragment Name, `th:replace` / `th:insert`, Parameter 개수 일치 여부를 확인하는 것이다.

Q. Static Resource 검수 핵심은?

A.
파일 위치가 `static` 하위인지, URL에 `/static`이 없는지, `@{}`를 사용하는지 확인하는 것이다.

Q. Error Page 검수 핵심은?

A.
Stack Trace와 내부 정보를 노출하지 않고 사용자 안내 중심인지 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Thymeleaf Layout이란?
A. Header, Footer, Sidebar 같은 공통 화면 구조를 재사용하는 방식이다.

Q. Thymeleaf Fragment란?
A. Template 일부를 재사용 가능한 HTML 조각으로 분리한 것이다.

Q. `th:fragment`는 무엇인가?
A. 재사용 가능한 HTML 조각을 정의하는 Thymeleaf Attribute이다.

Q. Fragment Expression은 무엇인가?
A. `~{templatePath :: fragmentName}` 형식으로 Fragment를 참조하는 Expression이다.

Q. Fragment 참조에 `.html`을 붙이는가?
A. 보통 붙이지 않는다.

Q. `th:replace`는 무엇인가?
A. 현재 Element를 Fragment Root Element로 완전히 교체하는 Attribute이다.

Q. `th:insert`는 무엇인가?
A. 현재 Element 내부에 Fragment를 삽입하는 Attribute이다.

Q. `th:replace`와 `th:insert` 차이는?
A. `th:replace`는 현재 Element를 교체하고, `th:insert`는 내부에 삽입한다.

Q. Fragment에 Parameter를 전달할 수 있는가?
A. 가능하다. `th:fragment="name(param)"` 형태로 선언한다.

Q. Parameterized Fragment는 언제 사용하는가?
A. Alert, Badge, Pagination처럼 같은 UI 구조에 값만 달라지는 경우 사용한다.

Q. Admin Layout에서 공통화할 요소는?
A. Header, Sidebar, Alert, Search Form, Pagination, Footer를 공통화할 수 있다.

Q. Spring Boot Static Resource는 어디에 둔다?
A. `src/main/resources/static` 하위에 둔다.

Q. Static Resource URL에 `/static`을 포함하는가?
A. 보통 포함하지 않는다.

Q. Thymeleaf에서 CSS는 어떻게 연결하는가?
A. `th:href="@{/css/file.css}"` 형식으로 연결한다.

Q. Thymeleaf에서 JavaScript는 어떻게 연결하는가?
A. `th:src="@{/js/file.js}"` 형식으로 연결한다.

Q. Thymeleaf에서 Image는 어떻게 연결하는가?
A. `th:src="@{/images/file.png}"` 형식으로 연결한다.

Q. CSS를 수정했는데 반영되지 않는 이유는?
A. Browser Cache 때문에 이전 CSS가 사용될 수 있다.

Q. Static Resource Cache 문제는 어떻게 줄이는가?
A. Version Query, Content Hash, Resource Chain Versioning을 사용할 수 있다.

Q. Pagination Fragment란?
A. Page 객체를 기반으로 페이지 이동 UI를 재사용하는 Thymeleaf Fragment이다.

Q. Pagination에서 검색 조건을 유지해야 하는 이유는?
A. 다음 페이지로 이동할 때 검색 결과 상태가 유지되어야 하기 때문이다.

Q. Pagination에서 검색 조건이 사라지는 이유는?
A. Page Link에 기존 Query Parameter를 포함하지 않았기 때문이다.

Q. Spring Data `Page`와 `Slice` 차이는?
A. `Page`는 전체 개수와 전체 페이지를 포함하고, `Slice`는 다음 페이지 존재 여부 중심이다.

Q. Error Page란?
A. 오류 발생 시 사용자에게 안내를 제공하는 SSR 화면이다.

Q. Error Template은 어디에 둔다?
A. 보통 `templates/error` 하위에 둔다.

Q. 404 Page는 언제 보여주는가?
A. 요청한 URL 또는 데이터가 존재하지 않을 때 보여준다.

Q. 500 Page는 언제 보여주는가?
A. 서버 내부 오류로 요청을 정상 처리하지 못했을 때 보여준다.

Q. Error Page에 Stack Trace를 출력해도 되는가?
A. 안 된다. 내부 정보 노출 위험이 있다.

Q. Validation Error는 Error Page로 보내는가?
A. 보통 보내지 않고 입력하던 Form View에서 Field Error로 표시한다.

Q. CSRF Fragment는 무엇인가?
A. 반복되는 CSRF Hidden Input을 공통 Fragment로 분리한 것이다.

Q. CSRF Fragment가 없으면 어떻게 되는가?
A. Spring Security CSRF 보호가 활성화된 경우 POST 요청에서 403이 발생할 수 있다.

Q. Fragment Not Found 원인은?
A. Fragment Template Path 또는 `th:fragment` 이름이 잘못되었을 가능성이 높다.

Q. Static Resource 404 원인은?
A. 파일 위치가 틀렸거나 URL에 `/static`을 잘못 포함했을 수 있다.

Q. Layout Fragment 검수 핵심은?
A. Fragment Path, Fragment Name, `th:replace` / `th:insert`, Parameter 개수 일치 여부를 확인하는 것이다.

Q. Static Resource 검수 핵심은?
A. 파일 위치, `/static` 포함 여부, `th:href`, `th:src`, `@{}` 사용 여부를 확인하는 것이다.

Q. Error Page 검수 핵심은?
A. Stack Trace와 내부 정보를 노출하지 않고 사용자 안내 중심인지 확인하는 것이다.
