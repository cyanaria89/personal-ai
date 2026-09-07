# Frontend Accessibility Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Frontend Accessibility Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- 접근성 있는 Frontend UI 작성 기준 제공
- Semantic HTML 사용 기준 제공
- 키보드 접근성 기준 제공
- 스크린 리더 대응 기준 제공
- Form 접근성 기준 제공
- Modal / Dialog / Dropdown / Tab 접근성 기준 제공
- Error / Loading / Empty State 접근성 기준 제공
- ARIA 속성 사용 기준 제공
- 색상 대비 / Focus / 대체 텍스트 기준 제공
- React Component 접근성 검토 기준 제공
- UI Component Pattern과 Testing 문서의 접근성 기준 연결
- 사용자 경험과 접근성 품질을 함께 개선

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

2026 실무 기준에서 Frontend Accessibility 문서는 단순히 `aria-label`을 붙이는 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 의미에 맞는 HTML 태그 선택
- `div onClick` 남용 방지
- Button / Link 역할 구분
- Form label 연결
- Error Message와 input 연결
- Modal focus 관리 기준 검토
- Dropdown / Tab 키보드 조작 기준 검토
- Loading / Error 상태를 보조기술에 전달
- 이미지 alt 기준 판단
- 색상만으로 상태를 전달하지 않도록 검토
- Focus outline 제거 방지
- React Component 접근성 리뷰
- Testing Library query 실패를 접근성 관점에서 분석

---

### [FAQ]

Q. Frontend Accessibility 문서는 UI Component Pattern과 뭐가 달라?

A.
UI Component Pattern은 Component 설계 기준이고 Frontend Accessibility는 사용자가 키보드, 스크린 리더 등 다양한 방식으로 UI를 사용할 수 있게 하는 기준이다.

Q. 접근성은 디자인 다 끝난 뒤에 추가하면 돼?

A.
권장하지 않는다. Semantic HTML, label, focus, keyboard 흐름은 Component 설계 단계부터 포함하는 것이 좋다.

Q. aria만 잘 붙이면 접근성이 해결돼?

A.
아니다. 먼저 의미에 맞는 HTML을 사용하고, 부족한 경우에만 ARIA를 보완적으로 사용하는 것이 원칙이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Accessibility 문서는 React Frontend 접근성 구현과 검토에 필요한 범위를 포함한다.

포함 범위:

- Semantic HTML
- Landmark
- Heading Structure
- Button Accessibility
- Link Accessibility
- Form Accessibility
- Label
- Accessible Name
- aria-label
- aria-labelledby
- aria-describedby
- aria-invalid
- aria-expanded
- aria-selected
- aria-current
- role
- Keyboard Navigation
- Focus Management
- Focus Visible
- Skip Link Basics
- Image Alt Text
- Icon Button Accessibility
- Color Contrast Basics
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

### [핵심]

반드시 포함:

- 가능한 경우 ARIA보다 Semantic HTML 우선
- 클릭 액션은 button 사용
- 페이지 이동은 link 사용
- 모든 input은 label과 연결
- error message는 input과 연결
- icon only button은 accessible name 필요
- keyboard만으로 주요 기능 사용 가능해야 함
- focus outline 제거 금지
- modal은 focus 관리 필요
- 색상만으로 상태 전달 금지
- 이미지 alt는 이미지 목적에 따라 결정
- loading / error 상태도 보조기술에 전달
- 접근성은 테스트와 연결됨

---

### [실무]

Frontend Accessibility는 모든 Frontend 문서와 연결된다.

실무 연결:

```text
HTML / CSS Foundation
→ React Core
→ UI Component Pattern
→ Form Handling
→ Error Handling & Loading UX
→ Frontend Testing
→ Frontend Accessibility Review
```

---

### [FAQ]

Q. 접근성은 별도 기능이야?

A.
아니다. 접근성은 HTML 구조, Component 설계, Form 처리, Error UX, Testing 전체에 포함되는 품질 기준이다.

Q. 화면상으로 잘 보이면 접근성도 괜찮은 거야?

A.
아니다. 키보드 조작, 스크린 리더 이름, focus 흐름, label 연결 등을 함께 확인해야 한다.

Q. 접근성 심화 표준 문서도 여기서 다뤄?

A.
기초 실무 기준은 포함하지만 WCAG 세부 조항 전체나 법적 감사 수준의 심화는 별도 문서가 적합하다.

---

## 2.2 Excluded Scope

### [개념]

Frontend Accessibility 문서에서는 법률 수준의 접근성 감사와 고급 보조기술 검증을 제외한다.

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

### [핵심]

제외 이유:

- Foundation 범위 초과
- Agent Retrieval 혼선 방지
- Frontend 실무 기본 접근성 기준에 집중
- UI Component / Form / Testing 문서와 연결되는 수준으로 유지

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

```text
Frontend Accessibility
→ Advanced Accessibility
→ Accessibility Audit
→ Design System Accessibility
→ Accessibility Testing Pipeline
```

---

### [FAQ]

Q. WCAG 전체를 외워야 해?

A.
실무 기본 단계에서는 Semantic HTML, keyboard, label, focus, color contrast, error message 같은 핵심 기준부터 적용하는 것이 좋다.

Q. 스크린 리더별 상세 테스트도 여기서 다뤄?

A.
아니다. 이 문서는 기본 구현과 검토 기준 중심이다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Frontend Accessibility RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 접근성 적용 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 접근성 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자가 자주 묻는 “왜 label 필요해?”, “div onClick 써도 돼?” 같은 질문과 매칭된다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Frontend Accessibility 문서에는 검토와 디버깅을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- Semantic HTML 설명 → [Comparison], [예제]
- Keyboard 접근성 → [Checklist], [Troubleshooting]
- Form 접근성 → [예제], [주의]
- Modal 접근성 → [Flow], [주의]
- ARIA 설명 → [Best Practice], [주의]
- 접근성 테스트 → [Checklist], [Troubleshooting]

---

### [실무]

예시:

```md
### [Checklist]

- [ ] button 역할에 button 태그를 사용했는가?
- [ ] input과 label이 연결되었는가?
- [ ] keyboard만으로 조작 가능한가?
- [ ] focus가 보이는가?
- [ ] error message가 input과 연결되었는가?
```

---

### [FAQ]

Q. Accessibility 문서에 Checklist가 중요한 이유는?

A.
접근성은 누락을 찾는 작업이 많기 때문에 체크리스트 기반 검토가 효과적이다.

Q. Accessibility 문서에 Troubleshooting이 필요한 이유는?

A.
getByRole 실패, focus 이동 오류, label 누락, keyboard 조작 불가 같은 문제가 자주 발생하기 때문이다.

---

# 4. Semantic HTML Rules

## 4.1 Semantic HTML First

### [개념]

Semantic HTML은 HTML 요소를 의미에 맞게 사용하는 방식이다.

접근성의 기본은 ARIA를 많이 쓰는 것이 아니라 올바른 HTML 태그를 먼저 사용하는 것이다.

---

### [핵심]

우선 사용:

- button
- a
- input
- label
- form
- fieldset
- legend
- header
- nav
- main
- section
- article
- aside
- footer
- ul / ol / li
- table / thead / tbody / th / td

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

권장:

- 클릭 액션은 `button`
- 페이지 이동은 `a` 또는 `Link`
- Form 입력은 `input`, `select`, `textarea`
- 목록은 `ul`, `ol`, `li`
- 표 데이터는 `table`
- 페이지 주요 영역은 `main`
- 네비게이션은 `nav`

---

### [FAQ]

Q. div에 onClick을 붙이면 안 돼?

A.
가능은 하지만 키보드 접근성과 의미가 부족하다. 클릭 액션은 button을 사용하는 것이 좋다.

Q. ARIA를 붙이면 div도 button처럼 되는 거 아니야?

A.
일부 보완은 가능하지만 keyboard 동작과 기본 의미를 직접 구현해야 한다. 가능하면 button을 쓰는 것이 더 안전하다.

---

## 4.2 Button vs Link

### [개념]

Button과 Link는 역할이 다르다.

Button은 현재 화면에서 액션을 실행하고, Link는 다른 위치로 이동한다.

---

### [핵심]

비교:

| 구분         | Button                | Link               |
| ------------ | --------------------- | ------------------ |
| 목적         | 액션 실행             | 페이지 / 위치 이동 |
| 예           | 저장, 삭제, 모달 열기 | 상세 페이지 이동   |
| 키보드       | Enter / Space         | Enter              |
| HTML         | button                | a / Link           |
| React Router | 액션에는 button       | 이동에는 Link      |

---

### [실무]

Button 예:

```jsx
<button type="button" onClick={onDelete}>
  삭제
</button>
```

Link 예:

```jsx
<Link to={`/festivals/${festivalId}`}>상세 보기</Link>
```

주의:

- 이동을 button + navigate로 처리할 수도 있지만 단순 이동은 Link가 의미상 적합
- 액션을 a 태그로 처리하지 않음
- form 내부 button은 type 명시
- icon button은 aria-label 제공

---

### [FAQ]

Q. 상세 페이지 이동 버튼은 button이야 Link야?

A.
단순 페이지 이동이라면 Link가 적합하다.

Q. 삭제는 Link로 만들어도 돼?

A.
권장하지 않는다. 삭제는 현재 상태를 변경하는 액션이므로 button이 적합하다.

---

## 4.3 Landmark Rules

