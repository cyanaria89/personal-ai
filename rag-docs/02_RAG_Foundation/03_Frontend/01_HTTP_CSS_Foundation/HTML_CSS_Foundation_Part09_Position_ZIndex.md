# HTML CSS Foundation Part09 - Position ZIndex

---

# 1. CSS Position

## 1.1 Position Concept

### [개념]

CSS Position은 요소를 일반 문서 흐름(normal flow) 기준 또는 특정 기준점 기준으로 배치하는 CSS Layout 기능이다.

`position`은 요소의 위치 계산 방식과 containing block 기준을 결정한다.

대표 값:

```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;
```

Position은 Tooltip, Dropdown, Modal, Header, Badge, Overlay, Floating Button, Sticky Navigation, Layered UI 구현에 자주 사용된다.

---

### [핵심]

Position 핵심:

- `static`은 기본 위치 방식이다.
- `relative`는 원래 위치를 기준으로 이동한다.
- `absolute`는 가장 가까운 positioned ancestor를 기준으로 배치된다.
- `fixed`는 viewport를 기준으로 고정 배치된다.
- `sticky`는 scroll 위치에 따라 relative와 fixed처럼 동작한다.
- `top`, `right`, `bottom`, `left`, `inset`으로 위치를 조정한다.
- `z-index`는 stacking order를 제어한다.
- Position 사용은 normal flow와 stacking context를 함께 고려해야 한다.

---

### [실무]

2026 실무 기준에서 Position은 단순 좌표 이동이 아니라 Layer UI와 Scroll UI를 안정적으로 구현하기 위한 도구다.

Frontend Agent는 Position을 사용할 때 아래 기준을 함께 검토해야 한다.

- Normal Flow 유지 여부
- Containing Block 기준
- Parent `position: relative` 필요 여부
- Scroll Container 영향
- z-index Layer 기준
- Stacking Context 발생 여부
- Focus / Keyboard 접근성
- Overlay 클릭 영역
- Mobile Viewport 대응
- Sticky 동작 조건

Position 작성 Flow:

```text
배치 목적 확인
→ normal flow 유지 필요 여부 확인
→ position 값 선택
→ 기준 부모 확인
→ inset 값 지정
→ z-index 필요 여부 확인
→ stacking context 확인
→ scroll / responsive 동작 검수
```

---

### [FAQ]

Q. CSS position이 뭐야?
A. 요소를 일반 문서 흐름 또는 특정 기준점에 따라 배치하는 CSS property다.

Q. position은 언제 써?
A. Tooltip, Dropdown, Modal, Sticky Header, Badge, Floating Button 같은 Layer UI에 사용한다.

Q. position을 쓰면 layout이 항상 좋아져?
A. 아니다. normal flow에서 빠지는 경우가 있어 Layout과 접근성 문제를 만들 수 있다.

Q. position 문제는 무엇부터 확인해?
A. position 값, 기준 부모, inset 값, z-index, stacking context, scroll container를 확인한다.

---

# 2. Static Position

## 2.1 position static

### [개념]

`position: static`은 모든 HTML 요소의 기본 position 값이다.

Static 요소는 일반 문서 흐름(normal flow)에 따라 배치된다.

---

### [핵심]

Static 핵심:

- 기본 position 값이다.
- normal flow에 따라 배치된다.
- `top`, `right`, `bottom`, `left`, `z-index`가 일반적으로 적용되지 않는다.
- 대부분의 일반 콘텐츠는 static 상태로 충분하다.
- 불필요하게 position을 지정하지 않는 것이 좋다.

예:

```css
.card {
  position: static;
}
```

---

### [실무]

대부분의 텍스트, 카드, 리스트, 섹션은 `position: static`으로 충분하다.

Position을 추가하기 전에 아래를 확인한다.

```text
일반 흐름 배치 가능?
→ Flexbox / Grid로 해결 가능?
→ margin / padding / gap으로 해결 가능?
→ Layer UI인가?
→ position 필요
```

검수 기준:

- 단순 정렬 문제를 position으로 해결하지 않았는가?
- Flexbox나 Grid가 더 적절하지 않은가?
- margin 대신 top/left로 억지 이동하지 않았는가?
- position이 필요 없는 요소에 position이 추가되지 않았는가?

---

### [FAQ]

Q. position static은 뭐야?
A. 요소가 일반 문서 흐름에 따라 배치되는 기본 position 값이다.

Q. static 요소에 top을 주면 이동해?
A. 일반적으로 이동하지 않는다. top, left 같은 offset은 positioned element에서 의미가 있다.

Q. 모든 요소에 position을 지정해야 해?
A. 아니다. 대부분 요소는 기본 static 상태로 충분하다.

---

# 3. Relative Position

## 3.1 position relative

### [개념]

`position: relative`는 요소를 원래 normal flow 위치를 기준으로 이동할 수 있게 하는 position 값이다.

Relative 요소는 normal flow에서 원래 공간을 유지한다.

---

### [핵심]

Relative 핵심:

- 원래 위치를 기준으로 이동한다.
- `top`, `right`, `bottom`, `left`, `inset`을 사용할 수 있다.
- 원래 차지하던 공간은 유지된다.
- `absolute` 자식의 기준 부모로 자주 사용된다.
- `z-index`를 적용할 수 있다.
- 단순 Layout 정렬용으로 남용하지 않는다.

예:

```css
.badge-wrapper {
  position: relative;
}
```

---

### [실무]

Relative는 보통 자식 absolute 배치의 기준을 만들기 위해 사용한다.

Badge 예:

```html
<div class="notification-button">
  <button type="button">Notifications</button>
  <span class="badge">3</span>
</div>
```

```css
.notification-button {
  position: relative;
  display: inline-block;
}

.badge {
  position: absolute;
  top: -6px;
  right: -6px;
}
```

검수 기준:

- relative가 자식 absolute 기준을 만들기 위한 것인가?
- top/left로 단순 위치 보정을 남용하지 않았는가?
- 원래 공간이 유지되는 것이 의도인가?
- z-index 적용이 필요한가?
- Flexbox / Grid / gap으로 해결 가능한 문제는 아닌가?

---

### [FAQ]

Q. position relative는 뭐야?
A. 요소를 원래 위치 기준으로 이동할 수 있게 하고 absolute 자식의 기준 부모가 될 수 있는 position 값이다.

Q. relative를 주면 normal flow에서 빠져?
A. 아니다. 원래 공간은 유지된다.

Q. relative는 언제 많이 써?
A. absolute 자식 요소의 기준 부모를 만들 때 많이 사용한다.

Q. relative로 레이아웃 정렬을 해도 돼?
A. 권장하지 않는다. 일반 정렬은 Flexbox, Grid, margin, gap을 우선 고려한다.

---

# 4. Absolute Position

## 4.1 position absolute

### [개념]

`position: absolute`는 요소를 normal flow에서 제거하고 기준 부모를 기준으로 배치하는 position 값이다.

Absolute 요소의 기준은 가장 가까운 positioned ancestor다.

Positioned ancestor는 `position` 값이 `static`이 아닌 조상 요소를 의미한다.

---

### [핵심]

Absolute 핵심:

- normal flow에서 제거된다.
- 원래 공간을 차지하지 않는다.
- 가장 가까운 positioned ancestor를 기준으로 배치된다.
- 기준 부모가 없으면 초기 containing block 또는 viewport에 가까운 기준을 사용할 수 있다.
- `top`, `right`, `bottom`, `left`, `inset`으로 위치를 지정한다.
- Tooltip, Dropdown, Badge, Overlay 내부 요소에 자주 사용된다.
- 부모에 `position: relative`가 필요한 경우가 많다.

