# Design System Foundation Part07 - Accessibility Documentation Review Rules

---

# 1. Accessibility System Core

## 1.1 Accessibility System Definition

### [개념]

Accessibility System은 Design System의 모든 컴포넌트와 화면이 키보드 사용자, 스크린 리더 사용자, 저시력 사용자, 색각 다양성 사용자, 터치 사용자에게 사용 가능하도록 만드는 공통 기준이다.

Accessibility System은 별도 선택 기능이 아니라 Core Component, Layout, Feedback State, Theme, Documentation, Review 단계에 모두 포함되어야 하는 품질 기준이다.

이 문서는 Frontend Agent가 접근성 기준을 반영해 UI를 생성하고, Review Agent가 접근성 누락을 검토하고, PM Agent가 출시 차단 이슈를 판단하기 위한 RAG Retrieval 최적화 문서다.

---

### [핵심]

Accessibility System 대상:

- Semantic HTML
- Landmark
- Heading Structure
- Button Accessibility
- Link Accessibility
- Form Accessibility
- Input Label Association
- Error Message Association
- Keyboard Navigation
- Focus Visible
- Focus Management
- ARIA Usage
- Accessible Name
- Color Contrast
- Motion Reduction
- Touch Target
- Modal Accessibility
- Table Accessibility
- Feedback Accessibility
- Theme Accessibility
- Documentation Accessibility
- Review Checklist

Accessibility System 목적:

- 키보드 조작 가능성 보장
- 스크린 리더 정보 전달
- 색상만으로 상태 전달 방지
- focus 위치 명확화
- form error 접근성 확보
- modal focus 관리
- table 구조 정보 제공
- dark mode contrast 유지
- Frontend Agent 생성 기준 제공
- Review Agent 반려 기준 제공
- PM Agent 완료 판단 기준 제공

---

### [실무]

Accessibility 적용 Flow:

```text
Requirement
→ Semantic Element 선택
→ Accessible Name 확인
→ Keyboard Interaction 확인
→ Focus Visible 적용
→ Label / Error 연결
→ Color Contrast 확인
→ Responsive / Touch Target 확인
→ Review Checklist 검토
```

Frontend Agent는 UI를 생성할 때 div와 span으로 모든 것을 만들지 않는다.

Review Agent는 기능이 동작하더라도 keyboard, label, focus, aria, contrast 문제가 있으면 Needs Fix 또는 Blocked로 판단할 수 있다.

PM Agent는 사용자가 기능을 실제로 사용할 수 없거나 주요 흐름이 막히면 UI Complete로 판단하지 않는다.

---

### [FAQ]

Q. Accessibility System이 뭐야?
A. 키보드, 스크린 리더, 저시력, 색각 다양성, 터치 사용자가 UI를 사용할 수 있도록 만드는 공통 기준이다.

Q. Design System에 Accessibility가 왜 필요해?
A. 공통 컴포넌트가 접근성을 만족하면 전체 화면의 사용성과 품질이 안정되기 때문이다.

Q. 접근성은 나중에 추가해도 돼?
A. 권장하지 않는다. 컴포넌트와 레이아웃 설계 단계부터 반영해야 수정 비용이 줄어든다.

Q. Review Agent는 Accessibility에서 뭘 봐야 해?
A. Semantic HTML, label 연결, focus-visible, keyboard 조작, accessible name, contrast, modal focus를 확인해야 한다.

---

## 1.2 Accessibility Scope

### [개념]

Accessibility Scope는 Design System Foundation 단계에서 반드시 검토해야 하는 접근성 기준의 범위다.

이 문서는 고급 접근성 감사 전체를 다루기보다 Frontend Foundation 단계에서 Agent가 반복적으로 생성하고 검토해야 하는 실무 기준을 다룬다.

---

### [핵심]

포함 범위:

- Semantic HTML
- Landmark
- Heading
- Button / Link 구분
- Form Label
- Helper Text
- Error Message
- aria-invalid
- aria-describedby
- Icon Button Accessible Name
- Keyboard Navigation
- Focus Visible
- Modal Focus Trap
- Focus Restore
- ARIA 기본 원칙
- Color Contrast 기본 기준
- Dark Mode Contrast
- Reduced Motion
- Touch Target
- Table Header
- Toast / Alert 접근성
- Documentation Checklist
- Review Decision

제외 범위:

- 전문 WCAG 감사 전체
- Screen Reader별 고급 차이 분석
- Enterprise Accessibility Governance
- 법률 준수 문서 심화
- 고급 자동화 접근성 테스트 전략
- 고급 ARIA Widget 직접 구현
- Native App Accessibility
- Accessibility Statement 작성 심화

---

### [실무]

접근성 기준은 다음 Part들과 연결된다.

```text
Part02 Design Token Rules
→ Color Contrast / Focus Ring / Theme Token

Part03 Component Specification Rules
→ Props / State / Accessibility Spec

Part04 Core Component Rules
→ Button / Input / Modal / Table 접근성

Part05 Feedback State Pattern Rules
→ Error / Loading / Toast / Alert 접근성

Part06 Layout Responsive Theme Rules
→ Landmark / Navigation / Responsive / Dark Mode 접근성

Part07 Accessibility Documentation Review Rules
→ 최종 검토 / 문서화 / Agent 판단 기준
```

위임 기준:

```text
컴포넌트 코드 상세 구현
→ React Component Design

form 상태 관리
→ Form Handling & Validation

error / loading UX 흐름
→ Error Handling Loading UX

테스트 자동화
→ Frontend Testing

색상 / token 기준
→ Design Token Rules
```

---

### [FAQ]

Q. Accessibility Scope는 어디까지야?
A. Semantic HTML, keyboard, focus, form label, error 연결, aria, contrast, modal, table, feedback 접근성까지다.

Q. WCAG 전체를 다뤄야 해?
A. 아니다. Foundation 단계에서는 공통 UI 생성과 검토에 필요한 실무 기준을 우선 다룬다.

Q. Accessibility와 Frontend Accessibility 문서는 겹치지 않아?
A. Frontend Accessibility는 접근성 전반이고, 이 문서는 Design System 컴포넌트와 Review 기준 중심이다.

Q. 접근성 자동 테스트까지 포함해?
A. 기본 검토 기준은 포함하지만 고급 자동화 테스트 전략은 Frontend Testing 또는 Expert 단계에서 다룬다.

---

# 2. Semantic HTML and Landmark Rules

## 2.1 Semantic HTML Rules

### [개념]

Semantic HTML은 div와 span만 사용하는 대신 HTML 요소의 의미를 올바르게 사용하는 기준이다.

Semantic HTML은 스크린 리더, 브라우저 기본 동작, keyboard 접근성, SEO, 유지보수성에 영향을 준다.

---

### [핵심]

권장 요소:

```text
button
→ 사용자 action 실행

a / Link
→ 페이지 이동 또는 외부 링크

input
→ 사용자 입력

label
→ 입력 항목 이름

form
→ 입력 제출 영역

main
→ 페이지 주요 콘텐츠

nav
→ navigation

header
→ 페이지 또는 영역 머리말

footer
→ 페이지 또는 영역 하단

section
→ 관련 콘텐츠 묶음

article
→ 독립적인 콘텐츠

table
→ 행 / 열 구조 데이터
```

비권장:

```text
div onClick
span button
table layout
button navigation link
a submit action
placeholder label 대체
```

---

### [실무]

나쁜 예:

```jsx
<div onClick={handleSave}>저장</div>
<span onClick={goToPage}>목록으로 이동</span>
```

좋은 예:

```jsx
<button type="button" onClick={handleSave}>
  저장
</button>

<Link to="/list">
  목록으로 이동
</Link>
```

Review 기준:

```md
- [ ] action에는 button을 사용하는가?
- [ ] navigation에는 Link 또는 a를 사용하는가?
- [ ] form input에 label이 있는가?
- [ ] 표 데이터에는 table을 사용하는가?
- [ ] layout 용도로 table을 사용하지 않는가?
```

---

### [FAQ]

Q. Semantic HTML이 뭐야?
A. HTML 요소를 시각적 모양이 아니라 의미에 맞게 사용하는 것이다.

Q. div에 onClick을 넣어 button처럼 써도 돼?
A. 권장하지 않는다. 기본 keyboard 동작과 접근성이 부족하므로 button을 사용한다.

Q. 페이지 이동에 button을 써도 돼?
A. 권장하지 않는다. 페이지 이동은 Link 또는 a를 사용한다.

Q. table은 언제 써?
A. 행과 열 구조의 표 데이터를 표현할 때 사용한다.

---

## 2.2 Landmark Rules

### [개념]

Landmark는 페이지의 주요 영역을 스크린 리더와 보조기기가 빠르게 탐색할 수 있게 하는 구조다.

Landmark는 main, nav, header, footer, aside 같은 semantic 영역으로 구성된다.

---

### [핵심]

주요 Landmark:

```text
main
→ 페이지 주요 콘텐츠

nav
→ 주요 메뉴 / 보조 메뉴

header
→ 페이지 또는 영역 상단

footer
→ 페이지 또는 영역 하단

aside
→ 보조 콘텐츠 / 사이드바

form
→ 입력 제출 영역

search
→ 검색 영역
```

Landmark 기준:

- 페이지당 main은 일반적으로 하나
- navigation은 nav 사용
- nav가 여러 개면 aria-label로 구분
- sidebar는 aside 고려
- header / footer는 문맥에 맞게 사용
- landmark 과도한 중첩 금지

---

### [실무]

App Layout 예:

```jsx
<header>
  <Logo />
  <nav aria-label="주요 메뉴">
    <NavLink to="/dashboard">대시보드</NavLink>
    <NavLink to="/lots">LOT 관리</NavLink>
  </nav>
</header>

<main>
  <Outlet />
</main>
```

여러 nav 구분 예:

```jsx
<nav aria-label="주요 메뉴">...</nav>
<nav aria-label="페이지 내 메뉴">...</nav>
```

Review 기준:

```md
- [ ] main landmark가 있는가?
- [ ] nav 영역이 semantic하게 구성되는가?
- [ ] 여러 nav가 aria-label로 구분되는가?
- [ ] sidebar가 aside 또는 명확한 영역으로 구분되는가?
```

---

### [FAQ]

Q. Landmark가 뭐야?
A. main, nav, header, footer, aside처럼 페이지 주요 영역을 의미적으로 구분하는 구조다.

Q. main은 꼭 필요해?
A. 권장된다. 페이지의 주요 콘텐츠 영역을 보조기기가 빠르게 찾을 수 있다.

Q. nav가 여러 개면 어떻게 해?
A. `aria-label`로 주요 메뉴, 보조 메뉴처럼 구분한다.

Q. sidebar는 어떤 요소가 좋아?
A. 보조 콘텐츠나 보조 navigation이면 aside 또는 nav를 고려한다.

---

