# Git / GitHub Part01 Core

---

# 1. Git Core

## 1.1 Git

### [개념]

Git은 Distributed Version Control System이다.

Git은 파일 변경 이력을 Commit 단위로 저장하고, Branch를 통해 독립 작업 흐름을 관리한다.

Git은 로컬 환경에서도 버전 관리가 가능하며, Remote Repository와 동기화하여 팀 협업을 지원한다.

---

### [핵심]

- Git = Version Control Tool
- GitHub = Remote Hosting Platform
- Commit = 변경 이력 Snapshot
- Branch = 독립 작업 공간
- Repository = Git이 추적하는 프로젝트 저장소
- Remote Repository = GitHub 같은 외부 저장소
- Git은 변경 내용을 파일 단위가 아니라 Snapshot 흐름으로 관리한다.

---

### [실무]

2026 실무 기준 Git은 거의 모든 Backend / Frontend / DevOps 프로젝트의 기본 협업 도구이다.

실무에서는 Git 단독보다 GitHub, GitLab, Bitbucket 같은 Remote Hosting Platform과 함께 사용한다.

일반적인 개발 흐름:

```text
Local Code 수정
→ git add
→ git commit
→ git push
→ Pull Request
→ Code Review
→ Merge
```

실무에서 Git을 사용하는 이유:

- 코드 변경 이력 추적
- 작업자별 Branch 분리
- 기능 단위 개발 관리
- Pull Request 기반 Code Review
- 배포 전 변경 내역 검증
- 문제 발생 시 특정 Commit 기준 복구

---

### [주의]

Git과 GitHub를 혼동하면 안 된다.

```text
Git = 버전 관리 도구
GitHub = Git 저장소를 원격으로 관리하는 플랫폼
```

Git은 로컬 PC에서도 동작한다.

GitHub는 Git Repository를 원격에서 공유하고 협업하기 위한 서비스이다.

---

### [FAQ]

Q. Git은 무엇인가?
A. Git은 코드 변경 이력을 Commit 단위로 관리하는 Distributed Version Control System이다.

Q. GitHub는 Git과 같은 것인가?
A. 아니다. Git은 버전 관리 도구이고, GitHub는 Git Repository를 원격으로 호스팅하는 플랫폼이다.

Q. Git을 쓰는 이유는?
A. 변경 이력 추적, 협업, Branch 분리, 코드 리뷰, 문제 복구를 위해 사용한다.

Q. Git은 인터넷이 없어도 사용할 수 있는가?
A. 가능하다. Git은 로컬 저장소에서 Commit과 Branch 관리가 가능하다. 단, Remote Repository 동기화는 인터넷이 필요하다.

---

# 2. Repository

## 2.1 Repository

### [개념]

Repository는 Git이 파일 변경 이력을 추적하는 프로젝트 저장소이다.

Repository는 Local Repository와 Remote Repository로 구분한다.

```text
Local Repository
→ 개발자 PC에 존재하는 Git 저장소

Remote Repository
→ GitHub / GitLab / Bitbucket 같은 원격 저장소
```

---

### [핵심]

- Repository = Git 프로젝트 저장소
- Local Repository = 개발자 로컬 PC 저장소
- Remote Repository = 원격 서버 저장소
- `.git` 디렉터리가 Git Repository의 핵심 메타데이터를 저장한다.
- Remote Repository는 협업과 백업을 담당한다.

---

### [실무]

실무 프로젝트는 보통 Remote Repository를 먼저 만들고, 로컬에서 clone 받아 작업한다.

```bash
git clone https://github.com/example/project.git
```

기존 로컬 프로젝트를 Git Repository로 만들 때는 `git init`을 사용한다.

```bash
git init
```

Remote Repository 연결은 `git remote add origin`을 사용한다.

```bash
git remote add origin https://github.com/example/project.git
```

---

### [Flow]

```text
Remote Repository 생성
→ git clone
→ Local Repository 생성
→ Code 수정
→ Commit
→ Push
→ Remote Repository 반영
```

---

### [주의]

`.git` 디렉터리를 삭제하면 Git 이력 정보가 사라진다.

