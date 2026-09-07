# HTML CSS Foundation Part03 - Form Elements

---

# 1. HTML Form

## 1.1 Form Concept

### [개념]

HTML Form은 사용자 입력을 수집하고 제출하기 위한 HTML 구조다.

Form은 로그인, 회원가입, 검색, 필터, 댓글, 리뷰, 결제 정보, 문의 작성 등 사용자 입력이 필요한 UI의 기본 구조다.

기본 예:

```html
<form>
  <label for="email">Email</label>
  <input id="email" name="email" type="email" />

  <button type="submit">Submit</button>
</form>
```

Form은 Frontend UI, Validation, Accessibility, Backend API Request와 직접 연결된다.

---

### [핵심]

Form 핵심:

- `form`은 사용자 입력 영역을 묶는다.
- `label`은 입력 필드의 이름을 제공한다.
- `input`은 한 줄 입력 필드다.
- `textarea`는 여러 줄 입력 필드다.
- `select`는 선택 목록이다.
- `button type="submit"`은 Form 제출에 사용한다.
- `name`은 Form Data 식별에 사용한다.
- `type`은 입력 목적과 브라우저 기본 검증에 영향을 준다.
- `required`는 필수 입력을 나타낸다.
- `disabled`는 입력 또는 제출을 비활성화한다.

---

### [실무]

2026 실무 기준에서 Form 문서는 단순 태그 사용법이 아니다.

Frontend Agent는 Form을 작성할 때 아래 기준을 함께 고려해야 한다.

- Accessibility
- Input Label 연결
- Form Validation
- Error Message 구조
- Backend API Request Body
- Controlled Component 변환 가능성
- React Form State 설계
- Submit Button 동작
- Loading / Disabled UX
- Mobile Input Keyboard 최적화

Form 실무 Flow:

```text
User Input
→ Form Field
→ Label Connection
→ Validation
→ Error Message
→ Submit
→ API Request
→ Success or Failure Feedback
```

---

### [FAQ]

Q. HTML Form이 뭐야?
A. 사용자 입력을 수집하고 제출하기 위한 HTML 구조다.

Q. Form은 언제 사용해?
A. 로그인, 회원가입, 검색, 댓글, 리뷰, 문의 작성처럼 사용자 입력이 필요한 UI에 사용한다.

Q. React를 써도 form 태그가 필요해?
A. 필요할 수 있다. React에서도 의미 있는 입력 구조와 submit 동작을 위해 form을 사용한다.

Q. Form은 Backend API와 연결돼?
A. 연결된다. Form 입력값은 보통 API Request Body 또는 Query Parameter로 전송된다.

---

# 2. Label

## 2.1 Label Element

### [개념]

`label`은 입력 필드의 이름을 제공하는 HTML 요소다.

사용자가 어떤 값을 입력해야 하는지 알려주고, 스크린 리더가 입력 필드를 올바르게 안내하도록 돕는다.

---

### [핵심]

`label` 핵심:

- 입력 필드의 이름을 제공한다.
- `for` 속성과 input `id`를 연결한다.
- label을 클릭하면 연결된 input에 focus가 이동한다.
- Accessibility에 필수적이다.
- placeholder를 label 대체로 사용하지 않는다.
- React에서는 `for` 대신 `htmlFor`를 사용한다.

HTML 예:

```html
<label for="email">Email</label> <input id="email" name="email" type="email" />
```

React JSX 예:

```jsx
<label htmlFor="email">Email</label>
<input id="email" name="email" type="email" />
```

---

### [실무]

실무에서는 모든 주요 입력 필드에 명확한 label을 제공한다.

좋은 예:

```html
<label for="password">Password</label>
<input id="password" name="password" type="password" />
```

나쁜 예:

```html
<input name="password" type="password" placeholder="Password" />
```

검수 기준:

- input에 연결된 label이 있는가?
- label `for`와 input `id`가 일치하는가?
- React에서는 `htmlFor`를 사용했는가?
- placeholder를 label처럼 사용하지 않았는가?
- label 텍스트가 입력 목적을 명확히 설명하는가?

---

### [FAQ]

Q. label은 왜 필요해?
A. 사용자가 입력 항목을 이해하고 스크린 리더가 필드를 올바르게 안내하기 위해 필요하다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. label for와 input id는 왜 맞춰야 해?
A. label과 input을 명확히 연결해 클릭, focus, 스크린 리더 안내가 가능하게 하기 위해서다.

Q. React에서 label for를 그대로 써도 돼?
A. 아니다. JSX에서는 `htmlFor`를 사용한다.

---

# 3. Input

## 3.1 Input Element

### [개념]

`input`은 사용자로부터 한 줄 데이터를 입력받는 HTML 요소다.

`type` 속성에 따라 text, email, password, number, date, checkbox, radio 등 다양한 입력 방식으로 동작한다.

---

### [핵심]

`input` 핵심:

- 한 줄 입력 필드다.
- `type`으로 입력 목적을 지정한다.
- `id`는 label 연결에 사용한다.
- `name`은 데이터 식별에 사용한다.
- `value`는 입력값이다.
- `placeholder`는 입력 예시 또는 힌트다.
- `required`는 필수 입력을 나타낸다.
- `disabled`는 입력 불가 상태를 만든다.
- `readonly`는 읽기 전용 입력을 만든다.

예:

```html
<label for="username">Username</label>
<input id="username" name="username" type="text" required />
```

---

### [실무]

Input type은 입력 목적에 맞게 선택해야 한다.

입력 목적별 예:

```html
<input type="text" name="nickname" />
<input type="email" name="email" />
<input type="password" name="password" />
<input type="number" name="age" />
<input type="date" name="eventDate" />
<input type="search" name="keyword" />
```

실무 기준:

- Email 입력은 `type="email"` 사용
- Password 입력은 `type="password"` 사용
- 검색 입력은 `type="search"` 고려
- 숫자 입력은 `type="number"` 사용 전 UX 검토
- 날짜 입력은 브라우저 지원과 디자인 요구사항 검토
- label 없는 input 금지
- placeholder에 필수 정보를 의존하지 않음

---

### [FAQ]

Q. input은 언제 써?
A. 사용자로부터 한 줄 데이터를 입력받을 때 사용한다.

Q. input type은 왜 중요해?
A. 브라우저 기본 검증, 모바일 키보드, 접근성, 사용자 경험에 영향을 주기 때문이다.

Q. email 입력에는 어떤 type을 써?
A. `type="email"`을 사용한다.

