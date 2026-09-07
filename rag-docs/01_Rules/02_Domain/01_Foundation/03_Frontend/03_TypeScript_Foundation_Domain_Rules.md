# TypeScript Foundation Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

TypeScript Foundation Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- TypeScript 기본 문법 이해
- JavaScript 코드에 Type System 적용 지원
- Frontend 코드 안정성 향상
- React TypeScript 코드 작성 기반 제공
- API Request / Response Type 정의 지원
- Component Props Type 정의 지원
- Event Handler Type 정의 지원
- State Type 정의 지원
- Type Error 원인 분석 지원
- JavaScript에서 TypeScript 전환 기준 제공

---

### [핵심]

우선순위:

1. TypeScript Basic Type
2. Type Inference
3. Type Annotation
4. Object Type
5. Array Type
6. Function Type
7. Union Type
8. Interface / Type Alias
9. Generic Basics
10. API Response Type
11. React TypeScript Readiness
12. Type Error Debugging

---

### [실무]

2026 실무 기준에서 TypeScript Foundation 문서는 타입 문법 암기용 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- JavaScript 코드를 TypeScript로 전환
- Props Type 정의
- API Response Type 정의
- Form Data Type 정의
- Event Handler Type 정의
- Utility Function Type 정의
- null / undefined Type Error 방어
- React Component Type 기반 작성
- Type Error 원인 분석
- 안전한 Frontend 코드 생성

---

### [FAQ]

Q. TypeScript Foundation 문서는 사람 공부용 문서야?

A.
아니다. Frontend Agent가 타입 안정성이 있는 JavaScript / React 코드를 생성하고 검토하기 위한 RAG 문서다.

Q. TypeScript는 JavaScript와 다른 언어야?

A.
TypeScript는 JavaScript에 정적 타입 시스템을 추가한 언어다. 최종적으로 JavaScript로 컴파일되어 실행된다.

Q. TypeScript Foundation에서 가장 중요한 기준은 뭐야?

A.
Basic Type, Object Type, Function Type, Union Type, Interface, Type Alias, Generic, API Response Type이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

TypeScript Foundation 문서는 Frontend TypeScript 기본 코드 작성에 필요한 범위를 포함한다.

포함 범위:

- TypeScript Overview
- Type Annotation
- Type Inference
- Primitive Type
- Array Type
- Tuple Type
- Object Type
- Optional Property
- Readonly Property
- Union Type
- Literal Type
- Type Alias
- Interface
- Function Type
- Optional Parameter
- Default Parameter
- Return Type
- Void
- Unknown
- Never
- Any
- Null / Undefined
- Type Narrowing
- Type Guard
- Generic Basics
- Utility Type Basics
- Enum / Union Alternative
- API Request Type
- API Response Type
- Error Response Type
- React Props Type Basics
- React Event Type Basics
- tsconfig Basics
- Type Error Debugging
- JavaScript to TypeScript Migration Basics

---

### [핵심]

반드시 포함:

- TypeScript는 JavaScript Runtime을 바꾸지 않음
- TypeScript Type은 Compile Time에 검사됨
- Runtime에는 Type 정보가 사라짐
- Type Annotation은 명시적 타입 지정
- Type Inference는 자동 타입 추론
- `any` 남용 금지
- API Response는 반드시 Type으로 정의
- React Component Props는 Type 정의 권장
- null / undefined 가능성은 명시적으로 처리

---

### [실무]

TypeScript Foundation은 React TypeScript 문서의 기반이다.

실무 연결:

```text
JavaScript Foundation
→ TypeScript Foundation
→ React Core
→ React Component Design
→ Data Fetching & REST API Integration
→ Frontend Architecture
```

---

### [FAQ]

Q. TypeScript 문서에서 React를 깊게 다뤄?

A.
아니다. React Props, Event Type 같은 기초 연결만 다루고 React Hook 심화는 React 문서에서 다룬다.

Q. TypeScript Backend도 여기서 다뤄?

A.
아니다. 이 문서는 Frontend Foundation 목적이므로 Frontend TypeScript 중심으로 작성한다.

Q. TypeScript 고급 타입도 포함해?

A.
기초 Utility Type과 Generic Basics만 포함한다. Conditional Type, Mapped Type 심화는 Advanced 문서로 분리한다.

---

## 2.2 Excluded Scope

### [개념]

TypeScript Foundation 문서에서는 고급 Type System과 Framework 심화를 제외한다.

제외 범위:

- React Hook Type 심화
- Next.js Type 심화
- Advanced Generic
- Conditional Type 심화
- Mapped Type 심화
- Template Literal Type 심화
- Type-Level Programming
- Declaration File 심화
- Library Type Definition 제작
- Node.js Backend TypeScript 심화
- Express / NestJS TypeScript
- Build Tool 설정 심화
- Monorepo TypeScript 설정
- TypeScript Compiler API

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- React / Frontend Architecture / Advanced TypeScript 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- TypeScript 기본 적용 능력에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
TypeScript Foundation
→ React TypeScript
→ Frontend Architecture
→ Advanced TypeScript
→ Monorepo / Design System
```

---

### [FAQ]

Q. Conditional Type은 여기서 다뤄?

A.
아니다. Foundation에서는 언급 정도만 가능하고 심화는 Advanced TypeScript 문서에서 다룬다.

Q. TypeScript Compiler 설정을 깊게 다뤄?

A.
아니다. tsconfig 기본 옵션만 다루고 세부 컴파일러 전략은 별도 문서가 적합하다.

Q. NestJS TypeScript도 여기서 다뤄?

A.
아니다. 이 문서는 Frontend TypeScript Foundation 전용이다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

TypeScript Foundation RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 Frontend 적용 기준
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

Q. 모든 TypeScript 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

TypeScript 문서에는 실무 적용과 검증을 위해 추가 Section을 포함할 수 있다.

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

- Type Narrowing 설명 → [Flow], [예제], [주의]
- Interface / Type Alias 설명 → [Comparison]
- Generic 설명 → [개념], [예제], [FAQ]
- API Response Type 설명 → [실무], [Best Practice]
- Type Error 설명 → [Troubleshooting]

---

### [실무]

예시:

```md
### [Flow]

JavaScript Value
→ Type Definition
→ Type Check
→ Safe Usage
→ Runtime Execution
```

---

### [FAQ]

Q. TypeScript 문서에 Troubleshooting이 필요한 이유는?

A.
Type Error, null 가능성, any 남용, API 타입 불일치, Generic 추론 실패가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
type vs interface, any vs unknown, enum vs union, optional vs nullable처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. TypeScript Core Rules

## 4.1 TypeScript Overview Rules

### [개념]

TypeScript는 JavaScript에 정적 타입 시스템을 추가한 언어다.

TypeScript 코드는 컴파일 과정을 거쳐 JavaScript로 실행된다.

기본 Flow:

```text
TypeScript Code
→ Type Check
→ Compile
→ JavaScript Code
→ Browser Runtime
```

---

### [핵심]

반드시 설명:

- TypeScript는 JavaScript Superset
- Type은 Compile Time에 검사
- Runtime에는 Type이 존재하지 않음
- TypeScript는 Runtime Error를 완전히 제거하지 않음
- TypeScript는 코드 자동완성, 리팩토링, 안정성에 도움
- Frontend API 연동에서 Response Type 관리에 유용

---

### [실무]

TypeScript는 아래 상황에서 실무 효과가 크다.

- API Response 구조가 복잡한 경우
- Component Props가 많은 경우
- Form Data가 복잡한 경우
- 상태 값이 여러 형태를 가지는 경우
- null / undefined 오류가 자주 발생하는 경우
- 대규모 Frontend 코드베이스
- 팀 협업 프로젝트

---

### [FAQ]

Q. TypeScript를 쓰면 Runtime Error가 없어져?

A.
아니다. TypeScript는 Compile Time 타입 오류를 줄여주지만 Runtime Error를 완전히 제거하지는 않는다.

Q. TypeScript Type은 브라우저에서 실행돼?

A.
아니다. Type 정보는 컴파일 후 제거되고 JavaScript만 실행된다.

Q. TypeScript는 왜 Frontend에서 많이 써?

A.
Component Props, API Response, State, Event Handler의 타입 안정성을 높일 수 있기 때문이다.

---

## 4.2 Type Annotation Rules

### [개념]

Type Annotation은 변수, 함수, 객체에 타입을 명시하는 문법이다.

예:

```typescript
const userName: string = "jun";
let count: number = 0;
const isActive: boolean = true;
```

---

### [핵심]

필수 포함:

- variable type annotation
- function parameter type
- function return type
- object property type
- array type
- optional property
- union type

---

### [실무]

Type Annotation은 필요한 곳에 명확히 작성한다.

권장:

```typescript
function formatPrice(price: number): string {
  return `${price.toLocaleString()}원`;
}
```

불필요한 예:

```typescript
const title: string = "Festival";
```

개선:

```typescript
const title = "Festival";
```

이유:

- TypeScript가 `"Festival"`을 string으로 추론 가능
- 명확한 추론이 가능한 곳은 Type Inference 활용

---

### [FAQ]

Q. 모든 변수에 타입을 직접 써야 해?

A.
아니다. TypeScript가 명확히 추론할 수 있는 값은 Type Inference를 활용한다.

Q. 함수 parameter에는 타입을 써야 해?

A.
대부분 써야 한다. parameter는 TypeScript가 추론하기 어려운 경우가 많다.

Q. 함수 return type은 항상 써야 해?

A.
복잡한 함수, API 함수, public utility 함수에는 명시하는 것이 좋다.

---

## 4.3 Type Inference Rules

### [개념]

Type Inference는 TypeScript가 값과 코드 흐름을 보고 타입을 자동으로 추론하는 기능이다.

예:

```typescript
const title = "Festival";
const count = 3;
const active = true;
```

TypeScript 추론:

```text
title → string
count → number
active → boolean
```

---

### [핵심]

반드시 설명:

- 명확한 초기값은 TypeScript가 타입 추론 가능
- 불필요한 Type Annotation은 생략 가능
- 함수 parameter는 추론이 어려워 명시 필요
- 빈 배열은 타입 추론 주의
- null 초기값은 타입 확장 필요

---

### [실무]

주의 예:

```typescript
const festivals = [];
```

문제:

- 빈 배열은 의도한 element type을 추론하기 어려움

개선:

```typescript
type Festival = {
  id: number;
  title: string;
};