### [개념]

Landmark는 페이지의 주요 영역을 의미 있는 구조로 나누는 HTML 요소 또는 role이다.

스크린 리더 사용자가 페이지 구조를 빠르게 탐색하는 데 도움을 준다.

---

### [핵심]

주요 Landmark:

- header
- nav
- main
- aside
- footer
- form
- search
- banner
- contentinfo

---

### [실무]

예:

```jsx
function AppLayout() {
  return (
    <>
      <header>
        <nav aria-label="주요 메뉴">...</nav>
      </header>

      <main>...</main>

      <footer>...</footer>
    </>
  );
}
```

권장:

- 페이지 주요 콘텐츠는 main 안에 배치
- main은 페이지에 하나를 기본으로 함
- nav가 여러 개면 aria-label로 구분
- header / footer를 의미 있게 사용
- 불필요한 role 중복 지양

---

### [FAQ]

Q. main 태그는 꼭 필요해?

A.
페이지 주요 콘텐츠를 나타내기 위해 사용하는 것이 좋다.

Q. nav가 여러 개면 어떻게 해?

A.
`aria-label`로 “주요 메뉴”, “하단 메뉴”처럼 구분하는 것이 좋다.

---

## 4.4 Heading Structure Rules

### [개념]

Heading Structure는 h1 ~ h6을 사용해 페이지 콘텐츠 계층을 표현하는 기준이다.

시각적 크기가 아니라 문서 구조를 기준으로 사용한다.

---

### [핵심]

기준:

- h1은 페이지 핵심 제목
- h2는 주요 Section
- h3는 h2 내부 하위 Section
- heading level skip 주의
- 스타일 목적 heading 사용 금지
- card title heading 기준 검토

---

### [실무]

좋은 구조:

```html
<h1>축제 목록</h1>

<section>
  <h2>인기 축제</h2>
  <article>
    <h3>봄꽃 축제</h3>
  </article>
</section>
```

주의:

- 글자 크기 때문에 h3부터 시작하지 않음
- heading 순서를 과도하게 건너뛰지 않음
- 카드 목록에서 각 카드 제목을 heading으로 둘지 기준 통일
- Modal title도 heading 역할 가능

---

### [FAQ]

Q. h1은 여러 개 있어도 돼?

A.
HTML상 가능하지만 일반적인 앱 페이지에서는 페이지 핵심 제목 하나를 h1로 두는 방식이 명확하다.

Q. 글자 크기를 줄이려고 h4를 써도 돼?

A.
권장하지 않는다. heading은 문서 구조 기준이고 크기는 CSS로 조정한다.

---

# 5. Form Accessibility Rules

## 5.1 Label Rules

### [개념]

Label은 input이 어떤 값을 입력받는지 설명하는 요소다.

모든 주요 Form Control은 label과 연결되어야 한다.

---

### [핵심]

연결 방식:

- `label htmlFor`
- `input id`
- wrapping label
- `aria-label`
- `aria-labelledby`

우선순위:

1. 보이는 label
2. label wrapping
3. aria-labelledby
4. aria-label

---

### [실무]

좋은 예:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

보이는 label이 어려운 icon input:

```jsx
<input type="search" aria-label="축제 검색어" />
```

주의:

- placeholder는 label 대체가 아님
- label과 id가 일치해야 함
- id 중복 금지
- 검색 input도 label 또는 aria-label 필요
- checkbox / radio도 label 연결 필요

---

### [FAQ]

Q. placeholder가 있으면 label은 없어도 돼?

A.
권장하지 않는다. placeholder는 입력 중 사라지고 스크린 리더 label을 안정적으로 대체하지 못한다.

Q. 디자인상 label을 보이기 어렵다면?

A.
시각적으로 숨긴 label을 제공하거나 aria-label / aria-labelledby를 사용할 수 있다.

---

## 5.2 Error Message Accessibility

### [개념]

Error Message Accessibility는 Form 오류가 발생했을 때 사용자가 어떤 필드를 어떻게 수정해야 하는지 이해할 수 있게 하는 기준이다.

---

### [핵심]

사용 속성:

- aria-invalid
- aria-describedby
- role alert
- error id
- field error
- global error
- focus management

---

### [실무]

예:

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
    {error}
  </p>
)}
```

권장:

- field error는 input 근처에 표시
- error message와 input을 aria-describedby로 연결
- 오류 상태는 aria-invalid로 표현
- submit 실패 시 첫 오류 field focus 이동 고려
- 색상만으로 오류 표시 금지
- 문구는 수정 방법을 알려주는 형태

---

### [FAQ]

Q. 에러 메시지는 input과 꼭 연결해야 해?

A.
권장한다. 스크린 리더 사용자가 어떤 입력값에 문제가 있는지 이해하기 쉽다.

Q. 빨간색 테두리만 표시하면 충분해?

A.
아니다. 색상만으로 오류를 전달하면 색각 이상 사용자나 스크린 리더 사용자가 오류를 인식하기 어렵다.

---

## 5.3 Required Field Rules

### [개념]

Required Field는 필수 입력 항목임을 사용자에게 명확히 알려야 한다.

시각적 표시와 보조기술 전달을 함께 고려한다.

---

### [핵심]

표현 방식:

- required attribute
- aria-required
- visible required text
- asterisk explanation
- validation message

---

### [실무]

예:

```jsx
<label htmlFor="nickname">
  닉네임 <span aria-hidden="true">*</span>
</label>
<input
  id="nickname"
  name="nickname"
  required
/>
<p>* 표시는 필수 입력 항목입니다.</p>
```

주의:

- 별표만 있고 설명이 없으면 의미가 불명확할 수 있음
- required attribute는 브라우저 기본 검증을 발생시킬 수 있음
- custom validation과 native validation 기준 통일
- 필수값 오류 메시지를 제공

---

### [FAQ]

Q. 필수값 표시로 별표만 붙이면 돼?

A.
별표의 의미를 설명하거나 “필수” 텍스트를 함께 제공하는 것이 좋다.

Q. required와 aria-required를 둘 다 써야 해?

A.
일반 input에서는 required가 우선이다. custom widget에서는 aria-required를 고려할 수 있다.

---

## 5.4 Fieldset and Legend Rules

### [개념]

fieldset과 legend는 관련된 Form Control 그룹을 묶고 그룹의 의미를 설명하는 요소다.

Radio Group, Checkbox Group에 특히 유용하다.

---

### [핵심]

사용 대상:

- radio group
- checkbox group
- address group
- date range group
- payment method group
- agreement group

---

### [실무]

예:

```jsx
<fieldset>
  <legend>알림 수신 방법</legend>

  <label>
    <input type="checkbox" name="notification" value="email" />
    이메일
  </label>

  <label>
    <input type="checkbox" name="notification" value="sms" />
    문자
  </label>
</fieldset>
```

권장:

- 여러 선택지가 하나의 질문에 속하면 fieldset 사용
- legend는 그룹 질문을 설명
- radio는 같은 name 사용
- 그룹 error message 연결 기준 고려

---

### [FAQ]

Q. radio group에는 fieldset이 꼭 필요해?

A.
권장한다. 여러 선택지가 하나의 질문에 속한다는 구조를 명확히 전달할 수 있다.

Q. legend는 label이랑 달라?

A.
label은 개별 input 설명이고 legend는 fieldset 그룹 전체 설명이다.

---

# 6. Keyboard Accessibility Rules

## 6.1 Keyboard Navigation

### [개념]

Keyboard Navigation은 마우스 없이 Tab, Shift+Tab, Enter, Space, Arrow Key 등으로 UI를 사용할 수 있게 하는 기준이다.

---

### [핵심]

검토 대상:

- Tab order
- Shift+Tab order
- Enter action
- Space action
- Escape close
- Arrow key navigation
- Focus visible
- Skip link
- Focus trap basics

---

### [실무]

기본 체크:

```text
마우스 없이 Tab만 사용
→ 주요 버튼 이동 가능
→ 입력 가능
→ 선택 가능
→ 제출 가능
→ Modal 닫기 가능
→ 현재 focus 위치가 보임
```

권장:

- native button / input / select 사용
- custom dropdown / tab은 keyboard 구현 필요
- focus 가능한 요소 순서가 시각 순서와 자연스러워야 함
- disabled 요소는 focus 대상에서 제외
- hidden 요소에 focus 가지 않게 함

---

### [FAQ]

Q. 마우스로 잘 되면 키보드도 되는 거 아니야?

A.
아니다. div onClick, custom dropdown, modal 등은 키보드 조작이 누락될 수 있다.

Q. 키보드 접근성은 뭘 먼저 확인해?

A.
Tab 이동, Enter / Space 실행, Escape 닫기, focus visible 여부부터 확인한다.

---

## 6.2 Focus Visible Rules

### [개념]

Focus Visible은 현재 키보드 초점이 어디에 있는지 사용자가 볼 수 있게 하는 기준이다.

---

### [핵심]

기준:

- focus outline 유지
- custom focus style 제공
- keyboard focus 구분
- focus indicator contrast
- focus not hidden
- no outline none without replacement

---

### [실무]

나쁜 예:

```css
button:focus {
  outline: none;
}
```

개선 예:

```css
button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

권장:

- 기본 outline을 무작정 제거하지 않음
- 디자인에 맞는 focus-visible style 제공
- 색상 대비 확인
- focus style이 잘리지 않도록 overflow 확인
- 모든 interactive element에 focus 확인

