# Infrastructure as Code Domain Rules

---

# 1. Domain Purpose

## 1.1 Infrastructure as Code 문서 목적

### [개념]

Infrastructure as Code Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Infrastructure Provisioning Support
- Environment Reproducibility Support
- Cloud Resource Automation Support
- Terraform / OpenTofu Workflow Support
- IaC Review / Validation Support
- Drift Detection Support
- Infrastructure Change Management Support

우선순위:

1. IaC Core
2. Terraform / OpenTofu Workflow
3. State Management
4. Module Design
5. Security / Review / Troubleshooting

---

### [핵심]

Infrastructure as Code 문서는 서버, 네트워크, 데이터베이스, 클라우드 리소스를 코드로 정의하고 재현 가능하게 관리하기 위한 DevOps Expert 문서이다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- IaC 개념 설명
- Terraform / OpenTofu 구성 작성
- Provider 설정
- Resource 정의
- Variable / Output 설계
- Module 구조 설계
- Remote State 구성 검토
- Plan / Apply Workflow 검토
- Infrastructure Drift 탐지
- Secret Hardcoding 탐지
- CI/CD Pipeline IaC 연계 검토
- Kubernetes / Cloud / Monitoring 문서와 연계

---

### [실무]

2026 실무 기준 IaC 문서는 다음 흐름을 기준으로 작성한다.

```text
Requirement
→ IaC Code
→ Format / Validate
→ Plan
→ Review
→ Apply
→ State Update
→ Drift Detection
```

IaC 문서는 수동 인프라 생성보다 코드 기반 변경 관리, 재현성, 검토 가능성, 자동화 가능성을 우선한다.

---

### [FAQ]

Q. Infrastructure as Code 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 인프라를 코드로 설계, 검토, 자동화, 문제 해결하기 위한 RAG 문서이다.

Q. IaC 문서는 단순 Terraform 사용법 문서인가?

A.
아니다. IaC 문서는 인프라 변경 관리, State, Module, 보안, Review, CI/CD 연계까지 포함한다.

Q. IaC 문서는 CI/CD 문서와 어떻게 연결되는가?

A.
CI/CD는 IaC 코드를 검증하고 Plan을 리뷰한 뒤 승인된 변경을 Apply하는 자동화 흐름을 담당한다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Infrastructure as Code Domain 문서는 코드 기반 인프라 정의, 배포, 검증, 운영을 다룬다.

포함 범위:

- Infrastructure as Code
- Declarative Infrastructure
- Terraform
- OpenTofu
- Provider
- Resource
- Data Source
- Variable
- Output
- Local Value
- Module
- State
- Remote State
- Backend
- Workspace
- Plan
- Apply
- Destroy
- Import
- Drift Detection
- Secret Management
- Policy as Code
- CI/CD Integration
- Cloud Resource Provisioning
- AWS / Azure / GCP 기본 연계
- Kubernetes IaC 연계
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Infrastructure as Code
- IaC
- Terraform
- OpenTofu
- Provider
- Resource
- Module
- State
- Remote State
- Backend
- Plan
- Apply
- Drift
- Secret
- Policy as Code
- CI/CD
- Cloud Infrastructure

---

### [실무]

IaC 문서는 아래 상황을 해결할 수 있어야 한다.

- AWS EC2 / VPC / RDS / S3 리소스 코드화
- Kubernetes Cluster 또는 Manifest 관리 연계
- Terraform Provider 설정
- 환경별 Variable 분리
- Module 재사용 구조 설계
- Remote State Locking 구성
- Plan 결과 Review
- Apply 전 변경 영향 분석
- 수동 변경으로 발생한 Drift 탐지
- Secret Hardcoding 제거
- CI/CD에서 Terraform Plan / Apply 자동화
- 운영 인프라 Destroy 방지

---

### [FAQ]

Q. IaC 문서에 Cloud Provider별 세부 서비스를 모두 포함해야 하는가?

A.
아니다. IaC 문서는 Provider, Resource, State, Module, Workflow 중심으로 작성하고 Cloud 서비스별 세부 내용은 Cloud Domain 문서와 연결한다.

Q. IaC 문서에 Kubernetes 내용을 포함해야 하는가?

A.
직접 깊게 포함하지 않는다. Kubernetes 리소스를 IaC로 관리하는 연결 지점만 다룬다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Infrastructure as Code 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

IaC 문서는 검색 친화적인 문제 해결 구조를 우선한다.

```text
Concept
→ Workflow
→ Example
→ State Impact
→ Security Risk
→ Review Point
→ Troubleshooting
→ FAQ
```

---

### [실무]

권장 Part 구성:

- Infrastructure_as_Code_Part01_Core.md
- Infrastructure_as_Code_Part02_Terraform_OpenTofu.md
- Infrastructure_as_Code_Part03_Provider_Resource.md
- Infrastructure_as_Code_Part04_Variable_Output.md
- Infrastructure_as_Code_Part05_State_Backend.md
- Infrastructure_as_Code_Part06_Module_Design.md
- Infrastructure_as_Code_Part07_CI_CD_Integration.md
- Infrastructure_as_Code_Part08_Security_Policy.md
- Infrastructure_as_Code_Part09_Drift_Import_Troubleshooting.md

---

### [FAQ]

Q. IaC 문서에 FAQ가 필요한가?

A.
필수이다. IaC 질문은 State 오류, Plan 결과, Drift, Module 구조, Secret 관리처럼 문제 상황으로 들어오는 경우가 많다.

Q. IaC 문서의 설명은 길어도 되는가?

A.
권장하지 않는다. 짧은 설명, 명확한 Flow, 짧은 코드 예제, Review 기준을 우선한다.

---

# 4. IaC Core Rules

## 4.1 Infrastructure as Code Core 작성 규칙

### [개념]

Infrastructure as Code는 인프라 리소스를 수동으로 생성하지 않고 코드로 정의, 검토, 적용, 추적하는 방식이다.

필수 포함:

- Declarative Infrastructure
- Version Control
- Reproducibility
- Change Review
- Automation
- Drift Detection

---

### [핵심]

IaC 핵심 구조:

```text
Infrastructure Definition
→ Version Control
→ Plan
→ Review
→ Apply
→ State
```

핵심 설명:

- IaC는 인프라를 코드로 선언한다.
- Git으로 변경 이력을 관리한다.
- Plan으로 변경 전 영향을 확인한다.
- Apply로 실제 인프라에 반영한다.
- State로 실제 리소스와 코드의 매핑을 추적한다.

---

### [실무]

수동 인프라 관리와 IaC 차이:

| 구분       | Manual Infrastructure | Infrastructure as Code      |
| ---------- | --------------------- | --------------------------- |
| 생성 방식  | Console / CLI 수동    | Code 기반                   |
| 변경 이력  | 추적 어려움           | Git 추적                    |
| 재현성     | 낮음                  | 높음                        |
| Review     | 어려움                | Pull Request 가능           |
| Drift 탐지 | 어려움                | Plan / Drift Detection 가능 |
| 자동화     | 낮음                  | CI/CD 연계 가능             |

