# Form Handling & Validation Part03 - Input Handling

---

# 1. Input Handling Foundation

## 1.1 Input Handling Definition

### [개념]

Input Handling은 사용자가 Form Field에 값을 입력하거나 선택했을 때 해당 값을 React Form State에 반영하는 처리 흐름이다.

Input Handling은 단순 `onChange` 작성이 아니라 Field Type별 값 읽기 기준, State Update 기준, name-key mapping, type conversion, validation trigger까지 포함한다.

---

### [핵심]

Input Handling 핵심 요소:

- onChange
- onBlur
- event.target
- name
- value
- checked
- files
- type
- Form State Update
- Common Change Handler
- Field Type Handling
- Type Conversion
- Input Normalization
- State Key Mapping
- Controlled Component

---

### [실무]

2026 실무 기준에서 Input Handling은 아래 흐름으로 처리한다.

```text
User Input
→ Event Trigger
→ Read Field Name
→ Read Field Value
→ Normalize if Needed
→ Update Form State
→ Clear Field Error if Needed
→ Optional Validation
→ Re-render UI
```

입력 타입별 값 읽기 기준:

| Field Type        | Read Value                          |
| ----------------- | ----------------------------------- |
| text              | event.target.value                  |
| textarea          | event.target.value                  |
| select            | event.target.value                  |
| checkbox          | event.target.checked                |
| radio             | event.target.value + checked        |
| file              | event.target.files                  |
| number            | event.target.value 또는 Number 변환 |
| multiple checkbox | array update                        |
| multiple select   | selectedOptions                     |

---

### [FAQ]

Q. Input Handling이 뭐야?
A. 사용자의 입력 이벤트를 받아 Form State를 업데이트하는 React Form 처리 흐름이다.

Q. 모든 input은 event.target.value로 처리해?
A. 아니다. checkbox는 checked, file input은 files, multiple select는 selectedOptions를 사용한다.

Q. Input Handling에서 가장 중요한 것은 뭐야?
A. field type별 값 읽기 기준과 input name, Form State key를 일치시키는 것이다.

Q. Input Handling은 Form State와 어떤 관계야?
A. Input Handling은 사용자의 입력을 Form State에 반영하는 연결 계층이다.

---

# 2. Common Change Handler Rules

## 2.1 Common Change Handler Definition

### [개념]

Common Change Handler는 여러 input의 `onChange`를 하나의 함수로 처리하는 패턴이다.

`input name`과 `values key`를 일치시켜 동적으로 Form State를 업데이트한다.

---

### [핵심]

Common Change Handler 핵심 요소:

- name
- value
- checked
- type
- event.target
- computed property name
- values key matching
- dynamic state update
- reusable handler
- checkbox handling

---

### [실무]

기본 Common Change Handler:

```javascript
function handleChange(event) {
  const { name, value } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));
}
```

사용 예:

```jsx
<input
  name="email"
  value={values.email}
  onChange={handleChange}
/>

<input
  name="nickname"
  value={values.nickname}
  onChange={handleChange}
/>
```

권장:

- `name`과 `values` key 일치
- state 직접 mutation 금지
- setState callback 형태 사용
- 복잡한 Field Type은 별도 handler 분리 가능
- TypeScript에서는 event type 명시

---

### [FAQ]

Q. 여러 input을 하나의 handleChange로 처리할 수 있어?
A. 가능하다. input name과 values 객체 key를 맞추면 공통 handler로 처리할 수 있다.

Q. Common Change Handler의 핵심 조건은 뭐야?
A. input name과 values key가 일치해야 한다.

Q. name이 없으면 공통 handler가 동작해?
A. 어렵다. 어떤 key를 업데이트할지 알 수 없기 때문이다.

Q. Common Change Handler는 모든 input에 써야 해?
A. 아니다. checkbox, file, custom component처럼 특수 처리가 필요하면 별도 handler를 사용할 수 있다.

---

## 2.2 Checkbox Included Handler

### [개념]

Checkbox Included Handler는 text, select, checkbox를 하나의 `handleChange`에서 처리하는 패턴이다.

checkbox는 `value`가 아니라 `checked`를 사용해야 한다.

---

### [핵심]

Checkbox 포함 handler 기준:

- type check
- checkbox
- checked
- value
- boolean field
- event.target.type
- dynamic value selection

---

### [실무]

Checkbox 포함 Common Change Handler:

```javascript
function handleChange(event) {
  const { name, type, value, checked } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: type === "checkbox" ? checked : value,
  }));
}
```

사용 예:

```jsx
<input
  name="email"
  value={values.email}
  onChange={handleChange}
/>

<input
  type="checkbox"
  name="agreed"
  checked={values.agreed}
  onChange={handleChange}
/>
```

주의:

- checkbox는 `checked`로 boolean 관리
- value로 처리하면 `"on"` 또는 지정 value가 들어갈 수 있음
- 다중 checkbox는 단순 boolean handler와 다름
- 약관 동의는 boolean field로 관리

---

### [FAQ]

Q. checkbox도 Common Change Handler로 처리할 수 있어?
A. 가능하다. 다만 type이 checkbox일 때 checked를 사용해야 한다.

Q. checkbox 값을 value로 읽으면 안 돼?
A. 선택 여부가 아니라 value 속성값을 읽게 되므로 일반적으로 checked를 사용한다.

Q. 약관 동의 checkbox는 어떤 값으로 관리해?
A. boolean 값으로 관리한다.

Q. 여러 checkbox도 같은 방식으로 처리해?
A. 아니다. 여러 checkbox는 배열 추가/제거 로직이 필요하다.

---

# 3. Text Input Handling Rules

## 3.1 Text Input onChange

### [개념]

Text Input Handling은 사용자의 문자열 입력을 `event.target.value`로 읽어 Form State에 저장하는 방식이다.

Text Input은 React에서 가장 일반적인 Controlled Component 처리 대상이다.

---

### [핵심]

Text Input Handling 요소:

- input type text
- value
- onChange
- event.target.value
- string state
- controlled input
- initial value
- maxLength
- trim timing

---

### [실무]

Text Input 예:

```jsx
function TitleField() {
  const [title, setTitle] = useState("");

  function handleTitleChange(event) {
    setTitle(event.target.value);
  }

  return (
    <input
      name="title"
      value={title}
      maxLength={50}
      onChange={handleTitleChange}
    />
  );
}
```

권장:

- 입력 중에는 사용자가 입력한 값을 그대로 보존
- submit 시 trim 적용 권장
- `maxLength`는 UX용, Backend Validation 필요
- 초기값은 빈 문자열 사용
- value와 onChange를 함께 제공