Q. password 입력에는 어떤 type을 써?
A. `type="password"`를 사용한다.

Q. input name은 왜 필요해?
A. Form Data와 Backend API Request에서 입력 필드를 식별하기 위해 필요하다.

---

## 3.2 Text Input

### [개념]

Text Input은 일반 문자열을 입력받는 기본 입력 필드다.

이름, 닉네임, 제목, 검색어, 주소 일부 등 짧은 텍스트 입력에 사용한다.

---

### [핵심]

Text Input 핵심:

- `type="text"`를 사용한다.
- 짧은 한 줄 텍스트 입력에 적합하다.
- `maxlength`로 입력 길이를 제한할 수 있다.
- `placeholder`는 예시 제공에 사용한다.
- label과 함께 사용해야 한다.

예:

```html
<label for="nickname">Nickname</label>
<input id="nickname" name="nickname" type="text" maxlength="20" />
```

---

### [실무]

Text Input은 가장 기본적인 Form Field다.

실무 검수 기준:

- 입력 목적에 맞는 label이 있는가?
- 불필요하게 모든 입력을 text로 처리하지 않았는가?
- 검색이면 `type="search"`가 더 적절하지 않은가?
- email이면 `type="email"`이 더 적절하지 않은가?
- password이면 `type="password"`가 더 적절하지 않은가?
- 길이 제한이 필요한 경우 `maxlength` 또는 validation이 있는가?

---

### [FAQ]

Q. type text는 언제 써?
A. 이름, 제목, 닉네임처럼 일반 한 줄 텍스트 입력에 사용한다.

Q. 모든 input을 type text로 써도 돼?
A. 권장하지 않는다. 입력 목적에 맞는 type을 사용하는 것이 좋다.

Q. maxlength는 언제 써?
A. 닉네임, 제목처럼 입력 길이 제한이 필요한 경우 사용한다.

---

## 3.3 Email Input

### [개념]

Email Input은 이메일 주소 입력을 위한 HTML 입력 필드다.

브라우저는 `type="email"`을 기준으로 이메일 형식 검증과 모바일 키보드 최적화를 제공할 수 있다.

---

### [핵심]

Email Input 핵심:

- `type="email"`을 사용한다.
- 이메일 형식 기본 검증에 도움을 준다.
- 모바일에서 이메일 입력에 맞는 키보드를 제공할 수 있다.
- 로그인, 회원가입, 비밀번호 찾기 Form에 자주 사용된다.
- Backend Validation도 반드시 필요하다.

예:

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" autocomplete="email" required />
```

---

### [실무]

Email Input은 Frontend 기본 검증만으로 충분하지 않다.

실무 Flow:

```text
Email Input
→ Browser Basic Validation
→ Frontend Validation
→ API Request
→ Backend Validation
→ Error Message
```

검수 기준:

- `type="email"`을 사용했는가?
- `autocomplete="email"`을 고려했는가?
- label이 연결되어 있는가?
- 이메일 형식 오류 메시지가 있는가?
- Backend에서도 이메일 형식을 검증하는가?

---

### [FAQ]

Q. email input은 왜 써?
A. 이메일 형식 기본 검증과 모바일 키보드 최적화에 도움이 되기 때문이다.

Q. type email만 쓰면 이메일 검증이 충분해?
A. 아니다. Frontend와 Backend Validation을 함께 사용해야 한다.

Q. 로그인 이메일 필드에 autocomplete를 써도 돼?
A. 가능하다. 일반적으로 `autocomplete="email"`을 사용할 수 있다.

---

## 3.4 Password Input

### [개념]

Password Input은 비밀번호 입력을 위한 HTML 입력 필드다.

입력값이 화면에 직접 표시되지 않도록 `type="password"`를 사용한다.

---

### [핵심]

Password Input 핵심:

- `type="password"`를 사용한다.
- 입력값이 마스킹된다.
- 로그인, 회원가입, 비밀번호 변경에 사용한다.
- `autocomplete` 값을 상황에 맞게 지정한다.
- 보안 검증은 Backend에서 반드시 수행한다.

예:

```html
<label for="password">Password</label>
<input
  id="password"
  name="password"
  type="password"
  autocomplete="current-password"
  required
/>
```

---

### [실무]

Autocomplete 권장 예:

```html
<!-- 로그인 -->
<input type="password" autocomplete="current-password" />

<!-- 회원가입 / 새 비밀번호 -->
<input type="password" autocomplete="new-password" />
```

검수 기준:

- 비밀번호 입력에 `type="password"`를 사용했는가?
- 로그인에서는 `autocomplete="current-password"`를 고려했는가?
- 회원가입 또는 변경에서는 `autocomplete="new-password"`를 고려했는가?
- 비밀번호 조건 안내가 있는가?
- 비밀번호 오류 메시지가 구체적인가?
- 비밀번호 정책은 Backend에서도 검증되는가?

---

### [FAQ]

Q. password input은 왜 type password를 써?
A. 입력값을 화면에 그대로 노출하지 않고 마스킹하기 위해 사용한다.

Q. password autocomplete는 어떻게 써?
A. 로그인은 `current-password`, 새 비밀번호는 `new-password`를 사용할 수 있다.

Q. Frontend에서 비밀번호 조건을 검사하면 충분해?
A. 아니다. Backend에서도 반드시 검증해야 한다.

---

## 3.5 Number Input

### [개념]

Number Input은 숫자 입력을 위한 HTML 입력 필드다.

수량, 나이, 금액, 인원 수 등 숫자 입력에 사용할 수 있다.

---

### [핵심]

Number Input 핵심:

- `type="number"`를 사용한다.
- `min`, `max`, `step`을 지정할 수 있다.
- 숫자 전용 입력 UI를 제공할 수 있다.
- 모바일에서 숫자 키보드를 제공할 수 있다.
- 모든 숫자형 데이터에 무조건 적합하지는 않다.

예:

```html
<label for="peopleCount">People Count</label>
<input id="peopleCount" name="peopleCount" type="number" min="1" max="10" />
```

---

### [실무]

Number Input 사용 전 데이터 성격을 확인해야 한다.

적합한 경우:

- 수량
- 인원 수
- 나이
- 평점
- 금액

부적합할 수 있는 경우:

- 전화번호
- 우편번호
- 사업자번호
- 앞자리 0이 의미 있는 숫자 문자열

전화번호 예:

```html
<label for="phone">Phone</label> <input id="phone" name="phone" type="tel" />
```

검수 기준:

- 진짜 계산 가능한 숫자인가?
- 앞자리 0이 사라지면 안 되는 값인가?
- `min`, `max`, `step`이 필요한가?
- 전화번호를 number로 처리하지 않았는가?
- Backend에서도 숫자 범위를 검증하는가?

---

### [FAQ]

Q. number input은 언제 써?
A. 수량, 인원 수, 나이, 금액처럼 실제 숫자 연산이나 범위 검증이 필요한 값에 사용한다.

Q. 전화번호에 type number를 써도 돼?
A. 권장하지 않는다. 전화번호는 숫자처럼 보이지만 문자열 데이터이므로 `type="tel"`이 더 적합하다.

Q. min과 max는 왜 써?
A. 입력 가능한 숫자 범위를 제한하기 위해 사용한다.

---

# 4. Textarea

## 4.1 Textarea Element

### [개념]

`textarea`는 여러 줄 텍스트 입력을 받는 HTML 요소다.

댓글, 리뷰, 문의 내용, 소개글, 게시글 내용처럼 긴 텍스트 입력에 사용한다.

---

### [핵심]

`textarea` 핵심:

- 여러 줄 입력 필드다.
- `rows`로 기본 높이를 지정할 수 있다.
- `maxlength`로 입력 길이를 제한할 수 있다.
- label과 연결해야 한다.
- placeholder는 입력 예시로만 사용한다.
- React에서는 children이 아니라 `value`로 제어하는 경우가 많다.

예:

```html
<label for="reviewContent">Review</label>
<textarea
  id="reviewContent"
  name="reviewContent"
  rows="5"
  maxlength="500"
