# Cloud Provider Domain Rules

---

# 1. Domain Purpose

## 1.1 Cloud Provider 문서 목적

### [개념]

Cloud Provider Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Cloud Service Selection Support
- AWS / Cloud Resource Understanding Support
- Home Server + Cloud Hybrid Support
- Cloud Cost Risk Review
- Cloud IAM / Network / Storage Review
- Backup Storage Support
- Cloud Deployment Support
- Cloud Troubleshooting Support

우선순위:

1. Cloud Provider Core
2. AWS Foundation
3. IAM / Network / Storage
4. Home Server Hybrid
5. Cost / Security / Troubleshooting

---

### [핵심]

Cloud Provider 문서는 모든 클라우드 서비스를 깊게 설명하는 백과사전이 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- Cloud Provider 기본 개념 설명
- AWS 핵심 서비스 구분
- Home Server와 Cloud 연계 설계
- DNS / Domain / CDN / Object Storage 이해
- IAM 권한 위험 검토
- Cloud Network 구조 검토
- Cloud Backup Storage 설계
- Cloud 비용 위험 탐지
- CI/CD / IaC / Kubernetes / Monitoring 문서와 연계
- 수업 / 학습 / 실무 프로젝트용 AWS 기본 흐름 지원

---

### [실무]

2026 개인 홈서버 + 학습 프로젝트 기준 Cloud Provider 문서는 다음 흐름을 기준으로 작성한다.

```text
Home Server
→ Domain / DNS
→ Tunnel / Reverse Proxy
→ Cloud Storage Backup
→ CI/CD Integration
→ Optional Cloud VM
→ Monitoring / Security Review
```

Cloud Provider 문서는 홈서버를 대체하는 문서가 아니라, 홈서버의 외부 접속, 백업, 배포, 보안, 장애 대응을 보완하는 문서이다.

---

### [FAQ]

Q. Cloud Provider 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 AWS 같은 Cloud Provider를 이해하고 홈서버 또는 프로젝트 배포와 연계하기 위한 RAG 문서이다.

Q. 홈서버 개인 프로젝트에도 Cloud Provider 문서가 필요한가?

A.
필수는 아니지만 DNS, 백업 저장소, CI/CD, 외부 접속, 임시 서버, 보안 학습에 유용하다.

Q. Cloud Provider 문서는 AWS 전체 서비스 설명서인가?

A.
아니다. 홈서버와 DevOps Agent에 필요한 Compute, Storage, Network, IAM, DNS, Backup, Cost, Security 중심 문서이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Cloud Provider Domain 문서는 Cloud 기반 리소스의 기본 개념과 홈서버 / DevOps 연계에 필요한 핵심 서비스를 다룬다.

포함 범위:

- Cloud Provider
- AWS
- Region
- Availability Zone
- IAM
- VPC
- Subnet
- Security Group
- EC2
- Lightsail
- S3
- EBS
- RDS
- Route 53
- CloudFront
- ACM
- Load Balancer
- CloudWatch
- CloudTrail
- ECR
- Backup Storage
- Cloud Cost
- Free Tier
- Billing Alert
- Home Server Hybrid
- CI/CD Integration
- IaC Integration
- Security Review
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Cloud Provider
- AWS
- Region
- Availability Zone
- IAM
- VPC
- Security Group
- EC2
- Lightsail
- S3
- RDS
- Route 53
- CloudFront
- CloudWatch
- CloudTrail
- ECR
- Cost
- Billing
- Home Server
- Hybrid Cloud

---

### [실무]

Cloud Provider 문서는 아래 상황을 해결할 수 있어야 한다.

- AWS 수업 내용을 DevOps 문서와 연결
- 홈서버 외부 접속 구조 이해
- 도메인 / DNS / HTTPS 구조 이해
- S3 기반 백업 저장소 설계
- EC2 / Lightsail 기반 임시 서버 이해
- Security Group 포트 개방 위험 검토
- IAM Access Key 노출 위험 검토
- CI/CD에서 Cloud 배포 권한 검토
- Docker Image를 ECR에 Push하는 흐름 이해
- CloudWatch / CloudTrail로 관측과 감사 로그 이해
- Cloud 비용 폭증 위험 탐지

---

### [FAQ]

Q. Cloud Provider 문서에서 AWS만 다뤄도 되는가?

A.
AWS를 중심으로 작성해도 된다. 단, Cloud Provider 공통 개념인 IAM, Region, Network, Storage, Billing은 일반화해서 작성한다.

Q. GCP나 Azure도 포함해야 하는가?

A.
우선순위는 낮다. 개인 프로젝트와 수업에서 AWS를 사용한다면 AWS 중심으로 작성하고, 공통 개념만 Cloud Provider 관점으로 확장한다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Cloud Provider 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

Cloud Provider 문서는 검색 친화적인 클라우드 리소스 구조를 우선한다.

```text
Cloud Need
→ Service Selection
→ IAM
→ Network
→ Storage
→ Deployment
→ Monitoring
→ Cost Review
```

---

### [실무]

권장 Part 구성:

- Cloud_Provider_Part01_Core.md
- Cloud_Provider_Part02_AWS_Foundation.md
- Cloud_Provider_Part03_IAM_Security.md
- Cloud_Provider_Part04_Network_DNS_TLS.md
- Cloud_Provider_Part05_Compute_Storage_Database.md
- Cloud_Provider_Part06_Backup_Home_Server_Hybrid.md
- Cloud_Provider_Part07_CI_CD_IaC_Integration.md
- Cloud_Provider_Part08_Monitoring_Audit_Cost.md
- Cloud_Provider_Part09_Troubleshooting.md

---

### [FAQ]

Q. Cloud Provider 문서에 FAQ가 필요한가?

A.
필수이다. Cloud 질문은 “EC2와 Lightsail 차이”, “S3 백업”, “Security Group 포트”, “비용 폭증”, “IAM Key 노출”처럼 문제 상황 중심으로 들어온다.

Q. Cloud Provider 문서는 어느 정도 깊이로 작성해야 하는가?

A.
홈서버와 DevOps Agent 기준으로 필요한 서비스 선택, 보안, 비용, 연계 흐름을 우선하고 전문 서비스 세부 튜닝은 별도 문서로 분리한다.

---

# 4. Cloud Provider Core Rules

## 4.1 Cloud Provider Core 작성 규칙

### [개념]

Cloud Provider는 서버, 저장소, 네트워크, 데이터베이스, 보안, 모니터링 같은 IT 인프라를 인터넷 기반 서비스로 제공하는 플랫폼이다.

대표 Cloud Provider:

- AWS
- Google Cloud
- Microsoft Azure
- Oracle Cloud
- Naver Cloud
- Cloudflare

---

### [핵심]

Cloud Provider 핵심 구성:

- Compute
- Storage
- Database
- Network
- IAM
- Monitoring
- Security
- Billing

기본 흐름:

```text
User Requirement
→ Cloud Service Selection
→ Resource Provisioning
→ Access Control
→ Deployment
→ Monitoring
→ Cost Review
```

---

### [실무]

홈서버 프로젝트에서 Cloud Provider는 다음 용도로 사용한다.

- 도메인 연결
- DNS 관리
- HTTPS 인증서
- Object Storage 백업
- CI/CD 배포 연계
- Container Registry
- 외부 접속 보조
- 장애 시 임시 서버
- 보안 로그 / 감사 로그
- 비용 학습

---

### [FAQ]

Q. Cloud Provider는 무엇인가?

A.
서버, 저장소, 네트워크, 데이터베이스, 보안, 모니터링을 인터넷 기반 서비스로 제공하는 플랫폼이다.

Q. 홈서버가 있으면 Cloud Provider가 필요 없는가?

A.
항상 필요한 것은 아니다. 하지만 DNS, 백업, 외부 접속, CI/CD, 임시 서버, 학습 목적에는 유용하다.