## 2.3 Heading Structure Rules

### [개념]

Heading Structure는 h1부터 h6까지의 제목 계층을 의미 구조에 맞게 사용하는 기준이다.

Heading은 시각적 크기가 아니라 문서 구조와 콘텐츠 계층을 표현한다.

---

### [핵심]

Heading 기준:

- 페이지 주요 제목은 h1
- section 제목은 h2 또는 적절한 heading level
- heading level을 시각 스타일 용도로 건너뛰지 않음
- h1을 여러 개 사용할 경우 문맥 명확화
- heading 없는 section 남발 금지
- Card title은 문맥에 맞게 h2 / h3 / p 선택
- 시각 크기는 typography token으로 조정

좋은 구조:

```text
h1 LOT 관리
→ h2 생산 지시 목록
→ h2 설비 상태
→ h3 EQ1 상태
```

나쁜 구조:

```text
h4 LOT 관리
→ h2 생산 지시 목록
→ h6 설비 상태
```

---

### [실무]

좋은 예:

```jsx
<main>
  <h1>LOT 관리</h1>

  <section>
    <h2>생산 지시 목록</h2>
    <LotTable />
  </section>

  <section>
    <h2>설비 상태</h2>
    <EquipmentGrid />
  </section>
</main>
```

시각 스타일 분리:

```css
.pageTitle {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
}
```

Review 기준:

```md
- [ ] 페이지 h1이 있는가?
- [ ] heading level이 자연스러운가?
- [ ] 시각 크기 때문에 heading level을 건너뛰지 않는가?
- [ ] section 제목이 필요한 곳에 있는가?
```

---

### [FAQ]

Q. Heading Structure는 왜 중요해?
A. 사용자와 보조기기가 페이지 구조를 이해하고 빠르게 탐색할 수 있기 때문이다.

Q. h1은 꼭 하나만 써야 해?
A. 일반적으로 페이지 주요 제목 하나를 권장한다. 여러 h1을 쓸 경우 문맥이 명확해야 한다.

Q. 글자를 작게 보이게 하려고 h4를 써도 돼?
A. 안 된다. heading level은 의미 구조이고, 크기는 CSS와 typography token으로 조정한다.

Q. Card title도 heading이어야 해?
A. Card가 독립 콘텐츠이면 heading을 고려하고, 단순 라벨이면 p나 span이 적절할 수 있다.

---

# 3. Keyboard Focus Rules

## 3.1 Keyboard Navigation Rules

### [개념]

Keyboard Navigation은 사용자가 마우스 없이 keyboard만으로 interactive element를 탐색하고 조작할 수 있게 하는 기준이다.

Keyboard 접근성은 Button, Link, Form, Modal, Tabs, Dropdown, Table Action에 반드시 필요하다.

---

### [핵심]

Keyboard 기준:

- interactive element는 Tab으로 접근 가능
- button은 Enter / Space로 실행
- link는 Enter로 이동
- form control은 keyboard 조작 가능
- disabled element는 불필요한 focus 방지
- focus 순서는 시각 순서와 일치
- custom control은 keyboard 동작 직접 구현 필요
- modal open 중 focus trap 고려
- ESC 닫기 정책 명확화
- skip link 고려 가능

---

### [실무]

좋은 예:

```jsx
<button type="button" onClick={handleSave}>
  저장
</button>

<Link to="/members">
  사용자 목록
</Link>
```

나쁜 예:

```jsx
<div onClick={handleSave}>저장</div>
```

custom control이 필요한 경우:

```text
role
tabIndex
keyboard event
focus style
aria state
```

위 항목을 직접 구현해야 하므로 가능한 native element를 우선 사용한다.

Review 기준:

```md
- [ ] keyboard만으로 주요 기능을 사용할 수 있는가?
- [ ] focus 순서가 자연스러운가?
- [ ] custom interactive element가 native 동작을 대체하지 않는가?
- [ ] disabled 상태가 focus 흐름을 방해하지 않는가?
```

---

### [FAQ]

Q. Keyboard Navigation이 뭐야?
A. 마우스 없이 keyboard만으로 화면을 탐색하고 조작할 수 있게 하는 기준이다.

Q. 모든 클릭 요소가 Tab으로 접근 가능해야 해?
A. 사용자가 조작하는 interactive element는 keyboard 접근이 가능해야 한다.

Q. div onClick을 keyboard로 쓰게 만들면 괜찮아?
A. 가능은 하지만 role, tabIndex, keyboard event를 직접 구현해야 하므로 native button이 우선이다.

Q. focus 순서는 왜 중요해?
A. keyboard 사용자가 화면 흐름을 예측하며 이동할 수 있어야 하기 때문이다.

---

## 3.2 Focus Visible Rules

### [개념]

Focus Visible은 keyboard 사용자가 현재 focus 위치를 볼 수 있게 하는 시각적 표시다.

Focus outline을 제거하면 keyboard 사용자는 현재 위치를 알 수 없어 UI 사용이 어려워진다.

---

### [핵심]

Focus Visible 기준:

- focus indicator 제공
- outline 제거만 금지
- focus color는 token 사용
- dark mode에서도 보여야 함
- button, link, input, select, checkbox, radio, tab, modal close에 적용
- focus indicator가 요소와 충분히 구분되어야 함
- focus-visible 사용 권장

권장 token:

```text
--color-focus-ring
--focus-ring-width
--focus-ring-offset
```

---

### [실무]

Focus style 예:

```css
:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

Component Focus 예:

```css
.button:focus-visible,
.link:focus-visible,
.input:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

나쁜 예:

```css
*:focus {
  outline: none;
}
```

Review 기준:

```md
- [ ] focus-visible이 제공되는가?
- [ ] outline 제거만 하지 않는가?
- [ ] dark mode에서 focus ring이 보이는가?
- [ ] 모든 interactive element가 focus 표시를 갖는가?
```

---

### [FAQ]

Q. Focus Visible이 뭐야?
A. keyboard 사용자가 현재 선택된 요소를 볼 수 있게 하는 focus 표시다.

Q. outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible style을 제공해야 한다.

Q. focus ring 색상도 token으로 관리해야 해?
A. 권장된다. theme와 dark mode 대응을 위해 `--color-focus-ring`을 사용한다.

Q. focus-visible은 모든 요소에 필요해?
A. 사용자가 조작하는 interactive element에는 필요하다.

---

## 3.3 Focus Management Rules

### [개념]

Focus Management는 Modal, Drawer, Error State, Route Change 같은 상황에서 focus 위치를 적절히 이동하거나 복원하는 기준이다.

Focus Management는 화면 상태가 바뀌었을 때 keyboard 사용자가 길을 잃지 않게 만든다.

---

### [핵심]

Focus Management 대상:

- Modal open / close
- Drawer open / close
- Form validation error
- Page-level error
- Route change
- Toast는 일반적으로 focus 이동 불필요
- Skip link 사용 가능
- Dynamic content update

기준:

```text
Modal Open
→ modal 내부 첫 focusable element 또는 title로 focus 이동

Modal Close
→ trigger element로 focus 복원

Form Error
→ 첫 번째 오류 field 또는 error summary로 focus 이동 고려

Page Error
→ error heading으로 focus 이동 고려

Route Change
→ page title 또는 main으로 focus 이동 고려
```

---

### [실무]

Modal Focus Flow:

```text
Open Button Focus
→ Modal Open
→ Close Button 또는 Modal Title Focus
→ Tab inside Modal
→ Modal Close
→ Open Button Focus Restore
```

Form Error Flow:

```text
Submit
→ Validation Failed
→ Error Summary 표시
→ First Invalid Field Focus
```

Error Summary 예:

```jsx
<div role="alert" tabIndex={-1} ref={errorSummaryRef}>
  입력 내용을 확인해 주세요.
</div>
```

Review 기준:

```md
- [ ] modal open 시 focus 이동이 있는가?
- [ ] modal close 후 focus 복원이 있는가?
- [ ] form error 위치를 keyboard 사용자가 찾을 수 있는가?
- [ ] route change 후 focus 흐름이 자연스러운가?
```

---

### [FAQ]

Q. Focus Management가 뭐야?
A. 화면 상태가 바뀔 때 focus 위치를 적절히 이동하거나 복원하는 기준이다.

Q. Modal을 열면 focus는 어디로 가야 해?
A. Modal 내부의 닫기 버튼, 첫 입력 요소, 또는 title 영역으로 이동하는 것이 좋다.

Q. Modal이 닫히면 focus는 어디로 가야 해?
A. Modal을 열었던 trigger element로 돌아가는 것이 좋다.

Q. Form 오류가 나면 focus를 이동해야 해?
A. 제출 실패 시 첫 번째 오류 field나 error summary로 이동을 고려한다.

---

## 3.4 Keyboard Focus Mistakes

### [개념]

Keyboard Focus Mistakes는 keyboard 사용자가 화면을 탐색하거나 조작할 수 없게 만드는 실수다.

이 실수는 주요 기능 사용 불가로 이어질 수 있으므로 Review Agent가 강하게 검토해야 한다.

---

### [핵심]

자주 발생하는 실수:

- focus outline 제거
- div onClick으로 button 대체
- keyboard event 누락
- modal focus trap 없음
- modal close 후 focus 복원 없음
- Tab 순서가 시각 순서와 다름
- disabled 요소가 불필요하게 focus됨
- icon button focus 표시 없음
- dropdown ESC 닫기 없음
- form error 후 focus 위치 안내 없음
- skip 없이 반복 navigation이 너무 김

---

### [실무]

Troubleshooting:

```text
keyboard로 버튼을 누를 수 없음
→ button element 사용 확인

현재 focus 위치를 알 수 없음
→ focus-visible 추가

Modal 밖으로 focus가 나감
→ focus trap 적용

Modal 닫은 후 focus가 사라짐
→ trigger focus restore 적용

Form 오류 위치를 찾기 어려움
→ error summary 또는 first invalid field focus
```

Review Checklist:

```md
- [ ] keyboard만으로 주요 흐름을 완료할 수 있는가?
- [ ] focus-visible이 있는가?
- [ ] custom control이 keyboard 조작을 지원하는가?
- [ ] modal focus가 관리되는가?
- [ ] focus 순서가 자연스러운가?
```

---

### [FAQ]

Q. Keyboard Focus에서 가장 흔한 실수는?
A. focus outline을 제거하거나 div onClick으로 button을 대체하는 것이다.

Q. keyboard로 저장 버튼을 못 누르면 Blocked야?
A. 주요 기능이라면 Blocked가 될 수 있다.

Q. Modal 밖으로 Tab이 나가면 문제야?
A. 문제가 될 수 있다. Modal이 열린 동안 focus trap을 고려해야 한다.

Q. focus 표시가 디자인과 안 맞으면 제거해도 돼?
A. 제거하면 안 된다. 디자인에 맞는 대체 focus style을 제공해야 한다.

