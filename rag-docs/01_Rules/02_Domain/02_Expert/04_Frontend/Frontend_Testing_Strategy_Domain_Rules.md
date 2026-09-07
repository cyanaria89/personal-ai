# Frontend Testing Strategy Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Testing Strategy Domain 목적

### [개념]

Frontend Testing Strategy Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent / QA Agent용 RAG 문서 제작 규칙이다.

Frontend Testing Strategy는 프론트엔드 애플리케이션의 UI, Component, Hook, Form, API 연동, Routing, 인증 흐름, 접근성, 성능 회귀, E2E 사용자 Flow를 검증하기 위한 테스트 체계이다.

목적:

- 프론트엔드 테스트 전략 설계 지원
- Unit / Component / Integration / E2E 테스트 구분 지원
- React / Next.js 테스트 기준 제공
- Testing Library 기반 사용자 중심 테스트 지원
- Mocking 전략 판단 지원
- API / Server State 테스트 지원
- Form / Validation 테스트 지원
- Authentication Flow 테스트 지원
- Accessibility 테스트 지원
- Visual Regression 테스트 지원
- CI 테스트 파이프라인 설계 지원
- Flaky Test 방지 기준 제공
- Frontend 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Testing Pyramid
2. User-centric Testing
3. Unit Test
4. Component Test
5. Integration Test
6. E2E Test
7. Accessibility Test
8. Visual Regression Test
9. API Mocking Strategy
10. Server State Testing
11. Form Testing
12. Authentication Flow Testing
13. Routing Testing
14. Next.js App Router Testing
15. Design System Testing
16. Performance Regression Testing
17. CI Test Pipeline
18. Test Data / Fixture
19. Flaky Test Prevention
20. Code Review Criteria

---

### [실무]

2026 실무 기준:

- React / TypeScript / Next.js App Router 기준 예제 우선
- 사용자 행동 중심 테스트 우선
- 구현 세부사항보다 화면 결과와 접근 가능한 역할 기준 검증
- Unit Test, Component Test, Integration Test, E2E Test의 목적을 분리
- 모든 테스트를 E2E로 해결하지 않음
- 모든 테스트를 snapshot으로 해결하지 않음
- Mocking은 필요한 경계에서만 사용
- API Mocking은 MSW 같은 네트워크 레벨 mocking 우선 검토
- Form / Auth / Routing / Error / Loading 상태를 테스트 범위에 포함
- Design System 컴포넌트는 Accessibility / Visual Regression 테스트 포함
- Next.js Server Component / Client Component 테스트 경계 구분
- CI에서 빠른 테스트와 느린 테스트를 분리
- Flaky Test는 실패 원인을 기록하고 안정화 기준을 포함
- Agent가 테스트 코드 생성과 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Testing Strategy 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 프로젝트에서 Unit, Component, Integration, E2E, Accessibility, Visual Regression 테스트 전략을 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. 프론트엔드 테스트는 무엇을 기준으로 작성해야 하나?

A.
사용자가 실제로 보는 UI와 수행하는 행동을 기준으로 작성해야 한다. 구현 세부사항보다 역할, 텍스트, 상태 변화, API 결과, 사용자 Flow를 검증한다.

Q. 모든 테스트를 E2E로 작성하면 안 되나?

A.
권장하지 않는다. E2E는 느리고 불안정해질 수 있으므로 핵심 사용자 Flow에 집중하고, 나머지는 Component / Integration Test로 보완한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Testing Strategy Domain은 프론트엔드 코드와 사용자 경험을 안정적으로 검증하기 위한 테스트 유형, 도구, 원칙, 자동화 기준을 포함한다.

---

### [핵심]

포함 범위:

- Frontend Testing
- Testing Strategy
- Testing Pyramid
- Unit Test
- Component Test
- Integration Test
- E2E Test
- Acceptance Test
- Regression Test
- Accessibility Test
- Visual Regression Test
- Performance Regression Test
- Snapshot Test
- Contract Test
- React Testing
- Next.js Testing
- App Router Testing
- Hook Testing
- Form Testing
- Routing Testing
- Auth Flow Testing
- Error Boundary Testing
- Suspense / Loading Testing
- API Mocking
- MSW
- Mock Function
- Test Fixture
- Test Data Builder
- User Event
- Query Priority
- Jest
- Vitest
- React Testing Library
- Playwright
- Cypress
- Storybook Test
- CI Test Pipeline
- Coverage
- Flaky Test
- Test Isolation
- Test Environment
- jsdom
- Browser Test
- Code Review Checklist

---

### [실무]

제외 범위:

- Backend Unit Test 심화
- Database Test 심화
- Load Test 심화
- Security Penetration Test 심화
- Mobile Native App Test 심화
- Browser Engine 내부 테스트 심화
- Manual QA 전체 프로세스 심화
- 테스트 도구별 CLI 전체 문법
- DevOps Pipeline 심화 전체

단, 프론트엔드 테스트 전략에 필요한 수준의 API Mocking, CI, Accessibility, Performance, Security, Observability 연계 지식은 포함 가능하다.

---

### [FAQ]

Q. Frontend Testing Strategy 문서에 Backend 테스트도 포함해야 하나?

A.
심화는 제외한다. 단, API Contract, Mocking, E2E Flow처럼 프론트엔드 테스트와 연결되는 부분은 포함할 수 있다.

Q. 테스트 도구 사용법 전체를 포함해야 하나?

A.
아니다. 도구별 전체 문법보다 어떤 테스트를 어떤 도구와 전략으로 검증할지에 집중한다.

Q. Visual Regression Test도 포함해야 하나?

A.
포함한다. 특히 Design System, 공통 UI, 레이아웃, 테마 변경 검증에 중요하다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Testing Strategy RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Frontend Testing Strategy 문서는 테스트 대상과 범위 판단이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Requirement → Test Scope → Test Type → Mock Boundary → Assertion → CI
- `[Comparison]`: Unit vs Component vs Integration vs E2E
- `[Best Practice]`: User-centric Query, Minimal Mocking, Stable Assertion
- `[Troubleshooting]`: Flaky Test, Mock 누락, 비동기 테스트 실패
- `[Checklist]`: 배포 전 테스트 전략 검수

---

### [FAQ]

Q. Frontend Testing 문서에 Comparison이 필요한 이유는?

A.
같은 기능도 Unit, Component, Integration, E2E 중 어디서 검증할지 판단해야 하므로 비교 기준이 필요하다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Testing Principles Rules

## 4.1 프론트엔드 테스트 원칙

### [개념]

Frontend Testing 원칙은 사용자의 행동과 화면 결과를 중심으로 신뢰할 수 있는 테스트를 작성하는 기준이다.

---

### [핵심]

필수 원칙:

- Test User Behavior
- Test Public Contract
- Avoid Implementation Detail
- Prefer Accessible Query
- Test Critical Flow
- Mock External Boundary
- Keep Tests Deterministic
- Test Error and Loading State
- Test Accessibility
- Avoid Snapshot Abuse
- Keep E2E Focused
- Fast Feedback
- Stable CI
- Clear Failure Message
- Maintainable Test

기본 Flow:

```text
기능 요구사항 확인
→ 사용자 행동 정의
→ 테스트 유형 선택
→ Mock 경계 결정
→ 화면 결과 검증
→ Error / Loading 상태 추가
→ CI에서 반복 실행
```

---

### [실무]

작성 기준:

- “컴포넌트 내부 state가 바뀌었다”보다 “사용자에게 결과가 보인다”를 검증
- class name, 내부 함수 호출, private state 직접 검증 지양
- `getByRole`, `getByLabelText`, `getByText` 같은 접근성 기반 query 우선
- 비동기 UI는 `findBy...`, `waitFor` 사용 기준 포함
- 실패 시 원인을 알 수 있는 assertion 작성
- 테스트 이름은 사용자 시나리오 중심
- Mock은 외부 API, 시간, 브라우저 API, 라우터 등 경계에 제한
- 테스트 데이터는 fixture / builder로 관리
- 중요한 bug는 regression test로 남김
- 테스트가 너무 복잡하면 컴포넌트 책임 분리 검토

---

### [FAQ]

Q. 프론트엔드 테스트에서 가장 중요한 원칙은?

A.
구현 세부사항이 아니라 사용자의 행동과 화면 결과를 검증하는 것이다.

Q. className이나 state를 직접 검증해도 되나?

A.
가능하면 피한다. 사용자가 볼 수 있는 텍스트, 역할, 상태, 접근성 속성, 화면 변화를 검증하는 것이 좋다.

Q. 테스트가 복잡해지면 어떻게 해야 하나?

A.
컴포넌트 책임이 너무 크거나 테스트 범위가 잘못되었을 수 있으므로 구조를 분리하거나 테스트 유형을 재선택한다.

---

# 5. Testing Pyramid Rules

## 5.1 테스트 피라미드

### [개념]

Testing Pyramid는 빠르고 작은 테스트를 많이 두고, 느리고 큰 E2E 테스트는 핵심 Flow 중심으로 제한하는 전략이다.

---

### [핵심]

테스트 계층:

| 계층               | 목적                               | 특징                 |
| ------------------ | ---------------------------------- | -------------------- |
| Unit Test          | 순수 함수 / Hook / 유틸 검증       | 빠름, 고립           |
| Component Test     | UI 컴포넌트 동작 검증              | 사용자 이벤트 중심   |
| Integration Test   | 여러 컴포넌트 / API Mock 연동 검증 | 기능 단위            |
| E2E Test           | 실제 브라우저 사용자 Flow 검증     | 느림, 핵심 Flow      |
| Visual Test        | UI 시각 회귀 검증                  | Design System에 유용 |
| Accessibility Test | 접근성 기본 오류 검증              | 자동 + 수동 병행     |

---

### [실무]

전략 기준:

- 유틸 / 순수 로직은 Unit Test
- Button / Input / Modal 같은 UI는 Component Test
- 검색 / 폼 제출 / 목록 로딩은 Integration Test
- 로그인 / 결제 / 회원가입 / 핵심 구매 Flow는 E2E Test
- Design System은 Component + Accessibility + Visual Test
- 모든 테스트를 Unit으로만 작성하지 않기
- 모든 테스트를 E2E로만 작성하지 않기
- 테스트 비용과 신뢰도의 균형 유지
- 실패 위치를 빠르게 알 수 있도록 계층 분리