---

### [FAQ]

Q. focus outline을 없애면 디자인이 깔끔해지는데 괜찮아?

A.
권장하지 않는다. 키보드 사용자가 현재 위치를 알 수 없게 된다. 대신 디자인에 맞는 focus style을 제공한다.

Q. focus와 hover는 같은 거야?

A.
다르다. hover는 마우스 상태이고 focus는 키보드나 프로그램적 초점 상태다.

---

## 6.3 Tab Order Rules

### [개념]

Tab Order는 키보드 Tab 이동 순서다.

자연스러운 DOM 순서와 시각적 흐름이 일치해야 한다.

---

### [핵심]

기준:

- DOM order
- visual order
- interactive elements
- tabindex
- tabindex 0
- tabindex -1
- avoid positive tabindex
- hidden element focus prevention

---

### [실무]

권장:

- DOM 순서를 자연스럽게 작성
- positive tabindex 사용 지양
- focus가 필요 없는 div에 tabindex 남발 금지
- modal 내부 focus 관리 필요
- 숨겨진 dropdown item에 focus 가지 않게 처리
- route 이동 후 focus 위치 고려

주의:

```text
tabindex="1", tabindex="2" 같은 양수 tabindex는
전체 focus 순서를 복잡하게 만들 수 있어 지양한다.
```

---

### [FAQ]

Q. tabindex를 많이 쓰면 키보드 순서를 쉽게 조정할 수 있지 않아?

A.
양수 tabindex는 유지보수를 어렵게 만들 수 있다. DOM 순서를 올바르게 설계하는 것이 우선이다.

Q. tabindex="-1"은 언제 써?

A.
사용자 Tab 순서에는 포함하지 않지만 코드로 focus를 이동해야 하는 요소에 사용할 수 있다.

---

# 7. ARIA Rules

## 7.1 ARIA Basics

### [개념]

ARIA는 HTML만으로 표현하기 어려운 역할, 상태, 관계를 보조기술에 전달하는 속성이다.

ARIA는 Semantic HTML을 대체하는 것이 아니라 보완하는 도구다.

---

### [핵심]

원칙:

- Semantic HTML 우선
- 필요한 경우에만 ARIA 사용
- 잘못된 ARIA는 없는 것보다 나쁠 수 있음
- role과 keyboard 동작이 일치해야 함
- aria 상태는 실제 UI 상태와 동기화
- accessible name 제공

---

### [실무]

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
aria-busy
```

주의:

- button 역할은 button 태그 우선
- role="button"을 쓰면 Enter / Space keyboard 처리 필요
- aria-expanded는 실제 open 상태와 일치
- aria-hidden 요소 안에 focus 가능한 요소가 있으면 문제 가능
- 불필요한 role 중복 지양

---

### [FAQ]

Q. ARIA를 많이 붙이면 접근성이 좋아져?

A.
아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다. 먼저 semantic HTML을 사용한다.

Q. role="button"을 쓰면 button처럼 동작해?

A.
스크린 리더 역할은 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다. 가능하면 button 태그를 사용한다.

---

## 7.2 Accessible Name Rules

### [개념]

Accessible Name은 스크린 리더와 Testing Library가 요소를 식별할 때 사용하는 이름이다.

Button, link, input 등 interactive element는 명확한 accessible name이 필요하다.

---

### [핵심]

Accessible Name 제공 방식:

- visible text
- label
- aria-label
- aria-labelledby
- alt text
- title fallback

---

### [실무]

좋은 예:

```jsx
<button type="button">검색</button>
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
<input id="keyword" />
```

주의:

- 아이콘만 있는 버튼은 이름이 없을 수 있음
- aria-label과 visible text가 충돌하지 않게 함
- 같은 이름의 버튼이 여러 개면 context 제공 고려
- “자세히 보기” 링크가 반복되면 구분 필요

---

### [FAQ]

Q. getByRole에서 name이 안 잡히는 이유는?

A.
요소에 accessible name이 없거나 기대한 이름과 실제 이름이 다를 수 있다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?

A.
시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

---

## 7.3 aria-live Rules

### [개념]

aria-live는 화면이 동적으로 변경될 때 보조기술에 변경 내용을 알려주는 속성이다.

Loading, Error, Success Message, Toast 등에 사용할 수 있다.

---

### [핵심]

값:

- polite
- assertive
- off

사용 대상:

- loading message
- success message
- error message
- toast
- validation summary
- background update notice

---

### [실무]

예:

```jsx
<div role="status" aria-live="polite">
  저장 중입니다.
</div>
```

Error 예:

```jsx
<div role="alert">저장에 실패했습니다.</div>
```

권장:

- 일반 상태 변경은 polite
- 즉시 알려야 하는 오류는 alert 사용 가능
- 너무 많은 live region은 사용자에게 방해
- 반복 업데이트 메시지 주의
- 화면에 보이는 메시지와 함께 제공

---

### [FAQ]

Q. role="alert"와 aria-live는 뭐가 달라?

A.
role="alert"는 중요한 오류나 긴급 메시지를 즉시 알리는 데 사용되고, aria-live="polite"는 덜 긴급한 변경을 자연스럽게 알린다.

Q. Toast에도 aria-live가 필요해?

A.
Toast가 중요한 상태 메시지를 전달한다면 보조기술 사용자가 인식할 수 있게 live region을 고려한다.

---

# 8. Image and Icon Accessibility Rules

## 8.1 Image Alt Text Rules

### [개념]

alt text는 이미지가 전달하는 의미를 텍스트로 제공하는 속성이다.

이미지의 목적에 따라 alt 작성 방식이 달라진다.

---

### [핵심]

이미지 유형:

- informative image
- decorative image
- functional image
- complex image
- avatar
- thumbnail
- icon

---

### [실무]

정보 이미지:

```jsx
<img src="/festival.jpg" alt="봄꽃 축제 행사장 전경" />
```

장식 이미지:

```jsx
<img src="/decorator.png" alt="" />
```

링크 이미지:

```jsx
<Link to="/festivals/1">
  <img src="/festival.jpg" alt="봄꽃 축제 상세 보기" />
</Link>
```

권장:

- 이미지를 설명하기보다 이미지의 목적을 설명
- 장식 이미지는 empty alt 사용
- “이미지”, “사진” 같은 불필요한 단어 지양
- 같은 정보가 주변 텍스트에 있으면 중복 여부 검토
- 복잡한 차트는 별도 설명 필요

---

### [FAQ]

Q. 모든 이미지에 자세한 alt를 넣어야 해?

A.
아니다. 장식 이미지는 `alt=""`가 적합하고, 정보 이미지는 의미를 전달하는 alt가 필요하다.

Q. 축제 카드 이미지 alt는 어떻게 써?

A.
이미지가 정보 전달 역할이면 축제명이나 이미지 의미를 포함하고, 카드 제목과 완전히 중복이면 장식 처리도 검토할 수 있다.

---

## 8.2 Icon Accessibility Rules

### [개념]

Icon Accessibility는 아이콘이 장식인지, 의미 전달인지, 버튼 기능인지에 따라 다르게 처리하는 기준이다.

---

### [핵심]

구분:

- decorative icon
- informative icon
- icon button
- status icon
- loading icon

---

### [실무]

장식 아이콘:

```jsx
<SearchIcon aria-hidden="true" />
```

아이콘 버튼:

```jsx
<button type="button" aria-label="알림 열기">
  <BellIcon aria-hidden="true" />
</button>
```

상태 아이콘:

```jsx
<span aria-label="성공">
  <CheckIcon aria-hidden="true" />
