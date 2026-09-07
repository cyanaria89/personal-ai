# Design System Foundation Part06 - Layout Responsive Theme Rules

---

# 1. Layout System Core

## 1.1 Layout System Definition

### [개념]

Layout System은 페이지와 컴포넌트를 일관되게 배치하기 위한 공통 구조 규칙이다.

Layout System은 Container, Section, Grid, Stack, Inline, Header, Sidebar, Footer, Responsive Layout 같은 화면 배치 기준을 포함한다.

Layout System은 Frontend Agent가 화면마다 임의 간격과 임의 배치를 만들지 않도록 하는 기준이며, Review Agent가 화면 구조와 반응형 품질을 검토하는 기준이다.

---

### [핵심]

Layout System 구성:

- App Layout
- Page Layout
- Container
- Section
- Grid
- Stack
- Inline
- Header
- Footer
- Sidebar Layout
- Content Layout
- Form Layout
- Card Grid
- Table Wrapper
- Responsive Layout

Layout System 목적:

- 페이지 구조 통일
- 화면 간 spacing 일관성 유지
- 컴포넌트 외부 배치 기준 분리
- 반응형 대응 기준 제공
- 모바일 깨짐 방지
- UI 재사용성 향상
- Frontend Agent 배치 기준 제공
- Review Agent layout 검토 기준 제공

---

### [실무]

Layout System 기본 Flow:

```text
Page Requirement
→ Page Layout 선택
→ Container 적용
→ Section 구성
→ Grid / Stack / Inline 배치
→ Component 배치
→ Responsive 기준 적용
→ Review Checklist
```

나쁜 흐름:

```text
Page Request
→ 각 컴포넌트에 margin 직접 지정
→ 화면별 간격 불일치
→ 모바일 깨짐
→ 유지보수 어려움
```

좋은 흐름:

```text
Page Request
→ Layout Component 사용
→ spacing token 사용
→ parent gap 사용
→ mobile first 적용
→ responsive 검토
```

---

### [FAQ]

Q. Layout System이 뭐야?
A. 페이지와 컴포넌트를 일관되게 배치하기 위한 Container, Section, Grid, Stack 같은 화면 구조 규칙이다.

Q. Layout System은 왜 필요해?
A. 페이지마다 간격과 배치가 달라지는 것을 막고 일관된 화면 구조를 만들기 위해 필요하다.

Q. Layout System은 Design System에 포함돼?
A. 포함된다. Design System은 컴포넌트뿐 아니라 화면 배치, 간격, 반응형 기준까지 포함한다.

Q. Review Agent는 Layout에서 뭘 봐야 해?
A. Container, Section spacing, Grid gap, mobile 대응, 컴포넌트 margin 남용 여부를 확인해야 한다.

---

## 1.2 Layout Responsibility Rules

### [개념]

Layout Responsibility Rules는 컴포넌트 내부 스타일과 외부 배치 책임을 분리하는 기준이다.

재사용 컴포넌트는 내부 구조와 padding을 담당하고, 외부 배치는 부모 Layout이 gap으로 담당하는 것이 좋다.

---

### [핵심]

책임 분리:

```text
Component
→ 내부 구조
→ 내부 padding
→ 자체 variant / state
→ 자체 accessibility

Parent Layout
→ 외부 간격
→ 목록 간 gap
→ grid column
→ section spacing
→ responsive 배치
```

권장:

- Card 내부 여백은 Card padding
- Card 목록 간격은 CardGrid gap
- Form Field 사이 간격은 FormStack gap
- Button 그룹 간격은 ButtonGroup gap
- Page section 간격은 Page Layout gap

비권장:

- Card에 margin-bottom 직접 지정
- Input에 화면별 margin 직접 지정
- Button마다 임의 margin 적용
- 컴포넌트가 외부 layout까지 담당
- 화면별 raw spacing 직접 사용

---

### [실무]

나쁜 예:

```css
.card {
  margin-bottom: 24px;
}

.input {
  margin-bottom: 16px;
}
```

좋은 예:

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-6);
}

.formStack {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-4);
}
```

Review 기준:

```md
- [ ] 재사용 컴포넌트가 외부 margin을 과하게 갖지 않는가?
- [ ] parent layout이 gap을 담당하는가?
- [ ] component padding과 layout spacing이 분리되는가?
- [ ] spacing token을 사용하는가?
```

---

### [FAQ]

Q. 컴포넌트에 margin을 직접 주면 안 돼?
A. 재사용 컴포넌트라면 외부 배치는 부모 layout이 담당하는 것이 좋다.

Q. Component padding과 Layout gap은 뭐가 달라?
A. padding은 컴포넌트 내부 여백이고, gap은 부모가 자식 사이 간격을 조정하는 값이다.

Q. Card list 간격은 어디서 관리해?
A. Card 자체가 아니라 CardGrid 같은 부모 layout에서 gap으로 관리한다.

Q. Form Field 간격은 어떻게 관리해?
A. 개별 Form Field margin보다 form parent의 gap으로 관리하는 것이 좋다.

---

# 2. Container and Page Layout Rules

## 2.1 Container Rules

### [개념]

Container는 페이지 콘텐츠의 최대 너비와 좌우 여백을 관리하는 layout component다.

Container는 화면이 너무 넓어져 가독성이 떨어지거나 모바일에서 좌우 여백이 깨지는 것을 방지한다.

---

### [핵심]

Container 기준:

- page content 최대 너비 제한
- 좌우 padding 제공
- 중앙 정렬
- mobile first 기준
- section 내부 콘텐츠 폭 통일
- raw width 남발 금지
- token 기반 padding 사용
- 프로젝트 전체 max width 통일

권장 token:

```text
--layout-container-max-width
--layout-page-padding
--layout-page-padding-md
--layout-page-padding-lg
```

---

### [실무]

Container CSS 예:

```css
:root {
  --layout-container-max-width: 1200px;
  --layout-page-padding: var(--spacing-4);
}

.container {
  width: min(
    100% - calc(var(--layout-page-padding) * 2),
    var(--layout-container-max-width)
  );
  margin-inline: auto;
}
```

Responsive Container 예:

```css
@media (min-width: 768px) {
  :root {
    --layout-page-padding: var(--spacing-6);
  }
}

@media (min-width: 1024px) {
  :root {
    --layout-page-padding: var(--spacing-8);
  }
}
```

---

### [FAQ]

Q. Container는 왜 필요해?
A. 페이지 콘텐츠 폭과 좌우 여백을 통일해 가독성과 화면 일관성을 유지하기 위해 필요하다.

Q. Container max width는 얼마가 좋아?
A. 일반 웹 페이지는 1080px, 1200px, 1280px 같은 기준을 사용할 수 있다. 프로젝트 기준으로 통일해야 한다.

Q. 모바일에서도 Container가 필요해?
A. 필요하다. 모바일 좌우 padding을 일관되게 관리해야 한다.

Q. width를 화면마다 직접 지정해도 돼?
A. 권장하지 않는다. Container와 layout token을 사용하는 것이 좋다.

---

## 2.2 Page Layout Rules

### [개념]

Page Layout은 한 페이지의 전체 구조를 정의하는 규칙이다.

Page Layout은 Header, Main, Section, Footer, Sidebar, Content Area 같은 영역을 일관되게 구성한다.

---

### [핵심]

Page Layout 구성:

```text
App Shell
→ Header
→ Sidebar
→ Main
→ Page Header
→ Section
→ Footer
```

Page Layout 기준:

- main landmark 사용
- page title 제공
- section 구조 명확화
- section spacing token 사용
- 페이지별 임의 padding 금지
- mobile first 기준
- route별 layout 재사용
- loading / error / empty state 배치 고려

---

### [실무]

기본 Page Layout 예:

```jsx
<AppLayout>
  <main>
    <Container>
      <PageHeader
        title="LOT 관리"
        description="생산 LOT를 조회하고 관리합니다."
      />
      <PageSection>
        <LotSearchForm />
      </PageSection>
      <PageSection>
        <LotTable />
      </PageSection>
    </Container>
  </main>
