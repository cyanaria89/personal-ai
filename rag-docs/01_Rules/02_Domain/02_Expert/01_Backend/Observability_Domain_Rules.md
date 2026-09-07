# Observability Domain Rules

---

# 1. Domain Purpose

Observability Domain 문서는 Backend Expert Agent / DevOps Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- Application Observability 설계
- Logging / Metrics / Tracing 기준 제공
- 장애 원인 분석 지원
- Distributed System 문제 추적
- API Latency / Error / Resource 상태 관측
- Monitoring / Alerting 기준 제공
- Performance Tuning 문서와 연계
- 운영 안정성 Review 지원

우선순위:

1. Incident Visibility
2. Root Cause Analysis
3. Service Health Monitoring
4. Log / Metric / Trace Correlation
5. Alert Quality
6. Operational Reliability

---

# 2. Scope

포함 범위:

- Observability Core
- Monitoring
- Logging
- Metrics
- Distributed Tracing
- Alerting
- Dashboard
- Health Check
- Correlation ID
- Trace ID
- Structured Logging
- Application Metrics
- JVM Metrics
- Database Metrics
- External API Metrics
- Error Tracking
- SLI / SLO / SLA
- Prometheus
- Grafana
- OpenTelemetry
- Spring Boot Actuator
- Micrometer
- Observability Troubleshooting

제외 범위:

- Kubernetes 운영 상세
- CI/CD 상세
- Linux OS Kernel 튜닝
- Elasticsearch 내부 운영 튜닝
- Kafka Broker 상세 운영 튜닝
- Frontend Observability 상세
- AI Observability 상세

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. Observability Core Rules

Observability 문서는 단순 모니터링 도구 설명이 아니라 시스템 상태를 이해하고 장애 원인을 추적하는 기준 중심으로 작성한다.

핵심 원칙:

```text
Logs
+ Metrics
+ Traces
→ System Understanding
→ Root Cause Analysis
→ Incident Response
```

반드시 설명:

- Monitoring은 상태 확인 중심
- Observability는 원인 분석 가능성 중심
- Log, Metric, Trace는 함께 사용해야 함
- 장애 발생 후 원인을 추적할 수 있어야 함
- 관측성 없는 시스템은 운영 중 문제 분석이 어려움

금지:

- 도구 설치법만 나열
- 로그를 많이 남기면 좋다는 식의 설명
- Metrics만 있으면 충분하다는 설명
- Trace만 있으면 원인 분석이 끝난다는 설명
- Alert를 많이 만들수록 좋다는 설명

---

# 5. Monitoring vs Observability Rules

Monitoring과 Observability 차이를 반드시 설명한다.

비교:

| 구분      | Monitoring     | Observability                               |
| --------- | -------------- | ------------------------------------------- |
| 목적      | 상태 감시      | 원인 분석                                   |
| 질문      | 지금 정상인가? | 왜 문제가 발생했는가?                       |
| 중심      | Metric / Alert | Log + Metric + Trace                        |
| 사용 시점 | 장애 감지      | 장애 분석                                   |
| 예시      | CPU 90% 알림   | 특정 요청이 어떤 서비스에서 지연됐는지 추적 |

반드시 설명:

- Monitoring은 알려진 문제를 감지하는 데 강함
- Observability는 알 수 없는 문제를 추적하는 데 중요
- 운영 시스템은 Monitoring과 Observability가 함께 필요함

---

# 6. Three Pillars Rules

Observability의 3요소를 반드시 포함한다.

필수 포함:

- Logs
- Metrics
- Traces

기본 Flow:

```text
Request
→ Generate Logs
→ Record Metrics
→ Propagate Trace
→ Analyze Incident
```

반드시 설명:

- Logs는 이벤트 상세 기록
- Metrics는 수치 기반 상태 지표
- Traces는 요청 흐름 추적
- 세 요소를 Correlation ID / Trace ID로 연결해야 효과적

주의:

- 로그만 있으면 전체 흐름 파악이 어려움
- Metrics만 있으면 상세 원인 분석이 어려움
- Trace만 있으면 내부 상태나 구체적 예외 정보가 부족할 수 있음

---

# 7. Logging Rules

Logging 문서는 장애 분석과 운영 추적 중심으로 작성한다.

필수 포함:

- Structured Logging
- Log Level
- Trace ID
- Correlation ID
- Request Log
- Error Log
- Audit Log
- Slow Query Log
- External API Log
- Sensitive Data Masking

Log Level 기준:

| Level | 용도               |
| ----- | ------------------ |
| TRACE | 매우 상세한 디버깅 |
| DEBUG | 개발/디버깅 정보   |
| INFO  | 정상 비즈니스 흐름 |
| WARN  | 잠재적 문제        |
| ERROR | 실패/장애          |

반드시 설명:

- 운영 로그는 검색 가능해야 함
- JSON 기반 Structured Logging 권장
- 요청 단위 추적을 위해 Trace ID / Correlation ID 포함
- Error Log에는 원인 분석에 필요한 Context 포함
- 개인정보 / 토큰 / 비밀번호 / 결제정보는 로그 금지 또는 Masking

주의:

- DEBUG 로그를 운영에서 과도하게 사용 금지
- 예외를 삼키고 로그만 남기는 방식 금지
- Stack Trace 없는 ERROR 로그 금지
- 민감정보 로그 출력 금지
- 로그 양이 많으면 저장소 비용과 성능 문제가 발생

---

# 8. Structured Logging Rules

Structured Logging은 검색과 분석을 쉽게 하기 위해 사용한다.

필수 포함:

- JSON Log
- Field Based Search
- timestamp
- level
- service
- traceId
- spanId
- userId
- requestId
- path
- method
- status
- latency
- errorCode

예시:

```json
{
  "timestamp": "2026-06-27T20:00:00",
  "level": "ERROR",
  "service": "festival-service",
  "traceId": "abc-123",
  "method": "GET",
  "path": "/festival/detail/1",
  "status": 500,
  "latencyMs": 321,
  "errorCode": "FESTIVAL_NOT_FOUND"
}
```

반드시 설명:

- 문자열 로그보다 구조화 로그가 검색/집계에 유리
- Trace ID와 Service Name은 필수에 가깝다
- 로그 필드 이름은 전체 서비스에서 통일해야 함

---

# 9. Correlation ID / Trace ID Rules

Correlation ID와 Trace ID는 요청 추적의 핵심이다.

필수 포함:

- Correlation ID
- Trace ID
- Span ID
- Request ID
- MDC
- Header Propagation

기본 Flow:

```text
Client Request
→ API Gateway / Filter
→ Generate Trace ID
→ Add MDC
→ Service Log
→ External Call Header Propagation
→ Trace Analysis
```

반드시 설명:

- Trace ID는 하나의 요청 흐름을 추적하기 위한 식별자
- Span ID는 요청 내부의 개별 작업 구간 식별자
- Correlation ID는 여러 시스템 로그를 연결하는 데 사용
- Spring에서는 Filter / Interceptor / MDC로 로그에 ID를 포함 가능

주의:

- 서비스 간 HTTP 호출 시 Trace ID 전파 필요
- 비동기 처리 시 MDC 전파 누락 주의
- 메시지 큐 사용 시 Message Header로 Trace ID 전달 고려

---

# 10. Metrics Rules

Metrics 문서는 수치 기반 상태 관측 중심으로 작성한다.

필수 포함:

- Counter
- Gauge
- Timer
- Histogram
- Summary
- RED Metrics
- USE Metrics
- Application Metrics
- JVM Metrics
- DB Metrics
- Cache Metrics
- External API Metrics

기본 Metric 유형:

| 유형      | 의미         | 예시                    |
| --------- | ------------ | ----------------------- |
| Counter   | 누적 증가 값 | request_count           |
| Gauge     | 현재 상태 값 | memory_usage            |
| Timer     | 시간 측정    | api_latency             |
| Histogram | 분포 측정    | request_duration_bucket |

반드시 설명:

- Metric은 추세와 이상 징후 파악에 유리
- Latency, Traffic, Error, Saturation 중심으로 수집
- Metric 이름과 Label은 일관되어야 함
- 너무 많은 Label은 Cardinality 폭증을 유발할 수 있음

주의:

- userId 같은 고유값을 Metric Label로 사용 금지
- Label Cardinality 폭증 주의
- 평균 Latency만 보지 말고 p95 / p99 확인
- Metric 수집 자체도 비용이 있음

---

# 11. RED / USE Metrics Rules

서비스 관측성 문서에는 RED / USE 기준을 포함한다.

RED Metrics:

```text
Rate
Errors
Duration
```

USE Metrics:

```text
Utilization
Saturation
Errors
```

설명:

- RED는 요청 기반 서비스에 적합
- USE는 인프라 리소스 분석에 적합
- Backend API는 RED Metrics를 우선 확인
- CPU, Memory, Disk, Network는 USE Metrics로 확인

예시:

| 관점        | 주요 지표                    |
| ----------- | ---------------------------- |
| Rate        | 초당 요청 수                 |
| Errors      | 5xx, Exception Count         |
| Duration    | 평균, p95, p99 Latency       |
| Utilization | CPU, Memory 사용률           |
| Saturation  | Queue 대기, Thread Pool 대기 |
| Errors      | 시스템/네트워크 오류         |

---

# 12. Distributed Tracing Rules

Distributed Tracing은 분산 시스템 요청 흐름 추적에 사용한다.

필수 포함:

- Trace
- Span
- Parent Span
- Child Span
- Trace Context
- OpenTelemetry
- Sampling
- Service Map
- Critical Path

기본 Flow:

```text
Client
→ API Gateway
→ Backend Service A
→ Database
→ Kafka
→ Backend Service B
→ External API
```

반드시 설명:

- Trace는 하나의 요청 전체 흐름
- Span은 요청 안의 개별 작업 단위
- 분산 시스템에서는 Trace ID 전파가 중요
- Trace를 통해 어느 구간에서 지연/오류가 발생했는지 확인 가능

주의:

- 모든 요청을 100% Trace하면 비용 증가
- Sampling 전략 필요
- 비동기 / 메시지 큐 구간에서 Trace 연결 누락 주의
- Trace가 있어도 로그와 메트릭이 함께 필요함

---

# 13. Spring Boot Actuator Rules

Spring Boot Actuator는 Spring Application 상태 확인에 사용한다.

필수 포함:

- health
- metrics
- info
- prometheus
- env
- loggers
- threaddump
- heapdump

반드시 설명:

- Actuator는 운영 상태 확인 Endpoint 제공
- `/actuator/health`는 Health Check에 사용
- `/actuator/metrics`는 Application Metric 확인에 사용
- Prometheus 연동 시 `/actuator/prometheus` 사용 가능
- 민감한 Endpoint는 반드시 보호해야 함

주의:

- Actuator Endpoint를 외부에 무방비 공개 금지
- heapdump / env / loggers 같은 Endpoint는 보안 주의
- 운영 환경에서는 필요한 Endpoint만 노출
- Security 설정과 함께 관리

---

# 14. Micrometer Rules

Micrometer는 Spring Boot Metric 수집 표준으로 설명한다.

필수 포함:

- MeterRegistry
- Counter
- Timer
- Gauge
- Tag
- Custom Metrics
- Prometheus Registry

예시:

```java
Timer.Sample sample = Timer.start(meterRegistry);

try {
    return service.process();
} finally {
    sample.stop(Timer.builder("api.process.time")
            .tag("type", "festival")
            .register(meterRegistry));
}
```

반드시 설명:

- Micrometer는 다양한 Monitoring 시스템에 Metric을 전달하는 Facade 역할
- Spring Boot Actuator와 함께 사용
- Custom Metric은 비즈니스 지표 관측에 유용
- Tag는 분석 기준이지만 Cardinality를 주의해야 함

주의:

- 고유 ID를 Tag로 사용 금지
- Metric 이름 규칙 통일
- 너무 많은 Custom Metric 생성 금지

---

# 15. Prometheus Rules

Prometheus 문서는 Metric 수집과 질의 기준 중심으로 작성한다.

필수 포함:

- Scrape
- Target
- Time Series
- PromQL
- Label
- Alert Rule
- Exporter

기본 Flow:

```text
Spring Boot Actuator
→ /actuator/prometheus
→ Prometheus Scrape
→ Time Series DB
→ PromQL Query
→ Grafana Dashboard
```

반드시 설명:

- Prometheus는 Pull 방식으로 Metric을 수집
- Metric은 Time Series 형태로 저장
- Label을 통해 지표를 분류
- Alert Rule과 연동 가능

주의:

- Label Cardinality 폭증 주의
- Scrape Interval 설정 고려
- Prometheus는 로그 저장소가 아님
- 장기 보관 정책은 별도 고려

---

# 16. Grafana Rules

Grafana 문서는 Dashboard와 시각화 기준 중심으로 작성한다.

필수 포함:

- Dashboard
- Panel
- Query
- Variable
- Alert
- Annotation
- SLO Dashboard

Dashboard 기본 구성:

```text
Overview
→ API Latency
→ Error Rate
→ Traffic
→ JVM
→ DB
→ Cache
→ External API
```

반드시 설명:

- Dashboard는 운영자가 빠르게 상태를 파악하도록 구성
- 서비스별 Overview Dashboard 필요
- 장애 분석용 상세 Dashboard 필요
- p95 / p99 Latency와 Error Rate를 포함
- Alert와 Dashboard는 연결되어야 함