></textarea>
```

---

### [실무]

Textarea는 긴 입력 UX를 고려해야 한다.

실무 기준:

- 입력 목적을 label로 명확히 제공
- 최대 글자 수 안내
- 글자 수 카운터 제공 고려
- Error Message를 textarea 근처에 배치
- Resize 허용 여부 결정
- 긴 내용 전송 시 Backend Validation 필수
- XSS 방어는 출력 시점에도 필요

예:

```html
<label for="comment">Comment</label>
<textarea
  id="comment"
  name="comment"
  rows="4"
  maxlength="300"
  placeholder="Write your comment"
></textarea>
<p id="comment-help">Maximum 300 characters.</p>
```

---

### [FAQ]

Q. textarea는 언제 써?
A. 댓글, 리뷰, 문의 내용처럼 여러 줄 텍스트 입력이 필요할 때 사용한다.

Q. textarea에 maxlength를 써도 돼?
A. 가능하다. 긴 입력의 최대 길이를 제한할 때 유용하다.

Q. textarea도 label이 필요해?
A. 필요하다. 입력 목적을 명확히 전달하기 위해 label을 연결하는 것이 좋다.

Q. textarea 내용은 보안 처리가 필요해?
A. 필요하다. 사용자 입력을 화면에 출력할 때 XSS 방어를 고려해야 한다.

---

# 5. Select

## 5.1 Select Element

### [개념]

`select`는 미리 정의된 선택지 중 하나 또는 여러 개를 선택하는 HTML 요소다.

지역, 카테고리, 정렬 기준, 필터 옵션 같은 선택 UI에 사용한다.

---

### [핵심]

`select` 핵심:

- 선택 목록을 제공한다.
- `option`으로 선택지를 작성한다.
- label과 연결해야 한다.
- `value`는 전송 또는 상태 관리 값이다.
- `disabled` option으로 안내 문구를 만들 수 있다.
- 선택지가 많으면 검색 가능한 Custom Select를 고려할 수 있다.

예:

```html
<label for="region">Region</label>
<select id="region" name="region">
  <option value="">Select Region</option>
  <option value="seoul">Seoul</option>
  <option value="busan">Busan</option>
</select>
```

---

### [실무]

Select는 정해진 값 중 선택할 때 사용한다.

실무 기준:

- 선택지가 적거나 중간 정도일 때 적합
- 선택지가 너무 많으면 검색 UI 고려
- Backend enum 또는 code value와 연결 가능
- value는 화면 텍스트가 아니라 안정적인 코드값 사용 권장
- 빈 값 처리 여부 명확히 결정
- label 연결 필수

예:

```html
<label for="sort">Sort</label>
<select id="sort" name="sort">
  <option value="latest">Latest</option>
  <option value="popular">Popular</option>
  <option value="rating">Rating</option>
</select>
```

---

### [FAQ]

Q. select는 언제 써?
A. 미리 정해진 선택지 중 하나를 선택해야 할 때 사용한다.

Q. option value는 왜 필요해?
A. 화면 표시 텍스트와 실제 전송 값을 분리하기 위해 필요하다.

Q. 선택지가 너무 많으면 select가 좋아?
A. 항상 좋지는 않다. 선택지가 많으면 검색 가능한 UI를 고려한다.

Q. select에도 label이 필요해?
A. 필요하다. 어떤 선택 목록인지 명확히 전달해야 한다.

---

# 6. Checkbox and Radio

## 6.1 Checkbox

### [개념]

Checkbox는 여러 선택지 중 복수 선택이 가능하거나 단일 boolean 상태를 표현하는 입력 요소다.

약관 동의, 관심 카테고리 선택, 필터 다중 선택에 사용한다.

---

### [핵심]

Checkbox 핵심:

- `type="checkbox"`를 사용한다.
- 복수 선택이 가능하다.
- 단일 true/false 상태에도 사용할 수 있다.
- label과 연결해야 한다.
- `checked`는 선택 상태를 나타낸다.
- 같은 그룹의 checkbox는 같은 name을 사용할 수 있다.

예:

```html
<input id="agree" name="agree" type="checkbox" />
<label for="agree">I agree to the terms.</label>
```

---

### [실무]

Checkbox는 선택 상태가 명확히 보여야 한다.

복수 선택 예:

```html
<fieldset>
  <legend>Festival Theme</legend>

  <input id="music" name="theme" type="checkbox" value="music" />
  <label for="music">Music</label>

  <input id="food" name="theme" type="checkbox" value="food" />
  <label for="food">Food</label>
