# SSR Thymeleaf Part07 - Troubleshooting Best Practice

---

# 1. Troubleshooting Core

## 1.1 SSR Thymeleaf Troubleshooting Definition

### [개념]

SSR Thymeleaf Troubleshooting은 Spring MVC View Rendering, Thymeleaf Template, Form Binding, Validation, Static Resource, Security View 문제를 원인별로 추적하는 과정이다.

```text
Problem
→ Request Flow 확인
→ Controller 확인
→ Model Attribute 확인
→ View Name 확인
→ Template 확인
→ Security / Static Resource 확인
→ Root Cause 도출
```

---

### [핵심]

- SSR 문제는 Controller와 Template 사이의 연결 오류가 많다.
- View Name과 Template Path 불일치가 자주 발생한다.
- Model Attribute 이름 불일치가 자주 발생한다.
- Form Binding 오류는 `th:object`, `th:field`, `@ModelAttribute` 연결을 확인한다.
- Validation 오류는 `@Valid`, `BindingResult`, `th:errors` 흐름을 확인한다.
- Security 오류는 CSRF, Role, Session, Login 상태를 확인한다.
- Static Resource 오류는 `/static` URL 포함 여부를 확인한다.
- Error Page는 내부 정보 노출 여부를 확인한다.

---

### [실무]

기본 점검 순서:

```text
1. Browser Network 요청 URL 확인
2. Controller Mapping 도달 여부 확인
3. Controller Annotation 확인
4. Model Attribute 이름 확인
5. View Name 확인
6. Template Path 확인
7. Thymeleaf Expression 확인
8. Security Filter / CSRF 확인
9. Static Resource URL 확인
10. Server Log 확인
```

문제 분류:

```text
문자열이 그대로 출력됨
→ Controller Annotation 문제

Template Not Found
→ View Name / Template Path 문제

Model 값 출력 안 됨
→ Model Attribute 이름 문제

Form Binding 오류
→ th:object / th:field 문제

Validation Error 미표시
→ BindingResult / Redirect 문제

POST 403
→ CSRF Token 문제

CSS / JS 404
→ Static Resource Path 문제

권한 버튼은 숨겨졌지만 URL 접근 가능
→ Server Authorization 누락
```

---

### [FAQ]

Q. SSR Thymeleaf Troubleshooting의 핵심은?

A.
Request → Controller → Model → View Name → Template → HTML Response 흐름을 순서대로 확인하는 것이다.

Q. Thymeleaf 오류는 주로 어디에서 발생하는가?

A.
Controller와 Template 사이의 View Name, Model Attribute, Expression 불일치에서 자주 발생한다.

Q. 가장 먼저 확인할 것은?

A.
요청 URL이 올바른 Controller Mapping에 도달하는지 확인한다.

---

# 2. Template Not Found

## 2.1 Template Path Error

### [개념]

Template Not Found는 Controller가 반환한 View Name과 실제 Thymeleaf Template 파일 경로가 일치하지 않을 때 발생한다.

Spring Boot + Thymeleaf 기본 설정에서는 View Name이 `src/main/resources/templates` 하위 `.html` 파일과 매핑된다.

```text
return "admin/users/list"
→ templates/admin/users/list.html
```

---

### [핵심]

- View Name은 논리 경로이다.
- `.html` 확장자는 보통 반환하지 않는다.
- View Name 앞에 불필요한 `/`를 붙이지 않는다.
- Template 파일은 `resources/templates` 하위에 있어야 한다.
- 대소문자와 디렉터리 이름을 확인한다.
- Build 결과에 Template이 포함되었는지 확인한다.
- `templates`와 `static` 위치를 혼동하지 않는다.

---

### [실무]

올바른 Controller:

```java
@GetMapping("/admin/users")
public String list(Model model) {
    model.addAttribute("users", userService.findAll());
    return "admin/users/list";
}
```

올바른 파일 위치:

```text
src/main/resources/templates/admin/users/list.html
```

잘못된 예:

```java
return "/admin/users/list.html";
```

권장 예:

```java
return "admin/users/list";
```

점검 Flow:

```text
View Name 확인
→ templates 하위 경로 확인
→ 파일명 확인
→ 확장자 확인
→ 대소문자 확인
→ Build Resource 포함 여부 확인
```

---

### [FAQ]

Q. Template Not Found가 발생하는 이유는?

A.
Controller의 View Name과 실제 Template 파일 경로가 일치하지 않기 때문이다.

Q. View Name에 `.html`을 붙이는가?

A.
보통 붙이지 않는다. View Resolver가 `.html` suffix를 적용한다.

Q. Template 파일은 어디에 있어야 하는가?

A.
`src/main/resources/templates` 하위에 있어야 한다.

---

# 3. View Name Printed As Text

## 3.1 @RestController Mistake

### [개념]

View Name Printed As Text는 Controller가 View Name을 반환했지만 Template Rendering이 아니라 문자열 Response Body로 반환되는 문제이다.

가장 흔한 원인은 `@RestController` 사용이다.

```text
@RestController
→ return "admin/users/list"
→ Response Body: admin/users/list
```

---

### [핵심]

- Thymeleaf View Rendering에는 `@Controller`를 사용한다.
- `@RestController`는 `@ResponseBody`를 포함한다.
- `@ResponseBody`가 있으면 문자열이 View Name이 아니라 Body로 반환된다.
- SSR View Controller와 REST API Controller를 분리한다.
- `/admin/**` View Controller는 `@Controller`를 사용한다.
- JSON API는 `@RestController`를 사용한다.

---

### [실무]

잘못된 예:

```java
@RestController
@RequestMapping("/admin/users")
public class AdminUserController {

    @GetMapping
    public String list() {
        return "admin/users/list";
    }
}
```

결과:

```text
Browser Body
→ admin/users/list
```

올바른 예:

```java
@Controller
@RequestMapping("/admin/users")
public class AdminUserController {

    @GetMapping
    public String list(Model model) {
        model.addAttribute("users", userService.findAll());
        return "admin/users/list";
    }
}
```

분리 기준:

```text
SSR Page
→ @Controller

REST API
→ @RestController
```

---

### [FAQ]

Q. `admin/users/list` 문자열이 그대로 출력되는 이유는?

A.
`@RestController` 또는 `@ResponseBody`가 적용되어 View Name이 Response Body로 반환되었기 때문이다.

Q. Thymeleaf View Controller는 무엇을 사용해야 하는가?

