# Form Handling & Validation Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Form Handling & Validation Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- React Form 입력 처리 기준 제공
- Controlled Component 작성 기준 제공
- Form State 설계 기준 제공
- Client Validation 기준 제공
- Server Validation Error 처리 기준 제공
- Submit Flow 설계 지원
- Form UX / Error UX 기준 제공
- React Hook Form 적용 판단 기준 제공
- TypeScript Form Type 설계 지원
- API Request Body와 Form Data 연결 기준 제공
- 로그인 / 회원가입 / 리뷰 작성 / 검색 Form 구현 지원
- 유지보수 가능한 Form Component 구조 설계 지원

---

### [핵심]

우선순위:

1. Form State
2. Controlled Component
3. Input Handling
4. onChange / onSubmit
5. Client Validation
6. Server Validation
7. Error Message
8. Submit Flow
9. Request Body Mapping
10. Form Reset
11. Disabled / Loading State
12. React Hook Form
13. TypeScript Form Type
14. Accessibility
15. Form Troubleshooting

---

### [실무]

2026 실무 기준에서 Form Handling & Validation 문서는 단순 input 사용법 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 입력값 State 설계
- Controlled Input 작성
- Form Submit 처리
- Client Validation 작성
- Backend Validation Error 표시
- Form Field Error 구조 설계
- Submit Loading 처리
- 중복 제출 방지
- Request DTO 생성
- Form Component 분리
- React Hook Form 적용 여부 판단
- 접근성 있는 Form 작성
- Form 오류 디버깅 수행

---

### [FAQ]

Q. Form Handling 문서는 React Core와 뭐가 달라?

A.
React Core는 기본 input과 event 처리이고 Form Handling은 여러 입력값, 검증, 제출, 에러 표시, API 연동까지 다룬다.

Q. Form Handling에서 가장 중요한 기준은 뭐야?

A.
Controlled Input, Form State, Validation, Submit Flow, Error Message, Request Body Mapping이다.

Q. 모든 Form에 React Hook Form을 써야 해?

A.
아니다. 간단한 Form은 useState로 충분하고, 필드와 검증이 많아지면 React Hook Form 같은 도구를 검토한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Form Handling & Validation 문서는 React Form 구현에 필요한 범위를 포함한다.

포함 범위:

- Form Element
- Input
- Textarea
- Select
- Checkbox
- Radio
- File Input Basics
- Controlled Component
- Uncontrolled Component Basics
- Form State
- Field State
- Error State
- Touched State
- Dirty State
- Submit State
- onChange
- onBlur
- onSubmit
- preventDefault
- Client Validation
- Required Validation
- Length Validation
- Format Validation
- Number Range Validation
- Password Confirm Validation
- Server Validation Error
- Field Error Message
- Global Form Error
- Request Body Mapping
- Form Reset
- Submit Loading
- Disabled State
- Duplicate Submit Prevention
- React Hook Form Basics
- TypeScript Form Type
- Form Accessibility
- Form Troubleshooting

---

### [핵심]

반드시 포함:

- Form Submit에는 preventDefault 필요
- Controlled Input은 value와 onChange로 제어
- Form State는 입력값과 에러 상태를 구분
- Client Validation은 UX용
- Server Validation은 최종 검증
- Field Error와 Global Error를 구분
- Submit 중 중복 제출 방지
- API Request Body는 Form State에서 생성
- 민감정보는 로그 출력 금지
- 복잡한 Form은 React Hook Form 도입 검토
- label / aria / role 등 접근성 기준 포함

---

### [실무]

Form Handling은 Data Fetching과 Authentication Frontend Flow 사이에서 자주 사용된다.

실무 연결:

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

Q. Form Handling 문서에서 로그인 Form도 다뤄?

A.
입력값, 검증, 제출, 에러 처리 기준은 포함한다. 인증 토큰 저장과 refresh flow 심화는 Authentication Frontend Flow 문서에서 다룬다.

Q. File Upload도 여기서 다뤄?

A.
기초 input과 FormData 연결은 포함하지만 multipart 업로드 심화는 Data Fetching 또는 File Upload 문서에서 다룬다.

Q. React Hook Form 심화도 여기서 다뤄?

A.
기초 적용 기준과 기본 패턴은 포함하지만 고급 schema resolver, field array 심화는 별도 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

Form Handling & Validation 문서에서는 고급 Form Library 심화와 인증 아키텍처 심화를 제외한다.

제외 범위:

- React Hook Form Advanced
- Zod / Yup Schema 심화
- Field Array 심화
- Wizard Form 심화
- Multi Step Form 심화
- Complex Dynamic Form Builder
- Payment Form 심화
- OAuth2 인증 전체 흐름
- Token Refresh 전체 구현
- File Upload 심화
- Drag and Drop Upload
- Rich Text Editor Form 심화
- Real-time Collaborative Form
- Server-driven Form Schema

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Authentication / File Upload / Advanced Form 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- React Form 기본 구현과 검증 흐름에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
Form Handling & Validation
→ Authentication Frontend Flow
→ File Upload
→ Advanced React Hook Form
→ Frontend Testing
```

---

### [FAQ]

Q. Zod나 Yup도 여기서 깊게 다뤄?

A.
기초 언급은 가능하지만 schema validation 심화는 Advanced Form Validation 문서에서 다룬다.

Q. 결제 Form도 여기서 다뤄?

A.
일반적인 입력 검증 기준은 포함하지만 결제 보안과 PG 연동은 Payment Integration 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Form Handling & Validation RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 Form 적용 기준
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

Q. 모든 Form Handling 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Form Handling 문서에는 입력 흐름과 검증 오류 분석을 위해 추가 Section을 포함할 수 있다.

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

- Submit Flow 설명 → [Flow]
- Controlled Input 설명 → [예제], [주의]
- Validation 설명 → [예제], [Best Practice]
- Server Error 처리 → [Troubleshooting]
- React Hook Form 적용 → [Comparison]
- Form 접근성 검토 → [Checklist]

---

### [실무]

예시:

```md
### [Flow]

