# HTML CSS Foundation Part10 - Responsive Media Query

---

# 1. Responsive Web Design

## 1.1 Responsive Web Design Concept

### [개념]

Responsive Web Design은 하나의 웹 페이지가 다양한 화면 크기와 입력 환경에서 깨지지 않고 읽기 쉽고 사용 가능하도록 만드는 설계 방식이다.

Responsive Web Design은 단순히 화면 크기만 줄이는 것이 아니라 Layout, Typography, Image, Table, Form, Navigation, Modal, Touch Target을 화면 조건에 맞게 조정하는 것이다.

---

### [핵심]

Responsive Web Design 핵심:

- 다양한 viewport width에 대응한다.
- 모바일, 태블릿, 데스크톱 화면을 고려한다.
- 고정 width보다 유동 width를 우선한다.
- `max-width`, `%`, `min()`, `clamp()`를 활용한다.
- 이미지와 미디어가 부모를 넘지 않게 한다.
- Flexbox와 Grid는 반응형 Layout의 핵심 도구다.
- media query로 breakpoint 조건을 적용한다.
- 모바일 터치 환경에서는 touch target을 고려한다.
- horizontal overflow를 피한다.
- 작은 화면에서 콘텐츠 우선순위를 명확히 한다.

---

### [실무]

2026 실무 기준에서 Responsive Web Design은 기본 품질 요구사항이다.

Frontend Agent는 Responsive CSS 작성 시 아래를 함께 검토해야 한다.

- Viewport meta 존재 여부
- Mobile First 적용 여부
- Fixed width 사용 여부
- Container width
- Flex wrap
- Grid minmax
- Responsive image
- Responsive typography
- Touch target
- Horizontal overflow
- Table overflow
- Modal viewport fit
- Fixed header/footer overlap

Responsive Design Flow:

```text
Mobile View 기준 작성
→ Fluid Container 적용
→ Image Responsive 처리
→ Flex/Grid Layout 작성
→ 필요한 Breakpoint 추가
→ Typography 조정
→ Touch Target 확인
→ Horizontal Overflow 확인
→ Desktop 확장 검수
```

---

### [FAQ]

Q. Responsive Web Design이 뭐야?
A. 하나의 웹 페이지가 다양한 화면 크기에서 깨지지 않고 읽기 쉽고 사용 가능하도록 만드는 설계 방식이다.

Q. 반응형은 media query만 쓰면 끝이야?
A. 아니다. fluid width, responsive image, flex/grid, typography, touch target, overflow 검수가 함께 필요하다.

Q. Responsive Design에서 가장 먼저 볼 것은?
A. viewport meta, fixed width, horizontal overflow, image overflow를 먼저 확인한다.

Q. 모바일 기준으로 먼저 만드는 게 좋아?
A. 일반적으로 Mobile First 방식이 유지보수와 확장성에 유리하다.

---

# 2. Viewport

## 2.1 Viewport Concept

### [개념]

Viewport는 사용자가 웹 페이지를 볼 수 있는 브라우저의 표시 영역이다.

Responsive Web Design에서는 viewport width를 기준으로 layout과 typography를 조정한다.

HTML 문서에는 모바일 브라우저가 페이지 폭을 올바르게 해석하도록 viewport meta가 필요하다.

예:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

---

### [핵심]

Viewport 핵심:

- viewport는 브라우저의 표시 영역이다.
- 모바일 브라우저는 viewport meta가 없으면 desktop width처럼 렌더링할 수 있다.
- `width=device-width`는 viewport 폭을 device width에 맞춘다.
- `initial-scale=1.0`은 초기 확대 비율을 지정한다.
- responsive media query는 viewport width 조건과 연결된다.
- viewport unit에는 `vw`, `vh`, `dvh`, `svh`, `lvh` 등이 있다.
- 모바일 브라우저 UI 변화 때문에 height unit 사용 시 주의가 필요하다.

---

### [실무]

기본 head 예:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Responsive Page</title>
</head>
```

Viewport Unit 예:

```css
.hero {
  min-height: 100dvh;
}
```

주의:

```css
.full-width {
  width: 100vw;
}
```

`100vw`는 scrollbar width까지 포함해 horizontal overflow를 만들 수 있다.

검수 기준:

- viewport meta가 있는가?
- 모바일에서 페이지가 축소된 desktop처럼 보이지 않는가?
- `100vw`로 horizontal overflow가 생기지 않는가?
- viewport height unit 사용 시 mobile browser UI를 고려했는가?
- fixed header/footer가 viewport 안에서 콘텐츠를 가리지 않는가?

---

### [FAQ]

Q. Viewport가 뭐야?
A. 사용자가 웹 페이지를 볼 수 있는 브라우저 표시 영역이다.

Q. viewport meta는 왜 필요해?
A. 모바일 브라우저가 페이지 폭을 device width 기준으로 올바르게 렌더링하도록 하기 위해 필요하다.

Q. width=device-width는 뭐야?
A. viewport 폭을 기기 화면 폭에 맞추도록 지정하는 값이다.

Q. 100vw를 쓰면 왜 가로 스크롤이 생길 수 있어?
A. scrollbar 폭까지 포함해 계산될 수 있어 body보다 넓어질 수 있기 때문이다.

---

# 3. Mobile First

## 3.1 Mobile First Concept

### [개념]

Mobile First는 작은 화면 기준으로 기본 CSS를 작성하고, 화면이 커질수록 media query로 확장하는 반응형 설계 방식이다.

기본 CSS는 mobile layout이고, `min-width` media query로 tablet/desktop layout을 추가한다.

---

### [핵심]

Mobile First 핵심:

- 작은 화면을 기본값으로 작성한다.
- 큰 화면 조건은 `@media (min-width: ...)`로 추가한다.
- 기본 layout이 단순하다.
- 불필요한 override가 줄어든다.
- 모바일 성능과 UX를 우선 고려할 수 있다.
- desktop 중심 layout을 mobile로 억지로 줄이는 문제를 줄인다.
- component 단위 responsive 설계와 잘 맞는다.

---

### [실무]

Mobile First 예:

```css
.card-grid {
  display: grid;
  gap: var(--space-4);
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

검수 기준:

- 기본 CSS가 모바일에서 동작하는가?
- breakpoint가 커질수록 layout이 확장되는가?
- min-width와 max-width를 혼동하지 않았는가?
- desktop style을 mobile에서 과도하게 override하지 않는가?
- 작은 화면에서 핵심 콘텐츠가 먼저 보이는가?

---

### [FAQ]

Q. Mobile First가 뭐야?
A. 모바일 화면을 기본 CSS로 작성하고 큰 화면에서 min-width media query로 확장하는 방식이다.

Q. Mobile First는 왜 좋아?
A. 작은 화면에서 기본 사용성을 확보하고 큰 화면 확장을 단계적으로 관리하기 쉽기 때문이다.

Q. Mobile First에서는 min-width를 써?
A. 일반적으로 큰 화면 조건을 추가할 때 `min-width` media query를 사용한다.

Q. Desktop First와 뭐가 달라?
A. Desktop First는 큰 화면 기준으로 작성하고 작은 화면에서 max-width로 줄이는 방식이다.

---

# 4. Media Query

## 4.1 Media Query Concept

### [개념]

Media Query는 viewport width, device 특성, 사용자 환경 조건에 따라 CSS를 조건부로 적용하는 문법이다.

Responsive Layout에서는 주로 `min-width` 또는 `max-width` 조건을 사용한다.

기본 예:

```css
@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
}
```

---

### [핵심]

Media Query 핵심:

- 조건이 true일 때 내부 CSS가 적용된다.
- viewport width 조건에 자주 사용한다.
- Mobile First에서는 주로 `min-width`를 사용한다.
- Desktop First에서는 주로 `max-width`를 사용한다.
- breakpoint는 디자인이 깨지는 지점 기준으로 정한다.
- device 이름 기준보다 layout 기준으로 잡는 것이 좋다.
- media query도 cascade와 source order 영향을 받는다.
- media query 내부 selector도 specificity 규칙을 따른다.

---

### [실무]

기본 형태:

```css
@media (min-width: 768px) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
  }
}
```

여러 조건:

```css
@media (min-width: 768px) and (max-width: 1023px) {
  .tablet-only {
    display: block;
  }
}
```

검수 기준:

- media query 조건이 현재 viewport에서 true인가?
- `min-width`와 `max-width` 방향을 혼동하지 않았는가?
- breakpoint가 디자인 깨짐 기준인가?
- 같은 selector가 뒤 media query에서 override되는가?
- media query 순서가 의도와 맞는가?

---

### [FAQ]

Q. Media Query가 뭐야?
A. 화면 크기나 사용자 환경 조건에 따라 CSS를 조건부로 적용하는 문법이다.

Q. min-width는 언제 적용돼?
A. viewport width가 지정한 값 이상일 때 적용된다.

Q. max-width는 언제 적용돼?
A. viewport width가 지정한 값 이하일 때 적용된다.

Q. Breakpoint는 어떻게 정해?
A. 특정 기기 이름보다 layout이 깨지는 지점을 기준으로 정하는 것이 좋다.

---

## 4.2 Breakpoint

### [개념]

Breakpoint는 Layout이나 Component가 특정 화면 폭에서 변경되는 기준점이다.

Breakpoint는 디자인 요구사항과 콘텐츠가 깨지는 지점을 기준으로 정한다.

---

### [핵심]

Breakpoint 핵심:

- 화면 폭 기준 전환점이다.
- device 이름보다 layout 기준으로 정한다.
- 너무 많은 breakpoint는 유지보수를 어렵게 만든다.
- component별 breakpoint가 필요할 수 있다.
- breakpoint 사이 구간도 검수해야 한다.
- Mobile First에서는 작은 화면 기본값 + 큰 화면 breakpoint 구조가 일반적이다.

---

### [실무]

예시 breakpoint:

```css
@media (min-width: 640px) {
}

@media (min-width: 768px) {
}

@media (min-width: 1024px) {
}

@media (min-width: 1280px) {
}
```

Breakpoint Token 예:

```css
/* CSS custom media는 빌드 도구 지원이 필요할 수 있다. */
@media (min-width: 768px) {
  .layout {
    grid-template-columns: 1fr 2fr;
  }
}
```

검수 기준:

- breakpoint가 너무 많지 않은가?
- breakpoint 직전과 직후에서 layout이 자연스러운가?
- 콘텐츠 길이가 늘어나도 breakpoint가 유효한가?
- component별로 다른 breakpoint가 필요한가?
- breakpoint가 디자인 시스템과 일관되는가?

---

### [FAQ]

Q. Breakpoint가 뭐야?
A. 화면 폭에 따라 layout이나 style이 변경되는 기준점이다.

Q. Breakpoint는 기기별로 정하면 돼?
A. 특정 기기보다 layout이 깨지는 지점을 기준으로 정하는 것이 좋다.

Q. Breakpoint가 많으면 좋아?
A. 아니다. 너무 많으면 유지보수와 검수가 어려워진다.

Q. Breakpoint 사이도 확인해야 해?
A. 해야 한다. 경계값 직전과 직후에서 layout이 깨질 수 있다.

---

# 5. Responsive Layout

## 5.1 Responsive Container

### [개념]

Responsive Container는 콘텐츠의 최대 폭을 제한하면서 작은 화면에서는 viewport에 맞게 줄어드는 layout wrapper다.

Container는 너무 넓은 본문과 너무 좁은 모바일 여백 문제를 해결한다.

---

### [핵심]

Responsive Container 핵심:

- 작은 화면에서는 viewport에 맞게 줄어든다.
- 큰 화면에서는 max-width로 폭을 제한한다.
- 좌우 padding 또는 `width: min()`으로 안전 여백을 만든다.
- `margin-inline: auto`로 가운데 정렬한다.
- `100vw` 대신 `100%` 기반 계산이 안전한 경우가 많다.
- container는 page layout의 기본 단위다.

---

### [실무]

Container 예:

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}
```

Section 예:

```css
.section {
  padding-block: clamp(3rem, 8vw, 6rem);
}

