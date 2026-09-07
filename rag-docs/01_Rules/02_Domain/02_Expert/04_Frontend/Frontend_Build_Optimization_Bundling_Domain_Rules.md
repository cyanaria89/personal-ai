# Frontend Build Optimization / Bundling Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Build Optimization / Bundling Domain 목적

### [개념]

Frontend Build Optimization / Bundling Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent / Performance Review Agent용 RAG 문서 제작 규칙이다.

Frontend Build Optimization은 프론트엔드 애플리케이션의 빌드 결과물을 더 작고, 빠르고, 안정적이며, 배포 친화적으로 만드는 영역이다.

Bundling은 JavaScript, TypeScript, CSS, 이미지, 폰트, 정적 자산, 외부 의존성을 브라우저가 효율적으로 로드할 수 있는 형태로 묶고 분리하는 과정이다.

목적:

- 프론트엔드 빌드 구조 설계 지원
- 번들 크기 최적화 지원
- Code Splitting / Lazy Loading 기준 제공
- Tree Shaking / Dead Code Elimination 기준 제공
- Chunk Strategy 설계 지원
- Dependency 분석 및 최적화 지원
- Dynamic Import 기준 제공
- CSS / Asset / Font 번들링 최적화 지원
- Source Map / Debug Build 기준 제공
- Next.js App Router 빌드 최적화 지원
- CI Build Cache / Monorepo Build 최적화 지원
- Bundle Analyzer 기반 코드 리뷰 지원
- 성능 회귀 방지 기준 제공

---

### [핵심]

우선순위:

1. Bundle Size Analysis
2. Code Splitting
3. Route-based Splitting
4. Dynamic Import
5. Tree Shaking
6. Dead Code Elimination
7. Dependency Optimization
8. Chunk Strategy
9. CSS Bundling
10. Asset Optimization
11. Font Optimization
12. Source Map Strategy
13. Build Cache
14. Transpilation Target
15. Minification
16. Compression
17. Next.js Build Optimization
18. CI Build Performance
19. Bundle Regression Prevention
20. Code Review Criteria

---

### [실무]

2026 실무 기준:

- React / TypeScript / Next.js App Router 기준 예제 우선
- 초기 번들 크기와 route별 chunk 크기를 분리해서 분석
- Bundle Analyzer 결과 기반으로 판단
- 모든 코드를 initial bundle에 넣지 않음
- route / feature / heavy component 단위 code splitting 검토
- Tree Shaking이 잘 되도록 ESM, side effects, import 방식 점검
- 큰 라이브러리 추가 시 대체안과 bundle impact 검토
- Dynamic Import는 UX와 loading fallback을 함께 설계
- CSS / image / font도 build optimization 대상에 포함
- Source Map은 debugging과 보안 / 배포 정책을 함께 고려
- CI에서는 build cache, dependency cache, affected build 전략 검토
- 성능 회귀 방지를 위해 bundle budget과 PR diff를 활용
- Agent가 빌드 산출물과 번들 구조를 리뷰할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Build Optimization / Bundling 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 프로젝트에서 번들 크기, chunk 구조, dependency, tree shaking, dynamic import, asset, CSS, font, source map, CI build를 최적화하도록 돕는 RAG 문서 제작 규칙이다.

Q. Build Optimization은 성능 최적화와 같은가?

A.
겹치지만 완전히 같지는 않다. Build Optimization은 빌드 산출물과 로딩 구조를 최적화하고, Performance Tuning은 런타임 렌더링과 사용자 체감 성능까지 포함한다.

Q. Bundling에서 가장 먼저 봐야 할 것은?

A.
초기 JavaScript 크기, route별 chunk, 중복 dependency, tree shaking 실패, 큰 라이브러리, dynamic import 대상이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Build Optimization / Bundling Domain은 프론트엔드 앱의 빌드 결과물, 의존성, chunk, asset, cache, source map, CI build 성능을 포함한다.

---

### [핵심]

포함 범위:

- Build Optimization
- Bundling
- Bundle Size
- Initial Bundle
- Route Chunk
- Shared Chunk
- Vendor Chunk
- Code Splitting
- Route-based Splitting
- Component-based Splitting
- Dynamic Import
- Lazy Loading
- Tree Shaking
- Dead Code Elimination
- Side Effects
- ESM
- CJS
- Dependency Optimization
- Bundle Analyzer
- Chunk Strategy
- Minification
- Compression
- Gzip
- Brotli
- Transpilation Target
- Polyfill
- CSS Bundling
- CSS Code Splitting
- CSS Modules
- CSS-in-JS Build Cost
- Tailwind CSS Purge
- Asset Optimization
- Image Optimization
- SVG Optimization
- Font Optimization
- Source Map
- Production Build
- Development Build
- Build Cache
- Incremental Build
- CI Build Cache
- Monorepo Build
- Turbopack
- Webpack
- Vite
- Rollup
- ESBuild
- SWC
- Next.js Build
- App Router Build
- Server Component Bundle
- Client Component Bundle
- Bundle Budget
- Bundle Regression
- Build Troubleshooting

---

### [실무]

제외 범위:

- Bundler 내부 구현 심화
- Compiler 이론 심화
- Browser Engine 내부 로딩 구현 심화
- CDN 운영 심화
- Backend Build Optimization 심화
- Kubernetes / Infra Build Pipeline 심화
- Native Mobile Build 심화
- WebAssembly 최적화 심화
- Performance Tuning 전체
- Security 전체

단, Frontend Build 판단에 필요한 수준의 성능, 보안, CI, 배포, source map, dependency security 지식은 포함 가능하다.

---

### [FAQ]

Q. Webpack / Vite / Turbopack 사용법 전체를 포함해야 하나?

A.
아니다. 도구별 전체 설정법보다 번들 구조, chunk 전략, tree shaking, dependency 분석, build 회귀 방지 기준에 집중한다.

Q. Frontend Performance 문서와 중복되지 않나?

A.
중복을 최소화한다. 이 문서는 빌드 산출물과 번들 구조 최적화에 집중하고, 런타임 렌더링 최적화는 Performance 문서와 연결한다.

Q. Security 문서와도 연결되나?

A.
그렇다. Source Map 공개, secret bundle 포함, dependency 취약점, third-party script는 Build Optimization에서도 검토해야 한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Build Optimization / Bundling RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

Build Optimization 문서는 빌드 분석 → 원인 진단 → 분리 / 제거 / 압축 → 회귀 방지 흐름이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Analyze → Identify → Split / Remove → Verify → Budget
- `[Comparison]`: Initial Bundle vs Route Chunk, ESM vs CJS
- `[Best Practice]`: Bundle Analyzer, Dynamic Import, Tree Shaking
- `[Troubleshooting]`: Tree Shaking 실패, chunk 과다 분리, build 느림
- `[Checklist]`: Build Optimization 코드 리뷰

---

### [FAQ]

Q. Build Optimization 문서에 Flow가 필요한 이유는?

A.
번들 최적화는 추측으로 하는 것이 아니라 분석, 원인 식별, 개선, 검증, 회귀 방지 흐름으로 진행해야 하기 때문이다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Build Optimization Core Concept Rules

## 4.1 Build Optimization 기본 개념

### [개념]

Build Optimization은 프론트엔드 소스 코드와 의존성을 브라우저가 효율적으로 내려받고 실행할 수 있는 산출물로 만드는 과정이다.

Bundling은 여러 파일을 chunk 단위로 묶고, 필요 없는 코드를 제거하며, 압축하고, cache 가능한 파일명으로 배포하는 과정이다.

---

### [핵심]

핵심 목표:

- Initial Bundle 축소
- Route Chunk 최적화
- 불필요한 코드 제거
- 중복 dependency 제거
- Tree Shaking 개선
- Code Splitting 적용
- Lazy Loading 적용
- CSS / Asset 최적화
- Font Loading 최적화
- Source Map 정책 수립
- Build 시간 단축
- Cache 효율 개선
- Bundle Regression 방지

기본 Flow:

```text
Bundle Analyzer 실행
→ Initial Bundle / Route Chunk 확인
→ 큰 dependency 확인
→ 중복 chunk 확인
→ Tree Shaking 실패 확인
→ Dynamic Import 후보 선정
→ 개선 적용
→ Build 결과 재측정
→ Bundle Budget 설정
```

---

### [실무]

작성 기준:

- 먼저 측정하고 나중에 최적화
- Lighthouse 점수만 보지 말고 실제 bundle 분석
- initial JS와 route별 JS를 분리해서 확인
- 큰 라이브러리는 import 방식과 대체안 검토
- user path와 business critical route 기준으로 우선순위 설정
- 코드 분리는 loading fallback과 UX를 함께 고려
- 압축 전 크기와 gzip / brotli 후 크기를 구분
- dependency 추가 PR에는 bundle impact 확인
- build cache와 CI 속도도 품질 요소로 다룸
- 운영 build와 개발 build 차이를 명확히 구분

---

### [FAQ]

Q. Build Optimization에서 가장 중요한 원칙은?

A.
추측하지 말고 Bundle Analyzer와 build output을 기준으로 병목을 확인한 뒤 개선하는 것이다.

Q. 번들 크기가 작으면 항상 좋은가?

A.
대체로 좋지만 지나친 code splitting은 요청 수와 UX 복잡도를 늘릴 수 있으므로 균형이 필요하다.

Q. Initial Bundle이 중요한 이유는?

A.
초기 화면 로딩과 JavaScript parse / execute 비용에 직접 영향을 주기 때문이다.

---

# 5. Bundle Analysis Rules

## 5.1 Bundle Analyzer 기준

### [개념]

Bundle Analysis는 빌드 산출물에서 어떤 코드와 dependency가 어느 chunk에 포함되었는지 분석하는 과정이다.

---

### [핵심]

분석 대상:

- Initial Bundle Size
- Route Chunk Size
- Shared Chunk
- Vendor Chunk
- Duplicated Module
- Large Dependency
- Unused Code
- Tree Shaking Failure
- CSS Bundle
- Asset Size
- Source Map Size
- Gzip Size
- Brotli Size

---

### [실무]

작성 기준:

- Bundle Analyzer를 기준으로 큰 dependency 식별
- initial bundle과 lazy chunk를 구분
- route별로 필요한 코드만 포함되는지 확인
- 공통 chunk에 너무 많은 코드가 들어가지 않는지 확인
- 같은 dependency가 여러 chunk에 중복 포함되는지 확인
- 압축 전 크기와 압축 후 전송 크기를 함께 확인
- bundle 크기만 보지 말고 parse / execute 비용도 고려
- heavy library는 사용 기능 대비 비용 검토
- build 전후 diff를 기록
- PR에서 bundle impact 표시 가능

예시 분석 질문:

```text
어떤 dependency가 initial bundle에 가장 크게 들어갔는가?
이 dependency는 첫 화면에 꼭 필요한가?
route별 chunk로 분리할 수 있는가?
더 작은 대체 라이브러리가 있는가?
import 방식 때문에 전체 라이브러리가 포함되었는가?
```

---

### [FAQ]

Q. Bundle Analyzer는 왜 필요한가?

A.
어떤 코드와 dependency가 번들을 크게 만드는지 실제 빌드 결과를 기준으로 확인하기 위해 필요하다.

Q. gzip 크기만 보면 충분한가?

A.
아니다. 전송 크기는 gzip / brotli가 중요하지만 브라우저 parse / execute 비용은 원본 JavaScript 크기와 복잡도에도 영향을 받는다.

Q. 큰 dependency가 보이면 무조건 제거해야 하나?

A.
아니다. 핵심 기능에 필요하면 유지할 수 있지만 lazy loading, 대체안, import 방식 최적화를 검토해야 한다.

---

# 6. Code Splitting Rules

## 6.1 Code Splitting 기준

### [개념]

Code Splitting은 전체 JavaScript를 하나의 큰 bundle로 보내지 않고, route, feature, component, dependency 단위로 나누어 필요한 시점에 로드하는 전략이다.

---

### [핵심]

분리 기준:

- Route-based Splitting
- Component-based Splitting
- Feature-based Splitting
- Dependency-based Splitting
- Vendor Splitting
- Dynamic Import
- Lazy Loading
- Conditional Loading

적합 대상:

- Admin Page
- Chart Library
- Rich Text Editor
- Map SDK
- Payment SDK
- Code Editor
- Markdown Preview
- Heavy Modal
- Rarely Used Feature
- Below-the-fold Component

---

### [실무]

작성 기준:

- route 단위 splitting 우선
- 첫 화면에 필요 없는 heavy component는 lazy loading 검토
- 관리자 / 설정 / 대시보드 같은 별도 route는 분리
- chart / map / editor / payment SDK는 필요 시점 로드 검토
- code splitting에는 loading fallback 포함
- 사용자 행동 직전에 prefetch 가능
- 너무 작은 chunk를 과도하게 만들지 않기
- 분리 후 실제 initial bundle 감소 확인
- chunk load error 처리 검토
- SSR / RSC / Client Component 경계 고려

예시:

```tsx
const ChartPanel = dynamic(() => import("./ChartPanel"), {
  loading: () => <p>차트를 불러오는 중입니다.</p>,
});
```

주의:

- dynamic import는 네트워크 요청을 추가함
- 사용자가 즉시 필요한 UI를 너무 늦게 로드하면 UX가 나빠짐
- 너무 잘게 쪼개면 request overhead 증가
- lazy component에 error boundary 필요 가능
- split 후 실제 개선이 있었는지 측정 필요

---

### [FAQ]

Q. Code Splitting은 언제 해야 하나?

A.
첫 화면에 필요 없는 무거운 기능, 특정 route에서만 쓰는 코드, 사용 빈도가 낮은 component, 큰 외부 library에 적용한다.

Q. 모든 component를 lazy loading하면 좋은가?

A.
아니다. 너무 작은 component까지 분리하면 요청 수와 loading 상태가 늘어 UX가 나빠질 수 있다.

Q. Code Splitting 후 무엇을 확인해야 하나?

A.
Initial bundle 감소, route chunk 크기, loading UX, chunk load error, 실제 사용자 성능 변화를 확인해야 한다.

---

# 7. Dynamic Import Rules

## 7.1 Dynamic Import 기준

### [개념]

Dynamic Import는 특정 코드나 dependency를 초기 로딩 시점이 아니라 필요한 시점에 비동기로 가져오는 방식이다.

---

### [핵심]

사용 대상:

- Heavy Component
- Client-only Component
- Browser-only Library
- Chart Library
- Map Library
- Editor Library
- Markdown Renderer
- PDF Viewer
- Search Worker
- Payment SDK
- Analytics SDK

---

### [실무]

작성 기준:

- 브라우저 API에 의존하는 library는 client-only dynamic import 검토
- 첫 화면에 필요 없는 heavy component 분리
- 사용자가 버튼을 누른 뒤 필요한 기능은 event 시점 import 가능
- loading fallback 제공
- import 실패 처리 검토
- prefetch 가능 여부 검토
- SSR 비활성화가 필요한 경우 이유 명확화
- dynamic import가 tree shaking을 방해하지 않는지 확인
- 동일 dependency가 여러 lazy chunk에 중복되지 않는지 분석
- TypeScript type import와 runtime import 구분

예시:

```ts
async function openEditor() {
  const { createEditor } = await import("./editor/createEditor");
  createEditor();
}
```

주의:

- dynamic import는 성능 개선이 아니라 로딩 시점 이동
- 사용 직전에 로드하면 지연이 체감될 수 있음
- SSR off는 SEO / 초기 렌더링 영향 검토
- dynamic import 경로가 너무 동적이면 bundler 최적화 어려움
- loading / error UX 없으면 빈 화면이 될 수 있음

---

### [FAQ]

Q. Dynamic Import는 언제 유용한가?

A.
초기 화면에 필요 없는 무거운 component나 browser-only library를 필요한 시점에 로드할 때 유용하다.

Q. Dynamic Import를 쓰면 번들 크기가 줄어드나?

A.
전체 코드량은 같을 수 있지만 initial bundle에서 분리되어 초기 로딩 부담이 줄어든다.

Q. Dynamic Import의 단점은?

A.
추가 네트워크 요청과 loading 지연이 생기며, 실패 처리와 fallback UI가 필요하다.

---

# 8. Tree Shaking Rules

## 8.1 Tree Shaking 기준

### [개념]

Tree Shaking은 실제로 사용하지 않는 export와 dead code를 빌드 과정에서 제거하는 최적화이다.

Tree Shaking이 잘 되려면 ESM 구조, side effect 정보, import 방식이 중요하다.

---

### [핵심]

필수 조건:

- ESM
- Static Import
- Pure Module
- Side Effects Metadata
- Dead Code Elimination
- Minification
- Named Export
- Import Path Optimization

Tree Shaking 방해 요소:

- CommonJS
- Dynamic Require
- Side Effect Module
- Namespace Import Misuse
- Barrel Export Misuse
- Global Mutation
- Polyfill Side Effects
- CSS Side Effects

---

### [실무]

작성 기준:

- 가능하면 ESM package 사용
- 필요한 함수만 named import
- 큰 라이브러리의 root import 주의
- side effect가 있는 module은 명확히 분리
- package.json의 `sideEffects` 설정 이해
- barrel file이 tree shaking을 방해하는지 확인
- lodash 같은 utility는 import 방식 점검
- icon library는 개별 import 확인
- moment처럼 큰 locale 포함 library 주의
- tree shaking 결과는 bundle analyzer로 확인

예시:

```ts
import { format } from "date-fns";
```

주의:

- named import라고 항상 tree shaking이 보장되는 것은 아님
- package가 CJS이면 제거가 어려울 수 있음
- barrel export가 모든 module을 끌고 올 수 있음
- CSS import는 side effect로 취급될 수 있음
- tree shaking은 production build에서 확인해야 함

---

### [FAQ]

Q. Tree Shaking은 무엇인가?

A.
사용하지 않는 export와 dead code를 빌드 결과에서 제거하는 최적화이다.

Q. Tree Shaking이 안 되는 이유는?

A.
CommonJS, side effect, dynamic require, 잘못된 import 방식, barrel export, package 설정 문제 때문일 수 있다.

Q. Named import를 쓰면 항상 tree shaking되나?

A.
항상 그렇지는 않다. 라이브러리의 module 형식과 side effect 설정, bundler 동작에 따라 달라진다.

---

# 9. Dependency Optimization Rules

## 9.1 Dependency 최적화

### [개념]

Dependency Optimization은 외부 라이브러리가 번들 크기, 빌드 시간, 보안, 런타임 성능에 미치는 영향을 분석하고 관리하는 전략이다.

---

### [핵심]

검토 대상:

- Large Dependency
- Duplicate Dependency
- Transitive Dependency
- Polyfill-heavy Dependency
- CJS Dependency
- Tree-shaking-unfriendly Dependency
- Date Library
- Chart Library
- Icon Library
- Utility Library
- UI Library
- Editor Library
- Map SDK
- Analytics SDK

---

### [실무]

작성 기준:

- 새 dependency 추가 전 필요성 검토
- native API로 대체 가능한지 확인
- 작은 유틸 때문에 큰 라이브러리 추가 금지
- 같은 역할의 dependency 중복 확인
- dependency별 bundle impact 확인
- ESM 지원 여부 확인
- browser build에 server-only dependency 포함 금지
- icon library는 필요한 icon만 포함되도록 확인
- locale / timezone 데이터가 과도하게 포함되는지 확인
- chart / editor / map library는 lazy loading 검토
- dependency update 후 bundle diff 확인

예시 검토 질문:

```text
이 라이브러리는 initial bundle에 들어가는가?
사용하는 기능 대비 크기가 적절한가?
더 작은 대체안이 있는가?
ESM과 tree shaking을 지원하는가?
같은 기능의 기존 dependency가 있는가?
```

---

### [FAQ]

Q. Dependency Optimization은 왜 중요한가?

A.
외부 라이브러리는 번들 크기, 초기 로딩, 빌드 시간, 보안 위험에 큰 영향을 줄 수 있기 때문이다.

Q. 작은 기능 하나 때문에 큰 라이브러리를 써도 되나?

A.
주의해야 한다. native API나 작은 대체 라이브러리, 직접 구현이 더 나을 수 있다.

Q. Dependency 중복은 어떻게 찾나?

A.
Bundle Analyzer, package manager dedupe, lockfile 분석, dependency tree 확인을 통해 찾는다.

---

# 10. Chunk Strategy Rules

## 10.1 Chunk 설계 기준

### [개념]

Chunk Strategy는 빌드 결과물이 어떤 단위로 분리되고, 어떤 chunk가 초기 로드되며, 어떤 chunk가 route나 사용자 행동에 따라 로드되는지 결정하는 전략이다.