</span>
```

권장:

- 텍스트와 함께 있는 장식 아이콘은 aria-hidden
- 아이콘만 있는 버튼은 aria-label 필수
- 색상 아이콘만으로 상태 전달 금지
- 로딩 아이콘은 텍스트 상태와 함께 제공

---

### [FAQ]

Q. 아이콘에 항상 aria-label을 붙여야 해?

A.
아니다. 장식 아이콘은 aria-hidden이 적합하고, 아이콘만으로 기능을 나타내는 버튼에는 aria-label이 필요하다.

Q. 체크 아이콘만 보여주면 성공 상태가 전달돼?

A.
색상이나 아이콘만으로는 부족할 수 있다. 텍스트나 accessible name을 함께 제공하는 것이 좋다.

---

# 9. Color and Visual Accessibility Rules

## 9.1 Color Contrast Rules

### [개념]

Color Contrast는 텍스트와 배경의 명도 차이가 충분해 읽기 쉬운지 판단하는 기준이다.

---

### [핵심]

검토 대상:

- body text
- button text
- link text
- disabled text
- placeholder
- error text
- focus outline
- badge text
- chart label

---

### [실무]

권장:

- 주요 텍스트는 배경과 충분한 대비 확보
- disabled text도 완전히 읽을 수 없게 만들지 않음
- placeholder를 중요한 정보 전달에 사용하지 않음
- error는 색상 외 텍스트 / 아이콘 제공
- focus indicator도 충분히 보여야 함
- 다크모드 / 라이트모드 모두 확인

주의:

```text
색상 대비는 디자인 감각만으로 판단하지 말고
도구를 사용해 확인하는 것이 좋다.
```

---

### [FAQ]

Q. 회색 글씨가 예쁘면 그냥 써도 돼?

A.
텍스트 대비가 낮으면 읽기 어려울 수 있다. 디자인보다 가독성과 접근성을 함께 고려해야 한다.

Q. 다크모드에서도 색상 대비를 따로 봐야 해?

A.
그렇다. 라이트모드에서 괜찮은 색상이 다크모드에서는 부족할 수 있다.

---

## 9.2 Color Only Meaning Rules

### [개념]

Color Only Meaning은 색상만으로 상태나 의미를 전달하는 문제를 말한다.

색상을 구분하기 어려운 사용자는 의미를 놓칠 수 있다.

---

### [핵심]

문제 예:

- 빨간색만으로 error 표시
- 초록색만으로 success 표시
- 색상만 다른 chart line
- 필수값을 색상만으로 표시
- 활성 tab을 색상만으로 표시

---

### [실무]

개선 기준:

```text
색상 + 텍스트
색상 + 아이콘
색상 + 패턴
색상 + aria 속성
색상 + 위치 / 형태
```

예:

```jsx
<p role="alert">오류: 이메일을 입력해 주세요.</p>
```

권장:

- 상태에는 텍스트를 함께 제공
- chart는 legend / label 제공
- active 상태는 aria-selected / aria-current 사용
- error는 aria-invalid와 message 연결
- success는 문구로도 표시

---

### [FAQ]

Q. 빨간색이면 에러라는 걸 알 수 있지 않아?

A.
모든 사용자가 색상을 동일하게 인식하지 않는다. 텍스트나 아이콘을 함께 제공해야 한다.

Q. 활성 메뉴를 색상만 다르게 해도 돼?

A.
권장하지 않는다. aria-current, 밑줄, 굵기, 텍스트 등 추가 단서를 제공하는 것이 좋다.

---

# 10. Component Accessibility Rules

## 10.1 Button Accessibility

### [개념]

Button Accessibility는 버튼이 키보드와 스크린 리더에서 명확히 인식되고 조작될 수 있게 하는 기준이다.

---

### [핵심]

기준:

- button tag
- type attribute
- accessible name
- disabled state
- loading state
- aria-label for icon button
- focus visible
- no div button

---

### [실무]

기본 버튼:

```jsx
<button type="button" onClick={onClick}>
  저장
</button>
```

로딩 버튼:

```jsx
<button type="submit" disabled={loading} aria-busy={loading}>
  {loading ? "저장 중..." : "저장"}
</button>
```

아이콘 버튼:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

주의:

- form 안 button은 type 명시
- disabled 버튼은 focus되지 않음
- loading 중 button text 제공
- aria-label이 visible text와 충돌하지 않게 함
- div button 지양

---

### [FAQ]

Q. Button에 type을 꼭 써야 해?

A.
form 안에서는 기본 submit 동작 때문에 type을 명시하는 것이 안전하다. 공통 Button은 type="button" 기본값이 좋다.

Q. 아이콘만 있는 닫기 버튼은 어떻게 해?

A.
`aria-label="닫기"`처럼 버튼의 목적을 제공해야 한다.

---

## 10.2 Link Accessibility

### [개념]

Link Accessibility는 링크가 이동 목적지를 명확히 설명하고 키보드와 스크린 리더에서 올바르게 인식되도록 하는 기준이다.

---

### [핵심]

기준:

- meaningful link text
- href / Link to
- no empty link
- external link notice
- aria-current
- avoid click here
- keyboard focus

---

### [실무]

좋은 예:

```jsx
<Link to="/festivals">축제 목록 보기</Link>
```

나쁜 예:

```jsx
<Link to="/festivals">여기를 클릭</Link>
```

현재 페이지 표시:

```jsx
<NavLink
  to="/calendar"
  aria-current={({ isActive }) => (isActive ? "page" : undefined)}
>
  캘린더
</NavLink>
```

권장:

- 링크 텍스트만 읽어도 목적지를 알 수 있게 함
- 현재 페이지는 aria-current 사용
- 새 창 열림은 사용자에게 안내 가능
- 링크처럼 보이지만 액션이면 button 사용

---

### [FAQ]

Q. “자세히 보기” 링크를 반복해서 써도 돼?

A.
가능하지만 스크린 리더에서는 목적지가 모호할 수 있다. “봄꽃 축제 자세히 보기”처럼 구체화하는 것이 좋다.

Q. 현재 메뉴는 어떻게 표시해?

A.
시각적 표시와 함께 `aria-current="page"`를 사용할 수 있다.

---

## 10.3 Modal / Dialog Accessibility

### [개념]

Modal / Dialog Accessibility는 Dialog가 열렸을 때 보조기술과 키보드 사용자가 현재 맥락을 이해하고 안전하게 닫을 수 있도록 하는 기준이다.

---

### [핵심]

필수 고려:

- role dialog
- aria-modal
- aria-labelledby
- aria-describedby
- focus move on open
- focus return on close
- Escape close
- close button
- backdrop click policy
- focus trap basics
- scroll lock basics

---

### [실무]

기본 구조:

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

권장:

- Modal 열릴 때 내부로 focus 이동
- 닫힐 때 trigger로 focus 복귀
- 닫기 버튼 제공
- Escape 닫기 기준 마련
- focus가 modal 밖으로 빠져나가지 않게 처리
- 중첩 modal 지양

주의:

- 접근성 있는 Modal 구현은 난도가 높음
- 복잡하면 검증된 라이브러리 사용 검토
- role과 aria만으로 focus 문제가 해결되지는 않음

---

### [FAQ]

Q. Modal에 role dialog만 붙이면 접근성이 끝이야?

A.
아니다. focus 이동, focus trap, 닫기 버튼, aria-labelledby 같은 요소도 필요하다.

Q. Modal 닫은 후 focus는 어디로 가야 해?

A.
일반적으로 Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

---

## 10.4 Dropdown Accessibility

### [개념]

Dropdown Accessibility는 메뉴나 선택지가 열리고 닫히는 상태를 보조기술과 키보드 사용자가 이해하고 조작할 수 있게 하는 기준이다.

---

### [핵심]

필수 고려:

- trigger button
- aria-expanded
- aria-haspopup
- menu role basics
- item role basics
- Escape close
- outside click
- arrow key basics
- focus management

---

### [실무]

기본 구조:

```jsx
<button
  type="button"
  aria-haspopup="menu"
  aria-expanded={open}
  onClick={toggleOpen}
>
  메뉴
</button>;

{
  open && (
    <ul role="menu">
      <li>
        <button type="button" role="menuitem">
          수정
        </button>
      </li>
    </ul>
  );
}
```

권장:

- trigger는 button 사용
- 열림 상태와 aria-expanded 동기화
- Escape로 닫기 고려
- 메뉴 item은 keyboard로 접근 가능해야 함
- 선택 후 닫기 기준 통일
- 복잡한 menu는 검증된 headless library 검토 가능

---

### [FAQ]

Q. Dropdown은 div로 만들어도 돼?

A.
시각적으로 가능하지만 keyboard, aria-expanded, focus 관리가 누락되기 쉽다. trigger는 button을 사용하는 것이 좋다.

Q. aria-expanded는 언제 바뀌어야 해?

A.
실제 dropdown open 상태와 항상 일치해야 한다.

---

## 10.5 Tab Accessibility

### [개념]

Tab Accessibility는 여러 패널을 탭으로 전환할 때 현재 선택된 탭과 연결된 패널을 보조기술에 전달하는 기준이다.

---

### [핵심]

필수 고려:

- role tablist
- role tab
- role tabpanel
- aria-selected
- aria-controls
- id relation
- keyboard arrow navigation basics
- selected state

---

### [실무]

기본 구조:

```jsx
<div role="tablist" aria-label="축제 상세 정보">
  <button
    type="button"
    role="tab"
    id="tab-info"
    aria-selected={selectedTab === "info"}
    aria-controls="panel-info"
    onClick={() => setSelectedTab("info")}
  >
    정보
  </button>

  <button
    type="button"
    role="tab"
    id="tab-review"
    aria-selected={selectedTab === "review"}
    aria-controls="panel-review"
    onClick={() => setSelectedTab("review")}
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
```

권장:

- 선택 상태를 aria-selected로 표현
- tab과 tabpanel 연결
- keyboard arrow navigation 고려
- 페이지 이동 수준이면 tab보다 route 사용
- hidden panel의 focus 처리 주의

---

### [FAQ]

Q. Tab은 button 여러 개만 있으면 돼?

A.
기본 전환은 가능하지만 접근성을 위해 role, aria-selected, tabpanel 연결을 고려해야 한다.

Q. Tab과 Route는 어떻게 구분해?

A.
같은 페이지 안의 패널 전환이면 Tab, 페이지 수준 이동이면 Route가 적합하다.

---

# 11. State Accessibility Rules

## 11.1 Loading Accessibility

### [개념]

Loading Accessibility는 사용자가 데이터 요청이나 작업 처리 중임을 보조기술로도 인식할 수 있게 하는 기준이다.

---

### [핵심]

사용 속성:

- role status
- aria-live polite
- aria-busy
- loading text
- spinner aria-hidden
- skeleton aria-hidden

---

### [실무]

예:

```jsx
<section aria-busy={loading}>
  {loading && (
    <div role="status" aria-live="polite">
      데이터를 불러오는 중입니다.
    </div>
  )}
</section>
```

Spinner 예:

```jsx
<div role="status">
  <span className="spinner" aria-hidden="true" />
  <span>처리 중입니다.</span>
