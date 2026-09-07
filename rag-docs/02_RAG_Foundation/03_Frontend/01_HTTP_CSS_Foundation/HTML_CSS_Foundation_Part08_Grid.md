# HTML CSS Foundation Part08 - Grid

---

# 1. CSS Grid

## 1.1 Grid Concept

### [개념]

CSS Grid는 행(row)과 열(column)을 기준으로 2차원 Layout을 구현하는 CSS Layout 방식이다.

Grid는 가로와 세로 배치를 동시에 제어할 수 있다.

기본 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

CSS Grid는 Card List, Gallery, Dashboard, Page Layout, Product List, Admin Layout, Form Layout에 자주 사용된다.

---

### [핵심]

Grid 핵심:

- `display: grid`로 Grid Formatting Context를 만든다.
- Grid Container는 부모 요소다.
- Grid Item은 Grid Container의 직접 자식 요소다.
- `grid-template-columns`는 열 구조를 정의한다.
- `grid-template-rows`는 행 구조를 정의한다.
- `gap`은 Grid Item 사이 간격을 만든다.
- `fr`은 Grid 남은 공간 비율 단위다.
- `repeat()`는 반복 Track을 만든다.
- `minmax()`는 Track의 최소 / 최대 크기를 지정한다.
- `auto-fit`, `auto-fill`은 반응형 Column 구성에 유용하다.
- Grid는 2차원 Layout에 적합하다.

---

### [실무]

2026 실무 기준에서 CSS Grid는 화면 구조와 반복 카드 배치를 안정적으로 만드는 핵심 Layout 도구다.

Frontend Agent는 Grid를 사용해 아래 UI를 구현해야 한다.

- Card Grid
- Festival List Grid
- Gallery
- Dashboard Layout
- Admin Data Summary
- Page Layout
- Sidebar + Main Layout
- Responsive Product List
- Form Field Grid
- Feature Section

Grid 작성 Flow:

```text
Grid Container 선택
→ display grid
→ columns 정의
→ rows 필요 여부 확인
→ gap 설정
→ item placement 확인
→ responsive column 전략 선택
→ mobile viewport 확인
```

---

### [FAQ]

Q. CSS Grid가 뭐야?
A. 행과 열을 기준으로 요소를 배치하는 CSS 2차원 Layout 방식이다.

Q. Grid는 언제 써?
A. 카드 목록, 갤러리, 대시보드, 페이지 레이아웃처럼 행과 열이 모두 중요한 UI에 사용한다.

Q. Grid는 2차원 Layout이야?
A. 맞다. row와 column을 함께 제어하는 Layout에 적합하다.

Q. Flexbox와 Grid 중 뭐를 써야 해?
A. 한 방향 정렬은 Flexbox, 행과 열이 모두 중요한 2차원 배치는 Grid가 적합하다.

---

# 2. Grid Container and Grid Item

## 2.1 Grid Container

### [개념]

Grid Container는 `display: grid` 또는 `display: inline-grid`가 적용된 부모 요소다.

Grid Container는 직접 자식 요소들을 Grid Item으로 배치한다.

예:

```html
<ul class="festival-grid">
  <li>Festival Card</li>
  <li>Festival Card</li>
  <li>Festival Card</li>
</ul>
```

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

---

### [핵심]

Grid Container 핵심:

- `display: grid`가 적용된 부모 요소다.
- 직접 자식 요소만 Grid Item이 된다.
- 손자 요소는 직접 Grid Item이 아니다.
- Grid Track은 row와 column으로 구성된다.
- `grid-template-columns`로 열 구조를 만든다.
- `grid-template-rows`로 행 구조를 만들 수 있다.
- `gap`으로 Item 사이 간격을 관리한다.
- Container 기준으로 Layout을 설계한다.

---

### [실무]

Grid Container는 반복 목록 또는 2차원 Layout의 부모에 적용한다.

좋은 예:

```css
.festival-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

나쁜 예:

```css
.festival-card {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

위 예는 카드 내부 구조에는 의미가 있을 수 있지만, 카드 목록 전체 배치에는 부족하다.

검수 기준:

- 배치하려는 Item의 부모에 `display: grid`를 적용했는가?
- Grid Item이 직접 자식인가?
- 손자 요소를 Grid Item처럼 착각하지 않았는가?
- Container가 columns, rows, gap을 책임지는가?
- List UI라면 `ul` / `li` 구조와 함께 사용할 수 있는가?

---

### [FAQ]

Q. Grid Container가 뭐야?
A. `display: grid`가 적용되어 자식 요소를 Grid Item으로 배치하는 부모 요소다.

Q. Grid Item은 어떤 요소야?
A. Grid Container의 직접 자식 요소다.

Q. 손자 요소도 Grid Item이 돼?
A. 아니다. Grid Container의 직접 자식만 Grid Item이 된다.

Q. 카드 목록을 Grid로 만들려면 어디에 display grid를 줘?
A. 카드들을 감싸는 부모 목록 또는 Container에 `display: grid`를 준다.

---

## 2.2 Grid Item

### [개념]

Grid Item은 Grid Container의 직접 자식 요소다.

Grid Item은 Grid Track, Grid Line, Grid Area 기준으로 배치될 수 있다.

---

### [핵심]

Grid Item 핵심:

- Grid Container의 직접 자식이다.
- 기본적으로 자동 배치된다.
- `grid-column`으로 column 위치나 span을 지정할 수 있다.
- `grid-row`로 row 위치나 span을 지정할 수 있다.
- `justify-self`로 개별 inline axis 정렬을 제어할 수 있다.
- `align-self`로 개별 block axis 정렬을 제어할 수 있다.
- Grid Item도 `min-width: auto` 때문에 overflow가 발생할 수 있다.
- 긴 텍스트가 있는 Grid Item에는 `min-width: 0`이 필요할 수 있다.

---

### [실무]

Grid Item 예:

```html
<section class="dashboard-grid">
  <article class="summary-card">Summary</article>
  <article class="summary-card">Chart</article>
  <article class="summary-card featured">Featured</article>
</section>
```

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.featured {
  grid-column: span 2;
}
```

검수 기준:

- Grid Item이 직접 자식인가?
- 특정 Item만 span이 필요한가?
- `grid-column: span 2`가 작은 화면에서 문제를 만들지 않는가?
- 긴 텍스트 Item에 `min-width: 0`이 필요한가?
- Item placement가 DOM 순서와 지나치게 어긋나지 않는가?

---

### [FAQ]

Q. Grid Item이 뭐야?
A. Grid Container의 직접 자식 요소다.

Q. Grid Item을 두 칸 차지하게 하려면?
A. `grid-column: span 2` 같은 속성을 사용할 수 있다.

Q. Grid Item이 부모 밖으로 나가는 이유는?
A. 고정 width, 긴 텍스트, 기본 min-width, 큰 이미지 때문에 줄어들지 못하기 때문일 수 있다.

Q. Grid Item에도 min-width 0이 필요해?
A. 긴 텍스트나 overflow가 있는 경우 필요할 수 있다.

---

# 3. Grid Track and Line

## 3.1 Grid Track

### [개념]

Grid Track은 Grid의 행 또는 열 하나를 의미한다.

Column Track은 열이고 Row Track은 행이다.

예:

```css
.grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  grid-template-rows: auto auto;
}
```

---

### [핵심]

Grid Track 핵심:

- Column Track은 세로 열이다.
- Row Track은 가로 행이다.
- `grid-template-columns`는 column track을 정의한다.
- `grid-template-rows`는 row track을 정의한다.
- Track 크기는 `px`, `%`, `rem`, `fr`, `auto`, `minmax()` 등으로 지정할 수 있다.
- `fr`은 남은 공간 비율을 나타낸다.
- 대부분의 카드 목록은 column track 정의만으로 충분하다.

---

### [실무]

Card Grid 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

Page Layout 예:

```css
.page-layout {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 32px;
}
```

검수 기준:

- column track 개수가 UI 목적과 맞는가?
- row track을 명시해야 하는 Layout인가?
- 고정 px track이 모바일 overflow를 만들지 않는가?
- `fr` 단위를 사용해 남은 공간을 유연하게 분배했는가?
- `minmax()`가 필요한 반응형 Grid인가?

---

### [FAQ]

Q. Grid Track이 뭐야?
A. Grid의 행 또는 열 하나를 의미한다.

Q. grid-template-columns는 뭐야?
A. Grid의 열 track 구조를 정의하는 property다.

Q. grid-template-rows는 언제 써?
A. 행 높이 구조를 명확히 정의해야 할 때 사용한다.

Q. fr 단위는 뭐야?
A. Grid Container의 남은 공간을 비율로 나누는 단위다.

---

## 3.2 Grid Line

### [개념]

Grid Line은 Grid Track을 나누는 경계선이다.

Grid Item은 Grid Line 번호를 기준으로 배치할 수 있다.

---

### [핵심]

Grid Line 핵심:

- Column Line은 열 경계선이다.
- Row Line은 행 경계선이다.
- Grid Line 번호는 1부터 시작한다.
- `grid-column: 1 / 3`은 column line 1부터 3까지 차지한다.
- `grid-row: 1 / 2`는 row line 1부터 2까지 차지한다.
- `span`을 사용하면 몇 칸을 차지할지 지정할 수 있다.
- 복잡한 Line 배치는 유지보수성을 낮출 수 있다.

예:

```css
.feature-card {
  grid-column: 1 / 3;
}
```

---

### [실무]

Line 기반 배치는 Dashboard나 특정 강조 카드에서 사용할 수 있다.

예:

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.large-card {
  grid-column: span 2;
  grid-row: span 2;
}
```

