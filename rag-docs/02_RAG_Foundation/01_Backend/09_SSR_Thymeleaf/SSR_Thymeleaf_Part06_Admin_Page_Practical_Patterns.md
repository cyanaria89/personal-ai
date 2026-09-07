# SSR Thymeleaf Part06 - Admin Page Practical Patterns

---

# 1. Admin Page Core

## 1.1 Admin Page Definition

### [개념]

Admin Page는 서비스 운영자, 관리자, 내부 담당자가 데이터를 조회, 생성, 수정, 삭제, 검색, 관리하기 위한 Backoffice 화면이다.

SSR Thymeleaf는 Admin Page처럼 Form, Table, Search, Pagination 중심의 화면에 적합하다.

```text
Admin Request
→ @Controller
→ Service Query / Command
→ Model
→ Thymeleaf Template
→ Admin HTML Page
```

---

### [핵심]

- Admin Page는 CRUD 중심이다.
- SSR Thymeleaf는 Table, Form, Pagination 화면에 적합하다.
- React 수준의 복잡한 Client State가 적은 화면에 유리하다.
- 관리자 권한 검증이 반드시 필요하다.
- View Hiding과 Server Authorization을 분리해야 한다.
- 검색 조건 유지, Pagination, Validation Error 표시가 중요하다.
- 내부 운영 도구라도 보안 검수를 생략하지 않는다.
- Delete, Update, Status Change 같은 상태 변경 요청은 CSRF 검수 대상이다.

---

### [실무]

2026 실무 기준 SSR Thymeleaf Admin Page는 다음 구조에 적합하다.

```text
Admin Dashboard
→ Summary Card
→ List Page
→ Search / Filter
→ Detail Page
→ Create Form
→ Update Form
→ Delete Action
→ Pagination
→ Error Page
```

권장 URL 구조:

```text
/admin
/admin/users
/admin/users/{id}
/admin/users/new
/admin/users/{id}/edit
/admin/users/{id}/delete
```

권장 Controller 분리:

```text
AdminUserViewController
→ SSR View Rendering

UserApiController
→ REST API Response
```

---

### [FAQ]

Q. Admin Page란?

A.
서비스 관리자나 운영자가 데이터를 관리하기 위한 Backoffice 화면이다.

Q. SSR Thymeleaf가 Admin Page에 적합한 이유는?

A.
Table, Form, Search, Pagination 중심 화면을 서버 렌더링으로 단순하게 만들 수 있기 때문이다.

Q. Admin Page도 보안 검수가 필요한가?

A.
필수이다. 내부 화면이어도 인증, 권한, CSRF, 입력 검증이 필요하다.

Q. Admin Page에서 View Hiding만으로 보안이 완료되는가?

A.
아니다. 실제 요청 차단은 Spring Security와 서버 권한 검증으로 처리해야 한다.

---

# 2. Admin URL Design

## 2.1 Resource Based Admin URL

### [개념]

Admin URL은 관리 대상 Resource를 기준으로 설계한다.

관리자 기능은 일반 사용자 URL과 구분하기 위해 `/admin/**` prefix를 사용하는 것이 일반적이다.

```text
/admin/{resource}
/admin/{resource}/{id}
/admin/{resource}/new
/admin/{resource}/{id}/edit
/admin/{resource}/{id}/delete
```

---

### [핵심]

- Admin URL은 `/admin/**`로 분리한다.
- Resource 이름은 복수형을 권장한다.
- 목록은 `/admin/users`처럼 표현한다.
- 상세는 `/admin/users/{id}`처럼 표현한다.
- 생성 Form은 `/admin/users/new`처럼 표현한다.
- 수정 Form은 `/admin/users/{id}/edit`처럼 표현한다.
- 삭제 Action은 `/admin/users/{id}/delete` POST로 처리한다.
- Status 변경 Action도 POST로 처리한다.

---

### [실무]

User Admin URL:

```text
GET  /admin/users
GET  /admin/users/{id}
GET  /admin/users/new
POST /admin/users
GET  /admin/users/{id}/edit
POST /admin/users/{id}/edit
POST /admin/users/{id}/delete
POST /admin/users/{id}/activate
POST /admin/users/{id}/deactivate
```

Festival Admin URL:

```text
GET  /admin/festivals
GET  /admin/festivals/{id}
GET  /admin/festivals/new
POST /admin/festivals
GET  /admin/festivals/{id}/edit
POST /admin/festivals/{id}/edit
POST /admin/festivals/{id}/delete
```

Security Mapping:

```java
http.authorizeHttpRequests(auth -> auth
    .requestMatchers("/admin/**").hasRole("ADMIN")
    .anyRequest().permitAll()
);
```

---

### [FAQ]

Q. Admin URL은 왜 `/admin/**`로 분리하는가?

A.
관리자 기능을 명확히 구분하고 Security Rule을 적용하기 쉽기 때문이다.

Q. Admin Resource URL은 단수형과 복수형 중 무엇을 쓰는가?

A.
일반적으로 복수형을 권장한다. 예: `/admin/users`

Q. 삭제 URL은 어떻게 설계하는가?

A.
`POST /admin/users/{id}/delete`처럼 POST Action으로 처리하는 것을 권장한다.

Q. 활성화 / 비활성화 같은 상태 변경은 GET으로 처리해도 되는가?

A.
권장하지 않는다. 상태 변경 요청은 POST Form으로 처리한다.

---

# 3. Admin Controller Pattern

## 3.1 View Controller

### [개념]

Admin View Controller는 Admin Page의 HTML View Rendering을 담당하는 `@Controller`이다.

REST API 응답이 아니라 Thymeleaf Template View Name을 반환한다.

```text
GET /admin/users
→ AdminUserController
→ model.addAttribute()
→ return "admin/users/list"
```

---

### [핵심]

- Admin View Controller는 `@Controller`를 사용한다.
- `@RestController`를 사용하지 않는다.
- 목록, 상세, 생성 Form, 수정 Form, 삭제 Action을 담당한다.
- Service 호출 결과를 Model에 담는다.
- View Name은 `templates/admin/...` 경로와 매핑한다.
- API Controller와 책임을 분리한다.
- Controller는 View에 필요한 데이터 조립까지만 담당한다.
- Business Logic은 Service에 둔다.