</fieldset>
```

검수 기준:

- checkbox와 label이 연결되어 있는가?
- 여러 선택지를 fieldset / legend로 묶었는가?
- 필수 동의 항목은 required 또는 validation이 있는가?
- checked 상태가 시각적으로 명확한가?
- label 클릭으로 선택이 가능한가?

---

### [FAQ]

Q. checkbox는 언제 써?
A. 복수 선택 또는 true/false 상태를 입력받을 때 사용한다.

Q. 약관 동의에는 checkbox를 써?
A. 일반적으로 사용한다. 사용자가 동의 여부를 명확히 선택할 수 있기 때문이다.

Q. checkbox 그룹에는 fieldset이 필요해?
A. 여러 관련 checkbox를 묶을 때 fieldset과 legend를 사용하면 접근성이 좋아진다.

---

## 6.2 Radio

### [개념]

Radio는 여러 선택지 중 하나만 선택할 수 있는 입력 요소다.

성별, 결제 방식, 정렬 기준, 공개 범위처럼 단일 선택이 필요한 경우 사용한다.

---

### [핵심]

Radio 핵심:

- `type="radio"`를 사용한다.
- 같은 `name`을 가진 radio 그룹에서 하나만 선택된다.
- 각 radio는 고유한 `id`를 가져야 한다.
- 각 radio는 label과 연결해야 한다.
- 관련 radio 그룹은 fieldset과 legend로 묶는 것이 좋다.

예:

```html
<fieldset>
  <legend>Visibility</legend>

  <input id="public" name="visibility" type="radio" value="public" />
  <label for="public">Public</label>

  <input id="private" name="visibility" type="radio" value="private" />
  <label for="private">Private</label>
</fieldset>
```

---

### [실무]

Radio는 하나만 선택 가능한 경우에 사용한다.

실무 기준:

- 선택지 수가 적을 때 적합
- 선택지가 많으면 select 고려
- 같은 그룹은 같은 name 사용
- 기본 선택값 필요 여부 검토
- label 클릭 가능해야 함
- fieldset / legend로 그룹 의미 제공

검수 기준:

- 같은 radio 그룹의 name이 동일한가?
- 각 radio의 id가 고유한가?
- label for와 input id가 일치하는가?
- 하나만 선택 가능한 요구사항인가?
- checkbox가 더 적절하지 않은가?

---

### [FAQ]

Q. radio는 언제 써?
A. 여러 선택지 중 하나만 선택해야 할 때 사용한다.

Q. radio와 checkbox 차이는 뭐야?
A. radio는 단일 선택, checkbox는 복수 선택 또는 boolean 상태에 사용한다.

Q. radio 그룹에서 name은 왜 같아야 해?
A. 같은 name을 가진 radio들이 하나의 선택 그룹으로 동작하기 때문이다.

Q. radio도 label이 필요해?
A. 필요하다. 선택지 의미와 클릭 영역을 제공하기 위해 label을 연결한다.

---

# 7. Fieldset and Legend

## 7.1 Fieldset

### [개념]

`fieldset`은 관련 있는 Form Control을 하나의 그룹으로 묶는 HTML 요소다.

`legend`는 해당 그룹의 제목을 제공한다.

---

### [핵심]

Fieldset / Legend 핵심:

- 관련 입력 그룹을 묶는다.
- radio 그룹에 특히 유용하다.
- checkbox 그룹에도 유용하다.
- `legend`는 그룹의 이름을 제공한다.
- Accessibility에서 입력 그룹 의미를 전달한다.

예:

```html
<fieldset>
  <legend>Notification Settings</legend>

  <input id="emailNotice" name="notice" type="checkbox" value="email" />
  <label for="emailNotice">Email Notification</label>

  <input id="smsNotice" name="notice" type="checkbox" value="sms" />
  <label for="smsNotice">SMS Notification</label>
</fieldset>
```

---

### [실무]

Form이 복잡해질수록 fieldset과 legend는 구조 이해를 돕는다.

사용 적합:

- Radio Group
- Checkbox Group
- 주소 입력 그룹
- 결제 정보 그룹
- 알림 설정 그룹
- 검색 필터 그룹

검수 기준:

- 관련 입력 필드가 의미 있게 묶였는가?
- legend가 그룹의 목적을 설명하는가?
- fieldset을 단순 border 스타일링 용도로 쓰지 않았는가?
- 너무 큰 Form 전체를 하나의 fieldset으로만 묶지 않았는가?

---

### [FAQ]

Q. fieldset은 언제 써?
A. 관련 있는 Form 입력들을 하나의 그룹으로 묶을 때 사용한다.

Q. legend는 왜 필요해?
A. fieldset 그룹의 제목을 제공해 사용자가 입력 그룹의 목적을 이해하게 한다.

Q. radio 그룹에는 fieldset이 좋아?
A. 좋다. radio 선택지가 하나의 질문에 속한다는 의미를 명확히 전달한다.

---

# 8. Button in Form

## 8.1 Submit Button

### [개념]

Submit Button은 Form 입력값을 제출하는 버튼이다.

Form 내부의 `button`은 기본적으로 `type="submit"`처럼 동작할 수 있으므로 type을 명시하는 것이 좋다.

---

### [핵심]

Submit Button 핵심:

- Form 제출에는 `type="submit"`을 사용한다.
- 단순 클릭 동작은 `type="button"`을 사용한다.
- 초기화는 `type="reset"`을 사용할 수 있지만 주의가 필요하다.
- Loading 중에는 submit button을 disabled 처리할 수 있다.
- Button Text는 동작을 명확히 표현해야 한다.

예:

```html
<form>
  <label for="keyword">Keyword</label>
  <input id="keyword" name="keyword" type="search" />

  <button type="submit">Search</button>
