# Styling Architecture Part06 - Accessibility Styling, Specificity, Override, Utility, Duplication Rules

---

# 1. Accessibility Styling Rules

## 1.1 Accessibility Style

### [개념]

Accessibility Style은 키보드 사용자, 스크린 리더 사용자, 저시력 사용자, 움직임에 민감한 사용자 등 다양한 사용자가 UI를 인식하고 조작할 수 있도록 돕는 스타일 기준이다.

Accessibility Style은 선택 사항이 아니다.

Frontend Agent는 스타일을 생성할 때 접근성 스타일을 제거하지 않아야 한다.

Review Agent는 화면이 예쁜지뿐 아니라 조작 가능성과 상태 인식 가능성을 검토해야 한다.

---

### [핵심]

Accessibility Style 검토 항목:

- focus-visible
- color contrast
- disabled state
- error state
- hover에만 의존하지 않음
- 색상만으로 상태 전달하지 않음
- text underline 제거 시 대체 표시
- reduced motion 대응
- screen reader only class
- touch target size
- keyboard navigation visibility

---

### [실무]

Accessibility Style 예:

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.errorText {
  color: var(--color-error);
}

.errorInput {
  border-color: var(--color-error);
}

.srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

Accessibility Style 리뷰 기준:

```md
- [ ] focus style이 보이는가?
- [ ] error를 색상만으로 표시하지 않는가?
- [ ] disabled 상태가 명확한가?
- [ ] link와 button이 시각적으로 구분되는가?
- [ ] motion 감소 설정을 고려했는가?
- [ ] keyboard 사용자가 현재 위치를 알 수 있는가?
```

---

### [FAQ]

Q. Accessibility Style은 왜 필요해?
A. 다양한 사용자가 UI 상태를 인식하고 키보드나 보조 기술로 조작할 수 있게 하기 위해 필요하다.

Q. 스타일이 예쁘면 접근성은 나중에 봐도 돼?
A. 아니다. 접근성 스타일은 UI 사용 가능성과 직접 연결되므로 초기부터 함께 고려해야 한다.

Q. 에러를 빨간색으로만 표시하면 안 돼?
A. 안 된다. 텍스트 메시지, 아이콘, aria 등 추가 정보가 필요하다.

Q. hover 효과만 있으면 충분해?
A. 아니다. 키보드 사용자를 위한 focus style이 필요하다.

---

## 1.2 Focus Style Rules

### [개념]

Focus Style은 키보드나 보조 기술 사용자가 현재 조작 중인 요소를 알 수 있게 하는 스타일이다.

Focus Style은 접근성에서 가장 중요한 시각적 피드백 중 하나다.

Focus outline을 제거하는 reset은 치명적인 접근성 문제를 만들 수 있다.

---

### [핵심]

Focus Style 기준:

- focus outline 제거 금지
- 제거 시 대체 focus style 제공
- 색상 대비 충분
- button, link, input, select, textarea 모두 확인
- modal 내부 focus 이동 확인
- skip link 고려 가능
- dark mode에서도 focus style 식별 가능
- focus와 hover 상태를 혼동하지 않음

---

### [실무]

권장 Focus Style:

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

나쁜 예:

```css
* {
  outline: none;
}
```

좋은 예:

```css
.button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.input:focus-visible {
  border-color: var(--color-primary);
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

Focus Style 리뷰 기준:

```md
- [ ] focus-visible 스타일이 존재하는가?
- [ ] outline을 무조건 제거하지 않는가?
- [ ] focus style이 배경과 충분히 대비되는가?
- [ ] button, link, input에 focus style이 적용되는가?
- [ ] dark mode에서도 focus style이 보이는가?
```

---

### [FAQ]

Q. focus outline이 디자인상 안 예쁘면 지워도 돼?
A. 지우기만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. focus와 focus-visible 차이는 뭐야?
A. focus는 모든 포커스 상태에 적용되고, focus-visible은 주로 키보드 접근처럼 시각적 표시가 필요한 경우에 적용된다.

Q. hover style이 있으면 focus style은 없어도 돼?
A. 아니다. 키보드 사용자는 hover 상태를 사용할 수 없으므로 focus style이 필요하다.

Q. dark mode에서도 focus style을 확인해야 해?
A. 필요하다. 어두운 배경에서 focus ring이 보이지 않으면 키보드 사용성이 떨어진다.

---

## 1.3 Color Contrast Rules

### [개념]

Color Contrast는 텍스트, 버튼, 아이콘, border, focus ring이 배경과 충분히 구분되는지 판단하는 기준이다.

Color Contrast가 낮으면 사용자가 정보를 읽거나 상태를 구분하기 어렵다.

---

### [핵심]

Contrast 검토 대상:

- body text
- muted text
- link text
- button text
- disabled text
- error text
- focus ring
- border
- icon
- dark mode surface

주의:

- 색상만으로 상태 전달 금지
- disabled opacity 과도하게 낮추지 않음
- dark mode에서 muted text 식별성 확인
- hover / selected 상태 대비 확인
- primary button의 배경과 글자 대비 확인

---

### [실무]

나쁜 예:

```css
.mutedText {
  color: #cccccc;
  background: #ffffff;
}
```

좋은 예:

```css
.mutedText {
  color: var(--color-muted);
}

