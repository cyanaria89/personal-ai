# TypeScript Foundation Part01 - Overview and Runtime Model

---

# 1. TypeScript Overview

## 1.1 TypeScript Definition

### [개념]

TypeScript는 JavaScript에 Static Type System을 추가한 언어다.

TypeScript Code는 Browser나 Node.js Runtime에서 직접 실행되는 것이 아니라, Compile 과정을 거쳐 JavaScript Code로 변환된 뒤 실행된다.

```text
TypeScript Code
→ Type Check
→ Compile
→ JavaScript Code
→ Runtime Execution
```

TypeScript의 핵심 목적은 Runtime 동작을 바꾸는 것이 아니라 Compile Time 단계에서 Type Error를 미리 발견하는 것이다.

---

### [핵심]

- TypeScript는 JavaScript Superset이다.
- TypeScript는 Static Type System을 제공한다.
- TypeScript Type은 Compile Time에 검사된다.
- TypeScript Type은 Runtime에 존재하지 않는다.
- TypeScript Code는 JavaScript Code로 Compile된다.
- Browser는 TypeScript Type을 실행하지 않는다.
- TypeScript는 Runtime Error를 완전히 제거하지 않는다.
- TypeScript는 API Response Type, Props Type, State Type 관리에 유용하다.
- Frontend Agent는 TypeScript를 사용해 Type Safe Frontend Code를 생성해야 한다.

---

### [실무]

2026 실무 기준에서 TypeScript는 Frontend 개발의 기본 선택지에 가깝다.

특히 React Frontend에서는 아래 영역에서 효과가 크다.

- API Response 구조 고정
- Request Body Type 정의
- Component Props Type 정의
- Form Data Type 정의
- Event Handler Type 정의
- State Type 정의
- null / undefined Error 방어
- 잘못된 Property 접근 방지
- Refactoring 안정성 향상
- 자동완성 품질 향상
- 협업 코드 리뷰 품질 향상

TypeScript Foundation 문서는 문법 암기 문서가 아니라 Frontend Agent가 안전한 TypeScript Code를 생성하고 검토하기 위한 RAG 문서다.

---

### [FAQ]

Q. TypeScript는 JavaScript와 다른 언어야?
A. TypeScript는 JavaScript에 정적 타입 시스템을 추가한 언어다. 최종 실행 코드는 JavaScript다.

Q. TypeScript는 Browser에서 직접 실행돼?
A. 아니다. TypeScript는 JavaScript로 Compile된 뒤 Browser에서 실행된다.

Q. TypeScript를 쓰면 Runtime Error가 없어져?
A. 아니다. Compile Time Type Error를 줄여주지만 Runtime Error를 완전히 제거하지는 않는다.

Q. TypeScript Foundation 문서는 사람 공부용이야?
A. 아니다. Frontend Agent가 타입 안정성이 있는 코드를 생성하고 검토하기 위한 RAG 문서다.

---

# 2. Compile Time and Runtime

## 2.1 Compile Time Type Check

### [개념]

Compile Time Type Check는 TypeScript가 코드를 JavaScript로 변환하기 전에 Type이 올바른지 검사하는 과정이다.

예:

```typescript
const count: number = "10";
```

위 코드는 TypeScript Type Check 단계에서 오류가 발생한다.

```text
Type 'string' is not assignable to type 'number'
```

이 오류는 Runtime에서 발생하는 JavaScript Error가 아니라 Compile Time Type Error다.

---

### [핵심]

- Compile Time은 코드 실행 전 검사 단계다.
- TypeScript Type Error는 Compile Time에 발생한다.
- TypeScript는 잘못된 Type Assignment를 감지한다.
- TypeScript는 잘못된 Function Parameter Type을 감지한다.
- TypeScript는 잘못된 Property Access를 감지할 수 있다.
- Type Check는 Runtime Validation을 대체하지 않는다.
- 외부 API Response는 Compile Time Type만으로 신뢰할 수 없다.

---

### [실무]

