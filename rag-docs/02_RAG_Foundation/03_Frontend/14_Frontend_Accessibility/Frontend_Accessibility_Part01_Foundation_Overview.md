# Frontend Accessibility Part01 - Foundation Overview

---

# 1. Frontend Accessibility Foundation

## 1.1 Accessibility Purpose

### [개념]

Frontend Accessibility는 사용자가 마우스, 키보드, 스크린 리더, 보조기술, 저시력 환경, 색각 이상 환경에서도 Frontend UI를 사용할 수 있게 만드는 기준이다.

접근성은 별도 기능이 아니라 HTML 구조, Component 설계, Form 처리, Error UX, Loading UX, Testing 전체에 포함되는 품질 기준이다.

Frontend Accessibility 문서는 Frontend Agent / Review Agent / PM Agent가 접근성 있는 React UI를 작성하고 검토하기 위한 RAG 기준 문서다.

---

### [핵심]

Frontend Accessibility 핵심 목표:

- Semantic HTML 우선
- Keyboard Accessibility 보장
- Focus Management 검토
- Accessible Name 제공
- Form Label 연결
- Error Message 접근성 적용
- ARIA는 보완적으로 사용
- Button / Link 역할 구분
- Image Alt Text 판단
- Color Only Meaning 방지
- Loading / Error / Empty State 전달
- Modal / Dropdown / Tab 접근성 검토
- Testing Library 접근성 Query 활용
- axe 자동화 테스트 보완 사용

---

### [실무]

2026 실무 기준에서 Frontend Accessibility는 `aria-label`을 많이 붙이는 작업이 아니다.

실무 접근성 우선순위:

```text
Semantic HTML
→ Keyboard Navigation
→ Focus Visible
→ Accessible Name
→ Label Connection
→ Error Message Connection
→ ARIA State Sync
→ Manual Keyboard Test
→ Testing Library Query
→ axe Basic Check
```

Frontend Agent는 UI 구현 시 아래를 기본 검토한다.

- 클릭 액션에 `button` 사용
- 페이지 이동에 `Link` 또는 `a` 사용
- `div onClick` 남용 방지
- `input`과 `label` 연결
- `placeholder`를 label 대체로 사용하지 않음
- 오류 메시지를 input과 연결
- 키보드만으로 주요 기능 사용 가능
- focus outline 제거 금지
- 아이콘 버튼에 accessible name 제공
- 색상만으로 상태 전달 금지
- Modal 열림 / 닫힘 시 focus 이동 검토
- Loading / Error 상태를 보조기술에 전달

---

### [FAQ]

Q. Frontend Accessibility는 왜 필요해?
A. 사용자가 키보드, 스크린 리더, 보조기술 등 다양한 방식으로 UI를 사용할 수 있어야 하기 때문이다.

Q. 접근성은 별도 기능이야?
A. 아니다. HTML 구조, Component 설계, Form 처리, Error UX, Testing 전체에 포함되는 품질 기준이다.

Q. aria-label만 잘 붙이면 접근성이 해결돼?
A. 아니다. 먼저 Semantic HTML을 사용하고 부족한 의미만 ARIA로 보완해야 한다.

Q. 접근성은 디자인 끝난 뒤에 추가하면 돼?
A. 권장하지 않는다. Semantic HTML, label, focus, keyboard 흐름은 Component 설계 단계부터 포함해야 한다.

---

# 2. Accessibility Priority

## 2.1 Core Priority

### [개념]

Frontend Accessibility Priority는 접근성 구현과 검토에서 무엇을 먼저 판단해야 하는지 정하는 기준이다.

접근성 문제는 대부분 잘못된 HTML 의미, 키보드 조작 누락, label 누락, focus 처리 누락에서 시작된다.

---

### [핵심]

우선순위:

1. Semantic HTML
2. Keyboard Accessibility
3. Focus Management
4. Accessible Name
5. Label
6. Form Accessibility
7. Error Message Accessibility
8. ARIA Basics
9. Button / Link Semantics
10. Image Alt Text
11. Color Contrast
12. Modal Accessibility
13. Dropdown Accessibility
14. Tab Accessibility
15. Loading / Error Accessibility
16. React Accessibility
17. Accessibility Testing

---

### [실무]

접근성 검토 Flow:

```text
UI Element 확인
→ 역할 판단
→ Native HTML 사용 가능 여부 확인
→ Keyboard 조작 확인
→ Accessible Name 확인
→ Focus 이동 확인
→ ARIA 상태 동기화 확인
→ Error / Loading / Empty State 확인
→ Testing Library Query 검증
```

실무 판단 기준:

- Native HTML로 가능하면 Native HTML 사용
- `role`을 붙이기 전에 적절한 태그가 있는지 확인
- `button`, `input`, `select`, `textarea`, `a`, `label` 우선 사용
- Custom Component는 role / keyboard / focus / aria 상태를 직접 구현해야 함
- 접근성 테스트는 자동화만으로 끝내지 않음
- keyboard only manual check를 반드시 고려

---

### [FAQ]

Q. 접근성 검토에서 가장 먼저 볼 것은?
A. Semantic HTML, keyboard 조작, label 연결, focus visible, error message 연결을 먼저 확인한다.

