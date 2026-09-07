# Backup / Disaster Recovery Domain Rules

---

# 1. Domain Purpose

## 1.1 Backup / Disaster Recovery 문서 목적

### [개념]

Backup / Disaster Recovery Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Backup Strategy Support
- Restore Procedure Support
- Home Server Data Protection Support
- Docker Volume Backup Support
- Database Backup / Restore Support
- Cloud Object Storage Backup Support
- Disaster Recovery Planning Support
- Recovery Test / Validation Support

우선순위:

1. Backup Core
2. Restore Core
3. Home Server Backup
4. Docker / Database Backup
5. Disaster Recovery / Recovery Test

---

### [핵심]

Backup / Disaster Recovery 문서는 단순 파일 복사 문서가 아니다.

Agent가 아래 작업을 수행할 수 있어야 한다.

- 백업 대상 식별
- 백업 전략 설계
- Docker Volume 백업 기준 작성
- Database Dump 백업 기준 작성
- RAG 문서 / AnythingLLM Storage 백업 기준 작성
- Cloud Object Storage 백업 설계
- 복구 절차 작성
- Restore Test 기준 정의
- RPO / RTO 이해
- 장애 유형별 복구 전략 제안
- Backup Security Review 수행
- Cloud Provider / Docker / Monitoring / Security Operations 문서와 연계

---

### [실무]

2026 개인 홈서버 + DevOps 운영 기준 Backup / Disaster Recovery 문서는 다음 흐름을 기준으로 작성한다.

```text
Important Data
→ Backup Target Selection
→ Backup Method
→ Backup Storage
→ Encryption
→ Verification
→ Restore Test
→ Disaster Recovery Plan
```

홈서버 기준에서는 대기업식 복잡한 DR보다 **데이터 손실 방지 + 빠른 복구 절차 + 주기적 복구 테스트**를 우선한다.

---

### [FAQ]

Q. Backup / Disaster Recovery 문서는 누구를 위한 문서인가?

A.
DevOps Agent, Backend Agent, Review Agent가 데이터 손실을 방지하고 장애 발생 시 복구 절차를 설계하기 위한 RAG 문서이다.

Q. 홈서버 개인 프로젝트에도 Backup / DR 문서가 필요한가?

A.
필요하다. SSD 고장, Docker Volume 삭제, OS 문제, 설정 파일 유실, RAG 문서 손실에 대비하기 위해 중요하다.

Q. Backup과 Disaster Recovery는 같은가?

A.
아니다. Backup은 데이터를 보관하는 것이고 Disaster Recovery는 장애 발생 후 서비스와 데이터를 복구하는 전체 절차이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Backup / Disaster Recovery Domain 문서는 데이터 백업, 복구, 장애 대응, 복구 검증, 백업 보안을 다룬다.

포함 범위:

- Backup
- Restore
- Disaster Recovery
- RPO
- RTO
- Backup Target
- Backup Schedule
- Full Backup
- Incremental Backup
- Differential Backup
- Snapshot
- Database Dump
- Docker Volume Backup
- File Backup
- Configuration Backup
- Cloud Object Storage Backup
- S3 Backup
- Offsite Backup
- Encryption
- Retention
- Versioning
- Restore Test
- Recovery Runbook
- Home Server Backup
- AnythingLLM Backup
- RAG Document Backup
- Monitoring / Alerting
- Troubleshooting

---

### [핵심]

반드시 포함할 키워드:

- Backup
- Restore
- Disaster Recovery
- RPO
- RTO
- Snapshot
- Dump
- Docker Volume
- Database Backup
- Configuration Backup
- Object Storage
- Offsite Backup
- Encryption
- Retention
- Versioning
- Restore Test
- Recovery Runbook
- Home Server

---

### [실무]

Backup / Disaster Recovery 문서는 아래 상황을 해결할 수 있어야 한다.

- 홈서버 SSD 고장 대비
- Ubuntu 재설치 대비
- Docker Volume 삭제 대비
- AnythingLLM 데이터 손실 대비
- RAG 문서 손실 대비
- PostgreSQL / MySQL / SQLite 백업
- Ollama 모델 / 설정 백업 필요 여부 판단
- `.env` / compose.yml / reverse proxy 설정 백업
- Cloud Object Storage로 Offsite Backup 구성
- 백업 암호화와 접근 권한 검토
- 백업 파일이 실제 복구 가능한지 검증
- 장애 발생 시 복구 순서 결정

---

### [FAQ]

Q. Backup / DR 문서에서 기업식 DR 전체를 다뤄야 하는가?

A.
아니다. 개인 홈서버와 DevOps Agent 기준에서는 백업 대상, 복구 절차, 복구 테스트, Cloud Storage 연계 중심으로 작성한다.

Q. Backup / DR 문서에 Cloud Provider 내용을 포함해야 하는가?

A.
깊게 포함하지 않는다. S3 같은 Object Storage를 백업 저장소로 사용하는 연결 지점만 다룬다.

---

# 3. Section Priority

## 3.1 문서 섹션 규칙

### [개념]

Backup / Disaster Recovery 문서는 MASTER_RAG_RULES의 Required Section 구조를 따른다.

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

Backup / Disaster Recovery 문서는 검색 친화적인 복구 중심 구조를 우선한다.

```text
Failure Scenario
→ Backup Target
→ Backup Method
→ Backup Storage
→ Restore Procedure
→ Restore Test
→ Recovery Review
```

---

### [실무]

권장 Part 구성:

- Backup_Disaster_Recovery_Part01_Core.md
- Backup_Disaster_Recovery_Part02_RPO_RTO.md
- Backup_Disaster_Recovery_Part03_Home_Server_Backup.md
- Backup_Disaster_Recovery_Part04_Docker_Volume_Backup.md
- Backup_Disaster_Recovery_Part05_Database_Backup.md
- Backup_Disaster_Recovery_Part06_Cloud_Offsite_Backup.md
- Backup_Disaster_Recovery_Part07_Restore_Test.md
- Backup_Disaster_Recovery_Part08_Disaster_Recovery_Runbook.md
- Backup_Disaster_Recovery_Part09_Security_Troubleshooting.md

---

### [FAQ]

Q. Backup / DR 문서에 FAQ가 필요한가?

A.
필수이다. 백업 질문은 “Docker Volume 날아감”, “DB 복구”, “S3 백업”, “복구 테스트”, “SSD 고장”처럼 문제 상황으로 들어오는 경우가 많다.

Q. Backup / DR 문서는 백업 명령어만 모으면 되는가?

A.
아니다. 백업 대상, 저장 위치, 암호화, 보존 기간, 복구 절차, 복구 테스트까지 포함해야 한다.

---

# 4. Backup Core Rules

## 4.1 Backup Core 작성 규칙

### [개념]

Backup은 장애, 실수, 삭제, 손상, 보안 사고에 대비하여 중요한 데이터를 별도 위치에 복사하고 보관하는 작업이다.

필수 포함:

- Backup Target
- Backup Frequency
- Backup Storage
- Backup Verification
- Retention
- Encryption
- Restore Test

---

### [핵심]

Backup 핵심 목표:

- 데이터 손실 방지
- 설정 복구 가능성 확보
- 서비스 복구 시간 단축
- 실수로 인한 삭제 대응
- 랜섬웨어 / 침해 사고 대응
- 홈서버 재설치 대응
- Docker / DB / RAG 문서 보호

기본 흐름:

```text
Identify Data
→ Create Backup
→ Store Safely
→ Verify Backup
→ Test Restore
```

---

### [실무]

홈서버 백업 우선순위:

1. 직접 만든 문서와 코드
2. RAG 문서
3. AnythingLLM Storage
4. Database Data
5. Docker Compose 설정
6. `.env.example` 또는 Secret 목록 구조
7. Nginx / Reverse Proxy 설정
8. SSH Key / 인증서 관련 정보
9. 시스템 설치 기록
10. 운영 Runbook

---

### [FAQ]

Q. Backup의 핵심은 무엇인가?

A.
중요 데이터를 별도 위치에 보관하고 실제로 복구 가능한 상태인지 검증하는 것이다.

Q. 백업 대상은 어떻게 정하는가?

A.
잃어버리면 다시 만들기 어렵거나 시간이 오래 걸리는 데이터와 설정을 우선 백업한다.

---

# 5. Disaster Recovery Core Rules

## 5.1 Disaster Recovery Core 작성 규칙

### [개념]

Disaster Recovery는 장애나 재해 발생 후 서비스와 데이터를 목표 수준으로 복구하는 절차이다.

Backup은 DR의 일부이다.

---

### [핵심]

필수 포함:

- Disaster Scenario
- Recovery Plan
- RPO
- RTO
- Restore Procedure
- Backup Storage
- Recovery Priority
- Runbook
- Validation

기본 흐름:

```text
Failure Detected
→ Impact Assessment
→ Recovery Target Select
→ Restore Data
→ Restore Service
→ Verify
→ Post-Recovery Review
```

---

### [실무]

홈서버 DR 시나리오:

- Docker Container만 죽음
- Docker Volume 삭제
- DB 데이터 손상
- Ubuntu 설정 꼬임
- SSD 고장
- 홈 네트워크 장애
- 공유기 / 포트포워딩 문제
- 외부 접속 도메인 문제
- Cloud 백업 접근 실패
- Secret 노출 후 재발급 필요

---

### [FAQ]

Q. Disaster Recovery는 무엇인가?

A.
장애 발생 후 서비스와 데이터를 복구하기 위한 계획, 절차, 검증 활동이다.

Q. Backup만 있으면 DR이 완성되는가?

A.
아니다. 백업을 어디서 어떻게 복구할지 절차와 테스트가 있어야 DR이 된다.

---

# 6. RPO / RTO Rules

## 6.1 RPO / RTO 작성 규칙

### [개념]

RPO는 허용 가능한 데이터 손실 시간이고 RTO는 허용 가능한 복구 시간이다.

- RPO: Recovery Point Objective
- RTO: Recovery Time Objective

---

### [핵심]

구분:

| 용어 | 의미                                   | 예                           |
| ---- | -------------------------------------- | ---------------------------- |
| RPO  | 어느 시점까지의 데이터 손실을 허용할지 | 최대 24시간 데이터 손실 허용 |
| RTO  | 장애 후 얼마나 빨리 복구해야 하는지    | 2시간 안에 서비스 복구       |

---

### [실무]

홈서버 기준 예시:

```text
RAG Documents
→ RPO: 24 hours
→ RTO: 2 hours

AnythingLLM Storage
→ RPO: 24 hours
→ RTO: 4 hours

Database
→ RPO: 6 hours
→ RTO: 2 hours

Ollama Models
→ RPO: 낮음
→ RTO: 재다운로드 가능하면 길어도 됨
```

RPO가 짧을수록 백업 주기가 짧아져야 한다.

RTO가 짧을수록 복구 절차가 자동화되어 있어야 한다.

---

### [FAQ]

Q. RPO는 무엇인가?

A.
장애 발생 시 어느 시점까지의 데이터 손실을 허용할지 정하는 목표이다.

Q. RTO는 무엇인가?

A.
장애 발생 후 서비스를 얼마나 빨리 복구해야 하는지 정하는 목표이다.

Q. 홈서버에서도 RPO / RTO가 필요한가?

A.
필요하다. 복잡하게 관리하지 않아도 백업 주기와 복구 우선순위를 정하는 기준이 된다.

---

# 7. Backup Target Rules

## 7.1 Backup Target 작성 규칙

### [개념]

Backup Target은 백업해야 하는 데이터, 설정, 상태, 문서, Secret 구조를 의미한다.

모든 파일을 백업하기보다 복구에 필요한 핵심 대상을 우선한다.

---

### [핵심]

필수 백업 대상:

- User Data
- RAG Documents
- Database
- Docker Volume
- Application Config
- Docker Compose File
- Reverse Proxy Config
- Environment Example
- SSL / TLS Certificate Metadata
- Recovery Runbook

---

### [실무]

개인 AI 홈서버 백업 대상 예시:

```text
RAG Documents
- Master Rules
- Domain Rules
- SQL / Java / Spring / DevOps 문서
- Project Progress

AnythingLLM
- storage directory
- uploaded documents
- workspace metadata
- vector database data

Ollama
- model list
- custom model file
- pull script
- 모델 자체는 재다운로드 가능하면 낮은 우선순위

Docker
- compose.yml
- volume data
- container env example
- network / port mapping 기록

System
- nginx config
- firewall rule notes
- cron backup script
- SSH access notes
```

---

### [주의]

Secret 원문은 백업 방식에 주의한다.

권장:

- Secret Manager 사용
- 암호화된 백업
- `.env.example`은 Git 관리 가능
- 실제 `.env`는 접근 제한
- Secret 목록 구조와 재발급 절차 문서화

---

### [FAQ]

Q. 홈서버에서 가장 먼저 백업해야 하는 것은?

A.
직접 만든 RAG 문서, DB 데이터, Docker Volume, 설정 파일, 복구 절차 문서이다.

Q. Ollama 모델도 반드시 백업해야 하는가?

A.
재다운로드 가능하면 우선순위는 낮다. 대신 모델 이름, 태그, pull 명령, 설정 파일은 기록해두는 것이 좋다.

---

# 8. Backup Type Rules

## 8.1 Backup Type 작성 규칙

### [개념]

Backup Type은 데이터를 어떤 방식으로 백업하는지 구분하는 기준이다.

대표 유형:

- Full Backup
- Incremental Backup
- Differential Backup
- Snapshot
- Dump
- File Sync

---

### [핵심]

비교:

| 유형                | 설명                         | 적합 대상                      |
| ------------------- | ---------------------------- | ------------------------------ |
| Full Backup         | 전체 백업                    | 중요 문서, 설정, 소규모 데이터 |
| Incremental Backup  | 변경분만 백업                | 대용량 데이터                  |
| Differential Backup | 마지막 Full 이후 변경분 백업 | 중간 규모 데이터               |
| Snapshot            | 특정 시점 상태 저장          | VM, Volume, DB                 |
| Dump                | 논리적 데이터 추출           | MySQL, PostgreSQL              |
| File Sync           | 파일 동기화                  | 문서, 설정 파일                |

---

### [실무]

홈서버 추천 방식:

```text
RAG Documents
→ File Sync + Versioning

Database
→ Dump + 압축 + 암호화

Docker Volume
→ Stop or Snapshot 후 Archive

AnythingLLM Storage
→ Volume Backup or Directory Backup

System Config
→ Git Repository or Encrypted Archive

Cloud Backup
→ S3 / Object Storage Upload
```

---

### [FAQ]

Q. Full Backup은 언제 적합한가?

A.
데이터 크기가 작고 복구 단순성이 중요한 문서, 설정, 소규모 홈서버 데이터에 적합하다.

Q. Database는 파일 복사만 하면 되는가?

A.
권장하지 않는다. DB는 논리적 Dump나 Snapshot 등 일관성을 보장하는 방식이 필요하다.

---

# 9. Backup Schedule Rules

## 9.1 Backup Schedule 작성 규칙

### [개념]

Backup Schedule은 백업을 언제, 얼마나 자주 수행할지 정하는 기준이다.

백업 주기는 RPO와 데이터 변경 빈도에 맞춘다.

---

### [핵심]

필수 포함:

- Daily Backup
- Weekly Backup
- Monthly Backup
- Pre-deployment Backup
- Pre-upgrade Backup
- Retention
- Automation
- Backup Log

---

### [실무]

홈서버 백업 스케줄 예시:

```text
Daily
- RAG 문서
- DB Dump
- AnythingLLM Storage Metadata

Weekly
- Docker Volume Archive
- System Config
- Reverse Proxy Config

Monthly
- 전체 설정 백업
- 복구 테스트
- 오래된 백업 정리

Before Upgrade
- OS Update 전 백업
- Docker Compose 변경 전 백업
- AnythingLLM 업데이트 전 백업
```

---

### [Best Practice]

- 자동 백업을 우선한다.
- 백업 성공 / 실패 로그를 남긴다.
- 실패 알림을 설정한다.
- 백업 파일명을 날짜 기반으로 만든다.
- 오래된 백업 삭제 정책을 둔다.
- 배포 / 업데이트 전 수동 백업 절차를 둔다.

---

### [FAQ]

Q. 백업은 얼마나 자주 해야 하는가?

A.
데이터 변경 빈도와 허용 가능한 데이터 손실 시간인 RPO에 따라 정한다.

Q. 업데이트 전 백업이 필요한가?

A.
필요하다. OS, Docker, AnythingLLM, DB, Reverse Proxy 변경 전에는 복구 지점을 확보하는 것이 안전하다.

---

# 10. Retention / Versioning Rules

## 10.1 Retention / Versioning 작성 규칙

### [개념]

Retention은 백업을 얼마나 오래 보관할지 정하는 정책이다.

Versioning은 같은 데이터의 여러 버전을 보관하여 실수나 손상에 대비하는 방식이다.

---

### [핵심]

필수 포함:

- Retention Period
- Backup Version
- Rotation
- Lifecycle Rule
- Old Backup Cleanup
- Accidental Deletion Recovery

---

### [실무]

홈서버 Retention 예시:

```text
Daily Backup
→ 최근 7일 보관

Weekly Backup
→ 최근 4주 보관

Monthly Backup
→ 최근 6개월 보관

Critical Config
→ 장기 보관

Before Upgrade Backup
→ 변경 안정화 후 삭제
```

S3 사용 시:

- Versioning 활성화
- Lifecycle Rule 설정
- 오래된 버전 자동 정리
- 삭제 보호 정책 검토
- 비용 확인

---

### [주의]

백업을 무한 보관하면 저장 비용과 관리 복잡도가 증가한다.

너무 짧게 보관하면 뒤늦게 발견한 데이터 손상을 복구하지 못할 수 있다.

---

### [FAQ]

Q. Retention은 왜 필요한가?

A.
백업 보관 기간을 정해 복구 가능성과 저장 비용을 균형 있게 관리하기 위해 필요하다.

Q. Versioning은 왜 필요한가?