A.
`@Controller`를 사용해야 한다.

Q. REST API Controller와 View Controller를 분리해야 하는가?

A.
분리 권장이다. View Rendering과 JSON 응답 책임이 다르기 때문이다.

---

# 4. Model Attribute Error

## 4.1 Attribute Name Mismatch

### [개념]

Model Attribute Error는 Controller에서 Model에 담은 이름과 Template에서 참조하는 이름이 다를 때 발생한다.

```text
Controller: model.addAttribute("user", user)
Template: ${member.name}
→ member Attribute 없음
```

---

### [핵심]

- Model Attribute 이름은 Template 변수명이다.
- Controller와 Template의 이름이 일치해야 한다.
- 목록은 복수형 이름을 권장한다.
- 단일 객체는 단수형 이름을 권장한다.
- Form Object는 `userForm`, `festivalForm`처럼 명확한 이름을 권장한다.
- Attribute 이름 변경 시 Template 전체 검색이 필요하다.
- Form Binding에서는 `th:object` 이름도 함께 확인한다.

---

### [실무]

잘못된 예:

```java
model.addAttribute("user", userResponse);
```

```html
<span th:text="${member.name}">name</span>
```

올바른 예:

```java
model.addAttribute("user", userResponse);
```

```html
<span th:text="${user.name}">name</span>
```

권장 Naming:

```text
users
→ 목록

user
→ 단일 상세

userForm
→ Form Object

searchForm
→ 검색 조건

page
→ Page 객체는 구체 이름 권장: users, festivals
```

---

### [FAQ]

Q. `${user.name}`이 출력되지 않는 이유는?

A.
Model에 `user` Attribute가 없거나 이름이 다를 수 있다.

Q. Model Attribute 이름은 무엇과 일치해야 하는가?

A.
Template의 `${...}` 또는 `th:object`에서 사용하는 이름과 일치해야 한다.

Q. 목록 Attribute 이름은 어떻게 짓는가?

A.
`users`, `festivals`, `orders`처럼 복수형을 권장한다.

---

# 5. Form Binding Error

## 5.1 th:object Missing

### [개념]

`th:object` Missing Error는 Form Binding 대상 객체가 Template에 없거나 `th:object` 선언이 누락되어 발생하는 오류이다.

`th:field="*{email}"`은 `th:object`로 지정된 객체가 있어야 안정적으로 동작한다.

```text
<form>
  <input th:field="*{email}">
</form>
→ Selection Object 없음
```

---

### [핵심]

- Form Binding에는 `th:object`가 필요하다.
- `th:object`는 Model Attribute를 참조한다.
- GET Form 화면에서 Form Object를 Model에 담아야 한다.
- `th:field="*{field}"`는 `th:object` 내부에서 사용한다.
- `th:object` 이름과 `@ModelAttribute` 이름을 통일한다.
- Form Object 이름과 DTO Field 이름을 함께 점검한다.

---

### [실무]

잘못된 예:

```java
@GetMapping("/admin/users/new")
public String createForm() {
    return "admin/users/create-form";
}
```

```html
<form th:object="${userForm}">
  <input th:field="*{email}" />
</form>
```

문제:

```text
Model에 userForm 없음
→ th:object 바인딩 실패
```

올바른 예:

```java
@GetMapping("/admin/users/new")
public String createForm(Model model) {
    model.addAttribute("userForm", new UserCreateForm());
    return "admin/users/create-form";
}
```

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <input th:field="*{email}" />
</form>
```

---

### [FAQ]

Q. `th:object` 오류가 발생하는 이유는?

A.
Form Object가 Model에 없거나 Template의 `th:object` 이름과 일치하지 않기 때문이다.

Q. GET Form Controller에서 반드시 해야 할 일은?

A.
빈 Form Object를 Model에 담아야 한다.

Q. `th:field="*{email}"`은 어디서 사용해야 하는가?

A.
`th:object`가 선언된 Form 내부에서 사용해야 한다.

---

## 5.2 Field Name Mismatch

### [개념]

Field Name Mismatch는 Form DTO Field 이름과 Template의 `th:field` 이름이 일치하지 않을 때 발생한다.

```text
UserCreateForm.email
Template th:field="*{userEmail}"
→ email Field Binding 실패
```

---

### [핵심]

- `th:field` 이름은 Form DTO Field와 일치해야 한다.
- `@ModelAttribute` Binding은 요청 Parameter 이름을 기준으로 Field를 채운다.
- `th:field`는 `name`, `id`, `value`를 자동 생성한다.
- Field 이름 변경 시 Template도 함께 수정한다.
- Nested Field는 DTO 구조와 일치해야 한다.
- Browser Network Payload에서 실제 parameter name을 확인한다.

---

### [실무]

Form DTO:

```java
public class UserCreateForm {

    private String email;
    private String name;
}
```

잘못된 Template:

```html
<input th:field="*{userEmail}" />
```

올바른 Template:

```html
<input th:field="*{email}" />
```

점검 Flow:

```text
Form DTO Field 확인
→ th:field 이름 확인
→ 렌더링된 name 속성 확인
→ POST Payload 확인
→ @ModelAttribute Binding 확인
```

---

### [FAQ]

Q. Form 값이 DTO에 들어오지 않는 이유는?

A.
Input name과 DTO Field 이름이 일치하지 않을 가능성이 높다.

Q. `th:field`는 어떤 이름을 기준으로 작성하는가?

A.
Form DTO Field 이름을 기준으로 작성한다.

Q. Binding 결과는 어디서 확인하는가?

A.
Controller Parameter, Debug Log, Browser Network Payload에서 확인할 수 있다.

---

# 6. Validation Error Not Displayed

## 6.1 BindingResult Order Error

### [개념]

BindingResult Order Error는 `BindingResult`가 `@Valid` 대상 Form Object 바로 뒤에 위치하지 않아 Validation Error를 처리하지 못하는 문제이다.

```java
public String create(
    @Valid @ModelAttribute("userForm") UserCreateForm userForm,
    Model model,
    BindingResult bindingResult
)
```

---

### [핵심]

- `BindingResult`는 `@Valid` 대상 바로 뒤에 있어야 한다.
- 위치가 틀리면 Validation Error를 Controller에서 처리하지 못할 수 있다.
- `bindingResult.hasErrors()`로 오류 여부를 확인한다.
- 오류가 있으면 같은 Form View를 반환한다.
- Redirect하면 Error 정보가 사라진다.
- `@Valid` 대상이 여러 개면 각각 바로 뒤에 BindingResult를 둔다.

---

### [실무]

잘못된 순서:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        Model model,
        BindingResult bindingResult
) {
    return "admin/users/create-form";
}
```