예:

```css
.card {
  position: relative;
}

.card-badge {
  position: absolute;
  top: 12px;
  right: 12px;
}
```

---

### [실무]

Card Badge 예:

```html
<article class="festival-card">
  <span class="festival-badge">Hot</span>
  <h2>Seoul Light Festival</h2>
</article>
```

```css
.festival-card {
  position: relative;
  padding: 20px;
}

.festival-badge {
  position: absolute;
  top: 12px;
  right: 12px;
}
```

Dropdown 예:

```css
.dropdown {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  z-index: 20;
}
```

검수 기준:

- 기준 부모에 `position: relative`가 있는가?
- absolute 요소가 normal flow에서 빠져도 되는가?
- 부모 높이가 absolute 자식 때문에 자동으로 늘어나지 않는 것을 이해했는가?
- 작은 화면에서 absolute 요소가 잘리지 않는가?
- overflow hidden 부모 때문에 잘리지 않는가?
- keyboard focus와 접근성 흐름이 유지되는가?

---

### [FAQ]

Q. position absolute는 뭐야?
A. 요소를 normal flow에서 제거하고 기준 부모를 기준으로 배치하는 position 값이다.

Q. absolute 기준은 무엇이야?
A. 가장 가까운 positioned ancestor가 기준이 된다.

Q. absolute 자식이 부모 밖으로 이상하게 가는 이유는?
A. 부모에 `position: relative` 같은 기준 position이 없기 때문일 수 있다.

Q. absolute 요소는 부모 높이에 영향을 줘?
A. 일반적으로 주지 않는다. normal flow에서 제거되기 때문이다.

---

# 5. Fixed Position

## 5.1 position fixed

### [개념]

`position: fixed`는 요소를 viewport 기준으로 고정 배치하는 position 값이다.

사용자가 페이지를 scroll해도 fixed 요소는 지정된 위치에 유지된다.

---

### [핵심]

Fixed 핵심:

- viewport 기준으로 배치된다.
- scroll해도 위치가 유지된다.
- normal flow에서 제거된다.
- Header, Floating Button, Toast, Modal Overlay에 자주 사용된다.
- `top`, `right`, `bottom`, `left`, `inset`을 사용한다.
- fixed 요소가 콘텐츠를 가릴 수 있다.
- Mobile viewport와 safe area를 고려해야 한다.

예:

```css
.floating-button {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 50;
}
```

---

### [실무]

Fixed Header 예:

```css
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 40;
}
```

Fixed Header 사용 시 본문 가림 대응:

```css
body {
  padding-top: 64px;
}
```

Modal Overlay 예:

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
}
```

검수 기준:

- fixed 요소가 콘텐츠를 가리지 않는가?
- Header 높이만큼 본문 여백이 필요한가?
- mobile safe area 대응이 필요한가?
- z-index layer가 명확한가?
- scroll lock이 필요한 UI인가?
- focus trap이 필요한 modal인가?

---

### [FAQ]

Q. position fixed는 뭐야?
A. 요소를 viewport 기준으로 고정 배치하는 position 값이다.

Q. fixed 요소는 scroll해도 움직이지 않아?
A. 맞다. viewport 기준 위치에 고정된다.

Q. fixed header가 본문을 가리면 어떻게 해?
A. Header 높이만큼 본문 padding 또는 layout offset을 제공해야 한다.

Q. fixed는 언제 많이 써?
A. 고정 Header, Floating Button, Toast, Modal Overlay에 자주 사용한다.

---

# 6. Sticky Position

## 6.1 position sticky

### [개념]

`position: sticky`는 요소가 scroll 위치에 따라 normal flow에 있다가 특정 위치에서 고정되는 position 값이다.

Sticky는 relative와 fixed의 중간처럼 동작한다.

---

### [핵심]

Sticky 핵심:

- normal flow를 유지한다.
- 지정한 offset에 도달하면 고정된다.
- `top`, `bottom` 같은 offset이 필요하다.
- scroll container의 영향을 받는다.
- 부모 영역 안에서만 sticky 동작이 유지된다.
- overflow 설정된 부모가 sticky 동작을 방해할 수 있다.
- Sticky Header, Table Header, Sidebar에 자주 사용된다.

예:

```css
.sticky-header {
  position: sticky;
  top: 0;
  z-index: 30;
}
```

---

### [실무]

Sticky Section Header 예:

```css
.section-title {
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: white;
}
```

Sticky Sidebar 예:

```css
.sidebar {
  position: sticky;
  top: 24px;
  align-self: start;
}
```

Sticky Debug 기준:

```text
position sticky 확인
→ top / bottom offset 확인
→ 부모 높이 확인
→ scroll container 확인
→ overflow hidden / auto 부모 확인
→ z-index / background 확인
```

검수 기준:

- `top` 또는 `bottom` offset이 있는가?
- 부모 요소 높이가 sticky 동작을 허용하는가?
- scroll container가 의도한 요소인가?
- 부모의 overflow가 sticky를 방해하지 않는가?
- sticky 요소에 배경색이 있어 겹침이 자연스러운가?
- z-index가 필요한가?

---

### [FAQ]

Q. position sticky는 뭐야?
A. scroll 위치에 따라 일반 흐름에 있다가 특정 위치에서 고정되는 position 값이다.

Q. sticky가 안 먹는 이유는 뭐야?
A. top 같은 offset 누락, 부모 overflow 설정, 부모 높이 부족, scroll container 문제 때문일 수 있다.

Q. sticky에는 top이 꼭 필요해?
A. 일반적으로 sticky 기준 위치를 만들기 위해 `top` 또는 `bottom` 같은 offset이 필요하다.

Q. sticky와 fixed 차이는 뭐야?
A. fixed는 항상 viewport 기준으로 고정되고 sticky는 scroll 조건에 따라 부모 영역 안에서 고정된다.

---

# 7. Offset Properties

## 7.1 top right bottom left

### [개념]

`top`, `right`, `bottom`, `left`는 positioned element의 위치를 조정하는 offset property다.

이 속성들은 `position: static` 요소에는 일반적으로 효과가 없다.

---

### [핵심]

Offset 핵심:

- `top`은 기준 상단에서의 거리다.
- `right`는 기준 오른쪽에서의 거리다.
- `bottom`은 기준 하단에서의 거리다.
- `left`는 기준 왼쪽에서의 거리다.
- `absolute`, `fixed`, `sticky`, `relative`에서 사용된다.
- 기준점은 position 값에 따라 달라진다.
- 양쪽 offset을 동시에 지정하면 크기 계산에도 영향을 줄 수 있다.

예:

```css
.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}
```

---

### [실무]

Overlay 전체 채우기:

```css
.overlay {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
```

중앙 배치 예:

```css
.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

검수 기준:

- offset 기준이 부모인지 viewport인지 명확한가?
- `position` 값이 static이 아닌가?
- top/left로 일반 Layout을 억지 조정하지 않았는가?
- 양방향 offset 사용이 의도한 크기를 만드는가?
- transform과 함께 사용할 때 기준을 이해했는가?

---

### [FAQ]

Q. top right bottom left는 뭐야?
A. positioned element의 기준점으로부터 위치를 조정하는 offset property다.

Q. top을 줬는데 요소가 안 움직이는 이유는?
A. 요소가 `position: static` 상태이기 때문일 수 있다.

Q. absolute의 top 기준은 뭐야?
A. 가장 가까운 positioned ancestor의 padding box를 기준으로 하는 경우가 많다.

Q. fixed의 top 기준은 뭐야?
A. 일반적으로 viewport를 기준으로 한다.

---

## 7.2 inset

### [개념]

`inset`은 `top`, `right`, `bottom`, `left`를 한 번에 지정하는 CSS shorthand property다.

Overlay, Fullscreen Layer, Absolute Fill 패턴에 자주 사용한다.

---

### [핵심]

Inset 핵심:

- `inset: 0`은 top/right/bottom/left 모두 0과 같다.
- positioned element에서 사용한다.
- Overlay 전체 채우기에 적합하다.
- 축약형이라 코드가 간결하다.
- 일부 방향만 지정할 수도 있다.
- offset 기준은 position 값에 따라 달라진다.

예:

```css
.overlay {
  position: fixed;
  inset: 0;
}
```

---

### [실무]

Modal Backdrop 예:

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
}
```

Absolute Fill 예:

```css
.card-image-overlay {
  position: absolute;
  inset: 0;
}
```

검수 기준:

- 전체 영역을 채우는 UI인가?
- parent 기준 absolute fill이면 parent에 position 기준이 있는가?
- fixed overlay라면 viewport 전체를 의도하는가?
- z-index layer와 함께 관리되는가?
- content가 overlay에 가려지는 것이 의도인가?

---

### [FAQ]

Q. inset은 뭐야?
A. top, right, bottom, left를 한 번에 지정하는 CSS shorthand property다.

Q. inset 0은 무슨 뜻이야?
A. `top: 0; right: 0; bottom: 0; left: 0;`과 같다.

Q. inset은 언제 써?
A. Modal Backdrop, Overlay, absolute fill처럼 전체 영역을 채울 때 자주 사용한다.

---

# 8. Z Index

## 8.1 z-index Concept

### [개념]

`z-index`는 positioned element 또는 stacking context 안의 요소가 z축에서 어떤 순서로 쌓이는지 결정하는 CSS property다.

z-index 값이 큰 요소는 같은 stacking context 안에서 더 앞에 표시될 수 있다.

---

### [핵심]

z-index 핵심:

- 요소의 쌓임 순서를 제어한다.
- 일반적으로 positioned element에서 의미가 있다.
- 같은 stacking context 안에서 비교된다.
- 값이 크다고 항상 모든 요소 위에 올라가는 것은 아니다.
- stacking context가 다르면 예상과 다르게 보일 수 있다.
- Layer UI에서는 z-index scale을 정해 관리하는 것이 좋다.

예:

```css
.dropdown-menu {
  position: absolute;
  z-index: 20;
}

