# Git / GitHub Part04 Remote GitHub Pull Request

---

# 1. Remote Repository

## 1.1 Remote Repository Core

### [개념]

Remote Repository는 Git Repository를 원격 서버에 저장하고 공유하는 저장소이다.

GitHub, GitLab, Bitbucket은 Remote Repository를 제공하는 Remote Hosting Platform이다.

Remote Repository는 팀원이 같은 코드베이스를 공유하고, Push / Pull / Pull Request 기반 협업을 가능하게 한다.

---

### [핵심]

- Remote Repository = 원격 Git 저장소
- GitHub = Remote Hosting Platform
- `origin` = 기본 Remote 이름
- `push` = Local Commit을 Remote에 업로드
- `pull` = Remote 변경 사항을 Local에 가져와 통합
- `fetch` = Remote 변경 사항을 가져오지만 자동 통합하지 않음
- 팀 협업은 Remote Repository 기준으로 동기화한다.

---

### [실무]

2026 실무 기준 대부분의 팀 프로젝트는 GitHub Remote Repository를 기준으로 협업한다.

일반적인 Remote Workflow:

```text
Remote Repository 생성
→ git clone
→ feature Branch 생성
→ Commit
→ git push origin feature/*
→ Pull Request
→ Review
→ Merge
→ Local 동기화
```

Remote 확인:

```bash
git remote -v
```

Remote 추가:

```bash
git remote add origin https://github.com/example/project.git
```

Remote URL 변경:

```bash
git remote set-url origin https://github.com/example/new-project.git
```

Remote 제거:

```bash
git remote remove origin
```

---

### [Flow]

```text
Local Repository
→ Commit
→ Push
→ Remote Repository
→ Pull Request
→ Merge
→ Team Sync
```

---

### [주의]

Remote Repository는 백업 저장소가 아니라 협업 기준 저장소이다.

Local Commit은 Push 전까지 Remote에 반영되지 않는다.

Remote의 변경 사항을 Pull하지 않고 오래 작업하면 Conflict 가능성이 높아진다.

Remote URL이 잘못되면 다른 Repository에 Push할 수 있다.

---

### [FAQ]

Q. Remote Repository는 무엇인가?
A. Remote Repository는 Git Repository를 원격 서버에 저장하고 팀과 공유하는 저장소이다.

Q. origin은 무엇인가?
A. origin은 기본 Remote Repository 이름이다.

Q. GitHub는 Remote Repository인가?
A. GitHub는 Remote Repository를 제공하는 Remote Hosting Platform이다.

Q. Local Commit은 GitHub에 자동 반영되는가?
A. 아니다. Local Commit은 `git push`를 해야 Remote Repository에 반영된다.

---

# 2. Clone And Remote Setup

## 2.1 Clone

### [개념]

Clone은 Remote Repository를 로컬 PC에 복사하여 Local Repository를 생성하는 Git 작업이다.

`git clone`은 코드 파일뿐 아니라 Commit History와 Remote 연결 정보도 함께 가져온다.

---

### [핵심]

- `git clone` = Remote Repository 복사
- Local Repository 자동 생성
- `.git` 디렉터리 생성
- `origin` Remote 자동 등록
- 기본 Branch Checkout
- 팀 프로젝트 참여 시 첫 작업으로 사용

---

### [예제]

HTTPS Clone:

```bash
git clone https://github.com/example/project.git
```

SSH Clone:

```bash
git clone git@github.com:example/project.git
```

특정 폴더명으로 Clone:

```bash
git clone https://github.com/example/project.git festa-pick
```

Clone 후 확인:

```bash
cd project
git remote -v
git branch
```

---

### [실무]

팀 프로젝트에서는 보통 GitHub Repository 주소를 받아 Clone한다.

Clone 후 초기 확인:

```text
1. README 확인
2. Branch 확인
3. Remote 확인
4. .env.example 확인
5. Build / Run 방법 확인
```

Spring Boot / React 프로젝트 예시:

```bash
git clone https://github.com/team/festapick.git
cd festapick
git remote -v
git branch -a
```

---

### [주의]

Clone한 프로젝트에서 바로 main에 작업하지 않는다.

작업 전 feature Branch를 생성한다.

```bash
git switch -c feature/festival-search
```

Private Repository는 권한이 없으면 Clone할 수 없다.

HTTPS 방식은 Personal Access Token 인증이 필요할 수 있다.

SSH 방식은 SSH Key 등록이 필요하다.

---

### [FAQ]

Q. git clone은 무엇인가?
A. Remote Repository를 로컬 PC에 복사하여 Local Repository를 만드는 명령이다.

Q. git clone을 하면 origin이 자동 등록되는가?
A. 맞다. Clone한 Remote Repository가 기본 origin으로 등록된다.

Q. HTTPS Clone과 SSH Clone 차이는?
A. HTTPS는 계정/토큰 기반 인증을 사용하고, SSH는 등록된 SSH Key 기반 인증을 사용한다.

Q. Clone 후 바로 main에 작업해도 되는가?
A. 실무에서는 권장하지 않는다. feature Branch를 생성한 뒤 작업한다.

---

## 2.2 Existing Local Project Remote Setup

### [개념]

기존 로컬 프로젝트를 GitHub에 올리려면 Local Repository를 초기화하고 Remote Repository를 연결해야 한다.

---

### [핵심]

- `git init` = Local Repository 초기화
- `.gitignore` 먼저 작성
- Initial Commit 생성
- GitHub Repository 생성
- `git remote add origin`으로 연결
- `git push -u origin main`으로 업로드

---

### [예제]

기존 프로젝트 Git 초기화:

```bash
git init
git add .
git commit -m "chore: initial commit"
```

Remote 연결:

```bash
git remote add origin https://github.com/example/project.git
```

기본 Branch 이름 main 설정:

```bash
git branch -M main
```

최초 Push:

```bash
git push -u origin main
```

---

### [실무]

기존 프로젝트를 GitHub에 처음 올릴 때는 민감 정보와 빌드 결과물을 먼저 제외한다.

초기 Push 전 확인:

```bash
git status
git diff --staged
```

필수 확인 파일:

```text
.gitignore
README.md
.env.example
build.gradle 또는 package.json
```

올리면 안 되는 파일:

```text
.env
application-local.properties
node_modules/
build/
dist/
.gradle/
```

