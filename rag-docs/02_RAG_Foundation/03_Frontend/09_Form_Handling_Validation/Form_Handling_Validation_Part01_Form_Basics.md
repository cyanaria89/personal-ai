# Form Handling & Validation Part01 - Form Basics

---

# 1. Form Handling Foundation

## 1.1 Form Handling Definition

### [개념]

Form Handling은 사용자의 입력값을 수집하고, React State로 관리하며, 검증 후 API 요청으로 연결하는 Frontend 구현 흐름이다.

React Form은 단순 HTML form 작성이 아니라 입력값 관리, 제출 이벤트 처리, Client Validation, Server Validation Error 처리, Request Body Mapping까지 포함한다.

---

### [핵심]

Form Handling 핵심 요소:

- form
- input
- textarea
- select
- checkbox
- radio
- file input
- value
- checked
- name
- onChange
- onSubmit
- preventDefault
- Form State
- Error State
- Submit Flow
- Client Validation
- Server Validation
- Request Body Mapping

---

### [실무]

2026 실무 기준에서 React Form은 아래 흐름으로 구현한다.

```text
User Input
→ onChange
→ Update Form State
→ Client Validation
→ onSubmit
→ preventDefault
→ Build Request Body
→ API Request
→ Success / Error UI
```

Form Handling은 다음 Domain과 연결된다.

```text
React Core
→ React Component Design
→ State Management
→ Data Fetching & REST API Integration
→ Form Handling & Validation
→ Authentication Frontend Flow
→ Error Handling & Loading UX
```

---

### [FAQ]

Q. Form Handling이 뭐야?
A. 사용자의 입력값을 State로 관리하고 검증 후 API 요청으로 연결하는 React Form 구현 흐름이다.

Q. Form Handling은 input 사용법만 의미해?
A. 아니다. 입력값 관리, 검증, 제출, 에러 표시, API Request Body 변환까지 포함한다.

Q. React Form에서 가장 중요한 것은 뭐야?
A. Controlled Component, Form State, onSubmit, preventDefault, Validation, Error Handling, Request Body Mapping이다.

Q. Form Handling 문서는 React Core와 뭐가 달라?
A. React Core는 기본 이벤트와 State를 다루고, Form Handling은 입력값 검증과 제출 흐름까지 다룬다.

---

# 2. Form Element Rules

## 2.1 Form Element

### [개념]

`form`은 사용자의 입력값을 하나의 제출 단위로 묶는 HTML 요소다.

React에서는 `form`의 기본 제출 동작을 막고 JavaScript 함수에서 검증과 API 요청을 처리한다.

---

### [핵심]

Form Element 필수 키워드:

- `<form>`
- `onSubmit`
- `event.preventDefault()`
- submit event
- Enter key submit
- button type
- input group
- validation
- API request

---

### [실무]

기본 Form 구조:

```jsx
function SearchForm({ onSearch }) {
  const [keyword, setKeyword] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    onSearch(keyword.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="keyword">검색어</label>
      <input
        id="keyword"
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <button type="submit">검색</button>
    </form>
  );
}
```

권장:

- form에는 `onSubmit` 사용
- submit button에는 `type="submit"` 명시
- 일반 button에는 `type="button"` 명시
- 제출 시 `event.preventDefault()` 호출
- 입력값 trim 기준 명확화
- submit handler에서 API 요청 또는 상위 callback 호출

---

### [FAQ]

Q. React에서도 form 태그를 써야 해?
A. 권장한다. form onSubmit을 사용하면 버튼 클릭과 Enter key 제출을 일관되게 처리할 수 있다.

Q. form 제출 시 페이지가 새로고침되는 이유는?
A. HTML form의 기본 제출 동작 때문이다. React에서는 onSubmit에서 event.preventDefault를 호출해야 한다.

Q. onClick으로 제출 처리해도 돼?
A. 가능하지만 form onSubmit이 Enter key 제출과 접근성 측면에서 더 적합하다.

Q. form action을 사용해도 돼?
A. 일반적인 React SPA에서는 action 대신 onSubmit에서 API 요청을 처리한다.

---

## 2.2 Button Type Rules

### [개념]

`button type`은 버튼이 form 내부에서 어떤 동작을 수행할지 결정한다.

form 내부의 button은 기본적으로 submit처럼 동작할 수 있으므로 명시적인 type 지정이 중요하다.

---

### [핵심]

Button Type 기준:

