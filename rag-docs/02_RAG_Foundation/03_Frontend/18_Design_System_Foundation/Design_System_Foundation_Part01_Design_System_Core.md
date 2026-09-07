# Design System Foundation Part01 - Design System Core

---

# 1. Design System Core

## 1.1 Design System Definition

### [개념]

Design System은 프론트엔드 UI를 일관되게 생성하고 검토하기 위한 **Design Principles, Design Token, Component Specification, UI Pattern, Accessibility, Responsive, Theme, Documentation 규칙의 집합**이다.

Design System 문서는 사람 공부용 디자인 이론 문서가 아니다.

이 문서는 Frontend Agent / Review Agent / PM Agent가 실제 화면을 생성하고 검토하고 완료 여부를 판단할 때 사용하는 **RAG Retrieval 최적화 기준 문서**이다.

---

### [핵심]

Design System의 핵심 구성:

- Design Principles
- Design Token
- Component Specification
- Component Variant
- Component Size
- Component State
- UI Pattern
- Feedback State
- Accessibility Rules
- Responsive Rules
- Theme Rules
- Documentation Rules
- Review Checklist

Design System의 핵심 목적:

- UI 일관성 유지
- 공통 컴포넌트 재사용
- 디자인 값 하드코딩 감소
- 화면별 스타일 편차 감소
- 접근성 기본 품질 확보
- 반응형 기준 통일
- Frontend Agent 코드 생성 기준 제공
- Review Agent 검토 기준 제공
- PM Agent 완료 판단 기준 제공

---

### [실무]

2026 실무 기준에서 Design System은 단순히 예쁜 UI 모음이 아니다.

실무 Flow:

```text
Requirement
→ Design Principles
→ Design Token
→ Component Specification
→ Component Implementation
→ UI Pattern
→ Page Composition
→ Review Checklist
→ Product Consistency
```

Frontend Agent는 화면을 만들기 전에 Design System 기준을 먼저 확인한다.

Review Agent는 구현된 UI가 Design System 기준을 따르는지 검토한다.

PM Agent는 화면이 요구사항과 Design System 기준을 만족하는지 판단한다.

---

### [FAQ]

Q. Design System이 뭐야?
A. 제품 UI를 일관되게 만들기 위한 디자인 원칙, 토큰, 컴포넌트, 패턴, 문서화, 사용 규칙의 집합이다.

Q. Design System은 컴포넌트 라이브러리와 같아?
A. 아니다. 컴포넌트 라이브러리는 Design System의 일부다. Design System은 토큰, 상태, 변형, 접근성, 반응형, 사용 기준까지 포함한다.

Q. Design System 문서는 사람 공부용이야?
A. 아니다. Frontend Agent / Review Agent / PM Agent가 UI를 생성하고 검토하기 위한 RAG 문서다.

Q. 작은 프로젝트에도 Design System이 필요해?
A. 거대한 시스템은 필요 없지만 Button, Input, Card, Color, Spacing 정도의 미니 Design System은 필요하다.

---

## 1.2 Design System Purpose

### [개념]

Design System Purpose는 프론트엔드 화면이 프로젝트 전체에서 동일한 기준으로 생성되도록 만드는 목적이다.

Design System은 다음 문제를 해결한다.

```text
화면마다 다른 버튼
화면마다 다른 간격
화면마다 다른 색상
상태 처리 누락
접근성 누락
모바일 깨짐
리뷰 기준 불명확
Agent별 UI 판단 기준 불일치
```

---

### [핵심]

Design System이 해결하는 문제:

- 색상 직접 사용 문제
- spacing 값 하드코딩 문제
- Button variant 불일치
- Input label 누락
- Loading State 누락
- Empty State 누락
- Error State 누락
- Disabled State 누락
- Focus Style 누락
- Modal 접근성 누락
- Table 모바일 대응 누락
- Dark Mode 확장 불가
- Agent별 UI 판단 기준 불일치

---

### [실무]

Design System이 없으면 Agent는 화면마다 다른 UI를 생성할 가능성이 높다.

나쁜 흐름:

```text
Page Request
→ Agent 임의 스타일 생성
→ 화면별 UI 편차 발생
→ Review 기준 불명확
→ 유지보수 어려움
```

좋은 흐름:

```text
Page Request
→ Design System 확인
→ Token 사용
→ Component Spec 사용
→ State / Accessibility 반영
→ Review Checklist 통과
```

---

### [FAQ]

