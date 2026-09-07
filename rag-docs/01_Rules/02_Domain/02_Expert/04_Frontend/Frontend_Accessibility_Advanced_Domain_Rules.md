# Frontend Accessibility Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Accessibility Advanced Domain 목적

### [개념]

Frontend Accessibility Advanced Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent / UI Review Agent용 RAG 문서 제작 규칙이다.

Frontend Accessibility는 장애 여부, 입력 방식, 기기 환경, 브라우저 설정, 보조 기술 사용 여부와 관계없이 사용자가 웹 애플리케이션을 이해하고 조작할 수 있도록 만드는 영역이다.

Accessibility Advanced는 단순히 `alt` 속성이나 색상 대비만 확인하는 수준을 넘어, Semantic HTML, Keyboard Navigation, Focus Management, ARIA, Screen Reader UX, Form Error, Dialog, Menu, Live Region, Motion, Design System, Testing까지 포함한다.

목적:

- 접근성 중심 UI 설계 지원
- Semantic HTML 사용 기준 제공
- Keyboard Navigation 설계 지원
- Focus Management 기준 제공
- ARIA 사용 기준 제공
- Form / Validation 접근성 지원
- Dialog / Modal / Menu / Dropdown 접근성 지원
- Screen Reader UX 개선 지원
- Color Contrast / Motion / Responsive 접근성 기준 제공
- React / Next.js 접근성 코드 리뷰 지원
- Design System 접근성 기준 제공
- Accessibility Testing 기준 제공

---

### [핵심]

우선순위:

1. Semantic HTML
2. Keyboard Accessibility
3. Focus Management
4. Accessible Name
5. ARIA Correctness
6. Form Accessibility
7. Error Message Accessibility
8. Dialog / Modal Accessibility
9. Menu / Dropdown Accessibility
10. Live Region
11. Color Contrast
12. Motion Accessibility
13. Image / Icon Accessibility
14. Link / Button Semantics
15. Screen Reader UX
16. Responsive / Zoom Accessibility
17. Design System Accessibility
18. React / Next.js Accessibility
19. Accessibility Testing
20. Code Review Criteria

---

### [실무]

2026 실무 기준:

- React / TypeScript / Next.js App Router 기준 예제 우선
- Semantic HTML을 ARIA보다 우선
- ARIA는 native HTML로 해결할 수 없을 때만 사용
- 모든 interactive element는 keyboard로 접근 가능해야 함
- Focus 이동, focus trap, focus return 기준을 명확히 작성
- Form field는 label, description, error message와 연결
- Modal / Dialog는 role, label, focus trap, escape, focus return 필요
- Icon-only button은 accessible name 필수
- Loading / Error / Success 상태는 보조 기술 사용자에게도 전달
- Color만으로 상태를 전달하지 않음
- Motion은 reduced motion 설정을 고려
- 자동 테스트와 수동 테스트를 함께 포함
- Design System 컴포넌트 단위 접근성 기준을 포함
- Agent가 UI 코드와 컴포넌트를 리뷰할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Accessibility Advanced 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 프로젝트에서 Semantic HTML, Keyboard, Focus, ARIA, Form, Dialog, Screen Reader, Color Contrast, Testing 기준으로 접근성을 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. 접근성은 장애인을 위한 기능만 의미하나?

A.
아니다. 키보드 사용자, 모바일 사용자, 저시력 사용자, 일시적 부상 사용자, 느린 네트워크 사용자, 다양한 입력 환경의 사용자 모두에게 영향을 준다.

Q. ARIA를 많이 쓰면 접근성이 좋아지나?

A.
아니다. native HTML이 우선이며, ARIA는 잘못 사용하면 오히려 접근성을 망칠 수 있다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Accessibility Advanced Domain은 UI 구조, 키보드 조작, 포커스, 보조 기술, 상태 전달, 테스트까지 포함하는 프론트엔드 접근성 기준을 다룬다.

---

### [핵심]

포함 범위:

- Accessibility
- A11y
- WCAG
- Semantic HTML
- Landmark
- Heading Structure
- Button
- Link
- Form
- Label
- Fieldset
- Legend
- Error Message
- Accessible Name
- Accessible Description
- ARIA
- ARIA Role
- ARIA State
- ARIA Property
- Keyboard Navigation
- Tab Order
- Focus Management
- Focus Trap
- Focus Return
- Focus Visible
- Skip Link
- Dialog
- Modal
- Popover
- Dropdown
- Menu
- Tooltip
- Combobox
- Tabs
- Accordion
- Live Region
- Toast
- Alert
- Status
- Loading State
- Screen Reader
- Image Alt
- Icon Button
- Color Contrast
- Reduced Motion
- Responsive Accessibility
- Zoom
- Touch Target
- Pointer Target
- Design System Accessibility
- React Accessibility
- Next.js Accessibility
- Accessibility Testing
- Automated A11y Test
- Manual Keyboard Test
- Screen Reader Test

---

### [실무]

제외 범위:

- WCAG 전체 조항 전문 해설
- 법률 / 규정 심화
- 보조공학 기기 내부 구현
- 브라우저 접근성 트리 내부 구현 심화
- 네이티브 모바일 접근성 심화
- 디자인 시각 이론 전체
- UX Research 전체
- 접근성 컨설팅 보고서 작성법 전체
- 다국어 i18n 전체
- Backend Accessibility

단, 프론트엔드 UI 접근성에 필요한 수준의 WCAG 개념, Screen Reader UX, i18n, Design System, Testing 지식은 포함 가능하다.

---

### [FAQ]

Q. WCAG 전체를 문서에 넣어야 하나?

A.
전체 전문을 넣기보다 프론트엔드 구현과 코드 리뷰에 필요한 핵심 기준을 실무 중심으로 정리한다.

Q. Accessibility Testing만 따로 문서화해도 되나?

A.
가능하지만 이 Domain에서는 설계 기준과 테스트 기준을 함께 다룬다.

Q. Design System 문서와 중복되지 않나?

A.
중복을 최소화한다. 이 문서는 접근성 원칙과 검증 기준에 집중하고, Design System 문서와 연결 가능하게 작성한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Accessibility Advanced RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Frontend Accessibility 문서는 UI 상태와 사용자 조작 흐름이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: User Interaction → Focus → State Change → Screen Reader Announcement
- `[Comparison]`: Button vs Link, Native HTML vs ARIA
- `[Best Practice]`: Semantic HTML 우선, Keyboard-first Review
- `[Troubleshooting]`: 스크린 리더가 안 읽음, focus가 사라짐, tab 순서 이상
- `[Checklist]`: 배포 전 접근성 리뷰

---

### [FAQ]

Q. Accessibility 문서에 Flow가 중요한 이유는?

A.
접근성은 정적인 HTML뿐 아니라 키보드 이동, 포커스 변화, 상태 알림, 오류 복구 흐름까지 포함하기 때문이다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Accessibility Core Principles Rules

## 4.1 접근성 기본 원칙

### [개념]

접근성의 핵심은 사용자가 콘텐츠를 인식하고, 조작하고, 이해하고, 안정적으로 사용할 수 있게 만드는 것이다.

실무에서는 아래 원칙을 기준으로 UI를 설계한다.

- Perceivable
- Operable
- Understandable
- Robust

---

### [핵심]

핵심 원칙:

- Semantic HTML First
- Keyboard First
- Visible Focus
- Clear Label
- Predictable Interaction
- Error Recovery
- No Color-only Meaning
- Respect User Preference
- Screen Reader Friendly
- Native Before Custom
- Test with Real Interaction

---

### [실무]

접근성 판단 질문:

- 이 UI는 키보드만으로 사용할 수 있는가?
- 현재 focus 위치를 볼 수 있는가?
- 버튼과 링크의 의미가 올바른가?
- Form field에 label이 있는가?
- 오류 메시지가 field와 연결되는가?
- Modal이 열렸을 때 focus가 올바르게 이동하는가?
- Modal이 닫히면 focus가 원래 위치로 돌아오는가?
- 상태 변화가 screen reader에 전달되는가?
- 색상 없이도 상태를 이해할 수 있는가?
- 애니메이션을 줄이려는 사용자 설정을 존중하는가?
- 200% zoom에서도 사용할 수 있는가?

---

### [FAQ]

Q. 접근성에서 가장 먼저 봐야 하는 것은?

A.
Semantic HTML, Keyboard 조작, Focus 표시, Label 연결, Form Error 전달을 먼저 봐야 한다.

Q. 접근성은 디자인이 끝난 뒤 수정하면 되나?

A.
아니다. 컴포넌트 설계와 Design System 단계에서 함께 고려해야 유지보수 비용이 낮다.

Q. 접근성이 좋으면 일반 사용자 UX도 좋아지나?

A.
대부분 그렇다. 명확한 구조, 좋은 키보드 흐름, 읽기 쉬운 오류 메시지는 모든 사용자에게 도움이 된다.

---

# 5. Semantic HTML Rules

## 5.1 Semantic HTML 우선 원칙

### [개념]

Semantic HTML은 HTML 요소 자체의 의미를 사용해 브라우저와 보조 기술이 UI 구조와 역할을 이해할 수 있게 하는 방식이다.

접근성에서는 가능한 한 ARIA보다 native HTML을 먼저 사용해야 한다.

---

### [핵심]

우선 사용 요소:

- `button`
- `a`
- `input`
- `label`
- `select`
- `textarea`
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
- `h1` ~ `h6`
- `ul` / `ol` / `li`
- `table`
- `caption`
- `th`
- `td`

---

### [실무]

작성 기준:

- 클릭 가능한 동작은 `button` 사용
- 페이지 이동은 `a` 또는 framework `Link` 사용
- `div` / `span`에 click handler만 붙여 button처럼 만들지 않기
- 제목 구조는 순서 있게 작성
- 주요 영역은 landmark로 구분
- 목록은 list semantic 사용
- 표 데이터는 table semantic 사용
- Form field는 label과 연결
- 시각적 스타일 때문에 semantic을 포기하지 않기
- ARIA로 native semantic을 불필요하게 덮어쓰지 않기

잘못된 예시:

```tsx
<div onClick={onSubmit}>저장</div>
```

권장 예시:

```tsx
<button type="button" onClick={onSubmit}>
  저장
</button>
```

---

### [FAQ]

Q. 왜 `div`를 버튼처럼 만들면 안 되나?

