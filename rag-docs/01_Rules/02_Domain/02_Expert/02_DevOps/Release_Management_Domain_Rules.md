# Release Management Domain Rules

---

# 1. Domain Purpose

## 1.1 Release Management 문서 목적

### [개념]

Release Management Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Release Planning Support
- Versioning Strategy Support
- Change Tracking Support
- Release Note Support
- Release Approval Support
- Rollback Target Management
- Home Server Update Management
- Deployment Strategy 연계 Support

우선순위:

1. Release Core
2. Versioning / Tagging
3. Change Log / Release Note
4. Approval / Checklist
5. Rollback / Hotfix / Home Server Update

---

### [핵심]

Release Management 문서는 단순 배포 문서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- Release와 Deployment 구분
- Version Naming 기준 정의
- Git Tag / Docker Image Tag 기준 설계
- Release Note 작성 기준 제안
- 변경 이력 추적
- 운영 반영 전 Checklist 작성
- 배포 승인 기준 검토
- Rollback 대상 Version 식별
- Hotfix Release 절차 정의
- 홈서버 업데이트 전 백업 / 복구 기준 연결
- CI/CD / Deployment Strategy / Backup DR 문서와 연계

---

### [실무]

2026 개인 홈서버 + DevOps 운영 기준 Release Management 문서는 다음 흐름을 기준으로 작성한다.

```text
Change Complete
→ Version Assign
→ Build Artifact
→ Release Note
→ Release Checklist
→ Approval
→ Deploy
→ Verify
→ Close Release
```

Release Management는 변경 사항을 사용자 또는 운영 환경에 안전하게 전달하고, 문제가 생겼을 때 어떤 버전으로 되돌릴지 명확히 하는 운영 관리 문서이다.

---

### [FAQ]

Q. Release Management 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 변경 이력, 버전, 릴리즈 노트, 승인, Rollback 대상을 관리하기 위한 RAG 문서이다.

Q. Release Management와 Deployment Strategy는 어떻게 다른가?

A.
Release Management는 무엇을 어떤 버전으로 언제 출시할지 관리하고, Deployment Strategy는 그것을 어떤 방식으로 배포할지 다룬다.

Q. 개인 홈서버에도 Release Management가 필요한가?

A.
가볍게는 필요하다. 업데이트 전 백업, 변경 기록, 버전 태그, Rollback 대상 보관만 해도 장애 대응이 쉬워진다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Release Management Domain 문서는 소프트웨어 변경 사항을 버전으로 묶고, 검토하고, 기록하고, 운영에 반영하는 기준을 다룬다.

포함 범위:

- Release Management
- Release Planning
- Versioning
- Semantic Versioning
- Git Tag
- Docker Image Tag
- Artifact Version
- Change Log
- Release Note
- Release Checklist
- Release Approval
- Deployment Window
- Release Candidate
- Stable Release
- Hotfix Release
- Patch Release
- Rollback Target
- Roll Forward
- Compatibility
- Feature Toggle
- Migration Included Release
- Home Server Update
- Release Verification
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Release
- Version
- Semantic Versioning
- Git Tag
- Docker Image Tag
- Artifact
- Change Log
- Release Note
- Release Checklist
- Approval
- Hotfix
- Rollback Target
- Release Candidate
- Stable Release
- Home Server Update

---

### [실무]

Release Management 문서는 아래 상황을 해결할 수 있어야 한다.

- 어떤 변경이 어느 버전에 포함됐는지 확인
- Docker Image Tag 기준 설계
- Git Tag와 Release Note 연결
- 운영 배포 전 Checklist 작성
- 홈서버 AnythingLLM / Docker Compose 업데이트 기록
- DB Migration 포함 여부 확인
- 배포 전 백업 필요 여부 판단
- 문제가 생겼을 때 이전 안정 버전 찾기
- Hotfix Release 절차 설계
- Release 후 검증 결과 기록
- Release 실패 시 Rollback / Roll Forward 판단

---

### [FAQ]

Q. Release Management 문서에 배포 전략을 깊게 포함해야 하는가?

A.
아니다. 배포 방식은 Deployment Strategy 문서에서 다루고, Release Management는 버전, 변경 기록, 승인, 체크리스트, Rollback 대상 관리에 집중한다.

Q. Release Management 문서에 Git 사용법을 모두 포함해야 하는가?

A.
아니다. Git Tag, Branch, Commit SHA와 Release 연결 기준만 다룬다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Release Management 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

Release Management 문서는 검색 친화적인 변경 추적 구조를 우선한다.

```text
Change
→ Version
→ Artifact
→ Release Note
→ Checklist
→ Approval
→ Deploy
→ Verify
→ Rollback Target
```

---

### [실무]

권장 Part 구성:

- Release_Management_Part01_Core.md
- Release_Management_Part02_Versioning_Tagging.md
- Release_Management_Part03_Change_Log_Release_Note.md
- Release_Management_Part04_Checklist_Approval.md
- Release_Management_Part05_Release_Candidate_Stable.md
- Release_Management_Part06_Hotfix_Patch.md
- Release_Management_Part07_Rollback_Target.md
- Release_Management_Part08_Home_Server_Update.md
- Release_Management_Part09_Troubleshooting.md

---

### [FAQ]

Q. Release Management 문서에 FAQ가 필요한가?

A.
필수이다. Release 질문은 “어느 버전으로 배포했지”, “릴리즈 노트 어떻게 쓰지”, “롤백 대상이 뭐지”처럼 문제 상황 중심으로 들어온다.

Q. Release Management 문서는 얼마나 복잡해야 하는가?

A.
개인 홈서버 기준에서는 가볍게 유지한다. 버전, 변경 기록, 업데이트 전 백업, Rollback 대상, 검증 기록만 명확하면 충분하다.

---

# 4. Release Core Rules

## 4.1 Release Core 작성 규칙

### [개념]

Release는 개발된 변경 사항을 특정 버전으로 묶고, 검증 후 사용자 또는 운영 환경에 제공하는 관리 단위이다.

Deployment는 Release를 실행 환경에 반영하는 행위이다.

---

### [핵심]

필수 포함:

- Release
- Deployment
- Version
- Artifact
- Change Set
- Release Note
- Approval
- Verification
- Rollback Target

기본 흐름:

```text
Code Change
→ Build
→ Version
→ Release
→ Deploy
→ Verify
```

---

### [실무]

Release와 Deployment 차이:

| 구분            | 의미                                | 예                         |
| --------------- | ----------------------------------- | -------------------------- |
| Release         | 변경 사항을 버전으로 묶어 출시 관리 | v1.2.0 Release             |
| Deployment      | 실행 환경에 배포                    | Docker Image를 서버에 반영 |
| Artifact        | 배포 가능한 결과물                  | jar, Docker Image          |
| Version         | Release 식별자                      | v1.2.0, 2026.06.29         |
| Rollback Target | 문제 시 되돌릴 안정 버전            | v1.1.9                     |

---

### [FAQ]

Q. Release와 Deployment는 같은가?

A.
아니다. Release는 변경 사항과 버전 관리이고 Deployment는 해당 버전을 실행 환경에 반영하는 작업이다.

Q. Release Management의 핵심은 무엇인가?

A.
어떤 변경이 어떤 버전으로 언제 반영되었고 문제가 생기면 어디로 되돌릴지 명확히 하는 것이다.

---

# 5. Versioning Rules

## 5.1 Versioning 작성 규칙