올바른 순서:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult,
        Model model
) {
    if (bindingResult.hasErrors()) {
        return "admin/users/create-form";
    }

    userService.create(userForm);
    return "redirect:/admin/users";
}
```

검수 기준:

```text
@Valid Form Object
→ 바로 다음 Parameter가 BindingResult인지 확인
```

---

### [FAQ]

Q. `BindingResult`는 어디에 위치해야 하는가?

A.
`@Valid`가 붙은 Form Object 바로 뒤에 위치해야 한다.

Q. Validation Error가 Controller에서 잡히지 않는 이유는?

A.
`BindingResult` 위치가 틀렸을 가능성이 있다.

Q. Validation Error 여부는 어떻게 확인하는가?

A.
`bindingResult.hasErrors()`를 사용한다.

---

## 6.2 Redirect On Validation Failure

### [개념]

Redirect On Validation Failure는 Validation 실패 시 같은 Form View를 반환하지 않고 Redirect하여 BindingResult와 입력값이 사라지는 문제이다.

```text
Validation Fail
→ redirect:/admin/users/new
→ BindingResult 소실
→ Error Message 미표시
```

---

### [핵심]

- Validation 실패 시 Redirect하지 않는다.
- 같은 Form View를 반환한다.
- `th:field`가 입력값을 유지한다.
- `th:errors`가 Error Message를 출력한다.
- Select Option 등 부가 Model Attribute를 다시 추가한다.
- 성공 시에만 Redirect한다.
- Flash Attribute로 Field Error를 전달하지 않는다.

---

### [실무]

잘못된 예:

```java
if (bindingResult.hasErrors()) {
    return "redirect:/admin/users/new";
}
```

올바른 예:

```java
if (bindingResult.hasErrors()) {
    model.addAttribute("roles", roleService.findAll());
    return "admin/users/create-form";
}
```

Flow:

```text
Validation Fail
→ Same Form View
→ BindingResult 유지
→ Input Value 유지
→ th:errors 출력

Validation Success
→ Redirect
→ PRG Pattern 적용
```

---

### [FAQ]

Q. Validation 실패 시 Redirect하면 안 되는 이유는?

A.
BindingResult와 입력값이 사라져 Error Message를 표시할 수 없기 때문이다.

Q. Validation 실패 시 무엇을 반환해야 하는가?

A.
사용자가 입력하던 같은 Form View를 반환해야 한다.

Q. Validation 성공 시에는 무엇을 반환하는가?

A.
PRG Pattern을 위해 Redirect를 반환한다.

---

# 7. Select Option Lost

## 7.1 Additional Model Attribute Missing

### [개념]

Select Option Lost는 Validation 실패 후 Form View를 다시 반환할 때 Select Option 목록 같은 부가 Model Attribute를 다시 담지 않아 발생한다.

```text
GET Form
→ roles Model 있음
→ Submit Validation Fail
→ return Form View
→ roles Model 없음
→ Select Option 사라짐
```

---

### [핵심]

- Select Option 목록은 Form Object와 별도 Model Attribute이다.
- Validation 실패 시 Option 목록을 다시 Model에 담아야 한다.
- Category, Role, Region, Status 목록에서 자주 발생한다.
- 공통 메서드로 Option Model 추가를 분리하는 것이 좋다.
- Create Form과 Update Form 모두 동일하게 적용한다.
- Checkbox / Radio 목록도 같은 방식으로 재등록한다.

---

### [실무]

잘못된 예:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult
) {
    if (bindingResult.hasErrors()) {
        return "admin/users/create-form";
    }

    userService.create(userForm);
    return "redirect:/admin/users";
}
```

올바른 예:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult,
        Model model
) {
    if (bindingResult.hasErrors()) {
        addUserFormOptions(model);
        return "admin/users/create-form";
    }

    userService.create(userForm);
    return "redirect:/admin/users";
}

private void addUserFormOptions(Model model) {
    model.addAttribute("roles", roleService.findAll());
    model.addAttribute("statuses", statusService.findAll());
}
```

Template:

```html
<select th:field="*{role}">
  <option value="">권한 선택</option>
  <option
    th:each="role : ${roles}"
    th:value="${role.code}"
    th:text="${role.name}"
  >
    role
  </option>
</select>
```

---

### [FAQ]

Q. Validation 실패 후 Select Option이 사라지는 이유는?

A.
Option 목록 Model Attribute를 다시 추가하지 않았기 때문이다.

Q. Select Option 목록은 어디서 전달하는가?

A.
Controller에서 Model Attribute로 전달한다.

Q. Option 목록 재등록은 어떻게 관리하는가?

A.
`addFormOptions(model)` 같은 공통 메서드로 분리하는 것이 좋다.

---

# 8. CSRF 403

## 8.1 POST Forbidden

### [개념]

CSRF 403은 Spring Security CSRF 보호가 활성화된 상태에서 POST, PUT, DELETE 같은 상태 변경 요청에 유효한 CSRF Token이 없을 때 발생한다.

SSR Thymeleaf Form에서는 Hidden Input으로 CSRF Token을 포함해야 한다.

```text
POST Form
→ CSRF Token 누락
→ Spring Security CSRF Filter
→ 403 Forbidden
```

---

### [핵심]

- 상태 변경 Form에는 CSRF Token이 필요하다.
- Create, Update, Delete, Logout Form에서 자주 발생한다.
- CSRF Token은 Hidden Input으로 전달한다.
- `_csrf.parameterName`과 `_csrf.token`을 사용한다.
- GET 요청으로 상태 변경을 처리하지 않는다.
- AJAX 요청은 CSRF Header 설정이 필요하다.
- 공통 CSRF Fragment를 사용할 수 있다.

---

### [실무]

CSRF Hidden Input:

```html
<input
  type="hidden"
  th:name="${_csrf.parameterName}"
  th:value="${_csrf.token}"
/>
```

Create Form:

```html
<form th:action="@{/admin/users}" method="post">
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />
  <button type="submit">저장</button>
</form>
```

Delete Form:

```html
<form th:action="@{/admin/users/{id}/delete(id=${user.id})}" method="post">
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />
  <button type="submit">삭제</button>