---

### [FAQ]

Q. Infrastructure as Code를 사용하는 이유는?

A.
인프라 변경을 코드로 관리하여 재현성, 검토 가능성, 자동화, 변경 이력 추적을 확보하기 위해 사용한다.

Q. IaC는 서버 설정 자동화와 같은가?

A.
완전히 같지 않다. IaC는 인프라 리소스 생성과 변경 관리가 중심이고, 서버 내부 설정은 Configuration Management 영역과 겹칠 수 있다.

---

# 5. Terraform / OpenTofu Rules

## 5.1 Terraform / OpenTofu 작성 규칙

### [개념]

Terraform과 OpenTofu는 선언형 IaC 도구이다.

인프라의 원하는 상태를 코드로 정의하고 Provider를 통해 Cloud Resource를 생성, 변경, 삭제한다.

---

### [핵심]

필수 포함:

- Terraform
- OpenTofu
- HCL
- Provider
- Resource
- Data Source
- Variable
- Output
- State
- Plan
- Apply

---

### [Flow]

```text
Write HCL
→ terraform init
→ terraform fmt
→ terraform validate
→ terraform plan
→ terraform apply
```

---

### [실무]

기본 명령:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

OpenTofu 사용 시:

```bash
tofu init
tofu fmt
tofu validate
tofu plan
tofu apply
```

---

### [주의]

Terraform과 OpenTofu 문서는 개념적으로 함께 다룰 수 있다.

단, 조직의 표준 도구가 Terraform인지 OpenTofu인지 명확히 구분해야 한다.

---

### [FAQ]

Q. Terraform과 OpenTofu는 무엇을 하는 도구인가?

A.
인프라 리소스를 코드로 선언하고 Provider를 통해 생성, 변경, 삭제하는 IaC 도구이다.

Q. Terraform Plan은 왜 중요한가?

A.
Apply 전에 어떤 리소스가 생성, 변경, 삭제되는지 확인하여 운영 장애를 예방할 수 있기 때문이다.

---

# 6. Provider Rules

## 6.1 Provider 작성 규칙

### [개념]

Provider는 Terraform / OpenTofu가 Cloud, Kubernetes, GitHub, Monitoring Tool 같은 외부 플랫폼과 통신하기 위한 Plugin이다.

---

### [핵심]

필수 포함:

- Provider
- Provider Version
- Required Providers
- Authentication
- Region
- API Permission
- Provider Lock

---

### [실무]

Provider 예시:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
```

Provider 인증은 코드에 직접 넣지 않는다.

권장 방식:

- Environment Variable
- Cloud IAM Role
- CI/CD Secret
- Secret Manager
- Workload Identity

---

### [주의]

금지:

```hcl
provider "aws" {
  access_key = "AKIA..."
  secret_key = "secret"
  region     = "ap-northeast-2"
}
```

Credential Hardcoding은 State, Git, Log, CI/CD Artifact를 통해 노출될 수 있다.

---

### [FAQ]

Q. Provider는 무엇인가?

A.
Terraform / OpenTofu가 AWS, Azure, GCP, Kubernetes 같은 외부 API와 통신하기 위한 Plugin이다.

Q. Provider Version을 고정해야 하는 이유는?

A.
Provider 업데이트로 인한 동작 변경을 방지하고 Plan 결과의 재현성을 높이기 위해 필요하다.

Q. Provider에 Access Key를 직접 쓰면 안 되는 이유는?

A.
Credential이 Git, State, Log에 노출될 수 있으므로 Environment Variable, IAM Role, CI/CD Secret을 사용해야 한다.

---

# 7. Resource Rules

## 7.1 Resource 작성 규칙

### [개념]

Resource는 IaC 코드가 생성하거나 관리할 실제 인프라 객체이다.

예:

- VPC
- Subnet
- Security Group
- EC2
- RDS
- S3 Bucket
- IAM Role
- Kubernetes Namespace
- Kubernetes Deployment

---

### [핵심]

필수 포함:

- Resource Type
- Resource Name
- Argument
- Attribute
- Dependency
- Lifecycle
- Tagging

---

### [실무]

Resource 예시:

```hcl
resource "aws_s3_bucket" "app_logs" {
  bucket = var.log_bucket_name

  tags = {
    Name        = "app-logs"
    Environment = var.environment
  }
}
```

Resource Naming 기준:

```text
resource "provider_resource_type" "logical_name"
```

예:

```hcl
resource "aws_instance" "app_server" {
  ami           = var.ami_id
  instance_type = var.instance_type
}
```

---

### [Best Practice]

- Resource 이름은 역할 중심으로 작성한다.
- Environment Tag를 포함한다.
- Owner / Project / ManagedBy Tag를 포함한다.
- Production Resource에는 삭제 방지 설정을 검토한다.
- Resource 간 암묵적 의존성을 우선 사용하고, 필요한 경우에만 `depends_on`을 사용한다.

---

### [FAQ]

Q. Resource는 무엇인가?

A.
IaC 코드가 생성하거나 관리하는 실제 인프라 객체이다.

Q. Resource 이름은 실제 Cloud 리소스 이름인가?

A.
아니다. Terraform 내부 Logical Name이다. 실제 이름은 Resource Argument에서 별도로 지정하는 경우가 많다.

Q. depends_on은 언제 사용하는가?

A.
명시적 의존성이 필요하지만 Terraform이 자동으로 추론하지 못하는 경우에만 사용한다.

---

# 8. Data Source Rules

## 8.1 Data Source 작성 규칙

### [개념]

Data Source는 IaC가 직접 생성하지 않는 기존 리소스나 외부 정보를 조회하기 위한 구성이다.

---

### [핵심]

필수 포함:

- Data Source
- Existing Resource Lookup
- Read-only Reference
- External Dependency
- AMI Lookup
- VPC Lookup

---

### [실무]

Data Source 예시:

```hcl
data "aws_vpc" "default" {
  default = true
}

data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*"]
  }
}
```

---

### [주의]

Data Source는 조회 대상이 변경되면 Plan 결과가 달라질 수 있다.

주의 대상:

- most_recent
- latest
- default
- 외부 Resource 이름 변경
- 권한 부족

---

### [FAQ]

Q. Data Source는 Resource와 무엇이 다른가?

A.
Resource는 IaC가 생성 / 관리하는 대상이고, Data Source는 기존 리소스나 외부 정보를 조회하는 읽기 전용 참조이다.

Q. most_recent 사용 시 주의할 점은?

A.
새 이미지가 나오면 Plan 결과가 바뀔 수 있어 운영 환경에서는 버전 고정 또는 검증 절차가 필요하다.

---

# 9. Variable Rules

## 9.1 Variable 작성 규칙

### [개념]

Variable은 IaC 코드에서 환경별로 달라지는 값을 외부에서 주입하기 위한 입력값이다.

---

### [핵심]

필수 포함:

- variable
- type
- default
- description
- validation
- sensitive
- tfvars
- environment separation

---

### [실무]

Variable 예시:

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging, or prod."
  }
}
```