---

### [주의]

GitHub에서 README를 먼저 만들고 로컬에서도 Initial Commit을 만들면 History가 달라 Push가 거부될 수 있다.

이 경우 Pull로 병합하거나 Remote Repository를 비운 상태에서 시작한다.

```bash
git pull origin main --allow-unrelated-histories
```

단, 무조건 사용하지 말고 두 Repository가 정말 같은 프로젝트인지 확인한다.

---

### [FAQ]

Q. 기존 프로젝트를 GitHub에 올리는 순서는?
A. `git init → git add → git commit → git remote add origin → git push -u origin main` 순서이다.

Q. git push -u origin main의 -u는 무엇인가?
A. Local Branch와 Remote Branch의 upstream 추적 관계를 설정하는 옵션이다.

Q. GitHub에서 README를 먼저 만들면 문제가 되는가?
A. 로컬 Initial Commit과 Remote Initial Commit이 달라 Push가 거부될 수 있다.

Q. --allow-unrelated-histories는 언제 쓰는가?
A. 서로 관련 없는 두 Git History를 병합해야 할 때 사용한다. 신중하게 사용해야 한다.

---

# 3. Push

## 3.1 Push Core

### [개념]

Push는 Local Repository의 Commit을 Remote Repository에 업로드하는 Git 작업이다.

Push를 해야 다른 팀원이 내 Commit을 Remote에서 확인할 수 있다.

---

### [핵심]

- Push = Local Commit을 Remote에 반영
- Commit 없는 변경 사항은 Push되지 않음
- `origin` = Push 대상 Remote
- Branch 단위로 Push
- 최초 Push 시 upstream 설정 권장
- Remote 변경과 충돌하면 Push가 거부될 수 있음

---

### [예제]

현재 Branch Push:

```bash
git push
```

특정 Branch Push:

```bash
git push origin feature/login-api
```

최초 Push와 upstream 설정:

```bash
git push -u origin feature/login-api
```

Rebase 후 안전 Force Push:

```bash
git push --force-with-lease origin feature/login-api
```

---

### [Flow]

```text
Code 수정
→ git add
→ git commit
→ git push origin feature/*
→ Remote Branch 생성
→ Pull Request 생성 가능
```

---

### [실무]

실무에서는 feature Branch를 Remote에 Push한 뒤 Pull Request를 생성한다.

예:

```bash
git switch -c feature/notification-api
git add .
git commit -m "feat: add notification API"
git push -u origin feature/notification-api
```

Push 전 확인:

```bash
git status
git log --oneline -5
git branch
```

---

### [주의]

Push는 Staging 파일을 올리는 작업이 아니다.

Push되는 것은 Commit이다.

`git add`만 하고 Commit하지 않은 변경은 Push되지 않는다.

main / develop에 직접 Push하지 않는다.

Force Push는 공유 Branch에서 위험하다.

---

### [FAQ]

Q. Push는 무엇인가?
A. Push는 Local Repository의 Commit을 Remote Repository에 업로드하는 작업이다.

Q. git add만 해도 Push되는가?
A. 아니다. Push는 Commit을 업로드한다. Staging만 된 변경은 Push되지 않는다.

Q. 최초 Push에서 -u는 왜 쓰는가?
A. Local Branch와 Remote Branch를 연결해 이후 `git push`, `git pull`을 간단히 사용하기 위해 쓴다.

Q. Force Push는 언제 위험한가?
A. 공유 Branch에서 사용하면 팀원의 Commit History를 덮어쓸 수 있어 위험하다.

---

## 3.2 Push Rejected

### [개념]

Push Rejected는 Local Branch의 History가 Remote Branch보다 뒤처졌거나, Remote와 충돌 가능성이 있을 때 Push가 거부되는 상태이다.

---

### [핵심]

- Push Rejected = Remote 반영 거부
- Remote에 내가 모르는 Commit이 있음
- Local Branch가 Remote보다 뒤처짐
- Pull / Fetch 후 통합 필요
- Rebase 후에는 Force Push가 필요할 수 있음

---

### [Troubleshooting]

문제:

```text
! [rejected] main -> main (fetch first)
```

원인:

```text
Remote Branch에 Local에 없는 Commit이 있다.
```

해결:

```bash
git pull origin main
git push origin main
```

---

문제:

```text
non-fast-forward
```

원인:

```text
Local History가 Remote History를 Fast Forward할 수 없는 상태이다.
```

해결:

```bash
git fetch origin
git rebase origin/main
git push origin main
```

---

문제:

```text
Rebase 후 Push 거부
```

원인:

```text
Rebase로 Local Commit Hash가 변경되어 Remote History와 달라졌다.
```

해결:

```bash
git push --force-with-lease origin feature/login-api
```

---

### [주의]

Push Rejected 상황에서 무조건 Force Push하지 않는다.

먼저 Remote 변경 사항을 확인한다.

```bash
git fetch origin
git log --oneline --graph --decorate --all
```

공유 Branch에서는 Force Push 금지에 가깝다.

---

### [FAQ]

Q. Push Rejected는 왜 발생하는가?
A. Remote Branch에 Local에 없는 Commit이 있거나 History가 달라졌기 때문이다.

Q. fetch first 에러는 어떻게 해결하는가?
A. Remote 변경을 Pull 또는 Fetch/Rebase로 반영한 뒤 Push한다.

Q. non-fast-forward는 무엇인가?
A. Local History가 Remote History를 단순히 앞으로 이동시킬 수 없는 상태이다.

Q. Push Rejected 때 Force Push해도 되는가?
A. 본인 feature Branch가 아니라면 위험하다. 먼저 Remote 변경을 확인해야 한다.

---

# 4. Fetch And Pull

## 4.1 Fetch

### [개념]

Fetch는 Remote Repository의 변경 사항을 Local로 가져오지만 현재 작업 Branch에 자동 통합하지 않는 Git 작업이다.

Fetch는 Remote 상태 확인에 안전하다.

---

### [핵심]

- Fetch = Remote 변경 가져오기
- 자동 Merge 없음
- 자동 Rebase 없음
- Local Working Directory 영향 적음
- Remote Tracking Branch 갱신
- Pull 전 확인 용도로 안전

---

### [예제]

전체 Remote 정보 가져오기:

```bash
git fetch origin
```

