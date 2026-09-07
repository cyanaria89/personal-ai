# Deployment Strategy Domain Rules

---

# 1. Domain Purpose

## 1.1 Deployment Strategy 문서 목적

### [개념]

Deployment Strategy Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Release Strategy Support
- Deployment Planning Support
- Zero Downtime Deployment Support
- Rollback / Recovery Support
- Traffic Switching Support
- Production Release Review Support
- Deployment Failure Troubleshooting

우선순위:

1. Deployment Strategy Core
2. Blue-Green Deployment
3. Rolling Deployment
4. Canary Deployment
5. Rollback / Recovery
6. Monitoring / Verification

---

### [핵심]

Deployment Strategy 문서는 단순 배포 방법 설명서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- 배포 전략 선택
- 무중단 배포 구조 설계
- Blue-Green Deployment 설계
- Rolling Deployment 설계
- Canary Deployment 설계
- Rollback 기준 정의
- 배포 전후 Health Check 설계
- 배포 실패 원인 분석
- CI/CD Pipeline과 배포 전략 연결
- Kubernetes Deployment Strategy 검토
- Docker / IaC / Monitoring 문서와 연계

---

### [실무]

2026 실무 기준 Deployment Strategy 문서는 다음 흐름을 기준으로 작성한다.

```text
Code Change
→ Build
→ Test
→ Artifact / Image
→ Deploy
→ Health Check
→ Traffic Switch
→ Monitoring
→ Rollback or Complete
```

Deployment Strategy 문서는 단순히 배포를 실행하는 것이 아니라 안전하게 변경을 사용자에게 반영하고 장애 발생 시 빠르게 복구하는 것을 목표로 한다.

---

### [FAQ]

Q. Deployment Strategy 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 운영 배포 전략을 설계, 검토, 자동화, 문제 해결하기 위한 RAG 문서이다.

Q. Deployment Strategy 문서는 CI/CD 문서와 어떻게 다른가?

A.
CI/CD는 Build / Test / Deploy 자동화 흐름이고, Deployment Strategy는 운영 반영 방식, 트래픽 전환, 무중단, Rollback 전략을 다룬다.

Q. Deployment Strategy 문서는 Kubernetes 문서와 겹치는가?

A.
일부 연결된다. Deployment Strategy는 전략 개념과 선택 기준을 다루고 Kubernetes 문서는 이를 Deployment, Service, Ingress, Rollout으로 구현한다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Deployment Strategy Domain 문서는 애플리케이션 변경 사항을 운영 환경에 안전하게 반영하는 전략과 검증 절차를 다룬다.

포함 범위:

- Deployment Strategy
- Release Strategy
- Manual Deployment
- Automated Deployment
- Rolling Deployment
- Blue-Green Deployment
- Canary Deployment
- Recreate Deployment
- Feature Toggle
- Dark Launch
- Traffic Switching
- Load Balancer
- Health Check
- Readiness Check
- Smoke Test
- Rollback
- Roll Forward
- Database Migration
- Backward Compatibility
- Monitoring
- Error Rate
- Latency
- Deployment Verification
- Kubernetes Rollout
- CI/CD Deployment Gate
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Deployment
- Release
- Rollout
- Rollback
- Blue-Green
- Canary
- Rolling
- Zero Downtime
- Traffic Switching
- Health Check
- Smoke Test
- Monitoring
- Error Rate
- Latency
- Database Migration
- Backward Compatibility
- CI/CD
- Kubernetes

---

### [실무]

Deployment Strategy 문서는 아래 상황을 해결할 수 있어야 한다.

- 단일 서버 수동 배포 위험 판단
- Docker Compose 기반 배포 전략 선택
- Kubernetes Rolling Update 검토
- Blue-Green 환경 구성 검토
- Canary Release 기준 정의
- 배포 전 Smoke Test 설계
- 배포 후 Monitoring 기준 정의
- Error Rate 증가 시 Rollback 판단
- DB Migration 포함 배포 순서 설계
- Frontend / Backend 호환성 고려
- Feature Toggle 기반 점진적 출시 설계
- CI/CD Approval Gate 설계

---

### [FAQ]

Q. Deployment Strategy 문서에 Cloud Provider별 Load Balancer 설정을 모두 포함해야 하는가?

A.
아니다. 이 문서는 배포 전략, 트래픽 전환, 검증, 복구 기준을 다룬다. Cloud 세부 설정은 Cloud / Infrastructure 문서와 연결한다.

Q. Deployment Strategy 문서에 Kubernetes YAML을 깊게 포함해야 하는가?

A.
직접 깊게 포함하지 않는다. Kubernetes 구현 세부는 Kubernetes Domain 문서에서 다루고, 이 문서는 전략 선택과 검토 기준을 우선한다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Deployment Strategy 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

Deployment Strategy 문서는 검색 친화적인 전략 선택 구조를 우선한다.

```text
Deployment Need
→ Strategy Selection
→ Traffic Control
→ Health Check
→ Monitoring
→ Rollback Decision
→ Post-deploy Review
```

---

### [실무]

권장 Part 구성:

- Deployment_Strategy_Part01_Core.md
- Deployment_Strategy_Part02_Rolling_Deployment.md
- Deployment_Strategy_Part03_Blue_Green_Deployment.md
- Deployment_Strategy_Part04_Canary_Deployment.md
- Deployment_Strategy_Part05_Feature_Toggle_Dark_Launch.md
- Deployment_Strategy_Part06_Database_Migration.md
- Deployment_Strategy_Part07_Rollback_Recovery.md
- Deployment_Strategy_Part08_Monitoring_Verification.md
- Deployment_Strategy_Part09_CI_CD_Kubernetes_Integration.md

---

### [FAQ]

Q. Deployment Strategy 문서에 FAQ가 필요한가?

A.
필수이다. 배포 질문은 “무중단 배포”, “롤백 기준”, “카나리 배포”, “DB 마이그레이션 순서”처럼 문제 상황 중심으로 들어오는 경우가 많다.

Q. Deployment Strategy 문서는 얼마나 자세해야 하는가?

A.
구현 세부보다 전략 선택 기준, Flow, 위험 요소, 검증 기준, Rollback 조건을 우선한다.

---

# 4. Deployment Core Rules

## 4.1 Deployment Core 작성 규칙

### [개념]

Deployment는 빌드된 애플리케이션 Artifact 또는 Container Image를 실행 환경에 반영하는 과정이다.

Release는 사용자에게 기능 변경이 실제로 노출되는 과정이다.

Deployment와 Release는 구분해서 작성한다.

---

### [핵심]

필수 포함:

- Deployment
- Release
- Rollout
- Rollback
- Artifact
- Environment
- Traffic
- Verification

기본 흐름:

```text
Build Artifact
→ Deploy to Runtime
→ Verify Health
→ Expose Traffic
→ Monitor
→ Complete or Rollback
```

---

### [실무]

Deployment와 Release 차이:

| 구분       | 의미                       | 예                              |
| ---------- | -------------------------- | ------------------------------- |
| Deployment | 실행 환경에 새 버전을 배치 | Pod 교체, 서버 재시작           |
| Release    | 사용자에게 기능을 노출     | Traffic 전환, Feature Toggle ON |
| Rollout    | 변경을 점진적으로 확산     | 10% → 50% → 100%                |
| Rollback   | 이전 안정 버전으로 복구    | 이전 Image Tag로 재배포         |

---

### [FAQ]

Q. Deployment와 Release는 같은 의미인가?

A.
아니다. Deployment는 실행 환경에 새 버전을 배치하는 것이고 Release는 사용자에게 기능을 노출하는 것이다.

Q. Rollout은 무엇인가?

A.
새 버전을 전체 사용자에게 한 번에 반영하지 않고 단계적으로 확산하는 과정이다.

---

