# HTML CSS Foundation Part01 - Document Structure

---

# 1. HTML Document Structure

## 1.1 HTML Document Structure

### [개념]

HTML Document Structure는 웹 페이지의 기본 골격이다.

HTML 문서는 브라우저가 웹 페이지를 해석하기 위한 최소 구조를 가진다.

기본 구성:

- `<!doctype html>`
- `<html>`
- `<head>`
- `<meta>`
- `<title>`
- `<body>`

HTML Document Structure는 React, Vite, Next.js 같은 Frontend Framework를 사용해도 유지되는 기본 개념이다.

---

### [핵심]

HTML Document Structure 핵심:

- `<!doctype html>`은 HTML5 문서 선언이다.
- `<html>`은 전체 HTML 문서의 루트 요소다.
- `lang` 속성은 문서 언어를 지정한다.
- `<head>`는 브라우저와 검색 엔진이 참고하는 메타데이터 영역이다.
- `<meta charset="UTF-8">`은 문자 인코딩을 지정한다.
- `<meta name="viewport">`는 반응형 웹의 기본 설정이다.
- `<title>`은 브라우저 탭 제목과 SEO에 사용된다.
- `<body>`는 사용자에게 실제로 보이는 콘텐츠 영역이다.

---

### [실무]

2026 실무 기준에서 HTML Document Structure는 직접 매번 작성하지 않을 수 있다.

하지만 Frontend Agent는 아래 작업을 위해 HTML Document Structure를 이해해야 한다.

- React JSX 구조 설계
- Semantic HTML 구성
- SEO 기본 검토
- Accessibility 기본 검토
- Responsive Web Design 기본 설정 확인
- SPA / MPA 구조 이해
- 브라우저 렌더링 문제 분석

React 프로젝트에서도 `public/index.html`, `index.html`, `layout.tsx`, `app.html` 등에서 HTML Document Structure 개념이 사용된다.

예:

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Festival Page</title>
  </head>
  <body>
    <main>
      <h1>Festival List</h1>
    </main>
  </body>
</html>
```

---

### [FAQ]

Q. HTML Document Structure가 뭐야?
A. 브라우저가 웹 페이지를 해석하기 위한 HTML 문서의 기본 골격이다.

Q. HTML 문서의 기본 구성은 뭐야?
A. `doctype`, `html`, `head`, `meta`, `title`, `body`로 구성된다.

Q. React를 써도 HTML Document Structure를 알아야 해?
A. 알아야 한다. React도 결국 HTML 구조를 브라우저에 렌더링하기 때문이다.

Q. body에는 무엇을 작성해?
A. 사용자가 실제로 보는 콘텐츠를 작성한다.

Q. head에는 무엇을 작성해?
A. 문자 인코딩, viewport, title, meta 정보 같은 문서 메타데이터를 작성한다.

---

# 2. Doctype

## 2.1 Doctype Declaration

### [개념]

`<!doctype html>`은 현재 문서가 HTML5 문서임을 브라우저에 알려주는 선언이다.

Doctype은 HTML 태그가 아니다.

브라우저가 문서를 Standards Mode로 렌더링하도록 만드는 기준이다.

---

### [핵심]

Doctype 핵심:

- HTML 문서 최상단에 작성한다.
- HTML5 문서 선언은 `<!doctype html>`이다.
- 대소문자 구분은 엄격하지 않지만 소문자 작성이 일반적이다.
- Doctype이 없으면 브라우저가 Quirks Mode로 렌더링할 수 있다.
- Quirks Mode에서는 CSS Layout이 예상과 다르게 동작할 수 있다.

---

### [실무]

실무에서는 대부분 빌드 도구가 Doctype을 포함한 HTML 템플릿을 제공한다.

하지만 문서 검수 시 아래 항목을 확인해야 한다.

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <title>Page Title</title>
  </head>
  <body></body>
</html>
```

검수 기준:

- Doctype이 HTML 문서 최상단에 있는가?
- HTML5 Doctype을 사용하는가?
- 불필요한 XHTML Doctype을 사용하지 않는가?
- 브라우저 렌더링 모드 문제가 없는가?

---

### [FAQ]

Q. doctype은 HTML 태그야?
A. 아니다. HTML 문서 타입을 브라우저에 알려주는 선언이다.

Q. doctype은 꼭 필요해?
A. 필요하다. 브라우저가 Standards Mode로 문서를 렌더링하도록 돕는다.

Q. doctype이 없으면 어떻게 돼?
A. 브라우저가 Quirks Mode로 렌더링하여 CSS Layout이 예상과 다르게 동작할 수 있다.

Q. HTML5 doctype은 어떻게 작성해?
A. `<!doctype html>`로 작성한다.

---

# 3. HTML Root Element

## 3.1 html Element

### [개념]

`<html>` 요소는 HTML 문서 전체를 감싸는 루트 요소다.

모든 HTML 요소는 `<html>` 요소 내부에 위치한다.

일반적으로 `<html>` 요소에는 `lang` 속성을 작성한다.

---

### [핵심]

`html` 요소 핵심:

- HTML 문서의 최상위 루트 요소다.
- 내부에 `<head>`와 `<body>`를 포함한다.
- `lang` 속성으로 문서 언어를 지정한다.
- Accessibility와 SEO에 영향을 준다.
- 브라우저, 검색 엔진, 스크린 리더가 문서 언어를 이해하는 데 사용한다.

예:

```html
<html lang="ko">
  <head></head>
  <body></body>
</html>
```

---

### [실무]

한국어 페이지에서는 `lang="ko"`를 기본으로 사용한다.

영어 페이지에서는 `lang="en"`을 사용한다.

다국어 서비스에서는 페이지 또는 라우트별 언어 설정을 명확히 해야 한다.

React / Next.js에서도 최종 HTML에는 `html lang` 정보가 반영되어야 한다.

검수 기준:

- `<html>` 요소가 존재하는가?
- `lang` 속성이 있는가?
- 실제 콘텐츠 언어와 `lang` 값이 일치하는가?
- 다국어 페이지에서 언어 설정이 정확한가?

---

### [FAQ]

Q. html 태그는 무슨 역할이야?
A. HTML 문서 전체를 감싸는 루트 요소다.

Q. html lang 속성은 왜 필요해?
A. 스크린 리더, 검색 엔진, 브라우저가 문서 언어를 이해하는 데 필요하다.

Q. 한국어 페이지의 lang 값은 뭐야?
A. 일반적으로 `lang="ko"`를 사용한다.

Q. lang 속성을 생략해도 돼?
A. 동작은 할 수 있지만 접근성과 SEO 측면에서 권장하지 않는다.

---

# 4. Head Element

## 4.1 head Element

### [개념]

`<head>` 요소는 HTML 문서의 메타데이터를 작성하는 영역이다.

`head` 내부 정보는 대부분 화면에 직접 표시되지 않는다.

브라우저, 검색 엔진, SNS 미리보기, 접근성 도구가 참고한다.

---

### [핵심]

`head` 요소 핵심:

- 문서 메타데이터 영역이다.
- `<meta charset>`을 포함한다.
- `<meta name="viewport">`를 포함한다.
- `<title>`을 포함한다.
- SEO 관련 meta tag를 포함할 수 있다.
- CSS 파일 연결 정보를 포함할 수 있다.
- script 로딩 정보를 포함할 수 있다.

---

### [실무]

Frontend Agent는 `head` 영역을 화면 콘텐츠와 혼동하면 안 된다.

`head`는 사용자 화면 구조가 아니라 문서 설정 영역이다.

실무에서 주로 확인하는 항목:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Festival Search</title>
  <meta
    name="description"
    content="Search festival information by region and date."
  />
