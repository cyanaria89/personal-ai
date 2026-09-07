# Frontend Accessibility Part03 - Form Label Error Accessibility

---

# 1. Form Accessibility

## 1.1 Form Accessibility Purpose

### [개념]

Form Accessibility는 사용자가 입력 필드의 목적, 필수 여부, 현재 상태, 오류 원인, 수정 방법을 명확히 이해하고 입력을 완료할 수 있게 만드는 기준이다.

Frontend Form은 시각적으로만 동작하면 충분하지 않다.

키보드 사용자, 스크린 리더 사용자, 자동완성 사용자, 오류 수정이 필요한 사용자도 Form을 사용할 수 있어야 한다.

---

### [핵심]

Form Accessibility 핵심 요소:

- `form`
- `label`
- `input`
- `select`
- `textarea`
- `fieldset`
- `legend`
- `required`
- `aria-required`
- `aria-invalid`
- `aria-describedby`
- `aria-labelledby`
- `role="alert"`
- field error
- global error
- validation message
- accessible name
- focus management

---

### [실무]

2026 실무 기준에서 Form 접근성은 아래 흐름으로 검토한다.

```text
Form Control 확인
→ Label 연결 확인
→ Required 표시 확인
→ Helper Text 연결 확인
→ Error Message 연결 확인
→ aria-invalid 상태 확인
→ Submit 실패 시 Focus 이동 확인
→ Keyboard 입력 / 제출 확인
→ Testing Library getByLabelText 검증
```

실무 기준:

- 모든 주요 input은 label과 연결
- placeholder는 label 대체 금지
- 필수 입력은 시각적 표시와 의미 전달을 함께 고려
- 오류 메시지는 input과 연결
- 오류 상태는 `aria-invalid`로 표현
- 도움말은 `aria-describedby`로 연결
- Form submit 실패 시 첫 오류 field focus 이동 고려
- keyboard만으로 입력, 선택, 제출 가능해야 함
- 내부 서버 오류나 stack trace를 사용자 메시지로 노출하지 않음

---

### [FAQ]

Q. Form Accessibility는 왜 중요해?
A. 사용자가 입력 필드의 목적, 필수 여부, 오류 원인, 수정 방법을 이해하고 Form을 완료해야 하기 때문이다.

Q. 화면상으로 input이 보이면 충분해?
A. 아니다. label, keyboard, error message, focus, accessible name이 함께 제공되어야 한다.

Q. placeholder가 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 label을 안정적으로 대체하지 못한다.

Q. Form 접근성은 Testing과도 관련 있어?
A. 그렇다. getByLabelText, getByRole 같은 Query는 접근성 구조를 기반으로 Form 요소를 찾는다.

---

# 2. Label Rules

## 2.1 Label Connection

### [개념]

Label은 Form Control이 어떤 값을 입력받는지 설명하는 요소다.

모든 주요 Form Control은 사용자가 목적을 이해할 수 있도록 label과 연결되어야 한다.

Label 연결은 스크린 리더, 브라우저 자동완성, Testing Library, 클릭 영역 확장에 영향을 준다.

---

### [핵심]

Label 연결 방식:

- `label htmlFor`
- `input id`
- wrapping label
- `aria-labelledby`
- `aria-label`

Label 우선순위:

1. 보이는 label
2. wrapping label
3. `aria-labelledby`
4. `aria-label`

적용 대상:

- text input
- email input
- password input
- search input
- checkbox
- radio
- select
- textarea
- file input
- date input

---

### [실무]

명시적 label 연결:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

Wrapping label:

```jsx
<label>
  <input type="checkbox" name="agree" />
  약관에 동의합니다.
</label>
```

검색 input:

```jsx
<label htmlFor="keyword">검색어</label>
<input id="keyword" name="keyword" type="search" />
```

시각적 label이 어려운 경우:

```jsx
<input type="search" name="keyword" aria-label="축제 검색어" />
```

실무 기준:

- label `htmlFor`와 input `id`는 동일해야 함
- `id` 중복 금지
- placeholder만 사용하는 Form 지양
- checkbox / radio도 label 연결
- icon search input도 accessible name 필요
- label text는 입력 목적을 명확히 표현
- label 없는 input은 `getByLabelText` 실패 원인이 됨

---

### [FAQ]

Q. input과 label은 어떻게 연결해?
A. label의 htmlFor와 input의 id를 같은 값으로 연결한다.

Q. label 없이 aria-label만 써도 돼?
A. 가능하지만 보이는 label이 더 명확하다. 디자인상 어렵다면 aria-label을 보완적으로 사용할 수 있다.

Q. checkbox도 label이 필요해?
A. 필요하다. 체크박스가 무엇을 의미하는지 사용자가 알 수 있어야 한다.

Q. getByLabelText가 실패하는 이유는?
A. input과 label이 연결되지 않았거나 label 텍스트가 예상과 다를 수 있다.

---

## 2.2 Placeholder Is Not Label

### [개념]

Placeholder는 입력 예시나 짧은 힌트를 제공하는 속성이다.

Placeholder는 label을 대체하지 않는다.

입력 중 사라질 수 있고, 항상 접근 가능한 이름으로 안정적으로 사용되지 않으며, 사용자가 입력 목적을 다시 확인하기 어렵게 만든다.

---

### [핵심]

Placeholder 한계:

- 입력 중 사라짐
- label보다 시각적 대비가 낮을 수 있음
- 입력 목적을 지속적으로 제공하지 못함
- 오류 수정 시 참고하기 어려움
- 스크린 리더 label 대체로 부적합
- Testing Library `getByLabelText` 실패 가능

사용 기준:

- label은 필수 기준
- placeholder는 예시 또는 보조 힌트
- 중요한 정보는 placeholder에만 두지 않음
- 형식 안내는 helper text로 분리 가능

---

### [실무]

나쁜 예:

```jsx
<input type="email" placeholder="이메일" />
```

좋은 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  placeholder="example@email.com"
/>
```

Helper Text와 함께 사용하는 예:

```jsx
<label htmlFor="phone">휴대폰 번호</label>
<input
  id="phone"
  name="phone"
  type="tel"
  aria-describedby="phone-help"
/>
<p id="phone-help">숫자만 입력해 주세요.</p>
```

실무 기준:

- placeholder는 예시 형식에만 제한적으로 사용
- 필수 설명은 label 또는 helper text로 제공
- placeholder 색상 대비 부족 주의
- placeholder만 보고 작성된 Form은 접근성 검토 대상
- Testing에서는 `getByPlaceholderText`보다 `getByLabelText` 우선

---

### [FAQ]

Q. placeholder가 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 label을 안정적으로 대체하지 못한다.

Q. placeholder는 언제 써?
A. 입력 예시나 형식 힌트를 보조적으로 제공할 때 사용한다.

Q. placeholder에 중요한 안내를 넣어도 돼?
A. 권장하지 않는다. 중요한 안내는 label이나 helper text로 제공한다.

Q. getByPlaceholderText를 쓰면 되지 않아?
A. 테스트는 가능하지만 접근성 좋은 Form은 getByLabelText로 찾을 수 있어야 한다.

---

## 2.3 Accessible Name for Form Control

### [개념]

Form Control의 Accessible Name은 스크린 리더와 Testing Library가 input, select, textarea를 식별하는 이름이다.

Form Control은 명확한 Accessible Name을 가져야 사용자가 입력 목적을 이해할 수 있다.

---

### [핵심]

Accessible Name 제공 방식:

- `label`
- `aria-label`
- `aria-labelledby`
- wrapping label
- fieldset / legend context
- visible text

주의 대상:

- icon search input
- hidden label input
- custom input
- date picker
- file upload
- checkbox group
- radio group

---

### [실무]

보이는 label:

```jsx
<label htmlFor="nickname">닉네임</label>
<input id="nickname" name="nickname" />
```

`aria-labelledby` 예:

```jsx
<h2 id="profile-title">프로필 수정</h2>

<label id="nickname-label" htmlFor="nickname">
  닉네임
</label>
<input
  id="nickname"
  name="nickname"
  aria-labelledby="profile-title nickname-label"
/>
```

Icon search input:

```jsx
<div className="search-box">
  <SearchIcon aria-hidden="true" />
  <label htmlFor="festival-keyword" className="sr-only">
    축제 검색어
  </label>
  <input id="festival-keyword" name="keyword" type="search" />
</div>
```

실무 기준:

- Visible label 우선
- `aria-label`은 화면에 label을 둘 수 없을 때 사용
- `aria-labelledby`는 기존 텍스트를 이름으로 연결할 때 사용
- 같은 이름의 input이 반복되면 context 제공
- `getByLabelText("이메일")`로 찾을 수 있어야 함
- Accessible Name과 visible label 의미가 충돌하지 않게 함

---

### [FAQ]

Q. Form Control의 Accessible Name이 뭐야?
A. 스크린 리더와 Testing Library가 input의 이름으로 인식하는 텍스트다.

Q. aria-label과 label은 뭐가 달라?
A. label은 시각적으로도 보이는 설명이고 aria-label은 보조기술에 이름을 제공하는 속성이다.

Q. aria-labelledby는 언제 써?
A. 화면에 이미 있는 텍스트를 Form Control의 이름으로 연결할 때 사용한다.

Q. 같은 label이 반복되면 문제야?
A. 문맥이 부족할 수 있다. 그룹 제목이나 구체적인 label로 구분하는 것이 좋다.

---

# 3. Required Field Rules

## 3.1 Required Field Indication

### [개념]

Required Field는 사용자가 반드시 입력해야 하는 필드다.

필수 입력 여부는 시각적으로도 이해 가능해야 하고, 보조기술에도 의미가 전달되어야 한다.

---

### [핵심]

Required Field 표현 방식:

- `required`
- `aria-required`
- visible required text
- asterisk explanation
- validation message
- field level 안내
- form level 안내

우선 기준:

1. Native input에는 `required`
2. Custom Widget에는 `aria-required` 고려
3. 별표 사용 시 의미 설명 제공
4. 오류 메시지로 수정 방법 제공

---

### [실무]

필수값 예:

```jsx
<label htmlFor="nickname">
  닉네임 <span aria-hidden="true">*</span>
