# HTML CSS Foundation Part06 - Box Model Display

---

# 1. CSS Box Model

## 1.1 Box Model Concept

### [개념]

CSS Box Model은 HTML 요소가 화면에서 차지하는 공간을 계산하는 방식이다.

모든 HTML 요소는 사각형 Box로 렌더링된다.

Box Model 구성:

```text
Content
→ Padding
→ Border
→ Margin
```

Box Model은 Layout, Spacing, Responsive Design, Component Styling의 기본이다.

---

### [핵심]

Box Model 핵심:

- `content`는 실제 콘텐츠 영역이다.
- `padding`은 콘텐츠와 border 사이의 내부 여백이다.
- `border`는 padding 바깥의 테두리다.
- `margin`은 border 바깥의 외부 여백이다.
- `width`와 `height`는 요소 크기를 지정한다.
- `box-sizing`은 width / height 계산 방식을 결정한다.
- 기본값은 일반적으로 `content-box`다.
- 실무에서는 `border-box`를 많이 사용한다.
- Box Model 오해는 Layout 깨짐의 주요 원인이다.

---

### [실무]

2026 실무 기준에서 Box Model은 Component 크기, Card Layout, Form Field, Button, Responsive Container를 안정적으로 만드는 핵심 기준이다.

Frontend Agent는 아래 문제를 Box Model 관점에서 분석해야 한다.

- 요소가 예상보다 커짐
- 카드가 Container 밖으로 삐져나감
- 모바일에서 가로 스크롤 발생
- padding 때문에 width가 초과됨
- margin 때문에 정렬이 어긋남
- border 추가 후 Layout이 깨짐
- button / input 높이가 예상과 다름

기본 Reset:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

Box Model Debug Flow:

```text
Element Inspect
→ Content Size Check
→ Padding Check
→ Border Check
→ Margin Check
→ box-sizing Check
→ Overflow Check
```

---

### [FAQ]

Q. CSS Box Model이 뭐야?
A. HTML 요소의 공간을 content, padding, border, margin으로 계산하는 방식이다.

Q. Box Model은 왜 중요해?
A. 요소 크기, 간격, 정렬, 반응형 Layout 계산에 직접 영향을 주기 때문이다.

Q. 요소가 예상보다 커지는 이유는 뭐야?
A. width에 padding과 border가 추가되는 content-box 계산 방식 때문일 수 있다.

Q. Box Model 문제는 어떻게 확인해?
A. 브라우저 개발자 도구에서 Layout 또는 Computed 영역의 content, padding, border, margin을 확인한다.

---

# 2. Content Area

## 2.1 Content

### [개념]

Content Area는 요소 내부의 실제 콘텐츠가 표시되는 영역이다.

텍스트, 이미지, 입력 필드, 자식 요소 등이 Content Area에 배치된다.

---

### [핵심]

Content Area 핵심:

- 실제 콘텐츠가 들어가는 공간이다.
- `width`와 `height`는 기본적으로 content 영역 크기를 지정한다.
- `box-sizing: content-box`에서는 padding과 border가 width / height에 추가된다.
- `box-sizing: border-box`에서는 padding과 border가 width / height 안에 포함된다.
- 콘텐츠가 영역보다 크면 overflow가 발생할 수 있다.

예:

```css
.card {
  width: 300px;
  padding: 24px;
  border: 1px solid #e5e7eb;
}
```

---

### [실무]

Content Area는 고정 크기보다 유연한 크기로 설계하는 것이 좋다.

권장:

```css
.card {
  width: min(100%, 360px);
}
```

주의:

```css
.card {
  width: 360px;
}
```

실무 검수 기준:

- 콘텐츠가 Container를 넘치지 않는가?
- 고정 width가 모바일에서 문제를 만들지 않는가?
- 긴 텍스트가 overflow를 만들지 않는가?
- 이미지가 content area보다 커지지 않는가?
- `min-width: 0`이 필요한 Flex/Grid item은 아닌가?

---

### [FAQ]

Q. Content Area는 뭐야?
A. 요소 안에서 실제 텍스트, 이미지, 자식 요소가 표시되는 영역이다.

Q. width는 항상 전체 박스 크기야?
A. 아니다. box-sizing 값에 따라 content 크기일 수도 있고 전체 border box 크기일 수도 있다.

Q. 콘텐츠가 박스 밖으로 나가면 무엇을 확인해?
A. width, min-width, overflow, box-sizing, 긴 텍스트, 이미지 크기를 확인한다.

---

# 3. Padding

## 3.1 Padding Concept

### [개념]

`padding`은 Content Area와 Border 사이의 내부 여백이다.

Padding은 요소 내부에서 콘텐츠와 테두리 사이 공간을 만든다.

예:

```css
.card {
  padding: 16px;
}
```

---

### [핵심]

Padding 핵심:

- 내부 여백이다.
- 콘텐츠와 border 사이의 공간을 만든다.
- 요소의 클릭 영역을 넓힐 수 있다.
- background-color는 padding 영역까지 적용된다.
- `content-box`에서는 padding이 width / height에 추가된다.
- `border-box`에서는 padding이 width / height 안에 포함된다.
- button, card, input, section spacing에 자주 사용한다.

방향별 속성:

```css
padding-top: 16px;
padding-right: 16px;
padding-bottom: 16px;
padding-left: 16px;
```

축약형:

```css
padding: 16px;
padding: 12px 16px;
padding: 8px 12px 16px 20px;
```

---

### [실무]

Padding은 Component 내부 여백을 만드는 기본 도구다.

좋은 예:

```css
.festival-card {
  padding: 20px;
  border-radius: 12px;
}
```

Button 예:

```css
.button {
  padding: 12px 16px;
}
```

검수 기준:

- 내부 여백을 margin으로 처리하지 않았는가?
- 클릭 가능한 요소에 충분한 padding이 있는가?
- padding 때문에 width가 초과되지 않는가?
- `box-sizing: border-box`가 적용되어 있는가?
- 상하좌우 padding이 디자인 의도와 일치하는가?

---

### [FAQ]

Q. padding이 뭐야?
A. 콘텐츠와 border 사이의 내부 여백이다.

Q. padding은 언제 써?
A. 카드, 버튼, 입력 필드처럼 요소 내부 공간을 만들 때 사용한다.

Q. padding을 주면 요소 크기가 커져?
A. `content-box`에서는 커지고 `border-box`에서는 지정한 width 안에 포함된다.

Q. 버튼 크기는 padding으로 조절해도 돼?
A. 가능하다. 버튼 내부 여백과 클릭 영역을 확보하는 데 적합하다.

---

# 4. Border

## 4.1 Border Concept

### [개념]

`border`는 padding 바깥에 위치하는 요소의 테두리다.

Border는 시각적 경계, 입력 상태, 카드 구분, 버튼 스타일에 사용한다.

예:

```css
.card {
  border: 1px solid #e5e7eb;
}
```

---

### [핵심]

Border 핵심:

- 요소의 테두리를 만든다.
- `border-width`, `border-style`, `border-color`로 구성된다.
- `border-radius`는 모서리를 둥글게 만든다.
- `content-box`에서는 border가 width / height에 추가된다.
- `border-box`에서는 border가 width / height 안에 포함된다.
- Form error 상태, focus 상태, card 구분에 자주 사용된다.

예:

```css
.input {
  border: 1px solid #d1d5db;
  border-radius: 8px;
}

.input[aria-invalid="true"] {
  border-color: #dc2626;
}
```

---

### [실무]

Border는 상태 표현과 UI 구분에 자주 사용된다.

사용 예:

```css
.card {
  border: 1px solid var(--color-border);
  border-radius: 12px;
}

.card:hover {
  border-color: var(--color-primary);
}
```

주의:

- border 추가로 Layout이 흔들리지 않도록 `border-box` 사용
- focus border와 outline의 접근성 차이 이해
- 색상만으로 상태 전달 금지
- error border에는 Error Message 함께 제공
- 투명 border를 기본으로 두면 hover 시 Layout shift를 줄일 수 있음

예:

```css
.button {
  border: 1px solid transparent;
}

.button:hover {
  border-color: currentColor;
}
```

검수 기준:

- border 추가로 요소 크기가 변하지 않는가?
- error 상태가 border 색상만으로 전달되지 않는가?
- focus state가 명확히 보이는가?
- border-radius가 Component 기준과 일관적인가?

---

### [FAQ]

Q. border는 뭐야?
A. 요소의 padding 바깥에 위치하는 테두리다.

Q. border-radius는 뭐야?
A. 요소의 모서리를 둥글게 만드는 CSS property다.

Q. border를 추가했더니 Layout이 밀리는 이유는?
A. `content-box`에서 border가 요소 크기에 추가되기 때문일 수 있다.

Q. 에러 상태를 border 색상만으로 표시해도 돼?
A. 안 된다. Error Message나 아이콘 등 다른 정보도 함께 제공해야 한다.

---

# 5. Margin

## 5.1 Margin Concept

### [개념]

`margin`은 Border 바깥의 외부 여백이다.

Margin은 요소와 요소 사이의 간격을 만든다.

예:

```css
.card {
  margin-bottom: 24px;
}
```

---

### [핵심]

Margin 핵심:

- 외부 여백이다.
- 요소와 요소 사이 간격을 만든다.
- background-color는 margin 영역에 적용되지 않는다.
- `margin: 0 auto`는 block 요소의 수평 중앙 정렬에 사용할 수 있다.
- vertical margin은 collapse될 수 있다.
- Component 내부 여백은 padding, 외부 간격은 margin 또는 gap을 사용한다.
- Flexbox / Grid에서는 `gap`이 margin보다 명확한 경우가 많다.

방향별 속성:

```css
margin-top: 16px;
margin-right: 16px;
margin-bottom: 16px;
margin-left: 16px;
```

축약형:

```css
margin: 16px;
margin: 0 auto;
margin: 8px 12px 16px 20px;
```

---

### [실무]

Margin은 요소 간 간격을 만드는 데 사용하지만, Component 내부 스타일과 외부 Layout 책임을 분리해야 한다.

권장:

```css
.section {
  margin-block: 48px;
}

.card-list {
  display: grid;
  gap: 24px;
}
```

주의:

```css
.card {
  margin-left: 24px;
  margin-right: 24px;
}
```

Component가 자체적으로 큰 margin을 가지면 재사용성이 떨어질 수 있다.

검수 기준:

- 내부 여백을 margin으로 처리하지 않았는가?
- 반복 요소 간 간격은 gap이 더 적절하지 않은가?
- margin collapse가 발생하지 않는가?
- Component가 외부 Layout 간격을 과도하게 책임지지 않는가?
- `margin: 0 auto` 사용 시 width가 지정되어 있는가?

---

### [FAQ]

Q. margin이 뭐야?
A. 요소 border 바깥의 외부 여백이다.

Q. margin과 padding 차이는 뭐야?
A. padding은 내부 여백이고 margin은 외부 여백이다.

Q. 요소 사이 간격은 margin과 gap 중 뭐가 좋아?
A. Flexbox나 Grid 내부 반복 요소 간격은 gap이 더 명확한 경우가 많다.

Q. margin auto는 언제 써?
A. block 요소를 수평 중앙 정렬할 때 `width`와 함께 사용할 수 있다.

---

## 5.2 Margin Collapse

### [개념]

Margin Collapse는 인접한 block 요소의 vertical margin이 합쳐지는 CSS 동작이다.

주로 위아래 margin에서 발생하며 좌우 margin에는 발생하지 않는다.

---

### [핵심]

Margin Collapse 핵심:

- block 요소의 vertical margin에서 발생할 수 있다.
- 인접 형제 요소의 margin이 합쳐질 수 있다.
- 부모와 첫 번째 / 마지막 자식 margin이 합쳐질 수 있다.
- margin 값이 더해지는 것이 아니라 큰 값 또는 규칙에 따라 합쳐진다.
- Flexbox / Grid container 내부에서는 일반적인 margin collapse가 발생하지 않는다.
- Layout 간격 예측을 어렵게 만들 수 있다.

예:

```css
.title {
  margin-bottom: 24px;
}

.description {
  margin-top: 16px;
}
```

두 margin이 40px로 더해지지 않고 collapse될 수 있다.

---

### [실무]

Margin Collapse를 피하거나 예측 가능하게 하려면 Layout Container와 gap을 사용한다.

권장:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.stack > * {
  margin: 0;
}
```

또는:

```css
.section {
  padding-block: 32px;
}
```

검수 기준:

- 위아래 간격이 예상과 다르면 margin collapse를 의심하는가?
- Flexbox / Grid gap으로 대체 가능한가?
- 자식 margin이 부모 밖으로 튀어나오는 현상이 있는가?
- `padding`, `border`, `overflow`, `display: flow-root`로 collapse를 제어할 필요가 있는가?

---

### [FAQ]

Q. Margin Collapse가 뭐야?
A. 인접한 block 요소의 위아래 margin이 합쳐지는 CSS 동작이다.

Q. margin이 더해지지 않는 이유는 뭐야?
A. vertical margin collapse가 발생했기 때문일 수 있다.

Q. Margin Collapse는 좌우 margin에도 발생해?
A. 아니다. 일반적으로 vertical margin에서 발생한다.

Q. Margin Collapse를 피하려면 어떻게 해?
A. Flexbox/Grid gap 사용, padding 사용, border 추가, `display: flow-root` 등을 고려할 수 있다.

---

# 6. Box Sizing

## 6.1 Content Box

### [개념]

`box-sizing: content-box`는 CSS의 기본 Box Sizing 방식이다.

`width`와 `height`가 Content Area만을 의미하고, padding과 border는 그 바깥에 추가된다.

---

### [핵심]

Content Box 핵심:

- 기본 box-sizing 값이다.
- width는 content 영역 크기다.
- padding과 border가 width에 추가된다.
- 요소의 실제 렌더링 너비가 예상보다 커질 수 있다.
- 반응형 Layout에서 overflow 원인이 될 수 있다.

예:

```css
.box {
  box-sizing: content-box;
  width: 300px;
  padding: 20px;
  border: 1px solid #000;
}
```

실제 너비:

```text
300px content
+ 40px padding
+ 2px border
= 342px
```

---

### [실무]

Content Box는 CSS 기본 동작이지만 실무에서는 직접 사용 빈도가 낮다.

검수 기준:

- width 100% 요소에 padding이 추가되어 overflow가 발생하지 않는가?
- Component 크기 계산이 예상보다 커지지 않는가?
- border 추가 후 Layout이 밀리지 않는가?
- `border-box` reset이 적용되어 있는가?

주의 예:

```css
.input {
  width: 100%;
  padding: 12px;
}
```

`content-box` 상태에서는 input이 부모 너비를 초과할 수 있다.

---

### [FAQ]

Q. content-box가 뭐야?
A. width와 height가 content 영역만 계산하고 padding과 border는 추가되는 box-sizing 방식이다.

Q. content-box가 기본값이야?
A. 일반적으로 기본값은 `content-box`다.

Q. width 100%에 padding을 줬더니 넘치는 이유는?
A. content-box에서는 padding이 100% width 바깥에 추가되기 때문이다.

---

## 6.2 Border Box

### [개념]

`box-sizing: border-box`는 width와 height에 content, padding, border를 모두 포함하는 Box Sizing 방식이다.

실무 Layout에서 가장 많이 사용하는 방식이다.

---

### [핵심]

Border Box 핵심:

- width 안에 padding과 border가 포함된다.
- 요소 크기 계산이 직관적이다.
- 반응형 Layout에 유리하다.
- padding 추가로 요소가 부모 밖으로 넘치는 문제를 줄인다.
- 전역 reset으로 자주 적용한다.

예:

```css
.box {
  box-sizing: border-box;
  width: 300px;
  padding: 20px;
  border: 1px solid #000;
}
```

실제 너비:

```text
300px total
= content + padding + border
```

전역 설정:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

### [실무]

Border Box는 실무 CSS Reset의 기본에 가깝다.

권장:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

사용 효과:

- width 계산 단순화
- Card Layout 안정화
- Form Input 너비 안정화
- Responsive Container overflow 감소
- Border 추가 시 Layout shift 감소

검수 기준:

- 전역 border-box reset이 있는가?
- pseudo element에도 box-sizing이 적용되는가?
- 외부 라이브러리와 충돌하지 않는가?
- Component width 계산이 예측 가능한가?

---

### [FAQ]

Q. border-box가 뭐야?
A. width와 height에 content, padding, border를 포함해서 계산하는 box-sizing 방식이다.

Q. box-sizing border-box는 왜 써?
A. 요소 크기 계산이 직관적이고 padding과 border로 인한 overflow를 줄일 수 있기 때문이다.

Q. border-box는 전역으로 설정해도 돼?
A. 일반적으로 많이 사용한다. `*`, `*::before`, `*::after`에 적용하는 방식이 흔하다.

---

# 7. Width and Height

## 7.1 Width

### [개념]

`width`는 요소의 너비를 지정하는 CSS property다.

Box Sizing 값에 따라 width가 content 영역만 의미할 수도 있고 border box 전체를 의미할 수도 있다.

---

### [핵심]

Width 핵심:

- 요소의 가로 크기를 지정한다.
- `px`, `%`, `rem`, `vw`, `auto`, `min()`, `max()`, `clamp()` 등을 사용할 수 있다.
- `width: 100%`는 기준 부모 너비를 따른다.
- 고정 width는 모바일 overflow 원인이 될 수 있다.
- `max-width`와 함께 사용하면 반응형에 유리하다.
- `min-width` 기본값 때문에 Flex/Grid item overflow가 발생할 수 있다.

예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}
```