---

### [FAQ]

Q. Testing Pyramid는 왜 필요한가?

A.
빠른 피드백과 높은 신뢰도를 균형 있게 얻기 위해 필요하다.

Q. E2E 테스트가 가장 실제와 가까운데 많이 쓰면 안 되나?

A.
E2E는 느리고 환경 의존성이 커서 핵심 Flow 중심으로 제한하는 것이 좋다.

Q. Component Test와 Integration Test 차이는?

A.
Component Test는 개별 UI 컴포넌트 동작 중심이고, Integration Test는 여러 컴포넌트와 API Mock을 포함한 기능 흐름 중심이다.

---

# 6. Unit Test Rules

## 6.1 Unit Test 기준

### [개념]

Unit Test는 작은 단위의 순수 함수, 유틸, Hook, 포맷터, validator, reducer 같은 로직을 빠르게 검증하는 테스트이다.

---

### [핵심]

적합 대상:

- Utility Function
- Formatter
- Parser
- Validator
- Mapper
- Reducer
- Custom Hook
- Pure Business Logic
- Date Calculation
- Permission Helper
- URL Helper
- State Machine
- Schema Validation

---

### [실무]

작성 기준:

- 입력과 출력이 명확한 로직 우선
- DOM이 필요 없는 로직은 순수 Unit Test
- 날짜 / 시간 / random 값은 고정
- 외부 API 호출은 mock
- edge case 포함
- 실패 케이스 포함
- permission helper는 role / 상태별 case 포함
- validator는 valid / invalid case 포함
- 테스트 이름은 조건과 기대 결과를 명확히 작성

예시:

```ts
describe("formatCurrency", () => {
  it("formats number as KRW currency text", () => {
    expect(formatCurrency(12000)).toBe("12,000원");
  });
});
```

---

### [FAQ]

Q. Unit Test는 무엇을 테스트하나?

A.
순수 함수, 유틸, validator, formatter, reducer, custom hook처럼 작은 로직 단위를 테스트한다.

Q. UI 컴포넌트도 Unit Test로 테스트하나?

A.
UI 컴포넌트는 보통 Component Test가 더 적합하다. 단순 로직은 별도 함수로 분리해 Unit Test할 수 있다.

Q. Unit Test에서 API를 실제 호출해도 되나?

A.
권장하지 않는다. 외부 API는 mock하고 API 연동은 Integration 또는 E2E에서 검증한다.

---

# 7. Component Test Rules

## 7.1 Component Test 기준

### [개념]

Component Test는 UI 컴포넌트를 렌더링하고 사용자의 상호작용에 따른 화면 변화를 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Render Result
- Text
- Accessible Role
- Label
- Button State
- Form Input
- Click Event
- Keyboard Interaction
- Loading State
- Error State
- Empty State
- Disabled State
- Validation Message
- Callback Invocation
- ARIA Attribute

---

### [실무]

작성 기준:

- 사용자가 보는 결과 기준으로 assertion
- `getByRole` 우선 사용
- 버튼 클릭은 `userEvent.click`
- 입력은 `userEvent.type`
- 비활성 상태는 disabled 여부 검증
- error message는 화면 표시와 접근성 연결 검증
- loading / empty / error 상태를 별도 테스트
- props 조합별 중요 case만 테스트
- 스타일 세부값보다 상태 / 역할 / 접근성 검증 우선
- snapshot 남용 금지

예시:

```tsx
it("calls onSubmit when user fills form and submits", async () => {
  render(<LoginForm onSubmit={onSubmit} />);

  await userEvent.type(screen.getByLabelText("이메일"), "test@example.com");
  await userEvent.type(screen.getByLabelText("비밀번호"), "password");
  await userEvent.click(screen.getByRole("button", { name: "로그인" }));

  expect(onSubmit).toHaveBeenCalled();
});
```

---

### [FAQ]

Q. Component Test는 무엇을 검증하나?

A.
컴포넌트가 사용자에게 어떻게 보이고 사용자의 행동에 어떻게 반응하는지 검증한다.

Q. Component Test에서 내부 state를 확인해야 하나?

A.
가능하면 확인하지 않는다. state 변화로 인해 사용자에게 보이는 결과를 검증한다.

Q. Snapshot Test로 Component Test를 대체해도 되나?

A.
권장하지 않는다. Snapshot은 구조 변화 감지에는 유용할 수 있지만 사용자 행동 검증을 대체하지 못한다.

---

# 8. Integration Test Rules

## 8.1 Integration Test 기준

### [개념]

Integration Test는 여러 컴포넌트, Hook, 상태 관리, API Mock, Router가 함께 동작하는 기능 단위 흐름을 검증하는 테스트이다.

---

### [핵심]

적합 대상:

- Search Flow
- Form Submit Flow
- List Fetching
- Filter / Sort
- Pagination
- Modal Interaction
- Auth State UI
- Error Retry
- Server State Update
- Cache Invalidation
- Route Navigation
- Feature Component Integration

---

### [실무]

작성 기준:

- 실제 사용자 Flow 중심
- API는 네트워크 레벨 mock 사용 권장
- 페이지 또는 Feature 단위로 렌더링
- loading → success → error 상태 검증
- Mutation 후 UI 갱신 검증
- Router와 URL State 검증
- Provider / Query Client / Theme Provider 등 테스트 wrapper 구성
- 지나친 mock으로 실제 흐름을 깨지 않기
- 실패 시 어느 경계에서 실패했는지 알 수 있게 구성
- E2E로 올릴지 Integration으로 충분한지 판단

예시 Flow:

```text
검색어 입력
→ 검색 버튼 클릭
→ API Mock 응답
→ 목록 표시
→ 결과 없음 상태 표시
→ API 실패 시 에러 메시지 표시
```

---

### [FAQ]

Q. Integration Test는 언제 필요한가?

A.
여러 컴포넌트와 API 응답, 상태, 라우팅이 함께 동작하는 기능 흐름을 검증할 때 필요하다.

Q. Integration Test에서 API는 실제 서버를 호출하나?

A.
일반적으로 mock한다. 실제 서버까지 포함하는 검증은 E2E나 별도 환경에서 수행한다.

Q. Component Test와 Integration Test의 경계는?

A.
Component Test는 개별 컴포넌트 동작이고, Integration Test는 기능 단위 사용자 흐름이다.

---

# 9. E2E Test Rules

## 9.1 E2E Test 기준

### [개념]

E2E Test는 실제 브라우저 환경에서 사용자의 핵심 Flow가 처음부터 끝까지 정상 동작하는지 검증하는 테스트이다.

---

### [핵심]

적합 대상:

- Login Flow
- Signup Flow
- Logout Flow
- Checkout Flow
- Payment Flow
- Search Flow
- Create / Edit / Delete Flow
- File Upload Flow
- Admin Approval Flow
- Critical Navigation Flow
- Permission Flow
- Error Recovery Flow

---

### [실무]

작성 기준:

- 핵심 사용자 Flow 중심으로 제한
- 실제 브라우저에서 실행
- 테스트 계정과 테스트 데이터 준비
- 외부 결제 / 이메일 / 지도 등은 테스트 모드 또는 mock 전략 사용
- selector는 접근성 role / label 우선
- 불안정한 sleep 사용 금지
- 명시적 상태 대기 사용
- 테스트 간 독립성 유지
- 실패 시 screenshot / video / trace 수집
- CI에서는 shard / parallel 검토
- 배포 전 smoke test로 핵심 Flow 검증

예시 Flow:

```text
사용자가 로그인한다
→ 검색 페이지로 이동한다
→ 키워드를 입력한다
→ 결과 상세로 이동한다
→ 찜 버튼을 누른다
→ 마이페이지에서 찜 목록을 확인한다
```

---

### [FAQ]

Q. E2E Test는 무엇을 검증하나?

A.
실제 브라우저에서 사용자가 수행하는 핵심 Flow가 전체 시스템과 함께 동작하는지 검증한다.

Q. E2E Test를 많이 만들면 좋은가?

A.
아니다. 느리고 flaky해질 수 있으므로 핵심 Flow와 smoke test 중심으로 작성한다.

Q. E2E Test에서 sleep을 써도 되나?

A.
권장하지 않는다. 특정 UI 상태나 네트워크 응답을 기다리는 명시적 wait를 사용해야 한다.

---

# 10. Accessibility Test Rules

## 10.1 Accessibility Testing 기준

### [개념]

Accessibility Test는 키보드 사용자, 스크린 리더 사용자, 저시력 사용자 등 다양한 사용자가 UI를 이용할 수 있는지 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Semantic HTML
- Accessible Name
- Role
- Label
- Keyboard Navigation
- Focus Management
- Focus Visible
- ARIA Attribute
- Color Contrast
- Error Message Association
- Dialog Focus Trap
- Live Region
- Touch Target
- Reduced Motion

---

### [실무]

작성 기준:

- 자동 접근성 테스트 도구 사용
- `getByRole`, `getByLabelText` 기반 테스트로 접근성 품질 간접 검증
- Button / Link 역할 구분 확인
- Input과 Label 연결 확인
- Error message와 field 연결 확인
- Modal / Dialog focus trap 검증
- Keyboard navigation 수동 / 자동 검증
- Color Contrast는 도구 검증
- 자동 테스트가 모든 접근성 문제를 잡지는 못함
- Design System 컴포넌트는 접근성 테스트 필수

