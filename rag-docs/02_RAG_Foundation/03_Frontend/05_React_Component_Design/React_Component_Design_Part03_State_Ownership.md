# React Component Design Part03 - State Ownership

---

# 1. State Ownership

## 1.1 State Ownership Definition

### [개념]

State Ownership은 React Component Tree에서 어떤 Component가 특정 State를 소유하고 변경 책임을 가질지 결정하는 설계 기준이다.

State는 단순히 `useState`를 어디에 작성할지의 문제가 아니다.

State Ownership은 Component Responsibility, Component Boundary, Props Design, Callback Props 흐름을 연결하는 핵심 기준이다.

State Owner는 해당 State의 원본 값을 보유하고, 하위 Component는 Props와 Callback Props를 통해 State를 읽거나 변경 요청을 전달한다.

---

### [핵심]

- State Ownership은 State의 소유자를 결정하는 기준이다.
- State는 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.
- Local State는 해당 Component 내부에 둔다.
- Shared State는 공통 부모에 둔다.
- Page State는 Page Component가 소유할 수 있다.
- UI Component는 서버 데이터 State를 직접 소유하지 않는 것이 좋다.
- State Owner가 명확해야 Props 흐름이 단순해진다.
- State Owner가 잘못되면 Props Drilling이 발생한다.
- State를 너무 위로 올리면 불필요한 Props 전달이 증가한다.
- State를 너무 아래에 두면 형제 Component가 공유하기 어렵다.
- 모든 State를 전역 상태로 만들지 않는다.

---

### [실무]

2026 실무 기준에서 State Ownership은 React Component 설계의 중심 기준이다.

State 위치 결정 질문:

```text
이 State를 읽는 Component는 어디인가?
이 State를 변경하는 Component는 어디인가?
이 State를 공유하는 Component들은 어디인가?
가장 가까운 공통 부모는 어디인가?
이 State는 URL과 동기화되어야 하는가?
이 State는 서버 데이터인가 UI 상태인가?
이 State는 여러 페이지에서 필요한가?
```

기본 Flow:

```text
Identify State
→ Find Components That Read State
→ Find Components That Change State
→ Find Closest Common Parent
→ Place State There
→ Pass Data Down
→ Pass Callback Down
```

예:

```tsx
function FestivalPage() {
  const [keyword, setKeyword] = useState("");

  return (
    <>
      <FestivalSearchForm onSearch={setKeyword} />
      <FestivalList keyword={keyword} />
    </>
  );
}
```

판단:

```text
keyword는 FestivalSearchForm에서 변경된다.
keyword는 FestivalList 데이터 조회 또는 필터링에 사용된다.
FestivalSearchForm과 FestivalList의 공통 부모는 FestivalPage다.
따라서 keyword State Owner는 FestivalPage다.
```

---

### [FAQ]

Q. State Ownership이 뭐야?
A. 어떤 Component가 특정 State를 소유하고 변경 책임을 가질지 결정하는 기준이다.

Q. State는 어디에 둬야 해?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. State Owner가 왜 중요해?
A. State Owner가 명확해야 Props 흐름, Callback Props, Component Boundary가 안정적으로 설계된다.

Q. 모든 State를 Page에 두면 안 돼?
A. 권장하지 않는다. Page가 너무 많은 State를 소유하면 Overgrown Component가 될 수 있다.

---

## 1.2 State Ownership Decision Rules

### [개념]

State Ownership Decision Rules는 State를 어디에 배치할지 판단하기 위한 규칙이다.

State는 사용 범위, 변경 위치, 공유 여부, 지속성, URL 동기화 여부, 서버 데이터 여부에 따라 위치가 달라진다.

---

### [핵심]

State 위치 결정 기준:

- 한 Component 내부에서만 사용하면 Local State
- 형제 Component가 공유하면 공통 부모 State
- Page 전체 데이터 흐름이면 Page State
- 반복되는 API 상태 로직이면 Custom Hook State
- 여러 페이지에서 공유하면 Context 또는 전역 상태 검토
- URL에 남아야 하면 URL State 검토
- 서버 데이터는 Server State로 구분
- Form 임시 입력값은 Form State로 관리 가능
- UI 열림/닫힘은 가까운 Component에 배치
- 로그인 사용자 정보는 전역 또는 Context 후보

---

### [실무]

State Ownership Decision Flow:

```text
Is state used by only one component?
→ Keep Local State

Is state shared by sibling components?
→ Lift State Up to Closest Common Parent

Is state page-level data?
→ Keep in Page or Page Hook

Is state server data?
→ Use API Hook or Server State Layer

Is state needed across many pages?
→ Consider Context or Global State

Should state be reflected in URL?
→ Use URL Search Params or Route Params
```

State 분류 예:

| State              | Owner 후보                     | 설명                       |
| ------------------ | ------------------------------ | -------------------------- |
| input focus        | Input Component                | Local UI State             |
| modal open         | Modal Owner Component          | Local 또는 Page UI State   |
| search keyword     | Search Page                    | 목록 조회와 공유           |
| selectedFestivalId | FestivalPage 또는 FestivalList | 선택 상태 공유 범위 기준   |
| login user         | Auth Context / Global State    | 여러 페이지에서 필요       |
| API list data      | Page Hook / Server State Layer | 서버 데이터                |
| pagination page    | Page 또는 URL                  | 공유 및 URL 복원 여부 기준 |
| form values        | Form Component                 | 제출 전 임시 상태          |

---

### [FAQ]

Q. State 위치는 어떤 기준으로 결정해?
A. State를 읽는 Component, 변경하는 Component, 공유 범위, URL 동기화 여부, 서버 데이터 여부를 기준으로 결정한다.

Q. 한 Component 안에서만 쓰는 State는 어디에 둬?
A. 해당 Component 내부 Local State로 둔다.

Q. 여러 형제 Component가 같은 State를 쓰면 어떻게 해?
A. 가장 가까운 공통 부모로 State를 올린다.

Q. 여러 페이지에서 쓰는 State는 어떻게 해?
A. Context 또는 전역 상태를 검토한다. 단, 너무 빨리 전역 상태로 올리지 않는다.

---

# 2. Local State

## 2.1 Local State Rules

### [개념]

Local State는 특정 Component 내부에서만 읽고 변경되는 State다.

Local State는 외부 Component가 알 필요 없는 UI 상태나 임시 입력 상태에 적합하다.

---

### [핵심]

Local State 적합 대상:

- input value
- dropdown open
- modal internal step
- hover-like UI state
- tab internal selection
- accordion open
- form draft values
- local validation message
- temporary preview
- focus state

Local State 원칙:

- 가능한 State는 사용하는 곳 가까이에 둔다.
- 외부 Component가 필요로 하지 않으면 올리지 않는다.
- 공유 필요성이 생기면 Lifting State Up을 검토한다.
- Local State를 전역 상태로 만들지 않는다.
- UI Component는 Local UI State를 가질 수 있다.

---

### [실무]

Dropdown Local State 예:

```tsx
function Dropdown({ label, children }: DropdownProps) {
  const [isOpen, setIsOpen] = useState(false);

  function handleToggle() {
    setIsOpen((prev) => !prev);
  }

  return (
    <div>
      <button type="button" aria-expanded={isOpen} onClick={handleToggle}>
        {label}
      </button>
      {isOpen && <div>{children}</div>}
    </div>
  );
}
```