### [개념]

Versioning은 Release를 식별하기 위해 버전 번호 또는 태그를 부여하는 기준이다.

버전은 변경 이력, 배포 이력, Rollback 대상을 추적하는 핵심 정보이다.

---

### [핵심]

필수 포함:

- Version
- Semantic Versioning
- Major
- Minor
- Patch
- Pre-release
- Build Metadata
- Date Version
- Commit SHA

Semantic Versioning 기본 구조:

```text
MAJOR.MINOR.PATCH
```

예:

```text
1.0.0
1.1.0
1.1.1
2.0.0
```

---

### [실무]

Version 증가 기준:

| 변경 유형           | Version 증가      |
| ------------------- | ----------------- |
| 호환 깨지는 큰 변경 | Major             |
| 기능 추가           | Minor             |
| 버그 수정           | Patch             |
| 긴급 수정           | Patch 또는 Hotfix |
| 실험 버전           | Pre-release       |

예시:

```text
v1.0.0
v1.1.0
v1.1.1
v1.2.0-rc.1
v1.2.0-hotfix.1
```

홈서버 문서 / 설정 버전 예시:

```text
Project_Progress_v3.md
Backup_20260629.tar.gz
anythingllm-compose_20260629.yml
```

---

### [FAQ]

Q. Semantic Versioning은 무엇인가?

A.
MAJOR.MINOR.PATCH 형식으로 변경 영향에 따라 버전을 관리하는 방식이다.

Q. 개인 프로젝트도 버전이 필요한가?

A.
복잡한 버전 체계는 필요 없지만 Release Tag, 날짜 버전, 백업 파일 버전은 있으면 복구와 추적이 쉬워진다.

---

# 6. Git Tag Rules

## 6.1 Git Tag 작성 규칙

### [개념]

Git Tag는 특정 Commit을 Release 지점으로 표시하는 기능이다.

Release된 코드 상태를 나중에 정확히 찾기 위해 사용한다.

---

### [핵심]

필수 포함:

- Git Tag
- Commit SHA
- Release Commit
- Annotated Tag
- Lightweight Tag
- Version Tag
- Tag Push

---

### [실무]

Tag 예시:

```bash
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
```

Release 추적 기준:

```text
Release Version
→ Git Tag
→ Commit SHA
→ Build Artifact
→ Docker Image Tag
→ Deployment Record
```

권장 Tag 이름:

```text
v1.0.0
v1.1.0
v1.1.1
v1.2.0-rc.1
v1.2.1-hotfix.1
```

---

### [주의]

Release 없이 Commit SHA만 기억하면 추적이 어려워질 수 있다.

운영 배포된 Commit은 Tag 또는 Release Record로 남긴다.

---

### [FAQ]

Q. Git Tag는 왜 사용하는가?

A.
Release된 코드 상태를 특정 Commit으로 고정하고 나중에 재현하거나 Rollback하기 위해 사용한다.

Q. Git Tag와 Docker Image Tag는 같아야 하는가?

A.
완전히 같을 필요는 없지만 연결 가능해야 한다. 예를 들어 Git Tag v1.2.0과 Image Tag app:v1.2.0을 맞추면 추적이 쉽다.

---

# 7. Artifact Version Rules

## 7.1 Artifact Version 작성 규칙

### [개념]

Artifact Version은 빌드 결과물에 부여되는 버전이다.

Artifact는 jar, war, Docker Image, static build, Helm Chart, backup archive일 수 있다.

---

### [핵심]

필수 포함:

- Artifact
- Build Output
- Docker Image Tag
- Jar Version
- Static Build
- Commit SHA
- Immutable Artifact
- Registry

---

### [실무]

Artifact 예시:

```text
backend-api-1.2.0.jar
frontend-web-v1.2.0.tar.gz
personal-ai:v1.2.0
personal-ai:git-a1b2c3d
```

Docker Image Tag 기준:

```text
service-name:version
service-name:git-sha
service-name:environment
```

권장:

```text
festa-api:v1.2.0
festa-api:git-a1b2c3d
anythingllm-backup:20260629
```

비권장:

```text
latest only
prod-final
real-final
test-new
```

---

### [주의]

`latest` 단독 사용은 Release 추적과 Rollback을 어렵게 만든다.

운영 배포는 Version Tag 또는 Commit SHA Tag를 함께 사용한다.

---

### [FAQ]

Q. Artifact Version은 왜 중요한가?

A.
어떤 빌드 결과물이 어떤 코드와 연결되는지 추적하고 문제 발생 시 정확히 Rollback하기 위해 필요하다.

Q. Docker Image에 latest만 쓰면 왜 위험한가?

A.
실제 배포된 버전을 알기 어렵고 이전 안정 버전으로 되돌리기 어렵기 때문이다.

---

# 8. Change Log Rules

## 8.1 Change Log 작성 규칙

### [개념]

Change Log는 Release별 변경 사항을 기록한 문서이다.

변경 이력은 장애 분석, 사용자 안내, Rollback 판단, 협업에 사용된다.

---

### [핵심]

필수 포함:

- Added
- Changed
- Fixed
- Removed
- Deprecated
- Security
- Migration
- Breaking Change

---

### [실무]

Change Log 예시:

```text
## v1.2.0 - 2026-06-29

### Added
- 축제 추천 API 추가
- RAG 문서 백업 스크립트 추가

### Changed
- Docker Compose 환경 변수 구조 변경

### Fixed
- 로그인 토큰 갱신 오류 수정

### Security
- 관리자 페이지 접근 제한 강화

### Migration
- notifications 테이블 인덱스 추가
```

---

### [Best Practice]

- 사용자 영향 있는 변경을 먼저 기록한다.
- Breaking Change를 명확히 표시한다.
- DB Migration 포함 여부를 표시한다.
- Security Fix를 별도 표시한다.
- Rollback 위험 변경을 표시한다.
- 너무 사소한 내부 변경은 줄인다.

---

### [FAQ]

Q. Change Log는 왜 필요한가?

A.
어떤 변경이 어떤 버전에 포함되었는지 추적하고 장애 발생 시 원인 후보를 빠르게 좁히기 위해 필요하다.

Q. Change Log에 모든 Commit을 써야 하는가?

A.
아니다. 사용자 영향, 운영 영향, 보안 영향, Migration, 버그 수정 중심으로 요약한다.

---

# 9. Release Note Rules

## 9.1 Release Note 작성 규칙

### [개념]

Release Note는 특정 Release의 주요 변경 사항, 주의사항, 배포 영향, 검증 항목을 정리한 문서이다.

Change Log보다 운영 / 사용자 전달에 가까운 문서이다.

---

### [핵심]

필수 포함:

- Release Version
- Release Date
- Summary
- Changes
- Impact
- Migration
- Rollback Plan
- Verification
- Known Issues

---

### [실무]

Release Note 기본 구조:

```text
Release:
Date:
Summary:
Included Changes:
Migration:
Config Changes:
User Impact:
Deployment Strategy:
Rollback Target:
Verification:
Known Issues:
```

홈서버 업데이트 Release Note 예시:

```text
Release: personal-ai-home-server-2026.06.29
Summary: AnythingLLM 설정 백업 구조 개선
Migration: 없음
Backup Required: Yes
Rollback Target: backup-2026.06.28
Verification: AnythingLLM 접속, RAG 문서 검색, Ollama 연결 확인
```

---

### [FAQ]

Q. Release Note와 Change Log는 무엇이 다른가?

