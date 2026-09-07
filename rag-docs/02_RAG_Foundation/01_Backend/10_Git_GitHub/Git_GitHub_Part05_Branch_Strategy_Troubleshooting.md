# Git / GitHub Part05 Branch Strategy Troubleshooting

---

# 1. Branch Strategy

## 1.1 Branch Strategy Core

### [개념]

Branch Strategy는 팀이 Git Branch를 어떤 기준으로 만들고, 병합하고, 배포할지 정하는 협업 규칙이다.

Branch Strategy는 코드 안정성, 협업 효율, Release 관리, Hotfix 대응에 직접 영향을 준다.

---

### [핵심]

- Branch Strategy = Branch 운영 규칙
- main = 배포 가능 안정 Branch
- develop = 통합 개발 Branch
- feature = 기능 개발 Branch
- release = 배포 준비 Branch
- hotfix = 운영 긴급 수정 Branch
- 팀 규모와 배포 방식에 맞게 선택한다.

---

### [실무]

2026 실무 기준 Branch Strategy는 프로젝트 규모와 배포 주기에 따라 선택한다.

대표 전략:

| Strategy                | 특징                             | 사용 상황                 |
| ----------------------- | -------------------------------- | ------------------------- |
| GitHub Flow             | 단순, main 중심                  | 소규모 팀, 빠른 배포      |
| Git Flow                | main/develop/release/hotfix 분리 | 배포 주기 명확한 프로젝트 |
| Trunk Based Development | main에 자주 통합                 | CI/CD 성숙한 팀           |
| Feature Branch Workflow | 기능 Branch 중심                 | 일반 팀 프로젝트          |

학원 팀 프로젝트나 소규모 웹 프로젝트에서는 다음 구조가 현실적이다.

```text
main
develop
feature/*
fix/*
docs/*
```

---

### [Flow]

```text
main
→ develop
→ feature/*
→ Pull Request
→ develop
→ main
```

---

### [Best Practice]

권장 기준:

- `main`은 항상 배포 가능한 상태 유지
- 기능 개발은 `feature/*`에서 진행
- 버그 수정은 `fix/*`에서 진행
- 작업 전 기준 Branch 최신화
- Pull Request 기반 Merge
- Merge 후 Branch 삭제
- Branch Naming Convention 통일
- main 직접 Push 금지

---

### [주의]

Branch Strategy가 없으면 협업 품질이 떨어진다.

자주 발생하는 문제:

- main 직접 Push
- Branch 이름 혼란
- 오래된 Branch 증가
- Conflict 증가
- Release 기준 불명확
- Hotfix 반영 누락
- PR 없이 Merge
- 배포 코드와 개발 코드 혼합

---

### [FAQ]

Q. Branch Strategy는 무엇인가?
A. Branch Strategy는 팀이 Branch를 생성, 병합, 배포하는 기준을 정한 협업 규칙이다.

Q. Branch Strategy가 필요한 이유는?
A. 협업 충돌을 줄이고, 배포 가능한 코드와 개발 중인 코드를 안전하게 분리하기 위해 필요하다.

Q. 소규모 팀 프로젝트에 적합한 Branch 구조는?
A. `main`, `develop`, `feature/*`, `fix/*`, `docs/*` 정도의 단순 구조가 적합하다.

Q. main Branch의 역할은?
A. 항상 배포 가능한 안정 코드를 유지하는 Branch이다.

---

# 2. GitHub Flow

## 2.1 GitHub Flow Core

### [개념]

GitHub Flow는 `main` Branch를 중심으로 feature Branch와 Pull Request만 사용하는 단순한 Branch Strategy이다.

GitHub Flow는 빠른 개발, 빠른 Review, 빠른 배포에 적합하다.

---

### [핵심]

- GitHub Flow = main 중심 단순 Workflow
- main은 항상 배포 가능 상태
- 모든 작업은 Branch에서 진행
- Pull Request로 Review
- Merge 후 즉시 배포 가능
- release Branch, develop Branch를 사용하지 않는 경우가 많다.

---

### [Flow]

```text
main 최신화
→ feature Branch 생성
→ Commit
→ Push
→ Pull Request
→ Review
→ Merge to main
→ Deploy
```

---

### [실무]

GitHub Flow는 다음 프로젝트에 적합하다.

- 소규모 웹 서비스
- 빠른 배포 프로젝트
- CI/CD 자동화가 있는 프로젝트
- 배포 주기가 짧은 프로젝트
- Release Branch가 필요 없는 프로젝트

명령 흐름:

```bash
git switch main
git pull origin main
git switch -c feature/login-api
git add .
git commit -m "feat: add login API"
git push -u origin feature/login-api
```

GitHub에서 Pull Request 생성 후 `main`에 Merge한다.

---

### [주의]

GitHub Flow에서는 `main` 안정성이 매우 중요하다.

Branch Protection과 CI Check가 없으면 깨진 코드가 main에 Merge될 수 있다.

권장 보호 규칙:

```text
main:
- Direct Push 금지
- Pull Request Required
- Review Required
- Status Check Required
```

---

### [FAQ]

Q. GitHub Flow는 무엇인가?
A. GitHub Flow는 main Branch와 feature Branch, Pull Request를 중심으로 운영하는 단순한 Branch Strategy이다.

