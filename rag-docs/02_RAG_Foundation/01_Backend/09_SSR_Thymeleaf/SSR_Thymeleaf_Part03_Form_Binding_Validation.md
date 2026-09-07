# SSR Thymeleaf Part03 - Form Binding And Validation

---

# 1. Form Binding Core

## 1.1 Form Binding Definition

### [개념]

Form Binding은 HTML Form 입력값을 Spring MVC Controller의 Java 객체로 바인딩하는 구조이다.

Thymeleaf에서는 `th:object`로 Form Object를 지정하고, `th:field`로 Field를 연결한다.

```text
GET Form Page
→ Controller creates Form Object
→ Model.addAttribute("userForm", userForm)
→ Thymeleaf th:object="${userForm}"
→ th:field="*{email}"

POST Submit
→ Request Parameter
→ @ModelAttribute UserForm userForm
→ @Valid Validation
→ BindingResult
→ Success Redirect or Error View
```

---

### [핵심]

- Form Binding은 SSR Thymeleaf의 핵심 기능이다.
- `th:object`는 Form 전체의 Binding 대상 객체이다.
- `th:field`는 Form Object Field와 HTML Input을 연결한다.
- `*{fieldName}`은 Selection Expression이다.
- Controller는 Form 화면 렌더링 전에 Form Object를 Model에 담아야 한다.
- Submit 후 Controller는 `@ModelAttribute`로 Form 데이터를 받는다.
- `@Valid`는 Form Object 검증을 실행한다.
- `BindingResult`는 Binding / Validation 결과를 저장한다.
- Validation 실패 시 같은 Form View를 다시 반환한다.
- Validation 성공 시 Redirect로 PRG Pattern을 적용한다.

---

### [실무]

2026 실무 기준 Form Binding은 다음 화면에 자주 사용된다.

- Admin Create Form
- Admin Update Form
- Search Form
- Login Form
- Signup Form
- Password Reset Form
- Internal Tool Input Page
- Backoffice Management Page

권장 구조:

```text
Form DTO
→ Controller Binding
→ Bean Validation
→ Business Validation
→ Service Command
→ Redirect
```

Entity 직접 Binding은 단순 내부 Admin Page에서만 제한적으로 허용하고, 일반적으로 Form DTO 사용을 권장한다.

---

### [FAQ]

Q. Form Binding이란?

A.
HTML Form 입력값을 Spring MVC 객체에 자동 연결하는 구조이다.

Q. Thymeleaf Form Binding 핵심 속성은?

A.
`th:object`와 `th:field`이다.

Q. Form Binding에서 Entity를 직접 사용해도 되는가?

A.
단순 내부 Admin Page에서는 가능하지만, 실무에서는 Form DTO 사용을 권장한다.

Q. Validation 실패 시 어떤 View를 반환하는가?

A.
Redirect하지 않고 사용자가 입력하던 같은 Form View를 반환한다.

---

# 2. Form Object

## 2.1 Form DTO

### [개념]

Form DTO는 HTML Form 입력값을 받기 위한 객체이다.

Entity와 화면 입력 구조를 분리하여 Validation, Security, 유지보수성을 높인다.

```text
HTML Form
→ UserCreateForm
→ Controller
→ Service
→ Entity
```

---

### [핵심]

- Form DTO는 입력 전용 객체이다.
- Entity 직접 노출을 줄인다.
- Validation Annotation을 Form DTO에 선언한다.
- 화면 요구사항에 맞는 Field만 포함한다.
- Create Form과 Update Form을 분리할 수 있다.
- API Request DTO와 View Form DTO는 목적에 따라 분리 가능하다.
- Form DTO 이름은 화면 목적 중심으로 작성한다.

---

### [실무]

Form DTO 예시:

```java
public class UserCreateForm {

    @NotBlank
    private String email;

    @NotBlank
    private String name;

    @NotBlank
    private String password;

    // getter / setter
}
```

Controller에서 Form Object 생성:

```java
@GetMapping("/admin/users/new")
public String createForm(Model model) {
    model.addAttribute("userForm", new UserCreateForm());
    return "admin/users/create-form";
}
```

Template에서 Binding:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <input type="email" th:field="*{email}" />
  <input type="text" th:field="*{name}" />
  <input type="password" th:field="*{password}" />
  <button type="submit">저장</button>
</form>
```

---

### [FAQ]

Q. Form DTO는 왜 사용하는가?

A.
Entity와 화면 입력값을 분리하고 Validation과 보안을 명확히 하기 위해 사용한다.

Q. Create Form과 Update Form을 분리해야 하는가?

A.
입력 Field나 Validation 조건이 다르면 분리 권장이다.

Q. Form DTO 이름은 어떻게 정하는가?

A.
`UserCreateForm`, `UserUpdateForm`, `FestivalSearchForm`처럼 화면 목적 중심으로 정한다.

---

## 2.2 Model Attribute Naming

### [개념]

Model Attribute Name은 Thymeleaf Template에서 Form Object를 참조하는 이름이다.

Controller의 `model.addAttribute("userForm", form)`과 Template의 `th:object="${userForm}"`는 반드시 일치해야 한다.

```text
model.addAttribute("userForm", new UserCreateForm())
→ th:object="${userForm}"
→ th:field="*{email}"
```

---

### [핵심]

- Model Attribute Name은 Template 변수명이다.
- `th:object` 이름과 Controller Attribute 이름이 일치해야 한다.
- `@ModelAttribute("userForm")` 이름도 Template의 `th:object`와 맞추는 것이 좋다.
- 이름 불일치는 Binding 오류의 주요 원인이다.
- Form Object 이름은 단수형 + `Form` suffix를 권장한다.
- 목록 데이터는 복수형, Form Object는 명확한 Form 이름을 권장한다.

---

### [실무]

권장 이름:

```text
userForm
festivalForm
reviewForm
searchForm
passwordResetForm
```

잘못된 예:

```java
model.addAttribute("form", new UserCreateForm());
```

```html
<form th:object="${userForm}"></form>
```

문제:

```text
Controller Attribute Name = form
Template th:object Name = userForm
→ 불일치
→ Binding 오류
```

올바른 예:

```java
model.addAttribute("userForm", new UserCreateForm());
```

```html
<form th:object="${userForm}"></form>
```

---

### [FAQ]

Q. `th:object="${userForm}"`의 `userForm`은 어디서 오는가?

A.
Controller에서 Model에 담은 Attribute 이름이다.

Q. Model Attribute 이름이 다르면 어떻게 되는가?

A.
Template에서 Form Object를 찾지 못해 Binding 오류가 발생할 수 있다.

Q. Form Object 이름은 어떻게 짓는가?

A.
`userForm`, `orderForm`, `searchForm`처럼 화면 목적이 드러나게 짓는다.

---

# 3. th:object

## 3.1 Selection Object

### [개념]

`th:object`는 Form 내부에서 사용할 Selection Object를 지정하는 Thymeleaf Attribute이다.

`th:object="${userForm}"`을 선언하면 Form 내부의 `*{email}`은 `userForm.email`을 의미한다.

```html
<form th:object="${userForm}">
  <input th:field="*{email}" />