판단:

```text
isOpen은 Dropdown 내부 표시 여부에만 사용된다.
외부 Component가 isOpen을 알 필요가 없다.
따라서 Dropdown이 Local State로 소유한다.
```

Form Local State 예:

```tsx
function ReviewForm({ onSubmit }: ReviewFormProps) {
  const [content, setContent] = useState("");
  const [rating, setRating] = useState(5);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSubmit({ content, rating });
  }

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={content}
        onChange={(event) => setContent(event.target.value)}
      />
      <button type="submit">리뷰 등록</button>
    </form>
  );
}
```

판단:

```text
content와 rating은 제출 전 ReviewForm 내부 임시값이다.
부모는 최종 submit 결과만 필요하다.
따라서 ReviewForm이 Local State로 소유한다.
```

---

### [FAQ]

Q. Local State가 뭐야?
A. 특정 Component 내부에서만 필요한 State다.

Q. Local State는 어디에 둬야 해?
A. 해당 State를 실제로 사용하는 Component 내부에 둔다.

Q. UI Component가 State를 가져도 돼?
A. 가능하다. dropdown open, accordion open 같은 Local UI State는 UI Component가 가질 수 있다.

Q. Form 입력값은 Local State로 둬도 돼?
A. Form 내부에서만 필요하고 submit 결과만 부모에게 전달하면 Local State로 두는 것이 적절하다.

---

## 2.2 Local State Caution

### [개념]

Local State Caution은 Local State를 잘못 배치했을 때 생기는 문제를 방지하기 위한 규칙이다.

Local State가 외부 Component와 공유되어야 하는데 내부에 갇혀 있으면 데이터 흐름이 막힌다.

---

### [핵심]

주의 상황:

- 형제 Component가 Local State 값을 필요로 함
- 부모가 자식의 선택 상태를 알아야 함
- 검색어가 목록 조회에 필요함
- Form 값이 Preview에 필요함
- Modal open 상태를 Page에서 제어해야 함
- URL과 동기화되어야 하는 값을 Local State로만 관리함

문제:

- 형제 Component와 공유 불가
- 상태 동기화 어려움
- 중복 State 생성
- Derived State 증가
- Callback 흐름 복잡화
- 테스트 어려움

---

### [실무]

나쁜 예:

```tsx
function SearchForm() {
  const [keyword, setKeyword] = useState("");

  return (
    <input
      value={keyword}
      onChange={(event) => setKeyword(event.target.value)}
    />
  );
}

function FestivalPage() {
  return (
    <>
      <SearchForm />
      <FestivalList />
    </>
  );
}
```

문제:

```text
keyword가 SearchForm 안에 갇혀 있다.
FestivalList가 keyword를 사용할 수 없다.
검색어 기반 목록 조회가 어렵다.
```

개선:

```tsx
function FestivalPage() {
  const [keyword, setKeyword] = useState("");

  return (
    <>
      <SearchForm keyword={keyword} onKeywordChange={setKeyword} />
      <FestivalList keyword={keyword} />
    </>
  );
}
```

또는 submit 방식:

```tsx
function FestivalPage() {
  const [keyword, setKeyword] = useState("");

  return (
    <>
      <SearchForm onSearch={setKeyword} />
      <FestivalList keyword={keyword} />
    </>
  );
}
```

---

### [FAQ]

Q. Local State가 문제가 되는 경우는 언제야?
A. 다른 Component가 그 State를 필요로 하는데 특정 Component 내부에 갇혀 있을 때 문제가 된다.

Q. 검색어 State는 Form 내부에 두면 안 돼?
A. 검색어가 목록 조회에 필요하면 Page나 공통 부모로 올리는 것이 좋다. Form 내부 임시 입력값은 Local State로 둘 수 있다.

Q. Local State를 부모로 올리는 기준은 뭐야?
A. 다른 Component가 읽거나 변경 결과를 공유해야 할 때 올린다.

Q. Local State와 Shared State를 어떻게 구분해?
A. 한 Component 내부에서만 쓰면 Local State, 여러 Component가 함께 쓰면 Shared State다.

---

# 3. Shared State

## 3.1 Shared State Rules

### [개념]

Shared State는 여러 Component가 함께 읽거나 변경 결과를 공유해야 하는 State다.

Shared State는 해당 State를 사용하는 Component들의 가장 가까운 공통 부모가 소유하는 것이 기본이다.

---

### [핵심]

Shared State 적합 대상:

- selected item
- search keyword
- filter values
- pagination page
- active tab shared by sections
- form value and preview
- list selection
- modal target id
- sort condition

Shared State 원칙:

- 가장 가까운 공통 부모가 소유한다.
- 필요한 Component에는 Props로 전달한다.
- 변경 이벤트는 Callback Props로 전달한다.
- 너무 높은 Component에 배치하지 않는다.
- 너무 낮은 Component에 배치하지 않는다.
- 공유 범위가 넓어지면 Context 또는 전역 상태를 검토한다.

---

### [실무]

Shared State 예:

```tsx
function FestivalPage() {
  const [selectedFestivalId, setSelectedFestivalId] = useState<number | null>(
    null,
  );

  return (
    <>
      <FestivalList
        selectedFestivalId={selectedFestivalId}
        onSelectFestival={setSelectedFestivalId}
      />
      <FestivalDetailPanel festivalId={selectedFestivalId} />
    </>
  );
}
```

판단:

```text
selectedFestivalId는 FestivalList에서 변경된다.
selectedFestivalId는 FestivalDetailPanel에서 사용된다.
두 Component의 공통 부모는 FestivalPage다.
따라서 FestivalPage가 selectedFestivalId를 소유한다.
```

Callback Props 흐름:

```text
FestivalCard click
→ onSelectFestival(festivalId)
→ FestivalPage updates selectedFestivalId
→ FestivalDetailPanel receives festivalId
```

---

### [FAQ]

Q. Shared State가 뭐야?
A. 여러 Component가 함께 읽거나 변경 결과를 공유해야 하는 State다.

Q. Shared State는 어디에 둬야 해?
A. 해당 State를 사용하는 Component들의 가장 가까운 공통 부모에 둔다.

Q. Shared State를 너무 위에 두면 뭐가 문제야?
A. 불필요한 Props 전달과 Re-render 범위가 커지고 Page 또는 App이 과도한 책임을 갖게 된다.

Q. Shared State를 너무 아래에 두면 뭐가 문제야?
A. 형제 Component가 State를 공유하기 어렵고 중복 State가 생길 수 있다.

---

## 3.2 Lifting State Up Rules

### [개념]

Lifting State Up은 여러 Component가 같은 State를 공유해야 할 때 State를 공통 부모로 올리는 React 설계 패턴이다.

자식 Component 내부에 있던 State를 부모로 이동시키고, 자식은 Props와 Callback Props를 통해 State를 사용한다.

---

### [핵심]

Lifting State Up 사용 상황:

- 형제 Component가 같은 값 필요
- 한 Component 입력이 다른 Component에 영향
- 부모가 자식 선택 결과를 알아야 함
- 검색 조건이 목록 데이터에 영향
- Form과 Preview가 같은 데이터 사용
- List 선택이 Detail 영역에 영향
- Modal open 대상 id를 Page가 알아야 함