---

### [실무]

Responsive Layout에서는 고정 width보다 유연한 width를 우선한다.

좋은 예:

```css
.card {
  width: 100%;
  max-width: 360px;
}
```

주의 예:

```css
.card {
  width: 360px;
}
```

Flex item overflow 대응:

```css
.flex-item {
  min-width: 0;
}
```

검수 기준:

- 고정 width가 모바일 화면을 넘지 않는가?
- `max-width`를 함께 사용했는가?
- 부모 기준이 명확한가?
- flex item에 `min-width: 0`이 필요한가?
- image, table, long text가 width를 초과하지 않는가?

---

### [FAQ]

Q. width는 뭐야?
A. 요소의 가로 크기를 지정하는 CSS property다.

Q. width 100%는 무엇을 기준으로 해?
A. 일반적으로 부모 요소의 content 영역 또는 기준 container 너비를 기준으로 한다.

Q. 고정 width가 문제인 이유는 뭐야?
A. 작은 화면에서 요소가 viewport를 초과해 가로 스크롤을 만들 수 있기 때문이다.

Q. flex item이 부모 밖으로 나가는 이유는 뭐야?
A. 기본 min-width 때문에 줄어들지 못할 수 있으며 `min-width: 0`이 필요할 수 있다.

---

## 7.2 Height

### [개념]

`height`는 요소의 높이를 지정하는 CSS property다.

높이는 콘텐츠 양, 부모 높이, viewport, min-height / max-height와 함께 고려해야 한다.

---

### [핵심]

Height 핵심:

- 요소의 세로 크기를 지정한다.
- 고정 height는 콘텐츠 overflow 원인이 될 수 있다.
- `height: 100%`는 부모 높이가 명확해야 동작한다.
- `min-height`는 최소 높이를 보장한다.
- `max-height`는 최대 높이를 제한한다.
- viewport 기준 높이는 `vh`, `dvh` 등을 사용할 수 있다.
- 버튼과 input 높이는 padding과 line-height 조합으로 관리하는 것이 유연하다.

---

### [실무]

실무에서는 `height` 고정보다 `min-height`를 자주 사용한다.

좋은 예:

```css
.hero {
  min-height: 60vh;
  padding-block: 64px;
}
```

주의 예:

```css
.card {
  height: 200px;
}
```

콘텐츠가 늘어나면 잘릴 수 있다.

Viewport 높이 주의:

```css
.full-screen {
  min-height: 100dvh;
}
```

검수 기준:

- 콘텐츠가 잘리지 않는가?
- 고정 height 대신 min-height가 적절하지 않은가?
- height 100%의 부모 높이가 명확한가?
- 모바일 브라우저 주소창 변화에 대응해야 하는가?
- overflow 처리 방식이 명확한가?

---

### [FAQ]

Q. height는 뭐야?
A. 요소의 세로 크기를 지정하는 CSS property다.

Q. height 100%가 안 먹는 이유는?
A. 부모 요소의 height가 명확히 지정되어 있지 않기 때문일 수 있다.

Q. 고정 height는 왜 위험해?
A. 콘텐츠가 늘어나면 잘리거나 overflow가 발생할 수 있기 때문이다.

Q. min-height는 언제 써?
A. 최소 높이를 보장하면서 콘텐츠 증가에 유연하게 대응하고 싶을 때 사용한다.

---

## 7.3 Min Width Max Width

### [개념]

`min-width`는 요소의 최소 너비를 지정하고 `max-width`는 요소의 최대 너비를 지정한다.

Responsive Design에서 width와 함께 자주 사용한다.

---

### [핵심]

Min / Max Width 핵심:

- `min-width`는 요소가 줄어들 수 있는 최소 너비다.
- `max-width`는 요소가 커질 수 있는 최대 너비다.
- `max-width: 100%`는 부모 너비를 넘지 않도록 한다.
- Container에는 `width: min(...)` 또는 `max-width`를 자주 사용한다.
- Flex/Grid item에는 `min-width: 0`이 필요할 수 있다.
- Image에는 `max-width: 100%`가 기본적으로 유용하다.

예:

```css
.container {
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
}

img {
  max-width: 100%;
  height: auto;
}
```

---

### [실무]

