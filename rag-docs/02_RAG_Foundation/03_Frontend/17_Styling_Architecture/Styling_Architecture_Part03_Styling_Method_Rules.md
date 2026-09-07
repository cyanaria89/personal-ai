# Styling Architecture Part03 - Styling Method Rules

---

# 1. Styling Method Overview

## 1.1 Styling Method Definition

### [개념]

Styling Method는 프론트엔드 프로젝트에서 스타일 코드를 작성하고 관리하는 방식이다.

Styling Method는 단순 취향이 아니라 프로젝트 규모, 팀 숙련도, 유지보수성, 컴포넌트 구조, theme 필요성, 빌드 환경에 따라 선택해야 한다.

대표 Styling Method:

- Plain CSS
- CSS Module
- CSS-in-JS
- Tailwind CSS
- SCSS / Sass

---

### [핵심]

Styling Method 선택 기준:

- 프로젝트 규모
- React 컴포넌트 단위 스타일 필요성
- 전역 CSS 충돌 가능성
- 팀 CSS 숙련도
- 동적 스타일 필요성
- Theme / Dark Mode 필요성
- Design System 필요성
- 빌드 환경
- 유지보수 기간
- 코드 리뷰 난이도

---

### [실무]

Styling Method 판단 Flow:

```text
Project Type 확인
→ Existing Styling Method 확인
→ Team Skill 확인
→ Component Scope 필요 여부 확인
→ Theme / Dark Mode 필요 여부 확인
→ Dynamic Style 필요 여부 확인
→ Build Environment 확인
→ Styling Method 선택
→ File Structure 정의
→ Review Checklist 적용
```

기본 선택 기준:

```text
소규모 학원 프로젝트
→ Plain CSS 또는 CSS Module

React 컴포넌트 단위 스타일
→ CSS Module

동적 스타일 / theme provider 필요
→ CSS-in-JS

빠른 UI 작성 / utility-first 선호
→ Tailwind CSS

기존 CSS 확장 / nesting 필요
→ SCSS
```

---

### [FAQ]

Q. Styling Method는 아무거나 골라도 돼?
A. 아니다. 프로젝트 규모, 팀 숙련도, 유지보수성, theme 필요성, 컴포넌트 구조를 기준으로 선택해야 한다.

Q. 한 프로젝트에서 여러 Styling Method를 섞어도 돼?
A. 가능하지만 명확한 기준 없이 섞으면 유지보수가 어려워진다.

Q. 학원 React 프로젝트에서는 뭐가 무난해?
A. Plain CSS 또는 CSS Module이 무난하다. 컴포넌트 단위 관리가 필요하면 CSS Module이 더 적합하다.

---

## 1.2 Styling Method Comparison

### [개념]

Styling Method Comparison은 Plain CSS, CSS Module, CSS-in-JS, Tailwind CSS, SCSS의 장단점과 적합 상황을 비교하는 기준이다.

Agent는 기존 프로젝트의 스타일링 방식을 우선 확인한 뒤 같은 방식을 따라야 한다.

---

### [핵심]

| 방식         | 장점                  | 단점              | 적합 상황              |
| ------------ | --------------------- | ----------------- | ---------------------- |
| Plain CSS    | 단순함, 표준          | 전역 충돌 가능    | 소규모, 학습, 단순 앱  |
| CSS Module   | scope 안전            | class 조합 필요   | React 중소규모 앱      |
| CSS-in-JS    | 동적 스타일 강함      | 런타임 비용 가능  | 테마, 디자인 시스템    |
| Tailwind CSS | 빠른 개발, scale 강제 | className 길어짐  | 빠른 UI, 컴포넌트 기반 |
| SCSS         | 구조화, mixin         | nesting 남용 위험 | 기존 CSS 확장          |

---

### [실무]

선택 기준:

```text
학원 프로젝트 / 단순 React
→ CSS Module 또는 Plain CSS

컴포넌트 scope 중요
→ CSS Module

동적 스타일 / Theme 중요
→ CSS-in-JS

빠른 UI 작성 / Utility 선호
→ Tailwind CSS

기존 CSS 확장 / 전처리 필요
→ SCSS
```

Review Agent 판단 기준:

```md
- [ ] 프로젝트 내 Styling Method가 일관적인가?
- [ ] 새로운 컴포넌트가 기존 스타일 방식과 맞는가?
- [ ] 여러 방식을 섞는 명확한 이유가 있는가?
- [ ] token 사용 기준이 모든 방식에서 유지되는가?
- [ ] 반응형과 접근성 스타일이 누락되지 않았는가?
```

---

### [FAQ]

Q. 어떤 스타일링 방식이 제일 좋아?
A. 정답은 없다. 팀 숙련도, 프로젝트 규모, 디자인 시스템 필요성, 배포 환경에 따라 선택한다.

Q. 여러 스타일 방식을 섞어도 돼?
A. 가능하지만 명확한 기준 없이 섞으면 유지보수가 어려워진다.

Q. Agent는 새로운 Styling Method를 임의로 도입해도 돼?
A. 아니다. 기존 프로젝트 방식이 있으면 먼저 기존 방식을 따라야 한다.

---

# 2. Plain CSS Rules

## 2.1 Plain CSS

### [개념]

Plain CSS는 별도 스타일링 라이브러리 없이 일반 CSS 파일을 작성하는 방식이다.

Plain CSS는 가장 단순하고 표준적인 방식이지만, 전역 class 충돌과 selector 우선순위 관리가 중요하다.

---

### [핵심]

Plain CSS 장점:

- 단순함
- 러닝 커브 낮음
- 브라우저 기본 기술
- 빌드 도구 의존도 낮음
- 빠른 프로토타입 작성 가능

Plain CSS 단점:

- 전역 충돌 가능
- naming 관리 필요
- 큰 프로젝트에서 유지보수 어려움
- unused CSS 관리 어려움
- selector 우선순위 복잡화 가능

---

### [실무]

Plain CSS 적합 상황:

```text
소규모 프로젝트
학원 프로젝트
빠른 프로토타입
CSS 기초 학습 목적
스타일 구조가 단순한 앱
```

권장 구조:

```text
src/
├─ styles/
│  ├─ reset.css
│  ├─ tokens.css
│  ├─ globals.css
│  └─ utilities.css
├─ components/
│  └─ Button.css
└─ pages/
   └─ MainPage.css
```

Plain CSS 리뷰 기준:

```md
- [ ] class naming 규칙이 있는가?
- [ ] 전역 class 충돌 가능성이 낮은가?
- [ ] selector가 과도하게 깊지 않은가?
- [ ] `!important`를 남용하지 않는가?
- [ ] component style과 page style이 구분되는가?
- [ ] token을 사용하고 있는가?
```

---

### [FAQ]

Q. Plain CSS는 실무에서 안 써?
A. 쓴다. 다만 규모가 커질수록 naming과 scope 관리 규칙이 중요해진다.

Q. Plain CSS에서 가장 조심할 점은?
A. 전역 class 충돌과 selector 우선순위 복잡도다.

Q. Plain CSS는 작은 프로젝트에만 적합해?
A. 작은 프로젝트에 특히 적합하지만 명확한 naming과 구조가 있으면 더 큰 프로젝트에서도 사용할 수 있다.

---

## 2.2 Plain CSS Naming

### [개념]

Plain CSS는 기본적으로 전역 scope를 가진다.

따라서 class naming 규칙 없이 작성하면 다른 화면이나 컴포넌트 스타일과 충돌할 수 있다.

---

### [핵심]

Plain CSS naming 원칙:

- 컴포넌트 단위 prefix 사용
- 역할 기반 이름 사용
- 색상 / 크기 중심 이름 지양
- box, temp, red 같은 모호한 이름 금지
- BEM 또는 유사한 구조 사용 가능
- 상태 class는 `is-active`, `has-error`처럼 명확히 작성

좋은 예:

```css
.festival-card {
}

.festival-card__title {
}

.festival-card--featured {
}
```

나쁜 예:

```css
.box {
}

.red {
}

.big {
}

.temp {
}
```

---

### [실무]

Plain CSS class 구조 예:

```html
<article class="festival-card festival-card--featured">
  <h2 class="festival-card__title">Festival Title</h2>
  <p class="festival-card__description">Description</p>
</article>
```

```css
.festival-card {
  padding: var(--spacing-4);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
}

.festival-card__title {
  font-size: var(--font-size-lg);
}

.festival-card--featured {
  border-color: var(--color-primary);
}
```

---

### [FAQ]

Q. Plain CSS에서 BEM은 꼭 써야 해?
A. 필수는 아니지만 전역 충돌을 줄이고 구조를 명확히 하는 데 유용하다.

Q. class 이름은 짧을수록 좋아?
A. 아니다. 의미가 명확한 이름이 더 중요하다.

Q. blue-button 같은 이름은 괜찮아?
A. 권장하지 않는다. 색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있다.

---

# 3. CSS Module Rules

## 3.1 CSS Module

### [개념]

CSS Module은 CSS class를 파일 단위로 scope 처리해 class 이름 충돌을 줄이는 방식이다.

React 컴포넌트 단위 스타일을 관리할 때 적합하다.

CSS Module 파일은 일반적으로 `ComponentName.module.css` 형식을 사용한다.

---

### [핵심]

CSS Module 특징:

- 파일 단위 scope
- class 이름 충돌 방지
- React 컴포넌트와 결합 쉬움
- build 시 고유 class name 생성
- 전역 스타일과 구분 가능
- 컴포넌트 전용 스타일 관리에 적합

CSS Module 주의:

- 전역 스타일은 별도 global 파일에서 관리
- className 조합이 복잡해질 수 있음
- shared style 분리 기준 필요
- dynamic variant가 많으면 class 조합 유틸 고려

---

### [실무]

파일 구조:

```text
Button.jsx
Button.module.css
```

CSS:

```css
.button {
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-md);
  background: var(--color-primary);
  color: white;
}

.button:hover {
  background: var(--color-primary-hover);
}
```

JSX:

```jsx
import styles from "./Button.module.css";

function Button({ children }) {
  return (
    <button className={styles.button} type="button">
      {children}
    </button>
  );
}
```

CSS Module 리뷰 기준:

```md
- [ ] 파일명이 `*.module.css`인가?
- [ ] 컴포넌트와 가까운 위치에 있는가?
- [ ] global style과 component style이 분리되어 있는가?
- [ ] className 조합이 과도하게 복잡하지 않은가?
- [ ] token을 사용하고 있는가?
- [ ] hover / focus / disabled 상태가 포함되어 있는가?
```

---

### [FAQ]

Q. CSS Module을 쓰면 class 이름 충돌이 없어져?
A. 대부분 줄어든다. build 시 고유 class name으로 변환되기 때문이다.

Q. CSS Module에서도 global style을 만들 수 있어?
A. 가능하지만 남용하지 않는 것이 좋다. 전역 스타일은 별도 global 파일에서 관리하는 것이 명확하다.

Q. CSS Module 파일명은 어떻게 해?
A. 보통 `ComponentName.module.css` 형식을 사용한다.

---

## 3.2 CSS Module Component Structure

### [개념]

CSS Module Component Structure는 컴포넌트 파일과 해당 컴포넌트 전용 스타일 파일을 가까이 배치하는 구조다.

컴포넌트와 스타일의 결합 위치가 명확하면 유지보수와 추적이 쉬워진다.

---

### [핵심]

권장 구조:

```text
src/
└─ components/
   └─ Button/
      ├─ Button.jsx
      ├─ Button.module.css
      └─ index.js
```

페이지 스타일 구조:

```text
src/
└─ pages/
   └─ MainPage/
      ├─ MainPage.jsx
      └─ MainPage.module.css
```

권장 원칙:

- component style은 component와 같은 폴더에 배치
- page layout style은 page 폴더에 배치
- global style은 styles 폴더에 배치
- token은 전역에서 먼저 import

---

### [실무]

컴포넌트 variant 예:

```css
.button {
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
}

.primary {
  background: var(--color-primary);
  color: white;
}

.danger {
  background: var(--color-error);
  color: white;
}

.sm {
  padding: var(--spacing-1) var(--spacing-3);
}

.md {
  padding: var(--spacing-2) var(--spacing-4);
}
```

```jsx
import styles from "./Button.module.css";

function Button({ variant = "primary", size = "md", children }) {
  return (
    <button
      type="button"
      className={`${styles.button} ${styles[variant]} ${styles[size]}`}
    >
      {children}
    </button>
  );
}
```

---

### [FAQ]

Q. CSS Module 파일은 components 폴더 밖에 둬도 돼?
A. 가능하지만 컴포넌트 전용 스타일이라면 컴포넌트와 가까이 두는 것이 유지보수에 좋다.

Q. CSS Module에서 variant는 어떻게 관리해?
A. base class와 variant class를 분리하고 JSX에서 조합해 관리한다.