</label>
<input
  id="nickname"
  name="nickname"
  required
/>
<p>* 표시는 필수 입력 항목입니다.</p>
```

텍스트로 명확히 제공:

```jsx
<label htmlFor="email">
  이메일 <span>(필수)</span>
</label>
<input id="email" name="email" type="email" required />
```

Custom Widget 예:

```jsx
<div role="combobox" aria-required="true" aria-labelledby="region-label">
  ...
</div>
```

실무 기준:

- 별표만 제공하지 말고 의미 설명 포함
- 가능하면 “필수” 텍스트를 직접 제공
- `required`는 브라우저 기본 validation을 발생시킬 수 있음
- Custom validation 사용 시 native validation과 UX 충돌 주의
- 필수값 미입력 시 명확한 error message 제공

---

### [FAQ]

Q. 필수값 표시로 별표만 붙이면 돼?
A. 별표의 의미를 설명하거나 “필수” 텍스트를 함께 제공하는 것이 좋다.

Q. required와 aria-required를 둘 다 써야 해?
A. 일반 input에서는 required가 우선이다. custom widget에서는 aria-required를 고려할 수 있다.

Q. required를 쓰면 자동으로 접근성이 해결돼?
A. 필수 상태 전달에는 도움이 되지만 오류 메시지와 수정 방법도 함께 제공해야 한다.

Q. 필수 입력 안내는 어디에 둬?
A. Form 상단 안내와 각 label 옆 표시를 함께 사용할 수 있다.

---

## 3.2 Required Validation Message

### [개념]

Required Validation Message는 필수 입력값이 비어 있을 때 사용자에게 어떤 값을 입력해야 하는지 알려주는 오류 메시지다.

오류 메시지는 단순히 “필수입니다”가 아니라 사용자가 수정할 수 있는 구체적인 안내여야 한다.

---

### [핵심]

Required Error 기준:

- field error 제공
- input 근처 표시
- `aria-invalid`
- `aria-describedby`
- `role="alert"` 고려
- 수정 방법 포함
- 색상만으로 전달 금지

좋은 메시지:

- 이메일을 입력해 주세요.
- 비밀번호를 입력해 주세요.
- 닉네임을 입력해 주세요.
- 지역을 선택해 주세요.

나쁜 메시지:

- 오류
- 필수
- 잘못됨
- invalid

---

### [실무]

필수 오류 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  required
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>

{errors.email && (
  <p id="email-error" role="alert">
    이메일을 입력해 주세요.
  </p>
)}
```

Submit 실패 시 focus 이동 예:

```tsx
const firstErrorRef = useRef<HTMLInputElement>(null);

useEffect(() => {
  if (submitted && errors.email) {
    firstErrorRef.current?.focus();
  }
}, [submitted, errors.email]);
```

실무 기준:

- 오류 메시지는 input 바로 아래 또는 가까운 곳에 배치
- 오류 메시지와 input 연결
- 첫 오류 field로 focus 이동 고려
- global error와 field error를 구분
- “무엇을 해야 하는지”가 메시지에 포함되어야 함
- 오류 색상 외 텍스트 제공

---

### [FAQ]

Q. 필수값 오류 메시지는 어떻게 써?
A. “이메일을 입력해 주세요”처럼 사용자가 해야 할 행동을 명확히 알려준다.

Q. error message는 input과 어떻게 연결해?
A. error message에 id를 주고 input의 aria-describedby에 연결한다.

Q. aria-invalid는 언제 true야?
A. 해당 input의 현재 값이 validation 기준을 통과하지 못한 상태일 때 true로 설정한다.

Q. Submit 실패 시 focus를 이동해야 해?
A. Form이 길거나 오류를 찾기 어려운 경우 첫 오류 field로 focus 이동을 고려한다.

---

# 4. Helper Text Rules

## 4.1 Helper Text Connection

### [개념]

Helper Text는 사용자가 Form Control에 어떤 형식이나 조건으로 입력해야 하는지 알려주는 보조 설명이다.

Helper Text는 input과 연결되어야 스크린 리더 사용자가 입력 중 함께 인식할 수 있다.

---

### [핵심]

Helper Text 사용 대상:

- 비밀번호 조건
- 이메일 형식
- 휴대폰 번호 형식
- 파일 업로드 조건
- 날짜 입력 형식
- 검색어 조건
- 글자 수 제한
- 닉네임 규칙

연결 속성:

- `aria-describedby`
- helper text `id`
- multiple description ids
- error와 helper 동시 연결

---

### [실무]

Helper Text 예:

```jsx
<label htmlFor="password">비밀번호</label>
<input
  id="password"
  name="password"
  type="password"
  aria-describedby="password-help"
/>
<p id="password-help">
  영문, 숫자, 특수문자를 포함해 8자 이상 입력해 주세요.
</p>
```

Helper + Error 동시 연결:

```jsx
<label htmlFor="nickname">닉네임</label>
<input
  id="nickname"
  name="nickname"
  aria-describedby={
    error ? "nickname-help nickname-error" : "nickname-help"
  }
  aria-invalid={Boolean(error)}
/>
<p id="nickname-help">2자 이상 20자 이하로 입력해 주세요.</p>
{error && (
  <p id="nickname-error" role="alert">
    닉네임을 입력해 주세요.
  </p>
)}
```

실무 기준:

- 입력 조건은 placeholder보다 helper text에 제공
- helper text와 input은 `aria-describedby`로 연결
- error가 있을 때 helper와 error 둘 다 연결 가능
- 너무 긴 helper text는 사용성을 해칠 수 있음
- 글자 수 제한은 시각적 표시와 validation message 함께 제공

---

### [FAQ]

Q. Helper Text는 꼭 연결해야 해?
A. 입력 조건이나 중요한 설명이라면 aria-describedby로 input과 연결하는 것이 좋다.

Q. placeholder와 helper text 차이는?
A. placeholder는 짧은 예시이고 helper text는 입력 조건이나 안내를 지속적으로 제공한다.

Q. helper text와 error message를 둘 다 연결할 수 있어?
A. 가능하다. aria-describedby에 여러 id를 공백으로 연결할 수 있다.

Q. 비밀번호 조건은 어디에 써?
A. input 근처 helper text로 제공하고 aria-describedby로 연결하는 것이 좋다.

---

# 5. Error Message Accessibility

## 5.1 Field Error Message

### [개념]

Field Error Message는 특정 입력 필드에 발생한 오류를 설명하는 메시지다.

사용자는 오류가 어떤 필드에서 발생했는지, 왜 발생했는지, 어떻게 수정해야 하는지 알 수 있어야 한다.

---

### [핵심]

Field Error 구성:

- input `aria-invalid`
- input `aria-describedby`
- error message `id`
- error text
- `role="alert"` 고려
- field 주변 위치
- 시각적 표시
- 색상 외 단서

좋은 Field Error:

- 구체적인 필드명 포함
- 수정 행동 포함
- 짧고 명확함
- 내부 오류 노출 없음

---

### [실무]

Field Error 예:

```jsx
<label htmlFor="password">비밀번호</label>
<input
  id="password"
  name="password"
  type="password"
  aria-invalid={Boolean(errors.password)}
  aria-describedby={errors.password ? "password-error" : undefined}
/>

{errors.password && (
  <p id="password-error" role="alert">
    비밀번호를 입력해 주세요.
  </p>
)}
```

형식 오류 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : "email-help"}
/>
<p id="email-help">example@email.com 형식으로 입력해 주세요.</p>
{errors.email && (
  <p id="email-error" role="alert">
    올바른 이메일 형식으로 입력해 주세요.
  </p>
)}
```

실무 기준:

- 오류 메시지는 input과 가까운 곳에 표시
- 오류 id는 고유해야 함
- `aria-describedby`는 실제 렌더링된 id와 일치해야 함
- `aria-invalid`는 오류 상태와 동기화
- error text는 사용자가 할 일을 알려줘야 함
- 색상, 아이콘만으로 오류 표시 금지

---

### [FAQ]

Q. 에러 메시지는 input과 꼭 연결해야 해?
A. 권장한다. 스크린 리더 사용자가 어떤 입력값에 문제가 있는지 이해하기 쉽다.

Q. role="alert"는 모든 에러에 붙여도 돼?
A. 중요한 오류 알림에는 도움이 되지만 모든 작은 변화에 남발하면 사용자를 방해할 수 있다.

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. 오류 메시지는 어떻게 작성해야 해?
A. 어떤 필드를 어떻게 수정해야 하는지 짧고 명확하게 작성한다.

---

## 5.2 Global Error Message

### [개념]

Global Error Message는 Form 전체 제출 실패, 서버 오류, 인증 실패처럼 특정 field만으로 설명하기 어려운 오류를 사용자에게 전달하는 메시지다.

Global Error는 field error를 대체하지 않는다.

필드별 수정이 필요한 오류는 field error와 함께 제공해야 한다.

---

### [핵심]

Global Error 사용 대상:

- 로그인 실패
- 서버 요청 실패
- 제출 실패 요약
- 권한 부족
- 네트워크 오류
- 결제 실패
- 저장 실패

구성 요소:

- `role="alert"`
- 오류 제목
- 사용자용 오류 설명
- 재시도 버튼
- field error summary
- focus 이동 고려

---

### [실무]

로그인 실패 예:

```jsx
{
  loginError && (
    <div role="alert" tabIndex={-1} ref={errorRef}>
      이메일 또는 비밀번호가 올바르지 않습니다.
    </div>
  );
}
```

서버 오류 예:

```jsx
<section role="alert">
  <h2>저장에 실패했습니다.</h2>
  <p>잠시 후 다시 시도해 주세요.</p>
  <button type="button" onClick={onRetry}>
    다시 시도
  </button>