A.
실수로 파일을 덮어쓰거나 손상된 데이터가 백업되었을 때 이전 버전으로 복구하기 위해 필요하다.

---

# 11. Local Backup Rules

## 11.1 Local Backup 작성 규칙

### [개념]

Local Backup은 같은 홈서버 또는 같은 네트워크 안의 외장 디스크, NAS, 다른 PC에 백업을 저장하는 방식이다.

---

### [핵심]

필수 포함:

- External SSD
- NAS
- Local Directory
- Fast Restore
- Same-site Risk
- Disk Failure Risk

---

### [실무]

Local Backup 사용 사례:

- 빠른 복구
- 대용량 Docker Volume 백업
- 클라우드 업로드 전 임시 백업
- 월간 전체 백업
- 복구 테스트용 데이터 보관

예시 구조:

```text
/home/user/ai-server
→ /mnt/backup/ai-server-backup
→ External SSD or NAS
```

---

### [주의]

Local Backup은 빠르지만 같은 장소 재해에 취약하다.

위험:

- 화재
- 도난
- 전원 문제
- 랜섬웨어
- 실수로 같은 디스크 삭제
- 홈서버와 백업 디스크 동시 고장

---

### [FAQ]

Q. Local Backup만으로 충분한가?

A.
빠른 복구에는 좋지만 같은 장소 장애에 취약하다. 중요한 데이터는 Offsite Backup도 필요하다.

Q. 외장 SSD 백업은 좋은가?

A.
홈서버에서는 현실적인 좋은 선택이다. 다만 주기적 연결, 백업 검증, 분리 보관을 고려해야 한다.

---

# 12. Offsite Backup Rules

## 12.1 Offsite Backup 작성 규칙

### [개념]

Offsite Backup은 홈서버가 있는 장소와 다른 위치에 백업을 저장하는 방식이다.

Cloud Object Storage, 원격 NAS, 다른 집의 서버 등을 사용할 수 있다.

---

### [핵심]

필수 포함:

- Offsite Backup
- Cloud Storage
- Object Storage
- Remote Backup
- Encryption
- Network Transfer
- Restore Test

---

### [실무]

Offsite Backup 후보:

- AWS S3
- Cloudflare R2
- Google Cloud Storage
- Backblaze B2
- Naver Object Storage
- 원격 NAS
- 다른 PC / 서버

Offsite Backup Flow:

```text
Local Backup
→ Encrypt
→ Upload to Offsite Storage
→ Verify Checksum
→ Retention Policy
→ Restore Test
```

---

### [주의]

Offsite Backup은 업로드 비용, 다운로드 비용, 저장 비용, 복구 시간을 고려해야 한다.

민감 데이터는 업로드 전 암호화한다.

---

### [FAQ]

Q. Offsite Backup은 왜 필요한가?

A.
홈서버와 로컬 백업이 동시에 손상되는 상황에 대비하기 위해 필요하다.

Q. Cloud Storage에 백업할 때 가장 중요한 것은?

A.
암호화, 접근 권한 제한, Versioning, Lifecycle, Restore Test이다.

---

# 13. 3-2-1 Backup Rules

## 13.1 3-2-1 Backup 작성 규칙

### [개념]

3-2-1 Backup은 중요한 데이터를 안전하게 보호하기 위한 기본 백업 원칙이다.

의미:

- 3 copies
- 2 different media
- 1 offsite copy

---

### [핵심]

구조:

```text
3 Copies
→ Original + 2 Backups

2 Media
→ Internal SSD + External SSD or NAS

1 Offsite
→ Cloud Storage or Remote Location
```

---

### [실무]

홈서버 적용 예시:

```text
Original
→ Home Server SSD

Local Backup
→ External SSD or NAS

Offsite Backup
→ S3 / R2 / Remote Server
```

RAG 문서 적용 예시:

```text
Working Markdown Files
→ Git Repository
→ External SSD Backup
→ Cloud Object Storage Backup
```

---

### [FAQ]

Q. 3-2-1 Backup은 무엇인가?

A.
데이터를 총 3개 복사본, 2가지 매체, 1개 외부 위치에 보관하는 백업 원칙이다.

Q. 홈서버에도 3-2-1 Backup을 적용해야 하는가?

A.
중요 데이터에는 적용하는 것이 좋다. 특히 RAG 문서, DB, 설정 파일은 3-2-1 원칙에 가깝게 관리하는 것이 안전하다.

---

# 14. Docker Volume Backup Rules

## 14.1 Docker Volume Backup 작성 규칙

### [개념]

Docker Volume Backup은 Container가 사용하는 영속 데이터를 백업하는 작업이다.

Docker Container를 삭제해도 Named Volume 데이터는 남지만, Volume 자체를 삭제하면 데이터가 손실된다.

---

### [핵심]

필수 포함:

- Docker Volume
- Named Volume
- Bind Mount
- Container Stop
- Archive
- Consistency
- Restore
- Permission

---

### [실무]

Docker Volume 확인:

```bash
docker volume ls
```

Volume 백업 예시:

```bash
docker run --rm \
  -v volume_name:/data \
  -v $(pwd):/backup \
  alpine \
  tar czf /backup/volume_name_backup.tar.gz -C /data .
```

Volume 복구 예시:

```bash
docker run --rm \
  -v volume_name:/data \
  -v $(pwd):/backup \
  alpine \
  tar xzf /backup/volume_name_backup.tar.gz -C /data
```

---

### [주의]

DB가 실행 중인 Volume을 그대로 Archive하면 일관성 문제가 발생할 수 있다.

DB는 Dump 또는 Snapshot 방식을 우선한다.

Volume 백업 전 확인:

- Container 중지 가능 여부
- 데이터 일관성
- Permission
- Volume 이름
- 백업 파일 위치
- 복구 테스트

---

### [FAQ]

Q. Docker Volume은 왜 백업해야 하는가?

A.
Container 데이터, DB 파일, AnythingLLM Storage, Vector DB 데이터가 Volume에 저장될 수 있기 때문이다.

Q. 실행 중인 DB Volume을 tar로 백업해도 되는가?

A.
권장하지 않는다. 데이터 일관성이 깨질 수 있으므로 DB Dump나 안전한 Snapshot을 우선한다.

---

# 15. Docker Compose Backup Rules

## 15.1 Docker Compose Backup 작성 규칙

### [개념]

Docker Compose Backup은 Compose 파일, 환경 설정, Volume, Network 구조를 함께 기록하여 서비스를 재현 가능하게 만드는 백업 방식이다.

---

### [핵심]

필수 포함:

- compose.yml
- .env.example
- volume list
- image tag
- port mapping
- network
- bind mount path
- restore command

---

### [실무]

백업 대상:

```text
docker-compose.yml
compose.yml
.env.example
nginx.conf
volume backup
README_restore.md
image tag list
```

현재 Container / Image 기록:

```bash
docker ps
docker images
docker volume ls
docker network ls
```

Compose 서비스 재현 흐름:

```text
Install Docker
→ Copy compose files
→ Restore .env
→ Restore volumes
→ docker compose up -d
→ Health Check
```

---

### [주의]

`.env` 실제 파일은 Secret을 포함할 수 있다.

백업 시 암호화하거나 Secret Manager / Password Manager 사용을 고려한다.

---

### [FAQ]

Q. Docker Compose 백업에서 compose.yml만 있으면 충분한가?

A.
아니다. Volume 데이터, 환경 변수, Reverse Proxy 설정, Image Tag, 복구 절차도 필요하다.

Q. `.env` 파일은 백업해야 하는가?

A.
필요하지만 민감 정보가 포함될 수 있으므로 암호화하거나 안전한 Secret 저장소에 보관해야 한다.

---

# 16. Database Backup Rules

## 16.1 Database Backup 작성 규칙

### [개념]

Database Backup은 DB의 데이터를 논리적 Dump 또는 물리적 Snapshot으로 보관하는 작업이다.

---

### [핵심]

필수 포함:

- Database Dump
- Logical Backup
- Physical Backup
- Snapshot
- Consistency
- Transaction
- Restore Test
- Backup User

---

### [실무]

MySQL Dump 예시:

```bash
mysqldump -u backup_user -p database_name > database_name_backup.sql
```

PostgreSQL Dump 예시:

```bash
pg_dump -U backup_user -d database_name -F c -f database_name_backup.dump
```

SQLite 백업 예시:

```bash
sqlite3 app.db ".backup 'app_backup.db'"
```

DB 백업 Flow:

```text
Create Dump
→ Compress
→ Encrypt
→ Store
→ Verify
→ Restore Test
```

---

### [주의]

DB 백업은 복구 테스트가 필수이다.

백업 파일이 있어도 아래 문제가 있으면 복구 실패할 수 있다.

- 권한 부족
- Dump 손상
- 문자셋 문제
- Schema 불일치
- Version 불일치
- Partial Backup
- Secret 누락
- Storage 부족

---

### [FAQ]

Q. Database Backup은 왜 Dump 방식이 자주 사용되는가?

A.
논리적 데이터와 Schema를 추출하여 다른 환경에서도 비교적 쉽게 복구할 수 있기 때문이다.

