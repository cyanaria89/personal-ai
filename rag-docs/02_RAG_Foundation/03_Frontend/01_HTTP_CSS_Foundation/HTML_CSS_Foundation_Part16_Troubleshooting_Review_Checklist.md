# HTML CSS Foundation Part16 - Troubleshooting Review Checklist

---

# 1. Document Role

## 1.1 Document Role Concept

### [개념]

이 문서는 HTML/CSS Foundation 전체 문서의 최종 Troubleshooting과 Review 기준이다.

Part16은 개별 기술을 새로 설명하는 문서가 아니라, Part01~Part15에서 다룬 HTML 구조, CSS 문법, Layout, Responsive, Accessibility, Component, Architecture 기준을 실제 문제 진단과 검수 흐름으로 연결하는 문서다.

---

### [핵심]

문서 역할:

- HTML/CSS 문제를 증상별로 분류한다.
- CSS Not Applied 문제를 진단한다.
- Cascade, Specificity, Inheritance 문제를 진단한다.
- Box Model, Display, Flexbox, Grid, Position 문제를 진단한다.
- Responsive 문제를 진단한다.
- Typography, Color, Spacing 문제를 진단한다.
- Form Accessibility 문제를 진단한다.
- Component Styling 문제를 진단한다.
- Reset/Base/Architecture 문제를 진단한다.
- 최종 Review Checklist를 제공한다.
- Frontend Agent와 Review Agent가 같은 기준으로 검수하도록 한다.

연계 기준:

- HTML Document Structure 문제는 Part01을 참조한다.
- Semantic HTML 문제는 Part02를 참조한다.
- Form Element 문제는 Part03을 참조한다.
- Text, Link, Image, List, Table 문제는 Part04를 참조한다.
- CSS selector, cascade, specificity 문제는 Part05를 함께 참조한다.
- Box Model과 Display 문제는 Part06을 함께 참조한다.
- Flexbox 문제는 Part07을 함께 참조한다.
- Grid 문제는 Part08을 함께 참조한다.
- Position, ZIndex, Stacking Context 문제는 Part09를 함께 참조한다.
- Responsive 문제는 Part10을 함께 참조한다.
- Typography, Color, Spacing 문제는 Part11을 함께 참조한다.
- CSS Variables, Pseudo Selector, Transition 문제는 Part12를 함께 참조한다.
- Reset/Base/Architecture 문제는 Part13을 함께 참조한다.
- Component 문제는 Part14를 함께 참조한다.
- Attribute, Accessibility, SEO 문제는 Part15를 함께 참조한다.

---

### [실무]

문서 사용 Flow:

```text
문제 증상 확인
→ 문제 범주 분류
→ 관련 Part 참조
→ DevTools로 실제 원인 확인
→ 최소 수정
→ 관련 Checklist 재검수
→ Part16 최종 Review 수행
```

문제 유형별 참조:

```text
HTML 구조 이상 → Part01 / Part02 / Part16
Form 오류 → Part03 / Part15 / Part16
Image alt / Table overflow → Part04 / Part10 / Part16
CSS 미적용 → Part05 / Part16
Box Model 깨짐 → Part06 / Part16
Flexbox 정렬 오류 → Part07 / Part16
Grid overflow → Part08 / Part16
Dropdown/Modal layer 오류 → Part09 / Part14 / Part16
Responsive overflow → Part10 / Part16
Color/Spacing/Readability 문제 → Part11 / Part16
State/Transition 문제 → Part12 / Part14 / Part16
Reset/Base 구조 문제 → Part13 / Part16
Component 접근성 문제 → Part14 / Part15 / Part16
```

---

### [FAQ]

Q. Part16은 어떤 문서야?
A. HTML/CSS Foundation 전체의 최종 Troubleshooting과 Review 기준 문서다.

Q. Part16은 새 개념 문서야?
A. 아니다. Part01~Part15의 기준을 문제 진단과 검수 흐름으로 연결하는 문서다.

Q. 문제가 생기면 Part16만 보면 돼?
A. Part16으로 원인을 분류하고, 세부 기준은 관련 Part를 함께 참조해야 한다.

Q. Part16의 최종 목적은 뭐야?
A. Frontend Agent와 Review Agent가 HTML/CSS 문제를 체계적으로 진단하고 동일한 기준으로 품질을 검수하게 만드는 것이다.

---

# 2. HTML CSS Troubleshooting

## 2.1 Troubleshooting Concept

### [개념]

HTML CSS Troubleshooting은 화면이 예상과 다르게 표시되거나, Layout이 깨지거나, 접근성 상태가 맞지 않거나, 스타일이 적용되지 않는 문제를 원인별로 분석하는 과정이다.

HTML/CSS 문제는 대부분 아래 범주 중 하나에 속한다.

- HTML 구조 문제
- Semantic HTML 문제
- Attribute 누락 문제
- CSS selector 문제
- Cascade / Specificity 문제
- Box Model 문제
- Display / Layout 문제
- Flexbox 문제
- Grid 문제
- Position / ZIndex 문제
- Responsive 문제
- Typography / Color / Spacing 문제
- Form Accessibility 문제
- Component State 문제
- Reset / Base Style 문제

---

### [핵심]

Troubleshooting 핵심:

- 증상을 먼저 명확히 분류한다.
- HTML 구조와 CSS 적용 여부를 분리해서 본다.
- DevTools에서 실제 DOM과 computed style을 확인한다.
- CSS가 안 먹는 문제와 CSS가 먹었지만 기대와 다른 문제를 구분한다.
- Layout 문제는 box model, display, parent-child 관계를 먼저 본다.
- Layer 문제는 position, z-index, stacking context, overflow를 본다.
- Responsive 문제는 viewport, fixed width, media query, overflow를 본다.
- 접근성 문제는 semantic element, focus, ARIA state, accessible name을 본다.
- Component 문제는 className, token, variant, state를 함께 본다.

---

### [실무]

Troubleshooting 전체 Flow:

```text
증상 확인
→ HTML DOM 구조 확인
→ CSS selector 매칭 확인
→ Computed Style 확인
→ Box Model 확인
→ Layout Context 확인
→ Responsive Viewport 확인
→ Accessibility State 확인
→ Component State 확인
→ 관련 Part 참조
→ 원인 분류
→ 최소 수정
→ 재검수
```

문제 분류 기준:

```text
스타일이 아예 안 먹음 → Part05 / selector / import / cascade / specificity
크기가 이상함 → Part06 / box model / width / padding / border / min-width
정렬이 이상함 → Part07 / Part08 / display / flex / grid / align
겹침이 이상함 → Part09 / position / z-index / stacking context / overflow
모바일에서 깨짐 → Part10 / media query / fixed width / image / table / minmax
키보드 접근 불가 → Part15 / semantic element / focus / hidden / aria
Component 상태 이상 → Part12 / Part14 / visual state / ARIA state / data-state
```

---

### [FAQ]

Q. HTML CSS Troubleshooting이 뭐야?
A. 화면, Layout, 스타일, 접근성 문제가 왜 발생했는지 HTML 구조와 CSS 적용 흐름을 기준으로 분석하는 과정이다.

Q. CSS 문제가 생기면 가장 먼저 뭘 봐?
A. DevTools에서 DOM 구조, selector 매칭, computed style, box model을 먼저 확인한다.

Q. Layout 문제는 어디서 시작해?
A. display 값, parent-child 관계, box model, width/min-width, overflow를 확인한다.

Q. 접근성 문제는 어디서 시작해?
A. semantic element, keyboard focus, accessible name, ARIA state, hidden/focus 상태를 확인한다.

---

# 3. CSS Not Applied

## 3.1 CSS Not Applied Concept

### [개념]

CSS Not Applied는 작성한 CSS가 요소에 적용되지 않거나, 적용되었지만 다른 CSS에 의해 덮어써지는 문제다.

주요 원인은 selector 불일치, className 오타, CSS import 누락, cascade 순서, specificity, media query 조건 불일치다.

---

### [핵심]

CSS Not Applied 주요 원인:

- CSS 파일이 import되지 않음
- className과 selector 이름 불일치
- selector가 실제 DOM 구조와 맞지 않음
- media query 조건이 현재 viewport와 맞지 않음
- 같은 property가 뒤에서 override됨
- specificity가 낮아 다른 selector에 밀림
- inline style이 우선 적용됨
- `!important`가 다른 style을 덮음
- CSS syntax error로 rule이 무시됨
- build/cache 문제로 최신 CSS가 반영되지 않음

---

### [실무]

Debug Flow:

```text
CSS 파일 import 확인
→ DevTools Elements에서 className 확인
→ Styles 패널에서 selector 매칭 확인
→ 취소선 CSS 확인
→ Computed Style 확인
→ Source Order 확인
→ Specificity 확인
→ Media Query 활성 여부 확인
→ Syntax Error 확인
→ Part05 참조
```

예:

```text
문제: button-primary 스타일이 적용되지 않음
원인: JSX className은 button-priamry, CSS selector는 .button-primary
해결: className 오타 수정
```

```text
문제: 모바일 CSS가 적용되지 않음
원인: @media (min-width: 768px)를 max-width처럼 이해
해결: viewport 조건 재확인
```

검수 기준:

- CSS 파일이 로드되었는가?
- className과 selector가 정확히 일치하는가?
- DevTools Styles 패널에 rule이 표시되는가?
- rule이 취소선 처리되어 있다면 어떤 rule이 덮는가?
- media query가 현재 viewport에서 활성화되는가?

---

### [FAQ]

Q. CSS가 안 먹을 때 가장 먼저 확인할 것은?
A. CSS 파일 import 여부와 className / selector 이름 일치 여부를 확인한다.

Q. DevTools에서 CSS가 취소선이면 무슨 뜻이야?
A. 해당 rule이 다른 CSS rule에 의해 override되었거나 적용 우선순위에서 밀렸다는 뜻이다.

Q. className 오타는 어떻게 찾나?
A. Elements 패널의 실제 DOM class와 CSS selector를 직접 비교한다.

Q. media query 안 CSS가 안 먹으면?
A. 현재 viewport width와 min-width / max-width 조건을 확인한다.

---

# 4. Cascade Specificity Debugging

## 4.1 Cascade Debug

### [개념]

Cascade Debugging은 여러 CSS rule 중 어떤 rule이 최종 적용되는지 확인하는 과정이다.

CSS는 cascade, specificity, source order, inheritance에 따라 최종 style이 결정된다.

---

### [핵심]

Cascade 핵심:

- 같은 property에 여러 rule이 적용될 수 있다.
- specificity가 높은 selector가 우선한다.
- specificity가 같으면 나중에 작성된 rule이 우선한다.
- inline style은 일반 stylesheet보다 우선순위가 높다.
- `!important`는 cascade를 강하게 변경한다.
- inherited property는 부모에서 자식으로 전달될 수 있다.
- DevTools Computed Style은 최종 적용값을 보여준다.
- CSS selector, cascade, specificity 기초는 Part05 기준을 따른다.

---

### [실무]

Debug Flow:

```text
문제 property 확인
→ DevTools Computed에서 최종값 확인
→ Styles에서 competing rule 확인
→ specificity 비교
→ source order 확인
→ inline style 확인
→ important 사용 여부 확인
→ 불필요한 selector 단순화
→ Part05 기준 검토
```

문제 예:

```text
문제: .button color가 안 바뀜
원인: .header .nav .button selector가 더 높은 specificity로 color 지정
해결: component selector 구조 단순화 또는 style 책임 분리
```

주의 예:

```css
#saveButton {
  color: red;
}
```

ID selector는 specificity가 높아 override를 어렵게 만들 수 있다.

---

### [FAQ]

Q. Cascade Debugging이 뭐야?
A. 여러 CSS rule 중 어떤 rule이 최종 적용되는지 cascade, specificity, source order 기준으로 확인하는 과정이다.

Q. specificity가 뭐야?
A. selector의 우선순위를 계산하는 기준이다.

Q. 같은 specificity면 어떤 CSS가 적용돼?
A. 나중에 작성되거나 나중에 로드된 rule이 우선 적용된다.

Q. !important를 쓰면 해결돼?
A. 임시로는 가능하지만 유지보수와 디버깅을 어렵게 하므로 남용하면 안 된다.

---

# 5. Box Model Troubleshooting

## 5.1 Box Model Bug

### [개념]

Box Model Bug는 요소의 실제 크기, padding, border, margin, overflow가 예상과 다르게 계산되는 문제다.

주요 원인은 `box-sizing`, fixed width, padding, border, margin collapse, overflow, min-width, max-width 오해다.

---

### [핵심]

Box Model 문제 원인:

- `box-sizing: content-box`로 padding과 border가 width에 추가됨
- width 100% input에 padding이 더해져 overflow 발생
- margin collapse로 세로 간격이 예상과 다름
- 부모 width보다 큰 fixed width 사용
- min-width 기본값 때문에 flex/grid item이 줄어들지 않음
- max-width 누락
- overflow hidden으로 content 또는 focus ring이 잘림
- border 추가로 layout이 흔들림
- Box Model과 Display 기본 기준은 Part06을 따른다.

---

### [실무]

Debug Flow:

```text
DevTools Box Model 확인
→ width / height 확인
→ padding / border / margin 확인
→ box-sizing 확인
→ min-width / max-width 확인
→ overflow 확인
→ parent width 확인
→ Part06 기준 검토
```

해결 예:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

