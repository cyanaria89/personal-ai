# Frontend Accessibility Part02 - Semantic HTML Landmark Heading

---

# 1. Semantic HTML

## 1.1 Semantic HTML First

### [개념]

Semantic HTML은 HTML 요소를 의미에 맞게 사용하는 방식이다.

Frontend Accessibility의 기본은 ARIA를 많이 붙이는 것이 아니라 HTML 자체가 올바른 의미를 갖도록 작성하는 것이다.

Semantic HTML은 브라우저, 스크린 리더, Testing Library, 검색 엔진, 개발자 도구가 UI 구조를 더 정확히 이해하게 만든다.

---

### [핵심]

Semantic HTML 핵심 요소:

- `button`
- `a`
- `input`
- `label`
- `form`
- `fieldset`
- `legend`
- `header`
- `nav`
- `main`
- `section`
- `article`
- `aside`
- `footer`
- `ul`
- `ol`
- `li`
- `table`
- `thead`
- `tbody`
- `th`
- `td`

Semantic HTML 우선순위:

1. Native Element 사용
2. 의미 없는 `div`, `span` 최소화
3. ARIA는 부족한 의미 보완
4. role 사용 시 keyboard 동작 일치
5. Testing Library `getByRole`로 검증 가능해야 함

---

### [실무]

좋은 예:

```jsx
<button type="button" onClick={onOpen}>
  메뉴 열기
</button>
```

나쁜 예:

```jsx
<div onClick={onOpen}>메뉴 열기</div>
```

실무 기준:

- 클릭 액션은 `button`
- 페이지 이동은 `a` 또는 React Router `Link`
- Form 입력은 `input`, `select`, `textarea`
- 입력 설명은 `label`
- 반복 목록은 `ul`, `ol`, `li`
- 표 데이터는 `table`
- 페이지 주요 콘텐츠는 `main`
- 네비게이션 영역은 `nav`
- 독립 콘텐츠는 `article`
- 관련 콘텐츠 묶음은 `section`
- 부가 정보는 `aside`
- 하단 정보는 `footer`

Review Agent는 `div onClick`, `span onClick`, 의미 없는 wrapper 남용을 우선 탐지한다.

---

### [FAQ]

Q. Semantic HTML이 뭐야?
A. HTML 요소를 의미에 맞게 사용하는 것이다. button, nav, main, label 같은 태그를 역할에 맞게 사용한다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

Q. div에 onClick을 붙이면 안 돼?
A. 가능은 하지만 keyboard 접근성과 의미가 부족하다. 클릭 액션은 button을 사용하는 것이 좋다.

Q. Semantic HTML이 Testing Library와도 관련 있어?
A. 그렇다. getByRole, getByLabelText는 semantic 구조와 accessible name을 기반으로 요소를 찾는다.

---

# 2. Button and Link Semantics

## 2.1 Button vs Link

### [개념]

Button과 Link는 역할이 다르다.

Button은 현재 화면이나 애플리케이션 상태를 변경하는 액션을 실행한다.

Link는 다른 페이지, 다른 위치, 다른 URL로 이동한다.

---

### [핵심]

Button 기준:

- 저장
- 삭제
- 등록
- 취소
- 제출
- 모달 열기
- 드롭다운 열기
- 탭 전환
- 좋아요 토글
- 필터 초기화

Link 기준:

- 상세 페이지 이동
- 목록 페이지 이동
- 외부 사이트 이동
- 문서 위치 이동
- 라우트 변경
- 앵커 이동

비교:

| 구분         | Button            | Link               |
| ------------ | ----------------- | ------------------ |
| 목적         | 액션 실행         | 페이지 / 위치 이동 |
| 상태 변경    | 가능              | 일반적으로 지양    |
| 키보드       | Enter / Space     | Enter              |
| HTML         | `button`          | `a`                |
| React Router | 액션에는 `button` | 이동에는 `Link`    |

---

### [실무]

Button 예:

```jsx
<button type="button" onClick={onDelete}>
  삭제
</button>
```

Link 예:

```jsx
<Link to={`/festivals/${festivalId}`}>축제 상세 보기</Link>
```

나쁜 예:

```jsx
<a href="#" onClick={onDelete}>
  삭제
</a>
```

주의:

- 삭제, 저장, 좋아요, 모달 열기는 `button`
- 상세 페이지 이동, 목록 이동은 `Link`
- `button`으로 이동 처리할 수는 있지만 단순 이동이면 `Link`가 더 적합
- `a` 태그에 `href="#"` 후 action 실행하는 패턴 지양
- Form 내부 `button`은 `type` 명시
- Icon Button은 `aria-label` 필요

---

### [FAQ]

Q. Button과 Link 차이는?
A. Button은 액션 실행이고 Link는 페이지나 위치 이동이다.

Q. 상세 페이지 이동 버튼은 button이야 Link야?
A. 단순 페이지 이동이라면 Link가 적합하다.

Q. 삭제는 Link로 만들어도 돼?
A. 권장하지 않는다. 삭제는 현재 상태를 변경하는 액션이므로 button이 적합하다.

Q. 모달 열기는 Button이야 Link야?
A. 현재 화면에서 UI 상태를 변경하는 액션이므로 button이 적합하다.

---

## 2.2 Button Type Rules

### [개념]

`button` 요소는 Form 내부에서 기본적으로 submit 동작을 가질 수 있다.

React 공통 Button Component는 의도하지 않은 submit을 방지하기 위해 `type`을 명확히 관리해야 한다.

---

### [핵심]

Button type:

- `type="button"`
- `type="submit"`
- `type="reset"`

실무 기본값:

- 일반 버튼: `type="button"`
- Form 제출 버튼: `type="submit"`
- reset 버튼: 명확한 의도가 있을 때만 사용

---

### [실무]

일반 버튼:

```jsx
<button type="button" onClick={onOpen}>
  열기
</button>
```

제출 버튼:

```jsx
<button type="submit">저장</button>
```