Q. Design System이 없으면 어떤 문제가 생겨?
A. 버튼, 입력, 카드, 간격, 색상, 상태 표현이 화면마다 달라지고 Review Agent가 승인 기준을 잡기 어렵다.

Q. Design System의 핵심 목적은 뭐야?
A. UI를 매번 새로 만들지 않고 정해진 토큰과 컴포넌트 기준으로 일관되게 만드는 것이다.

Q. Agent 시스템에서 Design System이 중요한 이유는?
A. Frontend Agent, Review Agent, PM Agent가 같은 UI 기준을 공유해야 결과물이 안정적이기 때문이다.

Q. Design System은 디자인 품질만 위한 거야?
A. 아니다. 재사용성, 접근성, 반응형, 유지보수성, 리뷰 기준까지 포함한다.

---

## 1.3 Design System Scope

### [개념]

Design System Scope는 이 문서가 다루는 UI 기준의 범위다.

이 문서는 Frontend Foundation 단계에서 필요한 실무 Design System 기준을 포함한다.

---

### [핵심]

포함 범위:

- Design System 개념
- Design Principles
- Design Token
- Color Token
- Typography Token
- Spacing Token
- Radius Token
- Shadow Token
- Z-index Token
- Motion Token
- Breakpoint Token
- Component Specification
- Button
- Input
- Form Field
- Select
- Checkbox
- Radio
- Card
- Badge
- Tag
- Alert
- Toast
- Modal
- Tabs
- Pagination
- Table
- Loading State
- Empty State
- Error State
- Success State
- Layout System
- Responsive Layout
- Theme
- Dark Mode
- Accessibility
- Documentation
- Review Checklist

제외 범위:

- Figma 운영 심화
- Design Ops 심화
- Brand Identity 전체 전략
- Motion Design System 심화
- Advanced Animation Library
- Enterprise Design Governance
- Multi-brand Design System
- Token Build Pipeline 심화
- Style Dictionary 심화
- Monorepo Package Publishing 심화
- Storybook Addon 심화
- Native App Design System
- Advanced Visual Regression Testing

---

### [실무]

Design System Foundation은 다음 문서들과 연결된다.

```text
HTML CSS Foundation
→ React Component Design
→ UI Component Pattern
→ Frontend Accessibility
→ Styling Architecture
→ Design System Foundation
→ Frontend Code Review
```

위임 기준:

```text
스타일 파일 구조
→ Styling Architecture

컴포넌트 코드 설계
→ React Component Design

컴포넌트 패턴
→ UI Component Pattern

접근성 상세 기준
→ Frontend Accessibility

테스트 상세 기준
→ Frontend Testing

빌드 / 배포
→ Frontend Build Deploy
```

---

### [FAQ]

Q. Design System 문서에 모든 컴포넌트를 다 넣어야 해?
A. 아니다. 프로젝트에서 반복 사용되는 핵심 컴포넌트부터 정의한다.

Q. Design System과 Styling Architecture는 뭐가 달라?
A. Styling Architecture는 스타일 코드 구조이고, Design System은 토큰, 컴포넌트 규격, 상태, 패턴, 사용 기준까지 포함한다.

Q. UI Component Pattern 문서와 겹치지 않아?
A. UI Component Pattern은 패턴 중심이고, Design System은 토큰, 규격, 상태, 변형, 리뷰 기준까지 포함한다.

Q. Storybook 심화 운영도 포함해?
A. 아니다. 기초 문서화와 예시 수준은 가능하지만 Storybook 심화 운영은 제외한다.

---

# 2. Design Principles

## 2.1 Design Principles Overview

### [개념]

Design Principles는 UI를 만들 때 지켜야 하는 상위 원칙이다.

Design Principles는 컴포넌트 규칙만으로 판단하기 어려운 상황에서 Agent가 우선순위를 결정하는 기준이다.

---

### [핵심]

권장 Design Principles:

- Consistency
- Clarity
- Accessibility
- Feedback
- Responsiveness
- Maintainability
- Scalability

정의:

```text
Consistency
→ 같은 의미의 UI는 같은 방식으로 표현한다.

Clarity
→ 사용자가 현재 상태와 다음 행동을 명확히 알 수 있어야 한다.

Accessibility
→ 키보드, 스크린 리더, 색각 다양성 사용자를 고려한다.

Feedback
→ 사용자 행동에 대한 loading, success, error 피드백을 제공한다.

Responsiveness
→ 모바일, 태블릿, 데스크톱 환경에서 화면이 자연스럽게 동작한다.

Maintainability
→ UI 변경이 토큰과 컴포넌트 기준으로 관리된다.

Scalability
→ 화면과 기능이 늘어나도 기존 규칙으로 확장 가능하다.
```

