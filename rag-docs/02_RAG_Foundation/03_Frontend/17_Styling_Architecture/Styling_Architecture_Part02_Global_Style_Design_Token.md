# Styling Architecture Part02 - Global Style, Reset, Design Token

---

# 1. Global Style Rules

## 1.1 Global Style

### [개념]

Global Style은 애플리케이션 전체에 적용되는 기본 스타일이다.

Global Style은 특정 컴포넌트 디자인을 작성하는 위치가 아니다.

Global Style의 목적:

- 브라우저 기본 스타일 차이 감소
- 앱 전체 기본 폰트 설정
- 앱 전체 기본 배경 설정
- 앱 전체 기본 텍스트 색상 설정
- CSS Variable 로드
- 기본 element 스타일 정리
- 전역 accessibility baseline 유지

---

### [핵심]

Global Style에 넣기 적합한 것:

- box-sizing
- body margin reset
- font-family
- background color
- text color
- root CSS variables
- a 기본 스타일
- img 기본 스타일
- button font inherit
- form element font inherit
- typography base

Global Style에 넣기 부적합한 것:

- 특정 Card 디자인
- 특정 Modal 디자인
- 특정 Page layout
- 특정 Button variant
- 특정 Form field spacing
- 특정 Header layout
- 특정 Sidebar layout
- 특정 컴포넌트 hover style

---

### [실무]

권장 Global Style 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: var(--font-family-base);
  color: var(--color-text);
  background: var(--color-background);
}

img {
  max-width: 100%;
  display: block;
}

button,
input,
textarea,
select {
  font: inherit;
}

a {
  color: inherit;
}
```

Global Style 리뷰 기준:

```md
- [ ] 전역 스타일이 너무 많은 책임을 갖지 않는가?
- [ ] 특정 컴포넌트 스타일이 global에 들어가지 않았는가?
- [ ] reset이 접근성 스타일을 제거하지 않는가?
- [ ] CSS variable이 root에 정의되어 있는가?
- [ ] body 기본 색상과 폰트가 설정되어 있는가?
- [ ] button, input, textarea, select의 font inherit이 적용되어 있는가?
```

권장 파일 위치:

```text
src/
└─ styles/
   ├─ reset.css
   ├─ tokens.css
   ├─ globals.css
   ├─ typography.css
   └─ utilities.css
```

---

### [FAQ]

Q. 모든 스타일을 globals.css에 넣어도 돼?
A. 권장하지 않는다. global에는 전체 기본 스타일만 두고 컴포넌트 스타일은 분리하는 것이 좋다.

Q. body에 font-family를 넣는 건 괜찮아?
A. 괜찮다. 전체 앱의 기본 폰트는 global style에서 관리하는 것이 일반적이다.

Q. button 기본 스타일을 global에서 모두 제거해도 돼?
A. 가능하지만 focus style과 접근성 상태를 함께 고려해야 한다.

Q. Global Style은 컴포넌트 스타일보다 먼저 import해야 해?
A. 일반적으로 reset, token, global 순서로 먼저 import하고 component style은 컴포넌트에서 import한다.

---

## 1.2 Global Style Boundary

### [개념]

Global Style Boundary는 전역 스타일에 허용되는 범위를 제한하는 규칙이다.

전역 스타일은 모든 화면과 컴포넌트에 영향을 준다.

따라서 Global Style은 최소 책임 원칙을 따라야 한다.

---

### [핵심]

Global Style 허용 범위:

- 전체 앱 기본값
- element baseline
- CSS variable
- 접근성 utility
- typography baseline
- reset / normalize

Global Style 금지에 가까운 범위:

- 화면별 layout
- 컴포넌트별 variant
- 특정 도메인 UI
- 특정 페이지 margin
- 특정 카드 디자인
- 특정 form spacing
- 강제 override

---

### [실무]

나쁜 예:

```css
.card {
  padding: 16px;
  border-radius: 12px;
  background: white;
}

.login-form input {
  margin-bottom: 12px;
}

.main-page .button {
  width: 100%;
}
```

좋은 예:

```css
body {
  color: var(--color-text);
  background: var(--color-background);
}

button,
input,
textarea,
select {
  font: inherit;
}
```

전역 스타일 판단 Flow:

```text
Style Rule 작성
→ 모든 화면에 적용되어도 안전한가?
→ 특정 컴포넌트 의미를 갖는가?
→ 특정 페이지 layout인가?
→ token / reset / baseline인가?
→ Global 또는 Component / Page Style 결정
```

---

### [FAQ]

Q. Global Style에 card class를 넣으면 안 돼?
A. 공통 utility 성격이면 가능하지만 특정 Card 컴포넌트 디자인이라면 컴포넌트 스타일로 분리하는 것이 좋다.

Q. Global Style이 많으면 뭐가 문제야?
A. 의도하지 않은 CSS 충돌, override 증가, 유지보수 어려움이 생길 수 있다.

Q. 전역 class를 아예 쓰면 안 돼?
A. 아니다. container, sr-only 같은 utility class는 전역으로 관리할 수 있다.

---

# 2. Reset CSS Rules

## 2.1 Reset CSS

### [개념]

Reset CSS는 브라우저 기본 스타일 차이를 줄이고 프로젝트 스타일 기준을 통일하기 위한 초기화 스타일이다.

Reset CSS는 UI를 직접 디자인하는 코드가 아니다.

Reset CSS의 목적:

- 브라우저 기본 margin 제거
- box-sizing 통일
- font inheritance 정리
- image layout 문제 감소
- form element 기본 차이 완화
- 예측 가능한 스타일 출발점 제공

---

### [핵심]

Reset CSS에서 권장되는 항목:

- universal box-sizing
- body margin 제거
- heading / paragraph margin 초기화
- image max-width 설정
- form element font inherit
- button 기본 font inherit
- list padding 초기화 여부 검토

주의할 항목:

- focus outline 제거 금지
- list style 제거 시 semantic list 사용성 고려
- button cursor와 disabled 상태 고려
- form 요소 접근성 고려
- 너무 공격적인 reset 지양

---

### [실무]

기본 Reset CSS 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body,
h1,
h2,
h3,
h4,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
}

ul,
ol {
  padding: 0;
}

img,
picture {
  max-width: 100%;
  display: block;
}

button,
input,
textarea,
select {
  font: inherit;
}
```