.form-input {
  width: 100%;
  min-width: 0;
}
```

문제 예:

```text
문제: input이 form 영역 밖으로 넘침
원인: width 100% + padding + content-box
해결: box-sizing border-box 적용
```

검수 기준:

- 전역 box-sizing이 적용되어 있는가?
- width 100% 요소가 padding 때문에 넘치지 않는가?
- margin collapse가 의도한 간격인가?
- min-width 0이 필요한 flex/grid item인가?
- overflow hidden이 focus ring이나 dropdown을 자르지 않는가?

---

### [FAQ]

Q. Box Model 문제가 생기면 무엇을 확인해?
A. width, padding, border, margin, box-sizing, min-width, overflow를 확인한다.

Q. width 100%인데 요소가 넘치는 이유는?
A. content-box에서 padding과 border가 width에 추가되기 때문일 수 있다.

Q. margin collapse는 뭐야?
A. 인접한 block 요소의 세로 margin이 합쳐지는 CSS 동작이다.

Q. flex item이 줄어들지 않는 이유는?
A. 기본 min-width 때문에 줄어들지 않을 수 있어 `min-width: 0`을 검토한다.

---

# 6. Display Layout Troubleshooting

## 6.1 Display Bug

### [개념]

Display Bug는 요소가 block, inline, inline-block, flex, grid, none 같은 display 특성 때문에 예상과 다르게 배치되는 문제다.

---

### [핵심]

Display 문제 원인:

- inline 요소에 width/height가 적용되지 않음
- block 요소가 한 줄 전체를 차지함
- inline image 하단 공백 발생
- `display: none`으로 accessibility tree에서도 숨김
- flex/grid container가 잘못된 요소에 적용됨
- direct child가 아닌 요소를 flex/grid item으로 착각
- visibility hidden과 display none을 혼동
- hidden 요소에 transition을 기대함
- Display 기본 기준은 Part06을 따른다.

---

### [실무]

Debug Flow:

```text
display 값 확인
→ block/inline 특성 확인
→ parent display 확인
→ direct child 관계 확인
→ hidden/display none 여부 확인
→ DevTools Layout panel 확인
→ Part06 기준 검토
```

예:

```css
img {
  display: block;
  max-width: 100%;
}
```

```text
문제: span에 width가 적용되지 않음
원인: span은 inline 요소
해결: display inline-block 또는 block 검토
```

검수 기준:

- 요소 display 값이 의도와 맞는가?
- width/height를 적용해야 하는 요소가 inline인가?
- flex/grid가 부모에 적용되어 있는가?
- 직접 자식만 flex/grid item임을 이해했는가?
- display none과 visibility hidden을 의도에 맞게 사용했는가?

---

### [FAQ]

Q. Display Bug에서 가장 먼저 볼 것은?
A. 해당 요소와 부모 요소의 display 값을 확인한다.

Q. inline 요소에 width가 안 먹는 이유는?
A. inline 요소는 일반적으로 width/height가 적용되지 않기 때문이다.

Q. display none과 visibility hidden 차이는?
A. display none은 layout에서 제거되고 visibility hidden은 공간을 유지한 채 보이지 않는다.

Q. flex item은 어떤 요소야?
A. flex container의 직접 자식 요소다.

---

# 7. Flexbox Troubleshooting

## 7.1 Flexbox Bug

### [개념]

Flexbox Bug는 1차원 Layout에서 item 정렬, 줄바꿈, 크기 분배, overflow가 예상과 다르게 동작하는 문제다.

---

### [핵심]

Flexbox 문제 원인:

- flex container가 잘못된 요소에 적용됨
- flex item이 직접 자식이 아님
- main axis와 cross axis 혼동
- `justify-content`와 `align-items` 혼동
- `flex-wrap` 누락
- item `min-width` 때문에 overflow 발생
- `flex: 1`로 item이 예상보다 늘어남
- `flex-basis`와 width의 관계 오해
- gap 대신 margin을 복잡하게 사용
- 모바일에서 row 유지로 overflow 발생
- Flexbox 상세 기준은 Part07을 따른다.

---

### [실무]

Debug Flow:

```text
display flex 확인
→ direct child item 확인
→ flex-direction 확인
→ main/cross axis 확인
→ justify-content / align-items 확인
→ flex-wrap 확인
→ flex item min-width 확인
→ gap 확인
→ responsive viewport 확인
→ Part07 기준 검토
```

해결 예:

```css
.toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.toolbar-item {
  min-width: 0;
}
```

문제 예:

```text
문제: 검색 input이 버튼을 밀어내며 overflow 발생
원인: flex item min-width 기본값
해결: input wrapper에 min-width: 0 적용
```

검수 기준:

- flex container와 flex item 관계가 맞는가?
- axis 방향을 정확히 이해했는가?
- wrap이 필요한 layout인가?
- item이 줄어들 수 있게 min-width 0이 필요한가?
- 모바일에서 column 전환이 필요한가?

---

### [FAQ]

Q. Flexbox 문제가 생기면 무엇부터 확인해?
A. container, direct child, flex-direction, axis, justify-content, align-items를 확인한다.

Q. justify-content와 align-items 차이는?
A. justify-content는 main axis 정렬이고 align-items는 cross axis 정렬이다.

Q. flex item이 넘치는 이유는?
A. min-width, fixed width, flex-basis, 긴 텍스트 때문에 줄어들지 못할 수 있다.

Q. flex-wrap은 언제 필요해?
A. item이 한 줄에 다 들어가지 않을 수 있는 toolbar, tag list, button group에서 필요하다.

---

# 8. Grid Troubleshooting

## 8.1 Grid Bug

### [개념]

Grid Bug는 2차원 Layout에서 column, row, gap, item span, responsive track이 예상과 다르게 동작하는 문제다.

---

### [핵심]

Grid 문제 원인:

- grid container가 잘못된 요소에 적용됨
- grid item이 직접 자식이 아님
- `grid-template-columns`가 고정되어 mobile overflow 발생
- `minmax()` 최소값이 너무 큼
- `gap`과 column 최소값 합이 viewport를 초과함
- `grid-column: span`이 모바일에서 유지됨
- `auto-fit`과 `auto-fill` 차이 오해
- `justify-items`와 `justify-content` 혼동
- 긴 텍스트 때문에 grid item이 overflow
- page layout에서 `minmax(0, 1fr)` 누락
- Grid 상세 기준은 Part08을 따른다.

---

### [실무]

Debug Flow:

```text
display grid 확인
→ direct child item 확인
→ grid-template-columns 확인
→ gap 확인
→ minmax 최소값 확인
→ item span 확인
→ min-width 확인
→ auto-fit / auto-fill 확인
→ responsive viewport 확인
→ Part08 기준 검토
```

해결 예:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: var(--space-6);
}

.page-main {
  min-width: 0;
}
```

문제 예:

```text
문제: 모바일에서 카드 grid가 가로 스크롤을 만듦
원인: repeat(3, 1fr) 고정 column
해결: mobile 1 column 또는 auto-fit minmax 적용
```

검수 기준:

- grid container와 item 관계가 맞는가?
- column 정의가 모바일에 적합한가?
- minmax 최소값이 viewport보다 크지 않은가?
- span item이 작은 화면에서 해제되는가?
- main content 영역에 min-width 0이 필요한가?

---

### [FAQ]

Q. Grid 문제가 생기면 무엇부터 확인해?
A. grid container, direct child item, grid-template-columns, gap, minmax, item span을 확인한다.

Q. 모바일에서 Grid가 넘치는 이유는?
A. 고정 column, 큰 minmax 최소값, 큰 gap, span item, 긴 텍스트 때문일 수 있다.

Q. auto-fit과 auto-fill 차이는?
A. auto-fit은 빈 track을 collapse할 수 있고 auto-fill은 빈 slot을 유지할 수 있다.

Q. grid item이 줄어들지 않으면?
A. item 또는 main 영역에 `min-width: 0`을 검토한다.

---

# 9. Position ZIndex Troubleshooting

## 9.1 Position ZIndex Bug

### [개념]

Position ZIndex Bug는 요소가 엉뚱한 위치에 배치되거나, 다른 요소에 가려지거나, z-index를 높여도 보이지 않는 문제다.

주요 원인은 기준 부모 누락, offset 오해, stacking context, overflow clipping, scroll container 문제다.

---

### [핵심]

Position / ZIndex 문제 원인:

- absolute 기준 부모에 `position: relative` 누락
- top/left가 static 요소에 적용되지 않음
- absolute 요소가 normal flow에서 빠지는 것을 놓침
- fixed 요소가 콘텐츠를 가림
- sticky에 top offset 누락
- sticky 부모 overflow 문제
- z-index만 높이고 stacking context를 확인하지 않음
- transform/opacity/filter로 stacking context 생성
- overflow hidden으로 dropdown/tooltip이 잘림
- modal/dropdown DOM 위치가 layer 구조에 부적합함
- Position/ZIndex 상세 기준은 Part09를 따른다.

---

### [실무]

Debug Flow:

```text
position 값 확인
→ offset 값 확인
→ containing block 확인
→ normal flow 영향 확인
→ z-index 확인
→ stacking context 확인
→ overflow clipping 확인
→ scroll container 확인
→ viewport responsive 확인
→ Part09 기준 검토
```

문제 예:

```text
문제: Badge가 카드 기준이 아니라 화면 기준으로 이동
원인: 카드에 position relative 없음
해결: badge 기준 부모인 card에 position relative 추가
```

```text
문제: Dropdown z-index 9999인데도 잘림
원인: 부모 overflow hidden clipping
해결: overflow 구조 수정 또는 portal/layer root 검토
```

검수 기준:

- absolute 기준 부모가 의도와 맞는가?
- z-index 비교가 같은 stacking context 안에서 이루어지는가?
- overflow clipping 문제를 z-index 문제로 오해하지 않았는가?
- sticky offset과 scroll container가 올바른가?
- modal/dropdown layer가 DOM 구조상 적절한가?

---

### [FAQ]

Q. absolute 요소가 엉뚱한 곳에 가는 이유는?
A. 기준이 되는 positioned ancestor가 없기 때문일 수 있다.

Q. z-index를 크게 줬는데 안 보이는 이유는?
A. stacking context가 다르거나 overflow clipping 때문에 가려질 수 있다.

Q. sticky가 안 되는 이유는?
A. top offset 누락, 부모 overflow, 부모 높이, scroll container 문제 때문일 수 있다.

Q. dropdown이 부모 밖으로 잘리면?
A. overflow hidden/auto 부모를 확인하고 portal 또는 layer 구조 변경을 검토한다.

---

# 10. Responsive Troubleshooting

## 10.1 Responsive Bug

### [개념]

Responsive Bug는 특정 viewport에서 Layout이 깨지거나 가로 스크롤이 생기거나, text, image, component가 화면에 맞지 않는 문제다.

---

### [핵심]

Responsive 문제 원인:

- viewport meta 누락
- fixed width 남용
- `width: 100vw`로 scrollbar 포함 overflow 발생
- image max-width 누락
- table overflow-x 처리 누락
- flex-wrap 누락
- grid minmax 최소값 과다
- media query 조건 오해
- mobile에서 button group row 유지
- modal max-height/overflow 누락
- fixed bottom UI가 content를 가림
- text wrapping 누락
- touch target 부족
- Responsive 기준은 Part10을 따른다.

---

### [실무]

Debug Flow:

```text
Viewport Meta 확인
→ mobile viewport 재현
→ horizontal overflow 확인
→ fixed width 확인
→ image/table 확인
→ flex/grid wrap 확인
→ media query 조건 확인
→ component width 확인
→ typography/touch target 확인
→ Part10 기준 검토
```

해결 예:

```css
.container {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}

img {
  max-width: 100%;
  height: auto;
}

.long-text {
  overflow-wrap: break-word;
}
```

문제 예:

```text
문제: 모바일에서 body 가로 스크롤 발생
원인: 360px fixed width card + 320px viewport
해결: width 100%, max-width, responsive grid 적용
```

검수 기준:

- viewport meta가 있는가?
- body에 가로 스크롤이 생기는가?
- fixed width 요소가 있는가?
- image와 table이 viewport를 넘지 않는가?
- media query가 의도한 조건에서 적용되는가?
- touch target이 충분한가?

---

### [FAQ]

Q. Responsive Bug에서 가장 흔한 원인은?
A. fixed width, image max-width 누락, table overflow, flex/grid wrap 누락, media query 조건 오해다.

Q. 모바일 가로 스크롤은 어떻게 찾나?
A. DevTools에서 mobile viewport로 줄이고 viewport보다 넓은 요소를 찾는다.

Q. Media Query가 안 먹으면?
A. viewport meta, min-width/max-width 조건, CSS 순서, selector 매칭을 확인한다.

Q. Modal이 모바일에서 넘치면?
A. width, max-height, overflow auto, 100dvh 기반 계산을 적용한다.

---

# 11. Typography Color Spacing Troubleshooting

## 11.1 Visual Readability Bug

### [개념]

Visual Readability Bug는 텍스트가 읽기 어렵거나, 색상 대비가 낮거나, 여백이 불균형하거나, UI hierarchy가 불명확한 문제다.

---

### [핵심]

Typography / Color / Spacing 문제 원인:

- font-size가 너무 작음
- line-height가 너무 좁음
- heading hierarchy가 불명확함
- text contrast가 낮음
- 색상만으로 상태를 전달함
- link underline 제거 후 대체 단서 없음
- spacing scale 없이 임의 값 사용
- padding과 margin 역할 혼동
- gap 대신 item margin 난립
- 긴 본문 line length 제한 없음
- disabled / placeholder text가 너무 흐림
- mobile에서 touch target과 spacing 부족
- Typography, Color, Spacing 기준은 Part11을 따른다.

---

### [실무]

Debug Flow:

```text
Text Role 확인
→ font-size 확인
→ line-height 확인
→ contrast 확인
→ heading hierarchy 확인
→ link style 확인
→ spacing scale 확인
→ margin/padding/gap 역할 확인
→ mobile readability 확인
→ Part11 기준 검토
```

문제 예:

```text
문제: Error 상태가 색약 사용자에게 전달되지 않음
원인: input border color만 빨간색으로 변경
해결: error message, aria-invalid, icon 또는 텍스트 상태 제공
```

```text
문제: 카드들이 붙어 답답해 보임
원인: card padding과 card-grid gap 부족
해결: spacing token 기준으로 padding/gap 조정
```

검수 기준:

- 본문 font-size와 line-height가 읽기 쉬운가?
- 텍스트와 배경 contrast가 충분한가?
- link가 링크처럼 보이는가?
- 상태가 색상만으로 전달되지 않는가?
- spacing이 token 기반인가?
- mobile touch target이 충분한가?

---

### [FAQ]

Q. 텍스트가 읽기 어려우면 무엇을 확인해?
A. font-size, line-height, contrast, line length, spacing을 확인한다.

Q. 색상 문제는 무엇을 봐?
A. 텍스트와 배경 contrast, 상태 색상이 색상만으로 전달되는지 확인한다.

Q. 여백 문제는 무엇을 봐?
A. padding, margin, gap 역할과 spacing scale 사용 여부를 확인한다.

Q. link가 잘 안 보이면?
A. 색상뿐 아니라 underline, focus, hover style을 제공한다.

---

# 12. Form Accessibility Troubleshooting

## 12.1 Form Accessibility Bug

### [개념]

Form Accessibility Bug는 입력 필드의 이름, 설명, 오류, 상태가 사용자와 보조 기술에 제대로 전달되지 않는 문제다.

---

### [핵심]

Form Accessibility 문제 원인:

- label 누락
- placeholder를 label로 사용
- label for와 input id 불일치
- input name 누락
- fieldset/legend 누락
- error message가 aria-describedby와 연결되지 않음
- aria-invalid와 실제 오류 상태 불일치
- required 표시가 시각적으로만 존재
- disabled와 readonly 의미 혼동
- autocomplete 부정확
- focus-visible style 누락
- 색상만으로 오류 상태 표시
- Form Element 기준은 Part03, Attribute/ARIA 기준은 Part15를 따른다.

---

### [실무]

Debug Flow:

```text
Input 목적 확인
→ label 연결 확인
→ name/type 확인
→ helper/error id 확인
→ aria-describedby 확인
→ aria-invalid 확인
→ required/disabled/readonly 확인
→ focus-visible 확인
→ keyboard 조작 확인
→ Part03 / Part15 기준 검토
```

문제 예:

```text
문제: Error message가 화면에는 보이지만 screen reader가 읽지 않음
원인: aria-describedby가 error message id를 참조하지 않음
해결: input aria-describedby와 error id 연결
```

```text
문제: label 클릭해도 input에 focus가 가지 않음
원인: label for와 input id 불일치
해결: for와 id 값을 일치시킴
```

검수 기준:

- 모든 input에 visible label 또는 accessible label이 있는가?
- label과 input이 연결되어 있는가?
- error message가 input에 연결되어 있는가?
- aria-invalid가 실제 상태와 일치하는가?
- keyboard로 모든 form control을 조작할 수 있는가?

---

### [FAQ]

Q. Form 접근성 문제에서 가장 흔한 것은?
A. label 누락, placeholder label 대체, error message 연결 누락, aria-invalid 불일치다.

Q. placeholder를 label 대신 쓰면 왜 안 돼?
A. 입력 중 사라지고 필드 이름으로 안정적으로 전달되지 않기 때문이다.

Q. error message는 어떻게 연결해?
A. input의 aria-describedby가 error message id를 참조하게 한다.

Q. required 표시만 별표로 하면 충분해?
A. 아니다. 필수 입력 의미와 validation message도 함께 제공해야 한다.

---

# 13. Component Troubleshooting

## 13.1 Component Bug

### [개념]

Component Bug는 Button, Card, Modal, Dropdown, Tabs, Accordion 같은 UI Component가 style, state, accessibility, responsive 측면에서 예상대로 동작하지 않는 문제다.

---

### [핵심]

Component 문제 원인:

- semantic element 선택 오류
- button/link 역할 혼동
- button type 누락
- className 오타
- component CSS import 누락
- token variable 누락
- variant class 누락
- state attribute와 visual state 불일치
- hover만 있고 focus-visible 없음
- disabled 상태에도 hover/active 적용
- hidden content에 focus 가능 요소 존재
- modal focus trap 누락
- dropdown aria-expanded 불일치
- tabs aria-selected/hidden 불일치
- accordion trigger를 div로 구현
- fixed width로 responsive overflow 발생
- Component Pattern 기준은 Part14, Attribute/ARIA 기준은 Part15를 따른다.

---

### [실무]

Debug Flow:

```text
Component 역할 확인
→ Semantic Element 확인
→ className / CSS 확인
→ Token 확인
→ Variant 확인
→ State Attribute 확인
→ Focus Style 확인
→ Hidden / Focus 상태 확인
→ Responsive 확인
→ Part14 / Part15 기준 검토
```

문제 예:

```text
문제: Dropdown은 닫혔는데 Tab으로 내부 item에 접근됨
원인: hidden 상태와 focus 가능 상태 불일치
해결: hidden 처리 또는 focus management 적용
```

