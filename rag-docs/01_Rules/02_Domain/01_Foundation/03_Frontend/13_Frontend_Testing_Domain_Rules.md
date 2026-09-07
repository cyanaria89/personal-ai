# Frontend Testing Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Frontend Testing Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Frontend 테스트 전략 기준 제공
- React Component 테스트 기준 제공
- UI 상태 테스트 기준 제공
- Form 테스트 기준 제공
- API 연동 테스트 기준 제공
- Mock / Stub / Spy 사용 기준 제공
- React Testing Library 기준 제공
- Vitest / Jest 기준 제공
- User Event 기반 테스트 기준 제공
- Accessibility 중심 테스트 기준 제공
- Routing 테스트 기준 제공
- Auth / Protected Route 테스트 기준 제공
- Error / Loading / Empty State 테스트 기준 제공
- 유지보수 가능한 테스트 코드 작성 기준 제공

---

### [핵심]

우선순위:

1. Testing Strategy
2. Unit Test
3. Component Test
4. Integration Test
5. E2E Test Basics
6. React Testing Library
7. User Event
8. Query Priority
9. Mocking
10. API Mocking
11. MSW Basics
12. Form Testing
13. Router Testing
14. Auth Testing
15. Loading / Error / Empty Testing
16. Accessibility Testing
17. Test Anti Pattern

---

### [실무]

2026 실무 기준에서 Frontend Testing 문서는 단순 함수 테스트 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 사용자 관점 테스트 작성
- Component 렌더링 테스트 작성
- Button / Form / Modal / List UI 테스트
- Loading / Error / Empty / Success 상태 테스트
- API 응답 Mock 테스트
- Form validation 테스트
- Routing 이동 테스트
- Protected Route 테스트
- Role Based UI 테스트
- TanStack Query 상태 테스트
- 접근성 기반 query 사용
- 테스트 유지보수성 검토
- 불필요한 구현 세부 테스트 방지

---

### [FAQ]

Q. Frontend Testing 문서는 UI Component Pattern과 뭐가 달라?

A.
UI Component Pattern은 Component 설계 기준이고 Frontend Testing은 그 Component가 사용자 관점에서 정상 동작하는지 검증하는 기준이다.

Q. Frontend Testing에서 가장 중요한 기준은 뭐야?

A.
구현 세부사항보다 사용자가 보는 화면, 클릭, 입력, 결과를 기준으로 테스트하는 것이다.

Q. 테스트는 무조건 많이 작성하면 좋아?

A.
아니다. 핵심 사용자 흐름, 오류 가능성이 큰 로직, 반복 회귀가 필요한 부분을 우선 테스트하는 것이 좋다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Testing 문서는 React Frontend 테스트에 필요한 범위를 포함한다.

포함 범위:

- Testing Strategy
- Test Pyramid Basics
- Unit Test
- Component Test
- Integration Test
- E2E Test Basics
- React Testing Library
- Vitest Basics
- Jest Basics
- Testing Environment
- jsdom
- render
- screen
- userEvent
- fireEvent Basics
- Query Priority
- getByRole
- getByLabelText
- getByText
- findBy
- queryBy
- waitFor
- Mock Function
- API Mocking
- MSW Basics
- Axios Mock Basics
- Form Testing
- Validation Testing
- Loading State Testing
- Error State Testing
- Empty State Testing
- Router Testing
- Protected Route Testing
- Auth State Testing
- TanStack Query Testing Basics
- Accessibility Testing Basics
- Snapshot Testing Caution
- Test File Structure
- Test Naming
- Test Troubleshooting

---

### [핵심]

반드시 포함:

- 사용자 관점 테스트 우선
- 구현 세부사항 테스트 지양
- getByRole 우선 사용
- 비동기 UI는 findBy / waitFor 사용
- API 요청은 mock으로 제어
- Form 입력은 userEvent 사용
- Loading / Error / Empty 상태 테스트
- Protected Route와 Auth State 테스트
- 접근성 좋은 Component가 테스트도 쉬움
- Snapshot 남용 금지
- 테스트 이름은 사용자 시나리오 중심
- 테스트가 깨지는 이유가 명확해야 함

---

### [실무]

Frontend Testing은 Component 구현 이후 품질을 검증하는 단계에서 사용한다.

실무 연결:

```text
React Component Design
→ UI Component Pattern
→ Data Fetching
→ Form Handling
→ Error Handling & Loading UX
→ Frontend Testing
→ Frontend Code Review
```

---

### [FAQ]

Q. E2E 테스트도 여기서 다뤄?

A.
기초 개념과 적용 기준은 포함하지만 Playwright / Cypress 심화는 E2E Testing 문서에서 다룬다.

Q. Storybook 테스트도 여기서 다뤄?

A.
기초 언급은 가능하지만 Storybook Interaction Test와 Visual Regression은 별도 문서가 적합하다.

Q. Backend API 실제 서버를 띄워서 테스트해?

A.
Frontend Component 테스트에서는 보통 API를 Mock 처리한다. 실제 통합 검증은 E2E 또는 별도 통합 환경에서 수행한다.

---

## 2.2 Excluded Scope

### [개념]

Frontend Testing 문서에서는 E2E 심화와 고급 테스트 인프라를 제외한다.

제외 범위:

- Playwright 심화
- Cypress 심화
- Visual Regression 심화
- Storybook Interaction Test 심화
- Contract Testing 심화
- Performance Testing 심화
- Load Testing
- Cross Browser Automation 심화
- CI/CD Test Pipeline 심화
- Test Coverage Gate 심화
- Mutation Testing
- Backend Unit Test
- Backend Integration Test
- Mobile Device Farm Testing

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- E2E / CI-CD / Monitoring 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- React Component와 사용자 흐름 테스트 기준에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
Frontend Testing
→ E2E Testing
→ Visual Regression Testing
→ CI/CD Testing Pipeline
→ Frontend Monitoring
```

---

### [FAQ]

Q. Playwright 전체 사용법도 여기서 다뤄?

A.
아니다. 여기서는 E2E 테스트의 위치와 기준만 다루고 Playwright 심화는 별도 문서에서 다룬다.

Q. 테스트 커버리지 목표도 여기서 정해?

A.
기초 기준은 언급할 수 있지만 조직별 coverage gate와 CI 정책은 별도 품질 정책 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Frontend Testing RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 테스트 작성 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 Frontend Testing 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Frontend Testing 문서에는 테스트 흐름과 디버깅을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- 테스트 전략 → [Comparison], [Checklist]
- Component 테스트 → [예제], [Best Practice]
- API Mocking → [Flow], [주의]
- Form 테스트 → [예제]
- 비동기 테스트 → [Troubleshooting]
- Anti Pattern → [주의], [Troubleshooting]

---

### [실무]

예시:

```md
### [Flow]

Render Component
→ Find Element by User-visible Query
→ User Interaction
→ Assert Result
→ Verify UI State
```

---

### [FAQ]

Q. Frontend Testing 문서에 Troubleshooting이 중요한 이유는?

A.
비동기 렌더링, mock 누락, act warning, query 실패, 테스트 환경 차이 같은 문제가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
Unit vs Component vs E2E, getBy vs findBy, fireEvent vs userEvent, mock API vs real API처럼 선택 기준이 필요한 경우에 사용한다.

---

# 4. Testing Strategy Rules

## 4.1 Testing Pyramid Basics

### [개념]

Testing Pyramid는 테스트를 목적과 비용에 따라 나누는 전략이다.

Frontend에서는 Unit Test, Component Test, Integration Test, E2E Test를 적절히 조합한다.

---

### [핵심]

테스트 종류:

| 종류             | 목적                                       | 예                      |
| ---------------- | ------------------------------------------ | ----------------------- |
| Unit Test        | 순수 함수 / 작은 로직 검증                 | 날짜 포맷 함수          |
| Component Test   | Component UI와 상호작용 검증               | SearchForm 입력         |
| Integration Test | 여러 Component / 상태 / API Mock 흐름 검증 | 로그인 후 화면 변경     |
| E2E Test         | 실제 브라우저 사용자 흐름 검증             | 회원가입부터 로그인까지 |

---

### [실무]

권장 기준:

```text
많이 작성 → Unit / Component Test
적당히 작성 → Integration Test
핵심 흐름만 작성 → E2E Test
```

주의:

- 모든 것을 E2E로 검증하지 않음
- 모든 것을 Unit Test로 쪼개지도 않음
- 사용자 핵심 흐름은 Integration / E2E 검토
- 단순 UI 스냅샷보다 실제 상호작용 검증 우선
- 비용 대비 회귀 방지 효과를 고려

---

### [FAQ]

Q. Frontend 테스트는 뭐부터 작성해?

A.
핵심 Component와 사용자 흐름부터 작성하는 것이 좋다. Form, API 상태, 인증 흐름처럼 오류 가능성이 큰 부분이 우선이다.

Q. E2E 테스트만 있으면 충분해?

A.
아니다. E2E는 신뢰도가 높지만 느리고 유지보수 비용이 크므로 Component / Integration Test와 함께 사용하는 것이 좋다.

---

## 4.2 What to Test

### [개념]

What to Test는 어떤 부분을 테스트할지 결정하는 기준이다.

Frontend 테스트는 사용자가 보고 조작하는 결과를 중심으로 작성한다.

---

### [핵심]

우선 테스트 대상:

- 사용자 입력
- 버튼 클릭
- Form submit
- Validation message
- API loading state
- API error state
- Empty state
- Routing result
- Protected route
- Conditional rendering
- Permission UI
- Critical business flow

낮은 우선순위:

- 단순 스타일 class
- 내부 state 이름
- 구현 함수 호출 여부
- 라이브러리 내부 동작
- 변경 가능성이 큰 snapshot

---

### [실무]

테스트 가치 판단:

```text
사용자가 체감하는가?
→ 실패하면 중요한 기능이 깨지는가?
→ 반복 회귀 가능성이 있는가?
→ 수동 확인 비용이 큰가?
→ 테스트 작성 가치 높음
```

예:

```text
검색어 입력 후 검색 결과가 표시되는지 → 테스트 가치 높음
Button className이 정확히 primary인지 → 낮음
```

---

### [FAQ]

Q. 모든 Component를 테스트해야 해?

A.
필수는 아니다. 재사용 빈도가 높거나 사용자 흐름에 중요한 Component를 우선 테스트한다.

Q. CSS class도 테스트해야 해?

A.
대부분 권장하지 않는다. 사용자가 볼 수 있는 텍스트, 역할, 상태, 동작을 테스트하는 것이 좋다.

---

# 5. React Testing Library Rules

## 5.1 Testing Philosophy

### [개념]

React Testing Library는 Component의 구현 세부사항보다 사용자가 실제로 보는 화면과 조작을 기준으로 테스트하는 도구다.

---

### [핵심]

핵심 원칙:

- 사용자 관점 테스트
- DOM 결과 테스트
- 접근성 기반 query 우선
- 구현 세부사항 테스트 지양
- 내부 state 직접 확인 지양
- 실제 사용자 이벤트에 가까운 테스트
- role / label / text 기반 탐색

---

### [실무]

좋은 테스트:

```tsx
render(<LoginForm onLogin={onLogin} />);