Remote 삭제 Branch 정리:

```bash
git fetch --prune
```

Remote Tracking Branch 확인:

```bash
git branch -r
```

Remote와 Local 차이 확인:

```bash
git log --oneline HEAD..origin/main
```

---

### [실무]

Fetch는 Remote 변경을 먼저 확인할 때 사용한다.

권장 흐름:

```text
git fetch origin
→ Remote 변경 확인
→ 필요 시 merge 또는 rebase
```

명령 예시:

```bash
git fetch origin
git log --oneline --graph --decorate --all
```

---

### [주의]

Fetch만으로 현재 코드가 최신화되지는 않는다.

Fetch는 Remote Tracking Branch를 갱신할 뿐, 현재 Branch에 자동 반영하지 않는다.

현재 Branch에 반영하려면 Merge 또는 Rebase가 필요하다.

---

### [FAQ]

Q. Fetch는 무엇인가?
A. Fetch는 Remote Repository 변경 사항을 가져오지만 현재 Branch에 자동 통합하지 않는 작업이다.

Q. Fetch만 하면 코드가 최신화되는가?
A. 아니다. Fetch 후 Merge 또는 Rebase가 필요하다.

Q. git fetch --prune은 무엇인가?
A. Remote에서 삭제된 Branch의 Local Tracking 정보를 정리하는 명령이다.

Q. Pull보다 Fetch가 안전한 이유는?
A. Fetch는 자동 통합하지 않아 현재 작업 Branch를 직접 변경하지 않기 때문이다.

---

## 4.2 Pull

### [개념]

Pull은 Remote Repository의 변경 사항을 가져오고 현재 Branch에 통합하는 Git 작업이다.

Pull은 기본적으로 Fetch 후 Merge를 수행한다.

설정에 따라 Fetch 후 Rebase로 동작할 수 있다.

---

### [핵심]

- Pull = Fetch + 통합
- 기본 동작 = Fetch + Merge
- 설정에 따라 Fetch + Rebase 가능
- 현재 Branch가 변경될 수 있음
- Conflict 발생 가능
- 작업 전 `git status` 확인 필요

---

### [예제]

현재 Branch Pull:

```bash
git pull
```

특정 Remote Branch Pull:

```bash
git pull origin main
```

Rebase 방식 Pull:

```bash
git pull --rebase origin main
```

Fast Forward만 허용:

```bash
git pull --ff-only origin main
```

---

### [Flow]

```text
git status
→ git pull origin main
→ Conflict 발생 시 해결
→ 테스트
→ 작업 계속
```

---

### [실무]

작업 시작 전 기준 Branch 최신화:

```bash
git switch develop
git pull origin develop
git switch -c feature/festival-map
```

feature Branch에서 기준 Branch 변경 반영:

```bash
git switch feature/festival-map
git pull --rebase origin develop
```

팀에서 Linear History를 선호하면 `pull --rebase`를 사용한다.

---

### [주의]

Commit하지 않은 변경이 있는 상태에서 Pull하면 충돌 가능성이 있다.

Pull 전 확인:

```bash
git status
```

작업 중인 변경이 있으면 Commit 또는 Stash 후 Pull한다.

```bash
git stash push -m "wip before pull"
git pull origin develop
git stash pop
```

---

### [FAQ]

Q. Pull은 무엇인가?
A. Pull은 Remote 변경 사항을 가져오고 현재 Branch에 통합하는 작업이다.

Q. Pull과 Fetch 차이는?
A. Fetch는 가져오기만 하고, Pull은 가져온 뒤 현재 Branch에 Merge 또는 Rebase한다.

Q. git pull --rebase는 무엇인가?
A. Remote 변경 사항을 가져온 뒤 현재 Local Commit을 그 위로 다시 쌓는 방식이다.

Q. Pull 전 확인할 것은?
A. `git status`로 Commit되지 않은 변경 사항이 있는지 확인해야 한다.

---

# 5. Upstream Tracking

## 5.1 Upstream Branch

### [개념]

Upstream Branch는 Local Branch가 추적하는 Remote Branch이다.

Upstream이 설정되면 `git push`, `git pull`에서 Remote와 Branch 이름을 생략할 수 있다.

---

### [핵심]

- Upstream = Local Branch와 Remote Branch 연결
- 최초 Push 시 `-u`로 설정
- Push / Pull 대상 자동 지정
- Branch 추적 관계 확인 가능
- 잘못 설정되면 다른 Branch로 Push/Pull할 수 있음

---

### [예제]

Upstream 설정하며 Push:

```bash
git push -u origin feature/login-api
```

현재 Branch의 Upstream 확인:

```bash
git branch -vv
```

Upstream 수동 설정:

```bash
git branch --set-upstream-to=origin/feature/login-api
```

Upstream 제거:

```bash
git branch --unset-upstream
```

---

### [실무]

새 feature Branch를 Remote에 처음 올릴 때는 `-u`를 붙인다.

```bash
git push -u origin feature/festival-search
```

이후에는 간단히 사용 가능하다.

```bash
git push
git pull
```

---

### [주의]

Upstream이 잘못 연결되어 있으면 예상하지 않은 Branch와 동기화될 수 있다.

항상 `git branch -vv`로 확인 가능하다.

Branch 이름이 비슷한 경우 주의한다.

```text
feature/login
feature/login-api
feature/login-page
```

---

### [FAQ]

Q. Upstream Branch란?
A. Local Branch가 추적하는 Remote Branch이다.

Q. git push -u는 무엇인가?
A. Push하면서 Local Branch와 Remote Branch의 upstream 추적 관계를 설정하는 옵션이다.

Q. Upstream을 확인하려면?
A. `git branch -vv` 명령을 사용한다.

Q. Upstream이 없으면 어떤 문제가 생기는가?
A. `git push`나 `git pull`만 실행했을 때 대상 Branch를 알 수 없어 에러가 발생할 수 있다.

---

# 6. GitHub

## 6.1 GitHub Core

### [개념]

GitHub는 Git Repository를 원격으로 호스팅하고 협업 기능을 제공하는 Remote Hosting Platform이다.

GitHub는 Remote Repository, Pull Request, Issue, Code Review, Actions, Wiki, Release 기능을 제공한다.

---

### [핵심]

