# Frontend Accessibility Part08 - Component Pattern Accessibility

---

# 1. Component Pattern Accessibility

## 1.1 Component Accessibility Purpose

### [개념]

Component Pattern Accessibility는 Button, Link, Modal, Dropdown, Tab, Accordion, Tooltip, Toast, Pagination 같은 공통 UI Component가 keyboard, screen reader, focus, state 기준을 만족하도록 설계하는 기준이다.

Frontend Component는 한 번 잘못 만들면 여러 화면에 같은 접근성 문제가 반복된다.

공통 Component는 시각적 재사용성뿐 아니라 semantic role, accessible name, keyboard interaction, focus management, ARIA state를 함께 포함해야 한다.

---

### [핵심]

Component Accessibility 핵심 기준:

- Native HTML 우선
- role과 실제 동작 일치
- accessible name 제공
- keyboard interaction 제공
- focus visible 유지
- focus management 검토
- ARIA state 동기화
- loading / disabled / error 상태 전달
- color only meaning 방지
- Testing Library role query 검증
- reusable component default 안전성 확보

공통 Component 검토 대상:

- Button
- IconButton
- Link
- Modal / Dialog
- Dropdown
- Accordion
- Tab
- Tooltip
- Toast
- Pagination
- Breadcrumb
- Card
- Table
- Form Control
- File Upload
- Search Box

---

### [실무]

Component Accessibility 설계 Flow:

```text
Component 목적 확인
→ Native HTML 선택
→ Accessible Name 제공
→ Keyboard 조작 확인
→ Focus Visible 적용
→ Disabled / Loading 상태 설계
→ ARIA 상태 동기화
→ Error / Status Message 연결
→ Testing Library Query 검증
→ Review Checklist 적용
```

실무 기준:

- 공통 Button은 기본 `type="button"` 사용
- Form Submit Button만 명시적으로 `type="submit"` 전달
- IconButton은 `aria-label` 필수
- Modal은 focus move / focus trap / focus return 포함
- Dropdown은 trigger button과 `aria-expanded` 동기화
- Tab은 `aria-selected`, `aria-controls`, `tabpanel` 연결
- Toast는 중요한 상태면 `role="status"` 또는 `role="alert"` 검토
- Card 전체 클릭 패턴은 Link 중복과 focus 순서 검토
- 공통 Component는 `getByRole`로 찾을 수 있어야 함

---

### [FAQ]

Q. Component Accessibility는 왜 중요해?
A. 공통 Component 하나의 접근성 문제가 여러 화면에 반복되기 때문에 설계 단계에서 기준을 잡아야 한다.

Q. 공통 Component는 디자인만 맞으면 돼?
A. 아니다. semantic role, keyboard, focus, accessible name, ARIA state까지 포함해야 한다.

Q. Component 접근성은 어디서 먼저 잡아야 해?
A. Button, Link, Form Control, Modal, Dropdown처럼 자주 재사용되는 Component부터 잡는 것이 좋다.

Q. 공통 Component 테스트는 어떻게 해?
A. Testing Library의 getByRole, getByLabelText, userEvent keyboard test로 핵심 동작을 검증한다.

---

# 2. Button Component

## 2.1 Button Component Rules

### [개념]

Button Component는 사용자가 현재 화면의 상태를 변경하거나 action을 실행하는 기본 interactive component다.

Button은 접근성의 가장 기본 단위이며, 잘못 설계되면 Form, Modal, Dropdown, Toast, Table Action 전체에 영향을 준다.

---

### [핵심]

Button 기준:

- native `button`
- 기본 `type="button"`
- submit일 때만 `type="submit"`
- visible text 또는 accessible name
- keyboard Enter / Space 실행
- focus visible
- disabled state
- loading state
- icon handling
- color only 상태 금지

Button 사용 대상:

- 저장
- 삭제
- 취소
- 검색
- 필터 초기화
- 모달 열기
- 드롭다운 열기
- 좋아요 토글
- 재시도
- 업로드
- 결제하기

---

### [실무]

공통 Button 예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({
  type = "button",
  disabled = false,
  loading = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      type={type}
      disabled={disabled || loading}
      aria-busy={loading}
      onClick={onClick}
    >
      {loading ? "처리 중..." : children}
    </button>
  );
}
```

Submit Button:

```jsx
<Button type="submit" loading={saving}>
  저장
</Button>
```

Action Button:

```jsx
<Button onClick={onResetFilter}>필터 초기화</Button>
```

실무 기준:

- 기본 type은 `"button"`
- Form 제출 전용일 때만 `"submit"`
- loading 중에는 텍스트로 상태 제공
- disabled 이유가 불명확하면 helper text 제공
- focus style은 공통 Button에 포함
- Icon과 text가 함께 있으면 icon은 `aria-hidden`
- button을 Link처럼 사용하지 않음

---

### [FAQ]

Q. 공통 Button의 기본 type은 뭐가 좋아?
A. 의도하지 않은 Form submit을 막기 위해 type="button"을 기본값으로 두는 것이 좋다.

Q. Button loading 상태는 어떻게 처리해?
A. 버튼 텍스트를 “저장 중...”처럼 바꾸고 disabled 또는 aria-busy를 고려한다.

Q. Button과 Link는 어떻게 구분해?
A. Button은 action 실행이고 Link는 페이지나 위치 이동이다.

Q. disabled Button에는 이유를 꼭 써야 해?
A. 사용자가 왜 사용할 수 없는지 알기 어렵다면 helper text나 안내 문구를 제공하는 것이 좋다.

---

## 2.2 IconButton Component

### [개념]

IconButton은 시각적 텍스트 없이 아이콘만으로 기능을 나타내는 Button Component다.

IconButton은 반드시 accessible name을 가져야 하며, 내부 icon은 보통 장식 처리한다.

---

### [핵심]

IconButton 기준:

- native `button`
- `type="button"`
- `aria-label` 필수
- icon `aria-hidden`
- focus visible
- disabled state
- pressed state
- loading state
- repeated icon context
- target name 포함 고려

사용 대상:

- 닫기
- 메뉴 열기
- 알림 열기
- 검색
- 공유
- 삭제
- 수정
- 좋아요
- 이전 / 다음
- 지도 확대 / 축소

---

### [실무]

공통 IconButton 예:

```tsx
type IconButtonProps = {
  label: string;
  children: React.ReactNode;
  disabled?: boolean;
  pressed?: boolean;
  onClick?: () => void;
};

function IconButton({
  label,
  children,
  disabled = false,
  pressed,
  onClick,
}: IconButtonProps) {
  return (
    <button
      type="button"
      aria-label={label}
      aria-pressed={pressed}
      disabled={disabled}
      onClick={onClick}
    >
      <span aria-hidden="true">{children}</span>
    </button>
  );
}
```

닫기 버튼:

```jsx
<IconButton label="닫기" onClick={onClose}>
  <CloseIcon />
</IconButton>
```

좋아요 토글:

```jsx
<IconButton
  label={liked ? "좋아요 취소" : "좋아요"}
  pressed={liked}
  onClick={toggleLike}
>
  <HeartIcon />
</IconButton>
```

반복 삭제 버튼:

```jsx
<IconButton label={`${review.authorName} 리뷰 삭제`} onClick={onDelete}>
  <TrashIcon />
