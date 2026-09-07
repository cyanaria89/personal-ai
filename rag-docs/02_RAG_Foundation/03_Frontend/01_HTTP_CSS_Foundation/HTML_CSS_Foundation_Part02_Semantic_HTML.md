# HTML CSS Foundation Part02 - Semantic HTML

---

# 1. Semantic HTML

## 1.1 Semantic HTML Concept

### [개념]

Semantic HTML은 태그의 의미를 기준으로 HTML 구조를 작성하는 방식이다.

Semantic HTML은 화면 모양이 아니라 콘텐츠의 역할과 구조를 표현한다.

예:

```html
<header>Header</header>
<nav>Navigation</nav>
<main>Main Content</main>
<section>Section</section>
<article>Article</article>
<aside>Aside</aside>
<footer>Footer</footer>
```

Semantic HTML은 Accessibility, SEO, Maintainability, Frontend Component Structure와 직접 연결된다.

---

### [핵심]

Semantic HTML 핵심:

- 태그의 의미를 기준으로 구조를 작성한다.
- `div`만 사용하는 구조를 줄인다.
- 문서 구조를 브라우저, 검색 엔진, 스크린 리더가 이해하기 쉽게 만든다.
- React Component도 최종적으로 Semantic HTML을 렌더링해야 한다.
- 화면 디자인은 CSS가 담당하고 HTML은 구조와 의미를 담당한다.
- Semantic HTML은 Accessibility 기본 품질을 높인다.
- Semantic HTML은 SEO Basics와 연결된다.

---

### [실무]

2026 실무 기준에서 Semantic HTML은 단순 HTML 태그 암기가 아니다.

Frontend Agent는 Semantic HTML을 사용해 아래 작업을 수행해야 한다.

- Page Layout 구조 설계
- Header / Navigation / Main / Footer 분리
- Section 단위 화면 구조 설계
- Card / List / Form / Button 의미 검토
- React JSX 변환 가능한 Markup 생성
- Accessibility 기본 검토
- SEO 기본 구조 검토
- div 남용 코드 Review

권장 Flow:

```text
Content Meaning
→ Semantic Tag Selection
→ Heading Structure
→ Accessibility Check
→ CSS Styling
→ React JSX Conversion
```

---

### [FAQ]

Q. Semantic HTML이 뭐야?
A. 태그의 의미를 기준으로 HTML 구조를 작성하는 방식이다.

Q. Semantic HTML은 왜 필요해?
A. 접근성, SEO, 유지보수성, 문서 구조 이해를 높이기 위해 필요하다.

Q. div를 쓰면 안 돼?
A. 아니다. 의미 있는 태그가 없을 때는 div를 사용할 수 있다.

Q. 모든 영역을 div로 작성하면 안 돼?
A. 권장하지 않는다. 문서 구조와 역할이 드러나지 않아 접근성과 유지보수성이 떨어진다.

Q. React를 써도 Semantic HTML이 필요해?
A. 필요하다. React Component도 최종적으로 HTML로 렌더링되기 때문이다.

---

# 2. Semantic Layout Tags

## 2.1 Header

### [개념]

`header`는 페이지 또는 구역의 상단 영역을 의미하는 Semantic HTML 태그다.

일반적으로 로고, 제목, 검색, 주요 안내, Navigation 진입부를 포함한다.

---

### [핵심]

`header` 핵심:

- 페이지 상단 영역에 사용한다.
- Section 또는 Article 내부에서도 사용할 수 있다.
- 로고, 제목, 검색, 주요 버튼을 포함할 수 있다.
- `header`는 단순 시각적 상단 박스가 아니라 콘텐츠의 머리말 영역이다.
- 페이지에 여러 개의 `header`가 존재할 수 있다.

예:

```html
<header class="site-header">
  <h1>FestaPick</h1>
  <nav aria-label="Main Navigation">
    <a href="/festivals">Festivals</a>
    <a href="/calendar">Calendar</a>
  </nav>
</header>
```

---

### [실무]

실무에서는 `header`를 App Layout 또는 Page Layout의 상단 구조로 자주 사용한다.

React Component 예:

```jsx
function SiteHeader() {
  return (
    <header className="site-header">
      <h1>FestaPick</h1>
      <nav aria-label="Main Navigation">
        <a href="/festivals">Festivals</a>
        <a href="/calendar">Calendar</a>
      </nav>
    </header>
  );
}
```

검수 기준:

- 페이지 상단 구조가 `div`만으로 작성되지 않았는가?
- 로고나 페이지 제목이 적절한 heading 또는 link로 작성되었는가?
- Navigation이 포함될 경우 `nav` 태그를 사용했는가?
- `header`를 단순 스타일 박스로만 사용하지 않았는가?

---

### [FAQ]

Q. header는 페이지에 하나만 써야 해?
A. 아니다. 페이지 전체 header와 article 또는 section 내부 header를 함께 사용할 수 있다.

Q. header 안에 nav를 넣어도 돼?
A. 가능하다. 주요 탐색 메뉴가 상단에 있으면 header 내부에 nav를 넣는 구조가 일반적이다.

Q. header는 div와 뭐가 달라?
A. header는 상단 머리말 영역이라는 의미를 가진다. div는 의미가 없는 일반 컨테이너다.

---

## 2.2 Nav

### [개념]

`nav`는 주요 탐색 링크 영역을 의미하는 Semantic HTML 태그다.

사이트 메뉴, 페이지 이동 링크, 주요 라우팅 링크를 묶을 때 사용한다.

---

### [핵심]

`nav` 핵심:

- 주요 Navigation 영역에 사용한다.
- 모든 링크 묶음에 사용할 필요는 없다.
- 사이트 전체 메뉴, 사이드 메뉴, 탭 메뉴에 적합하다.
- `aria-label`을 사용하면 여러 nav를 구분하기 쉽다.
- Navigation link는 보통 `a` 태그 또는 Router Link로 작성한다.

예:

```html
<nav aria-label="Main Navigation">
  <a href="/">Home</a>
  <a href="/search">Search</a>
  <a href="/calendar">Calendar</a>
</nav>
```

---

### [실무]

React Router를 사용하는 경우에도 의미는 `nav`로 유지한다.

예:

```jsx
import { Link } from "react-router-dom";

function MainNavigation() {
  return (
    <nav aria-label="Main Navigation">
      <Link to="/">Home</Link>
      <Link to="/search">Search</Link>
      <Link to="/calendar">Calendar</Link>
    </nav>
  );
}
```

검수 기준:

- 주요 메뉴가 `nav`로 감싸져 있는가?
- 단순 관련 링크 목록에 nav를 남용하지 않았는가?
- 여러 nav가 있을 때 `aria-label`로 구분했는가?
- 페이지 이동은 `button`이 아니라 link 계열로 작성했는가?

---

### [FAQ]

Q. nav는 언제 써?
A. 사이트 메뉴, 주요 페이지 이동, 탭 메뉴 같은 탐색 영역에 사용한다.

Q. 모든 링크에 nav를 써야 해?
A. 아니다. 주요 탐색 링크 묶음에만 사용하는 것이 좋다.

Q. nav에 aria-label이 필요한 이유는?
A. 여러 nav가 있을 때 스크린 리더가 탐색 영역을 구분할 수 있도록 돕는다.

Q. React Router Link도 nav 안에 넣어도 돼?
A. 가능하다. Router Link도 최종적으로 링크 역할을 하기 때문이다.

---

## 2.3 Main

### [개념]

`main`은 페이지의 핵심 콘텐츠 영역을 의미하는 Semantic HTML 태그다.

한 페이지에서 반복되는 Header, Navigation, Footer를 제외한 주요 내용을 담는다.

---

### [핵심]

`main` 핵심:

- 페이지의 주요 콘텐츠 영역이다.
- 일반적으로 한 페이지에 하나만 사용한다.
- Header, Nav, Footer와 구분되는 핵심 본문이다.
- Accessibility에서 본문 바로가기와 연결될 수 있다.
- SPA에서도 현재 Route의 주요 콘텐츠를 `main`으로 감싸는 것이 좋다.

예:

```html
<main>
  <h1>Festival Search</h1>
  <section>
    <h2>Search Filters</h2>
  </section>
</main>
```

---

### [실무]

React Layout에서는 App 또는 Page Component의 핵심 영역을 `main`으로 감싼다.

예:

```jsx
function FestivalSearchPage() {
  return (
    <main>
      <h1>Festival Search</h1>
      <section aria-labelledby="filter-title">
        <h2 id="filter-title">Search Filters</h2>
      </section>
    </main>
  );
}
```

검수 기준:

- 주요 콘텐츠가 `main` 내부에 있는가?
- 페이지에 `main`이 여러 개 있지 않은가?
- `main` 내부에 페이지 핵심 heading이 있는가?
- Header / Footer와 본문 영역이 분리되어 있는가?

---

### [FAQ]

Q. main은 언제 써?
A. 페이지의 핵심 본문 콘텐츠를 감쌀 때 사용한다.

Q. main은 여러 개 써도 돼?
A. 일반적인 페이지에서는 하나만 사용하는 것이 명확하다.

Q. React SPA에서도 main을 써야 해?
A. 권장된다. 현재 페이지 또는 Route의 핵심 콘텐츠 영역을 명확히 할 수 있다.

---

## 2.4 Section

### [개념]

`section`은 문서에서 주제별 구역을 나타내는 Semantic HTML 태그다.

각 `section`은 일반적으로 heading을 가진다.

---

### [핵심]

`section` 핵심:

- 주제별 콘텐츠 구역에 사용한다.
- heading과 함께 사용하는 것이 좋다.
- 독립 콘텐츠보다는 페이지 내부 구역에 적합하다.
- 단순 스타일링 wrapper로 사용하지 않는다.
- 의미 없는 grouping은 `div`가 더 적합할 수 있다.

예:

```html
<section aria-labelledby="popular-title">
  <h2 id="popular-title">Popular Festivals</h2>
  <p>Popular festival list by user activity.</p>
</section>
```

---

### [실무]

실무에서 `section`은 Page Component 내부 콘텐츠 구분에 자주 사용된다.

예:

```jsx
function HomePage() {
  return (
    <main>
      <h1>FestaPick</h1>

      <section aria-labelledby="banner-title">
        <h2 id="banner-title">Festival Banner</h2>
      </section>

      <section aria-labelledby="popular-title">
        <h2 id="popular-title">Popular Festivals</h2>
      </section>
    </main>
  );
}
```

검수 기준:

- section마다 명확한 주제가 있는가?
- section에 heading이 있는가?
- 단순 CSS wrapper를 section으로 사용하지 않았는가?
- article이 더 적절한 독립 콘텐츠인지 검토했는가?

---

### [FAQ]

Q. section은 언제 써?
A. 페이지 안에서 주제별 구역을 나눌 때 사용한다.

Q. section에는 heading이 꼭 필요해?
A. 일반적으로 필요하다. section의 주제를 heading으로 명확히 표현하는 것이 좋다.

Q. 단순히 여백을 주려고 section을 써도 돼?
A. 권장하지 않는다. 단순 스타일링 wrapper는 div가 더 적합할 수 있다.

---

## 2.5 Article

### [개념]

`article`은 독립적으로 의미를 가지는 콘텐츠를 나타내는 Semantic HTML 태그다.

게시글, 뉴스, 카드, 리뷰, 댓글, 축제 정보 카드처럼 독립적으로 재사용 가능한 콘텐츠에 적합하다.

---

### [핵심]

`article` 핵심:

- 독립 콘텐츠에 사용한다.
- 단독으로 분리해도 의미가 유지되어야 한다.
- 게시글, 리뷰, 댓글, 상품 카드, 축제 카드에 적합하다.
- 내부에 heading을 포함하는 것이 좋다.
- 목록 내부의 반복 카드 구조에 사용할 수 있다.