- `type="submit"`: Form 제출
- `type="button"`: 일반 클릭 버튼
- `type="reset"`: Native reset
- form 내부 button type 명시
- 중복 제출 방지
- 의도하지 않은 submit 방지

---

### [실무]

좋은 예:

```jsx
<form onSubmit={handleSubmit}>
  <input value={keyword} onChange={handleChange} />

  <button type="submit">검색</button>
  <button type="button" onClick={handleReset}>
    초기화
  </button>
</form>
```

나쁜 예:

```jsx
<form onSubmit={handleSubmit}>
  <input value={keyword} onChange={handleChange} />

  <button onClick={handleReset}>초기화</button>
</form>
```

주의:

- form 안의 일반 버튼은 `type="button"`을 명시
- reset 버튼은 React State와 동기화 기준 필요
- submit 중에는 submit button disabled 처리 권장
- 삭제, 취소, 모달 닫기 버튼은 일반적으로 `type="button"`

---

### [FAQ]

Q. button type을 꼭 써야 해?
A. 권장한다. form 내부 button은 의도치 않게 submit을 발생시킬 수 있다.

Q. 검색 버튼은 어떤 type을 써?
A. form 제출용이면 `type="submit"`을 사용한다.

Q. 초기화 버튼은 어떤 type을 써?
A. React State로 초기화할 경우 보통 `type="button"`과 reset handler를 사용한다.

Q. button type을 안 쓰면 어떤 문제가 생겨?
A. 취소나 초기화 버튼이 form submit을 발생시킬 수 있다.

---

# 3. Input Element Rules

## 3.1 Text Input

### [개념]

Text Input은 문자열 입력을 받는 가장 기본적인 Form Field다.

React에서는 일반적으로 `value`와 `onChange`를 사용해 Controlled Component로 관리한다.

---

### [핵심]

Text Input 핵심 요소:

- input
- type text
- value
- onChange
- event.target.value
- useState
- name
- placeholder
- label
- maxLength
- autoComplete

---

### [실무]

Text Input 예:

```jsx
function NicknameInput() {
  const [nickname, setNickname] = useState("");

  return (
    <div>
      <label htmlFor="nickname">닉네임</label>
      <input
        id="nickname"
        name="nickname"
        value={nickname}
        onChange={(event) => setNickname(event.target.value)}
      />
    </div>
  );
}
```

주의:

- 문자열 input 초기값은 `""` 권장
- `value`만 있고 `onChange`가 없으면 입력이 안 됨
- placeholder는 label 대체 불가
- `name`은 공통 handler와 Request Body Mapping에 중요
- maxLength는 UX용이며 Backend Validation도 필요

---

### [FAQ]

Q. input 값은 어떻게 State에 저장해?
A. value에 State를 연결하고 onChange에서 event.target.value로 State를 업데이트한다.

Q. input에 입력이 안 되는 이유는?
A. value만 설정하고 onChange로 State를 업데이트하지 않았을 가능성이 크다.

Q. input 초기값은 undefined로 둬도 돼?
A. 권장하지 않는다. 문자열 input은 빈 문자열 `""`로 시작하는 것이 안전하다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 아니다. 접근성과 사용성을 위해 label을 제공하는 것이 좋다.

---

## 3.2 Textarea

### [개념]

`textarea`는 여러 줄 문자열 입력을 받는 Form Field다.

리뷰, 댓글, 문의, 설명, 자기소개 같은 긴 텍스트 입력에 사용한다.

---

### [핵심]

Textarea 핵심 요소:

- textarea
- value
- onChange
- maxLength
- rows
- character count
- trim
- required
- content validation

---

### [실무]

Textarea 예:

```jsx
function ReviewContentField() {
  const [content, setContent] = useState("");

  return (
    <div>
      <label htmlFor="content">리뷰 내용</label>
      <textarea
        id="content"
        name="content"
        value={content}
        maxLength={500}
        rows={5}
        onChange={(event) => setContent(event.target.value)}
      />
      <p>{content.length}/500</p>
    </div>
  );
}
```

권장:

- 리뷰, 댓글, 문의 내용은 textarea 사용
- 글자 수 제한 표시 가능
- submit 시 trim 적용 기준 결정
- 공백만 입력한 경우 invalid 처리 권장
- Backend DTO length 제한과 Frontend maxLength 일치

---

### [FAQ]

Q. textarea도 value와 onChange로 제어해?
A. 그렇다. React에서는 textarea도 Controlled Component로 관리할 수 있다.