---

# 4. Form Accessibility Rules

## 4.1 Label Association Rules

### [개념]

Label Association은 label과 input, select, textarea 같은 form control을 명확히 연결하는 기준이다.

Label은 사용자가 입력해야 하는 값의 이름이며, placeholder는 label을 대체할 수 없다.

---

### [핵심]

Label 기준:

- 모든 form control은 label 필요
- label과 input은 htmlFor / id로 연결
- 또는 label 내부에 input 포함
- placeholder를 label 대체로 사용 금지
- hidden label이 필요한 경우 sr-only 사용 가능
- required 여부 명확화
- label 문구는 짧고 명확하게 작성

좋은 예:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

비권장 예:

```jsx
<input placeholder="이메일" />
```

---

### [실무]

명시적 연결:

```jsx
<label htmlFor="memberName">사용자 이름</label>
<input id="memberName" name="memberName" type="text" />
```

암시적 연결:

```jsx
<label>
  사용자 이름
  <input name="memberName" type="text" />
</label>
```

시각적으로 숨긴 label:

```jsx
<label htmlFor="searchKeyword" className="srOnly">
  검색어
</label>
<input id="searchKeyword" name="searchKeyword" type="search" placeholder="검색어 입력" />
```

Review 기준:

```md
- [ ] 모든 input에 label이 있는가?
- [ ] label과 input이 연결되는가?
- [ ] placeholder를 label 대체로 사용하지 않는가?
- [ ] required 정보가 명확한가?
```

---

### [FAQ]

Q. Label Association이 뭐야?
A. label과 input을 연결해 사용자가 어떤 값을 입력해야 하는지 알 수 있게 하는 기준이다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 안 된다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. 검색 input에도 label이 필요해?
A. 필요하다. 시각적으로 숨긴 label을 사용할 수 있다.

Q. label을 input 안에 넣어도 돼?
A. 가능하다. label 내부에 input을 넣으면 암시적으로 연결된다.

---

## 4.2 Error Message Association Rules

### [개념]

Error Message Association은 form control의 오류 메시지를 해당 input과 연결하는 기준이다.

오류 메시지는 시각적으로 보이는 것뿐 아니라 스크린 리더 사용자에게도 전달되어야 한다.

---

### [핵심]

Error 연결 기준:

- 오류 시 aria-invalid 사용
- error message id 생성
- aria-describedby로 input과 error 연결
- 동적 error는 role alert 고려
- helper text와 error message 구분
- error는 input 가까이에 표시
- 색상만으로 error 표시 금지

기본 구조:

```text
Label
→ Input aria-invalid aria-describedby
→ Helper Text or Error Message
```

---

### [실무]

좋은 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid={Boolean(emailError)}
  aria-describedby={emailError ? "email-error" : "email-help"}
/>
<p id="email-help">로그인에 사용할 이메일을 입력해 주세요.</p>
{emailError && (
  <p id="email-error" role="alert">
    올바른 이메일 형식이 아닙니다.
  </p>
)}
```

나쁜 예:

```jsx
<input style={{ borderColor: "red" }} />
<p>이메일 오류</p>
```

Review 기준:

```md
- [ ] error message가 input 가까이에 있는가?
- [ ] aria-invalid가 적용되는가?
- [ ] aria-describedby가 error message와 연결되는가?
- [ ] error를 색상만으로 표시하지 않는가?
```

---

### [FAQ]

Q. Error Message Association이 뭐야?
A. 오류 메시지를 해당 input과 연결해 보조기기도 오류를 인식할 수 있게 하는 기준이다.

Q. aria-invalid는 언제 써?
A. 입력값이 오류 상태일 때 `aria-invalid="true"`를 사용한다.

Q. aria-describedby는 왜 필요해?
A. helper text나 error message를 input과 연결해 스크린 리더가 읽을 수 있게 한다.

Q. error border만 있으면 충분해?
A. 아니다. error message와 접근성 속성이 함께 필요하다.

---

## 4.3 Required Disabled Readonly Rules

### [개념]

Required, Disabled, Readonly Rules는 form control의 필수 입력, 비활성, 읽기 전용 상태를 명확히 표현하는 기준이다.

이 세 상태는 의미와 동작이 다르므로 혼동하면 안 된다.

---

### [핵심]

상태 구분:

```text
required
→ 반드시 입력해야 하는 값

disabled
→ 조작 불가, form 제출에서 제외

readonly
→ 수정 불가, 값은 읽을 수 있고 제출 가능
```

기준:

- required 표시 명확화
- required만 표시하고 설명 누락 금지
- disabled 이유가 필요한 경우 안내
- disabled와 readonly 구분
- disabled text contrast 고려
- readonly는 읽을 수 있어야 함
- disabled 상태에서 action 실행 금지

---

### [실무]

Required 예:

```jsx
<label htmlFor="lotNo">
  LOT 번호 <span aria-hidden="true">*</span>
</label>
<input id="lotNo" name="lotNo" required />
```

Disabled 예:

```jsx
<input id="role" name="role" value="ADMIN" disabled />
```

Readonly 예:

```jsx
<input id="createdAt" name="createdAt" value={createdAt} readOnly />
```

Review 기준:

```md
- [ ] required 상태가 명확한가?
- [ ] disabled와 readonly를 혼동하지 않는가?
- [ ] disabled 상태가 실제 조작을 막는가?
- [ ] readonly 값이 읽을 수 있는가?
```

---

### [FAQ]

Q. required는 어떻게 표시해?
A. 필수 입력임을 label 근처에 표시하고 필요한 경우 안내 문구를 제공한다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있고 제출 가능하다.

Q. disabled 이유를 설명해야 해?
A. 사용자가 이유를 알기 어려운 경우 helper text나 tooltip으로 안내하는 것이 좋다.

Q. readonly를 disabled처럼 흐리게 보여도 돼?
A. 권장하지 않는다. readonly 값은 사용자가 읽을 수 있어야 한다.

---

## 4.4 Form Accessibility Mistakes

### [개념]

Form Accessibility Mistakes는 입력 폼에서 label, error, required, disabled, keyboard 기준을 누락하는 실수다.

Form 접근성 실수는 사용자 입력 실패와 Review Agent 반려의 주요 원인이다.

---

### [핵심]

자주 발생하는 실수:

- placeholder를 label로 사용
- label과 input id 불일치
- error message 연결 없음
- aria-invalid 누락
- helper text와 error message 혼동
- required 표시 없음
- required를 색상만으로 표시
- disabled와 readonly 혼동
- disabled 이유 설명 없음
- error를 상단 Alert로만 표시
- form submit 실패 후 focus 안내 없음
- autocomplete 누락

---

### [실무]

Troubleshooting:

```text
스크린 리더가 input 이름을 읽지 못함
→ label htmlFor / input id 확인

입력 오류를 찾기 어려움
→ aria-describedby + field error 확인

필수 입력인지 모름
→ required 표시와 안내 추가

읽기 전용 값이 너무 흐림
→ readonly style 조정

submit 후 오류 위치 모름
→ first invalid field focus 고려
```

Review Checklist:

```md
- [ ] label 연결이 올바른가?
- [ ] error message가 input과 연결되는가?
- [ ] required / disabled / readonly 의미가 구분되는가?
- [ ] keyboard로 form을 제출하고 수정할 수 있는가?
- [ ] autocomplete가 필요한 field에 적용되는가?
```

---

### [FAQ]

Q. Form Accessibility에서 가장 흔한 실수는?
A. placeholder를 label처럼 사용하고 error message를 input과 연결하지 않는 것이다.

Q. error를 상단 Alert에만 보여줘도 돼?
A. 전체 오류 안내에는 가능하지만 field 오류는 해당 입력 필드 가까이에 표시해야 한다.

Q. required 표시를 빨간색만으로 해도 돼?
A. 권장하지 않는다. 텍스트나 기호를 함께 사용해야 한다.

Q. autocomplete는 접근성과 관련 있어?
A. 그렇다. 로그인, 이메일, 비밀번호, 주소 같은 입력에서 사용자 편의와 접근성에 도움이 된다.

---

# 5. ARIA and Accessible Name Rules

## 5.1 ARIA Usage Rules

### [개념]

ARIA는 HTML의 의미를 보완하기 위한 접근성 속성이다.

ARIA는 Semantic HTML을 대체하는 도구가 아니다. native element로 해결할 수 있으면 native element를 우선 사용해야 한다.

---

### [핵심]

ARIA 원칙:

- Semantic HTML 우선
- 필요할 때만 ARIA 사용
- 잘못된 ARIA는 없는 것보다 나쁠 수 있음
- role과 keyboard 동작이 일치해야 함
- aria-label은 보이는 label 대체가 아님
- aria-hidden은 신중히 사용
- aria-live는 동적 메시지에 사용 가능
- aria-expanded, aria-selected, aria-current는 상태 표현에 사용

자주 쓰는 ARIA:

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
aria-modal
```

---

### [실무]

좋은 예:

```jsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

좋은 예:

```jsx
<button type="button" aria-expanded={isOpen} aria-controls="filter-panel">
  필터
</button>
```

나쁜 예:

```jsx
<div role="button" onClick={handleClick}>
  저장
</div>
```

위 경우는 가능하면 native button을 사용하는 것이 좋다.

Review 기준:

```md
- [ ] native element로 해결 가능한데 ARIA를 남용하지 않는가?
- [ ] role과 keyboard 동작이 일치하는가?
- [ ] aria 상태가 실제 UI 상태와 일치하는가?
- [ ] aria-hidden으로 중요한 정보를 숨기지 않는가?
```

---

### [FAQ]

Q. ARIA는 언제 써?
A. Semantic HTML만으로 의미를 전달하기 어려울 때 보완용으로 사용한다.

Q. ARIA를 많이 쓰면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다.

Q. role button을 div에 넣으면 button이 돼?
A. 의미 일부만 추가된다. keyboard 동작과 focus 처리를 직접 구현해야 하므로 native button이 우선이다.

Q. aria-hidden은 언제 써?
A. 장식 아이콘처럼 스크린 리더가 읽지 않아도 되는 요소에 사용한다.

---

## 5.2 Accessible Name Rules

### [개념]

Accessible Name은 스크린 리더가 interactive element의 이름으로 읽는 값이다.

Button, Link, Input, Icon Button, Form Control은 사용자가 목적을 알 수 있는 accessible name이 필요하다.

---

### [핵심]

Accessible Name 제공 방식:

```text
Visible Text
→ 가장 권장

label
→ form control 이름

aria-label
→ 보이는 텍스트가 없을 때

aria-labelledby
→ 다른 요소의 텍스트를 이름으로 사용

title
→ 주요 accessible name 수단으로 비권장
```

필수 대상:

- Icon Button
- Search Input
- Close Button
- Menu Button
- Form Input
- Navigation Link
- Pagination Button
- Table Action Button

---

### [실무]

좋은 예:

```jsx
<button type="button">저장</button>
```

Icon Button 예:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

Pagination 예:

```jsx
<button type="button" aria-label="다음 페이지">
  다음
