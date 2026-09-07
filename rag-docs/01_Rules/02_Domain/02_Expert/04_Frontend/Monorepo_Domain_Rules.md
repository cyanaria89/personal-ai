# Monorepo Domain Rules

---

# 1. Domain Purpose

## 1.1 Monorepo Domain 목적

### [개념]

Monorepo Domain 문서는 Frontend Agent / Backend Agent / DevOps Agent / Architecture Review Agent / Review Agent용 RAG 문서 제작 규칙이다.

Monorepo는 여러 애플리케이션과 패키지를 하나의 Repository에서 관리하는 구조이다. Frontend, Backend, Shared Library, Design System, Config, Tooling, CI/CD를 하나의 Workspace로 묶어 코드 공유, 의존성 관리, 빌드 최적화, 협업 표준화를 지원한다.

목적:

- Monorepo 구조 설계 지원
- Workspace / Package 경계 설계 지원
- Frontend / Backend / Shared Package 분리 지원
- Next.js / React / Node / Backend 프로젝트 통합 지원
- Design System Package 설계 지원
- Shared Config Package 설계 지원
- Dependency Management 지원
- Task Pipeline / Build Pipeline 설계 지원
- Local Cache / Remote Cache 전략 지원
- CI/CD 최적화 지원
- Versioning / Release 전략 지원
- Package Boundary / Import Boundary 리뷰 지원
- Monorepo 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Repository Structure
2. Workspace Management
3. Package Boundary
4. App / Package Separation
5. Shared Library Design
6. Dependency Management
7. Task Pipeline
8. Build / Test / Lint Orchestration
9. Local Cache / Remote Cache
10. Affected Build / Affected Test
11. TypeScript Project Reference
12. Shared Config
13. Design System Package
14. API Contract Sharing
15. CI/CD Optimization
16. Versioning / Release
17. Security / Access Control
18. Monorepo Troubleshooting
19. Architecture Review Criteria

---

### [실무]

2026 실무 기준:

- JavaScript / TypeScript Monorepo 기준 우선
- `pnpm workspace`, Turborepo, Nx 기준 구조 포함
- Next.js App Router / React / Design System / Shared UI 연계 가능하게 작성
- 앱과 패키지 경계를 명확히 구분
- `apps`는 실행 가능한 애플리케이션 중심
- `packages`는 재사용 가능한 라이브러리 중심
- Shared Package에는 비즈니스 결합도가 낮은 코드만 배치
- Feature 전용 코드를 무분별하게 Shared Package로 승격하지 않음
- Package 간 의존성 방향 명확화
- Root 설정과 Package 설정 책임 분리
- 빌드 / 테스트 / 린트 작업은 Task Pipeline으로 관리
- Cache 가능한 작업과 Cache하면 안 되는 작업 구분
- CI에서는 변경 영향 범위 기반 실행을 우선 검토
- Agent가 구조 설계와 코드 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Monorepo Domain 문서는 무엇을 위한 문서인가?

A.
Agent가 여러 앱과 패키지를 하나의 Repository에서 관리하는 구조, 의존성, 빌드, 테스트, 배포, 공유 코드 경계를 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. Monorepo는 단순히 여러 프로젝트를 한 폴더에 넣는 것인가?

A.
아니다. Workspace, Package Boundary, Task Pipeline, Dependency Management, CI/CD 최적화 기준이 함께 있어야 한다.

Q. Monorepo 문서는 Frontend 전용인가?

A.
아니다. Frontend 중심으로 시작할 수 있지만 Backend, Shared Package, Design System, API Contract, DevOps Pipeline까지 연결된다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Monorepo Domain은 여러 프로젝트를 하나의 Repository에서 안정적으로 관리하기 위한 구조, 도구, 규칙, 자동화 기준을 포함한다.

---

### [핵심]

포함 범위:

- Monorepo
- Workspace
- Package
- App
- Library
- `apps`
- `packages`
- `tools`
- `configs`
- `pnpm-workspace.yaml`
- `package.json`
- Workspace Protocol
- Turborepo
- Nx
- Task Pipeline
- Dependency Graph
- Build Graph
- Local Cache
- Remote Cache
- Affected Build
- Affected Test
- Incremental Build
- Shared UI Package
- Design System Package
- Shared Config Package
- TypeScript Config Package
- ESLint Config Package
- Prettier Config Package
- API Client Package
- Type Package
- Utility Package
- Versioning
- Release
- Changeset
- CI/CD
- Deployment
- Import Boundary
- Package Boundary
- Circular Dependency
- Dependency Hoisting
- Lockfile
- Peer Dependency
- Internal Package
- External Package

---

### [실무]

제외 범위:

- Git Submodule 심화
- Polyrepo 운영 심화
- Micro Frontend 심화
- Module Federation 심화
- Kubernetes 배포 심화
- Backend MSA 심화
- Package Registry 운영 심화
- NPM Package Publishing 심화
- Bazel / Buck / Pants 심화
- 대규모 Enterprise Governance 심화
- 언어별 빌드 시스템 전체 설명

단, Monorepo 구조 판단에 필요한 수준의 CI/CD, 배포, 버전 관리, 패키지 배포, 프론트엔드 / 백엔드 연계 지식은 포함 가능하다.

---

### [FAQ]

Q. Monorepo 문서에 Nx와 Turborepo를 모두 포함해야 하나?

A.
포함한다. 단, 도구 사용법 전체가 아니라 선택 기준, Task Pipeline, Cache, Affected 실행 기준 중심으로 작성한다.

Q. pnpm workspace도 포함해야 하나?

A.
포함한다. JavaScript / TypeScript Monorepo에서 Workspace와 Package 연결의 기본 개념으로 중요하다.

Q. Micro Frontend도 이 문서에 포함하나?

A.
심화는 제외한다. Monorepo와 Micro Frontend의 관계는 비교 수준으로만 다룬다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Monorepo RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Monorepo 문서는 구조와 작업 흐름이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Code Change → Dependency Graph → Affected Tasks → Cache → CI Result
- `[Comparison]`: Monorepo vs Polyrepo, Turborepo vs Nx
- `[Best Practice]`: Package Boundary, Shared Package, Task Pipeline
- `[Troubleshooting]`: Circular Dependency, Cache Miss, Dependency Conflict
- `[Checklist]`: Monorepo 설계 / CI / Release 검수

---

### [FAQ]

Q. Monorepo 문서에 Flow가 필요한 이유는?

A.
Monorepo는 코드 변경이 어떤 패키지와 앱의 build, test, deploy에 영향을 주는지 추적해야 하므로 Flow가 중요하다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Monorepo Core Concept Rules

## 4.1 Monorepo 기본 개념

### [개념]

Monorepo는 여러 개의 앱과 라이브러리 패키지를 하나의 Git Repository에서 관리하는 구조이다.

Polyrepo는 앱이나 서비스마다 별도 Repository를 사용하는 구조이다.

---

### [핵심]

Monorepo 핵심 요소:

- Single Repository
- Multiple Apps
- Multiple Packages
- Shared Code
- Workspace
- Dependency Graph
- Task Pipeline
- Unified Tooling
- Centralized Config
- Atomic Change
- Cross-package Refactoring
- Shared CI/CD

기본 구조:

```text
repository
├ apps
│  ├ web
│  ├ admin
│  └ api
├ packages
│  ├ ui
│  ├ config
│  ├ types
│  └ utils
├ tools
├ package.json
├ pnpm-workspace.yaml
└ turbo.json
```

---

### [실무]

Monorepo가 적합한 상황:

- 여러 앱이 공통 UI / 타입 / 유틸을 공유함
- Frontend Web / Admin / Mobile Web이 같은 도메인 공유
- Design System을 여러 앱에서 사용
- API Client / DTO / Schema를 공유
- 팀이 동일한 Tooling과 Coding Standard를 사용
- Cross-package 변경을 하나의 PR에서 처리하고 싶음
- CI에서 변경 영향 범위 기반 실행이 필요함

Monorepo가 부적합할 수 있는 상황:

- 프로젝트 간 공유 코드가 거의 없음
- 팀 / 권한 / 배포 주기가 완전히 다름
- Repository 크기와 CI 복잡도를 감당할 운영 체계가 없음
- Package Boundary를 관리할 규칙이 없음
- 모든 앱이 서로 무분별하게 의존할 가능성이 큼

---

### [FAQ]

Q. Monorepo는 언제 쓰는 게 좋아?

A.
여러 앱이 공통 UI, 타입, 유틸, API Client, 설정을 공유하고 변경을 하나의 PR에서 함께 관리해야 할 때 적합하다.

Q. Monorepo가 항상 좋은가?

A.
아니다. 공유 코드가 적거나 팀 / 배포 / 권한 경계가 완전히 다르면 Polyrepo가 더 단순할 수 있다.

Q. Monorepo의 핵심은 무엇인가?

A.
하나의 Repository 자체가 아니라 Package Boundary, Dependency Graph, Task Pipeline, Cache, CI 최적화이다.

---

# 5. Repository Structure Rules

## 5.1 Monorepo 폴더 구조

### [개념]

Repository Structure는 앱, 패키지, 설정, 도구, 문서의 위치를 명확히 하여 코드 탐색과 변경 영향 분석을 쉽게 만드는 기준이다.

---

### [핵심]

권장 최상위 구조:

```text
repo
├ apps
│  ├ web
│  ├ admin
│  └ api
├ packages
│  ├ ui
│  ├ config
│  ├ eslint-config
│  ├ typescript-config
│  ├ types
│  ├ api-client
│  └ utils
├ tools
│  └ scripts
├ docs
├ package.json
├ pnpm-workspace.yaml
├ turbo.json
└ tsconfig.base.json
```

역할:

| 경로        | 책임                        |
| ----------- | --------------------------- |
| `apps`      | 실행 가능한 애플리케이션    |
| `packages`  | 재사용 가능한 내부 패키지   |
| `tools`     | 빌드 / 생성 / 검증 스크립트 |
| `docs`      | 아키텍처 / 운영 문서        |
| root config | Workspace 공통 설정         |

---

### [실무]

구조 작성 기준:

- `apps`에는 배포 가능한 앱 배치
- `packages`에는 여러 앱에서 재사용되는 패키지 배치
- `packages/ui`는 Design System 또는 Shared UI
- `packages/config`는 공통 설정
- `packages/types`는 공유 타입
- `packages/api-client`는 API Client / SDK
- `tools`는 자동화 스크립트
- Root에는 Workspace 공통 설정
- 앱별 설정은 각 앱 내부에 둠
- 공통화되지 않은 Feature 코드는 해당 앱 내부에 유지

주의:

- 모든 코드를 `packages`로 빼지 않기
- Feature 전용 코드를 Shared Package로 성급히 승격하지 않기
- Root 설정이 너무 많은 책임을 갖지 않게 하기
- `packages/utils`가 잡동사니가 되지 않도록 관리
- 앱 간 직접 import보다 공유 패키지 사용

---

### [FAQ]

Q. Monorepo에서 `apps`와 `packages` 차이는?

A.
`apps`는 실행 / 배포되는 애플리케이션이고, `packages`는 여러 앱에서 재사용되는 라이브러리이다.

Q. 모든 공통 코드는 `packages`로 빼야 하나?

A.
아니다. 실제로 여러 앱에서 반복 사용되고 경계가 명확한 코드만 패키지로 분리한다.

Q. `packages/utils`는 어떻게 관리해야 하나?

A.
잡동사니 폴더가 되지 않도록 날짜, 문자열, 검증, 포맷터처럼 목적별로 나누고 도메인 로직은 별도 패키지로 분리한다.

---

# 6. Workspace Rules

## 6.1 Workspace 관리

### [개념]

Workspace는 하나의 Repository 안에서 여러 Package를 연결하고 내부 Package 간 의존성을 관리하는 기능이다.

---

### [핵심]

필수 포함:

- Workspace
- Package Manager
- pnpm Workspace
- npm Workspace
- Yarn Workspace
- Workspace Package
- Internal Dependency
- Workspace Protocol
- Lockfile
- Root Package
- Package Script
- Package Filter

`pnpm-workspace.yaml` 예시:

```yaml
packages:
  - "apps/*"
  - "packages/*"
```

내부 의존성 예시:

```json
{
  "dependencies": {
    "@repo/ui": "workspace:*",
    "@repo/utils": "workspace:*"
  }
}
```

---

### [실무]

Workspace 작성 기준:

- Workspace 범위는 `apps/*`, `packages/*`처럼 명확히 지정
- 내부 패키지는 `workspace:*` 또는 명확한 Workspace Protocol 사용
- Root `package.json`에는 공통 scripts 관리
- 각 패키지 `package.json`에는 개별 scripts 관리
- Lockfile은 Repository Root에서 관리
- 패키지 설치는 Root에서 수행
- Package Manager는 팀 전체에서 하나로 통일
- `packageManager` 필드 명시 권장

주의:

- npm / yarn / pnpm 혼용 금지
- Lockfile 여러 개 생성 금지
- 내부 패키지를 외부 registry 버전처럼 참조하지 않기
- Workspace 범위에 불필요한 폴더 포함 금지

---

### [FAQ]

Q. Workspace는 왜 필요한가?

A.
Monorepo 안의 여러 앱과 패키지를 하나의 의존성 그래프로 연결하고 내부 패키지 참조를 쉽게 관리하기 위해 필요하다.

Q. `workspace:*`는 무엇인가?

A.
외부 registry가 아니라 같은 Workspace 안의 내부 패키지를 참조한다는 의미이다.

Q. Lockfile은 어디에 두는 게 좋나?

A.
Monorepo Root에 하나로 관리하는 것이 일반적이다.

---

# 7. Package Boundary Rules

## 7.1 Package 경계 설계

### [개념]

Package Boundary는 각 패키지가 어떤 책임을 갖고 어떤 패키지에 의존할 수 있는지 정의하는 규칙이다.

---

### [핵심]

필수 포함:

- Package Responsibility
- Public API
- Internal API
- Dependency Direction
- Import Boundary
- Package Encapsulation
- Deep Import Prevention
- Circular Dependency Prevention
- Stable Interface
- Ownership

Boundary 원칙:

```text
apps
→ feature packages
→ domain packages
→ shared packages
→ config packages
```

---

### [실무]

Package Boundary 작성 기준:

- 패키지는 하나의 명확한 책임을 가짐
- 외부 공개 API는 `index.ts` 또는 `exports`로 제한
- 패키지 내부 파일 deep import 금지
- 앱은 패키지를 조합할 수 있음
- 공통 패키지는 앱을 import하지 않음
- 하위 패키지는 상위 패키지를 import하지 않음
- 순환 의존성 금지
- 패키지 간 의존성은 `package.json`에 명확히 선언
- 변경이 잦은 Feature 로직과 안정적인 Shared 로직 분리
- 패키지 README에 책임과 사용 기준 기록 권장

---

### [FAQ]

Q. Package Boundary가 왜 중요한가?

A.
패키지 간 결합도를 낮추고 변경 영향 범위와 빌드 / 테스트 대상을 예측 가능하게 만들기 위해 중요하다.

Q. Deep Import는 왜 피해야 하나?

A.
패키지 내부 구현에 직접 의존하면 리팩토링이 어려워지고 Public API가 무력화되기 때문이다.

Q. 순환 의존성이 생기면 어떻게 해야 하나?

A.
공통 타입이나 유틸을 더 하위 Shared Package로 분리하거나 패키지 책임을 재설계해야 한다.

---

# 8. App Package Rules

## 8.1 Apps 설계

### [개념]

App Package는 실제로 실행되고 배포되는 애플리케이션이다.

---

### [핵심]

App 예시:

- `apps/web`
- `apps/admin`
- `apps/api`
- `apps/docs`
- `apps/storybook`
- `apps/mobile-web`

App 책임:

- Routing
- Page Composition
- Environment Config
- App-level Provider
- App-specific Feature
- Deployment Config
- Runtime Config
- App-specific Test
- App-specific Assets

---

### [실무]

App 작성 기준:

- 앱은 배포 가능한 단위
- 앱 내부에는 해당 앱 전용 Feature 배치 가능
- 공통 UI / 타입 / 유틸은 패키지로 import
- 앱별 환경변수와 배포 설정은 앱 내부 또는 배포 시스템에서 관리
- 앱별 `package.json` scripts 명확화
- 앱이 다른 앱을 직접 import하지 않기
- 앱 간 공유가 필요하면 `packages`로 분리
- 앱 내부 Feature가 다른 앱에서도 필요해지면 Shared Package 승격 검토

예시:

```text
apps
└ web
   ├ app
   ├ src
   │  ├ features
   │  └ widgets
   ├ package.json
   └ next.config.ts
```

---

### [FAQ]

Q. App Package에는 무엇을 넣어야 하나?

A.
라우팅, 페이지 조립, 앱 전용 기능, 앱 전용 설정, 배포 설정을 넣는다.

Q. 앱끼리 직접 import해도 되나?

A.
권장하지 않는다. 공유가 필요하면 별도 Package로 분리해야 한다.

Q. 앱 전용 Feature를 처음부터 Package로 빼야 하나?

A.
아니다. 한 앱에서만 쓰이면 앱 내부에 두고 반복 사용이 확인되면 Package로 승격한다.

---

# 9. Shared Package Rules

## 9.1 Shared Package 설계

### [개념]

Shared Package는 여러 앱이나 패키지에서 재사용되는 공통 코드 단위이다.

---

### [핵심]

Shared Package 예시:

- `@repo/ui`
- `@repo/design-system`
- `@repo/types`
- `@repo/utils`
- `@repo/api-client`
- `@repo/config`
- `@repo/eslint-config`
- `@repo/typescript-config`
- `@repo/testing`
- `@repo/logger`
- `@repo/auth-client`

Shared Package 기준:

- Reusable
- Stable
- Low Business Coupling
- Clear Public API
- Independent Test
- Versionable
- Documented

---

### [실무]

Shared Package 승격 기준:

- 두 개 이상 앱 / 패키지에서 반복 사용
- 비즈니스 로직 결합도가 낮음
- 책임이 명확함
- 독립 테스트 가능
- API가 안정적
- 공통화 후 변경 영향이 예측 가능
- 문서화 가능한 사용 규칙이 있음

주의:

- 공통화가 목적이 아니라 변경 비용 감소가 목적
- 너무 빨리 Shared Package로 빼면 추상화 비용 증가
- 도메인 로직이 강하면 Domain Package로 분리 검토
- Shared Package가 앱을 import하면 안 됨
- `@repo/utils` 비대화 방지

---

### [FAQ]

Q. 어떤 코드를 Shared Package로 빼야 하나?

A.
여러 앱에서 반복 사용되고 책임이 명확하며 비즈니스 결합도가 낮은 코드를 Shared Package로 분리한다.

Q. Shared Package로 너무 빨리 빼면 왜 문제인가?

A.
요구사항이 안정되기 전에 추상화되어 API 변경 비용과 사용 복잡도가 증가할 수 있다.

Q. Shared Package가 App을 import해도 되나?

A.
안 된다. Shared Package는 하위 공통 레이어이므로 앱에 의존하면 구조가 무너진다.

---

# 10. Design System Package Rules

## 10.1 UI / Design System Package

### [개념]

Design System Package는 여러 앱에서 재사용되는 UI Component, Design Token, Theme, Accessibility Pattern을 제공하는 패키지이다.

---

### [핵심]

필수 포함:

- `@repo/ui`
- `@repo/design-system`
- Component Library
- Design Token
- Theme
- Button
- Input
- Modal
- Form Field
- Toast
- Storybook
- CSS Export
- Server Component Compatibility
- Client Component Boundary
- Peer Dependency

구조 예시:

```text
packages
└ ui
   ├ src
   │  ├ button
   │  ├ input
   │  ├ modal
   │  ├ theme
   │  └ index.ts
   ├ package.json
   └ tsconfig.json
```

---

### [실무]

Design System Package 기준:

- 비즈니스 로직 금지
- Feature Package import 금지
- Token과 Component 분리
- 접근성 기본값 포함
- Client Hook이 필요한 컴포넌트는 Client Boundary 명확화
- Next.js Server Component에서 사용할 수 있는 순수 UI와 Client Component 구분
- React는 보통 Peer Dependency로 관리 검토
- 스타일 export 방식 문서화
- Storybook 또는 Docs App과 연계
- Visual Regression Test 고려
- Breaking Change 관리

주의:

- UI Package 전체에 무조건 `use client` 선언 금지
- 단순 Button / Card / Badge는 Server Component 호환 가능하게 설계
- Modal / Dropdown / Select는 Client Component 필요 가능성 높음
- 앱별 비즈니스 스타일 요구를 공통 variant로 무분별하게 추가하지 않기

---

### [FAQ]

Q. Monorepo에서 Design System은 어디에 두나?

A.
보통 `packages/ui` 또는 `packages/design-system`에 둔다.

Q. UI Package 전체를 Client Component로 만들어도 되나?

A.
권장하지 않는다. 상호작용이 필요한 컴포넌트만 Client Boundary를 갖도록 분리하는 것이 좋다.

Q. Design System Package가 Feature를 import해도 되나?

A.
안 된다. Design System은 공통 UI Layer이므로 Feature에 의존하면 안 된다.

---

# 11. Shared Config Package Rules

## 11.1 Config Package 설계

### [개념]

