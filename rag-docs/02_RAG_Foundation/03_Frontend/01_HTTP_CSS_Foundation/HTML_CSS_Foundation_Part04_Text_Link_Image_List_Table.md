# HTML CSS Foundation Part04 - Text Link Image List Table

---

# 1. Text Elements

## 1.1 Text Element Concept

### [개념]

HTML Text Element는 문서의 텍스트 콘텐츠를 의미와 구조에 맞게 표현하는 요소다.

Text Element는 단순 글자 출력이 아니라 문서 계층, 강조, 설명, 문단, 코드, 인용, 보조 정보를 구분한다.

대표 요소:

- `p`
- `strong`
- `em`
- `small`
- `mark`
- `br`
- `hr`
- `code`
- `pre`
- `blockquote`

---

### [핵심]

Text Element 핵심:

- `p`는 문단을 표현한다.
- `strong`은 중요한 강조를 표현한다.
- `em`은 문맥상 강조를 표현한다.
- `small`은 부가 설명이나 작은 텍스트에 사용한다.
- `mark`는 하이라이트된 텍스트에 사용한다.
- `code`는 짧은 코드 조각에 사용한다.
- `pre`는 공백과 줄바꿈을 유지하는 블록에 사용한다.
- `blockquote`는 긴 인용문에 사용한다.
- 텍스트 스타일링만을 위해 의미 요소를 남용하지 않는다.

---

### [실무]

2026 실무 기준에서 Text Element는 Accessibility, SEO, Content Structure, React Component Markup과 연결된다.

Frontend Agent는 텍스트를 작성할 때 아래 기준을 적용해야 한다.

- 문단은 `p` 사용
- 제목은 heading 사용
- 중요한 의미 강조는 `strong` 사용
- 단순 시각 강조는 CSS class 사용
- 코드 조각은 `code` 사용
- 긴 코드 블록은 `pre` + `code` 사용
- 인용문은 `blockquote` 사용
- 줄 간격 목적의 `br` 남용 금지
- 수평 구분선은 의미 있는 구분일 때 `hr` 사용

예:

```html
<section>
  <h2>Festival Notice</h2>
  <p>
    <strong>Important:</strong>
    The event schedule may change depending on weather conditions.
  </p>
</section>
```

---

### [FAQ]

Q. HTML Text Element가 뭐야?
A. 텍스트 콘텐츠를 의미와 구조에 맞게 표현하는 HTML 요소다.

Q. 글자를 굵게 하려면 strong을 써?
A. 중요한 의미 강조라면 `strong`을 쓰고 단순 시각 스타일은 CSS를 사용한다.

Q. 줄바꿈하려고 br을 많이 써도 돼?
A. 권장하지 않는다. 레이아웃 간격은 CSS로 처리하는 것이 좋다.

Q. 문단은 어떤 태그를 써?
A. 일반 문단은 `p` 태그를 사용한다.

---

## 1.2 Paragraph

### [개념]

`p`는 문단을 나타내는 HTML Text Element다.

본문 설명, 안내 문구, 카드 설명, 에러 설명, 도움말 텍스트에 사용한다.

---

### [핵심]

`p` 핵심:

- 일반 문단에 사용한다.
- 제목에는 사용하지 않는다.
- 목록에는 `ul`, `ol`, `li`를 사용한다.
- 버튼이나 링크 역할로 사용하지 않는다.
- 문단 내부에 block element를 넣지 않는다.
- 문단 간 간격은 CSS margin으로 조절한다.

예:

```html
<p>Search festivals by region, date, and category.</p>
```

---

### [실무]

실무에서 `p`는 Card, Detail Page, Form Help Text, Error Message에 자주 사용된다.

예:

```html
<article class="festival-card">
  <h2>Seoul Light Festival</h2>
  <p>Enjoy night lights and performances in Seoul.</p>
  <a href="/festivals/1">View Detail</a>
</article>
```

검수 기준:

- 일반 설명 텍스트가 `p`로 작성되었는가?
- 제목 역할을 `p`로 작성하지 않았는가?
- 문단 간격을 `br`로 만들지 않았는가?
- 단순 클릭 요소를 `p`로 구현하지 않았는가?

---

### [FAQ]

Q. p 태그는 언제 써?
A. 일반 문단, 설명, 안내 문구, 카드 설명에 사용한다.

Q. 제목도 p로 써도 돼?
A. 권장하지 않는다. 제목은 heading 태그를 사용한다.

Q. p 사이 간격은 어떻게 조절해?
A. CSS margin 또는 layout spacing으로 조절한다.

---

## 1.3 Strong and Em

### [개념]

`strong`은 중요한 내용 강조를 나타내고, `em`은 문맥상 강조를 나타낸다.

두 요소는 단순히 굵게 또는 기울임을 만들기 위한 시각 스타일링 도구가 아니다.

---

### [핵심]

`strong` 핵심:

- 중요한 의미를 가진 강조에 사용한다.
- 기본적으로 굵게 표시되는 경우가 많다.
- 경고, 중요 안내, 핵심 문구에 적합하다.

`em` 핵심:

- 문맥상 강조에 사용한다.
- 기본적으로 기울임으로 표시되는 경우가 많다.
- 문장 안에서 특정 단어를 강조할 때 사용한다.

예:

```html
<p><strong>Required:</strong> Email address is required.</p>
<p>Please check the event date <em>before visiting</em>.</p>
```

---

### [실무]

실무에서는 의미 강조와 디자인 강조를 구분해야 한다.

좋은 예:

```html
<p><strong>Warning:</strong> Payment cannot be canceled after confirmation.</p>
```

나쁜 예:

```html
<strong class="large-title">Festival List</strong>
```

검수 기준:

- 의미상 중요한 내용에 `strong`을 사용했는가?
- 단순 굵은 글씨 스타일에 `strong`을 남용하지 않았는가?
- 제목은 heading으로 작성했는가?
- 디자인 강조는 CSS class로 처리했는가?

---

### [FAQ]

Q. strong은 언제 써?
A. 중요한 의미를 가진 내용이나 경고, 핵심 안내에 사용한다.

Q. em은 언제 써?
A. 문장 안에서 문맥상 강조가 필요한 단어나 표현에 사용한다.

Q. 글자를 굵게 만들려고 strong을 써도 돼?
A. 단순 시각 효과 목적이라면 CSS를 사용하는 것이 좋다.

---

## 1.4 Code and Pre

### [개념]

`code`는 짧은 코드 조각을 표현하는 inline element다.

`pre`는 공백과 줄바꿈을 유지하는 block element다.

긴 코드 블록은 일반적으로 `pre` 내부에 `code`를 넣어 표현한다.

---

### [핵심]