---

### [실무]

Frontend Agent UI 생성 우선순위:

```text
요구사항 충족
→ 사용자 흐름 명확성
→ 접근성
→ 일관성
→ 재사용성
→ 시각적 완성도
```

Review Agent 검토 우선순위:

```text
기능 사용 가능 여부
→ 주요 상태 처리 여부
→ 접근성 심각 이슈 여부
→ 반응형 깨짐 여부
→ Design Token / Component Spec 준수 여부
```

PM Agent 완료 판단 우선순위:

```text
요구사항 충족
→ 사용자 행동 가능
→ 상태 처리 존재
→ 화면 일관성
→ 출시 차단 이슈 없음
```

---

### [FAQ]

Q. Design Principles가 꼭 필요해?
A. 필요하다. 컴포넌트 규칙만으로 판단하기 어려운 상황에서 Agent의 상위 판단 기준이 된다.

Q. 예쁜 UI가 가장 중요해?
A. 아니다. 요구사항 충족, 사용성, 접근성, 일관성이 먼저다.

Q. Consistency는 무슨 뜻이야?
A. 같은 의미의 UI를 같은 방식으로 표현하는 것이다.

Q. Clarity는 무슨 뜻이야?
A. 사용자가 현재 상태와 다음 행동을 명확히 이해할 수 있게 하는 것이다.

---

## 2.2 Consistency Principle

### [개념]

Consistency는 같은 의미와 같은 기능을 가진 UI를 프로젝트 전체에서 같은 방식으로 표현하는 원칙이다.

---

### [핵심]

Consistency 기준:

- 같은 Primary Action은 같은 Button variant 사용
- 같은 위험 행동은 danger variant 사용
- 같은 입력 구조는 Form Field 사용
- 같은 상태는 같은 Badge variant 사용
- 같은 오류는 같은 Error State Pattern 사용
- 같은 목록 구조는 같은 Card / Table 기준 사용
- 같은 간격은 같은 Spacing Token 사용
- 같은 색상 의미는 같은 Color Token 사용

---

### [실무]

나쁜 예:

```jsx
<button className="blueBtn">저장</button>
<button className="saveButton">등록</button>
<button style={{ background: "#2563eb" }}>확인</button>
```

좋은 예:

```jsx
<Button variant="primary" type="submit">
  저장
</Button>
```

Review 기준:

```md
- [ ] 같은 행동이 같은 variant로 표현되는가?
- [ ] 화면마다 버튼 크기가 제각각이지 않은가?
- [ ] 색상 의미가 token으로 통일되어 있는가?
- [ ] 동일 상태 메시지가 같은 패턴을 사용하는가?
```

---

### [FAQ]

Q. Consistency가 중요한 이유는?
A. 사용자가 UI 의미를 빠르게 이해하고 Agent가 안정적으로 같은 기준의 화면을 생성할 수 있기 때문이다.

Q. 같은 색이면 같은 의미로 봐도 돼?
A. 아니다. 색상보다 semantic token과 variant 의미가 우선이다.

Q. 버튼 스타일이 화면마다 조금 달라도 괜찮아?
A. 공통 행동이면 같은 Button Spec을 따라야 한다. 임의 스타일은 일관성을 깨뜨린다.

Q. Consistency는 디자인만 보는 거야?
A. 아니다. 컴포넌트 API, 상태 처리, 메시지 문구, 반응형 기준까지 포함한다.

---

## 2.3 Clarity Principle

### [개념]

Clarity는 사용자가 화면의 현재 상태와 다음 행동을 명확하게 이해할 수 있도록 만드는 원칙이다.

---

### [핵심]

Clarity 기준:

- 버튼 텍스트는 행동 중심
- 에러 메시지는 사용자 친화적
- Empty State는 다음 행동 제공
- Loading State는 처리 중임을 표시
- Disabled 상태는 이유를 추론 가능하게 표현
- Form Error는 입력 필드 가까이에 표시
- 위험 행동은 danger style로 구분
- 주요 CTA는 시각적으로 명확하게 표시

---

### [실무]

나쁜 버튼 텍스트:

```text
OK
확인
처리
Submit
```

좋은 버튼 텍스트:

```text
저장
삭제
검색
다시 시도
필터 초기화
리뷰 등록
```

나쁜 에러 메시지:

```text
Error occurred.
500 Internal Server Error
Bad Request
```

좋은 에러 메시지:

```text
데이터를 불러오지 못했습니다.
네트워크 상태를 확인한 뒤 다시 시도해 주세요.
```

---

### [FAQ]

Q. Clarity가 중요한 이유는?
A. 사용자가 현재 상황과 다음 행동을 이해하지 못하면 기능이 있어도 사용성이 떨어지기 때문이다.

Q. 버튼 텍스트는 어떻게 써야 해?
A. 저장, 삭제, 검색, 다시 시도처럼 사용자가 수행할 행동을 동사 중심으로 작성한다.

Q. 에러 메시지는 어떻게 작성해?
A. 사용자가 이해할 수 있는 문장으로 실패 상황과 복구 방법을 안내한다.

Q. Empty State에는 무엇이 필요해?
A. 데이터가 없다는 설명과 사용자가 다음에 할 수 있는 행동이 필요하다.

---

## 2.4 Accessibility Principle

### [개념]

Accessibility는 키보드 사용자, 스크린 리더 사용자, 저시력 사용자, 색각 다양성 사용자가 UI를 사용할 수 있도록 설계하는 원칙이다.

---

### [핵심]

Accessibility 기본 기준:

- Semantic HTML 우선
- Button은 button 요소 사용
- Link는 a 또는 Router Link 사용
- Input은 label과 연결
- Error Message는 input과 연결
- Icon Button은 accessible name 제공
- Focus Visible 제공
- Keyboard 조작 가능
- 색상만으로 상태 전달 금지
- Modal은 dialog role과 title 연결
- Reduced Motion 고려
- Touch Target Size 고려

---

### [실무]

Form Field 접근성 예:

```jsx
<label htmlFor="email">이메일</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<p id="email-error" role="alert">
  올바른 이메일 형식이 아닙니다.
</p>
```

Icon Button 접근성 예:

```jsx
<button type="button" aria-label="검색">
  <SearchIcon aria-hidden="true" />
</button>
```

Focus Style 예:

```css
:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

---

### [FAQ]

Q. Design System에 접근성을 넣어야 해?
A. 반드시 넣어야 한다. 공통 컴포넌트가 접근성을 만족하면 전체 화면 품질이 올라간다.

Q. aria를 많이 넣으면 접근성이 좋아져?
A. 아니다. Semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. focus outline을 제거해도 돼?
A. 제거만 하면 안 된다. 반드시 대체 focus-visible style을 제공해야 한다.

Q. 색상만으로 상태를 표시해도 돼?
A. 안 된다. 텍스트, 아이콘, 메시지 등 추가 정보가 필요하다.

---

## 2.5 Feedback Principle

### [개념]

Feedback은 사용자 행동 이후 시스템이 어떤 상태인지 알려주는 원칙이다.

사용자가 저장, 삭제, 검색, 로그인, 제출, 결제 같은 행동을 수행하면 UI는 처리 중, 성공, 실패 상태를 명확히 알려야 한다.

---

### [핵심]

Feedback 필수 상태:

- Loading State
- Empty State
- Error State
- Success State
- Disabled State
- Validation State

상황별 Feedback:

```text
API 요청 중
→ Loading State

결과 없음
→ Empty State

요청 실패
→ Error State

작업 완료
→ Success State

중복 클릭 방지
→ Button Loading + Disabled

입력 오류
→ Form Validation Error
```

---

### [실무]

Button Loading 예:

```jsx
<Button type="submit" isLoading={isSubmitting} disabled={isSubmitting}>
  저장
</Button>
```

Error State 예:

```jsx
<ErrorState
  title="데이터를 불러오지 못했습니다"
  description="네트워크 상태를 확인한 뒤 다시 시도해 주세요."
  action={<Button onClick={refetch}>다시 시도</Button>}
/>
```

Empty State 예:

```jsx
<EmptyState
  title="검색 결과가 없습니다"
  description="다른 키워드나 지역으로 다시 검색해 보세요."
  action={<Button variant="secondary">필터 초기화</Button>}