Q. textarea 내용은 submit 전에 trim해야 해?
A. 대부분 권장한다. 공백만 입력한 값을 방지하기 위해 trim 기준을 둔다.

Q. textarea 글자 수 제한은 Frontend만 있으면 돼?
A. 아니다. Backend에서도 length validation이 필요하다.

Q. 리뷰 내용 입력은 input이 좋아 textarea가 좋아?
A. 여러 줄 내용이므로 textarea가 적합하다.

---

## 3.3 Select

### [개념]

`select`는 정해진 옵션 중 하나 또는 여러 개를 선택하는 Form Field다.

지역 코드, 카테고리, 정렬 조건, 필터, enum 값 선택에 자주 사용한다.

---

### [핵심]

Select 핵심 요소:

- select
- option
- value
- onChange
- empty option
- code value
- enum value
- selected option
- multiple select

---

### [실무]

Select 예:

```jsx
function RegionSelect({ regionCode, onChange }) {
  return (
    <div>
      <label htmlFor="regionCode">지역</label>
      <select
        id="regionCode"
        name="regionCode"
        value={regionCode}
        onChange={onChange}
      >
        <option value="">전체</option>
        <option value="11">서울</option>
        <option value="26">부산</option>
      </select>
    </div>
  );
}
```

주의:

- option value는 Backend code 또는 enum 값과 일치
- 전체 선택은 빈 문자열 `""`로 둘 수 있음
- 빈 문자열을 API 요청에서 제외할지 null로 보낼지 결정
- select 값도 문자열로 들어올 수 있음
- multiple select는 별도 배열 처리 필요

---

### [FAQ]

Q. select 값은 어떻게 관리해?
A. value와 onChange로 선택된 option 값을 State에 저장한다.

Q. option value는 화면 문구로 넣어도 돼?
A. 보통 Backend가 요구하는 code 또는 enum 값을 넣는 것이 좋다.

Q. 전체 선택 option은 어떻게 처리해?
A. 보통 value를 빈 문자열로 두고 Request Body 또는 Query Param 생성 시 제외한다.

Q. select 값도 문자열로 들어와?
A. 대부분 문자열로 들어온다. 숫자 코드가 필요하면 변환 기준을 둬야 한다.

---

# 4. Checkbox and Radio Rules

## 4.1 Checkbox

### [개념]

Checkbox는 boolean 값 또는 여러 선택값을 처리하는 Form Field다.

단일 checkbox는 보통 `checked`와 `event.target.checked`로 제어한다.

---

### [핵심]

Checkbox 핵심 요소:

- input type checkbox
- checked
- event.target.checked
- boolean field
- agreement checkbox
- multiple checkbox
- array field
- required agreement

---

### [실무]

단일 Checkbox 예:

```jsx
function AgreeCheckbox() {
  const [agreed, setAgreed] = useState(false);

  return (
    <label>
      <input
        type="checkbox"
        name="agreed"
        checked={agreed}
        onChange={(event) => setAgreed(event.target.checked)}
      />
      약관에 동의합니다.
    </label>
  );
}
```

여러 Checkbox는 배열 상태로 관리할 수 있다.

```jsx
function toggleTheme(themeCode) {
  setSelectedThemes((prevThemes) =>
    prevThemes.includes(themeCode)
      ? prevThemes.filter((code) => code !== themeCode)
      : [...prevThemes, themeCode],
  );
}
```

주의:

- checkbox 선택 여부는 value가 아니라 checked 기준
- 약관 동의는 boolean 값으로 관리
- 여러 checkbox는 array field로 관리 가능
- 필수 동의는 Client Validation과 Server Validation 모두 필요

---

### [FAQ]

Q. checkbox는 value로 제어해?
A. 아니다. 선택 여부는 보통 checked와 event.target.checked로 제어한다.

Q. 약관 동의 checkbox 초기값은 뭐가 좋아?
A. false가 적합하다.

Q. 여러 checkbox 선택값은 어떻게 저장해?
A. 선택된 code나 id를 배열로 저장하는 방식이 일반적이다.

Q. checkbox required는 Frontend만 체크하면 돼?
A. 아니다. 중요한 동의 여부는 Backend에서도 검증해야 한다.

---

## 4.2 Radio

### [개념]

Radio Button은 여러 옵션 중 하나만 선택하는 Form Field다.

같은 그룹의 radio는 동일한 `name`을 사용하고, 현재 State 값과 option value를 비교해 `checked`를 설정한다.

---

### [핵심]

