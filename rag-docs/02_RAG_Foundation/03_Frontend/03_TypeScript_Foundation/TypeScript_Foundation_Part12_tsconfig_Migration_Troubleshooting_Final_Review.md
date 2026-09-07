# TypeScript Foundation Part12 - tsconfig, Migration, Troubleshooting, Final Review

---

# 1. tsconfig Basics

## 1.1 tsconfig Definition

### [개념]

`tsconfig.json`은 TypeScript Compiler가 Project를 어떻게 해석하고 Compile할지 정의하는 설정 파일이다.

TypeScript Project의 Type Check 기준, JavaScript Target, Module 방식, JSX 처리 방식, Strict Mode 기준을 설정한다.

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "jsx": "react-jsx",
    "strict": true
  },
  "include": ["src"]
}
```

`tsconfig.json`은 TypeScript 코드 품질과 Type Safety 수준을 결정하는 핵심 설정이다.

---

### [핵심]

tsconfig 주요 영역:

- `compilerOptions`
- `target`
- `module`
- `jsx`
- `strict`
- `noImplicitAny`
- `strictNullChecks`
- `baseUrl`
- `paths`
- `moduleResolution`
- `include`
- `exclude`

핵심 기준:

- 신규 프로젝트는 `strict: true` 권장
- React Project는 `jsx` 설정 확인
- TypeScript 5.x+ 기준 modern option 사용
- compile target은 프로젝트 실행 환경에 맞춤
- path alias는 bundler 설정과 함께 맞춤

---

### [실무]

2026 Frontend 실무 기준에서는 Vite, React, TypeScript 조합에서 strict mode를 기본으로 사용하는 경우가 많다.

기본 예:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
```

실무 기준:

- `strict: true`로 Type Safety 확보
- `skipLibCheck: true`는 외부 library type check 비용 절감에 사용 가능
- `noEmit: true`는 bundler가 build를 담당할 때 사용 가능
- `jsx: "react-jsx"`는 modern React JSX transform 기준
- `include`는 실제 source directory를 포함
- tsconfig 변경 후 IDE / dev server 재시작 필요 가능

---

### [FAQ]

Q. tsconfig.json이 뭐야?
A. TypeScript Compiler가 Project를 어떻게 해석하고 검사할지 정의하는 설정 파일이다.

Q. strict true는 꼭 켜야 해?
A. 신규 프로젝트에서는 권장한다. Type Safety와 오류 탐지 품질이 크게 좋아진다.

Q. tsconfig를 바꾸면 바로 적용돼?
A. 보통 적용되지만 IDE나 dev server가 이전 설정을 유지하면 재시작이 필요할 수 있다.

Q. tsconfig는 Runtime 동작도 바꿔?
A. 일부 Compile 결과에 영향을 줄 수 있지만 Type 설정 자체는 Runtime 검증을 제공하지 않는다.

---

## 1.2 strict Mode

### [개념]

`strict` Mode는 TypeScript의 엄격한 Type Check 옵션 묶음이다.

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

`strict: true`를 사용하면 null, undefined, implicit any, function type 등 다양한 Type 오류를 더 강하게 검사한다.

---

### [핵심]

`strict`에 포함되는 주요 기준:

- `noImplicitAny`
- `strictNullChecks`
- `strictFunctionTypes`
- `strictBindCallApply`
- `strictPropertyInitialization`
- `noImplicitThis`
- `alwaysStrict`
- `useUnknownInCatchVariables`

실무 효과:

- any 누락 탐지
- null / undefined 오류 탐지
- 함수 parameter 오류 탐지
- nullable state 접근 오류 탐지
- API Type 불일치 탐지

---

### [실무]

strict mode에서 자주 발견되는 오류:

```typescript
function getTitle(festival) {
  return festival.title;
}
```

문제:

- `festival` parameter에 Type이 없다.
- `noImplicitAny`에서 오류 발생.

개선:

```typescript
type Festival = {
  title: string;
};

function getTitle(festival: Festival): string {
  return festival.title;
}
```

null 오류 예:

```typescript
type User = {
  nickname: string;
};

function getNickname(user: User | null): string {
  return user.nickname;
}
```

개선:

```typescript
function getNickname(user: User | null): string {
  return user?.nickname ?? "Guest";
}
```

실무 기준:

- 신규 프로젝트는 strict true 유지
- 기존 JavaScript Migration은 단계적으로 strict 적용 가능
- strict 오류를 `any`나 `as`로 숨기지 않음
- null / undefined 오류는 Type 정의와 guard로 해결
- Review Agent는 strict 우회 패턴 확인

---

### [FAQ]

Q. strict mode는 뭐야?
A. TypeScript의 엄격한 Type Check 옵션 묶음이다.

Q. strict를 켜면 오류가 많아져?
A. 기존 코드에서는 많아질 수 있다. 하지만 실제 위험한 Type 문제를 미리 찾는 데 도움이 된다.

Q. strict 오류는 any로 없애도 돼?
A. 권장하지 않는다. Type을 명확히 정의하거나 null guard, Type Guard로 해결하는 것이 좋다.

---

## 1.3 noImplicitAny

### [개념]

`noImplicitAny`는 TypeScript가 암묵적으로 `any`로 추론하는 상황을 오류로 처리하는 옵션이다.

```json
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}
```

Function Parameter Type 누락을 잡는 데 특히 중요하다.

---

### [핵심]

noImplicitAny가 잡는 문제:

- Function Parameter Type 누락
- Callback Parameter Type 불명확
- Object Index Access Type 불명확
- this Type 불명확
- Generic Type 누락

오류 예:

```text
Parameter 'event' implicitly has an 'any' type.
```

---

### [실무]

나쁜 예:

```typescript
function handleChange(event) {
  return event.target.value;
}
```

개선:

```typescript
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): string {
  return event.target.value;
}
```

Callback 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function getTitles(festivals: Festival[]): string[] {
  return festivals.map((festival) => festival.title);
}
```

실무 기준:

- Function Parameter Type 명시
- React Event Type 명시
- API Function Parameter Type 명시
- any가 필요하면 범위와 이유를 주석으로 제한
- 최종 코드에서 implicit any 제거

---

### [FAQ]

Q. noImplicitAny는 뭐야?
A. TypeScript가 자동으로 any로 추론하는 상황을 오류로 처리하는 설정이다.

Q. Parameter implicitly has an any type 오류는 왜 나?
A. Function Parameter Type이 없고 TypeScript가 Type을 추론할 수 없기 때문이다.

Q. 해결하려면 어떻게 해?
A. parameter에 구체적인 Type을 명시한다.

---

## 1.4 strictNullChecks

### [개념]

`strictNullChecks`는 `null`과 `undefined`를 다른 Type과 구분해 엄격하게 검사하는 옵션이다.

```json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

이 옵션이 켜져 있으면 null 가능 값에 직접 property 접근을 할 수 없다.

---

### [핵심]

strictNullChecks가 잡는 문제:

- nullable value direct access
- optional property direct access
- undefined result handling
- find result handling
- nullable state handling
- API nullable field handling