</button>
```

나쁜 예:

```jsx
<button type="button">
  <CloseIcon />
</button>
```

Review 기준:

```md
- [ ] icon button에 accessible name이 있는가?
- [ ] input에 label이 있는가?
- [ ] link 텍스트가 목적을 설명하는가?
- [ ] button 텍스트가 행동을 설명하는가?
```

---

### [FAQ]

Q. Accessible Name이 뭐야?
A. 스크린 리더가 버튼, 링크, 입력 요소의 이름으로 읽는 값이다.

Q. Icon Button에는 무엇이 필요해?
A. 보이는 텍스트가 없으면 `aria-label` 또는 스크린 리더용 텍스트가 필요하다.

Q. Button 안에 아이콘만 있으면 안 돼?
A. 접근 가능한 이름이 없으면 사용자가 버튼 목적을 알 수 없으므로 안 된다.

Q. Link 텍스트는 어떻게 써야 해?
A. “자세히 보기”만 반복하기보다 가능한 경우 대상이나 목적을 함께 설명한다.

---

## 5.3 ARIA State Rules

### [개념]

ARIA State는 UI의 현재 상태를 보조기기에 전달하는 속성이다.

ARIA State는 selected, expanded, current, invalid, busy 같은 상태가 실제 UI 상태와 일치해야 한다.

---

### [핵심]

주요 ARIA State:

```text
aria-expanded
→ 열림 / 닫힘 상태

aria-selected
→ 선택된 tab / option 상태

aria-current
→ 현재 페이지 / 현재 단계

aria-invalid
→ 입력 오류 상태

aria-busy
→ 처리 중 상태

aria-checked
→ custom checkbox / switch 상태

aria-disabled
→ custom disabled 상태
```

기준:

- 실제 UI 상태와 일치
- state 변경 시 값 업데이트
- native attribute 우선
- aria-disabled만으로 실제 조작 차단 안 됨
- aria-selected는 적절한 role과 함께 사용
- aria-current는 현재 navigation / pagination에 사용

---

### [실무]

Expanded 예:

```jsx
<button type="button" aria-expanded={isOpen} aria-controls="filter-panel">
  필터
</button>
```

Current Page 예:

```jsx
<NavLink to="/lots" aria-current={isCurrent ? "page" : undefined}>
  LOT 관리
</NavLink>
```

Invalid 예:

```jsx
<input
  aria-invalid={Boolean(errorMessage)}
  aria-describedby={errorMessage ? "email-error" : undefined}
/>
```

Review 기준:

```md
- [ ] ARIA state가 실제 UI 상태와 일치하는가?
- [ ] state 변경 시 ARIA 값도 업데이트되는가?
- [ ] native attribute로 가능한 경우 native를 사용하는가?
- [ ] aria-disabled만 쓰고 실제 클릭을 막지 않는 문제가 없는가?
```

---

### [FAQ]

Q. ARIA State가 뭐야?
A. expanded, selected, current, invalid 같은 UI 상태를 보조기기에 전달하는 속성이다.

Q. aria-expanded는 언제 써?
A. accordion, dropdown, drawer처럼 열림 / 닫힘 상태가 있는 컨트롤에 사용한다.

Q. aria-current는 언제 써?
A. 현재 페이지, 현재 단계, 현재 pagination item을 표시할 때 사용한다.

Q. aria-disabled만 쓰면 disabled가 돼?
A. 아니다. aria-disabled는 의미 전달이고 실제 조작 차단은 별도로 필요하다.

---

## 5.4 ARIA Mistakes

### [개념]

ARIA Mistakes는 ARIA를 잘못 사용해 오히려 접근성을 해치는 실수다.

ARIA는 필요한 곳에 정확히 사용해야 하며 native HTML을 대체하는 도구로 남용하면 안 된다.

---

### [핵심]

자주 발생하는 실수:

- native button 대신 div role button 사용
- role만 있고 keyboard 동작 없음
- aria-label이 보이는 텍스트와 충돌
- aria-hidden으로 중요한 텍스트 숨김
- aria-expanded 값이 실제 상태와 불일치
- aria-selected를 role 없이 사용
- aria-disabled만 쓰고 클릭 가능
- input label 없이 aria-label로만 처리
- 모든 div에 role 추가
- role alert 남발
- aria-live 과도 사용

---

### [실무]

Troubleshooting:

```text
스크린 리더가 이상하게 읽음
→ aria-label / aria-labelledby 충돌 확인

열림 상태가 다르게 읽힘
→ aria-expanded 상태 동기화 확인

disabled인데 실행됨
→ aria-disabled 외 실제 이벤트 차단 확인

icon button 목적을 못 읽음
→ aria-label 추가

role button이 keyboard로 동작 안 함
→ native button으로 변경
```

Review Checklist:

```md
- [ ] ARIA를 native HTML 대체로 남용하지 않는가?
- [ ] ARIA state가 실제 상태와 일치하는가?
- [ ] 중요한 콘텐츠가 aria-hidden 처리되지 않는가?
- [ ] role 사용 시 keyboard 동작이 구현되어 있는가?
```

---

### [FAQ]

Q. ARIA에서 가장 흔한 실수는?
A. native element를 쓰면 되는 곳에 role을 남용하고 keyboard 동작을 빠뜨리는 것이다.

Q. aria-hidden은 위험해?
A. 중요한 정보에 사용하면 스크린 리더가 읽지 못하므로 위험하다.

Q. aria-label만 있으면 보이는 label은 없어도 돼?
A. 상황에 따라 가능하지만 보이는 label이 필요한 입력에서는 label을 제공하는 것이 좋다.

Q. role alert를 많이 쓰면 좋아?
A. 아니다. 중요한 동적 오류에 제한적으로 사용해야 한다.

---

# 6. Visual Accessibility Rules

## 6.1 Color Contrast Rules

### [개념]

Color Contrast는 텍스트, 아이콘, border, focus ring, 상태 색상이 배경과 충분히 구분되도록 하는 기준이다.

Color Contrast는 Light Mode, Dark Mode, Disabled State, Error State, Focus State에서 모두 검토해야 한다.

---

### [핵심]

Contrast 검토 대상:

- Body Text
- Heading
- Muted Text
- Button Text
- Link Text
- Error Message
- Helper Text
- Disabled Text
- Icon
- Focus Ring
- Border
- Badge Text
- Toast / Alert Text
- Dark Mode Text

기준:

- text와 background contrast 확보
- muted text도 읽을 수 있어야 함
- 색상만으로 상태 전달 금지
- focus ring은 배경과 구분되어야 함
- disabled도 필요한 정보는 읽을 수 있어야 함
- dark mode token 별도 검토
- semantic color token 사용

---

### [실무]

Token 예:

```css
:root {
  --color-background: #ffffff;
  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-focus-ring: #2563eb;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
  --color-text-muted: #d1d5db;
  --color-focus-ring: #93c5fd;
}
```

나쁜 예:

```css
.helperText {
  color: #cccccc;
}
```

Review 기준:

```md
- [ ] 본문 텍스트가 배경과 충분히 구분되는가?
- [ ] muted text가 너무 흐리지 않은가?
- [ ] dark mode에서 text contrast가 유지되는가?
- [ ] focus ring이 모든 theme에서 보이는가?
```

---

### [FAQ]

Q. Color Contrast가 뭐야?
A. 텍스트와 UI 요소가 배경과 충분히 구분되어 읽고 인식할 수 있는 정도다.

Q. muted text는 흐려도 괜찮아?
A. 너무 흐리면 안 된다. 보조 텍스트도 읽을 수 있어야 한다.

Q. Error는 빨간색만 쓰면 충분해?
A. 아니다. 텍스트, 아이콘, 메시지 등 색상 외 정보가 필요하다.

Q. Dark Mode에서도 contrast를 봐야 해?
A. 반드시 봐야 한다. dark mode에서는 text, border, focus ring이 쉽게 묻힐 수 있다.

---

## 6.2 Color Independent State Rules

### [개념]

Color Independent State는 상태 정보를 색상만으로 전달하지 않는 기준이다.

사용자는 색각 다양성, 저시력, 화면 환경 때문에 색상 차이를 구분하지 못할 수 있다.

---

### [핵심]

상태 전달 보조 수단:

- 텍스트
- 아이콘
- 패턴
- border style
- aria state
- label
- helper message
- badge text
- error message
- selected indicator

상태별 권장:

```text
Error
→ error color + error message + aria-invalid

Success
→ success color + success text

Selected
→ color + check icon / underline / aria-selected

Required
→ symbol + text 안내

Disabled
→ visual style + actual disabled
```

---

### [실무]

나쁜 예:

```jsx
<input className="errorBorderOnly" />
```

좋은 예:

```jsx
<input
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error" role="alert">
  올바른 이메일 형식이 아닙니다.
</p>
```

Badge 예:

```jsx
<Badge variant="error">불량</Badge>
<Badge variant="success">정상</Badge>
```

Review 기준:

```md
- [ ] 상태를 색상만으로 전달하지 않는가?
- [ ] error message가 있는가?
- [ ] selected 상태가 텍스트나 indicator와 함께 표현되는가?
- [ ] badge에 상태 텍스트가 포함되는가?
```

---

### [FAQ]

Q. 색상만으로 상태를 표시하면 왜 문제야?
A. 색상 차이를 구분하기 어려운 사용자는 상태를 이해하지 못할 수 있기 때문이다.

Q. Error에는 무엇이 필요해?
A. 색상뿐 아니라 오류 메시지와 input 연결이 필요하다.

Q. Badge는 색상만 있으면 돼?
A. 아니다. 정상, 오류, 경고 같은 텍스트가 함께 있어야 한다.

Q. 선택 상태는 어떻게 표시해?
A. 색상 외에 underline, check icon, aria-selected, 텍스트 등을 함께 사용한다.

---

## 6.3 Motion Accessibility Rules

### [개념]

Motion Accessibility는 animation, transition, scroll behavior가 사용자에게 불편을 주지 않도록 조정하는 기준이다.

움직임에 민감한 사용자를 위해 prefers-reduced-motion을 고려해야 한다.

---

### [핵심]

Motion 접근성 기준:

- 과도한 animation 금지
- 반복 animation 주의
- 자동 재생 motion 주의
- Skeleton shimmer 과도 사용 주의
- prefers-reduced-motion 대응
- motion은 사용성 보조 목적
- 중요한 정보는 animation만으로 전달 금지
- transition duration token 사용

적용 대상:

- Modal animation
- Drawer slide
- Toast animation
- Skeleton shimmer
- Page transition
- Scroll behavior
- Loading animation

---

### [실무]

Reduced Motion 예:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
    scroll-behavior: auto;
  }
}
```