Radio 핵심 요소:

- input type radio
- same name
- value
- checked
- enum field
- single selection
- option group
- fieldset
- legend

---

### [실무]

Radio 예:

```jsx
function GenderRadioGroup({ gender, onChange }) {
  return (
    <fieldset>
      <legend>성별</legend>

      <label>
        <input
          type="radio"
          name="gender"
          value="MALE"
          checked={gender === "MALE"}
          onChange={onChange}
        />
        남성
      </label>

      <label>
        <input
          type="radio"
          name="gender"
          value="FEMALE"
          checked={gender === "FEMALE"}
          onChange={onChange}
        />
        여성
      </label>
    </fieldset>
  );
}
```

권장:

- 같은 radio group은 같은 name 사용
- 현재 State와 value 비교로 checked 설정
- Backend enum 값과 radio value 일치
- 접근성을 위해 fieldset / legend 고려
- 미선택 허용 여부 명확화

---

### [FAQ]

Q. radio button은 어떻게 제어해?
A. 같은 name을 사용하고 현재 State 값과 radio value가 같을 때 checked를 true로 설정한다.

Q. radio와 checkbox 차이는 뭐야?
A. radio는 여러 옵션 중 하나 선택이고 checkbox는 boolean 또는 다중 선택에 사용한다.

Q. radio value는 어떤 값을 넣어?
A. Backend enum 또는 code 값과 일치시키는 것이 좋다.

Q. radio group에는 label만 있으면 돼?
A. 접근성을 위해 fieldset과 legend를 함께 사용하는 것이 좋다.

---

# 5. File Input Basics

## 5.1 File Input

### [개념]

File Input은 사용자가 파일을 선택하는 Form Field다.

파일은 일반 문자열 value로 제어하지 않고 `File`, `FileList`, `FormData`로 처리한다.

---

### [핵심]

File Input 핵심 요소:

- input type file
- File
- FileList
- files
- accept
- multiple
- FormData
- image preview
- file size validation
- file type validation
- object URL cleanup

---

### [실무]

File Input 예:

```jsx
function ImageInput({ onFileSelect }) {
  function handleChange(event) {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    onFileSelect(file);
  }

  return <input type="file" accept="image/*" onChange={handleChange} />;
}
```

FormData 예:

```javascript
const formData = new FormData();

formData.append("image", file);
formData.append("content", values.content.trim());
```

주의:

- file input은 일반적으로 value로 제어하지 않음
- 파일 크기 제한 필요
- 파일 확장자와 MIME type 검증 필요
- 파일 업로드 보안 검증은 Backend 필수
- FormData key는 Backend field name과 일치
- 미리보기 URL은 필요 없어지면 정리

---

### [FAQ]

Q. file input도 value로 제어해?
A. 일반적으로 file input은 value로 제어하지 않고 event.target.files에서 File을 읽는다.

Q. 파일 업로드는 JSON으로 보내?
A. 보통 FormData를 사용해 multipart 요청으로 전송한다.

Q. 이미지 파일 미리보기는 어떻게 해?
A. URL.createObjectURL로 임시 URL을 만들 수 있다.

Q. 파일 검증은 Frontend만 하면 돼?
A. 아니다. 파일 크기, 타입, 보안 검증은 Backend에서도 반드시 수행해야 한다.

---

# 6. Controlled Component Basics

## 6.1 Controlled Component

### [개념]

Controlled Component는 Form 입력값을 DOM이 아니라 React State로 제어하는 방식이다.

입력값의 원본은 React State이며, 사용자의 입력은 onChange를 통해 State에 반영된다.

---

### [핵심]

Controlled Component 필수 요소:

- value
- checked
- onChange
- useState
- Form State
- Single Source of Truth
- input value update
- controlled input
- state-driven UI

---

### [실무]

Controlled Input 예:

```jsx
function EmailField() {
  const [email, setEmail] = useState("");

  return (
    <input
      type="email"
      value={email}
      onChange={(event) => setEmail(event.target.value)}
    />
  );
}
```

Controlled Checkbox 예:

```jsx
function TermsField() {
  const [agreed, setAgreed] = useState(false);

  return (
    <input
      type="checkbox"
      checked={agreed}
      onChange={(event) => setAgreed(event.target.checked)}
    />
  );
}
```

주의:

- text input은 `value` 사용
- checkbox / radio는 `checked` 사용
- value만 있고 onChange가 없으면 입력 불가
- 초기값 undefined 금지
- Controlled와 Uncontrolled 혼용 금지

