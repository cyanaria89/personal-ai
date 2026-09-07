# Frontend Accessibility Part04 - Keyboard Focus Accessibility

---

# 1. Keyboard Accessibility

## 1.1 Keyboard Accessibility Purpose

### [개념]

Keyboard Accessibility는 마우스 없이 `Tab`, `Shift+Tab`, `Enter`, `Space`, `Escape`, `Arrow Key` 등으로 UI를 사용할 수 있게 만드는 기준이다.

Frontend UI는 마우스로 클릭 가능한 것만으로 충분하지 않다.

키보드 사용자, 스크린 리더 사용자, 운동 제약 사용자, 임시로 마우스를 사용할 수 없는 사용자도 주요 기능을 사용할 수 있어야 한다.

---

### [핵심]

Keyboard Accessibility 핵심 요소:

- Tab Navigation
- Shift+Tab Navigation
- Enter Activation
- Space Activation
- Escape Close
- Arrow Key Navigation
- Focus Visible
- Focus Management
- Tab Order
- Focus Trap
- Focus Return
- Skip Link
- Keyboard Shortcut
- Native Element
- Custom Component Keyboard Support

---

### [실무]

2026 실무 기준에서 Keyboard Accessibility는 수동 점검이 필수다.

기본 점검 Flow:

```text
마우스 사용 금지
→ Tab으로 이동
→ 현재 focus 위치 확인
→ Enter / Space로 실행
→ Shift+Tab 역방향 확인
→ Escape 닫기 확인
→ Form 입력 / 제출 확인
→ Modal / Dropdown / Tab 조작 확인
→ Focus Lost 여부 확인
```

실무 기준:

- 클릭 가능한 요소는 keyboard로도 조작 가능해야 함
- Native `button`, `input`, `select`, `textarea`, `a` 우선 사용
- `div onClick`은 keyboard 접근성 누락 위험
- Focus outline 제거 금지
- Tab Order는 시각적 흐름과 자연스럽게 일치
- Modal은 focus 이동 / focus trap / focus return 고려
- Dropdown은 trigger focus, item focus, Escape 닫기 고려
- Custom Component는 role만으로 충분하지 않음
- Testing Library와 user-event keyboard 테스트로 일부 검증 가능

---

### [FAQ]

Q. Keyboard Accessibility는 왜 중요해?
A. 마우스 없이도 사용자가 주요 기능을 조작할 수 있어야 하기 때문이다.

Q. 마우스로 잘 되면 키보드도 되는 거 아니야?
A. 아니다. div onClick, custom dropdown, modal 등은 keyboard 조작이 누락될 수 있다.

Q. 키보드 접근성은 뭘 먼저 확인해?
A. Tab 이동, Enter / Space 실행, Escape 닫기, focus visible 여부부터 확인한다.

Q. Keyboard 접근성은 자동화 테스트만으로 충분해?
A. 아니다. focus 흐름과 실제 조작 가능성은 수동 점검이 필요하다.

---

# 2. Native Keyboard Behavior

## 2.1 Native Element Keyboard Support

### [개념]

Native Element는 브라우저가 기본 keyboard 동작과 focus 동작을 제공하는 HTML 요소다.

접근성 있는 UI는 가능한 한 Native Element를 먼저 사용해야 한다.

---

### [핵심]

Native keyboard 지원:

| 요소       | 기본 keyboard 동작                |
| ---------- | --------------------------------- |
| `button`   | Tab focus, Enter / Space 실행     |
| `a href`   | Tab focus, Enter 이동             |
| `input`    | Tab focus, 입력                   |
| `checkbox` | Tab focus, Space 토글             |
| `radio`    | Tab focus, Arrow 이동, Space 선택 |
| `select`   | Tab focus, Arrow 선택             |
| `textarea` | Tab focus, 입력                   |
| `summary`  | Tab focus, Enter / Space 토글     |

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

Link 예:

```jsx
<Link to="/festivals">축제 목록</Link>
```

Checkbox 예:

```jsx
<label>
  <input type="checkbox" name="terms" />
  이용약관에 동의합니다.
</label>
```

실무 기준:

- 액션은 `button`
- 이동은 `a` 또는 `Link`
- 선택은 native `input`, `select` 우선
- Native Element는 기본 focus와 keyboard 동작 제공
- Custom Element 사용 시 keyboard 동작 직접 구현 필요
- `role`만 붙여도 keyboard 동작은 자동 생성되지 않음

---

### [FAQ]

Q. Native Element를 우선해야 하는 이유는?
A. 기본 role, keyboard 동작, focus 동작이 이미 제공되기 때문에 접근성 누락 위험이 낮다.

Q. div에 role="button"을 붙이면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 Enter / Space keyboard 동작은 직접 구현해야 한다.

Q. a 태그는 Space로 실행돼?
A. 기본 link는 Enter로 이동한다. Button은 Enter와 Space로 실행된다.

Q. checkbox는 keyboard로 어떻게 조작해?
A. Tab으로 focus하고 Space로 checked 상태를 토글한다.

---

## 2.2 Custom Element Keyboard Requirement

### [개념]

Custom Element Keyboard Requirement는 `div`, `span` 등 non-interactive element를 interactive element처럼 사용할 때 필요한 keyboard 구현 기준이다.

가능하면 Custom Element 대신 Native Element를 사용해야 한다.

---

### [핵심]

Custom interactive element에 필요한 것:

- `tabIndex={0}`
- 적절한 `role`
- Enter 처리
- Space 처리
- Focus Visible
- Accessible Name
- Disabled 상태 처리
- 실제 UI 상태와 ARIA 동기화

주의:

- 구현 부담 증가
- 브라우저 기본 동작 재현 필요
- 실수 가능성 높음
- Testing 필요

---

### [실무]

비권장 예:

```jsx
<div
  role="button"
  tabIndex={0}
  onClick={onSave}
  onKeyDown={(event) => {
    if (event.key === "Enter" || event.key === " ") {
      onSave();
    }
  }}
>
  저장
</div>
```

권장 예:

```jsx
<button type="button" onClick={onSave}>
  저장
</button>
```

Custom이 필요한 경우 기준:

```text
Native Element로 가능한가?
→ 가능하면 Native Element 사용
→ 불가능하면 role / tabIndex / keyboard / focus / aria 상태 구현
→ keyboard 수동 점검
→ Testing Library getByRole 검증
```

실무 기준:

- `div onClick`은 우선 수정 대상
- `role="button"` + `tabIndex`만으로 충분하지 않음
- Space key는 page scroll 방지 고려
- disabled 상태는 focus와 click 처리 모두 검토
- Custom Component는 keyboard 테스트 필수

---

### [FAQ]

Q. div onClick을 keyboard 접근성 있게 만들 수 있어?
A. 가능은 하지만 role, tabIndex, Enter / Space 처리, focus style을 직접 구현해야 한다. 가능하면 button을 사용한다.

Q. role과 tabIndex만 있으면 충분해?
A. 아니다. keyboard activation과 상태 동기화가 필요하다.

Q. Custom Button을 만들면 안 돼?
A. 가능하지만 내부는 native button을 사용하는 방식이 가장 안전하다.

Q. Space key 처리는 왜 필요해?
A. button은 Space로 실행되므로 custom button도 유사한 조작을 제공해야 한다.

---

# 3. Tab Navigation

## 3.1 Tab Order Rules

### [개념]

Tab Order는 사용자가 `Tab` 키를 눌렀을 때 focus가 이동하는 순서다.

Tab Order는 DOM 순서와 시각적 흐름이 자연스럽게 일치해야 한다.

---

### [핵심]

Tab Order 기준:

- DOM order
- Visual order
- Interactive elements
- `tabIndex`
- `tabIndex={0}`
- `tabIndex={-1}`
- Avoid positive tabindex
- Hidden element focus prevention
- Disabled element exclusion
- Focusable element visibility

---

### [실무]

좋은 구조:

```jsx
<header>
  <nav>
    <Link to="/">홈</Link>
    <Link to="/festivals">축제</Link>
  </nav>
</header>

<main>
  <h1>축제 검색</h1>
  <label htmlFor="keyword">검색어</label>
  <input id="keyword" name="keyword" />
  <button type="submit">검색</button>
</main>
```

나쁜 예:

```jsx
<button tabIndex={3}>검색</button>
<input tabIndex={1} />
<a tabIndex={2} href="/festivals">축제</a>
```

실무 기준:

- DOM 순서를 먼저 올바르게 설계
- 시각적 배치와 focus 순서가 크게 어긋나지 않게 함
- 양수 `tabIndex` 사용 지양
- 숨겨진 Dropdown item에 focus 가지 않게 처리
- disabled 요소는 focus 대상에서 제외됨
- Modal open 시 배경 요소 focus 방지 필요
- CSS order로 시각 순서만 바꾸면 Tab Order와 불일치 가능