반응형 Container 예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}
```

Flex Text Overflow 대응:

```css
.card-content {
  min-width: 0;
}
```

검수 기준:

- 큰 화면에서 Container가 너무 넓어지지 않는가?
- 작은 화면에서 요소가 줄어드는가?
- 이미지가 부모를 넘지 않는가?
- Flex/Grid item overflow에 `min-width: 0`이 필요한가?
- 고정 width 대신 max-width로 대체 가능한가?

---

### [FAQ]

Q. max-width는 언제 써?
A. 요소가 너무 넓어지지 않게 제한할 때 사용한다.

Q. min-width는 언제 문제가 돼?
A. Flex/Grid item이 줄어들지 못해 overflow를 만들 때 문제가 될 수 있다.

Q. 이미지에 max-width 100%를 쓰는 이유는?
A. 이미지가 부모 요소 너비를 넘지 않도록 하기 위해 사용한다.

---

# 8. Overflow

## 8.1 Overflow Concept

### [개념]

`overflow`는 콘텐츠가 요소의 box를 넘칠 때 처리 방식을 지정하는 CSS property다.

대표 값:

```css
overflow: visible;
overflow: hidden;
overflow: auto;
overflow: scroll;
```

---

### [핵심]

Overflow 핵심:

- `visible`은 넘친 콘텐츠를 그대로 보여준다.
- `hidden`은 넘친 콘텐츠를 잘라낸다.
- `auto`는 필요할 때 스크롤을 만든다.
- `scroll`은 항상 스크롤 영역을 만든다.
- `overflow-x`는 가로 overflow를 제어한다.
- `overflow-y`는 세로 overflow를 제어한다.
- overflow hidden은 dropdown, tooltip, modal이 잘리는 원인이 될 수 있다.
- 가로 스크롤 문제는 overflow 원인 요소를 찾아야 한다.

---

### [실무]

가로 스크롤 Debug Flow:

```text
Viewport Check
→ Overflow Element Inspect
→ Fixed Width Check
→ Image Width Check
→ Table Width Check
→ Flex Item min-width Check
→ Long Text Check
→ Overflow Rule Fix
```

Responsive Table 예:

```css
.table-container {
  overflow-x: auto;
}

.table-container table {
  min-width: 640px;
}
```

긴 텍스트 처리:

```css
.text {
  overflow-wrap: break-word;
}
```

검수 기준:

- 모바일에서 body 가로 스크롤이 생기지 않는가?
- overflow hidden으로 필요한 UI가 잘리지 않는가?
- scroll 영역이 keyboard 접근에 문제 없는가?
- table에는 가로 스크롤 container가 있는가?
- 긴 단어와 URL이 줄바꿈되는가?

---

### [FAQ]

Q. overflow는 뭐야?
A. 콘텐츠가 요소의 박스를 넘칠 때 처리 방식을 지정하는 CSS property다.

Q. 모바일에서 가로 스크롤이 생기는 이유는?
A. 고정 width, 큰 이미지, table, 긴 텍스트, flex item min-width 문제 때문일 수 있다.

Q. overflow hidden은 언제 조심해야 해?
A. dropdown, tooltip, modal, focus outline이 잘릴 수 있으므로 주의해야 한다.

Q. 긴 URL 때문에 화면이 깨지면 어떻게 해?
A. `overflow-wrap: break-word` 등을 사용해 줄바꿈을 허용한다.

---

# 9. Display

## 9.1 Display Concept

### [개념]

`display`는 요소가 화면에서 어떤 box type과 layout context를 가지는지 결정하는 CSS property다.

대표 값:

```css
display: block;
display: inline;
display: inline-block;
display: flex;
display: grid;
display: none;
```

Display는 Box Model, Layout, Alignment, Visibility에 직접 영향을 준다.

---

### [핵심]

Display 핵심:

- `block`은 한 줄 전체 너비를 차지한다.
- `inline`은 콘텐츠 크기만큼만 차지한다.
- `inline-block`은 inline 흐름을 가지면서 width / height 지정이 가능하다.
- `flex`는 1차원 Layout을 만든다.
- `grid`는 2차원 Layout을 만든다.
- `none`은 요소를 화면과 접근성 트리에서 제거한다.
- display 변경은 요소의 크기 계산과 배치 방식에 영향을 준다.

---

### [실무]

Display 선택 기준:

```text
Document Flow Section → block
Text Inline Element → inline
Inline Button-like Box → inline-block or inline-flex
One-dimensional Layout → flex
Two-dimensional Layout → grid
Hide Completely → display none
```

실무 예:

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.card-list {
  display: grid;
  gap: 24px;
}
```

검수 기준:

- 요소 성격에 맞는 display를 사용했는가?
- inline 요소에 width / height가 안 먹는 문제를 이해했는가?
- 정렬 목적에 flex를 사용했는가?
- 카드 목록에 grid가 적절한가?
- 숨김 처리가 접근성에 미치는 영향을 고려했는가?

---

### [FAQ]

Q. display는 뭐야?
A. 요소가 화면에서 배치되는 방식과 layout context를 결정하는 CSS property다.

Q. display block과 inline 차이는 뭐야?
A. block은 한 줄 전체를 차지하고 inline은 콘텐츠 크기만큼만 차지한다.

Q. inline 요소에 width가 안 먹는 이유는?
A. inline 요소는 일반적으로 width / height 지정이 적용되지 않기 때문이다.

Q. flex와 grid는 display 값이야?
A. 맞다. `display: flex`, `display: grid`로 layout context를 만든다.

---

# 10. Block Inline Inline-Block

## 10.1 Block

### [개념]

Block 요소는 일반적으로 새 줄에서 시작하고 가능한 가로 공간 전체를 차지하는 요소다.

대표 요소:

- `div`
- `section`
- `article`
- `main`
- `header`
- `footer`
- `p`
- `h1` ~ `h6`
- `ul`
- `ol`
- `li`

---

### [핵심]

Block 핵심:

- 새 줄에서 시작한다.
- 기본적으로 부모 너비 전체를 차지한다.
- width / height 지정이 가능하다.
- margin / padding / border가 정상적으로 적용된다.
- Layout의 기본 구조를 만들 때 사용된다.

예:

```css
.card {
  display: block;
  width: 100%;
}
```

---

### [실무]

Block 요소는 Page Section, Card, Container, Paragraph에 적합하다.

예:

```html
<section class="section">
  <h2>Popular Festivals</h2>
  <p>Explore popular festivals.</p>
</section>
```

검수 기준:

- 구조적 영역에 block 성격 요소를 사용했는가?
- block 요소가 부모 너비를 모두 차지하는 것이 의도인가?
- 수평 정렬이 필요하면 flex/grid container가 더 적절하지 않은가?
- block 요소 사이 간격을 margin 또는 gap으로 관리하는가?

---

### [FAQ]

Q. block 요소는 뭐야?
A. 새 줄에서 시작하고 일반적으로 부모 너비 전체를 차지하는 요소다.

Q. block 요소에는 width와 height가 적용돼?
A. 적용된다.

Q. 대표적인 block 요소는 뭐야?
A. div, section, article, p, heading, ul, ol 등이 있다.

---

## 10.2 Inline

### [개념]

Inline 요소는 텍스트 흐름 안에서 콘텐츠 크기만큼만 차지하는 요소다.

대표 요소:

- `span`
- `a`
- `strong`
- `em`
- `code`
- `small`

---

### [핵심]

Inline 핵심:

- 새 줄을 만들지 않는다.
- 콘텐츠 크기만큼만 차지한다.
- 일반적으로 width / height 지정이 적용되지 않는다.
- 좌우 padding / margin은 적용되지만 상하 레이아웃 영향은 제한적일 수 있다.
- 텍스트 일부를 의미 있게 표시하거나 링크를 만들 때 사용한다.

예:

```html
<p>
  Visit
  <a href="/festivals/1">Seoul Light Festival</a>
  for details.
</p>
```

---

### [실무]

Inline 요소는 문장 안의 링크, 강조, 코드 조각에 적합하다.

주의:

```css
a {
  width: 200px;
  height: 40px;
}
```

일반 inline 상태에서는 width / height가 기대대로 동작하지 않을 수 있다.

버튼형 링크가 필요하면:

```css
.link-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 16px;
}
```

검수 기준:

- inline 요소에 width / height를 기대하고 있지 않은가?
- 텍스트 흐름 안에 적절히 사용했는가?
- 버튼형 UI는 inline-flex 또는 inline-block을 고려했는가?
- block 요소를 inline 요소 내부에 넣지 않았는가?

---

### [FAQ]

Q. inline 요소는 뭐야?
A. 텍스트 흐름 안에서 콘텐츠 크기만큼만 차지하는 요소다.

Q. inline 요소에는 width와 height가 적용돼?
A. 일반적으로 기대한 방식으로 적용되지 않는다.

Q. a 태그는 inline이야?
A. 기본적으로 inline 요소다.

Q. 링크를 버튼처럼 만들려면 어떻게 해?
A. `display: inline-flex` 또는 `inline-block`으로 변경하고 padding을 적용할 수 있다.

---

## 10.3 Inline Block

### [개념]

`inline-block`은 inline 흐름을 유지하면서 block처럼 width, height, padding, margin을 적용할 수 있는 display 값이다.

---

### [핵심]

Inline Block 핵심:

- 새 줄을 만들지 않는다.
- 콘텐츠 흐름에서는 inline처럼 배치된다.
- width / height 지정이 가능하다.
- padding / margin / border가 box처럼 적용된다.
- 과거에는 메뉴, 버튼, 카드 정렬에 자주 사용했다.
- 현대 Layout에서는 flex, inline-flex를 더 많이 사용하기도 한다.

예:

```css
.badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 999px;
}
```

---

### [실무]

Inline Block은 badge, chip, tag, 작은 label UI에 적합하다.

예:

```html
<span class="tag">Music</span>
```

```css
.tag {
  display: inline-block;
  padding: 4px 8px;
  border: 1px solid #e5e7eb;
  border-radius: 999px;
}
```

주의:

- 여러 inline-block 사이에 HTML 공백이 시각적 간격으로 나타날 수 있다.
- 복잡한 정렬은 flex가 더 적합하다.
- 아이콘 + 텍스트 정렬은 inline-flex가 더 편하다.

검수 기준:

- inline 흐름과 box 크기 지정이 모두 필요한가?
- flex가 더 적절하지 않은가?
- inline-block 사이 공백 문제가 없는가?
- vertical-align 설정이 필요한가?

---

### [FAQ]

Q. inline-block은 뭐야?
A. inline 흐름을 유지하면서 width, height, padding, margin을 적용할 수 있는 display 값이다.

Q. inline과 inline-block 차이는 뭐야?
A. inline-block은 inline처럼 배치되지만 width와 height를 지정할 수 있다.

Q. badge나 tag UI에는 무엇이 좋아?
A. 단순 badge는 inline-block 또는 inline-flex가 적합하다.

---

# 11. Display None and Visibility

## 11.1 Display None

### [개념]

`display: none`은 요소를 화면에서 제거하고 Layout 공간도 차지하지 않게 만드는 CSS 값이다.

일반적으로 접근성 트리에서도 제거된다.

---

### [핵심]

Display None 핵심:

- 요소가 화면에 표시되지 않는다.
- Layout 공간을 차지하지 않는다.
- 일반적으로 screen reader에서도 접근되지 않는다.
- DOM에는 존재하지만 렌더링되지 않는다.
- 조건부 UI 숨김에 사용한다.
- 접근성용 숨김 텍스트에는 적합하지 않을 수 있다.

예:

```css
.modal[hidden] {
  display: none;
}
```

---

### [실무]

Display None은 탭 패널, 모달, 드롭다운, 조건부 영역을 완전히 숨길 때 사용할 수 있다.

React 조건부 렌더링과 함께 사용:

```jsx
{
  isOpen && <div className="modal">Modal Content</div>;
}
```

주의:

- 스크린 리더가 읽어야 하는 텍스트를 display none으로 숨기지 않는다.
- focus 중인 요소를 display none 처리하면 focus 관리 문제가 생길 수 있다.
- transition animation과 함께 사용하면 즉시 사라져 애니메이션이 어려울 수 있다.

검수 기준:

- 완전히 숨겨도 되는 정보인가?
- 접근성 트리에서도 제거되어도 되는가?
- keyboard focus가 숨겨진 요소로 이동하지 않는가?
- hidden 상태와 aria-expanded 상태가 일치하는가?

---

### [FAQ]

Q. display none은 뭐야?
A. 요소를 화면과 Layout에서 제거하는 display 값이다.

Q. display none은 접근성에 영향 있어?
A. 있다. 일반적으로 접근성 트리에서도 제거되어 스크린 리더가 읽지 않는다.

Q. 숨김 텍스트를 display none으로 처리해도 돼?
A. 스크린 리더가 읽어야 하는 텍스트라면 적합하지 않다.

---

## 11.2 Visibility Hidden

### [개념]

`visibility: hidden`은 요소를 보이지 않게 하지만 Layout 공간은 유지하는 CSS property다.

---

### [핵심]

Visibility Hidden 핵심:

- 요소가 화면에 보이지 않는다.
- Layout 공간은 유지된다.
- 일반적으로 사용자와 상호작용할 수 없다.
- `display: none`과 달리 공간을 차지한다.
- 시각적 숨김과 공간 유지가 필요할 때 사용할 수 있다.

예:

```css
.placeholder {
  visibility: hidden;
}
```

---

### [실무]

Visibility Hidden은 공간 유지가 중요한 UI에서 제한적으로 사용한다.

사용 가능:

- Layout shift 방지
- Placeholder 영역 유지
- Hover 전후 공간 유지
- 임시 시각 숨김

주의:

- 접근성 요구사항에 따라 동작 확인 필요
- focus 가능한 요소에 사용하면 혼란을 만들 수 있음
- 단순 조건부 숨김은 display none 또는 conditional rendering이 더 명확할 수 있음

검수 기준:

- 공간 유지가 필요한가?
- 보이지 않는 요소가 focus 대상이 아닌가?
- display none이 더 적절하지 않은가?
- 접근성 트리 노출 여부를 검토했는가?

---

### [FAQ]

Q. visibility hidden은 뭐야?
A. 요소를 보이지 않게 하지만 Layout 공간은 유지하는 CSS property다.

Q. display none과 visibility hidden 차이는 뭐야?
A. display none은 공간도 제거하고 visibility hidden은 공간을 유지한다.

Q. visibility hidden은 언제 써?
A. 요소 공간은 유지하면서 시각적으로만 숨기고 싶을 때 사용한다.

---

# 12. Box Model and Display Debugging

## 12.1 Layout Broken Debug

### [개념]

Layout Broken은 요소가 예상 크기나 위치에서 벗어나는 문제다.

Box Model과 Display 설정은 Layout Broken의 주요 원인이다.

---

### [핵심]

주요 원인:

- `box-sizing` 누락
- 고정 `width`
- 고정 `height`
- 과도한 padding
- border 추가로 크기 증가
- margin collapse
- inline 요소에 width / height 지정
- `display: none`으로 Layout 제거
- `overflow: hidden`으로 UI 잘림
- flex item `min-width` 문제
- image `max-width` 누락
- table overflow 미처리

---

### [실무]

Layout Broken Debug Flow:

```text
Element Inspect
→ Box Model Check
→ box-sizing Check
→ display Check
→ width / height Check
→ padding / border / margin Check
→ overflow Check
→ parent layout Check
→ responsive viewport Check
```

문제 예:

```text
문제: input이 부모 밖으로 삐져나감
원인: width 100% + padding + content-box
해결: box-sizing border-box 적용
```