const festivals: Festival[] = [];
```

---

### [FAQ]

Q. Type Inference를 믿어도 돼?

A.
명확한 초기값이 있는 경우 신뢰해도 된다. 다만 빈 배열, null 초기값, 함수 parameter는 명시하는 것이 좋다.

Q. 빈 배열에는 왜 타입을 써야 해?

A.
배열에 어떤 타입의 요소가 들어갈지 TypeScript가 알기 어렵기 때문이다.

Q. Type Annotation과 Type Inference 중 뭐가 좋아?

A.
명확한 추론은 Inference를 활용하고, 외부 입력, 함수 parameter, API Response는 명시한다.

---

# 5. Basic Type Rules

## 5.1 Primitive Type Rules

### [개념]

Primitive Type은 JavaScript 기본 값에 대응하는 TypeScript 타입이다.

---

### [핵심]

필수 포함:

- string
- number
- boolean
- null
- undefined
- symbol
- bigint

예:

```typescript
const title: string = "Festival";
const count: number = 10;
const active: boolean = true;
```

---

### [실무]

실무 사용 기준:

- 문자열 값 → `string`
- 숫자 값 → `number`
- 참/거짓 → `boolean`
- 값 없음 의도 → `null`
- 값 미할당 → `undefined`

주의:

- `String`, `Number`, `Boolean` 객체 타입 사용 지양
- `string`, `number`, `boolean` 소문자 타입 사용
- API 응답의 nullable 값은 명시 필요

---

### [FAQ]

Q. string과 String 차이는?

A.
string은 primitive type이고 String은 객체 wrapper type이다. 실무에서는 string을 사용한다.

Q. number는 정수와 실수를 구분해?

A.
아니다. JavaScript number는 정수와 실수를 모두 표현한다.

Q. null 타입은 언제 써?

A.
의도적으로 값이 없음을 표현해야 할 때 사용한다.

---

## 5.2 Array Type Rules

### [개념]

Array Type은 같은 형태의 여러 값을 담는 배열 타입이다.

예:

```typescript
const names: string[] = ["jun", "kim"];
const scores: number[] = [90, 80, 70];
```

---

### [핵심]

필수 포함:

- `string[]`
- `number[]`
- `Array<T>`
- object array
- readonly array
- empty array annotation

---

### [실무]

객체 배열 예:

```typescript
type Festival = {
  id: number;
  title: string;
};

const festivals: Festival[] = [
  { id: 1, title: "Spring Festival" },
  { id: 2, title: "Summer Festival" },
];
```

API 목록 응답은 대부분 객체 배열로 처리한다.

주의:

- 빈 배열은 타입 명시
- 원본 변경 방지가 필요하면 readonly 고려
- sort, push, splice는 원본 변경
- map / filter 결과 타입 확인

---

### [FAQ]

Q. string[]와 Array<string> 중 뭐가 좋아?

A.
둘 다 가능하다. 일반 배열은 string[] 형태가 간결하고 자주 사용된다.

Q. 객체 배열 타입은 어떻게 정의해?

A.
객체 타입을 type 또는 interface로 정의한 뒤 `Festival[]`처럼 사용한다.

Q. 빈 배열 타입은 왜 명시해야 해?

A.
TypeScript가 요소 타입을 정확히 추론하기 어렵기 때문이다.

---

## 5.3 Tuple Type Rules

### [개념]

Tuple은 길이와 위치별 타입이 정해진 배열 타입이다.

예:

```typescript
const point: [number, number] = [10, 20];
```

---

### [핵심]

필수 포함:

- fixed length array
- position-based type
- readonly tuple
- tuple vs array
- destructuring

---

### [실무]

Tuple은 위치 의미가 명확한 짧은 데이터에 사용한다.

예:

```typescript
type Coordinate = [number, number];

const location: Coordinate = [127.0276, 37.4979];
```

주의:

- 필드 의미가 많아지면 object type이 더 명확함
- 긴 tuple은 가독성 저하
- 위치 순서 실수 주의

---

### [FAQ]

Q. Tuple은 언제 써?

A.
좌표, 쌍 데이터처럼 길이와 위치 의미가 명확한 경우 사용한다.

Q. Tuple 대신 object를 써도 돼?

A.
가능하다. 필드 의미를 명확히 보여줘야 하면 object가 더 좋다.

---

## 5.4 Any Unknown Never Void Rules

### [개념]

`any`, `unknown`, `never`, `void`는 TypeScript의 특수 타입이다.

---

### [핵심]

필수 포함:

- any
- unknown
- never
- void
- type safety
- error handling

정의:

- `any`: 타입 검사를 사실상 비활성화
- `unknown`: 타입을 알 수 없지만 사용 전 검증 필요
- `never`: 발생할 수 없는 값 또는 종료되는 함수
- `void`: 반환값 없음

---

### [실무]

`any` 지양:

```typescript
function parseData(data: any) {
  return data.title;
}
```

개선:

```typescript
function parseData(data: unknown): string {
  if (
    typeof data === "object" &&
    data !== null &&
    "title" in data &&
    typeof data.title === "string"
  ) {
    return data.title;
  }

  return "";
}
```

`void` 예:

```typescript
function logMessage(message: string): void {
  console.log(message);
}
```

---

### [FAQ]

Q. any는 왜 피해야 해?

A.
TypeScript의 타입 검사를 우회해서 오류를 미리 잡기 어렵게 만든다.

Q. unknown은 any랑 뭐가 달라?

A.
unknown은 사용하기 전에 타입 검사가 필요하지만 any는 검사 없이 사용할 수 있다.

Q. void는 언제 써?

A.
반환값이 없는 함수의 return type에 사용한다.

---

# 6. Object Type Rules

## 6.1 Object Type Rules

### [개념]

Object Type은 객체의 property 이름과 타입을 정의하는 방식이다.

예:

```typescript
type User = {
  id: number;
  name: string;
  active: boolean;
};
```

---

### [핵심]

필수 포함:

- property type
- optional property
- readonly property
- nested object
- object array
- index signature basics
- excess property check

---

### [실무]

API Response 객체 타입 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
  region: string;
  imageUrl?: string;
  averageRating: number | null;
};
```

주의:

- optional property와 nullable property 구분
- API 응답 구조와 Type 정의 일치
- 백엔드 DTO 이름과 Frontend Type 이름 정합성 유지
- 화면 전용 타입과 API 타입 분리 가능

---

### [FAQ]

Q. optional property는 어떻게 써?

A.
property 이름 뒤에 `?`를 붙인다. 예: `imageUrl?: string`.

Q. optional과 null은 같은 뜻이야?

A.
아니다. optional은 property가 없을 수 있다는 뜻이고 null은 property는 있지만 값이 null일 수 있다는 뜻이다.

Q. API 응답 타입은 어디에 정의해?

A.
일반적으로 `types`, `models`, `api` 폴더 등 프로젝트 기준 위치에 정의한다.

---

## 6.2 Optional and Nullable Rules

### [개념]