---

### [FAQ]

Q. Tab Order는 무엇 기준으로 정해져?
A. 기본적으로 DOM 순서와 focus 가능한 요소 기준으로 정해진다.

Q. tabindex를 많이 쓰면 키보드 순서를 쉽게 조정할 수 있지 않아?
A. 양수 tabindex는 유지보수를 어렵게 만들 수 있다. DOM 순서를 올바르게 설계하는 것이 우선이다.

Q. CSS flex order를 쓰면 Tab 순서도 바뀌어?
A. 보통 DOM 순서는 그대로라서 시각 순서와 Tab 순서가 어긋날 수 있다.

Q. disabled button은 Tab으로 focus돼?
A. 일반적으로 disabled button은 focus 대상에서 제외된다.

---

## 3.2 TabIndex Rules

### [개념]

`tabIndex`는 요소가 keyboard focus 순서에 포함되는 방식을 제어하는 속성이다.

`tabIndex`는 필요한 경우에만 사용해야 하며, 양수 값은 지양한다.

---

### [핵심]

`tabIndex` 값:

| 값   | 의미                                   |
| ---- | -------------------------------------- |
| `0`  | DOM 순서에 따라 Tab focus 가능         |
| `-1` | Tab 순서 제외, programmatic focus 가능 |
| 양수 | 지정 순서대로 focus, 사용 지양         |

사용 기준:

- `tabIndex={0}`: custom focusable 요소에 제한적 사용
- `tabIndex={-1}`: Error Summary, Modal Title, Route Heading focus 등에 사용
- 양수 `tabIndex`: 지양
- focus 불필요한 요소에 남발 금지

---

### [실무]

Programmatic focus 예:

```jsx
<div role="alert" tabIndex={-1} ref={errorSummaryRef}>
  입력 내용을 확인해 주세요.
</div>
```

Custom focusable 예:

```jsx
<div role="tabpanel" tabIndex={0}>
  탭 패널 내용
</div>
```

나쁜 예:

```jsx
<button tabIndex={10}>저장</button>
<button tabIndex={1}>취소</button>
```

실무 기준:

- focus 순서 조정은 DOM 구조 개선이 우선
- programmatic focus 대상은 `tabIndex={-1}` 사용 가능
- custom widget에서 `tabIndex={0}` 사용 시 keyboard 동작도 함께 구현
- 양수 tabindex는 복잡한 focus 순서 문제를 만들 수 있음
- 숨겨진 요소에 `tabIndex={0}` 남아있지 않게 함

---

### [FAQ]

Q. tabindex="-1"은 언제 써?
A. 사용자 Tab 순서에는 포함하지 않지만 코드로 focus를 이동해야 하는 요소에 사용할 수 있다.

Q. tabindex="0"은 언제 써?
A. 원래 focus되지 않는 요소를 DOM 순서에 따라 focus 가능하게 만들 때 제한적으로 사용한다.

Q. 양수 tabindex는 왜 피해야 해?
A. 전체 focus 순서를 복잡하게 만들고 유지보수를 어렵게 하기 때문이다.

Q. focus 순서를 바꾸고 싶으면 어떻게 해?
A. 먼저 DOM 순서를 자연스럽게 조정하는 것이 좋다.

---

# 4. Focus Visible

## 4.1 Focus Indicator Rules

### [개념]

Focus Visible은 현재 keyboard focus가 어디에 있는지 사용자가 볼 수 있게 하는 기준이다.

Focus indicator가 없으면 키보드 사용자는 현재 위치를 알 수 없어 UI를 사용할 수 없다.

---

### [핵심]

Focus Visible 기준:

- focus outline 유지
- custom focus style 제공
- keyboard focus 구분
- focus indicator contrast
- focus not clipped
- no outline none without replacement
- `:focus-visible`
- interactive element coverage

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

Link focus 예:

```css
a:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

실무 기준:

- 기본 outline을 무작정 제거하지 않음
- 디자인에 맞는 대체 focus style 제공
- focus style은 hover와 구분
- focus indicator가 overflow hidden에 잘리지 않게 확인
- 다크모드 / 라이트모드 모두 확인
- 버튼, 링크, input, checkbox, radio, custom trigger 모두 확인

---

### [FAQ]

Q. focus outline을 없애면 디자인이 깔끔해지는데 괜찮아?
A. 권장하지 않는다. 키보드 사용자가 현재 위치를 알 수 없게 된다.

Q. focus와 hover는 같은 거야?
A. 다르다. hover는 마우스 상태이고 focus는 키보드나 프로그램적 초점 상태다.

Q. :focus-visible은 언제 써?
A. keyboard focus에 적합한 focus style을 제공할 때 사용할 수 있다.

Q. focus indicator도 색상 대비가 필요해?
A. 필요하다. 현재 위치를 명확히 볼 수 있어야 한다.

---

## 4.2 Focus Style in Design System

### [개념]

Design System의 Focus Style은 모든 interactive component에 일관된 keyboard focus 표시를 제공하는 기준이다.

공통 Button, Link, Input, Select, Checkbox, Modal Trigger, Dropdown Trigger에 focus style이 누락되지 않아야 한다.

---

### [핵심]

Design System focus 대상:

- Button
- Icon Button
- Link
- Text Input
- Select
- Checkbox
- Radio
- Switch
- Tab
- Dropdown Trigger
- Modal Close Button
- Pagination
- Card Link
- Custom Component

Focus Style 기준:

- 일관성
- 충분한 대비
- outline clipping 방지
- disabled 상태와 구분
- hover와 구분
- dark mode 확인
- high contrast 환경 고려

---

### [실무]

공통 focus token 예:

```css
:root {
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
}
```

공통 class 예:

```css
.focus-ring:focus-visible {
  outline: var(--focus-ring-width) solid currentColor;
  outline-offset: var(--focus-ring-offset);
}
```

Component 적용 예:

```jsx
<button type="button" className="button focus-ring">
  저장
</button>
```

실무 기준:

- 공통 Component 단계에서 focus style 포함
- `outline: none` reset 코드 검토
- disabled 상태는 focus 불가 또는 명확한 상태 표현
- Custom Component에도 동일 focus rule 적용
- focus style regression은 UI QA 항목에 포함
- 디자인 시스템 문서에 focus token과 예시 포함

---

### [FAQ]

Q. Focus Style은 Component마다 따로 만들면 돼?
A. 가능하지만 Design System에서는 공통 focus rule을 제공하는 것이 일관성에 좋다.

Q. outline 대신 box-shadow를 써도 돼?
A. 가능하다. 다만 충분히 보이고 잘리지 않아야 한다.

Q. disabled 요소에도 focus style이 필요해?
A. 일반 disabled 요소는 focus 대상에서 제외되는 경우가 많다. disabled 상태는 시각적으로 명확해야 한다.

Q. focus style은 다크모드에서도 확인해야 해?
A. 그렇다. 배경과 충분히 구분되는지 확인해야 한다.

---

# 5. Activation Keys

## 5.1 Enter and Space Rules

### [개념]

Activation Key는 keyboard로 interactive element를 실행하는 키다.

Button은 일반적으로 `Enter`와 `Space`로 실행되고, Link는 `Enter`로 이동한다.

Custom Component는 해당 역할에 맞는 Activation Key를 구현해야 한다.

---

### [핵심]

Activation 기준:

- Button: `Enter`, `Space`
- Link: `Enter`
- Checkbox: `Space`
- Radio: `Space`, Arrow navigation
- Select: Arrow, Enter, Space
- Dialog close: `Escape`
- Menu item: Enter, Space
- Tab: Enter / Space 또는 자동 활성화 패턴 검토

---

### [실무]

Button은 native 사용:

```jsx
<button type="button" onClick={onSubmit}>
  저장