Lifting State Up 원칙:

- 공유가 필요한 순간에만 올린다.
- 가장 가까운 공통 부모까지만 올린다.
- 너무 일찍 전역 상태로 만들지 않는다.
- 자식은 Callback Props로 변경 요청을 전달한다.
- 부모는 State 변경과 후속 처리를 담당한다.

---

### [실무]

Lifting State Up 전:

```tsx
function FestivalSearchForm() {
  const [keyword, setKeyword] = useState("");

  return (
    <input
      value={keyword}
      onChange={(event) => setKeyword(event.target.value)}
    />
  );
}

function FestivalList() {
  return <section>{/* keyword 기반 목록 필요 */}</section>;
}
```

문제:

```text
FestivalList가 keyword를 필요로 하지만 SearchForm 내부 State에 접근할 수 없다.
```

Lifting State Up 후:

```tsx
function FestivalPage() {
  const [keyword, setKeyword] = useState("");

  return (
    <>
      <FestivalSearchForm keyword={keyword} onKeywordChange={setKeyword} />
      <FestivalList keyword={keyword} />
    </>
  );
}
```

Submit 방식:

```tsx
function FestivalSearchForm({ onSearch }: SearchFormProps) {
  const [draftKeyword, setDraftKeyword] = useState("");

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    onSearch(draftKeyword.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={draftKeyword}
        onChange={(event) => setDraftKeyword(event.target.value)}
      />
      <button type="submit">검색</button>
    </form>
  );
}
```

권장 판단:

```text
실시간 검색
→ keyword를 Page에서 제어 가능

submit 검색
→ draftKeyword는 Form Local State
→ submittedKeyword는 Page Shared State
```

---

### [FAQ]

Q. Lifting State Up이 뭐야?
A. 여러 Component가 같은 State를 공유해야 할 때 State를 공통 부모로 올리는 패턴이다.

Q. Lifting State Up은 언제 해?
A. 여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 어디까지 올려야 해?
A. 필요한 Component들의 가장 가까운 공통 부모까지만 올리는 것이 기본이다.

Q. Lifting State Up을 하면 Props가 많아지지 않아?
A. 그럴 수 있다. Props 전달이 깊어지면 Component 구조, Context, 전역 상태를 검토한다.

---

# 4. Page State and Feature State

## 4.1 Page State Rules

### [개념]

Page State는 라우트나 화면 단위에서 필요한 State다.

Page Component는 화면 조립, 주요 데이터 흐름, 검색 조건, 필터, Pagination, loading, error, empty 상태를 소유할 수 있다.

---

### [핵심]

Page State 후보:

- page-level API data
- loading
- error
- empty
- search keyword
- filters
- sort
- pagination
- selected item id
- modal target id
- URL parameter derived state

Page State 원칙:

- 화면 전체 데이터 흐름을 관리할 수 있다.
- Feature Component에 필요한 Props를 전달한다.
- Feature Component 이벤트를 Callback Props로 받는다.
- API 로직이 길어지면 Custom Hook으로 분리한다.
- Page에 모든 UI State를 몰아넣지 않는다.
- Feature 내부에서만 필요한 State는 Feature가 소유할 수 있다.

---

### [실무]

Page State 예:

```tsx
function FestivalSearchPage() {
  const [keyword, setKeyword] = useState("");
  const [filters, setFilters] = useState<FestivalFilters>({
    region: "",
    theme: "",
  });
  const [page, setPage] = useState(1);

  const { festivals, loading, error } = useFestivalSearch({
    keyword,
    filters,
    page,
  });

  return (
    <main>
      <FestivalSearchForm onSearch={setKeyword} />
      <FestivalFilterPanel filters={filters} onChangeFilters={setFilters} />
      <FestivalList festivals={festivals} loading={loading} error={error} />
      <Pagination page={page} onChangePage={setPage} />
    </main>
  );
}
```

판단:

```text
keyword, filters, page는 API 조회 조건이다.
festivals, loading, error는 화면 전체 목록 상태다.
FestivalSearchPage가 Page State로 관리한다.
API 상태 로직은 useFestivalSearch Custom Hook으로 분리한다.
```

---

### [FAQ]

Q. Page State가 뭐야?
A. 라우트나 화면 단위에서 필요한 State다.

Q. Page Component는 어떤 State를 가질 수 있어?
A. 검색 조건, 필터, 페이지 번호, 선택 항목, API loading/error/data 같은 화면 단위 State를 가질 수 있다.

Q. Page에 State가 많아지면 어떻게 해?
A. API 상태 로직은 Custom Hook으로 분리하고, 독립 Feature 내부 State는 Feature Component로 내린다.

Q. Page State와 전역 상태는 뭐가 달라?
A. Page State는 특정 화면 안에서만 필요하고 전역 상태는 여러 페이지에서 반복적으로 필요하다.

---

## 4.2 Feature State Rules

### [개념]

Feature State는 특정 도메인 기능 Component 내부에서 필요한 State다.

Feature Component는 SearchForm, ReviewForm, FilterPanel, ChatInput 같은 기능 단위에서 Local State 또는 부분 Shared State를 소유할 수 있다.

---

### [핵심]

Feature State 후보:

- Form draft value
- validation error
- temporary selected option
- local filter open state
- chat input text
- review rating draft
- editor content
- internal step
- upload preview
- temporary tab

Feature State 원칙:

- Feature 내부에서만 필요하면 Feature가 소유한다.
- 부모가 최종 결과만 필요하면 Callback Props로 전달한다.
- 외부 목록 조회 조건이 되면 Page로 올린다.
- Feature가 너무 많은 State를 가지면 하위 Component 또는 Custom Hook 분리 검토
- Form 상태가 복잡하면 Form Hook 또는 Form Library 검토

---

### [실무]

Feature State 예:

```tsx
function ReviewForm({ onSubmit }: ReviewFormProps) {
  const [rating, setRating] = useState(5);
  const [content, setContent] = useState("");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!content.trim()) {
      setErrorMessage("리뷰 내용을 입력해야 합니다.");
      return;
    }

    onSubmit({ rating, content: content.trim() });
  }

  return (
    <form onSubmit={handleSubmit}>
      <RatingInput value={rating} onChange={setRating} />
      <textarea
        value={content}
        onChange={(event) => setContent(event.target.value)}
      />
      {errorMessage && <p>{errorMessage}</p>}
      <button type="submit">등록</button>
    </form>
  );
}
```

판단:

```text
rating, content, errorMessage는 ReviewForm 내부 작성 중에만 필요하다.
부모는 최종 submit values만 필요하다.
따라서 ReviewForm이 Feature State로 소유한다.
```

---

### [FAQ]

Q. Feature State가 뭐야?
A. 특정 도메인 기능 Component 내부에서 필요한 State다.

Q. ReviewForm 입력값은 어디에 둬?
A. 부모가 실시간으로 필요하지 않으면 ReviewForm 내부 Feature State로 둔다.

Q. Feature State를 Page로 올려야 하는 경우는 언제야?
A. 다른 Component가 그 값을 읽거나 목록 조회, URL 동기화, 화면 전체 흐름에 영향을 줄 때 올린다.

Q. Feature Component에 State가 많아지면 어떻게 해?
A. 하위 Component 분리, Custom Hook 분리, Form Hook 도입을 검토한다.

---

# 5. Server State and UI State