Q. GitHub Flow는 언제 적합한가?
A. 소규모 팀, 빠른 배포, CI/CD가 있는 웹 서비스에 적합하다.

Q. GitHub Flow에서 main은 어떤 상태여야 하는가?
A. 항상 배포 가능한 안정 상태여야 한다.

Q. GitHub Flow의 핵심 절차는?
A. Branch 생성 → Commit → Push → Pull Request → Review → main Merge이다.

---

# 3. Git Flow

## 3.1 Git Flow Core

### [개념]

Git Flow는 `main`, `develop`, `feature`, `release`, `hotfix` Branch를 구분하여 개발과 배포를 관리하는 Branch Strategy이다.

Git Flow는 배포 주기가 명확하고 Release 관리가 필요한 프로젝트에 적합하다.

---

### [핵심]

- Git Flow = Branch 역할을 세분화한 전략
- main = 운영 배포 코드
- develop = 다음 배포를 위한 통합 개발 코드
- feature = 기능 개발
- release = 배포 준비
- hotfix = 운영 긴급 수정
- 배포 안정성과 버전 관리에 유리하다.

---

### [Flow]

```text
main
└─ develop
   └─ feature/*
      → develop Merge
   └─ release/*
      → main Merge
      → develop Merge
└─ hotfix/*
   → main Merge
   → develop Merge
```

---

### [실무]

Git Flow Branch 역할:

| Branch     | 역할                |
| ---------- | ------------------- |
| main       | 운영 배포 코드      |
| develop    | 기능 통합 개발 코드 |
| feature/\* | 개별 기능 개발      |
| release/\* | 배포 전 안정화      |
| hotfix/\*  | 운영 긴급 수정      |

기능 개발 흐름:

```text
develop
→ feature/festival-search
→ Pull Request
→ develop
```

배포 흐름:

```text
develop
→ release/v1.0.0
→ 테스트 / 버그 수정
→ main
→ tag v1.0.0
→ develop 반영
```

Hotfix 흐름:

```text
main
→ hotfix/payment-error
→ main Merge
→ tag v1.0.1
→ develop Merge
```

---

### [예제]

feature Branch 생성:

```bash
git switch develop
git pull origin develop
git switch -c feature/festival-search
```

release Branch 생성:

```bash
git switch develop
git pull origin develop
git switch -c release/v1.0.0
```

hotfix Branch 생성:

```bash
git switch main
git pull origin main
git switch -c hotfix/payment-error
```

---

### [주의]

Git Flow는 Branch가 많아져 운영 복잡도가 증가할 수 있다.

소규모 프로젝트에서 release, hotfix가 필요 없으면 과한 전략이 될 수 있다.

release Branch 수정 사항은 main과 develop 양쪽에 반영해야 한다.

hotfix 수정 사항도 main과 develop 양쪽에 반영해야 한다.

---

### [FAQ]

Q. Git Flow는 무엇인가?
A. Git Flow는 main, develop, feature, release, hotfix Branch를 구분하여 개발과 배포를 관리하는 Branch Strategy이다.

Q. develop Branch는 무엇인가?
A. 다음 배포를 위해 기능들이 통합되는 개발 Branch이다.

Q. release Branch는 언제 만드는가?
A. 배포 전 테스트, 버그 수정, 버전 준비를 위해 만든다.

Q. hotfix Branch는 언제 만드는가?
A. 운영 배포 코드에서 긴급 버그를 수정해야 할 때 main에서 분기한다.

---

# 4. Trunk Based Development

## 4.1 Trunk Based Development Core

### [개념]

Trunk Based Development는 모든 개발자가 짧은 주기로 main 또는 trunk Branch에 변경 사항을 자주 통합하는 Branch Strategy이다.

긴 feature Branch를 피하고 작은 변경을 빠르게 통합하는 것이 핵심이다.

---

### [핵심]

- Trunk = main Branch
- 짧은 수명의 Branch 사용
- 작은 단위 Commit
- 자주 통합
- 강한 CI/CD 필요
- Feature Flag와 함께 사용 가능
- 대기 시간이 긴 Pull Request를 피한다.

---

### [Flow]

```text
main 최신화
→ 짧은 feature Branch
→ 작은 변경
→ Pull Request
→ CI 통과
→ main Merge
→ Deploy Ready
```

---

### [실무]

Trunk Based Development는 다음 환경에 적합하다.

- CI/CD가 안정적인 팀
- 자동 테스트가 충분한 프로젝트
- 작은 단위 배포를 자주 하는 서비스
- Feature Flag를 활용하는 서비스
- 장기 Branch를 줄이고 싶은 팀

Feature Flag 예시:

```text
코드는 main에 Merge
→ 기능은 flag로 비활성화
→ 검증 후 flag 활성화
```

---

### [주의]

자동 테스트가 약한 팀에서 Trunk Based Development를 적용하면 main 안정성이 깨질 수 있다.

큰 기능을 잘게 나누지 못하면 main에 미완성 코드가 들어갈 수 있다.

Feature Flag 관리가 부실하면 사용하지 않는 분기 코드가 쌓인다.

---

### [FAQ]

Q. Trunk Based Development는 무엇인가?
A. 짧은 주기로 main 또는 trunk Branch에 작은 변경을 자주 통합하는 Branch Strategy이다.