/>
```

---

### [FAQ]

Q. Feedback State는 왜 필요해?
A. 사용자가 화면이 멈췄는지, 성공했는지, 실패했는지 알 수 있어야 하기 때문이다.

Q. Loading State는 언제 필요해?
A. 데이터 요청, 저장, 삭제, 로그인, 제출처럼 시간이 걸리는 작업에 필요하다.

Q. 중요한 오류를 Toast만으로 보여줘도 돼?
A. 권장하지 않는다. 사용자가 놓칠 수 있으므로 화면 내 Error State도 함께 제공하는 것이 좋다.

Q. 성공 메시지는 항상 필요해?
A. 사용자가 작업 완료를 확신해야 하는 행동에는 필요하다.

---

# 3. Agent Usage Rules

## 3.1 Frontend Agent Usage

### [개념]

Frontend Agent는 UI를 생성할 때 Design System 기준을 우선 적용한다.

Frontend Agent는 임의 스타일을 만들기 전에 기존 Token, Component Spec, Pattern을 확인해야 한다.

---

### [핵심]

Frontend Agent 기준:

- 기존 Design Token 사용
- 기존 Component Spec 사용
- 임의 variant 생성 금지
- Button / Input / Card / Modal 재사용
- Loading / Empty / Error State 포함
- 접근성 기본 반영
- Mobile First 기준 적용
- raw color 직접 사용 제한
- 임의 spacing 직접 사용 제한
- 새 패턴 필요 시 이유 명시

---

### [실무]

Frontend Agent UI 생성 Flow:

```text
Requirement 분석
→ Design System 확인
→ 필요한 Component 선택
→ Variant / Size / State 선택
→ Token 적용
→ Accessibility 적용
→ Responsive 적용
→ Feedback State 적용
→ Review Checklist 확인
→ UI Output
```

나쁜 생성:

```jsx
<div style={{ padding: "17px", color: "blue" }}>
  <button>OK</button>
</div>
```

좋은 생성:

```jsx
<Card>
  <CardHeader>
    <CardTitle>작업 목록</CardTitle>
  </CardHeader>
  <CardBody>
    <Button variant="primary" size="md">
      작업 등록
    </Button>
  </CardBody>
</Card>
```

---

### [FAQ]

Q. Frontend Agent는 Design System을 어떻게 사용해?
A. 기존 token과 component spec을 사용해 임의 스타일 생성을 줄이고 일관된 UI를 생성한다.

Q. Frontend Agent가 임의로 새 버튼 스타일을 만들어도 돼?
A. 기존 variant로 해결할 수 없을 때만 가능하다. 새 variant 추가 이유를 명확히 해야 한다.

Q. 공통 컴포넌트 대신 div로 직접 만들어도 돼?
A. 단순한 경우는 가능하지만 공통 UI가 이미 있다면 재사용하는 것이 좋다.

Q. Frontend Agent가 반드시 포함해야 하는 상태는?
A. Loading, Empty, Error, Disabled, Focus 상태를 우선 확인해야 한다.

---

## 3.2 Review Agent Usage

### [개념]

Review Agent는 Design System 기준으로 UI 품질을 검토한다.

Review Agent는 화면이 예쁜지보다 Token, Component Spec, State, Accessibility, Responsive 기준을 우선 검토한다.

---

### [핵심]

Review Agent 검토 기준:

- Token 사용 여부
- raw value 하드코딩 여부
- Component Spec 준수 여부
- Variant 의미 적절성
- Size 체계 일관성
- State 처리 여부
- Loading / Empty / Error 존재 여부
- Input label 연결 여부
- Icon Button accessible name 여부
- Focus Visible 존재 여부
- Modal 접근성 여부
- Mobile First 대응 여부
- Table 모바일 대응 여부
- Theme 확장 가능성
- Documentation 존재 여부

---

### [실무]

Review Agent 판단 Flow:

```text
Design System 기준 확인
→ Token 사용 확인
→ Component Spec 확인
→ Variant / Size / State 확인
→ Accessibility 확인
→ Responsive 확인
→ Theme 확장성 확인
→ Documentation 확인
→ Final Decision
```

Review Decision:

```text
Approved
→ 주요 Design System 기준 충족

Needs Fix
→ 기능은 가능하지만 UI 기준 일부 미흡