</form>
```

---

### [핵심]

- `th:object`는 Form Binding 대상 객체를 지정한다.
- `th:object` 값은 Model Attribute여야 한다.
- Form 내부에서는 `*{field}` Selection Expression을 사용한다.
- `th:field`와 함께 사용하는 것이 일반적이다.
- `th:object` 없이 `*{}`를 사용하면 오류 가능성이 높다.
- `th:object`는 보통 `<form>` 태그에 선언한다.

---

### [실무]

Controller:

```java
@GetMapping("/admin/users/new")
public String createForm(Model model) {
    model.addAttribute("userForm", new UserCreateForm());
    return "admin/users/create-form";
}
```

Template:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <input type="email" th:field="*{email}" />
  <input type="text" th:field="*{name}" />
  <button type="submit">저장</button>
</form>
```

Mapping:

```text
th:object="${userForm}"
+ th:field="*{email}"
→ userForm.email
```

---

### [FAQ]

Q. `th:object`는 무엇인가?

A.
Form 내부에서 사용할 Binding 대상 객체를 지정하는 Thymeleaf 속성이다.

Q. `th:object`는 어디에 선언하는가?

A.
보통 `<form>` 태그에 선언한다.

Q. `th:object` 없이 `th:field="*{email}"`을 써도 되는가?

A.
권장하지 않는다.
Selection Object가 명확하지 않아 Binding 오류가 발생하기 쉽다.

---

# 4. th:field

## 4.1 Field Binding

### [개념]

`th:field`는 Form Object의 Field와 HTML Form Input을 연결하는 Thymeleaf Attribute이다.

`th:field="*{email}"`은 Input의 `name`, `id`, `value` 속성을 Binding Field 기준으로 생성한다.

```html
<input type="email" th:field="*{email}" />
```

---

### [핵심]

- `th:field`는 Form Field Binding에 사용한다.
- `name`, `id`, `value`를 자동 처리한다.
- `th:object`와 함께 사용한다.
- Validation 실패 후 입력값 재표시에 유리하다.
- Text, Password, Checkbox, Radio, Select 등에 사용할 수 있다.
- Form Binding에서는 `th:value`보다 `th:field`를 우선 사용한다.
- DTO Field 이름과 `th:field` 이름이 일치해야 한다.

---

### [실무]

Text Input:

```html
<input type="text" th:field="*{name}" />
```

Email Input:

```html
<input type="email" th:field="*{email}" />
```

Password Input:

```html
<input type="password" th:field="*{password}" />
```

Textarea:

```html
<textarea th:field="*{description}"></textarea>
```

Rendered HTML 예시:

```html
<input type="email" id="email" name="email" value="user@example.com" />
```

---

### [FAQ]

Q. `th:field`는 무엇인가?

A.
Form Object의 Field와 HTML Input을 연결하는 Thymeleaf 속성이다.

Q. `th:field`는 어떤 속성을 자동 생성하는가?

A.
주로 `id`, `name`, `value`를 Field 기준으로 생성한다.

Q. Form Binding에서 `th:value`보다 `th:field`를 권장하는 이유는?

A.
Binding, Validation 실패 후 입력값 유지, Error 표시와 잘 연동되기 때문이다.

Q. Form 값이 DTO에 들어오지 않는 이유는?

A.
Input Name과 DTO Field 이름이 일치하지 않을 가능성이 높다.

---

## 4.2 Checkbox Radio Select Binding

### [개념]

Checkbox, Radio, Select Binding은 선택형 입력값을 Form Object Field에 연결하는 방식이다.

Thymeleaf는 `th:field`와 Option Value를 기준으로 선택 상태를 처리한다.

---

### [핵심]

- Checkbox는 boolean 또는 Collection Field와 연결할 수 있다.
- Radio는 단일 선택 Field와 연결한다.
- Select는 단일 선택 또는 다중 선택 Field와 연결한다.
- Option 목록은 Model Attribute로 전달하는 것이 좋다.
- `th:selected` 직접 처리보다 `th:field` 기반 Binding을 우선 사용한다.
- Validation 실패 시 Option 목록 Model Attribute를 다시 담아야 한다.

---

### [실무]

Checkbox boolean:

```html
<label>
  <input type="checkbox" th:field="*{active}" />
  활성화
</label>
```

Radio:

```html
<label>
  <input type="radio" th:field="*{role}" value="USER" />
  USER
</label>
<label>
  <input type="radio" th:field="*{role}" value="ADMIN" />
  ADMIN
</label>
```

Select:

```html
<select th:field="*{categoryCode}">
  <option value="">카테고리 선택</option>
  <option
    th:each="category : ${categories}"
    th:value="${category.code}"
    th:text="${category.name}"
  >
    category
  </option>
</select>
```

Controller:

```java
@GetMapping("/admin/festivals/new")
public String createForm(Model model) {
    model.addAttribute("festivalForm", new FestivalCreateForm());
    model.addAttribute("categories", categoryService.findAll());
    return "admin/festivals/create-form";
}
```

---

### [FAQ]

Q. Checkbox도 `th:field`를 사용하는가?

A.
사용한다.
boolean Field 또는 Collection Field와 Binding할 수 있다.

Q. Select Option 목록은 어디서 전달하는가?

A.
Controller에서 Model Attribute로 전달하는 것이 일반적이다.

Q. Select에서 선택 상태를 직접 `th:selected`로 처리해야 하는가?

A.
Form Binding에서는 `th:field`가 선택 상태를 처리하므로 직접 처리하지 않는 것을 권장한다.

Q. Validation 실패 후 Select Option이 사라지는 이유는?

A.
실패 View 반환 전에 Option 목록을 Model에 다시 담지 않았기 때문이다.

---

# 5. Form Submit

## 5.1 th:action And method

### [개념]

`th:action`은 Form Submit URL을 생성하는 Thymeleaf Attribute이다.