</form>
```

점검 Flow:

```text
403 발생
→ 요청 Method 확인
→ CSRF 활성화 여부 확인
→ Hidden Input 렌더링 확인
→ Payload에 CSRF 값 포함 여부 확인
→ Security Log 확인
```

---

### [FAQ]

Q. POST 요청에서 403이 발생하는 이유는?

A.
CSRF Token이 누락되었거나 잘못되었을 가능성이 높다.

Q. CSRF Token은 어떻게 Form에 넣는가?

A.
`th:name="${_csrf.parameterName}"`, `th:value="${_csrf.token}"` Hidden Input을 추가한다.

Q. Delete 요청에도 CSRF Token이 필요한가?

A.
필요하다. Delete는 상태 변경 요청이기 때문이다.

---

# 9. Static Resource 404

## 9.1 CSS JS Image Not Found

### [개념]

Static Resource 404는 CSS, JavaScript, Image 파일 경로가 Spring Boot Static Resource Mapping과 일치하지 않을 때 발생한다.

Spring Boot 기본 설정에서 `resources/static` 하위 파일은 URL Root 기준으로 제공된다.

```text
src/main/resources/static/css/admin.css
→ /css/admin.css
```

---

### [핵심]

- Static Resource는 `src/main/resources/static` 하위에 둔다.
- URL에는 `/static`을 포함하지 않는다.
- CSS는 `th:href`로 연결한다.
- JS와 Image는 `th:src`로 연결한다.
- Link Expression `@{}`를 사용한다.
- Browser Network에서 실제 요청 URL을 확인한다.
- Browser Cache 문제와 404 문제를 구분한다.

---

### [실무]

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

점검 Flow:

```text
Resource 404
→ 파일 위치 확인
→ URL에 /static 포함 여부 확인
→ th:href / th:src 확인
→ Browser Network 요청 URL 확인
→ Build Resource 포함 여부 확인
```

---

### [FAQ]

Q. CSS 404가 발생하는 이유는?

A.
파일 위치가 잘못되었거나 URL에 `/static`을 포함했을 가능성이 있다.

Q. Spring Boot Static Resource URL에 `/static`을 붙이는가?

A.
보통 붙이지 않는다. `static/css/admin.css`는 `/css/admin.css`로 접근한다.

Q. Thymeleaf에서 JS 파일은 어떻게 연결하는가?

A.
`<script th:src="@{/js/admin.js}"></script>` 형태로 연결한다.

---

# 10. Fragment Not Found

## 10.1 Fragment Path Name Error

### [개념]

Fragment Not Found는 `th:replace`, `th:insert`에서 참조한 Fragment Path 또는 Fragment Name이 실제 Template과 일치하지 않을 때 발생한다.

```text
~{fragments/header :: header}
→ templates/fragments/header.html
→ th:fragment="header"
```

---

### [핵심]

- Fragment Expression은 `~{templatePath :: fragmentName}` 형식이다.
- Template Path는 `templates` 하위 기준이다.
- `.html` 확장자는 보통 작성하지 않는다.
- Fragment Name은 `th:fragment` 값과 일치해야 한다.
- Path 앞에 불필요한 `/`를 붙이지 않는다.
- Parameterized Fragment는 Parameter 개수도 확인한다.
- Fragment 파일 위치와 이름을 함께 점검한다.

---

### [실무]

Fragment 파일:

```html
<!-- templates/fragments/header.html -->
<header th:fragment="header">
  <nav>Header</nav>
</header>
```

올바른 참조:

```html
<header th:replace="~{fragments/header :: header}"></header>
```

잘못된 참조:

```html
<header th:replace="~{/fragments/header.html :: adminHeader}"></header>
```

점검 Flow:

```text
Fragment Expression 확인
→ Template Path 확인
→ 실제 파일 위치 확인
→ th:fragment 이름 확인
→ Parameter 개수 확인
```

---

### [FAQ]

Q. Fragment Not Found가 발생하는 이유는?

A.
Fragment Template Path 또는 `th:fragment` 이름이 실제 파일과 일치하지 않기 때문이다.

Q. Fragment 참조에 `.html`을 붙이는가?

A.
보통 붙이지 않는다.

Q. Fragment 이름은 무엇과 일치해야 하는가?

A.
참조한 `fragmentName`과 실제 `th:fragment` 이름이 일치해야 한다.

---

# 11. Pagination Condition Lost

## 11.1 Search Query Parameter Missing

### [개념]

Pagination Condition Lost는 검색 결과에서 다음 페이지로 이동할 때 기존 검색 조건 Query Parameter가 Page Link에 포함되지 않아 검색 상태가 사라지는 문제이다.

```text
/admin/users?keyword=kim&role=ADMIN&page=0
→ 다음 클릭
→ /admin/users?page=1
→ 검색 조건 소실
```

---

### [핵심]

- Pagination Link에 검색 조건을 유지해야 한다.
- `keyword`, `status`, `category`, `role` 같은 조건을 Query Parameter에 포함한다.
- Search Form Object를 Model에 유지한다.
- Query Parameter에 민감 정보는 포함하지 않는다.
- Page Number는 내부적으로 0부터 시작한다.
- 화면에는 `page.number + 1`을 표시한다.

---

### [실무]

잘못된 Pagination:

```html
<a th:href="@{/admin/users(page=${users.number + 1})}"> 다음 </a>
```

올바른 Pagination:

```html
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

점검 Flow:

```text
Search Form Field 확인
→ Controller searchForm Model 확인
→ Pagination Link Query Parameter 확인
→ Browser URL 확인
→ 다음 Page 결과 확인
```

---

### [FAQ]

Q. Pagination에서 검색 조건이 사라지는 이유는?

A.
Page Link에 기존 검색 조건 Query Parameter를 포함하지 않았기 때문이다.

Q. 검색 조건은 어디에 유지하는가?

A.
Pagination Link의 Query Parameter에 유지한다.

Q. Query Parameter에 민감 정보를 넣어도 되는가?

A.
안 된다. URL에 노출되기 때문이다.

---

# 12. Login Logout Troubleshooting

## 12.1 Login Page Error

### [개념]

Login Page Error는 Spring Security Login 설정과 Thymeleaf Login Form의 Action, Parameter Name, CSRF 설정이 일치하지 않을 때 발생한다.

