# Frontend Observability Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Observability Domain 목적

### [개념]

Frontend Observability Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent / DevOps Agent용 RAG 문서 제작 규칙이다.

Frontend Observability는 사용자의 브라우저 환경에서 발생하는 Error, Performance, User Interaction, Network Request, Web Vitals, Session, Release Regression을 수집하고 분석하여 실제 사용자 경험을 추적하는 영역이다.

목적:

- 프론트엔드 장애 원인 분석 지원
- 사용자 환경 기반 Error Monitoring 지원
- Core Web Vitals / Performance Monitoring 지원
- API Request / Network Error 추적 지원
- User Interaction / Breadcrumb 추적 지원
- Session Replay 적용 기준 제공
- Source Map 기반 오류 추적 지원
- Release Regression 감지 지원
- Logging / Metrics / Tracing / Alerting 설계 지원
- Privacy / Security 기준 적용 지원
- Next.js / React 환경 Observability 설계 지원
- Frontend 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Error Monitoring
2. Performance Monitoring
3. Web Vitals Monitoring
4. Real User Monitoring
5. Logging
6. Metrics
7. Tracing
8. Breadcrumb
9. Network Request Tracking
10. Session Replay
11. Source Map Management
12. Release Tracking
13. Alerting
14. Dashboard
15. Privacy / PII Masking
16. Observability Sampling
17. Frontend Observability Architecture
18. Next.js / React Integration
19. Troubleshooting
20. Code Review Criteria

---

### [실무]

2026 실무 기준:

- 실제 사용자 환경 기반 RUM 중심으로 작성
- Lighthouse 같은 Lab Data와 RUM Field Data를 구분
- Error Monitoring과 Performance Monitoring을 함께 설계
- 단순 console log가 아니라 구조화된 event / context / metadata를 수집
- Source Map 업로드와 보안 정책 포함
- Release version / commit hash / environment를 모든 이벤트에 연결
- API Error와 UI Error를 구분
- User ID는 직접 식별 정보 대신 내부 식별자 또는 해시 사용 검토
- PII / Token / Secret / 개인정보 수집 금지 또는 masking
- Sampling 전략 포함
- Alert fatigue 방지를 위해 alert 기준 명확화
- Next.js App Router의 Server / Client boundary를 고려
- React Error Boundary와 Observability 도구 연계
- Agent가 장애 분석과 코드 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Observability 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 앱에서 Error, Performance, Web Vitals, API 실패, User Interaction, Release Regression을 추적하고 분석하도록 돕는 RAG 문서 제작 규칙이다.

Q. Frontend Observability는 console log를 많이 찍는 것인가?

A.
아니다. 실제 사용자 환경에서 발생한 오류, 성능, 네트워크, 상호작용, release 정보를 구조적으로 수집하고 분석하는 체계이다.

Q. Frontend Observability는 DevOps 영역인가 Frontend 영역인가?

A.
둘 다 연결된다. 브라우저에서 발생하는 데이터를 프론트엔드가 수집하고, DevOps / Observability 체계에서 분석한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Observability Domain은 브라우저 환경에서 발생하는 장애와 성능 문제를 재현, 추적, 분석하기 위한 기준을 포함한다.

---

### [핵심]

포함 범위:

- Frontend Observability
- Error Monitoring
- Runtime Error
- React Error Boundary
- Unhandled Error
- Unhandled Promise Rejection
- API Error
- Network Error
- Performance Monitoring
- Real User Monitoring
- Core Web Vitals
- LCP
- INP
- CLS
- TTFB
- FCP
- Resource Timing
- Navigation Timing
- Long Task
- User Timing
- Custom Metric
- Logging
- Structured Log
- Breadcrumb
- User Action Tracking
- Session Replay
- Source Map
- Release Tracking
- Environment Tracking
- Trace ID
- Correlation ID
- Distributed Tracing
- Frontend Metrics
- Alerting
- Dashboard
- Sampling
- PII Masking
- Privacy
- Consent
- Observability SDK
- Next.js Observability
- React Observability
- WebSocket Monitoring
- Third-party Script Monitoring
- Synthetic Monitoring
- RUM

---

### [실무]

제외 범위:

- Backend Observability 심화
- Kubernetes Observability 심화
- Prometheus / Grafana 운영 심화
- OpenTelemetry Collector 운영 심화
- APM 서버 구축 심화
- 로그 수집 파이프라인 인프라 심화
- SIEM / 보안 관제 심화
- Browser Engine 내부 구현 심화
- 프론트엔드 성능 최적화 전체
- Next.js App Router 전체 기능 설명

단, Frontend Observability 설계에 필요한 수준의 Monitoring, Metrics, Tracing, Logging, Performance, Security, Privacy 지식은 포함 가능하다.

---

### [FAQ]

Q. Frontend Observability 문서에 Backend Tracing도 포함해야 하나?

A.
심화는 제외한다. 단, 프론트엔드 요청과 백엔드 로그를 연결하기 위한 trace id / correlation id 개념은 포함한다.

Q. Performance Tuning 문서와 중복되지 않나?

A.
이 Domain은 성능 개선 방법보다 성능 문제를 수집, 측정, 감지, 분석하는 Observability 체계에 집중한다.

Q. Security 문서와 중복되지 않나?

A.
중복을 최소화한다. 이 문서는 로그와 Session Replay에 개인정보가 섞이지 않도록 masking / consent / retention 기준을 포함한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Observability RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

Frontend Observability 문서는 수집 흐름과 분석 흐름이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Error 발생 → Context 수집 → 전송 → Grouping → Alert → Debug
- `[Comparison]`: Logging vs Metrics vs Tracing, RUM vs Synthetic
- `[Best Practice]`: PII masking, release tagging, source map 관리
- `[Troubleshooting]`: source map 누락, alert 과다, session replay 개인정보 노출
- `[Checklist]`: 배포 전 Observability 점검

---

### [FAQ]

Q. Frontend Observability 문서에 Flow가 필요한 이유는?

A.
오류나 성능 문제가 브라우저에서 발생한 뒤 수집, 전송, 집계, 알림, 분석까지 이어지는 흐름을 Agent가 판단해야 하기 때문이다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Observability Core Concept Rules

## 4.1 Frontend Observability 기본 개념

### [개념]

Frontend Observability는 프론트엔드 앱 내부 상태를 외부에서 관찰할 수 있도록 Error, Log, Metric, Trace, User Session, Performance Event를 수집하는 체계이다.

핵심 질문:

- 어떤 오류가 발생했는가?
- 어떤 사용자 환경에서 발생했는가?
- 어느 release 이후 발생했는가?
- 사용자는 어떤 행동을 했는가?
- 어떤 API 요청이 실패했는가?
- 성능 지표가 어느 페이지에서 나빠졌는가?
- 문제가 특정 브라우저 / 기기 / 지역 / 네트워크에 집중되는가?
- 재현 가능한 정보가 충분한가?

---

### [핵심]

Observability 3요소:

- Logs
- Metrics
- Traces

Frontend 확장 요소:

- Error Event
- Breadcrumb
- Session Replay
- Web Vitals
- User Interaction
- Resource Timing
- Network Error
- Release Metadata
- Environment Metadata

기본 Flow:

```text
User Browser
→ Error / Metric / Interaction 발생
→ Observability SDK 수집
→ Context / Metadata 추가
→ Sampling / Masking
→ Observability Backend 전송
→ Grouping / Dashboard / Alert
→ Debug / Fix / Release
```

---

### [실무]

Frontend Observability 핵심 기준:

- 모든 이벤트에 release / environment / route / user context를 연결
- 오류는 stack trace와 source map으로 원본 코드 위치 추적
- 성능은 page route와 device / browser / network 기준으로 분리
- API 실패는 status code / endpoint / latency / correlation id 수집
- Breadcrumb으로 오류 직전 사용자 행동 기록
- Session Replay는 개인정보 masking 전제
- Alert는 사용자 영향도 기준으로 설계
- 로그 수집량과 비용을 고려해 sampling 적용
- 수집 자체가 성능 병목이 되지 않도록 주의

---

### [FAQ]

Q. Frontend Observability에서 가장 중요한 것은?

A.
오류나 성능 문제가 발생했을 때 사용자 환경, release, route, action, API 요청, stack trace를 함께 확인할 수 있어야 한다.

Q. Observability와 Monitoring 차이는?

A.
Monitoring은 정해진 지표를 감시하는 것에 가깝고, Observability는 수집된 데이터로 예상하지 못한 문제의 원인까지 추론할 수 있게 만드는 체계이다.

Q. Frontend Observability가 없으면 어떤 문제가 생기나?

A.
사용자 브라우저에서만 발생하는 오류, 특정 기기 성능 저하, 배포 후 회귀 문제를 재현하기 어렵다.

---

# 5. Error Monitoring Rules

## 5.1 Error Monitoring 기준

### [개념]

Error Monitoring은 브라우저에서 발생한 JavaScript Runtime Error, React Rendering Error, Promise Rejection, API Error를 수집하고 분석하는 체계이다.

---

### [핵심]

수집 대상:

- Runtime Error
- Syntax Error
- Type Error
- Reference Error
- React Error Boundary Error
- Unhandled Promise Rejection
- API Error
- Network Error
- Chunk Load Error
- Hydration Error
- Third-party Script Error
- WebSocket Error
- Permission Error

필수 metadata:

- Error message
- Stack trace
- Source map resolved location
- Release version
- Environment
- Route / URL
- Browser
- OS
- Device
- User context
- Breadcrumb
- API request context

---

### [실무]

Error Monitoring 작성 기준:

- React Error Boundary와 error reporter 연계
- 전역 error handler와 unhandled rejection handler 구성
- API client에서 error normalization 수행
- Chunk load failure 별도 분류
- Hydration Error는 route / component boundary 정보 포함
- Error grouping 기준 확인
- noise error는 filtering 적용
- 사용자 영향도가 큰 error는 alert 연결
- Error 발생 시 사용자에게 fallback UI 제공
- 민감한 error detail은 사용자 화면에 노출 금지

