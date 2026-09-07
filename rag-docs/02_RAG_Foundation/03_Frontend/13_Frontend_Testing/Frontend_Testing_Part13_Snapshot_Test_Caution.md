# Frontend Testing Part13 - Snapshot Test Caution

---

# 1. Snapshot Test Overview

## 1.1 Snapshot Test Definition

### [개념]

Snapshot Test는 렌더링 결과나 객체 구조를 저장해 두고, 이후 테스트 실행 시 이전 snapshot과 현재 결과가 같은지 비교하는 테스트다.

Frontend Testing에서 Snapshot Test는 UI 변경 감지에는 사용할 수 있지만, 사용자 행동과 의미 있는 결과를 검증하는 테스트를 대체하지 못한다.

### [핵심]

- Snapshot Test
- Jest Snapshot
- Vitest Snapshot
- toMatchSnapshot
- toMatchInlineSnapshot
- UI Snapshot
- Object Snapshot
- DOM Snapshot
- Regression Detection
- Snapshot Caution
- Behavior Test
- User-visible Result
- React Testing Library
- Snapshot Anti Pattern

### [실무]

Snapshot Test의 기본 개념:

```text
Render Component
→ Snapshot 저장
→ 다음 테스트 실행 시 현재 결과와 저장된 Snapshot 비교
→ 차이가 있으면 실패
```

Snapshot Test가 유용한 경우:

```text
작은 pure object output 확인
작은 formatter 결과 구조 확인
정적인 presentational component 변경 감지
복잡하지 않은 generated markup 확인
API schema fixture 변경 감지
```

Snapshot Test가 부적합한 경우:

```text
사용자 클릭 결과 검증
Form 입력 validation 검증
API 성공/실패 UI 검증
Router 이동 검증
Auth 접근 제어 검증
Loading/Error/Empty 상태 검증
접근성 role/label 검증
```

권장 원칙:

```text
Snapshot은 보조 수단
Behavior Test가 우선
Snapshot-only Test 금지
큰 DOM Snapshot 지양
Snapshot 변경은 반드시 리뷰
```

### [FAQ]

Q. Snapshot Test는 뭐야?
A. 이전에 저장한 렌더링 결과나 객체 구조와 현재 결과를 비교하는 테스트다.

Q. Snapshot Test만으로 UI 테스트를 대체할 수 있어?
A. 아니다. 사용자의 행동과 화면 결과를 검증하는 Behavior Test가 우선이다.

Q. Snapshot Test는 언제 유용해?
A. 작고 안정적인 출력 구조의 변경 감지나 정적인 결과 비교에 보조적으로 유용하다.

## 1.2 Snapshot Test Role

### [개념]

Snapshot Test의 역할은 예기치 않은 구조 변경을 감지하는 것이다.

하지만 구조가 같다고 사용자 경험이 올바른 것은 아니며, 구조가 바뀌었다고 항상 버그인 것도 아니다.

### [핵심]

Snapshot 역할:

- regression detection
- structure change detection
- static output check
- generated object check
- schema fixture check
- small component guard
- review signal

Snapshot이 검증하지 못하는 것:

- user behavior
- accessibility
- keyboard interaction
- validation logic
- async UI state
- API error handling
- visual correctness
- business correctness

### [실무]

Snapshot이 알려주는 것:

```text
렌더링 구조가 이전과 달라졌다.
객체 출력이 이전과 달라졌다.
className / text / element tree가 변경되었다.
```

Snapshot이 알려주지 못하는 것:

```text
이 버튼을 사용자가 이해할 수 있는가?
이 input에 label이 연결되어 있는가?
이 Modal이 keyboard로 닫히는가?
이 Form 오류가 사용자에게 적절한가?
API 실패 시 올바른 ErrorState가 나오는가?
```

따라서 Snapshot은 다음과 함께 사용한다.

```text
Snapshot Test
+ getByRole / getByLabelText
+ userEvent
+ findBy
+ accessibility assertion
+ visible UI assertion
```

### [FAQ]

Q. Snapshot Test의 핵심 역할은 뭐야?
A. 예기치 않은 구조 변경을 감지하는 보조 역할이다.

Q. Snapshot이 통과하면 UI가 정상이라고 봐도 돼?
A. 아니다. 사용자 행동, 접근성, 상태 흐름은 별도 테스트가 필요하다.

Q. Snapshot 실패는 항상 버그야?
A. 아니다. 의도된 UI 변경일 수 있으므로 변경 내용을 리뷰해야 한다.

# 2. Snapshot Test Priority

## 2.1 Behavior Test First Rule

### [개념]

Behavior Test First Rule은 Snapshot보다 사용자의 행동과 결과를 직접 검증하는 테스트를 우선 작성해야 한다는 규칙이다.

React Testing Library 기반 Frontend Testing에서는 사용자 관점 테스트가 Snapshot보다 우선순위가 높다.

### [핵심]

우선순위:

1. User-visible Result
2. Accessibility Query
3. userEvent Interaction
4. Async State
5. Error / Empty / Loading State
6. Snapshot as Supplement

관련 키워드:

- Behavior Test
- User-centric Test
- RTL Philosophy
- getByRole
- userEvent
- visible result
- snapshot supplement
- implementation detail caution

### [실무]

나쁜 예:

```tsx
test("LoginForm snapshot", () => {
  const { container } = render(<LoginForm />);

  expect(container).toMatchSnapshot();
});
```

좋은 예:

```tsx
test("로그인 Form은 이메일, 비밀번호 입력창과 로그인 버튼을 제공한다", () => {
  render(<LoginForm />);

  expect(screen.getByLabelText("이메일")).toBeInTheDocument();
  expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "로그인" })).toBeInTheDocument();
});
```

상호작용 테스트:

```tsx
test("이메일을 입력하지 않고 제출하면 오류 메시지를 표시한다", async () => {
  const user = userEvent.setup();

  render(<LoginForm />);

  await user.click(screen.getByRole("button", { name: "로그인" }));

  expect(screen.getByText("이메일을 입력해 주세요.")).toBeInTheDocument();
});
```

권장:

- 먼저 사용자가 보는 결과를 검증
- Snapshot은 추가 변경 감지 용도로만 사용
- Snapshot만 있는 테스트 금지
- Snapshot이 없어도 테스트 의도가 드러나야 함

### [FAQ]

Q. Snapshot보다 Behavior Test가 우선인 이유는?
A. 사용자가 실제로 보는 결과와 수행하는 행동이 테스트의 핵심이기 때문이다.

Q. Snapshot-only Test는 왜 안 좋아?
A. 테스트 의도가 불명확하고 사용자 기능이 실제로 동작하는지 알기 어렵기 때문이다.

Q. React Testing Library에서는 어떤 테스트가 좋아?
A. role, label, text, userEvent를 사용해 사용자 관점 결과를 검증하는 테스트가 좋다.

## 2.2 Snapshot Priority Table

### [개념]

Snapshot Priority Table은 어떤 상황에서 Snapshot을 쓰고 어떤 상황에서 피해야 하는지 판단하는 기준이다.

### [핵심]

| 테스트 대상                   | Snapshot 적합도 | 권장 방식                           |
| ----------------------------- | --------------: | ----------------------------------- |
| Form validation               |            낮음 | userEvent + error message           |
| Button click                  |            낮음 | userEvent + callback/result         |
| Router 이동                   |            낮음 | Page UI 결과                        |
| API 상태 UI                   |            낮음 | mock + Loading/Error/Empty          |
| Accessibility                 |            낮음 | getByRole / keyboard / axe          |
| 작은 pure object              |            중간 | inline snapshot 가능                |
| 정적 presentational component |            중간 | visible assertion + 선택적 snapshot |
| 복잡한 DOM tree               |            낮음 | 의미 있는 assertion 분리            |
| Storybook visual regression   |            별도 | visual regression tool              |
| Generated config/schema       |       중간~높음 | object snapshot 가능                |

