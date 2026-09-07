# Git / GitHub Part03 Rebase Reset Revert Stash

---

# 1. Rebase

## 1.1 Rebase Core

### [개념]

Rebase는 현재 Branch의 Commit들을 다른 기준 Branch의 최신 Commit 위로 다시 쌓는 Git 작업이다.

Rebase는 Commit History를 재작성하여 Linear History를 만들 때 사용한다.

```text
Before

main:    A---B---C
feature:     \---D---E

After Rebase

main:    A---B---C
feature:             \---D'---E'
```

`D`, `E` Commit은 Rebase 후 `D'`, `E'`처럼 새로운 Commit Hash를 가진다.

---

### [핵심]

- Rebase = Commit을 새 기준 위로 다시 적용
- History Rewrite 발생
- Commit Hash 변경
- Linear History 유지 가능
- Merge Commit 없이 최신 코드 반영 가능
- 공유 Branch Rebase는 위험하다.

---

### [예제]

`feature/login-api` Branch에서 `main` 최신 Commit 위로 Rebase:

```bash
git switch feature/login-api
git rebase main
```

Rebase 중 Conflict 해결 후 계속 진행:

```bash
git add <conflict-file>
git rebase --continue
```

Rebase 중단:

```bash
git rebase --abort
```

특정 Commit 건너뛰기:

```bash
git rebase --skip
```

---

### [Flow]

```text
feature Branch 이동
→ 기준 Branch 최신화 확인
→ git rebase main
→ Conflict 발생 시 해결
→ git add
→ git rebase --continue
→ 테스트
→ push
```

---

### [실무]

2026 실무 기준 Rebase는 개인 feature Branch를 최신 `main` 또는 `develop` 기준으로 정리할 때 자주 사용한다.

주요 사용 상황:

- Pull Request 생성 전 feature Branch 최신화
- Merge Commit 없이 History 정리
- Local Commit 정리
- Linear History 유지
- Review 전 Commit 정돈

권장 흐름:

```bash
git switch main
git pull origin main
git switch feature/login-api
git rebase main
```

Remote에 이미 Push한 Branch를 Rebase한 경우 Force Push가 필요할 수 있다.

```bash
git push --force-with-lease origin feature/login-api
```

`--force-with-lease`는 단순 `--force`보다 안전하다.

---

### [주의]

공유 Branch에서 Rebase를 남용하면 팀원의 History와 충돌한다.

Rebase 금지 대상:

- `main`
- `develop`
- release Branch
- 여러 사람이 함께 작업 중인 Branch
- 이미 Merge된 Branch

Rebase 권장 대상:

- 본인만 사용하는 Local feature Branch
- Pull Request 전 정리 대상 Branch
- 아직 팀원이 기반으로 작업하지 않은 Branch

---

### [Comparison]

| 항목        | Merge                         | Rebase               |
| ----------- | ----------------------------- | -------------------- |
| 목적        | Branch 통합                   | Commit 재배치        |
| History     | Merge Commit 가능             | Linear History       |
| Commit Hash | 기존 Commit 유지              | Commit Hash 변경     |
| 안전성      | 공유 Branch에 상대적으로 안전 | 공유 Branch에서 위험 |
| 사용 상황   | 통합 기록 필요                | 이력 정리 필요       |

---

### [FAQ]

Q. Rebase는 무엇인가?
A. Rebase는 현재 Branch의 Commit들을 다른 기준 Branch의 최신 Commit 위로 다시 쌓는 작업이다.

Q. Rebase를 쓰는 이유는?
A. Merge Commit 없이 Linear History를 유지하고 feature Branch를 최신 기준 Branch 위로 정리하기 위해 사용한다.

Q. Rebase가 위험한 이유는?
A. Commit History를 재작성하고 Commit Hash를 변경하기 때문에 공유 Branch에서 사용하면 팀원 작업과 충돌할 수 있다.

Q. Rebase 후 Push가 거부되는 이유는?
A. Remote Branch의 Commit History와 Local Rebase 후 History가 달라졌기 때문이다.

---

# 2. Interactive Rebase

## 2.1 Interactive Rebase Core

### [개념]

Interactive Rebase는 여러 Commit을 수정, 합치기, 삭제, 순서 변경할 수 있는 Rebase 방식이다.

주로 Pull Request 전 Commit History를 정리할 때 사용한다.

---

### [핵심]

- Interactive Rebase = Commit History 편집
- Commit Message 수정 가능
- 여러 Commit을 하나로 Squash 가능
- 불필요한 Commit 삭제 가능
- Commit 순서 변경 가능
- 이미 공유된 Commit에는 주의 필요