예시:

```tsx
function reportError(error: unknown, context: Record<string, unknown>) {
  observability.captureException(error, {
    tags: {
      source: "frontend",
    },
    extra: context,
  });
}
```

---

### [FAQ]

Q. 프론트엔드에서 어떤 오류를 수집해야 하나?

A.
Runtime Error, React Error Boundary Error, Unhandled Promise Rejection, API Error, Network Error, Chunk Load Error, Hydration Error를 수집해야 한다.

Q. Error Boundary만 있으면 모든 오류를 잡을 수 있나?

A.
아니다. Error Boundary는 렌더링 중 오류를 잡지만 이벤트 핸들러, 비동기 callback, Promise rejection은 별도 처리해야 한다.

Q. Error Monitoring에서 release 정보가 왜 중요한가?

A.
특정 배포 이후 오류가 증가했는지 확인하고 rollback 또는 hotfix 판단을 하기 위해 필요하다.

---

# 6. React Error Boundary Rules

## 6.1 React Error Boundary 연계

### [개념]

React Error Boundary는 하위 컴포넌트 렌더링 중 발생한 오류를 격리하고 fallback UI를 제공하는 React 패턴이다.

Frontend Observability에서는 Error Boundary가 단순 fallback UI만 제공하는 것이 아니라 error reporting과 연결되어야 한다.

---

### [핵심]

필수 포함:

- React Error Boundary
- Fallback UI
- Error Reporting
- Component Stack
- Reset
- Retry
- Segment Boundary
- Route Boundary
- User Feedback
- Error Isolation

---

### [실무]

작성 기준:

- Error Boundary에서 error reporter 호출
- component stack / route / feature 정보를 함께 수집
- fallback UI는 사용자에게 복구 가능성을 제공
- retry / reset 동작 제공
- 전체 앱을 죽이지 않고 segment 단위로 오류 격리
- Next.js App Router의 `error.tsx`와 연계
- Error Boundary가 잡지 못하는 async error는 별도 수집
- 에러 상세를 사용자에게 직접 노출하지 않음

예시:

```tsx
"use client";

export default function ErrorFallback({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  React.useEffect(() => {
    reportError(error, {
      boundary: "route-error",
    });
  }, [error]);

  return (
    <section>
      <p>문제가 발생했습니다.</p>
      <button onClick={reset}>다시 시도</button>
    </section>
  );
}
```

---

### [FAQ]

Q. Error Boundary에서 Observability 도구를 호출해야 하나?

A.
그렇다. fallback UI만 보여주면 개발자가 오류를 모를 수 있으므로 error reporting과 연결해야 한다.

Q. Error Boundary는 어디에 두는 것이 좋나?

A.
전체 앱 최상단과 주요 route / feature boundary에 배치해 오류를 적절히 격리하는 것이 좋다.

Q. 사용자에게 stack trace를 보여줘도 되나?

A.
안 된다. 사용자에게는 안전한 메시지를 보여주고 stack trace는 Observability 도구에만 전송한다.

---

# 7. API Error and Network Monitoring Rules

## 7.1 API / Network Error 추적

### [개념]

API Error and Network Monitoring은 프론트엔드에서 발생한 HTTP 실패, timeout, retry, latency, aborted request, CORS error, authentication error를 수집하는 체계이다.

---

### [핵심]

수집 대상:

- HTTP Status Code
- Endpoint
- Method
- Latency
- Timeout
- Retry Count
- Network Error
- CORS Error
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 429 Rate Limit
- 500 Server Error
- Aborted Request
- Correlation ID
- Trace ID

API Error Flow:

```text
Request Start
→ Attach Trace ID
→ Response or Error
→ Normalize Error
→ Record Metric / Log
→ Show UI Error
→ Alert if Needed
```

---

### [실무]

작성 기준:

- API client에서 요청 / 응답 / 실패를 공통 처리
- endpoint path와 status code 수집
- query parameter / body에 개인정보가 있으면 masking
- 401 / 403 / 500 에러를 구분
- latency metric 수집
- timeout과 aborted request를 구분
- retry count 기록
- backend log와 연결할 correlation id 사용
- API 실패가 UI에 어떤 영향을 줬는지 context 포함
- 같은 에러를 중복 report하지 않도록 주의

예시:

```ts
type ApiErrorLog = {
  endpoint: string;
  method: string;
  status?: number;
  latencyMs: number;
  traceId?: string;
  errorType: "network" | "timeout" | "server" | "client";
};
```

---

### [FAQ]

Q. API Error Monitoring에서 무엇을 수집해야 하나?

A.
endpoint, method, status code, latency, timeout 여부, retry count, trace id, 사용자 route context를 수집해야 한다.

Q. API 요청 body를 그대로 로그로 남겨도 되나?

A.
안 된다. 개인정보, token, password, 결제 정보가 포함될 수 있으므로 masking하거나 수집하지 않아야 한다.

Q. 401과 403은 어떻게 다르게 추적하나?

A.
401은 인증 실패 / 세션 만료, 403은 권한 부족으로 분류해 별도 metric과 alert 기준을 둔다.

---

# 8. Performance Monitoring Rules

## 8.1 Performance Monitoring 기준

### [개념]

Performance Monitoring은 실제 사용자 환경에서 페이지 로딩, 리소스 로딩, JavaScript 실행, interaction latency, rendering delay를 측정하는 체계이다.

---

### [핵심]

수집 대상:

- Page Load Time
- Route Transition Time
- Resource Timing
- Navigation Timing
- Long Task
- JavaScript Execution Time
- API Latency
- Render Duration
- Hydration Time
- Interaction Latency
- Memory Usage
- CPU Pressure
- Network Type
- Device Memory
- Browser / OS

---

### [실무]

작성 기준:

- route별 성능 지표 수집
- device / browser / network 조건별 분리
- release별 성능 회귀 추적
- Long Task 수집
- 특정 route transition 지연 측정
- API latency와 화면 rendering latency 구분
- React Profiler 데이터는 개발 / 분석 용도로 활용
- 성능 수집 SDK 자체가 과도한 overhead를 만들지 않게 주의
- 샘플링 적용 가능
- Core Web Vitals와 custom metric을 함께 수집

---

### [FAQ]

Q. Performance Monitoring은 Lighthouse와 같은가?

A.
아니다. Lighthouse는 실험실 측정에 가깝고, Performance Monitoring은 실제 사용자 환경의 데이터를 지속 수집하는 것이다.

Q. 프론트엔드 성능 지표는 route별로 봐야 하나?

A.
그렇다. 페이지마다 병목이 다르므로 route / feature / device 기준으로 분리해야 한다.

Q. 성능 데이터 수집이 성능에 영향을 줄 수 있나?

A.
그렇다. SDK와 수집 코드가 과도하면 오히려 성능에 영향을 줄 수 있으므로 sampling과 최소 수집이 필요하다.

---

# 9. Web Vitals Monitoring Rules

## 9.1 Core Web Vitals 수집 기준

### [개념]

Web Vitals Monitoring은 LCP, INP, CLS, TTFB, FCP 같은 사용자 중심 성능 지표를 실제 사용자 환경에서 수집하는 체계이다.

---

### [핵심]

필수 포함:

- LCP
- INP
- CLS
- TTFB
- FCP
- Web Vitals
- Route
- Device
- Browser
- Network
- Percentile
- p75
- Field Data
- Regression
- Attribution

지표 기준:

| 지표 | 의미                | 수집 목적            |
| ---- | ------------------- | -------------------- |
| LCP  | 가장 큰 콘텐츠 표시 | 로딩 성능            |
| INP  | 상호작용 응답성     | 입력 반응성          |
| CLS  | 레이아웃 이동       | 시각 안정성          |
| TTFB | 첫 응답 시간        | 서버 / 네트워크 응답 |
| FCP  | 첫 콘텐츠 표시      | 초기 렌더링          |

---

### [실무]

작성 기준:

- 평균보다 p75 기준을 우선 확인
- route별 Web Vitals 수집
- device / network / browser segment 분리
- release 전후 지표 비교
- LCP element attribution 수집 가능하면 포함
- CLS source attribution 수집 가능하면 포함
- INP interaction attribution 수집 가능하면 포함
- Web Vitals regression alert 설정
- Lab Data와 Field Data 차이를 문서화
- Web Vitals 개선 작업은 Performance Tuning 문서와 연결

예시:

```ts
type WebVitalEvent = {
  name: "LCP" | "INP" | "CLS" | "TTFB" | "FCP";
  value: number;
  route: string;
  release: string;
  rating: "good" | "needs-improvement" | "poor";
};
```

---

### [FAQ]

Q. Web Vitals는 왜 수집해야 하나?

A.
실제 사용자가 경험하는 로딩 속도, 반응성, 화면 안정성을 지속적으로 확인하기 위해 필요하다.

Q. 평균 성능만 보면 충분한가?

A.
아니다. p75나 느린 사용자 구간을 함께 봐야 실제 사용자 불편을 파악할 수 있다.

Q. Web Vitals는 어떤 기준으로 나눠서 봐야 하나?

A.
route, release, browser, device, network, country 또는 region 기준으로 분리해 보는 것이 좋다.

---

# 10. Real User Monitoring Rules

## 10.1 RUM 기준

### [개념]

Real User Monitoring은 실제 사용자의 브라우저에서 발생하는 성능, 오류, 상호작용 데이터를 수집하는 방식이다.

Synthetic Monitoring은 정해진 환경에서 주기적으로 테스트하는 방식이다.

---

### [핵심]

RUM 수집 정보:

- Real User Session
- Browser
- OS
- Device
- Network
- Route
- Page Load
- Interaction
- Error
- Web Vitals
- API Latency
- Release
- User Segment
- Geo / Region
- Consent State

RUM vs Synthetic:

| 기준        | RUM                    | Synthetic               |
| ----------- | ---------------------- | ----------------------- |
| 데이터 출처 | 실제 사용자            | 통제된 테스트 환경      |
| 장점        | 현실 반영              | 재현 가능               |
| 단점        | 노이즈 / 개인정보 고려 | 실제 다양성 부족        |
| 사용 목적   | 운영 모니터링          | 회귀 테스트 / 기준 측정 |