</section>
```

오류 요약 예:

```jsx
<div role="alert" tabIndex={-1} ref={summaryRef}>
  <h2>입력 내용을 확인해 주세요.</h2>
  <ul>
    <li>
      <a href="#email">이메일을 입력해 주세요.</a>
    </li>
    <li>
      <a href="#password">비밀번호를 입력해 주세요.</a>
    </li>
  </ul>
</div>
```

실무 기준:

- Global Error는 Form 상단 또는 사용자가 인식하기 쉬운 위치에 배치
- 내부 서버 메시지, stack trace, token 정보 노출 금지
- 재시도 가능한 오류에는 retry action 제공
- field 수정이 필요한 경우 field error도 함께 제공
- 긴 Form에서는 오류 요약과 첫 오류 focus 이동 고려

---

### [FAQ]

Q. Global Error만 있으면 field error는 없어도 돼?
A. 필드별 수정이 필요하다면 field error도 함께 제공하는 것이 좋다.

Q. 로그인 실패는 field error야 global error야?
A. 보안상 어떤 필드가 틀렸는지 구체화하지 않고 global error로 처리하는 경우가 많다.

Q. 서버 에러를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Global Error에는 focus를 이동해야 해?
A. 사용자가 오류를 놓치기 쉬운 경우 focus 이동을 고려할 수 있다.

---

## 5.3 Error Summary

### [개념]

Error Summary는 Form 제출 실패 시 발생한 여러 오류를 한 곳에 요약해서 제공하는 영역이다.

긴 Form이나 여러 오류가 동시에 발생하는 화면에서 사용자가 문제를 빠르게 찾도록 돕는다.

---

### [핵심]

Error Summary 구성:

- Form 상단 배치
- `role="alert"` 고려
- 제목 제공
- 오류 목록 제공
- 각 오류를 field로 연결
- field error와 함께 사용
- focus 이동 대상 고려

---

### [실무]

Error Summary 예:

```jsx
<div
  role="alert"
  tabIndex={-1}
  ref={errorSummaryRef}
  aria-labelledby="error-summary-title"
>
  <h2 id="error-summary-title">입력 내용을 확인해 주세요.</h2>
  <ul>
    <li>
      <a href="#email">이메일을 입력해 주세요.</a>
    </li>
    <li>
      <a href="#password">비밀번호를 입력해 주세요.</a>
    </li>
  </ul>
</div>
```

Submit 실패 후 focus:

```tsx
useEffect(() => {
  if (submitFailed) {
    errorSummaryRef.current?.focus();
  }
}, [submitFailed]);
```

실무 기준:

- 오류가 2개 이상이거나 Form이 길면 Error Summary 검토
- Error Summary link는 실제 field id와 연결
- Summary만 제공하고 field error를 생략하지 않음
- `tabIndex={-1}`은 programmatic focus 대상에 사용 가능
- 오류 문구는 field error와 일관되게 작성

---

### [FAQ]

Q. Error Summary는 언제 필요해?
A. Form이 길거나 여러 오류가 동시에 발생해 사용자가 오류 위치를 찾기 어려울 때 유용하다.

Q. Error Summary만 있으면 충분해?
A. 아니다. 각 field 근처에도 field error를 제공하는 것이 좋다.

Q. Error Summary에 focus를 줘도 돼?
A. 제출 실패 후 오류를 즉시 인식해야 하는 경우 programmatic focus를 줄 수 있다.

Q. Error Summary의 링크는 어디로 연결해?
A. 오류가 발생한 input 또는 관련 field group의 id로 연결한다.

---

# 6. Fieldset and Legend Rules

## 6.1 Field Group Accessibility

### [개념]

`fieldset`과 `legend`는 관련된 Form Control 그룹을 묶고 그룹의 질문이나 목적을 설명하는 요소다.

Radio Group, Checkbox Group, 주소 입력, 기간 선택처럼 여러 field가 하나의 의미 단위일 때 유용하다.

---

### [핵심]

사용 대상:

- radio group
- checkbox group
- address group
- date range group
- payment method group
- agreement group
- notification setting group
- search filter group

구성:

- `fieldset`
- `legend`
- group controls
- group helper text
- group error message

---

### [실무]

Checkbox Group 예:

```jsx
<fieldset>
  <legend>알림 수신 방법</legend>

  <label>
    <input type="checkbox" name="notification" value="email" />
    이메일
  </label>

  <label>
    <input type="checkbox" name="notification" value="sms" />
    문자
  </label>
</fieldset>
```

Radio Group 예:

```jsx
<fieldset>
  <legend>결제 수단</legend>

  <label>
    <input type="radio" name="paymentMethod" value="card" />
    카드
  </label>

  <label>
    <input type="radio" name="paymentMethod" value="bank" />
    계좌이체
  </label>
</fieldset>
```

기간 입력 예:

```jsx
<fieldset>
  <legend>축제 기간</legend>

  <label htmlFor="startDate">시작일</label>
  <input id="startDate" name="startDate" type="date" />

  <label htmlFor="endDate">종료일</label>
  <input id="endDate" name="endDate" type="date" />
</fieldset>
```

실무 기준:

- 여러 선택지가 하나의 질문에 속하면 `fieldset` 사용
- `legend`는 group의 질문을 설명
- radio는 같은 `name` 사용
- checkbox group은 각 checkbox label 제공
- group error message 연결 기준 검토
- 시각적 스타일 때문에 fieldset/legend를 제거하지 않음

---

### [FAQ]

Q. radio group에는 fieldset이 꼭 필요해?
A. 권장한다. 여러 선택지가 하나의 질문에 속한다는 구조를 명확히 전달할 수 있다.

Q. legend는 label이랑 달라?
A. label은 개별 input 설명이고 legend는 fieldset 그룹 전체 설명이다.

Q. checkbox group도 fieldset이 필요해?
A. 여러 checkbox가 하나의 질문에 속하면 fieldset과 legend를 사용하는 것이 좋다.

Q. fieldset은 디자인하기 불편한데 빼도 돼?
A. 스타일은 CSS로 조정하고 의미 구조는 유지하는 것이 좋다.

---

## 6.2 Group Error Message

### [개념]

Group Error Message는 radio group, checkbox group, date range group처럼 여러 Form Control이 하나의 validation 단위일 때 제공하는 오류 메시지다.

개별 input이 아니라 group 전체에 대한 오류를 설명해야 한다.

---

### [핵심]

Group Error 대상:

- radio 미선택
- checkbox 최소 1개 미선택
- 기간 시작일 / 종료일 불일치
- 주소 일부 누락
- 결제 수단 미선택
- 약관 필수 동의 누락

연결 기준:

- `fieldset`
- `legend`
- group error id
- `aria-describedby`
- `aria-invalid`는 custom group에서 고려
- error summary link target

---

### [실무]

Group Error 예:

```jsx
<fieldset aria-describedby={error ? "payment-error" : undefined}>
  <legend>결제 수단</legend>

  <label>
    <input type="radio" name="paymentMethod" value="card" />
    카드
  </label>

  <label>
    <input type="radio" name="paymentMethod" value="bank" />
    계좌이체
  </label>

  {error && (
    <p id="payment-error" role="alert">
      결제 수단을 선택해 주세요.
    </p>
  )}
</fieldset>
```

약관 동의 예:

```jsx
<fieldset aria-describedby={error ? "agreement-error" : undefined}>
  <legend>필수 약관 동의</legend>

  <label>
    <input type="checkbox" name="terms" />
    이용약관에 동의합니다.
  </label>

  {error && (
    <p id="agreement-error" role="alert">
      필수 약관에 동의해 주세요.
    </p>
  )}
</fieldset>
```

실무 기준:

- group 전체 오류는 fieldset 주변에 표시
- 오류 메시지는 group의 질문과 연결
- 첫 번째 radio나 checkbox에만 오류를 붙이는 방식은 문맥이 부족할 수 있음
- 오류 요약 링크는 fieldset 또는 첫 control로 이동 가능
- custom group은 role과 aria 상태를 별도로 검토

---

### [FAQ]

Q. radio group 오류는 어디에 표시해?
A. fieldset 내부 또는 group 가까운 위치에 group error message로 표시한다.

Q. group error는 개별 input error와 달라?
A. 그렇다. 여러 input이 하나의 validation 단위일 때 group 전체 오류로 처리한다.

Q. 약관 동의 오류는 어떻게 전달해?
A. fieldset과 legend로 약관 그룹을 설명하고 error message를 group과 연결한다.

Q. 날짜 범위 오류는 어느 input에 붙여?
A. 시작일과 종료일의 관계 오류라면 group error로 제공하는 것이 명확하다.

---

# 7. Select and Option Accessibility

## 7.1 Native Select Rules

### [개념]

`select`는 사용자가 정해진 옵션 중 하나 또는 여러 개를 선택하는 native Form Control이다.

Native Select는 기본 keyboard 조작과 보조기술 지원을 제공하므로 단순 선택 UI에서는 우선 고려할 수 있다.

---

### [핵심]

Select 기준:

- `label` 연결
- option text 명확화
- placeholder option 처리
- required 상태
- error message 연결
- helper text 연결
- keyboard 기본 지원

사용 대상:

- 지역 선택
- 카테고리 선택
- 정렬 조건 선택
- 페이지 크기 선택
- 결제 수단 선택
- 알림 시간 선택

---

### [실무]

기본 select:

```jsx
<label htmlFor="region">지역</label>
<select id="region" name="region">
  <option value="">지역을 선택하세요</option>
  <option value="seoul">서울</option>
  <option value="busan">부산</option>