</IconButton>
```

실무 기준:

- `aria-label` 없는 IconButton 금지
- icon 자체에 이름을 주기보다 button에 이름 제공
- toggle button은 `aria-pressed` 검토
- 반복되는 IconButton은 대상 이름 포함
- loading 중 icon만 spinner로 바꾸지 말고 상태 text 전략 검토
- destructive action은 label이 명확해야 함

---

### [FAQ]

Q. IconButton에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. aria-label은 icon에 붙여?
A. 아니다. 조작 대상인 button에 붙이는 것이 적합하다.

Q. 좋아요 같은 toggle button은 어떻게 표현해?
A. 상태에 따라 label을 바꾸거나 aria-pressed를 사용해 눌림 상태를 전달할 수 있다.

Q. 같은 삭제 아이콘이 여러 개 있으면?
A. “리뷰 삭제”, “댓글 삭제”처럼 대상이 드러나도록 accessible name을 구체화한다.

---

# 3. Link Component

## 3.1 Link Component Rules

### [개념]

Link Component는 페이지, route, URL, 문서 위치로 이동하는 interactive component다.

Link는 action 실행용 Button과 구분해야 하며, 링크 텍스트만 읽어도 이동 목적을 알 수 있어야 한다.

---

### [핵심]

Link 기준:

- `a href`
- React Router `Link`
- 의미 있는 link text
- focus visible
- visited / active 상태 선택
- current page `aria-current`
- external link 안내 선택
- repeated link text 주의
- button action 대체 금지

Link 사용 대상:

- 상세 페이지 이동
- 목록 페이지 이동
- 로그인 페이지 이동
- 회원가입 페이지 이동
- 외부 사이트 이동
- Breadcrumb
- Pagination
- Skip Link
- Anchor 이동

---

### [실무]

기본 Link:

```jsx
<Link to="/festivals">축제 목록 보기</Link>
```

상세 Link:

```jsx
<Link to={`/festivals/${festival.id}`}>{festival.title} 상세 보기</Link>
```

현재 페이지 Link:

```jsx
<NavLink to="/calendar" aria-current={isActive ? "page" : undefined}>
  캘린더
</NavLink>
```

External Link:

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  공식 홈페이지 새 창에서 열기
</a>
```

실무 기준:

- 이동은 Link 사용
- 삭제 / 저장 / 좋아요 같은 action은 Button 사용
- “여기를 클릭” 지양
- 반복되는 “자세히 보기”는 대상 이름 포함
- 현재 위치는 `aria-current` 고려
- 본문 링크는 색상만으로 구분하지 않음
- 외부 새 창 이동은 문구로 안내 고려

---

### [FAQ]

Q. Link Component는 언제 써?
A. 페이지, route, URL, 문서 위치로 이동할 때 사용한다.

Q. 삭제를 Link로 만들어도 돼?
A. 권장하지 않는다. 삭제는 현재 상태를 변경하는 action이므로 Button이 적합하다.

Q. 자세히 보기 링크를 반복해도 돼?
A. 가능하지만 목적지가 모호할 수 있으므로 대상 이름을 포함하는 것이 좋다.

Q. 현재 페이지 메뉴는 어떻게 표시해?
A. 시각적 active 표시와 함께 aria-current="page"를 사용할 수 있다.

---

# 4. Modal Dialog Component

## 4.1 Modal Component Rules

### [개념]

Modal Dialog Component는 사용자에게 중요한 정보, 입력, 확인 action을 현재 화면 위에 표시하는 overlay component다.

Modal이 열리면 사용자의 focus와 interaction 맥락은 Modal 내부로 이동해야 한다.

---

### [핵심]

Modal 기준:

- `role="dialog"` 또는 `role="alertdialog"`
- `aria-modal="true"`
- `aria-labelledby`
- `aria-describedby` 선택
- open 시 focus 이동
- focus trap
- close 시 focus return
- Escape 닫기
- 닫기 버튼
- background interaction 방지
- keyboard test

Modal 사용 대상:

- 리뷰 작성
- 삭제 확인
- 로그인 필요 안내
- 결제 확인
- 상세 설정
- 이미지 미리보기
- 권한 안내

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
  <h2 id="dialog-title" tabIndex={-1}>
    리뷰 작성
  </h2>

  <p id="dialog-description">축제 방문 경험을 작성해 주세요.</p>

  <button type="button" onClick={onClose}>
    닫기
  </button>
</section>
```

삭제 확인:

```jsx
<section
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="delete-title"
  aria-describedby="delete-description"
>
  <h2 id="delete-title">리뷰 삭제</h2>
  <p id="delete-description">삭제한 리뷰는 복구할 수 없습니다.</p>

  <button type="button" onClick={onCancel}>
    취소
  </button>
  <button type="button" onClick={onConfirm}>
    삭제
  </button>
</section>
```

Modal Flow:

```text
Trigger Focus
→ Modal Open
→ Focus Move Inside
→ Tab Stays Inside
→ Escape / Close Button
→ Modal Close
→ Focus Return to Trigger
```

실무 기준:

- Modal title은 accessible name으로 연결
- Modal open 직후 focus 위치 명확화
- Modal 내부에서 Tab 순환
- 배경 요소 focus 방지
- 닫기 버튼 제공
- Escape 닫기 지원 검토
- 닫은 후 trigger로 focus 복귀
- 중요한 확인 Modal은 `alertdialog` 검토
- 복잡한 Modal은 검증된 library 검토

---

### [FAQ]

Q. Modal에는 어떤 접근성 처리가 필요해?
A. role dialog, aria-modal, title 연결, focus 이동, focus trap, focus return, 닫기 버튼이 필요하다.

Q. Modal open 시 focus는 어디로 가야 해?
A. Modal title, 첫 입력 필드, 첫 버튼 등 Modal 내부의 적절한 위치로 이동해야 한다.

Q. Modal close 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아간다.

Q. aria-modal만 붙이면 Modal 접근성이 끝이야?
A. 아니다. focus management와 keyboard interaction이 함께 필요하다.

---

## 4.2 Confirm Dialog Component

### [개념]

Confirm Dialog는 삭제, 결제, 탈퇴, 취소처럼 사용자의 중요한 결정을 확인하는 Dialog다.

Confirm Dialog는 사용자가 action의 결과와 위험성을 이해하고 취소할 수 있어야 한다.

---

### [핵심]

Confirm Dialog 기준:

- 명확한 제목
- 결과 설명
- 취소 버튼
- 확인 버튼
- destructive action 명확화
- focus 위치 결정
- `role="alertdialog"` 고려
- Escape 닫기 정책
- focus return
- color only warning 금지

---

### [실무]

삭제 Confirm:

```jsx
<section
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="confirm-title"
  aria-describedby="confirm-description"
>
  <h2 id="confirm-title">리뷰를 삭제할까요?</h2>
  <p id="confirm-description">삭제한 리뷰는 복구할 수 없습니다.</p>

  <button type="button" onClick={onCancel}>
    취소
  </button>
  <button type="button" onClick={onConfirm}>
    삭제
  </button>
