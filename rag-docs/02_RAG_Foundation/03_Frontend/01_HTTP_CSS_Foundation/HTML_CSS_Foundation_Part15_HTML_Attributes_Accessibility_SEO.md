# HTML CSS Foundation Part15 - HTML Attributes Accessibility SEO

---

# 1. HTML Attributes

## 1.1 HTML Attribute Concept

### [개념]

HTML Attribute는 HTML 요소에 추가 정보를 제공하는 이름-값 구조다.

Attribute는 요소의 동작, 접근성, 식별자, 링크 대상, 이미지 대체 텍스트, Form 연결, 상태 표현, SEO 정보에 영향을 준다.

기본 예:

```html
<a href="/festivals" class="nav-link" aria-current="page"> Festivals </a>

<img src="/images/festival.jpg" alt="서울 야간 축제 조명" />
```

---

### [핵심]

HTML Attribute 핵심:

- attribute는 HTML 요소의 의미와 동작을 보완한다.
- `id`는 문서 내 고유 식별자다.
- `class`는 styling과 JavaScript hook에 자주 사용된다.
- `href`는 link destination을 지정한다.
- `src`는 media source를 지정한다.
- `alt`는 image alternative text를 제공한다.
- `type`은 button/input 동작을 명확히 한다.
- `name`은 form data 전송에 사용된다.
- `for`와 `id`는 label과 input 연결에 사용된다.
- `aria-*`는 접근성 상태와 이름을 보완한다.
- attribute 값은 의미와 실제 상태가 일치해야 한다.

---

### [실무]

2026 실무 기준에서 HTML Attribute는 Accessibility, SEO, Form UX, Component State와 직접 연결된다.

Frontend Agent는 HTML 생성 시 아래 attribute를 우선 검토해야 한다.

- `lang`
- `charset`
- `viewport`
- `title`
- `id`
- `class`
- `href`
- `src`
- `alt`
- `type`
- `name`
- `for`
- `disabled`
- `readonly`
- `required`
- `autocomplete`
- `aria-label`
- `aria-labelledby`
- `aria-describedby`
- `aria-expanded`
- `aria-current`
- `aria-invalid`
- `hidden`

Attribute 작성 Flow:

```text
요소 역할 확인
→ 필수 attribute 확인
→ 접근성 attribute 확인
→ Form 연결 확인
→ 상태 attribute 확인
→ SEO 관련 attribute 확인
→ 실제 UI 상태와 동기화 확인
```

---

### [FAQ]

Q. HTML Attribute가 뭐야?
A. HTML 요소에 추가 정보를 제공해 의미, 동작, 접근성, SEO를 보완하는 이름-값 구조다.

Q. Attribute는 왜 중요해?
A. 링크 이동, 이미지 설명, Form 연결, 접근성 상태, 검색 노출 정보에 영향을 주기 때문이다.

Q. 모든 요소에 attribute를 많이 넣으면 좋아?
A. 아니다. 요소의 의미와 동작에 필요한 attribute를 정확히 넣는 것이 중요하다.

Q. Attribute 검수에서 가장 먼저 볼 것은?
A. 요소 역할에 필요한 필수 attribute와 접근성 관련 attribute가 실제 상태와 일치하는지 확인한다.

---

# 2. Global Attributes

## 2.1 id

### [개념]

`id`는 HTML 문서 안에서 특정 요소를 고유하게 식별하는 attribute다.

`id`는 label 연결, aria 연결, fragment link, JavaScript 대상 지정에 사용된다.

예:

```html
<label for="email">Email</label> <input id="email" name="email" type="email" />
```

---

### [핵심]

`id` 핵심:

- 문서 내에서 고유해야 한다.
- 같은 `id`를 여러 요소에 중복 사용하면 안 된다.
- `label for`와 input id 연결에 사용된다.
- `aria-labelledby`, `aria-describedby` 연결에 사용된다.
- URL fragment link의 대상이 될 수 있다.
- CSS styling 용도로 id selector를 남용하지 않는다.
- React 반복 rendering에서 id 중복을 주의한다.

---

### [실무]

ARIA 연결 예:

```html
<h2 id="modal-title">Delete Festival</h2>

<section role="dialog" aria-modal="true" aria-labelledby="modal-title">
  Modal content
</section>
```

Fragment Link 예:

```html
<a href="#main-content">Skip to main content</a>

<main id="main-content">Main content</main>
```

검수 기준:

- id가 문서 내에서 고유한가?
- label for와 input id가 일치하는가?
- aria-labelledby와 aria-describedby가 실제 존재하는 id를 참조하는가?
- id selector로 styling을 남용하지 않았는가?
- 반복 component에서 id 충돌이 없는가?

---

### [FAQ]

Q. id attribute는 뭐야?
A. 문서 안에서 특정 요소를 고유하게 식별하는 attribute다.

Q. id는 중복되면 안 돼?
A. 맞다. 하나의 문서 안에서 id는 고유해야 한다.

Q. id는 언제 꼭 필요해?
A. label/input 연결, aria-labelledby, aria-describedby, fragment link 대상에 필요하다.

Q. CSS에서 id selector를 써도 돼?
A. 가능하지만 specificity가 높아 유지보수가 어려우므로 styling에는 class를 우선 사용한다.

---

## 2.2 class

### [개념]

`class`는 하나 이상의 class name을 요소에 부여하는 attribute다.

CSS styling, JavaScript hook, component variant, state styling에 자주 사용된다.

예:

```html
<button class="button button-primary" type="button">Save</button>
```

---

### [핵심]

`class` 핵심:

- 여러 class를 공백으로 구분해 사용할 수 있다.
- CSS selector로 가장 일반적으로 사용된다.
- component root class와 variant class를 구분할 수 있다.
- class name은 역할과 의미 중심으로 작성한다.
- 색상, 위치, 크기 기반 이름은 피한다.
- React에서는 `className`으로 작성한다.
- class 오타는 style 미적용의 주요 원인이다.

---

### [실무]

좋은 예:

```html
<article class="festival-card festival-card-featured">
  <h2 class="festival-card-title">Seoul Light Festival</h2>
</article>
```

나쁜 예:

```html
<div class="blue-box big left">Content</div>
```

검수 기준:

- class name이 component 역할을 표현하는가?
- variant class와 base class가 구분되는가?
- className과 CSS selector가 일치하는가?
- 색상이나 위치에 종속된 이름이 아닌가?
- 너무 많은 utility class로 의미가 흐려지지 않는가?

---

### [FAQ]

Q. class attribute는 뭐야?
A. CSS styling과 component 구분을 위해 요소에 class name을 부여하는 attribute다.

Q. class는 여러 개 쓸 수 있어?
A. 가능하다. 공백으로 구분해 여러 class를 사용할 수 있다.

Q. class 이름은 어떻게 짓는 게 좋아?
A. 색상이나 위치보다 component 역할과 의미 중심으로 짓는 것이 좋다.

Q. React에서는 class를 어떻게 써?
A. JSX에서는 `class`가 아니라 `className`을 사용한다.

---

## 2.3 title

### [개념]

`title` attribute는 요소에 추가 설명을 제공할 수 있는 attribute다.

브라우저에서는 마우스 hover 시 tooltip처럼 표시될 수 있지만 접근성과 모바일 사용성 측면에서 한계가 있다.

---

### [핵심]

`title` 핵심:

- 보조 설명으로 사용할 수 있다.
- 중요한 정보를 `title`에만 의존하면 안 된다.
- 모바일 touch 환경에서는 title tooltip 접근이 어렵다.
- keyboard와 screen reader에서 일관되게 전달되지 않을 수 있다.
- link나 button의 accessible name 대체로 남용하지 않는다.
- 필요한 정보는 visible text 또는 aria-label/description으로 제공한다.

---

### [실무]

나쁜 예:

```html
<button type="button" title="Delete">🗑</button>
```

좋은 예:

```html
<button type="button" aria-label="Delete festival">
  <span aria-hidden="true">🗑</span>
</button>
```

검수 기준:

- 중요한 정보가 title에만 들어 있지 않은가?
- 모바일에서도 접근 가능한 설명인가?
- icon-only button에 title만 사용하지 않았는가?
- visible label 또는 aria-label이 더 적절하지 않은가?

---

### [FAQ]

Q. title attribute는 뭐야?
A. 요소에 보조 설명을 제공할 수 있는 HTML attribute다.

Q. title만으로 버튼 이름을 제공해도 돼?
A. 권장하지 않는다. icon-only button에는 aria-label이나 숨김 텍스트가 더 안정적이다.

Q. title은 모바일에서 안전해?
A. 아니다. touch 환경에서는 hover tooltip처럼 접근하기 어렵다.

---

## 2.4 data Attribute

### [개념]

`data-*` attribute는 HTML 요소에 사용자 정의 데이터를 저장할 수 있는 attribute다.

JavaScript 상태 hook, 테스트 selector, 간단한 UI 상태 표현에 사용할 수 있다.

예:

```html
<button data-variant="primary" data-state="open" type="button">Menu</button>
```

---

### [핵심]

`data-*` 핵심:

- `data-`로 시작한다.
- 사용자 정의 데이터를 HTML에 저장한다.
- JavaScript에서 `dataset`으로 접근할 수 있다.
- CSS selector로도 사용할 수 있다.
- 접근성 의미를 대신하지 않는다.
- 상태 의미는 aria attribute와 함께 관리해야 한다.
- 민감한 정보를 data attribute에 넣지 않는다.

---

### [실무]

Theme 예:

```html
<html lang="ko" data-theme="dark"></html>
```

CSS 예:

```css
[data-theme="dark"] {
  --color-background: #111827;
  --color-text: #f9fafb;
}
```

상태 예:

```html
<button type="button" aria-expanded="true" data-state="open">Menu</button>
```

검수 기준:

- data attribute가 접근성 정보를 대체하지 않는가?
- UI 상태와 aria 상태가 동기화되는가?
- 민감한 데이터가 노출되지 않는가?
- styling hook으로 사용할 때 naming이 명확한가?
- 테스트용 selector와 UI state selector가 혼동되지 않는가?