주의:

- 보기 좋은 그래프보다 원인 분석 가능한 Dashboard 우선
- Panel이 너무 많으면 핵심 상태 파악이 어려움
- 단위와 범례를 명확히 표시
- 장애 시 확인 순서를 고려해 배치

---

# 17. Alerting Rules

Alerting 문서는 장애 대응 품질 중심으로 작성한다.

필수 포함:

- Alert Rule
- Threshold
- Warning
- Critical
- Notification
- Escalation
- Alert Fatigue
- False Positive
- Runbook

기본 Flow:

```text
Metric Condition
→ Alert Trigger
→ Notification
→ Runbook
→ Incident Response
→ Postmortem
```

반드시 설명:

- Alert는 행동 가능한 기준이어야 함
- 너무 많은 Alert는 Alert Fatigue를 유발
- Warning / Critical을 구분
- 알림에는 원인 분석에 필요한 링크 포함
- Runbook과 연결해야 함

주의:

- 단순 CPU 순간 상승만으로 Critical Alert 금지
- 원인 분석 불가능한 Alert 금지
- 너무 민감한 Threshold 금지
- 반복되는 False Positive는 반드시 개선

---

# 18. SLI / SLO / SLA Rules

SLI / SLO / SLA는 서비스 품질 기준으로 설명한다.

필수 포함:

- SLI
- SLO
- SLA
- Error Budget
- Availability
- Latency Objective
- Error Rate Objective

정의:

| 용어 | 의미                        |
| ---- | --------------------------- |
| SLI  | 서비스 수준을 측정하는 지표 |
| SLO  | 목표 서비스 수준            |
| SLA  | 사용자/고객과의 계약 수준   |

예시:

```text
SLI: p95 latency, error rate, availability
SLO: p95 latency < 500ms, availability 99.9%
SLA: 계약상 보장하는 서비스 수준
```

반드시 설명:

- SLI는 측정 지표
- SLO는 내부 목표
- SLA는 외부 약속
- Error Budget은 안정성과 개발 속도의 균형에 사용

주의:

- 측정 불가능한 SLO 설정 금지
- 모든 API에 동일한 SLO를 강제하지 말 것
- 사용자 체감과 연결된 지표를 우선

---

# 19. Health Check Rules

Health Check는 서비스 상태 판단에 사용한다.

필수 포함:

- Liveness Check
- Readiness Check
- Startup Check
- Dependency Health
- Database Health
- External API Health
- Kubernetes Probe

기본 Flow:

```text
Health Endpoint
→ Check Application
→ Check DB
→ Check External Dependency
→ Return Status
```

반드시 설명:

- Liveness는 애플리케이션이 살아있는지 확인
- Readiness는 요청을 받을 준비가 되었는지 확인
- DB / Redis / 외부 API 상태를 포함할 수 있음
- Health Check는 배포와 장애 감지에 중요

주의:

- 너무 무거운 Health Check 금지
- 외부 API 장애가 전체 서비스 Down으로 판단되는지 주의
- Readiness와 Liveness 역할 혼동 금지
- 민감한 상세 정보 노출 금지

---

# 20. Error Tracking Rules

Error Tracking 문서는 예외와 장애 패턴 분석 중심으로 작성한다.

필수 포함:

- Exception Count
- Error Rate
- Error Code
- Stack Trace
- Error Grouping
- Root Cause
- User Impact
- Incident Severity

반드시 설명:

- Error Rate는 서비스 안정성 핵심 지표
- 동일 예외는 그룹화해서 분석
- Error Log에는 Trace ID와 요청 Context 포함
- 비즈니스 예외와 시스템 예외를 구분
- 사용자 영향도를 기준으로 우선순위 판단

주의:

- 모든 예외를 ERROR로 기록하지 말 것
- 예상 가능한 비즈니스 실패와 시스템 장애 구분
- Stack Trace 없는 Error Log 금지
- 예외 메시지에 민감정보 포함 금지

---

# 21. Database Observability Rules

Database Observability는 Backend 장애 분석에 매우 중요하다.

필수 포함:

- Query Latency
- Slow Query
- Connection Pool Usage
- Lock Wait
- Deadlock
- Transaction Time
- Index Usage
- DB CPU / Memory / I/O
- Replication Lag

기본 Flow:

```text
Slow API
→ Check API Trace
→ Check Query Time
→ Check Connection Pool
→ Check Lock / Transaction
→ Check DB Resource
```