---

### [FAQ]

Q. Controlled Component가 뭐야?
A. 입력값을 React State로 관리하고 value 또는 checked로 input을 제어하는 방식이다.

Q. Controlled Component가 왜 중요해?
A. 검증, 에러 표시, 제출 상태, Request Body Mapping을 State 기준으로 일관되게 처리할 수 있기 때문이다.

Q. value만 넣으면 Controlled Component야?
A. 아니다. value와 함께 onChange로 State를 업데이트해야 한다.

Q. checkbox도 Controlled Component로 만들 수 있어?
A. 가능하다. checked와 event.target.checked를 사용한다.

---

## 6.2 Controlled Component Initial Value

### [개념]

Controlled Component는 초기값을 명확히 지정해야 한다.

초기값이 undefined 또는 null이면 Controlled / Uncontrolled Warning이 발생할 수 있다.

---

### [핵심]

초기값 기준:

- text input: `""`
- textarea: `""`
- select: `""`
- checkbox: `false`
- multiple checkbox: `[]`
- number input: `""` 또는 숫자 변환 기준 명시
- object form values: 명확한 initialValues 사용

---

### [실무]

좋은 예:

```jsx
const initialValues = {
  email: "",
  password: "",
  agreed: false,
  selectedThemes: [],
};

const [values, setValues] = useState(initialValues);
```

수정 Form 예:

```jsx
<input value={values.email ?? ""} onChange={handleChange} />
```

주의:

- API 로딩 전 value가 undefined가 되지 않도록 처리
- defaultValue와 value 혼용 금지
- 초기값과 reset 기준 일치
- 수정 Form은 서버 초기값과 사용자 입력값 구분

---

### [FAQ]

Q. input 초기값을 undefined로 두면 안 돼?
A. 권장하지 않는다. uncontrolled to controlled warning이 발생할 수 있다.

Q. 문자열 input 초기값은 뭐가 좋아?
A. 빈 문자열 `""`이 적합하다.

Q. checkbox 초기값은 뭐가 좋아?
A. false가 적합하다.

Q. API 데이터가 늦게 오면 value는 어떻게 처리해?
A. `values.email ?? ""`처럼 undefined가 되지 않게 처리하거나 초기 Form State를 명확히 만든다.

---

# 7. Uncontrolled Component Basics

## 7.1 Uncontrolled Component

### [개념]

Uncontrolled Component는 입력값을 React State로 매번 제어하지 않고 DOM 자체가 값을 관리하게 두는 방식이다.

필요할 때 ref 또는 FormData로 값을 읽을 수 있다.

---

### [핵심]

Uncontrolled Component 사용 대상:

- file input
- ref based read
- one-time form
- FormData
- external library integration
- performance-sensitive large form basics
- React Hook Form internal pattern

---

### [실무]

간단한 ref 기반 예:

```jsx
function SimpleForm() {
  const inputRef = useRef(null);

  function handleSubmit(event) {
    event.preventDefault();

    const keyword = inputRef.current.value.trim();
  }

  return (
    <form onSubmit={handleSubmit}>
      <input ref={inputRef} />
      <button type="submit">검색</button>
    </form>
  );
}
```

주의:

- 일반적인 React Form은 Controlled 방식이 검증과 에러 처리에 유리
- file input은 uncontrolled 성격이 강함
- Controlled와 Uncontrolled를 같은 input에서 혼용하지 않음
- Form Library는 내부적으로 uncontrolled 방식을 활용할 수 있음

---

### [FAQ]

Q. Uncontrolled Component가 뭐야?
A. 입력값을 React State로 매번 제어하지 않고 DOM이나 ref에서 필요할 때 읽는 방식이다.

Q. Uncontrolled Component는 나쁜 방식이야?
A. 아니다. file input이나 Form Library 내부 구현처럼 적합한 경우가 있다.

Q. Controlled와 Uncontrolled 중 뭐가 좋아?
A. 일반 Form 검증과 API 연동에는 Controlled가 명확하고, file input이나 특수 상황에는 Uncontrolled가 적합할 수 있다.

Q. 한 input에서 value와 defaultValue를 같이 써도 돼?
A. 권장하지 않는다. Controlled와 Uncontrolled 혼용으로 경고가 발생할 수 있다.

---

# 8. Basic Form Flow

## 8.1 Basic Submit Flow

### [개념]

Basic Submit Flow는 사용자가 Form을 제출했을 때 발생하는 기본 처리 순서다.