Optional은 property 또는 parameter가 없을 수 있음을 의미한다.

Nullable은 값이 `null`일 수 있음을 의미한다.

---

### [핵심]

필수 포함:

- optional property
- optional parameter
- nullable value
- undefined
- null
- strictNullChecks
- null guard

예:

```typescript
type User = {
  name?: string;
  profileImageUrl: string | null;
};
```

---

### [실무]

차이:

```typescript
type Example = {
  optionalName?: string;
  nullableName: string | null;
};
```

의미:

- `optionalName?: string` → property가 없거나 undefined 가능
- `nullableName: string | null` → property는 있고 값이 null 가능

사용 전 방어:

```typescript
function getProfileImage(url: string | null): string {
  return url ?? "/default-profile.png";
}
```

---

### [FAQ]

Q. `name?: string`과 `name: string | null`은 같아?

A.
아니다. optional은 property 누락 가능성이고 nullable은 값이 null일 가능성이다.

Q. null 가능 값은 어떻게 처리해?

A.
null check, optional chaining, nullish coalescing으로 기본값을 처리한다.

Q. strictNullChecks는 왜 중요해?

A.
null과 undefined 가능성을 타입 단계에서 검사해 런타임 오류를 줄일 수 있다.

---

## 6.3 Readonly Rules

### [개념]

readonly는 property 또는 배열이 직접 변경되지 않도록 제한하는 타입 키워드다.

예:

```typescript
type User = {
  readonly id: number;
  name: string;
};
```

---

### [핵심]

필수 포함:

- readonly property
- readonly array
- immutability
- React state update
- mutation prevention

---

### [실무]

readonly property 예:

```typescript
type Festival = {
  readonly festivalId: number;
  title: string;
};
```

readonly array 예:

```typescript
function getTitles(festivals: readonly Festival[]): string[] {
  return festivals.map((festival) => festival.title);
}
```

주의:

- readonly는 TypeScript 타입 검사 수준의 제한
- Runtime 불변성을 완전히 보장하지 않음
- React State 직접 변경 방지에 도움
- API ID 같은 값에 유용

---

### [FAQ]

Q. readonly를 쓰면 Runtime에서도 값이 안 바뀌어?

A.
아니다. readonly는 TypeScript 타입 검사 단계의 제한이다.

Q. readonly는 언제 쓰면 좋아?

A.
ID, 생성일, 외부에서 변경하면 안 되는 값, 함수 입력 배열을 보호할 때 좋다.

---

# 7. Union and Literal Type Rules

## 7.1 Union Type Rules

### [개념]

Union Type은 값이 여러 타입 중 하나일 수 있음을 표현한다.

예:

```typescript
type Id = number | string;
```

---

### [핵심]

필수 포함:

- union type
- nullable union
- status union
- type narrowing
- discriminated union basics

---

### [실무]

상태 값 예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

let status: RequestStatus = "idle";
```

API nullable 예:

```typescript
type Festival = {
  title: string;
  imageUrl: string | null;
};
```

주의:

- Union Type은 사용 전 narrowing 필요
- 너무 넓은 union은 코드 복잡도 증가
- 상태 값은 string literal union 권장

---

### [FAQ]

Q. Union Type은 언제 써?

A.
값이 여러 타입 또는 여러 상태 중 하나일 수 있을 때 사용한다.

Q. string 대신 literal union을 쓰는 이유는?

A.
허용 가능한 문자열 값을 제한해 오타와 잘못된 상태 값을 줄이기 위해서다.

---

## 7.2 Literal Type Rules

### [개념]

Literal Type은 특정 값만 허용하는 타입이다.

예:

```typescript
type UserRole = "USER" | "ADMIN";
type Theme = "light" | "dark";
```

---

### [핵심]

필수 포함:

- string literal
- number literal
- boolean literal
- status type
- role type
- route type

---

### [실무]

권한 타입 예:

```typescript
type UserRole = "ROLE_USER" | "ROLE_ADMIN";

function canAccessAdmin(role: UserRole): boolean {
  return role === "ROLE_ADMIN";
}
```

요청 상태 예:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

장점:

- 오타 방지
- 자동완성
- 상태 값 제한
- 조건 분기 안정성 증가

---

### [FAQ]

Q. Literal Type은 왜 써?

A.
허용 가능한 값만 사용하도록 제한해 잘못된 문자열이나 상태 값을 방지하기 위해 사용한다.

Q. Role Type은 string으로 두면 안 돼?

A.
가능하지만 literal union으로 제한하면 오타와 잘못된 권한 값을 줄일 수 있다.

---

## 7.3 Discriminated Union Basics

### [개념]

Discriminated Union은 공통 구분 property를 기준으로 여러 객체 형태를 안전하게 구분하는 타입 패턴이다.

---

### [핵심]

필수 포함:

- discriminant property
- status field
- union object
- narrowing
- exhaustive check basics

---

### [실무]

API 상태 예:

```typescript
type ApiState<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; message: string };

function getMessage(state: ApiState<string[]>): string {
  if (state.status === "success") {
    return `${state.data.length} items`;
  }

  if (state.status === "error") {
    return state.message;
  }

  return "Loading...";
}
```

주의:

- 공통 구분 property 이름 통일
- 상태별 필요한 데이터 명확화
- UI 상태 모델링에 유용

---

### [FAQ]

Q. Discriminated Union은 언제 써?

A.
loading, success, error처럼 상태별 데이터 구조가 다른 경우 사용하면 좋다.

Q. status property가 중요한 이유는?

A.
TypeScript가 status 값을 기준으로 안전하게 타입을 좁힐 수 있기 때문이다.

---

# 8. Interface and Type Alias Rules

## 8.1 Type Alias Rules

### [개념]

Type Alias는 타입에 이름을 붙이는 문법이다.

예:

```typescript
type UserId = number;

type User = {
  id: UserId;
  name: string;
};
```

---

### [핵심]

필수 포함:

- primitive alias
- object type
- union type
- function type
- intersection type basics
- reusable type

---

### [실무]

Type Alias 적합 상황:

- Union Type 정의
- Literal Type 정의
- Function Type 정의
- API Response Type 정의
- 화면 상태 Type 정의

예:

```typescript
type RequestStatus = "idle" | "loading" | "success" | "error";

type FestivalCard = {
  id: number;
  title: string;
  imageUrl: string;
};
```

---

### [FAQ]

Q. Type Alias는 언제 써?

A.
Union Type, Literal Type, Function Type, 객체 타입에 이름을 붙여 재사용할 때 쓴다.

Q. type으로 객체 타입도 만들 수 있어?

A.
가능하다. type은 객체 타입 정의에도 사용할 수 있다.

---

## 8.2 Interface Rules

### [개념]

Interface는 객체의 구조를 정의하는 TypeScript 문법이다.

예:

```typescript
interface User {
  id: number;
  name: string;
}
```

---

### [핵심]

필수 포함:

- object shape
- property type
- optional property
- readonly property
- extends
- declaration merging basics
- class implements basics

---

### [실무]

Interface 적합 상황:

- 객체 구조 정의
- Props Type 정의
- 확장 가능한 모델 정의
- Class와 계약 정의

예:

```typescript
interface Festival {
  festivalId: number;
  title: string;
  region: string;
  imageUrl?: string;
}
```

확장 예:

```typescript
interface FestivalDetail extends Festival {
  description: string;
  address: string;
}
```

---

### [FAQ]

Q. Interface는 언제 써?

A.
객체 구조를 정의하고 확장 가능성을 고려할 때 사용한다.

Q. Interface도 optional property를 지원해?

A.
지원한다. property 이름 뒤에 `?`를 붙이면 된다.

---

## 8.3 Type Alias vs Interface Rules

### [개념]

Type Alias와 Interface는 모두 타입에 이름을 붙일 수 있지만 사용 목적과 확장 방식이 다르다.

---

### [핵심]

비교:

| 비교                | Type Alias        | Interface    |
| ------------------- | ----------------- | ------------ |
| 객체 타입           | 가능              | 가능         |
| Union Type          | 가능              | 불가         |
| Literal Type        | 가능              | 불가         |
| 확장                | intersection 사용 | extends 사용 |
| Declaration Merging | 불가              | 가능         |
| Props 정의          | 가능              | 가능         |
| 상태 타입           | 적합              | 제한적       |

---

### [실무]

권장 기준:

- 객체 모델 중심 → interface 가능
- Union / Literal / 상태 타입 → type 권장
- React Props → type 또는 interface 모두 가능
- 팀 컨벤션 우선
- 일관성 유지 중요

예:

```typescript
type Status = "loading" | "success" | "error";