`code` 핵심:

- 짧은 코드, 명령어, 파일명, 속성명에 사용한다.
- inline code 표현에 적합하다.

`pre` 핵심:

- 줄바꿈과 공백을 유지한다.
- 긴 코드 블록이나 터미널 출력에 적합하다.

예:

```html
<p>Use <code>display: flex</code> for one-dimensional layout.</p>

<pre><code>.container {
  display: flex;
  gap: 16px;
}</code></pre>
```

---

### [실무]

개발 문서, 에러 메시지, 코드 예제 UI에서 `code`와 `pre`를 사용한다.

검수 기준:

- inline code는 `code`로 작성했는가?
- multi-line code는 `pre` + `code`로 작성했는가?
- 코드 블록을 단순 `div`로 작성하지 않았는가?
- 코드 줄바꿈이 유지되는가?
- 긴 코드 블록은 가로 스크롤 또는 wrapping 처리를 고려했는가?

---

### [FAQ]

Q. code 태그는 언제 써?
A. 짧은 코드 조각, 속성명, 명령어, 파일명을 표현할 때 사용한다.

Q. pre 태그는 언제 써?
A. 줄바꿈과 공백을 유지해야 하는 긴 코드 블록이나 출력 결과에 사용한다.

Q. 긴 코드 블록은 어떻게 작성해?
A. 보통 `<pre><code>...</code></pre>` 구조를 사용한다.

---

# 2. Link Elements

## 2.1 Anchor Link

### [개념]

`a` 태그는 다른 URL, 페이지, 파일, 문서 위치로 이동하는 링크 요소다.

Navigation, 상세 페이지 이동, 외부 링크, 다운로드 링크, 페이지 내부 이동에 사용한다.

---

### [핵심]

Anchor Link 핵심:

- `href`는 링크 목적지를 지정한다.
- 페이지 이동은 `a` 또는 Router Link를 사용한다.
- 동작 실행은 `button`을 사용한다.
- 링크 텍스트는 목적지를 설명해야 한다.
- `target="_blank"`는 새 탭 또는 새 창 이동에 사용한다.
- 새 창 링크에는 `rel="noopener noreferrer"`를 함께 사용한다.
- `href="#"` 남용 금지
- `href` 없는 `a` 태그 금지

예:

```html
<a href="/festivals/1">View Festival Detail</a>

<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  External Festival Site
</a>
```

---

### [실무]

React Router에서는 SPA Navigation을 위해 `Link`를 사용한다.

예:

```jsx
import { Link } from "react-router-dom";

function FestivalCard({ festival }) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <Link to={`/festivals/${festival.id}`}>View Festival Detail</Link>
    </article>
  );
}
```

검수 기준:

- 페이지 이동이 `a` 또는 Router Link로 작성되었는가?
- `button`으로 페이지 이동을 처리하지 않았는가?
- 링크 텍스트가 목적지를 설명하는가?
- `Click here`, `More`처럼 불명확한 텍스트를 남용하지 않았는가?
- 새 창 링크에 `rel="noopener noreferrer"`가 있는가?
- `href="#"`로 임시 링크를 방치하지 않았는가?

---

### [FAQ]

Q. a 태그는 언제 써?
A. URL 이동, 페이지 이동, 파일 다운로드, 문서 위치 이동에 사용한다.

Q. button과 a 태그 차이는 뭐야?
A. button은 동작 실행, a는 페이지 또는 URL 이동에 사용한다.

Q. href 없는 a 태그를 써도 돼?
A. 권장하지 않는다. 링크 의미와 접근성이 깨질 수 있다.

Q. 새 창 링크에는 무엇을 같이 써야 해?
A. `target="_blank"`를 사용할 때 `rel="noopener noreferrer"`를 함께 쓰는 것이 좋다.

---

## 2.2 Link Text

### [개념]

Link Text는 사용자가 링크를 클릭하기 전에 목적지를 이해하도록 제공되는 텍스트다.

좋은 Link Text는 접근성, SEO, 사용성에 직접 영향을 준다.

---

### [핵심]

Link Text 핵심:

- 링크 목적지를 설명해야 한다.
- 단독으로 읽어도 의미가 있어야 한다.
- `Click here`, `Read more`, `More` 남용 금지
- 동일한 텍스트가 서로 다른 목적지를 가리키지 않도록 주의
- 아이콘 링크에는 접근 가능한 이름을 제공해야 한다.
- 외부 링크는 새 창 여부를 안내할 수 있다.

좋은 예:

```html
<a href="/festivals/seoul-light">View Seoul Light Festival Detail</a>
```

나쁜 예:

```html
<a href="/festivals/seoul-light">Click here</a>
```

---

### [실무]

카드 UI에서는 카드 제목 또는 명확한 CTA 텍스트를 링크로 만든다.

예:

```html
<article class="festival-card">
  <h2>
    <a href="/festivals/1">Seoul Light Festival</a>
  </h2>
  <p>Night light festival in Seoul.</p>
</article>
```

아이콘 링크 예:

```html
<a href="/notifications" aria-label="Open notifications"> 🔔 </a>
```

검수 기준:

- 링크 텍스트만 보고 목적지를 알 수 있는가?
- 동일한 링크 텍스트가 서로 다른 URL에 반복되지 않았는가?
- 아이콘 링크에 accessible name이 있는가?
- 외부 링크 또는 다운로드 링크가 명확한가?

---

### [FAQ]

Q. 좋은 링크 텍스트는 뭐야?
A. 링크 목적지를 명확히 설명하고 단독으로 읽어도 의미가 있는 텍스트다.

Q. Click here는 왜 좋지 않아?
A. 링크 목적지를 설명하지 않아 접근성과 사용성이 떨어진다.

Q. 아이콘만 있는 링크는 어떻게 해야 해?
A. `aria-label` 또는 숨김 텍스트로 접근 가능한 이름을 제공해야 한다.

---

## 2.3 Internal Link and External Link

### [개념]

Internal Link는 같은 서비스 내부 페이지로 이동하는 링크다.

External Link는 다른 도메인 또는 외부 서비스로 이동하는 링크다.

---

### [핵심]

Internal Link 핵심:

- 같은 서비스 내부 Route 이동
- SPA에서는 Router Link 사용 가능
- 서비스 내 탐색과 SEO에 영향

External Link 핵심:

- 외부 도메인 이동
- 새 창 사용 시 `target="_blank"` 가능
- 보안상 `rel="noopener noreferrer"` 권장
- 사용자에게 외부 이동임을 알릴 수 있음

예:

```html
<a href="/calendar">Open Festival Calendar</a>

<a
  href="https://festival.example.com"
  target="_blank"
  rel="noopener noreferrer"
>
  Official Festival Website
</a>
```