React Form에서는 기본 제출 동작을 막고 검증과 API 요청을 직접 수행한다.

---

### [핵심]

Basic Submit Flow:

```text
Submit Event
→ preventDefault
→ Read Form State
→ Trim / Normalize
→ Client Validation
→ Build Request Body
→ API Request or Callback
→ Success / Error Handling
```

---

### [실무]

기초 Submit 예:

```jsx
function ReviewForm({ onCreateReview }) {
  const [content, setContent] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    const trimmedContent = content.trim();

    if (!trimmedContent) {
      return;
    }

    onCreateReview({
      content: trimmedContent,
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="content">리뷰</label>
      <textarea
        id="content"
        value={content}
        onChange={(event) => setContent(event.target.value)}
      />
      <button type="submit">등록</button>
    </form>
  );
}
```

권장:

- onSubmit에서 preventDefault 호출
- 입력값 정규화 기준 명확화
- 검증 실패 시 API 요청 중단
- Request Body 구조를 Backend DTO와 맞춤
- submit 성공 / 실패 처리는 별도 흐름에서 확장

---

### [FAQ]

Q. submit handler에서는 무엇을 해야 해?
A. preventDefault, 입력값 검증, Request Body 생성, API 요청 또는 상위 callback 호출을 처리한다.

Q. 검증 실패 시에도 API 요청을 보내?
A. 아니다. Client Validation 실패 시 요청을 중단한다.

Q. 입력값 trim은 어디서 해?
A. 보통 submit 직전 Request Body 생성 단계에서 처리한다.

Q. Form State를 그대로 API에 보내도 돼?
A. 간단한 경우 가능하지만 trim, type conversion, field mapping이 필요하면 Request Body로 변환한다.

---

# 9. Basic Form Accessibility

## 9.1 Label and Input Connection

### [개념]

Form Accessibility는 다양한 사용자가 Form을 이해하고 사용할 수 있도록 하는 기준이다.

가장 기본은 label과 input을 명확히 연결하는 것이다.

---

### [핵심]

접근성 핵심 요소:

- label
- htmlFor
- id
- aria-invalid
- aria-describedby
- role alert
- required indication
- keyboard navigation
- fieldset
- legend

---

### [실무]

접근성 있는 Field 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  value={values.email}
  onChange={handleChange}
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
{errors.email && (
  <p id="email-error" role="alert">
    {errors.email}
  </p>
)}
```

권장:

- 모든 input에 label 연결
- placeholder를 label 대체로 사용하지 않음
- 에러 메시지는 input과 연결
- 필수 입력 여부 표시
- radio / checkbox group에는 fieldset / legend 고려
- submit 실패 시 첫 에러 field focus 이동 고려

---

### [FAQ]

Q. label은 꼭 필요해?
A. 권장한다. label은 접근성과 사용성을 높이고 input 목적을 명확히 한다.

Q. placeholder로 label을 대체해도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 스크린 리더 사용자에게 불리할 수 있다.

Q. 에러 메시지는 input과 연결해야 해?
A. 권장한다. aria-describedby로 연결하면 오류를 더 명확히 전달할 수 있다.

Q. radio group 접근성은 어떻게 처리해?
A. fieldset과 legend를 사용해 그룹 목적을 설명하는 것이 좋다.

---

# 10. Common Mistakes

## 10.1 Form Basics Common Mistakes

### [개념]

Form Basics 단계에서 자주 발생하는 실수는 입력값 미변경, 페이지 새로고침, 의도치 않은 submit, checkbox 처리 오류, 접근성 누락이다.

---

### [핵심]

자주 발생하는 실수:

- onSubmit에서 preventDefault 누락
- button type 누락
- input value만 있고 onChange 없음
- checkbox를 value로 처리
- radio group name 불일치
- 초기값 undefined
- Controlled / Uncontrolled 혼용
- label 누락
- placeholder로 label 대체
- textarea trim 기준 없음
- select option value와 Backend code 불일치
- file input을 value로 제어하려고 함

---

### [실무]

Debug Flow:

```text
Form submit 문제
→ onSubmit 연결 확인
→ preventDefault 확인
→ button type 확인
→ input value / onChange 확인
→ checkbox checked 확인
→ initialValues 확인
→ label / id 연결 확인
```

나쁜 예:

```jsx
<input value={email} />
```

좋은 예:

```jsx
<input value={email} onChange={(event) => setEmail(event.target.value)} />
```

---

### [FAQ]

Q. Form 기초에서 가장 흔한 실수는 뭐야?
A. preventDefault 누락, button type 누락, value/onChange 불일치, checkbox checked 처리 누락이다.

Q. input 입력이 안 될 때 무엇을 확인해?
A. value, onChange, setState 호출, 초기값, disabled/readOnly 여부를 확인한다.

Q. submit이 갑자기 실행되는 이유는?
A. form 내부 button type을 지정하지 않아 기본 submit으로 동작했을 수 있다.

Q. checkbox 값이 이상하게 들어가는 이유는?
A. checked가 아니라 value를 읽고 있을 가능성이 크다.

---

# 11. Form Basics Checklist

## 11.1 Implementation Checklist

### [개념]

Form Basics Checklist는 React Form의 기본 구조가 안정적으로 작성되었는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] form에 onSubmit이 연결되었는가?
- [ ] submit handler에서 preventDefault를 호출하는가?
- [ ] submit button에 type="submit"이 명시되었는가?
- [ ] 일반 button에 type="button"이 명시되었는가?
- [ ] text input은 value와 onChange로 제어되는가?
- [ ] checkbox는 checked와 event.target.checked로 제어되는가?
- [ ] radio group은 같은 name을 사용하는가?
- [ ] select option value가 Backend code 또는 enum과 일치하는가?
- [ ] 문자열 input 초기값이 빈 문자열인가?
- [ ] checkbox 초기값이 false인가?
- [ ] Controlled와 Uncontrolled를 혼용하지 않는가?
- [ ] 모든 input에 label이 연결되었는가?
- [ ] placeholder를 label 대체로 사용하지 않는가?
- [ ] file input은 files 또는 FormData로 처리하는가?
- [ ] submit 전 trim / normalize 기준이 있는가?
- [ ] Request Body 구조가 Backend DTO와 연결 가능한가?
```