A.
Change Log는 변경 이력 중심이고 Release Note는 운영 반영, 영향, 검증, Rollback 정보를 포함한 출시 안내 문서이다.

Q. 개인 프로젝트에도 Release Note가 필요한가?

A.
짧게라도 있으면 좋다. 특히 설정 변경, DB 변경, Docker Compose 변경, 홈서버 업데이트 기록에 유용하다.

---

# 10. Release Checklist Rules

## 10.1 Release Checklist 작성 규칙

### [개념]

Release Checklist는 운영 반영 전 확인해야 할 항목을 정리한 검증 목록이다.

체크리스트는 실수와 누락을 줄이기 위한 Release Gate 역할을 한다.

---

### [핵심]

필수 포함:

- Build Success
- Test Pass
- Security Check
- Backup Check
- Migration Check
- Config Check
- Rollback Target
- Monitoring Ready
- Approval

---

### [실무]

Release Checklist 예시:

```text
[ ] Build 성공
[ ] Unit / Integration Test 통과
[ ] Docker Image Tag 확인
[ ] Release Note 작성
[ ] DB Migration 포함 여부 확인
[ ] 배포 전 Backup 완료
[ ] .env / Secret 변경 확인
[ ] Rollback 대상 Version 확인
[ ] Health Check 준비
[ ] Monitoring Dashboard 확인
[ ] 배포 승인 완료
```

홈서버용 Checklist:

```text
[ ] compose.yml 백업
[ ] Docker Volume 백업
[ ] AnythingLLM Storage 백업
[ ] RAG 문서 백업
[ ] 현재 Image Tag 기록
[ ] 복구 명령 확인
[ ] 업데이트 후 접속 테스트
```

---

### [FAQ]

Q. Release Checklist는 왜 필요한가?

A.
배포 전 테스트, 백업, 설정, Rollback, 모니터링 준비가 누락되지 않도록 하기 위해 필요하다.

Q. 개인 홈서버에서도 Checklist가 필요한가?

A.
필요하다. 업데이트 전 백업과 복구 대상 기록만 체크해도 장애 대응이 훨씬 쉬워진다.

---

# 11. Release Approval Rules

## 11.1 Release Approval 작성 규칙

### [개념]

Release Approval은 운영 환경에 변경을 반영하기 전에 승인 조건을 확인하는 절차이다.

개인 프로젝트에서는 자기 승인 형태의 체크리스트로 충분할 수 있다.

---

### [핵심]

필수 포함:

- Approval
- Reviewer
- Release Gate
- Risk Review
- Manual Approval
- Auto Approval
- Emergency Approval

---

### [실무]

승인 기준:

- 테스트 통과
- 릴리즈 노트 작성
- Migration 위험 확인
- 백업 완료
- Rollback 대상 확인
- 보안 위험 없음
- 비용 영향 확인
- 배포 시간 확인
- Monitoring 준비

개인 홈서버 승인 기준:

```text
내가 지금 복구할 수 있는가?
백업이 있는가?
문제 생기면 이전 상태로 돌아갈 수 있는가?
업데이트 후 검증할 항목이 명확한가?
```

---

### [주의]

승인 절차가 너무 복잡하면 개인 프로젝트에서는 유지되지 않는다.

홈서버 기준은 가볍고 반복 가능한 체크리스트를 우선한다.

---

### [FAQ]

Q. Release Approval은 왜 필요한가?

A.
운영에 영향을 주는 변경을 반영하기 전에 테스트, 백업, Rollback, 위험 검토가 완료되었는지 확인하기 위해 필요하다.

Q. 개인 프로젝트에서 승인자는 누구인가?

A.
대부분 본인이며, 승인 절차는 체크리스트 확인으로 대체할 수 있다.

---

# 12. Release Candidate Rules

## 12.1 Release Candidate 작성 규칙

### [개념]

Release Candidate는 정식 Release 후보 버전이다.

큰 문제가 없다면 Stable Release로 승격될 수 있는 검증 대상이다.

---

### [핵심]

필수 포함:

- Release Candidate
- RC Version
- Validation
- Smoke Test
- Regression Test
- Known Issues
- Promotion

---

### [실무]

RC Version 예시:

```text
v1.2.0-rc.1
v1.2.0-rc.2
```

RC Flow:

```text
Feature Complete
→ Build RC
→ Test
→ Fix
→ RC Rebuild
→ Approval
→ Stable Release
```

RC 사용이 적합한 상황:

- 큰 기능 변경
- DB Migration 포함
- 인프라 설정 변경
- 다수 사용자 영향
- 팀 프로젝트 발표 전 최종 검증
- 홈서버 대규모 업데이트 전 검증

---

### [FAQ]

Q. Release Candidate는 무엇인가?

A.
정식 Release 전 검증을 위해 만든 후보 버전이다.

Q. 개인 프로젝트에도 RC가 필요한가?

A.
매번 필요하지는 않다. 큰 변경, DB Migration, 홈서버 주요 업데이트 전에는 유용하다.

---

# 13. Stable Release Rules

## 13.1 Stable Release 작성 규칙

### [개념]

Stable Release는 검증을 통과하여 운영 또는 사용자에게 제공 가능한 안정 버전이다.

---

### [핵심]

필수 포함:

- Stable Version
- Approved Release
- Production Ready
- Release Tag
- Artifact Lock
- Verification Complete

---

### [실무]

Stable Release 조건:

- 테스트 통과
- Smoke Test 통과
- Release Note 작성
- Migration 완료 또는 불필요
- Rollback 대상 확인
- Known Critical Issue 없음
- Monitoring 준비
- 배포 후 검증 완료

Stable 기록 예시:

```text
Release: v1.2.0
Status: Stable
Git Tag: v1.2.0
Docker Image: app:v1.2.0
Rollback Target: v1.1.3
Verified: Health Check, Login, Main API
```

---

### [FAQ]

Q. Stable Release는 무엇인가?

A.
검증을 통과하여 운영 환경에 반영하거나 사용자에게 제공할 수 있는 안정 버전이다.

Q. Stable Release로 표시하기 전 무엇을 확인해야 하는가?

A.
테스트, 릴리즈 노트, Rollback 대상, Migration, Health Check, 주요 기능 검증을 확인해야 한다.

---

# 14. Hotfix Release Rules

## 14.1 Hotfix Release 작성 규칙

### [개념]

Hotfix Release는 운영 장애나 긴급 버그를 빠르게 수정하기 위한 Release이다.

일반 Release보다 속도가 중요하지만 추적과 검증을 생략하면 안 된다.

---

### [핵심]

필수 포함:

- Hotfix
- Critical Bug
- Emergency Release
- Minimal Change
- Patch Version
- Fast Verification
- Rollback Target

---

### [Flow]

```text
Issue Detected
→ Impact Confirmed
→ Minimal Fix
→ Build Hotfix
→ Smoke Test
→ Deploy
→ Verify
→ Record
```

---

### [실무]

Hotfix 기준:

- 운영 장애
- 로그인 / 결제 / 핵심 API 장애
- 보안 취약점 긴급 수정
- 데이터 손상 위험
- 배포 후 즉시 발견된 치명적 버그
- 홈서버 접속 불가 / 데이터 접근 불가

Hotfix Version 예시:

```text
v1.2.1
v1.2.1-hotfix.1
```

---

### [주의]

Hotfix는 작은 변경만 포함한다.