</section>
```

실무 기준:

- 제목은 질문형으로 명확하게 작성
- 설명은 결과와 위험을 전달
- 취소 action 제공
- 확인 button label은 “확인”보다 “삭제”, “결제하기”처럼 구체화
- destructive action은 색상만으로 구분하지 않음
- focus는 상황에 따라 취소 버튼 또는 제목에 배치
- 취소 / 확인 keyboard 조작 가능해야 함

---

### [FAQ]

Q. Confirm Dialog는 언제 alertdialog를 써?
A. 삭제나 결제처럼 중요한 결정을 즉시 인식해야 하는 경우 고려할 수 있다.

Q. 확인 버튼 문구는 “확인”이면 돼?
A. 가능하지만 “삭제”, “결제하기”처럼 실제 action을 명확히 쓰는 것이 좋다.

Q. 취소 버튼은 꼭 필요해?
A. 사용자가 action을 중단할 수 있도록 제공하는 것이 좋다.

Q. 삭제 Dialog에서 색상만 빨갛게 하면 충분해?
A. 아니다. 텍스트로 삭제 action과 결과를 명확히 전달해야 한다.

---

# 5. Dropdown Component

## 5.1 Dropdown Component Rules

### [개념]

Dropdown Component는 trigger를 통해 숨겨진 option, action, panel, menu를 열고 닫는 UI다.

Dropdown은 목적에 따라 Disclosure, Menu, Listbox, Combobox 패턴을 구분해야 한다.

---

### [핵심]

Dropdown 기준:

- trigger는 `button`
- `aria-expanded` 동기화
- `aria-controls` 고려
- `aria-haspopup` 목적에 따라 사용
- Escape 닫기
- 닫은 후 trigger focus return
- hidden item focus 방지
- item 역할 구분
- action item은 button
- navigation item은 Link

패턴 구분:

- Disclosure: 단순 panel 펼침
- Menu: action 목록
- Listbox: 선택 option 목록
- Combobox: 입력 + 선택 조합

---

### [실무]

Disclosure Dropdown:

```jsx
<button
  type="button"
  aria-expanded={open}
  aria-controls="filter-panel"
  onClick={toggleOpen}
>
  필터
</button>

<div id="filter-panel" hidden={!open}>
  필터 옵션
</div>
```

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

실무 기준:

- 단순 열림 / 닫힘은 Disclosure pattern 우선 검토
- 액션 목록은 Menu pattern 검토
- 선택 UI는 native Select 우선 검토
- trigger open 상태와 `aria-expanded` 동기화
- 닫힌 상태의 item이 focus되지 않게 함
- item이 action이면 button, 이동이면 Link
- keyboard pattern 구현 난도가 높으면 library 검토

---

### [FAQ]

Q. Dropdown에는 무조건 role="menu"를 써야 해?
A. 아니다. 단순 펼침이면 disclosure pattern이 적합할 수 있고 선택 UI면 native select나 listbox를 검토한다.

Q. Dropdown trigger는 div로 만들어도 돼?
A. 권장하지 않는다. trigger는 button을 사용하는 것이 keyboard와 semantic 측면에서 안전하다.

Q. Dropdown item은 Button이야 Link야?
A. action이면 Button, 페이지 이동이면 Link가 적합하다.

Q. Dropdown 닫힌 상태의 item에 focus가 가면 문제야?
A. 문제다. 보이지 않는 item에 keyboard focus가 가면 사용자가 혼란을 겪는다.

---

## 5.2 Menu Component

### [개념]

Menu Component는 여러 action item을 묶어 제공하는 Dropdown 유형이다.

Menu는 단순 시각적 목록이 아니라 keyboard interaction과 focus 관리가 필요한 복합 widget이다.

---

### [핵심]

Menu 기준:

- trigger button
- `aria-haspopup="menu"`
- `aria-expanded`
- `role="menu"`
- `role="menuitem"`
- Escape 닫기
- Arrow Key navigation 고려
- item 선택 후 닫기
- focus return
- hidden item focus 방지

---

### [실무]

Menu 구조:

```jsx
<button
  type="button"
  aria-haspopup="menu"
  aria-expanded={open}
  aria-controls="post-menu"
>
  게시글 메뉴
</button>;

{
  open && (
    <ul id="post-menu" role="menu">
      <li role="none">
        <button type="button" role="menuitem" onClick={onEdit}>
          수정
        </button>
      </li>
      <li role="none">
        <button type="button" role="menuitem" onClick={onDelete}>
          삭제
        </button>
      </li>
    </ul>
  );
}
```

Keyboard Flow:

```text
Trigger Enter / Space
→ Menu Open
→ Focus First Item or Keep Trigger
→ Arrow Key Item Navigation
→ Enter / Space Execute
→ Escape Close
→ Focus Return Trigger
```

실무 기준:

- menu item action은 button 사용
- menu item navigation은 Link 사용 가능하나 role 패턴 검토
- `role="menu"` 사용 시 keyboard pattern 구현 필요
- 단순 목록이면 menu role 없이 disclosure panel로 충분할 수 있음
- `li`에 `role="none"` 적용을 고려
- Menu는 복잡하므로 검증된 library 검토 가능

---

### [FAQ]

Q. Menu Component는 단순 ul/li와 달라?
A. 그렇다. role="menu"를 쓰면 keyboard pattern과 focus 관리가 필요하다.

Q. role="menuitem"만 붙이면 끝이야?
A. 아니다. Arrow Key, Escape, focus 흐름을 함께 구현해야 한다.

Q. 단순 더보기 panel에도 menu role이 필요해?
A. 꼭 그렇지 않다. 단순 정보 panel이면 disclosure가 더 적합할 수 있다.

Q. menu item 안에 button을 써도 돼?
A. action item이면 button을 사용하는 것이 적합하다.

---

# 6. Accordion Component

## 6.1 Accordion Component Rules

### [개념]

Accordion Component는 제목을 눌러 관련 panel을 펼치거나 접는 UI다.

Accordion은 trigger button과 panel의 open state를 명확히 연결해야 한다.

---

### [핵심]

Accordion 기준:

- heading 구조
- trigger는 `button`
- `aria-expanded`
- `aria-controls`
- panel id
- hidden state
- keyboard Enter / Space
- focus visible
- multiple open 정책
- one open 정책

사용 대상:

- FAQ
- 상세 정보 접기 / 펼치기
- 필터 그룹
- 설정 그룹
- 모바일 메뉴
- 추가 설명

---

### [실무]

Accordion Item:

```jsx
<h3>
  <button
    type="button"
    aria-expanded={open}
    aria-controls="faq-panel-1"
    onClick={toggleOpen}
  >
    환불 정책
  </button>
</h3>

<div id="faq-panel-1" hidden={!open}>
  환불 정책 설명입니다.