Form의 `method`는 일반적으로 `get` 또는 `post`를 사용한다.

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post"></form>
```

---

### [핵심]

- `th:action`은 Submit URL을 서버에서 생성한다.
- `@{}` Link Expression을 사용한다.
- 생성, 수정, 삭제 요청은 보통 `POST`를 사용한다.
- 조회와 검색은 보통 `GET`을 사용한다.
- HTML Form은 기본적으로 GET / POST만 지원한다.
- PUT / PATCH / DELETE는 Hidden Method Filter 또는 POST Endpoint로 처리한다.
- Spring Security CSRF 활성화 시 상태 변경 Form에는 CSRF Token이 필요하다.

---

### [실무]

Create Form Submit:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <input th:field="*{email}" />
  <button type="submit">등록</button>
</form>
```

Search Form Submit:

```html
<form th:action="@{/admin/users}" th:object="${searchForm}" method="get">
  <input th:field="*{keyword}" />
  <button type="submit">검색</button>
</form>
```

Update Form Submit:

```html
<form
  th:action="@{/admin/users/{id}(id=${userId})}"
  th:object="${userForm}"
  method="post"
>
  <input th:field="*{name}" />
  <button type="submit">수정</button>
</form>
```

CSRF Token:

```html
<input
  type="hidden"
  th:name="${_csrf.parameterName}"
  th:value="${_csrf.token}"
/>
```

---

### [FAQ]

Q. `th:action`은 무엇인가?

A.
Form Submit URL을 동적으로 생성하는 Thymeleaf 속성이다.

Q. 등록 Form은 어떤 HTTP Method를 사용하는가?

A.
일반적으로 `POST`를 사용한다.

Q. 검색 Form은 어떤 HTTP Method를 사용하는가?

A.
일반적으로 `GET`을 사용한다.

Q. 상태 변경 Form에 CSRF Token이 필요한가?

A.
Spring Security CSRF 보호가 활성화되어 있으면 필요하다.

---

## 5.2 @ModelAttribute Binding

### [개념]

`@ModelAttribute`는 Form Submit 데이터를 Java 객체에 바인딩하는 Spring MVC Annotation이다.

Form Input의 `name`과 Form DTO Field 이름이 일치하면 자동으로 값이 들어간다.

```text
<input name="email">
→ @ModelAttribute UserCreateForm userForm
→ userForm.email
```

---

### [핵심]

- `@ModelAttribute`는 요청 Parameter를 객체에 바인딩한다.
- Form Field Name과 DTO Field Name이 일치해야 한다.
- `th:field`를 사용하면 Field Name이 자동 생성된다.
- Validation과 함께 사용할 수 있다.
- Binding 결과는 `BindingResult`로 확인한다.
- `@ModelAttribute("userForm")` 이름은 Template `th:object`와 맞추는 것이 좋다.

---

### [실무]

Controller:

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

Template:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <input th:field="*{email}" />
  <input th:field="*{name}" />
  <button type="submit">저장</button>
</form>
```

Binding Flow:

```text
POST /admin/users
→ Request Parameter
→ @ModelAttribute UserCreateForm
→ @Valid Validation
→ BindingResult
→ Success Redirect or Error View
```

---

### [FAQ]

Q. `@ModelAttribute`는 무엇인가?

A.
요청 Parameter를 Java 객체에 바인딩하는 Spring MVC Annotation이다.

Q. Form Field 이름과 DTO Field 이름이 달라도 되는가?

A.
기본적으로 일치해야 한다.
`th:field`를 사용하면 이름 불일치를 줄일 수 있다.

Q. `@ModelAttribute("userForm")`의 이름은 무엇과 맞춰야 하는가?

A.
Template의 `th:object="${userForm}"` 이름과 맞추는 것이 좋다.

---

# 6. Validation Core

## 6.1 Bean Validation

### [개념]

Bean Validation은 Form DTO Field에 Validation Annotation을 선언하고, Controller에서 `@Valid`로 검증하는 구조이다.

Spring Boot 3.x 기준 Jakarta Validation을 사용한다.

```java
public class UserCreateForm {

    @NotBlank
    private String email;

    @Size(min = 2, max = 20)
    private String name;
}
```

---

### [핵심]

- Spring Boot 3.x는 Jakarta Validation 기반이다.
- 대표 Annotation은 `@NotBlank`, `@NotNull`, `@Email`, `@Size`, `@Min`, `@Max`이다.
- `@Valid`는 Controller Parameter에서 검증을 실행한다.
- 검증 결과는 `BindingResult`에 담긴다.
- Validation 실패 시 Form View를 다시 반환한다.
- 실패 시 Redirect하지 않는다.
- Business Validation은 Service 또는 별도 검증 로직과 함께 처리한다.

---

### [실무]

Form DTO:

```java
public class UserCreateForm {

    @NotBlank(message = "이메일은 필수입니다.")
    @Email(message = "이메일 형식이 올바르지 않습니다.")
    private String email;

    @NotBlank(message = "이름은 필수입니다.")
    @Size(max = 20, message = "이름은 20자 이하로 입력하세요.")
    private String name;

    @NotBlank(message = "비밀번호는 필수입니다.")
    @Size(min = 8, message = "비밀번호는 8자 이상이어야 합니다.")
    private String password;