---

# 5. AWS Foundation Rules

## 5.1 AWS Foundation 작성 규칙

### [개념]

AWS는 Compute, Storage, Database, Network, Security, Monitoring 등 다양한 Cloud Service를 제공하는 Cloud Provider이다.

AWS 문서는 수업 / 학습 / 프로젝트 기준으로 핵심 서비스 중심으로 작성한다.

---

### [핵심]

AWS 기초 서비스 매핑:

| 영역        | AWS 서비스                  | 역할                      |
| ----------- | --------------------------- | ------------------------- |
| Compute     | EC2, Lightsail              | 서버 실행                 |
| Storage     | S3, EBS                     | 파일 / 블록 저장소        |
| Database    | RDS                         | 관리형 DB                 |
| Network     | VPC, Subnet, Security Group | 네트워크 격리 / 접근 제어 |
| DNS         | Route 53                    | 도메인 / DNS 관리         |
| CDN         | CloudFront                  | 정적 파일 / CDN           |
| Certificate | ACM                         | TLS 인증서                |
| Registry    | ECR                         | Docker Image 저장소       |
| Monitoring  | CloudWatch                  | 지표 / 로그 / 알림        |
| Audit       | CloudTrail                  | API 호출 감사 로그        |
| IAM         | IAM User, Role, Policy      | 권한 관리                 |

---

### [실무]

AWS 학습 순서 추천:

```text
IAM
→ Region / AZ
→ VPC / Security Group
→ EC2 or Lightsail
→ S3
→ RDS
→ Route 53 / ACM
→ CloudWatch / CloudTrail
→ ECR
→ CI/CD / IaC
```

홈서버 연계 우선순위:

```text
S3 Backup
→ DNS / Domain
→ HTTPS
→ ECR or GitHub Registry
→ CloudWatch / Billing Alert
→ EC2 / Lightsail Backup Server
```

---

### [FAQ]

Q. AWS에서 가장 먼저 이해해야 하는 것은?

A.
IAM, Region, VPC, Security Group, EC2, S3, RDS, Billing을 먼저 이해하는 것이 좋다.

Q. AWS 수업을 홈서버 프로젝트에 어떻게 연결할 수 있는가?

A.
S3 백업, DNS, HTTPS, CI/CD, Docker Registry, 임시 EC2 서버, 비용 알림으로 연결할 수 있다.

---

# 6. Region / Availability Zone Rules

## 6.1 Region / AZ 작성 규칙

### [개념]

Region은 Cloud Provider의 지리적 리소스 위치이다.

Availability Zone은 하나의 Region 안에 있는 독립적인 데이터센터 단위이다.

---

### [핵심]

필수 포함:

- Region
- Availability Zone
- Latency
- Fault Isolation
- Data Residency
- Multi-AZ
- Cost Difference

기본 구조:

```text
Region
→ Availability Zone A
→ Availability Zone B
→ Availability Zone C
```

---

### [실무]

Region 선택 기준:

- 사용자와 가까운 위치
- 서비스 제공 여부
- 비용
- 법적 / 데이터 위치 요구사항
- 장애 대응 필요성
- 수업 / 실습 환경 기준

한국 사용자 기준 예시:

```text
ap-northeast-2
→ Seoul Region
```

---

### [주의]

Region을 잘못 선택하면 Latency와 비용이 증가할 수 있다.

리소스는 기본적으로 Region 단위로 분리된다.

---

### [FAQ]

Q. Region은 무엇인가?

A.
Cloud 리소스가 위치하는 지리적 영역이다.

Q. Availability Zone은 무엇인가?

A.
Region 안에 있는 독립적인 데이터센터 단위이며 장애 격리에 사용된다.

Q. Region 선택 기준은 무엇인가?

A.
사용자 위치, 지연 시간, 비용, 서비스 지원 여부, 데이터 위치 요구사항을 기준으로 선택한다.

---

# 7. IAM Rules

## 7.1 Cloud IAM 작성 규칙

### [개념]

IAM은 Cloud Resource에 누가 어떤 권한으로 접근할 수 있는지 제어하는 권한 관리 체계이다.

---

### [핵심]

필수 포함:

- IAM User
- IAM Group
- IAM Role
- IAM Policy
- Permission
- Least Privilege
- MFA
- Access Key
- Temporary Credential

---

### [실무]

IAM Review 기준:

- Root Account 사용 최소화
- MFA 활성화
- IAM User 대신 Role 우선 검토
- Access Key 장기 사용 주의
- Admin 권한 남용 금지
- CI/CD용 권한 분리
- 서비스별 최소 권한 적용
- 사용하지 않는 User / Key 삭제
- 권한 변경 Audit Log 확인

나쁜 권한 예시:

```json
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
```

권장 흐름:

```text
Task
→ Required Resource
→ Required Action
→ Least Privilege Policy
→ Review
```

---

### [주의]

Access Key는 유출되면 Cloud Resource 비용 폭증, 데이터 유출, 인프라 삭제로 이어질 수 있다.

가능하면 임시 자격 증명, Role, OIDC Federation을 사용한다.

---

### [FAQ]

Q. Cloud IAM은 무엇인가?

A.
Cloud Resource에 대한 사용자, 서비스, 시스템의 접근 권한을 관리하는 체계이다.

Q. Root Account를 평소에 사용해도 되는가?

A.
권장하지 않는다. Root Account는 초기 설정과 긴급 작업에만 사용하고 MFA를 반드시 적용해야 한다.

Q. Access Key가 노출되면 어떻게 해야 하는가?

A.
즉시 비활성화하거나 삭제하고 새 Key를 발급하며 사용 이력과 비정상 리소스 생성을 확인해야 한다.

---

# 8. Cloud Network Rules

## 8.1 Cloud Network 작성 규칙

### [개념]

Cloud Network는 Cloud Resource가 서로 통신하고 외부 인터넷과 연결되는 구조이다.

AWS 기준 핵심 구성은 VPC, Subnet, Route Table, Internet Gateway, NAT Gateway, Security Group이다.

---

### [핵심]

필수 포함:

- VPC
- Subnet
- Public Subnet
- Private Subnet
- Route Table
- Internet Gateway
- NAT Gateway
- Security Group
- Network ACL
- Ingress
- Egress

---

### [Flow]

```text
Internet
→ Load Balancer / Public Subnet
→ Application Server
→ Private Database
```

---

### [실무]

기본 네트워크 분리:

```text
Public Subnet
- Load Balancer
- Bastion Host
- Public Web Server

Private Subnet
- Application Server
- Database
- Cache
- Internal Service
```

홈서버 연계에서는 복잡한 VPC 설정보다 아래를 우선한다.

- 외부 공개 포트 최소화
- Cloudflare Tunnel 또는 Reverse Proxy 고려
- SSH 직접 공개 주의
- DB 포트 공개 금지
- HTTPS 적용
- Security Group 규칙 명확화

---

### [FAQ]

Q. VPC는 무엇인가?

A.
Cloud 안에서 사용하는 격리된 가상 네트워크이다.

Q. Public Subnet과 Private Subnet 차이는?

A.
Public Subnet은 인터넷 접근 경로가 있고 Private Subnet은 직접 인터넷 노출을 피하는 내부 리소스용 네트워크이다.

Q. Cloud Network에서 가장 흔한 보안 실수는?

A.
SSH, DB, 관리자 포트를 `0.0.0.0/0`으로 공개하는 것이다.

---

# 9. Security Group Rules

## 9.1 Security Group 작성 규칙

### [개념]

Security Group은 Cloud Resource에 대한 Inbound / Outbound 트래픽을 제어하는 가상 방화벽이다.

---

### [핵심]

필수 포함:

- Security Group
- Inbound Rule
- Outbound Rule
- Port
- Protocol
- Source
- Destination
- Least Exposure

---

### [실무]

Security Group Review 기준:

- SSH 22번 포트 전체 공개 금지
- DB 3306 / 5432 전체 공개 금지
- 관리자 포트 전체 공개 금지
- HTTP / HTTPS만 필요 시 공개
- 내부 서비스는 내부 Security Group끼리만 허용
- 임시 공개 규칙은 만료일 기록
- 사용하지 않는 규칙 제거

위험 예시:

```text
0.0.0.0/0:22
0.0.0.0/0:3306
0.0.0.0/0:6379
0.0.0.0/0:8080
```

권장 예시:

```text
0.0.0.0/0:443
office-ip/32:22
app-security-group:3306
```

---

### [FAQ]

Q. Security Group은 무엇인가?

A.
Cloud Resource의 네트워크 접근을 제어하는 가상 방화벽이다.

Q. `0.0.0.0/0`은 항상 나쁜가?

A.
HTTP / HTTPS 공개 서비스에는 필요할 수 있다. 하지만 SSH, DB, Redis, 관리자 포트에는 위험하다.

Q. DB 포트를 인터넷에 공개해도 되는가?

A.
권장하지 않는다. DB는 Private Network 또는 제한된 Source에서만 접근 가능해야 한다.

---

# 10. Compute Rules

## 10.1 Cloud Compute 작성 규칙

### [개념]

Cloud Compute는 Cloud에서 서버 또는 실행 환경을 제공하는 서비스이다.

AWS 기준 대표 서비스:

- EC2
- Lightsail
- ECS
- Lambda
- EKS

---

### [핵심]

필수 포함:

- EC2
- Lightsail
- Instance Type
- AMI
- Key Pair
- Security Group
- Public IP
- Elastic IP
- User Data
- Auto Scaling

---

### [실무]

홈서버 / 학습 기준 Compute 선택:

| 서비스    | 적합 상황                         |
| --------- | --------------------------------- |
| EC2       | AWS 기본 서버 학습, 자유로운 설정 |
| Lightsail | 단순 VPS, 초보자 실습             |
| ECS       | Docker Container 운영             |
| EKS       | Kubernetes 운영                   |
| Lambda    | 서버리스 이벤트 처리              |

학습 순서:

```text
Lightsail
→ EC2
→ Docker on EC2
→ ECS or EKS
```

홈서버 보조 용도:

- 임시 배포 서버
- 외부 공개 테스트 서버
- 백업 복구 테스트 서버
- 장애 시 대체 서버
- CI/CD 배포 실습 서버

---

### [FAQ]

Q. EC2는 무엇인가?

A.
AWS에서 가상 서버를 생성하고 운영하는 Compute 서비스이다.

Q. Lightsail과 EC2 차이는?

A.
Lightsail은 단순한 VPS 형태로 초보자에게 쉽고, EC2는 세부 설정과 확장성이 더 높은 서버 서비스이다.

Q. 홈서버가 있는데 EC2가 필요한가?

A.
필수는 아니다. 하지만 배포 실습, 임시 공개 서버, 장애 대응 테스트, AWS 수업 연계에는 유용하다.

---

# 11. Object Storage Rules

## 11.1 Object Storage 작성 규칙

### [개념]

Object Storage는 파일을 객체 단위로 저장하는 Cloud Storage이다.

AWS 기준 대표 서비스는 S3이다.

---

### [핵심]

필수 포함:

- Object Storage
- S3
- Bucket
- Object
- Storage Class
- Versioning
- Lifecycle Rule
- Encryption
- Public Access Block
- Backup

---

### [실무]

S3 사용 사례:

- 홈서버 백업 저장소
- RAG 문서 백업
- DB Dump 백업
- Docker Volume 백업
- 이미지 / 첨부파일 저장
- 정적 웹 파일 저장
- 로그 아카이브
- Terraform State Backend

홈서버 백업 흐름:

```text
Home Server Data
→ Compress / Encrypt
→ Upload to S3
→ Lifecycle Policy
→ Restore Test
```

---

### [주의]

S3 Bucket Public Access는 매우 주의해야 한다.

필수 검토:

- Public Access Block 활성화
- Bucket Policy 검토
- IAM Policy 최소 권한
- Server-side Encryption
- Versioning
- Lifecycle Rule
- 삭제 보호 전략

---

### [FAQ]

Q. S3는 무엇인가?

A.
AWS의 Object Storage 서비스로 파일, 백업, 정적 리소스, 로그 아카이브를 저장하는 데 사용한다.

Q. S3를 홈서버 백업용으로 사용할 수 있는가?

A.
가능하다. RAG 문서, 설정 파일, DB Dump, Docker Volume 백업 저장소로 사용할 수 있다.

Q. S3에서 가장 위험한 실수는?

A.
Bucket을 실수로 Public Access 가능하게 열어 민감 데이터가 노출되는 것이다.

---

# 12. Block Storage Rules

## 12.1 Block Storage 작성 규칙

### [개념]

Block Storage는 서버에 디스크처럼 연결되는 저장소이다.

AWS 기준 대표 서비스는 EBS이다.

---

### [핵심]

필수 포함:

- Block Storage
- EBS
- Volume
- Snapshot
- IOPS
- Encryption
- Attach / Detach
- Backup

---

### [실무]

EBS 사용 사례:

- EC2 OS Disk
- Application Data Disk
- DB Storage
- Snapshot Backup
- 서버 복구용 Volume

Snapshot 활용 흐름:

```text
EBS Volume
→ Snapshot
→ Restore Volume
→ Attach to EC2
```

---

### [주의]

EBS는 EC2와 연결되는 디스크 개념이다.

S3처럼 직접 파일 URL로 접근하는 Object Storage가 아니다.

---

### [FAQ]

Q. EBS는 무엇인가?

A.
EC2에 디스크처럼 연결해서 사용하는 Block Storage 서비스이다.

Q. EBS와 S3 차이는?

A.
EBS는 서버에 붙는 디스크이고 S3는 파일을 객체로 저장하는 Object Storage이다.

---

# 13. Database Service Rules

## 13.1 Cloud Database 작성 규칙

### [개념]

Cloud Database는 Cloud Provider가 관리하는 데이터베이스 서비스이다.

AWS 기준 대표 서비스는 RDS이다.

---

### [핵심]

필수 포함:

- RDS
- Managed Database
- Engine
- Backup
- Snapshot
- Multi-AZ
- Read Replica
- Security Group
- Parameter Group
- Maintenance Window

---

### [실무]

RDS 사용 사례:

- MySQL 운영
- PostgreSQL 운영
- 자동 백업
- Snapshot 기반 복구
- Multi-AZ 장애 대응
- Read Replica 기반 읽기 확장

RDS 기본 검토:

- Public Access 비활성화
- Security Group 제한
- Backup Retention 설정
- Encryption 활성화
- DB 계정 권한 제한
- Monitoring 활성화
- 비용 확인

---

### [주의]

RDS Public Access는 매우 주의해야 한다.

학습용이더라도 DB 포트를 전체 공개하지 않는다.

---

### [FAQ]

Q. RDS는 무엇인가?

A.
AWS에서 제공하는 관리형 관계형 데이터베이스 서비스이다.

Q. RDS와 직접 설치한 MySQL 차이는?

A.
RDS는 백업, 패치, 복구, 모니터링 같은 운영 기능을 Cloud Provider가 관리해준다.

Q. RDS를 Public Access로 열어도 되는가?

A.
권장하지 않는다. 제한된 네트워크와 Security Group으로 접근을 제어해야 한다.

---

# 14. DNS / Domain Rules

## 14.1 DNS / Domain 작성 규칙

### [개념]

DNS는 도메인 이름을 IP 주소나 서비스 주소로 변환하는 시스템이다.