검수 기준:

- Line 번호가 실제 Track 구조와 일치하는가?
- 특정 화면 크기에서 Line 배치가 깨지지 않는가?
- 복잡한 Line 번호보다 `grid-template-areas`가 더 명확하지 않은가?
- Item 배치가 DOM 순서와 접근성 흐름을 과도하게 바꾸지 않는가?

---

### [FAQ]

Q. Grid Line이 뭐야?
A. Grid Track을 나누는 경계선이다.

Q. grid-column 1 / 3은 무슨 뜻이야?
A. column line 1부터 3까지 차지한다는 뜻이다.

Q. span은 무슨 뜻이야?
A. Grid Item이 몇 개의 Track을 차지할지 지정하는 방식이다.

Q. Grid Line 번호를 많이 쓰면 좋아?
A. 복잡해질 수 있으므로 반복 Layout에서는 auto placement나 area를 우선 고려한다.

---

# 4. Grid Template Columns

## 4.1 grid-template-columns

### [개념]

`grid-template-columns`는 Grid Container의 열 구조를 정의하는 CSS property다.

Grid Layout에서 가장 자주 사용하는 핵심 속성이다.

---

### [핵심]

`grid-template-columns` 핵심:

- Grid의 column track을 정의한다.
- 고정 크기, 비율, 자동 크기, minmax를 사용할 수 있다.
- `1fr`은 남은 공간 1비율이다.
- `repeat()`로 반복 column을 간결하게 작성한다.
- `minmax()`로 최소 / 최대 크기를 지정한다.
- `auto-fit`, `auto-fill`과 함께 반응형 Grid를 만들 수 있다.

예:

```css
.grid {
  grid-template-columns: 1fr 1fr 1fr;
}

.grid-repeat {
  grid-template-columns: repeat(3, 1fr);
}

.grid-responsive {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

---

### [실무]

Card List에서는 `repeat(auto-fit, minmax())` 패턴이 실용적이다.

예:

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

Page Layout 예:

```css
.page-layout {
  display: grid;
  grid-template-columns: minmax(220px, 280px) 1fr;
  gap: 32px;
}
```

검수 기준:

- column 개수가 화면 크기에 맞게 변하는가?
- 고정 column이 모바일 overflow를 만들지 않는가?
- Card 최소 너비가 너무 크지 않은가?
- `auto-fit`과 `minmax()`가 적절한가?
- Page Layout은 mobile에서 1 column으로 전환되는가?

---

### [FAQ]

Q. grid-template-columns는 뭐야?
A. Grid의 열 구조를 정의하는 CSS property다.

Q. repeat(3, 1fr)은 무슨 뜻이야?
A. 같은 너비의 열 3개를 만든다는 뜻이다.

Q. 반응형 카드 Grid는 어떻게 작성해?
A. `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));` 패턴을 사용할 수 있다.

Q. 1fr은 뭐야?
A. Grid Container의 남은 공간을 1비율로 차지하는 단위다.

---

# 5. Grid Template Rows

## 5.1 grid-template-rows

### [개념]

`grid-template-rows`는 Grid Container의 행 구조를 정의하는 CSS property다.

Column 중심 카드 목록에서는 생략하는 경우가 많지만, Dashboard나 명확한 행 높이가 필요한 Layout에서 사용한다.

---

### [핵심]

`grid-template-rows` 핵심:

- Grid의 row track을 정의한다.
- 행 높이를 `auto`, `px`, `fr`, `minmax()` 등으로 지정할 수 있다.
- 콘텐츠 높이에 맞춰 자동으로 row가 생성될 수도 있다.
- 명시적 row와 암시적 row를 구분해야 한다.
- `grid-auto-rows`와 함께 사용할 수 있다.
- 고정 row height는 콘텐츠 잘림을 만들 수 있다.

예:

```css
.dashboard {
  display: grid;
  grid-template-rows: auto 1fr auto;
}
```

---

### [실무]

Dashboard Layout 예:

```css
.dashboard-layout {
  display: grid;
  grid-template-rows: auto 1fr;
  min-height: 100dvh;
}

.dashboard-header {
  grid-row: 1;
}

.dashboard-main {
  grid-row: 2;
}
```

Card Row 높이 통일 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(180px, auto);
}
```

검수 기준:

- row 높이를 명시해야 하는 UI인가?
- 콘텐츠가 고정 row height 안에서 잘리지 않는가?
- `grid-auto-rows`가 더 적절하지 않은가?
- viewport height 기반 Layout에서 mobile browser height 문제를 고려했는가?

---

### [FAQ]

Q. grid-template-rows는 뭐야?
A. Grid의 행 구조를 정의하는 CSS property다.

Q. 카드 목록에도 grid-template-rows가 꼭 필요해?
A. 보통은 필요 없다. 콘텐츠에 따라 자동 row가 생성되는 경우가 많다.

Q. 고정 row height는 왜 조심해야 해?
A. 콘텐츠가 늘어나면 잘리거나 overflow가 발생할 수 있기 때문이다.

Q. grid-auto-rows는 언제 써?
A. 자동으로 생성되는 row의 기본 크기를 지정할 때 사용한다.

---

# 6. Gap

## 6.1 Grid Gap

### [개념]

`gap`은 Grid Item 사이의 row와 column 간격을 지정하는 CSS property다.

Grid에서는 `row-gap`, `column-gap`을 따로 지정할 수 있다.

---

### [핵심]

Grid Gap 핵심:

- Item 사이 간격을 Container에서 관리한다.
- `gap`은 row gap과 column gap을 함께 지정한다.
- `row-gap`은 행 간격이다.
- `column-gap`은 열 간격이다.
- margin보다 반복 Item 간격 관리가 명확하다.
- 첫 번째 / 마지막 Item 외부에 불필요한 margin이 생기지 않는다.

예:

```css
.grid {
  display: grid;
  gap: 24px;
}

.grid-separated {
  row-gap: 32px;
  column-gap: 16px;
}
```

---

### [실무]

Card Grid 예:

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

Form Grid 예:

```css
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px 24px;
}
```

검수 기준:

- Grid Item 사이 간격을 margin이 아니라 gap으로 관리했는가?
- row와 column 간격이 다르면 `row-gap`, `column-gap`을 사용했는가?
- 모바일에서 gap이 과도하지 않은가?
- gap 때문에 작은 화면에서 column이 너무 좁아지지 않는가?

---

### [FAQ]

Q. Grid gap은 뭐야?
A. Grid Item 사이의 행과 열 간격을 지정하는 property다.

Q. Grid에서도 gap을 써?
A. 쓴다. Grid Item 간격 관리에 가장 일반적으로 사용한다.

Q. gap과 margin 중 뭐가 좋아?
A. 반복 Grid Item 사이 간격은 gap이 더 명확하고 관리하기 쉽다.

Q. row-gap과 column-gap 차이는 뭐야?
A. row-gap은 행 간격이고 column-gap은 열 간격이다.

---

# 7. Repeat Minmax Auto Fit

## 7.1 repeat()

### [개념]

`repeat()`는 Grid Track 정의를 반복해서 작성하는 CSS 함수다.

반복되는 column 또는 row 정의를 간결하게 만든다.

예:

```css
.grid {
  grid-template-columns: repeat(3, 1fr);
}
```

---

### [핵심]

`repeat()` 핵심:

- 반복되는 Track 정의를 줄인다.
- `repeat(3, 1fr)`은 `1fr 1fr 1fr`과 같다.
- 고정 반복 수를 사용할 수 있다.
- `auto-fit`, `auto-fill`과 함께 동적 반복에 사용할 수 있다.
- Card Grid와 Gallery에서 자주 사용한다.