Q. Trunk Based Development의 장점은?
A. 장기 Branch를 줄이고 Conflict를 줄이며 빠른 배포를 가능하게 한다.

Q. Trunk Based Development에 필요한 조건은?
A. 강한 CI/CD, 충분한 자동 테스트, 작은 변경 단위가 필요하다.

Q. Feature Flag는 왜 사용하는가?
A. 미완성 기능 코드를 main에 넣더라도 사용자에게 노출하지 않기 위해 사용한다.

---

# 5. Team Project Recommended Workflow

## 5.1 Small Team Web Project Workflow

### [개념]

Small Team Web Project Workflow는 학원 팀 프로젝트, 포트폴리오 프로젝트, 초기 서비스 개발에 적합한 단순 Branch Strategy이다.

복잡한 Git Flow보다 `main`, `develop`, `feature/*` 중심 구조를 권장한다.

---

### [핵심]

- main = 발표 / 배포용 안정 코드
- develop = 팀 개발 통합 Branch
- feature/\* = 개인 기능 개발 Branch
- fix/\* = 버그 수정 Branch
- Pull Request 기반 Merge
- Merge 전 최소 빌드 확인
- Merge 후 Branch 삭제

---

### [실무]

권장 Branch 구조:

```text
main
develop
feature/chat
feature/review
feature/festival-search
feature/kakao-map
fix/login-error
docs/readme
```

권장 작업 흐름:

```text
develop 최신화
→ feature Branch 생성
→ 기능 개발
→ Commit
→ Push
→ Pull Request to develop
→ Review
→ Merge
→ develop 안정화
→ main Merge
```

명령 흐름:

```bash
git switch develop
git pull origin develop
git switch -c feature/chat-notification
git add .
git commit -m "feat: add chat notification API"
git push -u origin feature/chat-notification
```

---

### [Checklist]

작업 시작 전:

- develop이 최신인가?
- 내 작업 Branch가 맞는가?
- Branch 이름이 명확한가?

작업 중:

- Commit 단위가 너무 크지 않은가?
- 다른 팀원 파일을 불필요하게 수정하지 않았는가?
- API Spec 변경을 공유했는가?

PR 생성 전:

- 빌드 또는 컴파일 확인했는가?
- Swagger / Postman 확인했는가?
- 프론트 영향 범위를 적었는가?
- DB / Entity 변경 사항을 공유했는가?

Merge 전:

- Conflict가 없는가?
- Review가 끝났는가?
- 실행 가능한 상태인가?

---

### [주의]

팀 프로젝트에서 가장 위험한 행동:

```text
main 직접 Push
develop에서 직접 기능 개발
Pull 없이 오래 작업
git add . 후 확인 없이 Commit
Conflict Marker 남긴 상태로 Commit
.env Commit
빌드 실패 상태 Merge
```

---

### [FAQ]

Q. 학원 팀 프로젝트에 추천하는 Branch 구조는?
A. `main`, `develop`, `feature/*`, `fix/*`, `docs/*` 중심의 단순 구조를 권장한다.

Q. develop Branch 역할은?
A. 팀원 기능을 통합하고 테스트하는 개발 통합 Branch이다.

Q. main Branch는 언제 업데이트하는가?
A. develop이 안정화되고 발표 또는 배포 가능한 상태일 때 main에 반영한다.

Q. feature Branch는 어디서 분기하는가?
A. 보통 최신 develop Branch에서 분기한다.

---

# 6. Release Workflow

## 6.1 Release Workflow Core

### [개념]

Release Workflow는 개발 완료된 코드를 배포 가능한 버전으로 안정화하고 main Branch에 반영하는 절차이다.

Release Workflow는 배포 기준 Commit, Tag, 변경 내역, Hotfix 기준을 명확하게 만든다.

---

### [핵심]

- Release = 배포 버전 확정
- main은 배포 기준 Branch
- release Branch에서 최종 테스트 가능
- Tag로 배포 Commit 표시
- Release Note 작성
- 배포 후 Hotfix 기준점이 된다.

---

### [실무]

단순 Release 흐름:

```text
develop 안정화
→ Pull Request to main
→ Review
→ Merge
→ Tag 생성
→ GitHub Release 작성
```

Git Flow Release 흐름:

```text
develop
→ release/v1.0.0
→ 테스트 / 버그 수정
→ main Merge
→ tag v1.0.0
→ develop Merge
```

명령 예시:

```bash
git switch main
git pull origin main
git tag -a v1.0.0 -m "release v1.0.0"
git push origin v1.0.0
```

Release Note 예시:

```md
## v1.0.0

### Features

- 축제 검색 API
- 실시간 채팅
- 리뷰 기능
- 알림 기능

### Fixes

- JWT 만료 응답 수정
- 캘린더 월별 조회 오류 수정
```

---

### [주의]

Release 직전에는 기능 추가보다 안정화가 우선이다.

release Branch에서는 큰 구조 변경을 피한다.

Release 후 발견된 운영 버그는 hotfix Branch로 처리한다.

Tag는 배포 기준점이므로 신중하게 생성한다.

---

### [FAQ]

Q. Release Workflow는 무엇인가?
A. 개발 완료 코드를 배포 가능한 버전으로 안정화하고 main에 반영하는 절차이다.

Q. Release Tag는 왜 필요한가?
A. 어떤 Commit이 배포 버전인지 명확히 표시하기 위해 필요하다.