---

### [FAQ]

Q. data-\* attribute는 뭐야?
A. HTML 요소에 사용자 정의 데이터를 저장하는 attribute다.

Q. data-state만 있으면 접근성 상태가 전달돼?
A. 아니다. 접근성 상태는 aria-expanded, aria-selected 같은 ARIA attribute가 필요하다.

Q. data attribute에 민감한 정보를 넣어도 돼?
A. 안 된다. HTML에 노출되므로 민감 정보는 넣지 않는다.

---

# 3. Link Attributes

## 3.1 href

### [개념]

`href`는 `a` 요소의 이동 대상 URL을 지정하는 attribute다.

`a` 요소는 `href`가 있을 때 실제 link 의미를 가진다.

예:

```html
<a href="/festivals">Festivals</a>
```

---

### [핵심]

`href` 핵심:

- link destination을 지정한다.
- 내부 경로, 외부 URL, fragment id를 사용할 수 있다.
- `href`가 없는 `a`는 link 역할이 불명확하다.
- 이동 목적이면 button이 아니라 `a href`를 사용한다.
- 새 창 링크는 `target="_blank"`와 보안 attribute를 함께 고려한다.
- fragment link는 해당 id가 실제 존재해야 한다.

---

### [실무]

내부 링크:

```html
<a href="/festivals/1">View festival detail</a>
```

Fragment 링크:

```html
<a href="#reviews">Skip to reviews</a>

<section id="reviews">Reviews</section>
```

외부 링크:

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">
  External site
</a>
```

검수 기준:

- 이동 목적에 `a href`를 사용했는가?
- 동작 실행에 `a href="#"`를 남용하지 않았는가?
- fragment target id가 존재하는가?
- 외부 새 창 링크에 rel 보안 값이 있는가?
- 링크 텍스트가 목적을 설명하는가?

---

### [FAQ]

Q. href attribute는 뭐야?
A. a 요소가 이동할 URL 또는 fragment target을 지정하는 attribute다.

Q. href 없는 a 태그는 link야?
A. 실제 link 의미가 불명확하므로 이동 목적이라면 href가 필요하다.

Q. 버튼처럼 동작하는 a href="#"는 괜찮아?
A. 권장하지 않는다. 동작 실행은 button을 사용한다.

Q. 새 창 링크에는 무엇이 필요해?
A. `target="_blank"`와 함께 `rel="noopener noreferrer"`를 사용하는 것이 좋다.

---

## 3.2 target and rel

### [개념]

`target`은 링크를 어디에서 열지 지정하고, `rel`은 현재 문서와 링크 대상 문서의 관계를 설명한다.

새 창 링크에서는 보안과 개인정보 보호를 위해 `rel`을 함께 사용하는 것이 중요하다.

---

### [핵심]

`target` 핵심:

- `_self`는 현재 browsing context에서 연다.
- `_blank`는 새 탭 또는 새 창에서 연다.
- 새 창은 사용자 흐름을 방해할 수 있다.

`rel` 핵심:

- `noopener`는 새 페이지가 원래 페이지에 접근하지 못하게 한다.
- `noreferrer`는 referrer 정보를 보내지 않게 할 수 있다.
- `nofollow`는 검색 엔진에 링크 관계를 알릴 때 사용할 수 있다.
- 외부 새 창 링크는 `noopener noreferrer`를 고려한다.

---

### [실무]

외부 링크 예:

```html
<a href="https://external.example" target="_blank" rel="noopener noreferrer">
  Open external resource
</a>
```

검수 기준:

- 새 창이 정말 필요한가?
- `target="_blank"`에 rel 보안 값이 있는가?
- 링크 텍스트가 외부 이동을 충분히 설명하는가?
- 사용자가 새 창 열림을 예측할 수 있는가?

---

### [FAQ]

Q. target="\_blank"는 뭐야?
A. 링크를 새 탭 또는 새 창에서 열도록 지정하는 값이다.

Q. noopener는 왜 필요해?
A. 새로 열린 페이지가 원래 페이지를 제어하지 못하게 하기 위해 필요하다.

Q. noreferrer는 뭐야?
A. 링크 대상에 referrer 정보를 보내지 않도록 하는 rel 값이다.

Q. 모든 링크를 새 창으로 열면 좋아?
A. 아니다. 사용자 흐름을 방해할 수 있으므로 필요한 경우에만 사용한다.

---

# 4. Image Attributes

## 4.1 src and alt

### [개념]

`src`는 이미지 파일 경로를 지정하고, `alt`는 이미지의 대체 텍스트를 제공한다.

`alt`는 이미지 접근성과 SEO에 중요한 attribute다.

예:

```html
<img src="/images/festival.jpg" alt="서울 야간 축제 조명 터널" />
```

---

### [핵심]

`src` 핵심:

- 이미지 파일 경로를 지정한다.
- 잘못된 경로는 broken image를 만든다.
- 상대 경로와 절대 경로를 구분해야 한다.

`alt` 핵심:

- 이미지가 전달하는 의미를 텍스트로 제공한다.
- 의미 있는 이미지에는 구체적인 alt가 필요하다.
- 장식 이미지는 `alt=""`를 사용할 수 있다.
- alt를 생략하면 screen reader 경험이 나빠질 수 있다.
- “image of”, “picture of” 같은 불필요한 표현은 보통 피한다.
- SEO에도 이미지 의미 파악에 도움을 준다.

---

### [실무]

의미 있는 이미지:

```html
<img
  src="/images/seoul-light-festival.jpg"
  alt="서울 빛 축제의 야간 조명 전시"
/>
```

장식 이미지:

```html
<img src="/images/decorative-line.png" alt="" />
```

잘못된 예:

```html
<img src="/images/festival.jpg" alt="image" />
```

검수 기준:

- 이미지가 의미 있는 콘텐츠인가?
- 의미 있는 이미지에 구체적인 alt가 있는가?
- 장식 이미지는 빈 alt로 보조 기술에서 제외되는가?
- alt가 파일명이나 “image”처럼 무의미하지 않은가?
- 이미지 경로가 올바른가?

---

### [FAQ]

Q. alt attribute는 뭐야?
A. 이미지가 보이지 않거나 screen reader가 읽을 때 사용할 대체 텍스트다.

Q. 모든 이미지에 alt가 필요해?
A. img 요소에는 alt가 있어야 한다. 장식 이미지는 `alt=""`를 사용할 수 있다.

Q. 장식 이미지는 alt를 어떻게 해?
A. 빈 alt인 `alt=""`를 사용해 보조 기술이 무시하게 할 수 있다.

Q. alt에는 뭐라고 써야 해?
A. 이미지가 전달하는 의미나 정보를 짧고 구체적으로 작성한다.

---

## 4.2 width height loading decoding

### [개념]

`width`, `height`, `loading`, `decoding`은 이미지의 layout 안정성, 성능, 렌더링 방식에 영향을 주는 attribute다.

---

### [핵심]

`width` / `height` 핵심:

- 이미지의 intrinsic size를 브라우저에 알려준다.
- layout shift를 줄이는 데 도움된다.
- CSS로 responsive 처리해도 HTML width/height를 함께 줄 수 있다.

`loading` 핵심:

- `loading="lazy"`는 이미지 lazy loading을 요청한다.
- 초기 화면 아래 이미지에 적합하다.
- 중요한 hero image에는 lazy를 신중히 사용한다.

`decoding` 핵심:

- 이미지 decoding 방식을 힌트로 제공한다.
- `async`를 사용할 수 있다.
- 성능 최적화 힌트이며 필수는 아니다.

---

### [실무]

예:

```html
<img
  src="/images/festival-card.jpg"
  alt="부산 바다 축제 무대"
  width="640"
  height="360"
  loading="lazy"
  decoding="async"
/>
```

CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

검수 기준:

- 이미지 width와 height가 실제 비율과 맞는가?
- lazy loading이 중요한 LCP 이미지에 잘못 적용되지 않았는가?
- 카드 목록 이미지에는 lazy loading이 적절한가?
- CSS responsive image 규칙이 함께 있는가?

---

### [FAQ]

Q. img width height attribute는 왜 써?
A. 브라우저가 이미지 공간을 미리 계산해 layout shift를 줄이는 데 도움이 된다.

Q. loading lazy는 언제 써?
A. 초기 화면 아래에 있는 이미지처럼 즉시 필요하지 않은 이미지에 사용한다.

Q. hero image에도 loading lazy를 써도 돼?
A. 주의해야 한다. 중요한 첫 화면 이미지는 lazy loading이 오히려 느리게 보이게 할 수 있다.

Q. decoding async는 필수야?
A. 필수는 아니지만 이미지 렌더링 최적화 힌트로 사용할 수 있다.

---

# 5. Form Attributes

## 5.1 name id for

### [개념]

Form Attribute는 Form 입력 요소의 이름, 연결, 제출 데이터, validation, accessibility에 영향을 준다.

`name`, `id`, `for`는 Form의 기본 연결 구조다.

---

### [핵심]

`name` 핵심:

- form submit 시 key로 사용된다.
- 서버 또는 FormData에서 값을 식별한다.
- radio group은 같은 name을 공유한다.

`id` 핵심:

- label과 연결된다.
- aria-describedby와 연결된다.
- 문서 내 고유해야 한다.

`for` 핵심:

- label이 어떤 input을 설명하는지 지정한다.
- `for` 값은 input id와 일치해야 한다.
- label 클릭 시 input focus가 이동한다.

---

### [실무]

기본 예:

```html
<label for="user-email">Email</label>
<input id="user-email" name="email" type="email" />
```

Radio Group 예:

```html
<fieldset>
  <legend>Notification Method</legend>

  <label>
    <input type="radio" name="notifyMethod" value="email" />
    Email
  </label>

  <label>
    <input type="radio" name="notifyMethod" value="sms" />
    SMS
  </label>