프로젝트 폴더에 `.git`이 없으면 Git Repository가 아니다.

Remote Repository가 있어도 로컬 Commit을 Push하지 않으면 GitHub에 반영되지 않는다.

---

### [FAQ]

Q. Repository는 무엇인가?
A. Repository는 Git이 파일 변경 이력을 추적하는 프로젝트 저장소이다.

Q. Local Repository와 Remote Repository 차이는?
A. Local Repository는 내 PC의 저장소이고, Remote Repository는 GitHub 같은 외부 서버의 저장소이다.

Q. GitHub Repository는 Remote Repository인가?
A. 맞다. GitHub Repository는 Git 원격 저장소 역할을 한다.

Q. git clone은 무엇을 하는 명령인가?
A. Remote Repository를 로컬 PC에 복사하여 Local Repository를 생성한다.

---

# 3. Git File States

## 3.1 Working Directory

### [개념]

Working Directory는 개발자가 실제로 파일을 수정하는 작업 공간이다.

Git은 Working Directory의 파일 상태를 추적한다.

주요 상태:

- Untracked
- Modified
- Staged
- Committed

---

### [핵심]

- Working Directory = 실제 코드 수정 공간
- Untracked = Git이 아직 추적하지 않는 새 파일
- Modified = Git이 추적 중이고 수정된 파일
- Staged = Commit 준비 영역에 올라간 파일
- Committed = Local Repository에 저장된 상태

---

### [실무]

파일 상태 확인은 `git status`를 사용한다.

```bash
git status
```

자주 보는 상태:

```text
Untracked files
Changes not staged for commit
Changes to be committed
```

실무에서는 Commit 전 반드시 `git status`로 포함될 파일을 확인한다.

---

### [Flow]

```text
파일 생성
→ Untracked
→ git add
→ Staged
→ git commit
→ Committed
```

```text
파일 수정
→ Modified
→ git add
→ Staged
→ git commit
→ Committed
```

---

### [주의]

Untracked 파일은 `git add` 전까지 Commit 대상이 아니다.

Modified 파일도 `git add` 하지 않으면 Commit에 포함되지 않는다.

`git status` 확인 없이 `git add .`를 사용하면 원하지 않는 파일이 Commit에 포함될 수 있다.

---

### [FAQ]

Q. Working Directory는 무엇인가?
A. Working Directory는 개발자가 실제로 코드를 수정하는 로컬 작업 공간이다.

Q. Untracked는 무엇인가?
A. Git이 아직 추적하지 않는 새 파일 상태이다.

Q. Modified는 무엇인가?
A. Git이 추적 중인 파일이 수정되었지만 아직 Staging Area에 올라가지 않은 상태이다.

Q. 파일을 수정했는데 Commit에 안 들어가는 이유는?
A. 수정 파일을 `git add`로 Staging Area에 올리지 않았기 때문이다.

---

## 3.2 Staging Area

### [개념]

Staging Area는 Commit에 포함할 변경 사항을 임시로 준비하는 영역이다.

`git add` 명령으로 Working Directory의 변경 사항을 Staging Area에 올린다.

---

### [핵심]

- Staging Area = Commit 전 준비 영역
- `git add` = Staging Area에 변경 사항 추가
- 선택적 Commit 가능
- 하나의 파일 일부만 Staging할 수도 있다.
- 좋은 Commit 품질은 Staging Area 관리에서 시작된다.

---

### [예제]

전체 변경 파일 Staging:

```bash
git add .
```

특정 파일만 Staging:

```bash
git add src/main/java/UserService.java
```

일부 변경만 Staging:

```bash
git add -p
```

---

### [실무]

실무에서는 관련 변경만 묶어서 Commit하는 것이 중요하다.

좋은 Commit 흐름:

```text
관련 파일만 git add
→ git status 확인
→ git commit
```

나쁜 Commit 흐름:

```text
모든 변경 git add .
→ 확인 없이 commit
→ 불필요한 파일 포함
```

---

### [주의]

`git add .`는 편하지만 위험할 수 있다.