    // getter / setter
}
```

Controller:

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

---

### [FAQ]

Q. Bean Validation이란?

A.
Annotation 기반으로 Java 객체의 입력값을 검증하는 방식이다.

Q. Spring Boot 3.x에서 Validation 패키지는 무엇인가?

A.
`jakarta.validation` 계열을 사용한다.

Q. Validation 실패 시 Redirect해도 되는가?

A.
권장하지 않는다.
BindingResult와 입력값 유지를 위해 같은 Form View를 다시 반환한다.

---

## 6.2 @Valid And BindingResult

### [개념]

`@Valid`는 Form Object 검증을 실행하고, `BindingResult`는 Binding / Validation 결과를 저장한다.

`BindingResult`는 반드시 검증 대상 객체 바로 뒤에 위치해야 한다.

```java
@PostMapping("/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult
) {
    // ...
}
```

---

### [핵심]

- `@Valid`는 Validation 실행 지점이다.
- `BindingResult`는 검증 결과를 담는다.
- `BindingResult`는 `@Valid` 대상 바로 뒤에 있어야 한다.
- 위치가 틀리면 검증 오류 처리 전에 예외가 발생할 수 있다.
- `bindingResult.hasErrors()`로 오류 여부를 확인한다.
- 오류가 있으면 Form View를 반환한다.
- 오류가 없으면 Service 호출 후 Redirect한다.

---

### [실무]

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

문제:

```text
@Valid 대상 바로 뒤에 BindingResult가 없음
→ Validation Error 처리 실패 가능
```

---

### [FAQ]

Q. `BindingResult`는 어디에 위치해야 하는가?

A.
`@Valid`가 붙은 Form Object 바로 뒤에 위치해야 한다.

Q. Validation Error는 어떻게 확인하는가?

A.
`bindingResult.hasErrors()`를 사용한다.

Q. `BindingResult` 위치가 틀리면 어떻게 되는가?

A.
검증 오류를 Controller에서 처리하지 못하고 예외가 발생할 수 있다.

---

# 7. Field Error Rendering

## 7.1 th:errors

### [개념]

`th:errors`는 특정 Field의 Validation Error Message를 출력하는 Thymeleaf Attribute이다.

Form Binding과 BindingResult가 연결되어 있을 때 동작한다.

```html
<p th:errors="*{email}">Email Error</p>
```

---

### [핵심]

- `th:errors`는 Field Error Message를 출력한다.
- `th:field`와 같은 Field 이름을 사용한다.
- `th:object` 내부에서 `*{field}` 형태로 작성한다.
- Validation 실패 후 같은 View를 반환해야 Error가 표시된다.
- Error Message는 Validation Annotation의 `message`를 사용할 수 있다.
- Redirect하면 `BindingResult`가 사라져 Error 표시가 어렵다.

---

### [실무]

Template:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <div>
    <label for="email">이메일</label>
    <input type="email" th:field="*{email}" />
    <p class="field-error" th:errors="*{email}">Email Error</p>
  </div>

  <button type="submit">저장</button>
</form>
```

Validation Error Flow:

```text
@Valid 실패
→ BindingResult에 Field Error 저장
→ return "admin/users/create-form"
→ th:errors="*{email}" 출력
```

---

### [FAQ]

Q. Field Error Message는 어떻게 출력하는가?

A.
`th:errors="*{fieldName}"`을 사용한다.

Q. `th:errors`가 출력되지 않는 이유는?

A.
BindingResult가 없거나, Redirect했거나, Field 이름이 일치하지 않을 수 있다.

Q. Validation 실패 후 왜 같은 View를 반환해야 하는가?

A.
BindingResult와 입력값을 유지해서 Error Message를 표시하기 위해서이다.

---

## 7.2 #fields.hasErrors

### [개념]

`#fields.hasErrors()`는 특정 Field에 Validation Error가 있는지 확인하는 Thymeleaf Utility이다.

Error 여부에 따라 CSS Class를 추가하거나 Error 영역을 조건부 렌더링할 때 사용한다.

```html
<input
  th:field="*{email}"
  th:classappend="${#fields.hasErrors('email')} ? 'is-invalid'"
/>
```

---

### [핵심]

- `#fields.hasErrors('fieldName')`은 Field Error 여부를 반환한다.
- `th:classappend`와 자주 함께 사용한다.
- Error가 있을 때만 Message 영역을 출력할 수 있다.
- `th:object` 내부에서 사용한다.
- Field 이름 문자열은 DTO Field와 일치해야 한다.

---

### [실무]

Input Error Class:

```html
<input
  type="email"
  th:field="*{email}"
  class="form-control"
  th:classappend="${#fields.hasErrors('email')} ? 'is-invalid'"
/>
```

Conditional Error Block:

```html
<div th:if="${#fields.hasErrors('email')}" class="invalid-feedback">
  <p th:errors="*{email}">Email Error</p>
</div>
```

Full Pattern:

```html
<div>
  <label for="email">이메일</label>
  <input
    type="email"
    th:field="*{email}"
    th:classappend="${#fields.hasErrors('email')} ? 'is-invalid'"
  />
  <p th:if="${#fields.hasErrors('email')}" th:errors="*{email}">email error</p>
</div>
```

---

### [FAQ]

Q. Field Error가 있는지 어떻게 확인하는가?

A.
`#fields.hasErrors('fieldName')`을 사용한다.

Q. Error가 있을 때 CSS Class를 추가하려면?

A.
`th:classappend`와 `#fields.hasErrors()`를 함께 사용한다.

Q. `#fields.hasErrors('email')`의 `email`은 무엇과 일치해야 하는가?

A.
Form DTO의 Field 이름과 일치해야 한다.

---

# 8. Global Error Rendering

## 8.1 Object Error

### [개념]

Global Error 또는 Object Error는 특정 Field 하나가 아니라 Form Object 전체에 대한 오류이다.

예: 비밀번호 확인 불일치, 기간 범위 오류, 중복 이메일 오류.

```text
Field Error
→ email 형식 오류

Global Error
→ password와 confirmPassword 불일치
→ startDate가 endDate보다 늦음
→ 이미 사용 중인 이메일
```

---

### [핵심]

- Global Error는 Form Object 전체 오류이다.
- 특정 Field 하나에 매핑하기 어려운 오류에 사용한다.
- `BindingResult.reject()`로 추가할 수 있다.
- Template에서는 `#fields.hasGlobalErrors()`로 확인한다.
- `th:each`와 `#fields.globalErrors()`로 출력한다.
- Field에 연결 가능한 오류는 `rejectValue()`가 더 적합하다.

---

### [실무]

Controller:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult
) {
    if (!userForm.getPassword().equals(userForm.getConfirmPassword())) {
        bindingResult.reject("passwordMismatch", "비밀번호 확인이 일치하지 않습니다.");
    }

    if (bindingResult.hasErrors()) {
        return "admin/users/create-form";
    }

    userService.create(userForm);
    return "redirect:/admin/users";
}
```

Template:

```html
<div th:if="${#fields.hasGlobalErrors()}" class="global-errors">
  <p th:each="error : ${#fields.globalErrors()}" th:text="${error}">
    Global Error
  </p>
</div>
```

---

### [FAQ]

Q. Global Error는 무엇인가?

A.
특정 Field가 아니라 Form Object 전체에 대한 Validation Error이다.

Q. Global Error는 어떻게 추가하는가?

A.
`bindingResult.reject("errorCode", "message")`를 사용한다.

Q. Global Error는 Template에서 어떻게 출력하는가?

A.
`#fields.hasGlobalErrors()`와 `#fields.globalErrors()`를 사용한다.

---

## 8.2 Business Validation Error

### [개념]

Business Validation Error는 단순 Field 형식 검증이 아니라 비즈니스 규칙 위반으로 발생하는 오류이다.

예: 이메일 중복, 예약 불가 날짜, 권한 없는 수정, 이미 삭제된 데이터.

---

### [핵심]

