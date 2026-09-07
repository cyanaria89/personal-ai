# Frontend Accessibility Part10 - Final Checklist Agent Review Guide

---

# 1. Frontend Accessibility Final Guide

## 1.1 Final Review Purpose

### [개념]

Frontend Accessibility Final Review는 Semantic HTML, Form, Keyboard, Focus, ARIA, Image, Color, State Feedback, Component Pattern, Testing 기준을 통합적으로 검토하는 최종 점검 과정이다.

이 문서는 개별 접근성 지식을 다시 설명하는 문서가 아니라 AI Agent가 실제 Frontend 코드를 생성, 수정, 검토할 때 사용할 최종 판단 기준이다.

---

### [핵심]

Final Review 핵심 영역:

- Semantic HTML
- Landmark
- Heading
- Button / Link
- Form Label
- Required Field
- Error Message
- Keyboard Navigation
- Focus Visible
- Focus Management
- ARIA Role
- Accessible Name
- ARIA State
- Image Alt
- Icon Button
- Color Contrast
- State Feedback
- Component Pattern
- Testing Library
- Manual Review
- Regression Check

최종 판단 기준:

```text
사용자가 마우스 없이 조작할 수 있는가?
사용자가 화면을 보지 않아도 목적을 이해할 수 있는가?
사용자가 오류와 상태 변화를 이해할 수 있는가?
사용자가 다음 행동을 알 수 있는가?
테스트가 사용자 관점 Query로 작성되어 있는가?
```

---

### [실무]

최종 접근성 검토 Flow:

```text
HTML 의미 검토
→ Interactive Element 검토
→ Form 접근성 검토
→ Keyboard 조작 검토
→ Focus 흐름 검토
→ ARIA 정확성 검토
→ 이미지 / 아이콘 검토
→ 색상 / 시각 상태 검토
→ 상태 피드백 검토
→ 공통 Component 검토
→ Testing Library 검토
→ 수동 점검 항목 정리
```

실무 기준:

- 접근성은 마지막에 한 번 체크하는 항목이 아니라 Component 설계 단계부터 반영
- 공통 Component 문제는 높은 우선순위로 수정
- Form, Modal, Dropdown, Tab은 접근성 오류 빈도가 높으므로 집중 검토
- 자동화 테스트는 보조 수단이며 수동 keyboard 점검 필요
- Review Agent는 “동작함”이 아니라 “접근 가능하게 동작함”을 기준으로 판단

---

### [FAQ]

Q. Frontend Accessibility Final Review는 뭐야?
A. Semantic HTML, Keyboard, Focus, ARIA, Form, State, Component, Testing을 통합해서 최종 점검하는 과정이다.

Q. 접근성 검토에서 가장 중요한 질문은?
A. 마우스 없이 사용할 수 있는지, 보조기술 사용자가 의미와 상태를 이해할 수 있는지 확인하는 것이다.

Q. 접근성은 개발 마지막에만 확인하면 돼?
A. 아니다. 공통 Component와 Form 설계 단계에서 반영해야 반복 오류를 줄일 수 있다.

Q. 자동 테스트만 통과하면 Final Review 완료야?
A. 아니다. keyboard, focus visible, 문구 품질, 색상 의미는 수동 검토가 필요하다.

---

# 2. Semantic HTML Final Checklist

## 2.1 Semantic HTML Review

### [개념]

Semantic HTML Review는 HTML 요소가 의미에 맞게 사용되었는지 확인하는 최종 점검이다.

접근성의 기본은 ARIA가 아니라 올바른 HTML 구조다.

---

### [핵심]

Checklist:

```md
- [ ] 클릭 action에 button을 사용했는가?
- [ ] 페이지 / route 이동에 Link 또는 a를 사용했는가?
- [ ] div onClick / span onClick 남용이 없는가?
- [ ] button에 type이 명시되었는가?
- [ ] Form 내부 일반 button은 type="button"인가?
- [ ] submit button만 type="submit"인가?
- [ ] 페이지 주요 콘텐츠가 main 안에 있는가?
- [ ] nav가 주요 탐색 영역에 사용되었는가?
- [ ] nav가 여러 개면 aria-label로 구분했는가?
- [ ] 페이지에 명확한 h1이 있는가?
- [ ] heading level이 자연스러운가?
- [ ] 반복 콘텐츠가 list 구조로 표현되었는가?
- [ ] 독립 콘텐츠 card에 article 사용을 검토했는가?
- [ ] 표 데이터에 table을 사용했는가?
- [ ] layout 목적 table을 사용하지 않았는가?
```

---

### [실무]

우선 수정 대상:

```text
div onClick
span onClick
a href="#" + onClick
button type 누락
h1 누락
heading level jump
table data를 div grid로 구현
```

수정 예:

```jsx
<button type="button" onClick={onOpen}>
  메뉴 열기
</button>
```

```jsx
<Link to={`/festivals/${festival.id}`}>{festival.title} 상세 보기</Link>
```

Review Agent 기준:

- Native Element로 해결 가능한 곳에 role을 붙인 custom element가 있으면 수정 제안
- action과 navigation이 섞여 있으면 역할 분리 제안
- DOM 구조와 시각적 구조가 지나치게 다르면 keyboard 순서 검토 요청
- Semantic HTML 문제는 접근성 테스트 실패의 근본 원인으로 분류

---

### [FAQ]

Q. Semantic HTML 최종 검토에서 가장 먼저 볼 것은?
A. Button / Link 역할 구분, main/nav 구조, h1과 heading 계층을 먼저 본다.

Q. div onClick은 무조건 수정 대상이야?
A. 대부분 우선 수정 대상이다. 가능하면 button이나 Link로 대체한다.

Q. ARIA를 붙이면 Semantic HTML 문제를 해결할 수 있어?
A. 일부 보완은 가능하지만 Native HTML을 먼저 사용하는 것이 원칙이다.

Q. table 데이터는 div grid로 만들어도 돼?
A. 행과 열 관계가 중요한 데이터는 table을 사용하는 것이 좋다.

---

# 3. Form Accessibility Final Checklist

## 3.1 Form Review

