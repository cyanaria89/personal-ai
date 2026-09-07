# Git / GitHub Part02 Branch Merge

---

# 1. Branch

## 1.1 Branch Core

### [개념]

Branch는 Git에서 독립적인 작업 흐름을 만들기 위한 포인터이다.

Branch는 특정 Commit을 기준으로 분기하며, 다른 Branch의 코드에 직접 영향을 주지 않고 기능 개발, 버그 수정, 실험 작업을 진행할 수 있게 한다.

---

### [핵심]

- Branch = 독립 작업 공간
- Branch는 Commit을 가리키는 포인터이다.
- 기본 Branch는 보통 `main` 또는 `master`이다.
- 기능 개발은 `feature/*` Branch에서 진행한다.
- Branch는 협업 충돌을 줄이고 작업 단위를 분리한다.
- Branch 작업 후 Merge 또는 Pull Request로 통합한다.

---

### [실무]

2026 실무 기준 대부분의 팀 프로젝트는 `main` 직접 작업을 금지하고 Branch 기반 Workflow를 사용한다.

일반적인 기능 개발 흐름:

```text
main 최신화
→ feature Branch 생성
→ 기능 개발
→ Commit
→ Push
→ Pull Request
→ Review
→ Merge
```

Branch 생성:

```bash
git branch feature/login
```

Branch 이동:

```bash
git switch feature/login
```

Branch 생성과 이동을 동시에 수행:

```bash
git switch -c feature/login
```

현재 Branch 확인:

```bash
git branch
```

---

### [Flow]

```text
main
→ git switch -c feature/login
→ Code 수정
→ git add
→ git commit
→ git push origin feature/login
→ Pull Request
```

---

### [주의]

`main` Branch에서 직접 기능 개발하지 않는다.

작업 전 `main`을 최신화하지 않으면 오래된 코드에서 Branch가 생성되어 충돌 가능성이 높아진다.

Branch 이름은 기능 목적이 드러나야 한다.

나쁜 예:

```text
test
mybranch
abc
work
```

좋은 예:

```text
feature/login-api
fix/token-validation
refactor/festival-search-service
docs/update-readme
```

---

### [FAQ]

Q. Branch는 무엇인가?
A. Branch는 특정 Commit을 기준으로 독립적인 작업 흐름을 만드는 Git 포인터이다.

Q. Branch를 사용하는 이유는?
A. 기능 개발, 버그 수정, 실험 작업을 독립적으로 진행하고 main 코드에 직접 영향을 주지 않기 위해 사용한다.

Q. main Branch에서 직접 작업해도 되는가?
A. 실무에서는 보통 금지한다. 기능별 Branch를 만들고 Pull Request로 통합하는 방식이 안전하다.

Q. git switch -c는 무엇인가?
A. 새 Branch를 생성하고 동시에 해당 Branch로 이동하는 명령이다.

---

# 2. Branch Naming

## 2.1 Branch Naming Convention

### [개념]

Branch Naming Convention은 Branch의 목적과 작업 범위를 이름만 보고 파악할 수 있게 하는 규칙이다.

---

### [핵심]

- Branch 이름은 작업 목적을 드러내야 한다.
- Prefix를 사용해 작업 유형을 구분한다.
- 팀 단위 Convention을 통일한다.
- Issue 번호를 포함할 수 있다.
- Branch 이름은 소문자와 하이픈 사용을 권장한다.

---

### [실무]

권장 Branch Prefix:

| Prefix   | 목적        | 예시                  |
| -------- | ----------- | --------------------- |
| feature  | 기능 개발   | feature/login-api     |
| fix      | 버그 수정   | fix/jwt-expired-error |
| refactor | 구조 개선   | refactor/user-service |
| docs     | 문서 수정   | docs/update-readme    |
| test     | 테스트 추가 | test/user-service     |
| chore    | 설정/기타   | chore/update-gradle   |
| hotfix   | 긴급 수정   | hotfix/payment-error  |
| release  | 배포 준비   | release/v1.0.0        |

Issue 번호를 포함하는 방식:

```text
feature/123-login-api
fix/215-refresh-token-error
```