---

### [실무]

고정 3열 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

반응형 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

검수 기준:

- 같은 Track을 반복 작성하고 있지 않은가?
- 고정 반복 수가 모바일에서 overflow를 만들지 않는가?
- 반응형이면 auto-fit / auto-fill이 더 적절한가?

---

### [FAQ]

Q. repeat()는 뭐야?
A. Grid Track 정의를 반복해서 작성하는 CSS 함수다.

Q. repeat(3, 1fr)은 무슨 뜻이야?
A. 1fr 크기의 column을 3개 만든다는 뜻이다.

Q. repeat()는 반응형에도 쓸 수 있어?
A. 가능하다. `auto-fit` 또는 `auto-fill`과 함께 사용할 수 있다.

---

## 7.2 minmax()

### [개념]

`minmax()`는 Grid Track의 최소 크기와 최대 크기를 지정하는 CSS 함수다.

반응형 Grid에서 매우 자주 사용한다.

예:

```css
.grid {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

---

### [핵심]

`minmax()` 핵심:

- Track의 최소값과 최대값을 지정한다.
- `minmax(240px, 1fr)`은 최소 240px, 최대 1fr이다.
- Card가 너무 좁아지는 것을 막는다.
- Container가 넓으면 남은 공간을 분배한다.
- 최소값이 너무 크면 모바일 overflow가 발생할 수 있다.
- `minmax(0, 1fr)`은 overflow 방지에 사용할 수 있다.

---

### [실무]

Responsive Card Grid 예:

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

Overflow 방지 예:

```css
.layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 320px;
}
```

검수 기준:

- 최소값이 모바일 화면보다 크지 않은가?
- Card 최소 너비가 실제 콘텐츠에 적합한가?
- `minmax(0, 1fr)`로 overflow를 줄일 수 있는가?
- 고정 width보다 유연한 minmax가 적절하지 않은가?

---

### [FAQ]

Q. minmax()는 뭐야?
A. Grid Track의 최소 크기와 최대 크기를 지정하는 CSS 함수다.

Q. minmax(240px, 1fr)은 무슨 뜻이야?
A. Track이 최소 240px이고 가능한 경우 1fr까지 늘어난다는 뜻이다.

Q. minmax 최소값이 너무 크면 어떻게 돼?
A. 작은 화면에서 Grid가 overflow되어 가로 스크롤이 생길 수 있다.

Q. minmax(0, 1fr)은 언제 써?
A. Grid Item이 최소 크기 때문에 overflow되는 문제를 줄일 때 사용할 수 있다.

---

## 7.3 auto-fit and auto-fill

### [개념]

`auto-fit`과 `auto-fill`은 Grid가 가능한 Track 수를 자동으로 계산하도록 하는 반복 키워드다.

주로 `repeat()`와 `minmax()`와 함께 사용한다.

예:

```css
.grid {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

---

### [핵심]

`auto-fit` 핵심:

- 가능한 column을 채운다.
- 빈 Track을 collapse할 수 있다.
- Item이 적을 때 남은 공간을 Item이 넓게 차지할 수 있다.

`auto-fill` 핵심:

- 가능한 column slot을 채운다.
- 빈 Track 공간을 유지할 수 있다.
- slot 구조를 유지해야 하는 Grid에서 사용할 수 있다.

공통 핵심:

- 반응형 Card Grid에 유용하다.
- media query 없이 column 수가 자동 조정된다.
- `minmax()`와 함께 사용하는 경우가 많다.

---

### [실무]

일반 Card Grid는 `auto-fit`을 우선 고려한다.

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

선택 기준:

```text
Item이 적을 때 남은 공간을 채움 → auto-fit
빈 column slot 유지 필요 → auto-fill
일반 반응형 카드 목록 → auto-fit 우선
```

검수 기준:

- Item이 적을 때 카드가 너무 넓어지지 않는가?
- 빈 column slot 유지가 필요한가?
- 최소 column 크기가 모바일에 적합한가?
- `auto-fit`과 `auto-fill` 차이를 이해하고 선택했는가?

---

### [FAQ]

Q. auto-fit은 뭐야?
A. 가능한 column을 채우고 빈 Track을 collapse해 Item이 남은 공간을 차지하게 하는 Grid 반복 키워드다.

Q. auto-fill은 뭐야?
A. 가능한 column slot을 채우고 빈 Track 공간을 유지할 수 있는 Grid 반복 키워드다.

Q. auto-fit과 auto-fill 중 뭐를 써?
A. 일반적인 반응형 카드 목록은 `auto-fit`을 우선 고려한다.

Q. auto-fit minmax 패턴은 왜 좋아?
A. media query 없이 화면 너비에 따라 column 수가 자동으로 조정되기 때문이다.

---

# 8. Grid Auto Placement

## 8.1 Auto Placement

### [개념]

Grid Auto Placement는 Grid Item의 위치를 명시하지 않아도 브라우저가 Grid에 자동으로 배치하는 방식이다.

대부분의 카드 목록과 갤러리는 Auto Placement로 충분하다.

---

### [핵심]

Auto Placement 핵심:

- Grid Item은 기본적으로 DOM 순서대로 배치된다.
- column이 채워지면 다음 row로 이동한다.
- `grid-auto-flow`로 자동 배치 방향을 조정할 수 있다.
- 명시적 배치를 최소화하면 유지보수가 쉽다.
- DOM 순서와 시각 순서가 일치하면 접근성에 유리하다.

예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
```

---

### [실무]

Card List 예:

```html
<ul class="card-grid">
  <li><article>Card 1</article></li>
  <li><article>Card 2</article></li>
  <li><article>Card 3</article></li>
  <li><article>Card 4</article></li>
</ul>
```

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

검수 기준:

- 명시적 위치 지정이 꼭 필요한가?
- DOM 순서가 시각 순서와 일치하는가?
- 카드 목록은 Auto Placement로 충분하지 않은가?
- 특정 강조 카드만 span 처리하는 것이 더 단순하지 않은가?

---

### [FAQ]

Q. Grid Auto Placement가 뭐야?
A. Grid Item 위치를 직접 지정하지 않아도 브라우저가 자동으로 배치하는 방식이다.

Q. 카드 목록은 Grid 위치를 하나씩 지정해야 해?
A. 아니다. 대부분 Auto Placement로 충분하다.

Q. Auto Placement는 어떤 순서로 배치돼?
A. 기본적으로 DOM 순서대로 row 방향으로 배치된다.

---

## 8.2 grid-auto-flow

### [개념]

`grid-auto-flow`는 Grid Item이 자동 배치되는 방향과 방식을 제어하는 CSS property다.

대표 값:

```css
grid-auto-flow: row;
grid-auto-flow: column;
grid-auto-flow: dense;
```

---

### [핵심]

`grid-auto-flow` 핵심:

- 기본값은 `row`다.
- `row`는 행 방향으로 채우고 다음 행으로 이동한다.
- `column`은 열 방향으로 채우고 다음 열로 이동한다.
- `dense`는 빈 공간을 채우기 위해 뒤의 Item을 앞쪽 빈칸에 배치할 수 있다.
- `dense`는 시각 순서와 DOM 순서를 다르게 만들 수 있다.
- 접근성과 키보드 탐색 순서를 고려해야 한다.

---

### [실무]

Masonry 유사 배치나 빈 공간 채우기에서 `dense`를 검토할 수 있다.

```css
.gallery {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-flow: dense;
  gap: 16px;
}
```

주의:

- `dense`는 시각 순서를 바꿀 수 있다.
- Keyboard Navigation 순서는 DOM 순서를 따른다.
- 중요한 순서가 있는 콘텐츠에는 신중하게 사용한다.

검수 기준:

- 자동 배치 방향을 바꿀 필요가 있는가?
- `dense` 사용으로 시각 순서와 DOM 순서가 달라지지 않는가?
- 순서가 중요한 콘텐츠인가?
- 접근성 검토가 필요한가?

---

### [FAQ]

Q. grid-auto-flow는 뭐야?
A. Grid Item이 자동 배치되는 방향과 방식을 제어하는 property다.

Q. grid-auto-flow 기본값은 뭐야?
A. 기본값은 `row`다.

Q. dense는 언제 조심해야 해?
A. 시각 순서와 DOM 순서를 다르게 만들 수 있어 접근성과 키보드 탐색에 주의해야 한다.

---

# 9. Grid Item Placement

## 9.1 grid-column

### [개념]

`grid-column`은 Grid Item이 차지할 column line 또는 span을 지정하는 CSS property다.

특정 Item을 여러 column에 걸치게 만들 수 있다.

---

### [핵심]

`grid-column` 핵심:

- Grid Item에 적용한다.
- `grid-column: span 2`는 2개 column을 차지한다.
- `grid-column: 1 / 3`은 column line 1부터 3까지 차지한다.
- 강조 카드, Hero Item, Dashboard Item에 사용할 수 있다.
- 반응형 화면에서 span이 문제를 만들 수 있으므로 media query 검토가 필요하다.

예:

```css
.featured-card {
  grid-column: span 2;
}
```

---

### [실무]

Responsive span 예:

```css
.featured-card {
  grid-column: auto;
}

@media (min-width: 768px) {
  .featured-card {
    grid-column: span 2;
  }
}
```

검수 기준:

- 특정 Item이 여러 column을 차지해야 하는가?
- 작은 화면에서 span을 해제했는가?
- Grid column 수보다 큰 span을 지정하지 않았는가?
- Item 강조가 DOM 순서와 접근성 흐름을 해치지 않는가?

---

### [FAQ]

Q. grid-column은 뭐야?
A. Grid Item이 차지할 column 위치나 span을 지정하는 property다.

Q. grid-column span 2는 뭐야?
A. 해당 Grid Item이 column 2칸을 차지한다는 뜻이다.

Q. 모바일에서도 span 2를 유지해도 돼?
A. 주의해야 한다. 작은 화면에서는 span을 해제하거나 1 column layout으로 전환하는 것이 좋다.

---

## 9.2 grid-row

### [개념]

`grid-row`는 Grid Item이 차지할 row line 또는 span을 지정하는 CSS property다.

특정 Item을 여러 row에 걸치게 만들 수 있다.

---

### [핵심]

`grid-row` 핵심:

- Grid Item에 적용한다.
- `grid-row: span 2`는 2개 row를 차지한다.
- Dashboard, Gallery, Feature Card에 사용할 수 있다.
- row 높이와 함께 고려해야 한다.
- 콘텐츠 높이에 따라 예상과 다르게 보일 수 있다.
- 반응형에서 row span이 깨질 수 있다.

예:

```css
.large-card {
  grid-row: span 2;
}
```

---

### [실무]

Dashboard 예:

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(120px, auto);
  gap: 24px;
}

.chart-card {
  grid-column: span 2;
  grid-row: span 2;
}
```

검수 기준:

- row 높이가 명확한가?
- row span이 콘텐츠 높이와 충돌하지 않는가?
- 작은 화면에서 row span을 해제해야 하는가?
- Masonry처럼 보이지만 실제 요구사항이 Grid에 적합한가?

---

### [FAQ]

Q. grid-row는 뭐야?
A. Grid Item이 차지할 row 위치나 span을 지정하는 property다.

Q. grid-row span 2는 뭐야?
A. 해당 Grid Item이 row 2칸을 차지한다는 뜻이다.

Q. grid-row를 쓰면 카드 높이가 자동으로 맞아?
A. 아니다. row 크기와 콘텐츠 높이에 따라 달라진다.

---

# 10. Grid Template Areas

## 10.1 grid-template-areas

### [개념]

`grid-template-areas`는 Grid Layout 영역에 이름을 부여해 배치하는 CSS 방식이다.

Page Layout처럼 구조가 명확한 화면에 유용하다.

---

### [핵심]

`grid-template-areas` 핵심:

- 이름 기반으로 Grid 영역을 정의한다.
- `grid-area`로 Item을 영역에 배치한다.
- Page Layout 가독성이 좋다.
- Header, Sidebar, Main, Footer 구조에 적합하다.
- 영역 이름은 직사각형이어야 한다.
- 복잡한 responsive layout에서 media query와 함께 사용한다.

예:

```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 240px 1fr;
}

.header {
  grid-area: header;
}

.sidebar {
  grid-area: sidebar;
}

.main {
  grid-area: main;
}

.footer {
  grid-area: footer;
}
```

---

### [실무]

Responsive Page Layout 예:

```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  gap: 24px;
}

@media (min-width: 1024px) {
  .page-layout {
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
    grid-template-columns: 280px minmax(0, 1fr);
  }
}
```

검수 기준:

- Page Layout처럼 이름 기반 배치가 명확한가?
- 영역 이름이 직사각형 형태인가?
- mobile layout과 desktop layout 영역 순서가 적절한가?
- DOM 순서와 시각 순서가 과도하게 어긋나지 않는가?
- `main`, `aside`, `header`, `footer` semantic tag와 함께 사용하는가?

---

### [FAQ]

Q. grid-template-areas는 뭐야?
A. Grid 영역에 이름을 부여해 배치하는 CSS 방식이다.

Q. grid-template-areas는 언제 써?
A. Header, Sidebar, Main, Footer처럼 페이지 영역이 명확한 Layout에 적합하다.

Q. grid-area는 뭐야?
A. Grid Item을 지정한 이름의 Grid Area에 배치하는 property다.

Q. grid-template-areas 사용 시 주의할 점은?
A. 영역이 직사각형이어야 하고 DOM 순서와 접근성 흐름을 고려해야 한다.

---

# 11. Alignment in Grid

## 11.1 justify-items and align-items

### [개념]

Grid에서 `justify-items`와 `align-items`는 Grid Item을 각 Grid Area 내부에서 정렬하는 property다.

`justify-items`는 inline axis 방향 정렬이고 `align-items`는 block axis 방향 정렬이다.

---

### [핵심]

Grid Alignment 핵심:

- `justify-items`는 Grid Item의 inline axis 정렬이다.
- `align-items`는 Grid Item의 block axis 정렬이다.
- `place-items`는 `align-items`와 `justify-items`의 축약이다.
- `justify-self`는 개별 Item의 inline axis 정렬이다.
- `align-self`는 개별 Item의 block axis 정렬이다.
- `place-self`는 개별 Item 정렬 축약이다.

예:

```css
.grid {
  display: grid;
  place-items: center;
}
```

---

### [실무]

Center Alignment 예:

```css
.empty-state {
  display: grid;
  place-items: center;
  min-height: 240px;
}
```

Card 내부 Item 정렬 예:

```css
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  align-items: stretch;
}
```

검수 기준:

- Grid Area 안에서 Item을 정렬하는 문제인가?
- 전체 Track 간격 문제와 Item 정렬 문제를 혼동하지 않았는가?
- 하나의 Item만 정렬해야 하면 justify-self / align-self를 사용하는가?
- 중앙 정렬만 필요하면 `place-items: center`가 적절한가?

---

### [FAQ]

Q. Grid에서 justify-items는 뭐야?
A. Grid Item을 Grid Area 내부의 inline axis 방향으로 정렬하는 property다.

Q. Grid에서 align-items는 뭐야?
A. Grid Item을 Grid Area 내부의 block axis 방향으로 정렬하는 property다.

Q. place-items는 뭐야?
A. `align-items`와 `justify-items`를 한 번에 지정하는 축약 property다.

Q. Grid로 가운데 정렬은 어떻게 해?
A. Container에 `display: grid`와 `place-items: center`를 사용할 수 있다.

---

## 11.2 justify-content and align-content

### [개념]

Grid에서 `justify-content`와 `align-content`는 Grid 전체 Track 묶음을 Container 내부에서 정렬하는 property다.

Item 개별 정렬이 아니라 Grid Track 전체 정렬에 사용한다.

---

### [핵심]

Grid Content Alignment 핵심:

- `justify-content`는 Grid Track 전체를 inline axis 방향으로 정렬한다.
- `align-content`는 Grid Track 전체를 block axis 방향으로 정렬한다.
- Container가 Grid Track보다 커야 효과가 보인다.
- Item 정렬은 `justify-items`, `align-items`가 담당한다.
- Track 묶음 정렬과 Item 정렬을 구분해야 한다.

예:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 200px);
  justify-content: center;
}
```

---

### [실무]

고정 폭 Grid 중앙 정렬 예:

```css
.fixed-card-grid {
  display: grid;
  grid-template-columns: repeat(3, 240px);
  gap: 24px;
  justify-content: center;
}
```

검수 기준:

- Grid Track 전체가 Container보다 작은가?
- Item 내부 정렬 문제가 아닌가?
- 고정 Track을 중앙에 배치하려는 목적이 맞는가?
- responsive Grid에서는 Track 정렬보다 Track 자체의 유연성이 더 적절하지 않은가?

---

### [FAQ]

Q. Grid에서 justify-content는 뭐야?
A. Grid Track 전체 묶음을 inline axis 방향으로 정렬하는 property다.

Q. Grid에서 align-content는 뭐야?
A. Grid Track 전체 묶음을 block axis 방향으로 정렬하는 property다.

Q. justify-items와 justify-content 차이는?
A. justify-items는 Item을 Area 안에서 정렬하고 justify-content는 Grid Track 전체를 Container 안에서 정렬한다.

---

# 12. Responsive Grid

## 12.1 Responsive Grid Concept

### [개념]

Responsive Grid는 화면 크기에 따라 column 수, track 크기, gap, item placement가 자연스럽게 변하는 Grid Layout이다.

---

### [핵심]

Responsive Grid 핵심:

- Mobile First로 기본 1 column을 작성한다.
- 넓은 화면에서 column을 늘린다.
- `repeat(auto-fit, minmax())`로 자동 column 조절이 가능하다.
- media query로 명시적 column 전환이 가능하다.
- gap도 화면 크기에 따라 조정할 수 있다.
- 작은 화면에서는 span item을 해제한다.
- 고정 px column은 모바일 overflow를 만들 수 있다.

---

### [실무]

Auto Responsive Grid 예:

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

Media Query Grid 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

Span 해제 예:

```css
.featured-card {
  grid-column: auto;
}