Q. Release Branch에서는 무엇을 하는가?
A. 배포 전 테스트, 버그 수정, 버전 정보 정리, 문서 정리를 수행한다.

Q. Release 직전 큰 기능 추가가 위험한 이유는?
A. 새 버그가 들어가 안정화와 배포 일정에 영향을 줄 수 있기 때문이다.

---

# 7. Hotfix Workflow

## 7.1 Hotfix Workflow Core

### [개념]

Hotfix Workflow는 main에 배포된 운영 코드에서 긴급 버그가 발생했을 때 빠르게 수정하고 배포하는 절차이다.

Hotfix는 일반 feature 개발 흐름보다 우선순위가 높다.

---

### [핵심]

- Hotfix = 운영 긴급 수정
- main에서 분기
- 최소 변경 원칙
- 빠른 테스트
- main에 Merge
- develop에도 반영
- Patch Version Tag 생성

---

### [Flow]

```text
main
→ hotfix/*
→ bug fix
→ Pull Request to main
→ Merge
→ tag patch version
→ Pull Request to develop
→ Merge
```

---

### [예제]

Hotfix Branch 생성:

```bash
git switch main
git pull origin main
git switch -c hotfix/jwt-expired-response
```

수정 후 Commit:

```bash
git add .
git commit -m "fix: correct expired JWT response status"
git push -u origin hotfix/jwt-expired-response
```

Tag 생성:

```bash
git switch main
git pull origin main
git tag -a v1.0.1 -m "hotfix v1.0.1"
git push origin v1.0.1
```

---

### [실무]

Hotfix는 다음 상황에서 사용한다.

- 운영 로그인 장애
- 결제 실패
- 인증/인가 오류
- 배포 후 API 500 오류
- 데이터 손상 가능성
- 보안 취약점 긴급 수정

Hotfix 원칙:

```text
원인 범위 최소화
→ 수정 범위 최소화
→ 테스트
→ main 반영
→ develop 반영
→ Release Note 기록
```

---

### [주의]

Hotfix를 main에만 반영하고 develop에 반영하지 않으면 다음 배포 때 버그가 다시 살아날 수 있다.

Hotfix Branch에서는 관련 없는 리팩토링을 하지 않는다.

긴급 수정이라도 테스트 없이 Merge하지 않는다.

---

### [FAQ]

Q. Hotfix는 무엇인가?
A. main에 배포된 운영 코드에서 긴급 버그를 빠르게 수정하는 작업 흐름이다.

Q. Hotfix Branch는 어디서 분기하는가?
A. 운영 코드 기준인 main Branch에서 분기한다.

Q. Hotfix 후 develop에도 Merge해야 하는가?
A. 해야 한다. develop에 반영하지 않으면 다음 배포에서 같은 버그가 다시 발생할 수 있다.

Q. Hotfix에서 리팩토링을 해도 되는가?
A. 권장하지 않는다. Hotfix는 최소 변경으로 긴급 문제만 해결해야 한다.

---

# 8. Detached HEAD

## 8.1 Detached HEAD Core

### [개념]

Detached HEAD는 HEAD가 Branch가 아니라 특정 Commit을 직접 가리키는 Git 상태이다.

이 상태에서 Commit하면 Branch에 연결되지 않은 Commit이 생성될 수 있다.

---

### [핵심]

- Detached HEAD = HEAD가 Branch가 아닌 Commit을 직접 가리킴
- 과거 Commit 확인 시 발생
- Tag Checkout 시 발생 가능
- 실험 작업은 가능하지만 Branch 생성 필요
- Branch 없이 만든 Commit은 잃어버리기 쉽다.

---

### [예제]

특정 Commit으로 이동:

```bash
git switch --detach a1b2c3d
```

또는 예전 방식:

```bash
git checkout a1b2c3d
```

현재 상태 확인:

```bash
git status
```

Detached HEAD에서 Branch 생성:

```bash
git switch -c experiment/from-old-commit
```

---

### [실무]

Detached HEAD는 다음 상황에서 발생한다.

- 과거 Commit 코드 확인
- 특정 Tag 확인
- CI 환경에서 특정 Commit Checkout
- 실험을 위해 특정 Commit 이동

과거 Commit에서 실험을 이어가려면 즉시 Branch를 만든다.

```bash
git switch -c fix/from-old-version
```

---

### [주의]

Detached HEAD 상태에서 만든 Commit은 Branch가 없으면 추적하기 어렵다.

다른 Branch로 이동하기 전 필요한 Commit을 Branch로 연결한다.

Commit을 잃어버린 경우 `git reflog`로 찾을 수 있다.

```bash
git reflog
```

---

### [FAQ]

Q. Detached HEAD는 무엇인가?
A. HEAD가 Branch가 아니라 특정 Commit을 직접 가리키는 상태이다.

Q. Detached HEAD는 위험한가?
A. Branch 없이 Commit하면 작업을 잃어버리기 쉬워 주의가 필요하다.

Q. Detached HEAD에서 작업을 보존하려면?
A. `git switch -c new-branch`로 Branch를 생성해야 한다.

Q. Detached HEAD에서 잃어버린 Commit은 찾을 수 있는가?
A. `git reflog`로 이전 HEAD 기록을 확인해 찾을 수 있다.

---