## 5.1 Server State vs UI State

### [개념]

Server State는 서버에서 가져오고 서버와 동기화되어야 하는 데이터 상태다.

UI State는 화면 표시와 사용자 상호작용을 위해 클라이언트에서 관리하는 상태다.

React Component Design에서는 Server State와 UI State를 구분해야 State Ownership과 API Logic Separation이 명확해진다.

---

### [핵심]

Server State 예:

- festival list
- festival detail
- user profile
- review list
- notification list
- chat message history
- API loading
- API error
- pagination response
- server cache data

UI State 예:

- modal open
- dropdown open
- selected tab
- input draft
- local validation message
- hover-like state
- accordion open
- current form step

구분 원칙:

- Server State는 API Hook 또는 Data Fetching 계층에서 관리한다.
- UI State는 가까운 Component에서 관리한다.
- Server State와 UI State를 같은 State로 섞지 않는다.
- API Response를 표시용 ViewModel로 mapping할 수 있다.
- loading/error/data는 같은 API 흐름에서 함께 관리한다.

---

### [실무]

나쁜 예:

```tsx
function FestivalPage() {
  const [state, setState] = useState({
    festivals: [],
    isModalOpen: false,
    selectedTab: "list",
    loading: false,
    error: null,
  });

  return null;
}
```

문제:

```text
Server State와 UI State가 하나의 객체에 섞여 있다.
업데이트 목적이 다르다.
State 변경 추적이 어려워진다.
```

개선:

```tsx
function FestivalPage() {
  const { festivals, loading, error } = useFestivals();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedTab, setSelectedTab] = useState<"list" | "map">("list");

  return null;
}
```

구분:

```text
useFestivals
- Server State 관리

FestivalPage Local State
- Modal open
- selectedTab
```

---

### [FAQ]

Q. Server State가 뭐야?
A. 서버에서 가져오고 서버와 동기화되어야 하는 데이터 상태다.

Q. UI State가 뭐야?
A. 화면 표시와 사용자 상호작용을 위해 클라이언트에서만 필요한 상태다.

Q. Server State와 UI State를 왜 구분해?
A. 변경 원인과 소유 위치가 다르기 때문에 구분해야 유지보수와 API 로직 분리가 쉬워진다.

Q. loading과 error는 Server State야?
A. API 요청 흐름에 포함되는 loading과 error는 Server State 관리 로직에 포함되는 경우가 많다.

---

## 5.2 API State Ownership

### [개념]

API State Ownership은 API 요청 결과, loading, error, refetch 상태를 어디에서 관리할지 결정하는 기준이다.

API State는 Page Component, Container Component, Custom Hook, Server State Library 계층에서 관리할 수 있다.

---

### [핵심]

API State 구성:

- data
- loading
- error
- refetch
- pagination
- hasNext
- query parameter
- request status

API State Owner 후보:

- Page Component
- Container Component
- Custom Hook
- Data Fetching Library
- Server State Layer

API State 원칙:

- 간단한 화면은 Page에서 관리 가능하다.
- 반복되는 API 패턴은 Custom Hook으로 분리한다.
- UI Component에서 API 호출을 직접 수행하지 않는다.
- API 함수는 api 파일로 분리한다.
- Response Mapping은 Hook 또는 Mapper에서 처리 가능하다.
- Server State와 UI State를 섞지 않는다.

---

### [실무]

Custom Hook API State 예:

```tsx
function useFestivalDetail(festivalId: number | null) {
  const [festival, setFestival] = useState<FestivalDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!festivalId) {
      return;
    }

    setLoading(true);
    getFestivalDetail(festivalId)
      .then(setFestival)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [festivalId]);

  return { festival, loading, error };
}
```

Page 사용:

```tsx
function FestivalDetailPage({ festivalId }: FestivalDetailPageProps) {
  const { festival, loading, error } = useFestivalDetail(festivalId);

  if (loading) {
    return <LoadingView />;
  }

  if (error) {
    return <ErrorMessage message="축제 상세 정보를 불러오지 못했습니다." />;
  }

  return <FestivalDetail festival={festival} />;
}
```

---

### [FAQ]

Q. API State는 어디에서 관리해?
A. 간단하면 Page에서 관리하고 반복되거나 복잡하면 Custom Hook 또는 Data Fetching 계층으로 분리한다.

Q. UI Component에서 API 호출하면 안 돼?
A. 권장하지 않는다. UI Component가 서버 구조에 의존해 재사용성과 테스트 가능성이 떨어진다.

Q. API loading과 error는 어디에 둬?
A. API 요청을 관리하는 Page, Container, Custom Hook, Server State Layer에서 data와 함께 관리하는 것이 좋다.

Q. API State를 Custom Hook으로 분리하는 기준은 뭐야?
A. API 요청 로직이 반복되거나 loading/error/refetch 패턴이 길어질 때 분리한다.

---

# 6. Derived State

## 6.1 Derived State Avoidance

### [개념]

Derived State는 기존 Props나 State에서 계산할 수 있는 값을 별도 State로 저장한 값이다.

계산 가능한 값을 불필요하게 State로 저장하면 중복 상태가 생기고 동기화 문제가 발생할 수 있다.

---

### [핵심]

Derived State 주의 대상:

- filtered list
- sorted list
- total count
- selected item object
- formatted text
- validation result
- computed status
- display label

원칙:

- 기존 State에서 계산 가능하면 State로 저장하지 않는다.
- 렌더링 중 계산하거나 `useMemo`를 검토한다.
- 원본 State는 하나로 유지한다.
- 중복 State는 동기화 오류를 만든다.
- 성능 문제가 실제로 있을 때 memoization을 검토한다.

---

### [실무]

나쁜 예:

```tsx
function FestivalPage() {
  const [festivals, setFestivals] = useState<Festival[]>([]);
  const [keyword, setKeyword] = useState("");
  const [filteredFestivals, setFilteredFestivals] = useState<Festival[]>([]);

  useEffect(() => {
    setFilteredFestivals(
      festivals.filter((festival) => festival.title.includes(keyword)),
    );
  }, [festivals, keyword]);

  return null;
}
```

문제:

```text
filteredFestivals는 festivals와 keyword로 계산 가능하다.
별도 State로 저장하면 동기화 오류 가능성이 생긴다.
```

개선:

```tsx
function FestivalPage() {
  const [festivals, setFestivals] = useState<Festival[]>([]);
  const [keyword, setKeyword] = useState("");

  const filteredFestivals = festivals.filter((festival) =>
    festival.title.includes(keyword),
  );

  return <FestivalList festivals={filteredFestivals} />;
}
```

성능 필요 시:

```tsx
const filteredFestivals = useMemo(
  () => festivals.filter((festival) => festival.title.includes(keyword)),
  [festivals, keyword],
);
```

---

### [FAQ]

Q. Derived State가 뭐야?
A. 기존 Props나 State에서 계산할 수 있는 값을 별도 State로 저장한 값이다.

Q. Derived State는 왜 주의해야 해?
A. 원본 State와 계산된 State가 서로 어긋나는 동기화 문제가 생길 수 있기 때문이다.

Q. filtered list를 State로 저장해도 돼?
A. 대부분은 원본 list와 filter 조건으로 계산하는 것이 좋다. 성능 문제가 있으면 useMemo를 검토한다.