@media (min-width: 768px) {
  .featured-card {
    grid-column: span 2;
  }
}
```

검수 기준:

- 모바일 기본 Layout이 1 column인가?
- column 최소 크기가 작은 화면에 적합한가?
- gap이 모바일에서 과도하지 않은가?
- span item이 모바일에서 overflow를 만들지 않는가?
- auto-fit 패턴과 media query 패턴 중 무엇이 더 명확한가?

---

### [FAQ]

Q. Responsive Grid는 어떻게 작성해?
A. Mobile First로 1 column을 기본으로 하고 media query 또는 `auto-fit minmax()`로 column을 늘린다.

Q. auto-fit minmax는 왜 반응형에 좋아?
A. Container 너비에 따라 가능한 column 수를 자동으로 조정하기 때문이다.

Q. 모바일에서 Grid가 깨지는 이유는?
A. column 최소 크기, 고정 width, 큰 gap, span item, 큰 이미지 때문에 overflow가 발생할 수 있다.

Q. 작은 화면에서는 grid-column span을 유지해도 돼?
A. 주의해야 한다. 보통 모바일에서는 span을 해제하거나 1 column으로 만든다.

---

# 13. Common Grid Patterns

## 13.1 Card Grid

### [개념]

Card Grid는 여러 Card Component를 행과 열로 배치하는 대표 Grid 패턴이다.

Festival Card, Product Card, Article Card, Review Card 목록에 적합하다.

---

### [핵심]

Card Grid 핵심:

- 목록 Container에 `display: grid`를 적용한다.
- `repeat(auto-fit, minmax())` 또는 breakpoint별 columns를 사용한다.
- `gap`으로 카드 간격을 관리한다.
- 카드 자체는 `article`로 구성할 수 있다.
- 목록 구조는 `ul` / `li`와 함께 사용할 수 있다.
- 이미지에는 `max-width: 100%`가 필요하다.

---

### [실무]

Card Grid 예:

```html
<ul class="festival-grid">
  <li>
    <article class="festival-card">
      <h2>Seoul Light Festival</h2>
      <p>Night light festival in Seoul.</p>
    </article>
  </li>
  <li>
    <article class="festival-card">
      <h2>Busan Sea Festival</h2>
      <p>Summer festival in Busan.</p>
    </article>
  </li>