주요 오류:

```text
Object is possibly 'null'.
Type 'undefined' is not assignable to type.
```

---

### [실무]

나쁜 예:

```typescript
type User = {
  nickname: string;
};

function getNickname(user: User | null): string {
  return user.nickname;
}
```

개선:

```typescript
function getNickname(user: User | null): string {
  return user?.nickname ?? "Guest";
}
```

find 결과 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function findTitle(festivals: Festival[], festivalId: number): string {
  const festival = festivals.find((item) => item.festivalId === festivalId);

  return festival?.title ?? "축제 없음";
}
```

실무 기준:

- API nullable field를 Type에 반영
- nullable state는 null guard 후 사용
- optional property는 fallback 처리
- find 결과 undefined 가능성 처리
- `as T`로 null 제거 금지

---

### [FAQ]

Q. strictNullChecks는 뭐야?
A. null과 undefined 가능성을 엄격하게 검사하는 TypeScript 옵션이다.

Q. Object is possibly null 오류는 왜 나?
A. 값이 null일 수 있는데 null check 없이 property나 method에 접근했기 때문이다.

Q. null 오류는 어떻게 해결해?
A. null check, optional chaining, nullish coalescing, Type Guard를 사용한다.

---

## 1.5 baseUrl and paths

### [개념]

`baseUrl`과 `paths`는 import 경로 alias를 설정하는 TypeScript 옵션이다.

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

Path Alias를 사용하면 긴 상대 경로를 줄이고 import 가독성을 높일 수 있다.

---

### [핵심]

Path Alias 장점:

- 긴 상대 경로 감소
- import path 일관성 향상
- 파일 이동 시 유지보수 편의
- Domain 구조 검색성 향상

주의:

- TypeScript 설정만으로 bundler가 항상 인식하는 것은 아님
- Vite / Webpack / Jest / ESLint 설정도 맞춰야 할 수 있음
- alias 남용 금지
- 실제 directory structure와 일치 필요

---

### [실무]

예:

```typescript
import type { ApiResponse } from "@/types/api";
import type { FestivalInfoResponse } from "@/features/festivals/types";
```

tsconfig 예:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/features/*": ["src/features/*"],
      "@/types/*": ["src/types/*"]
    }
  }
}
```

실무 기준:

- alias는 단순하게 유지
- `@/*` 하나로 충분한 경우가 많음
- bundler alias 설정과 일치
- 테스트 환경 alias 설정 확인
- path alias 오류는 tsconfig와 bundler 설정을 함께 검토

---

### [FAQ]

Q. baseUrl과 paths는 뭐야?
A. TypeScript import 경로 alias를 설정하는 옵션이다.

Q. tsconfig paths만 설정하면 Vite에서도 바로 돼?
A. 환경에 따라 Vite alias 설정도 필요할 수 있다.

Q. path alias는 꼭 써야 해?
A. 필수는 아니지만 프로젝트가 커지면 import 경로 관리에 도움이 된다.

---

# 2. JavaScript to TypeScript Migration

## 2.1 Migration Definition

### [개념]

JavaScript to TypeScript Migration은 기존 JavaScript / JSX 코드를 TypeScript / TSX 코드로 점진적으로 전환하는 작업이다.

```text
.js
→ .ts

.jsx
→ .tsx
```

Migration은 모든 파일을 한 번에 완벽하게 바꾸는 작업이 아니라 API Type, Props Type, State Type, Event Type부터 점진적으로 안정성을 높이는 작업이다.

---

### [핵심]

Migration 우선순위:

1. API Response Type
2. API Request Type
3. Component Props Type
4. Function Parameter Type
5. React Event Type
6. State Type
7. Form Data Type
8. Error Response Type
9. any 제거
10. strict mode 강화

Migration 핵심 원칙:

- 작은 단위로 전환
- Type 오류를 무작정 any로 숨기지 않음
- API Type 먼저 정의
- Component Props부터 안정화
- Event Type any 제거
- null / undefined 처리 강화

---

### [실무]

권장 Flow:

```text
1. TypeScript 설치 및 tsconfig 설정
2. .js 파일을 .ts로 변경
3. .jsx 파일을 .tsx로 변경
4. API Response Type 정의
5. API Request Type 정의
6. Props Type 정의
7. Event Handler Type 정의
8. State Type 정의
9. any 제거
10. strict true 적용 또는 단계적 적용
```

초기 Migration 예:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
};
```

실무 기준:

- API Layer부터 Type 안정화
- 공통 Type 파일 먼저 정리
- Page 단위보다 Feature 단위 Migration 권장
- any는 임시 TODO로 제한
- Review Agent는 any와 assertion 남용 확인

---

### [FAQ]

Q. JavaScript에서 TypeScript로 바꿀 때 어디부터 해?
A. API Response Type, Request Type, Props Type, Event Type, State Type부터 진행하는 것이 좋다.

Q. 모든 파일을 한 번에 바꿔야 해?
A. 아니다. 기능 단위 또는 파일 단위로 점진적으로 전환하는 것이 안전하다.

Q. Migration 중 any를 써도 돼?
A. 임시로는 가능하지만 범위를 제한하고 TODO로 추적한 뒤 제거해야 한다.

---

## 2.2 File Rename Strategy

### [개념]

File Rename Strategy는 JavaScript 파일 확장자를 TypeScript 확장자로 변경하는 기준이다.

```text
JavaScript Logic File
.js → .ts

React Component File
.jsx → .tsx
```

JSX 문법이 포함된 파일은 `.tsx`를 사용해야 한다.

---

### [핵심]

확장자 기준:

- `.js` → `.ts`
- `.jsx` → `.tsx`
- JSX 포함 TypeScript file → `.tsx`
- JSX 미포함 TypeScript file → `.ts`
- Type 선언 파일 → `.d.ts`

주의:

- JSX가 있으면 `.ts`가 아니라 `.tsx`
- 단순 utility file은 `.ts`
- API client file은 보통 `.ts`
- Component file은 보통 `.tsx`
- 파일명 변경 후 import 경로 확인

---

### [실무]

예:

```text
src/api/festivalApi.js
→ src/api/festivalApi.ts

src/components/FestivalCard.jsx
→ src/components/FestivalCard.tsx