---

### [핵심]

Chunk 유형:

- Entry Chunk
- Initial Chunk
- Route Chunk
- Shared Chunk
- Vendor Chunk
- Async Chunk
- Runtime Chunk
- CSS Chunk

설계 목표:

- 초기 로딩 최소화
- 중복 코드 최소화
- cache 효율 증가
- route 이동 성능 개선
- chunk load error 관리
- 지나친 chunk 분할 방지

---

### [실무]

작성 기준:

- 공통 dependency는 shared chunk로 분리 가능
- 모든 vendor를 하나의 거대한 chunk에 넣지 않도록 검토
- 자주 바뀌는 앱 코드와 잘 안 바뀌는 vendor code 분리
- route별 chunk가 독립적으로 로드되는지 확인
- admin / dashboard / editor 같은 heavy route는 분리
- shared chunk가 너무 커지면 route별 로딩 비용 증가
- 작은 chunk가 너무 많으면 request overhead 증가
- long-term cache를 위해 content hash 사용
- chunk naming과 source map 추적 가능성 확보
- chunk load failure에 fallback / reload 전략 검토

주의:

- Vendor chunk를 무조건 크게 분리하면 초기 비용이 커질 수 있음
- shared chunk가 모든 route에 강제로 로드되면 오히려 악화
- dynamic import 남용은 chunk 폭증 원인
- chunk splitting은 HTTP/2 / HTTP/3 환경과 cache 전략을 함께 고려
- 실제 네트워크 waterfall로 확인 필요

---

### [FAQ]

Q. Chunk를 많이 나누면 좋은가?

A.
항상 그렇지 않다. 초기 로딩은 줄 수 있지만 요청 수와 loading 상태가 늘어날 수 있다.

Q. Vendor Chunk는 무엇인가?

A.
외부 dependency를 앱 코드와 분리한 chunk이다. cache 효율을 높일 수 있지만 너무 커지면 초기 로딩 부담이 된다.

Q. Shared Chunk가 너무 크면 왜 문제인가?

A.
많은 route에서 불필요한 코드까지 함께 로드되어 초기 비용이 증가할 수 있다.

---

# 11. Transpilation and Polyfill Rules

## 11.1 Transpilation Target / Polyfill 기준

### [개념]

Transpilation은 최신 JavaScript / TypeScript 코드를 대상 브라우저가 이해할 수 있는 문법으로 변환하는 과정이다.

Polyfill은 대상 브라우저에 없는 API를 보완하는 코드이다.

---

### [핵심]

검토 대상:

- Browser Target
- Browserslist
- Transpilation Target
- Legacy Browser
- Modern Browser
- Polyfill
- Core-js
- Differential Loading
- SWC
- Babel
- TypeScript Compile
- JSX Transform

---

### [실무]

작성 기준:

- 지원 브라우저 범위를 명확히 정의
- 너무 오래된 브라우저 지원은 bundle 크기 증가
- 필요 없는 polyfill 제거
- polyfill은 전역 side effect를 가질 수 있음
- modern browser target으로 불필요한 변환 줄이기
- TypeScript type check와 transpile 역할 구분
- Babel plugin 남용 금지
- SWC / ESBuild 같은 빠른 compiler 활용 가능
- 외부 dependency transpilation 필요 여부 검토
- bundle output이 실제 대상 브라우저에서 동작하는지 테스트

주의:

- target이 낮으면 코드가 길어지고 polyfill이 늘어남
- polyfill 중복 포함 주의
- server bundle과 client bundle의 target이 다를 수 있음
- node-only API가 browser bundle에 포함되지 않게 주의
- browserslist 변경 후 bundle diff 확인

---

### [FAQ]

Q. Transpilation Target은 왜 중요한가?

A.
지원 브라우저 범위에 따라 변환 코드와 polyfill이 달라져 bundle 크기와 호환성에 영향을 주기 때문이다.

Q. 오래된 브라우저를 많이 지원하면 무엇이 문제인가?

A.
더 많은 transpilation과 polyfill이 필요해 bundle이 커지고 빌드 복잡도가 증가할 수 있다.

Q. Polyfill은 많이 넣으면 안전한가?

A.
아니다. bundle 크기 증가와 side effect, 중복 포함 문제가 생길 수 있으므로 필요한 것만 포함해야 한다.

---

# 12. Minification and Compression Rules

## 12.1 Minification / Compression 기준

### [개념]

Minification은 JavaScript / CSS에서 공백, 주석, 불필요한 코드를 제거하고 식별자를 줄여 파일 크기를 줄이는 과정이다.

Compression은 서버나 CDN에서 gzip, brotli 같은 방식으로 전송 크기를 줄이는 과정이다.

---

### [핵심]

최적화 대상:

- JavaScript Minification
- CSS Minification
- HTML Minification
- Gzip
- Brotli
- Terser
- SWC Minify
- ESBuild Minify
- Compression Header
- Static Asset Compression

---

### [실무]

작성 기준:

- Production build에서 minification 활성화
- console 제거 여부 정책 검토
- dead code 제거와 minification 연결
- gzip / brotli 전송 설정 확인
- 압축 전 크기와 압축 후 크기 모두 측정
- source map과 minified code 연결
- license comment 보존 정책 검토
- minification으로 인한 runtime 오류 확인
- CDN / hosting provider compression 설정 확인
- 이미 압축된 이미지 / font는 중복 압축 효과 제한적

주의:

- Minification은 보안 기능이 아님
- 압축 후 크기가 작아도 parse / execute 비용은 남음
- source map 없으면 production debugging 어려움
- console 제거가 debugging / observability에 영향 가능
- 잘못된 minifier 설정은 코드 동작을 깨뜨릴 수 있음

---

### [FAQ]

Q. Minification과 Compression 차이는?

A.
Minification은 파일 내용을 줄이는 빌드 과정이고, Compression은 네트워크 전송 시 gzip / brotli로 압축하는 과정이다.

Q. 압축 후 크기만 보면 충분한가?

A.
아니다. 브라우저가 압축을 푼 뒤 parse / execute하는 비용도 고려해야 한다.

Q. Minification이 보안 기능인가?

A.
아니다. 코드를 읽기 어렵게 만들 뿐 secret 보호나 권한 검증을 대체하지 못한다.

---

# 13. CSS Bundling Rules

## 13.1 CSS Build Optimization

### [개념]

CSS Bundling은 CSS 파일, CSS Modules, CSS-in-JS, Tailwind CSS, global style, component style을 빌드 결과물로 묶고 최적화하는 과정이다.

---

### [핵심]

검토 대상:

- Global CSS
- CSS Modules
- CSS-in-JS
- Tailwind CSS
- Critical CSS
- Unused CSS
- CSS Code Splitting
- CSS Minification
- Style Order
- Atomic CSS
- Runtime CSS Cost
- Theme CSS
- Dark Mode CSS

---

### [실무]

작성 기준:

- 사용하지 않는 CSS 제거
- Tailwind는 content scan / purge 설정 확인
- global CSS 범위 최소화
- route별 CSS chunk 가능 여부 확인
- CSS-in-JS runtime cost 검토
- critical CSS와 non-critical CSS 구분 가능
- style import 순서로 인한 override 문제 확인
- design token 기반 CSS 변수 사용 가능
- theme / dark mode CSS 중복 확인
- CSS 크기뿐 아니라 runtime style injection 비용도 고려

주의:

- CSS가 작아 보여도 render blocking이 될 수 있음
- 사용하지 않는 utility가 purge되지 않으면 CSS가 커짐
- CSS-in-JS는 runtime과 SSR 설정에 따라 성능 차이
- global style 남용은 예측하기 어려운 cascade 문제
- 중복 theme style은 bundle 증가 원인

예시:

```text
Tailwind 사용 시 content 경로가 실제 컴포넌트 파일을 포함하는지 확인
동적 class name이 purge에서 누락되지 않는지 확인
사용하지 않는 UI library CSS가 포함되지 않는지 확인
```

---

### [FAQ]

Q. CSS도 번들 최적화 대상인가?

A.
그렇다. CSS는 render blocking, 초기 로딩, 스타일 계산, layout에 영향을 줄 수 있다.

Q. Tailwind CSS에서 purge가 중요한 이유는?

A.
사용하지 않는 utility class가 제거되지 않으면 CSS 번들이 불필요하게 커지기 때문이다.

Q. CSS-in-JS는 항상 나쁜가?

A.
아니다. 하지만 runtime style injection, SSR 설정, bundle size, hydration 비용을 함께 검토해야 한다.

---

# 14. Asset Optimization Rules

## 14.1 Asset / Image / SVG 최적화

### [개념]

Asset Optimization은 이미지, SVG, 아이콘, JSON, media file 같은 정적 자산을 빌드와 배포 단계에서 최적화하는 기준이다.

---

### [핵심]

검토 대상:

- Image Size
- Image Format
- Responsive Image
- Lazy Image
- SVG Optimization
- Icon Sprite
- Inline SVG
- Static Asset Hash
- Public Folder
- Import Asset
- JSON Asset
- Media Asset

---

### [실무]

작성 기준:

- 큰 이미지는 압축 / 리사이징
- WebP / AVIF 같은 현대 포맷 검토
- responsive image와 width / height 지정
- below-the-fold image lazy loading
- SVG는 SVGO 등으로 최적화 가능
- 아이콘은 필요한 것만 bundle에 포함
- 거대한 JSON을 initial bundle에 포함하지 않기
- public asset과 imported asset의 cache 차이 이해
- content hash로 long-term cache 활용
- 동영상 / 큰 media는 CDN과 streaming 전략 검토

주의:

- 이미지 파일 하나가 JS 최적화보다 더 큰 병목일 수 있음
- inline SVG 남용은 HTML / JS 크기 증가
- icon library 전체 import 주의
- width / height 누락은 CLS 원인
- public folder asset은 import 최적화 대상이 아닐 수 있음

---

### [FAQ]

Q. Asset Optimization도 Bundling에 포함되나?

A.
그렇다. 이미지, SVG, 아이콘, JSON, media file은 초기 로딩과 네트워크 비용에 큰 영향을 준다.

Q. SVG를 inline으로 넣으면 항상 좋은가?

A.
아니다. 작은 아이콘에는 유용할 수 있지만 큰 SVG나 반복 SVG는 HTML / JS 크기를 늘릴 수 있다.