Shared Config Package는 TypeScript, ESLint, Prettier, Build Tool, Test Tool 설정을 여러 앱과 패키지에서 일관되게 공유하기 위한 패키지이다.

---

### [핵심]

Config Package 예시:

- `@repo/typescript-config`
- `@repo/eslint-config`
- `@repo/prettier-config`
- `@repo/vite-config`
- `@repo/jest-config`
- `@repo/playwright-config`

구조 예시:

```text
packages
├ typescript-config
│  ├ base.json
│  ├ react-library.json
│  └ nextjs.json
├ eslint-config
│  ├ base.js
│  ├ react.js
│  └ next.js
└ prettier-config
   └ index.js
```

---

### [실무]

Config Package 기준:

- Root 설정과 Package 설정을 분리
- React / Next.js / Node / Library별 config 분리
- 앱은 필요한 config를 extends
- 공통 룰은 Base Config에 둠
- 도구 버전은 Root에서 통일
- ESLint Boundary Rule 고려
- TypeScript path / reference 설정과 충돌 주의
- Config Package 변경 시 전체 앱 영향 확인
- Breaking Change로 취급할 수 있음

주의:

- 모든 프로젝트에 동일 config를 강제하지 않기
- Next.js 앱과 Node 패키지의 TypeScript 설정 차이 고려
- ESLint 규칙을 과도하게 엄격하게 만들어 개발 속도 저하시키지 않기

---

### [FAQ]

Q. Shared Config Package는 왜 필요한가?

A.
여러 앱과 패키지에서 TypeScript, ESLint, Prettier 설정을 일관되게 유지하고 중복을 줄이기 위해 필요하다.

Q. Next.js 앱과 Library Package가 같은 tsconfig를 써도 되나?

A.
항상 적합하지는 않다. 실행 환경과 빌드 방식이 다르므로 base config를 공유하고 세부 config를 분리하는 것이 좋다.

Q. Config Package 변경은 위험한가?

A.
그렇다. 여러 앱과 패키지에 동시에 영향을 줄 수 있으므로 CI 검증이 필요하다.

---

# 12. API Contract Package Rules

## 12.1 API Client / Types Package

### [개념]

API Contract Package는 Frontend와 Backend가 공유하는 API Request / Response Type, Schema, Client SDK를 관리하는 패키지이다.

---

### [핵심]

필수 포함:

- API Contract
- DTO
- Request Type
- Response Type
- Schema
- Runtime Validation
- API Client
- SDK
- OpenAPI Generated Client
- Type Sharing
- Version Compatibility
- Breaking Change

구조 예시:

```text
packages
├ api-contract
│  ├ src
│  │  ├ schemas
│  │  ├ types
│  │  └ index.ts
│  └ package.json
└ api-client
   ├ src
   │  ├ client.ts
   │  ├ auth.ts
   │  └ index.ts
   └ package.json
```

---

### [실무]

API Contract 작성 기준:

- Backend DTO와 Frontend View Model을 구분
- 외부 API 응답은 Runtime Validation 고려
- API Client는 인증 헤더 / 에러 매핑 기준 포함
- OpenAPI 기반 생성 코드는 생성물과 수동 코드를 분리
- Contract 변경은 Breaking Change 여부 확인
- Frontend와 Backend가 같은 TypeScript Monorepo에 있으면 타입 공유 가능
- 다른 언어 Backend와 연계 시 OpenAPI / Schema 기반 공유 검토
- API Contract Package가 UI Package를 import하지 않도록 함

주의:

- Backend 내부 Entity를 그대로 Frontend에 공유 금지
- API Contract를 지나치게 자주 변경하지 않기
- View Model을 Contract Package에 넣지 않기
- Runtime Validation 없는 외부 입력 신뢰 금지

---

### [FAQ]

Q. API 타입은 Monorepo에서 공유해도 되나?

A.
가능하다. 단, Backend 내부 Entity가 아니라 API Request / Response Contract를 공유해야 한다.

Q. DTO와 View Model은 같은가?

A.
아니다. DTO는 API 계약이고 View Model은 화면 표시를 위한 프론트엔드 구조이다.

Q. OpenAPI 생성 코드는 어디에 두나?

A.
`packages/api-client` 또는 `packages/api-contract`에 두고 수동 코드와 분리하는 것이 좋다.

---

# 13. Dependency Management Rules

## 13.1 의존성 관리

### [개념]

Dependency Management는 Monorepo 전체의 외부 패키지 버전, 내부 패키지 연결, Peer Dependency, Dev Dependency, Lockfile을 관리하는 기준이다.

---

### [핵심]

필수 포함:

- External Dependency
- Internal Dependency
- Peer Dependency
- Dev Dependency
- Root Dependency
- Package Dependency
- Hoisting
- Lockfile
- Version Pinning
- Dependency Deduplication
- Dependency Constraint
- Security Update

의존성 위치 기준:

| 유형                        | 위치                        |
| --------------------------- | --------------------------- |
| 앱 런타임 의존성            | 해당 app `package.json`     |
| 패키지 런타임 의존성        | 해당 package `package.json` |
| 공통 개발 도구              | root `package.json`         |
| React 같은 host 제공 의존성 | peerDependency 검토         |
| 내부 패키지                 | `workspace:*`               |

---

### [실무]

의존성 작성 기준:

- 사용하는 패키지의 `package.json`에 의존성 명시
- Root에 모든 의존성을 몰아넣지 않음
- 공통 개발 도구는 Root에 둠
- 내부 패키지는 Workspace Protocol 사용
- UI Library는 React / React DOM Peer Dependency 검토
- 중복 버전은 가능한 통일
- Lockfile 변경은 리뷰 대상
- 불필요한 의존성 제거
- 보안 취약 패키지 업데이트
- Dependency 변경은 영향 범위 확인

주의:

- Hoisting에 기대서 누락된 dependency 사용 금지
- 앱에서만 쓰는 패키지를 Root에 무분별하게 설치 금지
- Peer Dependency 누락 시 라이브러리 사용처에서 오류 발생 가능
- Dependency 버전 충돌은 빌드 / 런타임 오류 원인

---

### [FAQ]

Q. Monorepo에서 의존성은 Root에 다 설치하면 되나?

A.
아니다. 실제로 사용하는 앱이나 패키지의 `package.json`에 명시해야 한다. 공통 개발 도구만 Root에 두는 것이 좋다.

Q. Peer Dependency는 언제 쓰나?

A.
UI Library처럼 React를 직접 포함하지 않고 사용하는 앱이 제공해야 하는 의존성에 사용한다.

Q. Hoisting에 의존하면 왜 위험한가?

A.
패키지에 명시되지 않은 의존성을 우연히 사용할 수 있어 다른 환경에서 빌드가 깨질 수 있다.

---

# 14. Task Pipeline Rules

## 14.1 Build / Test / Lint 작업 파이프라인

### [개념]

Task Pipeline은 Monorepo 안의 여러 앱과 패키지에서 build, test, lint, typecheck 같은 작업을 올바른 순서와 의존성 기준으로 실행하는 구조이다.

---

### [핵심]

필수 포함:

- Task
- Pipeline
- Build
- Test
- Lint
- Typecheck
- Dev
- Dependency Task
- Parallel Task
- Sequential Task
- Output
- Cache Key
- Task Input
- Task Output
- Persistent Task

Pipeline Flow:

```text
Code Change
→ Determine Project
→ Determine Dependencies
→ Run Required Tasks
→ Store or Restore Cache
→ Report Result
```