Motion Token 예:

```css
:root {
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --easing-standard: ease;
}
```

Review 기준:

```md
- [ ] motion이 과도하지 않은가?
- [ ] prefers-reduced-motion을 고려했는가?
- [ ] animation만으로 상태를 전달하지 않는가?
- [ ] transition duration이 token으로 관리되는가?
```

---

### [FAQ]

Q. Motion Accessibility가 뭐야?
A. animation과 transition이 사용자에게 불편을 주지 않도록 조정하는 기준이다.

Q. prefers-reduced-motion은 왜 필요해?
A. 움직임에 민감한 사용자가 animation을 줄일 수 있어야 하기 때문이다.

Q. Skeleton shimmer는 항상 괜찮아?
A. 과도한 shimmer는 피하고 reduced motion을 고려해야 한다.

Q. Animation만으로 상태를 전달해도 돼?
A. 안 된다. 텍스트나 상태 표시가 함께 필요하다.

---

## 6.4 Touch Target Rules

### [개념]

Touch Target은 사용자가 손가락이나 포인터로 조작할 수 있는 실제 interactive area다.

Touch Target은 모바일과 태블릿에서 Button, Icon Button, Link, Checkbox, Radio, Pagination, Table Action에 중요하다.

---

### [핵심]

Touch Target 대상:

- Button
- Icon Button
- Link
- Checkbox
- Radio
- Select
- Pagination Button
- Table Action Button
- Navigation Item
- Close Button
- Menu Button

기준:

- 충분한 클릭 / 터치 영역 제공
- icon 자체보다 큰 button area 제공
- 인접 interactive element 간격 확보
- 모바일에서 너무 작은 link 금지
- disabled 상태에서도 layout shift 방지
- focus area와 click area 일치 권장

권장 기준:

```text
Button md
→ 40px 이상

Button lg
→ 48px 권장

Icon Button
→ 최소 40px 전후 권장

Form Input
→ 40px 이상 권장
```

---

### [실무]

Icon Button 예:

```css
.iconButton {
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

나쁜 예:

```css
.iconButton {
  width: 20px;
  height: 20px;
}
```

Review 기준:

```md
- [ ] 모바일에서 버튼을 누르기 충분한가?
- [ ] icon button 클릭 영역이 너무 작지 않은가?
- [ ] pagination button이 터치 가능한가?
- [ ] table action button이 모바일에서 사용 가능한가?
```

---

### [FAQ]

Q. Touch Target이 뭐야?
A. 사용자가 실제로 누르거나 클릭할 수 있는 조작 영역이다.

Q. Icon Button은 아이콘 크기만큼만 클릭되면 돼?
A. 아니다. 아이콘보다 넓은 button area를 제공해야 한다.

Q. 모바일에서 작은 링크는 문제야?
A. 문제가 될 수 있다. 충분한 터치 영역과 간격이 필요하다.

Q. Touch Target은 접근성 기준이야?
A. 그렇다. 모바일과 터치 환경의 사용성 및 접근성에 중요하다.

---

# 7. Component Accessibility Rules

## 7.1 Button Link Accessibility

### [개념]

Button Link Accessibility는 Button과 Link를 의미에 맞게 사용하고 접근 가능한 이름, keyboard 동작, focus 표시를 제공하는 기준이다.

Button은 action 실행이고 Link는 navigation이다.

---

### [핵심]

Button 기준:

- button element 사용
- type 기본값 button
- submit은 type submit 명시
- disabled 실제 적용
- loading 중 중복 클릭 방지
- focus-visible 제공
- icon button accessible name 제공

Link 기준:

- 페이지 이동에 Link 사용
- 외부 링크는 a 사용
- link text 목적 명확화
- 현재 페이지에는 aria-current 고려
- icon-only link는 accessible name 제공
- 새 창 열림 안내 고려

---

### [실무]

Button 예:

```jsx
<button type="button" onClick={handleSave}>
  저장
</button>
```

Link 예:

```jsx
<Link to="/lots">LOT 목록으로 이동</Link>
```

Icon Button 예:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

Review 기준:

```md
- [ ] action에 Button을 사용하는가?
- [ ] navigation에 Link를 사용하는가?
- [ ] icon button에 accessible name이 있는가?
- [ ] focus-visible이 있는가?
```

---

### [FAQ]

Q. Button과 Link는 어떻게 구분해?
A. 저장, 삭제 같은 action은 Button이고 페이지 이동은 Link다.

Q. Button type 기본값은 뭐가 좋아?
A. 공통 Button은 `type="button"`을 기본값으로 두는 것이 안전하다.

Q. Icon Button에는 뭐가 필요해?
A. `aria-label` 또는 스크린 리더용 텍스트가 필요하다.

Q. 현재 페이지 Link는 어떻게 표시해?
A. active style과 `aria-current="page"`를 고려한다.

---

## 7.2 Modal Drawer Accessibility

### [개념]

Modal Drawer Accessibility는 화면 위에 열리는 overlay UI가 keyboard와 스크린 리더 사용자에게 올바르게 동작하도록 만드는 기준이다.

Modal과 Drawer는 focus 흐름을 강하게 바꾸므로 접근성 검토가 필수다.

---

### [핵심]

Modal 기준:

- role dialog
- aria-modal true
- title 연결
- 닫기 버튼
- focus trap
- focus restore
- ESC 닫기 정책
- background scroll lock
- overlay click 정책
- loading / error 상태 접근 가능

Drawer 기준:

- title 제공
- 닫기 버튼 제공
- open / closed state
- trigger와 연결
- focus 관리
- keyboard 닫기
- navigation landmark 고려

---

### [실무]

Modal 구조 예:

```jsx
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">삭제 확인</h2>
  <button type="button" aria-label="닫기" onClick={onClose}>
    <CloseIcon aria-hidden="true" />
  </button>
  <p>삭제한 데이터는 복구할 수 없습니다.</p>
</div>
```

Drawer 예:

```jsx
<Drawer isOpen={isOpen} title="메뉴" onClose={closeDrawer}>
  <nav aria-label="모바일 메뉴">...</nav>
</Drawer>
```

Review 기준:

```md
- [ ] dialog role과 aria-modal이 있는가?
- [ ] title이 연결되는가?
- [ ] 닫기 버튼이 있는가?
- [ ] focus trap과 focus restore를 고려했는가?
- [ ] keyboard로 닫을 수 있는가?
```

---

### [FAQ]

Q. Modal 접근성에서 가장 중요한 것은?
A. dialog 역할, title 연결, 닫기 버튼, focus trap, focus restore다.

Q. Modal에 title이 꼭 필요해?
A. 필요하다. 사용자가 dialog의 목적을 이해할 수 있어야 한다.

Q. Drawer에도 focus 관리가 필요해?
A. 필요하다. Drawer가 overlay처럼 열리면 Modal과 유사하게 focus 관리를 고려해야 한다.

Q. ESC로 닫기 기능은 필수야?
A. 일반적으로 권장된다. 중요한 작업 중에는 정책을 명확히 정해야 한다.

---

## 7.3 Table Accessibility

### [개념]

Table Accessibility는 행과 열 구조 데이터를 스크린 리더와 keyboard 사용자가 이해할 수 있도록 table 구조를 올바르게 작성하는 기준이다.

Table은 레이아웃 용도가 아니라 표 데이터에 사용해야 한다.

---

### [핵심]

Table 기준:

- table element 사용
- thead / tbody 구조 사용
- th 사용
- scope 사용
- caption 필요성 검토
- 정렬 가능 컬럼 상태 표시
- row action accessible name 제공
- Empty State 제공
- 모바일 대응 유지
- layout 용도 table 금지

---

### [실무]

Table 예:

```jsx
<table>
  <caption className="srOnly">LOT 생산 현황 목록</caption>
  <thead>
    <tr>
      <th scope="col">LOT 번호</th>
      <th scope="col">상태</th>
      <th scope="col">완료 수량</th>
      <th scope="col">작업</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LOT-001</td>
      <td>진행중</td>
      <td>120EA</td>
      <td>
        <Button variant="secondary">상세 보기</Button>
      </td>
    </tr>
  </tbody>
</table>
```

Sort Button 예:

```jsx
<button type="button" aria-label="완료 수량 기준 정렬">
  완료 수량
</button>
```

Review 기준:

```md
- [ ] 표 데이터에 table을 사용하는가?
- [ ] th와 scope가 있는가?
- [ ] caption 필요성을 검토했는가?
- [ ] row action 이름이 명확한가?
- [ ] Empty State가 있는가?
```

---

### [FAQ]

Q. Table 접근성에서 중요한 것은?
A. thead, tbody, th, scope, caption, row action 이름, Empty State가 중요하다.

Q. layout을 위해 table을 써도 돼?
A. 안 된다. table은 표 데이터에 사용하고 layout은 Grid나 Flexbox를 사용한다.

Q. caption은 꼭 필요해?
A. 복잡한 표나 문맥이 불명확한 표에는 제공하는 것이 좋다.

Q. row action 버튼 이름은 어떻게 해야 해?
A. “상세 보기”처럼 명확하게 작성하고 필요하면 행 context를 포함한다.

---

## 7.4 Feedback Accessibility

### [개념]

Feedback Accessibility는 Loading, Error, Success, Empty, Toast, Alert 상태가 보조기기 사용자에게도 전달되도록 하는 기준이다.

Feedback State는 시각적으로 보이는 것뿐 아니라 screen reader와 keyboard 흐름에서도 인식 가능해야 한다.

---

### [핵심]

Feedback 접근성 기준:

- loading에는 role status 고려
- 중요한 error에는 role alert 고려
- toast에는 aria-live 고려
- field error는 input과 연결
- success message는 필요한 경우 aria-live
- empty state는 명확한 title 제공
- 색상만으로 상태 전달 금지
- modal 내부 error는 modal 안에서 접근 가능
- focus 이동 필요성 검토

---

### [실무]

Loading 예:

```jsx
<div role="status" aria-live="polite">
  데이터를 불러오는 중입니다.
</div>
```

Error 예:

```jsx
<p id="password-error" role="alert">
  비밀번호를 입력해 주세요.
</p>
```

Toast Live Region 예:

```jsx
<div aria-live="polite" aria-atomic="true">
  저장되었습니다.