팀 프로젝트 권장 형식:

```text
type/short-description
```

---

### [Best Practice]

좋은 Branch 이름:

```text
feature/festival-search
feature/kakao-map-marker
fix/oauth-login-redirect
refactor/notification-service
docs/api-spec
```

나쁜 Branch 이름:

```text
jun
test1
final
real-final
new
```

---

### [주의]

Branch 이름에 공백을 사용하지 않는다.

개인 이름만 사용하는 Branch는 목적 파악이 어렵다.

너무 긴 Branch 이름은 CLI와 Pull Request 목록에서 가독성이 떨어진다.

---

### [FAQ]

Q. Branch 이름은 어떻게 짓는가?
A. `type/short-description` 형식을 권장한다. 예: `feature/login-api`, `fix/token-error`.

Q. feature Branch는 언제 사용하는가?
A. 새 기능을 개발할 때 사용한다.

Q. fix Branch는 언제 사용하는가?
A. 버그를 수정할 때 사용한다.

Q. Branch 이름에 Issue 번호를 넣어도 되는가?
A. 가능하다. Issue 추적이 필요한 팀에서는 `feature/123-login-api`처럼 사용한다.

---

# 3. Branch Management

## 3.1 Branch Check And Delete

### [개념]

Branch Management는 Branch 목록 확인, 이동, 삭제, 최신화 등 Branch 상태를 관리하는 작업이다.

---

### [핵심]

- `git branch` = Local Branch 목록 확인
- `git branch -r` = Remote Branch 목록 확인
- `git branch -a` = Local + Remote Branch 목록 확인
- `git switch` = Branch 이동
- `git branch -d` = Merge된 Branch 삭제
- `git branch -D` = 강제 삭제
- 작업이 끝난 Branch는 정리한다.

---

### [예제]

Local Branch 목록 확인:

```bash
git branch
```

Remote Branch 목록 확인:

```bash
git branch -r
```

모든 Branch 확인:

```bash
git branch -a
```

Branch 이동:

```bash
git switch develop
```

Merge 완료된 Local Branch 삭제:

```bash
git branch -d feature/login-api
```

강제 삭제:

```bash
git branch -D feature/login-api
```

Remote Branch 삭제:

```bash
git push origin --delete feature/login-api
```

---

### [실무]

Pull Request가 Merge된 후에는 Local Branch와 Remote Branch를 정리한다.

정리 흐름:

```text
Pull Request Merge 완료
→ main 최신화
→ Local feature Branch 삭제
→ Remote feature Branch 삭제 확인
```

명령 흐름:

```bash
git switch main
git pull origin main
git branch -d feature/login-api
git push origin --delete feature/login-api
```

---

### [주의]

`git branch -D`는 Merge되지 않은 Branch도 삭제한다.

삭제 전 Branch에 필요한 Commit이 남아 있는지 확인한다.

Remote Branch 삭제는 팀원에게 영향을 줄 수 있으므로 Pull Request Merge 여부를 확인한다.

---

### [FAQ]

Q. Local Branch 목록은 어떻게 확인하는가?
A. `git branch` 명령으로 확인한다.

Q. Remote Branch 목록은 어떻게 확인하는가?
A. `git branch -r` 명령으로 확인한다.

Q. Branch 삭제는 어떻게 하는가?
A. Merge된 Local Branch는 `git branch -d <branch>`로 삭제한다.

Q. git branch -d와 -D 차이는?
A. `-d`는 Merge된 Branch만 삭제하고, `-D`는 Merge 여부와 관계없이 강제 삭제한다.

---

# 4. Merge

## 4.1 Merge Core

### [개념]

Merge는 두 Branch의 변경 이력을 하나의 Branch로 통합하는 Git 작업이다.

주로 feature Branch에서 개발한 기능을 `develop` 또는 `main` Branch에 반영할 때 사용한다.

---

### [핵심]

- Merge = Branch 변경 이력 통합
- Merge 대상 Branch로 이동한 뒤 실행한다.
- Merge는 Commit History에 영향을 준다.
- Fast Forward Merge와 Merge Commit 방식이 있다.
- 충돌이 발생하면 Conflict Resolve가 필요하다.