</div>
```

Multiple Accordion:

```text
Accordion Group
→ Item Heading
→ Button Trigger
→ Panel
→ aria-expanded state
→ hidden state
```

실무 기준:

- Accordion title은 heading 안의 button으로 구성 가능
- `aria-expanded`는 실제 open 상태와 일치
- `aria-controls`는 panel id와 연결
- panel이 닫힌 상태에서 내부 focus 방지
- Enter / Space로 trigger 동작
- heading level은 페이지 구조에 맞춤
- FAQ는 Accordion + 실제 FAQ text 구조 검토

---

### [FAQ]

Q. Accordion trigger는 button이어야 해?
A. 권장한다. 펼침 / 접힘은 현재 화면 상태를 바꾸는 action이므로 button이 적합하다.

Q. Accordion에는 aria-expanded가 필요해?
A. 필요하다. trigger의 open 상태를 보조기술에 전달해야 한다.

Q. Accordion title은 heading이어야 해?
A. 페이지 구조상 section 제목이면 heading 안에 button을 두는 방식을 사용할 수 있다.

Q. 닫힌 Accordion panel 안의 link에 focus가 가면 문제야?
A. 문제다. 보이지 않는 panel 내부 요소에 focus가 가지 않게 해야 한다.

---

# 7. Tab Component

## 7.1 Tab Component Rules

### [개념]

Tab Component는 같은 페이지 안에서 여러 panel을 전환하는 UI다.

Tab은 페이지 이동용 Navigation과 다르며, 동일한 맥락의 콘텐츠 패널 전환에 사용한다.

---

### [핵심]

Tab 기준:

- `role="tablist"`
- `role="tab"`
- `role="tabpanel"`
- `aria-selected`
- `aria-controls`
- `aria-labelledby`
- roving tabindex
- Arrow Key navigation
- selected panel
- hidden panel focus 방지

사용 대상:

- 상세 정보 / 리뷰
- 설정 카테고리
- 통계 panel
- 프로필 정보 구분
- 같은 페이지 내 콘텐츠 전환

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

- Tab과 panel은 id로 연결
- selected tab과 visible panel이 일치
- hidden panel 내부 focus 방지
- Arrow Key 이동 고려
- focus와 selected 상태 구분
- route 이동이면 Tab이 아니라 Link / Navigation 검토
- 구현 난도가 높으면 library 검토

---

### [FAQ]

Q. Tab과 Navigation은 뭐가 달라?
A. Tab은 같은 페이지 내부 panel 전환이고 Navigation은 page 또는 route 이동이다.

Q. Tab에는 aria-selected가 필요해?
A. 필요하다. 현재 선택된 tab을 보조기술에 전달해야 한다.

Q. Tab Panel은 어떻게 연결해?
A. tab의 aria-controls와 panel id를 연결하고 panel의 aria-labelledby로 tab id를 참조한다.

Q. hidden panel에 focus가 가면 문제야?
A. 문제다. 보이지 않는 panel 내부 요소는 focus되지 않아야 한다.

---

# 8. Tooltip Component

## 8.1 Tooltip Component Rules

### [개념]

Tooltip Component는 사용자가 특정 요소에 focus하거나 hover했을 때 짧은 보조 설명을 제공하는 UI다.

Tooltip은 중요한 정보나 필수 안내를 제공하는 유일한 수단이 되어서는 안 된다.

---

### [핵심]

Tooltip 기준:

- hover와 focus 모두 지원
- keyboard 사용자가 접근 가능
- 중요한 정보는 tooltip에만 두지 않음
- tooltip 내용은 짧게 작성
- dismiss 또는 blur 처리
- `aria-describedby` 고려
- interactive content tooltip 주의
- mobile / touch 대응 검토

사용 대상:

- 짧은 보조 설명
- 아이콘 설명
- 입력 도움말 보완
- 상태 보조 설명

---

### [실무]

Tooltip 연결:

```jsx
<button
  type="button"
  aria-describedby="save-tooltip"
>
  저장
</button>

<div id="save-tooltip" role="tooltip">
  변경 내용을 저장합니다.
</div>
```

Icon Help:

```jsx
<button
  type="button"
  aria-label="비밀번호 조건 도움말"
  aria-describedby="password-help-tooltip"
>
  <HelpIcon aria-hidden="true" />
</button>

<div id="password-help-tooltip" role="tooltip">
  영문, 숫자, 특수문자를 포함해 8자 이상 입력해 주세요.
</div>
```

실무 기준:

- hover만으로 표시되는 Tooltip 지양
- focus 시에도 표시되어야 함
- 필수 정보는 항상 보이는 helper text가 더 적합
- tooltip은 짧은 설명에 사용
- tooltip 안에 button / link 같은 interactive element를 넣는 패턴은 복잡하므로 주의
- mobile 환경에서 tooltip 접근성 검토
- tooltip이 focus를 가리지 않게 배치

---

### [FAQ]

Q. Tooltip은 hover만 지원하면 돼?
A. 아니다. keyboard 사용자를 위해 focus 시에도 접근 가능해야 한다.

Q. 중요한 정보를 Tooltip에만 넣어도 돼?
A. 권장하지 않는다. 필수 정보는 화면에 항상 보이거나 helper text로 제공하는 것이 좋다.

Q. Tooltip에는 aria-describedby를 써?
A. tooltip이 특정 요소의 설명이면 aria-describedby로 연결할 수 있다.

Q. Tooltip 안에 버튼을 넣어도 돼?
A. 가능은 하지만 focus 관리가 복잡해지므로 popover/dialog 패턴이 더 적합할 수 있다.

---

# 9. Toast Component

## 9.1 Toast Component Rules

### [개념]

Toast Component는 작업 결과나 상태 변화를 짧게 알려주는 알림 UI다.

Toast는 화면에 잠깐 나타나기 때문에 보조기술 전달, 표시 시간, 닫기 제어, action 접근성을 검토해야 한다.

---

### [핵심]

Toast 유형:

- success toast
- error toast
- warning toast
- info toast
- undo toast
- upload toast
- network toast

Toast 기준:

- message text
- `role="status"` 또는 `role="alert"`
- auto dismiss 시간 검토
- close button 선택
- action button keyboard 접근
- 중복 toast 관리
- focus를 불필요하게 빼앗지 않음
- color only 상태 금지

---

### [실무]

Success Toast:

```jsx
<div role="status" aria-live="polite">
  저장되었습니다.
</div>
```

Error Toast:

```jsx
<div role="alert">저장에 실패했습니다. 다시 시도해 주세요.</div>
```

Undo Toast:

```jsx
<div role="status" aria-live="polite">
  리뷰가 삭제되었습니다.
  <button type="button" onClick={onUndo}>
    실행 취소
  </button>
</div>
```

실무 기준:

- 성공 / 정보는 `role="status"` 고려
- 오류 / 경고는 `role="alert"` 고려
- toast message는 짧고 명확하게 작성
- action이 있으면 keyboard 접근 가능
- toast가 너무 빨리 사라지지 않게 함
- focus를 toast로 강제로 이동하지 않는 경우가 많음
- 여러 toast 동시 표시 제한 검토

---

### [FAQ]

Q. Toast에도 role이 필요해?
A. 중요한 상태를 전달한다면 role status 또는 role alert를 고려해야 한다.

Q. Toast는 focus를 가져가야 해?
A. 일반적으로 focus를 빼앗지 않는 것이 좋지만 action이 중요한 경우 별도 UX를 검토한다.

Q. Toast가 자동으로 사라져도 돼?
A. 가능하지만 중요한 메시지는 충분한 표시 시간이나 닫기 제어를 고려해야 한다.

Q. Toast 안 실행 취소 버튼은 keyboard로 접근 가능해야 해?
A. 그렇다. action이 있으면 keyboard로 조작 가능해야 한다.

---

# 10. Pagination Component

## 10.1 Pagination Rules

### [개념]

Pagination Component는 여러 페이지로 나뉜 콘텐츠 사이를 이동하는 navigation component다.

Pagination은 navigation landmark로 제공하고 현재 페이지를 명확히 표시해야 한다.

---

### [핵심]

Pagination 기준:

- `nav`
- `aria-label`
- page link
- current page `aria-current="page"`
- previous / next link
- disabled previous / next 처리
- meaningful link name
- focus visible
- keyboard navigation
- page size select label

---

### [실무]

Pagination 예:

```jsx
<nav aria-label="페이지네이션">
  <ul>
    <li>
      <Link to="?page=1">1페이지</Link>
    </li>
    <li>
      <Link to="?page=2" aria-current="page">
        2페이지
      </Link>
    </li>
    <li>
      <Link to="?page=3">3페이지</Link>
    </li>
  </ul>
