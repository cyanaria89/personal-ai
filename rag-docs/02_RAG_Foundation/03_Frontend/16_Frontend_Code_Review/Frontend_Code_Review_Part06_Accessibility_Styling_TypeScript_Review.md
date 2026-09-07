# Frontend Code Review Part06 - Accessibility, Styling, and TypeScript Review

---

# 1. Accessibility Review Rules

## 1.1 Semantic HTML Review

### [개념]

Semantic HTML Review는 프론트엔드 UI가 의미에 맞는 HTML 요소를 사용하고 있는지 검토하는 과정이다.

Semantic HTML은 접근성, SEO, 테스트 가능성, 유지보수성에 영향을 준다.

Review Agent는 div와 span 남용 여부, button / a 역할 구분, heading 구조, form label 연결을 검토해야 한다.

---

### [핵심]

Semantic HTML Review 검토 항목:

- 페이지 제목에 h1이 있는가?
- heading 구조가 h1 → h2 → h3 순서로 자연스러운가?
- 클릭 동작에는 button을 사용하는가?
- 페이지 이동에는 Link 또는 a를 사용하는가?
- 목록 데이터에는 ul / ol / li를 사용하는가?
- 표 형태 데이터에는 table을 사용하는가?
- form 입력에는 label이 연결되어 있는가?
- article / section / nav / main / header / footer 사용이 적절한가?
- div onClick을 버튼처럼 사용하지 않는가?
- aria를 semantic HTML 대체용으로 남용하지 않는가?

---

### [실무]

좋은 예:

```jsx
<main>
  <h1>축제 목록</h1>

  <section aria-labelledby="festival-filter-title">
    <h2 id="festival-filter-title">검색 조건</h2>
    <FestivalSearchForm />
  </section>

  <section aria-labelledby="festival-list-title">
    <h2 id="festival-list-title">검색 결과</h2>
    <FestivalList festivals={festivals} />
  </section>
</main>
```

나쁜 예:

```jsx
<div onClick={handleClick}>삭제</div>
```

개선 예:

```jsx
<button type="button" onClick={handleClick}>
  삭제
</button>
```

리뷰 코멘트 예:

```text
[Medium] 클릭 가능한 div가 버튼 역할을 하고 있습니다. 키보드 접근성과 의미 전달을 위해 button 요소로 변경하는 것이 좋습니다.
```

---

### [FAQ]

Q. Semantic HTML Review는 왜 필요해?
A. 의미 있는 HTML은 접근성, SEO, 테스트 가능성, 유지보수성을 높이기 때문이다.

Q. div에 onClick을 쓰면 안 돼?
A. 버튼 역할이면 button을 사용하는 것이 좋다. div 클릭은 키보드 접근성과 의미 전달에 문제가 생기기 쉽다.

Q. aria를 많이 넣으면 접근성이 좋아져?
A. 아니다. semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. heading 구조도 리뷰해야 해?
A. 해야 한다. heading 구조는 화면 구조 이해, 스크린 리더 탐색, SEO에 영향을 준다.

---

## 1.2 Keyboard Navigation Review

### [개념]

Keyboard Navigation Review는 사용자가 마우스 없이 키보드만으로 주요 기능을 사용할 수 있는지 검토하는 과정이다.

접근 가능한 UI는 Tab 이동, Enter / Space 실행, Escape 닫기, focus 이동이 자연스러워야 한다.

---

### [핵심]

Keyboard Navigation Review 검토 항목:

- Tab으로 주요 조작 요소에 접근 가능한가?
- focus 순서가 화면 흐름과 일치하는가?
- button은 Enter / Space로 실행 가능한가?
- Link는 Enter로 이동 가능한가?
- modal이 열리면 focus가 modal 내부로 이동하는가?
- modal에서 Escape 닫기가 가능한가?
- modal 내부 focus trap이 있는가?
- dropdown / menu 키보드 조작이 가능한가?
- focus outline이 제거되지 않았는가?
- disabled 요소와 focus 동작이 적절한가?

---

### [실무]

focus outline 제거 위험:

```css
button:focus {
  outline: none;
}
```

문제:

```text
키보드 사용자가 현재 focus 위치를 알 수 없음
```

개선 방향:

```css
button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

modal keyboard flow:

```text
Open Modal
→ Focus Move Into Modal
→ Tab Cycles Inside Modal
→ Escape Closes Modal
→ Focus Returns To Trigger Button
```

리뷰 코멘트 예:

```text
[Medium] focus outline이 전역에서 제거되어 키보드 사용자가 현재 위치를 알 수 없습니다. focus-visible 스타일을 제공해야 합니다.
```

---

### [FAQ]

Q. Keyboard Navigation Review는 왜 필요해?
A. 마우스를 사용하지 못하는 사용자도 주요 기능을 사용할 수 있어야 하기 때문이다.

Q. focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 제거하려면 대체 focus-visible 스타일을 제공해야 한다.

Q. modal이 열릴 때 focus는 어디로 가야 해?
A. modal 내부의 첫 번째 조작 가능한 요소나 modal 제목으로 이동하는 것이 좋다.

Q. Escape로 modal을 닫을 수 있어야 해?
A. 일반적으로 권장된다. 단, 중요한 확인 과정에서는 닫기 정책을 명확히 해야 한다.

---

## 1.3 Image Alt Review

### [개념]

Image Alt Review는 이미지에 적절한 대체 텍스트가 제공되는지 검토하는 과정이다.

이미지는 정보 전달 이미지, 장식 이미지, 링크 이미지, 버튼 이미지에 따라 alt 기준이 달라진다.

---

### [핵심]

Image Alt Review 검토 항목:

- 정보 전달 이미지에 의미 있는 alt가 있는가?
- 장식 이미지는 alt=""로 처리하는가?
- 링크 이미지에는 이동 목적이 드러나는 alt가 있는가?
- 버튼 이미지에는 동작이 드러나는 alt 또는 aria-label이 있는가?
- 이미지 파일명을 alt로 그대로 쓰지 않는가?
- 모든 이미지에 같은 alt를 반복하지 않는가?
- 외부 API 이미지 데이터가 없을 때 fallback이 있는가?

---

### [실무]

정보 이미지 예:

```jsx
<img src={festival.imageUrl} alt={`${festival.title} 대표 이미지`} />
```

장식 이미지 예:

```jsx
<img src="/decorative-line.png" alt="" />
```

나쁜 예:

```jsx
<img src={festival.imageUrl} alt="image" />
```

리뷰 코멘트 예:

```text
[Medium] 축제 대표 이미지 alt가 image로만 작성되어 의미를 전달하지 못합니다. 축제명 기반 대체 텍스트를 제공하는 것이 좋습니다.
```

---

### [FAQ]

Q. 모든 이미지에 alt가 필요해?
A. img 요소에는 alt가 필요하다. 정보 이미지는 의미 있는 alt, 장식 이미지는 alt=""를 사용한다.

Q. 장식 이미지에도 설명을 넣어야 해?
A. 아니다. 장식 목적이면 alt=""로 스크린 리더가 무시하게 하는 것이 좋다.

Q. alt="image"는 괜찮아?
A. 좋지 않다. 이미지가 전달하는 정보나 목적을 설명해야 한다.

Q. 이미지가 링크라면 alt는 어떻게 써?
A. 이미지 자체 설명보다 링크가 이동하는 목적을 설명하는 것이 좋다.

---

## 1.4 ARIA Review

### [개념]

ARIA Review는 HTML만으로 의미를 충분히 전달하기 어려운 UI에서 aria 속성을 적절하게 사용하는지 검토하는 과정이다.

ARIA는 semantic HTML을 대체하는 도구가 아니라 보완하는 도구이다.

---

### [핵심]

ARIA Review 검토 항목:

- semantic HTML로 해결 가능한데 aria를 남용하지 않는가?
- aria-label이 실제 동작과 일치하는가?
- aria-labelledby 연결 대상이 존재하는가?
- aria-describedby가 error message와 연결되는가?
- aria-expanded가 dropdown 상태와 일치하는가?
- aria-controls 대상 id가 존재하는가?
- role이 실제 키보드 동작과 일치하는가?
- role="alert"가 error message에 적절히 사용되는가?
- aria-hidden으로 중요한 내용을 숨기지 않는가?

---

### [실무]

error message 연결 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  aria-invalid={Boolean(errors.email)}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
{errors.email && (
  <p id="email-error" role="alert">
    {errors.email}
  </p>
)}
```

dropdown 예:

```jsx
<button
  type="button"
  aria-expanded={isOpen}
  aria-controls="region-menu"
  onClick={toggleOpen}
>
  지역 선택
</button>
```

리뷰 코멘트 예:

```text
[Medium] aria-controls가 menu-list를 가리키지만 해당 id를 가진 요소가 없습니다. aria 연결 대상이 실제 DOM에 존재하는지 확인해야 합니다.
```

---

### [FAQ]

Q. ARIA는 언제 사용해?
A. semantic HTML만으로 상태나 관계를 충분히 전달하기 어려울 때 사용한다.

Q. button 대신 div role="button"을 쓰면 돼?
A. 가능은 하지만 키보드 동작까지 직접 구현해야 하므로 실제 button 사용이 더 안전하다.

Q. aria-label은 아무 곳에나 붙여도 돼?
A. 아니다. 시각적 텍스트가 없거나 의미 보완이 필요한 조작 요소에 적절히 사용한다.

Q. aria-hidden은 주의해야 해?
A. 그렇다. 중요한 콘텐츠나 focus 가능한 요소에 aria-hidden을 적용하면 접근성 문제가 생긴다.

---

## 1.5 Modal Accessibility Review

### [개념]

Modal Accessibility Review는 modal, dialog, popup UI가 키보드와 스크린 리더 환경에서도 안전하게 동작하는지 검토하는 과정이다.

Modal은 focus 이동, focus trap, background interaction 차단, 닫기 동작이 중요하다.

---

### [핵심]

Modal Accessibility Review 검토 항목:

- role="dialog" 또는 dialog 요소를 사용하는가?
- aria-modal="true"가 있는가?
- modal title이 제공되는가?
- aria-labelledby가 title과 연결되는가?
- modal open 시 focus가 내부로 이동하는가?
- modal 내부 focus trap이 있는가?
- Escape 닫기가 가능한가?
- 닫기 버튼이 있는가?
- modal 닫힘 후 이전 focus가 복원되는가?
- 배경 스크롤이 방지되는가?
- overlay 클릭 닫기 정책이 명확한가?

---

### [실무]

modal 구조 예:

```jsx
<div role="dialog" aria-modal="true" aria-labelledby="review-modal-title">
  <h2 id="review-modal-title">리뷰 작성</h2>

  <ReviewForm />

  <button type="button" onClick={onClose}>
    닫기
  </button>
</div>
```

리뷰 코멘트 예:

```text
[High] 리뷰 작성 modal이 열려도 focus가 modal 내부로 이동하지 않고 배경 요소에 머물 수 있습니다. modal open 시 focus 이동과 focus trap 처리가 필요합니다.
```

---

### [FAQ]

Q. Modal Accessibility Review는 왜 중요해?
A. modal은 화면 흐름을 가로막는 UI이므로 focus 관리와 키보드 조작이 없으면 사용자가 갇히거나 내용을 놓칠 수 있다.

Q. modal에 role="dialog"가 필요해?
A. div 기반 modal이라면 dialog 역할과 aria-modal 설정이 필요하다.

Q. modal 닫기 버튼은 꼭 있어야 해?
A. 권장된다. Escape나 overlay 클릭 외에도 명확한 닫기 버튼을 제공해야 한다.

Q. modal 닫힌 후 focus는 어디로 가야 해?
A. modal을 열었던 버튼이나 이전 focus 위치로 복원하는 것이 좋다.

---

# 2. Styling Review Rules

## 2.1 Styling Consistency Review

### [개념]

Styling Consistency Review는 프론트엔드 스타일 코드가 프로젝트 규칙에 맞게 일관적으로 작성되었는지 검토하는 과정이다.

스타일 도구 자체보다 naming, spacing, color, responsive, state style의 일관성이 중요하다.

---

### [핵심]

Styling Consistency Review 검토 항목:

- className naming이 일관적인가?
- CSS Module / Styled Components / Tailwind / Plain CSS 사용 규칙이 섞이지 않는가?
- inline style을 남용하지 않는가?
- 중복 CSS가 과도하지 않은가?
- 색상값이 무분별하게 하드코딩되지 않는가?
- spacing 값이 일관적인가?
- font size 기준이 일관적인가?
- hover / active / disabled / focus 상태가 정의되어 있는가?
- dark mode 요구사항이 있으면 반영되어 있는가?
- 전역 class 충돌 위험이 없는가?

---

### [실무]

Review Agent는 스타일 도구 자체보다 일관성을 우선 본다.

```text
CSS Module 사용 프로젝트
→ className scope와 파일 분리 확인

Styled Components 사용 프로젝트
→ props 기반 스타일 과다 여부 확인

Tailwind 사용 프로젝트
→ className 중복과 component 추출 여부 확인

Plain CSS 사용 프로젝트
→ 전역 class 충돌과 naming 확인
```

리뷰 코멘트 예:

```text
[Low] 동일한 primary color 값이 여러 CSS 파일에 하드코딩되어 있습니다. CSS variable 또는 design token으로 분리하면 변경 관리가 쉬워집니다.
```

---

### [FAQ]

Q. Styling Review에서 가장 중요한 것은 뭐야?
A. 도구 선택보다 naming, spacing, color, responsive, 상태 스타일의 일관성이다.

Q. inline style은 무조건 나빠?
A. 무조건은 아니지만 반복되는 스타일이나 상태 스타일은 class 또는 styling system으로 분리하는 것이 좋다.

Q. 색상값을 직접 써도 돼?
A. 가능하지만 반복되는 색상은 CSS variable 또는 design token으로 관리하는 것이 좋다.

Q. 여러 스타일 방식을 섞어도 돼?
A. 가능은 하지만 규칙 없이 섞이면 유지보수성이 떨어진다.

---

## 2.2 Responsive Review

### [개념]

Responsive Review는 프론트엔드 화면이 모바일, 태블릿, 데스크톱 등 다양한 화면 크기에서 깨지지 않는지 검토하는 과정이다.

반응형 문제는 기능이 동작해도 실제 사용성을 크게 떨어뜨릴 수 있다.

---

### [핵심]

Responsive Review 검토 항목:

- 모바일 화면에서 가로 스크롤이 없는가?
- 고정 width로 인해 화면이 깨지지 않는가?
- 카드 / 리스트 줄바꿈이 정상인가?
- 이미지가 컨테이너를 넘지 않는가?
- table overflow 처리가 있는가?
- modal width가 모바일에서 적절한가?
- header / nav가 작은 화면에서 사용 가능한가?
- font size가 읽을 수 있는가?
- 터치 영역이 충분한가?
- breakpoint가 일관적인가?
- layout shift가 과도하지 않은가?

---

### [실무]

반응형 확인 기준:

```text
Mobile 360px
→ Tablet 768px
→ Desktop 1024px
→ Wide 1280px
```

대표 문제:

```text
fixed width
image max-width 누락
flex-wrap 누락
table overflow 처리 누락
modal width 고정
button touch area 부족
header menu overflow
```

개선 예:

```css
img {
  max-width: 100%;
  height: auto;
}
```

```css
.table-wrapper {
  overflow-x: auto;
}
```

리뷰 코멘트 예:

```text
[Medium] 모바일 360px 화면에서 카드 컨테이너의 고정 width로 가로 스크롤이 발생할 수 있습니다. width: 100%와 max-width 조합을 검토해야 합니다.
```

---

### [FAQ]

Q. Responsive Review에서 가장 먼저 볼 것은 뭐야?
A. 모바일 화면에서 가로 스크롤이 생기는지, 주요 버튼과 텍스트가 사용 가능한지 확인한다.

Q. 모든 기기 사이즈를 다 맞춰야 해?
A. 모든 기기를 개별 대응하기보다 콘텐츠가 깨지는 지점을 기준으로 breakpoint를 설정한다.

Q. table은 모바일에서 어떻게 처리해?
A. column 축약, card layout 전환, 또는 wrapper overflow-x 처리를 검토한다.

Q. modal은 모바일에서 무엇을 주의해야 해?
A. 고정 width, 화면 밖 overflow, 닫기 버튼 접근성, 배경 스크롤을 주의해야 한다.

---

## 2.3 State Style Review

### [개념]

State Style Review는 UI 요소가 hover, active, focus, disabled, selected, error, loading 상태를 시각적으로 명확히 표현하는지 검토하는 과정이다.

상태 스타일이 없으면 사용자는 현재 요소가 클릭 가능한지, 선택되었는지, 비활성화되었는지 알기 어렵다.

---

### [핵심]

State Style Review 검토 항목:

- hover 상태가 있는가?
- active 상태가 있는가?
- focus-visible 상태가 있는가?
- disabled 상태가 명확한가?
- selected 상태가 명확한가?
- error 상태가 색상 외 다른 방식으로도 표시되는가?
- loading 상태가 시각적으로 표시되는가?
- 색상만으로 상태를 전달하지 않는가?
- cursor 스타일이 상태와 일치하는가?
- 버튼 비활성화 시 실제 disabled 속성도 있는가?

---

### [실무]

disabled 예:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "저장 중..." : "저장"}
</button>
```

```css
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

error 상태 예:

```jsx
<input
  aria-invalid={Boolean(errors.email)}
  className={errors.email ? "input input-error" : "input"}
/>
<p id="email-error" role="alert">
  {errors.email}
</p>
```

리뷰 코멘트 예:

```text
[Medium] 제출 중 버튼이 시각적으로만 비활성화되어 있고 disabled 속성이 없습니다. 실제 중복 제출을 막기 위해 disabled 속성도 함께 적용해야 합니다.
```

---

### [FAQ]

Q. State Style Review는 왜 필요해?
A. 사용자가 현재 UI 요소의 상태와 가능한 행동을 이해할 수 있어야 하기 때문이다.

Q. disabled 스타일만 있으면 충분해?
A. 아니다. 실제 disabled 속성이나 클릭 guard도 함께 필요하다.