주의:

- onChange에서 무리한 trim을 하면 사용자가 공백 입력을 제어하기 어려움
- 숫자처럼 보여도 input value는 문자열일 수 있음
- format 변환은 UX를 해치지 않게 적용

---

### [FAQ]

Q. Text Input 값은 어디서 읽어?
A. event.target.value에서 읽는다.

Q. 입력 중에 trim을 바로 적용해도 돼?
A. 가능하지만 사용자가 의도한 공백 입력을 방해할 수 있어 보통 submit 시점에 처리한다.

Q. maxLength만 있으면 Backend 길이 검증은 없어도 돼?
A. 아니다. maxLength는 우회될 수 있으므로 Backend Validation도 필요하다.

Q. Text Input 초기값은 무엇이 좋아?
A. 빈 문자열 `""`이 안전하다.

---

## 3.2 Textarea onChange

### [개념]

Textarea Handling은 여러 줄 텍스트 입력을 Form State에 저장하는 처리다.

리뷰, 댓글, 문의, 설명처럼 긴 문자열에 사용한다.

---

### [핵심]

Textarea Handling 요소:

- textarea
- value
- onChange
- event.target.value
- content state
- character count
- maxLength
- rows
- trim
- empty content validation

---

### [실무]

Textarea Handling 예:

```jsx
function ContentField({ values, setValues }) {
  function handleChange(event) {
    setValues((prevValues) => ({
      ...prevValues,
      content: event.target.value,
    }));
  }

  return (
    <>
      <textarea
        name="content"
        value={values.content}
        maxLength={500}
        rows={5}
        onChange={handleChange}
      />
      <p>{values.content.length}/500</p>
    </>
  );
}
```

권장:

- 입력 중에는 줄바꿈 보존
- submit 시 trim 기준 명확화
- 공백만 입력한 값은 invalid 처리 가능
- 글자 수 카운트 표시 가능
- Backend DTO length와 maxLength 일치

---

### [FAQ]

Q. textarea도 event.target.value로 읽어?
A. 그렇다. textarea 값도 event.target.value로 읽는다.

Q. textarea 줄바꿈은 유지돼?
A. value에 문자열로 저장되며 줄바꿈도 포함된다.

Q. 리뷰 내용은 submit 전에 trim해야 해?
A. 대부분 권장한다. 공백만 입력한 리뷰를 방지할 수 있다.

Q. textarea 글자 수는 어떻게 표시해?
A. values.content.length를 사용해 현재 길이를 표시할 수 있다.

---

# 4. Select Handling Rules

## 4.1 Single Select Handling

### [개념]

Single Select Handling은 사용자가 선택한 option value를 Form State에 저장하는 처리다.

지역, 카테고리, 정렬, 상태, enum 선택에 자주 사용한다.

---

### [핵심]

Single Select 요소:

- select
- option
- value
- onChange
- event.target.value
- empty option
- code value
- enum value
- filter value
- query param mapping

---

### [실무]

Single Select 예:

```jsx
function CategorySelect({ values, handleChange }) {
  return (
    <select name="category" value={values.category} onChange={handleChange}>
      <option value="">전체</option>
      <option value="NOTICE">공지</option>
      <option value="REVIEW">리뷰</option>
    </select>
  );
}
```

권장:

- option value는 Backend enum 또는 code와 일치
- 전체 선택은 빈 문자열 `""`로 표현 가능
- 빈 값은 Request Mapping 단계에서 제외 가능
- select value 초기값을 undefined로 두지 않음
- 표시 문구와 전송 값을 구분

---

### [FAQ]

Q. select 값은 어디서 읽어?
A. event.target.value에서 선택된 option value를 읽는다.

Q. option value는 화면 문구로 넣어도 돼?
A. 보통 Backend enum 또는 code 값을 넣는 것이 좋다.

Q. 전체 선택은 어떻게 처리해?
A. value를 빈 문자열로 두고 Request Mapping에서 제외하거나 null로 변환할 수 있다.

Q. select value 초기값은 뭐가 좋아?
A. 빈 문자열 `""` 또는 기본 option value를 사용한다.

---

## 4.2 Multiple Select Handling

### [개념]

Multiple Select Handling은 여러 option 선택값을 배열로 저장하는 처리다.

`event.target.selectedOptions`를 배열로 변환해 Form State에 반영한다.

---

### [핵심]

Multiple Select 요소:

- multiple
- selectedOptions
- Array.from
- option.value
- array state
- multi filter
- code array
- Request Body Mapping

---

### [실무]

Multiple Select 예:

```jsx
function ThemeMultiSelect({ values, setValues }) {
  function handleThemeChange(event) {
    const selectedValues = Array.from(
      event.target.selectedOptions,
      (option) => option.value,
    );

    setValues((prevValues) => ({
      ...prevValues,
      themeCodes: selectedValues,
    }));
  }

  return (
    <select
      name="themeCodes"
      multiple
      value={values.themeCodes}
      onChange={handleThemeChange}
    >
      <option value="MUSIC">음악</option>
      <option value="FOOD">음식</option>
      <option value="CULTURE">문화</option>
    </select>
  );
}
```

주의:

- value는 배열이어야 함
- 초기값은 `[]`
- 선택값은 문자열 배열로 들어올 수 있음
- Backend가 숫자 배열을 요구하면 변환 필요
- UX상 multiple select보다 checkbox group이 더 적합할 수 있음

---

### [FAQ]

Q. multiple select 값은 어떻게 읽어?
A. event.target.selectedOptions를 Array.from으로 배열 변환한다.

Q. multiple select 초기값은 뭐가 좋아?
A. 빈 배열 `[]`이 적합하다.

Q. multiple select value는 문자열이야?
A. option value 기준이므로 보통 문자열이다. 필요하면 submit 시 변환한다.

Q. multiple select와 checkbox group 중 뭐가 좋아?
A. 선택 항목이 명확히 보이는 UX가 필요하면 checkbox group이 더 적합할 수 있다.

---

# 5. Checkbox Handling Rules

## 5.1 Boolean Checkbox Handling

### [개념]

Boolean Checkbox Handling은 단일 checkbox의 선택 여부를 boolean State로 관리하는 처리다.

약관 동의, 공개 여부, 알림 수신 여부 같은 값에 사용한다.

---

### [핵심]

Boolean Checkbox 요소:

- checkbox
- checked
- event.target.checked
- boolean state
- agreement
- enabled flag
- notification setting
- required checkbox

---

### [실무]

Boolean Checkbox 예:

```jsx
function AgreementField({ values, handleChange }) {
  return (
    <label>
      <input
        type="checkbox"
        name="agreed"
        checked={values.agreed}
        onChange={handleChange}
      />
      약관에 동의합니다.
    </label>
  );
}
```