Q. CSS Module에서도 token을 써야 해?
A. 권장된다. scope는 class 충돌을 줄이고 token은 디자인 일관성을 유지한다.

---

# 4. CSS-in-JS Rules

## 4.1 CSS-in-JS

### [개념]

CSS-in-JS는 JavaScript 또는 TypeScript 파일 안에서 스타일을 작성하는 방식이다.

대표 도구:

- Styled Components
- Emotion

CSS-in-JS는 컴포넌트와 스타일을 강하게 결합하고, props나 theme 기반 동적 스타일을 작성하기 쉽다.

---

### [핵심]

CSS-in-JS 장점:

- 컴포넌트와 스타일 결합
- props 기반 동적 스타일 작성 쉬움
- theme provider 사용 가능
- class naming 고민 감소
- 조건부 스타일 처리 쉬움
- 디자인 시스템 컴포넌트 구현에 적합

CSS-in-JS 단점:

- 런타임 비용 가능
- 번들 크기 증가 가능
- 스타일과 로직 과결합 위험
- SSR 설정 고려 필요
- 디버깅 방식이 달라질 수 있음
- props 분기 과다 위험

---

### [실무]

Styled Components 예:

```jsx
import styled from "styled-components";

const Button = styled.button`
  padding: 8px 16px;
  border-radius: 8px;
  background: ${({ $variant }) =>
    $variant === "primary" ? "var(--color-primary)" : "transparent"};
`;

function PrimaryButton() {
  return <Button $variant="primary">저장</Button>;
}
```

CSS-in-JS 적합 상황:

```text
컴포넌트 중심 개발
theme provider 필요
동적 스타일 많음
디자인 시스템 컴포넌트 구현
상태 기반 스타일 많음
```

CSS-in-JS 리뷰 기준:

```md
- [ ] theme 값이 일관적으로 관리되는가?
- [ ] raw color가 컴포넌트에 흩어지지 않는가?
- [ ] props 기반 style 분기가 과도하지 않은가?
- [ ] DOM에 불필요한 props가 전달되지 않는가?
- [ ] 반복 variant가 구조화되어 있는가?
```

---

### [FAQ]

Q. CSS-in-JS는 무조건 좋은 방식이야?
A. 아니다. 동적 스타일과 테마에는 강하지만 런타임 비용과 복잡도도 고려해야 한다.

Q. Styled Components에서 props 이름 앞에 `$`를 붙이는 이유는?
A. DOM으로 전달되지 않는 transient props로 구분하기 위해 사용한다.

Q. CSS-in-JS는 언제 적합해?
A. theme provider, 동적 스타일, 디자인 시스템 컴포넌트 구현이 중요한 경우 적합하다.

---

## 4.2 Theme Provider Rules

### [개념]

Theme Provider는 CSS-in-JS에서 theme 값을 컴포넌트 전체에 전달하는 구조다.

Theme Provider는 color, spacing, radius 같은 디자인 값을 일관되게 제공한다.

---

### [핵심]

Theme Provider 검토 항목:

- theme 값이 일관적인가?
- raw color가 컴포넌트에 흩어지지 않는가?
- theme 타입이 정의되어 있는가?
- light / dark theme 구조가 있는가?
- props 기반 분기가 과도하지 않은가?
- token과 theme 값의 책임이 명확한가?

---

### [실무]

Theme Provider 예:

```jsx
const theme = {
  colors: {
    primary: "#2563eb",
    text: "#111827",
    background: "#ffffff",
  },
  spacing: {
    sm: "8px",
    md: "16px",
  },
};

<ThemeProvider theme={theme}>
  <App />
</ThemeProvider>;
```

CSS variable과 조합 가능:

```jsx
const Button = styled.button`
  background: var(--color-primary);
  border-radius: ${({ theme }) => theme.radius.md};
`;
```

---

### [FAQ]

Q. Theme Provider는 언제 필요해?
A. CSS-in-JS에서 색상, 간격, theme 값을 컴포넌트 전체에 일관되게 제공할 때 필요하다.

Q. Theme와 CSS variable을 같이 써도 돼?
A. 가능하다. CSS-in-JS theme와 CSS variable을 조합해 사용할 수 있다.

Q. Theme Provider 없이 CSS-in-JS를 써도 돼?
A. 가능하지만 theme 확장과 일관성 관리가 약해질 수 있다.

---

## 4.3 Dynamic Style Rules

### [개념]

Dynamic Style은 props, state, theme에 따라 스타일이 바뀌는 구조다.

CSS-in-JS는 Dynamic Style을 작성하기 쉽지만, 분기가 많아지면 컴포넌트 복잡도가 증가한다.

---

### [핵심]

Dynamic Style 주의:

- dynamic style 분기가 너무 많으면 variant 체계 필요
- DOM에 불필요한 props 전달 금지
- style 계산이 복잡하면 helper로 분리
- theme token 사용
- inline style과 역할 구분
- 상태와 variant 책임 분리

---

### [실무]

Dynamic Style 예:

```jsx
const Badge = styled.span`
  color: ${({ $status }) =>
    $status === "error" ? "var(--color-error)" : "var(--color-success)"};
`;
```

분기 과다 예:

```jsx
const Button = styled.button`
  background: ${({ $variant, $danger, $active, $outline }) => {
    if ($danger) return "red";
    if ($active) return "blue";
    if ($outline) return "transparent";
    return "gray";
  }};
`;
```

개선 방향:

```text
variant mapping 분리
→ 상태 props 분리
→ theme token 사용
→ 컴포넌트 분리 검토
```

---

### [FAQ]

Q. props로 스타일을 많이 바꿔도 돼?
A. 가능하지만 분기가 많아지면 variant 설계나 컴포넌트 분리가 필요하다.

Q. DOM에 스타일용 props가 내려가면 문제야?
A. 불필요한 DOM attribute 경고가 날 수 있다. transient props나 prop filtering을 사용한다.

Q. Dynamic Style이 많아지면 어떻게 해?
A. variant 체계로 정리하거나 컴포넌트를 분리하는 것이 좋다.

---

# 5. Tailwind CSS Rules

## 5.1 Tailwind CSS

### [개념]

Tailwind CSS는 utility class를 조합해 스타일을 작성하는 Utility First CSS 프레임워크다.

Tailwind는 CSS 파일 작성을 줄이고 빠른 UI 구현을 돕지만, className 관리 기준이 필요하다.

---

### [핵심]

Tailwind CSS 장점:

- 빠른 UI 작성
- design scale 강제
- CSS 파일 작성량 감소
- 반응형 class 사용 쉬움
- 상태 class 관리 쉬움
- unused CSS 최적화 가능
- 컴포넌트 기반 개발과 결합 쉬움

Tailwind CSS 단점:

- className이 길어질 수 있음
- 재사용 패턴 추출 기준 필요
- 디자인 토큰 설정 필요
- class 중복 증가 가능
- 조건부 class 관리 복잡 가능
- arbitrary value 남용 위험

---

### [실무]

Tailwind 예:

```jsx
function Card({ title, description }) {
  return (
    <article className="rounded-lg border p-4 shadow-sm">
      <h2 className="text-lg font-bold">{title}</h2>
      <p className="mt-2 text-sm text-gray-600">{description}</p>
    </article>
  );
}
```

Tailwind 적합 상황:

```text
빠른 UI 개발
디자인 scale 강제
컴포넌트 기반 React 프로젝트
작은 팀
스타일 파일 분산을 줄이고 싶을 때
```

Tailwind 리뷰 기준:

```md
- [ ] className이 과도하게 길지 않은가?
- [ ] 반복되는 조합은 컴포넌트로 추출했는가?
- [ ] tailwind.config에 theme token이 정의되어 있는가?
- [ ] arbitrary value 남용이 없는가?
- [ ] responsive / hover / focus 상태가 일관적인가?
```

---

### [FAQ]

Q. Tailwind를 쓰면 CSS Architecture가 필요 없어?
A. 아니다. Tailwind도 token, component extraction, class 관리 기준이 필요하다.

Q. Tailwind className이 너무 길면 어떻게 해?
A. 반복되는 UI는 컴포넌트로 추출하거나 class 조합 유틸을 사용할 수 있다.

Q. Tailwind arbitrary value를 써도 돼?
A. 필요할 때는 가능하지만 남용하면 design scale이 깨진다.

---

## 5.2 Tailwind Project Structure

### [개념]

Tailwind Project Structure는 utility class를 사용하더라도 token, component extraction, class composition 기준을 정하는 구조다.

Tailwind는 CSS 파일이 적어져도 구조 규칙이 필요하다.

---

### [핵심]

Tailwind 구조 기준:

- `tailwind.config.js`에 theme 확장
- 반복 UI는 component로 추출
- arbitrary value 남용 금지
- className 조건부 조합 기준 마련
- design token과 Tailwind theme 연결
- global base style 최소화
- plugin 사용 기준 명확화

---

### [실무]

Tailwind config 예:

```js
export default {
  theme: {
    extend: {
      colors: {
        primary: "#2563eb",
        error: "#dc2626",
      },
      borderRadius: {
        card: "12px",
      },
    },
  },
};
```

Tailwind 구조 리뷰 기준:

```md
- [ ] 같은 class 조합이 반복되지 않는가?
- [ ] 반복 UI가 컴포넌트로 추출되었는가?
- [ ] `w-[437px]` 같은 arbitrary value가 남용되지 않는가?
- [ ] hover / focus / disabled 상태가 포함되어 있는가?
- [ ] responsive class가 일관적인가?
- [ ] tailwind.config가 프로젝트 token 역할을 하는가?
```

---

### [FAQ]

Q. Tailwind에서는 CSS 파일이 필요 없어?
A. 대부분 줄어들지만 global style, font, base reset, 일부 custom style은 필요할 수 있다.

Q. Tailwind config는 왜 중요해?
A. 색상, spacing, radius 같은 theme 값을 프로젝트 기준으로 통일하기 위해 중요하다.

Q. Tailwind도 token이 필요해?
A. 필요하다. Tailwind theme 설정이 token 역할을 하며 arbitrary value 남용을 줄인다.

---

## 5.3 Tailwind Class Composition

### [개념]

Tailwind Class Composition은 조건부 class와 variant class를 안전하게 조합하는 방식이다.

조건부 class가 많아질수록 문자열 조합이 복잡해지므로 유틸리티 사용을 고려한다.

---

### [핵심]

권장:

- 조건부 class는 `clsx` 등으로 명확히 관리
- variant는 객체 mapping으로 분리 가능
- 반복되는 class는 컴포넌트화
- class merge 충돌 주의
- Tailwind class 순서 일관성 유지
- disabled / focus / hover 상태 포함

---

### [실무]

clsx 사용 예:

```jsx
import clsx from "clsx";

function Button({ variant = "primary", disabled, children }) {
  return (
    <button
      type="button"
      disabled={disabled}
      className={clsx(
        "rounded-md px-4 py-2 font-medium",
        variant === "primary" && "bg-blue-600 text-white",
        variant === "secondary" && "border bg-white text-gray-900",
        disabled && "cursor-not-allowed opacity-50",
      )}
    >
      {children}
    </button>
  );
}
```

variant mapping 예:

```jsx
const variantClass = {
  primary: "bg-blue-600 text-white",
  secondary: "border bg-white text-gray-900",
  danger: "bg-red-600 text-white",
};
```

---

### [FAQ]

Q. 조건부 Tailwind class는 삼항 연산자로 계속 써도 돼?
A. 간단한 경우는 가능하지만 복잡해지면 clsx나 variant helper로 분리하는 것이 좋다.

Q. Tailwind에서 variant가 많아지면 어떻게 해?
A. Button, Card 같은 컴포넌트 내부에서 variant mapping을 만들거나 별도 유틸로 분리한다.

Q. Tailwind class 충돌은 어떻게 줄여?
A. class 조합 순서를 일관되게 유지하고 필요하면 class merge 유틸을 사용한다.

---

# 6. SCSS / Sass Rules

## 6.1 SCSS / Sass

### [개념]

SCSS / Sass는 CSS에 변수, nesting, mixin, function 같은 기능을 추가한 CSS 전처리기다.

SCSS는 기존 CSS를 구조화하는 데 유용하지만, nesting과 mixin을 남용하면 selector 복잡도가 증가한다.

---

### [핵심]

SCSS 장점:

- nesting 가능
- 변수 사용 가능
- mixin 재사용 가능
- partial 파일 분리 가능
- CSS 구조화에 유리
- 기존 CSS 확장에 적합

SCSS 단점:

- CSS variable과 역할 중복 가능
- nesting 남용 시 selector 복잡
- build 설정 필요
- 전역 충돌은 여전히 관리 필요
- mixin 남용 시 추적 어려움

---

### [실무]

SCSS 예:

```scss
.card {
  padding: var(--spacing-4);
  border: 1px solid var(--color-border);

  &__title {
    font-size: var(--font-size-lg);
    font-weight: var(--font-weight-bold);
  }
}
```

