# Frontend Testing Part06 - Component Test

---

# 1. Component Test Overview

## 1.1 Component Test Definition

### [개념]

Component Test는 React Component가 props, user event, state, conditional rendering에 따라 올바른 화면 결과를 만드는지 검증하는 테스트다.

Component Test는 내부 구현보다 사용자가 보는 UI와 조작 결과를 기준으로 작성한다.

---

### [핵심]

- Component Test
- React Component Test
- Presentational Component Test
- Interactive Component Test
- Props Rendering
- Conditional Rendering
- User Event
- Callback
- UI State
- Loading State
- Error State
- Empty State
- Accessibility Query
- React Testing Library
- userEvent

---

### [실무]

2026 실무 기준에서 Component Test는 단순히 Component가 렌더링되는지 확인하는 테스트가 아니다.

검증 흐름:

```text
Component render
→ 사용자 기준 query
→ props 기반 UI 확인
→ userEvent 실행
→ callback 또는 화면 결과 검증
→ 조건부 UI 상태 검증
```

좋은 Component Test:

```text
사용자가 볼 수 있는 텍스트 검증
사용자가 누를 수 있는 버튼 검증
사용자 입력 후 화면 결과 검증
Loading / Error / Empty 상태 검증
접근성 role / label 기반 query 사용
```

나쁜 Component Test:

```text
내부 state 직접 확인
CSS className만 확인
container.querySelector 남용
snapshot 하나로 전체 검증
구현 함수 호출 여부만 확인
```

---

### [FAQ]

Q. Component Test는 뭐야?
A. React Component가 props, 사용자 이벤트, 조건부 렌더링에 따라 올바른 UI 결과를 만드는지 검증하는 테스트다.

Q. Component Test에서 가장 중요한 기준은 뭐야?
A. 내부 구현보다 사용자가 보는 화면과 조작 결과를 검증하는 것이다.

Q. Component Test는 Unit Test와 달라?
A. 다르다. Unit Test는 순수 함수 중심이고 Component Test는 React Component의 화면과 상호작용 중심이다.

---

## 1.2 Component Test Scope

### [개념]

Component Test Scope는 단일 Component 또는 작은 UI 단위에서 검증할 범위를 정하는 기준이다.

Component Test는 화면 단위 전체 흐름보다 Component 자체의 props, event, 상태 UI를 검증하는 데 집중한다.

---

### [핵심]

포함 범위:

- props rendering
- text rendering
- image alt rendering
- button state
- callback call
- user input
- form field display
- modal open / close
- dropdown open / close
- tab change
- list rendering
- empty state
- loading state
- error state
- disabled state
- accessibility role

제외 또는 분리 권장:

- 실제 API 호출
- 전체 Router 흐름
- 실제 Backend 통합
- 실제 브라우저 E2E
- 복잡한 Auth Flow 전체
- 내부 hook 구현 직접 검증

---

### [실무]

Component Test 적합 예:

```text
FestivalCard가 축제 제목과 지역을 표시한다.
SearchBox에서 검색 버튼 클릭 시 onSearch가 호출된다.
Modal에서 닫기 버튼 클릭 시 dialog가 사라진다.
ReviewList에 리뷰가 없으면 EmptyState를 표시한다.
SubmitButton이 loading 중 disabled 된다.
```

Integration Test가 더 적합한 예:

```text
로그인 API 성공 후 Auth Store 업데이트와 Router 이동
검색 페이지에서 API 요청 후 결과 목록 표시
보호 라우트 접근 시 로그인 페이지 redirect
Mutation 성공 후 Query invalidation으로 목록 갱신
```

---

### [FAQ]

Q. Component Test는 어디까지 검증해?
A. 단일 Component의 표시, 입력, 클릭, 조건부 상태, callback, 접근성 요소를 검증한다.

Q. API 호출이 있는 Component는 Component Test로 못 해?
A. 가능하지만 실제 API는 호출하지 않고 mock으로 제어한다. 여러 Provider와 상태 흐름이 엮이면 Integration Test에 가깝다.

Q. Component 내부 hook을 직접 테스트해야 해?
A. 보통은 hook 결과가 반영된 UI를 테스트한다.

---

# 2. Presentational Component Test

## 2.1 Presentational Component Definition

### [개념]

Presentational Component는 주로 props를 받아 화면을 표시하는 Component다.

Presentational Component Test는 props 값에 따라 사용자가 보는 텍스트, 이미지, 버튼, badge, 상태 UI가 올바르게 표시되는지 검증한다.

---

### [핵심]

Presentational Component 대상:

- Card
- Badge
- Button
- Avatar
- Image
- ListItem
- StatusLabel
- EmptyState
- ErrorState
- LoadingState
- SectionTitle
- Display-only component

검증 대상:

- text
- heading
- image alt
- button name
- link name
- status label
- conditional text
- disabled state

---

### [실무]

예:

```tsx
type FestivalCardProps = {
  festival: {
    festivalId: number;
    title: string;
    regionName: string;
    imageUrl: string;
  };
};

function FestivalCard({ festival }: FestivalCardProps) {
  return (
    <article aria-label={festival.title}>
      <img src={festival.imageUrl} alt={`${festival.title} 대표 이미지`} />
      <h2>{festival.title}</h2>
      <p>{festival.regionName}</p>
      <a href={`/festivals/${festival.festivalId}`}>상세 보기</a>
    </article>
  );
}
```

테스트:

```tsx
test("축제 카드에 제목, 지역, 대표 이미지를 표시한다", () => {
  render(
    <FestivalCard
      festival={{
        festivalId: 1,
        title: "봄꽃 축제",
        regionName: "서울",
        imageUrl: "/festival.png",
      }}
    />,
  );

  expect(
    screen.getByRole("article", { name: "봄꽃 축제" }),
  ).toBeInTheDocument();
  expect(
    screen.getByRole("heading", { name: "봄꽃 축제" }),
  ).toBeInTheDocument();
  expect(screen.getByText("서울")).toBeInTheDocument();
  expect(screen.getByAltText("봄꽃 축제 대표 이미지")).toBeInTheDocument();
  expect(screen.getByRole("link", { name: "상세 보기" })).toHaveAttribute(
    "href",
    "/festivals/1",
  );
});
```

권장:

- props 기반 화면 결과 검증
- heading / link / image alt 등 semantic query 사용
- className 중심 테스트 지양
- snapshot만으로 대체하지 않음

---

### [FAQ]

Q. Presentational Component는 뭘 테스트해?
A. props에 따라 사용자가 보는 텍스트, 이미지, 버튼, 링크, 상태 표시가 올바른지 테스트한다.

Q. Card Component는 어떻게 테스트해?
A. 카드의 제목, 설명, 이미지 alt, 링크, 버튼 같은 사용자 표시 요소를 검증한다.

Q. className이 맞는지 테스트해야 해?
A. 대부분 지양한다. 사용자에게 보이는 의미와 상태를 우선 검증한다.

---

## 2.2 Props Rendering Test

### [개념]

Props Rendering Test는 Component에 전달된 props가 화면에 올바르게 표시되는지 검증하는 테스트다.

Props Rendering은 Presentational Component Test의 기본이다.

---

### [핵심]

검증 대상:

- title prop
- description prop
- label prop
- count prop
- imageUrl prop
- href prop
- disabled prop
- selected prop
- variant prop caution
- optional prop
- default prop

---

### [실무]

기본 예:

```tsx
test("버튼 label을 표시한다", () => {
  render(<Button label="저장" />);

  expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
});
```

Optional prop 예:

```tsx
test("설명이 있으면 설명을 표시한다", () => {
  render(<SectionHeader title="공지사항" description="중요한 안내입니다." />);

  expect(screen.getByRole("heading", { name: "공지사항" })).toBeInTheDocument();
  expect(screen.getByText("중요한 안내입니다.")).toBeInTheDocument();
});

test("설명이 없으면 설명 영역을 표시하지 않는다", () => {
  render(<SectionHeader title="공지사항" />);

  expect(screen.queryByText("중요한 안내입니다.")).not.toBeInTheDocument();
});
```

권장:

- 필수 props 표시 테스트
- optional props 조건부 표시 테스트
- default value 테스트
- href / alt / aria-label 같은 속성 검증
- variant prop은 사용자 결과로 검증

---

### [FAQ]

Q. Props Rendering Test는 뭐야?
A. Component에 전달한 props가 화면에 올바르게 반영되는지 검증하는 테스트다.

Q. optional prop도 테스트해야 해?
A. 조건부 UI가 달라진다면 테스트하는 것이 좋다.

Q. variant prop은 어떻게 테스트해?
A. className보다 버튼 이름, disabled 상태, visible text 같은 사용자 결과로 검증하는 것이 좋다.

---

## 2.3 Conditional Rendering Test

### [개념]

Conditional Rendering Test는 props, state, permission, data 상태에 따라 특정 UI가 표시되거나 사라지는지 검증하는 테스트다.

---

### [핵심]

조건부 렌더링 대상:

- optional text
- empty state
- loading state
- error state
- success state
- disabled state
- permission UI
- authenticated UI
- selected UI
- expanded UI
- collapsed UI

---

### [실무]

예:

```tsx
function FavoriteButton({ isFavorite }: { isFavorite: boolean }) {
  return <button>{isFavorite ? "찜 해제" : "찜하기"}</button>;
}
```

테스트:

```tsx
test("찜 상태이면 찜 해제 버튼을 표시한다", () => {
  render(<FavoriteButton isFavorite />);

  expect(screen.getByRole("button", { name: "찜 해제" })).toBeInTheDocument();
});

test("찜 상태가 아니면 찜하기 버튼을 표시한다", () => {
  render(<FavoriteButton isFavorite={false} />);

  expect(screen.getByRole("button", { name: "찜하기" })).toBeInTheDocument();
});
```

권한 UI 예:

```tsx
test("관리자 권한이 있으면 삭제 버튼을 표시한다", () => {
  render(<PostActions role="ADMIN" />);

  expect(screen.getByRole("button", { name: "삭제" })).toBeInTheDocument();
});

test("일반 사용자는 삭제 버튼을 볼 수 없다", () => {
  render(<PostActions role="USER" />);

  expect(
    screen.queryByRole("button", { name: "삭제" }),
  ).not.toBeInTheDocument();
});
```

권장:

- 표시되는 경우와 표시되지 않는 경우 모두 테스트
- absence 검증은 queryBy 사용
- 권한 UI는 role 값 기준 명확히 테스트
- 조건부 UI가 많으면 Component 분리 검토

---

### [FAQ]

Q. Conditional Rendering은 어떻게 테스트해?
A. 조건값을 다르게 전달하고 특정 UI가 표시되거나 표시되지 않는지 검증한다.

Q. 표시되지 않아야 하는 요소는 어떤 Query를 써?
A. `queryBy`를 사용한다.

Q. 권한별 버튼 표시도 Component Test 대상이야?
A. 단순 표시 여부는 Component Test 대상이다. 실제 권한 흐름 전체는 Integration Test로 검증한다.

---

# 3. Interactive Component Test

## 3.1 Interactive Component Definition

### [개념]

Interactive Component는 사용자의 클릭, 입력, 선택, hover, keyboard 조작에 따라 UI 상태나 callback이 변경되는 Component다.

Interactive Component Test는 userEvent 기반으로 작성한다.

---

### [핵심]

Interactive Component 대상:

- Button
- Input
- SearchBox
- Checkbox
- Radio
- Select
- Modal
- Dropdown
- Tabs
- Accordion
- Tooltip
- Pagination
- Toggle
- Form Field

검증 대상:

- click result
- input result
- selected result
- open / close
- callback call
- disabled state
- keyboard behavior
- visible UI change

---

### [실무]

기본 흐름:

```text
const user = userEvent.setup()
→ render Component
→ screen query
→ await user action
→ expect visible result
```

예:

```tsx
test("열기 버튼을 누르면 상세 내용을 표시한다", async () => {
  const user = userEvent.setup();

  render(<Accordion title="상세 정보">축제 상세 설명</Accordion>);

  await user.click(screen.getByRole("button", { name: "상세 정보" }));

  expect(screen.getByText("축제 상세 설명")).toBeInTheDocument();
});
```

권장:

- 실제 사용자 행동 순서로 작성
- userEvent에 await 사용
- 사용자에게 보이는 결과 검증
- callback 검증은 목적이 명확할 때 사용
- 접근성 role과 name 기반 query 우선

---

### [FAQ]

Q. Interactive Component는 뭐야?
A. 사용자의 클릭, 입력, 선택, 키보드 조작에 따라 UI나 callback이 변경되는 Component다.

Q. Interactive Component Test는 어떤 도구를 써?
A. userEvent를 우선 사용한다.

Q. 클릭 후 내부 state를 확인해야 해?
A. 아니다. 클릭 후 화면에 표시되는 결과를 확인하는 것이 좋다.

---

## 3.2 Callback Test

### [개념]

Callback Test는 사용자의 행동 후 Component가 props로 받은 callback을 올바르게 호출하는지 검증하는 테스트다.

Callback만 검증할지, callback 이후 UI 결과까지 검증할지 테스트 목적에 따라 결정한다.

---

### [핵심]

Callback 대상:

- onClick
- onChange
- onSubmit
- onClose
- onOpen
- onSelect
- onSearch
- onDelete
- onToggle
- callback arguments
- called times

---

### [실무]

단순 callback 예:

```tsx
test("닫기 버튼을 클릭하면 onClose가 호출된다", async () => {
  const user = userEvent.setup();
  const onClose = vi.fn();

  render(<Modal title="공지사항" onClose={onClose} />);

  await user.click(screen.getByRole("button", { name: "닫기" }));

  expect(onClose).toHaveBeenCalledTimes(1);
});
```

callback 인자 검증:

```tsx
test("검색어 입력 후 검색하면 onSearch가 검색어와 함께 호출된다", async () => {
  const user = userEvent.setup();
  const onSearch = vi.fn();

  render(<SearchBox onSearch={onSearch} />);

  await user.type(screen.getByLabelText("검색어"), "축제");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(onSearch).toHaveBeenCalledWith("축제");
});
```

권장:

- callback 횟수 검증
- callback 인자 검증
- 사용자 이벤트로 callback 발생
- 내부 함수 직접 호출 지양
- 핵심 흐름에서는 UI 결과까지 검증

---

### [FAQ]

Q. Callback Test는 언제 필요해?
A. Presentational 또는 재사용 Component가 부모에게 이벤트를 전달하는 역할을 할 때 필요하다.

Q. callback 호출만 확인해도 돼?
A. 단순 Component는 가능하다. 하지만 사용자 흐름이 중요하면 화면 결과도 함께 검증한다.