공통 Button Component 예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({ type = "button", children, onClick }: ButtonProps) {
  return (
    <button type={type} onClick={onClick}>
      {children}
    </button>
  );
}
```

주의:

- Form 내부 취소 버튼은 `type="button"` 사용
- Form 내부 모달 열기 버튼도 `type="button"` 사용
- 공통 Button의 기본 type은 `"button"` 권장
- 제출 버튼만 명시적으로 `type="submit"` 전달

---

### [FAQ]

Q. Button에 type을 꼭 써야 해?
A. Form 안에서는 기본 submit 동작 때문에 type을 명시하는 것이 안전하다.

Q. 공통 Button Component 기본 type은 뭐가 좋아?
A. 의도하지 않은 submit을 막기 위해 `type="button"`을 기본값으로 두는 것이 좋다.

Q. Form 제출 버튼은 type을 뭘로 해야 해?
A. `type="submit"`을 사용한다.

Q. 취소 버튼이 Form을 제출해버리면 왜 그래?
A. Form 내부 button의 기본 동작이 submit일 수 있기 때문이다. 취소 버튼에는 `type="button"`을 명시한다.

---

# 3. Landmark Structure

## 3.1 Landmark Basics

### [개념]

Landmark는 페이지의 주요 영역을 의미 있는 구조로 나누는 HTML 요소 또는 role이다.

스크린 리더 사용자는 Landmark를 통해 페이지의 주요 영역으로 빠르게 이동할 수 있다.

---

### [핵심]

주요 Landmark:

- `header`
- `nav`
- `main`
- `aside`
- `footer`
- `form`
- `search`
- `banner`
- `contentinfo`

Landmark 기본 기준:

- 페이지 주요 콘텐츠는 `main`
- 네비게이션 영역은 `nav`
- 페이지 상단 영역은 `header`
- 페이지 하단 영역은 `footer`
- 보조 콘텐츠는 `aside`
- 여러 `nav`는 accessible name으로 구분
- `main`은 페이지에 하나를 기본으로 함

---

### [실무]

기본 Layout 예:

```jsx
function AppLayout({ children }) {
  return (
    <>
      <header>
        <nav aria-label="주요 메뉴">...</nav>
      </header>

      <main>{children}</main>

      <footer>...</footer>
    </>
  );
}
```

여러 nav 예:

```jsx
<header>
  <nav aria-label="주요 메뉴">
    ...
  </nav>
</header>

<footer>
  <nav aria-label="하단 메뉴">
    ...
  </nav>
</footer>
```

실무 기준:

- 앱 전체 layout에는 `header`, `main`, `footer` 구조 권장
- 페이지 본문은 `main` 안에 배치
- `main` 내부에 페이지별 `h1` 배치 권장
- `nav`가 여러 개면 `aria-label`로 구분
- 의미 없는 `role="main"`보다 `main` 태그 우선
- `header`, `footer`를 단순 디자인 wrapper로만 남용하지 않음

---

### [FAQ]

Q. Landmark가 뭐야?
A. 페이지의 주요 영역을 의미 있게 나누는 구조다. header, nav, main, footer 같은 요소가 대표적이다.

Q. main 태그는 꼭 필요해?
A. 페이지 주요 콘텐츠를 나타내기 위해 사용하는 것이 좋다.

Q. nav가 여러 개면 어떻게 해?
A. `aria-label`로 “주요 메뉴”, “하단 메뉴”처럼 구분하는 것이 좋다.

Q. div에 role="main"을 붙여도 돼?
A. 가능하지만 가능하면 native `main` 태그를 사용하는 것이 더 명확하다.

---

## 3.2 Main Content Rules

### [개념]

`main`은 페이지의 핵심 콘텐츠 영역을 나타내는 Landmark다.

반복되는 header, navigation, footer를 제외한 현재 페이지의 고유한 콘텐츠를 담는다.

---

### [핵심]

`main` 기준:

- 페이지당 하나를 기본으로 사용
- 현재 페이지의 고유 콘텐츠 포함
- header / nav / footer 반복 영역 제외
- 페이지 제목 `h1` 포함 권장
- route 변경 시 focus 이동 대상 후보
- Skip Link 대상 후보

---

### [실무]

페이지 구조 예:

```jsx
function FestivalListPage() {
  return (
    <main id="main-content">
      <h1>축제 목록</h1>

      <section aria-labelledby="popular-festival-title">
        <h2 id="popular-festival-title">인기 축제</h2>
        ...
      </section>
    </main>
  );
}
```

Skip Link 연결 예:

```jsx
<a href="#main-content" className="skip-link">
  본문으로 건너뛰기
</a>

<main id="main-content">
  <h1>축제 목록</h1>
</main>
```

실무 기준:

- SPA에서도 route별 주요 콘텐츠를 `main`으로 감쌈
- `main` 안에 페이지 핵심 제목 배치
- Skip Link가 있다면 `main` id와 연결
- route 이동 후 focus를 `main` 또는 `h1`로 이동하는 전략 검토
- layout 전체에 `main`을 한 번 두고 페이지 children을 넣는 방식 가능

---

### [FAQ]

Q. SPA에서도 main이 필요해?
A. 필요하다. SPA도 사용자가 인식하는 페이지 구조가 있으므로 주요 콘텐츠 영역을 main으로 제공하는 것이 좋다.

Q. main은 여러 개 있어도 돼?
A. 일반적인 앱 페이지에서는 하나만 사용하는 것이 명확하다.

Q. Skip Link는 main과 연결해?
A. 보통 본문으로 건너뛰기 링크를 main 영역과 연결한다.

Q. route 이동 후 focus는 어디로 가야 해?
A. 페이지 제목 h1 또는 main 영역으로 focus 이동을 검토할 수 있다.

---

## 3.3 Navigation Landmark Rules

### [개념]

`nav`는 주요 탐색 링크 묶음을 나타내는 Landmark다.

스크린 리더 사용자는 `nav` Landmark를 통해 메뉴 영역을 빠르게 찾을 수 있다.

---

### [핵심]

`nav` 사용 대상:

- 주요 메뉴
- 하단 메뉴
- 사이드 메뉴
- Breadcrumb
- Pagination
- 탭이 아닌 페이지 이동 메뉴

`nav` 기준:

- 여러 nav는 `aria-label`로 구분
- 링크 목록은 `ul/li` 사용 고려
- 현재 페이지는 `aria-current="page"` 사용
- 버튼 액션을 nav link처럼 넣지 않음
- 메뉴명은 목적지를 이해할 수 있게 작성

---

### [실무]

주요 메뉴 예:

```jsx
<nav aria-label="주요 메뉴">
  <ul>
    <li>
      <NavLink to="/festivals">축제</NavLink>
    </li>
    <li>
      <NavLink to="/calendar">캘린더</NavLink>
    </li>
  </ul>
</nav>
```

현재 페이지 표시 예:

```jsx
<NavLink
  to="/calendar"
  aria-current={({ isActive }) => (isActive ? "page" : undefined)}
>
  캘린더
</NavLink>
```

Breadcrumb 예:

```jsx
<nav aria-label="Breadcrumb">
  <ol>
    <li>
      <Link to="/">홈</Link>
    </li>
    <li>
      <Link to="/festivals">축제</Link>
    </li>
    <li aria-current="page">축제 상세</li>
  </ol>