AWS 기준 대표 서비스는 Route 53이다.

---

### [핵심]

필수 포함:

- DNS
- Domain
- Hosted Zone
- A Record
- CNAME
- Alias
- TTL
- Route 53
- External DNS Provider

---

### [실무]

홈서버 외부 접속 DNS 흐름:

```text
Domain
→ DNS Record
→ Home Server Public IP or Tunnel Endpoint
→ Reverse Proxy
→ Service
```

레코드 예시:

| Record | 역할                      |
| ------ | ------------------------- |
| A      | 도메인을 IPv4 주소로 연결 |
| AAAA   | 도메인을 IPv6 주소로 연결 |
| CNAME  | 다른 도메인 이름으로 연결 |
| MX     | 메일 서버 연결            |
| TXT    | 인증 / 검증 값 저장       |

---

### [주의]

집 인터넷은 Public IP가 바뀔 수 있다.

홈서버에서는 다음을 고려한다.

- DDNS
- Cloudflare Tunnel
- Reverse Proxy
- ISP 포트 차단 여부
- 공유기 Port Forwarding
- HTTPS 인증서 갱신

---

### [FAQ]

Q. DNS는 무엇인가?

A.
도메인 이름을 IP 주소나 서비스 주소로 변환하는 시스템이다.

Q. Route 53은 무엇인가?

A.
AWS의 DNS 및 도메인 관리 서비스이다.

Q. 홈서버에서 Public IP가 바뀌면 어떻게 해야 하는가?

A.
DDNS, Cloudflare Tunnel, 자동 DNS 업데이트, 고정 IP 상품 등을 고려할 수 있다.

---

# 15. CDN / TLS Rules

## 15.1 CDN / TLS 작성 규칙

### [개념]

CDN은 정적 콘텐츠를 사용자 가까운 위치에서 제공해 속도와 안정성을 높이는 서비스이다.

TLS는 HTTPS 통신을 암호화하는 보안 기술이다.

AWS 기준 대표 서비스:

- CloudFront
- ACM

---

### [핵심]

필수 포함:

- CDN
- CloudFront
- HTTPS
- TLS
- Certificate
- ACM
- Cache
- Origin
- Edge Location

---

### [실무]

CDN 사용 사례:

- React 정적 파일 배포
- 이미지 / 첨부파일 캐싱
- S3 정적 웹 파일 제공
- API 앞단 캐싱 일부 적용
- 글로벌 사용자 Latency 개선

TLS 적용 흐름:

```text
Domain
→ Certificate
→ HTTPS Endpoint
→ Reverse Proxy / Load Balancer / CDN
→ Application
```

---

### [주의]

Cache 설정을 잘못하면 구버전 Frontend가 계속 제공될 수 있다.

민감 API 응답을 무분별하게 CDN Cache하면 안 된다.

---

### [FAQ]

Q. CDN은 무엇인가?

A.
정적 콘텐츠를 사용자 가까운 위치에서 제공하여 속도와 안정성을 높이는 서비스이다.

Q. TLS 인증서는 왜 필요한가?

A.
HTTPS 통신을 암호화하고 사용자와 서버 간 데이터 보호를 위해 필요하다.

Q. CloudFront와 ACM은 어떻게 연결되는가?

A.
CloudFront는 CDN이고 ACM은 HTTPS 인증서를 관리하는 서비스이다.

---

# 16. Container Registry Rules

## 16.1 Cloud Container Registry 작성 규칙

### [개념]

Container Registry는 Docker Image를 저장하고 배포 서버나 Kubernetes가 Pull할 수 있도록 제공하는 저장소이다.

AWS 기준 대표 서비스는 ECR이다.

---

### [핵심]

필수 포함:

- Container Registry
- ECR
- Docker Image
- Image Tag
- Push
- Pull
- Registry Login
- Image Scan
- Lifecycle Policy

---

### [실무]

ECR 연계 흐름:

```text
Docker Build
→ Image Tag
→ ECR Login
→ Docker Push
→ Server / Kubernetes Pull
```

CI/CD 연계:

```text
GitHub Actions
→ Docker Build
→ ECR Push
→ Deploy
```

Tag 기준:

- Git Commit SHA
- Semantic Version
- Build Number
- Environment Tag

---

### [주의]

`latest` 단독 사용은 Rollback과 추적이 어렵다.

Registry 권한은 Push 권한과 Pull 권한을 분리한다.

---

### [FAQ]

Q. ECR은 무엇인가?

A.
AWS에서 Docker Image를 저장하고 Pull / Push할 수 있는 Container Registry 서비스이다.

Q. Container Registry가 왜 필요한가?

A.
CI/CD에서 빌드한 Docker Image를 저장하고 서버나 Kubernetes에서 동일한 Image를 배포하기 위해 필요하다.

---

# 17. Monitoring / Audit Rules

## 17.1 Cloud Monitoring / Audit 작성 규칙

### [개념]

Cloud Monitoring은 Cloud Resource의 지표와 로그를 관측하는 체계이다.

Cloud Audit은 누가 어떤 Cloud API를 호출했는지 기록하는 감사 체계이다.

AWS 기준 대표 서비스:

- CloudWatch
- CloudTrail

---

### [핵심]

필수 포함:

- CloudWatch
- CloudTrail
- Metrics
- Logs
- Alarm
- Audit Log
- API Call History
- Billing Alarm
- Security Event

---

### [실무]

CloudWatch 사용 사례:

- EC2 CPU / Memory 관측
- RDS 지표 관측
- Application Log 수집
- Alarm 설정
- Billing Alarm
- 배포 후 지표 확인

CloudTrail 사용 사례:

- IAM 변경 추적
- Security Group 변경 추적
- S3 접근 추적
- 리소스 생성 / 삭제 추적
- 비정상 API 호출 분석

---

### [FAQ]

Q. CloudWatch는 무엇인가?

A.
AWS 리소스의 Metrics, Logs, Alarm을 관리하는 모니터링 서비스이다.

Q. CloudTrail은 무엇인가?

A.
AWS 계정에서 발생한 API 호출과 사용자 활동을 기록하는 감사 로그 서비스이다.

Q. CloudWatch와 CloudTrail 차이는?

A.
CloudWatch는 지표와 로그 기반 모니터링이고 CloudTrail은 API 호출 이력과 감사 로그 중심이다.

---

# 18. Home Server Hybrid Rules

## 18.1 Home Server + Cloud Hybrid 작성 규칙

### [개념]

Home Server Hybrid는 개인 홈서버를 중심으로 운영하면서 Cloud Provider를 외부 접속, 백업, DNS, 인증서, 임시 서버, CI/CD 보조 용도로 사용하는 구조이다.

---

### [핵심]

필수 포함:

- Home Server
- Hybrid Cloud
- DNS
- Tunnel
- Reverse Proxy
- Cloud Backup
- Object Storage
- CI/CD
- Failover
- Security

---

### [실무]

홈서버 + 클라우드 추천 구조:

```text
Home Server
→ Docker / AnythingLLM / Ollama / RAG
→ Cloud DNS or Cloudflare
→ HTTPS / Tunnel
→ Cloud Object Storage Backup
→ GitHub Actions CI/CD
→ Optional Cloud VM for Recovery Test
```

사용 사례:

- 홈서버 RAG 문서 S3 백업
- AnythingLLM Storage Volume 백업
- Git Repository와 CI/CD 연계
- 외부 접속용 도메인 연결
- HTTPS 인증서 적용
- 장애 시 Cloud VM에 최소 서비스 복구
- 백업 복구 테스트

---

### [주의]

홈서버 외부 공개 시 보안 위험이 증가한다.

확인:

- 관리자 페이지 공개 여부
- SSH 포트 공개 여부
- 기본 비밀번호 사용 여부
- HTTPS 적용 여부
- 방화벽 설정
- 인증 / 접근 제한
- 로그 모니터링
- 백업 암호화

---

### [FAQ]

Q. Home Server Hybrid는 무엇인가?

A.
개인 홈서버를 주 실행 환경으로 두고 Cloud를 DNS, 백업, 외부 접속, CI/CD, 임시 복구 서버 용도로 보조 사용하는 구조이다.

Q. 홈서버를 인터넷에 직접 공개해도 되는가?

A.
가능하지만 위험하다. HTTPS, 인증, 방화벽, 접근 제한, 로그, 백업을 반드시 고려해야 한다.

Q. 홈서버에서 Cloud를 가장 먼저 쓰기 좋은 용도는?

A.
Object Storage 백업, DNS / 도메인, HTTPS, CI/CD 연계가 우선순위가 높다.

---

# 19. Backup Storage Rules

## 19.1 Cloud Backup Storage 작성 규칙

### [개념]

Cloud Backup Storage는 홈서버 또는 서버의 중요 데이터를 Cloud Object Storage나 Backup Service에 저장하여 데이터 손실에 대비하는 구조이다.

---

### [핵심]

필수 포함:

- Backup
- Object Storage
- S3
- Versioning
- Encryption
- Lifecycle
- Retention
- Restore Test
- Offsite Backup

---

### [실무]

백업 대상:

- RAG 문서
- AnythingLLM Storage
- Docker Volume
- Database Dump
- `.env.example`
- 배포 설정 파일
- Nginx / Reverse Proxy 설정
- Git Repository
- SSH Public Key 목록
- 중요 Markdown 문서

백업 Flow:

```text
Stop or Snapshot
→ Compress
→ Encrypt
→ Upload to Cloud Storage
→ Verify Upload
→ Restore Test
```

---

### [Best Practice]

- 최소 1개 Offsite Backup 유지
- 백업 암호화
- 자동 백업 로그 기록
- 복구 테스트 수행
- 백업 보존 기간 설정
- 백업 접근 권한 제한
- 삭제 방지 / Versioning 고려

---

### [FAQ]

Q. Cloud Backup Storage는 왜 필요한가?

A.
홈서버 디스크 고장, 실수로 인한 삭제, OS 문제, Docker Volume 손실에 대비하기 위해 필요하다.

Q. 백업만 있으면 충분한가?

A.
아니다. Restore Test를 통해 실제 복구 가능한지 확인해야 한다.

---

# 20. CI/CD Integration Rules

## 20.1 Cloud CI/CD 연계 규칙

### [개념]

Cloud CI/CD Integration은 GitHub Actions, Jenkins 같은 Pipeline이 Cloud Resource에 접근하여 Image Push, 배포, 백업, IaC Apply를 수행하는 구조이다.

---

### [핵심]

필수 포함:

- GitHub Actions
- Jenkins
- Cloud Credential
- OIDC Federation
- ECR Push
- S3 Upload
- EC2 Deploy
- Terraform Apply
- Least Privilege

---

### [Flow]

```text
Git Push
→ CI/CD Pipeline
→ Test
→ Docker Build
→ Registry Push
→ Cloud or Home Server Deploy
```

---

### [실무]

Cloud 연계 작업:

- S3 백업 업로드
- ECR Docker Image Push
- EC2 배포
- Terraform Plan / Apply
- CloudFront Cache Invalidation
- CloudWatch 알림 연계
- 배포 승인 기록

보안 기준:

- 장기 Access Key 최소화
- OIDC Federation 사용 검토
- CI/CD Secret 보호
- 환경별 권한 분리
- Production Apply 승인 필요

---

### [FAQ]

Q. CI/CD에서 Cloud 권한은 어떻게 관리해야 하는가?

A.
최소 권한을 적용하고 장기 Access Key보다 OIDC Federation이나 Role 기반 임시 권한을 우선 검토한다.

Q. CI/CD에 Cloud Admin 권한을 줘도 되는가?

A.
권장하지 않는다. 필요한 S3, ECR, EC2, IaC 작업 권한만 분리해서 부여해야 한다.

---

# 21. Infrastructure as Code Integration Rules

## 21.1 Cloud IaC 연계 규칙

### [개념]

Cloud IaC Integration은 AWS 같은 Cloud Resource를 Terraform / OpenTofu 코드로 정의하고 재현 가능하게 관리하는 구조이다.

---

### [핵심]

필수 포함:

- Terraform
- OpenTofu
- Provider
- Resource
- Remote State
- S3 Backend
- IAM
- VPC
- Security Group
- Plan
- Apply

---

### [실무]

Cloud Resource IaC 대상:

- VPC
- Subnet
- Security Group
- EC2
- S3 Bucket
- RDS
- IAM Role
- Route 53 Record
- ECR Repository
- CloudWatch Alarm

IaC 흐름:

```text
Cloud Requirement
→ Terraform Code
→ Plan
→ Review
→ Apply
→ State
→ Monitoring
```

---

### [주의]

IaC로 Cloud Resource를 만들 때 가장 위험한 항목:

- Public Access
- IAM `Action: "*"`
- Security Group `0.0.0.0/0`
- RDS Public Access
- Secret Hardcoding
- State 파일 유출
- Destroy 위험

---

### [FAQ]

Q. Cloud Resource를 IaC로 관리하는 이유는?

A.
Cloud Resource를 코드로 정의하여 변경 이력, 재현성, 리뷰, 자동화를 확보하기 위해 사용한다.

Q. IaC Cloud Review에서 가장 먼저 볼 것은?

A.
IAM 권한, Public Access, Security Group, Secret Hardcoding, State 관리, 삭제 위험을 먼저 확인한다.

---

# 22. Cloud Cost Rules

## 22.1 Cloud Cost 작성 규칙

### [개념]

Cloud Cost 관리는 Cloud Resource 사용량과 요금을 추적하고 예상치 못한 비용 폭증을 막는 운영 기준이다.

---

### [핵심]

필수 포함:

- Billing
- Cost Explorer
- Free Tier
- Budget
- Billing Alert
- Resource Cleanup
- Data Transfer Cost
- Storage Cost
- Idle Resource

---

### [실무]

개인 / 학습 Cloud 비용 관리 기준:

- Free Tier 조건 확인
- Billing Alert 설정
- Budget 설정
- 사용하지 않는 EC2 중지 / 삭제
- Elastic IP 미사용 비용 확인
- NAT Gateway 비용 주의
- RDS 실행 비용 주의
- EBS Volume 방치 확인
- S3 Storage / Request 비용 확인
- CloudWatch Log 보존 기간 설정
- 데이터 전송 비용 확인

---

### [주의]

학습용 Cloud에서 비용 폭증이 자주 발생하는 원인:

- EC2 / RDS 계속 실행
- NAT Gateway 방치
- 큰 Instance 선택
- Log 무제한 저장
- EBS Volume 삭제 누락
- Elastic IP 미연결
- 과도한 데이터 전송
- Auto Scaling 설정 오류

---

### [FAQ]

Q. 개인 AWS 학습에서 가장 먼저 해야 할 비용 설정은?

A.
Budget과 Billing Alert를 설정하고 Free Tier 조건을 확인해야 한다.

Q. AWS 비용이 갑자기 증가하는 흔한 원인은?

A.
EC2 / RDS 방치, NAT Gateway, EBS Volume, Elastic IP, CloudWatch Log, 데이터 전송 비용 때문이다.

Q. 홈서버 사용자는 Cloud 비용이 거의 없지 않은가?

A.
Cloud를 백업, DNS, Object Storage 정도로만 쓰면 낮을 수 있다. 하지만 RDS, EC2, NAT Gateway를 켜두면 비용이 증가할 수 있다.

---

# 23. Security Review Rules