- Bean Validation은 기본 입력값 검증에 적합하다.
- Business Validation은 Service 또는 Domain Logic에서 처리한다.
- Form 화면에서 다시 표시해야 하면 BindingResult에 Error를 추가한다.
- Field에 연결 가능한 오류는 `rejectValue()`를 사용한다.
- Form 전체 오류는 `reject()`를 사용한다.
- Business Validation Error도 Validation 실패 흐름에서는 같은 Form View를 반환한다.

---

### [실무]

Field Error 추가:

```java
if (userService.existsEmail(userForm.getEmail())) {
    bindingResult.rejectValue(
            "email",
            "duplicateEmail",
            "이미 사용 중인 이메일입니다."
    );
}
```

Global Error 추가:

```java
if (!festivalService.canRegister(userForm.getFestivalId())) {
    bindingResult.reject(
            "festivalClosed",
            "현재 등록할 수 없는 축제입니다."
    );
}
```

Full Pattern:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult
) {
    if (userService.existsEmail(userForm.getEmail())) {
        bindingResult.rejectValue("email", "duplicateEmail", "이미 사용 중인 이메일입니다.");
    }

    if (bindingResult.hasErrors()) {
        return "admin/users/create-form";
    }

    userService.create(userForm);
    return "redirect:/admin/users";
}
```

---

### [FAQ]

Q. 이메일 중복 오류는 Bean Validation으로 처리하는가?

A.
일반적으로 Business Validation으로 처리한다.

Q. 특정 Field에 Business Error를 추가하려면?

A.
`bindingResult.rejectValue("fieldName", "errorCode", "message")`를 사용한다.

Q. Form 전체 Business Error를 추가하려면?

A.
`bindingResult.reject("errorCode", "message")`를 사용한다.

---

# 9. Validation Failure Handling

## 9.1 Return Same View

### [개념]

Validation 실패 시에는 Redirect하지 않고 같은 Form View를 반환한다.

같은 View를 반환해야 BindingResult, 입력값, Error Message가 유지된다.

```text
Validation Fail
→ return "admin/users/create-form"

Validation Success
→ return "redirect:/admin/users"
```

---

### [핵심]

- Validation 실패 시 같은 Form View를 반환한다.
- Redirect하면 BindingResult가 사라진다.
- 입력값 재표시를 위해 `th:field`를 사용한다.
- Error Message 출력을 위해 `th:errors`를 사용한다.
- Select Option 등 추가 Model Attribute를 다시 채워야 한다.
- Validation 성공 시 Redirect한다.

---

### [실무]

잘못된 예:

```java
if (bindingResult.hasErrors()) {
    return "redirect:/admin/users/new";
}
```

문제:

```text
Redirect 발생
→ BindingResult 소실
→ 입력값 소실
→ Error Message 표시 실패
```

올바른 예:

```java
if (bindingResult.hasErrors()) {
    model.addAttribute("categories", categoryService.findAll());
    return "admin/festivals/create-form";
}
```

추가 Model Attribute 재등록:

```java
private void addFestivalFormOptions(Model model) {
    model.addAttribute("categories", categoryService.findAll());
    model.addAttribute("regions", regionService.findAll());
}
```

---

### [FAQ]

Q. Validation 실패 시 Redirect하면 안 되는 이유는?

A.
BindingResult와 입력값이 사라져 Error Message를 표시하기 어렵기 때문이다.

Q. Validation 실패 시 어떤 View를 반환하는가?

A.
사용자가 입력하던 같은 Form View를 반환한다.

Q. Validation 실패 시 Select Option이 사라지는 이유는?

A.
Form View 반환 전에 Option 목록 Model Attribute를 다시 추가하지 않았기 때문이다.

---

# 10. Create Form Pattern

## 10.1 Create GET POST Flow

### [개념]

Create Form Pattern은 신규 데이터 등록을 위해 GET으로 Form 화면을 보여주고 POST로 입력값을 처리하는 SSR 패턴이다.

```text
GET /admin/users/new
→ Empty Form Object
→ Render Create Form

POST /admin/users
→ @Valid Form Object
→ BindingResult
→ Error View or Redirect List
```

---

### [핵심]

- GET은 빈 Form Object를 Model에 담는다.
- POST는 `@ModelAttribute`로 입력값을 받는다.
- POST는 `@Valid`로 검증한다.
- 실패하면 같은 Form View를 반환한다.
- 성공하면 Service 호출 후 Redirect한다.
- 성공 후 Redirect는 PRG Pattern을 따른다.
- Select Option이 있으면 GET과 Validation 실패 시 모두 Model에 추가한다.

---

### [실무]

Controller:

```java
@Controller
@RequestMapping("/admin/users")
public class AdminUserController {

    @GetMapping("/new")
    public String createForm(Model model) {
        model.addAttribute("userForm", new UserCreateForm());
        return "admin/users/create-form";
    }

    @PostMapping
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
}
```

Template:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <div>
    <label for="email">이메일</label>
    <input type="email" th:field="*{email}" />
    <p th:errors="*{email}">email error</p>
  </div>

  <div>
    <label for="name">이름</label>
    <input type="text" th:field="*{name}" />
    <p th:errors="*{name}">name error</p>
  </div>

  <button type="submit">등록</button>
</form>
```

---

### [FAQ]

Q. Create Form GET에서는 무엇을 해야 하는가?

A.
빈 Form Object를 Model에 담고 Form View를 반환한다.

Q. Create Form POST에서는 무엇을 해야 하는가?

A.
Form Object Binding, Validation, Service 호출, Redirect를 처리한다.

Q. 등록 성공 후에는 어떤 응답을 권장하는가?

A.
`redirect:`를 사용해 목록 또는 상세 화면으로 이동하는 것을 권장한다.

---

# 11. Update Form Pattern

## 11.1 Update GET POST Flow

### [개념]

Update Form Pattern은 기존 데이터를 조회하여 Form에 채우고, 수정된 입력값을 POST로 처리하는 SSR 패턴이다.

```text
GET /admin/users/{id}/edit
→ Find Existing Data
→ Convert To Update Form
→ Render Update Form

POST /admin/users/{id}/edit
→ @Valid Update Form
→ BindingResult
→ Error View or Redirect Detail
```

---

### [핵심]

- GET은 기존 데이터를 조회한다.
- 조회 결과를 Update Form Object로 변환한다.
- Form Object를 Model에 담는다.
- POST는 Path Variable ID와 Form Object를 함께 받는다.
- 실패하면 같은 Update Form View를 반환한다.
- 성공하면 수정 후 Redirect한다.
- Validation 실패 시 Form Action에 필요한 `id`를 다시 Model에 담아야 한다.