```text
GET /login
→ Login Page Render

POST /login
→ Spring Security Authentication Filter
→ Success or Failure
```

---

### [핵심]

- Login Page URL과 `loginPage()` 설정이 일치해야 한다.
- Login Form Action과 `loginProcessingUrl()`이 일치해야 한다.
- 기본 username parameter는 `username`이다.
- 기본 password parameter는 `password`이다.
- CSRF 활성화 시 Login POST에도 CSRF Token이 필요하다.
- 로그인 실패 URL과 Template의 Error 표시 조건을 맞춘다.
- Custom Parameter를 사용하면 Security 설정과 Form name을 함께 변경한다.

---

### [실무]

Security 설정:

```java
.formLogin(form -> form
    .loginPage("/login")
    .loginProcessingUrl("/login")
    .failureUrl("/login?error")
    .defaultSuccessUrl("/", true)
    .permitAll()
)
```

Login Form:

```html
<form th:action="@{/login}" method="post">
  <input type="text" name="username" />
  <input type="password" name="password" />

  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />

  <button type="submit">로그인</button>
</form>

<p th:if="${param.error}">로그인 정보가 올바르지 않습니다.</p>
```

점검 Flow:

```text
loginPage URL 확인
→ loginProcessingUrl 확인
→ Form action 확인
→ username/password name 확인
→ CSRF Token 확인
→ failureUrl 확인
```

---

### [FAQ]

Q. Login Form 제출이 처리되지 않는 이유는?

A.
Form Action이 `loginProcessingUrl()`과 일치하지 않을 수 있다.

Q. Spring Security 기본 로그인 파라미터 이름은?

A.
`username`, `password`이다.

Q. Login POST에도 CSRF Token이 필요한가?

A.
CSRF가 활성화되어 있으면 필요하다.

---

## 12.2 Logout Error

### [개념]

Logout Error는 Logout URL, Method, CSRF Token, Spring Security Logout 설정이 일치하지 않을 때 발생한다.

CSRF가 활성화된 경우 Logout은 POST Form으로 처리하는 것이 일반적이다.

```text
POST /logout
→ Logout Filter
→ Session Invalidate
→ SecurityContext Clear
→ Redirect
```

---

### [핵심]

- Logout URL과 `logoutUrl()` 설정이 일치해야 한다.
- CSRF 활성화 시 POST Logout Form을 사용한다.
- Logout Form에는 CSRF Token이 필요하다.
- Logout 성공 후 Redirect URL을 확인한다.
- GET Link Logout은 권장하지 않는다.
- Logout 후 Session과 SecurityContext가 정리되는지 확인한다.

---

### [실무]

Security 설정:

```java
.logout(logout -> logout
    .logoutUrl("/logout")
    .logoutSuccessUrl("/login?logout")
    .invalidateHttpSession(true)
    .clearAuthentication(true)
)
```

Logout Form:

```html
<form th:action="@{/logout}" method="post">
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />
  <button type="submit">로그아웃</button>
</form>
```

점검 Flow:

```text
Logout URL 확인
→ Form method 확인
→ CSRF Token 확인
→ logoutSuccessUrl 확인
→ Session invalidate 확인
```

---

### [FAQ]

Q. Logout에서 403이 발생하는 이유는?

A.
CSRF Token이 누락되었거나 GET Link로 Logout을 호출했을 수 있다.

Q. Logout은 GET Link로 처리해도 되는가?

A.
권장하지 않는다. CSRF 보호 관점에서 POST Form을 권장한다.

Q. Logout 후 무엇이 정리되는가?

A.
Session과 SecurityContext가 정리된다.

---

# 13. Error Page Troubleshooting

## 13.1 Error Page Information Exposure

### [개념]

Error Page Information Exposure는 404, 403, 500 화면에 Stack Trace, SQL Error, 내부 클래스명, 서버 경로 같은 민감한 구현 정보가 노출되는 문제이다.

```text
Exception 발생
→ Error Page
→ Stack Trace 출력
→ 내부 정보 노출
```

---

### [핵심]

- Error Page는 사용자 안내 중심이어야 한다.
- Stack Trace를 출력하지 않는다.
- Raw Exception Message를 그대로 출력하지 않는다.
- SQL Error를 출력하지 않는다.
- Server File Path를 출력하지 않는다.
- Security Rule 상세를 출력하지 않는다.
- 상세 원인은 Server Log와 Monitoring에서 확인한다.
- Admin Page라도 내부 정보를 화면에 노출하지 않는다.

---

### [실무]

비권장 Template:

```html
<pre th:text="${trace}">stack trace</pre>
<p th:text="${exception}">exception</p>
<p th:text="${message}">raw error message</p>
```

권장 Template:

```html
<h1>일시적인 오류가 발생했습니다.</h1>
<p>잠시 후 다시 시도해 주세요.</p>
<a th:href="@{/}">홈으로 이동</a>
```

운영 분리:

```text
User Error Page
→ 일반 안내 메시지

Server Log
→ Exception Detail

Monitoring
→ Alert / Trace / Metric
```

---

### [FAQ]

Q. Error Page에 Stack Trace를 보여줘도 되는가?

A.
안 된다. 내부 정보 노출 위험이 있다.

Q. Raw Exception Message를 사용자에게 보여줘도 되는가?

A.
권장하지 않는다. SQL, 경로, 내부 구조가 노출될 수 있다.

Q. 오류 상세 원인은 어디서 확인하는가?

A.
Server Log와 Monitoring 도구에서 확인한다.

---

# 14. Best Practice Core

## 14.1 SSR Thymeleaf Best Practice

### [개념]

SSR Thymeleaf Best Practice는 View Rendering, Form Binding, Validation, Security, Layout, Admin Page 구현을 일관된 구조로 유지하기 위한 기준이다.

```text
Consistent URL
→ View Controller
→ Form DTO
→ Model Attribute Naming
→ Template Path
→ Validation Flow
→ Security Rule
→ Review Checklist
```

---

### [핵심]

- SSR View Controller는 `@Controller`로 작성한다.
- API Controller와 View Controller를 분리한다.
- View Name과 Template Path를 일관되게 유지한다.
- Form Binding에는 Form DTO를 사용한다.
- Validation 실패 시 같은 View를 반환한다.
- POST 성공 시 Redirect한다.
- Delete는 POST Form으로 처리한다.
- 상태 변경 Form에는 CSRF Token을 포함한다.
- Static Resource는 `@{}` Link Expression으로 연결한다.
- Error Page에는 내부 정보를 노출하지 않는다.
- Template에는 Business Logic을 과도하게 넣지 않는다.