예:

```html
<article class="festival-card">
  <h2>Seoul Light Festival</h2>
  <p>Night light festival in Seoul.</p>
  <a href="/festivals/1">View Detail</a>
</article>
```

---

### [실무]

카드 UI에서 `article`은 자주 사용된다.

React 예:

```jsx
function FestivalCard({ festival }) {
  return (
    <article className="festival-card">
      <h2>{festival.title}</h2>
      <p>{festival.description}</p>
      <a href={`/festivals/${festival.id}`}>View Detail</a>
    </article>
  );
}
```

검수 기준:

- 카드가 독립 콘텐츠인가?
- article 내부에 제목이 있는가?
- 단순 레이아웃 박스를 article로 사용하지 않았는가?
- section과 article의 역할을 혼동하지 않았는가?

---

### [FAQ]

Q. article은 언제 써?
A. 게시글, 리뷰, 댓글, 카드처럼 독립적으로 의미 있는 콘텐츠에 사용한다.

Q. section과 article 차이는 뭐야?
A. section은 주제 구역이고 article은 독립적으로 재사용 가능한 콘텐츠다.

Q. 카드 UI에 article을 써도 돼?
A. 카드가 독립 콘텐츠라면 article을 사용할 수 있다.

---

## 2.6 Aside

### [개념]

`aside`는 본문과 관련된 보조 콘텐츠를 나타내는 Semantic HTML 태그다.

사이드바, 추천 목록, 관련 링크, 광고, 보조 정보에 적합하다.

---

### [핵심]

`aside` 핵심:

- 주요 본문이 아닌 보조 콘텐츠에 사용한다.
- 사이드바에 자주 사용된다.
- 관련 콘텐츠, 추천 콘텐츠, 부가 정보에 적합하다.
- main 내부 또는 외부에 위치할 수 있다.
- 핵심 콘텐츠를 aside에 넣지 않는다.

예:

```html
<aside aria-labelledby="related-title">
  <h2 id="related-title">Related Festivals</h2>
  <ul>
    <li><a href="/festivals/2">Busan Festival</a></li>
  </ul>
</aside>
```

---

### [실무]

실무에서는 Desktop Layout의 Sidebar 또는 Detail Page의 Related Section에 사용한다.

예:

```jsx
function FestivalAside() {
  return (
    <aside aria-labelledby="nearby-title">
      <h2 id="nearby-title">Nearby Festivals</h2>
      <ul>
        <li>
          <a href="/festivals/3">Nearby Festival</a>
        </li>
      </ul>
    </aside>
  );
}
```

검수 기준:

- 보조 콘텐츠인가?
- 본문 핵심 정보가 aside로 빠지지 않았는가?
- related, recommendation, sidebar 역할이 명확한가?
- heading 또는 aria-label로 보조 영역을 설명했는가?

---

### [FAQ]

Q. aside는 언제 써?
A. 본문과 관련된 보조 콘텐츠, 사이드바, 추천 목록에 사용한다.

Q. aside는 main 안에 있어도 돼?
A. 가능하다. 본문과 밀접한 보조 정보라면 main 내부에 위치할 수 있다.

Q. 핵심 콘텐츠를 aside에 넣어도 돼?
A. 권장하지 않는다. aside는 보조 콘텐츠를 위한 영역이다.

---

## 2.7 Footer

### [개념]

`footer`는 페이지 또는 구역의 하단 정보를 나타내는 Semantic HTML 태그다.

저작권, 회사 정보, 관련 링크, 정책 링크, 작성자 정보 등을 포함한다.

---

### [핵심]

`footer` 핵심:

- 페이지 또는 구역의 하단 정보에 사용한다.
- 저작권, 정책 링크, 연락처, 작성자 정보에 적합하다.
- 페이지에 여러 footer가 존재할 수 있다.
- article 내부 footer는 글 작성자, 작성일, 태그 정보를 담을 수 있다.
- 단순 하단 여백용 wrapper가 아니다.

예:

```html
<footer class="site-footer">
  <p>&copy; 2026 FestaPick</p>
  <a href="/privacy">Privacy Policy</a>
</footer>
```

---

### [실무]

React Layout에서는 SiteFooter Component로 분리하는 경우가 많다.

예:

```jsx
function SiteFooter() {
  return (
    <footer className="site-footer">
      <p>&copy; 2026 FestaPick</p>
      <nav aria-label="Footer Navigation">
        <a href="/terms">Terms</a>
        <a href="/privacy">Privacy</a>
      </nav>
    </footer>
  );
}
```

검수 기준:

- 페이지 하단 정보가 footer로 작성되었는가?
- footer 내부 링크가 명확한가?
- footer를 단순 스타일 박스로 사용하지 않았는가?
- footer nav가 있을 경우 aria-label로 구분했는가?

---

### [FAQ]

Q. footer는 페이지에 하나만 써야 해?
A. 아니다. 페이지 footer와 article footer를 함께 사용할 수 있다.

Q. footer에는 무엇을 넣어?
A. 저작권, 정책 링크, 연락처, 작성자 정보, 관련 링크를 넣을 수 있다.

Q. footer 안에 nav를 넣어도 돼?
A. 가능하다. 하단 탐색 링크가 있으면 footer 안에 nav를 사용할 수 있다.

---

# 3. Interactive Semantic Elements

## 3.1 Button

### [개념]

`button`은 사용자의 동작을 실행하는 Semantic HTML 요소다.

클릭, 제출, 모달 열기, 좋아요, 삭제, 필터 적용 같은 동작에 사용한다.

---

### [핵심]

`button` 핵심:

- 동작 실행에 사용한다.
- 페이지 이동에는 사용하지 않는다.
- `type` 속성을 명시하는 것이 좋다.
- form 내부 button의 기본 type은 submit이다.
- 클릭 가능한 div 대신 button을 사용한다.
- 키보드 접근성과 기본 동작을 제공한다.

