# HTML CSS Foundation Part11 - Typography Color Spacing

---

# 1. Typography

## 1.1 Typography Concept

### [개념]

Typography는 웹 페이지에서 텍스트의 글꼴, 크기, 굵기, 줄 높이, 간격, 행 길이, 계층 구조를 설계하는 CSS 영역이다.

Typography는 단순히 글자를 예쁘게 만드는 것이 아니라 콘텐츠 가독성, 정보 계층, 접근성, 브랜드 일관성을 만드는 핵심 기준이다.

대표 CSS property:

```css
font-family
font-size
font-weight
line-height
letter-spacing
text-align
text-decoration
text-transform
```

---

### [핵심]

Typography 핵심:

- 본문은 읽기 쉬운 font-size와 line-height가 필요하다.
- 제목은 heading structure와 시각 hierarchy가 함께 필요하다.
- `font-family`는 글꼴 후보 목록을 지정한다.
- `font-size`는 글자 크기를 지정한다.
- `font-weight`는 글자 굵기를 지정한다.
- `line-height`는 줄 간격을 지정한다.
- `letter-spacing`은 글자 간격을 지정한다.
- `text-align`은 텍스트 정렬을 지정한다.
- 긴 본문은 적절한 최대 줄 길이가 필요하다.
- 색상 대비는 접근성과 직접 연결된다.

---

### [실무]

2026 실무 기준에서 Typography는 Component UI와 Design System의 기본 토큰으로 관리한다.

Frontend Agent는 Typography 작성 시 아래 기준을 함께 검토해야 한다.

- Heading hierarchy
- Body text readability
- Responsive font scale
- Line height
- Text contrast
- Font fallback
- Button text readability
- Form label readability
- Error message readability
- Long text wrapping
- Internationalization 대응
- Mobile readability

Typography 작성 Flow:

```text
Content Role 확인
→ Heading / Body / Caption 구분
→ font-size 결정
→ line-height 결정
→ font-weight 결정
→ color contrast 확인
→ responsive scale 확인
→ overflow / wrapping 확인
```

---

### [FAQ]

Q. Typography가 뭐야?
A. 웹 텍스트의 글꼴, 크기, 굵기, 줄 높이, 간격, 계층 구조를 설계하는 CSS 영역이다.

Q. Typography는 왜 중요해?
A. 콘텐츠 가독성, 정보 계층, 접근성, 브랜드 일관성에 직접 영향을 주기 때문이다.

Q. 글자 크기만 맞추면 Typography가 끝이야?
A. 아니다. line-height, font-weight, contrast, spacing, responsive scale까지 함께 고려해야 한다.

Q. Typography 문제는 무엇부터 확인해?
A. font-size, line-height, contrast, heading hierarchy, text wrapping을 먼저 확인한다.

---

# 2. Font Family

## 2.1 font-family

### [개념]

`font-family`는 텍스트에 사용할 글꼴 목록을 지정하는 CSS property다.

브라우저는 앞에 있는 글꼴부터 사용할 수 있는 글꼴을 찾고, 사용할 수 없으면 다음 후보로 fallback한다.

예:

```css
body {
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}
```

---

### [핵심]

Font Family 핵심:

- 여러 font 후보를 comma로 나열한다.
- 글꼴 이름에 공백이 있으면 따옴표를 사용한다.
- 마지막에는 generic family를 지정한다.
- 대표 generic family는 `serif`, `sans-serif`, `monospace`, `cursive`, `fantasy`다.
- Web Font 사용 시 로딩 성능을 고려해야 한다.
- 한글, 영어, 숫자, 아이콘 fallback을 고려한다.
- 폰트가 로드되지 않아도 읽을 수 있어야 한다.

---

### [실무]

System Font Stack 예:

```css
:root {
  --font-sans:
    system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
}

body {
  font-family: var(--font-sans);
}
```

Code Font 예:

```css
code,
pre {
  font-family: var(--font-mono);
}
```

검수 기준:

- generic family fallback이 있는가?
- 한글이 깨지거나 어색하게 표시되지 않는가?
- Web Font 로딩 실패 시 fallback이 자연스러운가?
- 너무 많은 font weight를 로드하지 않았는가?
- code text에는 monospace 계열을 사용했는가?

---

### [FAQ]

Q. font-family는 뭐야?
A. 텍스트에 사용할 글꼴 후보 목록을 지정하는 CSS property다.

Q. font-family에 여러 글꼴을 쓰는 이유는?
A. 앞 글꼴을 사용할 수 없을 때 다음 글꼴로 fallback하기 위해서다.

Q. 마지막에 sans-serif를 쓰는 이유는?
A. 구체적인 글꼴이 없을 때 브라우저가 기본 sans-serif 글꼴을 사용하게 하기 위해서다.

Q. code에는 어떤 font-family가 좋아?
A. `monospace` 계열 글꼴이 적합하다.

---

# 3. Font Size

## 3.1 font-size

### [개념]

`font-size`는 텍스트의 글자 크기를 지정하는 CSS property다.

Font Size는 가독성, 정보 계층, 반응형 디자인에 직접 영향을 준다.

---

### [핵심]

Font Size 핵심:

- 본문 기본 크기는 보통 `1rem` 기준으로 관리한다.
- Heading은 body보다 명확히 큰 scale을 가진다.
- `rem`은 root font-size 기준이다.
- `em`은 현재 요소 또는 부모 font-size 기준이다.
- `px`는 고정 크기다.
- `clamp()`는 반응형 font-size에 유용하다.
- 모바일에서 너무 작은 글자는 가독성과 접근성 문제가 된다.
- 큰 화면에서 제목만 과도하게 커지지 않도록 제한한다.

예:

```css
body {
  font-size: 1rem;
}

.page-title {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

---

### [실무]

Font Scale 예:

```css
:root {
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;
}
```

사용 예:

```css
.card-title {
  font-size: var(--text-xl);
}

.card-description {
  font-size: var(--text-base);
}
```

검수 기준:

- 본문 글자가 모바일에서 읽기 쉬운가?
- Heading과 Body의 계층이 명확한가?
- rem 기반 scale을 사용하는가?
- 글자 크기가 고정 px만으로 구성되어 있지 않은가?
- 반응형 heading에는 clamp를 고려했는가?

---

### [FAQ]

Q. font-size는 뭐야?
A. 텍스트의 글자 크기를 지정하는 CSS property다.

Q. rem과 px 중 뭐가 좋아?
A. 일반적으로 rem은 사용자 설정과 확장성에 더 유리하고 px는 고정 크기에 적합하다.

Q. clamp()는 font-size에 왜 써?
A. 최소값과 최대값 사이에서 viewport에 따라 자연스럽게 변하는 글자 크기를 만들 수 있기 때문이다.

Q. 모바일에서 글자가 너무 작으면 뭐가 문제야?
A. 가독성이 떨어지고 접근성 문제가 생길 수 있다.

---

# 4. Font Weight

## 4.1 font-weight

### [개념]

`font-weight`는 텍스트의 굵기를 지정하는 CSS property다.

텍스트의 강조, 제목 계층, 버튼 가독성, 정보 우선순위 표현에 사용한다.

예:

```css
.title {
  font-weight: 700;
}
```

---

### [핵심]

Font Weight 핵심:

- `normal`은 일반적으로 400이다.
- `bold`는 일반적으로 700이다.
- 숫자 값은 100부터 900까지 사용할 수 있다.
- 실제 사용 가능한 굵기는 font file 또는 system font에 따라 다르다.
- Heading은 보통 body보다 높은 weight를 사용한다.
- 너무 많은 굵기 차이는 UI 일관성을 떨어뜨릴 수 있다.
- 색상 대신 굵기로 정보 계층을 보완할 수 있다.

---

### [실무]

권장 Weight Scale 예:

```css
:root {
  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
}
```

사용 예:

```css
.section-title {
  font-weight: var(--font-bold);
}