.errorText {
  color: var(--color-error);
  font-weight: var(--font-weight-medium);
}
```

Contrast 리뷰 기준:

```md
- [ ] 주요 텍스트가 배경과 충분히 구분되는가?
- [ ] muted text가 너무 흐리지 않은가?
- [ ] button text와 background 대비가 충분한가?
- [ ] error, warning, success 상태가 색상 외 정보와 함께 제공되는가?
- [ ] dark mode에서 border와 surface 구분이 가능한가?
```

---

### [FAQ]

Q. Color Contrast는 왜 중요해?
A. 텍스트와 UI 상태를 사용자가 명확히 인식할 수 있어야 하기 때문이다.

Q. disabled는 opacity를 아주 낮게 주면 돼?
A. 과도하게 낮추면 상태를 읽기 어려울 수 있다. 식별 가능한 수준을 유지해야 한다.

Q. 색상만으로 success와 error를 구분해도 돼?
A. 권장하지 않는다. 텍스트, 아이콘, aria 등 추가 단서가 필요하다.

---

## 1.4 Reduced Motion Rules

### [개념]

Reduced Motion은 사용자가 애니메이션 감소를 설정했을 때 과도한 움직임을 줄이는 접근성 기준이다.

움직임이 많은 UI는 일부 사용자에게 불편함을 줄 수 있다.

---

### [핵심]

Reduced Motion 적용 대상:

- page transition
- modal animation
- dropdown animation
- carousel
- auto scrolling
- parallax
- skeleton shimmer
- hover transform
- loading animation

주의:

- transition / animation 남용 금지
- motion이 정보 전달의 유일한 수단이 되면 안 됨
- prefers-reduced-motion 지원 고려
- transform animation이 사용자 흐름을 방해하지 않아야 함

---

### [실무]

Reduced Motion 예:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
    scroll-behavior: auto;
  }
}
```

Transition token과 함께 사용:

```css
.card {
  transition:
    box-shadow var(--transition-fast),
    transform var(--transition-fast);
}

@media (prefers-reduced-motion: reduce) {
  .card {
    transition: none;
  }
}
```

Reduced Motion 리뷰 기준:

```md
- [ ] 움직임이 많은 UI에 reduced motion 대응이 있는가?
- [ ] transition duration이 과도하게 길지 않은가?
- [ ] animation이 사용자 흐름을 방해하지 않는가?
- [ ] carousel / parallax / shimmer 효과가 과하지 않은가?
```

---

### [FAQ]

Q. prefers-reduced-motion은 꼭 필요해?
A. 움직임이 많은 UI라면 필요하다. 일부 사용자는 과도한 motion에 불편을 느낄 수 있다.

Q. 모든 transition을 없애야 해?
A. 사용자 설정이 reduce일 때는 불필요한 motion을 최소화하는 것이 좋다.

Q. hover transform도 reduced motion 대상이야?
A. 과도한 움직임이 있으면 reduced motion에서 줄이거나 제거하는 것이 좋다.

---

# 2. CSS Specificity Rules

## 2.1 Specificity Management

### [개념]

Specificity는 CSS selector의 우선순위다.

Styling Architecture에서는 우선순위가 복잡해지지 않도록 관리해야 한다.

Specificity가 복잡하면 스타일 override가 어려워지고, Agent가 안전한 스타일 코드를 생성하기 어렵다.

---

### [핵심]

권장:

- class 기반 styling
- id selector 스타일링 지양
- 긴 selector chain 지양
- `!important` 남용 금지
- component scope 유지
- override 최소화
- selector 단순화
- CSS Module 또는 naming convention 활용

금지에 가까운 예:

```css
body div main section article div .card .title span {
  color: red;
}
```

---

### [실무]

좋은 구조:

```css
.cardTitle {
  color: var(--color-text);
}
```

나쁜 구조:

```css
.page .container .section .card h2.title {
  color: var(--color-text);
}
```

Specificity 리뷰 기준:

```md
- [ ] selector가 과도하게 깊지 않은가?
- [ ] id selector를 일반 스타일링에 남용하지 않는가?
- [ ] `!important` 사용이 최소화되어 있는가?
- [ ] component scope가 유지되는가?
- [ ] override 없이 token / variant로 해결 가능한가?
```

---

### [FAQ]

Q. CSS Specificity는 왜 관리해야 해?
A. 우선순위가 복잡해지면 스타일 override가 어려워지고 예측하기 힘든 충돌이 생긴다.

Q. CSS가 안 먹으면 !important를 쓰면 돼?
A. 일시 해결은 가능하지만 장기적으로 유지보수를 어렵게 만든다. selector 구조와 우선순위를 먼저 확인해야 한다.

Q. id selector를 스타일링에 쓰면 안 돼?
A. 가능하지만 우선순위가 높아 override가 어려워지므로 일반 스타일링에는 class가 더 적합하다.

---

## 2.2 Selector Depth Rules

### [개념]

Selector Depth는 CSS selector가 얼마나 깊게 연결되어 있는지를 의미한다.

Selector가 깊어질수록 특정 DOM 구조에 강하게 의존하고 override가 어려워진다.

---

### [핵심]

Selector Depth 주의:

- page 구조에 과하게 의존하지 않음
- component 내부 class 직접 targeting 지양
- tag selector chain 남용 금지
- descendant selector 과다 사용 금지
- SCSS nesting 과다 주의
- selector는 가능한 짧고 역할 중심으로 작성

권장:

```css
.cardTitle {
}
```

주의:

```css
.main .section .container .card .header .title {
}
```

---

### [실무]

Selector Depth 판단 Flow:

```text
Style 적용 안 됨
→ selector depth 확인
→ specificity 확인
→ 더 단순한 class로 대체 가능 여부 확인
→ component scope 확인
→ naming 개선
```

리뷰 기준:

```md
- [ ] selector depth가 불필요하게 깊지 않은가?
- [ ] DOM 구조 변경 시 스타일이 쉽게 깨지지 않는가?
- [ ] SCSS nesting으로 결과 selector가 길어지지 않는가?
- [ ] 다른 컴포넌트 내부 구조를 직접 참조하지 않는가?
```

---

### [FAQ]

Q. selector가 깊으면 왜 문제야?
A. DOM 구조에 강하게 의존하고 우선순위가 높아져 수정과 override가 어려워진다.

Q. SCSS nesting을 쓰면 selector depth가 깊어지기 쉬워?
A. 그렇다. 작성은 편하지만 결과 CSS가 길고 복잡해질 수 있다.