# 5. Strategy Selection Rules

## 5.1 배포 전략 선택 규칙

### [개념]

Deployment Strategy 선택은 서비스 규모, 장애 허용 범위, 인프라 구조, 트래픽 제어 가능성, Rollback 요구사항에 따라 달라진다.

---

### [핵심]

전략 선택 기준:

- 무중단 필요 여부
- 트래픽 분산 가능 여부
- 인스턴스 수
- Load Balancer 사용 여부
- Kubernetes 사용 여부
- DB Migration 포함 여부
- Rollback 속도 요구사항
- 사용자 영향 범위
- 비용 허용 범위
- 운영 복잡도

---

### [Comparison]

| 전략           | 장점                 | 단점                 | 적합 상황                 |
| -------------- | -------------------- | -------------------- | ------------------------- |
| Recreate       | 단순함               | 다운타임 발생        | 개발 / 소규모 내부 서비스 |
| Rolling        | 자원 효율 좋음       | 구버전 / 신버전 공존 | 일반 웹 서비스            |
| Blue-Green     | 빠른 전환 / Rollback | 인프라 비용 증가     | 무중단 중요 서비스        |
| Canary         | 위험 최소화          | 관측 / 라우팅 복잡   | 대규모 트래픽 서비스      |
| Feature Toggle | 배포와 출시 분리     | Toggle 관리 필요     | 점진적 기능 출시          |

---

### [실무]

전략 선택 예시:

```text
단일 서버
→ Recreate or 간단한 Blue-Green

여러 인스턴스 + Load Balancer
→ Rolling or Blue-Green

Kubernetes
→ Rolling Update 기본
→ Canary / Blue-Green은 Ingress / Service Mesh / Progressive Delivery 도구와 연계

대규모 사용자 서비스
→ Canary + Monitoring + Automated Rollback
```

---

### [FAQ]

Q. 가장 기본적인 운영 배포 전략은 무엇인가?

A.
Kubernetes 환경에서는 Rolling Update가 기본이고, 무중단과 빠른 Rollback이 중요하면 Blue-Green 또는 Canary를 검토한다.

Q. 모든 서비스에 Canary Deployment를 적용해야 하는가?

A.
아니다. Canary는 관측, 라우팅, 자동화가 필요하므로 서비스 규모와 운영 역량을 고려해야 한다.

---

# 6. Recreate Deployment Rules

## 6.1 Recreate Deployment 작성 규칙

### [개념]

Recreate Deployment는 기존 버전을 중지한 뒤 새 버전을 실행하는 가장 단순한 배포 방식이다.

---

### [핵심]

필수 포함:

- Stop Old Version
- Deploy New Version
- Downtime
- Simple Deployment
- Low Complexity

Flow:

```text
Old Version Stop
→ New Version Deploy
→ Health Check
→ Service Resume
```

---

### [실무]

Recreate Deployment 적합 상황:

- 개발 환경
- 테스트 서버
- 내부 관리자 서비스
- 사용자가 거의 없는 서비스
- 다운타임 허용 가능 서비스
- 인프라 자원이 제한된 소규모 서버

---

### [주의]

Recreate Deployment는 운영 사용자에게 다운타임이 발생할 수 있다.

주의 대상:

- 결제 서비스
- 인증 서비스
- 실시간 채팅
- 예약 / 주문 서비스
- 사용량이 많은 API 서버

---

### [FAQ]

Q. Recreate Deployment는 언제 사용하는가?

A.
다운타임이 허용되는 개발, 테스트, 내부 서비스, 소규모 서비스에서 사용할 수 있다.

Q. Recreate Deployment가 운영에 위험한 이유는?

A.
기존 버전을 중지한 뒤 새 버전을 올리기 때문에 배포 중 서비스 중단이 발생할 수 있다.

---

# 7. Rolling Deployment Rules

## 7.1 Rolling Deployment 작성 규칙

### [개념]

Rolling Deployment는 여러 인스턴스를 순차적으로 새 버전으로 교체하는 배포 전략이다.

---

### [핵심]

필수 포함:

- Rolling Update
- Incremental Replacement
- Old / New Version Coexistence
- Health Check
- Minimum Available
- Maximum Surge

Flow:

```text
Instance 1 Update
→ Health Check
→ Instance 2 Update
→ Health Check
→ Continue
→ Complete
```

---

### [실무]

Rolling Deployment 적합 상황:

- 여러 인스턴스 운영
- 무중단 또는 최소 다운타임 필요
- Kubernetes 기본 Deployment 사용
- 리소스 추가 비용을 크게 늘리고 싶지 않은 경우
- 구버전과 신버전이 일정 시간 공존해도 되는 경우

Kubernetes Rolling Update 개념 예시:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
```

---

### [주의]

Rolling Deployment는 구버전과 신버전이 동시에 요청을 처리할 수 있다.

주의 대상:

- API 응답 형식 변경
- DB Schema 변경
- Session 호환성
- Message Queue Consumer 호환성
- Cache Key 변경
- Frontend / Backend API 호환성

---

### [FAQ]

Q. Rolling Deployment는 무엇인가?

A.
여러 인스턴스를 한 번에 교체하지 않고 순차적으로 새 버전으로 바꾸는 배포 전략이다.

Q. Rolling Deployment의 가장 큰 주의점은?

A.
구버전과 신버전이 동시에 실행되므로 API, DB, Cache, Message 호환성을 유지해야 한다.

Q. Kubernetes의 기본 배포 전략은 무엇인가?

A.
일반적인 Kubernetes Deployment의 기본 전략은 Rolling Update이다.

---

# 8. Blue-Green Deployment Rules

## 8.1 Blue-Green Deployment 작성 규칙

### [개념]

Blue-Green Deployment는 현재 운영 중인 Blue 환경과 새 버전이 배포된 Green 환경을 분리하고, 검증 후 트래픽을 전환하는 배포 전략이다.

---

### [핵심]

필수 포함:

- Blue Environment
- Green Environment
- Traffic Switch
- Load Balancer
- Zero Downtime
- Fast Rollback
- Environment Parity

Flow:

```text
Blue Running
→ Deploy Green
→ Verify Green
→ Switch Traffic
→ Monitor
→ Keep or Remove Blue
```

---

### [실무]

Blue-Green Deployment 적합 상황:

- 무중단 배포 필요
- 빠른 Rollback 필요
- 인프라를 이중으로 유지할 수 있음
- 배포 전 실제 운영 유사 환경 검증 필요
- Load Balancer 또는 Routing Control 가능

트래픽 전환 예시:

```text
Before:
User Traffic → Blue