예:

```html
<button type="button">Open Modal</button> <button type="submit">Submit</button>
```

---

### [실무]

React에서 클릭 이벤트는 button에 연결한다.

예:

```jsx
function LikeButton({ onLike }) {
  return (
    <button type="button" onClick={onLike}>
      Like
    </button>
  );
}
```

금지 예:

```html
<div onclick="openModal()">Open Modal</div>
```

검수 기준:

- 클릭 동작이 button으로 작성되었는가?
- form 내부 button에 type이 명시되었는가?
- 페이지 이동을 button으로 처리하지 않았는가?
- keyboard focus가 가능한가?
- disabled 상태가 필요한 경우 `disabled` 속성을 사용하는가?

---

### [FAQ]

Q. button은 언제 써?
A. 클릭, 제출, 삭제, 좋아요, 모달 열기 같은 동작 실행에 사용한다.

Q. div에 onClick을 붙이면 안 돼?
A. 권장하지 않는다. button은 기본 키보드 접근성과 역할을 제공한다.

Q. form 안의 button type을 꼭 써야 해?
A. 명시하는 것이 좋다. 기본 submit 동작으로 의도치 않은 제출이 발생할 수 있다.

Q. 페이지 이동에 button을 써도 돼?
A. 권장하지 않는다. 페이지 이동은 a 또는 Router Link를 사용한다.

---

## 3.2 Anchor Link

### [개념]

`a` 태그는 다른 URL, 페이지, 문서 위치로 이동하는 링크 요소다.

Navigation, 외부 링크, 상세 페이지 이동, 다운로드 링크 등에 사용한다.

---

### [핵심]

`a` 핵심:

- 페이지 이동 또는 URL 이동에 사용한다.
- `href` 속성이 핵심이다.
- 새 창 링크는 `target="_blank"`를 사용할 수 있다.
- 새 창 링크에는 보안상 `rel="noopener noreferrer"`를 함께 사용한다.
- 동작 실행에는 button이 더 적합하다.
- 링크 텍스트는 목적지를 이해할 수 있어야 한다.

예:

```html
<a href="/festivals/1">View Festival Detail</a>
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  External Site
</a>
```

---

### [실무]

React Router에서는 `Link`를 사용해 SPA Navigation을 처리한다.

예:

```jsx
import { Link } from "react-router-dom";

function FestivalDetailLink({ festivalId }) {
  return <Link to={`/festivals/${festivalId}`}>View Festival Detail</Link>;
}
```

검수 기준:

- 페이지 이동은 link 계열로 작성했는가?
- `href` 없는 a 태그를 사용하지 않았는가?
- 링크 텍스트가 “Click here”처럼 불명확하지 않은가?
- 새 창 링크에 `rel="noopener noreferrer"`가 있는가?
- 동작 실행을 a 태그로 남용하지 않았는가?

---

### [FAQ]

Q. a 태그는 언제 써?
A. URL 이동, 페이지 이동, 문서 위치 이동에 사용한다.

Q. button과 a 태그 차이는 뭐야?
A. button은 동작 실행, a는 페이지 또는 URL 이동에 사용한다.

Q. href 없는 a 태그를 써도 돼?
A. 권장하지 않는다. 링크 의미가 사라지고 접근성에 좋지 않다.

Q. 새 창 링크에는 무엇을 같이 써야 해?
A. `target="_blank"`를 사용할 때 `rel="noopener noreferrer"`를 함께 쓰는 것이 좋다.

---

# 4. Heading and Semantic Structure

## 4.1 Heading Structure

### [개념]

Heading은 문서의 제목 계층을 표현하는 HTML 요소다.

Semantic HTML에서 heading은 콘텐츠 구조를 이해하는 핵심 기준이다.

예:

```html
<h1>Festival Search</h1>
<h2>Search Filters</h2>
<h3>Region Filter</h3>
```

---

### [핵심]

Heading 핵심:

- `h1`은 페이지 핵심 제목이다.
- `h2`는 주요 구역 제목이다.
- `h3`는 하위 구역 제목이다.
- heading level을 건너뛰지 않는다.
- 글자 크기 조절 목적으로 heading을 사용하지 않는다.
- heading 구조는 스크린 리더와 SEO에 중요하다.
- section과 article은 heading과 함께 사용하는 것이 좋다.

좋은 구조:

```text
h1
→ h2
  → h3
→ h2
  → h3
```

나쁜 구조:

```text
h1
→ h4
→ h2
```

---

### [실무]

페이지 설계 시 먼저 heading outline을 만든다.

예:

```html
<main>
  <h1>Festival Search</h1>

  <section>
    <h2>Search Filters</h2>
    <h3>Region</h3>
    <h3>Date</h3>
  </section>

  <section>
    <h2>Search Results</h2>
  </section>
</main>
```

검수 기준:

- 한 페이지의 핵심 제목이 h1인가?
- heading level을 건너뛰지 않았는가?
- CSS 스타일링 목적으로 heading을 사용하지 않았는가?
- section과 article에 제목이 있는가?
- heading 텍스트가 구역 내용을 설명하는가?

---

### [FAQ]

Q. heading은 왜 중요해?
A. 문서 구조, 접근성, SEO, 콘텐츠 탐색에 중요하다.

Q. h1은 여러 개 써도 돼?
A. 가능은 하지만 일반적인 페이지에서는 핵심 제목 하나를 h1로 두는 구조가 명확하다.

Q. h2 다음에 h4를 써도 돼?
A. 권장하지 않는다. heading level을 순서대로 사용하는 것이 좋다.

Q. 글자 크게 만들려고 h1을 써도 돼?
A. 안 된다. 글자 크기는 CSS로 조절하고 heading은 문서 구조 표현에 사용한다.

---

# 5. Div and Span Usage

## 5.1 Div

### [개념]

`div`는 의미를 가지지 않는 block-level generic container다.