.section-content {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}
```

검수 기준:

- 작은 화면에서 좌우 여백이 충분한가?
- 큰 화면에서 본문 폭이 너무 넓지 않은가?
- container가 horizontal overflow를 만들지 않는가?
- `100vw` 사용으로 scrollbar overflow가 생기지 않는가?
- section spacing이 viewport에 따라 자연스러운가?

---

### [FAQ]

Q. Responsive Container가 뭐야?
A. 작은 화면에서는 줄어들고 큰 화면에서는 max-width로 폭을 제한하는 layout wrapper다.

Q. container를 가운데 정렬하려면?
A. `margin-inline: auto`를 사용할 수 있다.

Q. width min(100% - 32px, 1120px)는 뭐야?
A. viewport보다 32px 작게 유지하되 최대 1120px까지만 넓어지게 하는 방식이다.

---

## 5.2 Responsive Flexbox

### [개념]

Responsive Flexbox는 Flexbox를 사용해 item을 가로 또는 세로로 배치하고, 화면 크기에 따라 줄바꿈이나 방향 전환을 적용하는 방식이다.

---

### [핵심]

Responsive Flexbox 핵심:

- `flex-wrap: wrap`으로 overflow를 줄인다.
- 작은 화면에서는 column, 큰 화면에서는 row로 전환할 수 있다.
- `gap`으로 item 간격을 관리한다.
- flex item에 `min-width: 0`이 필요할 수 있다.
- button group, nav, toolbar, tag list에 유용하다.
- 모바일에서 row 유지가 overflow를 만들 수 있다.

---

### [실무]

Button Group 예:

```css
.button-group {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

@media (max-width: 480px) {
  .button-group {
    flex-direction: column;
  }

  .button-group .button {
    width: 100%;
  }
}
```

Toolbar 예:

```css
.toolbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-3);
}

.toolbar-search {
  flex: 1 1 240px;
  min-width: 0;
}
```

검수 기준:

- item이 한 줄에 모두 들어가지 않을 수 있는가?
- flex-wrap이 필요한가?
- 작은 화면에서 column 전환이 필요한가?
- flex item에 min-width 0이 필요한가?
- gap으로 간격을 관리하는가?

---

### [FAQ]

Q. Responsive Flexbox는 언제 써?
A. button group, toolbar, nav, tag list처럼 item이 한 방향으로 배치되고 줄바꿈이 필요한 경우에 쓴다.

Q. flex-wrap은 왜 필요해?
A. item이 viewport를 넘을 때 다음 줄로 내려 overflow를 줄이기 위해 필요하다.

Q. flex item이 줄어들지 않으면?
A. `min-width: 0`을 검토한다.

Q. 모바일에서 button group이 깨지면?
A. flex-wrap 또는 column 전환과 button width 100%를 고려한다.

---

## 5.3 Responsive Grid

### [개념]

Responsive Grid는 CSS Grid를 사용해 여러 column layout을 만들고, viewport에 따라 column 수와 item 크기를 조정하는 방식이다.

Card Grid, Gallery, Dashboard Layout, Product List에 자주 사용한다.

---

### [핵심]

Responsive Grid 핵심:

- 2차원 layout에 적합하다.
- `repeat()`, `minmax()`, `auto-fit`을 활용한다.
- 작은 화면에서는 1 column으로 시작하는 것이 안전하다.
- 큰 화면에서 column 수를 늘린다.
- `gap`으로 row/column 간격을 관리한다.
- `minmax()` 최소값이 너무 크면 overflow가 생긴다.
- item span은 작은 화면에서 해제해야 할 수 있다.

---

### [실무]

Auto Fit Grid 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: var(--space-6);
}
```

Breakpoint Grid 예:

```css
.card-grid {
  display: grid;
  gap: var(--space-6);
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

검수 기준:

- 작은 화면에서 1 column이 되는가?
- minmax 최소값이 viewport를 넘지 않는가?
- gap과 column width 합이 overflow를 만들지 않는가?
- span item이 mobile에서 깨지지 않는가?
- grid item 내부 긴 텍스트에 overflow 처리가 있는가?

---

### [FAQ]

Q. Responsive Grid는 언제 써?
A. card grid, gallery, dashboard처럼 여러 행과 열을 가진 layout에 적합하다.

Q. auto-fit minmax는 왜 유용해?
A. 사용 가능한 공간에 맞춰 column 수를 자동 조정할 수 있기 때문이다.

Q. Grid가 모바일에서 넘치면 무엇을 확인해?
A. 고정 column, minmax 최소값, gap, 긴 텍스트, item span을 확인한다.

Q. 작은 화면에서는 Grid를 안 써도 돼?
A. 사용할 수 있지만 기본 1 column으로 두는 것이 안전하다.

---

# 6. Responsive Images

## 6.1 Basic Responsive Image

### [개념]

Responsive Image는 이미지가 부모 컨테이너의 폭을 넘지 않고 화면 크기에 맞게 줄어드는 이미지 처리 방식이다.

기본 CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

---

### [핵심]

Responsive Image 핵심:

- `max-width: 100%`로 부모보다 커지지 않게 한다.
- `height: auto`로 비율을 유지한다.
- `display: block`으로 inline image 하단 공백을 줄일 수 있다.
- card image에는 `aspect-ratio`와 `object-fit`을 사용할 수 있다.
- 의미 있는 이미지는 `alt`가 필요하다.
- 이미지 width/height attribute는 layout shift를 줄이는 데 도움된다.
- 초기 화면 아래 이미지는 lazy loading을 고려한다.

---

### [실무]

기본 예:

```css
img {
  display: block;
  max-width: 100%;
  height: auto;
}
```

Card Image 예:

```css
.card-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
```

HTML 예:

```html
<img
  src="/images/festival.jpg"
  alt="서울 빛 축제 야간 조명"
  width="640"
  height="360"
  loading="lazy"
/>
```

검수 기준:

- 이미지가 부모를 넘지 않는가?
- 이미지 비율이 깨지지 않는가?
- card image가 일정 비율로 표시되는가?
- 중요한 이미지에 lazy loading을 잘못 적용하지 않았는가?
- alt가 의미에 맞게 작성되었는가?

---

### [FAQ]

Q. Responsive Image는 뭐야?
A. 이미지가 부모 컨테이너 폭을 넘지 않고 화면 크기에 맞게 줄어드는 이미지 처리 방식이다.

Q. img에 max-width 100%를 주는 이유는?
A. 원본 이미지가 부모보다 클 때 horizontal overflow를 막기 위해서다.

Q. height auto는 왜 필요해?
A. 이미지 비율을 유지하기 위해 필요하다.

Q. card image 비율을 맞추려면?
A. `aspect-ratio`와 `object-fit: cover`를 사용할 수 있다.

---

## 6.2 Picture and Source

### [개념]

`picture`와 `source`는 화면 조건이나 이미지 포맷에 따라 다른 이미지 파일을 제공하는 HTML 요소다.

Art Direction, responsive image source, modern image format 제공에 사용할 수 있다.

---

### [핵심]

Picture 핵심:

- `picture`는 여러 `source` 후보를 감싼다.
- `source`는 media condition 또는 type 조건을 가진다.
- 마지막 fallback으로 `img`가 필요하다.
- 화면 크기에 따라 다른 crop 이미지를 제공할 수 있다.
- WebP/AVIF 같은 포맷 fallback에 사용할 수 있다.
- `img`의 alt가 최종 접근성 텍스트 역할을 한다.

---

### [실무]

Art Direction 예:

```html
<picture>
  <source media="(min-width: 768px)" srcset="/images/festival-wide.jpg" />
  <img
    src="/images/festival-mobile.jpg"
    alt="축제 무대와 관람객"
    width="640"
    height="360"
  />
</picture>
```

Format Fallback 예:

```html
<picture>
  <source srcset="/images/festival.avif" type="image/avif" />
  <source srcset="/images/festival.webp" type="image/webp" />
  <img src="/images/festival.jpg" alt="축제 현장" />
</picture>
```

검수 기준:

- fallback img가 있는가?
- alt가 img에 작성되어 있는가?
- media condition이 의도와 맞는가?
- 모바일과 데스크톱 crop이 중요한 내용을 잘 보존하는가?
- 이미지 파일 크기가 과도하지 않은가?

---

### [FAQ]

Q. picture 요소는 언제 써?
A. 화면 크기나 이미지 포맷에 따라 다른 이미지를 제공해야 할 때 사용한다.

Q. picture 안에 img가 꼭 필요해?
A. 필요하다. img는 fallback이자 접근성 alt를 제공하는 핵심 요소다.

Q. source에 alt를 써?
A. 아니다. alt는 fallback img에 작성한다.

Q. Art Direction이 뭐야?
A. 화면 크기에 따라 다른 비율이나 crop의 이미지를 제공하는 방식이다.

---

# 7. Responsive Typography

## 7.1 Responsive Typography Concept

### [개념]

Responsive Typography는 화면 크기에 따라 글자 크기, 줄 높이, 행 길이, heading scale을 조정해 가독성을 유지하는 방식이다.

---

### [핵심]

Responsive Typography 핵심:

- 본문은 작은 화면에서도 읽기 쉬워야 한다.
- 제목은 큰 화면에서 너무 커지지 않도록 제한한다.
- `rem` 기반 font scale이 유지보수에 유리하다.
- `clamp()`로 fluid typography를 만들 수 있다.
- 본문 line length는 너무 길지 않아야 한다.
- line-height는 font-size와 함께 조정한다.
- 모바일에서 text가 너무 작으면 접근성 문제가 된다.

---

### [실무]

Fluid Heading 예:

```css
.page-title {
  font-size: clamp(2rem, 6vw, 4rem);
  line-height: 1.1;
}
```

Readable Text 예:

```css
.prose {
  max-width: 65ch;
}

.prose p {
  font-size: 1rem;
  line-height: 1.7;
}
```

검수 기준:

- 본문 font-size가 모바일에서 읽기 쉬운가?
- heading이 작은 화면에서 너무 크지 않은가?
- heading이 큰 화면에서 과도하게 커지지 않는가?
- 본문 행 길이가 너무 길지 않은가?
- line-height가 font-size와 어울리는가?

---

### [FAQ]

Q. Responsive Typography가 뭐야?
A. 화면 크기에 따라 글자 크기와 줄 높이, 행 길이를 조정해 가독성을 유지하는 방식이다.

Q. clamp()는 typography에 왜 써?
A. 최소값과 최대값 사이에서 viewport에 따라 자연스럽게 글자 크기를 조정할 수 있기 때문이다.

Q. 본문 max-width에 ch를 쓰는 이유는?
A. 글자 수 기준으로 행 길이를 제한해 긴 본문 가독성을 높이기 위해서다.

Q. 모바일에서 글자가 작으면 뭐가 문제야?
A. 읽기 어렵고 접근성 문제가 생길 수 있다.

---

# 8. Touch Target and Mobile UX

## 8.1 Touch Target

### [개념]

Touch Target은 사용자가 손가락으로 누를 수 있는 interactive element의 실제 터치 가능한 영역이다.

모바일 UI에서는 버튼, 링크, checkbox, radio, menu item이 충분한 크기와 간격을 가져야 한다.

---

### [핵심]

Touch Target 핵심:

- 작은 버튼은 누르기 어렵다.
- interactive element에는 충분한 height와 padding이 필요하다.
- 인접한 button/link 사이 간격이 필요하다.
- icon-only button도 충분한 hit area를 가져야 한다.
- 시각적 icon이 작아도 button 자체는 크게 만들 수 있다.
- fixed bottom UI는 엄지 조작을 고려한다.
- hover interaction에 의존하면 touch 환경에서 문제가 생길 수 있다.

---

### [실무]

Button 예:

```css
.button {
  min-height: 44px;
  padding-inline: var(--space-4);
}
```

Icon Button 예:

```css
.icon-button {
  display: inline-grid;
  place-items: center;
  width: 44px;
  height: 44px;
}
```

Menu Item 예:

```css
.menu-item {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding-inline: var(--space-4);
}
```

검수 기준:

- button/link가 손가락으로 누르기 충분한가?
- icon-only button의 시각 icon과 hit area를 구분했는가?
- 인접한 interactive element 사이에 충분한 간격이 있는가?
- hover 없이도 조작 가능성이 명확한가?
- fixed bottom UI가 콘텐츠를 가리지 않는가?

---

### [FAQ]

Q. Touch Target이 뭐야?
A. 사용자가 손가락으로 누를 수 있는 interactive element의 실제 터치 영역이다.

Q. 모바일 버튼은 왜 크게 만들어야 해?
A. 손가락으로 정확히 누르기 어렵기 때문에 충분한 높이와 여백이 필요하다.

Q. 아이콘은 작아도 버튼 영역은 크게 할 수 있어?
A. 가능하다. icon visual size와 button hit area는 분리해서 설계할 수 있다.

Q. hover 효과에 의존하면 왜 문제야?
A. touch 환경에는 hover가 없거나 불안정하기 때문이다.

---

# 9. Responsive Table

## 9.1 Responsive Table Concept

### [개념]

Responsive Table은 column이 많은 table이 작은 화면에서 layout을 깨뜨리지 않도록 처리하는 방식이다.

Table은 구조적으로 넓어지기 쉬우므로 모바일에서 horizontal scroll wrapper가 필요할 수 있다.

---

### [핵심]

Responsive Table 핵심:

- table은 작은 화면에서 overflow가 생기기 쉽다.
- table을 무리하게 줄이면 가독성이 떨어진다.
- wrapper에 `overflow-x: auto`를 적용할 수 있다.
- table의 semantic 구조는 유지한다.
- 중요한 column 우선순위를 검토한다.
- 카드 형태로 변환하는 방식도 가능하지만 의미와 접근성을 신중히 봐야 한다.

---

### [실무]

Table Wrapper 예:

```html
<div class="table-scroll" tabindex="0" aria-label="Festival schedule table">
  <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Festival</th>
        <th>Location</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2026-07-01</td>
        <td>Seoul Light Festival</td>
        <td>Seoul</td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.table-scroll {
  overflow-x: auto;
}