A.
기본 keyboard 조작, focus, role, screen reader 정보가 부족하므로 별도 구현이 필요해지고 실수 가능성이 커진다.

Q. Semantic HTML만 잘 쓰면 ARIA가 필요 없나?

A.
많은 경우 ARIA 없이도 충분하다. 복잡한 custom widget이나 상태 알림에는 ARIA가 필요할 수 있다.

Q. 스타일 때문에 `button` 대신 `div`를 써도 되나?

A.
권장하지 않는다. semantic은 유지하고 CSS로 원하는 스타일을 적용해야 한다.

---

# 6. Landmark and Page Structure Rules

## 6.1 Landmark / Page Structure

### [개념]

Landmark는 페이지의 주요 영역을 의미적으로 구분해 screen reader 사용자가 빠르게 탐색할 수 있게 돕는 구조이다.

---

### [핵심]

주요 landmark:

- `header`
- `nav`
- `main`
- `aside`
- `footer`
- `section`
- `form`
- `search`

Page Structure 기준:

- 하나의 주요 `main`
- 명확한 navigation
- 반복 영역 건너뛰기
- skip link
- heading structure
- section labeling

---

### [실무]

작성 기준:

- 페이지마다 `main` 영역을 명확히 제공
- 여러 navigation이 있으면 accessible name으로 구분
- 반복되는 header / nav를 건너뛸 수 있는 skip link 제공
- heading은 시각 크기가 아니라 문서 구조 기준으로 사용
- `section`은 heading 또는 label과 함께 사용 권장
- layout을 위해 landmark를 남용하지 않기
- 페이지 전환 후 main heading과 focus 흐름 검토
- SPA / App Router에서는 route 변경 후 focus 관리 검토

예시:

```tsx
<a href="#main-content" className="skip-link">
  본문으로 건너뛰기
</a>

<header>...</header>
<nav aria-label="주요 메뉴">...</nav>
<main id="main-content">
  <h1>대시보드</h1>
</main>
```

---

### [FAQ]

Q. `main`은 여러 개 있어도 되나?

A.
일반적으로 페이지의 주요 콘텐츠 영역은 하나의 `main`으로 두는 것이 좋다.

Q. Skip Link는 왜 필요한가?

A.
키보드 사용자가 매번 긴 navigation을 지나지 않고 본문으로 바로 이동할 수 있게 돕는다.

Q. Heading은 글자 크기 때문에 선택하나?

A.
아니다. heading은 문서 구조를 표현하기 위해 사용하고, 크기는 CSS로 조정한다.

---

# 7. Keyboard Accessibility Rules

## 7.1 Keyboard Navigation 기준

### [개념]

Keyboard Accessibility는 마우스 없이 Tab, Shift+Tab, Enter, Space, Arrow Key, Escape만으로 UI를 사용할 수 있게 하는 기준이다.

---

### [핵심]

필수 기준:

- Tab Navigation
- Shift+Tab Reverse Navigation
- Enter Activation
- Space Activation
- Arrow Key Navigation
- Escape Close
- Focus Order
- Focus Visible
- No Keyboard Trap
- Skip Link
- Roving Tabindex
- Typeahead Optional

---

### [실무]

작성 기준:

- 모든 interactive element는 keyboard focus 가능
- focus 순서는 시각적 흐름과 논리적으로 일치
- focus가 보이는 스타일 필수
- Modal / Menu 외에는 keyboard trap 금지
- Modal 내부에서는 focus trap 필요
- Escape로 닫을 수 있는 overlay는 닫힘 동작 제공
- custom menu / tab / combobox는 keyboard interaction pattern 준수
- disabled element는 keyboard 접근성과 설명 방식 검토
- hover로만 표시되는 기능은 focus에서도 표시
- drag-and-drop 기능은 keyboard 대안 검토

주의:

- `tabIndex={0}` 남용 금지
- `tabIndex={-1}`은 programmatic focus 용도
- 양수 `tabIndex` 사용 지양
- focus outline 제거 금지
- click handler만 있고 key handler 없는 custom control 금지

---

### [FAQ]

Q. 키보드 접근성에서 가장 중요한 것은?

A.
Tab으로 이동 가능하고, focus가 보이며, Enter / Space로 조작 가능하고, focus가 갇히지 않는 것이다.

Q. `outline: none`을 써도 되나?

A.
기본 focus outline을 제거하려면 반드시 대체 focus visible 스타일을 제공해야 한다.

Q. Hover 메뉴는 keyboard에서도 열려야 하나?

A.
그렇다. hover로 열리는 정보나 기능은 focus 또는 keyboard interaction으로도 접근 가능해야 한다.

---

# 8. Focus Management Rules

## 8.1 Focus 이동 / 복귀 기준

### [개념]

Focus Management는 사용자의 현재 조작 위치를 명확하게 유지하고, UI 상태 변화 후 적절한 위치로 focus를 이동하거나 복귀시키는 기준이다.

---

### [핵심]

검토 대상:

- Initial Focus
- Focus Trap
- Focus Return
- Focus Visible
- Programmatic Focus
- Route Change Focus
- Error Focus
- Skip Link Focus
- Focus Restoration
- Hidden Element Focus

---

### [실무]

작성 기준:

- Modal 열림 → Modal 내부 첫 의미 있는 요소로 focus 이동
- Modal 닫힘 → Modal을 열었던 trigger로 focus 복귀
- Form 제출 실패 → 첫 번째 오류 field 또는 error summary로 focus 이동
- Route 변경 → main heading 또는 main 영역 focus 검토
- Toast는 focus를 빼앗지 않음
- Dropdown / Menu 닫힘 → trigger로 focus 복귀
- `display: none` / hidden 요소에 focus 가지 않게 관리
- focus 가능한 요소가 DOM 순서와 시각 순서가 다르지 않게 설계
- programmatic focus에는 `tabIndex={-1}` 사용 가능
- focus 이동은 사용자 맥락을 깨지 않게 최소화

예시:

```tsx
function focusFirstError(inputRef: React.RefObject<HTMLInputElement | null>) {
  inputRef.current?.focus();
}
```

---

### [FAQ]

Q. Modal이 열리면 focus는 어디로 가야 하나?

A.
Modal 내부의 제목, 첫 번째 입력 필드, 또는 주요 action으로 이동해야 한다.

Q. Modal이 닫히면 focus는 어디로 가야 하나?

A.
Modal을 열었던 버튼이나 링크로 돌아가야 한다.

Q. Toast가 뜰 때 focus를 toast로 보내야 하나?

A.
대부분 아니다. Toast는 상태 알림으로 전달하고 사용자의 현재 작업 focus는 유지하는 것이 좋다.

---

# 9. Accessible Name and Description Rules

## 9.1 Accessible Name / Description

### [개념]

Accessible Name은 screen reader가 요소의 이름으로 읽는 텍스트이다.

Accessible Description은 요소를 추가로 설명하는 보조 텍스트이다.

---

### [핵심]

Accessible Name 제공 방식:

- Visible Text
- `label`
- `aria-label`
- `aria-labelledby`
- `alt`
- `title` 보조적 사용

Accessible Description 제공 방식:

- `aria-describedby`
- 도움말 텍스트
- 오류 메시지
- 설명 문구

---

### [실무]

작성 기준:

- visible label을 우선
- icon-only button에는 accessible name 필수
- `aria-label`은 visible text를 대체할 때 신중히 사용
- `aria-labelledby`는 화면에 보이는 텍스트와 연결할 때 사용
- Form 설명과 오류는 `aria-describedby`로 연결
- 같은 이름의 버튼이 반복될 때 맥락을 구분
- “자세히 보기” 링크가 여러 개면 대상 이름 포함
- 이미지 버튼은 alt 또는 button label 명확화
- placeholder를 label 대신 사용하지 않기
- title 속성만으로 중요한 설명 제공 금지

예시:

```tsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

---

### [FAQ]

Q. Accessible Name은 왜 중요한가?

A.
Screen reader 사용자가 버튼, 링크, 입력 필드의 목적을 이해하는 핵심 정보이기 때문이다.

Q. Icon-only button에는 무엇이 필요한가?

A.
`aria-label` 또는 화면에 보이지 않는 텍스트로 버튼의 이름을 제공해야 한다.

Q. Placeholder를 label로 써도 되나?

A.
권장하지 않는다. 입력 중 사라지고 screen reader와 오류 연결에도 부족할 수 있다.

---

# 10. ARIA Rules

## 10.1 ARIA 사용 기준

### [개념]

ARIA는 HTML만으로 표현하기 어려운 role, state, property를 보조 기술에 전달하기 위한 속성 집합이다.

ARIA는 native HTML을 대체하는 것이 아니라 보완하는 도구이다.

---

### [핵심]

ARIA 원칙:

- Native HTML First
- No ARIA Better Than Bad ARIA
- Role Must Match Behavior
- State Must Be Updated
- Keyboard Interaction Required
- Accessible Name Required
- Do Not Override Native Semantics Unnecessarily

주요 ARIA:

- `aria-label`
- `aria-labelledby`
- `aria-describedby`
- `aria-expanded`
- `aria-controls`
- `aria-current`
- `aria-selected`
- `aria-pressed`
- `aria-invalid`
- `aria-live`
- `aria-hidden`
- `role`

---

### [실무]

작성 기준:

- native HTML로 해결 가능하면 ARIA 사용하지 않기
- `role="button"`을 쓰면 keyboard 동작도 직접 구현해야 함
- `aria-expanded`는 실제 열림 상태와 동기화
- `aria-current`는 현재 페이지 / 현재 단계 표시
- `aria-selected`는 tab / option 같은 selectable widget에 사용
- `aria-pressed`는 toggle button에 사용
- `aria-hidden="true"`는 보조 기술에서 숨겨도 되는 장식 요소에만 사용
- focus 가능한 요소에 `aria-hidden` 적용 금지
- ARIA role과 DOM 구조 규칙 준수
- 상태가 바뀌면 ARIA 값도 함께 갱신

잘못된 예시:

```tsx
<div role="button" onClick={onClick}>
  저장
</div>
```

권장 예시:

```tsx
<button type="button" onClick={onClick}>
  저장