After:
User Traffic → Green
```

Rollback 예시:

```text
Green Error Detected
→ Switch Traffic Back to Blue
→ Investigate Green
```

---

### [주의]

Blue-Green Deployment는 비용과 환경 동기화 문제가 있다.

주의 대상:

- Blue / Green DB 공유 여부
- Database Migration 호환성
- Background Job 중복 실행
- Scheduler 중복 실행
- Cache Warm-up
- Session 저장소
- File Upload 저장소
- External Webhook Endpoint

---

### [FAQ]

Q. Blue-Green Deployment는 무엇인가?

A.
기존 Blue 환경과 새 Green 환경을 분리하고 Green 검증 후 트래픽을 전환하는 무중단 배포 전략이다.

Q. Blue-Green Deployment의 장점은?

A.
트래픽 전환이 빠르고 문제가 생기면 Blue로 되돌려 빠르게 Rollback할 수 있다.

Q. Blue-Green Deployment의 단점은?

A.
두 환경을 유지해야 하므로 비용이 증가하고 DB, Scheduler, Cache, Session 동기화 문제가 발생할 수 있다.

---

# 9. Canary Deployment Rules

## 9.1 Canary Deployment 작성 규칙

### [개념]

Canary Deployment는 새 버전을 일부 사용자 또는 일부 트래픽에만 먼저 노출하고 안정성을 확인한 뒤 점진적으로 확대하는 배포 전략이다.

---

### [핵심]

필수 포함:

- Canary Release
- Gradual Traffic
- Small User Group
- Metrics Verification
- Error Rate
- Latency
- Automated Rollback
- Progressive Delivery

Flow:

```text
Deploy Canary
→ Route 5% Traffic
→ Monitor Metrics
→ Increase to 25%
→ Increase to 50%
→ Increase to 100%
→ Complete
```

---

### [실무]

Canary Deployment 적합 상황:

- 사용자 규모가 큼
- 배포 위험을 최소화해야 함
- 관측 지표가 잘 구성됨
- 트래픽 비율 제어 가능
- A/B Testing 또는 Feature 검증 필요
- 자동 Rollback 기준을 만들 수 있음

Canary 단계 예시:

```text
5% Traffic
→ 15 minutes Monitoring
→ 25% Traffic
→ 30 minutes Monitoring
→ 50% Traffic
→ 100% Traffic
```

---

### [주의]

Canary Deployment는 Monitoring이 약하면 효과가 낮다.

필수 관측 지표:

- Error Rate
- Latency
- Request Success Rate
- CPU / Memory
- Saturation
- Business Metric
- Log Error Pattern
- User Complaint Signal

---

### [FAQ]

Q. Canary Deployment는 무엇인가?

A.
새 버전을 일부 트래픽에만 먼저 노출한 뒤 안정성을 확인하면서 점진적으로 확대하는 배포 전략이다.

Q. Canary Deployment의 핵심 조건은?

A.
트래픽 비율 제어와 신뢰 가능한 Monitoring / Alerting이 필요하다.

Q. Canary 배포 중 Error Rate가 증가하면 어떻게 해야 하는가?

A.
트래픽 확대를 중단하고 Canary를 Rollback하거나 이전 안정 버전으로 라우팅을 되돌린다.

---

# 10. Feature Toggle Rules

## 10.1 Feature Toggle 작성 규칙

### [개념]

Feature Toggle은 코드 배포와 기능 출시를 분리하기 위해 기능 활성화 여부를 설정으로 제어하는 방식이다.

---

### [핵심]

필수 포함:

- Feature Flag
- Toggle
- Release Control
- Runtime Switch
- Target User
- Gradual Rollout
- Kill Switch

Flow:

```text
Deploy Code with Feature Off
→ Enable Feature for Internal Users
→ Enable for Small Group
→ Monitor
→ Enable for All Users
```

---

### [실무]

Feature Toggle 적합 상황:

- 배포와 출시 시점을 분리해야 함
- 특정 사용자 그룹에만 기능을 열어야 함
- 긴급히 기능을 끌 수 있어야 함
- Canary와 함께 점진적 출시 필요
- Frontend / Backend 기능을 단계적으로 연결해야 함

Toggle 관리 기준:

- Toggle 이름 명확화
- Owner 지정
- 만료일 지정
- 오래된 Toggle 제거
- 운영 변경 이력 기록
- 기본값 안전하게 설정

---

### [주의]

Feature Toggle은 누적되면 기술 부채가 된다.

주의 대상:

- 오래된 Toggle 방치
- Toggle 조합 폭증
- 테스트 누락
- 권한 없는 운영 변경
- 프론트엔드 / 백엔드 Toggle 불일치
- Kill Switch 없음

---

### [FAQ]

Q. Feature Toggle은 왜 사용하는가?

A.
코드 배포와 기능 출시를 분리하고 특정 사용자에게만 기능을 점진적으로 노출하기 위해 사용한다.

Q. Feature Toggle의 단점은?

A.
오래 방치하면 코드 복잡도와 테스트 조합이 증가하여 기술 부채가 된다.

Q. Kill Switch는 무엇인가?

A.
문제가 생긴 기능을 코드 재배포 없이 즉시 비활성화하는 Toggle이다.

---

# 11. Dark Launch Rules

## 11.1 Dark Launch 작성 규칙

### [개념]

Dark Launch는 기능을 사용자에게 직접 노출하지 않고 운영 환경에서 내부적으로 실행하거나 제한된 방식으로 검증하는 출시 전략이다.

---

### [핵심]

필수 포함:

- Hidden Release
- Production Validation
- Internal Traffic
- Shadow Traffic
- No User Exposure
- Observability

Flow:

```text
Deploy Feature Hidden
→ Run Internal Validation
→ Collect Metrics
→ Fix Issues
→ Gradual User Exposure
```

---

### [실무]

Dark Launch 적합 상황:

- 운영 데이터 기반 검증 필요
- 사용자 UI 노출 전 Backend 성능 확인
- 새로운 추천 알고리즘 검증
- 검색 / 랭킹 로직 검증
- AI 기능 응답 품질 내부 검증
- 대규모 기능의 사전 부하 확인

---

### [주의]

Dark Launch도 운영 자원을 사용한다.

주의 대상:

- 불필요한 외부 API 호출
- DB 부하 증가
- 로그 폭증
- 비용 증가
- 사용자 데이터 처리 정책
- Shadow Write 금지 또는 엄격한 제어

---

### [FAQ]

Q. Dark Launch는 무엇인가?

A.
기능을 사용자에게 직접 노출하지 않고 운영 환경에서 내부적으로 검증하는 출시 전략이다.

Q. Dark Launch와 Feature Toggle은 어떤 관계인가?

A.
Dark Launch는 Feature Toggle을 사용해 기능을 숨긴 상태로 운영 검증을 진행할 수 있다.

---

# 12. Traffic Switching Rules

## 12.1 Traffic Switching 작성 규칙

### [개념]

Traffic Switching은 사용자 요청을 구버전에서 신버전으로 전환하거나 일정 비율로 분산하는 과정이다.

---

### [핵심]

필수 포함:

- Load Balancer
- DNS
- Ingress
- Service Mesh
- Weighted Routing
- Header Routing
- User Segment Routing
- Rollback Routing

---

### [실무]

트래픽 전환 방식:

| 방식                      | 설명                         | 적합 전략            |
| ------------------------- | ---------------------------- | -------------------- |
| Load Balancer Target 변경 | 대상 서버 그룹 전환          | Blue-Green           |
| Weighted Routing          | 비율 기반 트래픽 분산        | Canary               |
| DNS Switch                | 도메인 대상 변경             | 단순 Blue-Green      |
| Ingress Routing           | Kubernetes Ingress 규칙 변경 | Canary / Blue-Green  |
| Service Mesh Routing      | 세밀한 트래픽 제어           | Progressive Delivery |
| Feature Flag Routing      | 사용자 그룹 기반 제어        | Feature Toggle       |

---

### [주의]

DNS 기반 전환은 TTL 때문에 즉시 반영되지 않을 수 있다.

트래픽 전환 전 확인:

- Health Check 통과
- 새 버전 Warm-up 완료
- Cache 준비
- DB Migration 호환성
- Rollback 대상 유지
- Monitoring Dashboard 준비

---

### [FAQ]

Q. Traffic Switching은 무엇인가?

A.
사용자 요청을 구버전에서 신버전으로 전환하거나 비율별로 분산하는 배포 제어 방식이다.

Q. DNS 전환은 왜 Rollback이 느릴 수 있는가?

A.
DNS TTL과 캐시 때문에 변경 사항이 모든 사용자에게 즉시 반영되지 않을 수 있기 때문이다.

---

# 13. Health Check Rules

## 13.1 Health Check 작성 규칙

### [개념]

Health Check는 배포된 애플리케이션이 정상적으로 실행되고 요청을 처리할 준비가 되었는지 확인하는 검증 절차이다.

---

### [핵심]

필수 포함:

- Health Check
- Readiness Check
- Liveness Check
- Startup Check
- Dependency Check
- Load Balancer Health
- Kubernetes Probe

---

### [실무]

Health Check 단계:

```text
Process Running
→ Application Started
→ Dependency Connected
→ Readiness Passed
→ Traffic Allowed
```

Spring Boot 예시:

```text
/actuator/health
/actuator/health/readiness
/actuator/health/liveness
```

Kubernetes Probe 예시:

```yaml
readinessProbe:
  httpGet:
    path: /actuator/health/readiness
    port: 8080
  initialDelaySeconds: 20
  periodSeconds: 10