src/utils/formatDate.js
→ src/utils/formatDate.ts
```

실무 기준:

- API / utils / types는 `.ts`
- React Component는 `.tsx`
- Hook에서 JSX를 반환하지 않으면 `.ts`도 가능하지만 React Hook 파일은 팀 컨벤션 확인
- 파일 rename 후 build error 확인
- 확장자 생략 import는 대부분 유지 가능

---

### [FAQ]

Q. .ts와 .tsx 차이는 뭐야?
A. `.tsx`는 JSX 문법을 포함할 수 있는 TypeScript 파일이고 `.ts`는 일반 TypeScript 파일이다.

Q. React Component는 무조건 .tsx야?
A. JSX를 반환하면 `.tsx`를 사용해야 한다.

Q. API 파일은 .ts야 .tsx야?
A. JSX를 포함하지 않으므로 보통 `.ts`를 사용한다.

---

## 2.3 Migration Order

### [개념]

Migration Order는 TypeScript 전환 시 어떤 파일과 Type을 먼저 처리할지 정하는 순서다.

효과가 큰 Type부터 적용하면 오류를 빠르게 줄일 수 있다.

---

### [핵심]

권장 순서:

```text
1. Common Type
2. API Type
3. API Client
4. Props Type
5. State Type
6. Event Handler
7. Form Type
8. Custom Hook Type
9. Utility Function Type
10. Error Type
```

우선순위 이유:

- API Type은 전체 데이터 흐름의 기준
- Props Type은 Component 계약 안정화
- Event Type은 any 제거 효과 큼
- State Type은 null / array 오류 방지
- Error Type은 사용자 경험 안정화

---

### [실무]

Feature 단위 Migration 예:

```text
Festival Feature Migration

1. festivalTypes.ts 생성
2. FestivalInfoResponse 정의
3. FestivalSearchParams 정의
4. festivalApi.ts Type 적용
5. FestivalCardProps 정의
6. FestivalList State Type 적용
7. Event Handler Type 적용
8. Error Handling Type 적용
```

실무 기준:

- Common Wrapper Type 먼저 정의
- Domain API Type 작성
- API Client Return Type 적용
- Component Props Type 적용
- State Type 적용
- Event Type any 제거
- Feature 단위로 완료 후 다음 Feature 진행

---

### [FAQ]

Q. Migration 순서는 왜 중요해?
A. API Type과 Props Type을 먼저 잡으면 이후 State, Event, UI Type 작업이 안정적으로 진행된다.

Q. Feature 단위 Migration이 좋아?
A. 좋다. 관련 API, Component, State를 함께 정리할 수 있어 추적이 쉽다.

Q. Common Type은 왜 먼저 만들어?
A. ApiResponse, SliceResponse, ErrorResponse 같은 공통 Type을 여러 Domain에서 재사용하기 때문이다.

---

## 2.4 any Removal Strategy

### [개념]

any Removal Strategy는 Migration 중 임시로 사용한 `any`를 구체적 Type 또는 `unknown`으로 점진적으로 대체하는 기준이다.

```text
any
→ specific type
→ unknown + narrowing
→ generic type
```

`any`는 TypeScript Type Check를 약화시키므로 최종 코드에서 제거하는 것이 목표다.

---

### [핵심]

any 대체 방식:

- API Response → Response Type
- API Request → Request Type
- Event → React Event Type
- Props → Props Type
- State → State Type
- 외부 unknown data → unknown + Type Guard
- 공통 구조 → Generic
- key-value map → Record

주의:

- any를 unknown으로 바꾸면 사용 전 Narrowing 필요
- any 제거는 기능 단위로 진행
- 무리한 제거보다 정확한 Type 정의 우선
- `as unknown as Type` 패턴 지양

---

### [실무]

나쁜 예:

```typescript
function handleChange(event: any) {
  return event.target.value;
}
```

개선:

```typescript
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): string {
  return event.target.value;
}
```

API any 제거:

```typescript
type FestivalInfoResponse = {
  festivalId: number;
  title: string;
};

async function getFestivals(): Promise<FestivalInfoResponse[]> {
  const response = await fetch("/api/festivals");
  return await response.json();
}
```

외부 데이터:

```typescript
function parseValue(value: unknown): string {
  if (typeof value === "string") {
    return value;
  }

  return "";
}
```

실무 기준:

- any 사용 위치 목록화
- Event any부터 제거
- API any 제거
- Props / State any 제거
- 외부 데이터는 unknown으로 전환
- TODO 주석은 제거 계획과 함께 작성

---

### [FAQ]

Q. any를 없애려면 어디부터 해야 해?
A. Event, API Response, Props, State에 있는 any부터 제거하는 것이 효과가 크다.

Q. any 대신 unknown을 쓰면 무조건 좋아?
A. unknown은 더 안전하지만 사용 전 Narrowing이 필요하다. 외부 데이터에 적합하다.

Q. `as unknown as Type`은 괜찮아?
A. 권장하지 않는다. Type 검증을 우회하므로 Type Guard나 정확한 Type 정의를 우선해야 한다.

---

# 3. Type Error Troubleshooting

## 3.1 Troubleshooting Flow

### [개념]

Type Error Troubleshooting은 TypeScript 오류 메시지를 기준으로 원인과 해결 방향을 찾는 과정이다.

```text
Error Message
→ Error Location
→ Expected Type
→ Actual Type
→ Data Source
→ Fix Type or Fix Code
```

Type Error는 무조건 TypeScript를 조용히 만드는 것이 아니라 실제 데이터 구조와 코드 의도를 맞추는 과정이다.

---

### [핵심]

Troubleshooting 확인 순서:

1. 오류 메시지 읽기
2. 오류 위치 확인
3. 기대 Type 확인
4. 실제 Type 확인
5. 값의 출처 확인
6. null / undefined 가능성 확인
7. API Response 구조 확인
8. Type 정의 수정
9. 코드 로직 수정
10. Assertion 남용 여부 확인

원칙:

- `as`로 바로 덮지 않음
- any로 숨기지 않음
- 실제 데이터 구조 확인
- Backend DTO 확인
- Runtime 변환 필요 여부 확인

---

### [실무]

Flow 예:

```text
Type 'string' is not assignable to type 'number'

확인:
1. string 값이 어디서 왔는가?
2. input value인가?
3. API 응답이 string인가?
4. 실제로 number가 필요한가?
5. Number() 변환이 필요한가?
6. 변환 실패 처리는 있는가?
```

실무 기준:

- 오류 메시지의 expected / actual Type 확인
- API Type 문제면 Network Response Body 확인
- Form input 문제면 string 기반으로 처리
- null 문제면 Type과 fallback 확인
- `as` 사용 전 Runtime 검증 가능성 확인

---

### [FAQ]

Q. Type Error가 나면 제일 먼저 뭘 봐야 해?
A. 오류 메시지에서 기대 Type과 실제 Type을 먼저 확인해야 한다.

Q. Type Error는 as로 해결하면 돼?
A. 권장하지 않는다. 실제 데이터 구조와 Type 정의가 맞는지 먼저 확인해야 한다.

Q. Type Error가 많으면 TypeScript를 끄는 게 좋아?
A. 아니다. 오류를 단계적으로 줄이되 any나 assertion으로 숨기지 않는 것이 좋다.

---

## 3.2 Type is not assignable Error

### [개념]

`Type 'A' is not assignable to type 'B'` 오류는 실제 값의 Type이 기대 Type과 맞지 않을 때 발생한다.

```text
Type 'string' is not assignable to type 'number'.
```

---

### [핵심]

주요 원인:

- string을 number에 할당
- null을 non-null Type에 할당
- undefined를 required Type에 할당
- literal union에 허용되지 않은 값 할당
- API Response Type 불일치
- Form input value Type 오해

---

### [실무]

문제 예:

```typescript
const page: number = "1";
```

개선:

```typescript
const page = Number("1");
```

literal union 오류:

```typescript
type SortOption = "latest" | "popular" | "rating";

