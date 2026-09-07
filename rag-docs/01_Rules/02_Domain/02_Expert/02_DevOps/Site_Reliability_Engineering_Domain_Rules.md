# Site Reliability Engineering Domain Rules

---

# 1. Domain Purpose

## 1.1 Site Reliability Engineering 문서 목적

### [개념]

Site Reliability Engineering Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Reliability Engineering Support
- Service Health Review Support
- SLO / Error Budget Support
- Incident Management Support
- Toil Reduction Support
- Automation Priority Support
- Home Server Reliability Support
- Monitoring / Deployment / Backup 연계 Support

우선순위:

1. Reliability Core
2. SLI / SLO / Error Budget
3. Incident Response / Postmortem
4. Toil Reduction / Automation
5. Home Server Reliability
6. Reliability Review / Troubleshooting

---

### [핵심]

Site Reliability Engineering 문서는 대기업 운영 철학을 그대로 복사하는 문서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- 서비스 신뢰성 기준 정의
- SLI / SLO / Error Budget 설계
- 장애 영향 범위 판단
- Incident 대응 Flow 작성
- Postmortem 작성 기준 제안
- 반복 운영 작업을 Toil로 분류
- 자동화 우선순위 판단
- 배포 안정성 검토
- 홈서버 장애 대응 기준 작성
- Monitoring / Logging / Backup / Deployment 문서와 연계

---

### [실무]

2026 개인 홈서버 + DevOps 운영 기준 SRE 문서는 다음 흐름을 기준으로 작성한다.

```text
Service
→ Reliability Objective
→ Monitoring Signal
→ Alert
→ Incident Response
→ Recovery
→ Postmortem
→ Automation / Prevention
```

개인 홈서버 기준에서는 대규모 SRE 조직 운영보다 **서비스가 죽었는지 감지하고, 빠르게 복구하고, 같은 장애를 반복하지 않도록 자동화하는 것**을 우선한다.

---

### [FAQ]

Q. SRE 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 서비스 신뢰성, 장애 대응, 자동화, 운영 품질을 관리하기 위한 RAG 문서이다.

Q. 개인 홈서버에도 SRE가 필요한가?

A.
대기업식 SRE는 과하지만 경량 SRE는 유용하다. 서비스 죽음 감지, 백업, 복구, 자동 재시작, 장애 기록, 반복 작업 자동화에 도움이 된다.

Q. SRE와 Monitoring & Logging은 어떻게 다른가?

A.
Monitoring & Logging은 관측 도구와 신호를 다루고, SRE는 그 신호를 기준으로 신뢰성 목표, 장애 대응, 개선 활동을 운영한다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Site Reliability Engineering Domain 문서는 서비스 신뢰성 목표, 장애 대응, 자동화, 운영 개선 기준을 다룬다.

포함 범위:

- Site Reliability Engineering
- Reliability
- Availability
- Resilience
- SLI
- SLO
- SLA
- Error Budget
- Incident Response
- On-call
- Alerting
- Monitoring Signal
- Runbook
- Postmortem
- Toil
- Automation
- Capacity Planning
- Change Management
- Deployment Reliability
- Rollback Decision
- Disaster Recovery
- Backup Reliability
- Service Health
- Home Server Reliability
- Reliability Review
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- SRE
- Reliability
- Availability
- Resilience
- SLI
- SLO
- SLA
- Error Budget
- Incident
- Runbook
- Postmortem
- Toil
- Automation
- Alert
- Monitoring
- Capacity
- Change Risk
- Home Server
- Recovery
- Reliability Review

---

### [실무]

SRE 문서는 아래 상황을 해결할 수 있어야 한다.

- 서비스가 자주 죽는 원인 분석
- 장애 감지 기준 정의
- Alert가 너무 많거나 적은 문제 해결
- SLO 기준으로 서비스 상태 판단
- 배포 실패가 잦을 때 Release 안정성 검토
- 반복 수동 작업을 자동화 대상으로 분류
- 홈서버 Docker Container 자동 재시작 기준 작성
- 백업 실패를 신뢰성 위험으로 분류
- Postmortem 작성 기준 제공
- 장애 이후 재발 방지 Action Item 도출
- 비용 절감과 신뢰성 사이의 균형 판단

---

### [FAQ]

Q. SRE 문서에 대규모 On-call 조직 운영을 깊게 포함해야 하는가?

A.
아니다. 개인 홈서버와 DevOps Agent 기준에서는 장애 감지, 복구, 기록, 자동화, 신뢰성 기준을 우선한다.

Q. SRE 문서가 Deployment Strategy와 겹치는가?

A.
일부 연결된다. Deployment Strategy는 배포 방식 중심이고 SRE는 배포가 신뢰성에 미치는 영향과 장애 대응 기준을 다룬다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Site Reliability Engineering 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

SRE 문서는 검색 친화적인 신뢰성 운영 구조를 우선한다.

```text
Service Objective
→ SLI / SLO
→ Monitoring / Alert
→ Incident
→ Recovery
→ Postmortem
→ Automation
```

---

### [실무]

권장 Part 구성:

- Site_Reliability_Engineering_Part01_Core.md
- Site_Reliability_Engineering_Part02_SLI_SLO_Error_Budget.md
- Site_Reliability_Engineering_Part03_Incident_Response.md
- Site_Reliability_Engineering_Part04_Postmortem.md
- Site_Reliability_Engineering_Part05_Toil_Automation.md
- Site_Reliability_Engineering_Part06_Capacity_Change_Risk.md
- Site_Reliability_Engineering_Part07_Home_Server_Reliability.md
- Site_Reliability_Engineering_Part08_Reliability_Review.md
- Site_Reliability_Engineering_Part09_Troubleshooting.md

---

### [FAQ]

Q. SRE 문서에 FAQ가 필요한가?

A.
필수이다. SRE 질문은 “서비스가 자꾸 죽는다”, “Alert 기준이 뭐냐”, “SLO가 뭐냐”, “장애 후 뭘 기록하냐”처럼 문제 상황 중심으로 들어온다.

Q. SRE 문서는 얼마나 복잡해야 하는가?

A.
개인 홈서버 기준에서는 경량으로 유지한다. 서비스 상태 기준, 장애 대응, 복구, 자동화, 기록이 명확하면 충분하다.

---

# 4. SRE Core Rules

## 4.1 SRE Core 작성 규칙

### [개념]

Site Reliability Engineering은 소프트웨어 엔지니어링 방식으로 서비스 신뢰성을 관리하는 운영 접근이다.

핵심은 장애를 완전히 없애는 것이 아니라, 허용 가능한 신뢰성 목표를 정하고 반복 장애를 줄이는 것이다.

---

### [핵심]

SRE 핵심 목표:

- 서비스 안정성 확보
- 장애 감지 시간 단축
- 복구 시간 단축
- 반복 장애 제거
- 수동 운영 작업 감소
- 신뢰성 기준 기반 의사결정
- 배포 속도와 안정성 균형 유지

기본 흐름:

```text
Define Reliability
→ Measure Reliability
→ Detect Failure
→ Recover
→ Learn
→ Automate
```

---

### [실무]

SRE 적용 대상:

- API 서버
- Database
- Docker Container
- Kubernetes Workload
- Reverse Proxy
- AI Server
- AnythingLLM
- Ollama
- RAG Document System
- Backup Job
- Monitoring Stack
- Home Server Network

---

### [FAQ]

Q. SRE의 핵심은 무엇인가?

A.
서비스 신뢰성을 측정 가능한 목표로 관리하고 장애 대응과 자동화를 통해 반복 문제를 줄이는 것이다.

Q. SRE는 장애를 0으로 만드는 것인가?

A.
아니다. 장애를 완전히 없애기보다 사용자 영향이 허용 가능한 수준 안에 있도록 관리하는 것이다.

---

# 5. Reliability Rules

## 5.1 Reliability 작성 규칙

### [개념]

Reliability는 서비스가 기대한 기능을 일정 기간 동안 정상적으로 수행하는 능력이다.

홈서버 기준 Reliability는 “필요할 때 서비스가 켜져 있고, 데이터가 보존되며, 복구 가능한 상태”를 의미한다.

---

### [핵심]

Reliability 구성 요소:

- Availability
- Correctness
- Performance
- Recoverability
- Durability
- Observability
- Operability

---

### [실무]

서비스별 Reliability 기준 예시:

```text
AnythingLLM
→ 접속 가능
→ 문서 검색 가능
→ Ollama 연결 가능
→ Workspace 데이터 유지

Ollama
→ 모델 응답 가능
→ 모델 목록 유지
→ 메모리 부족으로 죽지 않음

RAG Documents
→ 원본 문서 보존
→ 백업 존재
→ 재업로드 가능

Database
→ 데이터 일관성 유지
→ 백업 존재
→ Restore Test 가능
```

---

### [FAQ]

Q. Reliability는 무엇인가?

A.
서비스가 기대한 기능을 안정적으로 수행하고 장애가 발생해도 복구 가능한 능력이다.

Q. 홈서버 Reliability에서 가장 중요한 것은?

A.
서비스 실행 상태, 데이터 보존, 백업, 복구 가능성, 장애 원인 추적 가능성이다.

---

# 6. Availability Rules

## 6.1 Availability 작성 규칙

### [개념]

Availability는 서비스가 사용 가능한 시간의 비율이다.

Availability는 단순히 서버 프로세스가 살아있는 것이 아니라 사용자가 핵심 기능을 사용할 수 있는지를 기준으로 판단한다.

---

### [핵심]

필수 포함:

- Uptime
- Downtime
- Service Available
- Health Check
- User Impact
- Availability Target

기본 계산:

```text
Availability = 정상 제공 시간 / 전체 시간
```

---

### [실무]

홈서버 Availability 기준 예시:

```text
Personal AI Server
→ 하루 대부분 접속 가능하면 충분

Public Demo Service
→ 발표 시간대에는 높은 Availability 필요

RAG Document Storage
→ 실시간 접속보다 데이터 보존이 더 중요

Backup Job
→ 매일 성공 여부가 Availability보다 중요
```

---

### [주의]

프로세스가 살아있어도 서비스가 사용 불가능할 수 있다.

예:

- API는 200 응답이지만 내부 오류 발생
- AnythingLLM은 접속되지만 Ollama 연결 실패
- DB는 켜져 있지만 주요 Query 실패
- 외부 접속은 되지만 로그인 실패

---

### [FAQ]

Q. Availability는 무엇인가?

A.
서비스가 사용 가능한 시간의 비율이다.

Q. 서버가 켜져 있으면 Availability가 높은 것인가?

A.
아니다. 사용자가 핵심 기능을 실제로 사용할 수 있어야 한다.

---

# 7. Resilience Rules

## 7.1 Resilience 작성 규칙

### [개념]

Resilience는 장애가 발생해도 서비스가 완전히 무너지지 않고 복구하거나 제한된 기능으로 계속 동작하는 능력이다.

---

### [핵심]

필수 포함:

- Fault Tolerance
- Graceful Degradation
- Retry
- Timeout
- Circuit Breaker
- Backup
- Recovery
- Failover

---

### [실무]

Resilience 적용 예시:

```text
Ollama 응답 실패
→ 사용자에게 AI 기능 일시 불가 안내
→ 일반 문서 검색은 유지

외부 API 장애
→ Cache 데이터 사용
→ 재시도 제한
→ 장애 로그 기록

DB 일시 장애
→ Connection Timeout 제한
→ 재시도 폭주 방지
→ Alert 발생

홈서버 외부 접속 장애
→ 내부 접속 확인
→ DNS / Tunnel / 공유기 순서로 점검
```

---

### [주의]

무제한 Retry는 Resilience가 아니다.

Retry는 Timeout, Backoff, 최대 횟수 제한이 필요하다.

---

### [FAQ]

Q. Resilience는 무엇인가?

A.
장애가 발생해도 서비스가 제한적으로 동작하거나 빠르게 복구할 수 있는 능력이다.

Q. Retry를 많이 하면 안정성이 좋아지는가?

A.
아니다. 무제한 Retry는 장애를 증폭시킬 수 있으므로 제한과 Backoff가 필요하다.

---

# 8. SLI Rules

## 8.1 SLI 작성 규칙

### [개념]

SLI는 Service Level Indicator의 약자로 서비스 수준을 측정하는 지표이다.

SLO를 정하려면 먼저 SLI를 정의해야 한다.

---

### [핵심]

대표 SLI:

- Availability
- Request Success Rate
- Error Rate
- Latency
- Freshness
- Durability
- Backup Success Rate
- Restore Success Rate

---

### [실무]

서비스별 SLI 예시:

| 서비스              | SLI                                            |
| ------------------- | ---------------------------------------------- |
| API Server          | 요청 성공률, P95 Latency, 5xx Rate             |
| AnythingLLM         | 접속 성공률, 문서 검색 성공률, LLM 응답 성공률 |
| Backup Job          | 백업 성공률, 마지막 성공 시각                  |
| Database            | Query 성공률, Connection 실패율                |
| Home Server         | Docker Container Up 상태, 외부 접속 성공률     |
| RAG Document System | 문서 존재 여부, 백업 최신성                    |

---

### [FAQ]

Q. SLI는 무엇인가?

A.
서비스 수준을 측정하기 위한 지표이다.

Q. 홈서버에서 쓸만한 SLI는 무엇인가?

A.
서비스 접속 성공, Docker Container 실행 상태, 백업 성공 여부, RAG 검색 성공 여부, Ollama 응답 성공 여부가 유용하다.

---

# 9. SLO Rules

## 9.1 SLO 작성 규칙

### [개념]

SLO는 Service Level Objective의 약자로 SLI에 대한 목표값이다.

SLO는 서비스 신뢰성의 목표 기준이다.

---

### [핵심]

필수 포함:

- Service Objective
- Target
- Measurement Window
- User Impact
- Reliability Goal

예시:

```text
API 요청 성공률 99.5% / 30일
백업 성공률 99% / 30일
RAG 문서 백업 최신성 24시간 이내
```

---

### [실무]

개인 홈서버 SLO 예시:

```text
AnythingLLM
→ 주간 접속 성공률 95% 이상

Ollama
→ 로컬 질의 응답 성공률 95% 이상

Backup Job
→ 최근 24시간 내 백업 1회 이상 성공

RAG Documents
→ 최근 7일 내 Offsite Backup 존재

Home Server
→ Docker 핵심 Container 자동 재시작 가능
```

기업식 99.99% 목표보다 개인 운영에 맞는 현실적인 목표를 우선한다.

---

### [주의]

SLO를 너무 높게 잡으면 운영 부담이 커진다.

개인 홈서버는 “내가 감당 가능한 목표”로 설정한다.

---

### [FAQ]

Q. SLO는 무엇인가?

A.
SLI 지표에 대해 달성하려는 목표값이다.

Q. 개인 홈서버에도 SLO가 필요한가?

A.
복잡한 SLO는 필요 없지만 백업 성공, 서비스 접속, 복구 가능성 같은 간단한 목표는 유용하다.

---

# 10. SLA Rules

## 10.1 SLA 작성 규칙

### [개념]

SLA는 Service Level Agreement의 약자로 외부 사용자 또는 고객과 약속한 서비스 수준 계약이다.

개인 홈서버에서는 일반적으로 엄격한 SLA가 필요하지 않다.

---

### [핵심]

구분:

| 용어 | 의미      | 개인 홈서버 적용 |
| ---- | --------- | ---------------- |
| SLI  | 측정 지표 | 사용 가능        |
| SLO  | 내부 목표 | 사용 권장        |
| SLA  | 외부 계약 | 대부분 불필요    |

---

### [실무]

SLA가 필요한 상황:

- 유료 서비스 제공
- 외부 사용자에게 공개
- 팀 프로젝트 운영
- 고객 데이터 처리
- 업무용 시스템 제공

홈서버 개인 사용:

```text
SLA 없음
→ SLO 중심 운영
→ 장애 기록과 복구 절차 우선
```

---

### [FAQ]

Q. SLA는 무엇인가?

A.
외부 사용자나 고객과 약속한 서비스 수준 계약이다.

Q. 개인 홈서버에 SLA가 필요한가?

A.
대부분 필요 없다. 대신 내부 목표인 SLO와 복구 절차를 관리하는 것이 현실적이다.

---

# 11. Error Budget Rules

## 11.1 Error Budget 작성 규칙

### [개념]

Error Budget은 SLO에서 허용하는 실패 여유분이다.

서비스가 일정 수준의 실패를 허용할 수 있다는 전제에서 배포 속도와 안정성의 균형을 잡는 기준이다.

