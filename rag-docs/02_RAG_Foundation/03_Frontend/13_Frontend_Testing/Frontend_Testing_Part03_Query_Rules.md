# Frontend Testing Part03 - Query Rules

---

# 1. Query Rules Overview

## 1.1 Query Definition

### [개념]

Query는 React Testing Library에서 렌더링된 화면 안의 요소를 찾는 방법이다.

Frontend Testing에서 Query는 사용자가 화면 요소를 인식하는 방식과 가까울수록 우선순위가 높다.

---

### [핵심]

- Query Rules
- React Testing Library Query
- screen query
- Accessible Query
- getByRole
- getByLabelText
- getByPlaceholderText
- getByText
- getByDisplayValue
- getByAltText
- getByTitle
- getByTestId
- findBy
- queryBy
- waitFor
- User-visible Element

---

### [실무]

2026 실무 기준에서 Query 선택은 테스트 품질과 접근성 품질을 동시에 결정한다.

좋은 Query는 아래 조건을 만족한다.

```text
사용자가 인식할 수 있는 요소를 찾음
→ 접근성 기준과 연결됨
→ 구현 세부사항 의존이 낮음
→ 테스트 실패 원인이 명확함
```

권장 흐름:

```text
screen.getByRole
→ screen.getByLabelText
→ screen.getByPlaceholderText
→ screen.getByText
→ screen.getByDisplayValue
→ screen.getByAltText
→ screen.getByTitle
→ screen.getByTestId
```

---

### [FAQ]

Q. Query는 뭐야?
A. 테스트 화면에서 버튼, 입력창, 제목, 메시지 같은 요소를 찾는 방법이다.

Q. Query 선택이 왜 중요해?
A. 사용자 관점 테스트, 접근성 품질, 테스트 유지보수성에 직접 영향을 주기 때문이다.

Q. 어떤 Query가 가장 좋아?
A. 대부분의 경우 `getByRole`이 가장 우선이다.

---

## 1.2 Query Priority

### [개념]

Query Priority는 요소를 찾을 때 어떤 Query를 우선 사용할지 정하는 기준이다.

React Testing Library는 사용자가 인식할 수 있는 방식과 가까운 Query를 우선 사용하도록 권장한다.

---

### [핵심]

Query 우선순위:

1. `getByRole`
2. `getByLabelText`
3. `getByPlaceholderText`
4. `getByText`
5. `getByDisplayValue`
6. `getByAltText`
7. `getByTitle`
8. `getByTestId`

---

### [실무]

권장 예:

```tsx
screen.getByRole("button", { name: "검색" });
screen.getByRole("heading", { name: "축제 목록" });
screen.getByLabelText("이메일");
screen.getByText("검색 결과가 없습니다.");
```

최후 수단 예:

```tsx
screen.getByTestId("festival-card");
```

Query 선택 기준:

```text
사용자가 역할로 인식 가능한가?
→ getByRole

label이 연결된 form 요소인가?
→ getByLabelText

placeholder가 유일한 식별자인가?
→ getByPlaceholderText

화면 텍스트를 검증하는가?
→ getByText

사용자 인식 query로 찾기 어려운가?
→ getByTestId 최후 사용
```

---

### [FAQ]

Q. Query Priority는 왜 필요해?
A. Agent가 무분별하게 testId나 DOM 구조에 의존하지 않고 사용자 관점 Query를 선택하게 하기 위해 필요하다.

Q. getByRole을 먼저 쓰는 이유는 뭐야?
A. role과 accessible name을 기준으로 찾기 때문에 실제 사용자와 보조기술 관점에 가장 가깝다.

Q. getByTestId는 쓰면 안 돼?
A. 쓸 수 있지만 role, label, text로 찾기 어려운 경우의 최후 수단으로 사용한다.

---

# 2. getByRole Rules

## 2.1 getByRole Definition

### [개념]

`getByRole`은 요소의 ARIA role과 accessible name을 기준으로 요소를 찾는 Query다.

React Testing Library에서 가장 우선적으로 고려해야 하는 Query다.

---

### [핵심]

- getByRole
- ARIA role
- accessible name
- button
- heading
- link
- textbox
- checkbox
- radio
- combobox
- dialog
- alert
- status
- navigation
- semantic HTML
- accessibility

---

### [실무]

기본 예:

```tsx
screen.getByRole("button", { name: "로그인" });
screen.getByRole("heading", { name: "축제 목록" });
screen.getByRole("link", { name: "상세 보기" });
screen.getByRole("dialog", { name: "공지사항" });
```

좋은 Component 구조:

```tsx
<button type="submit">로그인</button>
<h1>축제 목록</h1>
<a href="/festivals/1">상세 보기</a>
```

Icon Button 예:

```tsx
<button aria-label="검색">
  <SearchIcon />
</button>
```

테스트:

```tsx
screen.getByRole("button", { name: "검색" });
```

권장:

- button, heading, link, dialog는 getByRole 우선
- accessible name을 함께 지정
- icon button에는 aria-label 제공
- getByRole 실패 시 Component 접근성 확인
- 의미 없는 div button 지양

---

### [FAQ]

Q. getByRole은 뭐야?
A. 요소의 역할과 접근 가능한 이름을 기준으로 요소를 찾는 Query다.

Q. accessible name은 뭐야?
A. 사용자가 보조기술로 인식하는 요소의 이름이다. 버튼 텍스트, label, aria-label 등이 될 수 있다.

Q. getByRole이 실패하면 어떻게 해?
A. semantic HTML, role, accessible name, aria-label 누락 여부를 확인한다.

---

## 2.2 Common Role Query Examples

### [개념]

Common Role Query는 자주 사용하는 HTML 요소를 role 기준으로 찾는 패턴이다.

Agent는 가능한 한 역할과 이름을 함께 사용해 테스트 의도를 명확히 해야 한다.

---

### [핵심]

자주 쓰는 role:

- button
- heading
- link
- textbox
- checkbox
- radio
- combobox
- option
- dialog
- alert
- status
- list
- listitem
- navigation
- form
- table
- row
- cell

---

### [실무]

예:

```tsx
screen.getByRole("button", { name: "저장" });
screen.getByRole("heading", { name: "마이페이지" });
screen.getByRole("link", { name: "홈으로 이동" });
screen.getByRole("textbox", { name: "검색어" });
screen.getByRole("checkbox", { name: "약관 동의" });
screen.getByRole("combobox", { name: "지역 선택" });
screen.getByRole("alert");
screen.getByRole("status");
```