---

### [예제]

최근 3개 Commit 편집:

```bash
git rebase -i HEAD~3
```

Interactive Rebase 명령 예시:

```text
pick 1a2b3c4 feat: add login controller
pick 2b3c4d5 fix: typo
pick 3c4d5e6 refactor: extract auth service
```

Commit 합치기:

```text
pick 1a2b3c4 feat: add login controller
squash 2b3c4d5 fix: typo
pick 3c4d5e6 refactor: extract auth service
```

Commit Message만 수정:

```text
reword 1a2b3c4 feat: add login controller
pick 2b3c4d5 fix: token validation
```

Commit 삭제:

```text
pick 1a2b3c4 feat: add login controller
drop 2b3c4d5 test commit
```

---

### [실무]

Pull Request 전 Commit이 지저분할 때 Interactive Rebase로 정리한다.

정리 대상 Commit 예시:

```text
fix typo
review fix
real final
test
remove console
```

정리 후:

```text
feat: add login API
```

자주 쓰는 명령:

| Command | 의미                              |
| ------- | --------------------------------- |
| pick    | Commit 유지                       |
| reword  | Commit Message 수정               |
| edit    | Commit 내용 수정                  |
| squash  | 이전 Commit과 합치고 Message 편집 |
| fixup   | 이전 Commit과 합치고 Message 버림 |
| drop    | Commit 삭제                       |

---

### [Flow]

```text
git log --oneline
→ 정리할 Commit 범위 확인
→ git rebase -i HEAD~N
→ pick / squash / reword 선택
→ 저장
→ Conflict 발생 시 해결
→ git rebase --continue
→ 테스트
```

---

### [주의]

Interactive Rebase는 History Rewrite 작업이다.

이미 Remote에 Push했고 다른 팀원이 기반으로 작업한 Commit은 수정하지 않는다.

Commit을 삭제하면 해당 변경 내용이 사라질 수 있다.

Squash 범위를 잘못 잡으면 필요한 Commit까지 합쳐질 수 있다.

---

### [FAQ]

Q. Interactive Rebase는 무엇인가?
A. Interactive Rebase는 여러 Commit을 수정, 합치기, 삭제, 순서 변경할 수 있는 Rebase 방식이다.

Q. git rebase -i HEAD~3은 무엇인가?
A. 최근 3개 Commit을 대화형으로 편집하는 명령이다.

Q. squash와 fixup 차이는?
A. squash는 Commit Message를 합치거나 수정하고, fixup은 이전 Commit Message만 유지한다.

Q. Interactive Rebase는 언제 쓰는가?
A. Pull Request 전 Commit History를 정리하거나 Commit Message를 수정할 때 사용한다.

---

# 3. Cherry Pick

## 3.1 Cherry Pick Core

### [개념]

Cherry Pick은 특정 Commit 하나 또는 여러 개를 현재 Branch에 선택적으로 적용하는 Git 작업이다.

전체 Branch를 Merge하지 않고 필요한 Commit만 가져올 때 사용한다.

---

### [핵심]

- Cherry Pick = 특정 Commit 선택 적용
- Branch 전체가 아니라 Commit 단위 적용
- 현재 Branch에 새로운 Commit으로 적용됨
- 원본 Commit과 다른 Commit Hash를 가질 수 있음
- Hotfix, 누락 Commit 반영, 잘못된 Branch 작업 복구에 사용

---

### [예제]

특정 Commit 하나 적용:

```bash
git cherry-pick a1b2c3d
```

여러 Commit 적용:

```bash
git cherry-pick a1b2c3d e4f5g6h
```

범위 적용:

```bash
git cherry-pick a1b2c3d..e4f5g6h
```

Cherry Pick 중 Conflict 해결 후 계속:

```bash
git add <conflict-file>
git cherry-pick --continue
```

Cherry Pick 중단:

```bash
git cherry-pick --abort
```

---

### [Flow]

```text
필요 Commit Hash 확인
→ 대상 Branch 이동
→ git cherry-pick commit-hash
→ Conflict 발생 시 해결
→ 테스트
→ Push
```

---

### [실무]

Cherry Pick은 다음 상황에서 사용한다.

- 잘못된 Branch에 Commit한 내용을 올바른 Branch로 이동
- release Branch에 특정 bugfix Commit만 반영
- main에는 반영하지 않고 hotfix Branch에 특정 Commit만 반영
- 다른 기능 Branch의 일부 수정만 가져오기