Q. DB 백업에서 가장 중요한 검증은 무엇인가?

A.
백업 파일을 실제로 Restore해서 데이터가 정상적으로 복구되는지 확인하는 것이다.

---

# 17. Database Restore Rules

## 17.1 Database Restore 작성 규칙

### [개념]

Database Restore는 백업된 DB 데이터를 새 DB 또는 기존 DB에 복원하는 작업이다.

복구 전에는 원본 보호와 복구 대상 확인이 중요하다.

---

### [핵심]

필수 포함:

- Restore Target
- Backup File
- Schema
- User Permission
- Data Validation
- Application Connection
- Rollback Plan

---

### [실무]

MySQL Restore 예시:

```bash
mysql -u restore_user -p database_name < database_name_backup.sql
```

PostgreSQL Restore 예시:

```bash
pg_restore -U restore_user -d database_name database_name_backup.dump
```

SQLite Restore 예시:

```bash
cp app_backup.db app.db
```

Restore 검증:

- Table 목록 확인
- Row Count 확인
- 주요 데이터 조회
- Application 연결 확인
- Login / 핵심 API Smoke Test
- 권한 확인
- Encoding 확인

---

### [주의]

운영 DB에 바로 Restore하지 않는다.

권장 흐름:

```text
Restore to Test DB
→ Validate Data
→ Stop Application
→ Restore Production
→ Verify
→ Resume Service
```

---

### [FAQ]

Q. DB Restore는 바로 운영 DB에 해도 되는가?

A.
권장하지 않는다. 먼저 테스트 DB에 복구하여 백업 파일과 데이터 상태를 검증해야 한다.

Q. Restore 후 무엇을 확인해야 하는가?

A.
Table, Row Count, 주요 데이터, Application 연결, 핵심 기능 Smoke Test를 확인해야 한다.

---

# 18. Application Data Backup Rules

## 18.1 Application Data Backup 작성 규칙

### [개념]

Application Data Backup은 애플리케이션이 생성하거나 저장한 파일, 업로드 데이터, 메타데이터, 사용자 데이터를 백업하는 작업이다.

---

### [핵심]

필수 포함:

- Uploaded Files
- Application Storage
- Metadata
- User Data
- Generated Files
- Search Index
- Vector DB
- File Permission

---

### [실무]

백업 대상 예시:

- 업로드 이미지
- 첨부 파일
- 사용자 생성 문서
- AI 요약 결과
- Vector Database 파일
- Search Index
- Application Storage Directory
- AnythingLLM Storage Directory
- SQLite DB
- 설정 JSON

Application Data 백업 Flow:

```text
Stop Writes
→ Copy Data
→ Compress
→ Encrypt
→ Upload Backup
→ Verify
```

---

### [주의]

파일 데이터와 DB 메타데이터는 함께 맞아야 한다.

예:

- DB에는 이미지 경로가 있음
- 실제 이미지 파일은 누락됨
- 복구 후 화면에서 이미지 깨짐

---

### [FAQ]

Q. Application Data Backup은 DB Backup과 다른가?

A.
다르다. DB 외에도 업로드 파일, Storage Directory, Vector DB, 검색 인덱스 같은 파일 데이터가 있을 수 있다.

Q. 파일과 DB를 따로 백업해도 되는가?

A.
가능하지만 같은 시점의 데이터가 맞도록 백업 순서와 일관성을 고려해야 한다.

---

# 19. RAG Document Backup Rules

## 19.1 RAG Document Backup 작성 규칙

### [개념]

RAG Document Backup은 AI Agent가 참조하는 Markdown 문서, Domain Rules, Progress 문서, Retrieval 최적화 문서를 보호하는 작업이다.

---

### [핵심]

필수 포함:

- Markdown Documents
- Master Rules
- Domain Rules
- Project Progress
- Document Version
- Git Repository
- Cloud Backup
- Restore

---

### [실무]

백업 대상:

```text
Master_RAG_Rules.md
Project_Progress.md
Domain_Rules.md
Part Documents
SQL / Java / Spring / JPA / Security / DevOps 문서
Agent Prompt
제작 요청 프롬프트
검수 기록
```

추천 보관 방식:

```text
Working Directory
→ Git Repository
→ External SSD
→ Cloud Object Storage
```

파일명 기준:

```text
Domain_Part##_Topic.md
Project_Progress_vN.md
Backup_YYYYMMDD.tar.gz
```

---

### [주의]

RAG 문서는 모델보다 더 중요한 자산일 수 있다.

모델은 재다운로드 가능하지만 직접 제작한 RAG 문서는 재작성 비용이 크다.

---

### [FAQ]

Q. RAG 문서는 왜 백업 우선순위가 높은가?

A.
직접 제작한 지식 자산이고 Agent 성능에 직접 영향을 주며 재작성 비용이 크기 때문이다.

Q. RAG 문서는 Git에 올려도 되는가?

A.
민감 정보가 없다면 가능하다. 단, 개인 정보, API Key, 비공개 프로젝트 정보가 포함되면 Private Repository나 암호화 백업을 사용해야 한다.

---

# 20. AnythingLLM Backup Rules

## 20.1 AnythingLLM Backup 작성 규칙

### [개념]

AnythingLLM Backup은 AnythingLLM의 Storage, Workspace, 업로드 문서, Vector DB 관련 데이터를 복구 가능하게 보관하는 작업이다.

---

### [핵심]

필수 포함:

- AnythingLLM Storage
- Workspace Data
- Uploaded Documents
- Vector Store
- SQLite / Metadata
- Docker Volume
- Restore Procedure

---

### [실무]

AnythingLLM 백업 대상:

- `/app/storage`
- Docker named volume
- uploaded documents
- workspace metadata
- local database
- vector database files
- custom settings

Docker 기준 확인:

```bash
docker volume ls
docker inspect anythingllm
```

백업 흐름:

```text
Stop AnythingLLM
→ Backup Storage Volume
→ Backup Compose File
→ Backup Environment
→ Start AnythingLLM
→ Verify Backup File
```

---

### [주의]

AnythingLLM Storage는 Agent / RAG 운영 상태와 직접 연결된다.

업로드 문서 원본과 AnythingLLM 내부 Storage를 모두 관리하는 것이 안전하다.

---

### [FAQ]

Q. AnythingLLM은 무엇을 백업해야 하는가?

A.
Storage Volume, Workspace Metadata, 업로드 문서, Vector Store, 설정 파일을 백업해야 한다.

Q. AnythingLLM 백업 전 Container를 멈춰야 하는가?

A.
가능하면 중지 후 백업하는 것이 안전하다. 실행 중 백업은 데이터 일관성 문제가 생길 수 있다.

---

# 21. Configuration Backup Rules

## 21.1 Configuration Backup 작성 규칙

### [개념]

Configuration Backup은 서버와 서비스 재현에 필요한 설정 파일을 백업하는 작업이다.

데이터가 있어도 설정이 없으면 복구 시간이 길어진다.

---

### [핵심]

필수 포함:

- Docker Compose
- Environment File
- Nginx Config
- Reverse Proxy Config
- Firewall Rule
- Cron Job
- Systemd Service
- SSH Config
- Backup Script

---

### [실무]

홈서버 설정 백업 대상:

```text
compose.yml
.env.example
nginx.conf
Caddyfile
traefik.yml
ufw status 기록
crontab
backup.sh
restore.md
system package list
installed docker version
domain / DNS notes
port mapping notes
```

설치 패키지 기록:

```bash
apt list --installed > installed_packages.txt
```

Crontab 백업:

```bash
crontab -l > crontab_backup.txt
```

---

### [주의]

실제 `.env` 파일과 Private Key는 민감 정보이다.

암호화 백업 또는 별도 Secret 관리가 필요하다.

---

### [FAQ]

Q. 설정 파일 백업이 왜 중요한가?

A.
데이터가 있어도 Docker, Reverse Proxy, 방화벽, 환경 변수 설정이 없으면 서비스를 빠르게 복구하기 어렵기 때문이다.

Q. `.env.example`과 `.env`는 어떻게 다르게 관리해야 하는가?

A.
`.env.example`은 구조 공유용이고 `.env`는 Secret을 포함할 수 있으므로 암호화하거나 안전하게 보관해야 한다.

---

# 22. Secret Backup Rules

## 22.1 Secret Backup 작성 규칙

### [개념]

Secret Backup은 Password, API Key, Token, Private Key 같은 민감 정보를 안전하게 복구 가능하게 관리하는 기준이다.

Secret은 일반 백업과 다르게 접근 권한과 암호화가 중요하다.

---

### [핵심]

필수 포함:

- Secret
- Password Manager
- Secret Manager
- Encrypted Backup
- Access Control
- Recovery Key
- Rotation
- Revocation

---

### [실무]

Secret 관리 대상:

- DB Password
- JWT Secret
- API Key
- OAuth Client Secret
- Cloud Access Key
- SSH Private Key
- TLS Private Key
- Webhook Secret
- Admin Password

권장 방식:

```text
Password Manager
or
Secret Manager
or
Encrypted Archive
```