```text
문제: a 태그 버튼에 width가 안 먹음
원인: inline 요소
해결: display inline-flex 또는 inline-block 적용
```

```text
문제: 모바일에서 가로 스크롤 발생
원인: 고정 width, 큰 이미지, table overflow
해결: max-width 100%, responsive container, overflow-x auto 적용
```

검수 기준:

- DevTools Box Model 패널을 확인했는가?
- display 값이 의도와 일치하는가?
- box-sizing이 border-box인가?
- 고정 width / height가 문제를 만들지 않는가?
- overflow 원인 요소를 특정했는가?

---

### [FAQ]

Q. Layout이 깨질 때 Box Model에서 뭘 봐?
A. content, padding, border, margin, box-sizing, width, height를 확인한다.

Q. 요소가 부모 밖으로 나가면 무엇을 확인해?
A. 고정 width, padding, border-box 여부, image max-width, flex item min-width를 확인한다.

Q. inline 요소에 크기가 안 먹으면 어떻게 해?
A. `display: inline-block`, `inline-flex`, `block` 등으로 변경한다.

Q. 모바일 가로 스크롤은 어떻게 찾나?
A. DevTools로 viewport를 줄이고 overflow를 만드는 요소의 width, image, table, long text를 확인한다.

---

# 13. Comparison Rules

## 13.1 Margin vs Padding

### [개념]

Margin은 요소 바깥 여백이고 Padding은 요소 내부 여백이다.

---

### [핵심]

| 비교           | Margin                        | Padding                     |
| -------------- | ----------------------------- | --------------------------- |
| 위치           | border 바깥                   | content와 border 사이       |
| 목적           | 요소 간 간격                  | 요소 내부 공간              |
| 배경색 적용    | 적용되지 않음                 | 적용됨                      |
| 클릭 영역 영향 | 일반적으로 직접 확장 아님     | 클릭 영역 확장 가능         |
| collapse       | vertical margin collapse 가능 | collapse 없음               |
| 사용 예        | section 간격, card 간격       | card 내부 여백, button 크기 |

---

### [실무]

선택 기준:

```text
Card 내부 공간 → padding
Button 클릭 영역 → padding
Section 사이 간격 → margin or gap
List item 사이 간격 → gap
Component 외부 배치 → parent layout responsibility
```

---

### [FAQ]

Q. margin과 padding 차이는 뭐야?
A. padding은 내부 여백이고 margin은 외부 여백이다.

Q. 카드 안쪽 여백은 margin이야 padding이야?
A. padding이 적절하다.

Q. 카드 사이 간격은 margin이야 padding이야?
A. margin 또는 부모 layout의 gap이 적절하다.

---

## 13.2 Content Box vs Border Box

### [개념]

Content Box와 Border Box는 width / height 계산 방식이 다르다.

---

### [핵심]

| 비교       | content-box        | border-box                 |
| ---------- | ------------------ | -------------------------- |
| width 의미 | content 영역       | content + padding + border |
| padding    | width에 추가       | width 안에 포함            |
| border     | width에 추가       | width 안에 포함            |
| 기본값     | 일반적 기본값      | 실무 reset으로 자주 사용   |
| 장점       | CSS 기본 동작      | 크기 계산 직관적           |
| 주의       | overflow 발생 쉬움 | content 영역이 줄어듦      |

---

### [실무]

선택 기준:

```text
General Project Layout → border-box
Predictable Component Width → border-box
Legacy Default Behavior → content-box
Width 100% Form Input → border-box recommended
```

---

### [FAQ]

Q. content-box와 border-box 차이는 뭐야?
A. content-box는 padding과 border가 width 밖에 추가되고 border-box는 width 안에 포함된다.

Q. 실무에서는 무엇을 더 많이 써?
A. 일반적으로 `box-sizing: border-box`를 전역 reset으로 많이 사용한다.

Q. border-box를 쓰면 좋은 이유는?
A. 요소의 전체 크기를 예측하기 쉽고 responsive layout에서 overflow를 줄일 수 있다.

---

## 13.3 Block vs Inline vs Inline Block

### [개념]

Block, Inline, Inline Block은 요소의 기본 배치 흐름과 크기 적용 방식이 다르다.

---

### [핵심]

| 비교           | block           | inline          | inline-block          |
| -------------- | --------------- | --------------- | --------------------- |
| 줄바꿈         | 새 줄 시작      | 줄 안에 배치    | 줄 안에 배치          |
| 기본 너비      | 부모 너비 전체  | 콘텐츠 너비     | 콘텐츠 또는 지정 너비 |
| width / height | 적용            | 제한적          | 적용                  |
| 사용 예        | section, div, p | span, a, strong | badge, chip           |
| Layout 목적    | 구조            | 텍스트 흐름     | inline box            |

---

### [실무]

선택 기준:

```text
Page Structure → block
Text Link → inline
Badge / Chip → inline-block
Icon + Text Button → inline-flex
Full Layout → flex or grid
```

---

### [FAQ]

Q. block과 inline 차이는 뭐야?
A. block은 새 줄에서 시작하고 전체 너비를 차지하며 inline은 텍스트 흐름 안에서 콘텐츠 크기만 차지한다.

Q. inline-block은 언제 써?
A. 줄 안에 배치하면서 width, height, padding을 적용해야 할 때 사용한다.

Q. 버튼형 링크에는 어떤 display가 좋아?
A. `inline-flex` 또는 `inline-block`이 적합하다.

---

## 13.4 Display None vs Visibility Hidden

### [개념]

`display: none`은 요소와 공간을 제거하고, `visibility: hidden`은 요소를 보이지 않게 하지만 공간은 유지한다.

---

### [핵심]

| 비교        | display: none                    | visibility: hidden    |
| ----------- | -------------------------------- | --------------------- |
| 화면 표시   | 안 보임                          | 안 보임               |
| Layout 공간 | 제거                             | 유지                  |
| 접근성 트리 | 일반적으로 제거                  | 상황에 따라 검토 필요 |
| 상호작용    | 불가                             | 불가                  |
| 사용 예     | 조건부 UI 숨김                   | 공간 유지 숨김        |
| 주의        | screen reader 텍스트 숨김 부적합 | 보이지 않는 공간 혼란 |

---

### [실무]

선택 기준:

```text
Completely Hide UI → display none
Remove from Layout → display none
Keep Space While Hidden → visibility hidden
Accessible Hidden Text → visually-hidden pattern
Conditional React Rendering → render or not render
```

---

### [FAQ]

Q. display none과 visibility hidden 차이는 뭐야?
A. display none은 Layout 공간도 제거하고 visibility hidden은 공간을 유지한다.

Q. 스크린 리더용 텍스트를 display none으로 숨겨도 돼?
A. 권장하지 않는다. 스크린 리더가 읽어야 한다면 visually-hidden 패턴을 사용한다.

Q. 공간을 유지하면서 숨기려면 뭐를 써?
A. `visibility: hidden`을 사용할 수 있다.

---

# 14. Common Mistakes

## 14.1 Box Model Display Common Mistakes

### [개념]

Box Model과 Display 실수는 Layout 깨짐, Overflow, 모바일 가로 스크롤, Component 크기 불일치로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- `box-sizing: border-box` reset 누락
- width 100% 요소에 padding을 추가해 overflow 발생
- margin과 padding 역할 혼동
- margin collapse를 spacing bug로 오해
- Component 내부 간격을 margin으로 과도하게 처리
- 반복 요소 간격을 margin으로 복잡하게 관리
- fixed width 남용
- fixed height로 콘텐츠 잘림
- image `max-width: 100%` 누락
- inline 요소에 width / height 적용 기대
- link button에 display 설정 누락
- overflow hidden으로 dropdown / tooltip 잘림
- table overflow-x 처리 누락
- `display: none`으로 접근성 텍스트 숨김
- `visibility: hidden` 요소가 공간을 차지하는 것을 놓침
- Flex/Grid item에 `min-width: 0` 누락

