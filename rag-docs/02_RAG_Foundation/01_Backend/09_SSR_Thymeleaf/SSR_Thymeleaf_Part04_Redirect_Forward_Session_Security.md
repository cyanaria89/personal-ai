# SSR Thymeleaf Part04 - Redirect Forward Session Security

---

# 1. Redirect Core

## 1.1 Redirect Definition

### [개념]

Redirect는 서버가 Browser에게 새로운 URL로 다시 요청하라고 지시하는 응답 방식이다.

Spring MVC SSR에서는 View Name 앞에 `redirect:` prefix를 붙여 Redirect를 수행한다.

```text
POST /admin/users
→ Controller
→ return "redirect:/admin/users"
→ Browser receives 302
→ Browser requests GET /admin/users
→ Render List Page
```

---

### [핵심]

- Redirect는 Browser가 새로운 요청을 다시 보내는 방식이다.
- Spring MVC에서는 `redirect:/path` 형식을 사용한다.
- Redirect 후 기존 Request Scope 데이터는 사라진다.
- POST 성공 후 Redirect는 PRG Pattern의 핵심이다.
- 등록 / 수정 / 삭제 성공 후 Redirect를 권장한다.
- Validation 실패 시 Redirect하지 않는다.
- Redirect 성공 메시지는 Flash Attribute로 전달할 수 있다.

---

### [실무]

등록 성공 후 Redirect:

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

Redirect Flow:

```text
POST Submit
→ Success
→ redirect:/admin/users
→ GET /admin/users
→ List Page Rendering
```

권장 사용:

```text
Create Success
→ redirect:/admin/users

Update Success
→ redirect:/admin/users/{id}

Delete Success
→ redirect:/admin/users
```

비권장 사용:

```text
Validation Fail
→ redirect:/admin/users/new

POST Success
→ return "admin/users/list"
```

---

### [FAQ]

Q. Redirect란?

A.
Browser에게 다른 URL로 다시 요청하라고 지시하는 응답 방식이다.

Q. Spring MVC에서 Redirect는 어떻게 작성하는가?

A.
`return "redirect:/path"` 형식으로 작성한다.

Q. POST 성공 후 Redirect를 사용하는 이유는?

A.
새로고침 시 중복 Submit을 방지하고 PRG Pattern을 적용하기 위해서이다.

Q. Validation 실패 시 Redirect해도 되는가?

A.
권장하지 않는다.
BindingResult와 입력값이 사라질 수 있다.

---

# 2. PRG Pattern

## 2.1 Post Redirect Get

### [개념]

PRG(Post Redirect Get) Pattern은 POST 요청 처리 성공 후 View를 직접 반환하지 않고 Redirect로 GET 요청을 유도하는 패턴이다.

중복 등록, 중복 수정, 새로고침 재전송 문제를 줄인다.

```text
POST Submit
→ Server Process
→ Redirect Response
→ GET Request
→ HTML Render
```

---

### [핵심]

- POST 성공 후 GET 화면으로 Redirect한다.
- Browser 새로고침 시 POST 재전송을 방지한다.
- 등록 / 수정 / 삭제 성공 후 사용한다.
- 성공 메시지는 Flash Attribute로 전달한다.
- Validation 실패에는 PRG를 적용하지 않는다.
- Validation 실패 시 같은 Form View를 반환한다.
- PRG는 SSR Form 성공 처리의 기본 패턴이다.

---

### [실무]

PRG 적용 예시:

```java
@PostMapping("/admin/festivals")
public String create(
        @Valid @ModelAttribute("festivalForm") FestivalCreateForm festivalForm,
        BindingResult bindingResult,
        Model model,
        RedirectAttributes redirectAttributes
) {
    if (bindingResult.hasErrors()) {
        model.addAttribute("categories", categoryService.findAll());
        return "admin/festivals/create-form";
    }

    Long festivalId = festivalService.create(festivalForm);
    redirectAttributes.addFlashAttribute("message", "축제가 등록되었습니다.");
    return "redirect:/admin/festivals/" + festivalId;
}
```

PRG 적용 위치:

```text
POST /admin/festivals
→ create success
→ redirect:/admin/festivals/{id}
→ GET /admin/festivals/{id}
→ detail page
```

성공 / 실패 분기:

```text
POST Validation Fail
→ Same Form View

POST Success
→ Redirect GET View
```

---

### [FAQ]

Q. PRG Pattern이란?

A.
POST 성공 후 Redirect로 GET 화면을 다시 요청하게 만드는 패턴이다.

Q. PRG Pattern의 목적은?

A.
새로고침으로 인한 중복 Submit을 방지하는 것이다.

Q. Validation 실패 시 PRG를 쓰는가?

A.
아니다. Validation 실패 시에는 같은 Form View를 반환한다.

---

# 3. RedirectAttributes

## 3.1 Flash Attribute

### [개념]

Flash Attribute는 Redirect 이후 한 번만 사용할 데이터를 전달하는 Spring MVC 기능이다.

성공 메시지, 안내 메시지, 삭제 완료 메시지처럼 Redirect 후 View에서 잠깐 보여줄 데이터에 사용한다.

```text
POST
→ redirectAttributes.addFlashAttribute("message", "저장 완료")
→ Redirect
→ GET View
→ ${message}
→ Flash Attribute 소멸
```

---

### [핵심]

- `RedirectAttributes`는 Redirect 시 데이터 전달에 사용한다.
- `addFlashAttribute()`는 Redirect 이후 한 번만 유지된다.
- Flash Attribute는 내부적으로 Flash Scope를 사용한다.
- 성공 메시지 전달에 적합하다.
- Validation Error 전달에는 권장하지 않는다.
- Validation Error는 `BindingResult`로 처리한다.
- 대용량 객체나 장기 상태 저장에 사용하지 않는다.

---

### [실무]

Controller:

```java
@PostMapping("/admin/users/{id}/delete")
public String delete(
        @PathVariable Long id,
        RedirectAttributes redirectAttributes
) {
    userService.delete(id);
    redirectAttributes.addFlashAttribute("message", "사용자가 삭제되었습니다.");
    return "redirect:/admin/users";
}
```

Template:

```html
<div th:if="${message}" class="alert alert-success">
  <span th:text="${message}">message</span>
</div>
```

권장 사용:

```text
Create Success Message
Update Success Message
Delete Success Message
Password Change Success Message
Logout Message
```

비권장 사용:

```text
Validation Field Error
BindingResult Error
Large Object
Long-lived State
Sensitive Data
```

---

### [FAQ]

Q. Flash Attribute란?

A.
Redirect 이후 한 번만 사용할 데이터를 전달하는 기능이다.

Q. Flash Attribute는 언제 사용하는가?

A.
등록, 수정, 삭제 성공 메시지 전달에 자주 사용한다.

Q. Validation Error를 Flash Attribute로 전달해도 되는가?

A.
권장하지 않는다. Validation Error는 BindingResult로 처리하고 같은 Form View를 반환한다.

---

## 3.2 Redirect Query Parameter

### [개념]

Redirect Query Parameter는 Redirect URL에 Query Parameter를 포함하여 GET 요청으로 데이터를 전달하는 방식이다.

검색 조건, 페이지 번호, 간단한 상태값 유지에 사용할 수 있다.

```text
redirect:/admin/users?page=1&keyword=kim
```

---

### [핵심]

- Query Parameter는 URL에 노출된다.
- 검색 조건 유지에 적합하다.
- 민감 정보 전달에 사용하지 않는다.
- `RedirectAttributes.addAttribute()`로 Query Parameter를 추가할 수 있다.
- Flash Attribute와 목적이 다르다.
- Query Parameter는 Redirect 이후에도 URL에 남는다.
- Pagination 검색 조건 유지에 자주 사용한다.

---

### [실무]

Controller:

```java
@PostMapping("/admin/users/{id}/activate")
public String activate(
        @PathVariable Long id,
        @RequestParam(defaultValue = "0") int page,
        @RequestParam(required = false) String keyword,
        RedirectAttributes redirectAttributes
) {
    userService.activate(id);

    redirectAttributes.addAttribute("page", page);
    redirectAttributes.addAttribute("keyword", keyword);

    return "redirect:/admin/users";
}
```

Redirect 결과:

```text
/admin/users?page=0&keyword=kim
```

Flash Attribute와 비교:

| Category  | addAttribute        | addFlashAttribute |
| --------- | ------------------- | ----------------- |
| 전달 위치 | URL Query Parameter | Flash Scope       |
| URL 노출  | 노출됨              | 노출 안 됨        |
| 유지 기간 | URL에 남음          | Redirect 후 1회   |
| 적합      | 검색 조건, 페이지   | 성공 메시지       |
| 민감 정보 | 금지                | 제한적 가능       |

---

### [FAQ]

Q. `addAttribute()`는 무엇인가?

A.
Redirect URL에 Query Parameter를 추가하는 기능이다.

Q. `addAttribute()`와 `addFlashAttribute()` 차이는?

A.
`addAttribute()`는 URL에 남고, `addFlashAttribute()`는 Redirect 후 한 번만 유지된다.

Q. 민감 정보를 Query Parameter로 전달해도 되는가?

A.
안 된다. URL에 노출되므로 민감 정보 전달에는 사용하지 않는다.

---

# 4. Forward Core

## 4.1 Forward Definition

### [개념]

Forward는 서버 내부에서 다른 Handler 또는 View로 요청 처리를 넘기는 방식이다.

Browser URL은 변경되지 않고, 동일 Request Scope를 유지한다.

Spring MVC에서는 View Name 앞에 `forward:` prefix를 붙여 사용한다.

```text
Request /old-path
→ Controller
→ return "forward:/new-path"
→ Server Internal Forward
→ Browser URL unchanged
```

---

### [핵심]

- Forward는 서버 내부 이동이다.
- Browser는 새로운 요청을 보내지 않는다.
- Browser URL은 변경되지 않는다.
- Request Scope가 유지된다.
- `forward:/path` 형식을 사용한다.
- PRG Pattern에는 Redirect가 적합하다.
- Form Submit 성공 처리에는 Forward보다 Redirect를 권장한다.

---

### [실무]

Forward 예시:

```java
@GetMapping("/legacy/users")
public String legacyUsers() {
    return "forward:/admin/users";
}
```

Forward Flow:

```text
GET /legacy/users
→ forward:/admin/users
→ 내부적으로 /admin/users Handler 처리
→ Browser URL: /legacy/users
```

Forward 적합 사례:

```text
Legacy URL Compatibility
Internal Routing
Request Scope 유지 필요
Fallback View 연결
```

Forward 비권장 사례:

```text
POST Success
Create / Update / Delete Success
중복 Submit 방지 필요 상황
URL 변경이 필요한 상황
```

---

### [FAQ]

Q. Forward란?

A.
서버 내부에서 다른 Handler 또는 View로 요청 처리를 넘기는 방식이다.

Q. Forward하면 Browser URL이 바뀌는가?

A.
바뀌지 않는다.

Q. POST 성공 후 Forward를 사용해도 되는가?

A.
권장하지 않는다. POST 성공 후에는 Redirect로 PRG Pattern을 적용하는 것이 좋다.

---

## 4.2 Redirect vs Forward

### [개념]

Redirect와 Forward는 요청 흐름과 Browser URL 변경 여부가 다르다.

Redirect는 Browser에게 새 요청을 보내게 하고, Forward는 서버 내부에서 요청을 넘긴다.

| Category                | Redirect     | Forward      |
| ----------------------- | ------------ | ------------ |
| Prefix                  | `redirect:`  | `forward:`   |
| Browser Request         | 새 요청 발생 | 새 요청 없음 |
| URL 변경                | 변경됨       | 변경 안 됨   |
| Request Scope           | 사라짐       | 유지됨       |
| POST Success            | 권장         | 비권장       |
| Legacy Internal Routing | 가능         | 가능         |