SCSS 적합 상황:

```text
기존 CSS 확장
partial 파일 분리 필요
nesting이 일부 필요한 경우
mixin으로 반복 패턴 관리 필요
Plain CSS보다 구조화 필요
```

SCSS 리뷰 기준:

```md
- [ ] nesting 깊이가 과하지 않은가?
- [ ] mixin이 남용되지 않는가?
- [ ] partial 구조가 명확한가?
- [ ] CSS variable과 Sass variable 역할이 구분되는가?
- [ ] 전역 selector 충돌 가능성이 없는가?
```

---

### [FAQ]

Q. SCSS nesting은 깊게 써도 돼?
A. 권장하지 않는다. nesting이 깊으면 selector가 복잡해지고 override가 어려워진다.

Q. Sass variable과 CSS variable 중 뭐가 좋아?
A. Sass variable은 빌드 시점 값이고 CSS variable은 런타임 변경과 theme에 유리하다.

Q. SCSS를 쓰면 CSS 충돌이 없어져?
A. 아니다. SCSS도 최종적으로 CSS로 변환되므로 naming과 scope 관리가 필요하다.

---

## 6.2 SCSS Nesting Rules

### [개념]

SCSS Nesting은 selector를 중첩해서 작성하는 기능이다.

Nesting은 편리하지만 깊어질수록 specificity와 override 문제가 커진다.

---

### [핵심]

권장:

- nesting 깊이는 2단계 이하 권장
- BEM 구조와 조합 가능
- 상태 selector는 가까운 위치에 작성
- media query nesting은 과하지 않게 사용
- 긴 selector chain 생성 금지

주의:

- 중첩이 깊으면 CSS 결과물이 복잡해짐
- component 외부 구조에 의존하기 쉬움
- override가 어려워짐
- 재사용성이 낮아짐

---

### [실무]

나쁜 예:

```scss
.page {
  .section {
    .container {
      .card {
        .title {
          span {
            color: red;
          }
        }
      }
    }
  }
}
```

좋은 예:

```scss
.card {
  padding: var(--spacing-4);

  &__title {
    font-size: var(--font-size-lg);
  }

  &--featured {
    border-color: var(--color-primary);
  }
}
```

SCSS nesting 리뷰 기준:

```md
- [ ] selector 중첩이 2단계 이하인가?
- [ ] 부모 page 구조에 과하게 의존하지 않는가?
- [ ] 결과 selector가 불필요하게 길지 않은가?
- [ ] 상태와 modifier가 명확하게 분리되어 있는가?
```

---

### [FAQ]

Q. SCSS nesting은 어느 정도까지 괜찮아?
A. 일반적으로 2단계 이하가 좋다. 깊어질수록 selector 복잡도가 커진다.

Q. nesting을 많이 쓰면 왜 문제야?
A. 결과 CSS selector가 길어지고 specificity가 높아져 override가 어려워진다.

Q. SCSS에서 BEM을 같이 써도 돼?
A. 가능하다. nesting과 BEM을 함께 쓰면 구조를 명확히 할 수 있다.

---

# 7. Styling Method Mixing Rules

## 7.1 Multiple Styling Methods

### [개념]

Multiple Styling Methods는 하나의 프로젝트에서 여러 스타일링 방식을 함께 사용하는 상황이다.

여러 방식을 섞는 것은 가능하지만 명확한 역할 분리 없이 섞으면 유지보수 비용이 증가한다.

---

### [핵심]

혼합 사용 가능 예:

- Global Style은 Plain CSS
- Component Style은 CSS Module
- Design Token은 CSS Variable
- 일부 외부 UI Library override는 별도 CSS
- Tailwind와 component extraction 병행

위험한 혼합 예:

- 같은 컴포넌트에 CSS Module과 global class 혼용
- Tailwind와 CSS Module을 기준 없이 혼용
- CSS-in-JS와 SCSS가 같은 역할을 중복
- reset / global / component style 책임 불명확
- override가 여러 파일에 분산

---

### [실무]

권장 혼합 구조 예:

```text
src/styles/reset.css
→ Reset

src/styles/tokens.css
→ Design Token

src/styles/globals.css
→ Global Style

components/Button/Button.module.css
→ Component Style
```

혼합 사용 리뷰 기준:

```md
- [ ] 각 Styling Method의 책임이 명확한가?
- [ ] 같은 역할을 여러 방식이 중복 담당하지 않는가?
- [ ] 신규 코드가 기존 프로젝트 기준을 따르는가?
- [ ] override 위치가 명확한가?
- [ ] 유지보수자가 스타일 위치를 예측할 수 있는가?
```

---

### [FAQ]

Q. Plain CSS와 CSS Module을 같이 써도 돼?
A. 가능하다. global/reset/token은 Plain CSS, 컴포넌트 전용 스타일은 CSS Module로 분리할 수 있다.

Q. Tailwind와 CSS Module을 같이 써도 돼?
A. 가능하지만 역할 기준이 명확해야 한다. 기준 없이 섞으면 유지보수가 어려워진다.

Q. Styling Method를 섞을 때 가장 중요한 것은?
A. 각 방식의 책임과 적용 범위를 명확히 정하는 것이다.

---

## 7.2 Styling Method Migration

### [개념]

Styling Method Migration은 기존 프로젝트의 스타일링 방식을 다른 방식으로 변경하는 작업이다.

Migration은 비용이 크므로 필요한 범위와 기준을 명확히 해야 한다.

---

### [핵심]

Migration이 필요한 경우:

- 전역 CSS 충돌이 심각함
- 컴포넌트 재사용이 어려움
- token 체계가 없음
- theme / dark mode 추가 필요
- style duplication이 과도함
- 유지보수 비용이 커짐

Migration 주의:

- 한 번에 전체 변경 지양
- 신규 컴포넌트부터 적용 가능
- token 먼저 도입 권장
- reset / global 정리 우선
- page 단위 또는 component 단위로 점진 적용

---

### [실무]

점진적 Migration Flow:

```text
Current Styling Method 분석
→ Global / Component 책임 분리
→ Design Token 도입
→ 신규 컴포넌트 기준 정의
→ 중복 스타일 제거
→ 위험도 높은 global style 정리
→ page 또는 component 단위 migration
→ Review Checklist 적용
```

Migration 검토 기준:

```md
- [ ] migration 이유가 명확한가?
- [ ] 기존 스타일 영향 범위를 파악했는가?
- [ ] token 도입이 먼저 이루어졌는가?
- [ ] 점진 적용 계획이 있는가?
- [ ] regression UI 검토가 가능한가?
```

---

### [FAQ]

Q. Styling Method를 프로젝트 중간에 바꿔도 돼?
A. 가능하지만 비용이 크다. 기존 방식과 신규 방식이 섞이면 유지보수가 어려워질 수 있다.

Q. Migration은 한 번에 하는 게 좋아?
A. 보통은 점진적으로 하는 것이 안전하다. token과 global 정리부터 시작하는 것이 좋다.

Q. CSS Module로 바꾸면 모든 문제가 해결돼?
A. 아니다. class 충돌은 줄어들지만 token, 반응형, 접근성, 중복 문제는 별도로 관리해야 한다.

---

# 8. Agent Styling Method Rules

## 8.1 Frontend Agent Styling Method Rules

### [개념]

Frontend Agent는 스타일 코드를 생성하기 전에 프로젝트의 기존 Styling Method를 확인해야 한다.

Agent는 임의로 새로운 스타일링 방식을 도입하지 않는다.

---

### [핵심]

Frontend Agent 규칙:

- 기존 Styling Method 우선 확인
- 기존 파일 구조 확인
- token 사용 여부 확인
- component style 위치 확인
- global style 수정 최소화
- 새로운 library 도입 지양
- 기존 naming convention 유지
- 반응형과 접근성 상태 포함

---

### [실무]

Frontend Agent 작업 Flow:

```text
Styling Request
→ Existing Styling Method 확인
→ File Structure 확인
→ Token 확인
→ Component / Page Style 위치 결정
→ Style 작성
→ Responsive 적용
→ Interaction State 적용
→ Accessibility 확인
→ Review Agent 전달
```

생성 금지에 가까운 경우:

```text
기존 프로젝트는 CSS Module인데 임의로 styled-components 도입
기존 프로젝트는 Plain CSS인데 특정 컴포넌트만 Tailwind 사용
token이 있는데 raw color 반복 작성
global style에 컴포넌트 스타일 추가
```

---

### [FAQ]

Q. Frontend Agent가 스타일 라이브러리를 새로 추가해도 돼?
A. 명확한 요구나 승인 없이 새 라이브러리를 도입하면 안 된다.

Q. 기존 프로젝트가 Plain CSS면 Agent도 Plain CSS를 따라야 해?
A. 기본적으로 그렇다. 다만 CSS 충돌 문제가 명확하면 개선 제안을 분리해서 해야 한다.

Q. token이 없으면 Agent가 어떻게 해야 해?
A. 반복 값이 있다면 token 추가 제안을 하거나 최소한 raw value 남용을 피해야 한다.

---

## 8.2 Review Agent Styling Method Rules

### [개념]

Review Agent는 Styling Method가 프로젝트 기준과 일치하는지 검토한다.

Review Agent는 화면 결과뿐 아니라 구조, 유지보수성, 반응형, 접근성까지 확인해야 한다.

---

### [핵심]

Review Agent 검토 항목:

- Styling Method 일관성
- File Structure 일관성
- token 사용 여부
- global / component 분리
- page / component style 분리
- naming convention 일관성
- className 조합 복잡도
- dynamic style 분기 복잡도
- Tailwind arbitrary value 남용
- SCSS nesting 과다
- CSS-in-JS props 분기 과다

---

### [실무]

Review Agent 판단 Flow:

```text
Styling Method 확인
→ 기존 방식과 비교
→ File Structure 확인
→ Token 사용 확인
→ Scope 충돌 가능성 확인
→ Responsive 확인
→ Accessibility 확인
→ Duplication 확인
→ Final Review
```

Review 결과 예:

```text
Approved
→ 기존 방식 준수 + token 사용 + 반응형/접근성 문제 없음

Needs Fix
→ 일부 raw value 반복, className 복잡, focus 누락

Rejected
→ Styling Method 임의 변경, global 오염, 모바일 깨짐, 접근성 심각
```

---

### [FAQ]

Q. Review Agent는 스타일 코드에서 가장 먼저 뭘 봐야 해?
A. 기존 Styling Method와 일치하는지, token과 scope 기준을 따르는지 먼저 봐야 한다.

Q. 화면상 예쁘면 승인해도 돼?
A. 아니다. 유지보수성, 반응형, 접근성, 중복, 충돌 가능성도 검토해야 한다.

Q. Styling Method가 섞여 있으면 무조건 Reject야?
A. 아니다. 역할 기준이 명확하면 가능하지만 기준 없이 섞였으면 수정이 필요하다.

---

# 9. Part03 Quality Checklist

## 9.1 Styling Method Checklist

### [개념]

Part03 단계에서는 Styling Method 선택 기준과 각 방식의 사용 규칙이 명확한지 검토한다.

이 단계는 프로젝트 스타일링 방식의 일관성을 유지하기 위한 기준이다.

---

### [핵심]

Part03 체크리스트:

```md
## Styling Method

- [ ] Styling Method 선택 기준이 명확한가?
- [ ] Plain CSS / CSS Module / CSS-in-JS / Tailwind / SCSS 비교가 포함되어 있는가?
- [ ] 프로젝트 규모와 팀 숙련도 기준이 포함되어 있는가?
- [ ] 기존 Styling Method 우선 원칙이 있는가?

## Plain CSS

- [ ] 전역 충돌 위험을 설명하는가?
- [ ] naming convention 기준이 있는가?
- [ ] BEM 또는 prefix 구조를 안내하는가?

## CSS Module

- [ ] `*.module.css` 파일명 기준이 있는가?
- [ ] component와 가까운 위치 기준이 있는가?
- [ ] global style과 component style 분리 기준이 있는가?

## CSS-in-JS

- [ ] theme provider 기준이 있는가?
- [ ] dynamic style 주의사항이 있는가?
- [ ] transient props 기준이 포함되어 있는가?

## Tailwind CSS

- [ ] tailwind.config token 기준이 있는가?
- [ ] class composition 기준이 있는가?
- [ ] arbitrary value 남용 경고가 있는가?

## SCSS

- [ ] nesting 깊이 주의가 있는가?
- [ ] Sass variable과 CSS variable 차이를 설명하는가?
- [ ] selector 복잡도 경고가 있는가?

## Agent Review

- [ ] Frontend Agent 규칙이 있는가?
- [ ] Review Agent 규칙이 있는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Part03 승인 기준:

```text
Styling Method 선택 기준 명확
+ 각 방식별 장단점 포함
+ 기존 방식 우선 원칙 포함
+ Agent 생성 / 검토 기준 포함
+ FAQ 충분
+ Retrieval Queries 포함
→ Part03 승인 가능
```

Part03 보류 기준:

```text
특정 Styling Method를 무조건 정답처럼 설명
또는 기존 프로젝트 방식 확인 없이 신규 방식 도입 권장
또는 장단점 비교 부족
또는 Agent 검토 기준 부족
→ 재작성 필요
```

---

### [FAQ]

Q. Part03의 핵심 목적은 뭐야?
A. 프로젝트에 맞는 Styling Method를 선택하고, 기존 방식과 일관된 스타일 코드를 생성·검토할 기준을 정하는 것이다.

Q. Part03에서 가장 위험한 문제는 뭐야?
A. 특정 Styling Method를 무조건 정답처럼 설명하거나 기존 프로젝트 방식과 무관하게 새 방식을 도입하는 것이다.

Q. Part03 다음에는 뭘 다루는 게 자연스러워?
A. Naming Convention, Component Styling, Variant Style, State Class 같은 컴포넌트 스타일 규칙을 다루는 것이 자연스럽다.

---

# Retrieval Queries

### [FAQ]

Q. Styling Method가 뭐야?
A. 프론트엔드 프로젝트에서 스타일 코드를 작성하고 관리하는 방식이다.

Q. 대표 Styling Method는 뭐가 있어?
A. Plain CSS, CSS Module, CSS-in-JS, Tailwind CSS, SCSS / Sass가 있다.

Q. Styling Method는 어떻게 선택해?
A. 프로젝트 규모, 팀 숙련도, 컴포넌트 scope 필요성, theme 필요성, 동적 스타일 비중, 유지보수 기간을 기준으로 선택한다.

Q. Styling Method는 아무거나 골라도 돼?
A. 아니다. 프로젝트 조건과 기존 스타일 구조를 기준으로 선택해야 한다.

Q. 한 프로젝트에서 여러 Styling Method를 섞어도 돼?
A. 가능하지만 명확한 기준 없이 섞으면 유지보수가 어려워진다.

Q. 어떤 스타일링 방식이 제일 좋아?
A. 정답은 없다. 팀 숙련도, 프로젝트 규모, 디자인 시스템 필요성, 배포 환경에 따라 선택한다.

Q. 학원 React 프로젝트에서는 뭐가 무난해?
A. Plain CSS 또는 CSS Module이 무난하다. 컴포넌트 단위 관리가 필요하면 CSS Module이 더 적합하다.

Q. Plain CSS는 뭐야?
A. 별도 스타일링 라이브러리 없이 일반 CSS 파일을 작성하는 방식이다.

Q. Plain CSS 장점은 뭐야?
A. 단순하고 러닝 커브가 낮으며 브라우저 기본 기술이라 빠르게 사용할 수 있다.

Q. Plain CSS 단점은 뭐야?
A. 전역 class 충돌, naming 관리 부담, selector 우선순위 복잡도, unused CSS 문제가 생길 수 있다.

Q. Plain CSS는 언제 적합해?
A. 소규모 프로젝트, 학원 프로젝트, 빠른 프로토타입, 단순한 앱에 적합하다.

Q. Plain CSS에서 가장 조심할 점은?
A. 전역 class 충돌과 selector 우선순위 복잡도다.

Q. Plain CSS에서 BEM은 꼭 써야 해?
A. 필수는 아니지만 전역 충돌을 줄이고 구조를 명확히 하는 데 유용하다.

Q. Plain CSS class 이름은 어떻게 지어야 해?
A. 컴포넌트 단위 prefix와 역할 기반 이름을 사용하는 것이 좋다.

Q. blue-button 같은 class 이름은 괜찮아?
A. 권장하지 않는다. 색상이 바뀌면 이름과 실제 스타일이 어긋날 수 있다.

Q. CSS Module은 뭐야?
A. CSS class를 파일 단위로 scope 처리해 class 이름 충돌을 줄이는 방식이다.

Q. CSS Module은 언제 적합해?
A. React 컴포넌트 단위 스타일을 안전하게 관리하고 class 충돌을 줄이고 싶을 때 적합하다.

Q. CSS Module 장점은 뭐야?
A. 파일 단위 scope, class 충돌 방지, React 컴포넌트와 결합 쉬움, 전역 스타일과 구분 가능성이 장점이다.

Q. CSS Module 단점은 뭐야?
A. className 조합이 복잡해질 수 있고 shared style 분리 기준이 필요하다.

Q. CSS Module 파일명은 어떻게 해?
A. 보통 `ComponentName.module.css` 형식을 사용한다.

Q. CSS Module 파일은 어디에 두는 게 좋아?
A. 컴포넌트 전용 스타일이라면 컴포넌트와 가까운 위치에 두는 것이 좋다.

Q. CSS Module에서도 global style을 만들 수 있어?
A. 가능하지만 남용하지 않는 것이 좋다. 전역 스타일은 별도 global 파일에서 관리하는 것이 명확하다.

Q. CSS Module에서 variant는 어떻게 관리해?
A. base class와 variant class를 분리하고 JSX에서 조합해 관리한다.

Q. CSS-in-JS는 뭐야?
A. JavaScript 또는 TypeScript 파일 안에서 스타일을 작성하는 방식이다.

Q. CSS-in-JS 대표 도구는 뭐야?
A. Styled Components와 Emotion이 대표적이다.

Q. CSS-in-JS 장점은 뭐야?
A. 컴포넌트와 스타일 결합, props 기반 동적 스타일, theme provider, 조건부 스타일 처리에 강하다.

Q. CSS-in-JS 단점은 뭐야?
A. 런타임 비용, 번들 크기 증가, 스타일과 로직 과결합, SSR 설정 고려, props 분기 과다 문제가 있을 수 있다.

Q. CSS-in-JS는 언제 적합해?
A. theme provider, 동적 스타일, 디자인 시스템 컴포넌트 구현이 중요한 경우 적합하다.

Q. CSS-in-JS는 무조건 좋은 방식이야?
A. 아니다. 동적 스타일과 테마에는 강하지만 런타임 비용과 복잡도도 고려해야 한다.

Q. Styled Components에서 props 이름 앞에 `$`를 붙이는 이유는?
A. DOM으로 전달되지 않는 transient props로 구분하기 위해 사용한다.

Q. Theme Provider는 언제 필요해?
A. CSS-in-JS에서 색상, 간격, theme 값을 컴포넌트 전체에 일관되게 제공할 때 필요하다.

Q. Theme와 CSS variable을 같이 써도 돼?
A. 가능하다. CSS-in-JS theme와 CSS variable을 조합해 사용할 수 있다.

Q. Dynamic Style은 뭐야?
A. props, state, theme에 따라 스타일이 바뀌는 구조다.

Q. props로 스타일을 많이 바꿔도 돼?
A. 가능하지만 분기가 많아지면 variant 설계나 컴포넌트 분리가 필요하다.

Q. DOM에 스타일용 props가 내려가면 문제야?
A. 불필요한 DOM attribute 경고가 날 수 있다. transient props나 prop filtering을 사용한다.

Q. Tailwind CSS는 뭐야?
A. utility class를 조합해 스타일을 작성하는 Utility First CSS 프레임워크다.

Q. Tailwind CSS 장점은 뭐야?
A. 빠른 UI 작성, design scale 강제, CSS 파일 작성량 감소, 반응형과 상태 class 관리가 쉽다.

Q. Tailwind CSS 단점은 뭐야?
A. className이 길어질 수 있고, class 중복과 조건부 class 관리가 복잡해질 수 있다.

Q. Tailwind는 언제 적합해?
A. 빠른 UI 개발, 디자인 scale 강제, 컴포넌트 기반 React 프로젝트, 작은 팀에 적합하다.

Q. Tailwind를 쓰면 CSS Architecture가 필요 없어?
A. 아니다. Tailwind도 token, component extraction, class 관리 기준이 필요하다.

Q. Tailwind className이 너무 길면 어떻게 해?
A. 반복되는 UI는 컴포넌트로 추출하거나 class 조합 유틸을 사용할 수 있다.

Q. Tailwind arbitrary value를 써도 돼?
A. 필요할 때는 가능하지만 남용하면 design scale이 깨진다.

Q. Tailwind config는 왜 중요해?
A. 색상, spacing, radius 같은 theme 값을 프로젝트 기준으로 통일하기 위해 중요하다.

Q. Tailwind 조건부 class는 어떻게 관리해?
A. 간단한 경우 삼항 연산자로 가능하지만 복잡해지면 clsx나 variant helper를 사용한다.

Q. Tailwind에서 variant가 많아지면 어떻게 해?
A. Button, Card 같은 컴포넌트 내부에서 variant mapping을 만들거나 별도 유틸로 분리한다.

Q. SCSS / Sass는 뭐야?
A. CSS에 변수, nesting, mixin, function 같은 기능을 추가한 CSS 전처리기다.

Q. SCSS 장점은 뭐야?
A. nesting, 변수, mixin, partial 파일 분리로 CSS를 구조화하기 쉽다.

Q. SCSS 단점은 뭐야?
A. nesting 남용 시 selector가 복잡해지고 전역 충돌은 여전히 관리해야 한다.

Q. SCSS는 언제 적합해?
A. 기존 CSS를 구조화하고 nesting, mixin, partial 파일 분리가 필요한 경우 적합하다.

Q. SCSS nesting은 깊게 써도 돼?
A. 권장하지 않는다. nesting이 깊으면 selector가 복잡해지고 override가 어려워진다.

Q. Sass variable과 CSS variable 중 뭐가 좋아?
A. Sass variable은 빌드 시점 값이고 CSS variable은 런타임 변경과 theme에 유리하다.

Q. SCSS를 쓰면 CSS 충돌이 없어져?
A. 아니다. SCSS도 최종적으로 CSS로 변환되므로 naming과 scope 관리가 필요하다.

Q. Plain CSS와 CSS Module을 같이 써도 돼?
A. 가능하다. global/reset/token은 Plain CSS, 컴포넌트 전용 스타일은 CSS Module로 분리할 수 있다.

Q. Tailwind와 CSS Module을 같이 써도 돼?
A. 가능하지만 역할 기준이 명확해야 한다. 기준 없이 섞으면 유지보수가 어려워진다.

Q. Styling Method를 섞을 때 가장 중요한 것은?
A. 각 방식의 책임과 적용 범위를 명확히 정하는 것이다.

Q. Styling Method Migration은 뭐야?
A. 기존 프로젝트의 스타일링 방식을 다른 방식으로 변경하는 작업이다.

Q. Styling Method를 프로젝트 중간에 바꿔도 돼?
A. 가능하지만 비용이 크다. 기존 방식과 신규 방식이 섞이면 유지보수가 어려워질 수 있다.

Q. Migration은 한 번에 하는 게 좋아?
A. 보통은 점진적으로 하는 것이 안전하다. token과 global 정리부터 시작하는 것이 좋다.

Q. CSS Module로 바꾸면 모든 문제가 해결돼?
A. 아니다. class 충돌은 줄어들지만 token, 반응형, 접근성, 중복 문제는 별도로 관리해야 한다.

Q. Frontend Agent는 Styling Method를 어떻게 선택해?
A. 기존 프로젝트의 Styling Method, 파일 구조, token 사용 여부를 먼저 확인하고 같은 기준을 따른다.

Q. Frontend Agent가 스타일 라이브러리를 새로 추가해도 돼?
A. 명확한 요구나 승인 없이 새 라이브러리를 도입하면 안 된다.

Q. 기존 프로젝트가 Plain CSS면 Agent도 Plain CSS를 따라야 해?
A. 기본적으로 그렇다. 다만 CSS 충돌 문제가 명확하면 개선 제안을 분리해서 해야 한다.

Q. Review Agent는 Styling Method에서 뭘 검토해?
A. 기존 방식과의 일관성, token 사용, scope 분리, className 복잡도, 반응형, 접근성을 검토한다.

Q. Styling Method가 섞여 있으면 무조건 Reject야?
A. 아니다. 역할 기준이 명확하면 가능하지만 기준 없이 섞였으면 수정이 필요하다.

Q. Part03의 핵심 목적은 뭐야?
A. 프로젝트에 맞는 Styling Method를 선택하고, 기존 방식과 일관된 스타일 코드를 생성·검토할 기준을 정하는 것이다.

Q. Part03에서 가장 위험한 문제는 뭐야?
A. 특정 Styling Method를 무조건 정답처럼 설명하거나 기존 프로젝트 방식과 무관하게 새 방식을 도입하는 것이다.

Q. Part03 다음에는 뭘 다루는 게 자연스러워?
A. Naming Convention, Component Styling, Variant Style, State Class 같은 컴포넌트 스타일 규칙을 다루는 것이 자연스럽다.