---

### [실무]

Troubleshooting Flow:

```text
Layout Issue
→ Box Model Check
→ box-sizing Check
→ display Check
→ width / height Check
→ margin / padding Check
→ overflow Check
→ responsive viewport Check
→ accessibility hidden check
```

문제 예:

```text
문제: 모바일에서 페이지가 좌우로 흔들림
원인: 고정 width 또는 이미지 max-width 누락
해결: width 100%, max-width 100%, responsive container 적용
```

```text
문제: 카드 내부 텍스트가 잘림
원인: 고정 height
해결: height 제거 또는 min-height 사용
```

```text
문제: 링크 버튼의 padding은 먹는데 width가 안 먹음
원인: inline display
해결: display inline-flex 적용
```

---

### [FAQ]

Q. Box Model에서 가장 흔한 실수는 뭐야?
A. margin과 padding 혼동, border-box 누락, width 100%와 padding 조합으로 overflow를 만드는 실수다.

Q. Display에서 가장 흔한 실수는 뭐야?
A. inline 요소에 width와 height가 적용될 것이라고 기대하는 실수다.

Q. 모바일 가로 스크롤의 흔한 원인은 뭐야?
A. 고정 width, 큰 이미지, table, 긴 텍스트, flex item min-width 문제다.

Q. Layout 문제는 어떤 순서로 디버깅해?
A. Box Model, box-sizing, display, width/height, margin/padding, overflow, responsive viewport 순서로 확인한다.

---

# 15. Best Practice

## 15.1 Box Model Display Best Practice

### [개념]

Box Model Display Best Practice는 요소 크기 계산, 간격 관리, display 선택, overflow 방지, Responsive Layout 안정성을 높이는 작성 기준이다.

---

### [핵심]

권장 기준:

- 전역 `box-sizing: border-box` 적용
- Component 내부 여백은 padding 사용
- 요소 간 반복 간격은 gap 사용 고려
- Component 외부 margin 책임 최소화
- 고정 width 남용 금지
- 고정 height보다 min-height 고려
- image에 `max-width: 100%`, `height: auto` 적용
- Responsive Container는 `max-width`, `min()`, `%` 활용
- Flex/Grid item overflow에는 `min-width: 0` 검토
- inline 요소 크기 제어가 필요하면 inline-block / inline-flex 사용
- Hide 방식은 display none, visibility hidden, visually-hidden 목적별 구분
- overflow hidden 사용 시 dropdown, tooltip, focus outline 잘림 주의
- table은 overflow-x auto container 고려

---

### [실무]

기본 Reset 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

Responsive Container 예:

```css
.container {
  width: min(100% - 32px, 1200px);
  margin-inline: auto;
}
```

Card 예:

```css
.festival-card {
  padding: 20px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
}

.festival-card-list {
  display: grid;
  gap: 24px;
}
```

Button Link 예:

```css
.link-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 16px;
}
```

Visually Hidden 예:

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

검수 Checklist:

```md
- [ ] `box-sizing: border-box` reset이 있는가?
- [ ] padding과 margin 역할이 구분되어 있는가?
- [ ] 반복 요소 간격에 gap을 고려했는가?
- [ ] 고정 width가 모바일 overflow를 만들지 않는가?
- [ ] 고정 height로 콘텐츠가 잘리지 않는가?
- [ ] image에 max-width와 height auto가 있는가?
- [ ] inline 요소에 width/height를 기대하지 않는가?
- [ ] 버튼형 링크에 inline-flex 또는 inline-block을 사용했는가?
- [ ] overflow hidden으로 필요한 UI가 잘리지 않는가?
- [ ] display none과 visibility hidden 차이를 고려했는가?
- [ ] 스크린 리더용 숨김 텍스트에 display none을 쓰지 않았는가?
- [ ] table overflow-x 처리가 필요한가?
```

---

### [FAQ]

Q. Box Model Display Best Practice는 뭐야?
A. border-box 기준으로 크기를 예측 가능하게 만들고, padding/margin/display/overflow를 목적에 맞게 사용하는 것이다.

Q. Layout 검수에서 가장 먼저 볼 것은 뭐야?
A. box-sizing, width, padding, border, margin, display, overflow를 먼저 확인한다.

Q. 반응형 Layout에서 Box Model이 중요한 이유는 뭐야?
A. padding, border, width 계산이 viewport overflow와 가로 스크롤에 직접 영향을 주기 때문이다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Box Model과 Display를 기준으로 안정적인 Layout을 작성하고 깨짐 문제를 디버깅하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. CSS Box Model이 뭐야?
A. HTML 요소의 공간을 content, padding, border, margin으로 계산하는 방식이다.

Q. Box Model은 왜 중요해?
A. 요소 크기, 간격, 정렬, 반응형 Layout 계산에 직접 영향을 주기 때문이다.

Q. 요소가 예상보다 커지는 이유는 뭐야?
A. width에 padding과 border가 추가되는 content-box 계산 방식 때문일 수 있다.

Q. Box Model 문제는 어떻게 확인해?
A. 브라우저 개발자 도구에서 Layout 또는 Computed 영역의 content, padding, border, margin을 확인한다.

Q. Content Area는 뭐야?
A. 요소 안에서 실제 텍스트, 이미지, 자식 요소가 표시되는 영역이다.

Q. width는 항상 전체 박스 크기야?
A. 아니다. box-sizing 값에 따라 content 크기일 수도 있고 전체 border box 크기일 수도 있다.

Q. padding이 뭐야?
A. 콘텐츠와 border 사이의 내부 여백이다.

Q. padding은 언제 써?
A. 카드, 버튼, 입력 필드처럼 요소 내부 공간을 만들 때 사용한다.

Q. padding을 주면 요소 크기가 커져?
A. `content-box`에서는 커지고 `border-box`에서는 지정한 width 안에 포함된다.

Q. border는 뭐야?
A. 요소의 padding 바깥에 위치하는 테두리다.

Q. border-radius는 뭐야?
A. 요소의 모서리를 둥글게 만드는 CSS property다.

Q. border를 추가했더니 Layout이 밀리는 이유는?
A. `content-box`에서 border가 요소 크기에 추가되기 때문일 수 있다.

Q. margin이 뭐야?
A. 요소 border 바깥의 외부 여백이다.

Q. margin과 padding 차이는 뭐야?
A. padding은 내부 여백이고 margin은 외부 여백이다.

Q. 요소 사이 간격은 margin과 gap 중 뭐가 좋아?
A. Flexbox나 Grid 내부 반복 요소 간격은 gap이 더 명확한 경우가 많다.

Q. margin auto는 언제 써?
A. block 요소를 수평 중앙 정렬할 때 `width`와 함께 사용할 수 있다.

Q. Margin Collapse가 뭐야?
A. 인접한 block 요소의 위아래 margin이 합쳐지는 CSS 동작이다.

Q. margin이 더해지지 않는 이유는 뭐야?
A. vertical margin collapse가 발생했기 때문일 수 있다.

Q. Margin Collapse는 좌우 margin에도 발생해?
A. 아니다. 일반적으로 vertical margin에서 발생한다.

Q. content-box가 뭐야?
A. width와 height가 content 영역만 계산하고 padding과 border는 추가되는 box-sizing 방식이다.

