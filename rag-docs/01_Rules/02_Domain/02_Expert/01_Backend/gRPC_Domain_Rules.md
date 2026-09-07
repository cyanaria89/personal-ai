# gRPC Domain Rules

---

# 1. Domain Purpose

gRPC Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- High Performance Communication Support
- RPC Architecture Support
- Service-to-Service Communication Support
- Streaming Support
- gRPC Troubleshooting

우선순위:

1. gRPC Core
2. Protocol Buffers
3. RPC Communication
4. Streaming / Troubleshooting

---

# 2. Scope

포함 범위:

- gRPC Core
- RPC
- Protocol Buffers
- .proto
- Service Definition
- Message
- Unary RPC
- Server Streaming
- Client Streaming
- Bidirectional Streaming
- Stub
- Serialization
- HTTP/2
- Load Balancing
- Deadline
- Retry
- Interceptor
- Security
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

# 4. gRPC Core Rules

gRPC 문서는 High Performance RPC Communication 중심으로 작성.

핵심 구조:

- Client
- Stub
- Service
- Protocol Buffers

---

반드시 설명 포함:

- gRPC 역할
- 왜 사용하는가
- REST와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Client
→ Stub
→ gRPC Service
→ Response
```

---

# 5. RPC Rules

매우 중요.

필수 포함:

- RPC
- Remote Procedure Call

---

반드시 설명:

- 원격 함수 호출 개념
- Local Call과 차이

---

중요:

gRPC 문서 품질은 RPC 설명 품질이 결정.

---

# 6. Protocol Buffers Rules

매우 중요.

필수 포함:

- Protocol Buffers
- Binary Serialization

---

반드시 설명:

- 빠른 직렬화
- 경량 Payload

---

예:

- protobuf

---

# 7. Proto Rules

매우 중요.

필수 포함:

- .proto
- Schema Definition

---

예:

```proto
syntax = "proto3";
```

---

반드시 설명:

- Contract 정의
- Message / Service 선언

---

# 8. Message Rules

필수 포함:

- Message
- Field

---

예:

```proto
message UserRequest {
  string id = 1;
}
```

---

반드시 설명:

- Request / Response 구조

---

# 9. Service Rules

매우 중요.

필수 포함:

- Service Definition
- RPC Method

---

예:

```proto
service UserService {
}
```

---

반드시 설명:

- API Contract 역할

---

# 10. Unary RPC Rules

매우 중요.

필수 포함:

- Unary RPC
- Request / Response

---

Flow:

```text
Request
→ Response
```

---

반드시 설명:

- REST와 가장 유사한 패턴

---

# 11. Server Streaming Rules

필수 포함:

- Server Streaming

---

Flow:

```text
Client Request
→ Multiple Responses
```

---

반드시 설명:

- Server Push

---

# 12. Client Streaming Rules

필수 포함:

- Client Streaming

---

Flow:

```text
Multiple Requests
→ Single Response
```

---

반드시 설명:

- Batch Upload

---

# 13. Bidirectional Streaming Rules

매우 중요.

필수 포함:

- Bidirectional Streaming

---

Flow:

```text
Multiple Requests
↔ Multiple Responses
```

---

반드시 설명:

- Full Duplex Communication

---

# 14. Stub Rules

필수 포함:

- Client Stub
- Generated Client

---

반드시 설명:

- Client Proxy 역할

---

# 15. Serialization Rules

필수 포함:

- Binary Serialization
- Efficient Encoding

---

반드시 설명:

- JSON 대비 장점

---

# 16. HTTP/2 Rules

매우 중요.

필수 포함:

- HTTP/2
- Multiplexing

---

반드시 설명:

- 고성능 통신 기반

---

# 17. Deadline Rules

필수 포함:

- Deadline
- Timeout

---

반드시 설명:

- 무한 대기 방지
- Fail Fast

---

# 18. Retry Rules

필수 포함:

- Retry
- Backoff

---

반드시 설명:

- 일시 장애 대응

---

# 19. Interceptor Rules

필수 포함:

- Interceptor
- Cross Cutting Concern

---

반드시 설명:

- Logging
- Auth
- Metrics

---

# 20. Security Rules

필수 포함:

- TLS
- Authentication

---

반드시 설명:

- Secure Communication

---

# 21. Monitoring Rules

필수 포함:

- Latency
- Throughput
- Error Rate

---

반드시 설명:

- 운영 핵심 지표

---

# 22. Troubleshooting Rules

반드시 포함 추천.

예:

- Timeout
- Connection Failure
- Serialization Error
- Streaming Failure
- High Latency
- Contract Mismatch

---

형식:

문제:

원인:

해결:

---

# 23. Retrieval Optimization Rules

강조 대상:

- gRPC
- RPC
- Protocol Buffers
- Proto
- Unary
- Streaming
- Stub
- HTTP/2

키워드 반복 허용.

---

# 24. Version Rules

기준:

- gRPC
- Protocol Buffers v3
- HTTP/2
- Modern MSA Communication

---

Legacy 제외.

---

# 25. Common Mistakes

자주 발생:

- REST와 동일하게 사용
- Deadline 미설정
- Streaming 오남용
- Proto 변경 관리 실패
- Retry 폭주
- Contract Version 관리 부족

---

# 26. Final Goal

gRPC RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve gRPC Concepts
- Design RPC Communication
- Build gRPC Service
- Optimize Service Communication
- Troubleshoot gRPC Problems

문서 품질이 Service Communication 품질을 결정한다.