---

### [예제]

`feature/login-api` Branch를 `develop`에 Merge:

```bash
git switch develop
git merge feature/login-api
```

Merge 후 Push:

```bash
git push origin develop
```

---

### [Flow]

```text
feature/login-api 작업 완료
→ develop 이동
→ git merge feature/login-api
→ Conflict 확인
→ 테스트
→ git push origin develop
```

---

### [실무]

실무에서는 로컬에서 직접 Merge하기보다 GitHub Pull Request에서 Merge하는 경우가 많다.

일반적인 GitHub Merge 흐름:

```text
Feature Branch Push
→ Pull Request 생성
→ Code Review
→ CI Test
→ Merge
→ Branch Delete
```

로컬 Merge는 다음 상황에서 자주 사용한다.

- 개인 프로젝트
- 간단한 Branch 통합
- Conflict 사전 확인
- develop Branch 최신 코드 반영 테스트

---

### [주의]

Merge는 현재 위치한 Branch에 다른 Branch를 통합한다.

다음 명령은 `feature/login-api`를 `develop`에 넣는 명령이다.

```bash
git switch develop
git merge feature/login-api
```

반대로 실행하면 develop이 feature Branch에 들어간다.

Merge 전 현재 Branch를 반드시 확인한다.

```bash
git branch
```

---

### [FAQ]

Q. Merge는 무엇인가?
A. Merge는 두 Branch의 변경 이력을 하나의 Branch로 통합하는 Git 작업이다.

Q. Merge는 어느 Branch에서 실행해야 하는가?
A. 변경 내용을 받을 Branch로 이동한 뒤 실행해야 한다.

Q. feature Branch를 main에 반영하려면?
A. `main`으로 이동한 뒤 `git merge feature-branch`를 실행하거나 Pull Request로 Merge한다.

Q. Merge 전에 확인할 것은?
A. 현재 Branch, 작업 상태, 최신화 여부, 테스트 통과 여부를 확인해야 한다.

---

# 5. Fast Forward Merge

## 5.1 Fast Forward

### [개념]

Fast Forward Merge는 현재 Branch에 추가 Commit이 없고, 대상 Branch의 Commit만 앞으로 이어 붙일 수 있을 때 발생하는 Merge 방식이다.

Merge Commit을 만들지 않고 Branch 포인터만 앞으로 이동한다.

---

### [핵심]

- Fast Forward = Branch 포인터만 이동
- Merge Commit 생성 없음
- History가 단순하다.
- feature Branch 이력이 그대로 이어진다.
- 현재 Branch에 별도 Commit이 없을 때 가능하다.

---

### [Flow]

```text
main:    A---B
feature:     \---C---D

Fast Forward Merge 후

main:    A---B---C---D
```

---

### [예제]

```bash
git switch main
git merge feature/login-api
```

Fast Forward를 허용하지 않고 Merge Commit을 만들기:

```bash
git merge --no-ff feature/login-api
```

---

### [실무]

Fast Forward Merge는 이력이 단순해지는 장점이 있다.

하지만 기능 단위 Merge 기록이 명확히 남지 않을 수 있다.

팀에 따라 다음 전략 중 하나를 선택한다.

| 전략              | 특징                         |
| ----------------- | ---------------------------- |
| Fast Forward 허용 | History 단순                 |
| --no-ff 사용      | 기능 Branch Merge 기록 명확  |
| Squash Merge      | Commit 여러 개를 하나로 압축 |

---

### [주의]

Fast Forward Merge는 Merge Commit이 없기 때문에 어떤 기능 Branch가 언제 통합되었는지 추적이 어려울 수 있다.

협업 프로젝트에서는 GitHub Pull Request 기록과 함께 관리하는 것이 좋다.

---

### [FAQ]

Q. Fast Forward Merge란?
A. 현재 Branch 포인터를 대상 Branch의 최신 Commit으로 이동하는 Merge 방식이다.

Q. Fast Forward Merge는 Merge Commit을 만드는가?
A. 아니다. Merge Commit 없이 Branch 포인터만 이동한다.