</head>
```

검수 기준:

- 문자 인코딩이 지정되어 있는가?
- viewport meta가 있는가?
- title이 의미 있게 작성되어 있는가?
- description이 필요한 페이지에 작성되어 있는가?
- 화면 콘텐츠를 head에 넣지 않았는가?

---

### [FAQ]

Q. head는 화면에 보이는 영역이야?
A. 아니다. head는 문서 메타데이터를 작성하는 영역이다.

Q. head에는 무엇을 넣어?
A. charset, viewport, title, description, stylesheet, script 같은 문서 설정 정보를 넣는다.

Q. 본문 콘텐츠를 head에 넣어도 돼?
A. 안 된다. 사용자에게 보이는 콘텐츠는 body에 작성한다.

Q. SEO 기본 정보는 어디에 작성해?
A. title과 meta description 같은 정보는 head에 작성한다.

---

# 5. Meta Element

## 5.1 Charset Meta

### [개념]

`<meta charset="UTF-8">`은 HTML 문서의 문자 인코딩을 지정한다.

UTF-8은 한글, 영어, 숫자, 특수문자, 이모지 등 다양한 문자를 표현할 수 있는 표준 인코딩이다.

---

### [핵심]

Charset Meta 핵심:

- 문자 깨짐 방지를 위해 필요하다.
- 보통 `head`의 상단에 작성한다.
- 현대 웹에서는 `UTF-8` 사용이 일반적이다.
- 한글 페이지에서는 특히 중요하다.
- 잘못된 인코딩은 텍스트 깨짐 문제를 만든다.

예:

```html
<meta charset="UTF-8" />
```

---

### [실무]

한국어 웹 페이지에서는 UTF-8을 기본으로 사용한다.

문자 깨짐 문제가 발생하면 아래 항목을 확인한다.

```text
HTML charset
→ Server Response Header
→ File Encoding
→ Database Encoding
→ API Response Encoding
```

Frontend Agent는 한글 깨짐 문제를 HTML만의 문제로 단정하면 안 된다.

---

### [FAQ]

Q. meta charset은 왜 필요해?
A. 브라우저가 문서를 올바른 문자 인코딩으로 해석하도록 하기 위해 필요하다.

Q. 한글이 깨질 때 무엇을 확인해?
A. HTML charset, 서버 응답 헤더, 파일 인코딩, DB 인코딩, API 응답 인코딩을 확인한다.

Q. UTF-8을 쓰면 돼?
A. 현대 웹에서는 일반적으로 UTF-8을 사용한다.

---

## 5.2 Viewport Meta

### [개념]

`<meta name="viewport">`는 모바일 브라우저에서 화면 크기와 확대 비율을 제어하는 설정이다.

Responsive Web Design의 기본 설정이다.

---

### [핵심]

Viewport Meta 핵심:

- 모바일 반응형 UI에 필수다.
- `width=device-width`는 뷰포트 너비를 기기 너비에 맞춘다.
- `initial-scale=1.0`은 초기 확대 비율을 1로 설정한다.
- viewport meta가 없으면 모바일 화면에서 레이아웃이 작거나 깨질 수 있다.

예:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

---

### [실무]

모바일 반응형 문제를 검수할 때 viewport meta를 먼저 확인한다.

검수 Flow:

```text
Mobile Layout Broken
→ viewport meta Check
→ CSS Media Query Check
→ Fixed Width Check
→ Image Width Check
→ Overflow Check
```

주의:

- 사용자 확대를 막는 설정은 접근성에 불리할 수 있다.
- `user-scalable=no`는 일반적으로 권장하지 않는다.
- Mobile First CSS와 함께 사용해야 한다.

---

### [FAQ]

Q. viewport meta는 왜 필요해?
A. 모바일 화면에서 반응형 레이아웃이 의도대로 동작하도록 하기 위해 필요하다.

Q. viewport meta가 없으면 어떻게 돼?
A. 모바일 브라우저가 페이지를 데스크톱 폭 기준으로 렌더링해 UI가 작거나 깨질 수 있다.

Q. user-scalable=no를 써도 돼?
A. 권장하지 않는다. 사용자의 확대 기능을 막아 접근성에 문제가 될 수 있다.

Q. 반응형 웹의 기본 viewport 설정은 뭐야?
A. `width=device-width, initial-scale=1.0`이다.

---

# 6. Title Element

## 6.1 title Element

### [개념]

`<title>` 요소는 HTML 문서의 제목을 지정한다.

브라우저 탭, 검색 결과, 북마크, 공유 미리보기 등에 사용된다.

---

### [핵심]

`title` 요소 핵심:

- `head` 내부에 작성한다.
- 페이지의 핵심 내용을 짧고 명확하게 표현한다.
- SEO 기본 요소다.
- 모든 페이지는 고유한 title을 가지는 것이 좋다.
- 너무 길거나 의미 없는 title은 피한다.

예:

```html
<title>Festival Search</title>
```

---

### [실무]

SPA에서도 라우트별 title 관리가 필요하다.

좋은 title:

```text
Festival Search - FestaPick
Festival Detail - FestaPick
Login - FestaPick
```

나쁜 title:

```text
React App
Untitled
Page
Home
```

검수 기준:

- 기본값 `React App`이 남아 있지 않은가?
- 페이지 목적이 title에 드러나는가?
- 서비스명이 포함되어 있는가?
- 페이지별 title이 구분되는가?

---

### [FAQ]

Q. title은 어디에 표시돼?
A. 브라우저 탭, 검색 결과, 북마크 등에 표시된다.

Q. title은 SEO에 중요해?
A. 중요하다. 검색 엔진이 페이지 주제를 이해하는 기본 정보다.

Q. React App 기본 title을 그대로 둬도 돼?
A. 권장하지 않는다. 서비스와 페이지 목적에 맞게 변경해야 한다.

Q. 페이지마다 title이 달라야 해?
A. 가능하면 페이지 목적에 맞게 고유한 title을 사용하는 것이 좋다.

---

# 7. Body Element

## 7.1 body Element

### [개념]

`<body>` 요소는 사용자에게 실제로 표시되는 콘텐츠를 작성하는 영역이다.

HTML 문서의 주요 화면 구조는 `body` 내부에 작성한다.

---

### [핵심]

`body` 요소 핵심:

- 사용자에게 보이는 콘텐츠 영역이다.
- heading, paragraph, image, link, button, form 등을 포함한다.
- Semantic HTML 구조는 body 내부에서 구성한다.
- React SPA에서는 root element가 body 안에 위치한다.
- body 내부 콘텐츠는 접근성 구조와 직접 연결된다.

예:

```html
<body>
  <main>
    <h1>Festival List</h1>
    <section>
      <h2>Popular Festival</h2>
    </section>
  </main>