Q. selector depth를 줄이는 방법은 뭐야?
A. 역할 기반 class를 직접 부여하고 component scope를 유지하는 것이 좋다.

---

# 3. Override Rules

## 3.1 Override Policy

### [개념]

Override는 기존 스타일을 다른 스타일로 덮어쓰는 것이다.

Override는 필요한 경우가 있지만, 무분별한 override는 CSS 구조를 불안정하게 만든다.

Styling Architecture에서는 override 순서와 허용 범위를 명확히 해야 한다.

---

### [핵심]

Override가 필요한 경우:

- 외부 라이브러리 스타일 조정
- theme별 스타일 변경
- variant 스타일 적용
- 특정 page에서 spacing 조정
- responsive style 변경
- 상태 스타일 적용

주의할 경우:

- 다른 컴포넌트 내부 class 직접 수정
- 전역 selector로 강제 override
- `!important` 사용
- 깊은 selector chain 사용
- 의도하지 않은 side effect 발생

---

### [실무]

권장 override 순서:

```text
Token 변경
→ Variant 추가
→ Props 기반 style
→ Local class override
→ Global override 최소화
→ !important 최후 수단
```

Override 리뷰 기준:

```md
- [ ] token 변경으로 해결 가능한 문제인가?
- [ ] variant 추가가 더 적합하지 않은가?
- [ ] global override가 필요한 이유가 명확한가?
- [ ] override 범위가 안전한가?
- [ ] !important 없이 해결 가능한가?
```

---

### [FAQ]

Q. Override는 나쁜 거야?
A. 필요한 경우가 있지만 범위와 이유가 명확해야 한다.

Q. 외부 라이브러리 스타일은 어떻게 수정해?
A. 가능하면 라이브러리의 theme API나 className override API를 먼저 사용한다.

Q. !important는 절대 금지야?
A. 절대 금지는 아니지만 최후 수단으로만 사용해야 한다.

---

## 3.2 Global Override Warning

### [개념]

Global Override Warning은 전역 selector로 스타일을 강제로 덮어써서 다른 화면이나 컴포넌트에 부작용을 만드는 문제를 방지하는 규칙이다.

Global Override는 영향 범위가 넓기 때문에 최소화해야 한다.

---

### [핵심]

위험한 global override:

```css
button {
  width: 100%;
}

.card {
  margin-bottom: 24px;
}

input {
  border: 1px solid red;
}

* {
  outline: none;
}
```

허용 가능한 global baseline:

```css
button,
input,
textarea,
select {
  font: inherit;
}

img {
  max-width: 100%;
  display: block;
}
```

Global Override 위험:

- 모든 컴포넌트에 의도치 않은 영향
- UI library 스타일 충돌
- component variant 무력화
- 접근성 스타일 제거
- 디버깅 어려움

---

### [실무]

Global override 검토 Flow:

```text
Global Style 변경 요청
→ 전체 앱에 적용되어도 안전한가?
→ 특정 component 문제인가?
→ token / component style로 해결 가능한가?
→ 영향 범위 검토
→ 최소 selector 적용
```

리뷰 기준:

```md
- [ ] 전역 selector가 특정 컴포넌트 문제를 해결하려는 용도로 쓰이지 않는가?
- [ ] 모든 button, input에 적용되어도 안전한가?
- [ ] focus / disabled / hover 상태를 깨뜨리지 않는가?
- [ ] UI library와 충돌하지 않는가?
```

---

### [FAQ]

Q. button 전역 스타일을 바꿔도 돼?
A. 기본 font inherit 같은 baseline은 가능하지만 width, color, variant 같은 컴포넌트 스타일은 신중해야 한다.

Q. global override가 많으면 뭐가 문제야?
A. 의도하지 않은 side effect가 생기고 어떤 스타일이 어디서 적용되는지 추적하기 어려워진다.

Q. 특정 컴포넌트만 수정하려면 어떻게 해?
A. 해당 컴포넌트의 local class, variant, props 기반 스타일로 수정하는 것이 좋다.

---

## 3.3 Third-party UI Library Styling

### [개념]

Third-party UI Library Styling은 외부 UI 라이브러리의 기본 스타일을 프로젝트 디자인에 맞게 조정하는 방식이다.

예:

- MUI
- Ant Design
- Bootstrap
- Chakra UI
- Radix UI
- Headless UI

외부 라이브러리 스타일은 무작정 CSS로 덮어쓰기보다 라이브러리가 제공하는 theme API와 override API를 우선 사용해야 한다.

---

### [핵심]

검토 항목:

- theme API 사용 여부
- component props 사용 여부
- slot / className API 사용 여부
- 전역 override 남용 여부
- class selector 강제 override 여부
- design token과 연결 여부
- bundle size 영향
- accessibility 기본 제공 여부
- custom component와 스타일 일관성

---

### [실무]

권장 override 순서:

```text
Library Theme API
→ Component Props
→ Slot / className API
→ Local wrapper style
→ Global override 최소화
```

나쁜 예:

```css
.ant-btn {
  background: red !important;
}
```

좋은 방향:

```text
라이브러리 theme 설정 확인
→ Button variant / token 연결
→ 필요한 경우 local wrapper class 적용
→ global override는 제한적으로 사용
```

리뷰 기준:

```md
- [ ] 라이브러리 theme API를 먼저 확인했는가?
- [ ] 전역 class override를 남용하지 않는가?
- [ ] 프로젝트 token과 라이브러리 theme이 연결되는가?
- [ ] custom component와 UI library component 스타일이 일관적인가?
```

---

### [FAQ]

Q. UI 라이브러리 스타일은 그냥 CSS로 덮어써도 돼?
A. 가능하지만 theme API나 component props를 먼저 사용하는 것이 안전하다.