</nav>
```

실무 기준:

- 반복 메뉴는 list 구조 사용 권장
- 현재 위치는 시각적 표시와 `aria-current` 함께 제공
- Dropdown menu와 site navigation 역할 구분
- `nav` 안에는 주요 탐색 링크 중심으로 배치
- 모든 링크 텍스트는 목적지를 이해할 수 있어야 함

---

### [FAQ]

Q. 모든 링크 묶음에 nav를 써야 해?
A. 주요 탐색 영역에 사용한다. 단순 카드 내부 링크 묶음까지 모두 nav로 감쌀 필요는 없다.

Q. 현재 메뉴는 어떻게 표시해?
A. 시각적 표시와 함께 `aria-current="page"`를 사용할 수 있다.

Q. Breadcrumb도 nav야?
A. 페이지 위치를 탐색하는 링크 묶음이므로 nav와 aria-label을 사용할 수 있다.

Q. nav가 여러 개면 문제야?
A. 문제는 아니지만 `aria-label`로 각 nav의 목적을 구분하는 것이 좋다.

---

# 4. Heading Structure

## 4.1 Heading Hierarchy

### [개념]

Heading Structure는 `h1` ~ `h6`을 사용해 페이지 콘텐츠 계층을 표현하는 기준이다.

Heading은 글자 크기 조정용 요소가 아니라 문서 구조를 표현하는 요소다.

---

### [핵심]

Heading 기준:

- `h1`은 페이지 핵심 제목
- `h2`는 주요 Section 제목
- `h3`는 `h2` 내부 하위 Section 제목
- heading level skip 주의
- 스타일 목적 heading 사용 금지
- card title heading 기준 통일
- modal title heading 고려
- visually hidden heading 활용 가능

---

### [실무]

좋은 구조:

```html
<h1>축제 목록</h1>

<section>
  <h2>인기 축제</h2>

  <article>
    <h3>봄꽃 축제</h3>
    <p>서울에서 열리는 봄꽃 축제입니다.</p>
  </article>
</section>

<section>
  <h2>지역별 축제</h2>
  ...
</section>
```

나쁜 구조:

```html
<h3>축제 목록</h3>
<h1>인기 축제</h1>
<h5>봄꽃 축제</h5>
```

실무 기준:

- 페이지에는 명확한 `h1` 제공
- 시각적 크기는 CSS로 조정
- `h2` 없이 `h4`로 건너뛰는 구조 지양
- 카드 목록 제목은 `h2`, 카드 제목은 `h3`처럼 기준 통일
- Modal 제목은 `h2` 또는 적절한 heading으로 제공 가능
- 시각적으로 제목이 없어도 스크린 리더용 heading을 고려할 수 있음

---

### [FAQ]

Q. h1은 여러 개 있어도 돼?
A. HTML상 가능하지만 일반적인 앱 페이지에서는 페이지 핵심 제목 하나를 h1로 두는 방식이 명확하다.

Q. 글자 크기를 줄이려고 h4를 써도 돼?
A. 권장하지 않는다. heading은 문서 구조 기준이고 크기는 CSS로 조정한다.

Q. heading level을 건너뛰면 안 돼?
A. 가능한 한 자연스러운 계층을 유지하는 것이 좋다. 구조 이해가 어려워질 수 있다.

Q. 카드 제목도 heading으로 해야 해?
A. 카드가 독립 콘텐츠라면 heading을 고려할 수 있다. 목록 구조와 페이지 heading 계층에 맞춰 기준을 통일한다.

---

## 4.2 Page Title Rules

### [개념]

Page Title은 현재 화면의 핵심 목적을 나타내는 제목이다.

사용자는 Page Title을 통해 현재 위치와 페이지 목적을 이해한다.

---

### [핵심]

Page Title 기준:

- route별 `h1` 제공
- 페이지 목적을 명확히 표현
- 너무 포괄적인 제목 지양
- `main` 내부 상단 배치 권장
- route 이동 후 focus 대상 후보
- 브라우저 title과 의미 일치 권장

---

### [실무]

좋은 예:

```jsx
<main>
  <h1>축제 검색</h1>
  <FestivalSearchForm />
</main>
```

나쁜 예:

```jsx
<main>
  <h1>페이지</h1>
  <FestivalSearchForm />
</main>
```

실무 Page Title 예:

| Page                 | 권장 h1     |
| -------------------- | ----------- |
| Login Page           | 로그인      |
| Signup Page          | 회원가입    |
| Festival List Page   | 축제 목록   |
| Festival Detail Page | 봄꽃 축제   |
| Calendar Page        | 축제 캘린더 |
| My Page              | 내 정보     |
| Admin User Page      | 사용자 관리 |

실무 기준:

- 페이지당 핵심 h1을 명확히 작성
- Detail Page는 대상 이름을 h1로 사용 가능
- 디자인상 h1이 보이기 어렵다면 visually hidden heading 검토
- route 이동 후 h1 focus 또는 announce 전략 검토

---

### [FAQ]

Q. 페이지마다 h1이 필요해?
A. 현재 화면의 핵심 목적을 전달하기 위해 route별 h1을 두는 것이 좋다.

Q. 상세 페이지 h1은 뭘로 해?
A. 일반적으로 상세 대상의 이름을 h1로 사용할 수 있다.

Q. h1을 숨겨도 돼?
A. 시각적으로 숨기더라도 스크린 리더가 읽을 수 있는 방식으로 제공할 수 있다.

Q. 브라우저 title과 h1은 같아야 해?
A. 반드시 같을 필요는 없지만 사용자가 현재 위치를 이해할 수 있도록 의미가 일치하는 것이 좋다.

---

## 4.3 Section Heading Rules

### [개념]

Section Heading은 페이지 내부 콘텐츠 블록의 목적을 설명하는 제목이다.

`section`은 보통 해당 영역을 설명하는 heading과 함께 사용하는 것이 좋다.

---

### [핵심]

Section Heading 기준:

- `section`에는 의미 있는 heading 권장
- `aria-labelledby`로 section과 heading 연결 가능
- 반복 영역은 heading 구조 통일
- 제목 없는 단순 wrapper에는 `div` 사용 가능
- 시각적 구분만 필요한 경우 heading 남용 지양

---

### [실무]

Section 예:

```jsx
<section aria-labelledby="popular-festival-title">
  <h2 id="popular-festival-title">인기 축제</h2>
  <FestivalCardList />
</section>
```

제목 없는 wrapper 예:

```jsx
<div className="page-layout">
  <FestivalFilter />
  <FestivalList />