Reset CSS 리뷰 기준:

```md
- [ ] box-sizing이 전역 통일되어 있는가?
- [ ] body margin이 제거되어 있는가?
- [ ] image overflow를 줄이는 기본 스타일이 있는가?
- [ ] form element font가 상속되는가?
- [ ] focus outline을 무조건 제거하지 않는가?
- [ ] reset이 컴포넌트 디자인을 포함하지 않는가?
```

---

### [FAQ]

Q. reset css는 꼭 필요해?
A. 프로젝트 스타일 일관성을 위해 많이 사용한다. 다만 접근성에 필요한 기본 스타일을 제거하지 않도록 주의해야 한다.

Q. outline: none을 reset에 넣어도 돼?
A. 권장하지 않는다. 제거한다면 반드시 대체 focus style을 제공해야 한다.

Q. Reset CSS는 어디에 import해?
A. 일반적으로 앱의 entry 파일에서 가장 먼저 import한다.

Q. Reset CSS에 색상이나 버튼 디자인을 넣어도 돼?
A. 권장하지 않는다. Reset CSS는 초기화 역할에 집중해야 한다.

---

## 2.2 Reset CSS Accessibility Warning

### [개념]

Reset CSS Accessibility Warning은 초기화 과정에서 접근성에 필요한 브라우저 기본 기능을 제거하지 않도록 하는 규칙이다.

Reset은 스타일 통일을 위한 것이지 사용자 조작 가능성을 숨기기 위한 것이 아니다.

---

### [핵심]

주의해야 할 reset:

- `outline: none`
- `button { border: 0; background: none; }` 남용
- `a { text-decoration: none; }` 전역 적용
- list style 전역 제거
- input 기본 스타일 전부 제거
- disabled style 제거
- focus-visible 대체 없이 focus 제거

---

### [실무]

나쁜 예:

```css
* {
  outline: none;
}

a {
  text-decoration: none;
}

button {
  border: 0;
  background: none;
}
```

좋은 예:

```css
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

a {
  text-underline-offset: 0.2em;
}

button {
  font: inherit;
}
```

접근성 reset 검토 Flow:

```text
Reset Rule 확인
→ focus 표시 제거 여부 확인
→ link 구분 가능 여부 확인
→ form control 조작 가능성 확인
→ disabled 상태 인식 가능 여부 확인
→ 대체 스타일 제공 여부 확인
```

---

### [FAQ]

Q. focus outline이 보기 싫으면 지워도 돼?
A. 지우기만 하면 안 된다. 반드시 대체 focus-visible 스타일을 제공해야 한다.

Q. 링크 밑줄을 전역으로 제거해도 돼?
A. 가능하지만 링크를 색상만으로 구분하면 접근성 문제가 생길 수 있다.

Q. button 기본 스타일을 없애면 문제야?
A. 가능은 하지만 focus, disabled, cursor, hit area 같은 상태를 다시 설계해야 한다.

---

## 2.3 Normalize vs Reset

### [개념]

Normalize CSS는 브라우저 기본 스타일을 완전히 제거하기보다 브라우저 간 차이를 보정하는 방식이다.

Reset CSS는 브라우저 기본 스타일을 초기화하는 방식이다.

둘은 목적이 다르다.

---

### [핵심]

| 구분        | Reset CSS               | Normalize CSS                |
| ----------- | ----------------------- | ---------------------------- |
| 목적        | 기본 스타일 제거        | 브라우저 차이 보정           |
| 스타일 방향 | 초기화 중심             | 기본값 유지 중심             |
| 장점        | 프로젝트 기준 통일 쉬움 | 기본 접근성 스타일 유지 쉬움 |
| 단점        | 과하면 기본 사용성 손상 | 완전한 초기화는 아님         |
| 적합 상황   | 디자인 통제 강한 앱     | 기본 HTML 스타일 활용 앱     |

---

### [실무]

선택 기준:

```text
디자인 시안이 명확하고 UI 통제가 필요
→ Reset CSS

브라우저 기본 스타일을 어느 정도 유지
→ Normalize CSS

소규모 React 앱
→ 간단한 Reset + CSS Variable 조합

접근성 기본값 보존 중요
→ Normalize CSS 또는 약한 Reset
```

둘 다 사용할 때 주의:

```md
- [ ] 중복 초기화가 발생하지 않는가?
- [ ] import 순서가 명확한가?
- [ ] focus, link, form control 기본 사용성을 해치지 않는가?
- [ ] 프로젝트 기준과 충돌하지 않는가?
```

---

### [FAQ]

Q. Reset과 Normalize 중 뭐가 좋아?
A. 정답은 없다. 프로젝트 스타일 통제 수준과 접근성 기준에 따라 선택한다.

Q. 둘 다 써도 돼?
A. 가능은 하지만 중복 초기화가 생길 수 있어 주의해야 한다.

Q. React 프로젝트에서는 보통 뭘 써?
A. 간단한 reset과 token 기반 global style 조합을 많이 사용한다.

---

# 3. Design Token Rules

## 3.1 Design Token

### [개념]

Design Token은 색상, 간격, 폰트, radius, shadow, z-index 같은 디자인 값을 이름으로 관리하는 방식이다.

Design Token은 Agent가 일관된 스타일 코드를 생성하기 위한 기준 데이터다.

Design Token은 단순 변수 모음이 아니라 UI 의미를 보존하는 스타일 계약이다.

---

### [핵심]

Token으로 관리할 대상:

- Color
- Spacing
- Font Size
- Font Weight
- Line Height
- Border Radius
- Shadow
- Z-index
- Breakpoint
- Transition
- Layout Width

Design Token 장점:

- 스타일 일관성 유지
- 수정 범위 감소
- theme 확장 쉬움
- raw value 하드코딩 감소
- Agent 코드 생성 기준 명확
- Review Agent 검토 쉬움

---

### [실무]

기본 Design Token 예:

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-text: #111827;
  --color-muted: #6b7280;
  --color-border: #e5e7eb;
  --color-background: #ffffff;
  --color-surface: #f9fafb;

  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;

  --z-header: 100;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