예시:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeEnabled();
expect(screen.getByLabelText("이메일")).toBeInTheDocument();
```

---

### [FAQ]

Q. Accessibility Test는 왜 필요한가?

A.
공통 UI와 핵심 Flow가 키보드, 스크린 리더, 다양한 사용자 환경에서 사용할 수 있는지 확인하기 위해 필요하다.

Q. 자동 접근성 테스트만으로 충분한가?

A.
아니다. 자동 도구는 일부 문제만 잡으므로 키보드 탐색과 스크린 리더 흐름은 수동 검증도 필요하다.

Q. Testing Library의 role query가 접근성에 도움 되나?

A.
그렇다. 접근 가능한 역할과 이름을 기준으로 요소를 찾기 때문에 접근성 품질을 간접적으로 높인다.

---

# 11. Visual Regression Test Rules

## 11.1 Visual Regression Testing 기준

### [개념]

Visual Regression Test는 UI가 의도치 않게 깨지거나 달라졌는지 screenshot 비교로 검증하는 테스트이다.

---

### [핵심]

적합 대상:

- Design System Component
- Button / Input / Modal
- Theme
- Dark Mode
- Responsive Layout
- Marketing Page
- Critical Layout
- Chart / Dashboard
- Empty / Loading / Error State
- Cross-browser UI
- Typography / Spacing

---

### [실무]

작성 기준:

- Design System 컴포넌트 상태별 screenshot
- Light / Dark Theme 비교
- 주요 breakpoint별 비교
- Hover / Focus / Disabled 상태 포함 가능
- 동적 데이터는 fixture로 고정
- 날짜 / 시간 / animation은 고정 또는 비활성화
- 변경 승인 workflow 필요
- 시각 테스트는 의도된 변경과 회귀를 구분
- E2E screenshot과 Storybook screenshot 전략 분리 가능
- 너무 많은 screenshot은 유지 비용 증가

주의:

- Visual Test는 기능 동작 검증을 대체하지 않음
- 폰트 / 브라우저 / OS 차이로 flaky할 수 있음
- 애니메이션과 비동기 로딩 상태를 안정화해야 함
- screenshot diff는 코드 리뷰와 함께 판단

---

### [FAQ]

Q. Visual Regression Test는 언제 필요한가?

A.
Design System, 공통 UI, 레이아웃, 테마, 반응형 UI가 의도치 않게 깨지는 것을 막고 싶을 때 필요하다.

Q. Visual Test가 Component Test를 대체하나?

A.
아니다. Visual Test는 시각적 회귀 검증이고 Component Test는 사용자 상호작용과 상태를 검증한다.

Q. Visual Test가 flaky한 이유는?

A.
폰트 렌더링, 애니메이션, 동적 데이터, 브라우저 차이, 비동기 로딩 때문에 흔들릴 수 있다.

---

# 12. Snapshot Test Rules

## 12.1 Snapshot Test 기준

### [개념]

Snapshot Test는 렌더링 결과나 데이터 구조를 저장해 이후 변경 여부를 비교하는 테스트이다.

Snapshot은 구조 변화 감지에는 유용하지만 사용자 행동 검증을 대체할 수 없다.

---

### [핵심]

적합 대상:

- Stable Data Structure
- Generated Output
- Simple Serialized Result
- UI 구조 변경 감지
- Design Token Output
- Config Output

부적합 대상:

- 복잡한 UI 전체
- 자주 바뀌는 Component
- 동적 데이터 많은 화면
- 사용자 행동 검증
- 접근성 검증
- 비즈니스 Flow 검증

---

### [실무]

작성 기준:

- snapshot 크기는 작게 유지
- 변경 시 반드시 diff 확인
- snapshot update를 무의식적으로 실행하지 않기
- UI 전체 snapshot 남용 금지
- 사용자 행동 테스트를 snapshot으로 대체 금지
- 의미 있는 assertion과 함께 사용
- 동적 값은 고정
- snapshot이 너무 자주 깨지면 테스트 가치 재검토

---

### [FAQ]

Q. Snapshot Test는 언제 쓰면 좋나?

A.
작고 안정적인 출력 구조나 design token output처럼 변경 감지가 필요한 경우에 적합하다.

Q. Snapshot Test만 있으면 충분한가?

A.
아니다. 사용자 행동, 접근성, error state, API flow는 별도 테스트가 필요하다.

Q. Snapshot이 자주 깨지면 어떻게 해야 하나?

A.
테스트 대상이 너무 불안정하거나 snapshot 범위가 너무 큰지 확인하고 더 명시적인 assertion으로 바꾼다.

---

# 13. API Mocking Strategy Rules

## 13.1 API Mocking 전략

### [개념]

API Mocking Strategy는 테스트에서 실제 Backend에 의존하지 않고 API 응답을 안정적으로 제어하는 기준이다.

---

### [핵심]

Mocking 대상:

- REST API
- GraphQL API
- Auth API
- Search API
- Upload API
- Payment Test API
- Error Response
- Timeout
- Network Failure
- Empty Response
- Pagination Response

Mocking 방식:

- Mock Function
- Module Mock
- Network-level Mock
- MSW
- Playwright Route Mock
- Fixture Server
- Contract Mock

---

### [실무]

작성 기준:

- Component / Integration Test는 네트워크 레벨 mock 우선 검토
- API client 내부 구현을 과도하게 mock하지 않기
- success / error / loading / empty 상태 모두 준비
- HTTP status code와 response body를 실제 API와 맞춤
- fixture를 API Contract와 동기화
- E2E는 테스트 환경 Backend 사용 또는 route mock 선택
- 인증 API는 test user / fake session 전략 명확화
- Mock이 실제 API와 어긋나지 않도록 contract test 검토
- 불필요한 deep mock 금지

예시:

```ts
const handlers = [
  http.get("/api/posts", () => {
    return HttpResponse.json([{ id: 1, title: "첫 번째 글" }]);
  }),
];
```

---

### [FAQ]

Q. API Mocking은 왜 필요한가?

A.
테스트를 빠르고 안정적으로 만들고 success / error / empty 같은 다양한 응답 상태를 제어하기 위해 필요하다.

Q. API Client 함수를 직접 mock하면 안 되나?

A.
가능하지만 너무 깊게 mock하면 실제 네트워크 흐름과 멀어질 수 있다. Integration Test에서는 네트워크 레벨 mock이 더 자연스러울 때가 많다.

Q. Mock 데이터가 실제 API와 달라지면 어떻게 하나?

A.
API Contract, fixture 관리, contract test, schema validation으로 동기화해야 한다.

---

# 14. Server State Testing Rules

## 14.1 서버 상태 테스트

### [개념]

Server State Testing은 API에서 가져온 데이터, cache, stale state, loading, error, refetch, mutation, invalidation을 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Loading State
- Success State
- Error State
- Empty State
- Refetch
- Mutation
- Optimistic Update
- Cache Invalidation
- Stale Data
- Pagination
- Infinite Query
- Retry
- Request Deduplication
- Background Refetch

---

### [실무]

작성 기준:

- Query Client / Provider 테스트 wrapper 구성
- 테스트마다 cache 초기화
- loading / success / error 상태 검증
- mutation 후 화면 갱신 검증
- optimistic update는 성공 / 실패 rollback 검증
- pagination next page 동작 검증
- retry 동작은 필요 시 제한
- 테스트 간 서버 상태 cache 공유 금지
- API 응답은 MSW 등으로 제어
- stale time / refetch 설정에 따른 테스트 안정성 확인

---

### [FAQ]

Q. Server State 테스트에서 가장 중요한 것은?

A.
loading, success, error, empty, mutation 후 invalidation과 화면 갱신을 검증하는 것이다.

Q. 테스트마다 Query Cache를 초기화해야 하나?

A.
그렇다. 테스트 간 상태가 공유되면 결과가 불안정해질 수 있다.

Q. Optimistic Update는 어떻게 테스트하나?

A.
성공 시 즉시 UI 반영과 서버 확정 후 상태, 실패 시 rollback과 에러 표시를 검증한다.

---

# 15. Form Testing Rules

## 15.1 Form / Validation 테스트

### [개념]

Form Testing은 사용자의 입력, 검증, 에러 메시지, 제출, 서버 오류, 접근성 연결을 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Input Typing
- Select / Checkbox / Radio
- Required Field
- Validation Message
- Submit Button
- Disabled State
- Pending State
- Server Validation Error
- Field Error
- Form Error
- Success Message
- Reset
- Accessibility Association

---

### [실무]

작성 기준:

- `userEvent.type`, `userEvent.click` 사용
- label 기반 input query
- required field error 검증
- 잘못된 형식 validation 검증
- submit 중 버튼 disabled / loading 상태 검증
- 서버 validation error 표시 검증
- field error와 input의 접근성 연결 확인
- 성공 후 redirect / reset / toast 검증
- Form 전체 error와 field error 구분
- 비밀번호 / 민감 데이터는 테스트 로그에 노출 주의

예시 Flow:

```text
빈 값 제출
→ 필수 입력 에러 표시
→ 올바른 값 입력
→ 제출 버튼 클릭
→ pending 상태 표시
→ 성공 메시지 표시
```

---

### [FAQ]

Q. Form Test는 무엇을 검증해야 하나?

A.
입력, 검증 메시지, 제출, pending 상태, 서버 오류, 성공 상태, 접근성 연결을 검증해야 한다.

Q. Placeholder로 input을 찾아도 되나?

A.
가능은 하지만 label 기반 query가 더 좋다. Label이 없으면 접근성 문제일 가능성이 있다.

Q. 서버 validation error도 테스트해야 하나?

A.
해야 한다. 클라이언트 validation을 통과해도 서버에서 거절될 수 있기 때문이다.

---

# 16. Authentication Testing Rules

## 16.1 인증 / 권한 Flow 테스트

### [개념]

Authentication Testing은 로그인, 로그아웃, 세션 만료, 권한 없음, 보호 route, current user 상태를 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Login Success
- Login Failure
- Logout
- Session Check
- Session Expired
- Current User
- Protected Route
- Redirect
- 401 Handling
- 403 Handling
- Role-based UI
- Permission-based UI
- Token Refresh
- Multi-tab Logout

---

### [실무]

작성 기준:

- 로그인 성공 / 실패 테스트
- 인증되지 않은 사용자의 protected route 접근 테스트
- 401 발생 시 로그인 화면 또는 세션 만료 처리 검증
- 403 발생 시 권한 없음 화면 검증
- role별 메뉴 / 버튼 표시 테스트
- UI 권한 테스트와 API 권한 테스트 구분
- refresh 실패 시 logout 처리 검증
- current user loading 상태 검증
- E2E에서는 테스트 계정 사용
- 보안 판단은 서버 테스트와 함께 검증

주의:

- 버튼 숨김만 테스트하고 API 권한 검증을 생략하지 않기
- JWT payload decode만 신뢰하는 테스트 금지
- 실제 token을 테스트 로그에 남기지 않기
- 권한 상태 mock과 실제 서버 권한이 어긋나지 않게 관리

---

### [FAQ]

Q. Auth Flow 테스트는 무엇을 포함해야 하나?

A.
로그인 성공 / 실패, 로그아웃, 세션 만료, protected route, 401 / 403 처리, role-based UI를 포함해야 한다.

Q. 권한 테스트는 프론트엔드만 하면 충분한가?

A.
아니다. 프론트엔드 UI 테스트와 서버 API 권한 테스트가 함께 필요하다.

Q. 401과 403 테스트는 왜 구분해야 하나?

A.
401은 인증 필요, 403은 권한 없음 상태이므로 사용자 안내와 처리 Flow가 다르다.

---

# 17. Routing Testing Rules

## 17.1 Routing / Navigation 테스트

### [개념]

Routing Testing은 사용자가 링크, 버튼, 브라우저 뒤로가기, URL State, query parameter를 통해 올바르게 이동하는지 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Link Navigation
- Programmatic Navigation
- Redirect
- Protected Route
- Not Found
- Search Params
- Query String
- URL State
- Dynamic Route
- Back / Forward
- Tab State
- Pagination URL
- Filter URL
- Route Loading
- Route Error

---

### [실무]

작성 기준:

- 링크는 accessible name으로 찾음
- 클릭 후 URL / 화면 변화 검증
- 검색 / 필터 상태가 URL에 반영되는지 검증
- URL 직접 접근 시 상태 복원 검증
- 잘못된 dynamic route는 not found 검증
- protected route redirect 검증
- route loading / error UI 검증
- Next.js App Router에서는 server / client navigation 경계 고려
- E2E에서 실제 브라우저 history 동작 검증 가능

---

### [FAQ]

Q. Routing Test는 왜 필요한가?

A.
사용자가 링크와 URL을 통해 이동하는 흐름, 상태 복원, 보호 route 처리가 실제 UX에 큰 영향을 주기 때문이다.

Q. 검색 필터 상태를 URL에 넣으면 테스트해야 하나?

A.
그렇다. 새로고침, 공유 링크, 뒤로가기에서 상태가 복원되는지 확인해야 한다.

Q. Not Found도 테스트해야 하나?

A.
해야 한다. 잘못된 URL이나 삭제된 데이터 접근 시 안전한 fallback을 제공해야 한다.

---

# 18. Next.js App Router Testing Rules

## 18.1 Next.js App Router 테스트 기준

### [개념]

Next.js App Router Testing은 Server Component, Client Component, Route Handler, Server Action, `loading.tsx`, `error.tsx`, `not-found.tsx`, metadata, cache / revalidation 흐름을 테스트하는 기준이다.

---

### [핵심]

검증 대상:

- Server Component Rendering
- Client Component Interaction
- Route Handler
- Server Action
- `loading.tsx`
- `error.tsx`
- `not-found.tsx`
- `generateMetadata`
- Dynamic Route
- Search Params
- Revalidation
- Redirect
- Middleware / Proxy
- Auth Guard
- App Router Navigation

---

### [실무]

작성 기준:

- Client Component는 Component Test 가능
- Server Component는 integration / E2E / framework-aware test 전략 검토
- Server Action은 서버 함수처럼 입력 검증 / 권한 검증 테스트
- Route Handler는 API endpoint 테스트처럼 검증
- `error.tsx` fallback과 reset 동작 검증
- `not-found.tsx` 표시 검증
- `loading.tsx`는 E2E 또는 integration에서 검증
- redirect / notFound / revalidate 동작은 framework context 고려
- App Router navigation은 E2E에서 신뢰도 높게 검증
- Server / Client Boundary를 테스트 설계에 반영

주의:

- Server Component를 일반 React Component처럼 무리하게 테스트하지 않기
- framework 내부 동작을 지나치게 mock하지 않기
- Server Action 권한 검증 누락 금지
- Cache / Revalidation은 실제 환경과 차이가 클 수 있어 E2E 또는 integration 전략 필요

---

### [FAQ]

Q. Next.js App Router 테스트에서 가장 어려운 점은?

A.
Server Component, Server Action, Route Handler, Cache / Revalidation처럼 framework runtime과 연결된 부분의 테스트 경계를 정하는 것이다.

Q. Server Component도 Component Test로 테스트하나?

A.
단순 렌더링은 가능할 수 있지만 실제 데이터 fetching과 routing context가 있으면 integration 또는 E2E가 더 적합할 수 있다.

Q. Server Action은 어떻게 테스트하나?

A.
입력 검증, 인증 / 권한 검증, mutation 결과, revalidation 호출 여부를 서버 로직 테스트로 검증한다.

---

# 19. Design System Testing Rules

## 19.1 Design System 테스트 기준

### [개념]

Design System Testing은 공통 UI 컴포넌트가 다양한 variant, size, state, theme, accessibility, interaction에서 안정적으로 동작하는지 검증하는 전략이다.

---

### [핵심]

검증 대상:

- Variant
- Size
- State
- Disabled
- Loading
- Focus
- Hover
- Active
- Error
- Theme
- Dark Mode
- Keyboard Interaction
- ARIA
- Visual Regression
- Storybook Story
- Component API
- Composition

---

### [실무]

작성 기준:

- Button / Input / Modal / FormField 우선 테스트
- variant / size / state 조합 중 핵심 case 검증
- Icon-only Button accessible name 검증
- Input label / error association 검증
- Modal focus trap / escape / focus return 검증
- Theme / Dark Mode visual test 검토
- Storybook interaction test 활용 가능
- public component API 기준 테스트
- CSS class 세부값보다 사용자 상태와 접근성 검증
- Design System 변경은 visual regression과 함께 리뷰

---

### [FAQ]

Q. Design System 컴포넌트는 무엇을 테스트해야 하나?

A.
variant, state, accessibility, keyboard interaction, theme, visual regression, public API를 테스트해야 한다.

Q. Button 컴포넌트 테스트에서 중요한 것은?

A.
disabled, loading, click, type, variant의 핵심 상태와 accessible name을 검증하는 것이다.

Q. Modal 테스트에서 중요한 것은?

A.
focus trap, escape key, focus return, role, label, backdrop 동작을 검증하는 것이다.

---

# 20. Error and Loading State Testing Rules

## 20.1 Error / Loading / Empty 상태 테스트

### [개념]

Error and Loading State Testing은 성공 상태뿐 아니라 로딩, 실패, 빈 데이터, 재시도, 권한 없음, 네트워크 오류를 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Loading State
- Skeleton
- Spinner
- Pending State
- Empty State
- Error State
- Retry
- Offline
- Timeout
- 401 Error
- 403 Error
- 404 Error
- 500 Error
- Validation Error
- Toast / Alert
- Error Boundary Fallback

---

### [실무]

작성 기준:

- 성공 상태만 테스트하지 않기
- API loading 상태 검증
- 빈 목록 상태 검증
- API 실패 시 error message 검증
- retry 버튼 동작 검증
- 401 / 403 / 404 / 500 처리 구분
- Form validation error와 API error 구분
- Error Boundary fallback 검증
- Skeleton이 layout shift를 만들지 않는지 visual test 가능
- Error message는 사용자 친화적이고 안전해야 함

---

### [FAQ]

Q. Error State 테스트는 왜 중요한가?

A.
운영 환경에서는 API 실패, 권한 없음, 네트워크 오류가 발생하므로 사용자가 복구할 수 있는 UI가 필요하다.

Q. Empty State도 테스트해야 하나?

A.
해야 한다. 데이터가 없을 때 화면이 깨지지 않고 다음 행동을 안내해야 한다.

Q. Loading State는 어떻게 테스트하나?

A.
지연된 API mock을 사용해 loading UI가 나타나는지 확인한다.

---

# 21. Test Data and Fixture Rules

## 21.1 테스트 데이터 / Fixture 관리

### [개념]

Test Data and Fixture는 테스트에서 사용하는 사용자, 게시글, 상품, 응답, 에러, 권한 상태 데이터를 일관되게 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Fixture
- Test Data Builder
- Factory
- Mock User
- Mock API Response
- Seed Data
- Test Account
- Role Fixture
- Error Fixture
- Empty Fixture
- Edge Case Data
- Deterministic Data

---

### [실무]

작성 기준:

- 테스트 데이터는 작고 명확하게 유지
- 여러 테스트에서 반복되는 데이터는 fixture로 분리
- 필요 없는 필드까지 거대한 fixture에 넣지 않기
- edge case fixture 포함
- role별 user fixture 준비
- 날짜 / 시간 고정
- random 값 고정
- 테스트 간 데이터 공유로 인한 의존성 방지
- E2E 테스트 데이터는 setup / cleanup 전략 포함
- 실제 개인정보 사용 금지

예시:

```ts
export const mockUser = {
  id: "user-1",
  name: "테스트 사용자",
  role: "USER",
};
```

---

### [FAQ]

Q. Fixture는 왜 필요한가?

A.
테스트 데이터를 반복해서 만들지 않고 일관되고 읽기 쉽게 관리하기 위해 필요하다.

Q. Fixture는 실제 API 응답 전체를 그대로 복사해야 하나?

A.
필요한 필드만 유지하는 것이 좋다. 너무 큰 fixture는 테스트 의도를 흐린다.

Q. 테스트에 실제 개인정보를 써도 되나?

A.
안 된다. 테스트 데이터는 가짜 데이터를 사용해야 한다.

---

# 22. Mocking Rules

## 22.1 Mocking 기준

### [개념]

Mocking은 테스트 대상 외부의 의존성을 가짜 객체나 응답으로 대체해 테스트를 안정적으로 만드는 방법이다.

---

### [핵심]

Mock 대상:

- API
- Router
- Browser API
- Date / Time
- Random
- LocalStorage
- SessionStorage
- Clipboard
- IntersectionObserver
- ResizeObserver
- MatchMedia
- WebSocket
- Payment SDK
- Map SDK
- Analytics SDK

---

### [실무]

작성 기준:

- 외부 시스템과 불안정한 요소만 mock
- 테스트 대상 내부 구현을 과도하게 mock하지 않기
- 네트워크 요청은 MSW 등으로 mock
- 시간은 fake timer 또는 고정 clock 사용
- 브라우저 API 미지원 시 test setup에서 mock
- Third-party SDK는 wrapper를 만들어 mock하기 쉽게 설계
- mock은 테스트 후 reset / restore
- 실제 동작과 너무 다른 mock 금지
- Mocking이 많아지면 아키텍처 경계 재검토

주의:

- 과도한 mock은 테스트 신뢰도를 낮춤
- mock이 실제 API와 달라지면 false positive 발생
- shared mock 상태가 테스트 간 오염될 수 있음
- mock reset 누락은 flaky test 원인

---

### [FAQ]

Q. Mocking은 많이 할수록 좋은가?

A.
아니다. 외부 경계만 mock하고 테스트 대상의 실제 동작은 가능한 유지하는 것이 좋다.

Q. 브라우저 API가 jsdom에 없으면 어떻게 하나?

A.
test setup에서 필요한 최소 API를 mock하거나 browser-based test로 옮긴다.

Q. Third-party SDK는 어떻게 테스트하나?

A.
SDK를 직접 곳곳에서 호출하지 말고 wrapper로 감싼 뒤 wrapper를 mock하는 것이 좋다.

---

# 23. Async Testing Rules

## 23.1 비동기 UI 테스트

### [개념]

Async Testing은 API 요청, timeout, debounce, lazy loading, Suspense, route transition처럼 시간이 걸리는 UI 변화를 안정적으로 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- API Loading
- API Success
- API Error
- Debounce
- Timeout
- Retry
- Suspense Fallback
- Lazy Component
- Route Transition
- Mutation Pending
- Background Refetch
- Animation End

---

### [실무]

작성 기준:

- 비동기 렌더링은 `findBy...` 사용
- 상태가 사라지는 것은 `waitForElementToBeRemoved` 검토
- 불안정한 `setTimeout` 기반 대기 금지
- debounce는 fake timer 또는 user delay 전략 사용
- API mock 응답 timing 제어
- mutation pending / success / error 상태 검증
- Suspense fallback과 resolved UI 검증
- 테스트 timeout 증가로 문제를 덮지 않기
- 비동기 오류는 await 누락 확인

예시:

```tsx
expect(await screen.findByText("검색 결과")).toBeInTheDocument();
```

---

### [FAQ]

Q. 비동기 테스트에서 가장 흔한 실수는?

A.
await를 누락하거나 고정 sleep으로 기다리는 것이다.

Q. `findBy`와 `getBy` 차이는?

A.
`getBy`는 즉시 찾고, `findBy`는 비동기적으로 나타날 때까지 기다린다.

Q. waitFor를 남용해도 되나?

A.
권장하지 않는다. 가능한 사용자에게 나타나는 요소를 `findBy`로 기다리는 것이 더 명확하다.

---

# 24. Flaky Test Prevention Rules

## 24.1 Flaky Test 방지

### [개념]

Flaky Test는 코드가 바뀌지 않았는데 실행할 때마다 성공과 실패가 달라지는 불안정한 테스트이다.

---

### [핵심]

원인:

- 고정 sleep
- 비동기 await 누락
- 테스트 간 상태 공유
- 랜덤 데이터
- 시간 의존성
- 네트워크 의존성
- 외부 서비스 의존성
- animation
- race condition
- shared mock 오염
- 테스트 순서 의존
- selector 불안정
- CI 리소스 부족

---

### [실무]

방지 기준:

- sleep 대신 명시적 wait 사용
- 테스트마다 상태 초기화
- 날짜 / random 고정
- 외부 API mock
- 테스트 데이터 setup / cleanup 명확화
- stable selector 또는 accessible query 사용
- animation 비활성화 검토
- retry로 문제를 숨기지 않기
- flaky test는 quarantine / 이슈 등록 / 원인 해결
- CI와 local 환경 차이 문서화
- 병렬 실행 시 데이터 충돌 방지

---

### [FAQ]

Q. Flaky Test는 왜 위험한가?

A.
테스트 신뢰도를 떨어뜨리고 실제 버그를 놓치거나 배포 속도를 늦추기 때문이다.

Q. Flaky Test를 retry로 해결하면 되나?

A.
일시 완화는 가능하지만 근본 원인을 해결해야 한다.

Q. CI에서만 실패하는 테스트는 무엇을 봐야 하나?

A.
환경변수, 브라우저 버전, CPU 속도, 네트워크 mock, 테스트 데이터 충돌, 비동기 wait를 확인해야 한다.

---

# 25. Coverage Rules

## 25.1 Test Coverage 기준

### [개념]

Coverage는 코드 중 테스트가 실행한 부분의 비율을 보여주는 지표이다.

Coverage는 유용한 참고 지표이지만 테스트 품질을 보장하지는 않는다.

---

### [핵심]

Coverage 유형:

- Line Coverage
- Branch Coverage
- Function Coverage
- Statement Coverage
- Feature Coverage
- Flow Coverage
- Critical Path Coverage

---

### [실무]

작성 기준:

- 단순 숫자보다 핵심 Flow coverage 우선
- permission / error / edge case branch 확인
- 새 기능에는 테스트 기준 포함
- 중요한 유틸과 validator는 branch coverage 확인
- coverage 목표는 프로젝트 규모에 맞게 설정
- coverage를 높이기 위한 의미 없는 테스트 금지
- E2E coverage와 Unit coverage를 혼동하지 않기
- coverage report는 CI에서 확인 가능하게 구성
- 변경된 코드 기준 coverage 검토 가능

주의:

- 100% coverage가 버그 없음을 의미하지 않음
- assertion 없는 테스트도 coverage를 올릴 수 있음
- UI 사용자 Flow가 누락되어도 line coverage는 높을 수 있음

---

### [FAQ]

Q. Coverage가 높으면 테스트 품질이 좋은가?

A.
항상 그렇지 않다. 중요한 사용자 Flow와 edge case를 검증하는지가 더 중요하다.

Q. Coverage 목표를 정해야 하나?

A.
정할 수 있다. 단, 숫자 자체보다 핵심 기능과 위험 영역 검증을 우선해야 한다.

Q. Branch Coverage는 왜 중요한가?

A.
권한, 에러, validation 같은 조건 분기가 제대로 테스트되는지 확인할 수 있기 때문이다.

---

# 26. CI Test Pipeline Rules

## 26.1 CI 테스트 파이프라인

### [개념]

CI Test Pipeline은 Pull Request와 배포 과정에서 lint, typecheck, unit, component, integration, E2E, visual, accessibility test를 자동으로 실행하는 구조이다.

---

### [핵심]

CI 단계:

- Install
- Lint
- Typecheck
- Unit Test
- Component Test
- Integration Test
- Build
- E2E Test
- Accessibility Test
- Visual Regression Test
- Coverage Report
- Test Artifact Upload
- Flaky Test Report

권장 Flow:

```text
Pull Request
→ Install
→ Lint / Typecheck
→ Unit / Component / Integration Test
→ Build
→ E2E Smoke Test
→ Report / Artifact
```

---

### [실무]

작성 기준:

- 빠른 테스트는 PR마다 실행
- 느린 E2E는 핵심 smoke 중심으로 PR 실행
- 전체 E2E는 main / nightly / release 전 실행 가능
- Visual Regression은 Design System / UI 변경 시 실행
- 테스트 실패 artifact로 screenshot / video / trace 저장
- 병렬 실행과 shard 검토
- 테스트 캐시 사용 검토
- 환경변수와 secret은 CI에서 안전하게 관리
- PR에서 flaky test 발생 시 원인 기록
- CI와 local test 명령어 일치

주의:

- CI 속도만 위해 핵심 테스트를 생략하지 않기
- 모든 테스트를 PR에 넣어 지나치게 느리게 만들지 않기
- secret이 test log에 노출되지 않게 관리
- E2E 테스트 데이터 충돌 주의

---

### [FAQ]

Q. PR에서 어떤 테스트를 돌려야 하나?

A.
lint, typecheck, unit, component, integration, build, 핵심 E2E smoke test를 우선 실행한다.

Q. 전체 E2E는 언제 돌리면 좋나?

A.
main branch, nightly, release 전, 큰 변경 후에 실행하는 전략이 좋다.

Q. 테스트 artifact는 왜 필요한가?

A.
CI 실패 원인을 빠르게 분석하기 위해 screenshot, video, trace, coverage report가 필요하다.

---

# 27. Performance Regression Testing Rules

## 27.1 성능 회귀 테스트

### [개념]

Performance Regression Testing은 변경 이후 페이지 로딩, 번들 크기, Web Vitals, route transition, interaction latency가 악화되지 않았는지 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- Bundle Size
- Initial JavaScript
- Route Bundle
- Lighthouse Score
- LCP
- INP
- CLS
- TTFB
- Route Transition
- Interaction Latency
- Image Weight
- Third-party Script Weight
- Performance Budget

---

### [실무]

작성 기준:

- bundle size budget 설정
- PR에서 bundle diff 확인
- 핵심 페이지 Lighthouse / synthetic test 가능
- Web Vitals는 production RUM과 연결
- 성능 테스트 환경은 일정하게 유지
- threshold 기준 문서화
- 작은 변동과 실제 회귀를 구분
- Third-party Script 추가는 리뷰 대상
- 성능 회귀 발견 시 관련 PR / release와 연결
- Frontend Performance Tuning 문서와 연계

---

### [FAQ]

Q. Performance Regression Test는 왜 필요한가?

A.
기능 추가로 번들 크기와 로딩 시간이 점점 증가하는 것을 조기에 발견하기 위해 필요하다.

Q. Bundle Size도 테스트 대상인가?

A.
그렇다. Initial Bundle과 Route Bundle이 성능에 큰 영향을 주므로 budget을 두고 확인하는 것이 좋다.

Q. Lighthouse 점수만 CI에서 보면 충분한가?

A.
아니다. synthetic 지표로 유용하지만 production RUM과 함께 봐야 한다.

---

# 28. Security-related Frontend Test Rules

## 28.1 보안 관련 프론트엔드 테스트

### [개념]

Security-related Frontend Test는 프론트엔드에서 발생하기 쉬운 XSS, redirect, 권한 UI, token 노출, error leakage, file upload validation을 검증하는 테스트이다.

---

### [핵심]

검증 대상:

- XSS-safe Rendering
- HTML Sanitization
- Safe Redirect
- Protected Route
- Role-based UI
- Server Action Authorization
- File Upload Validation
- Error Message Safety
- Token Not Logged
- Sensitive Data Masking
- CSP Smoke Check
- Dependency Audit

---

### [실무]

작성 기준:

- 사용자 입력이 HTML로 실행되지 않고 텍스트로 표시되는지 검증
- Markdown / Rich Text sanitizer 동작 검증
- redirect URL allowlist 검증
- 권한 없는 사용자의 UI와 서버 호출 검증
- file type / size validation 검증
- error message에 내부 정보가 노출되지 않는지 검증
- token / 개인정보가 log에 포함되지 않도록 테스트 가능
- 공격 payload는 안전하고 최소한의 검증 문자열로 제한
- Frontend Security 문서와 연계

주의:

- 프론트엔드 보안 테스트만으로 서버 보안 보장 불가
- 실제 공격 payload를 과도하게 문서화하지 않기
- 권한 검증은 서버 테스트와 함께 수행
- 테스트 로그에 민감정보를 남기지 않기

---

### [FAQ]

Q. 프론트엔드에서도 보안 테스트가 필요한가?

A.
필요하다. XSS 렌더링, safe redirect, 권한 UI, file validation, error leakage 같은 문제는 프론트엔드에서 검출할 수 있다.

Q. 권한 테스트는 UI만 확인하면 되나?

A.
아니다. UI 숨김과 함께 Server Action / API 호출 권한도 검증해야 한다.

Q. XSS 테스트는 어떻게 안전하게 작성하나?

A.
위험 payload를 상세히 나열하지 않고, 입력이 HTML이 아니라 텍스트로 렌더링되는지 중심으로 검증한다.

---

# 29. Test Review Rules

## 29.1 테스트 코드 리뷰 기준

### [개념]

Test Review는 테스트가 실제 사용자 가치와 위험을 검증하는지, 불안정하거나 과도하게 구현 세부사항에 의존하지 않는지 확인하는 과정이다.

---

### [핵심]

리뷰 기준:

- 테스트 이름이 시나리오를 설명하는가?
- 사용자 행동 중심인가?
- 구현 세부사항에 의존하지 않는가?
- 중요한 error / loading / empty 상태가 있는가?
- 접근성 query를 사용하는가?
- Mock 경계가 적절한가?
- 테스트 데이터가 명확한가?
- 비동기 await가 올바른가?
- flaky 가능성이 낮은가?
- assertion이 의미 있는가?
- 테스트가 너무 많은 책임을 갖지 않는가?
- 실패 메시지가 원인 파악에 도움 되는가?

---

### [실무]

리뷰 질문:

- 이 테스트가 깨지면 실제 사용자 문제가 있는가?
- 이 테스트가 깨지면 구현 변경 때문인가, 동작 변경 때문인가?
- E2E로 테스트할 필요가 있는가, Integration으로 충분한가?
- Mock이 실제 API와 충분히 유사한가?
- Snapshot을 무분별하게 사용했는가?
- 테스트가 읽기 쉬운가?
- 같은 내용을 여러 계층에서 중복 검증하는가?
- CI에서 안정적으로 실행될 수 있는가?

---

### [FAQ]

Q. 좋은 테스트의 기준은?

A.
사용자 행동과 중요한 결과를 검증하고, 구현 세부사항에 덜 의존하며, 빠르고 안정적으로 실행되는 테스트이다.

Q. 테스트 중복은 나쁜가?

A.
일부 핵심 Flow는 중복 검증할 수 있지만, 같은 세부사항을 여러 계층에서 과도하게 검증하면 유지 비용이 증가한다.

Q. 테스트 코드도 리팩토링해야 하나?

A.
그렇다. 테스트 코드가 읽기 어렵거나 반복이 심하면 유지보수성이 떨어진다.

---

# 30. Troubleshooting Rules

## 30.1 자주 발생하는 테스트 문제

### [개념]

Troubleshooting 문서는 Agent가 Frontend Testing 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- 테스트가 CI에서만 실패
- 비동기 테스트 실패
- `act` warning 발생
- 요소를 찾지 못함
- Mock API가 호출되지 않음
- 테스트 간 상태 공유
- Query Cache 오염
- Router Mock 실패
- Browser API 없음
- Snapshot이 자주 깨짐
- Visual Test가 flaky
- E2E가 느림
- E2E가 가끔 실패
- 테스트 데이터 충돌
- 로그인 E2E 실패
- Timezone 차이
- Date / Random 때문에 실패
- Animation 때문에 실패
- Coverage는 높은데 버그가 많음

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- CI에서만 E2E 테스트가 실패함

원인:

- 고정 sleep 사용
- CI 환경 CPU가 느림
- 테스트 데이터가 병렬 실행 중 충돌
- 환경변수 누락

해결:

- 명시적 wait 사용
- 테스트 데이터 isolation
- CI 환경변수 확인
- screenshot / trace artifact 확인
```