Q. useMemo는 언제 써?
A. 계산 비용이 크거나 불필요한 재계산이 실제 문제가 될 때 사용한다.

---

## 6.2 Selected Item Derived State

### [개념]

Selected Item Derived State는 선택된 ID와 목록 데이터에서 계산할 수 있는 선택 객체를 별도 State로 저장하는 문제다.

선택 상태는 가능하면 원본 ID를 State로 관리하고, 선택 객체는 목록에서 계산하는 방식이 안정적이다.

---

### [핵심]

주의 상황:

- selectedId와 selectedItem을 둘 다 State로 저장
- list 변경 시 selectedItem이 오래된 데이터가 됨
- 서버 재조회 후 선택 객체 동기화 실패
- ID와 객체가 서로 다른 값을 가짐
- 수정 후 목록과 상세가 어긋남

원칙:

- 원본 선택 상태는 ID로 관리한다.
- 객체는 list 또는 detail API에서 가져온다.
- 계산 가능한 selectedItem은 Derived Value로 둔다.
- 상세 데이터가 필요하면 별도 detail API State로 관리한다.

---

### [실무]

나쁜 예:

```tsx
function FestivalPage() {
  const [festivals, setFestivals] = useState<Festival[]>([]);
  const [selectedFestivalId, setSelectedFestivalId] = useState<number | null>(
    null,
  );
  const [selectedFestival, setSelectedFestival] = useState<Festival | null>(
    null,
  );

  function handleSelect(festival: Festival) {
    setSelectedFestivalId(festival.festivalId);
    setSelectedFestival(festival);
  }

  return null;
}
```

문제:

```text
selectedFestivalId와 selectedFestival이 중복 State다.
festivals가 갱신되면 selectedFestival이 오래된 객체가 될 수 있다.
```

개선:

```tsx
function FestivalPage() {
  const [festivals, setFestivals] = useState<Festival[]>([]);
  const [selectedFestivalId, setSelectedFestivalId] = useState<number | null>(
    null,
  );

  const selectedFestival =
    festivals.find((festival) => festival.festivalId === selectedFestivalId) ??
    null;

  return <FestivalDetailPanel festival={selectedFestival} />;
}
```

상세 API가 필요한 경우:

```tsx
const { festivalDetail, loading, error } =
  useFestivalDetail(selectedFestivalId);
```

---

### [FAQ]

Q. selectedId와 selectedItem을 둘 다 State로 저장해도 돼?
A. 가능은 하지만 중복 State가 되어 동기화 문제가 생길 수 있다. 보통 selectedId만 State로 두고 selectedItem은 계산한다.

Q. 선택된 객체는 어떻게 관리하는 게 좋아?
A. selectedId를 State로 관리하고 목록에서 find로 계산하거나 상세 API Hook으로 가져오는 방식이 좋다.

Q. selectedItem이 오래된 데이터가 되는 이유는?
A. 목록 데이터가 갱신되어도 별도 저장된 selectedItem 객체는 자동으로 바뀌지 않기 때문이다.

Q. 상세 정보가 목록보다 많으면 어떻게 해?
A. selectedId를 기준으로 detail API를 호출하고 상세 데이터는 별도 Server State로 관리한다.

---

# 7. Controlled and Uncontrolled State

## 7.1 Controlled Component State

### [개념]

Controlled Component는 value와 onChange를 부모 또는 외부 State Owner가 제어하는 Component다.

Controlled Component는 입력값, 선택값, 열림 상태 등을 외부에서 명시적으로 제어해야 할 때 사용한다.

---

### [핵심]

Controlled Component 특징:

- value를 Props로 받는다.
- onChange Callback Props로 변경을 알린다.
- State Owner가 외부에 있다.
- 부모가 현재 값을 제어한다.
- Form, Input, Select, Modal open 제어에 자주 사용한다.
- 외부 동기화가 쉽다.
- Props 설계가 명확해야 한다.

---

### [실무]

Input Controlled 예:

```tsx
type TextInputProps = {
  value: string;
  onValueChange: (value: string) => void;
};

function TextInput({ value, onValueChange }: TextInputProps) {
  return (
    <input
      value={value}
      onChange={(event) => onValueChange(event.target.value)}
    />
  );
}
```

부모 사용:

```tsx
function SearchForm() {
  const [keyword, setKeyword] = useState("");

  return <TextInput value={keyword} onValueChange={setKeyword} />;
}
```

Modal Controlled 예:

```tsx
type ModalProps = {
  isOpen: boolean;
  onClose: () => void;
  children: React.ReactNode;
};

function Modal({ isOpen, onClose, children }: ModalProps) {
  if (!isOpen) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true">
      {children}
      <button type="button" onClick={onClose}>
        닫기
      </button>
    </section>
  );
}
```

---

### [FAQ]

Q. Controlled Component가 뭐야?
A. value와 onChange를 외부 State Owner가 제어하는 Component다.

Q. Controlled Component는 언제 써?
A. 입력값이나 열림 상태를 부모가 제어해야 하거나 다른 Component와 동기화해야 할 때 사용한다.

Q. Controlled Input의 기본 Props는 뭐야?
A. 일반적으로 value와 onChange 또는 onValueChange를 받는다.

Q. Modal도 Controlled Component가 될 수 있어?
A. 가능하다. isOpen과 onClose를 Props로 받아 부모가 열림 상태를 제어하게 만들 수 있다.

---

## 7.2 Uncontrolled Component Basics

### [개념]

Uncontrolled Component는 내부 DOM 상태나 ref를 통해 값을 관리하는 Component다.

React State로 모든 입력값을 제어하지 않고, 필요한 시점에 값을 읽는 방식이다.

---

### [핵심]

Uncontrolled Component 특징:

- value State를 React가 직접 소유하지 않는다.
- defaultValue를 사용할 수 있다.
- ref로 값을 읽을 수 있다.
- 간단한 Form에서 사용 가능하다.
- 외부 동기화가 필요한 경우에는 부적합하다.
- 복잡한 validation이나 실시간 UI 반영에는 Controlled 방식이 더 적합하다.

---

### [실무]

Uncontrolled Input 예:

```tsx
function SimpleSearchForm({ onSearch }: SimpleSearchFormProps) {
  const inputRef = useRef<HTMLInputElement | null>(null);

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const keyword = inputRef.current?.value.trim() ?? "";
    onSearch(keyword);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} defaultValue="" />
      <button type="submit">검색</button>
    </form>
  );
}
```

적합:

```text
- submit 시점에만 값이 필요
- 실시간 validation이 없음
- 외부 상태와 동기화 필요 없음
- 간단한 입력 Form
```

부적합:

```text
- 입력값에 따라 실시간 목록 필터링
- 입력값 Preview 표시
- 복잡한 validation
- 외부 reset 제어
- 여러 Component가 값 공유
```

---

### [FAQ]

Q. Uncontrolled Component가 뭐야?
A. 입력값을 React State로 직접 관리하지 않고 DOM 상태나 ref로 필요한 시점에 읽는 Component다.

Q. Uncontrolled Component는 언제 써?
A. submit 시점에만 값이 필요하고 외부 동기화가 필요 없는 간단한 Form에서 사용할 수 있다.

Q. Controlled와 Uncontrolled 중 뭐가 좋아?
A. 외부 동기화와 검증이 필요하면 Controlled, 단순 입력이면 Uncontrolled도 가능하다.

