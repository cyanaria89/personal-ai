# HTML CSS Foundation Part07 - Flexbox

---

# 1. Flexbox

## 1.1 Flexbox Concept

### [개념]

Flexbox는 1차원 Layout을 구현하기 위한 CSS Layout 방식이다.

Flexbox는 행(row) 또는 열(column) 한 방향을 기준으로 요소를 정렬하고 배치한다.

기본 예:

```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
}
```

Flexbox는 Button Group, Header Navigation, Card 내부 정렬, Icon + Text 정렬, 중앙 정렬, Form Field Row에 자주 사용된다.

---

### [핵심]

Flexbox 핵심:

- `display: flex`로 Flex Formatting Context를 만든다.
- Flex Container는 부모 요소다.
- Flex Item은 Flex Container의 직접 자식 요소다.
- `flex-direction`은 Main Axis 방향을 결정한다.
- `justify-content`는 Main Axis 정렬을 담당한다.
- `align-items`는 Cross Axis 정렬을 담당한다.
- `gap`은 Flex Item 사이 간격을 만든다.
- `flex-wrap`은 줄바꿈 여부를 결정한다.
- `flex-grow`, `flex-shrink`, `flex-basis`는 Flex Item 크기 분배를 제어한다.
- Flexbox는 1차원 Layout에 적합하다.

---

### [실무]

2026 실무 기준에서 Flexbox는 정렬과 배치 문제를 해결하는 기본 Layout 도구다.

Frontend Agent는 Flexbox를 사용해 아래 UI를 안정적으로 구현해야 한다.

- Header Navigation
- Button Group
- Form Row
- Card 내부 정렬
- Icon + Text
- Center Alignment
- Sidebar + Content 간단 배치
- Responsive Row Wrapping
- Toolbar
- Badge List
- Avatar + User Info

Flexbox 작성 Flow:

```text
Parent Container 선택
→ display flex
→ flex-direction 설정
→ main axis 정렬
→ cross axis 정렬
→ gap 설정
→ wrap 필요 여부 확인
→ item grow / shrink 검토
→ responsive viewport 확인
```

---

### [FAQ]

Q. Flexbox가 뭐야?
A. 행 또는 열 한 방향을 기준으로 요소를 정렬하고 배치하는 CSS 1차원 Layout 방식이다.

Q. Flexbox는 언제 써?
A. 버튼 정렬, 카드 내부 정렬, Header Navigation, 중앙 정렬, Icon + Text 정렬에 사용한다.

Q. Flexbox는 1차원 Layout이야?
A. 맞다. row 또는 column 한 방향 중심의 Layout에 적합하다.

Q. Flexbox와 Grid 중 뭐를 써야 해?
A. 한 방향 정렬은 Flexbox, 행과 열이 모두 중요한 2차원 배치는 Grid가 적합하다.

---

# 2. Flex Container and Flex Item

## 2.1 Flex Container

### [개념]

Flex Container는 `display: flex` 또는 `display: inline-flex`가 적용된 부모 요소다.

Flex Container는 직접 자식 요소들을 Flex Item으로 배치한다.

예:

```html
<div class="button-group">
  <button type="button">Cancel</button>
  <button type="submit">Save</button>
</div>
```

```css
.button-group {
  display: flex;
  gap: 12px;
}
```

---

### [핵심]

Flex Container 핵심:

- `display: flex`를 적용한 요소다.
- 직접 자식 요소만 Flex Item이 된다.
- 손자 요소는 직접 Flex Item이 아니다.
- Main Axis와 Cross Axis를 만든다.
- 정렬과 간격은 주로 Container에서 제어한다.
- `display: inline-flex`는 inline 흐름을 유지하면서 Flex Layout을 만든다.

---

### [실무]

Flex Container는 반복 요소 또는 정렬 대상의 부모에 적용한다.

좋은 예:

```css
.card-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
```

나쁜 예:

```css
.card-actions button {
  display: flex;
}
```

위 예는 버튼 내부 정렬에는 의미가 있지만, 버튼들 사이 정렬에는 부족하다.

검수 기준:

- 정렬하려는 요소들의 부모에 `display: flex`를 적용했는가?
- Flex Item이 직접 자식인가?
- 손자 요소를 Flex Item처럼 착각하지 않았는가?
- Container 책임과 Item 책임을 구분했는가?

---

### [FAQ]

Q. Flex Container가 뭐야?
A. `display: flex`가 적용되어 자식 요소를 Flex Item으로 배치하는 부모 요소다.

Q. Flex Item은 어떤 요소야?
A. Flex Container의 직접 자식 요소다.

Q. 손자 요소도 Flex Item이 돼?
A. 아니다. Flex Container의 직접 자식만 Flex Item이 된다.

Q. 버튼 여러 개를 정렬하려면 어디에 display flex를 줘?
A. 버튼들을 감싸는 부모 요소에 `display: flex`를 준다.

---

## 2.2 Flex Item

### [개념]

Flex Item은 Flex Container의 직접 자식 요소다.

Flex Item은 Container의 Main Axis와 Cross Axis 기준으로 배치된다.

---

### [핵심]

Flex Item 핵심:

- Flex Container의 직접 자식이다.
- `flex-grow`로 남은 공간을 얼마나 차지할지 정한다.
- `flex-shrink`로 줄어들 수 있는 정도를 정한다.
- `flex-basis`로 기본 크기를 정한다.
- `align-self`로 개별 Cross Axis 정렬을 바꿀 수 있다.
- 기본적으로 `min-width: auto` 특성 때문에 overflow가 발생할 수 있다.
- 긴 텍스트가 있는 Flex Item에는 `min-width: 0`이 필요할 수 있다.

---

### [실무]

Flex Item 크기 문제는 실무에서 자주 발생한다.

긴 텍스트 overflow 예:

```html
<div class="media">
  <img src="thumb.jpg" alt="" />
  <div class="media-content">
    <h2>Very long festival title that should shrink correctly</h2>
  </div>
</div>
```

```css
.media {
  display: flex;
  gap: 12px;
}

.media-content {
  min-width: 0;
}

.media-content h2 {
  overflow-wrap: break-word;
}
```

검수 기준:

- Flex Item이 줄어들어야 하는가?
- 긴 텍스트가 있는 Item에 `min-width: 0`이 필요한가?
- Item별 크기 분배가 명확한가?
- `flex: 1`을 무분별하게 사용하지 않았는가?
- `align-self`가 필요한 개별 Item만 사용하는가?

---

### [FAQ]

Q. Flex Item이 뭐야?
A. Flex Container의 직접 자식 요소다.

Q. Flex Item이 부모 밖으로 나가는 이유는?
A. 기본 `min-width: auto` 또는 고정 width, 긴 텍스트 때문에 줄어들지 못하기 때문일 수 있다.

Q. Flex Item에 min-width 0은 언제 써?
A. 긴 텍스트가 있는 Flex Item이 줄어들지 않아 overflow가 발생할 때 사용한다.

Q. flex: 1은 무슨 뜻이야?
A. 일반적으로 Item이 남은 공간을 나누어 차지하도록 만드는 축약 속성이다.

---

# 3. Flex Axis

## 3.1 Main Axis and Cross Axis

### [개념]

Flexbox는 Main Axis와 Cross Axis를 기준으로 요소를 배치한다.

Main Axis는 `flex-direction`이 결정하는 주 방향이다.

Cross Axis는 Main Axis에 수직인 보조 방향이다.

---

### [핵심]

Axis 핵심:

- Main Axis는 Flex Item이 배치되는 주 방향이다.
- Cross Axis는 Main Axis의 수직 방향이다.
- `flex-direction: row`이면 Main Axis는 가로 방향이다.
- `flex-direction: column`이면 Main Axis는 세로 방향이다.
- `justify-content`는 Main Axis 정렬이다.
- `align-items`는 Cross Axis 정렬이다.
- Main Axis와 Cross Axis는 화면 가로/세로가 아니라 flex-direction에 따라 달라진다.

---

### [실무]

Axis 이해는 Flexbox 정렬 오류를 줄인다.

row 기준:

```text
flex-direction: row
Main Axis → horizontal
Cross Axis → vertical
justify-content → horizontal alignment
align-items → vertical alignment
```

column 기준:

```text
flex-direction: column
Main Axis → vertical
Cross Axis → horizontal
justify-content → vertical alignment
align-items → horizontal alignment
```

검수 기준:

- flex-direction을 먼저 확인했는가?
- justify-content가 어느 축에 적용되는지 이해했는가?
- align-items가 어느 축에 적용되는지 이해했는가?
- row와 column에서 정렬 방향이 바뀌는 것을 고려했는가?

---

### [FAQ]

Q. Main Axis가 뭐야?
A. Flex Item이 배치되는 주 방향이며 `flex-direction`이 결정한다.

Q. Cross Axis가 뭐야?
A. Main Axis에 수직인 방향이다.

Q. justify-content는 어느 방향 정렬이야?
A. Main Axis 방향 정렬이다.

Q. align-items는 어느 방향 정렬이야?
A. Cross Axis 방향 정렬이다.

---

# 4. Flex Direction

## 4.1 flex-direction

### [개념]

`flex-direction`은 Flex Item이 배치되는 Main Axis 방향을 결정하는 CSS property다.

대표 값:

```css
flex-direction: row;
flex-direction: column;
flex-direction: row-reverse;
flex-direction: column-reverse;
```

---

### [핵심]

`flex-direction` 핵심:

- 기본값은 `row`다.
- `row`는 가로 방향 배치다.
- `column`은 세로 방향 배치다.
- `row-reverse`는 가로 역방향 배치다.
- `column-reverse`는 세로 역방향 배치다.
- reverse 값은 시각 순서와 DOM 순서를 다르게 만들 수 있다.
- 접근성과 keyboard navigation을 고려해야 한다.

---

### [실무]

일반적인 사용:

```css
.nav-menu {
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.form-stack {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
```

Responsive 전환 예:

```css
.filter-bar {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

@media (min-width: 768px) {
  .filter-bar {
    flex-direction: row;
    align-items: center;
  }
}
```

검수 기준:

- row와 column 중 UI 목적에 맞는 방향인가?
- reverse 값으로 DOM 순서와 시각 순서가 어긋나지 않는가?
- 모바일에서는 column, 데스크톱에서는 row가 더 적절한가?
- direction 변경 후 justify-content와 align-items 의미를 다시 확인했는가?

---

### [FAQ]

Q. flex-direction은 뭐야?
A. Flex Item이 배치되는 Main Axis 방향을 결정하는 property다.

Q. flex-direction 기본값은 뭐야?
A. 기본값은 `row`다.

Q. column을 쓰면 justify-content 방향도 바뀌어?
A. 맞다. column에서는 Main Axis가 세로 방향이므로 justify-content도 세로 방향 정렬이 된다.

Q. row-reverse를 써도 돼?
A. 가능하지만 시각 순서와 DOM 순서가 달라질 수 있어 접근성을 검토해야 한다.

---

# 5. Justify Content

## 5.1 justify-content

### [개념]

`justify-content`는 Flex Container의 Main Axis 방향에서 Flex Item을 정렬하는 CSS property다.

대표 값:

```css
justify-content: flex-start;
justify-content: center;
justify-content: flex-end;
justify-content: space-between;
justify-content: space-around;
justify-content: space-evenly;
```

---

### [핵심]

`justify-content` 핵심:

- Main Axis 방향 정렬을 담당한다.
- `flex-start`는 Main Axis 시작점 정렬이다.
- `center`는 Main Axis 중앙 정렬이다.
- `flex-end`는 Main Axis 끝점 정렬이다.
- `space-between`은 양 끝에 붙이고 사이 공간을 균등 분배한다.
- `space-around`는 각 Item 양쪽에 공간을 만든다.
- `space-evenly`는 모든 공간을 균등하게 만든다.
- 남은 공간이 있어야 효과가 명확하다.

---

### [실무]

Header Navigation 예:

```css
.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

Button Group 오른쪽 정렬 예:

```css
.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
```

중앙 정렬 예:

```css
.empty-state {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

검수 기준:

- Main Axis 방향을 정확히 이해했는가?
- 남은 공간이 있는 상태인가?
- `gap`이 더 적절한 간격 문제를 `space-between`으로 억지 해결하지 않았는가?
- Header 양끝 정렬에 `space-between`을 사용했는가?
- 버튼 그룹 정렬에 `flex-end`가 적절한가?

---

### [FAQ]

Q. justify-content는 뭐야?
A. Flex Item을 Main Axis 방향으로 정렬하는 property다.

Q. justify-content center는 언제 써?
A. Main Axis 방향 중앙 정렬이 필요할 때 사용한다.

Q. space-between은 언제 써?
A. 양 끝 요소를 끝에 붙이고 사이 공간을 균등하게 벌릴 때 사용한다.

Q. justify-content가 안 먹는 이유는?
A. 남은 공간이 없거나 Main Axis 방향을 잘못 이해했기 때문일 수 있다.

---

# 6. Align Items

## 6.1 align-items

### [개념]

`align-items`는 Flex Container의 Cross Axis 방향에서 Flex Item을 정렬하는 CSS property다.

대표 값:

```css
align-items: stretch;
align-items: flex-start;
align-items: center;
align-items: flex-end;
align-items: baseline;
```

---

### [핵심]

`align-items` 핵심:

- Cross Axis 방향 정렬을 담당한다.
- 기본값은 `stretch`다.
- `center`는 Cross Axis 중앙 정렬이다.
- `flex-start`는 Cross Axis 시작점 정렬이다.
- `flex-end`는 Cross Axis 끝점 정렬이다.
- `baseline`은 텍스트 기준선 정렬이다.
- `stretch`는 Item을 Cross Axis 방향으로 늘릴 수 있다.
- Item에 고정 크기가 있으면 stretch 효과가 제한될 수 있다.

---

### [실무]

Icon + Text 정렬 예:

```css
.icon-text {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
```

Header 세로 중앙 정렬 예:

```css
.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
```

Card Footer 정렬 예:

```css
.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
```

검수 기준:

- Cross Axis 방향을 정확히 이해했는가?
- 세로 중앙 정렬에 `align-items: center`가 적절한가?
- Item 높이가 서로 달라 baseline 정렬이 필요한가?
- stretch 때문에 Item 높이가 의도치 않게 늘어나지 않았는가?
- 개별 Item만 다르게 정렬하려면 `align-self`가 더 적절한가?

---

### [FAQ]

Q. align-items는 뭐야?
A. Flex Item을 Cross Axis 방향으로 정렬하는 property다.

Q. align-items center는 언제 써?
A. Cross Axis 방향 중앙 정렬이 필요할 때 사용한다.

Q. justify-content와 align-items 차이는 뭐야?
A. justify-content는 Main Axis 정렬이고 align-items는 Cross Axis 정렬이다.

Q. align-items 기본값은 뭐야?
A. 기본값은 `stretch`다.

---

## 6.2 align-self

### [개념]

`align-self`는 개별 Flex Item의 Cross Axis 정렬을 따로 지정하는 CSS property다.

Container의 `align-items` 값을 특정 Item에서만 override할 수 있다.

---

### [핵심]

`align-self` 핵심:

- 개별 Flex Item에 적용한다.
- Cross Axis 정렬을 개별적으로 제어한다.
- `auto`, `flex-start`, `center`, `flex-end`, `stretch`, `baseline` 값을 사용할 수 있다.
- 전체 정렬은 `align-items`, 개별 정렬은 `align-self`로 처리한다.
- 남용하면 Layout 일관성이 떨어질 수 있다.

---

### [실무]

예:

```css
.card-row {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.card-action {
  align-self: center;
}
```

사용 적합:

- 하나의 버튼만 중앙 정렬
- 특정 Badge만 상단 정렬
- 특정 Image만 높이 stretch 방지
- Card 내부 일부 Item 위치 조정

검수 기준:

- 전체 정렬이 아니라 특정 Item만 다르게 정렬해야 하는가?
- `align-items`로 해결 가능한 문제를 `align-self`로 복잡하게 만들지 않았는가?
- 개별 정렬이 시각적 일관성을 해치지 않는가?

---

### [FAQ]

Q. align-self는 뭐야?
A. 개별 Flex Item의 Cross Axis 정렬을 따로 지정하는 property다.

Q. align-items와 align-self 차이는 뭐야?
A. align-items는 모든 Item에 적용되고 align-self는 특정 Item에만 적용된다.

Q. align-self는 언제 써?
A. 하나의 Flex Item만 다른 Cross Axis 정렬이 필요할 때 사용한다.

---

# 7. Gap

## 7.1 gap

### [개념]

`gap`은 Flex Item 사이의 간격을 지정하는 CSS property다.

Flexbox와 Grid에서 모두 사용할 수 있다.

예:

```css
.button-group {
  display: flex;
  gap: 12px;
}
```

---

### [핵심]

`gap` 핵심:

- Flex Item 사이 간격을 만든다.
- margin보다 반복 요소 간격 관리가 단순하다.
- 첫 번째 / 마지막 Item의 불필요한 외부 margin 문제가 없다.
- row gap과 column gap을 따로 지정할 수 있다.
- `row-gap`, `column-gap` 사용 가능
- Flex Wrap과 함께 사용하면 줄 간격도 관리할 수 있다.

예:

```css
.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
}
```

---

### [실무]

반복 요소 간격은 margin보다 gap을 우선 고려한다.

좋은 예:

```css
.card-actions {
  display: flex;
  gap: 8px;
}
```

복잡한 margin 예:

```css
.card-actions button + button {
  margin-left: 8px;
}
```

검수 기준:

- 반복 요소 사이 간격에 gap을 사용했는가?
- Item 자체 margin으로 간격을 복잡하게 만들지 않았는가?
- wrap이 있을 때 row-gap과 column-gap을 고려했는가?
- margin collapse 문제를 gap으로 대체할 수 있는가?

---

### [FAQ]

Q. gap은 뭐야?
A. Flex Item 또는 Grid Item 사이 간격을 지정하는 CSS property다.

Q. Flexbox에서 gap을 써도 돼?
A. 가능하다. 현대 브라우저에서는 Flexbox gap을 사용할 수 있다.

Q. gap과 margin 중 뭐가 좋아?
A. 반복 요소 사이 간격은 gap이 더 명확하고 관리하기 쉬운 경우가 많다.

Q. gap으로 줄 간격도 조절돼?
A. flex-wrap이 있는 경우 row-gap과 column-gap으로 줄 간격과 열 간격을 조절할 수 있다.

---

# 8. Flex Wrap

## 8.1 flex-wrap

### [개념]

`flex-wrap`은 Flex Item이 한 줄에 들어가지 않을 때 줄바꿈할지 결정하는 CSS property다.

대표 값:

```css
flex-wrap: nowrap;
flex-wrap: wrap;
flex-wrap: wrap-reverse;
```

---

### [핵심]

`flex-wrap` 핵심:

- 기본값은 `nowrap`이다.
- `nowrap`은 한 줄에 계속 배치하려고 한다.
- `wrap`은 공간이 부족하면 다음 줄로 넘긴다.
- `wrap-reverse`는 줄바꿈 방향을 반대로 한다.
- Tag List, Filter Chip, Button Group, Card Row에 유용하다.
- wrap이 없으면 overflow가 발생할 수 있다.

---

### [실무]

Tag List 예:

```css
.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
```

Filter Bar 예:

```css
.filter-options {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
```

검수 기준:

- Item이 작은 화면에서 한 줄에 다 들어가는가?
- overflow가 생기면 `flex-wrap: wrap`이 필요한가?
- wrap 후 줄 간격이 gap으로 관리되는가?
- wrap이 아니라 horizontal scroll이 더 적절한 UI인가?
- 각 Item의 최소 너비가 너무 크지 않은가?

---

### [FAQ]

Q. flex-wrap은 뭐야?
A. Flex Item이 한 줄에 들어가지 않을 때 줄바꿈할지 결정하는 property다.

Q. flex-wrap 기본값은 뭐야?
A. 기본값은 `nowrap`이다.

Q. 모바일에서 Flex Item이 삐져나가면 뭘 확인해?
A. `flex-wrap`, fixed width, min-width, gap, overflow를 확인한다.

Q. tag list에는 flex-wrap이 좋아?
A. 좋다. 태그 개수가 많아질 때 자연스럽게 줄바꿈할 수 있다.

---

# 9. Flex Grow Shrink Basis

## 9.1 flex-grow

### [개념]

`flex-grow`는 Flex Container의 남은 공간을 Flex Item이 얼마나 차지할지 결정하는 CSS property다.

값은 비율을 의미한다.

---

### [핵심]

`flex-grow` 핵심:

- 기본값은 `0`이다.
- `0`이면 남은 공간을 차지하지 않는다.
- `1`이면 남은 공간을 비율에 따라 차지한다.
- 여러 Item이 grow 값을 가지면 비율대로 남은 공간을 나눈다.
- grow는 남은 공간이 있을 때 동작한다.
- 무분별한 grow 사용은 예상치 못한 Item 확대를 만든다.

예:

```css
.search-input {
  flex-grow: 1;
}
```

---

### [실무]

Search Bar 예:

```html
<form class="search-bar">
  <input type="search" name="keyword" />
  <button type="submit">Search</button>
</form>
```

```css
.search-bar {
  display: flex;
  gap: 8px;
}

.search-bar input {
  flex-grow: 1;
  min-width: 0;
}
```

검수 기준:

- 남은 공간을 차지해야 하는 Item인가?
- 모든 Item에 flex-grow를 줘도 되는가?
- input이나 content 영역만 커지는 것이 의도인가?
- grow로 인해 버튼이나 아이콘이 비정상적으로 커지지 않는가?

---

### [FAQ]

Q. flex-grow는 뭐야?
A. Flex Container의 남은 공간을 Flex Item이 얼마나 차지할지 결정하는 property다.

Q. flex-grow 기본값은 뭐야?
A. 기본값은 `0`이다.

Q. input을 남은 공간만큼 늘리려면 어떻게 해?
A. input에 `flex-grow: 1` 또는 `flex: 1`을 사용할 수 있다.

---

## 9.2 flex-shrink

### [개념]

`flex-shrink`는 Flex Container 공간이 부족할 때 Flex Item이 얼마나 줄어들 수 있는지 결정하는 CSS property다.

---

### [핵심]

`flex-shrink` 핵심:

- 기본값은 `1`이다.
- `1`이면 공간 부족 시 줄어들 수 있다.
- `0`이면 줄어들지 않는다.
- 고정 크기 아이콘이나 버튼에는 `flex-shrink: 0`을 사용할 수 있다.
- 텍스트 영역은 줄어들 수 있도록 `min-width: 0`과 함께 검토한다.
- shrink와 min-width는 함께 고려해야 한다.

예:

```css
.avatar {
  flex-shrink: 0;
}
```

---

### [실무]

Media Object 예:

```css
.media {
  display: flex;
  gap: 12px;
}

.media-thumbnail {
  width: 80px;
  height: 80px;
  flex-shrink: 0;
}

.media-content {
  min-width: 0;
}
```

검수 기준:

- 줄어들면 안 되는 Item에 `flex-shrink: 0`이 필요한가?
- 텍스트 영역은 줄어들 수 있게 설정했는가?
- Item이 줄어들지 않아 overflow를 만드는가?
- fixed width와 shrink 설정이 충돌하지 않는가?

---

### [FAQ]

Q. flex-shrink는 뭐야?
A. 공간이 부족할 때 Flex Item이 얼마나 줄어들 수 있는지 결정하는 property다.

Q. flex-shrink 기본값은 뭐야?
A. 기본값은 `1`이다.

Q. 이미지나 아이콘이 찌그러지지 않게 하려면?
A. 필요한 경우 `flex-shrink: 0`을 사용할 수 있다.

Q. flex item이 줄어들지 않는 이유는?
A. `min-width: auto`, 고정 width, 긴 텍스트, `flex-shrink: 0` 때문일 수 있다.

---

## 9.3 flex-basis

### [개념]

`flex-basis`는 Flex Item의 기본 크기를 지정하는 CSS property다.

Flexbox에서 공간 분배가 시작되기 전 기준 크기다.

---

### [핵심]

`flex-basis` 핵심:

- Flex Item의 초기 크기를 지정한다.
- 기본값은 `auto`다.
- width보다 Flex Layout에서 우선적으로 고려될 수 있다.
- `0`으로 설정하면 grow 비율 중심의 분배가 쉬워진다.
- `flex` 축약 속성 안에 포함된다.
- row 방향에서는 가로 기준, column 방향에서는 세로 기준이 된다.

예:

```css
.sidebar {
  flex-basis: 240px;
}
```

---

### [실무]

Sidebar Layout 예:

```css
.layout {
  display: flex;
  gap: 24px;
}

.sidebar {
  flex: 0 0 240px;
}

.content {
  flex: 1;
  min-width: 0;
}
```

Equal Column 예:

```css
.equal-item {
  flex: 1 1 0;
}
```

검수 기준:

- 기준 크기가 width가 아니라 flex-basis여야 하는가?
- Sidebar처럼 고정 기준 크기가 필요한가?
- Equal Column이 필요한가?
- flex-direction 변경 시 flex-basis 기준 방향을 다시 확인했는가?

---

### [FAQ]

Q. flex-basis는 뭐야?
A. Flex Item의 공간 분배 전 기본 크기를 지정하는 property다.

Q. flex-basis 기본값은 뭐야?
A. 기본값은 `auto`다.

Q. flex-basis와 width 차이는 뭐야?
A. flex-basis는 Flex Layout 안에서 Item의 기준 크기로 사용되고 width보다 우선 고려될 수 있다.

---

## 9.4 flex Shorthand

### [개념]

`flex`는 `flex-grow`, `flex-shrink`, `flex-basis`를 한 번에 지정하는 축약 속성이다.

기본 구조:

```css
.item {
  flex: grow shrink basis;
}
```

예:

```css
.item {
  flex: 1 1 0;
}
```

---

### [핵심]

`flex` 축약 핵심:

- `flex: 1`은 자주 사용되지만 정확한 의미를 이해해야 한다.
- `flex: 1`은 보통 Item이 남은 공간을 나누어 차지하도록 만든다.
- `flex: 0 0 auto`는 크기 고정 성격이다.
- `flex: 0 0 240px`는 240px 기준 크기를 유지한다.
- `flex: 1 1 0`은 균등 분배에 자주 사용한다.
- 축약 속성은 편하지만 의도를 명확히 해야 한다.

---

### [실무]

자주 쓰는 패턴:

```css
.content {
  flex: 1;
  min-width: 0;
}

.sidebar {
  flex: 0 0 240px;
}

.equal-column {
  flex: 1 1 0;
}

.fixed-icon {
  flex: 0 0 auto;
}
```

검수 기준:

- `flex: 1`을 왜 사용하는지 명확한가?
- 고정 영역과 유동 영역이 구분되는가?
- basis가 auto인지 0인지 의도했는가?
- overflow 방지를 위해 `min-width: 0`이 필요한가?

---

### [FAQ]

Q. flex 속성은 뭐야?
A. `flex-grow`, `flex-shrink`, `flex-basis`를 한 번에 지정하는 축약 속성이다.

Q. flex 1은 무슨 뜻이야?
A. 일반적으로 Flex Item이 남은 공간을 나누어 차지하도록 만드는 설정이다.

Q. sidebar 고정 너비는 어떻게 해?
A. 예를 들어 `flex: 0 0 240px`처럼 설정할 수 있다.

Q. flex 1을 쓰면 항상 좋아?
A. 아니다. Item이 의도치 않게 늘거나 줄 수 있으므로 목적을 확인해야 한다.

---

# 10. Align Content

## 10.1 align-content

### [개념]

`align-content`는 여러 줄로 wrapping된 Flex Line들을 Cross Axis 방향으로 정렬하는 property다.

`flex-wrap: wrap`이 있고 Flex Line이 여러 줄일 때 의미가 있다.

---

### [핵심]

`align-content` 핵심:

- 여러 Flex Line의 Cross Axis 정렬을 담당한다.
- 한 줄 Flex Layout에서는 효과가 거의 없다.
- `flex-wrap: wrap` 상태에서 의미가 있다.
- `align-items`는 각 줄 안의 Item 정렬이다.
- `align-content`는 줄 전체 묶음의 정렬이다.
- Container에 남은 Cross Axis 공간이 있어야 효과가 명확하다.

대표 값:

```css
align-content: flex-start;
align-content: center;
align-content: space-between;
align-content: stretch;
```

---

### [실무]

Wrap Layout 예:

```css
.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  gap: 8px;
  min-height: 160px;
}
```

검수 기준:

- Flex Item이 여러 줄로 wrap되는가?
- Container에 Cross Axis 남은 공간이 있는가?
- 줄 안의 Item 정렬 문제라면 align-items가 더 적절하지 않은가?
- 줄 전체 배치 문제인지 확인했는가?

---

### [FAQ]

Q. align-content는 뭐야?
A. 여러 줄로 wrapping된 Flex Line들을 Cross Axis 방향으로 정렬하는 property다.

Q. align-content가 안 먹는 이유는?
A. Flex Line이 한 줄이거나 `flex-wrap`이 없거나 남은 Cross Axis 공간이 없기 때문일 수 있다.

Q. align-items와 align-content 차이는 뭐야?
A. align-items는 Item 정렬이고 align-content는 여러 줄 전체 정렬이다.

---

# 11. Common Flexbox Patterns

## 11.1 Center Alignment

### [개념]

Flexbox Center Alignment는 요소를 가로와 세로 중앙에 배치하는 대표 패턴이다.

---

### [핵심]

중앙 정렬 핵심:

- `display: flex`
- `justify-content: center`
- `align-items: center`
- Container에 높이 또는 공간이 있어야 세로 중앙 정렬이 보인다.
- inline 요소 내부 정렬에는 `inline-flex`를 사용할 수 있다.

예:

```css
.center-box {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 240px;
}
```

---

### [실무]

Empty State 예:

```html
<section class="empty-state">
  <p>No festivals found.</p>
</section>
```

```css
.empty-state {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 240px;
  text-align: center;
}
```

검수 기준:

- Container에 충분한 높이가 있는가?
- Main Axis와 Cross Axis를 정확히 이해했는가?
- 텍스트 중앙 정렬이 필요한 경우 `text-align: center`도 적용했는가?
- column 방향에서는 justify-content와 align-items 방향이 바뀌는가?

---

### [FAQ]

Q. Flexbox로 가운데 정렬은 어떻게 해?
A. Container에 `display: flex`, `justify-content: center`, `align-items: center`를 적용한다.

Q. 세로 중앙 정렬이 안 되는 이유는?
A. Container에 높이나 남은 세로 공간이 없기 때문일 수 있다.

Q. 텍스트도 가운데 정렬하려면?
A. Flex 정렬과 별도로 `text-align: center`가 필요할 수 있다.

---

## 11.2 Header Layout

### [개념]

Header Layout은 로고, Navigation, Action Button을 가로로 정렬하는 대표 Flexbox 패턴이다.

---

### [핵심]

Header Layout 핵심:

- Header 내부를 Flex Container로 구성한다.
- 로고와 메뉴를 양끝 정렬할 수 있다.
- Navigation 내부도 Flexbox로 정렬할 수 있다.
- `align-items: center`로 세로 중앙 정렬한다.
- 모바일에서는 column 또는 menu toggle 구조로 전환할 수 있다.

---

### [실무]

기본 Header 예:

```html
<header class="site-header">
  <a class="site-logo" href="/">FestaPick</a>

  <nav aria-label="Main Navigation">
    <ul class="nav-list">
      <li><a href="/festivals">Festivals</a></li>
      <li><a href="/calendar">Calendar</a></li>
    </ul>
  </nav>
</header>
```

```css
.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
}

.nav-list {
  display: flex;
  gap: 16px;
  list-style: none;
  margin: 0;
  padding: 0;
}
```

검수 기준:

- Header 내부 주요 영역이 flex로 정렬되는가?
- Navigation list가 ul/li 구조를 유지하는가?
- nav item 간격을 gap으로 관리하는가?
- 모바일에서 메뉴가 깨지지 않는가?
- 로고와 메뉴의 accessible name이 명확한가?

---

### [FAQ]

Q. Header Layout에 Flexbox를 써도 돼?
A. 적합하다. 로고, 메뉴, 버튼을 한 방향으로 정렬하기 좋다.

Q. Header에서 space-between은 언제 써?
A. 로고와 메뉴 또는 액션 영역을 양끝에 배치할 때 사용한다.

Q. nav 메뉴 간격은 margin과 gap 중 뭐가 좋아?
A. Flexbox에서는 gap이 더 명확하고 관리하기 쉬운 경우가 많다.

---

## 11.3 Icon Text Alignment

### [개념]

Icon Text Alignment는 아이콘과 텍스트를 한 줄에서 자연스럽게 정렬하는 Flexbox 패턴이다.

---

### [핵심]

Icon Text Alignment 핵심:

- `display: inline-flex`를 자주 사용한다.
- `align-items: center`로 세로 중앙 정렬한다.
- `gap`으로 아이콘과 텍스트 간격을 만든다.
- 아이콘은 `flex-shrink: 0`이 필요할 수 있다.
- 아이콘만으로 의미를 전달하지 않는다.

---

### [실무]

Button 예:

```html
<button class="icon-button" type="button">
  <span aria-hidden="true">🔍</span>
  <span>Search</span>
</button>
```

```css
.icon-button {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.icon-button [aria-hidden="true"] {
  flex-shrink: 0;
}
```

검수 기준:

- icon과 text가 세로 중앙 정렬되는가?
- icon과 text 사이 간격이 gap으로 관리되는가?
- 아이콘만 있는 버튼에 accessible name이 있는가?
- 아이콘이 줄어들거나 찌그러지지 않는가?

---

### [FAQ]

Q. 아이콘과 텍스트 정렬은 어떻게 해?
A. 부모에 `display: inline-flex`, `align-items: center`, `gap`을 적용한다.

Q. 아이콘만 있는 버튼은 어떻게 접근성을 처리해?
A. `aria-label` 또는 숨김 텍스트로 버튼 이름을 제공한다.

Q. 아이콘이 찌그러지면 어떻게 해?
A. 아이콘 요소에 `flex-shrink: 0`을 적용할 수 있다.

---

## 11.4 Form Row

### [개념]

Form Row는 label, input, button 또는 여러 Form Field를 한 줄로 정렬하는 Flexbox 패턴이다.

---

### [핵심]

Form Row 핵심:

- 검색창 + 버튼 구조에 적합하다.
- input은 남은 공간을 차지하게 만들 수 있다.
- button은 고정 크기 또는 내용 크기를 유지할 수 있다.
- 모바일에서는 column으로 전환할 수 있다.
- input overflow 방지를 위해 `min-width: 0`을 고려한다.

---

### [실무]

Search Form 예:

```html
<form class="search-form">
  <label class="visually-hidden" for="keyword">Keyword</label>
  <input id="keyword" name="keyword" type="search" />
  <button type="submit">Search</button>
</form>
```

```css
.search-form {
  display: flex;
  gap: 8px;
}

.search-form input {
  flex: 1;
  min-width: 0;
}

.search-form button {
  flex-shrink: 0;
}

@media (max-width: 480px) {
  .search-form {
    flex-direction: column;
  }
}
```

검수 기준:

- input과 button이 한 줄에 정렬되는가?
- input이 남은 공간을 차지하는가?
- button이 줄어들지 않는가?
- 모바일에서 column 전환이 필요한가?
- label 접근성이 유지되는가?

---

### [FAQ]

Q. 검색창과 버튼을 한 줄로 만들려면?
A. form에 `display: flex`, input에 `flex: 1`, button에 `flex-shrink: 0`을 사용할 수 있다.

Q. input이 너무 커져서 버튼을 밀어내면?
A. input에 `min-width: 0`을 적용하고 button에 `flex-shrink: 0`을 검토한다.

Q. 모바일에서 Form Row는 어떻게 처리해?
A. 작은 화면에서는 `flex-direction: column`으로 전환할 수 있다.

---

# 12. Responsive Flexbox

## 12.1 Responsive Flex Layout

### [개념]

Responsive Flexbox는 화면 크기에 따라 Flex 방향, 줄바꿈, 간격, Item 크기를 조정하는 방식이다.

---

### [핵심]

Responsive Flexbox 핵심:

- 모바일에서는 column이 적합한 경우가 많다.
- 데스크톱에서는 row가 적합한 경우가 많다.
- `flex-wrap: wrap`으로 자연스러운 줄바꿈을 만들 수 있다.
- `gap`은 반응형 간격 관리에 유용하다.
- `flex-basis`와 media query를 함께 사용할 수 있다.
- 고정 width보다 유연한 basis와 max-width가 안정적이다.

---

### [실무]

Mobile First 예:

```css
.feature-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

@media (min-width: 768px) {
  .feature-list {
    flex-direction: row;
  }

  .feature-list > * {
    flex: 1;
  }
}
```

Wrap Card 예:

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}