---

### [핵심]

필수 포함:

- Error Budget
- SLO Burn
- Reliability Trade-off
- Deployment Freeze
- Risk Control
- Change Decision

예시:

```text
SLO: 30일 요청 성공률 99%
Error Budget: 1% 실패 허용
```

---

### [실무]

홈서버식 Error Budget 적용:

```text
최근 업데이트 후 장애가 잦음
→ 새 기능 추가 중단
→ 안정화 우선

백업 실패가 3일 연속 발생
→ 문서 제작보다 백업 복구 우선

Ollama가 자주 죽음
→ 모델 추가보다 메모리 / 재시작 정책 점검

외부 접속 장애 반복
→ 기능 개발보다 네트워크 / DNS 안정화 우선
```

---

### [주의]

Error Budget은 숫자 계산보다 의사결정 기준으로 사용하는 것이 중요하다.

개인 프로젝트에서는 “최근 장애가 많으면 새 작업보다 안정화 우선” 정도로 적용해도 충분하다.

---

### [FAQ]

Q. Error Budget은 무엇인가?

A.
SLO에서 허용하는 실패 여유분이다.

Q. 홈서버에서 Error Budget을 어떻게 쓰는가?

A.
장애가 반복되면 새 기능 추가보다 안정화, 백업, 복구, 자동화를 우선하는 기준으로 쓸 수 있다.

---

# 12. Service Health Rules

## 12.1 Service Health 작성 규칙

### [개념]

Service Health는 서비스가 정상 상태인지 판단하는 기준이다.

단순 프로세스 생존보다 핵심 기능 사용 가능 여부를 우선한다.

---

### [핵심]

필수 포함:

- Health Check
- Readiness
- Liveness
- Smoke Test
- Core Function
- Dependency Health
- User Journey

---

### [실무]

Home Server Health Check 예시:

```text
Docker Container Up
→ Port Listening
→ Web UI 접속
→ Login 가능
→ RAG 문서 검색 가능
→ Ollama 응답 가능
→ Backup Job 최근 성공
```

Application Health Check 예시:

```text
/actuator/health
→ DB 연결 확인
→ Redis 연결 확인
→ 외부 API 상태 확인
→ 핵심 API Smoke Test
```

---

### [주의]

Health Check가 너무 얕으면 장애를 놓친다.

Health Check가 너무 깊으면 외부 의존성 장애 때문에 서비스 전체가 불필요하게 Unhealthy로 표시될 수 있다.

---

### [FAQ]

Q. Service Health는 무엇으로 판단하는가?

A.
핵심 기능이 실제로 동작하는지, 주요 의존성이 정상인지, 사용자 관점에서 서비스가 사용 가능한지를 기준으로 판단한다.

Q. 프로세스가 살아 있으면 건강한 서비스인가?

A.
아니다. 핵심 기능이 실패하면 프로세스가 살아 있어도 서비스는 비정상일 수 있다.

---

# 13. Alerting Rules

## 13.1 SRE Alerting 작성 규칙

### [개념]

SRE에서 Alert는 즉시 행동이 필요한 신뢰성 문제를 알려야 한다.

모든 이상 지표가 Alert가 되어서는 안 된다.

---

### [핵심]

좋은 Alert 기준:

- 사용자 영향 있음
- 즉시 조치 필요
- 원인 확인 경로 있음
- 담당자 명확
- Runbook 존재
- 중복 적음
- 임계치 현실적

---

### [실무]

Alert 대상 예시:

```text
Critical
- 핵심 서비스 Down
- 최근 백업 없음
- DB 연결 실패
- Error Rate 급증
- 디스크 사용량 90% 이상
- Docker 핵심 Container 반복 재시작

Warning
- Latency 증가
- 메모리 사용량 지속 증가
- 백업 지연
- 로그 저장소 증가
- SSL 인증서 만료 임박
```

---

### [주의]

Alert Fatigue를 피한다.

나쁜 Alert:

- 조치할 수 없음
- 너무 자주 울림
- 사용자 영향 없음
- Runbook 없음
- 임계치가 너무 낮음
- 매 배포마다 반복됨

---

### [FAQ]

Q. 좋은 SRE Alert는 무엇인가?

A.
사용자 영향이 있고 즉시 대응이 필요하며 Runbook과 담당자가 명확한 Alert이다.

Q. 모든 Error Log를 Alert로 보내도 되는가?

A.
아니다. 반복성과 영향도, Error Rate, 사용자 영향을 기준으로 Alert를 설계해야 한다.

---

# 14. Incident Response Rules

## 14.1 Incident Response 작성 규칙

### [개념]

Incident Response는 서비스 장애나 신뢰성 문제가 발생했을 때 영향 범위를 파악하고 복구하는 절차이다.

---

### [핵심]

필수 포함:

- Detection
- Triage
- Impact Assessment
- Mitigation
- Recovery
- Communication
- Postmortem
- Prevention

---

### [Flow]

```text
Alert
→ Triage
→ Impact Assessment
→ Mitigation
→ Recovery
→ Verification
→ Postmortem
```

---

### [실무]

개인 홈서버 Incident 대응 순서:

```text
1. 어떤 서비스가 안 되는지 확인
2. 최근 변경 사항 확인
3. Docker Container 상태 확인
4. 로그 확인
5. 디스크 / 메모리 / 네트워크 확인
6. 필요 시 재시작
7. 복구 안 되면 백업 / Rollback 확인
8. 복구 후 원인 기록
9. 재발 방지 Action 작성
```

---

### [FAQ]

Q. Incident Response에서 가장 먼저 할 일은?

A.
영향 범위를 확인하고 사용자 또는 본인이 실제로 겪는 핵심 기능 장애를 파악하는 것이다.

Q. 장애 중 원인 분석과 복구 중 무엇이 먼저인가?

A.
사용자 영향이 크면 완전한 원인 분석보다 영향 완화와 복구가 먼저이다.

---

# 15. Incident Severity Rules

## 15.1 Incident Severity 작성 규칙

### [개념]

Incident Severity는 장애의 심각도를 분류하는 기준이다.

Severity는 대응 우선순위와 알림 강도를 결정한다.

---

### [핵심]

Severity 예시:

| Severity | 의미                                | 예                                      |
| -------- | ----------------------------------- | --------------------------------------- |
| SEV1     | 전체 서비스 중단 / 데이터 손실 위험 | DB 손상, 홈서버 부팅 불가               |
| SEV2     | 핵심 기능 장애                      | AnythingLLM 접속 불가, Ollama 응답 불가 |
| SEV3     | 일부 기능 장애                      | 특정 Workspace 오류, 외부 접속만 실패   |
| SEV4     | 낮은 영향                           | 로그 경고, 문서 일부 누락               |

---

### [실무]

홈서버 Severity 기준:

```text
SEV1
→ 데이터 손실, 백업 없음, 서버 부팅 불가

SEV2
→ AI 서버 핵심 기능 중단

SEV3
→ 외부 접속 장애, 특정 Container 장애

SEV4
→ 성능 저하, 경고 로그, 정리 필요
```

---

### [FAQ]

Q. Incident Severity는 왜 필요한가?

A.
장애의 심각도에 따라 대응 우선순위와 복구 속도를 정하기 위해 필요하다.

Q. 홈서버에서 SEV1은 어떤 상황인가?

A.
데이터 손실, SSD 고장, DB 손상, 백업 실패와 같이 복구 가능성에 직접 영향을 주는 상황이다.

---

# 16. Runbook Rules

## 16.1 Runbook 작성 규칙

### [개념]

Runbook은 장애나 운영 작업이 발생했을 때 따라야 하는 표준 절차이다.

SRE에서 Runbook은 빠른 복구와 운영 일관성을 위한 핵심 문서이다.

---

### [핵심]

필수 포함:

- Scenario
- Impact
- Detection
- Initial Check
- Recovery Steps
- Validation
- Escalation
- Last Tested

---

### [실무]

Runbook 기본 구조:

```text
Scenario:
Impact:
Detection:
Initial Check:
Recovery Steps:
Validation:
Rollback:
Escalation:
Last Tested:
```

홈서버 Runbook 대상:

- AnythingLLM 접속 불가
- Ollama 응답 실패
- Docker Container Down
- DB 연결 실패
- 디스크 용량 부족
- 백업 실패
- 외부 접속 실패
- SSL 인증서 만료
- RAG 문서 복구