민감 값 예시:

```hcl
variable "db_password" {
  type        = string
  description = "Database password"
  sensitive   = true
}
```

환경별 파일 예시:

```text
dev.tfvars
staging.tfvars
prod.tfvars
```

실행 예시:

```bash
terraform plan -var-file="prod.tfvars"
```

---

### [주의]

`sensitive = true`는 출력 노출을 줄이지만 Secret 저장 자체를 완전히 안전하게 만들지는 않는다.

Secret은 State에 남을 수 있으므로 Secret Manager 연계를 우선 검토한다.

---

### [FAQ]

Q. Variable은 왜 사용하는가?

A.
환경별 설정값을 코드에서 분리하고 재사용성을 높이기 위해 사용한다.

Q. tfvars 파일은 Git에 올려도 되는가?

A.
민감 정보가 포함된 tfvars는 Git에 올리면 안 된다. 예시 파일만 관리하고 실제 값은 Secret 관리 체계로 분리한다.

Q. sensitive 옵션을 쓰면 Secret이 안전한가?

A.
완전히 안전하지 않다. CLI 출력은 숨길 수 있지만 State에는 값이 남을 수 있다.

---

# 10. Output Rules

## 10.1 Output 작성 규칙

### [개념]

Output은 IaC 적용 후 생성된 리소스의 값을 외부로 노출하거나 다른 Module에서 참조하기 위한 출력값이다.

---

### [핵심]

필수 포함:

- output
- resource attribute
- module output
- sensitive output
- dependency reference

---

### [실무]

Output 예시:

```hcl
output "app_server_public_ip" {
  value       = aws_instance.app_server.public_ip
  description = "Public IP of app server"
}
```

민감 Output 예시:

```hcl
output "db_password" {
  value     = var.db_password
  sensitive = true
}
```

---

### [주의]

Output은 CLI, CI/CD Log, Remote State 참조를 통해 노출될 수 있다.

민감 정보는 Output으로 내보내지 않는 것을 우선한다.

---

### [FAQ]

Q. Output은 언제 사용하는가?

A.
생성된 리소스의 ID, DNS, Endpoint, IP, ARN 같은 값을 확인하거나 다른 Module에서 참조할 때 사용한다.

Q. Secret을 Output으로 출력해도 되는가?

A.
권장하지 않는다. 꼭 필요한 경우 `sensitive = true`를 적용하지만 Secret Manager 사용을 우선한다.

---

# 11. Local Value Rules

## 11.1 Local Value 작성 규칙

### [개념]

Local Value는 IaC 코드 내부에서 반복되는 표현식이나 공통 값을 재사용하기 위한 내부 변수이다.

---

### [핵심]

필수 포함:

- locals
- computed value
- naming convention
- tag merge
- duplication reduction

---

### [실무]

Local Value 예시:

```hcl
locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
```

Resource 적용 예시:

```hcl
resource "aws_s3_bucket" "app_logs" {
  bucket = var.log_bucket_name

  tags = local.common_tags
}
```

---

### [FAQ]

Q. Variable과 Local Value 차이는?

A.
Variable은 외부에서 주입되는 입력값이고 Local Value는 코드 내부에서 계산하거나 재사용하는 값이다.

Q. Local Value는 언제 사용하는가?

A.
공통 Tag, 이름 Prefix, 반복 Expression처럼 코드 중복을 줄일 때 사용한다.

---

# 12. State Rules

## 12.1 Terraform State 작성 규칙

### [개념]

State는 IaC 코드와 실제 인프라 리소스의 매핑 정보를 저장하는 핵심 파일이다.

Terraform / OpenTofu는 State를 기준으로 현재 상태와 원하는 상태를 비교한다.

---

### [핵심]

필수 포함:

- State
- State File
- Resource Mapping
- Remote State
- State Locking
- Sensitive Data
- Drift Detection
- State Backup

---

### [Flow]

```text
IaC Code
→ Current State
→ Actual Infrastructure
→ Plan Diff
```

---

### [실무]

State 관련 명령:

```bash
terraform state list
terraform state show aws_instance.app_server
terraform state mv
terraform state rm
```

Remote State 사용 권장:

- 팀 협업
- CI/CD 실행
- Locking 필요
- Backup 필요
- 접근 권한 관리 필요

---

### [주의]

State 파일은 민감 정보를 포함할 수 있다.

금지:

- `terraform.tfstate` Git Commit
- State 파일 Slack / Email 공유
- Local State로 팀 운영
- Lock 없이 동시 Apply

---

### [FAQ]

Q. Terraform State는 무엇인가?

A.
IaC 코드와 실제 인프라 리소스의 매핑을 저장하는 파일이다.

Q. State 파일을 Git에 올리면 안 되는 이유는?

A.
민감 정보가 포함될 수 있고 동시 작업 충돌, Drift, State 손상 위험이 있기 때문이다.

Q. 팀 작업에서 Remote State가 필요한 이유는?

A.
공유 State, Locking, Backup, 접근 제어를 통해 안전한 협업을 하기 위해 필요하다.

---

# 13. Backend / Remote State Rules

## 13.1 Backend 작성 규칙

### [개념]

Backend는 Terraform / OpenTofu State를 저장할 위치와 방식을 정의한다.

Remote Backend는 State를 원격 저장소에 보관한다.

---

### [핵심]

필수 포함:

- backend
- remote state
- state locking
- S3 backend
- DynamoDB locking
- Terraform Cloud
- encryption
- access control

---

### [실무]

S3 Backend 예시:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/app/terraform.tfstate"
    region         = "ap-northeast-2"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}
```

Backend 분리 기준:

```text
project/environment/component
```

예:

```text
prod/network/terraform.tfstate
prod/app/terraform.tfstate
staging/app/terraform.tfstate
```

---

### [주의]

Backend 설정은 운영 안정성과 직결된다.

확인:

- State Bucket 접근 권한
- Encryption 활성화
- Locking 활성화
- Versioning 활성화
- State 경로 분리
- 관리자 권한 최소화

---

### [FAQ]

Q. Backend는 무엇인가?

A.
Terraform / OpenTofu State를 어디에 저장할지 정의하는 설정이다.

Q. Remote State Locking은 왜 필요한가?

A.
여러 사용자가 동시에 Apply하여 State가 손상되는 것을 방지하기 위해 필요하다.

Q. S3 Backend에서 Versioning이 필요한 이유는?

A.
State 손상이나 실수 발생 시 이전 버전으로 복구할 수 있기 때문이다.

---

# 14. Module Rules

## 14.1 Module 작성 규칙

### [개념]

Module은 IaC 코드를 재사용 가능한 단위로 분리한 구조이다.

반복되는 인프라 패턴을 표준화하고 복잡도를 낮춘다.

---

### [핵심]

필수 포함:

- root module
- child module
- input variable
- output
- module version
- reusable infrastructure
- module interface

---

### [실무]

Module 호출 예시:

```hcl
module "app_network" {
  source = "./modules/vpc"