interface User {
  id: number;
  name: string;
}
```

---

### [FAQ]

Q. type과 interface 중 뭐를 써야 해?

A.
객체 구조는 둘 다 가능하다. Union이나 Literal Type이 필요하면 type을 사용한다. 팀 컨벤션이 가장 중요하다.

Q. React Props는 type과 interface 중 뭐가 좋아?

A.
둘 다 가능하다. 프로젝트 컨벤션에 맞춰 일관되게 사용하는 것이 좋다.

---

# 9. Function Type Rules

## 9.1 Function Type Rules

### [개념]

Function Type은 함수의 parameter와 return type을 정의하는 방식이다.

예:

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

---

### [핵심]

필수 포함:

- parameter type
- return type
- optional parameter
- default parameter
- function expression type
- callback type
- void return
- async function return type

---

### [실무]

Utility Function 예:

```typescript
function formatDate(dateText: string): string {
  return new Date(dateText).toLocaleDateString("ko-KR");
}
```

Callback Type 예:

```typescript
type ClickHandler = (id: number) => void;

const handleClick: ClickHandler = (id) => {
  console.log(id);
};
```

Async Function 예:

```typescript
async function fetchFestivals(): Promise<Festival[]> {
  const response = await fetch("/api/festivals");
  return await response.json();
}
```

---

### [FAQ]

Q. 함수 parameter에는 타입을 꼭 써야 해?

A.
대부분 써야 한다. 함수 parameter는 TypeScript가 자동 추론하기 어려운 경우가 많다.

Q. async 함수 return type은 어떻게 써?

A.
`Promise<T>` 형태로 작성한다.

Q. 반환값 없는 함수는 어떤 타입이야?

A.
`void`를 사용한다.

---

## 9.2 Optional Parameter Rules

### [개념]

Optional Parameter는 함수 호출 시 생략할 수 있는 parameter다.

예:

```typescript
function greet(name?: string): string {
  return `Hello ${name ?? "Guest"}`;
}
```

---

### [핵심]

필수 포함:

- optional parameter
- default parameter
- undefined handling
- parameter order
- nullish coalescing

---

### [실무]

권장:

```typescript
function createPageUrl(page: number = 1): string {
  return `/page/${page}`;
}
```

주의:

- optional parameter는 undefined 가능
- 사용 전 기본값 처리
- 필수 parameter 뒤에 배치
- optional 남용 금지

---

### [FAQ]

Q. Optional Parameter는 null도 허용해?

A.
아니다. `name?: string`은 기본적으로 string 또는 undefined를 의미한다. null도 허용하려면 `string | null`을 명시한다.

Q. Optional Parameter와 Default Parameter 차이는?

A.
Optional Parameter는 생략 가능하고, Default Parameter는 생략 시 사용할 기본값을 지정한다.

---

# 10. Type Narrowing Rules

## 10.1 Type Narrowing Rules

### [개념]

Type Narrowing은 Union Type처럼 넓은 타입을 조건문을 통해 더 구체적인 타입으로 좁히는 과정이다.

예:

```typescript
function formatId(id: number | string): string {
  if (typeof id === "number") {
    return id.toString();
  }

  return id;
}
```

---

### [핵심]

필수 포함:

- typeof
- instanceof
- in operator
- equality narrowing
- truthiness narrowing
- custom type guard
- discriminated union narrowing
- null check

---

### [실무]

Object Narrowing 예:

```typescript
type Festival = {
  title: string;
  address?: string;
};

function getAddress(festival: Festival): string {
  if ("address" in festival && festival.address) {
    return festival.address;
  }

  return "주소 없음";
}
```

주의:

- truthy check는 빈 문자열, 0 처리 주의
- nullable 값은 명시적으로 방어
- unknown은 narrowing 후 사용
- API Response는 런타임 검증과 함께 고려

---

### [FAQ]

Q. Type Narrowing은 왜 필요해?

A.
Union Type이나 unknown 값을 안전하게 사용하기 위해 필요하다.

Q. typeof는 언제 써?

A.
string, number, boolean 같은 primitive type을 구분할 때 사용한다.

Q. in operator는 언제 써?

A.
객체에 특정 property가 있는지 확인해 타입을 좁힐 때 사용한다.

---

## 10.2 Type Guard Rules

### [개념]

Type Guard는 값이 특정 타입인지 검사하고 TypeScript에 알려주는 함수 또는 조건이다.

예:

```typescript
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

---

### [핵심]

필수 포함:

- custom type guard
- `value is Type`
- runtime check
- unknown validation
- API response validation basics

---

### [실무]

API 응답 검증 예:

```typescript
type Festival = {
  id: number;
  title: string;
};

function isFestival(value: unknown): value is Festival {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "title" in value
  );
}
```

주의:

- Type Guard는 Runtime 조건과 Type 정의가 일치해야 함
- 복잡한 API Response는 Schema Validation 도구 고려
- 단순 type assertion보다 안전함

---

### [FAQ]

Q. Type Guard는 언제 써?

A.
unknown 값, 외부 API 응답, localStorage 데이터처럼 타입을 확신할 수 없는 값을 사용할 때 쓴다.

Q. `value is Type`은 뭐야?

A.
조건이 true일 때 value가 해당 Type임을 TypeScript에 알려주는 문법이다.

---

# 11. Generic Rules

## 11.1 Generic Basics

### [개념]

Generic은 타입을 parameter처럼 받아 재사용 가능한 타입과 함수를 만드는 문법이다.

예:

```typescript
function identity<T>(value: T): T {
  return value;
}
```

---

### [핵심]

필수 포함:

- generic type parameter
- reusable type
- generic function
- generic interface
- generic type alias
- constraint basics
- API response generic

---

### [실무]

API Response Generic 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

type Festival = {
  id: number;
  title: string;
};

type FestivalResponse = ApiResponse<Festival>;
type FestivalListResponse = ApiResponse<Festival[]>;
```

Generic Function 예:

```typescript
function getFirst<T>(items: T[]): T | undefined {
  return items[0];
}
```

---

### [FAQ]

Q. Generic은 왜 써?

A.
타입은 다르지만 구조가 같은 로직을 재사용하기 위해 사용한다.

Q. Generic의 T는 무슨 뜻이야?

A.
관례적으로 Type을 의미하는 타입 parameter 이름이다. 다른 이름도 사용할 수 있다.

Q. API Response에 Generic을 왜 써?

A.
응답 공통 구조는 유지하고 data 타입만 다르게 재사용할 수 있기 때문이다.

---

## 11.2 Generic Constraint Basics

### [개념]

Generic Constraint는 Generic 타입 parameter가 특정 조건을 만족하도록 제한하는 방식이다.

예:

```typescript
function getId<T extends { id: number }>(item: T): number {
  return item.id;
}
```

---

### [핵심]

필수 포함:

- extends constraint
- key constraint
- safe property access
- reusable function
- generic limitation

---

### [실무]

예:

```typescript
function findById<T extends { id: number }>(
  items: T[],
  id: number,
): T | undefined {
  return items.find((item) => item.id === id);
}
```

장점:

- id property 존재 보장
- 여러 객체 타입에 재사용 가능
- 타입 안정성 유지

주의:

- Constraint를 너무 복잡하게 만들지 않음
- Foundation 문서에서는 기본 constraint만 다룸

---

### [FAQ]

Q. Generic Constraint는 왜 필요해?

A.
Generic 타입에서도 특정 property나 구조가 있음을 보장하기 위해 필요하다.

Q. extends는 class 상속이야?

A.
Generic Constraint에서 extends는 타입이 특정 구조를 만족해야 한다는 의미다.

---

# 12. Utility Type Rules

## 12.1 Utility Type Basics

### [개념]

Utility Type은 기존 타입을 변형해 새 타입을 쉽게 만드는 TypeScript 내장 타입이다.

---

### [핵심]

Foundation 필수 포함:

- Partial
- Required
- Pick
- Omit
- Record
- Readonly
- ReturnType basics

---

### [실무]

예:

```typescript
type User = {
  id: number;
  name: string;
  email: string;
};

type UserUpdateRequest = Partial<User>;
type UserSummary = Pick<User, "id" | "name">;
type UserCreateRequest = Omit<User, "id">;
```

API DTO 구성에 유용하다.

주의:

- Utility Type 남용 금지
- 원본 타입과 요청 타입이 무조건 같은 것은 아님
- Backend DTO와 Frontend Type 차이 고려
- 너무 복잡하면 명시적 Type 정의가 더 좋음

---

### [FAQ]

Q. Partial은 언제 써?

A.
객체의 모든 property를 optional로 만들 때 사용한다. 수정 요청 타입에 사용할 수 있다.

Q. Pick은 언제 써?

A.
기존 타입에서 일부 property만 선택해 새 타입을 만들 때 사용한다.

Q. Omit은 언제 써?

A.
기존 타입에서 특정 property를 제외한 타입을 만들 때 사용한다.

---

# 13. API Type Rules

## 13.1 API Request Type Rules

### [개념]

API Request Type은 Frontend가 Backend로 보내는 요청 데이터의 구조를 정의하는 타입이다.

---

### [핵심]

필수 포함:

- request body type
- query parameter type
- path parameter type
- form data type
- create request
- update request
- search request
- optional field
- validation relation

---

### [실무]

예:

```typescript
type ReviewCreateRequest = {
  festivalId: number;
  rating: number;
  content: string;
};

