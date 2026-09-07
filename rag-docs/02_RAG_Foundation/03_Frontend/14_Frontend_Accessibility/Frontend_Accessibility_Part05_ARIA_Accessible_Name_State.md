# Frontend Accessibility Part05 - ARIA Accessible Name State

---

# 1. ARIA Foundation

## 1.1 ARIA Purpose

### [개념]

ARIA는 Accessible Rich Internet Applications의 약자다.

ARIA는 HTML만으로 표현하기 어려운 역할, 상태, 관계를 보조기술에 전달하는 속성이다.

ARIA는 Semantic HTML을 대체하는 기술이 아니다.

Frontend Accessibility의 기본 원칙은 먼저 의미에 맞는 HTML을 사용하고, 부족한 정보만 ARIA로 보완하는 것이다.

---

### [핵심]

ARIA 핵심 원칙:

- Semantic HTML 우선
- Native Element 우선
- 필요한 경우에만 ARIA 사용
- 잘못된 ARIA는 없는 것보다 나쁠 수 있음
- role과 keyboard 동작은 일치해야 함
- aria 상태는 실제 UI 상태와 동기화
- accessible name 제공
- hidden 상태와 focus 상태 충돌 방지
- Testing Library Query로 검증 가능해야 함

자주 사용하는 ARIA:

- `aria-label`
- `aria-labelledby`
- `aria-describedby`
- `aria-invalid`
- `aria-expanded`
- `aria-selected`
- `aria-current`
- `aria-hidden`
- `aria-live`
- `aria-busy`
- `aria-controls`
- `aria-modal`

---

### [실무]

ARIA 적용 Flow:

```text
UI 역할 확인
→ Native HTML로 가능한지 확인
→ Semantic HTML 사용
→ 부족한 이름 / 상태 / 관계 확인
→ 필요한 ARIA만 추가
→ 실제 UI 상태와 ARIA 상태 동기화
→ Keyboard 동작 확인
→ Testing Library getByRole 검증
```

좋은 기준:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="filter-panel"
  onClick={toggleOpen}
>
  필터 열기
</button>
```

나쁜 기준:

```jsx
<div role="button" aria-expanded={open} onClick={toggleOpen}>
  필터 열기
</div>
```

실무 기준:

- button 역할은 `button` 태그 우선
- link 역할은 `a` 또는 `Link` 우선
- form control은 native input / select / textarea 우선
- ARIA는 이름, 상태, 관계 보완에 사용
- `aria-expanded`는 실제 open 상태와 일치
- `aria-invalid`는 실제 validation 상태와 일치
- `aria-selected`는 실제 선택 상태와 일치
- `aria-hidden` 내부에 focus 가능한 요소가 있으면 문제 가능

---

### [FAQ]

Q. ARIA가 뭐야?
A. HTML만으로 표현하기 어려운 역할, 상태, 관계를 보조기술에 전달하는 속성이다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다.

Q. ARIA는 언제 써?
A. Semantic HTML만으로 역할, 상태, 관계를 충분히 전달하기 어려울 때 보완적으로 사용한다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

---

## 1.2 No ARIA is Better than Bad ARIA

### [개념]

잘못된 ARIA는 보조기술에 틀린 정보를 전달할 수 있다.

ARIA는 화면의 실제 상태와 일치해야 하며, role을 붙인 경우 해당 role에 맞는 keyboard 동작도 제공해야 한다.

---

### [핵심]

Bad ARIA 예:

- `div role="button"` + keyboard 미구현
- 닫힌 Dropdown에 `aria-expanded="true"`
- 열린 Modal에 `aria-modal` 누락
- 실제 오류가 없는데 `aria-invalid="true"`
- 숨겨진 요소에 focus 가능한 자식 존재
- tab이 선택되지 않았는데 `aria-selected="true"`
- 현재 페이지가 아닌 link에 `aria-current="page"`
- accessible name이 visible text와 충돌
- role과 실제 동작 불일치

---

### [실무]

나쁜 예:

```jsx
<button type="button" aria-expanded="true" onClick={toggleOpen}>
  메뉴
</button>
```

개선:

```jsx
<button type="button" aria-expanded={open} onClick={toggleOpen}>
  메뉴
</button>
```

나쁜 예:

```jsx
<div role="checkbox" aria-checked={checked}>
  약관 동의
</div>
```

개선:

```jsx
<label>
  <input type="checkbox" checked={checked} onChange={onChange} />
  약관 동의
</label>
```

실무 기준:

- ARIA 값은 state와 연결
- 하드코딩된 ARIA 상태 지양
- role을 붙이면 role별 keyboard interaction 확인
- Native Element로 대체 가능한지 먼저 검토
- Testing Library의 role/name query로 실제 노출 상태 확인
- ARIA 오류는 접근성 테스트와 수동 점검 모두에서 확인

---

### [FAQ]

Q. 잘못된 ARIA가 왜 위험해?
A. 보조기술 사용자에게 실제 UI와 다른 정보를 전달할 수 있기 때문이다.

Q. aria-expanded를 true로 고정하면 안 돼?
A. 안 된다. 실제 open 상태와 항상 동기화되어야 한다.

Q. role만 붙이면 접근성 문제가 해결돼?
A. 아니다. role에 맞는 keyboard 동작과 상태 관리가 함께 필요하다.

Q. ARIA를 쓰지 않는 게 나을 때도 있어?
A. 그렇다. 잘못 쓰는 ARIA보다 Semantic HTML만 정확히 쓰는 편이 더 안전할 수 있다.

---

# 2. Role Rules

## 2.1 Native Role First

### [개념]

Role은 요소의 의미나 역할을 보조기술에 전달한다.

대부분의 HTML 요소는 기본 role을 가지고 있으므로 불필요하게 role을 명시하지 않는 것이 좋다.

---

### [핵심]

Native role 예:

| HTML                    | 기본 Role  |
| ----------------------- | ---------- |
| `button`                | button     |
| `a href`                | link       |
| `input type="checkbox"` | checkbox   |
| `input type="radio"`    | radio      |
| `select`                | combobox   |
| `textarea`              | textbox    |
| `nav`                   | navigation |
| `main`                  | main       |
| `form`                  | form       |
| `table`                 | table      |
| `ul` / `ol`             | list       |
| `li`                    | listitem   |

원칙:

- 기본 role이 있으면 중복 role 지양
- `button role="button"` 불필요
- `nav role="navigation"` 대부분 불필요
- 부적절한 role override 금지
- role 변경 시 keyboard 동작 검토

---

### [실무]

좋은 예:

```jsx
<button type="button" onClick={onSave}>
  저장
</button>
```

불필요한 예:

```jsx
<button role="button" type="button" onClick={onSave}>
  저장
</button>
```

위험한 예:

```jsx
<a role="button" href="/festivals">
  축제 목록
</a>
```

개선:

```jsx
<Link to="/festivals">축제 목록</Link>
```

실무 기준:

- role을 직접 붙이기 전에 native element 확인
- HTML 의미와 role이 충돌하지 않게 함
- action이면 `button`, navigation이면 `a` / `Link`
- role override는 특별한 이유가 있을 때만 사용
- role에 맞는 keyboard interaction을 함께 구현

---

### [FAQ]

Q. role은 언제 써?
A. Native HTML만으로 역할을 표현하기 어려운 custom widget에서 보완적으로 사용한다.

Q. button에 role="button"을 붙여야 해?
A. 필요 없다. button은 기본적으로 button role을 가진다.

Q. nav에 role="navigation"을 붙여야 해?
A. 대부분 필요 없다. nav는 기본 navigation landmark 역할을 가진다.

Q. role을 바꾸면 keyboard 동작도 바뀌어?
A. 아니다. role은 의미 전달이고 keyboard 동작은 별도로 구현해야 할 수 있다.

---

## 2.2 Role and Keyboard Match

### [개념]

Role and Keyboard Match는 요소가 선언한 role과 실제 keyboard 동작이 일치해야 한다는 기준이다.

예를 들어 `role="button"`을 사용하면 keyboard 사용자도 button처럼 Enter / Space로 실행할 수 있어야 한다.

---

### [핵심]

Role별 keyboard 기대:

- `button`: Enter / Space 실행
- `link`: Enter 이동
- `checkbox`: Space toggle
- `radio`: Arrow 이동 / Space 선택
- `tab`: Arrow 이동 / Enter 또는 Space 선택
- `menuitem`: Arrow 이동 / Enter 또는 Space 실행
- `dialog`: 내부 focus 관리
- `listbox`: Arrow 이동 / option 선택

---

### [실무]

비권장 예:

```jsx
<div role="button" tabIndex={0} onClick={onOpen}>
  열기
</div>
```

개선:

```jsx
<button type="button" onClick={onOpen}>
  열기
</button>
```

Custom이 필요한 경우:

```jsx
<div
  role="button"
  tabIndex={0}
  onClick={onOpen}
  onKeyDown={(event) => {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      onOpen();
    }
  }}
>
  열기