Turborepo 예시:

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": []
    },
    "lint": {
      "outputs": []
    }
  }
}
```

---

### [실무]

Task Pipeline 작성 기준:

- 라이브러리 build 후 앱 build 실행
- `build`는 의존 패키지의 `build`에 의존
- `lint`, `test`, `typecheck`는 병렬 실행 가능
- `dev`는 cache하지 않음
- `build` output 명확히 지정
- `test` output이 없으면 빈 배열 지정 가능
- 입력 파일과 환경변수에 따라 cache key가 달라짐
- Cache 가능한 task와 cache하면 안 되는 task 구분
- Package별 script 이름 통일
- CI와 local script가 동일한 pipeline 사용

주의:

- `dependsOn` 누락 시 잘못된 순서로 build 가능
- outputs 설정 누락 시 cache restore가 불완전할 수 있음
- 환경변수를 cache input에 반영하지 않으면 잘못된 cache 사용 가능
- `dev` server 같은 persistent task는 일반 build task와 다르게 관리

---

### [FAQ]

Q. Task Pipeline은 왜 필요한가?

A.
여러 앱과 패키지의 build, test, lint를 올바른 순서로 실행하고 중복 작업을 줄이기 위해 필요하다.

Q. `build`가 `^build`에 의존한다는 뜻은?

A.
현재 패키지를 build하기 전에 의존하는 내부 패키지들의 build를 먼저 실행한다는 의미이다.

Q. `dev` task도 cache해야 하나?

A.
일반적으로 아니다. Dev server는 지속 실행 작업이므로 build / test cache와 다르게 관리한다.

---

# 15. Caching Rules

## 15.1 Local Cache / Remote Cache

### [개념]

Caching은 동일한 입력에 대해 이미 수행한 build, test, lint 결과를 재사용해 작업 시간을 줄이는 전략이다.

---

### [핵심]

필수 포함:

- Local Cache
- Remote Cache
- Cache Hit
- Cache Miss
- Task Input
- Task Output
- Hash
- Environment Variable
- Lockfile Input
- Output Restore
- Cache Invalidation
- Cache Security

Cache 판단 기준:

| Task         | Cache 적합도 |
| ------------ | ------------ |
| build        | 높음         |
| test         | 높음         |
| lint         | 높음         |
| typecheck    | 높음         |
| format check | 높음         |
| dev server   | 낮음         |
| deploy       | 낮음         |
| publish      | 낮음         |
| migration    | 낮음         |

---

### [실무]

Cache 작성 기준:

- build output 명확히 지정
- test / lint 결과 cache 가능 여부 확인
- 환경변수가 결과에 영향을 주면 cache input에 포함
- Lockfile 변경은 cache invalidation 대상
- Remote Cache는 팀 / CI 속도 개선에 유용
- 민감정보가 output에 포함되지 않도록 주의
- deploy / publish / DB migration은 cache하지 않음
- Cache Hit 결과가 이상하면 input / output 설정 확인
- CI에서는 Remote Cache와 Affected Task 조합 고려
- Remote Cache 권한과 보안 정책 확인

주의:

- 잘못된 Cache는 오래된 빌드 결과를 재사용하게 만듦
- 사용자별 Secret이나 환경별 output을 Cache에 저장하지 않기
- Remote Cache는 접근 권한과 branch / PR 보안 고려
- Cache Miss가 많으면 input 범위가 너무 넓은지 확인

---

### [FAQ]

Q. Monorepo에서 Cache는 왜 중요한가?

A.
여러 앱과 패키지의 build, test, lint 작업이 많아지므로 이전 결과를 재사용해 local과 CI 시간을 줄일 수 있다.

Q. 어떤 task를 cache하면 안 되나?

A.
deploy, publish, DB migration, dev server처럼 외부 상태를 변경하거나 지속 실행되는 작업은 일반적으로 cache하지 않는다.

Q. Cache 결과가 이상하면 무엇을 봐야 하나?

A.
Task input, output, 환경변수, lockfile, dependency graph 설정을 확인해야 한다.

---

# 16. Affected Task Rules

## 16.1 변경 영향 범위 기반 실행

### [개념]

Affected Task는 변경된 파일과 Dependency Graph를 기준으로 영향을 받는 앱과 패키지의 build, test, lint만 실행하는 전략이다.

---

### [핵심]

필수 포함:

- Affected Project
- Affected Build
- Affected Test
- Affected Lint
- Dependency Graph
- Base Commit
- Head Commit
- PR Check
- Changed Files
- Transitive Dependency
- CI Optimization

Affected Flow:

```text
Changed Files
→ Map to Package
→ Traverse Dependency Graph
→ Find Affected Apps / Packages
→ Run Affected Tasks
```

---

### [실무]

Affected 실행 기준:

- PR CI에서 변경 영향 범위 기반 task 실행
- Shared Package 변경 시 의존 앱도 affected
- Config Package 변경 시 넓은 범위 affected 가능
- Lockfile 변경 시 전체 affected 가능성 검토
- Root 설정 변경 시 전체 task 필요 가능
- Base / Head Commit 기준 명확히 설정
- Main Branch merge 후 기준점 관리
- Affected 결과를 신뢰하려면 Dependency Graph가 정확해야 함

주의:

- Dependency 선언 누락 시 affected 계산이 틀림
- Deep Import / Path Alias가 Graph에 반영되는지 확인
- Config 변경을 input으로 포함하지 않으면 누락 가능
- CI 속도만 보고 검증 범위를 과도하게 줄이지 않기

---

### [FAQ]

Q. Affected Build는 무엇인가?

A.
변경된 코드와 의존성 그래프를 기준으로 영향을 받는 앱과 패키지만 build하는 방식이다.

Q. Shared Package를 수정하면 어떤 앱이 affected 되나?

A.
해당 Shared Package를 의존하는 앱과 패키지가 affected 된다.

Q. Affected 실행이 틀릴 수 있나?

A.
그렇다. Dependency 선언 누락, Deep Import, 잘못된 Path Alias, Config input 누락이 있으면 영향을 잘못 계산할 수 있다.

---

# 17. TypeScript Monorepo Rules

## 17.1 TypeScript 설정

### [개념]

TypeScript Monorepo는 여러 앱과 패키지에서 공통 tsconfig를 공유하면서 각 패키지의 build, typecheck, path alias, declaration output을 관리하는 구조이다.

---

### [핵심]

필수 포함:

- `tsconfig.base.json`
- Package tsconfig
- TypeScript Project References
- Path Alias
- Declaration File
- Composite Project
- Incremental Typecheck
- Build Mode
- `noEmit`
- `emitDeclarationOnly`
- Type Boundary

기본 구조:

```text
repo
├ tsconfig.base.json
├ apps
│  └ web
│     └ tsconfig.json
└ packages
   └ ui
      └ tsconfig.json