</ul>
```

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
  list-style: none;
  margin: 0;
  padding: 0;
}
```

검수 기준:

- 카드 목록 부모가 Grid Container인가?
- 카드 목록이 list semantics를 유지하는가?
- 카드 최소 너비가 적절한가?
- gap이 일관적인가?
- 카드 내부 정렬은 Flexbox가 더 적절하지 않은가?

---

### [FAQ]

Q. Card Grid는 어떻게 만들어?
A. 카드 목록 부모에 `display: grid`, `grid-template-columns`, `gap`을 적용한다.

Q. 카드 목록에는 ul/li를 써도 돼?
A. 가능하다. 여러 카드가 반복되는 목록이라면 list semantics가 적절하다.

Q. 카드 내부 Layout도 Grid로 해야 해?
A. 반드시 아니다. 카드 내부의 한 방향 정렬은 Flexbox가 더 적합할 수 있다.

---

## 13.2 Page Layout Grid

### [개념]

Page Layout Grid는 Header, Sidebar, Main, Footer 같은 페이지 영역을 Grid로 배치하는 패턴이다.

---

### [핵심]

Page Layout Grid 핵심:

- 페이지 전체 영역 배치에 적합하다.
- `grid-template-areas`를 사용하면 구조가 명확하다.
- Desktop에서는 Sidebar + Main 2 column이 가능하다.
- Mobile에서는 1 column으로 전환한다.
- Semantic HTML과 함께 사용한다.
- DOM 순서와 시각 순서를 고려한다.

---

### [실무]

Page Layout 예:

```html
<div class="page-layout">
  <header class="page-header">Header</header>
  <aside class="page-sidebar">Sidebar</aside>
  <main class="page-main">Main</main>
  <footer class="page-footer">Footer</footer>
</div>
```

```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  gap: 24px;
}

.page-header {
  grid-area: header;
}

.page-sidebar {
  grid-area: sidebar;
}

.page-main {
  grid-area: main;
  min-width: 0;
}

.page-footer {
  grid-area: footer;
}

@media (min-width: 1024px) {
  .page-layout {
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
    grid-template-columns: 280px minmax(0, 1fr);
  }
}
```

검수 기준:

- Page 영역이 Semantic HTML로 작성되었는가?
- Mobile에서 1 column 흐름이 자연스러운가?
- Desktop에서 Sidebar width가 적절한가?
- Main 영역에 `min-width: 0`이 필요한가?
- DOM 순서와 시각 순서가 접근성에 문제 없는가?

---

### [FAQ]

Q. Page Layout에 Grid를 써도 돼?
A. 적합하다. Header, Sidebar, Main, Footer 같은 2차원 영역 배치에 좋다.

Q. Sidebar Layout은 Grid가 좋아 Flexbox가 좋아?
A. 단순 2 column은 둘 다 가능하지만 Page 전체 영역 배치는 Grid가 더 명확한 경우가 많다.

Q. Mobile에서는 Sidebar를 어떻게 처리해?
A. 1 column 흐름으로 전환하거나 main 뒤 또는 앞에 배치하는 전략을 선택한다.

---

## 13.3 Form Grid

### [개념]

Form Grid는 여러 Form Field를 열과 행으로 배치하는 Grid 패턴이다.

회원가입, 검색 필터, 관리자 입력 화면에 사용할 수 있다.

---

### [핵심]

Form Grid 핵심:

- 관련 Field를 2 column 이상으로 배치할 수 있다.
- 모바일에서는 1 column이 기본이다.
- Field label과 input 연결은 유지해야 한다.
- Error Message가 Field 영역 안에 있어야 한다.
- 필수 Field나 긴 Field는 전체 column을 span할 수 있다.
- Grid는 배치만 담당하고 Form semantics는 유지해야 한다.

---

### [실무]

Form Grid 예:

```html
<form class="profile-form">
  <div class="form-field">
    <label for="firstName">First Name</label>
    <input id="firstName" name="firstName" type="text" />
  </div>

  <div class="form-field">
    <label for="lastName">Last Name</label>
    <input id="lastName" name="lastName" type="text" />
  </div>

  <div class="form-field form-field-full">
    <label for="bio">Bio</label>
    <textarea id="bio" name="bio"></textarea>
  </div>
</form>
```

```css
.profile-form {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .profile-form {
    grid-template-columns: 1fr 1fr;
  }

  .form-field-full {
    grid-column: 1 / -1;
  }
}
```

검수 기준:

- 모바일에서 1 column으로 읽기 쉬운가?
- label과 input 연결이 유지되는가?
- error message가 해당 field와 함께 배치되는가?
- 긴 textarea나 full-width field가 적절히 span되는가?
- tab order가 시각 순서와 크게 어긋나지 않는가?

---

### [FAQ]

Q. Form Layout에 Grid를 써도 돼?
A. 가능하다. 여러 Field를 행과 열로 정렬할 때 유용하다.

Q. 모바일 Form Grid는 어떻게 해?
A. 기본 1 column으로 작성하고 넓은 화면에서 2 column 이상으로 확장한다.

Q. Form Grid에서 중요한 접근성 기준은?
A. label 연결, error message 위치, tab order, field grouping을 유지하는 것이다.

---