Common Handler:

```javascript
function handleChange(event) {
  const { name, checked } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: checked,
  }));
}
```

권장:

- checkbox는 checked로 제어
- 초기값은 false
- 필수 동의는 validation 필요
- Backend에도 동의 여부 전달 필요
- label로 클릭 영역 확장

---

### [FAQ]

Q. checkbox 선택 여부는 어떻게 읽어?
A. event.target.checked로 읽는다.

Q. checkbox 초기값은 뭐가 좋아?
A. false가 일반적이다.

Q. checked와 value 중 무엇을 써?
A. 선택 여부는 checked를 사용한다.

Q. 약관 동의 checkbox는 검증해야 해?
A. 필수 동의라면 Client Validation과 Server Validation 모두 필요하다.

---

## 5.2 Multiple Checkbox Handling

### [개념]

Multiple Checkbox Handling은 여러 checkbox에서 선택된 값을 배열로 관리하는 처리다.

관심 카테고리, 테마 필터, 권한 선택, 태그 선택에 사용한다.

---

### [핵심]

Multiple Checkbox 요소:

- checkbox group
- selected values
- array state
- includes
- add item
- remove item
- checked by includes
- code list
- id list

---

### [실무]

Multiple Checkbox 예:

```jsx
function ThemeCheckboxGroup({ selectedThemes, setSelectedThemes }) {
  function handleThemeToggle(themeCode) {
    setSelectedThemes((prevThemes) =>
      prevThemes.includes(themeCode)
        ? prevThemes.filter((code) => code !== themeCode)
        : [...prevThemes, themeCode],
    );
  }

  return (
    <>
      {["MUSIC", "FOOD", "CULTURE"].map((themeCode) => (
        <label key={themeCode}>
          <input
            type="checkbox"
            checked={selectedThemes.includes(themeCode)}
            onChange={() => handleThemeToggle(themeCode)}
          />
          {themeCode}
        </label>
      ))}
    </>
  );
}
```

권장:

- 선택된 값은 배열로 관리
- checked는 `array.includes(value)`로 계산
- 선택 시 배열에 추가
- 해제 시 배열에서 제거
- Backend Request에서 code array로 전송 가능
- 순서가 중요하면 정렬 기준 명확화

---

### [FAQ]

Q. 여러 checkbox 선택값은 어떻게 저장해?
A. 선택된 code 또는 id를 배열로 저장한다.

Q. multiple checkbox의 checked는 어떻게 계산해?
A. selectedValues.includes(value)를 사용한다.

Q. checkbox를 해제하면 어떻게 처리해?
A. filter로 해당 값을 배열에서 제거한다.

Q. 선택값 순서가 중요하면 어떻게 해?
A. 추가 순서를 유지하거나 Request Mapping 단계에서 정렬 기준을 적용한다.

---

# 6. Radio Handling Rules

## 6.1 Radio Group Handling

### [개념]

Radio Group Handling은 여러 radio option 중 하나의 값을 선택해 Form State에 저장하는 처리다.

같은 그룹의 radio는 동일한 `name`을 사용한다.

---

### [핵심]

Radio Handling 요소:

- input type radio
- same name
- value
- checked
- event.target.value
- single selection
- enum field
- option group
- fieldset
- legend

---

### [실무]

Radio Group 예:

```jsx
function VisibilityRadioGroup({ values, handleChange }) {
  return (
    <fieldset>
      <legend>공개 범위</legend>

      <label>
        <input
          type="radio"
          name="visibility"
          value="PUBLIC"
          checked={values.visibility === "PUBLIC"}
          onChange={handleChange}
        />
        공개
      </label>

      <label>
        <input
          type="radio"
          name="visibility"
          value="PRIVATE"
          checked={values.visibility === "PRIVATE"}
          onChange={handleChange}
        />
        비공개
      </label>
    </fieldset>
  );
}
```

권장:

- 같은 radio group은 같은 name 사용
- checked는 현재 State와 option value 비교
- value는 Backend enum 또는 code와 일치
- 접근성을 위해 fieldset / legend 사용
- 미선택 허용 여부와 초기값 명확화

---

### [FAQ]

Q. radio button 값은 어떻게 읽어?
A. 선택된 radio의 event.target.value를 읽는다.

Q. radio checked는 어떻게 설정해?
A. 현재 State 값과 radio value가 같을 때 checked를 true로 설정한다.

Q. radio group은 왜 같은 name을 써?
A. 같은 그룹에서 하나만 선택되도록 하기 위해서다.

Q. radio value는 어떤 값으로 맞춰?
A. Backend enum 또는 code 값과 일치시키는 것이 좋다.

---

# 7. Number Input Handling Rules

## 7.1 Number Input String Handling

### [개념]

Number Input은 화면상 숫자 입력처럼 보여도 `event.target.value`는 대부분 문자열로 들어온다.

입력 중에는 문자열로 관리하고 submit 또는 validation 단계에서 숫자로 변환하는 방식이 실무적으로 안전하다.

---

### [핵심]

Number Input 요소:

- input type number
- event.target.value
- string value
- Number conversion
- NaN validation
- empty string
- min
- max
- step
- numeric validation

---

### [실무]

문자열 유지 방식:

```jsx
function RatingField({ values, handleChange }) {
  return (
    <input
      type="number"
      name="rating"
      min="1"
      max="5"
      value={values.rating}
      onChange={handleChange}
    />
  );
}
```

Request Mapping 단계 변환:

```javascript
const requestBody = {
  rating: Number(values.rating),
};
```

Validation 예:

```javascript
const rating = Number(values.rating);

if (Number.isNaN(rating) || rating < 1 || rating > 5) {
  errors.rating = "평점은 1점에서 5점 사이여야 합니다.";
}
```

권장:

- 입력 중 빈 문자열 허용 여부 결정
- submit 시 Number 변환
- NaN 검증 필수
- min/max는 UX용이며 Backend Validation 필요
- 가격, 수량, 평점 등은 범위 검증 필요

---

### [FAQ]

Q. number input 값은 number로 들어와?
A. 대부분 문자열로 들어온다.

Q. 숫자 변환은 언제 하는 게 좋아?
A. 입력 중에는 문자열로 관리하고 submit 또는 validation 단계에서 변환하는 방식이 안전하다.

Q. 빈 숫자 input은 어떻게 처리해?
A. 빈 문자열로 관리하고 필수값 검증 또는 null 변환 기준을 둔다.

Q. min/max만 있으면 Backend 검증은 없어도 돼?
A. 아니다. Backend에서도 범위 검증이 필요하다.