---

### [실무]

Controller:

```java
@GetMapping("/{id}/edit")
public String updateForm(@PathVariable Long id, Model model) {
    UserResponse user = userService.findById(id);
    UserUpdateForm userForm = UserUpdateForm.from(user);

    model.addAttribute("userId", id);
    model.addAttribute("userForm", userForm);
    return "admin/users/update-form";
}

@PostMapping("/{id}/edit")
public String update(
        @PathVariable Long id,
        @Valid @ModelAttribute("userForm") UserUpdateForm userForm,
        BindingResult bindingResult,
        Model model
) {
    if (bindingResult.hasErrors()) {
        model.addAttribute("userId", id);
        return "admin/users/update-form";
    }

    userService.update(id, userForm);
    return "redirect:/admin/users/" + id;
}
```

Template:

```html
<form
  th:action="@{/admin/users/{id}/edit(id=${userId})}"
  th:object="${userForm}"
  method="post"
>
  <input type="text" th:field="*{name}" />
  <p th:errors="*{name}">name error</p>

  <button type="submit">수정</button>
</form>
```

---

### [FAQ]

Q. Update Form GET에서는 무엇을 해야 하는가?

A.
기존 데이터를 조회한 뒤 Update Form Object로 변환해 Model에 담는다.

Q. Update Form POST에서는 ID를 어떻게 받는가?

A.
보통 `@PathVariable Long id`로 받는다.

Q. Validation 실패 시 `userId`를 다시 Model에 넣어야 하는 이유는?

A.
Form Action URL 생성에 필요하기 때문이다.

---

# 12. Delete Form Pattern

## 12.1 Delete Action

### [개념]

Delete Action은 SSR 화면에서 삭제 버튼 또는 삭제 Form을 통해 서버에 삭제 요청을 보내는 패턴이다.

HTML Form은 DELETE Method를 직접 지원하지 않으므로 보통 POST를 사용한다.

```text
POST /admin/users/{id}/delete
→ Delete
→ Redirect List
```

---

### [핵심]

- 삭제는 링크보다 Form Submit을 권장한다.
- HTML Form은 GET / POST만 기본 지원한다.
- 삭제 요청은 `POST` Endpoint로 처리 가능하다.
- 성공 후 목록 화면으로 Redirect한다.
- CSRF 보호가 활성화된 경우 CSRF Token이 필요하다.
- 삭제 전 권한 검증이 필요하다.
- Soft Delete / Hard Delete 정책을 명확히 한다.

---

### [실무]

Controller:

```java
@PostMapping("/{id}/delete")
public String delete(@PathVariable Long id) {
    userService.delete(id);
    return "redirect:/admin/users";
}
```

Template:

```html
<form th:action="@{/admin/users/{id}/delete(id=${user.id})}" method="post">
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />
  <button type="submit" onclick="return confirm('삭제하시겠습니까?')">
    삭제
  </button>
</form>
```

권장:

```text
Delete Link <a href>
→ 비권장

Delete POST Form + CSRF Token
→ 권장
```

---

### [FAQ]

Q. 삭제 요청은 링크로 보내도 되는가?

A.
권장하지 않는다.
상태 변경 요청은 POST Form으로 처리하는 것이 안전하다.

Q. HTML Form에서 DELETE Method를 바로 사용할 수 있는가?

A.
기본 HTML Form은 GET과 POST만 지원한다.

Q. 삭제 성공 후에는 무엇을 반환하는가?

A.
일반적으로 목록 화면으로 Redirect한다.

---

# 13. Search Form Pattern

## 13.1 GET Search Form

### [개념]

Search Form Pattern은 검색 조건을 Query Parameter로 전달하고 결과 목록을 렌더링하는 SSR 패턴이다.

검색은 상태 변경이 아니므로 일반적으로 `GET`을 사용한다.

```text
GET /admin/users?keyword=kim&role=USER
→ @ModelAttribute SearchForm
→ Search Result
→ Render List View
```

---

### [핵심]

- 검색 Form은 `method="get"`을 사용한다.
- 검색 조건은 Query Parameter로 전달된다.
- Search Form Object를 사용할 수 있다.
- 검색 결과와 검색 조건을 함께 Model에 담는다.
- Pagination 링크에는 검색 조건을 유지해야 한다.
- `th:field`로 검색 조건 값을 유지할 수 있다.
- Query Parameter에 민감 정보를 포함하지 않는다.

---

### [실무]

Search Form DTO:

```java
public class UserSearchForm {

    private String keyword;
    private String role;

    // getter / setter
}
```

Controller:

```java
@GetMapping
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

Template:

```html
<form th:action="@{/admin/users}" th:object="${searchForm}" method="get">
  <input type="text" th:field="*{keyword}" placeholder="검색어" />

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

Q. 검색 Form은 어떤 Method를 사용하는가?

A.
일반적으로 `GET`을 사용한다.

Q. 검색 조건은 어디에 담기는가?

A.
Query Parameter로 전달되고 Search Form Object에 바인딩될 수 있다.

Q. 검색 후 입력값을 유지하려면?

A.
Search Form Object를 Model에 담고 `th:field`를 사용한다.

---

# 14. PRG Pattern

## 14.1 Post Redirect Get

### [개념]

PRG(Post Redirect Get) Pattern은 POST 처리 성공 후 View를 직접 반환하지 않고 Redirect로 GET 요청을 유도하는 패턴이다.

중복 Submit 방지와 새로고침 재전송 문제를 줄이기 위해 사용한다.

```text
POST Submit
→ Success
→ redirect:/admin/users
→ GET /admin/users
→ Render List
```

---

### [핵심]

- POST 성공 후 Redirect한다.
- 새로고침 시 POST 재전송을 방지한다.
- 등록 / 수정 / 삭제 성공 후 사용한다.
- Validation 실패 시에는 Redirect하지 않는다.
- 성공 메시지는 Flash Attribute로 전달할 수 있다.
- PRG는 SSR Form 처리의 기본 성공 흐름이다.

---

### [실무]