백업 원칙:

- 평문 Secret 파일 금지
- 백업 파일 암호화
- 접근 권한 최소화
- 복구용 Master Key 보호
- Secret 노출 시 Rotation 절차 포함

---

### [주의]

Secret 백업을 잃어버리면 복구가 어렵다.

Secret 백업이 노출되면 침해 사고가 될 수 있다.

따라서 가용성과 보안을 동시에 고려해야 한다.

---

### [FAQ]

Q. Secret도 백업해야 하는가?

A.
필요하다. 하지만 평문 파일로 백업하지 말고 Password Manager, Secret Manager, 암호화 백업을 사용해야 한다.

Q. Secret 백업이 노출되면 어떻게 해야 하는가?

A.
즉시 해당 Secret을 폐기하고 재발급하며 사용 이력과 접근 로그를 확인해야 한다.

---

# 23. Backup Security Rules

## 23.1 Backup Security 작성 규칙

### [개념]

Backup Security는 백업 데이터가 유출, 변조, 삭제되지 않도록 보호하는 기준이다.

백업에는 운영 데이터와 Secret이 포함될 수 있다.

---

### [핵심]

필수 포함:

- Encryption
- Access Control
- Backup Integrity
- Immutable Backup
- Retention Lock
- Audit Log
- Least Privilege
- Secure Deletion

---

### [실무]

Backup Security Checklist:

- 백업 파일 암호화
- 백업 저장소 접근 권한 제한
- 백업 업로드 전 Checksum 생성
- 백업 다운로드 / 삭제 Audit Log 확인
- Cloud Storage Public Access 차단
- 백업 Retention 설정
- 중요 백업 Versioning 활성화
- 삭제 권한 분리
- Secret 포함 여부 확인
- 복구용 Key 안전 보관

---

### [주의]

백업 저장소가 침해되면 운영 데이터 전체가 유출될 수 있다.

Cloud Storage Backup에서는 Public Access와 IAM 권한을 반드시 검토한다.

---

### [FAQ]

Q. 백업도 암호화해야 하는가?

A.
중요 데이터나 Secret이 포함될 수 있으므로 암호화하는 것이 안전하다.

Q. 백업 저장소 권한은 어떻게 관리해야 하는가?

A.
업로드, 다운로드, 삭제 권한을 최소화하고 필요하면 삭제 권한을 별도로 제한해야 한다.

---

# 24. Backup Verification Rules

## 24.1 Backup Verification 작성 규칙

### [개념]

Backup Verification은 백업 파일이 정상 생성되었고 손상되지 않았으며 복구 가능한지 확인하는 절차이다.

---

### [핵심]

필수 포함:

- Backup Success Check
- File Size Check
- Checksum
- Integrity Check
- Restore Validation
- Backup Log
- Alert

---

### [실무]

검증 항목:

- 백업 파일 존재 여부
- 파일 크기 0 여부
- 압축 파일 무결성
- Checksum 비교
- 업로드 성공 여부
- 백업 로그 확인
- 복구 테스트 여부
- 오래된 백업 삭제 여부

압축 파일 확인 예시:

```bash
tar tzf backup.tar.gz > /dev/null
```

Checksum 생성 예시:

```bash
sha256sum backup.tar.gz > backup.tar.gz.sha256
```

---

### [주의]

백업 명령이 성공했어도 실제 파일이 손상되었거나 비어 있을 수 있다.

백업 성공 로그만 믿지 않는다.

---

### [FAQ]

Q. Backup Verification은 왜 필요한가?

A.
백업 파일이 실제로 존재하고 손상되지 않았으며 복구 가능한지 확인하기 위해 필요하다.

Q. 백업 성공 로그가 있으면 충분한가?

A.
아니다. 파일 크기, 무결성, Restore Test까지 확인해야 안전하다.

---

# 25. Restore Test Rules

## 25.1 Restore Test 작성 규칙

### [개념]

Restore Test는 백업 파일로 실제 복구가 가능한지 테스트 환경에서 검증하는 절차이다.

백업의 가치는 복구 성공으로 판단한다.

---

### [핵심]

필수 포함:

- Restore Test
- Test Environment
- Data Validation
- Application Smoke Test
- Recovery Time Measurement
- Restore Runbook
- Verification

---

### [실무]

Restore Test Flow:

```text
Prepare Test Environment
→ Download Backup
→ Decrypt
→ Restore Data
→ Start Service
→ Validate Data
→ Run Smoke Test
→ Record Result
```

검증 항목:

- DB 복구 성공
- Volume 복구 성공
- Application 실행
- 로그인 가능
- 문서 조회 가능
- RAG 검색 가능
- 파일 업로드 데이터 존재
- 설정 정상 반영
- 예상 RTO 내 복구 가능 여부

---

### [주의]

복구 테스트를 하지 않은 백업은 신뢰할 수 없다.

운영 장애 시 처음 복구를 시도하면 절차 오류로 복구 시간이 길어진다.

---

### [FAQ]

Q. Restore Test는 얼마나 자주 해야 하는가?

A.
중요 데이터는 월 1회 또는 큰 변경 전후에 수행하는 것이 좋다. 개인 홈서버는 최소 분기별 테스트를 권장한다.

Q. 복구 테스트에서 가장 중요한 것은?

A.
서비스가 실제로 실행되고 핵심 데이터와 기능이 정상인지 확인하는 것이다.

---

# 26. Recovery Runbook Rules

## 26.1 Recovery Runbook 작성 규칙

### [개념]

Recovery Runbook은 장애 발생 시 어떤 순서로 복구해야 하는지 정리한 실행 절차 문서이다.

---

### [핵심]

필수 포함:

- Failure Scenario
- Impact
- Backup Location
- Restore Command
- Validation
- Rollback
- Owner
- Estimated RTO

---

### [실무]

Runbook 기본 구조:

```text
Scenario:
Impact:
Backup Location:
Required Secrets:
Recovery Steps:
Validation:
Rollback:
Owner:
Expected RTO:
Last Tested:
```

홈서버 복구 Runbook 예시 대상:

- Docker Volume 복구
- DB 복구
- AnythingLLM 복구
- Ubuntu 재설치 후 서비스 복구
- S3 백업에서 복원
- 외장 SSD에서 복원
- Secret 노출 후 재발급
- 도메인 / HTTPS 복구

---

### [FAQ]

Q. Recovery Runbook은 왜 필요한가?

A.
장애 상황에서 기억에 의존하지 않고 빠르게 일관된 절차로 복구하기 위해 필요하다.

Q. Runbook에는 무엇이 들어가야 하는가?

A.
장애 시나리오, 백업 위치, 복구 명령, 검증 방법, 필요한 Secret, 예상 복구 시간을 포함해야 한다.

---

# 27. Home Server Disaster Recovery Rules

## 27.1 Home Server DR 작성 규칙

### [개념]

Home Server Disaster Recovery는 개인 서버 장애 시 데이터를 복구하고 서비스를 다시 실행하기 위한 현실적인 복구 전략이다.

---

### [핵심]

필수 포함:

- Home Server
- Ubuntu Reinstall
- Docker Reinstall
- Compose Restore
- Volume Restore
- DNS Restore
- Backup Download
- Smoke Test

---

### [실무]

홈서버 전체 복구 Flow:

```text
Install Ubuntu
→ Install Docker
→ Restore Project Directory
→ Restore compose.yml
→ Restore .env / Secrets
→ Restore Docker Volumes
→ docker compose up -d
→ Check Logs
→ Health Check
→ Verify RAG / Application
```

복구 준비물:

- Ubuntu 설치 USB
- Docker 설치 명령 기록
- Git Repository 주소
- Backup Storage 접근 정보
- Secret 복구 방법
- External SSD 또는 Cloud Backup
- 네트워크 설정 기록
- 도메인 / DNS 기록

---

### [주의]

홈서버 복구에서 가장 오래 걸리는 것은 명령어보다 “무엇을 어디에 저장했는지 기억하는 것”이다.

따라서 백업 위치와 복구 순서를 문서화한다.

---

### [FAQ]

Q. 홈서버 전체 장애 시 무엇부터 복구해야 하는가?

A.
OS와 Docker 실행 환경을 먼저 만들고, Compose 설정과 Volume 데이터를 복구한 뒤 서비스를 실행하고 검증한다.

Q. 홈서버 DR에서 가장 중요한 준비물은?

A.
백업 파일, 복구 절차 문서, Secret 복구 방법, Docker Compose 설정, 네트워크 / 도메인 기록이다.

---

# 28. Cloud Object Storage Backup Rules

## 28.1 Cloud Object Storage Backup 작성 규칙

### [개념]

Cloud Object Storage Backup은 S3 같은 Object Storage에 백업 파일을 저장하여 Offsite Backup을 구성하는 방식이다.

---

### [핵심]

필수 포함:

- S3
- Object Storage
- Bucket
- Versioning
- Lifecycle
- Encryption
- Access Policy
- Upload
- Restore

---

### [실무]

S3 백업 Flow:

```text
Create Backup Archive
→ Encrypt
→ Upload to S3
→ Verify Upload
→ Apply Lifecycle
→ Restore Test
```