</div>
```

권장:

- spinner만 단독으로 제공하지 않음
- loading text 제공
- skeleton 장식 요소는 aria-hidden 고려
- 너무 잦은 live message는 피함
- submit button은 loading text로 상태 변경

---

### [FAQ]

Q. Spinner만 보이면 충분해?

A.
아니다. 스크린 리더 사용자를 위해 loading 상태를 설명하는 텍스트나 role status가 필요하다.

Q. Skeleton은 스크린 리더가 읽어야 해?

A.
대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

---

## 11.2 Error State Accessibility

### [개념]

Error State Accessibility는 오류 상황을 사용자가 명확히 인식하고 다음 행동을 할 수 있게 하는 기준이다.

---

### [핵심]

기준:

- role alert
- clear message
- retry button
- focus movement
- field error connection
- no color only
- no internal error exposure

---

### [실무]

Page Error 예:

```jsx
<section role="alert">
  <h2>축제 정보를 불러오지 못했습니다.</h2>
  <p>잠시 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Form Error 예:

```jsx
<p id="password-error" role="alert">
  비밀번호를 입력해 주세요.
</p>
```

권장:

- 오류 메시지는 명확하고 수정 가능하게 작성
- 재시도 가능한 경우 retry button 제공
- field error는 input과 연결
- global error는 form 상단에 표시
- stack trace 노출 금지

---

### [FAQ]

Q. Error Message에 role alert를 붙이면 돼?

A.
중요한 오류에는 도움이 된다. 다만 모든 작은 변화에 alert를 남발하면 사용자를 방해할 수 있다.

Q. Error State에는 focus를 이동해야 해?

A.
상황에 따라 필요하다. 페이지 전체 오류나 form submit 실패 시 사용자가 오류를 빠르게 인식하도록 focus 이동을 고려한다.

---

## 11.3 Empty State Accessibility

### [개념]

Empty State Accessibility는 데이터가 없는 상태도 명확한 메시지와 다음 행동으로 전달하는 기준이다.

---

### [핵심]

구성:

- clear title
- description
- next action
- semantic section
- action button / link
- no blank screen

---

### [실무]

예:

```jsx
<section>
  <h2>검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onReset}>
    필터 초기화
  </button>
</section>
```

권장:

- 빈 화면 방치 금지
- 제목과 설명 제공
- 다음 행동 제공
- error state와 구분
- 첫 사용 empty와 검색 결과 없음 구분

---

### [FAQ]

Q. 데이터가 없으면 그냥 빈 배열 렌더링하면 안 돼?

A.
권장하지 않는다. 사용자가 정상 상태인지 오류인지 알 수 있도록 Empty State를 제공하는 것이 좋다.

Q. Empty State도 접근성 이슈가 있어?

A.
있다. 메시지가 없으면 보조기술 사용자도 현재 상태를 이해하기 어렵다.

---

# 12. Table and List Accessibility Rules

## 12.1 List Accessibility

### [개념]

List Accessibility는 반복되는 항목을 의미 있는 목록 구조로 제공하는 기준이다.

---

### [핵심]

사용 요소:

- ul
- ol
- li
- article
- heading
- list item action
- unique key
- empty state

---

### [실무]

예:

```jsx
<ul>
  {festivals.map((festival) => (
    <li key={festival.festivalId}>
      <article>
        <h3>{festival.title}</h3>
        <p>{festival.regionName}</p>
      </article>
    </li>
  ))}
</ul>
```

권장:

- 반복 항목은 list 구조 검토
- 카드 내부 제목 구조 명확화
- 각 항목의 액션 이름 구체화
- “자세히 보기” 반복 링크는 대상 구분
- 빈 목록은 Empty State 제공

---

### [FAQ]

Q. 카드 목록은 ul/li로 감싸야 해?

A.
반복되는 항목 목록이라면 ul/li를 사용하는 것이 의미상 좋다.

Q. 자세히 보기 링크가 여러 개면 문제야?

A.
스크린 리더 사용자는 링크만 모아 들을 수 있어 대상이 모호할 수 있다. 축제명을 포함하는 등 구체화하는 것이 좋다.

---

## 12.2 Table Accessibility

### [개념]

Table Accessibility는 행과 열 관계가 있는 데이터를 table 구조로 명확히 전달하는 기준이다.

---

### [핵심]

필수 요소:

- table
- caption
- thead
- tbody
- th
- td
- scope
- row header
- sortable header basics

---

### [실무]

예:

```jsx
<table>
  <caption>사용자 목록</caption>
  <thead>
    <tr>
      <th scope="col">닉네임</th>
      <th scope="col">권한</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>jun</td>
      <td>ROLE_USER</td>
    </tr>
  </tbody>
</table>
```

권장:

- 표 데이터는 table 사용
- caption 제공 고려
- th와 scope 사용
- 정렬 가능한 열은 정렬 상태 제공
- layout 목적 table 사용 지양
- 모바일에서 의미를 잃지 않게 설계

---

### [FAQ]

Q. 표를 div로 만들어도 돼?

A.
행과 열 관계가 중요한 데이터는 table 요소를 사용하는 것이 접근성에 좋다.

Q. caption은 꼭 필요해?

A.
복잡한 표일수록 caption이 표의 목적을 이해하는 데 도움이 된다.

---

# 13. React Accessibility Rules

## 13.1 Conditional Rendering Accessibility

### [개념]

React Conditional Rendering은 조건에 따라 UI가 나타나거나 사라진다.

접근성에서는 focus, live region, hidden 상태, keyboard 흐름을 함께 고려해야 한다.

---

### [핵심]

주의 상황:

- modal open / close
- dropdown open / close
- error message show / hide
- loading show / hide
- tab panel switch
- route transition
- toast show / hide

---

### [실무]

권장:

- UI가 나타날 때 focus가 필요한지 검토
- 사라지는 요소에 focus가 남지 않게 처리
- error message는 role alert 또는 aria-describedby 연결
- hidden 콘텐츠가 keyboard focus 대상이 되지 않게 함
- aria-expanded와 실제 open 상태 동기화
- loading / success message는 live region 고려

---

### [FAQ]

Q. 조건부 렌더링이면 접근성에서 뭘 조심해야 해?

A.
focus가 사라진 요소에 남지 않는지, open 상태가 aria와 동기화되는지, 동적 메시지가 전달되는지 확인해야 한다.

Q. display none과 hidden은 접근성에 영향이 있어?

A.
숨겨진 콘텐츠는 보조기술과 키보드 접근에서 제외될 수 있다. 의도에 맞게 사용해야 한다.

---

## 13.2 Custom Component Accessibility

### [개념]

Custom Component Accessibility는 직접 만든 Button, Modal, Dropdown, Tab 같은 Component가 native element의 접근성 동작을 잃지 않도록 하는 기준이다.

---

### [핵심]

검토 대상:

- custom button
- custom select
- custom checkbox
- custom radio
- custom dropdown
- custom modal
- custom tab
- custom tooltip

---

### [실무]

기준:

```text
Native 요소로 가능한가?
→ 가능하면 native 사용
→ 불가능하면 role / keyboard / focus / aria 상태 구현
→ 테스트로 검증
```

주의:

- Custom Select는 구현 난도가 높음
- Custom Checkbox는 checked 상태 전달 필요
- Custom Dropdown은 keyboard와 focus 관리 필요
- Custom Tooltip은 hover뿐 아니라 focus도 고려
- 복잡하면 검증된 접근성 라이브러리 사용 검토

---

### [FAQ]

Q. 디자인 때문에 select를 직접 만들면 안 돼?

A.
가능하지만 keyboard, role, aria, focus 관리가 필요해 구현 난도가 높다. 기본 select나 접근성 검증된 라이브러리를 검토한다.

Q. Custom Component는 어떻게 검증해?

A.
keyboard 조작, screen reader 이름, role, focus 이동, Testing Library getByRole query 등을 확인한다.

---

# 14. Accessibility Testing Rules

## 14.1 Manual Accessibility Check

### [개념]

Manual Accessibility Check는 도구만으로 잡기 어려운 접근성 문제를 사람이 직접 확인하는 절차다.

---

### [핵심]

체크 대상:

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

---

### [실무]

기본 점검 Flow:

```text
마우스 없이 Tab으로 이동
→ 주요 액션 실행
→ Form 입력 / 제출
→ 오류 확인
→ Modal 열고 닫기
→ Dropdown / Tab 조작
→ Focus 위치 확인
```

권장:

- 중요한 사용자 흐름부터 점검
- Login / Signup / Search / Payment / Form 우선
- Modal / Dropdown / Tab은 별도 점검
- 키보드 조작이 막히는 지점 확인
- 화면 확대와 반응형도 함께 확인 가능

---

### [FAQ]

Q. 자동화 도구만 돌리면 접근성 테스트 끝이야?

A.
아니다. keyboard 조작, focus 흐름, 실제 사용자 경험은 수동 확인이 필요하다.

Q. 접근성 수동 점검은 어디부터 해?

A.
로그인, 회원가입, 검색, 결제, 주요 Form, Modal 같은 핵심 흐름부터 확인한다.

---

## 14.2 Testing Library Accessibility Query

### [개념]

Testing Library의 getByRole, getByLabelText 같은 query는 접근성 구조를 기반으로 요소를 찾는다.

접근성 좋은 UI는 테스트도 쉬워진다.

---

### [핵심]

우선 query:

- getByRole
- getByLabelText
- getByText
- getByAltText
- getByPlaceholderText
- getByTestId last resort

---

### [실무]

예:

```tsx
screen.getByRole("button", { name: "저장" });
screen.getByLabelText("이메일");
screen.getByRole("dialog", { name: "리뷰 삭제" });
screen.getByRole("alert");
```

권장:

- getByRole 우선
- getByLabelText로 Form label 검증
- icon button은 name으로 찾을 수 있어야 함
- dialog는 accessible name 필요
- testId는 최후 수단

---

### [FAQ]

Q. getByRole이 실패하면 접근성 문제야?

A.
가능성이 있다. semantic element, role, accessible name이 올바른지 확인해야 한다.

Q. getByLabelText가 실패하면?

A.
input과 label이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

---

## 14.3 axe Basics

### [개념]

axe 같은 접근성 자동화 도구는 일부 접근성 위반을 자동으로 탐지할 수 있다.

하지만 모든 문제를 잡지는 못한다.

---

### [핵심]

탐지 가능 예:

- label 누락
- aria 속성 오류
- role 불일치
- color contrast 일부
- heading 구조 일부
- landmark 일부
- alt 누락

한계:

- keyboard 흐름 전체
- 실제 스크린 리더 경험
- 문구 품질
- focus 이동 의도
- 사용자 맥락

---

### [실무]

권장:

- Form / Modal / Navigation / 공통 UI에 우선 적용
- 자동화 결과를 무조건 정답으로만 보지 않음
- 수동 점검과 함께 사용
- CI 연동은 별도 문서에서 심화
- 오류 메시지를 읽고 실제 UI 구조 개선

---

### [FAQ]

Q. axe 테스트 통과하면 접근성 문제 없는 거야?

A.
아니다. 자동화 도구가 잡지 못하는 keyboard, focus, 사용자 맥락 문제가 남을 수 있다.

Q. axe는 어디에 우선 적용해?

A.
Form, Modal, Navigation, 공통 UI Component처럼 접근성 영향이 큰 곳에 우선 적용한다.

---

# 15. Troubleshooting Rules

## 15.1 getByRole Failed Troubleshooting

### [개념]

getByRole 실패는 요소의 semantic role이나 accessible name이 기대와 다를 때 발생한다.

테스트 실패인 동시에 접근성 문제일 수 있다.

---

### [핵심]

원인:

- semantic element 아님
- div onClick 사용
- accessible name 없음
- aria-label 누락
- label 연결 누락
- role 오해
- hidden 상태
- name 문자열 불일치

---

### [실무]

Debug Flow:

```text
getByRole 실패
→ screen.debug 확인
→ 요소 태그 확인
→ role 확인
→ accessible name 확인
→ label / aria-label 확인
→ hidden 여부 확인
→ semantic HTML로 개선
```

예:

```jsx
// 실패 가능
<div onClick={onSave}>저장</div>

// 개선
<button type="button" onClick={onSave}>저장</button>
```

---

### [FAQ]

Q. getByRole로 버튼을 못 찾는 이유는?

A.
실제 요소가 button이 아니거나 accessible name이 없을 수 있다.

Q. testId로 찾으면 해결 아니야?

A.
테스트는 통과할 수 있지만 접근성 문제를 가릴 수 있다. 먼저 semantic 구조를 개선하는 것이 좋다.

---

## 15.2 Keyboard Trap Troubleshooting

### [개념]

Keyboard Trap은 키보드 사용자가 특정 UI 영역에 갇히거나 빠져나갈 수 없는 문제다.

Modal, Dropdown, Custom Widget에서 발생할 수 있다.

---

### [핵심]

원인:

- focus trap 구현 오류
- 닫기 버튼 없음
- Escape 닫기 없음
- focus return 누락
- hidden element focus 가능
- tab order 오류

---

### [실무]

Debug Flow:

```text
Tab 이동 확인
→ Shift+Tab 확인
→ Escape 확인
→ 닫기 버튼 확인
→ focus return 확인
→ hidden element focus 확인
```

권장:

- Modal은 의도된 focus trap 필요
- Dropdown은 닫기와 focus 흐름 필요
- 사용자가 빠져나갈 방법 제공
- focus 위치가 시각적으로 보여야 함
- 복잡한 focus 관리는 라이브러리 검토 가능

---

### [FAQ]

Q. Modal 안에 focus가 갇히는 건 문제야?

A.
Modal이 열려 있는 동안 내부에 focus를 제한하는 것은 정상일 수 있다. 하지만 닫을 방법이 없거나 닫은 뒤 focus가 사라지면 문제다.

Q. Dropdown에서 Tab을 누르면 이상하게 이동해?

A.
열린 메뉴 item의 focus 순서와 닫힘 처리를 확인해야 한다.

---

## 15.3 Missing Label Troubleshooting

### [개념]

Missing Label은 input이 어떤 값을 입력받는지 보조기술에 전달되지 않는 문제다.

---

### [핵심]

원인:

- label 없음
- htmlFor와 id 불일치
- id 중복
- placeholder만 사용
- custom input label 누락
- aria-label 누락

---

### [실무]

Debug Flow:

```text
Input 확인
→ label 존재 확인
→ label htmlFor 확인
→ input id 확인
→ id 중복 확인
→ getByLabelText 테스트 확인
```

개선:

```jsx
<label htmlFor="password">비밀번호</label>
<input id="password" type="password" />
```

---

### [FAQ]

Q. getByLabelText가 실패하는 이유는?

A.
label과 input이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

Q. placeholder로 label을 대신하면 왜 문제야?

A.
입력 중 사라지고 보조기술에서 안정적인 이름으로 쓰기 어렵기 때문이다.

---

## 15.4 Focus Lost Troubleshooting

### [개념]

Focus Lost는 UI 변경 후 사용자의 keyboard focus가 사라지거나 예상하지 못한 위치로 이동하는 문제다.

---

### [핵심]

원인:

- focused element unmounted
- modal close 후 focus return 없음
- route change 후 focus 처리 없음
- conditional rendering
- list rerender key 변경
- disabled focused element
- hidden focused element

---

### [실무]

Debug Flow:

```text
현재 focus 확인
→ UI 변경 시점 확인
→ unmount 여부 확인
→ key 변경 확인
→ modal close 처리 확인
→ route change 처리 확인
→ focus 이동 필요 여부 판단
```

권장:

- Modal 닫기 후 trigger로 focus 복귀
- 삭제 후 다음 합리적 위치로 focus 이동 고려
- route 이동 후 h1 또는 main으로 focus 이동 검토
- list item key 안정성 유지
- focus를 불필요하게 빼앗지 않음

---

### [FAQ]

Q. Modal을 닫으면 focus가 사라져?

A.
Modal을 열었던 버튼이나 적절한 다음 위치로 focus를 복귀시키는 처리가 필요할 수 있다.

Q. 항목 삭제 후 focus는 어디로 가야 해?

A.
삭제 버튼이 사라지므로 다음 항목, 이전 항목, 목록 제목 등 사용자가 이어서 조작할 수 있는 위치를 고려한다.

---

# 16. Security and Privacy Rules

## 16.1 Accessibility and Privacy

### [개념]

접근성 구현 중에도 민감정보가 불필요하게 노출되지 않도록 주의해야 한다.

aria-label, error message, live region, alt text에도 개인정보나 보안 정보가 과도하게 들어가지 않게 한다.

---

### [핵심]

주의 대상:

- password
- access token
- personal data
- user email
- phone number
- address
- internal error
- stack trace
- role policy detail

---

### [실무]

주의:

- 비밀번호 값을 accessible text로 노출하지 않음
- token 값을 error message에 포함하지 않음
- 내부 서버 오류를 role alert로 그대로 노출하지 않음
- 개인정보가 포함된 alt text 주의
- Toast / live region에 민감정보 노출 주의
- 403 메시지에 내부 권한 정책 상세 노출 지양

---

### [FAQ]

Q. 접근성 텍스트에는 어떤 정보든 넣어도 돼?

A.
아니다. 스크린 리더가 읽을 수 있는 텍스트도 사용자에게 노출되는 정보이므로 민감정보를 피해야 한다.

Q. 서버 에러를 alert로 그대로 읽어줘도 돼?

A.
권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

---

# 17. Comparison Rules

## 17.1 Required Comparisons

### [개념]

Frontend Accessibility 문서는 헷갈리는 접근성 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Semantic HTML vs ARIA
- Button vs Link
- Visible Label vs Placeholder
- aria-label vs aria-labelledby
- aria-describedby vs aria-label
- role status vs role alert
- Focus vs Hover
- Disabled vs ReadOnly
- Hidden vs Visually Hidden
- Decorative Image vs Informative Image
- Modal vs Popover
- Tab vs Route
- Dropdown vs Select
- Keyboard Trap vs Focus Trap
- Error Message vs Helper Text
- Manual Test vs Automated Test

---

### [실무]

예시:

| 비교      | Semantic HTML     | ARIA             |
| --------- | ----------------- | ---------------- |
| 역할      | 기본 의미 제공    | 부족한 의미 보완 |
| 예        | button, nav, main | aria-expanded    |
| 안정성    | 높음              | 잘못 쓰면 위험   |
| 우선순위  | 먼저 사용         | 필요한 경우 사용 |
| 구현 부담 | 낮음              | 상태 동기화 필요 |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
접근성은 비슷해 보이는 개념이 많아서 선택 기준을 표로 정리하면 Retrieval과 답변 정확도가 좋아진다.