</body>
```

---

### [실무]

React 프로젝트에서는 `body` 내부에 root element가 존재한다.

예:

```html
<body>
  <div id="root"></div>
</body>
```

하지만 React가 렌더링하는 최종 UI는 의미 있는 Semantic HTML 구조를 가져야 한다.

좋은 구조:

```html
<body>
  <div id="root">
    <header></header>
    <main></main>
    <footer></footer>
  </div>
</body>
```

나쁜 구조:

```html
<body>
  <div>
    <div>
      <div>
        <div>Content</div>
      </div>
    </div>
  </div>
</body>
```

---

### [FAQ]

Q. body에는 무엇을 작성해?
A. 사용자에게 실제로 보이는 화면 콘텐츠를 작성한다.

Q. React의 root div도 body 안에 있어?
A. 맞다. React SPA는 보통 body 안의 root element에 UI를 렌더링한다.

Q. body 안에 semantic tag를 써야 해?
A. 권장된다. header, main, section, footer 같은 의미 태그를 사용하면 구조와 접근성이 좋아진다.

Q. body와 head 차이는 뭐야?
A. head는 문서 설정 정보, body는 사용자에게 보이는 콘텐츠 영역이다.

---

# 8. Root Element in Frontend Framework

## 8.1 Root Element

### [개념]

Root Element는 Frontend Framework가 UI를 렌더링하는 기준 DOM 요소다.

React CRA, Vite React 프로젝트에서는 보통 `<div id="root"></div>`를 사용한다.

---

### [핵심]

Root Element 핵심:

- React App이 마운트되는 DOM 요소다.
- 보통 `body` 내부에 위치한다.
- `id="root"`가 일반적이다.
- 실제 UI 구조는 React Component가 root 내부에 렌더링한다.
- root element 자체는 Semantic HTML을 대체하지 않는다.

예:

```html
<body>
  <div id="root"></div>