Q. 색상만으로 error를 표시해도 돼?
A. 권장하지 않는다. 텍스트 메시지, 아이콘, aria-invalid 등도 함께 제공하는 것이 좋다.

Q. focus style은 디자인상 숨겨도 돼?
A. 숨기면 안 된다. 디자인에 맞는 focus-visible 대체 스타일을 제공해야 한다.

---

## 2.4 CSS Naming and Scope Review

### [개념]

CSS Naming and Scope Review는 className 이름이 역할을 명확히 표현하고 스타일 적용 범위가 예측 가능한지 검토하는 과정이다.

전역 CSS 충돌, 모호한 className, 중복 스타일은 유지보수성을 떨어뜨린다.

---

### [핵심]

검토 항목:

- className이 역할을 표현하는가?
- 너무 일반적인 이름을 사용하지 않는가?
- 전역 class 충돌 위험이 없는가?
- 컴포넌트 단위 scope가 유지되는가?
- BEM 또는 프로젝트 naming 규칙이 일관적인가?
- CSS Module 사용 시 파일명과 컴포넌트가 연결되는가?
- 사용하지 않는 class가 방치되지 않는가?
- 동일 스타일이 여러 이름으로 반복되지 않는가?

---

### [실무]

나쁜 예:

```css
.box {
  padding: 16px;
}

.title {
  font-size: 20px;
}
```

개선 예:

```css
.festival-card {
  padding: 16px;
}

.festival-card__title {
  font-size: 20px;
}
```

CSS Module 예:

```text
FestivalCard.module.css
→ FestivalCard.jsx에서 import styles from "./FestivalCard.module.css"
```

리뷰 코멘트 예:

```text
[Low] box, title처럼 전역적으로 충돌하기 쉬운 className이 사용되고 있습니다. 도메인과 컴포넌트 역할이 드러나는 이름으로 변경하는 것이 좋습니다.
```

---

### [FAQ]

Q. CSS className 이름도 리뷰해야 해?
A. 해야 한다. 모호한 이름과 전역 충돌은 유지보수성을 떨어뜨린다.

Q. box, title 같은 이름은 왜 위험해?
A. 전역 CSS에서 다른 컴포넌트와 충돌하거나 역할을 알기 어렵기 때문이다.

Q. CSS Module을 쓰면 naming이 중요하지 않아?
A. scope 충돌은 줄지만 역할을 이해하기 위한 명확한 naming은 여전히 중요하다.

Q. BEM은 꼭 써야 해?
A. 필수는 아니다. 프로젝트에서 정한 naming 규칙이 일관적으로 적용되는지가 더 중요하다.

---

# 3. TypeScript Review Rules

## 3.1 Type Safety Review

### [개념]

Type Safety Review는 TypeScript 타입이 실제 데이터 구조와 일치하고, any 또는 과도한 type assertion으로 타입 안전성이 약해지지 않았는지 검토하는 과정이다.

타입은 문서이자 컴파일 단계의 검증 장치이다.

Review Agent는 타입이 코드의 실제 흐름을 보호하고 있는지 확인해야 한다.

---

### [핵심]

Type Safety Review 검토 항목:

- API Response 타입이 정의되어 있는가?
- Props 타입이 명확한가?
- Event 타입이 적절한가?
- nullable field 처리가 있는가?
- optional field 처리가 있는가?
- any 남용이 없는가?
- unknown을 적절히 narrowing하는가?
- type assertion 남용이 없는가?
- enum 또는 union type이 적절한가?
- generic이 과도하게 복잡하지 않은가?
- backend DTO와 frontend type이 불일치하지 않는가?

---

### [실무]

Props type 예:

```tsx
type FestivalCardProps = {
  festival: Festival;
  isFavorite: boolean;
  onFavoriteClick: (festivalId: number) => void;
};

function FestivalCard({
  festival,
  isFavorite,
  onFavoriteClick,
}: FestivalCardProps) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <button type="button" onClick={() => onFavoriteClick(festival.id)}>
        {isFavorite ? "찜 해제" : "찜하기"}
      </button>
    </article>
  );
}
```

나쁜 예:

```tsx
function FestivalCard(props: any) {
  return <div>{props.data.title}</div>;
}
```

리뷰 코멘트 예:

```text
[Medium] FestivalCard props가 any로 선언되어 API 응답 구조 변경이나 필드 누락을 컴파일 단계에서 감지할 수 없습니다. 명시적인 Props 타입을 정의하는 것이 좋습니다.
```

---

### [FAQ]

Q. Type Safety Review는 왜 필요해?
A. 타입이 실제 데이터 구조와 맞아야 런타임 오류를 컴파일 단계에서 줄일 수 있기 때문이다.

Q. any를 써도 돼?
A. 임시로는 가능하지만 최종 코드에서는 구체적인 타입으로 대체하는 것이 좋다.

Q. API 응답 타입은 꼭 만들어야 해?
A. 권장된다. 응답 구조가 명확해야 화면 코드와 API 변경 영향도를 줄일 수 있다.

Q. backend DTO와 frontend type도 비교해야 해?
A. 해야 한다. 필드명, nullable, enum 값이 다르면 화면 오류나 타입 우회가 발생할 수 있다.

---

## 3.2 API Response Type Review

### [개념]

API Response Type Review는 백엔드 응답 wrapper, data payload, Page / Slice 구조가 TypeScript 타입으로 정확히 표현되는지 검토하는 과정이다.

API 타입이 부정확하면 response mapping 오류와 undefined 접근을 막기 어렵다.

---

### [핵심]

검토 항목:

- 공통 ApiResponse 타입이 있는가?
- data generic 타입이 있는가?
- Page response 타입이 있는가?
- Slice response 타입이 있는가?
- optional field가 optional로 표현되는가?
- null 가능 field가 명시되는가?
- enum 문자열 값이 union type으로 제한되는가?
- API 함수 return type이 명확한가?
- response.data.data 접근 구조가 타입으로 표현되는가?

---

### [실무]

ApiResponse type 예:

```tsx
type ApiResponse<T> = {
  success: boolean;
  message: string;
  data: T;
};
```

Page type 예:

```tsx
type PageResponse<T> = {
  content: T[];
  totalElements: number;
  totalPages: number;
  number: number;
  size: number;
  first: boolean;
  last: boolean;
};
```