</fieldset>
```

검수 기준:

- input에 name이 있는가?
- label for와 input id가 일치하는가?
- id가 중복되지 않는가?
- radio group name이 동일한가?
- label 클릭 시 input이 focus되는가?

---

### [FAQ]

Q. form input의 name은 왜 필요해?
A. form submit이나 FormData에서 해당 입력 값을 식별하는 key로 사용되기 때문이다.

Q. label for는 무엇과 연결돼?
A. input의 id와 연결된다.

Q. radio button들은 name을 어떻게 해야 해?
A. 같은 선택 그룹이면 같은 name을 사용해야 한다.

Q. label과 input을 연결하면 뭐가 좋아?
A. 접근성이 좋아지고 label 클릭으로 input focus 또는 선택이 가능해진다.

---

## 5.2 type

### [개념]

`type` attribute는 input 또는 button의 동작과 의미를 결정한다.

Button과 Input에서 `type`은 UX, validation, mobile keyboard, form submit 동작에 큰 영향을 준다.

---

### [핵심]

Button type:

- `type="button"`은 일반 동작 버튼이다.
- `type="submit"`은 form 제출 버튼이다.
- `type="reset"`은 form 값을 초기화한다.
- button의 기본 type은 상황에 따라 submit으로 동작할 수 있으므로 명시가 중요하다.

Input type:

- `text`는 일반 텍스트다.
- `email`은 이메일 입력과 validation에 도움된다.
- `password`는 비밀번호 입력이다.
- `number`는 숫자 입력이다.
- `search`는 검색 입력이다.
- `tel`은 전화번호 입력이다.
- `url`은 URL 입력이다.
- `checkbox`는 다중 선택이다.
- `radio`는 단일 선택 그룹이다.

---

### [실무]

Button 예:

```html
<button type="button">Open Modal</button> <button type="submit">Save</button>
```

Input 예:

```html
<input id="email" name="email" type="email" />
<input id="password" name="password" type="password" />
<input id="keyword" name="keyword" type="search" />
```

검수 기준:

- form 내부 button type이 명시되어 있는가?
- submit 의도가 아닌 button이 submit으로 동작하지 않는가?
- input type이 입력 목적과 맞는가?
- mobile keyboard가 입력 목적에 맞게 표시되는가?
- type number가 실제 요구사항에 적합한가?

---

### [FAQ]

Q. button type은 왜 명시해야 해?
A. form 내부에서 의도치 않게 submit이 발생하는 것을 막기 위해 중요하다.

Q. 일반 클릭 버튼은 어떤 type을 써?
A. `type="button"`을 사용한다.

Q. form 제출 버튼은 어떤 type을 써?
A. `type="submit"`을 사용한다.

Q. input type은 왜 중요해?
A. validation, mobile keyboard, 자동완성, 접근성에 영향을 주기 때문이다.

---

## 5.3 required disabled readonly

### [개념]

`required`, `disabled`, `readonly`는 Form 요소의 입력 가능 여부와 validation 상태를 제어하는 attribute다.

---

### [핵심]

`required` 핵심:

- 필수 입력임을 브라우저 validation에 전달한다.
- 시각 표시와 error message도 함께 필요하다.
- label 근처에 필수 표시를 제공할 수 있다.

`disabled` 핵심:

- 요소를 조작할 수 없게 한다.
- form submit에서 제외될 수 있다.
- focus되지 않는다.
- 조작 불가 상태를 시각적으로 표현해야 한다.

`readonly` 핵심:

- 값을 수정할 수 없지만 읽을 수 있다.
- 일부 form submit에 포함될 수 있다.
- focus 가능할 수 있다.
- disabled와 의미가 다르다.

---

### [실무]

예:

```html
<label for="title">Title <span aria-hidden="true">*</span></label>
<input id="title" name="title" type="text" required />

<input id="user-id" name="userId" type="text" readonly value="cyanaria89" />

<button type="submit" disabled>Saving...</button>
```

검수 기준:

- required 필드에 시각적 필수 표시가 있는가?
- required 상태가 error message와 연결되는가?
- disabled와 readonly를 의미에 맞게 구분했는가?
- disabled 상태가 시각적으로 명확한가?
- disabled 요소에 cursor pointer가 남아 있지 않은가?

---

### [FAQ]

Q. required는 뭐야?
A. 해당 form field가 필수 입력임을 나타내는 attribute다.

Q. disabled와 readonly 차이는 뭐야?
A. disabled는 조작 불가이고 submit에서 제외될 수 있으며, readonly는 읽을 수 있지만 수정할 수 없는 상태다.

Q. disabled 요소는 focus돼?
A. 일반적으로 focus되지 않는다.

Q. readonly는 submit에 포함돼?
A. 요소와 상황에 따라 포함될 수 있으며 disabled와 다르다.

---

## 5.4 autocomplete

### [개념]

`autocomplete` attribute는 브라우저가 입력 필드에 자동완성 정보를 제공할지와 어떤 종류의 값을 제공할지 지정한다.

Login, Sign Up, Address, Payment-like Form에서 UX와 보안에 영향을 준다.

---

### [핵심]

Autocomplete 핵심:

- 브라우저 자동완성을 돕는다.
- `autocomplete="email"`은 이메일 입력에 사용한다.
- `autocomplete="username"`은 사용자 이름에 사용한다.
- `autocomplete="current-password"`는 현재 비밀번호에 사용한다.
- `autocomplete="new-password"`는 새 비밀번호에 사용한다.
- 무조건 `off`를 남용하면 UX가 나빠질 수 있다.
- 민감한 입력에서는 정책과 보안 요구를 검토한다.

---

### [실무]

Login 예:

```html
<input id="login-email" name="email" type="email" autocomplete="email" />

<input
  id="login-password"
  name="password"
  type="password"
  autocomplete="current-password"
/>
```

Sign Up 예:

```html
<input
  id="signup-password"
  name="password"
  type="password"
  autocomplete="new-password"
/>
```

검수 기준:

- email field에 autocomplete email이 있는가?
- login password는 current-password인가?
- sign up password는 new-password인가?
- autocomplete off를 불필요하게 남용하지 않았는가?
- name과 autocomplete 값이 의미상 일치하는가?

---

### [FAQ]

Q. autocomplete는 뭐야?
A. 브라우저가 입력 필드에 어떤 자동완성 정보를 제공할지 지정하는 attribute다.

Q. 로그인 비밀번호에는 뭐를 써?
A. `autocomplete="current-password"`를 사용한다.

Q. 회원가입 새 비밀번호에는 뭐를 써?
A. `autocomplete="new-password"`를 사용한다.

Q. autocomplete off를 쓰면 좋아?
A. 무조건 좋지 않다. 자동완성 UX와 보안 요구를 함께 검토해야 한다.

---

# 6. Boolean Attributes

## 6.1 Boolean Attribute Concept

### [개념]

Boolean Attribute는 attribute가 존재하는 것만으로 true 의미를 가지는 HTML attribute다.

대표 예:

```html
<input required />
<button disabled>Save</button>
<input type="checkbox" checked />
```

---

### [핵심]

Boolean Attribute 핵심:

- attribute가 존재하면 true다.
- 값이 `"false"`여도 HTML에서는 true로 해석될 수 있다.
- `disabled="false"`는 disabled가 false라는 뜻이 아니다.
- React JSX에서는 boolean prop으로 제어한다.
- required, disabled, checked, selected, readonly, hidden 등이 있다.
- 실제 상태와 DOM attribute가 일치해야 한다.

---

### [실무]

HTML 예:

```html
<button type="button" disabled>Saving</button>
```

잘못된 HTML 예:

```html
<button type="button" disabled="false">Save</button>
```

React 예:

```jsx
<button type="button" disabled={isSaving}>
  Save
</button>
```

검수 기준:

- boolean attribute를 문자열 false로 작성하지 않았는가?
- React에서 boolean prop으로 상태를 제어하는가?
- checked/defaultChecked controlled 상태가 명확한가?
- hidden 상태와 CSS display 상태가 충돌하지 않는가?

---

### [FAQ]

Q. Boolean Attribute가 뭐야?
A. attribute가 존재하는 것만으로 true 의미를 가지는 HTML attribute다.

Q. disabled="false"는 disabled가 아니야?
A. 아니다. HTML에서는 disabled attribute가 존재하므로 disabled 상태로 해석될 수 있다.

Q. React에서 disabled는 어떻게 써?
A. `disabled={isDisabled}`처럼 boolean 값으로 제어한다.

Q. required도 boolean attribute야?
A. 맞다. 존재하면 필수 입력 상태를 의미한다.

---

# 7. ARIA Attributes

## 7.1 ARIA Concept

### [개념]

ARIA는 Accessible Rich Internet Applications의 약자다.

ARIA Attribute는 HTML만으로 표현하기 어려운 접근성 이름, 설명, 상태, 관계를 보조 기술에 전달하기 위해 사용한다.

예:

```html
<button type="button" aria-expanded="false" aria-controls="menu">Menu</button>
```

---

### [핵심]

ARIA 핵심:

- native semantic HTML을 대체하는 것이 아니라 보완한다.
- 가능한 경우 native HTML 요소를 먼저 사용한다.
- 잘못된 ARIA는 없는 것보다 더 나쁠 수 있다.
- 실제 UI 상태와 ARIA 상태는 반드시 일치해야 한다.
- `aria-label`은 접근성 이름을 제공한다.
- `aria-labelledby`는 다른 요소의 텍스트를 이름으로 참조한다.
- `aria-describedby`는 설명 텍스트를 참조한다.
- `aria-expanded`는 열림/닫힘 상태를 나타낸다.
- `aria-current`는 현재 항목을 나타낸다.
- `aria-invalid`는 입력 오류 상태를 나타낸다.

---

### [실무]

ARIA 사용 Flow:

```text
Native HTML로 표현 가능한가?
→ 가능하면 native 사용
→ 접근성 이름이 부족한가?
→ aria-label / labelledby 검토
→ 설명 연결이 필요한가?
→ aria-describedby 검토
→ 상태 전달이 필요한가?
→ aria-expanded / selected / current / invalid 검토
→ 실제 상태와 동기화
```

검수 기준:

- native button/link/input을 먼저 사용했는가?
- role을 불필요하게 추가하지 않았는가?
- ARIA 상태가 실제 UI 상태와 일치하는가?
- 참조하는 id가 실제 존재하는가?
- ARIA로 의미를 속이거나 잘못 전달하지 않았는가?

---

### [FAQ]

Q. ARIA는 뭐야?
A. HTML만으로 부족한 접근성 이름, 설명, 상태, 관계를 보조 기술에 전달하는 attribute 체계다.

Q. ARIA를 많이 쓰면 접근성이 좋아져?
A. 아니다. native HTML을 우선 사용하고 필요한 경우에만 정확히 써야 한다.

Q. 잘못된 ARIA는 왜 위험해?
A. 보조 기술 사용자에게 실제 UI와 다른 정보를 전달할 수 있기 때문이다.

Q. ARIA 검수에서 가장 중요한 것은?
A. 실제 UI 상태와 ARIA 상태가 일치하는지 확인하는 것이다.

---

## 7.2 aria-label and aria-labelledby

### [개념]

`aria-label`과 `aria-labelledby`는 요소의 accessible name을 제공하는 ARIA attribute다.

Accessible name은 screen reader가 요소를 어떤 이름으로 읽을지 결정하는 핵심 정보다.

---

### [핵심]

`aria-label` 핵심:

- 문자열로 직접 접근성 이름을 제공한다.
- icon-only button에 자주 사용한다.
- visible text가 없는 interactive element에 유용하다.
- visible text와 충돌하지 않도록 주의한다.

`aria-labelledby` 핵심:

- 다른 요소의 id를 참조해 접근성 이름을 만든다.
- visible heading이나 label을 재사용할 수 있다.
- 여러 id를 공백으로 연결할 수 있다.
- 참조 대상 id가 실제 존재해야 한다.

---

### [실무]

Icon Button 예:

```html
<button type="button" aria-label="Close dialog">
  <span aria-hidden="true">×</span>