await user.type(screen.getByLabelText("이메일"), "test@example.com");
await user.type(screen.getByLabelText("비밀번호"), "password123");
await user.click(screen.getByRole("button", { name: "로그인" }));

expect(onLogin).toHaveBeenCalled();
```

나쁜 테스트:

```tsx
const instance = component.instance();
expect(instance.state.email).toBe("test@example.com");
```

권장:

- 화면에 보이는 요소를 찾음
- 사용자가 하는 행동을 userEvent로 실행
- 결과 UI를 assert
- 내부 state나 private function 검증 지양
- 접근성 좋은 UI일수록 테스트가 쉬움

---

### [FAQ]

Q. React Testing Library는 Enzyme이랑 뭐가 달라?

A.
React Testing Library는 구현 내부보다 사용자가 보는 결과와 상호작용을 중심으로 테스트한다.

Q. 내부 state 값을 직접 확인하면 안 돼?

A.
권장하지 않는다. state가 아니라 사용자가 볼 수 있는 UI 결과를 검증하는 것이 더 유지보수에 좋다.

---

## 5.2 Render and Screen Rules

### [개념]

render는 Component를 테스트 DOM에 렌더링하는 함수이고 screen은 렌더링된 화면에서 요소를 찾는 객체다.

---

### [핵심]

필수 포함:

- render
- screen
- cleanup
- test environment
- jsdom
- custom render
- provider wrapper

---

### [실무]

기본 예:

```tsx
import { render, screen } from "@testing-library/react";

test("제목을 표시한다", () => {
  render(<FestivalCard festival={festival} />);

  expect(
    screen.getByRole("heading", { name: "봄꽃 축제" }),
  ).toBeInTheDocument();
});
```

Provider가 필요한 경우:

```tsx
function renderWithProviders(ui: ReactElement) {
  return render(<BrowserRouter>{ui}</BrowserRouter>);
}
```

권장:

- screen 사용
- 반복 Provider는 custom render로 분리
- 테스트마다 독립적으로 render
- 테스트 간 상태 공유 금지
- cleanup은 테스트 도구가 자동 처리하는 경우가 많음

---

### [FAQ]

Q. screen을 왜 써?

A.
현재 테스트 화면에서 요소를 찾는 방식이 명확하고 React Testing Library 권장 패턴이기 때문이다.

Q. Router나 QueryClient Provider가 필요하면?

A.
custom render 함수를 만들어 테스트마다 반복 설정을 줄이는 것이 좋다.

---

# 6. Query Rules

## 6.1 Query Priority

### [개념]

Query Priority는 테스트에서 요소를 찾을 때 어떤 query를 우선 사용할지 정하는 기준이다.

사용자가 인식할 수 있는 방식에 가까운 query를 우선한다.

---

### [핵심]

우선순위:

1. getByRole
2. getByLabelText
3. getByPlaceholderText
4. getByText
5. getByDisplayValue
6. getByAltText
7. getByTitle
8. getByTestId

---

### [실무]

권장 예:

```tsx
screen.getByRole("button", { name: "검색" });
screen.getByLabelText("이메일");
screen.getByRole("heading", { name: "축제 목록" });
```

최후 수단:

```tsx
screen.getByTestId("festival-card");
```

주의:

- testId 남용 금지
- getByRole을 사용하려면 semantic HTML과 accessible name 필요
- label 없는 input은 테스트도 어려움
- 접근성 개선이 테스트 품질도 높임

---

### [FAQ]

Q. getByRole을 왜 우선 사용해?

A.
사용자가 보조기술로 인식하는 역할과 이름을 기준으로 요소를 찾기 때문에 실제 사용성에 가깝다.

Q. testId는 쓰면 안 돼?

A.
쓰면 안 되는 것은 아니지만 사용자가 인식할 수 없는 구현용 식별자라 최후 수단으로 사용하는 것이 좋다.

---

## 6.2 getBy / findBy / queryBy Rules

### [개념]

getBy, findBy, queryBy는 요소 존재 여부와 비동기 렌더링 여부에 따라 선택하는 query 계열이다.

---

### [핵심]

비교:

| Query   | 사용 상황        | 실패 시          |
| ------- | ---------------- | ---------------- |
| getBy   | 즉시 존재해야 함 | 없으면 throw     |
| findBy  | 비동기로 나타남  | timeout 후 throw |
| queryBy | 없어야 함을 확인 | 없으면 null      |

---

### [실무]

즉시 존재:

```tsx
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

비동기 등장:

```tsx
expect(await screen.findByText("조회 성공")).toBeInTheDocument();
```

존재하지 않음:

```tsx
expect(screen.queryByText("에러")).not.toBeInTheDocument();
```

주의:

- 비동기 API 응답 후 UI는 findBy 사용
- 요소가 없어야 하는 테스트는 queryBy 사용
- getBy로 absence 테스트하면 throw 발생
- findBy는 await 필요

---

### [FAQ]

Q. getBy와 findBy 차이는?

A.
getBy는 즉시 존재하는 요소를 찾고 findBy는 비동기적으로 나중에 나타나는 요소를 기다린다.

Q. 요소가 없어야 하는 테스트는 뭘 써?

A.
queryBy를 사용해 null인지 확인한다.

---

## 6.3 waitFor Rules

### [개념]

waitFor는 특정 assertion이 통과할 때까지 기다리는 비동기 테스트 유틸이다.

상태 변경이 비동기로 발생할 때 사용한다.

---

### [핵심]

사용 상황:

- async state update
- mock API response
- debounce result
- element removed
- callback called later
- mutation success

---

### [실무]

예:

```tsx
await waitFor(() => {
  expect(mockSubmit).toHaveBeenCalledTimes(1);
});
```

권장:

- findBy로 충분하면 findBy 우선
- callback 호출 확인에는 waitFor 사용 가능
- waitFor 안에서 여러 assertion 남발 지양
- timeout이 발생하면 실제 UI 상태를 확인
- 비동기 원인을 명확히 이해하고 사용

---

### [FAQ]

Q. findBy와 waitFor 중 뭐를 써?

A.
화면 요소가 나타나는 것을 기다릴 때는 findBy가 더 간단하고, callback 호출이나 복잡한 조건은 waitFor를 사용할 수 있다.

Q. waitFor를 무조건 쓰면 돼?

A.
아니다. 불필요한 waitFor는 테스트를 느리고 불명확하게 만든다.

---

# 7. User Event Rules

## 7.1 userEvent Rules

### [개념]

userEvent는 사용자의 실제 상호작용에 가깝게 클릭, 입력, 키보드 조작을 시뮬레이션하는 도구다.

---

### [핵심]

사용 대상:

- click
- type
- clear
- selectOptions
- upload
- keyboard
- tab
- hover
- unhover

---

### [실무]

예:

```tsx
const user = userEvent.setup();

await user.type(screen.getByLabelText("검색어"), "축제");
await user.click(screen.getByRole("button", { name: "검색" }));

expect(onSearch).toHaveBeenCalledWith("축제");
```

권장:

- fireEvent보다 userEvent 우선
- userEvent.setup 사용
- user interaction은 await 사용
- 실제 사용자가 하는 흐름대로 작성
- 입력 후 결과 UI 검증

---

### [FAQ]

Q. userEvent와 fireEvent 차이는?

A.
userEvent는 실제 사용자 상호작용에 더 가깝고 fireEvent는 단일 DOM 이벤트를 직접 발생시키는 저수준 도구다.

Q. user.type에 await가 필요한 이유는?

A.
userEvent는 실제 이벤트 흐름을 비동기로 처리할 수 있으므로 await를 사용하는 것이 안전하다.

---

## 7.2 fireEvent Rules

### [개념]

fireEvent는 특정 DOM 이벤트를 직접 발생시키는 저수준 테스트 도구다.

대부분의 사용자 상호작용 테스트에서는 userEvent를 우선한다.

---

### [핵심]

사용 상황:

- low-level event
- custom event
- unsupported userEvent case
- specific DOM event simulation
- legacy test

---

### [실무]

예:

```tsx
fireEvent.change(input, {
  target: { value: "축제" },
});
```

주의:

- 일반 클릭 / 입력은 userEvent 우선
- fireEvent는 실제 사용자 행동과 다를 수 있음
- 이벤트 하나만 발생해 실제 브라우저 흐름을 놓칠 수 있음
- 필요한 경우에만 제한적으로 사용

---

### [FAQ]

Q. fireEvent를 쓰면 안 돼?

A.
쓰면 안 되는 것은 아니지만 일반 사용자 행동 테스트에는 userEvent가 더 적합하다.

Q. fireEvent는 언제 써?

A.
userEvent로 표현하기 어려운 저수준 이벤트나 커스텀 이벤트를 테스트할 때 사용한다.

---

# 8. Unit Test Rules

## 8.1 Pure Function Test

### [개념]

Pure Function Test는 입력이 같으면 항상 같은 결과를 반환하는 순수 함수를 검증하는 테스트다.

포맷팅, validation, mapping 함수에 적합하다.

---

### [핵심]

테스트 대상:

- validation function
- formatter
- mapper
- filter function
- sorting function
- date utility
- error message mapper
- request dto mapper

---

### [실무]

예:

```typescript
function toCreateReviewRequest(festivalId: number, values: ReviewFormValues) {
  return {
    festivalId,
    rating: Number(values.rating),
    content: values.content.trim(),
  };
}

test("리뷰 form 값을 create review request로 변환한다", () => {
  const result = toCreateReviewRequest(1, {
    rating: "5",
    content: " 좋았어요 ",
  });

  expect(result).toEqual({
    festivalId: 1,
    rating: 5,
    content: "좋았어요",
  });
});
```

권장:

- 입출력이 명확한 함수 테스트
- edge case 포함
- UI 렌더링 없이 빠르게 테스트
- 복잡한 Component 내부 로직은 함수로 분리 후 테스트 가능
- 날짜 / timezone / locale 주의