반드시 설명:

- DB 지연은 API 지연의 주요 원인
- Slow Query와 Connection Pool 지표를 함께 봐야 함
- Lock Wait / Deadlock은 간헐적 장애 원인이 될 수 있음
- Transaction 시간이 길면 Connection 점유와 Lock 위험 증가

주의:

- Application Metric만 보고 DB 문제를 단정하지 말 것
- Query Count 증가와 N+1 가능성 확인
- DB Metric과 Application Trace를 연결해 분석

---

# 22. JVM Observability Rules

JVM Observability는 Spring Backend 운영에 필요하다.

필수 포함:

- Heap Usage
- Non-Heap Usage
- GC Count
- GC Pause Time
- Thread Count
- Thread State
- Class Loading
- Memory Leak
- OOM
- Thread Dump
- Heap Dump

기본 Flow:

```text
High Memory / Latency
→ Check Heap Usage
→ Check GC Pause
→ Check Thread Count
→ Analyze Dump if Needed
```

반드시 설명:

- GC Pause는 Latency 증가 원인이 될 수 있음
- Heap 사용량 추세로 Memory Leak 가능성 확인
- Thread 수와 상태는 동시성 문제 분석에 중요
- Dump 분석은 장애 원인 확인에 사용

주의:

- Heap Dump에는 민감정보가 포함될 수 있음
- Dump 생성은 서비스에 부하를 줄 수 있음
- JVM 지표만으로 원인을 단정하지 말 것

---

# 23. External API Observability Rules

외부 API 관측성은 장애 전파를 막기 위해 중요하다.

필수 포함:

- External API Latency
- Timeout Count
- Retry Count
- Error Rate
- Circuit Breaker State
- Rate Limit
- Fallback Count

기본 Flow:

```text
Service
→ External API Call
→ Record Latency
→ Record Error / Timeout
→ Circuit Breaker Metrics
→ Alert if Needed
```

반드시 설명:

- 외부 API는 내부 시스템보다 예측하기 어려움
- Timeout / Retry / Circuit Breaker 지표가 필요
- 외부 API 장애는 내부 장애처럼 보일 수 있음
- 외부 호출 Trace와 Log를 남겨야 함

주의:

- 외부 API 응답 전체를 로그에 남기지 말 것
- Retry 폭증은 장애를 악화시킬 수 있음
- Rate Limit 초과 여부를 관측해야 함

---

# 24. Message Queue Observability Rules

Message Queue / Kafka 기반 시스템은 별도 관측 기준이 필요하다.

필수 포함:

- Producer Success / Failure
- Consumer Lag
- Consumer Error
- Retry Count
- DLQ Count
- Message Processing Time
- Offset
- Rebalance
- Dead Letter Queue

기본 Flow:

```text
Producer
→ Broker
→ Consumer
→ Processing
→ Retry / DLQ
→ Metrics / Logs / Trace
```

반드시 설명:

- Consumer Lag는 처리 지연의 핵심 지표
- DLQ Count는 실패 메시지 누적을 의미
- Consumer 처리 시간과 Error Rate를 확인
- 메시지에도 Trace ID / Correlation ID 전달 고려

주의:

- 메시지 발행 성공과 처리 성공은 다름
- Consumer Error를 로그만 남기고 무시 금지
- DLQ 누적 알림 필요
- 재처리 전략 필요

---

# 25. Dashboard Design Rules

Dashboard 문서는 장애 확인 순서 중심으로 작성한다.

필수 Dashboard:

- Service Overview Dashboard
- API Latency Dashboard
- Error Rate Dashboard
- JVM Dashboard
- Database Dashboard
- External API Dashboard
- Cache Dashboard
- Message Queue Dashboard

Service Overview 구성:

```text
Traffic
→ Error Rate
→ Latency p95 / p99
→ JVM
→ DB
→ External Dependencies
```

반드시 설명:

- 첫 화면에서 서비스 정상 여부를 알 수 있어야 함
- 장애 분석용 상세 Dashboard와 분리 가능
- Dashboard는 Alert와 연결되어야 함
- 배포 시점 Annotation이 있으면 분석에 유리

주의:

- 모든 지표를 한 화면에 넣지 말 것
- 원인 분석 흐름이 보이도록 구성
- 단위와 기준선을 명확히 표시

---

# 26. Incident Response Rules

Observability 문서는 장애 대응 흐름을 포함한다.

기본 Flow:

```text
Alert
→ Check Dashboard
→ Check Trace
→ Check Logs
→ Identify Root Cause
→ Mitigate
→ Recover
→ Postmortem
```