# 14. Grid Troubleshooting

## 14.1 Grid Layout Broken

### [개념]

Grid Layout Broken은 Grid Item이 예상 column, row, 크기, 간격, 반응형 동작과 다르게 배치되는 문제다.

주요 원인은 column 최소 크기, 고정 width, span 설정, gap 과다, min-width 문제, DOM 순서와 시각 순서 불일치다.

---

### [핵심]

주요 문제:

- `display: grid`를 잘못된 요소에 적용
- Grid Item이 직접 자식이 아님
- `grid-template-columns` 고정값으로 overflow 발생
- `minmax()` 최소값이 너무 큼
- `gap`이 작거나 큰 화면에 맞지 않음
- `grid-column: span`이 모바일에서 문제 발생
- 긴 텍스트 때문에 Grid Item overflow 발생
- 이미지 max-width 누락
- `auto-fit`과 `auto-fill` 차이 오해
- `justify-items`와 `justify-content` 혼동
- `grid-auto-flow: dense`로 시각 순서 변경
- Page Layout에서 DOM 순서와 시각 순서 불일치

---

### [실무]

Debug Flow:

```text
Grid Container Inspect
→ display grid 확인
→ Direct Child Grid Item 확인
→ grid-template-columns 확인
→ gap 확인
→ minmax 최소값 확인
→ item span 확인
→ min-width / overflow 확인
→ image max-width 확인
→ responsive viewport 확인
→ DOM order / visual order 확인
```

문제 예:

```text
문제: 모바일에서 Grid가 가로로 넘침
원인: minmax 최소값이 viewport보다 큼
해결: 최소값 축소, 1 column media query, overflow 원인 제거
```

```text
문제: 카드가 예상보다 넓게 늘어남
원인: auto-fit이 빈 Track을 collapse하고 Item이 남은 공간을 차지
해결: max-width, auto-fill, wrapper width 전략 검토
```

```text
문제: Main 영역 텍스트가 Sidebar를 밀어냄
원인: Grid Item min-width 기본값
해결: Main 영역에 min-width: 0 적용
```

---

### [FAQ]

Q. Grid가 안 먹을 때 가장 먼저 볼 것은?
A. 배치하려는 요소들의 부모에 `display: grid`가 적용되어 있는지 확인한다.

Q. Grid Item이 원하는 대로 배치되지 않는 이유는?
A. 직접 자식이 아니거나 column 정의, span 설정, auto placement 규칙이 원인일 수 있다.

Q. 모바일에서 Grid가 넘치는 이유는?
A. 고정 column, 큰 minmax 최소값, 큰 gap, span item, 큰 이미지, 긴 텍스트 때문일 수 있다.

Q. Grid overflow는 어떻게 해결해?
A. minmax 최소값 조정, 1 column 전환, min-width 0, image max-width, gap 조정을 확인한다.

---

# 15. Comparison Rules

## 15.1 Grid vs Flexbox

### [개념]

Grid는 2차원 Layout에 적합하고 Flexbox는 1차원 Layout에 적합하다.

---

### [핵심]

| 비교      | Grid                            | Flexbox                            |
| --------- | ------------------------------- | ---------------------------------- |
| 기준      | 2차원 Layout                    | 1차원 Layout                       |
| 방향      | row + column                    | row 또는 column                    |
| 적합      | 카드 목록, 갤러리, 대시보드     | 버튼 그룹, navbar, 카드 내부       |
| 배치 기준 | Track 중심                      | Item 중심                          |
| 핵심 속성 | grid-template-columns, grid-row | justify-content, align-items, flex |
| 대표 패턴 | Page Layout, Card Grid          | Header, Form Row, Icon Text        |

---

### [실무]

선택 기준:

```text
Card List → Grid
Gallery → Grid
Dashboard → Grid
Page Area Layout → Grid
Button Group → Flexbox
Icon + Text → Flexbox
Card Internal Alignment → Flexbox
Navigation Row → Flexbox
```

---

### [FAQ]

Q. Grid와 Flexbox 차이는 뭐야?
A. Grid는 2차원 배치, Flexbox는 1차원 배치에 적합하다.

Q. 카드 목록은 Grid가 좋아?
A. 행과 열이 중요한 카드 목록은 Grid가 적합한 경우가 많다.

Q. 카드 내부 정렬은 Grid가 좋아 Flexbox가 좋아?
A. 한 방향 정렬 중심이면 Flexbox가 더 단순한 경우가 많다.

---

## 15.2 auto-fit vs auto-fill

### [개념]

`auto-fit`과 `auto-fill`은 가능한 Grid Track을 자동 생성하지만 빈 Track 처리 방식이 다르다.

---

### [핵심]

| 비교           | auto-fit                     | auto-fill                     |
| -------------- | ---------------------------- | ----------------------------- |
| 빈 Track       | collapse 가능                | 유지 가능                     |
| Item 적을 때   | Item이 공간을 더 차지        | 빈 slot 유지                  |
| 일반 카드 목록 | 자주 적합                    | 경우에 따라 적합              |
| Slot 유지      | 약함                         | 강함                          |
| 사용 패턴      | `repeat(auto-fit, minmax())` | `repeat(auto-fill, minmax())` |

---

### [실무]

선택 기준:

```text
일반 반응형 카드 목록 → auto-fit
빈 column slot 유지 필요 → auto-fill
Item 수가 적을 때 카드가 너무 넓어짐 → auto-fill 또는 max-width 검토
```

---

### [FAQ]

Q. auto-fit과 auto-fill 차이는 뭐야?
A. auto-fit은 빈 Track을 collapse할 수 있고 auto-fill은 빈 Track 공간을 유지할 수 있다.

Q. 일반 카드 목록에는 뭐가 좋아?
A. 일반적으로 `auto-fit`을 먼저 고려한다.

Q. 카드가 너무 넓게 늘어나면 어떻게 해?
A. max-width를 주거나 auto-fill, wrapper layout을 검토할 수 있다.

---

## 15.3 justify-items vs justify-content

### [개념]

`justify-items`는 Grid Item을 Area 내부에서 정렬하고, `justify-content`는 Grid Track 전체를 Container 내부에서 정렬한다.

---

### [핵심]

| 비교      | justify-items             | justify-content                 |
| --------- | ------------------------- | ------------------------------- |
| 대상      | Grid Item                 | Grid Track 전체                 |
| 기준      | 각 Grid Area 내부         | Container 내부                  |
| 효과 조건 | Item 크기가 Area보다 작음 | Track 전체가 Container보다 작음 |
| 사용 예   | 카드 안쪽 정렬            | 고정폭 Grid 중앙 정렬           |
| 관련 속성 | align-items, place-items  | align-content, place-content    |

---

### [실무]

선택 기준:

```text
Item을 각 칸 안에서 중앙 정렬 → justify-items
Grid 전체 묶음을 Container 중앙 정렬 → justify-content
가로세로 Item 중앙 정렬 → place-items
Track 묶음 중앙 정렬 → place-content
```

---

### [FAQ]

Q. justify-items와 justify-content 차이는 뭐야?
A. justify-items는 Item 정렬이고 justify-content는 Grid Track 전체 정렬이다.

Q. Grid Item을 칸 안에서 가운데 두려면?
A. `justify-items: center` 또는 `place-items: center`를 사용할 수 있다.

Q. 고정 너비 Grid 전체를 가운데 두려면?
A. `justify-content: center`를 사용할 수 있다.

---

## 15.4 grid-column vs grid-template-columns

### [개념]

`grid-template-columns`는 Container의 column 구조를 정의하고 `grid-column`은 Item이 차지할 column 위치나 span을 지정한다.

---

### [핵심]

| 비교      | grid-template-columns | grid-column      |
| --------- | --------------------- | ---------------- |
| 적용 대상 | Grid Container        | Grid Item        |
| 역할      | 열 Track 정의         | Item column 배치 |
| 예시      | `repeat(3, 1fr)`      | `span 2`         |
| 사용 목적 | 전체 Grid 구조        | 특정 Item 위치   |
| 주의      | 고정 column overflow  | 모바일 span 문제 |

---

### [실무]

선택 기준:

```text
전체 column 구조 만들기 → grid-template-columns
특정 카드 2칸 차지 → grid-column: span 2
반응형 column 수 조절 → grid-template-columns + media query
모바일 span 해제 → grid-column: auto
```

---

### [FAQ]

Q. grid-template-columns와 grid-column 차이는 뭐야?
A. grid-template-columns는 Container의 열 구조를 만들고 grid-column은 Item의 열 배치를 지정한다.