Slice type 예:

```tsx
type SliceResponse<T> = {
  content: T[];
  number: number;
  size: number;
  first: boolean;
  last: boolean;
  hasNext: boolean;
};
```

API function 예:

```tsx
function getFestivalDetail(
  festivalId: number,
): Promise<AxiosResponse<ApiResponse<FestivalDetail>>> {
  return api.get(`/festivals/${festivalId}`);
}
```

리뷰 코멘트 예:

```text
[Medium] API 응답 타입이 FestivalDetail로만 선언되어 있지만 실제 응답은 ApiResponse<FestivalDetail> wrapper 구조입니다. response.data.data 접근이 타입으로 표현되도록 수정해야 합니다.
```

---

### [FAQ]

Q. ApiResponse generic type은 왜 필요해?
A. 공통 wrapper 구조와 실제 data payload를 함께 안전하게 표현하기 위해 필요하다.

Q. Page와 Slice 타입을 구분해야 해?
A. 그렇다. Page는 total count 정보가 있고 Slice는 hasNext 중심이므로 화면 처리 방식이 다르다.

Q. API 함수 return type을 생략해도 돼?
A. 추론이 가능하면 생략할 수 있지만 공통 API module에서는 명시하는 것이 유지보수에 도움이 된다.

Q. enum 문자열은 string으로 두면 안 돼?
A. 가능하지만 union type으로 제한하면 오타와 잘못된 값 사용을 줄일 수 있다.

---

## 3.3 Null Undefined Review

### [개념]

Null Undefined Review는 값이 없을 수 있는 상황을 TypeScript와 UI 로직에서 안전하게 처리하는지 검토하는 과정이다.

프론트엔드 런타임 오류는 데이터 로딩 전 undefined 접근, optional field 누락, null 응답에서 자주 발생한다.

---

### [핵심]

Null Undefined Review 검토 항목:

- 초기 데이터 null 처리가 있는가?
- loading 전 데이터 접근을 막는가?
- optional chaining을 적절히 사용하는가?
- fallback UI가 있는가?
- null 가능 타입이 명시되어 있는가?
- non-null assertion을 남용하지 않는가?
- API optional field에 대응하는가?
- empty string, 0, false를 null처럼 잘못 처리하지 않는가?
- map 호출 전 array 기본값이 있는가?

---

### [실무]

나쁜 예:

```tsx
return <h1>{festival.title}</h1>;
```

문제:

```text
festival이 null일 수 있으면 Cannot read properties of null 오류 발생
```

좋은 예:

```tsx
if (isLoading) {
  return <p>불러오는 중...</p>;
}

if (!festival) {
  return <p>축제 정보를 찾을 수 없습니다.</p>;
}

return <h1>{festival.title}</h1>;
```

non-null assertion 위험 예:

```tsx
return <h1>{festival!.title}</h1>;
```

리뷰 코멘트 예:

```text
[High] festival이 null일 수 있는데 festival.title에 바로 접근하고 있습니다. loading / empty 분기 후 안전하게 렌더링해야 합니다.
```

---

### [FAQ]

Q. Cannot read properties of undefined 오류는 왜 나?
A. 데이터가 로딩되기 전 undefined 또는 null 값에 접근했기 때문이다.

Q. optional chaining만 쓰면 충분해?
A. 항상 충분하지 않다. 사용자에게 보여줄 fallback UI도 필요하다.

Q. non-null assertion을 써도 돼?
A. 정말 null이 아님을 보장할 수 있을 때만 제한적으로 사용해야 한다.

Q. 빈 배열 기본값은 왜 필요해?
A. undefined 상태에서 map을 호출하면 런타임 오류가 발생할 수 있기 때문이다.

---

## 3.4 Event Type Review

### [개념]

Event Type Review는 React event handler의 event 타입이 명확하게 작성되었는지 검토하는 과정이다.

event 타입이 any이면 target value, checked, files 접근에서 타입 안정성을 잃는다.

---

### [핵심]

Event Type Review 검토 항목:

- input change event 타입이 명확한가?
- form submit event 타입이 명확한가?
- button click event 타입이 필요한 경우 명시되어 있는가?
- file input event에서 files null 처리가 있는가?
- event.target 대신 event.currentTarget 사용이 적절한가?
- any event를 사용하지 않는가?
- handler props 타입이 명확한가?

---

### [실무]

input change 예:

```tsx
function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
  const { name, value } = event.target;
}
```

form submit 예:

```tsx
function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
  event.preventDefault();
}
```

file input 예:

```tsx
function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
  const file = event.target.files?.[0];

  if (!file) return;

  validateFile(file);
}
```

리뷰 코멘트 예:

```text
[Low] form submit event가 any로 선언되어 있습니다. React.FormEvent<HTMLFormElement>로 명시하면 preventDefault와 currentTarget 사용이 더 안전해집니다.
```

---

### [FAQ]

Q. Event Type Review는 왜 필요해?
A. event 타입이 명확해야 value, checked, files 접근을 안전하게 처리할 수 있기 때문이다.

Q. input onChange 타입은 뭐야?
A. 일반 text input은 React.ChangeEvent<HTMLInputElement>를 사용한다.

Q. form onSubmit 타입은 뭐야?
A. React.FormEvent<HTMLFormElement>를 사용한다.

Q. file input에서 files는 항상 있어?
A. 아니다. files가 null이거나 비어 있을 수 있으므로 확인이 필요하다.

---

## 3.5 Type Assertion Review

### [개념]

Type Assertion Review는 `as` 또는 non-null assertion으로 TypeScript 검사를 우회하는 코드가 안전한지 검토하는 과정이다.

type assertion은 필요한 경우 사용할 수 있지만 남용하면 TypeScript의 보호 기능이 약해진다.

---

### [핵심]

Type Assertion Review 검토 항목:

- `as any`를 사용하지 않는가?
- `as unknown as` 이중 assertion을 남용하지 않는가?
- non-null assertion `!`을 남용하지 않는가?
- API response를 검증 없이 assertion하지 않는가?
- DOM query 결과 null 처리를 하는가?
- unknown error를 안전하게 narrowing하는가?
- assertion 대신 type guard를 사용할 수 있는가?