type FestivalSearchParams = {
  keyword?: string;
  regionCode?: string;
  themeCode?: string;
  targetMonth?: string;
};
```

주의:

- Backend Request DTO와 필드명 정합성 유지
- Optional field 명확히 표시
- Frontend validation과 Backend validation 구분
- 민감정보 포함 여부 주의

---

### [FAQ]

Q. API Request Type은 왜 필요해?

A.
Frontend가 Backend로 보내는 데이터 구조를 명확히 하고 필드 누락이나 타입 오류를 줄이기 위해 필요하다.

Q. Query Parameter도 타입으로 정의해?

A.
정의하는 것이 좋다. 검색 조건, 페이지 조건, 필터 조건이 많아질수록 타입 정의가 유리하다.

---

## 13.2 API Response Type Rules

### [개념]

API Response Type은 Backend가 Frontend로 반환하는 응답 데이터의 구조를 정의하는 타입이다.

---

### [핵심]

필수 포함:

- response body type
- common response wrapper
- data field
- list response
- page response
- slice response
- error response
- nullable field
- optional field

---

### [실무]

공통 응답 예:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};
```

목록 응답 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  eventStartDate: string;
  eventEndDate: string;
  averageRating: number | null;
};

type FestivalListResponse = ApiResponse<FestivalInfoResponse[]>;
```

Slice 응답 예:

```typescript
type SliceResponse<T> = {
  content: T[];
  hasNext: boolean;
  number: number;
  size: number;
};
```

주의:

- Backend 응답 wrapper 구조와 일치
- 날짜는 보통 string으로 수신
- nullable field 명시
- list와 page/slice 구조 구분
- 화면용 ViewModel Type과 분리 가능

---

### [FAQ]

Q. API Response Type은 왜 중요해?

A.
서버 응답 구조를 타입으로 고정해 화면 코드에서 잘못된 property 접근을 줄일 수 있다.

Q. 날짜 타입은 Date로 받아?

A.
대부분 JSON 응답에서는 string으로 받는다. 필요하면 Frontend에서 Date로 변환한다.

Q. nullable field는 어떻게 표현해?

A.
`string | null`, `number | null`처럼 Union Type으로 표현한다.

---

## 13.3 Error Response Type Rules

### [개념]

Error Response Type은 API 실패 응답의 구조를 정의하는 타입이다.

---

### [핵심]

필수 포함:

- error code
- message
- status
- field errors
- validation error
- global error
- fallback message

---

### [실무]

예:

```typescript
type ApiErrorResponse = {
  success: false;
  message: string;
  code?: string;
  errors?: Record<string, string>;
};
```

Error Handling 예:

```typescript
function getErrorMessage(error: ApiErrorResponse | null): string {
  return error?.message ?? "요청 처리 중 오류가 발생했습니다.";
}
```

주의:

- Backend GlobalExceptionHandler 응답 구조 확인
- validation error field 구조 확인
- 사용자 메시지와 개발자 로그 구분
- 민감한 서버 오류 그대로 노출 금지

---

### [FAQ]

Q. Error Response도 타입으로 정의해야 해?

A.
하는 것이 좋다. 실패 응답 구조가 명확해야 사용자 메시지와 검증 오류를 안정적으로 처리할 수 있다.

Q. errors는 왜 Record를 써?

A.
필드명과 오류 메시지의 key-value 구조를 표현하기 좋기 때문이다.

---

# 14. React TypeScript Readiness Rules

## 14.1 Props Type Basics

### [개념]

Props Type은 React Component가 외부에서 받는 데이터의 구조를 정의하는 타입이다.

---

### [핵심]

필수 포함:

- props type
- optional props
- children basics
- callback props
- event handler props
- component data props

---

### [실무]

기본 예:

```typescript
type FestivalCardProps = {
  title: string;
  imageUrl: string | null;
  onClick: () => void;
};

function FestivalCard({ title, imageUrl, onClick }: FestivalCardProps) {
  return null;
}
```

주의:

- Props Type은 Component 가까이에 정의 가능
- 여러 Component에서 공유하면 별도 파일로 분리
- optional props는 기본값 고려
- callback props는 parameter와 return type 명확화

---

### [FAQ]

Q. React Props Type은 왜 필요해?

A.
Component가 어떤 데이터를 받아야 하는지 명확히 하고 잘못된 props 전달을 막기 위해 필요하다.

Q. Props Type은 type과 interface 중 뭐로 정의해?

A.
둘 다 가능하다. 프로젝트 컨벤션에 맞춰 일관되게 사용한다.

---

## 14.2 React Event Type Basics

### [개념]

React Event Type은 React Event Handler의 event 객체 타입을 정의하는 방식이다.

---

### [핵심]

필수 포함:

- MouseEvent
- ChangeEvent
- FormEvent
- KeyboardEvent
- HTMLInputElement
- HTMLButtonElement
- HTMLFormElement
- event handler type

---

### [실무]

Input Change 예:

```typescript
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): void {
  console.log(event.target.value);
}
```

Form Submit 예:

```typescript
import type { FormEvent } from "react";

function handleSubmit(event: FormEvent<HTMLFormElement>): void {
  event.preventDefault();
}
```

주의:

- DOM Event Type과 React Event Type 구분
- target element type 명시
- handler return은 보통 void
- React 문서에서 심화 다룸

---

### [FAQ]

Q. input onChange event 타입은 뭐야?

A.
일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit event 타입은 뭐야?

A.
일반적으로 `FormEvent<HTMLFormElement>`를 사용한다.

Q. event handler return type은 뭐야?

A.
대부분 `void`를 사용한다.

---

## 14.3 State Type Basics

### [개념]

State Type은 React 상태 값의 타입을 정의하는 기준이다.

---

### [핵심]

필수 포함:

- primitive state
- object state
- array state
- nullable state
- loading state
- union state
- initial value inference

---

### [실무]

상태 타입 예:

```typescript
type Festival = {
  id: number;
  title: string;
};

const initialFestivals: Festival[] = [];
```

nullable 상태 예:

```typescript
type User = {
  id: number;
  name: string;
};

