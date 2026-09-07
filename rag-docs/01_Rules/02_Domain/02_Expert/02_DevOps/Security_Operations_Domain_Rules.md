# Security Operations Domain Rules

---

# 1. Domain Purpose

## 1.1 Security Operations 문서 목적

### [개념]

Security Operations Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Security Monitoring Support
- Incident Detection Support
- Vulnerability Management Support
- Secret / Credential Risk Review
- IAM / Access Control Review
- Audit Logging Support
- Security Incident Response Support
- DevSecOps Pipeline Review Support

우선순위:

1. Security Operations Core
2. IAM / Secret / Vulnerability
3. Security Monitoring / Audit Logging
4. Incident Response
5. DevSecOps / Compliance / Troubleshooting

---

### [핵심]

Security Operations 문서는 단순 보안 이론 문서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- 운영 보안 위험 식별
- IAM 권한 과다 탐지
- Secret Hardcoding 탐지
- Vulnerability Scan 기준 검토
- Container / Kubernetes 보안 검토
- Audit Log 기준 정의
- Security Alert 기준 정의
- 보안 사고 대응 Flow 설계
- CI/CD Security Gate 검토
- Infrastructure as Code 보안 검토
- Monitoring & Logging 문서와 연계

---

### [실무]

2026 실무 기준 Security Operations 문서는 다음 흐름을 기준으로 작성한다.

```text
Asset
→ Risk Detection
→ Security Monitoring
→ Alert
→ Triage
→ Containment
→ Eradication
→ Recovery
→ Post-Incident Review
```

Security Operations 문서는 개발 완료 후 보안 점검이 아니라 개발, 배포, 운영 전 과정에 보안을 연결하는 DevSecOps 운영 문서이다.

---

### [FAQ]

Q. Security Operations 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 운영 보안 위험을 탐지, 검토, 대응하기 위한 RAG 문서이다.

Q. Security Operations와 Spring Security 문서는 어떻게 다른가?

A.
Spring Security는 애플리케이션 인증 / 인가 구현 중심이고 Security Operations는 운영 보안, IAM, Secret, 취약점, 감사 로그, 사고 대응 중심이다.

Q. Security Operations는 DevOps 문서인가?

A.
DevOps Expert 영역에 포함된다. CI/CD, Docker, Kubernetes, IaC, Monitoring과 연결되는 운영 보안 문서이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Security Operations Domain 문서는 운영 환경에서 보안 위험을 줄이고 사고를 탐지, 대응, 복구하는 실무 기준을 다룬다.

포함 범위:

- Security Operations
- DevSecOps
- IAM
- Least Privilege
- Secret Management
- Credential Rotation
- Vulnerability Management
- Dependency Scan
- Container Image Scan
- Infrastructure as Code Security
- Kubernetes Security
- Network Security
- Audit Logging
- Security Monitoring
- SIEM
- Security Alert
- Incident Response
- Access Review
- Compliance
- Backup / Recovery
- Patch Management
- Threat Detection
- Security Runbook
- Post-Incident Review
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Security Operations
- DevSecOps
- IAM
- Least Privilege
- Secret
- Credential
- Vulnerability
- Audit Log
- Security Monitoring
- Security Alert
- Incident Response
- Access Control
- Compliance
- Container Security
- Kubernetes Security
- IaC Security
- CI/CD Security
- Zero Trust
- Defense in Depth

---

### [실무]

Security Operations 문서는 아래 상황을 해결할 수 있어야 한다.

- 운영 Secret 노출 여부 검토
- Git에 API Key가 올라간 사고 대응
- CI/CD Secret 권한 검토
- IAM Role 권한 과다 탐지
- S3 / Storage Public Access 탐지
- Docker Image 취약점 Scan
- Kubernetes Secret / RBAC 검토
- IaC Plan에서 Public Access 탐지
- Audit Log 기준 설계
- Security Alert 과다 발생 정리
- 보안 사고 발생 시 격리 / 복구 순서 정의
- 운영 접근 권한 정기 점검
- Dependency 취약점 대응 우선순위 판단

---

### [FAQ]

Q. Security Operations 문서에 암호학 이론을 깊게 포함해야 하는가?

A.
아니다. 운영 보안, 권한, Secret, 취약점, 감사 로그, 사고 대응, DevSecOps 검토 기준을 우선한다.

Q. Security Operations 문서에 공격 기법을 자세히 포함해야 하는가?

A.
방어와 탐지에 필요한 수준으로만 포함한다. 공격 재현보다 위험 패턴, 탐지 기준, 대응 절차를 우선한다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Security Operations 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

Security Operations 문서는 검색 친화적인 운영 보안 구조를 우선한다.

```text
Asset
→ Control
→ Detection
→ Alert
→ Response
→ Recovery
→ Review
```

---

### [실무]

권장 Part 구성:

- Security_Operations_Part01_Core.md
- Security_Operations_Part02_IAM_Access_Control.md
- Security_Operations_Part03_Secret_Management.md
- Security_Operations_Part04_Vulnerability_Management.md
- Security_Operations_Part05_Container_Kubernetes_Security.md
- Security_Operations_Part06_IaC_CI_CD_Security.md
- Security_Operations_Part07_Audit_Logging_Monitoring.md
- Security_Operations_Part08_Incident_Response.md
- Security_Operations_Part09_Compliance_Troubleshooting.md

---

### [FAQ]

Q. Security Operations 문서에 FAQ가 필요한가?

A.
필수이다. 보안 운영 질문은 “Secret이 노출됐다”, “권한이 과한가”, “취약점이 나왔다”, “보안 사고 대응 순서가 뭐냐”처럼 문제 상황 중심으로 들어온다.

Q. Security Operations 문서는 어떻게 작성해야 하는가?

A.
긴 이론보다 위험 패턴, 검토 기준, 대응 Flow, 체크리스트, FAQ를 우선한다.

---

# 4. Security Operations Core Rules

## 4.1 Security Operations Core 작성 규칙

### [개념]

Security Operations는 운영 중인 시스템의 보안 상태를 지속적으로 감시하고, 위험을 탐지하고, 사고 발생 시 대응하는 활동이다.

필수 포함:

- Asset Identification
- Risk Detection
- Access Control
- Security Monitoring
- Incident Response
- Recovery
- Continuous Improvement

---

### [핵심]

Security Operations 핵심 목표:

- 보안 사고 예방
- 침해 징후 조기 탐지
- 권한 오남용 방지
- Secret 노출 방지
- 취약점 대응
- 감사 가능성 확보
- 사고 발생 시 빠른 격리와 복구

기본 흐름:

```text
Prevent
→ Detect
→ Respond
→ Recover
→ Improve
```

---

### [실무]

Security Operations 대상:

- Application
- API
- Database
- Server
- Container
- Kubernetes
- CI/CD Pipeline
- Cloud Resource
- IAM Role
- Secret
- Network
- Audit Log
- Backup

---

### [FAQ]

Q. Security Operations의 핵심 목적은?

A.
운영 시스템의 보안 위험을 줄이고 침해 징후를 탐지하며 사고 발생 시 빠르게 대응하고 복구하는 것이다.