.modal {
  position: fixed;
  z-index: 100;
}
```

---

### [실무]

권장 z-index scale 예:

```css
:root {
  --z-dropdown: 20;
  --z-sticky: 30;
  --z-header: 40;
  --z-toast: 80;
  --z-modal: 100;
}
```

사용 예:

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-header);
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
}
```

검수 기준:

- z-index가 필요한 positioned element인가?
- 같은 stacking context 안에서 비교하고 있는가?
- 무작정 큰 숫자를 사용하지 않았는가?
- dropdown, header, modal, toast layer 순서가 명확한가?
- z-index scale을 변수로 관리하는가?

---

### [FAQ]

Q. z-index가 뭐야?
A. 요소가 z축에서 어떤 순서로 쌓이는지 결정하는 CSS property다.

Q. z-index가 큰데도 위로 안 올라오는 이유는?
A. 다른 stacking context 안에 있어서 같은 기준으로 비교되지 않기 때문일 수 있다.

Q. z-index는 숫자가 클수록 좋아?
A. 아니다. layer 기준을 정해 필요한 범위에서 관리하는 것이 좋다.

Q. z-index는 언제 써?
A. Dropdown, Header, Modal, Toast, Overlay처럼 겹치는 UI의 순서를 제어할 때 사용한다.

---

# 9. Stacking Context

## 9.1 Stacking Context Concept

### [개념]

Stacking Context는 요소들이 z축에서 쌓이는 독립적인 비교 그룹이다.

z-index는 같은 Stacking Context 안에서만 직접 비교된다.

---

### [핵심]

Stacking Context 핵심:

- z-index 비교의 독립 단위다.
- 부모 stacking context 안에서 자식 z-index가 제한된다.
- 자식 요소의 z-index가 커도 부모 stacking context 밖의 요소를 이기지 못할 수 있다.
- 특정 CSS property가 stacking context를 만들 수 있다.
- z-index 문제의 핵심 원인 중 하나다.

Stacking Context를 만들 수 있는 대표 조건:

- positioned element + z-index 값
- `position: fixed`
- `position: sticky`
- `opacity`가 1보다 작은 경우
- `transform`이 none이 아닌 경우
- `filter` 사용
- `isolation: isolate`
- 일부 `contain`, `will-change` 사용

---

### [실무]

z-index Debug Flow:

```text
겹침 문제 확인
→ 요소 position 확인
→ z-index 값 확인
→ 부모 stacking context 확인
→ transform / opacity / filter 확인
→ overflow clipping 확인
→ layer scale 기준 확인
```

문제 예:

```text
문제: dropdown z-index를 9999로 줘도 header 위로 안 올라감
원인: 부모 stacking context 또는 overflow clipping
해결: stacking context 구조 수정 또는 portal/layer 위치 변경
```

검수 기준:

- 부모 요소가 stacking context를 만들고 있는가?
- `transform`이 예상치 못한 stacking context를 만들었는가?
- `opacity` 또는 `filter`가 stacking context를 만들었는가?
- dropdown / modal을 DOM 상위 layer로 이동해야 하는가?
- React Portal이 필요한 UI인가?

---

### [FAQ]

Q. Stacking Context가 뭐야?
A. 요소들이 z축에서 쌓이는 독립적인 비교 그룹이다.

Q. z-index가 안 먹는 이유는 뭐야?
A. 다른 stacking context에 있거나 부모 stacking context에 갇혀 있기 때문일 수 있다.

Q. transform도 z-index 문제를 만들 수 있어?
A. 그렇다. transform은 새로운 stacking context를 만들 수 있다.

Q. Modal이나 Dropdown이 계속 가려지면 어떻게 해?
A. stacking context, overflow clipping, DOM 위치, portal 사용 필요성을 확인한다.

---

# 10. Overflow and Clipping

## 10.1 Overflow Clipping

### [개념]

Overflow Clipping은 요소가 부모 영역을 벗어날 때 부모의 `overflow` 설정에 의해 잘리는 현상이다.

Positioned element, Dropdown, Tooltip, Focus Outline에서 자주 문제가 된다.

---

### [핵심]

Overflow Clipping 핵심:

- `overflow: hidden`은 넘친 콘텐츠를 잘라낸다.
- `overflow: auto` 또는 `scroll`은 scroll container를 만든다.
- absolute 요소도 overflow hidden 부모에 의해 잘릴 수 있다.
- z-index를 높여도 overflow clipping을 이기지 못할 수 있다.
- Tooltip, Dropdown, Popover가 잘리는 주요 원인이다.
- 해결에는 DOM 위치 변경, portal, overflow 구조 수정이 필요할 수 있다.

---

### [실무]

문제 예:

```css
.card {
  overflow: hidden;
}

.dropdown-menu {
  position: absolute;
  z-index: 9999;
}
```

Dropdown이 card 밖으로 나가면 잘릴 수 있다.

해결 전략:

```text
overflow hidden 필요 여부 확인
→ dropdown을 card 밖 layer로 이동
→ React Portal 검토
→ parent overflow 구조 수정
→ clipping이 필요한 요소와 floating layer 분리
```