Create Success:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult,
        RedirectAttributes redirectAttributes
) {
    if (bindingResult.hasErrors()) {
        return "admin/users/create-form";
    }

    userService.create(userForm);
    redirectAttributes.addFlashAttribute("message", "사용자가 등록되었습니다.");
    return "redirect:/admin/users";
}
```

List Template:

```html
<div th:if="${message}" th:text="${message}" class="alert">message</div>
```

Flow:

```text
POST Success
→ redirectAttributes.addFlashAttribute()
→ redirect
→ GET View
→ message 출력
```

---

### [FAQ]

Q. PRG Pattern이란?

A.
POST 성공 후 Redirect하여 GET 화면을 다시 렌더링하는 패턴이다.

Q. PRG Pattern을 사용하는 이유는?

A.
새로고침 시 POST 재전송과 중복 등록을 방지하기 위해 사용한다.

Q. Validation 실패 시에도 PRG를 적용하는가?

A.
아니다.
Validation 실패 시에는 같은 Form View를 반환한다.

---

# 15. RedirectAttributes

## 15.1 Flash Attribute

### [개념]

Flash Attribute는 Redirect 이후 한 번만 사용할 데이터를 전달하는 Spring MVC 기능이다.

등록 성공 메시지, 수정 완료 메시지, 삭제 완료 메시지에 자주 사용한다.

```text
POST
→ addFlashAttribute("message", "저장 완료")
→ Redirect
→ GET View에서 message 사용
→ 이후 소멸
```

---

### [핵심]

- `RedirectAttributes`는 Redirect 시 데이터를 전달한다.
- `addFlashAttribute()`는 Redirect 이후 한 번만 유지된다.
- 성공 메시지 전달에 적합하다.
- Error Message 전달보다는 성공 메시지 전달에 주로 사용한다.
- Validation Error는 BindingResult로 처리하고 Redirect하지 않는다.
- Flash Attribute는 대용량 객체나 장기 상태 저장에 사용하지 않는다.

---

### [실무]

Controller:

```java
@PostMapping("/admin/users")
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult,
        RedirectAttributes redirectAttributes
) {
    if (bindingResult.hasErrors()) {
        return "admin/users/create-form";
    }

    userService.create(userForm);
    redirectAttributes.addFlashAttribute("message", "등록되었습니다.");
    return "redirect:/admin/users";
}
```

Template:

```html
<div th:if="${message}" class="alert alert-success">
  <span th:text="${message}">message</span>
</div>
```

---

### [FAQ]

Q. Flash Attribute는 무엇인가?

A.
Redirect 이후 한 번만 사용할 데이터를 전달하는 기능이다.

Q. Flash Attribute는 언제 사용하는가?

A.
등록, 수정, 삭제 성공 메시지 전달에 자주 사용한다.

Q. Validation Error를 Flash Attribute로 전달하는가?

A.
권장하지 않는다.
Validation Error는 BindingResult로 처리하고 같은 View를 반환한다.

---

# 16. Common Form Binding Mistakes

## 16.1 Binding Mistakes

### [개념]

Form Binding Mistake는 Form Object, Field Name, BindingResult, Validation Error 처리 흐름이 맞지 않아 발생하는 오류이다.

---

### [핵심]

자주 발생하는 실수:

- GET Form 화면에서 Form Object를 Model에 담지 않음
- `th:object` 이름과 Model Attribute 이름 불일치
- `th:object` 없이 `th:field="*{...}"` 사용
- Form DTO Field 이름과 Input Field 이름 불일치
- `@Valid` 뒤에 `BindingResult`를 바로 두지 않음
- Validation 실패 시 Redirect 사용
- 실패 View 반환 전 Select Option Model Attribute 재등록 누락
- `th:errors` Field 이름 불일치
- Business Error를 예외로만 처리하고 Form에 표시하지 않음
- Delete 요청을 GET Link로 처리
- POST 성공 후 View 직접 반환
- CSRF Token 누락

---

### [실무]

잘못된 예:

```java
@GetMapping("/admin/users/new")
public String createForm() {
    return "admin/users/create-form";
}
```

문제:

```text
Form Object 없음
→ th:object="${userForm}" 찾기 실패
```

올바른 예:

```java
@GetMapping("/admin/users/new")
public String createForm(Model model) {
    model.addAttribute("userForm", new UserCreateForm());
    return "admin/users/create-form";
}
```

잘못된 예:

```java
if (bindingResult.hasErrors()) {
    return "redirect:/admin/users/new";
}
```

올바른 예:

```java
if (bindingResult.hasErrors()) {
    return "admin/users/create-form";
}
```

---

### [FAQ]

Q. `th:object` 관련 오류가 나는 가장 흔한 이유는?

A.
Controller에서 Form Object를 Model에 담지 않았거나 이름이 불일치하기 때문이다.

Q. Validation Error가 화면에 안 보이는 이유는?

A.
Redirect했거나, `BindingResult` 위치가 틀렸거나, `th:errors` Field 이름이 다를 수 있다.

Q. Select Option이 Validation 실패 후 사라지는 이유는?

A.
실패 View 반환 전에 Option 목록을 Model에 다시 담지 않았기 때문이다.

---

# 17. Review Checklist

## 17.1 Form Binding Review Checklist

### [개념]

Form Binding Review Checklist는 SSR Thymeleaf Form 코드와 RAG 문서를 Agent가 검수하기 위한 기준이다.

---

### [핵심]

Form Object 검수:

- Form DTO 사용 여부
- Entity 직접 Binding 여부
- Form DTO Field와 화면 입력값 일치 여부
- Validation Annotation 적절성
- Create Form / Update Form 분리 필요 여부

Controller 검수:

- GET Form에서 Form Object Model 추가 여부
- POST Handler에서 `@ModelAttribute` 사용 여부
- `@Valid` 사용 여부
- `BindingResult`가 `@Valid` 대상 바로 뒤에 있는지 여부
- Validation 실패 시 같은 View 반환 여부
- Validation 성공 시 Redirect 여부
- Select Option 등 부가 Model Attribute 재등록 여부
- Business Validation Error 처리 여부
- POST Form CSRF Token 대응 여부

Template 검수:

- `th:object` 존재 여부
- `th:object`와 Model Attribute 이름 일치 여부
- `th:field` 사용 여부
- `th:action`에 `@{}` 사용 여부
- `th:errors` Field 이름 일치 여부
- `#fields.hasErrors()` 사용 적절성
- Checkbox / Radio / Select Binding 적절성
- Delete Action이 POST Form인지 여부

Flow 검수:

```text
GET Form
→ Form Object Model 등록
→ Render Form

POST Submit
→ @ModelAttribute Binding
→ @Valid Validation
→ BindingResult Check
→ Error View or Success Redirect
```

---

### [실무]

검수 Flow:

```text
Template th:object 확인
→ Controller Model Attribute 확인
→ th:field Field Name 확인
→ @ModelAttribute Name 확인
→ @Valid / BindingResult 순서 확인
→ Error Rendering 확인
→ Validation Fail Return View 확인
→ Success Redirect 확인
→ CSRF Token 확인
```