- GitHub = Git 기반 협업 플랫폼
- Repository Hosting
- Pull Request
- Code Review
- Issue Tracking
- Branch Protection
- GitHub Actions
- Release Management
- Team Collaboration

---

### [실무]

2026 실무 기준 GitHub는 단순 코드 저장소가 아니라 개발 협업 플랫폼이다.

팀 프로젝트에서 GitHub가 담당하는 역할:

```text
Code 저장
→ Branch 공유
→ Pull Request
→ Code Review
→ CI 실행
→ Merge 관리
→ Release 관리
```

주요 기능:

| 기능         | 목적                             |
| ------------ | -------------------------------- |
| Repository   | 코드 저장소                      |
| Issue        | 작업 항목 / 버그 / 요구사항 관리 |
| Pull Request | 변경 제안 / 리뷰 / 병합          |
| Actions      | CI/CD 자동화                     |
| Projects     | 칸반 / 작업 관리                 |
| Releases     | 배포 버전 관리                   |
| Wiki         | 프로젝트 문서화                  |

---

### [주의]

GitHub는 Git 자체가 아니다.

Git 명령은 로컬에서 실행되고, GitHub는 Remote Repository와 협업 기능을 제공한다.

GitHub에 코드가 있어도 Local이 자동 최신화되지는 않는다.

Local 최신화에는 `git pull` 또는 `git fetch`가 필요하다.

---

### [FAQ]

Q. GitHub는 무엇인가?
A. GitHub는 Git Repository를 원격으로 호스팅하고 Pull Request, Review, Issue 기능을 제공하는 협업 플랫폼이다.

Q. GitHub와 Git은 같은가?
A. 아니다. Git은 버전 관리 도구이고 GitHub는 Git 기반 원격 협업 플랫폼이다.

Q. GitHub에서 Pull Request는 왜 중요한가?
A. 코드를 main에 반영하기 전 Review, 테스트, 변경 이력 확인을 가능하게 하기 때문이다.

Q. GitHub Actions는 무엇인가?
A. GitHub에서 제공하는 CI/CD 자동화 기능이다.

---

# 7. Pull Request

## 7.1 Pull Request Core

### [개념]

Pull Request는 Branch의 변경 사항을 다른 Branch에 병합해 달라고 요청하는 GitHub 협업 기능이다.

Pull Request는 Code Review, Discussion, CI Check, Merge 관리를 위한 중심 단위이다.

---

### [핵심]

- Pull Request = 변경 병합 요청
- PR = Pull Request
- Feature Branch 변경을 main / develop에 반영하기 전 검토
- Code Review 중심
- CI Check 연동 가능
- 변경 파일과 Commit 확인 가능
- Merge Strategy 선택 가능

---

### [Flow]

```text
Feature Branch 생성
→ Code 수정
→ Commit
→ Push
→ Pull Request 생성
→ Reviewer 지정
→ Review
→ CI Check
→ 수정 Commit
→ Approval
→ Merge
→ Branch Delete
```

---

### [실무]

Pull Request 작성 시 포함할 내용:

```text
1. 작업 목적
2. 변경 내용
3. 테스트 결과
4. 영향 범위
5. 리뷰 요청 포인트
6. 관련 Issue
```

PR 제목 예시:

```text
feat: add festival search API
fix: resolve JWT expiration handling
refactor: separate notification service
```

PR 설명 템플릿:

```md
## 작업 내용

- 축제 검색 API 추가
- 지역 / 테마 / 기간 조건 처리
- Pageable 기반 목록 응답 적용

## 테스트

- [ ] 단위 테스트
- [ ] Swagger 확인
- [ ] 프론트 연동 확인

## 리뷰 포인트

- 검색 조건 조합 로직
- QueryDSL 동적 조건 처리
- 응답 DTO 구조
```

---

### [주의]

Pull Request는 단순 Merge 버튼이 아니다.

Pull Request는 변경 내용을 설명하고 검증받는 협업 절차이다.

큰 Pull Request는 Review 품질을 떨어뜨린다.

권장:

- 작은 기능 단위 PR
- 명확한 제목
- 충분한 설명
- 테스트 결과 포함
- 관련 Issue 연결
- 불필요한 파일 제외

---

### [FAQ]

Q. Pull Request는 무엇인가?
A. Pull Request는 Branch의 변경 사항을 다른 Branch에 병합해 달라고 요청하는 GitHub 협업 기능이다.

Q. PR은 왜 사용하는가?
A. Code Review, 테스트 확인, 변경 이력 검토 후 안전하게 Merge하기 위해 사용한다.

Q. 좋은 Pull Request 기준은?
A. 작업 목적, 변경 내용, 테스트 결과, 영향 범위, 리뷰 포인트가 명확해야 한다.

Q. 큰 PR이 나쁜 이유는?
A. Review 난이도가 높아지고 버그나 설계 문제를 놓칠 가능성이 커지기 때문이다.

---

## 7.2 Pull Request Merge Strategy

### [개념]

Pull Request Merge Strategy는 GitHub에서 Pull Request를 대상 Branch에 반영하는 방식이다.

대표 방식은 Merge Commit, Squash Merge, Rebase Merge이다.

---

### [핵심]

- Merge Commit = Branch 통합 Commit 생성
- Squash Merge = PR Commit들을 하나로 압축
- Rebase Merge = Commit들을 대상 Branch 위에 재배치
- 팀 History 정책에 따라 선택
- Merge Strategy는 Git History 품질에 영향을 준다.

---

### [Comparison]

| Strategy     | 결과              | 장점                  | 주의             |
| ------------ | ----------------- | --------------------- | ---------------- |
| Merge Commit | Merge Commit 생성 | Branch 통합 기록 명확 | History 복잡     |
| Squash Merge | Commit 1개로 압축 | main History 깔끔     | 세부 Commit 손실 |
| Rebase Merge | Linear History    | 이력 선형 유지        | Commit Hash 변경 |

---

### [실무]

소규모 팀 프로젝트 권장:

```text
feature Branch
→ Pull Request
→ Squash Merge
→ Branch Delete
```

이유:

- main History가 깔끔하다.
- PR 단위로 기능 추적이 쉽다.
- 의미 없는 중간 Commit을 줄일 수 있다.
- 초보 팀원 Commit Message 품질 편차를 줄인다.

대규모 프로젝트에서는 팀 규칙에 따라 Merge Commit 또는 Rebase Merge를 선택한다.