### [개념]

Form Accessibility Review는 사용자가 입력 필드의 목적, 필수 여부, 오류 원인, 수정 방법을 이해하고 Form을 완료할 수 있는지 확인하는 최종 점검이다.

Form 접근성은 label, helper text, error message, focus, validation 상태가 함께 맞아야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 모든 주요 input에 label이 연결되었는가?
- [ ] label htmlFor와 input id가 일치하는가?
- [ ] input id가 중복되지 않는가?
- [ ] placeholder를 label 대체로 사용하지 않았는가?
- [ ] select에 label이 연결되었는가?
- [ ] textarea에 label이 연결되었는가?
- [ ] checkbox / radio에 label이 연결되었는가?
- [ ] radio group에 fieldset / legend를 고려했는가?
- [ ] checkbox group에 fieldset / legend를 고려했는가?
- [ ] required field가 명확히 표시되었는가?
- [ ] 별표 사용 시 의미 설명이 있는가?
- [ ] helper text가 aria-describedby로 연결되었는가?
- [ ] error message가 aria-describedby로 연결되었는가?
- [ ] aria-invalid가 실제 error 상태와 일치하는가?
- [ ] field error와 global error를 구분했는가?
- [ ] submit 실패 시 focus 이동 기준을 검토했는가?
- [ ] Error Summary가 필요한 Form인지 검토했는가?
```

---

### [실무]

Form 기본 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
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

Group 예:

```jsx
<fieldset aria-describedby={error ? "payment-error" : undefined}>
  <legend>결제 수단</legend>

  <label>
    <input type="radio" name="paymentMethod" value="card" />
    카드
  </label>

  {error && (
    <p id="payment-error" role="alert">
      결제 수단을 선택해 주세요.
    </p>
  )}
</fieldset>
```

Review Agent 기준:

- `placeholder`만 있는 input은 label 누락으로 분류
- `aria-invalid`만 있고 error text가 없으면 수정 제안
- error message id와 `aria-describedby` 참조가 불일치하면 오류로 분류
- 긴 Form에서 error가 여러 개면 Error Summary 제안
- 로그인 실패는 보안상 global error로 처리 가능

---

### [FAQ]

Q. Form 최종 검토에서 가장 먼저 볼 것은?
A. label 연결, placeholder-only 여부, error message 연결, aria-invalid 상태를 먼저 본다.

Q. placeholder가 있으면 label은 생략해도 돼?
A. 권장하지 않는다. placeholder는 label 대체가 아니다.

Q. error message는 input과 꼭 연결해야 해?
A. 권장한다. aria-describedby로 연결하면 보조기술 사용자가 오류를 이해하기 쉽다.

Q. fieldset과 legend는 언제 필요해?
A. radio group, checkbox group처럼 여러 control이 하나의 질문에 속할 때 사용한다.

---

# 4. Keyboard and Focus Final Checklist

## 4.1 Keyboard Review

### [개념]

Keyboard Review는 마우스 없이 keyboard만으로 주요 기능을 사용할 수 있는지 확인하는 최종 점검이다.

Keyboard 접근성은 자동화 테스트만으로 충분하지 않으며 실제 Tab 이동과 focus 흐름을 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 마우스 없이 주요 user flow를 완료할 수 있는가?
- [ ] 모든 clickable element가 keyboard focus 가능한가?
- [ ] button은 Enter / Space로 실행되는가?
- [ ] link는 Enter로 이동하는가?
- [ ] checkbox는 Space로 toggle 가능한가?
- [ ] radio group은 keyboard로 선택 가능한가?
- [ ] Dropdown / Modal / Popover가 Escape로 닫히는가?
- [ ] Tab Order가 시각적 흐름과 자연스러운가?
- [ ] 양수 tabindex를 사용하지 않았는가?
- [ ] hidden element에 focus가 가지 않는가?
- [ ] keyboard trap이 없는가?
- [ ] custom widget에 필요한 keyboard pattern이 구현되었는가?
```

---

### [실무]

Manual Keyboard Flow:

```text
마우스 사용 금지
→ Tab 이동
→ Shift+Tab 역방향 이동
→ Enter 실행
→ Space 실행
→ Escape 닫기
→ Arrow Key 필요 Component 확인
→ Focus Lost / Keyboard Trap 확인
```

우선 점검 대상:

```text
Login
Signup
Search
Payment
Review Form
Modal
Dropdown
Tab
Accordion
File Upload
Pagination
Admin Table
```

Review Agent 기준:

- `tabIndex={0}`가 custom element에 붙어 있으면 keyboard activation 확인
- `tabIndex` 양수 사용은 수정 제안
- hidden dropdown item focus 가능성 확인
- route 이동 후 focus 정책이 필요한 경우 제안
- keyboard trap은 Critical 문제로 분류

---

### [FAQ]

Q. Keyboard 최종 검토에서 가장 중요한 것은?
A. 마우스 없이 핵심 기능을 완료할 수 있고 focus 위치가 명확히 보이는지 확인하는 것이다.

Q. keyboard test가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 실제 focus visible과 복잡한 흐름은 수동 확인이 필요하다.

Q. keyboard trap은 왜 심각해?
A. 사용자가 특정 영역에서 빠져나갈 수 없어 UI를 계속 사용할 수 없기 때문이다.

Q. custom widget은 왜 위험해?
A. role, keyboard, focus, ARIA state를 직접 구현해야 하므로 누락 가능성이 높다.

---

## 4.2 Focus Review

### [개념]

Focus Review는 keyboard focus가 현재 위치를 명확히 보여주고, Modal / Dropdown / Form Error / Route 이동 후 논리적으로 이동하는지 확인하는 최종 점검이다.

---

### [핵심]

Checklist:

```md
- [ ] 모든 interactive element에 focus visible이 있는가?
- [ ] outline none 후 대체 focus style이 있는가?
- [ ] focus ring이 충분히 보이는가?
- [ ] focus ring이 overflow로 잘리지 않는가?
- [ ] Modal open 시 focus가 내부로 이동하는가?
- [ ] Modal 내부 focus trap이 동작하는가?
- [ ] Modal close 시 trigger로 focus가 돌아가는가?
- [ ] Dropdown close 시 trigger로 focus가 돌아가는가?
- [ ] Form submit 실패 시 focus 이동 기준이 있는가?
- [ ] Error Summary focus가 필요한지 검토했는가?
- [ ] Route 변경 후 focus 위치를 검토했는가?
- [ ] 삭제된 요소에 focus가 남지 않는가?
```

---

### [실무]

Focus Style 예:

```css
:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

Focus Return 예:

```tsx
const triggerRef = useRef<HTMLButtonElement>(null);

function closeDialog() {
  setOpen(false);
  requestAnimationFrame(() => {
    triggerRef.current?.focus();
  });
}
```

Review Agent 기준:

- `outline: none`은 대체 focus style 없으면 오류로 분류
- Modal focus return 누락은 높은 우선순위
- focus visible이 디자인상 제거된 경우 대체 token 제안
- 동적 list 삭제 후 focus lost 가능성 검토
- focus 이동은 필요할 때만 제안하고 남발하지 않음

---

### [FAQ]

Q. Focus Review에서 가장 먼저 볼 것은?
A. focus visible이 모든 interactive element에 보이는지 확인한다.

Q. outline none은 무조건 문제야?
A. 대체 focus style 없이 제거하면 문제다.

Q. Modal close 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아간다.

Q. Form 오류 후 focus 이동은 항상 필요해?
A. 아니다. 긴 Form이나 오류를 찾기 어려운 경우 Error Summary 또는 첫 오류 field로 이동을 고려한다.

---

# 5. ARIA Final Checklist

## 5.1 ARIA Review

### [개념]

ARIA Review는 ARIA가 필요한 곳에만 정확히 사용되고 실제 UI 상태와 동기화되는지 확인하는 최종 점검이다.

ARIA는 Semantic HTML을 대체하지 않는다.

잘못된 ARIA는 없는 것보다 나쁠 수 있다.

---

### [핵심]

Checklist:

```md
- [ ] Native HTML로 대체 가능한 role 사용이 없는가?
- [ ] role과 실제 keyboard 동작이 일치하는가?
- [ ] interactive element에 accessible name이 있는가?
- [ ] icon only button에 aria-label이 있는가?
- [ ] aria-label과 visible text가 충돌하지 않는가?
- [ ] aria-labelledby 참조 id가 실제 DOM에 있는가?
- [ ] aria-describedby 참조 id가 실제 DOM에 있는가?
- [ ] aria-invalid가 실제 error 상태와 일치하는가?
- [ ] aria-expanded가 실제 open 상태와 일치하는가?
- [ ] aria-selected가 실제 selected 상태와 일치하는가?
- [ ] aria-current가 실제 현재 위치와 일치하는가?
- [ ] aria-busy가 실제 loading 상태와 일치하는가?
- [ ] aria-hidden 내부에 focus 가능한 요소가 없는가?
- [ ] role alert를 남발하지 않았는가?
- [ ] role status가 loading / success 상태에 적절히 사용되었는가?
- [ ] Dialog에 role, aria-modal, aria-labelledby가 있는가?
```

---

### [실무]

좋은 예:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="filter-panel"
  onClick={toggleOpen}
>
  필터
</button>
```

나쁜 예:

```jsx
<button type="button" aria-expanded="true" onClick={toggleOpen}>
  필터
</button>
```

IconButton 예:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

Review Agent 기준:

- ARIA state 하드코딩은 실제 state와 동기화하도록 수정 제안
- 없는 id를 참조하는 `aria-labelledby`, `aria-describedby`는 오류
- `aria-hidden="true"` 내부 interactive element는 Critical 문제
- `role="button"` 사용 시 Native button 전환 우선 제안
- `role="alert"` 남발은 상태 메시지 전략 재검토 제안

---

### [FAQ]

Q. ARIA 최종 검토에서 가장 중요한 것은?
A. ARIA가 실제 UI 상태와 동기화되는지, Native HTML로 대체 가능한지 확인하는 것이다.

Q. ARIA가 많으면 좋은 코드야?
A. 아니다. 필요한 ARIA만 정확히 사용하는 것이 좋다.

Q. aria-expanded는 어떻게 검토해?
A. 실제 open 상태와 값이 항상 일치하는지 확인한다.

Q. aria-hidden 내부 focusable element는 왜 문제야?
A. keyboard와 screen reader 흐름이 충돌해 사용자가 요소를 이해하기 어렵다.

---

# 6. Image Icon Color Final Checklist

## 6.1 Image and Icon Review

### [개념]

Image and Icon Review는 이미지와 아이콘이 정보, 기능, 장식 역할에 맞게 대체 텍스트와 accessible name을 제공하는지 확인하는 최종 점검이다.

---

### [핵심]

Checklist:

```md
- [ ] 정보 이미지에 의미 있는 alt가 있는가?
- [ ] 장식 이미지에 alt=""가 적용되었는가?
- [ ] 링크 이미지의 alt가 이동 목적을 설명하는가?
- [ ] 버튼 이미지의 alt 또는 accessible name이 기능을 설명하는가?
- [ ] 복잡한 차트 / 그래프에 별도 설명이 있는가?
- [ ] 차트 데이터가 표나 텍스트로 제공되는가?
- [ ] icon only button에 accessible name이 있는가?
- [ ] icon button 내부 icon이 aria-hidden 처리되었는가?
- [ ] 텍스트 옆 장식 icon이 aria-hidden 처리되었는가?
- [ ] 상태 icon에 텍스트 또는 accessible name이 함께 제공되는가?
- [ ] 파일명을 alt로 사용하지 않았는가?
- [ ] alt에 불필요하게 “이미지”, “사진”을 반복하지 않았는가?
```

---

### [실무]

정보 이미지:

```jsx
<img src="/festival.jpg" alt="봄꽃 축제 행사장 전경" />
```

장식 이미지:

```jsx
<img src="/decoration.png" alt="" />
```

IconButton:

```jsx
<button type="button" aria-label="알림 열기">
  <BellIcon aria-hidden="true" />
</button>
```