S3 저장 구조 예시:

```text
s3://my-home-backup/
  rag-docs/
  database/
  docker-volumes/
  anythingllm/
  config/
```

백업 파일명 예시:

```text
anythingllm_2026-06-29.tar.gz
mysql_2026-06-29.sql.gz
rag_docs_2026-06-29.tar.gz
```

---

### [주의]

S3 Bucket은 Public Access를 차단한다.

권장 설정:

- Public Access Block
- Server-side Encryption
- Versioning
- Lifecycle Rule
- 최소 권한 IAM
- MFA Delete 검토
- Billing Alert

---

### [FAQ]

Q. Cloud Object Storage는 백업에 왜 좋은가?

A.
홈서버와 물리적으로 분리된 위치에 데이터를 보관할 수 있고 Versioning, Lifecycle, 암호화 설정을 적용할 수 있기 때문이다.

Q. S3 백업에서 가장 중요한 보안 설정은?

A.
Public Access 차단, 암호화, 최소 권한 IAM, Versioning, 삭제 보호이다.

---

# 29. Monitoring / Alerting Rules

## 29.1 Backup Monitoring 작성 규칙

### [개념]

Backup Monitoring은 백업 작업이 성공했는지, 실패했는지, 오래된 백업만 남아 있는지 감시하는 체계이다.

---

### [핵심]

필수 포함:

- Backup Job Status
- Last Backup Time
- Backup Failure Alert
- Backup Size
- Backup Age
- Restore Test Status
- Notification

---

### [실무]

모니터링 대상:

- 마지막 백업 시각
- 백업 성공 여부
- 백업 파일 크기
- 업로드 성공 여부
- 백업 파일 개수
- 저장소 남은 용량
- 오래된 백업 여부
- Restore Test 마지막 수행일
- 백업 실패 로그

Alert 조건 예시:

```text
Daily Backup Missing
→ Warning

Backup Failed
→ Critical

Backup File Size 0
→ Critical

No Restore Test for 90 Days
→ Warning
```

---

### [FAQ]

Q. Backup Monitoring은 왜 필요한가?

A.
백업이 실패했는데 모르면 장애 발생 시 복구할 수 없기 때문이다.

Q. 백업 알림에서 가장 중요한 조건은?

A.
백업 실패, 백업 누락, 파일 크기 0, 오래된 백업, 저장소 용량 부족이다.

---

# 30. Backup Before Change Rules

## 30.1 변경 전 백업 규칙

### [개념]

Backup Before Change는 시스템 변경 전에 복구 지점을 확보하는 안전 절차이다.

배포, 업데이트, 마이그레이션, 설정 변경 전에 수행한다.

---

### [핵심]

필수 포함:

- Pre-deployment Backup
- Pre-upgrade Backup
- Pre-migration Backup
- Config Backup
- Rollback Point
- Validation

---

### [실무]

변경 전 백업이 필요한 작업:

- OS Update
- Docker Upgrade
- AnythingLLM Update
- Database Migration
- Docker Compose 변경
- Reverse Proxy 설정 변경
- Volume 구조 변경
- RAG 문서 대량 변경
- Storage 경로 변경
- Cloud Sync 설정 변경

변경 전 Flow:

```text
Backup Current State
→ Verify Backup
→ Apply Change
→ Test
→ Keep or Rollback
```

---

### [주의]

변경 후 문제가 생겼을 때 “변경 직전 백업”이 없으면 복구가 어려워진다.

특히 DB Migration 전 백업은 필수이다.

---

### [FAQ]

Q. 배포 전 백업은 항상 필요한가?

A.
데이터 구조 변경, DB Migration, Volume 변경, 운영 설정 변경이 포함되면 강하게 권장된다.

Q. 단순 코드 배포에도 백업이 필요한가?

A.
Stateless 코드 배포만이면 필수는 아니지만 Rollback 가능한 Image Tag와 설정 백업은 필요하다.

---

# 31. Disaster Scenario Rules

## 31.1 장애 시나리오 작성 규칙

### [개념]

Disaster Scenario는 어떤 장애가 발생했을 때 어떤 데이터와 서비스가 영향을 받는지 정의하는 기준이다.

---

### [핵심]

필수 포함:

- Failure Type
- Impact
- Detection
- Recovery Source
- Recovery Step
- Validation
- Expected RTO

---

### [실무]

대표 장애 시나리오:

| 시나리오               | 영향             | 복구 기준                  |
| ---------------------- | ---------------- | -------------------------- |
| Docker Container 종료  | 서비스 중단      | Container 재시작           |
| Docker Volume 삭제     | 데이터 손실      | Volume Restore             |
| DB 손상                | Application 장애 | DB Restore                 |
| RAG 문서 삭제          | Agent 품질 저하  | 문서 Backup Restore        |
| SSD 고장               | 전체 서버 장애   | OS 재설치 + Backup Restore |
| Secret 노출            | 보안 사고        | Secret Rotation            |
| Cloud Backup 접근 실패 | 복구 지연        | Local Backup 사용          |
| 도메인 장애            | 외부 접속 불가   | DNS / Tunnel 점검          |

---

### [FAQ]

Q. 장애 시나리오는 왜 미리 작성해야 하는가?

A.
장애 발생 시 영향 범위와 복구 절차를 빠르게 판단하기 위해 필요하다.

Q. 홈서버에서 가장 현실적인 장애 시나리오는?

A.
Docker Volume 손실, SSD 고장, OS 설정 문제, DB 손상, 외부 접속 문제, 백업 실패이다.

---

# 32. Troubleshooting Rules

## 32.1 Backup / DR Troubleshooting 작성 규칙

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

- Backup Failed
- Restore Failed
- Backup File Missing
- Backup File Corrupted
- Permission Denied
- Disk Full
- S3 Upload Failed
- S3 Access Denied
- Docker Volume Restore Failed
- Database Restore Failed
- Secret Missing
- Restore Data Inconsistent
- Backup Too Old
- Backup Not Encrypted
- Restore Test Failed

---

### [실무]

기본 확인 흐름:

```text
Failure Message
→ Backup Log
→ Storage Capacity
→ Permission
→ File Integrity
→ Encryption Key
→ Restore Target
→ Service Log
```

---

### [Troubleshooting]

문제:
백업 파일이 생성되지 않는다.

원인:

- 권한 부족
- 대상 경로 오류
- 디스크 용량 부족
- Cron 실행 실패
- Container 이름 오류
- 백업 Script 오류

해결:

```text
Backup Log 확인
→ Path 확인
→ Permission 확인
→ Disk 용량 확인
→ Script 수동 실행
→ Cron 로그 확인
```

문제:
S3 업로드가 실패한다.

원인:

- IAM 권한 부족
- Bucket 이름 오류
- Region 오류
- Network 장애
- Credential 만료
- 파일 크기 / 정책 제한

해결:

```text
IAM Policy 확인
→ Bucket / Region 확인
→ Credential 확인
→ Network 확인
→ CloudTrail 확인
```

문제:
DB Restore가 실패한다.

원인:

- DB Version 불일치
- 권한 부족
- Dump 파일 손상
- 대상 DB 미생성
- 문자셋 문제
- Storage 부족

해결:

```text
Dump 무결성 확인
→ DB Version 확인
→ 대상 DB 생성
→ 권한 확인
→ Test DB에 먼저 Restore
```

문제:
복구 후 데이터가 일부 누락된다.

원인:

- 오래된 백업 사용
- DB와 파일 백업 시점 불일치
- Incremental Backup 누락
- Volume 일부만 백업
- 업로드 파일 누락

해결:

```text
Backup Timestamp 확인
→ Backup 대상 확인
→ DB / File 일관성 확인
→ 다른 Backup Version 확인
→ 백업 범위 수정
```

---

### [FAQ]

Q. 백업 실패 시 가장 먼저 확인할 것은?

A.
백업 로그, 경로, 권한, 디스크 용량, 백업 대상 존재 여부를 먼저 확인한다.

Q. Restore 실패 시 가장 먼저 확인할 것은?

A.
백업 파일 무결성, 대상 환경, 권한, Version 호환성, Secret 존재 여부를 확인한다.

Q. 복구 후 데이터가 안 맞으면 무엇을 확인해야 하는가?

A.
DB 백업 시점과 파일 백업 시점이 일치하는지, 백업 대상이 누락되지 않았는지 확인해야 한다.

---

# 33. Common Mistakes

## 33.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Review Agent가 Backup / Disaster Recovery 구성을 검토할 때 우선 탐지해야 하는 위험 패턴이다.

---

### [핵심]

자주 발생:

- 백업 없음
- 복구 테스트 없음
- 같은 디스크에만 백업
- Docker Volume 백업 누락
- DB를 파일 복사로만 백업
- `.env` 평문 백업
- Secret 백업 미관리
- S3 Bucket Public Access
- 백업 암호화 누락
- 백업 성공 여부 미확인
- 백업 파일 크기 0 방치
- 오래된 백업만 존재
- Retention 정책 없음
- Versioning 없음
- 백업 위치 문서화 없음
- 복구 절차 문서 없음
- 업데이트 전 백업 누락
- Cloud 비용 알림 없음
- 복구에 필요한 Secret 분실