.table-scroll table {
  min-width: 640px;
  border-collapse: collapse;
}
```

검수 기준:

- table이 모바일에서 body overflow를 만들지 않는가?
- horizontal scroll wrapper가 있는가?
- table semantic이 유지되는가?
- scroll 가능한 영역이 keyboard로 접근 가능한가?
- column이 너무 많으면 정보 구조를 재검토했는가?

---

### [FAQ]

Q. Responsive Table은 왜 어려워?
A. table은 column 구조가 넓어지기 쉬워 작은 화면에서 overflow를 만들기 때문이다.

Q. 모바일 table은 어떻게 처리해?
A. wrapper에 `overflow-x: auto`를 주어 table 자체 의미를 유지하면서 가로 스크롤을 제공할 수 있다.

Q. table을 div 카드로 바꿔도 돼?
A. 가능하지만 table semantic과 데이터 관계가 사라질 수 있으므로 신중히 판단해야 한다.

Q. table min-width는 왜 써?
A. column 내용이 너무 좁아져 읽기 어려워지는 것을 막기 위해 사용할 수 있다.

---

# 10. Responsive Modal and Fixed UI

## 10.1 Responsive Modal

### [개념]

Responsive Modal은 작은 화면에서도 Dialog가 viewport 밖으로 나가지 않고 내용이 접근 가능하도록 만드는 Modal Layout 방식이다.

Modal은 width, max-height, overflow, padding, focus, scroll lock을 함께 고려해야 한다.

---

### [핵심]

Responsive Modal 핵심:

- modal backdrop은 viewport 전체를 덮는다.
- dialog width는 viewport보다 커지면 안 된다.
- `width: min(100%, max-width)` 패턴이 유용하다.
- `max-height`와 `overflow: auto`가 필요할 수 있다.
- mobile viewport에서는 padding을 줄일 수 있다.
- fixed header/footer가 dialog 내부 content를 가리지 않아야 한다.
- focus trap과 Escape handling은 JavaScript와 함께 필요하다.

---

### [실무]

Modal 예:

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: var(--space-4);
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-dialog {
  width: min(100%, 480px);
  max-height: calc(100dvh - 32px);
  overflow: auto;
  background-color: var(--color-background);
  border-radius: var(--radius-lg);
}
```

Mobile Bottom Sheet 예:

```css
@media (max-width: 480px) {
  .modal-backdrop {
    align-items: end;
    padding: 0;
  }

  .modal-dialog {
    width: 100%;
    max-height: 90dvh;
    border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  }
}
```

검수 기준:

- dialog가 viewport보다 넓지 않은가?
- 내용이 길 때 scroll 가능한가?
- small viewport에서 dialog가 잘리지 않는가?
- focus가 modal 밖으로 나가지 않는가?
- fixed position과 z-index layer가 적절한가?

---

### [FAQ]

Q. Responsive Modal은 뭐야?
A. 작은 화면에서도 dialog가 viewport 밖으로 나가지 않고 내용 접근이 가능한 modal layout이다.

Q. Modal이 모바일에서 잘리면 어떻게 해?
A. width, max-height, overflow auto, 100dvh 기반 계산을 적용한다.

Q. Modal은 CSS만으로 충분해?
A. 아니다. focus trap, scroll lock, Escape handling은 JavaScript와 함께 필요하다.

Q. 모바일에서는 bottom sheet 형태가 가능해?
A. 가능하다. 작은 화면에서 dialog를 하단 sheet처럼 배치할 수 있다.

---

## 10.2 Fixed Bottom UI

### [개념]

Fixed Bottom UI는 화면 하단에 고정되는 버튼, navigation, action bar 같은 UI다.

모바일에서 자주 사용되지만 콘텐츠를 가리거나 safe area를 침범하지 않도록 주의해야 한다.

---

### [핵심]

Fixed Bottom UI 핵심:

- `position: fixed`와 bottom offset을 사용한다.
- 콘텐츠 하단이 fixed UI에 가려질 수 있다.
- body 또는 main에 하단 padding을 추가할 수 있다.
- 모바일 safe area를 고려해야 한다.
- z-index layer가 필요하다.
- keyboard가 올라오는 환경에서 겹침을 검토해야 한다.
- 너무 많은 fixed UI는 화면을 좁게 만든다.

---

### [실무]

Fixed Action Bar 예:

```css
.mobile-action-bar {
  position: fixed;
  inset-inline: 0;
  bottom: 0;
  z-index: var(--z-fixed);
  padding: var(--space-4);
  padding-bottom: calc(var(--space-4) + env(safe-area-inset-bottom));
  background-color: var(--color-background);
  border-top: 1px solid var(--color-border);
}

.page-content {
  padding-bottom: calc(80px + env(safe-area-inset-bottom));
}
```

검수 기준:

- fixed UI가 콘텐츠를 가리지 않는가?
- safe area inset을 고려했는가?
- keyboard와 겹치는 입력 화면이 있는가?
- z-index가 modal/dropdown과 충돌하지 않는가?
- desktop에서도 fixed bottom이 필요한가?

---

### [FAQ]

Q. Fixed Bottom UI는 뭐야?
A. 화면 하단에 고정되는 버튼, navigation, action bar 같은 UI다.

Q. fixed bottom이 콘텐츠를 가리면 어떻게 해?
A. main content에 하단 padding을 추가하거나 layout 구조를 조정한다.

Q. safe-area-inset-bottom은 왜 써?
A. 모바일 기기의 홈 인디케이터나 노치 영역과 겹치지 않도록 여백을 확보하기 위해 사용한다.

Q. fixed UI는 z-index만 높이면 돼?
A. 아니다. modal, dropdown, header 등 전체 layer scale과 함께 관리해야 한다.

---

# 11. Feature Media Queries

## 11.1 Hover and Pointer Media Queries

### [개념]

Hover and Pointer Media Query는 사용자의 입력 장치가 hover를 지원하는지, pointer가 정밀한지 등을 조건으로 CSS를 적용하는 media feature다.

Responsive Design에서는 touch 환경과 mouse 환경을 구분해 hover 의존 문제를 줄일 때 사용한다.