반드시 설명:

- 장애 대응은 감지, 분석, 완화, 복구, 회고 흐름
- Alert에는 관련 Dashboard / Log / Trace 링크가 있어야 함
- 임시 완화와 근본 해결을 구분
- Postmortem으로 재발 방지책을 만든다

주의:

- 장애 중 무리한 구조 변경 금지
- 원인 불명 상태에서 재시작만 반복 금지
- 재발 방지 없이 종료 금지

---

# 27. Observability Review Rules

Review Agent가 확인할 기준을 포함한다.

필수 체크:

- 주요 API Latency Metric이 있는가?
- Error Rate Metric이 있는가?
- Trace ID / Correlation ID가 로그에 포함되는가?
- 외부 API Timeout / Error / Latency를 관측하는가?
- DB Query Time / Connection Pool 상태를 관측하는가?
- JVM Heap / GC / Thread 지표를 확인할 수 있는가?
- Alert가 행동 가능한 기준인가?
- Dashboard가 장애 분석 흐름에 맞는가?
- 민감정보가 로그에 남지 않는가?
- Actuator Endpoint가 보호되는가?

Review Flow:

```text
Code Review
→ Logging Review
→ Metrics Review
→ Trace Review
→ Alert Review
→ Dashboard Review
→ Security Review
```

---

# 28. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Trace ID가 로그에 없음

문제:

- 장애 발생 시 요청 흐름을 추적하기 어려움

원인:

- Filter / Interceptor에서 Trace ID 생성 누락
- MDC 설정 누락
- 비동기 작업에서 MDC 전파 누락

해결:

- 요청 시작 시 Trace ID 생성
- MDC에 Trace ID 저장
- 로그 패턴에 Trace ID 포함
- 비동기 / 메시지 큐 구간 전파 처리

---

## Alert가 너무 많이 발생함

문제:

- 운영자가 중요한 장애를 구분하기 어려움

원인:

- Threshold가 너무 민감함
- Warning / Critical 구분 없음
- 행동 불가능한 Alert가 많음
- False Positive가 많음

해결:

- Alert 기준 재정의
- Warning / Critical 분리
- Runbook 연결
- 반복 False Positive 제거

---

## Dashboard를 봐도 원인을 모르겠음

문제:

- 장애 원인 분석이 어려움

원인:

- 지표가 흩어져 있음
- Log / Metric / Trace 연결 부족
- Dashboard가 서비스 흐름 기준이 아님
- p95 / p99 / Error Rate 누락

해결:

- Service Overview Dashboard 구성
- Trace ID 기반 로그 연결
- API Latency / Error / DB / JVM 지표 추가
- 장애 분석 순서대로 Panel 배치

---

## 로그는 많은데 검색이 어려움

문제:

- 필요한 로그를 찾기 어려움

원인:

- Plain Text 로그 중심
- 필드 이름 불일치
- Trace ID / Request ID 누락
- 로그 레벨 기준 없음

해결:

- Structured Logging 적용
- 공통 필드 정의
- Trace ID 포함
- Log Level 기준 정리

---

## Metric Cardinality 폭증

문제:

- Prometheus 저장소와 Query 성능에 부담 발생

원인:

- userId, orderId 같은 고유값을 Label로 사용
- Label 조합이 과도함
- Custom Metric 남용

해결:

- 고유값 Label 제거
- Label 기준 최소화
- Metric 설계 재검토
- 필요한 지표만 수집

---

## Slow API 원인을 찾기 어려움

문제:

- API가 느리지만 어느 구간이 병목인지 모름

원인:

- 구간별 Metric 없음
- Trace 미수집
- DB Query Time 미수집
- 외부 API Latency 미수집

해결:

- Distributed Tracing 적용
- DB Query Time 관측
- 외부 API Latency Metric 추가
- p95 / p99 Latency 확인

---

# 29. Best Practice Rules

Best Practice:

- 모든 서비스 로그에 service, traceId, level, timestamp 포함
- Error Log에는 Stack Trace와 Context 포함
- 민감정보는 로그에 남기지 않음
- API Latency는 평균보다 p95 / p99 확인
- Error Rate는 서비스 안정성 핵심 지표로 관리
- 주요 외부 API 호출은 Latency / Timeout / Error 관측
- DB Connection Pool과 Slow Query를 함께 확인
- JVM Heap / GC / Thread 지표 수집
- Dashboard는 장애 분석 순서대로 구성
- Alert는 행동 가능한 기준으로 작성
- Runbook과 Alert를 연결
- 배포 시점 Annotation 기록
- Observability는 Performance Tuning과 연계