Form 예:

```tsx
<label htmlFor="keyword">검색어</label>
<input id="keyword" />

screen.getByRole("textbox", { name: "검색어" });
```

주의:

```text
input type="password"
→ role로 찾기 어려울 수 있음
→ getByLabelText 사용 권장
```

---

### [FAQ]

Q. input은 getByRole로 찾을 수 있어?
A. text input은 `textbox` role로 찾을 수 있다. 단 password input은 getByLabelText가 더 안전하다.

Q. loading spinner는 어떤 role로 찾으면 좋아?
A. 사용자에게 로딩 상태를 알리는 경우 `status` role을 사용할 수 있다.

Q. error message는 어떤 role이 좋아?
A. 중요한 오류 메시지는 `alert` role로 찾을 수 있다.

---

## 2.3 getByRole Troubleshooting

### [개념]

`getByRole` 실패는 테스트 문제일 수도 있지만 Component의 접근성 문제가 드러난 것일 수 있다.

role, accessible name, semantic HTML 구조를 함께 확인해야 한다.

---

### [핵심]

실패 원인:

- semantic HTML 누락
- accessible name 없음
- button 텍스트 없음
- aria-label 없음
- label 연결 누락
- role 오해
- 요소가 비동기로 렌더링됨
- 조건부 렌더링 조건 미충족
- Provider 누락
- mock data 누락

---

### [실무]

Debug Flow:

```text
getByRole 실패
→ screen.debug 확인
→ 요소가 실제 DOM에 있는지 확인
→ role이 맞는지 확인
→ accessible name 확인
→ 비동기 렌더링이면 findByRole 사용
→ 조건부 렌더링 조건 확인
→ Provider / mock 확인
```

나쁜 Component:

```tsx
<div onClick={onSubmit}>저장</div>
```

좋은 Component:

```tsx
<button type="button" onClick={onSubmit}>
  저장
</button>
```

비동기 UI:

```tsx
expect(
  await screen.findByRole("heading", { name: "축제 목록" }),
).toBeInTheDocument();
```

---

### [FAQ]

Q. getByRole이 실패하면 무조건 테스트가 잘못된 거야?
A. 아니다. Component의 semantic HTML이나 accessible name이 부족한 접근성 문제일 수 있다.

Q. 화면에는 버튼이 보이는데 getByRole이 못 찾아.
A. 실제 button 요소가 아니거나 accessible name이 없을 수 있다.

Q. 비동기로 나타나는 버튼은 어떻게 찾아?
A. `await screen.findByRole("button", { name: "..." })`를 사용한다.

---

# 3. getByLabelText Rules

## 3.1 getByLabelText Definition

### [개념]

`getByLabelText`는 label과 연결된 Form 요소를 찾는 Query다.

Form input, textarea, select, password input 테스트에서 자주 사용한다.

---

### [핵심]

- getByLabelText
- label
- htmlFor
- input id
- aria-label
- aria-labelledby
- form accessibility
- email input
- password input
- textarea
- select
- checkbox
- radio

---

### [실무]

기본 예:

```tsx
<label htmlFor="email">이메일</label>
<input id="email" type="email" />

screen.getByLabelText("이메일");
```

password input 예:

```tsx
<label htmlFor="password">비밀번호</label>
<input id="password" type="password" />

screen.getByLabelText("비밀번호");
```

테스트 예:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");
await user.type(screen.getByLabelText("비밀번호"), "password123");
```

권장:

- Form 요소는 label 연결
- password input은 getByLabelText 우선
- label 없는 input 발견 시 Component 개선
- placeholder를 label 대체용으로 사용하지 않음

---

### [FAQ]

Q. getByLabelText는 언제 써?
A. label이 있는 input, textarea, select, checkbox, radio 같은 Form 요소를 찾을 때 사용한다.

Q. password input은 getByRole로 못 찾아?
A. role로 찾기 어려울 수 있어 getByLabelText가 더 안전하다.

Q. label 없는 input은 어떻게 해야 해?
A. 테스트에서 testId를 쓰기보다 Component에 label 또는 aria-label을 추가하는 것이 좋다.

---

## 3.2 Label Connection Rules

### [개념]

Label Connection은 label과 form control이 명확히 연결된 상태를 의미한다.

Label 연결이 잘 되어 있으면 접근성과 테스트 품질이 모두 좋아진다.

---

### [핵심]

Label 연결 방식:

- `<label htmlFor="id">`
- `<input id="id">`
- wrapping label
- aria-label
- aria-labelledby
- visible label
- accessible form
- testable form

---

### [실무]

권장 방식:

```tsx
<label htmlFor="reviewContent">리뷰 내용</label>
<textarea id="reviewContent" />
```

테스트:

```tsx
screen.getByLabelText("리뷰 내용");
```

Wrapping label:

```tsx
<label>
  약관 동의
  <input type="checkbox" />
</label>
```

테스트:

```tsx
screen.getByLabelText("약관 동의");
```

Icon-only input 또는 숨김 label이 필요한 경우:

```tsx
<input aria-label="검색어" />
```

권장:

- 사용자에게 보이는 label 우선
- aria-label은 시각 label이 어려운 경우 사용
- placeholder만으로 label 대체 지양
- Form 테스트는 label 기반 query 우선

---

### [FAQ]

Q. placeholder만 있으면 label 없이 괜찮아?
A. 권장하지 않는다. placeholder는 입력 후 사라질 수 있고 접근성 label을 대체하기 어렵다.

Q. aria-label을 써도 getByLabelText로 찾을 수 있어?
A. 가능하다. 다만 가능한 경우 시각적으로 보이는 label이 더 좋다.

Q. label 연결이 테스트에 왜 중요해?
A. 사용자가 입력창의 의미를 이해할 수 있고 테스트도 사용자 관점으로 작성할 수 있기 때문이다.

---

# 4. getByText Rules

## 4.1 getByText Definition

### [개념]

`getByText`는 화면에 표시된 텍스트를 기준으로 요소를 찾는 Query다.

메시지, 설명, EmptyState, ErrorState, SuccessState, 일반 텍스트 검증에 사용한다.

---

### [핵심]

- getByText
- visible text
- message
- description
- error message
- success message
- empty message
- static text
- text content
- fragmented text caution

---

### [실무]

사용 예:

```tsx
screen.getByText("검색 결과가 없습니다.");
screen.getByText("저장되었습니다.");
screen.getByText("서버 오류가 발생했습니다.");
```

비동기 메시지:

```tsx
expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