Token 사용 예:

```css
.card {
  padding: var(--spacing-md);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
}
```

Design Token 리뷰 기준:

```md
- [ ] 반복 색상이 token으로 정의되어 있는가?
- [ ] spacing scale이 있는가?
- [ ] typography token이 있는가?
- [ ] radius, shadow, z-index 기준이 있는가?
- [ ] 컴포넌트에서 raw color를 남용하지 않는가?
- [ ] token 이름이 의미 기반인가?
```

---

### [FAQ]

Q. Design Token은 Design System에서만 쓰는 거야?
A. 아니다. 작은 프로젝트에서도 색상과 간격을 token으로 관리하면 유지보수에 좋다.

Q. 모든 값을 token으로 만들어야 해?
A. 아니다. 반복 사용되거나 의미가 있는 값부터 token으로 관리한다.

Q. 색상 코드를 직접 쓰면 안 돼?
A. 한두 번은 가능하지만 반복되는 색상은 token으로 분리하는 것이 좋다.

Q. Design Token은 Agent에게 왜 중요해?
A. Agent가 임의 색상과 간격을 만들지 않고 프로젝트 기준에 맞는 스타일을 생성할 수 있게 한다.

---

## 3.2 Token Naming Rules

### [개념]

Token Naming은 디자인 값을 의미 있는 이름으로 관리하는 규칙이다.

Token 이름은 값이 아니라 역할을 표현해야 한다.

예:

```text
나쁜 이름
→ --blue
→ --gray-1
→ --big-space

좋은 이름
→ --color-primary
→ --color-text
→ --color-border
→ --spacing-md
```

---

### [핵심]

Token Naming 원칙:

- 역할 기반 이름 사용
- 일관된 prefix 사용
- 의미 없는 숫자만 사용하지 않음
- component-specific token 남용 금지
- theme 확장을 고려
- color, spacing, radius 등 category 명시

권장 prefix:

```text
--color-*
--spacing-*
--font-size-*
--font-weight-*
--line-height-*
--radius-*
--shadow-*
--z-*
--transition-*
--layout-*
```

---

### [실무]

나쁜 예:

```css
:root {
  --blue: #2563eb;
  --red: #dc2626;
  --space1: 13px;
  --big: 9999;
}
```

좋은 예:

```css
:root {
  --color-primary: #2563eb;
  --color-error: #dc2626;
  --spacing-4: 16px;
  --z-modal: 1000;
}
```

Token Naming 리뷰 기준:

```md
- [ ] token 이름이 역할을 설명하는가?
- [ ] color, spacing, radius 등 category가 드러나는가?
- [ ] raw value 이름이 아니라 semantic name을 사용하는가?
- [ ] 프로젝트 전체에서 이름 체계가 일관적인가?
```

---

### [FAQ]

Q. token 이름은 색상명으로 지어도 돼?
A. primitive token에는 가능하지만 컴포넌트에서는 primary, error, surface 같은 semantic token 사용이 좋다.

Q. --blue와 --color-primary 중 뭐가 좋아?
A. 컴포넌트에서 사용할 값은 --color-primary처럼 역할 기반 이름이 좋다.

Q. spacing token은 xs, sm, md 방식과 숫자 방식 중 뭐가 좋아?
A. 둘 다 가능하다. 중요한 것은 프로젝트 전체에서 일관되게 사용하는 것이다.

---

# 4. Color Token Rules

## 4.1 Color Token

### [개념]

Color Token은 UI 색상을 의미 단위로 관리하는 방식이다.

Color Token은 단순 색상값 저장이 아니라 UI 상태와 역할을 표현한다.

---

### [핵심]

권장 color token 유형:

```text
Brand Color
→ --color-primary
→ --color-primary-hover

Text Color
→ --color-text
→ --color-muted

Background Color
→ --color-background
→ --color-surface

Border Color
→ --color-border

Semantic Color
→ --color-success
→ --color-warning
→ --color-error
→ --color-info
```

Color Token 주의:

- 색상만으로 상태 전달 금지
- contrast 부족 주의
- hover 색상 누락 주의
- disabled 색상 누락 주의
- brand color와 semantic color 구분
- dark mode 고려 시 token alias 구조 필요

---

### [실무]

Color Token 예:

```css
:root {
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;

  --color-success: #16a34a;
  --color-warning: #f59e0b;
  --color-error: #dc2626;
  --color-info: #0284c7;

  --color-text: #111827;
  --color-muted: #6b7280;
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-border: #e5e7eb;
}
```

나쁜 예:

```css
.error-message {
  color: red;
}
```

좋은 예:

```css
.error-message {
  color: var(--color-error);
}
```

Color Token 리뷰 기준:

```md
- [ ] primary, text, background, surface, border token이 있는가?
- [ ] success, warning, error, info token이 있는가?
- [ ] hover 상태 색상이 정의되어 있는가?
- [ ] raw color 하드코딩이 반복되지 않는가?
- [ ] dark mode 확장 가능성이 있는가?
```

---

### [FAQ]

Q. primary와 success는 뭐가 달라?
A. primary는 브랜드나 주요 행동 색상이고, success는 성공 상태를 나타내는 의미 색상이다.

Q. 에러 색상을 red로 쓰면 안 돼?
A. 가능하지만 token으로 관리하는 것이 일관성과 theme 확장에 좋다.

Q. color token은 왜 semantic name이 중요해?
A. theme나 brand 색상이 바뀌어도 컴포넌트 코드를 덜 수정하기 위해서다.

Q. 색상만으로 에러 상태를 표시해도 돼?
A. 안 된다. 에러 메시지, 아이콘, aria 등 추가 정보가 필요하다.

---

## 4.2 Semantic Color Token

### [개념]

Semantic Color Token은 색상을 실제 UI 역할 기준으로 이름 붙이는 방식이다.

Semantic Token은 theme 전환과 dark mode에 강하다.

구조:

```text
Primitive Color
→ Semantic Color
→ Component Style
```

예:

```text
blue-600
→ --color-primary
→ Button background
```

---

### [핵심]

Semantic Token 예:

- `--color-primary`
- `--color-primary-hover`
- `--color-text`
- `--color-muted`
- `--color-background`
- `--color-surface`
- `--color-border`
- `--color-error`
- `--color-success`
- `--color-warning`
- `--color-info`