기능 추가와 리팩터링을 함께 넣으면 위험이 커진다.

---

### [FAQ]

Q. Hotfix Release는 무엇인가?

A.
운영 장애나 긴급 보안 문제를 빠르게 수정하기 위한 긴급 Release이다.

Q. Hotfix에서 가장 중요한 원칙은?

A.
변경 범위를 최소화하고 빠르게 검증하며 변경 기록과 Rollback 대상을 남기는 것이다.

---

# 15. Patch Release Rules

## 15.1 Patch Release 작성 규칙

### [개념]

Patch Release는 기존 기능의 버그 수정, 작은 개선, 보안 패치를 반영하는 작은 Release이다.

---

### [핵심]

필수 포함:

- Patch
- Bug Fix
- Security Fix
- Minor Risk
- Compatibility
- Regression Check

---

### [실무]

Patch Release에 포함 가능한 변경:

- 버그 수정
- 오류 메시지 개선
- 작은 성능 개선
- 보안 패치
- 문서 수정
- 설정 기본값 개선
- 테스트 보강

포함하지 않는 것이 좋은 변경:

- 큰 기능 추가
- DB 구조 대변경
- API 호환성 깨는 변경
- 인프라 구조 변경
- 다수 설정 변경

---

### [FAQ]

Q. Patch Release는 무엇인가?

A.
기존 버전의 작은 버그 수정, 보안 패치, 안정성 개선을 반영하는 Release이다.

Q. Patch Release에 큰 기능을 넣어도 되는가?

A.
권장하지 않는다. 큰 기능은 Minor Release나 별도 Release로 분리하는 것이 좋다.

---

# 16. Rollback Target Rules

## 16.1 Rollback Target 작성 규칙

### [개념]

Rollback Target은 문제가 발생했을 때 되돌아갈 이전 안정 버전이다.

Release Management에서 Rollback Target은 반드시 기록해야 한다.

---

### [핵심]

필수 포함:

- Previous Stable Version
- Docker Image Tag
- Git Tag
- Backup Point
- Database Compatibility
- Config Compatibility
- Restore Path

---

### [실무]

Rollback Target 기록 예시:

```text
Current Release: v1.2.0
Rollback Target: v1.1.3
Docker Image: app:v1.1.3
Git Tag: v1.1.3
DB Migration Compatible: Yes
Backup Point: backup-20260629-before-release
```

Rollback 가능 여부 검토:

- 이전 Image 존재 여부
- 이전 Git Tag 존재 여부
- 이전 설정 파일 존재 여부
- DB Migration 호환 여부
- 데이터 손상 여부
- Secret 변경 영향
- 외부 API 설정 변경 여부

---

### [주의]

DB Migration이 포함된 Release는 Rollback이 어려울 수 있다.

애플리케이션 버전만 되돌려도 DB Schema가 호환되지 않으면 장애가 계속될 수 있다.

---

### [FAQ]

Q. Rollback Target은 왜 기록해야 하는가?

A.
문제가 생겼을 때 어떤 버전으로 되돌릴지 즉시 판단하기 위해 필요하다.

Q. Rollback Target이 있어도 복구가 안 될 수 있는 이유는?

A.
DB Migration, 설정 변경, 외부 시스템 변경, 데이터 손상 때문에 이전 애플리케이션 버전과 호환되지 않을 수 있다.

---

# 17. Roll Forward Rules

## 17.1 Release Roll Forward 작성 규칙

### [개념]

Roll Forward는 이전 버전으로 되돌리는 대신 새 수정 버전을 배포하여 문제를 해결하는 방식이다.

---

### [핵심]

필수 포함:

- Roll Forward
- Fix Forward
- Patch
- Hotfix
- Root Cause
- Fast Verification
- Risk Review

---

### [실무]

Roll Forward 적합 상황:

- DB Migration 때문에 Rollback이 어려움
- 문제 원인이 명확함
- 수정 범위가 작음
- 이전 버전 복원이 더 위험함
- Feature Toggle로 문제 기능을 끌 수 있음
- 새 Patch Release를 빠르게 검증 가능

Flow:

```text
Issue Detected
→ Root Cause Known
→ Patch Release
→ Smoke Test
→ Deploy
→ Verify
```

---

### [FAQ]

Q. Roll Forward는 무엇인가?

A.
이전 버전으로 되돌리지 않고 수정 버전을 새로 배포하여 문제를 해결하는 방식이다.

Q. Roll Forward는 언제 적합한가?

A.
Rollback이 어렵고 원인이 명확하며 작은 수정으로 해결 가능한 경우에 적합하다.

---

# 18. Feature Release Rules

## 18.1 Feature Release 작성 규칙

### [개념]

Feature Release는 새로운 기능을 포함하는 Release이다.

새 기능은 사용자 영향, API 호환성, Feature Toggle 여부를 함께 검토한다.

---

### [핵심]

필수 포함:

- New Feature
- User Impact
- API Change
- Feature Toggle
- Documentation
- Test Coverage
- Rollout Plan

---

### [실무]

Feature Release 체크 기준:

- 기능 설명
- 사용자 영향
- API 변경 여부
- DB Migration 여부
- Frontend / Backend 배포 순서
- Feature Toggle 필요 여부
- Rollout 방식
- Smoke Test 항목
- Rollback 영향

---

### [주의]

큰 기능은 작은 Release로 나누는 것이 안전하다.

배포와 기능 공개를 Feature Toggle로 분리하면 위험을 줄일 수 있다.

---

### [FAQ]

Q. Feature Release는 무엇인가?

A.
새로운 기능을 포함하는 Release이다.

Q. 큰 기능을 한 번에 Release해도 되는가?

A.
가능하지만 위험하다. 작은 단위로 나누고 Feature Toggle이나 Canary를 검토하는 것이 안전하다.

---

# 19. Migration Included Release Rules

## 19.1 Migration 포함 Release 작성 규칙

### [개념]

Migration Included Release는 DB Schema, 데이터 구조, Storage 경로, 설정 구조 변경이 포함된 Release이다.

가장 주의가 필요한 Release 유형 중 하나이다.

---

### [핵심]

필수 포함:

- Database Migration
- Schema Change
- Data Migration
- Backward Compatibility
- Backup Before Migration
- Rollback Risk
- Expand and Contract

---

### [실무]

Migration 포함 Release Checklist:

```text
[ ] Migration 내용 확인
[ ] Backward Compatibility 확인
[ ] 배포 전 DB Backup 완료
[ ] Migration 실행 순서 확인
[ ] Rollback 가능 여부 확인
[ ] 데이터 검증 Query 준비
[ ] Application Smoke Test 준비
[ ] 장애 시 복구 절차 준비
```

권장 Flow:

```text
Pre-backup
→ Apply Compatible Schema
→ Deploy App
→ Verify
→ Remove Old Schema Later
```

---

### [주의]

컬럼 삭제, 타입 변경, NOT NULL 추가, 대용량 테이블 Migration은 위험하다.

운영에서는 단계적 Migration을 우선한다.

---

### [FAQ]

Q. Migration 포함 Release가 위험한 이유는?

A.
데이터 구조가 바뀌면 단순히 애플리케이션 버전만 되돌려도 복구되지 않을 수 있기 때문이다.

Q. Migration 전 반드시 해야 할 것은?

A.
DB Backup, Rollback 가능성 검토, 데이터 검증 Query 준비, 배포 순서 확인이다.

---

# 20. Config Change Release Rules