권장:

- 사용자에게 보이는 메시지 검증
- Error / Empty / Success 메시지에 적합
- button, heading, link는 getByRole 우선
- form input은 getByLabelText 우선

주의:

```text
텍스트가 여러 요소로 나뉘면 getByText가 실패할 수 있음
번역 문구가 자주 바뀌면 테스트가 취약할 수 있음
```

---

### [FAQ]

Q. getByText는 언제 써?
A. 일반 메시지, 설명, EmptyState, ErrorState, SuccessState 같은 화면 텍스트를 검증할 때 사용한다.

Q. 버튼도 getByText로 찾으면 안 돼?
A. 가능하지만 버튼은 `getByRole("button", { name: "..." })`이 더 권장된다.

Q. 텍스트가 화면에 보이는데 getByText가 실패해.
A. 텍스트가 여러 요소로 나뉘었거나 비동기로 렌더링되었을 수 있다.

---

## 4.2 Text Matching Caution

### [개념]

Text Matching Caution은 텍스트 기반 Query가 문구 변경, 공백, 요소 분할, 다국어 처리에 취약할 수 있음을 주의하는 규칙이다.

---

### [핵심]

주의 대상:

- split text
- whitespace
- dynamic text
- i18n translation
- punctuation
- duplicated text
- partial match
- regex match
- exact option
- async rendering

---

### [실무]

정확한 문구:

```tsx
screen.getByText("검색 결과가 없습니다.");
```

정규식 활용:

```tsx
screen.getByText(/검색 결과가 없습니다/);
```

중복 텍스트가 있는 경우:

```tsx
screen.getAllByText("삭제");
```

더 좋은 대안:

```tsx
screen.getByRole("button", { name: "삭제" });
```

문구 변경이 잦은 경우:

```text
사용자에게 중요한 메시지
→ 문구 테스트 가능

문구가 자주 변경되는 내부 설명
→ role / 상태 / aria 기반 검증 고려
```

---

### [FAQ]

Q. getByText에 정규식을 써도 돼?
A. 가능하다. 공백이나 일부 문구 변경에 덜 취약하게 만들 수 있다.

Q. 같은 텍스트가 여러 개면 어떻게 해?
A. getAllByText를 사용하거나 더 명확한 role, name, within을 사용한다.

Q. 다국어 프로젝트에서 텍스트 테스트는 위험해?
A. 문구 변경에 취약할 수 있다. 핵심 사용자 메시지는 테스트하고 나머지는 더 안정적인 Query를 고려한다.

---

# 5. Placeholder, DisplayValue, AltText, Title Rules

## 5.1 getByPlaceholderText Rules

### [개념]

`getByPlaceholderText`는 input이나 textarea의 placeholder 값을 기준으로 요소를 찾는 Query다.

Label이 없는 입력 요소를 찾을 수 있지만 label 기반 Query보다 우선순위는 낮다.

---

### [핵심]

- getByPlaceholderText
- placeholder
- input
- textarea
- search input
- fallback query
- label preferred
- accessibility caution

---

### [실무]

예:

```tsx
screen.getByPlaceholderText("검색어를 입력하세요");
```

권장보다 낮은 우선순위:

```tsx
screen.getByLabelText("검색어");
```

주의:

```text
placeholder는 label이 아님
placeholder는 입력 후 사라질 수 있음
접근성 이름으로 항상 충분하지 않음
Form 테스트는 label 우선
```

사용 가능 상황:

```text
검색창이 placeholder 중심 UI로 설계됨
시각적 label이 별도로 없음
기존 코드 수정이 어려움
```

---

### [FAQ]

Q. getByPlaceholderText는 언제 써?
A. placeholder가 사용자가 입력창을 식별하는 주요 단서일 때 사용한다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. Form 요소에는 label이나 aria-label을 제공하는 것이 좋다.

Q. Form 테스트에서 가장 좋은 Query는 뭐야?
A. 대부분 `getByLabelText`가 좋다.

---

## 5.2 getByDisplayValue Rules

### [개념]

`getByDisplayValue`는 input, textarea, select에 현재 표시된 값을 기준으로 요소를 찾는 Query다.

사용자 입력 후 값이 반영되었는지 검증할 때 사용할 수 있다.

---

### [핵심]

- getByDisplayValue
- input value
- textarea value
- select value
- controlled component
- form state
- user input result
- displayed value

---

### [실무]

예:

```tsx
await user.type(screen.getByLabelText("검색어"), "축제");

expect(screen.getByDisplayValue("축제")).toBeInTheDocument();
```

Controlled Component 테스트:

```tsx
render(<SearchInput value="봄꽃" onChange={vi.fn()} />);

expect(screen.getByDisplayValue("봄꽃")).toBeInTheDocument();
```

권장:

- 입력값 반영 검증
- controlled input 초기값 검증
- Form 수정 화면 초기 데이터 검증
- Form submit 값 검증은 callback 또는 UI 결과와 함께 확인

---

### [FAQ]

Q. getByDisplayValue는 언제 써?
A. input, textarea, select에 표시된 현재 값을 검증할 때 사용한다.

Q. 입력 후 값 확인은 어떻게 해?
A. userEvent로 입력한 뒤 `getByDisplayValue` 또는 `toHaveValue`로 검증한다.

Q. getByDisplayValue와 toHaveValue 차이는?
A. getByDisplayValue는 값으로 요소를 찾고, toHaveValue는 찾은 요소의 값을 검증한다.

---

## 5.3 getByAltText Rules

### [개념]

`getByAltText`는 이미지의 alt text를 기준으로 요소를 찾는 Query다.

사용자에게 의미 있는 이미지는 적절한 alt text를 가져야 한다.

---

### [핵심]

- getByAltText
- image
- img
- alt
- accessible image
- decorative image
- meaningful image
- thumbnail
- profile image
- festival image

---

### [실무]

예:

```tsx
<img src="/festival.jpg" alt="봄꽃 축제 대표 이미지" />;

screen.getByAltText("봄꽃 축제 대표 이미지");
```

권장:

- 의미 있는 이미지는 alt 제공
- 축제 이미지, 프로필 이미지, 상품 이미지는 alt 검토
- 장식용 이미지는 빈 alt 사용 가능
- alt text도 사용자 관점 문구로 작성

장식용 이미지:

```tsx
<img src="/decoration.svg" alt="" />
```

---

### [FAQ]

Q. getByAltText는 언제 써?
A. 의미 있는 이미지가 올바른 alt text를 갖는지 검증할 때 사용한다.

Q. 장식용 이미지에도 alt가 필요해?
A. 장식용 이미지는 `alt=""`로 보조기술에서 무시되도록 할 수 있다.

Q. 이미지 테스트는 꼭 해야 해?
A. 사용자에게 의미 있는 이미지라면 alt text 검증이 유용하다.

---

## 5.4 getByTitle Rules

### [개념]

`getByTitle`은 title 속성을 기준으로 요소를 찾는 Query다.

일반적으로 우선순위가 낮으며 role, label, text, alt로 찾기 어려운 경우에 제한적으로 사용한다.

---

### [핵심]

- getByTitle
- title attribute
- low priority query
- tooltip title
- fallback query
- user-visible caution
- accessibility caution

---

### [실무]

예:

```tsx
<span title="도움말">?</span>;

screen.getByTitle("도움말");
```

주의:

```text
title 속성은 모바일 / 키보드 / 스크린리더 환경에서 일관적이지 않을 수 있음
사용자 인식 query로 보기 어려울 수 있음
가능하면 role / label / text 우선
```

사용 가능 상황:

```text
외부 라이브러리 Component가 title만 제공함
간단한 tooltip title 확인
대체 query가 없음
```

---

### [FAQ]

Q. getByTitle은 언제 써?
A. title 속성으로만 식별 가능한 요소를 찾을 때 제한적으로 사용한다.

Q. title은 접근성에 좋은 방식이야?
A. 항상 그렇지는 않다. 가능한 경우 명시적인 label이나 visible text를 사용하는 것이 좋다.

Q. getByTitle보다 좋은 Query는 뭐야?
A. role, label, text, alt 기반 Query가 더 우선이다.

---

# 6. getByTestId Rules

## 6.1 getByTestId Definition

### [개념]

`getByTestId`는 `data-testid` 속성을 기준으로 요소를 찾는 Query다.

사용자가 인식하는 정보가 아니라 테스트용 식별자를 사용하므로 Query Priority에서 가장 낮은 우선순위다.

---

### [핵심]

- getByTestId
- data-testid
- fallback query
- last resort
- implementation detail caution
- non-user-visible selector
- stable selector
- avoid overuse

---

### [실무]

사용 예:

```tsx
<div data-testid="festival-card">봄꽃 축제</div>;

screen.getByTestId("festival-card");
```

사용 가능한 경우:

```text
시각적으로 구분되지 않는 wrapper 검증
외부 라이브러리로 role 설정이 어려움
canvas / chart / virtualized list
동일한 텍스트가 매우 많고 다른 접근성 query가 어려움
```

지양해야 하는 경우:

```tsx
screen.getByTestId("login-button");
```

대체 권장:

```tsx
screen.getByRole("button", { name: "로그인" });
```

---

### [FAQ]

Q. getByTestId는 왜 우선순위가 낮아?
A. 사용자가 인식할 수 없는 테스트 전용 속성이므로 사용자 관점 테스트와 거리가 있기 때문이다.

Q. data-testid는 절대 쓰면 안 돼?
A. 아니다. 사용자 관점 Query로 찾기 어려운 경우 최후 수단으로 사용할 수 있다.

Q. 버튼에 data-testid를 붙여서 찾으면 안 돼?
A. 가능하지만 `getByRole("button", { name: "..." })`이 더 권장된다.

---

## 6.2 TestId Naming Rules

### [개념]

TestId Naming Rules는 `data-testid`를 사용할 때 안정적이고 의미 있는 이름을 작성하는 기준이다.

TestId는 최후 수단이므로 남용하지 않고 명확한 이름을 사용한다.

---

### [핵심]

Naming 기준:

- kebab-case 권장
- domain 의미 포함
- component 의미 포함
- index 의존 지양
- style 이름 지양
- 내부 구현명 지양
- 변경 가능성 낮은 이름
- 사용자 도메인 기준 이름

---

### [실무]

좋은 예:

```tsx
data-testid="festival-card"
data-testid="review-list"
data-testid="notification-badge"
data-testid="price-chart"
```

나쁜 예:

```tsx
data-testid="div1"
data-testid="blue-box"
data-testid="state-wrapper"
data-testid="handle-click-target"
```

권장:

```text
테스트 대상의 도메인 의미를 드러냄
스타일이나 내부 함수 이름에 의존하지 않음
리팩토링 후에도 유지 가능한 이름 사용
```

---

### [FAQ]

Q. data-testid 이름은 어떻게 지어?
A. `festival-card`, `review-list`처럼 도메인 의미가 드러나는 kebab-case 이름이 좋다.

Q. className과 같은 이름을 써도 돼?
A. 권장하지 않는다. 스타일 변경에 테스트가 영향받을 수 있다.

Q. index 기반 testId는 괜찮아?
A. 목록 순서가 바뀌면 깨질 수 있어 지양한다.

---

# 7. getBy / findBy / queryBy Rules

## 7.1 Query Family Definition

### [개념]

`getBy`, `findBy`, `queryBy`는 요소 존재 여부와 비동기 렌더링 여부에 따라 선택하는 Query 계열이다.

올바른 Query Family 선택은 테스트 안정성에 중요하다.

---

### [핵심]

| Query   | 사용 상황        | 실패 시          |
| ------- | ---------------- | ---------------- |
| getBy   | 즉시 존재해야 함 | 없으면 throw     |
| findBy  | 비동기로 나타남  | timeout 후 throw |
| queryBy | 없어야 함을 확인 | 없으면 null      |

---

### [실무]

즉시 존재:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

비동기 등장:

```tsx
expect(await screen.findByText("조회 성공")).toBeInTheDocument();
```

존재하지 않음:

```tsx
expect(screen.queryByText("에러")).not.toBeInTheDocument();
```

선택 기준:

```text
처음부터 있어야 함
→ getBy

API 응답 후 나타남
→ findBy

없어야 함
→ queryBy
```

---

### [FAQ]

Q. getBy와 findBy 차이는 뭐야?
A. getBy는 즉시 존재하는 요소를 찾고, findBy는 비동기로 나중에 나타나는 요소를 기다린다.

Q. queryBy는 언제 써?
A. 요소가 없어야 하는 것을 검증할 때 사용한다.

Q. 없는 요소를 getBy로 확인하면 어떻게 돼?
A. getBy는 요소가 없으면 throw하므로 absence 테스트에는 적합하지 않다.

---

## 7.2 getBy Rules

### [개념]

`getBy`는 요소가 현재 DOM에 즉시 존재해야 할 때 사용하는 Query다.

요소가 없으면 테스트를 즉시 실패시킨다.

---

### [핵심]

- getBy
- immediate element
- synchronous query
- throw on missing
- required UI
- initial render
- static element
- visible control

---

### [실무]

사용 예:

```tsx
render(<LoginForm />);

expect(screen.getByLabelText("이메일")).toBeInTheDocument();
expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
expect(screen.getByRole("button", { name: "로그인" })).toBeInTheDocument();
```

적합한 상황:

```text
초기 렌더링에 바로 있어야 하는 Form 요소
항상 표시되어야 하는 버튼
정적 제목
필수 UI
```

주의:

```text
API 응답 후 나타나는 요소
→ findBy 사용

없어야 하는 요소
→ queryBy 사용
```

---

### [FAQ]

Q. getBy는 언제 써?
A. 요소가 초기 렌더링 직후 즉시 존재해야 할 때 사용한다.

Q. getBy가 실패하면 무슨 의미야?
A. 요소가 현재 DOM에 없거나 Query 조건이 맞지 않는다는 의미다.

Q. 비동기 데이터에는 getBy를 쓰면 안 돼?
A. 응답 후 나타나는 요소라면 findBy를 사용해야 한다.

---

## 7.3 findBy Rules

### [개념]

`findBy`는 요소가 비동기로 나타날 때 사용하는 Query다.

API 응답, mutation 결과, auth 초기화, route 전환 후 UI가 나타나는 경우에 사용한다.

---

### [핵심]

- findBy
- async query
- await required
- API response
- mutation success
- mutation error
- delayed rendering
- loading to success
- route result
- auth initialization

---

### [실무]

사용 예:

```tsx
render(<FestivalListPage />);

expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
```

Form submit 후 성공 메시지:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

권장:

- `await` 필수
- API 응답 후 UI 검증에 사용
- loading 이후 success / error 화면 검증에 사용
- findBy로 충분하면 waitFor보다 findBy 우선

주의:

```tsx
screen.findByText("저장되었습니다.");
```

위 코드는 await가 없어 잘못된 테스트가 될 수 있다.

---

### [FAQ]

Q. findBy는 언제 써?
A. API 응답이나 상태 업데이트 후 요소가 나중에 나타날 때 사용한다.

Q. findBy에는 await가 필요해?
A. 필요하다. findBy는 Promise를 반환한다.

Q. findBy와 waitFor 중 뭐가 더 좋아?
A. 특정 요소가 나타나는 것을 기다릴 때는 findBy가 더 간단하고 명확하다.

---

## 7.4 queryBy Rules

### [개념]

`queryBy`는 요소가 없어야 하는 상황을 검증할 때 사용하는 Query다.

요소가 없어도 throw하지 않고 null을 반환한다.

---

### [핵심]

- queryBy
- absence check
- null result
- not in document
- removed element
- hidden caution
- conditional UI
- no error message
- no loading state

---

### [실무]

사용 예:

```tsx
expect(screen.queryByText("에러")).not.toBeInTheDocument();
```

Modal 닫힘 검증:

```tsx
await user.click(screen.getByRole("button", { name: "닫기" }));

expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
```

Error 없음 검증:

```tsx
expect(screen.queryByRole("alert")).not.toBeInTheDocument();
```

주의:

```text
getBy로 absence 검증 금지
queryBy는 요소 없음 확인용
비동기로 사라지는 요소는 waitFor 또는 waitForElementToBeRemoved 고려
```

---

### [FAQ]

Q. queryBy는 언제 써?
A. 특정 요소가 없어야 하는 것을 검증할 때 사용한다.

Q. getBy로 not.toBeInTheDocument를 쓰면 안 돼?
A. getBy는 요소가 없으면 먼저 throw하므로 absence 검증에 적합하지 않다.

Q. Modal 닫힘 테스트는 뭘 써?
A. 닫기 후 `queryByRole("dialog")`가 없는지 확인한다.

---

# 8. getAllBy / findAllBy / queryAllBy Rules

## 8.1 Multiple Elements Query

### [개념]

`getAllBy`, `findAllBy`, `queryAllBy`는 같은 조건에 맞는 여러 요소를 찾을 때 사용하는 Query 계열이다.

목록, 카드, 테이블 행, 반복 버튼 검증에 사용한다.

---

### [핵심]

- getAllBy
- findAllBy
- queryAllBy
- multiple elements
- list items
- cards
- table rows
- repeated buttons
- collection assertion
- array result

---

### [실무]

목록 검증:

```tsx
const items = screen.getAllByRole("listitem");

expect(items).toHaveLength(3);
```

비동기 목록:

```tsx
const cards = await screen.findAllByTestId("festival-card");

expect(cards).toHaveLength(5);
```

반복 버튼:

```tsx
const deleteButtons = screen.getAllByRole("button", { name: "삭제" });

expect(deleteButtons).toHaveLength(3);
```

권장:

- 가능하면 list / listitem / table role 활용
- 단순 개수보다 핵심 항목 표시도 함께 확인
- 중복 텍스트가 많은 경우 within 사용 고려

---

### [FAQ]

Q. 같은 버튼이 여러 개 있으면 어떻게 찾아?
A. `getAllByRole("button", { name: "삭제" })`처럼 AllBy 계열을 사용한다.

Q. 목록 개수는 어떻게 테스트해?
A. listitem, row, card testId 등을 배열로 가져와 length를 검증한다.