```

---

### [주의]

Process Running과 Service Ready는 다르다.

주의:

```text
Application Process Running
≠ Request Processing Ready
```

Health Check가 부정확하면 장애 상태의 인스턴스에 트래픽이 전달될 수 있다.

---

### [FAQ]

Q. Health Check는 왜 필요한가?

A.
배포된 애플리케이션이 실제 요청을 처리할 준비가 되었는지 확인하고 잘못된 인스턴스로 트래픽이 가지 않도록 하기 위해 필요하다.

Q. Readiness Check와 Liveness Check 차이는?

A.
Readiness는 트래픽을 받을 준비 여부이고 Liveness는 애플리케이션이 살아있는지 확인하는 검사이다.

---

# 14. Smoke Test Rules

## 14.1 Smoke Test 작성 규칙

### [개념]

Smoke Test는 배포 직후 핵심 기능이 정상 동작하는지 빠르게 확인하는 최소 검증 테스트이다.

---

### [핵심]

필수 포함:

- Smoke Test
- Post-deploy Test
- Critical Path
- API Check
- Login Check
- Database Check
- External API Check

---

### [실무]

Smoke Test 대상:

- 서버 Health Check
- 로그인 API
- 핵심 조회 API
- DB 연결
- Redis 연결
- 외부 API 연결
- 파일 업로드 경로
- 결제 / 예약 / 주문 핵심 흐름
- 프론트엔드 정적 파일 로딩
- API Gateway / Ingress 라우팅

예시 Flow:

```text
Deploy Complete
→ Health Check
→ Smoke Test
→ Monitor
→ Release Complete
```

---

### [주의]

Smoke Test는 전체 테스트가 아니다.

역할:

- 배포 직후 치명적 장애 탐지
- 핵심 경로 빠른 검증
- Rollback 판단 보조

---

### [FAQ]

Q. Smoke Test는 무엇인가?

A.
배포 직후 핵심 기능이 정상 동작하는지 빠르게 확인하는 최소 검증 테스트이다.

Q. Smoke Test와 전체 테스트는 같은가?

A.
아니다. Smoke Test는 핵심 경로만 빠르게 확인하는 배포 후 검증이다.

---

# 15. Monitoring / Verification Rules

## 15.1 배포 검증 및 모니터링 규칙

### [개념]

Deployment Verification은 배포 후 시스템 상태와 사용자 영향을 관측하여 배포 성공 여부를 판단하는 과정이다.

---

### [핵심]

필수 포함:

- Monitoring
- Metrics
- Logs
- Traces
- Error Rate
- Latency
- Throughput
- Saturation
- Business Metric
- Alerting
- SLO

---

### [실무]

배포 후 확인 지표:

- HTTP 5xx Error Rate
- HTTP 4xx 급증
- P95 / P99 Latency
- Request Per Second
- CPU / Memory
- Pod Restart Count
- DB Connection Pool
- Queue Lag
- External API Error
- Login Success Rate
- Payment Failure Rate
- Signup Conversion
- User Complaint

배포 검증 Flow:

```text
Deploy
→ Technical Metrics Check
→ Log Error Pattern Check
→ Business Metrics Check
→ Alert Check
→ Release Complete
```

---

### [주의]

기술 지표만으로는 부족하다.

예:

- 서버는 정상
- Error Rate 낮음
- 하지만 결제 성공률 급락
- Business Metric 기반 검증 필요

---

### [FAQ]

Q. 배포 후 반드시 봐야 하는 지표는?

A.
Error Rate, Latency, Traffic, Resource Usage, Log Error, 핵심 Business Metric을 확인해야 한다.

Q. Business Metric도 배포 검증에 필요한가?

A.
필요하다. 기술 지표가 정상이어도 로그인, 결제, 주문, 가입 같은 핵심 비즈니스 흐름이 실패할 수 있다.

---

# 16. Rollback Rules

## 16.1 Rollback 작성 규칙

### [개념]

Rollback은 배포 후 문제가 발생했을 때 이전 안정 버전으로 되돌리는 복구 전략이다.

---

### [핵심]

필수 포함:

- Rollback
- Previous Stable Version
- Image Tag
- Traffic Revert
- Database Compatibility
- Recovery Time
- Incident Response

Flow:

```text
Issue Detected
→ Stop Rollout
→ Decide Rollback
→ Revert Traffic or Version
→ Verify Recovery
→ Incident Review
```

---

### [실무]

Rollback 기준:

- Error Rate 임계치 초과
- Latency 급증
- Health Check 실패
- Pod Restart 반복
- 핵심 API 실패
- 결제 / 주문 / 로그인 실패
- DB Migration 문제
- 외부 API 연동 장애
- 사용자 신고 급증

Rollback 방식:

| 배포 전략      | Rollback 방식           |
| -------------- | ----------------------- |
| Rolling        | 이전 Image Tag로 재배포 |
| Blue-Green     | 트래픽을 Blue로 되돌림  |
| Canary         | Canary 트래픽 차단      |
| Feature Toggle | Toggle OFF              |
| Recreate       | 이전 Artifact 재배포    |

---

### [주의]

Rollback은 DB Migration과 강하게 연결된다.

DB가 이미 비호환 변경되었다면 애플리케이션만 이전 버전으로 되돌려도 복구되지 않을 수 있다.

---

### [FAQ]

Q. Rollback은 무엇인가?

A.
배포 후 문제가 발생했을 때 이전 안정 버전으로 되돌리는 복구 전략이다.

Q. Rollback이 항상 가능한가?

A.
아니다. DB Schema 비호환 변경, 데이터 손상, 외부 시스템 변경이 있으면 단순 Rollback이 어려울 수 있다.

Q. 가장 빠른 Rollback 전략은 무엇인가?

A.
Blue-Green에서는 트래픽을 이전 Blue 환경으로 되돌리는 방식이 빠르다. Feature Toggle은 기능을 즉시 끄는 방식으로 빠르게 대응할 수 있다.

---

# 17. Roll Forward Rules

## 17.1 Roll Forward 작성 규칙

### [개념]

Roll Forward는 이전 버전으로 되돌리는 대신 수정 버전을 빠르게 배포하여 문제를 해결하는 전략이다.

---

### [핵심]

필수 포함:

- Roll Forward
- Hotfix
- Patch Release
- Forward Recovery
- Fast Fix
- Risk Assessment

---

### [실무]

Roll Forward 적합 상황:

- Rollback이 DB 변경 때문에 어려움
- 원인이 명확하고 수정 범위가 작음
- 이전 버전 복구가 더 위험함
- 새 버전 기반으로 빠른 Patch 가능
- Feature Toggle로 문제 기능을 차단 가능

Flow:

```text
Issue Detected
→ Root Cause Known
→ Hotfix
→ Test
→ Deploy Patch
→ Verify
```

---

### [주의]

Roll Forward는 빠른 수정이 가능할 때만 안전하다.

원인이 불명확하면 Roll Forward가 추가 장애를 만들 수 있다.

---

### [FAQ]

Q. Roll Forward는 무엇인가?

A.
이전 버전으로 되돌리지 않고 수정 버전을 배포하여 앞으로 복구하는 전략이다.

Q. Rollback과 Roll Forward 중 무엇이 좋은가?

A.
상황에 따라 다르다. 빠른 복구가 가능하면 Rollback, DB 변경으로 Rollback이 어렵고 원인이 명확하면 Roll Forward를 고려한다.

---

# 18. Database Migration Rules

## 18.1 Database Migration 배포 규칙

### [개념]

Database Migration은 배포 중 DB Schema나 데이터를 변경하는 작업이다.

배포 전략에서 가장 위험한 요소 중 하나이다.

---

### [핵심]

필수 포함:

- Database Migration
- Schema Change
- Backward Compatibility
- Expand and Contract
- Zero Downtime Migration
- Data Backfill
- Migration Rollback
- Lock Risk

---

### [실무]

무중단 DB Migration 기본 전략:

```text
Expand
→ Deploy Compatible App
→ Backfill Data
→ Switch Read / Write
→ Verify
→ Contract
```

예시:

```text
1. 새 컬럼 추가
2. 기존 App과 새 App 모두 새 Schema와 호환
3. 데이터 Backfill
4. 새 App 배포
5. 충분한 검증 후 기존 컬럼 제거
```

---

### [주의]

위험한 DB 변경:

- 컬럼 즉시 삭제
- 컬럼 타입 변경
- NOT NULL 즉시 추가
- 대용량 테이블 Lock 발생 Migration
- 인덱스 생성 중 Lock
- 기존 API와 비호환 Schema
- Rollback 불가능한 데이터 변환

---

### [FAQ]

Q. DB Migration이 배포에서 위험한 이유는?

A.
Schema 변경이 애플리케이션 버전과 호환되지 않으면 장애가 발생하고 단순 Rollback이 어려울 수 있기 때문이다.

Q. Expand and Contract는 무엇인가?

A.
먼저 호환 가능한 Schema를 확장하고, 새 버전 안정화 후 오래된 Schema를 제거하는 무중단 Migration 전략이다.

Q. 배포 중 컬럼을 바로 삭제해도 되는가?

A.
권장하지 않는다. 구버전 애플리케이션이 해당 컬럼을 사용 중일 수 있으므로 단계적으로 제거해야 한다.

---

# 19. Backward Compatibility Rules

## 19.1 Backward Compatibility 작성 규칙

### [개념]

Backward Compatibility는 새 버전이 기존 클라이언트, 기존 데이터, 기존 API 소비자와 호환되는 성질이다.

---

### [핵심]

필수 포함:

- Backward Compatibility
- Forward Compatibility
- API Compatibility
- Schema Compatibility
- Consumer Compatibility
- Version Coexistence

---

### [실무]

호환성 검토 대상:

- REST API 응답 필드 삭제 여부
- 필수 Request Field 추가 여부
- DB Schema 변경 여부
- Message Queue Event Schema 변경
- Cache Key 변경
- Session 구조 변경
- Frontend / Backend 배포 순서
- Mobile App 구버전 지원

호환 배포 Flow:

```text
Add Optional Field
→ Deploy Backend
→ Deploy Frontend
→ Monitor
→ Remove Old Field Later
```

---

### [주의]

Rolling / Canary 배포에서는 구버전과 신버전이 동시에 실행된다.

따라서 호환성 없는 변경은 장애를 만들 수 있다.

---

### [FAQ]

Q. Backward Compatibility는 왜 중요한가?

A.
Rolling, Canary, Blue-Green 배포 중 구버전과 신버전, 기존 클라이언트가 동시에 존재할 수 있기 때문이다.

Q. API 필드를 삭제해도 되는가?

A.
바로 삭제하면 위험하다. 먼저 Deprecated 처리하고 소비자 전환 확인 후 제거해야 한다.

---

# 20. CI/CD Deployment Gate Rules

## 20.1 CI/CD Deployment Gate 작성 규칙

### [개념]

Deployment Gate는 배포 전후 특정 조건을 만족해야 다음 단계로 진행하도록 막는 검증 지점이다.

---

### [핵심]

필수 포함:

- Quality Gate
- Approval Gate
- Test Gate
- Security Gate
- Manual Approval
- Automated Verification
- Promotion

---

### [Flow]

```text
Build
→ Unit Test
→ Integration Test
→ Security Scan
→ Deploy Staging
→ Smoke Test
→ Manual Approval
→ Deploy Production
→ Monitoring Gate
```

---

### [실무]

Gate 예시:

- Test Coverage 기준
- Integration Test 통과
- Container Image Scan 통과
- IaC Plan Review 통과
- Staging Smoke Test 통과
- 승인자 승인
- Production Health Check 통과
- Error Rate 임계치 이하
- Canary 단계별 지표 통과

---

### [주의]

Gate가 너무 많으면 배포 속도가 느려진다.

Gate가 너무 적으면 장애 위험이 증가한다.

서비스 중요도에 따라 Gate 수준을 조정한다.

---

### [FAQ]

Q. Deployment Gate는 무엇인가?

A.
배포 전후 특정 검증 조건을 통과해야 다음 단계로 진행할 수 있게 하는 안전장치이다.

Q. 운영 배포에는 Manual Approval이 필요한가?

A.
서비스 중요도와 자동화 신뢰도에 따라 다르지만, 중요한 운영 환경은 승인 절차를 두는 것이 안전하다.

---

# 21. Kubernetes Deployment Strategy Rules

## 21.1 Kubernetes 연계 규칙

### [개념]

Kubernetes Deployment Strategy는 Pod 교체, Service 라우팅, Ingress 트래픽 제어, Rollout / Rollback 기능과 연결된다.

---

### [핵심]

필수 포함:

- Kubernetes Deployment
- RollingUpdate
- Recreate
- Readiness Probe
- Liveness Probe
- Service
- Ingress
- Rollout
- Rollback
- Progressive Delivery

---

### [실무]

Kubernetes 기본 Rollout 명령:

```bash
kubectl rollout status deployment/my-app
kubectl rollout history deployment/my-app
kubectl rollout undo deployment/my-app
```

Kubernetes 배포 검토 기준:

- readinessProbe 설정 여부
- livenessProbe 설정 여부
- maxUnavailable / maxSurge 적절성
- image tag 명확성
- resource limit 설정 여부
- deployment revision 추적 가능 여부
- service selector 정확성
- ingress routing 영향
- configmap / secret 변경 영향

---

### [주의]

Kubernetes에서 Pod가 Running이어도 Ready가 아닐 수 있다.

Traffic은 Ready 상태의 Pod로만 전달되어야 한다.

---

### [FAQ]

Q. Kubernetes에서 배포 상태는 어떻게 확인하는가?

A.
`kubectl rollout status deployment/name` 명령으로 확인한다.

Q. Kubernetes Rollback은 어떻게 수행하는가?

A.
`kubectl rollout undo deployment/name` 명령으로 이전 ReplicaSet 기반 Rollback을 수행할 수 있다.

Q. Kubernetes에서 Readiness Probe가 중요한 이유는?

A.
Ready 상태가 아닌 Pod에 트래픽이 전달되는 것을 방지하기 위해 필요하다.

---

# 22. Docker / Compose Deployment Rules

## 22.1 Docker / Compose 배포 규칙

### [개념]

Docker / Docker Compose 배포는 단일 서버 또는 소규모 운영 환경에서 Container Image를 Pull하고 Container를 재시작하는 방식으로 운영될 수 있다.

---

### [핵심]

필수 포함:

- Docker Image
- Docker Tag
- Docker Compose
- Pull
- Up
- Restart
- Health Check
- Volume Persistence
- Environment Variable

---

### [실무]

Compose 배포 흐름:

```text
Build Image
→ Push Registry
→ Server Pull
→ docker compose up -d
→ Health Check
→ Logs Check
```

명령 예시:

```bash
docker compose pull
docker compose up -d
docker compose ps
docker compose logs -f app
```

Rollback 예시:

```text
Change Image Tag to Previous Version
→ docker compose up -d
→ Health Check
```

---

### [주의]

Docker Compose 운영 배포 주의점:

- Image Tag 명확화
- `.env` 관리
- Volume 삭제 금지
- DB Container 재생성 주의
- Port 충돌 확인
- Health Check 구성
- 로그 확인
- 단일 서버 장애 한계 인지

---

### [FAQ]

Q. Docker Compose로 운영 배포가 가능한가?

A.
소규모 단일 서버 운영에는 가능하다. 대규모 무중단, 자동 복구, 확장성은 Kubernetes가 더 적합하다.

Q. Compose 배포에서 Rollback은 어떻게 하는가?

A.
이전 Image Tag로 되돌린 뒤 `docker compose up -d`로 재기동하고 Health Check를 확인한다.

---

# 23. Frontend / Backend Deployment Order Rules

## 23.1 Frontend / Backend 배포 순서 규칙

### [개념]

Frontend와 Backend가 함께 변경되는 경우 API 호환성과 배포 순서를 고려해야 한다.

---

### [핵심]

필수 포함:

- API Compatibility
- Frontend Deployment
- Backend Deployment
- Version Compatibility
- Static Asset Cache
- CDN Cache
- API Contract

---

### [실무]

안전한 배포 순서 예시:

```text
1. Backend가 기존 Frontend와 새 Frontend 모두 지원
2. Backend 배포
3. Backend Health / API 검증
4. Frontend 배포
5. CDN Cache 확인
6. 사용자 Flow 검증
7. Deprecated API 제거는 나중에 수행
```

---

### [주의]

위험한 변경:

- Backend API 필드 즉시 삭제
- Frontend가 새 API만 호출
- Backend 배포 전 Frontend 먼저 배포
- CDN Cache로 구버전 Frontend 잔존
- Mobile App 구버전 미고려
- CORS / Cookie / Auth 설정 변경

---

### [FAQ]

Q. Frontend와 Backend 중 무엇을 먼저 배포해야 하는가?

A.
일반적으로 Backend가 기존 Frontend와 새 Frontend를 모두 지원하도록 먼저 배포한 뒤 Frontend를 배포하는 것이 안전하다.

Q. API 응답 필드를 바로 삭제하면 안 되는 이유는?

A.
구버전 Frontend나 외부 클라이언트가 해당 필드에 의존할 수 있기 때문이다.

---

# 24. Release Note / Change Tracking Rules

## 24.1 Release 추적 규칙

### [개념]

Release Note와 Change Tracking은 어떤 변경이 언제, 어떤 버전으로 배포되었는지 추적하기 위한 운영 기록이다.

---

### [핵심]

필수 포함:

- Release Note
- Version
- Image Tag
- Commit SHA
- Change Log
- Deployment Time
- Deployed By
- Rollback Target

---

### [실무]

Release 기록 항목:

- Service Name
- Version
- Image Tag
- Git Commit SHA
- Deployment Environment
- Deployment Strategy
- Migration Included 여부
- Feature Toggle 변경 여부
- 배포 시작 / 완료 시간
- 승인자
- Rollback 대상 버전
- 배포 후 이슈

예시:

```text
service: festa-api
version: 1.4.2
image: festa-api:git-a1b2c3d
strategy: rolling
migration: yes
rollback_target: festa-api:git-z9y8x7w
```

---

### [FAQ]

Q. Release 기록은 왜 필요한가?

A.
장애 발생 시 어떤 변경이 원인인지 추적하고 빠르게 Rollback 대상을 찾기 위해 필요하다.

Q. Image Tag와 Commit SHA를 기록해야 하는 이유는?

A.
배포된 실행물이 어떤 코드에서 생성되었는지 추적하기 위해 필요하다.

---

# 25. Troubleshooting Rules

## 25.1 Deployment Troubleshooting 작성 규칙

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

- Deploy Failed
- Health Check Failed
- Smoke Test Failed
- Traffic Switch Failed
- Rollback Failed
- Canary Error Rate Increased
- Rolling Update Stuck
- Blue-Green Switch Failed
- Database Migration Failed
- Pod CrashLoopBackOff
- Image Pull Failed
- Config Missing
- Secret Missing
- Port Conflict
- Monitoring Missing

---

### [실무]

기본 확인 흐름:

```text
Deployment Status
→ Runtime Status
→ Health Check
→ Logs
→ Metrics
→ Traffic Routing
→ Config / Secret
→ Database Migration
→ Rollback Decision
```

Kubernetes 확인 명령:

```bash
kubectl rollout status deployment/my-app
kubectl get pods
kubectl describe pod pod-name
kubectl logs pod-name
```

Docker Compose 확인 명령:

```bash
docker compose ps
docker compose logs -f app
docker inspect container-name
```

---

### [Troubleshooting]

문제:
배포 후 Health Check 실패.

원인:

- Application Startup 실패
- 환경 변수 누락
- DB 연결 실패
- External API 연결 실패
- Readiness Path 오류
- Port 설정 오류

해결:

```text
Logs 확인
→ Environment 확인
→ Dependency 연결 확인
→ Health Check Path 확인
→ Port 확인
→ Rollback 판단
```

문제:
Canary 배포 중 Error Rate 증가.

원인:

- 새 버전 버그
- 특정 사용자 조건에서 오류
- DB Schema 호환성 문제
- External API 변경
- Cache / Session 호환성 문제

해결:

```text
Canary Traffic 중단
→ Error Log 확인
→ Metric 비교
→ Feature Toggle OFF
→ Rollback or Hotfix
```

문제:
Rolling Update가 멈춘다.

원인:

- Readiness Probe 실패
- 새 Pod Crash
- Resource 부족
- Image Pull 실패
- Config / Secret 오류

해결:

```text
Rollout Status 확인
→ Pod Event 확인
→ Logs 확인
→ Image / Config / Secret 확인
→ Rollback
```

문제:
Rollback 실패.

원인:

- 이전 Image Tag 없음
- DB Migration 비호환
- Config 변경 누락
- External System 변경
- State 불일치

해결:

```text
Rollback Target 확인
→ DB 호환성 확인
→ Config 복구
→ Traffic 우회
→ Roll Forward 검토
```

---

### [FAQ]

Q. 배포 실패 시 가장 먼저 확인할 것은?

A.
Deployment 상태, Runtime 상태, Health Check, 로그, 최근 변경 사항을 먼저 확인한다.

Q. Rolling Update가 멈추는 가장 흔한 원인은?

A.
Readiness Probe 실패, 새 Pod Crash, Resource 부족, Image Pull 실패, Config / Secret 오류이다.

Q. Canary 배포 실패 시 첫 조치는?

A.
Canary 트래픽 확대를 중단하고 Error Rate, 로그, 사용자 영향 범위를 확인한 뒤 Rollback 여부를 결정한다.

---

# 26. Common Mistakes

## 26.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 배포 전략과 운영 배포 설정을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- 배포 전략 없이 수동 배포
- latest Image Tag 사용
- Rollback 대상 미준비
- Health Check 미구성
- Smoke Test 누락
- Monitoring 없이 Canary 진행
- Blue-Green DB 호환성 미검토
- Rolling 중 API 호환성 깨짐
- DB Migration과 App 배포 순서 오류
- Feature Toggle 방치
- CDN Cache 고려 누락
- 운영 배포 승인 절차 없음
- 배포 후 Business Metric 미확인
- Config / Secret 변경 영향 미검토
- Scheduler / Batch 중복 실행
- 로그 확인 없이 배포 완료 처리

---

### [실무]

Review Agent 검토 기준:

```text
Deployment Strategy
→ Image Tag
→ Health Check
→ Smoke Test
→ Traffic Control
→ Monitoring
→ Rollback Target
→ DB Migration
→ Compatibility
→ Approval
```

---

### [FAQ]

Q. Deployment Review에서 가장 먼저 봐야 하는 것은?

A.
배포 전략, Rollback 대상, Health Check, Monitoring, DB Migration, 호환성 위험을 먼저 확인한다.

Q. latest Image Tag가 배포에서 위험한 이유는?

A.
실제 배포된 버전을 추적하기 어렵고 Rollback 대상이 불명확해지기 때문이다.

---

# 27. File Relationship Rules

## 27.1 다른 Domain Rules와 연계

### [개념]

Deployment Strategy Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Docker Advanced, Infrastructure as Code, Kubernetes, Monitoring과 연결된다.

---

### [핵심]

연계 구조:

```text
CI/CD
→ Docker Image
→ Deployment Strategy
→ Kubernetes / Server Runtime
→ Monitoring
→ Rollback
```

---

### [실무]

파일 간 역할 분리:

| Domain                 | 역할                                           |
| ---------------------- | ---------------------------------------------- |
| Deployment Strategy    | 배포 방식, 트래픽 전환, Rollback, 검증 기준    |
| CI/CD                  | Build / Test / Deploy Pipeline 자동화          |
| Docker Advanced        | Image Build, Tag, Runtime, Compose 배포        |
| Infrastructure as Code | 배포 대상 인프라 Provisioning                  |
| Kubernetes             | Rolling Update, Service, Ingress, Rollout 구현 |
| Monitoring & Logging   | 배포 후 지표, 로그, 알림, 장애 감지            |
| Security Operations    | 배포 권한, Secret, 승인, 감사                  |

---

### [FAQ]

Q. Deployment Strategy와 CI/CD는 어디서 연결되는가?

A.
CI/CD Pipeline의 Deploy 단계, Approval Gate, Smoke Test, Rollback 자동화에서 연결된다.

Q. Deployment Strategy와 Docker Advanced는 어떻게 연결되는가?

A.
Docker Image Tag, Registry Pull, Container 재기동, Compose 배포, Rollback 대상 Image 관리에서 연결된다.

Q. Deployment Strategy와 Kubernetes는 어떻게 연결되는가?

A.
Kubernetes Deployment, RollingUpdate, Service, Ingress, Rollout, Rollback 기능으로 전략을 구현한다.

---

# 28. Retrieval Optimization Rules

## 28.1 Retrieval 최적화 규칙

### [개념]

Deployment Strategy 문서는 배포 문제 상황 검색에 강해야 한다.

사용자 질문은 주로 무중단 배포, Blue-Green, Canary, Rolling, Rollback, DB Migration, Health Check 오류 형태로 들어온다.

---

### [핵심]

강조 대상:

- Deployment Strategy
- Release Strategy
- Rolling Deployment
- Blue-Green Deployment
- Canary Deployment
- Feature Toggle
- Dark Launch
- Traffic Switching
- Health Check
- Smoke Test
- Monitoring
- Rollback
- Roll Forward
- Database Migration
- Backward Compatibility
- CI/CD Deployment Gate
- Kubernetes Rollout
- Docker Compose Deployment

---

### [실무]

반복 허용 키워드:

- 무중단 배포
- 배포 전략 선택
- Rolling Update
- Blue-Green Deployment
- Canary Deployment
- Feature Toggle
- Traffic Switching
- Deployment Health Check
- Smoke Test
- 배포 후 Monitoring
- Rollback 기준
- Roll Forward 기준
- DB Migration 배포 순서
- Backward Compatibility
- Kubernetes Rollout
- Docker Compose 배포
- 배포 실패 Troubleshooting

---

### [FAQ]

Q. Deployment Strategy RAG 문서는 어떤 질문에 강해야 하는가?

A.
무중단 배포, Blue-Green, Canary, Rolling, Rollback, Health Check, DB Migration, Kubernetes Rollout 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
Deployment, Release, Rolling, Blue-Green, Canary, Rollback, Health Check, Monitoring, Traffic Switching, DB Migration 키워드를 반복할 수 있다.

---

# 29. Version Rules

## 29.1 버전 기준

### [개념]

Deployment Strategy 문서는 Modern Deployment 기준으로 작성한다.

---

### [핵심]

기준:

- Container Image 기반 배포
- Docker Compose 소규모 운영
- Kubernetes Rolling Update
- Blue-Green Deployment
- Canary Deployment
- Feature Toggle
- Progressive Delivery
- CI/CD Approval Gate
- Observability 기반 배포 검증
- Automated Rollback 고려

---

### [실무]

Legacy 또는 낮은 우선순위:

- FTP 수동 업로드 중심 배포
- 서버 접속 후 직접 파일 교체
- Rollback 대상 없는 배포
- latest Tag 단독 배포
- Monitoring 없는 운영 배포
- DB Migration 검토 없는 배포
- 무조건 재시작 방식
- 배포 후 검증 생략

---

### [FAQ]

Q. Deployment Strategy 문서에서 수동 배포도 다루는가?

A.
위험 패턴과 비교 목적으로만 다룬다. 2026 기준 문서는 CI/CD, Container, Kubernetes, Monitoring 기반 배포를 우선한다.

Q. Progressive Delivery는 무엇인가?

A.
Canary, Feature Toggle, Metrics 기반 자동 판단처럼 변경을 점진적으로 안전하게 출시하는 배포 방식이다.

---

# 30. Quality Checklist

## 30.1 최종 검수 기준

### [개념]

Deployment Strategy RAG 문서는 Agent가 배포 전략을 선택하고 안전한 운영 배포를 검토할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Deployment Strategy Scope 충족
- CI/CD Domain Rules와 역할 분리
- Docker Advanced Domain Rules와 연결
- Infrastructure as Code Domain Rules와 연결
- Kubernetes Domain Rules와 연결
- Monitoring Domain Rules와 연결
- FAQ 포함
- Retrieval Queries 포함
- Blue-Green / Canary / Rolling 포함
- Rollback / Roll Forward 포함
- Health Check / Smoke Test 포함
- DB Migration / Compatibility 포함
- Traffic Switching 포함
- Troubleshooting 포함
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

Q. Deployment Strategy 문서 품질은 무엇으로 판단하는가?

A.
Agent가 배포 전략 선택, 위험 검토, Health Check 설계, Rollback 판단, DB Migration 배포 순서 검토를 수행할 수 있으면 품질이 높다.

---

# 31. Final Goal

## 31.1 최종 목표

### [개념]

Deployment Strategy RAG 문서는 단순 배포 방식 설명서가 아니다.

DevOps Agent / Backend Agent / Review Agent가 운영 배포를 안전하게 설계, 검토, 자동화, 복구하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Deployment Workflow
- Select Deployment Strategy
- Design Zero Downtime Deployment
- Review Rolling / Blue-Green / Canary
- Define Health Check and Smoke Test
- Define Rollback Criteria
- Review Database Migration Risk
- Connect Deployment with CI/CD
- Connect Deployment with Kubernetes
- Troubleshoot Deployment Failure

---

### [실무]

최종 연결 흐름:

```text
Application Change
→ CI/CD Pipeline
→ Docker Image
→ Deployment Strategy
→ Health Check
→ Traffic Switching
→ Monitoring
→ Rollback or Release Complete
```

---

### [FAQ]

Q. Deployment Strategy 문서의 최종 목적은?

A.
Agent가 운영 배포 전략을 선택하고, 안전하게 검토하며, 배포 실패 시 빠르게 복구할 수 있게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Deployment Strategy Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 운영 배포 전략, 트래픽 전환, 검증, Rollback을 수행하기 위한 RAG 작성 규칙이다.

Q. Deployment Strategy 문서의 핵심 범위는?
A. Rolling, Blue-Green, Canary, Feature Toggle, Traffic Switching, Health Check, Smoke Test, Monitoring, Rollback, DB Migration, CI/CD 연계이다.

Q. Deployment와 Release 차이는?
A. Deployment는 새 버전을 실행 환경에 배치하는 것이고 Release는 사용자에게 기능을 노출하는 것이다.

Q. Rollout은 무엇인가?
A. 새 버전을 전체 사용자에게 한 번에 반영하지 않고 단계적으로 확산하는 과정이다.

Q. 배포 전략은 어떻게 선택하는가?
A. 무중단 필요 여부, 트래픽 제어 가능 여부, 인스턴스 수, Rollback 요구사항, DB Migration 여부, 운영 복잡도를 기준으로 선택한다.

Q. Recreate Deployment는 무엇인가?
A. 기존 버전을 중지한 뒤 새 버전을 실행하는 가장 단순한 배포 방식이다.

Q. Recreate Deployment는 언제 사용하는가?
A. 다운타임이 허용되는 개발, 테스트, 내부 서비스, 소규모 서비스에서 사용할 수 있다.

Q. Rolling Deployment는 무엇인가?
A. 여러 인스턴스를 한 번에 교체하지 않고 순차적으로 새 버전으로 바꾸는 배포 전략이다.

Q. Rolling Deployment의 주의점은?
A. 구버전과 신버전이 동시에 실행되므로 API, DB, Cache, Message 호환성을 유지해야 한다.

Q. Blue-Green Deployment는 무엇인가?
A. 기존 Blue 환경과 새 Green 환경을 분리하고 Green 검증 후 트래픽을 전환하는 무중단 배포 전략이다.

Q. Blue-Green Deployment의 장점은?
A. 트래픽 전환이 빠르고 문제가 생기면 이전 Blue 환경으로 빠르게 되돌릴 수 있다.

Q. Blue-Green Deployment의 단점은?
A. 두 환경을 유지해야 하므로 비용이 증가하고 DB, Scheduler, Cache, Session 동기화 문제가 생길 수 있다.

Q. Canary Deployment는 무엇인가?
A. 새 버전을 일부 트래픽에만 먼저 노출한 뒤 안정성을 확인하면서 점진적으로 확대하는 배포 전략이다.

Q. Canary Deployment의 핵심 조건은?
A. 트래픽 비율 제어와 신뢰 가능한 Monitoring / Alerting이 필요하다.

Q. Feature Toggle은 왜 사용하는가?
A. 코드 배포와 기능 출시를 분리하고 특정 사용자에게 기능을 점진적으로 노출하기 위해 사용한다.

Q. Kill Switch는 무엇인가?
A. 문제가 생긴 기능을 코드 재배포 없이 즉시 비활성화하는 Toggle이다.

Q. Dark Launch는 무엇인가?
A. 기능을 사용자에게 직접 노출하지 않고 운영 환경에서 내부적으로 검증하는 출시 전략이다.

Q. Traffic Switching은 무엇인가?
A. 사용자 요청을 구버전에서 신버전으로 전환하거나 비율별로 분산하는 배포 제어 방식이다.

Q. DNS 전환은 왜 Rollback이 느릴 수 있는가?
A. DNS TTL과 캐시 때문에 변경 사항이 모든 사용자에게 즉시 반영되지 않을 수 있기 때문이다.

Q. Health Check는 왜 필요한가?
A. 배포된 애플리케이션이 실제 요청을 처리할 준비가 되었는지 확인하기 위해 필요하다.

Q. Readiness Check와 Liveness Check 차이는?
A. Readiness는 트래픽을 받을 준비 여부이고 Liveness는 애플리케이션이 살아있는지 확인하는 검사이다.

Q. Smoke Test는 무엇인가?
A. 배포 직후 핵심 기능이 정상 동작하는지 빠르게 확인하는 최소 검증 테스트이다.

Q. 배포 후 반드시 봐야 하는 지표는?
A. Error Rate, Latency, Traffic, Resource Usage, Log Error, 핵심 Business Metric을 확인해야 한다.

Q. Rollback은 무엇인가?
A. 배포 후 문제가 발생했을 때 이전 안정 버전으로 되돌리는 복구 전략이다.

Q. Rollback이 항상 가능한가?
A. 아니다. DB Schema 비호환 변경, 데이터 손상, 외부 시스템 변경이 있으면 단순 Rollback이 어려울 수 있다.

Q. Roll Forward는 무엇인가?
A. 이전 버전으로 되돌리지 않고 수정 버전을 배포하여 앞으로 복구하는 전략이다.

Q. DB Migration이 배포에서 위험한 이유는?
A. Schema 변경이 애플리케이션 버전과 호환되지 않으면 장애가 발생하고 단순 Rollback이 어려울 수 있기 때문이다.

Q. Expand and Contract는 무엇인가?
A. 먼저 호환 가능한 Schema를 확장하고, 새 버전 안정화 후 오래된 Schema를 제거하는 무중단 Migration 전략이다.

Q. Backward Compatibility는 왜 중요한가?
A. Rolling, Canary, Blue-Green 배포 중 구버전과 신버전, 기존 클라이언트가 동시에 존재할 수 있기 때문이다.

Q. Deployment Gate는 무엇인가?
A. 배포 전후 특정 검증 조건을 통과해야 다음 단계로 진행할 수 있게 하는 안전장치이다.

Q. Kubernetes에서 배포 상태는 어떻게 확인하는가?
A. `kubectl rollout status deployment/name` 명령으로 확인한다.

Q. Kubernetes Rollback은 어떻게 수행하는가?
A. `kubectl rollout undo deployment/name` 명령으로 이전 ReplicaSet 기반 Rollback을 수행할 수 있다.

Q. Docker Compose 배포에서 Rollback은 어떻게 하는가?
A. 이전 Image Tag로 되돌린 뒤 `docker compose up -d`로 재기동하고 Health Check를 확인한다.

Q. Frontend와 Backend 중 무엇을 먼저 배포해야 하는가?
A. 일반적으로 Backend가 기존 Frontend와 새 Frontend를 모두 지원하도록 먼저 배포한 뒤 Frontend를 배포하는 것이 안전하다.

Q. Release 기록은 왜 필요한가?
A. 장애 발생 시 어떤 변경이 원인인지 추적하고 빠르게 Rollback 대상을 찾기 위해 필요하다.

Q. 배포 실패 시 가장 먼저 확인할 것은?
A. Deployment 상태, Runtime 상태, Health Check, 로그, 최근 변경 사항을 먼저 확인한다.

Q. Rolling Update가 멈추는 가장 흔한 원인은?
A. Readiness Probe 실패, 새 Pod Crash, Resource 부족, Image Pull 실패, Config / Secret 오류이다.

Q. Canary 배포 실패 시 첫 조치는?
A. Canary 트래픽 확대를 중단하고 Error Rate, 로그, 사용자 영향 범위를 확인한 뒤 Rollback 여부를 결정한다.

Q. latest Image Tag가 배포에서 위험한 이유는?
A. 실제 배포된 버전을 추적하기 어렵고 Rollback 대상이 불명확해지기 때문이다.

Q. Deployment Strategy와 CI/CD는 어떻게 연결되는가?
A. CI/CD Pipeline의 Deploy 단계, Approval Gate, Smoke Test, Rollback 자동화에서 연결된다.

Q. Deployment Strategy와 Kubernetes는 어떻게 연결되는가?
A. Kubernetes Deployment, RollingUpdate, Service, Ingress, Rollout, Rollback 기능으로 전략을 구현한다.

Q. Deployment Strategy 문서의 최종 목적은?
A. Agent가 운영 배포 전략을 선택하고, 안전하게 검토하며, 배포 실패 시 빠르게 복구할 수 있게 만드는 것이다.