</button>
```

Dialog 예:

```html
<section role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Delete Festival</h2>
</section>
```

검수 기준:

- visible text가 없는 interactive element에 accessible name이 있는가?
- aria-label이 visible label과 다른 의미를 전달하지 않는가?
- aria-labelledby가 실제 존재하는 id를 참조하는가?
- dialog나 section의 제목 연결이 명확한가?

---

### [FAQ]

Q. aria-label은 뭐야?
A. 요소에 문자열로 접근성 이름을 제공하는 attribute다.

Q. aria-labelledby는 뭐야?
A. 다른 요소의 텍스트를 참조해 접근성 이름을 제공하는 attribute다.

Q. icon-only button에는 무엇을 써?
A. `aria-label` 또는 visually-hidden 텍스트를 사용할 수 있다.

Q. aria-label과 visible text가 다르면 안 돼?
A. 사용자에게 혼란을 줄 수 있으므로 visible text와 의미가 일치해야 한다.

---

## 7.3 aria-describedby

### [개념]

`aria-describedby`는 요소에 추가 설명을 연결하는 ARIA attribute다.

Form helper text, error message, 입력 조건, 보조 설명을 연결할 때 사용한다.

---

### [핵심]

`aria-describedby` 핵심:

- 설명 요소의 id를 참조한다.
- 여러 id를 공백으로 연결할 수 있다.
- input helper text와 error message 연결에 유용하다.
- 접근성 이름이 아니라 추가 설명이다.
- 참조 id가 실제 존재해야 한다.
- error 상태에서는 error message id를 포함해야 한다.

---

### [실무]

Helper Text 예:

```html
<label for="password">Password</label>
<input
  id="password"
  name="password"
  type="password"
  aria-describedby="password-help"
/>
<p id="password-help">Use at least 8 characters.</p>
```

Error Text 예:

```html
<label for="email">Email</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error">Enter a valid email address.</p>
```

검수 기준:

- helper text id가 input aria-describedby와 일치하는가?
- error message가 aria-describedby로 연결되는가?
- 여러 설명 id가 필요한 경우 공백으로 연결되는가?
- 설명이 접근성 이름으로 잘못 들어가지 않았는가?

---

### [FAQ]

Q. aria-describedby는 뭐야?
A. 요소에 추가 설명 텍스트를 연결하는 ARIA attribute다.

Q. form error message는 어떻게 연결해?
A. input의 aria-describedby가 error message id를 참조하도록 연결한다.

Q. aria-describedby와 aria-label 차이는?
A. aria-label은 이름이고 aria-describedby는 추가 설명이다.

Q. aria-describedby는 여러 개 연결 가능해?
A. 가능하다. id를 공백으로 나열할 수 있다.

---

## 7.4 aria-expanded aria-controls

### [개념]

`aria-expanded`는 요소가 제어하는 콘텐츠가 열려 있는지 닫혀 있는지 나타낸다.

`aria-controls`는 trigger가 제어하는 대상 요소의 id를 참조한다.

Dropdown, Accordion, Disclosure, Mobile Navigation에 자주 사용된다.

---

### [핵심]

`aria-expanded` 핵심:

- 열림 상태는 `true`다.
- 닫힘 상태는 `false`다.
- 실제 UI 열림 상태와 반드시 일치해야 한다.
- trigger 요소에 사용한다.

`aria-controls` 핵심:

- 제어 대상 요소의 id를 참조한다.
- trigger와 controlled panel 관계를 표현한다.
- 참조 대상 id가 실제 존재해야 한다.

---

### [실무]

Accordion 예:

```html
<button type="button" aria-expanded="false" aria-controls="faq-panel-1">
  What is FestaPick?
</button>

<div id="faq-panel-1" hidden>FestaPick helps users discover festivals.</div>
```

Dropdown 예:

```html
<button type="button" aria-expanded="true" aria-controls="user-menu">
  User Menu
</button>

<div id="user-menu">Menu content</div>
```

검수 기준:

- aria-expanded 값이 실제 열림 상태와 일치하는가?
- aria-controls가 실제 존재하는 id를 참조하는가?
- 닫힌 panel이 hidden 처리되어 focus되지 않는가?
- trigger가 button인가?
- 상태 변경 시 aria-expanded도 함께 업데이트되는가?

---

### [FAQ]

Q. aria-expanded는 뭐야?
A. trigger가 제어하는 콘텐츠가 열려 있는지 닫혀 있는지 나타내는 attribute다.

Q. aria-controls는 뭐야?
A. trigger가 제어하는 요소의 id를 참조하는 attribute다.

Q. aria-expanded는 어디에 붙여?
A. Dropdown, Accordion, Disclosure를 여는 trigger button에 붙인다.

Q. aria-expanded 값은 언제 바뀌어야 해?
A. 실제 panel이 열리거나 닫힐 때 함께 바뀌어야 한다.

---

## 7.5 aria-current aria-invalid aria-hidden

### [개념]

`aria-current`, `aria-invalid`, `aria-hidden`은 현재 항목, 입력 오류 상태, 보조 기술 노출 여부를 표현하는 ARIA attribute다.

---

### [핵심]

`aria-current` 핵심:

- 현재 페이지나 현재 단계, 현재 위치를 나타낸다.
- navigation link의 현재 페이지 표시에 자주 사용한다.
- 대표 값은 `page`, `step`, `location`, `date`, `time`, `true`다.

`aria-invalid` 핵심:

- 입력 값이 유효하지 않은 상태를 나타낸다.
- error message와 함께 사용한다.
- validation 상태와 시각 상태가 일치해야 한다.

`aria-hidden` 핵심:

- 요소를 accessibility tree에서 숨긴다.
- 장식 아이콘에 `aria-hidden="true"`를 사용할 수 있다.
- focus 가능한 요소에 aria-hidden을 잘못 쓰면 위험하다.
- 보이는 중요한 콘텐츠를 aria-hidden으로 숨기면 안 된다.

---

### [실무]

Current Page 예:

```html
<a href="/festivals" aria-current="page"> Festivals </a>
```

Invalid Field 예:

```html
<input
  id="email"
  name="email"
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error">Enter a valid email address.</p>
```

Decorative Icon 예:

```html
<button type="button" aria-label="Search">
  <span aria-hidden="true">🔍</span>
</button>
```

검수 기준:

- 현재 페이지 link에 aria-current가 있는가?
- aria-invalid 상태와 error message가 연결되는가?
- 장식 아이콘만 aria-hidden 처리했는가?
- focus 가능한 요소에 aria-hidden을 적용하지 않았는가?
- 중요한 텍스트를 aria-hidden으로 숨기지 않았는가?

---

### [FAQ]

Q. aria-current는 뭐야?
A. navigation이나 step 안에서 현재 항목을 나타내는 ARIA attribute다.

Q. aria-invalid는 뭐야?
A. 입력 값이 유효하지 않은 상태임을 보조 기술에 전달하는 attribute다.

Q. aria-hidden은 언제 써?
A. 장식 아이콘처럼 보조 기술에 읽힐 필요가 없는 요소를 숨길 때 사용한다.

Q. aria-hidden을 focus 가능한 요소에 써도 돼?
A. 안 된다. 보조 기술에서는 숨겨졌는데 keyboard focus가 가는 문제가 생길 수 있다.

---

# 8. Hidden and Visibility Attributes

## 8.1 hidden

### [개념]

`hidden` attribute는 요소가 현재 관련 없거나 표시되지 않아야 함을 나타내는 boolean attribute다.

일반적으로 브라우저는 `[hidden]` 요소를 화면과 accessibility tree에서 숨긴다.

예:

```html
<div id="menu-panel" hidden>Menu content</div>
```

---

### [핵심]

`hidden` 핵심:

- boolean attribute다.
- 존재하면 숨김 상태를 의미한다.
- `hidden="false"`는 숨김 해제를 의미하지 않는다.
- 닫힌 dropdown, inactive tab panel, collapsed accordion panel에 사용할 수 있다.
- 숨겨진 요소 내부는 focus되지 않아야 한다.
- CSS display와 충돌하지 않게 관리해야 한다.
- transition이 필요한 경우 hidden 즉시 전환은 제한이 있다.

---

### [실무]

Tab Panel 예:

```html
<section id="panel-info" role="tabpanel">Info content</section>