---

### [FAQ]

Q. Form Binding 검수에서 가장 먼저 볼 것은?

A.
GET Controller가 Form Object를 Model에 담고 Template의 `th:object`와 이름이 일치하는지 확인한다.

Q. Validation 검수에서 가장 중요한 것은?

A.
`BindingResult`가 `@Valid` 대상 바로 뒤에 있는지와 실패 시 같은 View를 반환하는지 확인하는 것이다.

Q. Form Template 검수 핵심은?

A.
`th:object`, `th:field`, `th:errors`, `th:action`의 이름과 경로가 일치하는지 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Thymeleaf Form Binding이란?
A. HTML Form 입력값을 Spring MVC 객체에 바인딩하는 구조이다.

Q. Thymeleaf Form Binding 핵심 속성은?
A. `th:object`와 `th:field`이다.

Q. `th:object`는 무엇인가?
A. Form 내부에서 사용할 Binding 대상 객체를 지정하는 Thymeleaf 속성이다.

Q. `th:field`는 무엇인가?
A. Form Object의 Field와 HTML Input을 연결하는 Thymeleaf 속성이다.

Q. `th:field`가 자동 생성하는 HTML 속성은?
A. 주로 `id`, `name`, `value`를 Field 기준으로 생성한다.

Q. `th:object="${userForm}"`의 `userForm`은 어디서 오는가?
A. Controller에서 `model.addAttribute("userForm", form)`으로 전달한 Model Attribute이다.

Q. Form DTO를 사용하는 이유는?
A. Entity와 화면 입력값을 분리하고 Validation과 보안을 명확히 하기 위해 사용한다.

Q. Form Object 이름은 어떻게 정하는가?
A. `userForm`, `festivalForm`, `searchForm`처럼 화면 목적 중심으로 정한다.

Q. `*{email}`은 무엇인가?
A. `th:object`로 지정된 객체의 `email` Field에 접근하는 Selection Expression이다.

Q. `th:object` 없이 `*{}`를 쓰면 안 되는 이유는?
A. Selection Object가 명확하지 않아 Binding 오류가 발생하기 쉽기 때문이다.

Q. `th:action`은 무엇인가?
A. Form Submit URL을 동적으로 생성하는 Thymeleaf 속성이다.

Q. 등록 Form은 어떤 HTTP Method를 사용하는가?
A. 일반적으로 `POST`를 사용한다.

Q. 검색 Form은 어떤 HTTP Method를 사용하는가?
A. 일반적으로 `GET`을 사용한다.

Q. `@ModelAttribute`는 무엇인가?
A. 요청 Parameter를 Java 객체에 바인딩하는 Spring MVC Annotation이다.

Q. Form Field와 DTO Field 이름이 일치해야 하는가?
A. 기본적으로 일치해야 한다.

Q. Bean Validation이란?
A. Annotation 기반으로 Java 객체 입력값을 검증하는 방식이다.

Q. Spring Boot 3.x Validation 패키지는?
A. `jakarta.validation` 계열을 사용한다.

Q. `@Valid`는 무엇인가?
A. Form Object의 Bean Validation을 실행하는 Annotation이다.

Q. `BindingResult`는 무엇인가?
A. Binding 및 Validation 결과를 저장하는 객체이다.

Q. `BindingResult` 위치는 어디인가?
A. `@Valid` 대상 Form Object 바로 뒤에 위치해야 한다.

Q. Validation Error는 어떻게 확인하는가?
A. `bindingResult.hasErrors()`를 사용한다.

Q. Validation 실패 시 Redirect하면 안 되는 이유는?
A. BindingResult와 입력값이 사라져 Error Message를 표시하기 어렵기 때문이다.

Q. Validation 실패 시 무엇을 반환하는가?
A. 사용자가 입력하던 같은 Form View를 반환한다.

Q. Field Error Message는 어떻게 출력하는가?
A. `th:errors="*{fieldName}"`를 사용한다.

Q. Field Error 여부는 어떻게 확인하는가?
A. `#fields.hasErrors('fieldName')`을 사용한다.

Q. Error가 있을 때 CSS Class를 추가하려면?
A. `th:classappend`와 `#fields.hasErrors()`를 함께 사용한다.

Q. Global Error는 무엇인가?
A. 특정 Field가 아니라 Form Object 전체에 대한 Validation Error이다.

Q. Global Error는 어떻게 추가하는가?
A. `bindingResult.reject("errorCode", "message")`를 사용한다.

Q. 특정 Field에 Business Error를 추가하려면?
A. `bindingResult.rejectValue("fieldName", "errorCode", "message")`를 사용한다.

Q. 이메일 중복 오류는 어떻게 처리하는가?
A. Service에서 중복 여부를 확인한 뒤 `bindingResult.rejectValue()`로 Field Error를 추가한다.

Q. Validation 실패 후 Select Option이 사라지는 이유는?
A. 실패 View 반환 전에 Option 목록 Model Attribute를 다시 추가하지 않았기 때문이다.

Q. Create Form GET에서는 무엇을 하는가?
A. 빈 Form Object를 Model에 담고 Form View를 반환한다.

Q. Create Form POST에서는 무엇을 하는가?
A. Form Binding, Validation, Service 호출, Redirect를 처리한다.

Q. Update Form GET에서는 무엇을 하는가?
A. 기존 데이터를 조회한 뒤 Update Form Object로 변환해 Model에 담는다.

Q. Update Form POST에서 ID는 어떻게 받는가?
A. 보통 `@PathVariable`로 받는다.

Q. Delete 요청은 어떻게 처리하는가?
A. GET Link보다 POST Form으로 처리하는 것을 권장한다.

Q. Delete Form에 CSRF Token이 필요한가?
A. Spring Security CSRF 보호가 활성화된 경우 필요하다.

Q. PRG Pattern이란?
A. POST 성공 후 Redirect하여 GET 화면을 다시 렌더링하는 패턴이다.

Q. PRG Pattern을 사용하는 이유는?
A. 새로고침 시 POST 재전송과 중복 등록을 방지하기 위해서이다.

Q. Flash Attribute는 무엇인가?
A. Redirect 이후 한 번만 사용할 데이터를 전달하는 기능이다.

Q. Form Binding 검수 핵심은?
A. `th:object`, `th:field`, `@ModelAttribute`, `@Valid`, `BindingResult`, Error View 반환 흐름을 확인하는 것이다.

Q. Validation 검수 핵심은?
A. `BindingResult` 위치, 실패 시 같은 View 반환, `th:errors` 출력 여부를 확인하는 것이다.