검수 기준:

- 부모 중 `overflow: hidden`, `auto`, `scroll`이 있는가?
- z-index 문제가 아니라 clipping 문제인가?
- floating UI가 clipping container 내부에 있는가?
- portal 또는 layer root가 필요한가?
- focus outline도 잘리지 않는가?

---

### [FAQ]

Q. overflow clipping이 뭐야?
A. 요소가 부모 영역 밖으로 나갈 때 부모 overflow 설정 때문에 잘리는 현상이다.

Q. z-index를 높였는데 dropdown이 잘리는 이유는?
A. z-index 문제가 아니라 부모의 overflow clipping 문제일 수 있다.

Q. dropdown이 부모 밖에서 잘리면 어떻게 해?
A. overflow 구조를 수정하거나 dropdown을 상위 layer 또는 portal로 이동하는 방식을 검토한다.

Q. overflow hidden은 언제 조심해야 해?
A. Dropdown, Tooltip, Modal, Focus Outline 같은 요소가 부모 밖으로 나가야 할 때 조심해야 한다.

---

# 11. Common Position Patterns

## 11.1 Badge Pattern

### [개념]

Badge Pattern은 부모 요소의 모서리나 특정 위치에 작은 상태 표시 요소를 겹쳐 배치하는 패턴이다.

Notification Count, Status Label, Hot Badge, New Badge에 사용한다.

---

### [핵심]

Badge Pattern 핵심:

- 부모에 `position: relative`를 준다.
- Badge에 `position: absolute`를 준다.
- `top`, `right` 등 offset으로 위치를 지정한다.
- Badge가 부모 밖으로 나갈 수 있다.
- Badge 텍스트가 접근성 정보로 필요한지 확인한다.
- 숫자 Badge는 동적 크기를 고려한다.

---

### [실무]

예:

```html
<button
  class="notification-button"
  type="button"
  aria-label="Notifications, 3 unread"
>
  <span aria-hidden="true">🔔</span>
  <span class="notification-badge">3</span>
</button>
```

```css
.notification-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.notification-badge {
  position: absolute;
  top: -6px;
  right: -6px;
  min-width: 18px;
  padding-inline: 6px;
  border-radius: 999px;
}
```

검수 기준:

- 부모에 position 기준이 있는가?
- Badge가 absolute로 배치되는가?
- 숫자가 두 자리 이상일 때 깨지지 않는가?
- 시각 정보가 accessible name에도 반영되는가?
- Badge가 overflow hidden 부모 때문에 잘리지 않는가?

---

### [FAQ]

Q. Badge는 position으로 어떻게 만들어?
A. 부모에 `position: relative`, Badge에 `position: absolute`를 주고 top/right로 배치한다.

Q. Badge 숫자가 접근성에 필요하면 어떻게 해?
A. 버튼의 aria-label이나 숨김 텍스트로 unread count 의미를 제공한다.

Q. Badge가 잘리면 무엇을 확인해?
A. 부모 overflow 설정과 Badge 위치, z-index를 확인한다.

---

## 11.2 Dropdown Pattern

### [개념]

Dropdown Pattern은 Trigger 요소를 기준으로 Menu 또는 Option Panel을 겹쳐 표시하는 UI 패턴이다.

---

### [핵심]

Dropdown Pattern 핵심:

- Trigger와 Menu를 감싸는 부모에 `position: relative`를 줄 수 있다.
- Menu는 `position: absolute`로 배치한다.
- `top: 100%`로 Trigger 아래 배치할 수 있다.
- `z-index`가 필요하다.
- overflow clipping을 주의해야 한다.
- keyboard navigation과 focus 관리가 필요하다.
- 열림 상태는 `aria-expanded`와 연결할 수 있다.

---

### [실무]

기본 예:

```html
<div class="dropdown">
  <button type="button" aria-expanded="false" aria-haspopup="menu">Menu</button>

  <div class="dropdown-menu" role="menu">
    <button type="button" role="menuitem">Edit</button>
    <button type="button" role="menuitem">Delete</button>
  </div>
</div>
```

```css
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  z-index: 20;
  min-width: 160px;
}
```

검수 기준:

- Menu 기준 부모가 명확한가?
- Dropdown Menu가 clipping되지 않는가?
- z-index가 Header / Modal과 충돌하지 않는가?
- 열림 상태가 aria-expanded에 반영되는가?
- keyboard로 열고 닫고 선택할 수 있는가?
- 외부 클릭 또는 Escape 처리 기준이 있는가?

---

### [FAQ]

Q. Dropdown은 position으로 어떻게 만들어?
A. 부모에 `position: relative`, menu에 `position: absolute`를 주고 trigger 기준으로 배치한다.

Q. Dropdown이 다른 요소 뒤에 숨으면?
A. z-index와 stacking context를 확인한다.

Q. Dropdown이 부모 밖에서 잘리면?
A. 부모 overflow 설정을 확인하고 portal 또는 layer 구조를 검토한다.

Q. Dropdown에는 접근성 처리가 필요해?
A. 필요하다. aria-expanded, keyboard navigation, focus 관리가 중요하다.

---

## 11.3 Modal Overlay Pattern

### [개념]

Modal Overlay Pattern은 화면 전체 위에 Backdrop과 Dialog를 표시하는 Layer UI 패턴이다.

Modal은 일반적으로 fixed positioning과 높은 z-index를 사용한다.

---

### [핵심]

Modal Overlay 핵심:

- Backdrop은 `position: fixed`와 `inset: 0`을 사용한다.
- Dialog는 fixed 또는 backdrop 내부 flex/grid 중앙 정렬을 사용할 수 있다.
- Modal Layer는 높은 z-index가 필요하다.
- body scroll lock이 필요할 수 있다.
- focus trap이 필요하다.
- Escape 닫기와 backdrop 클릭 정책이 필요하다.
- 접근성 role과 label이 필요하다.

---

### [실무]

Modal 예:

```html
<div class="modal-backdrop">
  <section
    class="modal-dialog"
    role="dialog"
    aria-modal="true"
    aria-labelledby="modal-title"
  >
    <h2 id="modal-title">Confirm Delete</h2>
    <p>Are you sure you want to delete this item?</p>
    <button type="button">Cancel</button>
    <button type="button">Delete</button>
  </section>
</div>
```

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: grid;
  place-items: center;
}

.modal-dialog {
  width: min(100% - 32px, 480px);
  max-height: calc(100dvh - 32px);
  overflow: auto;
}
```

검수 기준:

- Backdrop이 viewport 전체를 덮는가?
- Dialog가 작은 화면에서 넘치지 않는가?
- Modal z-index가 Header / Dropdown보다 높은가?
- focus trap이 있는가?
- aria-modal과 label이 있는가?
- body scroll이 제어되는가?

---

### [FAQ]

Q. Modal Overlay는 position으로 어떻게 만들어?
A. Backdrop에 `position: fixed`, `inset: 0`, 높은 z-index를 주고 Dialog를 중앙 정렬한다.

Q. Modal에서 inset 0은 왜 써?
A. viewport 전체를 덮는 Backdrop을 만들기 위해 사용한다.

Q. Modal은 CSS만으로 충분해?
A. 아니다. focus trap, keyboard handling, scroll lock, aria 처리가 함께 필요하다.

Q. Modal이 화면 밖으로 넘치면 어떻게 해?
A. Dialog에 max-height와 overflow auto를 적용하고 mobile viewport를 고려한다.

---

## 11.4 Sticky Header Pattern

### [개념]

Sticky Header Pattern은 Header가 일반 흐름에 있다가 scroll 시 상단에 고정되는 UI 패턴이다.

`position: sticky`와 `top: 0`을 자주 사용한다.

---

### [핵심]

Sticky Header 핵심:

- Header에 `position: sticky`를 적용한다.
- `top: 0`이 필요하다.
- Header는 normal flow 공간을 유지한다.
- z-index가 필요할 수 있다.
- 배경색이 없으면 뒤 콘텐츠와 겹쳐 보일 수 있다.
- 부모 overflow가 sticky 동작을 방해할 수 있다.

---

### [실무]

예:

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 40;
  background-color: white;
}
```