```text
문제: Tab UI에서 보이는 panel과 aria-selected가 다름
원인: visual state와 ARIA state 동기화 실패
해결: selected tab, visible panel, hidden panel 상태를 동시에 업데이트
```

검수 기준:

- component 역할에 맞는 semantic element인가?
- visual state와 aria state가 일치하는가?
- hidden panel 내부로 focus가 가지 않는가?
- keyboard interaction이 가능한가?
- responsive viewport에서 overflow가 없는가?

---

### [FAQ]

Q. Component Bug는 무엇부터 확인해?
A. semantic element, className, CSS import, variant/state, focus, ARIA 상태를 확인한다.

Q. button과 link를 혼동하면 왜 문제야?
A. 의미, keyboard 동작, form 동작, screen reader 정보가 달라지기 때문이다.

Q. Dropdown 닫힘 상태에서 focus가 들어가면?
A. hidden 처리나 focus management가 잘못된 것이므로 닫힌 content를 focus 불가능하게 해야 한다.

Q. Tabs 상태는 무엇을 동기화해야 해?
A. aria-selected, tabpanel hidden, visual active style을 함께 동기화해야 한다.

---

# 14. Reset Base Architecture Troubleshooting

## 14.1 Reset Base Bug

### [개념]

Reset Base Architecture Bug는 프로젝트 초기 CSS 기준이 없거나 잘못되어 브라우저 기본 스타일 차이, 접근성 손상, component style 충돌이 발생하는 문제다.

---

### [핵심]

Reset / Base 문제 원인:

- reset 파일 누락
- reset이 component CSS 뒤에 로드됨
- body margin 제거 누락
- box-sizing border-box 누락
- media element max-width 누락
- form element font inherit 누락
- focus outline 제거 후 대체 style 없음
- list reset을 전역 적용해 article list marker 제거
- base typography/color/background 누락
- CSS token 없이 임의 값 반복
- CSS 파일 구조 없이 모든 style 누적
- selector specificity가 계속 증가
- Reset/Base/Architecture 기준은 Part13을 따른다.

---

### [실무]

Debug Flow:

```text
CSS 파일 구조 확인
→ import order 확인
→ reset 적용 확인
→ base style 확인
→ focus-visible 확인
→ media reset 확인
→ form reset 확인
→ token 사용 확인
→ component override 확인
→ Part13 기준 검토
```

문제 예:

```text
문제: 브라우저마다 페이지 상단 여백이 다름
원인: body margin reset 누락
해결: body { margin: 0; } 적용
```

```text
문제: keyboard focus가 전혀 보이지 않음
원인: *:focus { outline: none; }만 적용
해결: :focus-visible 대체 style 제공
```

검수 기준:

- reset/base/component 로드 순서가 맞는가?
- body, box-sizing, media, form reset이 적용되었는가?
- focus-visible이 유지되는가?
- 전역 selector가 component style을 깨지 않는가?
- token 기반 구조가 있는가?

---

### [FAQ]

Q. Reset Base 문제는 무엇부터 확인해?
A. reset 파일 로드, import order, body margin, box-sizing, focus-visible을 확인한다.

Q. focus outline을 없애면 왜 문제야?
A. keyboard 사용자가 현재 조작 위치를 알 수 없기 때문이다.

Q. reset이 component CSS 뒤에 로드되면?
A. component style을 reset이 덮어써 예상 스타일이 깨질 수 있다.

Q. 전역 list reset은 왜 위험해?
A. 문서 본문의 list marker까지 제거해 콘텐츠 의미 표현을 해칠 수 있다.

---

# 15. Review Checklist

## 15.1 HTML Review Checklist

### [개념]

HTML Review Checklist는 HTML 구조가 semantic하고 접근 가능하며 SEO 친화적인지 검수하는 기준이다.

---

### [핵심]

HTML 검수 항목:

```md
- [ ] doctype이 있는가?
- [ ] html lang이 문서 언어와 일치하는가?
- [ ] charset UTF-8이 있는가?
- [ ] viewport meta가 있는가?
- [ ] title이 페이지별로 고유하고 구체적인가?
- [ ] meta description이 페이지 내용을 설명하는가?
- [ ] header/nav/main/footer landmark가 적절한가?
- [ ] main이 페이지 핵심 콘텐츠를 감싸는가?
- [ ] h1이 페이지 주요 제목인가?
- [ ] heading hierarchy가 논리적인가?
- [ ] section에 heading 또는 accessible name이 있는가?
- [ ] button과 link 역할이 구분되는가?
- [ ] button type이 명시되어 있는가?
- [ ] img alt가 의미에 맞는가?
- [ ] form label과 input이 연결되어 있는가?
- [ ] id가 중복되지 않는가?
```

---

### [실무]

검수 Flow:

```text
Document Metadata
→ Landmark
→ Heading
→ Interactive Element
→ Image Alt
→ Form Label
→ ARIA Reference
→ SEO Text
→ Part01 / Part02 / Part15 기준 연결
```

검수 기준:

- HTML만 봐도 콘텐츠 구조가 이해되는가?
- div/span 남용 없이 semantic element를 사용했는가?
- metadata가 라우트별로 관리되는가?
- heading이 시각 크기만이 아니라 구조를 표현하는가?

---

### [FAQ]

Q. HTML Review에서 가장 먼저 볼 것은?
A. document metadata, landmark, heading hierarchy, button/link 역할, image alt, form label을 먼저 본다.

Q. h1은 왜 중요해?
A. 페이지의 주요 제목과 주제를 나타내기 때문이다.

Q. section에 heading이 필요한 이유는?
A. section의 주제와 구조를 명확히 하기 위해서다.

---

## 15.2 CSS Review Checklist

### [개념]

CSS Review Checklist는 CSS가 예측 가능하고 유지보수 가능하며 반응형과 접근성을 해치지 않는지 검수하는 기준이다.

---

### [핵심]

CSS 검수 항목:

```md
- [ ] reset과 base style이 정의되어 있는가?
- [ ] box-sizing border-box가 적용되어 있는가?
- [ ] focus-visible style이 유지되는가?
- [ ] token/CSS Variables를 사용하는가?
- [ ] selector specificity가 과도하지 않은가?
- [ ] ID selector styling을 피했는가?
- [ ] class naming이 의미 기반인가?
- [ ] component style과 page style 책임이 분리되어 있는가?
- [ ] padding/margin/gap 역할이 구분되어 있는가?
- [ ] fixed width 남용이 없는가?
- [ ] image max-width가 적용되어 있는가?
- [ ] typography line-height와 contrast가 적절한가?
- [ ] media query 조건이 명확한가?
- [ ] hover-only interaction이 없는가?
- [ ] reduced motion을 고려했는가?
```

---

### [실무]

검수 Flow:

```text
Reset/Base
→ Token
→ Selector
→ Layout
→ Responsive
→ Typography/Color/Spacing
→ Interaction State
→ Accessibility CSS
→ Part05 / Part10 / Part12 / Part13 기준 연결
```

검수 기준:

- CSS가 DOM 구조에 과도하게 의존하지 않는가?
- Component가 독립적으로 재사용 가능한가?
- cascade 충돌이 예상되는 selector가 없는가?
- responsive viewport에서 직접 확인했는가?

---

### [FAQ]

Q. CSS Review에서 가장 먼저 볼 것은?
A. reset/base, token 사용, selector specificity, layout, responsive, focus-visible을 먼저 본다.

Q. CSS에서 ID selector를 피하는 이유는?
A. specificity가 높아 override와 유지보수가 어려워지기 때문이다.

Q. fixed width는 왜 조심해야 해?
A. 작은 viewport에서 horizontal overflow를 만들 수 있기 때문이다.

---

## 15.3 Accessibility Review Checklist

### [개념]

Accessibility Review Checklist는 keyboard, screen reader, touch 환경에서 UI가 사용 가능한지 확인하는 기준이다.

---

### [핵심]

Accessibility 검수 항목:

```md
- [ ] interactive element가 semantic button/link/input인가?
- [ ] keyboard Tab 이동이 가능한가?
- [ ] focus-visible이 보이는가?
- [ ] focus order가 DOM 순서와 자연스러운가?
- [ ] icon-only button에 accessible name이 있는가?
- [ ] form label이 input과 연결되어 있는가?
- [ ] error message가 input에 연결되어 있는가?
- [ ] aria-invalid가 실제 오류 상태와 일치하는가?
- [ ] aria-expanded가 실제 열림 상태와 일치하는가?
- [ ] aria-selected와 visible panel이 일치하는가?
- [ ] aria-current가 현재 페이지 link에 적용되는가?
- [ ] hidden content 내부로 focus가 이동하지 않는가?
- [ ] modal focus trap이 있는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] contrast가 충분한가?
- [ ] touch target이 충분한가?
```

---

### [실무]

검수 Flow:

```text
Keyboard Only Test
→ Focus Visible Test
→ Accessible Name Test
→ Form Label Test
→ ARIA State Test
→ Hidden Focus Test
→ Contrast Test
→ Touch Target Test
→ Part15 기준 연결
```

검수 기준:

- 마우스 없이 주요 기능을 사용할 수 있는가?
- screen reader에 전달될 이름과 상태가 실제 UI와 일치하는가?
- 보이지 않는 요소가 focus되지 않는가?
- 색상 외 정보 전달 수단이 있는가?

---

### [FAQ]

Q. Accessibility Review에서 가장 먼저 볼 것은?
A. keyboard 조작, focus-visible, accessible name, form label, ARIA state를 먼저 본다.

Q. hidden content에 focus가 가면 왜 문제야?
A. 화면에는 보이지 않는데 keyboard 사용자가 해당 요소에 도달해 혼란을 느끼기 때문이다.

Q. 색상만으로 상태를 표시하면 왜 안 돼?
A. 색상 구분이 어려운 사용자에게 상태 정보가 전달되지 않을 수 있기 때문이다.

---

## 15.4 Responsive Review Checklist

### [개념]

Responsive Review Checklist는 다양한 viewport에서 Layout과 Component가 깨지지 않는지 확인하는 기준이다.

---

### [핵심]

Responsive 검수 항목:

```md
- [ ] viewport meta가 있는가?
- [ ] 모바일 기본 layout이 정상인가?
- [ ] body horizontal overflow가 없는가?
- [ ] fixed width가 viewport를 넘지 않는가?
- [ ] images가 부모를 넘지 않는가?
- [ ] table overflow-x 처리가 필요한가?
- [ ] flex item이 wrap 또는 column 전환되는가?
- [ ] grid minmax 최소값이 적절한가?
- [ ] button group이 작은 화면에서 깨지지 않는가?
- [ ] modal/dialog가 viewport 안에 들어오는가?
- [ ] dropdown/tooltip이 화면 밖으로 나가지 않는가?
- [ ] typography가 모바일에서 읽기 쉬운가?
- [ ] touch target이 충분한가?
- [ ] fixed bottom UI가 콘텐츠를 가리지 않는가?
```

---

### [실무]

검수 Flow:

```text
320px
→ 375px
→ 768px
→ 1024px
→ 1280px
→ Horizontal Scroll Check
→ Component Overflow Check
→ Touch Target Check
→ Part10 기준 연결
```

검수 기준:

- 가장 작은 viewport에서 핵심 기능이 사용 가능한가?
- desktop에서 content width가 너무 넓지 않은가?
- media query 경계값에서 layout이 갑자기 깨지지 않는가?
- component가 page layout에 따라 유연하게 줄어드는가?

---

### [FAQ]

Q. Responsive Review에서 가장 먼저 볼 것은?
A. mobile viewport, horizontal overflow, fixed width, image/table overflow를 먼저 본다.

Q. 최소 viewport는 어느 정도를 확인해?
A. 프로젝트 기준에 따라 다르지만 320px 또는 360px 근처 작은 viewport를 확인하는 것이 좋다.

Q. media query 경계값도 확인해야 해?
A. 해야 한다. breakpoint 직전과 직후에서 layout이 깨질 수 있다.

---

## 15.5 Component Review Checklist

### [개념]

Component Review Checklist는 Component가 semantic, state, responsive, accessibility, styling architecture 기준을 만족하는지 확인하는 기준이다.

---

### [핵심]

Component 검수 항목:

```md
- [ ] Component 역할이 명확한가?
- [ ] semantic element를 사용했는가?
- [ ] root class와 element class가 명확한가?
- [ ] token/CSS Variables를 사용하는가?
- [ ] variant와 state를 구분했는가?
- [ ] hover, focus-visible, active, disabled 상태가 있는가?
- [ ] aria-expanded/selected/current/invalid가 실제 상태와 일치하는가?
- [ ] hidden content 내부로 focus가 이동하지 않는가?
- [ ] button/link 역할이 올바른가?
- [ ] form field label/error 연결이 올바른가?
- [ ] modal/dropdown/tabs/accordion keyboard interaction이 가능한가?
- [ ] responsive viewport에서 overflow가 없는가?
- [ ] page style에 과도하게 의존하지 않는가?
```

---

### [실무]

검수 Flow:

```text
Role
→ Semantic Element
→ Class Naming
→ Token
→ Variant
→ State
→ Accessibility
→ Responsive
→ Reusability
→ Part14 기준 연결
```

검수 기준:

- Component가 독립적으로 재사용 가능한가?
- state가 CSS와 ARIA 양쪽에서 동기화되는가?
- variant가 token 또는 scoped variable로 관리되는가?
- page-specific override 없이도 기본 품질이 유지되는가?

---

### [FAQ]

Q. Component Review에서 가장 먼저 볼 것은?
A. 역할, semantic element, button/link 구분, accessible name, focus-visible을 먼저 본다.

Q. Variant와 State를 왜 구분해야 해?
A. variant는 종류이고 state는 현재 상태라서 관리 기준이 다르기 때문이다.

Q. Component가 page style에 의존하면 왜 문제야?
A. 다른 page에서 재사용할 때 깨지거나 예상과 다르게 보일 수 있기 때문이다.

---

# 16. Common Mistakes

## 16.1 Troubleshooting Review Common Mistakes

### [개념]

Troubleshooting과 Review 과정의 실수는 문제 원인을 잘못 판단하거나, 임시 수정으로 더 큰 cascade 충돌과 접근성 문제를 만드는 원인이 된다.

---

### [핵심]

자주 발생하는 실수:

- DevTools 확인 없이 추측으로 수정
- CSS import 누락을 specificity 문제로 착각
- className 오타를 layout 문제로 착각
- z-index 문제와 overflow clipping 문제 혼동
- media query 조건을 반대로 이해
- fixed width 문제를 body overflow hidden으로 숨김
- `!important`로 모든 문제를 해결하려 함
- focus outline을 제거해 시각만 맞춤
- 색상만 바꿔 error 상태를 표현
- ARIA 상태와 실제 UI 상태 불일치 방치
- hidden content focus 문제를 확인하지 않음
- 모바일 viewport 검수 누락
- keyboard only test 누락
- Component variant와 state 혼동
- reset/base import 순서 확인 누락
- 관련 Part를 보지 않고 Part16 checklist만 기계적으로 수행

---

### [실무]

잘못된 해결 예:

```css
body {
  overflow-x: hidden;
}
```

위 코드는 horizontal overflow 원인을 숨길 수 있지만 실제 넓은 요소 문제를 해결하지 않는다.

권장 해결 Flow:

```text
증상 재현
→ DevTools로 원인 요소 확인
→ 실제 원인 property 확인
→ 관련 Part 기준 확인
→ 최소 CSS 수정
→ responsive/accessibility 재검수
```

검수 기준:

- 문제를 재현했는가?
- DevTools에서 원인 rule을 확인했는가?
- 임시 hack이 아니라 원인을 수정했는가?
- 수정 후 keyboard/responsive/accessibility를 다시 확인했는가?
- 세부 기준은 관련 Part와 연결했는가?

---

### [FAQ]

Q. Troubleshooting에서 가장 흔한 실수는?
A. DevTools로 원인을 확인하지 않고 추측으로 CSS를 덮어쓰는 것이다.

Q. body overflow-x hidden으로 가로 스크롤을 없애도 돼?
A. 임시로 숨길 수는 있지만 원인 요소를 찾아 해결하는 것이 우선이다.

