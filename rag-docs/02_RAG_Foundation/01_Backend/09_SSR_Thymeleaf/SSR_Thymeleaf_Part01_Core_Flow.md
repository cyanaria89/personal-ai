# SSR Thymeleaf Part01 - Core Flow

---

# 1. SSR Thymeleaf Core

## 1.1 SSR Definition

### [개념]

SSR(Server-Side Rendering)은 서버가 HTML을 생성해서 Browser에게 반환하는 Rendering 방식이다.

Spring MVC + Thymeleaf 환경에서는 `@Controller`가 `Model`에 데이터를 담고 `View Name`을 반환한다. 이후 `View Resolver`와 `Thymeleaf Template Engine`이 Template을 렌더링하여 최종 HTML Response를 생성한다.

```text
Request
→ DispatcherServlet
→ @Controller
→ Model
→ View Name
→ View Resolver
→ Thymeleaf Template Engine
→ HTML Response
```

---

### [핵심]

- SSR은 서버에서 HTML을 생성한다.
- Browser는 완성된 HTML을 받아 렌더링한다.
- Spring MVC SSR은 `@Controller` 중심이다.
- Thymeleaf는 서버 Template Engine이다.
- `Model`은 Controller에서 Template으로 데이터를 전달한다.
- Controller의 `String` 반환값은 View Name으로 해석될 수 있다.
- View Name은 `src/main/resources/templates` 하위 Template 경로와 매핑된다.
- SSR Thymeleaf는 REST API가 아니라 HTML View Rendering 구조이다.

---

### [실무]

2026 실무 기준 SSR Thymeleaf는 전체 Public Web Service보다 다음 영역에 적합하다.

- Admin Page
- Backoffice
- Internal Tool
- Form-heavy CRUD Page
- Login Page
- Error Page
- Legacy Spring MVC Page
- Simple Management Page

복잡한 Client State, 실시간 UI, Dynamic UX가 많은 화면은 React / Vue / Next.js + REST API 구조를 우선 검토한다.

```text
Admin Page / Backoffice
→ SSR Thymeleaf 가능

Form-heavy Internal Tool
→ SSR Thymeleaf 가능

Login Page / Error Page
→ SSR Thymeleaf 가능

Public SPA / Dynamic UX
→ React / REST API 권장

Mobile App / External API
→ REST API 권장
```

---

### [FAQ]

Q. SSR이란?

A.
Server-Side Rendering이다.
서버가 HTML을 생성해서 Browser에게 반환하는 방식이다.

Q. Thymeleaf는 무엇인가?

A.
Spring MVC에서 자주 사용하는 서버 Template Engine이다.
Model 데이터를 HTML Template에 바인딩하여 최종 HTML을 생성한다.

Q. SSR Thymeleaf는 React와 같은 방식인가?

A.
아니다.
Thymeleaf는 서버에서 HTML을 생성하고, React는 주로 Browser에서 UI를 구성한다.

Q. SSR Thymeleaf는 언제 적합한가?

A.
Admin Page, Backoffice, Internal Tool, Form-heavy CRUD 화면에 적합하다.

---

# 2. Spring MVC SSR Flow

## 2.1 Request To HTML Response Flow

### [개념]

Spring MVC SSR Flow는 HTTP Request가 `DispatcherServlet`을 거쳐 Controller에 도달한 뒤, Controller가 Model에 데이터를 담고 View Name을 반환하여 HTML Response를 생성하는 흐름이다.

```text
Browser Request
→ DispatcherServlet
→ HandlerMapping
→ @Controller Method
→ Model Add Attribute
→ Return View Name
→ View Resolver
→ Thymeleaf Template Engine
→ Render HTML
→ Browser Response
```

---

### [핵심]

- `DispatcherServlet`은 Spring MVC의 Front Controller이다.
- `HandlerMapping`은 요청 URL에 맞는 Controller Method를 찾는다.
- `@Controller`는 View Rendering을 담당한다.
- `Model`은 View에 전달할 데이터를 저장한다.
- `return "users/list"`는 View Name이다.
- View Resolver는 View Name을 Template 경로로 해석한다.
- Thymeleaf Template Engine은 Model 데이터를 HTML에 반영한다.
- 최종 Response는 JSON이 아니라 HTML이다.

---