Q. 실시간 검색은 Controlled가 좋아?
A. 보통 좋다. 입력값 변경이 목록 조회나 필터링에 바로 영향을 주기 때문이다.

---

# 8. URL State and Global State

## 8.1 URL State Rules

### [개념]

URL State는 검색 조건, 필터, 페이지 번호처럼 URL에 반영되어야 하는 State다.

URL State는 새로고침, 공유 링크, 뒤로가기, 검색 결과 복원에 중요하다.

---

### [핵심]

URL State 후보:

- search keyword
- filters
- sort
- pagination page
- tab
- selected category
- date range
- map location query

URL State 원칙:

- 공유 가능한 화면 조건은 URL에 반영한다.
- 새로고침 후 복원되어야 하면 URL State를 검토한다.
- 검색 결과 페이지는 query string 사용을 검토한다.
- 단순 UI open state는 URL에 넣지 않아도 된다.
- URL 값을 Page State 초기값으로 사용할 수 있다.
- URL과 Local State 이중 관리를 주의한다.

---

### [실무]

URL State 예:

```text
/festivals?keyword=music&region=seoul&page=2
```

적합:

```text
축제 검색어
지역 필터
테마 필터
정렬 조건
페이지 번호
```

부적합 가능성:

```text
Dropdown open 여부
Hover 상태
일시적 Toast open 상태
Form 작성 중 임시값
```

설계 Flow:

```text
Should this state survive refresh?
→ Should this state be shareable as URL?
→ Should browser back restore this state?
→ Use URL Search Params
```

---

### [FAQ]

Q. URL State가 뭐야?
A. 검색 조건, 필터, 페이지 번호처럼 URL에 반영되어야 하는 State다.

Q. 어떤 State를 URL에 넣어야 해?
A. 새로고침 후 복원되어야 하거나 공유 링크로 유지되어야 하는 검색 조건, 필터, 페이지 번호가 후보가 된다.

Q. Modal open 상태도 URL에 넣어야 해?
A. 일반적으로는 필요 없다. 단, 상세 모달을 공유 가능한 상태로 만들려면 URL 설계를 검토할 수 있다.

Q. URL State와 Page State를 같이 쓰면 안 돼?
A. 가능하지만 이중 관리로 동기화 문제가 생기지 않도록 URL을 Source of Truth로 둘지 명확히 정해야 한다.

---

## 8.2 Global State Rules

### [개념]

Global State는 여러 페이지와 깊은 Component Tree에서 반복적으로 필요한 State다.

Global State는 Context, Zustand, Redux 같은 전역 상태 관리 계층에서 관리할 수 있다.

---

### [핵심]

Global State 후보:

- login user
- auth token status
- theme
- locale
- global notification
- app-wide permission
- cart items
- shared workspace
- global modal manager

Global State 비후보:

- 단일 Form 입력값
- 단일 Page 검색 조건
- 단일 Dropdown open
- 단일 Modal 내부 step
- 특정 Feature 내부 임시값
- API Response 전체를 무분별하게 저장

Global State 원칙:

- 여러 페이지에서 반복적으로 필요할 때 사용한다.
- 너무 빨리 전역 상태로 올리지 않는다.
- Page State와 Local State로 충분하면 유지한다.
- 전역 상태는 변경 추적과 의존성 관리 비용이 있다.
- Server State와 Global Client State를 구분한다.

---

### [실무]

전역 상태 검토 Flow:

```text
Is state used across multiple pages?
→ Is props drilling deep and repeated?
→ Is state app-wide concern?
→ Is Context enough?
→ Is global state library needed?
```

전역 상태 적합 예:

```text
로그인 사용자 정보
다크 모드 설정
언어 설정
앱 전체 알림
권한 정보
```

전역 상태 부적합 예:

```text
ReviewForm content
FestivalSearchPage filter
Dropdown open
Pagination page in one screen
Local validation error
```

주의:

```text
모든 State를 전역에 넣으면 초기에는 편하다.
하지만 시간이 지날수록 데이터 흐름 추적이 어렵다.
Component 재사용성과 테스트가 떨어질 수 있다.
```

---

### [FAQ]

Q. Global State는 언제 써?
A. 여러 페이지에서 반복적으로 필요하거나 Props Drilling이 깊고 반복될 때 검토한다.

Q. 모든 State를 전역 상태로 만들면 안 돼?
A. 권장하지 않는다. 변경 추적이 어려워지고 불필요한 의존성이 생긴다.

Q. 로그인 사용자 정보는 Global State 후보야?
A. 그렇다. 여러 페이지와 Component에서 반복적으로 필요하기 때문에 Context 또는 전역 상태 후보가 된다.

Q. 검색 필터는 Global State로 둬야 해?
A. 특정 Page에서만 쓰면 Page State 또는 URL State가 적합하다. 여러 페이지에서 공유될 때만 전역 상태를 검토한다.

---

# 9. State Ownership Anti Patterns

## 9.1 Wrong State Owner Problem

### [개념]

Wrong State Owner Problem은 State가 실제 사용 범위와 맞지 않는 Component에 배치되어 Props 흐름과 Component 구조가 복잡해지는 문제다.

State Owner가 잘못되면 Props Drilling, 중복 State, 불필요한 Re-render, Component 책임 혼합이 발생한다.

---

### [핵심]

문제 유형:

- State가 너무 위에 있음
- State가 너무 아래에 있음
- State가 형제 Component와 공유 불가
- State가 전역으로 과도하게 올라감
- Page가 모든 State를 소유함
- UI Component가 서버 데이터를 직접 소유함
- Derived State를 별도 State로 저장함

결과:

- Props Drilling 증가
- Component Responsibility 불명확
- State 동기화 오류
- API Logic과 UI Logic 혼합
- 테스트 어려움
- 리팩터링 비용 증가

---

### [실무]

State가 너무 위에 있는 예:

```tsx
function App() {
  const [reviewContent, setReviewContent] = useState("");

  return (
    <ReviewPage
      reviewContent={reviewContent}
      onChangeReviewContent={setReviewContent}
    />
  );
}
```

문제:

```text
reviewContent는 ReviewForm 내부 작성 중에만 필요한 값이다.
App이 소유할 이유가 없다.
```

개선:

```tsx
function ReviewForm({ onSubmit }: ReviewFormProps) {
  const [reviewContent, setReviewContent] = useState("");

  return null;
}
```

State가 너무 아래에 있는 예:

```text
SearchForm이 keyword를 소유한다.
FestivalList도 keyword가 필요하다.
→ keyword를 FestivalPage로 올려야 한다.
```

---

### [FAQ]

Q. Wrong State Owner Problem이 뭐야?
A. State가 실제 사용 범위와 맞지 않는 Component에 배치되어 구조가 복잡해지는 문제다.

Q. State가 너무 위에 있으면 뭐가 문제야?
A. 불필요한 Props 전달과 Re-render가 늘고 상위 Component 책임이 과도해진다.

Q. State가 너무 아래에 있으면 뭐가 문제야?
A. 형제 Component나 부모가 필요한 값을 공유하기 어렵다.

Q. Wrong State Owner는 어떻게 찾을 수 있어?
A. State를 읽는 Component와 변경하는 Component를 추적하고 가장 가까운 공통 부모가 맞는지 확인한다.