</button>
```

Custom button이 필요한 경우:

```jsx
function handleKeyDown(event) {
  if (event.key === "Enter" || event.key === " ") {
    event.preventDefault();
    onSubmit();
  }
}
```

실무 기준:

- Button 역할이면 Enter / Space 실행
- Link 역할이면 Enter 이동
- Space key에서 페이지 스크롤 방지 필요할 수 있음
- `onKeyDown`과 `onClick` 중복 실행 주의
- Native Element를 쓰면 직접 구현 필요 없음
- Custom Widget은 역할별 keyboard pattern 확인 필요

---

### [FAQ]

Q. Button은 어떤 키로 실행돼?
A. 일반적으로 Enter와 Space로 실행된다.

Q. Link는 어떤 키로 실행돼?
A. 일반적으로 Enter로 이동한다.

Q. Custom Button에서 Enter만 처리하면 돼?
A. Button 역할이면 Space 처리도 고려해야 한다.

Q. Space를 누르면 페이지가 움직여?
A. Custom Element에서는 Space가 스크롤을 유발할 수 있어 preventDefault가 필요할 수 있다.

---

## 5.2 Escape Key Rules

### [개념]

Escape Key는 Modal, Dropdown, Popover, Menu, Toast 등 임시 UI를 닫는 데 자주 사용되는 keyboard interaction이다.

사용자가 열린 UI에서 빠져나갈 수 있는 명확한 방법을 제공해야 한다.

---

### [핵심]

Escape 적용 대상:

- Modal
- Dialog
- Dropdown
- Menu
- Popover
- Combobox List
- Tooltip-like UI
- Search Overlay
- Side Panel

Escape 기준:

- 열린 UI 닫기
- focus return
- 상태 동기화
- 중첩 UI 처리
- 닫기 버튼도 제공
- 필수 확인 Modal에서는 정책 명확화

---

### [실무]

Escape 처리 예:

```tsx
useEffect(() => {
  if (!open) return;

  const handleKeyDown = (event: KeyboardEvent) => {
    if (event.key === "Escape") {
      onClose();
    }
  };

  document.addEventListener("keydown", handleKeyDown);

  return () => {
    document.removeEventListener("keydown", handleKeyDown);
  };
}, [open, onClose]);
```

닫기 버튼:

```jsx
<button type="button" onClick={onClose}>
  닫기
</button>
```

실무 기준:

- Escape로 닫을 수 있는지 검토
- 닫은 후 focus를 trigger로 복귀
- Escape 이벤트 listener cleanup 필수
- 중첩 Modal / Dropdown은 가장 위 UI만 닫기
- Escape 닫기가 불가능한 critical dialog는 닫기 정책을 명확히 제공
- 닫기 버튼은 항상 제공 권장

---

### [FAQ]

Q. Modal은 Escape로 닫혀야 해?
A. 일반적으로 Escape 닫기를 제공하는 것이 좋다. 단, 필수 확인 Dialog는 정책을 명확히 해야 한다.

Q. Dropdown도 Escape로 닫혀야 해?
A. 권장한다. 열린 메뉴에서 keyboard 사용자가 빠져나갈 수 있어야 한다.

Q. Escape로 닫은 후 focus는 어디로 가야 해?
A. 일반적으로 해당 UI를 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. 닫기 버튼이 있으면 Escape는 없어도 돼?
A. 닫기 버튼은 필수에 가깝고 Escape도 함께 지원하면 keyboard 사용성이 좋아진다.

---

# 6. Arrow Key Navigation

## 6.1 Arrow Key Pattern

### [개념]

Arrow Key Navigation은 Tab으로 모든 내부 항목을 이동하는 대신 방향키로 관련 항목 사이를 이동하는 keyboard pattern이다.

Radio Group, Tab, Menu, Listbox, Slider 같은 Component에서 자주 사용한다.

---

### [핵심]

Arrow Key 적용 대상:

- Radio Group
- Tab List
- Menu
- Listbox
- Combobox
- Slider
- Carousel
- Tree View
- Grid

기본 기준:

- Arrow Right / Down: 다음 항목
- Arrow Left / Up: 이전 항목
- Home: 첫 항목
- End: 마지막 항목
- Enter / Space: 선택 또는 실행
- Focus와 selected 상태 구분

---

### [실무]

Tab keydown 예:

```tsx
function handleTabKeyDown(event, index) {
  if (event.key === "ArrowRight") {
    focusTab(index + 1);
  }

  if (event.key === "ArrowLeft") {
    focusTab(index - 1);
  }
}
```

Radio는 native 사용 권장:

```jsx
<fieldset>
  <legend>정렬 방식</legend>
  <label>
    <input type="radio" name="sort" value="latest" />
    최신순
  </label>
  <label>
    <input type="radio" name="sort" value="popular" />
    인기순
  </label>
</fieldset>
```

실무 기준:

- Native radio는 기본 Arrow Key 지원
- Custom Tab / Menu / Listbox는 pattern 구현 필요
- Focus 이동과 선택 상태 변경 정책 명확화
- Arrow Key를 적용할 필요 없는 단순 버튼 목록에는 남용하지 않음
- 복잡한 widget은 접근성 라이브러리 검토 가능

---

### [FAQ]

Q. 모든 목록에 Arrow Key를 구현해야 해?
A. 아니다. 일반 링크 목록이나 버튼 목록은 Tab 이동으로 충분한 경우가 많다.

Q. Radio Group은 Arrow Key를 직접 구현해야 해?
A. Native radio를 사용하면 브라우저가 기본적으로 지원한다.

Q. Tab은 Arrow Key가 필요해?
A. 접근성 있는 Tab 패턴에서는 Arrow Key 이동을 고려하는 것이 좋다.

Q. Focus와 selected는 같은 거야?
A. 아니다. focus는 현재 keyboard 위치이고 selected는 선택된 상태다.

---

## 6.2 Roving TabIndex

### [개념]

Roving TabIndex는 복합 widget 내부에서 하나의 항목만 Tab 순서에 포함하고, 나머지는 방향키로 이동하게 하는 focus 관리 패턴이다.

Tab, Menu, Listbox 같은 widget에서 사용할 수 있다.

---

### [핵심]

Roving TabIndex 기준:

- 현재 focus 가능 항목: `tabIndex={0}`
- 나머지 항목: `tabIndex={-1}`
- Arrow Key로 focus 이동
- Tab은 widget 밖으로 이동
- selected 상태와 focus 상태 구분
- DOM ref 관리 필요

---

### [실무]

Tab 예:

```jsx
<button
  type="button"
  role="tab"
  tabIndex={activeIndex === 0 ? 0 : -1}
  aria-selected={selectedIndex === 0}
  onKeyDown={(event) => handleKeyDown(event, 0)}
>
  정보
</button>

<button
  type="button"
  role="tab"
  tabIndex={activeIndex === 1 ? 0 : -1}
  aria-selected={selectedIndex === 1}
  onKeyDown={(event) => handleKeyDown(event, 1)}
>
  리뷰
</button>
```

실무 기준:

- 단순 UI에는 불필요하게 적용하지 않음
- 복합 widget 내부 Tab stop 수를 줄이는 데 사용
- Arrow Key 이동을 함께 구현
- focus 상태와 selected 상태를 명확히 관리
- 구현 난도가 있으므로 테스트 필요
- 복잡하면 headless UI library 검토

---

### [FAQ]

Q. Roving TabIndex는 언제 써?
A. Tab, Menu, Listbox처럼 복합 widget 내부 항목을 방향키로 이동하게 할 때 사용한다.

Q. 모든 버튼 목록에 Roving TabIndex를 써야 해?
A. 아니다. 일반 버튼 목록은 Tab 이동만으로 충분한 경우가 많다.

Q. tabIndex가 -1이면 focus가 불가능해?
A. Tab 순서에서는 제외되지만 코드로 focus를 줄 수 있다.

Q. Roving TabIndex가 어려운 이유는?
A. focus index, selected state, keyboard event, ref 관리가 함께 필요하기 때문이다.

---

# 7. Focus Management

## 7.1 Programmatic Focus

### [개념]

Programmatic Focus는 JavaScript로 특정 요소에 focus를 이동시키는 방식이다.

Modal open, Form validation 실패, Route transition, 동적 요소 추가 같은 상황에서 사용자가 현재 위치를 잃지 않도록 도와준다.

---

### [핵심]

사용 상황:

- Modal open
- Modal close
- Error Summary focus
- First invalid field focus
- Route heading focus
- Dynamic field added
- Deleted item focus recovery
- Toast action focus
- Skip Link target focus

주의:

- focus를 불필요하게 빼앗지 않음
- 사용자의 현재 작업 흐름 고려
- `tabIndex={-1}` 사용 가능
- focus 대상은 실제 DOM에 있어야 함
- hidden element에 focus 금지

---

### [실무]

Focus 예:

```tsx
const titleRef = useRef<HTMLHeadingElement>(null);

useEffect(() => {
  if (open) {
    titleRef.current?.focus();
  }
}, [open]);
```

Focus 대상:

```jsx
<h2 tabIndex={-1} ref={titleRef}>
  리뷰 작성