</div>
```

실무 기준:

- role은 semantic만 제공
- keyboard 동작은 자동 생성되지 않을 수 있음
- role과 실제 동작이 다르면 혼란 발생
- custom widget은 keyboard test 필요
- 가능하면 native element로 대체

---

### [FAQ]

Q. role="button"을 쓰면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다.

Q. role과 실제 동작이 다르면 왜 문제야?
A. 보조기술 사용자가 기대한 조작과 실제 조작이 달라져 사용성이 떨어진다.

Q. role="link"를 붙이면 Enter로 이동해?
A. role만으로 이동 동작이 생기지 않는다. 실제 link는 href가 있는 a 또는 Link를 사용하는 것이 좋다.

Q. Custom Widget은 어떻게 검증해?
A. role, accessible name, keyboard 동작, focus 흐름을 함께 테스트한다.

---

# 3. Accessible Name Rules

## 3.1 Accessible Name Basics

### [개념]

Accessible Name은 스크린 리더와 Testing Library가 요소를 식별할 때 사용하는 이름이다.

Button, Link, Input, Checkbox, Radio, Dialog 같은 interactive element는 명확한 accessible name을 가져야 한다.

---

### [핵심]

Accessible Name 제공 방식:

- visible text
- `label`
- `aria-label`
- `aria-labelledby`
- `alt`
- `title` fallback

주요 대상:

- button
- icon button
- link
- input
- select
- textarea
- checkbox
- radio
- dialog
- navigation landmark
- search landmark
- tab
- menu item

---

### [실무]

Button:

```jsx
<button type="button">저장</button>
```

Input:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

Icon Button:

```jsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

Dialog:

```jsx
<section role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">리뷰 삭제</h2>
</section>
```

Testing Library:

```tsx
screen.getByRole("button", { name: "저장" });
screen.getByLabelText("이메일");
screen.getByRole("dialog", { name: "리뷰 삭제" });
```

실무 기준:

- visible text가 있으면 그것을 accessible name으로 활용
- visible text가 없으면 `aria-label` 또는 `aria-labelledby` 제공
- 같은 이름의 버튼이 반복되면 context 추가
- Dialog에는 title과 accessible name 제공
- icon만 있는 control은 반드시 이름 제공
- `getByRole` name 실패 시 accessible name 계산 확인

---

### [FAQ]

Q. Accessible Name이 뭐야?
A. 스크린 리더와 Testing Library가 요소의 이름으로 인식하는 텍스트다.

Q. visible text가 있으면 aria-label이 꼭 필요해?
A. 아니다. visible text가 명확하면 그것이 accessible name으로 사용될 수 있다.

Q. getByRole에서 name이 안 잡히는 이유는?
A. 요소에 accessible name이 없거나 기대한 이름과 실제 이름이 다를 수 있다.

Q. 같은 이름의 버튼이 여러 개면 문제야?
A. 문맥이 부족할 수 있다. 대상 이름을 포함해 구체화하는 것이 좋다.

---

## 3.2 aria-label Rules

### [개념]

`aria-label`은 화면에 보이는 텍스트가 없거나 부족할 때 보조기술에 요소의 이름을 직접 제공하는 속성이다.

`aria-label`은 visible label을 대체하기 위한 최우선 수단이 아니다.

가능하면 보이는 텍스트나 `label`을 먼저 사용한다.

---

### [핵심]

`aria-label` 사용 대상:

- icon only button
- search input without visible label
- close button
- notification button
- carousel control
- map control
- hidden visual label unavailable
- repeated short link 보완

주의:

- visible text와 의미 충돌 금지
- 과도한 설명 금지
- 상태 정보를 label에 고정하지 않음
- 번역 / 다국어 문구 관리 필요
- 민감정보 포함 금지

---

### [실무]

Icon Button:

```jsx
<button type="button" aria-label="알림 열기">
  <BellIcon aria-hidden="true" />
</button>
```

Close Button:

```jsx
<button type="button" aria-label="닫기" onClick={onClose}>
  <CloseIcon aria-hidden="true" />
</button>
```

Search Input:

```jsx
<input type="search" name="keyword" aria-label="축제 검색어" />
```

반복 링크 보완:

```jsx
<Link
  to={`/festivals/${festival.id}`}
  aria-label={`${festival.title} 자세히 보기`}
>
  자세히 보기
</Link>
```

실무 기준:

- icon only button에는 `aria-label` 제공
- 장식 icon은 `aria-hidden`
- form input은 visible label 우선
- `aria-label`에 내부 id, token, 개인정보 포함 금지
- visible text가 있는 요소에 다른 의미의 `aria-label`을 주지 않음
- 같은 기능의 label 문구는 일관되게 관리

---

### [FAQ]

Q. aria-label은 언제 써?
A. 화면에 보이는 이름이 없거나 부족할 때 보조기술에 이름을 제공하기 위해 사용한다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. aria-label이 visible text와 달라도 돼?
A. 의미가 충돌하면 안 된다. 사용자가 보는 이름과 보조기술 이름은 일관되어야 한다.

Q. aria-label에 자세한 설명을 길게 써도 돼?
A. 권장하지 않는다. 이름은 짧고 명확하게 제공하고 긴 설명은 aria-describedby를 고려한다.

---

## 3.3 aria-labelledby Rules

### [개념]

`aria-labelledby`는 화면에 이미 존재하는 텍스트 요소를 accessible name으로 연결하는 속성이다.

Dialog title, Section title, 복합 label, 기존 heading을 이름으로 사용할 때 유용하다.

---

### [핵심]

`aria-labelledby` 사용 대상:

- Dialog title 연결
- Section 이름 연결
- Tab panel 이름 연결
- Complex form label
- Group label
- Existing visible text reuse
- Multiple label text combination

특징:

- 참조 대상 id 필요
- 여러 id 공백 연결 가능
- `aria-label`보다 visible text 재사용에 유리
- 참조 요소가 DOM에 존재해야 함

---

### [실무]

Dialog:

```jsx
<section role="dialog" aria-modal="true" aria-labelledby="delete-dialog-title">
  <h2 id="delete-dialog-title">리뷰 삭제</h2>
</section>
```

Section:

```jsx
<section aria-labelledby="popular-title">
  <h2 id="popular-title">인기 축제</h2>
  ...
</section>
```

복합 이름:

```jsx
<h2 id="profile-title">프로필 수정</h2>
<label id="nickname-label" htmlFor="nickname">닉네임</label>
<input
  id="nickname"
  aria-labelledby="profile-title nickname-label"
/>
```

실무 기준:

- visible text를 accessible name으로 재사용할 때 사용
- Dialog에는 `aria-labelledby`로 title 연결 권장
- 참조 id가 실제 렌더링되는지 확인
- id 중복 금지
- `aria-label`과 동시에 사용할 때 우선순위와 충돌 주의
- 제목이 사라지는 conditional rendering 주의

---

### [FAQ]

Q. aria-labelledby는 언제 써?
A. 화면에 이미 있는 텍스트를 요소의 accessible name으로 연결할 때 사용한다.

Q. aria-label과 aria-labelledby 중 뭐가 좋아?
A. 보이는 텍스트를 재사용할 수 있다면 aria-labelledby가 더 명확하다.

Q. aria-labelledby에 여러 id를 넣을 수 있어?
A. 가능하다. 공백으로 여러 id를 연결할 수 있다.

Q. aria-labelledby가 동작하지 않는 이유는?
A. 참조 id가 없거나 중복되었거나 해당 요소가 렌더링되지 않았을 수 있다.

---

## 3.4 aria-describedby Rules

### [개념]

`aria-describedby`는 요소의 이름이 아니라 추가 설명을 연결하는 속성이다.

Helper Text, Error Message, 안내 문구, 제한 조건을 Form Control이나 interactive element와 연결할 때 사용한다.

---

### [핵심]

`aria-describedby` 사용 대상:

- helper text
- error message
- input condition
- password rule
- file upload condition
- tooltip-like description
- dialog description
- warning text
- multiple descriptions

Name과 Description 구분:

- `aria-label`: 이름
- `aria-labelledby`: 이름
- `aria-describedby`: 설명

---

### [실무]

Helper Text:

```jsx
<label htmlFor="password">비밀번호</label>
<input
  id="password"
  type="password"
  aria-describedby="password-help"
/>
<p id="password-help">
  영문, 숫자, 특수문자를 포함해 8자 이상 입력해 주세요.
</p>
```

Error Message:

```jsx
<input
  id="email"
  type="email"
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
/>;
{
  error && (
    <p id="email-error" role="alert">
      올바른 이메일 형식으로 입력해 주세요.
    </p>
  );
}
```

Helper + Error:

```jsx
<input
  id="nickname"
  aria-describedby={error ? "nickname-help nickname-error" : "nickname-help"}
/>
```

Dialog Description:

```jsx
<section
  role="dialog"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
>
  <h2 id="dialog-title">리뷰 삭제</h2>
  <p id="dialog-description">삭제한 리뷰는 복구할 수 없습니다.</p>
</section>
```

실무 기준:

- 설명용 문구는 `aria-describedby`
- 여러 설명 id는 공백으로 연결
- error message가 렌더링될 때만 id 연결
- 설명 문구는 너무 길지 않게 작성
- 이름과 설명 역할을 혼동하지 않음
- `aria-describedby` 참조 id 존재 여부 확인

---

### [FAQ]

Q. aria-describedby는 언제 써?
A. input 조건, helper text, error message 같은 추가 설명을 연결할 때 사용한다.

Q. aria-label과 aria-describedby 차이는?
A. aria-label은 요소의 이름이고 aria-describedby는 요소의 추가 설명이다.

Q. error message는 aria-describedby로 연결해?
A. 그렇다. error id를 만들고 input의 aria-describedby에 연결한다.

Q. aria-describedby에 여러 id를 넣을 수 있어?
A. 가능하다. helper text와 error message를 함께 연결할 수 있다.

---

# 4. State ARIA Rules

## 4.1 aria-invalid Rules

### [개념]

`aria-invalid`는 Form Control의 현재 값이 validation 기준을 통과하지 못했음을 보조기술에 전달하는 상태 속성이다.

오류 메시지와 함께 사용하면 사용자가 어떤 field에 문제가 있는지 이해하기 쉽다.

---

### [핵심]

사용 대상:

- text input
- email input
- password input
- textarea
- select
- custom form control
- invalid field
- validation failure

값:

- `true`
- `false`
- `grammar`
- `spelling`