Q. 특정 카드만 크게 만들려면?
A. 해당 Grid Item에 `grid-column: span 2`를 적용할 수 있다.

Q. 모바일에서 span이 깨지면?
A. media query로 `grid-column: auto` 또는 1 column layout을 적용한다.

---

# 16. Common Mistakes

## 16.1 Grid Common Mistakes

### [개념]

Grid 실수는 반응형 깨짐, overflow, 카드 배치 오류, Page Layout 순서 문제, 접근성 문제로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- Grid Container가 아닌 Item에 `display: grid` 적용
- Grid Item이 직접 자식인지 확인하지 않음
- 고정 column width 남용
- `repeat(3, 1fr)`만 쓰고 모바일 대응 없음
- `minmax()` 최소값을 너무 크게 설정
- `auto-fit`과 `auto-fill` 차이 오해
- `gap`을 고려하지 않아 column이 좁아짐
- `grid-column: span 2`를 모바일에서도 유지
- 긴 텍스트 Item에 `min-width: 0` 누락
- 이미지 `max-width: 100%` 누락
- `justify-items`와 `justify-content` 혼동
- `align-items`와 `align-content` 혼동
- `grid-auto-flow: dense`로 시각 순서와 DOM 순서 불일치
- table이 필요한 데이터를 Grid Card로만 처리
- 단순 한 줄 정렬에 Grid를 과도하게 사용

---

### [실무]

Troubleshooting Flow:

```text
Grid Bug
→ Container display grid 확인
→ Direct Child Item 확인
→ Columns 정의 확인
→ Track size 확인
→ Gap 확인
→ Item span 확인
→ min-width / max-width 확인
→ Responsive viewport 확인
→ Alignment property 확인
→ DOM order 확인
```

문제 예:

```text
문제: 카드 목록이 모바일에서 3열로 유지되어 깨짐
원인: repeat(3, 1fr) 고정
해결: mobile 1 column 기본 + media query 또는 auto-fit minmax 적용
```

```text
문제: 강조 카드가 작은 화면에서 넘침
원인: grid-column span 2 유지
해결: 모바일에서 grid-column auto 적용
```

```text
문제: Grid 내부 긴 제목이 column을 밀어냄
원인: Grid Item min-width 기본값
해결: Item 또는 content에 min-width: 0 적용
```

---

### [FAQ]

Q. Grid에서 가장 흔한 실수는 뭐야?
A. 고정 column을 만들고 모바일 대응을 하지 않거나 Grid Container와 Item을 혼동하는 것이다.

Q. 모바일에서 Grid Layout이 깨지는 흔한 이유는?
A. 고정 column, 큰 minmax 최소값, span 유지, gap 과다, 이미지 크기 때문이다.

Q. Grid 정렬에서 헷갈리는 점은 뭐야?
A. justify-items와 justify-content, align-items와 align-content를 혼동하는 것이다.

Q. Grid 문제는 어떤 순서로 디버깅해?
A. Container, Direct Child, columns, track size, gap, item span, overflow, responsive 순서로 확인한다.

---

# 17. Best Practice

## 17.1 Grid Best Practice

### [개념]

Grid Best Practice는 2차원 Layout, 반복 Card Grid, Page Layout, Responsive Layout을 안정적으로 구현하기 위한 기준이다.

---

### [핵심]

권장 기준:

- 2차원 Layout에는 Grid 우선 고려
- 정렬 대상의 부모에 `display: grid` 적용
- Grid Item이 직접 자식인지 확인
- 반복 카드 목록은 `repeat(auto-fit, minmax())` 고려
- Mobile First 기준으로 1 column 기본 작성
- 고정 column width 남용 금지
- `gap`으로 Item 간격 관리
- `grid-column: span`은 반응형 해제 고려
- 긴 텍스트 Item에는 `min-width: 0` 검토
- 이미지에는 `max-width: 100%` 적용
- Page Layout에는 `grid-template-areas` 고려
- DOM 순서와 시각 순서를 과도하게 다르게 만들지 않음
- `dense` 사용 시 접근성 검토
- 단순 한 방향 정렬은 Flexbox 검토
- table 데이터는 Grid가 아니라 table 검토

---

### [실무]

Responsive Card Grid 예:

```css
.festival-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}
```

Mobile First Grid 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
  }
}