---

## 9.2 Duplicated State Problem

### [개념]

Duplicated State Problem은 같은 의미의 값을 여러 State로 중복 저장하여 동기화 문제가 생기는 Anti Pattern이다.

중복 State는 React Component Design에서 Derived State 문제와 함께 자주 발생한다.

---

### [핵심]

중복 State 예:

- selectedId와 selectedItem 동시 저장
- 원본 list와 filtered list 동시 저장
- props value를 local state로 복사
- server response와 mapped display state 동시 저장
- form value와 preview value 동시 저장
- total count를 list length와 별도 저장

문제:

- 원본과 복사본이 어긋난다.
- useEffect 동기화 코드가 증가한다.
- 상태 변경 경로가 늘어난다.
- 버그 추적이 어려워진다.
- Component 테스트가 복잡해진다.

---

### [실무]

나쁜 예:

```tsx
function UserProfile({ user }: UserProfileProps) {
  const [localUser, setLocalUser] = useState(user);

  return <p>{localUser.name}</p>;
}
```

문제:

```text
props user가 변경되어도 localUser가 자동으로 동기화되지 않는다.
특별한 편집 목적이 없다면 복사할 필요가 없다.
```

개선:

```tsx
function UserProfile({ user }: UserProfileProps) {
  return <p>{user.name}</p>;
}
```

편집 Form에서 복사가 필요한 경우:

```tsx
function UserEditForm({ user, onSubmit }: UserEditFormProps) {
  const [draftUser, setDraftUser] = useState(() => ({
    name: user.name,
    bio: user.bio,
  }));

  return null;
}
```

판단:

```text
단순 표시
→ Props 직접 사용

편집 초안
→ Local Draft State 가능

계산 가능 값
→ Derived Value로 계산
```

---

### [FAQ]

Q. Duplicated State가 뭐야?
A. 같은 의미의 값을 여러 State로 중복 저장한 상태다.

Q. Props를 Local State로 복사하면 안 돼?
A. 단순 표시 목적이면 권장하지 않는다. 편집 초안처럼 독립 수정 목적이 있을 때만 검토한다.

Q. filtered list를 State로 저장하면 안 돼?
A. 원본 list와 filter 조건으로 계산 가능하면 별도 State로 저장하지 않는 것이 좋다.

Q. 중복 State는 왜 위험해?
A. 원본과 복사본이 어긋나는 동기화 버그가 생기기 때문이다.

---

# 10. State Ownership Review Checklist

## 10.1 State Ownership Checklist

### [개념]

State Ownership Checklist는 React Component 설계에서 State 위치가 적절한지 검수하기 위한 기준이다.

Frontend Agent와 Review Agent는 Component Tree, Props 흐름, Callback Props 흐름을 함께 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 각 State의 목적이 명확한가?
- [ ] State를 읽는 Component가 식별되었는가?
- [ ] State를 변경하는 Component가 식별되었는가?
- [ ] 가장 가까운 공통 부모가 State Owner인가?
- [ ] Local State로 충분한 값을 너무 위로 올리지 않았는가?
- [ ] Shared State가 너무 아래에 있지 않은가?
- [ ] Page State와 Feature State가 구분되는가?
- [ ] Server State와 UI State가 구분되는가?
- [ ] API State가 UI Component에 들어가지 않았는가?
- [ ] Derived State를 불필요하게 저장하지 않았는가?
- [ ] selectedId와 selectedItem을 중복 저장하지 않았는가?
- [ ] Props를 무분별하게 Local State로 복사하지 않았는가?
- [ ] URL에 반영되어야 하는 State를 검토했는가?
- [ ] 전역 상태가 필요한 State인지 검토했는가?
- [ ] 모든 State를 전역 상태로 올리지 않았는가?
- [ ] Props Drilling이 과도하지 않은가?
- [ ] Callback Props 흐름이 명확한가?
```

---

### [실무]

Review Flow:

```text
Component Tree Review
→ State List Up
→ State Reader Check
→ State Writer Check
→ Closest Common Parent Check
→ Local / Shared Classification
→ Server / UI Classification
→ Derived State Check
→ Props Drilling Check
→ Global State Necessity Check
```

치명적 문제:

```text
- UI Component가 API State를 직접 소유
- Page가 모든 Local UI State를 소유
- Form 내부 임시값이 App 전역 상태에 있음
- Shared State가 자식 내부에 갇힘
- 동일 의미 State가 여러 곳에 중복 저장됨
- Derived State를 useEffect로 계속 동기화
- 전역 상태 남용
```

---

### [FAQ]

Q. State Ownership 검수에서 가장 중요한 것은?
A. State를 읽는 Component, 변경하는 Component, 가장 가까운 공통 부모를 확인하는 것이다.

Q. 치명적인 State Ownership 문제는 뭐야?
A. State Owner가 실제 사용 범위와 맞지 않거나 중복 State와 Derived State를 불필요하게 저장하는 것이다.

Q. Review Agent는 State를 어떻게 검토해야 해?
A. State 목록을 만들고 각 State의 Reader, Writer, Owner, 공유 범위를 확인해야 한다.

Q. Props Drilling은 State Ownership 문제야?
A. State 위치가 부적절해서 발생하는 경우가 많다. Component 구조와 State Owner를 함께 검토해야 한다.

---

# 11. Agent Output Rules

## 11.1 Frontend Agent State Ownership Output

### [개념]

Frontend Agent는 Component 코드를 생성하기 전에 State Ownership을 명확히 설계해야 한다.

State Ownership Output은 State 이름, 목적, Owner Component, Reader Component, Writer Component, Props 흐름, Callback 흐름을 포함해야 한다.

---

### [핵심]

Frontend Agent State Ownership 출력 항목:

- State Name
- State Purpose
- State Type
- Owner Component
- Reader Components
- Writer Components
- Props Flow
- Callback Flow
- Local / Shared / Server / URL / Global Classification
- Derived State 여부
- Props Drilling Risk
- Anti Pattern Review

---

### [실무]

출력 예:

```text
State: keyword
Purpose: 축제 검색 조건
Type: Shared Page State
Owner: FestivalSearchPage
Readers:
- FestivalList
- useFestivalSearch

Writers:
- FestivalSearchForm

Props Flow:
FestivalSearchPage → FestivalList(keyword)

Callback Flow:
FestivalSearchForm → onSearch(keyword) → FestivalSearchPage