Q. getAllBy와 queryAllBy 차이는 뭐야?
A. getAllBy는 없으면 throw하고 queryAllBy는 없으면 빈 배열을 반환한다.

---

## 8.2 within Rules

### [개념]

`within`은 특정 요소 내부로 Query 범위를 제한하는 유틸리티다.

목록, 카드, 테이블처럼 반복 UI 안에서 특정 항목의 하위 요소를 찾을 때 사용한다.

---

### [핵심]

- within
- scoped query
- card query
- row query
- list item query
- table row
- duplicated text
- nested element
- precise assertion

---

### [실무]

카드 내부 버튼 찾기:

```tsx
const festivalCard = screen.getByText("봄꽃 축제").closest("article");

expect(
  within(festivalCard!).getByRole("button", { name: "찜하기" }),
).toBeInTheDocument();
```

더 좋은 구조:

```tsx
<article aria-label="봄꽃 축제">
  <h2>봄꽃 축제</h2>
  <button>찜하기</button>
</article>
```

테스트:

```tsx
const card = screen.getByRole("article", { name: "봄꽃 축제" });

expect(
  within(card).getByRole("button", { name: "찜하기" }),
).toBeInTheDocument();
```

권장:

- 중복 텍스트가 많은 UI에서 사용
- 카드 / row / section 단위로 범위 제한
- closest 남용보다 semantic wrapper 권장
- within 내부에서도 Query Priority 적용

---

### [FAQ]

Q. within은 언제 써?
A. 반복 카드나 테이블 행 안에서 특정 요소를 정확히 찾고 싶을 때 사용한다.

Q. 같은 이름의 버튼이 여러 개면 어떻게 구분해?
A. 특정 카드나 행을 먼저 찾고 within으로 그 내부 버튼을 찾는다.

Q. within도 getByRole을 우선 써?
A. 그렇다. 범위만 제한될 뿐 Query Priority는 동일하게 적용한다.

---

# 9. waitFor Rules

## 9.1 waitFor Definition

### [개념]

`waitFor`는 특정 assertion이 통과할 때까지 기다리는 비동기 테스트 유틸리티다.

화면 요소 등장에는 `findBy`를 우선 사용하고, callback 호출이나 복잡한 조건에는 `waitFor`를 사용할 수 있다.

---

### [핵심]

- waitFor
- async assertion
- callback verification
- delayed state
- mock function called
- debounce
- timer
- mutation callback
- retry assertion
- avoid overuse

---

### [실무]

callback 호출 검증:

```tsx
await waitFor(() => {
  expect(onSubmit).toHaveBeenCalledTimes(1);
});
```

복잡한 조건:

```tsx
await waitFor(() => {
  expect(screen.queryByRole("status")).not.toBeInTheDocument();
});
```

권장:

```text
화면 요소 등장
→ findBy 우선

callback 호출 확인
→ waitFor 사용 가능

복잡한 상태 변화
→ waitFor 사용 가능
```

주의:

```text
waitFor 안에서 userEvent 실행 지양
waitFor 안에 너무 많은 assertion 지양
무조건 waitFor로 감싸기 금지
```

---

### [FAQ]

Q. waitFor는 언제 써?
A. callback 호출이나 복잡한 비동기 조건이 만족될 때까지 기다릴 때 사용한다.

Q. 요소가 나타나는 테스트도 waitFor를 써야 해?
A. 보통은 `findBy`가 더 간단하고 명확하다.

Q. waitFor를 남용하면 왜 안 좋아?
A. 테스트가 느려지고 실패 원인이 불명확해질 수 있다.

---

## 9.2 waitFor Anti Pattern

### [개념]

waitFor Anti Pattern은 비동기 문제를 해결하기 위해 waitFor를 무분별하게 사용하는 잘못된 패턴이다.

waitFor는 필요한 assertion을 기다리는 용도로 제한해야 한다.

---

### [핵심]

Anti Pattern:

- waitFor 안에서 userEvent 실행
- 모든 assertion을 waitFor로 감쌈
- 여러 assertion을 한 waitFor에 과도하게 포함
- getBy 실패를 숨기기 위해 waitFor 사용
- 고정 시간 대기 대체로 오해
- mock 설정 누락을 waitFor로 해결하려 함

---

### [실무]

나쁜 예:

```tsx
await waitFor(() => {
  user.click(screen.getByRole("button", { name: "저장" }));
});
```

좋은 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

나쁜 예:

```tsx
await waitFor(() => {
  expect(screen.getByText("저장되었습니다.")).toBeInTheDocument();
  expect(screen.getByText("목록이 갱신되었습니다.")).toBeInTheDocument();
  expect(onSuccess).toHaveBeenCalled();
});
```

개선:

```tsx
expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
expect(screen.getByText("목록이 갱신되었습니다.")).toBeInTheDocument();
```

---

### [FAQ]

Q. waitFor 안에서 user.click을 해도 돼?
A. 지양한다. 사용자 이벤트는 waitFor 밖에서 실행하고 결과 assertion만 기다린다.

Q. 모든 expect를 waitFor로 감싸면 안정적이야?
A. 아니다. 실패 원인이 흐려지고 테스트가 느려질 수 있다.

Q. waitFor 대신 findBy를 써야 하는 경우는?
A. 화면 요소가 비동기로 나타나는 경우에는 findBy를 우선 사용한다.

---

# 10. Query Troubleshooting

## 10.1 Query Failed Troubleshooting

### [개념]

Query Failed는 테스트가 원하는 요소를 찾지 못하는 상황이다.

원인은 Query 선택 오류, 비동기 처리 누락, accessible name 문제, Provider 누락, mock data 문제일 수 있다.

---

### [핵심]

원인:

- Query Priority 미적용
- 텍스트 불일치
- accessible name 없음
- label 연결 누락
- role 오해
- 비동기 UI에 getBy 사용
- absence 테스트에 getBy 사용
- Provider 누락
- mock response 누락
- 조건부 렌더링 조건 미충족
- 중복 요소
- split text

---

### [실무]

Debug Flow:

```text
Query 실패
→ screen.debug 확인
→ 실제 DOM 존재 확인
→ 비동기 여부 확인
→ getBy / findBy / queryBy 선택 확인
→ role / accessible name 확인
→ label 연결 확인
→ Provider 확인
→ mock response 확인
→ 조건부 렌더링 조건 확인
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
expect(screen.queryByText("에러")).not.toBeInTheDocument();
```

