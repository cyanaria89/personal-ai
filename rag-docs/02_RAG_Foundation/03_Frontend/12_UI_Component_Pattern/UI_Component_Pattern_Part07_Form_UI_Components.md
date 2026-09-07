# UI Component Pattern Part07 - Form UI Components

---

# 1. Form UI Component Overview

## 1.1 Form UI Component Purpose

### [개념]

Form UI Component는 사용자의 입력을 받고, 입력 상태, 검증 상태, 제출 흐름을 화면에 표현하는 UI Component Pattern이다.

Form UI Component는 FormField, TextField, Textarea, Select, Checkbox, RadioGroup, SearchBox, FilterBar 같은 입력 UI를 포함한다.

Form UI Component는 입력값 검증, error message, helper text, label, aria-describedby, required, disabled, loading 상태를 일관되게 처리해야 한다.

---

### [핵심]

Form UI Component 핵심 대상:

- FormField
- TextField
- Textarea
- Select
- Checkbox
- RadioGroup
- SearchBox
- FilterBar
- FormActions
- FieldError
- HelperText
- Controlled Component
- Uncontrolled Component

핵심 기준:

- label 제공
- id / htmlFor 연결
- error message와 input 연결
- aria-invalid 적용
- aria-describedby 적용
- helperText와 error 우선순위 정의
- required / disabled / readOnly 상태 표현
- onChange 전달 방식 통일
- Form 제출과 Button type 구분
- API 호출은 Form UI Component가 직접 처리하지 않음
- 검증 로직은 Form Hook 또는 Feature Form에서 관리
- 공통 Form UI와 도메인 Form 구분

---

### [실무]

2026 실무 기준에서 Form UI Component는 입력 요소를 단순히 배치하는 것이 아니다.

Frontend Agent는 Form UI를 만들 때 다음 흐름을 따라야 한다.

```text
Identify Input Purpose
→ Define Field Structure
→ Connect Label
→ Define Controlled / Uncontrolled
→ Add Validation State
→ Connect Error Message
→ Add Accessibility
→ Separate Submit Logic
→ Review Form UX
```

책임 분리:

```text
Common Form UI
→ FormField, TextField, Select, Checkbox, RadioGroup

Feature Form
→ LoginForm, ReviewForm, FestivalSearchForm

Form Hook
→ value state, validation, submit handler

Page / Feature Container
→ API 호출, server error mapping, navigation
```

---

### [FAQ]

Q. Form UI Component 문서는 왜 필요해?
A. 입력 UI는 label, error, validation, accessibility 문제가 자주 발생하므로 Frontend Agent가 일관되게 설계하기 위해 필요하다.

Q. Form UI Component에서 가장 중요한 기준은 뭐야?
A. label 연결, error message 연결, controlled state 기준, submit 책임 분리, 접근성 속성이다.

Q. Form UI Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Form UI는 입력과 이벤트 전달을 담당하고 API 호출은 Feature Form, Page, Custom Hook에서 처리한다.

---

# 2. FormField Pattern

## 2.1 FormField Responsibility

### [개념]

FormField는 label, input control, helper text, error message를 하나의 구조로 묶는 Form UI Pattern이다.

FormField는 TextField, Select, Textarea 같은 입력 Component가 반복적으로 가지는 field layout과 설명 영역을 통일하는 역할을 한다.

---

### [핵심]

FormField 기본 책임:

- label 표시
- htmlFor 연결
- required mark 표시
- helperText 표시
- error message 표시
- error 우선순위 처리
- control 영역 제공
- aria-describedby 연결 지원
- field layout 통일

FormField Props 후보:

- id
- label
- required
- error
- helperText
- children
- className

주의:

- FormField가 직접 value state를 관리하지 않음
- FormField가 직접 validation을 수행하지 않음
- FormField가 직접 API 호출하지 않음
- label 없는 field 지양
- error와 helperText 우선순위 명확화

---

### [실무]

FormField 예:

```tsx
type FormFieldProps = {
  id: string;
  label: string;
  required?: boolean;
  error?: string;
  helperText?: string;
  children: React.ReactNode;
};

function FormField({
  id,
  label,
  required = false,
  error,
  helperText,
  children,
}: FormFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;

  return (
    <div className="form-field">
      <label htmlFor={id}>
        {label}
        {required && <span aria-hidden="true">*</span>}
      </label>

      {children}

      {helperText && !error && (
        <p id={helperId} className="form-field-helper">
          {helperText}
        </p>
      )}

      {error && (
        <p id={errorId} className="form-field-error" role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

TextField와 조합:

```tsx
function TextField({
  id,
  label,
  value,
  error,
  helperText,
  required,
  onChange,
}: TextFieldProps) {
  const errorId = `${id}-error`;
  const helperId = `${id}-helper`;
  const describedBy = error ? errorId : helperText ? helperId : undefined;

  return (
    <FormField
      id={id}
      label={label}
      error={error}
      helperText={helperText}
      required={required}
    >
      <input
        id={id}
        value={value}
        required={required}
        aria-invalid={Boolean(error)}
        aria-describedby={describedBy}
        onChange={(event) => onChange(event.target.value)}
      />
    </FormField>
  );
}
```

---

### [FAQ]

Q. FormField와 TextField는 뭐가 달라?
A. TextField는 input까지 포함한 Component이고 FormField는 label, 설명, 에러 영역을 감싸는 구조 Component로 사용할 수 있다.

Q. helper text와 error가 동시에 있으면?
A. 보통 error를 우선 표시하고 helper text는 숨기거나 보조로 유지한다.

Q. FormField에서 validation을 직접 처리해도 돼?
A. 권장하지 않는다. FormField는 표시 구조를 담당하고 validation은 Form Hook이나 Feature Form에서 처리한다.

---

## 2.2 FieldError and HelperText Pattern

### [개념]

FieldError와 HelperText는 입력값에 대한 오류 또는 보조 설명을 input 근처에 표시하는 UI Pattern이다.

FieldError는 사용자가 입력 문제를 즉시 이해하게 하고, HelperText는 입력 전후의 보조 안내를 제공한다.

---

### [핵심]

FieldError 기준:

- error message 표시
- role alert 사용 가능
- input과 aria-describedby 연결
- 사용자 친화 메시지 사용
- 서버 내부 에러 원문 노출 금지
- field 근처에 표시

HelperText 기준:

- 입력 가이드 제공
- 형식 안내 제공
- 제한 조건 안내 가능
- error가 있으면 숨기거나 보조로 처리
- input과 aria-describedby 연결 가능

주의:

- error message를 색상만으로 표시하지 않음
- helperText와 error id 충돌 방지
- 긴 설명은 field 밖 문서화 검토
- error message는 구체적이고 짧게 작성

---

### [실무]

FieldError 예:

```tsx
type FieldErrorProps = {
  id: string;
  message: string;
};

function FieldError({ id, message }: FieldErrorProps) {
  return (
    <p id={id} className="field-error" role="alert">
      {message}
    </p>
  );
}
```

HelperText 예:

```tsx
type HelperTextProps = {
  id: string;
  children: React.ReactNode;
};

function HelperText({ id, children }: HelperTextProps) {
  return (
    <p id={id} className="helper-text">
      {children}
    </p>
  );
}
```

Input 연결 예:

```tsx
<input
  id="email"
  value={email}
  aria-invalid={Boolean(emailError)}
  aria-describedby={emailError ? "email-error" : "email-helper"}
  onChange={(event) => setEmail(event.target.value)}
/>
<HelperText id="email-helper">이메일 형식으로 입력해 주세요.</HelperText>
<FieldError id="email-error" message="이메일 형식이 올바르지 않습니다." />
```

---

### [FAQ]

Q. error message는 input과 어떻게 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결한다.

Q. error message에 서버 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화적인 field error message로 변환하는 것이 좋다.

Q. helperText와 error를 동시에 보여줘도 돼?
A. 가능하지만 보통 error를 우선 표시하고 helperText는 숨기거나 보조로 유지한다.

---

# 3. Controlled and Uncontrolled UI

## 3.1 Controlled Component Pattern

### [개념]

Controlled Component는 입력값을 React state로 관리하고 value와 onChange를 통해 UI를 제어하는 Form UI Pattern이다.

Controlled Component는 입력값 검증, 조건부 버튼 disabled, 실시간 검색, 동적 UI 제어에 적합하다.

---

### [핵심]

Controlled Component 기준:

- value Props 사용
- onChange Props 사용
- React state가 source of truth
- 실시간 validation 가능
- submit 전 값 확인 쉬움
- UI 상태와 입력값 동기화 쉬움

사용 대상:

- LoginForm
- SearchBox
- FilterBar
- ReviewForm
- Controlled Select
- Dynamic Form
- validation이 필요한 입력

주의:

- value undefined 방지
- onChange 전달 방식 통일
- 불필요한 rerender 주의
- 대형 Form은 Form library 검토
- Form state와 server state 혼동 금지

---

### [실무]

Controlled TextField 예:

```tsx
function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    submitLogin({ email, password });
  }

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        id="email"
        label="이메일"
        type="email"
        value={email}
        onChange={setEmail}
      />

      <TextField
        id="password"
        label="비밀번호"
        type="password"
        value={password}
        onChange={setPassword}
      />

      <Button type="submit">로그인</Button>
    </form>
  );
}
```

Controlled Select 예:

```tsx
<Select
  id="region"
  label="지역"
  value={region}
  options={regionOptions}
  onChange={setRegion}