## 20.1 Config Change Release 작성 규칙

### [개념]

Config Change Release는 환경 변수, Secret, Reverse Proxy, Port, Feature Flag, 외부 API 설정 변경이 포함된 Release이다.

---

### [핵심]

필수 포함:

- Environment Variable
- Secret
- Config File
- Reverse Proxy
- Port Mapping
- Feature Flag
- External API Config
- Config Backup

---

### [실무]

Config 변경 Release 확인 대상:

- `.env` 변경
- Docker Compose 환경 변수 변경
- Nginx / Caddy / Traefik 설정 변경
- Port Mapping 변경
- DB URL 변경
- API Key 변경
- OAuth Redirect URI 변경
- CORS 설정 변경
- Cookie Domain 변경
- Feature Toggle 변경

Config 변경 전 Flow:

```text
Backup Current Config
→ Apply Config Change
→ Restart Service
→ Health Check
→ Verify External Access
```

---

### [주의]

Config 변경은 코드 변경보다 추적이 어려울 수 있다.

Release Note에 Config 변경 여부를 반드시 기록한다.

---

### [FAQ]

Q. Config 변경도 Release로 기록해야 하는가?

A.
운영 영향이 있으면 기록해야 한다. 특히 Secret, Port, Domain, Reverse Proxy, DB URL 변경은 반드시 남긴다.

Q. Config 변경에서 가장 흔한 장애 원인은?

A.
환경 변수 누락, Secret 불일치, Port 충돌, Reverse Proxy 오류, CORS / Cookie 설정 오류이다.

---

# 21. Home Server Release Rules

## 21.1 Home Server Release 작성 규칙

### [개념]

Home Server Release는 개인 홈서버에서 서비스, Docker Compose, AnythingLLM, Ollama, RAG 문서, OS 설정을 업데이트하는 관리 단위이다.

---

### [핵심]

필수 포함:

- Home Server Update
- Docker Compose Update
- AnythingLLM Update
- Ollama Model Update
- RAG Document Update
- Backup Before Update
- Restore Point
- Smoke Test

---

### [실무]

홈서버 Release 대상:

- Docker Compose 변경
- AnythingLLM Version 변경
- Ollama Model 추가 / 삭제
- RAG 문서 대량 추가
- Nginx / Reverse Proxy 변경
- Ubuntu Package Update
- Backup Script 변경
- 외부 접속 설정 변경
- Agent Prompt 변경

홈서버 Release Flow:

```text
Record Current State
→ Backup Config / Volume
→ Apply Update
→ Restart Service
→ Check Logs
→ Smoke Test
→ Record Result
```

---

### [주의]

홈서버 업데이트는 본인이 운영자이자 사용자이다.

문제 발생 시 복구 가능한 상태에서만 변경한다.

---

### [FAQ]

Q. 홈서버 Release에서 가장 중요한 것은?

A.
변경 전 백업, 현재 버전 기록, 복구 절차, 업데이트 후 Smoke Test이다.

Q. RAG 문서 추가도 Release로 기록해야 하는가?

A.
대량 변경이거나 Agent 답변 품질에 영향을 주는 경우 기록하는 것이 좋다.

---

# 22. Release Verification Rules

## 22.1 Release Verification 작성 규칙

### [개념]

Release Verification은 Release가 의도대로 적용되었고 주요 기능이 정상 동작하는지 확인하는 절차이다.

---

### [핵심]

필수 포함:

- Health Check
- Smoke Test
- Version Check
- Log Check
- Metrics Check
- Business Flow Check
- Rollback Decision

---

### [실무]

검증 항목:

- 배포된 Version 확인
- Health Check 통과
- 주요 API 응답 확인
- 로그인 / 인증 확인
- DB 연결 확인
- 외부 API 연결 확인
- 로그 Error 확인
- Monitoring 지표 확인
- RAG 검색 결과 확인
- AnythingLLM / Ollama 연결 확인
- 사용자 주요 Flow 확인

검증 Flow:

```text
Deploy Complete
→ Version Check
→ Health Check
→ Smoke Test
→ Logs
→ Metrics
→ Release Close
```

---

### [FAQ]

Q. Release 후 무엇을 확인해야 하는가?

A.
Version, Health Check, 주요 기능, 로그, 지표, 사용자 핵심 Flow를 확인해야 한다.

Q. Release가 성공했다는 기준은?

A.
배포가 완료되었고 핵심 기능이 정상 동작하며 Error Rate와 로그에 이상이 없을 때 성공으로 본다.

---

# 23. Release Record Rules

## 23.1 Release Record 작성 규칙

### [개념]

Release Record는 실제 Release 수행 결과를 기록한 운영 이력이다.

Release Note가 계획과 안내라면 Release Record는 실제 실행 결과이다.

---

### [핵심]

필수 포함:

- Release Version
- Released At
- Released By
- Environment
- Artifact
- Git Tag
- Docker Image
- Deployment Result
- Verification Result
- Issue

---

### [실무]

Release Record 예시:

```text
Release Version: v1.2.0
Environment: prod
Git Tag: v1.2.0
Commit SHA: a1b2c3d
Docker Image: app:v1.2.0
Released At: 2026-06-29 22:00 KST
Released By: JUN
Backup: backup-20260629-before-release
Result: Success
Verification: Health OK, Login OK, RAG Search OK
Issue: None
Rollback Target: v1.1.3
```

---

### [FAQ]

Q. Release Record는 왜 필요한가?

A.
나중에 어떤 버전이 언제 어떤 결과로 배포되었는지 확인하고 장애 원인을 추적하기 위해 필요하다.

Q. Release Note와 Release Record는 무엇이 다른가?

A.
Release Note는 출시 내용 설명이고 Release Record는 실제 배포 실행 결과 기록이다.

---

# 24. Release Branch Rules

## 24.1 Release Branch 작성 규칙

### [개념]

Release Branch는 특정 Release를 안정화하거나 Hotfix를 적용하기 위해 분리한 Git Branch이다.

개인 프로젝트에서는 필수는 아니지만 팀 프로젝트나 운영 Release에서 유용하다.

---

### [핵심]

필수 포함:

- release branch
- main branch
- develop branch
- hotfix branch
- branch protection
- merge back
- tag

---

### [실무]

Branch 예시:

```text
main
develop
release/v1.2.0
hotfix/v1.2.1
```

Release Branch Flow:

```text
develop
→ release/v1.2.0
→ test / fix
→ main merge
→ tag v1.2.0
→ develop merge back
```

---

### [주의]

개인 프로젝트에서 Branch 전략을 과하게 복잡하게 만들 필요는 없다.

단순 구조:

```text
main
feature/*
hotfix/*
tag
```

도 충분하다.

---

### [FAQ]

Q. Release Branch는 언제 필요한가?

A.
팀 프로젝트에서 Release 안정화 기간이 있거나 Hotfix와 다음 개발을 분리해야 할 때 필요하다.

Q. 개인 프로젝트에서도 Git Flow를 다 써야 하는가?

A.
아니다. main, feature, hotfix, tag 정도의 단순 구조가 유지하기 쉽다.

---

# 25. Release Communication Rules

## 25.1 Release Communication 작성 규칙

### [개념]

Release Communication은 Release 내용, 영향, 일정, 주의사항을 관련 사용자나 팀원에게 전달하는 절차이다.

개인 프로젝트에서는 기록 목적의 짧은 메모로 충분하다.

---

### [핵심]

필수 포함:

- Release Summary
- Impact
- Schedule
- Downtime
- Migration
- User Action
- Known Issue
- Contact

---

### [실무]

팀 프로젝트 Release 공유 예시:

```text
Release: v1.2.0
Time: 2026-06-29 22:00
Impact: 로그인 API 개선, 알림 오류 수정
Downtime: 없음
Migration: notifications index 추가
Action Required: Frontend 최신 API 반영 필요
Rollback: v1.1.3
```

홈서버 기록 예시:

```text
2026-06-29
- AnythingLLM Storage 백업 후 설정 변경
- 외부 접속 정상
- RAG 검색 정상
- 문제 없음
```

---

### [FAQ]

Q. Release Communication은 왜 필요한가?

A.
변경 영향, 일정, Downtime, 사용자 조치 필요 여부를 명확히 전달하기 위해 필요하다.

Q. 개인 프로젝트에서도 Release Communication이 필요한가?

A.
외부 사용자에게 공지할 필요는 없지만 본인 기록용 Release 메모는 유용하다.

---

# 26. Release Risk Rules

## 26.1 Release Risk 작성 규칙

### [개념]

Release Risk는 특정 Release가 장애, 데이터 손실, 사용자 영향, 보안 문제, 비용 증가를 만들 가능성이다.

---

### [핵심]

Risk 판단 기준:

- DB Migration 포함
- Config / Secret 변경
- 인증 / 권한 변경
- 결제 / 주문 / 로그인 변경
- 외부 API 연동 변경
- 인프라 변경
- 대량 데이터 처리 변경
- Rollback 어려움
- Monitoring 부족
- Backup 없음

---

### [실무]

Risk Level 예시:

| Risk     | 조건                                                     |
| -------- | -------------------------------------------------------- |
| Low      | 문서 수정, UI 문구 수정, 내부 코드 작은 수정             |
| Medium   | API 변경, 설정 변경, 배포 방식 변경                      |
| High     | DB Migration, 인증 변경, 인프라 변경, 대규모 기능        |
| Critical | 데이터 삭제 가능성, 보안 수정, 결제 / 로그인 장애 가능성 |

High Risk Release 추가 조건:

- 배포 전 백업 필수
- 승인 필수
- Rollback Target 확인
- Monitoring 준비
- Smoke Test 준비
- 배포 시간 조정

---

### [FAQ]

Q. Release Risk는 어떻게 판단하는가?

A.
DB, 인증, 설정, 인프라, 외부 API, 데이터 손실 가능성, Rollback 난이도를 기준으로 판단한다.

Q. High Risk Release는 어떻게 처리해야 하는가?

A.
백업, 승인, Rollback 계획, Monitoring, Smoke Test, 배포 시간 조정을 반드시 준비한다.

---

# 27. Troubleshooting Rules

## 27.1 Release Management Troubleshooting 작성 규칙

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

- Release Version Unknown
- Wrong Version Deployed
- Docker Image Tag Missing
- Git Tag Missing
- Release Note Missing
- Rollback Target Missing
- Hotfix Conflict
- Migration Release Failed
- Config Change Missing
- Release Verification Failed
- Release Record Missing

---

### [실무]

기본 확인 흐름:

```text
Issue
→ Release Record
→ Git Tag
→ Commit SHA
→ Artifact Tag
→ Deployment Log
→ Verification Result
→ Rollback Target
```

---

### [Troubleshooting]

문제:
어떤 버전이 배포되었는지 모른다.

원인:

- Release Record 없음
- Docker Image Tag가 latest만 사용됨
- Git Tag 없음
- 배포 로그 누락
- Commit SHA 기록 없음

해결:

```text
실행 중 Image 확인
→ 배포 로그 확인
→ Git Commit 추적
→ Release Record 작성
→ 이후 Version Tag 의무화
```

문제:
Rollback 대상이 없다.

원인:

- 이전 Image 삭제
- Git Tag 없음
- DB Migration 비호환
- 백업 없음
- Config 백업 없음

해결:

```text
Registry Image 확인
→ Git History 확인
→ Backup 확인
→ Roll Forward 검토
→ 이후 Rollback Target 기록
```

문제:
Release Note가 없다.

원인:

- 변경 사항 수동 관리
- Commit만 보고 Release 진행
- Checklist 없음
- 승인 절차 없음

해결:

```text
Git Log 확인
→ PR / Commit 요약
→ 변경 영향 분류
→ Release Note 작성
→ 다음 Release부터 Template 적용
```

문제:
Hotfix가 main과 충돌한다.

원인:

- Hotfix Branch Merge Back 누락
- Release Branch와 develop 차이
- 긴급 수정 후 정규 브랜치 반영 누락

해결:

```text
Hotfix Commit 확인
→ main 반영 확인
→ develop / release branch merge back
→ Tag 재확인
```

문제:
Release 후 검증 실패.

원인:

- Health Check 실패
- Config 누락
- DB Migration 문제
- 잘못된 Image Tag
- Secret 누락
- 외부 API 설정 오류

해결:

```text
Deployment Log 확인
→ Version 확인
→ Config / Secret 확인
→ DB 상태 확인
→ Rollback or Roll Forward 결정
```

---

### [FAQ]

Q. Release 문제가 생기면 가장 먼저 확인할 것은?

A.
Release Record, Git Tag, Commit SHA, Docker Image Tag, 배포 로그, Rollback Target을 먼저 확인한다.

Q. 배포된 버전을 모르면 어떻게 해야 하는가?

A.
실행 중인 Artifact / Docker Image Tag와 배포 로그를 확인하고 이후 Release Record와 Version Tag를 의무화한다.

Q. Rollback 대상이 없으면 어떻게 해야 하는가?

A.
가능한 이전 Artifact, Git History, 백업을 확인하고 어려우면 Roll Forward를 검토해야 한다.

---

# 28. Common Mistakes

## 28.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 Release Management 구성을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- Version 없이 배포
- latest Image Tag만 사용
- Release Note 없음
- Change Log 없음
- Rollback Target 없음
- Git Tag 없음
- Commit SHA 기록 없음
- DB Migration 포함 여부 미기록
- Config 변경 미기록
- 배포 전 백업 누락
- Release Checklist 없음
- 배포 후 검증 기록 없음
- Hotfix 후 main / develop 반영 누락
- Release와 Deployment 혼동
- 개인 홈서버 업데이트 기록 없음
- 이전 안정 버전 삭제
- Release 실패 원인 기록 없음

---

### [실무]

Review Agent 검토 기준:

```text
Version
→ Git Tag
→ Artifact Tag
→ Release Note
→ Checklist
→ Backup
→ Rollback Target
→ Verification
→ Release Record
```

---

### [FAQ]

Q. Release Management Review에서 가장 먼저 확인할 것은?

A.
Version, Git Tag, Artifact Tag, Release Note, Rollback Target, Backup, 검증 기록을 먼저 확인한다.

Q. Release Management에서 가장 위험한 실수는?

A.
어떤 버전이 배포되었는지 모르고, 문제 발생 시 되돌릴 Rollback Target이 없는 것이다.

---

# 29. File Relationship Rules

## 29.1 다른 Domain Rules와 연계

### [개념]

Release Management Domain Rules는 DevOps Expert 문서 체계에서 CI/CD, Deployment Strategy, Docker Advanced, Backup / Disaster Recovery, Monitoring & Logging, Security Operations와 연결된다.

---

### [핵심]