</select>
```

Error 연결:

```jsx
<label htmlFor="category">축제 카테고리</label>
<select
  id="category"
  name="category"
  required
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "category-error" : undefined}
>
  <option value="">카테고리를 선택하세요</option>
  <option value="music">음악</option>
  <option value="food">음식</option>
</select>

{error && (
  <p id="category-error" role="alert">
    축제 카테고리를 선택해 주세요.
  </p>
)}
```

실무 기준:

- select에도 label 필수
- 첫 option은 안내 문구로 사용할 수 있음
- required select에서는 빈 value option 처리 주의
- option text는 의미 있게 작성
- select를 custom dropdown으로 바꾸면 keyboard / focus / role 구현 부담 증가
- 단순 선택은 native select 우선 검토

---

### [FAQ]

Q. select에도 label이 필요해?
A. 필요하다. 사용자가 어떤 값을 선택해야 하는지 알아야 한다.

Q. select의 첫 옵션은 어떻게 써?
A. “지역을 선택하세요”처럼 안내 문구를 제공하고 빈 value로 처리할 수 있다.

Q. custom select가 더 좋아?
A. 디자인 자유도는 높지만 keyboard, role, focus 관리가 필요해 구현 난도가 높다.

Q. select 오류는 어떻게 연결해?
A. error message id를 만들고 select의 aria-describedby에 연결하며 aria-invalid를 오류 상태와 동기화한다.

---

## 7.2 Custom Select Warning

### [개념]

Custom Select는 기본 `select` 대신 직접 만든 선택 UI다.

Custom Select는 디자인 자유도가 높지만 keyboard, focus, role, aria 상태를 직접 구현해야 하므로 접근성 난도가 높다.

---

### [핵심]

Custom Select 구현 필요 요소:

- trigger button
- popup list
- selected state
- keyboard navigation
- Arrow Key 이동
- Enter / Space 선택
- Escape 닫기
- focus management
- accessible name
- `aria-expanded`
- `aria-controls`
- role combobox / listbox 검토
- hidden item focus 방지

---

### [실무]

단순 Dropdown처럼 처리하는 예:

```jsx
<button
  type="button"
  aria-haspopup="listbox"
  aria-expanded={open}
  aria-controls="region-listbox"
  onClick={toggleOpen}
>
  {selectedRegion || "지역 선택"}
</button>;

{
  open && (
    <ul id="region-listbox" role="listbox">
      <li role="option" aria-selected={selectedRegion === "서울"}>
        서울
      </li>
      <li role="option" aria-selected={selectedRegion === "부산"}>
        부산
      </li>
    </ul>
  );
}
```

실무 기준:

- 단순 선택은 native select 우선
- custom select는 검증된 headless library 검토 가능
- role만 붙이고 keyboard를 구현하지 않으면 문제
- open 상태와 `aria-expanded` 동기화
- 선택 상태와 `aria-selected` 동기화
- 숨겨진 list item에 focus가 가지 않게 처리
- Testing Library `getByRole`로 검증 가능해야 함

---

### [FAQ]

Q. 디자인 때문에 select를 직접 만들면 안 돼?
A. 가능하지만 keyboard, role, aria, focus 관리가 필요해 구현 난도가 높다.

Q. Custom Select에서 가장 위험한 누락은?
A. keyboard 조작, focus 이동, aria-expanded, aria-selected 동기화 누락이다.

Q. Custom Select에 role만 붙이면 접근성 해결돼?
A. 아니다. role과 keyboard 동작, focus 흐름이 함께 구현되어야 한다.

Q. Custom Select는 언제 라이브러리를 써?
A. 복잡한 검색형 select, multi select, combobox는 접근성 검증된 라이브러리를 검토하는 것이 좋다.

---

# 8. Checkbox and Radio Accessibility

## 8.1 Checkbox Rules

### [개념]

Checkbox는 독립적인 선택 여부를 나타내거나 여러 옵션 중 복수 선택을 허용하는 Form Control이다.

Checkbox는 label과 연결되어야 하며, group 단위라면 fieldset과 legend를 고려해야 한다.

---

### [핵심]

Checkbox 기준:

- label 연결
- checked state
- group이면 fieldset / legend
- 필수 동의는 required 또는 validation
- error message 연결
- keyboard Space 조작
- custom checkbox 주의

사용 대상:

- 약관 동의
- 알림 수신 여부
- 필터 다중 선택
- 관심 카테고리 선택
- 설정 on/off

---

### [실무]

단일 checkbox:

```jsx
<label>
  <input type="checkbox" name="marketing" />
  마케팅 정보 수신에 동의합니다.
</label>
```

필수 약관:

```jsx
<label>
  <input
    type="checkbox"
    name="terms"
    required
    aria-invalid={Boolean(error)}
    aria-describedby={error ? "terms-error" : undefined}
  />
  이용약관에 동의합니다.
</label>;

{
  error && (
    <p id="terms-error" role="alert">
      이용약관에 동의해 주세요.
    </p>
  );
}
```

다중 선택 group:

```jsx
<fieldset>
  <legend>관심 축제 유형</legend>

  <label>
    <input type="checkbox" name="category" value="music" />
    음악
  </label>

  <label>
    <input type="checkbox" name="category" value="food" />
    음식
  </label>
</fieldset>
```

실무 기준:

- checkbox label은 선택 의미를 명확히 설명
- label 클릭으로 checkbox가 토글되어야 함
- group이면 fieldset / legend 사용
- 필수 동의 누락은 명확한 error message 제공
- custom checkbox는 checked state와 keyboard 조작 검증 필요

---

### [FAQ]

Q. checkbox에도 label이 필요해?
A. 필요하다. 체크박스가 어떤 선택을 의미하는지 사용자가 알 수 있어야 한다.

Q. 약관 동의 checkbox 오류는 어떻게 표시해?
A. checkbox 또는 약관 group과 error message를 aria-describedby로 연결한다.

Q. checkbox group에는 fieldset이 필요해?
A. 여러 checkbox가 하나의 질문에 속하면 fieldset과 legend를 사용하는 것이 좋다.

Q. custom checkbox는 뭘 조심해야 해?
A. checked 상태, keyboard Space 조작, focus visible, accessible name을 직접 검증해야 한다.

---

## 8.2 Radio Rules

### [개념]

Radio는 여러 옵션 중 하나만 선택하는 Form Control이다.

Radio Group은 하나의 질문과 여러 선택지로 구성되므로 fieldset과 legend를 사용하는 것이 좋다.

---

### [핵심]

Radio 기준:

- 같은 group은 같은 `name`
- 각 radio에 label 연결
- group에는 fieldset / legend 권장
- 하나만 선택 가능
- keyboard arrow navigation 기본 지원
- group error message 제공
- custom radio 주의

사용 대상:

- 성별 선택
- 결제 수단 선택
- 공개 범위 선택
- 정렬 방식 선택
- 알림 방식 선택
- 답변 선택

---

### [실무]

Radio Group 예:

```jsx
<fieldset>
  <legend>공개 범위</legend>

  <label>
    <input type="radio" name="visibility" value="public" />
    공개
  </label>

  <label>
    <input type="radio" name="visibility" value="private" />
    비공개
  </label>
</fieldset>
```

Radio Error 예:

```jsx
<fieldset aria-describedby={error ? "payment-error" : undefined}>
  <legend>결제 수단</legend>

  <label>
    <input type="radio" name="paymentMethod" value="card" />
    카드
  </label>

  <label>
    <input type="radio" name="paymentMethod" value="bank" />
    계좌이체
  </label>

  {error && (
    <p id="payment-error" role="alert">
      결제 수단을 선택해 주세요.
    </p>
  )}
</fieldset>
```

실무 기준:

- radio group의 `name`은 동일해야 함
- 각 radio는 label과 연결
- group 질문은 legend로 제공
- 오류는 group 단위로 표시
- keyboard 방향키 이동 확인
- custom radio는 checked 상태, role, keyboard 검증 필요

---

### [FAQ]

Q. radio group에는 fieldset이 꼭 필요해?
A. 권장한다. 여러 선택지가 하나의 질문에 속한다는 구조를 명확히 전달할 수 있다.

Q. radio는 같은 name을 써야 해?
A. 같은 group에서 하나만 선택되도록 같은 name을 사용해야 한다.

Q. radio group 오류는 어디에 표시해?
A. fieldset 내부 또는 group 가까운 위치에 group error message로 표시한다.

Q. radio와 checkbox 차이는?
A. radio는 여러 옵션 중 하나 선택이고 checkbox는 독립 선택 또는 복수 선택이다.

---

# 9. File Input Accessibility

## 9.1 File Upload Field

### [개념]

File Input Accessibility는 사용자가 파일 업로드 조건, 선택된 파일, 오류 상태를 이해할 수 있게 하는 기준이다.

File input은 label과 연결되어야 하며 파일 형식, 크기 제한, 개수 제한 같은 조건은 helper text로 제공하는 것이 좋다.

---

### [핵심]

File Input 기준:

- label 연결
- accepted file type 안내
- file size 안내
- multiple 여부 안내
- helper text 연결
- error message 연결
- selected file name 표시
- custom upload button 주의

---

### [실무]

기본 file input:

```jsx
<label htmlFor="profileImage">프로필 이미지</label>
<input
  id="profileImage"
  name="profileImage"
  type="file"
  accept="image/png,image/jpeg"
  aria-describedby="profileImage-help"
/>
<p id="profileImage-help">
  PNG 또는 JPG 파일만 업로드할 수 있습니다. 최대 5MB까지 가능합니다.
</p>
```

Error 연결:

```jsx
<label htmlFor="reviewImages">리뷰 이미지</label>
<input
  id="reviewImages"
  name="reviewImages"
  type="file"
  multiple
  accept="image/png,image/jpeg"
  aria-invalid={Boolean(error)}
  aria-describedby={error ? "reviewImages-help reviewImages-error" : "reviewImages-help"}