---

### [실무]

Review Agent 검토 기준:

```text
Backup Target
→ Backup Method
→ Backup Schedule
→ Backup Storage
→ Encryption
→ Retention
→ Restore Test
→ Recovery Runbook
→ Monitoring
```

---

### [FAQ]

Q. Backup / DR Review에서 가장 먼저 확인할 것은?

A.
백업 대상, 백업 저장 위치, 복구 테스트 여부, 암호화, Retention, 복구 절차 문서를 먼저 확인한다.

Q. 백업에서 가장 위험한 착각은?

A.
백업 파일이 있다는 이유만으로 복구 가능하다고 믿는 것이다. Restore Test가 없으면 신뢰할 수 없다.

---

# 34. File Relationship Rules

## 34.1 다른 Domain Rules와 연계

### [개념]

Backup / Disaster Recovery Domain Rules는 DevOps Expert 문서 체계에서 Cloud Provider, Docker Advanced, Infrastructure as Code, Deployment Strategy, Monitoring & Logging, Security Operations와 연결된다.

---

### [핵심]

연계 구조:

```text
Backup / Disaster Recovery
→ Docker Volume
→ Database
→ Cloud Object Storage
→ Monitoring
→ Security
→ Recovery Runbook
```

---

### [실무]

파일 간 역할 분리:

| Domain                     | 역할                                                                |
| -------------------------- | ------------------------------------------------------------------- |
| Backup / Disaster Recovery | 백업, 복구, RPO / RTO, Restore Test, DR Runbook                     |
| Cloud Provider             | S3 / Object Storage, Snapshot, Backup Storage                       |
| Docker Advanced            | Docker Volume, Compose, Container Data                              |
| Infrastructure as Code     | Backup Resource Provisioning, State Backup                          |
| Deployment Strategy        | 배포 전 백업, Rollback, Migration 안전성                            |
| Monitoring & Logging       | Backup Job Monitoring, Alerting, Restore Verification               |
| Security Operations        | Backup Encryption, Access Control, Secret Backup, Incident Recovery |

---

### [FAQ]

Q. Backup / DR과 Cloud Provider는 어떻게 연결되는가?

A.
S3 같은 Object Storage, Snapshot, Cloud Backup Storage, Offsite Backup 구성에서 연결된다.

Q. Backup / DR과 Docker Advanced는 어떻게 연결되는가?

A.
Docker Volume, Compose 설정, Container 데이터 복구에서 연결된다.

Q. Backup / DR과 Security Operations는 어떻게 연결되는가?

A.
백업 암호화, 접근 권한, Secret 보호, 보안 사고 후 복구에서 연결된다.

---

# 35. Retrieval Optimization Rules

## 35.1 Retrieval 최적화 규칙

### [개념]

Backup / Disaster Recovery 문서는 데이터 손실과 복구 문제 상황 검색에 강해야 한다.

사용자 질문은 주로 Docker Volume 삭제, DB 복구, S3 백업, 홈서버 SSD 고장, AnythingLLM 복구, RAG 문서 백업 형태로 들어온다.

---

### [핵심]

강조 대상:

- Backup
- Restore
- Disaster Recovery
- RPO
- RTO
- Docker Volume Backup
- Database Backup
- Database Restore
- AnythingLLM Backup
- RAG Document Backup
- Home Server Backup
- S3 Backup
- Offsite Backup
- Restore Test
- Recovery Runbook
- Backup Encryption
- Retention

---

### [실무]

반복 허용 키워드:

- 홈서버 백업
- 홈서버 복구
- Docker Volume 백업
- Docker Volume 복구
- DB 백업
- DB 복구
- AnythingLLM 백업
- RAG 문서 백업
- S3 백업
- Offsite Backup
- Restore Test
- 백업 암호화
- 백업 실패
- 복구 실패
- SSD 고장 복구
- Ubuntu 재설치 복구
- Disaster Recovery Runbook

---

### [FAQ]

Q. Backup / DR RAG 문서는 어떤 질문에 강해야 하는가?

A.
홈서버 백업, Docker Volume 복구, DB 복구, S3 백업, RAG 문서 백업, AnythingLLM 복구, Restore Test 질문에 강해야 한다.

Q. Retrieval을 위해 어떤 키워드를 반복해야 하는가?

A.
Backup, Restore, Disaster Recovery, Docker Volume, Database Backup, S3 Backup, Home Server, Restore Test, RPO, RTO 키워드를 반복할 수 있다.

---

# 36. Version Rules

## 36.1 버전 기준

### [개념]

Backup / Disaster Recovery 문서는 Modern Home Server / DevOps Backup 기준으로 작성한다.

---

### [핵심]

기준:

- Docker Volume Backup
- Database Dump
- Cloud Object Storage Offsite Backup
- 3-2-1 Backup
- Backup Encryption
- Restore Test
- Recovery Runbook
- Backup Monitoring
- Home Server Hybrid
- RPO / RTO 기반 우선순위

---

### [실무]

Legacy 또는 낮은 우선순위:

- 같은 폴더에 복사만 하는 백업
- 복구 테스트 없는 백업
- DB 파일 강제 복사만 의존
- Secret 평문 백업
- 수동 백업만 의존
- 백업 로그 없음
- 백업 실패 알림 없음
- Retention 없는 무한 보관
- Offsite Backup 없음
- 복구 절차 미문서화

---

### [FAQ]

Q. Backup / DR 문서에서 Modern 기준은 무엇인가?

A.
Docker Volume, DB Dump, Cloud Offsite Backup, 암호화, Retention, Restore Test, Recovery Runbook을 포함하는 것이다.

Q. 수동 복사만으로 백업해도 되는가?

A.
소규모 문서에는 가능하지만 DB, Docker Volume, 운영 데이터는 일관성, 자동화, 복구 테스트가 필요하다.

---

# 37. Quality Checklist

## 37.1 최종 검수 기준

### [개념]

Backup / Disaster Recovery RAG 문서는 Agent가 데이터 손실에 대비하고 복구 절차를 설계할 수 있도록 검수한다.

---

### [핵심]

검수 항목:

- MASTER_RAG_RULES 구조 준수
- Backup / DR Scope 충족
- Home Server Backup 포함
- Docker Volume Backup 포함
- Database Backup / Restore 포함
- AnythingLLM Backup 포함
- RAG Document Backup 포함
- Cloud Object Storage Backup 포함
- RPO / RTO 포함
- Retention / Versioning 포함
- Backup Security 포함
- Restore Test 포함
- Recovery Runbook 포함
- Monitoring / Alerting 포함
- Troubleshooting 포함
- Cloud Provider Domain Rules와 연결
- Docker Advanced Domain Rules와 연결
- Monitoring & Logging Domain Rules와 연결
- Security Operations Domain Rules와 연결
- FAQ 포함
- Retrieval Queries 포함
- Secret 평문 백업 금지 강조
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

Q. Backup / DR 문서 품질은 무엇으로 판단하는가?

A.
Agent가 백업 대상 식별, 백업 전략 설계, 복구 절차 작성, Restore Test, 장애 복구 판단을 수행할 수 있으면 품질이 높다.

---

# 38. Final Goal

## 38.1 최종 목표

### [개념]

Backup / Disaster Recovery RAG 문서는 단순 백업 명령어 모음이 아니다.

DevOps Agent / Backend Agent / Review Agent가 홈서버와 운영 시스템의 데이터를 보호하고 장애 발생 시 복구를 수행하기 위한 실행 지식 문서이다.

---

### [핵심]

Agent 수행 목표:

- Retrieve Backup Workflow
- Identify Backup Targets
- Design Home Server Backup
- Backup Docker Volumes
- Backup Databases
- Backup RAG Documents
- Backup AnythingLLM Storage
- Use Cloud Object Storage
- Define RPO / RTO
- Review Backup Security
- Perform Restore Test
- Write Recovery Runbook
- Troubleshoot Backup / Restore Failure

---

### [실무]

최종 연결 흐름:

```text
Home Server / Application
→ Backup Target
→ Local Backup
→ Offsite Cloud Backup
→ Verification
→ Restore Test
→ Disaster Recovery Runbook
→ Service Recovery
```

---

### [FAQ]

Q. Backup / Disaster Recovery 문서의 최종 목적은?

A.
Agent가 홈서버와 운영 시스템의 중요 데이터를 백업하고, 장애 발생 시 실제 복구 가능한 절차를 설계하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Backup / Disaster Recovery Domain Rules는 무엇인가?
A. DevOps Agent, Backend Agent, Review Agent가 백업, 복구, RPO / RTO, Restore Test, DR Runbook을 수행하기 위한 RAG 작성 규칙이다.

Q. Backup / DR 문서의 핵심 범위는?
A. Backup, Restore, Disaster Recovery, RPO, RTO, Docker Volume Backup, Database Backup, Home Server Backup, Cloud Offsite Backup, Restore Test이다.