---

### [실무]

RUM 작성 기준:

- 실제 사용자 지표를 production에서 수집
- 개인정보 수집 최소화
- user segment는 필요 최소한만 사용
- route / release 기준 분석
- 느린 기기 / 느린 네트워크 사용자를 분리
- Synthetic 테스트와 함께 사용
- 데이터 샘플링 적용 가능
- bot / crawler 트래픽 제외 고려
- consent가 필요한 데이터는 동의 후 수집
- RUM SDK 장애가 앱 동작을 방해하지 않게 구성

---

### [FAQ]

Q. RUM은 왜 필요한가?

A.
실제 사용자의 브라우저, 네트워크, 기기 조건에서 발생하는 성능과 오류를 확인하기 위해 필요하다.

Q. Synthetic Monitoring만으로 충분한가?

A.
아니다. Synthetic은 재현 가능한 기준 측정에 좋지만 실제 사용자 환경의 다양성을 모두 반영하지 못한다.

Q. RUM 데이터에서 개인정보를 수집해도 되나?

A.
필요 최소한으로 제한하고, 개인정보는 masking / hashing / consent 기준을 따라야 한다.

---

# 11. Logging Rules

## 11.1 Frontend Logging 기준

### [개념]

Frontend Logging은 브라우저에서 발생한 의미 있는 이벤트, 오류, 상태 변화, 사용자 행동을 구조화된 형태로 기록하는 체계이다.

---

### [핵심]

로그 수준:

- Debug
- Info
- Warn
- Error
- Fatal

로그 유형:

- Application Log
- Error Log
- API Log
- User Action Log
- Performance Log
- Security Log
- Audit-like Event

구조화 로그 예시:

```ts
type FrontendLog = {
  level: "info" | "warn" | "error";
  message: string;
  route: string;
  release: string;
  timestamp: string;
  context?: Record<string, unknown>;
};
```

---

### [실무]

Logging 작성 기준:

- `console.log` 남발 금지
- production log는 구조화된 형태로 수집
- debug log는 production에서 제한
- error log에는 stack / route / release / context 포함
- 사용자 입력값은 그대로 저장하지 않기
- token / password / 개인정보 로그 금지
- 로그 수준 기준 문서화
- 같은 오류 반복 로그는 rate limit 또는 sampling
- 사용자 행동 추적은 breadcrumb 또는 analytics와 역할 구분
- 로그는 장애 분석에 필요한 정보만 수집

---

### [FAQ]

Q. 프론트엔드에서 console.log를 production에 남겨도 되나?

A.
권장하지 않는다. production에서는 구조화된 log와 error reporting을 사용하고 debug log는 제한해야 한다.

Q. 로그에 사용자 입력값을 남겨도 되나?

A.
안 된다. 개인정보나 민감 정보가 포함될 수 있으므로 masking하거나 수집하지 않아야 한다.

Q. Debug log와 Error log는 어떻게 구분하나?

A.
Debug log는 개발 진단용이고 Error log는 실제 문제 분석과 alert 대상으로 사용할 수 있는 오류 정보이다.

---

# 12. Metrics Rules

## 12.1 Frontend Metrics 기준

### [개념]

Frontend Metrics는 프론트엔드 상태와 사용자 경험을 숫자로 집계해 추세와 이상 징후를 파악하는 지표이다.

---

### [핵심]

대표 Metrics:

- Error Rate
- Crash-free Session Rate
- API Failure Rate
- API Latency
- Page Load Duration
- Route Transition Duration
- Web Vitals Score
- Long Task Count
- JS Chunk Load Failure Count
- Session Replay Count
- User Action Count
- Conversion-impact Error Count
- Release Regression Count

Metric 구성 요소:

- Name
- Value
- Unit
- Tags
- Timestamp
- Route
- Release
- Environment
- Browser
- Device

---

### [실무]

Metrics 작성 기준:

- 핵심 route별 metric 수집
- release별 metric 비교
- error count보다 error rate 우선
- user impact가 큰 metric 우선
- p50 / p75 / p95 같은 percentile 사용
- endpoint별 API latency 측정
- Core Web Vitals는 page / device별 집계
- alert에 사용할 metric과 dashboard metric 구분
- metric cardinality 과도화 주의
- user id 같은 high-cardinality tag 남용 금지

---

### [FAQ]

Q. Frontend Metrics에서 가장 중요한 것은?

A.
Error Rate, Crash-free Session Rate, API Failure Rate, Core Web Vitals, Route별 Latency가 중요하다.

Q. Error Count보다 Error Rate가 중요한 이유는?

A.
트래픽이 늘면 count는 자연스럽게 증가하므로 사용자 영향도를 보려면 rate가 더 유용하다.

Q. Metric tag는 많이 붙일수록 좋은가?

A.
아니다. tag가 너무 많으면 cardinality가 커져 비용과 분석 복잡도가 증가한다.

---

# 13. Tracing and Correlation Rules

## 13.1 Trace ID / Correlation ID 기준

### [개념]

Tracing은 프론트엔드 사용자 요청이 Backend API, Service, Database까지 이어지는 흐름을 추적하는 체계이다.

Frontend에서는 trace id 또는 correlation id를 요청에 포함해 브라우저 이벤트와 백엔드 로그를 연결할 수 있다.

---

### [핵심]

필수 포함:

- Trace ID
- Correlation ID
- Request ID
- Distributed Tracing
- Frontend Span
- Backend Span
- API Request Trace
- User Interaction Trace
- Route Transition Trace
- Error Correlation
- Log Correlation

Trace Flow:

```text
User Click
→ Frontend Action
→ API Request with Trace ID
→ Backend Log / Trace
→ Response
→ Frontend Metric / Error
```

---

### [실무]

작성 기준:

- API 요청마다 correlation id 추가 검토
- Backend response header의 request id 수집
- error event와 API request id 연결
- route transition과 API request를 하나의 흐름으로 묶기
- user action breadcrumb과 trace 연결
- trace id에는 개인정보 넣지 않기
- distributed tracing 도구와 연계 가능
- sampling 기준 명확화
- CORS에서 trace header 허용 필요 여부 확인
- Backend와 header 이름 규칙 합의

예시:

```ts
const traceId = crypto.randomUUID();

await fetch("/api/posts", {
  headers: {
    "x-correlation-id": traceId,
  },
});
```

---

### [FAQ]

Q. Correlation ID는 왜 필요한가?

A.
프론트엔드에서 발생한 API 실패를 백엔드 로그와 연결해 원인을 빠르게 찾기 위해 필요하다.

Q. Trace ID에 사용자 정보를 넣어도 되나?

A.
안 된다. Trace ID는 무작위 식별자여야 하며 개인정보를 포함하면 안 된다.

Q. Frontend Tracing은 언제 유용한가?

A.
사용자 클릭 이후 여러 API 요청과 백엔드 처리가 이어지는 복잡한 흐름을 분석할 때 유용하다.

---

# 14. Breadcrumb Rules

## 14.1 Breadcrumb / User Action Tracking

### [개념]

Breadcrumb는 오류나 성능 문제가 발생하기 전 사용자의 주요 행동, route 이동, API 요청, UI 상태 변화를 시간순으로 기록한 정보이다.

---

### [핵심]

Breadcrumb 유형:

- Navigation Breadcrumb
- Click Breadcrumb
- Form Submit Breadcrumb
- API Request Breadcrumb
- Console Breadcrumb
- State Change Breadcrumb
- Feature Event Breadcrumb
- Error Breadcrumb

Breadcrumb 예시:

```ts
type Breadcrumb = {
  category: "navigation" | "ui" | "api" | "state";
  message: string;
  timestamp: string;
  data?: Record<string, unknown>;
};
```

---

### [실무]

작성 기준:

- 오류 직전 사용자 행동을 재구성할 수 있게 기록
- route change 기록
- 주요 button click 기록
- form submit 성공 / 실패 기록
- API request / response summary 기록
- 민감한 input value 기록 금지
- breadcrumb 수 제한
- 너무 세부적인 event 수집 금지
- feature 이름과 action 이름을 명확히 작성
- analytics event와 observability breadcrumb 역할 구분

주의:

- password / token / address / phone / email 같은 값 기록 금지
- 모든 mouse move / key press 수집 금지
- breadcrumb가 많으면 비용과 노이즈 증가
- 사용자 동의가 필요한 추적은 consent 정책 확인

---

### [FAQ]

Q. Breadcrumb는 왜 필요한가?

A.
오류 발생 직전 사용자가 어떤 route를 이동하고 어떤 버튼을 눌렀는지 파악해 재현과 원인 분석을 돕기 위해 필요하다.

Q. Form 입력값을 breadcrumb에 남겨도 되나?

A.
안 된다. 입력값은 개인정보나 민감 정보일 수 있으므로 남기지 않아야 한다.

Q. Breadcrumb와 Analytics Event는 같은가?

A.
비슷하지만 목적이 다르다. Breadcrumb는 장애 분석용 흐름 기록이고, Analytics는 제품 사용 분석용 이벤트이다.

---

# 15. Session Replay Rules

## 15.1 Session Replay 기준

### [개념]

Session Replay는 사용자의 화면 상호작용 흐름을 재현해 오류와 UX 문제를 분석하는 기능이다.

Frontend Observability에서 Session Replay는 강력하지만 개인정보 노출 위험이 크므로 masking, sampling, consent 기준이 필수이다.

---

### [핵심]

필수 포함:

- Session Replay
- Replay Sampling
- Error-linked Replay
- Privacy Masking
- Input Masking
- Text Masking
- Network Masking
- DOM Recording
- User Consent
- Retention Policy
- Sensitive Page Exclusion

---

### [실무]

사용 기준:

- 모든 세션 full capture보다 sampling 우선
- 오류가 발생한 세션 중심 replay 수집 검토
- input field masking 필수
- 개인정보 텍스트 masking 검토
- password / token / payment / address 영역 제외
- 관리자 페이지 / 결제 페이지 / 개인정보 페이지 replay 제외 검토
- network request body 수집 금지 또는 masking
- replay 보관 기간 제한
- replay 접근 권한 제한
- 사용자 동의가 필요한 지역 / 서비스 정책 확인

주의:

- Session Replay는 개인정보 위험이 큼
- DOM에 민감 정보가 있으면 화면에 그대로 기록될 수 있음
- replay 접근 권한을 넓게 열어두면 위험
- 성능 overhead 확인 필요
- 모바일 / 저사양 기기 sampling 고려

---

### [FAQ]

Q. Session Replay는 언제 사용하나?

A.
오류 재현이 어렵거나 사용자의 실제 행동 흐름을 확인해야 할 때 사용한다.

Q. Session Replay에서 가장 중요한 보안 기준은?

A.
입력값과 개인정보 masking, 민감 페이지 제외, 접근 권한 제한, 보관 기간 제한이다.

Q. 모든 사용자 세션을 녹화해도 되나?

A.
권장하지 않는다. 비용, 성능, 개인정보 위험 때문에 sampling과 consent 기준이 필요하다.

---

# 16. Source Map Rules

## 16.1 Source Map 관리 기준

### [개념]

Source Map은 minified / bundled JavaScript 오류 stack trace를 원본 TypeScript / React 코드 위치로 매핑하기 위한 파일이다.

Frontend Observability에서 Source Map은 오류 원인 분석에 필수이지만 공개 노출 위험을 관리해야 한다.

---

### [핵심]

필수 포함:

- Source Map
- Minified Stack Trace
- Original Source Mapping
- Release Version
- Build Artifact
- Source Map Upload
- Hidden Source Map
- Public Source Map Risk
- Source Map Access Control
- CI Upload

Source Map Flow:

```text
Build
→ Generate Source Map
→ Attach Release Version
→ Upload Source Map to Observability Tool
→ Deploy App
→ Error Occurs
→ Stack Trace Resolved to Original Source
```

---

### [실무]

작성 기준:

- release version과 source map version 일치
- CI/CD에서 source map 자동 업로드
- source map 업로드 실패 시 배포 검증 가능
- public source map 노출 여부 정책 결정
- production source map을 공개 경로에 둘 경우 소스 노출 위험 검토
- hidden source map 또는 restricted access 검토
- source map은 build artifact와 동일해야 함
- release rollback 시 source map도 추적 가능해야 함
- source map 보관 기간 정의
- 민감 코드 / secret이 source에 포함되지 않게 관리

주의:

- Source Map 없으면 stack trace가 minified되어 디버깅 어려움
- release와 source map이 불일치하면 잘못된 위치로 매핑됨
- source map 공개 노출은 코드 유출 위험
- secret은 애초에 frontend bundle에 포함하면 안 됨

---

### [FAQ]

Q. Source Map은 왜 필요한가?

A.
production에서 minified된 오류 stack trace를 원본 TypeScript / React 코드 위치로 되돌려 원인 분석을 쉽게 하기 위해 필요하다.

Q. Source Map을 public에 올려도 되나?

A.
가능은 하지만 소스 코드 노출 위험이 있으므로 hidden source map이나 observability 도구 비공개 업로드를 검토해야 한다.

Q. Source Map이 있는데도 stack trace가 이상하면?

A.
release version 불일치, build artifact 불일치, source map 업로드 실패를 확인해야 한다.

---

# 17. Release Tracking Rules

## 17.1 Release / Deploy Tracking

### [개념]

Release Tracking은 어떤 배포 버전에서 오류나 성능 회귀가 발생했는지 추적하는 기준이다.

---

### [핵심]

필수 metadata:

- Release Version
- Commit SHA
- Build ID
- Deploy Environment
- Deployment Time
- Branch
- Pull Request
- Feature Flag State
- Source Map Version
- App Version

Release 분석 기준:

- Error Rate by Release
- Web Vitals by Release
- API Error by Release
- Crash-free Session by Release
- New Issue after Release
- Regression Detection
- Rollback Decision

---

### [실무]

작성 기준:

- 모든 error / metric / trace에 release 포함
- CI/CD에서 release version 자동 주입
- source map과 release 연결
- feature flag 상태 기록
- release 전후 error rate 비교
- release 전후 Web Vitals 비교
- 새 issue와 기존 issue 구분
- rollback 기준 정의
- hotfix release 추적
- canary / gradual rollout과 연계 가능

예시:

```ts
const observabilityConfig = {
  release: process.env.NEXT_PUBLIC_APP_VERSION,
  environment: process.env.NEXT_PUBLIC_APP_ENV,
};
```

---

### [FAQ]

Q. Release Tracking은 왜 필요한가?

A.
특정 배포 이후 오류나 성능 저하가 증가했는지 확인하고 rollback / hotfix 판단을 하기 위해 필요하다.

Q. Release 정보는 어디에 붙여야 하나?

A.
Error, Log, Metric, Trace, Web Vitals 이벤트 모두에 release metadata를 붙이는 것이 좋다.

Q. Source Map과 Release는 왜 연결해야 하나?

A.
해당 release에서 생성된 bundle과 source map이 일치해야 정확한 원본 코드 위치를 찾을 수 있기 때문이다.

---

# 18. Environment and Context Rules

## 18.1 Environment / User / Device Context

### [개념]

Environment and Context는 오류와 성능 문제를 분석하기 위해 필요한 실행 환경 정보를 의미한다.

---

### [핵심]

Context 유형:

- Environment
- Release
- Route
- Browser
- Browser Version
- OS
- Device Type
- Screen Size
- Network Type
- Locale
- Timezone
- User Segment
- Auth State
- Feature Flag
- Experiment Variant

---

### [실무]

작성 기준:

- production / staging / development 구분
- route와 page name 수집
- browser / OS / device 분리
- network type 수집 가능하면 포함
- user id는 직접 개인정보 대신 내부 id 또는 hash 검토
- auth state는 authenticated / anonymous 정도로 단순화 가능
- feature flag 상태 포함
- 실험 variant 포함
- locale / timezone으로 지역성 문제 분석
- high-cardinality context 남용 금지

주의:

- 이메일 / 이름 / 전화번호 / 주소 직접 수집 금지
- context가 많아질수록 비용과 노이즈 증가
- user segment는 분석에 필요한 최소 범위로 제한
- 개발 환경 이벤트가 production dashboard를 오염시키지 않게 구분

---

### [FAQ]

Q. Error 이벤트에 어떤 context를 붙여야 하나?

A.
release, environment, route, browser, OS, device, user segment, feature flag, breadcrumb를 붙이는 것이 좋다.

Q. 사용자 이메일을 context로 넣어도 되나?

A.
권장하지 않는다. 내부 user id나 hash를 사용하고 개인정보 직접 수집은 피해야 한다.

Q. environment 구분은 왜 중요한가?

A.
development / staging 오류가 production 장애 지표를 오염시키지 않도록 하기 위해 필요하다.

---

# 19. Alerting Rules

## 19.1 Alert 기준

### [개념]

Alerting은 오류나 성능 문제가 일정 기준을 넘었을 때 팀이 즉시 인지하고 대응하도록 알림을 보내는 체계이다.

---

### [핵심]

Alert 대상:

- Error Rate Spike
- New Critical Error
- Crash-free Session Drop
- API Failure Rate Spike
- LCP Regression
- INP Regression
- CLS Regression
- Chunk Load Error Spike
- Payment Flow Error
- Login Flow Error
- Release Regression
- Third-party Script Failure

Alert 기준 요소:

- Severity
- User Impact
- Frequency
- Affected Route
- Affected Release
- Business Critical Flow
- Threshold
- Duration
- Owner

---

### [실무]

작성 기준:

- 모든 error에 alert를 걸지 않음
- 사용자 영향도가 큰 오류 우선
- 결제 / 로그인 / 회원가입 / 핵심 검색 flow는 민감하게 감지
- error count보다 error rate 기준 사용
- release 직후 regression alert 설정
- route별 Web Vitals regression alert 가능
- alert owner 명확화
- alert에 runbook / dashboard link 포함
- noise error는 filtering
- alert fatigue 방지
- Warning과 Critical 기준 분리

예시:

```text
Critical Alert:
- payment route error rate > 2% for 5 minutes
- login API 5xx rate > 3% for 5 minutes
- new release crash-free session drops below threshold
```

---

### [FAQ]

Q. 모든 오류에 알림을 걸어야 하나?

A.
아니다. 사용자 영향도, 빈도, 핵심 flow 여부를 기준으로 alert를 제한해야 한다.

Q. Alert fatigue는 무엇인가?

A.
중요하지 않은 알림이 너무 많아져 실제 장애 알림을 놓치게 되는 문제이다.

Q. 어떤 프론트엔드 오류가 Critical인가?

A.
로그인, 결제, 회원가입, 핵심 검색, 페이지 전체 crash처럼 사용자 핵심 flow를 막는 오류가 Critical이다.

---

# 20. Dashboard Rules

## 20.1 Dashboard 구성 기준

### [개념]

Dashboard는 Frontend Observability 데이터를 팀이 빠르게 이해할 수 있도록 route, release, error, performance, user impact 기준으로 시각화한 화면이다.

---

### [핵심]

Dashboard 구성 요소:

- Error Rate
- Crash-free Session
- Top Errors
- New Issues
- Web Vitals by Route
- API Failure Rate
- API Latency
- Route Load Time
- Release Health
- Browser / Device Breakdown
- User Impact
- Session Replay Link
- Source Map Status
- Alert Status

---

### [실무]

Dashboard 작성 기준:

- 전체 앱 overview 제공
- release별 health 확인 가능
- route별 Web Vitals 확인 가능
- error rate와 affected user 수 함께 표시
- top error와 recent new issue 표시
- API failure endpoint 순위 표시
- device / browser별 분포 확인
- 핵심 business flow 별도 dashboard 구성
- alert와 연결
- owner가 바로 대응할 수 있는 정보 포함
- dashboard가 너무 복잡하면 목적별로 분리