Q. z-index를 계속 키우면 해결돼?
A. 아니다. stacking context나 overflow clipping 문제라면 숫자를 키워도 해결되지 않는다.

Q. Review에서 반드시 해야 할 테스트는?
A. viewport resize, keyboard only, focus-visible, contrast, hidden/focus 상태 검수를 해야 한다.

---

# 17. Best Practice

## 17.1 Troubleshooting Review Best Practice

### [개념]

Troubleshooting Review Best Practice는 HTML/CSS 문제를 증상 기준으로 분류하고, DevTools와 Checklist를 이용해 원인을 정확히 찾고, 최소 수정 후 재검수하는 기준이다.

---

### [핵심]

권장 기준:

- 문제를 먼저 재현한다.
- 증상을 CSS 적용 문제, Layout 문제, Responsive 문제, Accessibility 문제로 분류한다.
- DevTools Elements, Styles, Computed, Layout, Accessibility 정보를 확인한다.
- HTML 구조와 CSS 적용 여부를 분리해서 본다.
- className과 selector를 직접 비교한다.
- box model을 시각적으로 확인한다.
- flex/grid overlay를 사용해 layout context를 확인한다.
- z-index 문제는 stacking context와 overflow를 함께 본다.
- responsive 문제는 작은 viewport에서 시작한다.
- 접근성 문제는 keyboard only test로 확인한다.
- ARIA 상태는 실제 UI 상태와 동기화한다.
- `!important`와 body overflow hidden으로 원인을 숨기지 않는다.
- 수정은 최소 단위로 적용한다.
- 세부 기술 기준은 관련 Part를 참조한다.
- 수정 후 HTML/CSS/Accessibility/Responsive Checklist를 다시 수행한다.

---

### [실무]

Full Review Flow:

```text
1. Reproduce
2. Classify Symptom
3. Inspect DOM
4. Inspect CSS Rule
5. Inspect Computed Style
6. Inspect Box Model
7. Inspect Layout Context
8. Inspect Responsive Viewport
9. Inspect Accessibility Tree
10. Check Related Part
11. Apply Minimal Fix
12. Re-test
13. Document Cause
```

Final Review Checklist:

```md
- [ ] HTML 구조가 semantic한가?
- [ ] metadata와 SEO 기본값이 있는가?
- [ ] CSS 파일 import와 순서가 올바른가?
- [ ] className과 selector가 일치하는가?
- [ ] reset/base style이 적용되는가?
- [ ] box-sizing과 media reset이 있는가?
- [ ] selector specificity가 과도하지 않은가?
- [ ] layout display가 목적에 맞는가?
- [ ] flex/grid item 관계가 올바른가?
- [ ] position/z-index/overflow 문제가 없는가?
- [ ] responsive viewport에서 horizontal overflow가 없는가?
- [ ] typography, color, spacing이 읽기 쉬운가?
- [ ] interactive element focus-visible이 보이는가?
- [ ] form label/error 연결이 올바른가?
- [ ] ARIA state가 실제 UI 상태와 일치하는가?
- [ ] hidden content 내부에 focus가 가지 않는가?
- [ ] Component variant/state가 구분되는가?
- [ ] keyboard only test를 통과하는가?
```

---

### [FAQ]

Q. Troubleshooting Review Best Practice는 뭐야?
A. 문제를 재현하고 증상을 분류한 뒤 DevTools와 Checklist로 원인을 확인하고 최소 수정 후 재검수하는 것이다.

Q. HTML/CSS 문제를 해결할 때 가장 중요한 원칙은?
A. 추측이 아니라 실제 DOM, CSS rule, computed style, accessibility state를 확인하는 것이다.

Q. 수정 후 무엇을 다시 확인해야 해?
A. responsive viewport, keyboard focus, ARIA state, hidden/focus 상태, cascade 충돌을 다시 확인해야 한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent와 Review Agent가 HTML/CSS 문제를 체계적으로 진단하고 실무 기준 Checklist로 품질을 검수하게 만드는 것이다.

---

# 18. Linkage Reference

## 18.1 Related Documents

### [개념]

Linkage Reference는 Part16을 HTML/CSS Foundation 전체의 Troubleshooting Hub로 사용하기 위한 참조 기준이다.

Part16은 검수와 문제 진단의 출발점이며, 세부 해결 기준은 관련 Part 문서를 함께 참조한다.

---

### [핵심]

파일별 참조 기준:

- Part01 Document Structure: doctype, html, head, meta, body, root 구조 문제
- Part02 Semantic HTML: header, nav, main, section, article, aside, footer, heading 구조 문제
- Part03 Form Elements: form, label, input, textarea, select, checkbox, radio, fieldset 문제
- Part04 Text Link Image List Table: text, anchor, img alt, figure, list, table 문제
- Part05 CSS Syntax Selector Cascade: CSS 문법, selector, specificity, cascade 문제
- Part06 Box Model Display: box model, padding, margin, border, display 문제
- Part07 Flexbox: flex container, flex item, axis, wrap, align 문제
- Part08 Grid: grid track, minmax, auto-fit, item placement 문제
- Part09 Position ZIndex: position, z-index, stacking context, overflow clipping 문제
- Part10 Responsive Media Query: viewport, breakpoint, media query, responsive overflow 문제
- Part11 Typography Color Spacing: font, line-height, color, contrast, spacing 문제
- Part12 CSS Variables Pseudo Transition: token, pseudo selector, transition, reduced motion 문제
- Part13 Reset Normalize Styling Architecture: reset, base, file structure, scope 문제
- Part14 Component Styling Practical Patterns: button, card, modal, dropdown, tabs, accordion 문제
- Part15 HTML Attributes Accessibility SEO: attributes, ARIA, accessibility, SEO 문제
- Part16 Troubleshooting Review Checklist: 최종 문제 분류, 검수, 재검토 기준

---

### [실무]

상황별 빠른 연결:

```text
CSS가 안 먹음 → Part05 + Part16
레이아웃이 넘침 → Part06 / Part07 / Part08 / Part10 + Part16
모달/드롭다운이 잘림 → Part09 / Part14 + Part16
모바일에서 깨짐 → Part10 + Part16
버튼/탭/아코디언 상태가 이상함 → Part12 / Part14 / Part15 + Part16
form error가 screen reader에 전달 안 됨 → Part03 / Part15 + Part16
focus가 안 보임 → Part12 / Part13 / Part15 + Part16
reset 때문에 스타일이 깨짐 → Part13 + Part16
SEO title/meta/heading 문제 → Part01 / Part02 / Part15 + Part16
```

---

### [FAQ]

Q. Part16은 어떤 문서들과 연결돼?
A. Part01~Part15 전체와 연결되며 문제 유형별로 관련 세부 문서를 참조한다.

Q. CSS가 안 먹으면 어디를 봐?
A. Part05에서 selector/cascade를 확인하고 Part16의 CSS Not Applied Flow로 진단한다.

Q. Responsive 문제가 생기면 어디를 봐?
A. Part10 기준을 확인하고 Part16 Responsive Troubleshooting Flow로 진단한다.

Q. Component 문제가 생기면 어디를 봐?
A. Part14 Component Pattern, Part15 ARIA 기준, Part16 Review Checklist를 함께 참조한다.

---

# Retrieval Queries

### [FAQ]

Q. Part16은 어떤 문서야?
A. HTML/CSS Foundation 전체의 최종 Troubleshooting과 Review 기준 문서다.

Q. Part16은 새 개념 문서야?
A. 아니다. Part01~Part15의 기준을 문제 진단과 검수 흐름으로 연결하는 문서다.

Q. 문제가 생기면 Part16만 보면 돼?
A. Part16으로 원인을 분류하고, 세부 기준은 관련 Part를 함께 참조해야 한다.

Q. HTML CSS Troubleshooting이 뭐야?
A. 화면, Layout, 스타일, 접근성 문제가 왜 발생했는지 HTML 구조와 CSS 적용 흐름을 기준으로 분석하는 과정이다.

Q. CSS 문제가 생기면 가장 먼저 뭘 봐?
A. DevTools에서 DOM 구조, selector 매칭, computed style, box model을 먼저 확인한다.