---

### [실무]

실무에서는 내부 링크와 외부 링크 정책을 구분한다.

검수 기준:

- 내부 이동에 적절한 Router Link 또는 anchor를 사용했는가?
- 외부 링크에 보안 속성이 있는가?
- 외부 링크가 새 창으로 열리는 경우 사용자 경험이 적절한가?
- 외부 링크 텍스트가 목적지를 명확히 설명하는가?
- 다운로드 링크는 파일 형식 또는 동작을 안내하는가?

---

### [FAQ]

Q. Internal Link와 External Link 차이는 뭐야?
A. Internal Link는 서비스 내부 이동이고 External Link는 외부 도메인으로 이동하는 링크다.

Q. 외부 링크는 항상 새 창으로 열어야 해?
A. 필수는 아니다. 서비스 UX 정책에 따라 결정한다.

Q. target blank에는 왜 rel을 같이 써?
A. 새 창 보안 문제를 줄이기 위해 `rel="noopener noreferrer"`를 함께 사용한다.

---

# 3. Image Elements

## 3.1 Image Element

### [개념]

`img`는 웹 페이지에 이미지를 표시하는 HTML 요소다.

축제 이미지, 프로필 이미지, 썸네일, 아이콘, 지도 이미지, 장식 이미지에 사용한다.

기본 예:

```html
<img src="festival.jpg" alt="야간 축제 무대 전경" />
```

---

### [핵심]

Image Element 핵심:

- `src`는 이미지 경로다.
- `alt`는 이미지 대체 텍스트다.
- 의미 있는 이미지에는 설명 alt를 작성한다.
- 장식 이미지는 빈 alt를 사용할 수 있다.
- 파일명 그대로 alt 작성 금지
- `width`와 `height` 지정은 layout shift 감소에 도움된다.
- CSS에서 `max-width: 100%`와 `height: auto`를 자주 사용한다.
- 이미지 로딩 최적화에는 `loading="lazy"`를 고려한다.

---

### [실무]

Responsive Image 기본 CSS:

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

HTML 예:

```html
<img
  src="/images/seoul-light.jpg"
  alt="서울 야간 빛 축제의 조명 터널"
  width="640"
  height="360"
  loading="lazy"
/>
```

검수 기준:

- 의미 있는 이미지에 alt가 있는가?
- 장식 이미지의 alt가 비어 있는가?
- 파일명 그대로 alt를 작성하지 않았는가?
- 이미지가 반응형으로 줄어드는가?
- 큰 이미지에 lazy loading을 고려했는가?
- width / height로 layout shift를 줄였는가?

---

### [FAQ]

Q. img 태그는 언제 써?
A. 웹 페이지에 이미지를 표시할 때 사용한다.

Q. img src는 뭐야?
A. 표시할 이미지 파일의 경로다.

Q. img alt는 왜 필요해?
A. 이미지가 보이지 않거나 스크린 리더를 사용할 때 이미지 의미를 전달하기 위해 필요하다.

Q. 이미지 반응형은 어떻게 처리해?
A. 일반적으로 `max-width: 100%`와 `height: auto`를 사용한다.

---

## 3.2 Alt Text

### [개념]

Alt Text는 이미지의 대체 텍스트다.

이미지가 로드되지 않거나 스크린 리더 사용자가 페이지를 탐색할 때 이미지 의미를 전달한다.

---

### [핵심]

Alt Text 핵심:

- 의미 있는 이미지는 이미지 목적과 정보를 설명한다.
- 장식 이미지는 `alt=""`를 사용할 수 있다.
- “이미지”, “사진”이라는 단어 반복은 보통 불필요하다.
- 파일명, 랜덤 문자열, SEO 키워드 나열 금지
- 이미지 주변 문맥에 맞게 작성한다.
- 링크 이미지의 alt는 링크 목적지를 설명해야 한다.

좋은 예:

```html
<img src="map.png" alt="서울 강남구 축제 위치 지도" />
```

장식 이미지 예:

```html
<img src="decor-line.svg" alt="" />
```

---

### [실무]

Alt Text 작성 기준:

```text
Informative Image → 의미 설명
Decorative Image → alt=""
Functional Image Link → 기능 또는 목적지 설명
Complex Image → 주변 텍스트 또는 상세 설명 제공
```

나쁜 예:

```html
<img src="IMG_1234.jpg" alt="IMG_1234" />
<img src="festival.jpg" alt="축제 축제 축제 서울 축제" />
```

링크 이미지 예:

```html
<a href="/festivals/1">
  <img src="thumb.jpg" alt="View Seoul Light Festival Detail" />
</a>
```

검수 기준:

- alt가 이미지 의미를 설명하는가?
- 장식 이미지는 빈 alt인가?
- 파일명을 alt로 사용하지 않았는가?
- 링크 이미지 alt가 링크 목적을 설명하는가?
- alt가 너무 길거나 키워드 나열이 아닌가?

---

### [FAQ]

Q. 모든 이미지에 alt가 필요해?
A. 필요하다. 의미 있는 이미지는 설명을 넣고 장식 이미지는 빈 alt를 사용할 수 있다.

Q. alt에 “이미지”라고 써야 해?
A. 대부분 필요 없다. 스크린 리더가 이미 이미지임을 알려줄 수 있다.

Q. 장식 이미지는 alt를 어떻게 써?
A. `alt=""`처럼 빈 alt를 사용해 보조 기술이 무시하도록 할 수 있다.

Q. 링크 안의 이미지 alt는 어떻게 써?
A. 이미지 설명보다 링크 목적지를 설명하는 것이 좋다.

---

## 3.3 Figure and Figcaption

### [개념]

`figure`는 이미지, 차트, 코드, 도표처럼 독립적인 콘텐츠를 묶는 요소다.

`figcaption`은 `figure` 콘텐츠의 설명 또는 캡션을 제공한다.

---

### [핵심]

Figure 핵심:

- 이미지와 캡션을 의미 있게 묶는다.
- 도표, 차트, 코드 예제에도 사용할 수 있다.
- 본문 흐름과 관련 있지만 독립적으로 이해 가능한 콘텐츠에 적합하다.
- `figcaption`은 설명, 출처, 제목을 제공할 수 있다.
- 모든 이미지에 figure가 필요한 것은 아니다.

예:

```html
<figure>
  <img src="festival-stage.jpg" alt="야간 축제 무대에서 공연 중인 밴드" />
  <figcaption>Seoul Light Festival main stage.</figcaption>
</figure>
```

---

### [실무]

상세 페이지, 기사형 콘텐츠, 갤러리, 결과 리포트에서 figure를 사용할 수 있다.

검수 기준:

- 이미지와 캡션이 함께 의미를 가지는가?
- 단순 아이콘이나 장식 이미지에 figure를 남용하지 않았는가?
- figcaption이 이미지 설명 또는 출처를 제공하는가?
- alt와 figcaption이 불필요하게 동일 문장을 반복하지 않는가?

---

### [FAQ]

Q. figure는 언제 써?
A. 이미지, 차트, 코드, 도표처럼 캡션과 함께 독립적으로 이해 가능한 콘텐츠에 사용한다.

Q. figcaption은 왜 써?
A. figure 콘텐츠의 설명, 제목, 출처를 제공하기 위해 사용한다.

Q. 모든 이미지에 figure를 써야 해?
A. 아니다. 캡션이나 독립 콘텐츠 의미가 있을 때 사용하면 된다.

---

# 4. List Elements

## 4.1 Unordered List

### [개념]

`ul`은 순서가 중요하지 않은 목록을 표현하는 HTML 요소다.

각 항목은 `li`로 작성한다.

예:

```html
<ul>
  <li>Music Festival</li>
  <li>Food Festival</li>
  <li>Culture Festival</li>
</ul>
```

---

### [핵심]

Unordered List 핵심:

- 순서가 중요하지 않은 항목 목록에 사용한다.
- 각 항목은 `li`로 작성한다.
- Navigation menu에도 사용할 수 있다.
- 카드 목록에도 사용할 수 있다.
- 단순 줄바꿈 목록을 `br`로 만들지 않는다.
- list marker는 CSS로 조절할 수 있다.

---

### [실무]

실무에서 `ul`은 메뉴, 필터, 카드 목록, 태그 목록, 알림 목록에 자주 사용된다.

예:

```html
<nav aria-label="Main Navigation">
  <ul>
    <li><a href="/festivals">Festivals</a></li>
    <li><a href="/calendar">Calendar</a></li>
    <li><a href="/mypage">My Page</a></li>
  </ul>
</nav>
```

카드 목록 예:

```html
<ul class="festival-list">
  <li>
    <article>
      <h2>Seoul Light Festival</h2>
    </article>
  </li>
  <li>
    <article>
      <h2>Busan Sea Festival</h2>
    </article>
  </li>
</ul>
```

검수 기준:

- 순서 없는 반복 항목이 `ul` / `li`로 작성되었는가?
- 메뉴 목록이 list structure로 작성되었는가?
- 단순 `div` 반복으로 목록 의미를 잃지 않았는가?
- list marker 제거는 CSS로 처리했는가?

---

### [FAQ]

Q. ul은 언제 써?
A. 순서가 중요하지 않은 항목 목록에 사용한다.

Q. li는 어디에 써?
A. ul 또는 ol 내부의 각 목록 항목에 사용한다.

Q. 메뉴도 ul로 만들어도 돼?
A. 가능하다. Navigation 메뉴는 목록 구조로 표현하기 좋다.

Q. 카드 목록도 ul을 써도 돼?
A. 가능하다. 여러 카드가 반복되는 목록이라면 ul/li 구조가 적절할 수 있다.

---

## 4.2 Ordered List

### [개념]

`ol`은 순서가 중요한 목록을 표현하는 HTML 요소다.

각 항목은 `li`로 작성한다.

예:

```html
<ol>
  <li>Select region.</li>
  <li>Choose date.</li>
  <li>Search festivals.</li>
</ol>
```

---

### [핵심]

Ordered List 핵심:

- 순서가 중요한 항목에 사용한다.
- 절차, 단계, 순위, 랭킹에 적합하다.
- 각 항목은 `li`로 작성한다.
- `start`, `reversed`, `type` 속성을 사용할 수 있다.
- 단순 숫자 텍스트를 직접 작성하는 것보다 의미가 명확하다.

---

### [실무]

실무에서 `ol`은 절차 안내, 사용 방법, 체크 단계, 랭킹 목록에 사용된다.

예:

```html
<section>
  <h2>How to Search Festivals</h2>
  <ol>
    <li>Enter keyword.</li>
    <li>Select region.</li>
    <li>Click search button.</li>
  </ol>
</section>
```

검수 기준:

- 순서가 중요한 목록에 ol을 사용했는가?
- 순서가 중요하지 않은 목록에 ol을 남용하지 않았는가?
- 숫자를 텍스트로 직접 반복하지 않았는가?
- 단계 설명이 명확한가?

---

### [FAQ]

Q. ol은 언제 써?
A. 순서가 중요한 절차, 단계, 순위, 랭킹 목록에 사용한다.

Q. ul과 ol 차이는 뭐야?
A. ul은 순서 없는 목록, ol은 순서가 중요한 목록에 사용한다.

Q. 숫자를 직접 써도 되는데 왜 ol을 써?
A. ol을 쓰면 목록의 순서 의미가 HTML 구조로 전달된다.

---

## 4.3 Description List

### [개념]

`dl`은 용어와 설명의 쌍을 표현하는 Description List다.

`dt`는 용어 또는 이름, `dd`는 해당 설명을 의미한다.

예:

```html
<dl>
  <dt>Location</dt>
  <dd>Seoul</dd>

  <dt>Date</dt>
  <dd>2026-07-02</dd>
</dl>
```

---

### [핵심]

Description List 핵심:

- 이름과 값의 쌍에 사용한다.
- 용어와 정의, 메타데이터, 상세 정보에 적합하다.
- `dt`는 term 또는 name이다.
- `dd`는 description 또는 value다.
- 상세 페이지 정보 표시에 유용하다.
- 단순 레이아웃 목적의 남용 금지

---

### [실무]

축제 상세 정보, 사용자 프로필, 설정 요약, 메타데이터 표시에서 사용할 수 있다.

예:

```html
<section>
  <h2>Festival Information</h2>
  <dl>
    <dt>Region</dt>
    <dd>Seoul</dd>

    <dt>Period</dt>
    <dd>2026-07-01 ~ 2026-07-07</dd>

    <dt>Category</dt>
    <dd>Culture</dd>
  </dl>
</section>
```

검수 기준:

- 이름-값 쌍 구조인가?
- table보다 description list가 더 적합한 정보인가?
- dt와 dd 관계가 명확한가?
- 단순 grid layout 목적으로 dl을 남용하지 않았는가?

---

### [FAQ]

Q. dl은 언제 써?
A. 용어와 설명, 이름과 값의 쌍을 표현할 때 사용한다.

Q. dt와 dd는 뭐야?
A. dt는 용어 또는 이름이고 dd는 해당 설명 또는 값이다.

Q. 축제 상세 정보에 dl을 써도 돼?
A. 가능하다. 지역, 기간, 카테고리 같은 이름-값 쌍 정보에 적합하다.