---

### [주의]

Merge Strategy는 팀 전체가 통일해야 한다.

같은 Repository에서 전략이 섞이면 History 추적 방식이 불규칙해진다.

Squash Merge 후 같은 feature Branch를 계속 재사용하지 않는다.

Merge 후 Branch 삭제를 권장한다.

---

### [FAQ]

Q. Pull Request Merge Strategy 종류는?
A. Merge Commit, Squash Merge, Rebase Merge가 대표적이다.

Q. Squash Merge는 언제 좋은가?
A. Pull Request 단위로 main History를 깔끔하게 관리하고 싶을 때 좋다.

Q. Merge Commit 방식 장점은?
A. Branch가 언제 통합되었는지 Merge 기록이 명확하게 남는다.

Q. Rebase Merge는 무엇인가?
A. PR Commit들을 대상 Branch 최신 Commit 위로 재배치해 Linear History를 유지하는 방식이다.

---

# 8. Code Review

## 8.1 Code Review Core

### [개념]

Code Review는 Pull Request의 변경 사항을 팀원이 검토하고 품질, 버그, 설계, Convention을 확인하는 협업 절차이다.

---

### [핵심]

- Code Review = 변경 코드 검토
- Pull Request 기반으로 진행
- Reviewer가 Comment 작성
- Approval 또는 Change Request 가능
- 버그 예방
- 코드 품질 향상
- 팀 Convention 공유
- 지식 전파

---

### [실무]

Code Review에서 확인할 항목:

```text
1. 요구사항을 충족하는가?
2. 로직 오류가 없는가?
3. 예외 처리가 적절한가?
4. 보안 문제가 없는가?
5. 성능 문제가 없는가?
6. 코드 Convention을 지키는가?
7. 테스트가 충분한가?
8. 불필요한 파일이 포함되지 않았는가?
```

Review Comment 예시:

```text
이 조건은 null일 때 NPE가 발생할 수 있어 보입니다.
Optional 처리나 사전 검증을 추가하는 것이 좋겠습니다.
```

Change Request 예시:

```text
JWT 만료 예외 처리 테스트가 누락되어 있습니다.
Security Filter 변경 영향이 있으므로 테스트 추가 후 다시 확인하겠습니다.
```

Approval 예시:

```text
확인했습니다. 검색 조건 조합과 응답 DTO 구조 모두 문제 없어 보입니다.
```

---

### [Best Practice]

Reviewer 기준:

- 코드가 아니라 변경 목적을 먼저 이해한다.
- 문제를 지적할 때 이유를 함께 적는다.
- 취향보다 팀 Convention을 기준으로 판단한다.
- 치명도 높은 문제를 우선 확인한다.
- 작은 스타일 문제만 과하게 지적하지 않는다.

Author 기준:

- PR 설명을 충분히 작성한다.
- Review Comment에 근거 있게 답변한다.
- 수정 후 변경 내용을 다시 설명한다.
- 해결된 Comment는 Resolve 처리한다.
- 방어적으로 반응하지 않는다.

---

### [주의]

Code Review는 비난이 아니라 품질 검증 절차이다.

Comment는 구체적이어야 한다.

나쁜 Comment:

```text
이상함
별로임
다시 하세요
```

좋은 Comment:

```text
이 Service 메서드는 Transaction 경계가 필요해 보입니다.
Repository save 이후 추가 변경이 있으므로 @Transactional 적용을 검토해주세요.
```

---

### [FAQ]

Q. Code Review는 무엇인가?
A. Pull Request의 변경 사항을 검토하여 버그, 설계 문제, Convention 위반을 확인하는 협업 절차이다.

Q. Approval은 무엇인가?
A. Reviewer가 변경 사항을 승인하여 Merge 가능하다고 판단하는 상태이다.

Q. Change Request는 무엇인가?
A. Merge 전 반드시 수정이 필요하다고 Reviewer가 요청하는 상태이다.

Q. 좋은 Review Comment 기준은?
A. 문제 위치, 이유, 개선 방향이 구체적으로 포함되어야 한다.

---

# 9. GitHub Issue

## 9.1 Issue Core

### [개념]

Issue는 GitHub에서 작업 항목, 버그, 요구사항, 개선 사항을 추적하는 단위이다.

Issue는 Pull Request와 연결하여 작업 흐름을 관리할 수 있다.

---

### [핵심]

- Issue = 작업 추적 단위
- Bug Report
- Feature Request
- Task
- Discussion
- Label로 분류
- Assignee로 담당자 지정
- Milestone으로 일정 관리
- Pull Request와 연결 가능

---

### [실무]

Issue 작성 내용:

```text
1. 작업 목적
2. 현재 문제
3. 기대 결과
4. 작업 범위
5. 완료 기준
6. 참고 자료
```

Bug Issue 예시:

```md
## 문제

JWT 만료 시 500 에러가 반환됩니다.

## 기대 결과

만료 Token 요청은 401 Unauthorized로 응답해야 합니다.

## 재현 방법

1. 만료된 Access Token 생성
2. Authorization Header에 입력
3. 보호 API 요청

## 완료 기준

- 401 응답
- 표준 ApiResponse 오류 형식 적용
- 테스트 통과
```

PR에서 Issue 닫기:

```text
Closes #12
Fixes #15
Resolves #20
```

---

### [주의]

Issue는 메모장이 아니라 작업 추적 단위이다.

완료 기준이 없는 Issue는 작업 완료 판단이 어렵다.

Issue와 Pull Request를 연결하면 변경 이유 추적이 쉬워진다.

---

### [FAQ]

Q. GitHub Issue는 무엇인가?
A. 작업 항목, 버그, 요구사항, 개선 사항을 추적하는 GitHub 기능이다.

Q. Issue와 Pull Request를 연결하는 이유는?
A. 작업 이유와 실제 코드 변경을 함께 추적하기 위해서이다.

Q. Closes #12는 무엇인가?
A. 해당 Pull Request가 Merge되면 Issue #12를 자동으로 닫는 키워드이다.

Q. 좋은 Issue 기준은?
A. 문제, 기대 결과, 작업 범위, 완료 기준이 명확해야 한다.

---

# 10. Branch Protection

## 10.1 Branch Protection Rules

### [개념]