---

### [FAQ]

Q. Runbook은 왜 필요한가?

A.
장애 상황에서 기억에 의존하지 않고 빠르고 일관되게 복구하기 위해 필요하다.

Q. 개인 홈서버에도 Runbook이 필요한가?

A.
필요하다. 특히 자주 발생하는 장애나 복구 절차가 긴 작업은 Runbook으로 남기는 것이 좋다.

---

# 17. Postmortem Rules

## 17.1 Postmortem 작성 규칙

### [개념]

Postmortem은 장애 이후 원인, 영향, 대응, 개선점을 기록하는 문서이다.

목적은 책임 추궁이 아니라 재발 방지이다.

---

### [핵심]

필수 포함:

- Summary
- Impact
- Timeline
- Root Cause
- Detection
- Response
- Recovery
- What Went Well
- What Went Wrong
- Action Items

---

### [실무]

Postmortem Template:

```text
Incident:
Date:
Severity:
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

개인 홈서버용 경량 기록:

```text
장애:
원인:
복구 방법:
걸린 시간:
다음에 자동화할 것:
```

---

### [FAQ]

Q. Postmortem은 왜 작성하는가?

A.
장애 원인과 대응 과정을 기록하고 재발 방지 Action Item을 만들기 위해 작성한다.

Q. 작은 홈서버 장애도 Postmortem을 써야 하는가?

A.
반복되거나 복구에 오래 걸린 장애는 짧게라도 기록하는 것이 좋다.

---

# 18. Toil Rules

## 18.1 Toil 작성 규칙

### [개념]

Toil은 반복적이고 수동이며 자동화 가능하지만 장기적으로 가치를 만들지 않는 운영 작업이다.

SRE는 Toil을 줄이고 자동화하는 것을 중요하게 본다.

---

### [핵심]

Toil 특성:

- Manual
- Repetitive
- Automatable
- Tactical
- No Long-term Value
- Scales Linearly

---

### [실무]

홈서버 Toil 예시:

```text
매번 수동으로 Container 재시작
매번 수동으로 백업 실행
디스크 용량을 직접 확인
로그 파일을 매번 직접 뒤짐
업데이트 전 체크리스트를 매번 기억에 의존
S3 백업 업로드를 수동 실행
도메인 / 인증서 만료를 수동 확인
```

자동화 후보:

```text
백업 Cron
Docker restart policy
디스크 용량 Alert
Health Check Script
Backup Verification Script
Release Checklist Template
Log Rotation
SSL 만료 알림
```

---

### [FAQ]

Q. Toil은 무엇인가?

A.
반복적이고 수동이며 자동화 가능하지만 장기 가치가 낮은 운영 작업이다.

Q. 홈서버에서 줄여야 할 Toil은 무엇인가?

A.
수동 백업, 수동 재시작, 수동 로그 확인, 수동 용량 확인, 수동 업데이트 체크 같은 반복 작업이다.

---

# 19. Automation Rules

## 19.1 Automation 작성 규칙

### [개념]

Automation은 반복 운영 작업을 Script, Scheduler, CI/CD, Monitoring, Self-healing으로 자동화하는 것이다.

SRE에서 자동화는 신뢰성을 높이고 Toil을 줄이기 위한 수단이다.

---

### [핵심]

자동화 대상:

- Backup
- Health Check
- Restart
- Log Rotation
- Alerting
- Deployment
- Rollback
- Cleanup
- Report

---

### [실무]

홈서버 자동화 예시:

```text
Daily Backup
→ cron + backup script

Container Recovery
→ restart: unless-stopped

Disk Alert
→ script + notification

Backup Verification
→ checksum + tar test

Release Checklist
→ markdown template

Monthly Cost Review
→ billing check reminder

Restore Test
→ quarterly runbook test
```

Docker Compose 예시:

```yaml
services:
  app:
    restart: unless-stopped
```

---

### [주의]

자동화는 검증 없이 만들면 장애를 자동으로 반복할 수 있다.

자동화 전 확인:

- 실패 시 멈추는 조건
- 로그 기록
- 알림
- Rollback 가능성
- 수동 개입 방법
- Secret 보호

---

### [FAQ]

Q. 자동화는 언제 해야 하는가?

A.
반복되고 실수 가능성이 높으며 복구나 안정성에 중요한 작업부터 자동화한다.

Q. 모든 것을 자동화해야 하는가?

A.
아니다. 위험한 작업은 승인이나 수동 확인을 남겨야 한다.

---

# 20. Capacity Planning Rules

## 20.1 Capacity Planning 작성 규칙

### [개념]

Capacity Planning은 서비스가 필요한 리소스를 안정적으로 확보하도록 CPU, Memory, Disk, Network, DB Connection, GPU / VRAM 사용량을 계획하는 작업이다.

---

### [핵심]

필수 포함:

- CPU
- Memory
- Disk
- Network
- Database Connection
- Queue
- GPU / VRAM
- Headroom
- Growth Trend

---

### [실무]

홈서버 Capacity 대상:

```text
RAM
→ Ollama 모델 실행
→ AnythingLLM
→ Docker Container

Disk
→ RAG 문서
→ Vector DB
→ Docker Image
→ Backup Archive

CPU
→ LLM 추론
→ Embedding 처리
→ DB / API

Network
→ 외부 접속
→ Cloud Backup Upload

GPU / UMA
→ 모델 상주 가능성
→ VRAM 할당
```

---

### [주의]

디스크 용량 부족은 홈서버 장애의 흔한 원인이다.

주의 대상:

- Docker Image 누적
- Docker Volume 증가
- Log 누적
- Backup 파일 누적
- Model 파일 증가
- Vector DB 증가

---

### [FAQ]

Q. Capacity Planning은 왜 필요한가?

A.
리소스 부족으로 서비스가 느려지거나 중단되는 것을 예방하기 위해 필요하다.

Q. 홈서버에서 가장 먼저 봐야 할 Capacity는?

A.
Disk, RAM, Docker Volume, Backup 저장소, 모델 파일 크기, 로그 증가량을 먼저 본다.

---

# 21. Change Management Rules

## 21.1 Change Management 작성 규칙

### [개념]

Change Management는 서비스에 영향을 주는 변경을 계획, 검토, 적용, 검증하는 운영 기준이다.

SRE에서는 변경이 장애의 주요 원인이라는 전제를 둔다.

---

### [핵심]

필수 포함:

- Change Risk
- Release
- Deployment
- Migration
- Config Change
- Approval
- Rollback
- Verification

---

### [실무]

변경 전 확인:

```text
무엇을 바꾸는가?
영향 범위는 어디인가?
백업이 있는가?
Rollback 가능한가?
Monitoring 준비됐는가?
배포 후 무엇을 확인할 것인가?
```

High Risk Change:

- DB Migration
- 인증 / 권한 변경
- Docker Volume 구조 변경
- Reverse Proxy 변경
- Secret 변경
- 모델 / Vector DB 구조 변경
- 홈서버 네트워크 변경

---

### [FAQ]

Q. Change Management는 왜 필요한가?

A.
많은 장애가 변경 직후 발생하므로 변경 전 위험과 복구 방법을 확인하기 위해 필요하다.

Q. 홈서버에서도 Change Management가 필요한가?

A.
가볍게 필요하다. 특히 업데이트 전 백업과 Rollback 가능성 확인은 중요하다.

---

# 22. Deployment Reliability Rules

## 22.1 Deployment Reliability 작성 규칙

### [개념]

Deployment Reliability는 배포가 서비스 장애를 만들지 않도록 관리하는 신뢰성 기준이다.

Deployment Strategy와 연결되지만 SRE에서는 배포가 SLO와 Incident에 미치는 영향을 중심으로 본다.

---

### [핵심]

필수 포함:

- Deployment Risk
- Release Verification
- Rollback
- Canary
- Blue-Green
- Health Check
- Error Rate
- Change Failure Rate

---

### [실무]

배포 신뢰성 지표:

- 배포 성공률
- 배포 후 Incident 발생률
- Rollback 횟수
- 배포 후 Error Rate 증가
- 배포 후 Latency 증가
- 배포 후 사용자 불만
- Change Failure Rate
- Mean Time To Recovery

배포 후 확인 Flow:

```text
Deploy
→ Health Check
→ Smoke Test
→ Error Rate
→ Latency
→ Logs
→ SLO Impact
→ Complete or Rollback
```

---

### [FAQ]

Q. Deployment Reliability는 무엇인가?

A.
배포가 서비스 장애를 만들지 않도록 배포 전후 검증과 복구 기준을 관리하는 것이다.

Q. 배포 후 SRE 관점에서 무엇을 확인해야 하는가?

A.
Error Rate, Latency, Health Check, 핵심 기능, SLO 영향, Rollback 필요성을 확인해야 한다.

---

# 23. Backup Reliability Rules

## 23.1 Backup Reliability 작성 규칙

### [개념]

Backup Reliability는 백업이 정해진 주기에 성공하고 실제로 복구 가능한 상태인지 관리하는 신뢰성 기준이다.

---

### [핵심]

필수 포함:

- Backup Success Rate
- Last Backup Time
- Restore Test
- Backup Freshness
- Backup Integrity
- Recovery Runbook

---

### [실무]

Backup Reliability SLI 예시:

```text
Backup Success Rate
→ 최근 30일 백업 성공률