Semantic HTML 태그로 표현하기 어려운 레이아웃 그룹, 스타일링 wrapper, 컴포넌트 내부 구조에 사용한다.

---

### [핵심]

`div` 핵심:

- 의미 없는 일반 컨테이너다.
- 레이아웃과 스타일링 wrapper에 사용할 수 있다.
- semantic tag가 더 적절하면 semantic tag를 우선 사용한다.
- div 남용은 문서 구조 이해를 어렵게 만든다.
- React Component에서 wrapper로 자주 사용된다.

좋은 예:

```html
<section>
  <h2>Festival List</h2>
  <div class="festival-grid">
    <article class="festival-card"></article>
    <article class="festival-card"></article>
  </div>
</section>
```

나쁜 예:

```html
<div>
  <div>Festival List</div>
  <div>
    <div>Festival Card</div>
  </div>
</div>
```

---

### [실무]

`div`는 금지 대상이 아니라 의미 없는 컨테이너가 필요할 때 사용하는 도구다.

사용 기준:

```text
Meaning Exists → Semantic Tag
No Specific Meaning + Layout Needed → div
Inline Grouping Needed → span
```

검수 기준:

- 의미 있는 영역을 div로만 작성하지 않았는가?
- header, nav, main, section, article, footer가 더 적절하지 않은가?
- div가 스타일링 또는 layout 목적에 맞게 사용되었는가?
- div 중첩이 과도하지 않은가?

---

### [FAQ]

Q. div는 나쁜 태그야?
A. 아니다. 의미 없는 컨테이너가 필요할 때 사용하는 정상적인 태그다.

Q. 언제 div를 써야 해?
A. 의미 있는 semantic tag가 없고 레이아웃이나 스타일링 wrapper가 필요할 때 사용한다.

Q. div만 쓰면 왜 문제야?
A. 콘텐츠 구조와 역할이 드러나지 않아 접근성, SEO, 유지보수성이 떨어진다.

---

## 5.2 Span

### [개념]

`span`은 의미를 가지지 않는 inline generic container다.

문장 내부 일부 텍스트를 스타일링하거나 그룹화할 때 사용한다.

---

### [핵심]

`span` 핵심:

- 의미 없는 inline container다.
- 문장 내부 일부 텍스트 스타일링에 적합하다.
- block layout에는 div가 더 적합하다.
- 의미 있는 강조는 `strong`, `em` 등을 고려한다.
- span 남용은 콘텐츠 의미를 흐릴 수 있다.

예:

```html
<p>
  Festival status:
  <span class="status-badge">Open</span>
</p>
```

---

### [실무]

`span`은 시각적 스타일링에는 유용하지만 의미 전달에는 한계가 있다.

검수 기준:

- 의미 있는 강조를 span으로만 처리하지 않았는가?
- 상태 정보가 색상만으로 전달되지 않는가?
- inline grouping 목적에 맞게 사용되었는가?
- button, link 역할을 span으로 구현하지 않았는가?

금지 예:

```html
<span onclick="submitForm()">Submit</span>
```

권장 예:

```html
<button type="submit">Submit</button>
```

---

### [FAQ]

Q. span은 언제 써?
A. 문장 내부 일부 텍스트를 스타일링하거나 inline grouping이 필요할 때 사용한다.

Q. span으로 버튼을 만들어도 돼?
A. 권장하지 않는다. 동작 실행은 button을 사용한다.

Q. strong과 span 차이는 뭐야?
A. strong은 중요한 의미를 가진 강조이고 span은 의미 없는 inline container다.

---

# 6. Semantic HTML and Accessibility

## 6.1 Accessibility Connection

### [개념]

Semantic HTML은 Accessibility의 기본이다.

스크린 리더와 보조 기술은 Semantic HTML을 바탕으로 문서 구조와 요소 역할을 이해한다.

---

### [핵심]

Accessibility 연결 핵심:

- `header`, `nav`, `main`, `footer`는 Landmark 역할을 제공한다.
- heading 구조는 콘텐츠 탐색을 돕는다.
- `button`은 기본 keyboard interaction을 제공한다.
- `a`는 링크 역할과 이동 목적을 전달한다.
- `label`은 input의 이름을 제공한다.
- `alt`는 이미지 대체 텍스트를 제공한다.
- Semantic HTML을 먼저 사용하고 aria는 보완용으로 사용한다.

---

### [실무]

접근성 기본 검수 Checklist:

```md
- [ ] 페이지 핵심 콘텐츠가 main으로 감싸져 있는가?
- [ ] 주요 탐색 영역이 nav로 작성되었는가?
- [ ] heading level이 자연스러운가?
- [ ] 클릭 동작은 button으로 작성되었는가?
- [ ] 페이지 이동은 a 또는 Link로 작성되었는가?
- [ ] input과 label이 연결되어 있는가?
- [ ] 이미지에 적절한 alt가 있는가?
- [ ] div/span으로 interactive element를 만들지 않았는가?
```

---

### [FAQ]

Q. Semantic HTML이 접근성에 왜 중요해?
A. 보조 기술이 문서 구조와 요소 역할을 이해할 수 있게 해주기 때문이다.

Q. aria를 많이 쓰면 접근성이 좋아져?
A. 아니다. 먼저 Semantic HTML을 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. div에 role을 주면 semantic tag와 같아?
A. 일부 역할은 보완할 수 있지만 기본 semantic tag를 사용하는 것이 더 안정적이다.

---

# 7. Semantic HTML and SEO

## 7.1 SEO Basics

### [개념]

Semantic HTML은 검색 엔진이 페이지 구조와 콘텐츠 의미를 이해하는 데 도움을 준다.

SEO Basics에서 중요한 HTML 요소는 title, heading, main content, semantic structure, link text다.

---

### [핵심]

SEO 연결 핵심:

- `title`은 페이지 주제를 표현한다.
- `h1`은 페이지 핵심 제목이다.
- `h2`, `h3`는 콘텐츠 구조를 만든다.
- `main`은 핵심 콘텐츠 영역을 구분한다.
- `article`은 독립 콘텐츠 구조를 표현한다.
- `a`의 링크 텍스트는 목적지를 설명해야 한다.
- Semantic HTML은 검색 엔진의 콘텐츠 이해를 돕는다.

---

### [실무]

검색 친화 구조 예:

```html
<main>
  <h1>Seoul Festival Guide</h1>

  <section>
    <h2>Popular Festivals</h2>

    <article>
      <h3>Seoul Light Festival</h3>
      <p>Night light festival in Seoul.</p>
      <a href="/festivals/seoul-light">View Seoul Light Festival Detail</a>
    </article>
  </section>
</main>
```

검수 기준:

- 페이지 주제가 h1에 드러나는가?
- 구역별 heading이 명확한가?
- article 제목이 독립 콘텐츠를 설명하는가?
- 링크 텍스트가 목적지를 설명하는가?
- 의미 없는 “Click here” 링크를 남용하지 않았는가?

---

### [FAQ]

Q. Semantic HTML은 SEO에 도움이 돼?
A. 도움이 된다. 검색 엔진이 페이지 구조와 콘텐츠 의미를 이해하기 쉬워진다.

Q. h1은 SEO에 중요해?
A. 중요하다. 페이지 핵심 주제를 표현하는 제목으로 사용된다.

Q. 링크 텍스트도 SEO에 중요해?
A. 중요하다. 링크 목적지를 설명하는 텍스트가 검색 엔진과 사용자 모두에게 도움이 된다.

---

# 8. Semantic HTML in React

## 8.1 React JSX Semantic Markup

### [개념]

React JSX에서도 Semantic HTML 원칙은 유지된다.

JSX는 JavaScript 안에서 HTML과 유사한 구조를 작성하는 문법이지만, 최종 결과는 브라우저에 HTML DOM으로 렌더링된다.

---

### [핵심]

React Semantic Markup 핵심:

- Component 이름이 의미를 대체하지 않는다.
- 최종 렌더링 결과가 Semantic HTML이어야 한다.
- `Header` Component 내부는 `header` 태그를 사용할 수 있다.
- `Navigation` Component 내부는 `nav` 태그를 사용할 수 있다.
- `Page` Component의 핵심 영역은 `main`으로 감싸는 것이 좋다.
- `Card` Component가 독립 콘텐츠라면 `article`을 고려한다.
- 클릭 동작은 `button`, 페이지 이동은 `Link`를 사용한다.

---

### [실무]

나쁜 예:

```jsx
function FestivalPage() {
  return (
    <div>
      <div>Festival Search</div>
      <div>
        <div>Search Results</div>
      </div>
    </div>
  );
}
```

좋은 예:

```jsx
function FestivalPage() {
  return (
    <main>
      <h1>Festival Search</h1>

      <section aria-labelledby="results-title">
        <h2 id="results-title">Search Results</h2>
        <article>
          <h3>Seoul Light Festival</h3>
          <a href="/festivals/1">View Detail</a>
        </article>
      </section>
    </main>
  );
}
```

검수 기준:

- Component 이름만 의미 있고 실제 DOM은 div만 사용하지 않았는가?
- App Layout에 header, nav, main, footer가 적절히 사용되었는가?
- Page Component에 h1이 있는가?
- List Item/Card에 article이 적절한가?
- interactive element를 div/span으로 구현하지 않았는가?

---

### [FAQ]

Q. React Component 이름이 의미 있으면 div만 써도 돼?
A. 아니다. Component 이름은 개발자에게만 보이고 최종 DOM에는 Semantic HTML이 필요하다.

Q. JSX에서도 header, main, section을 써도 돼?
A. 당연히 가능하다. JSX에서도 일반 HTML semantic tag를 사용할 수 있다.

Q. React Card Component는 article로 만들어도 돼?
A. 카드가 독립 콘텐츠라면 article을 사용할 수 있다.

Q. React에서 페이지 이동은 button으로 해도 돼?
A. 권장하지 않는다. React Router의 Link 같은 링크 계열을 사용하는 것이 적절하다.

---

# 9. Comparison Rules

## 9.1 Div vs Semantic Tag

### [개념]

`div`는 의미 없는 generic container이고 Semantic Tag는 콘텐츠 역할과 구조를 표현하는 HTML 태그다.

---

### [핵심]

| 비교   | div                        | Semantic Tag                                            |
| ------ | -------------------------- | ------------------------------------------------------- |
| 의미   | 없음                       | 있음                                                    |
| 목적   | 레이아웃, 스타일링 wrapper | 구조와 역할 표현                                        |
| 접근성 | 직접 의미 제공 안 함       | 보조 기술이 역할 이해 가능                              |
| SEO    | 의미 전달 약함             | 콘텐츠 구조 이해에 도움                                 |
| 예시   | `div`                      | `header`, `nav`, `main`, `section`, `article`, `footer` |

---

### [실무]

선택 기준:

```text
페이지 상단 → header
주요 메뉴 → nav
핵심 본문 → main
주제별 구역 → section
독립 콘텐츠 → article
보조 콘텐츠 → aside
하단 정보 → footer
의미 없는 wrapper → div
```

---

### [FAQ]

Q. div와 semantic tag 차이는 뭐야?
A. div는 의미 없는 컨테이너이고 semantic tag는 콘텐츠의 역할과 구조를 표현한다.

Q. 언제 div를 선택해야 해?
A. 적절한 semantic tag가 없고 스타일링이나 레이아웃 wrapper가 필요할 때 선택한다.

---

## 9.2 Button vs Anchor

### [개념]

`button`은 동작 실행에 사용하고 `a`는 페이지 또는 URL 이동에 사용한다.

---

### [핵심]

| 비교             | button                | a                           |
| ---------------- | --------------------- | --------------------------- |
| 목적             | 동작 실행             | 페이지 / URL 이동           |
| 핵심 속성        | `type`, `disabled`    | `href`, `target`, `rel`     |
| 예시             | 제출, 삭제, 모달 열기 | 상세 페이지 이동, 외부 링크 |
| 키보드 기본 지원 | 있음                  | 있음                        |
| 잘못된 사용      | 페이지 이동 처리      | onClick 동작 처리 남용      |