실무에서는 주로 boolean 상태로 사용한다.

---

### [실무]

기본 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  type="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
{errors.email && (
  <p id="email-error" role="alert">
    이메일을 입력해 주세요.
  </p>
)}
```

Select 예:

```jsx
<label htmlFor="region">지역</label>
<select
  id="region"
  aria-invalid={Boolean(errors.region)}
  aria-describedby={errors.region ? "region-error" : undefined}
>
  <option value="">지역을 선택하세요</option>
</select>
```

실무 기준:

- 오류가 있을 때만 `aria-invalid={true}`
- 오류가 없으면 false 또는 생략 가능
- error message와 함께 사용 권장
- `aria-describedby`로 error message 연결
- 오류 상태와 UI 상태를 동기화
- 빨간색 테두리만 제공하지 않음

---

### [FAQ]

Q. aria-invalid는 언제 true야?
A. 해당 input의 현재 값이 validation 기준을 통과하지 못한 상태일 때 true로 설정한다.

Q. aria-invalid만 있으면 오류 전달이 충분해?
A. 아니다. 사용자가 수정할 수 있도록 error message도 함께 제공해야 한다.

Q. 오류가 없을 때 aria-invalid는 어떻게 해?
A. false로 두거나 속성을 생략할 수 있다.

Q. 빨간 테두리와 aria-invalid만 있으면 돼?
A. 아니다. 오류 원인과 수정 방법을 설명하는 텍스트가 필요하다.

---

## 4.2 aria-expanded Rules

### [개념]

`aria-expanded`는 어떤 control이 연결된 콘텐츠를 펼쳤는지 접었는지 보조기술에 전달하는 상태 속성이다.

Dropdown, Accordion, Disclosure, Tree Item 같은 열림 / 닫힘 UI에서 사용한다.

---

### [핵심]

사용 대상:

- Dropdown trigger
- Accordion trigger
- Disclosure button
- Menu button
- Combobox trigger
- Tree item
- Expandable panel

기준:

- trigger에 적용
- 실제 open 상태와 동기화
- `aria-controls`와 함께 사용 가능
- true / false 상태 관리
- 하드코딩 금지

---

### [실무]

Dropdown:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="user-menu"
  aria-haspopup="menu"
  onClick={toggleOpen}
>
  사용자 메뉴
</button>;

{
  open && (
    <ul id="user-menu" role="menu">
      ...
    </ul>
  );
}
```

Accordion:

```jsx
<button
  type="button"
  aria-expanded={isOpen}
  aria-controls="faq-panel-1"
  onClick={toggleOpen}
>
  환불 정책
</button>

<div id="faq-panel-1" hidden={!isOpen}>
  환불 정책 설명
</div>
```

실무 기준:

- `aria-expanded`는 trigger에 사용
- 실제 open state와 항상 일치
- 연결 panel이 있으면 `aria-controls` 고려
- 닫힌 상태에서 panel 내부 focus 방지
- visual open state와 aria state 동기화
- open label / close label 문구도 검토

---

### [FAQ]

Q. aria-expanded는 언제 써?
A. Dropdown, Accordion처럼 열림 / 닫힘 상태가 있는 trigger에서 사용한다.

Q. aria-expanded는 어디에 붙여?
A. 열고 닫는 trigger button에 붙인다.

Q. aria-expanded는 실제 open 상태와 같아야 해?
A. 그렇다. 실제 UI 상태와 항상 동기화되어야 한다.

Q. aria-controls도 꼭 필요해?
A. 필수는 아니지만 trigger와 panel 관계를 명확히 하는 데 도움이 될 수 있다.

---

## 4.3 aria-selected Rules

### [개념]

`aria-selected`는 Tab, Option, Grid Row 등 선택 가능한 항목의 선택 상태를 전달하는 속성이다.

Focus와 Selected는 다르다.

Focus는 현재 keyboard 위치이고, selected는 실제 선택된 상태다.

---

### [핵심]

사용 대상:

- `role="tab"`
- `role="option"`
- `role="row"`
- `role="gridcell"`
- custom listbox item

기준:

- 선택 가능한 항목에 사용
- 실제 selected 상태와 동기화
- focus 상태와 혼동 금지
- Tab Panel과 함께 연결
- roving tabindex와 함께 사용 가능

---

### [실무]

Tab 예:

```jsx
<button
  type="button"
  role="tab"
  id="tab-info"
  aria-selected={selectedTab === "info"}
  aria-controls="panel-info"
>
  정보
</button>
```

Listbox option 예:

```jsx
<li role="option" aria-selected={selectedRegion === "seoul"}>
  서울
</li>
```

실무 기준:

- `aria-selected`는 선택 상태 표현
- 현재 focus만 있다고 selected 처리하지 않음
- Tab에서는 selected tab과 visible panel이 일치해야 함
- Listbox에서는 selected option과 실제 value가 일치해야 함
- selected 상태는 시각적으로도 제공

---

### [FAQ]

Q. aria-selected는 언제 써?
A. Tab, Listbox Option처럼 선택 가능한 항목의 선택 상태를 전달할 때 사용한다.

Q. focus와 selected는 같은 거야?
A. 아니다. focus는 keyboard 위치이고 selected는 선택된 상태다.

Q. Tab에서 aria-selected는 어디에 붙여?
A. role="tab" 요소에 붙이고 실제 선택된 tab과 일치시킨다.

Q. aria-selected만 있으면 시각적 선택 표시가 필요 없어?
A. 아니다. 시각적으로도 선택 상태가 보여야 한다.

---

## 4.4 aria-current Rules

### [개념]

`aria-current`는 navigation이나 step 목록에서 현재 페이지, 현재 단계, 현재 위치를 보조기술에 전달하는 속성이다.

현재 메뉴, Breadcrumb, Pagination, Stepper에서 사용한다.

---

### [핵심]

사용 대상:

- current page navigation link
- breadcrumb current item
- pagination current page
- stepper current step
- calendar current date
- current location indicator

주요 값:

- `page`
- `step`
- `location`
- `date`
- `time`
- `true`
- `false`

---

### [실무]

Navigation:

```jsx
<NavLink to="/calendar" aria-current={isActive ? "page" : undefined}>
  캘린더
</NavLink>
```

Breadcrumb:

```jsx
<nav aria-label="Breadcrumb">
  <ol>
    <li>
      <Link to="/">홈</Link>
    </li>
    <li>
      <Link to="/festivals">축제</Link>
    </li>
    <li aria-current="page">축제 상세</li>
  </ol>
</nav>
```

Pagination:

```jsx
<a href="/page/3" aria-current="page">
  3
</a>
```

Stepper:

```jsx
<li aria-current="step">결제 정보 입력</li>
```

실무 기준:

- 현재 페이지 link에는 `aria-current="page"`
- 현재 step에는 `aria-current="step"`
- Breadcrumb 마지막 현재 위치에 사용 가능
- visual active state와 aria-current 동기화
- 현재가 아닌 항목에 aria-current를 남기지 않음
- Tab 선택 상태에는 `aria-current`보다 `aria-selected`가 적합

---

### [FAQ]

Q. aria-current는 언제 써?
A. 현재 페이지, 현재 단계, 현재 위치를 navigation이나 step 목록에서 전달할 때 사용한다.

Q. 현재 메뉴는 어떻게 표시해?
A. 시각적 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. aria-current와 aria-selected 차이는?
A. aria-current는 현재 위치를 나타내고 aria-selected는 선택 가능한 항목의 선택 상태를 나타낸다.

Q. Breadcrumb 마지막 항목에도 aria-current를 써?
A. 현재 페이지를 나타내기 위해 aria-current="page"를 사용할 수 있다.

---

## 4.5 aria-busy Rules

### [개념]

`aria-busy`는 특정 영역이 현재 업데이트 중이거나 로딩 중임을 보조기술에 전달하는 속성이다.

Loading State에서 `role="status"`나 loading text와 함께 사용할 수 있다.

---

### [핵심]

사용 대상:

- data loading section
- submit processing form
- list refresh
- table update
- dashboard widget update
- async content region

기준:

- loading 중 true
- 완료 후 false
- loading text 함께 제공
- spinner만 단독 제공 금지
- 너무 잦은 변경 주의

---

### [실무]

Section loading:

```jsx
<section aria-busy={loading}>
  {loading && (
    <div role="status" aria-live="polite">
      데이터를 불러오는 중입니다.
    </div>
  )}

  {!loading && <FestivalList />}
</section>
```

Submit button:

```jsx
<button type="submit" disabled={loading} aria-busy={loading}>
  {loading ? "저장 중..." : "저장"}
</button>
```

실무 기준:

- loading 상태와 `aria-busy` 동기화
- loading text 제공
- spinner는 장식이면 `aria-hidden`
- 완료 후 busy 상태 제거
- 과도한 live region 변경 방지
- submit button은 text 변경으로 상태 전달

---

### [FAQ]

Q. aria-busy는 언제 써?
A. 특정 영역이 로딩 중이거나 업데이트 중임을 전달할 때 사용할 수 있다.

Q. aria-busy만 있으면 loading 접근성이 충분해?
A. 아니다. 사용자가 이해할 수 있는 loading text나 role status도 함께 제공하는 것이 좋다.

Q. 버튼에도 aria-busy를 쓸 수 있어?
A. 저장 중, 로그인 중 같은 처리 상태를 전달할 때 사용할 수 있다.

Q. spinner만 보여주면 안 돼?
A. 스크린 리더 사용자를 위해 loading text를 함께 제공해야 한다.

---

# 5. Relationship ARIA Rules

## 5.1 aria-controls Rules

### [개념]

`aria-controls`는 한 요소가 다른 요소의 표시나 동작을 제어한다는 관계를 전달하는 속성이다.

