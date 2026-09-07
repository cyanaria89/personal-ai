# Monitoring & Logging Domain Rules

---

# 1. Domain Purpose

## 1.1 Monitoring & Logging 문서 목적

### [개념]

Monitoring & Logging Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Application Monitoring Support
- Infrastructure Monitoring Support
- Log Collection / Analysis Support
- Alerting Strategy Support
- Incident Detection Support
- Deployment Verification Support
- Troubleshooting Support
- Observability Review Support

우선순위:

1. Monitoring Core
2. Logging Core
3. Metrics / Logs / Traces
4. Alerting / Incident Response
5. Dashboard / Troubleshooting
6. Deployment Verification

---

### [핵심]

Monitoring & Logging 문서는 단순 로그 확인 문서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- Monitoring 대상 정의
- Logging 전략 설계
- Metrics 수집 기준 정의
- Log Level 기준 검토
- Alert Rule 설계
- Dashboard 구성 검토
- 배포 후 지표 검증
- 장애 원인 추적
- SLO / SLA / SLI 기준 이해
- Docker / Kubernetes / CI/CD / Deployment Strategy와 연계
- Observability 기반 운영 개선

---

### [실무]

2026 실무 기준 Monitoring & Logging 문서는 다음 흐름을 기준으로 작성한다.

```text
Application / Infrastructure
→ Metrics / Logs / Traces
→ Collection
→ Storage
→ Dashboard
→ Alerting
→ Incident Response
→ Postmortem
```

Monitoring & Logging 문서는 장애 발생 후 확인하는 보조 수단이 아니라, 장애를 조기에 감지하고 원인을 추적하며 재발을 방지하기 위한 운영 핵심 문서이다.

---

### [FAQ]

Q. Monitoring & Logging 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 서비스 상태를 관측하고 장애를 감지, 분석, 복구하기 위한 RAG 문서이다.

Q. Monitoring과 Logging은 같은가?

A.
아니다. Monitoring은 지표 기반 상태 관측이고 Logging은 이벤트와 실행 기록 기반 분석이다.

Q. Observability와 Monitoring은 어떻게 다른가?

A.
Monitoring은 알려진 문제를 감시하는 데 강하고, Observability는 Metrics, Logs, Traces를 통해 알 수 없는 문제를 추론하는 데 초점이 있다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Monitoring & Logging Domain 문서는 애플리케이션, 인프라, 컨테이너, 배포, 장애 대응에 필요한 관측 체계를 다룬다.

포함 범위:

- Monitoring
- Logging
- Observability
- Metrics
- Logs
- Traces
- Alerting
- Dashboard
- SLI
- SLO
- SLA
- Error Rate
- Latency
- Throughput
- Saturation
- Health Check
- Application Log
- Access Log
- Error Log
- Audit Log
- Structured Logging
- Log Level
- Log Aggregation
- Log Rotation
- Distributed Tracing
- Correlation ID
- Incident Response
- Postmortem
- Prometheus
- Grafana
- Loki
- ELK / OpenSearch
- OpenTelemetry
- Docker Logging
- Kubernetes Monitoring
- Deployment Verification
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Monitoring
- Logging
- Observability
- Metrics
- Logs
- Traces
- Alert
- Dashboard
- SLI
- SLO
- SLA
- Error Rate
- Latency
- Throughput
- Saturation
- Health Check
- Structured Logging
- Correlation ID
- Incident
- Postmortem
- Prometheus
- Grafana
- OpenTelemetry

---

### [실무]

Monitoring & Logging 문서는 아래 상황을 해결할 수 있어야 한다.

- 배포 후 Error Rate 증가 탐지
- API Latency 급증 원인 추적
- Container Memory 사용량 확인
- Kubernetes Pod Restart 원인 분석
- DB Connection Pool 고갈 탐지
- 외부 API 장애 감지
- 로그에서 특정 Request 흐름 추적
- Correlation ID 기반 장애 분석
- 알림 피로도 감소
- 운영 Dashboard 설계
- SLO 기반 장애 판단
- Incident Response와 Postmortem 작성 지원

---

### [FAQ]

Q. Monitoring & Logging 문서에 특정 도구 사용법을 모두 포함해야 하는가?

A.
아니다. Prometheus, Grafana, Loki, ELK, OpenTelemetry 같은 대표 도구는 다루되 핵심은 관측 기준, 지표 설계, 로그 전략, 장애 대응이다.

Q. Monitoring & Logging 문서는 Deployment Strategy와 어떻게 연결되는가?

A.
배포 후 Health Check, Error Rate, Latency, Business Metric을 확인하여 배포 성공, Rollback, Roll Forward를 판단하는 데 연결된다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Monitoring & Logging 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]

Optional:

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

### [핵심]

Monitoring & Logging 문서는 검색 친화적인 장애 분석 구조를 우선한다.

```text
Signal
→ Collection
→ Dashboard
→ Alert
→ Investigation
→ Mitigation
→ Postmortem
```

---

### [실무]

권장 Part 구성:

- Monitoring_Logging_Part01_Core.md
- Monitoring_Logging_Part02_Metrics.md
- Monitoring_Logging_Part03_Logging.md
- Monitoring_Logging_Part04_Tracing.md
- Monitoring_Logging_Part05_Alerting.md
- Monitoring_Logging_Part06_Dashboard.md
- Monitoring_Logging_Part07_Docker_Kubernetes.md
- Monitoring_Logging_Part08_Deployment_Verification.md
- Monitoring_Logging_Part09_Incident_Troubleshooting.md

---

### [FAQ]

Q. Monitoring & Logging 문서에 FAQ가 필요한가?

A.
필수이다. 운영 질문은 “왜 느려졌나”, “로그가 안 보인다”, “알림이 너무 많다”, “배포 후 장애인가”처럼 문제 상황으로 들어오는 경우가 많다.

Q. Monitoring & Logging 문서는 도구 중심으로 작성해야 하는가?

A.
도구보다 관측 대상, 지표 기준, 로그 품질, 알림 기준, 장애 분석 Flow 중심으로 작성해야 한다.

---

# 4. Monitoring Core Rules

## 4.1 Monitoring Core 작성 규칙

### [개념]

Monitoring은 시스템 상태를 지속적으로 관측하여 장애, 성능 저하, 비정상 패턴을 감지하는 활동이다.

필수 포함:

- System Health
- Metrics Collection
- Threshold
- Alerting
- Dashboard
- Incident Detection
- Trend Analysis

---

### [핵심]

Monitoring 핵심 목적:

- 장애 조기 감지
- 성능 저하 탐지
- 배포 영향 확인
- 용량 계획 지원
- 운영 의사결정 지원
- SLO 준수 확인

기본 흐름:

```text
Service
→ Metrics
→ Monitoring System
→ Dashboard
→ Alert
→ Response
```

---

### [실무]

Monitoring 대상:

- Application
- API
- Database
- Cache
- Message Queue
- Container
- Kubernetes
- Server
- Network
- External API
- Business Metric

Monitoring은 “서버가 살아있는가”보다 “사용자가 정상적으로 서비스를 이용할 수 있는가”를 우선해야 한다.

---

### [FAQ]

Q. Monitoring은 왜 필요한가?

A.
장애와 성능 저하를 조기에 감지하고 사용자 영향이 커지기 전에 대응하기 위해 필요하다.

Q. 서버 CPU만 보면 Monitoring이 충분한가?

A.
아니다. Error Rate, Latency, Traffic, Business Metric, Dependency 상태까지 함께 봐야 한다.

---

# 5. Logging Core Rules

## 5.1 Logging Core 작성 규칙

### [개념]

Logging은 애플리케이션과 시스템에서 발생한 이벤트, 오류, 요청, 상태 변화를 기록하는 활동이다.

필수 포함:

- Application Log
- Access Log
- Error Log
- Audit Log
- Structured Logging
- Log Level
- Log Aggregation
- Log Retention

---

### [핵심]

Logging 핵심 목적:

- 장애 원인 분석
- 사용자 요청 흐름 추적
- 보안 감사
- 배포 후 이상 탐지
- 비즈니스 이벤트 확인
- 재현 어려운 문제 조사