</nav>
```

Previous / Next:

```jsx
<nav aria-label="페이지네이션">
  <Link to="?page=1">이전 페이지</Link>
  <Link to="?page=3">다음 페이지</Link>
</nav>
```

disabled next:

```jsx
<span aria-disabled="true">다음 페이지</span>
```

실무 기준:

- Pagination은 `nav`와 `aria-label`로 영역 설명
- 현재 페이지는 `aria-current="page"`
- 숫자만 있는 link는 “2페이지”처럼 목적을 명확히 제공
- 이전 / 다음은 이동이므로 Link
- 더 이상 이동할 수 없는 이전 / 다음 처리 명확화
- 페이지 변경 후 focus 위치 검토
- infinite scroll과 pagination 혼합 시 상태 전달 검토

---

### [FAQ]

Q. Pagination은 nav로 감싸야 해?
A. 페이지 이동 navigation이므로 nav와 aria-label을 사용하는 것이 좋다.

Q. 현재 페이지는 어떻게 표시해?
A. 현재 page link에 aria-current="page"를 사용할 수 있다.

Q. 숫자만 있는 페이지 링크는 괜찮아?
A. 가능하지만 “2페이지”처럼 accessible name을 명확히 하는 것이 좋다.

Q. 이전 / 다음은 Button이야 Link야?
A. 페이지 이동이라면 Link가 적합하다.

---

# 11. Breadcrumb Component

## 11.1 Breadcrumb Rules

### [개념]

Breadcrumb Component는 현재 페이지의 계층적 위치를 보여주는 navigation component다.

Breadcrumb는 사용자가 현재 위치를 이해하고 상위 페이지로 이동할 수 있게 한다.

---

### [핵심]

Breadcrumb 기준:

- `nav`
- `aria-label="Breadcrumb"` 또는 한글 label
- ordered list `ol`
- page hierarchy
- current page `aria-current="page"`
- separator decoration
- meaningful link text

---

### [실무]

Breadcrumb 예:

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

Separator 처리:

```jsx
<span aria-hidden="true">/</span>
```

실무 기준:

- Breadcrumb는 navigation landmark
- 계층 순서가 있으므로 `ol` 사용
- 현재 페이지는 link가 아닐 수 있음
- 현재 항목에는 `aria-current="page"`
- separator는 장식이면 `aria-hidden`
- Breadcrumb가 너무 길면 현재 위치 이해를 해치지 않게 축약 검토

---

### [FAQ]

Q. Breadcrumb도 nav야?
A. 그렇다. 현재 페이지 위치를 탐색하는 링크 묶음이므로 nav로 감싸는 것이 좋다.

Q. Breadcrumb에는 ul과 ol 중 뭐가 좋아?
A. 계층 순서가 있으므로 ol이 적합하다.

Q. 마지막 현재 페이지도 link로 만들어야 해?
A. 필수는 아니다. 현재 위치를 나타내고 aria-current="page"를 사용할 수 있다.

Q. 구분자 / 는 스크린 리더가 읽어야 해?
A. 보통 장식으로 보고 aria-hidden 처리할 수 있다.

---

# 12. Card Component

## 12.1 Card Accessibility Rules

### [개념]

Card Component는 이미지, 제목, 설명, action을 묶어 하나의 콘텐츠 단위로 보여주는 UI다.

Card는 독립 콘텐츠라면 `article`을 사용할 수 있고, 반복 목록이라면 `ul/li` 구조와 함께 사용할 수 있다.

---

### [핵심]

Card 기준:

- `article` 고려
- list item 구조
- heading 제공
- meaningful link
- image alt 판단
- card action 구분
- 전체 카드 클릭 주의
- duplicate link focus 주의
- icon button name
- hover only action 금지

Card 사용 대상:

- 축제 카드
- 리뷰 카드
- 게시글 카드
- 상품 카드
- 알림 카드
- 결제 내역 카드
- 사용자 카드

---

### [실무]

Card List:

```jsx
<ul>
  {festivals.map((festival) => (
    <li key={festival.id}>
      <article>
        <img src={festival.imageUrl} alt="" />
        <h3>{festival.title}</h3>
        <p>{festival.regionName}</p>
        <Link to={`/festivals/${festival.id}`}>{festival.title} 상세 보기</Link>
      </article>
    </li>
  ))}
</ul>
```

Card with Action:

```jsx
<article>
  <h3>{review.title}</h3>
  <p>{review.content}</p>

  <button type="button" onClick={onLike}>
    좋아요
  </button>

  <Link to={`/reviews/${review.id}`}>{review.title} 상세 보기</Link>
</article>
```

실무 기준:

- 카드가 독립 콘텐츠면 `article` 검토
- 카드 목록은 `ul/li` 검토
- 카드 제목은 heading level 통일
- 이미지가 제목과 중복이면 empty alt 검토
- 링크 텍스트는 목적지 명확화
- 전체 카드 클릭 구현은 중복 링크와 focus 순서 주의
- hover 시에만 action이 나타나면 keyboard 사용자 접근성 검토
- 카드 내부 icon button에는 accessible name 제공

---

### [FAQ]

Q. Card는 div로만 만들어도 돼?
A. 단순 wrapper라면 가능하지만 독립 콘텐츠 단위라면 article과 heading을 고려할 수 있다.

Q. 카드 목록은 ul/li로 감싸야 해?
A. 반복되는 콘텐츠 목록이라면 ul/li 구조가 의미상 좋다.

Q. 카드 전체 클릭은 접근성에 문제야?
A. 구현 방식에 따라 중복 focus, 불명확한 link name, keyboard 조작 문제가 생길 수 있다.

Q. 카드 이미지 alt는 어떻게 정해?
A. 이미지가 정보를 전달하면 의미 있는 alt를 제공하고 제목과 중복되는 장식이면 alt=""를 검토한다.

---

# 13. Component Testing

## 13.1 Component Accessibility Test

### [개념]

Component Accessibility Test는 공통 Component가 role, accessible name, keyboard, focus, ARIA state 기준을 만족하는지 검증하는 테스트다.

공통 Component 테스트는 여러 화면의 접근성 품질을 안정적으로 유지하는 데 중요하다.

---

### [핵심]

테스트 대상:

- Button role/name
- IconButton accessible name
- Link role/name
- Modal role/name/focus
- Dropdown expanded state
- Accordion expanded state
- Tab selected state
- Toast status / alert
- Pagination current page
- Breadcrumb navigation
- Card link text
- Keyboard interaction

---

### [실무]

Button Test:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
```