---

### [실무]

위험 예:

```tsx
const festival = response.data as FestivalDetail;
```

문제:

```text
실제 response가 ApiResponse<FestivalDetail>이면 타입이 거짓으로 맞춰짐
→ response mapping 오류를 컴파일러가 감지하지 못함
```

type guard 예:

```tsx
function isApiError(error: unknown): error is AxiosError {
  return typeof error === "object" && error !== null && "isAxiosError" in error;
}
```

리뷰 코멘트 예:

```text
[Medium] API 응답을 as FestivalDetail로 강제 단언하고 있습니다. 실제 응답 wrapper 구조와 다를 수 있으므로 ApiResponse<FestivalDetail> 타입으로 정의하는 것이 안전합니다.
```

---

### [FAQ]

Q. Type Assertion은 쓰면 안 돼?
A. 필요한 경우 사용할 수 있지만 타입을 속이는 방식으로 남용하면 위험하다.

Q. as any는 왜 문제야?
A. 해당 값에 대한 타입 검사가 사실상 비활성화되어 런타임 오류를 막기 어렵다.

Q. non-null assertion은 언제 써도 돼?
A. 해당 값이 null이 아님을 구조적으로 보장할 수 있을 때만 제한적으로 사용한다.

Q. assertion 대신 무엇을 쓰면 좋아?
A. 타입 정의를 정확히 하거나 type guard, runtime validation, 조건 분기를 사용하는 것이 좋다.

---

# 4. Accessibility Styling TypeScript Review Checklist

## 4.1 Accessibility Review Checklist

### [개념]

Accessibility Review Checklist는 Review Agent가 프론트엔드 접근성 기본 품질을 검토할 때 사용하는 최종 점검 목록이다.

접근성은 선택 기능이 아니라 사용자 흐름, 품질, 테스트 가능성과 연결되는 기본 리뷰 항목이다.

---

### [핵심]

Accessibility Review Checklist:

```md
## Semantic HTML

- [ ] main, section, nav, header, footer 사용이 적절한가?
- [ ] heading 구조가 자연스러운가?
- [ ] button과 link 역할이 구분되는가?
- [ ] div onClick을 버튼처럼 사용하지 않는가?
- [ ] form input에 label이 연결되어 있는가?

## Keyboard

- [ ] 키보드만으로 주요 기능을 사용할 수 있는가?
- [ ] Tab focus 순서가 자연스러운가?
- [ ] focus-visible 스타일이 있는가?
- [ ] modal Escape 닫기가 가능한가?
- [ ] modal focus trap이 있는가?

## Image

- [ ] 정보 이미지에 의미 있는 alt가 있는가?
- [ ] 장식 이미지는 alt=""로 처리되는가?
- [ ] 이미지 버튼 또는 링크의 목적이 전달되는가?

## ARIA

- [ ] aria-label이 실제 동작과 일치하는가?
- [ ] aria-labelledby 연결 대상이 존재하는가?
- [ ] aria-describedby가 error message와 연결되는가?
- [ ] aria-expanded 상태가 실제 open 상태와 일치하는가?
- [ ] role="alert"가 필요한 error message에 적용되는가?

## Modal

- [ ] role="dialog" 또는 dialog 구조가 있는가?
- [ ] aria-modal="true"가 있는가?
- [ ] modal title이 연결되어 있는가?
- [ ] focus 이동과 복원이 처리되는가?
```

---

### [실무]

Accessibility Review 우선순위:

```text
Keyboard Blocking
→ Modal Focus Trap Missing
→ Form Label Missing
→ Button / Link Role Misuse
→ Missing Error Accessibility
→ Missing Image Alt
→ Heading Structure
```

우선순위 판단:

```text
키보드로 핵심 기능 사용 불가
→ High

modal focus trap 누락
→ High 또는 Medium

form label 누락
→ Medium

div onClick 버튼 역할
→ Medium

alt 누락
→ Medium 또는 Low

heading 구조 문제
→ Low 또는 Medium
```

---

### [FAQ]

Q. Accessibility Review에서 가장 먼저 볼 것은 뭐야?
A. 키보드 사용 가능 여부, form label, button / link 역할, modal focus 처리를 먼저 본다.

Q. 접근성 문제는 항상 High야?
A. 핵심 기능 사용을 막으면 High다. 단순 alt 누락이나 heading 문제는 Medium 또는 Low일 수 있다.

Q. 접근성 리뷰는 왜 코드 리뷰에 포함돼?
A. 접근성은 사용자 품질, 테스트 가능성, SEO, 법적 기준과 연결될 수 있기 때문이다.

Q. Semantic HTML을 쓰면 aria가 필요 없어?
A. 많은 경우 줄어든다. semantic HTML을 우선하고 부족한 의미를 aria로 보완한다.

---

## 4.2 Styling Review Checklist

### [개념]

Styling Review Checklist는 Review Agent가 스타일 일관성, 반응형, 상태 스타일, CSS scope를 검토할 때 사용하는 최종 점검 목록이다.

스타일 리뷰는 취향 평가가 아니라 유지보수성과 사용성 위험을 찾는 과정이다.

---

### [핵심]

Styling Review Checklist:

```md
## Consistency

- [ ] className naming이 일관적인가?
- [ ] 스타일 도구 사용 규칙이 일관적인가?
- [ ] inline style을 남용하지 않는가?
- [ ] 중복 CSS가 과도하지 않은가?
- [ ] 색상 / spacing / font size 기준이 일관적인가?

## Responsive

- [ ] 모바일 360px에서 가로 스크롤이 없는가?
- [ ] 고정 width로 layout이 깨지지 않는가?
- [ ] 이미지가 컨테이너를 넘지 않는가?
- [ ] table overflow 처리가 있는가?
- [ ] modal이 모바일 화면에서 사용 가능한가?
- [ ] 터치 영역이 충분한가?

## State Style

- [ ] hover / active / focus-visible 상태가 있는가?
- [ ] disabled 상태가 시각적으로 명확한가?
- [ ] selected 상태가 명확한가?
- [ ] error 상태가 색상 외 방식으로도 전달되는가?
- [ ] 실제 disabled 속성과 스타일이 함께 적용되는가?

## CSS Scope

- [ ] 전역 class 충돌 위험이 없는가?
- [ ] 너무 일반적인 className을 사용하지 않는가?
- [ ] CSS Module 사용 시 scope가 유지되는가?
- [ ] 사용하지 않는 class가 방치되지 않는가?
```

