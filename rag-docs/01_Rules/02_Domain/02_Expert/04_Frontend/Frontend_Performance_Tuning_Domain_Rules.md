# Frontend Performance Tuning Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Performance Tuning Domain 목적

### [개념]

Frontend Performance Tuning Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent용 RAG 문서 제작 규칙이다.

Frontend Performance Tuning은 사용자가 화면을 빠르게 보고, 빠르게 상호작용하고, 끊김 없이 사용할 수 있도록 렌더링, 번들, 네트워크, 이미지, 폰트, 캐시, JavaScript 실행 비용, Hydration 비용, Core Web Vitals를 개선하는 영역이다.

목적:

- 프론트엔드 성능 병목 진단 지원
- Core Web Vitals 기준 적용 지원
- Bundle Size 최적화 지원
- Code Splitting / Lazy Loading 판단 지원
- Image / Font 최적화 지원
- Rendering / Re-render 최적화 지원
- React / Next.js App Router 성능 개선 지원
- Data Fetching / Caching 성능 개선 지원
- Hydration Cost 감소 지원
- Network Waterfall 개선 지원
- Performance Profiling 지원
- Frontend Performance 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Core Web Vitals
2. Measurement First
3. Bundle Size Optimization
4. JavaScript Execution Cost
5. Rendering / Re-render Optimization
6. Image Optimization
7. Font Optimization
8. Code Splitting
9. Lazy Loading
10. Data Fetching Optimization
11. Caching Strategy
12. Network Waterfall Reduction
13. Hydration Cost Reduction
14. React Performance
15. Next.js App Router Performance
16. Runtime Performance
17. Performance Budget
18. Monitoring / Observability
19. Performance Review Criteria

---

### [실무]

2026 실무 기준:

- 측정 없이 최적화하지 않음
- Core Web Vitals 기준으로 사용자 체감 성능 판단
- Lighthouse / Web Vitals / Browser DevTools / React Profiler 사용 기준 포함
- 초기 로딩 성능과 상호작용 성능을 분리
- Bundle Size와 JavaScript 실행 비용을 함께 검토
- Image / Font 최적화는 기본 성능 작업으로 포함
- React에서는 상태 위치, Context 범위, Re-render 원인부터 점검
- Next.js App Router에서는 Server Component 활용과 Client Component 최소화 우선
- Hydration 비용을 줄이기 위해 `use client` 범위 최소화
- Data Fetching은 병렬화, 캐싱, 중복 요청 방지 기준 포함
- 성능 개선은 UX / 유지보수성 / 복잡도와 균형 유지
- Agent가 코드 생성과 코드 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Performance Tuning 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 성능 병목을 진단하고 Bundle, Rendering, Network, Image, Font, Cache, React, Next.js 성능을 개선하도록 돕는 RAG 문서 제작 규칙이다.

Q. 성능 최적화는 감으로 해도 되나?

A.
안 된다. 측정 도구로 병목을 확인한 뒤 가장 큰 영향을 주는 지점부터 개선해야 한다.

Q. Frontend Performance Tuning은 React 전용인가?

A.
아니다. React / Next.js 중심으로 작성하되 브라우저 렌더링, 네트워크, 이미지, 폰트, 캐시 같은 일반 프론트엔드 성능 기준도 포함한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Performance Tuning Domain은 사용자가 체감하는 로딩 속도, 렌더링 속도, 상호작용 반응성, 화면 안정성을 개선하는 기준을 포함한다.

---

### [핵심]

포함 범위:

- Core Web Vitals
- LCP
- INP
- CLS
- TTFB
- FCP
- TTI
- Lighthouse
- Web Vitals
- Performance Profiling
- Browser DevTools
- React Profiler
- Bundle Analysis
- Bundle Size
- JavaScript Execution Cost
- Code Splitting
- Lazy Loading
- Dynamic Import
- Tree Shaking
- Dead Code Elimination
- Minification
- Compression
- Image Optimization
- Responsive Image
- Lazy Image
- Font Optimization
- Font Loading
- Critical CSS
- CSS Optimization
- Rendering Optimization
- Re-render Optimization
- Memoization
- Virtualization
- Debounce / Throttle
- Web Worker
- Network Waterfall
- Preload
- Prefetch
- Preconnect
- DNS Prefetch
- Caching
- HTTP Cache
- CDN Cache
- Next.js Cache
- Data Fetching Optimization
- Hydration Cost
- Server Component
- Client Component
- Streaming
- Suspense
- Performance Budget
- Monitoring
- RUM
- Synthetic Monitoring

---

### [실무]

제외 범위:

- 브라우저 엔진 내부 구현 심화
- 네트워크 프로토콜 심화 전체
- CDN 운영 심화
- Backend Performance Tuning 심화
- Database Query Tuning 심화
- Kubernetes / Infra Scaling 심화
- Native App Performance 심화
- Game Rendering Optimization 심화
- WebGL / Canvas 심화
- React 기초 문법 전체
- Next.js App Router 상세 전체

단, Frontend 성능 개선에 필요한 수준의 React / Next.js / Network / Browser / Build Tool 지식은 포함 가능하다.

---

### [FAQ]

Q. Frontend Performance 문서에 Backend 성능도 포함해야 하나?

A.
심화는 제외한다. 단, TTFB, API 응답 시간, 캐싱, 데이터 요청 병렬화처럼 프론트엔드 체감 성능과 연결되는 범위는 포함한다.

Q. React 성능 최적화만 다루면 되나?

A.
아니다. Bundle, Network, Image, Font, Cache, Hydration, Rendering, Monitoring까지 함께 다뤄야 한다.

Q. Next.js App Router 성능 기준도 포함해야 하나?

A.
포함해야 한다. Server Component, Client Component, Streaming, Cache, Data Fetching은 App Router 성능의 핵심이다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Performance Tuning RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

Frontend Performance Tuning 문서는 진단과 개선 순서가 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Measure → Identify Bottleneck → Optimize → Verify → Monitor
- `[Comparison]`: Lazy Loading vs Preloading, SSR vs CSR, Memoization vs Component Split
- `[Best Practice]`: Performance Budget, Bundle Split, Image Optimization
- `[Troubleshooting]`: LCP 느림, INP 나쁨, CLS 발생, Hydration 비용 큼
- `[Checklist]`: 배포 전 성능 점검

---

### [FAQ]

Q. Frontend Performance 문서에 Flow가 필요한 이유는?

A.
성능 개선은 측정, 병목 확인, 개선, 재측정 순서가 중요하므로 Flow가 있어야 Agent가 무분별한 최적화를 피할 수 있다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Performance Tuning Principles Rules

## 4.1 성능 최적화 원칙

### [개념]

Frontend Performance Tuning 원칙은 사용자의 실제 체감 속도를 기준으로 병목을 측정하고, 가장 큰 영향을 주는 문제부터 해결하는 기준이다.

---

### [핵심]

필수 원칙:

- Measure First
- User-centric Metrics
- Performance Budget
- Critical Path Optimization
- Less JavaScript
- Less Blocking Work
- Faster Rendering
- Stable Layout
- Efficient Data Fetching
- Cache Correctly
- Optimize Images
- Optimize Fonts
- Avoid Premature Optimization
- Verify After Change
- Monitor in Production

기본 Flow:

```text
Measure
→ Find Bottleneck
→ Optimize One Area
→ Re-measure
→ Compare Result
→ Monitor
```

---

### [실무]

설계 기준:

- Lighthouse 점수만 보지 않고 실제 사용자 지표도 확인
- 가장 느린 페이지와 핵심 사용자 Flow부터 최적화
- 초기 로딩과 상호작용 지연을 분리해서 분석
- JavaScript를 줄이는 것이 많은 경우 가장 큰 개선
- 이미지와 폰트는 기본 점검 대상
- React Re-render보다 Bundle / Network가 더 큰 병목일 수 있음
- 성능 개선이 코드 복잡도를 과도하게 높이면 재검토
- 최적화 전후 수치를 기록
- Production Monitoring으로 실제 사용자 환경 확인

---

### [FAQ]

Q. 프론트엔드 성능 최적화는 무엇부터 해야 하나?

A.
먼저 Core Web Vitals, Lighthouse, DevTools, 실제 사용자 데이터를 측정하고 가장 큰 병목부터 개선한다.

Q. Lighthouse 점수만 높으면 성능이 좋은가?

A.
항상 그렇지는 않다. Lighthouse는 실험실 지표이고 실제 사용자 환경의 RUM 데이터와 함께 봐야 한다.

Q. 성능 최적화를 너무 많이 하면 문제가 되나?

A.
그렇다. 코드 복잡도 증가, 유지보수성 저하, 잘못된 캐싱 같은 문제가 생길 수 있다.

---

# 5. Core Web Vitals Rules

## 5.1 사용자 중심 성능 지표

### [개념]

Core Web Vitals는 사용자의 로딩 속도, 상호작용 반응성, 화면 안정성을 측정하는 핵심 지표이다.

---

### [핵심]

필수 포함:

- LCP
- INP
- CLS
- TTFB
- FCP
- Core Web Vitals
- Field Data
- Lab Data
- RUM
- Synthetic Test
- User Experience Metric

지표 의미:

| 지표 | 의미                     | 주요 병목                    |
| ---- | ------------------------ | ---------------------------- |
| LCP  | 가장 큰 콘텐츠 표시 시간 | 이미지, 서버 응답, CSS, JS   |
| INP  | 상호작용 응답성          | 긴 JS 작업, 렌더링 블로킹    |
| CLS  | 레이아웃 이동 안정성     | 이미지 크기 누락, 광고, 폰트 |
| TTFB | 서버 첫 응답 시간        | 서버 처리, CDN, 캐시         |
| FCP  | 첫 콘텐츠 표시 시간      | HTML, CSS, JS, 폰트          |

---

### [실무]

지표별 개선 방향:

- LCP 개선: Hero Image 최적화, 서버 응답 개선, Critical CSS, Preload
- INP 개선: 긴 JavaScript 작업 분할, Event Handler 최적화, 불필요한 Re-render 감소
- CLS 개선: 이미지 크기 지정, Skeleton 공간 확보, 폰트 교체 레이아웃 이동 방지
- TTFB 개선: CDN, 서버 캐시, Edge Cache, API 응답 개선
- FCP 개선: 초기 CSS / JS 최소화, 렌더링 차단 리소스 감소