Q. Native HTML을 우선해야 하는 이유는?
A. 기본 role, keyboard 동작, focus 동작이 이미 제공되기 때문에 접근성 누락 위험이 낮다.

Q. Custom Component는 접근성에 불리해?
A. 가능하지만 keyboard, role, focus, aria 상태를 직접 구현해야 하므로 검토 비용이 높다.

Q. 자동화 테스트만 통과하면 접근성 문제 없는 거야?
A. 아니다. keyboard 흐름, focus 이동, 사용자 맥락은 수동 확인이 필요하다.

---

# 3. Included Scope

## 3.1 Frontend Accessibility Scope

### [개념]

Frontend Accessibility 문서는 React Frontend에서 접근성 있는 UI를 설계, 구현, 검토하기 위한 기본 범위를 포함한다.

이 문서는 Foundation 단계의 접근성 기준이며, 법적 감사 수준의 WCAG 전체 조항이나 보조기술별 심화 검증은 제외한다.

---

### [핵심]

포함 범위:

- Semantic HTML
- Landmark
- Heading Structure
- Button Accessibility
- Link Accessibility
- Form Accessibility
- Label
- Accessible Name
- Keyboard Navigation
- Focus Management
- Focus Visible
- Tab Order
- Skip Link Basics
- Image Alt Text
- Icon Button Accessibility
- Color Contrast Basics
- Color Only Meaning
- Error Message Accessibility
- Loading Accessibility
- Empty State Accessibility
- Modal / Dialog Accessibility
- Dropdown Accessibility
- Tab Accessibility
- Accordion Accessibility
- Table Accessibility
- List Accessibility
- React Conditional Rendering Accessibility
- Accessibility Testing Basics
- Testing Library Accessibility Query
- axe Basics
- Common Accessibility Mistakes

---

### [실무]

Frontend Accessibility는 다음 Frontend 문서와 연결된다.

```text
HTML / CSS Foundation
→ React Core
→ React Component Design
→ UI Component Pattern
→ Form Handling & Validation
→ Error Handling & Loading UX
→ Frontend Testing
→ Frontend Accessibility
→ Frontend Code Review
```

실무 포함 기준:

- Agent가 UI 작성 시 바로 적용할 수 있는 규칙
- Review Agent가 코드 리뷰에서 찾을 수 있는 기준
- Testing Agent가 `getByRole`, `getByLabelText` 실패 원인을 분석할 수 있는 기준
- PM Agent가 접근성 요구사항을 작업 조건으로 변환할 수 있는 기준

---

### [FAQ]

Q. Frontend Accessibility 문서는 UI Component Pattern과 뭐가 달라?
A. UI Component Pattern은 Component 설계 기준이고 Frontend Accessibility는 키보드, 스크린 리더, focus, label 등 사용 가능성 기준이다.

Q. 접근성은 Testing 문서와 연결돼?
A. 그렇다. Testing Library의 getByRole, getByLabelText는 접근성 구조를 기반으로 요소를 찾는다.

Q. 접근성은 Error Handling 문서와 연결돼?
A. 그렇다. 오류 메시지는 사용자가 인식하고 수정할 수 있도록 input과 연결되어야 한다.

Q. 접근성은 Form Handling 문서와 연결돼?
A. 그렇다. label, required, validation, error message는 Form 접근성의 핵심이다.

---

# 4. Excluded Scope

## 4.1 Out of Scope

### [개념]

Frontend Accessibility Foundation 문서는 기본 실무 접근성 기준에 집중한다.

법적 감사, 고급 스크린 리더 검증, 복잡한 ARIA Widget 구현은 Foundation 범위를 초과하므로 별도 Advanced 문서에서 다룬다.

---

### [핵심]

제외 범위:

- WCAG 전체 조항 심화
- 법적 접근성 감사 문서
- Screen Reader별 상세 사용법
- NVDA / JAWS / VoiceOver 심화
- 고급 Focus Trap 구현
- Complex ARIA Widget 심화
- Accessibility Audit Report 심화
- Accessibility Automation Pipeline
- Cross Browser Assistive Technology Matrix
- Mobile Accessibility 심화
- International Accessibility Compliance 심화

---

### [실무]

고급 접근성 문서 분리 기준:

```text
Frontend Accessibility Foundation
→ Advanced Accessibility
→ Accessibility Audit
→ Design System Accessibility
→ Accessibility Testing Pipeline
```

Foundation 문서에서는 아래 수준까지만 다룬다.

- 실무 Component 작성 기준
- 기본 Keyboard 조작 기준
- 기본 Focus Management 기준
- 기본 ARIA 속성 사용 기준
- Testing Library Query 기반 접근성 검증
- axe 기초 자동화 검증

---

### [FAQ]

Q. WCAG 전체를 외워야 해?
A. Foundation 단계에서는 Semantic HTML, keyboard, label, focus, color contrast, error message 같은 핵심 기준부터 적용한다.

Q. 스크린 리더별 상세 테스트도 여기서 다뤄?
A. 아니다. 이 문서는 기본 구현과 검토 기준 중심이다.

Q. 법적 접근성 감사 문서로 사용할 수 있어?
A. 아니다. 이 문서는 Agent용 RAG 기준이며 법적 감사 보고서가 아니다.