</button>
```

---

### [FAQ]

Q. ARIA는 언제 써야 하나?

A.
Native HTML로 의미와 상태를 전달할 수 없을 때 보조적으로 사용한다.

Q. `role="button"`을 쓰면 버튼처럼 동작하나?

A.
Screen reader에는 버튼처럼 알려질 수 있지만 keyboard 동작은 직접 구현해야 하므로 native `button`이 더 좋다.

Q. `aria-hidden`은 언제 쓰나?

A.
장식 아이콘처럼 screen reader가 읽지 않아도 되는 요소를 숨길 때 사용한다.

---

# 11. Button and Link Rules

## 11.1 Button / Link Semantics

### [개념]

Button은 현재 페이지에서 동작을 실행하는 요소이고, Link는 다른 위치나 페이지로 이동하는 요소이다.

둘을 시각 스타일 기준으로 바꾸면 접근성과 UX가 깨질 수 있다.

---

### [핵심]

Button 사용 상황:

- Submit
- Open Modal
- Close Modal
- Toggle
- Delete
- Save
- Search
- Load More
- Like / Favorite

Link 사용 상황:

- Page Navigation
- External Navigation
- Anchor Navigation
- Download Link
- Detail Page 이동

---

### [실무]

작성 기준:

- 페이지 이동은 link 사용
- 동작 실행은 button 사용
- button에는 필요한 경우 `type="button"` 명시
- form submit button은 `type="submit"`
- icon-only button에는 accessible name 제공
- 외부 링크는 새 탭 여부와 보안 속성 검토
- disabled link는 의미와 keyboard 접근성 신중히 처리
- link처럼 보이는 button과 button처럼 보이는 link를 의미 없이 섞지 않기
- “클릭하세요”보다 목적을 설명하는 link text 사용
- 반복되는 “자세히 보기”는 대상 이름 포함

예시:

```tsx
<Link href={`/posts/${post.id}`}>{post.title}</Link>

<button type="button" onClick={onLike}>
  좋아요
</button>
```

---

### [FAQ]

Q. Button과 Link 차이는?

A.
Button은 동작을 실행하고, Link는 이동을 수행한다.

Q. 페이지 이동을 button으로 해도 되나?

A.
권장하지 않는다. 이동은 link semantic을 사용하는 것이 좋다.

Q. Icon-only button에는 무엇을 해야 하나?

A.
`aria-label`이나 숨김 텍스트로 목적을 명확히 제공해야 한다.

---

# 12. Form Accessibility Rules

## 12.1 Form / Input 접근성

### [개념]

Form Accessibility는 사용자가 입력 필드의 목적, 요구 조건, 오류 상태, 도움말을 이해하고 keyboard와 screen reader로 제출할 수 있게 하는 기준이다.

---

### [핵심]

필수 기준:

- Label
- Required Indicator
- Field Description
- Error Message
- `aria-invalid`
- `aria-describedby`
- Fieldset
- Legend
- Autocomplete
- Input Type
- Validation Timing
- Error Summary

---

### [실무]

작성 기준:

- 모든 input에 visible label 제공
- label과 input을 `htmlFor` / `id`로 연결
- required 표시는 시각적 표시와 텍스트 설명 함께 제공
- error message는 field와 `aria-describedby`로 연결
- invalid field에는 `aria-invalid` 사용 가능
- 여러 관련 input은 `fieldset` / `legend` 사용
- 적절한 input type 사용
- 자동완성 속성 검토
- 제출 실패 시 첫 오류 또는 error summary로 focus 이동
- placeholder만으로 label 대체 금지
- 오류 메시지는 구체적이고 해결 가능하게 작성

예시:

```tsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  type="email"
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "email-error" : undefined}
/>
{error && <p id="email-error">{error}</p>}
```

---

### [FAQ]

Q. Form 접근성에서 가장 중요한 것은?

A.
Label 연결, 오류 메시지 연결, keyboard 조작, 명확한 validation 안내이다.

Q. Required 필드는 별표만 표시하면 되나?

A.
별표만으로는 부족할 수 있다. “필수 입력”이라는 텍스트나 설명을 함께 제공하는 것이 좋다.

Q. Error message는 어떻게 연결하나?

A.
오류 메시지 요소에 id를 부여하고 input의 `aria-describedby`로 연결한다.

---

# 13. Error Message Accessibility Rules

## 13.1 오류 메시지 접근성

### [개념]

Error Message Accessibility는 사용자에게 무엇이 잘못되었고 어떻게 수정해야 하는지 명확하게 알려주는 기준이다.

---

### [핵심]

오류 유형:

- Field Error
- Form Error
- Page Error
- Inline Error
- Toast Error
- Validation Error
- Server Error
- Permission Error
- Network Error

필수 기준:

- Clear Message
- Field Association
- Error Summary
- Focus Management
- Live Announcement
- Recovery Action
- No Color-only Error

---

### [실무]

작성 기준:

- 오류 메시지는 구체적으로 작성
- 오류 위치와 수정 방법 제공
- field error는 해당 field와 연결
- form 제출 실패 시 error summary 제공 검토
- 첫 번째 오류 field로 focus 이동 가능
- 색상만으로 오류 표시 금지
- 아이콘 + 텍스트 조합 사용
- 서버 오류와 validation 오류 구분
- toast로만 중요한 오류 전달하지 않기
- screen reader에 오류가 전달되는지 테스트

예시:

```tsx
<div role="alert">이메일 형식이 올바르지 않습니다. 예: user@example.com</div>
```

주의:

- `role="alert"` 남용 금지
- 사용자가 입력 중일 때 과도한 즉시 오류 알림 지양
- 오류 메시지가 너무 추상적이면 수정 어려움
- Form 전체 오류와 Field 오류를 구분
- focus를 갑자기 이동시키는 것은 제출 실패처럼 명확한 시점에만 사용

---

### [FAQ]

Q. 오류 메시지는 어떻게 작성해야 하나?

A.
무엇이 문제인지, 어디를 고쳐야 하는지, 어떻게 고칠 수 있는지 알려줘야 한다.

Q. Toast로 오류를 보여주면 충분한가?

A.
중요한 Form 오류는 toast만으로 부족하다. 해당 field 근처와 error summary에 표시하는 것이 좋다.

Q. 오류를 색상만으로 표시해도 되나?

A.
안 된다. 텍스트, 아이콘, aria 속성 등 색상 외 정보가 필요하다.

---

# 14. Dialog / Modal Accessibility Rules

## 14.1 Dialog / Modal 접근성

### [개념]

Dialog / Modal은 현재 작업 흐름 위에 임시로 열리는 UI이며, 열리는 동안 focus와 screen reader 탐색이 dialog 내부로 제한되어야 한다.

---

### [핵심]

필수 기준:

- `role="dialog"` 또는 native dialog
- `aria-modal="true"`
- Accessible Name
- Initial Focus
- Focus Trap
- Escape Close
- Focus Return
- Background Inert
- Close Button
- Scroll Lock
- Keyboard Support

---

### [실무]

작성 기준:

- Dialog에는 제목 또는 accessible name 제공
- 열릴 때 focus를 dialog 내부로 이동
- 닫힐 때 trigger로 focus 복귀
- dialog 내부에서 Tab 순환
- Escape로 닫기 지원 가능
- 명확한 닫기 버튼 제공
- background content가 screen reader와 keyboard에서 비활성화되도록 처리
- destructive action confirm dialog는 action 이름 명확화
- alert dialog는 중요한 결정을 요구할 때만 사용
- 중첩 modal 지양

예시:

```tsx
<div role="dialog" aria-modal="true" aria-labelledby="delete-title">
  <h2 id="delete-title">게시글 삭제</h2>
  <p>삭제하면 되돌릴 수 없습니다.</p>
  <button type="button">취소</button>
  <button type="button">삭제</button>
</div>
```

---

### [FAQ]

Q. Modal이 열리면 focus를 어디로 보내야 하나?

A.
Dialog 제목, 첫 입력 필드, 또는 주요 action으로 보내야 한다.

Q. Modal이 닫히면 focus는 어디로 돌아가야 하나?

A.
Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. Modal 밖 배경은 keyboard로 접근 가능해도 되나?

A.
일반 modal에서는 안 된다. Modal이 열린 동안 focus는 modal 내부에 머물러야 한다.

---

# 15. Menu / Dropdown / Popover Rules

## 15.1 Menu / Dropdown / Popover 접근성

### [개념]

Menu, Dropdown, Popover는 trigger를 통해 열리고 닫히는 floating UI이다.

이 컴포넌트들은 keyboard 조작, focus 이동, 열림 상태 전달, 닫힘 동작이 명확해야 한다.

---

### [핵심]

검토 대상:

- Trigger Button
- `aria-expanded`
- `aria-controls`
- Focus Movement
- Escape Close
- Outside Click
- Arrow Key
- Roving Tabindex
- Menu Role
- Listbox Role
- Combobox Role
- Popover Semantics

---

### [실무]

작성 기준:

- trigger는 button 사용
- 열림 상태는 `aria-expanded`로 전달
- trigger와 popup 연결은 필요 시 `aria-controls`
- 열릴 때 focus 이동 정책 명확화
- 닫힐 때 trigger로 focus 복귀
- Escape로 닫기 지원
- Menu / Listbox / Combobox role은 실제 keyboard pattern과 함께 사용
- 단순 링크 목록은 native list + links로 충분할 수 있음
- hover만으로 열리는 dropdown 금지
- popup 내부 항목의 accessible name 명확화

주의:

- `role="menu"`는 애플리케이션 메뉴 패턴이므로 일반 navigation에 남용 금지
- ARIA role을 붙이면 keyboard interaction도 맞춰야 함
- Popover와 Tooltip을 혼동하지 않기
- Dropdown 내부에 form이 있으면 focus trap이 필요한지 검토
- 닫힘 후 focus가 사라지지 않게 관리

---

### [FAQ]

Q. Dropdown trigger는 무엇으로 만들어야 하나?

A.
대부분 `button`이 적합하다. 열림 / 닫힘 동작을 수행하기 때문이다.

Q. `aria-expanded`는 언제 쓰나?

A.
버튼이 dropdown, menu, accordion 같은 확장 영역을 열고 닫을 때 현재 상태를 전달하기 위해 사용한다.

Q. 모든 dropdown에 `role="menu"`를 써야 하나?

A.
아니다. 일반 navigation이나 선택 목록에는 더 적합한 semantic이 있을 수 있다.

---

# 16. Tabs / Accordion Rules

## 16.1 Tabs / Accordion 접근성

### [개념]

Tabs는 여러 panel 중 하나를 선택해 보여주는 UI이고, Accordion은 섹션을 펼치거나 접는 UI이다.

둘 다 선택 상태, 확장 상태, keyboard 조작, panel 연결이 명확해야 한다.

---

### [핵심]

Tabs 기준:

- `tablist`
- `tab`
- `tabpanel`
- `aria-selected`
- `aria-controls`
- Arrow Key Navigation
- Active Tab Focus
- Panel Labeling

Accordion 기준:

- Button Trigger
- `aria-expanded`
- `aria-controls`
- Heading Structure
- Panel Region
- Multiple Open Policy

---

### [실무]

Tabs 작성 기준:

- tab은 keyboard로 이동 가능
- arrow key로 tab 간 이동 검토
- 선택된 tab은 `aria-selected`
- tab과 panel 연결
- tab panel에는 적절한 label 제공
- focus와 selection 정책 명확화

Accordion 작성 기준:

- 각 header 내부에 button 사용
- 확장 상태를 `aria-expanded`로 표시
- button과 panel을 연결
- heading 구조 유지
- 한 개만 열림 / 여러 개 열림 정책 명확화
- 접힌 panel은 keyboard focus 대상이 되지 않게 처리

예시 Accordion:

```tsx
<h3>
  <button
    type="button"
    aria-expanded={isOpen}
    aria-controls="faq-panel-1"
  >
    결제는 어떻게 하나요?
  </button>