차트 설명:

```jsx
<img
  src="/monthly-chart.png"
  alt="월별 매출 추이 그래프"
  aria-describedby="monthly-chart-desc"
/>
<p id="monthly-chart-desc">
  1월부터 6월까지 매출은 전반적으로 증가했고 6월에 가장 높았습니다.
</p>
```

Review Agent 기준:

- 이미지의 정보 / 장식 / 기능 역할을 먼저 판단
- alt 품질은 문맥 기준으로 평가
- icon button name 누락은 높은 우선순위
- chart는 alt만으로 충분하지 않을 수 있으므로 설명 / table 제안
- 상태 icon만으로 success / error 전달하면 텍스트 추가 제안

---

### [FAQ]

Q. Image Review에서 가장 먼저 볼 것은?
A. 이미지가 정보인지 장식인지 기능인지 판단하고 alt를 결정한다.

Q. 장식 이미지는 alt를 비워도 돼?
A. 그렇다. alt=""를 사용해 스크린 리더가 건너뛰게 한다.

Q. icon button은 어떻게 검토해?
A. button에 accessible name이 있고 내부 icon이 장식 처리되었는지 확인한다.

Q. 차트 이미지는 alt만 있으면 돼?
A. 대체로 부족하다. 핵심 요약이나 데이터 table을 함께 제공하는 것이 좋다.

---

## 6.2 Color and Visual Review

### [개념]

Color and Visual Review는 색상 대비, 색상만 의미 전달, focus ring, disabled, loading, error, zoom, motion 상태를 최종 점검하는 과정이다.

---

### [핵심]

Checklist:

```md
- [ ] 텍스트와 배경 contrast가 충분한가?
- [ ] 다크모드에서도 contrast가 충분한가?
- [ ] 링크가 색상만으로 구분되지 않는가?
- [ ] error / success / selected 상태를 색상만으로 전달하지 않는가?
- [ ] focus ring이 명확히 보이는가?
- [ ] focus ring이 잘리지 않는가?
- [ ] placeholder가 중요한 정보를 단독으로 담지 않는가?
- [ ] disabled text가 지나치게 흐리지 않은가?
- [ ] loading 상태가 spinner만으로 전달되지 않는가?
- [ ] error 상태가 색상만으로 전달되지 않는가?
- [ ] browser zoom에서 텍스트가 잘리지 않는가?
- [ ] 작은 화면에서 Modal과 Form을 사용할 수 있는가?
- [ ] prefers-reduced-motion을 고려했는가?
```

---

### [실무]

색상만 의미 전달 문제:

```text
문제: 빨간 테두리만으로 오류 표시
해결: error text + aria-invalid + aria-describedby 제공
```

focus 문제:

```text
문제: outline: none
해결: :focus-visible focus style 제공
```

loading 문제:

```text
문제: spinner only
해결: role status + loading text 제공
```

Review Agent 기준:

- 색상 대비 수치는 도구 확인이 필요하므로 수동 검토 항목으로 표시
- 색상만 의미 전달은 코드와 UI 문구로 탐지 가능
- focus ring 제거는 높은 우선순위
- reduced motion은 animation / carousel / smooth scroll 사용 시 검토
- zoom / responsive는 수동 QA 항목으로 분류

---

### [FAQ]

Q. Color Review에서 가장 먼저 볼 것은?
A. 색상만으로 의미를 전달하는지와 텍스트 대비가 충분한지 확인한다.

Q. focus ring도 Visual Review 대상이야?
A. 그렇다. keyboard 사용자가 현재 위치를 볼 수 있어야 한다.

Q. 색상 대비는 코드 리뷰만으로 확인 가능해?
A. 어렵다. contrast checker 같은 도구와 수동 검토가 필요하다.

Q. animation도 접근성 검토 대상이야?
A. 그렇다. 과도한 움직임과 자동 재생은 사용자에게 불편을 줄 수 있다.

---

# 7. State Feedback Final Checklist

## 7.1 State Review

### [개념]

State Feedback Review는 Loading, Success, Error, Empty, Disabled, Offline, Upload, Progress 상태가 사용자가 이해할 수 있는 방식으로 제공되는지 확인하는 최종 점검이다.

---

### [핵심]

Checklist:

```md
- [ ] Loading 상태에 텍스트 메시지가 있는가?
- [ ] spinner only 상태가 아닌가?
- [ ] skeleton이 장식 처리되고 별도 loading text가 있는가?
- [ ] loading 영역에 aria-busy가 필요한지 검토했는가?
- [ ] button pending 상태에서 text가 변경되는가?
- [ ] pending 중 중복 제출이 방지되는가?
- [ ] Success 상태에 완료 메시지가 있는가?
- [ ] Success 상태가 색상 / 아이콘만으로 전달되지 않는가?
- [ ] Error 상태에 사용자용 오류 문구가 있는가?
- [ ] Error 상태가 내부 서버 메시지를 노출하지 않는가?
- [ ] Error 상태에 retry / recovery action이 있는가?
- [ ] Field Error와 Global Error를 구분했는가?
- [ ] Empty State가 Error State와 구분되는가?
- [ ] Empty State에 다음 행동이 있는가?
- [ ] Search Empty State에 필터 초기화 또는 검색어 변경 안내가 있는가?
- [ ] Disabled 상태에 이유가 필요한지 검토했는가?
- [ ] Offline / Network Error 상태에 재시도 안내가 있는가?
- [ ] Upload 상태에 선택 / 진행 / 성공 / 실패 메시지가 있는가?
- [ ] Progress 상태가 텍스트로도 전달되는가?
```

---

### [실무]

Loading:

```jsx
<div role="status">데이터를 불러오는 중입니다.</div>
```

Error:

```jsx
<section role="alert">
  <h2>목록을 불러오지 못했습니다.</h2>
  <p>잠시 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

Empty:

```jsx
<section>
  <h2>검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onResetFilter}>
    필터 초기화
  </button>