Frontend Agent는 Compile Time Type Check를 활용해 아래 문제를 사전에 방지해야 한다.

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function renderFestival(festival: Festival): string {
  return festival.name;
}
```

문제:

- `Festival` Type에는 `name` property가 없다.
- 올바른 property는 `title`이다.

개선:

```typescript
function renderFestival(festival: Festival): string {
  return festival.title;
}
```

실무 기준:

- Backend DTO와 Frontend Type 정합성 유지
- API Response Type 정의
- Props Type 정의
- nullable field 명시
- Function Parameter Type 명시
- Type Error 발생 시 실제 데이터 구조 확인

---

### [FAQ]

Q. Compile Time Type Check가 뭐야?
A. TypeScript가 JavaScript로 Compile되기 전에 Type 오류를 검사하는 과정이다.

Q. Type Error는 실행 중 오류야?
A. 대부분 TypeScript Type Error는 실행 전 Compile Time에 발견되는 오류다.

Q. Compile Time Type Check만 있으면 API 응답도 안전해?
A. 아니다. 외부 API 응답은 Runtime Data이므로 별도 검증이 필요할 수 있다.

---

## 2.2 Runtime Execution

### [개념]

Runtime Execution은 Compile된 JavaScript Code가 실제 Browser 또는 Node.js에서 실행되는 단계다.

TypeScript Type은 Runtime에 존재하지 않는다.

```typescript
type User = {
  id: number;
  name: string;
};

const user: User = {
  id: 1,
  name: "jun",
};
```

Compile 후 Runtime에는 Type 정보가 제거된다.

```javascript
const user = {
  id: 1,
  name: "jun",
};
```

---

### [핵심]

- Runtime에는 JavaScript만 실행된다.
- TypeScript Type 정보는 Compile 후 제거된다.
- `type`, `interface`는 Runtime에 존재하지 않는다.
- Runtime Data는 TypeScript Type만으로 검증되지 않는다.
- API Response, localStorage, user input은 Runtime 검증이 필요할 수 있다.
- TypeScript는 Runtime Validation Tool이 아니다.

---

### [실무]

API 응답을 Type만으로 단정하면 위험하다.

위험 예:

```typescript
type User = {
  id: number;
  name: string;
};

const user = response as User;
console.log(user.name);
```

문제:

- `response`가 실제로 `User` 구조인지 검증하지 않는다.
- `as User`는 TypeScript에게 강제로 믿게 만드는 Type Assertion이다.
- Runtime Data가 잘못되면 오류가 발생할 수 있다.

개선 방향:

```typescript
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}

if (isUser(response)) {
  console.log(response.name);
}
```

실무 기준:

- 외부 데이터는 `unknown`으로 받고 검증 후 사용
- API Response Type과 Backend DTO 정합성 유지
- 중요한 데이터는 Runtime Validation 고려
- Type Assertion 남용 금지

---

### [FAQ]

Q. TypeScript Type은 Runtime에도 남아?
A. 아니다. Compile 후 Type 정보는 제거되고 JavaScript만 실행된다.

Q. type과 interface는 JavaScript로 변환돼?
A. 아니다. type과 interface는 Type Check에만 사용되고 Runtime Code에는 남지 않는다.

Q. API Response를 Type으로 정의하면 자동 검증돼?
A. 아니다. Type 정의는 Compile Time 기준이고 실제 API Response 검증은 별도로 필요하다.

---

# 3. JavaScript vs TypeScript

## 3.1 JavaScript and TypeScript Difference

### [개념]

JavaScript는 Dynamic Type Language다.

TypeScript는 JavaScript에 Static Type System을 추가한다.

```text
JavaScript
→ Runtime 중심 Type 판단

TypeScript
→ Compile Time Type Check + JavaScript Runtime
```

JavaScript는 실행 중 값의 Type이 결정된다.
TypeScript는 코드 작성 단계에서 Type 오류를 미리 확인할 수 있다.

---

### [핵심]

| 비교               | JavaScript       | TypeScript                   |
| ------------------ | ---------------- | ---------------------------- |
| Type System        | Dynamic Type     | Static Type                  |
| Type Check 시점    | Runtime          | Compile Time                 |
| Browser 실행       | 직접 실행        | JavaScript로 Compile 후 실행 |
| API Type 관리      | 직접 관리 어려움 | Type 정의 가능               |
| Props Type 관리    | 별도 도구 필요   | Type 정의 가능               |
| Refactoring 안정성 | 낮음             | 높음                         |
| Runtime Error 제거 | 불가             | 완전 제거 불가               |
| 학습 난이도        | 낮음             | JavaScript보다 높음          |

---

### [실무]

JavaScript 예:

```javascript
function formatPrice(price) {
  return price.toLocaleString() + "원";
}