Q. callback은 직접 호출해서 테스트해도 돼?
A. 지양한다. 사용자가 하는 행동으로 callback이 호출되는지 테스트한다.

---

## 3.3 Controlled Component Test

### [개념]

Controlled Component는 value와 onChange를 부모 Component가 관리하는 Component다.

Controlled Component Test에서는 부모 state를 업데이트하는 wrapper가 필요할 수 있다.

---

### [핵심]

- Controlled Component
- value prop
- onChange prop
- parent state
- wrapper component
- input value
- user.type
- toHaveValue
- state update
- callback

---

### [실무]

문제 예:

```tsx
test("검색어를 입력한다", async () => {
  const user = userEvent.setup();

  render(<SearchInput value="" onChange={vi.fn()} />);

  await user.type(screen.getByLabelText("검색어"), "축제");

  expect(screen.getByLabelText("검색어")).toHaveValue("축제");
});
```

위 테스트는 value가 부모에서 업데이트되지 않아 실패할 수 있다.

Wrapper 예:

```tsx
function SearchInputWrapper() {
  const [value, setValue] = useState("");

  return <SearchInput value={value} onChange={setValue} />;
}
```

테스트:

```tsx
test("검색어를 입력하면 입력값이 반영된다", async () => {
  const user = userEvent.setup();

  render(<SearchInputWrapper />);

  await user.type(screen.getByLabelText("검색어"), "축제");

  expect(screen.getByLabelText("검색어")).toHaveValue("축제");
});
```

callback만 검증하는 경우:

```tsx
test("입력하면 onChange가 호출된다", async () => {
  const user = userEvent.setup();
  const onChange = vi.fn();

  render(<SearchInput value="" onChange={onChange} />);

  await user.type(screen.getByLabelText("검색어"), "축제");

  expect(onChange).toHaveBeenCalled();
});
```

---

### [FAQ]

Q. Controlled Component 테스트가 왜 실패해?
A. value가 부모 state에서 내려오므로 테스트에서도 state를 업데이트하는 wrapper가 필요할 수 있다.

Q. wrapper는 언제 만들어?
A. 입력 후 실제 value 변경까지 검증하려면 wrapper를 만든다.

Q. onChange 호출만 확인해도 돼?
A. 재사용 input Component에서는 가능하다. 실제 입력값 반영까지 보려면 wrapper가 필요하다.

---

# 4. Common Component Patterns

## 4.1 Button Component Test

### [개념]

Button Component Test는 버튼 label, disabled 상태, loading 상태, click callback, type 속성, 접근 가능한 이름을 검증한다.

---

### [핵심]

Button 검증 대상:

- button name
- disabled
- enabled
- loading text
- onClick
- type submit
- type button
- aria-label
- icon button
- duplicate click prevention

---

### [실무]

기본 예:

```tsx
test("버튼 label을 표시한다", () => {
  render(<Button>저장</Button>);

  expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
});
```

disabled 예:

```tsx
test("disabled이면 버튼이 비활성화된다", () => {
  render(<Button disabled>저장</Button>);

  expect(screen.getByRole("button", { name: "저장" })).toBeDisabled();
});
```

click 예:

```tsx
test("버튼을 클릭하면 onClick이 호출된다", async () => {
  const user = userEvent.setup();
  const onClick = vi.fn();

  render(<Button onClick={onClick}>저장</Button>);

  await user.click(screen.getByRole("button", { name: "저장" }));

  expect(onClick).toHaveBeenCalledTimes(1);
});
```

loading 예:

```tsx
test("loading 상태이면 처리 중 문구와 disabled 상태를 표시한다", () => {
  render(<Button loading>저장</Button>);

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

---

### [FAQ]

Q. Button Component는 뭘 테스트해?
A. label, disabled, loading, onClick, accessible name을 테스트한다.

Q. 버튼 스타일 variant도 테스트해야 해?
A. 대부분 className보다 사용자에게 보이는 상태와 동작을 우선 검증한다.

Q. loading 버튼은 어떻게 테스트해?
A. 처리 중 문구와 disabled 상태를 검증한다.

---

## 4.2 Modal Component Test

### [개념]

Modal Component Test는 Modal이 열리고 닫히는지, dialog role이 있는지, title과 content가 표시되는지, close action과 keyboard interaction이 동작하는지 검증한다.

---

### [핵심]

Modal 검증 대상:

- dialog role
- modal title
- modal content
- open state
- close button
- onClose
- Escape close
- backdrop close
- focus trap
- aria-labelledby
- aria-modal
- hidden when closed

---

### [실무]

표시 테스트:

```tsx
test("open 상태이면 모달 제목과 내용을 표시한다", () => {
  render(
    <ConfirmModal open title="삭제 확인" onClose={vi.fn()}>
      정말 삭제하시겠습니까?
    </ConfirmModal>,
  );

  expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
  expect(screen.getByText("정말 삭제하시겠습니까?")).toBeInTheDocument();
});
```

닫기 버튼 테스트:

```tsx
test("닫기 버튼을 클릭하면 onClose가 호출된다", async () => {
  const user = userEvent.setup();
  const onClose = vi.fn();

  render(<ConfirmModal open title="삭제 확인" onClose={onClose} />);

  await user.click(screen.getByRole("button", { name: "닫기" }));

  expect(onClose).toHaveBeenCalledTimes(1);
});
```

닫힌 상태 테스트:

```tsx
test("open이 false이면 dialog를 표시하지 않는다", () => {
  render(<ConfirmModal open={false} title="삭제 확인" onClose={vi.fn()} />);

  expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
});
```

권장:

- dialog role과 accessible name 확인
- close button 확인
- Escape close가 있으면 keyboard 테스트
- focus trap은 접근성 중요 UI에서 검증
- Portal 사용 시 test setup 확인

---

### [FAQ]

Q. Modal은 어떻게 테스트해?
A. open 상태에서 dialog, title, content를 확인하고 닫기 버튼이나 Escape 동작을 테스트한다.

Q. Modal이 닫혔는지는 어떻게 확인해?
A. `queryByRole("dialog")`가 문서에 없는지 확인한다.

Q. Modal 접근성에서 중요한 건 뭐야?
A. dialog role, accessible name, focus 관리, Escape 닫기, aria-modal 등이 중요하다.

---

## 4.3 Dropdown Component Test

### [개념]

Dropdown Component Test는 사용자가 버튼이나 combobox를 눌러 옵션 목록을 열고, option을 선택했을 때 선택 결과가 반영되는지 검증한다.

---

### [핵심]

Dropdown 검증 대상:

- trigger button
- combobox
- menu
- listbox
- option
- open / close
- select option
- selected label
- onSelect
- keyboard navigation
- outside click
- aria-expanded

---

### [실무]

기본 예:

```tsx
test("드롭다운을 열고 옵션을 선택한다", async () => {
  const user = userEvent.setup();
  const onSelect = vi.fn();

  render(
    <RegionDropdown
      options={[
        { label: "서울", value: "seoul" },
        { label: "부산", value: "busan" },
      ]}
      onSelect={onSelect}
    />,
  );

  await user.click(screen.getByRole("button", { name: "지역 선택" }));

  await user.click(screen.getByRole("option", { name: "서울" }));

  expect(onSelect).toHaveBeenCalledWith("seoul");
});
```

선택 결과 표시:

```tsx
expect(screen.getByRole("button", { name: "서울" })).toBeInTheDocument();
```

권장:

- trigger는 button 또는 combobox role로 찾음
- option은 role과 name으로 찾음
- 선택 후 menu가 닫히는지 확인 가능
- keyboard navigation이 중요하면 별도 테스트
- custom dropdown은 접근성 role 설계 확인

---

### [FAQ]

Q. Dropdown은 어떻게 테스트해?
A. trigger를 클릭해 option을 표시하고 option 클릭 후 선택 결과나 callback을 검증한다.

Q. Dropdown option은 어떤 Query로 찾아?
A. 가능한 경우 `getByRole("option", { name })`을 사용한다.

Q. custom dropdown은 테스트가 어려운 이유는?
A. semantic role과 keyboard 접근성이 제대로 설계되지 않으면 사용자 관점 Query가 어렵기 때문이다.

---

## 4.4 Tab Component Test

### [개념]

Tab Component Test는 사용자가 tab을 선택했을 때 선택 상태와 tab panel 내용이 올바르게 변경되는지 검증한다.

---

### [핵심]

Tab 검증 대상:

- tablist
- tab
- tabpanel
- selected tab
- aria-selected
- keyboard navigation
- content change
- active panel
- inactive panel hidden

---

### [실무]

예:

```tsx
test("공지 탭을 클릭하면 공지 내용을 표시한다", async () => {
  const user = userEvent.setup();

  render(<FestivalTabs />);

  await user.click(screen.getByRole("tab", { name: "공지" }));

  expect(screen.getByRole("tabpanel", { name: "공지" })).toHaveTextContent(
    "공지 내용",
  );
});
```

선택 상태:

```tsx
expect(screen.getByRole("tab", { name: "공지" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

권장:

- tab / tabpanel role 사용
- 선택된 tab 상태 확인
- panel 내용 변경 확인
- keyboard arrow 이동이 있으면 테스트
- 숨겨진 panel 처리 기준 명확히 검증

---

### [FAQ]

Q. Tab Component는 어떻게 테스트해?
A. tab을 클릭하고 선택 상태와 tabpanel 내용이 변경되는지 검증한다.

Q. Tab은 어떤 role을 써야 해?
A. tablist, tab, tabpanel role을 사용하는 것이 좋다.

Q. aria-selected도 테스트해야 해?
A. 접근성이 중요한 Tab UI에서는 선택 상태 확인에 유용하다.

---

## 4.5 Accordion Component Test

### [개념]

Accordion Component Test는 사용자가 header 버튼을 클릭했을 때 content가 펼쳐지거나 접히는지 검증한다.

---

### [핵심]

Accordion 검증 대상:

- trigger button
- expanded content
- collapsed content
- aria-expanded
- show / hide
- multiple open
- single open
- keyboard support

---

### [실무]

예:

```tsx
test("아코디언 버튼을 클릭하면 내용을 표시한다", async () => {
  const user = userEvent.setup();

  render(<Accordion title="상세 정보">축제 상세 설명</Accordion>);

  const trigger = screen.getByRole("button", { name: "상세 정보" });

  expect(screen.queryByText("축제 상세 설명")).not.toBeInTheDocument();

  await user.click(trigger);

  expect(screen.getByText("축제 상세 설명")).toBeInTheDocument();
  expect(trigger).toHaveAttribute("aria-expanded", "true");
});
```

접힘 테스트:

```tsx
await user.click(trigger);

expect(screen.queryByText("축제 상세 설명")).not.toBeInTheDocument();
expect(trigger).toHaveAttribute("aria-expanded", "false");
```

권장:

- trigger는 button으로 구현
- aria-expanded 확인
- content 표시 / 숨김 검증
- keyboard 조작이 있으면 테스트
- 여러 개 accordion의 동시 열림 정책 검증 가능

---

### [FAQ]

Q. Accordion은 어떻게 테스트해?
A. trigger button을 클릭하고 content가 표시되거나 사라지는지 확인한다.

Q. aria-expanded도 테스트해야 해?
A. 접근성 상태를 나타내므로 테스트하면 좋다.

Q. 접힌 content는 queryBy로 확인해?
A. DOM에서 제거되는 방식이면 queryBy로 확인한다. 숨김 처리라면 visibility를 확인한다.

---

## 4.6 List Component Test

### [개념]

List Component Test는 배열 데이터가 목록, 카드, 테이블 행으로 올바르게 렌더링되는지 검증하는 테스트다.

빈 목록과 항목 목록을 모두 테스트하는 것이 좋다.

---

### [핵심]

List 검증 대상:

- list
- listitem
- card list
- table row
- item count
- item text
- empty state
- key caution
- duplicated item
- item action button
- within

---

### [실무]

목록 예:

```tsx
test("축제 목록을 표시한다", () => {
  render(
    <FestivalList
      festivals={[
        { festivalId: 1, title: "봄꽃 축제" },
        { festivalId: 2, title: "음악 축제" },
      ]}
    />,
  );

  expect(screen.getByText("봄꽃 축제")).toBeInTheDocument();
  expect(screen.getByText("음악 축제")).toBeInTheDocument();
});
```

개수 검증:

```tsx
expect(screen.getAllByRole("listitem")).toHaveLength(2);
```

빈 목록:

```tsx
test("축제가 없으면 EmptyState를 표시한다", () => {
  render(<FestivalList festivals={[]} />);

  expect(screen.getByText("표시할 축제가 없습니다.")).toBeInTheDocument();
});
```

항목 내부 버튼:

```tsx
const card = screen.getByRole("article", { name: "봄꽃 축제" });

expect(
  within(card).getByRole("button", { name: "찜하기" }),
).toBeInTheDocument();
```

---

### [FAQ]

Q. List Component는 어떻게 테스트해?
A. 항목 텍스트, 항목 개수, 빈 목록 상태를 검증한다.

Q. 목록 개수는 어떻게 확인해?
A. listitem, row, article 등을 `getAllByRole`로 찾아 length를 검증한다.

Q. 목록 항목 안의 버튼은 어떻게 구분해?
A. 특정 카드나 행을 먼저 찾고 within으로 내부 버튼을 찾는다.

---

# 5. State UI Component Test

## 5.1 Loading State Component Test

### [개념]

Loading State Component Test는 Component가 loading 상태일 때 loading message, spinner, skeleton, disabled 상태를 올바르게 표시하는지 검증한다.

---

### [핵심]

Loading 검증 대상:

- loading text
- spinner
- skeleton
- role status
- aria-busy
- disabled button
- pending state
- duplicate action prevention

---

### [실무]

예:

```tsx
test("loading 상태이면 로딩 메시지를 표시한다", () => {
  render(<FestivalList loading festivals={[]} />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
});
```

버튼 loading:

```tsx
test("제출 중이면 버튼이 비활성화된다", () => {
  render(<SubmitButton loading>등록</SubmitButton>);

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

권장:

- loading 상태가 사용자에게 전달되는지 확인
- role status 또는 loading label 사용
- 버튼 중복 클릭 방지 검증
- loading과 empty state가 동시에 표시되지 않도록 검증 가능

---

### [FAQ]

Q. Loading State는 Component Test 대상이야?
A. 그렇다. loading 메시지, spinner, skeleton, disabled 상태를 검증할 수 있다.

Q. loading spinner는 어떻게 찾으면 좋아?
A. 사용자에게 전달되는 role status, aria-label, loading text를 사용하는 것이 좋다.

Q. loading과 empty state가 동시에 나오면 안 돼?
A. 일반적으로 loading 중에는 empty state를 표시하지 않는 것이 좋다.

---

## 5.2 Error State Component Test

### [개념]

Error State Component Test는 Component가 오류 상태일 때 사용자 오류 메시지, retry 버튼, 권한 안내, Not Found 안내를 표시하는지 검증한다.

---

### [핵심]

Error 검증 대상:

- error message
- role alert
- retry button
- forbidden message
- not found message
- global error
- field error
- safe message
- server detail hiding

---

### [실무]

예:

```tsx
test("error 상태이면 오류 메시지와 다시 시도 버튼을 표시한다", () => {
  render(<ErrorState message="서버 오류가 발생했습니다." onRetry={vi.fn()} />);

  expect(screen.getByRole("alert")).toHaveTextContent(
    "서버 오류가 발생했습니다.",
  );
  expect(screen.getByRole("button", { name: "다시 시도" })).toBeInTheDocument();
});
```

Retry callback:

```tsx
test("다시 시도 버튼을 클릭하면 onRetry가 호출된다", async () => {
  const user = userEvent.setup();
  const onRetry = vi.fn();

  render(<ErrorState message="조회 실패" onRetry={onRetry} />);

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(onRetry).toHaveBeenCalledTimes(1);
});
```

권장:

- 오류 메시지는 사용자 친화적 문구
- 서버 내부 상세 메시지 노출 지양
- retry action 검증
- role alert 사용 고려
- 권한 오류와 서버 오류 문구 구분

---

### [FAQ]

Q. Error State는 Component Test 대상이야?
A. 그렇다. 오류 메시지, alert role, retry 버튼, callback을 검증할 수 있다.

Q. 서버 내부 에러를 그대로 표시해도 돼?
A. 권장하지 않는다. 사용자에게 안전하고 일반적인 메시지를 표시한다.

Q. retry 버튼도 테스트해야 해?
A. retry 기능이 있으면 클릭 시 onRetry가 호출되는지 테스트하는 것이 좋다.

---

## 5.3 Empty State Component Test

### [개념]

Empty State Component Test는 데이터가 없을 때 빈 화면 대신 안내 메시지와 필요한 action이 표시되는지 검증한다.

---

### [핵심]

Empty 검증 대상:

- empty message
- no result message
- no data message
- reset filter action
- create action
- first use guide
- search no result
- no notification
- no review

---

### [실무]

예:

```tsx
test("데이터가 없으면 EmptyState 메시지를 표시한다", () => {
  render(<EmptyState message="검색 결과가 없습니다." />);

  expect(screen.getByText("검색 결과가 없습니다.")).toBeInTheDocument();
});
```

Action 포함:

```tsx
test("필터 초기화 버튼을 클릭하면 onReset이 호출된다", async () => {
  const user = userEvent.setup();
  const onReset = vi.fn();

  render(
    <EmptyState
      message="검색 결과가 없습니다."
      actionLabel="필터 초기화"
      onAction={onReset}
    />,
  );

  await user.click(screen.getByRole("button", { name: "필터 초기화" }));

  expect(onReset).toHaveBeenCalledTimes(1);
});
```

권장:

- 빈 목록과 오류 상태 구분
- 검색 결과 없음과 최초 데이터 없음 문구 구분 가능
- action이 있으면 callback 검증
- loading 중 empty 표시 방지 검토

---

### [FAQ]

Q. Empty State는 왜 테스트해?
A. 데이터가 없을 때 빈 화면이 아니라 적절한 안내가 표시되는지 확인하기 위해 필요하다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 성공 응답의 빈 데이터이고 Error State는 실패 상태다.

Q. EmptyState action도 테스트해야 해?
A. action이 있으면 callback이나 화면 결과를 검증하는 것이 좋다.

---

# 6. Accessibility Component Test

## 6.1 Accessibility Query Test

### [개념]

Accessibility Query Test는 Component를 role, label, accessible name 기준으로 찾을 수 있는지 검증하는 테스트다.

좋은 접근성 구조는 좋은 Component Test를 가능하게 한다.

---

### [핵심]

검증 대상:

- button accessible name
- input label
- heading role
- image alt
- dialog role
- alert role
- status role
- aria-expanded
- aria-selected
- aria-invalid
- aria-describedby
- icon button aria-label

---

### [실무]

예:

```tsx
test("검색 Form은 접근 가능한 입력창과 버튼을 제공한다", () => {
  render(<SearchForm />);

  expect(screen.getByRole("textbox", { name: "검색어" })).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
});
```

오류 접근성:

```tsx
test("입력 오류가 있으면 alert를 표시한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm />);

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByRole("alert")).toHaveTextContent(
    "이메일을 입력해 주세요.",
  );
});
```

권장:

- getByRole / getByLabelText 우선 사용
- icon button에는 aria-label 제공
- Modal은 dialog role과 name 확인
- Form error는 role alert 또는 aria-describedby 고려
- 접근성 Query 실패 시 Component 개선 우선

---

### [FAQ]

Q. Component Test에서 접근성도 확인할 수 있어?
A. role, label, name 기반 Query를 사용하면 기본 접근성 문제를 함께 발견할 수 있다.

Q. getByRole 실패는 접근성 문제일 수 있어?
A. 가능하다. semantic HTML이나 accessible name이 부족할 수 있다.

Q. icon button에는 무엇이 필요해?
A. 사용자가 의미를 알 수 있도록 aria-label이나 보이는 텍스트가 필요하다.

---

## 6.2 ARIA State Test

### [개념]

ARIA State Test는 Component의 선택, 확장, 오류, 숨김 상태가 aria 속성으로 올바르게 표현되는지 검증하는 테스트다.

Interactive UI에서 접근성 상태를 확인할 때 사용한다.

---

### [핵심]

ARIA 상태:

- aria-expanded
- aria-selected
- aria-checked
- aria-invalid
- aria-describedby
- aria-controls
- aria-current
- aria-hidden
- aria-busy
- aria-modal

---

### [실무]

Accordion:

```tsx
test("아코디언이 열리면 aria-expanded가 true가 된다", async () => {
  const user = userEvent.setup();

  render(<Accordion title="상세 정보">내용</Accordion>);

  const button = screen.getByRole("button", { name: "상세 정보" });

  expect(button).toHaveAttribute("aria-expanded", "false");

  await user.click(button);

  expect(button).toHaveAttribute("aria-expanded", "true");
});
```

Tab:

```tsx
expect(screen.getByRole("tab", { name: "공지" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

Form error:

```tsx
expect(screen.getByLabelText("이메일")).toHaveAttribute("aria-invalid", "true");
```

권장:

- aria 속성은 사용자 접근성 상태와 연결될 때 테스트
- 단순 구현 세부사항으로만 테스트하지 않음
- UI 결과와 함께 검증
- ARIA를 잘못 쓰기보다 semantic HTML 우선

---

### [FAQ]

Q. aria-expanded는 언제 테스트해?
A. Accordion, Dropdown처럼 펼침 상태를 보조기술에 전달해야 하는 UI에서 테스트한다.

Q. aria 속성은 전부 테스트해야 해?
A. 아니다. 사용자 접근성 상태에 중요한 속성을 중심으로 테스트한다.

Q. ARIA를 많이 붙이면 접근성이 좋아져?
A. 아니다. semantic HTML을 우선하고 필요한 경우에만 올바르게 사용한다.

---

# 7. Component Test Structure

## 7.1 Test File Location

### [개념]

Component Test 파일은 Component 옆에 두거나 feature 단위 `__tests__` 폴더에 둘 수 있다.

중요한 것은 팀 컨벤션과 일관성이다.

---

### [핵심]

배치 방식:

- colocated test
- component adjacent test
- feature **tests**
- test utils
- mocks
- fixtures
- renderWithProviders
- setup file

---

### [실무]

Component 옆 배치:

```text
src/components/Button/Button.tsx
src/components/Button/Button.test.tsx
```

Feature 단위 배치:

```text
src/features/festival/components/FestivalCard.tsx
src/features/festival/components/FestivalCard.test.tsx
```

공통 test utility:

```text
src/test/renderWithProviders.tsx
src/test/createTestQueryClient.ts
src/test/setup.ts
src/test/fixtures
```

권장:

- Component와 테스트를 가까이 배치
- 공통 Provider 설정은 test utils로 분리
- fixture 데이터는 작고 의미 있게 유지
- 테스트 파일명은 `.test.tsx` 또는 `.spec.tsx`로 통일
- 한 테스트 파일에 너무 많은 Component를 섞지 않음

---

### [FAQ]

Q. Component Test 파일은 어디에 두는 게 좋아?
A. Component 옆에 두거나 feature의 테스트 폴더에 둘 수 있다. 팀 컨벤션에 맞추면 된다.

Q. renderWithProviders는 어디에 둬?
A. `src/test/renderWithProviders.tsx` 같은 공통 test utils 폴더가 적합하다.

Q. 테스트 데이터 fixture는 어떻게 관리해?
A. 작고 명확한 도메인 데이터만 두고 과도하게 복잡한 fixture는 피한다.

---

## 7.2 Component Test Naming Rules

### [개념]

Component Test 이름은 사용자 시나리오와 기대 결과가 드러나도록 작성한다.

실패했을 때 어떤 UI 동작이 깨졌는지 바로 알 수 있어야 한다.

---

### [핵심]

좋은 이름:

- props 상황 포함
- 사용자 행동 포함
- 기대 결과 포함
- 조건부 상태 포함
- 접근 가능한 결과 포함
- 도메인 용어 포함

나쁜 이름:

- renders
- works
- click test
- state changes
- component test
- case1

---

### [실무]

좋은 예:

```tsx
test("축제 카드에 제목과 지역명을 표시한다", () => {});
test("찜하기 버튼을 클릭하면 onFavorite가 호출된다", async () => {});
test("축제가 없으면 EmptyState를 표시한다", () => {});
test("비활성화 상태이면 저장 버튼이 disabled 된다", () => {});
test("닫기 버튼을 클릭하면 모달이 닫힌다", async () => {});
```

나쁜 예:

```tsx
test("renders", () => {});
test("button works", () => {});
test("state true", () => {});
test("props test", () => {});
```

권장:

- 한국어 프로젝트면 테스트명도 한국어 가능
- describe는 Component 이름 기준
- test는 사용자 시나리오 기준
- 너무 길면 describe로 문맥 분리

---

### [FAQ]

Q. Component Test 이름은 어떻게 작성해?
A. 사용자의 상황, 행동, 기대 결과가 드러나게 작성한다.

Q. renders 같은 이름은 왜 안 좋아?
A. 무엇이 렌더링되어야 하는지 알 수 없어 실패 원인을 파악하기 어렵다.

Q. 테스트 이름을 한글로 써도 돼?
A. 가능하다. 팀 컨벤션에 맞고 의미가 명확하면 좋다.

---

# 8. Component Test Troubleshooting

## 8.1 Component Query Failed

### [개념]

Component Query Failed는 Component Test에서 원하는 요소를 찾지 못하는 상황이다.

Query 선택, props 누락, 조건부 렌더링, Provider 누락, 접근성 이름 누락을 확인해야 한다.

---

### [핵심]

원인:

- props 누락
- 잘못된 Query
- accessible name 없음
- label 연결 누락
- 조건부 렌더링 조건 미충족
- 비동기 UI에 getBy 사용
- absence 검증에 getBy 사용
- Provider 누락
- text split
- 중복 요소
- hidden element

---

### [실무]

Debug Flow:

```text
Query 실패
→ screen.debug 확인
→ props 입력 확인
→ 실제 DOM 확인
→ role / name 확인
→ label 연결 확인
→ 조건부 렌더링 조건 확인
→ 비동기 여부 확인
→ Provider 필요 여부 확인
→ within 필요 여부 확인
```

예:

```tsx
screen.debug();
```

비동기 수정:

```tsx
expect(await screen.findByText("조회 성공")).toBeInTheDocument();
```

absence 수정:

```tsx
expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

권장:

- Query 실패를 testId로 바로 우회하지 않음
- 접근성 구조 문제인지 먼저 확인
- 조건부 렌더링 props를 확인
- 필요한 Provider를 renderWithProviders에 추가

---

### [FAQ]

Q. Component Test에서 요소를 못 찾으면 뭘 확인해?
A. screen.debug로 DOM을 확인하고 props, query, accessible name, 조건부 렌더링, Provider를 확인한다.

Q. getByRole이 실패하면 바로 testId를 쓰면 돼?
A. 먼저 semantic HTML과 accessible name 문제를 확인하는 것이 좋다.

Q. 텍스트가 보이는데 getByText가 실패해.
A. 텍스트가 여러 요소로 나뉘었거나 비동기 렌더링 전일 수 있다.

---

## 8.2 Component Event Not Working

### [개념]

Component Event Not Working은 click, type, select 같은 사용자 이벤트 후 UI 결과나 callback이 발생하지 않는 상황이다.

userEvent await, disabled 상태, controlled component, callback 전달, mock 설정을 확인해야 한다.

---

### [핵심]

원인:

- userEvent await 누락
- disabled element
- wrong element query
- hidden element
- controlled component wrapper 없음
- callback prop 누락
- onChange 연결 누락
- validation 조건 미충족
- async result에 getBy 사용
- Provider 누락
- mock 누락

---

### [실무]

Debug Flow:

```text
이벤트 동작 안 함
→ await user action 확인
→ 클릭 대상 disabled 여부 확인
→ 올바른 element인지 확인
→ callback prop 전달 확인
→ controlled wrapper 필요 여부 확인
→ validation 조건 확인
→ async 결과는 findBy 사용
```

문제 예:

```tsx
render(<SearchInput value="" onChange={vi.fn()} />);
await user.type(screen.getByLabelText("검색어"), "축제");
expect(screen.getByLabelText("검색어")).toHaveValue("축제");
```

개선:

```tsx
render(<SearchInputWrapper />);
await user.type(screen.getByLabelText("검색어"), "축제");
expect(screen.getByLabelText("검색어")).toHaveValue("축제");
```

권장:

- userEvent는 항상 await
- controlled component는 wrapper 고려
- disabled 상태라면 not called 검증
- 비동기 결과는 findBy 사용
- callback prop 이름과 인자 확인

---

### [FAQ]

Q. click했는데 callback이 호출되지 않아.
A. 버튼이 disabled이거나 callback prop이 제대로 전달되지 않았거나 잘못된 요소를 클릭했을 수 있다.

Q. type했는데 value가 안 바뀌어.
A. controlled component에서 부모 state wrapper가 없을 수 있다.

Q. 이벤트 후 결과를 못 찾으면?
A. 비동기 결과일 수 있으므로 findBy를 사용한다.

---

# 9. Component Test Anti Pattern

## 9.1 Common Component Test Anti Patterns

### [개념]

Component Test Anti Pattern은 테스트가 사용자 관점에서 벗어나거나 구현 변경에 취약해지는 잘못된 작성 방식이다.

Component Test는 화면 결과와 사용자 상호작용을 중심으로 작성해야 한다.

---

### [핵심]

Anti Pattern:

- internal state 직접 검증
- private function 직접 호출
- container.querySelector 남용
- CSS class 중심 테스트
- snapshot-only test
- testId 우선 사용
- getBy로 absence 검증
- getBy로 async UI 검증
- userEvent await 누락
- waitFor 안에서 userEvent 실행
- Provider 누락
- mock reset 누락
- 테스트 간 상태 공유
- 실제 API 호출
- 너무 큰 fixture 사용

---

### [실무]

나쁜 예:

```tsx
const button = container.querySelector(".save-button");
fireEvent.click(button!);
expect(component.state.isSaved).toBe(true);
```

좋은 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

나쁜 예:

```tsx
expect(screen.getByText("에러")).not.toBeInTheDocument();
```

좋은 예:

```tsx
expect(screen.queryByText("에러")).not.toBeInTheDocument();
```

검수 기준:

```text
사용자 query를 사용하는가?
userEvent에 await가 있는가?
결과 UI를 검증하는가?
비동기와 absence query가 올바른가?
구현 세부사항에 의존하지 않는가?
```

---

### [FAQ]

Q. Component Test에서 가장 흔한 실수는 뭐야?
A. 내부 state를 테스트하거나 userEvent await를 누락하거나 비동기 UI에 getBy를 사용하는 것이다.

Q. snapshot-only Component Test는 왜 문제야?
A. 사용자 행동과 결과를 명확히 검증하지 못하고 의미 없는 변경에도 쉽게 깨질 수 있다.

Q. testId를 먼저 쓰면 안 돼?
A. role, label, text 같은 사용자 인식 Query를 먼저 고려해야 한다.

---

# 10. Component Test Checklist

## 10.1 Component Test Checklist

### [개념]

Component Test Checklist는 React Component 테스트가 사용자 관점, 접근성, 상호작용, 상태 검증 기준을 만족하는지 확인하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] Component 테스트 대상이 명확한가?
- [ ] props 기반 화면 결과를 검증했는가?
- [ ] 사용자 관점 Query를 사용했는가?
- [ ] getByRole / getByLabelText를 우선 검토했는가?
- [ ] userEvent를 사용했는가?
- [ ] userEvent에 await를 붙였는가?
- [ ] callback 호출 횟수와 인자를 검증했는가?
- [ ] callback 이후 UI 결과가 있으면 검증했는가?
- [ ] 조건부 렌더링의 표시 / 미표시를 모두 검증했는가?
- [ ] absence 검증에 queryBy를 사용했는가?
- [ ] 비동기 결과에 findBy를 사용했는가?
- [ ] Loading / Error / Empty 상태를 검증했는가?
- [ ] 접근성 role / label / aria 상태를 확인했는가?
- [ ] Controlled Component에는 wrapper 필요 여부를 검토했는가?
- [ ] 내부 state / className 중심 테스트를 피했는가?
- [ ] 실제 API 호출을 피했는가?
```

---

### [실무]

Agent Component Test 작성 Flow:

```text
Identify Component Type
→ Presentational or Interactive 판단
→ Define Props Cases
→ Define User Actions
→ Render Component
→ Query by Role / Label / Text
→ Execute userEvent
→ Assert Visible Result
→ Check Conditional State
→ Review Anti Pattern
```

예:

```text
FestivalCard
→ props title / region / image 표시
→ detail link href 확인
→ favorite button click callback
→ no image default state 확인
```

---

### [FAQ]

Q. Component Test 작성 전 무엇을 정해야 해?
A. Component 유형, props 케이스, 사용자 행동, 상태 UI, callback 검증 여부를 정해야 한다.

Q. Component Test Checklist의 핵심은 뭐야?
A. 사용자 관점 Query, userEvent, 화면 결과 검증, 조건부 상태 검증이다.

Q. Component Test가 너무 복잡하면 어떻게 해?
A. Component 책임을 줄이거나 Integration Test로 분리할 흐름인지 검토한다.

---

# 11. Part06 Summary

## 11.1 Component Test Final Rule

### [개념]

Frontend Testing Part06은 React Component Test의 작성 기준을 정의한다.

이 Part의 목적은 Agent가 Presentational Component와 Interactive Component를 사용자 관점으로 검증하고, Loading / Error / Empty / Accessibility 상태를 안정적으로 테스트하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Component Test는 사용자 화면과 상호작용 중심
- Presentational Component는 props 기반 UI 검증
- Interactive Component는 userEvent 기반 검증
- Callback은 사용자 행동으로 발생시켜 검증
- Controlled Component는 wrapper 필요 여부 확인
- Button / Modal / Dropdown / Tab / Accordion / List 패턴 검증
- Loading / Error / Empty 상태 검증
- 접근성 role / label / aria 상태 검증
- queryBy / findBy / within 적절히 사용
- 내부 state / CSS class / snapshot-only 테스트 지양
- 실제 API 호출 금지

---

### [실무]

Agent 작업 Flow:

```text
Component Test Request
→ Identify Component Responsibility
→ Choose Test Cases
→ Render Component
→ Query Accessible Element
→ Simulate User Event
→ Assert UI Result
→ Verify State UI
→ Check Accessibility
→ Remove Anti Pattern
```

Part07 이후 연결:

```text
Part06 Component Test
→ Part07 Form Testing
→ Part08 API Mocking
→ Part09 Loading Error Empty
→ Part10 Router Auth Testing
→ Part11 TanStack Query Testing
```

---

### [FAQ]

Q. Part06의 최종 목적은 뭐야?
A. Frontend Agent가 React Component를 사용자 관점으로 렌더링, 상호작용, 상태 UI까지 검증하게 만드는 것이다.

Q. Component Test에서 가장 중요한 규칙은 뭐야?
A. 내부 구현이 아니라 사용자가 보는 화면과 수행하는 행동 결과를 테스트하는 것이다.

Q. Part06 다음에는 어떤 내용이 이어져야 해?
A. Form 입력, validation, submit, field error를 검증하는 Form Testing 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Component Test는 뭐야?
A. React Component가 props, 사용자 이벤트, 조건부 렌더링에 따라 올바른 UI 결과를 만드는지 검증하는 테스트다.

Q. Component Test에서 가장 중요한 기준은 뭐야?
A. 내부 구현보다 사용자가 보는 화면과 조작 결과를 검증하는 것이다.

Q. Component Test는 Unit Test와 달라?
A. 다르다. Unit Test는 순수 함수 중심이고 Component Test는 React Component의 화면과 상호작용 중심이다.

Q. Component Test는 어디까지 검증해?
A. 단일 Component의 표시, 입력, 클릭, 조건부 상태, callback, 접근성 요소를 검증한다.

Q. API 호출이 있는 Component는 Component Test로 못 해?
A. 가능하지만 실제 API는 호출하지 않고 mock으로 제어한다. 여러 Provider와 상태 흐름이 엮이면 Integration Test에 가깝다.

Q. Presentational Component는 뭘 테스트해?
A. props에 따라 사용자가 보는 텍스트, 이미지, 버튼, 링크, 상태 표시가 올바른지 테스트한다.

Q. Card Component는 어떻게 테스트해?
A. 카드의 제목, 설명, 이미지 alt, 링크, 버튼 같은 사용자 표시 요소를 검증한다.

Q. Props Rendering Test는 뭐야?
A. Component에 전달한 props가 화면에 올바르게 반영되는지 검증하는 테스트다.

Q. optional prop도 테스트해야 해?
A. 조건부 UI가 달라진다면 테스트하는 것이 좋다.

Q. Conditional Rendering은 어떻게 테스트해?
A. 조건값을 다르게 전달하고 특정 UI가 표시되거나 표시되지 않는지 검증한다.

Q. 표시되지 않아야 하는 요소는 어떤 Query를 써?
A. `queryBy`를 사용한다.

Q. 권한별 버튼 표시도 Component Test 대상이야?
A. 단순 표시 여부는 Component Test 대상이다. 실제 권한 흐름 전체는 Integration Test로 검증한다.

Q. Interactive Component는 뭐야?
A. 사용자의 클릭, 입력, 선택, 키보드 조작에 따라 UI나 callback이 변경되는 Component다.

Q. Interactive Component Test는 어떤 도구를 써?
A. userEvent를 우선 사용한다.

Q. 클릭 후 내부 state를 확인해야 해?
A. 아니다. 클릭 후 화면에 표시되는 결과를 확인하는 것이 좋다.

Q. Callback Test는 언제 필요해?
A. Presentational 또는 재사용 Component가 부모에게 이벤트를 전달하는 역할을 할 때 필요하다.

Q. callback 호출만 확인해도 돼?
A. 단순 Component는 가능하다. 하지만 사용자 흐름이 중요하면 화면 결과도 함께 검증한다.

Q. callback은 직접 호출해서 테스트해도 돼?
A. 지양한다. 사용자가 하는 행동으로 callback이 호출되는지 테스트한다.

Q. Controlled Component 테스트가 왜 실패해?
A. value가 부모 state에서 내려오므로 테스트에서도 state를 업데이트하는 wrapper가 필요할 수 있다.

Q. Controlled Component wrapper는 언제 만들어?
A. 입력 후 실제 value 변경까지 검증하려면 wrapper를 만든다.

Q. onChange 호출만 확인해도 돼?
A. 재사용 input Component에서는 가능하다. 실제 입력값 반영까지 보려면 wrapper가 필요하다.

Q. Button Component는 뭘 테스트해?
A. label, disabled, loading, onClick, accessible name을 테스트한다.

Q. loading 버튼은 어떻게 테스트해?
A. 처리 중 문구와 disabled 상태를 검증한다.

Q. Modal은 어떻게 테스트해?
A. open 상태에서 dialog, title, content를 확인하고 닫기 버튼이나 Escape 동작을 테스트한다.

Q. Modal이 닫혔는지는 어떻게 확인해?
A. `queryByRole("dialog")`가 문서에 없는지 확인한다.

Q. Modal 접근성에서 중요한 건 뭐야?
A. dialog role, accessible name, focus 관리, Escape 닫기, aria-modal 등이 중요하다.

Q. Dropdown은 어떻게 테스트해?
A. trigger를 클릭해 option을 표시하고 option 클릭 후 선택 결과나 callback을 검증한다.

Q. Dropdown option은 어떤 Query로 찾아?
A. 가능한 경우 `getByRole("option", { name })`을 사용한다.

Q. custom dropdown은 테스트가 어려운 이유는?
A. semantic role과 keyboard 접근성이 제대로 설계되지 않으면 사용자 관점 Query가 어렵기 때문이다.

Q. Tab Component는 어떻게 테스트해?
A. tab을 클릭하고 선택 상태와 tabpanel 내용이 변경되는지 검증한다.

Q. Tab은 어떤 role을 써야 해?
A. tablist, tab, tabpanel role을 사용하는 것이 좋다.

Q. Accordion은 어떻게 테스트해?
A. trigger button을 클릭하고 content가 표시되거나 사라지는지 확인한다.

Q. aria-expanded도 테스트해야 해?
A. 접근성 상태를 나타내므로 테스트하면 좋다.

Q. List Component는 어떻게 테스트해?
A. 항목 텍스트, 항목 개수, 빈 목록 상태를 검증한다.

Q. 목록 개수는 어떻게 확인해?
A. listitem, row, article 등을 `getAllByRole`로 찾아 length를 검증한다.

Q. 목록 항목 안의 버튼은 어떻게 구분해?
A. 특정 카드나 행을 먼저 찾고 within으로 내부 버튼을 찾는다.

Q. Loading State는 Component Test 대상이야?
A. 그렇다. loading 메시지, spinner, skeleton, disabled 상태를 검증할 수 있다.

Q. loading spinner는 어떻게 찾으면 좋아?
A. 사용자에게 전달되는 role status, aria-label, loading text를 사용하는 것이 좋다.

Q. Error State는 Component Test 대상이야?
A. 그렇다. 오류 메시지, alert role, retry 버튼, callback을 검증할 수 있다.

Q. retry 버튼도 테스트해야 해?
A. retry 기능이 있으면 클릭 시 onRetry가 호출되는지 테스트하는 것이 좋다.

Q. Empty State는 왜 테스트해?
A. 데이터가 없을 때 빈 화면이 아니라 적절한 안내가 표시되는지 확인하기 위해 필요하다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 성공 응답의 빈 데이터이고 Error State는 실패 상태다.

Q. Component Test에서 접근성도 확인할 수 있어?
A. role, label, name 기반 Query를 사용하면 기본 접근성 문제를 함께 발견할 수 있다.

Q. getByRole 실패는 접근성 문제일 수 있어?
A. 가능하다. semantic HTML이나 accessible name이 부족할 수 있다.

Q. aria-expanded는 언제 테스트해?
A. Accordion, Dropdown처럼 펼침 상태를 보조기술에 전달해야 하는 UI에서 테스트한다.

Q. Component Test 파일은 어디에 두는 게 좋아?
A. Component 옆에 두거나 feature의 테스트 폴더에 둘 수 있다. 팀 컨벤션에 맞추면 된다.

Q. Component Test 이름은 어떻게 작성해?
A. 사용자의 상황, 행동, 기대 결과가 드러나게 작성한다.

Q. Component Test에서 요소를 못 찾으면 뭘 확인해?
A. screen.debug로 DOM을 확인하고 props, query, accessible name, 조건부 렌더링, Provider를 확인한다.

Q. type했는데 value가 안 바뀌어.
A. controlled component에서 부모 state wrapper가 없을 수 있다.

Q. Component Test에서 가장 흔한 실수는 뭐야?
A. 내부 state를 테스트하거나 userEvent await를 누락하거나 비동기 UI에 getBy를 사용하는 것이다.

Q. snapshot-only Component Test는 왜 문제야?
A. 사용자 행동과 결과를 명확히 검증하지 못하고 의미 없는 변경에도 쉽게 깨질 수 있다.

Q. Component Test Checklist의 핵심은 뭐야?
A. 사용자 관점 Query, userEvent, 화면 결과 검증, 조건부 상태 검증이다.

Q. Part06 Component Test의 최종 목표는 뭐야?
A. Frontend Agent가 React Component를 사용자 관점으로 렌더링, 상호작용, 상태 UI까지 검증하게 만드는 것이다.