### [실무]

Snapshot 사용 판단 Flow:

```text
사용자 행동 검증인가?
→ Snapshot보다 userEvent 사용

접근성 검증인가?
→ Snapshot보다 getByRole / getByLabelText 사용

비동기 상태 검증인가?
→ Snapshot보다 findBy / waitFor 사용

작고 안정적인 출력 구조인가?
→ Snapshot 고려 가능

Snapshot diff를 사람이 쉽게 리뷰할 수 있는가?
→ 가능하면 사용
→ 어렵다면 사용 지양
```

### [FAQ]

Q. Form 테스트에 Snapshot을 써도 돼?
A. 권장하지 않는다. 입력, 제출, 오류 메시지를 userEvent와 assertion으로 검증하는 것이 좋다.

Q. 정적인 Component에는 Snapshot을 써도 돼?
A. 가능하지만 visible assertion을 우선하고 Snapshot은 보조로만 사용하는 것이 좋다.

Q. 큰 DOM Snapshot은 왜 피해야 해?
A. diff가 크고 의미를 파악하기 어려워 무심코 업데이트하기 쉽기 때문이다.

# 3. Good Snapshot Use Cases

## 3.1 Inline Snapshot for Small Object

### [개념]

Inline Snapshot은 테스트 파일 안에 snapshot 값을 직접 저장하는 방식이다.

작고 안정적인 객체 출력이나 변환 결과를 확인할 때 유용하다.

### [핵심]

- inline snapshot
- toMatchInlineSnapshot
- small object
- stable output
- mapper output
- config output
- schema output
- readable diff
- reviewable snapshot

### [실무]

작은 mapper 결과:

```ts
test("API 응답을 카드 View Model로 변환한다", () => {
  const result = toFestivalCardView({
    festivalId: 1,
    title: "봄꽃 축제",
    regionName: "서울",
    imageUrl: null,
  });

  expect(result).toMatchInlineSnapshot(`
    {
      "id": 1,
      "imageUrl": "/images/default-festival.png",
      "region": "서울",
      "title": "봄꽃 축제",
    }
  `);
});
```

다만 명확한 assertion이 더 나은 경우:

```ts
expect(result).toEqual({
  id: 1,
  title: "봄꽃 축제",
  region: "서울",
  imageUrl: "/images/default-festival.png",
});
```

권장:

- 출력이 작고 안정적인 경우에만 사용
- Snapshot diff를 리뷰하기 쉬워야 함
- 동적인 값 제거
- 중요한 field는 명시 assertion도 고려
- 큰 객체 전체 snapshot 지양

### [FAQ]

Q. Inline Snapshot은 언제 좋아?
A. 작고 안정적인 객체 결과를 테스트 파일 안에서 바로 확인하고 싶을 때 좋다.

Q. toEqual과 inline snapshot 중 뭐가 좋아?
A. 작은 객체는 toEqual이 더 명확할 때가 많고, 구조 변경 감지에는 inline snapshot이 유용할 수 있다.

Q. Inline Snapshot도 무조건 좋은 건 아니야?
A. 그렇다. 출력이 크거나 자주 바뀌면 유지보수 비용이 커진다.

## 3.2 Small Presentational Component Snapshot

### [개념]

Small Presentational Component Snapshot은 props 기반으로 정적인 UI를 표시하는 작은 Component의 구조 변경을 감지하는 용도로 사용할 수 있다.

하지만 사용자에게 보이는 텍스트와 role assertion이 우선이다.

### [핵심]

- presentational component
- static component
- small DOM
- props rendering
- visible assertion first
- optional snapshot
- snapshot supplement

### [실무]

예:

```tsx
test("StatusBadge는 상태 label을 표시한다", () => {
  const { container } = render(<StatusBadge status="ACTIVE" />);

  expect(screen.getByText("진행 중")).toBeInTheDocument();
  expect(container).toMatchSnapshot();
});
```

더 권장되는 방식:

```tsx
test("ACTIVE 상태이면 진행 중 label을 표시한다", () => {
  render(<StatusBadge status="ACTIVE" />);

  expect(screen.getByText("진행 중")).toBeInTheDocument();
});
```

Snapshot을 사용할 수 있는 조건:

```text
Component가 작다
DOM 구조가 안정적이다
diff를 사람이 쉽게 리뷰할 수 있다
사용자 visible assertion이 이미 있다
Snapshot 업데이트가 잦지 않다
```

### [FAQ]

Q. Presentational Component에 Snapshot을 써도 돼?
A. 작고 정적인 Component에는 보조적으로 사용할 수 있다.

Q. visible assertion 없이 snapshot만 두면 안 돼?
A. 권장하지 않는다. 사용자에게 무엇이 보여야 하는지 명확히 검증해야 한다.

Q. Badge나 Label Component는 Snapshot이 적합해?
A. 작고 안정적이면 가능하지만 텍스트 assertion만으로 충분한 경우도 많다.

## 3.3 Schema or Fixture Snapshot

### [개념]

Schema or Fixture Snapshot은 API fixture, generated config, route config, menu config 같은 정적 구조가 의도치 않게 바뀌었는지 감지하는 Snapshot이다.

UI DOM Snapshot보다 리뷰하기 쉬운 경우가 많다.

### [핵심]

- schema snapshot
- fixture snapshot
- config snapshot
- route config
- menu config
- API fixture
- generated data
- stable object
- reviewable structure

### [실무]

Menu config 예:

```ts
test("메인 메뉴 구성을 유지한다", () => {
  expect(getMainMenuItems()).toMatchInlineSnapshot(`
    [
      {
        "label": "홈",
        "path": "/",
      },
      {
        "label": "축제",
        "path": "/festivals",
      },
      {
        "label": "마이페이지",
        "path": "/mypage",
      },
    ]
  `);
});
```

Route config 예:

```ts
test("공개 Route 구성을 유지한다", () => {
  expect(publicRoutes).toMatchInlineSnapshot(`
    [
      "/",
      "/login",
      "/signup",
      "/festivals",
    ]
  `);
});
```

권장:

- 정적 config 변경 감지에 사용
- 보안상 민감정보 포함 금지
- route / menu 변경 시 snapshot diff 리뷰
- 너무 큰 config는 핵심 field만 snapshot
- 동적 환경값 제거

### [FAQ]

Q. Schema나 Config Snapshot은 UI Snapshot보다 나아?
A. 작고 정적인 구조라면 diff가 명확해 유용할 수 있다.

Q. Route config snapshot은 언제 유용해?
A. 공개 Route나 메뉴 구성이 의도치 않게 바뀌는 것을 감지하고 싶을 때 유용하다.

Q. Fixture Snapshot에 실제 개인정보를 넣어도 돼?
A. 안 된다. 테스트 fixture에는 더미 데이터만 사용해야 한다.

# 4. Bad Snapshot Use Cases

## 4.1 Large DOM Snapshot Caution

### [개념]

Large DOM Snapshot은 Page 전체 또는 복잡한 Component 전체 DOM을 snapshot으로 저장하는 방식이다.

대부분 diff가 너무 크고 의미를 파악하기 어려워 유지보수성이 낮다.

### [핵심]

- large DOM snapshot
- full page snapshot
- unreadable diff
- brittle test
- noisy change
- snapshot update abuse
- low signal
- high maintenance cost

### [실무]

나쁜 예:

```tsx
test("HomePage snapshot", () => {
  const { container } = render(<HomePage />);

  expect(container).toMatchSnapshot();
});
```

문제:

```text
DOM이 너무 큼
작은 UI 변경에도 diff가 많이 발생
실패 원인을 파악하기 어려움
리뷰 없이 snapshot 업데이트하기 쉬움
사용자 기능 검증이 없음
```

개선:

```tsx
test("HomePage는 주요 섹션을 표시한다", () => {
  render(<HomePage />);

  expect(
    screen.getByRole("heading", { name: "추천 축제" }),
  ).toBeInTheDocument();
  expect(
    screen.getByRole("heading", { name: "인기 축제" }),
  ).toBeInTheDocument();
  expect(
    screen.getByRole("link", { name: "축제 전체 보기" }),
  ).toBeInTheDocument();
});
```

권장:

- Page 전체 Snapshot 지양
- 의미 있는 section / heading / action assertion으로 분리
- 큰 DOM 변경 감지는 visual regression 도구 고려
- Snapshot diff를 리뷰할 수 없으면 사용하지 않음

### [FAQ]

Q. Page 전체 Snapshot은 왜 안 좋아?
A. diff가 크고 의미가 불명확해 실제 기능 회귀를 잡기 어렵기 때문이다.

Q. 큰 UI 변경 감지는 어떻게 해?
A. 핵심 사용자 결과 assertion과 필요 시 visual regression tool을 사용하는 것이 좋다.

Q. 큰 Snapshot도 업데이트하면 되지 않아?
A. 무심코 업데이트하면 실제 버그를 놓칠 수 있어 위험하다.

## 4.2 Interaction Snapshot Caution

### [개념]

Interaction Snapshot은 클릭, 입력, API 응답 후 변경된 DOM을 snapshot으로 비교하는 방식이다.

사용자 상호작용 테스트는 snapshot보다 visible result와 accessibility assertion으로 검증해야 한다.

### [핵심]

- interaction snapshot
- click result
- form input
- modal open
- dropdown open
- async result
- behavior assertion
- userEvent
- visible UI
- avoid snapshot-only

### [실무]

나쁜 예:

```tsx
test("모달 열림 snapshot", async () => {
  const user = userEvent.setup();
  const { container } = render(<DeleteButton />);

  await user.click(screen.getByRole("button", { name: "삭제" }));

  expect(container).toMatchSnapshot();
});
```

좋은 예:

```tsx
test("삭제 버튼을 클릭하면 삭제 확인 모달을 표시한다", async () => {
  const user = userEvent.setup();

  render(<DeleteButton />);

  await user.click(screen.getByRole("button", { name: "삭제" }));

  expect(screen.getByRole("dialog", { name: "삭제 확인" })).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "취소" })).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "삭제" })).toBeInTheDocument();
});
```

Form 나쁜 예:

```tsx
await user.type(screen.getByLabelText("이메일"), "test@example.com");
expect(container).toMatchSnapshot();
```

Form 좋은 예:

```tsx
expect(screen.getByLabelText("이메일")).toHaveValue("test@example.com");
```

권장:

- 상호작용 결과는 의미 있는 assertion으로 검증
- Modal은 role dialog와 accessible name 검증
- Form은 value / error message / submit result 검증
- Dropdown은 option 표시와 선택 결과 검증
- Snapshot은 상호작용 결과 검증의 대체가 아님

### [FAQ]

Q. 클릭 후 Snapshot으로 결과를 확인하면 안 돼?
A. 권장하지 않는다. 사용자가 보는 구체적인 결과를 assertion으로 확인해야 한다.

Q. Modal 열림은 Snapshot보다 뭘 테스트해야 해?
A. dialog role, title, content, 닫기 버튼, focus 상태를 테스트하는 것이 좋다.

Q. Form 입력 후 Snapshot은 왜 안 좋아?
A. 입력값과 validation 결과를 직접 검증하지 못하고 diff가 불명확해질 수 있다.

## 4.3 Async Snapshot Caution

### [개념]

Async Snapshot은 API 응답, loading 전환, error 상태 같은 비동기 UI를 snapshot으로 비교하는 방식이다.

비동기 상태는 `findBy`, `waitFor`, Loading/Error/Empty assertion으로 명확히 검증해야 한다.

### [핵심]

- async snapshot
- API response
- loading state
- error state
- empty state
- success state
- findBy
- waitFor
- API mocking
- user-visible state

### [실무]

나쁜 예:

```tsx
test("API success snapshot", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  const { container } = render(<FestivalListPage />);

  await waitFor(() => {
    expect(container).toMatchSnapshot();
  });
});
```

좋은 예:

```tsx
test("축제 목록 조회 성공 시 축제 제목을 표시한다", async () => {
  vi.mocked(getFestivals).mockResolvedValue([
    { festivalId: 1, title: "봄꽃 축제" },
  ]);

  render(<FestivalListPage />);

  expect(await screen.findByText("봄꽃 축제")).toBeInTheDocument();
});
```

Error State:

```tsx
test("서버 오류 시 ErrorState를 표시한다", async () => {
  vi.mocked(getFestivals).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  render(<FestivalListPage />);

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "서버 오류가 발생했습니다.",
  );
});
```

권장:

- 비동기 성공은 findBy로 데이터 확인
- 비동기 실패는 error message 확인
- empty response는 EmptyState 확인
- loading은 pending promise로 검증
- waitFor 안에서 snapshot 비교 지양

### [FAQ]

Q. 비동기 UI를 Snapshot으로 테스트하면 안 돼?
A. 권장하지 않는다. 성공, 실패, 빈 상태를 사용자 UI assertion으로 검증하는 것이 좋다.

Q. waitFor 안에서 snapshot을 찍어도 돼?
A. 가능은 하지만 의미가 불명확하고 불안정해지기 쉬워 지양한다.

Q. API 응답 후에는 뭘 테스트해야 해?
A. 데이터 표시, ErrorState, EmptyState, Loading 제거 같은 사용자 상태를 검증한다.

# 5. Snapshot Review Rules

## 5.1 Snapshot Update Rule

### [개념]

Snapshot Update Rule은 Snapshot이 실패했을 때 무조건 업데이트하지 않고 변경 의도를 검토해야 한다는 규칙이다.

Snapshot update는 코드 변경 리뷰와 같은 수준으로 검토해야 한다.

### [핵심]

- snapshot update
- intentional change
- unintentional change
- review diff
- update snapshot caution
- regression
- test review
- commit diff

### [실무]

Snapshot 실패 시 Flow:

```text
Snapshot Test 실패
→ diff 확인
→ 의도된 UI/구조 변경인지 확인
→ 의도된 변경이면 snapshot update
→ 의도되지 않은 변경이면 코드 수정
→ snapshot diff를 PR/commit에서 리뷰
```

무조건 업데이트하면 위험한 경우:

```text
버튼 accessible name이 사라짐
label 연결이 사라짐
error message가 사라짐
중요 action button이 제거됨
route config가 바뀜
보안 관련 menu가 노출됨
```

권장:

- snapshot update는 자동 반사 작업이 아님
- snapshot diff를 반드시 읽음
- 큰 snapshot diff는 테스트 구조 개선 신호
- 자주 깨지는 snapshot은 제거 또는 축소
- snapshot 변경 이유를 commit message에 남김

### [FAQ]

Q. Snapshot이 실패하면 바로 업데이트하면 돼?
A. 안 된다. diff를 확인하고 의도된 변경인지 먼저 검토해야 한다.

Q. Snapshot update가 위험한 이유는?
A. 실제 회귀를 무심코 새로운 기준으로 저장해 버릴 수 있기 때문이다.

Q. Snapshot diff가 너무 크면 어떻게 해?
A. Snapshot을 줄이거나 의미 있는 assertion으로 대체하는 것이 좋다.

## 5.2 Snapshot Diff Review

### [개념]

Snapshot Diff Review는 Snapshot 변경 내역에서 의미 있는 UI/구조 변경과 노이즈를 구분해 검토하는 과정이다.

리뷰하기 어려운 Snapshot은 좋은 Snapshot이 아니다.

### [핵심]

Review 대상:

- removed element
- changed accessible name
- changed text
- added button
- removed button
- changed href
- changed aria attribute
- changed role
- exposed secret
- unstable id
- dynamic class

### [실무]

중요하게 봐야 하는 diff:

```text
button text 변경
link href 변경
input label 제거
dialog role 제거
aria-expanded 제거
error message 제거
loading message 제거
admin menu 노출
```