Branch Protection은 GitHub에서 main, develop 같은 중요 Branch를 보호하기 위한 Repository 설정이다.

직접 Push 제한, Pull Request Review 필수, Status Check 통과 필수 같은 규칙을 적용할 수 있다.

---

### [핵심]

- Branch Protection = 중요 Branch 보호
- main 직접 Push 제한
- Pull Request 필수화
- Review 승인 필수화
- CI Status Check 필수화
- Force Push 제한
- 삭제 방지
- 협업 안정성 강화

---

### [실무]

팀 프로젝트 권장 Branch Protection:

```text
main Branch:
- Direct Push 금지
- Pull Request Required
- 1명 이상 Review Required
- Status Check Required
- Force Push 금지
- Delete 금지
```

develop Branch:

```text
develop Branch:
- Direct Push 제한
- Pull Request 권장
- CI Check 권장
```

적용 목적:

- 실수로 main에 Push 방지
- Review 없는 코드 반영 방지
- 테스트 실패 코드 Merge 방지
- Force Push 사고 방지

---

### [주의]

Branch Protection이 너무 강하면 작은 팀에서는 작업 속도가 느려질 수 있다.

하지만 main Branch는 최소한 직접 Push와 Force Push를 막는 것이 안전하다.

권한 설정은 팀 규모와 프로젝트 중요도에 맞춰 조정한다.

---

### [FAQ]

Q. Branch Protection은 무엇인가?
A. GitHub에서 main 같은 중요 Branch를 보호하기 위한 Repository 설정이다.

Q. Branch Protection을 쓰는 이유는?
A. 직접 Push, Force Push, Review 없는 Merge 같은 사고를 방지하기 위해서이다.

Q. main Branch에 추천하는 보호 규칙은?
A. Direct Push 금지, Pull Request 필수, Review 승인 필수, Force Push 금지를 권장한다.

Q. Status Check Required는 무엇인가?
A. 테스트나 빌드 같은 CI Check가 통과해야 Merge할 수 있게 하는 규칙이다.

---

# 11. GitHub Actions

## 11.1 GitHub Actions Core

### [개념]

GitHub Actions는 GitHub에서 제공하는 CI/CD 자동화 기능이다.

Push, Pull Request, Release 같은 이벤트를 기준으로 테스트, 빌드, 배포 작업을 자동 실행할 수 있다.

---

### [핵심]

- GitHub Actions = CI/CD Automation
- Workflow = 자동화 정의 파일
- Event = 실행 조건
- Job = 실행 작업 묶음
- Step = Job 내부 실행 단계
- Runner = Workflow 실행 환경
- Pull Request 테스트 자동화 가능

---

### [예제]

Spring Boot 테스트 Workflow:

```yaml
name: Java CI

on:
  pull_request:
    branches: ["main", "develop"]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "21"
      - run: ./gradlew test
```

React 빌드 Workflow:

```yaml
name: React CI

on:
  pull_request:
    branches: ["main", "develop"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - run: npm ci
      - run: npm run build
```

---

### [실무]

Pull Request에 GitHub Actions를 연결하면 Merge 전 자동 검증이 가능하다.

일반적인 CI 흐름:

```text
Pull Request 생성
→ GitHub Actions 실행
→ Build
→ Test
→ Status Check 결과 표시
→ Review
→ Merge
```

Status Check를 Branch Protection과 연결하면 테스트 실패 PR은 Merge할 수 없다.

---

### [주의]

Secrets를 Workflow 파일에 직접 작성하지 않는다.

금지:

```yaml
DB_PASSWORD: my-secret-password
```

권장:

```yaml
DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

Workflow는 Repository의 `.github/workflows` 디렉터리에 위치한다.

---

### [FAQ]

Q. GitHub Actions는 무엇인가?
A. GitHub에서 제공하는 CI/CD 자동화 기능이다.

Q. Workflow는 무엇인가?
A. GitHub Actions 자동화 작업을 정의하는 YAML 파일이다.

Q. Pull Request에서 Actions를 쓰는 이유는?
A. Merge 전 빌드와 테스트를 자동 검증하기 위해 사용한다.

Q. GitHub Secrets는 무엇인가?
A. API Key, DB Password 같은 민감 정보를 안전하게 저장하고 Workflow에서 참조하는 기능이다.

---

# 12. Release And Tag

## 12.1 Tag

### [개념]

Tag는 특정 Commit에 이름을 붙여 버전이나 배포 지점을 표시하는 Git 기능이다.

Release는 GitHub에서 Tag를 기반으로 배포 버전, 변경 내역, 파일을 관리하는 기능이다.

---

### [핵심]

- Tag = 특정 Commit 표시
- Release = GitHub 배포 버전 관리
- Versioning에 사용
- 배포 기준 Commit 명확화
- Hotfix 기준점 추적 가능
- Semantic Versioning과 함께 사용

---

### [예제]

Tag 생성:

```bash
git tag v1.0.0
```

메시지 포함 Annotated Tag:

```bash
git tag -a v1.0.0 -m "release v1.0.0"
```

Tag Push:

```bash
git push origin v1.0.0
```

전체 Tag Push:

```bash
git push origin --tags
```

Tag 목록 확인:

```bash
git tag
```

---

### [실무]

버전 형식은 Semantic Versioning을 자주 사용한다.

```text
MAJOR.MINOR.PATCH
```

예:

```text
v1.0.0
v1.1.0
v1.1.1
```

의미:

| 버전  | 의미                  |
| ----- | --------------------- |
| MAJOR | 호환되지 않는 큰 변경 |
| MINOR | 하위 호환 기능 추가   |
| PATCH | 하위 호환 버그 수정   |

---

### [주의]

Tag는 배포 기준점이므로 잘못 찍으면 Release 추적이 혼란스러워진다.

Tag를 삭제하거나 수정할 때는 팀 공유가 필요하다.

Remote Tag 삭제:

```bash
git push origin --delete v1.0.0
```

Local Tag 삭제:

```bash
git tag -d v1.0.0
```

---

### [FAQ]

Q. Git Tag는 무엇인가?
A. 특정 Commit에 버전 이름을 붙여 배포 기준점을 표시하는 Git 기능이다.

Q. GitHub Release는 무엇인가?
A. Tag를 기반으로 배포 버전과 변경 내역을 관리하는 GitHub 기능이다.

Q. v1.0.0은 무엇인가?
A. Semantic Versioning 형식의 버전 태그이다.

Q. Tag를 Remote에 올리려면?
A. `git push origin v1.0.0` 명령을 사용한다.

---

# 13. Remote GitHub Troubleshooting

## 13.1 Troubleshooting

### [개념]

Remote GitHub Troubleshooting은 Clone, Push, Pull, Pull Request, GitHub 인증, Branch Protection 과정에서 발생하는 문제를 해결하는 절차이다.

---

### [Troubleshooting]

문제:

```text
Repository not found
```

원인:

```text
Repository URL이 잘못되었거나 Private Repository 접근 권한이 없다.
```

해결:

```bash
git remote -v
git remote set-url origin <correct-url>
```

GitHub 권한 확인:

```text
Repository 접근 권한
Organization 초대 수락
Personal Access Token 권한
SSH Key 등록
```

---

문제:

```text
Authentication failed
```

원인:

```text
비밀번호 인증이 불가능하거나 Token / SSH Key 인증이 올바르지 않다.
```

해결:

```text
HTTPS 사용 시 Personal Access Token 확인
SSH 사용 시 SSH Key 등록 확인
Credential Manager 캐시 확인
```

---

문제:

```text
Push Rejected
```

원인:

```text
Remote Branch에 Local에 없는 Commit이 있다.
```

해결:

```bash
git fetch origin
git rebase origin/main
git push origin main
```

---

문제:

```text
Pull Request를 만들 Branch가 보이지 않음
```

원인:

```text
feature Branch를 Remote에 Push하지 않았다.
```

해결:

```bash
git push -u origin feature/login-api
```

---

문제:

```text
Merge 버튼이 비활성화됨
```

원인:

```text
Conflict, Review 미승인, CI 실패, Branch Protection 조건 미충족 가능성이 있다.
```

해결:

```text
Conflict 해결
Required Review 승인
Status Check 통과
Branch 최신화
```

---

문제:

```text
Remote Branch 삭제 후 목록에 계속 보임
```

원인:

```text
Local Remote Tracking 정보가 갱신되지 않았다.
```

해결:

```bash
git fetch --prune
```

---

문제:

```text
잘못된 Repository에 Push함
```

원인:

```text
origin URL이 잘못 설정되어 있다.
```

해결:

```bash
git remote -v
git remote set-url origin <correct-url>
```

잘못 올라간 민감 정보가 있다면 즉시 폐기 및 재발급한다.

---

### [FAQ]

Q. Repository not found는 왜 발생하는가?
A. Repository URL이 틀렸거나 Private Repository 접근 권한이 없을 때 발생한다.

Q. Authentication failed는 왜 발생하는가?
A. GitHub 인증 정보가 잘못되었거나 Token / SSH Key 권한이 없을 때 발생한다.

Q. Pull Request Branch가 보이지 않는 이유는?
A. Local feature Branch를 Remote에 Push하지 않았기 때문이다.

Q. Merge 버튼이 비활성화되는 이유는?
A. Conflict, Review 미승인, CI 실패, Branch Protection 조건 미충족 때문일 수 있다.

---

# 14. Remote GitHub Best Practice

## 14.1 Team Collaboration Best Practice

### [개념]

Remote GitHub Best Practice는 GitHub Remote Repository를 기준으로 팀 협업 품질을 높이기 위한 운영 규칙이다.

---

### [핵심]

- main 직접 Push 금지
- feature Branch 기반 작업
- Pull Request 기반 Merge
- Code Review 필수
- CI Check 통과 후 Merge
- Branch Protection 적용
- Issue와 PR 연결
- Merge 후 Branch 삭제
- Secrets 직접 Commit 금지
- Commit / Branch / PR Naming 통일

---

### [실무]

팀 프로젝트 권장 Workflow:

```text
Issue 생성
→ feature Branch 생성
→ Commit
→ Push
→ Pull Request 생성
→ GitHub Actions 실행
→ Code Review
→ Approval
→ Merge
→ Branch Delete
→ Issue Close
```

권장 규칙:

```text
Branch: feature/festival-search
Commit: feat: add festival search API
PR: feat: add festival search API
Issue: [Feature] Festival Search API
```

---

### [Checklist]

작업 시작 전:

- Issue가 있는가?
- 기준 Branch가 최신인가?
- feature Branch 이름이 명확한가?

Push 전:

- `git status` 확인했는가?
- 민감 정보가 없는가?
- Commit Message가 규칙에 맞는가?
- 테스트 또는 빌드 확인했는가?

Pull Request 생성 전:

- PR 제목이 명확한가?
- 변경 내용이 설명되어 있는가?
- 테스트 결과가 적혀 있는가?
- 관련 Issue가 연결되어 있는가?

Merge 전:

- Review 승인되었는가?
- CI Check가 통과했는가?
- Conflict가 없는가?
- Branch Protection 조건을 만족했는가?

Merge 후:

- feature Branch를 삭제했는가?
- Local main/develop을 최신화했는가?
- Issue가 닫혔는가?

---

### [주의]

GitHub 협업 품질은 Repository 규칙 통일에 달려 있다.

규칙 없는 Repository에서 자주 발생하는 문제:

```text
main 직접 Push
Commit Message 혼란
PR 설명 부족
Review 누락
Conflict 방치
Force Push 사고
Secrets 노출
Branch 난립
Issue 추적 실패
```

---

### [FAQ]

Q. GitHub 팀 협업 기본 흐름은?
A. Issue → Branch → Commit → Push → Pull Request → Review → Merge → Branch Delete 흐름을 권장한다.

Q. main 직접 Push를 막는 방법은?
A. GitHub Branch Protection Rules를 설정한다.

Q. PR에 테스트 결과를 적는 이유는?
A. Reviewer가 변경 검증 여부를 빠르게 판단할 수 있기 때문이다.

Q. Merge 후 해야 할 일은?
A. feature Branch를 삭제하고 Local 기준 Branch를 최신화하며 관련 Issue를 닫는다.

---

# Retrieval Queries

### [FAQ]

Q. Remote Repository란?
A. Remote Repository는 Git Repository를 원격 서버에 저장하고 팀과 공유하는 저장소이다.

Q. origin이란?
A. origin은 기본 Remote Repository 이름이다.

Q. GitHub는 무엇인가?
A. GitHub는 Git Repository를 원격으로 호스팅하고 Pull Request, Review, Issue 기능을 제공하는 협업 플랫폼이다.

Q. GitHub와 Git 차이는?
A. Git은 버전 관리 도구이고 GitHub는 Git 기반 원격 협업 플랫폼이다.

Q. git clone이란?
A. git clone은 Remote Repository를 로컬 PC에 복사하여 Local Repository를 만드는 명령이다.

Q. HTTPS Clone과 SSH Clone 차이는?
A. HTTPS는 계정/토큰 인증을 사용하고 SSH는 등록된 SSH Key 인증을 사용한다.

Q. 기존 프로젝트를 GitHub에 올리는 순서는?
A. git init → git add → git commit → git remote add origin → git push -u origin main 순서이다.

Q. git remote -v란?
A. 현재 Local Repository에 연결된 Remote Repository URL을 확인하는 명령이다.

Q. git remote add origin이란?
A. Local Repository에 origin이라는 Remote Repository를 추가하는 명령이다.

Q. git remote set-url origin이란?
A. origin Remote Repository URL을 변경하는 명령이다.

Q. git push란?
A. git push는 Local Repository의 Commit을 Remote Repository에 업로드하는 작업이다.

Q. git push -u란?
A. Push하면서 Local Branch와 Remote Branch의 upstream 추적 관계를 설정하는 옵션이다.

Q. Push는 Staging 파일을 올리는가?
A. 아니다. Push는 Commit을 Remote Repository에 업로드한다.

Q. Push Rejected란?
A. Remote Branch에 Local에 없는 Commit이 있거나 History가 달라 Push가 거부되는 상태이다.

Q. fetch first 에러는 왜 발생하는가?
A. Remote Branch에 Local에 없는 Commit이 있기 때문에 발생한다.

Q. non-fast-forward란?
A. Local History가 Remote History를 단순히 앞으로 이동시킬 수 없는 상태이다.

Q. Push Rejected 해결 방법은?
A. Remote 변경을 fetch 또는 pull로 반영한 뒤 다시 push한다.

Q. git fetch란?
A. git fetch는 Remote 변경 사항을 가져오지만 현재 Branch에 자동 통합하지 않는 작업이다.

Q. git fetch --prune이란?
A. Remote에서 삭제된 Branch의 Local Tracking 정보를 정리하는 명령이다.

Q. git pull이란?
A. git pull은 Remote 변경 사항을 가져오고 현재 Branch에 통합하는 작업이다.

Q. Pull과 Fetch 차이는?
A. Fetch는 가져오기만 하고 Pull은 가져온 뒤 현재 Branch에 Merge 또는 Rebase한다.

Q. git pull --rebase란?
A. Remote 변경 사항을 가져온 뒤 Local Commit을 그 위로 다시 쌓는 방식이다.

Q. Upstream Branch란?
A. Upstream Branch는 Local Branch가 추적하는 Remote Branch이다.

Q. git branch -vv란?
A. Local Branch와 Upstream Branch 연결 상태를 확인하는 명령이다.

Q. Pull Request란?
A. Pull Request는 Branch 변경 사항을 다른 Branch에 병합해 달라고 요청하는 GitHub 협업 기능이다.

Q. PR을 사용하는 이유는?
A. Code Review, 테스트 확인, 변경 이력 검토 후 안전하게 Merge하기 위해 사용한다.

Q. 좋은 Pull Request 기준은?
A. 작업 목적, 변경 내용, 테스트 결과, 영향 범위, 리뷰 포인트가 명확해야 한다.

Q. Pull Request Merge Strategy 종류는?
A. Merge Commit, Squash Merge, Rebase Merge가 대표적이다.

Q. Squash Merge란?
A. Pull Request의 여러 Commit을 하나의 Commit으로 압축하여 대상 Branch에 반영하는 방식이다.

Q. Code Review란?
A. Pull Request의 변경 사항을 검토하여 버그, 설계 문제, Convention 위반을 확인하는 협업 절차이다.

Q. Approval이란?
A. Reviewer가 Pull Request 변경 사항을 승인하여 Merge 가능하다고 판단하는 상태이다.

Q. Change Request란?
A. Merge 전 반드시 수정이 필요하다고 Reviewer가 요청하는 상태이다.

Q. GitHub Issue란?
A. 작업 항목, 버그, 요구사항, 개선 사항을 추적하는 GitHub 기능이다.

Q. Closes #12란?
A. Pull Request가 Merge되면 Issue #12를 자동으로 닫는 GitHub 키워드이다.

Q. Branch Protection이란?
A. GitHub에서 main 같은 중요 Branch를 보호하기 위한 Repository 설정이다.

Q. main 직접 Push를 막는 방법은?
A. GitHub Branch Protection Rules를 설정한다.

Q. Status Check Required란?
A. CI Check가 통과해야 Merge할 수 있게 하는 Branch Protection 규칙이다.

Q. GitHub Actions란?
A. GitHub에서 제공하는 CI/CD 자동화 기능이다.

Q. Workflow란?
A. GitHub Actions 자동화 작업을 정의하는 YAML 파일이다.

Q. GitHub Secrets란?
A. API Key, DB Password 같은 민감 정보를 안전하게 저장하고 Workflow에서 참조하는 기능이다.

Q. Git Tag란?
A. 특정 Commit에 버전 이름을 붙여 배포 기준점을 표시하는 Git 기능이다.

Q. GitHub Release란?
A. Tag를 기반으로 배포 버전과 변경 내역을 관리하는 GitHub 기능이다.

Q. Repository not found 원인은?
A. Repository URL이 틀렸거나 Private Repository 접근 권한이 없기 때문이다.

Q. Authentication failed 원인은?
A. GitHub 인증 정보가 잘못되었거나 Token / SSH Key 권한이 없기 때문이다.

Q. Pull Request Branch가 보이지 않는 이유는?
A. Local feature Branch를 Remote에 Push하지 않았기 때문이다.

Q. Merge 버튼이 비활성화되는 이유는?
A. Conflict, Review 미승인, CI 실패, Branch Protection 조건 미충족 때문일 수 있다.

Q. GitHub 팀 협업 기본 흐름은?
A. Issue → Branch → Commit → Push → Pull Request → Review → Merge → Branch Delete 흐름이다.