---

# 5. Table Elements

## 5.1 Table Concept

### [개념]

`table`은 행과 열로 구성된 표 데이터를 표현하는 HTML 요소다.

Table은 레이아웃을 만들기 위한 요소가 아니라 데이터 관계를 표현하기 위한 요소다.

---

### [핵심]

Table 핵심:

- 표 형식 데이터에 사용한다.
- 행과 열의 관계가 중요한 데이터에 적합하다.
- 레이아웃 목적으로 사용하지 않는다.
- `caption`은 표 제목 또는 설명을 제공한다.
- `thead`는 헤더 영역이다.
- `tbody`는 본문 영역이다.
- `tr`은 table row다.
- `th`는 header cell이다.
- `td`는 data cell이다.
- `scope`는 header와 data cell의 관계를 명확히 한다.

기본 예:

```html
<table>
  <caption>
    Festival Schedule
  </caption>
  <thead>
    <tr>
      <th scope="col">Date</th>
      <th scope="col">Festival</th>
      <th scope="col">Region</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2026-07-02</td>
      <td>Seoul Light Festival</td>
      <td>Seoul</td>
    </tr>
  </tbody>
</table>
```

---

### [실무]

실무에서 table은 관리자 화면, 통계, 일정표, 주문 목록, 결제 내역, 비교표에 사용된다.

사용 적합:

- 행과 열 관계가 중요한 데이터
- 관리자 목록
- 통계표
- 일정표
- 비교표
- 가격표
- 결제 내역

사용 부적합:

- 페이지 레이아웃
- 카드 그리드
- 단순 정렬
- 버튼 그룹
- 반응형 레이아웃 대체

검수 기준:

- 데이터가 행과 열 관계를 가지는가?
- 레이아웃 목적으로 table을 사용하지 않았는가?
- caption이 있는가?
- th와 td가 구분되어 있는가?
- th에 scope가 있는가?
- 모바일에서 표가 깨지지 않는가?

---

### [FAQ]

Q. table은 언제 써?
A. 행과 열 관계가 중요한 표 데이터를 표현할 때 사용한다.

Q. table로 layout을 잡아도 돼?
A. 안 된다. layout은 CSS Flexbox나 Grid를 사용한다.

Q. th와 td 차이는 뭐야?
A. th는 헤더 셀이고 td는 데이터 셀이다.

Q. caption은 왜 필요해?
A. 표의 제목이나 설명을 제공해 사용자가 표의 목적을 이해하게 한다.

---

## 5.2 Table Accessibility

### [개념]

Table Accessibility는 사용자가 표 데이터의 행, 열, 헤더 관계를 이해할 수 있도록 만드는 기준이다.

스크린 리더는 `caption`, `th`, `scope`를 통해 표 구조를 해석한다.

---

### [핵심]

Table Accessibility 핵심:

- `caption`으로 표 제목 제공
- 컬럼 헤더는 `th scope="col"` 사용
- 행 헤더는 `th scope="row"` 사용
- 데이터 셀은 `td` 사용
- 복잡한 표는 구조를 단순화
- 빈 셀 남용 금지
- 레이아웃 목적 table 금지

예:

```html
<table>
  <caption>
    Monthly Festival Count
  </caption>
  <thead>
    <tr>
      <th scope="col">Month</th>
      <th scope="col">Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">July</th>
      <td>24</td>
    </tr>
  </tbody>
</table>
```

---

### [실무]

복잡한 관리자 테이블에서는 정렬, 필터, 페이지네이션, 반응형 처리를 함께 고려한다.

검수 Checklist:

```md
- [ ] table이 표 데이터에 사용되었는가?
- [ ] caption이 있는가?
- [ ] thead와 tbody가 구분되어 있는가?
- [ ] header cell은 th로 작성되었는가?
- [ ] th에 scope가 있는가?
- [ ] 데이터 셀은 td로 작성되었는가?
- [ ] 빈 셀과 병합 셀을 남용하지 않았는가?
- [ ] 모바일에서 가로 스크롤 또는 대체 UI를 고려했는가?
```

---

### [FAQ]

Q. table 접근성에서 중요한 것은 뭐야?
A. caption, th, scope, 행과 열 구조를 명확히 작성하는 것이다.

Q. scope 속성은 왜 써?
A. header cell이 열 기준인지 행 기준인지 보조 기술에 알려주기 위해 사용한다.

Q. 복잡한 표는 어떻게 해야 해?
A. 가능한 구조를 단순화하고, 필요하면 caption과 header 관계를 명확히 제공한다.

---

## 5.3 Responsive Table

### [개념]

Responsive Table은 작은 화면에서도 표 데이터를 읽고 조작할 수 있도록 설계한 Table UI다.

Table은 열이 많을수록 모바일 화면에서 깨지기 쉽다.

---

### [핵심]

Responsive Table 핵심:

- 표 데이터는 가로 공간을 많이 사용한다.
- 모바일에서 가로 스크롤이 필요할 수 있다.
- 컬럼 수를 줄이는 대체 UI를 고려할 수 있다.
- 카드형 변환 UI를 고려할 수 있다.
- 중요한 컬럼 우선순위를 정한다.
- table 자체를 무리하게 좁히면 가독성이 떨어진다.

기본 가로 스크롤 예:

```html
<div class="table-container">
  <table>
    <caption>
      Festival Schedule
    </caption>
    <thead>
      <tr>
        <th scope="col">Date</th>
        <th scope="col">Festival</th>
        <th scope="col">Region</th>
        <th scope="col">Status</th>
      </tr>
    </thead>
  </table>
</div>
```

```css
.table-container {
  overflow-x: auto;
}

.table-container table {
  min-width: 640px;
}
```

---

### [실무]

관리자 화면과 모바일 사용자 화면의 table 전략은 다를 수 있다.

실무 선택 기준:

```text
Few Columns → Normal Table
Many Columns → Horizontal Scroll
Mobile User Page → Card UI Alternative
Admin Desktop Page → Data Table
Critical Data → Column Priority Review
```

검수 기준:

- 모바일에서 표가 화면 밖으로 깨지지 않는가?
- 가로 스크롤 컨테이너가 있는가?
- 컬럼 수가 지나치게 많지 않은가?
- 카드형 대체 UI가 더 적절하지 않은가?
- 테이블 헤더가 사라져 데이터 의미가 불명확하지 않은가?

---

### [FAQ]

Q. 모바일에서 table이 깨지는 이유는?
A. 컬럼 수가 많고 셀 내용이 길어 화면 너비를 초과하기 때문이다.

Q. Responsive Table은 어떻게 처리해?
A. 가로 스크롤, 컬럼 축소, 카드형 대체 UI 등을 고려한다.