기본 흐름:

```text
Application Event
→ Log Output
→ Log Collector
→ Log Storage
→ Search / Analysis
```

---

### [실무]

운영 로그는 검색 가능해야 한다.

좋은 로그 조건:

- Timestamp 포함
- Log Level 포함
- Service Name 포함
- Environment 포함
- Request ID / Correlation ID 포함
- User ID는 필요 시 마스킹
- Error Stack Trace 포함
- 민감 정보 제외
- JSON Structured Logging 권장

---

### [FAQ]

Q. Logging은 왜 필요한가?

A.
장애 발생 시 어떤 요청, 어떤 조건, 어떤 코드 경로에서 문제가 발생했는지 분석하기 위해 필요하다.

Q. 좋은 운영 로그의 기준은?

A.
검색 가능하고, 요청 흐름을 추적할 수 있으며, 오류 원인을 파악할 수 있고, 민감 정보가 노출되지 않아야 한다.

---

# 6. Observability Rules

## 6.1 Observability 작성 규칙

### [개념]

Observability는 시스템 외부에서 수집한 신호를 통해 내부 상태를 추론할 수 있는 능력이다.

핵심 신호:

- Metrics
- Logs
- Traces

---

### [핵심]

Observability의 목표:

- 알 수 없는 장애 원인 추론
- 분산 시스템 요청 흐름 추적
- 병목 구간 식별
- 배포 영향 분석
- 사용자 경험 저하 원인 파악

```text
Metrics
+ Logs
+ Traces
→ Observability
```

---

### [실무]

Observability가 필요한 상황:

- Microservices 환경
- Kubernetes 운영
- 외부 API 연동이 많은 서비스
- 비동기 Message Queue 사용
- 요청 경로가 여러 서비스에 걸친 경우
- 배포 후 일부 사용자만 오류 발생
- 성능 저하 원인이 명확하지 않은 경우

---

### [FAQ]

Q. Observability의 3대 요소는 무엇인가?

A.
Metrics, Logs, Traces이다.

Q. Observability가 중요한 이유는?

A.
복잡한 시스템에서 단순 지표만으로는 알기 어려운 내부 상태와 장애 원인을 추론하기 위해 필요하다.

---

# 7. Metrics Rules

## 7.1 Metrics 작성 규칙

### [개념]

Metrics는 시스템 상태를 숫자로 표현한 시계열 데이터이다.

예:

- Request Count
- Error Rate
- Latency
- CPU Usage
- Memory Usage
- DB Connection Count

---

### [핵심]

필수 포함:

- Counter
- Gauge
- Histogram
- Summary
- Time Series
- Label
- Cardinality
- Scrape
- Retention

대표 지표:

```text
Traffic
Error Rate
Latency
Saturation
```

---

### [실무]

Application Metrics:

- Request Per Second
- HTTP Status Code Count
- Error Rate
- P95 / P99 Latency
- Active User
- Login Success Rate
- Payment Failure Rate

Infrastructure Metrics:

- CPU Usage
- Memory Usage
- Disk Usage
- Network I/O
- Container Restart Count
- Pod Status

Database Metrics:

- Connection Pool Usage
- Slow Query Count
- Lock Wait
- Replication Lag
- Query Latency

---

### [주의]

Metric Label Cardinality가 너무 높으면 Monitoring 시스템에 부하가 증가한다.

주의 대상:

- userId
- email
- requestId
- raw URL parameter
- sessionId

---

### [FAQ]

Q. Metrics는 무엇인가?

A.
시스템 상태를 숫자로 표현한 시계열 데이터이다.

Q. Metric Cardinality가 높으면 왜 위험한가?

A.
Label 조합이 폭증하여 저장소 비용, 쿼리 성능, Monitoring 시스템 부하가 증가하기 때문이다.

---

# 8. Golden Signals Rules

## 8.1 Golden Signals 작성 규칙

### [개념]

Golden Signals는 서비스 상태를 판단하기 위한 핵심 관측 지표이다.

대표 항목:

- Latency
- Traffic
- Errors
- Saturation

---

### [핵심]

필수 포함:

- Latency
- Traffic
- Error Rate
- Saturation

```text
Latency
→ 요청 처리 시간

Traffic
→ 요청량

Errors
→ 실패율

Saturation
→ 자원 포화도
```

---

### [실무]

API 서비스 기준 Golden Signals:

- P95 / P99 Latency
- Request Per Second
- HTTP 5xx Rate
- HTTP 4xx Rate
- CPU / Memory Usage
- DB Connection Pool Saturation
- Thread Pool Saturation
- Queue Lag

---

### [FAQ]

Q. Golden Signals는 무엇인가?

A.
서비스 상태를 빠르게 판단하기 위한 핵심 지표로 Latency, Traffic, Errors, Saturation을 의미한다.

Q. 배포 후 가장 먼저 볼 Golden Signals는?

A.
Error Rate, P95 / P99 Latency, Traffic 변화, Saturation 지표를 먼저 확인한다.

---

# 9. Logs Rules

## 9.1 Logs 작성 규칙

### [개념]

Logs는 시스템에서 발생한 개별 이벤트 기록이다.

Logs는 Metrics로 설명되지 않는 원인을 파악하는 데 사용한다.

---

### [핵심]

필수 포함:

- Event Log
- Access Log
- Error Log
- Audit Log
- Structured Log
- Stack Trace
- Correlation ID
- Log Query

---

### [실무]

운영 로그 필드 예시:

```json
{
  "timestamp": "2026-06-29T10:00:00+09:00",
  "level": "ERROR",
  "service": "payment-api",
  "environment": "prod",
  "traceId": "abc-123",
  "requestId": "req-456",
  "message": "Payment approval failed",
  "errorCode": "PAYMENT_TIMEOUT"
}
```

로그 검색 기준:

- service
- environment
- level
- traceId
- requestId
- userId
- errorCode
- endpoint
- time range

---

### [주의]

로그에 민감 정보를 남기지 않는다.

금지 대상:

- Password
- Access Token
- Refresh Token
- API Key
- 주민등록번호
- 카드번호
- 인증 코드
- Session Cookie
- 개인 식별 정보 원문

---

### [FAQ]

Q. Logs는 언제 보는가?

A.
Metrics에서 이상을 발견한 뒤 구체적인 오류 원인, 요청 흐름, 예외 Stack Trace를 확인할 때 본다.

Q. 로그에 Access Token을 남겨도 되는가?

A.
금지한다. Token은 인증 권한 탈취로 이어질 수 있으므로 절대 로그에 남기지 않는다.

---

# 10. Log Level Rules

## 10.1 Log Level 작성 규칙

### [개념]

Log Level은 로그의 중요도와 용도를 구분하는 기준이다.

대표 Level:

- TRACE
- DEBUG
- INFO
- WARN
- ERROR

---

### [핵심]

Log Level 기준:

| Level | 용도             | 운영 사용        |
| ----- | ---------------- | ---------------- |
| TRACE | 매우 상세한 흐름 | 기본 비활성      |
| DEBUG | 디버깅 정보      | 운영 기본 비활성 |
| INFO  | 정상 주요 이벤트 | 운영 사용        |
| WARN  | 잠재 문제        | 운영 사용        |
| ERROR | 실패 / 장애      | 운영 사용        |

---

### [실무]

운영 Log Level 기준:

- 정상 요청 성공 전체를 과도하게 INFO로 남기지 않는다.
- 비즈니스 주요 이벤트는 INFO 가능.
- 재시도 가능한 일시 오류는 WARN 가능.
- 사용자 요청 실패, 외부 API 실패, DB 오류는 ERROR 가능.
- Stack Trace는 원인 분석 가능한 위치에 기록한다.
- DEBUG는 장애 분석 시 제한적으로 활성화한다.

---

### [주의]

ERROR 로그가 너무 많으면 Alert 피로도가 증가한다.

WARN / ERROR 기준을 명확히 해야 한다.

---

### [FAQ]

Q. 운영 환경에서 DEBUG 로그를 항상 켜도 되는가?