  project_name = var.project_name
  environment  = var.environment
  cidr_block   = "10.0.0.0/16"
}
```

Module 구조 예시:

```text
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
  rds/
    main.tf
    variables.tf
    outputs.tf
envs/
  dev/
    main.tf
  prod/
    main.tf
```

---

### [Best Practice]

- Module은 하나의 책임만 가진다.
- Input / Output Interface를 명확히 한다.
- Module 내부에 Environment 값을 하드코딩하지 않는다.
- Module Version을 관리한다.
- 너무 많은 옵션을 가진 거대 Module을 피한다.
- 운영 Resource 삭제 방지 설정을 고려한다.

---

### [FAQ]

Q. Module은 왜 사용하는가?

A.
반복되는 인프라 구성을 재사용하고 표준화하며 코드 중복을 줄이기 위해 사용한다.

Q. Module을 너무 많이 나누면 좋은가?

A.
아니다. 과도한 분리는 복잡도를 높인다. 책임 단위로 적절히 분리해야 한다.

Q. Module 내부에 prod 값을 직접 넣어도 되는가?

A.
권장하지 않는다. 환경별 값은 Variable로 주입해야 한다.

---

# 15. Workspace Rules

## 15.1 Workspace 작성 규칙

### [개념]

Workspace는 같은 IaC 코드에서 여러 State를 분리하여 사용할 수 있는 기능이다.

---

### [핵심]

필수 포함:

- workspace
- state separation
- environment separation
- default workspace
- workspace risk

---

### [실무]

Workspace 명령:

```bash
terraform workspace list
terraform workspace new dev
terraform workspace select prod
```

Workspace 기반 환경 분리 예시:

```text
default
dev
staging
prod
```

---

### [주의]

Workspace는 편리하지만 환경별 차이가 큰 운영 구조에서는 디렉터리 기반 분리를 더 선호할 수 있다.

권장 비교:

| 방식                  | 장점             | 주의                     |
| --------------------- | ---------------- | ------------------------ |
| Workspace             | 코드 재사용 쉬움 | 현재 Workspace 착각 위험 |
| Directory 분리        | 환경 명확성 높음 | 중복 발생 가능           |
| Module + env 디렉터리 | 실무 표준화 쉬움 | 초기 구조 설계 필요      |

---

### [FAQ]

Q. Workspace는 언제 사용하는가?

A.
같은 코드로 여러 State를 관리할 때 사용한다.

Q. 운영 환경에서 Workspace만으로 dev와 prod를 나눠도 되는가?

A.
가능하지만 Workspace 착각 위험이 있다. 운영에서는 env 디렉터리 분리와 명확한 Backend 경로를 선호하는 경우가 많다.

---

# 16. Plan / Apply Rules

## 16.1 Plan / Apply 작성 규칙

### [개념]

Plan은 변경 예정 내용을 미리 계산하는 단계이고 Apply는 실제 인프라에 반영하는 단계이다.

---

### [핵심]

필수 포함:

- terraform plan
- terraform apply
- change review
- create
- update
- destroy
- replacement
- approval

---

### [Flow]

```text
Code Change
→ Format
→ Validate
→ Plan
→ Review
→ Approval
→ Apply
```

---

### [실무]

Plan 저장 예시:

```bash
terraform plan -out=tfplan
terraform apply tfplan
```

Plan Review 기준:

- 생성 Resource 확인
- 변경 Resource 확인
- 삭제 Resource 확인
- Replacement 여부 확인
- Security Group 변경 확인
- IAM Permission 변경 확인
- Database / Storage 삭제 여부 확인
- Cost 영향 확인

---

### [주의]

Plan에서 특히 위험한 항목:

```text
destroy
replace
forces replacement
security group open 0.0.0.0/0
database deletion
public access enabled
iam admin permission
```

---

### [FAQ]

Q. Plan과 Apply 차이는?

A.
Plan은 변경 예정 내용을 미리 보여주는 단계이고 Apply는 실제 인프라에 변경을 반영하는 단계이다.

Q. Apply 전에 반드시 확인해야 하는 것은?

A.
삭제, 교체, Public Access, IAM 권한 확대, Database / Storage 변경을 반드시 확인해야 한다.

Q. terraform plan -out을 사용하는 이유는?

A.
리뷰한 Plan과 실제 Apply 대상을 일치시키기 위해 사용한다.

---

# 17. Destroy Rules

## 17.1 Destroy 작성 규칙

### [개념]

Destroy는 IaC로 관리되는 리소스를 삭제하는 작업이다.

운영 환경에서는 가장 위험한 명령 중 하나이다.

---

### [핵심]

필수 포함:

- terraform destroy
- resource deletion
- production safety
- prevent_destroy
- approval
- backup

---

### [실무]

Destroy 명령:

```bash
terraform destroy
```

운영 보호 예시:

```hcl
resource "aws_db_instance" "main" {
  identifier = "prod-db"

  lifecycle {
    prevent_destroy = true
  }
}
```

---

### [주의]

Destroy 전 확인:

- 대상 Workspace / Backend 확인
- 대상 Environment 확인
- 삭제 Resource 목록 확인
- DB / Storage Backup 확인
- 승인 절차 확인
- CI/CD 자동 Destroy 차단 확인

---

### [FAQ]

Q. terraform destroy는 무엇인가?

A.
IaC State에 포함된 리소스를 실제 인프라에서 삭제하는 명령이다.

Q. 운영 DB에 prevent_destroy를 설정하는 이유는?

A.
실수로 운영 DB가 삭제되는 것을 방지하기 위해 사용한다.

---

# 18. Import Rules

## 18.1 Import 작성 규칙

### [개념]

Import는 이미 존재하는 수동 생성 리소스를 IaC State에 연결하여 코드로 관리하기 시작하는 작업이다.

---

### [핵심]

필수 포함:

- terraform import
- existing resource
- state mapping
- code alignment
- drift risk

---

### [실무]

Import 기본 흐름:

```text
Existing Resource 확인
→ IaC Resource Block 작성
→ terraform import 실행
→ terraform plan 확인
→ 코드와 실제 리소스 차이 수정
```

Import 예시:

```bash
terraform import aws_s3_bucket.app_logs my-existing-bucket
```

---

### [주의]

Import는 State에 리소스를 연결하지만 IaC 코드를 자동으로 완성해주지 않는다.

Import 후 반드시 Plan으로 차이를 확인해야 한다.

---

### [FAQ]

Q. terraform import는 언제 사용하는가?

A.
이미 존재하는 리소스를 Terraform / OpenTofu 관리 대상으로 편입할 때 사용한다.

Q. Import 후 바로 Apply해도 되는가?

A.
권장하지 않는다. 먼저 Plan을 확인하여 코드와 실제 리소스 차이를 조정해야 한다.

---

# 19. Drift Detection Rules

## 19.1 Drift Detection 작성 규칙

### [개념]

Drift는 IaC 코드와 실제 인프라 상태가 달라진 상황이다.

주로 Console 수동 변경, 외부 자동화, 권한 변경, 긴급 수정으로 발생한다.

---

### [핵심]

필수 포함:

- Infrastructure Drift
- Manual Change
- Plan Diff
- State Refresh
- Drift Detection
- Reconciliation

---

### [Flow]

```text
IaC Code
→ State
→ Actual Infrastructure
→ Drift Detection
→ Reconcile
```

---

### [실무]

Drift 확인:

```bash
terraform plan
```

Drift 발생 시 선택:

- IaC 코드에 실제 변경 반영
- 실제 인프라를 코드 기준으로 되돌림
- 리소스를 Import 또는 State 조정
- 긴급 변경 원인 기록
- Manual Change 방지 정책 강화

---

### [주의]

Drift를 무시하면 다음 Apply에서 예상치 못한 변경, 삭제, 장애가 발생할 수 있다.

---

### [FAQ]

Q. Infrastructure Drift는 무엇인가?

A.
IaC 코드와 실제 인프라 상태가 달라진 상황이다.

Q. Drift는 왜 위험한가?

A.
다음 Plan / Apply에서 예상하지 못한 변경이나 삭제가 발생할 수 있기 때문이다.

Q. Drift는 어떻게 확인하는가?

A.
Plan을 실행하여 코드, State, 실제 인프라의 차이를 확인한다.

---

# 20. Secret Management Rules

## 20.1 Secret 관리 규칙

### [개념]

Secret Management는 Credential, Password, Token, API Key를 IaC 코드와 State에서 안전하게 다루기 위한 기준이다.

---

### [핵심]

필수 포함:

- Secret Hardcoding 금지
- Sensitive Variable
- State Secret Exposure
- Secret Manager
- CI/CD Secret
- IAM Role
- Least Privilege
- Rotation

---

### [실무]

금지 예시:

```hcl
variable "db_password" {
  default = "my-password"
}
```

권장:

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

더 권장:

```text
Secret Manager
→ Runtime Reference
→ Application / Infrastructure
```

Secret 주입 방식:

- AWS Secrets Manager
- AWS SSM Parameter Store
- GCP Secret Manager
- Azure Key Vault
- Vault
- GitHub Actions Secrets
- Jenkins Credentials
- IAM Role / Workload Identity

---

### [주의]

`sensitive = true`는 만능 보안 기능이 아니다.

Secret은 State에 저장될 수 있다.

State 접근 권한은 Secret 접근 권한과 같은 수준으로 관리해야 한다.

---

### [FAQ]

Q. IaC 코드에 Secret을 직접 넣으면 안 되는 이유는?

A.
Git, State, Plan Log, CI/CD Log를 통해 노출될 수 있기 때문이다.

Q. sensitive 변수는 Secret을 완전히 보호하는가?

A.
아니다. 출력 노출은 줄이지만 State에 값이 저장될 수 있다.

Q. State 접근 권한을 강하게 제한해야 하는 이유는?

A.
State 파일에는 Secret이나 인프라 민감 정보가 포함될 수 있기 때문이다.

---

# 21. Policy as Code Rules

## 21.1 Policy as Code 작성 규칙

### [개념]

Policy as Code는 인프라 코드가 보안, 비용, 운영 정책을 위반하지 않는지 자동으로 검사하는 방식이다.

---

### [핵심]

필수 포함:

- Policy as Code
- Security Policy
- Cost Policy
- Compliance
- Static Analysis
- Plan Validation
- Preventive Guardrail

---

### [실무]

검사 대상:

- Public S3 Bucket
- Security Group 0.0.0.0/0
- IAM Administrator 권한
- 암호화 비활성화
- Logging 미설정
- Backup 미설정
- Tag 누락
- Region 정책 위반
- Instance Type 정책 위반

도구 예시:

- Checkov
- tfsec
- Terrascan
- OPA
- Sentinel

---

### [Best Practice]

CI/CD에서 Policy 검사를 Plan 전후에 수행한다.

```text
Pull Request
→ Format
→ Validate
→ Static Analysis
→ Plan
→ Policy Check
→ Review
```

---

### [FAQ]

Q. Policy as Code는 왜 필요한가?

A.
보안, 비용, 운영 정책 위반을 배포 전에 자동 탐지하기 위해 필요하다.

Q. Policy 검사는 언제 수행하는가?

A.
Pull Request와 CI/CD Plan 단계에서 수행하는 것이 좋다.

---

# 22. CI/CD Integration Rules

## 22.1 IaC CI/CD 연계 규칙

### [개념]

IaC CI/CD는 인프라 코드 변경을 자동으로 검증하고 승인된 변경만 적용하는 Pipeline 구조이다.

---

### [핵심]

필수 포함:

- Pull Request
- terraform fmt
- terraform validate
- terraform plan
- Plan Comment
- Manual Approval
- terraform apply
- Remote State
- Secret
- Audit Log

---

### [Flow]

```text
Pull Request
→ Format Check
→ Validate
→ Security Scan
→ Plan
→ Review
→ Approval
→ Apply
```

---

### [실무]

GitHub Actions IaC Workflow 예시:

```yaml
name: Terraform Plan