const initialUser: User | null = null;
```

비동기 상태 예:

```typescript
type AsyncStatus = "idle" | "loading" | "success" | "error";
```

주의:

- 빈 배열 초기값은 타입 명시 필요
- null 초기값은 Union Type 필요
- loading / error / success 상태는 literal union 권장

---

### [FAQ]

Q. React State 빈 배열은 타입을 써야 해?

A.
쓰는 것이 좋다. 빈 배열만으로는 요소 타입을 정확히 알기 어렵다.

Q. 초기값이 null이면 타입을 어떻게 써?

A.
`User | null`처럼 null 가능성을 Union Type으로 명시한다.

---

# 15. tsconfig Rules

## 15.1 tsconfig Basics

### [개념]

tsconfig는 TypeScript 프로젝트의 컴파일 옵션과 파일 포함 범위를 정의하는 설정 파일이다.

---

### [핵심]

필수 포함:

- compilerOptions
- strict
- target
- module
- jsx
- noImplicitAny
- strictNullChecks
- baseUrl
- paths basics
- include
- exclude

---

### [실무]

권장 기본 방향:

```json
{
  "compilerOptions": {
    "strict": true,
    "target": "ES2020",
    "module": "ESNext",
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
```

주의:

- `strict: true` 권장
- 기존 JS 프로젝트 전환 시 단계적 적용 가능
- `noImplicitAny`는 any 누락을 찾는 데 도움
- `strictNullChecks`는 null 안전성에 중요
- 설정 변경 후 IDE / Dev Server 재시작 필요 가능

---

### [FAQ]

Q. strict true를 켜야 해?

A.
신규 프로젝트에서는 권장한다. 기존 프로젝트는 오류량에 따라 단계적으로 적용할 수 있다.

Q. strictNullChecks는 왜 중요해?

A.
null과 undefined 가능성을 타입 단계에서 잡아 런타임 오류를 줄일 수 있기 때문이다.

Q. tsconfig 수정 후 오류가 계속 보이면?

A.
IDE TypeScript Server나 개발 서버를 재시작해야 할 수 있다.

---

# 16. Migration Rules

## 16.1 JavaScript to TypeScript Migration

### [개념]

JavaScript to TypeScript Migration은 기존 JavaScript 파일을 TypeScript 파일로 전환하는 과정이다.

---

### [핵심]

필수 포함:

- `.js` to `.ts`
- `.jsx` to `.tsx`
- type annotation
- props type
- API response type
- event type
- any 제거
- incremental migration
- strict mode 단계 적용

---

### [실무]

Migration Flow:

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

우선순위:

1. API Type
2. Props Type
3. Function Parameter Type
4. Event Type
5. State Type
6. Utility Type
7. Any 제거

---

### [FAQ]

Q. JS 파일을 바로 TS로 바꾸면 돼?

A.
작은 파일은 가능하지만 큰 프로젝트는 점진적으로 바꾸는 것이 안전하다.

Q. jsx 파일은 ts로 바꿔?

A.
React JSX가 포함된 파일은 `.tsx`로 바꾼다.

Q. Migration에서 가장 먼저 타입을 붙일 곳은?

A.
API Response, Props, Function Parameter, Event Handler부터 붙이는 것이 효과적이다.

---

# 17. Security Rules

## 17.1 TypeScript Security Basics

### [개념]

TypeScript는 타입 안정성을 높이지만 보안 기능을 자동 제공하지 않는다.

---

### [핵심]

필수 포함:

- Type Safety
- Runtime Validation
- API Response Validation
- User Input Validation
- XSS caution
- Token Type
- Sensitive Data Type
- any caution
- unknown validation

---

### [실무]

주의:

- TypeScript Type은 Runtime 검증이 아님
- 외부 API 응답은 신뢰하지 않음
- 사용자 입력은 검증 필요
- JWT / Token을 로그에 출력 금지
- 민감정보를 Frontend Type에 불필요하게 포함하지 않음
- `as` Type Assertion으로 검증을 우회하지 않음

위험 예:

```typescript
const user = response as User;
```

개선 방향:

```typescript
if (isUser(response)) {
  return response;
}
```

---

### [FAQ]

Q. TypeScript를 쓰면 API 응답이 자동 검증돼?

A.
아니다. TypeScript 타입은 컴파일 단계에서만 검사된다. Runtime API 응답 검증은 별도로 필요하다.

Q. Type Assertion은 위험해?

A.
검증 없이 타입을 강제로 믿게 만들 수 있어 남용하면 위험하다.

Q. unknown이 보안에 더 좋아?

A.
외부 입력을 바로 사용하지 못하게 하고 검증을 요구하므로 any보다 안전하다.

---

# 18. Code Example Rules

## 18.1 Example Style

### [개념]

TypeScript 예제는 짧고 직접적이어야 한다.

목적:

- Retrieval
- Code Generation
- Review
- Type Error Debugging
- React TypeScript 전환 기반 제공

---

### [핵심]

권장:

- 핵심 타입만 포함
- 실무형 API / Props 예제 사용
- `type` 또는 `interface` 명확히 사용
- `any` 지양
- nullable 명시
- 함수 parameter와 return type 표시
- Generic은 간단한 예제 중심
- 긴 전체 프로젝트 코드 금지

금지:

- any 중심 예제
- 복잡한 Advanced Type 예제
- Type Assertion 남용 예제
- 의미 없는 Foo / Bar 남용
- Runtime 검증 없는 API 단정
- 불필요한 타입 장식 과다

---

### [실무]

좋은 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};

async function getFestivals(): Promise<FestivalInfoResponse[]> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return await response.json();
}
```

---

### [FAQ]

Q. TypeScript 예제 코드는 길수록 좋아?

A.
아니다. RAG 문서에서는 짧고 검색 가능한 타입 예제가 더 좋다.

Q. 예제에 any를 써도 돼?

A.
가능하면 쓰지 않는다. unknown, 명시적 Type, Generic을 우선 고려한다.

---

# 19. Troubleshooting Rules

## 19.1 Type Error

### [개념]

Type Error는 TypeScript가 값의 타입과 사용 방식이 맞지 않는다고 판단할 때 발생한다.

---

### [핵심]

문제:

- Type 'string' is not assignable to type 'number'
- Object is possibly 'null'
- Property does not exist on type
- Type 'undefined' is not assignable
- Parameter implicitly has an 'any' type

원인:

- 잘못된 Type Annotation
- null / undefined 가능성 미처리
- API Response Type 불일치
- Optional Property 접근
- Function Parameter Type 누락
- tsconfig strict 설정

해결:

- 실제 데이터 구조 확인
- Type 정의 수정
- null guard 추가
- optional chaining 사용
- default value 적용
- parameter type 명시
- 잘못된 assertion 제거

---

### [실무]

Debug Flow:

```text
Type Error Message
→ Error Location Check
→ Actual Value Shape Check
→ Type Definition Check
→ Null / Undefined Check
→ Narrowing or Type Fix
→ Re-run Type Check
```

---

### [FAQ]

Q. Object is possibly null 오류는 왜 나?

A.
값이 null일 수 있는데 null check 없이 사용하려고 해서 발생한다.

Q. Property does not exist on type 오류는 왜 나?

A.
해당 타입 정의에 property가 없거나 TypeScript가 아직 타입을 좁히지 못했기 때문이다.

Q. implicitly has an any type은 왜 나?

A.
함수 parameter 타입이 명시되지 않았고 TypeScript가 추론할 수 없기 때문이다.

---

## 19.2 API Type Mismatch

### [개념]

API Type Mismatch는 Frontend Type 정의와 Backend 실제 응답 구조가 맞지 않는 문제다.

---

### [핵심]

문제:

- 화면에서 undefined 표시
- property 접근 오류
- 타입은 맞는데 런타임 값이 없음
- 날짜 / 숫자 타입 예상 불일치
- nullable 처리 누락

원인:

- Backend DTO 변경
- Frontend Type 업데이트 누락
- Response Wrapper 구조 오해
- Page / Slice 구조 혼동
- null field 미반영
- snake_case / camelCase 불일치

해결:

- Network Response Body 확인
- Backend DTO 확인
- Type 정의 갱신
- nullable 반영
- wrapper 구조 반영
- mapping 함수 작성

---

### [실무]

Debug Flow:

```text
Network Response Check
→ Backend DTO Check
→ Frontend Type Check
→ Mapping Function Check
→ UI Usage Check
```

---

### [FAQ]

Q. 타입은 맞는데 화면에서 undefined가 나와?

A.
실제 API 응답 구조와 Frontend Type 정의가 다를 수 있다. Network 탭에서 응답 body를 확인해야 한다.

Q. Backend DTO가 바뀌면 Type도 바꿔야 해?

A.
바꿔야 한다. Frontend API Response Type은 Backend 응답 구조와 정합성을 유지해야 한다.

---

## 19.3 Any Overuse

### [개념]

Any Overuse는 TypeScript 코드에서 `any`를 과도하게 사용해 타입 안정성이 무너지는 문제다.

---

### [핵심]

문제:

- TypeScript를 써도 오류를 못 잡음
- 자동완성 약화
- 잘못된 property 접근 허용
- API 구조 변경 감지 실패
- 런타임 오류 증가

원인:

- 빠른 오류 회피
- API Type 미정의
- 복잡한 타입 회피
- Migration 중 임시 any 방치
- 외부 라이브러리 타입 이해 부족

해결:

- API Type 정의
- unknown 사용 후 narrowing
- Generic 사용
- Utility Type 사용
- any 위치 TODO 관리
- 점진적 any 제거

---

### [실무]

나쁜 예:

```typescript
function renderFestival(festival: any) {
  return festival.title;
}
```

좋은 예:

```typescript
type Festival = {
  title: string;
};

function renderFestival(festival: Festival): string {
  return festival.title;
}
```

---

### [FAQ]

Q. any를 아예 쓰면 안 돼?

A.
임시로 사용할 수는 있지만 최종 코드에서는 제거하거나 범위를 최소화하는 것이 좋다.

Q. any 대신 뭘 써?

A.
타입을 모르면 unknown을 사용하고, 사용 전에 Type Guard로 검증한다.

---

# 20. Comparison Rules

## 20.1 Required Comparisons

### [개념]

TypeScript 문서는 헷갈리는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- JavaScript vs TypeScript
- Type Annotation vs Type Inference
- type vs interface
- any vs unknown
- null vs undefined
- optional vs nullable
- union type vs enum
- string vs String
- Array Type vs Tuple Type
- type assertion vs type guard
- interface extends vs type intersection
- Promise<T> vs T
- Partial vs Pick vs Omit

---

### [실무]

예시:

| 비교         | any            | unknown          |
| ------------ | -------------- | ---------------- |
| 의미         | 아무 타입 허용 | 알 수 없는 타입  |
| 사용 전 검사 | 필요 없음      | 필요함           |
| 타입 안정성  | 낮음           | 높음             |
| 권장도       | 지양           | 외부 입력에 권장 |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. TypeScript 비교 문서에서 가장 중요한 것은?

A.
실무 선택 기준과 오류 가능성을 함께 설명하는 것이다.

---

# 21. Checklist Rules

## 21.1 Document Quality Checklist

### [개념]

TypeScript 문서 검수 시 품질 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] TypeScript 기본 개념이 포함되었는가?
- [ ] Type Annotation / Type Inference 설명이 포함되었는가?
- [ ] Primitive / Array / Object Type이 포함되었는가?
- [ ] Optional / Nullable 차이가 포함되었는가?
- [ ] Union / Literal Type 예제가 포함되었는가?
- [ ] Type Alias / Interface 비교가 포함되었는가?
- [ ] Function Type 예제가 포함되었는가?
- [ ] Type Narrowing / Type Guard가 포함되었는가?
- [ ] Generic Basics가 포함되었는가?
- [ ] Utility Type 기초가 포함되었는가?
- [ ] API Request / Response Type이 포함되었는가?
- [ ] React TypeScript 연결 기초가 포함되었는가?
- [ ] Type Error Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Required Section Check
→ Type Example Check
→ API Type Check
→ React Readiness Check
→ Type Error Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. TypeScript 문서 검수에서 가장 중요한 것은?

A.
Basic Type, Object Type, Function Type, Union Type, Interface/Type Alias, Generic, API Type, Type Error 대응 포함 여부다.

---

# 22. Retrieval Optimization Rules

## 22.1 Keyword Rules

### [개념]

TypeScript Foundation 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- TypeScript
- TypeScript Foundation
- Frontend TypeScript
- Static Type
- Type Annotation
- Type Inference
- Primitive Type
- string
- number
- boolean
- null
- undefined
- Array Type
- Tuple Type
- Object Type
- Optional Property
- Nullable
- Readonly
- Union Type
- Literal Type
- Type Alias
- Interface
- Function Type
- Return Type
- Generic
- Generic Constraint
- Utility Type
- Partial
- Pick
- Omit
- Record
- Type Narrowing
- Type Guard
- unknown
- any
- never
- void
- API Request Type
- API Response Type
- Error Response Type
- React Props Type
- React Event Type
- tsconfig
- strict
- Type Error
- JavaScript to TypeScript Migration

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- TypeScript 왜 써?
- TypeScript는 JavaScript랑 뭐가 달라?
- Type Annotation이 뭐야?
- Type Inference가 뭐야?
- any와 unknown 차이는?
- type과 interface 차이는?
- optional과 nullable 차이는?
- Union Type은 언제 써?
- Generic은 왜 써?
- API Response Type은 어떻게 정의해?
- React Props Type은 어떻게 정의해?
- Object is possibly null 오류는 왜 나?
- Property does not exist on type 오류는 왜 나?
- TypeScript에서 fetch 응답 타입은 어떻게 써?
- JS를 TS로 바꾸려면 어디부터 해?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 23. Version Rules

## 23.1 Modern TypeScript 기준

### [개념]

TypeScript Foundation 문서는 Modern TypeScript 기준으로 작성한다.

---

### [핵심]

기준:

- TypeScript 5.x+
- ES Module
- strict mode 권장
- strictNullChecks 권장
- Type Inference 활용
- type-only import 고려
- React JSX / TSX 기반 준비
- Utility Type 활용
- Generic Basics
- API Type 중심
- Frontend Type Safety 기준

Legacy 제외:

- namespace 중심 설명
- triple slash reference 중심 설명
- any 중심 전환
- class 기반 React Type 중심 설명
- 오래된 decorator 중심 설명
- enum 남용 중심 설명
- tsconfig legacy 옵션 중심 설명

---

### [실무]

실무 기준:

```text
Modern TypeScript
→ Strict Type Check
→ API Type Definition
→ Props Type Definition
→ Event Type Definition
→ Type Safe Frontend Logic
```

---

### [FAQ]

Q. TypeScript strict mode는 꼭 써야 해?

A.
신규 프로젝트에서는 권장한다. 기존 프로젝트는 단계적으로 적용할 수 있다.

Q. enum은 쓰면 안 돼?

A.
쓸 수 있지만 단순 상태 값은 string literal union이 더 가볍고 직관적인 경우가 많다.

---

# 24. Common Mistakes

## 24.1 TypeScript Common Mistakes

### [개념]

TypeScript Foundation 문서는 자주 발생하는 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- any 남용
- Type Assertion 남용
- API Response Type 미정의
- Optional과 Nullable 혼동
- null / undefined 방어 누락
- 빈 배열 타입 미정의
- async 함수 return type 오해
- Promise<T>와 T 혼동
- Interface와 Type Alias 기준 혼동
- string과 String 혼동
- API 날짜 값을 Date로 단정
- Backend DTO 변경 후 Type 미수정
- Event Type 미정의
- Props Type 누락
- Generic 과도한 복잡화
- Utility Type 남용
- strict mode 끄고 방치
- Runtime Validation 없이 Type만 신뢰

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: Object is possibly null
원인: nullable 값 방어 누락
해결: null check, optional chaining, default value 적용
```

---

### [FAQ]

Q. TypeScript 초보가 가장 많이 하는 실수는?

A.
any 남용, null 방어 누락, API 응답 타입 불일치, type assertion 남용이 많다.

Q. TypeScript 오류는 어떻게 찾는 게 좋아?

A.
오류 메시지, 실제 값 구조, Type 정의, null 가능성, API 응답 구조를 순서대로 확인한다.

---

# 25. Final Goal

## 25.1 Domain Final Goal

### [개념]

TypeScript Foundation RAG 문서는 Frontend Agent가 타입 안정성이 있는 Frontend 코드를 생성하고 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- TypeScript 기본 개념 이해
- Type Annotation 작성
- Type Inference 활용
- Primitive Type 정의
- Array / Tuple Type 정의
- Object Type 정의
- Optional / Nullable 구분
- Union / Literal Type 작성
- Type Alias / Interface 사용
- Function Type 작성
- Type Narrowing 적용
- Type Guard 작성
- Generic Basics 이해
- Utility Type 활용
- API Request Type 정의
- API Response Type 정의
- Error Response Type 정의
- React Props Type 기초 작성
- React Event Type 기초 작성
- Type Error Debugging 수행
- JavaScript to TypeScript Migration 기준 제공

---

### [실무]

Agent 수행 가능 작업:

```text
Frontend Type Request
→ Type Definition
→ API Type Modeling
→ Component Props Type
→ Event Type
→ Type Narrowing
→ Type Error Review
→ Type Safe Frontend Code
```

---

### [FAQ]

Q. TypeScript Foundation 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 React TypeScript 이전 단계의 타입 정의, API 타입 모델링, 타입 오류 검토를 안정적으로 수행하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
React Core, React Component Design, React Router, Data Fetching & REST API Integration 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. TypeScript Foundation 문서는 왜 필요해?
A. Frontend Agent가 타입 안정성이 있는 React / JavaScript 코드를 만들기 전에 TypeScript 기본 타입 시스템을 이해해야 하기 때문이다.

Q. TypeScript는 JavaScript랑 뭐가 달라?
A. TypeScript는 JavaScript에 정적 타입 시스템을 추가한 언어이며 컴파일 후 JavaScript로 실행된다.

Q. TypeScript Type은 Runtime에도 남아?
A. 아니다. Type 정보는 컴파일 후 제거되고 Runtime에는 JavaScript만 실행된다.

Q. TypeScript를 쓰면 Runtime Error가 없어져?
A. 아니다. Compile Time 타입 오류를 줄여주지만 Runtime Error를 완전히 제거하지는 않는다.

Q. Type Annotation이 뭐야?
A. 변수, 함수, 객체에 타입을 명시하는 문법이다.

Q. Type Inference가 뭐야?
A. TypeScript가 값과 코드 흐름을 보고 타입을 자동으로 추론하는 기능이다.

Q. 모든 변수에 타입을 써야 해?
A. 아니다. 명확한 초기값이 있는 변수는 Type Inference를 활용하고 함수 parameter나 API 응답은 명시하는 것이 좋다.

Q. 빈 배열에는 왜 타입을 써야 해?
A. TypeScript가 배열 요소 타입을 정확히 추론하기 어렵기 때문이다.

Q. string과 String 차이는?
A. string은 primitive type이고 String은 객체 wrapper type이다. 실무에서는 string을 사용한다.

Q. number는 정수와 실수를 구분해?
A. 아니다. JavaScript number는 정수와 실수를 모두 표현한다.

Q. Array Type은 어떻게 써?
A. `string[]`, `number[]`, `Festival[]` 또는 `Array<T>` 형태로 작성한다.

Q. Tuple은 언제 써?
A. 좌표처럼 길이와 위치별 의미가 명확한 짧은 데이터에 사용한다.

Q. any는 왜 피해야 해?
A. TypeScript 타입 검사를 우회해 잘못된 property 접근이나 타입 오류를 미리 잡기 어렵게 만든다.

Q. unknown은 any랑 뭐가 달라?
A. unknown은 사용 전 타입 검사가 필요하지만 any는 검사 없이 사용할 수 있다.

Q. void는 언제 써?
A. 반환값이 없는 함수의 return type에 사용한다.

Q. never는 언제 써?
A. 절대 반환되지 않는 함수나 도달할 수 없는 상태를 표현할 때 사용한다.

Q. Object Type은 어떻게 정의해?
A. type 또는 interface를 사용해 property 이름과 타입을 정의한다.

Q. optional property는 어떻게 써?
A. property 이름 뒤에 `?`를 붙인다. 예: `imageUrl?: string`.

Q. optional과 nullable 차이는?
A. optional은 property가 없거나 undefined일 수 있다는 뜻이고 nullable은 값이 null일 수 있다는 뜻이다.

Q. `name?: string`과 `name: string | null`은 같아?
A. 아니다. optional은 누락 가능성이고 nullable은 null 값 가능성이다.

Q. readonly는 언제 써?
A. ID, 생성일, 외부에서 변경하면 안 되는 값, 함수 입력 배열을 보호할 때 사용한다.

Q. Union Type은 언제 써?
A. 값이 여러 타입 또는 여러 상태 중 하나일 수 있을 때 사용한다.

Q. Literal Type은 왜 써?
A. 허용 가능한 문자열이나 숫자 값을 제한해 오타와 잘못된 상태 값을 줄이기 위해 사용한다.

Q. 상태 타입은 string으로 두면 안 돼?
A. 가능하지만 `"idle" | "loading" | "success" | "error"` 같은 literal union이 더 안전하다.

Q. Discriminated Union은 뭐야?
A. 공통 구분 property를 기준으로 여러 객체 형태를 안전하게 구분하는 타입 패턴이다.

Q. type alias는 언제 써?
A. Union Type, Literal Type, Function Type, 객체 타입에 이름을 붙여 재사용할 때 사용한다.

Q. interface는 언제 써?
A. 객체 구조를 정의하고 확장 가능성을 고려할 때 사용한다.

Q. type과 interface 차이는?
A. 둘 다 객체 타입을 정의할 수 있지만 type은 Union / Literal Type에 적합하고 interface는 객체 확장에 적합하다.

Q. React Props는 type과 interface 중 뭐가 좋아?
A. 둘 다 가능하다. 프로젝트 컨벤션에 맞춰 일관되게 사용하는 것이 좋다.

Q. 함수 parameter에는 타입을 써야 해?
A. 대부분 써야 한다. 함수 parameter는 TypeScript가 자동 추론하기 어렵다.

Q. async 함수 return type은 어떻게 써?
A. `Promise<T>` 형태로 작성한다.

Q. Optional Parameter는 null도 허용해?
A. 아니다. `name?: string`은 string 또는 undefined를 의미한다. null도 허용하려면 `string | null`을 명시한다.

Q. Type Narrowing은 왜 필요해?
A. Union Type이나 unknown 값을 안전하게 사용하기 위해 필요하다.

Q. Type Guard는 언제 써?
A. unknown 값, 외부 API 응답, localStorage 데이터처럼 타입을 확신할 수 없는 값을 사용할 때 쓴다.

Q. `value is Type`은 뭐야?
A. 조건이 true일 때 value가 해당 Type임을 TypeScript에 알려주는 문법이다.

Q. Generic은 왜 써?
A. 타입은 다르지만 구조가 같은 로직을 재사용하기 위해 사용한다.

Q. Generic의 T는 무슨 뜻이야?
A. 관례적으로 Type을 의미하는 타입 parameter 이름이다. 다른 이름도 사용할 수 있다.

Q. API Response에 Generic을 왜 써?
A. 응답 공통 구조는 유지하고 data 타입만 다르게 재사용할 수 있기 때문이다.

Q. Generic Constraint는 왜 필요해?
A. Generic 타입에서도 특정 property나 구조가 있음을 보장하기 위해 필요하다.

Q. Partial은 언제 써?
A. 객체의 모든 property를 optional로 만들 때 사용한다.

Q. Pick은 언제 써?
A. 기존 타입에서 일부 property만 선택해 새 타입을 만들 때 사용한다.

Q. Omit은 언제 써?
A. 기존 타입에서 특정 property를 제외한 타입을 만들 때 사용한다.

Q. API Request Type은 왜 필요해?
A. Frontend가 Backend로 보내는 데이터 구조를 명확히 하고 필드 누락이나 타입 오류를 줄이기 위해 필요하다.

Q. API Response Type은 왜 중요해?
A. 서버 응답 구조를 타입으로 고정해 화면 코드에서 잘못된 property 접근을 줄일 수 있다.

Q. 날짜 타입은 Date로 받아?
A. 대부분 JSON 응답에서는 string으로 받는다. 필요하면 Frontend에서 Date로 변환한다.

Q. Slice Response Type은 어떻게 정의해?
A. content, hasNext, number, size 같은 필드를 포함하는 Generic Type으로 정의할 수 있다.

Q. Error Response도 타입으로 정의해야 해?
A. 하는 것이 좋다. 실패 응답 구조가 명확해야 사용자 메시지와 검증 오류를 안정적으로 처리할 수 있다.

Q. React Props Type은 왜 필요해?
A. Component가 어떤 데이터를 받아야 하는지 명확히 하고 잘못된 props 전달을 막기 위해 필요하다.

Q. input onChange event 타입은 뭐야?
A. 일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit event 타입은 뭐야?
A. 일반적으로 `FormEvent<HTMLFormElement>`를 사용한다.

Q. React State 빈 배열은 타입을 써야 해?
A. 쓰는 것이 좋다. 빈 배열만으로는 요소 타입을 정확히 알기 어렵다.

Q. 초기값이 null이면 타입을 어떻게 써?
A. `User | null`처럼 null 가능성을 Union Type으로 명시한다.

Q. tsconfig strict true를 켜야 해?
A. 신규 프로젝트에서는 권장한다. 기존 프로젝트는 단계적으로 적용할 수 있다.

Q. strictNullChecks는 왜 중요해?
A. null과 undefined 가능성을 타입 단계에서 잡아 런타임 오류를 줄일 수 있기 때문이다.

Q. JS 파일을 TS로 바꾸려면 어디부터 해?
A. API Response, Props, Function Parameter, Event Handler, State Type부터 점진적으로 적용하는 것이 좋다.

Q. jsx 파일은 ts로 바꿔?
A. React JSX가 포함된 파일은 `.tsx`로 바꾼다.

Q. Object is possibly null 오류는 왜 나?
A. 값이 null일 수 있는데 null check 없이 사용하려고 해서 발생한다.

Q. Property does not exist on type 오류는 왜 나?
A. 해당 타입 정의에 property가 없거나 TypeScript가 아직 타입을 좁히지 못했기 때문이다.

Q. Parameter implicitly has an any type은 왜 나?
A. 함수 parameter 타입이 명시되지 않았고 TypeScript가 추론할 수 없기 때문이다.

Q. 타입은 맞는데 화면에서 undefined가 나와?
A. 실제 API 응답 구조와 Frontend Type 정의가 다를 수 있다. Network 탭에서 응답 body를 확인해야 한다.

Q. Backend DTO가 바뀌면 Frontend Type도 바꿔야 해?
A. 바꿔야 한다. Frontend API Response Type은 Backend 응답 구조와 정합성을 유지해야 한다.

Q. Type Assertion은 위험해?
A. 검증 없이 타입을 강제로 믿게 만들 수 있어 남용하면 위험하다.

Q. TypeScript를 쓰면 API 응답이 자동 검증돼?
A. 아니다. TypeScript 타입은 컴파일 단계에서만 검사된다. Runtime API 응답 검증은 별도로 필요하다.

Q. enum은 쓰면 안 돼?
A. 쓸 수 있지만 단순 상태 값은 string literal union이 더 가볍고 직관적인 경우가 많다.

Q. TypeScript Foundation 다음 문서는 뭐가 좋아?
A. React Core, React Component Design, React Router, Data Fetching & REST API Integration 순서가 좋다.