IconButton Test:

```tsx
expect(screen.getByRole("button", { name: "닫기" })).toBeInTheDocument();
```

Modal Test:

```tsx
expect(screen.getByRole("dialog", { name: "리뷰 작성" })).toBeInTheDocument();
```

Dropdown State Test:

```tsx
expect(screen.getByRole("button", { name: "필터" })).toHaveAttribute(
  "aria-expanded",
  "true",
);
```

Tab Test:

```tsx
expect(screen.getByRole("tab", { name: "리뷰" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

Keyboard Test:

```tsx
await user.keyboard("{Escape}");
expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

실무 기준:

- `getByRole` 우선 사용
- Form Control은 `getByLabelText` 사용
- ARIA state는 실제 state와 함께 검증
- keyboard interaction은 userEvent 사용
- `getByTestId`는 최후 수단
- Modal / Dropdown / Tab은 수동 keyboard check도 필요

---

### [FAQ]

Q. 공통 Component는 무엇을 테스트해야 해?
A. role, accessible name, keyboard interaction, focus, ARIA state를 우선 테스트한다.

Q. IconButton은 어떻게 테스트해?
A. getByRole("button", { name })으로 accessible name을 검증한다.

Q. Dropdown은 무엇을 테스트해?
A. trigger button, aria-expanded 동기화, open/close, keyboard 조작을 확인한다.

Q. Component 테스트에 testId를 써도 돼?
A. 필요한 경우 가능하지만 접근성 구조 검증을 위해 role/name query를 우선 사용한다.

---

## 13.2 Component Manual Check

### [개념]

Component Manual Check는 공통 Component를 실제 keyboard, screen reader 기본 흐름, visual state 기준으로 직접 확인하는 절차다.

자동화 테스트가 있어도 focus visible, keyboard trap, visual clipping, motion, text 품질은 수동 검토가 필요하다.

---

### [핵심]

수동 점검 항목:

- keyboard only 조작
- focus visible
- focus order
- Escape close
- focus return
- hidden item focus
- ARIA state와 시각 상태 일치
- color only meaning
- loading / error 상태
- zoom / responsive
- dark mode
- reduced motion

---

### [실무]

Manual Check Flow:

```text
Component 렌더링
→ Tab 접근 확인
→ Focus Visible 확인
→ Enter / Space 실행
→ Arrow / Escape 필요 여부 확인
→ Open / Close 상태 확인
→ Focus Return 확인
→ Screen Reader Name 추정
→ Visual State 확인
```

우선 점검 Component:

- Button
- IconButton
- Modal
- Dropdown
- Accordion
- Tab
- Toast
- Pagination
- Form Control
- Search Box
- Card
- File Upload

실무 기준:

- Component Storybook 또는 demo page에서 점검 가능
- keyboard only로 핵심 조작 수행
- focus ring이 잘리는지 확인
- open/close component는 focus return 확인
- state message가 문구로 전달되는지 확인
- 반복 사용 전 공통 Component 단계에서 수정

---

### [FAQ]

Q. Component 수동 점검은 왜 필요해?
A. 자동화가 focus 시각 품질, keyboard trap, 문구 품질, 실제 조작 흐름을 완전히 검증하지 못하기 때문이다.

Q. 수동 점검은 어떤 Component부터 해?
A. Button, Modal, Dropdown, Form Control처럼 재사용성이 높고 영향이 큰 Component부터 확인한다.

Q. Storybook에서 접근성 점검해도 돼?
A. 가능하다. 공통 Component 상태별로 keyboard와 visual state를 확인하기 좋다.

Q. 자동화 테스트가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 둘은 보완 관계다.

---

# 14. Component Accessibility Review

## 14.1 Review Checklist

### [개념]

Component Accessibility Review는 공통 UI Component가 semantic, keyboard, focus, ARIA, state, testing 기준을 만족하는지 검토하는 과정이다.

Review Agent는 Component 단위로 접근성 문제를 잡아 반복 오류를 줄여야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Component 목적이 action인지 navigation인지 명확한가?
- [ ] Native HTML을 우선 사용했는가?
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
- [ ] Component의 focus visible이 명확한가?
- [ ] Component 상태가 색상만으로 전달되지 않는가?
- [ ] Testing Library role/name query로 검증 가능한가?
```

---

### [실무]

Review Flow:

```text
Component 역할 확인
→ Native HTML 확인
→ Accessible Name 확인
→ Keyboard 조작 확인
→ Focus Visible 확인
→ ARIA State 확인
→ Open / Close Focus 확인
→ State Feedback 확인
→ Testing Query 확인
→ Anti Pattern 확인
```

대표 수정 패턴:

```text
문제: IconButton aria-label 없음
해결: button에 aria-label 제공 + icon aria-hidden
```

```text
문제: Modal close 후 focus lost
해결: trigger ref로 focus return
```

```text
문제: Dropdown closed item focus 가능
해결: 닫힌 상태에서는 unmount 또는 hidden/focus 제외
```

```text
문제: Tab selected와 panel 표시 불일치
해결: aria-selected, hidden, selectedTab state 동기화
```

---

### [FAQ]

Q. Component Review에서 가장 먼저 볼 것은?
A. Component의 목적이 action인지 navigation인지 확인하고 Native HTML을 우선 사용했는지 본다.

Q. 공통 Component에서 접근성 문제를 잡는 이유는?
A. 공통 Component는 여러 화면에서 반복 사용되므로 한 번 수정하면 전체 품질이 개선된다.

Q. Component Review에서 ARIA만 보면 돼?
A. 아니다. semantic HTML, keyboard, focus, state, testing까지 함께 봐야 한다.

Q. Review Agent는 Component 테스트 가능성도 봐야 해?
A. 봐야 한다. getByRole, getByLabelText로 찾을 수 있는 구조인지 확인해야 한다.

---

# 15. Common Component Accessibility Mistakes

## 15.1 Component Anti Patterns

### [개념]

Component Anti Pattern은 공통 UI Component가 시각적으로는 동작하지만 semantic, keyboard, focus, ARIA, state 기준을 만족하지 못하는 구현 방식이다.

공통 Component의 Anti Pattern은 프로젝트 전체 접근성 문제로 확산된다.

---

### [핵심]

자주 발생하는 실수:

- Button 기본 type 누락
- Button을 Link처럼 사용
- Link를 Button action처럼 사용
- IconButton accessible name 누락
- icon에만 aria-label 제공
- Modal role 없음
- Modal title 연결 없음
- Modal open focus 이동 없음
- Modal close focus return 없음
- Escape 닫기 없음
- Dropdown trigger를 div로 구현
- Dropdown aria-expanded 불일치
- 닫힌 Dropdown item focus 가능
- Menu role 사용 후 keyboard 미구현
- Accordion trigger를 div로 구현
- Accordion panel hidden 처리 누락
- Tab aria-selected 불일치
- hidden tabpanel focus 가능
- Tooltip hover only
- Toast text 없이 icon만 표시
- Pagination 현재 페이지 aria-current 누락
- Breadcrumb separator를 읽게 둠
- Card 전체 클릭 구현으로 focus 중복
- Component testId 중심 테스트

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

```jsx
<button type="button">
  <CloseIcon />