on:
  pull_request:
    paths:
      - "infra/**"

jobs:
  plan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        run: terraform init
        working-directory: infra

      - name: Terraform Format Check
        run: terraform fmt -check
        working-directory: infra

      - name: Terraform Validate
        run: terraform validate
        working-directory: infra

      - name: Terraform Plan
        run: terraform plan
        working-directory: infra
```

운영 Apply는 승인 절차를 둔다.

```text
main merge
→ Plan
→ Manual Approval
→ Apply
```

---

### [주의]

자동 Apply는 위험하다.

운영 환경에서는 다음 조건을 권장한다.

- Pull Request Review 필수
- Plan 결과 확인
- Manual Approval
- 제한된 Apply 권한
- Remote State Locking
- 감사 로그 보관

---

### [FAQ]

Q. IaC 변경도 Pull Request가 필요한가?

A.
필수에 가깝다. 인프라 변경은 장애와 비용에 직접 영향을 주므로 리뷰가 필요하다.

Q. 운영 환경에서 자동 Apply를 해도 되는가?

A.
가능하지만 위험하다. 운영은 Plan Review와 Manual Approval을 두는 것이 안전하다.

Q. CI/CD에서 Terraform Plan 결과를 왜 남기는가?

A.
리뷰어가 생성, 변경, 삭제 리소스를 확인하고 위험 변경을 막기 위해 필요하다.

---

# 23. Environment Structure Rules

## 23.1 Environment 분리 규칙

### [개념]

Environment 분리는 dev, staging, prod 같은 환경별 인프라 상태와 설정을 분리하는 설계이다.

---

### [핵심]

필수 포함:

- dev
- staging
- prod
- environment directory
- tfvars
- backend key
- account separation
- blast radius

---

### [실무]

권장 구조:

```text
infra/
  modules/
    vpc/
    app/
    database/
  envs/
    dev/
      main.tf
      variables.tf
      dev.tfvars
    staging/
      main.tf
      variables.tf
      staging.tfvars
    prod/
      main.tf
      variables.tf
      prod.tfvars