## 23.1 Cloud Security Review 작성 규칙

### [개념]

Cloud Security Review는 Cloud Resource의 접근 권한, 네트워크 노출, 데이터 보호, 감사 로그, 비용 위험을 검토하는 절차이다.

---

### [핵심]

검토 대상:

- IAM 권한
- Root Account MFA
- Access Key 사용
- Security Group
- Public Storage
- Public Database
- Encryption
- Backup
- CloudTrail
- CloudWatch Alarm
- Billing Alert
- CI/CD Credential

---

### [실무]

Cloud Security Checklist:

- Root Account MFA 활성화
- 사용하지 않는 IAM User 제거
- Access Key Rotation
- Admin 권한 최소화
- S3 Public Access Block
- RDS Public Access 비활성화
- Security Group 최소 개방
- DB / Storage 암호화
- CloudTrail 활성화
- Billing Alert 설정
- CI/CD Secret 보호
- Backup 접근 권한 제한

---

### [FAQ]

Q. Cloud Security Review에서 가장 먼저 확인할 것은?

A.
Root Account MFA, IAM 권한, Access Key, Public Access, Security Group, CloudTrail, Billing Alert를 먼저 확인한다.

Q. Cloud에서 Public Access가 위험한 이유는?

A.
Storage, DB, 관리자 포트가 인터넷에 노출되면 데이터 유출과 침해 사고로 이어질 수 있기 때문이다.

---

# 24. Troubleshooting Rules

## 24.1 Cloud Troubleshooting 작성 규칙

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

- Access Denied
- Permission Denied
- EC2 접속 실패
- Security Group Port Blocked
- DNS Not Resolving
- HTTPS Certificate Issue
- S3 Access Denied
- RDS Connection Failed
- ECR Push Failed
- Billing Spike
- CloudWatch Logs Missing
- CloudTrail Missing
- Region Mismatch
- Resource Not Found

---

### [실무]

기본 확인 흐름:

```text
Error Message
→ Region 확인
→ IAM Permission 확인
→ Network 확인
→ Resource Status 확인
→ Log / Audit 확인
→ Cost 확인
```

---

### [Troubleshooting]

문제:
AWS Access Denied가 발생한다.

원인:

- IAM 권한 부족
- 잘못된 Role 사용
- Resource ARN 오류
- SCP / Permission Boundary 제한
- Region 착각

해결:

```text
현재 Principal 확인
→ IAM Policy 확인
→ Resource ARN 확인
→ Region 확인
→ CloudTrail 확인
```

문제:
EC2 SSH 접속이 안 된다.

원인:

- Security Group 22번 Port 미허용
- Key Pair 오류
- Public IP 없음
- OS User 이름 오류
- Network ACL / Route Table 문제

해결:

```text
Public IP 확인
→ Security Group 확인
→ Key Pair 확인
→ OS User 확인
→ Instance Status 확인
```

문제:
S3 Access Denied가 발생한다.

원인:

- IAM 권한 부족
- Bucket Policy 제한
- Public Access Block
- Object Ownership 문제
- KMS 권한 부족

해결:

```text
IAM Policy 확인
→ Bucket Policy 확인
→ Object 권한 확인
→ KMS 권한 확인
→ CloudTrail 확인
```

문제:
AWS 비용이 갑자기 증가했다.

원인:

- EC2 / RDS 실행 방치
- NAT Gateway 비용
- EBS Volume 방치
- CloudWatch Log 증가
- 데이터 전송 비용
- 큰 Instance 사용

해결:

```text
Billing Dashboard 확인
→ Cost Explorer 확인
→ 실행 중 Resource 확인
→ 미사용 Resource 정리
→ Budget Alert 설정
```

---

### [FAQ]

Q. Cloud 문제 해결에서 가장 먼저 확인할 것은?

A.
Region, IAM 권한, Resource 상태, Network 설정, 로그, 비용 정보를 먼저 확인한다.

Q. Resource가 없다고 나오는데 실제로 만든 것 같으면?

A.
Region이 다르거나 Account가 다르거나 Resource 이름 / ID를 잘못 확인했을 가능성이 높다.

Q. Cloud 비용 문제가 생기면 무엇부터 확인해야 하는가?

A.
Billing Dashboard, Cost Explorer, 실행 중인 EC2 / RDS / NAT Gateway / EBS / Log 저장소를 확인한다.

---

# 25. Common Mistakes

## 25.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 Cloud Provider 구성을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- Root Account 평상시 사용
- MFA 미설정
- Access Key Git Commit
- Admin 권한 남용
- Region 착각
- EC2 / RDS 방치
- NAT Gateway 비용 방치
- EBS Volume 삭제 누락
- S3 Bucket Public Access
- RDS Public Access
- Security Group `0.0.0.0/0` 과다 개방
- SSH Port 전체 공개
- DB Port 전체 공개
- CloudTrail 미활성화
- Billing Alert 미설정
- Backup 암호화 누락
- Restore Test 미수행
- `latest` Image Tag 사용
- CI/CD에 Cloud Admin 권한 부여
- Terraform State 유출

---

### [실무]

Review Agent 검토 기준:

```text
Cloud Account
→ IAM
→ Network
→ Compute
→ Storage
→ Database
→ DNS / TLS
→ Monitoring / Audit
→ Cost
→ Backup
```

---

### [FAQ]

Q. Cloud Provider Review에서 가장 먼저 확인할 것은?

A.
IAM, MFA, Access Key, Public Access, Security Group, Billing Alert, CloudTrail, Backup을 먼저 확인한다.

Q. 개인 AWS 학습에서 가장 위험한 실수는?

A.
비용 알림 없이 EC2 / RDS / NAT Gateway를 켜두거나 Access Key를 노출하는 것이다.

---

# 26. File Relationship Rules

## 26.1 다른 Domain Rules와 연계

### [개념]

Cloud Provider Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Docker Advanced, Infrastructure as Code, Deployment Strategy, Monitoring & Logging, Security Operations, Backup / Disaster Recovery와 연결된다.

---

### [핵심]

연계 구조:

```text
Cloud Provider
→ IAM / Network / Storage / Compute
→ IaC
→ CI/CD
→ Deployment
→ Monitoring
→ Security
→ Backup / DR
```

---

### [실무]

파일 간 역할 분리:

| Domain                     | 역할                                                     |
| -------------------------- | -------------------------------------------------------- |
| Cloud Provider             | AWS / Cloud Resource 기본, 홈서버 연계, 비용 / 보안 기준 |
| Infrastructure as Code     | Cloud Resource 코드화, State, Plan / Apply               |
| CI/CD                      | Cloud 배포, ECR Push, S3 Upload, IaC Pipeline            |
| Docker Advanced            | Image Build, Registry, Runtime                           |
| Deployment Strategy        | Cloud Resource에 배포하고 검증 / Rollback                |
| Monitoring & Logging       | CloudWatch, CloudTrail, Metrics, Logs                    |
| Security Operations        | IAM, Secret, Public Access, Audit, Incident              |
| Backup / Disaster Recovery | S3 Backup, Snapshot, Restore, Failover                   |

---

### [FAQ]

Q. Cloud Provider와 IaC는 어떻게 연결되는가?

A.
Cloud Resource를 Terraform / OpenTofu로 정의하고 Plan / Apply를 통해 생성, 변경, 삭제하는 단계에서 연결된다.

Q. Cloud Provider와 홈서버는 어떻게 연결되는가?

A.
DNS, HTTPS, Cloud Storage Backup, CI/CD, 임시 복구 서버, 외부 접속 보조 용도로 연결된다.

Q. Cloud Provider와 Security Operations는 어떻게 연결되는가?

A.
IAM, Access Key, Public Access, Security Group, Audit Log, Security Alert 검토에서 연결된다.

---