---

### [FAQ]

Q. Query가 실패하면 뭘 먼저 확인해?
A. screen.debug로 현재 DOM을 확인하고 비동기 렌더링 여부와 Query 선택을 확인한다.

Q. getByText가 못 찾는데 화면에는 보여.
A. 텍스트가 여러 요소로 나뉘었거나 아직 렌더링되기 전일 수 있다.

Q. 같은 요소가 여러 개라 실패하면 어떻게 해?
A. getAllBy 계열이나 within으로 Query 범위를 좁힌다.

---

## 10.2 Accessible Name Troubleshooting

### [개념]

Accessible Name Troubleshooting은 role 기반 Query가 실패할 때 요소의 접근 가능한 이름을 확인하는 과정이다.

버튼 텍스트, label, aria-label, aria-labelledby 등이 accessible name에 영향을 준다.

---

### [핵심]

확인 대상:

- button text
- link text
- label text
- aria-label
- aria-labelledby
- alt text
- hidden text
- icon button
- semantic HTML
- Testing Playground

---

### [실무]

문제 예:

```tsx
<button>
  <SearchIcon />
</button>
```

테스트 실패:

```tsx
screen.getByRole("button", { name: "검색" });
```

개선:

```tsx
<button aria-label="검색">
  <SearchIcon />
</button>
```

정상 테스트:

```tsx
screen.getByRole("button", { name: "검색" });
```

Debug Flow:

```text
getByRole 실패
→ 요소 role 확인
→ accessible name 확인
→ aria-label 필요 여부 확인
→ label 연결 확인
→ Testing Playground로 Query 후보 확인
```

---

### [FAQ]

Q. accessible name은 어디서 와?
A. 버튼 텍스트, label, aria-label, aria-labelledby, alt text 등에서 계산된다.

Q. 아이콘 버튼은 왜 getByRole name으로 못 찾아?
A. 텍스트나 aria-label이 없으면 accessible name이 비어 있을 수 있다.

Q. accessible name 문제는 어떻게 고쳐?
A. 의미 있는 텍스트, label, aria-label, aria-labelledby를 제공한다.

---

# 11. Query Checklist

## 11.1 Query Selection Checklist

### [개념]

Query Selection Checklist는 테스트 작성 시 Query가 사용자 관점과 접근성 기준에 맞게 선택되었는지 검수하는 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] getByRole을 우선 검토했는가?
- [ ] button / heading / link / dialog를 role로 찾는가?
- [ ] Form 요소는 label로 찾는가?
- [ ] 비동기 UI에는 findBy를 사용하는가?
- [ ] 없어야 하는 요소는 queryBy를 사용하는가?
- [ ] getByTestId를 최후 수단으로 사용하는가?
- [ ] accessible name이 명확한가?
- [ ] icon button에 aria-label이 있는가?
- [ ] 중복 요소는 getAllBy 또는 within으로 처리했는가?
- [ ] waitFor를 남용하지 않았는가?
- [ ] Query 실패 시 Component 접근성 문제를 확인했는가?
```

---

### [실무]

Agent Query 선택 Flow:

```text
찾을 요소 확인
→ 사용자 인식 방식 확인
→ role 가능 여부 확인
→ label 가능 여부 확인
→ text 가능 여부 확인
→ 비동기 여부 확인
→ 존재 / 부재 여부 확인
→ Query Family 선택
→ testId 최후 검토
```

예:

```text
로그인 버튼
→ getByRole("button", { name: "로그인" })

이메일 입력창
→ getByLabelText("이메일")

저장 완료 메시지
→ findByText("저장되었습니다.")