---

### [FAQ]

Q. 어떤 함수는 Unit Test가 좋아?

A.
validation, mapper, formatter처럼 입력과 출력이 명확한 순수 함수가 Unit Test에 적합하다.

Q. Component 내부 함수를 직접 테스트해야 해?

A.
보통은 사용자 결과를 통해 테스트한다. 복잡한 로직은 별도 순수 함수로 분리해 테스트할 수 있다.

---

## 8.2 Validation Function Test

### [개념]

Validation Function Test는 Form 입력값 검증 로직을 독립적으로 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- required
- email format
- password confirm
- length validation
- number range
- date range
- file size
- file type

---

### [실무]

예:

```typescript
test("리뷰 내용이 비어 있으면 content error를 반환한다", () => {
  const errors = validateReview({
    rating: 5,
    content: "   ",
  });

  expect(errors.content).toBe("리뷰 내용을 입력해 주세요.");
});
```

권장:

- 정상 케이스와 실패 케이스 모두 테스트
- 공백 입력 테스트
- boundary value 테스트
- Backend validation 기준과 맞는지 확인
- 메시지 문자열이 자주 바뀌면 에러 코드 기반 테스트 고려

---

### [FAQ]

Q. Validation은 Component 테스트만 하면 안 돼?

A.
간단하면 가능하지만 검증 로직이 복잡하면 함수 단위 테스트가 더 빠르고 명확하다.

Q. 에러 메시지 문자열까지 테스트해야 해?

A.
사용자에게 중요한 메시지라면 가능하다. 다만 문구 변경이 잦으면 에러 코드나 key 중심 테스트를 고려한다.

---

# 9. Component Test Rules

## 9.1 Presentational Component Test

### [개념]

Presentational Component Test는 props를 받아 화면을 올바르게 렌더링하는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- text rendering
- image alt
- button state
- badge text
- empty state
- conditional rendering
- accessibility role
- event callback

---

### [실무]

예:

```tsx
test("축제 카드에 축제 제목과 지역명을 표시한다", () => {
  render(
    <FestivalCard
      festival={{
        festivalId: 1,
        title: "봄꽃 축제",
        regionName: "서울",
        imageUrl: "/festival.jpg",
      }}
    />,
  );

  expect(
    screen.getByRole("heading", { name: "봄꽃 축제" }),
  ).toBeInTheDocument();
  expect(screen.getByText("서울")).toBeInTheDocument();
});
```

권장:

- props에 따른 화면 결과 검증
- 사용자가 볼 수 있는 텍스트 검증
- callback은 사용자 이벤트로 호출 확인
- className 중심 테스트 지양
- snapshot만으로 대체하지 않음

---

### [FAQ]

Q. Presentational Component는 뭘 테스트해?

A.
props에 따라 사용자가 보는 텍스트, 버튼 상태, 이미지, 조건부 UI가 올바른지 테스트한다.

Q. className이 맞는지 테스트해야 해?

A.
대부분 지양한다. 스타일 자체보다 사용자에게 보이는 상태와 의미를 테스트하는 것이 좋다.

---

## 9.2 Interactive Component Test

### [개념]

Interactive Component Test는 사용자가 클릭, 입력, 선택 같은 행동을 했을 때 UI와 callback이 올바르게 동작하는지 검증한다.

---

### [핵심]

테스트 대상:

- button click
- input change
- checkbox toggle
- radio select
- select option
- modal open / close
- tab change
- dropdown select
- form submit

---

### [실무]

예:

```tsx
test("검색어 입력 후 검색 버튼을 누르면 onSearch가 호출된다", async () => {
  const user = userEvent.setup();
  const onSearch = vi.fn();

  render(<SearchBox value="" onChange={() => {}} onSearch={onSearch} />);

  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(onSearch).toHaveBeenCalledTimes(1);
});
```

Controlled Component 예:

```tsx
function SearchBoxWrapper() {
  const [value, setValue] = useState("");

  return <SearchBox value={value} onChange={setValue} onSearch={() => {}} />;
}
```

권장:

- 실제 사용자 행동 순서로 테스트
- userEvent 사용
- callback 호출과 UI 변화 확인
- Controlled Component는 wrapper 필요 가능
- disabled / loading 상태도 테스트

---

### [FAQ]

Q. Controlled Component는 테스트가 왜 어려워?

A.
value가 부모 state에서 내려오므로 테스트에서도 상태를 업데이트하는 wrapper가 필요할 수 있다.

Q. 버튼 클릭 테스트는 어떻게 해?

A.
userEvent로 버튼을 클릭하고 callback 호출 또는 화면 변화를 확인한다.

---

# 10. Form Testing Rules

## 10.1 Form Input Test

### [개념]

Form Input Test는 사용자가 input에 값을 입력했을 때 화면과 제출 값이 올바르게 반영되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- text input
- password input
- textarea
- select
- checkbox
- radio
- file input
- submit button
- validation message

---

### [실무]

예:

```tsx
test("이메일과 비밀번호를 입력하고 로그인한다", async () => {
  const user = userEvent.setup();
  const onLogin = vi.fn();

  render(<LoginForm onLogin={onLogin} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(onLogin).toHaveBeenCalledWith({
    email: "test@example.com",
    password: "password123",
  });
});
```

권장:

- label 기반 query 사용
- user.type 사용
- submit은 button click 또는 Enter key로 테스트
- password 값 로그 출력 금지
- 실제 Form submit 결과 검증

---

### [FAQ]

Q. Form input 테스트는 어떻게 해?

A.
userEvent로 값을 입력하고 submit 후 callback 호출 값이나 화면 결과를 검증한다.

Q. input은 getByLabelText로 찾는 게 좋아?

A.
좋다. label 연결이 잘 되어 있는지 함께 검증할 수 있다.

---

## 10.2 Validation Test

### [개념]

Validation Test는 잘못된 입력값을 제출했을 때 적절한 오류 메시지가 표시되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- required error
- format error
- length error
- password mismatch
- number range error
- server field error
- global form error

---

### [실무]

예:

```tsx
test("이메일을 입력하지 않으면 이메일 오류를 표시한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={vi.fn()} />);

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByText("이메일을 입력해 주세요.")).toBeInTheDocument();
});
```

권장:

- 사용자 행동으로 validation 발생
- 오류 메시지가 화면에 표시되는지 확인
- invalid submit 시 API 호출이 안 되는지 확인
- Field Error와 Global Error 구분
- 서버 validation error는 API mock으로 테스트

---

### [FAQ]

Q. Validation 테스트에서 뭘 확인해?

A.
오류 메시지가 표시되는지, 잘못된 입력으로 submit이 중단되는지, 필요하면 API 호출이 발생하지 않는지 확인한다.

Q. 서버 validation error도 테스트해?

A.
중요한 Form이라면 API mock을 통해 서버 field error가 화면에 표시되는지 테스트하는 것이 좋다.

---

## 10.3 Submit Loading Test

### [개념]

Submit Loading Test는 Form 제출 중 버튼이 disabled되고 처리 중 문구가 표시되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- submitting state
- button disabled
- loading text
- duplicate submit prevention
- success state
- error state

---

### [실무]

예:

```tsx
test("로그인 요청 중 버튼을 비활성화한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm onLogin={() => new Promise(() => {})} />);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByRole("button", { name: "처리 중..." })).toBeDisabled();
});
```

권장:

- 요청 중 UI 상태 확인
- 중복 클릭 방지 확인
- 성공 / 실패 후 상태 복구 확인
- promise 제어 방식 사용 가능
- 무한 pending promise 사용 시 테스트 정리 주의

---

### [FAQ]

Q. 제출 중 버튼 disabled도 테스트해야 해?

A.
중복 제출이 중요한 Form이라면 테스트하는 것이 좋다.

Q. pending promise 테스트는 위험해?

A.
잘못 관리하면 테스트가 끝나지 않을 수 있다. 필요한 범위에서만 사용하고 상태 확인 후 테스트가 종료되도록 구성한다.

---

# 11. API Mocking Rules

## 11.1 API Mocking Basics

### [개념]

API Mocking은 실제 서버를 호출하지 않고 테스트에서 원하는 응답을 제어하는 방식이다.

Frontend 테스트에서는 성공, 실패, 로딩, 빈 데이터 상태를 안정적으로 검증하기 위해 사용한다.

---

### [핵심]

Mock 대상:

- API function
- fetch
- axios
- server response
- error response
- delay
- empty response
- auth response

---

### [실무]

API 함수 mock 예:

```tsx
vi.mock("../api/festivalApi", () => ({
  getFestivals: vi.fn(),
}));
```

테스트 예:

```tsx
test("축제 목록을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

권장:

- 테스트마다 mock 초기화
- 성공 / 실패 / 빈 응답 모두 테스트 가능
- 실제 API 서버 의존 금지
- response shape를 실제 Backend와 맞춤
- mock이 실제와 달라지지 않도록 관리

---

### [FAQ]

Q. Frontend 테스트에서 실제 API를 호출해도 돼?

A.
일반 Component 테스트에서는 권장하지 않는다. API 응답은 mock으로 제어하는 것이 안정적이다.

Q. API mock은 왜 필요해?

A.
테스트가 서버 상태, 네트워크, DB에 의존하지 않고 원하는 상황을 재현할 수 있게 하기 위해 필요하다.

---

## 11.2 MSW Basics

### [개념]

MSW는 Mock Service Worker 기반 API mocking 도구다.

Frontend 테스트에서 실제 네트워크 요청에 가까운 방식으로 API 응답을 mock할 수 있다.

---

### [핵심]

사용 상황:

- integration style test
- REST API mock
- GraphQL mock basics
- success response
- error response
- delay response
- shared mock handler
- browser mock
- test mock server

---

### [실무]

개념 Flow:

```text
Component
→ API Request
→ MSW Handler Intercept
→ Mock Response
→ Component UI Update
```

Handler 예:

```typescript
import { http, HttpResponse } from "msw";