예시:

```text
feature/payment에 잘못 Commit
→ feature/login으로 이동
→ git cherry-pick <commit-hash>
```

명령:

```bash
git switch feature/login
git cherry-pick 9f8e7d6
```

---

### [주의]

Cherry Pick은 중복 Commit을 만들 수 있다.

이미 Merge된 Commit을 다시 Cherry Pick하면 중복 변경이나 Conflict가 발생할 수 있다.

범위 Cherry Pick은 시작 Commit이 포함되지 않는 방식에 주의한다.

```bash
git cherry-pick A..D
```

위 명령은 `A` 다음 Commit부터 `D`까지 적용한다.

`A`도 포함하려면 다음처럼 사용한다.

```bash
git cherry-pick A^..D
```

---

### [FAQ]

Q. Cherry Pick은 무엇인가?
A. Cherry Pick은 특정 Commit을 현재 Branch에 선택적으로 적용하는 Git 작업이다.

Q. Cherry Pick은 언제 쓰는가?
A. 특정 Commit만 가져오거나 잘못된 Branch의 Commit을 올바른 Branch로 옮길 때 사용한다.

Q. Cherry Pick하면 Commit Hash가 유지되는가?
A. 대부분 새 Commit으로 적용되므로 Commit Hash가 달라질 수 있다.

Q. Cherry Pick 중 Conflict가 발생하면?
A. 충돌 파일을 수정하고 `git add` 후 `git cherry-pick --continue`를 실행한다.

---

# 4. Reset

## 4.1 Reset Core

### [개념]

Reset은 현재 Branch의 HEAD를 특정 Commit으로 이동시키는 Git 작업이다.

Reset은 Commit을 되돌리거나 Staging 상태를 변경할 때 사용한다.

Reset은 옵션에 따라 Working Directory, Staging Area, Commit History에 미치는 영향이 다르다.

---

### [핵심]

- Reset = HEAD 이동
- Commit History를 변경할 수 있음
- `--soft` = Commit만 취소
- `--mixed` = Commit + Staging 취소
- `--hard` = Commit + Staging + Working Directory 변경 제거
- 공유 Branch에서 Reset 후 Force Push는 위험하다.

---

### [Comparison]

| 옵션      | Commit 취소 | Staging 유지 | Working Directory 유지 | 위험도 |
| --------- | ----------- | ------------ | ---------------------- | ------ |
| `--soft`  | O           | O            | O                      | 낮음   |
| `--mixed` | O           | X            | O                      | 중간   |
| `--hard`  | O           | X            | X                      | 높음   |

---

### [예제]

최근 Commit만 취소하고 변경 사항은 Staging 유지:

```bash
git reset --soft HEAD~1
```

최근 Commit 취소 후 Staging도 취소, 파일 변경은 유지:

```bash
git reset --mixed HEAD~1
```

최근 Commit과 파일 변경 모두 제거:

```bash
git reset --hard HEAD~1
```

특정 파일 Staging 취소:

```bash
git reset HEAD <file>
```

---

### [Flow]

```text
되돌릴 범위 확인
→ git log --oneline
→ reset 옵션 선택
→ git reset --soft/mixed/hard HEAD~N
→ 상태 확인
→ 필요 시 다시 Commit
```

---

### [실무]

Reset은 Local Commit 정리에 자주 사용한다.

사용 상황:

- 방금 만든 Commit Message 수정
- Commit을 쪼개기 위해 되돌림
- 잘못 Staging한 파일 제거
- Local에서만 만든 불필요한 Commit 제거
- Push 전 Commit 정리

Commit Message만 수정하려면 Reset보다 amend가 더 간단하다.

```bash
git commit --amend -m "fix: update token validation"
```

---

### [주의]

`git reset --hard`는 Working Directory 변경 사항을 삭제한다.

복구가 어려울 수 있으므로 실행 전 반드시 확인한다.

```bash
git status
git log --oneline
```

Remote에 Push한 Commit을 Reset하고 Force Push하면 팀원 History를 깨뜨릴 수 있다.

공유 Branch에서는 Reset 대신 Revert를 우선 고려한다.

---

### [FAQ]

Q. Reset은 무엇인가?
A. Reset은 현재 Branch의 HEAD를 특정 Commit으로 이동시키는 Git 작업이다.

Q. git reset --soft는 무엇인가?
A. Commit만 취소하고 변경 사항은 Staging Area에 유지한다.