Primitive Token 예:

- `--blue-600`
- `--gray-900`
- `--red-600`

컴포넌트에서는 semantic token 우선 사용이 권장된다.

---

### [실무]

Semantic Token 구조 예:

```css
:root {
  --blue-600: #2563eb;
  --blue-700: #1d4ed8;
  --gray-50: #f9fafb;
  --gray-900: #111827;

  --color-primary: var(--blue-600);
  --color-primary-hover: var(--blue-700);
  --color-background: #ffffff;
  --color-surface: var(--gray-50);
  --color-text: var(--gray-900);
}
```

컴포넌트 사용:

```css
.buttonPrimary {
  background: var(--color-primary);
}

.buttonPrimary:hover {
  background: var(--color-primary-hover);
}
```

---

### [FAQ]

Q. primitive token과 semantic token은 뭐가 달라?
A. primitive token은 실제 색상값이고 semantic token은 UI 역할을 표현하는 이름이다.

Q. 컴포넌트에서는 어떤 token을 써야 해?
A. 일반적으로 semantic token을 사용하는 것이 theme 확장에 좋다.

Q. 작은 프로젝트도 primitive와 semantic을 나눠야 해?
A. 필수는 아니지만 dark mode나 theme 확장이 필요하면 나누는 것이 좋다.

---

# 5. Spacing Token Rules

## 5.1 Spacing Token

### [개념]

Spacing Token은 margin, padding, gap 같은 간격 값을 일정한 scale로 관리하는 방식이다.

Spacing Token은 UI 리듬과 화면 일관성을 유지하기 위한 기준이다.

---

### [핵심]

Spacing Token 사용 대상:

- margin
- padding
- gap
- section spacing
- card padding
- form field spacing
- layout gutter
- stack spacing

Spacing Token 장점:

- 무작위 spacing 방지
- UI 리듬 유지
- layout 일관성 강화
- Agent의 임의 간격 생성 방지
- Review 기준 명확화

---

### [실무]

권장 spacing scale 예:

```css
:root {
  --spacing-0: 0;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-5: 20px;
  --spacing-6: 24px;
  --spacing-8: 32px;
  --spacing-10: 40px;
  --spacing-12: 48px;
}
```

사용 예:

```css
.form {
  display: grid;
  gap: var(--spacing-4);
}

.card {
  padding: var(--spacing-6);
}
```

Review 기준:

```md
- [ ] 간격 값이 무작위로 증가하지 않는가?
- [ ] margin / padding / gap 사용 기준이 일관적인가?
- [ ] 컴포넌트 내부 간격과 외부 간격이 구분되는가?
- [ ] layout gap에 margin 남용이 없는가?
- [ ] 13px, 17px 같은 임의값이 반복되지 않는가?
```

---

### [FAQ]

Q. spacing token은 왜 필요해?
A. 간격이 화면마다 제각각이 되는 것을 막고 UI 리듬을 일관되게 유지하기 위해 필요하다.

Q. 13px, 17px 같은 값을 쓰면 안 돼?
A. 특별한 이유가 없다면 spacing scale 안에서 선택하는 것이 좋다.

Q. gap과 margin 중 무엇을 우선 사용해?
A. 반복 배치 간격은 부모 layout의 gap으로 관리하는 것이 예측하기 쉽다.

Q. 모든 margin을 token으로 써야 해?
A. 반복되거나 UI 기준이 되는 값은 token을 사용하는 것이 좋다.

---

## 5.2 Spacing Responsibility

### [개념]

Spacing Responsibility는 간격을 누가 담당하는지 정하는 규칙이다.

부모 layout은 외부 배치를 담당한다.

컴포넌트는 내부 간격을 담당한다.

---

### [핵심]

권장 원칙:

```text
Parent Layout
→ gap
→ section spacing
→ page spacing

Component
→ padding
→ internal gap
→ child alignment

Utility
→ one-off spacing helper
```

피해야 할 구조:

- 재사용 컴포넌트가 외부 margin을 강제
- 페이지 layout이 컴포넌트 내부에 포함
- margin collapse 고려 없이 세로 간격 작성
- 동일 간격을 여러 방식으로 반복 작성

---

### [실무]

나쁜 예:

```css
.card {
  margin-bottom: 24px;
  padding: 16px;
}
```

좋은 예:

```css
.cardList {
  display: grid;
  gap: var(--spacing-6);
}

.card {
  padding: var(--spacing-4);
}
```

Spacing 검토 Flow:

```text
간격 문제 확인
→ 부모 배치 간격인가?
→ 컴포넌트 내부 간격인가?
→ token scale에 있는 값인가?
→ margin 대신 gap 사용 가능한가?
→ 중복 spacing 제거
```

---

### [FAQ]

Q. Card 컴포넌트에 margin-bottom을 넣어도 돼?
A. 재사용 컴포넌트라면 권장하지 않는다. 목록 간격은 부모 layout의 gap으로 관리하는 것이 좋다.

Q. 컴포넌트 내부 padding은 컴포넌트가 가져도 돼?
A. 가능하다. 내부 여백은 컴포넌트 외형의 일부다.

Q. section 간격은 어디서 관리해?
A. page layout 또는 layout component에서 관리하는 것이 좋다.

---

# 6. Typography Token Rules

## 6.1 Typography Token

### [개념]

Typography Token은 font size, line height, font weight, font family, letter spacing 같은 글자 스타일을 체계화하는 방식이다.

Typography Token은 화면의 정보 계층과 가독성을 유지하기 위해 필요하다.

---

### [핵심]

권장 typography token:

- font-family
- font-size
- font-weight
- line-height
- letter-spacing
- heading size
- body size
- caption size

Typography Token 장점:

- 제목 / 본문 / 보조 텍스트 계층 유지
- 화면별 글자 크기 불일치 방지
- line-height 일관성 유지
- Agent의 임의 font-size 생성 방지
- theme 또는 brand 변경 대응 쉬움

---

### [실무]

Typography Token 예:

```css
:root {
  --font-family-base: system-ui, sans-serif;

  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-md: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2rem;

  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-base: 1.5;
  --line-height-relaxed: 1.7;
}
```