Dropdown trigger, Accordion trigger, Tab, Disclosure에서 연결된 panel id를 참조할 때 사용할 수 있다.

---

### [핵심]

사용 대상:

- Dropdown trigger → menu
- Accordion button → panel
- Tab → tabpanel
- Disclosure button → content
- Combobox → listbox
- Pagination control → content region

기준:

- 제어 대상 id 참조
- id 존재 필요
- open state와 함께 검토
- `aria-expanded`와 함께 사용 가능
- 관계 설명이지 동작 구현은 아님

---

### [실무]

Accordion:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="notice-panel"
>
  공지사항
</button>

<div id="notice-panel" hidden={!open}>
  공지사항 내용
</div>
```

Tab:

```jsx
<button
  type="button"
  role="tab"
  id="tab-review"
  aria-selected={selectedTab === "review"}
  aria-controls="panel-review"
>
  리뷰
</button>

<div
  role="tabpanel"
  id="panel-review"
  aria-labelledby="tab-review"
>
  리뷰 내용
</div>
```

실무 기준:

- `aria-controls`는 연결 대상 id와 일치해야 함
- id 중복 금지
- 연결 대상이 conditional rendering으로 없을 수 있는지 확인
- `aria-controls`만으로 UI 제어가 구현되는 것은 아님
- trigger와 panel 관계를 명확히 할 때 사용

---

### [FAQ]

Q. aria-controls는 언제 써?
A. trigger가 특정 panel, menu, tabpanel을 제어한다는 관계를 전달할 때 사용한다.

Q. aria-controls가 있으면 자동으로 열리고 닫혀?
A. 아니다. 관계만 전달하고 open / close 동작은 직접 구현해야 한다.

Q. aria-controls는 aria-expanded와 같이 써?
A. Dropdown, Accordion 같은 열림 상태 UI에서는 함께 사용할 수 있다.

Q. aria-controls가 안 먹는 이유는?
A. 참조하는 id가 없거나 중복되었거나 실제 DOM에 없을 수 있다.

---

## 5.2 aria-modal Rules

### [개념]

`aria-modal`은 Dialog가 modal인지, 즉 Dialog가 열린 동안 배경 콘텐츠와 상호작용하지 않는 상태인지 보조기술에 전달한다.

Modal Dialog는 `role="dialog"` 또는 `role="alertdialog"`와 함께 `aria-modal="true"`를 사용한다.

---

### [핵심]

Modal Dialog 기준:

- `role="dialog"`
- `aria-modal="true"`
- `aria-labelledby`
- `aria-describedby` 선택
- focus move on open
- focus trap
- focus return
- Escape close
- close button
- background interaction prevention

---

### [실무]

Modal 구조:

```jsx
<section
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
>
  <h2 id="dialog-title">리뷰 삭제</h2>
  <p id="dialog-description">삭제한 리뷰는 복구할 수 없습니다.</p>

  <button type="button" onClick={onCancel}>
    취소
  </button>
  <button type="button" onClick={onConfirm}>
    삭제
  </button>
</section>
```

Alert Dialog:

```jsx
<section
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="confirm-title"
  aria-describedby="confirm-description"
>
  <h2 id="confirm-title">정말 삭제할까요?</h2>
  <p id="confirm-description">이 작업은 되돌릴 수 없습니다.</p>
</section>
```

실무 기준:

- 일반 Modal은 `role="dialog"`
- 긴급 확인 Modal은 `role="alertdialog"` 고려
- `aria-modal`만으로 focus trap이 구현되지 않음
- Modal title을 `aria-labelledby`로 연결
- 설명이 있으면 `aria-describedby` 연결
- Modal close 후 trigger focus return 필요

---

### [FAQ]

Q. aria-modal은 언제 써?
A. Modal Dialog가 열린 동안 배경 콘텐츠와 상호작용하지 않는 상태를 전달할 때 사용한다.

Q. aria-modal만 붙이면 Modal 접근성이 끝이야?
A. 아니다. focus 이동, focus trap, focus return, 닫기 버튼도 필요하다.

Q. dialog와 alertdialog 차이는?
A. dialog는 일반 대화상자이고 alertdialog는 긴급하거나 중요한 확인이 필요한 대화상자다.

Q. Modal에는 aria-labelledby가 필요해?
A. 권장한다. Dialog의 제목을 accessible name으로 연결해야 한다.

---

# 6. Hidden ARIA Rules

## 6.1 aria-hidden Rules

### [개념]

`aria-hidden`은 특정 요소와 그 자식 요소를 보조기술 접근성 트리에서 숨기는 속성이다.

장식 아이콘, 중복 텍스트, 시각 효과 요소를 숨길 때 사용할 수 있다.

하지만 focus 가능한 요소를 `aria-hidden` 내부에 두면 심각한 접근성 문제가 발생할 수 있다.

---

### [핵심]

사용 대상:

- decorative icon
- decorative image alternative
- duplicate visual text
- visual effect element
- skeleton decoration
- background decoration

주의:

- focus 가능한 요소 내부 사용 금지
- interactive element에 사용 금지
- 실제로 필요한 콘텐츠 숨김 금지
- visible content와 screen reader content 불일치 주의
- `hidden`, `display:none`, `aria-hidden` 차이 이해

---

### [실무]

장식 아이콘:

```jsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

중복 텍스트 숨김:

```jsx
<span aria-hidden="true">★</span>
<span className="sr-only">즐겨찾기됨</span>
```

나쁜 예:

```jsx
<div aria-hidden="true">
  <button type="button">닫기</button>
</div>
```

실무 기준:

- 장식 아이콘은 `aria-hidden="true"`
- icon button의 이름은 icon이 아니라 button에 제공
- `aria-hidden` 내부에 button, link, input 등 focus 가능한 요소 금지
- 화면에는 보이지만 스크린 리더에는 숨길 정보인지 신중히 판단
- skeleton UI는 장식이면 `aria-hidden` 고려
- 중요한 상태 메시지는 `aria-hidden`으로 숨기지 않음

---

### [FAQ]

Q. aria-hidden은 언제 써?
A. 장식 아이콘이나 중복 시각 요소처럼 보조기술이 읽지 않아도 되는 요소를 숨길 때 사용한다.

Q. aria-hidden 안에 button이 있으면 왜 문제야?
A. focus 가능한 요소가 보조기술에는 숨겨져 keyboard와 screen reader 흐름이 충돌할 수 있다.

Q. 아이콘 버튼 내부 아이콘에는 aria-hidden을 써?
A. 보통 icon은 장식 처리하고 button에 aria-label을 제공한다.

Q. 중요한 메시지를 aria-hidden으로 숨겨도 돼?
A. 안 된다. 사용자에게 필요한 정보는 보조기술에도 전달되어야 한다.

---

## 6.2 Hidden vs Visually Hidden

### [개념]

Hidden은 콘텐츠를 화면과 보조기술 모두에서 숨기는 방식이고, Visually Hidden은 화면에서는 숨기지만 스크린 리더에는 제공하는 방식이다.

접근성 구현에서는 두 방식을 명확히 구분해야 한다.

---

### [핵심]

Hidden 방식:

- `hidden`
- `display: none`
- `visibility: hidden`
- unmount
- 보조기술에서도 일반적으로 제외

Visually Hidden 방식:

- `.sr-only`
- 화면에서는 보이지 않음
- 스크린 리더에는 제공
- icon button label
- section heading
- skip context
- additional link text

---

### [실무]

Visually Hidden CSS 예:

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

보이지 않는 label:

```jsx
<label htmlFor="search" className="sr-only">
  축제 검색어
</label>
<input id="search" type="search" />
```

반복 링크 보완:

```jsx
<Link to={`/festivals/${festival.id}`}>
  자세히 보기
  <span className="sr-only">: {festival.title}</span>
</Link>
```

실무 기준:

- 콘텐츠를 완전히 숨길 때는 `hidden` 또는 conditional rendering
- 스크린 리더에는 제공해야 하면 visually hidden
- focus 가능한 요소를 시각적으로 숨길 때는 주의
- Skip Link는 focus 시 visible해야 함
- sr-only text가 visible text와 충돌하지 않게 작성

---

### [FAQ]

Q. hidden과 visually hidden은 뭐가 달라?
A. hidden은 보조기술에서도 숨기고 visually hidden은 화면에서만 숨기며 스크린 리더에는 제공한다.

Q. label을 화면에서 숨겨도 돼?
A. 가능하다. sr-only 방식으로 스크린 리더에는 제공할 수 있다.

Q. Skip Link도 sr-only로 숨기면 돼?
A. 기본적으로 숨길 수 있지만 keyboard focus 시 화면에 보여야 한다.

Q. display none 요소는 스크린 리더가 읽어?
A. 일반적으로 읽지 않는다. 보조기술에도 숨겨지는 것으로 봐야 한다.

---

# 7. Live Region Rules

## 7.1 aria-live Basics

### [개념]

`aria-live`는 화면의 동적 변경 내용을 보조기술 사용자에게 알려주는 속성이다.

Loading, Success Message, Error Message, Toast, Search Result Count처럼 사용자에게 중요한 상태 변화에 사용할 수 있다.

---

### [핵심]

`aria-live` 값:

- `polite`
- `assertive`
- `off`

사용 대상:

- loading message
- success message
- error message
- toast
- validation summary
- search result count
- background update notice
- save status
- cart count update

기준:

- 일반 상태 변경은 `polite`
- 긴급 오류는 `assertive` 또는 `role="alert"` 고려
- 남발 금지
- 반복 업데이트 주의
- 화면에 보이는 메시지와 함께 제공

---

### [실무]

Status:

```jsx
<div role="status" aria-live="polite">
  저장 중입니다.
</div>
```