</h2>
```

첫 오류 field focus:

```tsx
useEffect(() => {
  if (submitFailed && firstErrorRef.current) {
    firstErrorRef.current.focus();
  }
}, [submitFailed]);
```

실무 기준:

- 사용자가 예상할 수 있는 위치로 focus 이동
- UI가 열린 직후 focus 대상 존재 여부 확인
- focus 이동 후 focus visible 확인
- `tabIndex={-1}`은 programmatic focus 대상에 사용
- Route 이동 시 h1 또는 main focus 전략 검토
- 동적 삭제 후 focus lost 방지

---

### [FAQ]

Q. Programmatic Focus는 언제 필요해?
A. Modal open, Form 오류, Route 이동, 동적 UI 변경처럼 사용자가 위치를 잃기 쉬운 상황에 필요할 수 있다.

Q. focus를 자동 이동하면 항상 좋아?
A. 아니다. 사용자의 작업 흐름을 방해할 수 있으므로 필요한 경우에만 사용한다.

Q. focus 대상에 tabIndex="-1"을 붙이는 이유는?
A. Tab 순서에는 포함하지 않지만 코드로 focus를 이동하기 위해서다.

Q. hidden 요소에 focus를 줘도 돼?
A. 안 된다. 사용자가 볼 수 없거나 접근할 수 없는 요소에 focus가 가면 혼란을 만든다.

---

## 7.2 Focus Return

### [개념]

Focus Return은 Modal, Dropdown, Popover 같은 임시 UI를 닫은 후 focus를 해당 UI를 열었던 trigger 요소로 되돌리는 기준이다.

Focus Return이 없으면 keyboard 사용자는 현재 위치를 잃을 수 있다.

---

### [핵심]

Focus Return 대상:

- Modal close → open button
- Dropdown close → trigger button
- Popover close → trigger button
- Side Panel close → open button
- Search overlay close → search button
- Delete confirm close → delete button 또는 다음 합리적 위치

주의 상황:

- trigger unmounted
- item deleted
- route changed
- disabled trigger
- nested modal
- async close

---

### [실무]

Focus Return 예:

```tsx
const triggerRef = useRef<HTMLButtonElement>(null);

function openDialog() {
  setOpen(true);
}

function closeDialog() {
  setOpen(false);
  requestAnimationFrame(() => {
    triggerRef.current?.focus();
  });
}
```

Trigger:

```jsx
<button ref={triggerRef} type="button" onClick={openDialog}>
  리뷰 작성
</button>
```

삭제 후 focus 후보:

```text
삭제 버튼이 사라짐
→ 다음 항목의 삭제 버튼
→ 이전 항목의 삭제 버튼
→ 목록 제목
→ 목록으로 돌아가기 버튼
```

실무 기준:

- 닫은 후 trigger로 focus 복귀
- trigger가 사라졌다면 다음 합리적 위치로 이동
- focus return은 Modal / Dropdown 기본 요구사항에 가깝게 검토
- focus 복귀 후 scroll jump 확인
- 비동기 unmount 이후 focus timing 확인

---

### [FAQ]

Q. Modal 닫은 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. Dropdown 닫은 후 focus는 어디로 가야 해?
A. Dropdown trigger button으로 돌아가는 것이 자연스럽다.

Q. 삭제 후 trigger가 사라지면 focus는 어디로 가?
A. 다음 항목, 이전 항목, 목록 제목 등 사용자가 이어서 조작할 수 있는 위치로 이동한다.

Q. Focus Return이 없으면 어떤 문제가 생겨?
A. keyboard 사용자가 현재 위치를 잃고 다음 조작을 하기 어려워질 수 있다.

---

# 8. Focus Trap and Keyboard Trap

## 8.1 Focus Trap

### [개념]

Focus Trap은 Modal처럼 특정 UI가 열린 동안 keyboard focus를 해당 UI 내부에 제한하는 패턴이다.

Modal이 열린 상태에서는 배경 콘텐츠가 비활성화된 것처럼 동작해야 하므로 focus가 Modal 밖으로 빠져나가지 않게 해야 한다.

---

### [핵심]

Focus Trap 기준:

- Modal open 시 내부로 focus 이동
- Tab은 Modal 내부 순환
- Shift+Tab도 Modal 내부 순환
- Escape 닫기 제공
- 닫기 버튼 제공
- Modal close 시 focus return
- 배경 focus 방지
- hidden / inert 처리 고려

---

### [실무]

Focus Trap Flow:

```text
Modal Open
→ Focus Move Into Modal
→ Tab Inside Modal
→ Shift+Tab Inside Modal
→ Escape or Close Button
→ Modal Close
→ Focus Return to Trigger
```

실무 기준:

- Modal은 focus trap 필요
- Dropdown은 항상 focus trap이 필요한 것은 아님
- 복잡한 focus trap은 검증된 라이브러리 사용 검토
- focus 가능한 요소가 없는 Modal은 title 또는 close button에 focus
- focus trap 중에도 닫을 방법이 있어야 함
- 배경 스크롤과 배경 focus를 함께 검토

---

### [FAQ]

Q. Modal 안에 focus가 갇히는 건 문제야?
A. Modal이 열려 있는 동안 내부에 focus를 제한하는 것은 정상이다. 하지만 닫을 방법이 없으면 문제다.

Q. 모든 팝업에 focus trap이 필요해?
A. 아니다. Modal dialog에는 필요하지만 작은 Dropdown이나 Tooltip은 패턴에 따라 다르다.

Q. Focus Trap 구현이 어려우면 어떻게 해?
A. 접근성 검증된 dialog library나 headless component를 검토할 수 있다.

Q. Modal 안에 focus 가능한 요소가 없으면?
A. Modal title이나 container에 programmatic focus를 줄 수 있다.

---

## 8.2 Keyboard Trap

### [개념]

Keyboard Trap은 사용자가 keyboard로 특정 UI 영역에 갇혀 빠져나갈 수 없는 문제다.

Focus Trap은 의도된 패턴이고, Keyboard Trap은 사용자를 막는 접근성 문제다.

---

### [핵심]

Keyboard Trap 원인:

- 닫기 버튼 없음
- Escape 닫기 없음
- focus trap 구현 오류
- Tab 순환 오류
- hidden element focus
- disabled focused element
- focus return 누락
- iframe escape 불가
- custom widget keyboard 누락

문제 기준:

- 사용자가 빠져나갈 수 없음
- 다음 조작 위치를 알 수 없음
- focus가 보이지 않음
- 닫기 방법이 keyboard로 불가능

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
→ disabled element focus 확인
```

문제 예:

```text
Dropdown 열림
→ Tab을 눌러도 메뉴 밖으로 나갈 수 없음
→ Escape도 닫히지 않음
→ 닫기 버튼 없음
= Keyboard Trap
```

실무 기준:

- 사용자가 keyboard로 UI를 닫거나 빠져나갈 수 있어야 함
- Modal은 의도된 focus trap과 닫기 방법을 함께 제공
- Dropdown은 Escape / outside click / selection 후 닫기 기준 제공
- focus가 사라지거나 보이지 않는 상태 방지
- keyboard trap은 수동 테스트로 반드시 확인

---

### [FAQ]

Q. Focus Trap과 Keyboard Trap은 뭐가 달라?
A. Focus Trap은 Modal 내부 focus 제한 같은 의도된 패턴이고 Keyboard Trap은 사용자가 빠져나갈 수 없는 접근성 문제다.

Q. Keyboard Trap은 어떻게 찾어?
A. Tab, Shift+Tab, Escape, 닫기 버튼, focus return을 직접 확인한다.

Q. Modal focus trap은 괜찮고 keyboard trap은 왜 문제야?
A. Modal focus trap은 닫을 방법이 있어야 정상이다. 닫을 방법이 없으면 keyboard trap이 된다.

Q. Dropdown에서 Tab을 누르면 이상하게 이동해?
A. 열린 메뉴 item의 focus 순서와 닫힘 처리를 확인해야 한다.

---

# 9. Skip Link

## 9.1 Skip Link Basics

### [개념]

Skip Link는 keyboard 사용자가 반복되는 navigation을 건너뛰고 주요 콘텐츠로 바로 이동할 수 있게 하는 링크다.

주로 페이지 상단에서 `main` 영역으로 이동하는 “본문으로 건너뛰기” 링크를 제공한다.

---

### [핵심]

Skip Link 기준:

- 페이지 상단 배치
- keyboard focus 시 보이게 처리
- `main` id와 연결
- 반복 navigation 건너뛰기
- focus target 제공
- SPA route에서도 유지 가능

---

### [실무]

Skip Link 예:

```jsx
<a href="#main-content" className="skip-link">
  본문으로 건너뛰기
</a>

<main id="main-content" tabIndex={-1}>
  <h1>축제 목록</h1>
</main>
```

CSS 예:

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
}