</AppLayout>
```

CSS 예:

```css
.page {
  display: flex;
  flex-direction: column;
  gap: var(--layout-section-gap);
}

.pageHeader {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-2);
}
```

Review 기준:

```md
- [ ] main 영역이 명확한가?
- [ ] page title이 있는가?
- [ ] section 구조가 명확한가?
- [ ] section spacing이 token으로 관리되는가?
- [ ] page padding이 Container 기준과 일치하는가?
```

---

### [FAQ]

Q. Page Layout은 왜 필요해?
A. 페이지마다 header, title, section, content 배치가 달라지는 것을 막기 위해 필요하다.

Q. main 태그는 꼭 필요해?
A. 권장된다. 페이지의 주요 콘텐츠 영역을 semantic하게 표시할 수 있다.

Q. Page title은 꼭 있어야 해?
A. 대부분 필요하다. 사용자가 현재 화면의 목적을 이해할 수 있어야 한다.

Q. section 간격은 어떻게 관리해?
A. `--layout-section-gap` 같은 layout token으로 관리한다.

---

## 2.3 Section Rules

### [개념]

Section은 페이지 안에서 관련 콘텐츠를 묶는 layout 단위다.

Section은 제목, 설명, 콘텐츠, action을 포함할 수 있으며 페이지 구조를 명확히 만든다.

---

### [핵심]

Section 구성:

```text
Section Header
→ Section Title
→ Section Description
→ Section Action
→ Section Body
```

Section 기준:

- 관련 콘텐츠를 하나의 section으로 묶음
- section title 제공 고려
- section spacing token 사용
- section 내부 layout은 Grid / Stack 사용
- unrelated content를 하나의 section에 섞지 않음
- heading level 순서 유지

---

### [실무]

Section 예:

```jsx
<section>
  <SectionHeader
    title="생산 현황"
    description="현재 진행 중인 LOT와 설비 상태를 확인합니다."
    action={<Button variant="primary">생산 지시 등록</Button>}
  />
  <ProductionStatusGrid />
</section>
```

Section CSS 예:

```css
.section {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-4);
}

.sectionHeader {
  display: flex;
  justify-content: space-between;
  gap: var(--spacing-4);
}
```

Review 기준:

```md
- [ ] section이 관련 콘텐츠를 묶는가?
- [ ] section title이 필요한 곳에 있는가?
- [ ] heading level이 자연스러운가?
- [ ] section action이 명확한가?
```

---

### [FAQ]

Q. Section은 언제 써?
A. 페이지 안에서 관련 콘텐츠를 제목과 함께 묶어 보여줄 때 사용한다.

Q. 모든 section에 title이 필요해?
A. 항상은 아니지만 콘텐츠 묶음의 의미가 필요하면 title을 제공하는 것이 좋다.

Q. Section과 Card는 뭐가 달라?
A. Section은 페이지 구조 단위이고, Card는 정보를 시각적으로 묶는 컴포넌트다.

Q. section heading level은 중요해?
A. 중요하다. heading 구조는 접근성과 문서 구조 이해에 영향을 준다.

---

# 3. Grid Stack Inline Rules

## 3.1 Grid Layout Rules

### [개념]

Grid Layout은 카드 목록, 대시보드, 통계 카드, 반응형 컬럼 배치를 만드는 layout 패턴이다.

Grid는 2차원 배치에 적합하며 화면 너비에 따라 column 수를 조정할 수 있다.

---

### [핵심]

Grid 사용 대상:

- Card List
- Dashboard Cards
- Statistic Cards
- Product Cards
- Equipment Status Cards
- Form Two Column Layout
- Image Gallery
- Responsive Content Blocks

Grid 기준:

- gap은 spacing token 사용
- column 수는 responsive 기준으로 조정
- mobile first 적용
- card 자체 margin 대신 grid gap 사용
- minmax / auto-fit 활용 가능
- 가로 스크롤 발생 주의

---

### [실무]

Responsive Grid 예:

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-6);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .cardGrid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .cardGrid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```

Auto-fit Grid 예:

```css
.autoGrid {
  display: grid;
  gap: var(--spacing-6);
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}
```

Review 기준:

```md
- [ ] grid gap이 token으로 관리되는가?
- [ ] mobile first 기준인가?
- [ ] card에 margin을 직접 주지 않는가?
- [ ] column 수가 화면 크기에 맞게 변하는가?
```

---

### [FAQ]

Q. Grid Layout은 언제 써?
A. 카드 목록, 대시보드, 통계 카드처럼 2차원 배치가 필요한 경우 사용한다.

Q. Grid gap은 어디서 관리해?
A. Grid parent에서 spacing token으로 관리한다.

Q. auto-fit과 minmax는 언제 좋아?
A. 카드가 화면 너비에 따라 자연스럽게 줄바꿈되어야 할 때 좋다.

Q. 모바일에서는 Grid를 어떻게 처리해?
A. 기본 1열로 시작하고 tablet, desktop에서 2열, 3열로 확장한다.

---

## 3.2 Stack Layout Rules

### [개념]

Stack Layout은 요소를 세로 방향으로 쌓고 일정한 간격을 주는 layout 패턴이다.

Stack은 Form, Section Body, List, Modal Body 같은 수직 흐름에 적합하다.

---

### [핵심]

Stack 사용 대상:

- Form Field List
- Section Content
- Modal Body
- Alert Content
- Vertical Menu
- Detail Information
- Empty State Content

Stack 기준:

- flex column 사용
- gap은 spacing token 사용
- child margin 제거
- 중첩 stack 가능
- spacing size를 의미 있게 선택
- 반응형에서 gap 조정 가능

---

### [실무]

Stack CSS 예:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-4);
}
```

Form Stack 예:

```jsx
<form className="formStack">
  <FormField id="email" label="이메일">
    <TextInput id="email" name="email" value={email} onChange={setEmail} />
  </FormField>
  <FormField id="password" label="비밀번호">
    <TextInput
      id="password"
      name="password"
      value={password}
      onChange={setPassword}
    />
  </FormField>
  <Button type="submit">로그인</Button>
</form>
```

Review 기준:

```md
- [ ] 수직 간격을 child margin이 아니라 parent gap으로 관리하는가?
- [ ] gap 값이 spacing token인가?
- [ ] form field spacing이 일관적인가?
- [ ] stack 중첩이 과도하지 않은가?
```

---

### [FAQ]

Q. Stack Layout은 언제 써?
A. Form Field, Section Body, Modal Body처럼 요소를 세로로 쌓을 때 사용한다.

Q. Stack에서 margin-bottom을 써도 돼?
A. 권장하지 않는다. parent gap으로 관리하는 것이 일관성에 좋다.

Q. Stack gap은 어떻게 정해?
A. 콘텐츠 밀도와 컴포넌트 관계에 따라 spacing token 중 선택한다.

Q. Stack은 Grid와 뭐가 달라?
A. Stack은 1차원 세로 배치이고, Grid는 2차원 행 / 열 배치다.

---

## 3.3 Inline Layout Rules

### [개념]

Inline Layout은 요소를 가로 방향으로 배치하고 간격과 정렬을 관리하는 layout 패턴이다.

Inline은 Button Group, Badge List, Action Row, Toolbar, Form Inline Control에 적합하다.

---

### [핵심]

Inline 사용 대상:

- Button Group
- Action Row
- Toolbar
- Badge List
- Tag List
- Pagination Controls
- Form Inline Controls
- Header Actions

Inline 기준:

- flex row 사용
- gap은 spacing token 사용
- align-items 기준 명확화
- wrap 필요성 검토
- 모바일에서 세로 전환 고려
- 버튼 간 margin 직접 지정 금지

---

### [실무]

Inline CSS 예:

```css
.inline {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
}
```

Button Group 예:

```jsx
<div className="buttonGroup">
  <Button variant="secondary">취소</Button>
  <Button variant="primary">저장</Button>