</div>
```

실무 기준:

- `section`은 문서 구조상 의미 있는 영역에 사용
- 단순 스타일 wrapper는 `div` 사용
- 여러 `section`은 `h2`로 주요 영역을 나눔
- `section` 제목이 시각적으로 필요 없으면 visually hidden heading 고려
- `aria-labelledby`로 section 이름 제공 가능

---

### [FAQ]

Q. 모든 div를 section으로 바꾸면 좋아?
A. 아니다. 의미 있는 콘텐츠 구역일 때 section을 사용하고 단순 wrapper는 div가 적합하다.

Q. section에는 heading이 꼭 필요해?
A. 의미 있는 section이라면 heading을 제공하는 것이 좋다.

Q. aria-labelledby는 section에도 쓸 수 있어?
A. 그렇다. section의 이름을 내부 heading과 연결할 수 있다.

Q. 제목이 화면에 필요 없으면 어떻게 해?
A. visually hidden heading을 사용해 보조기술에는 구조를 제공할 수 있다.

---

# 5. Article and Section

## 5.1 Article Rules

### [개념]

`article`은 독립적으로 배포하거나 재사용할 수 있는 콘텐츠 단위를 나타낸다.

카드, 게시글, 리뷰, 축제 항목처럼 하나의 독립 콘텐츠로 볼 수 있는 UI에 사용할 수 있다.

---

### [핵심]

`article` 사용 대상:

- 게시글 카드
- 축제 카드
- 리뷰 항목
- 댓글 항목
- 공지 항목
- 뉴스 항목
- 블로그 글
- 상품 카드

`article` 기준:

- 독립 콘텐츠 단위
- 자체 heading 권장
- 목록 안에 포함 가능
- 카드 UI에 적합할 수 있음
- 단순 레이아웃 wrapper로 사용 금지

---

### [실무]

축제 카드 예:

```jsx
<li>
  <article>
    <h3>{festival.title}</h3>
    <p>{festival.regionName}</p>
    <Link to={`/festivals/${festival.id}`}>{festival.title} 상세 보기</Link>
  </article>
</li>
```

리뷰 항목 예:

```jsx
<article aria-labelledby={`review-${review.id}-title`}>
  <h3 id={`review-${review.id}-title`}>{review.authorName}의 리뷰</h3>
  <p>{review.content}</p>
</article>
```

실무 기준:

- 카드 목록은 `ul/li` + `article` 조합 검토
- article 내부 제목 제공
- 반복 카드 제목 heading level 통일
- “자세히 보기” 링크는 대상 이름 포함 권장
- article을 클릭 가능한 전체 카드로 만들 때 keyboard와 link semantics 주의

---

### [FAQ]

Q. 카드 UI에는 article을 써도 돼?
A. 카드가 독립 콘텐츠 단위라면 article을 사용할 수 있다.

Q. article 안에는 heading이 필요해?
A. 독립 콘텐츠를 식별할 수 있도록 heading을 제공하는 것이 좋다.

Q. article과 section 차이는?
A. article은 독립 콘텐츠 단위이고 section은 문서 내 주제별 구역이다.

Q. 카드 전체 클릭은 어떻게 접근성 있게 처리해?
A. 단순 이동이면 카드 안에 명확한 Link를 제공하고 keyboard focus와 link text를 검토한다.

---

## 5.2 Section vs Div

### [개념]

`section`은 의미 있는 주제별 콘텐츠 구역이고 `div`는 의미 없는 일반 컨테이너다.

모든 레이아웃 wrapper를 `section`으로 바꾸는 것은 Semantic HTML이 아니다.

---

### [핵심]

`section` 사용:

- 페이지 주요 콘텐츠 구역
- heading으로 설명 가능한 영역
- 검색 결과 영역
- 인기 목록 영역
- 설정 그룹 영역
- 상세 정보 영역

`div` 사용:

- 스타일 wrapper
- grid / flex layout wrapper
- spacing wrapper
- animation wrapper
- 의미 없는 grouping
- component internal layout

---

### [실무]

section이 적합한 예:

```jsx
<section aria-labelledby="search-result-title">
  <h2 id="search-result-title">검색 결과</h2>
  <FestivalList />
</section>
```

div가 적합한 예:

```jsx
<div className="card-grid">
  {items.map((item) => (
    <FestivalCard key={item.id} item={item} />
  ))}
</div>
```

실무 기준:

- 영역을 제목으로 설명할 수 있으면 `section` 검토
- 단순 CSS layout이면 `div`
- section에는 heading 제공 권장
- 의미 없는 section 남발 금지
- 접근성 구조와 디자인 wrapper를 구분

---

### [FAQ]

Q. section을 많이 쓰면 접근성이 좋아져?
A. 아니다. 의미 있는 구역에만 사용해야 한다.

Q. 단순 스타일 wrapper는 뭘 써?
A. 의미가 필요 없다면 div가 적합하다.

Q. section과 article 중 뭘 써야 해?
A. 독립 콘텐츠 단위면 article, 주제별 구역이면 section을 사용한다.

Q. 검색 결과 영역은 section이 적합해?
A. 검색 결과라는 의미 있는 구역이므로 heading과 함께 section을 사용할 수 있다.

---

# 6. List Semantics

## 6.1 List Structure

### [개념]

List Semantics는 반복되는 항목을 `ul`, `ol`, `li` 구조로 표현하는 기준이다.

반복되는 카드, 메뉴, 검색 결과, 댓글, 리뷰는 목록 구조로 표현할 수 있다.

---

### [핵심]

List 사용 대상:

- 메뉴 목록
- 카드 목록
- 검색 결과 목록
- 리뷰 목록
- 댓글 목록
- 알림 목록
- 필터 옵션 목록
- 단계별 순서 목록

List 기준:

- 순서가 중요 없으면 `ul`
- 순서가 중요하면 `ol`
- 각 항목은 `li`
- 카드 내부는 `article` 사용 가능
- 빈 목록은 Empty State 제공
- key는 안정적인 id 사용

---

### [실무]

카드 목록 예:

```jsx
<ul>
  {festivals.map((festival) => (
    <li key={festival.festivalId}>
      <article>
        <h3>{festival.title}</h3>
        <p>{festival.regionName}</p>
      </article>
    </li>
  ))}
</ul>
```

순서 목록 예:

```jsx
<ol>
  <li>이메일 입력</li>
  <li>인증 코드 확인</li>
  <li>비밀번호 재설정</li>
</ol>
```

실무 기준:

- 반복 UI는 list 구조 검토
- list marker 제거는 CSS로 처리 가능
- list semantics를 제거하지 않도록 주의
- 카드 grid도 의미상 목록이면 `ul/li` 가능
- 빈 배열만 렌더링하지 말고 Empty State 제공
- “자세히 보기” 링크 반복 시 대상 이름 포함

---

### [FAQ]

Q. 카드 목록은 ul/li로 감싸야 해?
A. 반복되는 항목 목록이라면 ul/li를 사용하는 것이 의미상 좋다.

Q. CSS grid를 쓰면 ul/li를 못 써?
A. 아니다. ul/li에도 CSS grid를 적용할 수 있다.

Q. 순위 목록은 ul이야 ol이야?
A. 순서나 순위가 의미 있으면 ol이 적합하다.

Q. 빈 목록이면 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. Empty State를 제공해 현재 상태를 설명해야 한다.

---

## 6.2 Repeated Link Text

### [개념]

Repeated Link Text는 같은 링크 텍스트가 목록에서 반복되어 목적지가 모호해지는 문제다.

스크린 리더 사용자는 링크만 모아 탐색할 수 있으므로 “자세히 보기”가 반복되면 각 링크의 목적지를 알기 어렵다.

---

### [핵심]

문제 링크 텍스트:

- 자세히 보기
- 더보기
- 클릭
- 여기를 클릭
- 이동
- 보기

개선 방식:

- 대상 이름 포함
- aria-label로 목적지 구체화
- 카드 제목과 링크 관계 명확화
- visible text 우선
- 숨김 텍스트 활용 가능

---

### [실무]

나쁜 예:

```jsx
<Link to={`/festivals/${festival.id}`}>자세히 보기</Link>
```

좋은 예:

```jsx
<Link to={`/festivals/${festival.id}`}>{festival.title} 자세히 보기</Link>
```

aria-label 보완 예:

```jsx
<Link
  to={`/festivals/${festival.id}`}
  aria-label={`${festival.title} 자세히 보기`}