검수 기준:

- Header가 scroll container 안에서 sticky 동작하는가?
- `top: 0`이 있는가?
- Header 배경이 있는가?
- Header가 뒤 콘텐츠와 겹칠 때 z-index가 충분한가?
- 부모 overflow 설정이 sticky를 방해하지 않는가?
- fixed header가 더 적절한 요구사항은 아닌가?

---

### [FAQ]

Q. Sticky Header는 어떻게 만들어?
A. Header에 `position: sticky`, `top: 0`, 필요한 z-index와 background를 적용한다.

Q. sticky header가 안 붙는 이유는?
A. top 누락, 부모 overflow, scroll container, 부모 높이 문제 때문일 수 있다.

Q. sticky와 fixed header 중 뭐가 좋아?
A. 항상 고정이면 fixed, normal flow를 유지하면서 scroll 시 붙게 하려면 sticky가 적합하다.

---

# 12. Position and Accessibility

## 12.1 Accessibility Rules

### [개념]

Position 기반 UI는 화면에 보이는 순서와 DOM 순서, focus 순서, keyboard navigation이 어긋날 수 있다.

Accessibility를 유지하려면 Layer UI의 의미와 상호작용을 함께 설계해야 한다.

---

### [핵심]

Position Accessibility 핵심:

- DOM 순서와 시각 순서가 과도하게 다르면 안 된다.
- absolute / fixed UI도 keyboard로 접근 가능해야 한다.
- Dropdown은 trigger와 열림 상태를 연결해야 한다.
- Modal은 focus trap과 `aria-modal`을 고려해야 한다.
- Tooltip은 hover만 의존하면 안 된다.
- fixed header가 skip link나 focus target을 가리지 않아야 한다.
- z-index로 화면에 보이는 요소와 focus 가능한 요소 상태가 일치해야 한다.
- `display: none` / `hidden` 상태와 aria 상태가 일치해야 한다.

---

### [실무]

접근성 검수 Checklist:

```md
- [ ] 시각 순서와 DOM 순서가 크게 어긋나지 않는가?
- [ ] Dropdown Trigger에 aria-expanded가 있는가?
- [ ] Modal에 role dialog와 aria-modal이 있는가?
- [ ] Modal focus trap이 있는가?
- [ ] Overlay 뒤 요소로 focus가 이동하지 않는가?
- [ ] fixed header가 focus target을 가리지 않는가?
- [ ] hover-only tooltip이 아닌가?
- [ ] hidden 상태와 aria 상태가 일치하는가?
```

검수 기준:

- Layer UI가 키보드만으로 조작 가능한가?
- 닫힌 Dropdown 내부 요소에 focus가 가지 않는가?
- Modal이 열렸을 때 focus가 Modal 내부에 있는가?
- Escape 닫기 정책이 있는가?
- Scroll 위치 이동 시 focus 대상이 Header에 가리지 않는가?

---

### [FAQ]

Q. position UI도 접근성이 중요해?
A. 중요하다. Dropdown, Modal, Tooltip, Sticky Header는 focus와 keyboard 접근성 문제가 자주 발생한다.

Q. absolute 요소는 keyboard로 접근돼?
A. 요소 종류와 상태에 따라 가능하다. 시각 표시와 focus 가능 상태를 일치시켜야 한다.

Q. Modal 접근성에서 중요한 것은 뭐야?
A. role dialog, aria-modal, focus trap, Escape 닫기, background focus 차단이 중요하다.

Q. fixed header가 접근성 문제를 만들 수 있어?
A. 가능하다. focus target이나 skip link 대상이 header에 가려질 수 있다.

---

# 13. Position Troubleshooting

## 13.1 Position Layout Broken

### [개념]

Position Layout Broken은 요소가 예상 위치와 다르게 배치되거나 다른 요소 뒤에 숨기거나 잘리는 문제다.

주요 원인은 기준 부모 누락, offset 오해, stacking context, overflow clipping, scroll container 문제다.

---

### [핵심]

주요 문제:

- absolute 기준 부모 누락
- top/left가 static 요소에 적용되지 않음
- normal flow에서 빠져 부모 높이가 줄어듦
- fixed 요소가 콘텐츠를 가림
- sticky offset 누락
- sticky 부모 overflow 문제
- z-index를 줬는데도 뒤에 숨음
- stacking context에 갇힘
- overflow hidden 부모에 의해 잘림
- transform 부모로 인해 fixed 동작이 예상과 다름
- mobile viewport에서 fixed 위치 문제
- Tooltip / Dropdown이 화면 밖으로 나감

---

### [실무]

Debug Flow:

```text
Position Bug
→ position 값 확인
→ offset 값 확인
→ absolute 기준 부모 확인
→ normal flow 영향 확인
→ z-index 확인
→ stacking context 확인
→ overflow clipping 확인
→ scroll container 확인
→ responsive viewport 확인
→ accessibility focus 확인
```

문제 예:

```text
문제: Badge가 카드 기준이 아니라 화면 끝으로 이동함
원인: 카드 부모에 position relative 없음
해결: 카드에 position relative 추가
```

```text
문제: Dropdown z-index를 올려도 가려짐
원인: stacking context 또는 overflow clipping
해결: 부모 stacking context / overflow 확인, portal 검토
```

```text
문제: sticky header가 작동하지 않음
원인: top 누락 또는 부모 overflow auto/hidden
해결: top 지정, scroll container와 부모 overflow 구조 확인
```

검수 기준:

- Positioned element의 기준이 의도와 맞는가?
- `position: relative` 부모가 필요한가?
- z-index 문제가 아니라 overflow clipping 문제인가?
- sticky 요소의 scroll container가 올바른가?
- Layer UI의 DOM 위치가 적절한가?

---

### [FAQ]

Q. absolute 요소가 엉뚱한 곳에 가는 이유는?
A. 기준 부모가 없거나 예상한 부모가 positioned element가 아니기 때문일 수 있다.

Q. z-index를 높여도 안 보이는 이유는?
A. stacking context나 overflow clipping 문제일 수 있다.

Q. sticky가 안 되는 이유는?
A. top offset 누락, 부모 overflow, 부모 높이 부족, scroll container 문제를 확인해야 한다.

Q. position 문제는 어떤 순서로 디버깅해?
A. position 값, 기준 부모, offset, z-index, stacking context, overflow, scroll container 순서로 확인한다.

---

# 14. Comparison Rules

## 14.1 static vs relative vs absolute vs fixed vs sticky

### [개념]

CSS Position 값은 요소가 normal flow에 남는지, 기준점이 무엇인지, scroll에 어떻게 반응하는지에 따라 구분한다.

---

### [핵심]