연계 구조:

```text
Release Management
→ Version / Artifact / Release Note
→ CI/CD
→ Deployment Strategy
→ Monitoring
→ Rollback / Recovery
```

---

### [실무]

파일 간 역할 분리:

| Domain                     | 역할                                               |
| -------------------------- | -------------------------------------------------- |
| Release Management         | 버전, 변경 기록, Release Note, 승인, Rollback 대상 |
| CI/CD                      | Build / Test / Artifact 생성 / 배포 자동화         |
| Deployment Strategy        | Rolling, Blue-Green, Canary, Rollback 방식         |
| Docker Advanced            | Image Tag, Registry, Runtime                       |
| Backup / Disaster Recovery | 배포 전 백업, 복구 지점, Recovery Runbook          |
| Monitoring & Logging       | Release 후 검증, Error Rate, Logs                  |
| Security Operations        | 보안 Release, 취약점 대응, 승인, Audit             |
| Cost Optimization / FinOps | Release로 인한 비용 영향 확인                      |

---

### [FAQ]

Q. Release Management와 CI/CD는 어떻게 연결되는가?

A.
CI/CD가 Release Artifact를 빌드하고 테스트하며, Release Version과 배포 기록을 자동화하는 단계에서 연결된다.

Q. Release Management와 Deployment Strategy는 어떻게 연결되는가?

A.
Release Management가 어떤 버전을 출시할지 관리하고 Deployment Strategy가 그 버전을 어떻게 운영에 반영할지 결정한다.

Q. Release Management와 Backup / DR은 어떻게 연결되는가?

A.
Release 전 백업, Rollback Target, 복구 지점, Migration 실패 대응에서 연결된다.

---

# 30. Retrieval Optimization Rules

## 30.1 Retrieval 최적화 규칙

### [개념]

Release Management 문서는 버전, 릴리즈 기록, Rollback 대상, Hotfix 문제 상황 검색에 강해야 한다.

사용자 질문은 주로 “무슨 버전 배포했지”, “릴리즈 노트 작성”, “롤백 대상”, “핫픽스 절차”, “홈서버 업데이트 기록” 형태로 들어온다.

---

### [핵심]

강조 대상:

- Release Management
- Versioning
- Semantic Versioning
- Git Tag
- Docker Image Tag
- Artifact Version
- Change Log
- Release Note
- Release Checklist
- Release Approval
- Release Candidate
- Stable Release
- Hotfix Release
- Patch Release
- Rollback Target
- Home Server Release

---

### [실무]

반복 허용 키워드:

- Release Management
- Release Note
- Change Log
- Git Tag
- Docker Image Tag
- Versioning
- Semantic Versioning
- Rollback Target
- Hotfix Release
- Patch Release
- Release Checklist
- Release Record
- Home Server Update
- 배포 전 백업
- Release Verification
- Release Troubleshooting

---

### [FAQ]

Q. Release Management RAG 문서는 어떤 질문에 강해야 하는가?

A.
버전 관리, Git Tag, Docker Image Tag, Release Note, Rollback Target, Hotfix, 홈서버 업데이트 기록 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
Release, Version, Git Tag, Docker Image Tag, Artifact, Release Note, Change Log, Rollback Target, Hotfix 키워드를 반복할 수 있다.

---

# 31. Version Rules

## 31.1 버전 기준

### [개념]

Release Management 문서는 Modern DevOps Release 기준과 개인 홈서버 경량 운영 기준을 함께 따른다.

---

### [핵심]

기준:

- Semantic Versioning
- Git Tag
- Docker Image Tag
- Immutable Artifact
- Release Note
- Change Log
- Release Checklist
- Rollback Target
- Hotfix Release
- Home Server Update Record

---

### [실무]

Legacy 또는 낮은 우선순위:

- latest만 사용
- final.zip
- real-final-v2
- Git Tag 없는 배포
- Release Note 없는 운영 반영
- Rollback 대상 없는 배포
- 배포 후 검증 기록 없음
- 홈서버 업데이트 기록 없음
- DB Migration 포함 여부 미기록

---

### [FAQ]

Q. Release Management 문서에서 Modern 기준은 무엇인가?

A.
Version, Git Tag, Artifact Tag, Release Note, Checklist, Rollback Target, 검증 기록을 연결하는 것이다.

Q. 개인 프로젝트에서 복잡한 Release 프로세스가 필요한가?

A.
복잡할 필요는 없다. 버전 태그, 변경 기록, 백업, Rollback 대상, 검증 기록만 있어도 충분히 도움이 된다.

---

# 32. Quality Checklist

## 32.1 최종 검수 기준

### [개념]

Release Management RAG 문서는 Agent가 Release를 추적하고 안전하게 운영 반영을 관리할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Release Management Scope 충족
- Deployment Strategy와 역할 분리
- CI/CD Domain Rules와 연결
- Docker Advanced Domain Rules와 연결
- Backup / Disaster Recovery Domain Rules와 연결
- Monitoring & Logging Domain Rules와 연결
- Security Operations Domain Rules와 연결
- Versioning 포함
- Git Tag 포함
- Docker Image Tag 포함
- Release Note 포함
- Change Log 포함
- Checklist / Approval 포함
- Hotfix / Patch 포함
- Rollback Target 포함
- Home Server Release 포함
- Troubleshooting 포함
- FAQ 포함
- Retrieval Queries 포함
- latest 단독 사용 금지 강조
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

Q. Release Management 문서 품질은 무엇으로 판단하는가?

A.
Agent가 버전, Git Tag, Artifact Tag, Release Note, Rollback Target, Hotfix, 검증 기록을 관리할 수 있으면 품질이 높다.

---

# 33. Final Goal

## 33.1 최종 목표

### [개념]

Release Management RAG 문서는 단순 릴리즈 노트 작성 문서가 아니다.

DevOps Agent / Backend Agent / Review Agent가 변경 사항을 버전으로 관리하고, 운영 반영 전 검토하며, 문제 발생 시 추적과 복구를 지원하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Release Workflow
- Design Versioning Strategy
- Connect Git Tag and Artifact Tag
- Write Change Log
- Write Release Note
- Prepare Release Checklist
- Review Release Risk
- Identify Rollback Target
- Support Hotfix Release
- Record Home Server Update
- Verify Release Result
- Troubleshoot Release Tracking Issues

---

### [실무]

최종 연결 흐름:

```text
Change Set
→ Version
→ Git Tag
→ Artifact Tag
→ Release Note
→ Checklist
→ Deploy
→ Verify
→ Release Record
→ Rollback Target
```

---

### [FAQ]

Q. Release Management 문서의 최종 목적은?

A.
Agent가 변경 사항을 버전으로 추적하고, 안전하게 Release를 관리하며, 문제 발생 시 Rollback 또는 Hotfix를 지원하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Release Management Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 버전, 변경 이력, Release Note, Checklist, Rollback Target을 관리하기 위한 RAG 작성 규칙이다.

Q. Release Management 문서의 핵심 범위는?
A. Versioning, Git Tag, Docker Image Tag, Artifact Version, Change Log, Release Note, Checklist, Approval, Hotfix, Rollback Target, Home Server Update이다.

Q. Release와 Deployment는 무엇이 다른가?
A. Release는 변경 사항과 버전 관리이고 Deployment는 해당 버전을 실행 환경에 반영하는 작업이다.

Q. Semantic Versioning은 무엇인가?
A. MAJOR.MINOR.PATCH 형식으로 변경 영향에 따라 버전을 관리하는 방식이다.