<section id="panel-review" role="tabpanel" hidden>Review content</section>
```

CSS 보호:

```css
[hidden] {
  display: none !important;
}
```

검수 기준:

- hidden 상태가 실제 시각 상태와 일치하는가?
- hidden 내부 interactive element에 focus가 가지 않는가?
- `hidden="false"`처럼 잘못 작성하지 않았는가?
- transition이 필요한 요소에 hidden을 즉시 적용해 animation이 끊기지 않는가?

---

### [FAQ]

Q. hidden attribute는 뭐야?
A. 요소를 화면과 accessibility tree에서 숨기는 boolean attribute다.

Q. hidden="false"는 표시 상태야?
A. 아니다. hidden attribute가 존재하므로 숨김 상태로 해석될 수 있다.

Q. 닫힌 tab panel에 hidden을 써도 돼?
A. 가능하다. inactive panel을 숨기고 focus되지 않게 할 수 있다.

Q. hidden과 display none은 같아?
A. 브라우저 기본 동작은 display none과 유사하지만 hidden은 HTML 의미를 가진 attribute다.

---

# 9. Language and Document Metadata

## 9.1 lang

### [개념]

`lang` attribute는 문서 또는 특정 요소의 언어를 지정한다.

Screen Reader 발음, 번역, 검색 엔진 이해, typography 처리에 영향을 준다.

예:

```html
<html lang="ko"></html>
```

---

### [핵심]

`lang` 핵심:

- 문서 기본 언어를 지정한다.
- screen reader가 올바른 발음 규칙을 선택하는 데 도움된다.
- 검색 엔진이 문서 언어를 이해하는 데 도움된다.
- 문서 일부가 다른 언어면 해당 요소에 lang을 지정할 수 있다.
- 한국어 문서는 `lang="ko"`를 사용한다.
- 영어 문서는 `lang="en"`을 사용한다.

---

### [실무]

기본 문서:

```html
<html lang="ko"></html>
```

일부 외국어:

```html
<p>CSS의 <span lang="en">cascade</span>는 스타일 적용 순서를 의미한다.</p>
```

검수 기준:

- html 요소에 lang이 있는가?
- 문서 언어와 lang 값이 일치하는가?
- 일부 다른 언어 텍스트에 lang이 필요한가?
- template 복사로 잘못된 lang이 남아 있지 않은가?

---

### [FAQ]

Q. lang attribute는 뭐야?
A. 문서나 요소의 언어를 지정하는 attribute다.

Q. 한국어 페이지에는 어떤 lang을 써?
A. `lang="ko"`를 사용한다.

Q. lang은 접근성에 왜 중요해?
A. screen reader가 올바른 언어 발음 규칙을 적용하는 데 도움을 준다.

Q. 문서 일부가 영어면 어떻게 해?
A. 필요한 경우 해당 요소에 `lang="en"`을 지정할 수 있다.

---

## 9.2 charset viewport title meta description

### [개념]

문서 metadata는 브라우저, 검색 엔진, 공유 미리보기, 모바일 viewport에 문서 정보를 제공한다.

HTML `head` 내부에 작성한다.

---

### [핵심]

`charset` 핵심:

- 문자 인코딩을 지정한다.
- 일반적으로 `UTF-8`을 사용한다.
- 한글 깨짐 방지에 중요하다.

`viewport` 핵심:

- 모바일 viewport 크기와 확대 비율을 지정한다.
- responsive web design에 필수다.

`title` 핵심:

- 브라우저 탭 제목과 검색 결과 제목에 사용된다.
- 페이지별로 고유하고 설명적이어야 한다.

`meta description` 핵심:

- 검색 결과 snippet 후보로 사용될 수 있다.
- 페이지 내용을 짧고 명확하게 설명한다.
- 페이지마다 중복을 피한다.

---

### [실무]

기본 head 예:

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Festival Detail - FestaPick</title>
  <meta
    name="description"
    content="축제 상세 정보, 일정, 위치, 리뷰를 확인하세요."
  />
</head>
```

검수 기준:

- charset이 UTF-8로 지정되어 있는가?
- viewport meta가 있는가?
- title이 페이지 내용을 구체적으로 설명하는가?
- 모든 페이지 title이 동일하지 않은가?
- meta description이 페이지마다 적절한가?

---

### [FAQ]

Q. charset meta는 왜 필요해?
A. 문서 문자 인코딩을 지정해 한글 깨짐 같은 문제를 줄이기 위해 필요하다.

Q. viewport meta는 왜 필요해?
A. 모바일에서 페이지가 올바른 viewport 폭으로 표시되도록 하기 위해 필요하다.

Q. title 태그는 왜 중요해?
A. 브라우저 탭, 검색 결과, screen reader 문맥에 영향을 주기 때문이다.

Q. meta description은 SEO에 중요해?
A. 검색 결과 설명 후보가 될 수 있어 페이지 내용을 명확히 전달하는 데 중요하다.

---

# 10. SEO Basics

## 10.1 Semantic HTML and SEO

### [개념]

SEO Basics는 검색 엔진이 페이지의 주제, 구조, 콘텐츠 의미를 이해할 수 있도록 HTML을 작성하는 기본 기준이다.

Semantic HTML, heading hierarchy, title, meta description, link text, image alt가 SEO 기초에 해당한다.

---

### [핵심]

SEO 기초 핵심:

- 페이지마다 고유한 title을 작성한다.
- meta description은 페이지 내용을 설명한다.
- `h1`은 페이지의 주요 제목이다.
- heading은 순서와 계층을 지킨다.
- 의미 있는 link text를 사용한다.
- 이미지 alt는 이미지 의미를 설명한다.
- semantic landmark를 사용한다.
- 중복 콘텐츠와 빈 제목을 피한다.
- 중요한 콘텐츠를 이미지 안 텍스트로만 제공하지 않는다.
- SPA에서는 라우트별 metadata 관리가 필요하다.

---

### [실무]

좋은 heading 예:

```html
<main>
  <h1>Seoul Light Festival</h1>

  <section aria-labelledby="schedule-title">
    <h2 id="schedule-title">Schedule</h2>
  </section>

  <section aria-labelledby="location-title">
    <h2 id="location-title">Location</h2>
  </section>
</main>
```

좋은 link text:

```html
<a href="/festivals/seoul-light">View Seoul Light Festival details</a>
```

나쁜 link text:

```html
<a href="/festivals/seoul-light">Click here</a>
```

검수 기준:

- 페이지마다 h1이 명확한가?
- heading 순서가 논리적인가?
- title과 description이 페이지별로 고유한가?
- link text만 읽어도 목적을 알 수 있는가?
- 이미지 alt가 의미를 전달하는가?
- landmark가 semantic하게 사용되는가?

---

### [FAQ]

Q. SEO Basics에서 가장 중요한 HTML 요소는?
A. title, meta description, h1, semantic landmark, link text, image alt가 중요하다.

Q. h1은 여러 개 써도 돼?
A. 가능은 하지만 페이지의 주요 제목을 명확히 하기 위해 하나의 대표 h1을 유지하는 것이 일반적으로 관리하기 쉽다.

Q. Click here 같은 링크 텍스트는 왜 안 좋아?
A. 링크 텍스트만으로 이동 목적을 알 수 없기 때문이다.

Q. 이미지 alt는 SEO에도 영향이 있어?
A. 검색 엔진이 이미지와 주변 콘텐츠 의미를 이해하는 데 도움을 줄 수 있다.

---

# 11. Accessibility Basics

## 11.1 Accessibility Concept

### [개념]

Accessibility는 다양한 사용자가 웹 콘텐츠와 기능을 인식하고 조작하고 이해할 수 있게 만드는 기준이다.

HTML/CSS Foundation에서 Accessibility는 semantic HTML, keyboard navigation, focus style, label, alt, contrast, ARIA 상태와 연결된다.

---

### [핵심]

Accessibility 핵심:

- native semantic HTML을 우선 사용한다.
- 모든 interactive element는 keyboard로 접근 가능해야 한다.
- focus-visible이 명확해야 한다.
- button과 link 역할을 구분한다.
- form field는 label과 연결되어야 한다.
- 이미지에는 적절한 alt가 필요하다.
- 색상만으로 정보를 전달하지 않는다.
- contrast가 충분해야 한다.
- ARIA는 실제 상태와 일치해야 한다.
- hidden content에 focus가 가지 않아야 한다.
- motion과 hover-only interaction을 주의한다.

---

### [실무]

Accessibility 검수 Flow:

```text
Semantic Element 확인
→ Keyboard Tab 이동 확인
→ Focus Visible 확인
→ Accessible Name 확인
→ Form Label 확인
→ Error Message 연결 확인
→ Image Alt 확인
→ Contrast 확인
→ ARIA State 동기화 확인
→ Hidden Focus 확인
```

검수 기준:

- div/span으로 button을 만들지 않았는가?
- keyboard만으로 주요 기능을 사용할 수 있는가?
- focus outline이 보이는가?
- icon-only button에 accessible name이 있는가?
- form label이 input과 연결되어 있는가?
- error message가 보조 기술에 전달되는가?
- modal/dropdown hidden 상태와 focus 상태가 일치하는가?

---

### [FAQ]

Q. Accessibility가 뭐야?
A. 다양한 사용자가 웹 콘텐츠와 기능을 인식하고 조작하고 이해할 수 있게 만드는 기준이다.

Q. Accessibility에서 HTML이 중요한 이유는?
A. semantic HTML 자체가 보조 기술에 의미와 역할을 전달하기 때문이다.

Q. CSS도 접근성에 영향을 줘?
A. 그렇다. focus-visible, contrast, hidden 상태, responsive layout은 CSS와 직접 연결된다.

Q. 접근성 검수에서 가장 먼저 볼 것은?
A. semantic element, keyboard focus, accessible name, label 연결, ARIA 상태를 먼저 확인한다.

---

# 12. Keyboard Accessibility

## 12.1 Keyboard Navigation

### [개념]