닫힌 모달
→ queryByRole("dialog")
```

---

### [FAQ]

Q. Query 선택 체크리스트의 핵심은 뭐야?
A. role과 label을 우선 사용하고, 비동기에는 findBy, absence에는 queryBy를 사용하는 것이다.

Q. getByTestId 사용 전 뭘 확인해야 해?
A. role, label, text, alt 같은 사용자 인식 Query로 찾을 수 없는지 먼저 확인한다.

Q. Query 선택이 접근성과 연결되는 이유는?
A. 좋은 접근성 구조는 role, label, name 기반 Query로 쉽게 테스트할 수 있기 때문이다.

---

# 12. Part03 Summary

## 12.1 Query Rules Final Rule

### [개념]

Frontend Testing Part03은 React Testing Library Query 선택 기준을 정의한다.

이 Part의 목적은 Agent가 사용자 관점 Query를 우선 사용하고, 비동기 여부와 존재 여부에 맞는 Query Family를 선택하게 만드는 것이다.

---

### [핵심]

최종 기준:

- Query Priority 적용
- getByRole 최우선
- Form 요소는 getByLabelText 우선
- 일반 메시지는 getByText / findByText 사용
- 이미지 의미 검증은 getByAltText 사용
- getByTestId는 최후 수단
- 즉시 존재는 getBy
- 비동기 등장은 findBy
- 없어야 함은 queryBy
- 여러 요소는 AllBy 계열 사용
- 반복 UI 내부 검증은 within 사용
- waitFor는 callback / 복잡 조건에 제한 사용
- Query 실패 시 접근성 문제도 함께 확인

---

### [실무]

Agent 작업 Flow:

```text
Test Target Element
→ Select User-centered Query
→ Choose getBy / findBy / queryBy
→ Add accessible name
→ Use within if duplicated
→ Avoid testId unless necessary
→ Assert User-visible Result
→ Debug with screen.debug if failed
```

Part04 이후 연결:

```text
Part03 Query Rules
→ Part04 User Event
→ Part05 Unit Test
→ Part06 Component Test
→ Part07 Form Testing
→ Part08 API Mocking
→ Part09 Loading Error Empty
```

---

### [FAQ]

Q. Part03의 최종 목적은 뭐야?
A. Frontend Agent가 React Testing Library Query를 사용자 관점과 비동기 상황에 맞게 선택하게 만드는 것이다.

Q. Query Rules에서 가장 중요한 기준은 뭐야?
A. getByRole을 우선하고, 비동기 요소는 findBy, 없어야 하는 요소는 queryBy를 사용하는 것이다.

Q. Part03 다음에는 어떤 내용이 이어져야 해?
A. userEvent, fireEvent, 사용자 입력과 클릭 이벤트 테스트 기준이 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. React Testing Library Query는 뭐야?
A. 테스트 화면에서 버튼, 입력창, 제목, 메시지 같은 요소를 찾는 방법이다.

Q. Query Priority는 뭐야?
A. 요소를 찾을 때 사용자가 인식할 수 있는 방식과 가까운 Query를 우선 사용하는 기준이다.

Q. Query 우선순위는 어떻게 돼?
A. getByRole, getByLabelText, getByPlaceholderText, getByText, getByDisplayValue, getByAltText, getByTitle, getByTestId 순서다.

Q. getByRole은 언제 써?
A. button, heading, link, dialog, alert, status처럼 role과 accessible name으로 찾을 수 있는 요소에 우선 사용한다.

Q. getByRole을 먼저 쓰는 이유는 뭐야?
A. 사용자가 보조기술로 인식하는 역할과 이름을 기준으로 찾기 때문에 실제 사용성에 가깝다.

Q. accessible name은 뭐야?
A. 버튼 텍스트, label, aria-label, aria-labelledby, alt text 등에서 계산되는 접근 가능한 이름이다.

Q. getByRole이 실패하면 어떻게 해?
A. screen.debug로 DOM을 확인하고 semantic HTML, role, accessible name, aria-label 누락 여부를 확인한다.

Q. 아이콘 버튼은 어떻게 테스트해?
A. button에 aria-label을 제공하고 `getByRole("button", { name: "검색" })`처럼 찾는다.

Q. getByLabelText는 언제 써?
A. label이 있는 input, textarea, select, checkbox, radio 같은 Form 요소를 찾을 때 사용한다.

Q. password input은 어떤 Query가 좋아?
A. getByLabelText가 안전하다.

Q. label 없는 input은 어떻게 해야 해?
A. testId를 우선 쓰기보다 label 또는 aria-label을 추가하는 것이 좋다.

Q. placeholder를 label 대신 써도 돼?
A. 권장하지 않는다. placeholder는 입력 후 사라질 수 있고 접근성 label을 대체하기 어렵다.

Q. getByPlaceholderText는 언제 써?
A. placeholder가 사용자가 입력창을 식별하는 주요 단서일 때 제한적으로 사용한다.

Q. getByText는 언제 써?
A. 일반 메시지, 설명, EmptyState, ErrorState, SuccessState 같은 화면 텍스트를 검증할 때 사용한다.

Q. 버튼도 getByText로 찾아도 돼?
A. 가능하지만 버튼은 `getByRole("button", { name: "..." })`이 더 권장된다.

Q. getByText가 화면 텍스트를 못 찾는 이유는 뭐야?
A. 텍스트가 여러 요소로 나뉘었거나 비동기로 렌더링되었거나 문구가 정확히 일치하지 않을 수 있다.

Q. getByDisplayValue는 언제 써?
A. input, textarea, select에 표시된 현재 값을 검증할 때 사용한다.

Q. getByAltText는 언제 써?
A. 의미 있는 이미지가 올바른 alt text를 갖는지 검증할 때 사용한다.

Q. 장식용 이미지에도 alt가 필요해?
A. 장식용 이미지는 `alt=""`로 보조기술에서 무시되도록 할 수 있다.

Q. getByTitle은 언제 써?
A. title 속성으로만 식별 가능한 요소를 찾을 때 제한적으로 사용한다.

Q. getByTestId는 언제 써?
A. role, label, text, alt 같은 사용자 인식 Query로 찾기 어려운 경우 최후 수단으로 사용한다.

Q. data-testid 이름은 어떻게 지어?
A. `festival-card`, `review-list`처럼 도메인 의미가 드러나는 kebab-case 이름이 좋다.

Q. getBy와 findBy 차이는 뭐야?
A. getBy는 즉시 존재하는 요소를 찾고, findBy는 비동기로 나중에 나타나는 요소를 기다린다.

Q. queryBy는 언제 써?
A. 특정 요소가 없어야 하는 것을 검증할 때 사용한다.

Q. 없는 요소를 getBy로 확인하면 왜 안 돼?
A. getBy는 요소가 없으면 먼저 throw하므로 absence 테스트에 적합하지 않다.

Q. 비동기 UI는 어떤 Query를 써?
A. `await screen.findBy...`를 사용한다.

Q. findBy에는 await가 필요해?
A. 필요하다. findBy는 Promise를 반환한다.

Q. 같은 요소가 여러 개면 어떻게 찾아?
A. getAllBy, findAllBy, queryAllBy 같은 AllBy 계열을 사용한다.

Q. within은 언제 써?
A. 반복 카드나 테이블 행 안에서 특정 요소를 정확히 찾고 싶을 때 사용한다.

Q. 같은 이름의 삭제 버튼이 여러 개면 어떻게 구분해?
A. 특정 카드나 행을 먼저 찾고 within으로 그 내부의 삭제 버튼을 찾는다.

Q. waitFor는 언제 써?
A. callback 호출이나 복잡한 비동기 조건이 만족될 때까지 기다릴 때 사용한다.

Q. findBy와 waitFor 중 뭐가 좋아?
A. 화면 요소가 나타나는 것을 기다릴 때는 findBy가 더 간단하고 명확하다.

Q. waitFor 안에서 userEvent를 실행해도 돼?
A. 지양한다. 사용자 이벤트는 waitFor 밖에서 실행하고 결과 assertion만 기다린다.

Q. waitFor를 남용하면 왜 안 좋아?
A. 테스트가 느려지고 실패 원인이 불명확해질 수 있다.

Q. Query가 실패하면 뭘 먼저 확인해?
A. screen.debug로 현재 DOM을 확인하고 비동기 렌더링 여부와 Query 선택을 확인한다.

Q. getByRole 실패는 접근성 문제일 수 있어?
A. 가능하다. semantic HTML, role, accessible name이 부족할 수 있다.

Q. Query 선택 체크리스트의 핵심은 뭐야?
A. role과 label을 우선 사용하고, 비동기에는 findBy, absence에는 queryBy를 사용하는 것이다.

Q. Part03 Query Rules의 최종 목표는 뭐야?
A. Frontend Agent가 사용자 관점과 비동기 상황에 맞는 Query를 선택하게 만드는 것이다.