---

### [실무]

Controller 기본 구조:

```java
@Controller
@RequestMapping("/admin/users")
public class AdminUserController {

    @GetMapping
    public String list(Model model) {
        model.addAttribute("users", userService.findAll());
        return "admin/users/list";
    }

    @GetMapping("/{id}")
    public String detail(@PathVariable Long id, Model model) {
        model.addAttribute("user", userService.findById(id));
        return "admin/users/detail";
    }

    @GetMapping("/new")
    public String createForm(Model model) {
        model.addAttribute("userForm", new UserCreateForm());
        return "admin/users/create-form";
    }
}
```

Template Mapping:

```text
return "admin/users/list"
→ templates/admin/users/list.html

return "admin/users/detail"
→ templates/admin/users/detail.html

return "admin/users/create-form"
→ templates/admin/users/create-form.html
```

---

### [FAQ]

Q. Admin View Controller는 어떤 Annotation을 사용하는가?

A.
`@Controller`를 사용한다.

Q. Admin View Controller에서 문자열 반환값은 무엇인가?

A.
Thymeleaf Template을 찾기 위한 View Name이다.

Q. Admin API와 Admin View Controller를 같이 둬도 되는가?

A.
권장하지 않는다. View Rendering과 JSON API 응답은 Controller를 분리하는 것이 좋다.

Q. Admin Controller에 Business Logic을 많이 넣어도 되는가?

A.
권장하지 않는다. Business Logic은 Service로 분리한다.

---

# 4. Admin List Page

## 4.1 List Page Pattern

### [개념]

Admin List Page는 관리 대상 데이터를 Table 형태로 조회하고 Search, Filter, Pagination을 제공하는 화면이다.

```text
GET /admin/users
→ Search Condition Binding
→ Page Query
→ Model Add
→ Render List Template
```

---

### [핵심]

- 목록 화면은 `GET` 요청으로 처리한다.
- 검색 조건은 Query Parameter로 받는다.
- 검색 조건은 Search Form Object로 바인딩할 수 있다.
- 결과는 `Page` 또는 `Slice`로 조회한다.
- Template에서는 `th:each`로 Table Row를 렌더링한다.
- Pagination Link에 검색 조건을 유지한다.
- 목록 화면에는 Create Button, Detail Link, Edit Link, Delete Action을 배치한다.
- 대량 데이터에는 `findAll()`보다 Pagination 조회를 권장한다.

---

### [실무]

Search Form DTO:

```java
public class UserSearchForm {

    private String keyword;
    private String role;
    private Boolean active;

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
    Page<UserAdminResponse> users = userService.search(searchForm, pageable);

    model.addAttribute("users", users);
    model.addAttribute("searchForm", searchForm);
    return "admin/users/list";
}
```

Template:

```html
<form th:action="@{/admin/users}" th:object="${searchForm}" method="get">
  <input th:field="*{keyword}" placeholder="검색어" />

  <select th:field="*{role}">
    <option value="">전체 권한</option>
    <option value="USER">USER</option>
    <option value="ADMIN">ADMIN</option>
  </select>

  <button type="submit">검색</button>
</form>

<table>
  <tr>
    <th>ID</th>
    <th>Email</th>
    <th>Name</th>
    <th>Role</th>
    <th>Action</th>
  </tr>

  <tr th:each="user : ${users.content}">
    <td th:text="${user.id}">1</td>
    <td th:text="${user.email}">email</td>
    <td th:text="${user.name}">name</td>
    <td th:text="${user.role}">role</td>
    <td>
      <a th:href="@{/admin/users/{id}(id=${user.id})}">상세</a>
      <a th:href="@{/admin/users/{id}/edit(id=${user.id})}">수정</a>
    </td>
  </tr>
</table>
```

---

### [FAQ]

Q. Admin List Page는 어떤 HTTP Method를 사용하는가?

A.
일반적으로 `GET`을 사용한다.

Q. 검색 조건은 어떻게 받는가?

A.
Query Parameter를 Search Form Object로 바인딩한다.

Q. 목록 데이터는 Template에서 어떻게 반복하는가?

A.
`th:each`를 사용해 Table Row를 반복 렌더링한다.

Q. Admin List에서 Page 객체는 어떻게 반복하는가?

A.
보통 `${users.content}`를 반복한다.

---

# 5. Admin Detail Page

## 5.1 Detail Page Pattern

### [개념]

Admin Detail Page는 단일 Resource의 상세 정보를 조회하고, 수정 / 삭제 / 목록 이동 Action을 제공하는 화면이다.

```text
GET /admin/users/{id}
→ userService.findById(id)
→ model.addAttribute("user", user)
→ return "admin/users/detail"
```

---

### [핵심]

- 상세 화면은 `GET` 요청으로 처리한다.
- 식별자는 `@PathVariable`로 받는다.
- Service에서 단일 데이터를 조회한다.
- 조회 결과는 Detail Response DTO로 Model에 담는다.
- Template에서는 `${user.field}` 형태로 출력한다.
- 수정 / 삭제 / 목록 링크를 제공한다.
- 데이터가 없으면 404 또는 Not Found Error Page로 연결한다.
- 삭제 Form에는 CSRF Token을 포함한다.

---

### [실무]

Controller:

```java
@GetMapping("/{id}")
public String detail(@PathVariable Long id, Model model) {
    UserAdminDetailResponse user = userService.findAdminDetail(id);
    model.addAttribute("user", user);
    return "admin/users/detail";
}
```

Template:

```html
<h1>사용자 상세</h1>

<dl>
  <dt>ID</dt>
  <dd th:text="${user.id}">1</dd>

  <dt>Email</dt>
  <dd th:text="${user.email}">email</dd>

  <dt>Name</dt>
  <dd th:text="${user.name}">name</dd>

  <dt>Role</dt>
  <dd th:text="${user.role}">role</dd>

  <dt>Created At</dt>
  <dd th:text="${#temporals.format(user.createdAt, 'yyyy-MM-dd HH:mm')}">
    date
  </dd>
</dl>

<a th:href="@{/admin/users}">목록</a>
<a th:href="@{/admin/users/{id}/edit(id=${user.id})}">수정</a>

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

---

### [FAQ]

Q. Admin Detail Page에서 ID는 어떻게 받는가?

A.
`@PathVariable`로 받는다.

Q. 상세 데이터가 없으면 어떻게 처리하는가?

A.
Not Found 예외를 발생시키고 404 Error Page로 연결한다.

Q. 상세 화면에서 삭제는 어떻게 처리하는가?

A.
GET Link가 아니라 CSRF Token을 포함한 POST Form으로 처리한다.

---

# 6. Admin Create Page

## 6.1 Create Form Pattern

### [개념]

Admin Create Page는 신규 Resource 생성을 위한 Form 화면이다.

GET 요청은 빈 Form Object를 렌더링하고, POST 요청은 Form Binding, Validation, 저장 처리를 수행한다.

```text
GET /admin/users/new
→ Empty Form Object
→ Render Create Form

POST /admin/users
→ @Valid @ModelAttribute
→ BindingResult
→ Error View or Redirect
```

---

### [핵심]

- Create Form GET은 빈 Form Object를 Model에 담는다.
- Create Form POST는 `@ModelAttribute`로 입력값을 받는다.
- Validation은 `@Valid`로 실행한다.
- `BindingResult`는 `@Valid` 대상 바로 뒤에 위치한다.
- 실패 시 같은 Form View를 반환한다.
- 성공 시 Service 호출 후 Redirect한다.
- Select Option 등 Form 부가 데이터는 실패 시 다시 Model에 담는다.
- POST Form에는 CSRF Token을 포함한다.

---

### [실무]

Controller:

```java
@GetMapping("/new")
public String createForm(Model model) {
    model.addAttribute("userForm", new UserCreateForm());
    model.addAttribute("roles", roleService.findAll());
    return "admin/users/create-form";
}

@PostMapping
public String create(
        @Valid @ModelAttribute("userForm") UserCreateForm userForm,
        BindingResult bindingResult,
        Model model,
        RedirectAttributes redirectAttributes
) {
    if (bindingResult.hasErrors()) {
        model.addAttribute("roles", roleService.findAll());
        return "admin/users/create-form";
    }

    Long userId = userService.create(userForm);
    redirectAttributes.addFlashAttribute("message", "사용자가 등록되었습니다.");
    return "redirect:/admin/users/" + userId;
}
```

Template:

```html
<form th:action="@{/admin/users}" th:object="${userForm}" method="post">
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />

  <div>
    <label for="email">Email</label>
    <input type="email" th:field="*{email}" />
    <p th:errors="*{email}">email error</p>
  </div>

  <div>
    <label for="name">Name</label>
    <input type="text" th:field="*{name}" />
    <p th:errors="*{name}">name error</p>
  </div>

  <div>
    <label for="role">Role</label>
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
    <p th:errors="*{role}">role error</p>
  </div>

  <button type="submit">등록</button>
</form>
```

---

### [FAQ]

Q. Create Form GET에서 해야 할 일은?

A.
빈 Form Object와 Select Option 같은 부가 데이터를 Model에 담고 Form View를 반환한다.

Q. Create Form POST에서 Validation 실패 시 무엇을 반환하는가?

A.
같은 Create Form View를 반환한다.

Q. Create Form POST 성공 시 무엇을 반환하는가?

A.
등록 후 상세 또는 목록 화면으로 Redirect한다.

Q. Create Form Validation 실패 후 Select Option이 사라지는 이유는?

A.
실패 View 반환 전에 Option 데이터를 Model에 다시 담지 않았기 때문이다.

---

# 7. Admin Update Page

## 7.1 Update Form Pattern

### [개념]

Admin Update Page는 기존 Resource를 수정하기 위한 Form 화면이다.

GET 요청은 기존 데이터를 Form Object로 변환해 렌더링하고, POST 요청은 수정값을 검증 후 반영한다.

```text
GET /admin/users/{id}/edit
→ Find Existing Data
→ Convert To Update Form
→ Render Update Form

POST /admin/users/{id}/edit
→ @Valid Update Form
→ BindingResult
→ Error View or Redirect
```

---

### [핵심]

- Update Form GET은 기존 데이터를 조회한다.
- 기존 데이터를 Update Form DTO로 변환한다.
- Template의 Form Action에 ID가 필요하다.
- POST Handler는 `@PathVariable id`와 Form Object를 함께 받는다.
- Validation 실패 시 `id`와 Option 데이터를 다시 Model에 담는다.
- 성공 시 Service에서 수정 처리 후 Redirect한다.
- Update Form DTO는 Create Form DTO와 분리할 수 있다.
- POST Form에는 CSRF Token을 포함한다.

---

### [실무]

Controller:

```java
@GetMapping("/{id}/edit")
public String updateForm(@PathVariable Long id, Model model) {
    UserAdminDetailResponse user = userService.findAdminDetail(id);

    model.addAttribute("userId", id);
    model.addAttribute("userForm", UserUpdateForm.from(user));
    model.addAttribute("roles", roleService.findAll());

    return "admin/users/update-form";
}