Q. git reset --mixed는 무엇인가?
A. Commit과 Staging을 취소하고 파일 변경은 Working Directory에 유지한다.

Q. git reset --hard는 무엇인가?
A. Commit, Staging, Working Directory 변경을 모두 되돌리는 위험한 명령이다.

---

# 5. Revert

## 5.1 Revert Core

### [개념]

Revert는 기존 Commit의 변경 내용을 반대로 적용하는 새로운 Commit을 생성하여 변경을 취소하는 Git 작업이다.

Reset과 달리 기존 Commit History를 삭제하지 않는다.

---

### [핵심]

- Revert = 기록 유지 Undo
- 기존 Commit을 삭제하지 않음
- 취소 Commit을 새로 생성
- 공유 Branch에서 안전한 Undo 방식
- main, develop, release Branch에서 권장
- Conflict 발생 가능

---

### [예제]

특정 Commit 되돌리기:

```bash
git revert a1b2c3d
```

여러 Commit 되돌리기:

```bash
git revert a1b2c3d e4f5g6h
```

Commit 생성 없이 변경만 적용:

```bash
git revert --no-commit a1b2c3d
```

Revert 중 Conflict 해결 후 계속:

```bash
git add <conflict-file>
git revert --continue
```

Revert 중단:

```bash
git revert --abort
```

---

### [Flow]

```text
되돌릴 Commit 확인
→ git revert commit-hash
→ Conflict 발생 시 해결
→ Revert Commit 생성
→ 테스트
→ Push
```

---

### [실무]

실무에서 Remote에 이미 Push된 Commit은 Reset보다 Revert로 되돌리는 것이 안전하다.

사용 상황:

- main에 Merge된 기능 취소
- 배포 후 장애 Commit 롤백
- 공유 Branch의 잘못된 Commit 취소
- History를 유지하면서 변경만 제거

예시:

```text
main에 잘못된 Commit Merge
→ git revert <commit-hash>
→ Revert Commit Push
→ 변경 취소 기록 유지
```

---

### [주의]

Revert는 Commit History를 삭제하지 않는다.

기존 Commit과 Revert Commit이 모두 남는다.

Revert 대상 Commit 이후 코드가 많이 바뀌었다면 Conflict가 발생할 수 있다.

Merge Commit을 Revert할 때는 mainline 옵션이 필요할 수 있다.

```bash
git revert -m 1 <merge-commit-hash>
```

---

### [Comparison]

| 항목         | Reset      | Revert                |
| ------------ | ---------- | --------------------- |
| 방식         | HEAD 이동  | 반대 변경 Commit 생성 |
| History      | 변경 가능  | 유지                  |
| 공유 Branch  | 위험       | 안전                  |
| 사용 상황    | Local 정리 | Remote 반영 후 취소   |
| Push 후 사용 | 주의 필요  | 권장                  |

---

### [FAQ]

Q. Revert는 무엇인가?
A. Revert는 기존 Commit의 변경 내용을 반대로 적용하는 새 Commit을 만들어 변경을 취소하는 작업이다.

Q. Revert가 Reset보다 안전한 이유는?
A. Commit History를 삭제하지 않고 취소 기록을 남기기 때문이다.

Q. Push한 Commit을 되돌릴 때 Reset을 써도 되는가?
A. 공유 Branch에서는 Reset보다 Revert를 사용하는 것이 안전하다.

Q. Merge Commit을 Revert하려면?
A. `git revert -m 1 <merge-commit-hash>`처럼 mainline 옵션이 필요할 수 있다.

---

# 6. Stash

## 6.1 Stash Core

### [개념]

Stash는 Commit하지 않은 Working Directory 변경 사항을 임시로 저장하는 Git 기능이다.

Branch 이동, Pull, Rebase 전 현재 작업을 잠시 보관할 때 사용한다.

---

### [핵심]

- Stash = 작업 임시 저장
- Commit 없이 변경 사항 보관
- Branch 이동 전 유용
- Pull / Rebase 전 작업 보존
- 필요할 때 다시 적용 가능
- Stash는 임시 저장소이므로 장기 보관 용도는 아니다.

---

### [예제]

현재 변경 사항 Stash:

```bash
git stash
```

메시지와 함께 Stash:

```bash
git stash push -m "wip login form"
```

Untracked 파일까지 포함:

```bash
git stash -u
```

Stash 목록 확인:

```bash
git stash list
```

최근 Stash 적용 후 목록에서 제거:

```bash
git stash pop
```

최근 Stash 적용만 하고 목록 유지:

```bash
git stash apply
```

특정 Stash 적용:

```bash
git stash apply stash@{1}
```

Stash 삭제:

```bash
git stash drop stash@{0}
```

전체 Stash 삭제:

```bash
git stash clear
```

---

### [Flow]

```text
작업 중 변경 발생
→ 긴급 Branch 이동 필요
→ git stash push -m "wip message"
→ 다른 작업 수행
→ 원래 Branch 복귀
→ git stash pop
→ 작업 계속
```

---

### [실무]

Stash는 다음 상황에서 자주 사용한다.

- 작업 중 다른 Branch로 이동해야 할 때
- Pull 전에 Local 변경을 잠시 보관할 때
- Rebase 전에 충돌 가능 변경을 치워야 할 때
- 아직 Commit하기 애매한 WIP 작업을 잠시 저장할 때

예시:

```bash
git stash push -m "wip festival search filter"
git switch main
git pull origin main
git switch feature/festival-search
git stash pop
```

---

### [주의]

Stash는 임시 저장 용도이다.

중요 작업은 Stash에 오래 두지 않고 Commit하는 것이 안전하다.

`git stash pop`은 적용 후 Stash 목록에서 제거한다.

Conflict가 발생할 수 있으므로 `pop`보다 `apply`가 안전할 때도 있다.

Untracked 파일은 기본 `git stash`에 포함되지 않는다.

Untracked 파일까지 저장하려면 `git stash -u`를 사용한다.

---

### [FAQ]

Q. Stash는 무엇인가?
A. Stash는 Commit하지 않은 변경 사항을 임시로 저장하는 Git 기능이다.

Q. git stash pop과 apply 차이는?
A. pop은 Stash를 적용하고 목록에서 제거하며, apply는 적용만 하고 목록에는 유지한다.

Q. Untracked 파일도 Stash되는가?
A. 기본적으로 포함되지 않는다. `git stash -u`를 사용해야 한다.

Q. Stash는 오래 보관해도 되는가?
A. 권장하지 않는다. 중요한 작업은 Commit으로 저장하는 것이 안전하다.

---

# 7. Amend

## 7.1 Commit Amend

### [개념]

Amend는 가장 최근 Commit을 수정하는 Git 작업이다.

Commit Message를 바꾸거나 빠진 파일을 마지막 Commit에 추가할 때 사용한다.

---

### [핵심]

- Amend = 최근 Commit 수정
- 마지막 Commit Message 수정 가능
- 빠진 파일을 마지막 Commit에 포함 가능
- Commit Hash 변경
- 이미 Push한 Commit Amend는 주의 필요
- History Rewrite에 해당한다.

---

### [예제]

최근 Commit Message 수정:

```bash
git commit --amend -m "feat: add login API"
```

빠진 파일을 마지막 Commit에 추가:

```bash
git add src/main/java/LoginService.java
git commit --amend --no-edit
```

---

### [Flow]

```text
최근 Commit 확인
→ 수정 파일 Staging
→ git commit --amend
→ Commit Hash 변경
→ 필요 시 Push
```

---

### [실무]

Amend는 Push 전 Commit 수정에 적합하다.

사용 상황:

- Commit Message 오타 수정
- 빠진 파일을 직전 Commit에 추가
- 불필요한 작은 수정 Commit을 만들지 않고 마지막 Commit에 포함
- Pull Request 전 마지막 Commit 정리

예:

```text
feat: add login cotroller
```

수정:

```bash
git commit --amend -m "feat: add login controller"
```

---

### [주의]

Amend는 최근 Commit을 새 Commit으로 바꾼다.

이미 Remote에 Push한 Commit을 Amend하면 Force Push가 필요할 수 있다.

공유 Branch에서는 Amend 사용을 피한다.

Push 후 수정이 필요하면 새 Commit을 추가하거나 Revert를 고려한다.

---

### [FAQ]

Q. Amend는 무엇인가?
A. Amend는 가장 최근 Commit의 내용이나 Commit Message를 수정하는 작업이다.

Q. Commit Message 오타는 어떻게 수정하는가?
A. `git commit --amend -m "new message"` 명령을 사용한다.

Q. 빠진 파일을 마지막 Commit에 추가하려면?
A. 파일을 `git add` 한 뒤 `git commit --amend --no-edit`을 실행한다.

Q. Amend도 History Rewrite인가?
A. 맞다. 최근 Commit Hash가 변경된다.

---

# 8. Restore And Checkout

## 8.1 Restore

### [개념]

Restore는 Working Directory 또는 Staging Area의 변경 사항을 되돌리는 Git 명령이다.