A.
권장하지 않는다. 로그 비용, 성능 저하, 민감 정보 노출 위험이 증가할 수 있다.

Q. WARN과 ERROR 차이는?

A.
WARN은 잠재적 문제 또는 복구 가능한 이상이고 ERROR는 실제 실패나 장애 가능성이 높은 상황이다.

---

# 11. Structured Logging Rules

## 11.1 Structured Logging 작성 규칙

### [개념]

Structured Logging은 로그를 JSON 같은 구조화된 형식으로 기록하여 검색과 분석을 쉽게 만드는 방식이다.

---

### [핵심]

필수 포함:

- JSON Log
- Key-Value Field
- Log Query
- Index
- Trace ID
- Request ID
- Consistent Schema

---

### [실무]

권장 필드:

- timestamp
- level
- service
- environment
- version
- traceId
- requestId
- userId
- endpoint
- method
- statusCode
- latencyMs
- errorCode
- message

예시:

```json
{
  "level": "INFO",
  "service": "festival-api",
  "environment": "prod",
  "traceId": "trace-001",
  "method": "GET",
  "endpoint": "/api/festivals",
  "statusCode": 200,
  "latencyMs": 85
}
```

---

### [FAQ]

Q. Structured Logging은 왜 필요한가?

A.
로그를 필드 기반으로 검색, 집계, 필터링할 수 있어 장애 분석과 Dashboard 구성이 쉬워진다.

Q. 일반 문자열 로그보다 JSON 로그가 좋은 이유는?

A.
검색 도구가 필드를 인식할 수 있어 service, level, traceId, statusCode 같은 조건으로 정확히 조회할 수 있다.

---

# 12. Correlation ID Rules

## 12.1 Correlation ID 작성 규칙

### [개념]

Correlation ID는 하나의 사용자 요청이 여러 서비스와 로그를 거쳐 이동할 때 동일 요청임을 추적하기 위한 식별자이다.

---

### [핵심]

필수 포함:

- Correlation ID
- Request ID
- Trace ID
- Span ID
- Distributed Request
- Log Propagation
- Header Propagation

---

### [Flow]

```text
Client Request
→ API Gateway
→ Backend Service
→ Database / External API
→ Logs with same Correlation ID
```

---

### [실무]

권장 Header:

```text
X-Request-Id
X-Correlation-Id
traceparent
```

로그에는 동일한 Correlation ID를 포함한다.

```text
traceId=abc-123 requestId=req-456 service=order-api error=timeout
```

---

### [FAQ]

Q. Correlation ID는 왜 필요한가?

A.
여러 서비스와 로그에 흩어진 하나의 요청 흐름을 추적하기 위해 필요하다.

Q. Trace ID와 Request ID는 같은가?

A.
비슷하게 쓰이지만 Trace ID는 분산 추적 전체 흐름을, Request ID는 개별 요청 식별을 의미하는 경우가 많다.

---

# 13. Distributed Tracing Rules

## 13.1 Distributed Tracing 작성 규칙

### [개념]

Distributed Tracing은 하나의 요청이 여러 서비스, DB, 외부 API를 거치는 경로와 시간을 추적하는 방식이다.

---

### [핵심]

필수 포함:

- Trace
- Span
- Trace ID
- Span ID
- Parent Span
- Service Map
- Latency Breakdown
- OpenTelemetry

---

### [Flow]

```text
Client
→ API Gateway Span
→ Backend Span
→ DB Span
→ External API Span
```

---

### [실무]

Tracing이 유용한 상황:

- Microservices 요청 추적
- API Gateway → Backend → DB 병목 분석
- 외부 API 지연 원인 확인
- 배포 후 특정 서비스 Latency 증가 분석
- 비동기 처리 흐름 추적
- 사용자별 간헐 오류 분석

---

### [주의]

Tracing Sampling 비율을 고려한다.

모든 요청을 100% Trace하면 비용과 저장소 부하가 커질 수 있다.

---

### [FAQ]

Q. Distributed Tracing은 왜 필요한가?

A.
분산 시스템에서 요청이 어떤 서비스에서 지연되거나 실패했는지 파악하기 위해 필요하다.

Q. Span은 무엇인가?

A.
Trace 안에서 하나의 작업 단위나 서비스 호출 구간을 의미한다.

---

# 14. Alerting Rules

## 14.1 Alerting 작성 규칙

### [개념]

Alerting은 시스템 이상이 발생했을 때 담당자에게 자동으로 알리는 운영 체계이다.

Alert는 즉시 행동이 필요한 문제에만 발생해야 한다.

---

### [핵심]

필수 포함:

- Alert Rule
- Threshold
- Severity
- Notification
- Escalation
- Alert Fatigue
- Runbook
- On-call

---

### [실무]

좋은 Alert 조건:

- 사용자 영향이 있음
- 즉시 조치가 필요함
- 원인 확인 경로가 있음
- 담당자가 명확함
- Runbook이 있음
- 중복 알림이 적음
- 임계치가 현실적임

Alert Severity 예시:

| Severity | 의미           | 예                       |
| -------- | -------------- | ------------------------ |
| Critical | 즉시 대응 필요 | 결제 API 5xx 급증        |
| Warning  | 주의 필요      | DB Connection 사용률 80% |
| Info     | 기록 목적      | 배포 완료                |

---

### [주의]

나쁜 Alert:

- 조치 방법 없음
- 너무 자주 울림
- 사용자 영향 없음
- 담당자 불명확
- 임계치가 너무 낮음
- 매 배포마다 반복 발생

---

### [FAQ]

Q. 좋은 Alert의 기준은?

A.
사용자 영향이 있고 즉시 행동이 필요하며 담당자와 Runbook이 명확해야 한다.

Q. Alert Fatigue는 무엇인가?

A.
불필요하거나 반복적인 알림이 많아져 중요한 알림을 놓치게 되는 현상이다.

---

# 15. SLI / SLO / SLA Rules

## 15.1 SLI / SLO / SLA 작성 규칙

### [개념]

SLI, SLO, SLA는 서비스 신뢰성을 측정하고 관리하기 위한 기준이다.

- SLI: Service Level Indicator
- SLO: Service Level Objective
- SLA: Service Level Agreement

---

### [핵심]

구분:

| 용어 | 의미      | 예                |
| ---- | --------- | ----------------- |
| SLI  | 측정 지표 | 요청 성공률       |
| SLO  | 내부 목표 | 성공률 99.9%      |
| SLA  | 외부 계약 | 미달 시 보상 조건 |

---

### [실무]

대표 SLI:

- Availability
- Request Success Rate
- Latency
- Error Rate
- Durability
- Freshness

SLO 예시:

```text
API 요청의 99.9%는 30일 기준 성공해야 한다.
API 요청의 95%는 300ms 이하로 응답해야 한다.
```

---

### [주의]

SLO는 너무 높게 잡으면 운영 부담이 과도해진다.

SLO는 사용자 경험과 운영 비용 사이의 균형이 필요하다.

---

### [FAQ]

Q. SLI와 SLO 차이는?

A.
SLI는 측정 지표이고 SLO는 그 지표에 대한 목표값이다.

Q. SLA는 무엇인가?

A.
고객이나 외부 사용자와 약속한 서비스 수준 계약이다.

---

# 16. Dashboard Rules

## 16.1 Dashboard 작성 규칙

### [개념]

Dashboard는 시스템 상태, 장애 징후, 배포 영향, 비즈니스 흐름을 시각적으로 확인하는 운영 화면이다.

---

### [핵심]

필수 포함:

- Service Dashboard
- Infrastructure Dashboard
- Deployment Dashboard
- Business Dashboard
- Error Dashboard
- Latency Dashboard

---

### [실무]

Service Dashboard 구성:

- Request Rate
- Error Rate
- P95 / P99 Latency
- HTTP Status Code
- Top Error Endpoint
- Dependency Error
- Recent Deployment Version

Infrastructure Dashboard 구성:

- CPU
- Memory
- Disk
- Network
- Container Restart
- Pod Status
- Node Pressure

Business Dashboard 구성:

- Login Success Rate
- Signup Rate
- Payment Success Rate
- Order Count
- Search Success Rate
- AI Recommendation Success Rate