Q. --no-ff는 무엇인가?
A. Fast Forward가 가능한 상황에서도 Merge Commit을 강제로 생성하는 옵션이다.

Q. Fast Forward Merge는 언제 가능한가?
A. 현재 Branch에 대상 Branch 분기 이후 새로운 Commit이 없을 때 가능하다.

---

# 6. Merge Commit

## 6.1 Merge Commit

### [개념]

Merge Commit은 두 Branch의 이력을 통합할 때 생성되는 Commit이다.

Merge Commit은 부모 Commit을 두 개 이상 가진다.

---

### [핵심]

- Merge Commit = Branch 통합 기록
- 부모 Commit이 2개 이상이다.
- 기능 Branch 통합 시점을 명확히 남긴다.
- History가 복잡해질 수 있다.
- 협업에서 작업 흐름 추적에 유리하다.

---

### [Flow]

```text
main:    A---B-------M
              \     /
feature:       C---D
```

`M`은 Merge Commit이다.

---

### [예제]

Merge Commit 강제 생성:

```bash
git switch main
git merge --no-ff feature/login-api
```

Merge Commit Message 작성:

```text
Merge branch 'feature/login-api'
```

---

### [실무]

Merge Commit은 기능 단위 통합 기록을 남기고 싶을 때 사용한다.

GitHub에서 Pull Request를 `Create a merge commit` 방식으로 Merge하면 Merge Commit이 생성된다.

팀 프로젝트에서는 아래 기준으로 선택한다.

| 방식         | 사용 상황                             |
| ------------ | ------------------------------------- |
| Merge Commit | 기능 Branch 통합 기록이 필요할 때     |
| Squash Merge | 작은 Commit들을 하나로 합치고 싶을 때 |
| Rebase Merge | Linear History를 유지하고 싶을 때     |

---

### [주의]

Merge Commit이 많아지면 Git History가 복잡해진다.

불필요한 중간 Merge를 반복하면 이력 추적이 어려워진다.

팀에서 Merge Strategy를 통일해야 한다.

---

### [FAQ]

Q. Merge Commit은 무엇인가?
A. 두 Branch의 변경 이력을 통합할 때 생성되는 Commit이다.

Q. Merge Commit의 장점은?
A. 어떤 Branch가 언제 통합되었는지 기록으로 남길 수 있다.

Q. Merge Commit의 단점은?
A. History가 복잡해질 수 있다.

Q. GitHub Pull Request Merge는 Merge Commit을 만들 수 있는가?
A. 가능하다. `Create a merge commit` 방식을 선택하면 Merge Commit이 생성된다.

---

# 7. Squash Merge

## 7.1 Squash Merge

### [개념]

Squash Merge는 feature Branch의 여러 Commit을 하나의 Commit으로 압축하여 대상 Branch에 반영하는 Merge 방식이다.

---

### [핵심]

- Squash Merge = 여러 Commit을 하나로 압축
- 대상 Branch History를 깔끔하게 유지한다.
- feature Branch의 세부 Commit 이력은 대상 Branch에 그대로 남지 않는다.
- Pull Request 단위 변경 기록에 적합하다.
- GitHub에서 자주 사용하는 Merge Strategy이다.

---

### [예제]

로컬 Squash Merge:

```bash
git switch main
git merge --squash feature/login-api
git commit -m "feat: add login API"
```

GitHub에서는 Pull Request Merge 시 `Squash and merge`를 선택한다.

---

### [Flow]

```text
feature Branch Commit 5개
→ Squash Merge
→ main Branch에는 Commit 1개로 반영
```

---

### [실무]

Squash Merge는 다음 상황에 적합하다.

- feature Branch에 작은 수정 Commit이 많은 경우
- Commit Message 품질이 일정하지 않은 경우
- main History를 기능 단위로 깔끔하게 유지하고 싶은 경우
- Pull Request 하나를 하나의 변경 단위로 관리하고 싶은 경우

예:

```text
fix typo
fix test
update code
real final
review fix
```

위 Commit들을 하나로 압축:

```text
feat: add login API
```

---