Q. 복잡한 ARIA Widget은 여기서 구현해?
A. 아니다. Foundation에서는 기본 원칙을 다루고 복잡한 Widget은 Advanced 문서에서 다룬다.

---

# 5. Semantic HTML First

## 5.1 Semantic HTML Principle

### [개념]

Semantic HTML은 HTML 요소를 의미에 맞게 사용하는 방식이다.

Frontend Accessibility의 기본은 ARIA를 많이 사용하는 것이 아니라 올바른 HTML 태그를 먼저 선택하는 것이다.

---

### [핵심]

우선 사용 요소:

- `button`
- `a`
- `input`
- `label`
- `form`
- `fieldset`
- `legend`
- `header`
- `nav`
- `main`
- `section`
- `article`
- `aside`
- `footer`
- `ul`
- `ol`
- `li`
- `table`
- `thead`
- `tbody`
- `th`
- `td`

---

### [실무]

좋은 예:

```jsx
<button type="button" onClick={onOpen}>
  메뉴 열기
</button>
```

나쁜 예:

```jsx
<div onClick={onOpen}>메뉴 열기</div>
```

실무 기준:

- 클릭 액션은 `button`
- 페이지 이동은 `a` 또는 `Link`
- Form 입력은 `input`, `select`, `textarea`
- 입력 설명은 `label`
- 반복 항목은 `ul`, `ol`, `li`
- 표 데이터는 `table`
- 페이지 주요 콘텐츠는 `main`
- 네비게이션은 `nav`
- 의미 없는 `div`, `span` 남용 지양

---

### [FAQ]

Q. div에 onClick을 붙이면 안 돼?
A. 가능은 하지만 keyboard 접근성과 의미가 부족하다. 클릭 액션은 button을 사용하는 것이 좋다.

Q. role을 붙이면 div도 button처럼 되는 거 아니야?
A. 일부 의미는 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다. 가능하면 button을 사용한다.

Q. Semantic HTML이 접근성에서 중요한 이유는?
A. 브라우저와 보조기술이 요소의 역할을 기본적으로 이해할 수 있기 때문이다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

---

# 6. ARIA as Supplement

## 6.1 ARIA Principle

### [개념]

ARIA는 HTML만으로 표현하기 어려운 역할, 상태, 관계를 보조기술에 전달하는 속성이다.

ARIA는 Semantic HTML을 대체하는 도구가 아니라 보완하는 도구다.

---

### [핵심]

ARIA 원칙:

- Semantic HTML 우선
- 필요한 경우에만 ARIA 사용
- 잘못된 ARIA는 없는 것보다 나쁠 수 있음
- role과 keyboard 동작이 일치해야 함
- aria 상태는 실제 UI 상태와 동기화
- interactive element에는 accessible name 필요
- 숨김 상태와 focus 상태 충돌 주의

---

### [실무]

자주 사용하는 ARIA:

```text
aria-label
aria-labelledby
aria-describedby
aria-invalid
aria-expanded
aria-selected
aria-current
aria-hidden
aria-live
aria-busy
```

실무 예:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="menu-list"
  onClick={toggleOpen}
>
  메뉴
</button>
```

주의:

- `aria-expanded`는 실제 open 상태와 일치해야 함
- `aria-invalid`는 실제 validation 상태와 일치해야 함
- `aria-hidden` 내부에 focus 가능한 요소가 있으면 문제 가능
- `role="button"`을 쓰면 Enter / Space keyboard 처리 필요
- 불필요한 role 중복 지양

---

### [FAQ]

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다.

Q. ARIA는 언제 써?
A. Semantic HTML만으로 역할, 상태, 관계를 충분히 전달하기 어려울 때 보완적으로 사용한다.

Q. aria-expanded는 언제 써?
A. Dropdown, Accordion처럼 열림 / 닫힘 상태가 있는 trigger에서 실제 open 상태와 동기화해 사용한다.

Q. aria-hidden은 언제 조심해야 해?
A. aria-hidden 요소 안에 focus 가능한 요소가 있으면 보조기술과 keyboard 흐름이 충돌할 수 있다.

---

# 7. Keyboard Accessibility Foundation

## 7.1 Keyboard First Check

### [개념]

Keyboard Accessibility는 마우스 없이 Tab, Shift+Tab, Enter, Space, Escape, Arrow Key 등으로 UI를 사용할 수 있게 하는 기준이다.

키보드 접근성은 접근성 검토에서 가장 중요한 수동 점검 항목이다.

---

### [핵심]

검토 대상:

- Tab 이동
- Shift+Tab 역방향 이동
- Enter 실행
- Space 실행
- Escape 닫기
- Arrow Key 이동
- Focus Visible
- Tab Order
- Modal Focus
- Dropdown Keyboard
- Tab Component Keyboard
- Skip Link Basics

---

### [실무]

Keyboard 점검 Flow:

```text
마우스 사용 금지
→ Tab으로 주요 요소 이동
→ 현재 focus 위치 확인
→ Enter / Space로 액션 실행
→ Form 입력 가능 여부 확인
→ Modal 열기 / 닫기 확인
→ Dropdown 조작 확인
→ Escape 닫기 확인
→ Shift+Tab 역방향 확인
```

실무 기준:

- Native `button`, `input`, `select` 우선 사용
- `div onClick`은 keyboard 조작 누락 위험
- Focus outline 제거 금지
- 시각적 순서와 DOM 순서 일치 권장
- disabled 요소는 focus 대상에서 제외
- hidden 요소에 focus가 가지 않게 처리
- Custom Component는 keyboard 동작 직접 구현 필요

---

### [FAQ]

Q. 마우스로 잘 되면 키보드도 되는 거 아니야?
A. 아니다. div onClick, custom dropdown, modal 등은 keyboard 조작이 누락될 수 있다.

Q. 키보드 접근성은 뭘 먼저 확인해?
A. Tab 이동, Enter / Space 실행, Escape 닫기, focus visible 여부부터 확인한다.

Q. Focus visible이 왜 중요해?
A. 키보드 사용자가 현재 위치를 알 수 있어야 UI를 사용할 수 있기 때문이다.

Q. Custom Dropdown은 왜 어렵지?
A. open 상태, focus 이동, Escape 닫기, Arrow Key 이동, aria-expanded 동기화를 직접 처리해야 하기 때문이다.

---

# 8. Accessible Name Foundation

## 8.1 Accessible Name

### [개념]

Accessible Name은 스크린 리더와 Testing Library가 button, link, input 같은 요소를 식별할 때 사용하는 이름이다.

Interactive Element는 목적을 이해할 수 있는 accessible name을 가져야 한다.

---

### [핵심]

Accessible Name 제공 방식:

- visible text
- `label`
- `aria-label`
- `aria-labelledby`
- `alt`
- `title` fallback

---

### [실무]

Button 예:

```jsx
<button type="button">저장</button>
```

Icon Button 예:

```jsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