```

---

### [실무]

TypeScript 작성 기준:

- 공통 compilerOptions는 base config에 둠
- 앱별 / 패키지별 tsconfig 분리
- Library Package는 declaration 생성 검토
- 앱은 보통 framework build에 맡김
- Path Alias와 package exports가 충돌하지 않게 관리
- 내부 패키지 import는 package name 기준 권장
- 타입만 공유하는 패키지는 runtime dependency와 구분
- Typecheck task를 CI에 포함
- `skipLibCheck` 사용 여부는 팀 기준으로 결정
- Project References는 대규모 typecheck 최적화에 유용

주의:

- Path Alias만으로 Package Boundary를 대체하지 않기
- `paths`가 실제 package dependency와 불일치하면 빌드 오류 가능
- Declaration output 누락 시 외부 패키지 소비가 어려움
- App과 Library의 module 설정 차이 주의

---

### [FAQ]

Q. Monorepo에서 tsconfig는 어떻게 관리해?

A.
Root에 base config를 두고 앱과 패키지가 이를 extends해서 각 환경에 맞게 설정한다.

Q. TypeScript Project References는 언제 필요해?

A.
패키지가 많고 typecheck / build 속도와 의존성 순서 관리가 중요해질 때 유용하다.

Q. Path Alias만 쓰면 Monorepo Package가 필요 없나?

A.
아니다. Path Alias는 import 편의 기능이고 Package Boundary와 dependency 선언을 대체하지 않는다.

---

# 18. Build Output Rules

## 18.1 Package Build / Output 관리

### [개념]

Build Output은 각 앱과 패키지가 빌드 후 생성하는 파일이며, Task Cache와 배포에 직접 영향을 준다.

---

### [핵심]

필수 포함:

- Build Output
- `dist`
- `.next`
- `build`
- Declaration Output
- Source Map
- Package Export
- Tree Shaking
- ESM
- CJS
- Type Declaration
- Output Cache
- Clean Build

Output 예시:

| 프로젝트        | Output              |
| --------------- | ------------------- |
| Next.js App     | `.next`             |
| Vite App        | `dist`              |
| Library Package | `dist`              |
| Type Package    | `dist` 또는 `.d.ts` |
| Storybook       | `storybook-static`  |

---

### [실무]

Build Output 기준:

- 각 task의 output 경로 명시
- Library Package는 `dist` 생성 여부 결정
- Internal Package는 source import 방식과 build import 방식 중 선택
- 배포 대상 앱 output 확인
- Source Map 공개 정책 확인
- Clean Build 필요 여부 확인
- `dist`를 Git에 포함할지 여부 결정
- Package exports가 output과 일치해야 함
- Cache restore 대상 output 명확화

주의:

- output 설정이 틀리면 cache hit 후 파일이 없을 수 있음
- `.next`, `dist`, coverage output 구분
- build artifacts를 source와 혼동하지 않기
- Source Map에 민감 정보 포함 여부 확인

---

### [FAQ]

Q. Build Output은 왜 중요해?

A.
배포와 Cache Restore가 build output에 의존하기 때문에 output 경로가 정확해야 한다.

Q. Library Package는 꼭 build해야 하나?

A.
프로젝트 설정에 따라 다르다. source를 직접 참조할 수도 있고 `dist`로 빌드해 소비할 수도 있다.

Q. Source Map은 운영에 올려도 되나?

A.
가능하지만 공개 범위와 민감 정보 노출 여부를 검토해야 한다.

---

# 19. Versioning and Release Rules

## 19.1 버전 관리 / 배포 전략

### [개념]

Versioning and Release는 Monorepo 내부 패키지와 앱의 변경 사항을 어떻게 버전 표시하고 배포할지 정의하는 전략이다.

---

### [핵심]

필수 포함:

- Fixed Versioning
- Independent Versioning
- Semantic Versioning
- Changelog
- Changeset
- Release Note
- Package Publish
- App Deployment
- Breaking Change
- Migration Guide
- Tagging
- Release Branch

Versioning 비교:

| 전략                   | 설명                  | 적합 상황            |
| ---------------------- | --------------------- | -------------------- |
| Fixed Versioning       | 모든 패키지 같은 버전 | 강하게 결합된 패키지 |
| Independent Versioning | 패키지별 독립 버전    | 독립 배포 패키지     |
| App-only Release       | 앱만 배포             | 내부 패키지 비공개   |
| Changeset              | 변경 내역 기반 릴리즈 | 패키지 배포 관리     |

---

### [실무]

Release 기준:

- 내부 앱만 있으면 Package Version보다 App Deployment 중심 가능
- 외부 배포 패키지는 Semantic Versioning 적용
- Breaking Change는 명확히 표시
- Changelog 작성
- Deprecated API는 대체 경로 제공
- Design System Package는 변경 영향이 크므로 Release Note 중요
- API Contract 변경은 Frontend / Backend 영향 확인
- 배포 가능한 앱별 CI/CD 파이프라인 분리
- Tag 전략과 rollback 전략 정의

주의:

- 내부 패키지 버전과 앱 배포 버전을 혼동하지 않기
- Breaking Change를 minor patch처럼 배포하지 않기
- 패키지 배포와 앱 배포를 같은 기준으로 강제하지 않기
- Changelog 없는 공통 패키지 변경은 추적 어려움

---

### [FAQ]

Q. Monorepo에서 모든 패키지가 같은 버전을 가져야 하나?

A.
아니다. 강하게 결합된 패키지는 Fixed Versioning, 독립 배포 패키지는 Independent Versioning을 사용할 수 있다.

Q. 내부 패키지도 NPM에 publish해야 하나?

A.
반드시 그럴 필요는 없다. 같은 Workspace 내부에서만 사용한다면 publish 없이 관리할 수 있다.

Q. Changeset은 언제 쓰나?

A.
여러 패키지의 변경 내역, 버전, changelog, publish를 체계적으로 관리해야 할 때 사용한다.

---

# 20. CI/CD Rules

## 20.1 Monorepo CI/CD 설계

### [개념]

Monorepo CI/CD는 여러 앱과 패키지의 build, test, lint, deploy를 변경 영향 범위와 cache를 활용해 효율적으로 실행하는 구조이다.

---

### [핵심]

필수 포함:

- CI Pipeline
- PR Check
- Main Branch Build
- Affected Build
- Affected Test
- Remote Cache
- Dependency Install
- Lockfile Cache
- Build Cache
- Parallel Job
- Matrix Job
- Deploy Job
- Preview Deployment
- Production Deployment
- Smoke Test
- Rollback

CI Flow:

```text
Pull Request
→ Install Dependencies
→ Detect Affected Projects
→ Restore Cache
→ Run Lint / Test / Typecheck / Build
→ Upload Cache
→ Preview Deploy if Needed
```

---

### [실무]

CI 작성 기준:

- PR에서는 lint / test / typecheck / build 실행
- 변경 영향 범위 기반 실행으로 시간 단축
- Main Branch에서는 더 넓은 검증 수행 가능
- Remote Cache 사용 시 권한과 보안 검토
- Lockfile 기반 dependency cache 사용
- 앱별 Preview Deployment 구성 가능
- Production Deploy는 명시적 승인 또는 main merge 기준
- 공통 패키지 변경 시 의존 앱 검증
- Config Package 변경 시 넓은 검증
- 실패 로그를 패키지 / task 단위로 구분
- CI와 local task 명령어 일치

주의:

- CI 속도만 위해 검증을 과도하게 줄이지 않기
- Remote Cache에 민감 output 저장 금지
- Affected 계산 실패 대비 전체 검증 fallback 고려
- 배포 Job은 cache 대상이 아님
- 여러 앱 배포 순서와 의존성 확인

---

### [FAQ]

Q. Monorepo CI는 왜 복잡해지나?

A.
여러 앱과 패키지가 하나의 Repository에 있으므로 변경 영향 범위, build 순서, cache, deploy 대상을 함께 고려해야 하기 때문이다.

Q. PR에서 모든 앱을 매번 build해야 하나?

A.
작은 프로젝트는 가능하지만 규모가 커지면 affected build / affected test로 영향을 받는 대상만 실행하는 전략이 유용하다.

Q. Remote Cache를 CI에서 쓰면 좋은가?

A.
빌드 시간을 줄일 수 있지만 권한, 보안, cache poisoning, 민감 output 저장 위험을 검토해야 한다.

---

# 21. Deployment Rules

## 21.1 앱별 배포 구조

### [개념]

Deployment Rules는 Monorepo 안의 여러 앱을 독립적으로 또는 함께 배포하는 기준이다.

---

### [핵심]

필수 포함:

- App Deployment
- Independent Deployment
- Coordinated Deployment
- Preview Deployment
- Production Deployment
- Build Target
- Environment Variable
- Artifact
- Rollback
- Smoke Test
- Deployment Dependency

배포 대상 예시:

| 앱               | 배포 방식                      |
| ---------------- | ------------------------------ |
| `apps/web`       | Vercel / Node / Static Hosting |
| `apps/admin`     | Vercel / Static Hosting        |
| `apps/api`       | Container / Server             |
| `apps/docs`      | Static Hosting                 |
| `apps/storybook` | Static Hosting                 |

---

### [실무]

배포 기준:

- 앱별 배포 파이프라인 분리
- 공통 패키지 변경 시 의존 앱 재배포 필요 여부 확인
- 환경변수는 앱별로 관리
- Preview Deployment는 PR 단위 제공 가능
- Production Deployment는 승인 / main merge 기준
- 배포 artifact와 build output 일치 확인
- 배포 후 Smoke Test 수행
- 실패 시 rollback 전략 준비
- API Contract 변경 시 Frontend / Backend 배포 순서 고려

주의:

- 모든 앱을 무조건 같이 배포하지 않기
- 공통 패키지 변경 영향 앱 확인
- 앱별 환경변수 누락 주의
- 배포 순서가 중요한 API 변경은 backward compatibility 고려

---

### [FAQ]

Q. Monorepo에서는 모든 앱을 한 번에 배포해야 하나?

A.
아니다. 앱별 독립 배포가 가능하며 공통 패키지 변경 영향에 따라 필요한 앱만 배포할 수 있다.

Q. 공통 패키지를 수정하면 모든 앱을 재배포해야 하나?

A.
항상은 아니다. 해당 패키지에 의존하고 변경 영향을 받는 앱을 확인해야 한다.

Q. API 변경과 Frontend 배포 순서는 어떻게 잡아?

A.
Breaking Change가 생기지 않도록 backward compatibility를 유지하거나 Backend와 Frontend 배포 순서를 조율해야 한다.

---

# 22. Tool Selection Rules

## 22.1 Turborepo / Nx / pnpm 선택 기준

### [개념]

Monorepo Tool은 Workspace 관리, Task Orchestration, Cache, Affected 실행, Code Generation, Project Graph, CI 최적화를 지원한다.

---

### [핵심]

주요 도구:

- pnpm Workspace
- Turborepo
- Nx
- Changesets
- Lage
- Rush
- Yarn Workspace
- npm Workspace

비교 기준:

| 기준           | pnpm Workspace    | Turborepo                  | Nx                     |
| -------------- | ----------------- | -------------------------- | ---------------------- |
| 역할           | Package Workspace | Task Orchestration / Cache | Monorepo Platform      |
| 설정 복잡도    | 낮음              | 낮음~중간                  | 중간~높음              |
| Cache          | 제한적            | 강점                       | 강점                   |
| Affected       | 제한적            | 가능                       | 강점                   |
| Project Graph  | 제한적            | 제한적                     | 강점                   |
| Code Generator | 없음              | 제한적                     | 강점                   |
| 적합           | 작은 Monorepo     | JS/TS 앱 중심              | 대규모 / 복합 Monorepo |

---

### [실무]

선택 기준:

- 작은 Monorepo: pnpm Workspace만으로 시작 가능
- JS / TS 앱 중심: Turborepo 적합
- 대규모 프로젝트 / 복잡한 Dependency Graph: Nx 적합
- Affected Task와 Project Graph가 중요하면 Nx 검토
- 단순 Task Cache와 빠른 도입이 중요하면 Turborepo 검토
- Package Release가 중요하면 Changesets 검토
- 도구는 Repository 규모와 팀 운영 수준에 맞춰 선택
- 처음부터 복잡한 도구를 강제하지 않기

주의:

- 도구가 Package Boundary를 대신 지켜주지 않음
- Cache 설정이 틀리면 잘못된 결과를 재사용할 수 있음
- Nx / Turborepo 설정은 CI와 함께 설계해야 함
- 도구 변경 비용이 크므로 초기 선택 기준 문서화

---

### [FAQ]

Q. Turborepo와 Nx 중 무엇을 써야 하나?

A.
단순 JS/TS Monorepo와 빠른 도입은 Turborepo가 적합하고, 대규모 Project Graph, Affected 실행, Generator가 중요하면 Nx가 적합하다.

Q. pnpm Workspace만으로 Monorepo가 가능한가?

A.
가능하다. 작은 규모에서는 pnpm Workspace만으로 시작하고 필요해지면 Turborepo나 Nx를 추가할 수 있다.

Q. Monorepo 도구를 쓰면 구조 문제가 자동으로 해결되나?

A.
아니다. 도구는 실행과 캐시를 돕지만 Package Boundary와 의존성 규칙은 별도로 설계해야 한다.

---

# 23. Security Rules

## 23.1 Monorepo 보안 기준

### [개념]

Monorepo Security는 여러 앱과 패키지가 하나의 Repository를 공유할 때 발생하는 Secret 노출, 권한 범위, Dependency 취약점, Cache 보안, 배포 권한 문제를 관리하는 기준이다.

---

### [핵심]

필수 포함:

- Secret Management
- Environment Variable
- Dependency Security
- Package Access
- CI Secret
- Remote Cache Security
- Supply Chain Security
- Lockfile Review
- Script Security
- Publish Permission
- Deploy Permission
- Code Owner
- Branch Protection

---

### [실무]

보안 기준:

- Secret은 Repository에 커밋 금지
- 앱별 환경변수 분리
- CI Secret 접근 범위 최소화
- PR from fork의 Secret 노출 주의
- Remote Cache 권한 검토
- Cache output에 민감정보 포함 금지
- Lockfile 변경 리뷰
- Dependency 취약점 점검
- Package publish 권한 제한
- Deploy 권한 제한
- 공통 패키지 변경은 Code Owner 리뷰
- Script에서 외부 입력 실행 주의
- 내부 Package에 민감 데이터 하드코딩 금지

주의:

- 하나의 Repository라서 모든 팀이 모든 Secret에 접근해야 하는 것은 아님
- Remote Cache는 보안 정책 없이 도입하면 위험할 수 있음
- 공통 패키지 취약점은 여러 앱으로 확산됨
- CI Token 권한 과다 부여 금지

---

### [FAQ]

Q. Monorepo에서 보안상 가장 조심할 점은?

A.
Secret 노출, Remote Cache 보안, 공통 패키지 취약점 확산, CI 권한 과다 부여를 조심해야 한다.

Q. 공통 패키지 취약점은 왜 위험한가?

A.
여러 앱에서 동시에 사용되므로 하나의 취약점이 전체 제품으로 확산될 수 있다.

Q. Remote Cache에 민감정보가 들어가면 안 되는 이유는?

A.
Cache output이 팀이나 CI 환경에서 공유될 수 있어 Secret이나 개인정보가 노출될 수 있기 때문이다.

---

# 24. Governance Rules

## 24.1 운영 / Ownership 기준

### [개념]

Monorepo Governance는 앱과 패키지의 소유권, 변경 승인, 리뷰 기준, 문서화, Deprecation, Migration을 관리하는 운영 체계이다.

---

### [핵심]

필수 포함:

- Code Owner
- Package Owner
- App Owner
- Review Rule
- Contribution Rule
- Public API Change
- Breaking Change
- Deprecation
- Migration Guide
- Architecture Decision Record
- Package README
- Changelog
- Ownership Matrix

Ownership 예시:

| 대상                  | Owner              |
| --------------------- | ------------------ |
| `apps/web`            | Web Team           |
| `apps/admin`          | Admin Team         |
| `packages/ui`         | Design System Team |
| `packages/api-client` | Platform Team      |
| `packages/config`     | Architecture Team  |

---

### [실무]

운영 기준:

- 앱과 패키지별 Owner 지정
- 공통 패키지 변경은 Owner 리뷰 필수
- Public API 변경은 Breaking Change 여부 확인
- Deprecated API는 대체 경로 제공
- Package README 작성
- Architecture Decision Record 작성 권장
- 변경 영향 범위에 따라 리뷰어 지정
- 공통 Config 변경은 전체 영향 확인
- Design System 변경은 시각 / 접근성 리뷰 포함
- API Contract 변경은 Backend / Frontend 동시 리뷰

주의:

- Owner 없는 공통 패키지는 품질 저하 위험
- 공통 패키지 변경을 아무나 승인하면 전체 앱에 영향
- 문서 없는 Package는 잘못 사용될 가능성 증가
- Deprecation 없이 삭제하면 앱 빌드가 깨질 수 있음

---

### [FAQ]

Q. Monorepo에서 Ownership이 왜 필요한가?

A.
공통 패키지 변경이 여러 앱에 영향을 주므로 책임자와 리뷰 기준이 없으면 구조와 품질이 빠르게 무너질 수 있다.

Q. Package README에는 무엇을 써야 하나?

A.
패키지 목적, 공개 API, 사용 예시, 의존성, 금지 사용법, 변경 시 주의사항을 포함한다.

Q. 공통 패키지 변경은 어떻게 리뷰해야 하나?

A.
사용처 영향, Breaking Change 여부, 테스트, 문서, 배포 영향을 함께 확인해야 한다.

---

# 25. Testing Rules

## 25.1 Monorepo 테스트 전략

### [개념]

Monorepo Testing은 앱과 패키지 단위의 Unit, Component, Integration, E2E 테스트를 Dependency Graph와 CI Pipeline에 맞게 실행하는 전략이다.

---

### [핵심]

필수 포함:

- Unit Test
- Component Test
- Integration Test
- E2E Test
- Package Test
- App Test
- Affected Test
- Test Cache
- Test Sharding
- Test Fixture
- Mock Package
- Contract Test
- Visual Regression Test

테스트 대상:

| 대상                  | 테스트                                  |
| --------------------- | --------------------------------------- |
| `packages/utils`      | Unit Test                               |
| `packages/ui`         | Component / Accessibility / Visual Test |
| `packages/api-client` | Contract / Mock API Test                |
| `apps/web`            | Integration / E2E Test                  |
| `apps/admin`          | Integration / E2E Test                  |
| `packages/config`     | Smoke / Lint 적용 검증                  |

---

### [실무]

테스트 기준:

- Package는 독립 테스트 가능해야 함
- 앱은 Feature Flow 중심 테스트
- 공통 UI는 Component / Accessibility / Visual Test
- API Contract는 Backend 변경과 함께 검증
- Affected Test로 PR 시간 단축
- Main Branch에서는 전체 또는 넓은 범위 테스트 검토
- Test Fixture를 공통 패키지로 관리 가능
- 테스트 결과 cache 가능 여부 확인
- E2E는 앱별 핵심 Flow 중심
- 테스트 명령어 이름 통일

주의:

- Affected Test만 믿고 전체 회귀 테스트를 영구적으로 생략하지 않기
- 공통 패키지 변경 후 의존 앱 테스트 누락 주의
- Mock Package가 실제 API Contract와 어긋나지 않게 관리
- Visual Regression Test는 공통 UI 변경에 중요

---

### [FAQ]

Q. Monorepo에서 테스트는 어떻게 나눠야 하나?

A.
패키지는 독립 테스트, 앱은 통합 / E2E 테스트, 공통 UI는 컴포넌트 / 접근성 / 시각 회귀 테스트로 나눈다.

Q. Affected Test만 실행해도 되나?

A.
PR에서는 유용하지만 main branch나 release 전에는 더 넓은 범위 검증을 고려해야 한다.

Q. 공통 UI 패키지는 무엇을 테스트해야 하나?

A.
Component 상태, 접근성, 키보드 동작, Theme, Visual Regression을 테스트해야 한다.

---

# 26. Documentation Rules

## 26.1 Monorepo 문서화

### [개념]

Monorepo Documentation은 Repository 구조, Package 책임, 개발 명령어, 의존성 규칙, 배포 기준, 변경 절차를 팀과 Agent가 이해할 수 있게 정리하는 기준이다.

---

### [핵심]

필수 문서:

- Root README
- Package README
- Architecture Decision Record
- Contribution Guide
- Development Guide
- CI/CD Guide
- Release Guide
- Package Boundary Guide
- Troubleshooting Guide
- Migration Guide

Root README 포함 항목:

```text
- Repository 목적
- apps / packages 구조
- 개발 환경 세팅
- 주요 명령어
- 패키지 추가 기준
- 의존성 규칙
- 테스트 / 빌드 / 린트 방법
- 배포 방식
```

---

### [실무]

문서화 기준:

- Root README는 전체 구조와 실행 방법 중심
- Package README는 책임과 Public API 중심
- 새로운 Package 추가 시 README 작성
- Architecture Decision Record로 주요 결정 기록
- CI/CD 변경 시 문서 업데이트
- Release 절차 문서화
- Troubleshooting 문서 유지
- Deprecated Package는 Migration Guide 제공
- 문서와 실제 script가 어긋나지 않도록 관리

---

### [FAQ]

Q. Monorepo에서 문서화가 왜 중요한가?

A.
앱과 패키지가 많아질수록 구조와 의존성 규칙을 모르면 잘못된 import와 중복 구현이 빠르게 늘어나기 때문이다.

Q. Package README에는 무엇을 써야 하나?

A.
패키지 목적, 공개 API, 사용 예시, 의존성, 금지 사용법, 변경 시 주의사항을 포함한다.

Q. ADR은 언제 작성하나?

A.
도구 선택, 구조 변경, 패키지 분리, 배포 전략처럼 장기적인 영향을 주는 결정을 할 때 작성한다.

---

# 27. Troubleshooting Rules

## 27.1 자주 발생하는 문제

### [개념]

Troubleshooting 문서는 Agent가 Monorepo 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Dependency Conflict
- Peer Dependency Error
- Circular Dependency
- Deep Import
- Package Not Found
- Workspace Link Error
- TypeScript Path Error
- Build Order Error
- Cache Miss
- Stale Cache
- Affected Task Missing
- Lockfile Conflict
- Hoisting Issue
- Duplicate React
- Environment Variable Missing
- CI Only Failure
- Package Export Error
- Storybook Package Resolution Error
- Remote Cache Permission Error

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- 내부 패키지를 찾지 못함

원인:

- Workspace 범위에 패키지가 포함되지 않음
- package name과 import name이 다름
- dependency에 `workspace:*`가 선언되지 않음

해결:

- `pnpm-workspace.yaml` 범위 확인
- package.json의 `name` 확인
- 사용하는 패키지의 dependencies에 내부 패키지 선언
```