### [주의]

Squash Merge 후 feature Branch의 개별 Commit Hash는 main에 유지되지 않는다.

세부 Commit 단위 추적이 필요한 프로젝트에서는 적합하지 않을 수 있다.

Squash Merge 후 같은 Branch를 계속 재사용하면 충돌이 복잡해질 수 있으므로 Merge 후 Branch 삭제를 권장한다.

---

### [FAQ]

Q. Squash Merge란?
A. feature Branch의 여러 Commit을 하나의 Commit으로 압축하여 대상 Branch에 반영하는 방식이다.

Q. Squash Merge는 언제 사용하는가?
A. main History를 깔끔하게 유지하고 Pull Request 단위로 변경을 관리하고 싶을 때 사용한다.

Q. Squash Merge의 단점은?
A. feature Branch의 세부 Commit 이력이 대상 Branch에 그대로 남지 않는다.

Q. Squash Merge 후 Branch를 계속 써도 되는가?
A. 권장하지 않는다. Squash Merge 후에는 Branch를 삭제하고 새 Branch를 만드는 것이 안전하다.

---

# 8. Merge Conflict

## 8.1 Conflict Core

### [개념]

Merge Conflict는 Git이 두 Branch의 변경 내용을 자동으로 합칠 수 없을 때 발생한다.

주로 같은 파일의 같은 위치를 서로 다르게 수정했을 때 발생한다.

---

### [핵심]

- Conflict = Git 자동 병합 실패
- 같은 파일 같은 라인 수정 시 자주 발생
- 삭제한 파일을 다른 Branch에서 수정한 경우 발생 가능
- Conflict 파일을 직접 수정해야 한다.
- Conflict 해결 후 Staging과 Commit이 필요하다.

---

### [Flow]

```text
Merge 실행
→ Conflict 발생
→ Conflict 파일 확인
→ 코드 수정
→ git add
→ git commit
→ 테스트
```

---

### [예제]

Conflict 표시 예시:

```text
<<<<<<< HEAD
현재 Branch 코드
=======
병합하려는 Branch 코드
>>>>>>> feature/login-api
```

해결 후:

```java
return tokenService.validateToken(accessToken);
```

Conflict 해결 명령 흐름:

```bash
git status
# Conflict 파일 수정
git add src/main/java/AuthService.java
git commit
```

---

### [실무]

실무에서는 Conflict 발생 시 무조건 한쪽 코드를 삭제하지 않는다.

확인할 것:

- 현재 Branch 코드 의도
- 병합 대상 Branch 코드 의도
- 둘 다 필요한 로직인지
- 테스트 영향 범위
- API 응답 형식 변경 여부
- Entity / DTO / Service 변경 연계 여부

Conflict 해결 후 반드시 테스트한다.

```bash
./gradlew test
```

또는 최소 컴파일 확인:

```bash
./gradlew compileJava
```

---

### [주의]

Conflict Marker를 제거하지 않으면 빌드 오류가 발생한다.

남아 있으면 안 되는 Marker:

```text
<<<<<<<
=======
>>>>>>>
```

IDE 자동 Merge만 믿지 않는다.

중요 로직은 직접 확인한다.

---

### [FAQ]

Q. Merge Conflict는 무엇인가?
A. Git이 두 Branch의 변경 내용을 자동으로 합칠 수 없어 개발자가 직접 수정해야 하는 상태이다.

Q. Conflict는 왜 발생하는가?
A. 같은 파일의 같은 위치를 서로 다르게 수정했거나 삭제/수정이 충돌했을 때 발생한다.

Q. Conflict 해결 후 무엇을 해야 하는가?
A. 파일을 수정하고 `git add` 후 `git commit`을 실행해야 한다.

Q. Conflict Marker는 무엇인가?
A. `<<<<<<<`, `=======`, `>>>>>>>`로 표시되는 충돌 구간 표시이다.

---

# 9. Conflict Resolve

## 9.1 Conflict Resolve Strategy

### [개념]

Conflict Resolve는 충돌이 발생한 파일을 개발자가 직접 수정하여 최종 코드를 결정하는 과정이다.