</section>
```

Review Agent 기준:

- spinner only는 loading text 추가 제안
- 빈 배열만 렌더링하면 Empty State 추가 제안
- error 문구가 기술적이면 사용자용 문구로 수정 제안
- retry는 action이므로 button 사용 제안
- page 이동 recovery는 Link 사용 제안
- disabled 이유가 불명확하면 안내 문구 제안

---

### [FAQ]

Q. State Review에서 가장 먼저 볼 것은?
A. Loading, Error, Empty, Success 상태가 서로 구분되고 텍스트로 전달되는지 확인한다.

Q. Empty State 없이 빈 화면이면 문제야?
A. 문제다. 사용자가 로딩 중인지 오류인지 데이터 없음인지 알 수 없다.

Q. 서버 오류 원문을 보여줘도 돼?
A. 권장하지 않는다. 사용자용 오류 문구로 변환해야 한다.

Q. retry는 Button이야 Link야?
A. 현재 요청을 다시 실행하는 action이면 button이 적합하다.

---

# 8. Component Final Checklist

## 8.1 Component Review

### [개념]

Component Review는 공통 UI Component가 semantic, keyboard, focus, ARIA, state, testing 기준을 만족하는지 최종 점검하는 과정이다.

공통 Component 접근성 문제는 프로젝트 전체로 확산되므로 높은 우선순위로 검토한다.

---

### [핵심]

Checklist:

```md
- [ ] Button 기본 type이 button인가?
- [ ] Submit Button만 type="submit"을 사용하는가?
- [ ] IconButton에 accessible name이 있는가?
- [ ] Link text가 이동 목적을 설명하는가?
- [ ] Modal에 role, aria-modal, aria-labelledby가 있는가?
- [ ] Modal open 시 focus가 내부로 이동하는가?
- [ ] Modal close 시 focus가 trigger로 복귀하는가?
- [ ] Dropdown trigger가 button인가?
- [ ] Dropdown aria-expanded가 실제 상태와 일치하는가?
- [ ] 닫힌 Dropdown item에 focus가 가지 않는가?
- [ ] Accordion trigger가 button인가?
- [ ] Accordion panel hidden 상태와 aria-expanded가 일치하는가?
- [ ] Tab과 TabPanel이 id로 연결되었는가?
- [ ] Tab aria-selected가 실제 selected 상태와 일치하는가?
- [ ] Tooltip이 focus에서도 접근 가능한가?
- [ ] Toast가 중요한 상태를 role status / alert로 전달하는가?
- [ ] Pagination 현재 페이지가 aria-current로 표시되는가?
- [ ] Breadcrumb가 nav와 ol 구조를 사용하는가?
- [ ] Card link text가 목적지를 명확히 설명하는가?
```

---

### [실무]

공통 Button:

```tsx
function Button({ type = "button", children, ...props }) {
  return (
    <button type={type} {...props}>
      {children}
    </button>
  );
}
```

공통 IconButton:

```tsx
function IconButton({ label, children, ...props }) {
  return (
    <button type="button" aria-label={label} {...props}>
      <span aria-hidden="true">{children}</span>
    </button>
  );
}
```

Modal 필수 조건:

```text
role="dialog"
aria-modal="true"
aria-labelledby
focus move
focus trap
focus return
close button
Escape close
```

Review Agent 기준:

- 공통 Component 이슈는 우선순위 High
- Button / IconButton / Modal / Dropdown은 집중 검토 대상
- Component props가 접근성 필수 값을 강제하는지 확인
- `label` 없는 IconButton props는 타입 수준에서 제한 제안
- 공통 Component 테스트가 role/name 기반인지 확인

---

### [FAQ]

Q. Component Review에서 가장 먼저 볼 것은?
A. Button, IconButton, Modal, Dropdown처럼 자주 쓰이는 Component의 기본 접근성이다.

Q. 공통 Component 문제가 왜 더 심각해?
A. 여러 화면에 같은 문제가 반복되기 때문이다.

Q. IconButton label은 optional이어도 돼?
A. 권장하지 않는다. 타입 수준에서 필수로 두는 것이 안전하다.

Q. Modal Component는 UI만 있으면 돼?
A. 아니다. role, title 연결, focus move, focus trap, focus return이 필요하다.

---

# 9. Testing Final Checklist

## 9.1 Testing Review

### [개념]

Testing Review는 테스트가 사용자 관점의 role, label, text, state를 기준으로 작성되어 접근성 구조를 검증하는지 확인하는 최종 점검이다.

---

### [핵심]

Checklist:

```md
- [ ] Button을 getByRole("button", { name })으로 찾는가?
- [ ] Link를 getByRole("link", { name })으로 찾는가?
- [ ] Form Control을 getByLabelText로 찾는가?
- [ ] IconButton을 role/name으로 검증하는가?
- [ ] Dialog를 getByRole("dialog", { name })으로 검증하는가?
- [ ] Error를 role alert 또는 error text로 검증하는가?
- [ ] Loading을 role status 또는 loading text로 검증하는가?
- [ ] Empty State heading과 action을 검증하는가?
- [ ] Dropdown aria-expanded를 검증하는가?
- [ ] Tab aria-selected를 검증하는가?
- [ ] keyboard interaction을 userEvent로 검증하는가?
- [ ] focus return을 toHaveFocus로 검증하는가?
- [ ] testId 중심 테스트를 지양하는가?
- [ ] axe test를 핵심 Component에 적용했는가?
- [ ] 수동 keyboard 점검 항목이 남아 있는가?
```

---

### [실무]

좋은 테스트:

```tsx
screen.getByRole("button", { name: "저장" });
screen.getByLabelText("이메일");
screen.getByRole("dialog", { name: "리뷰 작성" });
screen.getByRole("alert");
screen.getByRole("status");
```

나쁜 테스트:

```tsx
screen.getByTestId("save-button");
screen.getByTestId("modal");
screen.getByTestId("spinner");
```

Review Agent 기준:

- testId 중심 테스트는 접근성 검증 약화로 분류
- getByPlaceholderText 중심 Form 테스트는 label 검증 누락으로 분류
- snapshot만 있는 UI 테스트는 접근성 테스트 부족으로 분류
- Modal / Dropdown / Tab은 state와 keyboard test 제안
- axe는 핵심 Component부터 단계적으로 제안

---

### [FAQ]

Q. Testing Review에서 가장 먼저 볼 것은?
A. 테스트가 getByRole과 getByLabelText를 우선 사용하는지 확인한다.

Q. getByTestId는 쓰면 안 돼?
A. 필요한 경우 가능하지만 접근성 구조 검증에는 약하므로 최후 수단으로 둔다.

Q. spinner 테스트는 어떻게 해야 해?
A. spinner 존재보다 role status와 loading text를 검증하는 것이 좋다.

Q. axe 테스트만 있으면 충분해?
A. 아니다. Testing Library Query, keyboard test, 수동 점검과 함께 사용해야 한다.

---

# 10. Review Agent Decision Rules

## 10.1 Severity Classification

### [개념]

Severity Classification은 접근성 문제의 영향도와 수정 우선순위를 정하는 기준이다.

Review Agent는 모든 문제를 같은 우선순위로 다루지 않고 사용자 영향과 확산 범위를 기준으로 분류해야 한다.

---

### [핵심]

Severity 기준:

| Severity | 기준                                                 | 예                                     |
| -------- | ---------------------------------------------------- | -------------------------------------- |
| Critical | 핵심 기능 사용 불가 / keyboard trap / 보안 정보 노출 | Modal에서 keyboard 탈출 불가           |
| High     | 주요 기능 접근 어려움 / 공통 Component 문제          | IconButton 이름 누락, Form label 누락  |
| Medium   | 일부 사용자 혼란 / 상태 전달 부족                    | Empty State 없음, 반복 link text 모호  |
| Low      | 개선 권장 / 문구 품질 / 추가 설명                    | 더 명확한 helper text, chart 설명 보완 |

---

### [실무]

Critical 예:

```text
- Modal keyboard trap 발생
- 닫기 불가 Dialog
- aria-hidden 내부 focusable control
- 결제 / 로그인 Form keyboard 사용 불가
- 서버 stack trace 사용자 노출
```

High 예:

```text
- 공통 IconButton accessible name 누락
- Form input label 누락
- Modal focus return 누락
- Dropdown hidden item focus 가능
- Button / Link 역할 혼동
```

Medium 예:

```text
- Empty State 없음
- 자세히 보기 link 반복
- aria-expanded 테스트 없음
- loading text 부족
```

Low 예:

```text
- error 문구 개선
- helper text 구체화
- alt text 품질 개선
- chart 설명 추가
```

Review Agent 기준:

- 공통 Component 문제는 영향 범위 때문에 severity 상향 가능
- 결제 / 로그인 / 회원가입 / 저장 / 삭제 flow 문제는 우선순위 상향
- keyboard 사용 불가 문제는 높은 우선순위
- 내부 시스템 정보 노출은 접근성과 보안 양쪽에서 Critical 가능
- 단순 스타일 취향 문제와 접근성 문제를 구분

---

### [FAQ]

Q. 접근성 문제 우선순위는 어떻게 정해?
A. 핵심 기능 사용 가능 여부, keyboard 사용 가능 여부, 공통 Component 영향 범위, 사용자 혼란 정도로 정한다.

Q. keyboard trap은 왜 Critical이야?
A. 사용자가 UI에서 빠져나갈 수 없어 전체 작업을 계속할 수 없기 때문이다.

Q. 공통 Component 문제는 왜 High야?
A. 여러 화면에 같은 문제가 반복되기 때문이다.

Q. 문구 개선은 항상 낮은 우선순위야?
A. 대체로 Low 또는 Medium이지만 오류 해결 방법을 알 수 없는 경우 우선순위가 높아질 수 있다.

---

## 10.2 Fix Recommendation Pattern

### [개념]

Fix Recommendation Pattern은 Review Agent가 접근성 문제를 발견했을 때 수정 가능한 형태로 제안하는 기준이다.

좋은 접근성 리뷰는 문제 지적에서 끝나지 않고 사용자 영향, 수정 방향, 테스트 기준까지 포함해야 한다.

---

### [핵심]

수정 제안 구성:

```md
## 문제