Backup Freshness
→ 마지막 백업이 24시간 이내인지

Restore Test Success
→ 최근 복구 테스트 성공 여부

Backup Integrity
→ Checksum / 압축 무결성 확인
```

홈서버 SLO 예시:

```text
최근 24시간 내 RAG 문서 백업 존재
최근 7일 내 DB 백업 존재
최근 90일 내 Restore Test 1회 이상
```

---

### [FAQ]

Q. Backup Reliability는 왜 SRE에 포함되는가?

A.
서비스 신뢰성은 장애 후 복구 가능성까지 포함하므로 백업 성공과 복구 테스트가 중요하다.

Q. 백업 파일이 있으면 Backup Reliability가 높은가?

A.
아니다. 최신성, 무결성, 복구 테스트가 확인되어야 한다.

---

# 24. Home Server Reliability Rules

## 24.1 Home Server Reliability 작성 규칙

### [개념]

Home Server Reliability는 개인 홈서버가 필요한 기능을 안정적으로 제공하고 장애 시 복구 가능한 상태를 유지하는 기준이다.

---

### [핵심]

필수 포함:

- Home Server
- Docker Health
- Auto Restart
- Backup
- Disk Monitoring
- Network Health
- Power Failure
- Recovery Plan
- Documentation

---

### [실무]

홈서버 Reliability Checklist:

```text
[ ] Docker 핵심 Container 자동 재시작 설정
[ ] 백업 자동화
[ ] 백업 실패 알림
[ ] 디스크 용량 확인
[ ] 로그 Rotation 설정
[ ] 외부 접속 경로 문서화
[ ] DNS / Tunnel 설정 기록
[ ] Secret 복구 방법 기록
[ ] 복구 Runbook 작성
[ ] 업데이트 전 백업 절차 존재
```

홈서버 장애 우선순위:

```text
Data Loss Risk
→ Backup / Restore 우선

Service Down
→ Container / Logs / Health Check

External Access Down
→ DNS / Tunnel / Router / Firewall