---

### [핵심]

Hover / Pointer 핵심:

- `(hover: hover)`는 hover가 가능한 환경을 의미한다.
- `(hover: none)`은 hover가 없거나 제한적인 환경을 의미한다.
- `(pointer: fine)`은 mouse처럼 정밀한 pointer를 의미한다.
- `(pointer: coarse)`는 finger touch처럼 덜 정밀한 pointer를 의미한다.
- card hover, tooltip, dropdown hover style은 touch 환경을 고려해야 한다.
- hover는 보조 feedback으로 사용하고 핵심 기능 접근 수단으로 의존하지 않는다.
- interaction 상세 기준은 Part12와 Part14에서 함께 다룬다.

---

### [실무]

Hover 가능한 환경에만 hover motion 적용:

```css
@media (hover: hover) and (pointer: fine) {
  .card:hover {
    transform: translateY(-2px);
  }
}
```

Touch 환경 button spacing:

```css
@media (pointer: coarse) {
  .icon-button {
    width: 48px;
    height: 48px;
  }
}
```

검수 기준:

- hover가 핵심 기능 접근 수단이 아닌가?
- touch 환경에서 hover style이 불안정하지 않은가?
- pointer coarse 환경에서 touch target이 충분한가?
- mouse 환경 hover와 keyboard focus가 모두 제공되는가?
- 관련 interaction state는 Part12/Part14 기준과 일치하는가?

---

### [FAQ]

Q. hover media query는 뭐야?
A. 사용자의 입력 환경이 hover를 지원하는지 조건으로 CSS를 적용하는 media query다.

Q. hover 효과는 모바일에서도 똑같이 적용돼?
A. touch 환경에서는 hover가 없거나 불안정할 수 있으므로 주의해야 한다.

Q. pointer coarse는 뭐야?
A. 손가락 터치처럼 정밀도가 낮은 입력 장치를 의미한다.

Q. hover/pointer 상세 기준은 어디서 봐?
A. media feature 기본은 Part10, interaction state 상세 기준은 Part12와 Component 적용 예시는 Part14를 참조한다.

---

## 11.2 prefers-reduced-motion

### [개념]

`prefers-reduced-motion`은 사용자가 시스템에서 움직임 감소를 선호하는지 감지하는 media feature다.

Responsive 관점에서는 사용자 환경 조건에 맞춰 motion과 transition을 조정하는 feature media query로 다룬다.

---

### [핵심]

prefers-reduced-motion 핵심:

- 사용자의 motion reduction preference를 감지한다.
- 큰 이동, 회전, parallax, smooth scroll을 줄일 수 있다.
- transition duration을 줄이거나 animation을 제한할 수 있다.
- motion 없이도 상태 변화가 이해되어야 한다.
- 필수 feedback 자체를 제거하기보다 과도한 motion을 줄이는 것이 좋다.
- transition과 animation 상세 기준은 Part12에서 다룬다.

---

### [실무]

기본 예:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    scroll-behavior: auto;
    transition-duration: 0.01ms;
  }
}
```

Component Motion 예:

```css
.card {
  transition: transform 180ms ease;
}

@media (prefers-reduced-motion: reduce) {
  .card {
    transition: none;
  }
}
```

검수 기준:

- 큰 이동 motion이 있는가?
- 자동 반복 animation이 있는가?
- smooth scroll이 필요한가?
- reduced motion에서도 상태 변화가 이해되는가?
- motion 상세 구현은 Part12 기준과 일치하는가?

---

### [FAQ]

Q. prefers-reduced-motion은 뭐야?
A. 사용자가 움직임 감소를 선호하는지 감지하는 CSS media feature다.

Q. reduced motion은 반응형이야?
A. 화면 크기 반응형은 아니지만 사용자 환경 조건에 반응하는 media query다.

Q. reduced motion에서는 모든 효과를 없애야 해?
A. 반드시 전부 없앨 필요는 없지만 과도한 움직임은 줄여야 한다.

Q. motion 상세 기준은 어디서 봐?
A. transition, transform, opacity, reduced motion 상세 기준은 Part12를 참조한다.

---

# 12. Responsive Debugging

## 12.1 Horizontal Overflow Debug

### [개념]

Horizontal Overflow는 viewport보다 넓은 요소가 생겨 가로 스크롤이 발생하는 문제다.

Responsive CSS에서 가장 흔한 문제 중 하나다.

---

### [핵심]

Horizontal Overflow 원인:

- fixed width 요소
- `width: 100vw`
- image max-width 누락
- table overflow 처리 누락
- long text / long URL
- flex item min-width
- grid minmax 최소값 과다
- absolute/fixed element가 viewport 밖으로 나감
- negative margin
- padding과 width 계산 문제
- border-box 미적용

---

### [실무]

Debug Flow:

```text
Mobile Viewport 설정
→ body horizontal scroll 확인
→ DevTools로 넓은 요소 찾기
→ fixed width 확인
→ image/table 확인
→ flex/grid item min-width 확인
→ long text 확인
→ position element 확인
→ 원인 property 수정
```

해결 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

img {
  max-width: 100%;
  height: auto;
}

.long-text {
  overflow-wrap: break-word;
}

.flex-item {
  min-width: 0;
}
```

검수 기준:

- 320px 또는 360px viewport에서 horizontal scroll이 없는가?
- fixed width component가 없는가?
- table wrapper가 있는가?
- long text가 줄바꿈되는가?
- flex/grid item이 줄어들 수 있는가?

---

### [FAQ]

Q. Horizontal Overflow는 뭐야?
A. viewport보다 넓은 요소가 생겨 가로 스크롤이 발생하는 문제다.

Q. 모바일 가로 스크롤은 왜 생겨?
A. fixed width, image overflow, table overflow, 긴 텍스트, flex/grid min-width 문제 때문일 수 있다.

Q. body overflow-x hidden으로 해결해도 돼?
A. 원인을 숨기는 임시 처리일 수 있으므로 넓은 요소를 찾아 수정하는 것이 우선이다.

Q. flex item overflow는 어떻게 해결해?
A. 필요한 경우 flex item에 `min-width: 0`을 적용한다.

---

## 12.2 Media Query Debug

### [개념]

Media Query Debug는 특정 viewport에서 media query CSS가 적용되지 않거나 예상과 다르게 적용되는 문제를 확인하는 과정이다.

---

### [핵심]

Media Query 문제 원인:

- viewport meta 누락
- min-width / max-width 방향 혼동
- breakpoint 값 오타
- CSS import 순서 문제
- 같은 selector가 뒤에서 override됨
- specificity 문제
- media query 조건이 현재 viewport와 맞지 않음
- browser zoom 또는 device emulation 설정 문제
- cached CSS 문제

---

### [실무]

Debug Flow:

```text
Viewport Meta 확인
→ 현재 viewport width 확인
→ media query 조건 확인
→ DevTools Styles에서 media rule 확인
→ 취소선 rule 확인
→ source order 확인
→ specificity 확인
→ breakpoint 직전/직후 확인
```

문제 예:

```text
문제: 768px 이상에서 grid가 2 column이 되지 않음
원인: CSS 파일 import 누락 또는 selector 오타
해결: import와 selector 매칭 확인
```

```text
문제: 모바일 style이 desktop에 적용됨
원인: max-width와 min-width 조건 혼동
해결: Mobile First 기준으로 min-width 조건 재정리
```

검수 기준:

- 현재 viewport가 media query 조건을 만족하는가?
- DevTools에서 media query rule이 표시되는가?
- rule이 override되고 있지 않은가?
- breakpoint 직전과 직후를 모두 확인했는가?
- media query 순서가 mobile first 구조와 맞는가?

---

### [FAQ]

Q. Media Query가 안 먹을 때 뭘 확인해?
A. viewport meta, 현재 viewport width, min/max 조건, CSS import, selector, source order를 확인한다.

Q. min-width와 max-width를 자주 헷갈리면?
A. Mobile First는 기본 CSS를 mobile로 두고 큰 화면에 min-width를 추가한다고 기억하면 된다.

Q. breakpoint 근처도 테스트해야 해?
A. 해야 한다. breakpoint 직전과 직후에서 layout이 깨질 수 있다.