const sort: SortOption = "newest";
```

개선:

```typescript
const sort: SortOption = "latest";
```

input value 예:

```typescript
function parsePage(value: string): number | null {
  const page = Number(value);

  if (Number.isNaN(page)) {
    return null;
  }

  return page;
}
```

실무 기준:

- 값 변환이 필요한지 확인
- literal union 허용 값 확인
- API 응답 실제 Type 확인
- nullable 여부 확인
- Type 수정과 Runtime 변환을 구분

---

### [FAQ]

Q. Type is not assignable 오류는 왜 나?
A. 실제 값의 Type이 기대 Type과 다르기 때문이다.

Q. string을 number에 넣으려면 어떻게 해?
A. `Number(value)` 같은 Runtime 변환을 사용하고 NaN 방어를 해야 한다.

Q. literal union 오류는 어떻게 해결해?
A. 허용된 literal 값만 사용하거나 Type 정의를 실제 허용 값에 맞게 수정한다.

---

## 3.3 Object is possibly null Error

### [개념]

`Object is possibly 'null'` 오류는 값이 null일 수 있는데 null check 없이 property나 method에 접근할 때 발생한다.

```text
Object is possibly 'null'.
```

---

### [핵심]

주요 원인:

- nullable state direct access
- nullable API field direct access
- selected item null 가능성
- current user null 가능성
- query result null 가능성
- ref null 가능성

해결 방식:

- null check
- optional chaining
- nullish coalescing
- conditional rendering
- Type Guard
- fallback value

---

### [실무]

문제 예:

```typescript
type User = {
  nickname: string;
};

function getNickname(user: User | null): string {
  return user.nickname;
}
```

개선:

```typescript
function getNickname(user: User | null): string {
  return user?.nickname ?? "Guest";
}
```

Conditional Rendering 기준:

```typescript
function getUserTitle(user: User | null): string {
  if (user === null) {
    return "로그인이 필요합니다.";
  }

  return user.nickname;
}
```

실무 기준:

- `T | null` 값은 사용 전 null guard
- nullable props는 fallback UI 처리
- nullable state는 loading 상태와 구분
- `as T`로 null 제거 금지
- null 가능성이 없으면 Type 정의 자체를 재검토

---

### [FAQ]

Q. Object is possibly null 오류는 왜 나?
A. 값이 null일 수 있는데 null check 없이 접근했기 때문이다.

Q. 해결 방법은 뭐야?
A. null check, optional chaining, nullish coalescing, fallback UI를 사용한다.

Q. `as User`로 해결해도 돼?
A. 권장하지 않는다. 실제로 null일 수 있으면 Runtime Error가 발생할 수 있다.

---

## 3.4 Property does not exist Error

### [개념]

`Property 'x' does not exist on type 'Y'` 오류는 Type에 정의되지 않은 property에 접근할 때 발생한다.

```text
Property 'name' does not exist on type 'Festival'.
```

---

### [핵심]

주요 원인:

- property 이름 오타
- Backend DTO field name 불일치
- Response Type과 ViewModel Type 혼동
- Union Type Narrowing 누락
- optional nested object 접근 오류
- snake_case / camelCase 불일치
- API wrapper data 구조 누락

---

### [실무]

문제 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function getName(festival: Festival): string {
  return festival.name;
}
```

개선:

```typescript
function getName(festival: Festival): string {
  return festival.title;
}
```

Wrapper 구조 오류:

```typescript
type ApiResponse<T> = {
  success: boolean;
  data: T;
  message: string;
};

function getFirstTitle(response: ApiResponse<Festival[]>): string {
  return response[0].title;
}
```

개선:

```typescript
function getFirstTitle(response: ApiResponse<Festival[]>): string {
  return response.data[0]?.title ?? "축제 없음";
}
```

실무 기준:

- property 이름 확인
- API Response Body 확인
- wrapper 구조 확인
- DTO field name 확인
- snake_case / camelCase mapping 확인
- Union Type이면 Narrowing 적용

---

### [FAQ]

Q. Property does not exist 오류는 왜 나?
A. Type에 없는 property에 접근했기 때문이다.

Q. API 응답에는 있는데 TypeScript가 없다고 해?
A. Frontend Type 정의가 실제 API Response와 다를 수 있다. Type을 수정해야 한다.

Q. wrapper 응답에서 data를 빼먹으면 오류가 나?
A. 그렇다. `ApiResponse<T>` 구조라면 실제 데이터는 `response.data`에 있다.

---

## 3.5 Type undefined is not assignable Error

### [개념]

`Type 'undefined' is not assignable to type` 오류는 undefined 가능 값이 undefined를 허용하지 않는 Type에 할당될 때 발생한다.

```text
Type 'undefined' is not assignable to type 'string'.
```

---

### [핵심]

주요 원인:

- optional property 사용
- optional parameter 사용
- find 결과 사용
- array index 접근
- query parameter undefined
- environment variable undefined
- optional callback result

해결 방식:

- fallback value
- undefined check
- Type 변경
- optional chaining
- nullish coalescing
- guard clause

---

### [실무]

문제 예:

```typescript
type SearchParams = {
  keyword?: string;
};

function getKeyword(params: SearchParams): string {
  return params.keyword;
}
```

개선:

```typescript
function getKeyword(params: SearchParams): string {
  return params.keyword ?? "";
}
```

find 예:

```typescript
type Festival = {
  festivalId: number;
  title: string;
};

function findFestivalTitle(festivals: Festival[], festivalId: number): string {
  const festival = festivals.find((item) => item.festivalId === festivalId);

  return festival?.title ?? "축제 없음";
}
```

실무 기준:

- optional property는 undefined 가능성 처리
- find 결과는 `T | undefined`
- array index 결과 undefined 가능성 고려
- 환경 변수는 undefined 가능성 처리
- fallback이 의미적으로 맞는지 확인

---

### [FAQ]

Q. undefined is not assignable 오류는 왜 나?
A. undefined가 올 수 있는 값을 undefined를 허용하지 않는 Type에 넣으려 해서 발생한다.

Q. optional property는 왜 undefined가 붙어?
A. property가 생략될 수 있기 때문이다.

Q. find 결과는 왜 undefined야?
A. 조건에 맞는 요소가 없을 수 있기 때문이다.

---

## 3.6 Parameter implicitly has any Error

### [개념]

`Parameter implicitly has an 'any' type` 오류는 Function Parameter Type이 명시되지 않았고 TypeScript가 추론할 수 없을 때 발생한다.

```text
Parameter 'event' implicitly has an 'any' type.
```

---

### [핵심]

주요 원인:

- function parameter type 누락
- event parameter type 누락
- callback parameter 추론 실패
- destructuring parameter type 누락
- props parameter type 누락
- noImplicitAny enabled

---

### [실무]

Event 예:

```typescript
function handleChange(event) {
  return event.target.value;
}
```