# 9. Reflog

## 9.1 Reflog Core

### [개념]

Reflog는 Local Repository에서 HEAD와 Branch Reference가 이동한 기록을 저장하는 Git 기능이다.

Reset, Rebase, Checkout, Commit 이동 기록을 추적하여 실수 복구에 사용할 수 있다.

---

### [핵심]

- Reflog = Local Reference 이동 기록
- HEAD 이동 기록 확인
- Reset 실수 복구 가능
- Rebase 전 Commit 추적 가능
- Detached HEAD Commit 추적 가능
- Remote 기록이 아니라 Local 기록이다.

---

### [예제]

Reflog 확인:

```bash
git reflog
```

이전 HEAD로 복구:

```bash
git reset --hard HEAD@{1}
```

특정 Reflog Commit으로 Branch 생성:

```bash
git switch -c recovery/a1b2c3d a1b2c3d
```

---

### [실무]

Reflog는 다음 상황에서 사용한다.

- `git reset --hard` 실수 복구
- Rebase 전 Commit 위치 찾기
- Detached HEAD에서 만든 Commit 찾기
- 잘못 이동한 Branch 복구
- 삭제한 Branch의 마지막 Commit 찾기

복구 흐름:

```text
문제 발생
→ git reflog
→ 복구할 Commit 확인
→ Branch 생성 또는 reset
→ 상태 확인
```

---

### [주의]

Reflog는 영구 저장소가 아니다.

Local Repository 내부 기록이며 일정 기간 후 정리될 수 있다.

Remote Repository에서 다른 팀원의 Reflog를 확인할 수 없다.

Untracked 파일 삭제는 Reflog로 복구하기 어렵다.

---

### [FAQ]

Q. Reflog는 무엇인가?
A. Local Repository에서 HEAD와 Branch Reference가 이동한 기록을 저장하는 Git 기능이다.

Q. Reflog는 언제 쓰는가?
A. Reset, Rebase, Detached HEAD, Branch 삭제 같은 실수를 복구할 때 사용한다.

Q. Reflog는 Remote에도 있는가?
A. 아니다. Reflog는 Local Repository 기준 기록이다.

Q. reset --hard 실수는 어떻게 복구하는가?
A. `git reflog`로 이전 HEAD를 찾고 `git reset --hard HEAD@{n}`으로 복구한다.

---

# 10. Force Push Accident

## 10.1 Force Push Accident Core

### [개념]

Force Push Accident는 `git push --force`로 Remote Branch History를 덮어써서 팀원의 Commit이 사라지거나 Pull Request 이력이 꼬이는 사고이다.

Force Push는 History Rewrite가 Remote에 반영되는 위험한 작업이다.

---

### [핵심]

- Force Push = Remote History 강제 덮어쓰기
- 공유 Branch에서 매우 위험
- 팀원 Commit 손실 가능
- Pull Request History 꼬임 가능
- `--force-with-lease`가 더 안전
- 사고 발생 시 즉시 Push 중단 후 복구 Commit 확인

---

### [실무]

Force Push가 필요한 경우:

- 본인 feature Branch를 Rebase 후 갱신
- 본인 Branch Commit Message 정리 후 갱신
- Pull Request 전 History 정리

Force Push 금지 대상:

```text
main
develop
release/*
hotfix/*
팀원이 함께 작업 중인 Branch
```

상대적으로 안전한 명령:

```bash
git push --force-with-lease origin feature/login-api
```

`--force-with-lease`는 Remote Branch가 내가 마지막으로 본 상태와 다르면 Push를 거부한다.

---

### [Troubleshooting]

문제:

```text
Force Push로 팀원 Commit이 사라짐
```

원인:

```text
Remote Branch History를 Local History로 강제로 덮어썼다.
```

해결:

```text
1. 즉시 추가 Push 중단
2. 팀원 Local Repository에서 사라진 Commit Hash 확인
3. 복구 Branch 생성
4. 누락 Commit cherry-pick 또는 merge
5. Remote Branch 복구
```

팀원이 Commit을 가지고 있는 경우:

```bash
git log --oneline
git switch -c recovery/missing-commits
git push -u origin recovery/missing-commits
```

복구 Branch에서 대상 Branch로 PR 생성한다.

---

### [주의]

Force Push 사고는 기술 문제보다 협업 사고에 가깝다.

공유 Branch에서 Force Push를 허용하지 않도록 Branch Protection을 설정한다.

Force Push 전 확인:

```bash
git branch
git status
git log --oneline --graph --decorate --all
```

---

### [FAQ]

Q. Force Push는 무엇인가?
A. Local History로 Remote Branch History를 강제로 덮어쓰는 Push 방식이다.

Q. Force Push가 위험한 이유는?
A. 팀원의 Commit을 Remote에서 사라지게 만들 수 있기 때문이다.

Q. --force와 --force-with-lease 차이는?
A. `--force-with-lease`는 Remote가 예상과 다르면 Push를 거부하여 덮어쓰기 위험을 줄인다.

Q. main에 Force Push를 막으려면?
A. GitHub Branch Protection에서 Force Push를 금지한다.

---

# 11. Wrong Commit And Wrong Branch

## 11.1 Wrong Commit

### [개념]

Wrong Commit은 잘못된 Branch에 Commit하거나, Commit에 잘못된 파일을 포함하거나, Commit Message를 잘못 작성한 상태이다.

