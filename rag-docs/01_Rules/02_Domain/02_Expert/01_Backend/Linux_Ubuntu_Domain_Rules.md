# Linux / Ubuntu Domain Rules

---

# 1. Domain Purpose

Linux / Ubuntu Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Server Operation Support
- Linux Troubleshooting Support
- Deployment Environment Support
- Process Management Support
- System Monitoring Support

우선순위:

1. Linux Core
2. File / Process / Permission
3. Network / Service Management
4. Troubleshooting

---

# 2. Scope

포함 범위:

- Linux Core
- Ubuntu
- File System
- Directory Structure
- Permission
- User
- Group
- Process
- Port
- Network
- SSH
- Bash
- Shell Script
- Package Manager
- Systemctl
- Journalctl
- Monitoring
- Troubleshooting

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

---

## Optional

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

# 4. Linux Core Rules

Linux 문서는 Server OS 운영 중심으로 작성.

핵심 구조:

- File System
- Process
- User
- Network
- Service

---

반드시 설명 포함:

- Linux 역할
- 왜 사용하는가
- Windows와 차이
- Backend / DevOps에서 왜 중요한가

---

예:

```text
Application
→ Linux Process
→ Network
→ Storage
```

---

# 5. File System Rules

매우 중요.

필수 포함:

- Root
- Directory
- Path

---

예:

```text
/home
/etc
/var
/opt
```

---

반드시 설명:

- 디렉토리 구조
- 주요 경로 역할

---

중요:

Linux 문서 품질은 File System 설명 품질이 결정.

---

# 6. Directory Rules

필수 포함:

- /home
- /etc
- /var
- /tmp
- /usr
- /opt

---

반드시 설명:

- 설정 파일 위치
- 로그 위치
- 애플리케이션 위치

---

# 7. Permission Rules

매우 중요.

필수 포함:

- read
- write
- execute
- chmod
- chown

---

예:

```bash
chmod 755 app.sh
```

---

반드시 설명:

- 권한 구조
- 소유자 / 그룹

---

# 8. User Rules

필수 포함:

- user
- group
- sudo

---

반드시 설명:

- 계정 관리
- 권한 분리

---

# 9. Process Rules

매우 중요.

필수 포함:

- Process
- PID
- Foreground
- Background

---

예:

```bash
ps -ef
```

---

반드시 설명:

- Process 관리
- 실행 상태 확인

---

# 10. Process Control Rules

필수 포함:

- kill
- top
- htop

---

예:

```bash
kill -9 PID
```

---

반드시 설명:

- Process 종료
- Resource 확인

---

# 11. Port Rules

필수 포함:

- Port
- Listening

---

예:

```bash
netstat -tulnp
```

또는

```bash
ss -tulnp
```

---

반드시 설명:

- Port 충돌
- Service 접근

---

# 12. Network Rules

매우 중요.

필수 포함:

- IP
- DNS
- Routing

---

반드시 설명:

- Network 기본
- 서버 통신

---

# 13. SSH Rules

필수 포함:

- SSH
- Remote Access

---

예:

```bash
ssh user@server-ip
```

---

반드시 설명:

- 원격 서버 접속

---

# 14. Bash Rules

필수 포함:

- Shell
- Bash Command

---

예:

```bash
ls
cd
pwd
grep
find
```

---

반드시 설명:

- CLI 기반 운영

---

# 15. Shell Script Rules

필수 포함:

- Script
- Automation

---

예:

```bash
#!/bin/bash
```

---

반드시 설명:

- 반복 작업 자동화

---

# 16. Package Manager Rules

필수 포함:

- apt
- install
- update

---

예:

```bash
sudo apt update
sudo apt install nginx
```

---

반드시 설명:

- 패키지 설치
- 업데이트

---

# 17. Systemctl Rules

매우 중요.

필수 포함:

- start
- stop
- restart
- status

---

예:

```bash
systemctl status nginx
```

---

반드시 설명:

- Service 관리 핵심

---

# 18. Journalctl Rules

필수 포함:

- Logs
- Service Logs

---

예:

```bash
journalctl -u nginx
```

---

반드시 설명:

- 시스템 로그 확인

---

# 19. Monitoring Rules

필수 포함:

- CPU
- Memory
- Disk
- Network

---

반드시 설명:

- 운영 상태 관측

---

# 20. Troubleshooting Rules

반드시 포함 추천.

예:

- Permission Denied
- Port Already In Use
- Service Down
- High CPU
- OOM
- SSH Connection Failed

---

형식:

문제:

원인:

해결:

---

# 21. Retrieval Optimization Rules

강조 대상:

- Linux
- Ubuntu
- Process
- Permission
- SSH
- Systemctl
- Journalctl
- Port

키워드 반복 허용.

---

# 22. Version Rules

기준:

- Ubuntu 24/26 LTS
- Linux Server Environment
- Modern DevOps Workflow

---

Legacy 제외.

---

# 23. Common Mistakes

자주 발생:

- Root 남용
- chmod 777 남발
- Port 확인 안함
- Log 미확인
- Permission 무시
- Systemctl 미숙
- OOM 원인 미확인

---

# 24. Final Goal

Linux / Ubuntu RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Linux Commands
- Operate Linux Server
- Manage Process / Service
- Solve Server Issues
- Troubleshoot Production Problems

문서 품질이 Server Operation 품질을 결정한다.