Q. Layout 문제는 어디서 시작해?
A. display 값, parent-child 관계, box model, width/min-width, overflow를 확인한다.

Q. 접근성 문제는 어디서 시작해?
A. semantic element, keyboard focus, accessible name, ARIA state, hidden/focus 상태를 확인한다.

Q. CSS가 안 먹을 때 가장 먼저 확인할 것은?
A. CSS 파일 import 여부와 className / selector 이름 일치 여부를 확인한다.

Q. DevTools에서 CSS가 취소선이면 무슨 뜻이야?
A. 해당 rule이 다른 CSS rule에 의해 override되었거나 적용 우선순위에서 밀렸다는 뜻이다.

Q. className 오타는 어떻게 찾나?
A. Elements 패널의 실제 DOM class와 CSS selector를 직접 비교한다.

Q. Cascade Debugging이 뭐야?
A. 여러 CSS rule 중 어떤 rule이 최종 적용되는지 cascade, specificity, source order 기준으로 확인하는 과정이다.

Q. specificity가 뭐야?
A. selector의 우선순위를 계산하는 기준이다.

Q. !important를 쓰면 해결돼?
A. 임시로는 가능하지만 유지보수와 디버깅을 어렵게 하므로 남용하면 안 된다.

Q. Box Model 문제가 생기면 무엇을 확인해?
A. width, padding, border, margin, box-sizing, min-width, overflow를 확인한다.

Q. width 100%인데 요소가 넘치는 이유는?
A. content-box에서 padding과 border가 width에 추가되기 때문일 수 있다.

Q. margin collapse는 뭐야?
A. 인접한 block 요소의 세로 margin이 합쳐지는 CSS 동작이다.

Q. Display Bug에서 가장 먼저 볼 것은?
A. 해당 요소와 부모 요소의 display 값을 확인한다.

Q. inline 요소에 width가 안 먹는 이유는?
A. inline 요소는 일반적으로 width/height가 적용되지 않기 때문이다.

Q. display none과 visibility hidden 차이는?
A. display none은 layout에서 제거되고 visibility hidden은 공간을 유지한 채 보이지 않는다.

Q. Flexbox 문제가 생기면 무엇부터 확인해?
A. container, direct child, flex-direction, axis, justify-content, align-items를 확인한다.

Q. justify-content와 align-items 차이는?
A. justify-content는 main axis 정렬이고 align-items는 cross axis 정렬이다.

Q. flex item이 넘치는 이유는?
A. min-width, fixed width, flex-basis, 긴 텍스트 때문에 줄어들지 못할 수 있다.

Q. Grid 문제가 생기면 무엇부터 확인해?
A. grid container, direct child item, grid-template-columns, gap, minmax, item span을 확인한다.

Q. 모바일에서 Grid가 넘치는 이유는?
A. 고정 column, 큰 minmax 최소값, 큰 gap, span item, 긴 텍스트 때문일 수 있다.

Q. absolute 요소가 엉뚱한 곳에 가는 이유는?
A. 기준이 되는 positioned ancestor가 없기 때문일 수 있다.

Q. z-index를 크게 줬는데 안 보이는 이유는?
A. stacking context가 다르거나 overflow clipping 때문에 가려질 수 있다.

Q. sticky가 안 되는 이유는?
A. top offset 누락, 부모 overflow, 부모 높이, scroll container 문제 때문일 수 있다.

Q. Responsive Bug에서 가장 흔한 원인은?
A. fixed width, image max-width 누락, table overflow, flex/grid wrap 누락, media query 조건 오해다.

Q. 모바일 가로 스크롤은 어떻게 찾나?
A. DevTools에서 mobile viewport로 줄이고 viewport보다 넓은 요소를 찾는다.

Q. Media Query가 안 먹으면?
A. viewport meta, min-width/max-width 조건, CSS 순서, selector 매칭을 확인한다.

Q. 텍스트가 읽기 어려우면 무엇을 확인해?
A. font-size, line-height, contrast, line length, spacing을 확인한다.

Q. 색상 문제는 무엇을 봐?
A. 텍스트와 배경 contrast, 상태 색상이 색상만으로 전달되는지 확인한다.

Q. 여백 문제는 무엇을 봐?
A. padding, margin, gap 역할과 spacing scale 사용 여부를 확인한다.

Q. Form 접근성 문제에서 가장 흔한 것은?
A. label 누락, placeholder label 대체, error message 연결 누락, aria-invalid 불일치다.

Q. placeholder를 label 대신 쓰면 왜 안 돼?
A. 입력 중 사라지고 필드 이름으로 안정적으로 전달되지 않기 때문이다.

Q. error message는 어떻게 연결해?
A. input의 aria-describedby가 error message id를 참조하게 한다.

Q. Component Bug는 무엇부터 확인해?
A. semantic element, className, CSS import, variant/state, focus, ARIA 상태를 확인한다.

Q. button과 link를 혼동하면 왜 문제야?
A. 의미, keyboard 동작, form 동작, screen reader 정보가 달라지기 때문이다.

Q. Dropdown 닫힘 상태에서 focus가 들어가면?
A. hidden 처리나 focus management가 잘못된 것이므로 닫힌 content를 focus 불가능하게 해야 한다.

Q. Reset Base 문제는 무엇부터 확인해?
A. reset 파일 로드, import order, body margin, box-sizing, focus-visible을 확인한다.

Q. focus outline을 없애면 왜 문제야?
A. keyboard 사용자가 현재 조작 위치를 알 수 없기 때문이다.

Q. HTML Review에서 가장 먼저 볼 것은?
A. document metadata, landmark, heading hierarchy, button/link 역할, image alt, form label을 먼저 본다.

Q. CSS Review에서 가장 먼저 볼 것은?
A. reset/base, token 사용, selector specificity, layout, responsive, focus-visible을 먼저 본다.

Q. Accessibility Review에서 가장 먼저 볼 것은?
A. keyboard 조작, focus-visible, accessible name, form label, ARIA state를 먼저 본다.

Q. Responsive Review에서 가장 먼저 볼 것은?
A. mobile viewport, horizontal overflow, fixed width, image/table overflow를 먼저 본다.

Q. Component Review에서 가장 먼저 볼 것은?
A. 역할, semantic element, button/link 구분, accessible name, focus-visible을 먼저 본다.

Q. Troubleshooting에서 가장 흔한 실수는?
A. DevTools로 원인을 확인하지 않고 추측으로 CSS를 덮어쓰는 것이다.

Q. body overflow-x hidden으로 가로 스크롤을 없애도 돼?
A. 임시로 숨길 수는 있지만 원인 요소를 찾아 해결하는 것이 우선이다.

Q. z-index를 계속 키우면 해결돼?
A. 아니다. stacking context나 overflow clipping 문제라면 숫자를 키워도 해결되지 않는다.

Q. Troubleshooting Review Best Practice는 뭐야?
A. 문제를 재현하고 증상을 분류한 뒤 DevTools와 Checklist로 원인을 확인하고 최소 수정 후 재검수하는 것이다.

Q. HTML/CSS 문제를 해결할 때 가장 중요한 원칙은?
A. 추측이 아니라 실제 DOM, CSS rule, computed style, accessibility state를 확인하는 것이다.

Q. 수정 후 무엇을 다시 확인해야 해?
A. responsive viewport, keyboard focus, ARIA state, hidden/focus 상태, cascade 충돌을 다시 확인해야 한다.

Q. Part16은 어떤 문서들과 연결돼?
A. Part01~Part15 전체와 연결되며 문제 유형별로 관련 세부 문서를 참조한다.

Q. CSS가 안 먹으면 어디를 봐?
A. Part05에서 selector/cascade를 확인하고 Part16의 CSS Not Applied Flow로 진단한다.

Q. Responsive 문제가 생기면 어디를 봐?
A. Part10 기준을 확인하고 Part16 Responsive Troubleshooting Flow로 진단한다.

Q. Component 문제가 생기면 어디를 봐?
A. Part14 Component Pattern, Part15 ARIA 기준, Part16 Review Checklist를 함께 참조한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent와 Review Agent가 HTML/CSS 문제를 체계적으로 진단하고 실무 기준 Checklist로 품질을 검수하게 만드는 것이다.