Keyboard Accessibility는 마우스 없이 keyboard만으로 웹 UI를 탐색하고 조작할 수 있는 기준이다.

Interactive Element는 Tab으로 이동 가능하고 Enter 또는 Space로 조작 가능해야 한다.

---

### [핵심]

Keyboard 핵심:

- link는 Enter로 활성화된다.
- button은 Enter와 Space로 활성화된다.
- form control은 keyboard로 조작 가능해야 한다.
- custom div button은 keyboard 접근성이 부족하므로 피한다.
- focus order는 DOM 순서를 따른다.
- visual order와 focus order가 크게 어긋나면 안 된다.
- skip link는 keyboard 사용자의 빠른 이동을 돕는다.
- Modal은 focus trap이 필요하다.
- Dropdown과 Tabs는 추가 keyboard interaction이 필요할 수 있다.

---

### [실무]

Skip Link 예:

```html
<a class="skip-link" href="#main-content"> Skip to main content </a>

<main id="main-content">Main content</main>
```

```css
.skip-link {
  position: absolute;
  left: 1rem;
  top: 1rem;
  transform: translateY(-200%);
}

.skip-link:focus-visible {
  transform: translateY(0);
}
```

검수 기준:

- Tab 이동 순서가 자연스러운가?
- focus-visible이 모든 interactive element에서 보이는가?
- custom interactive element를 div/span으로 만들지 않았는가?
- modal이 열렸을 때 focus가 modal 밖으로 나가지 않는가?
- hidden panel 내부 요소에 focus가 가지 않는가?
- skip link가 header에 가려지지 않는가?

---

### [FAQ]

Q. Keyboard Accessibility는 뭐야?
A. 마우스 없이 keyboard만으로 웹 UI를 탐색하고 조작할 수 있게 하는 기준이다.

Q. div에 onClick을 붙이면 button과 같아?
A. 아니다. keyboard 동작과 semantic role이 부족하므로 button을 사용하는 것이 좋다.

Q. focus order는 무엇을 따라가?
A. 일반적으로 DOM 순서를 따른다.

Q. Skip Link는 왜 필요해?
A. keyboard 사용자가 반복 navigation을 건너뛰고 main content로 이동할 수 있게 도와준다.

---

# 13. Attribute and Accessibility Troubleshooting

## 13.1 Attribute Bug

### [개념]

Attribute Bug는 HTML attribute가 누락되거나 잘못 작성되어 링크, 이미지, Form, 접근성, SEO, Component 상태가 올바르게 동작하지 않는 문제다.

주요 원인은 id 중복, label 연결 오류, aria 상태 불일치, alt 누락, button type 누락, boolean attribute 오용이다.

---

### [핵심]

주요 문제:

- id 중복
- label for와 input id 불일치
- aria-describedby가 없는 id 참조
- aria-expanded가 실제 열림 상태와 불일치
- aria-current 누락
- aria-invalid와 error message 연결 누락
- icon-only button accessible name 누락
- img alt 누락
- 장식 이미지에 불필요한 alt 텍스트
- button type 누락
- disabled="false" 오용
- hidden="false" 오용
- target="\_blank"에 rel 누락
- autocomplete 부정확
- lang 누락
- title과 meta description 중복

---

### [실무]

Debug Flow:

```text
Element Role 확인
→ Required Attribute 확인
→ id 연결 확인
→ Accessible Name 확인
→ ARIA State 확인
→ Boolean Attribute 확인
→ Form Submit 데이터 확인
→ SEO Metadata 확인
→ Keyboard Focus 확인
```

문제 예:

```text
문제: label 클릭해도 input에 focus가 가지 않음
원인: label for와 input id 불일치
해결: for 값과 id 값을 동일하게 수정
```

```text
문제: Dropdown은 닫혔는데 screen reader에는 열림으로 전달됨
원인: aria-expanded 값 미동기화
해결: 실제 open state와 aria-expanded를 함께 업데이트
```

```text
문제: Save button이 form 안에서 의도치 않게 submit됨
원인: button type 누락
해결: 일반 버튼에는 type="button" 명시
```

검수 기준:

- DevTools Accessibility Tree에서 이름과 역할을 확인했는가?
- id 참조 attribute가 실제 요소를 가리키는가?
- boolean attribute를 문자열 false로 작성하지 않았는가?
- ARIA 상태가 실제 UI 상태와 동기화되는가?
- SEO metadata가 라우트별로 적절한가?

---

### [FAQ]

Q. Attribute Bug에서 가장 흔한 문제는 뭐야?
A. label/id 연결 오류, button type 누락, aria 상태 불일치, alt 누락이 흔하다.

Q. ARIA 상태가 틀리면 왜 문제야?
A. 보조 기술 사용자에게 실제 UI와 다른 상태가 전달되기 때문이다.

Q. Boolean attribute는 어떻게 디버깅해?
A. disabled, hidden, checked 같은 attribute가 존재하는지만으로 true가 되는지 확인한다.

Q. Attribute 문제는 어떤 순서로 확인해?
A. 요소 역할, 필수 attribute, id 연결, accessible name, ARIA 상태, boolean attribute 순서로 확인한다.

---

# 14. Comparison Rules

## 14.1 id vs class

### [개념]

`id`와 `class`는 요소를 식별하는 attribute지만 목적과 제약이 다르다.

`id`는 고유 식별자이고 `class`는 styling과 grouping에 적합하다.

---

### [핵심]

| 비교            | id                       | class                         |
| --------------- | ------------------------ | ----------------------------- |
| 고유성          | 문서 내 고유             | 여러 요소 공유 가능           |
| 주 용도         | label/aria/fragment 연결 | CSS styling, component naming |
| CSS specificity | 높음                     | 일반적                        |
| 반복 사용       | 불가                     | 가능                          |
| 예시            | `id="email"`             | `class="form-input"`          |
| 주의            | 중복 금지                | 이름 일관성                   |

---

### [실무]

선택 기준:

```text
label 연결 → id
aria-labelledby 참조 → id
fragment link target → id
component styling → class
variant styling → class
반복 카드 styling → class
```

---

### [FAQ]

Q. id와 class 차이는 뭐야?
A. id는 문서 내 고유 식별자이고 class는 여러 요소에 공유 가능한 styling/grouping 이름이다.

Q. CSS styling에는 id와 class 중 뭐가 좋아?
A. 일반적으로 class가 유지보수에 더 적합하다.

Q. id는 언제 꼭 필요해?
A. label 연결, ARIA 참조, fragment link 대상에 필요하다.

---

## 14.2 alt vs title

### [개념]

`alt`는 이미지 대체 텍스트이고 `title`은 요소의 보조 설명이다.

`alt`는 이미지 접근성에 필수적이고, `title`은 중요한 정보 전달 수단으로 신뢰하기 어렵다.

---

### [핵심]

| 비교   | alt                | title               |
| ------ | ------------------ | ------------------- |
| 대상   | img                | 대부분 요소         |
| 목적   | 이미지 대체 텍스트 | 보조 설명           |
| 접근성 | 매우 중요          | 일관성 낮음         |
| 모바일 | 안정적             | hover 의존 한계     |
| 필수성 | img에 필요         | 선택                |
| 주의   | 의미에 맞게 작성   | 중요 정보 의존 금지 |

---

### [실무]

선택 기준:

```text
이미지 의미 설명 → alt
장식 이미지 → alt=""
Icon-only button 이름 → aria-label
부가 tooltip → title보다 visible/help text 검토
```

---

### [FAQ]

Q. alt와 title 차이는 뭐야?
A. alt는 이미지 대체 텍스트이고 title은 요소에 대한 보조 설명이다.

Q. 이미지 설명은 title에 쓰면 돼?
A. 아니다. 이미지 대체 텍스트는 alt에 작성해야 한다.

Q. 중요한 설명을 title에만 넣어도 돼?
A. 권장하지 않는다. 모바일과 보조 기술에서 안정적으로 전달되지 않을 수 있다.

---

## 14.3 disabled vs readonly

### [개념]

`disabled`와 `readonly`는 둘 다 사용자가 값을 수정하지 못하게 할 수 있지만 의미와 Form 동작이 다르다.

---

### [핵심]

| 비교      | disabled               | readonly                             |
| --------- | ---------------------- | ------------------------------------ |
| 수정 가능 | 불가                   | 불가                                 |
| focus     | 일반적으로 불가        | 가능할 수 있음                       |
| submit    | 제외될 수 있음         | 포함될 수 있음                       |
| 시각 상태 | 조작 불가              | 읽기 전용                            |
| 사용 예   | 저장 중 버튼           | 수정 불가 사용자 ID                  |
| 주의      | 값 전송 필요 시 부적합 | 모든 input type에 적용되는 것은 아님 |

---

### [실무]

선택 기준:

```text
저장 중 버튼 비활성 → disabled
권한 없어서 입력 불가 → disabled 또는 readonly 요구 검토
사용자 ID 표시만 하고 제출 필요 → readonly
값을 제출에서 제외 → disabled 가능
```

---

### [FAQ]

Q. disabled와 readonly 차이는 뭐야?
A. disabled는 조작 불가이고 submit에서 제외될 수 있으며, readonly는 읽을 수 있지만 수정할 수 없는 상태다.

Q. 값이 제출되어야 하면 disabled를 써도 돼?
A. 주의해야 한다. disabled 값은 submit에서 제외될 수 있으므로 readonly나 hidden input을 검토한다.

Q. readonly는 focus 가능해?
A. 가능할 수 있다. disabled와 동작이 다르다.

---

## 14.4 aria-label vs aria-labelledby vs aria-describedby

### [개념]

`aria-label`, `aria-labelledby`, `aria-describedby`는 모두 접근성 정보 제공에 사용되지만 역할이 다르다.

---

### [핵심]

| 비교      | aria-label                 | aria-labelledby           | aria-describedby       |
| --------- | -------------------------- | ------------------------- | ---------------------- |
| 목적      | 이름 직접 제공             | 다른 요소를 이름으로 참조 | 설명 연결              |
| 값        | 문자열                     | id 참조                   | id 참조                |
| 사용 예   | icon button                | dialog title              | helper/error text      |
| 정보 유형 | accessible name            | accessible name           | accessible description |
| 주의      | visible text와 불일치 금지 | id 존재 필요              | 이름 대체 아님         |