/>
```

---

### [FAQ]

Q. Controlled Component는 뭐야?
A. 입력값을 React state로 관리하고 value와 onChange로 input을 제어하는 Component다.

Q. Controlled Component는 언제 써?
A. 실시간 validation, 검색, 필터, 조건부 버튼 disabled처럼 입력값을 UI 상태와 연결해야 할 때 적합하다.

Q. value가 undefined이면 문제가 돼?
A. Controlled input에서는 value가 undefined가 되지 않도록 빈 문자열 같은 기본값을 사용하는 것이 좋다.

---

## 3.2 Uncontrolled Component Pattern

### [개념]

Uncontrolled Component는 입력값을 DOM 자체가 보유하고, ref 또는 FormData로 제출 시점에 값을 읽는 Form UI Pattern이다.

Uncontrolled Component는 단순 Form, 대형 Form, Form library register 방식에서 사용할 수 있다.

---

### [핵심]

Uncontrolled Component 기준:

- defaultValue 사용
- ref 또는 FormData로 값 읽기
- DOM이 입력 상태 보유
- React state 업데이트 감소
- Form library와 결합 가능
- 단순 제출 Form에 적합

사용 대상:

- 단순 문의 Form
- 검색어 제출만 필요한 Form
- React Hook Form register 구조
- 입력 중 UI 제어가 적은 Form

주의:

- 실시간 validation에는 부적합할 수 있음
- 조건부 UI 제어가 어렵다
- defaultValue와 value 혼용 금지
- ref 관리 필요
- 접근성 기준은 동일하게 적용

---

### [실무]

Uncontrolled FormData 예:

```tsx
function SearchForm() {
  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const keyword = String(formData.get("keyword") ?? "");

    search(keyword);
  }

  return (
    <form role="search" onSubmit={handleSubmit}>
      <label htmlFor="keyword">검색어</label>
      <input id="keyword" name="keyword" defaultValue="" />
      <Button type="submit">검색</Button>
    </form>
  );
}
```

ref 예:

```tsx
function CommentForm() {
  const inputRef = useRef<HTMLTextAreaElement>(null);

  function handleSubmit(event: React.FormEvent) {
    event.preventDefault();

    const content = inputRef.current?.value ?? "";
    submitComment(content);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="content">댓글</label>
      <textarea id="content" name="content" ref={inputRef} />
      <Button type="submit">등록</Button>
    </form>
  );
}
```

---

### [FAQ]

Q. Uncontrolled Component는 언제 써?
A. 입력 중 state 제어가 거의 필요 없고 제출 시점에만 값을 읽으면 되는 단순 Form에 사용할 수 있다.

Q. value와 defaultValue를 같이 써도 돼?
A. 권장하지 않는다. Controlled는 value, Uncontrolled는 defaultValue 기준으로 일관되게 사용해야 한다.

Q. Uncontrolled Form도 접근성 처리가 필요해?
A. 필요하다. label, error, aria-describedby 같은 접근성 기준은 동일하게 적용해야 한다.

---

## 3.3 Controlled vs Uncontrolled

### [개념]

Controlled vs Uncontrolled는 Form 입력값을 React state로 제어할지 DOM에 맡길지 선택하는 기준이다.

Form 복잡도, validation 방식, UI 제어 필요성, Form library 사용 여부에 따라 선택한다.

---

### [핵심]

비교:

| 기준         | Controlled       | Uncontrolled         |
| ------------ | ---------------- | -------------------- |
| 값 관리      | React state      | DOM                  |
| Props        | value / onChange | defaultValue / ref   |
| 실시간 검증  | 적합             | 제한적               |
| 조건부 UI    | 적합             | 제한적               |
| rerender     | 많을 수 있음     | 적을 수 있음         |
| 단순 Form    | 가능             | 적합                 |
| Form library | 가능             | register 방식과 적합 |

선택 기준:

```text
실시간 validation 필요
→ Controlled

입력값에 따라 UI가 변함
→ Controlled

제출 시점 값만 필요
→ Uncontrolled 가능

React Hook Form register 사용
→ Uncontrolled 기반 가능

복잡한 대형 Form
→ Form library 검토
```

---

### [실무]

Controlled 적합:

```tsx
<TextField id="keyword" label="검색어" value={keyword} onChange={setKeyword} />
```

Uncontrolled 적합:

```tsx
<input id="keyword" name="keyword" defaultValue="" />
```

혼용 금지 예:

```tsx
<input value={keyword} defaultValue="초기 검색어" />
```

---

### [FAQ]

Q. Controlled와 Uncontrolled 중 뭐가 더 좋아?
A. 우열보다 목적에 따라 다르다. 실시간 제어가 필요하면 Controlled, 제출 시점 값만 필요하면 Uncontrolled도 가능하다.

Q. Form library를 쓰면 Controlled가 필요 없어?
A. 아니다. Form library도 controlled 방식과 uncontrolled register 방식을 모두 사용할 수 있다.

Q. Controlled와 Uncontrolled를 섞어도 돼?
A. 한 input에서 value와 defaultValue를 혼용하는 것은 피해야 한다.

---

# 4. SearchBox Pattern

## 4.1 SearchBox Responsibility

### [개념]

SearchBox는 검색어 입력과 검색 실행을 위한 Form UI Component다.

SearchBox는 role search, input, submit button, reset button, loading 상태, onSearch 이벤트를 명확히 제공해야 한다.

---

### [핵심]

SearchBox 기본 책임:

- 검색어 입력
- 검색 제출
- Enter 제출 지원
- reset 가능
- loading 상태 표현
- disabled 상태 처리
- role search 제공
- placeholder 제공
- onChange 이벤트 전달
- onSearch 이벤트 전달
- onReset 이벤트 전달

Props 후보:

- value
- placeholder
- loading
- disabled
- autoFocus
- onChange
- onSearch
- onReset
- submitText
- resetText

주의:

- SearchBox 내부 API 호출 금지
- 검색 조건 URL 반영은 부모 책임
- debounce는 별도 기준 필요
- 검색어 검증은 Feature 기준
- reset 버튼 노출 기준 명확화

---

### [실무]

SearchBox 예:

```tsx
type SearchBoxProps = {
  value: string;
  placeholder?: string;
  loading?: boolean;
  disabled?: boolean;
  onChange: (value: string) => void;
  onSearch: () => void;
  onReset?: () => void;
};

