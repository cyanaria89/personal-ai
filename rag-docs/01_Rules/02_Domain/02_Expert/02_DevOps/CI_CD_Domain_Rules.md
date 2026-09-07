# CI/CD Domain Rules

---

# 1. Domain Purpose

CI/CD Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Build Automation Support
- Test Automation Support
- Deployment Automation Support
- Release Strategy Support
- CI/CD Troubleshooting

우선순위:

1. CI/CD Core
2. Pipeline
3. Deployment Strategy
4. Troubleshooting

---

# 2. Scope

포함 범위:

- CI/CD Core
- Pipeline
- Build
- Test Automation
- Artifact
- Deployment
- GitHub Actions
- Jenkins
- Docker Build
- Registry
- Environment
- Secrets
- Blue-Green Deployment
- Canary Deployment
- Rolling Deployment
- Rollback
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

# 4. CI/CD Core Rules

CI/CD 문서는 Software Delivery Automation 중심으로 작성.

핵심 구조:

- Source Code
- Build
- Test
- Artifact
- Deploy

---

반드시 설명 포함:

- CI/CD 역할
- 왜 사용하는가
- 수동 배포와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Code Push
→ Build
→ Test
→ Deploy
→ Production
```

---

# 5. CI Rules

매우 중요.

필수 포함:

- Continuous Integration
- Build
- Test

---

반드시 설명:

- 코드 통합 자동화
- 품질 검증

---

중요:

CI/CD 문서 품질은 CI 설명 품질이 결정.

---

# 6. CD Rules

매우 중요.

필수 포함:

- Continuous Delivery
- Continuous Deployment

---

반드시 설명:

- Delivery vs Deployment 차이
- 배포 자동화

---

# 7. Pipeline Rules

매우 중요.

필수 포함:

- Pipeline
- Workflow
- Stage

---

예:

```text
Build
→ Test
→ Package
→ Deploy
```

---

반드시 설명:

- 단계별 자동화 흐름

---

# 8. Build Rules

필수 포함:

- Compile
- Package
- Artifact

---

예:

```bash
./gradlew build
```

---

반드시 설명:

- Build 과정
- Artifact 생성

---

# 9. Test Rules

필수 포함:

- Unit Test
- Integration Test
- Automated Test

---

반드시 설명:

- 품질 보증
- 배포 전 검증

---

# 10. Artifact Rules

필수 포함:

- Jar
- Docker Image
- Build Output

---

반드시 설명:

- 배포 대상 산출물

---

# 11. GitHub Actions Rules

매우 중요.

필수 포함:

- Workflow
- Job
- Step

---

예:

```yaml
name: CI Pipeline
```

---

반드시 설명:

- GitHub 기반 자동화

---

# 12. Jenkins Rules

필수 포함:

- Jenkins
- Pipeline

---

반드시 설명:

- On-prem CI/CD
- Enterprise 활용

---

# 13. Docker Build Rules

필수 포함:

- Docker Build
- Container Artifact

---

반드시 설명:

- Container 기반 배포

---

# 14. Registry Rules

필수 포함:

- Docker Hub
- ECR
- Artifact Registry

---

반드시 설명:

- Artifact 저장소

---

# 15. Secrets Rules

매우 중요.

필수 포함:

- Secret
- Environment Variable

---

반드시 설명:

- Credential 관리
- 보안

---

주의:

Secret Hardcoding 금지.

---

# 16. Deployment Rules

매우 중요.

필수 포함:

- Deployment
- Release

---

반드시 설명:

- Production 반영 과정

---

# 17. Blue-Green Rules

필수 포함:

- Blue
- Green
- Switch Traffic

---

Flow:

```text
Blue Running
→ Green Deploy
→ Switch
```

---

반드시 설명:

- Zero Downtime

---

# 18. Canary Rules

필수 포함:

- Canary Deployment
- Gradual Release

---

반드시 설명:

- 일부 트래픽 대상 배포

---

# 19. Rolling Deployment Rules

필수 포함:

- Rolling Update
- Incremental Replace

---

반드시 설명:

- 점진적 배포

---

# 20. Rollback Rules

매우 중요.

필수 포함:

- Rollback
- Recovery

---

반드시 설명:

- 장애 시 복구

---

# 21. Monitoring Rules

필수 포함:

- Health Check
- Error Rate
- Latency

---

반드시 설명:

- 배포 후 검증

---

# 22. Troubleshooting Rules

반드시 포함 추천.

예:

- Build Failed
- Test Failed
- Deploy Failed
- Rollback Failed
- Secret Missing
- Pipeline Timeout

---

형식:

문제:

원인:

해결:

---

# 23. Retrieval Optimization Rules

강조 대상:

- CI/CD
- Pipeline
- Build
- Deploy
- GitHub Actions
- Jenkins
- Rollback
- Blue Green

키워드 반복 허용.

---

# 24. Version Rules

기준:

- GitHub Actions
- Jenkins
- Docker
- Kubernetes
- Modern DevOps Pipeline

---

Legacy 제외.

---

# 25. Common Mistakes

자주 발생:

- Manual Deploy 의존
- Test 누락
- Secret Hardcoding
- Rollback 미준비
- Monitoring 미연동
- Pipeline 복잡도 과다

---

# 26. Final Goal

CI/CD RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve CI/CD Workflow
- Design Deployment Pipeline
- Automate Build/Test/Deploy
- Solve Pipeline Problems
- Troubleshoot Deployment Issues

문서 품질이 Release Automation 품질을 결정한다.