Dashboard 예시:

```text
Frontend Overview Dashboard
- Error Rate
- Crash-free Sessions
- LCP p75 by Route
- INP p75 by Route
- CLS p75 by Route
- Top API Failures
- New Errors by Release
- Affected Users
```

---

### [FAQ]

Q. Frontend Dashboard에는 무엇이 있어야 하나?

A.
Error Rate, Crash-free Session, Web Vitals, API Failure, Release Health, Top Errors, Affected Users가 있어야 한다.

Q. Dashboard는 하나만 만들면 되나?

A.
아니다. 전체 Overview, Release, Performance, API, 핵심 Flow별 Dashboard로 나눌 수 있다.

Q. Error Count만 보면 충분한가?

A.
아니다. Error Rate와 affected user 수를 함께 봐야 사용자 영향도를 알 수 있다.

---

# 21. Privacy and Security Rules

## 21.1 Privacy / PII / Secret 보호

### [개념]

Frontend Observability는 사용자 브라우저 데이터를 수집하므로 개인정보, 인증 정보, 결제 정보, 민감한 입력값이 수집되지 않도록 보호해야 한다.

---

### [핵심]

보호 대상:

- Password
- Token
- API Key
- Session ID
- Email
- Phone Number
- Address
- Payment Info
- Personal Identifier
- Search Query
- Form Input
- Medical / Legal / Sensitive Data
- Location Data

필수 기준:

- PII Masking
- Secret Redaction
- Input Masking
- Network Body Masking
- URL Query Sanitization
- Session Replay Masking
- Data Retention
- Access Control
- Consent
- Compliance

---

### [실무]

작성 기준:

- token / password / API key 수집 금지
- request header의 Authorization masking
- URL query에 개인정보가 있으면 sanitization
- form input value 수집 금지
- Session Replay에서 input / text masking
- payment / account / profile page replay 제외 검토
- observability dashboard 접근 권한 제한
- 데이터 보관 기간 정의
- 사용자 동의가 필요한 데이터는 consent 후 수집
- 개인정보가 log에 들어가지 않도록 SDK 설정 검토
- 오류 context에 raw object를 그대로 넣지 않기

예시:

```ts
function sanitizeUrl(url: string) {
  return url.replace(/token=[^&]+/g, "token=[REDACTED]");
}
```

---

### [FAQ]

Q. Observability에서 가장 위험한 것은?

A.
개인정보, token, password, 결제 정보, 민감한 입력값이 log나 session replay에 수집되는 것이다.

Q. Authorization header를 수집해도 되나?

A.
안 된다. Authorization header는 반드시 redaction하거나 수집하지 않아야 한다.

Q. URL query도 masking해야 하나?

A.
필요하다. query string에 token, email, search keyword, 개인정보가 들어갈 수 있기 때문이다.

---

# 22. Sampling and Cost Rules

## 22.1 Sampling / 비용 관리

### [개념]

Sampling은 모든 이벤트를 수집하지 않고 일부 이벤트만 수집해 비용, 성능 overhead, 데이터 노이즈를 줄이는 전략이다.

---

### [핵심]

Sampling 대상:

- Error Event
- Performance Event
- Session Replay
- Breadcrumb
- API Log
- Trace
- RUM Event
- Debug Log

Sampling 기준:

- Fixed Rate Sampling
- Dynamic Sampling
- Error-based Sampling
- Route-based Sampling
- User Segment Sampling
- Release-based Sampling
- Critical Flow Full Capture
- Noise Filtering

---

### [실무]

작성 기준:

- Critical Error는 가능한 수집
- Session Replay는 낮은 비율 또는 error-linked sampling
- Performance metric은 대표성 유지
- debug log는 production에서 제한
- high-volume event는 sampling 적용
- 핵심 business flow는 sampling 비율 높게 설정 가능
- bot / crawler traffic 제외 검토
- sampling 후에도 분석 가능한 metadata 유지
- 비용과 데이터 품질 균형 유지
- sampling rate 변경 이력 관리

주의:

- sampling이 너무 낮으면 문제를 놓칠 수 있음
- error가 적은 서비스에서 과도한 sampling은 원인 분석 어려움
- 중요한 flow와 일반 flow의 sampling 기준을 다르게 설정
- 비용 절감을 위해 개인정보 보호 기준을 낮추면 안 됨

---

### [FAQ]

Q. Observability 데이터를 모두 수집해야 하나?

A.
아니다. 비용과 성능 overhead가 커질 수 있으므로 sampling과 filtering이 필요하다.

Q. Session Replay는 어떻게 sampling해야 하나?

A.
전체 세션은 낮은 비율로, 오류 발생 세션은 더 높은 비율로 수집하는 전략을 고려한다.

Q. Sampling하면 오류를 놓치지 않나?

A.
가능성이 있다. Critical Error와 핵심 flow는 별도 기준으로 수집률을 높여야 한다.

---

# 23. Next.js Observability Rules

## 23.1 Next.js App Router Observability

### [개념]

Next.js Observability는 App Router 환경에서 Client Component 오류, Server Component 오류, Route Handler 오류, Server Action 오류, Web Vitals, Middleware / Proxy, API 요청을 분리해 추적하는 기준이다.

---

### [핵심]

수집 대상:

- Client Component Error
- Server Component Error
- Route Segment Error
- `error.tsx`
- `global-error.tsx`
- Route Handler Error
- Server Action Error
- Hydration Error
- Chunk Load Error
- Web Vitals
- Route Transition
- Fetch Error
- Revalidation Error
- Middleware / Proxy Error
- Edge Runtime Error

---

### [실무]

작성 기준:

- `error.tsx`에서 client-side error reporting 연계
- server-side error는 server log / APM과 연결
- Route Handler error는 backend API error처럼 추적
- Server Action 실패는 mutation context와 함께 기록
- Web Vitals는 route 기준으로 수집
- Client Component boundary를 기준으로 오류 위치 파악
- Source Map과 release version 연결
- Hydration Error 별도 분류
- Chunk Load Error는 배포 / CDN / 캐시 문제와 연결
- Revalidation 실패는 cache / webhook / auth 문제로 분류

주의:

- Server Component error와 Client Component error 수집 위치가 다름
- Client SDK만으로 server-side error를 모두 잡을 수 없음
- App Router의 rendering / caching 정책과 error context를 함께 봐야 함
- production source map 관리 필요
- middleware / edge runtime은 별도 로그 경로 확인

---

### [FAQ]

Q. Next.js App Router에서 오류는 어디서 수집해야 하나?

A.
Client Component 오류는 client observability SDK, Server Component / Route Handler / Server Action 오류는 server log 또는 APM과 함께 수집해야 한다.

Q. `error.tsx`에서 error reporting을 해도 되나?

A.
가능하다. `error.tsx`는 Client Component이므로 route segment error를 사용자 fallback UI와 함께 report할 수 있다.

Q. Server Component 오류도 브라우저 SDK가 잡나?

A.
항상 그렇지 않다. Server Component 오류는 서버 로그와 APM에서 수집해야 한다.

---

# 24. React Observability Rules

## 24.1 React App Observability

### [개념]

React Observability는 컴포넌트 오류, 렌더링 지연, user interaction, 상태 전이, async boundary 문제를 추적하는 기준이다.

---

### [핵심]

수집 대상:

- Component Error
- Error Boundary Event
- Suspense Fallback Duration
- Render Duration
- Interaction Delay
- State Transition Event
- Form Submit Event
- Route Change Event
- Context Provider Error
- Hook Error
- Infinite Render Symptom
- Memory Leak Symptom

---

### [실무]

작성 기준:

- Error Boundary에 feature / component context 추가
- 주요 사용자 action을 breadcrumb로 기록
- Form submit success / failure 기록
- Suspense fallback이 오래 지속되는 경우 custom metric 검토
- route transition duration 측정
- 비정상적인 반복 error grouping 확인
- React Profiler는 개발 / 성능 분석 용도로 활용
- production에서 과도한 render instrumentation 금지
- custom hook 내부 error는 상위 boundary / reporter로 연결
- Memory leak 의심 시 runtime metric과 cleanup 확인

---

### [FAQ]

Q. React Observability에서 중요한 것은?

A.
컴포넌트 오류를 Error Boundary로 격리하고, 사용자 action과 route context를 함께 수집하는 것이다.

Q. React render 시간을 production에서 항상 수집해야 하나?

A.
권장하지 않는다. overhead가 있을 수 있으므로 샘플링하거나 특정 문제 분석 시 제한적으로 수집한다.

Q. Suspense fallback이 오래 보이면 무엇을 수집해야 하나?

A.
fallback duration, 관련 API latency, route, device, network 정보를 함께 수집하는 것이 좋다.

---

# 25. Third-party Monitoring Rules

## 25.1 Third-party Script / SDK 관측

### [개념]

Third-party Monitoring은 분석, 광고, 지도, 결제, 채팅, 인증 SDK 같은 외부 스크립트가 오류와 성능에 미치는 영향을 추적하는 기준이다.

---

### [핵심]

수집 대상:

- Third-party Script Load Error
- SDK Initialization Error
- Payment SDK Error
- Map SDK Error
- Analytics Script Error
- Chat Widget Error
- Script Load Time
- Main Thread Blocking
- Third-party Network Failure
- Consent State
- External Domain

---

### [실무]

작성 기준:

- 외부 SDK 로딩 성공 / 실패 기록
- SDK 초기화 시간 측정
- payment / auth SDK 오류는 별도 severity 부여
- map / chat SDK는 route별 영향 확인
- 외부 스크립트가 Core Web Vitals에 미치는 영향 추적
- consent 전 로딩 금지 대상 구분
- 외부 SDK 오류와 앱 오류를 구분
- fallback UI 제공 여부 확인
- 동일 SDK 중복 로딩 감지
- 외부 스크립트 장애 시 핵심 flow 차단 여부 분석