예시:

```md
문제:

- API Mock 응답이 적용되지 않음

원인:

- 요청 URL이 handler와 다름
- method가 다름
- mock server 시작 전 요청 발생
- handler reset 누락

해결:

- 실제 요청 URL / method 확인
- MSW handler 확인
- 테스트 setup에서 server lifecycle 설정
- 테스트 후 handler reset
```

예시:

```md
문제:

- 비동기 UI 요소를 찾지 못함

원인:

- `getBy`로 즉시 조회함
- API 응답 mock이 지연되거나 실패함
- await 누락
- loading 상태가 끝나기 전 검증함

해결:

- `findBy` 사용
- await 추가
- API mock 확인
- loading 제거 후 검증
```

---

### [FAQ]

Q. 테스트가 CI에서만 실패하면 무엇을 봐야 하나?

A.
환경변수, CPU 속도, 브라우저 버전, 테스트 데이터 충돌, 비동기 wait, artifact를 확인해야 한다.

Q. `act` warning은 왜 발생하나?

A.
상태 업데이트가 테스트 assertion 밖에서 비동기적으로 발생했는데 테스트가 이를 기다리지 않았을 때 발생할 수 있다.

Q. Coverage는 높은데 버그가 많으면 왜 그런가?

A.
line coverage만 높고 실제 사용자 Flow, edge case, error state를 검증하지 않았을 가능성이 있다.