Search Result Count:

```jsx
<p role="status" aria-live="polite">
  검색 결과 {resultCount}건
</p>
```

Error:

```jsx
<div role="alert">저장에 실패했습니다.</div>
```

Toast:

```jsx
<div role="status" aria-live="polite">
  저장되었습니다.
</div>
```

실무 기준:

- 일반 알림은 `role="status"` 또는 `aria-live="polite"`
- 긴급 오류는 `role="alert"` 고려
- 너무 잦은 업데이트는 방해가 될 수 있음
- spinner만 바꾸지 말고 text 상태 제공
- Toast가 중요한 상태라면 live region 고려
- live region은 초기 렌더링과 업데이트 타이밍 검토 필요

---

### [FAQ]

Q. aria-live는 언제 써?
A. 화면이 동적으로 바뀌고 그 변경을 보조기술 사용자에게 알려야 할 때 사용한다.

Q. polite와 assertive 차이는?
A. polite는 현재 읽기 흐름을 방해하지 않고 알리고 assertive는 더 즉시 알리는 방식이다.

Q. role="alert"와 aria-live는 뭐가 달라?
A. role="alert"는 중요한 오류나 긴급 메시지를 즉시 알리는 데 사용되고 aria-live="polite"는 덜 긴급한 변경을 자연스럽게 알린다.

Q. Toast에도 aria-live가 필요해?
A. Toast가 중요한 상태 메시지를 전달한다면 보조기술 사용자가 인식할 수 있게 live region을 고려한다.

---

## 7.2 role status Rules

### [개념]

`role="status"`는 사용자에게 현재 상태나 결과를 알려주는 non-critical live region이다.

일반적으로 `aria-live="polite"` 성격을 가지며 loading, save status, result count 같은 상태 메시지에 적합하다.

---

### [핵심]

사용 대상:

- loading status
- save success
- search result count
- filter result count
- background sync status
- upload progress text
- non-critical update

기준:

- 짧은 상태 메시지
- 긴급하지 않은 변경
- 반복 업데이트 최소화
- 화면에 보이는 메시지 권장
- spinner 단독 지양

---

### [실무]

Loading:

```jsx
<div role="status">데이터를 불러오는 중입니다.</div>
```

Save Success:

```jsx
<div role="status">저장되었습니다.</div>
```

Result Count:

```jsx
<p role="status">필터 적용 결과 {count}건</p>
```

Upload:

```jsx
<div role="status">이미지 업로드 중입니다.</div>
```

실무 기준:

- status message는 짧고 명확하게 작성
- loading / success / result count에 적합
- 긴급 오류에는 `role="alert"` 고려
- 중복 live region 남발 금지
- message가 너무 자주 바뀌면 사용자 방해 가능

---

### [FAQ]

Q. role="status"는 언제 써?
A. loading, 저장 완료, 검색 결과 수처럼 긴급하지 않은 상태 변경을 알릴 때 사용한다.

Q. role status와 role alert 차이는?
A. status는 덜 긴급한 상태 알림이고 alert는 즉시 알려야 하는 오류나 중요한 메시지에 사용한다.

Q. spinner에 role status만 붙이면 돼?
A. spinner만으로는 부족하다. “데이터를 불러오는 중입니다” 같은 텍스트가 필요하다.

Q. 검색 결과 개수에도 role status를 쓸 수 있어?
A. 검색 결과가 동적으로 바뀐다면 사용할 수 있다.

---

## 7.3 role alert Rules

### [개념]

`role="alert"`는 사용자가 즉시 알아야 하는 중요한 오류나 경고 메시지를 보조기술에 전달하는 역할이다.

Form Error, Page Error, Save Failure 같은 상황에서 사용할 수 있다.

---

### [핵심]

사용 대상:

- field error
- global error
- save failure
- network error
- payment failure
- validation summary
- destructive action warning

주의:

- 남발 금지
- 사소한 상태 변경에는 부적합
- alert message는 짧고 명확해야 함
- 내부 오류 노출 금지
- 반복 렌더링으로 중복 알림 주의

---

### [실무]

Field Error:

```jsx
<p id="email-error" role="alert">
  이메일을 입력해 주세요.
</p>
```

Global Error:

```jsx
<div role="alert">저장에 실패했습니다. 잠시 후 다시 시도해 주세요.</div>
```

Payment Error:

```jsx
<section role="alert">
  <h2>결제에 실패했습니다.</h2>
  <p>결제 수단을 확인한 후 다시 시도해 주세요.</p>
</section>
```

실무 기준:

- 중요한 오류에 사용
- 모든 validation typing 변화에 alert 남발 금지
- field error는 input과 `aria-describedby` 연결
- 서버 내부 에러 메시지를 그대로 노출하지 않음
- 사용자가 다음에 무엇을 해야 하는지 알려줌

---

### [FAQ]

Q. role="alert"는 언제 써?
A. 사용자가 즉시 알아야 하는 중요한 오류나 경고 메시지에 사용한다.

Q. 모든 에러 메시지에 role alert를 붙여도 돼?
A. 남발하면 사용자를 방해할 수 있다. 중요한 오류에 신중히 사용한다.

Q. role alert만 있으면 field error 연결은 필요 없어?
A. field error라면 input과 aria-describedby로 연결하는 것이 좋다.

Q. 서버 오류를 alert로 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

---

# 8. Component ARIA Patterns

## 8.1 Dialog ARIA Pattern

### [개념]

Dialog ARIA Pattern은 Modal이나 Dialog가 열렸을 때 보조기술 사용자가 Dialog의 제목, 설명, 현재 맥락을 이해할 수 있게 하는 기준이다.

ARIA만으로 Dialog 접근성이 완성되지 않으며 focus management가 함께 필요하다.

---

### [핵심]

Dialog ARIA:

- `role="dialog"`
- `role="alertdialog"`
- `aria-modal="true"`
- `aria-labelledby`
- `aria-describedby`
- focus move on open
- focus trap
- focus return
- Escape close
- close button

---

### [실무]

Dialog:

```jsx
<section
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
>
  <h2 id="dialog-title">리뷰 작성</h2>
  <p id="dialog-description">축제에 대한 경험을 작성해 주세요.</p>

  <button type="button" onClick={onClose}>
    닫기
  </button>
</section>
```

Alert Dialog:

```jsx
<section
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="delete-title"
  aria-describedby="delete-description"
>
  <h2 id="delete-title">리뷰 삭제</h2>
  <p id="delete-description">삭제한 리뷰는 복구할 수 없습니다.</p>

  <button type="button">취소</button>
  <button type="button">삭제</button>
</section>
```

실무 기준:

- Dialog title은 `aria-labelledby`로 연결
- 설명이 있으면 `aria-describedby` 연결
- Dialog open 시 내부 focus 이동
- Dialog close 시 trigger focus return
- Dialog 내부 Tab 순환 확인
- `aria-modal`만으로 배경 focus 방지가 자동 처리되지 않음

---

### [FAQ]

Q. Dialog에는 어떤 ARIA가 필요해?
A. role dialog, aria-modal, aria-labelledby를 기본으로 고려하고 설명이 있으면 aria-describedby를 연결한다.

Q. alertdialog는 언제 써?
A. 삭제 확인처럼 긴급하거나 중요한 결정을 요구하는 Dialog에서 고려한다.

Q. aria-modal만 붙이면 focus trap이 생겨?
A. 아니다. focus trap은 별도로 구현해야 한다.

Q. Dialog accessible name은 어떻게 정해?
A. 보통 Dialog title을 aria-labelledby로 연결해 제공한다.

---

## 8.2 Dropdown ARIA Pattern

### [개념]

Dropdown ARIA Pattern은 Dropdown trigger와 menu 또는 listbox의 열림 상태, 관계, item 역할을 전달하는 기준이다.

Dropdown은 목적에 따라 Menu, Listbox, Disclosure로 구분해야 한다.

---

### [핵심]

Dropdown Trigger:

- `button`
- `aria-expanded`
- `aria-controls`
- `aria-haspopup`

Menu Pattern:

- `role="menu"`
- `role="menuitem"`
- action item
- keyboard pattern 필요

Listbox Pattern:

- `role="listbox"`
- `role="option"`
- selected option
- keyboard pattern 필요

Disclosure Pattern:

- `button`
- `aria-expanded`
- panel content

---

### [실무]

Action Menu:

```jsx
<button
  type="button"
  aria-haspopup="menu"
  aria-expanded={open}
  aria-controls="more-menu"
>
  더보기
</button>;

{
  open && (
    <ul id="more-menu" role="menu">
      <li>
        <button type="button" role="menuitem">
          수정
        </button>
      </li>
      <li>
        <button type="button" role="menuitem">
          삭제
        </button>
      </li>
    </ul>
  );
}
```

Disclosure:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="filter-panel"
>
  필터
</button>

<div id="filter-panel" hidden={!open}>
  필터 옵션