다음 파일이 의도치 않게 포함될 수 있다.

- `.env`
- 빌드 결과물
- 로그 파일
- IDE 설정 파일
- 테스트용 임시 파일

Commit 전 반드시 `git status`를 확인한다.

---

### [FAQ]

Q. Staging Area는 무엇인가?
A. Staging Area는 Commit에 포함할 변경 사항을 준비하는 임시 영역이다.

Q. git add는 무엇을 하는가?
A. Working Directory의 변경 사항을 Staging Area에 올린다.

Q. git add .는 안전한가?
A. 항상 안전하지는 않다. 의도하지 않은 파일이 포함될 수 있으므로 `git status` 확인이 필요하다.

Q. 선택적 Commit은 어떻게 하는가?
A. 관련 파일만 `git add <file>`로 Staging한 뒤 Commit한다.

---

# 4. Commit

## 4.1 Commit

### [개념]

Commit은 Git Repository에 저장되는 변경 이력 Snapshot이다.

Commit은 특정 시점의 프로젝트 상태를 기록한다.

각 Commit은 고유한 Hash를 가진다.

---

### [핵심]

- Commit = 변경 이력 Snapshot
- Commit Hash = Commit 고유 식별자
- Commit Message = 변경 이유 설명
- Commit은 Local Repository에 저장된다.
- Push 전까지 Remote Repository에는 반영되지 않는다.

---

### [예제]

```bash
git commit -m "feat: add login API"
```

Commit 이력 확인:

```bash
git log
```

간단한 Commit 이력 확인:

```bash
git log --oneline
```

---

### [실무]

실무에서는 Commit Message를 명확하게 작성한다.

권장 형식:

```text
type: subject
```

Conventional Commit 예시:

```text
feat: add user login API
fix: resolve token validation error
refactor: extract festival search service
docs: update README
test: add user service unit test
```

주요 type:

| Type     | 의미                     |
| -------- | ------------------------ |
| feat     | 기능 추가                |
| fix      | 버그 수정                |
| refactor | 기능 변경 없는 구조 개선 |
| docs     | 문서 변경                |
| test     | 테스트 추가/수정         |
| chore    | 빌드, 설정, 기타 작업    |

---

### [Best Practice]

좋은 Commit 기준:

- 하나의 Commit은 하나의 목적만 가진다.
- Commit Message는 변경 이유를 설명한다.
- 너무 많은 변경을 한 Commit에 넣지 않는다.
- 빌드 실패 상태를 Commit하지 않는다.
- 민감 정보가 포함되지 않았는지 확인한다.

---

### [주의]

Commit은 로컬 저장소에만 저장된다.

GitHub에 반영하려면 `git push`가 필요하다.

민감 정보가 Commit되면 삭제가 어렵다.

주의 파일:

- `.env`
- API Key
- Secret Key
- DB Password
- Token
- 인증서 파일

---

### [FAQ]

Q. Commit은 무엇인가?
A. Commit은 Git Repository에 저장되는 변경 이력 Snapshot이다.

Q. Commit Message는 왜 중요한가?
A. 변경 이유와 목적을 빠르게 파악하게 해주며 Code Review와 문제 추적에 필요하다.

Q. Commit하면 GitHub에 바로 올라가는가?
A. 아니다. Commit은 Local Repository에 저장되고, GitHub 반영은 `git push`가 필요하다.

Q. 좋은 Commit 기준은?
A. 하나의 목적만 담고, 변경 이유가 명확하며, 불필요한 파일이 포함되지 않아야 한다.

---

# 5. Git Basic Workflow

## 5.1 Local Basic Workflow

### [개념]

Git 기본 흐름은 Working Directory의 변경 사항을 Staging Area에 올리고, Commit으로 Local Repository에 저장하는 과정이다.

---

### [핵심]

- `git status` = 상태 확인
- `git add` = Staging
- `git commit` = Snapshot 저장
- `git log` = 이력 확인
- `git diff` = 변경 차이 확인

---

### [예제]

기본 Commit 흐름:

```bash
git status
git add .
git status
git commit -m "feat: add festival list API"
git log --oneline
```