@media (min-width: 1024px) {
  .card-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

Page Layout 예:

```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  gap: 24px;
}

@media (min-width: 1024px) {
  .page-layout {
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
    grid-template-columns: 280px minmax(0, 1fr);
  }
}
```

검수 Checklist:

```md
- [ ] 2차원 Layout 요구사항인가?
- [ ] Grid Container에 `display: grid`가 적용되었는가?
- [ ] Grid Item이 직접 자식인가?
- [ ] `grid-template-columns`가 반응형에 적합한가?
- [ ] Mobile First 1 column 기준이 있는가?
- [ ] `gap`으로 간격을 관리하는가?
- [ ] `minmax()` 최소값이 너무 크지 않은가?
- [ ] span Item이 모바일에서 해제되는가?
- [ ] 긴 텍스트 Item에 `min-width: 0`이 필요한가?
- [ ] 이미지가 부모를 넘지 않는가?
- [ ] Page Layout에 semantic tag와 grid-template-areas를 적절히 사용했는가?
- [ ] DOM 순서와 시각 순서가 접근성에 문제 없는가?
- [ ] 단순 1차원 정렬에 Grid를 과도하게 쓰지 않았는가?
```

---

### [FAQ]

Q. Grid Best Practice는 뭐야?
A. 2차원 Layout에 Grid를 사용하고 Mobile First, gap, minmax, auto-fit, span 해제, DOM 순서를 함께 고려하는 것이다.

Q. Grid 검수에서 가장 먼저 볼 것은 뭐야?
A. `display: grid`가 올바른 부모에 적용되었는지와 Grid Item이 직접 자식인지 먼저 확인한다.

Q. Grid를 쓰면 안 좋은 경우는?
A. 단순 한 방향 정렬은 Flexbox가 더 단순하고, 표 데이터는 table이 더 적합하다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 CSS Grid로 Card Grid, Page Layout, Dashboard, Form Grid를 안정적으로 생성하고 디버깅하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. CSS Grid가 뭐야?
A. 행과 열을 기준으로 요소를 배치하는 CSS 2차원 Layout 방식이다.

Q. Grid는 언제 써?
A. 카드 목록, 갤러리, 대시보드, 페이지 레이아웃처럼 행과 열이 모두 중요한 UI에 사용한다.

Q. Grid는 2차원 Layout이야?
A. 맞다. row와 column을 함께 제어하는 Layout에 적합하다.

Q. Flexbox와 Grid 중 뭐를 써야 해?
A. 한 방향 정렬은 Flexbox, 행과 열이 모두 중요한 2차원 배치는 Grid가 적합하다.

Q. Grid Container가 뭐야?
A. `display: grid`가 적용되어 자식 요소를 Grid Item으로 배치하는 부모 요소다.

Q. Grid Item은 어떤 요소야?
A. Grid Container의 직접 자식 요소다.

Q. 손자 요소도 Grid Item이 돼?
A. 아니다. Grid Container의 직접 자식만 Grid Item이 된다.

Q. 카드 목록을 Grid로 만들려면 어디에 display grid를 줘?
A. 카드들을 감싸는 부모 목록 또는 Container에 `display: grid`를 준다.

Q. Grid Item을 두 칸 차지하게 하려면?
A. `grid-column: span 2` 같은 속성을 사용할 수 있다.

Q. Grid Item이 부모 밖으로 나가는 이유는?
A. 고정 width, 긴 텍스트, 기본 min-width, 큰 이미지 때문에 줄어들지 못하기 때문일 수 있다.

Q. Grid Track이 뭐야?
A. Grid의 행 또는 열 하나를 의미한다.

Q. grid-template-columns는 뭐야?
A. Grid의 열 구조를 정의하는 CSS property다.

Q. grid-template-rows는 언제 써?
A. 행 높이 구조를 명확히 정의해야 할 때 사용한다.

Q. fr 단위는 뭐야?
A. Grid Container의 남은 공간을 비율로 나누는 단위다.

Q. Grid Line이 뭐야?
A. Grid Track을 나누는 경계선이다.

Q. grid-column 1 / 3은 무슨 뜻이야?
A. column line 1부터 3까지 차지한다는 뜻이다.

Q. span은 무슨 뜻이야?
A. Grid Item이 몇 개의 Track을 차지할지 지정하는 방식이다.

Q. repeat(3, 1fr)은 무슨 뜻이야?
A. 같은 너비의 열 3개를 만든다는 뜻이다.

Q. 반응형 카드 Grid는 어떻게 작성해?
A. `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));` 패턴을 사용할 수 있다.

Q. grid-template-rows는 뭐야?
A. Grid의 행 구조를 정의하는 CSS property다.

Q. grid-auto-rows는 언제 써?
A. 자동으로 생성되는 row의 기본 크기를 지정할 때 사용한다.

Q. Grid gap은 뭐야?
A. Grid Item 사이의 행과 열 간격을 지정하는 property다.

Q. Grid에서도 gap을 써?
A. 쓴다. Grid Item 간격 관리에 가장 일반적으로 사용한다.

Q. row-gap과 column-gap 차이는 뭐야?
A. row-gap은 행 간격이고 column-gap은 열 간격이다.

Q. repeat()는 뭐야?
A. Grid Track 정의를 반복해서 작성하는 CSS 함수다.

Q. repeat()는 반응형에도 쓸 수 있어?
A. 가능하다. `auto-fit` 또는 `auto-fill`과 함께 사용할 수 있다.

Q. minmax()는 뭐야?
A. Grid Track의 최소 크기와 최대 크기를 지정하는 CSS 함수다.

Q. minmax(240px, 1fr)은 무슨 뜻이야?
A. Track이 최소 240px이고 가능한 경우 1fr까지 늘어난다는 뜻이다.

Q. minmax 최소값이 너무 크면 어떻게 돼?
A. 작은 화면에서 Grid가 overflow되어 가로 스크롤이 생길 수 있다.

Q. minmax(0, 1fr)은 언제 써?
A. Grid Item이 최소 크기 때문에 overflow되는 문제를 줄일 때 사용할 수 있다.

Q. auto-fit은 뭐야?
A. 가능한 column을 채우고 빈 Track을 collapse해 Item이 남은 공간을 차지하게 하는 Grid 반복 키워드다.

Q. auto-fill은 뭐야?
A. 가능한 column slot을 채우고 빈 Track 공간을 유지할 수 있는 Grid 반복 키워드다.

Q. auto-fit과 auto-fill 중 뭐를 써?
A. 일반적인 반응형 카드 목록은 `auto-fit`을 우선 고려한다.

Q. auto-fit minmax 패턴은 왜 좋아?
A. media query 없이 화면 너비에 따라 column 수가 자동으로 조정되기 때문이다.

Q. Grid Auto Placement가 뭐야?
A. Grid Item 위치를 직접 지정하지 않아도 브라우저가 자동으로 배치하는 방식이다.

Q. 카드 목록은 Grid 위치를 하나씩 지정해야 해?
A. 아니다. 대부분 Auto Placement로 충분하다.

Q. grid-auto-flow는 뭐야?
A. Grid Item이 자동 배치되는 방향과 방식을 제어하는 property다.

Q. grid-auto-flow 기본값은 뭐야?
A. 기본값은 `row`다.

Q. dense는 언제 조심해야 해?
A. 시각 순서와 DOM 순서를 다르게 만들 수 있어 접근성과 키보드 탐색에 주의해야 한다.

Q. grid-column은 뭐야?
A. Grid Item이 차지할 column 위치나 span을 지정하는 property다.

Q. grid-column span 2는 뭐야?
A. 해당 Grid Item이 column 2칸을 차지한다는 뜻이다.

Q. 모바일에서도 span 2를 유지해도 돼?
A. 주의해야 한다. 작은 화면에서는 span을 해제하거나 1 column layout으로 전환하는 것이 좋다.

Q. grid-row는 뭐야?
A. Grid Item이 차지할 row 위치나 span을 지정하는 property다.

Q. grid-template-areas는 뭐야?
A. Grid 영역에 이름을 부여해 배치하는 CSS 방식이다.

Q. grid-template-areas는 언제 써?
A. Header, Sidebar, Main, Footer처럼 페이지 영역이 명확한 Layout에 적합하다.

Q. grid-area는 뭐야?
A. Grid Item을 지정한 이름의 Grid Area에 배치하는 property다.

Q. Grid에서 justify-items는 뭐야?
A. Grid Item을 Grid Area 내부의 inline axis 방향으로 정렬하는 property다.

Q. Grid에서 align-items는 뭐야?
A. Grid Item을 Grid Area 내부의 block axis 방향으로 정렬하는 property다.

Q. place-items는 뭐야?
A. `align-items`와 `justify-items`를 한 번에 지정하는 축약 property다.

Q. Grid로 가운데 정렬은 어떻게 해?
A. Container에 `display: grid`와 `place-items: center`를 사용할 수 있다.

Q. Grid에서 justify-content는 뭐야?
A. Grid Track 전체 묶음을 inline axis 방향으로 정렬하는 property다.

Q. justify-items와 justify-content 차이는?
A. justify-items는 Item을 Area 안에서 정렬하고 justify-content는 Grid Track 전체를 Container 안에서 정렬한다.

Q. Responsive Grid는 어떻게 작성해?
A. Mobile First로 1 column을 기본으로 하고 media query 또는 `auto-fit minmax()`로 column을 늘린다.

Q. 모바일에서 Grid가 깨지는 이유는?
A. column 최소 크기, 고정 width, 큰 gap, span item, 큰 이미지 때문에 overflow가 발생할 수 있다.

Q. Card Grid는 어떻게 만들어?
A. 카드 목록 부모에 `display: grid`, `grid-template-columns`, `gap`을 적용한다.

Q. 카드 목록에는 ul/li를 써도 돼?
A. 가능하다. 여러 카드가 반복되는 목록이라면 list semantics가 적절하다.

Q. Page Layout에 Grid를 써도 돼?
A. 적합하다. Header, Sidebar, Main, Footer 같은 2차원 영역 배치에 좋다.

Q. Form Layout에 Grid를 써도 돼?
A. 가능하다. 여러 Field를 행과 열로 정렬할 때 유용하다.

Q. Grid가 안 먹을 때 가장 먼저 볼 것은?
A. 배치하려는 요소들의 부모에 `display: grid`가 적용되어 있는지 확인한다.

Q. Grid Item이 원하는 대로 배치되지 않는 이유는?
A. 직접 자식이 아니거나 column 정의, span 설정, auto placement 규칙이 원인일 수 있다.

Q. Grid overflow는 어떻게 해결해?
A. minmax 최소값 조정, 1 column 전환, min-width 0, image max-width, gap 조정을 확인한다.

Q. Grid와 Flexbox 차이는 뭐야?
A. Grid는 2차원 배치, Flexbox는 1차원 배치에 적합하다.

Q. auto-fit과 auto-fill 차이는 뭐야?
A. auto-fit은 빈 Track을 collapse할 수 있고 auto-fill은 빈 Track 공간을 유지할 수 있다.

Q. 카드가 너무 넓게 늘어나면 어떻게 해?
A. max-width를 주거나 auto-fill, wrapper layout을 검토할 수 있다.

Q. justify-items와 justify-content 차이는 뭐야?
A. justify-items는 Item 정렬이고 justify-content는 Grid Track 전체 정렬이다.

Q. grid-template-columns와 grid-column 차이는 뭐야?
A. grid-template-columns는 Container의 열 구조를 만들고 grid-column은 Item의 열 배치를 지정한다.

Q. 특정 카드만 크게 만들려면?
A. 해당 Grid Item에 `grid-column: span 2`를 적용할 수 있다.

Q. Grid에서 가장 흔한 실수는 뭐야?
A. 고정 column을 만들고 모바일 대응을 하지 않거나 Grid Container와 Item을 혼동하는 것이다.

Q. 모바일에서 Grid Layout이 깨지는 흔한 이유는?
A. 고정 column, 큰 minmax 최소값, span 유지, gap 과다, 이미지 크기 때문이다.

Q. Grid 문제는 어떤 순서로 디버깅해?
A. Container, Direct Child, columns, track size, gap, item span, overflow, responsive 순서로 확인한다.

Q. Grid Best Practice는 뭐야?
A. 2차원 Layout에 Grid를 사용하고 Mobile First, gap, minmax, auto-fit, span 해제, DOM 순서를 함께 고려하는 것이다.

Q. Grid 검수에서 가장 먼저 볼 것은 뭐야?
A. `display: grid`가 올바른 부모에 적용되었는지와 Grid Item이 직접 자식인지 먼저 확인한다.

Q. Grid를 쓰면 안 좋은 경우는?
A. 단순 한 방향 정렬은 Flexbox가 더 단순하고, 표 데이터는 table이 더 적합하다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 CSS Grid로 Card Grid, Page Layout, Dashboard, Form Grid를 안정적으로 생성하고 디버깅하게 만드는 것이다.
