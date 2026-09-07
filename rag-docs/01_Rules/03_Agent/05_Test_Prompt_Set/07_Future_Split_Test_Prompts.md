# 07. Future Split 테스트 프롬프트

## SPLIT-01. DevOps 분리 후보 테스트

### 테스트 프롬프트

```text
배포 자동화, Docker 이미지 빌드, 서버 환경 설정, CI/CD 파이프라인까지 포함해서 운영 구조를 설계해줘.
현재 Agent 구조에서 어떤 Agent가 담당하고, 나중에 어떤 Agent로 분리하는 게 좋을지도 알려줘.
```

### 기대 Workflow

```text
PM → Backend 또는 Review → Future Split Candidate
```

### 기대 동작

- 현재는 Backend/Review가 임시 검토 가능하다고 판단해야 함
- DevOps Agent 분리 후보를 제시해야 함
- Expert RAG 필요성을 언급해야 함

### 검증 체크리스트

```text
[ ] 현재 담당 Agent와 한계를 구분했는가?
[ ] DevOps Agent 분리 필요성을 제시했는가?
[ ] 필요한 Expert RAG 후보를 제안했는가?
```

---

## SPLIT-02. Test Agent 분리 후보 테스트

### 테스트 프롬프트

```text
전체 프로젝트의 테스트 전략, 단위 테스트, 통합 테스트, E2E 테스트 기준을 정리해줘.
현재 Review Agent 안에서 처리할지, Test Agent를 분리할지도 판단해줘.
```

### 기대 Workflow

```text
PM → Review → Future Split Candidate
```

### 기대 동작

- 초기에는 Review Agent가 테스트 관점 검토를 담당할 수 있다고 판단해야 함
- 테스트 전략이 반복적으로 필요하면 Test Agent 분리 후보로 제시해야 함

### 검증 체크리스트

```text
[ ] Review Agent의 임시 담당 범위를 설명했는가?
[ ] Test Agent 분리 기준을 제시했는가?
[ ] Testing Expert RAG 필요성을 언급했는가?
```

---

## SPLIT-03. Security Agent 분리 후보 테스트

### 테스트 프롬프트

```text
인증, 인가, 비밀번호 저장, 민감정보 노출, API 접근 제어를 전문적으로 검토하는 Agent가 필요한지 판단해줘.
```

### 기대 Workflow

```text
PM → Review → Future Split Candidate
```

### 기대 동작

- 현재는 Backend/Review가 기본 보안 검토를 담당할 수 있다고 판단해야 함
- 고급 보안 검토는 Security Agent 분리 후보로 제시해야 함

### 검증 체크리스트

```text
[ ] 기본 보안과 고급 보안 범위를 구분했는가?
[ ] Security Agent 분리 기준을 제시했는가?
[ ] Security Expert RAG 필요성을 언급했는가?
```