Q. 보안은 배포 후에만 확인하면 되는가?

A.
아니다. 개발, 코드 리뷰, CI/CD, 배포, 운영, 사고 대응 전 과정에 포함해야 한다.

---

# 5. DevSecOps Rules

## 5.1 DevSecOps 작성 규칙

### [개념]

DevSecOps는 DevOps Pipeline 전체에 보안 검증과 보안 자동화를 통합하는 방식이다.

---

### [핵심]

필수 포함:

- Shift Left Security
- Security Gate
- SAST
- DAST
- Dependency Scan
- Container Image Scan
- IaC Scan
- Secret Scan
- Policy as Code

---

### [Flow]

```text
Code Commit
→ Secret Scan
→ SAST
→ Dependency Scan
→ Container Image Scan
→ IaC Scan
→ Security Review
→ Deploy
```

---

### [실무]

CI/CD Security Gate 예시:

- Secret Scan 실패 시 Merge 차단
- Critical Vulnerability 발견 시 배포 차단
- IaC Public Access 발견 시 Review 필수
- Container Image High Risk 취약점 검토
- License Risk 확인
- 보안 승인자 Review
- 운영 배포 전 Security Checklist 확인

---

### [주의]

보안 Gate가 너무 약하면 사고 위험이 증가한다.

보안 Gate가 너무 강하면 배포 속도가 과도하게 느려질 수 있다.

Risk Severity 기준으로 차단 / 경고 / 승인 필요를 구분한다.

---

### [FAQ]

Q. DevSecOps는 무엇인가?

A.
개발과 운영 Pipeline에 보안 검증을 통합하여 보안 문제를 조기에 발견하고 자동으로 관리하는 방식이다.

Q. Shift Left Security는 무엇인가?

A.
보안 검토를 운영 직전이 아니라 개발 초기와 CI/CD 단계로 앞당기는 접근이다.

---

# 6. IAM / Access Control Rules

## 6.1 IAM 작성 규칙

### [개념]

IAM은 사용자, 서비스, 시스템이 어떤 리소스에 어떤 권한으로 접근할 수 있는지 관리하는 체계이다.

---

### [핵심]

필수 포함:

- IAM
- User
- Group
- Role
- Policy
- Permission
- Least Privilege
- Access Review
- Privilege Escalation
- Temporary Credential

---

### [실무]

IAM Review 기준:

- Admin 권한 남용 여부
- 사용하지 않는 User / Role 존재 여부
- 오래된 Access Key 존재 여부
- MFA 적용 여부
- Service Account 권한 범위
- CI/CD Role 권한 범위
- Production 접근 권한 제한
- Wildcard Permission 사용 여부
- Cross-account Trust 검토
- 권한 변경 Audit Log 확인

나쁜 예:

```json
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
```

검토 기준:

```text
필요한 작업
→ 필요한 리소스
→ 필요한 권한
→ 최소 권한 Policy
```

---

### [주의]

운영 환경에서 장기 Access Key 사용은 위험하다.

가능하면 Role 기반 임시 자격 증명, Workload Identity, OIDC Federation을 우선한다.

---

### [FAQ]

Q. Least Privilege는 무엇인가?

A.
작업에 필요한 최소한의 권한만 부여하는 보안 원칙이다.

Q. IAM에서 가장 위험한 패턴은?

A.
`Action: "*"`와 `Resource: "*"` 같은 전체 권한 부여, 오래된 Access Key, MFA 미적용, 사용하지 않는 권한 방치이다.

Q. CI/CD에 Admin 권한을 줘도 되는가?

A.
권장하지 않는다. 배포에 필요한 최소 권한만 부여하고 환경별 권한을 분리해야 한다.

---

# 7. Secret Management Rules

## 7.1 Secret Management 작성 규칙

### [개념]

Secret Management는 Password, Token, API Key, Private Key, Credential을 안전하게 저장, 주입, 회전, 폐기하는 운영 기준이다.

---

### [핵심]

필수 포함:

- Secret
- Credential
- API Key
- Token
- Private Key
- Secret Manager
- Environment Variable
- Rotation
- Revocation
- Secret Scan
- Hardcoding 금지

---

### [실무]

Secret 관리 원칙:

- 코드에 Secret 직접 작성 금지
- Git Commit 금지
- Docker Image에 Secret 포함 금지
- Terraform State 노출 주의
- CI/CD Secret 권한 제한
- 환경별 Secret 분리
- Secret Rotation 주기 정의
- Secret 접근 Audit Log 수집
- 노출 시 즉시 폐기 후 재발급

금지 예시:

```text
DB_PASSWORD=my-real-password
OPENAI_API_KEY=sk-real-key
AWS_SECRET_ACCESS_KEY=real-secret
```

권장 구조:

```text
Secret Manager
→ CI/CD or Runtime
→ Application Environment
```

---

### [주의]

`.env` 파일은 편하지만 유출 위험이 높다.

운영 Secret은 Secret Manager 또는 안전한 Credential Store를 우선한다.

---

### [FAQ]

Q. Secret Hardcoding이 위험한 이유는?

A.
Git, Docker Image, Log, CI/CD Artifact, Terraform State를 통해 Credential이 노출될 수 있기 때문이다.

Q. Secret이 노출되면 어떻게 해야 하는가?

A.
즉시 Secret을 폐기하고 재발급하며 사용 이력을 확인하고 노출 경로를 제거해야 한다.

Q. `.env` 파일을 운영 Secret 저장소로 사용해도 되는가?

A.
소규모에서는 가능하지만 위험하다. 운영에서는 Secret Manager와 접근 제어를 우선한다.

---

# 8. Credential Rotation Rules

## 8.1 Credential Rotation 작성 규칙

### [개념]

Credential Rotation은 Secret, Token, Key를 주기적으로 또는 사고 발생 시 새 값으로 교체하는 절차이다.

---

### [핵심]

필수 포함:

- Rotation
- Revocation
- Expiration
- Key Version
- Grace Period
- Rollout
- Audit

---

### [Flow]

```text
Create New Credential
→ Deploy New Credential
→ Verify Usage
→ Disable Old Credential
→ Delete Old Credential
→ Audit
```

---

### [실무]

Rotation 대상:

- API Key
- DB Password
- Cloud Access Key
- OAuth Client Secret
- JWT Signing Key
- SSH Key
- Webhook Secret
- CI/CD Token

Rotation 시 확인:

- 새 Credential 적용 여부
- 구 Credential 사용 중인 서비스 확인
- 배포 순서
- 장애 발생 시 Rollback 계획
- Audit Log 확인
- 구 Credential 폐기 완료

---

### [FAQ]

Q. Credential Rotation은 언제 필요한가?

A.
정기 보안 정책, 담당자 변경, 권한 변경, Secret 노출 의심, 외부 연동 변경 시 필요하다.

Q. Rotation에서 가장 중요한 것은?

A.
새 Credential 적용 확인 후 구 Credential을 비활성화하고, 사용 이력과 접근 로그를 확인하는 것이다.

---

# 9. Vulnerability Management Rules

## 9.1 Vulnerability Management 작성 규칙

### [개념]