---

# 31. Code Example Rules

## 31.1 코드 예제 작성 기준

### [개념]

Frontend Testing Strategy 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React / Next.js 기준 예제 우선
- 사용자 행동 중심
- 구현 세부사항 검증 금지
- 접근성 query 우선
- 긴 전체 파일 금지
- 불필요한 mock 최소화
- Secret / 개인정보 포함 금지
- flaky 패턴 금지
- 고정 sleep 금지
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Component Test
- Form Test
- API Mock Test
- Loading / Error Test
- Auth Flow Test
- Route Test
- Accessibility Assertion
- E2E Smoke Test
- Server Action Test
- Fixture Builder
- Test Wrapper
- Mock Browser API
- Flaky Test 개선 예제

금지 예제:

- class name만 검증하는 테스트
- 내부 state 직접 검증
- snapshot만 있는 UI 테스트
- 실제 API를 호출하는 Unit Test
- sleep으로 기다리는 E2E
- token / password / 개인정보 fixture
- 과도한 module mock
- 성공 상태만 검증하고 error state 누락
- 테스트 간 공유 상태를 초기화하지 않는 예제

---

### [FAQ]

Q. Frontend Testing 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. 테스트 예제에서 className을 검증해도 되나?

A.
스타일 시스템의 특정 계약을 검증하는 경우가 아니라면 사용자에게 보이는 상태와 접근성 기준으로 검증하는 것이 좋다.