export const handlers = [
  http.get("/api/festivals", () => {
    return HttpResponse.json([{ festivalId: 1, title: "봄꽃 축제" }]);
  }),
];
```

권장:

- API 함수 mock보다 실제 요청 흐름에 가까움
- 여러 Component가 API를 공유할 때 유용
- 성공 / 실패 / 지연 응답 handler 작성
- 테스트 환경 setup 필요
- Backend response shape와 일치시키기

---

### [FAQ]

Q. MSW는 언제 써?

A.
Component가 실제 API 요청을 보내는 흐름에 가깝게 테스트하고 싶을 때 유용하다.

Q. API 함수 mock과 MSW 중 뭐가 좋아?

A.
작은 단위는 API 함수 mock이 간단하고, 여러 Component와 실제 요청 흐름을 검증하려면 MSW가 더 적합할 수 있다.

---

## 11.3 Error Response Mocking

### [개념]

Error Response Mocking은 API 실패 상황을 테스트에서 재현하는 방식이다.

Error State, Toast, Form Error, Redirect를 검증할 때 필요하다.

---

### [핵심]

Mock 대상:

- 400 validation error
- 401 unauthorized
- 403 forbidden
- 404 not found
- 409 conflict
- 500 server error
- network error
- timeout basics

---

### [실무]

예:

```tsx
test("서버 오류가 발생하면 ErrorState를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  render(<FestivalListPage />);

  expect(
    await screen.findByText(
      "서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
    ),
  ).toBeInTheDocument();
});
```

권장:

- 상태 코드별 중요한 UX 테스트
- 401 / 403 구분 테스트
- validation error는 field error 표시 확인
- error object shape를 실제 axios error와 맞춤
- Retry 버튼 동작 테스트 가능

---

### [FAQ]

Q. 에러 응답도 테스트해야 해?

A.
중요한 화면이라면 해야 한다. 실제 서비스에서는 성공보다 실패 상황 UX가 사용자 경험에 큰 영향을 준다.

Q. mockRejectedValue 구조는 실제 AxiosError와 같아야 해?

A.
가능하면 실제 코드가 참조하는 error.response.status, error.response.data 구조와 맞춰야 한다.

---

# 12. Loading / Error / Empty Test Rules

## 12.1 Loading State Test

### [개념]

Loading State Test는 API 요청 중 사용자에게 Loading UI가 표시되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- initial loading
- refetch loading
- submit loading
- skeleton
- spinner
- aria status
- disabled state

---

### [실무]

예:

```tsx
test("축제 목록을 불러오는 동안 loading 메시지를 표시한다", () => {
  vi.mocked(getFestivals).mockReturnValue(new Promise(() => {}));

  render(<FestivalListPage />);

  expect(screen.getByRole("status")).toHaveTextContent("불러오는 중입니다.");
});
```

주의:

- pending promise 사용 시 테스트가 hang되지 않게 구성
- loading 이후 success / error도 별도 테스트
- 너무 짧은 loading은 테스트가 불안정할 수 있음
- accessible loading label 사용

---

### [FAQ]

Q. Loading 상태도 테스트해야 해?

A.
사용자 경험에 중요한 화면이라면 테스트하는 것이 좋다. 특히 빈 화면 방지를 확인할 수 있다.

Q. Skeleton은 어떻게 테스트해?

A.
사용자가 인식할 수 있는 role, label, loading message 또는 testId를 기준으로 확인할 수 있다.

---

## 12.2 Error State Test

### [개념]

Error State Test는 API 실패나 렌더링 실패 상황에서 적절한 오류 UI가 표시되는지 검증한다.

---

### [핵심]

테스트 대상:

- error message
- retry button
- forbidden page
- not found page
- form global error
- toast basics
- ErrorState component

---

### [실무]

예:

```tsx
test("조회 실패 시 다시 시도 버튼을 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: { status: 500 },
  });

  render(<FestivalListPage />);

  expect(
    await screen.findByRole("button", { name: "다시 시도" }),
  ).toBeInTheDocument();
});
```

권장:

- 사용자 메시지 확인
- retry action 확인
- status code별 주요 분기 테스트
- 서버 내부 에러 노출 여부 확인 가능
- Error Boundary 테스트와 API Error 테스트 구분

---

### [FAQ]

Q. ErrorState 테스트에서 뭘 봐야 해?

A.
사용자 메시지, 재시도 버튼, 권한 안내, Not Found 안내처럼 사용자가 볼 수 있는 결과를 확인한다.

Q. Error Boundary 테스트와 API Error 테스트는 달라?

A.
다르다. API Error는 요청 실패 상태이고 Error Boundary는 렌더링 중 예외 처리다.

---

## 12.3 Empty State Test

### [개념]

Empty State Test는 API 요청이 성공했지만 데이터가 없을 때 Empty UI가 표시되는지 검증한다.

---

### [핵심]

테스트 대상:

- empty list
- search no result
- no review
- no notification
- no favorite
- reset filter action
- first use empty state

---

### [실무]

예:

```tsx
test("검색 결과가 없으면 EmptyState를 표시한다", async () => {
  vi.mocked(searchFestivals).mockResolvedValue([]);

  render(<FestivalSearchPage />);

  expect(await screen.findByText("검색 결과가 없습니다.")).toBeInTheDocument();
});
```

권장:

- 성공 응답과 error 응답 구분
- empty message 확인
- action 버튼이 있으면 동작 확인
- 초기 loading 전 empty 표시 문제 방지
- 첫 사용 empty와 검색 결과 없음 구분 가능

---

### [FAQ]

Q. Empty State 테스트는 왜 필요해?

A.
데이터가 없을 때 빈 화면이 아니라 적절한 안내가 나오는지 확인하기 위해 필요하다.

Q. Empty State와 Error State 테스트는 어떻게 달라?

A.
Empty State는 성공 응답의 빈 데이터이고 Error State는 요청 실패다.

---

# 13. Router Testing Rules

## 13.1 React Router Test

### [개념]

React Router Test는 Route 이동, Link 클릭, path parameter, query string에 따른 화면 변화를 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Link navigation
- useNavigate result
- route param
- search params
- not found route
- layout route
- nested route
- protected route

---

### [실무]

Router Provider 예:

```tsx
function renderWithRouter(ui: ReactElement, initialEntries = ["/"]) {
  return render(
    <MemoryRouter initialEntries={initialEntries}>{ui}</MemoryRouter>,
  );
}
```

테스트 예:

```tsx
test("축제 상세 경로에서 상세 페이지를 표시한다", () => {
  renderWithRouter(<AppRoutes />, ["/festivals/1"]);

  expect(
    screen.getByRole("heading", { name: "축제 상세" }),
  ).toBeInTheDocument();
});
```

권장:

- MemoryRouter 사용
- initialEntries로 시작 경로 설정
- Route param 기반 UI 검증
- Query String 기반 검색 상태 검증
- 실제 browser history 의존 지양

---

### [FAQ]

Q. React Router 테스트에는 BrowserRouter를 써?

A.
테스트에서는 MemoryRouter를 많이 사용한다. 초기 경로를 쉽게 제어할 수 있기 때문이다.

Q. Route Param 테스트는 어떻게 해?

A.
initialEntries에 `/festivals/1` 같은 경로를 넣고 화면 결과를 검증한다.

---

## 13.2 Protected Route Test

### [개념]

Protected Route Test는 로그인 여부에 따라 보호 페이지 접근이 허용되거나 로그인 페이지로 이동하는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- authenticated user access
- unauthenticated redirect
- auth loading state
- role based route
- forbidden route
- previous location state

---

### [실무]

테스트 기준:

```text
비로그인 사용자
→ /mypage 접근
→ login page 표시

로그인 사용자
→ /mypage 접근
→ mypage 표시

권한 없는 사용자
→ /admin 접근
→ forbidden page 표시
```

예:

```tsx
test("비로그인 사용자가 마이페이지에 접근하면 로그인 페이지를 표시한다", () => {
  renderWithAuthRouter(<AppRoutes />, {
    authenticated: false,
    initialEntries: ["/mypage"],
  });

  expect(screen.getByRole("heading", { name: "로그인" })).toBeInTheDocument();
});
```

권장:

- auth state mock 필요
- initialized loading 상태 테스트
- 401 API Error와 Route Guard 테스트 구분
- role based route는 ROLE 값 기준 테스트
- redirect loop 방지 테스트 가능

---

### [FAQ]

Q. Protected Route는 어떻게 테스트해?

A.
인증 상태를 mock으로 주입하고 보호 경로 접근 시 로그인 페이지 또는 실제 페이지가 표시되는지 검증한다.

Q. auth loading도 테스트해야 해?

A.
중요하다. 인증 초기화 중 잘못 redirect되는 문제를 방지할 수 있다.

---

# 14. Auth Testing Rules

## 14.1 Login Flow Test

### [개념]

Login Flow Test는 사용자가 로그인 Form을 제출했을 때 로그인 API 호출, Auth State 업데이트, redirect가 올바르게 동작하는지 검증한다.

---

### [핵심]

테스트 대상:

- input email
- input password
- login submit
- validation error
- login API success
- login API failure
- global error
- auth state update
- redirect after login

---

### [실무]

Flow:

```text
Render Login Page
→ Type Email / Password
→ Click Login
→ Mock Login Success
→ Assert Redirect or Auth UI
```

예:

```tsx
test("로그인 성공 후 메인 페이지로 이동한다", async () => {
  const user = userEvent.setup();

  mockLoginSuccess();

  renderWithRouter(<AppRoutes />, ["/login"]);

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    await screen.findByRole("heading", { name: "메인" }),
  ).toBeInTheDocument();
});
```

권장:

- password 로그 출력 금지
- 실패 케이스도 테스트
- global error 표시 확인
- redirect target 확인
- login API response shape mock 정확히 맞춤

---

### [FAQ]

Q. 로그인 테스트에서 뭘 확인해?

A.
입력, 제출, 성공 처리, 실패 메시지, 인증 상태 변경, redirect 결과를 확인한다.

Q. 로그인 실패도 테스트해야 해?

A.
중요하다. 인증 실패 UX는 사용자가 자주 마주칠 수 있는 흐름이다.

---

## 14.2 Logout Flow Test

### [개념]

Logout Flow Test는 로그아웃 시 token, user state, cache가 정리되고 적절한 화면으로 이동하는지 검증한다.

---

### [핵심]

테스트 대상:

- logout button click
- logout API optional
- token clear
- user state clear
- cache clear
- redirect
- protected route access after logout

---

### [실무]

테스트 기준:

```text
로그인 상태
→ 로그아웃 클릭
→ 사용자 메뉴 사라짐
→ login 또는 main으로 이동
→ 보호 페이지 접근 불가
```

권장:

- Auth Store 초기 상태 설정
- logout 후 authenticated false 확인은 UI 결과로 검증
- 사용자 전용 데이터가 남지 않는지 확인 가능
- Query Cache clear가 중요하면 별도 테스트
- logout API 실패 시 local cleanup 정책 테스트

---

### [FAQ]

Q. 로그아웃 테스트는 뭘 봐야 해?

A.
로그아웃 후 인증 UI가 사라지고 보호 페이지에 접근할 수 없으며 사용자 상태가 정리되는지 확인한다.

Q. token 삭제 자체를 직접 테스트해야 해?

A.
가능하지만 보통은 사용자 UI와 보호 route 결과로 검증하는 것이 더 유지보수에 좋다.

---

# 15. TanStack Query Testing Rules

## 15.1 QueryClient Test Setup

### [개념]

TanStack Query를 사용하는 Component는 테스트에서 QueryClientProvider가 필요하다.

각 테스트는 독립적인 QueryClient를 사용하는 것이 좋다.

---

### [핵심]

필수 포함:

- QueryClient
- QueryClientProvider
- retry false
- cache isolation
- test wrapper
- cleanup
- staleTime basics

---

### [실무]

예:

```tsx
function createTestQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        retry: false,
      },
    },
  });
}