예시:

```md
문제:

- Duplicate React 오류 발생

원인:

- UI Package가 React를 dependency로 직접 포함함
- 앱과 패키지가 서로 다른 React 버전을 사용함

해결:

- UI Package에서 React를 peerDependency로 관리
- Root에서 React 버전 통일
- Lockfile 중복 버전 확인
```

예시:

```md
문제:

- Cache Hit인데 빌드 결과가 이상함

원인:

- Task input에 환경변수나 설정 파일이 누락됨
- output 경로가 잘못 지정됨
- 오래된 remote cache가 복원됨

해결:

- task input / output 설정 확인
- 환경변수와 lockfile을 cache input에 반영
- 필요 시 cache reset 후 재실행
```

---

### [FAQ]

Q. Monorepo에서 가장 자주 나는 오류는?

A.
내부 패키지 import 오류, dependency 선언 누락, TypeScript path 오류, cache 설정 오류, peer dependency 충돌이 자주 발생한다.

Q. Duplicate React 오류는 왜 발생하나?

A.
UI Package가 React를 dependency로 포함하거나 앱과 패키지가 서로 다른 React 버전을 사용하면 발생할 수 있다.

Q. CI에서만 실패하면 무엇을 확인해야 하나?

A.
환경변수, lockfile, Node / Package Manager 버전, cache, workspace install, affected 기준을 확인해야 한다.

---

# 28. Code Example Rules

## 28.1 코드 예제 작성 기준

### [개념]

Monorepo 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- 짧은 설정 예제 중심
- Root / App / Package 위치 명시
- `package.json` 예제 포함 가능
- `pnpm-workspace.yaml` 예제 포함 가능
- `turbo.json` 또는 `nx.json` 예제 포함 가능
- 불필요한 전체 설정 금지
- Secret 하드코딩 금지
- 긴 CI 전체 파일 금지
- 도구별 핵심 설정만 포함
- Package Boundary가 드러나게 작성

---

### [실무]

권장 예제 유형:

- 기본 Monorepo 폴더 구조
- `pnpm-workspace.yaml`
- Internal Package dependency
- `exports` 설정
- Shared Config extends
- Task Pipeline
- Affected Flow
- Package README Template
- Dependency 위치 기준
- TypeScript base config
- CI 단계 요약

금지 예제:

- 모든 의존성을 Root에 몰아넣는 예제
- 앱이 다른 앱을 직접 import하는 예제
- Deep Import를 권장하는 예제
- Secret이 포함된 CI 예제
- deploy / publish를 cache하는 예제
- `packages/utils`에 모든 로직을 넣는 예제
- UI Package가 Feature를 import하는 예제

---

### [FAQ]

Q. Monorepo 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 설정 snippet 중심으로 작성한다.

Q. CI 전체 파일을 예제로 넣어야 하나?

A.
전체 파일보다 install, affected, cache, build, test, deploy 단계 요약 예제가 더 검색과 재사용에 적합하다.

---

# 29. Comparison Rules

## 29.1 필수 비교 대상

### [개념]

Monorepo 문서는 Agent의 구조 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Monorepo vs Polyrepo
- `apps` vs `packages`
- App Package vs Library Package
- Shared Package vs Feature Code
- Internal Package vs External Package
- Turborepo vs Nx
- pnpm Workspace vs Turborepo
- Local Cache vs Remote Cache
- Build Cache vs Dependency Cache
- Full Build vs Affected Build
- Fixed Versioning vs Independent Versioning
- DTO Package vs View Model
- Type Package vs Runtime Package
- Peer Dependency vs Dependency
- Path Alias vs Package Import
- Public API Import vs Deep Import
- Package-level Test vs App-level Test
- App Deployment vs Package Publish
- Monorepo vs Micro Frontend

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 위치 / 장점 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Monorepo와 Polyrepo 중 무엇이 더 좋은가?

A.
공유 코드와 통합 변경이 많으면 Monorepo가 유리하고, 팀과 배포 경계가 완전히 다르면 Polyrepo가 단순할 수 있다.

Q. Turborepo와 Nx 중 무엇을 선택해야 하나?

A.
단순 JS/TS Monorepo는 Turborepo가 빠르게 도입하기 좋고, 대규모 그래프 분석과 Affected 실행이 중요하면 Nx가 적합하다.

Q. App Deployment와 Package Publish는 같은가?

A.
아니다. App Deployment는 실행 앱 배포이고, Package Publish는 재사용 패키지를 registry에 배포하는 작업이다.

---

# 30. Checklist Rules

## 30.1 문서 품질 체크리스트

### [개념]

Monorepo RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Monorepo 목적이 명확한가?
- [ ] `apps` / `packages` 구조를 포함했는가?
- [ ] Workspace 기준을 포함했는가?
- [ ] Package Boundary 기준을 포함했는가?
- [ ] App Package와 Shared Package 기준을 구분했는가?
- [ ] Design System Package 기준을 포함했는가?
- [ ] Shared Config Package 기준을 포함했는가?
- [ ] API Contract Package 기준을 포함했는가?
- [ ] Dependency Management 기준을 포함했는가?
- [ ] Task Pipeline 기준을 포함했는가?
- [ ] Cache 기준을 포함했는가?
- [ ] Affected Task 기준을 포함했는가?
- [ ] TypeScript Monorepo 기준을 포함했는가?
- [ ] Build Output 기준을 포함했는가?
- [ ] Versioning / Release 기준을 포함했는가?
- [ ] CI/CD 기준을 포함했는가?
- [ ] Deployment 기준을 포함했는가?
- [ ] Tool Selection 기준을 포함했는가?
- [ ] Security / Governance 기준을 포함했는가?
- [ ] Testing / Documentation 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Frontend Architecture / Design System / DevOps 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- Frontend Architecture / Design System / CI/CD 문서와 연계 가능해야 함