---

# 32. Comparison Rules

## 32.1 필수 비교 대상

### [개념]

Frontend Testing Strategy 문서는 Agent의 테스트 범위 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Unit Test vs Component Test
- Component Test vs Integration Test
- Integration Test vs E2E Test
- E2E Test vs Visual Regression Test
- Snapshot Test vs Visual Regression Test
- Mock Function vs Network Mock
- MSW vs Module Mock
- Testing Library vs Enzyme-style Testing
- User Event vs Fire Event
- `getBy` vs `findBy` vs `queryBy`
- jsdom Test vs Browser Test
- Lab Test vs Production Monitoring
- Coverage vs Test Quality
- Manual QA vs Automated Test
- Flaky Retry vs Flaky Fix
- Accessibility Auto Test vs Manual Test
- Contract Test vs Mock Fixture

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 속도 / 신뢰도 / 비용 / 적합 대상 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Unit Test와 Component Test 차이는?

A.
Unit Test는 작은 로직 단위를 검증하고, Component Test는 UI 렌더링과 사용자 상호작용을 검증한다.

Q. Integration Test와 E2E Test 차이는?

A.
Integration Test는 기능 단위를 mock과 함께 검증하고, E2E Test는 실제 브라우저에서 전체 사용자 Flow를 검증한다.

Q. Snapshot Test와 Visual Regression Test 차이는?

A.
Snapshot은 코드 구조나 직렬화 결과를 비교하고, Visual Regression은 실제 화면 screenshot 차이를 비교한다.

---

# 33. Checklist Rules

## 33.1 문서 품질 체크리스트

### [개념]