</form>
```

---

### [실무]

Form 내부 button에는 type을 명시한다.

좋은 예:

```html
<button type="submit">Login</button> <button type="button">Cancel</button>
```

나쁜 예:

```html
<button>Cancel</button>
```

React 예:

```jsx
function LoginForm({ isSubmitting }) {
  return (
    <form>
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Logging in..." : "Login"}
      </button>
    </form>
  );
}
```

검수 기준:

- submit button에 `type="submit"`이 있는가?
- 취소, 모달 열기, 중복 확인 버튼은 `type="button"`인가?
- Loading 중 중복 제출을 방지하는가?
- disabled 상태에서 사용자가 이유를 이해할 수 있는가?
- 버튼 텍스트가 동작을 설명하는가?

---

### [FAQ]

Q. Form 안의 button type을 꼭 써야 해?
A. 명시하는 것이 좋다. 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있다.

Q. 제출 버튼은 어떤 type을 써?
A. `type="submit"`을 사용한다.

Q. 취소 버튼은 어떤 type을 써?
A. Form 내부에서는 `type="button"`을 사용하는 것이 안전하다.

Q. Loading 중 submit button을 disabled 해도 돼?
A. 가능하다. 중복 제출 방지에 도움이 된다.

---

# 9. Form Validation

## 9.1 Validation Concept

### [개념]

Form Validation은 사용자 입력값이 요구사항을 만족하는지 확인하는 과정이다.

Validation은 Frontend와 Backend 양쪽에서 모두 필요하다.

---

### [핵심]

Validation 핵심:

- Frontend Validation은 빠른 피드백을 제공한다.
- Backend Validation은 데이터 무결성과 보안을 보장한다.
- `required`는 필수 입력을 나타낸다.
- `minlength`, `maxlength`는 길이 제한에 사용한다.
- `min`, `max`는 숫자 범위 제한에 사용한다.
- `pattern`은 정규식 검증에 사용할 수 있다.
- Error Message는 입력 필드 근처에 제공한다.

예:

```html
<label for="username">Username</label>
<input
  id="username"
  name="username"
  type="text"
  minlength="2"
  maxlength="20"
  required
/>
```

---

### [실무]

Validation Flow:

```text
User Input
→ Browser Constraint Validation
→ Frontend Custom Validation
→ API Request
→ Backend Validation
→ Error Response
→ Field Error Message
```

실무 기준:

- Frontend Validation만 믿지 않는다.
- Backend Validation은 필수다.
- Error Message는 구체적으로 작성한다.
- 에러 필드 근처에 메시지를 표시한다.
- 색상만으로 에러를 표시하지 않는다.
- submit 전 validation과 submit 후 서버 에러를 구분한다.
- API 에러를 Form Field Error로 매핑한다.

---

### [FAQ]

Q. Form Validation이 뭐야?
A. 사용자 입력값이 요구사항을 만족하는지 확인하는 과정이다.

Q. Frontend Validation만 있으면 충분해?
A. 아니다. Backend Validation도 반드시 필요하다.

Q. required는 무엇을 해?
A. 필수 입력 필드임을 브라우저에 알려준다.

Q. 에러 메시지는 어디에 보여줘야 해?
A. 사용자가 수정할 수 있도록 해당 입력 필드 가까이에 보여주는 것이 좋다.

---

## 9.2 Error Message

### [개념]

Error Message는 사용자가 입력 문제를 이해하고 수정할 수 있도록 안내하는 문구다.

Form Accessibility와 UX에서 중요한 요소다.

---

### [핵심]

Error Message 핵심:

- 입력 필드 근처에 표시한다.
- 무엇이 잘못됐는지 구체적으로 알려준다.
- 어떻게 수정해야 하는지 안내한다.
- 색상만으로 오류를 전달하지 않는다.
- 필요한 경우 `aria-describedby`로 input과 연결한다.
- Error Message는 상태 변화에 따라 동적으로 표시될 수 있다.

예:

```html
<label for="email">Email</label>
<input id="email" name="email" type="email" aria-describedby="email-error" />
<p id="email-error">Enter a valid email address.</p>
```

---

### [실무]

좋은 Error Message:

```text
Enter a valid email address.
Password must be at least 8 characters.
Nickname is required.
```

나쁜 Error Message:

```text
Invalid.
Error.
Wrong.
```

React Form에서는 서버 에러도 필드 단위로 매핑한다.

검수 기준:

- 에러 메시지가 구체적인가?
- 에러가 입력 필드 근처에 표시되는가?
- 색상 외 텍스트 정보가 있는가?
- input과 error message가 연결되어 있는가?
- 서버 에러와 클라이언트 에러를 구분할 수 있는가?

---

### [FAQ]

Q. 좋은 에러 메시지는 뭐야?
A. 무엇이 잘못됐고 어떻게 수정해야 하는지 구체적으로 알려주는 메시지다.

Q. 색상만으로 에러를 표시해도 돼?
A. 안 된다. 텍스트나 아이콘 등 다른 정보도 함께 제공해야 한다.

Q. aria-describedby는 언제 써?
A. 입력 필드와 도움말 또는 에러 메시지를 연결할 때 사용한다.

---

# 10. Form Accessibility

## 10.1 Accessibility Rules

### [개념]

Form Accessibility는 사용자가 다양한 환경에서 입력 UI를 이해하고 조작할 수 있도록 만드는 기준이다.

Label, fieldset, legend, error message, focus, keyboard navigation이 핵심이다.

---

### [핵심]

Form Accessibility 핵심:

- 모든 주요 input에 label 연결
- placeholder를 label 대체로 사용하지 않음
- radio / checkbox 그룹은 fieldset과 legend 사용 권장
- Error Message를 입력 필드와 연결
- Keyboard Navigation 가능
- Focus Style 유지
- Disabled 상태 명확히 표현
- 색상만으로 상태 전달 금지
- `aria-invalid`는 오류 상태 표현에 사용할 수 있음
- `aria-describedby`는 도움말 또는 오류 메시지 연결에 사용할 수 있음

---

### [실무]

Accessible Form 예:

```html
<form>
  <label for="email">Email</label>
  <input
    id="email"
    name="email"
    type="email"
    aria-invalid="true"
    aria-describedby="email-error"
    required
  />
  <p id="email-error">Enter a valid email address.</p>

  <button type="submit">Submit</button>