formatPrice("10000");
```

문제:

- `price`가 number인지 string인지 명확하지 않다.
- Runtime에서 예상과 다른 결과가 나올 수 있다.

TypeScript 개선:

```typescript
function formatPrice(price: number): string {
  return `${price.toLocaleString()}원`;
}

formatPrice(10000);
```

효과:

- `price`는 number만 허용된다.
- 잘못된 인자를 Compile Time에 감지한다.
- return type이 string임을 명확히 한다.

---

### [FAQ]

Q. JavaScript만 써도 개발 가능해?
A. 가능하다. 하지만 규모가 커질수록 TypeScript가 안정성, 자동완성, 리팩토링에 유리하다.

Q. TypeScript는 JavaScript를 대체해?
A. 아니다. TypeScript는 JavaScript 위에 Type System을 추가하고 최종적으로 JavaScript로 실행된다.

Q. TypeScript를 배우려면 JavaScript를 먼저 알아야 해?
A. 그렇다. TypeScript는 JavaScript 기반이므로 JavaScript 문법과 Runtime 이해가 필요하다.

---

# 4. TypeScript Runtime Misunderstanding

## 4.1 Type Does Not Change Runtime

### [개념]

TypeScript Type은 Runtime 동작을 변경하지 않는다.

아래 코드는 TypeScript에서 Type을 지정하지만 Runtime 값 변환은 하지 않는다.

```typescript
const price: number = Number("10000");
```

`number` Type Annotation은 값을 number로 바꾸는 기능이 아니다.
실제 변환은 `Number()` 함수가 수행한다.

---

### [핵심]

- Type Annotation은 Runtime 변환이 아니다.
- `: number`는 값을 숫자로 바꾸지 않는다.
- `: string`은 값을 문자열로 바꾸지 않는다.
- TypeScript Type은 Runtime Data를 자동 변환하지 않는다.
- Runtime 변환은 JavaScript 함수로 처리해야 한다.
- API Response 값 변환은 Mapping Function에서 처리한다.

---

### [실무]

잘못된 이해:

```typescript
const price: number = "10000" as unknown as number;
```

문제:

- 실제 Runtime 값은 string일 수 있다.
- Type Assertion으로 Type Check만 우회한다.
- 숫자 계산 시 버그가 발생할 수 있다.

올바른 변환:

```typescript
function parsePrice(value: string): number {
  return Number(value);
}
```

API Mapping 예:

```typescript
type FestivalResponse = {
  eventStartDate: string;
};

type FestivalViewModel = {
  eventStartDate: Date;
};

function toFestivalViewModel(response: FestivalResponse): FestivalViewModel {
  return {
    eventStartDate: new Date(response.eventStartDate),
  };
}
```

실무 기준:

- Type 정의와 Runtime 변환을 구분
- API Response Type과 화면 ViewModel Type 분리 가능
- 날짜 string은 필요 시 Date로 명시적 변환
- 숫자 string은 Number로 명시적 변환

---

### [FAQ]

Q. `const count: number = value`는 value를 number로 바꿔?
A. 아니다. Type Annotation은 Runtime 변환을 하지 않는다.

Q. API에서 받은 날짜 string을 Type에서 Date로 쓰면 자동 변환돼?
A. 아니다. JSON 날짜는 대부분 string으로 받고 필요하면 `new Date()`로 변환해야 한다.

Q. Type Assertion을 쓰면 Runtime 값도 바뀌어?
A. 아니다. Type Assertion은 TypeScript 검사만 우회할 뿐 Runtime 값은 바뀌지 않는다.

---

# 5. TypeScript Use Cases in Frontend

## 5.1 Frontend Type Safety

### [개념]

Frontend Type Safety는 화면 코드에서 사용하는 데이터 구조를 Type으로 고정하여 잘못된 접근과 상태 오류를 줄이는 방식이다.

TypeScript는 Frontend에서 아래 데이터 흐름을 안전하게 만든다.

```text
API Response
→ Type Definition
→ Component Props
→ State
→ Event Handler
→ UI Rendering
```

---

### [핵심]

Frontend TypeScript 주요 사용 영역:

- API Request Type
- API Response Type
- Error Response Type
- Component Props Type
- React State Type
- React Event Type
- Form Data Type
- Route Parameter Type
- Utility Function Type
- Async Status Type
- Nullable Data Handling

---

### [실무]

API Response Type 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
  eventEndDate: string;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

Component Props Type 예:

```typescript
type FestivalCardProps = {
  festival: FestivalInfoResponse;
  onClick: (festivalId: number) => void;
};