사용 예:

```css
.pageTitle {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
}

.bodyText {
  font-size: var(--font-size-md);
  line-height: var(--line-height-base);
}
```

Typography 리뷰 기준:

```md
- [ ] font-family가 token으로 관리되는가?
- [ ] font-size scale이 정의되어 있는가?
- [ ] heading과 body의 계층이 명확한가?
- [ ] line-height가 가독성을 해치지 않는가?
- [ ] 컴포넌트마다 임의 font-size가 반복되지 않는가?
```

---

### [FAQ]

Q. font-size를 매번 직접 써도 돼?
A. 가능하지만 typography token을 사용하면 화면 계층과 일관성을 유지하기 쉽다.

Q. line-height도 token으로 관리해야 해?
A. 권장된다. 가독성과 UI 밀도 관리에 중요하다.

Q. font-family는 어디에서 설정해?
A. token으로 정의한 뒤 body의 global style에서 적용하는 것이 일반적이다.

Q. heading마다 font-size를 직접 정해도 돼?
A. 가능하지만 반복되는 heading scale은 token으로 관리하는 것이 좋다.

---

## 6.2 Typography Responsibility

### [개념]

Typography Responsibility는 글자 스타일의 책임을 token, global, component로 나누는 기준이다.

---

### [핵심]

책임 분리:

```text
Font Family / Size Scale / Weight / Line Height
→ Typography Token

body 기본 font
→ Global Style

heading baseline
→ Typography Global or Component

컴포넌트별 title / label / caption
→ Component Style
```

주의:

- 모든 h1, h2를 전역에서 강하게 디자인하지 않음
- 컴포넌트 title은 컴포넌트 스타일에서 관리
- 글자 크기를 px로 무작위 작성하지 않음
- line-height를 너무 작게 설정하지 않음

---

### [실무]

구조 예:

```text
src/styles/tokens.css
→ font token 정의

src/styles/globals.css
→ body 기본 font 적용

src/styles/typography.css
→ 기본 heading / paragraph baseline

components/Card/Card.module.css
→ card title / description 스타일
```

컴포넌트 사용 예:

```css
.cardTitle {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  line-height: var(--line-height-tight);
}

.cardDescription {
  font-size: var(--font-size-sm);
  color: var(--color-muted);
  line-height: var(--line-height-base);
}
```

---

### [FAQ]

Q. typography.css 파일이 꼭 필요해?
A. 필수는 아니다. 프로젝트 규모에 따라 globals.css에 포함하거나 별도 파일로 분리할 수 있다.

Q. h1, h2 스타일을 global에서 모두 정해도 돼?
A. 가능하지만 컴포넌트별 title 계층과 충돌하지 않도록 주의해야 한다.

Q. 컴포넌트 title은 어디서 관리해?
A. 해당 컴포넌트 스타일에서 token을 사용해 관리하는 것이 좋다.

---

# 7. Radius, Shadow, Z-index Token Rules

## 7.1 Radius Token

### [개념]

Radius Token은 border-radius 값을 scale로 관리하는 방식이다.

Radius Token은 카드, 버튼, 입력창, 모달의 둥근 정도를 일관되게 유지한다.

---

### [핵심]

Radius Token 사용 대상:

- Button
- Card
- Input
- Modal
- Badge
- Dropdown
- Image thumbnail

권장 token:

```css
:root {
  --radius-none: 0;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;
}
```

---

### [실무]

나쁜 예:

```css
.card {
  border-radius: 13px;
}

.button {
  border-radius: 9px;
}
```

좋은 예:

```css
.card {
  border-radius: var(--radius-lg);
}

.button {
  border-radius: var(--radius-md);
}
```

Radius 리뷰 기준:

```md
- [ ] radius scale이 정의되어 있는가?
- [ ] 컴포넌트마다 임의 radius를 쓰지 않는가?
- [ ] button, card, modal의 radius 기준이 일관적인가?
- [ ] pill UI에는 radius-full 같은 token을 사용하는가?
```

---

### [FAQ]

Q. radius token은 꼭 필요해?
A. 반복되는 둥근 모서리 값이 있다면 token으로 관리하는 것이 좋다.

Q. border-radius를 직접 써도 돼?
A. 가능하지만 반복되는 값은 token으로 분리하는 것이 유지보수에 좋다.

Q. radius-full은 언제 써?
A. pill button, badge, avatar처럼 완전히 둥근 UI에 사용한다.

---

## 7.2 Shadow Token

### [개념]

Shadow Token은 box-shadow 값을 scale로 관리하는 방식이다.

Shadow Token은 카드, 모달, 드롭다운, 토스트 같은 elevation UI의 깊이감을 일관되게 유지한다.

---

### [핵심]

Shadow Token 사용 대상:

- Card
- Modal
- Dropdown
- Popover
- Tooltip
- Toast
- Floating Button

권장 token:

```css
:root {
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.08);
  --shadow-md: 0 4px 12px rgb(0 0 0 / 0.12);
  --shadow-lg: 0 12px 24px rgb(0 0 0 / 0.16);
}
```

주의:

- shadow 남용 금지
- dark mode에서 shadow만으로 elevation 표현 어려움
- border / surface token과 함께 사용
- hover shadow 변화는 transition 고려

---

### [실무]

사용 예:

```css
.dropdown {
  box-shadow: var(--shadow-md);
}

.modal {
  box-shadow: var(--shadow-lg);
}
```

Shadow 리뷰 기준:

```md
- [ ] shadow scale이 정의되어 있는가?
- [ ] modal, dropdown, card shadow 기준이 일관적인가?
- [ ] shadow 값이 컴포넌트마다 하드코딩되지 않는가?
- [ ] dark mode에서 surface / border와 함께 검토되는가?
```

---

### [FAQ]

Q. shadow도 token으로 관리해야 해?
A. 반복 사용되는 shadow는 token으로 관리하면 UI 깊이감이 일관된다.

Q. dark mode에서도 shadow가 잘 보여?
A. 항상 그렇지 않다. dark mode에서는 surface, border, overlay와 함께 조정해야 한다.

Q. hover마다 shadow를 크게 바꿔도 돼?
A. 가능하지만 과하면 산만하고 motion 문제가 생길 수 있다.