| 비교     | normal flow | 기준점              | scroll 반응      | 주요 사용              |
| -------- | ----------- | ------------------- | ---------------- | ---------------------- |
| static   | 유지        | 일반 흐름           | 일반 흐름        | 기본 배치              |
| relative | 유지        | 원래 위치           | 일반 흐름        | absolute 기준 부모     |
| absolute | 제거        | positioned ancestor | 기준 부모에 따름 | Badge, Dropdown        |
| fixed    | 제거        | viewport            | 고정             | Modal, Floating Button |
| sticky   | 유지        | scroll container    | 조건부 고정      | Sticky Header          |

---

### [실무]

선택 기준:

```text
일반 콘텐츠 배치 → static
absolute 자식 기준 부모 → relative
부모 기준 겹침 요소 → absolute
viewport 고정 UI → fixed
scroll 시 붙는 UI → sticky
```

---

### [FAQ]

Q. relative와 absolute 차이는 뭐야?
A. relative는 normal flow 공간을 유지하고 absolute는 normal flow에서 제거된다.

Q. fixed와 sticky 차이는 뭐야?
A. fixed는 항상 viewport 기준으로 고정되고 sticky는 scroll 조건에 따라 부모 영역 안에서 고정된다.

Q. absolute와 fixed 차이는 뭐야?
A. absolute는 positioned ancestor 기준이고 fixed는 일반적으로 viewport 기준이다.

---

## 14.2 z-index vs Stacking Context

### [개념]

`z-index`는 쌓임 순서 값이고 Stacking Context는 그 z-index가 비교되는 독립 그룹이다.

---

### [핵심]

| 비교      | z-index               | Stacking Context  |
| --------- | --------------------- | ----------------- |
| 의미      | z축 순서 값           | z축 비교 그룹     |
| 적용      | 요소                  | 요소와 자식 그룹  |
| 비교 범위 | 같은 stacking context | 독립적인 그룹     |
| 문제      | 숫자 남용             | 부모에 갇힘       |
| 디버깅    | 값 확인               | 부모 context 확인 |

---

### [실무]

선택 기준:

```text
같은 layer 안에서 순서 조정 → z-index
z-index가 안 먹음 → stacking context 확인
부모 transform / opacity 존재 → stacking context 의심
Modal / Dropdown 가림 → portal 검토
```

---

### [FAQ]

Q. z-index와 stacking context 차이는 뭐야?
A. z-index는 순서 값이고 stacking context는 그 값이 비교되는 독립 그룹이다.

Q. z-index 9999도 안 먹는 이유는?
A. 부모 stacking context 안에 갇혀 다른 context의 요소와 직접 비교되지 않기 때문일 수 있다.

Q. stacking context는 어떻게 확인해?
A. DevTools에서 부모 요소의 position, z-index, transform, opacity, filter 등을 확인한다.

---

## 14.3 Fixed vs Sticky

### [개념]

Fixed와 Sticky는 둘 다 scroll 중 요소를 고정하는 데 사용되지만 동작 기준이 다르다.

---

### [핵심]

| 비교        | fixed                  | sticky                 |
| ----------- | ---------------------- | ---------------------- |
| 기준        | viewport               | scroll container       |
| normal flow | 제거                   | 유지                   |
| 고정 시점   | 항상 고정              | offset 도달 후 고정    |
| 사용 예     | Modal, Floating Button | Sticky Header, Sidebar |
| 주의        | 콘텐츠 가림            | 부모 overflow 영향     |

---

### [실무]

선택 기준:

```text
항상 화면에 떠 있어야 함 → fixed
스크롤하다가 상단에 붙어야 함 → sticky
Modal Backdrop → fixed
Section Header → sticky
Floating Action Button → fixed
Sidebar 따라오기 → sticky
```

---

### [FAQ]

Q. fixed와 sticky 중 언제 fixed를 써?
A. viewport 기준으로 항상 고정되어야 하는 UI에 사용한다.

Q. fixed와 sticky 중 언제 sticky를 써?
A. normal flow를 유지하면서 scroll 시 특정 위치에 붙게 하고 싶을 때 사용한다.

Q. sticky가 fixed보다 항상 좋아?
A. 아니다. 요구사항에 따라 선택해야 한다.

---

## 14.4 Position vs Flexbox Grid

### [개념]

Position은 Layer UI와 기준점 배치에 적합하고, Flexbox와 Grid는 일반 Layout 배치에 적합하다.

---

### [핵심]

| 비교        | Position                | Flexbox              | Grid                   |
| ----------- | ----------------------- | -------------------- | ---------------------- |
| 목적        | 겹침 / 고정 / 기준 배치 | 1차원 정렬           | 2차원 배치             |
| normal flow | 값에 따라 제거 가능     | 유지                 | 유지                   |
| 적합        | Dropdown, Modal, Badge  | Header, Button Group | Card Grid, Page Layout |
| 주의        | 접근성 / z-index        | axis 이해            | track / responsive     |
| 남용 위험   | Layout 억지 이동        | 2차원 한계           | 단순 정렬 과함         |

---

### [실무]

선택 기준:

```text
요소를 겹쳐야 함 → Position
부모 안에서 가로/세로 정렬 → Flexbox
행과 열 구조 → Grid
화면 전체 Overlay → Fixed Position
일반 카드 목록 → Grid
카드 내부 버튼 정렬 → Flexbox
```

---

### [FAQ]

Q. Layout 정렬을 position으로 해도 돼?
A. 일반 정렬에는 권장하지 않는다. Flexbox나 Grid를 우선 고려한다.

Q. position은 언제 써야 해?
A. 요소를 겹치거나 viewport/부모 기준으로 고정 배치해야 할 때 사용한다.

Q. 카드 목록 배치에 position을 써도 돼?
A. 권장하지 않는다. 카드 목록은 Grid 또는 Flexbox가 적합하다.

---

# 15. Common Mistakes

## 15.1 Position ZIndex Common Mistakes

### [개념]

Position과 z-index 실수는 요소가 엉뚱한 곳에 배치되거나, 클릭이 막히거나, Layer UI가 가려지거나, 접근성 문제가 생기는 원인이 된다.

---

### [핵심]

자주 발생하는 실수:

- 단순 정렬을 position으로 해결
- absolute 기준 부모에 `position: relative` 누락
- absolute 요소가 normal flow에서 빠지는 것을 놓침
- 부모 높이가 absolute 자식만큼 늘어난다고 착각
- fixed header가 콘텐츠를 가림
- sticky에 top offset 누락
- sticky 부모에 overflow hidden / auto 존재
- z-index 숫자만 무작정 높임
- stacking context 확인 누락
- transform 부모가 stacking context를 만드는 것을 놓침
- overflow hidden으로 dropdown / tooltip 잘림
- modal layer가 header보다 낮음
- 닫힌 dropdown 내부 요소가 focus 가능 상태로 남음
- visual order와 DOM order를 과도하게 다르게 만듦
- hover-only tooltip으로 keyboard 접근성 누락
- mobile viewport에서 fixed bottom UI가 safe area와 충돌

---

### [실무]

Troubleshooting Flow:

```text
Layer Issue
→ 일반 Layout 문제인지 확인
→ position 값 확인
→ 기준 부모 확인
→ normal flow 영향 확인
→ offset 확인
→ z-index scale 확인
→ stacking context 확인
→ overflow clipping 확인
→ scroll container 확인
→ accessibility state 확인
```

문제 예:

```text
문제: Tooltip이 카드 밖으로 나오지 못하고 잘림
원인: 카드 부모의 overflow hidden
해결: Tooltip layer를 clipping container 밖으로 이동 또는 portal 사용
```

```text
문제: Modal 뒤의 버튼으로 focus가 이동함
원인: focus trap 없음
해결: Modal focus trap 및 background inert 처리 검토
```