</button>
```

개선:

```jsx
<button type="button" aria-label="닫기">
  <CloseIcon aria-hidden="true" />
</button>
```

Anti Pattern:

```jsx
<section className="modal">
  <h2>리뷰 작성</h2>
</section>
```

개선:

```jsx
<section role="dialog" aria-modal="true" aria-labelledby="review-dialog-title">
  <h2 id="review-dialog-title">리뷰 작성</h2>
</section>
```

Anti Pattern:

```jsx
<button aria-expanded="true">필터</button>
```

개선:

```jsx
<button type="button" aria-expanded={open} aria-controls="filter-panel">
  필터
</button>
```

---

### [FAQ]

Q. Component 접근성 초보가 가장 많이 하는 실수는?
A. IconButton 이름 누락, Modal focus 관리 누락, Dropdown keyboard 누락, Button/Link 역할 혼동이 많다.

Q. 공통 Button type 누락은 왜 문제야?
A. Form 내부에서 의도하지 않은 submit이 발생할 수 있다.

Q. Modal이 화면에 잘 보이면 접근성도 괜찮아?
A. 아니다. role, title 연결, focus 이동, focus trap, focus return을 함께 확인해야 한다.

Q. Dropdown이 클릭으로 열리면 충분해?
A. 아니다. keyboard 조작, aria-expanded 동기화, hidden item focus 방지를 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Component Accessibility는 왜 중요해?
A. 공통 Component 하나의 접근성 문제가 여러 화면에 반복되기 때문에 설계 단계에서 기준을 잡아야 한다.

Q. 공통 Component는 디자인만 맞으면 돼?
A. 아니다. semantic role, keyboard, focus, accessible name, ARIA state까지 포함해야 한다.

Q. Component 접근성은 어디서 먼저 잡아야 해?
A. Button, Link, Form Control, Modal, Dropdown처럼 자주 재사용되는 Component부터 잡는 것이 좋다.

Q. 공통 Component 테스트는 어떻게 해?
A. Testing Library의 getByRole, getByLabelText, userEvent keyboard test로 핵심 동작을 검증한다.

Q. Button Component 기준은?
A. native button, 기본 type button, accessible name, keyboard Enter/Space, focus visible, disabled/loading 상태를 제공해야 한다.

Q. 공통 Button의 기본 type은 뭐가 좋아?
A. 의도하지 않은 Form submit을 막기 위해 type="button"을 기본값으로 두는 것이 좋다.

Q. Button loading 상태는 어떻게 처리해?
A. 버튼 텍스트를 “저장 중...”처럼 바꾸고 disabled 또는 aria-busy를 고려한다.

Q. Button과 Link는 어떻게 구분해?
A. Button은 action 실행이고 Link는 페이지나 위치 이동이다.

Q. disabled Button에는 이유를 꼭 써야 해?
A. 사용자가 왜 사용할 수 없는지 알기 어렵다면 helper text나 안내 문구를 제공하는 것이 좋다.

Q. IconButton에는 왜 aria-label이 필요해?
A. 시각적 텍스트가 없으면 스크린 리더가 버튼의 목적을 알 수 없기 때문이다.

Q. IconButton aria-label은 icon에 붙여?
A. 아니다. 조작 대상인 button에 붙이는 것이 적합하다.

Q. 좋아요 같은 toggle IconButton은 어떻게 표현해?
A. 상태에 따라 label을 바꾸거나 aria-pressed를 사용해 눌림 상태를 전달할 수 있다.

Q. 같은 삭제 아이콘이 여러 개 있으면?
A. “리뷰 삭제”, “댓글 삭제”처럼 대상이 드러나도록 accessible name을 구체화한다.

Q. Link Component는 언제 써?
A. 페이지, route, URL, 문서 위치로 이동할 때 사용한다.

Q. 삭제를 Link로 만들어도 돼?
A. 권장하지 않는다. 삭제는 현재 상태를 변경하는 action이므로 Button이 적합하다.

Q. 자세히 보기 링크를 반복해도 돼?
A. 가능하지만 목적지가 모호할 수 있으므로 대상 이름을 포함하는 것이 좋다.

Q. 현재 페이지 메뉴는 어떻게 표시해?
A. 시각적 active 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. Modal에는 어떤 접근성 처리가 필요해?
A. role dialog, aria-modal, title 연결, focus 이동, focus trap, focus return, 닫기 버튼이 필요하다.

Q. Modal open 시 focus는 어디로 가야 해?
A. Modal title, 첫 입력 필드, 첫 버튼 등 Modal 내부의 적절한 위치로 이동해야 한다.

Q. Modal close 후 focus는 어디로 가야 해?
A. 일반적으로 Modal을 열었던 trigger 요소로 돌아간다.

Q. aria-modal만 붙이면 Modal 접근성이 끝이야?
A. 아니다. focus management와 keyboard interaction이 함께 필요하다.

Q. Confirm Dialog는 언제 alertdialog를 써?
A. 삭제나 결제처럼 중요한 결정을 즉시 인식해야 하는 경우 고려할 수 있다.

Q. Confirm Dialog 확인 버튼 문구는 확인이면 돼?
A. 가능하지만 “삭제”, “결제하기”처럼 실제 action을 명확히 쓰는 것이 좋다.

Q. Confirm Dialog에 취소 버튼은 꼭 필요해?
A. 사용자가 action을 중단할 수 있도록 제공하는 것이 좋다.

Q. 삭제 Dialog에서 색상만 빨갛게 하면 충분해?
A. 아니다. 텍스트로 삭제 action과 결과를 명확히 전달해야 한다.

Q. Dropdown에는 무조건 role="menu"를 써야 해?
A. 아니다. 단순 펼침이면 disclosure pattern이 적합할 수 있고 선택 UI면 native select나 listbox를 검토한다.

Q. Dropdown trigger는 div로 만들어도 돼?
A. 권장하지 않는다. trigger는 button을 사용하는 것이 keyboard와 semantic 측면에서 안전하다.

Q. Dropdown item은 Button이야 Link야?
A. action이면 Button, 페이지 이동이면 Link가 적합하다.

Q. Dropdown 닫힌 상태의 item에 focus가 가면 문제야?
A. 문제다. 보이지 않는 item에 keyboard focus가 가면 사용자가 혼란을 겪는다.

Q. Menu Component는 단순 ul/li와 달라?
A. 그렇다. role="menu"를 쓰면 keyboard pattern과 focus 관리가 필요하다.

Q. role="menuitem"만 붙이면 끝이야?
A. 아니다. Arrow Key, Escape, focus 흐름을 함께 구현해야 한다.

Q. 단순 더보기 panel에도 menu role이 필요해?
A. 꼭 그렇지 않다. 단순 정보 panel이면 disclosure가 더 적합할 수 있다.

Q. menu item 안에 button을 써도 돼?
A. action item이면 button을 사용하는 것이 적합하다.

Q. Accordion trigger는 button이어야 해?
A. 권장한다. 펼침 / 접힘은 현재 화면 상태를 바꾸는 action이므로 button이 적합하다.

Q. Accordion에는 aria-expanded가 필요해?
A. 필요하다. trigger의 open 상태를 보조기술에 전달해야 한다.

Q. Accordion title은 heading이어야 해?
A. 페이지 구조상 section 제목이면 heading 안에 button을 두는 방식을 사용할 수 있다.

Q. 닫힌 Accordion panel 안의 link에 focus가 가면 문제야?
A. 문제다. 보이지 않는 panel 내부 요소에 focus가 가지 않게 해야 한다.

Q. Tab과 Navigation은 뭐가 달라?
A. Tab은 같은 페이지 내부 panel 전환이고 Navigation은 page 또는 route 이동이다.

Q. Tab에는 aria-selected가 필요해?
A. 필요하다. 현재 선택된 tab을 보조기술에 전달해야 한다.

Q. Tab Panel은 어떻게 연결해?
A. tab의 aria-controls와 panel id를 연결하고 panel의 aria-labelledby로 tab id를 참조한다.

Q. hidden panel에 focus가 가면 문제야?
A. 문제다. 보이지 않는 panel 내부 요소는 focus되지 않아야 한다.

Q. Tooltip은 hover만 지원하면 돼?
A. 아니다. keyboard 사용자를 위해 focus 시에도 접근 가능해야 한다.

Q. 중요한 정보를 Tooltip에만 넣어도 돼?
A. 권장하지 않는다. 필수 정보는 화면에 항상 보이거나 helper text로 제공하는 것이 좋다.

Q. Tooltip에는 aria-describedby를 써?
A. tooltip이 특정 요소의 설명이면 aria-describedby로 연결할 수 있다.

Q. Tooltip 안에 버튼을 넣어도 돼?
A. 가능은 하지만 focus 관리가 복잡해지므로 popover/dialog 패턴이 더 적합할 수 있다.

Q. Toast에도 role이 필요해?
A. 중요한 상태를 전달한다면 role status 또는 role alert를 고려해야 한다.

Q. Toast는 focus를 가져가야 해?
A. 일반적으로 focus를 빼앗지 않는 것이 좋지만 action이 중요한 경우 별도 UX를 검토한다.

Q. Toast가 자동으로 사라져도 돼?
A. 가능하지만 중요한 메시지는 충분한 표시 시간이나 닫기 제어를 고려해야 한다.

Q. Toast 안 실행 취소 버튼은 keyboard로 접근 가능해야 해?
A. 그렇다. action이 있으면 keyboard로 조작 가능해야 한다.

Q. Pagination은 nav로 감싸야 해?
A. 페이지 이동 navigation이므로 nav와 aria-label을 사용하는 것이 좋다.

Q. Pagination 현재 페이지는 어떻게 표시해?
A. 현재 page link에 aria-current="page"를 사용할 수 있다.

Q. 숫자만 있는 페이지 링크는 괜찮아?
A. 가능하지만 “2페이지”처럼 accessible name을 명확히 하는 것이 좋다.

Q. Pagination 이전 / 다음은 Button이야 Link야?
A. 페이지 이동이라면 Link가 적합하다.

Q. Breadcrumb도 nav야?
A. 그렇다. 현재 페이지 위치를 탐색하는 링크 묶음이므로 nav로 감싸는 것이 좋다.

Q. Breadcrumb에는 ul과 ol 중 뭐가 좋아?
A. 계층 순서가 있으므로 ol이 적합하다.

Q. Breadcrumb 마지막 현재 페이지도 link로 만들어야 해?
A. 필수는 아니다. 현재 위치를 나타내고 aria-current="page"를 사용할 수 있다.

Q. Breadcrumb 구분자 / 는 스크린 리더가 읽어야 해?
A. 보통 장식으로 보고 aria-hidden 처리할 수 있다.

Q. Card는 div로만 만들어도 돼?
A. 단순 wrapper라면 가능하지만 독립 콘텐츠 단위라면 article과 heading을 고려할 수 있다.

Q. 카드 목록은 ul/li로 감싸야 해?
A. 반복되는 콘텐츠 목록이라면 ul/li 구조가 의미상 좋다.

Q. 카드 전체 클릭은 접근성에 문제야?
A. 구현 방식에 따라 중복 focus, 불명확한 link name, keyboard 조작 문제가 생길 수 있다.

Q. 카드 이미지 alt는 어떻게 정해?
A. 이미지가 정보를 전달하면 의미 있는 alt를 제공하고 제목과 중복되는 장식이면 alt=""를 검토한다.

Q. 공통 Component는 무엇을 테스트해야 해?
A. role, accessible name, keyboard interaction, focus, ARIA state를 우선 테스트한다.

Q. IconButton은 어떻게 테스트해?
A. getByRole("button", { name })으로 accessible name을 검증한다.

Q. Dropdown은 무엇을 테스트해?
A. trigger button, aria-expanded 동기화, open/close, keyboard 조작을 확인한다.

Q. Component 테스트에 testId를 써도 돼?
A. 필요한 경우 가능하지만 접근성 구조 검증을 위해 role/name query를 우선 사용한다.

Q. Component 수동 점검은 왜 필요해?
A. 자동화가 focus 시각 품질, keyboard trap, 문구 품질, 실제 조작 흐름을 완전히 검증하지 못하기 때문이다.

Q. 수동 점검은 어떤 Component부터 해?
A. Button, Modal, Dropdown, Form Control처럼 재사용성이 높고 영향이 큰 Component부터 확인한다.

Q. Storybook에서 접근성 점검해도 돼?
A. 가능하다. 공통 Component 상태별로 keyboard와 visual state를 확인하기 좋다.

Q. 자동화 테스트가 있으면 수동 점검은 생략해도 돼?
A. 아니다. 둘은 보완 관계다.

Q. Component Review에서 가장 먼저 볼 것은?
A. Component의 목적이 action인지 navigation인지 확인하고 Native HTML을 우선 사용했는지 본다.

Q. 공통 Component에서 접근성 문제를 잡는 이유는?
A. 공통 Component는 여러 화면에서 반복 사용되므로 한 번 수정하면 전체 품질이 개선된다.

Q. Component Review에서 ARIA만 보면 돼?
A. 아니다. semantic HTML, keyboard, focus, state, testing까지 함께 봐야 한다.

Q. Review Agent는 Component 테스트 가능성도 봐야 해?
A. 봐야 한다. getByRole, getByLabelText로 찾을 수 있는 구조인지 확인해야 한다.

Q. Component 접근성 초보가 가장 많이 하는 실수는?
A. IconButton 이름 누락, Modal focus 관리 누락, Dropdown keyboard 누락, Button/Link 역할 혼동이 많다.

Q. 공통 Button type 누락은 왜 문제야?
A. Form 내부에서 의도하지 않은 submit이 발생할 수 있다.

Q. Modal이 화면에 잘 보이면 접근성도 괜찮아?
A. 아니다. role, title 연결, focus 이동, focus trap, focus return을 함께 확인해야 한다.

Q. Dropdown이 클릭으로 열리면 충분해?
A. 아니다. keyboard 조작, aria-expanded 동기화, hidden item focus 방지를 확인해야 한다.