Blocked
→ 사용자 흐름 방해, 접근성 심각 문제, 모바일 깨짐, 주요 상태 누락
```

---

### [FAQ]

Q. Review Agent는 Design System에서 뭘 봐야 해?
A. Token, Component Spec, State, Accessibility, Responsive, Theme, Documentation 기준을 확인해야 한다.

Q. 디자인이 예쁘면 Design System 기준을 통과한 거야?
A. 아니다. 일관성, 재사용성, 접근성, 반응형, 문서화 기준까지 봐야 한다.

Q. raw color를 쓰면 무조건 반려야?
A. 공통 UI나 반복 스타일에서 raw color가 많으면 반려 대상이다. 의미 있는 token 사용이 우선이다.

Q. Review Agent가 가장 먼저 확인할 항목은?
A. Token, Component Spec, 주요 State, Accessibility, Responsive 기준이다.

---

## 3.3 PM Agent Usage

### [개념]

PM Agent는 Design System 기준을 사용해 화면 완료 여부를 판단한다.

PM Agent는 세부 구현보다 요구사항 충족, 사용자 흐름, 상태 처리, 화면 일관성, 출시 차단 이슈 여부를 중심으로 판단한다.

---

### [핵심]

PM Agent 완료 판단 기준:

- 화면이 요구사항과 일치하는가
- 주요 행동이 명확한가
- 주요 버튼과 입력이 일관적인가
- Loading / Empty / Error State가 있는가
- 모바일 화면이 깨지지 않는가
- 위험 행동이 danger style로 구분되는가
- 사용자 친화적 에러 메시지가 있는가
- 기능 사용을 막는 UI 문제가 없는가
- 접근성 심각 이슈가 없는가

---

### [실무]

PM Agent 판단 Flow:

```text
Requirement 확인
→ User Flow 확인
→ 주요 UI 요소 확인
→ Feedback State 확인
→ Mobile View 확인
→ Critical Issue 확인
→ Completion Decision
```

PM Decision:

```text
UI Complete
→ 요구사항 충족 + Design System 기준 충족

UI Partial
→ 기능은 가능하지만 일부 UI 기준 미흡

UI Blocked
→ 사용자 흐름 방해, 모바일 깨짐, 주요 상태 누락
```

---

### [FAQ]

Q. PM Agent는 Design System을 어떻게 써?
A. 화면이 요구사항과 일치하는지, UI가 일관적인지, 사용자 흐름이 명확한지 판단하는 데 사용한다.

Q. PM Agent는 디자인 토큰까지 봐야 해?
A. 세부 구현보다 화면 일관성, 사용자 흐름, 상태 처리, 완료 여부를 중심으로 판단한다.

Q. UI 이슈가 기능 완료를 막을 수 있어?
A. 사용자가 기능을 사용하기 어렵거나 모바일에서 깨지면 Blocker가 될 수 있다.

Q. PM Agent가 가장 중요하게 보는 것은?
A. 요구사항 충족, 사용자 흐름, 주요 상태 처리, 출시 차단 이슈 여부다.

---

# 4. Design System Maturity

## 4.1 Maturity Level

### [개념]

Design System은 한 번에 완성하지 않고 프로젝트 규모에 맞게 단계적으로 성장시킨다.

Foundation 단계에서는 완전한 Enterprise Design System보다 Agent가 일관된 UI를 생성할 수 있는 최소 기준을 우선 구축한다.

---

### [핵심]

Design System Maturity Level:

| Level   | 상태              | 구성                                |
| ------- | ----------------- | ----------------------------------- |
| Level 0 | 없음              | 화면마다 직접 스타일                |
| Level 1 | Basic Token       | color, spacing, typography token    |
| Level 2 | Core Components   | Button, Input, Card, Modal          |
| Level 3 | Pattern System    | Loading, Empty, Error, Form Pattern |
| Level 4 | Documented System | Spec, Do / Don't, Examples          |
| Level 5 | Managed System    | Versioning, Testing, Governance     |

---

### [실무]

학원 프로젝트 / 개인 프로젝트 권장 목표:

```text
Level 1 Basic Token
+ Level 2 Core Components
+ 일부 Level 3 Feedback Pattern
```

운영 서비스 권장 목표:

```text
Level 3 Pattern System
+ Level 4 Documented System
```

Agent 시스템 권장 목표:

```text
Level 1 Basic Token
→ Level 2 Core Components
→ Level 3 Feedback Pattern
→ Level 4 Documented System
```

---

### [FAQ]

Q. Design System은 처음부터 완성해야 해?
A. 아니다. token과 핵심 컴포넌트부터 시작해 단계적으로 확장하는 것이 좋다.

Q. 개인 AI 프로젝트에서는 어느 정도가 적당해?
A. Basic Token, Core Components, Feedback Pattern 기준까지 있으면 Frontend Agent가 일관된 UI를 만들기 좋다.

Q. Level 1은 뭐야?
A. color, spacing, typography 같은 기본 token이 있는 상태다.

Q. Level 2는 뭐야?
A. Button, Input, Card, Modal 같은 핵심 컴포넌트가 정의된 상태다.

---

## 4.2 Foundation Target

### [개념]

Design System Foundation의 목표는 Frontend Agent가 실무 화면을 일관되게 생성하고 Review Agent가 품질을 검토할 수 있는 최소 기준을 제공하는 것이다.

---

### [핵심]

Foundation Target:

- Design Principles 정의
- Design Token 기준 정의
- Core Component 기준 정의
- Component Variant 기준 정의
- Component State 기준 정의
- Feedback State Pattern 정의
- Accessibility 기본 기준 정의
- Responsive 기본 기준 정의
- Theme 확장 기준 정의
- Review Checklist 정의
- Retrieval Queries 제공

---

### [실무]

Foundation 단계에서 반드시 필요한 항목:

```text
Token
→ Color / Spacing / Typography / Radius / Shadow / Z-index