---

### [실무]

권장 Project Structure:

```text
controller/
├ AdminUserController
├ AdminFestivalController
└ AuthViewController

dto/
├ form/
│  ├ UserCreateForm
│  ├ UserUpdateForm
│  └ UserSearchForm
└ response/
   ├ UserAdminResponse
   └ UserAdminDetailResponse

templates/
├ admin/
│  ├ users/
│  │  ├ list.html
│  │  ├ detail.html
│  │  ├ create-form.html
│  │  └ update-form.html
├ auth/
│  └ login.html
├ fragments/
│  ├ header.html
│  ├ sidebar.html
│  ├ pagination.html
│  ├ alert.html
│  └ security.html
└ error/
   ├ 403.html
   ├ 404.html
   └ 500.html

static/
├ css/
├ js/
└ images/
```

---

### [FAQ]

Q. SSR Thymeleaf Best Practice 핵심은?

A.
`@Controller`, View Name, Form DTO, Validation Same View, POST Redirect, CSRF, Error Page 보안을 일관되게 유지하는 것이다.

Q. View Controller와 API Controller는 분리하는가?

A.
분리 권장이다. HTML 렌더링과 JSON 응답은 책임이 다르다.

Q. 상태 변경 요청은 어떻게 처리하는가?

A.
POST Form과 CSRF Token을 사용하고 성공 후 Redirect한다.

---

# 15. Naming Best Practice

## 15.1 Consistent Naming

### [개념]

Consistent Naming은 Controller, Model Attribute, Form DTO, Template Path, Fragment Name의 이름을 일관되게 유지하는 규칙이다.

RAG Retrieval과 Agent Code Generation 품질을 높이기 위해 Naming은 명확해야 한다.

---

### [핵심]

- View Controller 이름은 `AdminUserController`처럼 작성한다.
- Form DTO는 `UserCreateForm`, `UserUpdateForm`, `UserSearchForm`처럼 작성한다.
- Response DTO는 `UserAdminResponse`, `UserAdminDetailResponse`처럼 작성한다.
- Model Attribute는 Template 역할 기준으로 작성한다.
- Template 파일명은 화면 목적 기준으로 작성한다.
- Fragment Name은 UI 역할 기준으로 작성한다.
- Controller Method 이름은 화면 흐름 기준으로 작성한다.

---

### [실무]

권장 Naming Table:

| Target                 | Naming Example                                     |
| ---------------------- | -------------------------------------------------- |
| View Controller        | `AdminUserController`                              |
| API Controller         | `UserApiController`                                |
| Create Form DTO        | `UserCreateForm`                                   |
| Update Form DTO        | `UserUpdateForm`                                   |
| Search Form DTO        | `UserSearchForm`                                   |
| List Response DTO      | `UserAdminResponse`                                |
| Detail Response DTO    | `UserAdminDetailResponse`                          |
| Single Model Attribute | `user`                                             |
| List Model Attribute   | `users`                                            |
| Form Model Attribute   | `userForm`                                         |
| Search Model Attribute | `searchForm`                                       |
| Template List          | `admin/users/list`                                 |
| Template Detail        | `admin/users/detail`                               |
| Template Create        | `admin/users/create-form`                          |
| Template Update        | `admin/users/update-form`                          |
| Fragment               | `header`, `sidebar`, `pagination`, `alert`, `csrf` |

---

### [FAQ]

Q. Form DTO 이름은 어떻게 짓는가?

A.
`UserCreateForm`, `UserUpdateForm`, `UserSearchForm`처럼 화면 목적 기준으로 짓는다.

Q. Model Attribute 이름은 어떻게 짓는가?

A.
단일 객체는 `user`, 목록은 `users`, Form은 `userForm`, 검색 조건은 `searchForm`처럼 짓는다.

Q. Template 파일명은 어떻게 짓는가?

A.
`list.html`, `detail.html`, `create-form.html`, `update-form.html`처럼 화면 목적 기준으로 짓는다.

---

# 16. Security Best Practice

## 16.1 SSR Security Checklist

### [개념]

SSR Security Best Practice는 Thymeleaf 화면에서 인증, 권한, CSRF, XSS, Error 정보 노출을 방지하기 위한 기준이다.

```text
Authentication
→ Authorization
→ CSRF
→ Output Escaping
→ Error Page Protection
```

---

### [핵심]

- 관리자 URL은 `/admin/**` Security Rule로 보호한다.
- `sec:authorize`는 UI 표시 제어로만 사용한다.
- 실제 권한 검증은 Security Layer와 Service에서 수행한다.
- 사용자 입력값 출력에는 `th:text`를 사용한다.
- `th:utext`는 제한적으로 사용한다.
- 상태 변경 Form에는 CSRF Token을 포함한다.
- Delete는 GET Link가 아니라 POST Form으로 처리한다.
- Error Page에 Stack Trace를 출력하지 않는다.
- Session에는 최소 정보만 저장한다.
- Query Parameter에 민감 정보를 넣지 않는다.

---

### [실무]

Security Rule:

```java
http.authorizeHttpRequests(auth -> auth
    .requestMatchers("/admin/**").hasRole("ADMIN")
    .anyRequest().permitAll()
);
```

CSRF Token:

```html
<input
  type="hidden"
  th:name="${_csrf.parameterName}"
  th:value="${_csrf.token}"
/>
```

Safe Output:

```html
<p th:text="${userInput}">safe text</p>
```

Dangerous Output:

```html
<div th:utext="${userInput}">unsafe html</div>
```

권한 분리:

```text
sec:authorize
→ 버튼 / 메뉴 표시 제어

SecurityFilterChain
→ URL 접근 제어

Service Permission Check
→ 도메인 권한 검증
```

---

### [FAQ]

Q. SSR Thymeleaf 보안 핵심은?

A.
Server Authorization, CSRF Token, `th:text`, Error Page 정보 보호, Session 최소화이다.

Q. `sec:authorize`만으로 보안이 완료되는가?

A.
아니다. 실제 접근 제어는 서버 Security Rule과 Service 검증으로 처리해야 한다.

Q. 사용자 입력값 출력에는 무엇을 사용하는가?

A.
기본적으로 `th:text`를 사용한다.

---

# 17. Performance Best Practice