# 27. Retrieval Optimization Rules

## 27.1 Retrieval 최적화 규칙

### [개념]

Cloud Provider 문서는 Cloud 문제 상황과 홈서버 연계 질문 검색에 강해야 한다.

사용자 질문은 주로 AWS 수업, EC2 접속, S3 백업, IAM 권한, Security Group, DNS, 비용 폭증, 홈서버 외부 접속 형태로 들어온다.

---

### [핵심]

강조 대상:

- Cloud Provider
- AWS
- Home Server
- Hybrid Cloud
- IAM
- Region
- VPC
- Security Group
- EC2
- Lightsail
- S3
- RDS
- Route 53
- CloudFront
- ACM
- ECR
- CloudWatch
- CloudTrail
- Billing Alert
- Backup Storage

---

### [실무]

반복 허용 키워드:

- AWS 수업
- AWS 학습
- 홈서버 Cloud 연계
- S3 백업
- EC2 접속 실패
- Lightsail VPS
- IAM Access Key
- Security Group 포트
- RDS Public Access
- Route 53 DNS
- CloudFront CDN
- ACM HTTPS
- ECR Docker Image
- CloudWatch Logs
- CloudTrail Audit
- AWS 비용 폭증
- Billing Alert
- Home Server Hybrid

---

### [FAQ]

Q. Cloud Provider RAG 문서는 어떤 질문에 강해야 하는가?

A.
AWS 기초, 홈서버 연계, S3 백업, EC2 / Lightsail, IAM, Security Group, DNS, HTTPS, 비용, 보안 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
AWS, Cloud Provider, IAM, EC2, S3, RDS, Security Group, Route 53, CloudWatch, CloudTrail, Billing, Home Server 키워드를 반복할 수 있다.

---

# 28. Version Rules

## 28.1 버전 기준

### [개념]

Cloud Provider 문서는 Modern Cloud / Home Server Hybrid 기준으로 작성한다.

---

### [핵심]

기준:

- AWS Foundation
- IAM Least Privilege
- Region / AZ 이해
- VPC / Security Group
- Object Storage Backup
- Cloud DNS / TLS
- Container Registry
- Cloud Monitoring / Audit
- Billing Alert
- IaC Integration
- CI/CD Integration
- Home Server Hybrid

---

### [실무]

Legacy 또는 낮은 우선순위:

- FTP 중심 배포
- 서버 수동 복사 배포
- Root Account 평상시 사용
- Access Key 공유
- Public DB 운영
- 비용 알림 없는 실습
- Backup 없는 Cloud 운영
- Console 수동 생성만 의존
- Security Group 전체 개방
- CloudTrail 없는 운영

---

### [FAQ]

Q. Cloud Provider 문서에서 Modern 기준은 무엇인가?

A.
IAM 최소 권한, IaC, CI/CD, Object Storage Backup, Monitoring, Audit, Billing Alert, Home Server Hybrid 연계를 포함하는 것이다.

Q. Console에서 수동으로만 리소스를 만들면 안 되는가?

A.
학습 초기에는 가능하지만 운영과 반복 작업에는 IaC와 변경 이력 관리가 더 안전하다.

---

# 29. Quality Checklist

## 29.1 최종 검수 기준

### [개념]

Cloud Provider RAG 문서는 Agent가 Cloud 기본 구조와 홈서버 연계를 이해하고 위험을 검토할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Cloud Provider Scope 충족
- AWS Foundation 포함
- Home Server Hybrid 포함
- IAM / Security Group / Public Access 포함
- S3 / Backup Storage 포함
- DNS / TLS 포함
- EC2 / Lightsail 포함
- RDS 기본 포함
- CloudWatch / CloudTrail 포함
- Billing Alert / Cost 포함
- CI/CD Domain Rules와 연결
- Docker Advanced Domain Rules와 연결
- Infrastructure as Code Domain Rules와 연결
- Monitoring & Logging Domain Rules와 연결
- Security Operations Domain Rules와 연결
- Backup / Disaster Recovery Domain Rules와 연결
- FAQ 포함
- Retrieval Queries 포함
- Secret Hardcoding 금지 강조
- 비용 폭증 주의 포함
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

Q. Cloud Provider 문서 품질은 무엇으로 판단하는가?

A.
Agent가 AWS 기초, 홈서버 Cloud 연계, IAM / Network / Storage / Cost / Security Review를 수행할 수 있으면 품질이 높다.

---

# 30. Final Goal

## 30.1 최종 목표

### [개념]

Cloud Provider RAG 문서는 단순 AWS 서비스 목록이 아니다.

DevOps Agent / Backend Agent / Review Agent가 Cloud Resource를 이해하고 홈서버와 연결하며 보안, 비용, 백업, 배포 위험을 검토하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Cloud Provider Workflow
- Understand AWS Foundation
- Review IAM / Security Group
- Design Home Server Hybrid Cloud
- Use S3 for Backup Storage
- Understand EC2 / Lightsail / RDS
- Connect DNS / TLS / CDN
- Connect Cloud with CI/CD
- Connect Cloud with IaC
- Review Cloud Cost Risk
- Review Cloud Security Risk
- Troubleshoot Cloud Access / Network / Cost Issues

---

### [실무]

최종 연결 흐름:

```text
Home Server / Application
→ Cloud DNS / TLS
→ Cloud Backup Storage
→ CI/CD / Registry
→ Optional Cloud Compute
→ Monitoring / Audit
→ Cost / Security Review
```

---

### [FAQ]

Q. Cloud Provider 문서의 최종 목적은?

A.
Agent가 AWS 같은 Cloud Provider를 이해하고 홈서버, 백업, DNS, CI/CD, 보안, 비용 관리와 연결할 수 있게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Cloud Provider Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 AWS와 Cloud Resource를 이해하고 홈서버, 백업, DNS, CI/CD, 보안, 비용과 연계하기 위한 RAG 작성 규칙이다.

Q. Cloud Provider 문서의 핵심 범위는?
A. AWS, IAM, Region, VPC, Security Group, EC2, Lightsail, S3, RDS, Route 53, CloudFront, CloudWatch, CloudTrail, Billing, Home Server Hybrid이다.

Q. 홈서버 개인 프로젝트에도 Cloud Provider 문서가 필요한가?
A. 필수는 아니지만 DNS, 백업, 외부 접속, CI/CD, 임시 서버, 보안 학습에 유용하다.

Q. Cloud Provider는 무엇인가?
A. 서버, 저장소, 네트워크, 데이터베이스, 보안, 모니터링을 인터넷 기반 서비스로 제공하는 플랫폼이다.

Q. AWS에서 가장 먼저 이해해야 하는 것은?
A. IAM, Region, VPC, Security Group, EC2, S3, RDS, Billing을 먼저 이해하는 것이 좋다.

Q. AWS 수업을 홈서버 프로젝트에 어떻게 연결할 수 있는가?
A. S3 백업, DNS, HTTPS, CI/CD, Docker Registry, 임시 EC2 서버, 비용 알림으로 연결할 수 있다.

Q. Region은 무엇인가?
A. Cloud 리소스가 위치하는 지리적 영역이다.

Q. Availability Zone은 무엇인가?
A. Region 안에 있는 독립적인 데이터센터 단위이며 장애 격리에 사용된다.

Q. Cloud IAM은 무엇인가?
A. Cloud Resource에 대한 사용자, 서비스, 시스템의 접근 권한을 관리하는 체계이다.

Q. Root Account를 평소에 사용해도 되는가?
A. 권장하지 않는다. Root Account는 초기 설정과 긴급 작업에만 사용하고 MFA를 반드시 적용해야 한다.

Q. Access Key가 노출되면 어떻게 해야 하는가?
A. 즉시 비활성화하거나 삭제하고 새 Key를 발급하며 사용 이력과 비정상 리소스 생성을 확인해야 한다.