@PostMapping("/{id}/edit")
public String update(
        @PathVariable Long id,
        @Valid @ModelAttribute("userForm") UserUpdateForm userForm,
        BindingResult bindingResult,
        Model model,
        RedirectAttributes redirectAttributes
) {
    if (bindingResult.hasErrors()) {
        model.addAttribute("userId", id);
        model.addAttribute("roles", roleService.findAll());
        return "admin/users/update-form";
    }

    userService.update(id, userForm);
    redirectAttributes.addFlashAttribute("message", "사용자 정보가 수정되었습니다.");
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
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />

  <input type="text" th:field="*{name}" />
  <p th:errors="*{name}">name error</p>

  <select th:field="*{role}">
    <option
      th:each="role : ${roles}"
      th:value="${role.code}"
      th:text="${role.name}"
    >
      role
    </option>
  </select>

  <button type="submit">수정</button>
</form>
```

---

### [FAQ]

Q. Update Form GET에서 기존 데이터는 어떻게 처리하는가?

A.
Service에서 조회한 뒤 Update Form DTO로 변환해 Model에 담는다.

Q. Update Form POST에서 ID는 어떻게 유지하는가?

A.
`@PathVariable`로 받고 Validation 실패 시 Model에 다시 담아 Form Action에서 사용한다.

Q. Update Form에서 Create Form DTO를 그대로 써도 되는가?

A.
필드와 검증 조건이 같으면 가능하지만, 다르면 Update Form DTO를 분리하는 것이 좋다.

---

# 8. Admin Delete Action

## 8.1 Delete POST Pattern

### [개념]

Admin Delete Action은 Resource 삭제를 위한 상태 변경 요청이다.

GET Link가 아니라 POST Form으로 처리하고, CSRF Token과 권한 검증을 포함해야 한다.

```text
POST /admin/users/{id}/delete
→ Authorization Check
→ Delete
→ Redirect List
```

---

### [핵심]

- Delete는 상태 변경 요청이다.
- GET Link 삭제는 비권장이다.
- POST Form 삭제를 권장한다.
- CSRF Token이 필요하다.
- 삭제 전 권한 검증이 필요하다.
- 성공 후 목록 또는 상위 화면으로 Redirect한다.
- Soft Delete와 Hard Delete 정책을 명확히 한다.
- 삭제 성공 메시지는 Flash Attribute로 전달할 수 있다.

---

### [실무]

Controller:

```java
@PostMapping("/{id}/delete")
public String delete(
        @PathVariable Long id,
        RedirectAttributes redirectAttributes
) {
    userService.delete(id);
    redirectAttributes.addFlashAttribute("message", "삭제되었습니다.");
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
  <button type="submit" onclick="return confirm('정말 삭제하시겠습니까?')">
    삭제
  </button>
</form>
```

삭제 정책:

```text
Soft Delete
→ deletedAt / active false
→ 운영 데이터 보존

Hard Delete
→ 실제 DB 삭제
→ 복구 어려움
```

---

### [FAQ]

Q. Delete를 GET Link로 처리하면 안 되는 이유는?

A.
GET은 조회용이어야 하며, 삭제 같은 상태 변경은 POST Form으로 처리하는 것이 안전하다.

Q. Delete Form에 CSRF Token이 필요한가?

A.
필요하다. Spring Security CSRF 보호가 활성화된 경우 누락 시 403이 발생할 수 있다.

Q. 삭제 성공 후에는 어떤 응답을 반환하는가?

A.
목록 또는 상위 화면으로 Redirect한다.

---

# 9. Admin Search Filter Pattern

## 9.1 Search Form And Filter

### [개념]

Admin Search Filter Pattern은 검색어, 상태, 카테고리, 권한, 기간 조건으로 목록 데이터를 필터링하는 구조이다.

검색 조건은 Query Parameter로 전달하고, Search Form Object로 바인딩한다.

```text
GET /admin/festivals?keyword=music&status=OPEN&page=0
→ @ModelAttribute SearchForm
→ Service Search
→ Page Result
→ Render List
```

---

### [핵심]

- Search Form은 `method="get"`을 사용한다.
- 검색 조건은 URL Query Parameter에 남는다.
- Search Form Object는 `@ModelAttribute`로 받는다.
- 검색 후 입력값 유지를 위해 `th:field`를 사용한다.
- Pagination Link에 검색 조건을 유지한다.
- 민감 정보는 검색 조건 Query Parameter로 전달하지 않는다.
- 기간 검색은 시작일 / 종료일 범위 검증이 필요하다.

---

### [실무]

Search Form DTO:

```java
public class FestivalSearchForm {

    private String keyword;
    private String status;
    private String categoryCode;
    private LocalDate startDate;
    private LocalDate endDate;

    // getter / setter
}
```

Controller:

```java
@GetMapping("/admin/festivals")
public String list(
        @ModelAttribute("searchForm") FestivalSearchForm searchForm,
        Pageable pageable,
        Model model
) {
    Page<FestivalAdminResponse> festivals =
            festivalService.searchAdmin(searchForm, pageable);

    model.addAttribute("festivals", festivals);
    model.addAttribute("searchForm", searchForm);
    model.addAttribute("categories", categoryService.findAll());

    return "admin/festivals/list";
}
```

Template:

```html
<form th:action="@{/admin/festivals}" th:object="${searchForm}" method="get">
  <input th:field="*{keyword}" placeholder="축제명" />

  <select th:field="*{status}">
    <option value="">전체 상태</option>
    <option value="OPEN">OPEN</option>
    <option value="CLOSED">CLOSED</option>
  </select>

  <select th:field="*{categoryCode}">
    <option value="">전체 카테고리</option>
    <option
      th:each="category : ${categories}"
      th:value="${category.code}"
      th:text="${category.name}"
    >
      category
    </option>
  </select>

  <input type="date" th:field="*{startDate}" />
  <input type="date" th:field="*{endDate}" />

  <button type="submit">검색</button>
</form>
```

---

### [FAQ]

Q. Admin Search Form은 어떤 Method를 사용하는가?

A.
일반적으로 `GET`을 사용한다.

Q. 검색 후 입력값을 유지하려면 어떻게 하는가?

A.
Search Form Object를 Model에 담고 `th:field`를 사용한다.

Q. Pagination에서 검색 조건을 유지해야 하는 이유는?

A.
다음 페이지로 이동해도 같은 검색 결과 범위를 유지해야 하기 때문이다.

---

# 10. Admin Pagination Pattern

## 10.1 Page Pagination

### [개념]

Admin Pagination Pattern은 목록 데이터를 페이지 단위로 조회하고, 페이지 이동 링크를 제공하는 구조이다.

Spring Data `Page`를 사용하면 전체 개수, 전체 페이지 수, 현재 페이지 정보를 Template에서 활용할 수 있다.

```text
Pageable
→ Service Search
→ Page<Result>
→ Model
→ Pagination Fragment
```

---

### [핵심]

- Admin 목록은 `Pageable`을 사용할 수 있다.
- 전체 페이지 수가 필요하면 `Page`를 사용한다.
- 무한 스크롤이나 단순 다음 페이지 여부만 필요하면 `Slice`를 사용할 수 있다.
- Admin Table Pagination은 보통 `Page`가 적합하다.
- 검색 조건은 Pagination Link에 유지한다.
- Page Number는 내부적으로 0부터 시작한다.
- 화면에는 `page.number + 1`을 표시한다.

---

### [실무]

Controller:

```java
@GetMapping
public String list(
        @ModelAttribute("searchForm") UserSearchForm searchForm,
        @PageableDefault(size = 20, sort = "createdAt", direction = Sort.Direction.DESC)
        Pageable pageable,
        Model model
) {
    Page<UserAdminResponse> users = userService.search(searchForm, pageable);

    model.addAttribute("users", users);
    model.addAttribute("searchForm", searchForm);
    return "admin/users/list";
}
```

Template:

```html
<nav>
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

  <span th:text="${users.number + 1}">1</span>
  <span>/</span>
  <span th:text="${users.totalPages}">1</span>

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
</nav>
```

---

### [FAQ]

Q. Admin Pagination에는 Page와 Slice 중 무엇이 적합한가?

A.
전체 페이지 수와 총 개수가 필요한 Admin Table에는 보통 `Page`가 적합하다.

Q. 화면 Page Number와 내부 Page Number가 다른 이유는?

A.
Spring Data Page Number는 0부터 시작하고, 화면에는 보통 1부터 표시하기 때문이다.

Q. Pagination Link에서 검색 조건을 유지하지 않으면?

A.
페이지 이동 시 검색 조건이 사라져 전체 목록으로 돌아갈 수 있다.

---

# 11. Admin Flash Message Pattern

## 11.1 Success Message

### [개념]

Admin Flash Message Pattern은 등록, 수정, 삭제 성공 후 Redirect된 화면에서 성공 메시지를 한 번 표시하는 구조이다.

`RedirectAttributes.addFlashAttribute()`를 사용한다.

```text
POST Success
→ addFlashAttribute("message", "저장 완료")
→ Redirect
→ GET View
→ ${message} 출력
```

---

### [핵심]

- 성공 메시지는 Flash Attribute로 전달한다.
- Flash Attribute는 Redirect 후 한 번만 유지된다.
- 등록 / 수정 / 삭제 성공 메시지에 적합하다.
- Validation Error는 Flash Attribute로 처리하지 않는다.
- Flash Message 영역은 Layout 상단에 공통 배치할 수 있다.
- 메시지 이름은 `message` 또는 `successMessage`처럼 통일한다.

---

### [실무]

Controller:

```java
@PostMapping("/{id}/edit")
public String update(
        @PathVariable Long id,
        @Valid @ModelAttribute("userForm") UserUpdateForm userForm,
        BindingResult bindingResult,
        RedirectAttributes redirectAttributes
) {
    if (bindingResult.hasErrors()) {
        return "admin/users/update-form";
    }

    userService.update(id, userForm);
    redirectAttributes.addFlashAttribute("message", "수정되었습니다.");
    return "redirect:/admin/users/" + id;
}
```

Fragment:

```html
<div th:fragment="flashMessage">
  <div th:if="${message}" class="alert alert-success">
    <span th:text="${message}">message</span>
  </div>
</div>
```

Layout 사용:

```html
<div th:replace="~{fragments/alert :: flashMessage}"></div>
```

---

### [FAQ]

Q. 등록 성공 메시지는 어떻게 전달하는가?

A.
`RedirectAttributes.addFlashAttribute()`를 사용한다.

Q. Flash Message는 언제 사라지는가?

A.
Redirect 후 한 번 사용되면 사라진다.

Q. Validation Error도 Flash Message로 처리하는가?

A.
권장하지 않는다. Validation Error는 BindingResult와 Form View에서 처리한다.

---

# 12. Admin Authorization Pattern

## 12.1 Admin Access Control

### [개념]

Admin Authorization Pattern은 관리자 페이지 접근을 인증된 관리자에게만 허용하는 보안 구조이다.

Template에서 메뉴를 숨기는 것과 서버에서 URL 접근을 차단하는 것은 별개의 책임이다.

```text
View Menu Hiding
→ sec:authorize

Server URL Protection
→ SecurityFilterChain requestMatchers("/admin/**").hasRole("ADMIN")
```

---

### [핵심]

- `/admin/**`는 서버 Security Rule로 보호한다.
- `sec:authorize`는 View 표시 제어에 사용한다.
- View Hiding만으로 보안이 완성되지 않는다.
- Controller 또는 Service에서 도메인 권한 검증이 추가될 수 있다.
- 삭제, 수정 같은 위험 Action은 서버에서 권한을 재검증한다.
- 관리자 메뉴는 `sec:authorize="hasRole('ADMIN')"`로 조건부 표시할 수 있다.
- 403 Error Page를 제공한다.

---

### [실무]

Security Rule:

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

Admin Menu:

```html
<a sec:authorize="hasRole('ADMIN')" th:href="@{/admin}"> 관리자 </a>
```

Admin Delete Button:

```html
<form
  sec:authorize="hasRole('ADMIN')"
  th:action="@{/admin/users/{id}/delete(id=${user.id})}"
  method="post"
>
  <input
    type="hidden"
    th:name="${_csrf.parameterName}"
    th:value="${_csrf.token}"
  />
  <button type="submit">삭제</button>
</form>
```

권한 검수:

```text
Admin Menu 숨김
→ UX 제어

/admin/** 접근 제한
→ 실제 URL 보안

Service Permission Check
→ 도메인 규칙 보안
```

---

### [FAQ]

Q. Admin Page 접근 제어는 어디서 하는가?

A.
Spring Security 설정에서 `/admin/**` 접근을 관리자 권한으로 제한한다.

Q. `sec:authorize`만 사용하면 Admin 보안이 완료되는가?

A.
아니다. `sec:authorize`는 View 표시 제어이고 실제 보안은 서버에서 처리해야 한다.

Q. 삭제 버튼을 숨기면 삭제 요청도 막히는가?

A.
아니다. 직접 URL 요청을 막기 위해 서버 권한 검증이 필요하다.

---

# 13. Admin Dashboard Pattern

## 13.1 Dashboard Summary

### [개념]

Admin Dashboard는 서비스 운영 상태를 요약해서 보여주는 관리자 첫 화면이다.

주요 지표, 최근 데이터, 처리 필요 항목, 시스템 상태를 카드 또는 테이블로 표시한다.

```text
GET /admin
→ Summary Query
→ Recent Data Query
→ Model
→ Dashboard Template
```

---

### [핵심]

- Dashboard는 운영 현황 요약 화면이다.
- Summary Count, Recent List, Alert Item을 표시한다.
- 무거운 통계 쿼리는 별도 최적화가 필요하다.
- Dashboard DTO로 필요한 데이터만 전달한다.
- 관리자 권한이 필요하다.
- 캐싱 또는 집계 테이블을 검토할 수 있다.
- 실시간성이 낮은 통계는 매 요청마다 계산하지 않는다.

---

### [실무]

Controller:

```java
@GetMapping("/admin")
public String dashboard(Model model) {
    AdminDashboardResponse dashboard = adminDashboardService.getDashboard();

    model.addAttribute("dashboard", dashboard);
    return "admin/dashboard";
}
```

Template:

```html
<h1>Admin Dashboard</h1>

<section class="summary">
  <div class="card">
    <strong th:text="${dashboard.userCount}">0</strong>
    <span>Users</span>
  </div>

  <div class="card">
    <strong th:text="${dashboard.festivalCount}">0</strong>
    <span>Festivals</span>
  </div>

  <div class="card">
    <strong th:text="${dashboard.pendingReviewCount}">0</strong>
    <span>Pending Reviews</span>
  </div>
</section>

<section>
  <h2>최근 가입 사용자</h2>
  <table>
    <tr th:each="user : ${dashboard.recentUsers}">
      <td th:text="${user.email}">email</td>
      <td th:text="${#temporals.format(user.createdAt, 'yyyy-MM-dd HH:mm')}">
        date
      </td>
    </tr>
  </table>
</section>
```

---

### [FAQ]

Q. Admin Dashboard는 무엇인가?

A.
운영자가 서비스 상태를 빠르게 확인하는 관리자 요약 화면이다.

Q. Dashboard에는 어떤 데이터가 적합한가?

A.
주요 Count, 최근 데이터, 처리 필요 항목, 시스템 상태가 적합하다.

Q. Dashboard 쿼리가 느리면 어떻게 하는가?

A.
캐싱, 집계 테이블, 비동기 통계 갱신을 검토한다.

---

# 14. Admin Error Handling Pattern

## 14.1 Not Found And Access Denied

### [개념]

Admin Error Handling Pattern은 관리자 화면에서 데이터 없음, 권한 없음, 서버 오류를 사용자 친화적인 Error Page로 연결하는 구조이다.

```text
Admin Request
→ Resource Not Found
→ 404 Page

Admin Request
→ Access Denied
→ 403 Page

Admin Request
→ Server Error
→ 500 Page
```

---

### [핵심]

- 존재하지 않는 데이터는 404로 처리한다.
- 권한 없는 요청은 403으로 처리한다.
- 서버 내부 오류는 500으로 처리한다.
- Error Page에 Stack Trace를 출력하지 않는다.
- 관리자라도 내부 시스템 정보를 과도하게 노출하지 않는다.
- 목록으로 돌아가기 링크를 제공한다.
- 사용자 메시지와 서버 로그를 분리한다.

---

### [실무]

Not Found Exception:

```java
@ResponseStatus(HttpStatus.NOT_FOUND)
public class AdminResourceNotFoundException extends RuntimeException {

    public AdminResourceNotFoundException(String message) {
        super(message);
    }
}
```

Controller:

```java
@GetMapping("/{id}")
public String detail(@PathVariable Long id, Model model) {
    UserAdminDetailResponse user = userService.findAdminDetail(id);
    model.addAttribute("user", user);
    return "admin/users/detail";
}
```

404 Template:

```html
<h1>관리 데이터를 찾을 수 없습니다.</h1>
<p>요청한 데이터가 존재하지 않거나 삭제되었습니다.</p>
<a th:href="@{/admin}">관리자 홈</a>
<a th:href="@{/admin/users}">목록으로 이동</a>
```

403 Template:

```html
<h1>접근 권한이 없습니다.</h1>
<p>이 관리자 기능을 사용할 권한이 없습니다.</p>
<a th:href="@{/admin}">관리자 홈</a>
```

---

### [FAQ]

Q. Admin Detail에서 데이터가 없으면 어떻게 처리하는가?

A.
Not Found 예외를 발생시키고 404 Page로 연결한다.

Q. Admin 권한이 없으면 어떤 화면을 보여주는가?

A.
403 Access Denied Page를 보여준다.

Q. Admin Error Page에 내부 예외를 출력해도 되는가?

A.
권장하지 않는다. 내부 정보는 서버 로그에 남기고 화면에는 안내 메시지만 표시한다.

---

# 15. Admin Page Common Mistakes

## 15.1 Practical Mistakes

### [개념]

Admin Page Mistake는 SSR 구조, URL 설계, Form Binding, Pagination, Security 책임이 일관되지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Admin Controller를 `@RestController`로 작성
- View Name에 `.html` 포함
- `/admin/**` Security Rule 누락
- `sec:authorize`만 적용하고 서버 권한 검증 누락
- Delete를 GET Link로 처리
- POST Form에 CSRF Token 누락
- Validation 실패 시 Redirect 사용
- Select Option 재등록 누락
- Pagination Link에 검색 조건 누락
- Query Parameter에 민감 정보 포함
- Entity를 Form에 과도하게 직접 Binding
- Admin Error Page에 Stack Trace 출력
- Flash Attribute로 Validation Error 처리
- API Controller와 View Controller 혼합
- Dashboard에 무거운 실시간 집계 쿼리 과다 사용

---

### [실무]

잘못된 Controller:

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

올바른 Controller:

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

잘못된 Delete:

```html
<a th:href="@{/admin/users/{id}/delete(id=${user.id})}"> 삭제 </a>
```

올바른 Delete:

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

Q. Admin Controller에서 `@RestController`를 쓰면 안 되는 이유는?

A.
View Name이 Template Rendering이 아니라 Response Body로 반환되기 때문이다.

Q. Admin Delete를 GET Link로 처리하면 안 되는 이유는?

A.
GET은 조회용이고 삭제는 상태 변경 요청이므로 POST Form이 안전하다.

Q. Admin Pagination 검색 조건이 사라지는 이유는?

A.
Pagination Link에 기존 Query Parameter를 포함하지 않았기 때문이다.

---

# 16. Admin Page Troubleshooting

## 16.1 Practical Troubleshooting

### [개념]

Admin Page Troubleshooting은 SSR Admin 화면에서 발생하는 View Rendering, Binding, Pagination, Security 오류를 원인별로 점검하는 과정이다.

---

### [핵심]

문제별 주요 원인:

- `admin/users/list` 문자열 출력 → `@RestController` 사용
- Template Not Found → View Name과 Template Path 불일치
- Form Binding Error → `th:object`와 Model Attribute 불일치
- Validation Error 미출력 → Redirect 사용 또는 `BindingResult` 위치 오류
- Select Option 사라짐 → Validation 실패 시 Option Model 재등록 누락
- Delete 403 → CSRF Token 누락
- Admin URL 접근 가능 → Security Rule 누락
- Pagination 조건 소실 → Page Link Query Parameter 누락
- Flash Message 미출력 → Attribute 이름 불일치
- CSS 미반영 → Browser Cache 또는 Static Resource 경로 오류

---

### [실무]

View Rendering 점검:

```text
문자열이 그대로 출력됨
→ @RestController 여부 확인
→ @ResponseBody 여부 확인
→ @Controller 사용 확인
```

Form Binding 점검:

```text
Binding 오류
→ GET Controller Model Attribute 확인
→ th:object 이름 확인
→ th:field Field 이름 확인
→ @ModelAttribute 이름 확인
```

Validation 점검:

```text
Validation Error 미출력
→ @Valid 확인
→ BindingResult 위치 확인
→ hasErrors() 처리 확인
→ Redirect 사용 여부 확인
→ th:errors Field 이름 확인
```

Security 점검:

```text
Admin 접근 제어 문제
→ /admin/** Security Rule 확인
→ 로그인 사용자 Role 확인
→ sec:authorize는 UI 제어인지 확인
→ Service 권한 검증 확인
```

Pagination 점검:

```text
검색 조건 소실
→ searchForm Model 확인
→ Pagination Link 확인
→ keyword / status / category / page / size 유지 확인
```

---

### [FAQ]

Q. Admin View Name 문자열이 그대로 출력되는 이유는?

A.
`@RestController` 또는 `@ResponseBody`가 적용되었을 가능성이 높다.

Q. Admin Form Validation Error가 안 보이는 이유는?

A.
Redirect 사용, `BindingResult` 위치 오류, `th:errors` Field 이름 불일치가 원인일 수 있다.

Q. Admin Delete 요청이 403이 되는 이유는?

A.
CSRF Token이 누락되었을 가능성이 높다.

---

# 17. Review Checklist

## 17.1 Admin Page Review Checklist

### [개념]

Admin Page Review Checklist는 Agent가 SSR Thymeleaf Admin Page 코드를 검수하기 위한 기준이다.

---

### [핵심]

URL 검수:

- `/admin/**` prefix 사용 여부
- Resource 복수형 URL 사용 여부
- List / Detail / New / Edit / Delete URL 일관성
- Delete가 POST Action인지 여부
- 상태 변경 Action이 POST인지 여부

Controller 검수:

- `@Controller` 사용 여부
- `@RestController` 오사용 여부
- View Name과 Template Path 일치 여부
- API Controller와 View Controller 분리 여부
- GET Form에서 Form Object Model 등록 여부
- POST 성공 Redirect 여부
- Validation 실패 Same View 반환 여부
- Business Logic이 Service에 있는지 여부

Form 검수:

- Form DTO 사용 여부
- `th:object`와 Model Attribute 이름 일치 여부
- `th:field` 사용 여부
- `@Valid`와 `BindingResult` 위치 적절성
- Select Option 실패 시 재등록 여부
- `th:errors` 출력 여부
- CSRF Token 포함 여부

List / Pagination 검수:

- Search Form `method="get"` 여부
- Search Form Object 사용 여부
- Page 또는 Slice 선택 적절성
- Pagination Link의 검색 조건 유지 여부
- Query Parameter 민감 정보 포함 여부

Security 검수:

- `/admin/**` 서버 권한 제한 여부
- `sec:authorize`는 UI 제어로만 사용하는지 여부
- 수정 / 삭제 서버 권한 검증 여부
- CSRF Token 포함 여부
- Logout / Delete POST Form 여부
- Error Page 내부 정보 노출 여부

Dashboard 검수:

- Dashboard DTO 사용 여부
- 무거운 실시간 집계 쿼리 과다 여부
- 캐싱 필요성 여부
- 관리자 권한 제한 여부

---

### [실무]

검수 Flow:

```text
Admin URL 확인
→ Security Rule 확인
→ Controller Annotation 확인
→ View Name / Template Path 확인
→ Model Attribute 확인
→ Form Binding 확인
→ Validation Flow 확인
→ Pagination Query Parameter 확인
→ CSRF Token 확인
→ Error Page 정보 노출 확인
```

---

### [FAQ]

Q. Admin Page 검수에서 가장 먼저 확인할 것은?

A.
`/admin/**` URL 분리와 서버 Security Rule 적용 여부이다.

Q. Admin Controller 검수 핵심은?

A.
`@Controller` 사용, View Name 반환, Template Path 일치 여부이다.

Q. Admin Form 검수 핵심은?

A.
`th:object`, `th:field`, `@Valid`, `BindingResult`, `th:errors`, 실패 시 Same View 반환을 확인하는 것이다.

Q. Admin Security 검수 핵심은?

A.
`sec:authorize`만 믿지 않고 `/admin/**` 서버 권한 제한, CSRF Token, 수정 / 삭제 권한 검증을 확인하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. SSR Thymeleaf Admin Page란?
A. 관리자나 운영자가 데이터를 조회, 생성, 수정, 삭제, 검색하기 위한 Backoffice SSR 화면이다.

Q. Thymeleaf가 Admin Page에 적합한 이유는?
A. Table, Form, Search, Pagination 중심 화면을 서버 렌더링으로 단순하게 구현할 수 있기 때문이다.

Q. Admin URL은 어떻게 설계하는가?
A. `/admin/users`, `/admin/users/{id}`, `/admin/users/new`, `/admin/users/{id}/edit`처럼 Resource 기반으로 설계한다.

Q. Admin URL에 `/admin/**` prefix를 쓰는 이유는?
A. 관리자 기능을 분리하고 Security Rule을 적용하기 쉽기 때문이다.

Q. Admin Controller는 어떤 Annotation을 사용하는가?
A. `@Controller`를 사용한다.

Q. Admin Controller에서 `@RestController`를 쓰면 안 되는 이유는?
A. View Name이 Template Rendering이 아니라 Response Body로 반환되기 때문이다.

Q. Admin View Name은 어디에 매핑되는가?
A. `templates/admin/...` 하위 Thymeleaf Template에 매핑된다.

Q. Admin List Page는 어떤 Method를 사용하는가?
A. 일반적으로 `GET`을 사용한다.

Q. Admin Search Form은 어떤 Method를 사용하는가?
A. 일반적으로 `GET`을 사용한다.

Q. Admin Search 조건은 어떻게 받는가?
A. Query Parameter를 Search Form Object로 바인딩한다.

Q. Admin List 데이터는 어떻게 반복 출력하는가?
A. `th:each`로 Table Row를 반복 렌더링한다.

Q. Admin Detail Page에서 ID는 어떻게 받는가?
A. `@PathVariable`로 받는다.

Q. Admin Detail 데이터가 없으면 어떻게 처리하는가?
A. Not Found 예외를 발생시키고 404 Error Page로 연결한다.

Q. Admin Create Form GET에서 해야 할 일은?
A. 빈 Form Object와 Select Option 데이터를 Model에 담고 Form View를 반환한다.

Q. Admin Create Form POST에서 해야 할 일은?
A. Form Binding, Validation, Service 저장, 성공 Redirect를 처리한다.

Q. Admin Update Form GET에서 해야 할 일은?
A. 기존 데이터를 조회해 Update Form DTO로 변환하고 Model에 담는다.

Q. Admin Update Form POST에서 ID는 어떻게 유지하는가?
A. `@PathVariable`로 받고 Validation 실패 시 Model에 다시 담는다.

Q. Admin Delete는 어떻게 처리하는가?
A. GET Link가 아니라 CSRF Token을 포함한 POST Form으로 처리한다.

Q. Admin Delete 성공 후 무엇을 반환하는가?
A. 목록 또는 상위 화면으로 Redirect한다.

Q. Admin Delete에 CSRF Token이 필요한가?
A. 필요하다. CSRF 보호가 활성화된 경우 누락 시 403이 발생할 수 있다.

Q. Admin Pagination에는 Page와 Slice 중 무엇이 적합한가?
A. 전체 개수와 전체 페이지가 필요한 Table Pagination에는 보통 `Page`가 적합하다.

Q. Admin Pagination에서 검색 조건을 유지해야 하는 이유는?
A. 다음 페이지로 이동해도 같은 검색 결과를 유지해야 하기 때문이다.

Q. Pagination Link에서 검색 조건이 사라지는 이유는?
A. Page Link에 기존 Query Parameter를 포함하지 않았기 때문이다.

Q. Admin Flash Message는 어떻게 전달하는가?
A. `RedirectAttributes.addFlashAttribute()`를 사용한다.

Q. Flash Attribute는 언제 사용하는가?
A. 등록, 수정, 삭제 성공 메시지 전달에 사용한다.

Q. Validation Error를 Flash Attribute로 처리하는가?
A. 권장하지 않는다. BindingResult와 Form View에서 처리한다.

Q. Admin 접근 제어는 어디서 하는가?
A. Spring Security 설정에서 `/admin/**` 접근을 관리자 권한으로 제한한다.

Q. `sec:authorize`만으로 Admin 보안이 완료되는가?
A. 아니다. View 표시 제어일 뿐이고 실제 보안은 서버 권한 검증으로 처리해야 한다.

Q. Admin Dashboard란?
A. 운영자가 서비스 상태를 빠르게 확인하는 관리자 요약 화면이다.

Q. Dashboard에는 어떤 데이터가 적합한가?
A. 주요 Count, 최근 데이터, 처리 필요 항목, 시스템 상태가 적합하다.

Q. Dashboard 쿼리가 느리면 어떻게 하는가?
A. 캐싱, 집계 테이블, 비동기 통계 갱신을 검토한다.

Q. Admin Error Page에 Stack Trace를 출력해도 되는가?
A. 안 된다. 내부 정보 노출 위험이 있다.

Q. Admin View Name 문자열이 그대로 출력되는 이유는?
A. `@RestController` 또는 `@ResponseBody`가 적용되었을 가능성이 높다.

Q. Admin Form Validation Error가 안 보이는 이유는?
A. Redirect 사용, `BindingResult` 위치 오류, `th:errors` Field 이름 불일치가 원인일 수 있다.

Q. Admin Delete 요청이 403이 되는 이유는?
A. CSRF Token이 누락되었을 가능성이 높다.

Q. Admin Page 검수 핵심은?
A. URL 분리, Security Rule, `@Controller`, View Name, Form Binding, Validation, Pagination, CSRF를 확인하는 것이다.

Q. Admin Security 검수 핵심은?
A. `/admin/**` 서버 권한 제한, CSRF Token, 수정 / 삭제 권한 검증, Error Page 정보 노출 여부를 확인하는 것이다.