</div>
```

Review 기준:

```md
- [ ] 중요한 상태 변경이 보조기기에 전달되는가?
- [ ] field error가 input과 연결되는가?
- [ ] toast가 필요한 경우 live region으로 전달되는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
```

---

### [FAQ]

Q. Feedback State에도 접근성이 필요해?
A. 필요하다. loading, error, success 상태는 보조기기 사용자에게도 전달되어야 한다.

Q. role status는 언제 써?
A. loading처럼 현재 상태를 부드럽게 알릴 때 사용할 수 있다.

Q. role alert는 언제 써?
A. 중요한 동적 오류 메시지를 즉시 알릴 때 사용할 수 있다.

Q. Toast는 스크린 리더가 읽어야 해?
A. 중요한 Toast라면 aria-live 영역을 통해 전달하는 것이 좋다.

---

# 8. Documentation Rules

## 8.1 Design System Documentation Definition

### [개념]

Design System Documentation은 Design Token, Component Specification, Layout Pattern, Feedback Pattern, Accessibility Rule, Review Checklist를 Agent가 검색하고 사용할 수 있게 정리한 문서다.

이 문서는 사람용 디자인 설명서가 아니라 RAG Retrieval, Agent Code Generation, Agent Review를 위한 구조화 문서다.

---

### [핵심]

Documentation 필수 구성:

- Component Purpose
- Anatomy
- Props Table
- Variant Rules
- Size Rules
- State Rules
- Accessibility Rules
- Usage Rules
- Do / Don't
- Examples
- Common Mistakes
- Review Checklist
- Retrieval Queries
- FAQ

문서화 목적:

- Frontend Agent 생성 기준 제공
- Review Agent 검토 기준 제공
- PM Agent 완료 판단 기준 제공
- 컴포넌트 사용 기준 통일
- token / state / accessibility 연결
- 잘못된 사용 방지
- 검색 가능한 Q&A 제공

---

### [실무]

Component 문서 예:

```md
# Button

## Purpose

사용자 action을 실행한다.

## Variants

- primary: 주요 action
- secondary: 보조 action
- danger: 위험 action

## Accessibility

- button element 사용
- focus-visible 제공
- icon button은 aria-label 제공

## Do

- action 문구를 명확히 작성한다.

## Don't

- 페이지 이동에 Button을 사용하지 않는다.
```

Review 기준:

```md
- [ ] 문서가 RAG 검색 가능한 구조인가?
- [ ] FAQ가 충분한가?
- [ ] Do / Don't가 있는가?
- [ ] Review Checklist가 있는가?
- [ ] Retrieval Queries가 있는가?
```

---

### [FAQ]

Q. Design System Documentation이 뭐야?
A. Token, Component, Layout, Feedback, Accessibility, Review 기준을 Agent가 검색 가능하게 정리한 문서다.

Q. Documentation은 사람 공부용이야?
A. 아니다. RAG Retrieval과 Agent 생성 / 검토를 위한 기준 문서다.

Q. 컴포넌트 문서에 무엇이 필요해?
A. Purpose, Props, Variant, Size, State, Accessibility, Usage, Do / Don't, Examples, Checklist가 필요하다.

Q. FAQ가 왜 중요해?
A. Agent가 자연어 질문으로 규칙을 검색할 때 Q&A 구조가 retrieval 품질을 높이기 때문이다.

---

## 8.2 Documentation Structure Rules

### [개념]

Documentation Structure Rules는 Design System 문서가 일정한 구조를 유지하도록 만드는 기준이다.

구조가 일관되어야 Agent가 필요한 정보를 안정적으로 검색하고 비교할 수 있다.

---

### [핵심]

권장 구조:

```md
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]

정의와 목적.

---

### [핵심]

핵심 기준.

---

### [실무]

실무 적용 기준과 예시.

---

### [FAQ]

Q. 질문
A. 답변

---

# Retrieval Queries

### [FAQ]

Q. 질문
A. 답변
```

구조 기준:

- section 번호 사용
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 유지
- FAQ는 Q/A 형식
- FAQ 내부에 무분별한 구분선 금지
- Retrieval Queries 포함
- 같은 용어 반복 사용
- 코드 예시는 짧고 직접적
- chunk가 독립 검색 가능해야 함

---

### [실무]

좋은 문서 구조:

```md
## 2.1 Button Accessibility

### [개념]

Button 접근성 기준.

### [핵심]

- button element 사용
- focus-visible 제공
- icon button accessible name 제공

### [실무]

예제 코드.

### [FAQ]

Q. Icon Button에는 뭐가 필요해?
A. aria-label 또는 스크린 리더용 텍스트가 필요하다.
```

Review 기준:

```md
- [ ] 구조가 Master RAG Rules와 일치하는가?
- [ ] section이 너무 길거나 너무 짧지 않은가?
- [ ] FAQ가 충분한가?
- [ ] 검색 키워드가 반복 포함되는가?
```

---

### [FAQ]

Q. Documentation Structure가 왜 중요해?
A. 문서 구조가 일정해야 Agent가 필요한 기준을 안정적으로 검색할 수 있기 때문이다.

Q. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 유지해야 해?
A. 유지해야 한다. Master RAG Rules의 기본 검색 구조다.

Q. FAQ 내부에 구분선을 많이 넣어도 돼?
A. 권장하지 않는다. FAQ 내부는 Q/A 흐름을 유지해야 한다.

Q. Retrieval Queries는 왜 필요해?
A. 자연어 질문과 검색 키워드 기반 retrieval 성능을 높이기 위해 필요하다.

---

## 8.3 Example Documentation Rules

### [개념]

Example Documentation Rules는 문서에 포함되는 코드 예시와 사용 예시를 작성하는 기준이다.

예시는 Frontend Agent가 바로 코드 생성에 활용할 수 있을 만큼 짧고 명확해야 한다.

---

### [핵심]

예제 작성 기준:

- 짧고 직접적
- 좋은 예 / 나쁜 예 구분
- token 사용 포함
- accessibility 포함
- state 포함
- domain 예시 포함 가능
- boilerplate 최소화
- 실제 사용 가능한 코드 우선
- 잘못된 패턴을 명확히 제시

좋은 예제 조건:

```text
Button variant 사용
Input label 연결
Error aria-describedby 연결
Modal role dialog 사용
Table th scope 사용
Focus visible token 사용
```

---

### [실무]

좋은 예:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

나쁜 예:

```jsx
<div onClick={onClose}>
  <CloseIcon />
</div>
```

좋은 token 예:

```css
.button:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

Review 기준:

```md
- [ ] 예제가 실제 기준을 보여주는가?
- [ ] 예제가 너무 길지 않은가?
- [ ] 접근성 / token / state 기준이 포함되는가?
- [ ] 나쁜 예가 반려 기준을 명확히 보여주는가?
```

---

### [FAQ]

Q. 예제는 길수록 좋아?
A. 아니다. RAG 문서에서는 짧고 직접적인 예제가 검색과 코드 생성에 유리하다.

Q. 나쁜 예도 문서에 넣어야 해?
A. 넣는 것이 좋다. Review Agent가 반려 기준을 잡기 쉽다.

Q. 예제에 접근성을 포함해야 해?
A. Button, Input, Modal, Table 같은 핵심 컴포넌트에는 반드시 포함하는 것이 좋다.

Q. 도메인 예시도 필요해?
A. 가능하면 좋다. Agent가 실제 프로젝트 맥락에 맞게 생성하기 쉬워진다.

---

## 8.4 Documentation Mistakes

### [개념]

Documentation Mistakes는 문서가 사람 설명 중심으로 흐르거나 Agent Retrieval에 필요한 구조와 키워드를 제공하지 못하는 실수다.

Documentation 실수는 RAG 검색 누락, Agent 판단 오류, 중복 컴포넌트 생성 문제로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- 긴 서술형 설명만 있음
- FAQ 부족
- Retrieval Queries 없음
- 용어가 문서마다 다름
- token / component / state 연결 없음
- Do / Don't 없음
- Review Checklist 없음
- 코드 예제가 너무 김
- 좋은 예 / 나쁜 예 구분 없음
- 접근성 기준 누락
- Part 간 연계 없음
- 사람 공부용 문서처럼 작성
- Agent 역할 기준 없음

---

### [실무]

Troubleshooting:

```text
Agent가 Button 기준을 못 찾음
→ FAQ와 Retrieval Queries에 Button 관련 Q/A 추가

Review 기준이 모호함
→ Review Checklist 추가

컴포넌트 사용이 제각각
→ Usage / Do / Don't 추가

접근성 누락 반복
→ Accessibility Rules와 Common Mistakes 추가

Part 간 중복 / 충돌
→ Part 연계 Flow 추가
```

Review Checklist:

```md
- [ ] RAG Retrieval에 적합한 구조인가?
- [ ] FAQ가 충분한가?
- [ ] 핵심 용어가 반복되는가?
- [ ] Agent Usage 기준이 있는가?
- [ ] Review Checklist가 있는가?
```

---

### [FAQ]

Q. Documentation에서 가장 흔한 실수는?
A. 사람 설명 중심으로 길게 쓰고 FAQ, Retrieval Queries, Review Checklist를 부족하게 작성하는 것이다.

Q. 용어 통일이 왜 중요해?
A. 같은 개념을 다른 이름으로 쓰면 Agent 검색과 판단이 흔들릴 수 있다.

Q. Do / Don't가 없으면 왜 문제야?
A. 잘못된 사용을 Review Agent가 명확히 반려하기 어렵다.

Q. 문서가 길면 좋은 거 아니야?
A. 길이보다 검색 가능한 구조, 명확한 기준, FAQ, 독립 chunk가 더 중요하다.

---

# 9. Review System Rules

## 9.1 Review Agent Final Checklist

### [개념]

Review Agent Final Checklist는 Design System Foundation 문서를 기준으로 UI 구현을 최종 검토하는 통합 기준이다.

Review Agent는 정상 화면만 보지 않고 component, token, state, layout, responsive, theme, accessibility, documentation 기준을 함께 확인해야 한다.

---

### [핵심]

Final Review Checklist:

```md
## Token

- [ ] raw color가 남발되지 않는가?
- [ ] spacing token을 사용하는가?
- [ ] typography token을 사용하는가?
- [ ] focus ring token이 있는가?
- [ ] theme 확장 가능성이 있는가?

## Component

- [ ] Core Component를 적절히 사용하는가?
- [ ] Button과 Link를 혼동하지 않는가?
- [ ] Input label이 연결되는가?
- [ ] Modal 접근성이 있는가?
- [ ] Table 구조가 semantic한가?

## State

- [ ] Loading State가 있는가?
- [ ] Empty State가 있는가?
- [ ] Error State가 있는가?
- [ ] Success Feedback이 있는가?
- [ ] Disabled State가 실제로 동작하는가?

## Layout

- [ ] Container 기준이 적용되는가?
- [ ] Section 구조가 명확한가?
- [ ] Grid / Stack / Inline이 적절한가?
- [ ] component margin이 남용되지 않는가?

## Responsive

- [ ] mobile first 기준인가?
- [ ] 모바일에서 가로 스크롤이 없는가?
- [ ] Table / Modal / Form이 모바일에서 사용 가능한가?
- [ ] Touch Target이 충분한가?

## Accessibility

- [ ] Semantic HTML을 사용하는가?
- [ ] Keyboard 조작이 가능한가?
- [ ] Focus Visible이 있는가?
- [ ] Accessible Name이 있는가?
- [ ] Error Message가 input과 연결되는가?
- [ ] 색상만으로 상태를 전달하지 않는가?

## Documentation

- [ ] Component Spec과 구현이 일치하는가?
- [ ] 새로운 variant / props 추가 시 문서가 업데이트되었는가?
```