---

### [핵심]

- Redirect는 Client Side 재요청이다.
- Forward는 Server Side 내부 전달이다.
- Redirect는 URL이 변경된다.
- Forward는 URL이 유지된다.
- Redirect는 Request Scope가 유지되지 않는다.
- Forward는 Request Scope가 유지된다.
- Form Submit 성공 후에는 Redirect를 사용한다.
- 내부 경로 전달에는 Forward를 사용할 수 있다.

---

### [실무]

선택 기준:

```text
POST 성공 후 목록 이동
→ Redirect

중복 Submit 방지
→ Redirect

성공 메시지 1회 표시
→ Redirect + Flash Attribute

Legacy URL 내부 연결
→ Forward 가능

Request Attribute 유지 필요
→ Forward 가능

Browser URL 변경 필요
→ Redirect
```

잘못된 예:

```java
@PostMapping("/admin/users")
public String create(@ModelAttribute UserCreateForm form) {
    userService.create(form);
    return "forward:/admin/users";
}
```

문제:

```text
POST Success 후 Forward
→ 새로고침 시 POST 재전송 가능
→ PRG Pattern 미적용
```

올바른 예:

```java
@PostMapping("/admin/users")
public String create(@ModelAttribute UserCreateForm form) {
    userService.create(form);
    return "redirect:/admin/users";
}
```

---

### [FAQ]

Q. Redirect와 Forward의 가장 큰 차이는?

A.
Redirect는 Browser가 새 요청을 보내고, Forward는 서버 내부에서 요청을 넘긴다.

Q. URL이 바뀌는 것은 Redirect인가 Forward인가?

A.
Redirect는 URL이 바뀌고 Forward는 URL이 유지된다.

Q. Form POST 성공 후에는 무엇을 써야 하는가?

A.
Redirect를 사용한다.

---

# 5. Session Core

## 5.1 HttpSession

### [개념]

`HttpSession`은 여러 Request 사이에서 사용자별 상태를 유지하기 위한 서버 측 저장 공간이다.

SSR Thymeleaf에서는 로그인 사용자 정보, 임시 사용자 상태, 간단한 View 상태에 사용할 수 있다.

```text
Login Success
→ session.setAttribute("loginUser", loginUser)
→ Next Request
→ session.getAttribute("loginUser")
→ Render User View
```

---

### [핵심]

- Session은 사용자별 서버 측 상태 저장 공간이다.
- Browser는 Session ID Cookie를 가진다.
- 서버는 Session ID를 기준으로 사용자 상태를 찾는다.
- 로그인 사용자 정보 저장에 사용할 수 있다.
- 민감 정보 전체를 Session에 과도하게 저장하지 않는다.
- Session 남용은 확장성과 유지보수성을 떨어뜨린다.
- Spring Security 사용 시 직접 Session 관리보다 SecurityContext 활용을 우선 검토한다.

---

### [실무]

로그인 성공 시 Session 저장:

```java
@PostMapping("/login")
public String login(
        @ModelAttribute LoginForm loginForm,
        HttpSession session
) {
    LoginUser loginUser = authService.login(loginForm);
    session.setAttribute("loginUser", loginUser);
    return "redirect:/";
}
```

View에서 Session Attribute 사용:

```html
<div th:if="${session.loginUser != null}">
  <span th:text="${session.loginUser.name}">username</span>
</div>
```

권장:

```text
Session에는 최소 사용자 식별 정보 저장
→ userId, username, role summary

비권장:
→ password
→ token raw value
→ 대용량 객체
→ 변경 가능성이 큰 Entity 전체
```

Spring Security 사용 시:

```text
Authentication
→ SecurityContext
→ @AuthenticationPrincipal
→ 필요한 표시 정보만 Model 전달
```

---

### [FAQ]

Q. HttpSession이란?

A.
여러 Request 사이에서 사용자별 상태를 유지하는 서버 측 저장 공간이다.

Q. Session에는 무엇을 저장하는가?

A.
최소한의 로그인 사용자 식별 정보만 저장하는 것을 권장한다.

Q. Session에 Entity 전체를 저장해도 되는가?

A.
권장하지 않는다. 변경 불일치, 메모리 사용, 직렬화 문제가 생길 수 있다.

Q. Spring Security 사용 시 직접 Session을 관리해야 하는가?

A.
보통 SecurityContext와 `@AuthenticationPrincipal` 활용을 우선 검토한다.

---

## 5.2 Session Attribute

### [개념]

Session Attribute는 Session에 저장된 이름 기반 데이터이다.

Thymeleaf Template에서는 `${session.attributeName}` 형식으로 접근할 수 있다.

```html
<span th:text="${session.loginUser.name}">username</span>
```

---

### [핵심]

- Session Attribute는 Request 간 유지된다.
- Template에서 `${session.name}` 형태로 접근 가능하다.
- 로그인 상태 표시, 사용자 메뉴 표시 등에 사용한다.
- Null 가능성을 고려해 `th:if`를 함께 사용한다.
- 중요한 권한 검증은 Template이 아니라 서버에서 처리한다.
- Session Attribute에 민감 정보를 직접 출력하지 않는다.

---

### [실무]

Login User Menu:

```html
<div th:if="${session.loginUser != null}">
  <span th:text="${session.loginUser.name}">사용자</span>
  <a th:href="@{/logout}">로그아웃</a>
</div>

<div th:unless="${session.loginUser != null}">
  <a th:href="@{/login}">로그인</a>
</div>
```

Null Safe Pattern:

```html
<span th:if="${session.loginUser != null}" th:text="${session.loginUser.email}">
  email
</span>
```

권한 체크 주의:

```text
Template에서 버튼 숨김
→ UI 표시 제어

Server에서 Authorization 검증
→ 실제 보안 제어
```

---

### [FAQ]