</div>
```

Responsive Inline 예:

```css
.actionRow {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-3);
}

@media (min-width: 768px) {
  .actionRow {
    flex-direction: row;
    justify-content: flex-end;
  }
}
```

Review 기준:

```md
- [ ] inline gap이 token으로 관리되는가?
- [ ] 모바일에서 가로 배치가 깨지지 않는가?
- [ ] 버튼 그룹 순서가 명확한가?
- [ ] wrap 또는 세로 전환을 고려했는가?
```

---

### [FAQ]

Q. Inline Layout은 언제 써?
A. 버튼 그룹, 액션 영역, 태그 목록처럼 요소를 가로로 배치할 때 사용한다.

Q. 모바일에서도 Inline을 유지해야 해?
A. 항상은 아니다. 공간이 부족하면 세로 배치나 wrap을 고려한다.

Q. Button 사이 간격은 어떻게 관리해?
A. Button 자체 margin이 아니라 ButtonGroup 또는 Inline parent의 gap으로 관리한다.

Q. Inline과 Stack은 뭐가 달라?
A. Inline은 가로 배치이고 Stack은 세로 배치다.

---

## 3.4 Layout Pattern Mistakes

### [개념]

Layout Pattern Mistakes는 Grid, Stack, Inline 배치를 일관성 없이 사용하거나 컴포넌트 margin으로 화면을 억지로 맞추는 실수다.

Layout 실수는 화면 깨짐, 반응형 문제, 유지보수 문제를 만든다.

---

### [핵심]

자주 발생하는 실수:

- 모든 간격을 margin으로 처리
- Card에 margin-bottom 직접 지정
- Form Field마다 margin 직접 지정
- Grid gap 없이 child spacing 사용
- 모바일에서 inline button group 깨짐
- section spacing 기준 없음
- Container 없이 화면 전체 폭 사용
- desktop 기준으로만 layout 작성
- table overflow 방치
- layout component 없이 div 중첩 남발
- spacing token 없이 임의 px 사용

---

### [실무]

Troubleshooting:

```text
카드 목록 간격이 불일치
→ CardGrid gap 확인

Form 간격이 제각각
→ FormStack gap 확인

버튼 그룹이 모바일에서 깨짐
→ Inline responsive 전환 확인

페이지 좌우 여백이 화면마다 다름
→ Container 적용 확인

대시보드 카드가 좁은 화면에서 깨짐
→ Grid column responsive 확인
```

Review Checklist:

```md
- [ ] layout gap이 token으로 관리되는가?
- [ ] component margin이 남용되지 않는가?
- [ ] Container 기준이 적용되는가?
- [ ] mobile first 기준인가?
- [ ] Grid / Stack / Inline 선택이 적절한가?
```

---

### [FAQ]

Q. Layout에서 가장 흔한 실수는?
A. 컴포넌트마다 margin을 직접 넣고 parent gap을 사용하지 않는 것이다.

Q. div를 많이 중첩하면 문제야?
A. 의미 없는 중첩은 구조를 복잡하게 만들고 유지보수를 어렵게 한다.

Q. desktop에서 괜찮으면 layout 통과야?
A. 아니다. 모바일과 태블릿에서도 깨지지 않아야 한다.

Q. spacing token 없이 layout을 만들어도 돼?
A. 가능하지만 화면이 늘어날수록 일관성과 유지보수가 어려워진다.

---

# 4. Responsive Design Rules

## 4.1 Responsive Design Definition

### [개념]

Responsive Design은 화면 크기에 따라 UI 구조, 간격, 컬럼, navigation, table, modal이 자연스럽게 변하도록 만드는 기준이다.

Responsive Design은 모바일, 태블릿, 데스크톱, 와이드 화면에서 사용자가 동일한 기능을 사용할 수 있게 한다.

---

### [핵심]

Responsive 기준:

```text
Mobile First
→ Tablet
→ Desktop
→ Wide
```

권장 breakpoint:

```text
mobile: default
tablet: 768px
desktop: 1024px
wide: 1280px
```

검토 대상:

- Page Layout
- Container
- Grid
- Stack
- Inline
- Navigation
- Modal
- Table
- Form
- Typography
- Spacing
- Touch Target

---

### [실무]

Mobile First 예:

```css
.dashboardGrid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-4);
}

@media (min-width: 768px) {
  .dashboardGrid {
    grid-template-columns: repeat(2, 1fr);
    gap: var(--spacing-6);
  }
}