Q. Accessibility 비교 문서에서 가장 중요한 것은?

A.
Semantic HTML을 우선하고 ARIA는 보완으로 사용한다는 원칙이다.

---

# 18. Checklist Rules

## 18.1 Frontend Accessibility Checklist

### [개념]

Frontend Accessibility 문서 검수 시 접근성 체크리스트를 사용한다.

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

검수 기준:

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

---

### [FAQ]

Q. 접근성 검수에서 가장 먼저 볼 것은?

A.
Semantic HTML, keyboard 조작, label 연결, focus visible, error message 연결을 먼저 확인하는 것이 좋다.

Q. 접근성 체크리스트는 매번 다 봐야 해?

A.
핵심 Form, Modal, Navigation, 공통 UI Component에서는 꼼꼼히 확인하는 것이 좋다.

---

# 19. Retrieval Optimization Rules

## 19.1 Keyword Rules

### [개념]

Frontend Accessibility 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Frontend Accessibility
- Web Accessibility
- a11y
- Semantic HTML
- Keyboard Accessibility
- Focus Management
- Focus Visible
- Tab Order
- Accessible Name
- Label
- aria-label
- aria-labelledby
- aria-describedby
- aria-invalid
- aria-expanded
- aria-selected
- aria-current
- aria-live
- role alert
- role status
- Button Accessibility
- Link Accessibility
- Form Accessibility
- Modal Accessibility
- Dropdown Accessibility
- Tab Accessibility
- Image Alt Text
- Icon Button
- Color Contrast
- Color Only Meaning
- Error Message Accessibility
- Loading Accessibility
- Screen Reader
- Testing Library Accessibility Query
- getByRole
- getByLabelText
- axe

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- div onClick 써도 돼?
- placeholder가 있으면 label 없어도 돼?
- getByRole이 실패하는 이유는?
- icon button에는 aria-label이 필요해?
- focus outline 없애도 돼?
- Modal 접근성은 어떻게 처리해?
- Dropdown 접근성은 어떻게 처리해?
- aria-expanded는 언제 써?
- error message는 input과 어떻게 연결해?
- 색상만으로 에러 표시해도 돼?
- alt text는 어떻게 써?
- axe 테스트만 통과하면 돼?
- 키보드 접근성은 어떻게 확인해?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 20. Version Rules

## 20.1 Modern Frontend Accessibility 기준

### [개념]

Frontend Accessibility 문서는 Modern React Frontend 접근성 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Semantic HTML 우선
- ARIA 보완 사용
- Keyboard First Check
- Focus Visible 유지
- Label 기반 Form
- Accessible Error Message
- Accessible Loading State
- React Testing Library Query 연동
- axe 기초 고려
- Component 설계 단계에서 접근성 포함

Legacy 제외:

- div onClick 남용
- label 없는 input
- placeholder-only form
- focus outline 제거
- 색상만으로 상태 표시
- icon button accessible name 누락
- role만 붙이고 keyboard 구현 누락
- Modal focus 관리 누락
- testId 중심 테스트로 접근성 문제 숨김
- ARIA 무분별 사용

---

### [실무]

실무 기준:

```text
Modern Accessibility
→ Semantic HTML
→ Keyboard Support
→ Accessible Name
→ Focus Management
→ State Announcement
→ Testing Query Verification
```

---

### [FAQ]

Q. React에서 접근성은 특별한 라이브러리가 필요해?

A.
기본은 Semantic HTML과 올바른 props 설계로 시작한다. 복잡한 Modal, Dropdown, Select는 접근성 검증된 라이브러리를 검토할 수 있다.

Q. 접근성은 나중에 고쳐도 돼?

A.
일부는 가능하지만 구조를 나중에 고치면 비용이 커진다. Component 설계 단계부터 반영하는 것이 좋다.

---

# 21. Common Mistakes

## 21.1 Frontend Accessibility Common Mistakes

### [개념]