</div>
```

실무 기준:

- 단순 펼침 영역은 Disclosure Pattern 검토
- 액션 메뉴는 Menu Pattern 검토
- 선택 UI는 Listbox 또는 native Select 검토
- `aria-expanded`는 실제 open 상태와 일치
- 닫힌 item에 focus 가지 않게 처리
- role을 선택하면 해당 keyboard pattern 구현 필요

---

### [FAQ]

Q. Dropdown에는 무조건 role="menu"를 써?
A. 아니다. 단순 펼침이면 disclosure pattern이 적합할 수 있고 선택 UI면 listbox나 native select를 검토한다.

Q. aria-haspopup는 언제 써?
A. trigger가 menu, listbox, dialog 같은 popup을 연다는 것을 전달할 때 사용한다.

Q. Dropdown item은 role menuitem이면 끝이야?
A. 아니다. menu keyboard pattern과 focus 관리도 필요하다.

Q. 단순 필터 패널 열기는 menu야?
A. 보통 menu보다 disclosure button + panel 구조가 더 적합할 수 있다.

---

## 8.3 Tab ARIA Pattern

### [개념]

Tab ARIA Pattern은 같은 페이지 안에서 여러 panel을 전환하는 UI의 구조와 선택 상태를 보조기술에 전달하는 기준이다.

Tab은 route navigation과 다르며, 같은 맥락 안의 content panel 전환에 사용한다.

---

### [핵심]

Tab ARIA:

- `role="tablist"`
- `role="tab"`
- `role="tabpanel"`
- `aria-selected`
- `aria-controls`
- `aria-labelledby`
- `id` relation
- roving tabindex
- Arrow Key navigation

---

### [실무]

Tab 구조:

```jsx
<div role="tablist" aria-label="축제 상세 정보">
  <button
    type="button"
    role="tab"
    id="tab-info"
    aria-selected={selectedTab === "info"}
    aria-controls="panel-info"
    tabIndex={selectedTab === "info" ? 0 : -1}
  >
    정보
  </button>

  <button
    type="button"
    role="tab"
    id="tab-review"
    aria-selected={selectedTab === "review"}
    aria-controls="panel-review"
    tabIndex={selectedTab === "review" ? 0 : -1}
  >
    리뷰
  </button>
</div>

<div
  role="tabpanel"
  id="panel-info"
  aria-labelledby="tab-info"
  hidden={selectedTab !== "info"}
>
  축제 정보
</div>

<div
  role="tabpanel"
  id="panel-review"
  aria-labelledby="tab-review"
  hidden={selectedTab !== "review"}
>
  리뷰 목록