---

### [실무]

Review Decision:

```text
Approved
→ 주요 Design System 기준 충족

Needs Fix
→ 일부 token / state / responsive / accessibility 미흡

Blocked
→ 사용자 흐름 차단, keyboard 사용 불가, 주요 error 누락, 모바일 사용 불가, 심각한 contrast 문제
```

Blocked 예:

```text
저장 버튼 keyboard 조작 불가
Input label 없음
Error Message 없음
Modal 닫기 불가
Modal focus 관리 없음
모바일에서 주요 action 화면 밖으로 나감
Dark Mode에서 텍스트가 보이지 않음
중요 오류를 Toast만으로 표시
```

---

### [FAQ]

Q. Review Agent Final Checklist는 뭐야?
A. Token, Component, State, Layout, Responsive, Theme, Accessibility, Documentation을 통합 검토하는 기준이다.

Q. Review Agent가 가장 중요하게 봐야 하는 것은?
A. 사용자 흐름을 막는 문제, 접근성 심각 문제, 주요 상태 누락, 모바일 사용 불가 여부다.

Q. 어떤 경우 Blocked야?
A. 주요 기능을 사용할 수 없거나 keyboard, form, modal, error, responsive 문제가 심각하면 Blocked다.

Q. 디자인이 예쁘면 Approved야?
A. 아니다. Design System 기준과 접근성, 상태 처리, 반응형 기준을 만족해야 한다.

---

## 9.2 PM Agent Completion Checklist

### [개념]

PM Agent Completion Checklist는 PM Agent가 화면이 실제로 완료되었는지 판단할 때 사용하는 기준이다.

PM Agent는 세부 코드보다 요구사항 충족, 사용자 흐름, 주요 상태, 모바일 사용성, 출시 차단 이슈 여부를 판단한다.

---

### [핵심]

PM Completion Checklist:

```md
## Requirement

- [ ] 요구사항과 화면 목적이 일치하는가?
- [ ] 주요 사용자 action이 가능한가?
- [ ] 필수 정보가 표시되는가?

## User Flow

- [ ] 사용자가 다음 행동을 이해할 수 있는가?
- [ ] 버튼 문구가 명확한가?
- [ ] 성공 / 실패 / 빈 상태를 이해할 수 있는가?

## State

- [ ] loading 상태가 있는가?
- [ ] empty 상태가 있는가?
- [ ] error 상태가 있는가?
- [ ] success feedback이 있는가?

## Responsive

- [ ] 모바일에서 주요 기능을 사용할 수 있는가?
- [ ] Modal / Table / Form이 깨지지 않는가?

## Accessibility Critical

- [ ] label 없는 주요 input이 없는가?
- [ ] 주요 button이 keyboard로 조작 가능한가?
- [ ] focus 위치를 알 수 있는가?

## Decision

- [ ] UI Complete
- [ ] UI Partial
- [ ] UI Blocked
```

---

### [실무]

PM Decision 기준:

```text
UI Complete
→ 요구사항 충족 + 주요 흐름 가능 + 상태 처리 존재 + 모바일 사용 가능

UI Partial
→ 기능은 가능하지만 일부 상태 / 문구 / layout 개선 필요

UI Blocked
→ 주요 기능 사용 불가, 상태 이해 불가, 모바일 사용 불가, 접근성 심각 문제
```

PM 판단 예:

```text
검색 화면
→ 검색 가능
→ 결과 없음 안내 있음
→ 로딩 표시 있음
→ 실패 시 다시 시도 있음
→ 모바일에서 입력 / 버튼 사용 가능
→ UI Complete
```

---

### [FAQ]

Q. PM Agent는 무엇을 기준으로 완료 판단해?
A. 요구사항 충족, 사용자 흐름, 상태 처리, 모바일 사용성, 심각한 접근성 이슈 여부를 기준으로 판단한다.

Q. PM Agent가 CSS 세부 구현까지 봐야 해?
A. 아니다. 사용자가 화면을 이해하고 기능을 사용할 수 있는지 중심으로 판단한다.

Q. 정상 화면만 동작하면 Complete야?
A. 아니다. Loading, Empty, Error, Success 상태도 기본적으로 확인해야 한다.

Q. 모바일 사용 불가는 Blocked야?
A. 주요 기능 사용이 불가능하면 Blocked가 될 수 있다.

---

## 9.3 Frontend Agent Final Generation Rules

### [개념]

Frontend Agent Final Generation Rules는 Frontend Agent가 Design System Foundation 기준을 적용해 최종 UI를 생성할 때 따라야 하는 통합 규칙이다.

Frontend Agent는 컴포넌트, token, feedback, layout, responsive, theme, accessibility를 함께 고려해야 한다.

---

### [핵심]

Frontend Agent 생성 순서:

```text
Requirement 분석
→ Page Layout 선택
→ Core Component 선택
→ Design Token 적용
→ Component Variant / Size / State 선택
→ Feedback State 설계
→ Responsive 기준 적용
→ Accessibility 기준 적용
→ Theme 확장성 확인
→ Review Checklist 자체 검토
→ Output
```

생성 기준:

- raw color 직접 사용 금지
- spacing token 사용
- Core Component 우선 사용
- Button / Link 의미 구분
- Input label 연결
- Error Message 연결
- Loading / Empty / Error / Success 포함
- Mobile First 적용
- Focus Visible 유지
- Accessible Name 제공
- Modal / Table 접근성 검토
- 문구는 사용자 친화적으로 작성

---

### [실무]

생성 전 Self Checklist:

```md
- [ ] 요구사항과 화면 목적을 이해했는가?
- [ ] 기존 Core Component로 해결 가능한가?
- [ ] 필요한 token이 있는가?
- [ ] loading / empty / error / success가 필요한가?
- [ ] 모바일에서 깨지지 않는가?
- [ ] keyboard로 조작 가능한가?
- [ ] input label과 error 연결이 있는가?
- [ ] raw color / raw spacing을 피했는가?
```

나쁜 생성:

```jsx
<div style={{ color: "red" }} onClick={save}>
  OK
</div>
```

좋은 생성:

```jsx
<Button
  variant="primary"
  type="submit"
  isLoading={isSubmitting}
  disabled={isSubmitting}
>
  저장
</Button>
```

---

### [FAQ]

Q. Frontend Agent는 최종 UI 생성 시 무엇을 확인해야 해?
A. Requirement, Layout, Core Component, Token, State, Responsive, Theme, Accessibility 기준을 함께 확인해야 한다.

Q. Frontend Agent가 raw style을 써도 돼?
A. 공통 UI에서는 피해야 한다. token과 component style을 우선 사용한다.

Q. Frontend Agent가 정상 상태만 만들면 안 돼?
A. 안 된다. loading, empty, error, success 상태를 함께 고려해야 한다.

Q. Frontend Agent가 접근성을 자동으로 고려해야 해?
A. 그래야 한다. label, focus, keyboard, accessible name, error 연결은 기본 생성 기준이다.

---

# 10. Final Checklist

## 10.1 Part07 Quality Checklist

### [개념]

Part07 Quality Checklist는 Accessibility Documentation Review Rules 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Accessibility Core

- [ ] Accessibility System 정의가 명확한가?
- [ ] Scope 포함 / 제외 기준이 명확한가?
- [ ] Semantic HTML 기준이 있는가?
- [ ] Landmark 기준이 있는가?
- [ ] Heading Structure 기준이 있는가?

## Keyboard / Focus

- [ ] Keyboard Navigation 기준이 있는가?
- [ ] Focus Visible 기준이 있는가?
- [ ] Focus Management 기준이 있는가?
- [ ] Keyboard Focus Mistakes가 포함되어 있는가?

## Form Accessibility

- [ ] Label Association 기준이 있는가?
- [ ] Error Message Association 기준이 있는가?
- [ ] Required / Disabled / Readonly 기준이 있는가?
- [ ] Form Accessibility Mistakes가 포함되어 있는가?

## ARIA

- [ ] ARIA Usage 기준이 있는가?
- [ ] Accessible Name 기준이 있는가?
- [ ] ARIA State 기준이 있는가?
- [ ] ARIA Mistakes가 포함되어 있는가?

## Visual Accessibility

- [ ] Color Contrast 기준이 있는가?
- [ ] Color Independent State 기준이 있는가?
- [ ] Motion Accessibility 기준이 있는가?
- [ ] Touch Target 기준이 있는가?

## Component Accessibility

- [ ] Button / Link 접근성 기준이 있는가?
- [ ] Modal / Drawer 접근성 기준이 있는가?
- [ ] Table 접근성 기준이 있는가?
- [ ] Feedback 접근성 기준이 있는가?

## Documentation

- [ ] Documentation 기준이 있는가?
- [ ] Documentation Structure 기준이 있는가?
- [ ] Example Documentation 기준이 있는가?
- [ ] Documentation Mistakes가 포함되어 있는가?

## Review System