---

# 30. Comparison Rules

Observability 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Monitoring vs Observability
- Logs vs Metrics vs Traces
- Trace ID vs Correlation ID
- Counter vs Gauge vs Timer
- RED Metrics vs USE Metrics
- Warning Alert vs Critical Alert
- Liveness Check vs Readiness Check
- 평균 Latency vs p95 / p99 Latency
- Plain Text Logging vs Structured Logging

예시:

| 비교 | Logs                  | Metrics             | Traces           |
| ---- | --------------------- | ------------------- | ---------------- |
| 목적 | 이벤트 상세 기록      | 수치 기반 상태 확인 | 요청 흐름 추적   |
| 장점 | 상세한 원인 확인      | 추세/이상 징후 파악 | 병목 구간 파악   |
| 단점 | 양이 많고 검색 어려움 | 상세 원인 부족      | 비용/샘플링 필요 |
| 적합 | 예외 분석             | 알림/대시보드       | 분산 요청 추적   |

---

# 31. Checklist Rules

Observability 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] 주요 API Latency Metric이 있는가?
- [ ] p95 / p99 Latency를 확인할 수 있는가?
- [ ] Error Rate를 확인할 수 있는가?
- [ ] Trace ID가 로그에 포함되는가?
- [ ] 외부 API Latency / Timeout / Error를 관측하는가?
- [ ] DB Connection Pool 상태를 관측하는가?
- [ ] JVM Heap / GC / Thread 지표를 관측하는가?
- [ ] Dashboard가 장애 분석 흐름에 맞는가?
- [ ] Alert가 행동 가능한 기준인가?
- [ ] 민감정보가 로그에 남지 않는가?
```

---

# 32. Retrieval Optimization Rules

강조 대상 키워드:

- Observability
- Monitoring
- Logging
- Structured Logging
- Metrics
- Distributed Tracing
- Trace ID
- Correlation ID
- Span ID
- MDC
- OpenTelemetry
- Prometheus
- Grafana
- Spring Boot Actuator
- Micrometer
- Health Check
- Liveness
- Readiness
- Alerting
- Dashboard
- SLI
- SLO
- SLA
- Error Budget
- RED Metrics
- USE Metrics
- p95
- p99
- Error Rate
- API Latency
- JVM Metrics
- DB Metrics
- Connection Pool
- Consumer Lag
- DLQ
- Incident Response
- Runbook
- Postmortem

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Observability가 뭐야?
- Monitoring이랑 Observability 차이는?
- 로그 메트릭 트레이스 차이는?
- Trace ID는 왜 필요해?
- Spring Boot에서 Observability 어떻게 구성해?
- Prometheus랑 Grafana는 각각 뭐야?
- Actuator는 운영에서 열어도 돼?
- Alert는 어떻게 잡아야 해?
- p95 p99는 왜 봐야 해?
- Dashboard는 어떻게 구성해?
- 장애가 났을 때 어디부터 봐야 해?

---

# 33. Version Rules

기준:

- Java 21
- Spring Boot 3.x
- Spring Framework 6.x
- Spring Boot Actuator
- Micrometer
- OpenTelemetry
- Prometheus
- Grafana
- Modern Backend Observability
- MSA / Modular Monolith 관측성 기준

Legacy 제외:

- Spring Boot 1.x / 2.x 전용 방식
- XML 기반 Spring 설정 중심
- 단순 로그 파일 확인만으로 끝나는 운영 방식
- 도구 설치법만 나열하는 문서

---

# 34. Common Mistakes

자주 발생:

- 로그만 많고 Trace ID가 없음
- Error Log에 Stack Trace가 없음
- 민감정보를 로그에 출력
- Metric Label에 userId 같은 고유값 사용
- 평균 Latency만 보고 p95 / p99 무시
- Alert가 너무 많아 Alert Fatigue 발생
- Dashboard가 원인 분석 흐름과 무관함
- Actuator Endpoint를 외부에 무방비 공개
- 외부 API Timeout / Error 지표 없음
- DB Connection Pool 지표 없음
- Consumer Lag / DLQ 지표 없음
- Trace Sampling 비용 고려 없음
- 장애 후 Postmortem 없이 종료

---

# 35. Final Goal

Observability RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- 로그 설계 기준 제안
- Metric 수집 기준 제안
- Trace ID / Correlation ID 적용 여부 검토
- API Latency / Error Rate 분석
- Dashboard 구성 제안
- Alert 기준 검토
- Actuator 보안 노출 여부 검토
- Prometheus / Grafana 구성 방향 제안
- OpenTelemetry 적용 여부 판단
- 장애 분석 흐름 제안
- Performance Tuning과 연계한 병목 분석
- MSA / Message Queue 기반 시스템 관측성 검토
- Observability Review
- Incident Response Direction 제안

문서 품질이 운영 안정성과 장애 대응 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Observability가 뭐야?

A.
시스템 내부 상태를 로그, 메트릭, 트레이스로 관측하고 장애 원인을 분석할 수 있게 만드는 능력이다.

Q. Monitoring이랑 Observability 차이는?

A.
Monitoring은 현재 상태 감시 중심이고, Observability는 문제가 왜 발생했는지 원인을 추적하는 데 초점이 있다.

Q. 로그, 메트릭, 트레이스 차이는?

A.
로그는 이벤트 상세 기록, 메트릭은 수치 기반 상태, 트레이스는 요청 흐름 추적이다.

Q. Trace ID는 왜 필요해?

A.
하나의 요청이 여러 서비스와 컴포넌트를 지나갈 때 전체 흐름을 연결해서 추적하기 위해 필요하다.

Q. Correlation ID는 언제 써?

A.
여러 시스템의 로그와 이벤트를 하나의 사용자 요청이나 작업 단위로 묶어 분석할 때 사용한다.

Q. Spring Boot에서 Observability는 어떻게 구성해?

A.
Spring Boot Actuator, Micrometer, Prometheus, Grafana, OpenTelemetry를 조합해 로그, 메트릭, 트레이스를 수집한다.

Q. Actuator Endpoint는 운영에서 열어도 돼?

A.
필요한 Endpoint만 제한적으로 열고, health / metrics 외의 민감 Endpoint는 인증과 접근 제어를 적용해야 한다.

Q. Prometheus는 뭐 하는 도구야?

A.
Application과 Infrastructure Metric을 주기적으로 수집하고 Time Series 형태로 저장하는 모니터링 도구다.

Q. Grafana는 뭐 하는 도구야?

A.
Prometheus 같은 데이터 소스를 시각화해서 Dashboard와 Alert를 구성하는 도구다.

Q. Alert는 어떻게 잡아야 해?

A.
행동 가능한 기준으로 만들고, Warning / Critical을 구분하며, Runbook과 Dashboard 링크를 함께 제공해야 한다.

Q. Alert가 너무 많이 울리면 어떻게 해?

A.
Threshold를 조정하고 False Positive를 줄이며, 실제 대응이 필요한 Alert만 남긴다.

Q. p95와 p99는 왜 봐야 해?

A.
평균 응답 시간은 일부 느린 요청을 숨길 수 있다. p95와 p99는 사용자가 체감하는 지연을 더 잘 보여준다.

Q. Dashboard는 어떻게 구성해야 해?

A.
Overview에서 Traffic, Error Rate, Latency, JVM, DB, 외부 의존성을 빠르게 확인하고 상세 Dashboard로 원인을 분석할 수 있게 구성한다.

Q. 로그에 무엇을 남겨야 해?

A.
timestamp, level, service, traceId, request path, status, latency, errorCode 같은 검색 가능한 정보를 남긴다.

Q. 로그에 남기면 안 되는 것은?

A.
비밀번호, 토큰, 개인정보, 결제정보 같은 민감정보는 남기지 않거나 반드시 Masking해야 한다.

Q. Metric Label에 userId를 넣어도 돼?

A.
안 된다. userId 같은 고유값은 Cardinality를 폭증시켜 Prometheus 성능과 저장소에 문제를 만든다.

Q. 장애가 났을 때 어디부터 봐야 해?

A.
Alert 확인 후 Service Dashboard, Trace, Error Log, DB Metric, JVM Metric, 외부 API 상태 순서로 확인한다.

Q. Consumer Lag는 왜 중요해?

A.
Message Queue나 Kafka에서 Consumer가 메시지를 처리하지 못하고 밀리고 있는지 보여주는 핵심 지표다.

Q. DLQ는 왜 관측해야 해?

A.
처리에 실패한 메시지가 쌓이는 곳이므로 DLQ 증가 여부는 비동기 처리 장애를 판단하는 중요한 신호다.

Q. Observability와 Performance Tuning은 어떤 관계야?

A.
Observability는 병목을 발견하고 원인을 추적하는 기반이고, Performance Tuning은 그 원인을 개선하는 작업이다.