Input 예:

```jsx
<label htmlFor="keyword">검색어</label>
<input id="keyword" name="keyword" />
```

Testing Library 예:

```tsx
screen.getByRole("button", { name: "저장" });
screen.getByLabelText("검색어");
```

주의:

- 아이콘만 있는 버튼은 accessible name이 없을 수 있음
- 같은 이름의 링크가 반복되면 목적지가 모호할 수 있음
- `aria-label`과 visible text가 충돌하지 않게 함
- `getByRole` 실패는 accessible name 문제일 수 있음

---

### [FAQ]

Q. Accessible Name이 뭐야?
A. 스크린 리더와 Testing Library가 요소의 이름으로 인식하는 텍스트다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼 목적을 알 수 없기 때문이다.

Q. getByRole에서 name이 안 잡히는 이유는?
A. 요소에 accessible name이 없거나 기대한 이름과 실제 이름이 다를 수 있다.

Q. visible text가 있으면 aria-label이 꼭 필요해?
A. 아니다. visible text가 명확하면 그것이 accessible name으로 사용될 수 있다.

---

# 9. Form Accessibility Foundation

## 9.1 Label and Error Foundation

### [개념]

Form Accessibility는 사용자가 입력 필드의 목적, 필수 여부, 오류 상태, 수정 방법을 명확히 이해할 수 있게 하는 기준이다.

모든 주요 Form Control은 label과 연결되어야 하며, 오류 메시지는 관련 input과 연결되어야 한다.

---

### [핵심]

Form 접근성 핵심:

- `label htmlFor`
- `input id`
- visible label
- `aria-label`
- `aria-labelledby`
- `aria-describedby`
- `aria-invalid`
- `required`
- field error
- global error
- role alert
- placeholder is not label

---

### [실무]

Label 예:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

Error Message 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  value={email}
  onChange={onChange}
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
/>
{error && (
  <p id="email-error" role="alert">
    이메일을 입력해 주세요.
  </p>
)}
```

실무 기준:

- `placeholder`는 label 대체 금지
- label과 input id 일치
- id 중복 금지
- checkbox / radio도 label 연결
- error message는 input 근처 표시
- error message와 input은 `aria-describedby`로 연결
- 오류 상태는 `aria-invalid`로 표현
- 색상만으로 오류 표시 금지

---

### [FAQ]

Q. placeholder가 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 label을 안정적으로 대체하지 못한다.

Q. 에러 메시지는 input과 꼭 연결해야 해?
A. 권장한다. 사용자가 어떤 입력값에 문제가 있는지 이해하기 쉽다.

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. getByLabelText가 실패하면?
A. input과 label이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

---

# 10. State Accessibility Foundation

## 10.1 Loading Error Empty State

### [개념]

State Accessibility는 Loading, Error, Empty State 같은 UI 상태 변화를 보조기술 사용자도 인식할 수 있게 하는 기준이다.

화면에 보이는 상태 메시지는 스크린 리더와 keyboard 사용자에게도 전달되어야 한다.

---

### [핵심]

상태별 기준:

- Loading: `role="status"`, `aria-live="polite"`, `aria-busy`
- Error: `role="alert"`, 명확한 오류 메시지, 재시도 버튼
- Empty: 빈 화면 방치 금지, 설명과 다음 행동 제공
- Success: 상태 문구 제공, 필요 시 live region
- Toast: 중요한 메시지는 보조기술 전달 고려

---

### [실무]

Loading 예:

```jsx
<section aria-busy={loading}>
  {loading && (
    <div role="status" aria-live="polite">
      데이터를 불러오는 중입니다.
    </div>
  )}