</h3>
<div id="faq-panel-1" hidden={!isOpen}>
  카드 또는 간편결제로 결제할 수 있습니다.
</div>
```

---

### [FAQ]

Q. Accordion header는 `div`로 만들어도 되나?

A.
권장하지 않는다. 확장 / 축소 동작은 button으로 구현하는 것이 좋다.

Q. Tabs에서 선택 상태는 어떻게 전달하나?

A.
선택된 tab에 `aria-selected`를 사용하고 tab과 tabpanel을 연결한다.

Q. 접힌 Accordion 내부 요소가 Tab으로 접근되면 안 되나?

A.
접힌 상태에서는 내부 interactive element가 keyboard focus 대상이 되지 않아야 한다.

---

# 17. Tooltip Rules

## 17.1 Tooltip 접근성

### [개념]

Tooltip은 요소에 대한 보조 설명을 제공하는 UI이다.

Tooltip은 중요한 정보를 유일한 전달 수단으로 사용하면 안 되며, keyboard와 screen reader 접근성을 고려해야 한다.

---

### [핵심]

필수 기준:

- Trigger Focus
- Hover and Focus
- `aria-describedby`
- Non-essential Info
- Dismiss Behavior
- No Interactive Content
- Delay Policy
- Touch Alternative

---

### [실무]

작성 기준:

- Tooltip은 hover뿐 아니라 focus에서도 표시
- trigger와 tooltip을 `aria-describedby`로 연결 가능
- 중요한 정보는 tooltip에만 넣지 않기
- tooltip 내부에 button / link 같은 interactive content 넣지 않기
- Escape로 닫기 검토
- 터치 기기에서 대안 제공
- tooltip은 짧고 보조적인 설명만 제공
- tooltip 표시 / 숨김 지연은 과도하지 않게 설정
- tooltip이 focus를 빼앗지 않게 처리

주의:

- Tooltip을 error message 대체로 사용 금지
- Tooltip을 form label 대체로 사용 금지
- hover 전용 tooltip은 keyboard 사용자에게 보이지 않음
- 모바일에서 hover tooltip은 동작하지 않을 수 있음
- 복잡한 콘텐츠는 popover나 dialog가 더 적합

---

### [FAQ]

Q. Tooltip에 중요한 안내를 넣어도 되나?

A.
권장하지 않는다. 중요한 정보는 항상 보이는 텍스트나 field description으로 제공해야 한다.

Q. Tooltip은 keyboard focus에서도 보여야 하나?

A.
그렇다. hover만으로 표시되면 keyboard 사용자가 접근할 수 없다.

Q. Tooltip 안에 버튼을 넣어도 되나?

A.
권장하지 않는다. interactive content가 필요하면 popover나 dialog 패턴을 고려한다.

---

# 18. Live Region Rules

## 18.1 Dynamic Content Announcement

### [개념]

Live Region은 화면의 동적 변화가 screen reader 사용자에게 전달되도록 하는 ARIA 메커니즘이다.

검색 결과 갱신, 저장 성공, 오류 발생, 로딩 완료, 알림 도착 같은 변화에 사용할 수 있다.

---

### [핵심]

관련 속성:

- `aria-live="polite"`
- `aria-live="assertive"`
- `role="status"`
- `role="alert"`
- `aria-atomic`
- `aria-busy`

사용 상황:

- Toast
- Form Error
- Search Result Count
- Loading Complete
- Save Success
- Background Update
- Notification
- Step Change

---

### [실무]

작성 기준:

- 일반 상태 알림은 `polite`
- 긴급 오류는 `assertive` 또는 `role="alert"` 신중히 사용
- 저장 성공 / 실패 메시지는 screen reader에 전달
- 검색 결과 개수 변경 알림 제공
- 로딩 중인 영역에는 `aria-busy` 검토
- live region text는 간결하게 작성
- 너무 잦은 업데이트는 announcement noise 발생
- 동일한 텍스트 반복은 읽히지 않을 수 있음
- Toast는 focus를 빼앗지 않고 live region으로 전달 가능

예시:

```tsx
<div role="status" aria-live="polite">
  저장되었습니다.
</div>
```

---

### [FAQ]

Q. Live Region은 언제 필요한가?

A.
사용자 focus를 이동시키지 않고 동적 상태 변화를 screen reader에 알려야 할 때 필요하다.

Q. `aria-live="assertive"`는 언제 쓰나?

A.
즉시 알려야 하는 중요한 오류나 위험 상황에 제한적으로 사용한다.

Q. Toast는 screen reader에 어떻게 전달하나?

A.
Toast 메시지를 `role="status"`나 적절한 live region에 넣어 전달할 수 있다.

---

# 19. Image and Icon Accessibility Rules

## 19.1 Image / Icon 접근성

### [개념]

Image Accessibility는 이미지가 전달하는 의미를 텍스트 대체 정보로 제공하거나, 장식 이미지는 보조 기술에서 숨기는 기준이다.

Icon Accessibility는 아이콘이 장식인지 기능인지에 따라 다르게 처리해야 한다.

---

### [핵심]

이미지 유형:

- Informative Image
- Decorative Image
- Functional Image
- Complex Image
- Chart / Graph
- Icon
- Logo
- Avatar
- Thumbnail
- Background Image

---

### [실무]

작성 기준:

- 의미 있는 이미지는 alt 제공
- 장식 이미지는 빈 alt 또는 `aria-hidden`
- 링크 / 버튼 안의 이미지는 action 목적을 설명
- 복잡한 chart는 요약과 데이터 설명 제공
- avatar alt는 맥락에 따라 사용자 이름 또는 빈 alt 판단
- logo는 조직 / 서비스 이름 제공
- icon-only button은 button에 accessible name 제공
- icon이 텍스트와 함께 있으면 icon은 `aria-hidden`
- background image에 중요한 정보만 넣지 않기
- 이미지 alt에 “이미지” 같은 불필요한 표현 지양

예시:

```tsx
<img src="/logo.png" alt="FestaPick" />

<button type="button" aria-label="알림 열기">
  <BellIcon aria-hidden="true" />
</button>
```

---

### [FAQ]

Q. 모든 이미지에 alt가 필요하나?

A.
의미 있는 이미지는 alt가 필요하고, 장식 이미지는 빈 alt로 보조 기술에서 무시되게 하는 것이 좋다.

Q. 아이콘 옆에 텍스트가 있으면 아이콘도 읽혀야 하나?

A.
대부분 아니다. 텍스트가 의미를 전달한다면 아이콘은 `aria-hidden` 처리할 수 있다.

Q. Chart 이미지는 alt만으로 충분한가?

A.
대부분 부족하다. 핵심 요약과 데이터 표 또는 상세 설명을 함께 제공하는 것이 좋다.

---

# 20. Color Contrast and Visual Accessibility Rules

## 20.1 색상 대비 / 시각 접근성

### [개념]

Color Contrast는 텍스트와 배경, UI 상태, focus indicator가 충분히 구분되도록 하는 기준이다.

시각 접근성은 색상뿐 아니라 크기, 간격, 상태 표시, 확대, 가독성을 포함한다.

---

### [핵심]

검토 대상:

- Text Contrast
- Large Text Contrast
- Non-text Contrast
- Focus Indicator Contrast
- Error Color
- Disabled State
- Link Contrast
- Dark Mode
- High Contrast Mode
- Color-blind Friendly Design

---

### [실무]

작성 기준:

- 텍스트와 배경의 대비 기준 충족
- 버튼 / 입력 / border / focus indicator도 충분히 구분
- 색상만으로 상태 전달 금지
- error는 색상 + 텍스트 + 아이콘 조합
- link는 색상 외 underline 등 추가 구분 검토
- disabled 상태가 너무 흐려져 읽기 어려운지 확인
- dark mode에서도 대비 확인
- hover / focus / active 상태 대비 확인
- 그래프는 색상 외 패턴 / 라벨 제공
- 200% zoom에서도 콘텐츠 사용 가능해야 함

주의:

- placeholder 색상이 너무 연하면 읽기 어려움
- disabled text도 필요한 정보라면 지나치게 낮은 대비 금지
- 브랜드 색상만 고집하면 접근성 기준을 못 맞출 수 있음
- focus ring 색상이 배경과 섞이면 keyboard 사용자가 위치를 잃음
- 색각 이상 사용자를 고려해 색상 조합 검토

---

### [FAQ]

Q. 색상만으로 오류를 표시해도 되나?

A.
안 된다. 텍스트, 아이콘, aria 상태 등 색상 외 정보가 함께 필요하다.

Q. Dark Mode도 접근성 테스트가 필요한가?

A.
필요하다. Light Mode에서 충분한 대비가 Dark Mode에서도 유지된다는 보장은 없다.

Q. Focus indicator도 색상 대비가 중요한가?

A.
중요하다. 키보드 사용자가 현재 위치를 알아야 하므로 충분히 눈에 보여야 한다.

---

# 21. Motion and Animation Accessibility Rules

## 21.1 Motion / Animation 접근성

### [개념]

Motion Accessibility는 애니메이션, 전환 효과, 자동 재생, 움직이는 콘텐츠가 사용자에게 불편이나 멀미, 집중 방해를 주지 않도록 제어하는 기준이다.

---

### [핵심]

검토 대상:

- Reduced Motion
- Animation Duration
- Auto-play
- Carousel
- Parallax
- Skeleton Animation
- Loading Animation
- Flashing Content
- Scroll Animation
- Focus Animation
- Transition

---

### [실무]

작성 기준:

- `prefers-reduced-motion` 설정 존중
- 필수 아닌 애니메이션은 줄이거나 제거 가능
- 자동 재생 carousel은 일시정지 제공
- 빠르게 깜빡이는 콘텐츠 금지
- parallax / zoom / large motion은 reduced motion에서 제거
- skeleton shimmer도 과도하지 않게 설계
- focus 이동을 방해하는 animation 지양
- 중요한 상태 변화는 animation만으로 전달하지 않기
- loading animation에는 텍스트 상태 제공
- 사용자가 제어할 수 없는 반복 motion 지양

예시:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms;
    transition-duration: 0.01ms;
    scroll-behavior: auto;
  }
}
```