주의:

- Lab Data와 Field Data가 다를 수 있음
- 페이지별로 병목 지표가 다를 수 있음
- 평균보다 느린 사용자 구간을 함께 확인
- 성능 지표는 개선 전후 비교해야 의미 있음

---

### [FAQ]

Q. Core Web Vitals에서 가장 중요한 지표는?

A.
LCP, INP, CLS가 핵심이다. 각각 로딩 속도, 상호작용 반응성, 화면 안정성을 나타낸다.

Q. LCP가 느리면 무엇을 봐야 하나?

A.
Hero Image, 서버 응답 시간, CSS / JS 차단, 이미지 preload 여부를 확인해야 한다.

Q. INP가 나쁘면 무엇을 봐야 하나?

A.
긴 JavaScript 작업, 무거운 이벤트 핸들러, 불필요한 Re-render, 메인 스레드 blocking 작업을 확인해야 한다.

Q. CLS가 발생하면 무엇을 봐야 하나?

A.
이미지 크기 누락, 광고 / 배너 삽입, 폰트 로딩, 동적 콘텐츠 공간 확보 여부를 확인해야 한다.

---

# 6. Measurement and Profiling Rules

## 6.1 측정 / 프로파일링 기준

### [개념]

Measurement and Profiling은 성능 병목을 추측하지 않고 도구로 확인하는 과정이다.

---

### [핵심]

필수 도구:

- Lighthouse
- Chrome DevTools Performance
- Chrome DevTools Network
- Chrome DevTools Coverage
- React Profiler
- Bundle Analyzer
- Web Vitals
- Real User Monitoring
- Synthetic Monitoring
- Performance Mark
- Performance Measure

측정 Flow:

```text
Select Page
→ Run Lab Test
→ Check Core Web Vitals
→ Inspect Network
→ Inspect Main Thread
→ Inspect Bundle
→ Inspect React Render
→ Apply Fix
→ Re-measure
```

---

### [실무]

측정 기준:

- 핵심 페이지부터 측정
- 모바일 네트워크 / 저사양 CPU 조건도 확인
- DevTools Network로 요청 Waterfall 확인
- Performance 패널로 Long Task 확인
- Coverage로 사용하지 않는 JS / CSS 확인
- React Profiler로 비용 큰 컴포넌트 확인
- Bundle Analyzer로 큰 dependency 확인
- 실제 사용자 RUM 데이터와 비교
- 변경 전후 수치를 기록
- 한 번에 여러 최적화를 섞지 않기

---

### [FAQ]

Q. 성능 병목은 어떻게 찾나?

A.
Lighthouse, DevTools Network, Performance 패널, React Profiler, Bundle Analyzer를 사용해 Network, JavaScript, Rendering 병목을 분리해서 확인한다.

Q. React Profiler만 보면 충분한가?

A.
아니다. React Re-render보다 Bundle, Image, Network, Font가 더 큰 병목일 수 있다.

Q. 성능 측정은 개발 환경에서만 해도 되나?

A.
아니다. Production Build 기준으로 측정해야 실제 성능에 가깝다.

---

# 7. Bundle Size Optimization Rules

## 7.1 Bundle Size 최적화

### [개념]

Bundle Size Optimization은 브라우저가 다운로드, 파싱, 컴파일, 실행해야 하는 JavaScript와 CSS의 양을 줄이는 작업이다.

---

### [핵심]

필수 포함:

- Bundle Size
- Initial Bundle
- Route Bundle
- Shared Chunk
- Code Splitting
- Tree Shaking
- Dead Code Elimination
- Dynamic Import
- Bundle Analyzer
- Dependency Audit
- Polyfill
- Minification
- Compression
- Gzip
- Brotli

Bundle 분석 Flow:

```text
Build Production
→ Run Bundle Analyzer
→ Find Large Dependency
→ Check Initial Bundle
→ Split or Replace
→ Remove Unused Code
→ Rebuild and Compare
```

---

### [실무]

최적화 기준:

- Initial Bundle 크기 우선 확인
- 사용 빈도가 낮은 기능은 lazy loading
- 큰 라이브러리는 대체 가능성 검토
- 전체 라이브러리 import 대신 필요한 모듈만 import
- 중복 dependency 확인
- polyfill이 과도하게 포함되는지 확인
- Tree Shaking이 가능한 import 형태 사용
- 개발 전용 코드가 production에 포함되지 않게 관리
- CSS도 사용하지 않는 스타일 제거 고려
- Bundle Budget 설정 권장

주의:

- 번들을 무조건 잘게 쪼개면 요청 수와 관리 복잡도 증가
- Code Splitting은 사용자 흐름 기준으로 적용
- Dynamic Import가 UX 지연을 만들 수 있음
- 큰 dependency 추가는 리뷰 대상

---

### [FAQ]

Q. Bundle Size가 크면 왜 느려지나?

A.
다운로드뿐 아니라 JavaScript 파싱, 컴파일, 실행 비용이 증가해 초기 로딩과 상호작용이 느려질 수 있다.

Q. Bundle Analyzer로 무엇을 봐야 하나?

A.
Initial Bundle, 큰 dependency, 중복 dependency, 예상보다 큰 shared chunk를 확인해야 한다.

Q. 큰 라이브러리를 쓰면 무조건 나쁜가?

A.
아니다. 사용 가치가 크면 사용할 수 있지만 초기 번들에 포함되는지, lazy loading 가능한지 검토해야 한다.

---

# 8. Code Splitting and Lazy Loading Rules

## 8.1 Code Splitting / Lazy Loading

### [개념]

Code Splitting은 코드를 여러 bundle로 나누는 전략이고, Lazy Loading은 필요한 시점에 코드를 불러오는 전략이다.

---

### [핵심]

필수 포함:

- Code Splitting
- Lazy Loading
- Dynamic Import
- Route-based Splitting
- Component-based Splitting
- Library Lazy Loading
- Suspense
- Loading Fallback
- Prefetch
- Initial Bundle Reduction
- Interaction Delay

예시:

```tsx
const ChartPanel = React.lazy(() => import("./ChartPanel"));

export function Dashboard() {
  return (
    <React.Suspense fallback={<p>Loading chart...</p>}>
      <ChartPanel />
    </React.Suspense>
  );
}
```

---

### [실무]

적합한 대상:

- 차트 라이브러리
- 에디터
- 지도
- 관리자 전용 기능
- 모달 내부 무거운 기능
- 사용 빈도 낮은 위젯
- 라우트별 큰 페이지
- 결제 / 분석 / 리포트 기능

주의:

- 첫 화면 핵심 UI를 과도하게 lazy loading하지 않기
- Lazy Loading fallback UI 제공
- 사용자 클릭 후 너무 오래 기다리게 하지 않기
- 필요한 경우 prefetch 검토
- Code Splitting이 너무 세분화되면 overhead 증가
- Suspense Boundary 위치를 명확히 설정

---

### [FAQ]

Q. Code Splitting은 언제 해야 하나?

A.
초기 화면에 필요 없는 큰 기능이나 특정 라우트에서만 사용하는 코드를 분리할 때 사용한다.

Q. Lazy Loading은 무엇을 줄이나?

A.
초기 Bundle Size와 초기 JavaScript 실행 비용을 줄인다.

Q. 모든 컴포넌트를 lazy loading하면 좋은가?

A.
아니다. 핵심 UI까지 lazy loading하면 오히려 사용자 체감 속도가 나빠질 수 있다.

---

# 9. JavaScript Execution Cost Rules

## 9.1 JavaScript 실행 비용 최적화

### [개념]

JavaScript Execution Cost는 브라우저가 JavaScript를 파싱, 컴파일, 실행하는 데 드는 비용이다.

---

### [핵심]

필수 포함:

- Main Thread
- Long Task
- Script Evaluation
- Parse Cost
- Compile Cost
- Event Handler Cost
- Blocking JavaScript
- Task Splitting
- Idle Callback
- Web Worker
- Debounce
- Throttle
- Less JavaScript

---

### [실무]

최적화 기준:

- Long Task를 DevTools Performance에서 확인
- 무거운 계산은 memoization 또는 worker 검토
- 입력 이벤트 핸들러는 가볍게 유지
- 스크롤 / 리사이즈 이벤트는 throttle / debounce 적용
- 대용량 JSON 파싱 주의
- 반복 DOM 계산 최소화
- Third-party Script 영향 확인
- 초기 실행 JS 줄이기
- 사용하지 않는 코드 제거
- 복잡한 작업은 작은 task로 분할

주의:

- `useMemo`는 렌더링 중 계산 비용을 줄이지만 초기 bundle 비용을 줄이지 않음
- Web Worker는 통신 비용이 있으므로 무거운 작업에만 적합
- debounce는 반응성을 늦출 수 있음
- throttle은 최신 입력 반영 지연 가능성 있음

---

### [FAQ]

Q. JavaScript 실행 비용은 왜 중요한가?

A.
다운로드가 끝나도 JavaScript 파싱, 컴파일, 실행이 오래 걸리면 화면 표시와 사용자 상호작용이 느려진다.

Q. Long Task는 무엇인가?

A.
메인 스레드를 오래 점유해 사용자 입력 처리와 렌더링을 지연시키는 작업이다.

Q. 무거운 계산은 어떻게 처리하나?

A.
계산량이 크면 memoization, task splitting, Web Worker, 서버 계산 이전을 검토한다.

---

# 10. Rendering Optimization Rules

## 10.1 브라우저 렌더링 최적화

### [개념]

Rendering Optimization은 Layout, Paint, Composite 비용을 줄이고 화면 갱신을 부드럽게 만드는 작업이다.

---

### [핵심]

필수 포함:

- Rendering Pipeline
- Style Calculation
- Layout
- Paint
- Composite
- Layout Thrashing
- Reflow
- Repaint
- CSS Containment
- Transform
- Opacity
- Animation Performance
- DOM Size
- Virtualization

렌더링 비용 Flow:

```text
DOM / CSSOM Change
→ Style
→ Layout
→ Paint
→ Composite
```