노이즈 가능성이 높은 diff:

```text
자동 생성 className
랜덤 id
날짜/시간
정렬 순서 불안정
테스트 환경별 속성
```

권장:

- 접근성 관련 diff는 특히 주의
- 동적 값은 Snapshot 대상에서 제거
- 불안정한 className Snapshot 지양
- 중요한 요소는 Snapshot보다 직접 assertion
- secret/token 포함 여부 확인

### [FAQ]

Q. Snapshot diff에서 무엇을 가장 주의해야 해?
A. accessible name, role, label, href, 중요 버튼/메시지 제거 같은 사용자 영향이 큰 변경이다.

Q. className diff는 중요해?
A. 스타일 회귀와 관련될 수 있지만 대부분 Snapshot에서는 노이즈가 되기 쉽다. 목적에 따라 판단한다.

Q. Snapshot에 token이 들어가면?
A. 즉시 제거해야 한다. 테스트 데이터에 실제 token이나 secret이 포함되면 안 된다.

# 6. Snapshot Data Stability

## 6.1 Dynamic Value Caution

### [개념]

Dynamic Value Caution은 날짜, 시간, 랜덤 값, 자동 생성 id, locale 의존 값이 Snapshot을 불안정하게 만들 수 있음을 주의하는 규칙이다.

Snapshot 대상은 안정적인 값이어야 한다.

### [핵심]

불안정한 값:

- Date.now
- new Date
- Math.random
- crypto.randomUUID
- generated id
- locale-dependent text
- timezone-dependent date
- random className
- order unstable array
- environment value

### [실무]

나쁜 예:

```tsx
test("현재 시간 snapshot", () => {
  expect({
    createdAt: new Date().toISOString(),
  }).toMatchSnapshot();
});
```

개선:

```tsx
test("날짜 formatter 결과를 검증한다", () => {
  expect(formatDate("2026-07-06")).toBe("2026.07.06");
});
```

랜덤 id 문제:

```text
snapshot에 매번 다른 id가 들어감
→ 테스트가 계속 실패
→ id를 mock하거나 snapshot 대상에서 제외
```

권장:

- 동적 값은 인자로 주입
- 날짜는 고정 입력 사용
- 랜덤 값은 mock 또는 제거
- 정렬 순서가 불안정하면 정렬 후 비교
- Snapshot 대상은 deterministic 해야 함

### [FAQ]

Q. Snapshot이 매번 바뀌는 이유는?
A. 날짜, 랜덤 id, 자동 생성 className 같은 동적 값이 포함되었을 수 있다.

Q. 날짜가 포함된 Snapshot은 어떻게 처리해?
A. 날짜를 고정 입력으로 만들거나 명시 assertion으로 검증한다.

Q. 랜덤 id는 Snapshot에 넣어도 돼?
A. 권장하지 않는다. mock하거나 비교 대상에서 제외한다.

## 6.2 CSS-in-JS and ClassName Caution

### [개념]

CSS-in-JS and ClassName Caution은 자동 생성 className이 Snapshot을 불안정하게 만들 수 있음을 주의하는 규칙이다.

스타일 구현 세부사항보다 사용자 상태와 접근성 상태를 우선 검증한다.

### [핵심]

주의 대상:

- generated className
- CSS-in-JS hash
- styled-components class
- emotion class
- CSS module hash
- Tailwind long class
- implementation detail
- style snapshot
- visual regression

### [실무]

나쁜 예:

```tsx
expect(container).toMatchSnapshot();
```

Snapshot diff:

```text
class="css-a1b2c3"
→ class="css-d4e5f6"
```