</form>
```

검수 Checklist:

```md
- [ ] input과 label이 연결되어 있는가?
- [ ] placeholder를 label 대체로 사용하지 않았는가?
- [ ] radio / checkbox 그룹에 fieldset과 legend가 있는가?
- [ ] error message가 필드 근처에 있는가?
- [ ] error message가 input과 연결되어 있는가?
- [ ] keyboard로 모든 필드에 접근 가능한가?
- [ ] focus style이 보이는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] disabled 상태가 명확한가?
```

---

### [FAQ]

Q. Form Accessibility에서 가장 중요한 것은 뭐야?
A. label 연결, keyboard 접근, error message, focus style, fieldset/legend 구조다.

Q. placeholder만 있으면 접근성에 충분해?
A. 아니다. placeholder는 label을 대체할 수 없다.

Q. aria-invalid는 언제 써?
A. 입력 필드가 오류 상태임을 보조 기술에 전달할 때 사용할 수 있다.

Q. focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

---

# 11. Form and React

## 11.1 React Form Markup

### [개념]

React Form은 HTML Form 구조를 JSX로 작성하고, 입력값을 State 또는 Form Library로 관리하는 방식이다.

React에서도 HTML Form의 Semantic Structure와 Accessibility 기준은 유지된다.

---

### [핵심]

React Form 핵심:

- `form` 태그 사용 가능
- `label htmlFor` 사용
- input `id`와 label `htmlFor` 일치
- `onSubmit`에서 제출 처리
- 기본 submit reload 방지를 위해 `event.preventDefault()` 사용 가능
- Controlled Component는 `value`와 `onChange`를 사용
- Loading 중 button disabled 처리
- Field Error를 input 근처에 표시

예:

```jsx
function SearchForm({ onSearch }) {
  function handleSubmit(event) {
    event.preventDefault();
    onSearch();
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="keyword">Keyword</label>
      <input id="keyword" name="keyword" type="search" />

      <button type="submit">Search</button>
    </form>
  );
}
```

---

### [실무]

React Form 검수 기준:

- `label htmlFor`가 올바른가?
- input id와 htmlFor가 일치하는가?
- Form 제출은 onSubmit에서 처리하는가?
- submit button type이 명확한가?
- 단순 버튼이 submit으로 오작동하지 않는가?
- Field Error가 입력 필드와 가까운가?
- API 요청 중 중복 제출을 방지하는가?
- Controlled / Uncontrolled 전략이 혼용되어 혼란스럽지 않은가?

Controlled Input 예:

```jsx
function NicknameForm() {
  const [nickname, setNickname] = useState("");

  return (
    <form>
      <label htmlFor="nickname">Nickname</label>
      <input
        id="nickname"
        name="nickname"
        type="text"
        value={nickname}
        onChange={(event) => setNickname(event.target.value)}
      />
    </form>
  );
}
```

---

### [FAQ]

Q. React에서도 form 태그를 써?
A. 쓸 수 있다. Form 의미와 submit 처리 구조를 명확히 하기 위해 사용한다.

Q. React label에서는 for를 써?
A. 아니다. JSX에서는 `htmlFor`를 사용한다.

Q. React Form에서 onSubmit은 왜 써?
A. Form 제출 이벤트를 한 곳에서 처리하기 위해 사용한다.

Q. Controlled Component가 뭐야?
A. input value를 React State로 관리하는 입력 컴포넌트 방식이다.

---

# 12. Common Mistakes

## 12.1 Form Common Mistakes

### [개념]

Form 실수는 입력 오류, 접근성 저하, API 요청 실패, 사용자 경험 문제로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- label 없이 input 작성
- placeholder를 label 대체로 사용
- label `for`와 input `id` 불일치
- React에서 `for` 사용
- input `name` 누락
- Form 내부 button type 누락
- 취소 버튼이 submit으로 동작
- 전화번호에 `type="number"` 사용
- radio 그룹 name 불일치
- checkbox / radio label 미연결
- fieldset / legend 없이 복잡한 선택 그룹 작성
- 에러 메시지가 입력 필드와 떨어져 있음
- 색상만으로 에러 표시
- Frontend Validation만 믿고 Backend Validation 누락
- Loading 중 중복 제출 허용
- disabled 상태 설명 부족
- focus style 제거

---

### [실무]

Troubleshooting Flow:

```text
Form Bug
→ Label Connection Check
→ Input Type Check
→ Name / Value Check
→ Button Type Check
→ Validation Check
→ Error Message Check
→ API Payload Check
→ Backend Error Mapping Check
```

문제 예:

```text
문제: 취소 버튼 클릭 시 Form 제출됨
원인: Form 내부 button type 누락
해결: 취소 버튼에 type="button" 추가
```

```text
문제: 스크린 리더가 입력 필드 이름을 읽지 못함
원인: label 미연결
해결: label htmlFor와 input id 연결
```

```text
문제: 전화번호 앞자리 0이 사라짐
원인: type="number" 사용
해결: type="tel" 또는 text 사용
```

---

### [FAQ]

Q. Form에서 가장 흔한 실수는 뭐야?
A. label 누락, button type 누락, input type 오용, error message 부족이 흔하다.

Q. 취소 버튼이 제출되는 이유는 뭐야?
A. Form 내부 button의 기본 동작이 submit일 수 있기 때문이다.

Q. 전화번호 앞자리 0이 사라지는 이유는 뭐야?
A. 전화번호를 number로 처리했기 때문일 수 있다. 전화번호는 문자열로 다루는 것이 좋다.

Q. Form 오류는 어떻게 디버깅해?
A. label 연결, input type, name/value, button type, validation, API payload 순서로 확인한다.

---

# 13. Comparison Rules

## 13.1 Input vs Textarea

### [개념]

`input`은 한 줄 입력에 사용하고 `textarea`는 여러 줄 입력에 사용한다.

---

### [핵심]

| 비교       | input                | textarea              |
| ---------- | -------------------- | --------------------- |
| 입력 형태  | 한 줄                | 여러 줄               |
| 주요 사용  | 이름, 이메일, 검색어 | 댓글, 리뷰, 문의 내용 |
| type 속성  | 사용                 | 사용하지 않음         |
| 길이 제한  | maxlength            | maxlength             |
| 높이 조절  | 제한적               | rows / CSS            |
| React 제어 | value / onChange     | value / onChange      |

---

### [실무]

선택 기준:

```text
Short Single Line Text → input
Long Multi Line Text → textarea
Email → input type="email"
Password → input type="password"
Comment / Review → textarea
```

---

### [FAQ]

Q. input과 textarea 차이는 뭐야?
A. input은 한 줄 입력, textarea는 여러 줄 입력에 사용한다.

Q. 댓글 입력은 input이 좋아 textarea가 좋아?
A. 여러 줄 입력 가능성이 있으므로 textarea가 적합하다.

---

## 13.2 Checkbox vs Radio

### [개념]

Checkbox는 복수 선택 또는 boolean 상태에 사용하고 Radio는 여러 선택지 중 하나만 선택할 때 사용한다.

---

### [핵심]

| 비교      | checkbox             | radio                      |
| --------- | -------------------- | -------------------------- |
| 선택 방식 | 복수 선택 가능       | 단일 선택                  |
| 사용 예   | 약관 동의, 다중 필터 | 결제 방식, 공개 범위       |
| name      | 그룹 공유 가능       | 같은 그룹은 동일 name 필수 |
| 상태      | checked true/false   | 그룹 중 하나 checked       |
| 그룹 구조 | fieldset 권장        | fieldset 권장              |

---

### [실무]

선택 기준:

```text
Multiple Selection → checkbox
Single Selection → radio
Boolean Agreement → checkbox
One Payment Method → radio
Many Options Dropdown → select
```

---

### [FAQ]

Q. checkbox와 radio 차이는 뭐야?
A. checkbox는 복수 선택, radio는 단일 선택에 사용한다.

Q. 약관 동의는 checkbox야 radio야?
A. 일반적으로 checkbox를 사용한다.

Q. 결제 방식 선택은 checkbox야 radio야?
A. 하나만 선택하는 경우 radio가 적합하다.

---

## 13.3 Disabled vs Readonly

### [개념]

`disabled`는 사용자가 값을 변경하거나 제출할 수 없게 하고, `readonly`는 값을 변경할 수 없지만 읽을 수 있게 한다.

---

### [핵심]

| 비교      | disabled                    | readonly            |
| --------- | --------------------------- | ------------------- |
| 수정 가능 | 불가                        | 불가                |
| focus     | 일반적으로 불가             | 가능                |
| Form 제출 | 보통 제외                   | 포함 가능           |
| 사용 예   | 비활성 버튼, 선택 불가 필드 | 수정 불가 정보      |
| 시각 상태 | 비활성 표현 필요            | 읽기 전용 표현 필요 |

---

### [실무]

선택 기준:

```text
Submit Prevent During Loading → disabled
Unavailable Option → disabled
Read Only User Email → readonly
Generated Value Preview → readonly
```

주의:

- disabled input은 Form 제출 데이터에서 제외될 수 있다.
- 제출해야 하는 읽기 전용 값은 readonly 또는 hidden input을 검토한다.
- disabled 상태는 이유를 사용자가 이해할 수 있어야 한다.

---

### [FAQ]

Q. disabled와 readonly 차이는 뭐야?
A. disabled는 비활성 상태로 제출에서 제외될 수 있고 readonly는 읽기 전용이지만 값은 유지된다.

Q. 제출해야 하는 값을 disabled로 둬도 돼?
A. 주의해야 한다. disabled 값은 제출에서 제외될 수 있으므로 readonly를 검토한다.

Q. Loading 중 버튼에는 disabled를 써도 돼?
A. 가능하다. 중복 제출 방지에 도움이 된다.

---

# 14. Best Practice

## 14.1 Form Best Practice

### [개념]

Form Best Practice는 입력 구조, 접근성, Validation, API 연동, React 변환 가능성을 안정적으로 만드는 작성 기준이다.

---

### [핵심]

권장 기준:

- 모든 주요 input에 label 연결
- placeholder를 label 대체로 사용하지 않음
- input type을 목적에 맞게 선택
- input name 작성
- Form 내부 button type 명시
- radio / checkbox 그룹은 fieldset과 legend 사용
- Error Message를 입력 필드 근처에 배치
- 색상만으로 에러 전달 금지
- Frontend Validation과 Backend Validation 병행
- Loading 중 중복 제출 방지
- disabled / readonly 차이 구분
- React JSX에서는 `htmlFor` 사용
- API Request Body와 Form Field Name 일관성 유지

---

### [실무]

기본 Form 예:

```html
<form>
  <label for="email">Email</label>
  <input
    id="email"
    name="email"
    type="email"
    autocomplete="email"
    required
    aria-describedby="email-help"
  />
  <p id="email-help">Enter your email address.</p>

  <label for="password">Password</label>
  <input
    id="password"
    name="password"
    type="password"
    autocomplete="current-password"
    required
  />

  <button type="submit">Login</button>