---

# 13. Common Mistakes

## 13.1 Responsive Common Mistakes

### [개념]

Responsive 실수는 작은 화면에서 horizontal overflow, 읽기 어려운 텍스트, 깨진 layout, 접근 불가능한 button, 잘린 modal, 사용 불가능한 table로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- viewport meta 누락
- desktop 기준 fixed width 남용
- `width: 100vw` 남용
- body overflow-x hidden으로 원인 숨김
- image max-width 누락
- table overflow-x 누락
- media query min/max 방향 혼동
- breakpoint를 device 이름 기준으로만 결정
- flex-wrap 누락
- grid minmax 최소값 과다
- mobile에서 button group row 유지
- touch target 부족
- hover에 핵심 기능 의존
- modal max-height/overflow 누락
- fixed bottom UI가 content를 가림
- long text overflow-wrap 누락
- heading이 모바일에서 과도하게 큼
- desktop에서 본문 line length가 너무 김
- reduced motion 미고려

---

### [실무]

Troubleshooting Flow:

```text
Responsive Bug
→ viewport meta 확인
→ mobile width 재현
→ horizontal overflow 확인
→ fixed width 확인
→ image/table 확인
→ flex/grid 확인
→ media query 조건 확인
→ typography/touch target 확인
→ component별 responsive 확인
```

문제 예:

```text
문제: 모바일에서 body 가로 스크롤 발생
원인: card width 420px 고정
해결: width 100%, max-width, responsive grid 적용
```

```text
문제: button 두 개가 모바일에서 화면 밖으로 나감
원인: button group flex-wrap 누락
해결: flex-wrap 또는 column 전환 적용
```

```text
문제: modal 내용이 작은 화면에서 잘림
원인: max-height와 overflow auto 누락
해결: max-height calc(100dvh - spacing), overflow auto 적용
```

검수 기준:

- 가장 작은 viewport에서 핵심 기능이 동작하는가?
- horizontal overflow가 없는가?
- touch target이 충분한가?
- media query 조건이 의도와 맞는가?
- component가 page layout 변화에 대응하는가?

---

### [FAQ]

Q. Responsive에서 가장 흔한 실수는 뭐야?
A. fixed width, image/table overflow, flex/grid wrap 누락, media query 조건 오해가 흔하다.

Q. 모바일 가로 스크롤은 어떻게 해결해?
A. body overflow를 숨기기보다 viewport보다 넓은 원인 요소를 찾아 수정한다.

Q. Breakpoint를 많이 만들면 해결돼?
A. 아니다. fluid layout, flex/grid, responsive image를 먼저 적용하고 필요한 지점만 breakpoint로 처리한다.

Q. Touch target은 왜 중요해?
A. 모바일 사용자가 손가락으로 정확히 조작할 수 있어야 하기 때문이다.

---

# 14. Comparison Rules

## 14.1 Mobile First vs Desktop First

### [개념]

Mobile First는 작은 화면을 기본으로 작성하고 큰 화면으로 확장하는 방식이다.

Desktop First는 큰 화면을 기본으로 작성하고 작은 화면으로 축소하는 방식이다.

---

### [핵심]

| 비교        | Mobile First           | Desktop First          |
| ----------- | ---------------------- | ---------------------- |
| 기본 CSS    | 모바일                 | 데스크톱               |
| Media Query | 주로 min-width         | 주로 max-width         |
| 확장 방향   | 작은 화면 → 큰 화면    | 큰 화면 → 작은 화면    |
| 장점        | 모바일 UX 우선         | desktop 시안 반영 쉬움 |
| 주의        | desktop 확장 설계 필요 | mobile override 증가   |
| 추천        | 일반적인 현대 웹       | desktop 중심 특수 UI   |

---

### [실무]

선택 기준:

```text
일반 서비스 UI → Mobile First
관리자 대시보드 중심 → Desktop First 가능
콘텐츠 중심 사이트 → Mobile First 권장
학습/실무 기본값 → Mobile First 권장
```

---

### [FAQ]

Q. Mobile First와 Desktop First 차이는 뭐야?
A. Mobile First는 모바일 기본에서 큰 화면으로 확장하고 Desktop First는 데스크톱 기본에서 작은 화면으로 줄이는 방식이다.

Q. Mobile First에서는 어떤 media query를 써?
A. 주로 `min-width` media query를 사용한다.

Q. Desktop First는 안 좋은 방식이야?
A. 아니다. 다만 모바일 대응 override가 많아질 수 있어 일반 서비스 UI에서는 Mobile First가 더 관리하기 쉽다.

---

## 14.2 min-width vs max-width Media Query

### [개념]

`min-width`와 `max-width`는 media query에서 viewport width 조건을 지정하는 대표 방식이다.

---

### [핵심]

| 비교      | min-width                   | max-width                   |
| --------- | --------------------------- | --------------------------- |
| 조건      | 지정 폭 이상                | 지정 폭 이하                |
| 사용 방식 | Mobile First                | Desktop First               |
| 예시      | `@media (min-width: 768px)` | `@media (max-width: 767px)` |
| 의미      | 화면이 커질 때 적용         | 화면이 작을 때 적용         |
| 주의      | 작은 화면 기본 필요         | 큰 화면 기본 필요           |

---

### [실무]

Mobile First 예:

```css
.card-grid {
  display: grid;
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

Desktop First 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

@media (max-width: 767px) {
  .card-grid {
    grid-template-columns: 1fr;
  }
}
```

---

### [FAQ]

Q. min-width와 max-width 차이는 뭐야?
A. min-width는 지정 폭 이상에서 적용되고 max-width는 지정 폭 이하에서 적용된다.

Q. Mobile First에서는 무엇을 써?
A. 일반적으로 min-width를 사용한다.

Q. max-width는 언제 써?
A. 큰 화면 기본 style에서 작은 화면만 별도 override할 때 사용할 수 있다.

---

## 14.3 Fixed Width vs Fluid Width

### [개념]

Fixed Width는 요소 폭을 고정 값으로 지정하는 방식이고 Fluid Width는 부모나 viewport에 맞게 유동적으로 변하는 방식이다.

---

### [핵심]

| 비교 | Fixed Width        | Fluid Width            |
| ---- | ------------------ | ---------------------- |
| 예시 | `width: 400px`     | `width: 100%`          |
| 장점 | 예측 쉬움          | 반응형에 유리          |
| 단점 | 작은 화면 overflow | 제한 없으면 너무 넓음  |
| 보완 | max-width 필요     | max-width 필요         |
| 사용 | icon, 작은 요소    | container, card, image |

---

### [실무]

권장:

```css
.card {
  width: 100%;
  max-width: 420px;
}
```