.skip-link:focus {
  top: 0;
}
```

실무 기준:

- Skip Link는 focus 시 화면에 보여야 함
- target id는 실제 `main` 영역과 일치
- `main`에 `tabIndex={-1}`을 줄 수 있음
- fixed header에 가려지지 않게 확인
- SPA에서도 layout 상단에 배치 가능
- keyboard 수동 테스트로 확인

---

### [FAQ]

Q. Skip Link는 왜 필요해?
A. keyboard 사용자가 반복되는 메뉴를 매번 거치지 않고 본문으로 바로 이동할 수 있게 하기 위해서다.

Q. Skip Link는 항상 보여야 해?
A. 보통 기본적으로 숨기고 keyboard focus 시 보이게 처리한다.

Q. Skip Link는 어디로 연결해?
A. 일반적으로 main 영역의 id로 연결한다.

Q. SPA에서도 Skip Link가 필요해?
A. 반복 navigation이 있는 SPA에서도 유용하다.

---

# 10. Route Focus Management

## 10.1 SPA Route Focus

### [개념]

SPA Route Focus Management는 React Router 같은 SPA 환경에서 route가 변경될 때 keyboard focus와 화면 맥락을 관리하는 기준이다.

브라우저 전체 페이지 이동과 달리 SPA route 변경은 focus가 기존 위치에 남아 사용자가 새 페이지로 이동했는지 인식하기 어려울 수 있다.

---

### [핵심]

Route Focus 대상:

- `h1`
- `main`
- page container
- route announcement
- document title update
- loading state
- skip link target

검토 상황:

- Link navigation
- programmatic navigate
- redirect
- protected route
- form submit 후 이동
- modal route
- error page

---

### [실무]

Route heading focus 예:

```tsx
function PageTitle({ children }) {
  const headingRef = useRef<HTMLHeadingElement>(null);
  const location = useLocation();

  useEffect(() => {
    headingRef.current?.focus();
  }, [location.pathname]);

  return (
    <h1 ref={headingRef} tabIndex={-1}>
      {children}
    </h1>
  );
}
```

Page 예:

```jsx
<main id="main-content">
  <PageTitle>축제 목록</PageTitle>
  <FestivalList />
</main>
```

실무 기준:

- SPA route 변경 후 focus 위치 검토
- h1 또는 main으로 focus 이동 고려
- document title도 route에 맞게 갱신
- focus 이동이 과도하면 사용자 흐름 방해 가능
- modal 내부 route나 nested route는 별도 기준 필요
- skip link target과 route focus target 일관성 유지

---

### [FAQ]

Q. SPA에서 route 이동 후 focus가 왜 문제야?
A. 전체 페이지 새로고침이 아니므로 focus가 이전 위치에 남아 사용자가 새 화면 전환을 인식하기 어려울 수 있다.

Q. route 이동 후 focus는 어디로 가야 해?
A. 페이지 제목 h1 또는 main 영역으로 focus 이동을 검토할 수 있다.

Q. route 이동마다 focus를 강제로 옮겨도 돼?
A. 필요할 수 있지만 사용자 흐름을 방해하지 않도록 상황에 맞게 적용한다.

Q. document title도 접근성과 관련 있어?
A. 관련 있다. 사용자가 현재 페이지를 이해하는 데 도움이 된다.

---

# 11. Component Keyboard Patterns

## 11.1 Modal Keyboard Pattern

### [개념]

Modal Keyboard Pattern은 Modal이 열렸을 때 keyboard 사용자가 Modal 내용을 이해하고, 내부를 조작하고, 안전하게 닫을 수 있게 하는 기준이다.

---

### [핵심]

Modal keyboard 기준:

- open 시 Modal 내부 focus 이동
- Tab 내부 순환
- Shift+Tab 내부 순환
- Escape 닫기
- 닫기 버튼 제공
- close 후 trigger focus return
- background focus 방지
- confirm / cancel button keyboard 조작

---

### [실무]

Modal Flow:

```text
Open Button Focus
→ Enter / Space
→ Modal Open
→ Focus Move to Dialog Title or First Control
→ Tab Through Dialog
→ Escape or Close Button
→ Modal Close
→ Focus Return to Open Button
```

Modal 구조:

```jsx
<section role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title" tabIndex={-1}>
    리뷰 삭제
  </h2>

  <p>삭제한 리뷰는 복구할 수 없습니다.</p>

  <button type="button" onClick={onCancel}>
    취소
  </button>

  <button type="button" onClick={onConfirm}>
    삭제
  </button>
</section>
```

실무 기준:

- Modal open 직후 focus 위치 명확화
- Modal 내부에서 Tab 순환 확인
- 닫기 버튼은 keyboard로 접근 가능
- Escape 닫기 지원 검토
- 닫은 후 trigger focus return
- 복잡한 Modal은 접근성 라이브러리 사용 고려

---

### [FAQ]

Q. Modal을 열면 focus는 어디로 가야 해?
A. Modal title, 첫 입력 필드, 첫 버튼 등 Modal 내부의 적절한 위치로 이동해야 한다.

Q. Modal 닫은 후 focus는 어디로 돌아가?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아간다.

Q. Modal에서 Tab이 배경으로 빠지면 문제야?
A. Modal이 열려 있는 동안 배경으로 focus가 빠지면 접근성 문제가 될 수 있다.

Q. Modal에는 닫기 버튼이 꼭 필요해?
A. 권장한다. Escape만으로 닫게 하는 것은 충분하지 않을 수 있다.

---

## 11.2 Dropdown Keyboard Pattern

### [개념]

Dropdown Keyboard Pattern은 Dropdown이 열리고 닫히는 상태와 내부 item 조작을 keyboard로 수행할 수 있게 하는 기준이다.

Dropdown은 trigger button, open state, menu item, focus 이동, Escape 닫기를 함께 검토해야 한다.

---

### [핵심]

Dropdown keyboard 기준:

- trigger는 `button`
- trigger focus 가능
- Enter / Space로 열기
- `aria-expanded` 동기화
- item keyboard 접근
- Escape 닫기
- 선택 후 닫기
- 닫은 후 trigger focus return
- hidden item focus 방지

---

### [실무]

Dropdown trigger:

```jsx
<button
  type="button"
  aria-haspopup="menu"
  aria-expanded={open}
  aria-controls="festival-menu"
  onClick={toggleOpen}
>
  메뉴