변경 내용 확인:

```bash
git diff
```

Staging된 변경 확인:

```bash
git diff --staged
```

---

### [Flow]

```text
Code 수정
→ git status
→ git diff
→ git add
→ git status
→ git diff --staged
→ git commit
→ git log --oneline
```

---

### [실무]

실무에서는 Commit 전 아래 순서를 권장한다.

```text
1. git status
2. git diff
3. git add <related-files>
4. git diff --staged
5. git commit -m "type: message"
```

이 흐름은 불필요한 파일 Commit을 줄이고, Commit 품질을 높인다.

---

### [주의]

`git commit -am`은 Untracked 파일을 포함하지 않는다.

```bash
git commit -am "fix: update login validation"
```

위 명령은 이미 Git이 추적 중인 Modified 파일만 Staging 후 Commit한다.

새 파일은 별도 `git add`가 필요하다.

---

### [FAQ]

Q. Git 기본 작업 순서는?
A. `git status → git add → git commit` 순서가 기본이다.

Q. git diff는 언제 사용하는가?
A. Commit 전 실제 변경 내용을 확인할 때 사용한다.

Q. git diff와 git diff --staged 차이는?
A. `git diff`는 아직 Staging되지 않은 변경을 보여주고, `git diff --staged`는 Commit 예정 변경을 보여준다.

Q. git commit -am은 새 파일도 포함하는가?
A. 아니다. Git이 이미 추적 중인 Modified 파일만 포함한다.

---

# 6. Git Ignore

## 6.1 .gitignore

### [개념]

`.gitignore`는 Git이 추적하지 않아야 할 파일과 디렉터리를 지정하는 설정 파일이다.

---

### [핵심]

- `.gitignore` = Git 추적 제외 규칙
- 민감 정보 제외
- 빌드 결과물 제외
- 로컬 IDE 설정 제외
- 로그 파일 제외
- OS 임시 파일 제외

---

### [예제]

Spring Boot / Java 프로젝트 예시:

```gitignore
/build/
/.gradle/
*.class
*.log
.env
application-local.properties
```

Node / React 프로젝트 예시:

```gitignore
node_modules/
build/
dist/
.env
.env.local
npm-debug.log
```

VS Code 예시:

```gitignore
.vscode/
```

단, 팀 공통 설정이 필요한 경우 일부 파일은 예외적으로 추적할 수 있다.

```gitignore
.vscode/*
!.vscode/extensions.json
!.vscode/settings.json
```

---

### [실무]

실무에서는 프로젝트 초기 설정 시 `.gitignore`를 먼저 작성한다.

특히 아래 파일은 Git에 올리지 않는다.

- `.env`
- Secret Key
- API Key
- DB Password
- Build Output
- Log File
- Local IDE Cache

이미 추적 중인 파일은 `.gitignore`에 추가해도 자동 제외되지 않는다.

Git 캐시에서 제거해야 한다.

```bash
git rm --cached .env
```

디렉터리 제거:

```bash
git rm -r --cached .vscode
```

---

### [주의]

`.gitignore`는 아직 Git이 추적하지 않는 파일에만 적용된다.

이미 Commit된 파일은 별도 제거 작업이 필요하다.

민감 정보가 이미 Commit되었다면 단순 삭제 Commit만으로는 완전 제거되지 않는다.

필요 시 Key 폐기, Secret 재발급, Git History Rewrite가 필요하다.

---

### [FAQ]

Q. .gitignore는 무엇인가?
A. Git이 추적하지 않을 파일과 디렉터리를 지정하는 설정 파일이다.

Q. .gitignore에 추가했는데 계속 추적되는 이유는?
A. 이미 Git이 추적 중인 파일이기 때문이다. `git rm --cached`로 캐시에서 제거해야 한다.

Q. .env는 Git에 올려도 되는가?
A. 안 된다. API Key, DB Password 같은 민감 정보가 포함될 수 있다.

Q. .vscode는 무조건 제외해야 하는가?
A. 개인 설정은 제외하는 것이 일반적이다. 팀 공통 설정은 예외적으로 일부 파일만 추적할 수 있다.