function SearchBox({
  value,
  placeholder = "검색어를 입력하세요.",
  loading = false,
  disabled = false,
  onChange,
  onSearch,
  onReset,
}: SearchBoxProps) {
  function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    onSearch();
  }

  return (
    <form role="search" onSubmit={handleSubmit}>
      <label htmlFor="search-keyword">검색어</label>
      <input
        id="search-keyword"
        value={value}
        placeholder={placeholder}
        disabled={disabled || loading}
        onChange={(event) => onChange(event.target.value)}
      />

      {onReset && value && (
        <Button type="button" variant="secondary" onClick={onReset}>
          초기화
        </Button>
      )}

      <Button type="submit" loading={loading} disabled={disabled}>
        검색
      </Button>
    </form>
  );
}
```

사용 예:

```tsx
<SearchBox
  value={keyword}
  loading={loading}
  onChange={setKeyword}
  onSearch={() => searchFestivals(keyword)}
  onReset={() => setKeyword("")}
/>
```

---

### [FAQ]

Q. SearchBox 안에서 API 호출까지 해도 돼?
A. 공통 SearchBox라면 검색 이벤트만 부모로 전달하고 API 호출은 부모나 Hook에서 처리하는 것이 좋다.

Q. 검색 Form에는 form 태그를 쓰는 게 좋아?
A. 좋다. Enter key 제출과 접근성 측면에서 유리하다.

Q. SearchBox에는 role search가 필요해?
A. 검색 영역임을 명확히 하려면 form에 role search를 사용할 수 있다.

---

## 4.2 SearchBox Debounce Pattern

### [개념]

SearchBox Debounce Pattern은 사용자가 입력할 때마다 즉시 검색하지 않고 일정 시간 입력이 멈춘 뒤 검색하는 패턴이다.

Debounce는 자동완성, 실시간 검색, 필터 검색에서 API 호출 빈도를 줄이기 위해 사용한다.

---

### [핵심]

Debounce 적합:

- 실시간 검색
- 자동완성
- 키워드 추천
- 필터 결과 자동 갱신
- 입력 중 API 호출 최소화

Debounce 부적합:

- 명시적 검색 버튼 제출
- Enter 기반 검색
- 즉시 반응이 중요한 로컬 필터
- 짧고 단순한 Form submit

주의:

- SearchBox 자체에 debounce를 고정하지 않음
- debounce는 Hook 또는 부모에서 처리 가능
- loading 상태와 race condition 고려
- 최신 요청만 반영하는 기준 필요
- URL query sync와 함께 사용할 때 주의

---

### [실무]

Debounce Hook 예:

```tsx
function useDebouncedValue<T>(value: T, delay: number) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timerId = window.setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => window.clearTimeout(timerId);
  }, [value, delay]);

  return debouncedValue;
}
```

사용 예:

```tsx
function FestivalSearchPage() {
  const [keyword, setKeyword] = useState("");
  const debouncedKeyword = useDebouncedValue(keyword, 300);

  const { data, loading } = useFestivalSearch({
    keyword: debouncedKeyword,
  });

  return (
    <>
      <SearchBox
        value={keyword}
        loading={loading}
        onChange={setKeyword}
        onSearch={() => searchNow(keyword)}
      />
      <FestivalList festivals={data ?? []} />
    </>
  );
}
```

권장:

```text
SearchBox
→ 입력 UI 담당

useDebouncedValue
→ debounce 상태 담당

useFestivalSearch
→ API 요청 담당
```

---

### [FAQ]

Q. SearchBox 안에 debounce를 넣어도 돼?
A. 공통 SearchBox에 고정하기보다 Hook이나 부모에서 처리하면 재사용성이 좋다.

Q. 검색 버튼이 있는 SearchBox에도 debounce가 필요해?
A. 명시적 검색 버튼 제출만 사용한다면 debounce가 필요 없을 수 있다.

Q. 실시간 검색에서 주의할 점은 뭐야?
A. API 호출 빈도, loading 표시, 오래된 요청 결과가 최신 결과를 덮어쓰지 않도록 주의해야 한다.

---

# 5. FilterBar Pattern

## 5.1 FilterBar Responsibility

### [개념]

FilterBar는 목록이나 검색 결과를 좁히기 위해 여러 필터 입력을 한 영역에 배치하는 UI Component Pattern이다.

FilterBar는 Select, Checkbox, SearchBox, DateRange, Toggle 같은 입력 UI를 조합할 수 있다.

---

### [핵심]

FilterBar 기본 책임:

- 필터 UI 그룹 제공
- 검색어 입력 조합
- select 필터 조합
- checkbox / toggle 필터 조합
- reset action 제공
- apply action 제공 가능
- loading / disabled 상태 전달
- URL query state와 연동 가능
- 접근 가능한 label 제공
- responsive layout 고려

Props 후보:

- filters
- value
- loading
- disabled
- onChange
- onApply
- onReset
- children

주의:

- FilterBar가 API를 직접 호출하지 않음
- 복잡한 필터 상태는 부모 또는 Hook에서 관리
- 모든 필터를 공통 Props로 추상화하지 않음
- Feature별 FilterBar가 더 적합할 수 있음
- label 없는 Select 지양

---

### [실무]

Feature FilterBar 예:

```tsx
type FestivalFilterValue = {
  keyword: string;
  region: string;
  category: string;
};