```text
문제: sticky sidebar가 동작하지 않음
원인: 부모 overflow 또는 align stretch
해결: scroll container 확인, align-self start, top offset 적용
```

---

### [FAQ]

Q. Position에서 가장 흔한 실수는 뭐야?
A. absolute 기준 부모를 만들지 않거나 단순 정렬을 position으로 해결하는 실수다.

Q. z-index에서 가장 흔한 실수는 뭐야?
A. stacking context를 확인하지 않고 숫자만 계속 높이는 실수다.

Q. Dropdown이 잘리는 흔한 이유는 뭐야?
A. 부모의 overflow hidden 또는 scroll container clipping 때문이다.

Q. Position 문제는 어떤 순서로 디버깅해?
A. position 값, 기준 부모, offset, z-index, stacking context, overflow, scroll container, 접근성 상태 순서로 확인한다.

---

# 16. Best Practice

## 16.1 Position ZIndex Best Practice

### [개념]

Position ZIndex Best Practice는 Layer UI, Floating UI, Sticky UI, Overlay UI를 안정적으로 구현하고 z-index 충돌과 접근성 문제를 줄이는 작성 기준이다.

---

### [핵심]

권장 기준:

- 일반 Layout은 Flexbox / Grid 우선 사용
- Position은 겹침, 고정, 기준 배치가 필요할 때 사용
- absolute 자식 기준 부모에는 `position: relative` 명시
- absolute 요소가 normal flow에서 빠지는 영향 확인
- fixed 요소가 콘텐츠를 가리지 않도록 offset 설계
- sticky에는 `top` 또는 `bottom` offset 지정
- sticky 동작 전 부모 overflow / scroll container 확인
- z-index scale을 정의해 layer 순서 관리
- 무작정 큰 z-index 숫자 사용 금지
- stacking context 발생 조건 확인
- overflow hidden과 floating layer 분리
- Modal / Dropdown은 focus와 keyboard 접근성 함께 설계
- 닫힌 layer 내부 요소는 focus되지 않게 관리
- DOM 순서와 시각 순서가 과도하게 어긋나지 않게 설계
- React에서는 필요 시 Portal 사용 검토

---

### [실무]

Layer Scale 예:

```css
:root {
  --z-dropdown: 20;
  --z-sticky: 30;
  --z-header: 40;
  --z-toast: 80;
  --z-modal: 100;
}
```

Badge 예:

```css
.notification-button {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: -6px;
  right: -6px;
}
```

Dropdown 예:

```css
.dropdown {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  z-index: var(--z-dropdown);
}
```

Modal 예:

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  display: grid;
  place-items: center;
}
```

Sticky Header 예:

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-header);
  background-color: white;
}
```

검수 Checklist:

```md
- [ ] 일반 Layout 문제를 position으로 해결하지 않았는가?
- [ ] absolute 기준 부모에 `position: relative`가 있는가?
- [ ] absolute 요소가 normal flow에서 빠져도 되는가?
- [ ] fixed 요소가 콘텐츠를 가리지 않는가?
- [ ] sticky 요소에 top/bottom offset이 있는가?
- [ ] sticky 부모 overflow가 동작을 방해하지 않는가?
- [ ] z-index scale이 정의되어 있는가?
- [ ] stacking context를 만드는 부모가 없는가?
- [ ] overflow hidden으로 Dropdown / Tooltip이 잘리지 않는가?
- [ ] Modal / Dropdown focus 관리가 되어 있는가?
- [ ] 닫힌 layer 내부 요소가 focus되지 않는가?
- [ ] DOM 순서와 시각 순서가 접근성에 문제 없는가?
```

---

### [FAQ]

Q. Position ZIndex Best Practice는 뭐야?
A. 일반 Layout은 Flexbox/Grid로 처리하고, Layer UI에만 position을 사용하며 z-index와 stacking context를 체계적으로 관리하는 것이다.

Q. Position 검수에서 가장 먼저 볼 것은 뭐야?
A. position 값, 기준 부모, normal flow 영향, offset, z-index, stacking context를 먼저 확인한다.

Q. z-index 관리는 어떻게 하는 게 좋아?
A. dropdown, sticky, header, toast, modal 같은 layer scale을 정해 변수로 관리하는 것이 좋다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Position, z-index, Stacking Context를 기준으로 Dropdown, Modal, Badge, Sticky UI를 안정적으로 생성하고 디버깅하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. CSS position이 뭐야?
A. 요소를 일반 문서 흐름 또는 특정 기준점에 따라 배치하는 CSS property다.

Q. position은 언제 써?
A. Tooltip, Dropdown, Modal, Sticky Header, Badge, Floating Button 같은 Layer UI에 사용한다.

Q. position 문제는 무엇부터 확인해?
A. position 값, 기준 부모, inset 값, z-index, stacking context, scroll container를 확인한다.

Q. position static은 뭐야?
A. 요소가 일반 문서 흐름에 따라 배치되는 기본 position 값이다.

Q. static 요소에 top을 주면 이동해?
A. 일반적으로 이동하지 않는다. top, left 같은 offset은 positioned element에서 의미가 있다.

Q. position relative는 뭐야?
A. 요소를 원래 위치 기준으로 이동할 수 있게 하고 absolute 자식의 기준 부모가 될 수 있는 position 값이다.

Q. relative를 주면 normal flow에서 빠져?
A. 아니다. 원래 공간은 유지된다.

Q. relative는 언제 많이 써?
A. absolute 자식 요소의 기준 부모를 만들 때 많이 사용한다.

Q. position absolute는 뭐야?
A. 요소를 normal flow에서 제거하고 기준 부모를 기준으로 배치하는 position 값이다.

Q. absolute 기준은 무엇이야?
A. 가장 가까운 positioned ancestor가 기준이 된다.

Q. absolute 자식이 부모 밖으로 이상하게 가는 이유는?
A. 부모에 `position: relative` 같은 기준 position이 없기 때문일 수 있다.

Q. absolute 요소는 부모 높이에 영향을 줘?
A. 일반적으로 주지 않는다. normal flow에서 제거되기 때문이다.

Q. position fixed는 뭐야?
A. 요소를 viewport 기준으로 고정 배치하는 position 값이다.

Q. fixed 요소는 scroll해도 움직이지 않아?
A. 맞다. viewport 기준 위치에 고정된다.

Q. fixed header가 본문을 가리면 어떻게 해?
A. Header 높이만큼 본문 padding 또는 layout offset을 제공해야 한다.

Q. position sticky는 뭐야?
A. scroll 위치에 따라 일반 흐름에 있다가 특정 위치에서 고정되는 position 값이다.

Q. sticky가 안 먹는 이유는 뭐야?
A. top 같은 offset 누락, 부모 overflow 설정, 부모 높이 부족, scroll container 문제 때문일 수 있다.

Q. sticky에는 top이 꼭 필요해?
A. 일반적으로 sticky 기준 위치를 만들기 위해 `top` 또는 `bottom` 같은 offset이 필요하다.

Q. sticky와 fixed 차이는 뭐야?
A. fixed는 항상 viewport 기준으로 고정되고 sticky는 scroll 조건에 따라 부모 영역 안에서 고정된다.

Q. top right bottom left는 뭐야?
A. positioned element의 기준점으로부터 위치를 조정하는 offset property다.

Q. top을 줬는데 요소가 안 움직이는 이유는?
A. 요소가 `position: static` 상태이기 때문일 수 있다.

Q. absolute의 top 기준은 뭐야?
A. 가장 가까운 positioned ancestor의 padding box를 기준으로 하는 경우가 많다.