---

### [FAQ]

Q. Reduced Motion은 왜 필요한가?

A.
움직임에 민감한 사용자가 멀미, 어지러움, 집중 방해를 겪지 않도록 하기 위해 필요하다.

Q. Carousel은 접근성에 문제가 많나?

A.
그럴 수 있다. 자동 재생, focus 이동, screen reader 알림, pause control을 신중히 설계해야 한다.

Q. 애니메이션을 전부 없애야 하나?

A.
아니다. 사용자의 reduced motion 설정을 존중하고 불필요하거나 큰 움직임을 줄이면 된다.

---

# 22. Responsive / Zoom / Touch Accessibility Rules

## 22.1 반응형 / 확대 / 터치 접근성

### [개념]

Responsive Accessibility는 화면 크기, 확대 비율, 터치 입력, 모바일 브라우저에서도 콘텐츠와 기능을 사용할 수 있게 하는 기준이다.

---

### [핵심]

검토 대상:

- 200% Zoom
- 400% Reflow
- Responsive Layout
- Touch Target
- Pointer Target
- Orientation
- Text Scaling
- Mobile Keyboard
- Horizontal Scroll
- Sticky Header
- Viewport Unit
- Safe Area

---

### [실무]

작성 기준:

- 200% zoom에서 텍스트와 기능 사용 가능
- 작은 화면에서 가로 스크롤 최소화
- touch target 크기와 간격 확보
- 모바일 keyboard가 input을 가리지 않게 확인
- orientation 고정 지양
- text scaling에 레이아웃이 깨지지 않게 설계
- sticky header가 content / focus를 가리지 않게 처리
- viewport height 사용 시 모바일 주소창 변화 고려
- responsive nav도 keyboard / screen reader 접근 가능해야 함
- table은 작은 화면 대체 표현 검토

주의:

- hover-only interaction은 touch에서 동작하지 않음
- 너무 작은 icon button은 터치하기 어려움
- zoom 시 fixed layout은 콘텐츠 겹침 원인
- sticky footer / header가 focus target을 가릴 수 있음
- 모바일에서 modal focus와 scroll lock을 테스트해야 함

---

### [FAQ]

Q. 확대해서도 접근성을 확인해야 하나?

A.
그렇다. 사용자가 브라우저 zoom이나 OS 글자 크기를 키워도 콘텐츠와 기능을 사용할 수 있어야 한다.

Q. Touch target은 왜 중요한가?

A.
작은 버튼이나 링크는 터치하기 어렵고 오작동을 유발할 수 있기 때문이다.

Q. Hover interaction은 모바일에서 문제가 되나?

A.
그렇다. 터치 환경에서는 hover가 없으므로 focus, click, visible control 대안이 필요하다.

---

# 23. Screen Reader UX Rules

## 23.1 Screen Reader 사용자 경험

### [개념]

Screen Reader UX는 보조 기술 사용자가 페이지 구조, 버튼, 링크, Form, 상태 변화, 오류 메시지를 이해하고 조작할 수 있도록 설계하는 기준이다.

---

### [핵심]

검토 대상:

- Reading Order
- Accessible Name
- Landmark Navigation
- Heading Navigation
- Form Label
- Error Announcement
- Live Region
- Button State
- Link Purpose
- Hidden Text
- Decorative Content
- Dynamic Update

---

### [실무]

작성 기준:

- 읽기 순서가 시각적 순서와 논리적으로 일치
- heading으로 주요 구조 탐색 가능
- link text만 들어도 목적 이해 가능
- button name이 action을 설명
- Form field label과 error 연결
- 상태 변화는 live region으로 전달
- 장식 아이콘은 screen reader에서 숨김
- 시각적으로 숨긴 텍스트는 접근 가능한 방식으로 숨김
- screen reader 전용 텍스트 남용 금지
- 실제 screen reader 수동 테스트 포함

주의:

- CSS order로 시각 순서만 바꾸면 읽기 순서와 불일치 가능
- `aria-label`이 visible text와 다르면 혼란 가능
- `display: none`은 screen reader에서도 숨김
- offscreen hidden class는 focusable element에 신중히 사용
- 너무 많은 live announcement는 사용자를 방해함

---

### [FAQ]

Q. Screen Reader 테스트는 꼭 해야 하나?

A.
자동 도구로 잡히지 않는 읽기 순서, 상태 알림, 상호작용 문제를 확인하기 위해 필요하다.

Q. 링크 텍스트는 어떻게 작성해야 하나?

A.
링크 텍스트만 들어도 어디로 이동하는지 이해할 수 있어야 한다.

Q. 시각적으로 숨긴 텍스트는 screen reader가 읽을 수 있나?

A.
CSS 방식에 따라 다르다. 접근 가능한 visually-hidden 패턴을 사용해야 한다.

---

# 24. React Accessibility Rules

## 24.1 React 컴포넌트 접근성

### [개념]

React Accessibility는 컴포넌트 단위로 semantic, keyboard, focus, ARIA, 상태 전달을 안정적으로 구현하는 기준이다.

---

### [핵심]

검토 대상:

- Component API
- Prop-driven Accessibility
- Accessible Name Prop
- Ref Forwarding
- Focus Control
- Portal
- Conditional Rendering
- Hydration
- Error State
- Loading State
- Composition
- Custom Hook

---

### [실무]

작성 기준:

- 공통 컴포넌트는 accessible name 제공 방식을 설계
- icon-only component는 label prop 요구
- Modal / Popover는 ref와 focus 관리 필요
- Portal 사용 시 focus trap과 DOM order 검토
- 조건부 렌더링 시 focus가 사라지지 않게 관리
- loading 상태가 보조 기술에 전달되게 처리
- error state prop과 aria 연결을 컴포넌트 API에 포함
- wrapper component가 native prop을 누락하지 않게 설계
- `as` polymorphic component는 semantic 변경에 따른 접근성 책임 명시
- `forwardRef` 또는 ref 전달은 focus 관리에 필요할 수 있음

예시:

```tsx
type IconButtonProps = {
  label: string;
  onClick: () => void;
  children: React.ReactNode;
};

function IconButton({ label, onClick, children }: IconButtonProps) {
  return (
    <button type="button" aria-label={label} onClick={onClick}>
      <span aria-hidden="true">{children}</span>
    </button>
  );
}
```

---

### [FAQ]

Q. React 컴포넌트에서 접근성을 어디에 넣어야 하나?

A.
개별 화면에서 임시로 처리하기보다 공통 컴포넌트 API에 label, error, description, focus 기준을 포함하는 것이 좋다.

Q. Portal은 접근성 문제가 있나?

A.
가능하다. DOM 위치가 바뀌므로 focus trap, focus return, screen reader 탐색을 검토해야 한다.

Q. Polymorphic 컴포넌트는 접근성에 위험한가?

A.
잘못된 element로 렌더링되면 semantic과 keyboard 동작이 깨질 수 있으므로 주의가 필요하다.

---

# 25. Next.js Accessibility Rules

## 25.1 Next.js App Router 접근성

### [개념]

Next.js Accessibility는 App Router 환경에서 route 이동, layout, loading, error, metadata, Server / Client Component 경계가 접근성에 미치는 영향을 관리하는 기준이다.

---

### [핵심]

검토 대상:

- Route Change Focus
- Layout Landmark
- `loading.tsx`
- `error.tsx`
- `not-found.tsx`
- Metadata
- Server Component
- Client Component
- Link Navigation
- Image Alt
- Streaming
- Suspense
- Skip Link
- Dynamic Route
- Hydration

---

### [실무]

작성 기준:

- route 변경 후 main heading focus 또는 skip link 흐름 검토
- layout에 중복 landmark가 과도하지 않게 관리
- `loading.tsx`는 loading 상태를 명확히 전달
- `error.tsx`는 안전하고 복구 가능한 UI 제공
- `not-found.tsx`는 명확한 안내와 navigation 제공
- `next/link`는 목적이 명확한 link text 사용
- `next/image` alt 기준 준수
- Streaming / Suspense fallback이 screen reader에 혼란을 주지 않게 구성
- Server Component에서 semantic 구조 유지
- Client Component에서 focus / interaction 관리

주의:

- route 이동 후 focus가 body에 남으면 keyboard / screen reader 사용자가 맥락을 잃을 수 있음
- loading skeleton만 있고 상태 텍스트가 없으면 보조 기술 사용자에게 불친절
- Error 페이지가 원인 없이 “오류”만 표시하면 복구가 어려움
- 동적 title / metadata는 페이지 맥락 이해에 중요
- server / client boundary 때문에 focus 제어 위치가 달라질 수 있음

---

### [FAQ]

Q. Next.js에서 route 변경 후 focus 관리는 왜 필요한가?

A.
SPA처럼 화면이 바뀌어도 focus가 이전 위치에 남을 수 있어 screen reader와 keyboard 사용자가 새 페이지 맥락을 놓칠 수 있기 때문이다.

Q. `loading.tsx`도 접근성을 고려해야 하나?

A.
그렇다. Loading 상태가 시각적으로만 표시되지 않고 보조 기술에도 이해 가능해야 한다.