---

### [실무]

검수 Flow:

```text
Form Structure Check
→ Input Control Check
→ Button Type Check
→ Submit Flow Check
→ Initial Value Check
→ Accessibility Check
→ Request Mapping Readiness Check
```

---

### [FAQ]

Q. Form Basics 검수에서 가장 중요한 것은?
A. onSubmit, preventDefault, button type, value/onChange, checked 처리, 초기값, label 연결이다.

Q. Form Basics가 안정적이면 다음에 무엇을 검토해?
A. Form State 설계, Validation, Server Error Handling, Submit Loading, Request Body Mapping을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Form Handling이 뭐야?
A. 사용자의 입력값을 React State로 관리하고 검증 후 API 요청으로 연결하는 Frontend Form 구현 흐름이다.

Q. React Form은 어떻게 처리해?
A. 보통 Controlled Component로 입력값을 State에 저장하고 onSubmit에서 검증 후 API 요청을 수행한다.

Q. React에서 form 태그를 써야 해?
A. 권장한다. form onSubmit을 사용하면 버튼 클릭과 Enter key 제출을 일관되게 처리할 수 있다.

Q. form 제출 시 페이지가 새로고침되는 이유는?
A. 기본 form 제출 동작 때문이다. React에서는 onSubmit에서 event.preventDefault를 호출해야 한다.

Q. preventDefault는 왜 필요해?
A. 브라우저의 기본 form submit 새로고침을 막고 React에서 직접 제출 로직을 처리하기 위해 필요하다.

Q. onClick으로 submit 처리해도 돼?
A. 가능하지만 form onSubmit을 사용하는 것이 Enter key 제출과 접근성 측면에서 더 좋다.

Q. button type을 꼭 써야 해?
A. 권장한다. form 안의 button은 기본 submit으로 동작할 수 있어 일반 버튼은 type="button"을 명시하는 것이 안전하다.

Q. submit button type은 뭐야?
A. Form 제출용 버튼은 `type="submit"`을 사용한다.

Q. 일반 button type은 뭐야?
A. Form 제출이 아닌 버튼은 `type="button"`을 사용한다.

Q. input 값은 어떻게 State에 저장해?
A. value에 State를 연결하고 onChange에서 event.target.value로 State를 업데이트한다.

Q. input 값이 안 바뀌는 이유는?
A. value는 설정했지만 onChange로 State를 업데이트하지 않았을 가능성이 크다.

Q. 문자열 input 초기값은 뭐가 좋아?
A. 빈 문자열 `""`이 적합하다.