---

## 7.3 Z-index Token

### [개념]

Z-index Token은 modal, header, dropdown, toast 같은 겹침 UI의 stacking order를 체계적으로 관리하는 방식이다.

Z-index는 큰 숫자를 임의로 쓰는 방식으로 해결하면 안 된다.

---

### [핵심]

권장 z-index scale:

```css
:root {
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-header: 300;
  --z-overlay: 900;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

Z-index 문제 원인:

- stacking context
- position 미설정
- 부모 z-index
- transform
- opacity
- filter
- overflow hidden
- portal 미사용

---

### [실무]

나쁜 예:

```css
.modal {
  z-index: 999999;
}
```

좋은 예:

```css
.modal {
  z-index: var(--z-modal);
}
```

Z-index 리뷰 기준:

```md
- [ ] z-index token scale이 있는가?
- [ ] 9999 같은 임의 숫자를 남용하지 않는가?
- [ ] modal, overlay, toast 우선순위가 명확한가?
- [ ] dropdown이 header / modal과 충돌하지 않는가?
- [ ] stacking context 문제를 확인했는가?
```

Z-index 검토 Flow:

```text
겹침 문제 발생
→ 대상 element position 확인
→ z-index token 확인
→ 부모 stacking context 확인
→ overflow hidden 확인
→ portal 필요 여부 확인
```

---

### [FAQ]

Q. z-index는 크게 주면 해결돼?
A. 아니다. stacking context 때문에 큰 숫자를 줘도 해결되지 않을 수 있다.

Q. modal z-index는 어떻게 관리해?
A. 프로젝트 z-index token scale을 정하고 modal, toast, dropdown 우선순위를 명확히 관리한다.

Q. z-index 9999를 쓰면 안 돼?
A. 임시 해결은 가능하지만 token 없이 남용하면 겹침 구조를 예측하기 어려워진다.

---

# 8. Transition Token Rules

## 8.1 Transition Token

### [개념]

Transition Token은 상태 변화에 사용하는 duration과 easing을 일관되게 관리하는 방식이다.

Transition Token은 hover, focus, modal open, dropdown open 같은 상호작용 스타일에 사용된다.

---

### [핵심]

Transition Token 사용 대상:

- button hover
- link hover
- card hover
- modal open
- dropdown open
- opacity change
- transform change
- background color change
- border color change

권장 token:

```css
:root {
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
  --transition-slow: 350ms ease;
}
```

주의:

- transition duration 남용 금지
- width / height transition 남용 금지
- layout shift 유발 금지
- prefers-reduced-motion 고려
- 모든 요소에 transition all 남용 금지

---

### [실무]

나쁜 예:

```css
.card {
  transition: all 1s;
}
```

좋은 예:

```css
.card {
  transition:
    box-shadow var(--transition-fast),
    transform var(--transition-fast);
}
```

Transition 리뷰 기준:

```md
- [ ] 반복 transition 값이 token으로 관리되는가?
- [ ] transition all을 남용하지 않는가?
- [ ] duration이 과하게 길지 않은가?
- [ ] layout shift를 유발하는 속성을 transition하지 않는가?
- [ ] reduced motion 기준을 고려하는가?
```

---

### [FAQ]

Q. transition도 token으로 관리해야 해?
A. 반복 사용되는 duration과 easing은 token으로 관리하면 일관성에 좋다.

Q. transition: all을 써도 돼?
A. 권장하지 않는다. 의도하지 않은 속성까지 transition되어 성능과 예측 가능성이 떨어진다.

Q. transition 시간이 길면 더 부드러워?
A. 항상 그렇지 않다. 너무 길면 사용성이 떨어지고 답답하게 느껴질 수 있다.

---

# 9. Token File Structure

## 9.1 Token File Structure

### [개념]

Token File Structure는 디자인 토큰을 프로젝트 안에서 어디에 배치하고 어떻게 import할지 정하는 규칙이다.

Token은 token을 사용하는 CSS보다 먼저 로드되어야 한다.

---

### [핵심]

권장 구조:

```text
src/
└─ styles/
   ├─ reset.css
   ├─ tokens.css
   ├─ globals.css
   ├─ typography.css
   └─ utilities.css
```

권장 import 순서:

```text
Reset
→ Token
→ Global
→ Typography
→ Utility
→ Layout
→ Component
```

---

### [실무]

CRA / React 예:

```js
import "./styles/reset.css";
import "./styles/tokens.css";
import "./styles/globals.css";
import "./styles/typography.css";
import "./styles/utilities.css";
```

토큰 파일 분리 기준:

```text
소규모 프로젝트
→ tokens.css 하나로 관리 가능

중규모 이상
→ colors.css, spacing.css, typography.css 등 분리 가능

theme 필요
→ theme.css 또는 themes/light.css, themes/dark.css 분리 가능
```

Token Structure 리뷰 기준:

```md
- [ ] token 파일이 전역에서 먼저 import되는가?
- [ ] token이 component style보다 먼저 로드되는가?
- [ ] token 파일이 너무 복잡해지면 분리 기준이 있는가?
- [ ] theme token과 base token의 책임이 구분되는가?
```

---

### [FAQ]

Q. token 파일은 어디에 두는 게 좋아?
A. 일반적으로 src/styles/tokens.css처럼 전역 styles 폴더에 둔다.

Q. token 파일은 언제 import해야 해?
A. token을 사용하는 global, component style보다 먼저 import해야 한다.

Q. token 파일을 여러 개로 나눠도 돼?
A. 가능하다. 규모가 커지면 color, spacing, typography 등으로 분리할 수 있다.

---

# 10. Part02 Quality Checklist

## 10.1 Global Style and Token Checklist

### [개념]

Part02 단계에서는 Global Style, Reset CSS, Design Token의 기준이 명확한지 검토한다.

이 단계는 실제 컴포넌트 스타일 생성 전 프로젝트 전체 스타일 기반을 고정하는 단계다.

---

### [핵심]

Part02 체크리스트:

```md
## Global Style

- [ ] Global Style의 책임이 명확한가?
- [ ] 특정 컴포넌트 스타일이 global에 들어가지 않았는가?
- [ ] body 기본 font, color, background가 설정되어 있는가?
- [ ] image, button, input 기본 스타일이 정리되어 있는가?