</body>
```

---

### [실무]

Root Element는 앱 진입점과 연결된다.

React 예:

```jsx
import { createRoot } from "react-dom/client";
import App from "./App";

createRoot(document.getElementById("root")).render(<App />);
```

실무 검수 기준:

- HTML에 root element가 존재하는가?
- JavaScript 진입점에서 동일한 id를 찾는가?
- root id 오타가 없는가?
- root 내부에 렌더링되는 App 구조가 Semantic HTML을 사용하는가?

---

### [FAQ]

Q. root element가 뭐야?
A. React 같은 Frontend Framework가 UI를 렌더링하는 기준 DOM 요소다.

Q. root element는 꼭 div여야 해?
A. 꼭 div일 필요는 없지만 React 프로젝트에서는 일반적으로 `<div id="root"></div>`를 사용한다.

Q. root element가 Semantic HTML을 대신해?
A. 아니다. 실제 화면 구조는 App 내부에서 semantic tag로 구성해야 한다.

Q. root id가 다르면 어떻게 돼?
A. JavaScript에서 해당 element를 찾지 못해 앱이 렌더링되지 않을 수 있다.

---

# 9. HTML Document Structure Flow

## 9.1 Browser Parsing Flow

### [개념]

Browser Parsing Flow는 브라우저가 HTML 문서를 읽고 화면을 구성하는 과정이다.

HTML Document Structure는 브라우저 파싱 흐름의 기준이 된다.

---

### [핵심]

기본 Flow:

```text
HTML Document Request
→ Doctype Check
→ html Element Parse
→ head Metadata Parse
→ CSS / Script Resource Load
→ body Content Parse
→ DOM Tree Build
→ Render Tree Build
→ Layout
→ Paint
```

---

### [실무]

Frontend Agent는 HTML 구조 문제를 UI 문제와 연결해서 분석해야 한다.

예:

```text
문제: 모바일 화면이 작게 보임
원인: viewport meta 누락
해결: meta viewport 추가
```

```text
문제: 앱이 렌더링되지 않음
원인: root element id 불일치
해결: index.html root id와 React entry id 일치
```

```text
문제: 한글이 깨짐
원인: charset 또는 서버 인코딩 문제
해결: UTF-8 설정 확인
```

---

### [FAQ]

Q. 브라우저는 HTML을 어떻게 화면으로 만들어?
A. HTML을 파싱해 DOM을 만들고 CSS와 결합해 Render Tree, Layout, Paint 과정을 거쳐 화면을 만든다.

Q. HTML 구조 오류가 CSS 문제처럼 보일 수 있어?
A. 그렇다. viewport, root element, semantic structure 문제는 화면 깨짐이나 렌더링 문제로 나타날 수 있다.

Q. root element id 오류는 어떤 문제를 만들어?
A. React App이 마운트되지 않아 화면이 비어 보일 수 있다.

---

# 10. Common Mistakes

## 10.1 HTML Document Structure Mistakes

### [개념]

HTML Document Structure에서 발생하는 실수는 렌더링, 반응형, 접근성, SEO 문제로 이어질 수 있다.

---

### [핵심]

자주 발생하는 실수:

- Doctype 누락
- `html lang` 누락
- `meta charset` 누락
- `meta viewport` 누락
- 기본 title 방치
- body에 있어야 할 콘텐츠를 head에 작성
- root element id 불일치
- Semantic HTML 없이 div만 사용
- title과 페이지 내용 불일치
- 사용자 확대를 막는 viewport 설정
- 한글 페이지에서 잘못된 charset 사용

---

### [실무]

Troubleshooting 기준:

```text
문제: 모바일 반응형이 이상함
확인: meta viewport 존재 여부
```

```text
문제: 한글이 깨짐
확인: meta charset UTF-8 여부
```

```text
문제: React 화면이 안 뜸
확인: root element id와 React entry id 일치 여부
```

```text
문제: 접근성 점수가 낮음
확인: html lang, heading structure, semantic tag 여부
```

---

### [FAQ]

Q. HTML 기본 구조에서 가장 흔한 실수는 뭐야?
A. viewport 누락, lang 누락, 기본 title 방치, root id 불일치가 흔하다.

Q. 모바일 화면이 이상하면 HTML에서 무엇을 먼저 봐?
A. `meta name="viewport"`가 있는지 먼저 확인한다.

Q. React 화면이 비어 있으면 무엇을 확인해?
A. root element id와 React entry 파일의 `getElementById` 값이 일치하는지 확인한다.

Q. 접근성 기본 검수에서 HTML 구조는 왜 중요해?
A. lang, heading, semantic tag가 스크린 리더와 문서 구조 이해에 직접 영향을 주기 때문이다.

---

# 11. Best Practice

## 11.1 HTML Document Structure Best Practice

### [개념]

HTML Document Structure Best Practice는 브라우저 렌더링, 접근성, SEO, 반응형 UI의 기본 안정성을 높이는 작성 기준이다.

---

### [핵심]

권장 기준:

- HTML5 Doctype 사용
- `html lang` 지정
- `meta charset="UTF-8"` 작성
- `meta viewport` 작성
- 의미 있는 `title` 작성
- 사용자 화면 콘텐츠는 `body`에 작성
- React root element id 일치
- Semantic HTML 기반 body 구조 구성
- 기본 title 방치 금지
- 사용자 확대 차단 금지

---

### [실무]

기본 템플릿:

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Festival Search - FestaPick</title>
    <meta name="description" content="지역과 날짜로 축제 정보를 검색합니다." />
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

React App 내부 권장 구조:

```jsx
function App() {
  return (
    <>
      <header>Header</header>
      <main>
        <h1>Festival Search</h1>
      </main>
      <footer>Footer</footer>
    </>
  );
}
```

검수 Checklist:

```md
- [ ] `<!doctype html>`이 있는가?
- [ ] `<html lang="ko">`가 있는가?
- [ ] `<meta charset="UTF-8">`이 있는가?
- [ ] `<meta name="viewport">`가 있는가?
- [ ] `<title>`이 의미 있게 작성되었는가?
- [ ] `body` 내부에 root element가 있는가?
- [ ] React entry id와 root id가 일치하는가?
- [ ] App 내부 구조가 Semantic HTML을 사용하는가?
```

---

### [FAQ]

Q. HTML Document Structure의 Best Practice는 뭐야?
A. Doctype, lang, charset, viewport, title, body, root element, semantic structure를 명확히 작성하는 것이다.

Q. React 프로젝트의 index.html에서 꼭 확인할 것은 뭐야?
A. viewport, title, root element id, lang, charset을 확인한다.

Q. App 컴포넌트 안에서도 HTML 구조를 신경 써야 해?
A. 그렇다. React Component도 최종적으로 HTML로 렌더링되므로 Semantic HTML 구조가 중요하다.

---

# Retrieval Queries

### [FAQ]

Q. HTML Document Structure가 뭐야?
A. 브라우저가 웹 페이지를 해석하기 위한 HTML 문서의 기본 골격이다.

Q. HTML 기본 구조는 뭐야?
A. `doctype`, `html`, `head`, `meta`, `title`, `body`로 구성된다.

Q. doctype은 왜 필요해?
A. 브라우저가 HTML5 문서를 Standards Mode로 렌더링하도록 하기 위해 필요하다.

Q. HTML5 doctype은 어떻게 작성해?
A. `<!doctype html>`로 작성한다.

Q. html 태그는 무슨 역할이야?
A. HTML 문서 전체를 감싸는 루트 요소다.

Q. html lang 속성은 왜 필요해?
A. 스크린 리더, 검색 엔진, 브라우저가 문서 언어를 이해하는 데 필요하다.

Q. 한국어 페이지의 lang 값은 뭐야?
A. 일반적으로 `lang="ko"`를 사용한다.

Q. head 태그는 뭐야?
A. 문서의 메타데이터를 작성하는 영역이다.

Q. head에는 무엇을 넣어?
A. charset, viewport, title, description, stylesheet, script 같은 문서 설정 정보를 넣는다.

Q. body 태그는 뭐야?
A. 사용자에게 실제로 표시되는 콘텐츠를 작성하는 영역이다.

Q. head와 body 차이는 뭐야?
A. head는 문서 설정 정보 영역이고 body는 사용자에게 보이는 콘텐츠 영역이다.

Q. meta charset은 왜 필요해?
A. 브라우저가 문자를 올바르게 해석하도록 하기 위해 필요하다.

Q. 한글이 깨질 때 무엇을 확인해?
A. charset, 서버 응답 헤더, 파일 인코딩, DB 인코딩, API 응답 인코딩을 확인한다.

Q. viewport meta는 왜 필요해?
A. 모바일 화면에서 반응형 레이아웃이 의도대로 동작하도록 하기 위해 필요하다.

Q. viewport meta 기본 설정은 뭐야?
A. `width=device-width, initial-scale=1.0`이다.

Q. viewport meta가 없으면 어떻게 돼?
A. 모바일 브라우저에서 페이지가 데스크톱 폭 기준으로 렌더링되어 UI가 작거나 깨질 수 있다.

Q. user-scalable=no를 써도 돼?
A. 권장하지 않는다. 사용자의 확대 기능을 막아 접근성 문제가 생길 수 있다.

Q. title 태그는 뭐야?
A. 브라우저 탭, 검색 결과, 북마크 등에 표시되는 문서 제목이다.

Q. title은 SEO에 중요해?
A. 중요하다. 검색 엔진이 페이지 주제를 이해하는 기본 정보다.

Q. React App 기본 title을 그대로 둬도 돼?
A. 권장하지 않는다. 서비스와 페이지 목적에 맞게 변경해야 한다.

Q. React root element가 뭐야?
A. React App이 마운트되는 기준 DOM 요소다.

Q. React root element는 어디에 있어?
A. 보통 `body` 내부에 `<div id="root"></div>` 형태로 위치한다.

Q. root element id가 다르면 어떻게 돼?
A. JavaScript에서 element를 찾지 못해 React App이 렌더링되지 않을 수 있다.

Q. React를 써도 HTML Document Structure를 알아야 해?
A. 알아야 한다. React도 최종적으로 HTML 구조를 브라우저에 렌더링하기 때문이다.

Q. 모바일 화면이 이상할 때 HTML에서 먼저 확인할 것은 뭐야?
A. `meta name="viewport"`가 있는지 먼저 확인한다.

Q. React 화면이 비어 있을 때 먼저 확인할 것은 뭐야?
A. root element id와 React entry 파일의 `getElementById` 값이 일치하는지 확인한다.

Q. HTML Document Structure 검수 Checklist는 뭐야?
A. Doctype, lang, charset, viewport, title, body, root element, Semantic HTML 구조를 확인한다.

Q. HTML Document Structure의 최종 목적은 뭐야?
A. 브라우저 렌더링, 반응형 UI, 접근성, SEO, Frontend Framework 렌더링의 기본 안정성을 확보하는 것이다.