Frontend Accessibility 문서는 자주 발생하는 접근성 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- div onClick을 button처럼 사용
- Link와 Button 역할 혼동
- input label 누락
- placeholder를 label로 대체
- icon button aria-label 누락
- focus outline 제거
- keyboard 조작 불가
- positive tabindex 남용
- color only status
- error message와 input 미연결
- aria-invalid 상태 불일치
- aria-expanded 상태 불일치
- Modal focus 관리 누락
- Modal 닫기 후 focus 복귀 누락
- Dropdown keyboard 조작 누락
- Tab aria-selected 누락
- 이미지 alt 누락 또는 과도한 alt
- 장식 이미지를 스크린 리더가 읽음
- role을 붙였지만 keyboard 동작 미구현
- Testing에서 testId만 사용해 접근성 문제를 숨김

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: getByRole("button")이 실패함
원인: div에 onClick을 붙여 button처럼 사용함
해결: button 태그로 변경하고 accessible name을 제공
```

---

### [FAQ]

Q. 접근성 초보가 가장 많이 하는 실수는?

A.
div onClick 사용, label 누락, focus outline 제거, icon button 이름 누락, 색상만으로 상태 표시하는 실수가 많다.

Q. 접근성 문제는 어떻게 찾는 게 좋아?

A.
키보드만으로 조작해 보고, getByRole / getByLabelText 테스트를 사용하며, label과 focus 흐름을 확인한다.

---

# 22. Final Goal

## 22.1 Domain Final Goal

### [개념]

Frontend Accessibility RAG 문서는 Frontend Agent가 React UI를 키보드, 스크린 리더, 다양한 사용자 환경에서도 사용할 수 있도록 설계하고 검토하게 해야 한다.

---

### [핵심]

최종 목표:

- Semantic HTML 우선 적용
- Button / Link 역할 구분
- Landmark 구조 설계
- Heading 구조 검토
- Form label 연결
- Error Message 접근성 적용
- Required Field 명확화
- Keyboard Navigation 검토
- Focus Visible 유지
- Tab Order 검토
- ARIA 속성 적절히 사용
- Accessible Name 제공
- aria-live 상태 메시지 적용
- Image Alt Text 판단
- Icon Accessibility 적용
- Color Contrast 검토
- Color Only Meaning 방지
- Modal / Dropdown / Tab 접근성 검토
- Loading / Error / Empty State 접근성 적용
- Table / List 접근성 적용
- React Conditional Rendering 접근성 검토
- Testing Library Accessibility Query로 검증
- Common Accessibility Mistakes 검토

---

### [실무]

Agent 수행 가능 작업:

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

### [FAQ]

Q. Frontend Accessibility 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 Semantic HTML, keyboard, focus, label, ARIA, error message, testing query를 기준으로 접근성 있는 UI를 만들고 검토하게 하는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Frontend Build & Deploy, Frontend Code Review, Styling Architecture, Design System 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Accessibility 문서는 왜 필요해?
A. Frontend Agent가 키보드, 스크린 리더, 다양한 사용자 환경에서도 사용할 수 있는 UI를 만들고 검토해야 하기 때문이다.

Q. 접근성은 왜 중요해?
A. 사용자가 마우스, 키보드, 스크린 리더 등 다양한 방식으로 서비스를 사용할 수 있어야 하기 때문이다.

Q. Semantic HTML이 뭐야?
A. HTML 요소를 의미에 맞게 사용하는 것이다. button, nav, main, label 같은 태그를 역할에 맞게 사용한다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

Q. div onClick을 써도 돼?
A. 가능은 하지만 키보드 접근성과 의미가 부족하다. 클릭 액션은 button을 사용하는 것이 좋다.

Q. role="button"을 쓰면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다. 가능하면 button 태그를 사용한다.

Q. Button과 Link 차이는?
A. Button은 액션 실행이고 Link는 페이지나 위치 이동이다.

Q. 상세 페이지 이동 버튼은 button이야 Link야?
A. 단순 페이지 이동이라면 Link가 적합하다.

Q. 삭제는 Link로 만들어도 돼?
A. 권장하지 않는다. 삭제는 현재 상태를 변경하는 액션이므로 button이 적합하다.

Q. main 태그는 꼭 필요해?
A. 페이지 주요 콘텐츠를 나타내기 위해 사용하는 것이 좋다.

Q. nav가 여러 개면 어떻게 해?
A. aria-label로 “주요 메뉴”, “하단 메뉴”처럼 구분하는 것이 좋다.

Q. h1은 여러 개 있어도 돼?
A. HTML상 가능하지만 일반적인 앱 페이지에서는 페이지 핵심 제목 하나를 h1로 두는 방식이 명확하다.

Q. 글자 크기를 줄이려고 h4를 써도 돼?
A. 권장하지 않는다. heading은 문서 구조 기준이고 크기는 CSS로 조정한다.

Q. placeholder가 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 스크린 리더 label을 안정적으로 대체하지 못한다.

Q. 디자인상 label을 보이기 어렵다면?
A. 시각적으로 숨긴 label을 제공하거나 aria-label / aria-labelledby를 사용할 수 있다.

Q. 에러 메시지는 input과 꼭 연결해야 해?
A. 권장한다. 스크린 리더 사용자가 어떤 입력값에 문제가 있는지 이해하기 쉽다.

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 색각 이상 사용자나 스크린 리더 사용자가 오류를 인식하기 어렵다.

Q. 필수값 표시로 별표만 붙이면 돼?
A. 별표의 의미를 설명하거나 “필수” 텍스트를 함께 제공하는 것이 좋다.

Q. required와 aria-required를 둘 다 써야 해?
A. 일반 input에서는 required가 우선이다. custom widget에서는 aria-required를 고려할 수 있다.

Q. radio group에는 fieldset이 꼭 필요해?
A. 권장한다. 여러 선택지가 하나의 질문에 속한다는 구조를 명확히 전달할 수 있다.

Q. legend는 label이랑 달라?
A. label은 개별 input 설명이고 legend는 fieldset 그룹 전체 설명이다.

Q. 마우스로 잘 되면 키보드도 되는 거 아니야?
A. 아니다. div onClick, custom dropdown, modal 등은 키보드 조작이 누락될 수 있다.

Q. 키보드 접근성은 뭘 먼저 확인해?
A. Tab 이동, Enter / Space 실행, Escape 닫기, focus visible 여부부터 확인한다.

Q. focus outline을 없애면 디자인이 깔끔해지는데 괜찮아?
A. 권장하지 않는다. 키보드 사용자가 현재 위치를 알 수 없게 된다. 대신 디자인에 맞는 focus style을 제공한다.

Q. focus와 hover는 같은 거야?
A. 다르다. hover는 마우스 상태이고 focus는 키보드나 프로그램적 초점 상태다.

Q. tabindex를 많이 쓰면 키보드 순서를 쉽게 조정할 수 있지 않아?
A. 양수 tabindex는 유지보수를 어렵게 만들 수 있다. DOM 순서를 올바르게 설계하는 것이 우선이다.

Q. tabindex="-1"은 언제 써?
A. 사용자 Tab 순서에는 포함하지 않지만 코드로 focus를 이동해야 하는 요소에 사용할 수 있다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. 잘못된 ARIA는 오히려 접근성을 해칠 수 있다. 먼저 semantic HTML을 사용한다.

Q. getByRole에서 name이 안 잡히는 이유는?
A. 요소에 accessible name이 없거나 기대한 이름과 실제 이름이 다를 수 있다.

Q. 아이콘 버튼에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. role="alert"와 aria-live는 뭐가 달라?
A. role="alert"는 중요한 오류나 긴급 메시지를 즉시 알리는 데 사용되고, aria-live="polite"는 덜 긴급한 변경을 자연스럽게 알린다.

Q. Toast에도 aria-live가 필요해?
A. Toast가 중요한 상태 메시지를 전달한다면 보조기술 사용자가 인식할 수 있게 live region을 고려한다.

Q. 모든 이미지에 자세한 alt를 넣어야 해?
A. 아니다. 장식 이미지는 alt=""가 적합하고, 정보 이미지는 의미를 전달하는 alt가 필요하다.

Q. 축제 카드 이미지 alt는 어떻게 써?
A. 이미지가 정보 전달 역할이면 축제명이나 이미지 의미를 포함하고, 카드 제목과 완전히 중복이면 장식 처리도 검토할 수 있다.

Q. 아이콘에 항상 aria-label을 붙여야 해?
A. 아니다. 장식 아이콘은 aria-hidden이 적합하고, 아이콘만으로 기능을 나타내는 버튼에는 aria-label이 필요하다.

Q. 체크 아이콘만 보여주면 성공 상태가 전달돼?
A. 색상이나 아이콘만으로는 부족할 수 있다. 텍스트나 accessible name을 함께 제공하는 것이 좋다.

Q. 회색 글씨가 예쁘면 그냥 써도 돼?
A. 텍스트 대비가 낮으면 읽기 어려울 수 있다. 디자인보다 가독성과 접근성을 함께 고려해야 한다.

Q. 다크모드에서도 색상 대비를 따로 봐야 해?
A. 그렇다. 라이트모드에서 괜찮은 색상이 다크모드에서는 부족할 수 있다.

Q. 빨간색이면 에러라는 걸 알 수 있지 않아?
A. 모든 사용자가 색상을 동일하게 인식하지 않는다. 텍스트나 아이콘을 함께 제공해야 한다.

Q. 활성 메뉴를 색상만 다르게 해도 돼?
A. 권장하지 않는다. aria-current, 밑줄, 굵기, 텍스트 등 추가 단서를 제공하는 것이 좋다.

Q. Button에 type을 꼭 써야 해?
A. form 안에서는 기본 submit 동작 때문에 type을 명시하는 것이 안전하다. 공통 Button은 type="button" 기본값이 좋다.

Q. 아이콘만 있는 닫기 버튼은 어떻게 해?
A. aria-label="닫기"처럼 버튼의 목적을 제공해야 한다.

Q. “자세히 보기” 링크를 반복해서 써도 돼?
A. 가능하지만 스크린 리더에서는 목적지가 모호할 수 있다. “봄꽃 축제 자세히 보기”처럼 구체화하는 것이 좋다.

Q. 현재 메뉴는 어떻게 표시해?
A. 시각적 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. Modal에 role dialog만 붙이면 접근성이 끝이야?
A. 아니다. focus 이동, focus trap, 닫기 버튼, aria-labelledby 같은 요소도 필요하다.

Q. Modal 닫은 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. Dropdown은 div로 만들어도 돼?
A. 시각적으로 가능하지만 keyboard, aria-expanded, focus 관리가 누락되기 쉽다. trigger는 button을 사용하는 것이 좋다.

Q. aria-expanded는 언제 바뀌어야 해?
A. 실제 dropdown open 상태와 항상 일치해야 한다.

Q. Tab은 button 여러 개만 있으면 돼?
A. 기본 전환은 가능하지만 접근성을 위해 role, aria-selected, tabpanel 연결을 고려해야 한다.

Q. Tab과 Route는 어떻게 구분해?
A. 같은 페이지 안의 패널 전환이면 Tab, 페이지 수준 이동이면 Route가 적합하다.

Q. Spinner만 보이면 충분해?
A. 아니다. 스크린 리더 사용자를 위해 loading 상태를 설명하는 텍스트나 role status가 필요하다.

Q. Skeleton은 스크린 리더가 읽어야 해?
A. 대부분 장식 요소로 보고 aria-hidden 처리하고 별도 loading message를 제공하는 것이 좋다.

Q. Error Message에 role alert를 붙이면 돼?
A. 중요한 오류에는 도움이 된다. 다만 모든 작은 변화에 alert를 남발하면 사용자를 방해할 수 있다.

Q. 데이터가 없으면 그냥 빈 배열 렌더링하면 안 돼?
A. 권장하지 않는다. 사용자가 정상 상태인지 오류인지 알 수 있도록 Empty State를 제공하는 것이 좋다.

Q. 카드 목록은 ul/li로 감싸야 해?
A. 반복되는 항목 목록이라면 ul/li를 사용하는 것이 의미상 좋다.

Q. 표를 div로 만들어도 돼?
A. 행과 열 관계가 중요한 데이터는 table 요소를 사용하는 것이 접근성에 좋다.

Q. 조건부 렌더링이면 접근성에서 뭘 조심해야 해?
A. focus가 사라진 요소에 남지 않는지, open 상태가 aria와 동기화되는지, 동적 메시지가 전달되는지 확인해야 한다.

Q. Custom Component는 어떻게 검증해?
A. keyboard 조작, screen reader 이름, role, focus 이동, Testing Library getByRole query 등을 확인한다.

Q. 자동화 도구만 돌리면 접근성 테스트 끝이야?
A. 아니다. keyboard 조작, focus 흐름, 실제 사용자 경험은 수동 확인이 필요하다.

Q. getByRole이 실패하면 접근성 문제야?
A. 가능성이 있다. semantic element, role, accessible name이 올바른지 확인해야 한다.

Q. axe 테스트 통과하면 접근성 문제 없는 거야?
A. 아니다. 자동화 도구가 잡지 못하는 keyboard, focus, 사용자 맥락 문제가 남을 수 있다.

Q. testId로 찾으면 해결 아니야?
A. 테스트는 통과할 수 있지만 접근성 문제를 가릴 수 있다. 먼저 semantic 구조를 개선하는 것이 좋다.

Q. Modal 안에 focus가 갇히는 건 문제야?
A. Modal이 열려 있는 동안 내부에 focus를 제한하는 것은 정상일 수 있다. 하지만 닫을 방법이 없거나 닫은 뒤 focus가 사라지면 문제다.

Q. getByLabelText가 실패하는 이유는?
A. label과 input이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

Q. Modal을 닫으면 focus가 사라져?
A. Modal을 열었던 버튼이나 적절한 다음 위치로 focus를 복귀시키는 처리가 필요할 수 있다.

Q. 접근성 텍스트에는 어떤 정보든 넣어도 돼?
A. 아니다. 스크린 리더가 읽을 수 있는 텍스트도 사용자에게 노출되는 정보이므로 민감정보를 피해야 한다.

Q. 접근성 초보가 가장 많이 하는 실수는?
A. div onClick 사용, label 누락, focus outline 제거, icon button 이름 누락, 색상만으로 상태 표시하는 실수가 많다.

Q. 접근성 문제는 어떻게 찾는 게 좋아?
A. 키보드만으로 조작해 보고, getByRole / getByLabelText 테스트를 사용하며, label과 focus 흐름을 확인한다.

Q. Frontend Accessibility 다음 문서는 뭐가 좋아?
A. Frontend Build & Deploy, Frontend Code Review, Styling Architecture, Design System 순서가 좋다.