</section>
```

Error 예:

```jsx
<section role="alert">
  <h2>축제 정보를 불러오지 못했습니다.</h2>
  <p>잠시 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Empty State 예:

```jsx
<section>
  <h2>검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onReset}>
    필터 초기화
  </button>
</section>
```

실무 기준:

- spinner만 단독 제공하지 않음
- loading text 제공
- skeleton은 장식이면 `aria-hidden` 고려
- error는 stack trace 대신 사용자용 메시지 제공
- error에는 가능한 경우 retry action 제공
- empty state는 정상 상태와 오류 상태를 구분

---

### [FAQ]

Q. Spinner만 보이면 충분해?
A. 아니다. 스크린 리더 사용자를 위해 loading 상태를 설명하는 텍스트나 role status가 필요하다.

Q. Error Message에 role alert를 붙이면 돼?
A. 중요한 오류에는 도움이 되지만 alert 남발은 사용자를 방해할 수 있다.

Q. 데이터가 없으면 빈 배열만 렌더링하면 안 돼?
A. 권장하지 않는다. 사용자가 정상 상태인지 오류인지 알 수 있도록 Empty State를 제공해야 한다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

---

# 11. Component Accessibility Foundation

## 11.1 Interactive Component Baseline

### [개념]

Component Accessibility는 Button, Link, Modal, Dropdown, Tab 같은 Interactive Component가 keyboard와 스크린 리더에서 올바르게 동작하도록 만드는 기준이다.

React Custom Component는 Native Element의 접근성 동작을 잃지 않도록 설계해야 한다.

---

### [핵심]

Component별 핵심:

- Button: `button`, `type`, accessible name
- Link: 의미 있는 link text, `href` / `to`
- Modal: `role="dialog"`, `aria-modal`, focus 이동 / 복귀
- Dropdown: trigger `button`, `aria-expanded`, Escape 닫기
- Tab: `role="tablist"`, `role="tab"`, `aria-selected`
- Icon Button: `aria-label`
- Custom Component: role / keyboard / focus 직접 구현

---

### [실무]

Button 예:

```jsx
<button type="button" onClick={onSave}>
  저장
</button>
```

Link 예:

```jsx
<Link to="/festivals">축제 목록 보기</Link>
```

Modal 기본 구조:

```jsx
<section role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">리뷰 삭제</h2>
  <button type="button" onClick={onCancel}>
    취소
  </button>
  <button type="button" onClick={onConfirm}>
    삭제
  </button>
</section>
```

Dropdown trigger 예:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-haspopup="menu"
  onClick={toggleOpen}
>
  메뉴
