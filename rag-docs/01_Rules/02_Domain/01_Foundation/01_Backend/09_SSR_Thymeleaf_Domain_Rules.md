# SSR Thymeleaf Domain Rules

---

# 1. Domain Purpose

SSR Thymeleaf Domain 문서는 Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Server-Side Rendering Support
- Spring MVC View Rendering Support
- Thymeleaf Template Generation Support
- Form Binding Support
- Validation Error Rendering Support
- Session / Authentication View Support
- Legacy / Admin Page Support

우선순위:

1. Spring MVC SSR Flow
2. Thymeleaf Template Syntax
3. Form Binding / Validation
4. Security / Session View Handling
5. Practical Admin Page Pattern

---

# 2. Scope

포함 범위:

- SSR (Server-Side Rendering)
- Spring MVC
- Controller
- Model
- ModelAndView
- View Resolver
- Thymeleaf
- Template Engine
- HTML
- HTML Template
- Thymeleaf Standard Attributes
- Text Rendering
- Conditional Rendering
- Iteration Rendering
- Link Rendering
- Form Binding Attributes
- Fragment Attributes
- Form Binding
- BindingResult
- Validation
- Layout
- Fragment
- Header / Footer
- Static Resource
- CSS / JS
- Session
- Authentication View
- CSRF
- Spring Security Integration
- Admin Page
- Error Page
- Redirect
- Forward
- PRG Pattern
- Troubleshooting

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]

---

## Optional

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

# 4. SSR Core Rules

SSR Thymeleaf 문서는 Server-Side Rendering 흐름 중심으로 작성.

핵심 구조:

- Request
- Controller
- Model
- View Name
- Thymeleaf Template
- HTML Response

---

반드시 설명 포함:

- SSR 역할
- CSR과 차이
- Controller가 View Name을 반환하는 방식
- Model 데이터가 Template에 전달되는 방식

---

예:

```text
Request
→ Controller
→ Model Add Attribute
→ Return View Name
→ Thymeleaf Render
→ HTML Response
```

---

# 5. Spring MVC View Rules

반드시 포함:

- @Controller
- @GetMapping
- @PostMapping
- Model
- ModelAndView
- View Name
- View Resolver

---

예:

```java
@GetMapping("/users")
public String users(Model model) {
    model.addAttribute("users", userService.findAll());
    return "users/list";
}
```

---

반드시 설명:

- @Controller와 @RestController 차이
- String 반환값이 View Name으로 해석되는 조건
- templates 디렉터리 기준 View Mapping

---

중요:

SSR Controller는 JSON 반환이 아니라 View Rendering 중심.

---

# 6. Thymeleaf Template Rules

반드시 포함:

- th:text
- th:utext
- th:if
- th:unless
- th:each
- th:href
- th:src
- th:classappend

---

반드시 설명:

- 서버에서 HTML 생성
- Model Attribute 접근
- 조건 렌더링
- 반복 렌더링

---

예:

```html
<span th:text="${user.name}">username</span>
```

---

금지:

Thymeleaf를 React / SPA 방식처럼 설명하지 않는다.

---

# 7. Expression Rules

반드시 포함:

- Variable Expression
- Selection Expression
- Message Expression
- Link Expression
- Fragment Expression

---

예:

```text
${user.name}      → Variable Expression
*{email}          → Selection Expression
#{label.email}    → Message Expression
@{/users}         → Link Expression
~{layout/header}  → Fragment Expression
```

---

# 8. Form Binding Rules

매우 중요.

반드시 포함:

- th:object
- th:field
- th:action
- th:errors
- BindingResult
- @ModelAttribute
- @Valid

---

예:

```html
<form th:action="@{/users}" th:object="${userForm}" method="post">
  <input th:field="*{email}" />
</form>
```

---

# 9. Validation Rules

반드시 포함:

- Bean Validation
- @Valid
- BindingResult
- Field Error
- Global Error
- th:errors
- #fields.hasErrors

---

# 10. Redirect / Forward Rules

반드시 포함:

- redirect:
- forward:
- PRG Pattern
- RedirectAttributes
- Flash Attribute

---

# 11. Layout / Fragment Rules

반드시 포함:

- Fragment
- Layout
- th:fragment
- th:replace
- th:insert

---

# 12. Static Resource Rules

반드시 포함:

- static
- css
- js
- images
- th:href
- th:src

---

# 13. Spring Security View Rules

반드시 포함:

- Login Page
- Logout
- CSRF
- Authentication
- Authorization
- Role-based View
- sec:authorize

---

# 14. Session View Rules

포함:

- HttpSession
- Session Attribute
- Login User
- Flash Attribute
- RedirectAttributes

---

# 15. Admin Page Rules

SSR Thymeleaf는 Admin Page / Internal Tool에 적합.

반드시 포함:

- List Page
- Detail Page
- Create Form
- Update Form
- Delete Action
- Search / Filter
- Pagination

---

# 16. Pagination Rules

포함:

- Pageable
- Page
- Page Number
- Sort
- Search Condition 유지

---

# 17. Error Page Rules

포함:

- Error View
- 404
- 500
- Validation Error
- Global Error

---

# 18. SSR vs REST Rules

반드시 비교.

| Category   | SSR Thymeleaf | REST API        |
| ---------- | ------------- | --------------- |
| Response   | HTML          | JSON            |
| Client     | Browser       | FE App          |
| Controller | @Controller   | @RestController |
| View       | Thymeleaf     | 없음            |

---

# 19. Common Mistakes

자주 발생:

- @RestController로 View 반환
- BindingResult 위치 오류
- Validation 실패 후 Redirect
- th:object 누락
- Static Resource 경로 오류
- CSRF Token 누락
- Session 남용
- th:utext 남용

---

# 20. Troubleshooting Rules

반드시 포함 추천.

예:

- Template Not Found
- Static Resource 404
- Binding Error
- Validation Error Not Displayed
- CSRF 403
- Fragment Not Found

---

# 21. Retrieval Optimization Rules

강조 대상:

- SSR
- Thymeleaf
- Spring MVC
- @Controller
- Model
- View Resolver
- Form Binding
- BindingResult
- Validation
- Redirect
- PRG Pattern
- Fragment
- Spring Security
- CSRF
- Admin Page
- Pagination

---

# 22. Version Rules

기준:

- Java 21
- Spring Boot 3.x
- Spring MVC
- Thymeleaf 3.x
- Spring Security 6
- Jakarta Validation

---

Legacy 제외:

- JSP
- Servlet 직접 렌더링
- XML MVC 설정
- Spring Boot 1.x / 2.x 중심 설명

---

# 23. Agent Decision Rules

```text
Admin Page / Backoffice
→ SSR Thymeleaf 가능

Public SPA / Dynamic UX
→ React / REST API 권장

Form-heavy Internal Tool
→ SSR Thymeleaf 가능

Mobile App / External API
→ REST API 권장
```

---

# 24. Final Goal

SSR Thymeleaf RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve SSR Pattern
- Generate Thymeleaf Template
- Generate MVC Controller
- Generate Form Binding Code
- Generate Validation Rendering
- Review SSR Controller
- Review Thymeleaf Template
- Detect BindingResult Error
- Detect Security View Mistake