---

### [실무]

선택 기준:

```text
Submit Form → button type="submit"
Open Modal → button type="button"
Like / Delete → button type="button"
Move Page → a or Link
External URL → a href
```

---

### [FAQ]

Q. button과 a는 어떻게 구분해?
A. 동작 실행은 button, 페이지 또는 URL 이동은 a를 사용한다.

Q. a 태그에 onClick만 넣어도 돼?
A. 권장하지 않는다. 이동 목적이 없으면 button을 사용하는 것이 적절하다.

---

## 9.3 Section vs Article

### [개념]

`section`은 주제별 구역이고 `article`은 독립적으로 의미를 가지는 콘텐츠다.

---

### [핵심]

| 비교     | section                   | article                  |
| -------- | ------------------------- | ------------------------ |
| 의미     | 주제별 구역               | 독립 콘텐츠              |
| 독립성   | 낮음                      | 높음                     |
| 예시     | 검색 필터 구역, 결과 구역 | 게시글, 리뷰, 댓글, 카드 |
| heading  | 권장                      | 권장                     |
| 재사용성 | 페이지 내부 구역          | 단독 배포 가능 콘텐츠    |

---

### [실무]

선택 기준:

```text
Search Filter Area → section
Search Result Area → section
Festival Card → article
Review Item → article
Comment Item → article
```

---

### [FAQ]

Q. section과 article 차이는 뭐야?
A. section은 페이지 안의 주제 구역이고 article은 독립적으로 재사용 가능한 콘텐츠다.

Q. 카드 목록은 section이야 article이야?
A. 목록 전체는 section, 각 카드가 독립 콘텐츠라면 article이 적합하다.

---

# 10. Common Mistakes

## 10.1 Semantic HTML Common Mistakes

### [개념]

Semantic HTML 실수는 접근성, SEO, 유지보수성, Component 구조 품질을 떨어뜨린다.

---

### [핵심]

자주 발생하는 실수:

- 모든 구조를 `div`로 작성
- `button`과 `a` 역할 혼동
- `section`에 heading 없음
- `article`을 단순 wrapper로 사용
- `nav`를 모든 링크 묶음에 남용
- `main`을 여러 개 사용
- heading level 건너뜀
- 클릭 가능한 `div` 또는 `span` 사용
- `href` 없는 `a` 태그 사용
- Component 이름만 의미 있고 실제 DOM은 div만 사용
- `aria`로 Semantic HTML 부족을 무리하게 보완
- 스타일링 목적으로 semantic tag 선택

---

### [실무]

Troubleshooting Flow:

```text
DOM Inspect
→ Semantic Tag Check
→ Heading Structure Check
→ Interactive Element Check
→ Accessibility Tree Check
→ React Component Markup Review
```

문제 예:

```text
문제: 키보드로 클릭 요소 접근 불가
원인: div onClick 사용
해결: button 사용
```

```text
문제: 페이지 구조가 스크린 리더에서 불명확함
원인: main, heading, section 구조 부족
해결: semantic layout과 heading 구조 추가
```

```text
문제: 링크 목적이 불명확함
원인: Click here 텍스트 남용
해결: 목적지가 드러나는 link text 작성
```

---

### [FAQ]

Q. Semantic HTML에서 가장 흔한 실수는 뭐야?
A. div 남용, button/a 혼동, heading 구조 오류, 클릭 가능한 div 사용이다.

Q. div onClick이 문제인 이유는?
A. 기본 keyboard interaction과 semantic role이 없어 접근성 문제가 생길 수 있다.

Q. aria로 다 해결하면 안 돼?
A. 안 된다. 먼저 적절한 HTML 태그를 사용하고 aria는 보완용으로 사용한다.

---

# 11. Best Practice

## 11.1 Semantic HTML Best Practice

### [개념]

Semantic HTML Best Practice는 콘텐츠 의미, 문서 구조, 접근성, SEO, React Component Markup 품질을 높이는 작성 기준이다.

---

### [핵심]

권장 기준:

- 페이지 상단은 `header`
- 주요 탐색은 `nav`
- 핵심 본문은 `main`
- 주제별 구역은 `section`
- 독립 콘텐츠는 `article`
- 보조 콘텐츠는 `aside`
- 하단 정보는 `footer`
- 동작 실행은 `button`
- 페이지 이동은 `a` 또는 Router Link
- heading level은 순서대로 작성
- `section`과 `article`에는 heading 제공
- 의미 없는 wrapper는 `div`
- inline grouping은 `span`
- Semantic HTML 우선, aria는 보완
- React Component의 최종 DOM 구조 검토

---

### [실무]

기본 Page Layout 예:

```html
<header>
  <h1>FestaPick</h1>
  <nav aria-label="Main Navigation">
    <a href="/festivals">Festivals</a>
    <a href="/calendar">Calendar</a>
  </nav>
</header>

<main>
  <section aria-labelledby="popular-title">
    <h2 id="popular-title">Popular Festivals</h2>

    <article>
      <h3>Seoul Light Festival</h3>
      <p>Night festival in Seoul.</p>
      <a href="/festivals/1">View Seoul Light Festival Detail</a>
    </article>
  </section>
</main>

<footer>
  <p>&copy; 2026 FestaPick</p>
</footer>
```

검수 Checklist:

```md
- [ ] `header`, `nav`, `main`, `footer` 구조가 명확한가?
- [ ] 페이지 핵심 제목이 `h1`인가?
- [ ] section과 article에 heading이 있는가?
- [ ] 독립 콘텐츠에 article을 사용했는가?
- [ ] 클릭 동작은 button인가?
- [ ] 페이지 이동은 a 또는 Link인가?
- [ ] div/span interactive element가 없는가?
- [ ] 링크 텍스트가 목적지를 설명하는가?
- [ ] aria를 semantic tag 대체 용도로 남용하지 않았는가?
- [ ] React Component 최종 DOM이 Semantic HTML인가?
```