무엇이 잘못되었는가?

## 영향

사용자에게 어떤 문제가 생기는가?

## 수정 방향

어떤 코드 / 구조로 바꿀 것인가?

## 예시

최소 수정 예시는 무엇인가?

## 테스트

어떤 Query 또는 수동 점검으로 확인할 것인가?
```

---

### [실무]

예시 1:

```md
## 문제

`NotificationButton`이 icon만 렌더링되고 accessible name이 없습니다.

## 영향

스크린 리더 사용자는 버튼의 목적을 알 수 없습니다.

## 수정 방향

button에 `aria-label="알림 열기"`를 제공하고 내부 icon은 `aria-hidden` 처리합니다.

## 테스트

`getByRole("button", { name: "알림 열기" })`로 검증합니다.
```

예시 2:

```md
## 문제

`FilterDropdown`의 `aria-expanded`가 실제 open 상태와 동기화되지 않습니다.

## 영향

보조기술 사용자에게 Dropdown이 열렸는지 닫혔는지 잘못 전달됩니다.

## 수정 방향

`aria-expanded={open}`으로 상태와 연결합니다.

## 테스트

open / close 후 `aria-expanded` 값이 변경되는지 확인합니다.
```

Review Agent 기준:

- 추상적 지적 금지
- 수정 가능한 코드 단위로 제안
- 사용자 영향 포함
- 테스트 기준 포함
- 공통 Component면 영향 범위 명시
- 기존 디자인을 유지하면서 semantic 구조 개선 우선

---

### [FAQ]

Q. 접근성 수정 제안은 어떻게 써야 해?
A. 문제, 영향, 수정 방향, 예시, 테스트 기준을 함께 제공한다.

Q. “접근성 안 좋음”이라고만 말하면 안 돼?
A. 안 된다. 수정 가능한 구체적 문제로 나눠야 한다.

Q. 테스트 기준도 같이 제안해야 해?
A. 가능하면 같이 제안해야 재발을 줄일 수 있다.

Q. 사용자 영향 설명이 필요한 이유는?
A. 왜 수정해야 하는지 개발자가 이해하고 우선순위를 정할 수 있기 때문이다.

---

# 11. Final Integrated Review Checklist

## 11.1 One Pass Checklist

### [개념]

One Pass Checklist는 Review Agent가 Frontend UI를 한 번에 빠르게 훑으며 접근성 문제를 찾는 통합 점검표다.

세부 문서로 들어가기 전 1차 필터로 사용할 수 있다.

---

### [핵심]

One Pass Checklist:

```md
## Semantic