Vulnerability Management는 애플리케이션, Dependency, Container Image, OS Package, Infrastructure의 취약점을 탐지하고 우선순위에 따라 조치하는 활동이다.

---

### [핵심]

필수 포함:

- Vulnerability
- CVE
- CVSS
- Severity
- Dependency Scan
- Container Scan
- Patch
- Mitigation
- Risk Acceptance
- Remediation SLA

---

### [실무]

취약점 대응 기준:

| Severity | 기본 대응                |
| -------- | ------------------------ |
| Critical | 즉시 조치 또는 배포 차단 |
| High     | 빠른 조치 및 승인 필요   |
| Medium   | 계획 수립 후 조치        |
| Low      | 추적 관리                |

취약점 판단 기준:

- 실제 사용 여부
- 외부 노출 여부
- 인증 우회 가능성
- 원격 코드 실행 가능성
- 데이터 유출 가능성
- 패치 가능 여부
- 대체 완화책 존재 여부

---

### [주의]

취약점 Scan 결과는 그대로 배포 차단 기준이 아니다.

실제 영향, Exploit 가능성, 노출 범위, 운영 중요도를 함께 판단해야 한다.

---

### [FAQ]

Q. Vulnerability Management는 무엇인가?

A.
취약점을 탐지하고 위험도에 따라 패치, 완화, 추적, 승인하는 운영 보안 활동이다.

Q. CVSS 점수만 보고 우선순위를 정하면 되는가?

A.
아니다. 실제 사용 여부, 외부 노출 여부, Exploit 가능성, 서비스 중요도를 함께 봐야 한다.

---

# 10. Dependency Security Rules

## 10.1 Dependency Security 작성 규칙

### [개념]

Dependency Security는 애플리케이션이 사용하는 라이브러리, 패키지, 프레임워크의 취약점과 공급망 위험을 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Dependency Scan
- Software Supply Chain
- SBOM
- License Risk
- Package Lock
- Version Pinning
- Transitive Dependency
- Update Policy

---

### [실무]

검토 대상:

- Maven / Gradle Dependency
- npm Package
- Python Package
- Docker Base Image
- GitHub Actions Dependency
- Transitive Dependency
- License
- Deprecated Package
- Maintainer Risk

실무 기준:

- Lock File 유지
- 자동 업데이트 PR 검토
- Critical / High 취약점 우선 조치
- 사용하지 않는 Dependency 제거
- 출처 불명 Package 금지
- SBOM 생성 고려

---

### [FAQ]

Q. Dependency Scan은 왜 필요한가?

A.
사용 중인 라이브러리와 하위 의존성의 알려진 취약점을 조기에 발견하기 위해 필요하다.

Q. Transitive Dependency는 무엇인가?

A.
직접 추가한 라이브러리가 내부적으로 의존하는 간접 의존성이다.

---

# 11. Container Security Rules

## 11.1 Container Security 작성 규칙

### [개념]

Container Security는 Docker Image와 Container Runtime에서 발생할 수 있는 보안 위험을 줄이는 기준이다.

---

### [핵심]

필수 포함:

- Minimal Base Image
- Image Scan
- Non-root User
- Read-only Filesystem
- Capability Drop
- Privileged Mode 금지
- Docker Socket Mount 금지
- Secret in Image 금지

---

### [실무]

Container Security Review 기준:

- Base Image 버전 고정
- Image 취약점 Scan
- Non-root User 사용
- 불필요 Package 제거
- Secret 포함 여부 확인
- `privileged: true` 금지
- Docker Socket Mount 금지
- Resource Limit 설정
- Healthcheck 설정
- Image Tag 추적 가능성 확보

위험 예시:

```yaml
services:
  app:
    privileged: true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

---

### [FAQ]

Q. Container를 root로 실행하면 왜 위험한가?

A.
Container 탈출이나 권한 상승 사고 시 Host와 다른 리소스에 미치는 피해가 커질 수 있다.

Q. Docker Socket Mount가 위험한 이유는?

A.
Container 내부에서 Host Docker Daemon을 제어할 수 있어 Host 장악 위험이 생긴다.

---

# 12. Kubernetes Security Rules

## 12.1 Kubernetes Security 작성 규칙

### [개념]

Kubernetes Security는 Cluster, Node, Pod, Secret, RBAC, Network Policy, Admission Control을 안전하게 운영하는 기준이다.

---

### [핵심]

필수 포함:

- RBAC
- Service Account
- Kubernetes Secret
- Network Policy
- Pod Security
- Admission Control
- Namespace Isolation
- Resource Quota
- Image Pull Policy
- Audit Log

---

### [실무]

Kubernetes Security Review 기준:

- Default Service Account 사용 여부
- 과도한 ClusterRoleBinding 여부
- Namespace 분리 여부
- Secret 평문 노출 여부
- Pod가 root로 실행되는지 확인
- Privileged Pod 금지
- HostPath Mount 제한
- Network Policy 적용
- Image Registry 신뢰성 확인
- Resource Limit 설정
- Kubernetes Audit Log 활성화

위험 패턴:

```text
cluster-admin 권한 남용
default namespace 운영 사용
privileged pod
hostPath mount
secret yaml Git commit
NetworkPolicy 없음
```

---

### [FAQ]

Q. Kubernetes RBAC에서 가장 위험한 실수는?

A.
불필요한 cluster-admin 권한 부여와 Default Service Account에 과도한 권한을 주는 것이다.

Q. Kubernetes Secret은 완전히 안전한가?

A.
아니다. 기본적으로 인코딩된 값이며 접근 권한, 암호화, Secret Store 연계를 함께 고려해야 한다.

---

# 13. Infrastructure as Code Security Rules

## 13.1 IaC Security 작성 규칙

### [개념]

Infrastructure as Code Security는 Terraform / OpenTofu 같은 IaC 코드에서 위험한 인프라 설정을 배포 전에 탐지하는 기준이다.

---

### [핵심]

필수 포함:

- IaC Scan
- Policy as Code
- Public Access Detection
- Security Group Review
- IAM Policy Review
- Encryption
- Backup
- Logging
- Prevent Destroy

---

### [실무]

IaC Security Review 대상:

- S3 / Storage Public Access
- Security Group `0.0.0.0/0`
- IAM `Action: "*"`
- 암호화 비활성화
- Backup 미설정
- Audit Log 미설정
- 운영 DB `prevent_destroy` 누락
- Remote State 암호화 / Locking 누락
- Secret Hardcoding
- Provider Version 미고정

---

### [FAQ]

Q. IaC Security Scan은 왜 필요한가?

A.
위험한 인프라 설정이 운영에 반영되기 전에 자동으로 탐지하기 위해 필요하다.

Q. IaC에서 가장 위험한 설정은?

A.
Public Access, 과도한 IAM 권한, 암호화 비활성화, Secret Hardcoding, 운영 리소스 삭제 위험이다.

---

# 14. CI/CD Security Rules

## 14.1 CI/CD Security 작성 규칙

### [개념]

CI/CD Security는 Pipeline, Runner, Artifact, Secret, Registry, Deployment 권한을 안전하게 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Pipeline Security
- CI/CD Secret
- Runner Permission
- Artifact Integrity
- Registry Access
- Deployment Approval
- OIDC Federation
- Branch Protection

---

### [실무]

CI/CD Security Review 기준:

- Branch Protection 적용
- Pull Request Review 필수
- Secret 접근 범위 제한
- Fork PR Secret 노출 방지
- Runner 권한 최소화
- 배포 Job 권한 분리
- 운영 배포 Manual Approval
- Artifact 서명 / 검증 고려
- Registry Push 권한 제한
- CI/CD Log에 Secret 노출 금지

---

### [주의]

CI/CD Pipeline은 배포 권한을 가진 고위험 경로이다.

Pipeline 탈취는 운영 배포 탈취로 이어질 수 있다.

---

### [FAQ]

Q. CI/CD Security에서 가장 중요한 것은?

A.
Secret 보호, Runner 권한 제한, Branch Protection, 배포 승인, Artifact 무결성이다.

Q. CI/CD Log에 Secret이 출력되면 어떻게 해야 하는가?

A.
즉시 Secret을 폐기하고 재발급하며 Log 접근 범위와 Pipeline 출력 내용을 점검해야 한다.

---

# 15. Network Security Rules

## 15.1 Network Security 작성 규칙

### [개념]

Network Security는 서비스 간 통신, 외부 노출, 방화벽, 보안 그룹, TLS, Ingress / Egress를 통제하는 기준이다.

---

### [핵심]

필수 포함:

- Firewall
- Security Group
- Ingress
- Egress
- Private Network
- TLS
- Network Policy
- Zero Trust
- Port Exposure

---

### [실무]

Network Security Review 기준:

- 운영 DB Public Access 금지
- 관리자 포트 외부 공개 금지
- SSH 접근 IP 제한
- Security Group 최소 포트 개방
- TLS 적용
- 내부 서비스 Private Network 우선
- Kubernetes Network Policy 검토
- 불필요한 Egress 차단 검토
- Load Balancer 노출 범위 확인

위험 예시:

```text
0.0.0.0/0:22
0.0.0.0/0:3306
Public RDS
내부 관리자 API 외부 공개
TLS 미적용 로그인 API
```

---

### [FAQ]

Q. Network Security에서 가장 흔한 위험은?

A.
관리자 포트, DB 포트, 내부 API가 Public Internet에 노출되는 것이다.

Q. `0.0.0.0/0`은 항상 나쁜가?

A.
HTTP / HTTPS 공개 서비스에는 필요할 수 있다. 하지만 SSH, DB, 관리자 포트에는 매우 위험하다.

---

# 16. Audit Logging Rules

## 16.1 Audit Logging 작성 규칙

### [개념]

Audit Logging은 중요한 보안 / 운영 행위에 대해 누가, 언제, 무엇을, 어떤 결과로 수행했는지 기록하는 것이다.

---

### [핵심]

필수 포함:

- Audit Log
- Actor
- Action
- Target
- Result
- Timestamp
- Source IP
- Trace ID
- Tamper Resistance
- Retention

---

### [실무]

Audit Log 대상:

- 로그인 성공 / 실패
- 관리자 로그인
- 권한 변경
- 비밀번호 변경
- Secret 조회 / 변경
- 배포 승인
- 인프라 변경
- 결제 상태 변경
- 데이터 삭제
- 보안 설정 변경
- Backup / Restore
- 사용자 개인정보 접근

Audit Log 필드:

```json
{
  "timestamp": "2026-06-29T10:00:00+09:00",
  "actor": "admin-user",
  "action": "ROLE_CHANGE",
  "target": "user-123",
  "result": "SUCCESS",
  "sourceIp": "203.0.113.10",
  "traceId": "trace-001"
}
```

---

### [주의]

Audit Log는 조작 방지, 접근 제한, 보존 정책이 중요하다.

Audit Log에 Password, Token, 카드번호 같은 민감 정보 원문을 남기면 안 된다.

---

### [FAQ]

Q. Audit Log는 왜 필요한가?

A.
보안 사고와 운영 사고 발생 시 누가 어떤 작업을 했는지 추적하고 책임 경로를 확인하기 위해 필요하다.

Q. Audit Log와 Application Log는 같은가?

A.
아니다. Application Log는 동작 분석 중심이고 Audit Log는 중요한 행위의 추적성과 증적 중심이다.

---

# 17. Security Monitoring Rules

## 17.1 Security Monitoring 작성 규칙

### [개념]

Security Monitoring은 보안 이벤트와 이상 행위를 지속적으로 감시하여 침해 징후를 탐지하는 활동이다.

---

### [핵심]

필수 포함:

- Security Event
- Threat Detection
- Failed Login
- Anomaly Detection
- Privilege Change
- Suspicious Access
- SIEM
- Alert Rule

---

### [실무]

Security Monitoring 대상:

- 로그인 실패 급증
- 관리자 로그인
- 해외 / 비정상 위치 로그인
- 권한 변경
- Secret 접근
- 대량 데이터 조회
- 관리자 API 호출
- WAF 차단 이벤트
- 4xx / 5xx 급증
- 비정상 User-Agent
- Brute Force 의심
- Rate Limit 초과
- IAM Policy 변경
- 보안 그룹 변경
- CloudTrail / Audit Log 이벤트

---

### [FAQ]

Q. Security Monitoring은 일반 Monitoring과 무엇이 다른가?

A.
일반 Monitoring은 성능과 장애 중심이고 Security Monitoring은 권한, 접근, 이상 행위, 침해 징후 탐지 중심이다.

Q. 로그인 실패가 많으면 항상 공격인가?

A.
아니다. 사용자 실수나 외부 장애일 수 있다. 실패 패턴, IP, 계정 수, 시간대, User-Agent를 함께 봐야 한다.

---

# 18. Security Alert Rules

## 18.1 Security Alert 작성 규칙

### [개념]

Security Alert는 보안 위험이 감지되었을 때 담당자에게 조치를 요구하는 알림이다.

---

### [핵심]

필수 포함:

- Alert Severity
- Critical Alert
- Warning Alert
- False Positive
- Alert Fatigue
- Escalation
- Runbook

---

### [실무]

Critical Alert 예시:

- 운영 Secret 노출 탐지
- 관리자 계정 탈취 의심
- Public DB 노출
- IAM Admin 권한 갑작스러운 부여
- 대량 데이터 유출 의심
- WAF 공격 차단 급증
- Kubernetes cluster-admin 권한 변경
- CI/CD 배포 권한 비정상 사용

Warning Alert 예시:

- 로그인 실패 증가
- 취약점 High 발견
- 오래된 Access Key 발견
- 보안 그룹 변경
- Audit Log 수집 지연
- 외부 IP 접근 증가

---

### [주의]

Security Alert는 조치 가능한 기준으로 설계해야 한다.

Runbook이 없는 Alert는 운영 피로도를 높인다.

---

### [FAQ]

Q. Security Alert의 좋은 기준은?

A.
위험도가 명확하고 조치 방법이 있으며 담당자와 Escalation 경로가 정의되어 있어야 한다.

Q. False Positive가 많으면 어떻게 해야 하는가?

A.
탐지 조건, 임계치, 예외 규칙, Severity, Runbook을 조정해야 한다.

---

# 19. Incident Response Rules

## 19.1 Security Incident Response 작성 규칙

### [개념]

Security Incident Response는 보안 사고를 감지한 뒤 피해 확산을 막고 원인을 제거하며 정상 상태로 복구하는 절차이다.

---

### [핵심]

필수 포함:

- Detection
- Triage
- Containment
- Eradication
- Recovery
- Evidence Preservation
- Communication
- Post-Incident Review

---

### [Flow]

```text
Alert
→ Triage
→ Containment
→ Evidence Preservation
→ Eradication
→ Recovery
→ Post-Incident Review
```

---

### [실무]

Security Incident 대응 순서:

1. Alert / 신고 확인
2. 사고 유형 분류
3. 영향 범위 확인
4. 관련 계정 / Secret / 리소스 격리
5. 증거 보존
6. 유출 Credential 폐기
7. 취약점 또는 설정 오류 제거
8. 서비스 복구
9. Audit Log / Access Log 분석
10. 재발 방지 조치
11. Post-Incident Review 작성

---

### [주의]

보안 사고 중 무작정 로그나 리소스를 삭제하면 증거가 손실될 수 있다.

격리와 증거 보존을 함께 고려한다.

---

### [FAQ]

Q. 보안 사고 대응에서 가장 먼저 할 일은?

A.
영향 범위를 확인하고 피해 확산을 막기 위해 계정, Secret, 네트워크, 리소스를 격리해야 한다.

Q. 보안 사고에서 증거 보존이 중요한 이유는?

A.
침해 경로, 피해 범위, 재발 방지책을 분석하기 위해 로그와 상태 정보가 필요하기 때문이다.

---

# 20. Secret Leak Response Rules

## 20.1 Secret Leak 대응 규칙

### [개념]

Secret Leak Response는 API Key, Token, Password, Private Key 같은 Credential이 노출되었을 때 수행하는 긴급 대응 절차이다.

---

### [핵심]

필수 포함:

- Leak Detection
- Immediate Revocation
- Rotation
- Scope Analysis
- Audit Log
- Repository Cleanup
- Image Rebuild
- State Review

---

### [Flow]

```text
Secret Leak Detected
→ Revoke Secret
→ Issue New Secret
→ Deploy New Secret
→ Audit Usage
→ Remove Exposure
→ Prevent Recurrence
```

---

### [실무]

Secret 노출 대응 Checklist:

- 노출 Secret 즉시 폐기
- 새 Secret 발급
- 관련 서비스 재배포
- 사용 이력 확인
- 비정상 접근 확인
- Git History 정리 검토
- Docker Image / Artifact 재생성
- CI/CD Log 노출 확인
- Terraform State 포함 여부 확인
- Secret Scan Rule 추가
- 재발 방지 교육 / 자동화 추가

---

### [FAQ]

Q. Git에 API Key를 올렸는데 삭제 Commit만 하면 충분한가?

A.
아니다. Git History에 남을 수 있으므로 해당 Key를 즉시 폐기하고 재발급해야 한다.

Q. Secret이 Docker Image에 들어갔으면 어떻게 해야 하는가?

A.
Secret을 폐기하고 Image를 재빌드하며 기존 Image와 Registry 접근 범위를 점검해야 한다.

---

# 21. Backup / Recovery Security Rules

## 21.1 Backup / Recovery 보안 규칙

### [개념]

Backup / Recovery Security는 장애나 보안 사고 후 데이터를 복구할 수 있도록 백업을 보호하고 복구 가능성을 검증하는 기준이다.

---

### [핵심]

필수 포함:

- Backup
- Recovery
- RPO
- RTO
- Encryption
- Access Control
- Restore Test
- Immutable Backup

---

### [실무]

보안 관점 Backup Review 기준:

- Backup 암호화
- Backup 접근 권한 제한
- 운영 DB Backup 주기
- Restore Test 수행
- Backup Retention 정책
- Ransomware 대비 Immutable Backup
- Backup 삭제 권한 제한
- Backup Audit Log
- Cross-region Backup 검토

---

### [FAQ]

Q. Backup이 있으면 복구가 보장되는가?

A.
아니다. Restore Test를 통해 실제 복구 가능성을 검증해야 한다.

Q. Backup도 보안 관리 대상인가?

A.
그렇다. Backup에는 민감 데이터가 포함될 수 있으므로 암호화와 접근 제어가 필요하다.

---

# 22. Compliance Rules

## 22.1 Compliance 작성 규칙

### [개념]

Compliance는 법규, 보안 정책, 내부 기준, 감사 요구사항을 만족하기 위한 운영 보안 관리이다.

---

### [핵심]

필수 포함:

- Compliance
- Policy
- Audit
- Evidence
- Retention
- Access Review
- Data Protection
- Change Management

---

### [실무]

Compliance Evidence 예시:

- Access Review 기록
- 배포 승인 기록
- Audit Log
- 취약점 조치 기록
- Backup / Restore Test 기록
- Incident Report
- 보안 교육 기록
- 권한 변경 이력
- 인프라 변경 이력
- Encryption 적용 증적

---

### [주의]

Compliance는 문서만 작성하는 것이 아니다.

실제 통제, 기록, 검증, 개선이 함께 있어야 한다.

---

### [FAQ]

Q. Compliance에서 Evidence가 중요한 이유는?

A.
보안 통제가 실제로 수행되었음을 증명하기 위해 필요하다.

Q. Compliance와 Security Operations는 어떻게 연결되는가?

A.
Security Operations의 로그, 접근 검토, 사고 대응, 취약점 관리 기록이 Compliance Evidence가 된다.

---

# 23. Patch Management Rules

## 23.1 Patch Management 작성 규칙

### [개념]

Patch Management는 OS, Runtime, Library, Container Base Image, Kubernetes Component의 보안 업데이트를 계획하고 적용하는 활동이다.

---

### [핵심]

필수 포함:

- Security Patch
- OS Update
- Runtime Update
- Dependency Update
- Base Image Update
- Maintenance Window
- Rollback Plan
- Patch Priority

---

### [실무]

Patch 대상:

- Linux Package
- Java Runtime
- Node.js Runtime
- Docker Base Image
- Application Dependency
- Database Engine
- Kubernetes Component
- CI/CD Runner
- Monitoring Agent

Patch 우선순위:

```text
Exploited Critical
→ Internet-facing High
→ Auth / Data Exposure Risk
→ Internal High
→ Medium / Low
```

---

### [FAQ]

Q. Patch Management는 왜 필요한가?

A.
알려진 취약점이 공격에 악용되기 전에 시스템을 업데이트하기 위해 필요하다.

Q. 모든 Patch를 즉시 적용해야 하는가?

A.
아니다. 위험도, 영향 범위, 테스트 가능성, Rollback 계획을 기준으로 우선순위를 정해야 한다.

---

# 24. Access Review Rules

## 24.1 Access Review 작성 규칙

### [개념]

Access Review는 사용자, 관리자, 서비스 계정, CI/CD 권한이 적절한지 정기적으로 검토하는 활동이다.

---

### [핵심]

필수 포함:

- User Access Review
- Admin Access
- Service Account
- Dormant Account
- Permission Creep
- Joiner / Mover / Leaver
- MFA
- Access Revocation

---

### [실무]

Access Review 대상:

- 운영 서버 접근 권한
- Cloud Console 권한
- Database 접근 권한
- Kubernetes Cluster 권한
- CI/CD 배포 권한
- Secret Manager 접근 권한
- Git Repository 관리자 권한
- Monitoring / Audit Log 접근 권한

검토 기준:

- 퇴사자 / 이동자 권한 제거
- 사용하지 않는 계정 제거
- 과도한 관리자 권한 제거
- MFA 적용 확인
- 장기 Access Key 제거
- 권한 변경 이력 확인

---

### [FAQ]

Q. Access Review는 왜 필요한가?

A.
시간이 지나며 누적된 불필요하거나 과도한 권한을 제거하여 침해 위험을 줄이기 위해 필요하다.

Q. Permission Creep은 무엇인가?

A.
업무 변경이나 임시 권한 부여 후 권한이 회수되지 않고 계속 누적되는 현상이다.

---

# 25. Security Runbook Rules

## 25.1 Security Runbook 작성 규칙

### [개념]

Security Runbook은 보안 사고나 알림 발생 시 담당자가 따라야 하는 표준 대응 절차이다.

---

### [핵심]

필수 포함:

- Alert Type
- Severity
- Owner
- Initial Check
- Containment
- Escalation
- Recovery
- Evidence
- Communication

---

### [실무]

Runbook 기본 구조:

```text
Alert Name:
Severity:
Owner:
Impact:
Initial Check:
Containment:
Investigation:
Recovery:
Escalation:
Evidence:
Post-Incident Action:
```

Runbook 대상:

- Secret Leak
- Brute Force
- Admin Account Compromise
- Public DB Exposure
- Suspicious IAM Change
- Container Escape Suspicion
- Kubernetes RBAC Abuse
- CI/CD Pipeline Compromise
- Data Exfiltration Suspicion

---

### [FAQ]

Q. Security Runbook은 왜 필요한가?

A.
보안 사고 발생 시 혼란을 줄이고 빠르게 일관된 대응을 하기 위해 필요하다.

Q. Runbook 없는 Alert는 왜 문제인가?

A.
알림을 받아도 담당자가 무엇을 확인하고 어떻게 대응해야 하는지 알기 어렵기 때문이다.

---

# 26. Troubleshooting Rules

## 26.1 Security Operations Troubleshooting 작성 규칙

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

- Secret Leak
- Access Denied
- Permission Too Broad
- Vulnerability Found
- Security Alert Too Noisy
- Audit Log Missing
- Container Image Vulnerability
- Kubernetes RBAC Misconfiguration
- Public Access Detected
- CI/CD Secret Exposed
- IAM Key Compromised
- Failed Login Spike
- Suspicious Deployment

---

### [실무]

기본 확인 흐름:

```text
Security Event
→ Scope 확인
→ Asset 확인
→ Credential 확인
→ Access Log 확인
→ Audit Log 확인
→ Containment
→ Remediation
→ Prevention
```

---

### [Troubleshooting]

문제:
Secret이 노출되었다.

원인:

- Git Commit
- CI/CD Log 출력
- Docker Image 포함
- Terraform State 포함
- Chat / 문서 공유

해결:

```text
Secret 폐기
→ 새 Secret 발급
→ 서비스 재배포
→ 사용 이력 확인
→ 노출 경로 제거
→ Secret Scan 추가
```

문제:
권한이 너무 넓다.

원인:

- Admin Policy 남용
- Wildcard Permission 사용
- 임시 권한 미회수
- Service Account 공용 사용

해결:

```text
사용 작업 식별
→ 필요한 Resource 식별
→ 최소 권한 Policy 작성
→ 기존 권한 제거
→ Audit Log 확인
```

문제:
취약점 Scan에서 Critical이 발견되었다.

원인:

- 오래된 Dependency
- 취약한 Base Image
- OS Package 미패치
- Transitive Dependency 취약점

해결:

```text
실제 영향 확인
→ 외부 노출 여부 확인
→ Patch / Upgrade
→ Mitigation 적용
→ 재스캔
```

문제:
Audit Log가 없다.

원인:

- 감사 로그 비활성화
- 로그 수집 설정 누락
- Retention 만료
- 권한 부족
- Collector 장애

해결:

```text
Audit 설정 확인
→ Collector 확인
→ Storage 확인
→ Retention 확인
→ Alert 추가
```

---

### [FAQ]

Q. Secret Leak 대응 첫 단계는?

A.
노출된 Secret을 즉시 폐기하고 새 Secret을 발급하는 것이다.

Q. Access Denied 오류는 항상 보안 문제인가?

A.
아니다. 정상적인 최소 권한 정책일 수도 있다. 필요한 작업과 권한 범위를 확인해야 한다.

Q. Security Alert가 너무 많으면 어떻게 해야 하는가?

A.
Severity, 임계치, 예외 규칙, Runbook, 중복 Alert를 정리해야 한다.

---

# 27. Common Mistakes

## 27.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 Security Operations 구성을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- Secret Hardcoding
- `.env` Git Commit
- Terraform State 유출
- CI/CD Log에 Secret 출력
- Admin 권한 남용
- 장기 Access Key 방치
- MFA 미적용
- 사용하지 않는 계정 방치
- Public DB 노출
- Security Group 과다 개방
- Audit Log 미수집
- Alert Rule 없음
- Runbook 없는 Alert
- 취약점 Scan 미수행
- Container Image Scan 누락
- Kubernetes cluster-admin 남용
- Docker Socket Mount 허용
- Backup 암호화 누락
- Restore Test 미수행
- Patch 지연
- 보안 사고 후 Secret 미폐기

---

### [실무]

Review Agent 검토 기준:

```text
Asset
→ IAM
→ Secret
→ Network
→ Container
→ Kubernetes
→ IaC
→ CI/CD
→ Audit Log
→ Security Alert
→ Incident Runbook
```

---

### [FAQ]

Q. Security Operations Review에서 가장 먼저 확인할 것은?

A.
Secret 노출, IAM 과다 권한, Public Access, Audit Log, 취약점 Scan, Incident Runbook을 먼저 확인한다.

Q. 운영 보안에서 가장 위험한 실수는?

A.
Secret 유출, 관리자 권한 남용, Public DB 노출, Audit Log 미수집, 사고 대응 절차 부재이다.

---

# 28. File Relationship Rules

## 28.1 다른 Domain Rules와 연계

### [개념]

Security Operations Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Docker Advanced, Infrastructure as Code, Deployment Strategy, Monitoring & Logging, Kubernetes와 연결된다.

---

### [핵심]

연계 구조:

```text
Security Operations
→ CI/CD Security
→ IaC Security
→ Container Security
→ Kubernetes Security
→ Monitoring & Logging
→ Incident Response
```

---

### [실무]

파일 간 역할 분리:

| Domain                 | 역할                                         |
| ---------------------- | -------------------------------------------- |
| Security Operations    | 운영 보안, IAM, Secret, 취약점, 사고 대응    |
| CI/CD                  | Security Gate, Secret Scan, 배포 승인        |
| Docker Advanced        | Container Security, Image Scan, Runtime Risk |
| Infrastructure as Code | Public Access, IAM, State, Policy as Code    |
| Deployment Strategy    | 안전한 배포, Rollback, 승인                  |
| Monitoring & Logging   | Security Monitoring, Audit Log, Alert        |
| Kubernetes             | RBAC, Secret, Network Policy, Pod Security   |

---

### [FAQ]

Q. Security Operations와 Monitoring & Logging은 어떻게 연결되는가?

A.
Security Monitoring, Audit Log, Security Alert, Incident Detection에서 연결된다.

Q. Security Operations와 IaC는 어떻게 연결되는가?

A.
IaC 코드에서 Public Access, IAM 과다 권한, Secret Hardcoding, State 노출을 검토하는 단계에서 연결된다.

Q. Security Operations와 CI/CD는 어떻게 연결되는가?

A.
Secret Scan, 취약점 Scan, Security Gate, 배포 승인, Artifact 검증에서 연결된다.

---

# 29. Retrieval Optimization Rules

## 29.1 Retrieval 최적화 규칙

### [개념]

Security Operations 문서는 운영 보안 문제 상황 검색에 강해야 한다.

사용자 질문은 주로 Secret 노출, 권한 문제, 취약점, Public Access, Audit Log, Security Alert, 사고 대응 형태로 들어온다.

---

### [핵심]

강조 대상:

- Security Operations
- DevSecOps
- IAM
- Least Privilege
- Secret Management
- Credential Rotation
- Vulnerability Management
- Container Security
- Kubernetes Security
- IaC Security
- CI/CD Security
- Network Security
- Audit Logging
- Security Monitoring
- Security Alert
- Incident Response
- Compliance
- Patch Management
- Access Review
- Security Runbook

---

### [실무]

반복 허용 키워드:

- Secret Leak 대응
- Secret Hardcoding 금지
- IAM 권한 과다
- Least Privilege
- Access Key Rotation
- Vulnerability Scan
- Container Image Scan
- Kubernetes RBAC
- Terraform State Secret
- Public Access 탐지
- Security Group 0.0.0.0/0
- CI/CD Secret 노출
- Audit Log 누락
- Security Alert 기준
- Incident Response Flow
- 보안 사고 대응
- Access Review
- Patch Management

---

### [FAQ]

Q. Security Operations RAG 문서는 어떤 질문에 강해야 하는가?

A.
Secret 노출, IAM 권한, 취약점 조치, Public Access, Audit Log, Security Alert, 보안 사고 대응 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
Security Operations, DevSecOps, IAM, Secret, Vulnerability, Audit Log, Security Alert, Incident Response, Container Security, Kubernetes Security 키워드를 반복할 수 있다.

---

# 30. Version Rules

## 30.1 버전 기준

### [개념]

Security Operations 문서는 Modern DevSecOps / Cloud Native Security 기준으로 작성한다.

---

### [핵심]

기준:

- DevSecOps Pipeline
- Secret Scan
- Dependency Scan
- Container Image Scan
- IaC Security Scan
- Kubernetes Security
- IAM Least Privilege
- Security Monitoring
- Audit Logging
- Incident Response
- Zero Trust
- Defense in Depth

---

### [실무]

Legacy 또는 낮은 우선순위:

- 배포 후 수동 보안 점검만 수행
- 장기 Access Key 공유
- 서버에 직접 비밀번호 저장
- 공용 관리자 계정 사용
- Audit Log 없는 운영
- 취약점 Scan 없는 배포
- Secret을 문서 / 메신저로 공유
- 방화벽만으로 보안 충분하다고 판단
- 사고 대응 절차 없는 운영

---

### [FAQ]

Q. Modern Security Operations 기준은 무엇인가?

A.
DevSecOps, Secret 관리, IAM 최소 권한, 취약점 관리, Audit Log, Security Monitoring, Incident Response를 통합하는 것이다.

Q. 방화벽만 있으면 보안 운영이 충분한가?

A.
아니다. IAM, Secret, 취약점, 로그, 알림, 사고 대응, 접근 검토가 함께 필요하다.

---

# 31. Quality Checklist

## 31.1 최종 검수 기준

### [개념]

Security Operations RAG 문서는 Agent가 운영 보안 위험을 식별하고 사고 대응을 지원할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Security Operations Scope 충족
- CI/CD Domain Rules와 연결
- Docker Advanced Domain Rules와 연결
- Infrastructure as Code Domain Rules와 연결
- Deployment Strategy Domain Rules와 연결
- Monitoring & Logging Domain Rules와 연결
- Kubernetes Domain Rules와 연결
- FAQ 포함
- Retrieval Queries 포함
- IAM / Least Privilege 포함
- Secret Management / Rotation 포함
- Vulnerability Management 포함
- Container / Kubernetes Security 포함
- IaC / CI/CD Security 포함
- Audit Logging / Security Monitoring 포함
- Incident Response 포함
- Troubleshooting 포함
- Secret Hardcoding 금지 강조
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

Q. Security Operations 문서 품질은 무엇으로 판단하는가?

A.
Agent가 Secret, IAM, 취약점, Audit Log, Security Alert, Incident Response를 검토하고 대응할 수 있으면 품질이 높다.

---

# 32. Final Goal

## 32.1 최종 목표

### [개념]

Security Operations RAG 문서는 단순 보안 체크리스트가 아니다.

DevOps Agent / Backend Agent / Review Agent가 운영 환경의 보안 위험을 탐지, 검토, 대응, 복구, 개선하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Security Operations Workflow
- Review IAM and Least Privilege
- Detect Secret Hardcoding
- Plan Credential Rotation
- Review Vulnerability Risk
- Review Container Security
- Review Kubernetes Security
- Review IaC / CI/CD Security
- Define Audit Logging
- Define Security Alert
- Support Security Incident Response
- Connect Security with Monitoring / Deployment / DevOps

---

### [실무]

최종 연결 흐름:

```text
Application / Infrastructure
→ IAM / Secret / Network / Runtime
→ Security Monitoring
→ Security Alert
→ Incident Response
→ Recovery
→ Post-Incident Improvement
```

---

### [FAQ]

Q. Security Operations 문서의 최종 목적은?

A.
Agent가 운영 보안 위험을 탐지하고, 취약점을 검토하며, 보안 사고 발생 시 대응과 복구를 지원하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Security Operations Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 운영 보안, IAM, Secret, 취약점, Audit Log, Security Alert, 사고 대응을 수행하기 위한 RAG 작성 규칙이다.

Q. Security Operations 문서의 핵심 범위는?
A. DevSecOps, IAM, Secret Management, Vulnerability Management, Container Security, Kubernetes Security, IaC Security, CI/CD Security, Audit Logging, Incident Response이다.

Q. Security Operations와 Spring Security 문서는 어떻게 다른가?
A. Spring Security는 애플리케이션 인증 / 인가 구현 중심이고 Security Operations는 운영 보안, Secret, IAM, 취약점, 감사 로그, 사고 대응 중심이다.

Q. DevSecOps는 무엇인가?
A. 개발과 운영 Pipeline에 보안 검증을 통합하여 보안 문제를 조기에 발견하고 자동으로 관리하는 방식이다.

Q. Shift Left Security는 무엇인가?
A. 보안 검토를 운영 직전이 아니라 개발 초기와 CI/CD 단계로 앞당기는 접근이다.

Q. Least Privilege는 무엇인가?
A. 작업에 필요한 최소한의 권한만 부여하는 보안 원칙이다.

Q. IAM에서 가장 위험한 패턴은?
A. 전체 권한 부여, 오래된 Access Key, MFA 미적용, 사용하지 않는 권한 방치이다.

Q. CI/CD에 Admin 권한을 줘도 되는가?
A. 권장하지 않는다. 배포에 필요한 최소 권한만 부여하고 환경별 권한을 분리해야 한다.

Q. Secret Hardcoding이 위험한 이유는?
A. Git, Docker Image, Log, CI/CD Artifact, Terraform State를 통해 Credential이 노출될 수 있기 때문이다.

Q. Secret이 노출되면 어떻게 해야 하는가?
A. 즉시 Secret을 폐기하고 재발급하며 사용 이력을 확인하고 노출 경로를 제거해야 한다.

Q. Credential Rotation은 언제 필요한가?
A. 정기 보안 정책, 담당자 변경, 권한 변경, Secret 노출 의심, 외부 연동 변경 시 필요하다.

Q. Vulnerability Management는 무엇인가?
A. 취약점을 탐지하고 위험도에 따라 패치, 완화, 추적, 승인하는 운영 보안 활동이다.

Q. CVSS 점수만 보고 우선순위를 정하면 되는가?
A. 아니다. 실제 사용 여부, 외부 노출 여부, Exploit 가능성, 서비스 중요도를 함께 봐야 한다.

Q. Dependency Scan은 왜 필요한가?
A. 사용 중인 라이브러리와 하위 의존성의 알려진 취약점을 조기에 발견하기 위해 필요하다.

Q. Container를 root로 실행하면 왜 위험한가?
A. Container 탈출이나 권한 상승 사고 시 피해 범위가 커질 수 있기 때문이다.

Q. Docker Socket Mount가 위험한 이유는?
A. Container 내부에서 Host Docker Daemon을 제어할 수 있어 Host 장악 위험이 생긴다.

Q. Kubernetes RBAC에서 가장 위험한 실수는?
A. 불필요한 cluster-admin 권한 부여와 Default Service Account에 과도한 권한을 주는 것이다.

Q. Kubernetes Secret은 완전히 안전한가?
A. 아니다. 접근 권한, 암호화, Secret Store 연계를 함께 고려해야 한다.

Q. IaC Security Scan은 왜 필요한가?
A. 위험한 인프라 설정이 운영에 반영되기 전에 자동으로 탐지하기 위해 필요하다.

Q. CI/CD Security에서 가장 중요한 것은?
A. Secret 보호, Runner 권한 제한, Branch Protection, 배포 승인, Artifact 무결성이다.

Q. Network Security에서 가장 흔한 위험은?
A. 관리자 포트, DB 포트, 내부 API가 Public Internet에 노출되는 것이다.

Q. `0.0.0.0/0`은 항상 나쁜가?
A. HTTP / HTTPS 공개 서비스에는 필요할 수 있다. 하지만 SSH, DB, 관리자 포트에는 매우 위험하다.

Q. Audit Log는 왜 필요한가?
A. 보안 사고와 운영 사고 발생 시 누가 어떤 작업을 했는지 추적하고 책임 경로를 확인하기 위해 필요하다.

Q. Security Monitoring은 일반 Monitoring과 무엇이 다른가?
A. 일반 Monitoring은 성능과 장애 중심이고 Security Monitoring은 권한, 접근, 이상 행위, 침해 징후 탐지 중심이다.

Q. Security Alert의 좋은 기준은?
A. 위험도가 명확하고 조치 방법이 있으며 담당자와 Escalation 경로가 정의되어 있어야 한다.

Q. 보안 사고 대응에서 가장 먼저 할 일은?
A. 영향 범위를 확인하고 피해 확산을 막기 위해 계정, Secret, 네트워크, 리소스를 격리해야 한다.

Q. 보안 사고에서 증거 보존이 중요한 이유는?
A. 침해 경로, 피해 범위, 재발 방지책을 분석하기 위해 로그와 상태 정보가 필요하기 때문이다.

Q. Git에 API Key를 올렸는데 삭제 Commit만 하면 충분한가?
A. 아니다. Git History에 남을 수 있으므로 해당 Key를 즉시 폐기하고 재발급해야 한다.

Q. Backup이 있으면 복구가 보장되는가?
A. 아니다. Restore Test를 통해 실제 복구 가능성을 검증해야 한다.

Q. Compliance에서 Evidence가 중요한 이유는?
A. 보안 통제가 실제로 수행되었음을 증명하기 위해 필요하다.

Q. Patch Management는 왜 필요한가?
A. 알려진 취약점이 공격에 악용되기 전에 시스템을 업데이트하기 위해 필요하다.

Q. Access Review는 왜 필요한가?
A. 시간에 따라 누적된 불필요하거나 과도한 권한을 제거하여 침해 위험을 줄이기 위해 필요하다.

Q. Permission Creep은 무엇인가?
A. 업무 변경이나 임시 권한 부여 후 권한이 회수되지 않고 계속 누적되는 현상이다.

Q. Security Runbook은 왜 필요한가?
A. 보안 사고 발생 시 혼란을 줄이고 빠르게 일관된 대응을 하기 위해 필요하다.

Q. Secret Leak 대응 첫 단계는?
A. 노출된 Secret을 즉시 폐기하고 새 Secret을 발급하는 것이다.

Q. Security Operations Review에서 가장 먼저 확인할 것은?
A. Secret 노출, IAM 과다 권한, Public Access, Audit Log, 취약점 Scan, Incident Runbook을 먼저 확인한다.

Q. Security Operations와 Monitoring & Logging은 어떻게 연결되는가?
A. Security Monitoring, Audit Log, Security Alert, Incident Detection에서 연결된다.

Q. Security Operations와 IaC는 어떻게 연결되는가?
A. IaC 코드에서 Public Access, IAM 과다 권한, Secret Hardcoding, State 노출을 검토하는 단계에서 연결된다.

Q. Security Operations와 CI/CD는 어떻게 연결되는가?
A. Secret Scan, 취약점 Scan, Security Gate, 배포 승인, Artifact 검증에서 연결된다.

Q. Modern Security Operations 기준은 무엇인가?
A. DevSecOps, Secret 관리, IAM 최소 권한, 취약점 관리, Audit Log, Security Monitoring, Incident Response를 통합하는 것이다.

Q. Security Operations 문서의 최종 목적은?
A. Agent가 운영 보안 위험을 탐지하고, 취약점을 검토하며, 보안 사고 발생 시 대응과 복구를 지원하게 만드는 것이다.