Review:
- Local State로 두면 FestivalList와 공유 불가
- Global State까지 올릴 필요 없음
- URL Search Params 반영 검토 가능
```

State Table 예:

| State        | Type                  | Owner               | Reader              | Writer              |
| ------------ | --------------------- | ------------------- | ------------------- | ------------------- |
| keyword      | Page State / URL 후보 | FestivalSearchPage  | useFestivalSearch   | FestivalSearchForm  |
| filters      | Page State / URL 후보 | FestivalSearchPage  | useFestivalSearch   | FestivalFilterPanel |
| draftKeyword | Local State           | FestivalSearchForm  | FestivalSearchForm  | FestivalSearchForm  |
| festivals    | Server State          | useFestivalSearch   | FestivalList        | API Hook            |
| isFilterOpen | Local UI State        | FestivalFilterPanel | FestivalFilterPanel | FestivalFilterPanel |

---

### [FAQ]

Q. Frontend Agent는 State를 언제 설계해야 해?
A. Component 코드 생성 전에 Component Responsibility, Props Contract와 함께 State Ownership을 설계해야 한다.

Q. State Ownership Output에는 무엇이 포함돼야 해?
A. State 이름, 목적, Owner, Reader, Writer, Props Flow, Callback Flow, State Type이 포함되어야 한다.

Q. State Type은 어떻게 분류해?
A. Local State, Shared State, Page State, Feature State, Server State, URL State, Global State로 분류한다.

Q. State 설계 없이 코드를 만들면 뭐가 문제야?
A. Props Drilling, 중복 State, 잘못된 State Owner, Derived State 동기화 문제가 발생하기 쉽다.

---

# Retrieval Queries

### [FAQ]

Q. React State Ownership이 뭐야?
A. 어떤 Component가 특정 State를 소유하고 변경 책임을 가질지 결정하는 기준이다.

Q. State는 어디에 둬야 해?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. State Owner가 왜 중요해?
A. State Owner가 명확해야 Props 흐름, Callback Props, Component Boundary가 안정적으로 설계된다.

Q. State 위치는 어떤 기준으로 결정해?
A. State를 읽는 Component, 변경하는 Component, 공유 범위, URL 동기화 여부, 서버 데이터 여부를 기준으로 결정한다.

Q. Local State가 뭐야?
A. 특정 Component 내부에서만 필요한 State다.

Q. Local State는 어디에 둬야 해?
A. 해당 State를 실제로 사용하는 Component 내부에 둔다.

Q. UI Component가 State를 가져도 돼?
A. 가능하다. dropdown open, accordion open 같은 Local UI State는 UI Component가 가질 수 있다.

Q. Form 입력값은 Local State로 둬도 돼?
A. Form 내부에서만 필요하고 submit 결과만 부모에게 전달하면 Local State로 두는 것이 적절하다.

Q. Local State가 문제가 되는 경우는 언제야?
A. 다른 Component가 그 State를 필요로 하는데 특정 Component 내부에 갇혀 있을 때 문제가 된다.

Q. 검색어 State는 Form 내부에 둬도 돼?
A. 검색어가 목록 조회에 필요하면 Page나 공통 부모로 올리는 것이 좋다. Form 내부 임시 입력값은 Local State로 둘 수 있다.

Q. Shared State가 뭐야?
A. 여러 Component가 함께 읽거나 변경 결과를 공유해야 하는 State다.

Q. Shared State는 어디에 둬야 해?
A. 해당 State를 사용하는 Component들의 가장 가까운 공통 부모에 둔다.

Q. Lifting State Up이 뭐야?
A. 여러 Component가 같은 State를 공유해야 할 때 State를 공통 부모로 올리는 패턴이다.

Q. Lifting State Up은 언제 해?
A. 여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 어디까지 올려야 해?
A. 필요한 Component들의 가장 가까운 공통 부모까지만 올리는 것이 기본이다.

Q. Page State가 뭐야?
A. 라우트나 화면 단위에서 필요한 State다.

Q. Page Component는 어떤 State를 가질 수 있어?
A. 검색 조건, 필터, 페이지 번호, 선택 항목, API loading/error/data 같은 화면 단위 State를 가질 수 있다.

Q. Feature State가 뭐야?
A. 특정 도메인 기능 Component 내부에서 필요한 State다.

Q. ReviewForm 입력값은 어디에 둬?
A. 부모가 실시간으로 필요하지 않으면 ReviewForm 내부 Feature State로 둔다.

Q. Server State가 뭐야?
A. 서버에서 가져오고 서버와 동기화되어야 하는 데이터 상태다.

Q. UI State가 뭐야?
A. 화면 표시와 사용자 상호작용을 위해 클라이언트에서만 필요한 상태다.

Q. Server State와 UI State를 왜 구분해?
A. 변경 원인과 소유 위치가 다르기 때문에 구분해야 유지보수와 API 로직 분리가 쉬워진다.

Q. API State는 어디에서 관리해?
A. 간단하면 Page에서 관리하고 반복되거나 복잡하면 Custom Hook 또는 Data Fetching 계층으로 분리한다.

Q. UI Component에서 API 호출하면 안 돼?
A. 권장하지 않는다. UI Component가 서버 구조에 의존해 재사용성과 테스트 가능성이 떨어진다.

Q. Derived State가 뭐야?
A. 기존 Props나 State에서 계산할 수 있는 값을 별도 State로 저장한 값이다.

Q. Derived State는 왜 주의해야 해?
A. 원본 State와 계산된 State가 서로 어긋나는 동기화 문제가 생길 수 있기 때문이다.

Q. filtered list를 State로 저장해도 돼?
A. 대부분은 원본 list와 filter 조건으로 계산하는 것이 좋다. 성능 문제가 있으면 useMemo를 검토한다.

Q. selectedId와 selectedItem을 둘 다 State로 저장해도 돼?
A. 가능은 하지만 중복 State가 되어 동기화 문제가 생길 수 있다. 보통 selectedId만 State로 두고 selectedItem은 계산한다.

Q. Controlled Component가 뭐야?
A. value와 onChange를 외부 State Owner가 제어하는 Component다.

Q. Controlled Component는 언제 써?
A. 입력값이나 열림 상태를 부모가 제어해야 하거나 다른 Component와 동기화해야 할 때 사용한다.

Q. Uncontrolled Component가 뭐야?
A. 입력값을 React State로 직접 관리하지 않고 DOM 상태나 ref로 필요한 시점에 읽는 Component다.

Q. Controlled와 Uncontrolled 중 뭐가 좋아?
A. 외부 동기화와 검증이 필요하면 Controlled, 단순 입력이면 Uncontrolled도 가능하다.

Q. URL State가 뭐야?
A. 검색 조건, 필터, 페이지 번호처럼 URL에 반영되어야 하는 State다.

Q. 어떤 State를 URL에 넣어야 해?
A. 새로고침 후 복원되어야 하거나 공유 링크로 유지되어야 하는 검색 조건, 필터, 페이지 번호가 후보가 된다.

Q. Global State는 언제 써?
A. 여러 페이지에서 반복적으로 필요하거나 Props Drilling이 깊고 반복될 때 검토한다.

Q. 모든 State를 전역 상태로 만들면 안 돼?
A. 권장하지 않는다. 변경 추적이 어려워지고 불필요한 의존성이 생긴다.

Q. Wrong State Owner Problem이 뭐야?
A. State가 실제 사용 범위와 맞지 않는 Component에 배치되어 구조가 복잡해지는 문제다.

Q. Duplicated State가 뭐야?
A. 같은 의미의 값을 여러 State로 중복 저장한 상태다.

Q. Props를 Local State로 복사하면 안 돼?
A. 단순 표시 목적이면 권장하지 않는다. 편집 초안처럼 독립 수정 목적이 있을 때만 검토한다.

Q. State Ownership 검수에서 가장 중요한 것은?
A. State를 읽는 Component, 변경하는 Component, 가장 가까운 공통 부모를 확인하는 것이다.

Q. React Component Design Part03의 핵심은 뭐야?
A. State Owner를 명확히 정하고 Local State, Shared State, Page State, Server State, URL State, Global State를 구분해 안정적인 React Component 구조를 만드는 것이다.