개선:

```typescript
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): string {
  return event.target.value;
}
```

Props Destructuring 예:

```typescript
function FestivalCard({ title }) {
  return null;
}
```

개선:

```typescript
type FestivalCardProps = {
  title: string;
};

function FestivalCard({ title }: FestivalCardProps) {
  return null;
}
```

실무 기준:

- Function Parameter Type 명시
- Props Type 정의 후 destructuring
- React Event Type 명시
- Callback Type Alias 활용
- noImplicitAny 오류를 any로 덮지 않음

---

### [FAQ]

Q. Parameter implicitly has any 오류는 왜 나?
A. parameter Type이 없고 TypeScript가 추론할 수 없기 때문이다.

Q. React event에서 이 오류가 나면 어떻게 해?
A. `ChangeEvent<HTMLInputElement>` 같은 React Event Type을 명시한다.

Q. Props destructuring에서 이 오류가 나면 어떻게 해?
A. Props Type을 정의하고 destructuring parameter에 적용한다.

---

# 4. Build and IDE Troubleshooting

## 4.1 TypeScript Build Error

### [개념]

TypeScript Build Error는 Type Check 또는 Compile 단계에서 발생하는 오류다.

Build Error는 Runtime 실행 전 코드의 Type 문제, module 문제, import 문제를 드러낸다.

---

### [핵심]

Build Error 주요 원인:

- Type Error
- import path error
- module resolution error
- tsconfig mismatch
- missing type package
- JSX setting error
- path alias bundler mismatch
- case sensitive path mismatch
- library type conflict

---

### [실무]

확인 순서:

```text
1. 오류 메시지 확인
2. 파일 경로 확인
3. import 경로 확인
4. Type 정의 확인
5. tsconfig include / paths 확인
6. bundler alias 확인
7. package type 설치 여부 확인
8. dev server / IDE 재시작
```

자주 발생하는 문제:

```text
Cannot find module '@/types/api'
```

확인:

- tsconfig paths 설정
- Vite alias 설정
- 실제 파일 위치
- 대소문자 일치
- IDE cache

실무 기준:

- Build Error는 Type Error와 Module Error를 구분
- Path Alias 오류는 tsconfig와 bundler 설정을 함께 확인
- Linux 배포 환경은 파일 대소문자에 민감
- IDE 오류와 실제 build 오류를 구분
- 불확실하면 `tsc --noEmit`으로 Type Check

---

### [FAQ]

Q. TypeScript Build Error가 나면 어디부터 봐?
A. 오류 메시지, 파일 경로, import 경로, tsconfig 설정을 먼저 확인한다.

Q. Cannot find module 오류는 왜 나?
A. 파일 경로, path alias, module resolution, 대소문자 불일치가 원인일 수 있다.

Q. IDE에서는 오류인데 build는 되면 어떻게 해?
A. IDE TypeScript server cache 문제일 수 있어 TypeScript server restart나 IDE 재시작을 시도한다.

---

## 4.2 IDE Type Error

### [개념]

IDE Type Error는 VS Code, WebStorm 같은 IDE가 TypeScript Language Server를 통해 표시하는 Type 오류다.

IDE 오류는 실제 TypeScript 설정, 캐시, tsconfig 인식 상태에 영향을 받는다.

---

### [핵심]

IDE 오류 원인:

- tsconfig 미인식
- TypeScript server cache
- workspace root 오류
- dependency type 미설치
- path alias 미인식
- stale build cache
- wrong TypeScript version
- monorepo project reference 문제

---

### [실무]

VS Code 확인:

```text
1. Command Palette 열기
2. TypeScript: Restart TS Server 실행
3. Workspace root 확인
4. tsconfig.json 위치 확인
5. npm install 상태 확인
6. node_modules 존재 확인
7. VS Code 재시작
```

TypeScript Version 확인:

```text
VS Code Status Bar
→ TypeScript Version
→ Workspace Version 사용 권장
```

실무 기준:

- IDE 오류와 CLI build 결과 비교
- tsconfig가 project root에 있는지 확인
- path alias 인식 여부 확인
- dependency type 설치 확인
- TypeScript server restart로 cache 갱신

---

### [FAQ]

Q. IDE에서만 Type 오류가 보이면 어떻게 해?
A. TypeScript server restart, workspace root 확인, tsconfig 인식 여부를 확인한다.

Q. VS Code가 tsconfig를 못 읽는 것 같으면?
A. project root를 제대로 열었는지 확인하고 tsconfig 위치를 확인한다.

Q. TypeScript 버전은 중요해?
A. 중요하다. 프로젝트의 workspace TypeScript version을 사용하는 것이 좋다.

---

# 5. Final Review Rules

## 5.1 TypeScript Foundation Review Scope

### [개념]

TypeScript Foundation Review Scope는 TypeScript Foundation 전체 문서가 Frontend Agent, Review Agent, PM Agent의 작업에 필요한 TypeScript 기본 기준을 충족하는지 검수하는 범위다.

이 문서 세트는 사람용 문법 암기 문서가 아니라 RAG Retrieval과 Agent Code Generation / Review를 위한 기준 문서다.

---

### [핵심]

최종 검수 대상:

- TypeScript Overview
- Runtime Model
- Type Annotation
- Type Inference
- Basic Type
- Object Type
- Union Type
- Literal Type
- Type Alias
- Interface
- Function Type
- Type Narrowing
- Type Guard
- Generic
- Utility Type
- API Request Type
- API Response Type
- React Props Type
- React State Type
- React Event Type
- tsconfig
- Migration
- Troubleshooting

---

### [실무]

Agent Review 기준:

```text
PM Agent
→ 요구사항의 TypeScript 영향 확인

Frontend Agent
→ Type-safe React / API Code 생성

Review Agent
→ any, nullable, API mismatch, event type, props type 검토

RAG Retrieval
→ FAQ / Retrieval Queries 기반 검색
```

검수 기준:

- 모든 Part에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 포함
- 모든 Part에 Retrieval Queries 포함
- 용어 통일
- Code Example 직접성 유지
- Runtime과 Compile Time 구분
- API Type과 ViewModel Type 구분
- Optional과 Nullable 구분
- any 남용 방지
- Type Assertion 남용 방지

---

### [FAQ]

Q. TypeScript Foundation 최종 검수 범위는 뭐야?
A. TypeScript 기본 문법, API Type, React TypeScript 준비, tsconfig, Migration, Troubleshooting 전체다.

Q. 이 문서 세트는 사람 공부용이야?
A. 아니다. RAG Retrieval과 Agent Code Generation / Review를 위한 기준 문서다.

Q. Review Agent는 무엇을 중점적으로 봐야 해?
A. any 남용, nullable 처리 누락, API Type 불일치, Props / State / Event Type 누락을 중점적으로 봐야 한다.

---

## 5.2 Cross-Part Consistency Check

### [개념]

Cross-Part Consistency Check는 Part01부터 Part12까지 용어, Type 예제, 설계 기준이 서로 충돌하지 않는지 확인하는 과정이다.