---

## 7.2 Immediate Number Conversion

### [개념]

Immediate Number Conversion은 onChange 시점에 입력값을 바로 숫자로 변환해 State에 저장하는 방식이다.

간단한 값에는 사용할 수 있지만 빈 값, 소수점, 중간 입력 상태 처리에 주의해야 한다.

---

### [핵심]

즉시 변환 주의점:

- Number(value)
- empty string
- NaN
- decimal input
- partial input
- controlled value
- UX issue
- validation timing

---

### [실무]

즉시 변환 예:

```javascript
function handleAmountChange(event) {
  const nextValue = event.target.value;

  setValues((prevValues) => ({
    ...prevValues,
    amount: nextValue === "" ? "" : Number(nextValue),
  }));
}
```

주의:

- `Number("")`는 0이 될 수 있어 의도와 다를 수 있음
- `-`, `.`, `1.` 같은 중간 입력 처리 주의
- 금액, 수량 등은 문자열 유지 후 submit 변환이 더 안정적일 수 있음
- UI formatting과 실제 value 분리 필요 가능

---

### [FAQ]

Q. onChange에서 바로 Number로 변환해도 돼?
A. 가능하지만 빈 값과 중간 입력 상태 처리가 까다로울 수 있다.

Q. Number("")는 어떻게 돼?
A. 0으로 변환될 수 있어 필수값 검증에서 문제가 될 수 있다.

Q. 숫자 input은 문자열로 두는 게 좋아?
A. 많은 경우 입력 중에는 문자열로 두고 submit 시 변환하는 방식이 실무적으로 안전하다.

Q. 금액 입력은 어떻게 처리하는 게 좋아?
A. 표시용 문자열과 요청용 숫자 변환 기준을 분리하는 것이 좋다.

---

# 8. File Input Handling Rules

## 8.1 Single File Handling

### [개념]

Single File Handling은 사용자가 선택한 하나의 File 객체를 읽어 상태 또는 업로드 처리로 연결하는 방식이다.

File Input은 일반 text input처럼 value로 제어하지 않는다.

---

### [핵심]

Single File 요소:

- input type file
- event.target.files
- FileList
- File
- accept
- file size
- file type
- FormData
- upload
- preview

---

### [실무]

Single File 예:

```jsx
function ImageInput({ setImageFile }) {
  function handleFileChange(event) {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    setImageFile(file);
  }

  return <input type="file" accept="image/*" onChange={handleFileChange} />;
}
```

파일 검증 예:

```javascript
if (file.size > 5 * 1024 * 1024) {
  setErrors((prevErrors) => ({
    ...prevErrors,
    image: "이미지는 5MB 이하만 업로드할 수 있습니다.",
  }));
}
```

권장:

- `files?.[0]` 존재 여부 확인
- accept는 UX용이며 Backend 검증 필요
- 파일 크기와 MIME type 검증
- 파일은 FormData로 전송
- 민감 파일 업로드 주의

---

### [FAQ]

Q. File 객체는 어디서 읽어?
A. event.target.files에서 읽는다.

Q. 파일 input은 value로 제어해?
A. 일반적으로 value로 제어하지 않는다.

Q. accept 속성만 있으면 파일 타입 검증은 충분해?
A. 아니다. accept는 UX 보조이며 Backend 검증이 필요하다.

Q. 파일 크기 검증은 어디서 해?
A. Frontend에서 UX용으로 검증하고 Backend에서도 반드시 검증한다.

---

## 8.2 Multiple File Handling

### [개념]

Multiple File Handling은 여러 파일을 선택하고 배열로 관리하는 처리다.

`FileList`는 배열이 아니므로 `Array.from`으로 변환해 사용하는 것이 편하다.

---

### [핵심]

Multiple File 요소:

- multiple
- FileList
- Array.from
- File array
- file count limit
- total size
- FormData append
- preview list
- remove selected file

---

### [실무]

Multiple File 예:

```jsx
function ImagesInput({ setImageFiles }) {
  function handleFilesChange(event) {
    const files = Array.from(event.target.files ?? []);

    setImageFiles(files);
  }

  return (
    <input type="file" accept="image/*" multiple onChange={handleFilesChange} />
  );
}
```

FormData 연결:

```javascript
const formData = new FormData();

imageFiles.forEach((file) => {
  formData.append("images", file);
});
```

권장:

- FileList를 배열로 변환
- 파일 개수 제한
- 개별 파일 크기 제한
- 전체 업로드 용량 제한
- 미리보기 제거 기능 고려
- FormData key와 Backend field name 일치

---

### [FAQ]

Q. 여러 파일은 어떻게 읽어?
A. event.target.files를 Array.from으로 배열 변환한다.

Q. multiple file input 초기값은 뭐가 좋아?
A. 빈 배열 `[]`로 관리하는 것이 좋다.

Q. FormData에 여러 파일은 어떻게 넣어?
A. 같은 key로 여러 번 append하거나 Backend 규칙에 맞게 append한다.

Q. 파일 제거 기능은 어떻게 구현해?
A. 선택된 File 배열에서 해당 파일을 filter로 제거한다.

---

# 9. Input Normalization Rules

## 9.1 Trim Rules

### [개념]

Trim은 문자열 앞뒤 공백을 제거하는 정규화 처리다.

Form에서는 입력 중 trim과 제출 시 trim을 구분해야 한다.

---

### [핵심]

Trim 기준:

- trim on submit
- trim on blur
- no aggressive trim
- whitespace validation
- empty string after trim
- Request Body Mapping
- username caution
- password no trim caution

---

### [실무]

Submit 시 trim:

```javascript
const requestBody = {
  title: values.title.trim(),
  content: values.content.trim(),
};
```

Validation 예:

```javascript
if (!values.title.trim()) {
  errors.title = "제목을 입력해 주세요.";
}
```

주의:

- 입력 중 매번 trim하면 UX가 불편할 수 있음
- title, content, nickname은 submit 시 trim 가능
- password는 임의 trim 금지 또는 정책 명확화
- 검색어는 submit 시 trim 권장
- 공백만 입력한 값은 invalid 처리 가능

---

### [FAQ]

Q. trim은 언제 하는 게 좋아?
A. 보통 submit 또는 validation 단계에서 처리하는 것이 안전하다.

Q. onChange에서 바로 trim해도 돼?
A. 가능하지만 사용자의 입력 경험을 방해할 수 있다.

Q. password도 trim해도 돼?
A. 정책에 따라 다르지만 임의로 trim하지 않는 것이 안전하다.