문제 상황에 따라 Amend, Reset, Restore, Cherry Pick, Revert를 선택한다.

---

### [핵심]

- Push 전 실수 = Amend / Reset / Restore로 정리 가능
- Push 후 실수 = Revert 우선
- 잘못된 Branch Commit = Cherry Pick으로 이동 가능
- 잘못 Staging = Restore Staged
- 잘못된 파일 포함 = Reset 후 다시 Commit
- 민감 정보 포함 = 즉시 폐기와 History 처리 필요

---

### [Troubleshooting]

문제:

```text
Commit Message 오타
```

Push 전 해결:

```bash
git commit --amend -m "feat: add festival search API"
```

Push 후 공유 Branch라면 새 수정 Commit 또는 팀 규칙에 따른 처리 권장.

---

문제:

```text
Commit에 잘못된 파일 포함
```

Push 전 해결:

```bash
git reset --mixed HEAD~1
git restore --staged <file>
git add <correct-files>
git commit -m "feat: correct commit"
```

---

문제:

```text
잘못된 Branch에 Commit
```

해결:

```bash
git log --oneline
git switch correct-branch
git cherry-pick <commit-hash>
```

기존 Branch에서 제거:

```bash
git switch wrong-branch
git reset --soft HEAD~1
```

---

문제:

```text
이미 Push한 Commit을 취소해야 함
```

공유 Branch 해결:

```bash
git revert <commit-hash>
git push origin <branch>
```

---

### [주의]

민감 정보가 Commit되면 단순 삭제로 끝나지 않는다.

필수 조치:

```text
1. 노출된 Key / Password 폐기
2. 새 Secret 발급
3. Git 추적 제거
4. 필요 시 History Rewrite
5. 팀원에게 공유
```

---

### [FAQ]

Q. 잘못된 Branch에 Commit했을 때는?
A. 올바른 Branch로 이동해 `git cherry-pick <commit-hash>`를 사용한다.

Q. Commit Message 오타는 어떻게 고치는가?
A. Push 전이면 `git commit --amend -m "new message"`를 사용한다.

Q. Commit에 잘못된 파일이 들어갔을 때는?
A. Push 전이면 Reset 후 올바른 파일만 다시 Staging하여 Commit한다.

Q. Push한 Commit을 취소하려면?
A. 공유 Branch에서는 `git revert <commit-hash>`를 사용하는 것이 안전하다.

---

# 12. Git Troubleshooting Index

## 12.1 Troubleshooting Index

### [개념]

Git Troubleshooting Index는 Git 사용 중 자주 발생하는 문제를 빠르게 검색하고 해결하기 위한 문제 중심 색인이다.

---

### [Troubleshooting]

문제:

```text
파일을 수정했는데 Commit에 포함되지 않음
```

원인:

```text
git add를 하지 않아 Staging Area에 올라가지 않았다.
```

해결:

```bash
git status
git add <file>
git commit -m "message"
```

---

문제:

```text
새 파일이 git commit -am에 포함되지 않음
```

원인:

```text
git commit -am은 이미 추적 중인 Modified 파일만 포함한다.
```

해결:

```bash
git add <new-file>
git commit -m "message"
```

---

문제:

```text
.gitignore에 추가했는데 계속 추적됨
```

원인:

```text
이미 Git이 추적 중인 파일이다.
```

해결:

```bash
git rm --cached <file>
git commit -m "chore: remove tracked ignored file"
```

---

문제:

```text
Branch 이동이 안 됨
```

원인:

```text
Commit되지 않은 변경 사항이 대상 Branch와 충돌할 수 있다.
```

해결:

```bash
git status
git stash push -m "wip before switch"
git switch target-branch
```

---

문제:

```text
Merge Conflict 발생
```

원인:

```text
두 Branch가 같은 파일의 같은 위치를 다르게 수정했다.
```

해결:

```bash
git status
# conflict 파일 수정
git add <file>
git commit
```

---

문제:

```text
Rebase Conflict 발생
```

원인:

```text
Commit을 새 기준 Branch 위로 다시 적용하는 과정에서 충돌했다.
```

해결:

```bash
git status
# conflict 파일 수정
git add <file>
git rebase --continue
```

---

문제:

```text
Push Rejected 발생
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
Pull Request Branch가 GitHub에 안 보임
```

원인:

```text
Local Branch를 Remote에 Push하지 않았다.
```

해결:

```bash
git push -u origin feature/name
```

---

문제:

```text
Detached HEAD 상태가 됨
```

원인:

```text
Branch가 아니라 특정 Commit 또는 Tag로 이동했다.
```

해결:

```bash
git switch -c recovery/branch-name
```

---

문제:

```text
reset --hard로 작업이 사라짐
```

원인:

```text
Working Directory 변경 사항까지 삭제했다.
```

해결:

```bash
git reflog
git reset --hard HEAD@{1}
```

---

문제:

```text
Stash 적용 중 Conflict 발생
```

원인:

```text
Stash 변경과 현재 Branch 코드가 같은 영역을 수정했다.
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
Repository not found
```

원인:

```text
Repository URL이 틀렸거나 접근 권한이 없다.
```

해결:

```bash
git remote -v
git remote set-url origin <correct-url>
```

---

문제:

```text
Authentication failed
```