Q. 큰 JSON을 import해도 되나?

A.
주의해야 한다. import하면 bundle에 포함될 수 있으므로 필요 시 동적 로딩이나 API 제공을 검토한다.

---

# 15. Font Optimization Rules

## 15.1 Font Build / Loading Optimization

### [개념]

Font Optimization은 웹폰트 파일 크기, 로딩 전략, preload, subset, fallback, layout shift를 관리해 텍스트 렌더링 성능과 UX를 개선하는 기준이다.

---

### [핵심]

검토 대상:

- Web Font
- Font Subset
- Font Weight
- Font Display
- Preload
- Fallback Font
- Variable Font
- Local Font
- FOIT
- FOUT
- CLS
- Next.js Font Optimization

---

### [실무]

작성 기준:

- 필요한 font weight만 포함
- 불필요한 font family 제거
- subset 사용 검토
- variable font 사용 시 실제 크기 확인
- `font-display` 정책 설정
- 중요한 font는 preload 검토
- fallback font metric 차이로 인한 CLS 확인
- 아이콘 폰트보다 SVG icon 검토
- Next.js font 최적화 기능 활용 가능
- 외부 font provider 사용 시 privacy / performance 고려

주의:

- 많은 font weight는 큰 네트워크 비용
- 웹폰트 로딩은 LCP와 CLS에 영향
- icon font는 접근성과 렌더링 문제가 있을 수 있음
- preload 남용은 중요한 리소스 경쟁 유발
- 외부 font 요청은 DNS / TLS 비용 발생

예시:

```text
사용하지 않는 100 / 200 / 300 / 800 / 900 weight 제거
한글 폰트는 파일 크기가 크므로 subset과 fallback 전략 검토
LCP 텍스트에 사용되는 font는 로딩 전략 확인
```

---

### [FAQ]

Q. Font Optimization은 왜 중요한가?

A.
웹폰트는 파일 크기가 크고 LCP, CLS, 텍스트 표시 지연에 영향을 줄 수 있기 때문이다.

Q. font weight는 많이 넣어도 되나?

A.
필요한 weight만 포함하는 것이 좋다. weight가 많을수록 다운로드 비용이 증가한다.

Q. font-display는 왜 필요한가?

A.
폰트 로딩 중 텍스트 표시 방식과 FOIT / FOUT를 제어하기 위해 필요하다.

---

# 16. Source Map Strategy Rules

## 16.1 Source Map 빌드 전략

### [개념]

Source Map은 minified production bundle에서 발생한 오류를 원본 TypeScript / React 코드 위치로 매핑하기 위한 파일이다.

Build Optimization에서는 debugging, observability, 보안, 배포 artifact 관점에서 Source Map 전략을 정해야 한다.

---

### [핵심]

검토 대상:

- Development Source Map
- Production Source Map
- Hidden Source Map
- Inline Source Map
- External Source Map
- Source Map Upload
- Release Version
- Error Tracking
- Public Exposure
- Build Artifact
- CI Upload

---

### [실무]

작성 기준:

- development와 production source map 정책 분리
- production debugging 필요 시 source map 생성
- public source map 노출 위험 검토
- observability 도구에 비공개 업로드 검토
- release version과 source map 연결
- CI에서 source map upload 자동화
- source map upload 실패 시 알림 가능
- source map에 secret이 들어가지 않도록 bundle 자체 점검
- source map 보관 기간 정의
- source map 크기가 배포 artifact에 미치는 영향 확인

주의:

- Source Map 공개는 코드 이해를 쉽게 만듦
- Source Map이 없으면 production error debugging 어려움
- release와 source map이 불일치하면 stack trace 매핑 실패
- inline source map은 production에 부적합한 경우 많음
- minification은 secret 보호 수단이 아님

---

### [FAQ]

Q. Production Source Map은 만들어야 하나?

A.
오류 추적과 디버깅에는 유용하다. 다만 공개 노출 위험이 있으므로 비공개 업로드나 접근 제한을 검토해야 한다.

Q. Source Map을 공개하면 위험한가?

A.
코드 구조와 원본 소스가 더 쉽게 노출될 수 있으므로 보안 정책을 검토해야 한다.

Q. Source Map과 release version은 왜 연결해야 하나?

A.
해당 release의 minified bundle과 source map이 일치해야 정확한 원본 위치를 찾을 수 있기 때문이다.

---

# 17. Next.js Build Optimization Rules

## 17.1 Next.js App Router Build 기준

### [개념]

Next.js Build Optimization은 App Router 환경에서 Server Component, Client Component, route segment, dynamic import, image, font, metadata, cache, bundle output을 최적화하는 기준이다.

---

### [핵심]

검토 대상:

- Server Component
- Client Component
- `use client`
- Client Bundle
- Server Bundle
- Route Segment
- Layout
- Page
- Dynamic Import
- Image Optimization
- Font Optimization
- Metadata
- Static Rendering
- Dynamic Rendering
- Build Output
- Bundle Analyzer
- Turbopack / Webpack
- Edge Runtime Bundle

---

### [실무]

작성 기준:

- 불필요한 `use client`를 줄임
- Client Component boundary를 작게 유지
- server-only code가 client bundle에 들어가지 않게 관리
- heavy client component는 dynamic import 검토
- route segment별 bundle 크기 확인
- 공통 layout에 heavy client dependency 넣지 않기
- `next/image` 최적화 활용 가능
- `next/font` 최적화 활용 가능
- 사용자별 데이터와 static rendering 혼동 방지
- middleware / edge runtime bundle에 큰 dependency 포함 주의
- Bundle Analyzer로 client / server bundle 분리 확인

예시:

```text
공통 layout에 chart library import 금지
chart가 필요한 dashboard route에서만 dynamic import
Server Component에서 data fetch 후 Client Component에는 필요한 최소 props 전달
```

주의:

- 상위 layout에 `use client`를 붙이면 하위 client bundle이 커질 수 있음
- Client Component가 import한 dependency는 browser bundle에 포함될 수 있음
- Server Component에서 Client Component로 넘기는 props는 클라이언트에 노출됨
- Edge runtime은 Node API와 큰 dependency 제약 확인 필요
- Next.js Cache와 bundle optimization을 혼동하지 않기

---

### [FAQ]

Q. Next.js에서 `use client`가 번들에 영향을 주나?

A.
그렇다. Client Component와 그 dependency는 브라우저 bundle에 포함될 수 있으므로 boundary를 신중히 설계해야 한다.

Q. 공통 layout에 무거운 dependency를 넣으면 왜 문제인가?

A.
여러 route에서 불필요하게 로드되어 initial 또는 shared chunk가 커질 수 있기 때문이다.

Q. Server Component를 쓰면 JS bundle이 줄어드나?

A.
상호작용이 필요 없는 UI를 Server Component로 유지하면 client bundle을 줄이는 데 도움이 될 수 있다.

---

# 18. Build Cache Rules

## 18.1 Build Cache / Incremental Build

### [개념]

Build Cache는 이전 빌드 결과를 재사용해 local build와 CI build 시간을 줄이는 전략이다.

Incremental Build는 변경된 부분만 다시 빌드하거나 테스트하는 방식이다.

---

### [핵심]

검토 대상:

- Local Build Cache
- CI Cache
- Package Manager Cache
- Turborepo Cache
- Nx Cache
- Next.js Cache
- TypeScript Incremental
- Dependency Cache
- Remote Cache
- Affected Build
- Cache Key
- Cache Invalidation

---

### [실무]

작성 기준:

- package manager cache 사용
- Next.js build cache 보존 검토
- TypeScript incremental build 활용 가능
- monorepo에서는 affected package만 build 검토
- remote cache 사용 시 cache key 정확성 확보
- CI cache hit / miss 관찰
- lockfile 변경 시 cache invalidation
- 환경변수 변경이 build output에 영향 주는지 확인
- cache가 오래되어 잘못된 빌드 산출물이 생기지 않게 관리
- cache 저장소에 secret 포함 금지

주의:

- 잘못된 cache는 깨진 build를 통과시킬 수 있음
- cache key가 너무 넓으면 stale cache 위험
- cache key가 너무 좁으면 hit rate 낮음
- 환경변수 / build target / lockfile이 cache key에 반영되어야 함
- remote cache는 보안과 접근 권한 검토 필요

---

### [FAQ]

Q. Build Cache는 왜 필요한가?

A.
로컬 개발과 CI에서 반복 빌드 시간을 줄이고 피드백 속도를 높이기 위해 필요하다.

Q. Cache가 있으면 항상 좋은가?

A.
아니다. cache key가 잘못되면 오래된 결과를 재사용해 문제를 만들 수 있다.

Q. Monorepo에서는 어떤 build 최적화가 중요한가?

A.
변경된 package만 build / test하는 affected build와 remote cache 전략이 중요하다.

---

# 19. Monorepo Build Rules

## 19.1 Monorepo Build Optimization

### [개념]

Monorepo Build Optimization은 여러 app과 package가 한 repository에 있을 때 build dependency graph, affected task, shared package, remote cache를 활용해 빌드 효율을 높이는 전략이다.

---

### [핵심]

검토 대상:

- Workspace
- Package Boundary
- Dependency Graph
- Affected Build
- Task Pipeline
- Remote Cache
- Shared Config
- Shared UI Package
- Build Order
- Incremental Build
- Circular Dependency
- Version Mismatch

---

### [실무]

작성 기준:

- package dependency graph 명확화
- app과 shared package 경계 분리
- shared package 변경 시 영향받는 app 확인
- affected build / test 적용 가능
- remote cache 사용 시 team / CI 설정 검토
- shared UI package가 모든 app bundle을 키우지 않게 import 경로 관리
- barrel export가 tree shaking에 미치는 영향 확인
- circular dependency 방지
- TypeScript project references 검토
- package별 build output과 entry point 명확화

주의:

- shared package에 너무 많은 dependency를 넣으면 모든 app에 영향
- barrel file로 전체 UI library가 bundle에 포함될 수 있음
- package boundary가 약하면 affected build가 부정확
- remote cache에 secret이나 private artifact 포함 금지
- build 순서가 dependency graph와 맞아야 함

---

### [FAQ]

Q. Monorepo에서 Build Optimization은 왜 중요한가?

A.
app과 package가 많아질수록 전체 build 시간이 늘어나므로 변경 영향 범위만 build하는 전략이 필요하다.