### [실무]

SSR Controller는 JSON API Controller와 목적이 다르다.

```java
@Controller
public class UserViewController {

    @GetMapping("/users")
    public String users(Model model) {
        model.addAttribute("users", userService.findAll());
        return "users/list";
    }
}
```

Template 위치:

```text
src/main/resources/templates/users/list.html
```

View Name Mapping:

```text
return "users/list"
→ templates/users/list.html
```

Controller와 Template 연결 기준:

```text
Controller Method
→ model.addAttribute("users", users)
→ return "users/list"
→ templates/users/list.html
→ ${users}
```

---

### [FAQ]

Q. Spring MVC SSR Flow는?

A.
Request → DispatcherServlet → Controller → Model → View Name → Thymeleaf Template → HTML Response 흐름이다.

Q. Controller에서 문자열을 반환하면 항상 HTML View인가?

A.
아니다.
`@Controller`에서는 View Name으로 해석될 수 있지만, `@RestController`에서는 Response Body로 반환된다.

Q. `return "users/list"`는 파일 경로인가?

A.
정확히는 View Name이다.
기본 설정에서는 `templates/users/list.html`과 매핑된다.

Q. SSR Controller에서 `@ResponseBody`를 붙이면 어떻게 되는가?

A.
View Rendering이 아니라 Response Body 반환이 된다.
HTML Template Rendering 목적이면 사용하지 않는다.

---

# 3. @Controller And @RestController

## 3.1 Controller Type Difference

### [개념]

`@Controller`는 View Rendering을 위한 Controller이다.

`@RestController`는 JSON, Text 같은 Response Body 반환을 위한 Controller이다.

| Category        | @Controller    | @RestController |
| --------------- | -------------- | --------------- |
| Main Purpose    | View Rendering | REST API        |
| Return String   | View Name      | Response Body   |
| Response        | HTML           | JSON / Text     |
| Template Engine | 사용           | 보통 사용 안 함 |
| Typical Use     | SSR Page       | API Server      |

---

### [핵심]

- SSR Thymeleaf는 `@Controller`를 사용한다.
- REST API는 `@RestController`를 사용한다.
- `@RestController`는 `@Controller + @ResponseBody`이다.
- Thymeleaf View Name 반환에는 `@RestController`를 사용하지 않는다.
- View Rendering과 API Response를 같은 Controller에 섞지 않는 것이 좋다.
- `@ResponseBody`가 붙으면 View Resolver를 거치지 않는다.

---

### [실무]

SSR View Controller 예시:

```java
@Controller
@RequestMapping("/admin/users")
public class AdminUserViewController {

    @GetMapping
    public String list(Model model) {
        model.addAttribute("users", userService.findAll());
        return "admin/users/list";
    }
}
```

REST API Controller 예시:

```java
@RestController
@RequestMapping("/api/users")
public class UserApiController {

    @GetMapping
    public List<UserResponse> list() {
        return userService.findAll();
    }
}
```

권장 분리:

```text
/admin/users
→ SSR View Controller
→ @Controller
→ HTML Response

/api/users
→ REST API Controller
→ @RestController
→ JSON Response
```

---

### [FAQ]

Q. Thymeleaf 화면을 반환하려면 어떤 Annotation을 사용하는가?

A.
`@Controller`를 사용한다.

Q. `@RestController`로 Thymeleaf View를 반환할 수 있는가?

A.
일반적으로 불가능하다.
문자열이 View Name이 아니라 Response Body로 반환된다.

Q. `users/list` 문자열이 그대로 출력되는 이유는?

A.
`@RestController` 또는 `@ResponseBody`가 적용되었을 가능성이 높다.

Q. View Controller와 API Controller를 분리해야 하는가?

A.
실무에서는 분리 권장이다.
View Rendering과 API Response 책임이 다르기 때문이다.

---

# 4. Model

## 4.1 Model Attribute

### [개념]

`Model`은 Controller에서 Thymeleaf Template으로 데이터를 전달하는 객체이다.

Controller는 `model.addAttribute(name, value)`로 데이터를 담고, Template은 `${name}`으로 접근한다.

```text
Controller
→ model.addAttribute("user", user)
→ Thymeleaf Template
→ ${user.name}
```

---

### [핵심]