Q. 홈서버 개인 프로젝트에도 Backup / DR 문서가 필요한가?
A. 필요하다. SSD 고장, Docker Volume 삭제, OS 문제, 설정 파일 유실, RAG 문서 손실에 대비하기 위해 중요하다.

Q. Backup과 Disaster Recovery는 무엇이 다른가?
A. Backup은 데이터를 보관하는 것이고 Disaster Recovery는 장애 후 서비스와 데이터를 복구하는 전체 절차이다.

Q. Backup의 핵심은 무엇인가?
A. 중요 데이터를 별도 위치에 보관하고 실제로 복구 가능한 상태인지 검증하는 것이다.

Q. Disaster Recovery는 무엇인가?
A. 장애 발생 후 서비스와 데이터를 복구하기 위한 계획, 절차, 검증 활동이다.

Q. RPO는 무엇인가?
A. 장애 발생 시 어느 시점까지의 데이터 손실을 허용할지 정하는 목표이다.

Q. RTO는 무엇인가?
A. 장애 발생 후 서비스를 얼마나 빨리 복구해야 하는지 정하는 목표이다.

Q. 홈서버에서 가장 먼저 백업해야 하는 것은?
A. 직접 만든 RAG 문서, DB 데이터, Docker Volume, 설정 파일, 복구 절차 문서이다.

Q. Ollama 모델도 반드시 백업해야 하는가?
A. 재다운로드 가능하면 우선순위는 낮다. 대신 모델 이름, 태그, pull 명령, 설정 파일은 기록해두는 것이 좋다.

Q. Full Backup은 언제 적합한가?
A. 데이터 크기가 작고 복구 단순성이 중요한 문서, 설정, 소규모 홈서버 데이터에 적합하다.

Q. Database는 파일 복사만 하면 되는가?
A. 권장하지 않는다. DB는 논리적 Dump나 Snapshot 등 일관성을 보장하는 방식이 필요하다.

Q. 백업은 얼마나 자주 해야 하는가?
A. 데이터 변경 빈도와 허용 가능한 데이터 손실 시간인 RPO에 따라 정한다.

Q. 업데이트 전 백업이 필요한가?
A. 필요하다. OS, Docker, AnythingLLM, DB, Reverse Proxy 변경 전에는 복구 지점을 확보하는 것이 안전하다.

Q. Retention은 왜 필요한가?
A. 백업 보관 기간을 정해 복구 가능성과 저장 비용을 균형 있게 관리하기 위해 필요하다.

Q. Versioning은 왜 필요한가?
A. 실수로 파일을 덮어쓰거나 손상된 데이터가 백업되었을 때 이전 버전으로 복구하기 위해 필요하다.

Q. Local Backup만으로 충분한가?
A. 빠른 복구에는 좋지만 같은 장소 장애에 취약하다. 중요한 데이터는 Offsite Backup도 필요하다.

Q. Offsite Backup은 왜 필요한가?
A. 홈서버와 로컬 백업이 동시에 손상되는 상황에 대비하기 위해 필요하다.

Q. 3-2-1 Backup은 무엇인가?
A. 데이터를 총 3개 복사본, 2가지 매체, 1개 외부 위치에 보관하는 백업 원칙이다.

Q. Docker Volume은 왜 백업해야 하는가?
A. Container 데이터, DB 파일, AnythingLLM Storage, Vector DB 데이터가 Volume에 저장될 수 있기 때문이다.

Q. 실행 중인 DB Volume을 tar로 백업해도 되는가?
A. 권장하지 않는다. 데이터 일관성이 깨질 수 있으므로 DB Dump나 안전한 Snapshot을 우선한다.

Q. Docker Compose 백업에서 compose.yml만 있으면 충분한가?
A. 아니다. Volume 데이터, 환경 변수, Reverse Proxy 설정, Image Tag, 복구 절차도 필요하다.

Q. `.env` 파일은 백업해야 하는가?
A. 필요하지만 민감 정보가 포함될 수 있으므로 암호화하거나 안전한 Secret 저장소에 보관해야 한다.

Q. Database Backup은 왜 Dump 방식이 자주 사용되는가?
A. 논리적 데이터와 Schema를 추출하여 다른 환경에서도 비교적 쉽게 복구할 수 있기 때문이다.

Q. DB 백업에서 가장 중요한 검증은 무엇인가?
A. 백업 파일을 실제로 Restore해서 데이터가 정상적으로 복구되는지 확인하는 것이다.

Q. DB Restore는 바로 운영 DB에 해도 되는가?
A. 권장하지 않는다. 먼저 테스트 DB에 복구하여 백업 파일과 데이터 상태를 검증해야 한다.

Q. Application Data Backup은 DB Backup과 다른가?
A. 다르다. DB 외에도 업로드 파일, Storage Directory, Vector DB, 검색 인덱스 같은 파일 데이터가 있을 수 있다.

Q. RAG 문서는 왜 백업 우선순위가 높은가?
A. 직접 제작한 지식 자산이고 Agent 성능에 직접 영향을 주며 재작성 비용이 크기 때문이다.

Q. AnythingLLM은 무엇을 백업해야 하는가?
A. Storage Volume, Workspace Metadata, 업로드 문서, Vector Store, 설정 파일을 백업해야 한다.

Q. AnythingLLM 백업 전 Container를 멈춰야 하는가?
A. 가능하면 중지 후 백업하는 것이 안전하다. 실행 중 백업은 데이터 일관성 문제가 생길 수 있다.

Q. 설정 파일 백업이 왜 중요한가?
A. 데이터가 있어도 Docker, Reverse Proxy, 방화벽, 환경 변수 설정이 없으면 서비스를 빠르게 복구하기 어렵기 때문이다.

Q. Secret도 백업해야 하는가?
A. 필요하다. 하지만 평문 파일로 백업하지 말고 Password Manager, Secret Manager, 암호화 백업을 사용해야 한다.

Q. 백업도 암호화해야 하는가?
A. 중요 데이터나 Secret이 포함될 수 있으므로 암호화하는 것이 안전하다.

Q. Backup Verification은 왜 필요한가?
A. 백업 파일이 실제로 존재하고 손상되지 않았으며 복구 가능한지 확인하기 위해 필요하다.

Q. Restore Test는 얼마나 자주 해야 하는가?
A. 중요 데이터는 월 1회 또는 큰 변경 전후에 수행하는 것이 좋다. 개인 홈서버는 최소 분기별 테스트를 권장한다.

Q. Recovery Runbook은 왜 필요한가?
A. 장애 상황에서 기억에 의존하지 않고 빠르게 일관된 절차로 복구하기 위해 필요하다.

Q. 홈서버 전체 장애 시 무엇부터 복구해야 하는가?
A. OS와 Docker 실행 환경을 먼저 만들고, Compose 설정과 Volume 데이터를 복구한 뒤 서비스를 실행하고 검증한다.

Q. Cloud Object Storage는 백업에 왜 좋은가?
A. 홈서버와 물리적으로 분리된 위치에 데이터를 보관할 수 있고 Versioning, Lifecycle, 암호화 설정을 적용할 수 있기 때문이다.

Q. Backup Monitoring은 왜 필요한가?
A. 백업이 실패했는데 모르면 장애 발생 시 복구할 수 없기 때문이다.

Q. 배포 전 백업은 항상 필요한가?
A. 데이터 구조 변경, DB Migration, Volume 변경, 운영 설정 변경이 포함되면 강하게 권장된다.

Q. 장애 시나리오는 왜 미리 작성해야 하는가?
A. 장애 발생 시 영향 범위와 복구 절차를 빠르게 판단하기 위해 필요하다.

Q. 백업 실패 시 가장 먼저 확인할 것은?
A. 백업 로그, 경로, 권한, 디스크 용량, 백업 대상 존재 여부를 먼저 확인한다.

Q. Restore 실패 시 가장 먼저 확인할 것은?
A. 백업 파일 무결성, 대상 환경, 권한, Version 호환성, Secret 존재 여부를 확인한다.

Q. Backup / DR Review에서 가장 먼저 확인할 것은?
A. 백업 대상, 백업 저장 위치, 복구 테스트 여부, 암호화, Retention, 복구 절차 문서를 먼저 확인한다.

Q. 백업에서 가장 위험한 착각은?
A. 백업 파일이 있다는 이유만으로 복구 가능하다고 믿는 것이다. Restore Test가 없으면 신뢰할 수 없다.

Q. Backup / DR과 Cloud Provider는 어떻게 연결되는가?
A. S3 같은 Object Storage, Snapshot, Cloud Backup Storage, Offsite Backup 구성에서 연결된다.

Q. Backup / DR과 Docker Advanced는 어떻게 연결되는가?
A. Docker Volume, Compose 설정, Container 데이터 복구에서 연결된다.

Q. Backup / DR과 Security Operations는 어떻게 연결되는가?
A. 백업 암호화, 접근 권한, Secret 보호, 보안 사고 후 복구에서 연결된다.

Q. Backup / Disaster Recovery 문서의 최종 목적은?
A. Agent가 홈서버와 운영 시스템의 중요 데이터를 백업하고, 장애 발생 시 실제 복구 가능한 절차를 설계하게 만드는 것이다.