</div>
```

실무 기준:

- Tab과 TabPanel은 id로 연결
- 선택 상태는 `aria-selected`
- panel은 `aria-labelledby`로 tab과 연결
- hidden panel 내부 focus 방지
- Arrow Key 이동 고려
- 페이지 이동이면 Tab 대신 Route / Link 사용

---

### [FAQ]

Q. Tab에는 어떤 ARIA가 필요해?
A. tablist, tab, tabpanel role과 aria-selected, aria-controls, aria-labelledby 연결을 고려한다.

Q. Tab과 Route는 어떻게 구분해?
A. 같은 페이지 안의 panel 전환이면 Tab, 페이지 수준 이동이면 Route가 적합하다.

Q. aria-selected는 tab에 붙여?
A. 그렇다. 선택된 role="tab"에 aria-selected true를 설정한다.

Q. hidden tabpanel에 focus가 가면 문제야?
A. 문제다. 보이지 않는 panel 내부 요소에 focus가 가지 않게 해야 한다.

---

# 9. ARIA Testing Rules

## 9.1 Testing Library and ARIA

### [개념]

Testing Library는 사용자가 인식하는 role, name, label, text를 기준으로 요소를 찾도록 권장한다.

ARIA가 올바르게 적용되면 `getByRole`, `getByLabelText`, `getByText`로 UI를 자연스럽게 검증할 수 있다.

---

### [핵심]

우선 Query:

- `getByRole`
- `getByLabelText`
- `getByText`
- `getByAltText`
- `getByDisplayValue`
- `getByTestId` last resort

ARIA 검증 대상:

- role
- accessible name
- description
- invalid state
- expanded state
- selected state
- current state
- dialog name
- alert
- status

---

### [실무]

Button name:

```tsx
screen.getByRole("button", { name: "저장" });
```

Icon Button:

```tsx
screen.getByRole("button", { name: "알림 열기" });
```

Dialog:

```tsx
screen.getByRole("dialog", { name: "리뷰 삭제" });
```

Alert:

```tsx
screen.getByRole("alert");
```

Expanded state:

```tsx
expect(screen.getByRole("button", { name: "필터" })).toHaveAttribute(
  "aria-expanded",
  "true",
);
```

Selected tab:

```tsx
expect(screen.getByRole("tab", { name: "리뷰" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

실무 기준:

- `getByRole` 실패 시 semantic role과 accessible name 확인
- `getByLabelText` 실패 시 label 연결 확인
- aria state는 실제 UI state와 함께 검증
- `getByTestId`는 ARIA 오류를 숨길 수 있음
- Dialog, Dropdown, Tab은 role/name/state 검증 필요

---

### [FAQ]

Q. getByRole이 실패하면 ARIA 문제야?
A. 가능성이 있다. role, accessible name, hidden 상태를 확인해야 한다.

Q. icon button은 어떻게 테스트해?
A. getByRole("button", { name: "알림 열기" })처럼 accessible name으로 찾는다.

Q. aria-expanded도 테스트해야 해?
A. Dropdown이나 Accordion처럼 open 상태가 중요한 경우 실제 상태와 동기화되는지 확인하는 것이 좋다.

Q. testId로 찾으면 ARIA 검증이 필요 없어?
A. 아니다. testId는 접근성 구조를 검증하지 못할 수 있다.

---

## 9.2 axe ARIA Checks

### [개념]

axe 같은 접근성 자동화 도구는 ARIA 속성 오류, role 불일치, label 누락 같은 일부 문제를 탐지할 수 있다.

하지만 keyboard 흐름, focus 의도, 문구 품질, 사용자 맥락은 자동으로 완전히 검증하지 못한다.

---

### [핵심]

axe가 탐지할 수 있는 예:

- invalid ARIA attribute
- invalid ARIA role
- missing accessible name
- form label missing
- aria reference broken
- aria-hidden focus issue 일부
- role required children 누락
- role required parent 누락

한계:

- keyboard flow 전체
- focus return 의도
- aria label 문구 품질
- custom widget 사용성
- screen reader 실제 경험
- 사용자 task 맥락

---

### [실무]

axe 적용 우선순위:

```text
Common Components
→ Form
→ Modal
→ Dropdown
→ Tab
→ Navigation
→ Table
→ Page Template
```

검수 기준:

- axe 오류를 무조건 무시하지 않음
- 오류 메시지의 role / aria reference를 확인
- 수동 keyboard test와 함께 사용
- Testing Library Query와 함께 사용
- CI 연동은 별도 Advanced 문서에서 관리

실무 기준:

- ARIA 오류는 자동화 도구로 일부 탐지 가능
- axe 통과가 접근성 완료를 의미하지 않음
- 수동 keyboard / focus 점검 필수
- role이 복잡한 component는 별도 테스트 필요

---

### [FAQ]

Q. axe는 ARIA 오류를 잡아줘?
A. 일부 invalid role, aria reference, accessible name 누락 등을 잡을 수 있다.

Q. axe 테스트 통과하면 접근성 문제 없는 거야?
A. 아니다. keyboard, focus, 사용자 맥락 문제는 자동화 도구가 잡지 못할 수 있다.

Q. axe는 어디에 우선 적용해?
A. Form, Modal, Navigation, 공통 UI Component처럼 접근성 영향이 큰 곳에 우선 적용한다.

Q. axe와 Testing Library 중 하나만 쓰면 돼?
A. 아니다. 서로 보완 관계다. role/name query와 자동화 검사를 함께 사용하는 것이 좋다.

---

# 10. ARIA Review

## 10.1 ARIA Review Checklist

### [개념]

ARIA Review는 ARIA가 필요한 곳에만 사용되었는지, 실제 UI 상태와 동기화되는지, Semantic HTML을 대체하지 않았는지 검토하는 과정이다.

Review Agent는 ARIA를 많이 쓴 코드를 좋은 코드로 판단하지 말고, 필요한 ARIA인지 먼저 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Native HTML로 대체 가능한 role 사용이 없는가?
- [ ] button 역할에 button 태그를 우선 사용했는가?
- [ ] link 역할에 a 또는 Link를 우선 사용했는가?
- [ ] role과 keyboard 동작이 일치하는가?
- [ ] interactive element에 accessible name이 있는가?
- [ ] icon only button에 aria-label이 있는가?
- [ ] aria-label과 visible text가 충돌하지 않는가?
- [ ] aria-labelledby 참조 id가 존재하는가?
- [ ] aria-describedby 참조 id가 존재하는가?
- [ ] aria-invalid가 실제 error 상태와 일치하는가?
- [ ] aria-expanded가 실제 open 상태와 일치하는가?
- [ ] aria-selected가 실제 selected 상태와 일치하는가?
- [ ] aria-current가 현재 페이지 / 단계와 일치하는가?
- [ ] aria-hidden 내부에 focus 가능한 요소가 없는가?
- [ ] role alert를 남발하지 않았는가?
- [ ] role status가 loading / success 상태에 적절히 사용되었는가?
- [ ] Dialog에 role, aria-modal, aria-labelledby가 있는가?
- [ ] Dropdown role 선택이 목적에 맞는가?
- [ ] Tab role과 tabpanel 연결이 올바른가?
- [ ] Testing Library getByRole로 검증 가능한가?
```

---

### [실무]

Review Flow:

```text
ARIA 발견
→ Native HTML 대체 가능 여부 확인
→ role 적합성 확인
→ accessible name 확인
→ ARIA 참조 id 확인
→ ARIA state 동기화 확인
→ keyboard 동작 확인
→ hidden / focus 충돌 확인
→ Testing Library Query 확인
```

대표 수정 패턴:

```text
문제: div role="button" + keyboard 미구현
해결: button type="button"으로 변경
```

```text
문제: aria-expanded 하드코딩
해결: open state와 동기화
```

```text
문제: aria-describedby가 없는 id 참조
해결: 실제 렌더링되는 helper/error id와 연결
```

```text
문제: aria-hidden 내부 button 존재
해결: interactive element를 aria-hidden 영역 밖으로 이동하거나 숨김 처리 방식 변경
```

---

### [FAQ]

Q. ARIA Review에서 가장 먼저 볼 것은?
A. Native HTML로 대체 가능한지와 ARIA 상태가 실제 UI 상태와 동기화되는지 먼저 본다.

Q. ARIA가 많으면 접근성이 좋은 코드야?
A. 아니다. 필요한 ARIA만 정확히 쓰는 것이 좋다.

Q. aria 참조 id가 없으면 문제야?
A. 문제다. aria-labelledby나 aria-describedby가 참조하는 id는 실제 DOM에 존재해야 한다.

Q. Review Agent는 role과 keyboard도 같이 봐야 해?
A. 봐야 한다. role만 있고 keyboard 동작이 없으면 접근성 문제가 된다.

---

# 11. Common ARIA Mistakes

## 11.1 ARIA Anti Patterns

### [개념]

ARIA Anti Pattern은 접근성을 개선하려고 추가한 ARIA가 오히려 잘못된 의미, 잘못된 상태, keyboard 불일치를 만드는 구현 방식이다.

ARIA는 정확히 사용해야 하며, Semantic HTML을 대체하는 용도로 남용하면 안 된다.

---

### [핵심]

자주 발생하는 실수:

- `button` 대신 `div role="button"` 사용
- `role="button"`만 있고 keyboard 미구현
- `button role="button"` 불필요한 중복
- `aria-label`이 visible text와 다른 의미
- icon button에 accessible name 없음
- `aria-expanded` 실제 open 상태 불일치
- `aria-selected` 실제 selected 상태 불일치
- `aria-current` 현재 위치 불일치
- `aria-invalid` 오류 상태 불일치
- `aria-describedby` 없는 id 참조
- `aria-labelledby` 중복 id 참조
- `aria-hidden` 내부 focusable element 존재
- `role="alert"` 남발
- Dialog에 accessible name 없음
- Tab과 TabPanel id 관계 불일치
- Menu role을 단순 disclosure에 남용
- Custom Select role만 있고 keyboard 미구현
- live region이 너무 자주 업데이트됨

---

### [실무]

Anti Pattern:

```jsx
<div role="button" onClick={onSave}>
  저장
</div>
```

개선:

```jsx
<button type="button" onClick={onSave}>
  저장
</button>
```

Anti Pattern:

```jsx
<button aria-label="삭제">저장</button>
```

개선:

```jsx
<button type="button">저장</button>
```

Anti Pattern:

```jsx
<input id="email" aria-describedby="email-error" />
```

문제:

```text
email-error id를 가진 error message가 실제 DOM에 없음
```

개선:

```jsx
<input id="email" aria-describedby={error ? "email-error" : undefined} />;
{
  error && <p id="email-error">이메일을 입력해 주세요.</p>;
}
```

Anti Pattern:

```jsx
<div aria-hidden="true">
  <button type="button">닫기</button>
</div>
```

개선:

```text
aria-hidden 영역 내부에 focus 가능한 button을 두지 않는다.
```

---

### [FAQ]

Q. ARIA 초보가 가장 많이 하는 실수는?
A. div role button 사용, aria-expanded 불일치, aria-describedby id 누락, aria-hidden 내부 focus 요소 문제가 많다.

Q. aria-label이 visible text와 다르면 왜 문제야?
A. 보는 사용자와 보조기술 사용자가 서로 다른 의미를 받게 되어 혼란이 생긴다.

Q. role alert를 많이 쓰면 더 잘 알려줘?
A. 아니다. 너무 많은 alert는 사용자를 방해할 수 있다.

Q. Menu role은 Dropdown에 항상 써야 해?
A. 아니다. 단순 펼침 UI는 disclosure pattern이 더 적합할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. ARIA가 뭐야?
A. HTML만으로 표현하기 어려운 역할, 상태, 관계를 보조기술에 전달하는 속성이다.

Q. ARIA는 왜 필요해?
A. Semantic HTML만으로 부족한 이름, 상태, 관계 정보를 보조기술에 전달하기 위해 필요하다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다.

Q. ARIA는 언제 써?
A. Semantic HTML만으로 역할, 상태, 관계를 충분히 전달하기 어려울 때 보완적으로 사용한다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

Q. 잘못된 ARIA가 왜 위험해?
A. 보조기술 사용자에게 실제 UI와 다른 정보를 전달할 수 있기 때문이다.

Q. aria-expanded를 true로 고정하면 안 돼?
A. 안 된다. 실제 open 상태와 항상 동기화되어야 한다.

Q. role만 붙이면 접근성 문제가 해결돼?
A. 아니다. role에 맞는 keyboard 동작과 상태 관리가 함께 필요하다.

Q. ARIA를 쓰지 않는 게 나을 때도 있어?
A. 그렇다. 잘못 쓰는 ARIA보다 Semantic HTML만 정확히 쓰는 편이 더 안전할 수 있다.

Q. role은 언제 써?
A. Native HTML만으로 역할을 표현하기 어려운 custom widget에서 보완적으로 사용한다.

Q. button에 role="button"을 붙여야 해?
A. 필요 없다. button은 기본적으로 button role을 가진다.

Q. nav에 role="navigation"을 붙여야 해?
A. 대부분 필요 없다. nav는 기본 navigation landmark 역할을 가진다.

Q. role을 바꾸면 keyboard 동작도 바뀌어?
A. 아니다. role은 의미 전달이고 keyboard 동작은 별도로 구현해야 할 수 있다.

Q. role="button"을 쓰면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다.

Q. role과 실제 동작이 다르면 왜 문제야?
A. 보조기술 사용자가 기대한 조작과 실제 조작이 달라져 사용성이 떨어진다.

Q. role="link"를 붙이면 Enter로 이동해?
A. role만으로 이동 동작이 생기지 않는다. 실제 link는 href가 있는 a 또는 Link를 사용하는 것이 좋다.

Q. Custom Widget은 어떻게 검증해?
A. role, accessible name, keyboard 동작, focus 흐름을 함께 테스트한다.

Q. Accessible Name이 뭐야?
A. 스크린 리더와 Testing Library가 요소의 이름으로 인식하는 텍스트다.

Q. accessible name은 어떻게 제공해?
A. visible text, label, aria-label, aria-labelledby, alt text 등을 사용할 수 있다.

Q. visible text가 있으면 aria-label이 꼭 필요해?
A. 아니다. visible text가 명확하면 그것이 accessible name으로 사용될 수 있다.

Q. getByRole에서 name이 안 잡히는 이유는?
A. 요소에 accessible name이 없거나 기대한 이름과 실제 이름이 다를 수 있다.

Q. 같은 이름의 버튼이 여러 개면 문제야?
A. 문맥이 부족할 수 있다. 대상 이름을 포함해 구체화하는 것이 좋다.

Q. aria-label은 언제 써?
A. 화면에 보이는 이름이 없거나 부족할 때 보조기술에 이름을 제공하기 위해 사용한다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. aria-label이 visible text와 달라도 돼?
A. 의미가 충돌하면 안 된다. 사용자가 보는 이름과 보조기술 이름은 일관되어야 한다.

Q. aria-label에 자세한 설명을 길게 써도 돼?
A. 권장하지 않는다. 이름은 짧고 명확하게 제공하고 긴 설명은 aria-describedby를 고려한다.

Q. aria-labelledby는 언제 써?
A. 화면에 이미 있는 텍스트를 요소의 accessible name으로 연결할 때 사용한다.

Q. aria-label과 aria-labelledby 중 뭐가 좋아?
A. 보이는 텍스트를 재사용할 수 있다면 aria-labelledby가 더 명확하다.

Q. aria-labelledby에 여러 id를 넣을 수 있어?
A. 가능하다. 공백으로 여러 id를 연결할 수 있다.

Q. aria-labelledby가 동작하지 않는 이유는?
A. 참조 id가 없거나 중복되었거나 해당 요소가 렌더링되지 않았을 수 있다.

Q. aria-describedby는 언제 써?
A. input 조건, helper text, error message 같은 추가 설명을 연결할 때 사용한다.

Q. aria-label과 aria-describedby 차이는?
A. aria-label은 요소의 이름이고 aria-describedby는 요소의 추가 설명이다.

Q. error message는 aria-describedby로 연결해?
A. 그렇다. error id를 만들고 input의 aria-describedby에 연결한다.

Q. aria-describedby에 여러 id를 넣을 수 있어?
A. 가능하다. helper text와 error message를 함께 연결할 수 있다.

Q. aria-invalid는 언제 true야?
A. 해당 input의 현재 값이 validation 기준을 통과하지 못한 상태일 때 true로 설정한다.

Q. aria-invalid만 있으면 오류 전달이 충분해?
A. 아니다. 사용자가 수정할 수 있도록 error message도 함께 제공해야 한다.

Q. 오류가 없을 때 aria-invalid는 어떻게 해?
A. false로 두거나 속성을 생략할 수 있다.

Q. 빨간 테두리와 aria-invalid만 있으면 돼?
A. 아니다. 오류 원인과 수정 방법을 설명하는 텍스트가 필요하다.

Q. aria-expanded는 언제 써?
A. Dropdown, Accordion처럼 열림 / 닫힘 상태가 있는 trigger에서 사용한다.

Q. aria-expanded는 어디에 붙여?
A. 열고 닫는 trigger button에 붙인다.

Q. aria-expanded는 실제 open 상태와 같아야 해?
A. 그렇다. 실제 UI 상태와 항상 동기화되어야 한다.

Q. aria-controls도 꼭 필요해?
A. 필수는 아니지만 trigger와 panel 관계를 명확히 하는 데 도움이 될 수 있다.

Q. aria-selected는 언제 써?
A. Tab, Listbox Option처럼 선택 가능한 항목의 선택 상태를 전달할 때 사용한다.

Q. focus와 selected는 같은 거야?
A. 아니다. focus는 keyboard 위치이고 selected는 선택된 상태다.

Q. Tab에서 aria-selected는 어디에 붙여?
A. role="tab" 요소에 붙이고 실제 선택된 tab과 일치시킨다.

Q. aria-selected만 있으면 시각적 선택 표시가 필요 없어?
A. 아니다. 시각적으로도 선택 상태가 보여야 한다.

Q. aria-current는 언제 써?
A. 현재 페이지, 현재 단계, 현재 위치를 navigation이나 step 목록에서 전달할 때 사용한다.

Q. 현재 메뉴는 어떻게 표시해?
A. 시각적 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. aria-current와 aria-selected 차이는?
A. aria-current는 현재 위치를 나타내고 aria-selected는 선택 가능한 항목의 선택 상태를 나타낸다.

Q. Breadcrumb 마지막 항목에도 aria-current를 써?
A. 현재 페이지를 나타내기 위해 aria-current="page"를 사용할 수 있다.

Q. aria-busy는 언제 써?
A. 특정 영역이 로딩 중이거나 업데이트 중임을 전달할 때 사용할 수 있다.

Q. aria-busy만 있으면 loading 접근성이 충분해?
A. 아니다. 사용자가 이해할 수 있는 loading text나 role status도 함께 제공하는 것이 좋다.

Q. 버튼에도 aria-busy를 쓸 수 있어?
A. 저장 중, 로그인 중 같은 처리 상태를 전달할 때 사용할 수 있다.

Q. spinner만 보여주면 안 돼?
A. 스크린 리더 사용자를 위해 loading text를 함께 제공해야 한다.

Q. aria-controls는 언제 써?
A. trigger가 특정 panel, menu, tabpanel을 제어한다는 관계를 전달할 때 사용한다.

Q. aria-controls가 있으면 자동으로 열리고 닫혀?
A. 아니다. 관계만 전달하고 open / close 동작은 직접 구현해야 한다.

Q. aria-controls는 aria-expanded와 같이 써?
A. Dropdown, Accordion 같은 열림 상태 UI에서는 함께 사용할 수 있다.

Q. aria-controls가 안 먹는 이유는?
A. 참조하는 id가 없거나 중복되었거나 실제 DOM에 없을 수 있다.

Q. aria-modal은 언제 써?
A. Modal Dialog가 열린 동안 배경 콘텐츠와 상호작용하지 않는 상태를 전달할 때 사용한다.

Q. aria-modal만 붙이면 Modal 접근성이 끝이야?
A. 아니다. focus 이동, focus trap, focus return, 닫기 버튼도 필요하다.

Q. dialog와 alertdialog 차이는?
A. dialog는 일반 대화상자이고 alertdialog는 긴급하거나 중요한 확인이 필요한 대화상자다.

Q. Modal에는 aria-labelledby가 필요해?
A. 권장한다. Dialog의 제목을 accessible name으로 연결해야 한다.

Q. aria-hidden은 언제 써?
A. 장식 아이콘이나 중복 시각 요소처럼 보조기술이 읽지 않아도 되는 요소를 숨길 때 사용한다.

Q. aria-hidden 안에 button이 있으면 왜 문제야?
A. focus 가능한 요소가 보조기술에는 숨겨져 keyboard와 screen reader 흐름이 충돌할 수 있다.

Q. 아이콘 버튼 내부 아이콘에는 aria-hidden을 써?
A. 보통 icon은 장식 처리하고 button에 aria-label을 제공한다.

Q. 중요한 메시지를 aria-hidden으로 숨겨도 돼?
A. 안 된다. 사용자에게 필요한 정보는 보조기술에도 전달되어야 한다.

Q. hidden과 visually hidden은 뭐가 달라?
A. hidden은 보조기술에서도 숨기고 visually hidden은 화면에서만 숨기며 스크린 리더에는 제공한다.

Q. label을 화면에서 숨겨도 돼?
A. 가능하다. sr-only 방식으로 스크린 리더에는 제공할 수 있다.

Q. Skip Link도 sr-only로 숨기면 돼?
A. 기본적으로 숨길 수 있지만 keyboard focus 시 화면에 보여야 한다.

Q. display none 요소는 스크린 리더가 읽어?
A. 일반적으로 읽지 않는다. 보조기술에도 숨겨지는 것으로 봐야 한다.

Q. aria-live는 언제 써?
A. 화면이 동적으로 바뀌고 그 변경을 보조기술 사용자에게 알려야 할 때 사용한다.

Q. polite와 assertive 차이는?
A. polite는 현재 읽기 흐름을 방해하지 않고 알리고 assertive는 더 즉시 알리는 방식이다.

Q. role="alert"와 aria-live는 뭐가 달라?
A. role="alert"는 중요한 오류나 긴급 메시지를 즉시 알리는 데 사용되고 aria-live="polite"는 덜 긴급한 변경을 자연스럽게 알린다.

Q. Toast에도 aria-live가 필요해?
A. Toast가 중요한 상태 메시지를 전달한다면 보조기술 사용자가 인식할 수 있게 live region을 고려한다.

Q. role="status"는 언제 써?
A. loading, 저장 완료, 검색 결과 수처럼 긴급하지 않은 상태 변경을 알릴 때 사용한다.

Q. role status와 role alert 차이는?
A. status는 덜 긴급한 상태 알림이고 alert는 즉시 알려야 하는 오류나 중요한 메시지에 사용한다.

Q. spinner에 role status만 붙이면 돼?
A. spinner만으로는 부족하다. “데이터를 불러오는 중입니다” 같은 텍스트가 필요하다.

Q. 검색 결과 개수에도 role status를 쓸 수 있어?
A. 검색 결과가 동적으로 바뀐다면 사용할 수 있다.

Q. role="alert"는 언제 써?
A. 사용자가 즉시 알아야 하는 중요한 오류나 경고 메시지에 사용한다.

Q. 모든 에러 메시지에 role alert를 붙여도 돼?
A. 남발하면 사용자를 방해할 수 있다. 중요한 오류에 신중히 사용한다.

Q. role alert만 있으면 field error 연결은 필요 없어?
A. field error라면 input과 aria-describedby로 연결하는 것이 좋다.

Q. 서버 오류를 alert로 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Dialog에는 어떤 ARIA가 필요해?
A. role dialog, aria-modal, aria-labelledby를 기본으로 고려하고 설명이 있으면 aria-describedby를 연결한다.

Q. alertdialog는 언제 써?
A. 삭제 확인처럼 긴급하거나 중요한 결정을 요구하는 Dialog에서 고려한다.

Q. aria-modal만 붙이면 focus trap이 생겨?
A. 아니다. focus trap은 별도로 구현해야 한다.

Q. Dialog accessible name은 어떻게 정해?
A. 보통 Dialog title을 aria-labelledby로 연결해 제공한다.

Q. Dropdown에는 무조건 role="menu"를 써?
A. 아니다. 단순 펼침이면 disclosure pattern이 적합할 수 있고 선택 UI면 listbox나 native select를 검토한다.

Q. aria-haspopup는 언제 써?
A. trigger가 menu, listbox, dialog 같은 popup을 연다는 것을 전달할 때 사용한다.

Q. Dropdown item은 role menuitem이면 끝이야?
A. 아니다. menu keyboard pattern과 focus 관리도 필요하다.

Q. 단순 필터 패널 열기는 menu야?
A. 보통 menu보다 disclosure button + panel 구조가 더 적합할 수 있다.

Q. Tab에는 어떤 ARIA가 필요해?
A. tablist, tab, tabpanel role과 aria-selected, aria-controls, aria-labelledby 연결을 고려한다.

Q. aria-selected는 tab에 붙여?
A. 그렇다. 선택된 role="tab"에 aria-selected true를 설정한다.

Q. hidden tabpanel에 focus가 가면 문제야?
A. 문제다. 보이지 않는 panel 내부 요소에 focus가 가지 않게 해야 한다.

Q. getByRole이 실패하면 ARIA 문제야?
A. 가능성이 있다. role, accessible name, hidden 상태를 확인해야 한다.

Q. icon button은 어떻게 테스트해?
A. getByRole("button", { name: "알림 열기" })처럼 accessible name으로 찾는다.

Q. aria-expanded도 테스트해야 해?
A. Dropdown이나 Accordion처럼 open 상태가 중요한 경우 실제 상태와 동기화되는지 확인하는 것이 좋다.

Q. testId로 찾으면 ARIA 검증이 필요 없어?
A. 아니다. testId는 접근성 구조를 검증하지 못할 수 있다.

Q. axe는 ARIA 오류를 잡아줘?
A. 일부 invalid role, aria reference, accessible name 누락 등을 잡을 수 있다.

Q. axe 테스트 통과하면 접근성 문제 없는 거야?
A. 아니다. keyboard, focus, 사용자 맥락 문제는 자동화 도구가 잡지 못할 수 있다.

Q. ARIA Review에서 가장 먼저 볼 것은?
A. Native HTML로 대체 가능한지와 ARIA 상태가 실제 UI 상태와 동기화되는지 먼저 본다.

Q. ARIA가 많으면 접근성이 좋은 코드야?
A. 아니다. 필요한 ARIA만 정확히 쓰는 것이 좋다.

Q. aria 참조 id가 없으면 문제야?
A. 문제다. aria-labelledby나 aria-describedby가 참조하는 id는 실제 DOM에 존재해야 한다.

Q. ARIA 초보가 가장 많이 하는 실수는?
A. div role button 사용, aria-expanded 불일치, aria-describedby id 누락, aria-hidden 내부 focus 요소 문제가 많다.