Container:

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}
```

---

### [FAQ]

Q. Fixed Width와 Fluid Width 차이는 뭐야?
A. Fixed Width는 고정 폭이고 Fluid Width는 부모나 viewport에 맞춰 유동적으로 변하는 폭이다.

Q. fixed width는 쓰면 안 돼?
A. 작은 요소에는 사용할 수 있지만 layout container나 card에는 overflow 위험이 있어 주의해야 한다.

Q. fluid width만 쓰면 충분해?
A. 아니다. 큰 화면에서 너무 넓어지지 않도록 max-width가 필요하다.

---

## 14.4 Responsive Image vs Picture

### [개념]

Responsive Image CSS는 이미지가 container 안에서 줄어들게 하는 방식이고 `picture`는 조건에 따라 다른 이미지 source를 제공하는 HTML 구조다.

---

### [핵심]

| 비교 | Responsive Image CSS   | Picture Element                |
| ---- | ---------------------- | ------------------------------ |
| 목적 | 이미지 크기 유동화     | 이미지 source 조건 분기        |
| 핵심 | max-width, height auto | source, media, type            |
| 사용 | 대부분 이미지 기본     | art direction, format fallback |
| alt  | img에 작성             | fallback img에 작성            |
| 주의 | source 자체는 동일     | fallback img 필수              |

---

### [실무]

선택 기준:

```text
같은 이미지가 줄어들기만 하면 됨 → img + max-width
화면별 crop이 달라야 함 → picture
AVIF/WebP fallback 필요 → picture
Card image 비율 유지 → aspect-ratio + object-fit
```

---

### [FAQ]

Q. Responsive Image와 picture 차이는 뭐야?
A. Responsive Image CSS는 같은 이미지를 유동 크기로 만들고 picture는 조건별로 다른 이미지 source를 제공한다.

Q. picture는 언제 필요해?
A. 화면별 crop 변경이나 이미지 포맷 fallback이 필요할 때 사용한다.

Q. picture에서도 alt는 어디에 써?
A. fallback img 요소에 작성한다.

---

# 15. Best Practice

## 15.1 Responsive Media Query Best Practice

### [개념]

Responsive Media Query Best Practice는 다양한 viewport와 입력 환경에서 layout, text, image, component가 깨지지 않도록 설계하고 검수하는 기준이다.

---

### [핵심]

권장 기준:

- viewport meta를 반드시 작성한다.
- Mobile First 방식으로 기본 CSS를 작성한다.
- fixed width보다 fluid width를 우선한다.
- container는 `width`, `max-width`, `margin-inline: auto`로 관리한다.
- image는 `max-width: 100%`, `height: auto`를 기본 적용한다.
- card image에는 `aspect-ratio`, `object-fit`을 고려한다.
- Flexbox에는 `flex-wrap`과 `gap`을 고려한다.
- Grid에는 `auto-fit`, `minmax()`, `min(100%, value)`를 고려한다.
- media query는 layout이 깨지는 지점에만 추가한다.
- typography는 `clamp()`와 `max-width: ch`를 고려한다.
- table은 `overflow-x: auto` wrapper를 고려한다.
- modal은 `max-height`, `overflow: auto`, `100dvh`를 고려한다.
- touch target과 hover 의존 문제를 확인한다.
- horizontal overflow를 반드시 검수한다.
- breakpoint 직전과 직후를 확인한다.

---

### [실무]

Responsive Base 예:

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: var(--space-6);
}

.page-title {
  font-size: clamp(2rem, 6vw, 4rem);
}
```

Review Checklist:

```md
- [ ] viewport meta가 있는가?
- [ ] 기본 CSS가 mobile에서 정상 동작하는가?
- [ ] fixed width가 horizontal overflow를 만들지 않는가?
- [ ] container가 작은 화면에서 줄어드는가?
- [ ] image가 부모를 넘지 않는가?
- [ ] table overflow 처리가 필요한가?
- [ ] flex item이 wrap되는가?
- [ ] grid minmax 최소값이 안전한가?
- [ ] media query 조건이 의도와 맞는가?
- [ ] breakpoint 직전/직후를 확인했는가?
- [ ] typography가 모바일에서 읽기 쉬운가?
- [ ] touch target이 충분한가?
- [ ] modal/dialog가 viewport 안에 들어오는가?
- [ ] horizontal overflow가 없는가?
```

---

### [FAQ]

Q. Responsive Media Query Best Practice는 뭐야?
A. Mobile First, fluid width, responsive image, flex/grid, media query, touch target, overflow 검수를 함께 적용하는 기준이다.

Q. Responsive 검수에서 가장 먼저 볼 것은 뭐야?
A. viewport meta, mobile layout, horizontal overflow, fixed width, image/table overflow를 먼저 확인한다.

Q. Breakpoint는 많이 만들수록 좋아?
A. 아니다. fluid layout을 우선하고 필요한 지점에만 breakpoint를 추가하는 것이 좋다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 다양한 viewport에서 깨지지 않는 responsive layout과 media query를 생성하고 검수하게 만드는 것이다.

---

# 16. Linkage Reference

## 16.1 Related Documents

### [개념]

Linkage Reference는 이 문서와 다른 HTML/CSS Foundation 문서의 역할을 구분하기 위한 참조 기준이다.

Part10은 Responsive Layout, Viewport, Breakpoint, Media Query의 기본 기준 문서다.

---

### [핵심]

연계 기준:

- Responsive Layout, Breakpoint, Viewport, Media Query 기준은 Part10에서 다룬다.
- Flexbox의 상세 축, 정렬, item 크기 기준은 Part07을 참조한다.
- Grid의 상세 track, minmax, auto-fit, item placement 기준은 Part08을 참조한다.
- Position, Fixed, Sticky, ZIndex, Stacking Context 기준은 Part09를 참조한다.
- Typography, Color, Spacing의 상세 기준은 Part11을 참조한다.
- `hover`, `pointer`, `prefers-reduced-motion`처럼 interaction과 motion에 연결되는 media feature 상세 기준은 Part12를 참조한다.
- Component Responsive Styling 적용 예시는 Part14를 참조한다.
- Attribute, Accessibility, SEO 기준은 Part15를 참조한다.
- Responsive Troubleshooting과 Review Checklist는 Part16을 참조한다.

---

### [실무]

문제 상황별 참조:

```text
viewport meta / breakpoint 문제 → Part10
flex wrap / flex item overflow 문제 → Part07 + Part10
grid column overflow 문제 → Part08 + Part10
fixed/sticky/mobile layer 문제 → Part09 + Part10
responsive typography 문제 → Part10 + Part11
hover/touch/reduced motion 문제 → Part10 + Part12
button group/modal/card responsive 문제 → Part14
responsive accessibility 문제 → Part15 + Part16
전체 responsive troubleshooting → Part16
```

---

### [FAQ]

Q. Part10은 어떤 문서야?
A. Responsive Layout, Viewport, Breakpoint, Media Query의 기본 기준 문서다.

Q. hover와 reduced motion은 Part10에서 다 끝나?
A. Part10은 media feature 기본을 다루고 interaction/motion 상세 기준은 Part12를 참조한다.

Q. Responsive Component 예시는 어디서 봐?
A. responsive 원칙은 Part10, component 적용 예시는 Part14를 참조한다.

Q. Responsive 문제가 생기면 어디서 봐?
A. 원칙은 Part10, 최종 troubleshooting과 review checklist는 Part16을 참조한다.

---

# Retrieval Queries

### [FAQ]

Q. Responsive Web Design이 뭐야?
A. 하나의 웹 페이지가 다양한 화면 크기에서 깨지지 않고 읽기 쉽고 사용 가능하도록 만드는 설계 방식이다.

Q. 반응형은 media query만 쓰면 끝이야?
A. 아니다. fluid width, responsive image, flex/grid, typography, touch target, overflow 검수가 함께 필요하다.

Q. Responsive Design에서 가장 먼저 볼 것은?
A. viewport meta, fixed width, horizontal overflow, image overflow를 먼저 확인한다.

Q. Viewport가 뭐야?
A. 사용자가 웹 페이지를 볼 수 있는 브라우저 표시 영역이다.

Q. viewport meta는 왜 필요해?
A. 모바일 브라우저가 페이지 폭을 device width 기준으로 올바르게 렌더링하도록 하기 위해 필요하다.

Q. width=device-width는 뭐야?
A. viewport 폭을 기기 화면 폭에 맞추도록 지정하는 값이다.

Q. 100vw를 쓰면 왜 가로 스크롤이 생길 수 있어?
A. scrollbar 폭까지 포함해 계산될 수 있어 body보다 넓어질 수 있기 때문이다.

Q. Mobile First가 뭐야?
A. 모바일 화면을 기본 CSS로 작성하고 큰 화면에서 min-width media query로 확장하는 방식이다.

Q. Mobile First는 왜 좋아?
A. 작은 화면에서 기본 사용성을 확보하고 큰 화면 확장을 단계적으로 관리하기 쉽기 때문이다.

Q. Mobile First에서는 min-width를 써?
A. 일반적으로 큰 화면 조건을 추가할 때 `min-width` media query를 사용한다.

Q. Media Query가 뭐야?
A. 화면 크기나 사용자 환경 조건에 따라 CSS를 조건부로 적용하는 문법이다.

Q. min-width는 언제 적용돼?
A. viewport width가 지정한 값 이상일 때 적용된다.

Q. max-width는 언제 적용돼?
A. viewport width가 지정한 값 이하일 때 적용된다.