---

### [실무]

선택 기준:

```text
Icon-only button 이름 → aria-label
Dialog 제목 연결 → aria-labelledby
Input helper text 연결 → aria-describedby
Input error message 연결 → aria-describedby + aria-invalid
Visible label이 있으면 → label/labelledby 우선
```

---

### [FAQ]

Q. aria-label과 aria-labelledby 차이는?
A. aria-label은 문자열로 이름을 제공하고 aria-labelledby는 다른 요소의 텍스트를 이름으로 참조한다.

Q. aria-describedby는 이름이야?
A. 아니다. 이름이 아니라 추가 설명이다.

Q. Form error message에는 무엇을 써?
A. `aria-describedby`로 error message를 연결하고 `aria-invalid`로 오류 상태를 표시한다.

---

# 15. Common Mistakes

## 15.1 HTML Attributes Accessibility SEO Common Mistakes

### [개념]

HTML Attribute, Accessibility, SEO 실수는 사용성 저하, screen reader 정보 오류, Form UX 문제, 검색 노출 품질 저하, Component 상태 불일치로 이어진다.

---

### [핵심]

자주 발생하는 실수:

- html `lang` 누락
- charset 누락
- viewport meta 누락
- 모든 페이지 title 동일
- meta description 중복 또는 누락
- h1 누락 또는 heading hierarchy 혼란
- 의미 없는 link text 사용
- `a href="#"`를 button처럼 사용
- button type 누락
- icon-only button accessible name 누락
- img alt 누락
- 장식 이미지에 불필요한 alt 작성
- alt에 파일명 또는 “image”만 작성
- label for와 input id 불일치
- input name 누락
- id 중복
- aria-labelledby/describedby가 없는 id 참조
- aria-expanded와 실제 UI 상태 불일치
- aria-invalid와 error message 연결 누락
- aria-hidden을 focus 가능한 요소에 적용
- disabled="false" 또는 hidden="false" 오용
- target="\_blank"에 rel 누락
- autocomplete 부정확
- title attribute에 중요한 정보 의존
- hidden content 내부 focus 가능

---

### [실무]

Troubleshooting Flow:

```text
HTML Review
→ Document Metadata 확인
→ Semantic Structure 확인
→ Link/Button 역할 확인
→ Image Alt 확인
→ Form Label 연결 확인
→ ARIA 참조 확인
→ State Attribute 동기화 확인
→ Keyboard Focus 확인
→ SEO Text 확인
```

문제 예:

```text
문제: 스크린 리더가 버튼을 'button'으로만 읽음
원인: icon-only button에 accessible name 없음
해결: aria-label 또는 visually-hidden 텍스트 추가
```

```text
문제: 검색 결과 제목이 모든 페이지에서 동일함
원인: title이 route별로 변경되지 않음
해결: 페이지별 고유 title과 meta description 관리
```

```text
문제: error text가 화면에는 보이지만 보조 기술에 연결되지 않음
원인: aria-describedby 누락
해결: input과 error message id 연결
```

---

### [FAQ]

Q. HTML Attribute에서 가장 흔한 실수는 뭐야?
A. button type 누락, alt 누락, label/id 연결 오류, ARIA 상태 불일치가 흔하다.

Q. Accessibility에서 가장 흔한 실수는 뭐야?
A. semantic element 대신 div/span을 쓰고 focus-visible, accessible name, label 연결을 놓치는 것이다.

Q. SEO에서 가장 흔한 실수는 뭐야?
A. 모든 페이지 title이 같거나 heading hierarchy가 불명확하고 link text가 의미 없는 것이다.

Q. Attribute Accessibility SEO 문제는 어떤 순서로 디버깅해?
A. metadata, semantic structure, link/button 역할, image alt, form label, ARIA 상태, keyboard focus 순서로 확인한다.

---

# 16. Best Practice

## 16.1 HTML Attributes Accessibility SEO Best Practice

### [개념]

HTML Attributes Accessibility SEO Best Practice는 HTML 요소의 필수 attribute, 접근성 연결, Form 상태, SEO metadata를 정확하게 작성하는 기준이다.

---

### [핵심]

권장 기준:

- html 요소에 `lang`을 지정한다.
- `charset="UTF-8"`을 지정한다.
- viewport meta를 작성한다.
- 페이지별 고유 title을 작성한다.
- 페이지별 meta description을 작성한다.
- semantic HTML과 heading hierarchy를 유지한다.
- 이동은 `a href`, 동작은 `button`을 사용한다.
- button에는 type을 명시한다.
- icon-only button에는 accessible name을 제공한다.
- image에는 의미에 맞는 alt를 작성한다.
- 장식 이미지는 `alt=""`를 사용한다.
- label과 input을 for/id로 연결한다.
- input에는 적절한 type, name, autocomplete를 사용한다.
- error message는 aria-describedby로 연결한다.
- invalid 상태는 aria-invalid로 전달한다.
- disclosure state는 aria-expanded와 실제 상태를 동기화한다.
- 현재 페이지 link에는 aria-current를 사용한다.
- boolean attribute에 문자열 false를 쓰지 않는다.
- hidden content 내부에 focus가 가지 않게 한다.
- 새 창 외부 링크에는 rel 보안 값을 사용한다.

---

### [실무]

기본 Document Template:

```html
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Festival Detail - FestaPick</title>
    <meta
      name="description"
      content="축제 상세 정보, 일정, 위치, 리뷰를 확인하세요."
    />
  </head>
  <body>
    <a class="skip-link" href="#main-content">Skip to main content</a>

    <header>
      <nav aria-label="Main Navigation">
        <ul>
          <li>
            <a href="/festivals" aria-current="page">Festivals</a>
          </li>
        </ul>
      </nav>
    </header>

    <main id="main-content">
      <h1>Seoul Light Festival</h1>
    </main>
  </body>
</html>
```

Form Field Template:

```html
<div class="form-field">
  <label for="email">Email</label>
  <input
    id="email"
    name="email"
    type="email"
    autocomplete="email"
    required
    aria-describedby="email-help"
  />
  <p id="email-help">Use a valid email address.</p>
</div>
```

Error Field Template:

```html
<div class="form-field">
  <label for="password">Password</label>
  <input
    id="password"
    name="password"
    type="password"
    autocomplete="current-password"
    aria-invalid="true"
    aria-describedby="password-error"
  />
  <p id="password-error">Password is required.</p>
</div>
```

Disclosure Template:

```html
<button type="button" aria-expanded="false" aria-controls="filter-panel">
  Filters
</button>

<div id="filter-panel" hidden>Filter content</div>
```

검수 Checklist:

```md
- [ ] html lang이 문서 언어와 일치하는가?
- [ ] charset과 viewport meta가 있는가?
- [ ] 페이지별 title과 meta description이 고유한가?
- [ ] h1과 heading hierarchy가 논리적인가?
- [ ] link text만으로 이동 목적을 알 수 있는가?
- [ ] 동작 실행에 button을 사용하는가?
- [ ] button type이 명시되어 있는가?
- [ ] icon-only button에 accessible name이 있는가?
- [ ] 의미 있는 image에 적절한 alt가 있는가?
- [ ] 장식 image는 alt=""인가?
- [ ] label for와 input id가 일치하는가?
- [ ] input name과 type이 적절한가?
- [ ] autocomplete가 입력 목적과 맞는가?
- [ ] error message가 aria-describedby로 연결되는가?
- [ ] aria-invalid가 실제 오류 상태와 일치하는가?
- [ ] aria-expanded가 실제 열림 상태와 일치하는가?
- [ ] aria-current가 현재 페이지 link에 적용되는가?
- [ ] boolean attribute를 문자열 false로 쓰지 않았는가?
- [ ] hidden content 내부로 focus가 이동하지 않는가?
- [ ] target="\_blank" 외부 링크에 rel이 있는가?
```

---

### [FAQ]

Q. HTML Attributes Accessibility SEO Best Practice는 뭐야?
A. HTML 요소에 필요한 attribute를 정확히 작성하고 접근성 상태, Form 연결, SEO metadata를 실제 UI와 일치시키는 것이다.

Q. Attribute 검수에서 가장 먼저 볼 것은 뭐야?
A. lang, metadata, link/button 역할, image alt, form label 연결, ARIA 상태를 먼저 확인한다.

Q. Accessibility 검수에서 가장 먼저 볼 것은 뭐야?
A. semantic HTML, keyboard focus, accessible name, label 연결, hidden/focus 상태를 먼저 확인한다.

Q. SEO 검수에서 가장 먼저 볼 것은 뭐야?
A. title, meta description, h1, heading hierarchy, link text, image alt를 먼저 확인한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 HTML Attribute, Accessibility, SEO 기준을 적용해 의미 있고 접근 가능하며 검색 친화적인 HTML 구조를 생성하고 검토하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. HTML Attribute가 뭐야?
A. HTML 요소에 추가 정보를 제공해 의미, 동작, 접근성, SEO를 보완하는 이름-값 구조다.

Q. Attribute는 왜 중요해?
A. 링크 이동, 이미지 설명, Form 연결, 접근성 상태, 검색 노출 정보에 영향을 주기 때문이다.

Q. Attribute 검수에서 가장 먼저 볼 것은?
A. 요소 역할에 필요한 필수 attribute와 접근성 관련 attribute가 실제 상태와 일치하는지 확인한다.

Q. id attribute는 뭐야?
A. 문서 안에서 특정 요소를 고유하게 식별하는 attribute다.

Q. id는 중복되면 안 돼?
A. 맞다. 하나의 문서 안에서 id는 고유해야 한다.

Q. id는 언제 꼭 필요해?
A. label/input 연결, aria-labelledby, aria-describedby, fragment link 대상에 필요하다.

Q. class attribute는 뭐야?
A. CSS styling과 component 구분을 위해 요소에 class name을 부여하는 attribute다.