Core Component
→ Button / Input / FormField / Card / Modal

Feedback Pattern
→ Loading / Empty / Error / Success

Accessibility
→ Label / Focus / Keyboard / Accessible Name

Responsive
→ Mobile First / Breakpoint / Table / Modal
```

Foundation 단계에서 과도한 항목:

```text
Multi-brand Design System
Design Token Build Pipeline
Enterprise Governance
Advanced Visual Regression Testing
Storybook Addon 심화
Package Publishing
```

---

### [FAQ]

Q. Design System Foundation의 목표는 뭐야?
A. Frontend Agent가 일관된 UI를 생성하고 Review Agent가 검토할 수 있는 최소 기준을 제공하는 것이다.

Q. Foundation 단계에서 꼭 필요한 컴포넌트는?
A. Button, Input, FormField, Card, Modal이 우선이다.

Q. Foundation 단계에서 꼭 필요한 패턴은?
A. Loading, Empty, Error, Success State Pattern이 우선이다.

Q. Foundation 단계에서 심화 운영까지 해야 해?
A. 아니다. Enterprise Governance, Token Pipeline, Package Publishing 같은 심화 운영은 Expert 단계에서 다룬다.

---

# 5. Final Checklist

## 5.1 Part01 Quality Checklist

### [개념]

Part01 Quality Checklist는 Design System Core 문서가 Agent 기준 문서로 사용 가능한지 확인하는 검수 기준이다.

---

### [핵심]

최종 체크 항목:

```md
## Core

- [ ] Design System 정의가 명확한가?
- [ ] 사람 공부용이 아니라 Agent 기준 문서인가?
- [ ] Frontend Agent / Review Agent / PM Agent 역할이 구분되는가?
- [ ] Design Principles가 포함되어 있는가?
- [ ] Scope 포함 / 제외 기준이 명확한가?

## Retrieval

- [ ] 핵심 용어가 반복 검색 가능하게 포함되어 있는가?
- [ ] FAQ가 충분한가?
- [ ] 질문-답변 패턴이 명확한가?
- [ ] Chunk가 독립 검색 가능하게 구성되어 있는가?

## Agent Usage

- [ ] Frontend Agent 생성 Flow가 있는가?
- [ ] Review Agent 검토 Flow가 있는가?
- [ ] PM Agent 완료 판단 Flow가 있는가?
- [ ] Approved / Needs Fix / Blocked 기준이 있는가?

## Design System