Performance Issue
→ CPU / RAM / Disk / Model Load
```

---

### [FAQ]

Q. 홈서버 Reliability에서 가장 중요한 것은?

A.
데이터 보존, 백업, 복구 절차, Docker 자동 재시작, 디스크 용량 관리, 외부 접속 설정 기록이다.

Q. 홈서버는 개인용이라 장애 기록이 필요 없는가?

A.
반복 장애나 복구가 어려웠던 장애는 기록하는 것이 좋다. 나중에 같은 문제를 빠르게 해결할 수 있다.

---

# 25. AI Server Reliability Rules

## 25.1 AI Server Reliability 작성 규칙

### [개념]

AI Server Reliability는 Ollama, AnythingLLM, Vector DB, RAG 문서, Embedding Pipeline이 안정적으로 동작하도록 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Ollama Health
- LLM Response
- Embedding Model
- Vector DB
- RAG Documents
- AnythingLLM Storage
- Model Availability
- Memory Pressure

---

### [실무]

AI Server Health Check:

```text
Ollama API 응답 확인
모델 목록 확인
Qwen 모델 응답 확인
BGE-M3 Embedding 가능 여부 확인
AnythingLLM 접속 확인
Workspace 문서 검색 확인
Vector DB 데이터 존재 확인
RAG 원본 문서 백업 확인
```

AI 서버 장애 원인:

- RAM 부족
- Model Load 실패
- Ollama Daemon 중단
- AnythingLLM Container 중단
- Vector DB 손상
- RAG 문서 누락
- Docker Volume 손상
- Disk Full
- 권한 문제

---

### [FAQ]

Q. AI Server Reliability에서 가장 중요한 지표는?

A.
LLM 응답 가능 여부, RAG 검색 성공 여부, AnythingLLM Storage 보존, 모델 로드 가능 여부, 디스크 / 메모리 상태이다.

Q. 모델 파일 자체도 고신뢰 백업 대상인가?

A.
재다운로드 가능하면 우선순위는 낮다. 대신 모델 이름, 태그, 설정, RAG 문서, Workspace 데이터는 중요하다.

---

# 26. Toil Reduction Priority Rules

## 26.1 Toil Reduction Priority 작성 규칙

### [개념]

Toil Reduction Priority는 어떤 반복 작업을 먼저 자동화할지 결정하는 기준이다.

자동화는 비용이 들기 때문에 신뢰성 효과가 큰 작업부터 진행한다.

---

### [핵심]

우선순위 기준:

- 장애 예방 효과
- 복구 시간 단축 효과
- 반복 빈도
- 실수 가능성
- 자동화 난이도
- 데이터 손실 위험
- 보안 영향

---

### [실무]

우선 자동화 대상:

```text
1. 백업 자동화
2. 백업 성공 / 실패 알림
3. Docker Container 자동 재시작
4. 디스크 용량 알림
5. 로그 Rotation
6. 업데이트 전 Checklist
7. Restore Test Runbook
8. 비용 알림
9. SSL 인증서 만료 알림
```

낮은 우선순위:

```text
자주 안 쓰는 임시 작업
위험한 자동 삭제
복잡하지만 효과 적은 자동화
수동 확인이 필요한 보안 작업
```

---

### [FAQ]

Q. 어떤 Toil을 먼저 자동화해야 하는가?

A.
장애 예방, 데이터 보호, 복구 시간 단축에 직접 도움이 되는 반복 작업을 먼저 자동화한다.

Q. 자동 삭제 작업도 자동화해도 되는가?

A.
주의해야 한다. 삭제 자동화는 백업, 승인, 로그, 복구 가능성을 함께 설계해야 한다.

---

# 27. Reliability Metrics Rules

## 27.1 Reliability Metrics 작성 규칙

### [개념]

Reliability Metrics는 서비스 신뢰성을 측정하는 지표이다.

Metrics는 SLO와 Incident 판단의 근거가 된다.

---

### [핵심]

대표 지표:

- Availability
- Error Rate
- Latency
- Request Success Rate
- MTTR
- MTTD
- Change Failure Rate
- Backup Success Rate
- Restore Test Success
- Incident Count

---

### [실무]

지표 설명:

| 지표                 | 의미                              |
| -------------------- | --------------------------------- |
| MTTD                 | 장애를 감지하는 데 걸린 평균 시간 |
| MTTR                 | 장애를 복구하는 데 걸린 평균 시간 |
| Change Failure Rate  | 변경 후 장애가 발생한 비율        |
| Backup Success Rate  | 백업 성공률                       |
| Restore Test Success | 복구 테스트 성공 여부             |
| Incident Count       | 일정 기간 장애 건수               |

홈서버에 유용한 지표:

```text
최근 장애 횟수
최근 복구 시간
최근 백업 성공 시각
디스크 사용률
Container 재시작 횟수
최근 업데이트 후 문제 발생 여부
```

---

### [FAQ]

Q. MTTR은 무엇인가?

A.
Mean Time To Recovery로 장애 발생 후 복구까지 걸리는 평균 시간이다.

Q. 개인 홈서버에서 Reliability Metric은 무엇을 보면 되는가?

A.
장애 횟수, 복구 시간, 백업 성공 여부, 디스크 사용률, Container 재시작 횟수를 보면 충분하다.

---

# 28. Reliability Review Rules

## 28.1 Reliability Review 작성 규칙

### [개념]

Reliability Review는 서비스가 안정적으로 운영될 수 있는지 사전에 검토하는 절차이다.

배포 전, 인프라 변경 전, 홈서버 구조 변경 전에 수행한다.

---

### [핵심]

검토 대상:

- Single Point of Failure
- Backup
- Restore
- Monitoring
- Alert
- Runbook
- Capacity
- Security
- Cost
- Change Risk

---

### [실무]

Reliability Review Checklist:

```text
[ ] 핵심 서비스 Health Check 존재
[ ] 백업 존재
[ ] Restore Test 수행
[ ] Rollback 가능
[ ] 로그 확인 가능
[ ] Alert 기준 존재
[ ] 디스크 용량 충분
[ ] Memory 여유 있음
[ ] Secret 복구 가능
[ ] 장애 대응 Runbook 존재
[ ] 최근 변경 사항 기록
```

---

### [FAQ]

Q. Reliability Review는 언제 해야 하는가?

A.
큰 배포, DB Migration, 홈서버 구조 변경, 백업 정책 변경, 외부 공개 전 수행하는 것이 좋다.

Q. Reliability Review에서 가장 먼저 볼 것은?

A.
백업, 복구 가능성, Health Check, Monitoring, Rollback, 디스크 / 메모리 여유를 먼저 본다.

---

# 29. Operational Readiness Rules

## 29.1 Operational Readiness 작성 규칙

### [개념]

Operational Readiness는 서비스가 운영 가능한 상태인지 확인하는 준비 기준이다.

개발 완료와 운영 준비는 다르다.

---

### [핵심]

필수 포함:

- Health Check
- Monitoring
- Logging
- Alerting
- Backup
- Runbook
- Rollback
- Security
- Cost Alert
- Documentation

---

### [실무]

운영 준비 Checklist:

```text
[ ] Health Check 가능
[ ] 로그 확인 가능
[ ] 주요 지표 확인 가능
[ ] Alert 설정
[ ] 백업 자동화
[ ] 복구 절차 문서화
[ ] Rollback 대상 존재
[ ] Secret 관리
[ ] 비용 알림
[ ] 장애 대응 절차
```

홈서버 운영 준비:

```text
[ ] Docker Compose 재현 가능
[ ] Volume 백업 가능
[ ] 외부 접속 설정 기록
[ ] 도메인 / DNS 기록
[ ] 관리자 URL 보호
[ ] 업데이트 전 백업 절차
```

---

### [FAQ]

Q. Operational Readiness는 무엇인가?

A.
서비스가 운영 환경에서 감시, 복구, 보안, 비용 관리가 가능한 상태인지 확인하는 기준이다.

Q. 개발이 끝나면 운영 준비도 끝난 것인가?

A.
아니다. Monitoring, Backup, Runbook, Rollback, Security가 준비되어야 운영 가능하다고 볼 수 있다.

---

# 30. Cost / Reliability Trade-off Rules

## 30.1 비용과 신뢰성 균형 규칙

### [개념]

Cost / Reliability Trade-off는 비용 절감과 서비스 신뢰성 사이의 균형을 판단하는 기준이다.

SRE는 무조건 비용을 줄이거나 무조건 안정성을 높이는 것이 아니라 목표에 맞는 균형을 선택한다.

---

### [핵심]

비용 절감 시 유지해야 할 것:

- 최소 백업
- 핵심 Monitoring
- 장애 로그
- 복구 절차
- 보안 로그
- Rollback 대상
- 디스크 여유

---

### [실무]

좋은 비용 절감:

```text
오래된 로그 Retention 조정
미사용 리소스 삭제
Docker Image 정리
낮은 우선순위 백업 보존 기간 조정
Right Sizing
API Cache 적용
```

나쁜 비용 절감:

```text
백업 제거
Monitoring 제거
Security Log 제거
복구 테스트 제거
운영 DB 암호화 해제
디스크 여유 없이 운영
```

---

### [FAQ]

Q. 비용을 줄이려고 백업을 꺼도 되는가?

A.
권장하지 않는다. 백업 범위와 보존 기간을 조정하되 핵심 데이터 백업은 유지해야 한다.

Q. 신뢰성을 높이면 항상 비용이 증가하는가?

A.
항상 그렇지는 않다. 자동화, 정리, 적절한 모니터링은 비용 증가 없이 신뢰성을 높일 수 있다.

---

# 31. Troubleshooting Rules

## 31.1 SRE Troubleshooting 작성 규칙

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

- Service Down
- Alert Not Firing
- Alert Too Noisy
- High Error Rate
- High Latency
- Backup Not Reliable
- Repeated Incident
- Container Restart Loop
- Disk Full
- Memory Pressure
- Deployment Caused Incident
- No Runbook
- No Postmortem
- Toil Too High

---

### [실무]

기본 확인 흐름:

```text
Symptom
→ User Impact
→ Recent Change
→ Health Check
→ Logs
→ Metrics
→ Dependencies
→ Recovery
→ Postmortem
```

---

### [Troubleshooting]

문제:
서비스가 자주 죽는다.

원인:

- Memory 부족
- Disk Full
- Container Restart Policy 없음
- Application Crash
- Dependency 장애
- 설정 오류
- 배포 후 버그

해결:

```text
Container 상태 확인
→ Logs 확인
→ Memory / Disk 확인
→ 최근 변경 확인
→ Restart Policy 설정
→ Root Cause 기록
```

문제:
Alert가 울리지 않는다.

원인:

- Alert Rule 없음
- 임계치 부적절
- Monitoring Target 누락
- Notification 설정 오류
- Health Check가 너무 얕음

해결:

```text
Monitoring Target 확인
→ Metric 수집 확인
→ Alert Rule 확인
→ Notification Test
→ Runbook 연결
```

문제:
Alert가 너무 자주 울린다.

원인:

- 임계치가 너무 낮음
- 사용자 영향 없는 Alert
- 중복 Alert
- 지속 시간 조건 없음
- 배포 중 일시 변동 미고려

해결:

```text
Alert별 사용자 영향 확인
→ Threshold 조정
→ For Duration 추가
→ 중복 제거
→ Severity 분리
```

문제:
장애가 반복된다.

원인:

- Postmortem 없음
- Action Item 미완료
- 임시 조치만 반복
- 자동화 없음
- 근본 원인 미해결

해결:

```text
최근 Incident 기록 확인
→ 공통 원인 추출
→ Action Item 작성
→ 자동화 / 구조 개선
→ 재발 여부 추적
```

문제:
백업이 신뢰되지 않는다.

원인:

- Restore Test 없음
- 백업 실패 알림 없음
- 백업 파일 무결성 확인 없음
- 오래된 백업만 존재
- 백업 대상 누락

해결:

```text
최근 백업 확인
→ 무결성 확인
→ Test Restore 수행
→ Backup Alert 추가
→ 백업 대상 재검토
```

---

### [FAQ]

Q. SRE Troubleshooting에서 가장 먼저 확인할 것은?

A.
사용자 영향, 최근 변경, Health Check, 로그, Metrics, 의존성 상태를 먼저 확인한다.

Q. 장애가 반복되면 어떻게 해야 하는가?

A.
Postmortem을 작성하고 공통 원인을 찾아 자동화 또는 구조 개선 Action Item을 실행해야 한다.

---

# 32. Common Mistakes

## 32.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 SRE 관점에서 운영 구조를 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- Monitoring 없이 운영
- Alert 없이 Dashboard만 존재
- Runbook 없음
- Postmortem 없음
- 백업은 있지만 Restore Test 없음
- SLO 없이 감으로 운영
- 장애 후 기록 없음
- 같은 장애 반복
- 수동 재시작 반복
- 디스크 용량 알림 없음
- Error Rate 기준 없음
- 배포 후 검증 없음
- 변경 전 백업 없음
- 비용 절감으로 핵심 로그 제거
- Container restart policy 없음
- 최근 변경 기록 없음
- 홈서버 외부 접속 설정 문서화 없음
- Secret 복구 절차 없음

---

### [실무]

Review Agent 검토 기준:

```text
SLI / SLO
→ Monitoring
→ Alert
→ Runbook
→ Backup
→ Restore Test
→ Incident Record
→ Postmortem
→ Automation
```

---

### [FAQ]

Q. SRE Review에서 가장 먼저 확인할 것은?

A.
Monitoring, Alert, Backup, Restore Test, Runbook, 최근 장애 기록, 반복 수동 작업을 먼저 확인한다.

Q. SRE 관점에서 가장 위험한 착각은?

A.
서비스가 지금 켜져 있다는 이유만으로 신뢰성이 충분하다고 생각하는 것이다.

---

# 33. File Relationship Rules

## 33.1 다른 Domain Rules와 연계

### [개념]

Site Reliability Engineering Domain Rules는 DevOps Expert 문서 체계에서 Monitoring & Logging, Deployment Strategy, Backup / Disaster Recovery, Security Operations, Cost Optimization / FinOps, Cloud Provider와 연결된다.

---

### [핵심]

연계 구조:

```text
SRE
→ SLI / SLO
→ Monitoring / Alert
→ Incident Response
→ Backup / Recovery
→ Postmortem
→ Automation
```

---

### [실무]

파일 간 역할 분리:

| Domain                       | 역할                                       |
| ---------------------------- | ------------------------------------------ |
| Site Reliability Engineering | 신뢰성 목표, 장애 대응, 자동화, 운영 개선  |
| Monitoring & Logging         | Metrics, Logs, Traces, Alert, Dashboard    |
| Deployment Strategy          | 배포 방식, Rollback, 배포 후 검증          |
| Backup / Disaster Recovery   | 백업, 복구, RPO / RTO, Restore Test        |
| Security Operations          | 보안 사고 대응, Audit, Security Alert      |
| Cost Optimization / FinOps   | 비용과 신뢰성 균형                         |
| Cloud Provider               | Cloud Resource 신뢰성, Region, Monitoring  |
| Release Management           | Release 기록, Rollback Target, Change Risk |

---

### [FAQ]

Q. SRE와 Monitoring & Logging은 어떻게 연결되는가?

A.
Monitoring & Logging이 수집한 Metrics, Logs, Alert를 SRE가 SLO 판단, 장애 대응, 개선 활동에 사용한다.

Q. SRE와 Backup / DR은 어떻게 연결되는가?

A.
서비스 신뢰성은 장애 후 복구 가능성을 포함하므로 Backup Success, Restore Test, Recovery Runbook이 SRE 기준에 포함된다.

Q. SRE와 FinOps는 어떻게 연결되는가?

A.
비용 최적화가 신뢰성을 해치지 않도록 백업, 모니터링, 보안 로그, 복구 가능성을 유지하는 기준에서 연결된다.

---

# 34. Retrieval Optimization Rules

## 34.1 Retrieval 최적화 규칙

### [개념]

SRE 문서는 신뢰성, 장애 대응, SLO, 자동화, 홈서버 안정성 문제 검색에 강해야 한다.

사용자 질문은 주로 “서비스가 자주 죽는다”, “SLO가 뭐냐”, “Alert 기준”, “장애 기록”, “자동화할 것”, “홈서버 안정화” 형태로 들어온다.

---

### [핵심]

강조 대상:

- Site Reliability Engineering
- SRE
- Reliability
- Availability
- Resilience
- SLI
- SLO
- SLA
- Error Budget
- Incident Response
- Runbook
- Postmortem
- Toil
- Automation
- Capacity Planning
- Change Management
- Home Server Reliability
- AI Server Reliability

---

### [실무]

반복 허용 키워드:

- SRE
- 서비스 신뢰성
- 홈서버 안정화
- SLO 설정
- SLI 지표
- Error Budget
- Incident Response
- 장애 대응
- Postmortem
- Runbook
- Toil Reduction
- 운영 자동화
- Docker 자동 재시작
- 백업 신뢰성
- Restore Test
- 배포 신뢰성
- Alert 기준
- MTTR
- MTTD

---

### [FAQ]

Q. SRE RAG 문서는 어떤 질문에 강해야 하는가?

A.
서비스 신뢰성, SLI / SLO, Error Budget, 장애 대응, Runbook, Postmortem, Toil, 자동화, 홈서버 안정화 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
SRE, Reliability, SLI, SLO, Error Budget, Incident, Runbook, Postmortem, Toil, Automation, Home Server Reliability 키워드를 반복할 수 있다.

---

# 35. Version Rules

## 35.1 버전 기준

### [개념]

SRE 문서는 Modern Reliability Engineering 기준과 개인 홈서버 경량 운영 기준을 함께 따른다.

---

### [핵심]

기준:

- SLI / SLO
- Error Budget
- Monitoring / Alerting
- Incident Response
- Postmortem
- Toil Reduction
- Automation
- Backup Reliability
- Deployment Reliability
- Home Server Reliability
- Cost / Reliability Balance

---

### [실무]

Legacy 또는 낮은 우선순위:

- 장애 발생 후 기억에만 의존
- 로그 직접 확인만 수행
- Alert 없이 수동 확인
- 백업 성공 여부 미확인
- Restore Test 없음
- Postmortem 없음
- Runbook 없음
- 반복 수동 작업 방치
- 장애 원인 기록 없음
- 서비스 상태 기준 없음

---

### [FAQ]

Q. SRE 문서에서 Modern 기준은 무엇인가?

A.
SLI / SLO, Monitoring, Alert, Incident Response, Postmortem, Toil Reduction, Automation, Backup Reliability를 포함하는 것이다.

Q. 개인 홈서버에 대기업식 SRE가 필요한가?

A.
아니다. 개인 홈서버에는 경량 SRE 기준으로 장애 감지, 백업, 복구, 기록, 자동화만 적용해도 충분하다.

---

# 36. Quality Checklist

## 36.1 최종 검수 기준

### [개념]

SRE RAG 문서는 Agent가 서비스 신뢰성을 정의하고 장애 대응과 자동화를 설계할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- SRE Scope 충족
- SLI / SLO / SLA 포함
- Error Budget 포함
- Reliability / Availability / Resilience 포함
- Incident Response 포함
- Runbook 포함
- Postmortem 포함
- Toil / Automation 포함
- Capacity Planning 포함
- Change Management 포함
- Home Server Reliability 포함
- AI Server Reliability 포함
- Backup Reliability 포함
- Deployment Reliability 포함
- Troubleshooting 포함
- Monitoring & Logging Domain Rules와 연결
- Backup / Disaster Recovery Domain Rules와 연결
- Deployment Strategy Domain Rules와 연결
- Cost Optimization / FinOps Domain Rules와 연결
- Security Operations Domain Rules와 연결
- FAQ 포함
- Retrieval Queries 포함
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

Q. SRE 문서 품질은 무엇으로 판단하는가?

A.
Agent가 SLI / SLO, 장애 대응, Runbook, Postmortem, Toil 자동화, 홈서버 안정화 기준을 제안할 수 있으면 품질이 높다.

---

# 37. Final Goal

## 37.1 최종 목표

### [개념]

Site Reliability Engineering RAG 문서는 단순 운영 철학 문서가 아니다.

DevOps Agent / Backend Agent / Review Agent가 서비스 신뢰성을 정의하고, 장애를 감지 / 복구 / 기록 / 개선하며, 반복 운영 작업을 자동화하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve SRE Workflow
- Define Reliability Goals
- Design SLI / SLO
- Apply Error Budget
- Detect Incident
- Support Incident Response
- Write Runbook
- Write Postmortem
- Identify Toil
- Prioritize Automation
- Review Home Server Reliability
- Review AI Server Reliability
- Balance Cost and Reliability
- Connect SRE with Monitoring / Backup / Deployment

---

### [실무]

최종 연결 흐름:

```text
Service / Home Server
→ Reliability Goal
→ Monitoring Signal
→ Alert
→ Incident Response
→ Recovery
→ Postmortem
→ Toil Reduction
→ Automation
→ Reliability Improvement
```

---

### [FAQ]

Q. SRE 문서의 최종 목적은?

A.
Agent가 서비스와 홈서버의 신뢰성 목표를 세우고, 장애 대응과 자동화를 통해 반복 문제를 줄이도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Site Reliability Engineering Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 서비스 신뢰성, SLI / SLO, 장애 대응, Runbook, Postmortem, 자동화를 수행하기 위한 RAG 작성 규칙이다.

Q. SRE 문서의 핵심 범위는?
A. Reliability, Availability, Resilience, SLI, SLO, Error Budget, Incident Response, Runbook, Postmortem, Toil, Automation, Home Server Reliability이다.

Q. 개인 홈서버에도 SRE가 필요한가?
A. 대기업식 SRE는 필요 없지만 서비스 죽음 감지, 백업, 복구, 자동 재시작, 장애 기록, 반복 작업 자동화에는 유용하다.

Q. SRE와 Monitoring & Logging은 어떻게 다른가?
A. Monitoring & Logging은 관측 도구와 신호를 다루고, SRE는 그 신호를 기준으로 신뢰성 목표, 장애 대응, 개선 활동을 운영한다.

Q. SRE의 핵심은 무엇인가?
A. 서비스 신뢰성을 측정 가능한 목표로 관리하고 장애 대응과 자동화를 통해 반복 문제를 줄이는 것이다.

Q. Reliability는 무엇인가?
A. 서비스가 기대한 기능을 안정적으로 수행하고 장애가 발생해도 복구 가능한 능력이다.

Q. Availability는 무엇인가?
A. 서비스가 사용 가능한 시간의 비율이다.

Q. 서버가 켜져 있으면 Availability가 높은 것인가?
A. 아니다. 사용자가 핵심 기능을 실제로 사용할 수 있어야 한다.

Q. Resilience는 무엇인가?
A. 장애가 발생해도 서비스가 제한적으로 동작하거나 빠르게 복구할 수 있는 능력이다.

Q. SLI는 무엇인가?
A. 서비스 수준을 측정하기 위한 지표이다.

Q. 홈서버에서 쓸만한 SLI는 무엇인가?
A. 서비스 접속 성공, Docker Container 실행 상태, 백업 성공 여부, RAG 검색 성공 여부, Ollama 응답 성공 여부가 유용하다.

Q. SLO는 무엇인가?
A. SLI 지표에 대해 달성하려는 목표값이다.

Q. 개인 홈서버에도 SLO가 필요한가?
A. 복잡한 SLO는 필요 없지만 백업 성공, 서비스 접속, 복구 가능성 같은 간단한 목표는 유용하다.

Q. SLA는 무엇인가?
A. 외부 사용자나 고객과 약속한 서비스 수준 계약이다.

Q. 개인 홈서버에 SLA가 필요한가?
A. 대부분 필요 없다. 대신 내부 목표인 SLO와 복구 절차를 관리하는 것이 현실적이다.

Q. Error Budget은 무엇인가?
A. SLO에서 허용하는 실패 여유분이다.

Q. 홈서버에서 Error Budget을 어떻게 쓰는가?
A. 장애가 반복되면 새 기능 추가보다 안정화, 백업, 복구, 자동화를 우선하는 기준으로 쓸 수 있다.

Q. Service Health는 무엇으로 판단하는가?
A. 핵심 기능이 실제로 동작하는지, 주요 의존성이 정상인지, 사용자 관점에서 서비스가 사용 가능한지를 기준으로 판단한다.

Q. 좋은 SRE Alert는 무엇인가?
A. 사용자 영향이 있고 즉시 대응이 필요하며 Runbook과 담당자가 명확한 Alert이다.

Q. Incident Response에서 가장 먼저 할 일은?
A. 영향 범위를 확인하고 사용자 또는 본인이 실제로 겪는 핵심 기능 장애를 파악하는 것이다.

Q. Incident Severity는 왜 필요한가?
A. 장애의 심각도에 따라 대응 우선순위와 복구 속도를 정하기 위해 필요하다.

Q. 홈서버에서 SEV1은 어떤 상황인가?
A. 데이터 손실, SSD 고장, DB 손상, 백업 실패와 같이 복구 가능성에 직접 영향을 주는 상황이다.

Q. Runbook은 왜 필요한가?
A. 장애 상황에서 기억에 의존하지 않고 빠르고 일관되게 복구하기 위해 필요하다.

Q. Postmortem은 왜 작성하는가?
A. 장애 원인과 대응 과정을 기록하고 재발 방지 Action Item을 만들기 위해 작성한다.

Q. Toil은 무엇인가?
A. 반복적이고 수동이며 자동화 가능하지만 장기 가치가 낮은 운영 작업이다.

Q. 홈서버에서 줄여야 할 Toil은 무엇인가?
A. 수동 백업, 수동 재시작, 수동 로그 확인, 수동 용량 확인, 수동 업데이트 체크 같은 반복 작업이다.

Q. 자동화는 언제 해야 하는가?
A. 반복되고 실수 가능성이 높으며 복구나 안정성에 중요한 작업부터 자동화한다.

Q. 모든 것을 자동화해야 하는가?
A. 아니다. 위험한 작업은 승인이나 수동 확인을 남겨야 한다.

Q. Capacity Planning은 왜 필요한가?
A. 리소스 부족으로 서비스가 느려지거나 중단되는 것을 예방하기 위해 필요하다.

Q. 홈서버에서 가장 먼저 봐야 할 Capacity는?
A. Disk, RAM, Docker Volume, Backup 저장소, 모델 파일 크기, 로그 증가량을 먼저 본다.

Q. Change Management는 왜 필요한가?
A. 많은 장애가 변경 직후 발생하므로 변경 전 위험과 복구 방법을 확인하기 위해 필요하다.

Q. Deployment Reliability는 무엇인가?
A. 배포가 서비스 장애를 만들지 않도록 배포 전후 검증과 복구 기준을 관리하는 것이다.

Q. Backup Reliability는 왜 SRE에 포함되는가?
A. 서비스 신뢰성은 장애 후 복구 가능성까지 포함하므로 백업 성공과 복구 테스트가 중요하다.

Q. 홈서버 Reliability에서 가장 중요한 것은?
A. 데이터 보존, 백업, 복구 절차, Docker 자동 재시작, 디스크 용량 관리, 외부 접속 설정 기록이다.

Q. AI Server Reliability에서 가장 중요한 지표는?
A. LLM 응답 가능 여부, RAG 검색 성공 여부, AnythingLLM Storage 보존, 모델 로드 가능 여부, 디스크 / 메모리 상태이다.

Q. 어떤 Toil을 먼저 자동화해야 하는가?
A. 장애 예방, 데이터 보호, 복구 시간 단축에 직접 도움이 되는 반복 작업을 먼저 자동화한다.

Q. MTTR은 무엇인가?
A. Mean Time To Recovery로 장애 발생 후 복구까지 걸리는 평균 시간이다.

Q. 개인 홈서버에서 Reliability Metric은 무엇을 보면 되는가?
A. 장애 횟수, 복구 시간, 백업 성공 여부, 디스크 사용률, Container 재시작 횟수를 보면 충분하다.

Q. Reliability Review는 언제 해야 하는가?
A. 큰 배포, DB Migration, 홈서버 구조 변경, 백업 정책 변경, 외부 공개 전 수행하는 것이 좋다.

Q. Operational Readiness는 무엇인가?
A. 서비스가 운영 환경에서 감시, 복구, 보안, 비용 관리가 가능한 상태인지 확인하는 기준이다.

Q. 비용을 줄이려고 백업을 꺼도 되는가?
A. 권장하지 않는다. 백업 범위와 보존 기간을 조정하되 핵심 데이터 백업은 유지해야 한다.

Q. SRE Troubleshooting에서 가장 먼저 확인할 것은?
A. 사용자 영향, 최근 변경, Health Check, 로그, Metrics, 의존성 상태를 먼저 확인한다.

Q. 장애가 반복되면 어떻게 해야 하는가?
A. Postmortem을 작성하고 공통 원인을 찾아 자동화 또는 구조 개선 Action Item을 실행해야 한다.

Q. SRE Review에서 가장 먼저 확인할 것은?
A. Monitoring, Alert, Backup, Restore Test, Runbook, 최근 장애 기록, 반복 수동 작업을 먼저 확인한다.

Q. SRE와 Backup / DR은 어떻게 연결되는가?
A. 서비스 신뢰성은 장애 후 복구 가능성을 포함하므로 Backup Success, Restore Test, Recovery Runbook이 SRE 기준에 포함된다.

Q. SRE와 FinOps는 어떻게 연결되는가?
A. 비용 최적화가 신뢰성을 해치지 않도록 백업, 모니터링, 보안 로그, 복구 가능성을 유지하는 기준에서 연결된다.

Q. SRE 문서의 최종 목적은?
A. Agent가 서비스와 홈서버의 신뢰성 목표를 세우고, 장애 대응과 자동화를 통해 반복 문제를 줄이도록 만드는 것이다.