---

### [실무]

Styling Review 우선순위:

```text
Responsive Broken
→ Hidden Critical Button
→ Disabled State Missing
→ Focus Style Missing
→ CSS Global Conflict
→ Color / Spacing Inconsistency
→ Naming Improvement
```

우선순위 판단:

```text
모바일에서 핵심 버튼 사용 불가
→ High

가로 스크롤로 주요 콘텐츠 접근 어려움
→ Medium 또는 High

focus style 제거
→ Medium

disabled 실제 속성 누락
→ Medium

색상 하드코딩 반복
→ Low

className 모호함
→ Low
```

---

### [FAQ]

Q. Styling Review는 취향 리뷰야?
A. 아니다. 일관성, 반응형, 상태 전달, 유지보수성, 접근성 위험을 검토하는 것이다.

Q. 모바일 화면 깨짐은 어떤 우선순위야?
A. 핵심 기능 사용을 막으면 High, 일부 layout 문제면 Medium으로 볼 수 있다.

Q. 색상 하드코딩은 어떤 우선순위야?
A. 보통 Low지만 디자인 시스템 변경 비용이 크면 Medium이 될 수 있다.

Q. disabled 스타일만 있고 실제 disabled가 없으면 문제야?
A. 문제다. 시각적으로만 비활성화되어도 실제 클릭이 가능하면 중복 요청이 발생할 수 있다.

---

## 4.3 TypeScript Review Checklist

### [개념]

TypeScript Review Checklist는 Review Agent가 타입 안정성, API 응답 타입, null 처리, event 타입, assertion 남용을 검토할 때 사용하는 최종 점검 목록이다.

TypeScript 리뷰의 목적은 타입 작성 자체가 아니라 런타임 오류를 줄이는 것이다.

---

### [핵심]

TypeScript Review Checklist:

```md
## Type Safety

- [ ] Props 타입이 명확한가?
- [ ] API Response 타입이 정의되어 있는가?
- [ ] Event 타입이 적절한가?
- [ ] any 남용이 없는가?
- [ ] unknown을 안전하게 narrowing하는가?
- [ ] enum 또는 union type이 적절한가?

## API Type

- [ ] ApiResponse<T> wrapper 타입이 있는가?
- [ ] PageResponse<T>와 SliceResponse<T>를 구분하는가?
- [ ] response.data.data 구조가 타입으로 표현되는가?
- [ ] optional field와 nullable field가 정확한가?
- [ ] backend DTO와 frontend type이 일치하는가?

## Null Undefined

- [ ] 초기 null 상태를 안전하게 처리하는가?
- [ ] loading 전 데이터 접근을 막는가?
- [ ] optional chaining과 fallback UI가 있는가?
- [ ] non-null assertion을 남용하지 않는가?
- [ ] array map 전 기본값이 있는가?

## Event

- [ ] input change event 타입이 명확한가?
- [ ] form submit event 타입이 명확한가?
- [ ] file input files null 처리가 있는가?

## Assertion

- [ ] as any를 사용하지 않는가?
- [ ] API response를 검증 없이 assertion하지 않는가?
- [ ] assertion 대신 정확한 타입 정의나 type guard를 사용할 수 있는가?
```

---

### [실무]

TypeScript Review 우선순위:

```text
Runtime Null Error
→ API Type Mismatch
→ any on Core Data
→ Unsafe Type Assertion
→ Event Type any
→ Union Type Improvement
```

우선순위 판단:

```text
null 접근으로 흰 화면 발생
→ High

API wrapper 타입 불일치
→ Medium 또는 High

핵심 데이터 any 남용
→ Medium

as any 남용
→ Medium

event 타입 any
→ Low

union type 개선
→ Low 또는 Suggestion
```

---

### [FAQ]

Q. TypeScript Review에서 가장 먼저 볼 것은 뭐야?
A. null 접근 위험, API 응답 타입 불일치, any 남용, unsafe assertion을 먼저 본다.

Q. any가 하나라도 있으면 Critical이야?
A. 아니다. 핵심 데이터 흐름에서 any가 런타임 오류를 숨기면 Medium 이상으로 본다.

Q. API 타입 불일치는 어떤 문제야?
A. response mapping 오류, undefined 접근, 화면 데이터 누락을 만들 수 있다.

Q. TypeScript Review의 최종 목적은 뭐야?
A. 타입을 통해 런타임 오류 가능성을 줄이고 API 변경 영향을 빠르게 감지하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Semantic HTML Review는 뭐야?
A. 프론트엔드 UI가 의미에 맞는 HTML 요소를 사용하고 있는지 검토하는 과정이다.

Q. div에 onClick을 쓰면 안 돼?
A. 버튼 역할이면 button을 사용하는 것이 좋다. div 클릭은 키보드 접근성과 의미 전달에 문제가 생기기 쉽다.

Q. heading 구조도 리뷰해야 해?
A. 해야 한다. heading 구조는 화면 구조 이해, 스크린 리더 탐색, SEO에 영향을 준다.

Q. Keyboard Navigation Review는 뭐야?
A. 사용자가 마우스 없이 키보드만으로 주요 기능을 사용할 수 있는지 검토하는 과정이다.

Q. focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 제거하려면 대체 focus-visible 스타일을 제공해야 한다.

Q. modal이 열릴 때 focus는 어디로 가야 해?
A. modal 내부의 첫 번째 조작 가능한 요소나 modal 제목으로 이동하는 것이 좋다.

Q. Image Alt Review는 뭐야?
A. 이미지에 적절한 대체 텍스트가 제공되는지 검토하는 과정이다.

Q. 모든 이미지에 alt가 필요해?
A. img 요소에는 alt가 필요하다. 정보 이미지는 의미 있는 alt, 장식 이미지는 alt=""를 사용한다.

Q. alt="image"는 괜찮아?
A. 좋지 않다. 이미지가 전달하는 정보나 목적을 설명해야 한다.