---

### [핵심]

- 충돌 파일을 확인한다.
- 양쪽 변경 의도를 비교한다.
- 최종 코드를 직접 작성한다.
- Conflict Marker를 제거한다.
- `git add`로 해결 완료 표시한다.
- 테스트 후 Commit한다.

---

### [실무]

Conflict 해결 순서:

```text
1. git status로 충돌 파일 확인
2. 파일에서 Conflict Marker 확인
3. HEAD 코드와 incoming 코드 비교
4. 최종 코드 작성
5. Marker 제거
6. git add
7. git commit
8. 테스트 실행
```

명령 예시:

```bash
git status
git add src/main/java/FestivalService.java
git commit -m "fix: resolve festival service merge conflict"
```

Merge 중단:

```bash
git merge --abort
```

---

### [Comparison]

| 선택            | 의미                       | 주의                              |
| --------------- | -------------------------- | --------------------------------- |
| Current Change  | 현재 Branch 코드 선택      | 대상 Branch 변경이 사라질 수 있음 |
| Incoming Change | 병합 대상 Branch 코드 선택 | 현재 Branch 변경이 사라질 수 있음 |
| Both Changes    | 양쪽 코드 모두 반영        | 중복/순서 오류 가능               |
| Manual Edit     | 직접 최종 코드 작성        | 가장 안전하지만 검토 필요         |

---

### [주의]

`Accept Current Change`와 `Accept Incoming Change`를 무조건 누르면 필요한 코드가 사라질 수 있다.

Conflict 해결은 Git 명령 문제가 아니라 코드 의도 판단 문제이다.

Service, Controller, DTO, Entity 충돌은 연계 영향까지 확인한다.

---

### [FAQ]

Q. Conflict 해결은 어떻게 하는가?
A. 충돌 파일을 수정해 최종 코드를 만들고 Marker를 제거한 뒤 `git add`와 `git commit`을 수행한다.

Q. git merge --abort는 무엇인가?
A. 진행 중인 Merge를 취소하고 Merge 이전 상태로 되돌리는 명령이다.

Q. Accept Current Change는 안전한가?
A. 항상 안전하지 않다. 병합 대상 Branch의 필요한 변경이 사라질 수 있다.

Q. Conflict 해결 후 테스트가 필요한가?
A. 필요하다. 문법 오류뿐 아니라 로직 충돌이 남아 있을 수 있다.

---

# 10. Branch And Merge Best Practice

## 10.1 Team Workflow

### [개념]

Branch And Merge Best Practice는 팀 협업에서 코드 충돌을 줄이고 안정적으로 변경 사항을 통합하기 위한 규칙이다.

---

### [핵심]

- main 직접 작업 금지
- 기능별 Branch 생성
- 작업 전 기준 Branch 최신화
- 작은 단위 Commit
- Pull Request 기반 Merge
- Code Review 후 Merge
- Merge 후 Branch 삭제
- Conflict 해결 후 테스트

---

### [실무]

팀 프로젝트 권장 흐름:

```text
main 또는 develop 최신화
→ feature Branch 생성
→ 기능 개발
→ 작은 단위 Commit
→ Push
→ Pull Request 생성
→ Review
→ Merge
→ Branch 삭제
```

명령 흐름:

```bash
git switch develop
git pull origin develop
git switch -c feature/festival-search
# code 작업
git add .
git commit -m "feat: add festival search API"
git push origin feature/festival-search
```

---

### [Checklist]

Branch 생성 전:

- 기준 Branch가 최신인가?
- 작업 범위가 명확한가?
- Branch 이름이 규칙에 맞는가?

Commit 전:

- `git status` 확인했는가?
- `git diff` 확인했는가?
- 관련 파일만 Staging했는가?
- 민감 정보가 없는가?

Merge 전:

- Pull Request 설명이 충분한가?
- Review가 완료되었는가?
- 테스트가 통과했는가?
- Conflict가 해결되었는가?

Merge 후:

- Branch를 삭제했는가?
- Local main/develop을 최신화했는가?
- 관련 Issue를 닫았는가?

---

### [주의]