- `Model`은 View에 전달할 데이터를 저장한다.
- Attribute Name은 Template에서 사용하는 변수명이 된다.
- Attribute Value는 DTO, List, Page, Form Object 등이 될 수 있다.
- Template은 `${attributeName}`으로 Model Attribute에 접근한다.
- Form Binding에서는 `th:object`와 함께 Form Object를 Model에 담아야 한다.
- Model Attribute 이름과 Template Expression 이름은 반드시 일치해야 한다.

---

### [실무]

Controller:

```java
@GetMapping("/users/{id}")
public String detail(@PathVariable Long id, Model model) {
    UserResponse user = userService.findById(id);
    model.addAttribute("user", user);
    return "users/detail";
}
```

Template:

```html
<h1 th:text="${user.name}">User Name</h1>
<p th:text="${user.email}">user@example.com</p>
```

권장 기준:

```text
단일 객체
→ user, order, festival

목록 객체
→ users, orders, festivals

Form Object
→ userForm, orderForm, festivalForm

Search Form
→ searchForm, userSearchForm
```

Entity 직접 전달 기준:

```text
단순 내부 Admin Page
→ Entity 직접 전달 가능

외부 노출 화면 / 복잡한 화면 / 보안 고려 필요
→ DTO 전달 권장
```

---

### [FAQ]

Q. Model은 무엇인가?

A.
Controller에서 View로 데이터를 전달하는 객체이다.

Q. `model.addAttribute("user", user)`의 `"user"`는 무엇인가?

A.
Template에서 접근할 변수명이다.
Thymeleaf에서는 `${user}`로 접근한다.

Q. `${user.name}`이 출력되지 않는 이유는?

A.
Model에 `user` Attribute가 없거나 이름이 다를 수 있다.

Q. Entity를 Model에 직접 담아도 되는가?

A.
단순 Admin Page에서는 가능하다.
외부 노출 화면이나 복잡한 화면에서는 DTO 사용을 권장한다.

---

# 5. View Name And Template Path

## 5.1 View Name Mapping

### [개념]

View Name은 Controller가 반환하는 논리적인 View 이름이다.

Spring Boot + Thymeleaf 기본 설정에서는 View Name이 `templates` 하위 HTML Template 경로로 매핑된다.

```text
return "admin/users/list"
→ src/main/resources/templates/admin/users/list.html
```

---

### [핵심]

- View Name은 논리 경로이다.
- 기본 prefix는 `classpath:/templates/`이다.
- 기본 suffix는 `.html`이다.
- `return "index"`는 `templates/index.html`로 매핑된다.
- `return "admin/dashboard"`는 `templates/admin/dashboard.html`로 매핑된다.
- View Name에 `.html`을 붙이지 않는 것이 일반적이다.
- View Name 앞에 불필요한 `/`를 붙이지 않는 것이 일반적이다.

---

### [실무]

Controller:

```java
@GetMapping("/admin")
public String dashboard() {
    return "admin/dashboard";
}
```

Template Path:

```text
src/main/resources/templates/admin/dashboard.html
```

잘못된 예:

```java
return "/admin/dashboard.html";
```

권장 예:

```java
return "admin/dashboard";
```

Template Not Found 점검:

```text
View Name 확인
→ templates 하위 경로 확인
→ 파일명 확인
→ 대소문자 확인
→ .html 확장자 확인
→ Build Resource 포함 여부 확인
```

---

### [FAQ]

Q. View Name에 `.html`을 붙이는가?

A.
보통 붙이지 않는다.
Thymeleaf View Resolver가 suffix `.html`을 적용한다.

Q. View Name 앞에 `/`를 붙이는가?

A.
일반적으로 붙이지 않는다.
`"admin/dashboard"`처럼 논리 경로를 반환한다.

Q. Template Not Found가 발생하는 이유는?

A.
View Name과 실제 Template 경로가 맞지 않거나 Template 파일이 없기 때문이다.

---

# 6. Thymeleaf Rendering

## 6.1 Template Rendering

### [개념]

Thymeleaf Rendering은 HTML Template에 Model 데이터를 바인딩하여 최종 HTML을 생성하는 과정이다.

```text
Template HTML
+ Model Attribute
+ Thymeleaf th:* Attribute
→ Thymeleaf Render
→ Final HTML Response
```

---