Q. width 100%에 padding을 줬더니 넘치는 이유는?
A. content-box에서는 padding이 100% width 바깥에 추가되기 때문이다.

Q. border-box가 뭐야?
A. width와 height에 content, padding, border를 포함해서 계산하는 box-sizing 방식이다.

Q. box-sizing border-box는 왜 써?
A. 요소 크기 계산이 직관적이고 padding과 border로 인한 overflow를 줄일 수 있기 때문이다.

Q. border-box는 전역으로 설정해도 돼?
A. 일반적으로 많이 사용한다. `*`, `*::before`, `*::after`에 적용하는 방식이 흔하다.

Q. width는 뭐야?
A. 요소의 가로 크기를 지정하는 CSS property다.

Q. width 100%는 무엇을 기준으로 해?
A. 일반적으로 부모 요소의 content 영역 또는 기준 container 너비를 기준으로 한다.

Q. 고정 width가 문제인 이유는 뭐야?
A. 작은 화면에서 요소가 viewport를 초과해 가로 스크롤을 만들 수 있기 때문이다.

Q. flex item이 부모 밖으로 나가는 이유는 뭐야?
A. 기본 min-width 때문에 줄어들지 못할 수 있으며 `min-width: 0`이 필요할 수 있다.

Q. height는 뭐야?
A. 요소의 세로 크기를 지정하는 CSS property다.

Q. height 100%가 안 먹는 이유는?
A. 부모 요소의 height가 명확히 지정되어 있지 않기 때문일 수 있다.

Q. 고정 height는 왜 위험해?
A. 콘텐츠가 늘어나면 잘리거나 overflow가 발생할 수 있기 때문이다.

Q. min-height는 언제 써?
A. 최소 높이를 보장하면서 콘텐츠 증가에 유연하게 대응하고 싶을 때 사용한다.

Q. max-width는 언제 써?
A. 요소가 너무 넓어지지 않게 제한할 때 사용한다.

Q. 이미지에 max-width 100%를 쓰는 이유는?
A. 이미지가 부모 요소 너비를 넘지 않도록 하기 위해 사용한다.

Q. overflow는 뭐야?
A. 콘텐츠가 요소의 박스를 넘칠 때 처리 방식을 지정하는 CSS property다.

Q. 모바일에서 가로 스크롤이 생기는 이유는?
A. 고정 width, 큰 이미지, table, 긴 텍스트, flex item min-width 문제 때문일 수 있다.

Q. overflow hidden은 언제 조심해야 해?
A. dropdown, tooltip, modal, focus outline이 잘릴 수 있으므로 주의해야 한다.

Q. 긴 URL 때문에 화면이 깨지면 어떻게 해?
A. `overflow-wrap: break-word` 등을 사용해 줄바꿈을 허용한다.

Q. display는 뭐야?
A. 요소가 화면에서 배치되는 방식과 layout context를 결정하는 CSS property다.

Q. display block과 inline 차이는 뭐야?
A. block은 한 줄 전체를 차지하고 inline은 콘텐츠 크기만큼만 차지한다.

Q. inline 요소에 width가 안 먹는 이유는?
A. inline 요소는 일반적으로 width / height 지정이 적용되지 않기 때문이다.

Q. flex와 grid는 display 값이야?
A. 맞다. `display: flex`, `display: grid`로 layout context를 만든다.

Q. block 요소는 뭐야?
A. 새 줄에서 시작하고 일반적으로 부모 너비 전체를 차지하는 요소다.

Q. inline 요소는 뭐야?
A. 텍스트 흐름 안에서 콘텐츠 크기만큼만 차지하는 요소다.

Q. a 태그는 inline이야?
A. 기본적으로 inline 요소다.

Q. 링크를 버튼처럼 만들려면 어떻게 해?
A. `display: inline-flex` 또는 `inline-block`으로 변경하고 padding을 적용할 수 있다.

Q. inline-block은 뭐야?
A. inline 흐름을 유지하면서 width, height, padding, margin을 적용할 수 있는 display 값이다.

Q. inline과 inline-block 차이는 뭐야?
A. inline-block은 inline처럼 배치되지만 width와 height를 지정할 수 있다.

Q. badge나 tag UI에는 무엇이 좋아?
A. 단순 badge는 inline-block 또는 inline-flex가 적합하다.

Q. display none은 뭐야?
A. 요소를 화면과 Layout에서 제거하는 display 값이다.

Q. display none은 접근성에 영향 있어?
A. 있다. 일반적으로 접근성 트리에서도 제거되어 스크린 리더가 읽지 않는다.

Q. 숨김 텍스트를 display none으로 처리해도 돼?
A. 스크린 리더가 읽어야 하는 텍스트라면 적합하지 않다.

Q. visibility hidden은 뭐야?
A. 요소를 보이지 않게 하지만 Layout 공간은 유지하는 CSS property다.

Q. display none과 visibility hidden 차이는 뭐야?
A. display none은 공간도 제거하고 visibility hidden은 공간을 유지한다.

Q. Layout이 깨질 때 Box Model에서 뭘 봐?
A. content, padding, border, margin, box-sizing, width, height를 확인한다.

Q. 요소가 부모 밖으로 나가면 무엇을 확인해?
A. 고정 width, padding, border-box 여부, image max-width, flex item min-width를 확인한다.

Q. inline 요소에 크기가 안 먹으면 어떻게 해?
A. `display: inline-block`, `inline-flex`, `block` 등으로 변경한다.

Q. 카드 안쪽 여백은 margin이야 padding이야?
A. padding이 적절하다.

Q. 카드 사이 간격은 margin이야 padding이야?
A. margin 또는 부모 layout의 gap이 적절하다.

Q. content-box와 border-box 차이는 뭐야?
A. content-box는 padding과 border가 width 밖에 추가되고 border-box는 width 안에 포함된다.

Q. 실무에서는 content-box와 border-box 중 무엇을 더 많이 써?
A. 일반적으로 `box-sizing: border-box`를 전역 reset으로 많이 사용한다.

Q. block과 inline 차이는 뭐야?
A. block은 새 줄에서 시작하고 전체 너비를 차지하며 inline은 텍스트 흐름 안에서 콘텐츠 크기만 차지한다.

Q. display none과 visibility hidden 차이는 뭐야?
A. display none은 Layout 공간도 제거하고 visibility hidden은 공간을 유지한다.

Q. 스크린 리더용 텍스트를 display none으로 숨겨도 돼?
A. 권장하지 않는다. 스크린 리더가 읽어야 한다면 visually-hidden 패턴을 사용한다.

Q. Box Model에서 가장 흔한 실수는 뭐야?
A. margin과 padding 혼동, border-box 누락, width 100%와 padding 조합으로 overflow를 만드는 실수다.

Q. Display에서 가장 흔한 실수는 뭐야?
A. inline 요소에 width와 height가 적용될 것이라고 기대하는 실수다.

Q. 모바일 가로 스크롤의 흔한 원인은 뭐야?
A. 고정 width, 큰 이미지, table, 긴 텍스트, flex item min-width 문제다.

Q. Box Model Display Best Practice는 뭐야?
A. border-box 기준으로 크기를 예측 가능하게 만들고, padding/margin/display/overflow를 목적에 맞게 사용하는 것이다.

Q. 반응형 Layout에서 Box Model이 중요한 이유는 뭐야?
A. padding, border, width 계산이 viewport overflow와 가로 스크롤에 직접 영향을 주기 때문이다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Box Model과 Display를 기준으로 안정적인 Layout을 작성하고 깨짐 문제를 디버깅하게 만드는 것이다.