오래 살아 있는 Branch는 Conflict 위험이 크다.

큰 기능은 작은 Pull Request로 나누는 것이 좋다.

여러 사람이 같은 파일을 동시에 수정하면 Conflict 가능성이 높다.

Entity, DTO, API Spec, Security Config 변경은 팀 공유가 필요하다.

---

### [FAQ]

Q. Branch 작업 전 가장 먼저 할 일은?
A. 기준 Branch를 최신화한 뒤 새 feature Branch를 생성한다.

Q. 오래된 Branch는 왜 위험한가?
A. 기준 Branch와 차이가 커져 Merge Conflict 가능성이 높아진다.

Q. Merge 후 Branch는 삭제해야 하는가?
A. 일반적으로 삭제한다. 작업 완료된 Branch를 남기면 관리가 어려워진다.

Q. Pull Request 없이 Merge해도 되는가?
A. 개인 프로젝트는 가능하지만 팀 프로젝트에서는 Code Review를 위해 Pull Request 기반 Merge를 권장한다.

---

# 11. Troubleshooting

## 11.1 Branch Merge Troubleshooting

### [개념]

Branch Merge Troubleshooting은 Branch 생성, 이동, 삭제, Merge, Conflict 과정에서 발생하는 문제를 해결하는 절차이다.

---

### [Troubleshooting]

문제:

```text
Branch 이동이 안 됨
```

원인:

```text
현재 Working Directory에 Commit되지 않은 변경 사항이 있고, 이동할 Branch와 충돌 가능성이 있다.
```

해결:

```bash
git status
git add .
git commit -m "wip: save current work"
```

또는 임시 저장:

```bash
git stash
git switch target-branch
```

---

문제:

```text
Merge 중 Conflict 발생
```

원인:

```text
두 Branch가 같은 파일의 같은 위치를 다르게 수정했다.
```

해결:

```bash
git status
# conflict 파일 직접 수정
git add <file>
git commit
```

---

문제:

```text
Merge를 취소하고 싶음
```

원인:

```text
Conflict가 복잡하거나 잘못된 Branch에서 Merge를 실행했다.
```

해결:

```bash
git merge --abort
```

---

문제:

```text
Branch 삭제가 안 됨
```

원인:

```text
해당 Branch가 아직 Merge되지 않았다.
```

해결:

```bash
git branch -d feature/login-api
```

정말 삭제해야 하면:

```bash
git branch -D feature/login-api
```

---

문제:

```text
Remote Branch는 삭제했는데 Local 목록에 계속 보임
```

원인:

```text
Remote Tracking 정보가 갱신되지 않았다.
```

해결:

```bash
git fetch --prune
```

---

문제:

```text
잘못된 Branch에서 작업함
```

원인:

```text
Branch 확인 없이 작업을 시작했다.
```

해결:

```bash
git switch -c feature/correct-branch
git add .
git commit -m "feat: move work to correct branch"
```

이미 Commit한 경우:

```bash
git switch correct-branch
git cherry-pick <commit-hash>
```

---

### [FAQ]

Q. Branch 이동이 안 되는 이유는?
A. Commit되지 않은 변경 사항이 이동 대상 Branch와 충돌할 수 있기 때문이다.

Q. Merge를 취소하려면?
A. `git merge --abort` 명령을 사용한다.

Q. Remote Branch 삭제 후 목록 갱신은?
A. `git fetch --prune` 명령으로 Remote Tracking 정보를 정리한다.

Q. 잘못된 Branch에서 작업했을 때는?
A. 새 Branch를 만들거나 Commit 후 `cherry-pick`으로 올바른 Branch에 적용한다.

---

# Retrieval Queries

### [FAQ]

Q. Git Branch란?
A. Branch는 특정 Commit을 기준으로 독립적인 작업 흐름을 만드는 Git 포인터이다.

Q. Branch를 사용하는 이유는?
A. 기능 개발, 버그 수정, 실험 작업을 main 코드와 분리하기 위해 사용한다.

Q. main Branch에서 직접 작업하면 안 되는 이유는?
A. 안정 코드가 깨질 수 있고 Review 없이 변경이 반영될 위험이 있기 때문이다.