</button>
```

실무 기준:

- 액션은 Button
- 이동은 Link
- Modal은 focus 관리 필요
- Dropdown은 open 상태와 `aria-expanded` 동기화
- Tab은 선택 상태와 `aria-selected` 동기화
- Icon Button은 visible text가 없으면 `aria-label` 필요
- 복잡한 Custom Component는 접근성 검증된 라이브러리 검토

---

### [FAQ]

Q. Button과 Link 차이는?
A. Button은 액션 실행이고 Link는 페이지나 위치 이동이다.

Q. 상세 페이지 이동 버튼은 button이야 Link야?
A. 단순 페이지 이동이라면 Link가 적합하다.

Q. Modal에 role dialog만 붙이면 접근성이 끝이야?
A. 아니다. focus 이동, focus trap, 닫기 버튼, aria-labelledby 같은 요소도 필요하다.

Q. Dropdown은 div로 만들어도 돼?
A. 시각적으로 가능하지만 keyboard, aria-expanded, focus 관리가 누락되기 쉽다.

---

# 12. Accessibility Testing Foundation

## 12.1 Test and Review Baseline

### [개념]

Accessibility Testing은 접근성 있는 UI 구조를 테스트와 리뷰로 검증하는 과정이다.

Testing Library의 `getByRole`, `getByLabelText`는 접근성 구조를 기반으로 요소를 찾기 때문에 접근성 좋은 UI는 테스트도 쉬워진다.

---

### [핵심]

우선 Query:

- `getByRole`
- `getByLabelText`
- `getByText`
- `getByAltText`
- `getByPlaceholderText`
- `getByTestId` last resort

수동 점검:

- keyboard only navigation
- focus visible
- tab order
- form label
- error message
- modal focus
- dropdown keyboard
- color only meaning
- image alt
- screen reader basics

자동화 점검:

- axe basics
- label 누락
- aria 속성 오류
- role 불일치
- color contrast 일부
- heading 구조 일부
- landmark 일부
- alt 누락

---

### [실무]

Testing Library 예:

```tsx
screen.getByRole("button", { name: "저장" });
screen.getByLabelText("이메일");
screen.getByRole("dialog", { name: "리뷰 삭제" });
screen.getByRole("alert");
```

Manual Check Flow:

```text
마우스 없이 Tab 이동
→ 주요 액션 실행
→ Form 입력 / 제출
→ 오류 확인
→ Modal 열고 닫기
→ Dropdown / Tab 조작
→ Focus 위치 확인
```

실무 기준:

- `getByRole` 우선 사용
- Form은 `getByLabelText`로 검증
- icon button은 name으로 찾을 수 있어야 함
- dialog는 accessible name 필요
- `getByTestId`는 최후 수단
- axe 통과만으로 접근성 완료 판단 금지
- keyboard 조작은 반드시 수동 확인 고려

---

### [FAQ]

Q. getByRole이 실패하면 접근성 문제야?
A. 가능성이 있다. semantic element, role, accessible name이 올바른지 확인해야 한다.

Q. getByLabelText가 실패하면?
A. input과 label이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

Q. testId로 찾으면 해결 아니야?
A. 테스트는 통과할 수 있지만 접근성 문제를 가릴 수 있다. 먼저 semantic 구조를 개선하는 것이 좋다.

Q. axe 테스트 통과하면 접근성 문제 없는 거야?
A. 아니다. keyboard, focus, 사용자 맥락 문제는 자동화 도구가 잡지 못할 수 있다.

---

# 13. Common Accessibility Mistakes

## 13.1 Foundation Mistakes

### [개념]

Common Accessibility Mistakes는 Frontend 개발에서 자주 발생하는 접근성 누락 패턴이다.

RAG 문서에는 Agent가 코드 리뷰 시 바로 탐지할 수 있도록 실수와 수정 기준을 명확히 포함해야 한다.

---

### [핵심]

자주 발생하는 실수:

- `div onClick`을 button처럼 사용
- Button과 Link 역할 혼동
- input label 누락
- placeholder를 label로 대체
- icon button `aria-label` 누락
- focus outline 제거
- keyboard 조작 불가
- positive tabindex 남용
- 색상만으로 상태 표시
- error message와 input 미연결
- `aria-invalid` 상태 불일치
- `aria-expanded` 상태 불일치
- Modal focus 관리 누락
- Modal 닫기 후 focus 복귀 누락
- Dropdown keyboard 조작 누락
- Tab `aria-selected` 누락
- 이미지 alt 누락 또는 과도한 alt
- 장식 이미지를 스크린 리더가 읽음
- role만 붙이고 keyboard 동작 미구현
- testId 중심 테스트로 접근성 문제를 숨김

---

### [실무]

Review Pattern:

```text
문제: getByRole("button") 실패
원인: div에 onClick 사용
해결: button 태그 사용 + accessible name 제공
```

```text
문제: getByLabelText("이메일") 실패
원인: label과 input 연결 누락
해결: label htmlFor와 input id 연결
```

```text
문제: Modal 닫은 뒤 focus 사라짐
원인: focus return 처리 누락
해결: Modal trigger로 focus 복귀
```

```text
문제: 오류가 빨간색으로만 표시됨
원인: color only meaning
해결: 오류 텍스트 + aria-invalid + aria-describedby 제공
```

---

### [FAQ]

Q. 접근성 초보가 가장 많이 하는 실수는?
A. div onClick 사용, label 누락, focus outline 제거, icon button 이름 누락, 색상만으로 상태 표시하는 실수가 많다.

Q. 접근성 문제는 어떻게 찾는 게 좋아?
A. 키보드만으로 조작해 보고 getByRole / getByLabelText 테스트를 사용하며 label과 focus 흐름을 확인한다.

Q. focus outline을 없애면 디자인이 깔끔해지는데 괜찮아?
A. 권장하지 않는다. 키보드 사용자가 현재 위치를 알 수 없게 된다.

Q. 빨간색이면 에러라는 걸 알 수 있지 않아?
A. 모든 사용자가 색상을 동일하게 인식하지 않는다. 텍스트나 아이콘을 함께 제공해야 한다.

---

# 14. Frontend Accessibility Review Flow

## 14.1 Agent Review Flow

### [개념]

Frontend Accessibility Review Flow는 Frontend Agent와 Review Agent가 접근성 기준으로 React UI를 검토하는 절차다.

이 Flow는 문서 검색, 코드 생성, 코드 리뷰, 테스트 실패 분석에 공통 적용된다.

---

### [핵심]

Review Flow:

```text
User Accessibility Request
→ Identify UI Element Role
→ Check Semantic HTML
→ Check Keyboard Flow
→ Check Accessible Name
→ Check Focus Management
→ Check ARIA State
→ Check Form / Error Connection
→ Check Image / Color Meaning
→ Verify with Testing Query
→ Frontend Accessibility Output
```

---

### [실무]

Agent 검토 순서:

1. UI 요소의 실제 역할 판단
2. Native HTML로 구현 가능한지 확인
3. Button / Link 역할 구분
4. Form label 연결 확인
5. Error Message 연결 확인
6. Keyboard 조작 가능 여부 확인
7. Focus visible 유지 여부 확인
8. Modal / Dropdown / Tab focus 관리 확인
9. ARIA 상태와 실제 상태 동기화 확인
10. Image alt 목적 적합성 확인
11. Color only meaning 여부 확인
12. Testing Library Query로 검증 가능 여부 확인
13. Common Mistakes 패턴 확인

---

### [FAQ]

Q. Review Agent는 접근성에서 무엇을 먼저 봐야 해?
A. Semantic HTML, keyboard 조작, label 연결, focus visible, error message 연결을 먼저 봐야 한다.

Q. Frontend Agent는 접근성을 언제 반영해야 해?
A. Component 설계와 구현 단계부터 반영해야 한다.

Q. Testing Agent는 접근성을 어떻게 확인해?
A. getByRole, getByLabelText, getByAltText 같은 접근성 query와 keyboard 수동 점검을 함께 고려한다.

Q. PM Agent는 접근성을 어떻게 요구사항으로 바꿔?
A. “키보드만으로 사용 가능”, “input label 연결”, “오류 메시지 전달”처럼 검증 가능한 조건으로 바꾼다.

---

# 15. Foundation Checklist

## 15.1 Accessibility Checklist

### [개념]

Frontend Accessibility Checklist는 접근성 문서와 React UI를 검수할 때 사용하는 기본 점검 목록이다.

Checklist는 누락 탐지와 Retrieval Query 매칭을 강화한다.

---

### [핵심]

Checklist:

```md
- [ ] Semantic HTML을 우선 사용했는가?
- [ ] 클릭 액션에 button을 사용했는가?
- [ ] 페이지 이동에 Link 또는 a를 사용했는가?
- [ ] input과 label이 연결되었는가?
- [ ] placeholder를 label 대체로 사용하지 않았는가?
- [ ] icon only button에 accessible name이 있는가?
- [ ] error message가 input과 연결되었는가?
- [ ] aria-invalid가 오류 상태와 일치하는가?
- [ ] keyboard만으로 주요 기능을 사용할 수 있는가?
- [ ] focus visible이 유지되는가?
- [ ] tab order가 자연스러운가?
- [ ] Modal focus 이동 / 복귀 기준이 있는가?
- [ ] Dropdown aria-expanded가 실제 상태와 일치하는가?
- [ ] Tab aria-selected가 실제 상태와 일치하는가?
- [ ] 이미지 alt가 목적에 맞는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] Loading 상태가 보조기술에 전달되는가?
- [ ] Error 상태가 명확히 전달되는가?
- [ ] Testing Library 접근성 query로 찾을 수 있는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Semantic HTML Check
→ Keyboard Check
→ Form Label Check
→ Error Message Check
→ Focus Check
→ ARIA State Check
→ Image / Color Check
→ Component Pattern Check
→ Testing Query Check
→ Final Review
```

실무 적용 대상:

- Login Form
- Signup Form
- Search Form
- Payment Form
- Modal
- Dropdown
- Tab
- Navigation
- Toast
- Loading State
- Error State
- Empty State
- Festival Card List
- Review Form
- Admin Table

---

### [FAQ]

Q. 접근성 체크리스트는 매번 다 봐야 해?
A. 핵심 Form, Modal, Navigation, 공통 UI Component에서는 꼼꼼히 확인하는 것이 좋다.

Q. 접근성 검수에서 가장 중요한 항목은?
A. Semantic HTML, keyboard 조작, label 연결, focus visible, error message 연결이다.

Q. 접근성 체크리스트는 RAG 문서에 왜 필요해?
A. Agent가 누락 항목을 검색하고 검토하기 쉽게 만들기 때문이다.

Q. 체크리스트는 코드 리뷰에도 사용할 수 있어?
A. 그렇다. Review Agent가 접근성 기준으로 코드 누락을 찾는 데 사용할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Accessibility 문서는 왜 필요해?
A. Frontend Agent가 키보드, 스크린 리더, 다양한 사용자 환경에서도 사용할 수 있는 UI를 만들고 검토해야 하기 때문이다.

Q. 접근성은 왜 중요해?
A. 사용자가 마우스, 키보드, 스크린 리더, 보조기술 등 다양한 방식으로 서비스를 사용할 수 있어야 하기 때문이다.

Q. 접근성은 별도 기능이야?
A. 아니다. HTML 구조, Component 설계, Form 처리, Error UX, Testing 전체에 포함되는 품질 기준이다.

Q. 접근성은 디자인 끝난 뒤에 추가하면 돼?
A. 권장하지 않는다. Semantic HTML, label, focus, keyboard 흐름은 Component 설계 단계부터 포함하는 것이 좋다.

Q. Frontend Accessibility 우선순위는?
A. Semantic HTML, Keyboard Accessibility, Focus Management, Accessible Name, Label, Error Message, ARIA 순서로 우선 검토한다.

Q. Semantic HTML이 뭐야?
A. HTML 요소를 의미에 맞게 사용하는 것이다. button, nav, main, label 같은 태그를 역할에 맞게 사용한다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

Q. div onClick을 써도 돼?
A. 가능은 하지만 keyboard 접근성과 의미가 부족하다. 클릭 액션은 button을 사용하는 것이 좋다.

Q. role="button"을 쓰면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다. 가능하면 button 태그를 사용한다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다.

Q. aria-expanded는 언제 써?
A. Dropdown, Accordion처럼 열림 / 닫힘 상태가 있는 trigger에서 실제 open 상태와 동기화해 사용한다.

Q. Keyboard Accessibility는 뭐야?
A. 마우스 없이 Tab, Shift+Tab, Enter, Space, Escape 등으로 UI를 사용할 수 있게 하는 기준이다.

Q. 마우스로 잘 되면 키보드도 되는 거 아니야?
A. 아니다. div onClick, custom dropdown, modal 등은 keyboard 조작이 누락될 수 있다.

Q. 키보드 접근성은 뭘 먼저 확인해?
A. Tab 이동, Enter / Space 실행, Escape 닫기, focus visible 여부부터 확인한다.

Q. focus visible이 왜 중요해?
A. 키보드 사용자가 현재 위치를 알 수 있어야 UI를 사용할 수 있기 때문이다.

Q. focus outline을 없애도 돼?
A. 권장하지 않는다. 키보드 사용자가 현재 위치를 알 수 없게 된다.

Q. Accessible Name이 뭐야?
A. 스크린 리더와 Testing Library가 요소의 이름으로 인식하는 텍스트다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. getByRole에서 name이 안 잡히는 이유는?
A. 요소에 accessible name이 없거나 기대한 이름과 실제 이름이 다를 수 있다.

Q. placeholder가 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 label을 안정적으로 대체하지 못한다.

Q. input과 label은 어떻게 연결해?
A. label의 htmlFor와 input의 id를 같은 값으로 연결한다.

Q. getByLabelText가 실패하는 이유는?
A. input과 label이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

Q. 에러 메시지는 input과 꼭 연결해야 해?
A. 권장한다. 사용자가 어떤 입력값에 문제가 있는지 이해하기 쉽다.

Q. error message는 input과 어떻게 연결해?
A. error id를 만들고 input의 aria-describedby에 연결하며 오류 상태는 aria-invalid로 표현한다.

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. Spinner만 보이면 충분해?
A. 아니다. 스크린 리더 사용자를 위해 loading 상태를 설명하는 텍스트나 role status가 필요하다.

Q. Loading 상태는 어떻게 전달해?
A. role="status", aria-live="polite", aria-busy, loading text를 사용할 수 있다.

Q. Error State는 어떻게 접근성 있게 만들까?
A. 명확한 오류 메시지, role alert, 재시도 버튼, focus 이동 여부를 고려한다.

Q. Empty State는 왜 필요해?
A. 데이터가 없는 상태를 사용자가 정상 상태인지 오류인지 이해할 수 있게 하기 위해 필요하다.

Q. Button과 Link 차이는?
A. Button은 액션 실행이고 Link는 페이지나 위치 이동이다.

Q. 상세 페이지 이동 버튼은 button이야 Link야?
A. 단순 페이지 이동이라면 Link가 적합하다.

Q. 삭제는 Link로 만들어도 돼?
A. 권장하지 않는다. 삭제는 현재 상태를 변경하는 액션이므로 button이 적합하다.

Q. Modal 접근성은 어떻게 처리해?
A. role dialog, aria-modal, aria-labelledby, focus 이동, focus 복귀, Escape 닫기, 닫기 버튼을 고려한다.

Q. Modal에 role dialog만 붙이면 접근성이 끝이야?
A. 아니다. focus 이동, focus trap, 닫기 버튼, aria-labelledby 같은 요소도 필요하다.

Q. Dropdown 접근성은 어떻게 처리해?
A. trigger는 button을 사용하고 aria-expanded를 실제 open 상태와 동기화하며 keyboard와 focus 흐름을 검토한다.

Q. Tab 접근성은 어떻게 처리해?
A. role tablist, role tab, role tabpanel, aria-selected, aria-controls 연결을 고려한다.

Q. 색상만으로 에러 표시해도 돼?
A. 권장하지 않는다. 텍스트나 아이콘, aria 속성을 함께 제공해야 한다.

Q. alt text는 어떻게 써?
A. 이미지의 목적에 따라 정보 이미지는 의미 있는 alt를 제공하고 장식 이미지는 alt=""를 사용한다.

Q. getByRole이 실패하면 접근성 문제야?
A. 가능성이 있다. semantic element, role, accessible name이 올바른지 확인해야 한다.

Q. testId로 찾으면 해결 아니야?
A. 테스트는 통과할 수 있지만 접근성 문제를 가릴 수 있다. 먼저 semantic 구조를 개선하는 것이 좋다.

Q. axe 테스트 통과하면 접근성 문제 없는 거야?
A. 아니다. keyboard, focus, 사용자 맥락 문제는 자동화 도구가 잡지 못할 수 있다.

Q. 접근성 초보가 가장 많이 하는 실수는?
A. div onClick 사용, label 누락, focus outline 제거, icon button 이름 누락, 색상만으로 상태 표시하는 실수가 많다.

Q. 접근성 문제는 어떻게 찾는 게 좋아?
A. 키보드만으로 조작해 보고 getByRole / getByLabelText 테스트를 사용하며 label과 focus 흐름을 확인한다.

Q. Frontend Accessibility Review Flow는?
A. UI 역할 확인, Semantic HTML 확인, keyboard 확인, accessible name 확인, focus 확인, ARIA 상태 확인, Testing Query 검증 순서다.

Q. Review Agent는 접근성에서 무엇을 먼저 봐야 해?
A. Semantic HTML, keyboard 조작, label 연결, focus visible, error message 연결을 먼저 봐야 한다.

Q. Frontend Agent는 접근성을 언제 반영해야 해?
A. Component 설계와 구현 단계부터 반영해야 한다.

Q. Accessibility Checklist 핵심은?
A. Semantic HTML, button/link 구분, label 연결, error 연결, keyboard 조작, focus visible, ARIA 상태 동기화, Testing Query 검증이다.