function FestivalCard({ festival, onClick }: FestivalCardProps) {
  return null;
}
```

실무 기준:

- Backend Response DTO와 Frontend Response Type 일치
- nullable field는 `string | null`처럼 명시
- 목록 응답은 `T[]`로 명시
- 공통 응답 wrapper는 Generic으로 재사용
- Props Type은 Component 입력 계약으로 관리

---

### [FAQ]

Q. Frontend에서 TypeScript가 가장 많이 쓰이는 곳은?
A. API Response Type, Component Props Type, State Type, Event Handler Type이다.

Q. API Response Type은 왜 중요해?
A. 서버 응답 구조를 고정해 화면 코드에서 잘못된 property 접근을 줄일 수 있기 때문이다.

Q. Props Type은 왜 필요해?
A. Component가 어떤 데이터를 받아야 하는지 명확히 하고 잘못된 props 전달을 막기 위해 필요하다.

---

# 6. TypeScript Adoption Criteria

## 6.1 When TypeScript Is Useful

### [개념]

TypeScript는 코드 규모가 커지고 데이터 구조가 복잡해질수록 효과가 커진다.

특히 여러 명이 작업하는 Frontend Project에서는 Type Definition이 코드 계약 역할을 한다.

---

### [핵심]

TypeScript 효과가 큰 상황:

- API Response 구조가 복잡한 경우
- Backend DTO가 자주 변경되는 경우
- React Component Props가 많은 경우
- Form Data가 복잡한 경우
- 상태 값이 여러 형태를 가지는 경우
- null / undefined 오류가 자주 발생하는 경우
- 팀 협업 프로젝트
- Refactoring이 자주 발생하는 프로젝트
- Frontend Agent가 코드를 생성하고 Review Agent가 검토해야 하는 프로젝트

---

### [실무]

TypeScript 우선 적용 영역:

```text
1. API Response Type
2. API Request Type
3. Component Props Type
4. Function Parameter Type
5. React Event Type
6. React State Type
7. Error Response Type
8. Utility Function Type
```

JavaScript에서 TypeScript로 전환할 때는 모든 코드를 한 번에 바꾸지 않아도 된다.

권장 Migration Flow:

```text
JavaScript File
→ Rename to TypeScript
→ Fix Syntax Error
→ Add Function Parameter Type
→ Add Props Type
→ Add API Type
→ Remove any
→ Enable Strict Rules Gradually
```

---

### [FAQ]

Q. TypeScript는 작은 프로젝트에도 필요해?
A. 필수는 아니지만 API 연동, Props, Form이 있는 프로젝트라면 작은 규모에서도 도움이 된다.

Q. JS 프로젝트를 한 번에 TS로 바꿔야 해?
A. 아니다. API Type, Props Type, Function Parameter부터 점진적으로 적용하는 것이 안전하다.

Q. Migration에서 가장 먼저 타입을 붙일 곳은?
A. API Response, Props, Function Parameter, Event Handler, State Type부터 적용하는 것이 좋다.

---

# 7. Common Mistakes

## 7.1 TypeScript Overview Mistakes

### [개념]

TypeScript 초기에 자주 발생하는 실수는 Type과 Runtime을 혼동하는 것이다.

TypeScript는 Type Check 도구이지 Runtime Data를 자동으로 보정하는 도구가 아니다.

---

### [핵심]

자주 발생하는 실수:

- TypeScript Type이 Runtime에 남는다고 오해
- Type Annotation이 값 변환을 한다고 오해
- API Response가 Type 정의대로 온다고 단정
- `as` Type Assertion으로 검증 우회
- `any`로 Type Error 숨김
- JSON 날짜 값을 Date로 단정
- nullable field를 string으로 단정
- Backend DTO 변경 후 Frontend Type 미수정
- Type Error를 무조건 Type Assertion으로 해결
- Runtime Validation 없이 외부 입력 신뢰

---

### [실무]

나쁜 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string;
};

function getImageUrl(festival: Festival): string {
  return festival.imageUrl;
}
```