### [핵심]

- Thymeleaf는 서버에서 실행된다.
- `th:*` 속성은 서버 렌더링 시 처리된다.
- Browser는 처리 완료된 HTML을 받는다.
- `th:text`는 Text Escaping을 적용한다.
- `th:utext`는 Unescaped Text를 출력한다.
- `th:if`, `th:each`, `th:href` 등으로 동적 HTML을 구성한다.
- Template에 복잡한 Business Logic을 넣지 않는다.

---

### [실무]

Template:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
  <body>
    <h1 th:text="${pageTitle}">Default Title</h1>

    <ul>
      <li th:each="user : ${users}" th:text="${user.name}">User Name</li>
    </ul>
  </body>
</html>
```

Rendering 결과:

```html
<h1>사용자 목록</h1>
<ul>
  <li>kim</li>
  <li>lee</li>
</ul>
```

권장 역할 분리:

```text
Service
→ Business Logic 처리

Controller
→ View에 필요한 데이터 준비

Template
→ Rendering 전용
```

---

### [FAQ]

Q. `th:text`는 언제 처리되는가?

A.
서버에서 HTML Response를 생성할 때 처리된다.

Q. Browser에서 `th:text`가 실행되는가?

A.
아니다.
Browser는 Thymeleaf 처리 후 완성된 HTML을 받는다.

Q. `th:utext`는 왜 주의해야 하는가?

A.
HTML Escaping 없이 출력하므로 XSS 위험이 있다.

Q. Template에 Business Logic을 넣어도 되는가?

A.
권장하지 않는다.
Service에서 처리 후 Model로 전달하는 것이 좋다.

---

# 7. SSR vs CSR vs REST API

## 7.1 Rendering Architecture Comparison

### [개념]

SSR은 서버가 HTML을 반환하는 방식이다.

CSR(Client-Side Rendering)은 Browser가 JavaScript로 UI를 구성하는 방식이다.

REST API는 JSON 데이터를 반환하고, 화면 렌더링은 Client가 담당한다.

| Category   | SSR Thymeleaf           | CSR React         | REST API        |
| ---------- | ----------------------- | ----------------- | --------------- |
| Response   | HTML                    | HTML + JS         | JSON            |
| Rendering  | Server                  | Browser           | 없음            |
| Controller | @Controller             | Static Host + API | @RestController |
| Template   | Thymeleaf               | JSX               | 없음            |
| State      | Server / Session / Form | Client State      | Stateless API   |
| Use Case   | Admin, Internal Tool    | Dynamic UX        | External API    |

---

### [핵심]

- SSR은 HTML을 직접 반환한다.
- CSR은 JavaScript가 화면을 구성한다.
- REST API는 데이터만 반환한다.
- Thymeleaf는 REST API 대체물이 아니다.
- React와 Thymeleaf를 같은 화면 책임으로 혼합하면 복잡도가 증가한다.
- SSR과 REST API는 Controller 책임을 분리하는 것이 좋다.

---

### [실무]

선택 기준:

```text
단순 CRUD Admin
→ SSR Thymeleaf

복잡한 사용자 인터랙션
→ React / CSR

Mobile App 연동
→ REST API

외부 서비스 연동
→ REST API