>
  자세히 보기
</Link>
```

실무 기준:

- 링크 텍스트만 읽어도 목적지를 알 수 있어야 함
- visible text로 구체화하는 방식 우선
- 디자인상 짧은 문구가 필요하면 `aria-label` 검토
- 같은 이름의 버튼 / 링크 반복 시 context 제공
- 카드 전체 링크 패턴은 중복 focus와 중복 링크 주의

---

### [FAQ]

Q. “자세히 보기” 링크를 반복해서 써도 돼?
A. 가능하지만 스크린 리더에서는 목적지가 모호할 수 있다. 대상 이름을 포함하는 것이 좋다.

Q. aria-label로 링크 목적지를 보완해도 돼?
A. 가능하다. 다만 visible text와 의미가 충돌하지 않게 해야 한다.

Q. 링크 텍스트는 어떻게 써야 해?
A. 링크만 읽어도 이동 목적지를 이해할 수 있게 작성한다.

Q. “여기를 클릭”은 왜 안 좋아?
A. 링크 목적지가 설명되지 않아 스크린 리더 사용자와 키보드 사용자에게 불명확하다.

---

# 7. Table Semantics

## 7.1 Table Structure

### [개념]

Table Semantics는 행과 열 관계가 있는 데이터를 `table` 구조로 명확히 전달하는 기준이다.

표 데이터는 `div` grid가 아니라 `table`, `thead`, `tbody`, `th`, `td`를 사용해야 관계를 보조기술에 전달할 수 있다.

---

### [핵심]

Table 요소:

- `table`
- `caption`
- `thead`
- `tbody`
- `tr`
- `th`
- `td`
- `scope`
- row header
- column header

Table 사용 대상:

- 사용자 목록
- 결제 내역
- 주문 내역
- 관리자 데이터
- 통계 데이터
- 비교 데이터
- 행 / 열 관계가 중요한 정보

---

### [실무]

기본 예:

```jsx
<table>
  <caption>사용자 목록</caption>
  <thead>
    <tr>
      <th scope="col">닉네임</th>
      <th scope="col">권한</th>
      <th scope="col">가입일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>jun</td>
      <td>ROLE_USER</td>
      <td>2026-07-06</td>
    </tr>
  </tbody>
</table>
```

행 제목 예:

```jsx
<table>
  <caption>월별 결제 금액</caption>
  <tbody>
    <tr>
      <th scope="row">2026년 1월</th>
      <td>120,000원</td>
    </tr>
  </tbody>
</table>
```

실무 기준:

- 행과 열 관계가 있으면 `table` 사용
- `th`에는 `scope="col"` 또는 `scope="row"` 제공
- 복잡한 표는 `caption` 제공 고려
- layout 목적 table 사용 지양
- 모바일에서도 데이터 관계가 깨지지 않게 설계
- 정렬 가능한 header는 정렬 상태 전달 고려

---

### [FAQ]

Q. 표를 div로 만들어도 돼?
A. 행과 열 관계가 중요한 데이터는 table 요소를 사용하는 것이 접근성에 좋다.

Q. caption은 꼭 필요해?
A. 복잡한 표일수록 caption이 표의 목적을 이해하는 데 도움이 된다.

Q. th의 scope는 왜 필요해?
A. header가 열 기준인지 행 기준인지 명확히 전달할 수 있다.

Q. layout용 table을 써도 돼?
A. 권장하지 않는다. 레이아웃은 CSS로 처리하고 table은 표 데이터에 사용한다.

---

## 7.2 Sortable Table Header

### [개념]

Sortable Table Header는 사용자가 열 기준으로 데이터를 정렬할 수 있는 표 header다.

정렬 가능한 header는 버튼 역할과 현재 정렬 상태를 명확히 전달해야 한다.

---

### [핵심]

Sortable Header 기준:

- 정렬 액션은 `button`
- header 안에 button 배치 가능
- 현재 정렬 상태 제공
- `aria-sort` 고려
- 정렬 방향 텍스트 제공
- icon only 상태 지양

---

### [실무]

정렬 header 예:

```jsx
<th scope="col" aria-sort="ascending">
  <button type="button" onClick={() => onSort("createdAt")}>
    가입일 오름차순 정렬
  </button>
</th>
```

정렬 상태 값:

```text
aria-sort="ascending"
aria-sort="descending"
aria-sort="none"
aria-sort="other"
```

실무 기준:

- 정렬 클릭 대상은 `button`
- 정렬 상태는 시각적 아이콘만으로 전달하지 않음
- `aria-sort`는 현재 정렬된 column에 사용
- 버튼 accessible name에 정렬 방향 포함 가능
- 정렬 후 focus가 유지되는지 확인

---

### [FAQ]

Q. 정렬 가능한 table header는 th만 클릭하면 돼?
A. 클릭 액션이 있으므로 th 내부에 button을 두는 방식이 명확하다.

Q. 정렬 방향은 아이콘만 보여주면 돼?
A. 권장하지 않는다. 텍스트나 aria-sort로 상태를 함께 전달해야 한다.

Q. aria-sort는 어디에 써?
A. 정렬 상태가 있는 column header에 사용할 수 있다.

Q. 정렬 버튼은 Link야 Button이야?
A. 현재 표 상태를 변경하는 액션이므로 button이 적합하다.

---

# 8. Image Semantics

## 8.1 Informative vs Decorative Image

### [개념]

Image Semantics는 이미지가 정보를 전달하는지, 장식 목적인지에 따라 alt text를 결정하는 기준이다.

이미지 alt는 이미지를 자세히 묘사하는 것이 아니라 이미지의 목적을 텍스트로 전달하는 것이다.

---

### [핵심]

이미지 유형:

- informative image
- decorative image
- functional image
- complex image
- avatar
- thumbnail
- icon
- chart image

Alt 기준:

- 정보 이미지: 의미 있는 `alt`
- 장식 이미지: `alt=""`
- 링크 이미지: 링크 목적 포함
- 아이콘 버튼 내부 아이콘: `aria-hidden`
- 복잡한 차트: 별도 설명 제공

---

### [실무]

정보 이미지:

```jsx
<img src="/festival.jpg" alt="봄꽃 축제 행사장 전경" />
```

장식 이미지:

```jsx
<img src="/decoration.png" alt="" />
```

링크 이미지:

```jsx
<Link to="/festivals/1">
  <img src="/festival.jpg" alt="봄꽃 축제 상세 보기" />