</button>
```

Menu 구조:

```jsx
{
  open && (
    <ul id="festival-menu" role="menu">
      <li>
        <button type="button" role="menuitem" onClick={onEdit}>
          수정
        </button>
      </li>
      <li>
        <button type="button" role="menuitem" onClick={onDelete}>
          삭제
        </button>
      </li>
    </ul>
  );
}
```

실무 기준:

- 단순 액션 목록이면 button item 사용
- navigation 목록이면 link item 사용
- open 상태와 `aria-expanded` 일치
- Dropdown 닫힌 상태에서 item focus 방지
- Escape로 닫기 고려
- item 선택 후 닫기 기준 통일
- 복잡한 Menu는 Arrow Key pattern 검토

---

### [FAQ]

Q. Dropdown trigger는 div로 만들어도 돼?
A. 권장하지 않는다. trigger는 button을 사용하는 것이 keyboard와 semantic 측면에서 안전하다.

Q. aria-expanded는 언제 바뀌어야 해?
A. 실제 Dropdown open 상태와 항상 일치해야 한다.

Q. Dropdown item은 button이야 Link야?
A. 액션이면 button, 페이지 이동이면 Link가 적합하다.

Q. Dropdown 닫힌 상태의 item에 focus가 가면 문제야?
A. 문제다. 보이지 않는 item에 keyboard focus가 가면 사용자가 혼란을 겪는다.

---

## 11.3 Tab Component Keyboard Pattern

### [개념]

Tab Component Keyboard Pattern은 여러 패널을 Tab으로 전환할 때 keyboard 사용자가 tablist, tab, tabpanel을 이해하고 조작할 수 있게 하는 기준이다.

Tab은 page route 이동이 아니라 같은 페이지 안의 content panel 전환에 적합하다.

---

### [핵심]

Tab keyboard 기준:

- `role="tablist"`
- `role="tab"`
- `role="tabpanel"`
- `aria-selected`
- `aria-controls`
- `aria-labelledby`
- Arrow Key navigation
- roving tabindex 고려
- selected panel 표시
- hidden panel focus 방지

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
    tabIndex={selectedTab === "review" ? 0 : -1}
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

실무 기준:

- 같은 페이지 내부 패널 전환이면 Tab 사용
- 페이지 수준 이동이면 Route / Link 사용
- 선택 상태는 `aria-selected`
- tab과 panel은 id로 연결
- hidden panel에 focus 가능한 요소가 남지 않게 처리
- Arrow Key navigation 고려
- 복잡하면 접근성 라이브러리 검토

---

### [FAQ]

Q. Tab은 button 여러 개만 있으면 돼?
A. 기본 전환은 가능하지만 접근성을 위해 role, aria-selected, tabpanel 연결을 고려해야 한다.

Q. Tab과 Route는 어떻게 구분해?
A. 같은 페이지 안의 패널 전환이면 Tab, 페이지 수준 이동이면 Route가 적합하다.

Q. Tab에 Arrow Key가 필요해?
A. 접근성 있는 Tab 패턴에서는 Arrow Key 이동을 고려하는 것이 좋다.

Q. hidden tabpanel에 focus가 가면 문제야?
A. 문제다. 보이지 않는 패널 내부 요소에 focus가 가지 않게 해야 한다.

---

# 12. Keyboard Testing

## 12.1 Manual Keyboard Check

### [개념]

Manual Keyboard Check는 실제 keyboard만 사용해 UI를 조작하며 접근성 문제를 찾는 절차다.

자동화 도구는 keyboard 흐름 전체와 focus 맥락을 완전히 검증하지 못하므로 수동 점검이 필요하다.

---

### [핵심]

수동 점검 항목:

- Tab 이동 가능
- Shift+Tab 역방향 가능
- 현재 focus 위치 보임
- Enter / Space 실행 가능
- Escape 닫기 가능
- Form 입력 가능
- Modal 내부 focus 제한
- Dropdown 조작 가능
- Tab Component 조작 가능
- Route 이동 후 focus 확인
- focus lost 없음
- keyboard trap 없음

---

### [실무]

Manual Check Flow:

```text
마우스 사용 금지
→ Tab으로 Header Navigation 이동
→ Main Content 이동
→ Form 입력
→ Submit 실행
→ Error 표시 확인
→ Modal 열기
→ Modal 내부 Tab 순환 확인
→ Escape 닫기
→ Focus Return 확인
→ Dropdown 열기 / 닫기 확인
```

실무 우선 점검 화면:

- Login
- Signup
- Search
- Payment
- Review Form
- Festival Detail
- Modal
- Dropdown
- Navigation
- Admin Table
- File Upload
- Calendar

실무 기준:

- 마우스 없이 핵심 user flow 완료 가능해야 함
- focus가 화면 밖으로 사라지지 않아야 함
- keyboard trap이 없어야 함
- focus visible이 모든 interactive element에 보여야 함
- route 전환 후 focus 위치를 확인
- 수동 점검 결과는 코드 수정 항목으로 연결

---

### [FAQ]

Q. 자동화 도구만 돌리면 keyboard 접근성 테스트 끝이야?
A. 아니다. 실제 Tab 순서, focus 흐름, keyboard trap은 수동 확인이 필요하다.

Q. keyboard 수동 점검은 어디부터 해?
A. 로그인, 회원가입, 검색, 결제, 주요 Form, Modal 같은 핵심 흐름부터 확인한다.

Q. keyboard trap은 어떻게 발견해?
A. Tab, Shift+Tab, Escape, 닫기 버튼으로 빠져나갈 수 있는지 확인한다.

Q. focus visible은 어떻게 확인해?
A. Tab 이동하면서 현재 focus 위치가 시각적으로 명확히 보이는지 확인한다.

---

## 12.2 Testing Library Keyboard Test

### [개념]

Testing Library Keyboard Test는 `userEvent.keyboard`, `userEvent.tab` 등을 사용해 keyboard interaction을 코드로 검증하는 방식이다.

모든 keyboard 접근성을 자동화할 수는 없지만 주요 동작 검증에 도움이 된다.

---

### [핵심]

테스트 대상:

- Tab focus 이동
- Enter 실행
- Space 실행
- Escape 닫기
- checkbox toggle
- radio selection
- form submit
- dropdown open / close
- modal close
- focus return

사용 도구:

- `userEvent.tab()`
- `userEvent.keyboard()`
- `toHaveFocus()`
- `getByRole`
- `getByLabelText`

---

### [실무]

Tab focus 테스트:

```tsx
test("Tab으로 로그인 Form을 이동할 수 있다", async () => {
  render(<LoginForm />);

  await user.tab();
  expect(screen.getByLabelText("이메일")).toHaveFocus();

  await user.tab();
  expect(screen.getByLabelText("비밀번호")).toHaveFocus();

  await user.tab();
  expect(screen.getByRole("button", { name: "로그인" })).toHaveFocus();
});
```

Escape 닫기 테스트:

```tsx
test("Escape로 Modal을 닫고 trigger로 focus가 돌아간다", async () => {
  render(<ReviewDialog />);

  const openButton = screen.getByRole("button", { name: "리뷰 작성" });

  await user.click(openButton);
  expect(screen.getByRole("dialog")).toBeInTheDocument();

  await user.keyboard("{Escape}");
  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  expect(openButton).toHaveFocus();
});
```

Space toggle 테스트:

```tsx
test("Space로 checkbox를 토글할 수 있다", async () => {
  render(<TermsCheckbox />);

  const checkbox = screen.getByRole("checkbox", {
    name: /이용약관에 동의합니다/,
  });

  checkbox.focus();
  await user.keyboard("[Space]");

  expect(checkbox).toBeChecked();
});
```

실무 기준:

- keyboard test도 role / label query 우선
- focus 흐름은 `toHaveFocus`로 확인
- Modal / Dropdown / Form 주요 흐름 우선 테스트
- 모든 수동 점검을 테스트로 대체할 수는 없음
- testId 중심 테스트는 접근성 검증을 약화할 수 있음

---

### [FAQ]

Q. keyboard 접근성도 Testing Library로 테스트할 수 있어?
A. 일부 가능하다. userEvent.tab, userEvent.keyboard, toHaveFocus를 사용할 수 있다.

Q. keyboard 테스트에서 무엇을 확인해?
A. focus 이동, Enter / Space 실행, Escape 닫기, focus return 등을 확인한다.

Q. keyboard 테스트가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 실제 화면의 focus visible, scroll, 복잡한 흐름은 수동 확인이 필요하다.

Q. keyboard 테스트도 getByRole을 써야 해?
A. 권장한다. 사용자가 인식하는 role과 name 기준으로 테스트하는 것이 좋다.

---

# 13. Keyboard Accessibility Review

## 13.1 Review Checklist

### [개념]

Keyboard Accessibility Review는 UI가 keyboard만으로 사용 가능한지 검토하는 과정이다.

Review Agent는 클릭 가능한 UI를 발견하면 keyboard로 focus 가능하고 실행 가능한지 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 마우스 없이 주요 기능을 사용할 수 있는가?
- [ ] 클릭 가능한 요소가 keyboard focus 가능한가?
- [ ] 클릭 액션에 button을 사용했는가?
- [ ] 페이지 이동에 Link 또는 a를 사용했는가?
- [ ] div onClick / span onClick 남용이 없는가?
- [ ] Enter / Space 실행이 역할과 일치하는가?
- [ ] Escape로 Modal / Dropdown을 닫을 수 있는가?
- [ ] focus visible이 모든 interactive element에 보이는가?
- [ ] outline none만 있고 대체 focus style이 없는 코드는 없는가?
- [ ] Tab Order가 시각적 흐름과 자연스러운가?
- [ ] 양수 tabindex를 사용하지 않았는가?
- [ ] hidden element에 focus가 가지 않는가?
- [ ] Modal open 시 내부로 focus가 이동하는가?
- [ ] Modal 내부에서 focus가 적절히 제한되는가?
- [ ] Modal close 후 trigger로 focus가 복귀하는가?
- [ ] Dropdown open 상태와 aria-expanded가 일치하는가?
- [ ] Dropdown item을 keyboard로 조작할 수 있는가?
- [ ] Tab Component의 aria-selected와 focus가 관리되는가?
- [ ] Form submit 실패 시 focus 이동 기준이 있는가?
- [ ] Route 이동 후 focus 위치를 검토했는가?
- [ ] keyboard trap이 없는가?
- [ ] userEvent keyboard test가 필요한 핵심 흐름에 있는가?
```

---

### [실무]

Review Flow:

```text
Interactive Element 확인
→ Native Element 사용 여부 확인
→ Focus 가능 여부 확인
→ Focus Visible 확인
→ Enter / Space 실행 확인
→ Tab Order 확인
→ Escape 닫기 확인
→ Focus Management 확인
→ Keyboard Trap 확인
→ Testing Query / Keyboard Test 확인
```

대표 수정 패턴:

```text
문제: div onClick 사용
해결: button type="button" 사용
```

```text
문제: outline none으로 focus가 보이지 않음
해결: :focus-visible 대체 style 제공
```

```text
문제: Modal 닫은 후 focus lost
해결: trigger ref로 focus return
```

```text
문제: hidden dropdown item에 focus 가능
해결: 닫힌 상태에서는 unmount 또는 focus 제외
```

---

### [FAQ]

Q. Keyboard Review에서 가장 먼저 볼 것은?
A. clickable element가 native button/link인지, focus 가능한지, focus visible이 있는지 먼저 본다.

Q. div onClick은 Review에서 잡아야 해?
A. 잡아야 한다. keyboard 조작 누락 가능성이 높다.

Q. outline none은 무조건 문제야?
A. 대체 focus style 없이 제거하면 문제다.

Q. keyboard trap은 어떻게 확인해?
A. Tab, Shift+Tab, Escape, 닫기 버튼, focus return을 수동으로 확인한다.

---