Q. 모든 표를 카드형으로 바꾸는 게 좋아?
A. 아니다. 표 데이터의 비교와 행열 관계가 중요하면 table 구조를 유지하는 것이 좋다.

---

# 6. Comparison Rules

## 6.1 Text Element Comparison

### [개념]

Text Element는 텍스트의 의미와 역할에 따라 구분해서 사용한다.

---

### [핵심]

| 비교         | 목적             | 예시             |
| ------------ | ---------------- | ---------------- |
| `p`          | 일반 문단        | 설명, 안내       |
| `strong`     | 중요한 의미 강조 | 경고, 필수 안내  |
| `em`         | 문맥상 강조      | 특정 단어 강조   |
| `small`      | 부가 설명        | 보조 문구        |
| `mark`       | 하이라이트       | 검색 결과 강조   |
| `code`       | 코드 조각        | CSS 속성, 명령어 |
| `pre`        | 공백 유지 블록   | 코드 블록        |
| `blockquote` | 인용문           | 긴 인용          |

---

### [실무]

선택 기준:

```text
Paragraph → p
Important Warning → strong
Context Emphasis → em
Inline Code → code
Multi Line Code → pre + code
Quote → blockquote
Visual Style Only → CSS class
```

---

### [FAQ]

Q. Text Element는 어떻게 선택해?
A. 텍스트의 시각 모양이 아니라 의미와 역할을 기준으로 선택한다.

Q. 시각 스타일만 바꾸려면 어떤 방식이 좋아?
A. 의미 태그를 남용하지 말고 CSS class를 사용하는 것이 좋다.

---

## 6.2 Link vs Button

### [개념]

Link는 이동을 담당하고 Button은 동작 실행을 담당한다.

---

### [핵심]

| 비교        | Link                        | Button                |
| ----------- | --------------------------- | --------------------- |
| 태그        | `a`                         | `button`              |
| 목적        | 페이지 / URL 이동           | 동작 실행             |
| 핵심 속성   | `href`                      | `type`                |
| 예시        | 상세 페이지 이동, 외부 링크 | 제출, 삭제, 모달 열기 |
| 잘못된 사용 | onClick 동작 남용           | 페이지 이동 처리      |

---

### [실무]

선택 기준:

```text
Move to Detail Page → a / Link
External Website → a
Open Modal → button
Submit Form → button type="submit"
Delete Item → button type="button"
```

---

### [FAQ]

Q. Link와 Button 차이는 뭐야?
A. Link는 이동, Button은 동작 실행에 사용한다.

Q. 상세 페이지 이동은 button이야 link야?
A. link가 적절하다. React Router에서는 Link를 사용할 수 있다.

---

## 6.3 Image Alt Comparison

### [개념]

Image Alt는 이미지의 역할에 따라 다르게 작성한다.

---

### [핵심]

| 이미지 유형      | alt 작성                    |
| ---------------- | --------------------------- |
| 의미 있는 이미지 | 이미지가 전달하는 정보 설명 |
| 장식 이미지      | `alt=""`                    |
| 링크 이미지      | 링크 목적지 설명            |
| 복잡한 차트      | 요약 alt + 상세 설명        |
| 아이콘 버튼      | 버튼 기능 설명              |

---

### [실무]

선택 기준:

```text
Informative Festival Image → 축제 장면 설명
Decorative Divider Image → alt=""
Image Link to Detail Page → 상세 페이지 이동 목적 설명
Chart Image → 핵심 요약 + 주변 설명
Icon Button → aria-label or accessible text
```

---

### [FAQ]

Q. alt는 이미지마다 똑같이 쓰면 돼?
A. 아니다. 이미지가 정보 전달용인지 장식용인지 기능용인지에 따라 다르게 작성한다.

Q. 장식 이미지 alt는 왜 빈 값으로 둬?
A. 보조 기술이 불필요한 장식 이미지를 읽지 않도록 하기 위해서다.

---

## 6.4 List vs Table

### [개념]

List는 항목의 나열에 사용하고 Table은 행과 열 관계가 있는 데이터에 사용한다.

---

### [핵심]

| 비교          | List                  | Table                     |
| ------------- | --------------------- | ------------------------- |
| 목적          | 항목 나열             | 행과 열 데이터            |
| 요소          | `ul`, `ol`, `li`      | `table`, `tr`, `th`, `td` |
| 적합          | 메뉴, 카드 목록, 단계 | 일정표, 통계, 비교표      |
| 구조          | 단순 항목 중심        | 셀 관계 중심              |
| 레이아웃 사용 | 가능하나 의미 우선    | 레이아웃 목적 금지        |

---

### [실무]

선택 기준:

```text
Navigation Menu → ul/li
Card Collection → ul/li + article
Step Guide → ol/li
Name-Value Detail → dl/dt/dd
Schedule Matrix → table
Admin Data List → table
```

---

### [FAQ]

Q. List와 Table은 어떻게 구분해?
A. 단순 항목 나열은 List, 행과 열 관계가 중요한 데이터는 Table을 사용한다.

Q. 카드 목록은 table로 만들어도 돼?
A. 권장하지 않는다. 카드 목록은 list 또는 grid layout이 더 적합하다.

---

# 7. Common Mistakes

## 7.1 Text Link Image List Table Common Mistakes

### [개념]

Text, Link, Image, List, Table 요소의 잘못된 사용은 Accessibility, SEO, UX, Maintainability 문제로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- 문단 간격을 `br`로 조절
- 제목을 `p` 또는 `strong`으로 작성
- 단순 스타일링 목적으로 `strong`, `em` 남용
- `href` 없는 `a` 태그 사용
- `href="#"` 임시 링크 방치
- 페이지 이동을 `button`으로 처리
- 링크 텍스트를 `Click here`로 작성
- 아이콘 링크에 accessible name 없음
- 이미지 alt 누락
- 파일명을 alt로 사용
- 장식 이미지에 불필요한 alt 작성
- 링크 이미지 alt가 목적지를 설명하지 않음
- 목록을 `br` 또는 `div` 반복으로 작성
- 순서 있는 절차를 `ul`로 작성
- table을 layout 목적으로 사용
- table에 caption 없음
- th와 td 구분 없음
- 모바일 table overflow 미처리

---

### [실무]

Troubleshooting Flow:

```text
UI Content Review
→ Text Semantics Check
→ Link Purpose Check
→ Image Alt Check
→ List Structure Check
→ Table Data Structure Check
→ Accessibility Check
→ Responsive Check
```

문제 예:

```text
문제: 스크린 리더가 이미지 의미를 전달하지 못함
원인: alt 누락
해결: 의미 있는 alt 작성
```