Q. 공백만 입력한 값은 어떻게 처리해?
A. trim 후 빈 문자열이면 invalid로 처리하는 것이 일반적이다.

---

## 9.2 Empty String and Null Handling

### [개념]

Empty String and Null Handling은 빈 입력값을 `""`, `null`, `undefined`, 또는 요청 제외 중 어떤 방식으로 처리할지 결정하는 기준이다.

Frontend Form State와 Backend Request DTO의 빈 값 기준은 다를 수 있다.

---

### [핵심]

빈 값 처리 기준:

- empty string
- null
- undefined
- optional field
- required field
- request omit
- query param omit
- DTO mapping
- Backend contract

---

### [실무]

Form State:

```javascript
const values = {
  keyword: "",
  category: "",
};
```

Query Param Mapping:

```javascript
const params = new URLSearchParams();

if (values.keyword.trim()) {
  params.set("keyword", values.keyword.trim());
}

if (values.category) {
  params.set("category", values.category);
}
```

Request Body Mapping:

```javascript
const requestBody = {
  nickname: values.nickname.trim(),
  bio: values.bio.trim() || null,
};
```

권장:

- Form State에서는 Controlled 안정성을 위해 빈 문자열 사용
- Request Body에서는 Backend DTO 기준에 맞게 null 또는 제외 처리
- Query Param에서는 빈 문자열 제외 권장
- 필수값은 validation에서 차단
- optional field 기준 명확화

---

### [FAQ]

Q. Form State에서 빈 값은 null로 둬도 돼?
A. 가능하지만 input value에는 빈 문자열이 더 안정적이다.

Q. optional field가 비어 있으면 어떻게 보내?
A. Backend 계약에 따라 null로 보내거나 field를 제외한다.

Q. 검색 query param에 빈 문자열을 넣어도 돼?
A. 보통 제외하는 것이 깔끔하다.

Q. 빈 문자열과 null 기준은 어디서 맞춰?
A. Backend Request DTO 계약과 Frontend Request Mapping에서 맞춘다.

---

# 10. onBlur Handling Rules

## 10.1 onBlur Handling

### [개념]

onBlur Handling은 사용자가 input에서 focus를 벗어났을 때 실행되는 처리다.

Touched State 업데이트, blur validation, 입력값 정규화에 사용할 수 있다.

---

### [핵심]

onBlur 사용 대상:

- touched update
- field validation
- trim on blur
- format check
- duplicate check trigger
- focus out event
- UX validation timing

---

### [실무]

Touched 업데이트:

```javascript
function handleBlur(event) {
  const { name } = event.target;

  setTouched((prevTouched) => ({
    ...prevTouched,
    [name]: true,
  }));
}
```

Field에 연결:

```jsx
<input
  name="email"
  value={values.email}
  onChange={handleChange}
  onBlur={handleBlur}
/>
```

Blur Validation 예:

```javascript
function handleEmailBlur(event) {
  const email = event.target.value.trim();

  setTouched((prevTouched) => ({
    ...prevTouched,
    email: true,
  }));

  if (!email.includes("@")) {
    setErrors((prevErrors) => ({
      ...prevErrors,
      email: "이메일 형식이 올바르지 않습니다.",
    }));
  }
}
```

권장:

- touched update는 onBlur에서 처리
- 실시간 validation이 부담스러우면 blur validation 사용
- 중복 확인 API는 blur 또는 명시 버튼 기준 검토
- onBlur에서 과도한 자동 변환 주의

---

### [FAQ]

Q. onBlur는 언제 실행돼?
A. input에서 focus가 벗어날 때 실행된다.

Q. onBlur는 어디에 사용해?
A. touched 업데이트, field validation, 일부 정규화 처리에 사용한다.

Q. onChange validation과 onBlur validation 중 뭐가 좋아?
A. 실시간 피드백은 onChange, 부담이 적은 검증은 onBlur가 적합할 수 있다.

Q. 이메일 중복 검사를 onBlur에서 해도 돼?
A. 가능하지만 API 호출 빈도와 UX를 고려해야 한다.

---

# 11. Field Error Clearing Rules

## 11.1 Clear Field Error on Change

### [개념]

Clear Field Error on Change는 사용자가 해당 field를 다시 수정할 때 기존 에러 메시지를 제거하는 패턴이다.

서버 에러 또는 validation error가 오래 남아 현재 입력값과 맞지 않는 문제를 줄인다.

---

### [핵심]

Error Clearing 기준:

- clear field error
- onChange
- errors[name]
- server error reset
- stale error
- validation recheck
- user correction
- field feedback

---

### [실무]

onChange에서 해당 field error 제거:

```javascript
function handleChange(event) {
  const { name, value } = event.target;

  setValues((prevValues) => ({
    ...prevValues,
    [name]: value,
  }));

  setErrors((prevErrors) => ({
    ...prevErrors,
    [name]: "",
  }));
}
```

key 제거 방식:

```javascript
function clearFieldError(fieldName) {
  setErrors((prevErrors) => {
    const nextErrors = { ...prevErrors };
    delete nextErrors[fieldName];
    return nextErrors;
  });
}
```

권장:

- 수정한 field의 기존 error만 제거
- global error는 submit 재시도 시 제거 가능
- 입력할 때 즉시 제거하거나 재검증 후 갱신
- 서버 field error도 재입력 시 제거 가능
- 에러 제거 기준을 Form 전체에서 통일

---

### [FAQ]

Q. 입력을 수정하면 기존 에러를 지워야 해?
A. 권장한다. 사용자가 수정 중인데 이전 에러가 계속 남으면 혼란스러울 수 있다.

Q. 모든 에러를 onChange마다 지워도 돼?
A. 보통 수정한 field의 에러만 지우는 것이 좋다.

Q. 서버 에러도 입력 수정 시 지워도 돼?
A. 가능하다. 다시 제출하거나 재검증하면 새 에러를 받을 수 있다.

Q. global error도 onChange에서 지워야 해?
A. 상황에 따라 다르다. 로그인 실패 메시지는 입력 수정 시 지울 수 있고, 서버 장애 메시지는 재시도 시 지울 수 있다.

---

# 12. Custom Component Handling Rules

## 12.1 Custom Field Component Input Contract

### [개념]

Custom Field Component는 label, input, error message, 접근성 속성을 재사용 가능한 단위로 묶은 Component다.

Custom Field는 value, name, onChange, error, disabled 같은 입력 계약을 명확히 가져야 한다.

---

### [핵심]

Custom Field props:

- id
- name
- label
- value
- checked
- onChange
- onBlur
- error
- required
- disabled
- aria-invalid
- aria-describedby

---

### [실무]