Q. 외부 UI 라이브러리를 쓰면 Styling Architecture가 필요 없어?
A. 아니다. theme, override, custom component와의 일관성 기준이 필요하다.

Q. 라이브러리 class에 !important를 쓰면 안 돼?
A. 최후 수단으로만 사용해야 한다. 먼저 theme API와 override API를 확인해야 한다.

---

# 4. Utility Class Rules

## 4.1 Utility Class

### [개념]

Utility Class는 하나의 작은 스타일 역할을 수행하는 재사용 class다.

Utility Class는 컴포넌트 스타일을 대체하는 것이 아니라 반복되는 작은 보조 스타일을 관리하는 방식이다.

예:

- sr-only
- text-center
- container
- flex-center
- visually-hidden
- stack
- cluster

---

### [핵심]

Utility Class 적합 대상:

- screen reader only
- visually hidden
- text alignment
- flex center
- layout helper
- spacing helper
- container helper
- simple display helper

주의:

- utility class가 너무 많으면 관리 체계 필요
- 컴포넌트 스타일을 utility로 과도하게 조합하지 않음
- 의미 있는 component class와 균형 필요
- Tailwind와 유사한 체계를 직접 만들 때는 범위 제한 필요

---

### [실무]

Utility Class 예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}

.flexCenter {
  display: flex;
  align-items: center;
  justify-content: center;
}

.srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

Utility Class 리뷰 기준:

```md
- [ ] utility class의 역할이 작고 명확한가?
- [ ] component style을 utility 조합으로 과도하게 대체하지 않는가?
- [ ] utility class naming이 일관적인가?
- [ ] 접근성 utility가 안전하게 작성되어 있는가?
```

---

### [FAQ]

Q. Utility Class는 뭐야?
A. text-center, sr-only, container, flex-center처럼 작은 스타일 역할을 수행하는 재사용 class다.

Q. Utility class를 직접 만들어도 돼?
A. 가능하다. 다만 프로젝트 전체에서 일관된 규칙이 있어야 한다.

Q. Utility class가 많아지면 문제야?
A. 관리 체계 없이 많아지면 중복과 혼란이 생긴다. Tailwind 같은 체계를 쓰거나 범위를 제한해야 한다.

---

## 4.2 Utility vs Component Style

### [개념]

Utility Style은 작은 보조 스타일이고, Component Style은 특정 UI 컴포넌트의 외형과 상태를 정의하는 스타일이다.

두 책임을 섞으면 스타일 위치와 의미가 불명확해진다.

---

### [핵심]

Utility Style에 적합:

- `.container`
- `.srOnly`
- `.textCenter`
- `.flexCenter`
- `.stack`
- `.cluster`

Component Style에 적합:

- `.button`
- `.card`
- `.modal`
- `.input`
- `.toast`
- `.dropdown`

주의:

- button 디자인을 utility class 조합으로 반복 작성하지 않음
- card 디자인을 여러 페이지에서 utility 조합으로 복사하지 않음
- 반복되는 UI 구조는 component로 분리
- 반복되는 layout 구조는 layout utility 또는 layout component로 분리

---

### [실무]

나쁜 예:

```html
<button class="flexCenter textCenter rounded shadow primaryBg largePadding">
  저장
</button>
```

좋은 예:

```html
<button class="button button--primary">저장</button>
```

분리 기준:

```text
작은 단일 역할
→ Utility

반복되는 UI 구조 + 상태 + 의미
→ Component

반복되는 배치 구조
→ Layout Utility 또는 Layout Component
```

---

### [FAQ]

Q. Utility class만으로 컴포넌트를 만들면 안 돼?
A. 가능하지만 반복되는 UI라면 컴포넌트 스타일로 분리하는 것이 유지보수에 좋다.

Q. container는 utility야 component야?
A. 보통 layout utility에 가깝다.

Q. sr-only는 어디에 두는 게 좋아?
A. 전역 utilities.css에 두는 것이 일반적이다.

---

# 5. Style Duplication Rules

## 5.1 Style Duplication

### [개념]

Style Duplication은 같은 스타일 패턴이 여러 파일에 반복 작성되는 문제다.

Style Duplication은 UI 일관성을 깨뜨리고 수정 범위를 넓히며 Agent가 서로 다른 스타일을 생성하게 만드는 원인이 된다.

---

### [핵심]

중복이 자주 발생하는 대상:

- button style
- card style
- input style
- modal layout
- page container
- section spacing
- typography
- color
- shadow
- radius
- z-index
- responsive breakpoint

중복 해결 우선순위:

```text
반복되는 디자인 값
→ token으로 분리

반복되는 UI 구조
→ component로 분리

반복되는 layout
→ layout component 또는 utility로 분리

반복되는 class 조합
→ variant 또는 helper로 분리
```

---

### [실무]

나쁜 예:

```css
.noticeCard {
  padding: 16px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}

.reviewCard {
  padding: 16px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}
```

좋은 예:

```css
.card {
  padding: var(--spacing-4);
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
}
```

Duplication 리뷰 기준:

```md
- [ ] 같은 color, spacing, radius가 반복되지 않는가?
- [ ] 같은 button / card / input 스타일이 여러 파일에 복사되지 않는가?
- [ ] 반복되는 layout이 page마다 중복 작성되지 않는가?
- [ ] 중복이 우연히 같은 것인지 의미상 같은 패턴인지 구분했는가?
```

---

### [FAQ]

Q. Style Duplication은 뭐야?
A. 같은 스타일 패턴이 여러 파일에 반복 작성되는 문제다.

Q. 중복 스타일은 무조건 공통화해야 해?
A. 무조건은 아니다. 우연히 같은 스타일인지, 의미상 같은 패턴인지 구분해야 한다.

Q. 언제 컴포넌트로 분리해야 해?
A. 같은 UI 구조와 행동이 반복될 때 컴포넌트로 분리하는 것이 좋다.

---