.button {
  font-weight: var(--font-semibold);
}

.helper-text {
  font-weight: var(--font-regular);
}
```

검수 기준:

- 제목, 본문, 보조 텍스트 weight가 구분되는가?
- 너무 많은 font-weight를 사용하지 않았는가?
- Web Font에서 실제 해당 weight가 로드되는가?
- 강조가 색상만으로 전달되지 않는가?
- button text가 충분히 읽기 쉬운가?

---

### [FAQ]

Q. font-weight는 뭐야?
A. 텍스트의 굵기를 지정하는 CSS property다.

Q. bold와 700은 같아?
A. 일반적으로 bold는 700에 대응된다.

Q. font-weight 500을 줬는데 차이가 없는 이유는?
A. 사용 중인 font가 해당 weight를 지원하지 않거나 브라우저가 대체 렌더링하기 때문일 수 있다.

Q. 굵기를 많이 쓰면 좋아?
A. 아니다. 제한된 weight scale을 사용해야 UI 일관성이 좋아진다.

---

# 5. Line Height

## 5.1 line-height

### [개념]

`line-height`는 텍스트 줄의 높이를 지정하는 CSS property다.

Line Height는 본문 가독성, 버튼 높이, 입력 필드 높이, 텍스트 정렬에 영향을 준다.

---

### [핵심]

Line Height 핵심:

- 줄 간격을 결정한다.
- 본문은 보통 `1.4` ~ `1.7` 범위가 읽기 쉽다.
- 제목은 본문보다 조금 더 타이트한 line-height를 사용할 수 있다.
- 단위 없는 line-height는 상속과 확장성에 유리하다.
- 버튼과 input은 padding과 line-height 조합으로 높이를 만든다.
- line-height가 너무 작으면 글자가 답답해 보인다.
- line-height가 너무 크면 콘텐츠 밀도가 낮아진다.

예:

```css
body {
  line-height: 1.5;
}

h1 {
  line-height: 1.1;
}
```

---

### [실무]

Typography Token 예:

```css
:root {
  --leading-tight: 1.1;
  --leading-snug: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.7;
}
```

사용 예:

```css
.card-title {
  line-height: var(--leading-snug);
}

.card-description {
  line-height: var(--leading-normal);
}
```

검수 기준:

- 본문 line-height가 충분한가?
- Heading line-height가 너무 크거나 작지 않은가?
- button text가 수직으로 어긋나지 않는가?
- line-height를 px 고정값으로만 관리하지 않았는가?
- 줄바꿈이 많은 한글 본문에서도 읽기 쉬운가?

---

### [FAQ]

Q. line-height는 뭐야?
A. 텍스트 줄의 높이와 줄 간격을 지정하는 CSS property다.

Q. 본문 line-height는 어느 정도가 좋아?
A. 보통 1.4에서 1.7 사이가 읽기 쉬운 경우가 많다.

Q. 단위 없는 line-height가 좋은 이유는?
A. font-size 변화에 따라 자연스럽게 비례하고 상속 관리가 쉬워지기 때문이다.

Q. 버튼 높이는 line-height로만 맞춰?
A. 보통 line-height와 padding을 함께 사용해 높이와 클릭 영역을 만든다.

---

# 6. Text Alignment and Decoration

## 6.1 text-align

### [개념]

`text-align`은 inline content의 가로 정렬 방식을 지정하는 CSS property다.

문단, 제목, 버튼 텍스트, 카드 내용 정렬에 사용한다.

예:

```css
.empty-state {
  text-align: center;
}
```

---

### [핵심]

Text Align 핵심:

- `left`, `right`, `center`, `justify`, `start`, `end` 값을 사용할 수 있다.
- `center`는 제목, empty state, hero section에 자주 사용한다.
- 긴 본문에는 일반적으로 left 또는 start 정렬이 읽기 쉽다.
- `justify`는 단어 간격 문제를 만들 수 있다.
- 다국어 대응에는 `start`, `end`가 유용할 수 있다.
- block 자체 중앙 정렬은 `margin-inline: auto`, Flexbox, Grid를 사용한다.

---

### [실무]

예:

```css
.hero {
  text-align: center;
}

.prose {
  text-align: start;
}
```

검수 기준:

- 텍스트 정렬 문제와 block 정렬 문제를 혼동하지 않았는가?
- 긴 본문을 center 정렬로 처리하지 않았는가?
- 다국어 방향성을 고려해 start/end 사용이 더 적절한가?
- 버튼 내부 텍스트 정렬과 버튼 자체 정렬을 구분했는가?

---

### [FAQ]

Q. text-align은 뭐야?
A. inline content의 가로 정렬을 지정하는 CSS property다.

Q. div 자체를 가운데 두려면 text-align center를 쓰면 돼?
A. 아니다. block 자체 정렬은 margin, Flexbox, Grid를 사용한다.

Q. 긴 본문도 center 정렬하면 좋아?
A. 일반적으로 읽기 어렵다. 긴 본문은 start 또는 left 정렬이 좋다.

---

## 6.2 text-decoration

### [개념]

`text-decoration`은 텍스트의 밑줄, 취소선, 윗줄 같은 장식을 지정하는 CSS property다.

링크 스타일과 상태 표현에 자주 사용한다.

---

### [핵심]

Text Decoration 핵심:

- 링크는 기본적으로 underline을 가진다.
- underline 제거 시 링크임을 알 수 있는 다른 표시가 필요하다.
- `text-decoration: none` 남용은 접근성 문제를 만들 수 있다.
- `text-decoration-line`, `text-decoration-color`, `text-decoration-thickness`를 사용할 수 있다.
- 취소선은 삭제되었거나 비활성 의미에 사용할 수 있다.

예:

```css
a {
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.16em;
}
```

---

### [실무]

링크 스타일 예:

```css
.text-link {
  color: var(--color-link);
  text-decoration: underline;
  text-underline-offset: 0.16em;
}