Q. Thymeleaf에서 Session 값은 어떻게 접근하는가?

A.
`${session.attributeName}` 형식으로 접근한다.

Q. `${session.loginUser}`가 null일 수 있는가?

A.
가능하다. `th:if`로 Null Check를 하는 것이 좋다.

Q. Template에서 버튼을 숨기면 보안 처리가 끝나는가?

A.
아니다. 실제 권한 검증은 Controller, Service, Security Layer에서 처리해야 한다.

---

# 6. Authentication View

## 6.1 Login Page

### [개념]

Login Page는 사용자 인증 정보를 입력받는 SSR 화면이다.

Spring Security를 사용하는 경우 Login Processing URL, Parameter Name, CSRF Token, Error Parameter를 함께 고려해야 한다.

```text
GET /login
→ Render Login Form

POST /login
→ Spring Security Authentication Filter
→ Success Redirect or Failure Redirect
```

---

### [핵심]

- Login Page는 보통 `GET /login`으로 렌더링한다.
- Login Processing은 Spring Security Filter가 처리할 수 있다.
- Form `action`은 Security 설정의 Login Processing URL과 일치해야 한다.
- 기본 로그인 Parameter 이름은 `username`, `password`이다.
- CSRF가 활성화된 경우 POST Form에 CSRF Token이 필요하다.
- 로그인 실패 메시지는 Query Parameter 또는 Flash Attribute로 표시할 수 있다.
- 로그인 성공 후 Redirect URL 정책을 명확히 한다.

---

### [실무]

Security 설정 예시:

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http
        .formLogin(form -> form
            .loginPage("/login")
            .loginProcessingUrl("/login")
            .defaultSuccessUrl("/", true)
            .failureUrl("/login?error")
            .permitAll()
        );

    return http.build();
}
```

Login Controller:

```java
@GetMapping("/login")
public String loginPage() {
    return "auth/login";
}
```

Login Template:

```html
<form th:action="@{/login}" method="post">
  <input type="text" name="username" placeholder="email" />
  <input type="password" name="password" placeholder="password" />

  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />

  <button type="submit">로그인</button>
</form>

<p th:if="${param.error}" class="field-error">
  로그인 정보가 올바르지 않습니다.
</p>
```

---

### [FAQ]

Q. Login Page는 누가 렌더링하는가?

A.
`@Controller`가 GET `/login` 요청을 받아 Thymeleaf Template을 렌더링한다.

Q. Login POST는 누가 처리하는가?

A.
Spring Security 설정을 사용하면 Authentication Filter가 처리한다.

Q. Login Form의 action은 무엇과 일치해야 하는가?

A.
Spring Security의 `loginProcessingUrl()`과 일치해야 한다.

Q. Spring Security 기본 로그인 Parameter 이름은?

A.
`username`, `password`이다.

---

## 6.2 Logout

### [개념]

Logout은 인증 상태를 종료하고 Session 또는 SecurityContext를 정리하는 처리이다.

Spring Security 사용 시 Logout URL, Method, CSRF 설정을 고려해야 한다.

```text
POST /logout
→ Spring Security Logout Filter
→ Session Invalidate
→ SecurityContext Clear
→ Redirect
```

---

### [핵심]

- Spring Security 기본 Logout은 보통 `/logout`으로 처리한다.
- CSRF 활성화 시 Logout은 POST를 사용하는 것이 일반적이다.
- Logout 후 Session이 무효화된다.
- SecurityContext가 정리된다.
- Logout 성공 후 Redirect URL을 설정한다.
- Logout Link보다 POST Form을 권장한다.
- Logout Form에도 CSRF Token이 필요할 수 있다.

---

### [실무]

Security 설정:

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http
        .logout(logout -> logout
            .logoutUrl("/logout")
            .logoutSuccessUrl("/login?logout")
            .invalidateHttpSession(true)
            .clearAuthentication(true)
        );

    return http.build();
}
```

Logout Template:

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

Logout Message:

```html
<p th:if="${param.logout}" class="alert">로그아웃되었습니다.</p>
```

---

### [FAQ]

Q. Logout은 GET Link로 처리해도 되는가?

A.
CSRF 보호 관점에서 POST Form을 권장한다.

Q. Logout 후 무엇이 정리되는가?

A.
Session과 SecurityContext가 정리된다.

Q. Logout 성공 후 메시지는 어떻게 표시하는가?

A.
`/login?logout` 같은 Query Parameter를 사용하거나 Flash Attribute를 사용할 수 있다.

---

# 7. CSRF

## 7.1 CSRF Token

### [개념]

CSRF(Cross-Site Request Forgery)는 사용자의 인증 상태를 악용해 원치 않는 요청을 보내게 만드는 공격이다.

Spring Security에서 CSRF 보호가 활성화된 경우, 상태 변경 POST Form에는 CSRF Token이 필요하다.

```text
HTML Form
→ CSRF Hidden Input 포함
→ POST Submit
→ Spring Security CSRF Filter 검증
→ Valid Request
```

---

### [핵심]

- CSRF는 인증된 사용자의 상태 변경 요청을 악용하는 공격이다.
- Spring Security는 CSRF Token으로 요청을 검증한다.
- SSR Form POST에는 CSRF Hidden Input이 필요하다.
- Token이 없거나 틀리면 403 Forbidden이 발생할 수 있다.
- GET 요청에는 상태 변경 작업을 넣지 않는다.
- Delete / Update / Create / Logout Form은 CSRF 검증 대상이 될 수 있다.

---

### [실무]

CSRF Hidden Input:

```html
<form th:action="@{/admin/users}" method="post">
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />

  <input type="text" name="name" />
  <button type="submit">저장</button>
</form>
```

공통 Fragment로 분리:

```html
<input
  th:fragment="csrf"
  type="hidden"
  th:name="${_csrf.parameterName}"
  th:value="${_csrf.token}"
/>
```

사용:

```html
<form th:action="@{/admin/users}" method="post">
  <input th:replace="~{fragments/security :: csrf}" />
  <button type="submit">저장</button>
</form>
```

---

### [FAQ]

Q. CSRF란?

A.
인증된 사용자의 권한을 악용해 원치 않는 상태 변경 요청을 보내게 하는 공격이다.

Q. CSRF Token이 없으면 어떻게 되는가?

A.
Spring Security에서 403 Forbidden이 발생할 수 있다.

Q. 어떤 Form에 CSRF Token이 필요한가?

A.
생성, 수정, 삭제, 로그아웃처럼 상태를 변경하는 POST Form에 필요할 수 있다.

---

## 7.2 CSRF Troubleshooting

### [개념]

CSRF 오류는 Spring Security가 상태 변경 요청의 CSRF Token을 검증하지 못했을 때 발생한다.

주로 POST Form, Logout Form, Delete Form에서 403 Forbidden으로 나타난다.

---

### [핵심]

자주 발생하는 원인:

- POST Form에 CSRF Hidden Input 누락
- Logout Form에 CSRF Token 누락
- Delete Form에 CSRF Token 누락
- AJAX 요청에 CSRF Header 누락
- Template에서 `_csrf` 접근 불가
- CSRF 비활성화 여부 혼동
- GET Link로 Delete 요청 처리

---

### [실무]

문제 상황:

```text
POST /admin/users
→ 403 Forbidden
```

점검 순서:

```text
Spring Security CSRF 활성화 여부 확인
→ Form method 확인
→ CSRF Hidden Input 존재 여부 확인
→ _csrf Model Attribute 접근 여부 확인
→ Token Name / Token Value 렌더링 확인
→ Browser Network Payload 확인
```

POST Form 검수:

```html
<input
  type="hidden"
  th:name="${_csrf.parameterName}"
  th:value="${_csrf.token}"
/>
```

삭제 버튼 검수:

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

---

### [FAQ]

Q. POST 요청에서 403 Forbidden이 발생하는 이유는?

A.
CSRF Token이 없거나 잘못되었을 가능성이 높다.

Q. Logout에서 403이 발생하는 이유는?

A.
CSRF 활성화 상태에서 POST Logout Form에 Token이 없을 수 있다.

Q. CSRF 오류는 어디서 확인하는가?

A.
Browser Network Payload와 Spring Security 로그를 확인한다.

---

# 8. Authorization View

## 8.1 Role Based View Rendering

### [개념]

Role Based View Rendering은 사용자의 권한에 따라 화면 요소를 조건부로 표시하는 방식이다.

Spring Security + Thymeleaf 환경에서는 `sec:authorize`를 사용할 수 있다.

```html
<div sec:authorize="hasRole('ADMIN')">Admin Menu</div>
```

---

### [핵심]

- `sec:authorize`는 권한 기반 View 표시 제어에 사용한다.
- Thymeleaf Spring Security Dialect가 필요하다.
- View에서 버튼을 숨기는 것은 UI 제어일 뿐이다.
- 실제 권한 검증은 Security Filter, Controller, Service에서 수행해야 한다.
- Role 이름은 Spring Security 규칙과 일치해야 한다.
- `hasRole('ADMIN')`은 내부적으로 `ROLE_ADMIN`을 확인한다.
- `hasAuthority('ROLE_ADMIN')`는 권한 문자열을 직접 확인한다.

---

### [실무]

Dependency 예시:

```gradle
implementation 'org.thymeleaf.extras:thymeleaf-extras-springsecurity6'
```

Template Namespace:

```html
<html
  xmlns:th="http://www.thymeleaf.org"
  xmlns:sec="https://www.thymeleaf.org/extras/spring-security"
></html>
```

Admin Menu:

```html
<a sec:authorize="hasRole('ADMIN')" th:href="@{/admin}"> 관리자 페이지 </a>
```

Login / Anonymous 분기:

```html
<div sec:authorize="isAuthenticated()">
  <span sec:authentication="name">username</span>
</div>

<a sec:authorize="isAnonymous()" th:href="@{/login}"> 로그인 </a>
```

---

### [FAQ]

Q. `sec:authorize`는 무엇인가?

A.
Spring Security 권한에 따라 Thymeleaf View 요소를 조건부 렌더링하는 속성이다.

Q. `sec:authorize`만 있으면 보안 처리가 끝나는가?

A.
아니다. View 표시 제어일 뿐이고 실제 접근 제어는 서버 보안 계층에서 처리해야 한다.

Q. `hasRole('ADMIN')`은 어떤 권한을 확인하는가?

A.
일반적으로 `ROLE_ADMIN` 권한을 확인한다.

Q. `sec:authorize`가 동작하려면 무엇이 필요한가?

A.
`thymeleaf-extras-springsecurity6` 의존성과 `xmlns:sec` 선언이 필요하다.

---

## 8.2 Authentication Information Rendering

### [개념]

Authentication Information Rendering은 현재 인증된 사용자 정보를 Thymeleaf View에 출력하는 방식이다.

Spring Security Dialect를 사용하면 `sec:authentication`으로 인증 정보를 출력할 수 있다.

```html
<span sec:authentication="name">username</span>
```

---

### [핵심]

- `sec:authentication`은 인증 객체의 정보를 출력한다.
- `name`은 현재 인증 사용자 이름이다.
- Principal 정보에 접근할 수 있다.
- 화면 표시용 정보만 출력한다.
- 민감 정보는 출력하지 않는다.
- 복잡한 사용자 정보는 Controller에서 별도 DTO로 전달할 수 있다.

---

### [실무]

사용자 이름 출력:

```html
<span sec:authentication="name">username</span>
```

권한 기반 표시:

```html
<span sec:authorize="hasRole('ADMIN')">관리자</span>
```

Controller에서 Login User DTO 전달:

```java
@GetMapping("/mypage")
public String myPage(
        @AuthenticationPrincipal CustomUserDetails userDetails,
        Model model
) {
    model.addAttribute("loginUser", userService.getLoginUser(userDetails.getUserId()));
    return "users/mypage";
}
```

