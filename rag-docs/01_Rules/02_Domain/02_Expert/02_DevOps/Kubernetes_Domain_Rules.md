# Kubernetes Domain Rules

---

# 1. Domain Purpose

Kubernetes Domain 문서는 DevOps Agent / Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Container Orchestration Support
- Production Deployment Automation
- High Availability Support
- Scaling Support
- Kubernetes Troubleshooting

우선순위:

1. Kubernetes Core
2. Pod / Deployment / Service
3. Scaling / Rolling Update
4. Troubleshooting

---

# 2. Scope

포함 범위:

- Kubernetes Core
- Cluster
- Node
- Control Plane
- Worker Node
- Pod
- ReplicaSet
- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- Volume
- PVC
- Namespace
- HPA
- Rolling Update
- Health Check
- Logs
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

# 4. Kubernetes Core Rules

Kubernetes 문서는 Container Orchestration 중심으로 작성.

핵심 구조:

- Cluster
- Control Plane
- Worker Node
- Pod
- Service

---

반드시 설명 포함:

- Kubernetes 역할
- 왜 필요한가
- Docker와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Container
→ Pod
→ Deployment
→ Service
→ Ingress
```

---

# 5. Cluster Rules

필수 포함:

- Cluster
- Control Plane
- Worker Node

---

반드시 설명:

- Cluster 구조
- Node 구성

---

예:

```text
Cluster
├─ Control Plane
└─ Worker Nodes
```

---

# 6. Node Rules

필수 포함:

- Node
- Worker Node
- Kubelet
- Container Runtime

---

반드시 설명:

- Pod 실행 위치
- Node 역할

---

# 7. Pod Rules

매우 중요.

필수 포함:

- Pod
- Container Group
- Smallest Deploy Unit

---

예:

```yaml
apiVersion: v1
kind: Pod
```

---

반드시 설명:

- Pod란
- 왜 Container 직접 배포하지 않는가

---

중요:

Kubernetes 문서 품질은 Pod 설명 품질이 결정.

---

# 8. ReplicaSet Rules

필수 포함:

- ReplicaSet
- Desired State
- Self Healing

---

반드시 설명:

- Pod 개수 유지
- 장애 복구

---

# 9. Deployment Rules

매우 중요.

필수 포함:

- Deployment
- Rolling Update
- Rollback

---

예:

```yaml
apiVersion: apps/v1
kind: Deployment
```

---

반드시 설명:

- 운영 배포 핵심 객체
- Deployment vs Pod 차이

---

# 10. Service Rules

매우 중요.

필수 포함:

- ClusterIP
- NodePort
- LoadBalancer

---

반드시 설명:

- Pod IP 변경 문제 해결
- Stable Endpoint 제공

---

예:

```yaml
kind: Service
```

---

# 11. Ingress Rules

필수 포함:

- Ingress
- HTTP Routing
- Reverse Proxy

---

반드시 설명:

- External Traffic Routing
- Domain 기반 라우팅

---

예:

```text
Client
→ Ingress
→ Service
→ Pod
```

---

# 12. Namespace Rules

필수 포함:

- Namespace
- Resource Isolation

---

반드시 설명:

- 환경 분리
- 팀 분리

---

예:

```text
dev
staging
prod
```

---

# 13. ConfigMap Rules

필수 포함:

- ConfigMap
- Configuration Injection

---

반드시 설명:

- 환경 설정 분리
- Application Config 관리

---

# 14. Secret Rules

매우 중요.

필수 포함:

- Secret
- Sensitive Data

---

반드시 설명:

- Password
- Token
- API Key 관리

---

중요:

Secret 평문 하드코딩 금지.

---

# 15. Volume Rules

필수 포함:

- Volume
- Persistent Storage

---

반드시 설명:

- Container 재시작 시 데이터 보존

---

# 16. PVC Rules

필수 포함:

- PersistentVolume
- PersistentVolumeClaim

---

반드시 설명:

- Storage 요청
- Persistent Storage 연결

---

# 17. Health Check Rules

매우 중요.

필수 포함:

- Liveness Probe
- Readiness Probe

---

예:

```yaml
livenessProbe:
readinessProbe:
```

---

반드시 설명:

- Restart 판단
- Traffic Routing 판단

---

# 18. Scaling Rules

필수 포함:

- Manual Scaling
- HPA

---

반드시 설명:

- Auto Scaling
- CPU / Memory 기반 Scaling

---

# 19. Rolling Update Rules

매우 중요.

필수 포함:

- Rolling Update
- Zero Downtime
- Rollback

---

Flow:

```text
Old Pods
→ New Pods
→ Health Check
→ Replace
```

---

# 20. Logs Rules

필수 포함:

- kubectl logs
- Container Logs

---

예:

```bash
kubectl logs pod-name
```

---

# 21. Troubleshooting Rules

반드시 포함 추천.

예:

- Pod CrashLoopBackOff
- ImagePullBackOff
- Pending Pod
- OOMKilled
- Service Unreachable
- Ingress Issue

---

형식:

문제:

원인:

해결:

---

# 22. Performance Rules

필수 포함:

- Resource Request
- Resource Limit
- CPU
- Memory

---

반드시 설명:

- Resource Allocation
- Performance Tuning

---

# 23. Retrieval Optimization Rules

강조 대상:

- Kubernetes
- Pod
- Deployment
- Service
- Ingress
- HPA
- Rolling Update
- Probe

키워드 반복 허용.

---

# 24. Version Rules

기준:

- Kubernetes 1.30+
- Docker / Container Runtime
- Spring Boot 3.x
- Java 21
- Ubuntu 24/26 LTS

---

Legacy 제외.

---

# 25. Common Mistakes

자주 발생:

- Pod 직접 운영
- Resource Limit 미설정
- Probe 누락
- Secret 평문 저장
- Namespace 미분리
- Rolling Update 미설정
- Logs 미확인
- Storage 미설계

---

# 26. Final Goal

Kubernetes RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Kubernetes Pattern
- Design Cluster Deployment
- Deploy Applications
- Configure Scaling
- Solve Kubernetes Issues
- Troubleshoot Production Problems

문서 품질이 DevOps Agent 품질을 결정한다.