.text-link:hover {
  text-decoration-thickness: 0.12em;
}
```

검수 기준:

- 링크가 링크처럼 인식되는가?
- 색상만으로 링크를 구분하지 않았는가?
- underline 제거 시 hover/focus 외 기본 구분이 있는가?
- 취소선이 의미와 일치하는가?

---

### [FAQ]

Q. text-decoration은 뭐야?
A. 텍스트에 밑줄, 취소선, 윗줄 같은 장식을 지정하는 property다.

Q. 링크 밑줄을 없애도 돼?
A. 가능하지만 링크임을 알 수 있는 다른 시각적 단서가 필요하다.

Q. 색상만으로 링크를 표시해도 돼?
A. 권장하지 않는다. 접근성을 위해 underline 등 추가 단서를 제공하는 것이 좋다.

---

# 7. Text Wrapping and Overflow

## 7.1 Text Wrapping

### [개념]

Text Wrapping은 텍스트가 Container 너비를 초과하지 않도록 줄바꿈되는 동작이다.

긴 단어, URL, 코드, 사용자 입력 텍스트는 Layout overflow를 만들 수 있다.

---

### [핵심]

Text Wrapping 핵심:

- 일반 문장은 자연스럽게 줄바꿈된다.
- 긴 URL이나 긴 단어는 overflow를 만들 수 있다.
- `overflow-wrap: break-word`는 긴 단어를 줄바꿈할 수 있게 한다.
- `word-break: break-all`은 더 강하게 글자를 쪼갤 수 있어 주의가 필요하다.
- `white-space`는 공백과 줄바꿈 처리 방식을 결정한다.
- 말줄임은 `text-overflow: ellipsis`와 함께 사용한다.

예:

```css
.content {
  overflow-wrap: break-word;
}
```

---

### [실무]

긴 텍스트 대응:

```css
.card-description {
  overflow-wrap: break-word;
}

