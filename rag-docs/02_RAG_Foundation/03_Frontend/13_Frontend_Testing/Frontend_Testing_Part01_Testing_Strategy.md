# Frontend Testing Part01 - Testing Strategy

---

# 1. Frontend Testing Overview

## 1.1 Frontend Testing Definition

### [개념]

Frontend Testing은 사용자가 화면에서 보고 조작하는 UI, 상태 변화, API 결과, Routing, Form, Auth 흐름이 정상 동작하는지 검증하는 테스트 영역이다.

Frontend Testing은 내부 구현보다 사용자 행동과 화면 결과를 기준으로 작성한다.

---

### [핵심]

- Frontend Testing
- React Testing
- React Testing Library
- User Behavior Test
- Component Test
- Integration Test
- E2E Test
- UI State Test
- Form Testing
- API Mocking
- Router Testing
- Auth Testing
- Accessibility Query
- Implementation Detail Test 지양

---

### [실무]

2026 실무 기준에서 Frontend Testing은 단순 렌더링 확인이 아니다.

검증 기준:

```text
사용자 화면
→ 사용자 입력
→ 사용자 클릭
→ API 상태 변화
→ Loading / Error / Empty / Success UI
→ Routing 결과
→ Auth 상태 결과
```

좋은 Frontend Test는 사용자가 체감하는 결과를 검증한다.

예:

```text
검색어 입력 후 검색 버튼 클릭
→ 검색 결과 표시
→ 결과 없음이면 EmptyState 표시
→ 서버 오류면 ErrorState 표시
```

나쁜 Frontend Test는 내부 구현에 과도하게 의존한다.

예:

```text
state 값 직접 확인
internal function 호출 여부만 확인
CSS className만 확인
snapshot 하나로 전체 화면 검증
```

---

### [FAQ]

Q. Frontend Testing은 뭐야?
A. 사용자가 보는 화면, 입력, 클릭, 상태 변화, 결과 UI를 검증하는 테스트다.

Q. Frontend Testing에서 가장 중요한 기준은 뭐야?
A. 내부 구현보다 사용자 행동과 화면 결과를 기준으로 테스트하는 것이다.

Q. React Component가 렌더링되는지만 확인하면 충분해?
A. 부족하다. 사용자 입력, 클릭, API 상태, 오류 상태, Routing 결과까지 핵심 흐름을 검증해야 한다.

---

# 2. Testing Philosophy

## 2.1 User Behavior First

### [개념]

User Behavior First는 테스트를 작성할 때 내부 코드 구조보다 사용자가 실제로 수행하는 행동과 결과를 우선하는 원칙이다.

React Testing Library의 핵심 철학은 사용자 관점 테스트다.

---

### [핵심]

- User Behavior First
- User-visible Result
- Screen Result
- DOM Result
- Accessible Query
- click
- type
- submit
- navigation
- message display
- loading display
- error display
- internal state 직접 검증 지양

---

### [실무]

테스트 작성 기준:

```text
사용자가 요소를 볼 수 있는가?
사용자가 입력할 수 있는가?
사용자가 클릭할 수 있는가?
행동 후 결과가 화면에 표시되는가?
실패 상황에서 안내가 표시되는가?
```

권장 테스트 흐름:

```text
Render Component
→ Find Element by Role / Label / Text
→ Simulate User Event
→ Wait for Async Result
→ Assert User-visible UI
```

예:

```tsx
test("검색어를 입력하고 검색하면 검색 결과를 표시한다", async () => {
  const user = userEvent.setup();

  render(<FestivalSearchPage />);

  await user.type(screen.getByLabelText("검색어"), "봄꽃");
  await user.click(screen.getByRole("button", { name: "검색" }));

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

---

### [FAQ]

Q. User Behavior Test는 뭐야?
A. 사용자가 실제로 입력, 클릭, 이동하는 흐름과 그 결과 화면을 검증하는 테스트다.

Q. 내부 state를 직접 테스트하면 안 돼?
A. 권장하지 않는다. state 값보다 사용자가 볼 수 있는 화면 결과를 검증하는 것이 유지보수에 좋다.

Q. React Testing Library는 왜 사용자 관점을 강조해?
A. 구현 방식이 바뀌어도 사용자 결과가 같으면 테스트가 깨지지 않도록 하기 위해서다.

---

## 2.2 Implementation Detail Test Caution

### [개념]

Implementation Detail Test는 Component 내부 state, private function, className, hook 내부 구조처럼 사용자가 직접 인식하지 못하는 구현 세부사항을 검증하는 테스트다.

Frontend Testing에서는 Implementation Detail Test를 지양한다.

---

### [핵심]

지양 대상:

- 내부 state 직접 확인
- 내부 함수 직접 호출
- private method 테스트
- hook 내부 변수명 테스트
- CSS className 중심 테스트
- DOM 구조 과도 검증
- 전체 snapshot 의존
- 라이브러리 내부 동작 검증
- mock 함수 호출만 검증하고 UI 결과 미검증

---

### [실무]

나쁜 예:

```tsx
test("state가 변경된다", () => {
  expect(component.state.searchKeyword).toBe("축제");
});
```

좋은 예:

```tsx
test("검색어를 입력하면 입력값이 화면에 표시된다", async () => {
  const user = userEvent.setup();

  render(<SearchForm />);

  await user.type(screen.getByLabelText("검색어"), "축제");

  expect(screen.getByDisplayValue("축제")).toBeInTheDocument();
});
```

검증 기준:

```text
사용자가 인식할 수 있는 결과인가?
구현 변경에 쉽게 깨지지 않는가?
테스트 실패 시 기능 문제가 명확한가?
```

---

### [FAQ]

Q. Implementation Detail Test는 왜 피해야 해?
A. 내부 구현 변경만으로 테스트가 깨져 유지보수 비용이 커지기 때문이다.

Q. CSS className 테스트는 무조건 나쁜가?
A. 대부분 우선순위가 낮다. 사용자에게 보이는 텍스트, 역할, 상태, 동작을 먼저 테스트한다.

Q. mock 함수 호출 여부만 확인하면 안 돼?
A. 부족할 수 있다. 가능하면 호출 후 사용자에게 보이는 UI 결과까지 검증한다.

---

# 3. Testing Pyramid

## 3.1 Frontend Testing Pyramid

### [개념]

Testing Pyramid는 테스트를 목적, 속도, 비용, 신뢰도에 따라 나누는 전략이다.

Frontend에서는 Unit Test, Component Test, Integration Test, E2E Test를 조합한다.

---

### [핵심]

| Test Type        | 목적                            | 속도 |      비용 | 예                      |
| ---------------- | ------------------------------- | ---: | --------: | ----------------------- |
| Unit Test        | 순수 함수 검증                  | 빠름 |      낮음 | validation, formatter   |
| Component Test   | 단일 Component UI 검증          | 빠름 | 낮음~중간 | Button, Form, Modal     |
| Integration Test | 여러 Component와 상태 흐름 검증 | 중간 |      중간 | Login Flow, Search Flow |
| E2E Test         | 실제 브라우저 전체 흐름 검증    | 느림 |      높음 | 회원가입부터 로그인까지 |

---

### [실무]

권장 비율:

```text
많이 작성
→ Unit Test / Component Test

적당히 작성
→ Integration Test

핵심 흐름만 작성
→ E2E Test
```

주의:

- 모든 것을 E2E로 검증하지 않음
- 모든 것을 Unit Test로만 쪼개지 않음
- 핵심 사용자 흐름은 Integration Test 또는 E2E Test로 보강
- 단순 snapshot보다 실제 상호작용 검증 우선
- 테스트 비용 대비 회귀 방지 효과를 고려

---

### [FAQ]

Q. Frontend 테스트는 어떤 종류가 있어?
A. Unit Test, Component Test, Integration Test, E2E Test가 있다.

Q. E2E Test만 있으면 충분해?
A. 아니다. E2E는 신뢰도는 높지만 느리고 유지보수 비용이 커서 Component Test와 함께 사용해야 한다.

Q. Unit Test만 많이 작성하면 충분해?
A. 아니다. 사용자 UI 흐름과 Component 상호작용은 Component Test나 Integration Test로 검증해야 한다.

---

## 3.2 Unit Test Strategy

### [개념]

Unit Test는 입력과 출력이 명확한 작은 함수나 로직을 독립적으로 검증하는 테스트다.

Frontend에서는 validation, formatter, mapper, filter, sorting utility에 적합하다.

---

### [핵심]

Unit Test 대상:

- validation function
- formatter
- mapper
- date utility
- filter function
- sorting function
- error message mapper
- request dto mapper
- pure function
- business rule helper

---

### [실무]

Unit Test가 적합한 경우:

```text
입력이 명확함
→ 출력이 명확함
→ UI 렌더링이 필요 없음
→ 빠르게 edge case 검증 가능
```

예:

```ts
function toReviewRequest(festivalId: number, content: string, rating: string) {
  return {
    festivalId,
    content: content.trim(),
    rating: Number(rating),
  };
}