/>
<p id="reviewImages-help">이미지는 최대 3장까지 업로드할 수 있습니다.</p>
{error && (
  <p id="reviewImages-error" role="alert">
    업로드 가능한 이미지 형식을 확인해 주세요.
  </p>
)}
```

실무 기준:

- file input에도 label 필수
- 파일 조건은 helper text로 명확히 제공
- 선택된 파일명을 화면에 표시
- 오류는 파일 형식, 크기, 개수 기준으로 구체화
- custom upload button은 native input과 label 연결 유지
- drag and drop upload는 keyboard 대체 수단 제공

---

### [FAQ]

Q. file input에도 label이 필요해?
A. 필요하다. 어떤 파일을 업로드해야 하는지 사용자가 알아야 한다.

Q. 파일 크기 제한은 어디에 써?
A. input 근처 helper text로 제공하고 aria-describedby로 연결하는 것이 좋다.

Q. drag and drop만 제공해도 돼?
A. 권장하지 않는다. keyboard 사용자를 위해 파일 선택 버튼 같은 대체 수단이 필요하다.

Q. 파일 업로드 오류는 어떻게 작성해?
A. 파일 형식, 크기, 개수 중 무엇이 문제인지 명확히 알려준다.

---

# 10. Search Form Accessibility

## 10.1 Search Input Rules

### [개념]

Search Form Accessibility는 사용자가 검색어 입력, 필터 선택, 검색 실행, 검색 결과 없음 상태를 명확히 이해할 수 있게 하는 기준이다.

Search input은 label 또는 accessible name이 필요하며, 검색 버튼은 명확한 이름을 가져야 한다.

---

### [핵심]

Search Form 구성:

- `form`
- `role="search"` 또는 search landmark 고려
- search input label
- search button
- filter select / checkbox
- clear button
- result count
- empty state
- loading state

---

### [실무]

검색 Form 예:

```jsx
<form role="search" onSubmit={onSearch}>
  <label htmlFor="festival-search">축제 검색어</label>
  <input id="festival-search" name="keyword" type="search" />

  <button type="submit">검색</button>
</form>
```

Icon 검색 버튼:

```jsx
<button type="submit" aria-label="축제 검색">
  <SearchIcon aria-hidden="true" />
</button>
```

검색 결과 개수:

```jsx
<p role="status" aria-live="polite">
  검색 결과 {resultCount}건
</p>
```

결과 없음:

```jsx
<section>
  <h2>검색 결과가 없습니다.</h2>
  <p>검색어를 바꾸거나 필터를 초기화해 보세요.</p>
  <button type="button" onClick={onReset}>
    필터 초기화
  </button>
</section>
```

실무 기준:

- 검색 input은 label 필요
- 검색 버튼은 text 또는 aria-label 필요
- icon button 내부 icon은 `aria-hidden`
- 검색 중 Loading 상태 제공
- 검색 결과 개수는 status로 전달 가능
- 검색 결과 없음은 Empty State로 제공
- 필터 초기화는 button 사용

---

### [FAQ]

Q. 검색 input에도 label이 필요해?
A. 필요하다. 사용자가 무엇을 검색하는지 알 수 있어야 한다.

Q. 검색 아이콘 버튼에는 aria-label이 필요해?
A. 버튼에 visible text가 없다면 aria-label로 목적을 제공해야 한다.

Q. 검색 결과 개수는 스크린 리더에 알려야 해?
A. 동적으로 바뀌는 중요한 상태라면 role status 또는 aria-live를 고려할 수 있다.

Q. 검색 결과가 없으면 어떻게 보여줘?
A. Empty State로 결과 없음 메시지와 다음 행동을 제공한다.

---

# 11. Login and Signup Form Patterns

## 11.1 Login Form Accessibility

### [개념]

Login Form Accessibility는 사용자가 이메일, 비밀번호 입력, 로그인 실패 메시지, 비밀번호 찾기 링크를 명확히 이해하고 사용할 수 있게 하는 기준이다.

로그인 실패 메시지는 보안상 어떤 필드가 틀렸는지 과도하게 구체화하지 않는 경우가 많다.

---

### [핵심]

Login Form 구성:

- email label
- password label
- submit button
- global login error
- password visibility toggle
- forgot password link
- signup link
- loading submit state
- keyboard submit

---

### [실무]

Login Form 예:

```jsx
<form onSubmit={onSubmit}>
  <label htmlFor="email">이메일</label>
  <input
    id="email"
    name="email"
    type="email"
    autoComplete="email"
    aria-invalid={Boolean(errors.email)}
    aria-describedby={errors.email ? "email-error" : undefined}
  />
  {errors.email && (
    <p id="email-error" role="alert">
      이메일을 입력해 주세요.
    </p>
  )}

  <label htmlFor="password">비밀번호</label>
  <input
    id="password"
    name="password"
    type="password"
    autoComplete="current-password"
    aria-invalid={Boolean(errors.password)}
    aria-describedby={errors.password ? "password-error" : undefined}
  />
  {errors.password && (
    <p id="password-error" role="alert">
      비밀번호를 입력해 주세요.
    </p>
  )}

  {loginError && (
    <div role="alert">이메일 또는 비밀번호가 올바르지 않습니다.</div>
  )}

  <button type="submit" disabled={loading} aria-busy={loading}>
    {loading ? "로그인 중..." : "로그인"}
  </button>

  <Link to="/find-password">비밀번호 찾기</Link>
</form>
```

실무 기준:

- email / password label 제공
- `autoComplete` 적절히 사용
- 로그인 실패는 global error로 제공 가능
- 로그인 중 버튼 상태 text 변경
- 비밀번호 찾기는 Link
- 회원가입 이동은 Link
- 비밀번호 보기 토글은 button + aria-label / aria-pressed 고려

---

### [FAQ]

Q. 로그인 실패는 field error야 global error야?
A. 보안상 어떤 필드가 틀렸는지 구체화하지 않고 global error로 처리하는 경우가 많다.

Q. 로그인 버튼 loading 상태는 어떻게 표시해?
A. button text를 “로그인 중...”으로 바꾸고 필요하면 aria-busy를 사용할 수 있다.

Q. 비밀번호 찾기는 Button이야 Link야?
A. 비밀번호 찾기 페이지로 이동한다면 Link가 적합하다.

Q. autoComplete는 접근성과 관련 있어?
A. 사용자가 입력을 더 쉽게 완료하도록 도와주므로 적절히 사용하는 것이 좋다.

---

## 11.2 Signup Form Accessibility

### [개념]

Signup Form Accessibility는 사용자가 여러 입력 조건과 오류를 이해하고 회원가입을 완료할 수 있게 하는 기준이다.

회원가입 Form은 필수값, 형식 조건, 중복 확인, 약관 동의 등 접근성 검토 지점이 많다.

---

### [핵심]

Signup Form 구성:

- email field
- password field
- password confirm field
- nickname field
- phone field optional
- region select optional
- required indication
- helper text
- field error
- global error
- terms checkbox
- submit loading state

---

### [실무]

비밀번호 조건 예:

```jsx
<label htmlFor="password">비밀번호</label>
<input
  id="password"
  name="password"
  type="password"
  autoComplete="new-password"
  aria-describedby={
    errors.password ? "password-help password-error" : "password-help"
  }
  aria-invalid={Boolean(errors.password)}
/>
<p id="password-help">
  영문, 숫자, 특수문자를 포함해 8자 이상 입력해 주세요.
</p>
{errors.password && (
  <p id="password-error" role="alert">
    비밀번호 조건을 확인해 주세요.
  </p>
)}
```

약관 동의 예:

```jsx
<fieldset aria-describedby={errors.terms ? "terms-error" : undefined}>
  <legend>약관 동의</legend>

  <label>
    <input type="checkbox" name="terms" required />
    이용약관에 동의합니다. <span>(필수)</span>
  </label>

  {errors.terms && (
    <p id="terms-error" role="alert">
      필수 약관에 동의해 주세요.
    </p>
  )}
</fieldset>
```

실무 기준:

- 필수 입력 표시 제공
- password 조건은 helper text로 제공
- password confirm 오류는 구체적으로 작성
- 중복 확인 결과는 status / alert 기준 검토
- 약관 동의 group은 fieldset / legend 고려
- submit 실패 시 Error Summary 고려
- 내부 validation과 서버 validation 메시지 일관성 유지

---

### [FAQ]

Q. 회원가입 Form에서 가장 중요한 접근성 기준은?
A. label 연결, 필수값 표시, helper text 연결, error message 연결, 약관 checkbox 접근성이다.

Q. 비밀번호 조건은 어디에 써?
A. password input 근처 helper text로 제공하고 aria-describedby로 연결한다.

Q. 비밀번호 확인 오류는 어떻게 써?
A. “비밀번호가 일치하지 않습니다”처럼 사용자가 수정할 수 있게 명확히 작성한다.

Q. 약관 동의는 checkbox 하나면 충분해?
A. label 연결과 필수 여부, 오류 메시지 연결까지 함께 제공해야 한다.

---

# 12. Form Focus Management

## 12.1 Focus on Validation Failure

### [개념]

Form Focus Management는 Form 제출 실패, 오류 발생, 동적 field 추가 / 제거 시 keyboard focus가 논리적으로 유지되도록 관리하는 기준이다.

사용자가 submit 후 오류를 찾기 어렵다면 focus를 Error Summary 또는 첫 오류 field로 이동할 수 있다.

---

### [핵심]

Focus 이동 대상:

- Error Summary
- first invalid field
- global error
- newly added field
- submit button
- success message

주의 상황:

- 긴 Form
- 여러 오류
- Modal Form
- Step Form
- Conditional Field
- disabled focused element
- unmounted focused element

---

### [실무]

첫 오류 field focus:

```tsx
const emailRef = useRef<HTMLInputElement>(null);

