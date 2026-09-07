# Network Domain Rules

---

# 1. Domain Purpose

Network Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Network Architecture Support
- Backend Communication Support
- Infrastructure Troubleshooting
- Network Performance Optimization
- Production Incident Analysis

우선순위:

1. Network Core
2. TCP/IP / HTTP
3. DNS / Proxy / Load Balancer
4. Troubleshooting

---

# 2. Scope

포함 범위:

- Network Core
- OSI 7 Layer
- TCP/IP
- IP
- Port
- DNS
- TCP
- UDP
- HTTP
- HTTPS
- TLS
- REST
- WebSocket
- Load Balancer
- Proxy
- Reverse Proxy
- CDN
- Firewall
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

# 4. Network Core Rules

Network 문서는 Backend Infrastructure Communication 중심으로 작성.

핵심 구조:

- Client
- Server
- Protocol
- Network Device
- Internet

---

반드시 설명 포함:

- Network 역할
- 왜 중요한가
- Backend에서 왜 필요한가
- 어떤 문제를 해결하는가

---

예:

```text
Client
→ Network
→ Server
→ Response
```

---

# 5. OSI Rules

필수 포함:

- OSI 7 Layer
- Layer 역할

---

예:

```text
Application
Presentation
Session
Transport
Network
Data Link
Physical
```

---

반드시 설명:

- Layer 구조
- Backend 관련 Layer 중심

---

중요:

Network 문서 품질은 OSI / TCP-IP 설명 품질이 결정.

---

# 6. TCP/IP Rules

매우 중요.

필수 포함:

- TCP/IP
- Protocol Stack

---

예:

```text
Application
Transport
Internet
Network Access
```

---

반드시 설명:

- 실제 인터넷 구조
- OSI와 차이

---

# 7. IP Rules

필수 포함:

- IP Address
- Routing

---

예:

```text
192.168.x.x
10.x.x.x
```

---

반드시 설명:

- Host 식별
- Packet 전달

---

# 8. Port Rules

매우 중요.

필수 포함:

- Port
- Listening Port

---

예:

```text
80
443
3306
8080
6379
```

---

반드시 설명:

- Process 식별
- 서비스 구분

---

# 9. DNS Rules

매우 중요.

필수 포함:

- DNS
- Domain Resolution

---

예:

```text
api.example.com
→ 192.168.x.x
```

---

반드시 설명:

- 도메인 → IP 변환

---

# 10. TCP Rules

매우 중요.

필수 포함:

- TCP
- Connection
- Reliability

---

반드시 설명:

- 3-way Handshake
- Reliable Delivery

---

Flow:

```text
SYN
→ SYN ACK
→ ACK
```

---

# 11. UDP Rules

필수 포함:

- UDP
- Fast Delivery

---

반드시 설명:

- Low Latency
- No Reliability

---

TCP 비교 포함.

---

# 12. HTTP Rules

매우 중요.

필수 포함:

- Request
- Response
- Stateless

---

예:

```text
GET /api/users
```

---

반드시 설명:

- Web 핵심 프로토콜
- Backend API 기반

---

# 13. HTTPS Rules

매우 중요.

필수 포함:

- HTTPS
- TLS

---

반드시 설명:

- Encryption
- Secure Communication

---

# 14. HTTP Method Rules

필수 포함:

- GET
- POST
- PUT
- PATCH
- DELETE

---

반드시 설명:

- REST API 설계 기본

---

# 15. HTTP Status Rules

필수 포함:

- 2xx
- 3xx
- 4xx
- 5xx

---

예:

```text
200
201
400
401
403
404
500
```

---

반드시 설명:

- 응답 상태 의미

---

# 16. WebSocket Rules

필수 포함:

- WebSocket
- Full Duplex

---

반드시 설명:

- 실시간 통신
- HTTP와 차이

---

예:

- Chat
- Notification
- Live Dashboard

---

# 17. Load Balancer Rules

매우 중요.

필수 포함:

- Load Balancer
- Traffic Distribution

---

반드시 설명:

- Scale Out
- High Availability

---

예:

```text
Client
→ Load Balancer
→ Server A / B / C
```

---

# 18. Proxy Rules

필수 포함:

- Proxy
- Forward Proxy

---

반드시 설명:

- Client 대리

---

# 19. Reverse Proxy Rules

매우 중요.

필수 포함:

- Reverse Proxy

---

반드시 설명:

- Server 대리
- Backend 보호

---

예:

- Nginx
- Apache

---

# 20. CDN Rules

필수 포함:

- CDN
- Edge Cache

---

반드시 설명:

- Static Resource Cache
- Latency 감소

---

# 21. Firewall Rules

필수 포함:

- Firewall
- Traffic Filter

---

반드시 설명:

- Security
- Access Control

---

# 22. Monitoring Rules

필수 포함:

- Latency
- Throughput
- Packet Loss
- Error Rate

---

반드시 설명:

- 운영 핵심 지표

---

# 23. Troubleshooting Rules

반드시 포함 추천.

예:

- Connection Refused
- Timeout
- DNS Failure
- Packet Loss
- SSL Error
- High Latency

---

형식:

문제:

원인:

해결:

---

# 24. Retrieval Optimization Rules

강조 대상:

- Network
- TCP
- HTTP
- DNS
- WebSocket
- Load Balancer
- Proxy
- HTTPS

키워드 반복 허용.

---

# 25. Version Rules

기준:

- Modern Internet Architecture
- HTTP/1.1
- HTTP/2
- HTTP/3
- TLS 1.3

---

Legacy 제외.

---

# 26. Common Mistakes

자주 발생:

- Port 개념 부족
- DNS 무시
- LB 역할 오해
- HTTP 상태 코드 오사용
- Timeout 원인 오판
- Reverse Proxy 이해 부족
- SSL 문제 대응 미숙

---

# 27. Final Goal

Network RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Network Concepts
- Explain Backend Communication
- Solve Network Problems
- Analyze Production Incidents
- Troubleshoot Infrastructure Issues

문서 품질이 Infrastructure Troubleshooting 품질을 결정한다.