파일 변경 취소와 Staging 취소에 사용한다.

---

### [핵심]

- `git restore <file>` = Working Directory 변경 취소
- `git restore --staged <file>` = Staging 취소
- Commit History는 변경하지 않음
- 파일 단위 복구에 적합
- 잘못 사용하면 수정 내용이 사라질 수 있음

---

### [예제]

파일 변경 취소:

```bash
git restore src/main/java/UserService.java
```

Staging 취소:

```bash
git restore --staged src/main/java/UserService.java
```

특정 Commit 기준 파일 복구:

```bash
git restore --source a1b2c3d src/main/java/UserService.java
```

---

### [실무]

실무에서는 `git restore --staged`를 Commit 대상에서 파일을 제외할 때 자주 사용한다.

예시:

```text
git add . 실행
→ .env가 Staging됨
→ git restore --staged .env
→ .gitignore 확인
```

명령:

```bash
git restore --staged .env
```

---

### [주의]

`git restore <file>`은 Working Directory의 수정 내용을 버린다.

복구 전 `git diff`로 변경 내용을 확인한다.

```bash
git diff src/main/java/UserService.java
```

Staging 취소는 파일 변경을 삭제하지 않는다.

```bash
git restore --staged <file>
```

---

### [FAQ]

Q. git restore는 무엇인가?
A. Working Directory 또는 Staging Area의 변경 사항을 되돌리는 명령이다.

Q. Staging을 취소하려면?
A. `git restore --staged <file>` 명령을 사용한다.

Q. 파일 수정 내용을 버리려면?
A. `git restore <file>` 명령을 사용한다.

Q. git restore --staged는 파일 변경을 삭제하는가?
A. 아니다. Staging만 취소하고 Working Directory 변경은 유지한다.

---

# 9. Troubleshooting

## 9.1 Rebase Reset Revert Stash Troubleshooting

### [개념]

Rebase, Reset, Revert, Stash Troubleshooting은 Git History 수정, 변경 취소, 임시 저장 과정에서 발생하는 문제를 해결하는 절차이다.

---

### [Troubleshooting]

문제:

```text
Rebase 중 Conflict 발생
```

원인:

```text
현재 Branch Commit을 새 기준 Branch 위에 다시 적용하는 과정에서 같은 코드 영역이 충돌했다.
```

해결:

```bash
git status
# conflict 파일 수정
git add <file>
git rebase --continue
```

중단:

```bash
git rebase --abort
```

---

문제:

```text
Rebase 후 Push가 거부됨
```

원인:

```text
Rebase로 Commit Hash가 변경되어 Remote History와 Local History가 달라졌다.
```

해결:

```bash
git push --force-with-lease origin feature/login-api
```

주의:

```text
공유 Branch에서는 Force Push 전 팀원과 반드시 확인한다.
```

---

문제:

```text
git reset --hard 후 파일이 사라짐
```

원인:

```text
Working Directory 변경 사항까지 모두 제거했다.
```

해결:

```bash
git reflog
```

필요 시 이전 HEAD로 복구:

```bash
git reset --hard HEAD@{1}
```

주의:

```text
Untracked 파일은 복구가 어려울 수 있다.
```

---

문제:

```text
Push한 Commit을 잘못 되돌리고 싶음
```

원인:

```text
Remote에 이미 반영된 Commit을 취소해야 한다.
```

해결:

```bash
git revert <commit-hash>
git push origin main
```

---

문제:

```text
Stash 한 작업이 보이지 않음
```

원인:

```text
Stash 목록을 확인하지 않았거나 pop으로 이미 제거되었다.
```

해결:

```bash
git stash list
```

pop으로 제거 후 복구가 필요하면 Reflog 확인:

```bash
git reflog
```

---

문제:

```text
Stash 적용 중 Conflict 발생
```

원인:

```text
Stash에 저장된 변경과 현재 Branch 코드가 같은 영역을 수정했다.
```

해결:

```bash
git status
# conflict 파일 수정
git add <file>
```

---

문제:

```text
잘못된 Commit을 다른 Branch로 옮기고 싶음
```

원인:

```text
작업 Branch를 확인하지 않고 Commit했다.
```

해결:

```bash
git log --oneline
git switch correct-branch
git cherry-pick <commit-hash>
```

기존 Branch에서 제거가 필요하면:

```bash
git switch wrong-branch
git reset --soft HEAD~1
```

---

### [FAQ]