useEffect(() => {
  if (submitFailed && errors.email) {
    emailRef.current?.focus();
  }
}, [submitFailed, errors.email]);
```

Error Summary focus:

```tsx
const errorSummaryRef = useRef<HTMLDivElement>(null);

useEffect(() => {
  if (submitFailed) {
    errorSummaryRef.current?.focus();
  }
}, [submitFailed]);
```

대상 요소:

```jsx
<div role="alert" tabIndex={-1} ref={errorSummaryRef}>
  입력 내용을 확인해 주세요.
</div>
```

실무 기준:

- 짧은 Form은 field error만으로 충분할 수 있음
- 긴 Form은 Error Summary focus 고려
- focus 이동은 사용자를 돕기 위한 경우에만 사용
- focus를 불필요하게 빼앗지 않음
- 오류 field가 unmount되지 않게 conditional rendering 주의
- Modal Form은 Modal 내부 focus 흐름과 함께 검토

---

### [FAQ]

Q. Submit 실패 시 focus를 이동해야 해?
A. Form이 길거나 오류를 찾기 어려운 경우 Error Summary 또는 첫 오류 field로 이동을 고려한다.

Q. Error Summary와 첫 오류 field 중 어디로 focus를 줘?
A. 오류가 여러 개면 Error Summary, 단일 오류나 짧은 Form이면 첫 오류 field가 적합할 수 있다.

Q. focus 이동은 항상 좋은 거야?
A. 아니다. 불필요한 focus 이동은 사용자를 혼란스럽게 할 수 있다.

Q. tabIndex="-1"은 왜 써?
A. Tab 순서에는 포함하지 않지만 코드로 focus를 이동해야 하는 요소에 사용할 수 있다.

---

## 12.2 Dynamic Field Focus

### [개념]

Dynamic Field Focus는 조건부 렌더링으로 Form Field가 나타나거나 사라질 때 focus가 사라지거나 예상하지 못한 위치로 이동하지 않게 관리하는 기준이다.

React Form에서는 선택값에 따라 field가 추가되거나 제거되는 경우가 많다.

---

### [핵심]

주의 상황:

- conditional field show / hide
- dynamic list field
- add item button
- remove item button
- dependent select
- address search result
- file upload preview
- step form transition

Focus 기준:

- 새 field가 나타났을 때 focus 필요 여부 판단
- 삭제된 field에 focus가 남지 않게 처리
- 삭제 후 다음 합리적 위치로 focus 이동
- hidden field에 focus 가지 않게 처리
- validation 대상과 hidden 상태 동기화

---

### [실무]

항목 추가 후 focus:

```tsx
const newItemRef = useRef<HTMLInputElement>(null);

useEffect(() => {
  if (itemAdded) {
    newItemRef.current?.focus();
  }
}, [itemAdded]);
```

삭제 후 focus 후보:

```text
삭제된 field
→ 다음 field
→ 이전 field
→ 항목 추가 버튼
→ Section heading
```

조건부 field 예:

```jsx
{
  useCustomRegion && (
    <div>
      <label htmlFor="custom-region">직접 입력 지역</label>
      <input id="custom-region" name="customRegion" />
    </div>
  );
}
```

실무 기준:

- 조건부 field는 label과 validation을 함께 관리
- 숨겨진 field는 validation에서 제외할지 명확히 결정
- field 제거 후 focus lost 여부 확인
- 동적 field 추가 후 자동 focus는 상황에 맞게 제한적으로 사용
- Screen Reader 사용자에게 상태 변화가 필요한 경우 status message 고려

---

### [FAQ]

Q. 조건부 input이 생기면 자동 focus를 줘야 해?
A. 상황에 따라 다르다. 사용자가 바로 입력해야 하는 흐름이면 focus를 고려할 수 있다.

Q. input을 삭제했더니 focus가 사라져?
A. 삭제 후 다음 field, 이전 field, 추가 버튼 등 합리적인 위치로 focus를 이동해야 할 수 있다.

Q. 숨겨진 field도 validation 해야 해?
A. 일반적으로 사용자가 볼 수 없고 입력할 수 없는 field는 validation 대상에서 제외하는 것이 자연스럽다.

Q. 동적 Form에서 가장 흔한 문제는?
A. label 누락, validation 상태 불일치, focus lost, hidden field focus 문제가 자주 발생한다.

---

# 13. Form Testing Rules

## 13.1 Testing Library Form Query

### [개념]

Testing Library Form Query는 사용자가 실제로 인식하는 label, role, text를 기준으로 Form 요소를 찾는 테스트 방식이다.

접근성 있는 Form은 `getByLabelText`, `getByRole`, `getByText`로 자연스럽게 테스트할 수 있다.

---

### [핵심]

우선 Query:

- `getByLabelText`
- `getByRole`
- `getByText`
- `getByDisplayValue`
- `getByPlaceholderText`
- `getByTestId` last resort

Form 검증 대상:

- label 연결
- submit button name
- error alert
- helper text
- required field
- checkbox label
- radio group
- select label
- file input label

---

### [실무]

Input Query:

```tsx
screen.getByLabelText("이메일");
screen.getByLabelText("비밀번호");
```

Button Query:

```tsx
screen.getByRole("button", { name: "로그인" });
screen.getByRole("button", { name: "검색" });
```

Error Query:

```tsx
screen.getByRole("alert");
screen.getByText("이메일을 입력해 주세요.");
```

Select Query:

```tsx
screen.getByLabelText("지역");
screen.getByRole("combobox", { name: "지역" });
```

Checkbox Query:

```tsx
screen.getByRole("checkbox", {
  name: "이용약관에 동의합니다.",
});
```

실무 기준:

- `getByLabelText`가 실패하면 label 연결 확인
- `getByRole("button", { name })` 실패 시 accessible name 확인
- `getByRole("alert")`로 오류 메시지 확인 가능
- `getByTestId`는 접근성 문제를 숨길 수 있으므로 최후 수단
- Form 테스트는 사용자가 인식하는 이름 중심으로 작성

---

### [FAQ]

Q. Form input은 어떤 query로 찾는 게 좋아?
A. label이 연결되어 있다면 getByLabelText가 가장 자연스럽다.

Q. getByLabelText가 실패하면 접근성 문제야?
A. 가능성이 높다. label과 input 연결, label text, id 중복 여부를 확인한다.

Q. submit button은 어떻게 테스트해?
A. getByRole("button", { name: "로그인" })처럼 accessible name으로 찾는다.

Q. testId로 찾으면 안 돼?
A. 필요한 경우 사용할 수 있지만 접근성 구조 검증을 놓칠 수 있으므로 최후 수단으로 둔다.

---

## 13.2 Form Accessibility Test Cases

### [개념]

Form Accessibility Test Case는 Form이 label, error, keyboard, required, helper text 기준을 만족하는지 검증하는 테스트 항목이다.

Agent는 Form 구현 후 접근성 테스트 케이스를 기준으로 누락을 찾을 수 있어야 한다.

---

### [핵심]

테스트 항목:

- label로 input을 찾을 수 있는가?
- submit button을 role/name으로 찾을 수 있는가?
- required field 오류가 표시되는가?
- error message가 role alert로 노출되는가?
- helper text가 화면에 존재하는가?
- checkbox / radio를 label로 조작할 수 있는가?
- select를 label로 찾을 수 있는가?
- loading 상태가 button text로 표현되는가?
- field error가 구체적인가?
- testId 없이 주요 요소를 찾을 수 있는가?

---

### [실무]

테스트 예:

```tsx
test("로그인 Form은 label로 입력 필드를 찾을 수 있다", () => {
  render(<LoginForm />);

  expect(screen.getByLabelText("이메일")).toBeInTheDocument();
  expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "로그인" })).toBeInTheDocument();
});
```

오류 테스트 예:

```tsx
test("이메일 미입력 시 오류 메시지를 보여준다", async () => {
  render(<LoginForm />);

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByRole("alert")).toHaveTextContent(
    "이메일을 입력해 주세요.",
  );
});
```

Checkbox 테스트 예:

```tsx
test("약관 동의 checkbox를 label로 조작할 수 있다", async () => {
  render(<SignupForm />);

  const checkbox = screen.getByRole("checkbox", {
    name: /이용약관에 동의합니다/,
  });

  await user.click(checkbox);

  expect(checkbox).toBeChecked();
});
```

실무 기준:

- 테스트는 사용자 행동 기준으로 작성
- label과 role 기반 Query 우선
- 오류 메시지 문구는 사용자용 문구 검증
- loading 중 버튼 disabled와 text 변경 확인
- checkbox / radio는 keyboard 조작도 고려
- Form 접근성 테스트는 UI 구조 개선에 직접 연결됨

---

### [FAQ]

Q. Form 접근성 테스트에서 가장 먼저 볼 것은?
A. input을 label로 찾을 수 있는지와 submit button을 role/name으로 찾을 수 있는지 확인한다.

Q. 오류 메시지는 어떻게 테스트해?
A. role alert 또는 오류 텍스트로 확인할 수 있다.

Q. checkbox는 어떻게 테스트해?
A. getByRole("checkbox", { name })으로 찾고 click 또는 keyboard로 checked 상태를 확인한다.

Q. 접근성 테스트가 코드 품질에도 도움이 돼?
A. 그렇다. 사용자가 인식하는 구조로 테스트하기 때문에 UI 의미와 접근성이 함께 개선된다.

---

# 14. Form Accessibility Review

## 14.1 Review Checklist

### [개념]

Form Accessibility Review는 Form이 label, required, helper text, error message, focus, keyboard, testing 기준을 만족하는지 검토하는 과정이다.

Review Agent는 Form 구현에서 가장 먼저 label 누락과 error message 미연결을 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 모든 주요 input에 label이 연결되었는가?
- [ ] label htmlFor와 input id가 일치하는가?
- [ ] input id가 중복되지 않는가?
- [ ] placeholder를 label 대체로 사용하지 않았는가?
- [ ] required field가 명확히 표시되었는가?
- [ ] 별표 사용 시 의미 설명이 있는가?
- [ ] helper text가 input과 aria-describedby로 연결되었는가?
- [ ] error message가 input과 aria-describedby로 연결되었는가?
- [ ] aria-invalid가 실제 오류 상태와 일치하는가?
- [ ] field error가 구체적인 수정 방법을 제공하는가?
- [ ] global error와 field error를 구분했는가?
- [ ] 긴 Form에서 Error Summary를 고려했는가?
- [ ] radio / checkbox group에 fieldset과 legend를 고려했는가?
- [ ] select에 label이 연결되었는가?
- [ ] file input에 label과 업로드 조건이 제공되었는가?
- [ ] submit 실패 시 focus 이동 기준이 있는가?
- [ ] keyboard만으로 입력, 선택, 제출 가능한가?
- [ ] loading 중 submit button 상태가 전달되는가?
- [ ] getByLabelText로 주요 input을 찾을 수 있는가?
- [ ] getByRole로 submit button과 alert를 찾을 수 있는가?
```