- [ ] div/span onClick이 없는가?
- [ ] Button과 Link 역할이 구분되었는가?
- [ ] main/nav/h1 구조가 있는가?

## Form

- [ ] input/select/textarea에 label이 있는가?
- [ ] placeholder를 label로 쓰지 않았는가?
- [ ] error message가 input과 연결되었는가?

## Keyboard

- [ ] keyboard만으로 핵심 flow가 가능한가?
- [ ] focus visible이 명확한가?
- [ ] keyboard trap이 없는가?

## ARIA

- [ ] ARIA state가 실제 UI state와 일치하는가?
- [ ] aria 참조 id가 실제 DOM에 있는가?
- [ ] aria-hidden 내부 focusable 요소가 없는가?

## Image / Icon

- [ ] 정보 이미지 alt가 적절한가?
- [ ] 장식 이미지 alt=""인가?
- [ ] IconButton에 accessible name이 있는가?

## Color / Visual

- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] focus ring이 보이는가?
- [ ] dark mode / zoom 검토가 필요한가?

## State

- [ ] loading / error / empty / success 상태가 텍스트로 구분되는가?
- [ ] retry / reset / next action이 적절한가?

## Component

- [ ] Modal / Dropdown / Tab의 focus와 ARIA가 올바른가?
- [ ] 공통 Component에 문제가 반복되지 않는가?

## Testing