---

# 7. Git Command Summary

## 7.1 Core Commands

### [개념]

Git Core Command는 Repository 생성, 상태 확인, Staging, Commit, 이력 확인에 사용되는 기본 명령이다.

---

### [핵심]

| Command         | 목적                                |
| --------------- | ----------------------------------- |
| git init        | 현재 폴더를 Git Repository로 초기화 |
| git clone       | Remote Repository 복사              |
| git status      | 파일 상태 확인                      |
| git add         | Staging Area에 변경 추가            |
| git commit      | Commit 생성                         |
| git log         | Commit 이력 확인                    |
| git diff        | 변경 차이 확인                      |
| git rm --cached | Git 추적만 제거                     |

---

### [예제]

```bash
git init
git status
git add .
git commit -m "feat: initial commit"
git log --oneline
```

---

### [실무]

Core Command는 모든 Git Workflow의 기반이다.

Branch, Merge, Rebase, Pull Request도 결국 Commit 이력을 기준으로 동작한다.

따라서 Git 학습은 아래 순서가 좋다.

```text
Repository
→ Working Directory
→ Staging Area
→ Commit
→ Branch
→ Merge
→ Remote
→ Pull Request
```

---

### [FAQ]

Q. Git에서 가장 먼저 익혀야 할 명령은?
A. `git status`, `git add`, `git commit`, `git log`, `git diff`이다.

Q. git status는 왜 자주 써야 하는가?
A. 현재 변경 파일, Staging 상태, Commit 대상 파일을 확인할 수 있기 때문이다.

Q. git log --oneline은 언제 쓰는가?
A. Commit 이력을 간단하게 확인할 때 사용한다.

Q. git rm --cached는 파일을 삭제하는가?
A. 로컬 파일은 유지하고 Git 추적 대상에서만 제거한다.

---

# 8. Common Mistakes

## 8.1 Git Core Mistakes

### [개념]

Git Core Mistake는 Staging, Commit, Ignore, Repository 개념을 잘못 이해해서 발생하는 기본 오류이다.

---

### [핵심]

자주 발생하는 실수:

- Git과 GitHub 혼동
- `git add .` 남용
- Commit 전 `git status` 미확인
- 불필요한 파일 Commit
- `.env` Commit
- `.gitignore` 적용 방식 오해
- 너무 큰 단위의 Commit
- Commit Message 부실
- 새 파일을 `git commit -am`으로 Commit하려고 함

---

### [Troubleshooting]

문제:

```text
.env를 .gitignore에 추가했는데 계속 Git에 잡힘
```

원인:

```text
이미 Git이 해당 파일을 추적 중이다.
```

해결:

```bash
git rm --cached .env
git commit -m "chore: remove env file from git tracking"
```

---

문제:

```text
새 파일이 Commit되지 않음
```

원인:

```text
Untracked 파일을 git add 하지 않았다.
```

해결:

```bash
git add <file>
git commit -m "feat: add new file"
```

---

문제:

```text
원하지 않는 파일이 Commit에 포함됨
```

원인:

```text
git add . 사용 후 Staging 상태를 확인하지 않았다.
```

해결:

```bash
git restore --staged <file>
```

---

### [Best Practice]

Git Core Best Practice:

- Commit 전 `git status` 확인
- Commit 전 `git diff` 확인
- 관련 파일만 Staging
- `.gitignore` 프로젝트 초기에 설정
- Commit Message 규칙 통일
- 민감 정보 Commit 금지
- 하나의 Commit에는 하나의 목적만 포함

---

### [FAQ]

Q. Git 초보자가 가장 많이 하는 실수는?
A. `git add .` 후 확인 없이 Commit하여 불필요한 파일이나 민감 정보를 포함하는 것이다.

Q. Commit을 잘게 나누는 이유는?
A. 변경 이유 추적, Code Review, 문제 발생 시 Rollback이 쉬워지기 때문이다.

Q. .env를 Commit했다면 어떻게 해야 하는가?
A. 파일을 Git 추적에서 제거하고, 노출된 Key나 Password는 즉시 폐기 후 재발급해야 한다.