---

### [Best Practice]

Dashboard는 목적별로 분리한다.

- 장애 대응용 Dashboard
- 배포 검증용 Dashboard
- 용량 계획용 Dashboard
- 비즈니스 지표 Dashboard

---

### [FAQ]

Q. Dashboard는 왜 필요한가?

A.
서비스 상태와 장애 징후를 빠르게 파악하고 배포 영향과 사용자 영향을 확인하기 위해 필요하다.

Q. 좋은 Dashboard의 기준은?

A.
장애 상황에서 원인 후보를 빠르게 좁힐 수 있고, 핵심 지표가 목적별로 정리되어 있어야 한다.

---

# 17. Health Check Rules

## 17.1 Health Check 작성 규칙

### [개념]

Health Check는 서비스가 정상적으로 실행되고 요청을 처리할 준비가 되었는지 확인하는 검사이다.

---

### [핵심]

필수 포함:

- Health Check
- Readiness
- Liveness
- Startup
- Dependency Health
- Synthetic Check

---

### [실무]

Health Check 유형:

| 유형       | 목적                          |
| ---------- | ----------------------------- |
| Liveness   | 프로세스 생존 확인            |
| Readiness  | 트래픽 수신 가능 확인         |
| Startup    | 초기 구동 완료 확인           |
| Dependency | DB, Redis, 외부 API 연결 확인 |
| Synthetic  | 실제 사용자 흐름 모사         |

Spring Boot Actuator 예시:

```text
/actuator/health
/actuator/health/readiness
/actuator/health/liveness
```

---

### [주의]

Health Check가 너무 깊으면 외부 장애가 App 전체 장애로 오판될 수 있다.

Readiness와 Liveness 기준을 분리해야 한다.

---

### [FAQ]

Q. Health Check는 Monitoring과 어떻게 연결되는가?

A.
Health Check 결과를 Load Balancer, Kubernetes, Alerting, 배포 검증에 활용한다.

Q. Liveness Check에 DB 연결 검사를 넣어도 되는가?

A.
주의해야 한다. DB 일시 장애로 애플리케이션이 반복 재시작될 수 있으므로 Readiness와 분리하는 것이 좋다.

---

# 18. Docker Logging / Monitoring Rules

## 18.1 Docker 관측 규칙

### [개념]

Docker Monitoring & Logging은 Container의 상태, 자원 사용량, 표준 출력 로그를 관측하는 기준이다.

---

### [핵심]

필수 포함:

- docker logs
- docker stats
- stdout
- stderr
- log driver
- container restart
- healthcheck
- resource limit

---

### [실무]

기본 명령:

```bash
docker ps
docker logs app
docker logs -f app
docker stats
docker inspect app
```

Docker 운영 로그 기준:

- Application Log는 stdout / stderr 출력
- Log Rotation 설정 검토
- Container 내부 파일 로그 단독 의존 금지
- Container Restart Count 확인
- Memory Limit과 OOM Kill 확인

---

### [주의]

Container 내부에만 저장된 로그는 Container 삭제 시 손실될 수 있다.

운영 환경에서는 중앙 로그 수집을 권장한다.

---

### [FAQ]

Q. Docker Container 로그는 어떻게 확인하는가?

A.
`docker logs containerName` 명령으로 확인한다.

Q. Docker에서 Application Log는 어디로 출력하는 것이 좋은가?

A.
stdout / stderr로 출력하여 Docker Logging Driver나 중앙 로그 시스템이 수집하도록 하는 것이 좋다.

---

# 19. Kubernetes Monitoring / Logging Rules

## 19.1 Kubernetes 관측 규칙

### [개념]

Kubernetes Monitoring & Logging은 Pod, Node, Deployment, Service, Ingress, Cluster 상태를 관측하는 기준이다.

---

### [핵심]

필수 포함:

- Pod Status
- Node Status
- Deployment Rollout
- Restart Count
- CrashLoopBackOff
- OOMKilled
- Events
- kubectl logs
- Metrics Server
- Prometheus
- Grafana
- Loki / ELK

---

### [실무]

기본 확인 명령:

```bash
kubectl get pods
kubectl describe pod pod-name
kubectl logs pod-name
kubectl logs -f deployment/my-app
kubectl top pod
kubectl top node
kubectl get events
kubectl rollout status deployment/my-app
```

Kubernetes Dashboard 지표:

- Pod Restart Count
- Pod Ready 상태
- CPU / Memory Usage
- Node Pressure
- Deployment Available Replicas
- Ingress 5xx Rate
- Service Latency
- HPA Scaling 상태

---

### [주의]

Pod가 Running이어도 Ready가 아닐 수 있다.

CrashLoopBackOff는 로그, 이벤트, 환경 변수, Secret, ConfigMap, Resource Limit을 함께 확인해야 한다.

---

### [FAQ]

Q. Kubernetes에서 장애 확인 첫 단계는?

A.
Pod 상태, Events, Logs, Rollout 상태를 먼저 확인한다.

Q. CrashLoopBackOff는 무엇인가?

A.
Container가 반복적으로 시작에 실패하고 재시작되는 상태이다.

---

# 20. Application Monitoring Rules

## 20.1 Application Monitoring 작성 규칙

### [개념]

Application Monitoring은 애플리케이션 내부 동작, API 상태, 비즈니스 기능 성공 여부를 관측하는 것이다.

---

### [핵심]

필수 포함:

- API Metrics
- Error Rate
- Latency
- Request Count
- Business Transaction
- Dependency Call
- Exception Count
- Thread Pool
- Connection Pool

---

### [실무]

Spring Boot Application Monitoring 대상:

- Actuator Health
- HTTP Server Requests
- JVM Memory
- JVM GC
- Thread Count
- Tomcat Thread Pool
- HikariCP Connection Pool
- Exception Count
- External API Call Latency
- Scheduled Job Success / Failure

비즈니스 기능 Monitoring 대상:

- Login Success / Failure
- Signup Success / Failure
- Payment Success / Failure
- Chat Message Send Failure
- File Upload Failure
- AI Recommendation Failure
- Notification Send Failure

---

### [FAQ]

Q. Application Monitoring은 서버 Monitoring과 무엇이 다른가?

A.
서버 Monitoring은 CPU, Memory 같은 자원 상태를 보고 Application Monitoring은 API, 오류, Latency, 비즈니스 기능 상태를 본다.

Q. JVM 애플리케이션에서 봐야 할 지표는?

A.
Heap Memory, GC, Thread, Connection Pool, HTTP Latency, Error Rate를 확인해야 한다.

---

# 21. Infrastructure Monitoring Rules

## 21.1 Infrastructure Monitoring 작성 규칙

### [개념]

Infrastructure Monitoring은 서버, 네트워크, 디스크, 컨테이너, 클러스터 같은 실행 기반 자원의 상태를 관측하는 것이다.

---

### [핵심]

필수 포함:

- CPU
- Memory
- Disk
- Network
- Process
- File Descriptor
- Container
- Node
- Load Average

---

### [실무]

확인 지표:

- CPU Usage
- Memory Usage
- Disk Usage
- Disk I/O
- Network In / Out
- Network Error
- Load Average
- Process Count
- Open File Count
- Container CPU / Memory
- Node Condition
- Host Uptime

---

### [주의]

인프라 지표만 정상이어도 애플리케이션 장애가 발생할 수 있다.

Application Metric과 Business Metric을 함께 확인해야 한다.

---

### [FAQ]

Q. Infrastructure Monitoring은 무엇을 확인하는가?

A.
서버, 컨테이너, 네트워크, 디스크, 클러스터 자원 상태를 확인한다.

Q. CPU와 Memory가 정상인데 서비스가 느릴 수 있는가?

A.
가능하다. DB Lock, 외부 API 지연, Connection Pool 고갈, 코드 병목이 원인일 수 있다.

---

# 22. Database Monitoring Rules

## 22.1 Database Monitoring 작성 규칙

### [개념]

Database Monitoring은 DB 성능, 연결 상태, 쿼리 지연, Lock, 저장소 상태를 관측하는 것이다.