type FestivalFilterBarProps = {
  value: FestivalFilterValue;
  regionOptions: SelectOption[];
  categoryOptions: SelectOption[];
  loading?: boolean;
  onChange: (value: FestivalFilterValue) => void;
  onReset: () => void;
};

function FestivalFilterBar({
  value,
  regionOptions,
  categoryOptions,
  loading = false,
  onChange,
  onReset,
}: FestivalFilterBarProps) {
  return (
    <section aria-label="축제 검색 필터" className="filter-bar">
      <TextField
        id="festival-keyword"
        label="검색어"
        value={value.keyword}
        onChange={(keyword) => onChange({ ...value, keyword })}
      />

      <Select
        id="festival-region"
        label="지역"
        value={value.region}
        options={regionOptions}
        disabled={loading}
        onChange={(region) => onChange({ ...value, region })}
      />

      <Select
        id="festival-category"
        label="카테고리"
        value={value.category}
        options={categoryOptions}
        disabled={loading}
        onChange={(category) => onChange({ ...value, category })}
      />

      <Button type="button" variant="secondary" onClick={onReset}>
        필터 초기화
      </Button>
    </section>
  );
}
```

Page 조합:

```tsx
<FestivalFilterBar
  value={filter}
  regionOptions={regionOptions}
  categoryOptions={categoryOptions}
  loading={loading}
  onChange={setFilter}
  onReset={resetFilter}
/>
```

---

### [FAQ]

Q. FilterBar는 Common UI야 Feature UI야?
A. 필터 항목이 도메인에 강하게 의존하면 Feature UI로 두는 것이 적합하다.

Q. FilterBar 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 필터 값 변경 이벤트만 전달하고 API 호출은 Page나 Hook에서 처리하는 것이 좋다.

Q. 모든 필터를 하나의 공통 FilterBar로 만들면 좋아?
A. 과도한 추상화가 될 수 있다. 도메인별 필터 요구가 다르면 Feature FilterBar가 더 안전하다.

---

## 5.2 Filter State and URL Query

### [개념]

Filter State and URL Query는 필터 상태를 Local State로만 관리할지, URL query parameter와 동기화할지 판단하는 기준이다.

검색 결과 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query state를 검토한다.

---

### [핵심]

Local State 적합:

- 화면 내부 임시 필터
- 공유 필요 없음
- 새로고침 유지 필요 없음
- 단순 UI 상태

URL Query 적합:

- 검색 결과 공유 필요
- 새로고침 후 필터 유지 필요
- 브라우저 뒤로가기 의미 있음
- 서버 검색 조건과 직접 연결
- 페이지네이션과 함께 사용

주의:

- URL query와 input state 동기화 기준 필요
- 빈 값 제거 기준 필요
- debounce와 URL sync 충돌 주의
- page 변경 시 filter 유지 기준 필요
- filter 변경 시 page reset 기준 필요

---

### [실무]

URL Query 예:

```text
/festivals?keyword=music&region=seoul&page=1
```

Filter 변경 Flow:

```text
Filter Input Change
→ Update Local Filter State
→ Apply Search
→ Update URL Query
→ Fetch Data
```

Filter 변경 시 page reset:

```text
region 변경
→ page=1로 reset
→ query update
→ data refetch
```

권장 판단:

```text
사용자가 검색 결과 URL을 공유해야 하는가?
→ URL Query

단순 화면 내부 toggle인가?
→ Local State