Q. `not-found.tsx`는 어떻게 작성해야 하나?

A.
페이지를 찾을 수 없다는 명확한 heading과 설명, 돌아갈 수 있는 navigation을 제공해야 한다.

---

# 26. Design System Accessibility Rules

## 26.1 Design System 접근성 기준

### [개념]

Design System Accessibility는 공통 컴포넌트가 기본적으로 접근성 요구사항을 충족하도록 API, 상태, keyboard, ARIA, focus, 테스트 기준을 내장하는 전략이다.

---

### [핵심]

우선 컴포넌트:

- Button
- IconButton
- Link
- Input
- Select
- Checkbox
- Radio
- Switch
- FormField
- Modal
- Dialog
- Tooltip
- Popover
- Dropdown
- Tabs
- Accordion
- Toast
- Alert
- Table
- Pagination

---

### [실무]

작성 기준:

- 컴포넌트별 accessibility contract 정의
- IconButton은 label 필수
- FormField는 label / description / error 연결 제공
- Modal은 focus trap / return 내장
- Toast는 live region 지원
- Tabs / Accordion은 keyboard pattern 포함
- Select / Combobox는 native 우선, custom이면 ARIA pattern 준수
- Variant / Size가 접근성 기준을 깨지 않게 관리
- Disabled / Loading / Error 상태 접근성 포함
- Storybook에서 accessibility test 연결 가능
- Design Token에서 contrast 기준 관리

예시 Component Contract:

```text
IconButton
- label 필수
- icon은 aria-hidden
- keyboard focus 가능
- disabled 상태 지원
- focus visible 스타일 필수
```

---

### [FAQ]

Q. Design System에서 접근성을 왜 먼저 넣어야 하나?

A.
공통 컴포넌트가 여러 화면에서 재사용되므로 기본 접근성이 깨지면 전체 제품에 문제가 확산되기 때문이다.

Q. IconButton label을 필수로 해야 하나?

A.
그렇다. 아이콘만으로는 screen reader가 목적을 알 수 없으므로 accessible name이 필요하다.

Q. Custom Select는 만들면 안 되나?

A.
만들 수 있지만 keyboard, focus, ARIA, screen reader 동작을 모두 구현해야 하므로 native select를 먼저 검토한다.

---

# 27. Accessibility Testing Rules

## 27.1 접근성 테스트 기준

### [개념]

Accessibility Testing은 자동 도구와 수동 검증을 함께 사용해 semantic, keyboard, focus, screen reader, color contrast, form error, dialog 동작을 확인하는 과정이다.

---

### [핵심]

테스트 유형:

- Automated A11y Test
- Keyboard Manual Test
- Screen Reader Test
- Color Contrast Test
- Focus Order Test
- Zoom Test
- Reduced Motion Test
- Component Test
- E2E Accessibility Test
- Visual Regression Test

---

### [실무]

작성 기준:

- 자동 접근성 테스트는 기본 오류 탐지용
- keyboard-only 테스트 필수
- focus visible / focus order 수동 확인
- screen reader로 핵심 flow 테스트
- Form validation error 테스트
- Modal focus trap / return 테스트
- Color contrast 도구 검증
- 200% zoom / 작은 화면 테스트
- reduced motion 설정 테스트
- Design System 컴포넌트는 접근성 테스트 기본 포함
- CI에 자동 a11y smoke test 연결 가능

테스트 체크:

```text
키보드만으로 로그인할 수 있는가?
Form 오류를 이해할 수 있는가?
Modal을 열고 닫은 뒤 focus가 돌아오는가?
Screen reader가 버튼 이름을 읽는가?
색상 없이 상태를 이해할 수 있는가?
```

---

### [FAQ]

Q. 자동 접근성 테스트만으로 충분한가?

A.
아니다. 자동 도구는 일부 문제만 잡는다. Keyboard, focus, screen reader 수동 테스트가 필요하다.

Q. 접근성 테스트는 언제 해야 하나?

A.
공통 컴포넌트 제작 시, 핵심 사용자 flow 개발 시, 배포 전 regression test에서 해야 한다.

Q. CI에 접근성 테스트를 넣을 수 있나?

A.
가능하다. 단, 자동 테스트 한계를 이해하고 수동 테스트와 병행해야 한다.

---

# 28. Troubleshooting Rules

## 28.1 자주 발생하는 접근성 문제

### [개념]

Troubleshooting 문서는 Agent가 Accessibility 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- 키보드로 버튼에 접근 불가
- Focus outline이 안 보임
- Modal 닫은 후 focus 사라짐
- Tab 순서가 이상함
- Screen reader가 버튼 이름을 읽지 않음
- Form error를 읽지 않음
- Placeholder가 label 역할을 못함
- Dropdown이 keyboard로 안 열림
- Tooltip이 keyboard에서 안 보임
- Toast를 screen reader가 읽지 않음
- 색상만으로 오류 표시
- Icon-only button 이름 없음
- `aria-hidden` 요소가 focus됨
- Custom select가 screen reader에서 깨짐
- route 변경 후 focus가 이전 위치에 남음
- reduced motion 설정 무시
- 200% zoom에서 레이아웃 깨짐

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- Screen reader가 아이콘 버튼의 목적을 읽지 못함

원인:

- 버튼 내부에 아이콘만 있음
- accessible name 없음
- 아이콘 자체도 의미 없는 SVG로만 존재

해결:

- button에 aria-label 추가
- 아이콘은 aria-hidden 처리
- 버튼 목적을 명확한 동사로 작성
```

예시:

```md
문제:

- Modal을 닫은 후 focus가 사라짐

원인:

- Modal을 열었던 trigger를 저장하지 않음
- 닫힘 시 focus return 로직 없음
- trigger가 unmount됨

해결:

- Modal open 시 trigger ref 저장
- close 후 trigger로 focus 복귀
- trigger가 사라질 수 있으면 대체 focus target 지정
```

예시:

```md
문제:

- Form error를 screen reader가 읽지 않음

원인:

- error message가 input과 연결되지 않음
- aria-describedby 누락
- aria-invalid 누락
- 제출 실패 후 focus 이동 없음

해결:

- error message에 id 부여
- input의 aria-describedby와 연결
- invalid 상태에 aria-invalid 설정
- 제출 실패 시 첫 오류 field 또는 error summary로 focus 이동
```

---

### [FAQ]

Q. 키보드로 조작이 안 되는 UI는 무엇을 확인해야 하나?

A.
native button / link 사용 여부, tab focus 가능 여부, key interaction, focus visible, disabled 처리 여부를 확인한다.

Q. Screen reader가 이름을 읽지 않으면 무엇을 확인하나?

A.
visible text, label, aria-label, aria-labelledby, alt, hidden 처리 여부를 확인한다.

Q. Focus가 사라지면 무엇을 봐야 하나?

A.
조건부 렌더링, modal 닫힘, route 변경, hidden 요소 focus, trigger unmount 여부를 확인한다.

---

# 29. Code Example Rules

## 29.1 코드 예제 작성 기준

### [개념]

Frontend Accessibility Advanced 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript / React 우선
- Semantic HTML 우선
- ARIA는 필요한 경우만 사용
- Keyboard 접근 가능해야 함
- Focus 관리 기준 포함 가능
- Form label / error 연결 예제 포함 권장
- Modal focus 기준 포함 권장
- 긴 전체 파일 금지
- 시각 스타일만 보여주는 예제 금지
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Accessible Button
- Icon Button
- Form Field
- Error Message
- Dialog
- Dropdown Trigger
- Accordion
- Live Region
- Skip Link
- Focus Return
- Reduced Motion CSS
- Accessible Image
- Tabs
- Toast Announcement
- Accessibility Test

금지 예제:

- `div` onClick button
- focus outline 제거 후 대체 없음
- label 없는 input
- placeholder-only form
- `aria-hidden`이 focus 가능한 요소에 적용된 예제
- keyboard 동작 없는 `role="button"`
- 이름 없는 icon button
- focus trap 없는 modal
- 색상만으로 error 전달
- tooltip에 중요한 정보만 넣는 예제

---

### [FAQ]

Q. Accessibility 코드 예제는 어떤 기준이어야 하나?

A.
Semantic HTML을 우선하고, keyboard / focus / accessible name / error 연결이 명확한 짧은 예제여야 한다.

Q. ARIA 예제를 많이 넣어도 되나?

A.
필요할 때만 넣는다. native HTML로 해결 가능한 경우 ARIA 예제를 남용하지 않는다.

---

# 30. Comparison Rules

## 30.1 필수 비교 대상

### [개념]

Frontend Accessibility Advanced 문서는 Agent의 접근성 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Native HTML vs ARIA
- Button vs Link
- Label vs Placeholder
- `aria-label` vs `aria-labelledby`
- `aria-describedby` vs Help Text
- `aria-hidden` vs visually hidden
- Modal vs Popover vs Tooltip
- Menu vs Navigation
- Tabs vs Accordion
- Disabled vs Readonly
- Hidden vs Visually Hidden
- Color Contrast vs Color-only Meaning
- Automated Test vs Manual Test
- Keyboard Test vs Screen Reader Test
- Skeleton vs Spinner
- Toast vs Inline Error
- Focus Trap vs Focus Return
- Native Select vs Custom Combobox

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 장점 / 위험 / 적합 상황 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Native HTML과 ARIA 중 무엇이 우선인가?

A.
Native HTML이 우선이다. ARIA는 native HTML로 의미와 상태를 표현하기 어려울 때 보완적으로 사용한다.

Q. Button과 Link는 어떻게 구분하나?

A.
동작 실행은 button, 페이지나 위치 이동은 link를 사용한다.

Q. Label과 Placeholder는 같은 역할인가?

A.
아니다. Placeholder는 입력 예시나 힌트이고, label은 field의 이름이다.

---

# 31. Checklist Rules

## 31.1 문서 품질 체크리스트

### [개념]

Frontend Accessibility Advanced RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Accessibility Advanced 목적이 명확한가?
- [ ] Semantic HTML 우선 원칙을 포함했는가?
- [ ] Landmark / Heading 구조 기준을 포함했는가?
- [ ] Keyboard Navigation 기준을 포함했는가?
- [ ] Focus Management 기준을 포함했는가?
- [ ] Accessible Name / Description 기준을 포함했는가?
- [ ] ARIA 사용 기준을 포함했는가?
- [ ] Button / Link 구분 기준을 포함했는가?
- [ ] Form Accessibility 기준을 포함했는가?
- [ ] Error Message 접근성 기준을 포함했는가?
- [ ] Dialog / Modal 접근성 기준을 포함했는가?
- [ ] Menu / Dropdown / Popover 기준을 포함했는가?
- [ ] Tabs / Accordion 기준을 포함했는가?
- [ ] Tooltip 기준을 포함했는가?
- [ ] Live Region 기준을 포함했는가?
- [ ] Image / Icon 접근성 기준을 포함했는가?
- [ ] Color Contrast 기준을 포함했는가?
- [ ] Motion / Reduced Motion 기준을 포함했는가?
- [ ] Responsive / Zoom / Touch 접근성 기준을 포함했는가?
- [ ] Screen Reader UX 기준을 포함했는가?
- [ ] React / Next.js 접근성 기준을 포함했는가?
- [ ] Design System 접근성 기준을 포함했는가?
- [ ] Accessibility Testing 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Design System / Testing / Frontend Architecture 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- 접근성 문서는 규칙 나열보다 실무 판단 기준 중심으로 작성
- Design System / Testing / Next.js / Security 문서와 연계 가능해야 함

---

### [FAQ]

Q. Frontend Accessibility 문서 품질에서 가장 중요한 것은?

A.
Semantic HTML, Keyboard, Focus, Form Error, ARIA, Dialog, Screen Reader, Testing 기준이 명확해야 한다.

---

# 32. Retrieval Optimization Rules

## 32.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Accessibility
- Accessibility Advanced
- A11y
- WCAG
- Semantic HTML
- Keyboard Navigation
- Focus Management
- Focus Trap
- Focus Return
- Focus Visible
- Accessible Name
- Accessible Description
- ARIA
- ARIA Role
- `aria-label`
- `aria-labelledby`
- `aria-describedby`
- `aria-expanded`
- `aria-invalid`
- `aria-live`
- Screen Reader
- Form Accessibility
- Error Message Accessibility
- Dialog Accessibility
- Modal Accessibility
- Dropdown Accessibility
- Tooltip Accessibility
- Live Region
- Button vs Link
- Label vs Placeholder
- Image Alt
- Icon Button
- Color Contrast
- Reduced Motion
- Responsive Accessibility
- Touch Target
- Design System Accessibility
- React Accessibility
- Next.js Accessibility
- Accessibility Testing
- Keyboard Test
- Screen Reader Test

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Frontend Accessibility는 뭐야?
- 접근성은 왜 필요해?
- Semantic HTML이 왜 중요해?
- div onClick 버튼으로 써도 돼?
- Button과 Link 차이
- 키보드 접근성 어떻게 확인해?
- focus outline 없애도 돼?
- Modal focus trap 어떻게 해?
- Modal 닫으면 focus 어디로 가?
- Accessible Name은 뭐야?
- aria-label 언제 써?
- aria-describedby 언제 써?
- ARIA는 언제 써야 해?
- placeholder를 label로 써도 돼?
- Form error screen reader가 읽게 하려면?
- Icon-only button 접근성
- Tooltip 접근성 어떻게 해?
- Toast screen reader가 읽게 하려면?
- 색상만으로 error 표시해도 돼?
- Reduced Motion은 어떻게 적용해?
- Screen Reader 테스트는 어떻게 해?
- Next.js route change focus 어떻게 해?
- Design System 접근성 기준
- 접근성 테스트는 어떻게 해?
- Accessibility 코드 리뷰 기준

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 33. Version Rules

## 33.1 기준 버전

### [개념]

Frontend Accessibility Advanced 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern HTML
- Modern CSS
- React 19+
- Next.js App Router
- TypeScript
- Semantic HTML
- ARIA 1.2+ 패턴 참고
- WCAG 실무 기준
- Keyboard-first UI
- Design System Accessibility
- Testing Library 접근성 query
- Automated + Manual Testing
- Screen Reader Testing
- Reduced Motion
- Responsive Accessibility

Legacy 제외:

- table layout 기반 접근성 설명
- `div` / `span` interactive control 기본 권장
- ARIA 남용
- placeholder-only form
- focus outline 제거 후 대체 없음
- mouse-only interaction
- hover-only content
- color-only status
- screen reader-only workaround 남용
- 접근성 테스트 없이 자동 도구만 신뢰
- 시각 디자인만 기준으로 semantic 무시

---

### [실무]

문서 작성 시 주의:

- 접근성은 도구보다 사용자 경험과 semantic 기준이 우선
- WCAG / ARIA 패턴은 최신 기준 확인 가능하게 작성
- React / Next.js 구현은 Server / Client Component 경계 고려
- Design System 컴포넌트 단위 접근성 계약을 강조
- Testing 문서와 접근성 테스트 기준을 연결
- Security / Privacy와 충돌하지 않게 live region / error message / log 정보 주의
- 과도한 ARIA 예제보다 native HTML 예제 우선

---

### [FAQ]

Q. 접근성 문서는 최신성이 중요한가?

A.
중요하다. 브라우저, 보조 기술, ARIA 패턴, 프레임워크 구현 방식은 변할 수 있으므로 최신 기준을 확인해야 한다.

Q. 특정 screen reader 기준으로만 작성해도 되나?

A.
아니다. 가능한 한 일반 원칙을 기준으로 작성하고, 주요 screen reader에서 수동 테스트를 병행하는 것이 좋다.

---

# 34. Common Mistakes

## 34.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Accessibility 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- `div` / `span`을 button처럼 사용
- 페이지 이동을 button으로 처리
- focus outline 제거
- keyboard interaction 누락
- hover에서만 표시되는 메뉴
- label 없는 input
- placeholder를 label로 사용
- error message와 input 연결 누락
- icon-only button에 accessible name 없음
- `aria-hidden`이 focus 가능한 요소에 적용됨
- ARIA role만 붙이고 keyboard 동작 구현 누락
- Modal focus trap 누락
- Modal 닫힘 후 focus return 누락
- Tooltip에 중요한 정보를 넣음
- Toast가 screen reader에 전달되지 않음
- 색상만으로 오류 / 성공 상태 표시
- 이미지 alt 누락 또는 불필요한 alt
- Heading 구조가 시각 스타일 기준으로 뒤섞임
- route 변경 후 focus 관리 없음
- reduced motion 무시
- 200% zoom에서 레이아웃 깨짐
- 자동 접근성 테스트만 믿음
- Design System 컴포넌트에 접근성 contract 없음

---

### [실무]

리뷰 기준:

- Semantic HTML 사용 여부 확인
- Keyboard-only 사용 가능 여부 확인
- Focus visible / trap / return 확인
- Accessible name 확인
- Form label / error 연결 확인
- ARIA 역할과 동작 일치 확인
- Modal / Dropdown keyboard interaction 확인
- Live region 상태 전달 확인
- Image / Icon alt 기준 확인
- Color contrast와 color-only meaning 확인
- Reduced motion 지원 확인
- Zoom / responsive 접근성 확인
- Screen reader 수동 테스트 여부 확인
- Automated a11y test 결과 확인

---

### [FAQ]

Q. Frontend Accessibility에서 가장 흔한 실수는?

A.
Semantic HTML을 무시하고 `div`에 click handler를 붙여 interactive UI를 만드는 것이다.

Q. ARIA 관련 가장 흔한 실수는?

A.
role이나 aria 속성만 붙이고 실제 keyboard 동작과 상태 갱신을 구현하지 않는 것이다.

Q. Form 접근성에서 가장 흔한 실수는?

A.
label이 없거나 error message가 input과 연결되지 않는 것이다.

---

# 35. Final Goal

## 35.1 최종 목표

### [개념]

Frontend Accessibility Advanced RAG 문서는 Agent가 프론트엔드 프로젝트에서 접근성 있는 UI를 설계, 생성, 검토, 개선할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Semantic HTML 기준 제안
- Landmark / Heading 구조 리뷰
- Keyboard Navigation 리뷰
- Focus Management 설계
- Accessible Name / Description 검토
- ARIA 사용 적절성 판단
- Button / Link semantic 판단
- Form Accessibility 설계
- Error Message 접근성 설계
- Dialog / Modal 접근성 리뷰
- Dropdown / Popover 접근성 리뷰
- Tabs / Accordion 접근성 리뷰
- Tooltip 접근성 리뷰
- Live Region 설계
- Image / Icon 접근성 리뷰
- Color Contrast 기준 제안
- Reduced Motion 기준 제안
- Responsive / Zoom / Touch 접근성 검토
- Screen Reader UX 개선
- React / Next.js 접근성 리뷰
- Design System Accessibility Contract 설계
- Accessibility Testing 기준 제안
- 접근성 Troubleshooting
- Accessibility 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Semantic HTML / Keyboard / Focus / ARIA / Form / Dialog 기준 명확화
- Design System / Testing / Next.js 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Accessibility Advanced Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 Semantic HTML, Keyboard, Focus, ARIA, Form, Dialog, Screen Reader, Testing 기준으로 접근성을 설계하고 코드 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Accessibility Advanced 문서는 어떤 기준으로 작성해야 해?

A.
Semantic HTML, Keyboard Navigation, Focus Management, ARIA, Form Error, Dialog, Screen Reader, Color Contrast, Testing 기준으로 작성해야 한다.

Q. Frontend Accessibility는 뭐야?

A.
사용자가 장애 여부, 입력 방식, 보조 기술, 기기 환경과 관계없이 웹 UI를 이해하고 조작할 수 있게 만드는 프론트엔드 설계 영역이다.

Q. 접근성은 왜 필요해?

A.
키보드 사용자, screen reader 사용자, 저시력 사용자, 모바일 사용자, 일시적 부상 사용자 등 다양한 환경의 사용자가 서비스를 사용할 수 있게 하기 위해 필요하다.

Q. Semantic HTML이 왜 중요해?

A.
HTML 요소 자체의 의미를 브라우저와 보조 기술이 이해할 수 있어 keyboard, screen reader, form 동작이 자연스럽게 지원되기 때문이다.

Q. div onClick 버튼으로 써도 돼?

A.
권장하지 않는다. 기본 keyboard 조작, focus, role이 부족하므로 native `button`을 사용해야 한다.

Q. Button과 Link 차이는?

A.
Button은 동작 실행에 사용하고, Link는 페이지나 위치 이동에 사용한다.

Q. 페이지 이동을 button으로 해도 돼?

A.
권장하지 않는다. 이동은 link semantic을 사용하는 것이 좋다.

Q. 키보드 접근성 어떻게 확인해?

A.
Tab, Shift+Tab, Enter, Space, Arrow Key, Escape만으로 주요 기능을 사용할 수 있는지 확인한다.

Q. focus outline 없애도 돼?

A.
기본 outline을 제거하려면 반드시 대체 focus visible 스타일을 제공해야 한다.

Q. Tab 순서가 이상하면 무엇을 확인해?

A.
DOM 순서, CSS order, 양수 tabIndex, hidden focusable element, portal 구조를 확인한다.

Q. Modal focus trap 어떻게 해?

A.
Modal이 열리면 focus를 내부로 이동시키고, Tab이 modal 내부에서 순환되게 하며, 닫히면 trigger로 focus를 복귀시킨다.

Q. Modal 닫으면 focus 어디로 가?

A.
Modal을 열었던 버튼이나 링크로 돌아가는 것이 좋다.

Q. Toast가 뜨면 focus를 이동해야 해?

A.
대부분 아니다. 사용자의 현재 focus는 유지하고 live region으로 상태를 알려주는 것이 좋다.

Q. Accessible Name은 뭐야?

A.
Screen reader가 버튼, 링크, 입력 필드의 이름으로 읽는 텍스트이다.

Q. aria-label 언제 써?

A.
화면에 보이는 텍스트가 없거나 icon-only button처럼 accessible name을 별도로 제공해야 할 때 사용한다.

Q. aria-labelledby는 언제 써?

A.
화면에 이미 존재하는 텍스트를 요소의 accessible name으로 연결할 때 사용한다.

Q. aria-describedby 언제 써?

A.
도움말, 설명, 오류 메시지처럼 요소에 대한 추가 설명을 연결할 때 사용한다.

Q. ARIA는 언제 써야 해?

A.
Native HTML로 의미와 상태를 표현하기 어려울 때 보조적으로 사용한다.

Q. role button 쓰면 버튼처럼 동작해?

A.
Screen reader에는 버튼처럼 알려질 수 있지만 keyboard 동작은 직접 구현해야 하므로 native `button`이 더 좋다.

Q. aria-hidden은 언제 써?

A.
장식 아이콘처럼 screen reader가 읽지 않아도 되는 요소를 숨길 때 사용한다.

Q. aria-hidden 요소가 focus되면 왜 문제야?

A.
Screen reader에서는 숨겨졌는데 keyboard focus는 이동해 사용자가 현재 위치를 이해하기 어려워진다.

Q. placeholder를 label로 써도 돼?

A.
권장하지 않는다. Placeholder는 입력 중 사라지고 field 이름과 오류 연결에 부족하다.

Q. Form label은 어떻게 연결해?

A.
`label`의 `htmlFor`와 input의 `id`를 연결하거나 label 내부에 input을 포함한다.

Q. Form error screen reader가 읽게 하려면?

A.
오류 메시지에 id를 주고 input의 `aria-describedby`로 연결하며 invalid 상태에는 `aria-invalid`를 사용할 수 있다.

Q. Required 필드는 별표만 표시하면 돼?

A.
별표만으로는 부족할 수 있다. “필수 입력”이라는 텍스트나 설명을 함께 제공하는 것이 좋다.

Q. Error message는 어떻게 작성해야 해?

A.
무엇이 문제인지, 어디를 고쳐야 하는지, 어떻게 고칠 수 있는지 구체적으로 알려줘야 한다.

Q. Toast로 Form 오류를 보여주면 충분해?

A.
중요한 Form 오류는 toast만으로 부족하다. 해당 field 근처와 error summary에 표시하는 것이 좋다.

Q. Dialog 접근성은 어떻게 해?

A.
Accessible name, initial focus, focus trap, Escape close, close button, focus return, background inert를 제공해야 한다.

Q. Modal 밖 배경은 keyboard로 접근 가능해도 돼?

A.
일반 modal에서는 안 된다. Modal이 열린 동안 focus는 modal 내부에 머물러야 한다.

Q. Dropdown trigger는 뭐로 만들어야 해?

A.
대부분 `button`이 적합하다. 열림 / 닫힘 동작을 수행하기 때문이다.

Q. aria-expanded는 언제 써?

A.
버튼이 dropdown, menu, accordion 같은 확장 영역을 열고 닫을 때 현재 상태를 전달하기 위해 사용한다.

Q. 모든 dropdown에 role menu 써야 해?

A.
아니다. 일반 navigation이나 선택 목록에는 더 적합한 semantic이 있을 수 있다.

Q. Accordion header는 div로 만들어도 돼?

A.
권장하지 않는다. 확장 / 축소 동작은 button으로 구현하는 것이 좋다.

Q. Tabs에서 선택 상태는 어떻게 전달해?

A.
선택된 tab에 `aria-selected`를 사용하고 tab과 tabpanel을 연결한다.

Q. Tooltip 접근성 어떻게 해?

A.
Hover뿐 아니라 focus에서도 표시하고, trigger와 tooltip을 `aria-describedby`로 연결하며, 중요한 정보는 tooltip에만 넣지 않는다.

Q. Tooltip 안에 버튼 넣어도 돼?

A.
권장하지 않는다. interactive content가 필요하면 popover나 dialog 패턴을 고려한다.

Q. Toast screen reader가 읽게 하려면?

A.
Toast 메시지를 `role="status"`나 적절한 live region에 넣어 전달할 수 있다.

Q. aria-live polite와 assertive 차이는?

A.
`polite`는 사용자의 현재 작업을 방해하지 않고 읽고, `assertive`는 긴급하게 알린다. `assertive`는 신중히 사용해야 한다.

Q. Icon-only button 접근성은 어떻게 해?

A.
버튼에 `aria-label` 또는 숨김 텍스트로 accessible name을 제공하고 아이콘은 `aria-hidden` 처리한다.

Q. 이미지 alt는 어떻게 써?

A.
의미 있는 이미지는 내용을 설명하고, 장식 이미지는 빈 alt로 보조 기술에서 무시되게 한다.

Q. Chart 이미지는 alt만으로 충분해?

A.
대부분 부족하다. 핵심 요약과 데이터 표 또는 상세 설명을 함께 제공하는 것이 좋다.

Q. 색상만으로 error 표시해도 돼?

A.
안 된다. 텍스트, 아이콘, aria 상태 등 색상 외 정보가 함께 필요하다.

Q. Dark Mode도 접근성 테스트해야 해?

A.
필요하다. Light Mode에서 충분한 대비가 Dark Mode에서도 유지된다는 보장은 없다.

Q. Focus indicator도 대비가 중요해?

A.
중요하다. 키보드 사용자가 현재 위치를 알아야 하므로 충분히 눈에 보여야 한다.

Q. Reduced Motion은 어떻게 적용해?

A.
`prefers-reduced-motion` 미디어 쿼리를 사용해 불필요한 애니메이션, 큰 움직임, 자동 전환을 줄인다.

Q. Carousel은 접근성에 문제가 많아?

A.
그럴 수 있다. 자동 재생, pause control, keyboard 조작, screen reader 알림을 신중히 설계해야 한다.

Q. 확대해서도 접근성 확인해야 해?

A.
그렇다. 브라우저 zoom이나 OS 글자 크기를 키워도 콘텐츠와 기능을 사용할 수 있어야 한다.

Q. Touch target은 왜 중요해?

A.
작은 버튼이나 링크는 터치하기 어렵고 오작동을 유발할 수 있기 때문이다.

Q. Hover interaction은 모바일에서 문제야?

A.
그렇다. 터치 환경에는 hover가 없으므로 focus, click, visible control 대안이 필요하다.

Q. Screen Reader 테스트는 어떻게 해?

A.
주요 flow를 screen reader로 탐색하며 heading, landmark, link, button name, form label, error message, live update를 확인한다.

Q. 링크 텍스트는 어떻게 작성해야 해?

A.
링크 텍스트만 들어도 어디로 이동하는지 이해할 수 있어야 한다.

Q. visually hidden은 언제 써?

A.
시각적으로는 숨기지만 screen reader에는 필요한 텍스트를 제공할 때 사용한다.

Q. React 컴포넌트 접근성은 어디에 넣어야 해?

A.
공통 컴포넌트 API에 label, description, error, focus 기준을 포함하는 것이 좋다.

Q. Portal은 접근성 문제가 있어?

A.
가능하다. DOM 위치가 바뀌므로 focus trap, focus return, screen reader 탐색을 검토해야 한다.

Q. Next.js route change focus 어떻게 해?

A.
Route 변경 후 main heading이나 main 영역으로 focus를 이동하거나 skip link 흐름을 제공해 새 페이지 맥락을 전달한다.

Q. loading.tsx도 접근성 고려해야 해?

A.
그렇다. Loading 상태가 시각적으로만 표시되지 않고 보조 기술에도 이해 가능해야 한다.

Q. Design System 접근성 기준은 뭐야?

A.
공통 컴포넌트마다 accessible name, keyboard, focus, ARIA, error, loading, disabled 상태 기준을 contract로 정의하는 것이다.

Q. Custom Select 만들어도 돼?

A.
가능하지만 keyboard, focus, ARIA, screen reader 동작을 모두 구현해야 하므로 native select를 먼저 검토한다.

Q. 접근성 테스트는 어떻게 해?

A.
자동 a11y 테스트, keyboard-only 테스트, screen reader 테스트, color contrast 확인, zoom / reduced motion 테스트를 함께 수행한다.

Q. 자동 접근성 테스트만으로 충분해?

A.
아니다. 자동 도구는 일부 문제만 잡으므로 keyboard와 screen reader 수동 테스트가 필요하다.

Q. Accessibility 코드 리뷰 기준은?

A.
Semantic HTML, keyboard, focus, accessible name, form error, ARIA 적절성, modal / dropdown 동작, color contrast, reduced motion, testing 여부를 확인한다.

Q. Frontend Accessibility Advanced RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 Semantic HTML, Keyboard, Focus, ARIA, Form, Dialog, Screen Reader, Testing 기준으로 접근성을 설계하고 코드 리뷰하게 만드는 것이다.