---

### [핵심]

필수 포함:

- Connection Count
- Connection Pool
- Slow Query
- Query Latency
- Lock Wait
- Deadlock
- Replication Lag
- Disk Usage
- Index Usage
- Transaction

---

### [실무]

DB Monitoring 지표:

- Active Connection
- Max Connection Usage
- Slow Query Count
- Query P95 / P99 Latency
- Lock Wait Time
- Deadlock Count
- Buffer Pool Hit Ratio
- Disk Usage
- IOPS
- Replication Lag
- Backup Status

Application 연계 지표:

- HikariCP Active Connection
- HikariCP Pending Thread
- DB Timeout Count
- Transaction Rollback Count

---

### [주의]

DB 장애는 API Latency와 Error Rate로 먼저 나타날 수 있다.

DB Monitoring과 Application Monitoring을 함께 봐야 한다.

---

### [FAQ]

Q. DB Connection Pool 고갈은 어떻게 감지하는가?

A.
Active Connection, Pending Thread, Timeout Count, API Latency 증가를 함께 확인한다.

Q. Slow Query는 왜 중요한가?

A.
API Latency 증가, DB 부하, Lock 대기, 사용자 경험 저하의 원인이 될 수 있다.

---

# 23. Log Aggregation Rules

## 23.1 Log Aggregation 작성 규칙

### [개념]

Log Aggregation은 여러 서버, 컨테이너, 서비스에서 발생한 로그를 중앙 저장소로 수집하는 방식이다.

---

### [핵심]

필수 포함:

- Log Collector
- Log Shipper
- Centralized Logging
- Log Storage
- Log Query
- Log Retention
- Index
- Search

---

### [실무]

대표 구성:

```text
Application
→ stdout / file
→ Collector
→ Log Storage
→ Query / Dashboard / Alert
```

도구 예시:

- Loki
- Elasticsearch
- OpenSearch
- Fluent Bit
- Fluentd
- Logstash
- Filebeat
- Vector

---

### [Best Practice]

- Service / Environment 필드를 반드시 포함한다.
- JSON Structured Logging을 우선한다.
- 로그 보존 기간을 정한다.
- 민감 정보 마스킹을 적용한다.
- Error Log와 Access Log 검색 기준을 통일한다.
- Log Volume 폭증에 대비한다.

---

### [FAQ]

Q. Log Aggregation이 필요한 이유는?

A.
여러 서버와 컨테이너에 흩어진 로그를 한 곳에서 검색하고 분석하기 위해 필요하다.

Q. 로그 보존 기간은 왜 정해야 하는가?

A.
저장 비용, 보안 정책, 감사 요구사항, 장애 분석 가능 기간을 균형 있게 관리하기 위해 필요하다.

---

# 24. Log Rotation / Retention Rules

## 24.1 Log Rotation / Retention 작성 규칙

### [개념]

Log Rotation은 로그 파일이 무한히 커지는 것을 방지하기 위해 크기나 시간 기준으로 파일을 분리하고 오래된 로그를 삭제 또는 보관하는 방식이다.

Log Retention은 로그를 얼마나 오래 보관할지 정하는 정책이다.

---

### [핵심]

필수 포함:

- Log Rotation
- Retention Period
- Compression
- Archive
- Disk Usage
- Compliance
- Cost Control

---

### [실무]

Retention 기준:

| 로그 유형       | 보존 기준               |
| --------------- | ----------------------- |
| Debug Log       | 짧게 보관               |
| Application Log | 운영 분석 기간 기준     |
| Error Log       | 장애 분석 기준          |
| Access Log      | 트래픽 분석 / 보안 기준 |
| Audit Log       | 규정 / 감사 기준        |