Template:

```html
<h1 th:text="${loginUser.name}">name</h1>
<p th:text="${loginUser.email}">email</p>
```

---

### [FAQ]

Q. 현재 로그인한 사용자 이름은 어떻게 출력하는가?

A.
`sec:authentication="name"`을 사용할 수 있다.

Q. Principal의 모든 정보를 View에 출력해도 되는가?

A.
안 된다. 민감 정보는 출력하지 않고 필요한 표시 정보만 사용한다.

Q. 복잡한 사용자 정보는 어떻게 View에 전달하는가?

A.
Controller에서 DTO를 Model에 담아 전달하는 것이 좋다.

---

# 9. Access Control And View Security

## 9.1 View Hiding vs Server Authorization

### [개념]

View Hiding은 버튼, 링크, 메뉴를 화면에서 숨기는 UI 제어이다.

Server Authorization은 실제 요청을 서버에서 허용하거나 차단하는 보안 제어이다.

```text
View Hiding
→ 사용자에게 버튼 숨김

Server Authorization
→ 요청 자체를 검증하고 차단
```

---

### [핵심]

- View Hiding은 보안이 아니다.
- 숨겨진 URL도 직접 요청할 수 있다.
- Controller / Security Layer에서 권한 검증이 필요하다.
- Service에서도 도메인 권한 검증을 수행할 수 있다.
- 관리자 메뉴 숨김과 관리자 URL 차단은 별개이다.
- SSR Template 권한 조건은 UX 개선용으로 사용한다.

---

### [실무]

View Hiding:

```html
<a sec:authorize="hasRole('ADMIN')" th:href="@{/admin/users}"> 사용자 관리 </a>
```