Q. Breakpoint는 어떻게 정해?
A. 특정 기기 이름보다 layout이 깨지는 지점을 기준으로 정하는 것이 좋다.

Q. Breakpoint가 뭐야?
A. 화면 폭에 따라 layout이나 style이 변경되는 기준점이다.

Q. Breakpoint가 많으면 좋아?
A. 아니다. 너무 많으면 유지보수와 검수가 어려워진다.

Q. Responsive Container가 뭐야?
A. 작은 화면에서는 줄어들고 큰 화면에서는 max-width로 폭을 제한하는 layout wrapper다.

Q. container를 가운데 정렬하려면?
A. `margin-inline: auto`를 사용할 수 있다.

Q. width min(100% - 32px, 1120px)는 뭐야?
A. viewport보다 32px 작게 유지하되 최대 1120px까지만 넓어지게 하는 방식이다.

Q. Responsive Flexbox는 언제 써?
A. button group, toolbar, nav, tag list처럼 item이 한 방향으로 배치되고 줄바꿈이 필요한 경우에 쓴다.

Q. flex-wrap은 왜 필요해?
A. item이 viewport를 넘을 때 다음 줄로 내려 overflow를 줄이기 위해 필요하다.

Q. flex item이 줄어들지 않으면?
A. `min-width: 0`을 검토한다.

Q. Responsive Grid는 언제 써?
A. card grid, gallery, dashboard처럼 여러 행과 열을 가진 layout에 적합하다.

Q. auto-fit minmax는 왜 유용해?
A. 사용 가능한 공간에 맞춰 column 수를 자동 조정할 수 있기 때문이다.

Q. Grid가 모바일에서 넘치면 무엇을 확인해?
A. 고정 column, minmax 최소값, gap, 긴 텍스트, item span을 확인한다.

Q. Responsive Image는 뭐야?
A. 이미지가 부모 컨테이너 폭을 넘지 않고 화면 크기에 맞게 줄어드는 이미지 처리 방식이다.

Q. img에 max-width 100%를 주는 이유는?
A. 원본 이미지가 부모보다 클 때 horizontal overflow를 막기 위해서다.

Q. height auto는 왜 필요해?
A. 이미지 비율을 유지하기 위해 필요하다.

Q. picture 요소는 언제 써?
A. 화면 크기나 이미지 포맷에 따라 다른 이미지를 제공해야 할 때 사용한다.

Q. picture 안에 img가 꼭 필요해?
A. 필요하다. img는 fallback이자 접근성 alt를 제공하는 핵심 요소다.

Q. Responsive Typography가 뭐야?
A. 화면 크기에 따라 글자 크기와 줄 높이, 행 길이를 조정해 가독성을 유지하는 방식이다.

Q. clamp()는 typography에 왜 써?
A. 최소값과 최대값 사이에서 viewport에 따라 자연스럽게 글자 크기를 조정할 수 있기 때문이다.

Q. Touch Target이 뭐야?
A. 사용자가 손가락으로 누를 수 있는 interactive element의 실제 터치 영역이다.

Q. 모바일 버튼은 왜 크게 만들어야 해?
A. 손가락으로 정확히 누르기 어렵기 때문에 충분한 높이와 여백이 필요하다.

Q. hover 효과에 의존하면 왜 문제야?
A. touch 환경에는 hover가 없거나 불안정하기 때문이다.

Q. Responsive Table은 왜 어려워?
A. table은 column 구조가 넓어지기 쉬워 작은 화면에서 overflow를 만들기 때문이다.

Q. 모바일 table은 어떻게 처리해?
A. wrapper에 `overflow-x: auto`를 주어 table 자체 의미를 유지하면서 가로 스크롤을 제공할 수 있다.

Q. Responsive Modal은 뭐야?
A. 작은 화면에서도 dialog가 viewport 밖으로 나가지 않고 내용 접근이 가능한 modal layout이다.

Q. Modal이 모바일에서 잘리면 어떻게 해?
A. width, max-height, overflow auto, 100dvh 기반 계산을 적용한다.

Q. Fixed Bottom UI는 뭐야?
A. 화면 하단에 고정되는 버튼, navigation, action bar 같은 UI다.

Q. fixed bottom이 콘텐츠를 가리면 어떻게 해?
A. main content에 하단 padding을 추가하거나 layout 구조를 조정한다.

Q. hover media query는 뭐야?
A. 사용자의 입력 환경이 hover를 지원하는지 조건으로 CSS를 적용하는 media query다.

Q. pointer coarse는 뭐야?
A. 손가락 터치처럼 정밀도가 낮은 입력 장치를 의미한다.

Q. prefers-reduced-motion은 뭐야?
A. 사용자가 움직임 감소를 선호하는지 감지하는 CSS media feature다.

Q. reduced motion은 반응형이야?
A. 화면 크기 반응형은 아니지만 사용자 환경 조건에 반응하는 media query다.

Q. motion 상세 기준은 어디서 봐?
A. transition, transform, opacity, reduced motion 상세 기준은 Part12를 참조한다.

Q. Horizontal Overflow는 뭐야?
A. viewport보다 넓은 요소가 생겨 가로 스크롤이 발생하는 문제다.

Q. 모바일 가로 스크롤은 왜 생겨?
A. fixed width, image overflow, table overflow, 긴 텍스트, flex/grid min-width 문제 때문일 수 있다.

Q. body overflow-x hidden으로 해결해도 돼?
A. 원인을 숨기는 임시 처리일 수 있으므로 넓은 요소를 찾아 수정하는 것이 우선이다.

Q. Media Query가 안 먹을 때 뭘 확인해?
A. viewport meta, 현재 viewport width, min/max 조건, CSS import, selector, source order를 확인한다.

Q. min-width와 max-width를 자주 헷갈리면?
A. Mobile First는 기본 CSS를 mobile로 두고 큰 화면에 min-width를 추가한다고 기억하면 된다.

Q. Responsive에서 가장 흔한 실수는 뭐야?
A. fixed width, image/table overflow, flex/grid wrap 누락, media query 조건 오해가 흔하다.

Q. 모바일 가로 스크롤은 어떻게 해결해?
A. body overflow를 숨기기보다 viewport보다 넓은 원인 요소를 찾아 수정한다.

Q. Mobile First와 Desktop First 차이는 뭐야?
A. Mobile First는 모바일 기본에서 큰 화면으로 확장하고 Desktop First는 데스크톱 기본에서 작은 화면으로 줄이는 방식이다.

Q. min-width와 max-width 차이는 뭐야?
A. min-width는 지정 폭 이상에서 적용되고 max-width는 지정 폭 이하에서 적용된다.

Q. Fixed Width와 Fluid Width 차이는 뭐야?
A. Fixed Width는 고정 폭이고 Fluid Width는 부모나 viewport에 맞춰 유동적으로 변하는 폭이다.

Q. Responsive Image와 picture 차이는 뭐야?
A. Responsive Image CSS는 같은 이미지를 유동 크기로 만들고 picture는 조건별로 다른 이미지 source를 제공한다.

Q. Responsive Media Query Best Practice는 뭐야?
A. Mobile First, fluid width, responsive image, flex/grid, media query, touch target, overflow 검수를 함께 적용하는 기준이다.

Q. Responsive 검수에서 가장 먼저 볼 것은 뭐야?
A. viewport meta, mobile layout, horizontal overflow, fixed width, image/table overflow를 먼저 확인한다.

Q. Part10은 어떤 문서야?
A. Responsive Layout, Viewport, Breakpoint, Media Query의 기본 기준 문서다.

Q. hover와 reduced motion은 Part10에서 다 끝나?
A. Part10은 media feature 기본을 다루고 interaction/motion 상세 기준은 Part12를 참조한다.

Q. Responsive Component 예시는 어디서 봐?
A. responsive 원칙은 Part10, component 적용 예시는 Part14를 참조한다.

Q. Responsive 문제가 생기면 어디서 봐?
A. 원칙은 Part10, 최종 troubleshooting과 review checklist는 Part16을 참조한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 다양한 viewport에서 깨지지 않는 responsive layout과 media query를 생성하고 검수하게 만드는 것이다.