RAG 문서 세트는 파일 간 용어와 예제가 일관되어야 Retrieval 품질이 높아진다.

---

### [핵심]

파일 간 일관성 기준:

- Compile Time / Runtime 용어 일관성
- Type Annotation / Type Inference 기준 일관성
- Optional / Nullable 구분 일관성
- `string` / `String` 기준 일관성
- `any` / `unknown` 기준 일관성
- Type Alias / Interface 선택 기준 일관성
- Union / Enum 기준 일관성
- API Response / ViewModel 구분 일관성
- React Event Type 기준 일관성
- tsconfig strict 기준 일관성

---

### [실무]

검수 예:

```text
Part03
→ null / undefined 구분

Part04
→ Optional / Nullable Property 구분

Part05
→ Nullable Union

Part08
→ Null / Undefined Narrowing

Part11
→ Nullable Props / Nullable State

결론:
모든 문서에서 null / undefined / optional / nullable 기준이 일관되어야 함
```

API Type 검수 예:

```text
Part09
→ ApiResponse<T>, SliceResponse<T>, PageResponse<T>

Part10
→ API Request / Response Type

Part11
→ API Response to Props

결론:
API Generic Type과 React Props 연결 기준이 충돌하지 않아야 함
```

실무 기준:

- 같은 개념은 같은 용어 사용
- 같은 예제 Type 이름 반복 사용 가능
- API Type naming suffix 통일
- Response / Request / Props / State suffix 구분
- FAQ 질문 표현 반복 허용
- Retrieval Queries에서 핵심 질문 반복 강화

---

### [FAQ]

Q. Cross-Part Consistency Check는 왜 필요해?
A. 파일 간 용어와 기준이 다르면 RAG Retrieval과 Agent Code Generation 품질이 떨어지기 때문이다.

Q. FAQ 질문이 여러 Part에서 반복돼도 돼?
A. 된다. RAG Retrieval에서는 핵심 질문 반복이 검색 품질에 도움이 된다.

Q. 예제 Type 이름을 반복해도 돼?
A. 된다. FestivalInfoResponse, ApiResponse 같은 일관된 예제는 검색성과 이해에 도움이 된다.

---

## 5.3 Final Quality Checklist

### [개념]

Final Quality Checklist는 TypeScript Foundation 전체 문서 세트가 MASTER_RAG_RULES와 TypeScript Foundation Domain Rules를 충족하는지 확인하는 최종 검수 목록이다.

---

### [핵심]

최종 Checklist:

```md
- [ ] 모든 Part가 RAG Retrieval 최적화 구조인가?
- [ ] 모든 Part에 [개념] 섹션이 있는가?
- [ ] 모든 Part에 [핵심] 섹션이 있는가?
- [ ] 모든 Part에 [실무] 섹션이 있는가?
- [ ] 모든 Part에 [FAQ] 섹션이 있는가?
- [ ] 모든 Part 마지막에 Retrieval Queries가 있는가?
- [ ] [FAQ] 내부에 무분별한 ---가 없는가?
- [ ] Compile Time과 Runtime 구분이 일관적인가?
- [ ] Type Annotation과 Type Inference 기준이 일관적인가?
- [ ] Basic Type에서 Wrapper Type 사용 지양 기준이 포함되었는가?
- [ ] Optional과 Nullable 구분이 일관적인가?
- [ ] Union Type과 Literal Type 사용 기준이 명확한가?
- [ ] Type Alias와 Interface 선택 기준이 명확한가?
- [ ] Function Type과 Callback Type 기준이 명확한가?
- [ ] Type Narrowing과 Type Guard 기준이 명확한가?
- [ ] Generic과 Utility Type 남용 방지 기준이 있는가?
- [ ] API Request / Response / Error Type 기준이 명확한가?
- [ ] React Props / State / Event / Form Type 기준이 명확한가?
- [ ] tsconfig strict 기준이 포함되었는가?
- [ ] Migration 순서가 포함되었는가?
- [ ] Troubleshooting 기준이 포함되었는가?
- [ ] any 남용 방지 기준이 반복 강화되었는가?
- [ ] Type Assertion 남용 방지 기준이 반복 강화되었는가?
- [ ] API Response와 ViewModel 구분이 포함되었는가?
- [ ] Retrieval Queries가 충분히 많은가?
- [ ] Code Example이 짧고 직접적인가?
- [ ] 사람용 설명보다 Agent Retrieval 기준이 우선되는가?
```

---

### [실무]

최종 문서 세트 구성:

```text
TypeScript_Foundation_Part01_Overview_and_Runtime.md
TypeScript_Foundation_Part02_Type_Annotation_and_Inference.md
TypeScript_Foundation_Part03_Basic_Types.md
TypeScript_Foundation_Part04_Object_Types.md
TypeScript_Foundation_Part05_Union_and_Literal_Types.md
TypeScript_Foundation_Part06_Type_Alias_and_Interface.md
TypeScript_Foundation_Part07_Function_Types.md
TypeScript_Foundation_Part08_Type_Narrowing_and_Type_Guard.md
TypeScript_Foundation_Part09_Generic_and_Utility_Types.md
TypeScript_Foundation_Part10_API_Request_and_Response_Types.md
TypeScript_Foundation_Part11_React_TypeScript_Readiness.md
TypeScript_Foundation_Part12_tsconfig_Migration_Troubleshooting_Final_Review.md
```

Agent 연결:

```text
Frontend Agent
→ TypeScript Code 생성 기준

Review Agent
→ Type Error / any / nullable / API mismatch 검토 기준

PM Agent
→ Frontend Type 작업 범위 판단 기준

RAG Retrieval
→ FAQ / Retrieval Queries 기반 검색 기준
```

실무 기준:

- Part12 완료 후 TypeScript Foundation은 React Core 문서의 선행 기반으로 사용
- 다음 문서 흐름은 React Core Domain Rules 또는 React Core Part01로 연결
- TypeScript Foundation은 Frontend Foundation 단계의 Type Safety 기준 문서
- 추후 React Component Design / Data Fetching 문서에서 재참조 가능

---

### [FAQ]

Q. TypeScript Foundation 전체는 몇 Part야?
A. 12 Part 구성이 적합하다.

Q. TypeScript Foundation 완료 후 다음 문서는 뭐야?
A. React Core 문서로 진행하는 것이 적합하다.

Q. TypeScript Foundation은 어떤 Agent가 참조해?
A. Frontend Agent, Review Agent, PM Agent가 주로 참조한다.

Q. 최종 검수에서 가장 중요한 기준은?
A. RAG Retrieval 최적화, 용어 일관성, API / React Type 실무 기준, any / assertion 남용 방지다.

---

# 6. Common Mistakes

## 6.1 tsconfig Mistakes

### [개념]

tsconfig 실수는 TypeScript 설정과 실제 프로젝트 구조, bundler 설정, IDE 인식 상태가 맞지 않을 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- strict false로 방치
- noImplicitAny 비활성화
- strictNullChecks 비활성화
- include에 src 누락
- paths 설정 후 bundler alias 미설정
- moduleResolution 설정 불일치
- jsx 설정 오류
- tsconfig 위치 오류
- IDE가 다른 TypeScript version 사용
- skipLibCheck 의미 오해