## 5.2 Duplication Resolution Flow

### [개념]

Duplication Resolution Flow는 중복 스타일을 발견했을 때 token, component, layout, utility 중 어디로 분리할지 판단하는 절차다.

중복을 발견했다고 즉시 공통화하면 안 된다.

의미와 변경 방향을 먼저 확인해야 한다.

---

### [핵심]

공통화 판단 기준:

```text
3회 이상 반복
+ 의미가 같음
+ 변경 방향이 같음
+ 재사용 가능성이 있음
→ 공통화 고려
```

공통화 보류 기준:

```text
모양만 우연히 비슷함
도메인 의미가 다름
변경 방향이 다름
조건 분기가 더 복잡해짐
한 번만 사용됨
```

---

### [실무]

Duplication Resolution Flow:

```text
중복 스타일 발견
→ 반복 횟수 확인
→ 의미 동일 여부 확인
→ 변경 방향 동일 여부 확인
→ 디자인 값 중복이면 token
→ UI 구조 중복이면 component
→ layout 중복이면 layout utility
→ class 조합 중복이면 variant/helper
→ 과한 공통화 여부 검토
```

예:

```text
#2563eb 반복
→ --color-primary token

padding 16px + border + radius 반복
→ Card component 또는 card class

page container 반복
→ container utility

button primary / danger 반복
→ Button variant
```

---

### [FAQ]

Q. 중복이 보이면 바로 공통화해야 해?
A. 아니다. 의미와 변경 방향이 같은지 확인한 뒤 공통화해야 한다.

Q. 반복 색상은 어디로 빼야 해?
A. color token으로 분리하는 것이 좋다.

Q. 반복 layout은 어디로 빼야 해?
A. layout utility 또는 layout component로 분리하는 것이 좋다.

---

## 5.3 Over-Abstraction Warning

### [개념]

Over-Abstraction은 공통화를 지나치게 많이 해서 오히려 수정과 이해가 어려워지는 문제다.

중복 제거는 중요하지만, 모든 비슷한 코드를 무조건 하나로 합치면 컴포넌트 복잡도가 증가한다.

---

### [핵심]

과한 공통화 징후:

- props가 너무 많음
- variant 조합이 폭발함
- 작은 차이 때문에 조건문이 많음
- 공통 컴포넌트 수정 시 영향 범위가 너무 큼
- 실제로는 다른 UI인데 억지로 하나로 합침
- component API가 불명확함
- Review Agent가 영향 범위를 판단하기 어려움

공통화 보류 상황:

- 모양만 우연히 비슷함
- 도메인 의미가 다름
- 변경 방향이 다름
- 조건 분기가 더 복잡해짐
- 재사용 가능성이 낮음

---

### [실무]

나쁜 예:

```text
UniversalCard props:
type
variant
size
hasImage
hasFooter
hasBadge
isNotice
isReview
isProduct
isCompact
isFeatured
```

좋은 방향:

```text
BaseCard
→ 공통 padding / border / radius

NoticeCard
→ notice 도메인 구조

ReviewCard
→ review 도메인 구조

ProductCard
→ product 도메인 구조
```

Over-Abstraction 리뷰 기준:

```md
- [ ] 공통 컴포넌트 props가 과도하지 않은가?
- [ ] 서로 다른 UI를 억지로 하나로 합치지 않았는가?
- [ ] variant 조합이 폭발하지 않는가?
- [ ] 분리하는 것이 더 명확하지 않은가?
```

---

### [FAQ]

Q. Over-Abstraction은 뭐야?
A. 공통화를 지나치게 많이 해서 props와 variant가 복잡해지고 오히려 수정이 어려워지는 문제다.

Q. 공통 컴포넌트가 너무 복잡해지면 어떻게 해?
A. variant를 정리하거나 도메인별 컴포넌트로 분리하는 것이 좋다.

Q. 중복 제거와 과한 공통화 중 뭐가 더 위험해?
A. 둘 다 위험하다. 의미와 변경 방향이 같은 중복만 공통화하는 것이 좋다.

---

# 6. Animation and Transition Rules

## 6.1 Transition Rules

### [개념]

Transition은 상태 변화가 부드럽게 보이도록 CSS 속성 변화를 시간에 따라 처리하는 방식이다.

Transition은 사용성을 돕는 수준으로 제한해야 하며, 과도한 motion은 피해야 한다.

---

### [핵심]

Transition 적합 대상:

- button hover
- link hover
- modal open
- dropdown open
- opacity
- transform
- background color
- border color
- box-shadow

주의 대상:

- width / height transition 남용
- layout shift 유발
- 긴 animation
- motion sickness 유발
- prefers-reduced-motion 미고려
- transition all 남용

---

### [실무]

Transition 예:

```css
.button {
  transition:
    background-color var(--transition-fast),
    transform var(--transition-fast);
}

.button:hover {
  background: var(--color-primary-hover);
}
```

나쁜 예:

```css
.card {
  transition: all 1s ease;
}
```

Transition 리뷰 기준:

```md
- [ ] transition 대상 속성이 명확한가?
- [ ] transition all을 남용하지 않는가?
- [ ] duration이 과하게 길지 않은가?
- [ ] layout shift를 유발하지 않는가?
- [ ] reduced motion 대응이 필요한가?
```

---

### [FAQ]

Q. 애니메이션은 많을수록 좋아?
A. 아니다. 사용성을 돕는 정도로 제한해야 한다.

Q. transition도 token으로 관리해야 해?
A. 반복 사용되는 duration과 easing은 token으로 관리하면 일관성에 좋다.

Q. transition all은 왜 안 좋아?
A. 의도하지 않은 속성까지 transition되어 성능과 예측 가능성이 떨어질 수 있다.

---

# 7. Agent Accessibility, Specificity, Duplication Rules

## 7.1 Frontend Agent Rules

### [개념]