Q. textarea도 Controlled Component로 관리해?
A. 그렇다. value와 onChange로 textarea 값을 State에 저장할 수 있다.

Q. textarea 내용은 submit 전에 trim해야 해?
A. 대부분 권장한다. 공백만 입력한 값을 방지하기 위해 trim 기준을 둔다.

Q. select 값은 어떻게 관리해?
A. value와 onChange로 선택된 option 값을 State에 저장한다.

Q. select option value는 무엇으로 맞춰?
A. Backend가 요구하는 code 또는 enum 값과 일치시키는 것이 좋다.

Q. checkbox는 value야 checked야?
A. checkbox는 보통 checked와 event.target.checked로 제어한다.

Q. 약관 동의 checkbox 초기값은 뭐가 좋아?
A. false가 적합하다.

Q. 여러 checkbox 선택값은 어떻게 저장해?
A. 선택된 code 또는 id를 배열로 저장하는 방식이 일반적이다.

Q. radio button은 어떻게 제어해?
A. 같은 name을 가진 radio들 중 현재 값과 value가 일치하는 항목에 checked를 설정한다.

Q. radio와 checkbox 차이는 뭐야?
A. radio는 여러 옵션 중 하나 선택이고 checkbox는 boolean 또는 다중 선택에 사용한다.

Q. file input도 value로 제어해?
A. 일반적으로 file input은 value로 제어하지 않고 event.target.files에서 File을 읽는다.

Q. 파일 업로드는 어떻게 처리해?
A. File 객체를 읽고 FormData에 append한 뒤 multipart 요청으로 전송한다.

Q. Controlled Component가 뭐야?
A. 입력값을 DOM이 아니라 React State로 관리하는 input 방식이다.

Q. Controlled Component가 왜 중요해?
A. 검증, 에러 표시, 제출 상태, Request Body Mapping을 State 기준으로 일관되게 처리할 수 있기 때문이다.

Q. value만 있으면 Controlled Component야?
A. 아니다. value와 함께 onChange로 State를 업데이트해야 한다.

Q. Controlled Component 초기값은 왜 중요해?
A. undefined나 null로 시작하면 uncontrolled to controlled warning이 발생할 수 있기 때문이다.

Q. uncontrolled to controlled warning은 왜 나?
A. input value가 처음에는 undefined였다가 나중에 문자열로 바뀌는 등 제어 방식이 바뀌었기 때문이다.

Q. uncontrolled to controlled warning 해결 방법은 뭐야?
A. 초기값을 빈 문자열, false, []처럼 명확히 설정하고 value가 undefined가 되지 않게 한다.

Q. Uncontrolled Component가 뭐야?
A. 입력값을 React State로 매번 제어하지 않고 DOM이나 ref에서 필요할 때 읽는 방식이다.

Q. Uncontrolled Component는 언제 써?
A. file input, ref 기반 one-time form, 외부 라이브러리 연동, Form Library 내부 구현에서 사용할 수 있다.

Q. Controlled와 Uncontrolled를 섞어도 돼?
A. 한 input에서 두 방식을 혼용하면 경고와 예측 어려운 동작이 생길 수 있어 피한다.

Q. submit handler에서는 무엇을 해야 해?
A. preventDefault, 입력값 검증, Request Body 생성, API 요청 또는 상위 callback 호출을 처리한다.

Q. 검증 실패 시에도 API 요청을 보내?
A. 아니다. Client Validation 실패 시 요청을 중단한다.

Q. Form State를 그대로 API에 보내도 돼?
A. 간단한 경우 가능하지만 trim, type conversion, field mapping이 필요하면 Request Body로 변환한다.

Q. label은 꼭 필요해?
A. 권장한다. label은 접근성과 사용성을 높이고 input 목적을 명확히 한다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 접근성 측면에서 label을 대체하기 어렵다.

Q. 에러 메시지는 input과 연결해야 해?
A. 권장한다. aria-describedby로 연결하면 오류를 더 명확히 전달할 수 있다.

Q. Form 기초에서 가장 흔한 실수는 뭐야?
A. preventDefault 누락, button type 누락, value/onChange 불일치, checkbox checked 처리 누락이다.

Q. submit이 갑자기 실행되는 이유는?
A. form 내부 button type을 지정하지 않아 기본 submit으로 동작했을 수 있다.

Q. Form Basics 다음 문서는 뭐가 좋아?
A. Form State, Input Handling, Validation, Server Error Handling, Submit Flow 순서로 이어지는 것이 좋다.