Q. Shared UI Package가 bundle을 키울 수 있나?

A.
그렇다. import 구조와 barrel export가 잘못되면 사용하지 않는 컴포넌트까지 포함될 수 있다.

Q. Affected Build는 무엇인가?

A.
변경된 파일이 영향을 주는 app과 package만 build / test하는 전략이다.

---

# 20. Build Environment Rules

## 20.1 Development / Production Build 구분

### [개념]

Development Build는 빠른 피드백과 디버깅을 위한 빌드이고, Production Build는 최적화와 배포를 위한 빌드이다.

두 환경은 source map, minification, HMR, debug code, tree shaking, compression 정책이 다르다.

---

### [핵심]

Development Build 특징:

- 빠른 rebuild
- HMR
- 상세 오류
- source map
- 최적화 제한
- debug log 허용 가능

Production Build 특징:

- minification
- tree shaking
- code splitting
- compression
- content hash
- optimized asset
- error tracking source map
- debug code 제거

---

### [실무]

작성 기준:

- 개발 build 결과로 production 성능 판단 금지
- production build를 기준으로 bundle 분석
- debug log / dev-only code가 production에 남지 않게 관리
- 환경변수별 build output 차이 확인
- production source map 정책 별도 설정
- local production build 재현 가능해야 함
- CI build와 local build 차이 최소화
- build mode에 따라 feature flag가 달라지는지 확인
- env별 API endpoint와 secret 노출 점검

주의:

- development build는 tree shaking / minification이 다를 수 있음
- production-only 오류가 발생할 수 있음
- env 변수 누락이 build-time에 고정될 수 있음
- `NEXT_PUBLIC_` 값은 client bundle에 들어갈 수 있음
- production build 테스트 없이 배포 금지

---

### [FAQ]

Q. Development Build로 번들 크기를 판단해도 되나?

A.
안 된다. production build는 minification, tree shaking, code splitting이 다르게 적용된다.

Q. Production Build에서만 오류가 나는 이유는?

A.
minification, env 차이, tree shaking, SSR / hydration 차이, build-time 값 고정 때문일 수 있다.

Q. Debug code는 어떻게 관리해야 하나?

A.
dev-only 조건으로 분리하고 production build에 포함되지 않는지 확인해야 한다.

---

# 21. Bundle Budget Rules

## 21.1 Bundle Budget / Regression 방지

### [개념]

Bundle Budget은 initial JS, route chunk, CSS, asset 크기에 허용 기준을 설정해 성능 회귀를 방지하는 전략이다.

---

### [핵심]

Budget 대상:

- Initial JavaScript
- Route JavaScript
- Shared Chunk
- CSS Bundle
- Image Asset
- Font Asset
- Total Blocking Script
- Third-party Script
- Dependency Size
- Build Time

Budget Flow:

```text
Baseline 측정
→ Budget 설정
→ PR에서 bundle diff 확인
→ 기준 초과 시 리뷰
→ 예외 승인 또는 개선
```

---

### [실무]

작성 기준:

- 프로젝트 기준 baseline 측정
- critical route와 non-critical route budget 분리
- 새 dependency 추가 시 bundle diff 확인
- PR comment로 bundle change 표시 가능
- budget 초과 시 원인과 필요성 기록
- 무조건 실패보다 warning / review 정책 가능
- gzip / brotli 크기와 raw size를 함께 고려
- third-party script budget 포함
- performance regression test와 연결
- budget은 프로젝트 성장에 따라 조정 가능

주의:

- 너무 엄격한 budget은 개발을 방해할 수 있음
- 너무 느슨한 budget은 회귀를 못 잡음
- route별 중요도를 반영해야 함
- 일시적 증가가 필요한 경우 이유 기록
- budget 숫자보다 사용자 영향이 중요

---

### [FAQ]

Q. Bundle Budget은 왜 필요한가?

A.
기능이 추가되면서 번들이 계속 커지는 것을 조기에 감지하고 성능 회귀를 막기 위해 필요하다.

Q. Budget을 넘으면 무조건 실패 처리해야 하나?

A.
프로젝트 정책에 따라 warning, PR review, 실패 처리 중 선택할 수 있다.

Q. 어떤 route에 더 엄격한 budget을 둬야 하나?

A.
홈, 로그인, 검색, 결제처럼 사용자가 자주 방문하거나 성능이 중요한 route에 더 엄격한 기준을 둘 수 있다.

---

# 22. Third-party Script Bundling Rules

## 22.1 Third-party Script 로딩 최적화

### [개념]

Third-party Script Bundling은 analytics, ads, map, payment, chat widget, A/B testing SDK 같은 외부 스크립트가 초기 로딩과 보안에 미치는 영향을 관리하는 기준이다.

---

### [핵심]

검토 대상:

- Analytics Script
- Ads Script
- Tag Manager
- Map SDK
- Payment SDK
- Chat Widget
- A/B Testing SDK
- Consent Script
- Script Loading Strategy
- Lazy Script
- Defer / Async
- Main Thread Blocking
- Third-party Budget

---

### [실무]

작성 기준:

- 외부 script는 꼭 필요한 것만 로드
- critical path에 필요 없는 script는 지연 로드
- consent가 필요한 script는 동의 후 로드
- map / chat / payment SDK는 해당 route나 action에서 로드
- Tag Manager로 추가되는 script도 budget에 포함
- third-party script가 main thread를 막는지 확인
- 외부 script 실패 시 fallback 처리
- CSP allowlist와 함께 관리
- 개인정보 전달 최소화
- Performance / Security 리뷰 대상에 포함

주의:

- Third-party script는 앱 코드보다 통제하기 어려움
- Tag Manager는 우회적인 번들 증가 / 보안 위험이 될 수 있음
- analytics script가 초기 렌더링을 방해할 수 있음
- payment script는 필요한 시점보다 너무 늦게 로드하면 UX 지연
- 외부 script가 LCP / INP에 영향 가능

---

### [FAQ]

Q. Third-party Script도 build optimization 대상인가?

A.
그렇다. 외부 script는 초기 로딩, main thread, 보안, 개인정보에 큰 영향을 줄 수 있다.

Q. Analytics script는 언제 로드하면 좋나?

A.
서비스 요구에 따라 다르지만 critical rendering을 방해하지 않도록 지연 로드나 전략적 로딩을 검토한다.

Q. Payment SDK는 lazy loading해도 되나?

A.
가능하지만 결제 버튼 클릭 후 지연이 커지지 않도록 prefetch나 결제 페이지 진입 시 로딩을 검토한다.

---

# 23. Worker and Off-main-thread Rules

## 23.1 Worker / Off-main-thread 최적화

### [개념]

Worker Optimization은 무거운 계산, 검색, 파싱, 변환 작업을 main thread가 아닌 Web Worker 등으로 옮겨 UI 응답성을 개선하는 전략이다.

---

### [핵심]

적합 대상:

- Large Data Parsing
- Search Index
- Markdown Parsing
- Image Processing
- CSV Processing
- PDF Processing
- Syntax Highlighting
- Compression
- Background Computation

Build 고려 요소:

- Worker Bundle
- Worker Chunk
- Worker Loader
- Transferable Object
- WASM Asset
- Code Splitting
- Browser Support

---

### [실무]

작성 기준:

- main thread를 막는 작업인지 먼저 측정
- worker bundle 크기 확인
- worker를 initial bundle에 불필요하게 포함하지 않기
- 필요한 시점에 worker lazy load 가능
- 큰 데이터는 transferable object 검토
- worker와 main thread 메시지 protocol 정의
- worker error 처리
- worker 종료 / cleanup
- SSR 환경에서 worker import 주의
- browser support와 fallback 검토

주의:

- Worker는 네트워크와 초기화 비용이 있음
- 작은 작업까지 worker로 옮기면 오히려 overhead
- worker bundle도 최적화 대상
- worker 내부 dependency가 중복 포함될 수 있음
- DOM 접근은 worker에서 불가능

---

### [FAQ]

Q. Web Worker는 언제 쓰면 좋나?

A.
큰 데이터 파싱, 검색 인덱싱, 이미지 처리처럼 main thread를 오래 막는 작업에 적합하다.

Q. Worker를 쓰면 항상 빨라지나?

A.
아니다. worker 초기화와 메시지 전달 비용이 있어 작은 작업에는 오히려 비효율적일 수 있다.

Q. Worker bundle도 분석해야 하나?

A.
그렇다. worker 내부 dependency도 별도 chunk로 포함되어 번들 크기에 영향을 준다.

---

# 24. Build Security Rules

## 24.1 Build / Bundle 보안 기준

### [개념]

Build Security는 빌드 산출물에 secret, server-only code, 민감한 debug 정보, 의존성 취약점, 공개 source map이 포함되지 않도록 관리하는 기준이다.

---

### [핵심]

검토 대상:

- Secret in Bundle
- `NEXT_PUBLIC_`
- Environment Variable
- Source Map Exposure
- Dependency Vulnerability
- Supply Chain Risk
- Debug Code
- Console Log
- API Endpoint Exposure
- License Exposure
- Server-only Code in Client Bundle
- Build Artifact Access

---

### [실무]

작성 기준:

- frontend bundle에 secret 포함 금지
- `NEXT_PUBLIC_` 값은 공개 값으로 취급
- server-only module이 client bundle에 포함되지 않게 관리
- source map 공개 정책 검토
- dependency audit 수행
- lockfile 변경 리뷰
- build artifact 접근 권한 관리
- debug page / test page production 포함 여부 확인
- console log / dev tool code 제거 정책
- sourcemap upload 시 권한과 retention 관리
- CI log에 env / secret 노출 금지

주의:

- Minification은 secret 보호가 아님
- 브라우저로 내려간 코드는 사용자가 볼 수 있음
- public API key는 권한 / origin 제한 필요
- source map은 원본 코드 이해를 쉽게 만듦
- build cache나 artifact에 secret이 들어갈 수 있음

---

### [FAQ]

Q. Build 결과물에 secret이 들어가면 어떻게 되나?

A.
브라우저 사용자에게 노출될 수 있으므로 즉시 제거하고 secret rotate와 노출 범위 확인이 필요하다.

Q. `NEXT_PUBLIC_`에 secret을 넣어도 되나?

A.
안 된다. `NEXT_PUBLIC_` 환경변수는 client bundle에 포함될 수 있으므로 공개 값으로 취급해야 한다.