Frontend Testing Strategy RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Testing Strategy 목적이 명확한가?
- [ ] Testing Pyramid 기준을 포함했는가?
- [ ] User-centric Testing 원칙을 포함했는가?
- [ ] Unit Test 기준을 포함했는가?
- [ ] Component Test 기준을 포함했는가?
- [ ] Integration Test 기준을 포함했는가?
- [ ] E2E Test 기준을 포함했는가?
- [ ] Accessibility Test 기준을 포함했는가?
- [ ] Visual Regression Test 기준을 포함했는가?
- [ ] Snapshot Test 남용 방지 기준을 포함했는가?
- [ ] API Mocking 전략을 포함했는가?
- [ ] Server State 테스트 기준을 포함했는가?
- [ ] Form / Auth / Routing 테스트 기준을 포함했는가?
- [ ] Next.js App Router 테스트 기준을 포함했는가?
- [ ] Design System 테스트 기준을 포함했는가?
- [ ] Error / Loading / Empty 상태 테스트를 포함했는가?
- [ ] Test Data / Fixture 기준을 포함했는가?
- [ ] Mocking 기준을 포함했는가?
- [ ] Async Testing 기준을 포함했는가?
- [ ] Flaky Test 방지 기준을 포함했는가?
- [ ] Coverage 기준을 포함했는가?
- [ ] CI Test Pipeline 기준을 포함했는가?
- [ ] Performance Regression / Security-related Test 기준을 포함했는가?
- [ ] Test Review 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Frontend Architecture / Design System / Performance / Security 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- 테스트 전략 문서는 도구 사용법보다 판단 기준 중심으로 작성
- Frontend Architecture / Design System / Next.js / Security 문서와 연계 가능해야 함

---

### [FAQ]

Q. Frontend Testing Strategy 문서 품질에서 가장 중요한 것은?

A.
테스트 유형별 목적, 사용자 중심 검증, Mocking 경계, 비동기 안정성, CI 실행 전략, Flaky Test 방지 기준이 명확해야 한다.

---

# 34. Retrieval Optimization Rules

## 34.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Testing Strategy
- Frontend Test
- Testing Pyramid
- Unit Test
- Component Test
- Integration Test
- E2E Test
- Accessibility Test
- Visual Regression Test
- Snapshot Test
- React Testing
- Next.js Testing
- App Router Testing
- Testing Library
- React Testing Library
- Vitest
- Jest
- Playwright
- Cypress
- MSW
- API Mocking
- User Event
- Accessible Query
- `getByRole`
- `findBy`
- `waitFor`
- Form Testing
- Auth Flow Testing
- Routing Testing
- Server State Testing
- Query Cache
- Error State Test
- Loading State Test
- Empty State Test
- Test Fixture
- Mocking Strategy
- Async Testing
- Flaky Test
- CI Test Pipeline
- Coverage
- Smoke Test
- Regression Test
- Design System Testing
- Performance Regression Test
- Security Test

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- 프론트엔드 테스트 전략 어떻게 잡아?
- Unit Component Integration E2E 차이
- React Testing Library는 어떻게 써?
- getBy findBy queryBy 차이
- userEvent와 fireEvent 차이
- API Mocking은 어떻게 해?
- MSW는 언제 써?
- Component Test는 뭘 검증해?
- E2E Test는 언제 써?
- Snapshot Test는 언제 써?
- Visual Regression Test는 왜 필요해?
- Accessibility Test는 어떻게 해?
- Form Test는 어떻게 작성해?
- Auth Flow Test는 어떻게 해?
- Next.js App Router 테스트는 어떻게 해?
- Server Action 테스트는 어떻게 해?
- Error Loading Empty 상태 테스트해야 해?
- 테스트가 CI에서만 실패해
- Flaky Test는 어떻게 줄여?
- Coverage 높으면 충분해?
- PR에서 어떤 테스트 돌려?
- 테스트 코드 리뷰 기준은?
- Design System 테스트는 어떻게 해?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 35. Version Rules

## 35.1 기준 버전

### [개념]

Frontend Testing Strategy 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern Frontend
- React 19+
- Next.js App Router
- TypeScript
- Testing Library
- User Event
- Vitest / Jest
- Playwright / Cypress
- MSW
- jsdom
- Browser Testing
- Accessibility Testing
- Visual Regression Testing
- CI-based Testing
- Component-driven Testing
- User-centric Testing

Legacy 제외:

- Enzyme-style implementation detail testing 중심
- class component 내부 state 직접 검증 중심
- Snapshot-only UI 테스트
- 모든 테스트를 E2E로 처리하는 방식
- 실제 API를 호출하는 Unit Test
- 고정 sleep 기반 E2E
- 테스트 간 공유 상태 방치
- 사용자 개인정보 fixture 사용
- Mock이 실제 API와 완전히 다른 테스트
- Coverage 숫자만 목표로 하는 테스트 전략

---

### [실무]

문서 작성 시 주의:

- 테스트 도구별 API는 버전별로 변할 수 있음
- 특정 도구보다 테스트 전략과 판단 기준을 우선
- React / Next.js App Router의 Server / Client Boundary 고려
- Frontend Architecture의 feature 구조와 테스트 위치 연계
- Design System 문서의 접근성 / visual test 기준과 연계
- Performance / Security 문서의 회귀 테스트 기준과 연계
- 테스트는 품질 보장 수단이지 목표 자체가 아님

---

### [FAQ]

Q. Frontend Testing 문서는 특정 도구 기준이어야 하나?

A.
아니다. Testing Library, Vitest, Jest, Playwright, Cypress, MSW 같은 도구를 다룰 수 있지만 핵심은 테스트 전략과 판단 기준이다.

Q. React 19와 Next.js App Router 기준을 고려해야 하나?

A.
그렇다. Server Component, Client Component, Server Action, Route Handler 테스트 경계를 고려해야 한다.

---

# 36. Common Mistakes

## 36.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Frontend Testing 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- 구현 세부사항을 직접 검증
- 내부 state를 테스트
- className만 검증
- Snapshot Test만 작성
- 성공 상태만 테스트하고 error / loading 누락
- 모든 테스트를 E2E로 작성
- 모든 API를 실제 호출
- Mock이 실제 API와 다름
- 테스트 간 cache / state 공유
- Query Client 초기화 누락
- 고정 sleep 사용
- async await 누락
- `getBy`로 비동기 요소 조회
- Flaky Test를 retry로만 해결
- 테스트 데이터가 너무 거대함
- 실제 개인정보를 fixture로 사용
- 접근성 query 대신 test id 남용
- E2E selector가 UI 구조에 강하게 의존
- CI artifact 저장 안 함
- Coverage 숫자만 높이고 핵심 Flow 누락
- Auth / 권한 테스트에서 UI만 검증
- Visual Test의 동적 데이터 고정 누락

---

### [실무]

리뷰 기준:

- 사용자 행동 중심인지 확인
- 테스트 유형이 적절한지 확인
- 접근성 query 사용 여부 확인
- API Mock 경계 확인
- loading / error / empty 상태 확인
- Auth / 권한 Flow 확인
- 비동기 wait 안정성 확인
- 테스트 데이터 명확성 확인
- 테스트 간 독립성 확인
- Flaky 가능성 확인
- CI 실행 시간과 artifact 확인
- Coverage보다 핵심 Flow 검증 확인

---

### [FAQ]

Q. Frontend Testing에서 가장 흔한 실수는?

A.
사용자 행동이 아니라 내부 구현을 테스트하고, 성공 상태만 검증하며, 비동기 처리를 안정적으로 기다리지 않는 것이다.

Q. test id를 쓰면 안 되나?

A.
필요할 때는 사용할 수 있지만 role, label, text 같은 사용자 중심 query를 먼저 고려해야 한다.

Q. Flaky Test를 방치하면 왜 위험한가?

A.
테스트 신뢰도가 떨어지고 실제 버그와 테스트 문제를 구분하기 어려워진다.

---

# 37. Final Goal

## 37.1 최종 목표

### [개념]

Frontend Testing Strategy RAG 문서는 Agent가 프론트엔드 프로젝트에서 테스트 전략을 설계, 생성, 검토, 개선할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Testing Pyramid 설계
- Unit / Component / Integration / E2E 테스트 범위 판단
- 사용자 중심 테스트 코드 생성
- API Mocking 전략 제안
- MSW / 네트워크 Mock 기준 제안
- Server State 테스트 설계
- Form / Auth / Routing 테스트 설계
- Error / Loading / Empty 상태 테스트 설계
- Next.js App Router 테스트 경계 판단
- Server Action / Route Handler 테스트 기준 제안
- Design System 테스트 기준 제안
- Accessibility Test 기준 제안
- Visual Regression Test 기준 제안
- Snapshot Test 남용 진단
- Test Fixture / Mocking 기준 제안
- Async / Flaky Test 문제 진단
- CI Test Pipeline 구성 제안
- Coverage 기준 제안
- Performance / Security Regression Test 제안
- 테스트 코드 리뷰
- 테스트 Troubleshooting

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- 사용자 행동 중심 테스트 원칙 명확화
- 테스트 유형 / Mocking / CI / Flaky / Coverage 경계 명확화
- Frontend Architecture / Design System / Next.js / Security / Performance 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Testing Strategy Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 테스트 유형을 적절히 선택하고, 사용자 중심 테스트를 생성하며, Mocking / CI / Flaky / Coverage 문제를 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Testing Strategy 문서는 어떤 기준으로 작성해야 해?

A.
Testing Pyramid, 사용자 중심 테스트, Unit / Component / Integration / E2E, Mocking, Accessibility, Visual Regression, CI, Flaky Test 방지 기준으로 작성해야 한다.

Q. 프론트엔드 테스트 전략 어떻게 잡아?

A.
순수 로직은 Unit, UI 상호작용은 Component, 기능 흐름은 Integration, 핵심 사용자 Flow는 E2E로 나누어 설계한다.

Q. Testing Pyramid는 뭐야?

A.
빠른 작은 테스트를 많이 두고, 느리고 큰 E2E 테스트는 핵심 Flow 중심으로 제한하는 전략이다.

Q. Unit Component Integration E2E 차이는?

A.
Unit은 작은 로직, Component는 UI 상호작용, Integration은 기능 흐름, E2E는 실제 브라우저 전체 Flow를 검증한다.

Q. Unit Test는 언제 써?

A.
순수 함수, 유틸, formatter, validator, reducer, custom hook 같은 작은 로직을 검증할 때 사용한다.

Q. Component Test는 뭘 검증해?

A.
컴포넌트가 사용자에게 어떻게 보이고 사용자의 행동에 어떻게 반응하는지 검증한다.

Q. Integration Test는 언제 필요해?

A.
여러 컴포넌트와 API 응답, 상태, 라우팅이 함께 동작하는 기능 흐름을 검증할 때 필요하다.

Q. E2E Test는 언제 써?

A.
로그인, 결제, 회원가입, 검색, 파일 업로드 같은 핵심 사용자 Flow를 실제 브라우저에서 검증할 때 사용한다.