User Input
→ onChange
→ Update Form State
→ Client Validation
→ Submit
→ API Request
→ Server Validation
→ Success / Error UI
```

---

### [FAQ]

Q. Form Handling 문서에 Troubleshooting이 중요한 이유는?

A.
input 값이 안 바뀜, submit 시 새로고침, validation error 미표시, 중복 제출 같은 문제가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
Controlled vs Uncontrolled, Client Validation vs Server Validation, useState Form vs React Hook Form처럼 선택 기준이 필요한 경우에 사용한다.

---

# 4. Form Basics Rules

## 4.1 Form Element Rules

### [개념]

Form은 사용자의 입력을 수집하고 제출하는 HTML 요소다.

React에서는 Form 입력값을 State로 관리하고 Submit Event에서 API 요청을 수행하는 방식이 일반적이다.

---

### [핵심]

반드시 설명:

- form
- input
- textarea
- select
- checkbox
- radio
- button type
- onSubmit
- preventDefault
- name
- value
- disabled
- required
- label

---

### [실무]

기본 Form 예:

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

주의:

- submit button은 `type="submit"`
- 일반 button은 `type="button"`
- form submit에는 preventDefault 필요
- label과 input 연결
- 입력값 trim 기준 명확화
- submit handler에서 API 호출 또는 상위 callback 호출

---

### [FAQ]

Q. form submit 시 페이지가 새로고침돼?

A.
기본 form 제출 동작 때문이다. React에서는 onSubmit에서 event.preventDefault를 호출해야 한다.

Q. button type을 꼭 써야 해?

A.
권장한다. form 안의 button은 기본 submit으로 동작할 수 있어 일반 버튼은 `type="button"`을 명시하는 것이 안전하다.

---

## 4.2 Controlled Component Rules

### [개념]

Controlled Component는 input value를 React State로 제어하는 Form 입력 방식이다.

입력값의 원본은 DOM이 아니라 React State다.

---

### [핵심]

필수 포함:

- value
- checked
- onChange
- useState
- Form State
- Controlled Input
- Single Source of Truth
- input value update

---

### [실무]

Text Input 예:

```jsx
function NicknameInput() {
  const [nickname, setNickname] = useState("");

  return (
    <input
      value={nickname}
      onChange={(event) => setNickname(event.target.value)}
    />
  );
}
```

Checkbox 예:

```jsx
function AgreeCheckbox() {
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

- text input은 value 사용
- checkbox / radio는 checked 사용
- value만 있고 onChange가 없으면 읽기 전용처럼 동작
- 초기값을 undefined로 두지 않음
- 문자열 input 초기값은 빈 문자열 권장

---

### [FAQ]

Q. Controlled Component가 뭐야?

A.
입력값을 DOM이 아니라 React State로 관리하는 input 방식이다.

Q. input value는 있는데 입력이 안 돼?

A.
value만 있고 onChange가 없거나 State 업데이트가 되지 않을 가능성이 크다.

Q. checkbox는 value로 제어해?

A.
checkbox는 보통 checked와 event.target.checked로 제어한다.

---

## 4.3 Uncontrolled Component Basics

### [개념]

Uncontrolled Component는 입력값을 React State로 매번 제어하지 않고 DOM 자체가 값을 관리하게 두는 방식이다.

필요할 때 ref나 FormData로 값을 읽을 수 있다.

---

### [핵심]

사용 대상:

- file input
- 간단한 one-time form
- ref based read
- FormData
- external library integration
- performance-sensitive large form basics

---

### [실무]

File Input은 보통 uncontrolled 성격을 가진다.

```jsx
function ImageInput({ onFileSelect }) {
  function handleChange(event) {
    const file = event.target.files?.[0];

    if (file) {
      onFileSelect(file);
    }
  }

  return <input type="file" onChange={handleChange} />;
}
```

주의:

- 일반 text input은 Controlled 방식이 상태 추적에 유리
- file input value는 보안상 직접 제어하기 어려움
- Controlled와 Uncontrolled를 같은 input에서 혼용하지 않음
- Form Library는 내부적으로 uncontrolled 방식을 활용할 수 있음

---

### [FAQ]

Q. Uncontrolled Component는 나쁜 방식이야?

A.
아니다. 파일 입력이나 Form Library 내부 구현처럼 적합한 경우가 있다.

Q. Controlled와 Uncontrolled를 섞어도 돼?

A.
한 input을 두 방식으로 혼용하면 경고와 예측 어려운 동작이 생길 수 있어 피한다.

---

# 5. Form State Rules

## 5.1 Form State Design

### [개념]

Form State는 사용자가 입력한 값과 Form 처리 상태를 관리하는 상태다.

입력값, 에러, 제출 상태, touched, dirty 등을 포함할 수 있다.

---

### [핵심]

Form State 구성:

- values
- errors
- touched
- dirty
- submitting
- submitError
- fieldError
- globalError
- isValid
- canSubmit

---

### [실무]

단순 Form State 예:

```jsx
function LoginForm({ onLogin }) {
  const [values, setValues] = useState({
    email: "",
    password: "",
  });

  function handleChange(event) {
    const { name, value } = event.target;

    setValues((prevValues) => ({
      ...prevValues,
      [name]: value,
    }));
  }

  return (
    <>
      <input name="email" value={values.email} onChange={handleChange} />
      <input name="password" value={values.password} onChange={handleChange} />
    </>
  );
}
```

권장:

- 입력값과 에러 상태를 구분
- Form이 커지면 values 객체 사용
- name 속성과 state key 일치
- 서버 요청용 DTO 변환 함수 분리 가능
- 불필요한 전역 상태화 금지

---

### [FAQ]

Q. Form 입력값은 각각 useState로 둬야 해, 객체로 둬야 해?

A.
입력값이 적으면 각각 useState도 가능하고, 필드가 많으면 values 객체로 관리하는 것이 편할 수 있다.

Q. Form State를 전역 상태로 둬도 돼?

A.
대부분 권장하지 않는다. Form 내부 임시 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

---

## 5.2 Field State Rules

### [개념]

Field State는 개별 입력 필드의 값, 에러, 방문 여부, 수정 여부를 나타내는 상태다.

---

### [핵심]

Field State 종류:

- value
- error
- touched
- dirty
- focused
- disabled
- required
- valid
- invalid

---

### [실무]

에러 표시 기준:

```jsx
function FieldError({ message }) {
  if (!message) {
    return null;
  }

  return <p role="alert">{message}</p>;
}
```

Field 구성 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  value={values.email}
  onChange={handleChange}
  onBlur={handleBlur}
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

- 에러 메시지는 input 근처에 표시
- touched 이후 에러 표시 가능
- aria-invalid와 aria-describedby 연결
- 필수값 표시 기준 통일
- 서버 field error와 client field error 통합 기준 마련

---

### [FAQ]

Q. touched는 뭐야?

A.
사용자가 해당 필드를 방문하거나 blur한 적이 있는지를 나타내는 상태다.

Q. dirty는 뭐야?

A.
초기값과 현재 입력값이 달라졌는지를 나타내는 상태다.

Q. 에러 메시지는 언제 보여줘?

A.
보통 submit 후 또는 touched 이후 보여주는 방식이 사용자 경험에 좋다.

---

## 5.3 Form State Location Rules

### [개념]

Form State Location은 Form 입력값과 에러 상태를 어느 Component가 소유할지 결정하는 기준이다.

---

### [핵심]

위치 기준:

- 단일 Form 내부에서만 필요 → Form Component
- 부모가 제출 결과만 필요 → callback props
- 여러 Step에서 공유 → 공통 부모 또는 Form Context
- URL 공유 필요 → URL State
- 서버 저장 값 → Server State
- 여러 페이지 임시 저장 → 전역 상태 검토

---

### [실무]

권장 Flow:

```text
Identify Form Fields
→ Check Usage Scope
→ Keep Local if Single Form
→ Lift Up if Shared
→ Use URL for Shareable Filters
→ Use Form Library if Complex
```

예:

```text
SearchForm 입력 중 keyword → Local State
검색 submit 후 keyword → URL Search Params
ReviewForm content/rating → ReviewForm Local State
회원가입 여러 Step 입력값 → 공통 부모 또는 Form Library
```

주의:

- Form 입력값을 무조건 Global Store에 넣지 않음
- 검색 조건은 제출 후 URL State로 옮길 수 있음
- 서버 응답 데이터와 Form 임시값 구분
- 편집 Form 초기값과 입력값 구분

---

### [FAQ]

Q. 검색 Form 입력값은 어디에 둬?

A.
입력 중 임시값은 Local State로 두고, 제출된 검색 조건은 URL Query String으로 관리할 수 있다.

Q. 수정 Form의 초기값은 Server State야 Form State야?

A.
서버에서 받은 초기값은 Server State이고 사용자가 수정 중인 값은 Form State다.

---

# 6. Input Handling Rules

## 6.1 Common Change Handler

### [개념]

Common Change Handler는 여러 input의 onChange를 하나의 함수로 처리하는 패턴이다.

name 속성과 values key를 맞춰 사용한다.

---

### [핵심]

필수 포함:

- name
- value
- checked
- event.target
- computed property name
- text input
- checkbox handling
- select handling

---

### [실무]

기본 예:

```jsx
function handleChange(event) {
  const { name, value } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));
}
```

Checkbox 포함 예:

```jsx
function handleChange(event) {
  const { name, type, value, checked } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: type === "checkbox" ? checked : value,
  }));
}
```

주의:

- input name과 values key 일치
- checkbox는 checked 사용
- number input도 value는 문자열로 들어올 수 있음
- select multiple은 별도 처리
- nested field는 별도 helper 필요 가능

---

### [FAQ]

Q. 여러 input을 하나의 handleChange로 처리할 수 있어?

A.
가능하다. input name과 values 객체 key를 맞추면 공통 handler로 처리할 수 있다.

Q. number input 값은 number로 들어와?

A.
대부분 문자열로 들어온다. 숫자가 필요하면 Number 변환과 NaN 검증이 필요하다.

---

## 6.2 Select / Checkbox / Radio Rules

### [개념]

Select, Checkbox, Radio는 입력 방식에 따라 value / checked 처리 기준이 다르다.

---

### [핵심]

처리 기준:

- select: value
- checkbox: checked
- radio: checked + value
- multiple select: selected options
- boolean field
- enum field
- array field

---

### [실무]

Select 예:

```jsx
<select name="regionCode" value={values.regionCode} onChange={handleChange}>
  <option value="">전체</option>
  <option value="11">서울</option>
</select>
```

Radio 예:

```jsx
<label>
  <input
    type="radio"
    name="gender"
    value="MALE"
    checked={values.gender === "MALE"}
    onChange={handleChange}
  />
  남성
</label>
```

Checkbox 예:

```jsx
<label>
  <input
    type="checkbox"
    name="agreed"
    checked={values.agreed}
    onChange={handleChange}
  />
  약관 동의
</label>
```

주의:

- checkbox는 value가 아니라 checked 기준
- radio group은 같은 name 사용
- select option value와 Backend enum / code 값 일치
- 빈 option 값 처리 기준 필요

---

### [FAQ]

Q. checkbox 값은 event.target.value로 읽어?

A.
보통 checked를 사용한다. value는 checkbox의 선택 여부가 아니라 value 속성값이다.

Q. radio button은 어떻게 제어해?

A.
같은 name을 가진 radio들 중 현재 값과 value가 일치하는 항목에 checked를 설정한다.

---

## 6.3 File Input Rules

### [개념]

File Input은 사용자가 파일을 선택하는 input이다.

파일은 일반 JSON이 아니라 File 객체나 FormData로 처리한다.

---

### [핵심]

필수 포함:

- input type file
- File
- FileList
- FormData
- accept
- multiple
- preview
- file size validation
- file type validation
- object URL cleanup

---

### [실무]

기본 예:

```jsx
function ImageUploader({ onUpload }) {
  const [previewUrl, setPreviewUrl] = useState("");

  function handleFileChange(event) {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    const nextPreviewUrl = URL.createObjectURL(file);
    setPreviewUrl(nextPreviewUrl);
    onUpload(file);
  }

  return (
    <>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {previewUrl && <img src={previewUrl} alt="미리보기" />}
    </>
  );
}
```

주의:

- 파일 크기 제한
- 파일 확장자 / MIME type 검증
- 미리보기 object URL 정리 필요
- FormData key와 Backend field name 일치
- 민감 파일 업로드 주의
- 보안 검증은 Backend에서도 필수

---

### [FAQ]

Q. 파일 input도 value로 제어해?

A.
일반적으로 파일 input은 value로 제어하지 않고 files를 읽어서 처리한다.

Q. 이미지 미리보기 URL은 정리해야 해?

A.
URL.createObjectURL을 사용했다면 필요 없어진 시점에 URL.revokeObjectURL로 정리하는 것이 좋다.

---

# 7. Validation Rules

## 7.1 Client Validation Rules

### [개념]

Client Validation은 사용자가 Form을 제출하기 전에 브라우저에서 입력값을 검증하는 과정이다.

Client Validation은 사용자 경험을 개선하지만 최종 검증은 Backend에서 수행해야 한다.

---

### [핵심]

검증 대상:

- required
- min length
- max length
- email format
- password confirm
- number range
- date range
- checkbox required
- file size
- file type
- trim
- forbidden characters

---

### [실무]

예:

```javascript
function validateReview(values) {
  const errors = {};

  if (!values.content.trim()) {
    errors.content = "리뷰 내용을 입력해 주세요.";
  }

  if (values.rating < 1 || values.rating > 5) {
    errors.rating = "평점은 1점에서 5점 사이여야 합니다.";
  }

  return errors;
}
```

Submit 적용:

```javascript
function handleSubmit(event) {
  event.preventDefault();

  const nextErrors = validateReview(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  onSubmit(values);
}
```

권장:

- submit 전 validation 수행
- 에러 객체로 field별 메시지 관리
- trim 기준 명확화
- 필수값과 형식 검증 분리
- Client Validation은 UX용
- Server Validation은 반드시 필요

---

### [FAQ]

Q. Client Validation이 있으면 Server Validation은 없어도 돼?

A.
안 된다. Client Validation은 우회될 수 있으므로 Backend 검증이 반드시 필요하다.

Q. Validation 함수는 Component 안에 둬도 돼?

A.
간단한 Form은 가능하지만 재사용되거나 복잡하면 별도 함수로 분리하는 것이 좋다.

---

## 7.2 Required and Length Validation

### [개념]

Required Validation은 필수 입력 여부를 확인하고 Length Validation은 문자열 길이 제한을 확인한다.

---

### [핵심]

필수 포함:

- required
- trim
- minLength
- maxLength
- empty string
- whitespace
- character count
- validation message

---

### [실무]

예:

```javascript
function validateTitle(title) {
  const trimmedTitle = title.trim();

  if (!trimmedTitle) {
    return "제목을 입력해 주세요.";
  }

  if (trimmedTitle.length > 50) {
    return "제목은 50자 이하로 입력해 주세요.";
  }

  return "";
}
```

주의:

- 공백만 입력한 경우 empty로 처리할지 결정
- Backend length 제한과 Frontend 제한 일치
- textarea 글자 수 표시 가능
- 다국어 글자 수 기준 주의
- DB 컬럼 길이와 DTO validation 기준 확인

---

### [FAQ]

Q. 공백만 입력해도 값이 있는 걸로 봐?

A.
대부분 trim 후 빈 문자열이면 입력하지 않은 것으로 처리한다.

Q. Frontend maxLength와 Backend 제한이 다르면?

A.
Backend 기준이 최종이므로 Frontend 제한을 Backend와 맞춰야 한다.

---

## 7.3 Format Validation

### [개념]

Format Validation은 email, phone, password, date 같은 입력값이 정해진 형식에 맞는지 확인하는 검증이다.

---

### [핵심]

사용 대상:

- email
- phone
- password
- url
- date
- time
- number
- code
- nickname
- username

---

### [실무]

Email 기초 예:

```javascript
function validateEmail(email) {
  const trimmedEmail = email.trim();

  if (!trimmedEmail) {
    return "이메일을 입력해 주세요.";
  }

  if (!trimmedEmail.includes("@")) {
    return "이메일 형식이 올바르지 않습니다.";
  }

  return "";
}
```

주의:

- 지나치게 복잡한 정규식 지양
- 최종 형식 검증은 Backend 기준
- password 정책은 Backend와 일치
- phone format은 국가 / 서비스 기준 확인
- 날짜는 timezone과 format 기준 확인

---

### [FAQ]

Q. 이메일 검증은 정규식으로 완벽하게 해야 해?

A.
완벽한 이메일 정규식보다 기본 형식 확인과 Backend 검증을 함께 사용하는 것이 실용적이다.

Q. 비밀번호 정책은 어디 기준으로 맞춰?

A.
Backend Validation 정책과 동일하게 맞춰야 한다.

---

## 7.4 Cross Field Validation

### [개념]

Cross Field Validation은 여러 필드 값을 함께 비교해 검증하는 방식이다.

예:

- password와 confirmPassword 일치
- startDate와 endDate 순서
- minPrice와 maxPrice 범위
- 체크박스 동의 여부

---

### [핵심]

사용 대상:

- password confirm
- date range
- number range
- dependent select
- agreement checkbox
- conditional required field

---

### [실무]

비밀번호 확인 예:

```javascript
function validateSignup(values) {
  const errors = {};

  if (values.password !== values.confirmPassword) {
    errors.confirmPassword = "비밀번호가 일치하지 않습니다.";
  }

  return errors;
}
```

날짜 범위 예:

```javascript
function validateDateRange(values) {
  const errors = {};

  if (values.startDate && values.endDate && values.startDate > values.endDate) {
    errors.endDate = "종료일은 시작일 이후여야 합니다.";
  }

  return errors;
}
```

주의:

- 관련 필드 중 하나가 비어 있을 때 처리 기준 필요
- 에러를 어느 필드에 표시할지 결정
- submit 시 전체 검증 필요
- 입력 중 실시간 검증은 UX 고려

---

### [FAQ]

Q. 비밀번호 확인 검증은 어디에 표시해?

A.
보통 confirmPassword 필드 근처에 표시한다.

Q. 날짜 범위 검증은 문자열 비교로 해도 돼?

A.
ISO 형식 날짜 문자열이면 가능할 수 있지만 명확한 Date 변환 기준을 두는 것이 안전하다.

---

# 8. Server Validation Rules

## 8.1 Server Validation Error Handling

### [개념]

Server Validation Error는 Backend가 요청 데이터를 검증한 뒤 실패 결과를 Frontend에 반환하는 오류다.

Frontend는 이를 Field Error 또는 Global Error로 표시한다.

---

### [핵심]

필수 포함:

- server validation
- field errors
- global error
- 400
- 422
- duplicate error
- backend message
- request body
- validation response mapping

---

### [실무]

Backend 응답 예:

```json
{
  "success": false,
  "message": "검증 실패",
  "errors": {
    "email": "이미 사용 중인 이메일입니다.",
    "nickname": "닉네임은 2자 이상이어야 합니다."
  }
}
```

Frontend 처리 예:

```javascript
function mapServerErrors(error) {
  if (!axios.isAxiosError(error)) {
    return {};
  }

  return error.response?.data?.errors ?? {};
}
```

권장:

- field별 error는 해당 field 근처에 표시
- global error는 form 상단에 표시
- 서버 메시지 구조를 타입으로 정의
- client error와 server error 통합 기준 마련
- submit 실패 후 입력값 유지
- 재입력 시 해당 field error 초기화 가능

---

### [FAQ]

Q. Server Validation Error는 어디에 보여줘?

A.
필드별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시한다.

Q. 서버가 준 에러 메시지를 그대로 보여줘도 돼?

A.
서비스 정책에 따라 가능하지만 민감한 내부 정보가 포함되지 않도록 Backend 응답 메시지를 관리해야 한다.

---

## 8.2 Client Validation vs Server Validation

### [개념]

Client Validation은 브라우저에서 사용자 입력을 사전 검증하는 UX용 검증이다.

Server Validation은 Backend에서 실제 데이터를 보호하기 위한 최종 검증이다.

---

### [핵심]

비교:

| 비교        | Client Validation | Server Validation    |
| ----------- | ----------------- | -------------------- |
| 위치        | Frontend          | Backend              |
| 목적        | UX 개선           | 데이터 무결성 / 보안 |
| 우회 가능성 | 가능              | 최종 기준            |
| 속도        | 빠름              | 네트워크 필요        |
| 예          | 빈 값, 형식       | 중복, 권한, DB 기준  |
| 필수 여부   | 권장              | 필수                 |

---

### [실무]

권장 Flow:

```text
User Input
→ Client Validation
→ If Valid
→ API Request
→ Server Validation
→ Success or Server Error Mapping
→ UI Update
```

주의:

- Client Validation만 믿지 않음
- Backend Validation과 규칙 일치
- 중복 이메일 / 중복 닉네임은 서버 검증 필요
- 권한 / 소유자 검증은 서버 필수
- Frontend는 사용자 경험 개선 역할

---

### [FAQ]

Q. Client Validation만 있으면 충분해?

A.
아니다. 사용자가 우회할 수 있으므로 Backend Validation이 최종 기준이다.

Q. 중복 이메일 검사는 Frontend에서 할 수 있어?

A.
입력 형식 검사는 Frontend에서 가능하지만 실제 중복 여부는 서버에 확인해야 한다.

---

# 9. Submit Flow Rules

## 9.1 Form Submit Flow

### [개념]

Form Submit Flow는 사용자가 Form을 제출했을 때 검증, API 요청, 성공 처리, 실패 처리를 수행하는 흐름이다.

---

### [핵심]

기본 Flow:

```text
Submit Event
→ preventDefault
→ Clear Previous Errors
→ Client Validation
→ If Invalid Stop
→ Set Submitting True
→ Build Request Body
→ API Request
→ Handle Success
→ Handle Server Error
→ Set Submitting False
```

---

### [실무]

예:

```jsx
async function handleSubmit(event) {
  event.preventDefault();

  setErrors({});
  setSubmitError("");

  const nextErrors = validateReview(values);
  setErrors(nextErrors);

  if (Object.keys(nextErrors).length > 0) {
    return;
  }

  setSubmitting(true);

  try {
    await createReview({
      festivalId,
      rating: values.rating,
      content: values.content.trim(),
    });

    resetForm();
  } catch (error) {
    setErrors(mapServerErrors(error));
    setSubmitError(getApiErrorMessage(error));
  } finally {
    setSubmitting(false);
  }
}
```

권장:

- 이전 에러 초기화
- Client Validation 먼저 수행
- Request Body 생성 기준 명확화
- submitting 상태로 중복 제출 방지
- 성공 후 reset 또는 이동 기준 결정
- 실패 후 입력값 유지
- finally에서 submitting false 처리

---

### [FAQ]

Q. Submit 전에 에러를 초기화해야 해?

A.
권장한다. 이전 제출의 에러가 남아 현재 상태와 맞지 않을 수 있기 때문이다.

Q. Submit 실패 후 입력값은 지워야 해?

A.
보통 지우지 않는다. 사용자가 수정 후 다시 제출할 수 있도록 유지하는 것이 좋다.

---

## 9.2 Duplicate Submit Prevention

### [개념]

Duplicate Submit Prevention은 사용자가 버튼을 여러 번 눌러 같은 요청이 중복 전송되는 것을 방지하는 기준이다.

---

### [핵심]

방지 방법:

- submitting state
- button disabled
- loading indicator
- debounce basics
- idempotency basics
- server duplicate prevention
- mutation pending

---

### [실무]

예:

```jsx
<button type="submit" disabled={submitting}>
  {submitting ? "저장 중..." : "저장"}
</button>
```

권장:

- 제출 중 submit 버튼 disabled
- API 요청 중 중복 클릭 방지
- mutation pending 상태 활용
- 서버에서도 중복 처리 기준 필요
- 결제 / 주문 / 후원 요청은 특히 주의

주의:

- Frontend disabled만으로 중복 제출을 완전히 막을 수 없음
- 중요한 요청은 Backend idempotency 또는 중복 검증 필요
- 실패 시 다시 제출 가능하게 상태 복구

---

### [FAQ]

Q. 버튼 disabled만 하면 중복 제출이 완전히 막혀?

A.
아니다. UX상 중복 클릭을 줄일 수 있지만 중요한 요청은 Backend에서도 중복 방지 기준이 필요하다.

Q. 제출 중 버튼 문구를 바꿔야 해?

A.
권장한다. 사용자가 현재 처리 중임을 알 수 있다.

---

## 9.3 Form Reset Rules

### [개념]

Form Reset은 제출 성공, 취소, 초기화 버튼 클릭 후 Form State를 초기값으로 되돌리는 작업이다.

---

### [핵심]

초기화 대상:

- values
- errors
- touched
- dirty
- submitError
- file input
- preview url
- server errors
- submitting state

---

### [실무]

예:

```javascript
const initialValues = {
  content: "",
  rating: 5,
};

function resetForm() {
  setValues(initialValues);
  setErrors({});
  setSubmitError("");
}
```

사용 기준:

- 생성 Form 성공 후 reset 가능
- 수정 Form 성공 후 서버 최신값 반영
- 취소 버튼 클릭 시 초기값으로 복원
- 검색 Form reset 시 URL Search Params도 초기화 가능
- file preview 정리 필요

주의:

- 수정 Form은 최초 서버 데이터와 reset 기준 구분
- 파일 input은 별도 ref 필요 가능
- reset 후 focus 처리 고려
- 성공 후 페이지 이동이면 reset 불필요할 수 있음

---

### [FAQ]

Q. Form 제출 성공 후 항상 reset해야 해?

A.
항상은 아니다. 리뷰 작성처럼 새 입력을 받는 Form은 reset하고, 수정 Form은 최신 서버 값으로 갱신하는 것이 좋다.

Q. 검색 Form reset은 URL도 같이 초기화해야 해?

A.
검색 조건을 URL State로 관리한다면 URL Search Params도 함께 초기화해야 한다.

---

# 10. Request Body Mapping Rules

## 10.1 Form Values to Request DTO

### [개념]

Request Body Mapping은 Form State를 Backend가 요구하는 Request DTO 구조로 변환하는 과정이다.

---

### [핵심]

필수 포함:

- form values
- request dto
- trim
- type conversion
- date format
- enum value
- boolean value
- file data
- null handling
- optional field

---

### [실무]

Form Values:

```javascript
const values = {
  rating: "5",
  content: " 좋았어요 ",
};
```

Request DTO:

```javascript
const requestBody = {
  rating: Number(values.rating),
  content: values.content.trim(),
};
```

권장:

- 화면용 Form State와 API Request Body 구분
- trim 적용 기준 명확화
- 숫자 문자열 변환
- 빈 문자열을 null로 보낼지 생략할지 결정
- Backend DTO 필드명과 일치
- 날짜 format 통일
- enum / code 값 일치

---

### [FAQ]

Q. Form State를 그대로 API body로 보내도 돼?

A.
간단한 경우 가능하지만 trim, type conversion, field name mapping이 필요하면 Request DTO로 변환하는 것이 좋다.

Q. 숫자 input 값은 변환해야 해?

A.
대부분 문자열로 들어오므로 Backend가 숫자를 기대하면 Number 변환과 검증이 필요하다.

---

## 10.2 Request DTO Type Rules

### [개념]

Request DTO Type은 Backend API에 보낼 요청 Body 구조를 TypeScript 타입으로 정의하는 방식이다.

---

### [핵심]

필수 포함:

- Request Type
- Form Values Type
- Response Type
- Params Type
- optional field
- nullable field
- enum union
- Backend DTO matching

---

### [실무]

예:

```typescript
type ReviewFormValues = {
  rating: string;
  content: string;
};

type CreateReviewRequest = {
  festivalId: number;
  rating: number;
  content: string;
};

function toCreateReviewRequest(
  festivalId: number,
  values: ReviewFormValues,
): CreateReviewRequest {
  return {
    festivalId,
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}
```

권장:

- Form Values Type과 Request Type 분리
- 변환 함수 작성 가능
- API 함수 parameter는 Request Type 사용
- Backend DTO와 필드명 동기화
- any 사용 지양

---

### [FAQ]

Q. Form Values Type과 Request Type을 왜 나눠?

A.
input 값은 문자열일 수 있지만 Backend Request는 number, boolean, enum 등 다른 타입을 요구할 수 있기 때문이다.

Q. 변환 함수는 왜 필요해?

A.
trim, Number 변환, null 처리, 필드명 mapping을 일관되게 처리하기 위해 필요하다.

---

# 11. React Hook Form Rules

## 11.1 React Hook Form Use Criteria

### [개념]

React Hook Form은 React Form 상태와 검증을 효율적으로 관리하기 위한 라이브러리다.

필드 수가 많거나 검증이 복잡한 Form에서 유용하다.

---

### [핵심]

사용 기준:

- field count 많음
- validation 복잡
- touched / dirty 관리 필요
- error handling 많음
- performance concern
- reusable form field 필요
- schema validation 연동 필요
- uncontrolled 기반 효율성

---

### [실무]

React Hook Form 검토 상황:

```text
간단한 검색 Form → useState 가능
간단한 리뷰 Form → useState 가능
회원가입 Form + 여러 validation → React Hook Form 검토
관리자 등록 Form + 필드 다수 → React Hook Form 검토
동적 필드 Form → React Hook Form 심화 검토
```

주의:

- 라이브러리 도입 비용 고려
- 팀 컨벤션 확인
- 작은 Form에 과도한 도입 지양
- schema validation은 별도 기준 필요
- Server Error mapping 기준 마련

---

### [FAQ]

Q. React Hook Form은 언제 써?

A.
입력 필드가 많고 검증, touched, dirty, error 상태 관리가 복잡해질 때 검토한다.

Q. 간단한 Form에도 React Hook Form을 써야 해?

A.
필수는 아니다. 간단한 검색 Form이나 작은 입력 Form은 useState로 충분할 수 있다.

---

## 11.2 React Hook Form Basics

### [개념]

React Hook Form은 register, handleSubmit, formState를 사용해 Form 입력과 검증을 관리한다.

---

### [핵심]

필수 키워드:

- useForm
- register
- handleSubmit
- formState
- errors
- reset
- setError
- watch
- defaultValues
- Controller basics

---

### [실무]

기초 예:

```tsx
function ReviewForm({ onSubmit }) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm({
    defaultValues: {
      content: "",
      rating: 5,
    },
  });

  async function submitForm(values) {
    await onSubmit(values);
    reset();
  }

  return (
    <form onSubmit={handleSubmit(submitForm)}>
      <textarea
        {...register("content", {
          required: "리뷰 내용을 입력해 주세요.",
        })}
      />
      {errors.content && <p role="alert">{errors.content.message}</p>}

      <button type="submit" disabled={isSubmitting}>
        저장
      </button>
    </form>
  );
}
```

주의:

- register name과 type key 일치
- defaultValues 설정
- errors 표시 위치 명확화
- server error는 setError로 연결 가능
- 외부 controlled component는 Controller 필요 가능
- 상세 심화는 별도 문서로 분리

---

### [FAQ]

Q. register는 뭐야?

A.
input을 React Hook Form에 등록해 값과 검증 규칙을 관리하게 하는 함수다.

Q. handleSubmit은 preventDefault를 대신 해?

A.
React Hook Form의 handleSubmit은 form submit 기본 동작을 처리하고 검증 후 submit 함수를 호출한다.

Q. 서버 에러는 React Hook Form에 어떻게 넣어?

A.
setError를 사용해 field error 또는 root error로 연결할 수 있다.

---

# 12. Form Accessibility Rules

## 12.1 Label and Input Accessibility

### [개념]

Form Accessibility는 사용자가 키보드, 스크린 리더 등 다양한 방식으로 Form을 사용할 수 있게 하는 기준이다.

---

### [핵심]

필수 포함:

- label
- htmlFor
- id
- aria-invalid
- aria-describedby
- role alert
- required indication
- fieldset
- legend
- keyboard navigation
- focus management

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
- error message와 input 연결
- 필수 입력 표시 제공
- submit 실패 시 첫 에러 field로 focus 이동 고려
- radio / checkbox group에는 fieldset / legend 고려

---

### [FAQ]

Q. placeholder만 있으면 label은 없어도 돼?

A.
권장하지 않는다. placeholder는 입력 중 사라지고 접근성 측면에서 label을 대체하기 어렵다.

Q. 에러 메시지는 input과 연결해야 해?

A.
권장한다. aria-describedby로 input과 에러 메시지를 연결하면 스크린 리더 사용자가 오류를 이해하기 쉽다.

---

## 12.2 Focus Management Rules

### [개념]

Focus Management는 Form 제출 실패, Modal Form, Step Form 등에서 사용자의 키보드 초점을 적절히 이동시키는 기준이다.

---

### [핵심]

사용 상황:

- submit validation failed
- modal open
- modal close
- first invalid field
- success message
- dynamic field added
- keyboard navigation

---

### [실무]

권장:

- submit 실패 시 첫 번째 invalid field로 focus 이동 고려
- Modal Form 열릴 때 첫 입력 또는 제목으로 focus 이동
- Modal 닫힐 때 trigger button으로 focus 복귀
- disabled field는 focus 대상에서 제외
- 에러 메시지만 보여주고 focus를 방치하지 않음

주의:

- focus 이동 남용 금지
- 사용자가 입력 중인 focus를 불필요하게 빼앗지 않음
- Custom Component는 ref 전달 필요 가능
- 상세 구현은 Accessibility 문서에서 심화

---

### [FAQ]

Q. Submit 실패 시 focus를 이동해야 해?

A.
필수는 아니지만 첫 오류 field로 이동하면 사용자가 문제를 빠르게 수정할 수 있다.

Q. Modal Form에서는 focus를 어떻게 해?

A.
열릴 때 Modal 내부로 focus를 이동하고 닫힐 때 이전 trigger로 복귀하는 것이 좋다.

---

# 13. Form Component Design Rules

## 13.1 Form Component Separation

### [개념]

Form Component Separation은 Form 전체, Field, Error Message, Submit Button, API 처리 로직을 적절히 분리하는 설계 기준이다.

---

### [핵심]

분리 대상:

- Form Container
- Field Component
- Error Message Component
- Submit Button
- Validation Function
- Request Mapping Function
- API Function
- Form Hook

---

### [실무]

기본 구조:

```text
ReviewForm
├ ReviewRatingField
├ ReviewContentField
├ FieldError
└ SubmitButton
```

파일 구조 예:

```text
src
├ features
│  └ review
│     ├ components
│     │  ├ ReviewForm.tsx
│     │  └ ReviewContentField.tsx
│     ├ validators
│     │  └ reviewValidator.ts
│     ├ mappers
│     │  └ reviewMapper.ts
│     └ api
│        └ reviewApi.ts
```

권장:

- 작은 Form은 한 파일 가능
- 검증이 길어지면 validator 분리
- Request DTO 변환이 있으면 mapper 분리
- 반복 Field UI는 Field Component로 분리
- API 함수는 api layer로 분리
- 제출 성공 / 실패 처리는 Form 책임으로 유지 가능

---

### [FAQ]

Q. Form Component는 언제 분리해?

A.
필드가 많아지거나 검증/에러/제출 로직이 길어지면 Field, Validator, Mapper, API 함수로 분리한다.

Q. Validation 함수는 어디에 둬?

A.
단순하면 Component 안에 둘 수 있고 복잡하거나 재사용되면 validators 파일로 분리한다.

---

## 13.2 Field Component Rules

### [개념]

Field Component는 label, input, error message를 하나의 재사용 가능한 단위로 묶은 Component다.

---

### [핵심]

포함 요소:

- label
- input
- id
- name
- value
- onChange
- error
- required
- disabled
- aria-invalid
- aria-describedby

---

### [실무]

예:

```tsx
type TextFieldProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  error?: string;
  required?: boolean;
  disabled?: boolean;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
};

function TextField({
  id,
  name,
  label,
  value,
  error,
  required = false,
  disabled = false,
  onChange,
}: TextFieldProps) {
  const errorId = `${id}-error`;

  return (
    <div className="form-field">
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        name={name}
        value={value}
        required={required}
        disabled={disabled}
        onChange={onChange}
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : undefined}
      />
      {error && (
        <p id={errorId} role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
```

주의:

- 범용 Field와 도메인 Field 구분
- 모든 input type을 하나의 Field로 무리하게 통합하지 않음
- error 접근성 연결
- id 중복 방지
- React Hook Form register와 결합 시 props 설계 주의

---

### [FAQ]

Q. Field Component는 왜 만들어?

A.
label, input, error message, 접근성 속성을 반복하지 않고 일관되게 관리하기 위해 만든다.

Q. 모든 input을 하나의 TextField로 처리해도 돼?

A.
text 계열은 가능하지만 checkbox, radio, file, custom select는 별도 Component가 더 명확할 수 있다.

---

# 14. Search Form Rules

## 14.1 Search Form Handling

### [개념]

Search Form은 사용자가 입력한 검색 조건을 기준으로 목록 데이터를 조회하는 Form이다.

입력 중 임시값과 제출된 검색 조건을 구분할 수 있다.

---

### [핵심]

필수 포함:

- keyword
- filter
- submit
- reset
- URL Search Params
- page reset
- debounce basics
- empty query
- query param mapping

---

### [실무]

권장 Flow:

```text
User Typing
→ Local Form State
→ Submit
→ Trim Keyword
→ Update URL Search Params
→ Reset Page
→ Fetch List
```

예:

```jsx
function FestivalSearchForm({ initialKeyword, onSearch }) {
  const [keyword, setKeyword] = useState(initialKeyword);

  function handleSubmit(event) {
    event.preventDefault();
    onSearch(keyword.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <button type="submit">검색</button>
    </form>
  );
}
```

주의:

- 검색 submit 시 page reset
- 빈 검색어 처리 기준 결정
- URL Search Params와 input state 동기화
- 실시간 검색이면 debounce 고려
- Enter key submit 고려
- 검색 조건 reset 제공 가능

---

### [FAQ]

Q. 검색어 입력 중에도 바로 API 호출해야 해?

A.
필수는 아니다. 검색 버튼 submit 방식이 단순하고, 실시간 검색이 필요하면 debounce를 적용한다.

Q. 검색 조건이 바뀌면 page를 reset해야 해?

A.
대부분 그렇다. 기존 page가 새 검색 결과 범위를 벗어날 수 있기 때문이다.

---

# 15. Authentication Form Rules

## 15.1 Login Form Rules

### [개념]

Login Form은 사용자 인증 정보를 입력받아 로그인 API를 호출하는 Form이다.

---

### [핵심]

필수 포함:

- email / username
- password
- client validation
- submit loading
- login API
- global error
- field error
- token handling basics
- redirect after login
- security caution

---

### [실무]

Login Flow:

```text
Input Email / Password
→ Client Validation
→ Login API Request
→ Success
→ Store Auth Result
→ Redirect
→ Failure
→ Show Global Error
```

주의:

- password console.log 금지
- 로그인 실패 메시지는 과도하게 구체적이지 않게 처리 가능
- submit 중 버튼 disabled
- 401 처리 기준
- 로그인 성공 후 redirect 기준
- token 저장과 refresh는 Authentication 문서에서 심화
- 브라우저 자동완성 고려

---

### [FAQ]

Q. 로그인 실패 에러는 field error야 global error야?

A.
이메일 형식 오류는 field error이고, 계정 정보가 일치하지 않음 같은 인증 실패는 global error로 처리하는 경우가 많다.

Q. password를 console.log로 확인해도 돼?

A.
안 된다. 민감정보는 로그에 남기지 않는 것이 원칙이다.

---

## 15.2 Signup Form Rules

### [개념]

Signup Form은 회원가입에 필요한 여러 입력값과 검증 규칙을 처리하는 Form이다.

---

### [핵심]

필수 포함:

- email
- password
- confirmPassword
- nickname
- required
- format validation
- duplicate check
- agreement checkbox
- server validation
- submit loading

---

### [실무]

Signup Validation 대상:

- 이메일 형식
- 이메일 중복
- 비밀번호 길이 / 형식
- 비밀번호 확인 일치
- 닉네임 길이
- 필수 약관 동의
- 서버 검증 에러

주의:

- 중복 검사는 서버 요청 필요
- password 정책은 Backend와 일치
- 약관 동의 checkbox는 checked로 관리
- 서버 검증 실패 시 field error 표시
- 회원가입 성공 후 로그인 페이지 이동 또는 자동 로그인 기준 결정

---

### [FAQ]

Q. 이메일 중복 검사는 Frontend에서만 가능해?

A.
아니다. 실제 중복 여부는 서버 데이터 기준이므로 Backend API 확인이 필요하다.

Q. 회원가입 Form은 useState로 충분해?

A.
필드와 검증이 많다면 React Hook Form이나 schema validation 도입을 검토할 수 있다.

---

# 16. Troubleshooting Rules

## 16.1 Input Not Updating

### [개념]

Input Not Updating은 사용자가 입력해도 input 값이 바뀌지 않는 문제다.

---

### [핵심]

원인:

- value만 있고 onChange 없음
- onChange에서 setState 미호출
- name과 state key 불일치
- disabled 상태
- readOnly 상태
- State 초기값 undefined
- Controlled / Uncontrolled 혼용

---

### [실무]

Debug Flow:

```text
Input value 확인
→ onChange 연결 확인
→ setState 호출 확인
→ event.target.name 확인
→ state key 확인
→ disabled / readOnly 확인
→ Console warning 확인
```

나쁜 예:

```jsx
<input value={values.email} />
```

좋은 예:

```jsx
<input name="email" value={values.email} onChange={handleChange} />
```

---

### [FAQ]

Q. input에 입력이 안 되는 이유는?

A.
value는 설정했지만 onChange로 State를 업데이트하지 않았을 가능성이 크다.

Q. name과 state key가 다르면 어떻게 돼?

A.
공통 handleChange에서 잘못된 key가 업데이트되어 input 값이 바뀌지 않을 수 있다.

---

## 16.2 Form Refresh Problem

### [개념]

Form Refresh Problem은 Form 제출 시 페이지가 새로고침되는 문제다.

---

### [핵심]

원인:

- preventDefault 누락
- form onSubmit 미사용
- button type 혼동
- submit event 처리 위치 오류
- native form action 사용

---

### [실무]

나쁜 예:

```jsx
function handleSubmit() {
  createReview(values);
}
```

좋은 예:

```jsx
function handleSubmit(event) {
  event.preventDefault();
  createReview(values);
}
```

주의:

- form에는 onSubmit 사용
- submit button에는 type submit 사용
- 일반 button에는 type button 사용
- Enter key submit도 고려

---

### [FAQ]

Q. Form 제출하면 화면이 새로고침돼?

A.
event.preventDefault를 호출하지 않아 브라우저 기본 submit 동작이 실행된 것이다.

Q. onClick으로 submit 처리해도 돼?

A.
가능하지만 form onSubmit을 사용하는 것이 Enter key 제출과 접근성 측면에서 더 좋다.

---

## 16.3 Validation Error Not Showing

### [개념]

Validation Error Not Showing은 검증 실패는 발생했지만 사용자에게 에러 메시지가 표시되지 않는 문제다.

---

### [핵심]

원인:

- errors state 업데이트 누락
- error key와 field name 불일치
- 조건부 렌더링 조건 오류
- server error mapping 실패
- touched 조건 때문에 숨김
- role / aria 연결 누락
- submit 후 return 누락

---

### [실무]

Debug Flow:

```text
Validation Function Result 확인
→ setErrors 호출 확인
→ errors key 확인
→ Field name 확인
→ Error Rendering 조건 확인
→ Server Error Mapping 확인
```

주의:

- errors.email과 input name email 일치
- 서버 errors 구조 확인
- submit 실패 시 API 요청 중단
- error message 문자열 존재 여부 확인

---

### [FAQ]

Q. Validation은 실패했는데 메시지가 안 보여?

A.
errors state key와 input field name이 일치하는지, error rendering 조건이 맞는지 확인해야 한다.

Q. 서버 에러가 Form에 안 붙어?

A.
서버 응답의 errors 구조와 Frontend mapping 함수가 일치하는지 확인해야 한다.

---

## 16.4 Submit Not Working

### [개념]

Submit Not Working은 Form 제출 이벤트가 발생하지 않거나 API 요청이 실행되지 않는 문제다.

---

### [핵심]

원인:

- button type이 button
- form onSubmit 없음
- disabled 상태
- validation에서 항상 return
- async 함수 에러
- API 함수 호출 누락
- handleSubmit 연결 오류
- React Hook Form handleSubmit 사용 오류

---

### [실무]

Debug Flow:

```text
Button type 확인
→ form onSubmit 확인
→ handleSubmit console 확인
→ validation result 확인
→ API function call 확인
→ Network Tab 확인
→ Error catch 확인
```

주의:

- submit button은 type submit
- onSubmit에 함수 참조 전달
- `onSubmit={handleSubmit()}` 즉시 실행 주의
- disabled 조건 확인
- Network 요청 발생 여부 확인

---

### [FAQ]

Q. 버튼을 눌러도 submit이 안 돼?

A.
button type, form onSubmit 연결, disabled 상태, validation return, API 호출 여부를 확인해야 한다.

Q. Network 요청이 안 보여?

A.
submit handler 자체가 실행되지 않았거나 validation에서 중단되었을 수 있다.

---

## 16.5 Controlled Uncontrolled Warning

### [개념]

Controlled Uncontrolled Warning은 input이 처음에는 uncontrolled였다가 나중에 controlled로 바뀌거나 반대로 바뀔 때 발생하는 React 경고다.

---

### [핵심]

원인:

- 초기값 undefined
- API 데이터 로딩 전 value undefined
- null value
- 조건부 value 전달
- defaultValue와 value 혼용
- Controlled / Uncontrolled 혼용

---

### [실무]

나쁜 예:

```jsx
const [email, setEmail] = useState();

<input value={email} onChange={handleChange} />;
```

좋은 예:

```jsx
const [email, setEmail] = useState("");

<input value={email} onChange={handleChange} />;
```

수정 Form 예:

```jsx
<input value={values.email ?? ""} onChange={handleChange} />
```

주의:

- 문자열 input 초기값은 빈 문자열
- checkbox 초기값은 false
- 배열 초기값은 []
- 객체 초기값은 명확한 기본값
- defaultValue와 value 혼용 금지

---

### [FAQ]

Q. uncontrolled to controlled 경고는 왜 나?

A.
input value가 처음에는 undefined였다가 나중에 문자열로 바뀌는 등 제어 방식이 바뀌었기 때문이다.

Q. 해결 방법은 뭐야?

A.
초기값을 빈 문자열, false, []처럼 명확히 설정하고 value가 undefined가 되지 않게 한다.

---

# 17. Security Rules

## 17.1 Form Security Basics

### [개념]

Form Security는 사용자가 입력한 데이터와 민감정보를 안전하게 처리하기 위한 기본 기준이다.

---

### [핵심]

주의 대상:

- password
- access token
- personal information
- file upload
- XSS
- HTML injection
- client validation bypass
- sensitive console log
- autocomplete
- CSRF basics

---

### [실무]

기준:

- password console.log 금지
- 개인정보 console.log 금지
- Form 입력값을 innerHTML로 삽입 금지
- Client Validation만 신뢰 금지
- Server Validation 필수
- 파일 업로드는 Backend 검증 필수
- 민감정보 localStorage 저장 주의
- 에러 메시지에 내부 정보 노출 금지
- API Secret을 Frontend Form에 포함 금지

---

### [FAQ]

Q. Form 입력값은 안전한 데이터야?

A.
아니다. 사용자가 입력한 값은 항상 신뢰하지 말고 Backend에서 검증해야 한다.

Q. password를 로그로 찍으면 안 돼?

A.
안 된다. 민감정보가 브라우저 로그나 공유 화면에 노출될 수 있다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

Form Handling & Validation 문서는 헷갈리는 Form 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Controlled Component vs Uncontrolled Component
- Client Validation vs Server Validation
- Field Error vs Global Error
- Form State vs Server State
- Form Values Type vs Request DTO Type
- useState Form vs React Hook Form
- onChange vs onBlur
- onSubmit vs onClick
- disabled vs readOnly
- value vs defaultValue
- checkbox checked vs value
- FormData vs JSON Body
- URL Search Params vs Form State
- Submit Loading vs Initial Loading

---

### [실무]

예시:

| 비교   | Field Error       | Global Error             |
| ------ | ----------------- | ------------------------ |
| 위치   | 특정 input 근처   | Form 상단 또는 공통 영역 |
| 예     | 이메일 형식 오류  | 로그인 실패              |
| 기준   | field name과 연결 | Form 전체 실패           |
| 접근성 | aria-describedby  | role alert               |
| 처리   | errors.email      | submitError              |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 Form 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Form Handling 비교 문서에서 가장 중요한 것은?

A.
입력 제어 방식, 검증 위치, 에러 표시 기준, 제출 흐름, API 요청 구조를 함께 설명하는 것이다.

---

# 19. Checklist Rules

## 19.1 Form Handling Checklist

### [개념]

Form Handling 문서 검수 시 Form 구현 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Form 목적과 입력 필드가 명확한가?
- [ ] Controlled Component 기준이 포함되었는가?
- [ ] value / checked / onChange 기준이 포함되었는가?
- [ ] onSubmit과 preventDefault가 포함되었는가?
- [ ] button type 기준이 포함되었는가?
- [ ] Form State와 Error State가 분리되었는가?
- [ ] Client Validation 기준이 포함되었는가?
- [ ] Server Validation Error 처리 기준이 포함되었는가?
- [ ] Field Error와 Global Error 차이가 포함되었는가?
- [ ] Submit Loading과 중복 제출 방지가 포함되었는가?
- [ ] Request Body Mapping 기준이 포함되었는가?
- [ ] Form Reset 기준이 포함되었는가?
- [ ] React Hook Form 적용 기준이 포함되었는가?
- [ ] Accessibility 기준이 포함되었는가?
- [ ] Security 주의사항이 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Form Element Check
→ Controlled Input Check
→ State Check
→ Validation Check
→ Submit Flow Check
→ Error UX Check
→ Accessibility Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Form Handling 문서 검수에서 가장 중요한 것은?

A.
Controlled Input, Validation, Submit Flow, Error Handling, Request Mapping, Accessibility, Troubleshooting 포함 여부다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

Form Handling & Validation 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Form Handling
- Form Validation
- React Form
- Controlled Component
- Uncontrolled Component
- Form State
- Field State
- Error State
- Touched
- Dirty
- onChange
- onBlur
- onSubmit
- preventDefault
- Input Handling
- Textarea
- Select
- Checkbox
- Radio
- File Input
- Client Validation
- Server Validation
- Field Error
- Global Error
- Submit Flow
- Duplicate Submit
- Form Reset
- Request Body Mapping
- Request DTO
- React Hook Form
- useForm
- register
- handleSubmit
- setError
- Form Accessibility
- aria-invalid
- aria-describedby
- Controlled Uncontrolled Warning

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- React Form은 어떻게 처리해?
- input 값이 안 바뀌는 이유는?
- form 제출하면 새로고침되는 이유는?
- Controlled Component가 뭐야?
- checkbox는 value야 checked야?
- validation error는 어떻게 보여줘?
- server validation error는 어떻게 처리해?
- Field Error와 Global Error 차이는?
- submit 중복 요청은 어떻게 막아?
- Form State는 어디에 둬?
- React Hook Form은 언제 써?
- Request Body는 Form State 그대로 보내도 돼?
- uncontrolled to controlled 경고는 왜 나?
- placeholder만 쓰면 label 없어도 돼?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 21. Version Rules

## 21.1 Modern Form Handling 기준

### [개념]

Form Handling & Validation 문서는 Modern React Form 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- Hook 기반 Form State
- Controlled Component
- React Hook Form 고려
- TypeScript Ready Form
- Client + Server Validation
- Accessibility 기본 포함
- API Request DTO Mapping
- Loading / Error UX 포함

Legacy 제외:

- jQuery form submit 중심 설명
- DOM 직접 조작 중심 Form
- uncontrolled form만 기본으로 사용하는 방식
- validation 없이 API 요청
- password console.log
- 모든 Form State 전역 저장
- label 없는 placeholder-only Form
- Error Message 없는 Form
- submit 중복 방지 없는 Form

---

### [실무]

실무 기준:

```text
Modern React Form
→ Controlled Input
→ Form State
→ Validation
→ Submit Flow
→ Request DTO Mapping
→ Server Error Mapping
→ Accessible Error UI
```

---

### [FAQ]

Q. jQuery 방식 Form 처리를 써야 해?

A.
신규 React 문서에서는 Controlled Component, Hook, React Hook Form, API Layer 기준으로 작성한다.

Q. label 없는 placeholder Form은 괜찮아?

A.
권장하지 않는다. 접근성과 사용성 측면에서 label을 제공하는 것이 좋다.

---

# 22. Common Mistakes

## 22.1 Form Handling Common Mistakes

### [개념]

Form Handling & Validation 문서는 자주 발생하는 Form 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- form submit에서 preventDefault 누락
- button type 누락
- input value만 있고 onChange 없음
- checkbox를 value로 처리
- number input 문자열 변환 누락
- name과 values key 불일치
- 초기값 undefined로 controlled warning 발생
- Controlled와 Uncontrolled 혼용
- validation error state 업데이트 누락
- server validation error mapping 누락
- field error와 global error 혼동
- submit 실패 후 입력값 초기화
- submitting 상태 없이 중복 제출 허용
- Request Body 변환 없이 Form State 그대로 전송
- Backend DTO 필드명과 불일치
- password console.log
- placeholder로 label 대체
- aria-invalid / aria-describedby 누락
- Client Validation만 믿고 Server Validation 생략
- 파일 업로드에서 Content-Type 직접 잘못 설정
- Form State를 무조건 전역 Store에 저장

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: input 입력이 안 됨
원인: value는 설정했지만 onChange에서 State를 업데이트하지 않음
해결: value와 onChange를 함께 설정하고 State 초기값을 명확히 지정
```

---

### [FAQ]

Q. Form Handling 초보가 가장 많이 하는 실수는?

A.
preventDefault 누락, value/onChange 불일치, checkbox checked 처리 누락, validation error mapping 누락이 많다.

Q. Form 문제는 어떻게 찾는 게 좋아?

A.
input value, onChange, state key, submit event, validation result, API request body, server error response를 순서대로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

Form Handling & Validation RAG 문서는 Frontend Agent가 React Form 입력, 검증, 제출, 에러 처리, API 연동을 안정적으로 구현하고 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Form Element 구조 이해
- Controlled Component 작성
- Uncontrolled Component 적용 판단
- Form State 설계
- Field State 설계
- onChange 처리
- onBlur 처리
- onSubmit 처리
- preventDefault 적용
- Client Validation 작성
- Server Validation Error 처리
- Field Error / Global Error 구분
- Submit Loading 처리
- Duplicate Submit 방지
- Form Reset 처리
- Request Body Mapping
- Request DTO Type 작성
- React Hook Form 적용 판단
- Form Accessibility 적용
- Form Security 기본 주의
- Form Troubleshooting 수행
- Common Mistakes 검토

---

### [실무]

Agent 수행 가능 작업:

```text
User Form Request
→ Identify Form Fields
→ Define Form State
→ Define Validation Rules
→ Build Controlled Inputs
→ Implement Submit Flow
→ Map Request Body
→ Handle Server Errors
→ Add Loading / Disabled State
→ Check Accessibility
→ Form Handling Output
```

---

### [FAQ]

Q. Form Handling 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 입력값 관리, 검증, 제출, 에러 표시, API 요청 Body 변환까지 포함한 실무형 React Form을 만들게 하는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Authentication Frontend Flow, Error Handling & Loading UX, Frontend Testing, Frontend Accessibility 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Form Handling 문서는 왜 필요해?
A. Frontend Agent가 React Form의 입력, 검증, 제출, 에러 처리, API 연동을 안정적으로 구현해야 하기 때문이다.

Q. React Form은 어떻게 처리해?
A. 보통 Controlled Component로 입력값을 State에 저장하고 onSubmit에서 검증 후 API 요청을 수행한다.

Q. Controlled Component가 뭐야?
A. 입력값을 DOM이 아니라 React State로 관리하는 input 방식이다.

Q. Uncontrolled Component가 뭐야?
A. 입력값을 React State로 매번 제어하지 않고 DOM이나 ref를 통해 필요할 때 읽는 방식이다.

Q. input 값이 안 바뀌는 이유는?
A. value는 설정했지만 onChange로 State를 업데이트하지 않았을 가능성이 크다.

Q. checkbox는 value야 checked야?
A. checkbox는 보통 checked와 event.target.checked로 제어한다.

Q. radio button은 어떻게 제어해?
A. 같은 name을 가진 radio들 중 현재 값과 value가 일치하는 항목에 checked를 설정한다.

Q. number input 값은 number로 들어와?
A. 대부분 문자열로 들어온다. 숫자가 필요하면 Number 변환과 NaN 검증이 필요하다.

Q. form submit 시 페이지가 새로고침돼?
A. 기본 form 제출 동작 때문이다. React에서는 onSubmit에서 event.preventDefault를 호출해야 한다.

Q. button type을 꼭 써야 해?
A. 권장한다. form 안의 button은 기본 submit으로 동작할 수 있어 일반 버튼은 type="button"을 명시하는 것이 안전하다.

Q. onClick으로 submit 처리해도 돼?
A. 가능하지만 form onSubmit을 사용하는 것이 Enter key 제출과 접근성 측면에서 더 좋다.

Q. Form State는 어디에 둬?
A. 단일 Form 내부에서만 필요하면 Form Component의 Local State에 두는 것이 일반적이다.

Q. Form 입력값은 각각 useState로 둬야 해, 객체로 둬야 해?
A. 입력값이 적으면 각각 useState도 가능하고, 필드가 많으면 values 객체로 관리하는 것이 편할 수 있다.

Q. Form State를 전역 상태로 둬도 돼?
A. 대부분 권장하지 않는다. Form 내부 임시 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. 수정 Form의 초기값은 Server State야 Form State야?
A. 서버에서 받은 초기값은 Server State이고 사용자가 수정 중인 값은 Form State다.

Q. touched는 뭐야?
A. 사용자가 해당 필드를 방문하거나 blur한 적이 있는지를 나타내는 상태다.

Q. dirty는 뭐야?
A. 초기값과 현재 입력값이 달라졌는지를 나타내는 상태다.

Q. 에러 메시지는 언제 보여줘?
A. 보통 submit 후 또는 touched 이후 보여주는 방식이 사용자 경험에 좋다.

Q. 여러 input을 하나의 handleChange로 처리할 수 있어?
A. 가능하다. input name과 values 객체 key를 맞추면 공통 handler로 처리할 수 있다.

Q. name과 state key가 다르면 어떻게 돼?
A. 공통 handleChange에서 잘못된 key가 업데이트되어 input 값이 바뀌지 않을 수 있다.

Q. 파일 input도 value로 제어해?
A. 일반적으로 파일 input은 value로 제어하지 않고 files를 읽어서 처리한다.

Q. 파일 업로드는 어떻게 처리해?
A. File 객체를 읽고 FormData에 append한 뒤 multipart 요청으로 전송한다.

Q. 이미지 미리보기 URL은 정리해야 해?
A. URL.createObjectURL을 사용했다면 필요 없어진 시점에 URL.revokeObjectURL로 정리하는 것이 좋다.

Q. Client Validation이 뭐야?
A. 사용자가 Form을 제출하기 전에 브라우저에서 입력값을 검증하는 UX용 검증이다.

Q. Client Validation이 있으면 Server Validation은 없어도 돼?
A. 안 된다. Client Validation은 우회될 수 있으므로 Backend 검증이 반드시 필요하다.

Q. Validation 함수는 Component 안에 둬도 돼?
A. 간단한 Form은 가능하지만 재사용되거나 복잡하면 별도 함수로 분리하는 것이 좋다.

Q. 공백만 입력해도 값이 있는 걸로 봐?
A. 대부분 trim 후 빈 문자열이면 입력하지 않은 것으로 처리한다.

Q. Frontend maxLength와 Backend 제한이 다르면?
A. Backend 기준이 최종이므로 Frontend 제한을 Backend와 맞춰야 한다.

Q. 이메일 검증은 정규식으로 완벽하게 해야 해?
A. 완벽한 이메일 정규식보다 기본 형식 확인과 Backend 검증을 함께 사용하는 것이 실용적이다.

Q. 비밀번호 정책은 어디 기준으로 맞춰?
A. Backend Validation 정책과 동일하게 맞춰야 한다.

Q. 비밀번호 확인 검증은 어디에 표시해?
A. 보통 confirmPassword 필드 근처에 표시한다.

Q. Server Validation Error는 어디에 보여줘?
A. 필드별 오류는 해당 input 근처에 표시하고 공통 오류는 form 상단에 표시한다.

Q. 서버가 준 에러 메시지를 그대로 보여줘도 돼?
A. 서비스 정책에 따라 가능하지만 민감한 내부 정보가 포함되지 않도록 Backend 응답 메시지를 관리해야 한다.

Q. Field Error와 Global Error 차이는?
A. Field Error는 특정 input에 연결되는 오류이고 Global Error는 Form 전체 실패나 인증 실패처럼 공통 영역에 표시하는 오류다.

Q. 로그인 실패 에러는 field error야 global error야?
A. 이메일 형식 오류는 field error이고, 계정 정보가 일치하지 않음 같은 인증 실패는 global error로 처리하는 경우가 많다.

Q. Submit 전에 에러를 초기화해야 해?
A. 권장한다. 이전 제출의 에러가 남아 현재 상태와 맞지 않을 수 있기 때문이다.

Q. Submit 실패 후 입력값은 지워야 해?
A. 보통 지우지 않는다. 사용자가 수정 후 다시 제출할 수 있도록 유지하는 것이 좋다.

Q. 버튼 disabled만 하면 중복 제출이 완전히 막혀?
A. 아니다. UX상 중복 클릭을 줄일 수 있지만 중요한 요청은 Backend에서도 중복 방지 기준이 필요하다.

Q. 제출 중 버튼 문구를 바꿔야 해?
A. 권장한다. 사용자가 현재 처리 중임을 알 수 있다.

Q. Form 제출 성공 후 항상 reset해야 해?
A. 항상은 아니다. 리뷰 작성처럼 새 입력을 받는 Form은 reset하고, 수정 Form은 최신 서버 값으로 갱신하는 것이 좋다.

Q. 검색 Form reset은 URL도 같이 초기화해야 해?
A. 검색 조건을 URL State로 관리한다면 URL Search Params도 함께 초기화해야 한다.

Q. Form State를 그대로 API body로 보내도 돼?
A. 간단한 경우 가능하지만 trim, type conversion, field name mapping이 필요하면 Request DTO로 변환하는 것이 좋다.

Q. Form Values Type과 Request Type을 왜 나눠?
A. input 값은 문자열일 수 있지만 Backend Request는 number, boolean, enum 등 다른 타입을 요구할 수 있기 때문이다.

Q. 변환 함수는 왜 필요해?
A. trim, Number 변환, null 처리, 필드명 mapping을 일관되게 처리하기 위해 필요하다.

Q. React Hook Form은 언제 써?
A. 입력 필드가 많고 검증, touched, dirty, error 상태 관리가 복잡해질 때 검토한다.

Q. 간단한 Form에도 React Hook Form을 써야 해?
A. 필수는 아니다. 간단한 검색 Form이나 작은 입력 Form은 useState로 충분할 수 있다.

Q. register는 뭐야?
A. input을 React Hook Form에 등록해 값과 검증 규칙을 관리하게 하는 함수다.

Q. handleSubmit은 preventDefault를 대신 해?
A. React Hook Form의 handleSubmit은 form submit 기본 동작을 처리하고 검증 후 submit 함수를 호출한다.

Q. 서버 에러는 React Hook Form에 어떻게 넣어?
A. setError를 사용해 field error 또는 root error로 연결할 수 있다.

Q. placeholder만 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 접근성 측면에서 label을 대체하기 어렵다.

Q. 에러 메시지는 input과 연결해야 해?
A. 권장한다. aria-describedby로 input과 에러 메시지를 연결하면 스크린 리더 사용자가 오류를 이해하기 쉽다.

Q. Submit 실패 시 focus를 이동해야 해?
A. 필수는 아니지만 첫 오류 field로 이동하면 사용자가 문제를 빠르게 수정할 수 있다.

Q. Modal Form에서는 focus를 어떻게 해?
A. 열릴 때 Modal 내부로 focus를 이동하고 닫힐 때 이전 trigger로 복귀하는 것이 좋다.

Q. Form Component는 언제 분리해?
A. 필드가 많아지거나 검증/에러/제출 로직이 길어지면 Field, Validator, Mapper, API 함수로 분리한다.

Q. Validation 함수는 어디에 둬?
A. 단순하면 Component 안에 둘 수 있고 복잡하거나 재사용되면 validators 파일로 분리한다.

Q. Field Component는 왜 만들어?
A. label, input, error message, 접근성 속성을 반복하지 않고 일관되게 관리하기 위해 만든다.

Q. 검색어 입력 중에도 바로 API 호출해야 해?
A. 필수는 아니다. 검색 버튼 submit 방식이 단순하고, 실시간 검색이 필요하면 debounce를 적용한다.

Q. 검색 조건이 바뀌면 page를 reset해야 해?
A. 대부분 그렇다. 기존 page가 새 검색 결과 범위를 벗어날 수 있기 때문이다.

Q. 이메일 중복 검사는 Frontend에서만 가능해?
A. 아니다. 실제 중복 여부는 서버 데이터 기준이므로 Backend API 확인이 필요하다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 민감정보는 로그에 남기지 않는 것이 원칙이다.

Q. Validation은 실패했는데 메시지가 안 보여?
A. errors state key와 input field name이 일치하는지, error rendering 조건이 맞는지 확인해야 한다.

Q. 서버 에러가 Form에 안 붙어?
A. 서버 응답의 errors 구조와 Frontend mapping 함수가 일치하는지 확인해야 한다.

Q. 버튼을 눌러도 submit이 안 돼?
A. button type, form onSubmit 연결, disabled 상태, validation return, API 호출 여부를 확인해야 한다.

Q. Network 요청이 안 보여?
A. submit handler 자체가 실행되지 않았거나 validation에서 중단되었을 수 있다.

Q. uncontrolled to controlled 경고는 왜 나?
A. input value가 처음에는 undefined였다가 나중에 문자열로 바뀌는 등 제어 방식이 바뀌었기 때문이다.

Q. uncontrolled to controlled 경고 해결 방법은 뭐야?
A. 초기값을 빈 문자열, false, []처럼 명확히 설정하고 value가 undefined가 되지 않게 한다.

Q. Form 입력값은 안전한 데이터야?
A. 아니다. 사용자가 입력한 값은 항상 신뢰하지 말고 Backend에서 검증해야 한다.

Q. Form Handling 초보가 가장 많이 하는 실수는?
A. preventDefault 누락, value/onChange 불일치, checkbox checked 처리 누락, validation error mapping 누락이 많다.

Q. Form 문제는 어떻게 찾는 게 좋아?
A. input value, onChange, state key, submit event, validation result, API request body, server error response를 순서대로 확인한다.

Q. Form Handling 다음 문서는 뭐가 좋아?
A. Authentication Frontend Flow, Error Handling & Loading UX, Frontend Testing, Frontend Accessibility 순서가 좋다.