</Link>
```

주변 텍스트와 중복되는 카드 이미지:

```jsx
<article>
  <img src="/festival.jpg" alt="" />
  <h3>봄꽃 축제</h3>
  <p>서울에서 열리는 봄꽃 축제입니다.</p>
</article>
```

실무 기준:

- 이미지가 정보를 전달하면 alt 제공
- 주변 텍스트와 완전히 중복이면 장식 처리 검토
- “이미지”, “사진” 같은 불필요한 단어 지양
- 기능을 가진 이미지의 alt는 기능 목적 중심
- 장식 이미지는 empty alt로 스크린 리더가 건너뛰게 함

---

### [FAQ]

Q. 모든 이미지에 자세한 alt를 넣어야 해?
A. 아니다. 장식 이미지는 `alt=""`가 적합하고 정보 이미지는 의미를 전달하는 alt가 필요하다.

Q. 축제 카드 이미지 alt는 어떻게 써?
A. 이미지가 정보 전달 역할이면 축제명이나 이미지 의미를 포함하고 카드 제목과 완전히 중복이면 장식 처리도 검토할 수 있다.

Q. alt에 “이미지”라는 말을 넣어야 해?
A. 보통 넣지 않는다. 스크린 리더가 이미 이미지임을 전달할 수 있다.

Q. 링크 이미지 alt는 어떻게 써?
A. 이미지 설명보다 링크의 목적을 전달하는 alt를 제공한다.

---

## 8.2 Icon Semantics

### [개념]

Icon Semantics는 아이콘이 장식인지, 정보인지, 기능인지에 따라 보조기술 전달 방식을 결정하는 기준이다.

아이콘은 시각적으로 의미가 있어도 스크린 리더에는 이름이 없거나 불필요한 정보로 읽힐 수 있다.

---

### [핵심]

Icon 유형:

- decorative icon
- informative icon
- icon button
- status icon
- loading icon

처리 기준:

- 장식 아이콘: `aria-hidden="true"`
- 아이콘 버튼: button에 `aria-label`
- 상태 아이콘: 텍스트 또는 accessible name 제공
- loading icon: loading text 함께 제공
- 색상 아이콘만으로 상태 전달 금지

---

### [실무]

장식 아이콘:

```jsx
<SearchIcon aria-hidden="true" />
```

아이콘 버튼:

```jsx
<button type="button" aria-label="알림 열기">
  <BellIcon aria-hidden="true" />
</button>
```

상태 아이콘:

```jsx
<span aria-label="성공">
  <CheckIcon aria-hidden="true" />
</span>
```

로딩 아이콘:

```jsx
<div role="status">
  <Spinner aria-hidden="true" />
  <span>처리 중입니다.</span>
</div>
```

실무 기준:

- 텍스트 옆 장식 아이콘은 `aria-hidden`
- 아이콘만 있는 버튼은 button에 accessible name 제공
- 아이콘 자체에 label을 붙이기보다 interactive element에 이름 제공
- 성공 / 실패 / 경고는 텍스트와 함께 제공
- 색상과 아이콘만으로 상태 전달 금지

---

### [FAQ]

Q. 아이콘에 항상 aria-label을 붙여야 해?
A. 아니다. 장식 아이콘은 aria-hidden이 적합하고 아이콘만으로 기능을 나타내는 버튼에는 aria-label이 필요하다.

Q. 아이콘 버튼에는 aria-label을 어디에 붙여?
A. 아이콘이 아니라 button 요소에 붙이는 것이 적합하다.

Q. 체크 아이콘만 보여주면 성공 상태가 전달돼?
A. 색상이나 아이콘만으로는 부족할 수 있다. 텍스트나 accessible name을 함께 제공하는 것이 좋다.

Q. 텍스트 옆 아이콘은 어떻게 처리해?
A. 텍스트가 의미를 이미 전달한다면 아이콘은 aria-hidden으로 장식 처리할 수 있다.

---

# 9. Semantic HTML Review

## 9.1 Review Checklist

### [개념]

Semantic HTML Review는 UI가 의미 있는 HTML 구조로 작성되었는지 검토하는 과정이다.

Review Agent는 접근성 문제를 찾을 때 Semantic HTML 누락을 가장 먼저 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] 클릭 액션에 button을 사용했는가?
- [ ] 페이지 이동에 Link 또는 a를 사용했는가?
- [ ] Form Control에 input/select/textarea를 사용했는가?
- [ ] input과 label이 연결되었는가?
- [ ] 주요 콘텐츠가 main 안에 있는가?
- [ ] nav가 주요 탐색 영역에 사용되었는가?
- [ ] nav가 여러 개면 aria-label로 구분했는가?
- [ ] 페이지 h1이 있는가?
- [ ] heading level이 자연스러운가?
- [ ] 반복 항목이 list 구조로 표현되었는가?
- [ ] 독립 카드에 article 사용을 검토했는가?
- [ ] 표 데이터에 table을 사용했는가?
- [ ] 이미지 alt가 목적에 맞는가?
- [ ] icon only button에 accessible name이 있는가?
- [ ] 의미 없는 div/span 남용이 없는가?
- [ ] ARIA가 Semantic HTML 대체용으로 남용되지 않았는가?
```

---

### [실무]

Review Flow:

```text
React Component 확인
→ Interactive Element 역할 확인
→ Native Element 사용 여부 확인
→ Landmark 구조 확인
→ Heading 구조 확인
→ List / Table 구조 확인
→ Image / Icon 의미 확인
→ Testing Library Query 가능 여부 확인
```

대표 문제와 수정:

```text
문제: div onClick 사용
수정: button type="button" 사용
```

```text
문제: 상세 이동을 button + navigate로 처리
수정: 단순 이동이면 Link 사용
```

```text
문제: nav 여러 개에 이름 없음
수정: nav aria-label 제공
```

```text
문제: 카드 목록이 div 반복만 사용
수정: ul/li + article 구조 검토
```

---

### [FAQ]

Q. Semantic HTML Review에서 가장 먼저 볼 것은?
A. Button / Link 역할 구분, label 연결, main/nav 구조, heading 구조를 먼저 본다.

Q. div가 많으면 무조건 문제야?
A. 아니다. 단순 layout wrapper는 div가 적합하다. 의미가 필요한 곳에 semantic element를 사용해야 한다.

Q. ARIA를 붙이면 semantic 문제를 해결할 수 있어?
A. 일부 보완은 가능하지만 가능한 경우 native semantic element를 우선 사용해야 한다.