원인:

```text
GitHub Token 또는 SSH Key 인증이 올바르지 않다.
```

해결:

```text
HTTPS: Personal Access Token 확인
SSH: SSH Key 등록 확인
Credential Manager 캐시 확인
```

---

### [FAQ]

Q. Git 문제가 발생하면 가장 먼저 확인할 것은?
A. `git status`, `git branch`, `git log --oneline`을 먼저 확인한다.

Q. History 관련 실수 복구는 무엇으로 확인하는가?
A. `git reflog`로 HEAD 이동 기록을 확인한다.

Q. Remote 관련 문제는 무엇을 확인하는가?
A. `git remote -v`, `git branch -vv`, `git fetch origin`으로 Remote와 Upstream 상태를 확인한다.

Q. Conflict 해결 후 공통으로 해야 할 일은?
A. 파일 수정, Marker 제거, `git add`, Commit 또는 Rebase Continue, 테스트를 수행한다.

---

# 13. Final Review Checklist

## 13.1 Git GitHub Document Checklist

### [개념]

Final Review Checklist는 Git / GitHub RAG 문서가 Agent Retrieval, Code Generation Support, Review Support, Troubleshooting Support에 적합한지 검수하는 기준이다.

---

### [핵심]

검수 대상:

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
- Remote
- GitHub
- Pull Request
- Code Review
- Branch Strategy
- Git Flow
- Troubleshooting

---

### [Checklist]

문서 구조:

- [개념] 포함
- [핵심] 포함
- [실무] 포함
- [FAQ] 포함
- Flow 포함
- 예제 포함
- Troubleshooting 포함
- Retrieval Queries 포함

용어 통일:

- Git
- GitHub
- Repository
- Local Repository
- Remote Repository
- Working Directory
- Staging Area
- Commit
- Branch
- Merge
- Rebase
- Pull Request
- Code Review
- Branch Protection

실무성:

- main 직접 Push 금지
- feature Branch 기반 작업
- Pull Request 기반 Merge
- Code Review 반영
- Branch Protection 반영
- Force Push 주의
- Secrets Commit 금지
- Conflict 해결 후 테스트

Troubleshooting:

- Push Rejected
- Merge Conflict
- Rebase Conflict
- Detached HEAD
- Wrong Commit
- Wrong Branch
- Reset 실수
- Force Push 사고
- Authentication failed
- Repository not found

---

### [주의]

Git 문서는 명령어 나열만으로는 부족하다.

Agent가 사용자 상황을 판단하려면 다음 정보가 필요하다.

```text
문제
→ 원인
→ 해결 명령
→ 주의사항
```

RAG Retrieval을 위해 FAQ와 Troubleshooting Query를 충분히 포함해야 한다.

---

### [FAQ]

Q. Git / GitHub 문서 검수 핵심은?
A. Core 개념, 실무 Workflow, Troubleshooting, Retrieval Queries가 모두 포함되었는지 확인하는 것이다.

Q. Agent용 Git 문서에서 가장 중요한 영역은?
A. Staging Area, Commit, Branch, Merge, Rebase, Remote, Pull Request, Troubleshooting이다.

Q. Git 명령어만 정리하면 충분한가?
A. 아니다. 문제 상황, 원인, 해결 흐름, 주의사항이 함께 있어야 Agent가 판단할 수 있다.

Q. Git / GitHub RAG 문서의 최종 목표는?
A. Agent가 Git Workflow 설명, 명령 추천, 충돌 해결, 협업 절차 검토를 수행할 수 있게 하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Branch Strategy란?
A. Branch Strategy는 팀이 Branch를 생성, 병합, 배포하는 기준을 정한 협업 규칙이다.

Q. Branch Strategy가 필요한 이유는?
A. 협업 충돌을 줄이고 배포 가능한 코드와 개발 중인 코드를 안전하게 분리하기 위해 필요하다.

Q. main Branch 역할은?
A. main Branch는 항상 배포 가능한 안정 코드를 유지하는 Branch이다.

Q. develop Branch 역할은?
A. develop Branch는 다음 배포를 위해 기능들이 통합되는 개발 Branch이다.

Q. feature Branch 역할은?
A. feature Branch는 개별 기능을 독립적으로 개발하기 위한 Branch이다.

Q. release Branch 역할은?
A. release Branch는 배포 전 테스트, 버그 수정, 버전 준비를 위한 Branch이다.

Q. hotfix Branch 역할은?
A. hotfix Branch는 운영 배포 코드에서 긴급 버그를 수정하기 위한 Branch이다.

Q. GitHub Flow란?
A. GitHub Flow는 main Branch와 feature Branch, Pull Request를 중심으로 운영하는 단순한 Branch Strategy이다.

Q. GitHub Flow는 언제 적합한가?
A. 소규모 팀, 빠른 배포, CI/CD가 있는 웹 서비스에 적합하다.

Q. GitHub Flow 핵심 절차는?
A. Branch 생성 → Commit → Push → Pull Request → Review → main Merge이다.

Q. Git Flow란?
A. Git Flow는 main, develop, feature, release, hotfix Branch를 구분하여 개발과 배포를 관리하는 Branch Strategy이다.

Q. Git Flow는 언제 적합한가?
A. 배포 주기가 명확하고 Release 관리가 필요한 프로젝트에 적합하다.