문제:

- 실제 API에서 `imageUrl`이 null일 수 있다면 Type이 잘못되었다.
- Runtime에서 이미지 처리 오류가 발생할 수 있다.

개선:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

function getImageUrl(festival: Festival): string {
  return festival.imageUrl ?? "/default-image.png";
}
```

실무 기준:

- 실제 API Response Body 확인
- nullable field를 Type에 반영
- 기본값 처리
- Type Assertion보다 Type Definition 수정 우선
- Runtime Data와 Type Definition 정합성 유지

---

### [FAQ]

Q. TypeScript 초보가 가장 많이 하는 실수는?
A. Type과 Runtime을 혼동하고 any 또는 Type Assertion으로 오류를 숨기는 것이다.

Q. API Type은 맞는데 화면에서 undefined가 나와?
A. 실제 API Response 구조와 Frontend Type 정의가 다를 수 있다. Network Response Body를 확인해야 한다.

Q. Type Error는 무조건 as로 해결해도 돼?
A. 아니다. Type Assertion은 검증을 우회하므로 실제 Type 정의와 데이터 구조를 먼저 확인해야 한다.

---

# 8. Review Checklist

## 8.1 Part01 Checklist

### [개념]

TypeScript Foundation Part01 검수는 TypeScript의 역할, Compile Time, Runtime, JavaScript와의 차이, Frontend 적용 기준을 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] TypeScript가 JavaScript Superset임을 설명했는가?
- [ ] Static Type System을 설명했는가?
- [ ] Compile Time Type Check를 설명했는가?
- [ ] Runtime에는 Type 정보가 없음을 설명했는가?
- [ ] TypeScript Code가 JavaScript로 Compile됨을 설명했는가?
- [ ] Type Annotation이 Runtime 변환이 아님을 설명했는가?
- [ ] API Response는 Runtime 검증이 필요할 수 있음을 설명했는가?
- [ ] JavaScript vs TypeScript 비교가 포함되었는가?
- [ ] Frontend TypeScript 사용 영역이 포함되었는가?
- [ ] API Response Type 예제가 포함되었는가?
- [ ] Props Type 예제가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Required Section Check
→ Runtime Model Check
→ Frontend Use Case Check
→ Code Example Check
→ Common Mistake Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

Part01은 이후 Type Annotation, Type Inference, Basic Type, Object Type, API Type 문서의 기반이 되어야 한다.

---

### [FAQ]

Q. Part01에서 가장 중요한 검수 기준은?
A. TypeScript Type이 Compile Time 전용이며 Runtime에는 JavaScript만 실행된다는 점이 명확해야 한다.

Q. Part01이 이후 문서와 어떻게 연결돼?
A. Type Annotation, Type Inference, API Response Type, Props Type, Type Error Debugging의 전제 지식을 제공한다.

---

# Retrieval Queries

### [FAQ]

Q. TypeScript가 뭐야?
A. TypeScript는 JavaScript에 Static Type System을 추가한 언어이며 Compile 후 JavaScript로 실행된다.

Q. TypeScript는 JavaScript랑 뭐가 달라?
A. JavaScript는 Runtime 중심 Dynamic Type이고 TypeScript는 Compile Time Type Check를 제공한다.

Q. TypeScript는 Browser에서 직접 실행돼?
A. 아니다. TypeScript는 JavaScript로 Compile된 뒤 Browser에서 실행된다.

Q. TypeScript Type은 Runtime에도 남아?
A. 아니다. Type 정보는 Compile 후 제거되고 Runtime에는 JavaScript만 실행된다.

Q. type과 interface는 Runtime에 존재해?
A. 아니다. type과 interface는 Type Check에만 사용되고 JavaScript Runtime에는 남지 않는다.

Q. TypeScript를 쓰면 Runtime Error가 없어져?
A. 아니다. Compile Time Type Error를 줄여주지만 Runtime Error를 완전히 제거하지는 않는다.

Q. Compile Time Type Check가 뭐야?
A. TypeScript가 JavaScript로 Compile되기 전에 Type 오류를 검사하는 과정이다.

Q. Runtime Execution이 뭐야?
A. Compile된 JavaScript Code가 Browser 또는 Node.js에서 실제로 실행되는 단계다.

Q. Type Annotation은 값을 변환해?
A. 아니다. Type Annotation은 Type Check용이며 Runtime 값 변환을 하지 않는다.

Q. `: number`를 쓰면 문자열이 숫자로 바뀌어?
A. 아니다. 문자열을 숫자로 바꾸려면 `Number()` 같은 Runtime 변환 함수가 필요하다.

Q. API Response Type을 정의하면 응답이 자동 검증돼?
A. 아니다. Type 정의는 Compile Time 기준이고 실제 API Response는 Runtime Data이므로 별도 검증이 필요할 수 있다.

Q. Type Assertion은 Runtime 값을 바꿔?
A. 아니다. Type Assertion은 TypeScript 검사만 우회할 뿐 Runtime 값은 바꾸지 않는다.

Q. TypeScript에서 as를 쓰면 안전해?
A. 아니다. 검증 없이 Type을 강제로 믿게 만들 수 있어 남용하면 위험하다.

Q. Frontend에서 TypeScript는 어디에 많이 써?
A. API Response Type, API Request Type, Component Props Type, State Type, Event Handler Type에 많이 쓴다.

Q. API Response Type은 왜 중요해?
A. 서버 응답 구조를 Type으로 고정해 잘못된 property 접근과 화면 오류를 줄일 수 있기 때문이다.

Q. Props Type은 왜 필요해?
A. Component가 받아야 하는 데이터 구조를 명확히 하고 잘못된 props 전달을 막기 위해 필요하다.

Q. JavaScript 프로젝트를 TypeScript로 바꾸려면 어디부터 해?
A. API Response Type, Props Type, Function Parameter Type, Event Handler Type, State Type부터 점진적으로 적용하는 것이 좋다.

Q. TypeScript Migration Flow는?
A. JavaScript File → Rename to TypeScript → Fix Syntax Error → Add Function Parameter Type → Add Props Type → Add API Type → Remove any → Enable Strict Rules Gradually.

Q. TypeScript 초보가 가장 많이 하는 실수는?
A. Type과 Runtime을 혼동하고 any 또는 Type Assertion으로 Type Error를 숨기는 것이다.

Q. API Type은 맞는데 화면에서 undefined가 나와?
A. 실제 API Response 구조와 Frontend Type 정의가 다를 수 있다. Network Response Body와 Backend DTO를 확인해야 한다.

Q. JSON 날짜는 Date Type으로 받아?
A. 대부분 JSON 응답에서는 string으로 받고 필요하면 Frontend에서 Date로 변환한다.

Q. nullable API field는 어떻게 Type으로 표현해?
A. `string | null`, `number | null`처럼 Union Type으로 표현한다.

Q. TypeScript Foundation Part01의 핵심은 뭐야?
A. TypeScript는 Compile Time Type Check를 제공하지만 Runtime에는 JavaScript만 실행된다는 점이다.

Q. TypeScript Foundation 다음 학습 문서는 뭐야?
A. Type Annotation, Type Inference, Basic Type, Object Type, Union Type, Function Type, API Type 순서가 적합하다.