Q. getByRole이 실패하면 Semantic HTML 문제일 수 있어?
A. 그렇다. 요소의 role, accessible name, hidden 여부를 확인해야 한다.

---

# 10. Semantic HTML Anti Patterns

## 10.1 Common Mistakes

### [개념]

Semantic HTML Anti Pattern은 화면은 동작하지만 의미, keyboard, 스크린 리더, 테스트 관점에서 문제가 생기는 구현 방식이다.

---

### [핵심]

자주 발생하는 실수:

- `div onClick`을 button처럼 사용
- `span onClick`을 button처럼 사용
- 삭제 액션을 `a`로 구현
- 상세 이동을 button으로 구현
- `href="#"` 사용 후 action 처리
- `button`에 type 누락
- label 없는 input
- `placeholder`를 label로 사용
- `main` 없는 페이지
- 페이지 `h1` 누락
- heading level skip
- nav 여러 개에 이름 없음
- list를 div 반복으로만 구현
- 표 데이터를 div grid로 구현
- 장식 이미지에 불필요한 alt 제공
- 정보 이미지 alt 누락
- icon button accessible name 누락
- role만 붙이고 keyboard 동작 미구현

---

### [실무]

Anti Pattern 예:

```jsx
<div role="button" onClick={onSave}>
  저장
</div>
```

개선:

```jsx
<button type="button" onClick={onSave}>
  저장
</button>
```

Anti Pattern 예:

```jsx
<a href="#" onClick={onDelete}>
  삭제
</a>
```

개선:

```jsx
<button type="button" onClick={onDelete}>
  삭제
</button>
```

Anti Pattern 예:

```jsx
<input placeholder="이메일" />
```

개선:

```jsx
<label htmlFor="email">이메일</label>
<input id="email" name="email" type="email" />
```

Anti Pattern 예:

```jsx
<div className="table">
  <div>닉네임</div>
  <div>권한</div>
</div>
```

개선:

```jsx
<table>
  <thead>
    <tr>
      <th scope="col">닉네임</th>
      <th scope="col">권한</th>
    </tr>
  </thead>
</table>
```

---

### [FAQ]

Q. div onClick이 왜 문제야?
A. 기본 keyboard 동작과 semantic role이 없어서 접근성과 테스트에 문제가 생길 수 있다.

Q. role="button"을 붙이면 해결 아니야?
A. role만으로는 keyboard 동작이 생기지 않는다. Enter / Space 처리와 focus 관리가 필요하다.

Q. placeholder만 있는 input은 왜 문제야?
A. 입력 중 사라지고 label을 안정적으로 대체하지 못하기 때문이다.

Q. 표를 div로 만들면 왜 문제야?
A. 행과 열 관계가 보조기술에 명확히 전달되지 않을 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Semantic HTML이 뭐야?
A. HTML 요소를 의미에 맞게 사용하는 것이다. button, nav, main, label 같은 태그를 역할에 맞게 사용한다.

Q. Frontend Accessibility에서 Semantic HTML이 왜 중요해?
A. 브라우저와 보조기술이 요소의 역할을 기본적으로 이해할 수 있고 keyboard와 Testing Library 검증에도 유리하기 때문이다.

Q. ARIA보다 Semantic HTML을 먼저 써야 해?
A. 그렇다. 가능한 경우 의미 있는 HTML을 먼저 사용하고 ARIA는 부족한 의미를 보완할 때 사용한다.

Q. div onClick을 써도 돼?
A. 가능은 하지만 keyboard 접근성과 의미가 부족하다. 클릭 액션은 button을 사용하는 것이 좋다.

Q. span onClick을 버튼처럼 써도 돼?
A. 권장하지 않는다. 클릭 액션은 button을 사용하는 것이 접근성과 keyboard 동작에 안전하다.

Q. role="button"을 쓰면 button처럼 동작해?
A. 스크린 리더 역할은 전달할 수 있지만 keyboard 동작은 직접 구현해야 한다. 가능하면 button 태그를 사용한다.

Q. Button과 Link 차이는?
A. Button은 액션 실행이고 Link는 페이지나 위치 이동이다.

Q. 상세 페이지 이동 버튼은 button이야 Link야?
A. 단순 페이지 이동이라면 Link가 적합하다.

Q. 삭제는 Link로 만들어도 돼?
A. 권장하지 않는다. 삭제는 현재 상태를 변경하는 액션이므로 button이 적합하다.

Q. 모달 열기는 Button이야 Link야?
A. 현재 화면에서 UI 상태를 변경하는 액션이므로 button이 적합하다.

Q. 좋아요 토글은 Button이야 Link야?
A. 현재 상태를 변경하는 액션이므로 button이 적합하다.

Q. Button에 type을 꼭 써야 해?
A. Form 안에서는 기본 submit 동작 때문에 type을 명시하는 것이 안전하다.

Q. 공통 Button Component 기본 type은 뭐가 좋아?
A. 의도하지 않은 submit을 막기 위해 type="button"을 기본값으로 두는 것이 좋다.

Q. Form 제출 버튼은 type을 뭘로 해야 해?
A. type="submit"을 사용한다.

Q. 취소 버튼이 Form을 제출해버리는 이유는?
A. Form 내부 button의 기본 동작이 submit일 수 있기 때문이다. 취소 버튼에는 type="button"을 명시한다.

Q. Landmark가 뭐야?
A. 페이지의 주요 영역을 의미 있게 나누는 구조다. header, nav, main, footer 같은 요소가 대표적이다.

Q. main 태그는 꼭 필요해?
A. 페이지 주요 콘텐츠를 나타내기 위해 사용하는 것이 좋다.

Q. SPA에서도 main이 필요해?
A. 필요하다. SPA도 사용자가 인식하는 페이지 구조가 있으므로 주요 콘텐츠 영역을 main으로 제공하는 것이 좋다.

Q. main은 여러 개 있어도 돼?
A. 일반적인 앱 페이지에서는 하나만 사용하는 것이 명확하다.

Q. Skip Link는 main과 연결해?
A. 보통 본문으로 건너뛰기 링크를 main 영역과 연결한다.

Q. route 이동 후 focus는 어디로 가야 해?
A. 페이지 제목 h1 또는 main 영역으로 focus 이동을 검토할 수 있다.

Q. nav가 여러 개면 어떻게 해?
A. aria-label로 “주요 메뉴”, “하단 메뉴”처럼 구분하는 것이 좋다.

Q. 모든 링크 묶음에 nav를 써야 해?
A. 주요 탐색 영역에 사용한다. 단순 카드 내부 링크 묶음까지 모두 nav로 감쌀 필요는 없다.

Q. 현재 메뉴는 어떻게 표시해?
A. 시각적 표시와 함께 aria-current="page"를 사용할 수 있다.