대체:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeEnabled();
expect(screen.getByRole("button", { name: "저장" })).toBeInTheDocument();
```

상태 스타일이 중요할 경우:

```tsx
expect(screen.getByRole("button", { name: "저장" })).toBeDisabled();
expect(screen.getByRole("tab", { name: "공지" })).toHaveAttribute(
  "aria-selected",
  "true",
);
```

권장:

- className Snapshot 지양
- 상태는 disabled / aria-selected / aria-expanded로 검증
- 시각 회귀는 visual regression 도구 고려
- CSS-in-JS hash 변경을 테스트 실패 원인으로 만들지 않음
- 스타일 자체보다 사용자에게 전달되는 상태 검증

### [FAQ]

Q. className Snapshot은 왜 불안정해?
A. CSS-in-JS나 빌드 설정에 따라 자동 생성 className이 바뀔 수 있기 때문이다.

Q. 스타일이 깨지는 건 어떻게 테스트해?
A. 단위 테스트보다는 visual regression이나 E2E, 디자인 시스템 테스트가 더 적합할 수 있다.

Q. active 스타일은 className으로 테스트해도 돼?
A. 가능하지만 tab, nav 같은 UI는 aria-selected나 aria-current가 더 의미 있는 검증이다.

# 7. Snapshot and Accessibility

## 7.1 Snapshot Does Not Guarantee Accessibility

### [개념]

Snapshot은 DOM 구조 변경을 보여줄 수 있지만 접근성 보장을 하지 않는다.

접근성은 role, accessible name, label 연결, keyboard, focus, ARIA 상태를 직접 검증해야 한다.

### [핵심]

Snapshot으로 부족한 항목:

- accessible name correctness
- keyboard navigation
- focus management
- label connection
- error description connection
- focus trap
- aria state sync
- screen reader context
- semantic intent

### [실무]

나쁜 예:

```tsx
test("LoginForm snapshot", () => {
  const { container } = render(<LoginForm />);

  expect(container).toMatchSnapshot();
});
```

좋은 예:

```tsx
test("LoginForm은 접근 가능한 입력 요소를 제공한다", () => {
  render(<LoginForm />);

  expect(screen.getByLabelText("이메일")).toBeInTheDocument();
  expect(screen.getByLabelText("비밀번호")).toBeInTheDocument();
  expect(screen.getByRole("button", { name: "로그인" })).toBeInTheDocument();
});
```

Keyboard:

```tsx
test("로그인 Form은 Tab으로 이동할 수 있다", async () => {
  const user = userEvent.setup();

  render(<LoginForm />);

  await user.tab();
  expect(screen.getByLabelText("이메일")).toHaveFocus();

  await user.tab();
  expect(screen.getByLabelText("비밀번호")).toHaveFocus();
});
```

권장:

- 접근성 검증은 getByRole / getByLabelText 우선
- Snapshot으로 접근성 테스트를 대체하지 않음
- dialog / form / navigation은 별도 접근성 테스트
- axe는 Snapshot보다 접근성 검증에 적합한 보조 도구

### [FAQ]

Q. Snapshot에 label이 보이면 접근성 OK야?
A. 아니다. label이 실제 input과 연결되어 있는지 getByLabelText로 확인해야 한다.

Q. Snapshot으로 keyboard 접근성을 확인할 수 있어?
A. 없다. user.tab, user.keyboard, toHaveFocus로 직접 검증해야 한다.

Q. 접근성 테스트는 Snapshot 대신 뭘 써?
A. getByRole, getByLabelText, userEvent keyboard, aria assertion, axe를 사용한다.

## 7.2 Snapshot and ARIA Caution

### [개념]

Snapshot에 ARIA 속성이 포함되어 있어도 실제 상태와 동기화되는지 보장하지 않는다.

ARIA 상태는 사용자 행동 후 실제 UI 상태와 함께 검증해야 한다.

### [핵심]

ARIA 상태:

- aria-expanded
- aria-selected
- aria-current
- aria-invalid
- aria-describedby
- aria-busy
- aria-modal
- role alert
- role status
- state sync

### [실무]

나쁜 예:

```tsx
expect(container).toMatchSnapshot();
```

좋은 예:

```tsx
test("아코디언 열림 상태와 aria-expanded가 일치한다", async () => {
  const user = userEvent.setup();

  render(<Accordion title="상세 정보">내용</Accordion>);

  const button = screen.getByRole("button", { name: "상세 정보" });

  expect(button).toHaveAttribute("aria-expanded", "false");

  await user.click(button);

  expect(button).toHaveAttribute("aria-expanded", "true");
  expect(screen.getByText("내용")).toBeInTheDocument();
});
```

Form error:

```tsx
expect(screen.getByLabelText("이메일")).toHaveAttribute("aria-invalid", "true");
expect(screen.getByText("이메일을 입력해 주세요.")).toHaveAttribute(
  "id",
  "email-error",
);
```

권장:

- ARIA는 직접 assertion으로 검증
- 사용자 이벤트 후 상태 변경 검증
- 시각 상태와 ARIA 상태가 일치해야 함
- Snapshot에 ARIA가 있다고 안심하지 않음

### [FAQ]

Q. Snapshot에 aria-expanded가 있으면 충분해?
A. 아니다. 클릭 후 true/false가 실제 상태와 함께 변경되는지 테스트해야 한다.

Q. ARIA 상태는 어떻게 테스트해?
A. userEvent로 상태를 바꾸고 toHaveAttribute로 aria 속성을 확인한다.

Q. aria 속성이 많으면 Snapshot으로 보는 게 편하지 않아?
A. 편해 보여도 상태 동기화를 검증하지 못하므로 직접 assertion이 더 안전하다.

# 8. Snapshot and Visual Regression

## 8.1 Snapshot vs Visual Regression

### [개념]

Snapshot Test는 DOM 구조를 비교하고 Visual Regression Test는 실제 렌더링된 화면 이미지를 비교한다.

UI 시각 회귀를 잡고 싶다면 DOM Snapshot보다 Visual Regression 도구가 더 적합할 수 있다.

### [핵심]

| 기준             | Snapshot Test        | Visual Regression                |
| ---------------- | -------------------- | -------------------------------- |
| 비교 대상        | DOM / object 구조    | 렌더링 이미지                    |
| 시각적 차이 감지 | 낮음                 | 높음                             |
| 사용자 행동 검증 | 낮음                 | 낮음~중간                        |
| 접근성 검증      | 낮음                 | 낮음                             |
| 적합 대상        | 작은 구조 변경       | 디자인 회귀                      |
| 도구 예          | Jest/Vitest Snapshot | Chromatic, Playwright screenshot |

### [실무]

DOM Snapshot이 잡기 어려운 것:

```text
색상 변경
간격 깨짐
아이콘 위치 어긋남
반응형 레이아웃 깨짐
폰트 크기 변경
overflow 문제
```

Visual Regression이 잡기 쉬운 것:

```text
버튼 색상 변경
카드 정렬 깨짐
Modal 위치 오류
모바일 layout 깨짐
디자인 시스템 token 변경 영향
```

주의:

```text
Visual Regression도 사용자 행동과 접근성을 대체하지 않음
```

권장:

- DOM Snapshot으로 시각 회귀를 잡으려 하지 않음
- 디자인 회귀는 Storybook + Chromatic 또는 Playwright screenshot 고려
- Functional Test와 Visual Test 역할 분리
- 시각 테스트도 flaky 요소 제거 필요

### [FAQ]

Q. Snapshot Test로 디자인 깨짐을 잡을 수 있어?
A. 일부 구조 변경은 감지할 수 있지만 실제 시각 회귀는 Visual Regression 도구가 더 적합하다.

Q. Visual Regression Test는 기능 테스트를 대체해?
A. 아니다. 시각 차이 감지용이며 사용자 행동 검증은 별도 테스트가 필요하다.

Q. CSS 변경을 Snapshot으로 잡는 게 좋아?
A. 대부분 권장하지 않는다. CSS 변경은 시각 테스트나 상태 assertion으로 관리하는 것이 좋다.

## 8.2 Storybook Snapshot Caution

### [개념]

Storybook Snapshot은 Storybook story를 기반으로 Component 구조 또는 화면을 비교하는 방식이다.

Storybook은 시각 상태 관리에 유용하지만 Snapshot 남용은 여전히 유지보수 문제를 만든다.

### [핵심]

- Storybook
- Story Snapshot
- Chromatic
- visual regression
- component states
- design system
- snapshot caution
- story coverage
- visual diff

### [실무]

Storybook에 적합한 상태:

```text
Default
Hover
Disabled
Loading
Error
Empty
Long Text
Mobile
Dark Mode
```

Snapshot보다 좋은 활용:

```text
Storybook story로 상태 문서화
Chromatic으로 visual regression 확인
RTL test로 behavior 검증
axe addon으로 accessibility 보조 검증
```

주의:

```text
Story Snapshot만 있으면 사용자가 클릭 가능한지 알 수 없음
Story Snapshot만 있으면 keyboard 접근성 확인 불가
Story Snapshot만 있으면 API 상태 전환 확인 부족
```

권장:

- Storybook은 상태 문서화와 시각 회귀에 활용
- behavior는 RTL test로 검증
- Snapshot은 작고 안정적인 story에 제한
- 큰 story snapshot 자동 업데이트 지양

### [FAQ]

Q. Storybook Snapshot은 좋은 테스트야?
A. 상태 문서화에는 도움이 되지만 behavior와 접근성 테스트를 대체하지는 못한다.

Q. Storybook에는 어떤 상태를 만들어야 해?
A. default, loading, error, empty, disabled, long text, responsive 같은 주요 상태가 좋다.

Q. Storybook과 RTL Test는 역할이 달라?
A. 다르다. Storybook은 시각 상태와 문서화에 강하고 RTL은 사용자 행동 검증에 강하다.

# 9. Snapshot Security Rules

## 9.1 Sensitive Data in Snapshot

### [개념]

Sensitive Data in Snapshot은 Snapshot 파일에 실제 token, secret, 개인정보, 운영 URL, 결제 정보가 저장되는 문제를 방지하는 규칙이다.

Snapshot은 저장 파일이므로 테스트 데이터 보안 기준을 반드시 지켜야 한다.

### [핵심]

금지 대상:

- real access token
- real refresh token
- API key
- OAuth secret
- production secret
- personal email
- phone number
- address
- payment card
- real user data
- production URL
- private file path
- internal server detail

### [실무]

나쁜 예:

```tsx
expect({
  accessToken: "real-production-token",
  email: "real-user@example.com",
}).toMatchSnapshot();
```

좋은 예:

```tsx
expect({
  accessToken: "test-access-token",
  email: "test@example.com",
}).toMatchInlineSnapshot(`
  {
    "accessToken": "test-access-token",
    "email": "test@example.com",
  }
`);
```

Snapshot 리뷰 시 확인:

```text
token 문자열 포함 여부
실제 이메일 포함 여부
전화번호 / 주소 포함 여부
운영 API URL 포함 여부
서버 내부 error detail 포함 여부
개인 파일 경로 포함 여부
```

권장:

- Snapshot에는 더미 데이터만 사용
- 실제 사용자 응답을 그대로 snapshot 저장 금지
- 운영 환경 값이 들어오는 테스트 지양
- snapshot 파일도 코드 리뷰 대상
- secret scanner에 걸릴 수 있는 값 금지

### [FAQ]

Q. Snapshot에 실제 token이 들어가면 안 돼?
A. 절대 안 된다. Snapshot 파일은 저장되고 공유될 수 있으므로 더미 token만 사용한다.

Q. 실제 이메일은 Snapshot에 넣어도 돼?
A. 권장하지 않는다. `test@example.com` 같은 더미 이메일을 사용한다.

Q. Snapshot도 보안 검토 대상이야?
A. 그렇다. Snapshot 파일에 민감정보가 저장될 수 있으므로 검토해야 한다.

## 9.2 Snapshot File Review

### [개념]

Snapshot File Review는 `.snap` 파일 또는 inline snapshot 변경사항을 코드 변경과 함께 검토하는 과정이다.

Snapshot 파일은 테스트 코드의 일부로 취급해야 한다.

### [핵심]

- .snap file
- inline snapshot
- code review
- sensitive data review
- diff review
- accidental update
- generated file caution
- test artifact

### [실무]

리뷰 체크:

```md
- [ ] 변경된 snapshot이 의도된 결과인가?
- [ ] diff가 사람이 이해 가능한가?
- [ ] 민감정보가 포함되지 않았는가?
- [ ] accessible name / role / label이 사라지지 않았는가?
- [ ] 중요한 action button이 사라지지 않았는가?
- [ ] 동적 값이 snapshot에 포함되지 않았는가?
- [ ] snapshot이 너무 커지지 않았는가?
```

권장:

- `.snap` 파일을 자동 생성물이라고 무시하지 않음
- inline snapshot도 코드 리뷰
- Snapshot 변경 이유 확인
- 큰 snapshot 변경은 테스트 방식 개선 신호
- 민감정보 발견 시 snapshot 제거 및 secret rotation 검토

### [FAQ]

Q. .snap 파일은 리뷰해야 해?
A. 해야 한다. Snapshot 파일도 테스트 기준을 저장하는 코드의 일부다.

Q. Snapshot 파일은 자동 생성이라 신경 안 써도 돼?
A. 아니다. 자동 생성되더라도 변경 기준을 사람이 검토해야 한다.

Q. Snapshot에 민감정보가 들어갔으면?
A. 즉시 제거하고 노출 범위에 따라 secret 교체나 이력 정리가 필요할 수 있다.

# 10. Snapshot Troubleshooting

## 10.1 Snapshot Changes Too Often

### [개념]

Snapshot Changes Too Often은 Snapshot이 자주 실패하고 자주 업데이트되는 상황이다.

대부분 Snapshot 대상이 너무 크거나 동적 값이 포함되었거나 테스트가 구현 세부사항에 의존한다는 신호다.

### [핵심]

원인:

- large DOM snapshot
- dynamic value
- generated className
- random id
- date/time
- unstable order
- environment-dependent output
- broad snapshot target
- implementation detail

### [실무]

Debug Flow:

```text
Snapshot 자주 변경
→ diff 확인
→ 동적 값 포함 여부 확인
→ DOM이 너무 큰지 확인
→ className/hash 포함 여부 확인
→ 정렬 순서 불안정 확인
→ snapshot 범위 축소
→ meaningful assertion으로 대체
```

개선 전:

```tsx
expect(container).toMatchSnapshot();
```

개선 후:

```tsx
expect(screen.getByRole("heading", { name: "축제 목록" })).toBeInTheDocument();
expect(screen.getByRole("button", { name: "검색" })).toBeInTheDocument();
```

권장:

- Snapshot 범위 축소
- 동적 값 제거
- className 의존 제거
- object field를 명시 assertion으로 전환
- 자주 바뀌는 Snapshot은 삭제 검토

### [FAQ]

Q. Snapshot이 자주 바뀌면 어떻게 해?
A. 동적 값과 큰 DOM을 제거하고 의미 있는 assertion으로 대체하는 것이 좋다.

Q. 자주 업데이트하는 Snapshot은 괜찮아?
A. 좋지 않다. 테스트 신뢰도가 낮아지고 회귀를 놓치기 쉽다.

Q. Snapshot을 줄이는 기준은 뭐야?
A. 사람이 diff를 읽고 의미를 이해할 수 있는 크기여야 한다.

## 10.2 Snapshot Diff Unreadable

### [개념]

Snapshot Diff Unreadable은 Snapshot 실패 diff가 너무 크거나 노이즈가 많아 변경 의미를 파악하기 어려운 상황이다.

읽기 어려운 Snapshot은 테스트 가치가 낮다.

### [핵심]

원인:

- full page snapshot
- deeply nested DOM
- generated className
- too much markup
- duplicated content
- unstable attributes
- noisy diff
- low signal

### [실무]

개선 Flow:

```text
Diff가 읽기 어려움
→ Snapshot 제거 검토
→ Component 단위로 쪼개기
→ 핵심 role/text assertion 작성
→ 작은 object snapshot으로 대체
→ visual regression 필요 여부 검토
```

나쁜 Snapshot 대상:

```text
전체 App
전체 Page
API 응답 전체 원본
큰 Form 전체 DOM
복잡한 Table 전체 DOM
```

대체 assertion:

```tsx
expect(
  screen.getByRole("heading", { name: "관리자 페이지" }),
).toBeInTheDocument();
expect(screen.getByRole("button", { name: "사용자 검색" })).toBeInTheDocument();
expect(screen.getByRole("table", { name: "사용자 목록" })).toBeInTheDocument();
```

권장:

- diff를 읽을 수 없으면 Snapshot 가치 낮음
- 큰 구조는 의미 있는 assertion으로 분해
- 동일한 정보가 반복되는 snapshot 지양
- Snapshot 리뷰 시간이 과도하면 제거 검토

### [FAQ]

Q. Snapshot diff가 너무 길면 어떻게 해?
A. Snapshot을 줄이거나 의미 있는 assertion으로 대체한다.

Q. 읽기 어려운 Snapshot도 회귀 방지에는 도움 되지 않아?
A. 실제로는 무심코 업데이트하기 쉬워 회귀 방지 효과가 낮다.

Q. 큰 Table Snapshot은 좋은가?
A. 대부분 좋지 않다. 핵심 column, row, action만 의미 있게 검증하는 것이 좋다.

## 10.3 Snapshot Fails After Dependency Update

### [개념]

Snapshot Fails After Dependency Update는 React, Testing Library, UI Library, CSS-in-JS, Icon Library 업데이트 후 Snapshot이 대량으로 실패하는 상황이다.

의존성 업데이트에 따른 정상 구조 변경인지 실제 회귀인지 구분해야 한다.

### [핵심]

원인:

- React rendering change
- Testing Library output change
- UI library markup change
- CSS-in-JS hash change
- icon markup change
- aria attribute change
- dependency update
- snapshot mass failure

### [실무]

Debug Flow:

```text
의존성 업데이트 후 Snapshot 대량 실패
→ 어떤 dependency가 변경되었는지 확인
→ diff 유형 분류
→ class/hash 변경인지 확인
→ role/aria 변경인지 확인
→ 사용자 기능 테스트 통과 여부 확인
→ 의도된 변경이면 snapshot update
→ 접근성/기능 회귀면 코드 수정
```

주의 깊게 볼 diff:

```text
role 제거
aria-label 제거
button이 div로 변경
input label 연결 변경
disabled 속성 제거
href 변경
```

노이즈 가능성:

```text
class hash 변경
icon svg path 변경
data attribute 변경
내부 wrapper 추가
```

권장:

- dependency update PR에서 snapshot diff를 분리 리뷰
- 대량 Snapshot 실패는 snapshot 남용 신호일 수 있음
- 중요 기능은 Behavior Test 결과 확인
- 구조 변화가 의미 없는 snapshot은 제거 검토

### [FAQ]

Q. 의존성 업데이트 후 Snapshot이 대량 실패하면 전부 업데이트해도 돼?
A. 바로 업데이트하지 말고 diff 유형을 분류하고 실제 기능/접근성 회귀가 없는지 확인해야 한다.

Q. UI 라이브러리 업데이트로 DOM이 바뀌면?
A. 의도된 변경일 수 있지만 role, label, aria 상태가 유지되는지 검증해야 한다.

Q. 이 상황을 줄이려면?
A. 큰 DOM Snapshot을 줄이고 사용자 관점 assertion을 늘리는 것이 좋다.

# 11. Snapshot Anti Pattern

## 11.1 Common Snapshot Anti Patterns

### [개념]

Snapshot Anti Pattern은 Snapshot을 과도하게 사용하거나 사용자 행동 검증을 대체해 테스트 신뢰도를 낮추는 잘못된 방식이다.

### [핵심]

Anti Pattern:

- snapshot-only test
- full page snapshot
- large DOM snapshot
- interaction snapshot
- async snapshot
- accessibility snapshot
- className snapshot
- dynamic value snapshot
- unreviewed update
- actual user data snapshot
- secret in snapshot
- snapshot for implementation detail
- snapshot instead of assertion
- snapshot update without diff review

### [실무]

나쁜 예:

```tsx
test("renders correctly", () => {
  const { container } = render(<App />);

  expect(container).toMatchSnapshot();
});
```

좋은 예:

```tsx
test("App은 주요 navigation과 main 영역을 표시한다", () => {
  render(<App />);

  expect(
    screen.getByRole("navigation", { name: "주요 메뉴" }),
  ).toBeInTheDocument();
  expect(screen.getByRole("main")).toBeInTheDocument();
});
```

나쁜 예:

```tsx
test("error snapshot", async () => {
  vi.mocked(getData).mockRejectedValue(new Error("failed"));

  const { container } = render(<Page />);

  await waitFor(() => expect(container).toMatchSnapshot());
});
```

좋은 예:

```tsx
test("조회 실패 시 오류 메시지와 다시 시도 버튼을 표시한다", async () => {
  vi.mocked(getData).mockRejectedValue({
    response: {
      status: 500,
    },
  });

  render(<Page />);

  expect(await screen.findByRole("alert")).toHaveTextContent(
    "서버 오류가 발생했습니다.",
  );
  expect(screen.getByRole("button", { name: "다시 시도" })).toBeInTheDocument();
});
```

### [FAQ]

Q. Snapshot Anti Pattern의 대표 사례는 뭐야?
A. 전체 Page를 snapshot-only로 테스트하고 실패하면 diff 검토 없이 업데이트하는 것이다.

Q. Snapshot으로 접근성을 검증하면 안 돼?
A. 접근성은 role, label, keyboard, focus, ARIA assertion으로 직접 검증해야 한다.

Q. Snapshot은 아예 쓰지 말아야 해?
A. 아니다. 작고 안정적인 구조에 보조적으로 사용할 수 있다.

# 12. Snapshot Testing Checklist

## 12.1 Snapshot Testing Checklist

### [개념]

Snapshot Testing Checklist는 Snapshot 사용이 적절하고 유지보수 가능한지 검수하는 기준이다.

Snapshot은 테스트 의도를 흐리지 않고, 사람이 리뷰 가능한 크기여야 한다.

### [핵심]

Checklist:

```md
- [ ] Snapshot이 필요한 테스트인가?
- [ ] Behavior Test로 대체할 수 없는가?
- [ ] Snapshot-only Test가 아닌가?
- [ ] Snapshot 대상이 작고 안정적인가?
- [ ] Snapshot diff를 사람이 쉽게 리뷰할 수 있는가?
- [ ] 동적 값(Date, Random, generated id)이 제거되었는가?
- [ ] generated className 중심 Snapshot이 아닌가?
- [ ] 실제 token / secret / 개인정보가 포함되지 않았는가?
- [ ] 접근성 검증을 Snapshot으로 대체하지 않았는가?
- [ ] interaction 결과를 Snapshot으로만 검증하지 않았는가?
- [ ] async 상태를 Snapshot으로만 검증하지 않았는가?
- [ ] Snapshot 실패 시 diff를 리뷰하는가?
- [ ] Snapshot 변경 이유가 명확한가?
- [ ] 자주 깨지는 Snapshot은 제거 또는 축소했는가?
```

### [실무]

Agent Snapshot Test 판단 Flow:

```text
Test Request
→ Can assert user-visible result?
→ Yes: use Behavior Test