# 14. Common Keyboard Accessibility Mistakes

## 14.1 Keyboard Anti Patterns

### [개념]

Keyboard Anti Pattern은 화면상 마우스로는 동작하지만 keyboard 사용자에게 조작 불가, focus lost, focus invisible, keyboard trap을 유발하는 구현 방식이다.

---

### [핵심]

자주 발생하는 실수:

- `div onClick`을 button처럼 사용
- `span onClick`을 button처럼 사용
- `role="button"`만 붙이고 keyboard 미구현
- `tabIndex={0}`만 붙이고 Enter / Space 미구현
- `outline: none`만 적용
- focus style이 hover와만 연결
- 양수 `tabIndex` 남용
- CSS order로 시각 순서와 Tab 순서 불일치
- hidden dropdown item에 focus 가능
- Modal open 시 focus 이동 없음
- Modal close 후 focus return 없음
- Escape 닫기 없음
- 닫기 버튼 없음
- focus trap 구현 오류
- keyboard trap 발생
- route 이동 후 focus가 이전 trigger에 남음
- form submit 실패 후 오류 위치를 찾기 어려움
- custom select / tab / menu keyboard 구현 누락

---

### [실무]

Anti Pattern:

```jsx
<div onClick={onOpen}>메뉴 열기</div>
```

개선:

```jsx
<button type="button" onClick={onOpen}>
  메뉴 열기
</button>
```

Anti Pattern:

```css
*:focus {
  outline: none;
}
```

개선:

```css
:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

Anti Pattern:

```jsx
{
  open && <Modal />;
}
```

개선 기준:

```text
Modal open
→ focus move inside
→ focus trap
→ Escape close
→ close button
→ focus return
```

Anti Pattern:

```jsx
<div className={open ? "menu open" : "menu"}>
  <button>수정</button>
  <button>삭제</button>