Q. class는 여러 개 쓸 수 있어?
A. 가능하다. 공백으로 구분해 여러 class를 사용할 수 있다.

Q. React에서는 class를 어떻게 써?
A. JSX에서는 `class`가 아니라 `className`을 사용한다.

Q. title attribute는 뭐야?
A. 요소에 보조 설명을 제공할 수 있는 HTML attribute다.

Q. title만으로 버튼 이름을 제공해도 돼?
A. 권장하지 않는다. icon-only button에는 aria-label이나 숨김 텍스트가 더 안정적이다.

Q. data-\* attribute는 뭐야?
A. HTML 요소에 사용자 정의 데이터를 저장하는 attribute다.

Q. data-state만 있으면 접근성 상태가 전달돼?
A. 아니다. 접근성 상태는 aria-expanded, aria-selected 같은 ARIA attribute가 필요하다.

Q. href attribute는 뭐야?
A. a 요소가 이동할 URL 또는 fragment target을 지정하는 attribute다.

Q. href 없는 a 태그는 link야?
A. 실제 link 의미가 불명확하므로 이동 목적이라면 href가 필요하다.

Q. 버튼처럼 동작하는 a href="#"는 괜찮아?
A. 권장하지 않는다. 동작 실행은 button을 사용한다.

Q. 새 창 링크에는 무엇이 필요해?
A. `target="_blank"`와 함께 `rel="noopener noreferrer"`를 사용하는 것이 좋다.

Q. target="\_blank"는 뭐야?
A. 링크를 새 탭 또는 새 창에서 열도록 지정하는 값이다.

Q. noopener는 왜 필요해?
A. 새로 열린 페이지가 원래 페이지를 제어하지 못하게 하기 위해 필요하다.

Q. alt attribute는 뭐야?
A. 이미지가 보이지 않거나 screen reader가 읽을 때 사용할 대체 텍스트다.

Q. 모든 이미지에 alt가 필요해?
A. img 요소에는 alt가 있어야 한다. 장식 이미지는 `alt=""`를 사용할 수 있다.

Q. 장식 이미지는 alt를 어떻게 해?
A. 빈 alt인 `alt=""`를 사용해 보조 기술이 무시하게 할 수 있다.

Q. img width height attribute는 왜 써?
A. 브라우저가 이미지 공간을 미리 계산해 layout shift를 줄이는 데 도움이 된다.

Q. loading lazy는 언제 써?
A. 초기 화면 아래에 있는 이미지처럼 즉시 필요하지 않은 이미지에 사용한다.

Q. form input의 name은 왜 필요해?
A. form submit이나 FormData에서 해당 입력 값을 식별하는 key로 사용되기 때문이다.

Q. label for는 무엇과 연결돼?
A. input의 id와 연결된다.

Q. radio button들은 name을 어떻게 해야 해?
A. 같은 선택 그룹이면 같은 name을 사용해야 한다.

Q. button type은 왜 명시해야 해?
A. form 내부에서 의도치 않게 submit이 발생하는 것을 막기 위해 중요하다.

Q. 일반 클릭 버튼은 어떤 type을 써?
A. `type="button"`을 사용한다.

Q. form 제출 버튼은 어떤 type을 써?
A. `type="submit"`을 사용한다.

Q. input type은 왜 중요해?
A. validation, mobile keyboard, 자동완성, 접근성에 영향을 주기 때문이다.

Q. required는 뭐야?
A. 해당 form field가 필수 입력임을 나타내는 attribute다.

Q. disabled와 readonly 차이는 뭐야?
A. disabled는 조작 불가이고 submit에서 제외될 수 있으며, readonly는 읽을 수 있지만 수정할 수 없는 상태다.

Q. autocomplete는 뭐야?
A. 브라우저가 입력 필드에 어떤 자동완성 정보를 제공할지 지정하는 attribute다.

Q. 로그인 비밀번호에는 뭐를 써?
A. `autocomplete="current-password"`를 사용한다.

Q. 회원가입 새 비밀번호에는 뭐를 써?
A. `autocomplete="new-password"`를 사용한다.

Q. Boolean Attribute가 뭐야?
A. attribute가 존재하는 것만으로 true 의미를 가지는 HTML attribute다.

Q. disabled="false"는 disabled가 아니야?
A. 아니다. HTML에서는 disabled attribute가 존재하므로 disabled 상태로 해석될 수 있다.

Q. ARIA는 뭐야?
A. HTML만으로 부족한 접근성 이름, 설명, 상태, 관계를 보조 기술에 전달하는 attribute 체계다.

Q. ARIA를 많이 쓰면 접근성이 좋아져?
A. 아니다. native HTML을 우선 사용하고 필요한 경우에만 정확히 써야 한다.

Q. aria-label은 뭐야?
A. 요소에 문자열로 접근성 이름을 제공하는 attribute다.

Q. aria-labelledby는 뭐야?
A. 다른 요소의 텍스트를 참조해 접근성 이름을 제공하는 attribute다.

Q. icon-only button에는 무엇을 써?
A. `aria-label` 또는 visually-hidden 텍스트를 사용할 수 있다.

Q. aria-describedby는 뭐야?
A. 요소에 추가 설명 텍스트를 연결하는 ARIA attribute다.

Q. form error message는 어떻게 연결해?
A. input의 aria-describedby가 error message id를 참조하도록 연결한다.

Q. aria-expanded는 뭐야?
A. trigger가 제어하는 콘텐츠가 열려 있는지 닫혀 있는지 나타내는 attribute다.

Q. aria-controls는 뭐야?
A. trigger가 제어하는 요소의 id를 참조하는 attribute다.

Q. aria-current는 뭐야?
A. navigation이나 step 안에서 현재 항목을 나타내는 ARIA attribute다.

Q. aria-invalid는 뭐야?
A. 입력 값이 유효하지 않은 상태임을 보조 기술에 전달하는 attribute다.

Q. aria-hidden은 언제 써?
A. 장식 아이콘처럼 보조 기술에 읽힐 필요가 없는 요소를 숨길 때 사용한다.

Q. hidden attribute는 뭐야?
A. 요소를 화면과 accessibility tree에서 숨기는 boolean attribute다.

Q. hidden="false"는 표시 상태야?
A. 아니다. hidden attribute가 존재하므로 숨김 상태로 해석될 수 있다.

Q. lang attribute는 뭐야?
A. 문서나 요소의 언어를 지정하는 attribute다.

Q. 한국어 페이지에는 어떤 lang을 써?
A. `lang="ko"`를 사용한다.

Q. charset meta는 왜 필요해?
A. 문서 문자 인코딩을 지정해 한글 깨짐 같은 문제를 줄이기 위해 필요하다.

Q. viewport meta는 왜 필요해?
A. 모바일에서 페이지가 올바른 viewport 폭으로 표시되도록 하기 위해 필요하다.

Q. title 태그는 왜 중요해?
A. 브라우저 탭, 검색 결과, screen reader 문맥에 영향을 주기 때문이다.

Q. SEO Basics에서 가장 중요한 HTML 요소는?
A. title, meta description, h1, semantic landmark, link text, image alt가 중요하다.

Q. Click here 같은 링크 텍스트는 왜 안 좋아?
A. 링크 텍스트만으로 이동 목적을 알 수 없기 때문이다.

Q. Accessibility가 뭐야?
A. 다양한 사용자가 웹 콘텐츠와 기능을 인식하고 조작하고 이해할 수 있게 만드는 기준이다.

Q. Accessibility에서 HTML이 중요한 이유는?
A. semantic HTML 자체가 보조 기술에 의미와 역할을 전달하기 때문이다.

Q. CSS도 접근성에 영향을 줘?
A. 그렇다. focus-visible, contrast, hidden 상태, responsive layout은 CSS와 직접 연결된다.

Q. Keyboard Accessibility는 뭐야?
A. 마우스 없이 keyboard만으로 웹 UI를 탐색하고 조작할 수 있게 하는 기준이다.

Q. div에 onClick을 붙이면 button과 같아?
A. 아니다. keyboard 동작과 semantic role이 부족하므로 button을 사용하는 것이 좋다.

Q. Skip Link는 왜 필요해?
A. keyboard 사용자가 반복 navigation을 건너뛰고 main content로 이동할 수 있게 도와준다.

Q. Attribute Bug에서 가장 흔한 문제는 뭐야?
A. label/id 연결 오류, button type 누락, aria 상태 불일치, alt 누락이 흔하다.

Q. id와 class 차이는 뭐야?
A. id는 문서 내 고유 식별자이고 class는 여러 요소에 공유 가능한 styling/grouping 이름이다.

Q. alt와 title 차이는 뭐야?
A. alt는 이미지 대체 텍스트이고 title은 요소에 대한 보조 설명이다.

Q. aria-label과 aria-labelledby 차이는?
A. aria-label은 문자열로 이름을 제공하고 aria-labelledby는 다른 요소의 텍스트를 이름으로 참조한다.

Q. aria-describedby는 이름이야?
A. 아니다. 이름이 아니라 추가 설명이다.

Q. HTML Attribute에서 가장 흔한 실수는 뭐야?
A. button type 누락, alt 누락, label/id 연결 오류, ARIA 상태 불일치가 흔하다.

Q. SEO에서 가장 흔한 실수는 뭐야?
A. 모든 페이지 title이 같거나 heading hierarchy가 불명확하고 link text가 의미 없는 것이다.

Q. HTML Attributes Accessibility SEO Best Practice는 뭐야?
A. HTML 요소에 필요한 attribute를 정확히 작성하고 접근성 상태, Form 연결, SEO metadata를 실제 UI와 일치시키는 것이다.

Q. Attribute 검수에서 가장 먼저 볼 것은 뭐야?
A. lang, metadata, link/button 역할, image alt, form label 연결, ARIA 상태를 먼저 확인한다.

Q. 이 문서의 최종 목적은 뭐야?
A. Frontend Agent가 HTML Attribute, Accessibility, SEO 기준을 적용해 의미 있고 접근 가능하며 검색 친화적인 HTML 구조를 생성하고 검토하게 만드는 것이다.