Q. Rebase 중 Conflict가 나면?
A. 충돌 파일을 수정하고 `git add` 후 `git rebase --continue`를 실행한다.

Q. Rebase를 취소하려면?
A. `git rebase --abort`를 사용한다.

Q. Rebase 후 Push가 안 되면?
A. History가 변경된 것이므로 본인 Branch라면 `git push --force-with-lease`를 사용한다.

Q. Reset 실수를 복구하려면?
A. `git reflog`로 이전 HEAD를 찾고 필요 시 `git reset --hard HEAD@{n}`으로 복구한다.

---

# 10. Best Practice

## 10.1 History Control Best Practice

### [개념]

History Control Best Practice는 Git History를 안전하고 명확하게 관리하기 위한 Rebase, Reset, Revert, Stash 사용 기준이다.

---

### [핵심]

- 공유 Branch는 Rebase보다 Merge 또는 Revert 우선
- Push 전 Local Commit은 Rebase, Reset, Amend로 정리 가능
- Push 후 공개 Commit은 Revert로 취소
- `reset --hard` 전 반드시 `git status` 확인
- Force Push는 `--force-with-lease` 사용
- Stash는 임시 저장 용도로만 사용
- 중요한 작업은 Commit으로 남긴다.

---

### [실무]

권장 판단 기준:

| 상황                     | 권장 명령                     |
| ------------------------ | ----------------------------- |
| Commit Message 오타 수정 | git commit --amend            |
| Push 전 최근 Commit 취소 | git reset --soft HEAD~1       |
| Push 전 Commit 쪼개기    | git reset --mixed HEAD~1      |
| 파일 수정 내용 버리기    | git restore <file>            |
| Staging 취소             | git restore --staged <file>   |
| Push 후 Commit 취소      | git revert <commit-hash>      |
| feature Branch 최신화    | git rebase main               |
| 특정 Commit만 가져오기   | git cherry-pick <commit-hash> |
| 작업 임시 저장           | git stash push -m "message"   |

---

### [Checklist]

Rebase 전:

- 본인만 쓰는 Branch인가?
- 기준 Branch가 최신인가?
- Working Directory가 깨끗한가?
- Push 후 Force Push가 필요한 상황인가?

Reset 전:

- 어떤 옵션을 사용할지 정했는가?
- Working Directory 변경을 보존해야 하는가?
- `--hard`가 필요한 상황이 맞는가?
- Remote에 Push한 Commit은 아닌가?

Revert 전:

- 취소할 Commit Hash가 맞는가?
- Merge Commit인지 확인했는가?
- Revert 후 테스트 계획이 있는가?

Stash 전:

- Untracked 파일도 포함해야 하는가?
- Stash 메시지를 남겼는가?
- 장기 보관용으로 쓰고 있지 않은가?

---

### [주의]

Git History 변경 명령은 실행 전 상태 확인이 필수이다.

기본 확인 명령:

```bash
git status
git log --oneline
git branch
```

위험 명령:

```bash
git reset --hard
git push --force
git rebase shared-branch
git stash clear
```

대체 권장:

```bash
git push --force-with-lease
git revert <commit-hash>
git stash apply
```

---

### [FAQ]

Q. Push 전 Commit을 정리하려면?
A. Rebase, Reset, Amend를 사용할 수 있다.

Q. Push 후 Commit을 취소하려면?
A. 공유 Branch에서는 Revert를 사용하는 것이 안전하다.

Q. Force Push는 언제 쓰는가?
A. Rebase나 Amend로 Remote와 Local History가 달라졌고, 본인 Branch임이 확실할 때 사용한다.

Q. reset --hard는 언제 피해야 하는가?
A. 보존해야 할 Working Directory 변경 사항이 있을 때는 피해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Rebase란?
A. Rebase는 현재 Branch의 Commit들을 다른 기준 Branch의 최신 Commit 위로 다시 쌓는 Git 작업이다.

Q. Rebase를 쓰는 이유는?
A. Merge Commit 없이 Linear History를 유지하고 feature Branch를 최신 기준 Branch 위로 정리하기 위해 사용한다.

Q. Rebase가 위험한 이유는?
A. Commit History를 재작성하고 Commit Hash를 변경하기 때문에 공유 Branch에서 사용하면 충돌 위험이 있다.

Q. git rebase main은 무엇인가?
A. 현재 Branch의 Commit들을 main Branch 최신 Commit 위로 다시 적용하는 명령이다.

Q. Rebase 중 Conflict가 발생하면?
A. 충돌 파일을 수정하고 `git add` 후 `git rebase --continue`를 실행한다.