주의:

- Third-party error는 noise가 많을 수 있음
- 모든 외부 script error를 critical로 처리하지 않기
- 결제 / 인증 관련 SDK는 business critical 가능성 높음
- 외부 스크립트에 개인정보를 과도하게 전달하지 않기

---

### [FAQ]

Q. Third-party Script도 Observability 대상인가?

A.
그렇다. 외부 SDK 오류나 로딩 지연은 사용자 경험과 핵심 flow에 직접 영향을 줄 수 있다.

Q. 결제 SDK 오류는 어떻게 분류해야 하나?

A.
Business Critical Error로 별도 분류하고 route, payment step, SDK error code를 함께 수집하는 것이 좋다.

Q. 외부 스크립트 오류가 너무 많으면 어떻게 하나?

A.
noise filtering, sampling, script domain별 분류, 사용자 영향도 기준 alert를 적용한다.

---

# 26. Business Flow Observability Rules

## 26.1 핵심 사용자 Flow 관측

### [개념]

Business Flow Observability는 로그인, 회원가입, 결제, 검색, 예약, 주문, 게시글 작성 같은 핵심 사용자 흐름을 단계별로 관측하는 기준이다.

---

### [핵심]

Flow 예시:

- Login Flow
- Signup Flow
- Checkout Flow
- Payment Flow
- Search Flow
- Booking Flow
- Post Creation Flow
- File Upload Flow
- Onboarding Flow
- Admin Approval Flow

Flow Metric:

- Start Count
- Step Completion Rate
- Drop-off Rate
- Error Rate
- API Failure Rate
- Latency by Step
- Retry Count
- Conversion Impact

---

### [실무]

작성 기준:

- 핵심 flow 단계를 정의
- step별 성공 / 실패 event 수집
- error 발생 step 기록
- API latency와 UI latency 분리
- 사용자 입력값은 수집하지 않음
- conversion에 영향을 주는 오류 별도 alert
- release별 flow success rate 비교
- session replay는 critical flow에서 masking 강화
- feature flag / experiment variant와 flow 결과 연결
- funnel analytics와 observability event 역할 구분

예시:

```ts
type FlowEvent = {
  flow: "checkout";
  step: "payment-submit";
  result: "success" | "failure";
  route: string;
  release: string;
  errorCode?: string;
};
```

---

### [FAQ]

Q. Business Flow Observability는 왜 필요한가?

A.
단순 오류 수보다 로그인, 결제, 검색 같은 핵심 흐름이 실제로 막히는지 확인하기 위해 필요하다.

Q. Flow event에 입력값을 넣어도 되나?

A.
안 된다. step 이름, 결과, error code 정도만 수집하고 입력값은 수집하지 않아야 한다.

Q. 결제 flow는 어떻게 관측해야 하나?

A.
결제 시작, SDK 로딩, 결제 요청, 승인, 실패, 취소 단계를 나누고 step별 error rate와 latency를 수집한다.

---

# 27. Troubleshooting Rules

## 27.1 자주 발생하는 Observability 문제

### [개념]

Troubleshooting 문서는 Agent가 Frontend Observability 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Source Map 누락
- Stack Trace가 minified로 보임
- Release 정보 없음
- Error가 너무 많이 수집됨
- Alert가 너무 많이 울림
- 중요한 오류 Alert 누락
- Session Replay에 개인정보 노출
- API Error와 Backend Log 연결 불가
- Web Vitals가 route별로 안 나뉨
- RUM 데이터가 Lab Data와 다름
- Development Error가 Production Dashboard에 섞임
- Chunk Load Error 증가
- Hydration Error 원인 추적 어려움
- Third-party Error Noise
- Observability SDK가 성능에 영향
- CORS 때문에 Trace Header 전달 실패
- User Context가 너무 많아 비용 증가

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

- Production 오류 stack trace가 minified 코드로만 보임

원인:

- Source Map이 업로드되지 않음
- Release version과 Source Map version이 불일치함
- 배포 artifact와 source map이 다른 build에서 생성됨

해결:

- CI/CD에서 source map 업로드 자동화
- release / build id를 동일하게 주입
- 배포 전 source map upload 검증 추가
```

예시:

```md
문제:

- Alert가 너무 많이 울림

원인:

- 모든 error event에 alert 설정
- 사용자 영향도와 severity 구분 없음
- noise error filtering 없음

해결:

- error rate / affected user 기준으로 alert 변경
- critical flow 중심 alert 설정
- known noise error filtering
- warning / critical 기준 분리
```

예시:

```md
문제:

- API Error와 Backend Log를 연결할 수 없음

원인:

- correlation id가 request header에 없음
- backend response request id를 frontend가 수집하지 않음
- CORS에서 trace header가 허용되지 않음

해결:

- frontend에서 correlation id 생성
- backend에서 request id 응답 header 제공
- CORS exposed headers 설정
- error event에 trace id 저장
```

---

### [FAQ]

Q. Stack trace가 minified로만 보이면 무엇을 확인해야 하나?

A.
Source Map 업로드 여부, release version 일치 여부, build artifact와 source map이 같은 build에서 생성되었는지 확인해야 한다.

Q. Alert가 너무 많으면 어떻게 해야 하나?

A.
사용자 영향도, error rate, route, critical flow 기준으로 alert를 줄이고 noise error를 filtering해야 한다.

Q. Session Replay에 개인정보가 보이면 어떻게 해야 하나?

A.
즉시 replay 수집을 중단하거나 masking을 강화하고, 민감 페이지 제외와 데이터 삭제 / 접근 제한을 검토해야 한다.

---

# 28. Code Example Rules

## 28.1 코드 예제 작성 기준

### [개념]

Frontend Observability 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React / Next.js 기준 예제 우선
- 핵심 instrumentation만 포함
- 긴 전체 설정 금지
- Secret 하드코딩 금지
- 개인정보 포함 예제 금지
- Token / password / email logging 금지
- Error Boundary reporting 예제 포함 권장
- API Error normalization 예제 포함 권장
- Source Map / release 설정 예제 포함 가능
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Error reporting wrapper
- React Error Boundary reporting
- Next.js `error.tsx` reporting
- API client error logging
- Web Vitals event type
- Correlation ID header
- Breadcrumb helper
- URL sanitization
- PII masking helper
- Release metadata config
- Alert rule 예시
- Dashboard metric 예시

금지 예제:

- request body 전체 logging
- Authorization header logging
- password / token / email 수집
- 모든 click event 무분별 수집
- 모든 session replay full capture
- production에서 debug log 무제한 전송
- source map public 노출을 기본 권장
- Observability SDK 초기화 실패 시 앱 crash

---

### [FAQ]

Q. Observability 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 instrumentation snippet 중심으로 작성한다.

Q. 로그 예제에 사용자 정보를 넣어도 되나?

A.
안 된다. 예제에서도 개인정보와 민감 정보는 masking하거나 포함하지 않아야 한다.

---

# 29. Comparison Rules

## 29.1 필수 비교 대상

### [개념]

Frontend Observability 문서는 Agent의 관측 설계 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Observability vs Monitoring
- Logging vs Metrics vs Tracing
- RUM vs Synthetic Monitoring
- Error Monitoring vs Analytics
- Breadcrumb vs Analytics Event
- Session Replay vs Event Log
- Lab Data vs Field Data
- Error Count vs Error Rate
- Alert Count vs User Impact
- Source Map Public vs Private Upload
- Client Error vs Server Error
- Runtime Error vs API Error
- Network Error vs HTTP Error
- 401 vs 403
- Sampling vs Full Capture
- Debug Log vs Production Log
- Dashboard vs Alert
- Core Web Vitals vs Custom Metrics

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 수집 대상 / 장점 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Logging, Metrics, Tracing 차이는?

A.
Logging은 사건 기록, Metrics는 수치 집계, Tracing은 요청 흐름 추적이다.

Q. Error Monitoring과 Analytics는 어떻게 다른가?

A.
Error Monitoring은 장애와 오류 분석이 목적이고, Analytics는 제품 사용 행동 분석이 목적이다.

Q. RUM과 Synthetic Monitoring 중 무엇이 더 중요한가?

A.
둘 다 중요하다. RUM은 실제 사용자 경험을 보여주고 Synthetic은 통제된 환경에서 회귀를 재현하는 데 유용하다.

---

# 30. Checklist Rules

## 30.1 문서 품질 체크리스트

### [개념]

Frontend Observability RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Observability 목적이 명확한가?
- [ ] Error Monitoring 기준을 포함했는가?
- [ ] React Error Boundary 연계 기준을 포함했는가?
- [ ] API / Network Error 추적 기준을 포함했는가?
- [ ] Performance Monitoring 기준을 포함했는가?
- [ ] Web Vitals Monitoring 기준을 포함했는가?
- [ ] RUM / Synthetic 구분을 포함했는가?
- [ ] Logging / Metrics / Tracing 구분을 포함했는가?
- [ ] Breadcrumb 기준을 포함했는가?
- [ ] Session Replay 기준을 포함했는가?
- [ ] Source Map 관리 기준을 포함했는가?
- [ ] Release Tracking 기준을 포함했는가?
- [ ] Environment / Context 기준을 포함했는가?
- [ ] Alerting 기준을 포함했는가?
- [ ] Dashboard 기준을 포함했는가?
- [ ] Privacy / PII / Security 기준을 포함했는가?
- [ ] Sampling / Cost 기준을 포함했는가?
- [ ] Next.js / React Observability 기준을 포함했는가?
- [ ] Third-party Monitoring 기준을 포함했는가?
- [ ] Business Flow Observability 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Performance / Architecture / Security 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- Frontend Performance / Security / Next.js App Router 문서와 연계 가능해야 함

---

### [FAQ]

Q. Frontend Observability 문서 품질에서 가장 중요한 것은?

A.
Error, Performance, Web Vitals, API Error, Source Map, Release, Privacy, Alerting 기준이 명확해야 한다.

---

# 31. Retrieval Optimization Rules

## 31.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Observability
- Frontend Monitoring
- Error Monitoring
- Performance Monitoring
- Real User Monitoring
- RUM
- Synthetic Monitoring
- Web Vitals Monitoring
- Core Web Vitals
- LCP
- INP
- CLS
- TTFB
- Error Boundary
- React Error Boundary
- Next.js error.tsx
- Runtime Error
- Unhandled Promise Rejection
- API Error Monitoring
- Network Error
- Correlation ID
- Trace ID
- Distributed Tracing
- Logging
- Metrics
- Tracing
- Structured Log
- Breadcrumb
- User Action Tracking
- Session Replay
- Source Map
- Release Tracking
- Release Regression
- Environment Context
- Alerting
- Dashboard
- PII Masking
- Privacy
- Sampling
- Observability SDK
- Chunk Load Error
- Hydration Error
- Third-party Script Monitoring
- Business Flow Observability

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Frontend Observability는 뭐야?
- 프론트엔드 에러 모니터링 어떻게 해?
- React Error Boundary에서 오류 수집 어떻게 해?
- Next.js error.tsx에서 error reporting 해도 돼?
- API Error를 어떻게 추적해?
- Correlation ID는 왜 필요해?
- Source Map은 왜 필요해?
- Production stack trace가 minified로 보여
- Release Tracking은 왜 필요해?
- Web Vitals는 어떻게 수집해?
- RUM과 Synthetic Monitoring 차이는?
- Logging Metrics Tracing 차이는?
- Breadcrumb는 왜 필요해?
- Session Replay는 언제 써?
- Session Replay 개인정보는 어떻게 보호해?
- Observability에서 PII masking 어떻게 해?
- Alert가 너무 많이 울려
- Error Count와 Error Rate 차이는?
- Dashboard에는 무엇을 넣어?
- Third-party Script 오류도 추적해야 해?
- 결제 flow 오류는 어떻게 관측해?
- Observability 코드 리뷰 기준은?

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

Frontend Observability 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern Frontend
- React 19+
- Next.js App Router
- TypeScript
- Real User Monitoring
- Core Web Vitals
- Source Map Upload
- Release Tracking
- Error Boundary Integration
- API Error Monitoring
- Privacy-first Observability
- Sampling
- Session Replay with Masking
- Distributed Tracing 연계
- Observability SDK 기반 수집
- Production Monitoring

Legacy 제외:

- production console.log 중심 운영
- Source Map 없는 오류 추적
- release metadata 없는 error reporting
- 개인정보를 그대로 log에 저장하는 방식
- request / response body 전체 logging
- 모든 session replay full capture
- alert 기준 없는 모든 error 알림
- frontend / backend log 연결 없는 API 장애 분석
- development / production 이벤트 혼합
- 사용자를 식별 가능한 개인정보로 추적하는 방식

---

### [실무]

문서 작성 시 주의:

- Observability 도구별 SDK 설정은 변동 가능하므로 도구 일반 개념 중심으로 작성
- Sentry, Datadog, New Relic, OpenTelemetry, Grafana 등 특정 도구는 예시로만 사용 가능
- Vendor Lock-in 설명보다 수집 기준과 보안 기준 우선
- Next.js App Router의 client / server error 수집 위치 구분
- Frontend Performance 문서와 중복되는 최적화 상세는 최소화
- Security 문서와 중복되는 개인정보 보호 상세는 Observability 수집 관점으로 제한
- Production 데이터 수집에는 법적 / 조직 정책 확인 필요

---

### [FAQ]

Q. Frontend Observability 문서는 특정 도구 기준이어야 하나?

A.
아니다. 특정 도구보다 Error, Metric, Trace, Web Vitals, Source Map, Release, Privacy 기준을 중심으로 작성한다.

Q. React / Next.js 버전이 중요한가?

A.
중요하다. App Router의 Server / Client Boundary와 Error 처리 방식에 따라 수집 위치가 달라질 수 있다.

Q. Session Replay는 항상 넣어야 하나?

A.
아니다. 개인정보와 비용 위험이 크므로 필요성과 보호 기준을 먼저 검토해야 한다.

---

# 33. Common Mistakes

## 33.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Frontend Observability 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- production에서 console.log만 사용
- Source Map 업로드 누락
- release version 없이 error 수집
- development error가 production dashboard에 섞임
- Error Boundary에 reporting 없음
- unhandled promise rejection 수집 누락
- API Error를 UI toast만 띄우고 수집하지 않음
- request body 전체 logging
- Authorization header logging
- 개인정보를 breadcrumb에 저장
- Session Replay masking 누락
- 모든 세션을 full replay로 수집
- alert를 모든 error에 연결
- Error Count만 보고 사용자 영향도 무시
- Web Vitals를 route별로 분리하지 않음
- RUM 없이 Lighthouse 점수만 확인
- API Error와 Backend Log를 연결할 trace id 없음
- Source Map과 release가 불일치
- Observability SDK가 앱 crash를 유발
- Third-party Script Error를 모두 Critical로 분류
- high-cardinality tag 남용
- sampling 기준 없이 비용 폭증
- Dashboard는 있지만 owner / action 기준 없음

---

### [실무]

리뷰 기준:

- Error Monitoring 적용 여부 확인
- Error Boundary reporting 확인
- Unhandled Rejection 수집 확인
- API Error normalization 확인
- Correlation ID / Trace ID 확인
- Source Map upload 확인
- Release metadata 확인
- Web Vitals route별 수집 확인
- Privacy masking 확인
- Session Replay masking / sampling 확인
- Alert 기준 확인
- Dashboard user impact 표시 확인
- SDK overhead 확인
- Development / Production environment 분리 확인
- 로그에 PII / Secret 포함 여부 확인

---

### [FAQ]

Q. Frontend Observability에서 가장 흔한 실수는?

A.
Source Map과 release metadata 없이 오류를 수집하거나, 개인정보를 로그와 session replay에 그대로 남기는 것이다.

Q. Error Boundary에 fallback UI만 있으면 충분한가?

A.
아니다. error reporting이 없으면 개발팀이 실제 사용자 오류를 알기 어렵다.

Q. Alert를 모든 오류에 걸면 왜 문제인가?

A.
중요하지 않은 알림이 많아져 실제 장애를 놓치는 alert fatigue가 발생한다.

---

# 34. Final Goal

## 34.1 최종 목표

### [개념]

Frontend Observability RAG 문서는 Agent가 프론트엔드 운영 환경의 오류, 성능, 사용자 흐름, 배포 회귀를 관측하고 분석할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Frontend Observability 구조 설계
- Error Monitoring 기준 작성
- React Error Boundary reporting 설계
- Next.js App Router error reporting 설계
- API Error / Network Error 추적 설계
- Correlation ID / Trace ID 연계 설계
- Web Vitals Monitoring 설계
- RUM / Synthetic Monitoring 구분
- Structured Logging 기준 작성
- Metrics 기준 작성
- Breadcrumb 기준 작성
- Session Replay 적용 여부 판단
- Source Map 업로드 / 보안 기준 작성
- Release Tracking 설계
- Alerting 기준 작성
- Dashboard 구성 제안
- PII Masking / Privacy 기준 검토
- Sampling / Cost 전략 제안
- Third-party Script Monitoring 설계
- Business Flow Observability 설계
- Observability 문제 Troubleshooting
- Frontend Observability 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Error / Performance / Web Vitals / API / Release / Privacy 경계 명확화
- 개인정보와 Secret 수집 금지 기준 포함
- Next.js App Router / React / Performance / Security 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Observability Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 운영 환경에서 Error, Performance, Web Vitals, API 실패, 사용자 flow, release regression을 수집하고 privacy-safe하게 분석하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Observability 문서는 어떤 기준으로 작성해야 해?

A.
Error Monitoring, Performance Monitoring, Web Vitals, RUM, Logging, Metrics, Tracing, Source Map, Release Tracking, Alerting, Privacy 중심으로 작성해야 한다.

Q. Frontend Observability는 뭐야?

A.
브라우저에서 발생하는 오류, 성능, 네트워크, 사용자 행동, release 정보를 수집해 실제 사용자 문제를 분석하는 체계이다.

Q. Frontend Monitoring과 Observability 차이는?

A.
Monitoring은 정해진 지표를 감시하는 것이고, Observability는 수집된 데이터로 예상하지 못한 문제의 원인까지 추론할 수 있게 만드는 체계이다.

Q. 프론트엔드 에러 모니터링 어떻게 해?

A.
Error Boundary, global error handler, unhandled promise rejection handler, API client error normalization을 통해 오류를 수집한다.

Q. React Error Boundary에서 오류 수집 어떻게 해?

A.
fallback UI를 제공하면서 error, component stack, route, release, feature context를 observability 도구로 전송한다.

Q. Next.js error.tsx에서 error reporting 해도 돼?

A.
가능하다. `error.tsx`는 Client Component로 동작하므로 route segment error를 report하고 reset UI를 제공할 수 있다.

Q. Server Component 오류도 브라우저 SDK가 잡아?

A.
항상 그렇지 않다. Server Component 오류는 server log 또는 APM에서 수집해야 한다.

Q. 어떤 프론트엔드 오류를 수집해야 해?

A.
Runtime Error, Error Boundary Error, Unhandled Promise Rejection, API Error, Network Error, Chunk Load Error, Hydration Error를 수집해야 한다.

Q. Error Boundary만 있으면 모든 오류를 잡아?

A.
아니다. 이벤트 핸들러, 비동기 callback, Promise rejection은 별도 수집이 필요하다.

Q. API Error를 어떻게 추적해?

A.
API client에서 endpoint, method, status code, latency, timeout, retry count, trace id를 기록하고 error type을 normalize한다.

Q. API 요청 body를 그대로 로그로 남겨도 돼?

A.
안 된다. 개인정보, token, password, 결제 정보가 포함될 수 있으므로 masking하거나 수집하지 않아야 한다.

Q. 401과 403은 어떻게 다르게 추적해?

A.
401은 인증 실패 / 세션 만료, 403은 권한 부족으로 분류해 별도 metric과 alert 기준을 둔다.

Q. Correlation ID는 왜 필요해?

A.
프론트엔드 API 실패 이벤트를 백엔드 로그와 연결해 원인을 빠르게 찾기 위해 필요하다.

Q. Trace ID에 사용자 정보를 넣어도 돼?

A.
안 된다. Trace ID는 무작위 식별자여야 하며 개인정보를 포함하면 안 된다.

Q. CORS 때문에 trace header가 안 보여. 무엇을 확인해?

A.
Backend의 allowed headers와 exposed headers 설정을 확인해야 한다.

Q. Web Vitals는 어떻게 수집해?

A.
LCP, INP, CLS, TTFB, FCP를 route, release, browser, device, network context와 함께 RUM 이벤트로 수집한다.

Q. Web Vitals는 평균만 보면 돼?

A.
아니다. p75와 느린 사용자 구간을 함께 봐야 실제 사용자 불편을 파악할 수 있다.

Q. LCP는 무엇을 관측해?

A.
가장 큰 콘텐츠가 화면에 표시되는 시간을 관측해 로딩 성능을 판단한다.

Q. INP는 무엇을 관측해?

A.
사용자 상호작용에 대한 응답성을 관측한다.

Q. CLS는 무엇을 관측해?

A.
예상하지 못한 레이아웃 이동으로 인한 화면 안정성을 관측한다.

Q. RUM과 Synthetic Monitoring 차이는?

A.
RUM은 실제 사용자 데이터를 수집하고, Synthetic Monitoring은 정해진 환경에서 반복 측정한다.

Q. RUM은 왜 필요해?

A.
실제 사용자의 브라우저, 네트워크, 기기 조건에서 발생하는 성능과 오류를 확인하기 위해 필요하다.

Q. Synthetic Monitoring만으로 충분해?

A.
아니다. Synthetic은 재현 가능한 기준 측정에 좋지만 실제 사용자 환경의 다양성을 모두 반영하지 못한다.

Q. Logging Metrics Tracing 차이는?

A.
Logging은 사건 기록, Metrics는 수치 집계, Tracing은 요청 흐름 추적이다.

Q. production에서 console.log 써도 돼?

A.
권장하지 않는다. production에서는 구조화된 log와 error reporting을 사용하고 debug log는 제한해야 한다.

Q. 로그에 사용자 입력값을 남겨도 돼?

A.
안 된다. 개인정보나 민감 정보가 포함될 수 있으므로 masking하거나 수집하지 않아야 한다.

Q. Frontend Metrics에서 무엇이 중요해?

A.
Error Rate, Crash-free Session Rate, API Failure Rate, API Latency, Core Web Vitals, Route Load Time이 중요하다.

Q. Error Count와 Error Rate 차이는?

A.
Error Count는 오류 개수이고 Error Rate는 전체 세션이나 요청 대비 오류 비율이다. 사용자 영향도 판단에는 Error Rate가 더 유용하다.

Q. Metric tag는 많이 붙이면 좋아?

A.
아니다. tag가 너무 많으면 cardinality가 커져 비용과 분석 복잡도가 증가한다.

Q. Breadcrumb는 왜 필요해?

A.
오류 발생 직전 사용자가 어떤 route로 이동하고 어떤 버튼을 눌렀는지 파악해 재현과 원인 분석을 돕기 위해 필요하다.

Q. Breadcrumb와 Analytics Event는 같은가?

A.
비슷하지만 목적이 다르다. Breadcrumb는 장애 분석용 흐름 기록이고 Analytics는 제품 사용 분석용 이벤트이다.

Q. Form 입력값을 breadcrumb에 남겨도 돼?

A.
안 된다. 입력값은 개인정보나 민감 정보일 수 있으므로 남기지 않아야 한다.

Q. Session Replay는 언제 써?

A.
오류 재현이 어렵거나 사용자의 실제 행동 흐름을 확인해야 할 때 사용한다.

Q. Session Replay 개인정보는 어떻게 보호해?

A.
input masking, text masking, network body masking, 민감 페이지 제외, 접근 권한 제한, 보관 기간 제한을 적용한다.

Q. 모든 사용자 세션을 녹화해도 돼?

A.
권장하지 않는다. 비용, 성능, 개인정보 위험 때문에 sampling과 consent 기준이 필요하다.

Q. Source Map은 왜 필요해?

A.
production에서 minified된 오류 stack trace를 원본 TypeScript / React 코드 위치로 되돌려 원인 분석을 쉽게 하기 위해 필요하다.

Q. Production stack trace가 minified로 보여. 무엇을 확인해?

A.
Source Map 업로드 여부, release version 일치 여부, build artifact와 source map이 같은 build에서 생성되었는지 확인해야 한다.

Q. Source Map을 public에 올려도 돼?

A.
가능은 하지만 소스 코드 노출 위험이 있으므로 hidden source map이나 observability 도구 비공개 업로드를 검토해야 한다.

Q. Release Tracking은 왜 필요해?

A.
특정 배포 이후 오류나 성능 저하가 증가했는지 확인하고 rollback / hotfix 판단을 하기 위해 필요하다.

Q. Release 정보는 어디에 붙여야 해?

A.
Error, Log, Metric, Trace, Web Vitals 이벤트 모두에 release metadata를 붙이는 것이 좋다.

Q. Source Map과 Release는 왜 연결해?

A.
해당 release에서 생성된 bundle과 source map이 일치해야 정확한 원본 코드 위치를 찾을 수 있기 때문이다.

Q. Error 이벤트에 어떤 context를 붙여?

A.
release, environment, route, browser, OS, device, user segment, feature flag, breadcrumb를 붙이는 것이 좋다.

Q. 사용자 이메일을 context로 넣어도 돼?

A.
권장하지 않는다. 내부 user id나 hash를 사용하고 개인정보 직접 수집은 피해야 한다.

Q. Observability에서 PII masking 어떻게 해?

A.
Authorization header, token, password, email, phone, address, payment info, form input, URL query를 redaction하거나 수집하지 않는다.

Q. Authorization header를 수집해도 돼?

A.
안 된다. Authorization header는 반드시 redaction하거나 수집하지 않아야 한다.

Q. URL query도 masking해야 해?

A.
필요하다. query string에 token, email, search keyword, 개인정보가 들어갈 수 있기 때문이다.

Q. Alert가 너무 많이 울려. 어떻게 해?

A.
사용자 영향도, error rate, route, critical flow 기준으로 alert를 줄이고 noise error를 filtering해야 한다.

Q. 모든 오류에 알림을 걸어야 해?

A.
아니다. 사용자 영향도, 빈도, 핵심 flow 여부를 기준으로 alert를 제한해야 한다.

Q. Alert fatigue는 뭐야?

A.
중요하지 않은 알림이 너무 많아져 실제 장애 알림을 놓치게 되는 문제이다.

Q. 어떤 오류가 Critical이야?

A.
로그인, 결제, 회원가입, 핵심 검색, 페이지 전체 crash처럼 사용자 핵심 flow를 막는 오류가 Critical이다.

Q. Dashboard에는 무엇을 넣어?

A.
Error Rate, Crash-free Session, Web Vitals, API Failure, Release Health, Top Errors, Affected Users를 넣는다.

Q. Dashboard는 하나면 충분해?

A.
아니다. 전체 Overview, Release, Performance, API, 핵심 Flow별 Dashboard로 나눌 수 있다.

Q. Third-party Script 오류도 추적해야 해?

A.
그렇다. 외부 SDK 오류나 로딩 지연은 사용자 경험과 핵심 flow에 직접 영향을 줄 수 있다.

Q. 결제 SDK 오류는 어떻게 분류해?

A.
Business Critical Error로 별도 분류하고 route, payment step, SDK error code를 함께 수집하는 것이 좋다.

Q. 외부 스크립트 오류가 너무 많으면 어떻게 해?

A.
noise filtering, sampling, script domain별 분류, 사용자 영향도 기준 alert를 적용한다.

Q. 결제 flow 오류는 어떻게 관측해?

A.
결제 시작, SDK 로딩, 결제 요청, 승인, 실패, 취소 단계를 나누고 step별 error rate와 latency를 수집한다.

Q. Business Flow Observability는 왜 필요해?

A.
단순 오류 수보다 로그인, 결제, 검색 같은 핵심 흐름이 실제로 막히는지 확인하기 위해 필요하다.

Q. Flow event에 입력값을 넣어도 돼?

A.
안 된다. step 이름, 결과, error code 정도만 수집하고 입력값은 수집하지 않아야 한다.

Q. Observability 데이터를 모두 수집해야 해?

A.
아니다. 비용과 성능 overhead가 커질 수 있으므로 sampling과 filtering이 필요하다.

Q. Sampling하면 오류를 놓치지 않아?

A.
가능성이 있다. Critical Error와 핵심 flow는 별도 기준으로 수집률을 높여야 한다.

Q. Observability SDK가 성능에 영향 줄 수 있어?

A.
그렇다. 수집량, session replay, heavy instrumentation이 많으면 성능 overhead가 생길 수 있다.

Q. Development Error가 Production Dashboard에 섞이면?

A.
environment tag를 명확히 설정하고 production dashboard는 production event만 보도록 필터링한다.

Q. Chunk Load Error가 증가하면 무엇을 의심해?

A.
배포 중 캐시 불일치, CDN 문제, 오래된 HTML이 새 chunk를 찾는 문제, 네트워크 오류를 확인한다.

Q. Hydration Error는 어떻게 관측해?

A.
route, release, browser, component boundary, error message, 관련 breadcrumb를 함께 수집한다.

Q. Frontend Observability 코드 리뷰 기준은?

A.
Error 수집, Source Map, Release metadata, API trace, Web Vitals, PII masking, alert 기준, sampling, SDK overhead를 확인한다.

Q. Frontend Observability RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 운영 환경에서 Error, Performance, Web Vitals, API 실패, 사용자 flow, release regression을 수집하고 privacy-safe하게 분석하도록 만드는 것이다.