Q. Breadcrumb도 nav야?
A. 페이지 위치를 탐색하는 링크 묶음이므로 nav와 aria-label을 사용할 수 있다.

Q. Heading Structure가 뭐야?
A. h1부터 h6까지의 제목 요소로 페이지 콘텐츠 계층을 표현하는 구조다.

Q. h1은 여러 개 있어도 돼?
A. HTML상 가능하지만 일반적인 앱 페이지에서는 페이지 핵심 제목 하나를 h1로 두는 방식이 명확하다.

Q. 글자 크기를 줄이려고 h4를 써도 돼?
A. 권장하지 않는다. heading은 문서 구조 기준이고 크기는 CSS로 조정한다.

Q. heading level을 건너뛰면 안 돼?
A. 가능한 한 자연스러운 계층을 유지하는 것이 좋다. 구조 이해가 어려워질 수 있다.

Q. 카드 제목도 heading으로 해야 해?
A. 카드가 독립 콘텐츠라면 heading을 고려할 수 있다. 목록 구조와 페이지 heading 계층에 맞춰 기준을 통일한다.

Q. 페이지마다 h1이 필요해?
A. 현재 화면의 핵심 목적을 전달하기 위해 route별 h1을 두는 것이 좋다.

Q. 상세 페이지 h1은 뭘로 해?
A. 일반적으로 상세 대상의 이름을 h1로 사용할 수 있다.

Q. h1을 숨겨도 돼?
A. 시각적으로 숨기더라도 스크린 리더가 읽을 수 있는 방식으로 제공할 수 있다.

Q. section에는 heading이 꼭 필요해?
A. 의미 있는 section이라면 heading을 제공하는 것이 좋다.

Q. 모든 div를 section으로 바꾸면 좋아?
A. 아니다. 의미 있는 콘텐츠 구역일 때 section을 사용하고 단순 wrapper는 div가 적합하다.

Q. article과 section 차이는?
A. article은 독립 콘텐츠 단위이고 section은 문서 내 주제별 구역이다.

Q. 카드 UI에는 article을 써도 돼?
A. 카드가 독립 콘텐츠 단위라면 article을 사용할 수 있다.

Q. article 안에는 heading이 필요해?
A. 독립 콘텐츠를 식별할 수 있도록 heading을 제공하는 것이 좋다.

Q. section과 div 차이는?
A. section은 의미 있는 주제별 구역이고 div는 의미 없는 일반 컨테이너다.

Q. 단순 스타일 wrapper는 뭘 써?
A. 의미가 필요 없다면 div가 적합하다.

Q. 검색 결과 영역은 section이 적합해?
A. 검색 결과라는 의미 있는 구역이므로 heading과 함께 section을 사용할 수 있다.

Q. 카드 목록은 ul/li로 감싸야 해?
A. 반복되는 항목 목록이라면 ul/li를 사용하는 것이 의미상 좋다.

Q. CSS grid를 쓰면 ul/li를 못 써?
A. 아니다. ul/li에도 CSS grid를 적용할 수 있다.

Q. 순위 목록은 ul이야 ol이야?
A. 순서나 순위가 의미 있으면 ol이 적합하다.

Q. 빈 목록이면 아무것도 안 보여줘도 돼?
A. 권장하지 않는다. Empty State를 제공해 현재 상태를 설명해야 한다.

Q. 자세히 보기 링크를 반복해서 써도 돼?
A. 가능하지만 스크린 리더에서는 목적지가 모호할 수 있다. 대상 이름을 포함하는 것이 좋다.

Q. 링크 텍스트는 어떻게 써야 해?
A. 링크만 읽어도 이동 목적지를 이해할 수 있게 작성한다.

Q. 여기를 클릭 링크는 왜 안 좋아?
A. 링크 목적지가 설명되지 않아 스크린 리더 사용자와 키보드 사용자에게 불명확하다.

Q. 표를 div로 만들어도 돼?
A. 행과 열 관계가 중요한 데이터는 table 요소를 사용하는 것이 접근성에 좋다.

Q. caption은 꼭 필요해?
A. 복잡한 표일수록 caption이 표의 목적을 이해하는 데 도움이 된다.

Q. th의 scope는 왜 필요해?
A. header가 열 기준인지 행 기준인지 명확히 전달할 수 있다.

Q. layout용 table을 써도 돼?
A. 권장하지 않는다. 레이아웃은 CSS로 처리하고 table은 표 데이터에 사용한다.

Q. 정렬 가능한 table header는 어떻게 만들어?
A. th 내부에 button을 두고 정렬 상태를 텍스트나 aria-sort로 전달한다.

Q. aria-sort는 어디에 써?
A. 정렬 상태가 있는 column header에 사용할 수 있다.

Q. 정렬 버튼은 Link야 Button이야?
A. 현재 표 상태를 변경하는 액션이므로 button이 적합하다.

Q. 모든 이미지에 자세한 alt를 넣어야 해?
A. 아니다. 장식 이미지는 alt=""가 적합하고 정보 이미지는 의미를 전달하는 alt가 필요하다.

Q. 축제 카드 이미지 alt는 어떻게 써?
A. 이미지가 정보 전달 역할이면 축제명이나 이미지 의미를 포함하고 카드 제목과 완전히 중복이면 장식 처리도 검토할 수 있다.

Q. alt에 이미지라는 말을 넣어야 해?
A. 보통 넣지 않는다. 스크린 리더가 이미 이미지임을 전달할 수 있다.

Q. 링크 이미지 alt는 어떻게 써?
A. 이미지 설명보다 링크의 목적을 전달하는 alt를 제공한다.

Q. 아이콘에 항상 aria-label을 붙여야 해?
A. 아니다. 장식 아이콘은 aria-hidden이 적합하고 아이콘만으로 기능을 나타내는 버튼에는 aria-label이 필요하다.

Q. 아이콘 버튼에는 aria-label을 어디에 붙여?
A. 아이콘이 아니라 button 요소에 붙이는 것이 적합하다.

Q. 체크 아이콘만 보여주면 성공 상태가 전달돼?
A. 색상이나 아이콘만으로는 부족할 수 있다. 텍스트나 accessible name을 함께 제공하는 것이 좋다.

Q. Semantic HTML Review에서 가장 먼저 볼 것은?
A. Button / Link 역할 구분, label 연결, main/nav 구조, heading 구조를 먼저 본다.

Q. div가 많으면 무조건 문제야?
A. 아니다. 단순 layout wrapper는 div가 적합하다. 의미가 필요한 곳에 semantic element를 사용해야 한다.

Q. ARIA를 붙이면 semantic 문제를 해결할 수 있어?
A. 일부 보완은 가능하지만 가능한 경우 native semantic element를 우선 사용해야 한다.

Q. getByRole이 실패하면 Semantic HTML 문제일 수 있어?
A. 그렇다. 요소의 role, accessible name, hidden 여부를 확인해야 한다.