---

### [실무]

최적화 기준:

- DOM node 수 과다 여부 확인
- 큰 리스트는 virtualization 적용 검토
- 애니메이션은 transform / opacity 우선
- layout을 자주 유발하는 속성 애니메이션 지양
- 반복적인 DOM read / write 섞기 주의
- CSS selector 복잡도 과도화 주의
- Layout Shift 발생 요소 공간 확보
- 고정 크기 이미지 / 광고 / 배너 영역 지정
- Offscreen 영역 렌더링 지연 고려
- Paint 비용 큰 effect 사용 주의

---

### [FAQ]

Q. Layout Thrashing은 무엇인가?

A.
DOM 읽기와 쓰기가 반복되어 브라우저가 Layout 계산을 여러 번 강제로 수행하는 문제이다.

Q. 애니메이션에서 어떤 속성이 성능에 좋은가?

A.
대체로 `transform`, `opacity`는 layout을 덜 유발해 성능에 유리하다.

Q. DOM이 많으면 왜 느려지나?

A.
Style 계산, Layout, Paint 비용이 증가하고 이벤트 처리와 메모리 사용량도 늘어날 수 있다.

---

# 11. React Performance Rules

## 11.1 React Rendering / Re-render 최적화

### [개념]

React Performance는 state, props, context 변경으로 발생하는 렌더링 비용을 분석하고 필요한 범위만 최적화하는 작업이다.

---

### [핵심]

필수 포함:

- Re-render Cause
- State Colocation
- Component Split
- Context Split
- React Profiler
- `React.memo`
- `useMemo`
- `useCallback`
- `useTransition`
- `useDeferredValue`
- List Key
- Virtualization
- Expensive Component
- Stale Closure

Re-render 분석 Flow:

```text
Re-render 발생
→ React Profiler 확인
→ State 위치 확인
→ Props 변경 확인
→ Context 변경 확인
→ Component Split 검토
→ Memoization 필요 여부 판단
```

---

### [실무]

최적화 우선순위:

1. State Colocation
2. Component Split
3. Context 범위 축소
4. Context Value 분리
5. Derived Value 계산 최적화
6. List Virtualization
7. `React.memo`
8. `useMemo`
9. `useCallback`
10. `useTransition` / `useDeferredValue`

주의:

- Re-render 자체는 문제 아님
- 비용 큰 Re-render가 자주 발생하는 것이 문제
- `useMemo` / `useCallback` 남용 금지
- Dependency 누락은 stale value 버그 발생
- Context Provider value가 매번 새 객체이면 re-render 증가
- List key로 index 남용 시 렌더링 문제 가능
- Profiler로 실제 병목 확인 후 최적화

---

### [FAQ]

Q. React에서 re-render는 무조건 나쁜가?

A.
아니다. 문제는 비용이 큰 re-render가 자주 발생해 사용자 상호작용을 지연시키는 경우이다.

Q. React 성능 최적화는 무엇부터 해야 하나?

A.
State 위치와 컴포넌트 분리를 먼저 확인하고, 그 다음 Context 범위와 memoization을 검토한다.

Q. `useMemo`와 `useCallback`은 항상 써야 하나?

A.
아니다. 계산 비용이 크거나 참조 안정성이 실제로 필요한 경우에만 사용한다.

---

# 12. Context Performance Rules

## 12.1 Context Re-render 최적화

### [개념]

Context Performance는 Provider value 변경으로 많은 하위 컴포넌트가 다시 렌더링되는 문제를 줄이는 기준이다.

---

### [핵심]

필수 포함:

- Context Provider
- Context Value
- Provider Scope
- Context Split
- State Context
- Action Context
- Memoized Value
- Frequent Update
- Selector Pattern
- External Store

예시:

```tsx
const value = React.useMemo(() => {
  return { theme, setTheme };
}, [theme]);
```

---

### [실무]

최적화 기준:

- Provider 범위를 필요한 영역으로 제한
- 자주 바뀌는 값과 거의 안 바뀌는 값 분리
- State Context와 Action Context 분리 검토
- Provider value memoization
- 대규모 자주 변경되는 상태는 External Store 검토
- Context를 전역 Store처럼 남용하지 않기
- Compound Component 내부 Context는 범위를 좁게 유지
- Context 변경으로 re-render되는 컴포넌트 확인

주의:

- `useMemo`만으로 모든 Context re-render가 해결되지 않음
- Context 소비 컴포넌트가 많을수록 영향 증가
- 고빈도 입력 상태를 Context에 넣지 않기
- Context는 낮은 빈도의 공유 값에 적합

---

### [FAQ]

Q. Context를 쓰면 왜 re-render가 많이 발생하나?

A.
Provider value가 변경되면 해당 Context를 사용하는 하위 컴포넌트들이 다시 렌더링될 수 있기 때문이다.

Q. Context 성능은 어떻게 개선하나?

A.
Provider 범위를 줄이고, value를 memoization하고, 자주 바뀌는 값과 안정적인 값을 분리한다.

Q. 모든 전역 상태를 Context에 넣어도 되나?

A.
권장하지 않는다. 자주 바뀌는 대규모 상태는 External Store를 검토한다.

---

# 13. List Rendering and Virtualization Rules

## 13.1 대량 리스트 렌더링 최적화

### [개념]

List Rendering Optimization은 많은 항목을 렌더링할 때 DOM 수와 렌더링 비용을 줄이는 전략이다.

---

### [핵심]

필수 포함:

- Large List
- Virtualization
- Windowing
- Infinite Scroll
- Pagination
- Stable Key
- Item Memoization
- Row Height
- Overscan
- Scroll Performance
- Table Performance

---

### [실무]

최적화 기준:

- 항목 수가 많으면 pagination 또는 virtualization 검토
- 화면에 보이는 항목만 렌더링
- 안정적인 key 사용
- index key 남용 금지
- Row height가 일정하면 virtualization 구현이 쉬움
- 무한 스크롤은 접근성과 SEO 고려
- Pagination은 관리 화면 / 검색 결과에 적합
- Item 컴포넌트 비용이 크면 memoization 검토
- Scroll 이벤트는 throttle 고려
- Table은 column 수와 cell 렌더링 비용 확인

주의:

- Virtualization은 구현 복잡도 증가
- SEO가 중요한 목록은 SSR / Pagination 고려
- 동적 높이 리스트는 virtualization 난이도 증가
- 무한 스크롤은 footer 접근과 브라우저 history 고려

---

### [FAQ]

Q. 리스트가 느리면 무엇을 해야 하나?

A.
항목 수, item 렌더링 비용, key 안정성, pagination 또는 virtualization 적용 가능성을 확인한다.

Q. Virtualization은 언제 쓰나?

A.
수백 개 이상의 항목처럼 화면 밖 항목까지 모두 렌더링해 성능 문제가 발생할 때 사용한다.

Q. index를 key로 쓰면 안 되나?

A.
정렬, 삽입, 삭제가 있는 리스트에서는 렌더링 오류와 상태 꼬임이 발생할 수 있어 피하는 것이 좋다.

---

# 14. Image Optimization Rules

## 14.1 이미지 최적화

### [개념]

Image Optimization은 이미지 용량, 크기, 포맷, 로딩 시점, LCP 이미지 우선순위를 최적화해 로딩 성능을 개선하는 작업이다.

---

### [핵심]

필수 포함:

- Image Size
- Responsive Image
- Image Format
- WebP
- AVIF
- Lazy Loading
- Priority Image
- LCP Image
- Width / Height
- Placeholder
- Blur Placeholder
- CDN
- Compression
- `srcset`
- `sizes`
- Next.js Image

예시:

```tsx
import Image from "next/image";

export function HeroImage() {
  return (
    <Image src="/hero.webp" alt="Hero" width={1200} height={630} priority />
  );
}
```

---

### [실무]

최적화 기준:

- 실제 표시 크기에 맞는 이미지 제공
- LCP Hero Image는 우선 로딩 고려
- 화면 아래 이미지는 lazy loading
- width / height 지정으로 CLS 방지
- WebP / AVIF 같은 현대 포맷 검토
- 큰 배경 이미지는 LCP 영향 확인
- Placeholder로 체감 로딩 개선 가능
- Decorative Image는 alt 처리 명확화
- CDN Image Optimization 검토
- 이미지 품질과 용량 균형 유지

주의:

- 모든 이미지에 priority 사용 금지
- 이미지 크기를 CSS로만 줄이고 원본을 크게 내려받지 않기
- alt 누락 금지
- Lazy Loading이 LCP 이미지를 늦추지 않도록 주의
- 외부 이미지 도메인 설정 확인

---

### [FAQ]

Q. 이미지 때문에 LCP가 느리면 무엇을 해야 하나?

A.
Hero Image 크기, 포맷, preload 또는 priority, 서버 응답, width / height 지정 여부를 확인해야 한다.

Q. 모든 이미지를 lazy loading하면 되나?

A.
아니다. 첫 화면의 LCP 이미지는 lazy loading하면 오히려 느려질 수 있다.

Q. 이미지 width와 height는 왜 지정해야 하나?

A.
브라우저가 이미지 공간을 미리 확보해 CLS를 줄일 수 있기 때문이다.

---

# 15. Font Optimization Rules

## 15.1 폰트 최적화

### [개념]

Font Optimization은 웹 폰트 로딩으로 인한 렌더링 지연, 텍스트 깜빡임, 레이아웃 이동을 줄이는 작업이다.

---

### [핵심]

필수 포함:

- Web Font
- Font Display
- FOIT
- FOUT
- Font Subset
- Preload Font
- Self-hosted Font
- System Font
- Variable Font
- Font Metric
- CLS
- Next Font

---

### [실무]

최적화 기준:

- 필요한 font weight만 로드
- 사용하지 않는 font subset 제거
- `font-display` 전략 설정
- 중요한 폰트는 preload 고려
- 시스템 폰트 사용 가능성 검토
- Variable Font는 weight 다수가 필요할 때 검토
- 폰트 교체로 인한 CLS 확인
- Next.js에서는 font optimization 기능 활용 가능
- 한 페이지에 너무 많은 font family 사용 금지
- 아이콘 폰트보다 SVG 아이콘 검토

주의:

- 모든 폰트를 preload하지 않기
- 커스텀 폰트가 브랜드에 필수인지 검토
- 폰트 로딩 전략은 가독성과 성능 균형 필요
- 폰트 메트릭 차이로 레이아웃 이동 발생 가능

---

### [FAQ]

Q. 웹 폰트가 성능에 영향을 주나?

A.
그렇다. 폰트 다운로드와 교체 과정이 FCP, LCP, CLS에 영향을 줄 수 있다.

Q. 모든 폰트를 preload하면 좋은가?

A.
아니다. 중요한 폰트만 preload해야 하며 과도한 preload는 네트워크 경쟁을 만든다.

Q. 시스템 폰트는 성능에 유리한가?

A.
대체로 유리하다. 별도 다운로드가 필요 없기 때문이다.

---

# 16. CSS Performance Rules

## 16.1 CSS 최적화

### [개념]

CSS Performance는 렌더링 차단 CSS, 사용하지 않는 스타일, 복잡한 selector, critical CSS, 스타일 계산 비용을 줄이는 작업이다.

---

### [핵심]

필수 포함:

- Critical CSS
- Render Blocking CSS
- Unused CSS
- CSS Splitting
- CSS Minification
- CSS Containment
- Selector Complexity
- Style Recalculation
- CSS-in-JS Runtime Cost
- Tailwind Purge
- CSS Modules
- Theme CSS Variable

---

### [실무]

최적화 기준:

- Critical CSS 우선 로딩
- 사용하지 않는 CSS 제거
- 페이지별 CSS 분리 검토
- selector 과도한 중첩 지양
- Runtime CSS-in-JS 비용 확인
- CSS Variable은 theme에 유용하지만 남용 주의
- 애니메이션은 layout 유발 속성보다 transform / opacity 우선
- Tailwind 사용 시 purge / content 설정 확인
- CSS 파일 크기와 적용 범위 확인
- 디자인 시스템 CSS가 전체 앱에 과도하게 로드되는지 확인

주의:

- CSS를 과도하게 쪼개면 관리 복잡도 증가
- Critical CSS 추출 오류는 스타일 깨짐 발생 가능
- Runtime style 생성은 hydration과 rendering 비용을 증가시킬 수 있음
- 사용하지 않는 글로벌 CSS 방치 금지

---

### [FAQ]

Q. CSS도 성능 병목이 될 수 있나?

A.
그렇다. 렌더링 차단 CSS, 사용하지 않는 대용량 CSS, 복잡한 selector는 렌더링을 늦출 수 있다.

Q. Critical CSS는 무엇인가?

A.
첫 화면 렌더링에 필요한 최소 CSS를 우선 제공하는 전략이다.

Q. Runtime CSS-in-JS는 왜 주의해야 하나?

A.
런타임에 스타일을 생성하면 JavaScript 실행과 hydration 비용이 증가할 수 있기 때문이다.

---

# 17. Network Optimization Rules

## 17.1 네트워크 최적화

### [개념]

Network Optimization은 요청 수, 요청 크기, 요청 순서, 캐시, CDN, preload / prefetch 전략을 조정해 리소스 로딩 시간을 줄이는 작업이다.

---

### [핵심]

필수 포함:

- Network Waterfall
- Request Count
- Request Size
- Critical Request
- Blocking Request
- Preload
- Prefetch
- Preconnect
- DNS Prefetch
- Compression
- CDN
- HTTP Cache
- Cache-Control
- Resource Priority
- Third-party Script

---

### [실무]

최적화 기준:

- DevTools Network Waterfall 확인
- Critical Request Chain 줄이기
- 불필요한 요청 제거
- 작은 요청이 너무 많은지 확인
- 압축 적용 확인
- CDN 사용 검토
- Static Asset Cache-Control 설정
- 외부 도메인은 preconnect 검토
- 다음 페이지 리소스는 prefetch 고려
- LCP 리소스는 preload 검토
- Third-party Script는 지연 로딩 또는 제한 검토
- API 중복 요청 제거

주의:

- preload 남용은 네트워크 경쟁을 유발
- prefetch는 사용 가능성이 높은 리소스에만 적용
- 외부 스크립트는 Core Web Vitals에 큰 영향 가능
- 캐시 정책은 데이터 신선도와 균형 필요

---

### [FAQ]

Q. Network Waterfall에서 무엇을 봐야 하나?

A.
느린 요청, 순차 요청, blocking 리소스, 큰 파일, 중복 요청, 외부 스크립트를 확인해야 한다.

Q. preload와 prefetch 차이는?

A.
preload는 현재 페이지에 곧 필요한 리소스 우선 로딩이고, prefetch는 다음에 필요할 가능성이 있는 리소스 사전 로딩이다.

Q. Third-party Script는 왜 위험한가?

A.
외부 스크립트가 메인 스레드를 점유하거나 네트워크를 차단해 LCP와 INP를 악화시킬 수 있다.

---

# 18. Data Fetching Performance Rules

## 18.1 데이터 패칭 성능

### [개념]

Data Fetching Performance는 API 요청 시점, 병렬화, 캐싱, 중복 제거, pagination, streaming, revalidation을 조정해 데이터 로딩 지연을 줄이는 작업이다.

---

### [핵심]

필수 포함:

- Parallel Fetching
- Sequential Fetching
- Request Waterfall
- Duplicate Request
- Cache
- Revalidation
- Pagination
- Infinite Query
- Prefetch Data
- Abort Request
- Race Condition
- Optimistic Update
- Stale Data
- Background Refetch
- Streaming

Flow:

```text
Page Request
→ Fetch Critical Data
→ Render Initial UI
→ Fetch Non-critical Data
→ Cache / Revalidate
→ Update UI
```

---

### [실무]

최적화 기준:

- 독립 요청은 병렬 처리
- 의존성이 있는 요청만 순차 처리
- 중복 API 요청 제거
- 서버 데이터는 cache 전략 적용
- 목록 데이터는 pagination / infinite scroll 검토
- 검색 입력은 debounce 적용 가능
- 사용자 이동 예상 경로는 prefetch 검토
- Mutation 후 cache invalidation / revalidation 수행
- 느린 데이터는 Suspense / Streaming 고려
- API 응답 크기 줄이기
- 필요한 필드만 요청 가능하면 projection 검토
- AbortController로 불필요한 요청 취소 가능

주의:

- 모든 데이터를 첫 화면에서 가져오지 않기
- waterfall 구조는 LCP 지연 원인
- cache 신선도 정책 없이 무작정 캐싱 금지
- debounce가 사용자 피드백을 늦추지 않게 조정
- optimistic update는 실패 rollback 필요

---

### [FAQ]

Q. API 요청이 느리면 프론트에서 무엇을 개선할 수 있나?

A.
요청 병렬화, 중복 요청 제거, 캐싱, pagination, prefetch, 응답 크기 축소, loading UI 개선을 검토할 수 있다.

Q. Request Waterfall은 왜 문제인가?

A.
독립적인 요청이 순차 실행되면 전체 대기 시간이 길어져 초기 렌더링이 늦어진다.

Q. 검색 API는 어떻게 최적화하나?

A.
debounce, abort, cache, URL State, pagination을 함께 고려한다.

---

# 19. Caching Strategy Rules

## 19.1 Cache 전략

### [개념]

Caching Strategy는 정적 리소스, API 응답, 서버 렌더링 결과, 클라이언트 서버 상태를 저장해 반복 요청 비용을 줄이는 전략이다.

---

### [핵심]

필수 포함:

- HTTP Cache
- Browser Cache
- CDN Cache
- Service Worker Cache
- Query Cache
- Next.js Cache
- Static Asset Cache
- API Cache
- Stale-while-revalidate
- Cache Invalidation
- Revalidation
- Cache Key
- User-specific Cache
- Public Cache
- Private Cache

---

### [실무]

Cache 판단 기준:

| 데이터 / 리소스     | 권장 전략                |
| ------------------- | ------------------------ |
| hashed static asset | long-term cache          |
| public image        | CDN cache                |
| 사용자별 정보       | private / no-store       |
| 게시글 목록         | revalidate / query cache |
| 검색 결과           | query key 기반 cache     |
| 실시간 알림         | no-store / short cache   |
| 관리자 통계         | short cache / dynamic    |
| design system CSS   | static cache             |
| API contract file   | versioned cache          |

주의:

- 사용자별 민감 데이터 public cache 금지
- Cache Key에 query / auth / locale 등 영향 요소 반영
- Mutation 후 Invalidation 필요
- 오래된 데이터 허용 범위 명확화
- 캐시가 성능을 높이지만 버그를 숨길 수 있음
- CDN Cache와 Browser Cache 정책 구분
- Next.js App Router Cache 정책은 데이터 성격별로 명확히 설정

---

### [FAQ]

Q. Cache는 무조건 많이 쓰면 좋은가?

A.
아니다. 데이터 신선도, 사용자별 보안, invalidation 전략이 없으면 오래된 데이터나 정보 노출 문제가 생길 수 있다.

Q. 사용자별 데이터는 캐시해도 되나?

A.
주의해야 한다. public cache는 금지하고 private cache 또는 no-store를 고려해야 한다.

Q. Mutation 후 데이터가 안 바뀌면 무엇을 확인해야 하나?

A.
Cache Key, Invalidation, Revalidation, Router Refresh, stale time 설정을 확인해야 한다.

---

# 20. Next.js App Router Performance Rules

## 20.1 Next.js App Router 성능 기준

### [개념]

Next.js App Router Performance는 Server Component, Client Component, Streaming, Suspense, Cache, Route Segment, Image / Font Optimization을 활용해 초기 로딩과 상호작용 비용을 줄이는 작업이다.

---

### [핵심]

필수 포함:

- Server Component
- Client Component
- `use client`
- Hydration Cost
- Streaming
- Suspense
- Route Segment
- `loading.tsx`
- `error.tsx`
- Dynamic Import
- Next Image
- Next Font
- Fetch Cache
- Revalidation
- Dynamic Rendering
- Static Rendering
- Partial Rendering

---

### [실무]

최적화 기준:

- Server Component를 기본으로 사용
- Client Component 범위 최소화
- `use client`는 필요한 leaf component에만 선언
- 상호작용 없는 UI는 Client Component로 만들지 않음
- 큰 Client Component는 분리 검토
- 느린 데이터는 Suspense / Streaming 활용
- `loading.tsx`로 route segment loading UX 제공
- 이미지와 폰트는 Next.js 최적화 기능 활용
- Fetch Cache / Revalidation 정책 명확화
- Dynamic Rendering이 필요한 이유를 명확히 함
- 사용자별 데이터와 public cache 혼동 금지

주의:

- Page 전체에 `use client` 남용 금지
- Server Component에서 Browser API 사용 금지
- Client Component로 전달하는 props 크기 주의
- 불필요한 Dynamic Rendering은 캐시 이점 감소
- Route Handler를 불필요하게 거쳐 내부 데이터 fetch하지 않기

---

### [FAQ]

Q. Next.js App Router 성능 최적화의 핵심은?

A.
Server Component를 기본으로 사용하고 Client Component와 Hydration 비용을 최소화하는 것이다.

Q. `use client`가 많으면 왜 느려질 수 있나?

A.
브라우저로 전송되는 JavaScript와 Hydration 비용이 증가하기 때문이다.

Q. App Router에서 느린 데이터는 어떻게 처리하나?

A.
Suspense, Streaming, `loading.tsx`, 캐싱, 병렬 Fetch를 고려한다.

---

# 21. Hydration Optimization Rules

## 21.1 Hydration Cost 감소

### [개념]

Hydration은 서버에서 렌더링된 HTML에 클라이언트 JavaScript 이벤트와 상태를 연결하는 과정이다. Hydration Cost는 이 과정에서 발생하는 JavaScript 실행 비용이다.

---

### [핵심]

필수 포함:

- Hydration
- Hydration Cost
- Hydration Error
- Client Component
- Server Component
- Partial Hydration
- Island Pattern
- JavaScript Bundle
- Event Handler
- Client Boundary
- Initial Interactivity
- Mismatch

Hydration 비용 Flow:

```text
Server HTML
→ Download JavaScript
→ Parse JavaScript
→ Execute JavaScript
→ Attach Event Handlers
→ Interactive UI
```

---

### [실무]

최적화 기준:

- 상호작용 없는 UI는 Server Component 유지
- Client Component 범위 최소화
- 무거운 Client Library lazy loading
- Client Component에 큰 데이터 props 전달 주의
- 브라우저 전용 로직은 작은 컴포넌트로 격리
- 초기 상호작용에 필요 없는 기능은 지연 로딩
- Hydration Error는 서버 / 클라이언트 렌더링 결과 차이 확인
- 날짜 / 랜덤 값 / window 접근은 Hydration mismatch 원인
- Theme 초기값 불일치로 flash / mismatch 발생 가능

주의:

- Hydration 비용은 Bundle Size와 연결됨
- 모든 UI를 Client Component로 만들면 SSR 장점 감소
- Hydration Error를 suppress로 덮기 전에 원인 확인
- 큰 Provider Tree도 Hydration 비용 증가 가능

---

### [FAQ]

Q. Hydration Cost는 왜 발생하나?

A.
서버 HTML에 클라이언트 JavaScript가 이벤트와 상태를 연결하기 위해 다운로드, 파싱, 실행되어야 하기 때문이다.

Q. Hydration 비용은 어떻게 줄이나?

A.
Client Component 범위를 줄이고, 상호작용 없는 UI를 Server Component로 유지하며, 무거운 클라이언트 코드를 지연 로딩한다.

Q. Hydration Error는 왜 발생하나?

A.
서버에서 렌더링한 결과와 클라이언트에서 렌더링한 결과가 다를 때 발생한다.

---

# 22. Third-party Script Performance Rules

## 22.1 외부 스크립트 최적화

### [개념]

Third-party Script Performance는 광고, 분석, 채팅, 지도, 결제, 소셜 위젯 같은 외부 스크립트가 로딩과 상호작용 성능에 미치는 영향을 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Third-party Script
- Analytics Script
- Ads Script
- Chat Widget
- Map SDK
- Payment SDK
- Social Widget
- Script Loading Strategy
- Defer
- Async
- Lazy Load
- Main Thread Blocking
- Resource Priority
- Consent-based Loading

---

### [실무]

최적화 기준:

- 꼭 필요한 외부 스크립트만 로드
- 첫 화면에 필요 없는 스크립트는 지연 로딩
- 사용자 동의 후 로딩이 필요한 스크립트 구분
- 지도 / 결제 / 채팅 SDK는 사용 페이지에서만 로드
- 분석 스크립트가 INP에 미치는 영향 확인
- Script loading strategy 명시
- 외부 스크립트 실패 시 UI fallback 고려
- 동일 기능 스크립트 중복 로드 금지
- 보안과 개인정보 처리 기준 검토

주의:

- 외부 스크립트는 직접 최적화가 어려움
- Third-party Script가 메인 스레드를 장시간 점유할 수 있음
- SDK를 전역으로 모든 페이지에 로드하지 않기
- 성능과 비즈니스 요구 균형 필요

---

### [FAQ]

Q. Third-party Script는 왜 성능에 위험한가?

A.
외부 스크립트가 네트워크와 메인 스레드를 점유해 LCP, INP, 초기 로딩을 악화시킬 수 있기 때문이다.

Q. 지도 SDK는 어디서 로드해야 하나?

A.
지도 기능이 필요한 페이지나 컴포넌트에서만 지연 로딩하는 것이 좋다.

Q. 분석 스크립트는 무조건 head에 넣어야 하나?

A.
아니다. 비즈니스 요구와 성능 영향을 고려해 loading strategy를 정해야 한다.

---

# 23. Performance Budget Rules

## 23.1 Performance Budget 기준

### [개념]

Performance Budget은 페이지나 앱이 넘지 말아야 할 Bundle Size, 이미지 용량, 요청 수, Core Web Vitals 목표를 미리 정하는 기준이다.

---

### [핵심]

필수 포함:

- Performance Budget
- JavaScript Budget
- CSS Budget
- Image Budget
- Request Budget
- LCP Target
- INP Target
- CLS Target
- Bundle Budget
- Route Budget
- CI Performance Check
- Regression Prevention

Budget 예시:

```text
Initial JS Budget
Route Bundle Budget
Image Weight Budget
Third-party Script Budget
LCP Target
INP Target
CLS Target
```

---

### [실무]

Budget 작성 기준:

- 핵심 페이지별 budget 설정
- 초기 JS 크기 제한
- Route별 bundle 크기 제한
- 이미지 최대 크기 기준 설정
- Third-party Script 추가는 리뷰 대상
- CI에서 bundle size regression 확인
- 목표 지표는 사용자 환경 기준으로 조정
- 성능 budget 초과 시 변경 이유 문서화
- 성능 개선은 지속 관리 대상
- Budget은 제품 성장에 따라 재검토

주의:

- 비현실적인 budget은 무시됨
- 모든 페이지에 같은 budget 강제 금지
- 성능 목표와 기능 요구 균형 필요
- Budget은 측정과 자동화가 있어야 효과 있음

---

### [FAQ]

Q. Performance Budget은 왜 필요한가?

A.
기능 추가로 Bundle과 리소스가 계속 커지는 것을 막고 성능 회귀를 조기에 발견하기 위해 필요하다.

Q. Bundle Budget은 어디에 적용하나?

A.
Initial Bundle과 Route Bundle에 적용하는 것이 일반적이다.

Q. Budget을 넘으면 무조건 배포하면 안 되나?

A.
상황에 따라 예외는 가능하지만 이유를 기록하고 후속 개선 계획을 세우는 것이 좋다.

---

# 24. Runtime Performance Rules

## 24.1 런타임 성능 최적화

### [개념]

Runtime Performance는 앱이 로드된 이후 사용자 입력, 스크롤, 애니메이션, 데이터 갱신, 상태 변경 중 발생하는 성능 문제를 개선하는 영역이다.

---

### [핵심]

필수 포함:

- Runtime Performance
- Input Responsiveness
- Scroll Performance
- Animation Performance
- Memory Usage
- Memory Leak
- Event Listener Cleanup
- Timer Cleanup
- Subscription Cleanup
- WebSocket Update
- Real-time Data
- Long-running Session

---

### [실무]

최적화 기준:

- 입력 이벤트 핸들러를 가볍게 유지
- 스크롤 이벤트는 throttle / passive listener 검토
- 애니메이션은 transform / opacity 우선
- setInterval / setTimeout cleanup 확인
- WebSocket / subscription cleanup 확인
- unmounted component state update 방지
- 큰 데이터 상태 누적 방지
- 오래 켜두는 대시보드 메모리 사용 확인
- 실시간 업데이트는 batch / throttle 검토
- React Profiler와 Memory 탭 함께 사용

주의:

- 초기 로딩이 빨라도 런타임이 느리면 UX가 나쁨
- 실시간 데이터는 렌더링 빈도를 제한해야 할 수 있음
- cleanup 누락은 memory leak 원인
- 무거운 애니메이션은 배터리와 CPU 사용 증가

---

### [FAQ]

Q. Runtime Performance는 무엇을 의미하나?

A.
앱이 열린 뒤 입력, 스크롤, 애니메이션, 실시간 업데이트, 상태 변경 중 발생하는 성능을 의미한다.

Q. Memory Leak은 왜 생기나?

A.
이벤트 리스너, 타이머, subscription, WebSocket 연결을 cleanup하지 않으면 발생할 수 있다.

Q. 실시간 데이터가 많으면 어떻게 최적화하나?

A.
업데이트 batch 처리, throttle, virtualization, 부분 렌더링, 서버 필터링을 검토한다.

---

# 25. Accessibility and Performance Rules

## 25.1 접근성과 성능 균형

### [개념]

Accessibility and Performance는 빠른 UI를 만들면서도 키보드, 스크린 리더, motion 민감 사용자, 저사양 환경 사용자를 배려하는 기준이다.

---

### [핵심]

필수 포함:

- Accessible Loading
- Focus Management
- Reduced Motion
- Skeleton Accessibility
- Live Region
- Keyboard Interaction
- Touch Target
- Color Contrast
- Lazy Loading Accessibility
- Infinite Scroll Accessibility