---

### [FAQ]

Q. Monorepo 문서 품질에서 가장 중요한 것은?

A.
Repository 구조보다 Package Boundary, Dependency Graph, Task Pipeline, Cache, CI/CD, Release 기준이 명확해야 한다.

---

# 31. Retrieval Optimization Rules

## 31.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Monorepo
- Mono Repository
- Workspace
- pnpm Workspace
- Turborepo
- Nx
- Apps
- Packages
- Shared Package
- Internal Package
- Package Boundary
- Import Boundary
- Public API
- Deep Import
- Circular Dependency
- Dependency Graph
- Task Pipeline
- Build Pipeline
- Build Cache
- Local Cache
- Remote Cache
- Affected Build
- Affected Test
- Incremental Build
- TypeScript Monorepo
- Project References
- Path Alias
- Package Export
- Peer Dependency
- Workspace Protocol
- `workspace:*`
- Design System Package
- Shared Config Package
- API Contract Package
- DTO Package
- API Client Package
- Versioning
- Changeset
- Release
- CI/CD
- Preview Deployment
- Production Deployment
- Dependency Conflict
- Duplicate React
- Lockfile Conflict
- Monorepo Governance

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Monorepo는 언제 써?
- Monorepo 폴더 구조 어떻게 잡아?
- `apps`와 `packages` 차이는?
- pnpm workspace는 어떻게 구성해?
- Turborepo와 Nx 차이는?
- Shared Package는 언제 만들어?
- Package Boundary는 어떻게 잡아?
- Deep Import는 왜 피해야 해?
- 내부 패키지를 찾지 못해
- Duplicate React 오류 왜 나?
- Monorepo에서 의존성은 어디에 설치해?
- React는 dependency야 peerDependency야?
- Task Pipeline은 어떻게 구성해?
- build가 의존 패키지 build를 먼저 실행하게 하려면?
- Cache Hit인데 결과가 이상해
- Affected Build는 뭐야?
- 공통 패키지 수정하면 어떤 앱을 build해야 해?
- Monorepo CI는 어떻게 최적화해?
- Monorepo에서 Design System은 어디에 둬?
- API 타입은 Monorepo에서 공유해도 돼?
- Monorepo release는 어떻게 해?
- Package publish와 App deploy 차이는?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 32. Version Rules

## 32.1 기준 버전

### [개념]

Monorepo 문서는 Modern JavaScript / TypeScript Monorepo 기준으로 작성하며, React / Next.js / Backend / DevOps 구조와 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern Monorepo
- JavaScript / TypeScript Monorepo
- pnpm Workspace
- Turborepo
- Nx
- React 19+
- Next.js App Router 연계 가능
- TypeScript
- Shared UI Package
- Design System Package
- Shared Config Package
- API Contract Package
- Task Pipeline
- Local Cache / Remote Cache
- Affected Task
- CI/CD Optimization
- Package Boundary
- Security-aware Monorepo

Legacy 제외:

- 단순 폴더 모음식 Repository
- Package Boundary 없는 구조
- 모든 의존성을 Root에 몰아넣는 구조
- 모든 공통 코드를 `utils`에 넣는 구조
- 앱끼리 직접 import하는 구조
- Deep Import를 권장하는 구조
- Cache 없는 대규모 전체 빌드만 고집하는 구조
- Secret을 Repository에 포함하는 구조
- 문서 없는 공통 패키지 운영

---

### [실무]

문서 작성 시 주의:

- 도구 버전별 설정이 달라질 수 있으므로 최신 공식 문서 확인 필요
- Nx / Turborepo / pnpm 설정은 프로젝트 규모와 CI 요구에 따라 선택
- Frontend Architecture의 Feature 구조와 Monorepo Package 구조를 혼동하지 않기
- Design System 문서와 UI Component 상세 설명 중복 최소화
- CI/CD 문서와 Pipeline 상세 중복 최소화
- Monorepo는 구조보다 경계와 자동화가 핵심임을 강조

---

### [FAQ]

Q. Monorepo 문서는 특정 도구 하나만 기준으로 작성해야 하나?

A.
아니다. pnpm Workspace, Turborepo, Nx의 역할과 선택 기준을 포함하되 프로젝트 상황에 맞게 선택하도록 작성한다.

Q. Monorepo와 Frontend Architecture는 어떻게 구분하나?

A.
Frontend Architecture는 앱 내부 구조이고, Monorepo는 여러 앱과 패키지를 Repository 단위로 관리하는 구조이다.

---

# 33. Common Mistakes

## 33.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Monorepo 코드 리뷰와 구조 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- Monorepo를 단순 폴더 모음으로만 구성
- Package Boundary 없이 모든 패키지가 서로 import
- 앱끼리 직접 import
- Deep Import 남용
- Public API 없이 내부 파일 직접 참조
- Shared Package를 너무 빨리 생성
- `packages/utils`가 잡동사니화
- 모든 dependency를 Root에 설치
- 사용하는 패키지의 `package.json`에 dependency 누락
- React를 UI Package dependency로 포함해 Duplicate React 발생
- Workspace Protocol 누락
- Lockfile 여러 개 생성
- npm / yarn / pnpm 혼용
- Task Pipeline `dependsOn` 누락
- Cache input / output 설정 누락
- deploy / publish task를 cache
- Affected 계산에 필요한 dependency 선언 누락
- Config Package 변경 영향 무시
- 환경변수 차이로 CI에서만 실패
- 공통 패키지 변경 후 의존 앱 테스트 누락
- Breaking Change 문서화 누락
- Package Owner 없음
- Remote Cache 보안 검토 없이 도입

---

### [실무]

리뷰 기준:

- `apps` / `packages` 역할 확인
- Workspace 범위 확인
- 내부 패키지 의존성 선언 확인
- Package Boundary 확인
- Deep Import 확인
- 순환 참조 확인
- dependency / peerDependency 위치 확인
- Task Pipeline 순서 확인
- Cache input / output 확인
- Affected Task 신뢰성 확인
- CI와 local script 일치 확인
- Config 변경 영향 확인
- Release / Changelog 확인
- Security / Secret / Remote Cache 확인

---

### [FAQ]

Q. Monorepo에서 가장 흔한 실수는?

A.
Package Boundary 없이 모든 패키지가 서로 import하고, 의존성 선언 없이 Hoisting에 기대는 것이다.

Q. `packages/utils`가 커지면 왜 문제인가?

A.
책임이 불명확한 코드가 모이고 패키지 간 의존성이 흐려져 구조가 무너질 수 있다.

Q. Root에 모든 dependency를 설치하면 왜 문제인가?

A.
각 패키지가 실제 의존성을 선언하지 않아 다른 환경이나 CI에서 빌드가 깨질 수 있다.

---

# 34. Final Goal

## 34.1 최종 목표

### [개념]

Monorepo RAG 문서는 Agent가 여러 앱과 패키지가 포함된 Repository를 설계, 생성, 검토, 최적화, 운영할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Monorepo 구조 설계
- `apps` / `packages` 경계 설계
- Workspace 설정 작성
- Package Boundary 검토
- Shared Package 승격 판단
- Design System Package 설계
- Shared Config Package 설계
- API Contract Package 설계
- Dependency Management 리뷰
- Peer Dependency 판단
- Duplicate React 원인 진단
- Task Pipeline 설계
- Cache 전략 설계
- Affected Build / Affected Test 전략 제안
- TypeScript Monorepo 설정 검토
- Build Output 설정 검토
- CI/CD Pipeline 구조 제안
- App Deployment 영향 분석
- Versioning / Release 전략 제안
- Security / Remote Cache 위험 검토
- Governance / Ownership 기준 작성
- Monorepo Troubleshooting
- Monorepo Architecture 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 설정 예제는 짧고 안전하게 작성
- Repository / Workspace / Package / Task / CI 경계 명확화
- Cache / Affected / Release / Security 기준 포함
- Frontend Architecture / Design System / CI-CD 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Monorepo Domain Rules의 최종 목적은?

A.
Agent가 여러 앱과 패키지가 포함된 Repository에서 구조, 패키지 경계, 의존성, 빌드, 캐시, CI/CD, 배포, 릴리즈, 보안을 설계하고 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Monorepo 문서는 어떤 기준으로 작성해야 해?

A.
Repository Structure, Workspace, Package Boundary, Dependency Management, Task Pipeline, Cache, Affected Task, CI/CD, Release, Security 중심으로 작성해야 한다.

Q. Monorepo는 언제 써?

A.
여러 앱이 공통 UI, 타입, 유틸, API Client, 설정을 공유하고 변경을 하나의 PR에서 함께 관리해야 할 때 적합하다.

Q. Monorepo가 항상 좋은가?

A.
아니다. 공유 코드가 거의 없거나 팀 / 배포 / 권한 경계가 완전히 다르면 Polyrepo가 더 단순할 수 있다.

Q. Monorepo 폴더 구조 어떻게 잡아?

A.
보통 `apps`에는 실행 앱, `packages`에는 공유 라이브러리, `tools`에는 자동화 스크립트, Root에는 공통 설정을 둔다.

Q. `apps`와 `packages` 차이는?

A.
`apps`는 실행 / 배포되는 애플리케이션이고, `packages`는 여러 앱에서 재사용되는 내부 라이브러리이다.

Q. App Package에는 무엇을 넣어?

A.
라우팅, 페이지 조립, 앱 전용 기능, 앱 전용 설정, 배포 설정을 넣는다.

Q. Shared Package에는 무엇을 넣어?

A.
여러 앱에서 반복 사용되고 책임이 명확하며 비즈니스 결합도가 낮은 UI, 타입, 유틸, API Client, 설정을 넣는다.

Q. 모든 공통 코드를 Package로 빼야 해?

A.
아니다. 실제로 여러 앱에서 반복 사용되고 경계가 명확한 코드만 패키지로 분리한다.

Q. Shared Package는 언제 만들어?

A.
두 개 이상 앱이나 패키지에서 반복 사용되고 독립 테스트와 문서화가 가능할 때 만든다.

Q. `packages/utils`는 어떻게 관리해?

A.
잡동사니가 되지 않도록 날짜, 문자열, 검증, 포맷터처럼 목적별로 나누고 도메인 로직은 별도 패키지로 분리한다.

Q. Workspace는 왜 필요해?

A.
Monorepo 안의 여러 앱과 패키지를 하나의 의존성 그래프로 연결하고 내부 패키지 참조를 관리하기 위해 필요하다.

Q. pnpm workspace는 어떻게 구성해?

A.
Root에 `pnpm-workspace.yaml`을 두고 `apps/*`, `packages/*` 같은 workspace 범위를 지정한다.