## Reset CSS

- [ ] reset이 초기화 역할에 집중하는가?
- [ ] focus outline을 무조건 제거하지 않는가?
- [ ] form element 접근성을 해치지 않는가?
- [ ] reset과 normalize 선택 기준이 명확한가?

## Design Token

- [ ] color token이 정의되어 있는가?
- [ ] spacing token이 정의되어 있는가?
- [ ] typography token이 정의되어 있는가?
- [ ] radius, shadow, z-index token이 정의되어 있는가?
- [ ] transition token이 필요한 경우 정의되어 있는가?
- [ ] token naming이 일관적인가?
- [ ] raw value 하드코딩이 과하지 않은가?

## File Structure

- [ ] tokens.css 위치가 명확한가?
- [ ] reset, token, global import 순서가 명확한가?
- [ ] component style보다 token이 먼저 로드되는가?
```

---

### [실무]

Part02 승인 기준:

```text
Global Style 책임 명확
+ Reset CSS 접근성 문제 없음
+ Design Token 정의
+ Token Naming 일관성
+ Import Order 명확
+ FAQ 충분
+ Retrieval Queries 포함
→ Part02 승인 가능
```

Part02 보류 기준:

```text
모든 스타일이 global에 몰림
또는 reset에서 focus 제거
또는 token 없이 raw value 반복
또는 token naming 불일치
또는 import 순서 불명확
→ 재작성 필요
```

---

### [FAQ]

Q. Part02의 핵심 목적은 뭐야?
A. Global Style, Reset CSS, Design Token의 기준을 고정해 프로젝트 전체 스타일 기반을 만드는 것이다.

Q. Part02에서 가장 위험한 문제는 뭐야?
A. 모든 스타일을 global에 몰아넣거나 reset에서 접근성 스타일을 제거하거나 token 없이 raw value를 반복하는 것이다.

Q. Part02가 완료되면 다음에 뭘 다뤄야 해?
A. Styling Method Rules에서 Plain CSS, CSS Module, CSS-in-JS, Tailwind, SCSS 선택 기준을 다루는 것이 자연스럽다.

---

# Retrieval Queries

### [FAQ]

Q. Global Style은 뭐야?
A. 애플리케이션 전체에 적용되는 기본 스타일이며 reset, body 기본값, font, background, text color, CSS variable 등을 관리한다.

Q. Global Style에 넣기 적합한 것은 뭐야?
A. box-sizing, body margin reset, font-family, background, text color, root CSS variables, image 기본 스타일, form font inherit이다.

Q. Global Style에 넣으면 안 되는 것은 뭐야?
A. 특정 Card, Modal, Button variant, Page layout, Form spacing 같은 컴포넌트 전용 스타일은 넣지 않는 것이 좋다.

Q. 모든 스타일을 globals.css에 넣어도 돼?
A. 권장하지 않는다. global에는 전체 기본 스타일만 두고 컴포넌트 스타일은 분리하는 것이 좋다.

Q. Global Style Boundary가 뭐야?
A. 전역 스타일에 허용되는 범위를 제한해 CSS 충돌과 유지보수 문제를 줄이는 규칙이다.

Q. 전역 class를 아예 쓰면 안 돼?
A. 아니다. container, sr-only 같은 utility class는 전역으로 관리할 수 있다.

Q. Reset CSS는 뭐야?
A. 브라우저 기본 스타일 차이를 줄이고 프로젝트 스타일 기준을 통일하기 위한 초기화 스타일이다.

Q. Reset CSS의 목적은 뭐야?
A. 브라우저 기본 margin 제거, box-sizing 통일, font inheritance 정리, image layout 문제 감소, form element 기본 차이 완화다.

Q. reset css는 꼭 필요해?
A. 프로젝트 스타일 일관성을 위해 많이 사용한다. 다만 접근성에 필요한 기본 스타일을 제거하지 않도록 주의해야 한다.

Q. outline none을 reset에 넣어도 돼?
A. 권장하지 않는다. 제거한다면 반드시 대체 focus style을 제공해야 한다.

Q. Reset CSS에서 조심해야 할 것은 뭐야?
A. focus outline 제거, link underline 전역 제거, form control 초기화, button 기본 스타일 제거를 주의해야 한다.

Q. Reset CSS와 Normalize CSS 차이는 뭐야?
A. Reset은 기본 스타일 제거 중심이고 Normalize는 브라우저 차이 보정 중심이다.

Q. Reset과 Normalize 중 뭐가 좋아?
A. 정답은 없다. 프로젝트 스타일 통제 수준과 접근성 기준에 따라 선택한다.

Q. React 프로젝트에서는 reset을 어떻게 쓰는 게 좋아?
A. 간단한 reset과 token 기반 global style 조합을 많이 사용한다.

Q. Design Token이 뭐야?
A. 색상, 간격, 폰트, radius, shadow, z-index 같은 디자인 값을 이름으로 관리하는 방식이다.

Q. Design Token은 왜 필요해?
A. 스타일 일관성을 유지하고 수정 범위를 줄이며 theme 확장을 쉽게 하기 위해 필요하다.

Q. Design Token은 Agent에게 왜 중요해?
A. Agent가 임의 색상과 간격을 만들지 않고 프로젝트 기준에 맞는 스타일을 생성할 수 있게 한다.

Q. 모든 값을 token으로 만들어야 해?
A. 아니다. 반복 사용되거나 의미가 있는 값부터 token으로 관리한다.

Q. 색상 코드를 직접 쓰면 안 돼?
A. 한두 번은 가능하지만 반복되는 색상은 token으로 분리하는 것이 좋다.

Q. Token Naming 원칙은 뭐야?
A. 역할 기반 이름을 사용하고 color, spacing, radius 같은 category prefix를 일관되게 붙이는 것이다.

Q. --blue와 --color-primary 중 뭐가 좋아?
A. 컴포넌트에서 사용할 값은 --color-primary처럼 역할 기반 이름이 좋다.

Q. 권장 token prefix는 뭐야?
A. --color-_, --spacing-_, --font-size-_, --font-weight-_, --line-height-_, --radius-_, --shadow-_, --z-_ 형식이 좋다.

Q. Color Token은 뭐야?
A. UI 색상을 primary, text, background, border, success, error 같은 의미 단위로 관리하는 방식이다.

Q. Color Token은 어떻게 나눠?
A. brand color, text color, background color, border color, semantic color로 나눌 수 있다.

Q. primary와 success는 뭐가 달라?
A. primary는 브랜드나 주요 행동 색상이고, success는 성공 상태를 나타내는 의미 색상이다.

Q. 에러 색상을 red로 쓰면 안 돼?
A. 가능하지만 token으로 관리하는 것이 일관성과 theme 확장에 좋다.

Q. 색상만으로 에러 상태를 표시해도 돼?
A. 안 된다. 에러 메시지, 아이콘, aria 등 추가 정보가 필요하다.

Q. Semantic Color Token은 뭐야?
A. 실제 색상값보다 UI 역할을 기준으로 이름 붙인 color token이다.

Q. primitive token과 semantic token은 뭐가 달라?
A. primitive token은 실제 색상값이고 semantic token은 UI 역할을 표현하는 이름이다.

Q. 컴포넌트에서는 어떤 color token을 써야 해?
A. 일반적으로 semantic token을 사용하는 것이 theme 확장에 좋다.

Q. Spacing Token은 뭐야?
A. margin, padding, gap 같은 간격 값을 일정한 scale로 관리하는 방식이다.

Q. Spacing Token은 왜 필요해?
A. 간격이 화면마다 제각각이 되는 것을 막고 UI 리듬을 일관되게 유지하기 위해 필요하다.

Q. 13px, 17px 같은 값을 써도 돼?
A. 특별한 이유가 없다면 spacing scale 안에서 선택하는 것이 좋다.

Q. gap과 margin 중 무엇을 우선 사용해?
A. 반복 배치 간격은 부모 layout의 gap으로 관리하는 것이 예측하기 쉽다.

Q. Spacing Responsibility는 뭐야?
A. 부모 layout은 외부 배치 간격을 담당하고 컴포넌트는 내부 간격을 담당하는 규칙이다.

Q. Card 컴포넌트에 margin-bottom을 넣어도 돼?
A. 재사용 컴포넌트라면 권장하지 않는다. 목록 간격은 부모 layout의 gap으로 관리하는 것이 좋다.

Q. Typography Token은 뭐야?
A. font size, line height, font weight, font family, letter spacing 같은 글자 스타일을 체계화하는 방식이다.

Q. Typography Token은 왜 필요해?
A. 화면의 정보 계층과 가독성을 유지하고 글자 스타일 불일치를 줄이기 위해 필요하다.

Q. font-size를 매번 직접 써도 돼?
A. 가능하지만 typography token을 사용하면 화면 계층과 일관성을 유지하기 쉽다.

Q. line-height도 token으로 관리해야 해?
A. 권장된다. 가독성과 UI 밀도 관리에 중요하다.

Q. font-family는 어디에서 설정해?
A. token으로 정의한 뒤 body의 global style에서 적용하는 것이 일반적이다.

Q. Typography Responsibility는 뭐야?
A. font scale은 token, body 기본 font는 global, 컴포넌트 title은 component style에서 관리하는 기준이다.

Q. Radius Token은 뭐야?
A. border-radius 값을 scale로 관리해 버튼, 카드, 입력창, 모달의 둥근 정도를 일관되게 유지하는 방식이다.

Q. radius token은 꼭 필요해?
A. 반복되는 둥근 모서리 값이 있다면 token으로 관리하는 것이 좋다.

Q. radius-full은 언제 써?
A. pill button, badge, avatar처럼 완전히 둥근 UI에 사용한다.

Q. Shadow Token은 뭐야?
A. box-shadow 값을 scale로 관리해 카드, 모달, 드롭다운 같은 elevation UI의 깊이감을 일관되게 유지하는 방식이다.

Q. shadow도 token으로 관리해야 해?
A. 반복 사용되는 shadow는 token으로 관리하면 UI 깊이감이 일관된다.

Q. dark mode에서도 shadow가 잘 보여?
A. 항상 그렇지 않다. dark mode에서는 surface, border, overlay와 함께 조정해야 한다.

Q. Z-index Token은 뭐야?
A. modal, header, dropdown, toast 같은 겹침 UI의 stacking order를 체계적으로 관리하는 방식이다.

Q. z-index는 크게 주면 해결돼?
A. 아니다. stacking context 때문에 큰 숫자를 줘도 해결되지 않을 수 있다.

Q. z-index 9999를 써도 돼?
A. 임시 해결은 가능하지만 token 없이 남용하면 겹침 구조를 예측하기 어려워진다.

Q. Transition Token은 뭐야?
A. 상태 변화에 사용하는 duration과 easing을 일관되게 관리하는 방식이다.

Q. transition도 token으로 관리해야 해?
A. 반복 사용되는 duration과 easing은 token으로 관리하면 일관성에 좋다.

Q. transition all을 써도 돼?
A. 권장하지 않는다. 의도하지 않은 속성까지 transition되어 성능과 예측 가능성이 떨어진다.

Q. Token File Structure는 어떻게 하는 게 좋아?
A. src/styles/tokens.css에 두고 reset, token, global 순서로 import하는 것이 일반적이다.

Q. token 파일은 언제 import해야 해?
A. token을 사용하는 global, component style보다 먼저 import해야 한다.

Q. CSS import 순서는 어떻게 하는 게 좋아?
A. Reset → Token → Global → Typography → Utility → Layout → Component 순서가 좋다.

Q. Part02의 핵심 목적은 뭐야?
A. Global Style, Reset CSS, Design Token의 기준을 고정해 프로젝트 전체 스타일 기반을 만드는 것이다.

Q. Part02에서 가장 위험한 문제는 뭐야?
A. 모든 스타일을 global에 몰아넣거나 reset에서 접근성 스타일을 제거하거나 token 없이 raw value를 반복하는 것이다.

Q. Part02 다음에는 뭘 다루는 게 자연스러워?
A. Plain CSS, CSS Module, CSS-in-JS, Tailwind, SCSS 같은 Styling Method Rules를 다루는 것이 자연스럽다.