Q. Minification하면 secret이 안전해지나?

A.
아니다. minification은 읽기 어렵게 할 뿐 secret 보호 수단이 아니다.

---

# 25. Testing and Verification Rules

## 25.1 Build Optimization 검증 기준

### [개념]

Build Optimization은 적용 후 실제 빌드 결과와 사용자 성능이 개선되었는지 검증해야 한다.

---

### [핵심]

검증 대상:

- Production Build
- Bundle Analyzer
- Bundle Diff
- Lighthouse
- WebPageTest
- Core Web Vitals
- Network Waterfall
- Coverage Tab
- Source Map Mapping
- Chunk Load
- E2E Smoke Test
- Visual Regression
- Build Time
- CI Cache Hit Rate

---

### [실무]

검증 기준:

- production build로 측정
- initial JS 감소 확인
- route chunk 크기 확인
- 중복 dependency 제거 확인
- dynamic import chunk 정상 로드 확인
- loading fallback 정상 표시 확인
- source map stack trace 매핑 확인
- gzip / brotli 전송 확인
- Lighthouse / synthetic test로 회귀 확인
- production RUM과 연결 가능
- CI build 시간 변화 확인
- E2E smoke test로 lazy route 검증

주의:

- 개발 서버 기준으로 성능 판단 금지
- bundle 크기 감소가 UX 개선으로 이어졌는지 확인
- lazy loading 후 사용 시점 지연이 커지지 않았는지 확인
- source map / chunk path가 배포 환경에서 맞는지 확인
- cache 때문에 이전 chunk를 참조하는 문제 확인

---

### [FAQ]

Q. Build Optimization 후 무엇을 검증해야 하나?

A.
production build, bundle analyzer, route chunk, gzip / brotli 크기, loading UX, source map, E2E smoke test, 성능 지표를 확인해야 한다.

Q. 번들 크기가 줄었으면 성공인가?

A.
중요한 개선이지만 loading UX, runtime 성능, chunk error, 사용자 체감 성능도 함께 확인해야 한다.

Q. Dynamic Import 후 어떤 테스트가 필요한가?

A.
해당 component가 필요한 시점에 정상 로드되는지, fallback이 보이는지, chunk load 실패 대응이 있는지 확인해야 한다.

---

# 26. Troubleshooting Rules

## 26.1 자주 발생하는 Build / Bundling 문제

### [개념]

Troubleshooting 문서는 Agent가 Frontend Build Optimization 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Initial Bundle이 너무 큼
- 특정 route chunk가 너무 큼
- Shared Chunk가 너무 큼
- Tree Shaking이 안 됨
- 큰 dependency가 bundle에 포함됨
- icon library 전체가 포함됨
- locale 데이터가 과도하게 포함됨
- CSS가 purge되지 않음
- dynamic import 했는데 bundle이 줄지 않음
- chunk가 너무 많이 생김
- chunk load error 발생
- production build에서만 오류 발생
- source map이 매핑되지 않음
- build 시간이 너무 김
- CI cache가 hit되지 않음
- server-only code가 client bundle에 포함됨
- secret이 bundle에 포함됨
- public asset cache가 안 됨
- Edge bundle이 너무 큼

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

- Initial Bundle이 너무 큼

원인:

- 공통 layout에서 heavy dependency import
- route별 code splitting 부족
- icon / chart / editor library가 초기 bundle에 포함
- tree shaking 실패

해결:

- Bundle Analyzer로 큰 module 확인
- route / component 단위 dynamic import 적용
- import 방식 최적화
- shared chunk 크기 확인
- dependency 대체안 검토
```

예시:

```md
문제:

- Tree Shaking이 되지 않음

원인:

- CommonJS package 사용
- side effect module 포함
- barrel export로 전체 module import
- root import가 전체 library를 포함

해결:

- ESM 지원 package 사용
- 개별 경로 import 검토
- sideEffects 설정 확인
- bundle analyzer로 제거 여부 확인
```

예시:

```md
문제:

- Dynamic Import를 했는데 초기 번들이 줄지 않음

원인:

- 같은 dependency가 상위 module에서 이미 import됨
- shared chunk로 분리되어 initial에 포함
- dynamic import 대상이 initial render에서 즉시 필요
- bundler split 조건이 맞지 않음

해결:

- 상위 import 제거
- chunk analyzer 확인
- lazy boundary 위치 조정
- 실제 route별 chunk 변화 확인
```

---

### [FAQ]

Q. Initial Bundle이 너무 크면 무엇을 확인해야 하나?

A.
Bundle Analyzer로 큰 dependency, 공통 layout import, shared chunk, route splitting, tree shaking 실패를 확인해야 한다.

Q. Dynamic Import를 했는데 번들이 줄지 않으면 왜 그런가?

A.
상위에서 이미 import했거나 shared chunk에 포함되었거나 dynamic boundary 위치가 잘못되었을 수 있다.

Q. Production Build에서만 오류가 나면 무엇을 봐야 하나?

A.
minification, tree shaking, env 변수, source map, SSR / hydration 차이, browser target을 확인해야 한다.

---

# 27. Code Example Rules

## 27.1 코드 예제 작성 기준

### [개념]

Frontend Build Optimization / Bundling 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript / React / Next.js 우선
- Dynamic Import 예제 포함 가능
- Query보다 build 구조 중심
- 긴 config 전체 파일 금지
- Secret 하드코딩 금지
- 실제 API key 포함 금지
- 번들 분석 기준 함께 설명
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Dynamic Import
- Lazy Component
- Route-based Splitting
- Heavy Library Lazy Loading
- Named Import
- Query Key가 아니라 Import Boundary 중심 예제
- Bundle Analyzer 명령 예시
- Source Map Upload Flow
- Build Budget Config 예시
- Worker Lazy Loading
- Font Optimization
- Image Import 기준
- Monorepo affected build 예시

금지 예제:

- 모든 component lazy loading 권장
- root에서 heavy dependency import
- `NEXT_PUBLIC_` secret 사용
- token / secret console log
- source map public 공개를 기본 권장
- CJS root import를 최적화 예제로 제시
- production build 없이 dev build 분석
- dynamic import fallback 없는 예제
- huge config 전체 복붙

---

### [FAQ]

Q. Build Optimization 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. 설정 파일 전체를 예제로 넣어도 되나?

A.
권장하지 않는다. 중요한 옵션과 판단 기준만 짧게 보여주는 것이 좋다.

---

# 28. Comparison Rules

## 28.1 필수 비교 대상

### [개념]

Frontend Build Optimization / Bundling 문서는 Agent의 빌드 최적화 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Development Build vs Production Build
- Initial Bundle vs Route Chunk
- Static Import vs Dynamic Import
- Code Splitting vs Lazy Loading
- Tree Shaking vs Minification
- Minification vs Compression
- Gzip vs Brotli
- ESM vs CommonJS
- Vendor Chunk vs Shared Chunk
- Route-based Splitting vs Component-based Splitting
- Server Component vs Client Component Bundle
- Public Asset vs Imported Asset
- Inline SVG vs External SVG
- Icon Font vs SVG Icon
- Local Font vs External Font
- Source Map Public vs Private Upload
- Bundle Size vs Runtime Cost
- Build Cache vs Clean Build
- Full Build vs Affected Build
- Webpack vs Vite vs Turbopack 개념 비교
- Bundle Budget Warning vs Failure

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 장점 / 위험 / 적합 상황 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Tree Shaking과 Minification 차이는?

A.
Tree Shaking은 사용하지 않는 코드를 제거하는 것이고, Minification은 남은 코드의 크기를 줄이는 것이다.

Q. Initial Bundle과 Route Chunk 차이는?

A.
Initial Bundle은 첫 화면 로딩에 필요한 코드이고, Route Chunk는 특정 route에 진입할 때 필요한 코드이다.

Q. Dynamic Import와 Lazy Loading은 같은가?

A.
Dynamic Import는 코드를 비동기로 가져오는 문법 / 방식이고, Lazy Loading은 필요한 시점까지 로딩을 미루는 전략이다.

---

# 29. Checklist Rules

## 29.1 문서 품질 체크리스트

### [개념]

Frontend Build Optimization / Bundling RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Build Optimization 목적이 명확한가?
- [ ] Bundling 기본 개념을 포함했는가?
- [ ] Bundle Analysis 기준을 포함했는가?
- [ ] Code Splitting 기준을 포함했는가?
- [ ] Dynamic Import 기준을 포함했는가?
- [ ] Tree Shaking 기준을 포함했는가?
- [ ] Dependency Optimization 기준을 포함했는가?
- [ ] Chunk Strategy 기준을 포함했는가?
- [ ] Transpilation / Polyfill 기준을 포함했는가?
- [ ] Minification / Compression 기준을 포함했는가?
- [ ] CSS Bundling 기준을 포함했는가?
- [ ] Asset Optimization 기준을 포함했는가?
- [ ] Font Optimization 기준을 포함했는가?
- [ ] Source Map Strategy 기준을 포함했는가?
- [ ] Next.js App Router Build 기준을 포함했는가?
- [ ] Build Cache 기준을 포함했는가?
- [ ] Monorepo Build 기준을 포함했는가?
- [ ] Development / Production Build 구분을 포함했는가?
- [ ] Bundle Budget 기준을 포함했는가?
- [ ] Third-party Script 기준을 포함했는가?
- [ ] Worker / Off-main-thread 기준을 포함했는가?
- [ ] Build Security 기준을 포함했는가?
- [ ] Testing / Verification 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] Secret / API key 예제가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Performance / Security / Next.js / Monorepo 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- 빌드 도구 사용법보다 최적화 판단 기준 중심으로 작성
- Frontend Performance / Security / Next.js / Monorepo 문서와 연계 가능해야 함

---

### [FAQ]

Q. Build Optimization 문서 품질에서 가장 중요한 것은?

A.
Bundle 분석, Code Splitting, Tree Shaking, Dependency 최적화, Chunk 전략, Source Map, Build Cache, Budget 기준이 명확해야 한다.

---

# 30. Retrieval Optimization Rules

## 30.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Build Optimization
- Frontend Bundling
- Bundle Size
- Bundle Analyzer
- Initial Bundle
- Route Chunk
- Shared Chunk
- Vendor Chunk
- Code Splitting
- Dynamic Import
- Lazy Loading
- Tree Shaking
- Dead Code Elimination
- Side Effects
- ESM
- CommonJS
- Dependency Optimization
- Chunk Strategy
- Minification
- Compression
- Gzip
- Brotli
- Transpilation Target
- Polyfill
- CSS Bundling
- Tailwind Purge
- CSS Code Splitting
- Asset Optimization
- Image Optimization
- SVG Optimization
- Font Optimization
- Source Map
- Production Build
- Build Cache
- Incremental Build
- Monorepo Build
- Affected Build
- Bundle Budget
- Bundle Regression
- Third-party Script
- Worker Bundle
- Next.js Build Optimization
- Client Bundle
- Server Component
- `use client`

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Frontend Build Optimization은 뭐야?
- Bundling은 뭐야?
- Initial Bundle이 너무 커
- Bundle Analyzer는 왜 필요해?
- Code Splitting은 언제 해?
- Dynamic Import는 언제 써?
- dynamic import 했는데 bundle이 안 줄어
- Tree Shaking이 안 돼
- ESM과 CommonJS 차이
- dependency가 bundle을 너무 키워
- icon library 전체가 포함돼
- vendor chunk가 너무 커
- shared chunk가 너무 커
- chunk를 많이 나누면 좋아?
- Minification과 Compression 차이
- gzip과 brotli 차이
- CSS bundle이 너무 커
- Tailwind purge가 안 돼
- 이미지도 build optimization 대상이야?
- font가 LCP를 느리게 해
- Source Map 공개해도 돼?
- Next.js use client가 bundle에 영향 줘?
- Server Component 쓰면 bundle 줄어?
- Build Cache는 왜 필요해?
- Bundle Budget은 어떻게 잡아?
- Production Build에서만 오류가 나
- Frontend Build Optimization 코드 리뷰 기준

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 31. Version Rules

## 31.1 기준 버전

### [개념]

Frontend Build Optimization / Bundling 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern JavaScript
- TypeScript
- React 19+
- Next.js App Router
- Server Component
- Client Component
- Dynamic Import
- ESM
- Modern Bundler
- Webpack
- Vite
- Rollup
- ESBuild
- SWC
- Turbopack
- Bundle Analyzer
- Build Cache
- Source Map Upload
- Bundle Budget
- CI Build Optimization

Legacy 제외:

- 모든 코드를 하나의 거대한 bundle로 묶는 방식
- CommonJS 중심 최적화 설명
- Dynamic Import 없이 모든 heavy library 초기 로드
- Source Map 없는 production debugging
- dev build 기준 bundle 분석
- secret을 client bundle에 포함하는 구조
- 사용하지 않는 polyfill 과다 포함
- 모든 vendor를 무조건 하나로 묶는 설명
- snapshot처럼 build output을 검증 없이 업데이트하는 방식
- bundle size 숫자만 보고 UX를 무시하는 방식

---

### [실무]

문서 작성 시 주의:

- Bundler와 framework는 버전별 동작 차이가 큼
- 특정 도구 API보다 bundle 최적화 원칙과 판단 기준 우선
- Next.js App Router의 Server / Client Component 경계 고려
- Performance 문서의 Core Web Vitals / Request Waterfall 기준과 연계
- Security 문서의 Source Map / Secret / Dependency 기준과 연계
- Monorepo 문서의 affected build / remote cache 기준과 연계
- Testing 문서의 build verification / regression test 기준과 연계

---

### [FAQ]

Q. Build Optimization 문서는 특정 bundler 기준이어야 하나?

A.
아니다. Webpack, Vite, Turbopack, Rollup 등을 다룰 수 있지만 핵심은 번들 분석과 최적화 판단 기준이다.

Q. Next.js App Router 기준을 고려해야 하나?

A.
그렇다. Server Component와 Client Component 경계, `use client`, route segment, dynamic import가 bundle에 큰 영향을 준다.

---

# 32. Common Mistakes

## 32.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Build Optimization 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- Bundle Analyzer 없이 추측으로 최적화
- development build 기준으로 bundle 판단
- 모든 코드를 initial bundle에 포함
- 공통 layout에 heavy dependency import
- chart / editor / map SDK를 초기 로드
- dynamic import 후 fallback 없음
- 너무 작은 component까지 lazy loading
- Query Key가 아니라 import boundary 문제인데 cache 문제로 오해
- Tree Shaking 안 되는 CJS package 사용
- barrel export로 전체 module 포함
- icon library 전체 import
- 사용하지 않는 locale 데이터 포함
- dependency 중복 방치
- Tailwind content 경로 누락
- 사용하지 않는 CSS 포함
- font weight 과다 포함
- 큰 JSON을 정적 import
- Source Map 공개 정책 없음
- production source map upload 누락
- `NEXT_PUBLIC_`에 secret 포함
- server-only code가 client bundle에 포함
- CI build cache key 오류
- Bundle Budget 없음
- bundle size만 줄이고 loading UX 검증 누락

---

### [실무]

리뷰 기준:

- production build 기준 분석 여부 확인
- initial bundle / route chunk 확인
- 큰 dependency와 import 위치 확인
- dynamic import 후보 확인
- tree shaking 실패 여부 확인
- ESM / CJS dependency 확인
- chunk splitting 적절성 확인
- CSS / image / font 크기 확인
- source map 정책 확인
- secret bundle 포함 여부 확인
- Next.js `use client` boundary 확인
- Build Cache와 CI build 시간 확인
- Bundle Budget / regression check 확인
- lazy loading UX / error handling 확인

---

### [FAQ]

Q. Frontend Build Optimization에서 가장 흔한 실수는?

A.
Bundle Analyzer 없이 추측으로 최적화하거나, development build를 기준으로 production bundle을 판단하는 것이다.

Q. Next.js에서 흔한 bundle 실수는?

A.
상위 layout에 `use client`나 heavy dependency를 넣어 많은 route의 client bundle을 키우는 것이다.

Q. Dynamic Import 관련 흔한 실수는?

A.
fallback 없이 lazy loading하거나, 상위 module에서 이미 같은 dependency를 import해 initial bundle이 줄지 않는 것이다.

---

# 33. Final Goal

## 33.1 최종 목표

### [개념]

Frontend Build Optimization / Bundling RAG 문서는 Agent가 프론트엔드 프로젝트에서 빌드 산출물과 번들 구조를 분석, 설계, 검토, 개선할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Bundle Analyzer 결과 해석
- Initial Bundle / Route Chunk 분석
- Code Splitting 후보 제안
- Dynamic Import 적용 기준 제안
- Tree Shaking 실패 진단
- Dependency 크기와 중복 분석
- Chunk Strategy 리뷰
- Transpilation / Polyfill 기준 검토
- Minification / Compression 차이 설명
- CSS Bundling 최적화 제안
- Asset / Image / SVG 최적화 제안
- Font Optimization 제안
- Source Map 전략 제안
- Next.js App Router Build 리뷰
- `use client` boundary 리뷰
- Build Cache / CI build 최적화 제안
- Monorepo affected build 제안
- Bundle Budget 기준 제안
- Third-party Script 로딩 전략 제안
- Worker bundle 기준 제안
- Build Security 검토
- Build Optimization 테스트 / 검증 기준 제안
- Build / Bundling Troubleshooting
- Frontend Build Optimization 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Bundle Analysis / Code Splitting / Tree Shaking / Dependency / Chunk / Source Map 기준 명확화
- Next.js / Performance / Security / Monorepo / Testing 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Build Optimization / Bundling Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 bundle size, chunk strategy, code splitting, tree shaking, dependency, source map, build cache, bundle budget을 분석하고 최적화하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Build Optimization / Bundling 문서는 어떤 기준으로 작성해야 해?

A.
Bundle Analysis, Code Splitting, Dynamic Import, Tree Shaking, Dependency Optimization, Chunk Strategy, Source Map, Build Cache, Bundle Budget 중심으로 작성해야 한다.

Q. Frontend Build Optimization은 뭐야?

A.
프론트엔드 빌드 산출물을 더 작고 빠르고 안정적으로 만들어 초기 로딩, route 이동, 배포, CI 효율을 개선하는 작업이다.

Q. Bundling은 뭐야?

A.
JavaScript, CSS, asset, dependency를 브라우저가 효율적으로 로드할 수 있는 chunk로 묶고 분리하는 과정이다.

Q. Build Optimization과 Performance Tuning은 같은 거야?

A.
겹치지만 다르다. Build Optimization은 빌드 산출물과 로딩 구조에 집중하고 Performance Tuning은 런타임 렌더링과 사용자 체감 성능까지 포함한다.

Q. Bundle Analyzer는 왜 필요해?

A.
어떤 코드와 dependency가 번들을 크게 만드는지 실제 production build 기준으로 확인하기 위해 필요하다.

Q. Initial Bundle이 너무 커. 무엇을 봐?

A.
큰 dependency, 공통 layout import, shared chunk, route splitting 부족, tree shaking 실패, icon / chart / editor library 포함 여부를 확인한다.

Q. gzip 크기만 보면 충분해?

A.
아니다. 전송 크기는 gzip / brotli가 중요하지만 parse / execute 비용은 원본 JavaScript 크기와 복잡도에도 영향을 받는다.

Q. Code Splitting은 언제 해?

A.
첫 화면에 필요 없는 무거운 기능, 특정 route에서만 쓰는 코드, 사용 빈도가 낮은 component, 큰 외부 library에 적용한다.

Q. 모든 component를 lazy loading하면 좋아?

A.
아니다. 너무 작은 component까지 분리하면 요청 수와 loading 상태가 늘어 UX가 나빠질 수 있다.

Q. Dynamic Import는 언제 써?

A.
초기 화면에 필요 없는 무거운 component나 browser-only library를 필요한 시점에 로드할 때 사용한다.

Q. Dynamic Import를 쓰면 전체 번들 크기가 줄어?

A.
전체 코드량은 같을 수 있지만 initial bundle에서 분리되어 초기 로딩 부담이 줄어든다.

Q. dynamic import 했는데 bundle이 안 줄어. 왜?

A.
상위에서 이미 import했거나 shared chunk에 포함되었거나 dynamic boundary 위치가 잘못되었을 수 있다.

Q. Dynamic Import의 단점은?

A.
추가 네트워크 요청과 loading 지연이 생기며 fallback UI와 실패 처리가 필요하다.

Q. Tree Shaking이 뭐야?

A.
사용하지 않는 export와 dead code를 빌드 결과에서 제거하는 최적화이다.

Q. Tree Shaking이 안 돼. 왜?

A.
CommonJS, side effect, dynamic require, 잘못된 import 방식, barrel export, package 설정 문제 때문일 수 있다.

Q. ESM과 CommonJS 차이가 bundle에 영향 줘?

A.
그렇다. ESM은 정적 분석이 쉬워 tree shaking에 유리하고, CommonJS는 사용하지 않는 코드 제거가 어려울 수 있다.

Q. Named import를 쓰면 항상 tree shaking돼?

A.
항상 그렇지는 않다. 라이브러리의 module 형식, side effect 설정, bundler 동작에 따라 달라진다.

Q. barrel export가 bundle을 키울 수 있어?

A.
그렇다. barrel file이 전체 module을 import하게 만들면 사용하지 않는 코드까지 포함될 수 있다.

Q. dependency가 bundle을 너무 키워. 어떻게 해?

A.
사용 기능 대비 크기, import 방식, ESM 지원, 대체 라이브러리, lazy loading 가능성, 중복 dependency를 확인한다.

Q. 작은 기능 하나 때문에 큰 라이브러리 써도 돼?

A.
주의해야 한다. native API나 작은 대체 라이브러리, 직접 구현이 더 나을 수 있다.

Q. icon library 전체가 포함돼. 어떻게 해?

A.
개별 icon import, tree shaking 지원, barrel export 여부, icon package의 ESM 지원을 확인한다.

Q. locale 데이터가 과도하게 포함돼. 왜?

A.
date library나 i18n library에서 사용하지 않는 locale까지 bundle에 포함되었을 수 있다.

Q. Vendor Chunk는 뭐야?

A.
외부 dependency를 앱 코드와 분리한 chunk이다. cache 효율을 높일 수 있지만 너무 커지면 초기 로딩 부담이 된다.

Q. Shared Chunk가 너무 커. 왜 문제야?

A.
여러 route에서 불필요한 코드까지 함께 로드되어 초기 비용이 증가할 수 있다.

Q. chunk를 많이 나누면 좋아?

A.
항상 그렇지 않다. 초기 로딩은 줄 수 있지만 요청 수와 loading 상태가 늘어날 수 있다.

Q. Chunk Load Error는 왜 생겨?

A.
배포 중 HTML과 chunk 파일 버전이 어긋나거나 CDN cache, 네트워크 오류, 오래된 client가 새 chunk를 찾지 못할 때 발생할 수 있다.

Q. Transpilation Target은 왜 중요해?

A.
지원 브라우저 범위에 따라 변환 코드와 polyfill이 달라져 bundle 크기와 호환성에 영향을 주기 때문이다.

Q. 오래된 브라우저 지원하면 bundle이 커져?

A.
그럴 수 있다. 더 많은 transpilation과 polyfill이 필요하기 때문이다.

Q. Polyfill은 많이 넣으면 안전해?

A.
아니다. bundle 크기 증가와 side effect, 중복 포함 문제가 생길 수 있으므로 필요한 것만 포함해야 한다.

Q. Minification과 Compression 차이는?

A.
Minification은 파일 내용을 줄이는 빌드 과정이고, Compression은 네트워크 전송 시 gzip / brotli로 압축하는 과정이다.

Q. gzip과 brotli 차이는?

A.
둘 다 전송 압축 방식이다. Brotli는 정적 asset에서 더 작은 결과를 줄 수 있지만 서버 / CDN 지원 설정을 확인해야 한다.

Q. 압축 후 크기만 보면 돼?

A.
아니다. 압축을 푼 뒤 브라우저가 parse / execute하는 비용도 고려해야 한다.

Q. Minification은 보안 기능이야?

A.
아니다. 코드를 읽기 어렵게 만들 뿐 secret 보호나 권한 검증을 대체하지 못한다.

Q. CSS bundle이 너무 커. 무엇을 봐?

A.
사용하지 않는 CSS, Tailwind purge 설정, global CSS, UI library CSS, CSS-in-JS runtime cost, route별 CSS splitting을 확인한다.

Q. Tailwind purge가 안 돼. 왜?

A.
content 경로가 실제 컴포넌트 파일을 포함하지 않거나 동적 class name이 scan에서 누락되었을 수 있다.

Q. CSS-in-JS는 항상 나빠?

A.
아니다. 하지만 runtime style injection, SSR 설정, bundle size, hydration 비용을 함께 검토해야 한다.

Q. 이미지도 build optimization 대상이야?

A.
그렇다. 이미지, SVG, 아이콘, JSON, media file은 초기 로딩과 네트워크 비용에 큰 영향을 준다.

Q. 큰 JSON을 import해도 돼?

A.
주의해야 한다. import하면 bundle에 포함될 수 있으므로 필요 시 dynamic import나 API 제공을 검토한다.

Q. SVG를 inline으로 넣으면 항상 좋아?

A.
아니다. 작은 아이콘에는 유용할 수 있지만 큰 SVG나 반복 SVG는 HTML / JS 크기를 늘릴 수 있다.

Q. font가 LCP를 느리게 해. 무엇을 봐?

A.
font 파일 크기, weight 수, subset, preload, font-display, fallback metric, 외부 font provider 요청을 확인한다.

Q. font weight는 많이 넣어도 돼?

A.
필요한 weight만 포함하는 것이 좋다. weight가 많을수록 다운로드 비용이 증가한다.

Q. Source Map 공개해도 돼?

A.
가능은 하지만 코드 노출 위험이 있으므로 비공개 업로드나 접근 제한을 검토해야 한다.

Q. Production Source Map은 왜 필요해?

A.
minified production 오류를 원본 TypeScript / React 코드 위치로 매핑해 debugging과 error monitoring을 쉽게 하기 위해 필요하다.

Q. Source Map과 release version은 왜 연결해?

A.
해당 release의 minified bundle과 source map이 일치해야 정확한 원본 위치를 찾을 수 있기 때문이다.

Q. Next.js use client가 bundle에 영향 줘?

A.
그렇다. Client Component와 그 dependency는 브라우저 bundle에 포함될 수 있으므로 boundary를 신중히 설계해야 한다.

Q. Server Component 쓰면 bundle 줄어?

A.
상호작용이 필요 없는 UI를 Server Component로 유지하면 client bundle을 줄이는 데 도움이 될 수 있다.

Q. 공통 layout에 무거운 dependency 넣으면 왜 문제야?

A.
여러 route에서 불필요하게 로드되어 initial 또는 shared chunk가 커질 수 있기 때문이다.

Q. server-only code가 client bundle에 들어가면 왜 위험해?

A.
서버 전용 로직이나 secret 접근 코드가 브라우저 bundle에 포함될 수 있어 보안과 번들 크기 문제가 생긴다.

Q. Build Cache는 왜 필요해?

A.
로컬 개발과 CI에서 반복 빌드 시간을 줄이고 피드백 속도를 높이기 위해 필요하다.

Q. Cache가 있으면 항상 좋아?

A.
아니다. cache key가 잘못되면 오래된 결과를 재사용해 문제를 만들 수 있다.

Q. Monorepo에서 affected build는 뭐야?

A.
변경된 파일이 영향을 주는 app과 package만 build / test하는 전략이다.

Q. Shared UI Package가 bundle을 키울 수 있어?

A.
그렇다. import 구조와 barrel export가 잘못되면 사용하지 않는 컴포넌트까지 포함될 수 있다.

Q. Development Build로 bundle 크기 판단해도 돼?

A.
안 된다. production build는 minification, tree shaking, code splitting이 다르게 적용된다.

Q. Production Build에서만 오류가 나. 무엇을 봐?

A.
minification, tree shaking, env 변수, source map, SSR / hydration 차이, browser target을 확인해야 한다.

Q. Bundle Budget은 어떻게 잡아?

A.
현재 baseline을 측정하고 critical route와 non-critical route를 나눈 뒤 initial JS, route chunk, CSS, asset 기준을 설정한다.

Q. Bundle Budget 넘으면 무조건 실패시켜야 해?

A.
프로젝트 정책에 따라 warning, PR review, 실패 처리 중 선택할 수 있다.

Q. Third-party Script도 build optimization 대상이야?

A.
그렇다. 외부 script는 초기 로딩, main thread, 보안, 개인정보에 큰 영향을 줄 수 있다.

Q. Analytics script는 언제 로드해야 해?

A.
critical rendering을 방해하지 않도록 지연 로드나 consent 이후 로딩을 검토한다.

Q. Payment SDK는 lazy loading해도 돼?

A.
가능하지만 결제 버튼 클릭 후 지연이 커지지 않도록 결제 페이지 진입 시 로딩이나 prefetch를 검토한다.

Q. Web Worker는 언제 써?

A.
큰 데이터 파싱, 검색 인덱싱, 이미지 처리처럼 main thread를 오래 막는 작업에 적합하다.

Q. Worker를 쓰면 항상 빨라져?

A.
아니다. worker 초기화와 메시지 전달 비용이 있어 작은 작업에는 오히려 비효율적일 수 있다.

Q. Worker bundle도 분석해야 해?

A.
그렇다. worker 내부 dependency도 별도 chunk로 포함되어 번들 크기에 영향을 준다.

Q. Build 결과물에 secret이 들어가면 어떻게 해?

A.
즉시 secret을 제거하고 rotate하며, 노출된 build artifact와 로그 범위를 확인해야 한다.

Q. NEXT_PUBLIC에 secret 넣어도 돼?

A.
안 된다. `NEXT_PUBLIC_` 환경변수는 client bundle에 포함될 수 있으므로 공개 값으로 취급해야 한다.

Q. Build Optimization 후 무엇을 검증해?

A.
production build, bundle analyzer, route chunk, gzip / brotli 크기, loading UX, source map, E2E smoke test, 성능 지표를 확인해야 한다.

Q. 번들 크기가 줄었으면 성공이야?

A.
중요한 개선이지만 loading UX, runtime 성능, chunk error, 사용자 체감 성능도 함께 확인해야 한다.

Q. Frontend Build Optimization 코드 리뷰 기준은?

A.
Production build 분석, initial bundle, route chunk, dependency, tree shaking, dynamic import, source map, `use client`, build cache, bundle budget을 확인한다.

Q. Frontend Build Optimization / Bundling RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 bundle size, chunk strategy, code splitting, tree shaking, dependency, source map, build cache, bundle budget을 분석하고 최적화하게 만드는 것이다.