function renderWithQueryClient(ui: ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <QueryClientProvider client={queryClient}>{ui}</QueryClientProvider>,
  );
}
```

권장:

- 테스트마다 새 QueryClient 생성
- retry false로 테스트 지연 방지
- Query Cache가 테스트 간 공유되지 않게 함
- Router / Auth Provider와 함께 custom render 구성 가능
- mutation test도 QueryClient 필요

---

### [FAQ]

Q. TanStack Query Component 테스트에서 Provider 오류가 나?

A.
QueryClientProvider로 감싸야 한다.

Q. 테스트에서 retry를 false로 하는 이유는?

A.
실패 테스트가 재시도 때문에 느려지거나 예측하기 어려워지는 것을 방지하기 위해서다.

---

## 15.2 Query State Test

### [개념]

Query State Test는 useQuery 기반 화면의 loading, success, error, empty 상태를 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- isLoading
- isFetching
- isError
- data
- refetch
- empty response
- retry button
- invalidation result basics

---

### [실무]

기준:

```text
mock success response
→ content rendered

mock empty response
→ EmptyState rendered

mock error response
→ ErrorState rendered

pending response
→ LoadingState rendered
```

권장:

- API mock 또는 MSW 사용
- queryKey에 params 반영되는지 간접 검증 가능
- UI 상태 중심으로 테스트
- Query 내부 상태 직접 테스트 지양
- retry button은 refetch 결과로 테스트 가능

---

### [FAQ]

Q. useQuery 내부 상태를 직접 테스트해야 해?

A.
보통은 아니다. loading, error, data UI 결과를 테스트하는 것이 좋다.

Q. queryKey를 테스트해야 해?

A.
직접 queryKey 문자열을 테스트하기보다 검색 조건 변경 후 올바른 데이터가 표시되는지 검증하는 것이 좋다.

---

## 15.3 Mutation Test

### [개념]

Mutation Test는 useMutation 기반 생성, 수정, 삭제 요청이 사용자 액션 후 올바른 UI 결과를 만드는지 검증한다.

---

### [핵심]

테스트 대상:

- mutate call
- pending state
- success message
- error message
- invalidate query effect
- form reset
- redirect
- button disabled

---

### [실무]

예:

```tsx
test("리뷰 등록 성공 후 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  mockCreateReviewSuccess();

  renderWithQueryClient(<ReviewForm />);

  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

권장:

- 사용자 액션으로 mutation 실행
- pending 상태 확인
- 성공 후 invalidate 결과나 refetch 결과 확인
- 실패 시 error message 확인
- mutation 함수 호출만 확인하고 끝내지 않음

---

### [FAQ]

Q. mutation 테스트에서 함수 호출만 확인하면 돼?

A.
부족할 수 있다. 사용자가 보는 성공 메시지, 목록 갱신, form reset 같은 결과를 함께 확인하는 것이 좋다.

Q. invalidateQueries를 직접 테스트해야 해?

A.
직접 호출 여부보다 mutation 후 화면 데이터가 갱신되는지 확인하는 것이 더 사용자 관점에 가깝다.

---

# 16. Accessibility Testing Rules

## 16.1 Accessibility Query Test

### [개념]

Accessibility Query Test는 role, label, name 기반 query를 사용해 UI 접근성을 간접적으로 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- button accessible name
- input label
- heading structure
- image alt
- dialog role
- alert role
- tab role
- aria-invalid
- aria-describedby

---

### [실무]

예:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
expect(screen.getByLabelText("이메일")).toBeInTheDocument();
expect(screen.getByRole("alert")).toHaveTextContent("이메일을 입력해 주세요.");
```

권장:

- getByRole 우선
- label 없는 input 발견 시 Component 개선
- icon button에는 aria-label 필요
- error message는 role alert 또는 연결 확인
- Modal / Tab / Dropdown은 접근성 테스트 강화

---

### [FAQ]

Q. getByRole 테스트가 실패하면 접근성 문제야?

A.
항상은 아니지만 role이나 accessible name이 부족할 가능성이 있다. HTML 구조와 aria 속성을 확인해야 한다.

Q. 접근성 테스트를 따로 해야 해?

A.
기본 query를 접근성 중심으로 작성하면 많은 접근성 문제를 초기에 발견할 수 있다.

---

## 16.2 a11y Automated Test Basics

### [개념]

a11y 자동화 테스트는 axe 같은 도구를 사용해 기본 접근성 위반을 검사하는 테스트다.

---

### [핵심]

검사 대상:

- missing label
- color contrast basics
- aria invalid usage
- role mismatch
- heading order basics
- form accessibility
- dialog accessibility basics

---

### [실무]

기준:

```text
Component Render
→ Run Accessibility Check
→ Assert No Major Violations
```

주의:

- 자동화 테스트가 모든 접근성 문제를 잡지는 못함
- 키보드 사용성은 수동 또는 별도 테스트 필요
- 색상 대비와 focus 이동은 추가 검토 필요
- 접근성 테스트는 UI Component와 Form에 특히 유용

---

### [FAQ]

Q. axe 테스트만 통과하면 접근성은 끝이야?

A.
아니다. 자동화 도구는 일부 문제만 잡을 수 있다. 키보드 조작, 스크린 리더 흐름, focus 관리도 확인해야 한다.

Q. 접근성 테스트는 어떤 Component에 우선 적용해?

A.
Form, Modal, Dropdown, Tab, Button, Navigation처럼 사용자 상호작용이 많은 Component에 우선 적용한다.

---

# 17. Snapshot Testing Rules

## 17.1 Snapshot Testing Caution

### [개념]

Snapshot Testing은 렌더링 결과 구조를 저장해 이후 변경 여부를 비교하는 테스트다.

하지만 의미 없는 변경에도 쉽게 깨질 수 있어 남용을 주의한다.

---

### [핵심]

주의 대상:

- large snapshot
- entire page snapshot
- style class snapshot
- unstable markup
- low signal test
- update snapshot habit

---

### [실무]

권장하지 않는 방식:

```text
전체 페이지 snapshot 하나로 UI 검증
→ 변경 이유 파악 어려움
→ 무의미한 snapshot update 반복
```

사용 가능 상황:

- 작은 순수 UI 출력
- stable markup
- 의도적 구조 검증
- serialization utility

대체 권장:

```text
텍스트 / role / interaction / state result 검증
```

---

### [FAQ]

Q. Snapshot 테스트는 쓰면 안 돼?

A.
쓰면 안 되는 것은 아니지만 전체 UI를 snapshot으로만 검증하는 것은 유지보수성이 낮다.

Q. Snapshot이 자주 깨지면 어떻게 해?

A.
테스트 의도가 약한 snapshot일 가능성이 있다. 사용자 관점 assertion으로 바꾸는 것이 좋다.

---

# 18. Test File Structure Rules

## 18.1 Test File Location

### [개념]

Test File Location은 테스트 파일을 Component 옆에 둘지 별도 테스트 폴더에 둘지 정하는 기준이다.

---

### [핵심]

배치 방식:

- colocated test
- `__tests__` folder
- feature test folder
- test utils
- mocks folder
- setup file

---

### [실무]

예:

```text
src
├ components
│  └ ui
│     ├ Button.tsx
│     └ Button.test.tsx
├ features
│  └ festival
│     ├ components
│     │  ├ FestivalCard.tsx
│     │  └ FestivalCard.test.tsx
│     └ api
├ test
│  ├ setup.ts
│  ├ renderWithProviders.tsx
│  └ server.ts
└ mocks
   └ handlers.ts
```

권장:

- Component 가까이에 test 배치 가능
- 공통 setup은 test 폴더로 분리
- renderWithProviders 재사용
- mock handlers 관리
- Feature 단위 테스트 구조 통일

---

### [FAQ]

Q. 테스트 파일은 Component 옆에 두는 게 좋아?

A.
많이 사용되는 방식이다. 관련 파일이 가까워 유지보수하기 쉽다. 팀 컨벤션에 맞추면 된다.

Q. test utils는 어디에 둬?

A.
공통 renderWithProviders, mock server setup, test data factory는 test 폴더에 둘 수 있다.

---

## 18.2 Test Naming Rules

### [개념]

Test Naming은 테스트가 어떤 사용자 시나리오를 검증하는지 명확히 드러나도록 이름을 작성하는 기준이다.

---

### [핵심]

좋은 이름:

- 사용자 행동 포함
- 기대 결과 포함
- 도메인 상황 포함
- 실패 시 원인 파악 가능
- 구현 세부사항보다 결과 중심

---

### [실무]

좋은 예:

```typescript
test("검색어를 입력하고 검색하면 검색 결과를 표시한다", async () => {});
test("비로그인 사용자가 마이페이지에 접근하면 로그인 페이지를 표시한다", () => {});
test("리뷰 내용이 비어 있으면 오류 메시지를 표시한다", async () => {});
```

나쁜 예:

```typescript
test("handleClick works", () => {});
test("state changes", () => {});
test("component renders", () => {});
```

권장:

- 한국어 프로젝트면 테스트명도 한국어 가능
- given / when / then 흐름 반영 가능
- 너무 긴 경우 describe로 문맥 분리
- 실패했을 때 무엇이 깨졌는지 알 수 있게 작성

---

### [FAQ]

Q. 테스트 이름은 한글로 써도 돼?

A.
가능하다. 팀 컨벤션에 맞추면 되며 사용자 시나리오를 명확히 표현하는 것이 중요하다.

Q. component renders 같은 이름은 왜 별로야?

A.
무엇을 렌더링해야 하는지, 어떤 결과를 기대하는지 알기 어렵기 때문이다.

---

# 19. Troubleshooting Rules

## 19.1 Query Failed Troubleshooting

### [개념]

Query Failed 문제는 테스트에서 screen.getByRole, getByText 같은 query가 요소를 찾지 못하는 상황이다.

---

### [핵심]

원인:

- 실제 텍스트 불일치
- 비동기 렌더링인데 getBy 사용
- label 연결 누락
- accessible name 없음
- role 잘못 이해
- 조건부 렌더링 미충족
- Provider 누락
- mock data 누락

---

### [실무]

Debug Flow:

```text
Query 실패
→ screen.debug 확인
→ 비동기 여부 확인
→ getBy / findBy 선택 확인
→ role / name 확인
→ Provider 확인
→ mock 응답 확인
→ 조건부 렌더링 조건 확인
```

권장:

- screen.debug로 현재 DOM 확인
- Testing Playground 활용 가능
- getByRole 실패 시 accessible name 확인
- 비동기 응답이면 findBy 사용
- text가 여러 조각으로 나뉘는지 확인

---

### [FAQ]

Q. getByText가 못 찾는데 화면에는 보이는 것 같아?

A.
텍스트가 여러 요소로 나뉘었거나 비동기 렌더링 전일 수 있다. screen.debug와 findBy를 확인한다.

Q. getByRole이 실패하면?

A.
해당 요소의 semantic role과 accessible name이 제대로 있는지 확인해야 한다.

---

## 19.2 Async Test Troubleshooting

### [개념]

Async Test 문제는 비동기 상태 업데이트, API mock, timer, promise 처리 때문에 테스트가 실패하거나 불안정해지는 상황이다.

---

### [핵심]

원인:

- await 누락
- findBy 대신 getBy 사용
- waitFor 잘못 사용
- promise unresolved
- mockResolvedValue 누락
- timer 처리 누락
- query retry로 지연
- act warning

---

### [실무]

Debug Flow:

```text
비동기 테스트 실패
→ userEvent await 확인
→ findBy 사용 여부 확인
→ mock promise 확인
→ waitFor 조건 확인
→ Query retry false 확인
→ act warning 메시지 확인
```

권장:

- userEvent는 await
- 비동기 UI는 findBy
- mockResolvedValue / mockRejectedValue 명확히 설정
- TanStack Query retry false
- waitFor 남용 금지
- 테스트가 끝나기 전에 상태 업데이트가 남지 않게 처리

---

### [FAQ]

Q. act warning은 왜 나?

A.
테스트가 상태 업데이트가 끝나기 전에 assertion을 하거나 비동기 처리를 기다리지 않았을 가능성이 있다.

Q. 비동기 테스트가 가끔 실패해?

A.
await 누락, 불안정한 timer, 실제 시간 의존, query retry, mock 초기화 누락을 확인해야 한다.

---

## 19.3 Mock Not Working Troubleshooting

### [개념]

Mock Not Working은 테스트에서 설정한 mock이 실제 Component 호출에 적용되지 않는 문제다.

---

### [핵심]

원인:

- import 경로 불일치
- vi.mock 위치 오류
- mock 초기화 누락
- default export / named export 혼동
- 실제 API가 호출됨
- MSW handler 경로 불일치
- baseURL 불일치
- 테스트 간 mock 상태 공유

---

### [실무]

Debug Flow:

```text
Mock 미적용
→ Component import 경로 확인
→ vi.mock 경로 확인
→ named/default export 확인
→ mock function 호출 여부 확인
→ MSW request URL 확인
→ beforeEach mock reset 확인
```

권장:

- mock 경로는 실제 import 경로와 일치
- 테스트마다 mock clear / reset
- API 함수 export 방식 확인
- MSW handler URL과 실제 요청 URL 일치
- 실제 네트워크 요청이 나가지 않게 확인

---

### [FAQ]

Q. mock을 했는데 실제 API가 호출돼?

A.
mock 경로가 실제 import 경로와 다르거나 MSW handler가 실제 요청 URL과 일치하지 않을 수 있다.

Q. mockResolvedValue가 적용되지 않아?

A.
mock 함수가 실제 호출되는 함수인지, named export와 default export를 혼동하지 않았는지 확인해야 한다.

---

## 19.4 Provider Missing Troubleshooting

### [개념]

Provider Missing은 Component가 Router, QueryClient, Auth Context, Theme Provider 등 필요한 Provider 없이 테스트되어 오류가 나는 상황이다.

---

### [핵심]

필요 Provider:

- Router Provider
- QueryClientProvider
- AuthProvider
- ThemeProvider
- Store Provider
- Intl Provider
- Toast Provider

---

### [실무]

Debug Flow:

```text
Provider 오류 발생
→ 오류 메시지 확인
→ Component가 사용하는 Hook 확인
→ 필요한 Provider 확인
→ renderWithProviders 추가
→ 테스트별 초기 상태 주입
```

예:

```tsx
function renderWithProviders(ui: ReactElement) {
  const queryClient = createTestQueryClient();

  return render(
    <MemoryRouter>
      <QueryClientProvider client={queryClient}>
        <AuthProvider>{ui}</AuthProvider>
      </QueryClientProvider>
    </MemoryRouter>,
  );
}
```

권장:

- 공통 renderWithProviders 작성
- 테스트별 auth state override 가능하게 설계
- QueryClient는 테스트마다 새로 생성
- Provider가 너무 많으면 Component 의존성 검토

---

### [FAQ]

Q. useNavigate may be used only in context 오류는 왜 나?

A.
Router Provider 없이 useNavigate를 사용하는 Component를 테스트했기 때문이다. MemoryRouter로 감싸야 한다.

Q. No QueryClient set 오류는 왜 나?

A.
QueryClientProvider 없이 TanStack Query Hook을 사용하는 Component를 테스트했기 때문이다.

---

# 20. Security Rules

## 20.1 Test Data Security

### [개념]

Test Data Security는 테스트 코드와 mock 데이터에 실제 비밀번호, token, 개인정보, secret이 포함되지 않도록 하는 기준이다.

---

### [핵심]

주의 대상:

- real password
- real access token
- real refresh token
- API secret
- OAuth secret
- personal email
- phone number
- address
- production URL
- payment information

---

### [실무]

권장:

- 테스트용 더미 데이터 사용
- 실제 token / secret commit 금지
- `.env.test`에도 secret 관리 주의
- production API URL 사용 금지
- 개인정보는 익명화
- snapshot에 민감정보 포함 주의
- mock response에 실제 사용자 데이터 사용 금지

예:

```typescript
const testUser = {
  userId: 1,
  email: "test@example.com",
  nickname: "tester",
};
```

---

### [FAQ]

Q. 테스트 코드에 실제 token을 넣어도 돼?

A.
안 된다. 테스트에는 더미 token을 사용하고 실제 secret이나 token을 commit하지 않는다.

Q. 운영 API URL로 테스트해도 돼?

A.
권장하지 않는다. 테스트는 mock 또는 테스트 환경을 사용해야 한다.

---

# 21. Comparison Rules

## 21.1 Required Comparisons

### [개념]

Frontend Testing 문서는 헷갈리는 테스트 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Unit Test vs Component Test
- Component Test vs Integration Test
- Integration Test vs E2E Test
- React Testing Library vs Enzyme
- userEvent vs fireEvent
- getBy vs findBy vs queryBy
- Mock Function vs MSW
- API Mock vs Real API
- Snapshot Test vs Behavior Test
- Implementation Detail Test vs User Behavior Test
- Loading Test vs Empty Test
- API Error Test vs Error Boundary Test
- Router Test vs Protected Route Test
- Vitest vs Jest Basics

---

### [실무]

예시:

| 비교     | Behavior Test            | Implementation Detail Test |
| -------- | ------------------------ | -------------------------- |
| 기준     | 사용자 행동과 결과       | 내부 구조와 상태           |
| 예       | 버튼 클릭 후 메시지 표시 | state 값 직접 확인         |
| 유지보수 | 상대적으로 좋음          | 구현 변경에 취약           |
| 권장도   | 높음                     | 낮음                       |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 테스트 선택 기준에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Frontend Testing 비교 문서에서 가장 중요한 것은?

A.
사용자 행동 기반 테스트와 구현 세부사항 테스트의 차이를 명확히 설명하는 것이다.

---

# 22. Checklist Rules

## 22.1 Frontend Testing Checklist

### [개념]

Frontend Testing 문서 검수 시 테스트 전략 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] 테스트 전략이 포함되었는가?
- [ ] Unit / Component / Integration / E2E 차이가 포함되었는가?
- [ ] React Testing Library 철학이 포함되었는가?
- [ ] Query Priority가 포함되었는가?
- [ ] getBy / findBy / queryBy 차이가 포함되었는가?
- [ ] userEvent 기준이 포함되었는가?
- [ ] fireEvent 사용 주의가 포함되었는가?
- [ ] Form 테스트 기준이 포함되었는가?
- [ ] Validation 테스트 기준이 포함되었는가?
- [ ] API Mocking 기준이 포함되었는가?
- [ ] MSW 기초 기준이 포함되었는가?
- [ ] Loading / Error / Empty 테스트가 포함되었는가?
- [ ] Router 테스트가 포함되었는가?
- [ ] Auth / Protected Route 테스트가 포함되었는가?
- [ ] TanStack Query 테스트 기준이 포함되었는가?
- [ ] Accessibility 테스트 기준이 포함되었는가?
- [ ] Snapshot 테스트 주의가 포함되었는가?
- [ ] Test File Structure가 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] Security 주의사항이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Strategy Check
→ RTL Philosophy Check
→ Query Check
→ User Event Check
→ Mocking Check
→ Async Check
→ Router / Auth Check
→ Accessibility Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Frontend Testing 문서 검수에서 가장 중요한 것은?

A.
사용자 관점 테스트, query priority, userEvent, API mocking, 비동기 테스트, 핵심 상태 UI 테스트 포함 여부다.

---

# 23. Retrieval Optimization Rules

## 23.1 Keyword Rules

### [개념]

Frontend Testing 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Frontend Testing
- React Testing
- React Testing Library
- RTL
- Vitest
- Jest
- jsdom
- Unit Test
- Component Test
- Integration Test
- E2E Test
- render
- screen
- userEvent
- fireEvent
- getByRole
- getByLabelText
- getByText
- findBy
- queryBy
- waitFor
- Mock Function
- vi.fn
- jest.fn
- API Mocking
- MSW
- Mock Service Worker
- Form Testing
- Validation Testing
- Loading Test
- Error State Test
- Empty State Test
- Router Testing
- Protected Route Test
- Auth Testing
- TanStack Query Testing
- QueryClientProvider
- Accessibility Testing
- Snapshot Testing
- Test Troubleshooting

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- React 테스트는 뭘 테스트해야 해?
- getBy와 findBy 차이는?
- userEvent와 fireEvent 차이는?
- API mock은 어떻게 해?
- 실제 API를 호출해도 돼?
- Form validation 테스트는 어떻게 해?
- Loading State 테스트는 어떻게 해?
- Protected Route 테스트는 어떻게 해?
- QueryClientProvider 오류는 왜 나?
- getByRole이 못 찾는 이유는?
- act warning은 왜 나?
- mock을 했는데 실제 API가 호출돼?
- Snapshot 테스트는 써도 돼?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 24. Version Rules

## 24.1 Modern Frontend Testing 기준

### [개념]

Frontend Testing 문서는 Modern React Testing 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- React Testing Library
- Vitest / Jest
- jsdom
- userEvent
- MSW 고려
- TanStack Query Test Setup
- React Router v6+
- Accessibility Query 우선
- User Behavior Test 우선
- TypeScript Ready Test

Legacy 제외:

- Enzyme 중심 shallow rendering
- 내부 state 직접 검사
- instance method 테스트
- class component 중심 테스트
- Snapshot 남용
- testId 남용
- 실제 운영 API 호출
- setTimeout으로 대충 기다리기
- 구현 세부사항 중심 테스트
- CSS class 중심 테스트

---

### [실무]

실무 기준:

```text
Modern Frontend Testing
→ User Behavior
→ Accessible Query
→ Controlled Mocking
→ Async Handling
→ State UI Verification
→ Maintainable Test
```

---

### [FAQ]

Q. Enzyme 방식도 다뤄?

A.
신규 React 문서에서는 React Testing Library와 사용자 관점 테스트를 우선한다.

Q. Vitest와 Jest 중 하나만 써야 해?

A.
프로젝트 환경에 맞춰 선택한다. Vite 기반 프로젝트는 Vitest를 많이 사용하고 CRA나 기존 프로젝트는 Jest를 사용할 수 있다.

---

# 25. Common Mistakes

## 25.1 Frontend Testing Common Mistakes

### [개념]

Frontend Testing 문서는 자주 발생하는 테스트 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- 내부 state 직접 테스트
- 구현 함수 호출 여부만 테스트
- 사용자 결과를 검증하지 않음
- getByRole 대신 testId 남용
- 비동기 UI에 getBy 사용
- userEvent await 누락
- waitFor 남용
- API mock 누락
- mock response shape 불일치
- 실제 API 호출
- QueryClientProvider 누락
- Router Provider 누락
- Auth Provider 누락
- 테스트 간 mock 상태 공유
- Query Cache 공유
- Snapshot 남용
- CSS class 중심 테스트
- StrictMode 중복 호출 오해
- act warning 방치
- 테스트 데이터에 실제 secret 사용
- 테스트 이름이 모호함

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: getByText가 요소를 찾지 못함
원인: API 응답 후 비동기로 렌더링되는 요소인데 getBy를 사용함
해결: await screen.findByText(...) 사용
```

---

### [FAQ]

Q. Frontend Testing 초보가 가장 많이 하는 실수는?

A.
사용자 결과 대신 내부 구현을 테스트하거나, 비동기 UI를 기다리지 않고 바로 검증하는 실수가 많다.

Q. 테스트 문제는 어떻게 찾는 게 좋아?

A.
screen.debug, Network mock, Provider 설정, query 선택, async await, mock 초기화를 순서대로 확인한다.

---

# 26. Final Goal

## 26.1 Domain Final Goal

### [개념]

Frontend Testing RAG 문서는 Frontend Agent가 사용자 관점에서 React Component, Form, API 상태, Routing, Auth 흐름을 안정적으로 검증하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Frontend Testing Strategy 이해
- Unit / Component / Integration / E2E 구분
- React Testing Library 철학 적용
- render / screen 사용
- Query Priority 적용
- getBy / findBy / queryBy 구분
- userEvent 기반 상호작용 테스트
- fireEvent 제한적 사용
- 순수 함수 테스트 작성
- Component 테스트 작성
- Form 테스트 작성
- Validation 테스트 작성
- API Mocking 작성
- MSW 기초 적용 판단
- Loading / Error / Empty 상태 테스트
- Router 테스트 작성
- Protected Route 테스트 작성
- Auth Flow 테스트 작성
- TanStack Query 테스트 설정
- Accessibility Query 테스트
- Snapshot 남용 방지
- Test File Structure 정리
- Async / Mock / Provider 오류 디버깅
- 테스트 데이터 보안 검토

---

### [실무]

Agent 수행 가능 작업:

```text
User Testing Request
→ Identify Test Target
→ Choose Test Type
→ Render Component with Providers
→ Query by User-visible Element
→ Simulate User Event
→ Mock API if Needed
→ Assert UI Result
→ Check Async / Accessibility / Security
→ Frontend Testing Output
```

---

### [FAQ]

Q. Frontend Testing 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 사용자 행동과 화면 결과를 기준으로 유지보수 가능한 React 테스트를 작성하고 검토하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Frontend Accessibility, Frontend Build & Deploy, Frontend Code Review, Styling Architecture 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Testing 문서는 왜 필요해?
A. Frontend Agent가 React Component, Form, API 상태, Routing, Auth 흐름을 사용자 관점에서 검증해야 하기 때문이다.

Q. React 테스트는 뭘 테스트해야 해?
A. 사용자가 보는 화면, 입력, 클릭, 결과 메시지, loading, error, empty 상태를 우선 테스트한다.

Q. Frontend 테스트는 뭐부터 작성해?
A. 핵심 Component와 사용자 흐름부터 작성하는 것이 좋다. Form, API 상태, 인증 흐름처럼 오류 가능성이 큰 부분이 우선이다.

Q. 모든 Component를 테스트해야 해?
A. 필수는 아니다. 재사용 빈도가 높거나 사용자 흐름에 중요한 Component를 우선 테스트한다.

Q. E2E 테스트만 있으면 충분해?
A. 아니다. E2E는 신뢰도가 높지만 느리고 유지보수 비용이 크므로 Component / Integration Test와 함께 사용하는 것이 좋다.

Q. CSS class도 테스트해야 해?
A. 대부분 권장하지 않는다. 사용자가 볼 수 있는 텍스트, 역할, 상태, 동작을 테스트하는 것이 좋다.

Q. React Testing Library는 Enzyme이랑 뭐가 달라?
A. React Testing Library는 구현 내부보다 사용자가 보는 결과와 상호작용을 중심으로 테스트한다.

Q. 내부 state 값을 직접 확인하면 안 돼?
A. 권장하지 않는다. state가 아니라 사용자가 볼 수 있는 UI 결과를 검증하는 것이 더 유지보수에 좋다.

Q. screen을 왜 써?
A. 현재 테스트 화면에서 요소를 찾는 방식이 명확하고 React Testing Library 권장 패턴이기 때문이다.

Q. Router나 QueryClient Provider가 필요하면?
A. custom render 함수를 만들어 테스트마다 반복 설정을 줄이는 것이 좋다.

Q. getByRole을 왜 우선 사용해?
A. 사용자가 보조기술로 인식하는 역할과 이름을 기준으로 요소를 찾기 때문에 실제 사용성에 가깝다.

Q. testId는 쓰면 안 돼?
A. 쓰면 안 되는 것은 아니지만 사용자가 인식할 수 없는 구현용 식별자라 최후 수단으로 사용하는 것이 좋다.

Q. getBy와 findBy 차이는?
A. getBy는 즉시 존재하는 요소를 찾고 findBy는 비동기적으로 나중에 나타나는 요소를 기다린다.

Q. 요소가 없어야 하는 테스트는 뭘 써?
A. queryBy를 사용해 null인지 확인한다.

Q. findBy와 waitFor 중 뭐를 써?
A. 화면 요소가 나타나는 것을 기다릴 때는 findBy가 더 간단하고, callback 호출이나 복잡한 조건은 waitFor를 사용할 수 있다.

Q. waitFor를 무조건 쓰면 돼?
A. 아니다. 불필요한 waitFor는 테스트를 느리고 불명확하게 만든다.

Q. userEvent와 fireEvent 차이는?
A. userEvent는 실제 사용자 상호작용에 더 가깝고 fireEvent는 단일 DOM 이벤트를 직접 발생시키는 저수준 도구다.

Q. user.type에 await가 필요한 이유는?
A. userEvent는 실제 이벤트 흐름을 비동기로 처리할 수 있으므로 await를 사용하는 것이 안전하다.

Q. fireEvent를 쓰면 안 돼?
A. 쓰면 안 되는 것은 아니지만 일반 사용자 행동 테스트에는 userEvent가 더 적합하다.

Q. fireEvent는 언제 써?
A. userEvent로 표현하기 어려운 저수준 이벤트나 커스텀 이벤트를 테스트할 때 사용한다.

Q. 어떤 함수는 Unit Test가 좋아?
A. validation, mapper, formatter처럼 입력과 출력이 명확한 순수 함수가 Unit Test에 적합하다.

Q. Component 내부 함수를 직접 테스트해야 해?
A. 보통은 사용자 결과를 통해 테스트한다. 복잡한 로직은 별도 순수 함수로 분리해 테스트할 수 있다.

Q. Validation은 Component 테스트만 하면 안 돼?
A. 간단하면 가능하지만 검증 로직이 복잡하면 함수 단위 테스트가 더 빠르고 명확하다.

Q. 에러 메시지 문자열까지 테스트해야 해?
A. 사용자에게 중요한 메시지라면 가능하다. 다만 문구 변경이 잦으면 에러 코드나 key 중심 테스트를 고려한다.

Q. Presentational Component는 뭘 테스트해?
A. props에 따라 사용자가 보는 텍스트, 버튼 상태, 이미지, 조건부 UI가 올바른지 테스트한다.

Q. className이 맞는지 테스트해야 해?
A. 대부분 지양한다. 스타일 자체보다 사용자에게 보이는 상태와 의미를 테스트하는 것이 좋다.

Q. Controlled Component는 테스트가 왜 어려워?
A. value가 부모 state에서 내려오므로 테스트에서도 상태를 업데이트하는 wrapper가 필요할 수 있다.

Q. 버튼 클릭 테스트는 어떻게 해?
A. userEvent로 버튼을 클릭하고 callback 호출 또는 화면 변화를 확인한다.

Q. Form input 테스트는 어떻게 해?
A. userEvent로 값을 입력하고 submit 후 callback 호출 값이나 화면 결과를 검증한다.

Q. input은 getByLabelText로 찾는 게 좋아?
A. 좋다. label 연결이 잘 되어 있는지 함께 검증할 수 있다.

Q. Validation 테스트에서 뭘 확인해?
A. 오류 메시지가 표시되는지, 잘못된 입력으로 submit이 중단되는지, 필요하면 API 호출이 발생하지 않는지 확인한다.

Q. 서버 validation error도 테스트해?
A. 중요한 Form이라면 API mock을 통해 서버 field error가 화면에 표시되는지 테스트하는 것이 좋다.

Q. 제출 중 버튼 disabled도 테스트해야 해?
A. 중복 제출이 중요한 Form이라면 테스트하는 것이 좋다.

Q. pending promise 테스트는 위험해?
A. 잘못 관리하면 테스트가 끝나지 않을 수 있다. 필요한 범위에서만 사용하고 상태 확인 후 테스트가 종료되도록 구성한다.

Q. Frontend 테스트에서 실제 API를 호출해도 돼?
A. 일반 Component 테스트에서는 권장하지 않는다. API 응답은 mock으로 제어하는 것이 안정적이다.

Q. API mock은 왜 필요해?
A. 테스트가 서버 상태, 네트워크, DB에 의존하지 않고 원하는 상황을 재현할 수 있게 하기 위해 필요하다.

Q. MSW는 언제 써?
A. Component가 실제 API 요청을 보내는 흐름에 가깝게 테스트하고 싶을 때 유용하다.

Q. API 함수 mock과 MSW 중 뭐가 좋아?
A. 작은 단위는 API 함수 mock이 간단하고, 여러 Component와 실제 요청 흐름을 검증하려면 MSW가 더 적합할 수 있다.

Q. 에러 응답도 테스트해야 해?
A. 중요한 화면이라면 해야 한다. 실제 서비스에서는 성공보다 실패 상황 UX가 사용자 경험에 큰 영향을 준다.

Q. mockRejectedValue 구조는 실제 AxiosError와 같아야 해?
A. 가능하면 실제 코드가 참조하는 error.response.status, error.response.data 구조와 맞춰야 한다.

Q. Loading 상태도 테스트해야 해?
A. 사용자 경험에 중요한 화면이라면 테스트하는 것이 좋다. 특히 빈 화면 방지를 확인할 수 있다.

Q. Skeleton은 어떻게 테스트해?
A. 사용자가 인식할 수 있는 role, label, loading message 또는 testId를 기준으로 확인할 수 있다.

Q. ErrorState 테스트에서 뭘 봐야 해?
A. 사용자 메시지, 재시도 버튼, 권한 안내, Not Found 안내처럼 사용자가 볼 수 있는 결과를 확인한다.

Q. Error Boundary 테스트와 API Error 테스트는 달라?
A. 다르다. API Error는 요청 실패 상태이고 Error Boundary는 렌더링 중 예외 처리다.

Q. Empty State 테스트는 왜 필요해?
A. 데이터가 없을 때 빈 화면이 아니라 적절한 안내가 나오는지 확인하기 위해 필요하다.

Q. Empty State와 Error State 테스트는 어떻게 달라?
A. Empty State는 성공 응답의 빈 데이터이고 Error State는 요청 실패다.

Q. React Router 테스트에는 BrowserRouter를 써?
A. 테스트에서는 MemoryRouter를 많이 사용한다. 초기 경로를 쉽게 제어할 수 있기 때문이다.

Q. Route Param 테스트는 어떻게 해?
A. initialEntries에 `/festivals/1` 같은 경로를 넣고 화면 결과를 검증한다.

Q. Protected Route는 어떻게 테스트해?
A. 인증 상태를 mock으로 주입하고 보호 경로 접근 시 로그인 페이지 또는 실제 페이지가 표시되는지 검증한다.

Q. auth loading도 테스트해야 해?
A. 중요하다. 인증 초기화 중 잘못 redirect되는 문제를 방지할 수 있다.

Q. 로그인 테스트에서 뭘 확인해?
A. 입력, 제출, 성공 처리, 실패 메시지, 인증 상태 변경, redirect 결과를 확인한다.

Q. 로그인 실패도 테스트해야 해?
A. 중요하다. 인증 실패 UX는 사용자가 자주 마주칠 수 있는 흐름이다.

Q. 로그아웃 테스트는 뭘 봐야 해?
A. 로그아웃 후 인증 UI가 사라지고 보호 페이지에 접근할 수 없으며 사용자 상태가 정리되는지 확인한다.

Q. token 삭제 자체를 직접 테스트해야 해?
A. 가능하지만 보통은 사용자 UI와 보호 route 결과로 검증하는 것이 더 유지보수에 좋다.

Q. TanStack Query Component 테스트에서 Provider 오류가 나?
A. QueryClientProvider로 감싸야 한다.

Q. 테스트에서 retry를 false로 하는 이유는?
A. 실패 테스트가 재시도 때문에 느려지거나 예측하기 어려워지는 것을 방지하기 위해서다.

Q. useQuery 내부 상태를 직접 테스트해야 해?
A. 보통은 아니다. loading, error, data UI 결과를 테스트하는 것이 좋다.

Q. queryKey를 테스트해야 해?
A. 직접 queryKey 문자열을 테스트하기보다 검색 조건 변경 후 올바른 데이터가 표시되는지 검증하는 것이 좋다.

Q. mutation 테스트에서 함수 호출만 확인하면 돼?
A. 부족할 수 있다. 사용자가 보는 성공 메시지, 목록 갱신, form reset 같은 결과를 함께 확인하는 것이 좋다.

Q. invalidateQueries를 직접 테스트해야 해?
A. 직접 호출 여부보다 mutation 후 화면 데이터가 갱신되는지 확인하는 것이 더 사용자 관점에 가깝다.

Q. getByRole 테스트가 실패하면 접근성 문제야?
A. 항상은 아니지만 role이나 accessible name이 부족할 가능성이 있다. HTML 구조와 aria 속성을 확인해야 한다.

Q. 접근성 테스트를 따로 해야 해?
A. 기본 query를 접근성 중심으로 작성하면 많은 접근성 문제를 초기에 발견할 수 있다.

Q. axe 테스트만 통과하면 접근성은 끝이야?
A. 아니다. 자동화 도구는 일부 문제만 잡을 수 있다. 키보드 조작, 스크린 리더 흐름, focus 관리도 확인해야 한다.

Q. Snapshot 테스트는 쓰면 안 돼?
A. 쓰면 안 되는 것은 아니지만 전체 UI를 snapshot으로만 검증하는 것은 유지보수성이 낮다.

Q. Snapshot이 자주 깨지면 어떻게 해?
A. 테스트 의도가 약한 snapshot일 가능성이 있다. 사용자 관점 assertion으로 바꾸는 것이 좋다.

Q. 테스트 파일은 Component 옆에 두는 게 좋아?
A. 많이 사용되는 방식이다. 관련 파일이 가까워 유지보수하기 쉽다. 팀 컨벤션에 맞추면 된다.

Q. test utils는 어디에 둬?
A. 공통 renderWithProviders, mock server setup, test data factory는 test 폴더에 둘 수 있다.

Q. 테스트 이름은 한글로 써도 돼?
A. 가능하다. 팀 컨벤션에 맞추면 되며 사용자 시나리오를 명확히 표현하는 것이 중요하다.

Q. component renders 같은 이름은 왜 별로야?
A. 무엇을 렌더링해야 하는지, 어떤 결과를 기대하는지 알기 어렵기 때문이다.

Q. getByText가 못 찾는데 화면에는 보이는 것 같아?
A. 텍스트가 여러 요소로 나뉘었거나 비동기 렌더링 전일 수 있다. screen.debug와 findBy를 확인한다.

Q. getByRole이 실패하면?
A. 해당 요소의 semantic role과 accessible name이 제대로 있는지 확인해야 한다.

Q. act warning은 왜 나?
A. 테스트가 상태 업데이트가 끝나기 전에 assertion을 하거나 비동기 처리를 기다리지 않았을 가능성이 있다.

Q. 비동기 테스트가 가끔 실패해?
A. await 누락, 불안정한 timer, 실제 시간 의존, query retry, mock 초기화 누락을 확인해야 한다.

Q. mock을 했는데 실제 API가 호출돼?
A. mock 경로가 실제 import 경로와 다르거나 MSW handler가 실제 요청 URL과 일치하지 않을 수 있다.

Q. mockResolvedValue가 적용되지 않아?
A. mock 함수가 실제 호출되는 함수인지, named export와 default export를 혼동하지 않았는지 확인해야 한다.

Q. useNavigate may be used only in context 오류는 왜 나?
A. Router Provider 없이 useNavigate를 사용하는 Component를 테스트했기 때문이다. MemoryRouter로 감싸야 한다.

Q. No QueryClient set 오류는 왜 나?
A. QueryClientProvider 없이 TanStack Query Hook을 사용하는 Component를 테스트했기 때문이다.

Q. 테스트 코드에 실제 token을 넣어도 돼?
A. 안 된다. 테스트에는 더미 token을 사용하고 실제 secret이나 token을 commit하지 않는다.

Q. 운영 API URL로 테스트해도 돼?
A. 권장하지 않는다. 테스트는 mock 또는 테스트 환경을 사용해야 한다.

Q. Vitest와 Jest 중 하나만 써야 해?
A. 프로젝트 환경에 맞춰 선택한다. Vite 기반 프로젝트는 Vitest를 많이 사용하고 CRA나 기존 프로젝트는 Jest를 사용할 수 있다.

Q. Frontend Testing 초보가 가장 많이 하는 실수는?
A. 사용자 결과 대신 내부 구현을 테스트하거나, 비동기 UI를 기다리지 않고 바로 검증하는 실수가 많다.

Q. 테스트 문제는 어떻게 찾는 게 좋아?
A. screen.debug, Network mock, Provider 설정, query 선택, async await, mock 초기화를 순서대로 확인한다.

Q. Frontend Testing 다음 문서는 뭐가 좋아?
A. Frontend Accessibility, Frontend Build & Deploy, Frontend Code Review, Styling Architecture 순서가 좋다.