## 17.1 SSR Performance

### [개념]

SSR Performance Best Practice는 서버에서 HTML을 생성하는 SSR 구조에서 Query, Pagination, Static Resource, Template 중복을 최적화하는 기준이다.

```text
Request
→ Query Optimization
→ DTO Projection
→ Pagination
→ Template Rendering
→ Static Resource Cache
```

---

### [핵심]

- Admin 목록은 Pagination을 적용한다.
- 대량 데이터 전체 조회를 피한다.
- N+1 Query를 주의한다.
- View 전용 DTO를 사용한다.
- Dashboard 통계는 캐싱 또는 집계 테이블을 검토한다.
- Static Resource는 Cache 전략을 적용한다.
- Fragment 중복을 줄인다.
- Template에 복잡한 Business Logic을 넣지 않는다.
- 이미지, CSS, JS 404가 많으면 Rendering 체감 성능이 나빠진다.

---

### [실무]

비권장:

```java
@GetMapping("/admin/users")
public String list(Model model) {
    model.addAttribute("users", userRepository.findAll());
    return "admin/users/list";
}
```

권장:

```java
@GetMapping("/admin/users")
public String list(Pageable pageable, Model model) {
    Page<UserAdminResponse> users = userService.search(pageable);
    model.addAttribute("users", users);
    return "admin/users/list";
}
```

성능 점검:

```text
List Page 느림
→ Pagination 적용 여부 확인
→ Query Count 확인
→ N+1 확인
→ DTO Projection 확인
→ Index 확인

Dashboard 느림
→ 실시간 Count 과다 확인
→ Cache 적용 검토
→ 집계 테이블 검토
```

---

### [FAQ]

Q. Admin 목록에서 `findAll()`을 사용해도 되는가?

A.
데이터가 적은 초기에는 가능하지만, 실무에서는 Pagination을 권장한다.

Q. Dashboard가 느리면 어떻게 하는가?

A.
캐싱, 집계 테이블, Query 최적화를 검토한다.

Q. Template에 Business Logic을 넣어도 되는가?

A.
권장하지 않는다. Service에서 처리 후 Model로 전달하는 것이 좋다.

---

# 18. Agent Review Checklist

## 18.1 Final SSR Thymeleaf Review Checklist

### [개념]

Agent Review Checklist는 SSR Thymeleaf 문서와 코드를 검수할 때 사용하는 최종 기준이다.

RAG Agent는 이 Checklist를 기준으로 코드 생성, 코드 리뷰, 오류 탐지, 개선 제안을 수행한다.

---

### [핵심]

Controller 검수:

- `@Controller` 사용 여부
- `@RestController` 오사용 여부
- View Name 반환 여부
- View Name과 Template Path 일치 여부
- API Controller와 View Controller 분리 여부
- POST 성공 후 Redirect 여부
- Validation 실패 후 Same View 반환 여부

Model 검수:

- Model Attribute 이름 일치 여부
- Form Object Model 등록 여부
- Select Option Model 재등록 여부
- Search Form Model 유지 여부
- DTO 사용 여부
- Entity 직접 노출 위험 여부

Template 검수:

- `xmlns:th` 선언 여부
- `th:object` 존재 여부
- `th:field` Field 이름 일치 여부
- `th:text` 사용 여부
- `th:utext` 위험성 확인
- `th:href`, `th:src`, `@{}` 사용 여부
- Fragment Path와 Name 일치 여부
- Static Resource URL에 `/static` 포함 여부

Validation 검수:

- `@Valid` 사용 여부
- `BindingResult` 위치 적절성
- `bindingResult.hasErrors()` 처리 여부
- `th:errors` 출력 여부
- `#fields.hasErrors()` 사용 적절성
- Business Validation Error 처리 여부

Security 검수:

- `/admin/**` Security Rule 적용 여부
- CSRF Token 포함 여부
- Delete POST Form 사용 여부
- Logout POST Form 사용 여부
- `sec:authorize`는 UI 제어로만 사용 여부
- Server Authorization 존재 여부
- Error Page 정보 노출 여부
- Session 최소화 여부

Pagination 검수:

- Page / Slice 선택 적절성
- Page Link 검색 조건 유지 여부
- Page Number 표시 보정 여부
- Query Parameter 민감 정보 포함 여부

Troubleshooting 검수:

```text
문자열 출력
→ @RestController 확인

Template Not Found
→ View Name / Path 확인

Binding Error
→ th:object / Model Attribute 확인

Validation Error 미표시
→ BindingResult / Redirect 확인

POST 403
→ CSRF Token 확인

Static 404
→ /static URL 포함 여부 확인

Fragment Not Found
→ Fragment Path / Name 확인

Pagination 조건 소실
→ Query Parameter 유지 확인
```

---

### [실무]

최종 검수 Flow:

```text
Request URL 확인
→ Security Rule 확인
→ Controller Annotation 확인
→ View Name 확인
→ Template Path 확인
→ Model Attribute 확인
→ Template Expression 확인
→ Form Binding 확인
→ Validation Flow 확인
→ Redirect / PRG 확인
→ CSRF 확인
→ Static Resource 확인
→ Error Page 확인
```

---

### [FAQ]

Q. SSR Thymeleaf 최종 검수에서 가장 중요한 것은?

A.
Controller, Model, View Name, Template, Form Binding, Validation, Security 흐름이 일관되는지 확인하는 것이다.

Q. 코드 리뷰에서 가장 흔히 잡아야 할 오류는?

A.
`@RestController` 오사용, Model Attribute 불일치, Validation 실패 Redirect, CSRF Token 누락이다.

Q. Agent가 SSR Thymeleaf 코드를 생성할 때 따라야 할 기준은?

A.
`@Controller`, Form DTO, `th:object`, `th:field`, `BindingResult`, Same View, Redirect, CSRF, Template Path 일치를 기준으로 생성한다.

---

# Retrieval Queries

### [FAQ]

Q. SSR Thymeleaf Troubleshooting 기본 흐름은?
A. Request → Controller → Model → View Name → Template → Security / Static Resource 순서로 확인한다.

Q. Template Not Found 원인은?
A. View Name과 실제 `templates` 하위 HTML 파일 경로가 일치하지 않기 때문이다.

Q. View Name에 `.html`을 붙이는가?
A. 보통 붙이지 않는다.