</div>
```

개선 기준:

```text
Dropdown closed
→ hidden items should not be focusable
→ unmount or inert / hidden handling
```

---

### [FAQ]

Q. Keyboard 접근성 초보가 가장 많이 하는 실수는?
A. div onClick 사용, focus outline 제거, Modal focus 관리 누락, Dropdown keyboard 누락이 많다.

Q. role="button"만 붙이면 왜 부족해?
A. keyboard activation과 focus style을 직접 구현해야 하기 때문이다.

Q. hidden item에 focus가 가면 왜 문제야?
A. 사용자가 화면에서 보이지 않는 위치로 이동했다고 느껴 조작 맥락을 잃을 수 있다.

Q. route 이동 후 focus가 이상하면 접근성 문제야?
A. 가능성이 있다. SPA에서는 route 변경 후 focus 위치를 별도로 검토해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Keyboard Accessibility는 왜 중요해?
A. 마우스 없이도 사용자가 주요 기능을 조작할 수 있어야 하기 때문이다.

Q. Keyboard Accessibility는 무엇을 확인해?
A. Tab 이동, Shift+Tab 이동, Enter / Space 실행, Escape 닫기, focus visible, keyboard trap 여부를 확인한다.

Q. 마우스로 잘 되면 키보드도 되는 거 아니야?
A. 아니다. div onClick, custom dropdown, modal 등은 keyboard 조작이 누락될 수 있다.

Q. 키보드 접근성은 뭘 먼저 확인해?
A. Tab 이동, Enter / Space 실행, Escape 닫기, focus visible 여부부터 확인한다.

Q. Native Element를 우선해야 하는 이유는?
A. 기본 role, keyboard 동작, focus 동작이 이미 제공되기 때문에 접근성 누락 위험이 낮다.

Q. button은 keyboard로 어떻게 실행돼?
A. 일반적으로 Enter와 Space로 실행된다.

Q. Link는 keyboard로 어떻게 실행돼?
A. 일반적으로 Enter로 이동한다.

Q. checkbox는 keyboard로 어떻게 조작해?
A. Tab으로 focus하고 Space로 checked 상태를 토글한다.

Q. radio group은 keyboard로 어떻게 조작해?
A. Native radio는 Tab으로 group에 접근하고 Arrow Key로 option 이동이 가능하다.

Q. div에 role="button"을 붙이면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 Enter / Space keyboard 동작은 직접 구현해야 한다.

Q. div onClick을 keyboard 접근성 있게 만들 수 있어?
A. 가능은 하지만 role, tabIndex, Enter / Space 처리, focus style을 직접 구현해야 한다. 가능하면 button을 사용한다.

Q. role과 tabIndex만 있으면 충분해?
A. 아니다. keyboard activation과 상태 동기화가 필요하다.

Q. Custom Button을 만들면 안 돼?
A. 가능하지만 내부는 native button을 사용하는 방식이 가장 안전하다.

Q. Space key 처리는 왜 필요해?
A. button은 Space로 실행되므로 custom button도 유사한 조작을 제공해야 한다.

Q. Tab Order는 무엇 기준으로 정해져?
A. 기본적으로 DOM 순서와 focus 가능한 요소 기준으로 정해진다.

Q. tabindex를 많이 쓰면 키보드 순서를 쉽게 조정할 수 있지 않아?
A. 양수 tabindex는 유지보수를 어렵게 만들 수 있다. DOM 순서를 올바르게 설계하는 것이 우선이다.

Q. CSS flex order를 쓰면 Tab 순서도 바뀌어?
A. 보통 DOM 순서는 그대로라서 시각 순서와 Tab 순서가 어긋날 수 있다.

Q. disabled button은 Tab으로 focus돼?
A. 일반적으로 disabled button은 focus 대상에서 제외된다.

Q. tabindex="-1"은 언제 써?
A. 사용자 Tab 순서에는 포함하지 않지만 코드로 focus를 이동해야 하는 요소에 사용할 수 있다.

Q. tabindex="0"은 언제 써?
A. 원래 focus되지 않는 요소를 DOM 순서에 따라 focus 가능하게 만들 때 제한적으로 사용한다.

Q. 양수 tabindex는 왜 피해야 해?
A. 전체 focus 순서를 복잡하게 만들고 유지보수를 어렵게 하기 때문이다.

Q. focus 순서를 바꾸고 싶으면 어떻게 해?
A. 먼저 DOM 순서를 자연스럽게 조정하는 것이 좋다.

Q. Focus Visible이 뭐야?
A. 현재 keyboard focus가 어디에 있는지 사용자가 볼 수 있게 하는 기준이다.

Q. focus outline을 없애면 디자인이 깔끔해지는데 괜찮아?
A. 권장하지 않는다. 키보드 사용자가 현재 위치를 알 수 없게 된다.

Q. focus와 hover는 같은 거야?
A. 다르다. hover는 마우스 상태이고 focus는 키보드나 프로그램적 초점 상태다.

Q. :focus-visible은 언제 써?
A. keyboard focus에 적합한 focus style을 제공할 때 사용할 수 있다.

Q. focus indicator도 색상 대비가 필요해?
A. 필요하다. 현재 위치를 명확히 볼 수 있어야 한다.

Q. Focus Style은 Component마다 따로 만들면 돼?
A. 가능하지만 Design System에서는 공통 focus rule을 제공하는 것이 일관성에 좋다.

Q. outline 대신 box-shadow를 써도 돼?
A. 가능하다. 다만 충분히 보이고 잘리지 않아야 한다.

Q. disabled 요소에도 focus style이 필요해?
A. 일반 disabled 요소는 focus 대상에서 제외되는 경우가 많다. disabled 상태는 시각적으로 명확해야 한다.

Q. Button은 어떤 키로 실행돼?
A. 일반적으로 Enter와 Space로 실행된다.

Q. Link는 어떤 키로 실행돼?
A. 일반적으로 Enter로 이동한다.

Q. Custom Button에서 Enter만 처리하면 돼?
A. Button 역할이면 Space 처리도 고려해야 한다.

Q. Space를 누르면 페이지가 움직여?
A. Custom Element에서는 Space가 스크롤을 유발할 수 있어 preventDefault가 필요할 수 있다.

Q. Escape Key는 언제 써?
A. Modal, Dropdown, Popover, Menu 같은 임시 UI를 닫는 데 사용한다.

Q. Modal은 Escape로 닫혀야 해?
A. 일반적으로 Escape 닫기를 제공하는 것이 좋다. 단, 필수 확인 Dialog는 정책을 명확히 해야 한다.

Q. Dropdown도 Escape로 닫혀야 해?
A. 권장한다. 열린 메뉴에서 keyboard 사용자가 빠져나갈 수 있어야 한다.

Q. Escape로 닫은 후 focus는 어디로 가야 해?
A. 일반적으로 해당 UI를 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. 닫기 버튼이 있으면 Escape는 없어도 돼?
A. 닫기 버튼은 필수에 가깝고 Escape도 함께 지원하면 keyboard 사용성이 좋아진다.

Q. 모든 목록에 Arrow Key를 구현해야 해?
A. 아니다. 일반 링크 목록이나 버튼 목록은 Tab 이동으로 충분한 경우가 많다.

Q. Radio Group은 Arrow Key를 직접 구현해야 해?
A. Native radio를 사용하면 브라우저가 기본적으로 지원한다.

Q. Tab은 Arrow Key가 필요해?
A. 접근성 있는 Tab 패턴에서는 Arrow Key 이동을 고려하는 것이 좋다.

Q. Focus와 selected는 같은 거야?
A. 아니다. focus는 현재 keyboard 위치이고 selected는 선택된 상태다.

Q. Roving TabIndex는 언제 써?
A. Tab, Menu, Listbox처럼 복합 widget 내부 항목을 방향키로 이동하게 할 때 사용한다.

Q. 모든 버튼 목록에 Roving TabIndex를 써야 해?
A. 아니다. 일반 버튼 목록은 Tab 이동만으로 충분한 경우가 많다.

Q. tabIndex가 -1이면 focus가 불가능해?
A. Tab 순서에서는 제외되지만 코드로 focus를 줄 수 있다.

Q. Roving TabIndex가 어려운 이유는?
A. focus index, selected state, keyboard event, ref 관리가 함께 필요하기 때문이다.

Q. Programmatic Focus는 언제 필요해?
A. Modal open, Form 오류, Route 이동, 동적 UI 변경처럼 사용자가 위치를 잃기 쉬운 상황에 필요할 수 있다.

Q. focus를 자동 이동하면 항상 좋아?
A. 아니다. 사용자의 작업 흐름을 방해할 수 있으므로 필요한 경우에만 사용한다.

Q. focus 대상에 tabIndex="-1"을 붙이는 이유는?
A. Tab 순서에는 포함하지 않지만 코드로 focus를 이동하기 위해서다.

Q. hidden 요소에 focus를 줘도 돼?
A. 안 된다. 사용자가 볼 수 없거나 접근할 수 없는 요소에 focus가 가면 혼란을 만든다.

Q. Focus Return이 뭐야?
A. Modal이나 Dropdown을 닫은 후 focus를 해당 UI를 열었던 trigger 요소로 되돌리는 기준이다.

Q. Modal 닫은 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아가는 것이 좋다.

Q. Dropdown 닫은 후 focus는 어디로 가야 해?
A. Dropdown trigger button으로 돌아가는 것이 자연스럽다.

Q. 삭제 후 trigger가 사라지면 focus는 어디로 가?
A. 다음 항목, 이전 항목, 목록 제목 등 사용자가 이어서 조작할 수 있는 위치로 이동한다.

Q. Focus Return이 없으면 어떤 문제가 생겨?
A. keyboard 사용자가 현재 위치를 잃고 다음 조작을 하기 어려워질 수 있다.

Q. Focus Trap이 뭐야?
A. Modal처럼 특정 UI가 열린 동안 keyboard focus를 해당 UI 내부에 제한하는 패턴이다.

Q. Modal 안에 focus가 갇히는 건 문제야?
A. Modal이 열려 있는 동안 내부에 focus를 제한하는 것은 정상이다. 하지만 닫을 방법이 없으면 문제다.

Q. 모든 팝업에 focus trap이 필요해?
A. 아니다. Modal dialog에는 필요하지만 작은 Dropdown이나 Tooltip은 패턴에 따라 다르다.

Q. Focus Trap 구현이 어려우면 어떻게 해?
A. 접근성 검증된 dialog library나 headless component를 검토할 수 있다.

Q. Keyboard Trap이 뭐야?
A. 사용자가 keyboard로 특정 UI 영역에 갇혀 빠져나갈 수 없는 접근성 문제다.

Q. Focus Trap과 Keyboard Trap은 뭐가 달라?
A. Focus Trap은 Modal 내부 focus 제한 같은 의도된 패턴이고 Keyboard Trap은 사용자가 빠져나갈 수 없는 접근성 문제다.

Q. Keyboard Trap은 어떻게 찾아?
A. Tab, Shift+Tab, Escape, 닫기 버튼, focus return을 직접 확인한다.

Q. Modal focus trap은 괜찮고 keyboard trap은 왜 문제야?
A. Modal focus trap은 닫을 방법이 있어야 정상이다. 닫을 방법이 없으면 keyboard trap이 된다.

Q. Dropdown에서 Tab을 누르면 이상하게 이동해?
A. 열린 메뉴 item의 focus 순서와 닫힘 처리를 확인해야 한다.

Q. Skip Link는 왜 필요해?
A. keyboard 사용자가 반복되는 메뉴를 매번 거치지 않고 본문으로 바로 이동할 수 있게 하기 위해서다.

Q. Skip Link는 항상 보여야 해?
A. 보통 기본적으로 숨기고 keyboard focus 시 보이게 처리한다.

Q. Skip Link는 어디로 연결해?
A. 일반적으로 main 영역의 id로 연결한다.

Q. SPA에서도 Skip Link가 필요해?
A. 반복 navigation이 있는 SPA에서도 유용하다.

Q. SPA에서 route 이동 후 focus가 왜 문제야?
A. 전체 페이지 새로고침이 아니므로 focus가 이전 위치에 남아 사용자가 새 화면 전환을 인식하기 어려울 수 있다.

Q. route 이동 후 focus는 어디로 가야 해?
A. 페이지 제목 h1 또는 main 영역으로 focus 이동을 검토할 수 있다.

Q. route 이동마다 focus를 강제로 옮겨도 돼?
A. 필요할 수 있지만 사용자 흐름을 방해하지 않도록 상황에 맞게 적용한다.

Q. document title도 접근성과 관련 있어?
A. 관련 있다. 사용자가 현재 페이지를 이해하는 데 도움이 된다.

Q. Modal을 열면 focus는 어디로 가야 해?
A. Modal title, 첫 입력 필드, 첫 버튼 등 Modal 내부의 적절한 위치로 이동해야 한다.

Q. Modal에서 Tab이 배경으로 빠지면 문제야?
A. Modal이 열려 있는 동안 배경으로 focus가 빠지면 접근성 문제가 될 수 있다.

Q. Modal에는 닫기 버튼이 꼭 필요해?
A. 권장한다. Escape만으로 닫게 하는 것은 충분하지 않을 수 있다.

Q. Dropdown trigger는 div로 만들어도 돼?
A. 권장하지 않는다. trigger는 button을 사용하는 것이 keyboard와 semantic 측면에서 안전하다.

Q. Dropdown item은 button이야 Link야?
A. 액션이면 button, 페이지 이동이면 Link가 적합하다.

Q. Dropdown 닫힌 상태의 item에 focus가 가면 문제야?
A. 문제다. 보이지 않는 item에 keyboard focus가 가면 사용자가 혼란을 겪는다.

Q. Tab은 button 여러 개만 있으면 돼?
A. 기본 전환은 가능하지만 접근성을 위해 role, aria-selected, tabpanel 연결을 고려해야 한다.

Q. Tab과 Route는 어떻게 구분해?
A. 같은 페이지 안의 패널 전환이면 Tab, 페이지 수준 이동이면 Route가 적합하다.

Q. hidden tabpanel에 focus가 가면 문제야?
A. 문제다. 보이지 않는 패널 내부 요소에 focus가 가지 않게 해야 한다.

Q. 자동화 도구만 돌리면 keyboard 접근성 테스트 끝이야?
A. 아니다. 실제 Tab 순서, focus 흐름, keyboard trap은 수동 확인이 필요하다.

Q. keyboard 수동 점검은 어디부터 해?
A. 로그인, 회원가입, 검색, 결제, 주요 Form, Modal 같은 핵심 흐름부터 확인한다.

Q. keyboard 접근성도 Testing Library로 테스트할 수 있어?
A. 일부 가능하다. userEvent.tab, userEvent.keyboard, toHaveFocus를 사용할 수 있다.

Q. keyboard 테스트에서 무엇을 확인해?
A. focus 이동, Enter / Space 실행, Escape 닫기, focus return 등을 확인한다.

Q. keyboard 테스트가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 실제 화면의 focus visible, scroll, 복잡한 흐름은 수동 확인이 필요하다.

Q. Keyboard Review에서 가장 먼저 볼 것은?
A. clickable element가 native button/link인지, focus 가능한지, focus visible이 있는지 먼저 본다.

Q. div onClick은 Review에서 잡아야 해?
A. 잡아야 한다. keyboard 조작 누락 가능성이 높다.

Q. outline none은 무조건 문제야?
A. 대체 focus style 없이 제거하면 문제다.

Q. Keyboard 접근성 초보가 가장 많이 하는 실수는?
A. div onClick 사용, focus outline 제거, Modal focus 관리 누락, Dropdown keyboard 누락이 많다.