Q. release Branch는 언제 만드는가?
A. 배포 전 테스트, 버그 수정, 버전 준비를 위해 만든다.

Q. hotfix Branch는 어디서 분기하는가?
A. 운영 배포 코드 기준인 main Branch에서 분기한다.

Q. Hotfix 후 develop에도 Merge해야 하는가?
A. 해야 한다. develop에 반영하지 않으면 다음 배포에서 같은 버그가 다시 발생할 수 있다.

Q. Trunk Based Development란?
A. 짧은 주기로 main 또는 trunk Branch에 작은 변경을 자주 통합하는 Branch Strategy이다.

Q. Trunk Based Development 장점은?
A. 장기 Branch를 줄이고 Conflict를 줄이며 빠른 배포를 가능하게 한다.

Q. Trunk Based Development에 필요한 조건은?
A. 강한 CI/CD, 충분한 자동 테스트, 작은 변경 단위가 필요하다.

Q. Feature Flag란?
A. 코드 배포와 기능 노출을 분리하기 위해 기능 활성화 여부를 설정으로 제어하는 방식이다.

Q. 학원 팀 프로젝트에 추천하는 Branch 구조는?
A. main, develop, feature/_, fix/_, docs/\* 중심의 단순 구조를 권장한다.

Q. feature Branch는 어디서 분기하는가?
A. 보통 최신 develop Branch에서 분기한다.

Q. main Branch는 언제 업데이트하는가?
A. develop이 안정화되고 발표 또는 배포 가능한 상태일 때 main에 반영한다.

Q. Release Workflow란?
A. 개발 완료 코드를 배포 가능한 버전으로 안정화하고 main에 반영하는 절차이다.

Q. Release Tag는 왜 필요한가?
A. 어떤 Commit이 배포 버전인지 명확히 표시하기 위해 필요하다.

Q. Release Note에는 무엇을 적는가?
A. 배포 버전의 기능 추가, 버그 수정, 변경 사항을 적는다.

Q. Detached HEAD란?
A. HEAD가 Branch가 아니라 특정 Commit을 직접 가리키는 상태이다.

Q. Detached HEAD에서 작업을 보존하려면?
A. git switch -c new-branch로 Branch를 생성해야 한다.

Q. Detached HEAD에서 잃어버린 Commit은 어떻게 찾는가?
A. git reflog로 이전 HEAD 기록을 확인해 찾을 수 있다.

Q. Reflog란?
A. Local Repository에서 HEAD와 Branch Reference가 이동한 기록을 저장하는 Git 기능이다.

Q. Reflog는 언제 쓰는가?
A. Reset, Rebase, Detached HEAD, Branch 삭제 같은 실수를 복구할 때 사용한다.

Q. reset --hard 실수는 어떻게 복구하는가?
A. git reflog로 이전 HEAD를 찾고 git reset --hard HEAD@{n}으로 복구한다.

Q. Force Push란?
A. Local History로 Remote Branch History를 강제로 덮어쓰는 Push 방식이다.

Q. Force Push가 위험한 이유는?
A. 팀원의 Commit을 Remote에서 사라지게 만들 수 있기 때문이다.

Q. --force와 --force-with-lease 차이는?
A. --force-with-lease는 Remote가 예상과 다르면 Push를 거부하여 덮어쓰기 위험을 줄인다.

Q. main에 Force Push를 막으려면?
A. GitHub Branch Protection에서 Force Push를 금지한다.

Q. 잘못된 Branch에 Commit했을 때는?
A. 올바른 Branch로 이동해 git cherry-pick <commit-hash>를 사용한다.

Q. Commit Message 오타는 어떻게 고치는가?
A. Push 전이면 git commit --amend -m "new message"를 사용한다.

Q. Commit에 잘못된 파일이 들어갔을 때는?
A. Push 전이면 Reset 후 올바른 파일만 다시 Staging하여 Commit한다.

Q. Push한 Commit을 취소하려면?
A. 공유 Branch에서는 git revert <commit-hash>를 사용하는 것이 안전하다.

Q. Git 문제가 발생하면 가장 먼저 확인할 것은?
A. git status, git branch, git log --oneline을 먼저 확인한다.

Q. Remote 관련 문제는 무엇을 확인하는가?
A. git remote -v, git branch -vv, git fetch origin으로 Remote와 Upstream 상태를 확인한다.

Q. Conflict 해결 후 공통으로 해야 할 일은?
A. 파일 수정, Marker 제거, git add, Commit 또는 Rebase Continue, 테스트를 수행한다.

Q. Git / GitHub 문서 검수 핵심은?
A. Core 개념, 실무 Workflow, Troubleshooting, Retrieval Queries가 모두 포함되었는지 확인하는 것이다.

Q. Agent용 Git 문서에서 가장 중요한 영역은?
A. Staging Area, Commit, Branch, Merge, Rebase, Remote, Pull Request, Troubleshooting이다.

Q. Git 명령어만 정리하면 충분한가?
A. 아니다. 문제 상황, 원인, 해결 흐름, 주의사항이 함께 있어야 Agent가 판단할 수 있다.

Q. Git / GitHub RAG 문서의 최종 목표는?
A. Agent가 Git Workflow 설명, 명령 추천, 충돌 해결, 협업 절차 검토를 수행할 수 있게 하는 것이다.