```text
문제: 링크 목록 의미가 불명확함
원인: div 반복으로 메뉴 작성
해결: nav + ul + li + a 구조 사용
```

```text
문제: 모바일에서 표가 화면 밖으로 삐져나감
원인: 컬럼이 많은 table에 overflow 처리 없음
해결: table container에 overflow-x auto 적용
```

---

### [FAQ]

Q. 텍스트 요소에서 가장 흔한 실수는 뭐야?
A. 제목을 p나 strong으로 작성하고, 간격을 br로 조절하는 실수가 많다.

Q. 링크에서 가장 흔한 실수는 뭐야?
A. href 없는 a 태그, Click here 텍스트, button으로 페이지 이동 처리하는 실수가 많다.

Q. 이미지에서 가장 흔한 실수는 뭐야?
A. alt 누락, 파일명 alt, 장식 이미지 alt 오용이 흔하다.

Q. 목록에서 가장 흔한 실수는 뭐야?
A. 목록을 ul/ol/li가 아니라 div나 br로 표현하는 실수가 많다.

Q. table에서 가장 흔한 실수는 뭐야?
A. layout 목적으로 table을 쓰거나 caption, th, scope를 누락하는 실수가 많다.

---

# 8. Best Practice

## 8.1 Text Link Image List Table Best Practice

### [개념]

Text, Link, Image, List, Table Best Practice는 콘텐츠 의미, 접근성, SEO, 반응형 UI, React Markup 품질을 높이는 작성 기준이다.

---

### [핵심]

권장 기준:

- 문단은 `p` 사용
- 제목은 heading 사용
- 중요한 의미 강조는 `strong` 사용
- 단순 스타일링은 CSS class 사용
- inline code는 `code` 사용
- code block은 `pre` + `code` 사용
- 페이지 이동은 `a` 또는 Router Link 사용
- 동작 실행은 `button` 사용
- 링크 텍스트는 목적지 설명
- 외부 새 창 링크는 `rel="noopener noreferrer"` 사용
- 의미 있는 이미지는 alt 작성
- 장식 이미지는 `alt=""`
- 이미지와 캡션은 `figure` + `figcaption` 고려
- 순서 없는 목록은 `ul`
- 순서 있는 목록은 `ol`
- 이름-값 쌍은 `dl`
- 표 데이터는 `table`
- table에는 `caption`, `th`, `scope` 사용
- 모바일 table overflow 처리 고려

---

### [실무]

콘텐츠 구조 예:

```html
<main>
  <h1>Festival Guide</h1>

  <section aria-labelledby="popular-title">
    <h2 id="popular-title">Popular Festivals</h2>
    <p>Explore popular festivals by region and date.</p>

    <ul class="festival-list">
      <li>
        <article>
          <h3>
            <a href="/festivals/1">Seoul Light Festival</a>
          </h3>
          <figure>
            <img
              src="/images/seoul-light.jpg"
              alt="서울 야간 빛 축제의 조명 터널"
              width="640"
              height="360"
              loading="lazy"
            />
            <figcaption>Seoul Light Festival main light tunnel.</figcaption>
          </figure>
          <p>
            <strong>Notice:</strong> Schedule may change depending on weather.
          </p>
        </article>
      </li>
    </ul>
  </section>
</main>
```

Table 예:

```html
<div class="table-container">
  <table>
    <caption>
      Festival Schedule
    </caption>
    <thead>
      <tr>
        <th scope="col">Date</th>
        <th scope="col">Festival</th>
        <th scope="col">Region</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2026-07-02</td>
        <td>Seoul Light Festival</td>
        <td>Seoul</td>
      </tr>
    </tbody>
  </table>
</div>
```

검수 Checklist:

```md
- [ ] 일반 문단이 p로 작성되었는가?
- [ ] 제목이 heading으로 작성되었는가?
- [ ] 의미 강조와 시각 스타일링을 구분했는가?
- [ ] 링크 텍스트가 목적지를 설명하는가?
- [ ] 페이지 이동과 동작 실행을 구분했는가?
- [ ] 외부 링크 보안 속성이 있는가?
- [ ] 이미지 alt가 적절한가?
- [ ] 장식 이미지 alt가 비어 있는가?
- [ ] 목록이 ul/ol/li로 작성되었는가?
- [ ] 이름-값 쌍에 dl을 고려했는가?
- [ ] 표 데이터에 table을 사용했는가?
- [ ] table에 caption, th, scope가 있는가?
- [ ] 모바일 table 대응이 있는가?
```

---

### [FAQ]

Q. Text Link Image List Table Best Practice는 뭐야?
A. 콘텐츠의 의미에 맞는 HTML 요소를 선택하고 접근성, SEO, 반응형 기준을 함께 적용하는 것이다.

Q. 이 문서 검수에서 가장 먼저 볼 것은 뭐야?
A. 텍스트 의미, 링크 목적, 이미지 alt, 목록 구조, table 접근성을 먼저 확인한다.

Q. React에서도 이 기준을 적용해야 해?
A. 적용해야 한다. JSX도 최종적으로 HTML DOM으로 렌더링되기 때문이다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 텍스트, 링크, 이미지, 목록, 표 콘텐츠를 의미 있고 접근성 있게 생성하고 검토하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. HTML Text Element가 뭐야?
A. 텍스트 콘텐츠를 의미와 구조에 맞게 표현하는 HTML 요소다.

Q. p 태그는 언제 써?
A. 일반 문단, 설명, 안내 문구, 카드 설명에 사용한다.

Q. 제목도 p로 써도 돼?
A. 권장하지 않는다. 제목은 heading 태그를 사용한다.

Q. strong은 언제 써?
A. 중요한 의미를 가진 내용이나 경고, 핵심 안내에 사용한다.

Q. em은 언제 써?
A. 문장 안에서 문맥상 강조가 필요한 단어나 표현에 사용한다.

Q. 글자를 굵게 만들려고 strong을 써도 돼?
A. 단순 시각 효과 목적이라면 CSS를 사용하는 것이 좋다.

Q. code 태그는 언제 써?
A. 짧은 코드 조각, 속성명, 명령어, 파일명을 표현할 때 사용한다.

Q. pre 태그는 언제 써?
A. 줄바꿈과 공백을 유지해야 하는 긴 코드 블록이나 출력 결과에 사용한다.

Q. 긴 코드 블록은 어떻게 작성해?
A. 보통 `<pre><code>...</code></pre>` 구조를 사용한다.

Q. a 태그는 언제 써?
A. URL 이동, 페이지 이동, 파일 다운로드, 문서 위치 이동에 사용한다.

Q. button과 a 태그 차이는 뭐야?
A. button은 동작 실행, a는 페이지 또는 URL 이동에 사용한다.