로그인 페이지 / 에러 페이지
→ SSR Thymeleaf 가능
```

혼합 구조 예:

```text
/admin/**
→ Thymeleaf SSR

/api/**
→ REST API

/static/**
→ CSS / JS / Images
```

---

### [FAQ]

Q. Thymeleaf와 React를 같이 사용할 수 있는가?

A.
가능은 하다.
하지만 같은 화면 책임을 섞으면 유지보수가 어려워질 수 있다.

Q. Admin Page는 Thymeleaf로 만들어도 되는가?

A.
가능하다.
단순 CRUD, 검색, Pagination 중심이면 SSR Thymeleaf가 효율적이다.

Q. 외부 API 서버에 Thymeleaf가 필요한가?

A.
대부분 필요 없다.
외부 API는 JSON 기반 REST API가 적합하다.

---

# 8. Basic SSR List Pattern

## 8.1 List Page Pattern

### [개념]

List Page Pattern은 목록 데이터를 조회하여 Model에 담고 목록 Template을 렌더링하는 SSR 기본 패턴이다.

```text
GET /admin/users
→ userService.findAll()
→ model.addAttribute("users", users)
→ return "admin/users/list"
```

---

### [핵심]

- 목록 화면은 `GET` 요청으로 처리한다.
- Service에서 필요한 데이터를 조회한다.
- 조회 결과를 Model에 담는다.
- View Name은 목록 Template을 가리킨다.
- Template에서는 `th:each`로 반복 렌더링한다.
- 데이터가 많으면 `Page` 또는 `Slice`를 사용한다.

---

### [실무]

Controller:

```java
@Controller
@RequestMapping("/admin/users")
public class AdminUserController {

    @GetMapping
    public String list(Model model) {
        List<UserResponse> users = userService.findAll();
        model.addAttribute("users", users);
        return "admin/users/list";
    }
}
```

Template:

```html
<table>
  <tr>
    <th>ID</th>
    <th>Email</th>
    <th>Name</th>
  </tr>
  <tr th:each="user : ${users}">
    <td th:text="${user.id}">1</td>
    <td th:text="${user.email}">email</td>
    <td th:text="${user.name}">name</td>
  </tr>
</table>
```

대량 데이터 기준:

```text
소량 고정 데이터
→ List 가능

관리자 목록 / 검색 목록 / 운영 데이터
→ Page 권장

무한 스크롤 / 더보기
→ Slice 가능
```

---

### [FAQ]

Q. 목록 화면에서는 어떤 HTTP Method를 사용하는가?

A.
일반적으로 `GET`을 사용한다.

Q. 목록 데이터는 Template에서 어떻게 반복하는가?

A.
`th:each`를 사용한다.

Q. 목록 데이터 Attribute 이름은 어떻게 정하는가?

A.
명확한 복수형 이름을 권장한다.
예: `users`, `orders`, `festivals`

Q. Admin 목록에서 `findAll()`을 사용해도 되는가?

A.
데이터가 적은 초기에는 가능하지만, 실무에서는 Pagination을 권장한다.

---

# 9. Basic SSR Detail Pattern

## 9.1 Detail Page Pattern

### [개념]

Detail Page Pattern은 식별자를 통해 단일 데이터를 조회하고 상세 Template을 렌더링하는 패턴이다.

```text
GET /admin/users/{id}
→ userService.findById(id)
→ model.addAttribute("user", user)
→ return "admin/users/detail"
```

---

### [핵심]

- 상세 화면은 `GET` 요청으로 처리한다.
- URL Path Variable로 식별자를 받는다.
- Service에서 단일 데이터를 조회한다.
- 조회 결과를 Model에 담는다.
- Template에서는 `${user.property}` 형태로 출력한다.
- 데이터가 없으면 Not Found 처리한다.

---

### [실무]

Controller:

```java
@GetMapping("/{id}")
public String detail(@PathVariable Long id, Model model) {
    UserResponse user = userService.findById(id);
    model.addAttribute("user", user);
    return "admin/users/detail";
}
```

Template:

```html
<h1 th:text="${user.name}">User Name</h1>
<p th:text="${user.email}">email@example.com</p>

<a th:href="@{/admin/users}">목록</a>
<a th:href="@{/admin/users/{id}/edit(id=${user.id})}">수정</a>
```

Not Found 처리:

```text
조회 대상 없음
→ ResourceNotFoundException
→ 404 Error Page
```

---

### [FAQ]

Q. 상세 화면에서 ID는 어떻게 받는가?

A.
`@PathVariable`로 받는다.

Q. 상세 데이터가 없으면 어떻게 처리하는가?

A.
Service에서 Not Found 예외를 발생시키고 404 Error Page로 연결한다.

Q. 상세 화면 Template에서는 데이터를 어떻게 출력하는가?

A.
`${user.name}`, `${user.email}` 같은 Variable Expression을 사용한다.

---

# 10. Basic SSR Navigation Pattern

## 10.1 Link Rendering

### [개념]

Thymeleaf에서 링크는 `th:href`와 Link Expression `@{}`를 사용한다.

```html
<a th:href="@{/admin/users}">Users</a>
```

---

### [핵심]

- `th:href`는 서버에서 URL을 생성한다.
- Link Expression은 `@{}`를 사용한다.
- Path Variable과 Query Parameter를 표현할 수 있다.
- Context Path를 자동 반영할 수 있다.
- 직접 문자열 조합보다 `@{}` 사용을 권장한다.

---

### [실무]

고정 URL:

```html
<a th:href="@{/admin/users}">사용자 목록</a>
```

Path Variable:

```html
<a th:href="@{/admin/users/{id}(id=${user.id})}">상세</a>
```

Query Parameter:

```html
<a th:href="@{/admin/users(page=${page.number}, keyword=${keyword})}">
  검색 유지
</a>
```

Path Variable + Query Parameter:

```html
<a
  th:href="@{/admin/users/{id}(id=${user.id}, page=${page.number}, keyword=${keyword})}"
>
  상세
</a>
```

---

### [FAQ]

Q. Thymeleaf에서 링크는 어떻게 만든다?

A.
`th:href`와 `@{}` Link Expression을 사용한다.

Q. Path Variable은 어떻게 넣는가?

A.
`@{/users/{id}(id=${user.id})}` 형태를 사용한다.

Q. Query Parameter는 어떻게 넣는가?

A.
`@{/users(page=${page}, keyword=${keyword})}` 형태를 사용한다.

---

# 11. Agent Decision Rules

## 11.1 SSR Thymeleaf Selection Rules

### [개념]

Agent Decision Rules는 요구사항을 보고 SSR Thymeleaf 적용 여부를 판단하는 기준이다.

SSR Thymeleaf는 모든 Web UI에 적용하는 기본값이 아니라, 화면 특성과 운영 목적에 따라 선택한다.

---

### [핵심]

SSR Thymeleaf 적합:

- Admin Page
- Backoffice
- Internal Tool
- Form-heavy CRUD
- Simple Search / Filter / Pagination
- Login Page
- Error Page
- Legacy MVC 유지보수

SSR Thymeleaf 비적합:

- 복잡한 Client State
- 실시간 UX 중심 화면
- Public SPA
- Mobile App API
- 외부 공개 API
- 대규모 Frontend 상태 관리 필요 화면

---

### [실무]

선택 Flow:

```text
관리자 / 내부 도구인가?
→ Yes
→ Form / Table / Pagination 중심인가?
→ Yes
→ SSR Thymeleaf 가능

사용자 Public 화면인가?
→ Yes
→ Dynamic UX / Client State가 많은가?
→ Yes
→ React / REST API 권장

Mobile App 또는 외부 연동인가?
→ Yes
→ REST API 권장
```

---

### [FAQ]

Q. Agent는 언제 Thymeleaf를 선택해야 하는가?

A.
Admin Page, Backoffice, Form-heavy CRUD, 단순 검색 / 목록 / 상세 화면이면 Thymeleaf를 선택할 수 있다.

Q. Agent는 언제 REST API를 선택해야 하는가?

A.
Mobile App, 외부 API, React Frontend, 복잡한 Dynamic UX가 필요하면 REST API를 선택한다.

Q. Thymeleaf와 REST API를 함께 사용할 수 있는가?

A.
가능하다.
단, `/admin/**`는 SSR, `/api/**`는 REST API처럼 책임을 분리하는 것이 좋다.

---

# 12. Common Mistakes

## 12.1 SSR Core Mistakes

### [개념]

SSR Thymeleaf Core Mistake는 View Rendering 흐름을 REST API 흐름처럼 작성해서 발생하는 오류이다.

---

### [핵심]

자주 발생하는 실수:

- `@RestController`로 View Name 반환
- `@ResponseBody`가 붙은 Method에서 View Name 반환
- View Name에 `.html` 포함
- View Name 앞에 불필요한 `/` 포함
- Template 경로와 View Name 불일치
- `Model`에 필요한 Attribute 누락
- Template에서 잘못된 Attribute 이름 사용
- `th:text` 대신 일반 HTML Text만 작성
- `th:utext` 남용
- Static Resource 경로 직접 하드코딩
- JSON API와 SSR View 책임 혼합
- Template에 Business Logic 과다 작성

---

### [실무]

잘못된 예:

```java
@RestController
public class PageController {

    @GetMapping("/users")
    public String users() {
        return "users/list";
    }
}
```

결과:

```text
Response Body: users/list
```

올바른 예:

```java
@Controller
public class PageController {

    @GetMapping("/users")
    public String users() {
        return "users/list";
    }
}
```

결과:

```text
templates/users/list.html 렌더링
```

잘못된 View Name:

```java
return "/admin/users/list.html";
```

올바른 View Name:

```java
return "admin/users/list";
```

---

### [FAQ]

Q. `users/list` 문자열만 화면에 출력되는 이유는?

A.
`@RestController`를 사용했을 가능성이 높다.
SSR View 반환은 `@Controller`를 사용해야 한다.

Q. Template Not Found가 나는 이유는?

A.
View Name과 Template 파일 경로가 일치하지 않기 때문이다.

Q. `${user.name}`이 출력되지 않는 이유는?

A.
Model에 `user` Attribute가 없거나 이름이 다를 수 있다.

Q. SSR 화면과 REST API를 같은 Controller에 섞어도 되는가?

A.
권장하지 않는다.
View Controller와 API Controller를 분리하는 것이 좋다.

---

# 13. Review Checklist

## 13.1 SSR Core Review Checklist

### [개념]

Review Checklist는 SSR Thymeleaf 문서 또는 코드 검수 시 사용하는 Agent용 점검 기준이다.

---

### [핵심]

Controller 검수:

- `@Controller` 사용 여부
- `@RestController` 오사용 여부
- `@ResponseBody` 오사용 여부
- View Name 반환 여부
- Model Attribute 누락 여부
- URL Mapping 명확성
- View Controller와 API Controller 분리 여부

View Name 검수:

- View Name과 Template Path 일치 여부
- View Name에 `.html` 포함 여부
- View Name 앞에 불필요한 `/` 포함 여부
- Template 파일 위치가 `resources/templates` 하위인지 여부

Template 검수:

- Template 경로와 View Name 일치 여부
- `xmlns:th` 선언 여부
- `th:text` 사용 여부
- `th:each` 반복 렌더링 적절성
- `th:href` Link Expression 사용 여부
- `th:utext` 남용 여부
- Model Attribute 이름 일치 여부

Architecture 검수:

- SSR이 적합한 화면인지 확인
- REST API가 더 적합한 요구사항인지 확인
- Admin / Backoffice / Internal Tool 여부 확인
- Dynamic UX 요구사항 과다 여부 확인
- API Controller와 View Controller 분리 여부 확인

---

### [실무]

검수 Flow:

```text
Request Mapping 확인
→ Controller Annotation 확인
→ @ResponseBody 여부 확인
→ Model Attribute 확인
→ View Name 확인
→ Template Path 확인
→ Thymeleaf Attribute 확인
→ SSR 적용 적합성 확인
→ HTML Response 목적 확인
```

---

### [FAQ]

Q. SSR Controller 검수에서 가장 먼저 볼 것은?

A.
`@Controller` 사용 여부와 View Name 반환 여부이다.

Q. Template 검수에서 가장 중요한 것은?

A.
Model Attribute 이름과 Template Expression 이름이 일치하는지 확인하는 것이다.

Q. SSR 적용 여부는 어떻게 판단하는가?

A.
Admin Page, Backoffice, Form-heavy 화면이면 적합하다.
복잡한 Client Interaction 중심이면 React / REST API를 우선 검토한다.

Q. View Name 검수 핵심은?

A.
View Name과 실제 `templates` 하위 Template 경로가 일치하는지 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. SSR Thymeleaf 기본 흐름은?
A. Request → Controller → Model → View Name → Thymeleaf Template → HTML Response 흐름이다.

Q. Spring MVC SSR Flow는?
A. Browser Request → DispatcherServlet → @Controller → Model → View Resolver → Thymeleaf Render → HTML Response 흐름이다.

Q. Thymeleaf에서 Controller는 무엇을 반환하는가?
A. `@Controller`는 View Name을 반환하고 Thymeleaf Template을 렌더링한다.

Q. `@Controller`와 `@RestController` 차이는?
A. `@Controller`는 View Rendering, `@RestController`는 Response Body 반환에 사용한다.

Q. Thymeleaf View Controller는 어떤 Annotation을 사용하는가?
A. `@Controller`를 사용한다.

Q. `@RestController`로 Thymeleaf View를 반환하면 어떻게 되는가?
A. View Name이 아니라 문자열 Response Body로 반환된다.

Q. `@ResponseBody`가 있으면 View Rendering이 되는가?
A. 아니다. Response Body 반환이 된다.

Q. `users/list` 문자열이 그대로 출력되는 이유는?
A. `@RestController` 또는 `@ResponseBody`가 적용되었을 가능성이 높다.

Q. Thymeleaf View Name은 어디에 매핑되는가?
A. 기본적으로 `src/main/resources/templates` 하위 `.html` Template에 매핑된다.

Q. `return "users/list"`는 어떤 파일을 찾는가?
A. 기본 설정 기준 `templates/users/list.html`을 찾는다.

Q. View Name에 `.html`을 붙이는가?
A. 보통 붙이지 않는다.

Q. View Name 앞에 `/`를 붙이는가?
A. 일반적으로 붙이지 않는다.

Q. Template Not Found 원인은?
A. View Name과 실제 Template 경로가 불일치하거나 파일이 없기 때문이다.

Q. Thymeleaf에서 Model 데이터는 어떻게 접근하는가?
A. `${attributeName}` Variable Expression으로 접근한다.

Q. `model.addAttribute("user", user)`는 무엇인가?
A. `user`라는 이름으로 Template에 데이터를 전달하는 코드이다.

Q. `${user.name}`이 출력되지 않는 이유는?
A. Model에 `user` Attribute가 없거나 이름이 다를 수 있다.

Q. Entity를 Model에 직접 담아도 되는가?
A. 단순 Admin Page에서는 가능하지만 외부 노출 화면이나 복잡한 화면에서는 DTO를 권장한다.

Q. Thymeleaf에서 목록 반복은 어떻게 하는가?
A. `th:each`를 사용한다.

Q. Thymeleaf에서 텍스트 출력은 어떻게 하는가?
A. `th:text`를 사용한다.

Q. Thymeleaf에서 링크는 어떻게 생성하는가?
A. `th:href`와 `@{}` Link Expression을 사용한다.

Q. Thymeleaf에서 Path Variable 링크는 어떻게 작성하는가?
A. `@{/users/{id}(id=${user.id})}` 형태로 작성한다.

Q. Thymeleaf에서 Query Parameter 링크는 어떻게 작성하는가?
A. `@{/users(page=${page}, keyword=${keyword})}` 형태로 작성한다.

Q. Thymeleaf는 Browser에서 실행되는가?
A. 아니다. 서버에서 처리되고 Browser는 완성된 HTML을 받는다.

Q. `th:utext`를 조심해야 하는 이유는?
A. Escaping 없이 HTML을 출력하므로 XSS 위험이 있다.

Q. Template에 Business Logic을 넣어도 되는가?
A. 권장하지 않는다. Service에서 처리 후 Model로 전달하는 것이 좋다.

Q. SSR Thymeleaf가 적합한 화면은?
A. Admin Page, Backoffice, Internal Tool, Form-heavy CRUD 화면이다.

Q. React가 더 적합한 경우는?
A. Public SPA, 복잡한 Dynamic UX, Client State가 많은 화면이다.

Q. REST API와 SSR Thymeleaf 차이는?
A. SSR은 HTML을 반환하고 REST API는 JSON을 반환한다.

Q. SSR Controller와 API Controller는 분리하는가?
A. 실무에서는 책임 분리를 위해 분리 권장이다.

Q. Agent는 언제 Thymeleaf를 선택해야 하는가?
A. Admin Page, Backoffice, Form-heavy CRUD, 단순 검색 / 목록 / 상세 화면이면 Thymeleaf를 선택할 수 있다.

Q. Agent는 언제 REST API를 선택해야 하는가?
A. Mobile App, 외부 API, React Frontend, 복잡한 Dynamic UX가 필요하면 REST API를 선택한다.

Q. Admin 목록에서 `findAll()`을 사용해도 되는가?
A. 데이터가 적은 초기에는 가능하지만 실무에서는 Pagination을 권장한다.

Q. SSR Core 검수 핵심은?
A. `@Controller`, Model Attribute, View Name, Template Path, Thymeleaf Expression, SSR 적용 적합성을 확인하는 것이다.

Q. View Name 검수 핵심은?
A. View Name과 실제 `templates` 하위 Template 경로가 일치하는지 확인하는 것이다.