Q. Rebase를 취소하려면?
A. `git rebase --abort` 명령을 사용한다.

Q. Rebase 후 Push가 거부되는 이유는?
A. Rebase로 Commit Hash가 변경되어 Remote History와 Local History가 달라졌기 때문이다.

Q. Rebase 후 Push하려면?
A. 본인 Branch라면 `git push --force-with-lease`를 사용한다.

Q. Interactive Rebase란?
A. Interactive Rebase는 여러 Commit을 수정, 합치기, 삭제, 순서 변경할 수 있는 Rebase 방식이다.

Q. git rebase -i HEAD~3이란?
A. 최근 3개 Commit을 대화형으로 편집하는 명령이다.

Q. squash란?
A. squash는 현재 Commit을 이전 Commit과 합치고 Commit Message를 편집하는 Interactive Rebase 명령이다.

Q. fixup이란?
A. fixup은 현재 Commit을 이전 Commit과 합치되 현재 Commit Message는 버리는 명령이다.

Q. Cherry Pick이란?
A. Cherry Pick은 특정 Commit을 현재 Branch에 선택적으로 적용하는 Git 작업이다.

Q. Cherry Pick은 언제 쓰는가?
A. 특정 Commit만 가져오거나 잘못된 Branch의 Commit을 올바른 Branch로 옮길 때 사용한다.

Q. git cherry-pick commit-hash란?
A. 지정한 Commit의 변경 내용을 현재 Branch에 새 Commit으로 적용하는 명령이다.

Q. Cherry Pick 중 Conflict가 나면?
A. 충돌 파일을 수정하고 `git add` 후 `git cherry-pick --continue`를 실행한다.

Q. Reset이란?
A. Reset은 현재 Branch의 HEAD를 특정 Commit으로 이동시키는 Git 작업이다.

Q. git reset --soft란?
A. Commit만 취소하고 변경 사항은 Staging Area에 유지하는 명령이다.

Q. git reset --mixed란?
A. Commit과 Staging을 취소하고 파일 변경은 Working Directory에 유지하는 명령이다.

Q. git reset --hard란?
A. Commit, Staging, Working Directory 변경을 모두 되돌리는 위험한 명령이다.

Q. Reset과 Revert 차이는?
A. Reset은 History를 변경하고 Revert는 기존 History를 유지하며 반대 변경 Commit을 만든다.

Q. Revert란?
A. Revert는 기존 Commit의 변경 내용을 반대로 적용하는 새 Commit을 생성하여 변경을 취소하는 작업이다.

Q. Push한 Commit을 되돌리려면?
A. 공유 Branch에서는 `git revert <commit-hash>`를 사용하는 것이 안전하다.

Q. Merge Commit Revert는 어떻게 하는가?
A. `git revert -m 1 <merge-commit-hash>`처럼 mainline 옵션을 지정한다.

Q. Stash란?
A. Stash는 Commit하지 않은 Working Directory 변경 사항을 임시로 저장하는 Git 기능이다.

Q. git stash pop이란?
A. 최근 Stash를 적용하고 Stash 목록에서 제거하는 명령이다.

Q. git stash apply란?
A. Stash를 적용하되 Stash 목록에는 유지하는 명령이다.

Q. Untracked 파일도 Stash하려면?
A. `git stash -u`를 사용한다.

Q. Amend란?
A. Amend는 가장 최근 Commit의 내용이나 Commit Message를 수정하는 작업이다.

Q. Commit Message 오타 수정은?
A. `git commit --amend -m "new message"` 명령을 사용한다.

Q. 빠진 파일을 마지막 Commit에 추가하려면?
A. 파일을 `git add` 한 뒤 `git commit --amend --no-edit`을 실행한다.

Q. git restore란?
A. Working Directory 또는 Staging Area의 변경 사항을 되돌리는 명령이다.

Q. Staging을 취소하려면?
A. `git restore --staged <file>` 명령을 사용한다.

Q. 파일 수정 내용을 버리려면?
A. `git restore <file>` 명령을 사용한다.

Q. Git History 정리 기준은?
A. Push 전 Local Commit은 Rebase, Reset, Amend로 정리하고 Push 후 공유 Commit은 Revert로 취소한다.

Q. Force Push를 안전하게 하려면?
A. 단순 `--force`보다 `--force-with-lease`를 사용한다.

Q. reset --hard 전 확인할 것은?
A. `git status`, `git log --oneline`으로 삭제될 변경 사항과 HEAD 위치를 확인해야 한다.