.card-list > li {
  flex: 1 1 280px;
}
```

검수 기준:

- Mobile First로 기본 Layout을 작성했는가?
- 작은 화면에서 row가 무리하게 유지되지 않는가?
- wrap이 필요한 곳에 적용했는가?
- flex-basis가 너무 커서 overflow를 만들지 않는가?
- gap이 화면 크기에 맞게 조정되는가?

---

### [FAQ]

Q. Responsive Flexbox는 어떻게 작성해?
A. Mobile First로 column 또는 wrap 구조를 기본으로 하고 media query에서 row 또는 item 크기를 조정한다.

Q. 모바일에서는 flex-direction을 column으로 바꿔도 돼?
A. 가능하다. 좁은 화면에서는 column 배치가 더 자연스러운 경우가 많다.

Q. 카드 목록을 Flexbox로 반응형 처리할 수 있어?
A. 가능하다. `flex-wrap: wrap`과 `flex: 1 1 280px` 같은 패턴을 사용할 수 있다.

---

# 13. Flexbox Troubleshooting

## 13.1 Flexbox Layout Broken

### [개념]

Flexbox Layout Broken은 Flex Item이 예상 위치, 크기, 줄바꿈, 정렬과 다르게 배치되는 문제다.

주요 원인은 Axis 오해, min-width 문제, wrap 누락, shrink/grow 오용, gap/space 혼동이다.

---

### [핵심]

주요 문제:

- justify-content와 align-items 축 혼동
- flex-direction 변경 후 정렬 방향 착각
- flex-wrap 누락으로 overflow 발생
- Flex Item 기본 `min-width: auto`로 overflow 발생
- `flex: 1` 남용으로 Item이 과도하게 늘어남
- `flex-shrink: 0` 남용으로 Item이 줄어들지 않음
- Container가 아니라 Item에 flex를 적용
- 직접 자식이 아닌 요소를 Flex Item으로 착각
- `space-between`으로 간격을 억지 조절
- `align-content`를 한 줄 Layout에 사용

---

### [실무]

Debug Flow:

```text
Flex Container Inspect
→ display flex 확인
→ 직접 자식 Flex Item 확인
→ flex-direction 확인
→ Main Axis / Cross Axis 확인
→ justify-content / align-items 확인
→ gap 확인
→ flex-wrap 확인
→ item flex-grow / shrink / basis 확인
→ min-width 0 필요 여부 확인
→ responsive viewport 확인
```

문제 예:

```text
문제: justify-content center가 세로 중앙 정렬이 안 됨
원인: flex-direction row에서 justify-content는 가로 정렬
해결: 세로 중앙은 align-items center 사용
```

```text
문제: 긴 텍스트가 부모 밖으로 나감
원인: Flex Item의 기본 min-width
해결: 텍스트 영역 Item에 min-width: 0 적용
```

```text
문제: 태그 목록이 모바일에서 삐져나감
원인: flex-wrap 누락
해결: flex-wrap: wrap 적용
```

---

### [FAQ]

Q. Flexbox가 안 먹을 때 가장 먼저 볼 것은?
A. 정렬하려는 요소의 부모에 `display: flex`가 적용되어 있는지 확인한다.

Q. justify-content가 원하는 방향으로 안 움직이는 이유는?
A. justify-content는 Main Axis 기준이고 Main Axis는 flex-direction에 따라 달라지기 때문이다.

Q. Flex Item이 줄어들지 않는 이유는?
A. 기본 min-width, 고정 width, 긴 텍스트, flex-shrink 설정 때문일 수 있다.

Q. Flexbox overflow는 어떻게 해결해?
A. flex-wrap, min-width: 0, max-width, overflow-wrap, flex-basis를 확인한다.

---

# 14. Comparison Rules

## 14.1 Flexbox vs Grid

### [개념]

Flexbox는 1차원 Layout에 적합하고 Grid는 2차원 Layout에 적합하다.

---

### [핵심]

| 비교      | Flexbox                            | Grid                            |
| --------- | ---------------------------------- | ------------------------------- |
| 기준      | 1차원 Layout                       | 2차원 Layout                    |
| 방향      | row 또는 column 중심               | row + column                    |
| 적합      | 정렬, navbar, card 내부            | 카드 목록, 갤러리, 대시보드     |
| 공간 분배 | Item 중심                          | Track 중심                      |
| 핵심 속성 | justify-content, align-items, flex | grid-template-columns, grid-row |
| 대표 패턴 | header, button group, form row     | page grid, card grid, dashboard |

---

### [실무]

선택 기준:

```text
Icon + Text → Flexbox
Button Group → Flexbox
Header Navigation → Flexbox
Card Internal Layout → Flexbox
Card List Grid → Grid
Dashboard Layout → Grid
Two-dimensional Gallery → Grid
```

---

### [FAQ]

Q. Flexbox와 Grid 차이는 뭐야?
A. Flexbox는 1차원 배치, Grid는 2차원 배치에 적합하다.

Q. 카드 내부 정렬은 Flexbox가 좋아?
A. 보통 Flexbox가 적합하다.

Q. 카드 목록은 Flexbox와 Grid 중 뭐가 좋아?
A. 행과 열이 중요한 카드 목록은 Grid가 더 적합한 경우가 많다.

---

## 14.2 justify-content vs align-items

### [개념]

`justify-content`는 Main Axis 정렬이고 `align-items`는 Cross Axis 정렬이다.

두 property의 방향은 `flex-direction`에 따라 달라진다.

---

### [핵심]

| flex-direction | justify-content | align-items |
| -------------- | --------------- | ----------- |
| row            | 가로 정렬       | 세로 정렬   |
| column         | 세로 정렬       | 가로 정렬   |

---

### [실무]

선택 기준:

```text
row에서 가로 중앙 → justify-content: center
row에서 세로 중앙 → align-items: center
column에서 세로 중앙 → justify-content: center
column에서 가로 중앙 → align-items: center
```

---

### [FAQ]

Q. justify-content와 align-items 차이는 뭐야?
A. justify-content는 Main Axis 정렬이고 align-items는 Cross Axis 정렬이다.

Q. row에서 세로 중앙 정렬은 무엇을 써?
A. `align-items: center`를 사용한다.

Q. column에서 세로 중앙 정렬은 무엇을 써?
A. `justify-content: center`를 사용한다.

---

## 14.3 gap vs margin

### [개념]

`gap`은 Flex Item 사이 간격을 Container에서 관리하고, `margin`은 개별 요소의 외부 여백을 관리한다.

---

### [핵심]

| 비교            | gap                       | margin                 |
| --------------- | ------------------------- | ---------------------- |
| 적용 위치       | Container                 | Item                   |
| 목적            | Item 사이 간격            | 요소 외부 여백         |
| 반복 간격 관리  | 쉬움                      | 복잡해질 수 있음       |
| 첫/마지막 간격  | 자동으로 불필요 간격 없음 | 별도 처리 필요         |
| Flex/Grid       | 적합                      | 가능하지만 주의        |
| Margin Collapse | 없음                      | vertical collapse 가능 |

---

### [실무]

선택 기준:

```text
Flex Item 사이 간격 → gap
Grid Item 사이 간격 → gap
Section 외부 간격 → margin
Component 내부 여백 → padding
특정 Item만 별도 간격 → margin
```

---

### [FAQ]

Q. gap과 margin 차이는 뭐야?
A. gap은 Container가 Item 사이 간격을 관리하고 margin은 개별 요소의 외부 여백이다.

Q. Flexbox에서는 gap이 좋아?
A. 반복 요소 사이 간격에는 gap이 더 단순하고 명확한 경우가 많다.

Q. 특정 하나의 요소만 밀고 싶으면?
A. 그 경우에는 margin 또는 align-self 같은 개별 Item 제어가 적절할 수 있다.

---

## 14.4 flex-grow vs flex-shrink vs flex-basis

### [개념]

`flex-grow`, `flex-shrink`, `flex-basis`는 Flex Item의 크기 분배를 제어하는 핵심 property다.

---

### [핵심]

| 속성        | 역할                   | 기본값 |
| ----------- | ---------------------- | ------ |
| flex-grow   | 남은 공간 확대 비율    | 0      |
| flex-shrink | 부족한 공간 축소 비율  | 1      |
| flex-basis  | 공간 분배 전 기준 크기 | auto   |

---

### [실무]

선택 기준:

```text
남은 공간을 차지해야 함 → flex-grow
줄어들면 안 되는 아이콘 → flex-shrink: 0
기준 너비가 있는 Sidebar → flex-basis 또는 flex: 0 0 240px
균등 분배 Column → flex: 1 1 0
```

---

### [FAQ]

Q. flex-grow와 flex-shrink 차이는 뭐야?
A. flex-grow는 남은 공간을 차지하는 비율이고 flex-shrink는 부족한 공간에서 줄어드는 비율이다.

Q. flex-basis는 무슨 역할이야?
A. Flex Item의 공간 분배 전 기준 크기를 정한다.

Q. flex 1은 언제 써?
A. Item이 남은 공간을 유동적으로 차지해야 할 때 사용할 수 있다.

---

# 15. Common Mistakes

## 15.1 Flexbox Common Mistakes

### [개념]

Flexbox 실수는 정렬 오류, overflow, 반응형 깨짐, 접근성 순서 문제로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- Flex Container가 아닌 Item에 `display: flex` 적용
- Flex Item이 직접 자식인지 확인하지 않음
- Main Axis와 Cross Axis 혼동
- `justify-content`와 `align-items` 역할 혼동
- `flex-direction: column`에서 정렬 방향 착각
- `flex-wrap` 누락으로 모바일 overflow 발생
- Flex Item `min-width: 0` 누락
- `flex: 1` 무분별한 사용
- `flex-shrink: 0` 남용
- `space-between`으로 모든 간격 문제 해결
- `gap` 대신 복잡한 margin 사용
- `align-content`를 한 줄 Layout에 사용
- reverse 방향으로 DOM 순서와 시각 순서 불일치
- hover 정렬만 고려하고 focus 상태 누락
- 고정 width와 Flexbox를 충돌시킴

---

### [실무]

Troubleshooting Flow:

```text
Flex Bug
→ Container display flex 확인
→ Direct Child Item 확인
→ flex-direction 확인
→ Axis 확인
→ justify / align 확인
→ gap / wrap 확인
→ Item flex 속성 확인
→ min-width / overflow 확인
→ responsive 확인
```

문제 예:

```text
문제: 버튼들이 정렬되지 않음
원인: 버튼 부모가 아니라 버튼 자체에 display flex 적용
해결: 버튼들을 감싸는 부모에 display flex 적용
```

```text
문제: 모바일에서 필터 칩이 화면 밖으로 나감
원인: flex-wrap 없음
해결: flex-wrap: wrap 및 gap 적용
```

```text
문제: 카드 제목이 줄바꿈되지 않고 넘침
원인: Flex Item min-width 기본값
해결: 텍스트 영역에 min-width: 0 및 overflow-wrap 적용
```

---

### [FAQ]

Q. Flexbox에서 가장 흔한 실수는 뭐야?
A. Container와 Item을 혼동하고 justify-content와 align-items 축을 잘못 이해하는 것이다.

Q. 모바일에서 Flex Layout이 깨지는 흔한 이유는?
A. flex-wrap 누락, 고정 width, min-width 문제, gap 미고려 때문이다.

Q. flex-direction column에서 헷갈리는 점은 뭐야?
A. Main Axis가 세로 방향으로 바뀌므로 justify-content도 세로 정렬이 된다는 점이다.

Q. Flexbox 문제는 어떤 순서로 디버깅해?
A. Container, Direct Child, flex-direction, Axis, justify/align, gap/wrap, Item flex 속성, min-width 순서로 확인한다.

---

# 16. Best Practice

## 16.1 Flexbox Best Practice

### [개념]

Flexbox Best Practice는 1차원 정렬, Item 간격, Responsive Wrapping, Component 내부 배치를 안정적으로 구현하기 위한 기준이다.

---

### [핵심]

권장 기준:

- 정렬 대상의 부모에 `display: flex` 적용
- Flex Item이 직접 자식인지 확인
- Main Axis와 Cross Axis 먼저 파악
- `flex-direction` 변경 후 justify / align 방향 재확인
- 반복 요소 간격은 `gap` 우선 고려
- 모바일 overflow 가능성이 있으면 `flex-wrap` 고려
- 긴 텍스트 Flex Item에는 `min-width: 0` 검토
- 고정 아이콘 / 썸네일에는 `flex-shrink: 0` 검토
- Header / Button Group / Icon Text / Form Row에 Flexbox 활용
- 2차원 Layout에는 Grid 검토
- reverse 방향 사용 시 DOM 순서와 접근성 검토
- `flex: 1` 사용 의도 명확히 하기
- `space-between` 남용 금지
- DevTools Flex overlay로 Layout 확인

---

### [실무]

Header 예:

```css
.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}
```

Icon Text 예:

```css
.icon-text {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
```

Search Form 예:

```css
.search-form {
  display: flex;
  gap: 8px;
}

.search-form input {
  flex: 1;
  min-width: 0;
}

.search-form button {
  flex-shrink: 0;
}
```

Responsive Card Row 예:

```css
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
}