Q. href 없는 a 태그를 써도 돼?
A. 권장하지 않는다. 링크 의미와 접근성이 깨질 수 있다.

Q. 새 창 링크에는 무엇을 같이 써야 해?
A. `target="_blank"`를 사용할 때 `rel="noopener noreferrer"`를 함께 쓰는 것이 좋다.

Q. 좋은 링크 텍스트는 뭐야?
A. 링크 목적지를 명확히 설명하고 단독으로 읽어도 의미가 있는 텍스트다.

Q. Click here는 왜 좋지 않아?
A. 링크 목적지를 설명하지 않아 접근성과 사용성이 떨어진다.

Q. 아이콘만 있는 링크는 어떻게 해야 해?
A. `aria-label` 또는 숨김 텍스트로 접근 가능한 이름을 제공해야 한다.

Q. Internal Link와 External Link 차이는 뭐야?
A. Internal Link는 서비스 내부 이동이고 External Link는 외부 도메인으로 이동하는 링크다.

Q. target blank에는 왜 rel을 같이 써?
A. 새 창 보안 문제를 줄이기 위해 `rel="noopener noreferrer"`를 함께 사용한다.

Q. img 태그는 언제 써?
A. 웹 페이지에 이미지를 표시할 때 사용한다.

Q. img src는 뭐야?
A. 표시할 이미지 파일의 경로다.

Q. img alt는 왜 필요해?
A. 이미지가 보이지 않거나 스크린 리더를 사용할 때 이미지 의미를 전달하기 위해 필요하다.

Q. 이미지 반응형은 어떻게 처리해?
A. 일반적으로 `max-width: 100%`와 `height: auto`를 사용한다.

Q. 모든 이미지에 alt가 필요해?
A. 필요하다. 의미 있는 이미지는 설명을 넣고 장식 이미지는 빈 alt를 사용할 수 있다.

Q. alt에 이미지라고 써야 해?
A. 대부분 필요 없다. 스크린 리더가 이미 이미지임을 알려줄 수 있다.

Q. 장식 이미지는 alt를 어떻게 써?
A. `alt=""`처럼 빈 alt를 사용해 보조 기술이 무시하도록 할 수 있다.

Q. 링크 안의 이미지 alt는 어떻게 써?
A. 이미지 설명보다 링크 목적지를 설명하는 것이 좋다.

Q. figure는 언제 써?
A. 이미지, 차트, 코드, 도표처럼 캡션과 함께 독립적으로 이해 가능한 콘텐츠에 사용한다.

Q. figcaption은 왜 써?
A. figure 콘텐츠의 설명, 제목, 출처를 제공하기 위해 사용한다.

Q. 모든 이미지에 figure를 써야 해?
A. 아니다. 캡션이나 독립 콘텐츠 의미가 있을 때 사용하면 된다.

Q. ul은 언제 써?
A. 순서가 중요하지 않은 항목 목록에 사용한다.

Q. ol은 언제 써?
A. 순서가 중요한 절차, 단계, 순위, 랭킹 목록에 사용한다.

Q. ul과 ol 차이는 뭐야?
A. ul은 순서 없는 목록, ol은 순서가 중요한 목록에 사용한다.

Q. li는 어디에 써?
A. ul 또는 ol 내부의 각 목록 항목에 사용한다.

Q. 메뉴도 ul로 만들어도 돼?
A. 가능하다. Navigation 메뉴는 목록 구조로 표현하기 좋다.

Q. 카드 목록도 ul을 써도 돼?
A. 가능하다. 여러 카드가 반복되는 목록이라면 ul/li 구조가 적절할 수 있다.

Q. dl은 언제 써?
A. 용어와 설명, 이름과 값의 쌍을 표현할 때 사용한다.

Q. dt와 dd는 뭐야?
A. dt는 용어 또는 이름이고 dd는 해당 설명 또는 값이다.

Q. 축제 상세 정보에 dl을 써도 돼?
A. 가능하다. 지역, 기간, 카테고리 같은 이름-값 쌍 정보에 적합하다.

Q. table은 언제 써?
A. 행과 열 관계가 중요한 표 데이터를 표현할 때 사용한다.

Q. table로 layout을 잡아도 돼?
A. 안 된다. layout은 CSS Flexbox나 Grid를 사용한다.

Q. th와 td 차이는 뭐야?
A. th는 헤더 셀이고 td는 데이터 셀이다.

Q. caption은 왜 필요해?
A. 표의 제목이나 설명을 제공해 사용자가 표의 목적을 이해하게 한다.

Q. table 접근성에서 중요한 것은 뭐야?
A. caption, th, scope, 행과 열 구조를 명확히 작성하는 것이다.

Q. scope 속성은 왜 써?
A. header cell이 열 기준인지 행 기준인지 보조 기술에 알려주기 위해 사용한다.

Q. 모바일에서 table이 깨지는 이유는?
A. 컬럼 수가 많고 셀 내용이 길어 화면 너비를 초과하기 때문이다.

Q. Responsive Table은 어떻게 처리해?
A. 가로 스크롤, 컬럼 축소, 카드형 대체 UI 등을 고려한다.

Q. List와 Table은 어떻게 구분해?
A. 단순 항목 나열은 List, 행과 열 관계가 중요한 데이터는 Table을 사용한다.

Q. 카드 목록은 table로 만들어도 돼?
A. 권장하지 않는다. 카드 목록은 list 또는 grid layout이 더 적합하다.

Q. 텍스트 요소에서 가장 흔한 실수는 뭐야?
A. 제목을 p나 strong으로 작성하고, 간격을 br로 조절하는 실수가 많다.

Q. 링크에서 가장 흔한 실수는 뭐야?
A. href 없는 a 태그, Click here 텍스트, button으로 페이지 이동 처리하는 실수가 많다.

Q. 이미지에서 가장 흔한 실수는 뭐야?
A. alt 누락, 파일명 alt, 장식 이미지 alt 오용이 흔하다.

Q. 목록에서 가장 흔한 실수는 뭐야?
A. 목록을 ul/ol/li가 아니라 div나 br로 표현하는 실수가 많다.

Q. table에서 가장 흔한 실수는 뭐야?
A. layout 목적으로 table을 쓰거나 caption, th, scope를 누락하는 실수가 많다.

Q. Text Link Image List Table Best Practice는 뭐야?
A. 콘텐츠의 의미에 맞는 HTML 요소를 선택하고 접근성, SEO, 반응형 기준을 함께 적용하는 것이다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 텍스트, 링크, 이미지, 목록, 표 콘텐츠를 의미 있고 접근성 있게 생성하고 검토하게 만드는 것이다.