Q. 모든 테스트를 E2E로 작성하면 안 돼?

A.
권장하지 않는다. E2E는 느리고 flaky해질 수 있으므로 핵심 Flow 중심으로 제한한다.

Q. React Testing Library는 어떻게 써?

A.
구현 세부사항이 아니라 사용자의 행동과 화면 결과를 검증하고, role / label / text 기반 query를 우선 사용한다.

Q. getBy findBy queryBy 차이는?

A.
`getBy`는 즉시 찾아야 할 요소, `findBy`는 비동기적으로 나타나는 요소, `queryBy`는 없어야 하는 요소 검증에 주로 사용한다.

Q. userEvent와 fireEvent 차이는?

A.
userEvent는 실제 사용자 상호작용에 더 가깝게 이벤트를 발생시키고, fireEvent는 낮은 수준의 이벤트 발생에 가깝다.

Q. 접근성 query는 왜 중요해?

A.
사용자가 접근 가능한 역할과 이름을 기준으로 요소를 찾기 때문에 테스트와 접근성 품질을 함께 높일 수 있다.

Q. test id를 쓰면 안 돼?

A.
필요할 때는 사용할 수 있지만 role, label, text 같은 사용자 중심 query를 먼저 고려해야 한다.

Q. API Mocking은 어떻게 해?

A.
Component / Integration Test에서는 MSW 같은 네트워크 레벨 mocking을 우선 검토하고, success / error / empty 상태를 제어한다.

Q. MSW는 언제 써?

A.
API Client 내부를 직접 mock하지 않고 실제 네트워크 요청에 가까운 방식으로 응답을 제어하고 싶을 때 사용한다.

Q. Mock 데이터가 실제 API와 다르면 어떻게 해?

A.
API Contract, fixture 관리, contract test, schema validation으로 동기화해야 한다.

Q. Server State 테스트는 뭘 봐야 해?

A.
loading, success, error, empty, mutation 후 invalidation, optimistic update rollback을 검증해야 한다.

Q. Query Cache는 테스트마다 초기화해야 해?

A.
그렇다. 테스트 간 cache가 공유되면 결과가 불안정해질 수 있다.

Q. Form Test는 어떻게 작성해?

A.
입력, validation message, submit, pending state, server error, success state, 접근성 연결을 검증한다.

Q. Placeholder로 input 찾아도 돼?

A.
가능은 하지만 label 기반 query가 더 좋다. Label이 없으면 접근성 문제가 있을 수 있다.

Q. 서버 validation error도 테스트해야 해?

A.
해야 한다. 클라이언트 validation을 통과해도 서버에서 거절될 수 있기 때문이다.

Q. Auth Flow Test는 어떻게 해?

A.
로그인 성공 / 실패, 로그아웃, 세션 만료, protected route, 401 / 403, role-based UI를 검증한다.

Q. 권한 테스트는 프론트엔드만 하면 충분해?

A.
아니다. UI 숨김 테스트와 서버 API / Server Action 권한 테스트가 함께 필요하다.

Q. 401과 403 테스트는 왜 구분해?

A.
401은 인증 필요, 403은 권한 없음 상태이므로 사용자 안내와 처리 Flow가 다르다.

Q. Routing Test는 어떻게 해?

A.
링크 클릭 후 URL과 화면 변화, search params, dynamic route, protected route redirect, not found를 검증한다.

Q. 검색 필터 상태를 URL에 넣으면 테스트해야 해?

A.
그렇다. 새로고침, 공유 링크, 뒤로가기에서 상태가 복원되는지 확인해야 한다.

Q. Next.js App Router 테스트는 어떻게 해?

A.
Client Component는 Component Test, Server Component와 routing / cache 흐름은 Integration 또는 E2E, Server Action은 서버 로직 테스트로 검증한다.

Q. Server Component도 Component Test로 테스트해?

A.
단순 렌더링은 가능할 수 있지만 실제 data fetching과 framework context가 있으면 Integration 또는 E2E가 더 적합할 수 있다.

Q. Server Action 테스트는 어떻게 해?

A.
입력 검증, 인증 / 권한 검증, mutation 결과, revalidation 호출 여부를 서버 로직 테스트로 검증한다.

Q. Route Handler 테스트는 어떻게 해?

A.
API endpoint처럼 method, auth, input validation, response, error handling을 검증한다.

Q. error.tsx 테스트는 어떻게 해?

A.
fallback UI, 안전한 에러 메시지, reset 동작, error reporting 호출 여부를 검증한다.

Q. Design System 테스트는 어떻게 해?

A.
variant, state, accessibility, keyboard interaction, theme, visual regression, public API를 테스트한다.

Q. Modal 테스트에서 중요한 것은?

A.
focus trap, escape key, focus return, role, label, backdrop 동작을 검증하는 것이다.

Q. Accessibility Test는 어떻게 해?

A.
자동 접근성 도구, role / label 기반 query, keyboard navigation, focus management, color contrast 검증을 함께 사용한다.

Q. 자동 접근성 테스트만으로 충분해?

A.
아니다. 자동 도구는 일부 문제만 잡으므로 키보드 탐색과 스크린 리더 흐름은 수동 검증도 필요하다.

Q. Visual Regression Test는 왜 필요해?

A.
Design System, 공통 UI, 레이아웃, 테마가 의도치 않게 깨지는 것을 막기 위해 필요하다.

Q. Visual Test가 flaky하면 왜 그래?

A.
폰트 렌더링, 애니메이션, 동적 데이터, 브라우저 차이, 비동기 로딩 때문일 수 있다.

Q. Snapshot Test는 언제 써?

A.
작고 안정적인 출력 구조나 design token output처럼 변경 감지가 필요한 경우에 적합하다.

Q. Snapshot Test만 있으면 충분해?

A.
아니다. 사용자 행동, 접근성, error state, API flow는 별도 테스트가 필요하다.

Q. Error Loading Empty 상태 테스트해야 해?

A.
해야 한다. 운영 환경에서는 로딩, 빈 데이터, API 실패, 권한 없음이 자주 발생하기 때문이다.

Q. Loading State는 어떻게 테스트해?

A.
지연된 API mock을 사용해 loading UI가 나타나고 응답 후 사라지는지 확인한다.

Q. Empty State도 테스트해야 해?

A.
해야 한다. 데이터가 없을 때 화면이 깨지지 않고 다음 행동을 안내해야 한다.

Q. Test Fixture는 어떻게 관리해?

A.
작고 명확한 fixture를 사용하고, role별 / error별 / edge case별 데이터를 분리하며 실제 개인정보는 사용하지 않는다.

Q. Mocking은 많이 할수록 좋아?

A.
아니다. 외부 경계만 mock하고 테스트 대상의 실제 동작은 가능한 유지하는 것이 좋다.

Q. 브라우저 API가 jsdom에 없으면 어떻게 해?

A.
test setup에서 필요한 최소 API를 mock하거나 browser-based test로 옮긴다.

Q. 비동기 테스트에서 가장 흔한 실수는?

A.
await를 누락하거나 고정 sleep으로 기다리는 것이다.

Q. findBy와 getBy 차이는?

A.
`getBy`는 즉시 찾고, `findBy`는 비동기적으로 나타날 때까지 기다린다.

Q. waitFor를 남용해도 돼?

A.
권장하지 않는다. 가능한 사용자에게 나타나는 요소를 `findBy`로 기다리는 것이 더 명확하다.

Q. 테스트가 CI에서만 실패해. 무엇을 봐?

A.
환경변수, CPU 속도, 브라우저 버전, 테스트 데이터 충돌, 비동기 wait, artifact를 확인한다.

Q. Flaky Test는 어떻게 줄여?

A.
sleep 제거, 명시적 wait, 상태 초기화, 날짜 / random 고정, API mock, 테스트 데이터 isolation을 적용한다.

Q. Flaky Test를 retry로 해결하면 돼?

A.
일시 완화는 가능하지만 근본 원인을 해결해야 한다.

Q. act warning은 왜 발생해?

A.
상태 업데이트가 테스트 assertion 밖에서 비동기적으로 발생했는데 테스트가 이를 기다리지 않았을 때 발생할 수 있다.

Q. Coverage 높으면 충분해?

A.
아니다. 핵심 사용자 Flow, error state, edge case, branch 검증이 더 중요하다.

Q. Branch Coverage는 왜 중요해?

A.
권한, 에러, validation 같은 조건 분기가 제대로 테스트되는지 확인할 수 있기 때문이다.

Q. PR에서 어떤 테스트 돌려?

A.
lint, typecheck, unit, component, integration, build, 핵심 E2E smoke test를 우선 실행한다.

Q. 전체 E2E는 언제 돌려?

A.
main branch, nightly, release 전, 큰 변경 후에 실행하는 전략이 좋다.

Q. 테스트 artifact는 왜 필요해?

A.
CI 실패 원인을 빠르게 분석하기 위해 screenshot, video, trace, coverage report가 필요하다.

Q. Performance Regression Test는 왜 필요해?

A.
기능 추가로 bundle size와 로딩 시간이 증가하는 것을 조기에 발견하기 위해 필요하다.

Q. Bundle Size도 테스트 대상이야?

A.
그렇다. Initial Bundle과 Route Bundle이 성능에 큰 영향을 주므로 budget을 두고 확인하는 것이 좋다.

Q. 프론트엔드 보안 테스트는 뭐를 봐?

A.
XSS-safe rendering, safe redirect, 권한 UI, Server Action 권한, file validation, error leakage를 검증한다.

Q. 테스트 코드 리뷰 기준은?

A.
사용자 행동 중심인지, 테스트 유형이 적절한지, mock 경계가 올바른지, 비동기 안정성이 있는지, error / loading 상태를 포함했는지 확인한다.

Q. 좋은 테스트의 기준은?

A.
사용자 행동과 중요한 결과를 검증하고, 구현 세부사항에 덜 의존하며, 빠르고 안정적으로 실행되는 테스트이다.

Q. Frontend Testing Strategy RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 테스트 유형을 적절히 선택하고, 사용자 중심 테스트를 생성하며, Mocking / CI / Flaky / Coverage 문제를 리뷰하도록 만드는 것이다.