---

### [FAQ]

Q. Semantic HTML Best Practice는 뭐야?
A. 콘텐츠 역할에 맞는 태그를 선택하고 heading, landmark, button, link 구조를 명확히 작성하는 것이다.

Q. Semantic HTML 검수에서 가장 먼저 볼 것은 뭐야?
A. header, nav, main, section, article, footer, heading, button/a 역할을 먼저 확인한다.

Q. React Component 검수에서 Semantic HTML은 어떻게 봐?
A. Component 이름이 아니라 최종 렌더링되는 DOM 태그가 의미 있는지 확인한다.

---

# Retrieval Queries

### [FAQ]

Q. Semantic HTML이 뭐야?
A. 태그의 의미를 기준으로 HTML 구조를 작성하는 방식이다.

Q. Semantic HTML은 왜 필요해?
A. 접근성, SEO, 유지보수성, 문서 구조 이해를 높이기 위해 필요하다.

Q. div만 쓰면 안 돼?
A. div도 사용할 수 있지만 의미 있는 영역은 header, nav, main, section, article, footer 같은 semantic tag를 우선 고려해야 한다.

Q. React를 써도 Semantic HTML이 필요해?
A. 필요하다. React Component도 최종적으로 HTML DOM으로 렌더링되기 때문이다.

Q. header 태그는 언제 써?
A. 페이지 또는 구역의 상단 머리말 영역에 사용한다.

Q. nav 태그는 언제 써?
A. 사이트 메뉴, 주요 페이지 이동, 탭 메뉴 같은 탐색 영역에 사용한다.

Q. main 태그는 언제 써?
A. 페이지의 핵심 본문 콘텐츠를 감쌀 때 사용한다.

Q. main은 여러 개 써도 돼?
A. 일반적인 페이지에서는 하나만 사용하는 것이 명확하다.

Q. section 태그는 언제 써?
A. 페이지 안에서 주제별 구역을 나눌 때 사용한다.

Q. section에는 heading이 필요해?
A. 일반적으로 필요하다. section의 주제를 heading으로 명확히 표현하는 것이 좋다.

Q. article 태그는 언제 써?
A. 게시글, 리뷰, 댓글, 카드처럼 독립적으로 의미 있는 콘텐츠에 사용한다.

Q. section과 article 차이는 뭐야?
A. section은 주제별 구역이고 article은 독립적으로 재사용 가능한 콘텐츠다.

Q. aside 태그는 언제 써?
A. 본문과 관련된 보조 콘텐츠, 사이드바, 추천 목록에 사용한다.

Q. footer 태그는 언제 써?
A. 페이지 또는 구역의 하단 정보, 저작권, 정책 링크, 작성자 정보에 사용한다.

Q. button 태그는 언제 써?
A. 클릭, 제출, 삭제, 좋아요, 모달 열기 같은 동작 실행에 사용한다.

Q. a 태그는 언제 써?
A. URL 이동, 페이지 이동, 문서 위치 이동에 사용한다.

Q. button과 a 태그 차이는?
A. button은 동작 실행, a는 페이지 또는 URL 이동에 사용한다.

Q. div onClick을 쓰면 안 돼?
A. 권장하지 않는다. button은 기본 키보드 접근성과 의미를 제공한다.

Q. href 없는 a 태그를 써도 돼?
A. 권장하지 않는다. 링크 의미가 사라지고 접근성에 좋지 않다.

Q. heading 구조는 왜 중요해?
A. 문서 구조, 접근성, SEO, 콘텐츠 탐색에 중요하다.

Q. h1 h2 h3는 어떻게 써?
A. h1은 페이지 핵심 제목, h2는 주요 구역, h3는 하위 구역처럼 계층 구조에 맞게 사용한다.

Q. heading level을 건너뛰어도 돼?
A. 권장하지 않는다. heading level은 순서대로 사용하는 것이 좋다.

Q. 글자 크기 때문에 h1을 써도 돼?
A. 안 된다. 글자 크기는 CSS로 조절하고 heading은 문서 구조 표현에 사용한다.

Q. div는 언제 써?
A. 의미 있는 semantic tag가 없고 레이아웃이나 스타일링 wrapper가 필요할 때 사용한다.

Q. span은 언제 써?
A. 문장 내부 일부 텍스트를 스타일링하거나 inline grouping이 필요할 때 사용한다.

Q. strong과 span 차이는 뭐야?
A. strong은 중요한 의미를 가진 강조이고 span은 의미 없는 inline container다.

Q. Semantic HTML과 Accessibility는 무슨 관계야?
A. Semantic HTML은 보조 기술이 문서 구조와 요소 역할을 이해할 수 있게 해준다.

Q. aria를 많이 쓰면 접근성이 좋아져?
A. 아니다. 먼저 Semantic HTML을 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. Semantic HTML은 SEO에 도움이 돼?
A. 도움이 된다. 검색 엔진이 페이지 구조와 콘텐츠 의미를 이해하기 쉬워진다.

Q. React Component 이름이 의미 있으면 div만 써도 돼?
A. 아니다. Component 이름은 개발자에게만 보이고 최종 DOM에는 Semantic HTML이 필요하다.

Q. React에서 페이지 이동은 button으로 해도 돼?
A. 권장하지 않는다. React Router Link 같은 링크 계열을 사용하는 것이 적절하다.

Q. Semantic HTML 검수 Checklist는 뭐야?
A. header, nav, main, section, article, footer, heading, button, a, div/span interactive 사용 여부를 확인한다.

Q. Semantic HTML의 최종 목적은 뭐야?
A. Frontend Agent가 의미 있는 화면 구조, 접근성 기본, SEO 기본, React JSX Markup을 안정적으로 생성하고 검토하게 만드는 것이다.