Q. VPC는 무엇인가?
A. Cloud 안에서 사용하는 격리된 가상 네트워크이다.

Q. Public Subnet과 Private Subnet 차이는?
A. Public Subnet은 인터넷 접근 경로가 있고 Private Subnet은 직접 인터넷 노출을 피하는 내부 리소스용 네트워크이다.

Q. Security Group은 무엇인가?
A. Cloud Resource의 네트워크 접근을 제어하는 가상 방화벽이다.

Q. `0.0.0.0/0`은 항상 나쁜가?
A. HTTP / HTTPS 공개 서비스에는 필요할 수 있다. 하지만 SSH, DB, Redis, 관리자 포트에는 위험하다.

Q. DB 포트를 인터넷에 공개해도 되는가?
A. 권장하지 않는다. DB는 Private Network 또는 제한된 Source에서만 접근 가능해야 한다.

Q. EC2는 무엇인가?
A. AWS에서 가상 서버를 생성하고 운영하는 Compute 서비스이다.

Q. Lightsail과 EC2 차이는?
A. Lightsail은 단순한 VPS 형태로 초보자에게 쉽고, EC2는 세부 설정과 확장성이 더 높은 서버 서비스이다.

Q. 홈서버가 있는데 EC2가 필요한가?
A. 필수는 아니다. 하지만 배포 실습, 임시 공개 서버, 장애 대응 테스트, AWS 수업 연계에는 유용하다.

Q. S3는 무엇인가?
A. AWS의 Object Storage 서비스로 파일, 백업, 정적 리소스, 로그 아카이브를 저장하는 데 사용한다.

Q. S3를 홈서버 백업용으로 사용할 수 있는가?
A. 가능하다. RAG 문서, 설정 파일, DB Dump, Docker Volume 백업 저장소로 사용할 수 있다.

Q. S3에서 가장 위험한 실수는?
A. Bucket을 실수로 Public Access 가능하게 열어 민감 데이터가 노출되는 것이다.

Q. EBS는 무엇인가?
A. EC2에 디스크처럼 연결해서 사용하는 Block Storage 서비스이다.

Q. EBS와 S3 차이는?
A. EBS는 서버에 붙는 디스크이고 S3는 파일을 객체로 저장하는 Object Storage이다.

Q. RDS는 무엇인가?
A. AWS에서 제공하는 관리형 관계형 데이터베이스 서비스이다.

Q. RDS와 직접 설치한 MySQL 차이는?
A. RDS는 백업, 패치, 복구, 모니터링 같은 운영 기능을 Cloud Provider가 관리해준다.

Q. RDS를 Public Access로 열어도 되는가?
A. 권장하지 않는다. 제한된 네트워크와 Security Group으로 접근을 제어해야 한다.

Q. DNS는 무엇인가?
A. 도메인 이름을 IP 주소나 서비스 주소로 변환하는 시스템이다.

Q. Route 53은 무엇인가?
A. AWS의 DNS 및 도메인 관리 서비스이다.

Q. 홈서버에서 Public IP가 바뀌면 어떻게 해야 하는가?
A. DDNS, Cloudflare Tunnel, 자동 DNS 업데이트, 고정 IP 상품 등을 고려할 수 있다.

Q. CDN은 무엇인가?
A. 정적 콘텐츠를 사용자 가까운 위치에서 제공하여 속도와 안정성을 높이는 서비스이다.

Q. TLS 인증서는 왜 필요한가?
A. HTTPS 통신을 암호화하고 사용자와 서버 간 데이터 보호를 위해 필요하다.

Q. ECR은 무엇인가?
A. AWS에서 Docker Image를 저장하고 Pull / Push할 수 있는 Container Registry 서비스이다.

Q. Container Registry가 왜 필요한가?
A. CI/CD에서 빌드한 Docker Image를 저장하고 서버나 Kubernetes에서 동일한 Image를 배포하기 위해 필요하다.

Q. CloudWatch는 무엇인가?
A. AWS 리소스의 Metrics, Logs, Alarm을 관리하는 모니터링 서비스이다.

Q. CloudTrail은 무엇인가?
A. AWS 계정에서 발생한 API 호출과 사용자 활동을 기록하는 감사 로그 서비스이다.

Q. CloudWatch와 CloudTrail 차이는?
A. CloudWatch는 지표와 로그 기반 모니터링이고 CloudTrail은 API 호출 이력과 감사 로그 중심이다.

Q. Home Server Hybrid는 무엇인가?
A. 개인 홈서버를 주 실행 환경으로 두고 Cloud를 DNS, 백업, 외부 접속, CI/CD, 임시 복구 서버 용도로 보조 사용하는 구조이다.

Q. 홈서버를 인터넷에 직접 공개해도 되는가?
A. 가능하지만 위험하다. HTTPS, 인증, 방화벽, 접근 제한, 로그, 백업을 반드시 고려해야 한다.

Q. Cloud Backup Storage는 왜 필요한가?
A. 홈서버 디스크 고장, 실수로 인한 삭제, OS 문제, Docker Volume 손실에 대비하기 위해 필요하다.

Q. 백업만 있으면 충분한가?
A. 아니다. Restore Test를 통해 실제 복구 가능한지 확인해야 한다.

Q. CI/CD에서 Cloud 권한은 어떻게 관리해야 하는가?
A. 최소 권한을 적용하고 장기 Access Key보다 OIDC Federation이나 Role 기반 임시 권한을 우선 검토한다.

Q. Cloud Resource를 IaC로 관리하는 이유는?
A. Cloud Resource를 코드로 정의하여 변경 이력, 재현성, 리뷰, 자동화를 확보하기 위해 사용한다.

Q. 개인 AWS 학습에서 가장 먼저 해야 할 비용 설정은?
A. Budget과 Billing Alert를 설정하고 Free Tier 조건을 확인해야 한다.

Q. AWS 비용이 갑자기 증가하는 흔한 원인은?
A. EC2 / RDS 방치, NAT Gateway, EBS Volume, Elastic IP, CloudWatch Log, 데이터 전송 비용 때문이다.

Q. Cloud Security Review에서 가장 먼저 확인할 것은?
A. Root Account MFA, IAM 권한, Access Key, Public Access, Security Group, CloudTrail, Billing Alert를 먼저 확인한다.

Q. Cloud 문제 해결에서 가장 먼저 확인할 것은?
A. Region, IAM 권한, Resource 상태, Network 설정, 로그, 비용 정보를 먼저 확인한다.

Q. Resource가 없다고 나오는데 실제로 만든 것 같으면?
A. Region이 다르거나 Account가 다르거나 Resource 이름 / ID를 잘못 확인했을 가능성이 높다.

Q. 개인 AWS 학습에서 가장 위험한 실수는?
A. 비용 알림 없이 EC2 / RDS / NAT Gateway를 켜두거나 Access Key를 노출하는 것이다.

Q. Cloud Provider와 IaC는 어떻게 연결되는가?
A. Cloud Resource를 Terraform / OpenTofu로 정의하고 Plan / Apply를 통해 생성, 변경, 삭제하는 단계에서 연결된다.

Q. Cloud Provider와 홈서버는 어떻게 연결되는가?
A. DNS, HTTPS, Cloud Storage Backup, CI/CD, 임시 복구 서버, 외부 접속 보조 용도로 연결된다.

Q. Cloud Provider와 Security Operations는 어떻게 연결되는가?
A. IAM, Access Key, Public Access, Security Group, Audit Log, Security Alert 검토에서 연결된다.

Q. Cloud Provider 문서의 최종 목적은?
A. Agent가 AWS 같은 Cloud Provider를 이해하고 홈서버, 백업, DNS, CI/CD, 보안, 비용 관리와 연결할 수 있게 만드는 것이다.