- [ ] Token, Component, Pattern, Accessibility, Responsive, Theme 흐름이 연결되는가?
- [ ] Foundation 단계 목표가 명확한가?
- [ ] Expert 단계 제외 범위가 분리되어 있는가?
```

---

### [실무]

Part01은 Design System Foundation 전체의 기준 문서다.

Part02 이후 문서는 Part01 기준을 따른다.

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

---

### [FAQ]

Q. Part01의 역할은 뭐야?
A. Design System Foundation 전체의 목적, 범위, 원칙, Agent 사용 기준을 정의하는 기준 문서다.

Q. Part02 이후 문서는 Part01과 어떻게 연결돼?
A. Part01의 Design Principles와 Agent Usage 기준을 기반으로 token, component, pattern, accessibility 문서가 확장된다.

Q. Part01에서 코드 구현을 자세히 다뤄야 해?
A. 아니다. Part01은 기준과 원칙 중심이고, 구체 구현은 이후 Part에서 다룬다.

Q. Part01 최종 승인 기준은 뭐야?
A. Design System 정의, Scope, Principles, Agent Usage, Maturity, Retrieval Queries가 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Design System이 뭐야?
A. 제품 UI를 일관되게 만들기 위한 디자인 원칙, 토큰, 컴포넌트, 패턴, 문서화, 사용 규칙의 집합이다.

Q. Design System 문서는 사람 공부용이야?
A. 아니다. Frontend Agent / Review Agent / PM Agent가 UI를 생성하고 검토하기 위한 RAG 문서다.

Q. Design System은 컴포넌트 라이브러리와 같아?
A. 아니다. 컴포넌트 라이브러리는 Design System의 일부이고, Design System은 토큰과 사용 규칙까지 포함한다.

Q. Design System의 핵심 목적은 뭐야?
A. UI를 매번 새로 만들지 않고 정해진 규칙과 컴포넌트로 일관성 있게 만드는 것이다.

Q. Design System이 없으면 어떤 문제가 생겨?
A. 버튼, 입력, 카드, 간격, 색상, 상태 표현이 화면마다 달라지고 리뷰 기준이 불명확해진다.

Q. Design Principles는 뭐야?
A. UI를 만들 때 지켜야 하는 상위 원칙이다. 예: Consistency, Clarity, Accessibility, Feedback, Responsiveness.

Q. 예쁜 UI가 가장 중요해?
A. 아니다. 요구사항 충족, 사용성, 접근성, 일관성이 먼저다.

Q. Consistency는 뭐야?
A. 같은 의미의 UI를 같은 방식으로 표현하는 원칙이다.

Q. Clarity는 뭐야?
A. 사용자가 현재 상태와 다음 행동을 명확히 이해할 수 있게 하는 원칙이다.

Q. Accessibility는 뭐야?
A. 키보드, 스크린 리더, 저시력, 색각 다양성 사용자를 고려하는 원칙이다.

Q. Feedback은 뭐야?
A. 사용자 행동 후 loading, success, error, empty 같은 시스템 상태를 알려주는 원칙이다.

Q. Frontend Agent는 Design System을 어떻게 사용해?
A. 기존 token과 component spec을 사용해 임의 스타일 생성을 줄이고 일관된 UI를 생성한다.

Q. Review Agent는 Design System에서 뭘 봐야 해?
A. Token, Component Spec, State, Accessibility, Responsive, Theme, Documentation 기준을 확인해야 한다.

Q. PM Agent는 Design System을 어떻게 사용해?
A. 화면이 요구사항과 일치하는지, 사용자 흐름이 명확한지, 주요 상태 처리가 있는지 판단한다.

Q. Frontend Agent가 임의로 새 버튼 스타일을 만들어도 돼?
A. 기존 variant로 해결할 수 없을 때만 가능하고, 새 variant 추가 이유를 명확히 해야 한다.

Q. raw color를 직접 쓰면 안 돼?
A. 공통 UI와 반복 스타일에서는 semantic token을 사용하는 것이 좋다.

Q. Loading State는 왜 필요해?
A. 사용자가 화면이 멈췄는지 처리 중인지 알 수 있어야 하기 때문이다.

Q. Error State는 왜 필요해?
A. 요청 실패나 처리 오류를 사용자에게 알리고 복구 방법을 안내하기 위해 필요하다.

Q. Empty State는 왜 필요해?
A. 데이터가 없는 상황과 다음 행동을 사용자에게 알려야 하기 때문이다.

Q. Design System Foundation의 목표는 뭐야?
A. Frontend Agent가 일관된 UI를 생성하고 Review Agent가 검토할 수 있는 최소 기준을 제공하는 것이다.

Q. Foundation 단계에서 꼭 필요한 컴포넌트는?
A. Button, Input, FormField, Card, Modal이 우선이다.

Q. Foundation 단계에서 꼭 필요한 패턴은?
A. Loading, Empty, Error, Success State Pattern이 우선이다.

Q. 개인 AI 프로젝트에서는 어느 정도 Design System이 적당해?
A. Basic Token, Core Components, Feedback Pattern 기준까지 있으면 Frontend Agent가 일관된 UI를 만들기 좋다.

Q. Part01의 역할은 뭐야?
A. Design System Foundation 전체의 목적, 범위, 원칙, Agent 사용 기준을 정의하는 기준 문서다.