</form>
```

React Form 예:

```jsx
function LoginForm({ isSubmitting }) {
  return (
    <form>
      <label htmlFor="email">Email</label>
      <input
        id="email"
        name="email"
        type="email"
        autoComplete="email"
        required
      />

      <label htmlFor="password">Password</label>
      <input
        id="password"
        name="password"
        type="password"
        autoComplete="current-password"
        required
      />

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Logging in..." : "Login"}
      </button>
    </form>
  );
}
```

검수 Checklist:

```md
- [ ] form 구조가 명확한가?
- [ ] 모든 주요 input에 label이 있는가?
- [ ] label과 input id가 연결되어 있는가?
- [ ] React JSX에서 htmlFor를 사용했는가?
- [ ] input type이 입력 목적에 맞는가?
- [ ] input name이 API Request와 일치하는가?
- [ ] button type이 명시되어 있는가?
- [ ] radio / checkbox 그룹에 fieldset과 legend가 있는가?
- [ ] Validation 기준이 있는가?
- [ ] Error Message가 필드 근처에 있는가?
- [ ] 색상만으로 에러를 전달하지 않는가?
- [ ] Loading 중 중복 제출을 방지하는가?
- [ ] Backend Validation을 전제로 하는가?
```

---

### [FAQ]

Q. Form Best Practice는 뭐야?
A. label 연결, 올바른 input type, button type 명시, validation, error message, accessibility를 함께 고려하는 것이다.

Q. Form 검수에서 가장 먼저 볼 것은 뭐야?
A. label 연결, input type, button type, validation, error message를 먼저 확인한다.

Q. Backend API와 Form Field는 어떻게 맞춰?
A. input name, request body field, DTO field naming을 일관되게 맞추는 것이 좋다.

Q. Form 문서의 최종 목적은 뭐야?
A. Frontend Agent가 접근성 있는 입력 UI를 만들고 Backend API와 안정적으로 연결할 수 있게 하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. HTML Form이 뭐야?
A. 사용자 입력을 수집하고 제출하기 위한 HTML 구조다.

Q. Form은 언제 사용해?
A. 로그인, 회원가입, 검색, 댓글, 리뷰, 문의 작성처럼 사용자 입력이 필요한 UI에 사용한다.

Q. React를 써도 form 태그가 필요해?
A. 필요할 수 있다. React에서도 의미 있는 입력 구조와 submit 동작을 위해 form을 사용한다.

Q. Form은 Backend API와 연결돼?
A. 연결된다. Form 입력값은 보통 API Request Body 또는 Query Parameter로 전송된다.

Q. label은 왜 필요해?
A. 사용자가 입력 항목을 이해하고 스크린 리더가 필드를 올바르게 안내하기 위해 필요하다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 입력 예시이고 label은 입력 항목의 이름이다.

Q. label for와 input id는 왜 맞춰야 해?
A. label과 input을 명확히 연결해 클릭, focus, 스크린 리더 안내가 가능하게 하기 위해서다.

Q. React에서 label for를 그대로 써도 돼?
A. 아니다. JSX에서는 `htmlFor`를 사용한다.

Q. input은 언제 써?
A. 사용자로부터 한 줄 데이터를 입력받을 때 사용한다.

Q. input type은 왜 중요해?
A. 브라우저 기본 검증, 모바일 키보드, 접근성, 사용자 경험에 영향을 주기 때문이다.

Q. input name은 왜 필요해?
A. Form Data와 Backend API Request에서 입력 필드를 식별하기 위해 필요하다.

Q. type text는 언제 써?
A. 이름, 제목, 닉네임처럼 일반 한 줄 텍스트 입력에 사용한다.

Q. 모든 input을 type text로 써도 돼?
A. 권장하지 않는다. 입력 목적에 맞는 type을 사용하는 것이 좋다.

Q. email input은 왜 써?
A. 이메일 형식 기본 검증과 모바일 키보드 최적화에 도움이 되기 때문이다.

Q. type email만 쓰면 이메일 검증이 충분해?
A. 아니다. Frontend와 Backend Validation을 함께 사용해야 한다.

Q. password input은 왜 type password를 써?
A. 입력값을 화면에 그대로 노출하지 않고 마스킹하기 위해 사용한다.

Q. password autocomplete는 어떻게 써?
A. 로그인은 `current-password`, 새 비밀번호는 `new-password`를 사용할 수 있다.

Q. number input은 언제 써?
A. 수량, 인원 수, 나이, 금액처럼 실제 숫자 연산이나 범위 검증이 필요한 값에 사용한다.

Q. 전화번호에 type number를 써도 돼?
A. 권장하지 않는다. 전화번호는 숫자처럼 보이지만 문자열 데이터이므로 `type="tel"`이 더 적합하다.

Q. textarea는 언제 써?
A. 댓글, 리뷰, 문의 내용처럼 여러 줄 텍스트 입력이 필요할 때 사용한다.

Q. textarea도 label이 필요해?
A. 필요하다. 입력 목적을 명확히 전달하기 위해 label을 연결하는 것이 좋다.

Q. select는 언제 써?
A. 미리 정해진 선택지 중 하나를 선택해야 할 때 사용한다.

Q. option value는 왜 필요해?
A. 화면 표시 텍스트와 실제 전송 값을 분리하기 위해 필요하다.

Q. checkbox는 언제 써?
A. 복수 선택 또는 true/false 상태를 입력받을 때 사용한다.

Q. radio는 언제 써?
A. 여러 선택지 중 하나만 선택해야 할 때 사용한다.

Q. checkbox와 radio 차이는 뭐야?
A. checkbox는 복수 선택, radio는 단일 선택에 사용한다.

Q. radio 그룹에서 name은 왜 같아야 해?
A. 같은 name을 가진 radio들이 하나의 선택 그룹으로 동작하기 때문이다.

Q. fieldset은 언제 써?
A. 관련 있는 Form 입력들을 하나의 그룹으로 묶을 때 사용한다.

Q. legend는 왜 필요해?
A. fieldset 그룹의 제목을 제공해 사용자가 입력 그룹의 목적을 이해하게 한다.

Q. Form 안의 button type을 꼭 써야 해?
A. 명시하는 것이 좋다. 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있다.

Q. 제출 버튼은 어떤 type을 써?
A. `type="submit"`을 사용한다.

Q. 취소 버튼은 어떤 type을 써?
A. Form 내부에서는 `type="button"`을 사용하는 것이 안전하다.

Q. Form Validation이 뭐야?
A. 사용자 입력값이 요구사항을 만족하는지 확인하는 과정이다.

Q. Frontend Validation만 있으면 충분해?
A. 아니다. Backend Validation도 반드시 필요하다.

Q. required는 무엇을 해?
A. 필수 입력 필드임을 브라우저에 알려준다.

Q. 좋은 에러 메시지는 뭐야?
A. 무엇이 잘못됐고 어떻게 수정해야 하는지 구체적으로 알려주는 메시지다.

Q. 색상만으로 에러를 표시해도 돼?
A. 안 된다. 텍스트나 아이콘 등 다른 정보도 함께 제공해야 한다.

Q. aria-describedby는 언제 써?
A. 입력 필드와 도움말 또는 에러 메시지를 연결할 때 사용한다.

Q. Form Accessibility에서 가장 중요한 것은 뭐야?
A. label 연결, keyboard 접근, error message, focus style, fieldset/legend 구조다.

Q. aria-invalid는 언제 써?
A. 입력 필드가 오류 상태임을 보조 기술에 전달할 때 사용할 수 있다.

Q. React Form에서 onSubmit은 왜 써?
A. Form 제출 이벤트를 한 곳에서 처리하기 위해 사용한다.

Q. Controlled Component가 뭐야?
A. input value를 React State로 관리하는 입력 컴포넌트 방식이다.

Q. disabled와 readonly 차이는 뭐야?
A. disabled는 비활성 상태로 제출에서 제외될 수 있고 readonly는 읽기 전용이지만 값은 유지된다.

Q. 제출해야 하는 값을 disabled로 둬도 돼?
A. 주의해야 한다. disabled 값은 제출에서 제외될 수 있으므로 readonly를 검토한다.

Q. Form에서 가장 흔한 실수는 뭐야?
A. label 누락, button type 누락, input type 오용, error message 부족이 흔하다.

Q. 취소 버튼이 제출되는 이유는 뭐야?
A. Form 내부 button의 기본 동작이 submit일 수 있기 때문이다.

Q. 전화번호 앞자리 0이 사라지는 이유는 뭐야?
A. 전화번호를 number로 처리했기 때문일 수 있다. 전화번호는 문자열로 다루는 것이 좋다.

Q. Form 오류는 어떻게 디버깅해?
A. label 연결, input type, name/value, button type, validation, API payload 순서로 확인한다.

Q. Form Best Practice는 뭐야?
A. label 연결, 올바른 input type, button type 명시, validation, error message, accessibility를 함께 고려하는 것이다.

Q. Backend API와 Form Field는 어떻게 맞춰?
A. input name, request body field, DTO field naming을 일관되게 맞추는 것이 좋다.

Q. Form 문서의 최종 목적은 뭐야?
A. Frontend Agent가 접근성 있는 입력 UI를 만들고 Backend API와 안정적으로 연결할 수 있게 하는 것이다.