---

### [실무]

Path Alias 실수:

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

문제 가능성:

- `baseUrl` 누락
- Vite alias 미설정
- Jest alias 미설정
- 실제 경로 대소문자 불일치

개선 기준:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}
```

실무 기준:

- tsconfig와 bundler 설정을 함께 확인
- strict 관련 옵션을 의도 없이 끄지 않음
- JSX 포함 프로젝트는 jsx option 확인
- IDE와 CLI 결과 비교
- 설정 변경 후 TS Server 재시작

---

### [FAQ]

Q. tsconfig에서 가장 흔한 실수는?
A. strict 관련 옵션을 끄거나 paths 설정과 bundler alias 설정을 맞추지 않는 것이다.

Q. paths 설정했는데 import가 안 되면?
A. baseUrl, bundler alias, 실제 파일 경로, 대소문자, IDE cache를 확인해야 한다.

Q. strict를 false로 두면 안 돼?
A. 가능은 하지만 Type Safety가 크게 낮아진다. 신규 프로젝트는 strict true가 권장된다.

---

## 6.2 Migration Mistakes

### [개념]

Migration 실수는 JavaScript 코드를 TypeScript로 바꾸는 과정에서 any로 오류를 숨기거나, API Type과 Props Type을 제대로 잡지 않고 파일 확장자만 바꿀 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- `.jsx`를 `.ts`로 변경
- API Type 없이 Component부터 전환
- 모든 오류를 any로 처리
- Event Type any 방치
- Props Type 누락
- State Type 누락
- null / undefined 오류를 assertion으로 제거
- Form input value Type 오해
- TypeScript 전환 후 Runtime 검증 생략
- Migration 범위를 너무 크게 잡음

---

### [실무]

나쁜 Migration:

```typescript
type Props = any;

function FestivalCard(props: Props) {
  return null;
}
```

개선:

```typescript
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  onSelect: (festivalId: number) => void;
};

function FestivalCard(props: FestivalCardProps) {
  return null;
}
```

실무 기준:

- 파일 확장자만 바꾸는 것은 Migration 완료가 아님
- API Type과 Props Type을 먼저 정리
- any는 임시 사용 후 제거
- Event Type을 명시
- Feature 단위로 작은 범위부터 진행
- strict 오류를 Type 개선 기회로 사용

---

### [FAQ]

Q. Migration에서 가장 흔한 실수는?
A. Type 오류를 any로 덮고 실제 Type 구조를 정의하지 않는 것이다.

Q. .jsx를 .ts로 바꿔도 돼?
A. JSX가 있으면 `.tsx`를 사용해야 한다.

Q. TypeScript Migration은 파일 확장자만 바꾸면 끝이야?
A. 아니다. API Type, Props Type, State Type, Event Type을 정의해야 실질적인 Migration이다.

---

## 6.3 Troubleshooting Mistakes

### [개념]

Troubleshooting 실수는 오류 메시지를 정확히 읽지 않고 `as`, `any`, `!` non-null assertion으로 Type Error를 억지로 없앨 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Error Message를 읽지 않고 any 적용
- `as Type`으로 API Response 단정
- non-null assertion `!` 남용
- Runtime 변환 없이 Type만 바꿈
- Form input string을 number로 Type만 변경
- nullable field를 non-null로 단정
- Backend DTO 확인 없이 Frontend Type 수정
- Network Response Body 확인 누락
- IDE cache 오류와 실제 build 오류 혼동

---

### [실무]

나쁜 예:

```typescript
const page = event.target.value as unknown as number;
```

문제:

- Runtime 값은 여전히 string이다.
- Type Assertion은 값 변환이 아니다.

개선:

```typescript
const page = Number(event.target.value);