Q. `workspace:*`는 무엇이야?

A.
외부 registry가 아니라 같은 Workspace 안의 내부 패키지를 참조한다는 의미이다.

Q. 내부 패키지를 찾지 못해. 무엇을 확인해?

A.
`pnpm-workspace.yaml` 범위, package name, dependency의 `workspace:*` 선언, install 상태를 확인한다.

Q. Package Boundary는 어떻게 잡아?

A.
패키지마다 하나의 명확한 책임을 주고 Public API만 외부에 노출하며 의존성 방향과 금지 import를 정한다.

Q. Package Boundary가 왜 중요해?

A.
패키지 간 결합도를 낮추고 변경 영향 범위와 빌드 / 테스트 대상을 예측 가능하게 만들기 위해 중요하다.

Q. Deep Import는 왜 피해야 해?

A.
패키지 내부 구현에 직접 의존하면 리팩토링이 어려워지고 Public API가 무력화되기 때문이다.

Q. Public API는 어떻게 관리해?

A.
`index.ts` 또는 `package.json`의 `exports`를 통해 외부에 노출할 API만 제한한다.

Q. 앱끼리 직접 import해도 돼?

A.
권장하지 않는다. 공유가 필요하면 별도 Package로 분리해야 한다.

Q. 순환 의존성은 어떻게 해결해?

A.
공통 타입이나 유틸을 하위 Shared Package로 분리하거나 패키지 책임을 재설계한다.

Q. Monorepo에서 Design System은 어디에 둬?

A.
보통 `packages/ui` 또는 `packages/design-system`에 둔다.

Q. UI Package 전체를 Client Component로 만들어도 돼?

A.
권장하지 않는다. 상호작용이 필요한 컴포넌트만 Client Boundary를 갖도록 분리하는 것이 좋다.

Q. Shared Config Package는 왜 필요해?

A.
여러 앱과 패키지에서 TypeScript, ESLint, Prettier 설정을 일관되게 유지하고 중복을 줄이기 위해 필요하다.

Q. API 타입은 Monorepo에서 공유해도 돼?

A.
가능하다. 단, Backend 내부 Entity가 아니라 API Request / Response Contract를 공유해야 한다.

Q. DTO와 View Model은 같은가?

A.
아니다. DTO는 API 계약이고 View Model은 화면 표시를 위한 프론트엔드 구조이다.

Q. Monorepo에서 의존성은 어디에 설치해?

A.
실제로 사용하는 앱이나 패키지의 `package.json`에 명시하고, 공통 개발 도구는 Root에 둔다.

Q. Root에 모든 dependency를 설치하면 안 돼?

A.
권장하지 않는다. 각 패키지가 실제 의존성을 선언하지 않으면 CI나 다른 환경에서 빌드가 깨질 수 있다.

Q. React는 dependency야 peerDependency야?

A.
UI Library처럼 React를 사용하는 앱이 제공해야 하는 경우 peerDependency로 관리하는 것이 일반적이다.

Q. Duplicate React 오류 왜 나?

A.
UI Package가 React를 dependency로 직접 포함하거나 앱과 패키지가 서로 다른 React 버전을 사용하면 발생할 수 있다.

Q. Lockfile은 어디에 둬?

A.
Monorepo Root에 하나로 관리하는 것이 일반적이다.

Q. npm, yarn, pnpm을 섞어 써도 돼?

A.
권장하지 않는다. Package Manager는 팀 전체에서 하나로 통일해야 한다.

Q. Task Pipeline은 어떻게 구성해?

A.
build, test, lint, typecheck task를 패키지 의존성 순서와 cache 가능 여부에 맞게 구성한다.

Q. build가 의존 패키지 build를 먼저 실행하게 하려면?

A.
Task Pipeline에서 현재 package build가 dependency package build에 의존하도록 설정한다.

Q. 어떤 task를 cache하면 좋아?

A.
build, test, lint, typecheck처럼 입력이 같으면 결과가 같은 작업은 cache에 적합하다.

Q. 어떤 task를 cache하면 안 돼?

A.
deploy, publish, DB migration, dev server처럼 외부 상태를 변경하거나 지속 실행되는 작업은 일반적으로 cache하지 않는다.

Q. Cache Hit인데 결과가 이상해. 무엇을 확인해?

A.
Task input, output, 환경변수, lockfile, dependency graph 설정을 확인해야 한다.

Q. Cache Miss가 너무 많으면?

A.
Input 범위가 너무 넓거나 lockfile / 환경변수 / 설정 파일이 자주 바뀌는지 확인한다.

Q. Remote Cache를 써도 돼?

A.
빌드 시간을 줄일 수 있지만 권한, 보안, cache poisoning, 민감 output 저장 위험을 검토해야 한다.

Q. Affected Build는 뭐야?

A.
변경된 코드와 Dependency Graph를 기준으로 영향을 받는 앱과 패키지만 build하는 방식이다.

Q. 공통 패키지 수정하면 어떤 앱을 build해야 해?

A.
해당 공통 패키지에 의존하는 앱과 패키지를 affected 대상으로 build해야 한다.

Q. Affected 실행이 틀릴 수 있어?

A.
그렇다. Dependency 선언 누락, Deep Import, 잘못된 Path Alias, Config input 누락이 있으면 영향을 잘못 계산할 수 있다.

Q. Monorepo에서 tsconfig는 어떻게 관리해?

A.
Root에 base config를 두고 앱과 패키지가 이를 extends해서 각 환경에 맞게 설정한다.

Q. TypeScript Project References는 언제 필요해?

A.
패키지가 많고 typecheck / build 속도와 의존성 순서 관리가 중요해질 때 유용하다.

Q. Path Alias만 쓰면 Monorepo Package가 필요 없어?

A.
아니다. Path Alias는 import 편의 기능이고 Package Boundary와 dependency 선언을 대체하지 않는다.

Q. Build Output은 왜 중요해?

A.
배포와 Cache Restore가 build output에 의존하기 때문에 output 경로가 정확해야 한다.

Q. Library Package는 꼭 build해야 해?

A.
프로젝트 설정에 따라 다르다. source를 직접 참조할 수도 있고 `dist`로 빌드해 소비할 수도 있다.

Q. Monorepo release는 어떻게 해?

A.
내부 앱만 있으면 App Deployment 중심으로 관리하고, 외부 배포 패키지가 있으면 Semantic Versioning과 Changeset을 검토한다.

Q. 모든 패키지가 같은 버전을 가져야 해?

A.
아니다. 강하게 결합된 패키지는 Fixed Versioning, 독립 배포 패키지는 Independent Versioning을 사용할 수 있다.

Q. 내부 패키지도 NPM에 publish해야 해?

A.
반드시 그럴 필요는 없다. 같은 Workspace 내부에서만 사용한다면 publish 없이 관리할 수 있다.

Q. Package publish와 App deploy 차이는?

A.
Package publish는 재사용 라이브러리를 registry에 배포하는 것이고, App deploy는 실행 애플리케이션을 운영 환경에 배포하는 것이다.

Q. Monorepo CI는 어떻게 최적화해?

A.
Affected Task, Remote Cache, 병렬 실행, Lockfile Cache, 앱별 Preview Deployment를 조합해 최적화한다.

Q. PR에서 모든 앱을 매번 build해야 해?

A.
작은 프로젝트는 가능하지만 규모가 커지면 affected build / affected test로 영향을 받는 대상만 실행하는 전략이 유용하다.

Q. 모든 앱을 한 번에 배포해야 해?

A.
아니다. 앱별 독립 배포가 가능하며 공통 패키지 변경 영향에 따라 필요한 앱만 배포할 수 있다.

Q. API 변경과 Frontend 배포 순서는 어떻게 잡아?

A.
Breaking Change가 생기지 않도록 backward compatibility를 유지하거나 Backend와 Frontend 배포 순서를 조율해야 한다.

Q. Turborepo와 Nx 차이는?

A.
Turborepo는 단순 JS/TS Monorepo의 Task Orchestration과 Cache에 적합하고, Nx는 Project Graph, Affected 실행, Generator가 중요한 대규모 Monorepo에 적합하다.

Q. pnpm Workspace만으로 Monorepo가 가능해?

A.
가능하다. 작은 규모에서는 pnpm Workspace만으로 시작하고 필요해지면 Turborepo나 Nx를 추가할 수 있다.

Q. Monorepo 도구를 쓰면 구조 문제가 자동으로 해결돼?

A.
아니다. 도구는 실행과 cache를 돕지만 Package Boundary와 의존성 규칙은 별도로 설계해야 한다.

Q. Monorepo 보안에서 가장 조심할 점은?

A.
Secret 노출, Remote Cache 보안, 공통 패키지 취약점 확산, CI 권한 과다 부여를 조심해야 한다.

Q. Remote Cache에 민감정보가 들어가면 안 되는 이유는?

A.
Cache output이 팀이나 CI 환경에서 공유될 수 있어 Secret이나 개인정보가 노출될 수 있기 때문이다.

Q. Monorepo에서 Ownership이 왜 필요해?

A.
공통 패키지 변경이 여러 앱에 영향을 주므로 책임자와 리뷰 기준이 없으면 구조와 품질이 빠르게 무너질 수 있다.

Q. Package README에는 무엇을 써야 해?

A.
패키지 목적, 공개 API, 사용 예시, 의존성, 금지 사용법, 변경 시 주의사항을 포함한다.

Q. Monorepo에서 테스트는 어떻게 나눠?

A.
패키지는 독립 테스트, 앱은 통합 / E2E 테스트, 공통 UI는 컴포넌트 / 접근성 / 시각 회귀 테스트로 나눈다.

Q. Affected Test만 실행해도 돼?

A.
PR에서는 유용하지만 main branch나 release 전에는 더 넓은 범위 검증을 고려해야 한다.

Q. Monorepo에서 문서화가 왜 중요해?

A.
앱과 패키지가 많아질수록 구조와 의존성 규칙을 모르면 잘못된 import와 중복 구현이 빠르게 늘어나기 때문이다.

Q. CI에서만 실패하면 무엇을 확인해?

A.
환경변수, lockfile, Node / Package Manager 버전, cache, workspace install, affected 기준을 확인해야 한다.

Q. Monorepo 코드 리뷰에서 가장 중요한 것은?

A.
Package Boundary, dependency 선언, deep import, task pipeline, cache 설정, affected 정확성, CI/CD 영향, 보안 위험을 확인하는 것이다.

Q. Monorepo RAG 문서 최종 목표는?

A.
Agent가 여러 앱과 패키지가 포함된 Repository에서 구조, 패키지 경계, 의존성, 빌드, 캐시, CI/CD, 배포, 릴리즈, 보안을 설계하고 리뷰하게 만드는 것이다.