Q. `admin/users/list` 문자열이 그대로 출력되는 이유는?
A. `@RestController` 또는 `@ResponseBody`가 적용되어 View Name이 Response Body로 반환되었기 때문이다.

Q. Thymeleaf View Controller는 어떤 Annotation을 사용하는가?
A. `@Controller`를 사용한다.

Q. Model Attribute 이름 오류는 어떻게 확인하는가?
A. Controller의 `model.addAttribute()` 이름과 Template의 `${...}` 이름이 일치하는지 확인한다.

Q. `${user.name}`이 출력되지 않는 이유는?
A. Model에 `user` Attribute가 없거나 이름이 다를 수 있다.

Q. `th:object` 오류가 발생하는 이유는?
A. Form Object가 Model에 없거나 `th:object` 이름이 일치하지 않기 때문이다.

Q. GET Form Controller에서 반드시 해야 할 일은?
A. 빈 Form Object를 Model에 담아야 한다.

Q. Form 값이 DTO에 들어오지 않는 이유는?
A. Input name과 DTO Field 이름이 일치하지 않을 가능성이 높다.

Q. `th:field`는 어떤 이름을 기준으로 작성하는가?
A. Form DTO Field 이름을 기준으로 작성한다.

Q. `BindingResult`는 어디에 위치해야 하는가?
A. `@Valid` 대상 Form Object 바로 뒤에 위치해야 한다.

Q. Validation Error가 화면에 안 보이는 이유는?
A. Redirect 사용, BindingResult 위치 오류, `th:errors` Field 이름 불일치가 원인일 수 있다.

Q. Validation 실패 시 Redirect하면 안 되는 이유는?
A. BindingResult와 입력값이 사라져 Error Message를 표시할 수 없기 때문이다.

Q. Validation 실패 시 무엇을 반환하는가?
A. 같은 Form View를 반환한다.

Q. Validation 성공 시 무엇을 반환하는가?
A. Redirect를 반환해 PRG Pattern을 적용한다.

Q. Validation 실패 후 Select Option이 사라지는 이유는?
A. Option 목록 Model Attribute를 다시 추가하지 않았기 때문이다.

Q. POST 요청에서 403이 발생하는 이유는?
A. CSRF Token이 누락되었거나 잘못되었을 가능성이 높다.

Q. CSRF Hidden Input은 어떻게 작성하는가?
A. `th:name="${_csrf.parameterName}"`, `th:value="${_csrf.token}"` 형태로 작성한다.

Q. Static Resource 404 원인은?
A. 파일 위치가 틀렸거나 URL에 `/static`을 포함했을 가능성이 있다.

Q. Spring Boot Static Resource URL에 `/static`을 붙이는가?
A. 보통 붙이지 않는다.

Q. Thymeleaf에서 CSS는 어떻게 연결하는가?
A. `th:href="@{/css/file.css}"` 형식으로 연결한다.

Q. Thymeleaf에서 JS는 어떻게 연결하는가?
A. `th:src="@{/js/file.js}"` 형식으로 연결한다.

Q. Fragment Not Found 원인은?
A. Fragment Template Path 또는 `th:fragment` 이름이 실제 파일과 일치하지 않기 때문이다.

Q. Fragment Expression 형식은?
A. `~{templatePath :: fragmentName}` 형식이다.

Q. Fragment 참조에 `.html`을 붙이는가?
A. 보통 붙이지 않는다.

Q. Pagination에서 검색 조건이 사라지는 이유는?
A. Page Link에 기존 검색 조건 Query Parameter를 포함하지 않았기 때문이다.

Q. Login Form 제출이 처리되지 않는 이유는?
A. Form Action이 Spring Security `loginProcessingUrl()`과 일치하지 않을 수 있다.

Q. Spring Security 기본 로그인 파라미터 이름은?
A. `username`, `password`이다.

Q. Logout에서 403이 발생하는 이유는?
A. CSRF Token이 누락되었거나 GET Link로 Logout을 호출했을 수 있다.

Q. Logout은 어떤 Method를 권장하는가?
A. CSRF 보호 관점에서 POST Form을 권장한다.

Q. Error Page에 Stack Trace를 보여줘도 되는가?
A. 안 된다. 내부 정보 노출 위험이 있다.

Q. Raw Exception Message를 사용자에게 보여줘도 되는가?
A. 권장하지 않는다. SQL, 경로, 내부 구조가 노출될 수 있다.

Q. SSR Thymeleaf Best Practice 핵심은?
A. `@Controller`, View Name, Form DTO, Validation Same View, POST Redirect, CSRF, Error Page 보안을 일관되게 유지하는 것이다.

Q. View Controller와 API Controller는 분리하는가?
A. 분리 권장이다. HTML 렌더링과 JSON 응답은 책임이 다르다.

Q. Form DTO 이름은 어떻게 짓는가?
A. `UserCreateForm`, `UserUpdateForm`, `UserSearchForm`처럼 화면 목적 기준으로 짓는다.

Q. Model Attribute 이름은 어떻게 짓는가?
A. 단일 객체는 `user`, 목록은 `users`, Form은 `userForm`, 검색 조건은 `searchForm`처럼 짓는다.

Q. SSR Thymeleaf 보안 핵심은?
A. Server Authorization, CSRF Token, `th:text`, Error Page 정보 보호, Session 최소화이다.

Q. `sec:authorize`만으로 보안이 완료되는가?
A. 아니다. 실제 접근 제어는 서버 Security Rule과 Service 검증으로 처리해야 한다.

Q. 사용자 입력값 출력에는 무엇을 사용하는가?
A. 기본적으로 `th:text`를 사용한다.

Q. Admin 목록에서 `findAll()`을 사용해도 되는가?
A. 데이터가 적은 초기에는 가능하지만 실무에서는 Pagination을 권장한다.

Q. Dashboard가 느리면 어떻게 하는가?
A. 캐싱, 집계 테이블, Query 최적화를 검토한다.

Q. Template에 Business Logic을 넣어도 되는가?
A. 권장하지 않는다. Service에서 처리 후 Model로 전달하는 것이 좋다.

Q. SSR Thymeleaf 최종 검수 기준은?
A. Controller, Model, View Name, Template, Form Binding, Validation, Security 흐름이 일관되는지 확인하는 것이다.

Q. SSR Thymeleaf 코드 리뷰에서 가장 흔한 오류는?
A. `@RestController` 오사용, Model Attribute 불일치, Validation 실패 Redirect, CSRF Token 누락이다.