if (Number.isNaN(page)) {
  throw new Error("Invalid page value");
}
```

Non-null Assertion 주의:

```typescript
const title = festival!.title;
```

문제:

- festival이 실제 null / undefined이면 Runtime Error 발생

개선:

```typescript
const title = festival?.title ?? "축제 없음";
```

실무 기준:

- Type Error 해결 전 실제 값 확인
- Runtime 변환과 Type 정의 구분
- non-null assertion 최소화
- API 문제는 Network Response Body 확인
- IDE 문제는 TS Server restart와 CLI build 비교

---

### [FAQ]

Q. Troubleshooting에서 가장 흔한 실수는?
A. Type Error를 any, as, non-null assertion으로 숨기는 것이다.

Q. non-null assertion `!`은 써도 돼?
A. 제한적으로 가능하지만 실제 null 가능성이 있으면 Runtime Error가 발생할 수 있어 주의해야 한다.

Q. Type만 number로 바꾸면 string이 number가 돼?
A. 아니다. Runtime 변환은 `Number()` 같은 함수로 해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. tsconfig.json이 뭐야?
A. TypeScript Compiler가 Project를 어떻게 해석하고 검사할지 정의하는 설정 파일이다.

Q. strict true는 꼭 켜야 해?
A. 신규 프로젝트에서는 권장한다. Type Safety와 오류 탐지 품질이 크게 좋아진다.

Q. tsconfig를 바꾸면 바로 적용돼?
A. 보통 적용되지만 IDE나 dev server가 이전 설정을 유지하면 재시작이 필요할 수 있다.

Q. strict mode는 뭐야?
A. TypeScript의 엄격한 Type Check 옵션 묶음이다.

Q. strict를 켜면 오류가 많아져?
A. 기존 코드에서는 많아질 수 있다. 하지만 실제 위험한 Type 문제를 미리 찾는 데 도움이 된다.

Q. strict 오류는 any로 없애도 돼?
A. 권장하지 않는다. Type을 명확히 정의하거나 null guard, Type Guard로 해결하는 것이 좋다.

Q. noImplicitAny는 뭐야?
A. TypeScript가 자동으로 any로 추론하는 상황을 오류로 처리하는 설정이다.

Q. Parameter implicitly has an any type 오류는 왜 나?
A. Function Parameter Type이 없고 TypeScript가 Type을 추론할 수 없기 때문이다.

Q. strictNullChecks는 뭐야?
A. null과 undefined 가능성을 엄격하게 검사하는 TypeScript 옵션이다.

Q. Object is possibly null 오류는 왜 나?
A. 값이 null일 수 있는데 null check 없이 property나 method에 접근했기 때문이다.

Q. baseUrl과 paths는 뭐야?
A. TypeScript import 경로 alias를 설정하는 옵션이다.

Q. tsconfig paths만 설정하면 Vite에서도 바로 돼?
A. 환경에 따라 Vite alias 설정도 필요할 수 있다.

Q. JavaScript에서 TypeScript로 바꿀 때 어디부터 해?
A. API Response Type, Request Type, Props Type, Event Type, State Type부터 진행하는 것이 좋다.

Q. 모든 파일을 한 번에 바꿔야 해?
A. 아니다. 기능 단위 또는 파일 단위로 점진적으로 전환하는 것이 안전하다.

Q. Migration 중 any를 써도 돼?
A. 임시로는 가능하지만 범위를 제한하고 TODO로 추적한 뒤 제거해야 한다.

Q. .ts와 .tsx 차이는 뭐야?
A. `.tsx`는 JSX 문법을 포함할 수 있는 TypeScript 파일이고 `.ts`는 일반 TypeScript 파일이다.

Q. React Component는 무조건 .tsx야?
A. JSX를 반환하면 `.tsx`를 사용해야 한다.

Q. API 파일은 .ts야 .tsx야?
A. JSX를 포함하지 않으므로 보통 `.ts`를 사용한다.

Q. Migration 순서는 왜 중요해?
A. API Type과 Props Type을 먼저 잡으면 이후 State, Event, UI Type 작업이 안정적으로 진행된다.

Q. Feature 단위 Migration이 좋아?
A. 좋다. 관련 API, Component, State를 함께 정리할 수 있어 추적이 쉽다.

Q. any를 없애려면 어디부터 해야 해?
A. Event, API Response, Props, State에 있는 any부터 제거하는 것이 효과가 크다.

Q. any 대신 unknown을 쓰면 무조건 좋아?
A. unknown은 더 안전하지만 사용 전 Narrowing이 필요하다. 외부 데이터에 적합하다.

Q. `as unknown as Type`은 괜찮아?
A. 권장하지 않는다. Type 검증을 우회하므로 Type Guard나 정확한 Type 정의를 우선해야 한다.

Q. Type Error가 나면 제일 먼저 뭘 봐야 해?
A. 오류 메시지에서 기대 Type과 실제 Type을 먼저 확인해야 한다.

Q. Type Error는 as로 해결하면 돼?
A. 권장하지 않는다. 실제 데이터 구조와 Type 정의가 맞는지 먼저 확인해야 한다.

Q. Type is not assignable 오류는 왜 나?
A. 실제 값의 Type이 기대 Type과 다르기 때문이다.

Q. string을 number에 넣으려면 어떻게 해?
A. `Number(value)` 같은 Runtime 변환을 사용하고 NaN 방어를 해야 한다.

Q. literal union 오류는 어떻게 해결해?
A. 허용된 literal 값만 사용하거나 Type 정의를 실제 허용 값에 맞게 수정한다.

Q. Object is possibly null 오류는 어떻게 해결해?
A. null check, optional chaining, nullish coalescing, fallback UI를 사용한다.

Q. Property does not exist 오류는 왜 나?
A. Type에 없는 property에 접근했기 때문이다.

Q. API 응답에는 있는데 TypeScript가 없다고 해?
A. Frontend Type 정의가 실제 API Response와 다를 수 있다. Type을 수정해야 한다.

Q. wrapper 응답에서 data를 빼먹으면 오류가 나?
A. 그렇다. `ApiResponse<T>` 구조라면 실제 데이터는 `response.data`에 있다.

Q. undefined is not assignable 오류는 왜 나?
A. undefined가 올 수 있는 값을 undefined를 허용하지 않는 Type에 넣으려 해서 발생한다.

Q. optional property는 왜 undefined가 붙어?
A. property가 생략될 수 있기 때문이다.

Q. find 결과는 왜 undefined야?
A. 조건에 맞는 요소가 없을 수 있기 때문이다.

Q. React event에서 implicit any 오류가 나면 어떻게 해?
A. `ChangeEvent<HTMLInputElement>` 같은 React Event Type을 명시한다.

Q. Props destructuring에서 implicit any 오류가 나면 어떻게 해?
A. Props Type을 정의하고 destructuring parameter에 적용한다.

Q. TypeScript Build Error가 나면 어디부터 봐?
A. 오류 메시지, 파일 경로, import 경로, tsconfig 설정을 먼저 확인한다.

Q. Cannot find module 오류는 왜 나?
A. 파일 경로, path alias, module resolution, 대소문자 불일치가 원인일 수 있다.

Q. IDE에서만 Type 오류가 보이면 어떻게 해?
A. TypeScript server restart, workspace root 확인, tsconfig 인식 여부를 확인한다.

Q. VS Code가 tsconfig를 못 읽는 것 같으면?
A. project root를 제대로 열었는지 확인하고 tsconfig 위치를 확인한다.

Q. TypeScript Foundation 전체는 몇 Part야?
A. 12 Part 구성이 적합하다.

Q. TypeScript Foundation 완료 후 다음 문서는 뭐야?
A. React Core 문서로 진행하는 것이 적합하다.

Q. TypeScript Foundation은 어떤 Agent가 참조해?
A. Frontend Agent, Review Agent, PM Agent가 주로 참조한다.

Q. TypeScript Foundation 최종 검수 범위는 뭐야?
A. TypeScript 기본 문법, API Type, React TypeScript 준비, tsconfig, Migration, Troubleshooting 전체다.

Q. Cross-Part Consistency Check는 왜 필요해?
A. 파일 간 용어와 기준이 다르면 RAG Retrieval과 Agent Code Generation 품질이 떨어지기 때문이다.

Q. FAQ 질문이 여러 Part에서 반복돼도 돼?
A. 된다. RAG Retrieval에서는 핵심 질문 반복이 검색 품질에 도움이 된다.

Q. tsconfig에서 가장 흔한 실수는?
A. strict 관련 옵션을 끄거나 paths 설정과 bundler alias 설정을 맞추지 않는 것이다.

Q. paths 설정했는데 import가 안 되면?
A. baseUrl, bundler alias, 실제 파일 경로, 대소문자, IDE cache를 확인해야 한다.

Q. Migration에서 가장 흔한 실수는?
A. Type 오류를 any로 덮고 실제 Type 구조를 정의하지 않는 것이다.

Q. .jsx를 .ts로 바꿔도 돼?
A. JSX가 있으면 `.tsx`를 사용해야 한다.

Q. TypeScript Migration은 파일 확장자만 바꾸면 끝이야?
A. 아니다. API Type, Props Type, State Type, Event Type을 정의해야 실질적인 Migration이다.

Q. Troubleshooting에서 가장 흔한 실수는?
A. Type Error를 any, as, non-null assertion으로 숨기는 것이다.

Q. non-null assertion `!`은 써도 돼?
A. 제한적으로 가능하지만 실제 null 가능성이 있으면 Runtime Error가 발생할 수 있어 주의해야 한다.

Q. Type만 number로 바꾸면 string이 number가 돼?
A. 아니다. Runtime 변환은 `Number()` 같은 함수로 해야 한다.

Q. TypeScript Part12의 핵심은 뭐야?
A. tsconfig strict 기준, JavaScript to TypeScript Migration 순서, Type Error Troubleshooting, 전체 문서 Final Review 기준을 정리하는 것이다.

Q. TypeScript Foundation 다음 흐름은 뭐야?
A. React Core → React Component Design → React Router → State Management → Data Fetching & REST API Integration 순서가 적합하다.