@media (min-width: 1024px) {
  .dashboardGrid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

Review 기준:

```md
- [ ] mobile first 기준인가?
- [ ] 모바일에서 가로 스크롤이 없는가?
- [ ] 주요 action이 모바일에서 사용 가능한가?
- [ ] touch target이 충분한가?
- [ ] breakpoint 기준이 문서화되어 있는가?
```

---

### [FAQ]

Q. Responsive Design이 뭐야?
A. 화면 크기에 따라 UI 구조와 배치가 자연스럽게 변하도록 만드는 기준이다.

Q. Mobile First가 뭐야?
A. 모바일 기본 스타일을 먼저 작성하고 tablet, desktop에서 확장하는 방식이다.

Q. Design System에도 반응형 기준이 필요해?
A. 필요하다. 컴포넌트와 레이아웃이 같은 breakpoint 기준을 공유해야 한다.

Q. breakpoint는 고정값이야?
A. 아니다. 일반 기준은 있지만 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

---

## 4.2 Mobile First Rules

### [개념]

Mobile First Rules는 작은 화면을 기본 기준으로 UI를 설계하고 큰 화면에서 점진적으로 확장하는 방식이다.

Mobile First는 모바일 깨짐을 줄이고 핵심 콘텐츠 중심의 화면 구성을 돕는다.

---

### [핵심]

Mobile First 기준:

- 기본 CSS는 모바일 기준
- tablet / desktop은 min-width media query로 확장
- 1열 layout에서 시작
- 복잡한 sidebar는 desktop에서 확장
- touch target 고려
- 모바일 navigation 별도 고려
- table overflow 대응
- modal max height 고려
- form field 세로 배치 우선

---

### [실무]

나쁜 예:

```css
.layout {
  display: grid;
  grid-template-columns: 240px 1fr;
}

@media (max-width: 767px) {
  .layout {
    display: block;
  }
}
```

좋은 예:

```css
.layout {
  display: block;
}

@media (min-width: 1024px) {
  .layout {
    display: grid;
    grid-template-columns: 240px 1fr;
    gap: var(--spacing-6);
  }
}
```

Review 기준:

```md
- [ ] 기본 스타일이 모바일 기준인가?
- [ ] desktop 전용 layout이 모바일을 깨뜨리지 않는가?
- [ ] 모바일에서 form / button / table이 사용 가능한가?
- [ ] min-width 기반 media query를 사용하는가?
```

---

### [FAQ]

Q. Mobile First는 왜 좋아?
A. 작은 화면에서 핵심 UI를 먼저 보장하고 큰 화면에서 점진적으로 확장할 수 있기 때문이다.

Q. max-width media query를 쓰면 안 돼?
A. 쓸 수 있지만 Design System 기준은 mobile first와 min-width 확장을 우선한다.

Q. 모바일에서 sidebar는 어떻게 처리해?
A. 숨김, drawer, bottom navigation, collapsible menu 같은 패턴을 고려한다.

Q. 모바일에서 form은 어떻게 배치해?
A. 기본적으로 세로 Stack 배치가 안정적이다.

---

## 4.3 Responsive Component Rules

### [개념]

Responsive Component Rules는 컴포넌트가 화면 크기에 따라 깨지지 않고 자연스럽게 동작하도록 만드는 기준이다.

컴포넌트는 독립적으로 보일 때뿐 아니라 Layout 안에서도 반응형을 고려해야 한다.

---

### [핵심]

컴포넌트별 반응형 기준:

```text
Button Group
→ 모바일에서 세로 배치 또는 wrap

Card Grid
→ 1열 → 2열 → 3열

Modal
→ 모바일에서 max-width / max-height 조정

Table
→ overflow-x 또는 카드형 변환

Form
→ 모바일 1열, desktop 2열 가능

Navigation
→ 모바일 drawer / bottom nav 고려

Tabs
→ 모바일 horizontal scroll 또는 select 대체 고려

Toast
→ 모바일 width와 position 조정
```

---

### [실무]

Responsive Button Group 예:

```css
.buttonGroup {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-3);
}

@media (min-width: 768px) {
  .buttonGroup {
    flex-direction: row;
    justify-content: flex-end;
  }
}
```

Responsive Modal 예:

```css
.modal {
  width: min(100% - 32px, 560px);
  max-height: min(90vh, 720px);
  overflow: auto;
}
```

Responsive Form 예:

```css
.formGrid {
  display: grid;
  gap: var(--spacing-4);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .formGrid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

---

### [FAQ]

Q. 컴포넌트도 반응형을 고려해야 해?
A. 필요하다. Button Group, Modal, Table, Form은 화면 크기에 따라 배치가 달라질 수 있다.

Q. 모바일에서 Button Group은 어떻게 해?
A. 세로 배치 또는 wrap을 고려해 버튼이 화면 밖으로 나가지 않게 한다.

Q. 모바일에서 Modal은 어떻게 해?
A. 화면 너비와 높이를 넘지 않도록 width, max-height, overflow 기준을 둔다.

Q. 모바일에서 Tabs가 많으면 어떻게 해?
A. horizontal scroll, select 대체, navigation 구조 변경을 고려한다.

---

## 4.4 Table Responsive Rules

### [개념]

Table Responsive Rules는 행과 열 구조 데이터를 모바일 화면에서 사용할 수 있게 만드는 기준이다.

Table은 데스크톱에서는 자연스럽지만 모바일에서는 가로 폭이 부족해 별도 대응이 필요하다.

---

### [핵심]

모바일 Table 대응 방식:

```text
Horizontal Scroll
→ 컬럼 유지, 가로 스크롤 허용

Card Transformation
→ 행 데이터를 카드 형태로 변환

Priority Columns
→ 주요 컬럼만 표시

Detail Page
→ 목록은 요약, 상세는 별도 화면

Column Toggle
→ 사용자가 컬럼 표시 선택
```

기준:

- 데이터 성격에 맞는 방식 선택
- 중요한 컬럼 우선 표시
- 가로 스크롤 안내 고려
- header와 cell 관계 유지
- Empty / Loading State 유지
- action column 모바일 대응

---

### [실무]

Horizontal Scroll 예:

```css
.tableWrapper {
  overflow-x: auto;
}

.table {
  min-width: 720px;
}
```

Card Transformation 예:

```jsx
<div className="mobileCardList">
  {rows.map((row) => (
    <Card key={row.id}>
      <CardHeader>
        <CardTitle>{row.lotNo}</CardTitle>
      </CardHeader>
      <CardBody>
        <p>상태: {row.status}</p>
        <p>완료 수량: {row.completedQty}EA</p>
      </CardBody>
    </Card>
  ))}
</div>
```

Review 기준:

```md
- [ ] 모바일 table 대응 방식이 정의되어 있는가?
- [ ] 가로 스크롤이 필요한 경우 wrapper가 있는가?
- [ ] 주요 컬럼이 모바일에서 확인 가능한가?
- [ ] action button이 모바일에서 사용 가능한가?
```

---

### [FAQ]

Q. 모바일에서 table은 어떻게 처리해?
A. 가로 스크롤, 카드형 변환, 주요 컬럼만 표시 등 프로젝트 기준을 정해야 한다.

Q. Horizontal Scroll은 나쁜 방식이야?
A. 아니다. 많은 컬럼을 보존해야 하는 관리자 화면에서는 현실적인 방식이다.

Q. Table을 Card로 변환해도 돼?
A. 가능하다. 모바일에서 행 단위 정보를 읽기 쉽게 만들 수 있다.

Q. 모바일 table에서 가장 중요한 것은?
A. 핵심 데이터를 확인하고 필요한 action을 수행할 수 있어야 한다.

---

## 4.5 Responsive Mistakes

### [개념]

Responsive Mistakes는 desktop 기준으로만 UI를 만들고 모바일, 태블릿 대응을 누락하는 실수다.

Responsive 실수는 모바일 화면 깨짐, 가로 스크롤, 버튼 조작 어려움, table 사용 불가 문제를 만든다.

---

### [핵심]

자주 발생하는 실수:

- desktop layout만 작성
- 모바일에서 가로 스크롤 발생
- button group이 화면 밖으로 나감
- table overflow 대응 없음
- modal이 모바일 화면을 넘음
- form 2열 layout이 모바일에서 깨짐
- touch target이 너무 작음
- navigation 모바일 대응 없음
- typography가 모바일에서 과도하게 큼
- spacing이 모바일에서 과도함
- chart / image overflow 방치

---

### [실무]

Troubleshooting:

```text
모바일에서 가로 스크롤 발생
→ width fixed / table / image overflow 확인

버튼이 화면 밖으로 나감
→ button group wrap 또는 column 전환

Modal이 잘림
→ max-height / overflow auto 적용

Form이 좁게 깨짐
→ mobile 1열 layout 적용

Table이 깨짐
→ table wrapper overflow-x 적용
```

Review Checklist:

```md
- [ ] 모바일에서 가로 스크롤이 없는가?
- [ ] interactive element가 터치하기 충분한가?
- [ ] Modal / Table / Form 모바일 대응이 있는가?
- [ ] typography와 spacing이 모바일에 적절한가?
- [ ] navigation이 모바일에서 사용 가능한가?
```

---

### [FAQ]

Q. Responsive에서 가장 흔한 실수는?
A. desktop에서는 정상인데 모바일에서 table, modal, button group이 깨지는 것이다.

Q. 모바일 가로 스크롤은 항상 문제야?
A. 페이지 전체 가로 스크롤은 문제다. 단, table wrapper 내부 가로 스크롤은 허용할 수 있다.

Q. 모바일에서 버튼이 작아도 돼?
A. 권장하지 않는다. 터치 가능한 충분한 영역을 제공해야 한다.

Q. 반응형 검토는 언제 해야 해?
A. 화면 구현 후가 아니라 layout 설계 단계부터 함께 해야 한다.

---

# 5. Navigation Layout Rules

## 5.1 App Shell Rules

### [개념]

App Shell은 애플리케이션의 공통 구조를 담당하는 layout이다.

App Shell은 Header, Sidebar, Main, Footer, Navigation, User Menu 같은 반복 영역을 포함한다.

---

### [핵심]

App Shell 구성:

```text
Header
→ Navigation
→ Sidebar
→ Main
→ Footer
```

App Shell 기준:

- route별 공통 layout 제공
- main content 영역 명확화
- navigation 접근성 고려
- 현재 위치 표시
- 모바일 navigation 대응
- header height 기준 통일
- sidebar collapse / drawer 고려
- content overflow 관리

---

### [실무]

App Shell 예:

```jsx
<AppShell>
  <Header />
  <Sidebar />
  <main>
    <Outlet />
  </main>
</AppShell>
```

CSS 예:

```css
.appShell {
  min-height: 100vh;
  display: grid;
  grid-template-rows: auto 1fr;
}

.appMain {
  min-width: 0;
}
```

Desktop Sidebar 예:

```css
@media (min-width: 1024px) {
  .appShell {
    grid-template-columns: 240px 1fr;
  }

  .header {
    grid-column: 1 / -1;
  }
}
```

---

### [FAQ]

Q. App Shell이 뭐야?
A. Header, Sidebar, Main 같은 애플리케이션 공통 구조를 담당하는 layout이다.

Q. App Shell은 왜 필요해?
A. 페이지마다 공통 navigation과 main 영역을 일관되게 유지하기 위해 필요하다.

Q. main 영역은 왜 중요해?
A. 주요 콘텐츠 영역을 semantic하게 구분하고 접근성 탐색을 돕는다.

Q. Sidebar는 모바일에서 어떻게 해?
A. Drawer, collapse, bottom navigation, hidden menu 같은 방식으로 대응한다.

---

## 5.2 Navigation Rules

### [개념]

Navigation은 사용자가 애플리케이션의 주요 화면으로 이동할 수 있게 하는 구조다.

Navigation은 현재 위치, 이동 대상, 권한에 따른 접근 가능 여부를 명확히 보여야 한다.

---

### [핵심]

Navigation 기준:

- Link 사용
- 현재 위치 active 상태 표시
- aria-current 사용 고려
- keyboard 탐색 가능
- 권한별 메뉴 표시 기준 명확화
- 모바일 navigation 대응
- 너무 많은 메뉴 노출 금지
- 메뉴 그룹화 고려
- icon만 있는 navigation은 accessible name 필요

---

### [실무]

Navigation 예:

```jsx
<nav aria-label="주요 메뉴">
  <NavLink to="/dashboard">대시보드</NavLink>
  <NavLink to="/lots">LOT 관리</NavLink>
  <NavLink to="/equipment">설비 관리</NavLink>
</nav>
```

Active Link 예:

```jsx
<NavLink to="/lots" aria-current={isActive ? "page" : undefined}>
  LOT 관리
</NavLink>
```

Review 기준:

```md
- [ ] navigation이 nav landmark를 사용하는가?
- [ ] 현재 위치가 명확한가?
- [ ] keyboard로 이동 가능한가?
- [ ] 모바일 navigation이 있는가?
- [ ] icon-only menu에 accessible name이 있는가?
```

---

### [FAQ]

Q. Navigation에는 Button과 Link 중 뭐를 써야 해?
A. 페이지 이동은 Link를 사용한다. Button은 행동 실행에 사용한다.

Q. 현재 페이지는 어떻게 표시해?
A. active style과 `aria-current="page"`를 고려한다.

Q. icon만 있는 navigation은 어떻게 접근성 처리해?
A. `aria-label` 또는 보이는 텍스트를 제공해야 한다.

Q. 권한별 메뉴는 어떻게 처리해?
A. 사용자 권한에 따라 표시 여부를 제어하고 접근 불가 화면도 별도로 처리해야 한다.

---

## 5.3 Sidebar Drawer Rules

### [개념]

Sidebar / Drawer는 주요 메뉴나 보조 탐색을 제공하는 layout component다.

Sidebar는 데스크톱에서 고정 영역으로 사용하고, Drawer는 모바일에서 임시 패널로 사용할 수 있다.

---

### [핵심]

Sidebar 기준:

- desktop에서 사용 적합
- 현재 메뉴 active 표시
- collapse 가능성 검토
- main content와 width 충돌 방지
- scroll 영역 관리

Drawer 기준:

- 모바일 navigation에 적합
- open / closed 상태 필요
- overlay 필요성 검토
- 닫기 버튼 제공
- ESC 닫기 고려
- focus 관리 고려
- 배경 스크롤 방지 고려

---

### [실무]

Responsive Sidebar / Drawer Flow:

```text
mobile
→ Drawer Navigation

tablet
→ Drawer 또는 Collapsed Sidebar

desktop
→ Fixed Sidebar
```

Drawer 예:

```jsx
<Drawer isOpen={isOpen} title="메뉴" onClose={closeDrawer}>
  <Navigation />
</Drawer>
```

Review 기준:

```md
- [ ] sidebar가 desktop layout에서 content를 가리지 않는가?
- [ ] drawer에 닫기 버튼이 있는가?
- [ ] drawer open 상태에서 focus 관리가 되는가?
- [ ] 모바일 navigation을 사용할 수 있는가?
```

---

### [FAQ]

Q. Sidebar와 Drawer는 뭐가 달라?
A. Sidebar는 보통 데스크톱의 고정 탐색 영역이고, Drawer는 필요할 때 열리는 임시 패널이다.

Q. 모바일에서 Sidebar를 그대로 보여줘도 돼?
A. 대부분 어렵다. Drawer나 bottom navigation으로 전환하는 것이 좋다.

Q. Drawer에도 접근성이 필요해?
A. 필요하다. 닫기 버튼, focus 관리, keyboard 조작을 고려해야 한다.

Q. Drawer는 Modal과 비슷해?
A. 화면 위에 뜨고 focus 관리가 필요하다는 점에서 비슷하지만 주로 navigation이나 보조 패널에 사용한다.

---

# 6. Theme System Rules

## 6.1 Theme System Definition

### [개념]

Theme System은 같은 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환할 수 있도록 만드는 구조다.

Theme System은 Light Mode, Dark Mode, Brand Theme, User Preference를 token 기반으로 관리한다.

---

### [핵심]

Theme System 구성:

```text
Primitive Token
→ Semantic Token
→ Theme Value
→ Component Token
→ Component Style
```

Theme 대상:

- background
- surface
- text
- text-muted
- border
- primary
- error
- warning
- success
- focus-ring
- overlay
- disabled
- shadow
- icon
- chart color

Theme 기준:

- raw color 직접 사용 금지
- semantic token 기반
- component style은 theme 이름을 몰라도 동작
- dark mode contrast 검토
- user preference 저장 가능
- system preference 대응 가능

---

### [실무]

Theme 기본 예:

```css
:root {
  --color-background: #ffffff;
  --color-surface: #f9fafb;
  --color-text: #111827;
  --color-text-muted: #6b7280;
  --color-border: #e5e7eb;
}

[data-theme="dark"] {
  --color-background: #111827;
  --color-surface: #1f2937;
  --color-text: #f9fafb;
  --color-text-muted: #d1d5db;
  --color-border: #374151;
}
```

Component Style 예:

```css
.card {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid var(--color-border);
}
```

Review 기준:

```md
- [ ] 컴포넌트가 raw color 대신 semantic token을 사용하는가?
- [ ] light / dark token이 구분되어 있는가?
- [ ] background / surface / text / border가 정의되어 있는가?
- [ ] focus ring이 모든 theme에서 보이는가?
```

---

### [FAQ]

Q. Theme System이 뭐야?
A. 같은 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환하는 구조다.

Q. Theme를 만들려면 CSS variable이 좋아?
A. CSS variable은 런타임 theme 전환에 유리하다.

Q. 컴포넌트에서 raw color를 쓰면 왜 문제야?
A. theme 변경 시 컴포넌트마다 직접 수정해야 하므로 확장성이 떨어진다.

Q. Theme System에서 가장 중요한 token은?
A. background, surface, text, border, primary, error, focus-ring token이 중요하다.

---

## 6.2 Dark Mode Rules

### [개념]

Dark Mode는 어두운 배경과 밝은 텍스트를 사용하는 theme다.

Dark Mode는 단순히 배경만 검게 바꾸는 것이 아니라 text, surface, border, disabled, hover, focus, icon까지 함께 조정해야 한다.

---

### [핵심]

Dark Mode 필수 확인:

```md
- [ ] background와 text contrast
- [ ] surface 색상
- [ ] border 색상
- [ ] muted text 색상
- [ ] disabled 색상
- [ ] hover 색상
- [ ] active 색상
- [ ] focus ring 색상
- [ ] shadow 대체
- [ ] icon visibility
- [ ] overlay 색상
- [ ] chart color
```

Dark Mode 기준:

- semantic token 재정의
- raw color 제거
- image / icon visibility 확인
- shadow만 의존하지 않음
- focus ring contrast 확보
- disabled text 가독성 확보
- error / warning 색상 contrast 확인

---

### [실무]

Dark Mode 예:

```css
[data-theme="dark"] {
  --color-background: #111827;
  --color-surface: #1f2937;
  --color-surface-muted: #374151;

  --color-text: #f9fafb;
  --color-text-muted: #d1d5db;

  --color-border: #374151;
  --color-border-strong: #4b5563;

  --color-primary: #60a5fa;
  --color-primary-hover: #93c5fd;

  --color-error: #f87171;
  --color-warning: #fbbf24;
  --color-success: #4ade80;
  --color-focus-ring: #93c5fd;
}
```

Dark Mode Review:

```md
- [ ] dark mode에서 text가 읽히는가?
- [ ] surface와 background가 구분되는가?
- [ ] focus ring이 보이는가?
- [ ] raw color가 dark mode에서 깨지지 않는가?
- [ ] icon과 chart 색상이 보이는가?
```

---

### [FAQ]

Q. Dark Mode는 배경만 검게 바꾸면 돼?
A. 아니다. text, border, surface, disabled, hover, focus, icon까지 함께 조정해야 한다.

Q. Dark Mode에서 가장 중요한 것은?
A. background, surface, text, border, focus-ring contrast를 유지하는 것이다.

Q. Dark Mode에서 shadow가 잘 안 보이면 어떻게 해?
A. surface 색상, border, overlay를 함께 사용해 depth를 표현한다.

Q. Dark Mode가 필수야?
A. 요구사항이 아니라면 필수는 아니지만 token 기반 구조로 확장 가능하게 만드는 것이 좋다.

---

## 6.3 Theme Preference Rules

### [개념]

Theme Preference Rules는 사용자의 theme 선택을 저장하고 적용하는 기준이다.

Theme Preference는 System Preference, User Preference, Default Theme의 우선순위를 명확히 해야 한다.

---

### [핵심]

Theme Preference 우선순위:

```text
User Preference
→ System Preference
→ Default Theme
```

Theme Preference 종류:

- light
- dark
- system

적용 기준:

- 사용자가 직접 선택하면 우선 적용
- system 선택 시 OS 설정 반영
- 선택값 localStorage 저장 가능
- 초기 로딩 시 flash 방지 고려
- data-theme attribute 사용 가능
- 접근성 contrast 유지

---

### [실무]

Theme attribute 예:

```html
<html data-theme="dark"></html>
```

Theme 선택 예:

```tsx
type ThemePreference = "light" | "dark" | "system";
```

적용 Flow:

```text
App Start
→ saved theme preference 확인
→ system preference 확인
→ resolved theme 결정
→ document data-theme 적용
```

Review 기준:

```md
- [ ] theme preference 우선순위가 명확한가?
- [ ] system preference를 고려하는가?
- [ ] 초기 화면 flash를 고려하는가?
- [ ] 저장된 preference가 일관되게 적용되는가?
```

---

### [FAQ]

Q. Theme Preference는 뭐야?
A. 사용자가 light, dark, system theme 중 어떤 방식을 사용할지 선택하는 설정이다.

Q. Theme 우선순위는 어떻게 정해?
A. 사용자 선택이 가장 우선이고, 그 다음 system preference, 마지막 default theme 순서가 좋다.

Q. theme 선택은 어디에 저장해?
A. 웹에서는 localStorage에 저장할 수 있다.

Q. system theme은 어떻게 처리해?
A. `prefers-color-scheme`을 확인해 OS 설정을 반영한다.

---

## 6.4 Theme Mistakes

### [개념]

Theme Mistakes는 token 기반 구조 없이 raw color를 직접 사용하거나 dark mode 대응을 일부 색상만 바꾸는 실수다.

Theme 실수는 dark mode 깨짐, 접근성 contrast 문제, 유지보수 문제를 만든다.

---

### [핵심]

자주 발생하는 실수:

- raw hex color 직접 사용
- semantic token 없이 color palette만 사용
- dark mode에서 background만 변경
- text / border / surface 미변경
- focus ring이 dark mode에서 안 보임
- disabled text가 너무 흐림
- icon 색상이 보이지 않음
- chart color가 theme과 충돌
- shadow만으로 depth 표현
- theme preference 저장 안 됨
- 초기 theme flash 방치

---

### [실무]

Troubleshooting:

```text
Dark Mode에서 글자가 안 보임
→ color-text / color-background contrast 확인

Card가 배경과 구분 안 됨
→ color-surface / color-border 확인

Focus ring이 안 보임
→ color-focus-ring dark token 확인

Icon이 안 보임
→ currentColor 또는 icon token 확인

Theme 변경해도 일부 컴포넌트 색이 그대로임
→ raw color 제거
```

Review Checklist:

```md
- [ ] semantic token 기반 theme 구조인가?
- [ ] raw color가 컴포넌트에 흩어져 있지 않은가?
- [ ] dark mode에서 contrast가 유지되는가?
- [ ] focus / disabled / icon 상태가 theme별로 보이는가?
- [ ] theme preference 적용 기준이 있는가?
```

---

### [FAQ]

Q. Theme에서 가장 흔한 실수는?
A. 컴포넌트에 raw color를 직접 쓰고 dark mode에서 background만 바꾸는 것이다.

Q. Dark Mode에서 text만 바꾸면 돼?
A. 아니다. surface, border, disabled, hover, focus, icon까지 확인해야 한다.

Q. Theme 변경 시 일부 컴포넌트 색이 안 바뀌는 이유는?
A. 대부분 raw color를 직접 사용했기 때문이다.

Q. Theme에서 focus ring도 봐야 해?
A. 반드시 봐야 한다. 모든 theme에서 keyboard focus가 보여야 한다.

---

# 7. Responsive Theme Layout Review Rules

## 7.1 Frontend Agent Layout Rules

### [개념]

Frontend Agent Layout Rules는 Frontend Agent가 화면을 만들 때 Layout System, Responsive 기준, Theme System을 함께 적용하는 규칙이다.

Frontend Agent는 정상 desktop 화면만 생성하지 않고 모바일, theme, layout consistency를 함께 고려해야 한다.

---

### [핵심]

Frontend Agent 생성 기준:

- Container 사용
- Page Layout 사용
- Section 구조 명확화
- Grid / Stack / Inline 적절히 선택
- spacing token 사용
- component margin 남용 금지
- mobile first 적용
- table / modal / form responsive 고려
- theme semantic token 사용
- raw color 직접 사용 금지
- dark mode 확장 가능성 고려

---

### [실무]

Frontend Agent Flow:

```text
Requirement 분석
→ Page Layout 선택
→ Container 적용
→ Section 구성
→ Grid / Stack / Inline 선택
→ Component 배치
→ Mobile First 적용
→ Theme Token 적용
→ Responsive 검토
→ Output
```

생성 전 체크:

```md
- [ ] 이 화면은 Container가 필요한가?
- [ ] section 구조가 명확한가?
- [ ] Grid / Stack / Inline 중 무엇이 적절한가?
- [ ] 모바일에서 몇 열이 적절한가?
- [ ] Table / Modal 모바일 대응이 필요한가?
- [ ] raw color 없이 semantic token을 사용하는가?
```

---

### [FAQ]

Q. Frontend Agent는 Layout을 어떻게 적용해?
A. Page Layout, Container, Section, Grid, Stack, Inline을 선택하고 mobile first와 theme token을 함께 적용한다.

Q. Frontend Agent가 desktop 화면만 만들면 안 돼?
A. 안 된다. 모바일과 반응형 상태를 함께 고려해야 한다.

Q. Layout 생성 전 가장 먼저 확인할 것은?
A. 페이지 구조, 콘텐츠 그룹, Container 필요성, responsive column 기준이다.

Q. theme를 고려하지 않고 색상을 직접 쓰면 안 돼?
A. 공통 UI에서는 semantic token을 사용해야 theme 확장이 가능하다.

---

## 7.2 Review Agent Layout Responsive Theme Checklist

### [개념]

Review Agent Layout Responsive Theme Checklist는 구현된 화면이 Layout, Responsive, Theme 기준을 만족하는지 검토하는 기준이다.

Review Agent는 화면이 desktop에서만 정상인지가 아니라 모바일과 theme 확장성까지 확인해야 한다.

---

### [핵심]

Review Checklist:

```md
## Layout

- [ ] Container 기준이 적용되는가?
- [ ] Page Layout 구조가 명확한가?
- [ ] Section 구조가 명확한가?
- [ ] Grid / Stack / Inline 선택이 적절한가?
- [ ] spacing token을 사용하는가?
- [ ] component margin이 남용되지 않는가?

## Responsive

- [ ] Mobile First 기준인가?
- [ ] 모바일에서 가로 스크롤이 없는가?
- [ ] Button Group이 모바일에서 깨지지 않는가?
- [ ] Modal이 모바일 화면을 넘지 않는가?
- [ ] Table 모바일 대응 기준이 있는가?
- [ ] Form이 모바일에서 1열로 사용 가능한가?
- [ ] touch target이 충분한가?

## Theme

- [ ] semantic token을 사용하는가?
- [ ] raw color가 남발되지 않는가?
- [ ] dark mode 확장이 가능한가?
- [ ] background / surface / text / border가 구분되는가?
- [ ] focus ring이 모든 theme에서 보이는가?
```

---

### [실무]

Review Decision:

```text
Approved
→ Layout, Responsive, Theme 기준 충족

Needs Fix
→ 일부 모바일 배치, spacing, theme token 미흡

Blocked
→ 모바일 사용 불가, 주요 layout 깨짐, theme contrast 심각 문제
```

Blocked 예:

```text
모바일에서 전체 페이지 가로 스크롤 발생
Modal 닫기 버튼이 화면 밖으로 나감
Table action button 사용 불가
Text가 dark mode에서 보이지 않음
Button focus ring이 안 보임
```

---

### [FAQ]

Q. Review Agent는 Layout에서 뭘 봐야 해?
A. Container, Section, Grid, Stack, spacing token, component margin 남용 여부를 확인해야 한다.

Q. Review Agent는 Responsive에서 뭘 봐야 해?
A. 모바일 가로 스크롤, table, modal, form, button group, touch target을 확인해야 한다.

Q. Review Agent는 Theme에서 뭘 봐야 해?
A. semantic token 사용, raw color 여부, dark mode contrast, focus ring visibility를 확인해야 한다.

Q. 모바일에서 화면이 깨지면 Blocked야?
A. 주요 기능 사용이 어렵다면 Blocked가 될 수 있다.

---

## 7.3 PM Agent Layout Completion Rules

### [개념]

PM Agent Layout Completion Rules는 PM Agent가 화면 완료 여부를 판단할 때 Layout, Responsive, Theme 관점에서 확인하는 기준이다.

PM Agent는 세부 CSS보다 사용자가 화면을 이해하고 모바일에서도 주요 기능을 사용할 수 있는지 확인한다.

---

### [핵심]

PM Agent 확인 기준:

- 화면 구조가 요구사항과 일치하는가
- 주요 정보가 눈에 잘 들어오는가
- 주요 action 위치가 명확한가
- 모바일에서 주요 흐름이 가능한가
- Table / Form / Modal이 모바일에서 사용 가능한가
- 화면 간 간격과 구성 일관성이 있는가
- dark mode 요구사항이 있으면 깨지지 않는가
- 접근성 심각 이슈가 없는가

---

### [실무]

PM 판단 Flow:

```text
Requirement 확인
→ Page Structure 확인
→ Main Action 확인
→ Mobile View 확인
→ Table / Modal / Form 확인
→ Theme Issue 확인
→ Completion Decision
```

PM Decision:

```text
UI Complete
→ 요구사항 충족 + layout / responsive 문제 없음

UI Partial
→ 기능은 가능하지만 일부 layout / responsive 개선 필요

UI Blocked
→ 모바일 사용 불가, 주요 action 접근 불가, 화면 구조 혼란
```

PM 체크 예:

```md
- [ ] 모바일에서 저장 버튼을 누를 수 있는가?
- [ ] 테이블 데이터를 확인할 수 있는가?
- [ ] Modal이 화면 밖으로 나가지 않는가?
- [ ] 주요 정보가 section별로 구분되는가?
```

---

### [FAQ]

Q. PM Agent는 Layout을 어떻게 봐야 해?
A. 사용자가 화면 구조를 이해하고 주요 action을 수행할 수 있는지 확인한다.

Q. PM Agent가 CSS 세부 구현까지 봐야 해?
A. 아니다. 화면 완료 여부, 사용자 흐름, 모바일 사용성, 심각 이슈 중심으로 판단한다.

Q. 모바일 이슈가 기능 완료를 막을 수 있어?
A. 그렇다. 모바일에서 주요 기능을 사용할 수 없다면 Blocker가 될 수 있다.

Q. Theme 이슈도 PM 판단 대상이야?
A. 요구사항에 theme가 포함되거나 text가 보이지 않는 심각 문제가 있으면 판단 대상이다.

---

# 8. Final Checklist

## 8.1 Part06 Quality Checklist

### [개념]

Part06 Quality Checklist는 Layout Responsive Theme Rules 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Layout Core

- [ ] Layout System 정의가 명확한가?
- [ ] Layout 책임 분리 기준이 있는가?
- [ ] Container 기준이 있는가?
- [ ] Page Layout 기준이 있는가?
- [ ] Section 기준이 있는가?

## Layout Pattern

- [ ] Grid Layout 기준이 있는가?
- [ ] Stack Layout 기준이 있는가?
- [ ] Inline Layout 기준이 있는가?
- [ ] Layout Mistakes가 포함되어 있는가?

## Responsive

- [ ] Responsive Design 정의가 명확한가?
- [ ] Mobile First 기준이 있는가?
- [ ] Responsive Component 기준이 있는가?
- [ ] Table Responsive 기준이 있는가?
- [ ] Responsive Mistakes가 포함되어 있는가?

## Navigation

- [ ] App Shell 기준이 있는가?
- [ ] Navigation 기준이 있는가?
- [ ] Sidebar / Drawer 기준이 있는가?

## Theme

- [ ] Theme System 기준이 있는가?
- [ ] Dark Mode 기준이 있는가?
- [ ] Theme Preference 기준이 있는가?
- [ ] Theme Mistakes가 포함되어 있는가?

## Agent Usage

- [ ] Frontend Agent 생성 기준이 있는가?
- [ ] Review Agent 검토 기준이 있는가?
- [ ] PM Agent 완료 판단 기준이 있는가?
```

---

### [실무]

Part06은 Part02 Design Token Rules의 spacing, breakpoint, theme token 기준과 Part04 Core Component Rules의 Modal, Table, Navigation 관련 기준을 확장한다.

Part 연계:

```text
Part01 Design System Core
→ Part02 Design Token Rules
→ Part03 Component Specification Rules
→ Part04 Core Component Rules
→ Part05 Feedback State Pattern Rules
→ Part06 Layout Responsive Theme Rules
→ Part07 Accessibility Documentation Review Rules
```

Part06 기준은 Frontend Agent가 실제 화면을 구성할 때 page structure, responsive behavior, theme compatibility를 판단하는 데 사용한다.

---

### [FAQ]

Q. Part06의 역할은 뭐야?
A. Layout System, Responsive Design, Navigation Layout, Theme System, Dark Mode 기준을 정의하는 문서다.

Q. Part06은 Part02와 어떻게 연결돼?
A. Part02의 spacing, breakpoint, color, theme token을 실제 layout과 responsive, theme 기준에 적용한다.

Q. Part06은 Part04와 어떻게 연결돼?
A. Part04의 Modal, Table, Navigation, Button Group 같은 component가 Part06의 layout과 responsive 기준을 사용한다.

Q. Part06 최종 승인 기준은 뭐야?
A. Frontend Agent가 화면 구조와 반응형, theme를 생성하고 Review Agent가 검토할 수 있을 만큼 기준과 FAQ가 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Layout System이 뭐야?
A. 페이지와 컴포넌트를 일관되게 배치하기 위한 Container, Section, Grid, Stack 같은 화면 구조 규칙이다.

Q. Layout System은 왜 필요해?
A. 페이지마다 간격과 배치가 달라지는 것을 막고 일관된 화면 구조를 만들기 위해 필요하다.

Q. 컴포넌트에 margin을 직접 주면 안 돼?
A. 재사용 컴포넌트라면 외부 배치는 부모 layout이 담당하는 것이 좋다.

Q. Component padding과 Layout gap은 뭐가 달라?
A. padding은 컴포넌트 내부 여백이고, gap은 부모가 자식 사이 간격을 조정하는 값이다.

Q. Container는 왜 필요해?
A. 페이지 콘텐츠 폭과 좌우 여백을 통일해 가독성과 화면 일관성을 유지하기 위해 필요하다.

Q. Page Layout은 왜 필요해?
A. 페이지마다 header, title, section, content 배치가 달라지는 것을 막기 위해 필요하다.

Q. main 태그는 꼭 필요해?
A. 권장된다. 페이지의 주요 콘텐츠 영역을 semantic하게 표시할 수 있다.

Q. Section은 언제 써?
A. 페이지 안에서 관련 콘텐츠를 제목과 함께 묶어 보여줄 때 사용한다.

Q. Section과 Card는 뭐가 달라?
A. Section은 페이지 구조 단위이고, Card는 정보를 시각적으로 묶는 컴포넌트다.

Q. Grid Layout은 언제 써?
A. 카드 목록, 대시보드, 통계 카드처럼 2차원 배치가 필요한 경우 사용한다.

Q. Grid gap은 어디서 관리해?
A. Grid parent에서 spacing token으로 관리한다.

Q. 모바일에서는 Grid를 어떻게 처리해?
A. 기본 1열로 시작하고 tablet, desktop에서 2열, 3열로 확장한다.

Q. Stack Layout은 언제 써?
A. Form Field, Section Body, Modal Body처럼 요소를 세로로 쌓을 때 사용한다.

Q. Stack에서 margin-bottom을 써도 돼?
A. 권장하지 않는다. parent gap으로 관리하는 것이 일관성에 좋다.

Q. Inline Layout은 언제 써?
A. 버튼 그룹, 액션 영역, 태그 목록처럼 요소를 가로로 배치할 때 사용한다.

Q. Button 사이 간격은 어떻게 관리해?
A. Button 자체 margin이 아니라 ButtonGroup 또는 Inline parent의 gap으로 관리한다.

Q. Layout에서 가장 흔한 실수는?
A. 컴포넌트마다 margin을 직접 넣고 parent gap을 사용하지 않는 것이다.

Q. Responsive Design이 뭐야?
A. 화면 크기에 따라 UI 구조와 배치가 자연스럽게 변하도록 만드는 기준이다.

Q. Mobile First가 뭐야?
A. 모바일 기본 스타일을 먼저 작성하고 tablet, desktop에서 확장하는 방식이다.

Q. Design System에도 반응형 기준이 필요해?
A. 필요하다. 컴포넌트와 레이아웃이 같은 breakpoint 기준을 공유해야 한다.

Q. breakpoint는 고정값이야?
A. 아니다. 일반 기준은 있지만 콘텐츠가 깨지는 지점을 기준으로 조정할 수 있다.

Q. Mobile First는 왜 좋아?
A. 작은 화면에서 핵심 UI를 먼저 보장하고 큰 화면에서 점진적으로 확장할 수 있기 때문이다.

Q. 모바일에서 form은 어떻게 배치해?
A. 기본적으로 세로 Stack 배치가 안정적이다.

Q. 컴포넌트도 반응형을 고려해야 해?
A. 필요하다. Button Group, Modal, Table, Form은 화면 크기에 따라 배치가 달라질 수 있다.

Q. 모바일에서 Button Group은 어떻게 해?
A. 세로 배치 또는 wrap을 고려해 버튼이 화면 밖으로 나가지 않게 한다.

Q. 모바일에서 Modal은 어떻게 해?
A. 화면 너비와 높이를 넘지 않도록 width, max-height, overflow 기준을 둔다.

Q. 모바일에서 table은 어떻게 처리해?
A. 가로 스크롤, 카드형 변환, 주요 컬럼만 표시 등 프로젝트 기준을 정해야 한다.

Q. Horizontal Scroll은 나쁜 방식이야?
A. 아니다. 많은 컬럼을 보존해야 하는 관리자 화면에서는 현실적인 방식이다.

Q. Table을 Card로 변환해도 돼?
A. 가능하다. 모바일에서 행 단위 정보를 읽기 쉽게 만들 수 있다.

Q. Responsive에서 가장 흔한 실수는?
A. desktop에서는 정상인데 모바일에서 table, modal, button group이 깨지는 것이다.

Q. App Shell이 뭐야?
A. Header, Sidebar, Main 같은 애플리케이션 공통 구조를 담당하는 layout이다.

Q. Navigation에는 Button과 Link 중 뭐를 써야 해?
A. 페이지 이동은 Link를 사용한다. Button은 행동 실행에 사용한다.

Q. 현재 페이지는 어떻게 표시해?
A. active style과 `aria-current="page"`를 고려한다.

Q. Sidebar와 Drawer는 뭐가 달라?
A. Sidebar는 보통 데스크톱의 고정 탐색 영역이고, Drawer는 필요할 때 열리는 임시 패널이다.

Q. 모바일에서 Sidebar를 그대로 보여줘도 돼?
A. 대부분 어렵다. Drawer나 bottom navigation으로 전환하는 것이 좋다.

Q. Theme System이 뭐야?
A. 같은 컴포넌트 구조를 유지하면서 색상과 시각 스타일을 전환하는 구조다.

Q. Theme를 만들려면 CSS variable이 좋아?
A. CSS variable은 런타임 theme 전환에 유리하다.

Q. 컴포넌트에서 raw color를 쓰면 왜 문제야?
A. theme 변경 시 컴포넌트마다 직접 수정해야 하므로 확장성이 떨어진다.

Q. Dark Mode는 배경만 검게 바꾸면 돼?
A. 아니다. text, border, surface, disabled, hover, focus, icon까지 함께 조정해야 한다.

Q. Dark Mode에서 가장 중요한 것은?
A. background, surface, text, border, focus-ring contrast를 유지하는 것이다.

Q. Theme Preference는 뭐야?
A. 사용자가 light, dark, system theme 중 어떤 방식을 사용할지 선택하는 설정이다.

Q. Theme 우선순위는 어떻게 정해?
A. 사용자 선택이 가장 우선이고, 그 다음 system preference, 마지막 default theme 순서가 좋다.

Q. Theme에서 가장 흔한 실수는?
A. 컴포넌트에 raw color를 직접 쓰고 dark mode에서 background만 바꾸는 것이다.

Q. Frontend Agent는 Layout을 어떻게 적용해?
A. Page Layout, Container, Section, Grid, Stack, Inline을 선택하고 mobile first와 theme token을 함께 적용한다.

Q. Review Agent는 Layout에서 뭘 봐야 해?
A. Container, Section, Grid, Stack, spacing token, component margin 남용 여부를 확인해야 한다.

Q. Review Agent는 Responsive에서 뭘 봐야 해?
A. 모바일 가로 스크롤, table, modal, form, button group, touch target을 확인해야 한다.

Q. Review Agent는 Theme에서 뭘 봐야 해?
A. semantic token 사용, raw color 여부, dark mode contrast, focus ring visibility를 확인해야 한다.

Q. PM Agent는 Layout을 어떻게 봐야 해?
A. 사용자가 화면 구조를 이해하고 주요 action을 수행할 수 있는지 확인한다.

Q. Part06의 역할은 뭐야?
A. Layout System, Responsive Design, Navigation Layout, Theme System, Dark Mode 기준을 정의하는 문서다.
