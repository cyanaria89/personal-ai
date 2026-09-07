# Git / GitHub Domain Rules

---

# 1. Domain Purpose

Git / GitHub Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Version Control Support
- Collaboration Workflow Support
- Branch Strategy Support
- Code Review Support
- Git Troubleshooting

우선순위:

1. Git Core
2. Branch / Merge
3. GitHub Workflow
4. Troubleshooting

---

# 2. Scope

포함 범위:

- Git Core
- Repository
- Working Directory
- Staging Area
- Commit
- Branch
- Merge
- Rebase
- Cherry Pick
- Reset
- Revert
- Stash
- Conflict Resolve
- Remote Repository
- GitHub
- Pull Request
- Code Review
- Branch Strategy
- Git Flow
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

# 4. Git Core Rules

Git 문서는 Distributed Version Control 중심으로 작성.

핵심 구조:

- Working Directory
- Staging Area
- Local Repository
- Remote Repository

---

반드시 설명 포함:

- Git 역할
- 왜 사용하는가
- 버전 관리 의미
- 협업에서 어떤 문제를 해결하는가

---

예:

```text
Working Directory
→ Staging Area
→ Local Repository
→ Remote Repository
```

---

# 5. Repository Rules

필수 포함:

- Repository
- Local Repo
- Remote Repo

---

반드시 설명:

- 저장소 역할
- GitHub와 Git 차이

---

중요:

Git = Version Control Tool
GitHub = Remote Hosting Platform

---

# 6. Working Directory Rules

필수 포함:

- Modified
- Untracked

---

반드시 설명:

- 작업 중 파일 상태
- 변경 추적

---

# 7. Staging Area Rules

매우 중요.

필수 포함:

- git add
- Staging

---

예:

```bash
git add .
```

---

반드시 설명:

- Commit 전 준비 영역
- 선택적 Commit 가능

---

중요:

Git 문서 품질은 Staging Area 설명 품질이 결정.

---

# 8. Commit Rules

매우 중요.

필수 포함:

- Commit
- Snapshot

---

예:

```bash
git commit -m "feat: add login API"
```

---

반드시 설명:

- 변경 기록 저장
- Commit Message 규칙

---

권장:

Conventional Commit

```text
feat:
fix:
refactor:
docs:
test:
```

---

# 9. Branch Rules

매우 중요.

필수 포함:

- Branch
- Branch Isolation

---

예:

```bash
git branch feature/login
```

---

반드시 설명:

- 독립 작업 공간
- 협업 구조

---

# 10. Merge Rules

매우 중요.

필수 포함:

- Merge
- Fast Forward
- Merge Commit

---

예:

```bash
git merge feature/login
```

---

반드시 설명:

- Branch 통합
- History 영향

---

# 11. Rebase Rules

매우 중요.

필수 포함:

- Rebase
- History Rewrite

---

예:

```bash
git rebase main
```

---

반드시 설명:

- Merge와 차이
- Linear History

---

주의:

공유 Branch Rebase 주의.

---

# 12. Cherry Pick Rules

필수 포함:

- Cherry Pick
- Selective Commit Apply

---

예:

```bash
git cherry-pick commit-hash
```

---

반드시 설명:

- 특정 Commit만 가져오기

---

# 13. Reset Rules

필수 포함:

- soft
- mixed
- hard

---

예:

```bash
git reset --hard HEAD~1
```

---

반드시 설명:

- Commit 이동
- 변경 제거 위험

---

주의:

Hard Reset 주의.

---

# 14. Revert Rules

필수 포함:

- Revert
- Safe Undo

---

예:

```bash
git revert commit-hash
```

---

반드시 설명:

- 기록 유지하며 취소

---

# 15. Stash Rules

필수 포함:

- Stash
- Temporary Save

---

예:

```bash
git stash
```

---

반드시 설명:

- 작업 임시 저장

---

# 16. Conflict Rules

매우 중요.

필수 포함:

- Merge Conflict
- Conflict Resolve

---

반드시 설명:

- 충돌 발생 원인
- 해결 흐름

---

Flow:

```text
Conflict 발생
→ File 수정
→ Resolve
→ Commit
```

---

# 17. Remote Rules

필수 포함:

- Origin
- Push
- Pull
- Fetch

---

예:

```bash
git push origin main
git pull origin main
```

---

반드시 설명:

- Remote Sync

---

# 18. GitHub Rules

필수 포함:

- GitHub Repository
- Collaboration

---

반드시 설명:

- GitHub 역할
- Team Workflow

---

# 19. Pull Request Rules

매우 중요.

필수 포함:

- Pull Request
- Review
- Merge

---

반드시 설명:

- 코드 리뷰
- 협업 핵심

---

Flow:

```text
Feature Branch
→ Push
→ Pull Request
→ Review
→ Merge
```

---

# 20. Code Review Rules

필수 포함:

- Review Comment
- Approval
- Change Request

---

반드시 설명:

- Quality Assurance
- Collaboration

---

# 21. Branch Strategy Rules

매우 중요.

필수 포함:

- Main
- Develop
- Feature Branch

---

예:

```text
main
develop
feature/*
```

---

반드시 설명:

- 협업 Branch 전략

---

# 22. Git Flow Rules

필수 포함:

- main
- develop
- feature
- release
- hotfix

---

반드시 설명:

- Release Workflow

---

# 23. Troubleshooting Rules

반드시 포함 추천.

예:

- Merge Conflict
- Detached HEAD
- Push Rejected
- Rebase Conflict
- Wrong Commit
- Force Push Accident

---

형식:

문제:

원인:

해결:

---

# 24. Retrieval Optimization Rules

강조 대상:

- Git
- Commit
- Branch
- Merge
- Rebase
- Conflict
- Pull Request
- GitHub

키워드 반복 허용.

---

# 25. Version Rules

기준:

- Git 2.4+
- GitHub Workflow
- Modern Team Collaboration

---

Legacy 제외.

---

# 26. Common Mistakes

자주 발생:

- Main 직접 작업
- Commit Message 부실
- Rebase 오남용
- Hard Reset 남용
- Force Push 실수
- Conflict 무시
- Branch 전략 부재
- PR 없이 Merge

---

# 27. Final Goal

Git / GitHub RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Git Workflow
- Explain Git Commands
- Solve Git Conflicts
- Support Team Collaboration
- Review PR Workflow
- Troubleshoot Git Problems

문서 품질이 Collaboration 품질을 결정한다.