TextField 예:

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
  onBlur?: (event: FocusEvent<HTMLInputElement>) => void;
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
  onBlur,
}: TextFieldProps) {
  const errorId = `${id}-error`;

  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        name={name}
        value={value}
        required={required}
        disabled={disabled}
        onChange={onChange}
        onBlur={onBlur}
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

권장:

- 범용 Field와 도메인 Field 구분
- id와 name 전달 명확화
- error 접근성 연결 포함
- onChange event contract 유지
- checkbox, radio, file은 별도 Component 검토

---

### [FAQ]

Q. Custom Field Component는 왜 필요해?
A. label, input, error, 접근성 속성을 반복하지 않고 일관되게 관리하기 위해 필요하다.

Q. TextField에 name이 꼭 필요해?
A. Common Change Handler를 사용한다면 필요하다.

Q. 모든 input을 하나의 Field Component로 처리해도 돼?
A. text 계열은 가능하지만 checkbox, radio, file은 별도 Component가 더 명확할 수 있다.

Q. Custom Field에서도 aria 속성을 넣어야 해?
A. 권장한다. error와 input을 연결해 접근성을 개선할 수 있다.

---

## 12.2 Custom Select and Checkbox Contract

### [개념]

Custom Select와 Checkbox Component는 일반 text input과 값 처리 방식이 다르므로 props 계약을 명확히 분리해야 한다.

Select는 value를 사용하고 Checkbox는 checked를 사용한다.

---

### [핵심]

Custom Field 계약 차이:

| Component     | Control Prop    | Change Value         |
| ------------- | --------------- | -------------------- |
| TextField     | value           | event.target.value   |
| SelectField   | value           | event.target.value   |
| CheckboxField | checked         | event.target.checked |
| RadioField    | checked + value | event.target.value   |
| FileField     | files           | event.target.files   |

---

### [실무]

CheckboxField 예:

```tsx
type CheckboxFieldProps = {
  name: string;
  label: string;
  checked: boolean;
  onChange: (event: ChangeEvent<HTMLInputElement>) => void;
};

function CheckboxField({ name, label, checked, onChange }: CheckboxFieldProps) {
  return (
    <label>
      <input
        type="checkbox"
        name={name}
        checked={checked}
        onChange={onChange}
      />
      {label}
    </label>
  );
}
```

SelectField 예:

```tsx
type SelectFieldProps = {
  id: string;
  name: string;
  label: string;
  value: string;
  options: { label: string; value: string }[];
  onChange: (event: ChangeEvent<HTMLSelectElement>) => void;
};

function SelectField({
  id,
  name,
  label,
  value,
  options,
  onChange,
}: SelectFieldProps) {
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <select id={id} name={name} value={value} onChange={onChange}>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}
```

주의:

- CheckboxField에 value만 전달하지 않음
- Select option value와 Backend code 일치
- Radio group은 같은 name 유지
- FileField는 value 제어하지 않음
- Custom Component 내부에서 name을 누락하지 않음

---

### [FAQ]

Q. CheckboxField는 value를 받아야 해 checked를 받아야 해?
A. 선택 여부 제어를 위해 checked를 받는 것이 맞다.

Q. SelectField options에는 무엇이 필요해?
A. 화면 표시용 label과 전송용 value가 필요하다.

Q. Custom Component에서 name을 숨겨도 돼?
A. 공통 handler와 Request Mapping을 위해 명확히 전달하는 것이 좋다.

Q. FileField도 value를 prop으로 받아야 해?
A. 일반적으로 file input은 value로 제어하지 않는다.

---

# 13. Input Handling Troubleshooting

## 13.1 Input Not Updating

### [개념]

Input Not Updating은 사용자가 입력해도 input 값이 화면에 반영되지 않는 문제다.

Controlled Component에서 value와 onChange 연결이 잘못되었을 때 자주 발생한다.

---

### [핵심]

주요 원인:

- value만 있고 onChange 없음
- onChange에서 setState 미호출
- name과 values key 불일치
- State 직접 mutation
- disabled 상태
- readOnly 상태
- 초기값 undefined
- 잘못된 event value 사용
- checkbox value 사용

---

### [실무]

Debug Flow:

```text
Input value 확인
→ onChange 연결 확인
→ setState 호출 확인
→ event.target.name 확인
→ values key 확인
→ direct mutation 확인
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

name 불일치 예:

```jsx
<input name="userEmail" value={values.email} onChange={handleChange} />
```

이 경우 Common Change Handler는 `values.userEmail`을 업데이트하고 `values.email`은 바뀌지 않을 수 있다.

---

### [FAQ]

Q. input에 입력이 안 되는 이유는?
A. value만 있고 onChange가 없거나 State 업데이트가 잘못되었을 가능성이 크다.

Q. name과 values key가 다르면 어떻게 돼?
A. 공통 handler에서 다른 key를 업데이트해 화면 value가 바뀌지 않을 수 있다.

Q. setState를 호출했는데도 값이 안 바뀌면?
A. State를 직접 mutation하고 같은 객체를 다시 넣었는지 확인해야 한다.

Q. checkbox가 안 바뀌는 이유는?
A. checked가 아니라 value로 제어하거나 onChange에서 checked를 반영하지 않았을 수 있다.

---

## 13.2 Wrong Value Type

### [개념]

Wrong Value Type은 input type과 Form State 값의 타입이 맞지 않아 발생하는 문제다.

checkbox에 문자열을 넣거나, number input 값을 숫자로만 강제하거나, select value가 option value와 맞지 않을 때 발생한다.

---

### [핵심]

주요 원인:

- checkbox value vs checked 혼동
- number string conversion 누락
- select option mismatch
- array field에 string 저장
- radio value enum 불일치
- null value 전달
- undefined value 전달

---

### [실무]

문제 예:

```jsx
<input type="checkbox" value={values.agreed} onChange={handleChange} />
```

수정 예:

```jsx
<input type="checkbox" checked={values.agreed} onChange={handleChange} />
```

select mismatch 예:

```jsx
<select value={values.category}>
  <option value="NOTICE">공지</option>
</select>
```

`values.category`가 `"notice"`이면 option value와 일치하지 않아 의도한 선택이 표시되지 않을 수 있다.

---

### [FAQ]

Q. checkbox 값이 이상하게 들어가는 이유는?
A. checked가 아니라 value를 사용했을 가능성이 크다.

Q. select가 선택되어 보이지 않는 이유는?
A. select value와 option value가 일치하지 않을 수 있다.

Q. number input 값 타입이 왜 문자열이야?
A. DOM input value는 대부분 문자열로 전달되기 때문이다.

Q. undefined value가 문제를 만들 수 있어?
A. 그렇다. Controlled / Uncontrolled Warning이나 표시 오류가 발생할 수 있다.

---

## 13.3 Common Handler Not Working

### [개념]

Common Handler Not Working은 공통 `handleChange`가 여러 input 값을 정상 업데이트하지 못하는 문제다.

대부분 `name` 누락, key 불일치, checkbox 처리 누락, event contract 불일치가 원인이다.

---

### [핵심]

점검 대상:

- input name exists
- values key exists
- event.target.name
- event.target.value
- event.target.checked
- custom component event forwarding
- nested field issue
- typo

---

### [실무]

Debug Flow:

```text
Check input name
→ Check values key
→ Log event.target.name
→ Log event.target.value / checked
→ Check setValues callback
→ Check custom component props
→ Check typo
```

좋은 예:

```jsx
<input name="email" value={values.email} onChange={handleChange} />
```

문제 예:

```jsx
<TextField value={values.email} onChange={handleChange} />
```

Custom TextField 내부에서 `name`을 input에 전달하지 않으면 공통 handler가 정상 동작하지 않는다.

---

### [FAQ]

Q. Common Change Handler가 동작하지 않는 이유는?
A. input name이 없거나 values key와 일치하지 않을 가능성이 크다.

Q. Custom Field에서 공통 handler가 안 돼?
A. Custom Field 내부 input에 name과 onChange가 제대로 전달되는지 확인해야 한다.

Q. checkbox만 공통 handler에서 이상해?
A. checkbox는 value가 아니라 checked를 사용하도록 분기해야 한다.

Q. nested object field도 공통 handler로 처리 가능해?
A. 가능하지만 단순 handler로는 어렵고 별도 path update helper가 필요할 수 있다.

---

# 14. Input Handling Checklist

## 14.1 Implementation Checklist

### [개념]

Input Handling Checklist는 Form Field별 값 읽기, State Update, Field Type 처리, 오류 가능성을 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] 모든 Controlled Input에 value 또는 checked가 있는가?
- [ ] 모든 Controlled Input에 onChange가 연결되어 있는가?
- [ ] input name과 values key가 일치하는가?
- [ ] Common Change Handler에서 name/value를 읽는가?
- [ ] checkbox는 checked를 사용하는가?
- [ ] multiple checkbox는 배열 추가/제거로 처리하는가?
- [ ] radio group은 같은 name을 사용하는가?
- [ ] radio checked는 현재 값과 option value를 비교하는가?
- [ ] select option value가 Backend code 또는 enum과 일치하는가?
- [ ] multiple select는 selectedOptions를 배열로 변환하는가?
- [ ] number input의 문자열/숫자 변환 기준이 명확한가?
- [ ] file input은 files에서 File 객체를 읽는가?
- [ ] FormData key가 Backend field name과 일치하는가?
- [ ] trim 시점이 정의되어 있는가?
- [ ] 빈 문자열/null/undefined 처리 기준이 있는가?
- [ ] onBlur 사용 기준이 정의되어 있는가?
- [ ] field 수정 시 기존 field error 제거 기준이 있는가?
- [ ] Custom Field Component가 name/onChange/error를 전달하는가?
- [ ] State 직접 mutation 없이 업데이트하는가?
```

---

### [실무]

검수 Flow:

```text
Field Type Identify
→ Value Read Rule Check
→ name-key Mapping Check
→ State Update Check
→ Type Conversion Check
→ Normalization Check
→ Error Clearing Check
→ Custom Component Contract Check
→ Troubleshooting Review
```

---

### [FAQ]

Q. Input Handling 검수에서 가장 중요한 것은?
A. field type별 값 읽기 기준, name-key 일치, onChange State Update, checkbox checked 처리다.

Q. Input Handling 다음에는 무엇을 검토해?
A. Validation, Server Validation Error Handling, Submit Flow, Request Body Mapping을 검토한다.

---

# Retrieval Queries

### [FAQ]

Q. Input Handling이 뭐야?
A. 사용자의 입력 이벤트를 받아 Form State를 업데이트하는 React Form 처리 흐름이다.

Q. Input Handling에서 가장 중요한 것은 뭐야?
A. field type별 값 읽기 기준과 input name, Form State key를 일치시키는 것이다.

Q. 모든 input은 event.target.value로 처리해?
A. 아니다. checkbox는 checked, file input은 files, multiple select는 selectedOptions를 사용한다.

Q. 여러 input을 하나의 handleChange로 처리할 수 있어?
A. 가능하다. input name과 values 객체 key를 맞추면 공통 handler로 처리할 수 있다.

Q. Common Change Handler의 핵심 조건은 뭐야?
A. input name과 values key가 일치해야 한다.

Q. name이 없으면 공통 handler가 동작해?
A. 어렵다. 어떤 key를 업데이트할지 알 수 없기 때문이다.

Q. checkbox도 Common Change Handler로 처리할 수 있어?
A. 가능하다. 다만 type이 checkbox일 때 checked를 사용해야 한다.

Q. checkbox 값을 value로 읽으면 안 돼?
A. 선택 여부가 아니라 value 속성값을 읽게 되므로 일반적으로 checked를 사용한다.

Q. 약관 동의 checkbox는 어떤 값으로 관리해?
A. boolean 값으로 관리한다.

Q. 여러 checkbox도 같은 방식으로 처리해?
A. 아니다. 여러 checkbox는 배열 추가/제거 로직이 필요하다.

Q. Text Input 값은 어디서 읽어?
A. event.target.value에서 읽는다.

Q. 입력 중에 trim을 바로 적용해도 돼?
A. 가능하지만 사용자가 의도한 공백 입력을 방해할 수 있어 보통 submit 시점에 처리한다.

Q. Text Input 초기값은 무엇이 좋아?
A. 빈 문자열 `""`이 안전하다.

Q. textarea도 event.target.value로 읽어?
A. 그렇다. textarea 값도 event.target.value로 읽는다.

Q. textarea 줄바꿈은 유지돼?
A. value에 문자열로 저장되며 줄바꿈도 포함된다.

Q. 리뷰 내용은 submit 전에 trim해야 해?
A. 대부분 권장한다. 공백만 입력한 리뷰를 방지할 수 있다.

Q. select 값은 어디서 읽어?
A. event.target.value에서 선택된 option value를 읽는다.

Q. option value는 화면 문구로 넣어도 돼?
A. 보통 Backend enum 또는 code 값을 넣는 것이 좋다.

Q. 전체 선택은 어떻게 처리해?
A. value를 빈 문자열로 두고 Request Mapping에서 제외하거나 null로 변환할 수 있다.

Q. multiple select 값은 어떻게 읽어?
A. event.target.selectedOptions를 Array.from으로 배열 변환한다.

Q. multiple select 초기값은 뭐가 좋아?
A. 빈 배열 `[]`이 적합하다.

Q. multiple select와 checkbox group 중 뭐가 좋아?
A. 선택 항목이 명확히 보이는 UX가 필요하면 checkbox group이 더 적합할 수 있다.

Q. checkbox 선택 여부는 어떻게 읽어?
A. event.target.checked로 읽는다.

Q. checkbox 초기값은 뭐가 좋아?
A. false가 일반적이다.

Q. checked와 value 중 무엇을 써?
A. 선택 여부는 checked를 사용한다.

Q. 약관 동의 checkbox는 검증해야 해?
A. 필수 동의라면 Client Validation과 Server Validation 모두 필요하다.

Q. 여러 checkbox 선택값은 어떻게 저장해?
A. 선택된 code 또는 id를 배열로 저장한다.

Q. multiple checkbox의 checked는 어떻게 계산해?
A. selectedValues.includes(value)를 사용한다.

Q. checkbox를 해제하면 어떻게 처리해?
A. filter로 해당 값을 배열에서 제거한다.

Q. radio button 값은 어떻게 읽어?
A. 선택된 radio의 event.target.value를 읽는다.

Q. radio checked는 어떻게 설정해?
A. 현재 State 값과 radio value가 같을 때 checked를 true로 설정한다.

Q. radio group은 왜 같은 name을 써?
A. 같은 그룹에서 하나만 선택되도록 하기 위해서다.

Q. radio value는 어떤 값으로 맞춰?
A. Backend enum 또는 code 값과 일치시키는 것이 좋다.

Q. number input 값은 number로 들어와?
A. 대부분 문자열로 들어온다.

Q. 숫자 변환은 언제 하는 게 좋아?
A. 입력 중에는 문자열로 관리하고 submit 또는 validation 단계에서 변환하는 방식이 안전하다.

Q. 빈 숫자 input은 어떻게 처리해?
A. 빈 문자열로 관리하고 필수값 검증 또는 null 변환 기준을 둔다.

Q. onChange에서 바로 Number로 변환해도 돼?
A. 가능하지만 빈 값과 중간 입력 상태 처리가 까다로울 수 있다.

Q. Number("")는 어떻게 돼?
A. 0으로 변환될 수 있어 필수값 검증에서 문제가 될 수 있다.

Q. 금액 입력은 어떻게 처리하는 게 좋아?
A. 표시용 문자열과 요청용 숫자 변환 기준을 분리하는 것이 좋다.

Q. File 객체는 어디서 읽어?
A. event.target.files에서 읽는다.

Q. 파일 input은 value로 제어해?
A. 일반적으로 value로 제어하지 않는다.

Q. 파일 크기 검증은 어디서 해?
A. Frontend에서 UX용으로 검증하고 Backend에서도 반드시 검증한다.

Q. 여러 파일은 어떻게 읽어?
A. event.target.files를 Array.from으로 배열 변환한다.

Q. multiple file input 초기값은 뭐가 좋아?
A. 빈 배열 `[]`로 관리하는 것이 좋다.

Q. FormData에 여러 파일은 어떻게 넣어?
A. 같은 key로 여러 번 append하거나 Backend 규칙에 맞게 append한다.

Q. trim은 언제 하는 게 좋아?
A. 보통 submit 또는 validation 단계에서 처리하는 것이 안전하다.

Q. onChange에서 바로 trim해도 돼?
A. 가능하지만 사용자의 입력 경험을 방해할 수 있다.

Q. password도 trim해도 돼?
A. 정책에 따라 다르지만 임의로 trim하지 않는 것이 안전하다.

Q. 공백만 입력한 값은 어떻게 처리해?
A. trim 후 빈 문자열이면 invalid로 처리하는 것이 일반적이다.

Q. Form State에서 빈 값은 null로 둬도 돼?
A. 가능하지만 input value에는 빈 문자열이 더 안정적이다.

Q. optional field가 비어 있으면 어떻게 보내?
A. Backend 계약에 따라 null로 보내거나 field를 제외한다.

Q. 검색 query param에 빈 문자열을 넣어도 돼?
A. 보통 제외하는 것이 깔끔하다.

Q. onBlur는 언제 실행돼?
A. input에서 focus가 벗어날 때 실행된다.

Q. onBlur는 어디에 사용해?
A. touched 업데이트, field validation, 일부 정규화 처리에 사용한다.

Q. onChange validation과 onBlur validation 중 뭐가 좋아?
A. 실시간 피드백은 onChange, 부담이 적은 검증은 onBlur가 적합할 수 있다.

Q. 입력을 수정하면 기존 에러를 지워야 해?
A. 권장한다. 사용자가 수정 중인데 이전 에러가 계속 남으면 혼란스러울 수 있다.

Q. 모든 에러를 onChange마다 지워도 돼?
A. 보통 수정한 field의 에러만 지우는 것이 좋다.

Q. 서버 에러도 입력 수정 시 지워도 돼?
A. 가능하다. 다시 제출하거나 재검증하면 새 에러를 받을 수 있다.

Q. Custom Field Component는 왜 필요해?
A. label, input, error, 접근성 속성을 반복하지 않고 일관되게 관리하기 위해 필요하다.

Q. TextField에 name이 꼭 필요해?
A. Common Change Handler를 사용한다면 필요하다.

Q. CheckboxField는 value를 받아야 해 checked를 받아야 해?
A. 선택 여부 제어를 위해 checked를 받는 것이 맞다.

Q. SelectField options에는 무엇이 필요해?
A. 화면 표시용 label과 전송용 value가 필요하다.

Q. input에 입력이 안 되는 이유는?
A. value만 있고 onChange가 없거나 State 업데이트가 잘못되었을 가능성이 크다.

Q. name과 values key가 다르면 어떻게 돼?
A. 공통 handler에서 다른 key를 업데이트해 화면 value가 바뀌지 않을 수 있다.

Q. select가 선택되어 보이지 않는 이유는?
A. select value와 option value가 일치하지 않을 수 있다.

Q. Common Change Handler가 동작하지 않는 이유는?
A. input name이 없거나 values key와 일치하지 않을 가능성이 크다.

Q. Custom Field에서 공통 handler가 안 돼?
A. Custom Field 내부 input에 name과 onChange가 제대로 전달되는지 확인해야 한다.

Q. Input Handling 다음 문서는 뭐가 좋아?
A. Validation, Server Validation Error Handling, Submit Flow, Request Body Mapping 순서가 좋다.