Q. fixed의 top 기준은 뭐야?
A. 일반적으로 viewport를 기준으로 한다.

Q. inset은 뭐야?
A. top, right, bottom, left를 한 번에 지정하는 CSS shorthand property다.

Q. inset 0은 무슨 뜻이야?
A. `top: 0; right: 0; bottom: 0; left: 0;`과 같다.

Q. inset은 언제 써?
A. Modal Backdrop, Overlay, absolute fill처럼 전체 영역을 채울 때 자주 사용한다.

Q. z-index가 뭐야?
A. 요소가 z축에서 어떤 순서로 쌓이는지 결정하는 CSS property다.

Q. z-index가 큰데도 위로 안 올라오는 이유는?
A. 다른 stacking context 안에 있어서 같은 기준으로 비교되지 않기 때문일 수 있다.

Q. z-index는 숫자가 클수록 좋아?
A. 아니다. layer 기준을 정해 필요한 범위에서 관리하는 것이 좋다.

Q. z-index는 언제 써?
A. Dropdown, Header, Modal, Toast, Overlay처럼 겹치는 UI의 순서를 제어할 때 사용한다.

Q. Stacking Context가 뭐야?
A. 요소들이 z축에서 쌓이는 독립적인 비교 그룹이다.

Q. z-index가 안 먹는 이유는 뭐야?
A. 다른 stacking context에 있거나 부모 stacking context에 갇혀 있기 때문일 수 있다.

Q. transform도 z-index 문제를 만들 수 있어?
A. 그렇다. transform은 새로운 stacking context를 만들 수 있다.

Q. Modal이나 Dropdown이 계속 가려지면 어떻게 해?
A. stacking context, overflow clipping, DOM 위치, portal 사용 필요성을 확인한다.

Q. overflow clipping이 뭐야?
A. 요소가 부모 영역 밖으로 나갈 때 부모 overflow 설정 때문에 잘리는 현상이다.

Q. z-index를 높였는데 dropdown이 잘리는 이유는?
A. z-index 문제가 아니라 부모의 overflow clipping 문제일 수 있다.

Q. dropdown이 부모 밖에서 잘리면 어떻게 해?
A. overflow 구조를 수정하거나 dropdown을 상위 layer 또는 portal로 이동하는 방식을 검토한다.

Q. Badge는 position으로 어떻게 만들어?
A. 부모에 `position: relative`, Badge에 `position: absolute`를 주고 top/right로 배치한다.

Q. Badge 숫자가 접근성에 필요하면 어떻게 해?
A. 버튼의 aria-label이나 숨김 텍스트로 unread count 의미를 제공한다.

Q. Dropdown은 position으로 어떻게 만들어?
A. 부모에 `position: relative`, menu에 `position: absolute`를 주고 trigger 기준으로 배치한다.

Q. Dropdown이 다른 요소 뒤에 숨으면?
A. z-index와 stacking context를 확인한다.

Q. Dropdown에는 접근성 처리가 필요해?
A. 필요하다. aria-expanded, keyboard navigation, focus 관리가 중요하다.

Q. Modal Overlay는 position으로 어떻게 만들어?
A. Backdrop에 `position: fixed`, `inset: 0`, 높은 z-index를 주고 Dialog를 중앙 정렬한다.

Q. Modal은 CSS만으로 충분해?
A. 아니다. focus trap, keyboard handling, scroll lock, aria 처리가 함께 필요하다.

Q. Sticky Header는 어떻게 만들어?
A. Header에 `position: sticky`, `top: 0`, 필요한 z-index와 background를 적용한다.

Q. sticky header가 안 붙는 이유는?
A. top 누락, 부모 overflow, scroll container, 부모 높이 문제 때문일 수 있다.

Q. position UI도 접근성이 중요해?
A. 중요하다. Dropdown, Modal, Tooltip, Sticky Header는 focus와 keyboard 접근성 문제가 자주 발생한다.

Q. Modal 접근성에서 중요한 것은 뭐야?
A. role dialog, aria-modal, focus trap, Escape 닫기, background focus 차단이 중요하다.

Q. fixed header가 접근성 문제를 만들 수 있어?
A. 가능하다. focus target이나 skip link 대상이 header에 가려질 수 있다.

Q. absolute 요소가 엉뚱한 곳에 가는 이유는?
A. 기준 부모가 없거나 예상한 부모가 positioned element가 아니기 때문일 수 있다.

Q. z-index를 높여도 안 보이는 이유는?
A. stacking context나 overflow clipping 문제일 수 있다.

Q. sticky가 안 되는 이유는?
A. top offset 누락, 부모 overflow, 부모 높이 부족, scroll container 문제를 확인해야 한다.

Q. relative와 absolute 차이는 뭐야?
A. relative는 normal flow 공간을 유지하고 absolute는 normal flow에서 제거된다.

Q. fixed와 sticky 차이는 뭐야?
A. fixed는 항상 viewport 기준으로 고정되고 sticky는 scroll 조건에 따라 부모 영역 안에서 고정된다.

Q. absolute와 fixed 차이는 뭐야?
A. absolute는 positioned ancestor 기준이고 fixed는 일반적으로 viewport 기준이다.

Q. z-index와 stacking context 차이는 뭐야?
A. z-index는 순서 값이고 stacking context는 그 값이 비교되는 독립 그룹이다.

Q. z-index 9999도 안 먹는 이유는?
A. 부모 stacking context 안에 갇혀 다른 context의 요소와 직접 비교되지 않기 때문일 수 있다.

Q. fixed와 sticky 중 언제 fixed를 써?
A. viewport 기준으로 항상 고정되어야 하는 UI에 사용한다.

Q. fixed와 sticky 중 언제 sticky를 써?
A. normal flow를 유지하면서 scroll 시 특정 위치에 붙게 하고 싶을 때 사용한다.

Q. Layout 정렬을 position으로 해도 돼?
A. 일반 정렬에는 권장하지 않는다. Flexbox나 Grid를 우선 고려한다.

Q. position은 언제 써야 해?
A. 요소를 겹치거나 viewport/부모 기준으로 고정 배치해야 할 때 사용한다.

Q. Position에서 가장 흔한 실수는 뭐야?
A. absolute 기준 부모를 만들지 않거나 단순 정렬을 position으로 해결하는 실수다.

Q. z-index에서 가장 흔한 실수는 뭐야?
A. stacking context를 확인하지 않고 숫자만 계속 높이는 실수다.

Q. Dropdown이 잘리는 흔한 이유는 뭐야?
A. 부모의 overflow hidden 또는 scroll container clipping 때문이다.

Q. Position 문제는 어떤 순서로 디버깅해?
A. position 값, 기준 부모, offset, z-index, stacking context, overflow, scroll container, 접근성 상태 순서로 확인한다.

Q. Position ZIndex Best Practice는 뭐야?
A. 일반 Layout은 Flexbox/Grid로 처리하고, Layer UI에만 position을 사용하며 z-index와 stacking context를 체계적으로 관리하는 것이다.

Q. Position 검수에서 가장 먼저 볼 것은 뭐야?
A. position 값, 기준 부모, normal flow 영향, offset, z-index, stacking context를 먼저 확인한다.

Q. z-index 관리는 어떻게 하는 게 좋아?
A. dropdown, sticky, header, toast, modal 같은 layer scale을 정해 변수로 관리하는 것이 좋다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 Position, z-index, Stacking Context를 기준으로 Dropdown, Modal, Badge, Sticky UI를 안정적으로 생성하고 디버깅하게 만드는 것이다.