Frontend Agent는 스타일 코드를 생성할 때 accessibility, specificity, override, utility, duplication 기준을 함께 적용해야 한다.

Frontend Agent는 접근성 스타일을 제거하거나, 깊은 selector와 global override로 문제를 해결하면 안 된다.

---

### [핵심]

Frontend Agent 생성 규칙:

- focus-visible 유지
- error state는 색상만으로 전달하지 않음
- disabled는 attribute와 style 함께 처리
- reduced motion 고려
- selector depth 최소화
- `!important` 남용 금지
- global override 최소화
- token / variant 우선
- utility와 component style 책임 분리
- 중복 스타일은 token / component / layout utility로 분리
- 과한 공통화 지양

---

### [실무]

Frontend Agent 작업 Flow:

```text
Style Request
→ Accessibility State 확인
→ Focus / Disabled / Error 처리
→ Selector 단순화
→ Token / Variant로 해결 가능 여부 확인
→ Utility / Component 책임 분리
→ Duplication 확인
→ Reduced Motion 필요 여부 확인
→ Review Agent 전달
```

생성 금지에 가까운 예:

```text
* { outline: none; }
!important 남용
body div main section .card .title 같은 깊은 selector
global.css에 특정 component override 추가
error를 red color만으로 표현
disabled를 class만으로 처리
transition: all 1s
```

---

### [FAQ]

Q. Frontend Agent가 CSS가 안 먹을 때 !important를 써도 돼?
A. 최후 수단으로만 사용해야 한다. 먼저 selector, import order, specificity를 확인해야 한다.

Q. Frontend Agent가 focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible 스타일을 제공해야 한다.

Q. Frontend Agent가 중복 스타일을 발견하면 바로 공통화해야 해?
A. 아니다. 의미와 변경 방향이 같은지 확인한 뒤 token, component, layout utility로 분리해야 한다.

---

## 7.2 Review Agent Rules

### [개념]

Review Agent는 접근성 스타일, specificity, override, utility, duplication 문제가 없는지 검토한다.

Review Agent는 단순 화면 결과가 아니라 유지보수성과 사용 가능성을 함께 판단해야 한다.

---

### [핵심]

Review Agent 검토 항목:

- focus-visible 존재 여부
- disabled attribute 사용 여부
- error message 제공 여부
- color contrast
- reduced motion 대응 여부
- selector depth
- `!important` 남용 여부
- global override 남용 여부
- third-party override 안전성
- utility class 범위
- style duplication
- over-abstraction
- transition all 남용 여부

---

### [실무]

Review Agent 판단 Flow:

```text
Accessibility 확인
→ Focus / Disabled / Error 확인
→ Specificity 확인
→ Override 범위 확인
→ Utility 책임 확인
→ Duplication 확인
→ Over-Abstraction 확인
→ Transition / Motion 확인
→ Final Review
```

Review 결과 기준:

```text
Approved
→ 접근성 상태 OK + selector 단순 + override 안전 + 중복 관리 OK

Needs Fix
→ 일부 focus 누락, raw value 반복, utility 범위 불명확

Rejected
→ focus 제거, disabled attribute 누락, !important 남용, global override 오염, 접근성 심각
```

---

### [FAQ]

Q. Review Agent는 accessibility style도 봐야 해?
A. 반드시 봐야 한다. focus, disabled, error, contrast는 UI 사용 가능성과 직접 연결된다.

Q. Review Agent는 specificity를 왜 봐야 해?
A. specificity가 복잡하면 유지보수가 어려워지고 이후 스타일 수정이 위험해진다.

Q. 화면상 문제없으면 duplication은 넘어가도 돼?
A. 아니다. 반복 스타일은 수정 비용과 Agent 생성 품질에 영향을 준다.

---

# 8. Part06 Quality Checklist

## 8.1 Accessibility, Specificity, Utility, Duplication Checklist

### [개념]

Part06 단계에서는 Accessibility Styling, CSS Specificity, Override, Utility Class, Style Duplication 기준이 명확한지 검토한다.

이 단계는 스타일 코드의 사용 가능성, 유지보수성, 충돌 방지, 중복 관리 품질을 결정한다.

---

### [핵심]

Part06 체크리스트:

```md
## Accessibility

- [ ] focus-visible 기준이 있는가?
- [ ] outline 제거 경고가 있는가?
- [ ] error state가 색상만으로 전달되지 않는가?
- [ ] disabled state가 attribute와 연결되는가?
- [ ] color contrast 기준이 있는가?
- [ ] reduced motion 기준이 있는가?

## Specificity

- [ ] selector depth 경고가 있는가?
- [ ] id selector 남용 경고가 있는가?
- [ ] !important 남용 경고가 있는가?
- [ ] class 기반 styling 기준이 있는가?

## Override

- [ ] override 순서가 명확한가?
- [ ] global override warning이 있는가?
- [ ] third-party UI library override 기준이 있는가?

## Utility

- [ ] utility class 책임이 명확한가?
- [ ] utility와 component style이 구분되는가?
- [ ] sr-only 같은 accessibility utility가 포함되어 있는가?

## Duplication

- [ ] style duplication 해결 기준이 있는가?
- [ ] token / component / layout utility 분리 기준이 있는가?
- [ ] over-abstraction warning이 있는가?

## Agent Review

- [ ] Frontend Agent 생성 규칙이 있는가?
- [ ] Review Agent 검토 규칙이 있는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Part06 승인 기준:

```text
Accessibility 기준 명확
+ Specificity / Override 기준 명확
+ Utility 책임 명확
+ Duplication 해결 기준 포함
+ Over-Abstraction Warning 포함
+ Agent 생성 / 검토 기준 포함
+ FAQ 충분
+ Retrieval Queries 포함
→ Part06 승인 가능
```

Part06 보류 기준:

```text
focus 제거 허용
또는 error를 색상만으로 처리
또는 !important 남용 허용
또는 global override 기준 없음
또는 duplication / over-abstraction 기준 없음
또는 Agent 검토 기준 부족
→ 재작성 필요
```

---

### [FAQ]

Q. Part06의 핵심 목적은 뭐야?
A. 접근성 스타일, CSS 우선순위, override, utility, 중복 관리 기준을 고정해 스타일 코드의 유지보수성과 사용 가능성을 높이는 것이다.

Q. Part06에서 가장 위험한 문제는 뭐야?
A. focus 제거, error 색상 단독 표현, !important 남용, global override 오염, 중복 스타일 방치다.

Q. Part06 다음에는 뭘 다루는 게 자연스러워?
A. File Structure, Import Order, Troubleshooting, Review Agent Rules, Frontend Agent Rules, PM Agent Rules를 다루는 것이 자연스럽다.

---

# Retrieval Queries

### [FAQ]

Q. Accessibility Style은 뭐야?
A. 키보드 사용자, 스크린 리더 사용자, 저시력 사용자 등 다양한 사용자가 UI를 인식하고 조작할 수 있도록 돕는 스타일 기준이다.

Q. Accessibility Style은 왜 필요해?
A. 다양한 사용자가 UI 상태를 인식하고 키보드나 보조 기술로 조작할 수 있게 하기 위해 필요하다.

Q. Focus Style은 뭐야?
A. 키보드나 보조 기술 사용자가 현재 조작 중인 요소를 알 수 있게 하는 스타일이다.

Q. focus outline이 디자인상 안 예쁘면 지워도 돼?
A. 지우기만 하면 안 된다. 반드시 대체 focus style을 제공해야 한다.

Q. focus와 focus-visible 차이는 뭐야?
A. focus는 모든 포커스 상태에 적용되고, focus-visible은 주로 키보드 접근처럼 시각적 표시가 필요한 경우에 적용된다.

Q. hover style이 있으면 focus style은 없어도 돼?
A. 아니다. 키보드 사용자는 hover 상태를 사용할 수 없으므로 focus style이 필요하다.

Q. dark mode에서도 focus style을 확인해야 해?
A. 필요하다. 어두운 배경에서 focus ring이 보이지 않으면 키보드 사용성이 떨어진다.

Q. Color Contrast는 뭐야?
A. 텍스트, 버튼, 아이콘, border, focus ring이 배경과 충분히 구분되는지 판단하는 기준이다.

Q. Color Contrast는 왜 중요해?
A. 텍스트와 UI 상태를 사용자가 명확히 인식할 수 있어야 하기 때문이다.

Q. disabled는 opacity를 아주 낮게 주면 돼?
A. 과도하게 낮추면 상태를 읽기 어려울 수 있다. 식별 가능한 수준을 유지해야 한다.

Q. 색상만으로 success와 error를 구분해도 돼?
A. 권장하지 않는다. 텍스트, 아이콘, aria 등 추가 단서가 필요하다.

Q. Reduced Motion은 뭐야?
A. 사용자가 애니메이션 감소를 설정했을 때 과도한 움직임을 줄이는 접근성 기준이다.

Q. prefers-reduced-motion은 꼭 필요해?
A. 움직임이 많은 UI라면 필요하다. 일부 사용자는 과도한 motion에 불편을 느낄 수 있다.

Q. 모든 transition을 없애야 해?
A. 사용자 설정이 reduce일 때는 불필요한 motion을 최소화하는 것이 좋다.

Q. CSS Specificity는 뭐야?
A. CSS selector의 우선순위다.

Q. CSS Specificity는 왜 관리해야 해?
A. 우선순위가 복잡해지면 스타일 override가 어려워지고 예측하기 힘든 충돌이 생긴다.

Q. CSS가 안 먹으면 !important를 쓰면 돼?
A. 일시 해결은 가능하지만 장기적으로 유지보수를 어렵게 만든다. selector 구조와 우선순위를 먼저 확인해야 한다.

Q. id selector를 스타일링에 써도 돼?
A. 가능하지만 우선순위가 높아 override가 어려워지므로 일반 스타일링에는 class가 더 적합하다.

Q. Selector Depth는 뭐야?
A. CSS selector가 얼마나 깊게 연결되어 있는지를 의미한다.

Q. selector가 깊으면 왜 문제야?
A. DOM 구조에 강하게 의존하고 우선순위가 높아져 수정과 override가 어려워진다.

Q. SCSS nesting을 쓰면 selector depth가 깊어지기 쉬워?
A. 그렇다. 작성은 편하지만 결과 CSS가 길고 복잡해질 수 있다.

Q. selector depth를 줄이는 방법은 뭐야?
A. 역할 기반 class를 직접 부여하고 component scope를 유지하는 것이 좋다.

Q. Override는 뭐야?
A. 기존 스타일을 다른 스타일로 덮어쓰는 것이다.

Q. Override는 나쁜 거야?
A. 필요한 경우가 있지만 범위와 이유가 명확해야 한다.

Q. Override 권장 순서는 뭐야?
A. Token 변경 → Variant 추가 → Props 기반 style → Local class override → Global override 최소화 → !important 최후 수단 순서가 좋다.

Q. 외부 라이브러리 스타일은 어떻게 수정해?
A. 가능하면 라이브러리의 theme API나 className override API를 먼저 사용한다.

Q. !important는 절대 금지야?
A. 절대 금지는 아니지만 최후 수단으로만 사용해야 한다.

Q. Global Override는 왜 위험해?
A. 모든 컴포넌트에 의도치 않은 영향을 주고 디버깅과 유지보수를 어렵게 만든다.

Q. button 전역 스타일을 바꿔도 돼?
A. 기본 font inherit 같은 baseline은 가능하지만 width, color, variant 같은 컴포넌트 스타일은 신중해야 한다.

Q. 특정 컴포넌트만 수정하려면 어떻게 해?
A. 해당 컴포넌트의 local class, variant, props 기반 스타일로 수정하는 것이 좋다.

Q. Third-party UI Library Styling은 뭐야?
A. 외부 UI 라이브러리의 기본 스타일을 프로젝트 디자인에 맞게 조정하는 방식이다.

Q. UI 라이브러리 스타일은 그냥 CSS로 덮어써도 돼?
A. 가능하지만 theme API나 component props를 먼저 사용하는 것이 안전하다.

Q. 외부 UI 라이브러리를 쓰면 Styling Architecture가 필요 없어?
A. 아니다. theme, override, custom component와의 일관성 기준이 필요하다.

Q. Utility Class는 뭐야?
A. text-center, sr-only, container, flex-center처럼 작은 스타일 역할을 수행하는 재사용 class다.

Q. Utility class를 직접 만들어도 돼?
A. 가능하다. 다만 프로젝트 전체에서 일관된 규칙이 있어야 한다.

Q. Utility class가 많아지면 문제야?
A. 관리 체계 없이 많아지면 중복과 혼란이 생긴다. Tailwind 같은 체계를 쓰거나 범위를 제한해야 한다.

Q. Utility Style과 Component Style 차이는 뭐야?
A. Utility Style은 작은 보조 스타일이고 Component Style은 특정 UI 컴포넌트의 외형과 상태를 정의하는 스타일이다.

Q. Utility class만으로 컴포넌트를 만들면 안 돼?
A. 가능하지만 반복되는 UI라면 컴포넌트 스타일로 분리하는 것이 유지보수에 좋다.

Q. container는 utility야 component야?
A. 보통 layout utility에 가깝다.

Q. sr-only는 어디에 두는 게 좋아?
A. 전역 utilities.css에 두는 것이 일반적이다.

Q. Style Duplication은 뭐야?
A. 같은 스타일 패턴이 여러 파일에 반복 작성되는 문제다.

Q. Style Duplication은 왜 문제야?
A. UI 일관성을 깨뜨리고 수정 범위를 넓히며 Agent가 서로 다른 스타일을 생성하게 만들 수 있다.

Q. 중복 스타일은 무조건 공통화해야 해?
A. 무조건은 아니다. 우연히 같은 스타일인지, 의미상 같은 패턴인지 구분해야 한다.

Q. 언제 컴포넌트로 분리해야 해?
A. 같은 UI 구조와 행동이 반복될 때 컴포넌트로 분리하는 것이 좋다.

Q. 중복 해결 우선순위는 뭐야?
A. 디자인 값은 token, UI 구조는 component, layout은 layout utility, class 조합은 variant/helper로 분리한다.

Q. 중복이 보이면 바로 공통화해야 해?
A. 아니다. 의미와 변경 방향이 같은지 확인한 뒤 공통화해야 한다.

Q. 반복 색상은 어디로 빼야 해?
A. color token으로 분리하는 것이 좋다.

Q. 반복 layout은 어디로 빼야 해?
A. layout utility 또는 layout component로 분리하는 것이 좋다.

Q. Over-Abstraction은 뭐야?
A. 공통화를 지나치게 많이 해서 props와 variant가 복잡해지고 오히려 수정이 어려워지는 문제다.

Q. 공통 컴포넌트가 너무 복잡해지면 어떻게 해?
A. variant를 정리하거나 도메인별 컴포넌트로 분리하는 것이 좋다.

Q. 중복 제거와 과한 공통화 중 뭐가 더 위험해?
A. 둘 다 위험하다. 의미와 변경 방향이 같은 중복만 공통화하는 것이 좋다.

Q. Transition은 뭐야?
A. 상태 변화가 부드럽게 보이도록 CSS 속성 변화를 시간에 따라 처리하는 방식이다.

Q. 애니메이션은 많을수록 좋아?
A. 아니다. 사용성을 돕는 정도로 제한해야 한다.

Q. transition도 token으로 관리해야 해?
A. 반복 사용되는 duration과 easing은 token으로 관리하면 일관성에 좋다.

Q. transition all은 왜 안 좋아?
A. 의도하지 않은 속성까지 transition되어 성능과 예측 가능성이 떨어질 수 있다.

Q. Frontend Agent가 CSS가 안 먹을 때 !important를 써도 돼?
A. 최후 수단으로만 사용해야 한다. 먼저 selector, import order, specificity를 확인해야 한다.

Q. Frontend Agent가 focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible 스타일을 제공해야 한다.

Q. Frontend Agent가 중복 스타일을 발견하면 바로 공통화해야 해?
A. 아니다. 의미와 변경 방향이 같은지 확인한 뒤 token, component, layout utility로 분리해야 한다.

Q. Review Agent는 accessibility style도 봐야 해?
A. 반드시 봐야 한다. focus, disabled, error, contrast는 UI 사용 가능성과 직접 연결된다.

Q. Review Agent는 specificity를 왜 봐야 해?
A. specificity가 복잡하면 유지보수가 어려워지고 이후 스타일 수정이 위험해진다.

Q. 화면상 문제없으면 duplication은 넘어가도 돼?
A. 아니다. 반복 스타일은 수정 비용과 Agent 생성 품질에 영향을 준다.

Q. Part06의 핵심 목적은 뭐야?
A. 접근성 스타일, CSS 우선순위, override, utility, 중복 관리 기준을 고정해 스타일 코드의 유지보수성과 사용 가능성을 높이는 것이다.

Q. Part06에서 가장 위험한 문제는 뭐야?
A. focus 제거, error 색상 단독 표현, !important 남용, global override 오염, 중복 스타일 방치다.

Q. Part06 다음에는 뭘 다루는 게 자연스러워?
A. File Structure, Import Order, Troubleshooting, Review Agent Rules, Frontend Agent Rules, PM Agent Rules를 다루는 것이 자연스럽다.