.code-inline {
  overflow-wrap: anywhere;
}
```

한 줄 말줄임:

```css
.one-line-ellipsis {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

검수 기준:

- 긴 URL이 Layout을 깨지 않는가?
- 사용자 입력 텍스트가 overflow를 만들지 않는가?
- 말줄임이 필요한 UI인가?
- 말줄임으로 중요한 정보가 사라지지 않는가?
- tooltip이나 상세보기로 전체 텍스트 접근이 가능한가?

---

### [FAQ]

Q. 긴 텍스트가 박스 밖으로 나가면 어떻게 해?
A. `overflow-wrap: break-word` 또는 `overflow-wrap: anywhere`를 검토한다.

Q. text-overflow ellipsis는 언제 써?
A. 한 줄 또는 제한된 영역에서 텍스트를 말줄임으로 표시할 때 사용한다.

Q. ellipsis만 주면 말줄임이 돼?
A. 아니다. 보통 `overflow: hidden`, `white-space: nowrap`, `text-overflow: ellipsis`가 함께 필요하다.

Q. word-break break-all은 언제 조심해야 해?
A. 모든 글자를 강제로 끊을 수 있어 가독성이 떨어질 수 있으므로 주의해야 한다.

---

# 8. Color

## 8.1 Color Concept

### [개념]

Color는 UI의 텍스트, 배경, 테두리, 상태, 강조, 브랜드 표현을 담당하는 CSS 속성 영역이다.

Color는 시각 디자인뿐 아니라 접근성, 상태 전달, 사용자 피드백과 연결된다.

대표 property:

```css
color
background-color
border-color
outline-color
caret-color
accent-color
```

---

### [핵심]

Color 핵심:

- `color`는 텍스트 색상이다.
- `background-color`는 배경 색상이다.
- `border-color`는 테두리 색상이다.
- 상태 색상은 success, warning, error, info 등으로 관리한다.
- 색상만으로 정보를 전달하면 접근성 문제가 생길 수 있다.
- 텍스트와 배경의 contrast가 충분해야 한다.
- Theme 대응을 위해 CSS Variable 사용을 고려한다.
- Dark Mode를 고려할 경우 semantic color token이 중요하다.

---

### [실무]

Semantic Color Token 예:

```css
:root {
  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-border: #e5e7eb;
  --color-primary: #2563eb;
  --color-danger: #dc2626;
  --color-success: #16a34a;
}
```

사용 예:

```css
body {
  color: var(--color-text);
  background-color: var(--color-background);
}

.error-message {
  color: var(--color-danger);
}
```

검수 기준:

- 색상 이름이 의미 기반인가?
- 텍스트와 배경 contrast가 충분한가?
- error 상태를 색상만으로 표시하지 않는가?
- dark mode 대응 가능성이 있는 구조인가?
- 임의 hex 값이 Component마다 흩어져 있지 않은가?

---

### [FAQ]

Q. CSS color는 뭐야?
A. 텍스트, 배경, 테두리, 상태, 브랜드 표현에 사용하는 색상 관련 CSS 영역이다.

Q. color와 background-color 차이는 뭐야?
A. color는 텍스트 색상이고 background-color는 배경 색상이다.

Q. 색상만으로 에러를 표시해도 돼?
A. 안 된다. 에러 메시지, 아이콘, aria-invalid 같은 추가 정보가 필요하다.

Q. Semantic Color Token은 왜 필요해?
A. 색상을 역할 기준으로 관리해 유지보수와 theme 대응을 쉽게 하기 위해 필요하다.

---

## 8.2 Color Format

### [개념]

CSS Color Format은 색상을 표현하는 방식이다.

대표 형식:

```css
hex
rgb()
rgba()
hsl()
hsla()
oklch()
currentColor
transparent
```

---

### [핵심]

Color Format 핵심:

- Hex는 가장 흔한 색상 표기 중 하나다.
- `rgb()`는 red, green, blue 기반 색상이다.
- `rgba()`는 alpha 투명도를 포함한다.
- `hsl()`은 hue, saturation, lightness 기반 색상이다.
- `oklch()`는 최신 색상 공간 기반 표현이다.
- `currentColor`는 현재 text color 값을 사용한다.
- `transparent`는 투명 색상을 의미한다.
- 프로젝트 내 색상 표기 방식은 일관성이 중요하다.

---

### [실무]

currentColor 예:

```css
.icon-button {
  color: var(--color-primary);
  border: 1px solid currentColor;
}
```

Transparent Border 예:

```css
.button {
  border: 1px solid transparent;
}

.button:hover {
  border-color: currentColor;
}
```

검수 기준:

- 프로젝트에서 색상 표기 방식이 일관적인가?
- currentColor로 icon/border 색상을 일관되게 관리할 수 있는가?
- alpha 색상 사용 시 contrast가 충분한가?
- 최신 색상 포맷 사용 시 브라우저 지원을 검토했는가?

---

### [FAQ]

Q. CSS 색상은 어떤 형식으로 쓸 수 있어?
A. hex, rgb, rgba, hsl, oklch, currentColor, transparent 등을 사용할 수 있다.

Q. currentColor는 뭐야?
A. 현재 요소의 `color` 값을 재사용하는 CSS 키워드다.

Q. transparent는 뭐야?
A. 투명한 색상을 의미한다.

Q. rgba는 언제 써?
A. 색상에 투명도를 적용해야 할 때 사용할 수 있다.

---

## 8.3 Contrast

### [개념]

Contrast는 텍스트와 배경 또는 UI 요소 간의 명도 차이다.

충분한 Contrast는 텍스트 가독성과 접근성의 핵심이다.

---

### [핵심]

Contrast 핵심:

- 텍스트와 배경의 대비가 충분해야 한다.
- 낮은 contrast는 읽기 어려운 UI를 만든다.
- disabled 상태도 완전히 읽기 어려울 정도로 흐리면 안 된다.
- placeholder text는 너무 옅으면 안 된다.
- error, success, warning 색상도 배경과 구분되어야 한다.
- 색상 조합은 실제 배경 위에서 확인해야 한다.

---

### [실무]

좋은 예:

```css
body {
  color: var(--color-text);
  background-color: var(--color-background);
}

.muted-text {
  color: var(--color-text-muted);
}
```

주의 예:

```css
.helper-text {
  color: #cccccc;
  background-color: #ffffff;
}
```

검수 기준:

- 본문 텍스트 contrast가 충분한가?
- 보조 텍스트가 지나치게 흐리지 않은가?
- button text와 background contrast가 충분한가?
- error text가 배경과 충분히 구분되는가?
- hover/focus 상태에서 contrast가 유지되는가?

---

### [FAQ]

Q. Contrast가 뭐야?
A. 텍스트와 배경 또는 UI 요소 간의 명도 차이다.

Q. Contrast는 왜 중요해?
A. 낮은 contrast는 텍스트를 읽기 어렵게 만들고 접근성 문제를 만든다.

Q. placeholder 색상은 옅게 해도 돼?
A. 가능하지만 너무 옅으면 입력 힌트를 읽기 어려워진다.

Q. disabled 색상은 얼마나 흐리게 해도 돼?
A. 비활성 상태를 표현하되 정보가 완전히 읽기 어려울 정도로 흐리게 만들면 안 된다.

---

# 9. Background

## 9.1 background-color

### [개념]

`background-color`는 요소의 배경 색상을 지정하는 CSS property다.

배경은 텍스트 contrast, section 구분, card surface, button 상태 표현에 사용한다.

---

### [핵심]

Background Color 핵심:

- 요소의 배경색을 지정한다.
- padding 영역까지 배경이 적용된다.
- margin 영역에는 배경이 적용되지 않는다.
- 텍스트 색상과 contrast를 함께 고려해야 한다.
- Card, Button, Section, Modal, Badge에 자주 사용한다.
- State Background는 semantic token으로 관리하는 것이 좋다.

예:

```css
.card {
  background-color: var(--color-surface);
}
```

---

### [실무]

Surface Token 예:

```css
:root {
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-surface-elevated: #ffffff;
}

body {
  background-color: var(--color-background);
}

.card {
  background-color: var(--color-surface-elevated);
}
```

검수 기준:

- background-color와 text color contrast가 충분한가?
- section 구분이 명확한가?
- card surface가 page background와 구분되는가?
- background만으로 상태를 전달하지 않는가?
- dark mode 대응 시 semantic token으로 교체 가능한가?

---

### [FAQ]

Q. background-color는 뭐야?
A. 요소의 배경 색상을 지정하는 CSS property다.

Q. background-color는 margin 영역에도 적용돼?
A. 아니다. margin 영역에는 배경이 적용되지 않는다.

Q. 배경색을 바꿀 때 무엇을 함께 확인해야 해?
A. 텍스트 색상과 contrast를 반드시 함께 확인해야 한다.

---

## 9.2 background-image

### [개념]

`background-image`는 요소의 배경에 이미지를 지정하는 CSS property다.

장식 이미지, hero background, gradient overlay에 사용할 수 있다.

---

### [핵심]

Background Image 핵심:

- CSS 배경 이미지다.
- 콘텐츠 이미지에는 `img`를 사용한다.
- 의미 있는 이미지는 background-image만으로 처리하지 않는다.
- `background-size`, `background-position`, `background-repeat`와 함께 사용한다.
- 배경 이미지 위 텍스트는 contrast를 확인해야 한다.
- 장식 목적에 적합하다.

예:

```css
.hero {
  background-image: url("/images/hero.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
```

---

### [실무]

Gradient Overlay 예:

```css
.hero {
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)),
    url("/images/festival-hero.jpg");
  background-size: cover;
  background-position: center;
}
```

검수 기준:

- 이미지가 의미 있는 콘텐츠인가 장식인가?
- 의미 있는 이미지라면 img와 alt가 더 적절하지 않은가?
- 배경 위 텍스트 contrast가 충분한가?
- 작은 화면에서 핵심 이미지 영역이 잘리지 않는가?
- background-size cover로 중요한 부분이 잘리지 않는가?

---

### [FAQ]

Q. background-image는 언제 써?
A. 장식 배경, hero 배경, gradient overlay처럼 콘텐츠 의미보다 시각 배경 목적일 때 사용한다.

Q. 의미 있는 이미지를 background-image로 넣어도 돼?
A. 권장하지 않는다. 의미 있는 이미지는 img와 alt를 사용하는 것이 좋다.

Q. background-size cover는 뭐야?
A. 이미지가 요소를 꽉 채우도록 비율을 유지하며 확대 또는 축소하는 값이다.

Q. 배경 이미지 위 텍스트는 무엇을 확인해야 해?
A. 텍스트와 배경 이미지 사이 contrast를 확인해야 한다.

---

# 10. Spacing

## 10.1 Spacing Concept

### [개념]

Spacing은 UI 요소 사이와 내부의 여백을 설계하는 기준이다.

Spacing은 Layout 안정성, 시각적 계층, 터치 영역, 가독성, Component 재사용성에 영향을 준다.

대표 property:

```css
margin
padding
gap
inset
```

---

### [핵심]

Spacing 핵심:

- `padding`은 요소 내부 여백이다.
- `margin`은 요소 외부 여백이다.
- `gap`은 Flex/Grid Item 사이 간격이다.
- Spacing scale을 사용하면 UI 일관성이 높아진다.
- 무작위 spacing 값은 유지보수성을 떨어뜨린다.
- Component 내부 여백과 외부 layout 간격을 구분해야 한다.
- 반복 요소 간격은 gap을 우선 고려한다.
- Touch target 확보에도 spacing이 중요하다.

---

### [실무]

Spacing Token 예:

```css
:root {
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
}
```

사용 예:

```css
.card {
  padding: var(--space-6);
}

.card-list {
  display: grid;
  gap: var(--space-6);
}

.section {
  padding-block: var(--space-12);
}
```

검수 기준:

- spacing 값이 scale 기반인가?
- Component 내부 padding과 외부 margin이 구분되는가?
- 반복 목록 간격에 gap을 사용하는가?
- 모바일에서 spacing이 과도하지 않은가?
- touch target 확보에 충분한 여백이 있는가?

---

### [FAQ]

Q. Spacing이 뭐야?
A. UI 요소의 내부 여백과 외부 간격을 설계하는 기준이다.

Q. padding과 margin 차이는 뭐야?
A. padding은 내부 여백이고 margin은 외부 여백이다.

Q. gap은 언제 써?
A. Flexbox나 Grid의 반복 Item 사이 간격을 관리할 때 사용한다.

Q. Spacing scale은 왜 필요해?
A. 무작위 여백 값을 줄이고 UI 일관성과 유지보수성을 높이기 위해 필요하다.

---

## 10.2 Margin Padding Gap

### [개념]

Margin, Padding, Gap은 모두 여백을 만들지만 적용 위치와 책임이 다르다.

올바른 구분은 Layout 품질과 Component 재사용성에 중요하다.

---

### [핵심]

Margin 핵심:

- 요소 외부 간격
- section 사이 간격
- 특정 요소만 밀어야 할 때 사용
- vertical margin collapse 주의

Padding 핵심:

- 요소 내부 간격
- card, button, input 내부 공간
- 클릭 영역 확대에 사용
- background-color 영역에 포함

Gap 핵심:

- Flex/Grid Item 사이 간격
- 반복 요소 간격 관리
- 첫/마지막 item 별도 처리 불필요
- margin collapse 없음

---

### [실무]

선택 기준:

```text
Card 내부 여백 → padding
Button 클릭 영역 → padding
List item 사이 간격 → gap
Grid column 간격 → gap
Section 간격 → padding-block or margin
특정 하나만 분리 → margin
```

예:

```css
.card {
  padding: 1.5rem;
}

.card-list {
  display: grid;
  gap: 1.5rem;
}

.section {
  padding-block: 4rem;
}
```

검수 기준:

- 내부 여백을 margin으로 처리하지 않았는가?
- 반복 item 사이 간격에 gap을 고려했는가?
- Component가 외부 margin을 과도하게 가지지 않는가?
- Section spacing이 일관적인가?
- margin collapse 문제가 없는가?

---

### [FAQ]

Q. margin padding gap은 어떻게 구분해?
A. 내부 여백은 padding, 외부 간격은 margin, 반복 item 사이는 gap을 우선 고려한다.

Q. 카드 내부 여백은 뭐를 써?
A. padding을 사용한다.

Q. 카드 목록 사이 간격은 뭐를 써?
A. Grid 또는 Flex container의 gap을 사용하는 것이 좋다.

Q. section 사이 간격은 어떻게 처리해?
A. section padding-block이나 layout wrapper margin을 사용할 수 있다.

---

# 11. CSS Units for Typography and Spacing

## 11.1 rem em px percent

### [개념]

CSS Unit은 크기와 간격을 표현하는 단위다.

Typography와 Spacing에서는 `rem`, `em`, `px`, `%`를 자주 사용한다.

---

### [핵심]

`rem` 핵심:

- root font-size 기준
- typography scale과 spacing token에 적합
- 사용자 설정과 확장성에 유리

`em` 핵심:

- 현재 요소 또는 부모 font-size 기준
- component 내부 상대 크기에 유용
- 중첩 시 계산이 복잡할 수 있음

`px` 핵심:

- 고정 pixel 단위
- border, icon size, fine tuning에 적합
- 반응형 확장성은 낮을 수 있음

`%` 핵심:

- 부모 또는 기준 요소 대비 비율
- width와 layout에 자주 사용
- property에 따라 기준이 다름

---

### [실무]

선택 기준:

```text
Font Size Scale → rem
Spacing Token → rem
Border Width → px
Icon Size → px or rem
Fluid Width → %
Component relative padding → em 가능
```

예:

```css
:root {
  --space-4: 1rem;
}

.button {
  font-size: 1rem;
  padding: 0.75em 1em;
  border: 1px solid currentColor;
}
```

검수 기준:

- font-size와 spacing이 rem 기반 scale인가?
- border와 미세한 선은 px가 적절한가?
- em 중첩으로 예측하기 어려운 크기가 되지 않았는가?
- % 기준이 어떤 부모인지 이해했는가?

---

### [FAQ]

Q. rem은 뭐야?
A. root font-size를 기준으로 하는 CSS 단위다.

Q. em은 뭐야?
A. 현재 요소 또는 부모 font-size를 기준으로 하는 CSS 단위다.

Q. px는 언제 써?
A. border, icon, 미세한 크기 조정처럼 고정 값이 필요한 경우에 사용한다.

Q. spacing에는 어떤 단위가 좋아?
A. 일반적으로 rem 기반 spacing scale이 유지보수에 유리하다.

---

## 11.2 clamp min max

### [개념]

`clamp()`, `min()`, `max()`는 CSS에서 유동적인 크기 계산을 할 수 있는 함수다.

Responsive Typography, Container Width, Fluid Spacing에 유용하다.

---

### [핵심]

`clamp()` 핵심:

- 최소값, 선호값, 최대값을 지정한다.
- `clamp(min, preferred, max)` 구조다.
- Responsive font-size에 자주 사용한다.

`min()` 핵심:

- 여러 값 중 더 작은 값을 선택한다.
- container width 제한에 유용하다.

`max()` 핵심:

- 여러 값 중 더 큰 값을 선택한다.
- 최소 여백이나 안전 영역 처리에 사용할 수 있다.

예:

```css
.title {
  font-size: clamp(2rem, 5vw, 4rem);
}

.container {
  width: min(100% - 32px, 1200px);
}
```

---

### [실무]

Fluid Typography 예:

```css
.hero-title {
  font-size: clamp(2.25rem, 6vw, 5rem);
  line-height: 1;
}
```

Fluid Spacing 예:

```css
.section {
  padding-block: clamp(3rem, 8vw, 6rem);
}
```

Container 예:

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

검수 기준:

- 최소값과 최대값이 실제 UI에 적절한가?
- viewport 기준 값이 너무 빠르게 커지지 않는가?
- 작은 화면에서 spacing이 과도하지 않은가?
- clamp로 readability가 유지되는가?

---

### [FAQ]

Q. clamp()는 뭐야?
A. 최소값, 선호값, 최대값 사이에서 유동적인 값을 선택하는 CSS 함수다.

Q. clamp()는 언제 써?
A. 반응형 font-size나 spacing을 자연스럽게 조정할 때 사용한다.

Q. min()은 언제 써?
A. 여러 값 중 작은 값을 선택해야 할 때 사용하며 container width에 자주 사용한다.

Q. max()는 언제 써?
A. 여러 값 중 큰 값을 선택해야 할 때 사용한다.

---

# 12. Typography Color Spacing Debugging

## 12.1 Readability Debug

### [개념]

Readability Debug는 텍스트가 읽기 어렵거나 UI 계층이 불명확한 문제를 분석하는 과정이다.

Typography, Color, Spacing은 함께 검수해야 한다.

---

### [핵심]

Readability 문제 원인:

- font-size가 너무 작음
- line-height가 너무 좁음
- text contrast가 낮음
- heading과 body 차이가 불명확함
- 본문 줄 길이가 너무 김
- spacing이 부족해 콘텐츠가 붙어 보임
- 링크가 링크처럼 보이지 않음
- error text가 눈에 띄지 않음
- mobile viewport에서 글자와 버튼이 작음
- 장식 font로 긴 본문 작성

---

### [실무]

Debug Flow:

```text
Text Role 확인
→ font-size 확인
→ line-height 확인
→ font-weight 확인
→ color contrast 확인
→ line length 확인
→ spacing 확인
→ mobile viewport 확인
→ state text 확인
```

문제 예:

```text
문제: 본문이 읽기 어려움
원인: font-size 12px + line-height 1.1
해결: font-size와 line-height를 본문 기준으로 조정
```

```text
문제: 링크인지 알기 어려움
원인: 색상만 다르고 underline 없음
해결: underline 또는 명확한 link style 제공
```

```text
문제: Card들이 답답하게 보임
원인: padding과 gap 부족
해결: spacing scale 기준으로 card padding과 list gap 조정
```

검수 기준:

- 읽기 어려운 원인이 크기인지 contrast인지 spacing인지 분리했는가?
- heading hierarchy가 semantic heading과 시각적으로 일치하는가?
- mobile에서 실제 읽기 쉬운가?
- hover/focus/error 상태의 contrast가 유지되는가?

---

### [FAQ]

Q. 글자가 읽기 어려울 때 무엇을 확인해?
A. font-size, line-height, contrast, 줄 길이, spacing을 확인한다.

Q. 링크가 잘 안 보이면 어떻게 해?
A. 색상뿐 아니라 underline, hover, focus style을 함께 제공한다.

Q. UI가 답답해 보이면 무엇을 확인해?
A. padding, gap, line-height, section spacing을 확인한다.

Q. Typography 문제는 Color와 Spacing도 같이 봐야 해?
A. 그렇다. 가독성은 글자 크기만 아니라 contrast와 여백의 영향을 함께 받는다.

---

# 13. Comparison Rules

## 13.1 font-size vs line-height

### [개념]

`font-size`는 글자 크기이고 `line-height`는 줄 높이와 줄 간격이다.

두 속성은 함께 조정해야 읽기 좋은 텍스트가 된다.

---

### [핵심]

| 비교      | font-size               | line-height         |
| --------- | ----------------------- | ------------------- |
| 역할      | 글자 크기               | 줄 높이             |
| 영향      | 정보 계층, 가독성       | 줄 간격, 가독성     |
| 단위      | rem, px, em, clamp      | 단위 없는 숫자 권장 |
| 본문 기준 | 너무 작으면 읽기 어려움 | 너무 좁으면 답답함  |
| 제목 기준 | 계층 표현               | 타이트하게 가능     |

---

### [실무]

선택 기준:

```text
본문이 작음 → font-size 조정
줄이 답답함 → line-height 조정
제목이 너무 퍼짐 → heading line-height 조정
모바일 글자 작음 → responsive font-size 검토
```

---

### [FAQ]

Q. font-size와 line-height 차이는 뭐야?
A. font-size는 글자 크기이고 line-height는 줄 높이다.

Q. 본문 가독성에는 무엇이 더 중요해?
A. 둘 다 중요하다. 글자 크기와 줄 높이를 함께 조정해야 한다.

---

## 13.2 color vs background-color

### [개념]

`color`는 텍스트 색상이고 `background-color`는 요소의 배경 색상이다.

두 속성은 contrast 관점에서 함께 검토해야 한다.

---

### [핵심]

| 비교      | color                  | background-color      |
| --------- | ---------------------- | --------------------- |
| 역할      | 텍스트 색상            | 배경 색상             |
| 적용 대상 | 텍스트 / currentColor  | 요소 배경             |
| 접근성    | 배경과 대비 필요       | 텍스트와 대비 필요    |
| 사용 예   | body text, link, error | card, button, section |
| 주의      | 너무 옅은 텍스트       | 대비 부족 배경        |

---

### [실무]

검수 기준:

```text
Text Color 변경 → Background와 contrast 확인
Background 변경 → Text Color 재확인
Button Background 변경 → Button Text contrast 확인
Error Color 사용 → 메시지와 아이콘 함께 제공
```

---

### [FAQ]

Q. color와 background-color 차이는 뭐야?
A. color는 텍스트 색상이고 background-color는 배경 색상이다.

Q. 둘을 왜 같이 확인해야 해?
A. 텍스트와 배경의 contrast가 충분해야 읽기 쉽고 접근성이 좋아지기 때문이다.

---

## 13.3 margin vs padding vs gap

### [개념]

Margin, Padding, Gap은 모두 여백을 만들지만 목적과 적용 위치가 다르다.

---

### [핵심]

| 비교      | margin       | padding          | gap                 |
| --------- | ------------ | ---------------- | ------------------- |
| 위치      | 요소 외부    | 요소 내부        | Flex/Grid item 사이 |
| 책임      | 외부 배치    | 내부 공간        | 반복 간격           |
| 배경 포함 | 포함 안 됨   | 포함             | 해당 없음           |
| collapse  | 가능         | 없음             | 없음                |
| 대표 사용 | section 간격 | card/button 내부 | list/card 간격      |

---

### [실무]

선택 기준:

```text
Card 내부 → padding
Button 클릭 영역 → padding
Card 목록 사이 → gap
Section 사이 → padding-block or margin
특정 요소만 분리 → margin
```

---

### [FAQ]

Q. margin padding gap 차이는 뭐야?
A. margin은 외부 여백, padding은 내부 여백, gap은 Flex/Grid item 사이 간격이다.

Q. 반복 목록 간격은 무엇이 좋아?
A. Flexbox나 Grid에서는 gap이 적절한 경우가 많다.

---

## 13.4 rem vs em vs px

### [개념]

`rem`, `em`, `px`는 크기와 간격을 지정하는 CSS 단위다.

각 단위는 기준이 다르므로 목적에 맞게 사용해야 한다.

---

### [핵심]

| 비교 | rem                 | em                  | px                 |
| ---- | ------------------- | ------------------- | ------------------ |
| 기준 | root font-size      | 현재/부모 font-size | 고정 pixel         |
| 적합 | font scale, spacing | component 상대 크기 | border, icon       |
| 장점 | 일관성, 확장성      | 상대적 유연성       | 정확한 제어        |
| 주의 | root 기준 이해 필요 | 중첩 계산 복잡      | 반응형 유연성 낮음 |

---

### [실무]

선택 기준:

```text
Typography Scale → rem
Spacing Token → rem
Button padding relative to text → em 가능
Border 1px → px
Icon size → px or rem
```

---

### [FAQ]

Q. rem과 em 차이는 뭐야?
A. rem은 root font-size 기준이고 em은 현재 요소 또는 부모 font-size 기준이다.

Q. px는 쓰면 안 돼?
A. 아니다. border, icon, 세밀한 크기 제어에는 px가 적합할 수 있다.

---

# 14. Common Mistakes

## 14.1 Typography Color Spacing Common Mistakes

### [개념]

Typography, Color, Spacing 실수는 UI 가독성 저하, 접근성 문제, 디자인 일관성 저하, 유지보수 어려움으로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- 본문 font-size가 너무 작음
- line-height가 너무 좁음
- heading hierarchy가 시각적으로 불명확함
- 제목을 크기만 키우고 line-height를 조정하지 않음
- px 고정값만으로 typography 구성
- 너무 많은 font-size와 font-weight 사용
- Web Font fallback 누락
- code text에 monospace 미사용
- 긴 본문 line length 제한 없음
- 링크 underline 제거 후 대체 표시 없음
- 색상만으로 error / success 전달
- 텍스트와 배경 contrast 부족
- disabled text를 너무 흐리게 처리
- placeholder가 너무 옅음
- 임의 hex 값이 Component마다 흩어짐
- semantic color token 없이 색상 관리
- margin / padding / gap 역할 혼동
- 무작위 spacing 값 남용
- Component 외부 margin 과다
- 모바일에서 spacing과 touch target 부족
- 긴 텍스트 overflow 미처리

---

### [실무]

Troubleshooting Flow:

```text
UI Readability Issue
→ font-size 확인
→ line-height 확인
→ font-weight 확인
→ contrast 확인
→ text wrapping 확인
→ spacing 확인
→ responsive viewport 확인
→ token 사용 여부 확인
```

문제 예:

```text
문제: Error 상태가 색약 사용자에게 구분되지 않음
원인: border 색상만 변경
해결: error message, icon, aria-invalid 함께 제공
```

```text
문제: 카드 UI가 일관되지 않음
원인: padding과 gap이 임의 값으로 흩어짐
해결: spacing token 기준으로 통일
```

```text
문제: 본문이 큰 화면에서 읽기 어려움
원인: line length 제한 없음
해결: prose container에 max-width 적용
```

---

### [FAQ]

Q. Typography에서 가장 흔한 실수는 뭐야?
A. font-size만 조정하고 line-height, contrast, 줄 길이를 함께 보지 않는 것이다.

Q. Color에서 가장 흔한 실수는 뭐야?
A. 색상만으로 상태를 전달하거나 contrast가 부족한 색을 사용하는 것이다.

Q. Spacing에서 가장 흔한 실수는 뭐야?
A. margin, padding, gap 역할을 혼동하고 무작위 여백 값을 사용하는 것이다.

Q. Typography Color Spacing 문제는 어떤 순서로 디버깅해?
A. font-size, line-height, contrast, text wrapping, spacing, responsive viewport 순서로 확인한다.

---

# 15. Best Practice

## 15.1 Typography Color Spacing Best Practice

### [개념]

Typography Color Spacing Best Practice는 텍스트 가독성, 색상 접근성, 여백 일관성, Component 유지보수성을 높이는 작성 기준이다.

---

### [핵심]

권장 기준:

- Typography scale을 정의한다.
- 본문은 읽기 쉬운 font-size와 line-height를 사용한다.
- Heading hierarchy와 시각 hierarchy를 일치시킨다.
- font-family fallback을 제공한다.
- code text에는 monospace를 사용한다.
- 긴 본문에는 max-width를 적용한다.
- 링크는 색상 외에도 underline 등 식별 단서를 제공한다.
- semantic color token을 사용한다.
- 텍스트와 배경 contrast를 확인한다.
- error / success 상태는 색상만으로 전달하지 않는다.
- spacing scale을 정의한다.
- 내부 여백은 padding, 반복 간격은 gap, 외부 간격은 margin으로 구분한다.
- Component 외부 margin 책임을 최소화한다.
- rem 기반 scale을 우선 고려한다.
- responsive font-size와 spacing에는 clamp를 고려한다.

---

### [실무]

기본 Token 예:

```css
:root {
  --font-sans:
    system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", monospace;

  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;

  --leading-tight: 1.1;
  --leading-normal: 1.5;
  --leading-relaxed: 1.7;

  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-border: #e5e7eb;
  --color-primary: #2563eb;
  --color-danger: #dc2626;

  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
}
```

Base Style 예:

```css
body {
  margin: 0;
  font-family: var(--font-sans);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text);
  background-color: var(--color-background);
}

.prose {
  max-width: 65ch;
}

.prose h1 {
  font-size: clamp(2rem, 4vw, 3.5rem);
  line-height: var(--leading-tight);
}

.prose p {
  line-height: var(--leading-relaxed);
}
```

Component 예:

```css
.card {
  padding: var(--space-6);
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
}

.card-title {
  margin: 0;
  font-size: var(--text-xl);
  line-height: var(--leading-tight);
}

.card-description {
  margin-block-start: var(--space-2);
  color: var(--color-text-muted);
  overflow-wrap: break-word;
}

.card-list {
  display: grid;
  gap: var(--space-6);
}
```

검수 Checklist:

```md
- [ ] font-family fallback이 있는가?
- [ ] 본문 font-size와 line-height가 읽기 쉬운가?
- [ ] heading hierarchy가 명확한가?
- [ ] typography scale이 일관적인가?
- [ ] code에는 monospace가 적용되었는가?
- [ ] 긴 본문 max-width가 있는가?
- [ ] 긴 텍스트 overflow 처리가 있는가?
- [ ] 링크가 색상 외에도 식별 가능한가?
- [ ] semantic color token을 사용하는가?
- [ ] 텍스트와 배경 contrast가 충분한가?
- [ ] error 상태를 색상만으로 전달하지 않는가?
- [ ] spacing scale을 사용하는가?
- [ ] padding, margin, gap 역할이 구분되어 있는가?
- [ ] 모바일에서 touch target과 spacing이 충분한가?
```

---

### [FAQ]

Q. Typography Color Spacing Best Practice는 뭐야?
A. Typography scale, semantic color token, spacing scale을 사용해 가독성과 접근성, 유지보수성을 높이는 것이다.

Q. Typography 검수에서 가장 먼저 볼 것은 뭐야?
A. font-size, line-height, heading hierarchy, contrast, line length를 먼저 확인한다.

Q. Color 검수에서 가장 먼저 볼 것은 뭐야?
A. 텍스트와 배경 contrast, 색상만으로 상태를 전달하는지 여부를 확인한다.

Q. Spacing 검수에서 가장 먼저 볼 것은 뭐야?
A. padding, margin, gap 역할 구분과 spacing scale 사용 여부를 확인한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 읽기 쉽고 접근성 있는 Typography, Color, Spacing 스타일을 일관되게 생성하고 검토하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Typography가 뭐야?
A. 웹 텍스트의 글꼴, 크기, 굵기, 줄 높이, 간격, 계층 구조를 설계하는 CSS 영역이다.

Q. Typography는 왜 중요해?
A. 콘텐츠 가독성, 정보 계층, 접근성, 브랜드 일관성에 직접 영향을 주기 때문이다.

Q. 글자 크기만 맞추면 Typography가 끝이야?
A. 아니다. line-height, font-weight, contrast, spacing, responsive scale까지 함께 고려해야 한다.

Q. font-family는 뭐야?
A. 텍스트에 사용할 글꼴 후보 목록을 지정하는 CSS property다.

Q. font-family에 여러 글꼴을 쓰는 이유는?
A. 앞 글꼴을 사용할 수 없을 때 다음 글꼴로 fallback하기 위해서다.

Q. code에는 어떤 font-family가 좋아?
A. `monospace` 계열 글꼴이 적합하다.

Q. font-size는 뭐야?
A. 텍스트의 글자 크기를 지정하는 CSS property다.

Q. rem과 px 중 뭐가 좋아?
A. 일반적으로 rem은 사용자 설정과 확장성에 더 유리하고 px는 고정 크기에 적합하다.

Q. clamp()는 font-size에 왜 써?
A. 최소값과 최대값 사이에서 viewport에 따라 자연스럽게 변하는 글자 크기를 만들 수 있기 때문이다.

Q. font-weight는 뭐야?
A. 텍스트의 굵기를 지정하는 CSS property다.

Q. bold와 700은 같아?
A. 일반적으로 bold는 700에 대응된다.

Q. font-weight 500을 줬는데 차이가 없는 이유는?
A. 사용 중인 font가 해당 weight를 지원하지 않거나 브라우저가 대체 렌더링하기 때문일 수 있다.

Q. line-height는 뭐야?
A. 텍스트 줄의 높이와 줄 간격을 지정하는 CSS property다.

Q. 본문 line-height는 어느 정도가 좋아?
A. 보통 1.4에서 1.7 사이가 읽기 쉬운 경우가 많다.

Q. 단위 없는 line-height가 좋은 이유는?
A. font-size 변화에 따라 자연스럽게 비례하고 상속 관리가 쉬워지기 때문이다.

Q. text-align은 뭐야?
A. inline content의 가로 정렬을 지정하는 CSS property다.

Q. div 자체를 가운데 두려면 text-align center를 쓰면 돼?
A. 아니다. block 자체 정렬은 margin, Flexbox, Grid를 사용한다.

Q. 긴 본문도 center 정렬하면 좋아?
A. 일반적으로 읽기 어렵다. 긴 본문은 start 또는 left 정렬이 좋다.

Q. text-decoration은 뭐야?
A. 텍스트에 밑줄, 취소선, 윗줄 같은 장식을 지정하는 property다.

Q. 링크 밑줄을 없애도 돼?
A. 가능하지만 링크임을 알 수 있는 다른 시각적 단서가 필요하다.

Q. 색상만으로 링크를 표시해도 돼?
A. 권장하지 않는다. 접근성을 위해 underline 등 추가 단서를 제공하는 것이 좋다.

Q. 긴 텍스트가 박스 밖으로 나가면 어떻게 해?
A. `overflow-wrap: break-word` 또는 `overflow-wrap: anywhere`를 검토한다.

Q. text-overflow ellipsis는 언제 써?
A. 한 줄 또는 제한된 영역에서 텍스트를 말줄임으로 표시할 때 사용한다.

Q. ellipsis만 주면 말줄임이 돼?
A. 아니다. 보통 `overflow: hidden`, `white-space: nowrap`, `text-overflow: ellipsis`가 함께 필요하다.

Q. CSS color는 뭐야?
A. 텍스트, 배경, 테두리, 상태, 브랜드 표현에 사용하는 색상 관련 CSS 영역이다.

Q. color와 background-color 차이는 뭐야?
A. color는 텍스트 색상이고 background-color는 배경 색상이다.

Q. 색상만으로 에러를 표시해도 돼?
A. 안 된다. 에러 메시지, 아이콘, aria-invalid 같은 추가 정보가 필요하다.

Q. Semantic Color Token은 왜 필요해?
A. 색상을 역할 기준으로 관리해 유지보수와 theme 대응을 쉽게 하기 위해 필요하다.

Q. CSS 색상은 어떤 형식으로 쓸 수 있어?
A. hex, rgb, rgba, hsl, oklch, currentColor, transparent 등을 사용할 수 있다.

Q. currentColor는 뭐야?
A. 현재 요소의 `color` 값을 재사용하는 CSS 키워드다.

Q. Contrast가 뭐야?
A. 텍스트와 배경 또는 UI 요소 간의 명도 차이다.

Q. Contrast는 왜 중요해?
A. 낮은 contrast는 텍스트를 읽기 어렵게 만들고 접근성 문제를 만든다.

Q. placeholder 색상은 옅게 해도 돼?
A. 가능하지만 너무 옅으면 입력 힌트를 읽기 어려워진다.

Q. background-color는 뭐야?
A. 요소의 배경 색상을 지정하는 CSS property다.

Q. background-color는 margin 영역에도 적용돼?
A. 아니다. margin 영역에는 배경이 적용되지 않는다.

Q. background-image는 언제 써?
A. 장식 배경, hero 배경, gradient overlay처럼 콘텐츠 의미보다 시각 배경 목적일 때 사용한다.

Q. 의미 있는 이미지를 background-image로 넣어도 돼?
A. 권장하지 않는다. 의미 있는 이미지는 img와 alt를 사용하는 것이 좋다.

Q. Spacing이 뭐야?
A. UI 요소의 내부 여백과 외부 간격을 설계하는 기준이다.

Q. padding과 margin 차이는 뭐야?
A. padding은 내부 여백이고 margin은 외부 여백이다.

Q. gap은 언제 써?
A. Flexbox나 Grid의 반복 Item 사이 간격을 관리할 때 사용한다.

Q. Spacing scale은 왜 필요해?
A. 무작위 여백 값을 줄이고 UI 일관성과 유지보수성을 높이기 위해 필요하다.

Q. margin padding gap은 어떻게 구분해?
A. 내부 여백은 padding, 외부 간격은 margin, 반복 item 사이는 gap을 우선 고려한다.

Q. rem은 뭐야?
A. root font-size를 기준으로 하는 CSS 단위다.

Q. em은 뭐야?
A. 현재 요소 또는 부모 font-size를 기준으로 하는 CSS 단위다.

Q. px는 언제 써?
A. border, icon, 미세한 크기 조정처럼 고정 값이 필요한 경우에 사용한다.

Q. spacing에는 어떤 단위가 좋아?
A. 일반적으로 rem 기반 spacing scale이 유지보수에 유리하다.

Q. clamp()는 뭐야?
A. 최소값, 선호값, 최대값 사이에서 유동적인 값을 선택하는 CSS 함수다.

Q. clamp()는 언제 써?
A. 반응형 font-size나 spacing을 자연스럽게 조정할 때 사용한다.

Q. min()은 언제 써?
A. 여러 값 중 작은 값을 선택해야 할 때 사용하며 container width에 자주 사용한다.

Q. 글자가 읽기 어려울 때 무엇을 확인해?
A. font-size, line-height, contrast, 줄 길이, spacing을 확인한다.

Q. 링크가 잘 안 보이면 어떻게 해?
A. 색상뿐 아니라 underline, hover, focus style을 함께 제공한다.

Q. UI가 답답해 보이면 무엇을 확인해?
A. padding, gap, line-height, section spacing을 확인한다.

Q. font-size와 line-height 차이는 뭐야?
A. font-size는 글자 크기이고 line-height는 줄 높이다.

Q. color와 background-color 차이는 뭐야?
A. color는 텍스트 색상이고 background-color는 배경 색상이다.

Q. margin padding gap 차이는 뭐야?
A. margin은 외부 여백, padding은 내부 여백, gap은 Flex/Grid item 사이 간격이다.

Q. rem과 em 차이는 뭐야?
A. rem은 root font-size 기준이고 em은 현재 요소 또는 부모 font-size 기준이다.

Q. Typography에서 가장 흔한 실수는 뭐야?
A. font-size만 조정하고 line-height, contrast, 줄 길이를 함께 보지 않는 것이다.

Q. Color에서 가장 흔한 실수는 뭐야?
A. 색상만으로 상태를 전달하거나 contrast가 부족한 색을 사용하는 것이다.

Q. Spacing에서 가장 흔한 실수는 뭐야?
A. margin, padding, gap 역할을 혼동하고 무작위 여백 값을 사용하는 것이다.

Q. Typography Color Spacing Best Practice는 뭐야?
A. Typography scale, semantic color token, spacing scale을 사용해 가독성과 접근성, 유지보수성을 높이는 것이다.

Q. Typography 검수에서 가장 먼저 볼 것은 뭐야?
A. font-size, line-height, heading hierarchy, contrast, line length를 먼저 확인한다.

Q. Color 검수에서 가장 먼저 볼 것은 뭐야?
A. 텍스트와 배경 contrast, 색상만으로 상태를 전달하는지 여부를 확인한다.

Q. Spacing 검수에서 가장 먼저 볼 것은 뭐야?
A. padding, margin, gap 역할 구분과 spacing scale 사용 여부를 확인한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 읽기 쉽고 접근성 있는 Typography, Color, Spacing 스타일을 일관되게 생성하고 검토하게 만드는 것이다.