---

### [실무]

Review Flow:

```text
Form Component 확인
→ Label 연결 확인
→ Required 표시 확인
→ Helper Text 연결 확인
→ Error Message 연결 확인
→ Group Field 확인
→ Submit Failure Focus 확인
→ Keyboard 조작 확인
→ Testing Library Query 확인
→ Common Mistake 확인
```

대표 수정 패턴:

```text
문제: placeholder만 있는 input
해결: label htmlFor + input id 연결
```

```text
문제: error message가 input과 미연결
해결: error id + aria-describedby + aria-invalid 적용
```

```text
문제: radio group 질문 누락
해결: fieldset + legend 적용
```

```text
문제: getByLabelText 실패
해결: label text, htmlFor, input id, id 중복 확인
```

---

### [FAQ]

Q. Form Review에서 가장 먼저 볼 것은?
A. label 연결, placeholder-only 여부, error message 연결, aria-invalid 상태를 먼저 확인한다.

Q. Form에서 가장 흔한 접근성 문제는?
A. label 누락, placeholder label 대체, error message 미연결, checkbox/radio group 구조 누락이다.

Q. Form 테스트 실패가 접근성 문제일 수 있어?
A. 그렇다. getByLabelText나 getByRole 실패는 label, role, accessible name 문제일 수 있다.

Q. Review Agent는 Form 오류 문구도 봐야 해?
A. 봐야 한다. 오류 문구는 사용자가 무엇을 수정해야 하는지 명확히 알려야 한다.

---

# 15. Common Form Accessibility Mistakes

## 15.1 Form Anti Patterns

### [개념]

Form Anti Pattern은 화면상 입력은 가능하지만 label, error, keyboard, focus, testing 관점에서 문제가 발생하는 구현 방식이다.

Form 접근성 문제는 사용자 이탈, 테스트 실패, validation UX 문제로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- label 없는 input
- placeholder를 label로 대체
- label htmlFor와 input id 불일치
- input id 중복
- icon search input에 accessible name 없음
- required 표시가 별표만 있음
- 별표 의미 설명 없음
- helper text 미연결
- error message 미연결
- aria-invalid 상태 불일치
- 빨간색 테두리만 오류 표시
- role alert 남발
- global error만 제공하고 field error 없음
- radio group에 fieldset / legend 없음
- checkbox label 누락
- select label 누락
- file input 조건 안내 없음
- submit 실패 후 focus lost
- hidden field validation 오류
- getByTestId 중심 Form 테스트

---

### [실무]

Anti Pattern:

```jsx
<input placeholder="이메일" />
```

개선:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

Anti Pattern:

```jsx
<input id="password" type="password" />
<p>비밀번호를 입력해 주세요.</p>
```

개선:

```jsx
<input
  id="password"
  type="password"
  aria-invalid="true"
  aria-describedby="password-error"
/>
<p id="password-error" role="alert">
  비밀번호를 입력해 주세요.
</p>
```

Anti Pattern:

```jsx
<div>
  <p>결제 수단</p>
  <input type="radio" name="payment" /> 카드
  <input type="radio" name="payment" /> 계좌이체
</div>
```

개선:

```jsx
<fieldset>
  <legend>결제 수단</legend>
  <label>
    <input type="radio" name="payment" value="card" />
    카드
  </label>
  <label>
    <input type="radio" name="payment" value="bank" />
    계좌이체
  </label>
</fieldset>
```

---

### [FAQ]

Q. Form 접근성 초보가 가장 많이 하는 실수는?
A. label 누락, placeholder label 대체, error message 미연결, fieldset/legend 누락이 많다.

Q. 빨간색 테두리만 오류 표시하면 왜 문제야?
A. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. hidden field validation 오류는 왜 문제야?
A. 사용자가 볼 수 없고 수정할 수 없는 field에 오류가 발생하면 Form을 완료하기 어렵다.

Q. getByTestId로 Form 테스트하면 왜 아쉬워?
A. 사용자가 인식하는 label, role, error 구조를 검증하지 못할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Form Accessibility는 왜 중요해?
A. 사용자가 입력 필드의 목적, 필수 여부, 오류 원인, 수정 방법을 이해하고 Form을 완료해야 하기 때문이다.

Q. Form 접근성에서 가장 먼저 볼 것은?
A. label 연결, required 표시, helper text 연결, error message 연결, keyboard 조작을 먼저 확인한다.

Q. input과 label은 어떻게 연결해?
A. label의 htmlFor와 input의 id를 같은 값으로 연결한다.

Q. 모든 input에 label이 필요해?
A. 주요 Form Control에는 label이 필요하다. 사용자가 어떤 값을 입력해야 하는지 알아야 한다.

Q. label 없이 aria-label만 써도 돼?
A. 가능하지만 보이는 label이 더 명확하다. 디자인상 어렵다면 aria-label을 보완적으로 사용할 수 있다.

Q. checkbox도 label이 필요해?
A. 필요하다. 체크박스가 어떤 선택을 의미하는지 사용자가 알 수 있어야 한다.

Q. radio도 label이 필요해?
A. 필요하다. 각 radio option의 의미를 사용자가 알 수 있어야 한다.

Q. select에도 label이 필요해?
A. 필요하다. 사용자가 어떤 값을 선택해야 하는지 알아야 한다.

Q. file input에도 label이 필요해?
A. 필요하다. 어떤 파일을 업로드해야 하는지 사용자가 알아야 한다.

Q. placeholder가 있으면 label은 없어도 돼?
A. 권장하지 않는다. placeholder는 입력 중 사라지고 label을 안정적으로 대체하지 못한다.

Q. placeholder는 언제 써?
A. 입력 예시나 형식 힌트를 보조적으로 제공할 때 사용한다.

Q. placeholder에 중요한 안내를 넣어도 돼?
A. 권장하지 않는다. 중요한 안내는 label이나 helper text로 제공한다.

Q. getByPlaceholderText를 쓰면 되지 않아?
A. 테스트는 가능하지만 접근성 좋은 Form은 getByLabelText로 찾을 수 있어야 한다.

Q. Form Control의 Accessible Name이 뭐야?
A. 스크린 리더와 Testing Library가 input의 이름으로 인식하는 텍스트다.

Q. aria-label과 label은 뭐가 달라?
A. label은 시각적으로도 보이는 설명이고 aria-label은 보조기술에 이름을 제공하는 속성이다.

Q. aria-labelledby는 언제 써?
A. 화면에 이미 있는 텍스트를 Form Control의 이름으로 연결할 때 사용한다.

Q. 같은 label이 반복되면 문제야?
A. 문맥이 부족할 수 있다. 그룹 제목이나 구체적인 label로 구분하는 것이 좋다.

Q. 필수값 표시로 별표만 붙이면 돼?
A. 별표의 의미를 설명하거나 “필수” 텍스트를 함께 제공하는 것이 좋다.

Q. required와 aria-required를 둘 다 써야 해?
A. 일반 input에서는 required가 우선이다. custom widget에서는 aria-required를 고려할 수 있다.

Q. required를 쓰면 자동으로 접근성이 해결돼?
A. 필수 상태 전달에는 도움이 되지만 오류 메시지와 수정 방법도 함께 제공해야 한다.

Q. 필수 입력 안내는 어디에 둬?
A. Form 상단 안내와 각 label 옆 표시를 함께 사용할 수 있다.

Q. 필수값 오류 메시지는 어떻게 써?
A. “이메일을 입력해 주세요”처럼 사용자가 해야 할 행동을 명확히 알려준다.

Q. error message는 input과 어떻게 연결해?
A. error message에 id를 주고 input의 aria-describedby에 연결한다.

Q. aria-invalid는 언제 true야?
A. 해당 input의 현재 값이 validation 기준을 통과하지 못한 상태일 때 true로 설정한다.

Q. Submit 실패 시 focus를 이동해야 해?
A. Form이 길거나 오류를 찾기 어려운 경우 첫 오류 field나 Error Summary로 focus 이동을 고려한다.

Q. Helper Text는 꼭 연결해야 해?
A. 입력 조건이나 중요한 설명이라면 aria-describedby로 input과 연결하는 것이 좋다.

Q. placeholder와 helper text 차이는?
A. placeholder는 짧은 예시이고 helper text는 입력 조건이나 안내를 지속적으로 제공한다.

Q. helper text와 error message를 둘 다 연결할 수 있어?
A. 가능하다. aria-describedby에 여러 id를 공백으로 연결할 수 있다.