Server Authorization:

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests(auth -> auth
        .requestMatchers("/admin/**").hasRole("ADMIN")
        .anyRequest().permitAll()
    );

    return http.build();
}
```

Service Authorization:

```java
public void deleteUser(Long targetUserId, Long loginUserId) {
    if (!permissionService.canDeleteUser(loginUserId, targetUserId)) {
        throw new AccessDeniedException("삭제 권한이 없습니다.");
    }

    userRepository.deleteById(targetUserId);
}
```

---

### [FAQ]

Q. 버튼을 숨기면 보안 처리가 완료되는가?

A.
아니다. URL 직접 요청을 막기 위해 서버 권한 검증이 필요하다.

Q. `sec:authorize`는 보안인가?

A.
View 표시 제어이다. 실제 보안은 Security 설정과 서버 검증으로 처리해야 한다.

Q. 관리자 페이지 접근 제어는 어디서 해야 하는가?

A.
Spring Security 설정에서 `/admin/**` 접근 권한을 제한해야 한다.

---

# 10. Error Page Security

## 10.1 Authentication Authorization Error Page

### [개념]

Authentication Error Page와 Authorization Error Page는 인증 실패 또는 접근 거부 상황에서 사용자에게 보여주는 SSR 화면이다.

대표 상태는 401 Unauthorized, 403 Forbidden이다.

```text
Unauthenticated Access
→ Login Redirect or 401

Authenticated But Forbidden
→ 403 Error Page
```

---

### [핵심]

- 인증되지 않은 사용자는 Login Page로 Redirect할 수 있다.
- 권한이 부족한 사용자는 403 Page를 보여준다.
- Error Page는 민감한 서버 정보를 노출하지 않는다.
- Stack Trace를 View에 출력하지 않는다.
- 사용자에게 필요한 행동만 안내한다.
- Admin Page 접근 거부와 일반 사용자 접근 거부 메시지를 구분할 수 있다.

---

### [실무]

Security Access Denied 설정:

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    http
        .exceptionHandling(exception -> exception
            .accessDeniedPage("/error/403")
        );

    return http.build();
}
```

Error Controller:

```java
@GetMapping("/error/403")
public String accessDenied() {
    return "error/403";
}
```

403 Template:

```html
<h1>접근 권한이 없습니다.</h1>
<p>이 페이지에 접근할 권한이 없습니다.</p>
<a th:href="@{/}">홈으로 이동</a>
```

비권장:

```text
Exception Stack Trace 출력
Security Rule 상세 출력
Internal URL 구조 노출
Database Error Message 출력
```

---

### [FAQ]

Q. 403 Error는 언제 발생하는가?

A.
인증은 되었지만 요청한 리소스에 접근할 권한이 없을 때 발생한다.

Q. Error Page에 Stack Trace를 보여줘도 되는가?

A.
안 된다. 내부 정보 노출 위험이 있다.

Q. 접근 거부 화면은 어떻게 연결하는가?

A.
Spring Security의 `accessDeniedPage()` 또는 Exception Handling으로 연결할 수 있다.

---

# 11. Common Mistakes

## 11.1 Redirect Forward Session Security Mistakes

### [개념]

Redirect, Forward, Session, Security View 실수는 SSR 흐름과 보안 책임을 혼동할 때 자주 발생한다.

---

### [핵심]

자주 발생하는 실수:

- POST 성공 후 View 직접 반환
- POST 성공 후 Forward 사용
- Validation 실패 후 Redirect 사용
- Flash Attribute로 Validation Error 처리
- Query Parameter로 민감 정보 전달
- Session에 Entity 전체 저장
- Session에 Password 또는 Token Raw Value 저장
- Logout을 GET Link로 처리
- POST Form에 CSRF Token 누락
- Delete를 GET Link로 처리
- `sec:authorize`만 믿고 서버 권한 검증 생략
- 관리자 URL 접근 제어 누락
- Error Page에 Stack Trace 출력
- Authentication 정보 과다 출력

---

### [실무]

잘못된 예:

```java
@PostMapping("/admin/users")
public String create(@ModelAttribute UserCreateForm form) {
    userService.create(form);
    return "admin/users/list";
}
```

문제:

```text
POST 성공 후 View 직접 반환
→ 새로고침 시 POST 재전송 가능
→ PRG Pattern 미적용
```

올바른 예:

```java
@PostMapping("/admin/users")
public String create(@ModelAttribute UserCreateForm form) {
    userService.create(form);
    return "redirect:/admin/users";
}
```

잘못된 예:

```html
<a th:href="@{/admin/users/{id}/delete(id=${user.id})}"> 삭제 </a>
```

올바른 예:

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

---

### [FAQ]

Q. POST 성공 후 View를 직접 반환하면 안 되는 이유는?

A.
새로고침 시 POST가 재전송되어 중복 등록이 발생할 수 있기 때문이다.

Q. Delete를 GET Link로 처리하면 안 되는 이유는?

A.
GET은 조회용이어야 하며 상태 변경 요청은 POST Form으로 처리하는 것이 안전하다.

Q. `sec:authorize`만으로 관리자 기능을 보호할 수 있는가?

A.
아니다. 서버의 Security 설정과 권한 검증이 반드시 필요하다.

---

# 12. Troubleshooting

## 12.1 Redirect Forward Session Security Troubleshooting

### [개념]

Troubleshooting은 SSR 흐름, Redirect 데이터 전달, Session 상태, Security Form 오류를 원인별로 점검하는 과정이다.

---

### [핵심]

문제별 주요 원인:

- Redirect 후 메시지 없음 → Flash Attribute 누락 또는 이름 불일치
- Validation Error 사라짐 → Redirect 사용
- POST 후 새로고침 중복 등록 → PRG Pattern 미적용
- Forward 후 URL 이상 → Forward는 Browser URL을 변경하지 않음
- 로그인 사용자 표시 안 됨 → Session Attribute 또는 Security Principal 접근 오류
- POST 403 → CSRF Token 누락
- Logout 403 → Logout Form CSRF Token 누락
- 관리자 버튼은 숨겨졌지만 URL 접근 가능 → 서버 권한 설정 누락
- `sec:authorize` 미동작 → 의존성 또는 namespace 누락

---

### [실무]

점검 Flow:

```text
POST 요청 문제
→ Validation 실패인지 성공인지 확인
→ 실패면 Same View Return 확인
→ 성공이면 Redirect 확인
→ CSRF Token 확인
→ Flash Attribute 확인
```

Security View 점검 Flow:

```text
sec:* 속성 사용
→ thymeleaf-extras-springsecurity6 의존성 확인
→ xmlns:sec 선언 확인
→ Authentication 존재 여부 확인
→ Role 이름 확인
→ Server Security Rule 확인
```

CSRF 403 점검 Flow:

```text
403 발생
→ 요청 Method 확인
→ 상태 변경 요청인지 확인
→ CSRF 활성화 여부 확인
→ Hidden Input 렌더링 확인
→ Payload에 CSRF Parameter 포함 여부 확인
```

---

### [FAQ]

Q. Redirect 후 성공 메시지가 안 보이는 이유는?

A.
`addFlashAttribute()`를 사용하지 않았거나 Template의 Attribute 이름이 다를 수 있다.

Q. Validation Error가 Redirect 후 사라지는 이유는?

A.
Redirect로 인해 BindingResult가 유지되지 않기 때문이다.

Q. `sec:authorize`가 동작하지 않는 이유는?

A.
Spring Security Thymeleaf Extras 의존성 또는 `xmlns:sec` 선언이 누락되었을 수 있다.

---

# 13. Review Checklist

## 13.1 Redirect Forward Session Security Review Checklist

### [개념]

Review Checklist는 Agent가 SSR Redirect, Forward, Session, Security View 코드를 검수하기 위한 기준이다.

---

### [핵심]

Redirect / Forward 검수:

- POST 성공 후 Redirect 사용 여부
- Validation 실패 시 같은 View 반환 여부
- Forward를 POST 성공 처리에 사용하지 않았는지 여부
- Redirect URL이 명확한지 여부
- Query Parameter에 민감 정보가 없는지 여부
- Flash Attribute 사용 목적이 적절한지 여부

Session 검수:

- Session 저장 데이터 최소화 여부
- Entity 전체 Session 저장 여부
- Password / Token Raw Value 저장 여부
- Session Attribute Null Check 여부
- Spring Security 사용 시 SecurityContext 활용 여부

Security View 검수:

- Login Form Action과 `loginProcessingUrl` 일치 여부
- Login Form Parameter 이름 일치 여부
- Logout POST Form 사용 여부
- CSRF Token 포함 여부
- `sec:authorize` 사용 시 의존성 및 namespace 확인
- View Hiding과 Server Authorization 분리 여부
- `/admin/**` 서버 접근 제어 여부
- Error Page 내부 정보 노출 여부

---

### [실무]

검수 Flow:

```text
Form Submit 흐름 확인
→ POST 성공 Redirect 확인
→ Validation 실패 Same View 확인
→ Flash Attribute 확인
→ CSRF Token 확인
→ Session 저장 데이터 확인
→ View 권한 표시 확인
→ Server Authorization 확인
→ Error Page 정보 노출 확인
```

---

### [FAQ]

Q. Redirect 검수 핵심은?

A.
POST 성공 후 Redirect를 사용하고 Validation 실패 시 Redirect하지 않는지 확인하는 것이다.

Q. Session 검수 핵심은?

A.
최소 정보만 저장하고 Entity, Password, Token Raw Value를 저장하지 않는지 확인하는 것이다.

Q. Security View 검수 핵심은?

A.
CSRF Token, Logout POST Form, `sec:authorize`, 서버 권한 검증을 함께 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Spring MVC Redirect는 어떻게 작성하는가?
A. `return "redirect:/path"` 형식으로 작성한다.

Q. Redirect란?
A. Browser에게 다른 URL로 새 요청을 보내게 하는 응답 방식이다.

Q. POST 성공 후 Redirect를 사용하는 이유는?
A. 새로고침 시 중복 Submit을 방지하고 PRG Pattern을 적용하기 위해서이다.

Q. PRG Pattern이란?
A. POST 성공 후 Redirect로 GET 화면을 다시 요청하게 만드는 패턴이다.

Q. Validation 실패 시 Redirect하면 안 되는 이유는?
A. BindingResult와 입력값이 사라져 Error Message를 표시하기 어렵기 때문이다.

Q. Flash Attribute란?
A. Redirect 이후 한 번만 사용할 데이터를 전달하는 Spring MVC 기능이다.

Q. Flash Attribute는 언제 사용하는가?
A. 등록, 수정, 삭제 성공 메시지 전달에 사용한다.

Q. `addAttribute()`와 `addFlashAttribute()` 차이는?
A. `addAttribute()`는 Query Parameter로 URL에 남고, `addFlashAttribute()`는 Redirect 후 한 번만 유지된다.

Q. Query Parameter로 민감 정보를 전달해도 되는가?
A. 안 된다. URL에 노출되므로 사용하지 않는다.

Q. Forward란?
A. 서버 내부에서 다른 Handler 또는 View로 요청 처리를 넘기는 방식이다.

Q. Spring MVC Forward는 어떻게 작성하는가?
A. `return "forward:/path"` 형식으로 작성한다.

Q. Redirect와 Forward 차이는?
A. Redirect는 Browser가 새 요청을 보내고 URL이 바뀌며, Forward는 서버 내부 이동이고 URL이 유지된다.

Q. POST 성공 후 Forward를 사용해도 되는가?
A. 권장하지 않는다. POST 성공 후에는 Redirect를 사용한다.

Q. HttpSession이란?
A. 여러 Request 사이에서 사용자별 상태를 유지하는 서버 측 저장 공간이다.

Q. Thymeleaf에서 Session 값은 어떻게 접근하는가?
A. `${session.attributeName}` 형식으로 접근한다.

Q. Session에 Entity 전체를 저장해도 되는가?
A. 권장하지 않는다. 최소한의 사용자 식별 정보만 저장하는 것이 좋다.

Q. Session에 Password를 저장해도 되는가?
A. 안 된다. 민감 정보는 Session에 저장하지 않는다.

Q. Login Page는 어떤 Controller가 렌더링하는가?
A. `@Controller`가 GET `/login` 요청을 받아 Thymeleaf Template을 렌더링한다.

Q. Spring Security Login POST는 누가 처리하는가?
A. Authentication Filter가 처리한다.

Q. Login Form Action은 무엇과 일치해야 하는가?
A. Spring Security의 `loginProcessingUrl()`과 일치해야 한다.

Q. Spring Security 기본 로그인 Parameter 이름은?
A. `username`, `password`이다.

Q. Logout은 GET Link로 처리해도 되는가?
A. CSRF 보호 관점에서 POST Form을 권장한다.

Q. Logout 후 무엇이 정리되는가?
A. Session과 SecurityContext가 정리된다.

Q. CSRF란?
A. 인증된 사용자의 권한을 악용해 원치 않는 상태 변경 요청을 보내게 하는 공격이다.

Q. SSR POST Form에 CSRF Token이 필요한 이유는?
A. Spring Security CSRF Filter가 상태 변경 요청의 유효성을 검증하기 때문이다.

Q. CSRF Token이 없으면 어떻게 되는가?
A. 403 Forbidden이 발생할 수 있다.

Q. CSRF Hidden Input은 어떻게 작성하는가?
A. `th:name="${_csrf.parameterName}"`, `th:value="${_csrf.token}"` 형태로 작성한다.

Q. Delete 요청은 GET Link로 처리해도 되는가?
A. 권장하지 않는다. POST Form으로 처리하는 것이 안전하다.

Q. `sec:authorize`는 무엇인가?
A. Spring Security 권한에 따라 Thymeleaf View 요소를 조건부 렌더링하는 속성이다.

Q. `sec:authorize`를 사용하려면 무엇이 필요한가?
A. `thymeleaf-extras-springsecurity6` 의존성과 `xmlns:sec` 선언이 필요하다.

Q. `hasRole('ADMIN')`은 어떤 권한을 확인하는가?
A. 일반적으로 `ROLE_ADMIN` 권한을 확인한다.

Q. `sec:authorize`만으로 보안 처리가 완료되는가?
A. 아니다. 실제 접근 제어는 Spring Security 설정과 서버 검증으로 처리해야 한다.

Q. 현재 로그인 사용자 이름은 어떻게 출력하는가?
A. `sec:authentication="name"`을 사용할 수 있다.

Q. View Hiding과 Server Authorization 차이는?
A. View Hiding은 UI 표시 제어이고 Server Authorization은 실제 요청 접근 제어이다.

Q. 관리자 URL 접근 제어는 어디서 해야 하는가?
A. Spring Security 설정에서 `/admin/**`에 대한 권한을 제한해야 한다.

Q. 403 Error Page는 언제 사용되는가?
A. 인증은 되었지만 접근 권한이 없을 때 사용된다.

Q. Error Page에 Stack Trace를 보여줘도 되는가?
A. 안 된다. 내부 정보 노출 위험이 있다.

Q. POST 요청에서 403 Forbidden이 발생하는 이유는?
A. CSRF Token 누락 또는 잘못된 Token일 가능성이 높다.

Q. Redirect 후 성공 메시지가 안 보이는 이유는?
A. `addFlashAttribute()` 누락 또는 Template Attribute 이름 불일치일 수 있다.

Q. `sec:authorize`가 동작하지 않는 이유는?
A. Spring Security Thymeleaf Extras 의존성 또는 `xmlns:sec` 선언이 누락되었을 수 있다.

Q. Redirect Forward Security 검수 핵심은?
A. POST 성공 Redirect, Validation 실패 Same View, CSRF Token, Session 최소화, Server Authorization을 확인하는 것이다.