Q. 개인 프로젝트도 버전이 필요한가?
A. 복잡한 버전 체계는 필요 없지만 Release Tag, 날짜 버전, 백업 파일 버전은 있으면 복구와 추적이 쉬워진다.

Q. Git Tag는 왜 사용하는가?
A. Release된 코드 상태를 특정 Commit으로 고정하고 나중에 재현하거나 Rollback하기 위해 사용한다.

Q. Git Tag와 Docker Image Tag는 같아야 하는가?
A. 완전히 같을 필요는 없지만 연결 가능해야 한다. Git Tag v1.2.0과 Image Tag app:v1.2.0을 맞추면 추적이 쉽다.

Q. Artifact Version은 왜 중요한가?
A. 어떤 빌드 결과물이 어떤 코드와 연결되는지 추적하고 문제 발생 시 정확히 Rollback하기 위해 필요하다.

Q. Docker Image에 latest만 쓰면 왜 위험한가?
A. 실제 배포된 버전을 알기 어렵고 이전 안정 버전으로 되돌리기 어렵기 때문이다.

Q. Change Log는 왜 필요한가?
A. 어떤 변경이 어떤 버전에 포함되었는지 추적하고 장애 발생 시 원인 후보를 빠르게 좁히기 위해 필요하다.

Q. Release Note와 Change Log는 무엇이 다른가?
A. Change Log는 변경 이력 중심이고 Release Note는 운영 반영, 영향, 검증, Rollback 정보를 포함한 출시 안내 문서이다.

Q. Release Checklist는 왜 필요한가?
A. 배포 전 테스트, 백업, 설정, Rollback, 모니터링 준비가 누락되지 않도록 하기 위해 필요하다.

Q. 개인 홈서버에서도 Checklist가 필요한가?
A. 필요하다. 업데이트 전 백업과 복구 대상 기록만 체크해도 장애 대응이 쉬워진다.

Q. Release Approval은 왜 필요한가?
A. 운영에 영향을 주는 변경을 반영하기 전에 테스트, 백업, Rollback, 위험 검토가 완료되었는지 확인하기 위해 필요하다.

Q. Release Candidate는 무엇인가?
A. 정식 Release 전 검증을 위해 만든 후보 버전이다.

Q. Stable Release는 무엇인가?
A. 검증을 통과하여 운영 환경에 반영하거나 사용자에게 제공할 수 있는 안정 버전이다.

Q. Hotfix Release는 무엇인가?
A. 운영 장애나 긴급 보안 문제를 빠르게 수정하기 위한 긴급 Release이다.

Q. Hotfix에서 가장 중요한 원칙은?
A. 변경 범위를 최소화하고 빠르게 검증하며 변경 기록과 Rollback 대상을 남기는 것이다.

Q. Patch Release는 무엇인가?
A. 기존 버전의 작은 버그 수정, 보안 패치, 안정성 개선을 반영하는 Release이다.

Q. Rollback Target은 왜 기록해야 하는가?
A. 문제가 생겼을 때 어떤 버전으로 되돌릴지 즉시 판단하기 위해 필요하다.

Q. Rollback Target이 있어도 복구가 안 될 수 있는 이유는?
A. DB Migration, 설정 변경, 외부 시스템 변경, 데이터 손상 때문에 이전 애플리케이션 버전과 호환되지 않을 수 있다.

Q. Roll Forward는 무엇인가?
A. 이전 버전으로 되돌리지 않고 수정 버전을 새로 배포하여 문제를 해결하는 방식이다.

Q. Feature Release는 무엇인가?
A. 새로운 기능을 포함하는 Release이다.

Q. Migration 포함 Release가 위험한 이유는?
A. 데이터 구조가 바뀌면 단순히 애플리케이션 버전만 되돌려도 복구되지 않을 수 있기 때문이다.

Q. Migration 전 반드시 해야 할 것은?
A. DB Backup, Rollback 가능성 검토, 데이터 검증 Query 준비, 배포 순서 확인이다.

Q. Config 변경도 Release로 기록해야 하는가?
A. 운영 영향이 있으면 기록해야 한다. 특히 Secret, Port, Domain, Reverse Proxy, DB URL 변경은 반드시 남긴다.

Q. 홈서버 Release에서 가장 중요한 것은?
A. 변경 전 백업, 현재 버전 기록, 복구 절차, 업데이트 후 Smoke Test이다.

Q. RAG 문서 추가도 Release로 기록해야 하는가?
A. 대량 변경이거나 Agent 답변 품질에 영향을 주는 경우 기록하는 것이 좋다.

Q. Release 후 무엇을 확인해야 하는가?
A. Version, Health Check, 주요 기능, 로그, 지표, 사용자 핵심 Flow를 확인해야 한다.

Q. Release Record는 왜 필요한가?
A. 나중에 어떤 버전이 언제 어떤 결과로 배포되었는지 확인하고 장애 원인을 추적하기 위해 필요하다.

Q. Release Branch는 언제 필요한가?
A. 팀 프로젝트에서 Release 안정화 기간이 있거나 Hotfix와 다음 개발을 분리해야 할 때 필요하다.

Q. 개인 프로젝트에서도 Git Flow를 다 써야 하는가?
A. 아니다. main, feature, hotfix, tag 정도의 단순 구조가 유지하기 쉽다.

Q. Release Risk는 어떻게 판단하는가?
A. DB, 인증, 설정, 인프라, 외부 API, 데이터 손실 가능성, Rollback 난이도를 기준으로 판단한다.

Q. High Risk Release는 어떻게 처리해야 하는가?
A. 백업, 승인, Rollback 계획, Monitoring, Smoke Test, 배포 시간 조정을 반드시 준비한다.

Q. Release 문제가 생기면 가장 먼저 확인할 것은?
A. Release Record, Git Tag, Commit SHA, Docker Image Tag, 배포 로그, Rollback Target을 먼저 확인한다.

Q. 배포된 버전을 모르면 어떻게 해야 하는가?
A. 실행 중인 Artifact / Docker Image Tag와 배포 로그를 확인하고 이후 Release Record와 Version Tag를 의무화한다.

Q. Rollback 대상이 없으면 어떻게 해야 하는가?
A. 가능한 이전 Artifact, Git History, 백업을 확인하고 어려우면 Roll Forward를 검토해야 한다.

Q. Release Management Review에서 가장 먼저 확인할 것은?
A. Version, Git Tag, Artifact Tag, Release Note, Rollback Target, Backup, 검증 기록을 먼저 확인한다.

Q. Release Management와 CI/CD는 어떻게 연결되는가?
A. CI/CD가 Release Artifact를 빌드하고 테스트하며, Release Version과 배포 기록을 자동화하는 단계에서 연결된다.

Q. Release Management와 Deployment Strategy는 어떻게 연결되는가?
A. Release Management가 어떤 버전을 출시할지 관리하고 Deployment Strategy가 그 버전을 어떻게 운영에 반영할지 결정한다.

Q. Release Management와 Backup / DR은 어떻게 연결되는가?
A. Release 전 백업, Rollback Target, 복구 지점, Migration 실패 대응에서 연결된다.

Q. Release Management 문서의 최종 목적은?
A. Agent가 변경 사항을 버전으로 추적하고, 안전하게 Release를 관리하며, 문제 발생 시 Rollback 또는 Hotfix를 지원하게 만드는 것이다.