Q. 비밀번호 조건은 어디에 써?
A. password input 근처 helper text로 제공하고 aria-describedby로 연결하는 것이 좋다.

Q. 에러 메시지는 input과 꼭 연결해야 해?
A. 권장한다. 스크린 리더 사용자가 어떤 입력값에 문제가 있는지 이해하기 쉽다.

Q. role="alert"는 모든 에러에 붙여도 돼?
A. 중요한 오류 알림에는 도움이 되지만 모든 작은 변화에 남발하면 사용자를 방해할 수 있다.

Q. 빨간색 테두리만 표시하면 충분해?
A. 아니다. 색상만으로 오류를 전달하면 일부 사용자가 오류를 인식하기 어렵다.

Q. 오류 메시지는 어떻게 작성해야 해?
A. 어떤 필드를 어떻게 수정해야 하는지 짧고 명확하게 작성한다.

Q. Global Error만 있으면 field error는 없어도 돼?
A. 필드별 수정이 필요하다면 field error도 함께 제공하는 것이 좋다.

Q. 로그인 실패는 field error야 global error야?
A. 보안상 어떤 필드가 틀렸는지 구체화하지 않고 global error로 처리하는 경우가 많다.

Q. 서버 에러를 그대로 보여줘도 돼?
A. 권장하지 않는다. 내부 정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. Global Error에는 focus를 이동해야 해?
A. 사용자가 오류를 놓치기 쉬운 경우 focus 이동을 고려할 수 있다.

Q. Error Summary는 언제 필요해?
A. Form이 길거나 여러 오류가 동시에 발생해 사용자가 오류 위치를 찾기 어려울 때 유용하다.

Q. Error Summary만 있으면 충분해?
A. 아니다. 각 field 근처에도 field error를 제공하는 것이 좋다.

Q. Error Summary에 focus를 줘도 돼?
A. 제출 실패 후 오류를 즉시 인식해야 하는 경우 programmatic focus를 줄 수 있다.

Q. Error Summary의 링크는 어디로 연결해?
A. 오류가 발생한 input 또는 관련 field group의 id로 연결한다.

Q. radio group에는 fieldset이 꼭 필요해?
A. 권장한다. 여러 선택지가 하나의 질문에 속한다는 구조를 명확히 전달할 수 있다.

Q. legend는 label이랑 달라?
A. label은 개별 input 설명이고 legend는 fieldset 그룹 전체 설명이다.

Q. checkbox group도 fieldset이 필요해?
A. 여러 checkbox가 하나의 질문에 속하면 fieldset과 legend를 사용하는 것이 좋다.

Q. fieldset은 디자인하기 불편한데 빼도 돼?
A. 스타일은 CSS로 조정하고 의미 구조는 유지하는 것이 좋다.

Q. radio group 오류는 어디에 표시해?
A. fieldset 내부 또는 group 가까운 위치에 group error message로 표시한다.

Q. group error는 개별 input error와 달라?
A. 그렇다. 여러 input이 하나의 validation 단위일 때 group 전체 오류로 처리한다.

Q. 약관 동의 오류는 어떻게 전달해?
A. fieldset과 legend로 약관 그룹을 설명하고 error message를 group과 연결한다.

Q. 날짜 범위 오류는 어느 input에 붙여?
A. 시작일과 종료일의 관계 오류라면 group error로 제공하는 것이 명확하다.

Q. select의 첫 옵션은 어떻게 써?
A. “지역을 선택하세요”처럼 안내 문구를 제공하고 빈 value로 처리할 수 있다.

Q. custom select가 더 좋아?
A. 디자인 자유도는 높지만 keyboard, role, focus 관리가 필요해 구현 난도가 높다.

Q. select 오류는 어떻게 연결해?
A. error message id를 만들고 select의 aria-describedby에 연결하며 aria-invalid를 오류 상태와 동기화한다.

Q. 디자인 때문에 select를 직접 만들면 안 돼?
A. 가능하지만 keyboard, role, aria, focus 관리가 필요해 구현 난도가 높다.

Q. Custom Select에서 가장 위험한 누락은?
A. keyboard 조작, focus 이동, aria-expanded, aria-selected 동기화 누락이다.

Q. Custom Select에 role만 붙이면 접근성 해결돼?
A. 아니다. role과 keyboard 동작, focus 흐름이 함께 구현되어야 한다.

Q. checkbox group에는 fieldset이 필요해?
A. 여러 checkbox가 하나의 질문에 속하면 fieldset과 legend를 사용하는 것이 좋다.

Q. checkbox 오류는 어떻게 표시해?
A. checkbox 또는 checkbox group과 error message를 aria-describedby로 연결한다.

Q. custom checkbox는 뭘 조심해야 해?
A. checked 상태, keyboard Space 조작, focus visible, accessible name을 직접 검증해야 한다.

Q. radio는 같은 name을 써야 해?
A. 같은 group에서 하나만 선택되도록 같은 name을 사용해야 한다.

Q. radio와 checkbox 차이는?
A. radio는 여러 옵션 중 하나 선택이고 checkbox는 독립 선택 또는 복수 선택이다.

Q. 파일 크기 제한은 어디에 써?
A. input 근처 helper text로 제공하고 aria-describedby로 연결하는 것이 좋다.

Q. drag and drop만 제공해도 돼?
A. 권장하지 않는다. keyboard 사용자를 위해 파일 선택 버튼 같은 대체 수단이 필요하다.

Q. 파일 업로드 오류는 어떻게 작성해?
A. 파일 형식, 크기, 개수 중 무엇이 문제인지 명확히 알려준다.

Q. 검색 input에도 label이 필요해?
A. 필요하다. 사용자가 무엇을 검색하는지 알 수 있어야 한다.

Q. 검색 아이콘 버튼에는 aria-label이 필요해?
A. 버튼에 visible text가 없다면 aria-label로 목적을 제공해야 한다.

Q. 검색 결과 개수는 스크린 리더에 알려야 해?
A. 동적으로 바뀌는 중요한 상태라면 role status 또는 aria-live를 고려할 수 있다.

Q. 검색 결과가 없으면 어떻게 보여줘?
A. Empty State로 결과 없음 메시지와 다음 행동을 제공한다.

Q. 로그인 버튼 loading 상태는 어떻게 표시해?
A. button text를 “로그인 중...”으로 바꾸고 필요하면 aria-busy를 사용할 수 있다.

Q. 비밀번호 찾기는 Button이야 Link야?
A. 비밀번호 찾기 페이지로 이동한다면 Link가 적합하다.

Q. autoComplete는 접근성과 관련 있어?
A. 사용자가 입력을 더 쉽게 완료하도록 도와주므로 적절히 사용하는 것이 좋다.

Q. 회원가입 Form에서 가장 중요한 접근성 기준은?
A. label 연결, 필수값 표시, helper text 연결, error message 연결, 약관 checkbox 접근성이다.

Q. 비밀번호 확인 오류는 어떻게 써?
A. “비밀번호가 일치하지 않습니다”처럼 사용자가 수정할 수 있게 명확히 작성한다.

Q. 약관 동의는 checkbox 하나면 충분해?
A. label 연결과 필수 여부, 오류 메시지 연결까지 함께 제공해야 한다.

Q. Error Summary와 첫 오류 field 중 어디로 focus를 줘?
A. 오류가 여러 개면 Error Summary, 단일 오류나 짧은 Form이면 첫 오류 field가 적합할 수 있다.

Q. focus 이동은 항상 좋은 거야?
A. 아니다. 불필요한 focus 이동은 사용자를 혼란스럽게 할 수 있다.

Q. tabIndex="-1"은 왜 써?
A. Tab 순서에는 포함하지 않지만 코드로 focus를 이동해야 하는 요소에 사용할 수 있다.

Q. 조건부 input이 생기면 자동 focus를 줘야 해?
A. 상황에 따라 다르다. 사용자가 바로 입력해야 하는 흐름이면 focus를 고려할 수 있다.

Q. input을 삭제했더니 focus가 사라져?
A. 삭제 후 다음 field, 이전 field, 추가 버튼 등 합리적인 위치로 focus를 이동해야 할 수 있다.

Q. 숨겨진 field도 validation 해야 해?
A. 일반적으로 사용자가 볼 수 없고 입력할 수 없는 field는 validation 대상에서 제외하는 것이 자연스럽다.

Q. 동적 Form에서 가장 흔한 문제는?
A. label 누락, validation 상태 불일치, focus lost, hidden field focus 문제가 자주 발생한다.

Q. Form input은 어떤 query로 찾는 게 좋아?
A. label이 연결되어 있다면 getByLabelText가 가장 자연스럽다.

Q. getByLabelText가 실패하면 접근성 문제야?
A. 가능성이 높다. label과 input 연결, label text, id 중복 여부를 확인한다.

Q. submit button은 어떻게 테스트해?
A. getByRole("button", { name: "로그인" })처럼 accessible name으로 찾는다.

Q. 오류 메시지는 어떻게 테스트해?
A. role alert 또는 오류 텍스트로 확인할 수 있다.

Q. checkbox는 어떻게 테스트해?
A. getByRole("checkbox", { name })으로 찾고 click 또는 keyboard로 checked 상태를 확인한다.

Q. Form Review에서 가장 먼저 볼 것은?
A. label 연결, placeholder-only 여부, error message 연결, aria-invalid 상태를 먼저 확인한다.

Q. Form에서 가장 흔한 접근성 문제는?
A. label 누락, placeholder label 대체, error message 미연결, checkbox/radio group 구조 누락이다.

Q. Form 테스트 실패가 접근성 문제일 수 있어?
A. 그렇다. getByLabelText나 getByRole 실패는 label, role, accessible name 문제일 수 있다.

Q. Review Agent는 Form 오류 문구도 봐야 해?
A. 봐야 한다. 오류 문구는 사용자가 무엇을 수정해야 하는지 명확히 알려야 한다.