Q. Staging 실수를 되돌리려면?
A. `git restore --staged <file>` 명령으로 Staging Area에서 제거한다.

---

# Retrieval Queries

### [FAQ]

Q. Git이란?
A. Git은 코드 변경 이력을 Commit 단위로 관리하는 Distributed Version Control System이다.

Q. GitHub란?
A. GitHub는 Git Repository를 원격으로 저장하고 협업을 지원하는 Remote Hosting Platform이다.

Q. Git과 GitHub 차이는?
A. Git은 버전 관리 도구이고 GitHub는 Git 저장소 호스팅 플랫폼이다.

Q. Repository란?
A. Repository는 Git이 파일 변경 이력을 추적하는 프로젝트 저장소이다.

Q. Local Repository란?
A. Local Repository는 개발자 PC에 존재하는 Git 저장소이다.

Q. Remote Repository란?
A. Remote Repository는 GitHub 같은 외부 서버에 존재하는 Git 저장소이다.

Q. Working Directory란?
A. Working Directory는 개발자가 실제로 파일을 수정하는 작업 공간이다.

Q. Untracked란?
A. Untracked는 Git이 아직 추적하지 않는 새 파일 상태이다.

Q. Modified란?
A. Modified는 Git이 추적 중인 파일이 수정되었지만 아직 Staging되지 않은 상태이다.

Q. Staging Area란?
A. Staging Area는 Commit에 포함할 변경 사항을 준비하는 임시 영역이다.

Q. git add란?
A. git add는 Working Directory의 변경 사항을 Staging Area에 올리는 명령이다.

Q. git add .는 무엇인가?
A. git add .는 현재 경로 기준 모든 변경 사항을 Staging Area에 추가하는 명령이다.

Q. Commit이란?
A. Commit은 Git Repository에 저장되는 변경 이력 Snapshot이다.

Q. Commit Message란?
A. Commit Message는 Commit에 포함된 변경 이유와 목적을 설명하는 문장이다.

Q. Conventional Commit이란?
A. Conventional Commit은 feat, fix, refactor 같은 type으로 Commit Message를 구조화하는 규칙이다.

Q. git status란?
A. git status는 Working Directory와 Staging Area의 파일 상태를 확인하는 명령이다.

Q. git diff란?
A. git diff는 아직 Staging되지 않은 변경 차이를 확인하는 명령이다.

Q. git diff --staged란?
A. git diff --staged는 Commit 예정인 Staging Area 변경 차이를 확인하는 명령이다.

Q. git log --oneline이란?
A. git log --oneline은 Commit 이력을 한 줄 형식으로 간단히 확인하는 명령이다.

Q. .gitignore란?
A. .gitignore는 Git이 추적하지 않을 파일과 디렉터리를 지정하는 설정 파일이다.

Q. .gitignore가 적용되지 않는 이유는?
A. 이미 Git이 추적 중인 파일은 .gitignore에 추가해도 계속 추적되기 때문이다.

Q. git rm --cached란?
A. git rm --cached는 로컬 파일은 유지하고 Git 추적 대상에서만 제거하는 명령이다.

Q. .env를 Git에 올리면 안 되는 이유는?
A. API Key, DB Password, Secret Key 같은 민감 정보가 노출될 수 있기 때문이다.

Q. git commit -am은 새 파일을 포함하는가?
A. 아니다. git commit -am은 이미 Git이 추적 중인 Modified 파일만 포함한다.

Q. Staging을 취소하려면?
A. git restore --staged <file> 명령을 사용한다.

Q. Git 기본 흐름은?
A. git status → git add → git commit 순서가 기본 흐름이다.

Q. Commit 전 확인할 것은?
A. git status, git diff, git diff --staged로 변경 파일과 Commit 대상을 확인해야 한다.

Q. 좋은 Commit 기준은?
A. 하나의 목적만 포함하고 변경 이유가 명확하며 불필요한 파일이 없어야 한다.

Q. Git Core에서 가장 중요한 개념은?
A. Working Directory, Staging Area, Commit, Repository 흐름이다.