Q. ARIA Review는 뭐야?
A. HTML만으로 의미를 충분히 전달하기 어려운 UI에서 aria 속성을 적절하게 사용하는지 검토하는 과정이다.

Q. ARIA는 언제 사용해?
A. semantic HTML만으로 상태나 관계를 충분히 전달하기 어려울 때 사용한다.

Q. aria를 많이 넣으면 접근성이 좋아져?
A. 아니다. semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. Modal Accessibility Review는 뭐야?
A. modal, dialog, popup UI가 키보드와 스크린 리더 환경에서도 안전하게 동작하는지 검토하는 과정이다.

Q. modal에 role="dialog"가 필요해?
A. div 기반 modal이라면 dialog 역할과 aria-modal 설정이 필요하다.

Q. modal 닫힌 후 focus는 어디로 가야 해?
A. modal을 열었던 버튼이나 이전 focus 위치로 복원하는 것이 좋다.

Q. Styling Consistency Review는 뭐야?
A. 프론트엔드 스타일 코드가 프로젝트 규칙에 맞게 일관적으로 작성되었는지 검토하는 과정이다.

Q. inline style은 무조건 나빠?
A. 무조건은 아니지만 반복되는 스타일이나 상태 스타일은 class 또는 styling system으로 분리하는 것이 좋다.

Q. 색상값을 직접 써도 돼?
A. 가능하지만 반복되는 색상은 CSS variable 또는 design token으로 관리하는 것이 좋다.

Q. Responsive Review는 뭐야?
A. 프론트엔드 화면이 모바일, 태블릿, 데스크톱 등 다양한 화면 크기에서 깨지지 않는지 검토하는 과정이다.

Q. Responsive Review에서 가장 먼저 볼 것은 뭐야?
A. 모바일 화면에서 가로 스크롤이 생기는지, 주요 버튼과 텍스트가 사용 가능한지 확인한다.

Q. table은 모바일에서 어떻게 처리해?
A. column 축약, card layout 전환, 또는 wrapper overflow-x 처리를 검토한다.

Q. State Style Review는 뭐야?
A. UI 요소가 hover, active, focus, disabled, selected, error, loading 상태를 시각적으로 명확히 표현하는지 검토하는 과정이다.

Q. disabled 스타일만 있으면 충분해?
A. 아니다. 실제 disabled 속성이나 클릭 guard도 함께 필요하다.

Q. 색상만으로 error를 표시해도 돼?
A. 권장하지 않는다. 텍스트 메시지, 아이콘, aria-invalid 등도 함께 제공하는 것이 좋다.

Q. CSS Naming and Scope Review는 뭐야?
A. className 이름이 역할을 명확히 표현하고 스타일 적용 범위가 예측 가능한지 검토하는 과정이다.

Q. box, title 같은 className은 왜 위험해?
A. 전역 CSS에서 다른 컴포넌트와 충돌하거나 역할을 알기 어렵기 때문이다.

Q. Type Safety Review는 뭐야?
A. TypeScript 타입이 실제 데이터 구조와 일치하고 any 또는 type assertion으로 타입 안전성이 약해지지 않았는지 검토하는 과정이다.

Q. any를 써도 돼?
A. 임시로는 가능하지만 최종 코드에서는 구체적인 타입으로 대체하는 것이 좋다.

Q. API 응답 타입은 꼭 만들어야 해?
A. 권장된다. 응답 구조가 명확해야 화면 코드와 API 변경 영향도를 줄일 수 있다.

Q. API Response Type Review는 뭐야?
A. 백엔드 응답 wrapper, data payload, Page / Slice 구조가 TypeScript 타입으로 정확히 표현되는지 검토하는 과정이다.

Q. ApiResponse generic type은 왜 필요해?
A. 공통 wrapper 구조와 실제 data payload를 함께 안전하게 표현하기 위해 필요하다.

Q. Page와 Slice 타입을 구분해야 해?
A. 그렇다. Page는 total count 정보가 있고 Slice는 hasNext 중심이므로 화면 처리 방식이 다르다.

Q. Null Undefined Review는 뭐야?
A. 값이 없을 수 있는 상황을 TypeScript와 UI 로직에서 안전하게 처리하는지 검토하는 과정이다.

Q. Cannot read properties of undefined 오류는 왜 나?
A. 데이터가 로딩되기 전 undefined 또는 null 값에 접근했기 때문이다.

Q. optional chaining만 쓰면 충분해?
A. 항상 충분하지 않다. 사용자에게 보여줄 fallback UI도 필요하다.

Q. non-null assertion을 써도 돼?
A. 정말 null이 아님을 보장할 수 있을 때만 제한적으로 사용해야 한다.

Q. Event Type Review는 뭐야?
A. React event handler의 event 타입이 명확하게 작성되었는지 검토하는 과정이다.

Q. input onChange 타입은 뭐야?
A. 일반 text input은 React.ChangeEvent<HTMLInputElement>를 사용한다.

Q. form onSubmit 타입은 뭐야?
A. React.FormEvent<HTMLFormElement>를 사용한다.

Q. Type Assertion Review는 뭐야?
A. as 또는 non-null assertion으로 TypeScript 검사를 우회하는 코드가 안전한지 검토하는 과정이다.

Q. as any는 왜 문제야?
A. 해당 값에 대한 타입 검사가 사실상 비활성화되어 런타임 오류를 막기 어렵다.

Q. Accessibility Review에서 가장 먼저 볼 것은 뭐야?
A. 키보드 사용 가능 여부, form label, button / link 역할, modal focus 처리를 먼저 본다.

Q. Styling Review는 취향 리뷰야?
A. 아니다. 일관성, 반응형, 상태 전달, 유지보수성, 접근성 위험을 검토하는 것이다.

Q. TypeScript Review에서 가장 먼저 볼 것은 뭐야?
A. null 접근 위험, API 응답 타입 불일치, any 남용, unsafe assertion을 먼저 본다.

Q. Accessibility Styling TypeScript Review의 최종 목적은 뭐야?
A. 프론트엔드 UI가 접근 가능하고 일관된 스타일을 가지며 타입 안정성으로 런타임 오류를 줄일 수 있는지 판단하는 것이다.
