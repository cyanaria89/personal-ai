# Redis Part 05 - Advanced

---

# 1. Redis Advanced Core

## 1.1 Advanced Redis Overview

### [개념]

Redis Advanced는 고가용성, 분산 처리, 성능 최적화, 장애 대응과 관련된 실무 심화 영역이다.

주요 목적:

- High Availability
- Scalability
- Distributed Coordination
- Performance Optimization

---

### [핵심]

핵심 영역:

- Distributed Lock
- Replication
- Sentinel
- Cluster
- Performance Tuning
- Troubleshooting

---

### [실무]

2026 실무 기준 Redis Advanced는 대규모 서비스에서 필수다.

대표 사용처:

- Multi Server Coordination
- High Traffic Cache
- Distributed Lock
- Failover

---

### [FAQ]

Q. Redis Advanced란?
A. 고가용성, 분산 처리, 성능 최적화 관련 Redis 심화 영역이다.

---

# 2. Distributed Lock

## 2.1 Lock Overview

### [개념]

Distributed Lock은 여러 서버가 동일 자원에 동시에 접근하지 못하도록 제어한다.

---

### [핵심]

주요 목적:

- Race Condition 방지
- Concurrent Update 방지
- Resource Coordination

---

### [Flow]

```text
Server A Lock Acquire
→ Critical Section
→ Lock Release
```

---

### [FAQ]

Q. Distributed Lock이 필요한 이유는?
A. 분산 환경에서 동시성 문제를 방지하기 위해서다.

---

## 2.2 Lock Acquire

### [예제]

```text
SET lock:order:1001 unique-value NX EX 10
```

---

### [핵심]

의미:

- lock:order:1001 → Lock Key
- unique-value → Lock Owner 식별값
- NX → Key 없을 때만 생성
- EX → Lock TTL

---

### [FAQ]

Q. Redis Lock 구현 핵심 명령어는?
A. SET with NX EX 옵션이다.

---

## 2.3 Safe Unlock

### [개념]

Unlock 시 단순 DEL은 위험하다.

Lock Owner 검증 후 삭제해야 한다.

---

### [Flow]

```text
Acquire Lock
→ Save Unique Value
→ Compare Value
→ Unlock
```

---

### [주의]

위험한 방식:

```text
DEL lock:order:1001
```

문제:

- 다른 서버 Lock 삭제 가능
- Race Condition 발생

---

### [Best Practice]

권장:

- Unique Value 저장
- Lua Script 기반 Unlock
- Redisson 사용

---

### [FAQ]

Q. 단순 DEL로 Unlock하면 왜 위험한가?
A. 다른 서버가 획득한 Lock까지 삭제할 수 있기 때문이다.

---

# 3. Replication

## 3.1 Master Replica

### [개념]

Replication은 Master 데이터를 Replica가 복제하는 구조다.

---

### [Flow]

```text
Master
→ Replica 1
→ Replica 2
```

---

### [핵심]

장점:

- Read Scaling
- High Availability

---

### [FAQ]

Q. Replication 목적은?
A. Read 확장과 고가용성 확보.

---

# 4. Sentinel

## 4.1 Failover Management

### [개념]

Sentinel은 Redis Failover를 자동 관리한다.

---

### [핵심]

역할:

- Health Check
- Failure Detection
- Failover
- Notification

---

### [Flow]

```text
Master Down
→ Sentinel Detect
→ Replica Promote
```

---

### [FAQ]

Q. Sentinel 역할은?
A. Redis 장애 감지 및 자동 Failover 관리.

---

# 5. Cluster

## 5.1 Cluster Overview

### [개념]

Redis Cluster는 Sharding 기반 수평 확장 구조다.

---

### [핵심]

핵심 기능:

- Sharding
- Scalability
- High Availability

---

### [FAQ]

Q. Redis Cluster 목적은?
A. 수평 확장과 대용량 처리다.

---

## 5.2 Hash Slot

### [개념]

Redis Cluster는 Hash Slot 기반으로 데이터를 분산 저장한다.

---

### [핵심]

총 Slot 수:

```text
16384 Slots
```

---

### [FAQ]

Q. Hash Slot이란?
A. Redis Cluster 데이터 분산 단위다.

---

# 6. Performance Tuning

## 6.1 Optimization

### [개념]

Redis 성능 최적화 전략.

---

### [핵심]

주요 포인트:

- Key Size 관리
- Pipeline 활용
- Memory Monitoring
- Hot Key 대응

---

### [FAQ]

Q. Redis 성능 최적화 핵심은?
A. Memory, Key Size, Hot Key 관리다.

---

# 7. Pipeline

## 7.1 Batch Processing

### [개념]

Pipeline은 여러 명령어를 Batch 처리한다.

---

### [핵심]

장점:

- Network Overhead 감소
- Throughput 향상

---

### [FAQ]

Q. Pipeline 목적은?
A. 다수 명령 처리 성능 향상.

---

# 8. Memory Optimization

## 8.1 Memory Management

### [개념]

Redis는 Memory 관리가 핵심이다.

---

### [핵심]

확인 대상:

- Memory Usage
- Eviction
- Fragmentation

---

### [FAQ]

Q. Redis에서 Memory 관리가 중요한 이유는?
A. 모든 데이터가 Memory에 있기 때문이다.

---

# 9. Hot Key

## 9.1 Hot Key Problem

### [개념]

특정 Key에 요청이 과도하게 집중되는 문제.

---

### [핵심]

문제:

- CPU Spike
- Latency Increase
- Bottleneck

해결:

- Sharding
- Local Cache
- Replication

---

### [FAQ]

Q. Hot Key 해결 방법은?
A. Sharding, Local Cache, Replication.

---

# 10. Troubleshooting

## 10.1 Common Issues

### [Troubleshooting]

문제:

High Memory Usage

원인:

TTL 누락

해결:

Expiration 적용

---

문제:

Slow Response

원인:

Hot Key

해결:

Sharding 검토

---

문제:

Lock Failure

원인:

TTL 문제

해결:

Lock Timeout 조정

---

문제:

Unexpected Unlock

원인:

Unsafe DEL

해결:

Value 검증 후 Unlock

---

# 11. Redis Advanced Rules

## 11.1 Best Practice

### [Best Practice]

권장:

- Lock TTL 설정
- Safe Unlock 적용
- Sentinel 활용
- Cluster 고려
- Memory 모니터링

---

### [주의]

금지:

- TTL 없는 Lock
- 단순 DEL Unlock
- Single Point Failure 방치
- Hot Key 무시

---

### [Checklist]

- Lock TTL 설정
- Safe Unlock 적용
- Failover 구성
- Cluster 필요 여부
- Hot Key 대응

---

# 12. Agent Decision Rules

## 12.1 Redis Routing

### [Flow]

```text
Concurrent Access Control
→ Distributed Lock

High Availability
→ Sentinel

Horizontal Scaling
→ Cluster
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Distributed Lock을 사용하는가?
A. 분산 환경 동시성 제어가 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Distributed Lock이란?
A. 분산 환경에서 동시성 제어를 위한 Lock이다.

Q. Sentinel 역할은?
A. 장애 감지 및 Failover 관리.

Q. Redis Cluster 목적은?
A. 수평 확장과 대용량 처리.

Q. Hot Key란?
A. 특정 Key에 트래픽이 집중되는 현상.

Q. 왜 DEL Unlock이 위험한가?
A. 다른 서버가 획득한 Lock까지 삭제할 수 있기 때문이다.

Q. 언제 Cluster를 사용하는가?
A. 대규모 트래픽과 데이터 분산이 필요할 때.