test("리뷰 입력값을 리뷰 등록 요청 값으로 변환한다", () => {
  expect(toReviewRequest(1, " 좋았어요 ", "5")).toEqual({
    festivalId: 1,
    content: "좋았어요",
    rating: 5,
  });
});
```

권장:

- 정상 케이스와 실패 케이스 모두 작성
- boundary value 포함
- 날짜 / timezone / locale 주의
- Component 내부 복잡 로직은 순수 함수로 분리 가능

---

### [FAQ]

Q. Frontend에서 Unit Test는 언제 써?
A. validation, formatter, mapper처럼 입력과 출력이 명확한 순수 함수에 사용한다.

Q. Component 내부 함수도 Unit Test로 직접 테스트해야 해?
A. 보통은 사용자 결과로 테스트한다. 복잡하면 별도 순수 함수로 분리해 테스트한다.

Q. Unit Test의 장점은 뭐야?
A. 빠르고 안정적이며 edge case를 많이 검증하기 좋다.

---

## 3.3 Component Test Strategy

### [개념]

Component Test는 React Component가 props, state, user event, conditional rendering에 따라 올바른 UI 결과를 만드는지 검증한다.

---

### [핵심]

Component Test 대상:

- Presentational Component
- Interactive Component
- Button
- Form
- Modal
- Dropdown
- Tab
- List
- Card
- EmptyState
- ErrorState
- LoadingState
- callback
- conditional rendering

---

### [실무]

Component Test 기준:

```text
Component Render
→ Props 기반 UI 표시
→ User Event 실행
→ Callback 또는 UI 결과 검증
→ Loading / Error / Empty 상태 확인
```

예:

```tsx
test("축제 카드에 제목과 지역명을 표시한다", () => {
  render(
    <FestivalCard
      festival={{
        festivalId: 1,
        title: "봄꽃 축제",
        regionName: "서울",
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

- 사용자에게 보이는 텍스트와 role 검증
- callback은 userEvent 이후 검증
- disabled / loading 상태 포함
- className 중심 검증 지양
- snapshot만으로 대체하지 않음

---

### [FAQ]

Q. Component Test는 뭘 검증해?
A. props, 사용자 입력, 클릭, 조건부 렌더링에 따른 화면 결과를 검증한다.

Q. 모든 Component를 테스트해야 해?
A. 필수는 아니다. 재사용 빈도가 높거나 핵심 사용자 흐름에 포함되는 Component를 우선 테스트한다.

Q. Presentational Component도 테스트해야 해?
A. 중요 UI이거나 조건부 렌더링이 있으면 테스트하는 것이 좋다.

---

## 3.4 Integration Test Strategy

### [개념]

Integration Test는 여러 Component, 상태 관리, Router, API Mock이 함께 동작하는 사용자 흐름을 검증하는 테스트다.

Frontend에서는 Login Flow, Search Flow, Form Submit Flow, Protected Route Flow에 적합하다.

---

### [핵심]

Integration Test 대상:

- Login Flow
- Logout Flow
- Search Flow
- Form Submit Flow
- API success flow
- API error flow
- Router navigation
- Protected Route
- Auth state
- TanStack Query state
- Global Store
- Toast message
- cache invalidation result

---

### [실무]

Integration Test 흐름:

```text
Render Page with Providers
→ Mock API Response
→ User Interaction
→ State Change
→ UI Result
→ Route Result
```

예:

```tsx
test("로그인 성공 후 마이페이지로 이동한다", async () => {
  const user = userEvent.setup();

  mockLoginSuccess();

  renderWithProviders(<AppRoutes />, {
    initialEntries: ["/login"],
  });

  await user.type(screen.getByLabelText("이메일"), "test@example.com");
  await user.type(screen.getByLabelText("비밀번호"), "password123");
  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(
    await screen.findByRole("heading", { name: "마이페이지" }),
  ).toBeInTheDocument();
});
```

권장:

- 실제 API 서버 호출 금지
- API Mock 또는 MSW 사용
- Provider 누락 방지
- 사용자 흐름 중심 테스트명 작성
- 실패 상황도 함께 검증

---

### [FAQ]

Q. Integration Test는 Component Test와 뭐가 달라?
A. Component Test는 단일 Component 중심이고 Integration Test는 여러 Component, 상태, Router, API Mock 흐름을 함께 검증한다.

Q. Integration Test에서 실제 API를 호출해도 돼?
A. 일반적으로 권장하지 않는다. API 응답은 mock으로 제어한다.

Q. Integration Test는 언제 필요해?
A. 로그인, 검색, Form 제출, 인증 Route처럼 여러 요소가 함께 동작하는 핵심 흐름에 필요하다.

---

## 3.5 E2E Test Strategy

### [개념]

E2E Test는 실제 브라우저 환경에서 사용자 흐름 전체가 정상 동작하는지 검증하는 테스트다.

Frontend Testing Foundation에서는 E2E Test의 위치와 기준만 다룬다.

---

### [핵심]

E2E Test 대상:

- 회원가입 전체 흐름
- 로그인 전체 흐름
- 결제 핵심 흐름
- 게시글 작성 흐름
- 예약 / 신청 흐름
- 관리자 핵심 작업
- 서비스 핵심 사용자 여정
- smoke test
- critical path

---

### [실무]

E2E Test 기준:

```text
실제 브라우저 실행
→ 실제 사용자 경로 이동
→ 실제 UI 조작
→ 핵심 결과 검증
```

권장:

- 핵심 흐름만 선별
- 너무 많은 E2E Test 작성 지양
- 느리고 불안정한 테스트 최소화
- Component / Integration Test로 대부분 보강
- Playwright / Cypress 심화는 별도 E2E Testing 문서에서 관리

---

### [FAQ]

Q. E2E Test는 언제 써?
A. 로그인, 결제, 회원가입처럼 서비스 핵심 흐름을 실제 브라우저 기준으로 검증할 때 사용한다.

Q. E2E Test를 많이 작성하면 좋은가?
A. 아니다. 느리고 유지보수 비용이 높으므로 핵심 사용자 흐름 위주로 작성한다.

Q. Playwright 사용법도 이 문서에서 다뤄?
A. 이 문서에서는 E2E의 위치와 기준만 다루고 Playwright 심화는 별도 문서에서 다룬다.

---

# 4. What To Test

## 4.1 High Priority Test Targets

### [개념]

High Priority Test Target은 실패했을 때 사용자 경험이나 핵심 기능에 큰 영향을 주는 테스트 대상이다.

Frontend Testing은 사용자 가치와 회귀 위험이 높은 영역을 우선 테스트한다.

---

### [핵심]

우선 테스트 대상:

- 사용자 입력
- 버튼 클릭
- Form submit
- Validation message
- API success state
- API loading state
- API error state
- Empty state
- Routing result
- Protected Route
- Auth Flow
- Permission UI
- Conditional rendering
- Critical business flow
- Payment UI flow
- Review submit flow
- Search result flow

---

### [실무]

테스트 가치 판단 기준:

```text
사용자가 체감하는가?
실패하면 중요한 기능이 깨지는가?
반복 회귀 가능성이 높은가?
수동 확인 비용이 큰가?
비즈니스 영향이 큰가?
```

우선순위 높은 예:

```text
로그인 실패 시 오류 메시지 표시
검색 결과 없음 안내 표시
비로그인 사용자가 마이페이지 접근 시 로그인 페이지 표시
리뷰 작성 후 목록 갱신
API 실패 시 다시 시도 버튼 표시
```

우선순위 낮은 예:

```text
Button className이 primary인지 확인
내부 state 이름 확인
라이브러리 내부 함수 호출 확인
전체 페이지 snapshot만 비교
```

---

### [FAQ]

Q. Frontend 테스트는 뭐부터 작성해?
A. 핵심 사용자 흐름, Form, API 상태, 인증 흐름처럼 실패 영향이 큰 부분부터 작성한다.

Q. 모든 UI 상태를 테스트해야 해?
A. 핵심 화면에서는 Loading, Error, Empty, Success 상태를 우선 검증하는 것이 좋다.

Q. 단순 스타일도 테스트해야 해?
A. 대부분 우선순위가 낮다. 사용자에게 보이는 의미와 동작을 먼저 검증한다.

---

## 4.2 Low Priority Test Targets

### [개념]

Low Priority Test Target은 사용자 기능 검증 효과가 낮거나 구현 변경에 취약한 테스트 대상이다.

이 영역은 필요한 경우에만 제한적으로 테스트한다.

---

### [핵심]

낮은 우선순위:

- 단순 CSS class
- inline style
- 내부 state 이름
- private function
- hook 내부 변수명
- 라이브러리 내부 동작
- 단순 렌더링 smoke test
- 큰 snapshot
- data-testid 남용
- DOM 구조 세부사항
- 구현 함수 호출 여부만 검증

---

### [실무]

지양 예:

```tsx
expect(button).toHaveClass("primary-button");
```

대체 예:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeEnabled();
```

지양 예:

```tsx
expect(handleClick).toHaveBeenCalled();
```

보완 예:

```tsx
await user.click(screen.getByRole("button", { name: "저장" }));

expect(await screen.findByText("저장되었습니다.")).toBeInTheDocument();
```

기준:

```text
사용자 결과를 검증할 수 있으면 사용자 결과를 우선한다.
구현 세부사항 검증은 최후 수단으로 제한한다.
```

---

### [FAQ]

Q. className 테스트는 아예 하지 말아야 해?
A. 아니다. 하지만 대부분 사용자 결과 검증보다 우선순위가 낮다.

Q. data-testid는 쓰면 안 돼?
A. 쓸 수 있지만 role, label, text로 찾기 어려운 경우의 최후 수단으로 사용한다.

Q. 단순 렌더링 테스트는 의미가 없어?
A. 일부 smoke test로는 가능하지만 핵심 테스트는 사용자 행동과 결과를 포함해야 한다.

---

# 5. Test Selection Rules

## 5.1 Choosing Test Type

### [개념]

Choosing Test Type은 테스트 대상에 맞게 Unit Test, Component Test, Integration Test, E2E Test 중 적절한 테스트 유형을 선택하는 기준이다.

---

### [핵심]

선택 기준:

| 상황                                  | 권장 테스트      |
| ------------------------------------- | ---------------- |
| formatter / validation / mapper 검증  | Unit Test        |
| props 기반 UI 표시 검증               | Component Test   |
| 클릭 / 입력 / Modal 동작 검증         | Component Test   |
| API Mock 기반 Page 상태 검증          | Integration Test |
| Router / Auth Provider 포함 흐름 검증 | Integration Test |
| 실제 브라우저 핵심 사용자 여정 검증   | E2E Test         |
| 전체 서비스 smoke 검증                | E2E Test         |

---

### [실무]

선택 Flow:

```text
순수 함수인가?
→ Unit Test

단일 Component UI인가?
→ Component Test

여러 Component / Provider / API 상태가 엮이는가?
→ Integration Test

실제 브라우저에서 전체 사용자 여정 검증이 필요한가?
→ E2E Test
```

주의:

- 테스트 유형을 과하게 높이지 않음
- Unit으로 충분한 것을 E2E로 만들지 않음
- E2E로만 검증하고 세부 상태 테스트를 생략하지 않음
- Integration Test에서 실제 서버 의존을 만들지 않음

---

### [FAQ]

Q. 어떤 테스트 유형을 선택해야 할지 모르겠어.
A. 순수 함수는 Unit, 단일 UI는 Component, 여러 흐름은 Integration, 실제 브라우저 핵심 여정은 E2E로 선택한다.

Q. Page Component는 Component Test야 Integration Test야?
A. API, Router, Provider, 상태 흐름이 포함되면 Integration Test에 가깝다.

Q. 작은 UI도 E2E로 테스트해도 돼?
A. 가능은 하지만 비용이 크다. 작은 UI는 Component Test가 더 적합하다.

---

## 5.2 Test Priority Decision

### [개념]

Test Priority Decision은 테스트 작성 순서를 정하는 기준이다.

모든 것을 한 번에 테스트하지 않고 가치가 높은 영역부터 테스트한다.

---

### [핵심]

우선순위 판단:

1. Critical User Flow
2. Auth / Permission
3. Form / Validation
4. API State
5. Error Handling
6. Routing
7. Reusable Component
8. Utility Function
9. Accessibility Risk
10. Regression Risk

---

### [실무]

우선순위 높은 테스트:

```text
로그인 / 로그아웃
회원가입
결제
글 작성 / 수정 / 삭제
검색 / 필터
리뷰 등록
보호 라우트
권한별 UI
API 실패 처리
```

우선순위 낮은 테스트:

```text
단순 텍스트 표시
단순 wrapper Component
스타일 class
레이아웃 margin
변경 잦은 snapshot
```

권장:

```text
기능 실패 영향이 큰 테스트
→ 먼저 작성

반복 회귀가 잦은 테스트
→ 먼저 작성

수동 확인이 번거로운 테스트
→ 자동화 우선
```

---

### [FAQ]

Q. 테스트 작성 순서는 어떻게 정해?
A. 핵심 사용자 흐름, 인증, Form, API 상태, 오류 처리, Routing 순서로 우선순위를 잡는다.

Q. 시간이 부족하면 어떤 테스트만 작성해?
A. 로그인, Form 제출, API 성공/실패, 보호 Route 같은 핵심 흐름을 먼저 작성한다.

Q. 단순 Component는 나중에 해도 돼?
A. 핵심 흐름에 영향이 적다면 나중에 해도 된다.

---

# 6. Frontend Testing Anti Pattern

## 6.1 Common Anti Patterns

### [개념]

Frontend Testing Anti Pattern은 테스트 신뢰도와 유지보수성을 낮추는 작성 방식이다.

RAG 문서는 Agent가 테스트 작성 시 Anti Pattern을 피하도록 명확한 기준을 제공해야 한다.

---

### [핵심]

대표 Anti Pattern:

- 내부 state 직접 테스트
- 구현 함수 호출 여부만 테스트
- 사용자 결과 검증 누락
- getByRole 대신 testId 남용
- 비동기 UI에 getBy 사용
- userEvent await 누락
- waitFor 남용
- 실제 API 호출
- mock response shape 불일치
- Provider 누락
- 테스트 간 Query Cache 공유
- mock reset 누락
- 전체 snapshot 의존
- CSS class 중심 테스트
- 테스트 이름 모호함
- 실제 token / secret 사용

---

### [실무]

나쁜 패턴:

```tsx
test("handleSubmit works", () => {
  expect(handleSubmit).toHaveBeenCalled();
});
```

개선 패턴:

```tsx
test("리뷰를 입력하고 등록하면 성공 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  mockCreateReviewSuccess();

  render(<ReviewForm />);

  await user.type(screen.getByLabelText("리뷰 내용"), "좋았어요");
  await user.click(screen.getByRole("button", { name: "등록" }));

  expect(await screen.findByText("리뷰가 등록되었습니다.")).toBeInTheDocument();
});
```

검수 기준:

```text
테스트 이름이 사용자 시나리오인가?
query가 사용자 인식 기준인가?
userEvent에 await가 있는가?
비동기 UI에 findBy를 사용하는가?
mock response가 실제 API shape와 맞는가?
결과 UI를 검증하는가?
```

---

### [FAQ]

Q. Frontend Testing 초보가 가장 많이 하는 실수는?
A. 사용자 결과 대신 내부 구현을 테스트하거나 비동기 UI를 기다리지 않고 검증하는 것이다.

Q. waitFor를 많이 쓰면 안 좋아?
A. 불필요한 waitFor는 테스트를 느리고 불명확하게 만든다. 화면 요소 등장은 findBy를 우선 사용한다.

Q. 실제 API를 호출하는 테스트는 왜 문제야?
A. 서버 상태, 네트워크, DB에 의존해 테스트가 불안정해지기 때문이다.

---

# 7. Strategy Checklist

## 7.1 Frontend Testing Strategy Checklist

### [개념]

Frontend Testing Strategy Checklist는 테스트 전략 문서를 검수할 때 사용하는 기준이다.

Agent는 테스트 작성 전 테스트 대상, 테스트 유형, 사용자 결과, mock 필요 여부를 먼저 판단해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 사용자 관점 테스트인가?
- [ ] 내부 구현 테스트를 피했는가?
- [ ] 테스트 유형이 적절한가?
- [ ] Unit / Component / Integration / E2E 구분이 명확한가?
- [ ] 핵심 사용자 흐름을 우선했는가?
- [ ] Loading / Error / Empty / Success 상태를 고려했는가?
- [ ] API Mock 필요 여부를 판단했는가?
- [ ] Router / Auth / Provider 필요 여부를 확인했는가?
- [ ] 접근성 기반 query를 우선 고려했는가?
- [ ] 테스트 이름이 사용자 시나리오 중심인가?
- [ ] 실제 secret / token / 운영 API를 사용하지 않았는가?
```

---

### [실무]

테스트 전략 수립 Flow:

```text
Feature 확인
→ 사용자 흐름 확인
→ 실패 영향 확인
→ 테스트 유형 선택
→ Mock 필요 여부 확인
→ Provider 필요 여부 확인
→ 주요 상태 정의
→ 테스트 케이스 작성
```

예:

```text
Login Page
→ Form 입력
→ Login API Mock
→ Success Redirect
→ Failure Error Message
→ Protected Route 연계
```

---

### [FAQ]

Q. 테스트 작성 전에 무엇을 먼저 정해야 해?
A. 테스트 대상, 사용자 흐름, 테스트 유형, mock 필요 여부, Provider 필요 여부를 먼저 정한다.

Q. Strategy Checklist의 핵심은 뭐야?
A. 사용자 관점 테스트, 적절한 테스트 유형 선택, 핵심 상태 UI 검증이다.

Q. 테스트 케이스가 너무 많으면 어떻게 줄여?
A. 핵심 사용자 흐름과 실패 영향이 큰 상태를 우선 남긴다.

---

# 8. Part01 Summary

## 8.1 Testing Strategy Final Rule

### [개념]

Frontend Testing Part01은 React Frontend 테스트의 전체 전략 기준을 정의한다.

이 Part의 목적은 Agent가 테스트 유형을 선택하고, 사용자 관점 테스트를 우선하며, 내부 구현 테스트를 피하도록 만드는 것이다.

---

### [핵심]

최종 기준:

- 사용자 행동 기반 테스트 우선
- 구현 세부사항 테스트 지양
- Unit / Component / Integration / E2E 구분
- 핵심 사용자 흐름 우선
- Form / API / Auth / Router 우선 검증
- Loading / Error / Empty / Success 상태 고려
- 실제 API 호출 지양
- 접근성 기반 query 고려
- 테스트 이름은 사용자 시나리오 중심
- 테스트 가치는 회귀 방지와 사용자 영향 기준으로 판단

---

### [실무]

Agent 판단 Flow:

```text
User Testing Request
→ Identify Feature
→ Identify User Behavior
→ Choose Test Type
→ Identify Required Provider
→ Identify Mock Target
→ Write Test Case
→ Assert User-visible Result
→ Review Anti Pattern
```

Part02 이후 연결:

```text
Part01 Testing Strategy
→ Part02 React Testing Library
→ Part03 Query Rules
→ Part04 User Event
→ Part05 Unit Test
→ Part06 Component Test
→ Part07 Form Testing
→ Part08 API Mocking
→ Part09 Loading Error Empty
→ Part10 Router Auth Testing
```

---

### [FAQ]

Q. Part01의 최종 목적은 뭐야?
A. Frontend Agent가 테스트 전략을 선택하고 사용자 관점 테스트 기준을 적용하게 만드는 것이다.

Q. Part01 다음에는 어떤 내용이 이어져야 해?
A. React Testing Library 철학, render / screen, query priority, userEvent 기준이 이어지는 것이 좋다.

Q. Frontend Testing의 핵심 한 줄은 뭐야?
A. 내부 구현이 아니라 사용자의 행동과 화면 결과를 테스트한다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Testing은 뭐야?
A. 사용자가 보는 화면, 입력, 클릭, API 상태, Routing, Auth 흐름이 정상 동작하는지 검증하는 테스트다.

Q. React 테스트는 무엇을 기준으로 작성해야 해?
A. 내부 구현보다 사용자 행동과 화면 결과를 기준으로 작성해야 한다.

Q. User Behavior Test는 뭐야?
A. 사용자가 실제로 입력, 클릭, 이동하는 흐름과 그 결과 UI를 검증하는 테스트다.

Q. Implementation Detail Test는 왜 피해야 해?
A. 내부 state, private function, className 같은 구현 세부사항은 변경에 취약해 테스트 유지보수성을 낮추기 때문이다.

Q. Frontend 테스트 종류는 뭐가 있어?
A. Unit Test, Component Test, Integration Test, E2E Test가 있다.

Q. Unit Test는 언제 써?
A. validation, formatter, mapper처럼 입력과 출력이 명확한 순수 함수 검증에 사용한다.

Q. Component Test는 언제 써?
A. 단일 React Component의 props, 사용자 입력, 클릭, 조건부 렌더링 결과를 검증할 때 사용한다.

Q. Integration Test는 언제 써?
A. 여러 Component, 상태 관리, Router, API Mock이 함께 동작하는 사용자 흐름을 검증할 때 사용한다.

Q. E2E Test는 언제 써?
A. 실제 브라우저에서 로그인, 회원가입, 결제 같은 핵심 사용자 여정을 검증할 때 사용한다.

Q. E2E Test만 있으면 충분해?
A. 아니다. E2E는 느리고 유지보수 비용이 커서 Unit, Component, Integration Test와 함께 사용해야 한다.

Q. Frontend 테스트는 뭐부터 작성해?
A. 로그인, Form 제출, API 상태, 오류 처리, 보호 Route처럼 실패 영향이 큰 핵심 사용자 흐름부터 작성한다.

Q. 모든 Component를 테스트해야 해?
A. 필수는 아니다. 재사용 빈도가 높거나 핵심 사용자 흐름에 포함되는 Component를 우선 테스트한다.

Q. Loading State도 테스트해야 해?
A. 핵심 화면에서는 Loading, Error, Empty, Success 상태를 함께 검증하는 것이 좋다.

Q. 실제 API를 호출해도 돼?
A. 일반 Frontend Component 또는 Integration Test에서는 권장하지 않는다. API 응답은 mock으로 제어한다.

Q. CSS className도 테스트해야 해?
A. 대부분 우선순위가 낮다. 사용자에게 보이는 역할, 텍스트, 상태, 동작을 먼저 테스트한다.

Q. data-testid는 언제 써?
A. role, label, text 같은 사용자 인식 query로 찾기 어려울 때 최후 수단으로 사용한다.

Q. 테스트 유형은 어떻게 선택해?
A. 순수 함수는 Unit, 단일 UI는 Component, 여러 상태 흐름은 Integration, 실제 브라우저 핵심 여정은 E2E로 선택한다.

Q. Page Component는 Component Test야 Integration Test야?
A. API, Router, Provider, 상태 흐름이 포함되면 Integration Test에 가깝다.

Q. 테스트 우선순위는 어떻게 정해?
A. 사용자 영향, 회귀 위험, 수동 확인 비용, 비즈니스 중요도를 기준으로 정한다.

Q. Frontend Testing Anti Pattern은 뭐가 있어?
A. 내부 state 직접 테스트, testId 남용, userEvent await 누락, 실제 API 호출, snapshot 남용, mock reset 누락 등이 있다.

Q. Frontend Testing 전략 체크리스트는 뭐야?
A. 사용자 관점, 테스트 유형, 핵심 흐름, API Mock, Provider, 상태 UI, 접근성 query, 보안 데이터를 확인하는 기준이다.

Q. Part01 Testing Strategy의 최종 목표는 뭐야?
A. Frontend Agent가 테스트 유형을 올바르게 선택하고 사용자 행동 기반 테스트를 작성하게 만드는 것이다.