Docker Logging 옵션 예시:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "5"
  }
}
```

---

### [주의]

Log Rotation이 없으면 Disk Full로 서비스 장애가 발생할 수 있다.

Audit Log는 임의 삭제를 방지해야 한다.

---

### [FAQ]

Q. Log Rotation은 왜 필요한가?

A.
로그 파일이 디스크를 가득 채워 서비스 장애를 일으키는 것을 방지하기 위해 필요하다.

Q. 모든 로그를 오래 보관해야 하는가?

A.
아니다. 로그 유형, 비용, 보안, 감사 요구사항에 따라 보존 기간을 다르게 설정해야 한다.

---

# 25. Security / Audit Logging Rules

## 25.1 Security / Audit Logging 작성 규칙

### [개념]

Security Logging과 Audit Logging은 보안 이벤트, 권한 변경, 인증 실패, 관리자 작업을 추적하기 위한 로그이다.

---

### [핵심]

필수 포함:

- Authentication Event
- Authorization Failure
- Admin Action
- Permission Change
- Secret Access
- Audit Trail
- Tamper Resistance
- PII Masking

---

### [실무]

Audit Log 대상:

- 로그인 성공 / 실패
- 비밀번호 변경
- 권한 변경
- 관리자 기능 실행
- 결제 상태 변경
- 데이터 삭제
- Secret 조회
- 배포 승인
- 인프라 변경
- 보안 설정 변경

Audit Log 필드:

- actor
- action
- target
- timestamp
- sourceIp
- result
- reason
- traceId

---

### [주의]

Audit Log는 조작 방지와 접근 권한 제한이 중요하다.

개인정보와 민감 정보는 마스킹한다.

---

### [FAQ]

Q. Audit Log는 왜 필요한가?

A.
누가 언제 어떤 중요한 작업을 수행했는지 추적하고 보안 사고와 운영 사고를 분석하기 위해 필요하다.

Q. Audit Log에도 개인정보를 그대로 남겨도 되는가?

A.
권장하지 않는다. 필요한 최소 정보만 남기고 개인정보는 마스킹해야 한다.

---

# 26. Deployment Verification Rules

## 26.1 배포 검증 관측 규칙

### [개념]

Deployment Verification은 배포 후 지표와 로그를 확인하여 새 버전이 정상 동작하는지 판단하는 과정이다.

---

### [핵심]

필수 포함:

- Post-deploy Monitoring
- Release Version
- Error Rate
- Latency
- Traffic
- Business Metric
- Log Error Pattern
- Rollback Signal

---

### [실무]

배포 후 확인 순서:

```text
Deployment Complete
→ Health Check
→ Smoke Test
→ Error Rate
→ Latency
→ Logs
→ Business Metric
→ Alert Status
→ Release Complete or Rollback
```

배포 검증 지표:

- HTTP 5xx Rate
- API P95 / P99 Latency
- Pod Restart Count
- Error Log Count
- Payment Failure Rate
- Login Failure Rate
- External API Failure
- DB Connection Timeout
- Queue Lag
- User Complaint

---

### [주의]

배포 직후 5분만 보고 종료하지 않는다.

Canary, Blue-Green, Rolling 전략에 따라 충분한 관측 기간을 둔다.

---

### [FAQ]

Q. 배포 후 Monitoring에서 가장 먼저 볼 것은?

A.
Health Check, Error Rate, Latency, 로그 오류 패턴, 핵심 Business Metric을 먼저 확인한다.

Q. 배포 후 기술 지표가 정상인데도 장애일 수 있는가?

A.
가능하다. 결제 성공률, 로그인 성공률, 주문 수 같은 Business Metric이 깨질 수 있다.

---

# 27. Incident Response Rules

## 27.1 Incident Response 작성 규칙

### [개념]

Incident Response는 장애를 감지한 뒤 영향 범위를 파악하고 복구하며 원인을 분석하는 운영 절차이다.

---

### [핵심]

필수 포함:

- Incident
- Detection
- Triage
- Mitigation
- Communication
- Recovery
- Postmortem
- Action Item

---

### [Flow]

```text
Alert
→ Triage
→ Impact Assessment
→ Mitigation
→ Recovery
→ Postmortem
→ Prevention
```

---

### [실무]

Incident 대응 순서:

1. Alert 확인
2. 사용자 영향 범위 확인
3. 최근 배포 / 설정 변경 확인
4. Dashboard 지표 확인
5. Error Log 확인
6. Dependency 상태 확인
7. Rollback / Traffic 우회 / Scale Out 판단
8. 복구 확인
9. 원인 분석
10. 재발 방지 Action Item 작성

---

### [FAQ]

Q. 장애 대응에서 가장 먼저 할 일은?

A.
사용자 영향 범위와 서비스 핵심 기능 장애 여부를 확인하고, 최근 변경 사항을 함께 확인한다.

Q. 장애 중 원인 분석과 복구 중 무엇이 우선인가?

A.
사용자 영향이 크면 완전한 원인 분석보다 우선 복구와 영향 완화가 먼저이다.

---

# 28. Postmortem Rules

## 28.1 Postmortem 작성 규칙

### [개념]

Postmortem은 장애 발생 후 원인, 영향, 대응, 재발 방지책을 정리하는 문서이다.

목적은 책임 추궁이 아니라 시스템 개선이다.

---

### [핵심]

필수 포함:

- Incident Summary
- Timeline
- Impact
- Root Cause
- Detection
- Mitigation
- What Went Well
- What Went Wrong
- Action Items
- Prevention

---

### [실무]

Postmortem 항목:

```text
Summary:
Impact:
Timeline:
Root Cause:
Detection:
Resolution:
What went well:
What went wrong:
Action items:
Owner:
Due date:
```

좋은 Action Item:

- 구체적
- 담당자 있음
- 완료 기준 명확
- 재발 방지와 연결
- 우선순위 있음

---

### [FAQ]

Q. Postmortem은 왜 작성하는가?

A.
장애 원인과 대응 과정을 기록하고 재발 방지 Action Item을 만들기 위해 작성한다.

Q. Postmortem은 누군가의 책임을 묻기 위한 문서인가?

A.
아니다. 시스템과 프로세스를 개선하기 위한 문서이다.

---

# 29. Tooling Rules

## 29.1 Monitoring & Logging 도구 작성 규칙

### [개념]

Monitoring & Logging 도구는 Metrics, Logs, Traces를 수집, 저장, 시각화, 알림으로 연결하는 역할을 한다.

---

### [핵심]

대표 도구:

| 영역             | 도구                                               |
| ---------------- | -------------------------------------------------- |
| Metrics          | Prometheus                                         |
| Dashboard        | Grafana                                            |
| Logs             | Loki, ELK, OpenSearch                              |
| Tracing          | Jaeger, Tempo                                      |
| Instrumentation  | OpenTelemetry                                      |
| Alerting         | Alertmanager, Grafana Alerting                     |
| Cloud Monitoring | CloudWatch, Azure Monitor, Google Cloud Monitoring |

---

### [실무]

도구 선택 기준:

- 운영 환경 규모
- Kubernetes 사용 여부
- 로그 저장 비용
- Query 성능
- 알림 연계
- Cloud Provider 연계
- OpenTelemetry 지원
- 팀 운영 난이도

---

### [FAQ]

Q. Prometheus와 Grafana는 각각 무엇인가?

A.
Prometheus는 Metrics 수집과 저장에 강하고, Grafana는 Dashboard와 시각화에 강하다.

Q. OpenTelemetry는 무엇인가?

A.
Metrics, Logs, Traces를 표준 방식으로 수집하고 전달하기 위한 Observability 표준 도구 체계이다.

---

# 30. Troubleshooting Rules

## 30.1 Monitoring & Logging Troubleshooting 작성 규칙

### [개념]

Troubleshooting 문서는 문제, 원인, 해결 형식으로 작성한다.

형식:

```text
문제:
원인:
해결:
```

---

### [핵심]

반드시 포함할 문제:

- Metrics Missing
- Logs Missing
- Trace Missing
- Alert Not Firing
- Alert Too Noisy
- Dashboard Empty
- Log Query Slow
- High Cardinality
- Disk Full by Logs
- Health Check False Positive
- Deployment Issue Not Detected
- Kubernetes Pod Logs Missing
- Prometheus Scrape Failed
- Grafana Dashboard Broken

---

### [실무]

기본 확인 흐름:

```text
Signal Missing
→ Target Status
→ Collector Status
→ Permission
→ Network
→ Label / Query
→ Storage
→ Dashboard
→ Alert Rule
```

기본 확인 대상:

- 수집 대상이 살아있는가
- Exporter가 동작하는가
- Scrape 설정이 맞는가
- 로그 Collector가 실행 중인가
- Label이 변경되었는가
- Dashboard Query가 맞는가
- Retention으로 삭제된 것은 아닌가
- 권한 문제는 없는가

---

### [Troubleshooting]

문제:
Metrics가 수집되지 않는다.

원인:

- Exporter 미실행
- Scrape Target 설정 오류
- Network 차단
- 인증 실패
- Endpoint 경로 오류
- Label 설정 오류

해결:

```text
Target 상태 확인
→ Exporter 로그 확인
→ Scrape 설정 확인
→ Network 확인
→ Endpoint 직접 호출
```

문제:
로그가 검색되지 않는다.

원인:

- Application이 stdout / stderr로 출력하지 않음
- Log Collector 미실행
- Label 누락
- Index 지연
- Retention 만료
- Query 조건 오류

해결:

```text
Application 로그 출력 확인
→ Collector 상태 확인
→ Label 확인
→ Time Range 확인
→ Query 조건 단순화
```

문제:
Alert가 너무 자주 울린다.

원인:

- 임계치가 너무 낮음
- 지속 시간 조건 없음
- 중복 Alert
- 사용자 영향 없는 지표 Alert
- 배포 중 일시 변동 미고려

해결:

```text
Threshold 조정
→ For Duration 추가
→ Severity 조정
→ 중복 Rule 제거
→ Runbook 연결
```

문제:
배포 장애가 Monitoring에 잡히지 않는다.

원인:

- Business Metric 누락
- Error Rate 기준 부적절
- Health Check가 너무 얕음
- Canary 대상 지표 분리 안 됨
- Alert Rule 미설정

해결:

```text
Business Metric 추가
→ Error Rate / Latency Alert 조정
→ Synthetic Check 추가
→ 배포 버전 Label 추가
```

---

### [FAQ]

Q. Metrics가 안 보일 때 첫 확인 대상은?

A.
수집 대상, Exporter, Scrape 설정, Network, Endpoint 상태를 먼저 확인한다.

Q. 로그가 안 보일 때 첫 확인 대상은?

A.
애플리케이션 로그 출력, Log Collector 상태, Label, Time Range, Query 조건을 확인한다.

Q. Alert가 너무 많으면 어떻게 해야 하는가?

A.
Threshold, 지속 시간, Severity, 중복 Rule, 사용자 영향 여부를 기준으로 정리한다.

---

# 31. Common Mistakes

## 31.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 Monitoring & Logging 구성을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- Health Check만 있고 Monitoring 없음
- 서버 CPU만 보고 서비스 정상 판단
- Error Rate Alert 누락
- Latency Percentile 미확인
- Business Metric 미관측
- 로그에 Secret / Token 출력
- Correlation ID 없음
- JSON Structured Logging 미사용
- 로그 보존 정책 없음
- Log Rotation 미설정
- Alert가 너무 많음
- Runbook 없는 Alert
- Dashboard만 있고 Alert 없음
- 배포 버전 Label 없음
- Canary 지표 분리 없음
- Kubernetes Event 미확인
- DB Connection Pool 지표 누락
- 외부 API 지표 누락
- Postmortem 미작성

---

### [실무]

Review Agent 검토 기준:

```text
Monitoring Target
→ Metrics
→ Logs
→ Traces
→ Dashboard
→ Alert
→ Runbook
→ Incident Flow
→ Postmortem
```

---

### [FAQ]

Q. Monitoring Review에서 가장 먼저 확인할 것은?

A.
Error Rate, Latency, Traffic, Saturation, Health Check, Alert Rule, 로그 검색 가능성, Correlation ID를 먼저 확인한다.

Q. Logging Review에서 가장 위험한 문제는?

A.
Secret, Token, 개인정보가 로그에 남는 것과 장애 분석에 필요한 Trace ID / Request ID가 없는 것이다.

---

# 32. File Relationship Rules

## 32.1 다른 Domain Rules와 연계

### [개념]

Monitoring & Logging Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Docker Advanced, Infrastructure as Code, Deployment Strategy, Kubernetes, Security Operations와 연결된다.

---

### [핵심]

연계 구조:

```text
Application / Infrastructure
→ Docker / Kubernetes Runtime
→ Monitoring & Logging
→ Alerting
→ Incident Response
→ Deployment / CI/CD Feedback
```

---

### [실무]

파일 간 역할 분리:

| Domain                 | 역할                                                |
| ---------------------- | --------------------------------------------------- |
| Monitoring & Logging   | Metrics, Logs, Traces, Alert, Dashboard, Incident   |
| CI/CD                  | 배포 Pipeline, 검증 단계, 품질 Gate                 |
| Docker Advanced        | Container Logs, Resource Usage, Healthcheck         |
| Infrastructure as Code | Monitoring Resource Provisioning, Alert Rule 코드화 |
| Deployment Strategy    | 배포 후 검증, Rollback Signal                       |
| Kubernetes             | Pod / Node / Service / Ingress 관측 구현            |
| Security Operations    | Audit Log, Security Alert, Incident 대응            |

---

### [FAQ]

Q. Monitoring & Logging과 Deployment Strategy는 어떻게 연결되는가?

A.
배포 후 Error Rate, Latency, Logs, Business Metric을 확인하여 성공, Rollback, Roll Forward를 판단하는 데 연결된다.

Q. Monitoring & Logging과 Docker Advanced는 어떻게 연결되는가?

A.
Container logs, docker stats, Healthcheck, Resource Limit, Restart Count 관측에서 연결된다.

Q. Monitoring & Logging과 Kubernetes는 어떻게 연결되는가?

A.
Pod 상태, Node 상태, Events, Logs, Metrics, Rollout 상태 관측에서 연결된다.

---

# 33. Retrieval Optimization Rules

## 33.1 Retrieval 최적화 규칙

### [개념]

Monitoring & Logging 문서는 운영 문제 상황 검색에 강해야 한다.

사용자 질문은 주로 로그 확인, 지표 누락, 알림, 배포 장애, 성능 저하, Kubernetes 상태 확인 형태로 들어온다.

---

### [핵심]

강조 대상:

- Monitoring
- Logging
- Observability
- Metrics
- Logs
- Traces
- Alerting
- Dashboard
- Error Rate
- Latency
- Health Check
- Structured Logging
- Correlation ID
- SLI
- SLO
- Incident Response
- Postmortem
- Prometheus
- Grafana
- Loki
- ELK
- OpenTelemetry
- Kubernetes Monitoring
- Docker Logging

---

### [실무]

반복 허용 키워드:

- Monitoring 설정
- Logging 전략
- Observability 구성
- Metrics 수집
- Logs 검색
- Traces 추적
- Alert Rule
- Dashboard 구성
- Error Rate 증가
- Latency 증가
- Health Check 실패
- Structured Logging
- Correlation ID
- Kubernetes Pod Logs
- Docker Container Logs
- Deployment Verification
- Incident Response
- Postmortem 작성

---

### [FAQ]

Q. Monitoring & Logging RAG 문서는 어떤 질문에 강해야 하는가?

A.
성능 저하, 로그 검색, Metrics 누락, Alert 설정, 배포 검증, 장애 분석, Kubernetes / Docker 관측 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
Monitoring, Logging, Metrics, Logs, Traces, Alert, Dashboard, Error Rate, Latency, Health Check, Correlation ID, Incident 키워드를 반복할 수 있다.

---

# 34. Version Rules

## 34.1 버전 기준

### [개념]

Monitoring & Logging 문서는 Modern Observability 기준으로 작성한다.

---

### [핵심]

기준:

- Metrics / Logs / Traces 통합 관측
- Prometheus / Grafana 기반 Metrics
- Loki / ELK / OpenSearch 기반 Logging
- OpenTelemetry 기반 표준 수집
- Kubernetes Observability
- Container Logging
- SLO 기반 운영
- Alert Fatigue 감소
- Incident Response / Postmortem

---

### [실무]

Legacy 또는 낮은 우선순위:

- 서버 접속 후 로그 파일만 직접 확인
- CPU만 기준으로 장애 판단
- Alert 없이 Dashboard만 운영
- 모든 로그를 문자열로만 출력
- Correlation ID 없는 분산 시스템
- 로그에 Secret 출력
- Postmortem 없는 장애 대응
- 배포 후 수동 확인만 수행

---

### [FAQ]

Q. Monitoring & Logging 문서에서 Modern 기준은 무엇인가?

A.
Metrics, Logs, Traces를 함께 사용하고, Alerting, Dashboard, Incident Response, SLO 기반 운영을 포함하는 것이다.

Q. 서버 로그 파일 직접 확인만으로 충분한가?

A.
운영 환경에서는 부족하다. 중앙 로그 수집, Metrics, Alert, Dashboard, Trace 체계가 필요하다.

---

# 35. Quality Checklist

## 35.1 최종 검수 기준

### [개념]

Monitoring & Logging RAG 문서는 Agent가 서비스 상태를 관측하고 장애를 분석할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Monitoring & Logging Scope 충족
- CI/CD Domain Rules와 연결
- Docker Advanced Domain Rules와 연결
- Infrastructure as Code Domain Rules와 연결
- Deployment Strategy Domain Rules와 연결
- Kubernetes Domain Rules와 연결
- FAQ 포함
- Retrieval Queries 포함
- Metrics / Logs / Traces 포함
- Alerting / Dashboard 포함
- SLI / SLO / SLA 포함
- Structured Logging 포함
- Correlation ID 포함
- Incident Response / Postmortem 포함
- Deployment Verification 포함
- Troubleshooting 포함
- Secret Logging 금지 강조
- 용어 통일
- 긴 서술 최소화
- 코드블록 id 제거
- [FAQ] 내부 구분선 남발 없음
- 오타 최소화

---

### [실무]

품질 목표:

- Minimum: 95/100
- Target: 97+/100

---

### [FAQ]

Q. Monitoring & Logging 문서 품질은 무엇으로 판단하는가?

A.
Agent가 지표 설계, 로그 전략, 알림 기준, 배포 검증, 장애 분석, Incident 대응을 수행할 수 있으면 품질이 높다.

---

# 36. Final Goal

## 36.1 최종 목표

### [개념]

Monitoring & Logging RAG 문서는 단순 로그 확인 문서가 아니다.

DevOps Agent / Backend Agent / Review Agent가 운영 시스템을 관측하고 장애를 감지, 분석, 복구, 재발 방지하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Monitoring Workflow
- Design Metrics
- Design Logging Strategy
- Review Structured Logging
- Trace Request Flow
- Define Alert Rules
- Build Dashboard Criteria
- Verify Deployment Health
- Detect Incident
- Troubleshoot Runtime Issues
- Support Postmortem
- Connect Monitoring with CI/CD / Deployment / Kubernetes

---

### [실무]

최종 연결 흐름:

```text
Application Change
→ Deployment
→ Metrics / Logs / Traces
→ Dashboard
→ Alert
→ Incident Response
→ Rollback or Recovery
→ Postmortem
→ Prevention
```

---

### [FAQ]

Q. Monitoring & Logging 문서의 최종 목적은?

A.
Agent가 운영 시스템을 관측하고, 장애를 빠르게 감지하며, 원인을 분석하고, 재발 방지까지 수행하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Monitoring & Logging Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 Metrics, Logs, Traces, Alert, Dashboard, Incident 대응을 수행하기 위한 RAG 작성 규칙이다.

Q. Monitoring & Logging 문서의 핵심 범위는?
A. Monitoring, Logging, Observability, Metrics, Logs, Traces, Alerting, Dashboard, SLI / SLO / SLA, Incident Response, Postmortem이다.

Q. Monitoring과 Logging은 무엇이 다른가?
A. Monitoring은 지표 기반 상태 관측이고 Logging은 이벤트와 실행 기록 기반 분석이다.

Q. Observability의 3대 요소는 무엇인가?
A. Metrics, Logs, Traces이다.

Q. Metrics는 무엇인가?
A. 시스템 상태를 숫자로 표현한 시계열 데이터이다.

Q. Logs는 언제 보는가?
A. Metrics에서 이상을 발견한 뒤 구체적인 오류 원인, 요청 흐름, 예외 Stack Trace를 확인할 때 본다.

Q. Distributed Tracing은 왜 필요한가?
A. 분산 시스템에서 요청이 어떤 서비스에서 지연되거나 실패했는지 파악하기 위해 필요하다.

Q. Golden Signals는 무엇인가?
A. 서비스 상태를 빠르게 판단하기 위한 핵심 지표로 Latency, Traffic, Errors, Saturation을 의미한다.

Q. 배포 후 가장 먼저 볼 Golden Signals는?
A. Error Rate, P95 / P99 Latency, Traffic 변화, Saturation 지표를 먼저 확인한다.

Q. Log Level은 어떻게 구분하는가?
A. TRACE, DEBUG, INFO, WARN, ERROR로 구분하며 운영에서는 INFO, WARN, ERROR를 주로 사용한다.

Q. 운영 환경에서 DEBUG 로그를 항상 켜도 되는가?
A. 권장하지 않는다. 로그 비용, 성능 저하, 민감 정보 노출 위험이 증가할 수 있다.

Q. Structured Logging은 왜 필요한가?
A. 로그를 필드 기반으로 검색, 집계, 필터링할 수 있어 장애 분석과 Dashboard 구성이 쉬워진다.

Q. Correlation ID는 왜 필요한가?
A. 여러 서비스와 로그에 흩어진 하나의 요청 흐름을 추적하기 위해 필요하다.

Q. Alerting은 무엇인가?
A. 시스템 이상이 발생했을 때 담당자에게 자동으로 알리는 운영 체계이다.

Q. 좋은 Alert의 기준은?
A. 사용자 영향이 있고 즉시 행동이 필요하며 담당자와 Runbook이 명확해야 한다.

Q. Alert Fatigue는 무엇인가?
A. 불필요하거나 반복적인 알림이 많아져 중요한 알림을 놓치게 되는 현상이다.

Q. SLI와 SLO 차이는?
A. SLI는 측정 지표이고 SLO는 그 지표에 대한 목표값이다.

Q. SLA는 무엇인가?
A. 고객이나 외부 사용자와 약속한 서비스 수준 계약이다.

Q. Dashboard는 왜 필요한가?
A. 서비스 상태와 장애 징후를 빠르게 파악하고 배포 영향과 사용자 영향을 확인하기 위해 필요하다.

Q. 좋은 Dashboard의 기준은?
A. 장애 상황에서 원인 후보를 빠르게 좁힐 수 있고, 핵심 지표가 목적별로 정리되어 있어야 한다.

Q. Health Check는 Monitoring과 어떻게 연결되는가?
A. Health Check 결과를 Load Balancer, Kubernetes, Alerting, 배포 검증에 활용한다.

Q. Liveness Check에 DB 연결 검사를 넣어도 되는가?
A. 주의해야 한다. DB 일시 장애로 애플리케이션이 반복 재시작될 수 있으므로 Readiness와 분리하는 것이 좋다.

Q. Docker Container 로그는 어떻게 확인하는가?
A. `docker logs containerName` 명령으로 확인한다.

Q. Docker에서 Application Log는 어디로 출력하는 것이 좋은가?
A. stdout / stderr로 출력하여 Docker Logging Driver나 중앙 로그 시스템이 수집하도록 하는 것이 좋다.

Q. Kubernetes에서 장애 확인 첫 단계는?
A. Pod 상태, Events, Logs, Rollout 상태를 먼저 확인한다.

Q. CrashLoopBackOff는 무엇인가?
A. Container가 반복적으로 시작에 실패하고 재시작되는 상태이다.

Q. Application Monitoring은 서버 Monitoring과 무엇이 다른가?
A. 서버 Monitoring은 CPU, Memory 같은 자원 상태를 보고 Application Monitoring은 API, 오류, Latency, 비즈니스 기능 상태를 본다.

Q. JVM 애플리케이션에서 봐야 할 지표는?
A. Heap Memory, GC, Thread, Connection Pool, HTTP Latency, Error Rate를 확인해야 한다.

Q. DB Connection Pool 고갈은 어떻게 감지하는가?
A. Active Connection, Pending Thread, Timeout Count, API Latency 증가를 함께 확인한다.

Q. Slow Query는 왜 중요한가?
A. API Latency 증가, DB 부하, Lock 대기, 사용자 경험 저하의 원인이 될 수 있다.

Q. Log Aggregation이 필요한 이유는?
A. 여러 서버와 컨테이너에 흩어진 로그를 한 곳에서 검색하고 분석하기 위해 필요하다.

Q. Log Rotation은 왜 필요한가?
A. 로그 파일이 디스크를 가득 채워 서비스 장애를 일으키는 것을 방지하기 위해 필요하다.

Q. Audit Log는 왜 필요한가?
A. 누가 언제 어떤 중요한 작업을 수행했는지 추적하고 보안 사고와 운영 사고를 분석하기 위해 필요하다.

Q. 로그에 Access Token을 남겨도 되는가?
A. 금지한다. Token은 인증 권한 탈취로 이어질 수 있으므로 절대 로그에 남기지 않는다.

Q. 배포 후 Monitoring에서 가장 먼저 볼 것은?
A. Health Check, Error Rate, Latency, 로그 오류 패턴, 핵심 Business Metric을 먼저 확인한다.

Q. 장애 대응에서 가장 먼저 할 일은?
A. 사용자 영향 범위와 서비스 핵심 기능 장애 여부를 확인하고, 최근 변경 사항을 함께 확인한다.

Q. 장애 중 원인 분석과 복구 중 무엇이 우선인가?
A. 사용자 영향이 크면 완전한 원인 분석보다 우선 복구와 영향 완화가 먼저이다.

Q. Postmortem은 왜 작성하는가?
A. 장애 원인과 대응 과정을 기록하고 재발 방지 Action Item을 만들기 위해 작성한다.

Q. Prometheus와 Grafana는 각각 무엇인가?
A. Prometheus는 Metrics 수집과 저장에 강하고, Grafana는 Dashboard와 시각화에 강하다.

Q. OpenTelemetry는 무엇인가?
A. Metrics, Logs, Traces를 표준 방식으로 수집하고 전달하기 위한 Observability 표준 도구 체계이다.

Q. Metrics가 안 보일 때 첫 확인 대상은?
A. 수집 대상, Exporter, Scrape 설정, Network, Endpoint 상태를 먼저 확인한다.

Q. 로그가 안 보일 때 첫 확인 대상은?
A. 애플리케이션 로그 출력, Log Collector 상태, Label, Time Range, Query 조건을 확인한다.

Q. Alert가 너무 많으면 어떻게 해야 하는가?
A. Threshold, 지속 시간, Severity, 중복 Rule, 사용자 영향 여부를 기준으로 정리한다.

Q. Monitoring Review에서 가장 먼저 확인할 것은?
A. Error Rate, Latency, Traffic, Saturation, Health Check, Alert Rule, 로그 검색 가능성, Correlation ID를 먼저 확인한다.

Q. Logging Review에서 가장 위험한 문제는?
A. Secret, Token, 개인정보가 로그에 남는 것과 장애 분석에 필요한 Trace ID / Request ID가 없는 것이다.

Q. Monitoring & Logging과 Deployment Strategy는 어떻게 연결되는가?
A. 배포 후 Error Rate, Latency, Logs, Business Metric을 확인하여 성공, Rollback, Roll Forward를 판단하는 데 연결된다.

Q. Monitoring & Logging과 Kubernetes는 어떻게 연결되는가?
A. Pod 상태, Node 상태, Events, Logs, Metrics, Rollout 상태 관측에서 연결된다.

Q. Monitoring & Logging 문서의 최종 목적은?
A. Agent가 운영 시스템을 관측하고, 장애를 빠르게 감지하며, 원인을 분석하고, 재발 방지까지 수행하게 만드는 것이다.