- [ ] getByRole / getByLabelText 기반 테스트가 있는가?
- [ ] testId 중심 테스트로 접근성 문제가 숨겨지지 않는가?
```

---

### [실무]

One Pass Review Flow:

```text
Code 검색
→ onClick / aria / tabIndex / outline / placeholder 확인
→ 주요 Component 확인
→ Form 확인
→ State UI 확인
→ Test Query 확인
→ 수동 점검 필요 항목 표시
```

코드 검색 키워드:

```text
onClick
role=
aria-
tabIndex
outline
placeholder
disabled
loading
error
alert
status
dialog
expanded
selected
testId
```

Review Agent 기준:

- One Pass에서 발견된 문제는 세부 문서 기준으로 재검토
- Critical / High 문제부터 보고
- 확실하지 않은 시각 대비 문제는 “수동 contrast 확인 필요”로 표시
- 테스트 부족은 코드 문제와 분리해서 Testing Gap으로 분류
- 수동 점검이 필요한 항목을 명시

---

### [FAQ]

Q. One Pass Checklist는 언제 써?
A. PR이나 코드 리뷰에서 접근성 문제를 빠르게 1차 탐지할 때 사용한다.

Q. One Pass만 통과하면 충분해?
A. 아니다. Modal, Form, Dropdown 같은 복잡한 Component는 세부 체크가 필요하다.

Q. 코드 검색 키워드는 왜 필요해?
A. 접근성 문제가 자주 발생하는 패턴을 빠르게 찾기 위해서다.

Q. 수동 점검 항목도 Review에 남겨야 해?
A. 그렇다. 자동으로 판단하기 어려운 focus visible, contrast, keyboard flow는 수동 점검으로 남긴다.

---

# 12. Retrieval Queries

### [FAQ]

Q. Frontend Accessibility Final Review는 뭐야?
A. Semantic HTML, Keyboard, Focus, ARIA, Form, State, Component, Testing을 통합해서 최종 점검하는 과정이다.

Q. 접근성 검토에서 가장 중요한 질문은?
A. 마우스 없이 사용할 수 있는지, 보조기술 사용자가 의미와 상태를 이해할 수 있는지 확인하는 것이다.

Q. 접근성은 개발 마지막에만 확인하면 돼?
A. 아니다. 공통 Component와 Form 설계 단계에서 반영해야 반복 오류를 줄일 수 있다.

Q. 자동 테스트만 통과하면 Final Review 완료야?
A. 아니다. keyboard, focus visible, 문구 품질, 색상 의미는 수동 검토가 필요하다.

Q. Semantic HTML 최종 검토에서 가장 먼저 볼 것은?
A. Button / Link 역할 구분, main/nav 구조, h1과 heading 계층을 먼저 본다.

Q. div onClick은 무조건 수정 대상이야?
A. 대부분 우선 수정 대상이다. 가능하면 button이나 Link로 대체한다.

Q. ARIA를 붙이면 Semantic HTML 문제를 해결할 수 있어?
A. 일부 보완은 가능하지만 Native HTML을 먼저 사용하는 것이 원칙이다.

Q. table 데이터는 div grid로 만들어도 돼?
A. 행과 열 관계가 중요한 데이터는 table을 사용하는 것이 좋다.

Q. Form 최종 검토에서 가장 먼저 볼 것은?
A. label 연결, placeholder-only 여부, error message 연결, aria-invalid 상태를 먼저 본다.

Q. placeholder가 있으면 label은 생략해도 돼?
A. 권장하지 않는다. placeholder는 label 대체가 아니다.

Q. error message는 input과 꼭 연결해야 해?
A. 권장한다. aria-describedby로 연결하면 보조기술 사용자가 오류를 이해하기 쉽다.

Q. fieldset과 legend는 언제 필요해?
A. radio group, checkbox group처럼 여러 control이 하나의 질문에 속할 때 사용한다.

Q. Keyboard 최종 검토에서 가장 중요한 것은?
A. 마우스 없이 핵심 기능을 완료할 수 있고 focus 위치가 명확히 보이는지 확인하는 것이다.

Q. keyboard test가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 실제 focus visible과 복잡한 흐름은 수동 확인이 필요하다.

Q. keyboard trap은 왜 심각해?
A. 사용자가 특정 영역에서 빠져나갈 수 없어 UI를 계속 사용할 수 없기 때문이다.

Q. custom widget은 왜 위험해?
A. role, keyboard, focus, ARIA state를 직접 구현해야 하므로 누락 가능성이 높다.

Q. Focus Review에서 가장 먼저 볼 것은?
A. focus visible이 모든 interactive element에 보이는지 확인한다.

Q. outline none은 무조건 문제야?
A. 대체 focus style 없이 제거하면 문제다.

Q. Modal close 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아간다.

Q. Form 오류 후 focus 이동은 항상 필요해?
A. 아니다. 긴 Form이나 오류를 찾기 어려운 경우 Error Summary 또는 첫 오류 field로 이동을 고려한다.

Q. ARIA 최종 검토에서 가장 중요한 것은?
A. ARIA가 실제 UI 상태와 동기화되는지, Native HTML로 대체 가능한지 확인하는 것이다.

Q. ARIA가 많으면 좋은 코드야?
A. 아니다. 필요한 ARIA만 정확히 사용하는 것이 좋다.

Q. aria-expanded는 어떻게 검토해?
A. 실제 open 상태와 값이 항상 일치하는지 확인한다.

Q. aria-hidden 내부 focusable element는 왜 문제야?
A. keyboard와 screen reader 흐름이 충돌해 사용자가 요소를 이해하기 어렵다.

Q. Image Review에서 가장 먼저 볼 것은?
A. 이미지가 정보인지 장식인지 기능인지 판단하고 alt를 결정한다.

Q. 장식 이미지는 alt를 비워도 돼?
A. 그렇다. alt=""를 사용해 스크린 리더가 건너뛰게 한다.

Q. icon button은 어떻게 검토해?
A. button에 accessible name이 있고 내부 icon이 장식 처리되었는지 확인한다.

Q. 차트 이미지는 alt만 있으면 돼?
A. 대체로 부족하다. 핵심 요약이나 데이터 table을 함께 제공하는 것이 좋다.

Q. Color Review에서 가장 먼저 볼 것은?
A. 색상만으로 의미를 전달하는지와 텍스트 대비가 충분한지 확인한다.

Q. focus ring도 Visual Review 대상이야?
A. 그렇다. keyboard 사용자가 현재 위치를 볼 수 있어야 한다.

Q. 색상 대비는 코드 리뷰만으로 확인 가능해?
A. 어렵다. contrast checker 같은 도구와 수동 검토가 필요하다.

Q. animation도 접근성 검토 대상이야?
A. 그렇다. 과도한 움직임과 자동 재생은 사용자에게 불편을 줄 수 있다.

Q. State Review에서 가장 먼저 볼 것은?
A. Loading, Error, Empty, Success 상태가 서로 구분되고 텍스트로 전달되는지 확인한다.

Q. Empty State 없이 빈 화면이면 문제야?
A. 문제다. 사용자가 로딩 중인지 오류인지 데이터 없음인지 알 수 없다.

Q. 서버 오류 원문을 보여줘도 돼?
A. 권장하지 않는다. 사용자용 오류 문구로 변환해야 한다.

Q. retry는 Button이야 Link야?
A. 현재 요청을 다시 실행하는 action이면 button이 적합하다.

Q. Component Review에서 가장 먼저 볼 것은?
A. Button, IconButton, Modal, Dropdown처럼 자주 쓰이는 Component의 기본 접근성이다.

Q. 공통 Component 문제가 왜 더 심각해?
A. 여러 화면에 같은 문제가 반복되기 때문이다.

Q. IconButton label은 optional이어도 돼?
A. 권장하지 않는다. 타입 수준에서 필수로 두는 것이 안전하다.

Q. Modal Component는 UI만 있으면 돼?
A. 아니다. role, title 연결, focus move, focus trap, focus return이 필요하다.

Q. Testing Review에서 가장 먼저 볼 것은?
A. 테스트가 getByRole과 getByLabelText를 우선 사용하는지 확인한다.

Q. getByTestId는 쓰면 안 돼?
A. 필요한 경우 가능하지만 접근성 구조 검증에는 약하므로 최후 수단으로 둔다.

Q. spinner 테스트는 어떻게 해야 해?
A. spinner 존재보다 role status와 loading text를 검증하는 것이 좋다.

Q. axe 테스트만 있으면 충분해?
A. 아니다. Testing Library Query, keyboard test, 수동 점검과 함께 사용해야 한다.

Q. 접근성 문제 우선순위는 어떻게 정해?
A. 핵심 기능 사용 가능 여부, keyboard 사용 가능 여부, 공통 Component 영향 범위, 사용자 혼란 정도로 정한다.

Q. keyboard trap은 왜 Critical이야?
A. 사용자가 UI에서 빠져나갈 수 없어 전체 작업을 계속할 수 없기 때문이다.

Q. 공통 Component 문제는 왜 High야?
A. 여러 화면에 같은 문제가 반복되기 때문이다.

Q. 접근성 수정 제안은 어떻게 써야 해?
A. 문제, 영향, 수정 방향, 예시, 테스트 기준을 함께 제공한다.

Q. “접근성 안 좋음”이라고만 말하면 안 돼?
A. 안 된다. 수정 가능한 구체적 문제로 나눠야 한다.

Q. 테스트 기준도 같이 제안해야 해?
A. 가능하면 같이 제안해야 재발을 줄일 수 있다.

Q. One Pass Checklist는 언제 써?
A. PR이나 코드 리뷰에서 접근성 문제를 빠르게 1차 탐지할 때 사용한다.

Q. One Pass만 통과하면 충분해?
A. 아니다. Modal, Form, Dropdown 같은 복잡한 Component는 세부 체크가 필요하다.

Q. 코드 검색 키워드는 왜 필요해?
A. 접근성 문제가 자주 발생하는 패턴을 빠르게 찾기 위해서다.

Q. 수동 점검 항목도 Review에 남겨야 해?
A. 그렇다. 자동으로 판단하기 어려운 focus visible, contrast, keyboard flow는 수동 점검으로 남긴다.