---

### [실무]

균형 기준:

- Loading 상태를 스크린 리더가 인식할 수 있게 처리
- Skeleton만 있고 텍스트 정보가 없으면 접근성 보완
- Infinite Scroll은 keyboard / screen reader 사용성 고려
- Reduced Motion 설정을 존중
- Lazy Loaded 콘텐츠의 focus 이동 주의
- 버튼 disabled 상태와 pending 상태 명확히 전달
- 이미지 lazy loading 시 alt 유지
- 성능 때문에 focus ring 제거 금지
- 애니메이션 최적화와 motion 접근성 함께 고려

---

### [FAQ]

Q. 성능을 위해 접근성을 포기해도 되나?

A.
안 된다. 성능과 접근성은 모두 사용자 경험의 핵심이다.

Q. Infinite Scroll은 접근성에 문제가 있나?

A.
문제가 될 수 있다. 키보드 탐색, 스크린 리더 안내, footer 접근, URL 복원성을 고려해야 한다.

Q. Skeleton UI도 접근성을 고려해야 하나?

A.
그렇다. 로딩 상태가 보조 기술 사용자에게도 전달되어야 한다.

---

# 26. Monitoring and Observability Rules

## 26.1 성능 모니터링

### [개념]

Performance Monitoring은 배포 후 실제 사용자 환경에서 성능 지표와 회귀를 지속적으로 관찰하는 체계이다.

---

### [핵심]

필수 포함:

- Real User Monitoring
- Synthetic Monitoring
- Web Vitals Reporting
- Performance Dashboard
- Error Monitoring
- Long Task Monitoring
- Resource Timing
- Navigation Timing
- Regression Alert
- Release Comparison
- Device / Network Segment

Monitoring Flow:

```text
Deploy
→ Collect Web Vitals
→ Segment by Page / Device / Network
→ Detect Regression
→ Investigate Cause
→ Fix and Verify
```

---

### [실무]

모니터링 기준:

- 페이지별 Core Web Vitals 수집
- 모바일 / 데스크톱 분리
- 네트워크 조건별 분리
- 배포 전후 성능 변화 비교
- 특정 Release 이후 regression 추적
- Error Monitoring과 성능 지표 연결
- Third-party Script 영향 추적
- 느린 사용자 구간 확인
- 성능 알림 기준 설정
- 성능 개선 결과를 지속 관찰

주의:

- Lab Test만으로 실제 사용자 성능을 판단하지 않기
- 평균값만 보면 느린 사용자 경험을 놓칠 수 있음
- 모니터링 데이터 수집 자체가 성능에 부담이 되지 않게 주의
- 개인정보 수집 정책 준수

---

### [FAQ]

Q. 성능 모니터링은 왜 필요한가?

A.
개발 환경 테스트와 실제 사용자 환경이 다르기 때문에 배포 후 성능 회귀를 지속적으로 확인해야 한다.

Q. RUM과 Synthetic Monitoring 차이는?

A.
RUM은 실제 사용자 데이터를 수집하고, Synthetic Monitoring은 정해진 환경에서 반복 측정한다.

Q. 평균 성능만 보면 충분한가?

A.
아니다. 느린 기기나 느린 네트워크 사용자 구간도 확인해야 한다.

---

# 27. Troubleshooting Rules

## 27.1 자주 발생하는 성능 문제

### [개념]

Troubleshooting 문서는 Agent가 성능 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- LCP Slow
- INP Poor
- CLS High
- Bundle Too Large
- Hydration Slow
- Request Waterfall
- Image Too Large
- Font Causes CLS
- Long Task
- Re-render Too Often
- Context Re-render
- Large List Slow
- Third-party Script Blocking
- Cache Stale Data
- Cache Miss
- Memory Leak
- Slow Route Transition
- Dev Fast Production Slow
- Production Fast Dev Slow

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

- LCP가 느림

원인:

- Hero Image 용량이 큼
- LCP 이미지가 lazy loading됨
- 서버 응답 시간이 느림
- 렌더링 차단 CSS / JS가 많음

해결:

- 이미지 크기와 포맷 최적화
- LCP 이미지 priority 또는 preload 적용
- 서버 / CDN cache 확인
- 초기 CSS / JS 줄이기
```

예시:

```md
문제:

- INP가 나쁨

원인:

- 이벤트 핸들러가 무거움
- Long Task가 메인 스레드를 점유
- 사용자 입력마다 큰 리스트가 다시 렌더링됨

해결:

- 이벤트 핸들러 단순화
- 작업 분할 또는 Web Worker 검토
- 리스트 virtualization 적용
- React Profiler로 re-render 원인 확인
```

예시:

```md
문제:

- Bundle Size가 너무 큼

원인:

- 큰 라이브러리가 initial bundle에 포함됨
- 사용하지 않는 코드가 제거되지 않음
- route별 code splitting이 부족함

해결:

- Bundle Analyzer 확인
- Dynamic Import 적용
- Tree Shaking 가능한 import로 변경
- 불필요한 dependency 제거
```

---

### [FAQ]

Q. LCP가 느리면 무엇을 확인해야 하나?

A.
Hero Image, 서버 응답, 렌더링 차단 CSS / JS, preload / priority 설정을 확인해야 한다.

Q. INP가 나쁘면 무엇을 확인해야 하나?

A.
Long Task, 이벤트 핸들러, 무거운 re-render, 큰 리스트 렌더링을 확인해야 한다.

Q. CLS가 높으면 무엇을 확인해야 하나?

A.
이미지 크기, 광고 / 배너 공간, 폰트 로딩, 동적 콘텐츠 삽입을 확인해야 한다.

---

# 28. Code Example Rules

## 28.1 코드 예제 작성 기준

### [개념]

Frontend Performance Tuning 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React / Next.js 기준 예제 우선
- 핵심 최적화만 포함
- 긴 전체 파일 금지
- 불필요한 import 최소화
- 측정 없이 최적화하는 예제 금지
- 안전한 fallback UI 포함 권장
- 접근성 훼손 금지
- 성능 개선 의도가 명확해야 함
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Dynamic Import
- React.lazy / Suspense
- Next.js Image
- Font Optimization
- Memoization
- Virtualized List
- Debounce Search
- Abort Request
- Parallel Fetching
- Cache Revalidation
- Performance Mark
- Bundle Analyzer Script
- Context Split
- Web Worker 기본 구조

금지 예제:

- 모든 컴포넌트에 `memo` 적용
- 모든 이미지에 priority 적용
- 모든 기능을 lazy loading
- 접근성 없는 skeleton / loading
- 사용자별 데이터를 public cache
- 거대한 utility 파일
- Third-party Script 전역 무분별 로드
- Hydration Error를 무조건 suppress
- API 요청 실패 무시

---

### [FAQ]

Q. 성능 최적화 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. `useMemo` 예제를 많이 넣어야 하나?

A.
무분별하게 넣지 않는다. 실제 계산 비용이나 참조 안정성이 필요한 상황으로 제한한다.

---

# 29. Comparison Rules

## 29.1 필수 비교 대상

### [개념]

Frontend Performance Tuning 문서는 Agent의 성능 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Lab Data vs Field Data
- Lighthouse vs RUM
- LCP vs FCP
- INP vs TTI
- Bundle Size vs JavaScript Execution Cost
- Code Splitting vs Lazy Loading
- Preload vs Prefetch
- SSR vs CSR
- Static Rendering vs Dynamic Rendering
- Server Component vs Client Component
- `React.memo` vs Component Split
- `useMemo` vs `useCallback`
- Pagination vs Virtualization
- Skeleton vs Spinner
- Debounce vs Throttle
- Browser Cache vs CDN Cache
- Public Cache vs Private Cache
- Lazy Image vs Priority Image
- System Font vs Web Font
- Local Monitoring vs Production Monitoring

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 개선 지표 / 장점 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Preload와 Prefetch는 어떻게 구분하나?

A.
Preload는 현재 페이지에서 곧 필요한 리소스에 사용하고, Prefetch는 다음 페이지에서 필요할 가능성이 높은 리소스에 사용한다.

Q. Pagination과 Virtualization 중 무엇을 써야 하나?

A.
관리형 목록과 SEO가 중요하면 Pagination, 한 화면에서 많은 항목을 부드럽게 보여줘야 하면 Virtualization을 고려한다.

Q. Lab Data와 Field Data 중 무엇이 더 중요한가?

A.
둘 다 중요하다. Lab Data는 재현 가능한 진단에 좋고 Field Data는 실제 사용자 경험을 보여준다.

---

# 30. Checklist Rules

## 30.1 문서 품질 체크리스트

### [개념]

Frontend Performance Tuning RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Performance Tuning 목적이 명확한가?
- [ ] Core Web Vitals 기준을 포함했는가?
- [ ] Measurement First 원칙을 포함했는가?
- [ ] Lighthouse / DevTools / React Profiler 기준을 포함했는가?
- [ ] Bundle Size 최적화 기준을 포함했는가?
- [ ] Code Splitting / Lazy Loading 기준을 포함했는가?
- [ ] JavaScript Execution Cost 기준을 포함했는가?
- [ ] Rendering Optimization 기준을 포함했는가?
- [ ] React Re-render Optimization 기준을 포함했는가?
- [ ] Context Performance 기준을 포함했는가?
- [ ] List Virtualization 기준을 포함했는가?
- [ ] Image Optimization 기준을 포함했는가?
- [ ] Font Optimization 기준을 포함했는가?
- [ ] CSS Performance 기준을 포함했는가?
- [ ] Network Optimization 기준을 포함했는가?
- [ ] Data Fetching Performance 기준을 포함했는가?
- [ ] Caching Strategy 기준을 포함했는가?
- [ ] Next.js App Router Performance 기준을 포함했는가?
- [ ] Hydration Optimization 기준을 포함했는가?
- [ ] Third-party Script 기준을 포함했는가?
- [ ] Performance Budget 기준을 포함했는가?
- [ ] Monitoring / Observability 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Next.js App Router / Advanced React Pattern / Frontend Architecture 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- App Router / React Pattern / Architecture / Observability 문서와 연계 가능해야 함

---

### [FAQ]

Q. Frontend Performance Tuning 문서 품질에서 가장 중요한 것은?

A.
측정 기준, Core Web Vitals, Bundle, Rendering, Image, Font, Network, Cache, Hydration, Monitoring 기준이 명확해야 한다.

---

# 31. Retrieval Optimization Rules

## 31.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Performance
- Frontend Performance Tuning
- Web Performance
- Core Web Vitals
- LCP
- INP
- CLS
- TTFB
- FCP
- Lighthouse
- Web Vitals
- RUM
- Synthetic Monitoring
- Browser DevTools
- React Profiler
- Bundle Analyzer
- Bundle Size
- Initial Bundle
- Code Splitting
- Lazy Loading
- Dynamic Import
- Tree Shaking
- JavaScript Execution Cost
- Long Task
- Main Thread
- Rendering Optimization
- Re-render Optimization
- React Performance
- Context Performance
- Virtualization
- Image Optimization
- Next Image
- Font Optimization
- CSS Performance
- Network Waterfall
- Preload
- Prefetch
- Preconnect
- Data Fetching Performance
- Request Waterfall
- Caching Strategy
- Cache Invalidation
- Next.js App Router Performance
- Hydration Cost
- Server Component
- Client Component
- Third-party Script
- Performance Budget
- Performance Monitoring

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- 프론트엔드 성능 최적화 뭐부터 해?
- Core Web Vitals는 뭐야?
- LCP가 느린 이유는?
- INP가 나쁜 이유는?
- CLS가 발생하는 이유는?
- Bundle Size 줄이는 방법은?
- React re-render 왜 많이 발생해?
- useMemo는 언제 써?
- Context 때문에 느려졌어
- 리스트가 너무 느려
- 이미지 최적화 어떻게 해?
- 웹 폰트 때문에 느려?
- Network Waterfall은 어떻게 봐?
- preload와 prefetch 차이는?
- API 요청이 느릴 때 프론트에서 뭘 할 수 있어?
- Cache 때문에 데이터가 안 바뀌어
- Next.js App Router 성능 최적화는?
- Hydration Cost 줄이는 방법은?
- use client가 많으면 왜 느려?
- Third-party Script가 느리게 해?
- Performance Budget은 왜 필요해?
- 성능 모니터링은 어떻게 해?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 32. Version Rules

## 32.1 기준 버전

### [개념]

Frontend Performance Tuning 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern Frontend
- Core Web Vitals
- React 19+
- Next.js App Router
- TypeScript
- Server Component
- Client Component
- Streaming
- Suspense
- Modern Image Format
- Modern Font Loading
- Modern Browser DevTools
- Performance Monitoring
- Bundle Analyzer
- RUM
- Performance Budget

Legacy 제외:

- jQuery 중심 성능 최적화
- Class Component 중심 React 최적화
- 측정 없는 추측 기반 최적화
- 모든 상태를 전역 Store에 넣는 구조
- 모든 컴포넌트에 `memo` 적용하는 방식
- 모든 이미지를 lazy loading하는 방식
- 모든 리소스를 preload하는 방식
- 접근성을 희생하는 성능 최적화
- Secret이 포함된 성능 로그

---

### [실무]

문서 작성 시 주의:

- Next.js App Router의 Server / Client Component 경계와 충돌하지 않게 작성
- Advanced React Pattern의 Hook 상세와 중복 최소화
- Frontend Architecture의 구조 기준과 연계
- Design System의 Token / Component / Accessibility 기준과 연계
- Observability 문서와 Monitoring 상세 중복 최소화
- 성능 최적화는 프로젝트 규모와 사용자 환경에 따라 우선순위가 달라짐
- 최신 브라우저 / 프레임워크 동작 변화 가능성을 고려

---

### [FAQ]

Q. Frontend Performance 문서는 React 19 기준이어야 하나?

A.
Modern React 기준으로 작성하고, React 19 이후의 Transition, Actions, Server Component 연계를 고려하는 것이 좋다.

Q. Next.js 성능 문서와 중복되면 안 되나?

A.
중복을 최소화해야 한다. 이 문서는 성능 관점에서 App Router, Hydration, Cache, Image, Font 기준을 다룬다.

---

# 33. Common Mistakes

## 33.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 성능 코드 리뷰와 병목 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- 측정 없이 `useMemo`부터 적용
- Lighthouse 점수만 보고 실제 사용자 지표 무시
- Initial Bundle에 큰 라이브러리 포함
- 모든 컴포넌트를 Client Component로 작성
- Page 전체에 `use client` 선언
- 모든 이미지를 lazy loading
- LCP 이미지에 lazy loading 적용
- 이미지 width / height 누락
- 웹 폰트 weight 과다 로드
- 모든 리소스를 preload
- Third-party Script 전역 로드
- 독립 API 요청을 순차 실행
- 중복 API 요청 방치
- Cache Invalidation 누락
- 사용자별 데이터를 public cache
- Context에 자주 바뀌는 큰 상태 저장
- Provider value를 매번 새 객체로 생성
- 큰 리스트를 모두 렌더링
- index를 list key로 남용
- Scroll 이벤트에 throttle 없음
- 타이머 / 이벤트 리스너 cleanup 누락
- Hydration Error를 원인 분석 없이 suppress
- 성능 개선 후 재측정하지 않음

---

### [실무]

리뷰 기준:

- Core Web Vitals 확인
- Production Build 기준 측정 여부 확인
- Bundle Analyzer 확인
- Initial JS 크기 확인
- 큰 dependency 추가 여부 확인
- Image / Font 최적화 확인
- Network Waterfall 확인
- Request 병렬화 확인
- Cache 정책 확인
- Client Component 범위 확인
- Hydration Cost 확인
- React Profiler로 re-render 확인
- Context Provider 범위 확인
- Large List 처리 확인
- Third-party Script 로딩 전략 확인
- Performance Budget 초과 여부 확인

---

### [FAQ]

Q. Frontend Performance에서 가장 흔한 실수는?

A.
측정 없이 최적화하거나, Bundle / Image / Network 문제를 보지 않고 React memoization만 적용하는 것이다.

Q. 모든 이미지를 lazy loading하면 왜 문제인가?

A.
첫 화면 LCP 이미지까지 lazy loading되면 가장 중요한 콘텐츠 표시가 늦어질 수 있다.

Q. 모든 컴포넌트에 `memo`를 붙이면 좋은가?

A.
아니다. 실제 병목이 없으면 복잡도만 늘고 dependency 문제나 stale value 버그가 생길 수 있다.

---

# 34. Final Goal

## 34.1 최종 목표

### [개념]

Frontend Performance Tuning RAG 문서는 Agent가 프론트엔드 성능 병목을 측정, 진단, 개선, 검증, 모니터링할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Core Web Vitals 기준 성능 진단
- Lighthouse / DevTools 결과 해석
- Bundle Analyzer 결과 리뷰
- Bundle Size 최적화 제안
- Code Splitting / Lazy Loading 판단
- JavaScript Long Task 원인 분석
- React Re-render 원인 분석
- Context Performance 문제 진단
- Large List Virtualization 판단
- Image Optimization 제안
- Font Optimization 제안
- CSS Performance 리뷰
- Network Waterfall 분석
- Data Fetching 병렬화 제안
- Cache Strategy 검토
- Next.js App Router 성능 리뷰
- Hydration Cost 감소 제안
- Third-party Script 영향 분석
- Performance Budget 제안
- Monitoring / RUM 기준 제안
- 성능 문제 Troubleshooting
- Frontend Performance 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- 측정 → 개선 → 재측정 Flow 명확화
- Core Web Vitals / Bundle / Rendering / Network / Cache / Hydration 기준 포함
- Next.js App Router / Advanced React Pattern / Frontend Architecture 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Performance Tuning Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 성능을 측정하고 Bundle, Rendering, Image, Font, Network, Cache, React, Next.js, Hydration 병목을 진단하고 개선하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Performance Tuning 문서는 어떤 기준으로 작성해야 해?

A.
Core Web Vitals, 측정 도구, Bundle, Rendering, Image, Font, Network, Data Fetching, Cache, React, Next.js, Hydration 중심으로 작성해야 한다.

Q. 프론트엔드 성능 최적화 뭐부터 해?

A.
먼저 Core Web Vitals, Lighthouse, DevTools, RUM 데이터로 병목을 측정하고 가장 영향이 큰 문제부터 개선한다.

Q. Core Web Vitals는 뭐야?

A.
사용자 체감 성능을 측정하는 핵심 지표로 LCP, INP, CLS가 대표적이다.

Q. LCP는 무엇을 의미해?

A.
가장 큰 콘텐츠가 화면에 표시되는 시간을 의미하며 로딩 속도와 관련이 깊다.

Q. INP는 무엇을 의미해?

A.
사용자 상호작용에 대한 응답성을 나타내며 긴 JavaScript 작업이나 무거운 렌더링이 영향을 준다.

Q. CLS는 무엇을 의미해?

A.
화면 레이아웃이 예기치 않게 움직이는 정도를 나타내는 지표이다.

Q. LCP가 느린 이유는?

A.
Hero Image 용량, 서버 응답, 렌더링 차단 CSS / JS, preload 누락이 주요 원인이다.

Q. INP가 나쁜 이유는?

A.
Long Task, 무거운 이벤트 핸들러, 큰 리스트 re-render, 메인 스레드 blocking 작업이 원인일 수 있다.

Q. CLS가 발생하는 이유는?

A.
이미지 크기 누락, 광고 / 배너 삽입, 폰트 로딩, 동적 콘텐츠 공간 미확보가 원인일 수 있다.

Q. Lighthouse 점수만 보면 돼?

A.
아니다. Lighthouse는 Lab Data이므로 실제 사용자 RUM 데이터와 함께 봐야 한다.

Q. 성능 병목은 어떻게 찾어?

A.
DevTools Network, Performance 패널, React Profiler, Bundle Analyzer를 사용해 Network, JavaScript, Rendering 병목을 분리한다.

Q. Production Build로 측정해야 해?

A.
그렇다. 개발 환경은 dev overlay, source map, HMR 등으로 실제 성능과 다를 수 있다.

Q. Bundle Size 줄이는 방법은?

A.
큰 dependency 제거, dynamic import, code splitting, tree shaking 가능한 import, dead code 제거, 중복 dependency 정리를 적용한다.

Q. Bundle Size가 크면 왜 느려져?

A.
다운로드뿐 아니라 JavaScript 파싱, 컴파일, 실행 비용이 증가하기 때문이다.

Q. Bundle Analyzer로 무엇을 봐?

A.
Initial Bundle, 큰 dependency, 중복 dependency, 예상보다 큰 shared chunk를 확인한다.

Q. Code Splitting은 언제 해?

A.
초기 화면에 필요 없는 큰 기능이나 특정 라우트에서만 사용하는 코드를 분리할 때 사용한다.

Q. Lazy Loading은 언제 해?

A.
차트, 에디터, 지도, 모달 내부 무거운 기능처럼 처음부터 필요하지 않은 기능에 적용한다.

Q. 모든 컴포넌트를 lazy loading하면 좋아?

A.
아니다. 핵심 UI까지 lazy loading하면 사용자 체감 속도가 나빠질 수 있다.

Q. JavaScript 실행 비용은 왜 중요해?

A.
JavaScript가 다운로드된 뒤에도 파싱, 컴파일, 실행 시간이 길면 화면과 상호작용이 느려진다.

Q. Long Task는 무엇이야?

A.
메인 스레드를 오래 점유해 렌더링과 사용자 입력 처리를 지연시키는 작업이다.

Q. 무거운 계산은 어떻게 최적화해?

A.
memoization, task splitting, Web Worker, 서버 계산 이전을 검토한다.

Q. React re-render 왜 많이 발생해?

A.
state 변경, props 변경, parent re-render, context value 변경, key 변경 때문에 발생한다.

Q. React re-render는 무조건 나빠?

A.
아니다. 비용이 큰 re-render가 자주 발생할 때 문제가 된다.

Q. React 성능 최적화는 무엇부터 해?

A.
State 위치, Component Split, Context 범위, 큰 리스트, Profiler 결과를 먼저 확인한다.

Q. useMemo는 언제 써?

A.
계산 비용이 크거나 memoized child에 안정적인 값을 전달해야 할 때 사용한다.

Q. useCallback은 언제 써?

A.
함수 참조 안정성이 필요하거나 memoized child에 callback을 전달할 때 사용한다.

Q. 모든 컴포넌트에 memo 붙여도 돼?

A.
권장하지 않는다. 실제 병목이 확인된 비용 큰 컴포넌트에 제한적으로 적용한다.

Q. Context 때문에 느려졌어. 무엇을 봐?

A.
Provider value 변경 빈도, Provider 범위, Context Split, value memoization, 소비 컴포넌트 수를 확인한다.

Q. Context re-render는 어떻게 줄여?

A.
Provider 범위를 줄이고, 자주 바뀌는 값과 안정적인 값을 분리하고, 필요한 경우 External Store를 검토한다.

Q. 리스트가 너무 느려. 어떻게 해?

A.
항목 수, item 렌더링 비용, key 안정성, pagination, virtualization 적용 가능성을 확인한다.

Q. Virtualization은 언제 써?

A.
수백 개 이상의 항목처럼 화면 밖 항목까지 모두 렌더링해 성능 문제가 발생할 때 사용한다.

Q. index를 key로 써도 돼?

A.
정렬, 삽입, 삭제가 있는 리스트에서는 상태 꼬임과 렌더링 문제가 생길 수 있어 피하는 것이 좋다.

Q. 이미지 최적화 어떻게 해?

A.
실제 표시 크기에 맞는 이미지, WebP / AVIF, width / height 지정, lazy loading, LCP 이미지 priority를 적용한다.

Q. 모든 이미지를 lazy loading하면 돼?

A.
아니다. 첫 화면 LCP 이미지는 lazy loading하면 오히려 느려질 수 있다.

Q. 이미지 width와 height는 왜 필요해?

A.
브라우저가 이미지 공간을 미리 확보해 CLS를 줄일 수 있기 때문이다.

Q. 웹 폰트 때문에 느려?

A.
그럴 수 있다. 폰트 다운로드, 교체, weight 과다 로드가 FCP, LCP, CLS에 영향을 준다.

Q. 폰트 최적화는 어떻게 해?

A.
필요한 weight만 로드하고, subset, font-display, preload, system font, Next Font를 검토한다.

Q. 모든 폰트를 preload하면 좋아?

A.
아니다. 중요한 폰트만 preload해야 하며 과도한 preload는 네트워크 경쟁을 만든다.

Q. CSS도 성능 병목이 돼?

A.
그렇다. 렌더링 차단 CSS, 사용하지 않는 대용량 CSS, 복잡한 selector가 렌더링을 늦출 수 있다.

Q. Critical CSS는 뭐야?

A.
첫 화면 렌더링에 필요한 최소 CSS를 우선 제공하는 전략이다.

Q. Runtime CSS-in-JS는 왜 주의해야 해?

A.
런타임 스타일 생성이 JavaScript 실행과 hydration 비용을 증가시킬 수 있기 때문이다.

Q. Network Waterfall은 어떻게 봐?

A.
느린 요청, 순차 요청, blocking 리소스, 큰 파일, 중복 요청, 외부 스크립트를 확인한다.

Q. preload와 prefetch 차이는?

A.
preload는 현재 페이지에 곧 필요한 리소스 우선 로딩이고, prefetch는 다음에 필요할 가능성이 있는 리소스 사전 로딩이다.

Q. preconnect는 언제 써?

A.
외부 도메인 리소스를 곧 요청해야 할 때 연결 설정 비용을 줄이기 위해 사용한다.

Q. Third-party Script가 느리게 해?

A.
그럴 수 있다. 외부 스크립트가 네트워크와 메인 스레드를 점유해 LCP와 INP를 악화시킬 수 있다.

Q. 지도 SDK는 어디서 로드해?

A.
지도 기능이 필요한 페이지나 컴포넌트에서만 지연 로딩하는 것이 좋다.

Q. API 요청이 느릴 때 프론트에서 뭘 할 수 있어?

A.
요청 병렬화, 중복 요청 제거, 캐싱, pagination, prefetch, 응답 크기 축소, loading UI 개선을 할 수 있다.

Q. Request Waterfall은 왜 문제야?

A.
독립적인 요청이 순차 실행되면 전체 대기 시간이 길어져 초기 렌더링이 늦어진다.

Q. 검색 API는 어떻게 최적화해?

A.
debounce, abort, cache, URL State, pagination을 함께 고려한다.

Q. Cache는 무조건 많이 쓰면 좋아?

A.
아니다. 데이터 신선도, 사용자별 보안, invalidation 전략이 없으면 오래된 데이터나 정보 노출 문제가 생길 수 있다.

Q. 사용자별 데이터는 캐시해도 돼?

A.
public cache는 금지하고 private cache 또는 no-store를 고려해야 한다.

Q. Cache 때문에 데이터가 안 바뀌어. 무엇을 봐?

A.
Cache Key, Invalidation, Revalidation, Router Refresh, stale time 설정을 확인해야 한다.

Q. Next.js App Router 성능 최적화는?

A.
Server Component를 기본으로 사용하고 Client Component 범위, Hydration Cost, Fetch Cache, Streaming, Image / Font 최적화를 점검한다.

Q. use client가 많으면 왜 느려?

A.
브라우저로 전송되는 JavaScript와 Hydration 비용이 증가하기 때문이다.

Q. Hydration Cost 줄이는 방법은?

A.
Client Component 범위를 줄이고 상호작용 없는 UI를 Server Component로 유지하며 무거운 클라이언트 코드를 지연 로딩한다.

Q. Hydration Error는 왜 발생해?

A.
서버에서 렌더링한 결과와 클라이언트에서 렌더링한 결과가 다를 때 발생한다.

Q. App Router에서 느린 데이터는 어떻게 처리해?

A.
Suspense, Streaming, `loading.tsx`, 병렬 Fetch, Cache / Revalidation을 고려한다.

Q. Performance Budget은 왜 필요해?

A.
기능 추가로 Bundle과 리소스가 계속 커지는 것을 막고 성능 회귀를 조기에 발견하기 위해 필요하다.

Q. Bundle Budget은 어디에 적용해?

A.
Initial Bundle과 Route Bundle에 적용하는 것이 일반적이다.

Q. Runtime Performance는 뭐야?

A.
앱이 열린 뒤 입력, 스크롤, 애니메이션, 실시간 업데이트, 상태 변경 중 발생하는 성능이다.

Q. Memory Leak은 왜 생겨?

A.
이벤트 리스너, 타이머, subscription, WebSocket 연결을 cleanup하지 않으면 발생할 수 있다.

Q. 실시간 데이터가 많으면 어떻게 최적화해?

A.
업데이트 batch 처리, throttle, virtualization, 부분 렌더링, 서버 필터링을 검토한다.

Q. 성능을 위해 접근성을 포기해도 돼?

A.
안 된다. 성능과 접근성은 모두 사용자 경험의 핵심이다.

Q. Infinite Scroll은 접근성 문제가 있어?

A.
문제가 될 수 있다. 키보드 탐색, 스크린 리더 안내, footer 접근, URL 복원성을 고려해야 한다.

Q. 성능 모니터링은 어떻게 해?

A.
RUM, Synthetic Monitoring, Web Vitals Reporting, Release Comparison, Regression Alert를 사용한다.

Q. RUM과 Synthetic Monitoring 차이는?

A.
RUM은 실제 사용자 데이터를 수집하고, Synthetic Monitoring은 정해진 환경에서 반복 측정한다.

Q. 평균 성능만 보면 충분해?

A.
아니다. 느린 기기나 느린 네트워크 사용자 구간도 확인해야 한다.

Q. Frontend Performance 코드 리뷰에서 가장 중요한 것은?

A.
측정 여부, Core Web Vitals, Bundle Size, Image / Font, Network, Cache, Client Component 범위, Hydration Cost, Re-render 원인을 확인하는 것이다.

Q. Frontend Performance Tuning RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 성능을 측정하고 Bundle, Rendering, Image, Font, Network, Cache, React, Next.js, Hydration 병목을 진단하고 개선하게 만드는 것이다.