.card-list > li {
  flex: 1 1 280px;
}
```

검수 Checklist:

```md
- [ ] 정렬 대상의 부모에 `display: flex`가 있는가?
- [ ] Flex Item이 직접 자식인가?
- [ ] flex-direction이 UI 목적과 맞는가?
- [ ] Main Axis와 Cross Axis를 기준으로 정렬했는가?
- [ ] justify-content와 align-items를 혼동하지 않았는가?
- [ ] Item 간격을 gap으로 관리했는가?
- [ ] 모바일에서 flex-wrap이 필요한가?
- [ ] 긴 텍스트 Item에 min-width: 0이 필요한가?
- [ ] 아이콘 또는 썸네일에 flex-shrink: 0이 필요한가?
- [ ] flex: 1 사용 의도가 명확한가?
- [ ] 2차원 Layout에 Flexbox를 억지로 쓰지 않았는가?
- [ ] reverse 방향 사용 시 접근성을 검토했는가?
```

---

### [FAQ]

Q. Flexbox Best Practice는 뭐야?
A. 부모 Container에 flex를 적용하고 Axis, gap, wrap, Item 크기 제어를 명확히 하여 1차원 Layout을 안정적으로 만드는 것이다.

Q. Flexbox 검수에서 가장 먼저 볼 것은 뭐야?
A. `display: flex`가 정렬 대상의 부모에 적용되었는지와 Flex Item이 직접 자식인지 먼저 확인한다.

Q. Flexbox를 쓰면 안 좋은 경우는?
A. 행과 열이 모두 중요한 2차원 Layout은 Grid가 더 적합하다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Flexbox로 Header, Button Group, Form Row, Card 내부 정렬, Responsive Wrap을 안정적으로 생성하고 디버깅하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Flexbox가 뭐야?
A. 행 또는 열 한 방향을 기준으로 요소를 정렬하고 배치하는 CSS 1차원 Layout 방식이다.

Q. Flexbox는 언제 써?
A. 버튼 정렬, 카드 내부 정렬, Header Navigation, 중앙 정렬, Icon + Text 정렬에 사용한다.

Q. Flexbox는 1차원 Layout이야?
A. 맞다. row 또는 column 한 방향 중심의 Layout에 적합하다.

Q. Flexbox와 Grid 중 뭐를 써야 해?
A. 한 방향 정렬은 Flexbox, 행과 열이 모두 중요한 2차원 배치는 Grid가 적합하다.

Q. Flex Container가 뭐야?
A. `display: flex`가 적용되어 자식 요소를 Flex Item으로 배치하는 부모 요소다.

Q. Flex Item은 어떤 요소야?
A. Flex Container의 직접 자식 요소다.

Q. 손자 요소도 Flex Item이 돼?
A. 아니다. Flex Container의 직접 자식만 Flex Item이 된다.

Q. 버튼 여러 개를 정렬하려면 어디에 display flex를 줘?
A. 버튼들을 감싸는 부모 요소에 `display: flex`를 준다.

Q. Flex Item이 부모 밖으로 나가는 이유는?
A. 기본 `min-width: auto` 또는 고정 width, 긴 텍스트 때문에 줄어들지 못하기 때문일 수 있다.

Q. Flex Item에 min-width 0은 언제 써?
A. 긴 텍스트가 있는 Flex Item이 줄어들지 않아 overflow가 발생할 때 사용한다.

Q. flex: 1은 무슨 뜻이야?
A. 일반적으로 Item이 남은 공간을 나누어 차지하도록 만드는 축약 속성이다.

Q. Main Axis가 뭐야?
A. Flex Item이 배치되는 주 방향이며 `flex-direction`이 결정한다.

Q. Cross Axis가 뭐야?
A. Main Axis에 수직인 방향이다.

Q. justify-content는 어느 방향 정렬이야?
A. Main Axis 방향 정렬이다.

Q. align-items는 어느 방향 정렬이야?
A. Cross Axis 방향 정렬이다.

Q. flex-direction은 뭐야?
A. Flex Item이 배치되는 Main Axis 방향을 결정하는 property다.

Q. flex-direction 기본값은 뭐야?
A. 기본값은 `row`다.

Q. column을 쓰면 justify-content 방향도 바뀌어?
A. 맞다. column에서는 Main Axis가 세로 방향이므로 justify-content도 세로 방향 정렬이 된다.

Q. row-reverse를 써도 돼?
A. 가능하지만 시각 순서와 DOM 순서가 달라질 수 있어 접근성을 검토해야 한다.

Q. justify-content는 뭐야?
A. Flex Item을 Main Axis 방향으로 정렬하는 property다.

Q. justify-content center는 언제 써?
A. Main Axis 방향 중앙 정렬이 필요할 때 사용한다.

Q. space-between은 언제 써?
A. 양 끝 요소를 끝에 붙이고 사이 공간을 균등하게 벌릴 때 사용한다.

Q. justify-content가 안 먹는 이유는?
A. 남은 공간이 없거나 Main Axis 방향을 잘못 이해했기 때문일 수 있다.

Q. align-items는 뭐야?
A. Flex Item을 Cross Axis 방향으로 정렬하는 property다.

Q. align-items center는 언제 써?
A. Cross Axis 방향 중앙 정렬이 필요할 때 사용한다.

Q. justify-content와 align-items 차이는 뭐야?
A. justify-content는 Main Axis 정렬이고 align-items는 Cross Axis 정렬이다.

Q. align-items 기본값은 뭐야?
A. 기본값은 `stretch`다.

Q. align-self는 뭐야?
A. 개별 Flex Item의 Cross Axis 정렬을 따로 지정하는 property다.

Q. align-items와 align-self 차이는 뭐야?
A. align-items는 모든 Item에 적용되고 align-self는 특정 Item에만 적용된다.

Q. gap은 뭐야?
A. Flex Item 또는 Grid Item 사이 간격을 지정하는 CSS property다.

Q. Flexbox에서 gap을 써도 돼?
A. 가능하다. 현대 브라우저에서는 Flexbox gap을 사용할 수 있다.

Q. gap과 margin 중 뭐가 좋아?
A. 반복 요소 사이 간격은 gap이 더 명확하고 관리하기 쉬운 경우가 많다.

Q. flex-wrap은 뭐야?
A. Flex Item이 한 줄에 들어가지 않을 때 줄바꿈할지 결정하는 property다.

Q. flex-wrap 기본값은 뭐야?
A. 기본값은 `nowrap`이다.

Q. 모바일에서 Flex Item이 삐져나가면 뭘 확인해?
A. `flex-wrap`, fixed width, min-width, gap, overflow를 확인한다.

Q. tag list에는 flex-wrap이 좋아?
A. 좋다. 태그 개수가 많아질 때 자연스럽게 줄바꿈할 수 있다.

Q. flex-grow는 뭐야?
A. Flex Container의 남은 공간을 Flex Item이 얼마나 차지할지 결정하는 property다.

Q. flex-grow 기본값은 뭐야?
A. 기본값은 `0`이다.

Q. input을 남은 공간만큼 늘리려면 어떻게 해?
A. input에 `flex-grow: 1` 또는 `flex: 1`을 사용할 수 있다.

Q. flex-shrink는 뭐야?
A. 공간이 부족할 때 Flex Item이 얼마나 줄어들 수 있는지 결정하는 property다.

Q. flex-shrink 기본값은 뭐야?
A. 기본값은 `1`이다.

Q. 이미지나 아이콘이 찌그러지지 않게 하려면?
A. 필요한 경우 `flex-shrink: 0`을 사용할 수 있다.

Q. flex item이 줄어들지 않는 이유는?
A. `min-width: auto`, 고정 width, 긴 텍스트, `flex-shrink: 0` 때문일 수 있다.

Q. flex-basis는 뭐야?
A. Flex Item의 공간 분배 전 기본 크기를 지정하는 property다.

Q. flex-basis 기본값은 뭐야?
A. 기본값은 `auto`다.

Q. flex-basis와 width 차이는 뭐야?
A. flex-basis는 Flex Layout 안에서 Item의 기준 크기로 사용되고 width보다 우선 고려될 수 있다.

Q. flex 속성은 뭐야?
A. `flex-grow`, `flex-shrink`, `flex-basis`를 한 번에 지정하는 축약 속성이다.

Q. sidebar 고정 너비는 어떻게 해?
A. 예를 들어 `flex: 0 0 240px`처럼 설정할 수 있다.

Q. flex 1을 쓰면 항상 좋아?
A. 아니다. Item이 의도치 않게 늘거나 줄 수 있으므로 목적을 확인해야 한다.

Q. align-content는 뭐야?
A. 여러 줄로 wrapping된 Flex Line들을 Cross Axis 방향으로 정렬하는 property다.

Q. align-content가 안 먹는 이유는?
A. Flex Line이 한 줄이거나 `flex-wrap`이 없거나 남은 Cross Axis 공간이 없기 때문일 수 있다.

Q. Flexbox로 가운데 정렬은 어떻게 해?
A. Container에 `display: flex`, `justify-content: center`, `align-items: center`를 적용한다.

Q. 세로 중앙 정렬이 안 되는 이유는?
A. Container에 높이나 남은 세로 공간이 없기 때문일 수 있다.

Q. Header Layout에 Flexbox를 써도 돼?
A. 적합하다. 로고, 메뉴, 버튼을 한 방향으로 정렬하기 좋다.

Q. Header에서 space-between은 언제 써?
A. 로고와 메뉴 또는 액션 영역을 양끝에 배치할 때 사용한다.

Q. 아이콘과 텍스트 정렬은 어떻게 해?
A. 부모에 `display: inline-flex`, `align-items: center`, `gap`을 적용한다.

Q. 아이콘만 있는 버튼은 어떻게 접근성을 처리해?
A. `aria-label` 또는 숨김 텍스트로 버튼 이름을 제공한다.

Q. 검색창과 버튼을 한 줄로 만들려면?
A. form에 `display: flex`, input에 `flex: 1`, button에 `flex-shrink: 0`을 사용할 수 있다.

Q. input이 너무 커져서 버튼을 밀어내면?
A. input에 `min-width: 0`을 적용하고 button에 `flex-shrink: 0`을 검토한다.

Q. Responsive Flexbox는 어떻게 작성해?
A. Mobile First로 column 또는 wrap 구조를 기본으로 하고 media query에서 row 또는 item 크기를 조정한다.

Q. 모바일에서는 flex-direction을 column으로 바꿔도 돼?
A. 가능하다. 좁은 화면에서는 column 배치가 더 자연스러운 경우가 많다.

Q. 카드 목록을 Flexbox로 반응형 처리할 수 있어?
A. 가능하다. `flex-wrap: wrap`과 `flex: 1 1 280px` 같은 패턴을 사용할 수 있다.

Q. Flexbox가 안 먹을 때 가장 먼저 볼 것은?
A. 정렬하려는 요소의 부모에 `display: flex`가 적용되어 있는지 확인한다.

Q. Flex Item이 줄어들지 않는 이유는?
A. 기본 min-width, 고정 width, 긴 텍스트, flex-shrink 설정 때문일 수 있다.

Q. Flexbox overflow는 어떻게 해결해?
A. flex-wrap, min-width: 0, max-width, overflow-wrap, flex-basis를 확인한다.

Q. 카드 내부 정렬은 Flexbox가 좋아?
A. 보통 Flexbox가 적합하다.

Q. 카드 목록은 Flexbox와 Grid 중 뭐가 좋아?
A. 행과 열이 중요한 카드 목록은 Grid가 더 적합한 경우가 많다.

Q. row에서 세로 중앙 정렬은 무엇을 써?
A. `align-items: center`를 사용한다.

Q. column에서 세로 중앙 정렬은 무엇을 써?
A. `justify-content: center`를 사용한다.

Q. gap과 margin 차이는 뭐야?
A. gap은 Container가 Item 사이 간격을 관리하고 margin은 개별 요소의 외부 여백이다.

Q. flex-grow와 flex-shrink 차이는 뭐야?
A. flex-grow는 남은 공간을 차지하는 비율이고 flex-shrink는 부족한 공간에서 줄어드는 비율이다.

Q. Flexbox에서 가장 흔한 실수는 뭐야?
A. Container와 Item을 혼동하고 justify-content와 align-items 축을 잘못 이해하는 것이다.

Q. 모바일에서 Flex Layout이 깨지는 흔한 이유는?
A. flex-wrap 누락, 고정 width, min-width 문제, gap 미고려 때문이다.

Q. Flexbox 문제는 어떤 순서로 디버깅해?
A. Container, Direct Child, flex-direction, Axis, justify/align, gap/wrap, Item flex 속성, min-width 순서로 확인한다.

Q. Flexbox Best Practice는 뭐야?
A. 부모 Container에 flex를 적용하고 Axis, gap, wrap, Item 크기 제어를 명확히 하여 1차원 Layout을 안정적으로 만드는 것이다.

Q. Flexbox 검수에서 가장 먼저 볼 것은 뭐야?
A. `display: flex`가 정렬 대상의 부모에 적용되었는지와 Flex Item이 직접 자식인지 먼저 확인한다.

Q. Flexbox를 쓰면 안 좋은 경우는?
A. 행과 열이 모두 중요한 2차원 Layout은 Grid가 더 적합하다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Flexbox로 Header, Button Group, Form Row, Card 내부 정렬, Responsive Wrap을 안정적으로 생성하고 디버깅하게 만드는 것이다.