- [ ] Review Agent Final Checklist가 있는가?
- [ ] PM Agent Completion Checklist가 있는가?
- [ ] Frontend Agent Final Generation Rules가 있는가?
- [ ] Approved / Needs Fix / Blocked 기준이 있는가?
```

---

### [실무]

Part07은 Design System Foundation의 최종 검토 문서다.

Part07은 Part01부터 Part06까지의 기준을 접근성, 문서화, 최종 Review 관점에서 통합한다.

Part 연계:

```text
Part01 Design System Core
→ Part02 Design Token Rules
→ Part03 Component Specification Rules
→ Part04 Core Component Rules
→ Part05 Feedback State Pattern Rules
→ Part06 Layout Responsive Theme Rules
→ Part07 Accessibility Documentation Review Rules
```

Part07 기준은 Review Agent가 최종 UI 품질을 승인 / 수정 요청 / 차단 판단할 때 사용한다.

---

### [FAQ]

Q. Part07의 역할은 뭐야?
A. Accessibility, Documentation, Final Review 기준을 정의하고 Part01~Part06을 통합 검토하는 문서다.

Q. Part07은 왜 마지막에 있어?
A. Token, Component, Feedback, Layout, Theme 기준을 최종 접근성 및 Review 기준으로 통합하기 때문이다.

Q. Part07에서 가장 중요한 것은 뭐야?
A. Semantic HTML, Keyboard, Focus, Form Accessibility, ARIA, Contrast, Documentation, Review Checklist다.

Q. Part07 최종 승인 기준은 뭐야?
A. Frontend Agent가 접근성 기준을 반영해 UI를 생성하고 Review Agent가 최종 검토할 수 있을 만큼 기준과 FAQ가 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Accessibility System이 뭐야?
A. 키보드, 스크린 리더, 저시력, 색각 다양성, 터치 사용자가 UI를 사용할 수 있도록 만드는 공통 기준이다.

Q. Design System에 Accessibility가 왜 필요해?
A. 공통 컴포넌트가 접근성을 만족하면 전체 화면의 사용성과 품질이 안정되기 때문이다.

Q. 접근성은 나중에 추가해도 돼?
A. 권장하지 않는다. 컴포넌트와 레이아웃 설계 단계부터 반영해야 수정 비용이 줄어든다.

Q. Accessibility Scope는 어디까지야?
A. Semantic HTML, keyboard, focus, form label, error 연결, aria, contrast, modal, table, feedback 접근성까지다.

Q. Semantic HTML이 뭐야?
A. HTML 요소를 시각적 모양이 아니라 의미에 맞게 사용하는 것이다.

Q. div에 onClick을 넣어 button처럼 써도 돼?
A. 권장하지 않는다. 기본 keyboard 동작과 접근성이 부족하므로 button을 사용한다.

Q. 페이지 이동에 button을 써도 돼?
A. 권장하지 않는다. 페이지 이동은 Link 또는 a를 사용한다.

Q. Landmark가 뭐야?
A. main, nav, header, footer, aside처럼 페이지 주요 영역을 의미적으로 구분하는 구조다.

Q. main은 꼭 필요해?
A. 권장된다. 페이지의 주요 콘텐츠 영역을 보조기기가 빠르게 찾을 수 있다.

Q. nav가 여러 개면 어떻게 해?
A. `aria-label`로 주요 메뉴, 보조 메뉴처럼 구분한다.

Q. Heading Structure는 왜 중요해?
A. 사용자와 보조기기가 페이지 구조를 이해하고 빠르게 탐색할 수 있기 때문이다.

Q. 글자를 작게 보이게 하려고 h4를 써도 돼?
A. 안 된다. heading level은 의미 구조이고, 크기는 CSS와 typography token으로 조정한다.

Q. Keyboard Navigation이 뭐야?
A. 마우스 없이 keyboard만으로 화면을 탐색하고 조작할 수 있게 하는 기준이다.

Q. 모든 클릭 요소가 Tab으로 접근 가능해야 해?
A. 사용자가 조작하는 interactive element는 keyboard 접근이 가능해야 한다.

Q. div onClick을 keyboard로 쓰게 만들면 괜찮아?
A. 가능은 하지만 role, tabIndex, keyboard event를 직접 구현해야 하므로 native button이 우선이다.

Q. Focus Visible이 뭐야?
A. keyboard 사용자가 현재 선택된 요소를 볼 수 있게 하는 focus 표시다.

Q. outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible style을 제공해야 한다.

Q. focus ring 색상도 token으로 관리해야 해?
A. 권장된다. theme와 dark mode 대응을 위해 `--color-focus-ring`을 사용한다.

Q. Focus Management가 뭐야?
A. 화면 상태가 바뀔 때 focus 위치를 적절히 이동하거나 복원하는 기준이다.

Q. Modal을 열면 focus는 어디로 가야 해?
A. Modal 내부의 닫기 버튼, 첫 입력 요소, 또는 title 영역으로 이동하는 것이 좋다.

Q. Modal이 닫히면 focus는 어디로 가야 해?
A. Modal을 열었던 trigger element로 돌아가는 것이 좋다.

Q. Keyboard Focus에서 가장 흔한 실수는?
A. focus outline을 제거하거나 div onClick으로 button을 대체하는 것이다.

Q. Label Association이 뭐야?
A. label과 input을 연결해 사용자가 어떤 값을 입력해야 하는지 알 수 있게 하는 기준이다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 안 된다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. 검색 input에도 label이 필요해?
A. 필요하다. 시각적으로 숨긴 label을 사용할 수 있다.

Q. Error Message Association이 뭐야?
A. 오류 메시지를 해당 input과 연결해 보조기기도 오류를 인식할 수 있게 하는 기준이다.

Q. aria-invalid는 언제 써?
A. 입력값이 오류 상태일 때 `aria-invalid="true"`를 사용한다.

Q. aria-describedby는 왜 필요해?
A. helper text나 error message를 input과 연결해 스크린 리더가 읽을 수 있게 한다.

Q. required는 어떻게 표시해?
A. 필수 입력임을 label 근처에 표시하고 필요한 경우 안내 문구를 제공한다.

Q. disabled와 readonly는 뭐가 달라?
A. disabled는 조작과 제출에서 제외되고, readonly는 수정은 불가하지만 값은 읽을 수 있고 제출 가능하다.

Q. Form Accessibility에서 가장 흔한 실수는?
A. placeholder를 label처럼 사용하고 error message를 input과 연결하지 않는 것이다.

Q. ARIA는 언제 써?
A. Semantic HTML만으로 의미를 전달하기 어려울 때 보완용으로 사용한다.

Q. ARIA를 많이 쓰면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다.

Q. role button을 div에 넣으면 button이 돼?
A. 의미 일부만 추가된다. keyboard 동작과 focus 처리를 직접 구현해야 하므로 native button이 우선이다.

Q. Accessible Name이 뭐야?
A. 스크린 리더가 버튼, 링크, 입력 요소의 이름으로 읽는 값이다.

Q. Icon Button에는 무엇이 필요해?
A. 보이는 텍스트가 없으면 `aria-label` 또는 스크린 리더용 텍스트가 필요하다.

Q. Button 안에 아이콘만 있으면 안 돼?
A. 접근 가능한 이름이 없으면 사용자가 버튼 목적을 알 수 없으므로 안 된다.

Q. ARIA State가 뭐야?
A. expanded, selected, current, invalid 같은 UI 상태를 보조기기에 전달하는 속성이다.

Q. aria-expanded는 언제 써?
A. accordion, dropdown, drawer처럼 열림 / 닫힘 상태가 있는 컨트롤에 사용한다.

Q. aria-current는 언제 써?
A. 현재 페이지, 현재 단계, 현재 pagination item을 표시할 때 사용한다.

Q. aria-disabled만 쓰면 disabled가 돼?
A. 아니다. aria-disabled는 의미 전달이고 실제 조작 차단은 별도로 필요하다.

Q. ARIA에서 가장 흔한 실수는?
A. native element를 쓰면 되는 곳에 role을 남용하고 keyboard 동작을 빠뜨리는 것이다.

Q. Color Contrast가 뭐야?
A. 텍스트와 UI 요소가 배경과 충분히 구분되어 읽고 인식할 수 있는 정도다.

Q. muted text는 흐려도 괜찮아?
A. 너무 흐리면 안 된다. 보조 텍스트도 읽을 수 있어야 한다.

Q. 색상만으로 상태를 표시하면 왜 문제야?
A. 색상 차이를 구분하기 어려운 사용자는 상태를 이해하지 못할 수 있기 때문이다.

Q. Error에는 무엇이 필요해?
A. 색상뿐 아니라 오류 메시지와 input 연결이 필요하다.

Q. Motion Accessibility가 뭐야?
A. animation과 transition이 사용자에게 불편을 주지 않도록 조정하는 기준이다.

Q. prefers-reduced-motion은 왜 필요해?
A. 움직임에 민감한 사용자가 animation을 줄일 수 있어야 하기 때문이다.

Q. Touch Target이 뭐야?
A. 사용자가 실제로 누르거나 클릭할 수 있는 조작 영역이다.

Q. Icon Button은 아이콘 크기만큼만 클릭되면 돼?
A. 아니다. 아이콘보다 넓은 button area를 제공해야 한다.

Q. Button과 Link는 어떻게 구분해?
A. 저장, 삭제 같은 action은 Button이고 페이지 이동은 Link다.

Q. Modal 접근성에서 가장 중요한 것은?
A. dialog 역할, title 연결, 닫기 버튼, focus trap, focus restore다.

Q. Modal에 title이 꼭 필요해?
A. 필요하다. 사용자가 dialog의 목적을 이해할 수 있어야 한다.

Q. Drawer에도 focus 관리가 필요해?
A. 필요하다. Drawer가 overlay처럼 열리면 Modal과 유사하게 focus 관리를 고려해야 한다.

Q. Table 접근성에서 중요한 것은?
A. thead, tbody, th, scope, caption, row action 이름, Empty State가 중요하다.

Q. layout을 위해 table을 써도 돼?
A. 안 된다. table은 표 데이터에 사용하고 layout은 Grid나 Flexbox를 사용한다.

Q. Feedback State에도 접근성이 필요해?
A. 필요하다. loading, error, success 상태는 보조기기 사용자에게도 전달되어야 한다.

Q. role status는 언제 써?
A. loading처럼 현재 상태를 부드럽게 알릴 때 사용할 수 있다.

Q. role alert는 언제 써?
A. 중요한 동적 오류 메시지를 즉시 알릴 때 사용할 수 있다.

Q. Design System Documentation이 뭐야?
A. Token, Component, Layout, Feedback, Accessibility, Review 기준을 Agent가 검색 가능하게 정리한 문서다.

Q. Documentation은 사람 공부용이야?
A. 아니다. RAG Retrieval과 Agent 생성 / 검토를 위한 기준 문서다.

Q. Documentation Structure가 왜 중요해?
A. 문서 구조가 일정해야 Agent가 필요한 기준을 안정적으로 검색할 수 있기 때문이다.

Q. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 유지해야 해?
A. 유지해야 한다. Master RAG Rules의 기본 검색 구조다.

Q. 예제는 길수록 좋아?
A. 아니다. RAG 문서에서는 짧고 직접적인 예제가 검색과 코드 생성에 유리하다.

Q. Documentation에서 가장 흔한 실수는?
A. 사람 설명 중심으로 길게 쓰고 FAQ, Retrieval Queries, Review Checklist를 부족하게 작성하는 것이다.

Q. Review Agent Final Checklist는 뭐야?
A. Token, Component, State, Layout, Responsive, Theme, Accessibility, Documentation을 통합 검토하는 기준이다.

Q. Review Agent가 가장 중요하게 봐야 하는 것은?
A. 사용자 흐름을 막는 문제, 접근성 심각 문제, 주요 상태 누락, 모바일 사용 불가 여부다.

Q. PM Agent는 무엇을 기준으로 완료 판단해?
A. 요구사항 충족, 사용자 흐름, 상태 처리, 모바일 사용성, 심각한 접근성 이슈 여부를 기준으로 판단한다.

Q. Frontend Agent는 최종 UI 생성 시 무엇을 확인해야 해?
A. Requirement, Layout, Core Component, Token, State, Responsive, Theme, Accessibility 기준을 함께 확인해야 한다.

Q. Part07의 역할은 뭐야?
A. Accessibility, Documentation, Final Review 기준을 정의하고 Part01~Part06을 통합 검토하는 문서다.