Q. feature Branch란?
A. 새 기능 개발을 위해 main 또는 develop에서 분기한 작업 Branch이다.

Q. Branch 생성 명령은?
A. `git switch -c feature/name` 또는 `git branch feature/name`을 사용한다.

Q. Branch 이동 명령은?
A. `git switch branch-name`을 사용한다.

Q. Branch 목록 확인 명령은?
A. `git branch`는 Local Branch, `git branch -r`은 Remote Branch를 보여준다.

Q. Branch 삭제 명령은?
A. Local Branch는 `git branch -d branch-name`, Remote Branch는 `git push origin --delete branch-name`으로 삭제한다.

Q. git branch -d와 -D 차이는?
A. `-d`는 Merge된 Branch만 삭제하고 `-D`는 강제로 삭제한다.

Q. Branch Naming Convention이란?
A. Branch 목적을 이름으로 구분하기 위한 규칙이다.

Q. 좋은 Branch 이름 예시는?
A. `feature/login-api`, `fix/token-error`, `refactor/user-service`이다.

Q. Merge란?
A. Merge는 두 Branch의 변경 이력을 하나의 Branch로 통합하는 Git 작업이다.

Q. Merge는 어느 Branch에서 실행하는가?
A. 변경 내용을 받을 대상 Branch로 이동한 뒤 실행한다.

Q. feature Branch를 main에 Merge하려면?
A. `main`으로 이동한 뒤 `git merge feature-branch`를 실행하거나 GitHub Pull Request로 Merge한다.

Q. Fast Forward Merge란?
A. Merge Commit 없이 Branch 포인터만 대상 Branch 최신 Commit으로 이동하는 Merge 방식이다.

Q. Merge Commit이란?
A. 두 Branch의 이력을 통합할 때 생성되는 Commit이며 부모 Commit을 두 개 이상 가진다.

Q. Squash Merge란?
A. feature Branch의 여러 Commit을 하나의 Commit으로 압축해 대상 Branch에 반영하는 방식이다.

Q. Squash Merge는 언제 사용하는가?
A. main History를 깔끔하게 유지하고 Pull Request 단위로 변경을 관리할 때 사용한다.

Q. Merge Conflict란?
A. Git이 두 Branch의 변경 내용을 자동으로 합칠 수 없어 개발자가 직접 수정해야 하는 상태이다.

Q. Conflict는 왜 발생하는가?
A. 같은 파일의 같은 위치를 서로 다르게 수정했거나 삭제/수정 변경이 충돌했기 때문이다.

Q. Conflict Marker란?
A. `<<<<<<<`, `=======`, `>>>>>>>`로 표시되는 충돌 구간 표시이다.

Q. Conflict 해결 순서는?
A. 충돌 파일 수정 → Marker 제거 → `git add` → `git commit` → 테스트 순서이다.

Q. git merge --abort란?
A. 진행 중인 Merge를 취소하고 Merge 이전 상태로 되돌리는 명령이다.

Q. Accept Current Change는 무엇인가?
A. 현재 Branch의 변경 내용을 선택하는 Conflict 해결 옵션이다.

Q. Accept Incoming Change는 무엇인가?
A. 병합 대상 Branch의 변경 내용을 선택하는 Conflict 해결 옵션이다.

Q. Branch 작업 전 해야 할 일은?
A. 기준 Branch를 최신화한 뒤 새 Branch를 생성해야 한다.

Q. 오래된 Branch가 위험한 이유는?
A. 기준 Branch와 차이가 커져 Merge Conflict 가능성이 높아지기 때문이다.

Q. Merge 후 Branch를 삭제해야 하는가?
A. 일반적으로 작업 완료 Branch는 삭제하여 Branch 목록을 정리한다.

Q. Remote Branch 목록이 갱신되지 않을 때는?
A. `git fetch --prune` 명령으로 Remote Tracking 정보를 정리한다.

Q. 잘못된 Branch에서 작업했을 때 해결 방법은?
A. 새 Branch를 만들거나 Commit을 올바른 Branch에 `cherry-pick`한다.