```

Backend Key 분리:

```text
dev/app/terraform.tfstate
staging/app/terraform.tfstate
prod/app/terraform.tfstate
```

---

### [Best Practice]

- prod State는 dev와 분리한다.
- prod Account는 가능하면 분리한다.
- prod Apply 권한은 제한한다.
- prod 변수 파일은 별도 관리한다.
- 공통 구조는 Module로 재사용한다.
- 환경별 차이는 Variable로 주입한다.

---

### [FAQ]

Q. dev와 prod State를 분리해야 하는 이유는?

A.
실수로 운영 리소스를 변경하거나 삭제하는 위험을 줄이기 위해 필요하다.

Q. 환경별 디렉터리 분리와 Workspace 중 무엇이 좋은가?

A.
운영 명확성과 안전성이 중요하면 환경별 디렉터리와 Backend Key 분리를 선호한다.

---

# 24. Naming / Tagging Rules

## 24.1 Naming / Tagging 작성 규칙

### [개념]

Naming과 Tagging은 인프라 리소스를 식별하고 비용, 소유자, 환경, 운영 책임을 추적하기 위한 기준이다.

---

### [핵심]

필수 포함:

- naming convention
- tag
- environment
- project
- owner
- managed_by
- cost center
- resource purpose

---

### [실무]

Tag 예시:

```hcl
locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    Owner       = var.owner
    ManagedBy   = "terraform"
  }
}
```

Naming 예시:

```text
{project}-{environment}-{component}-{resource}
```

예:

```text
festapick-prod-app-sg
festapick-prod-db-subnet-group
festapick-dev-log-bucket
```

---

### [Best Practice]

필수 Tag:

- Project
- Environment
- Owner
- ManagedBy
- CostCenter
- Service

---

### [FAQ]

Q. Tagging은 왜 중요한가?

A.
비용 추적, 리소스 소유자 확인, 운영 관리, 자동화 정책 적용에 필요하다.

Q. ManagedBy Tag는 왜 사용하는가?

A.
해당 리소스가 Terraform / OpenTofu 같은 IaC로 관리되는지 식별하기 위해 사용한다.

---

# 25. Review Rules

## 25.1 IaC Review 작성 규칙

### [개념]

IaC Review는 인프라 코드가 안전하게 적용 가능한지 검토하는 절차이다.

Review Agent가 반드시 수행해야 하는 검증 기준이다.

---

### [핵심]

Review 대상:

- Provider Version 고정
- Backend / Remote State 설정
- State Locking
- Secret Hardcoding
- Resource Naming
- Tagging
- Public Access
- IAM Permission
- Security Group Rule
- Destroy / Replacement
- Module Interface
- Environment 분리
- Plan 결과
- Cost 영향

---

### [실무]

Review Flow:

```text
Code Diff
→ Format / Validate
→ Security Scan
→ Plan Diff
→ Risk Check
→ Approval
```

High Risk 변경:

- Database 삭제
- Storage 삭제
- Resource Replacement
- IAM 권한 확대
- Public Access 추가
- Security Group 0.0.0.0/0
- Encryption 비활성화
- Backup 비활성화
- prod Backend 변경
- State 조작

---

### [FAQ]

Q. IaC Review에서 가장 먼저 확인할 것은?

A.
Plan 결과의 삭제, 교체, Public Access, IAM 권한 확대, Secret 노출 여부를 먼저 확인한다.

Q. Plan 결과에서 replacement가 위험한 이유는?

A.
기존 리소스를 삭제하고 새로 만들 수 있어 장애나 데이터 손실로 이어질 수 있기 때문이다.

Q. IaC Review는 Backend 코드 리뷰보다 중요한가?

A.
둘 다 중요하다. IaC Review는 운영 인프라, 보안, 비용, 데이터 보존에 직접 영향을 준다.

---

# 26. Troubleshooting Rules

## 26.1 IaC Troubleshooting 작성 규칙

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

- Init Failed
- Provider Download Failed
- Authentication Failed
- Plan Failed
- Apply Failed
- State Lock Failed
- State Drift
- Resource Already Exists
- Import Failed
- Access Denied
- Invalid Variable
- Module Source Error
- Backend Configuration Error
- Destroy Accident Risk

---

### [실무]

기본 확인 명령:

```bash
terraform fmt
terraform validate
terraform plan
terraform state list
terraform providers
terraform workspace show
```

상세 로그:

```bash
TF_LOG=DEBUG terraform plan
```

---

### [Troubleshooting]

문제:
Provider 인증 실패.

원인:

- Credential 누락
- IAM 권한 부족
- Region 오류
- CI/CD Secret 누락
- 만료된 Token

해결:

```text
Credential 확인
→ IAM Permission 확인
→ Region 확인
→ CI/CD Secret 확인
→ Provider 설정 확인
```

문제:
State Lock 획득 실패.

원인:

- 다른 Apply 진행 중
- 이전 작업 비정상 종료
- Lock Table 문제
- Backend 권한 부족

해결:

```text
진행 중인 작업 확인
→ Lock 소유자 확인
→ Backend 상태 확인
→ 필요 시 승인 후 Lock 해제
```

문제:
Resource Already Exists 오류.

원인:

- 수동 생성 리소스 존재
- 이전 State 손실
- 이름 중복
- Import 누락

해결:

```text
기존 리소스 확인
→ Import 여부 결정
→ Resource 이름 조정
→ State 매핑 확인
```

문제:
Plan에서 예상치 못한 Destroy 발생.

원인:

- Resource 이름 변경
- State 불일치
- Provider 변경
- Module 구조 변경
- Lifecycle 설정 누락

해결:

```text
Plan 상세 확인
→ State 확인
→ 코드 변경 이력 확인
→ prevent_destroy 검토
→ Apply 중단 후 Review
```

---

### [FAQ]

Q. Terraform Init 실패는 주로 왜 발생하는가?

A.
Backend 설정 오류, Provider 다운로드 실패, Network 문제, 인증 문제로 발생한다.

Q. State Lock 오류는 어떻게 처리해야 하는가?

A.
다른 작업이 진행 중인지 먼저 확인하고, 비정상 Lock일 때만 승인 후 해제해야 한다.

Q. Resource Already Exists 오류는 어떻게 해결하는가?

A.
기존 리소스를 Import하거나 리소스 이름을 변경하고 State 매핑을 확인한다.

---

# 27. Common Mistakes

## 27.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 IaC 문서와 코드를 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- State 파일 Git Commit
- Secret Hardcoding
- tfvars에 Secret 저장 후 Git Commit
- Provider Version 미고정
- latest / most_recent 무분별 사용
- Remote State 미사용
- State Locking 미구성
- prod와 dev State 혼용
- Workspace 착각
- Plan Review 없이 Apply
- 운영 자동 Apply
- prevent_destroy 미적용
- Public Access 실수
- IAM 권한 과다
- Module 과도한 추상화
- Tag 누락
- Import 후 Plan 미확인
- Drift 무시
- Destroy 명령 오사용

---

### [실무]

Review Agent 검토 기준:

```text
IaC Code
→ Provider
→ Backend
→ State
→ Variable
→ Secret
→ Resource
→ Module
→ Plan
→ Security
→ Cost
→ Apply Risk
```

---

### [FAQ]

Q. IaC에서 가장 위험한 실수는?

A.
State 파일 유출, Secret Hardcoding, 운영 리소스 삭제, Public Access, 과도한 IAM 권한 부여이다.

Q. 운영 IaC에서 Apply 전 필수 확인은?

A.
Plan 결과, 삭제 / 교체 리소스, IAM 변경, Public Access, DB / Storage 변경, 승인 여부이다.

---

# 28. File Relationship Rules

## 28.1 다른 Domain Rules와 연계

### [개념]

Infrastructure as Code Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Docker Advanced, Kubernetes, Linux / Ubuntu Server, Monitoring과 연결된다.

---

### [핵심]

연계 구조:

```text
Infrastructure as Code
→ Cloud Resource
→ Docker Runtime
→ Kubernetes
→ CI/CD
→ Monitoring
```

---

### [실무]

파일 간 역할 분리:

| Domain                 | 역할                                           |
| ---------------------- | ---------------------------------------------- |
| Infrastructure as Code | Cloud Resource / State / Module / Provisioning |
| CI/CD                  | Plan / Apply 자동화, 승인 Workflow             |
| Docker Advanced        | Container Image / Runtime / Compose            |
| Kubernetes             | Orchestration / Deployment / Service / Ingress |
| Linux / Ubuntu Server  | Host OS / Permission / Process / Network       |
| Monitoring & Logging   | Provisioned Resource Observability             |
| Security Operations    | IAM / Secret / Policy / Audit                  |

---

### [FAQ]

Q. IaC와 CI/CD는 어디서 연결되는가?

A.
Pull Request, Format, Validate, Plan, Review, Approval, Apply 단계에서 연결된다.

Q. IaC와 Docker Advanced는 어떻게 구분되는가?

A.
IaC는 인프라 리소스 Provisioning을 담당하고 Docker Advanced는 Container Image와 Runtime 구성을 담당한다.

Q. IaC와 Kubernetes는 어떻게 연결되는가?

A.
IaC로 Kubernetes Cluster나 기반 Cloud Resource를 만들고 Kubernetes Domain에서 Workload와 Service 운영을 다룬다.

---

# 29. Retrieval Optimization Rules

## 29.1 Retrieval 최적화 규칙

### [개념]

Infrastructure as Code 문서는 사용자의 문제 상황 검색에 강해야 한다.

사용자 질문은 주로 State, Plan, Apply, Secret, Module, Drift, CI/CD 오류 형태로 들어온다.

---

### [핵심]

강조 대상:

- Infrastructure as Code
- Terraform
- OpenTofu
- Provider
- Resource
- Variable
- Output
- Module
- State
- Remote State
- Backend
- Workspace
- Plan
- Apply
- Destroy
- Import
- Drift
- Secret
- Policy as Code
- CI/CD Integration
- Troubleshooting

---

### [실무]

반복 허용 키워드:

- Terraform State 오류
- Terraform Plan 결과 확인
- Terraform Apply 실패
- Terraform Backend 설정
- Terraform Remote State
- Terraform State Lock
- Terraform Import
- Infrastructure Drift
- IaC Secret 관리
- IaC Module 설계
- IaC CI/CD 연계
- Terraform Destroy 방지
- Terraform Provider 인증 실패
- Terraform Resource Already Exists
- Terraform Workspace 착각

---

### [FAQ]

Q. IaC RAG 문서는 어떤 질문에 강해야 하는가?

A.
State 오류, Plan / Apply 실패, Module 구조, Secret 관리, Remote State, Drift, Import, CI/CD 연계 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
Terraform, OpenTofu, State, Remote State, Plan, Apply, Module, Provider, Secret, Drift, Import, CI/CD 키워드를 반복할 수 있다.

---

# 30. Version Rules

## 30.1 버전 기준

### [개념]

Infrastructure as Code 문서는 Modern IaC 기준으로 작성한다.

---

### [핵심]

기준:

- Terraform
- OpenTofu
- HCL
- Remote State
- State Locking
- Module Versioning
- Provider Version Pinning
- CI/CD Plan Review
- Policy as Code
- Cloud Native Provisioning

---

### [실무]

Legacy 또는 낮은 우선순위:

- 수동 Console 중심 운영
- State Local File 팀 공유
- FTP / 수동 서버 생성 중심
- Secret 파일 직접 공유
- Plan 없이 Apply
- 운영 자동 Destroy
- Provider Version 미고정

---

### [FAQ]

Q. IaC 문서에서 Terraform과 OpenTofu를 함께 다뤄도 되는가?

A.
가능하다. 핵심 개념과 Workflow가 유사하므로 함께 다루되 조직 표준 도구는 명확히 구분한다.

Q. Local State만으로 팀 운영해도 되는가?

A.
권장하지 않는다. 팀 운영은 Remote State, Locking, Backup, 접근 제어가 필요하다.

---

# 31. Quality Checklist

## 31.1 최종 검수 기준

### [개념]

Infrastructure as Code RAG 문서는 Agent가 IaC 실무 문제를 해결할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- IaC Scope 충족
- CI/CD Domain Rules와 충돌 없음
- Docker Advanced Domain Rules와 역할 분리
- Kubernetes Domain Rules와 역할 분리
- FAQ 포함
- Retrieval Queries 포함
- State 관리 강조
- Remote State / Locking 포함
- Secret Hardcoding 금지 강조
- Terraform / OpenTofu Workflow 포함
- Module 설계 포함
- Plan / Apply Review 포함
- Drift / Import / Troubleshooting 포함
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

Q. IaC 문서 품질은 무엇으로 판단하는가?

A.
Agent가 Terraform / OpenTofu 기반 인프라 작성, 검토, State 문제 해결, Secret 검토, CI/CD 연계를 수행할 수 있으면 품질이 높다.

---

# 32. Final Goal

## 32.1 최종 목표

### [개념]

Infrastructure as Code RAG 문서는 단순 IaC 설명서가 아니다.

DevOps Agent / Backend Agent / Review Agent가 인프라를 코드로 생성, 검토, 변경, 복구, 자동화하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve IaC Workflow
- Generate Terraform / OpenTofu Code
- Review Provider / Resource / Module
- Manage Remote State
- Detect Secret Hardcoding
- Review Plan Risk
- Detect Infrastructure Drift
- Support Import Workflow
- Connect IaC with CI/CD
- Prepare Infrastructure for Kubernetes / Docker Runtime

---

### [실무]

최종 연결 흐름:

```text
Infrastructure Requirement
→ Terraform / OpenTofu Code
→ Remote State
→ Plan
→ Review
→ Apply
→ Cloud Resource
→ Docker / Kubernetes Runtime
→ Monitoring
```

---

### [FAQ]

Q. Infrastructure as Code 문서의 최종 목적은?

A.
Agent가 인프라를 코드로 정의하고, 안전하게 검토하고, 자동화하며, State와 Drift 문제를 해결하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Infrastructure as Code Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 IaC 기반 인프라 생성, 검토, 자동화, 문제 해결을 수행하기 위한 RAG 작성 규칙이다.

Q. IaC 문서의 핵심 범위는?
A. Terraform, OpenTofu, Provider, Resource, Variable, Output, Module, State, Remote State, Plan, Apply, Drift, Secret, CI/CD 연계이다.

Q. Infrastructure as Code를 사용하는 이유는?
A. 인프라 변경을 코드로 관리하여 재현성, 변경 이력, 리뷰 가능성, 자동화를 확보하기 위해 사용한다.

Q. Terraform과 OpenTofu는 무엇인가?
A. 인프라 리소스를 코드로 선언하고 Provider를 통해 생성, 변경, 삭제하는 IaC 도구이다.

Q. Terraform Provider는 무엇인가?
A. AWS, Azure, GCP, Kubernetes 같은 외부 API와 통신하기 위한 Plugin이다.

Q. Provider Version을 고정해야 하는 이유는?
A. Provider 변경으로 인한 예기치 않은 Plan 변화와 운영 장애를 줄이기 위해 필요하다.

Q. Resource는 무엇인가?
A. IaC 코드가 생성하거나 관리하는 실제 인프라 객체이다.

Q. Data Source는 무엇인가?
A. IaC가 직접 생성하지 않는 기존 리소스나 외부 정보를 조회하는 읽기 전용 참조이다.

Q. Variable은 왜 사용하는가?
A. 환경별 설정값을 코드에서 분리하고 재사용성을 높이기 위해 사용한다.

Q. Output은 언제 사용하는가?
A. 생성된 리소스의 ID, Endpoint, DNS, IP, ARN 등을 외부로 노출하거나 다른 Module에서 참조할 때 사용한다.

Q. Local Value는 언제 사용하는가?
A. 공통 Tag, 이름 Prefix, 반복 Expression처럼 코드 내부 중복을 줄일 때 사용한다.

Q. Terraform State는 무엇인가?
A. IaC 코드와 실제 인프라 리소스의 매핑 정보를 저장하는 핵심 파일이다.

Q. State 파일을 Git에 올리면 안 되는 이유는?
A. 민감 정보가 포함될 수 있고 State 충돌, 손상, Drift 위험이 있기 때문이다.

Q. Remote State가 필요한 이유는?
A. 팀 협업, State Locking, Backup, 접근 제어, CI/CD 실행을 안전하게 하기 위해 필요하다.

Q. Backend는 무엇인가?
A. Terraform / OpenTofu State를 어디에 저장할지 정의하는 설정이다.

Q. State Locking은 왜 필요한가?
A. 여러 사용자가 동시에 Apply하여 State가 손상되는 것을 방지하기 위해 필요하다.

Q. Module은 왜 사용하는가?
A. 반복되는 인프라 구성을 재사용하고 표준화하며 코드 중복을 줄이기 위해 사용한다.

Q. Workspace는 언제 사용하는가?
A. 같은 IaC 코드에서 여러 State를 분리하여 사용할 때 사용한다.

Q. Plan과 Apply 차이는?
A. Plan은 변경 예정 내용을 미리 보여주고 Apply는 실제 인프라에 변경을 반영한다.

Q. Apply 전에 반드시 확인해야 하는 것은?
A. 삭제, 교체, Public Access, IAM 권한 확대, DB / Storage 변경, Cost 영향이다.

Q. terraform destroy는 무엇인가?
A. IaC State에 포함된 리소스를 실제 인프라에서 삭제하는 명령이다.

Q. prevent_destroy는 왜 사용하는가?
A. 운영 DB, Storage 같은 중요 리소스가 실수로 삭제되는 것을 방지하기 위해 사용한다.

Q. terraform import는 언제 사용하는가?
A. 이미 존재하는 수동 생성 리소스를 Terraform / OpenTofu 관리 대상으로 편입할 때 사용한다.

Q. Infrastructure Drift는 무엇인가?
A. IaC 코드와 실제 인프라 상태가 달라진 상황이다.

Q. Drift는 왜 위험한가?
A. 다음 Plan / Apply에서 예상하지 못한 변경이나 삭제가 발생할 수 있기 때문이다.

Q. IaC 코드에 Secret을 직접 넣으면 안 되는 이유는?
A. Git, State, Plan Log, CI/CD Log를 통해 Credential이 노출될 수 있기 때문이다.

Q. sensitive 변수는 Secret을 완전히 보호하는가?
A. 아니다. 출력 노출은 줄이지만 State에 값이 저장될 수 있다.

Q. Policy as Code는 왜 필요한가?
A. 보안, 비용, 운영 정책 위반을 배포 전에 자동 탐지하기 위해 필요하다.

Q. IaC와 CI/CD는 어떻게 연결되는가?
A. Pull Request, Format, Validate, Security Scan, Plan, Review, Approval, Apply 단계에서 연결된다.

Q. 운영 환경에서 자동 Apply를 해도 되는가?
A. 가능하지만 위험하다. 운영은 Plan Review와 Manual Approval을 두는 것이 안전하다.

Q. dev와 prod State를 분리해야 하는 이유는?
A. 실수로 운영 리소스를 변경하거나 삭제하는 위험을 줄이기 위해 필요하다.

Q. Tagging은 왜 중요한가?
A. 비용 추적, 소유자 확인, 환경 구분, 운영 관리, 자동화 정책 적용에 필요하다.

Q. IaC Review에서 가장 먼저 확인할 것은?
A. Plan 결과의 삭제, 교체, Public Access, IAM 권한 확대, Secret 노출 여부이다.

Q. Terraform Init 실패는 주로 왜 발생하는가?
A. Backend 설정 오류, Provider 다운로드 실패, Network 문제, 인증 문제로 발생한다.

Q. Resource Already Exists 오류는 어떻게 해결하는가?
A. 기존 리소스를 Import하거나 이름을 변경하고 State 매핑을 확인한다.

Q. IaC에서 가장 위험한 실수는?
A. State 파일 유출, Secret Hardcoding, 운영 리소스 삭제, Public Access, 과도한 IAM 권한 부여이다.

Q. IaC와 Docker Advanced는 어떻게 구분되는가?
A. IaC는 인프라 리소스 Provisioning을 담당하고 Docker Advanced는 Container Image와 Runtime 구성을 담당한다.

Q. IaC와 Kubernetes는 어떻게 연결되는가?
A. IaC로 Kubernetes Cluster나 기반 Cloud Resource를 만들고 Kubernetes Domain에서 Workload와 Service 운영을 다룬다.

Q. Infrastructure as Code 문서의 최종 목적은?
A. Agent가 인프라를 코드로 정의하고, 안전하게 검토하고, 자동화하며, State와 Drift 문제를 해결하게 만드는 것이다.