페이지네이션과 연결되는가?
→ URL Query 권장
```

---

### [FAQ]

Q. 필터 상태는 URL에 넣는 게 좋아?
A. 검색 결과 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query parameter가 적합하다.

Q. 필터 변경 시 page는 유지해야 해?
A. 보통 필터 조건이 바뀌면 page를 1로 reset하는 것이 자연스럽다.

Q. URL Query와 Local State를 같이 써도 돼?
A. 가능하지만 동기화 기준을 명확히 정해야 한다.

---

# 6. Form Submit Pattern

## 6.1 Form Submit Responsibility

### [개념]

Form Submit Pattern은 사용자가 Form을 제출할 때 validation, loading, disabled, error mapping, success action을 처리하는 기준이다.

공통 Form UI는 제출 이벤트를 전달하고, 도메인 submit 로직은 Feature Form이나 Hook에서 처리한다.

---

### [핵심]

Submit Flow:

```text
User Submit
→ Prevent Default
→ Client Validation
→ Set Loading
→ API Request
→ Handle Success
→ Handle Server Error
→ Clear Loading
```

Form Submit 고려:

- form onSubmit 사용
- Button type submit 사용
- 일반 버튼은 type button 사용
- loading 중 중복 제출 방지
- submit disabled 기준
- field error 표시
- global error 표시
- server error mapping
- 성공 후 reset / navigate 기준

주의:

- Button 기본 type 누락 주의
- onClick만으로 submit 처리 지양
- API 요청 중 중복 제출 방지
- server error 원문 노출 금지
- validation 책임 위치 명확화

---

### [실무]

Submit 예:

```tsx
function ReviewForm() {
  const [content, setContent] = useState("");
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(event: React.FormEvent) {
    event.preventDefault();

    if (!content.trim()) {
      setError("리뷰 내용을 입력해 주세요.");
      return;
    }

    setSubmitting(true);

    try {
      await createReview({ content });
      setContent("");
      setError("");
    } catch {
      setError("리뷰를 등록하지 못했습니다. 다시 시도해 주세요.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <Textarea
        id="review-content"
        label="리뷰 내용"
        value={content}
        error={error}
        onChange={setContent}
      />

      <Button type="submit" loading={submitting}>
        리뷰 등록
      </Button>
    </form>
  );
}
```

FormActions 예:

```tsx
type FormActionsProps = {
  children: React.ReactNode;
};

function FormActions({ children }: FormActionsProps) {
  return <div className="form-actions">{children}</div>;
}
```

---

### [FAQ]

Q. Form 제출은 button onClick으로 처리해도 돼?
A. 가능하지만 form onSubmit과 submit button을 사용하면 Enter 제출과 접근성 측면에서 더 좋다.

Q. submit 버튼 type은 뭘로 해야 해?
A. Form 제출 버튼은 type submit을 명시하고, 일반 버튼은 type button을 사용한다.

Q. 제출 중에는 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 막고 처리 중임을 명확히 보여줄 수 있다.

---

## 6.2 Field Error vs Global Error

### [개념]

Field Error는 특정 입력값에 대한 오류이고, Global Error는 Form 전체 또는 요청 전체에 대한 오류다.

Form UI는 field error와 global error를 구분해서 표시해야 한다.

---

### [핵심]

Field Error 적합:

- 이메일 형식 오류
- 비밀번호 길이 오류
- 필수 입력 누락
- 특정 필드 중복
- 날짜 범위 오류

Global Error 적합:

- 로그인 실패
- 서버 오류
- 네트워크 오류
- 권한 오류
- 알 수 없는 요청 실패
- 여러 필드와 관련된 오류

비교:

| 기준  | Field Error      | Global Error        |
| ----- | ---------------- | ------------------- |
| 위치  | 입력 필드 근처   | Form 상단 또는 하단 |
| 연결  | aria-describedby | role alert          |
| 대상  | 특정 input       | Form 전체           |
| 예    | 이메일 형식 오류 | 로그인 실패         |
| Props | error            | formError           |

---

### [실무]

Field Error 예:

```tsx
<TextField
  id="email"
  label="이메일"
  value={email}
  error={emailError}
  onChange={setEmail}
/>
```

Global Error 예:

```tsx
{
  formError && <ErrorState message={formError} />;
}
```

Login Form 예:

```tsx
<form onSubmit={handleSubmit}>
  {formError && (
    <div role="alert" className="form-error">
      {formError}
    </div>
  )}

  <TextField
    id="email"
    label="이메일"
    value={email}
    error={emailError}
    onChange={setEmail}
  />

  <TextField
    id="password"
    label="비밀번호"
    type="password"
    value={password}
    error={passwordError}
    onChange={setPassword}
  />

  <Button type="submit" loading={submitting}>
    로그인
  </Button>
</form>
```

---

### [FAQ]

Q. Field Error와 Global Error는 어떻게 구분해?
A. 특정 input 문제는 Field Error, Form 전체 요청 실패나 서버 오류는 Global Error로 표시한다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 보통 이메일이나 비밀번호 중 어느 필드가 문제인지 특정하지 않으므로 Global Error가 적합하다.

Q. 서버 validation error는 어떻게 표시해?
A. 필드와 매핑 가능한 오류는 Field Error로, 매핑이 어려운 오류는 Global Error로 표시한다.

---

# 7. Form UI Anti Pattern

## 7.1 Form UI Common Mistakes

### [개념]

Form UI Common Mistakes는 입력 UI에서 자주 발생하는 접근성, 상태 관리, submit 처리, validation 책임 문제다.

Form UI는 사용자 입력과 직접 연결되므로 작은 설계 오류가 사용성 문제로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- label 없이 placeholder만 사용
- input과 error message 연결 누락
- aria-invalid 누락
- required 표시와 required 속성 불일치
- Button 기본 type 누락
- 일반 버튼이 submit으로 동작
- form onSubmit 없이 onClick만 사용
- loading 중 중복 제출 허용
- 서버 에러 원문 노출
- Field Error와 Global Error 혼동
- Controlled와 Uncontrolled 혼용
- value undefined 발생
- FilterBar에서 API 직접 호출
- SearchBox에서 API 직접 호출
- Form UI Component에 도메인 검증 로직 포함
- 모든 Form을 하나의 만능 Component로 추상화

---

### [실무]

나쁜 예:

```tsx
<form>
  <input placeholder="이메일" />
  <input placeholder="비밀번호" />
  <button onClick={login}>로그인</button>
</form>
```

문제점:

```text
label 없음
button type 누락
form submit 흐름 없음
Enter 제출 기준 불명확
error 연결 불가능
접근성 부족
```

개선:

```tsx
<form onSubmit={handleSubmit}>
  <TextField
    id="email"
    label="이메일"
    type="email"
    value={email}
    error={emailError}
    onChange={setEmail}
  />

  <TextField
    id="password"
    label="비밀번호"
    type="password"
    value={password}
    error={passwordError}
    onChange={setPassword}
  />

  <Button type="submit" loading={submitting}>
    로그인
  </Button>
</form>
```

---

### [FAQ]

Q. placeholder만 쓰면 안 돼?
A. 권장하지 않는다. placeholder는 입력하면 사라지고 접근성 측면에서도 label을 대체하기 어렵다.

Q. Form 안의 일반 버튼도 type을 지정해야 해?
A. 지정하는 것이 좋다. 일반 버튼은 type button, 제출 버튼은 type submit으로 명확히 구분한다.

Q. Form UI에서 가장 흔한 실수는 뭐야?
A. label 누락, error 연결 누락, Button type 누락, 중복 제출 방지 누락이 많다.

---

## 7.2 Form UI Review Checklist

### [개념]

Form UI Review Checklist는 FormField, SearchBox, FilterBar, Submit Pattern이 적절히 설계되었는지 검수하는 기준이다.

Frontend Agent와 Review Agent는 Form UI 생성 후 입력 구조, 상태, 접근성, submit 책임을 반드시 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 모든 입력에 label이 있는가?
- [ ] label과 input이 id / htmlFor로 연결되었는가?
- [ ] error message가 input과 aria-describedby로 연결되었는가?
- [ ] aria-invalid가 error 상태와 연결되었는가?
- [ ] helperText와 error 우선순위가 정의되었는가?
- [ ] required 표시와 required 속성이 일치하는가?
- [ ] Controlled / Uncontrolled 기준이 일관적인가?
- [ ] value와 defaultValue를 혼용하지 않는가?
- [ ] value undefined가 발생하지 않는가?
- [ ] onChange 전달 방식이 프로젝트 기준과 일치하는가?
- [ ] form onSubmit을 사용하는가?
- [ ] submit 버튼에 type submit을 명시했는가?
- [ ] 일반 버튼에 type button을 명시했는가?
- [ ] loading 중 중복 제출을 방지하는가?
- [ ] Field Error와 Global Error가 구분되었는가?
- [ ] 서버 에러 원문을 노출하지 않는가?
- [ ] SearchBox가 API를 직접 호출하지 않는가?
- [ ] FilterBar가 API를 직접 호출하지 않는가?
- [ ] Form UI Component에 도메인 검증 로직이 과도하게 들어가지 않았는가?
- [ ] 과도한 Form 추상화가 없는가?
```

---

### [실무]

검수 Flow:

```text
Form Draft
→ Label Check
→ Value State Check
→ Error Connection Check
→ Submit Flow Check
→ Loading / Disabled Check
→ Server Error Mapping Check
→ Accessibility Check
→ Anti Pattern Check
→ Final Review
```

치명적 문제:

```text
label 없는 input
placeholder만 사용하는 input
aria-describedby 누락
Button type 누락
중복 제출 가능
서버 에러 원문 노출
Controlled / Uncontrolled 혼용
SearchBox 내부 API 호출
FilterBar 내부 API 호출
```

---

### [FAQ]

Q. Form UI 검수에서 가장 중요한 것은 뭐야?
A. label 연결, error message 연결, submit 책임 분리, Button type, 중복 제출 방지를 먼저 확인해야 한다.

Q. Form UI에서 치명적인 문제는 뭐야?
A. label 누락, error 연결 누락, Button type 누락, 서버 에러 원문 노출, 중복 제출 허용이 치명적이다.

Q. Review Agent는 Form UI를 어떻게 검토해야 해?
A. label, value state, error 연결, submit flow, loading, 접근성, API 호출 위치를 순서대로 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Form UI Component 문서는 왜 필요해?
A. 입력 UI는 label, error, validation, accessibility 문제가 자주 발생하므로 Frontend Agent가 일관되게 설계하기 위해 필요하다.

Q. Form UI Component에서 가장 중요한 기준은 뭐야?
A. label 연결, error message 연결, controlled state 기준, submit 책임 분리, 접근성 속성이다.

Q. Form UI Component 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. Form UI는 입력과 이벤트 전달을 담당하고 API 호출은 Feature Form, Page, Custom Hook에서 처리한다.

Q. FormField와 TextField는 뭐가 달라?
A. TextField는 input까지 포함한 Component이고 FormField는 label, 설명, 에러 영역을 감싸는 구조 Component로 사용할 수 있다.

Q. helper text와 error가 동시에 있으면?
A. 보통 error를 우선 표시하고 helper text는 숨기거나 보조로 유지한다.

Q. FormField에서 validation을 직접 처리해도 돼?
A. 권장하지 않는다. FormField는 표시 구조를 담당하고 validation은 Form Hook이나 Feature Form에서 처리한다.

Q. error message는 input과 어떻게 연결해?
A. error message id를 만들고 input의 aria-describedby에 연결한다.

Q. error message에 서버 원문을 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 친화적인 field error message로 변환하는 것이 좋다.

Q. helperText와 error를 동시에 보여줘도 돼?
A. 가능하지만 보통 error를 우선 표시하고 helperText는 숨기거나 보조로 유지한다.

Q. Controlled Component는 뭐야?
A. 입력값을 React state로 관리하고 value와 onChange로 input을 제어하는 Component다.

Q. Controlled Component는 언제 써?
A. 실시간 validation, 검색, 필터, 조건부 버튼 disabled처럼 입력값을 UI 상태와 연결해야 할 때 적합하다.

Q. value가 undefined이면 문제가 돼?
A. Controlled input에서는 value가 undefined가 되지 않도록 빈 문자열 같은 기본값을 사용하는 것이 좋다.

Q. Uncontrolled Component는 언제 써?
A. 입력 중 state 제어가 거의 필요 없고 제출 시점에만 값을 읽으면 되는 단순 Form에 사용할 수 있다.

Q. value와 defaultValue를 같이 써도 돼?
A. 권장하지 않는다. Controlled는 value, Uncontrolled는 defaultValue 기준으로 일관되게 사용해야 한다.

Q. Uncontrolled Form도 접근성 처리가 필요해?
A. 필요하다. label, error, aria-describedby 같은 접근성 기준은 동일하게 적용해야 한다.

Q. Controlled와 Uncontrolled 중 뭐가 더 좋아?
A. 우열보다 목적에 따라 다르다. 실시간 제어가 필요하면 Controlled, 제출 시점 값만 필요하면 Uncontrolled도 가능하다.

Q. Form library를 쓰면 Controlled가 필요 없어?
A. 아니다. Form library도 controlled 방식과 uncontrolled register 방식을 모두 사용할 수 있다.

Q. Controlled와 Uncontrolled를 섞어도 돼?
A. 한 input에서 value와 defaultValue를 혼용하는 것은 피해야 한다.

Q. SearchBox 안에서 API 호출까지 해도 돼?
A. 공통 SearchBox라면 검색 이벤트만 부모로 전달하고 API 호출은 부모나 Hook에서 처리하는 것이 좋다.

Q. 검색 Form에는 form 태그를 쓰는 게 좋아?
A. 좋다. Enter key 제출과 접근성 측면에서 유리하다.

Q. SearchBox에는 role search가 필요해?
A. 검색 영역임을 명확히 하려면 form에 role search를 사용할 수 있다.

Q. SearchBox 안에 debounce를 넣어도 돼?
A. 공통 SearchBox에 고정하기보다 Hook이나 부모에서 처리하면 재사용성이 좋다.

Q. 검색 버튼이 있는 SearchBox에도 debounce가 필요해?
A. 명시적 검색 버튼 제출만 사용한다면 debounce가 필요 없을 수 있다.

Q. 실시간 검색에서 주의할 점은 뭐야?
A. API 호출 빈도, loading 표시, 오래된 요청 결과가 최신 결과를 덮어쓰지 않도록 주의해야 한다.

Q. FilterBar는 Common UI야 Feature UI야?
A. 필터 항목이 도메인에 강하게 의존하면 Feature UI로 두는 것이 적합하다.

Q. FilterBar 안에서 API 호출을 해도 돼?
A. 권장하지 않는다. 필터 값 변경 이벤트만 전달하고 API 호출은 Page나 Hook에서 처리하는 것이 좋다.

Q. 모든 필터를 하나의 공통 FilterBar로 만들면 좋아?
A. 과도한 추상화가 될 수 있다. 도메인별 필터 요구가 다르면 Feature FilterBar가 더 안전하다.

Q. 필터 상태는 URL에 넣는 게 좋아?
A. 검색 결과 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query parameter가 적합하다.

Q. 필터 변경 시 page는 유지해야 해?
A. 보통 필터 조건이 바뀌면 page를 1로 reset하는 것이 자연스럽다.

Q. URL Query와 Local State를 같이 써도 돼?
A. 가능하지만 동기화 기준을 명확히 정해야 한다.

Q. Form 제출은 button onClick으로 처리해도 돼?
A. 가능하지만 form onSubmit과 submit button을 사용하면 Enter 제출과 접근성 측면에서 더 좋다.

Q. submit 버튼 type은 뭘로 해야 해?
A. Form 제출 버튼은 type submit을 명시하고, 일반 버튼은 type button을 사용한다.

Q. 제출 중에는 버튼을 disabled 해야 해?
A. 권장한다. 중복 제출을 막고 처리 중임을 명확히 보여줄 수 있다.

Q. Field Error와 Global Error는 어떻게 구분해?
A. 특정 input 문제는 Field Error, Form 전체 요청 실패나 서버 오류는 Global Error로 표시한다.

Q. 로그인 실패는 Field Error야 Global Error야?
A. 보통 이메일이나 비밀번호 중 어느 필드가 문제인지 특정하지 않으므로 Global Error가 적합하다.

Q. 서버 validation error는 어떻게 표시해?
A. 필드와 매핑 가능한 오류는 Field Error로, 매핑이 어려운 오류는 Global Error로 표시한다.

Q. placeholder만 쓰면 안 돼?
A. 권장하지 않는다. placeholder는 입력하면 사라지고 접근성 측면에서도 label을 대체하기 어렵다.

Q. Form 안의 일반 버튼도 type을 지정해야 해?
A. 지정하는 것이 좋다. 일반 버튼은 type button, 제출 버튼은 type submit으로 명확히 구분한다.

Q. Form UI에서 가장 흔한 실수는 뭐야?
A. label 누락, error 연결 누락, Button type 누락, 중복 제출 방지 누락이 많다.

Q. Form UI 검수에서 가장 중요한 것은 뭐야?
A. label 연결, error message 연결, submit 책임 분리, Button type, 중복 제출 방지를 먼저 확인해야 한다.

Q. Form UI에서 치명적인 문제는 뭐야?
A. label 누락, error 연결 누락, Button type 누락, 서버 에러 원문 노출, 중복 제출 허용이 치명적이다.

Q. Review Agent는 Form UI를 어떻게 검토해야 해?
A. label, value state, error 연결, submit flow, loading, 접근성, API 호출 위치를 순서대로 확인해야 한다.