No
→ Is output small and stable?
→ No: avoid Snapshot

Yes
→ Is diff reviewable?
→ No: avoid Snapshot

Yes
→ Use inline snapshot or small snapshot
→ Add explicit assertions for important behavior
→ Review security data
```

Snapshot 사용 전 질문:

```text
이 Snapshot을 실패했을 때 사람이 읽을 수 있는가?
이 Snapshot이 사용자 기능을 검증하는가?
이 Snapshot을 무심코 업데이트할 위험이 큰가?
명시 assertion이 더 낫지 않은가?
```

### [FAQ]

Q. Snapshot Testing Checklist의 핵심은 뭐야?
A. Snapshot이 작고 안정적이며 리뷰 가능하고 Behavior Test를 대체하지 않는지 확인하는 것이다.

Q. Snapshot을 쓰기 전 가장 먼저 물어볼 질문은?
A. 이 테스트를 사용자 visible assertion으로 더 명확하게 작성할 수 있는지 확인해야 한다.

Q. 자주 깨지는 Snapshot은 어떻게 해?
A. 동적 값을 제거하거나 Snapshot을 줄이고, 필요하면 명시 assertion으로 대체한다.

# 13. Part13 Summary

## 13.1 Snapshot Test Caution Final Rule

### [개념]

Frontend Testing Part13은 Snapshot Test의 한계와 사용 기준을 정의한다.

이 Part의 목적은 Agent가 Snapshot을 남용하지 않고, 사용자 행동과 접근성 중심 테스트를 우선하도록 만드는 것이다.

### [핵심]

최종 기준:

- Snapshot은 보조 수단이다.
- Snapshot-only Test는 금지한다.
- Behavior Test가 Snapshot보다 우선이다.
- 사용자 visible result는 직접 assertion으로 검증한다.
- Form, Router, Auth, API State, Accessibility는 Snapshot보다 명시 테스트가 적합하다.
- 큰 DOM Snapshot과 Page 전체 Snapshot은 지양한다.
- Interaction 결과를 Snapshot으로만 검증하지 않는다.
- Async UI 상태를 Snapshot으로만 검증하지 않는다.
- Inline Snapshot은 작고 안정적인 object에 제한적으로 사용한다.
- Snapshot diff는 반드시 리뷰한다.
- Snapshot update는 의도된 변경일 때만 수행한다.
- 동적 값과 generated className은 Snapshot에서 제거한다.
- Snapshot에 실제 token, secret, 개인정보를 포함하지 않는다.
- 접근성은 role, label, keyboard, focus, ARIA assertion으로 검증한다.
- 시각 회귀는 DOM Snapshot보다 Visual Regression 도구를 고려한다.

### [실무]

Agent 작업 Flow:

```text
Snapshot Test Request
→ Check Behavior Assertion Alternative
→ Avoid Snapshot-only
→ Keep Snapshot Small
→ Remove Dynamic Values
→ Add Explicit User-visible Assertion
→ Review Accessibility Separately
→ Review Snapshot Diff
→ Check Sensitive Data
```

Part14 이후 연결:

```text
Part13 Snapshot Test Caution
→ Part14 Test Structure
→ Part15 Troubleshooting
→ Part16 Frontend Testing Review
→ Part17 Final Frontend Testing Rules
```

### [FAQ]

Q. Part13의 최종 목적은 뭐야?
A. Frontend Agent가 Snapshot Test를 남용하지 않고 사용자 행동, 접근성, 명시 assertion 중심으로 테스트하게 만드는 것이다.

Q. Snapshot Test에서 가장 중요한 규칙은 뭐야?
A. Snapshot은 보조 수단이며 Snapshot-only Test를 작성하지 않는 것이다.

Q. Part13 다음에는 어떤 내용이 이어져야 해?
A. 테스트 파일 구조, render utility, fixture, naming, setup 기준을 정의하는 Test Structure 기준이 이어지는 것이 좋다.

# Retrieval Queries

### [FAQ]

Q. Snapshot Test는 뭐야?
A. 이전에 저장한 렌더링 결과나 객체 구조와 현재 결과를 비교하는 테스트다.

Q. Snapshot Test만으로 UI 테스트를 대체할 수 있어?
A. 아니다. 사용자의 행동과 화면 결과를 검증하는 Behavior Test가 우선이다.

Q. Snapshot Test는 언제 유용해?
A. 작고 안정적인 출력 구조의 변경 감지나 정적인 결과 비교에 보조적으로 유용하다.

Q. Snapshot Test의 핵심 역할은 뭐야?
A. 예기치 않은 구조 변경을 감지하는 보조 역할이다.

Q. Snapshot이 통과하면 UI가 정상이라고 봐도 돼?
A. 아니다. 사용자 행동, 접근성, 상태 흐름은 별도 테스트가 필요하다.

Q. Snapshot 실패는 항상 버그야?
A. 아니다. 의도된 UI 변경일 수 있으므로 변경 내용을 리뷰해야 한다.

Q. Snapshot보다 Behavior Test가 우선인 이유는?
A. 사용자가 실제로 보는 결과와 수행하는 행동이 테스트의 핵심이기 때문이다.

Q. Snapshot-only Test는 왜 안 좋아?
A. 테스트 의도가 불명확하고 사용자 기능이 실제로 동작하는지 알기 어렵기 때문이다.

Q. React Testing Library에서는 어떤 테스트가 좋아?
A. role, label, text, userEvent를 사용해 사용자 관점 결과를 검증하는 테스트가 좋다.

Q. Form 테스트에 Snapshot을 써도 돼?
A. 권장하지 않는다. 입력, 제출, 오류 메시지를 userEvent와 assertion으로 검증하는 것이 좋다.

Q. 정적인 Component에는 Snapshot을 써도 돼?
A. 가능하지만 visible assertion을 우선하고 Snapshot은 보조로만 사용하는 것이 좋다.

Q. 큰 DOM Snapshot은 왜 피해야 해?
A. diff가 크고 의미를 파악하기 어려워 무심코 업데이트하기 쉽기 때문이다.

Q. Inline Snapshot은 언제 좋아?
A. 작고 안정적인 객체 결과를 테스트 파일 안에서 바로 확인하고 싶을 때 좋다.

Q. toEqual과 inline snapshot 중 뭐가 좋아?
A. 작은 객체는 toEqual이 더 명확할 때가 많고, 구조 변경 감지에는 inline snapshot이 유용할 수 있다.

Q. Presentational Component에 Snapshot을 써도 돼?
A. 작고 정적인 Component에는 보조적으로 사용할 수 있다.

Q. visible assertion 없이 snapshot만 두면 안 돼?
A. 권장하지 않는다. 사용자에게 무엇이 보여야 하는지 명확히 검증해야 한다.

Q. Schema나 Config Snapshot은 UI Snapshot보다 나아?
A. 작고 정적인 구조라면 diff가 명확해 유용할 수 있다.

Q. Route config snapshot은 언제 유용해?
A. 공개 Route나 메뉴 구성이 의도치 않게 바뀌는 것을 감지하고 싶을 때 유용하다.

Q. Page 전체 Snapshot은 왜 안 좋아?
A. diff가 크고 의미가 불명확해 실제 기능 회귀를 잡기 어렵기 때문이다.

Q. 큰 UI 변경 감지는 어떻게 해?
A. 핵심 사용자 결과 assertion과 필요 시 visual regression tool을 사용하는 것이 좋다.

Q. 클릭 후 Snapshot으로 결과를 확인하면 안 돼?
A. 권장하지 않는다. 사용자가 보는 구체적인 결과를 assertion으로 확인해야 한다.

Q. Modal 열림은 Snapshot보다 뭘 테스트해야 해?
A. dialog role, title, content, 닫기 버튼, focus 상태를 테스트하는 것이 좋다.

Q. 비동기 UI를 Snapshot으로 테스트하면 안 돼?
A. 권장하지 않는다. 성공, 실패, 빈 상태를 사용자 UI assertion으로 검증하는 것이 좋다.

Q. waitFor 안에서 snapshot을 찍어도 돼?
A. 가능은 하지만 의미가 불명확하고 불안정해지기 쉬워 지양한다.

Q. Snapshot이 실패하면 바로 업데이트하면 돼?
A. 안 된다. diff를 확인하고 의도된 변경인지 먼저 검토해야 한다.

Q. Snapshot update가 위험한 이유는?
A. 실제 회귀를 무심코 새로운 기준으로 저장해 버릴 수 있기 때문이다.

Q. Snapshot diff에서 무엇을 가장 주의해야 해?
A. accessible name, role, label, href, 중요 버튼/메시지 제거 같은 사용자 영향이 큰 변경이다.

Q. Snapshot이 매번 바뀌는 이유는?
A. 날짜, 랜덤 id, 자동 생성 className 같은 동적 값이 포함되었을 수 있다.

Q. 날짜가 포함된 Snapshot은 어떻게 처리해?
A. 날짜를 고정 입력으로 만들거나 명시 assertion으로 검증한다.

Q. className Snapshot은 왜 불안정해?
A. CSS-in-JS나 빌드 설정에 따라 자동 생성 className이 바뀔 수 있기 때문이다.

Q. 스타일이 깨지는 건 어떻게 테스트해?
A. 단위 테스트보다는 visual regression이나 E2E, 디자인 시스템 테스트가 더 적합할 수 있다.

Q. Snapshot에 label이 보이면 접근성 OK야?
A. 아니다. label이 실제 input과 연결되어 있는지 getByLabelText로 확인해야 한다.

Q. Snapshot으로 keyboard 접근성을 확인할 수 있어?
A. 없다. user.tab, user.keyboard, toHaveFocus로 직접 검증해야 한다.

Q. 접근성 테스트는 Snapshot 대신 뭘 써?
A. getByRole, getByLabelText, userEvent keyboard, aria assertion, axe를 사용한다.

Q. Snapshot에 aria-expanded가 있으면 충분해?
A. 아니다. 클릭 후 true/false가 실제 상태와 함께 변경되는지 테스트해야 한다.

Q. Snapshot Test로 디자인 깨짐을 잡을 수 있어?
A. 일부 구조 변경은 감지할 수 있지만 실제 시각 회귀는 Visual Regression 도구가 더 적합하다.

Q. Visual Regression Test는 기능 테스트를 대체해?
A. 아니다. 시각 차이 감지용이며 사용자 행동 검증은 별도 테스트가 필요하다.

Q. Storybook Snapshot은 좋은 테스트야?
A. 상태 문서화에는 도움이 되지만 behavior와 접근성 테스트를 대체하지는 못한다.

Q. Snapshot에 실제 token이 들어가면 안 돼?
A. 절대 안 된다. Snapshot 파일은 저장되고 공유될 수 있으므로 더미 token만 사용한다.

Q. .snap 파일은 리뷰해야 해?
A. 해야 한다. Snapshot 파일도 테스트 기준을 저장하는 코드의 일부다.

Q. Snapshot이 자주 바뀌면 어떻게 해?
A. 동적 값과 큰 DOM을 제거하고 의미 있는 assertion으로 대체하는 것이 좋다.

Q. Snapshot diff가 너무 길면 어떻게 해?
A. Snapshot을 줄이거나 의미 있는 assertion으로 대체한다.

Q. 의존성 업데이트 후 Snapshot이 대량 실패하면 전부 업데이트해도 돼?
A. 바로 업데이트하지 말고 diff 유형을 분류하고 실제 기능/접근성 회귀가 없는지 확인해야 한다.

Q. Snapshot Anti Pattern의 대표 사례는 뭐야?
A. 전체 Page를 snapshot-only로 테스트하고 실패하면 diff 검토 없이 업데이트하는 것이다.

Q. Snapshot Testing Checklist의 핵심은 뭐야?
A. Snapshot이 작고 안정적이며 리뷰 가능하고 Behavior Test를 대체하지 않는지 확인하는 것이다.

Q. Part13 Snapshot Test Caution의 최종 목표는 뭐야?
A. Frontend Agent가 Snapshot Test를 남용하지 않고 사용자 행동, 접근성, 명시 assertion 중심으로 테스트하게 만드는 것이다.
