# Frontend Security Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Security Domain 목적

### [개념]

Frontend Security Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent / Security Review Agent용 RAG 문서 제작 규칙이다.

Frontend Security는 브라우저 환경에서 발생할 수 있는 XSS, CSRF, Token 노출, 민감정보 노출, 인증 / 권한 처리 오류, CORS 오해, CSP 미적용, 의존성 취약점, Third-party Script 위험, 사용자 입력 검증 문제를 줄이는 영역이다.

목적:

- 프론트엔드 보안 취약점 진단 지원
- XSS / DOM XSS 방어 기준 제공
- CSRF 방어 기준 제공
- Token / Cookie / Session 보안 판단 지원
- 인증 / 권한 Frontend Flow 검토 지원
- CSP / Security Header 적용 기준 제공
- CORS 오해 방지 지원
- 민감정보 / Secret 노출 방지 지원
- Form / File Upload / Redirect 보안 기준 제공
- Next.js App Router 보안 기준 제공
- Server Action / Route Handler 보안 검토 지원
- Frontend 코드 리뷰 지원

OWASP Top 10은 웹 애플리케이션의 주요 보안 위험에 대한 표준 인식 문서이며, 최신 릴리스는 OWASP Top 10 2025로 안내된다.

---

### [핵심]

우선순위:

1. Threat Modeling
2. XSS Prevention
3. DOM XSS Prevention
4. CSRF Prevention
5. Authentication Flow
6. Authorization UI Boundary
7. Token / Cookie Security
8. Secret Exposure Prevention
9. CSP / Security Headers
10. CORS Understanding
11. Input Validation
12. Output Encoding
13. Safe Redirect
14. File Upload Security
15. Third-party Script Security
16. Dependency Security
17. Next.js App Router Security
18. Server Action Security
19. Logging / Observability Security
20. Security Review Checklist

---

### [실무]

2026 실무 기준:

- React / Next.js App Router / TypeScript 기준 예제 우선
- Frontend 보안은 “서버 보안 대체”가 아니라 “브라우저 공격면 축소”로 설명
- 클라이언트 권한 체크는 UX용이며 실제 권한 검사는 서버에서 수행
- 사용자 입력은 클라이언트와 서버에서 모두 검증
- XSS 방어는 React escaping만 믿지 않고 HTML 삽입, URL, DOM API, Third-party Script까지 검토
- Token 저장 위치는 XSS / CSRF / UX / Backend 구조를 함께 고려
- HttpOnly Cookie 기반 인증과 Bearer Token 기반 인증의 차이를 명확히 설명
- CSP는 XSS 피해 완화를 위한 방어층으로 포함
- Secret은 Frontend Bundle에 절대 포함하지 않음
- `NEXT_PUBLIC_` 환경변수는 공개 값으로 취급
- Server Action은 서버 함수처럼 보이더라도 public endpoint로 취급하고 권한 검증 필요
- Agent가 보안 리뷰와 코드 생성에 바로 사용할 수 있는 판단 기준 포함

Next.js 공식 Data Security 가이드는 Server Action이 public HTTP endpoint처럼 취급되어야 하며, 페이지 수준 인증 확인이 해당 페이지 안의 Server Action까지 자동 확장되지 않으므로 Server Action 내부에서 재검증해야 한다고 설명한다.

---

### [FAQ]

Q. Frontend Security 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 코드에서 XSS, CSRF, Token 노출, Secret 노출, 인증 / 권한 오류, CSP 누락, CORS 오해, 의존성 취약점을 검토하도록 돕는 RAG 문서 제작 규칙이다.

Q. 프론트엔드 보안만 잘하면 서버 보안이 필요 없나?

A.
아니다. 프론트엔드 보안은 브라우저 공격면을 줄이는 것이고 실제 데이터 보호와 권한 검증은 서버에서 반드시 수행해야 한다.

Q. React를 쓰면 XSS가 자동으로 다 막히나?

A.
아니다. React는 기본 텍스트 escaping을 제공하지만 `dangerouslySetInnerHTML`, URL 삽입, DOM API, Third-party Script, Markdown 렌더링은 별도 검토가 필요하다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Security Domain은 브라우저, UI, 인증 흐름, API 호출, 상태 저장, 빌드 산출물, 외부 스크립트에서 발생할 수 있는 보안 위험을 포함한다.

---

### [핵심]

포함 범위:

- Frontend Security
- Web Security
- OWASP Top 10
- XSS
- DOM XSS
- Stored XSS
- Reflected XSS
- CSRF
- CSP
- Trusted Types
- Security Headers
- CORS
- Same-Origin Policy
- Cookie Security
- HttpOnly Cookie
- Secure Cookie
- SameSite Cookie
- LocalStorage Token
- SessionStorage Token
- Memory Token
- JWT Handling
- Access Token
- Refresh Token
- Authentication Flow
- Authorization UI
- Role-based UI
- Protected Route
- Server-side Authorization
- Secret Exposure
- Environment Variable
- `NEXT_PUBLIC_`
- Input Validation
- Output Encoding
- HTML Sanitization
- URL Sanitization
- Open Redirect
- File Upload Security
- Download Security
- Clipboard Security
- Third-party Script
- Dependency Vulnerability
- Supply Chain Security
- Source Map Exposure
- Error Message Exposure
- Logging PII
- Session Replay Privacy
- Next.js Server Action Security
- Route Handler Security
- Middleware / Proxy Security
- Security Review Checklist

---

### [실무]

제외 범위:

- Backend Security 심화 전체
- DB Security 심화
- Network Security 심화
- Kubernetes Security 심화
- Cloud IAM 심화
- Cryptography 구현 심화
- OAuth2 / OIDC 프로토콜 심화 전체
- Penetration Testing 공격 기법 심화
- Malware 분석
- Reverse Engineering
- Browser Exploit 내부 구현
- 보안 관제 / SIEM 심화

단, Frontend Security 판단에 필요한 인증 / 권한 / 세션 / API / 보안 헤더 / 배포 설정 지식은 포함 가능하다.

---

### [FAQ]

Q. OAuth2나 OIDC도 포함해야 하나?

A.
프로토콜 심화는 제외한다. 단, 프론트엔드 로그인 흐름, redirect 처리, token 저장, callback 검증 기준은 포함한다.

Q. Backend Security와 중복되지 않나?

A.
중복을 최소화한다. 이 문서는 브라우저와 프론트엔드 코드에서 발생하는 보안 위험과 서버 검증 경계를 중심으로 다룬다.

Q. Frontend Security 문서에 공격 코드 예제를 넣어도 되나?

A.
불필요한 공격 payload 예제는 지양하고, 안전한 방어 기준과 잘못된 패턴 설명 중심으로 작성한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Security RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

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

Frontend Security 문서는 위험 판단과 방어 기준이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: User Input → Validation → Encoding / Sanitization → Render → Server Validation
- `[Comparison]`: LocalStorage vs HttpOnly Cookie, XSS vs CSRF
- `[Best Practice]`: CSP, Token 최소 노출, Server-side Authorization
- `[Troubleshooting]`: Token 노출, CORS 오류, CSP 위반, Hydration 보안 오해
- `[Checklist]`: 배포 전 Security Review

---

### [FAQ]

Q. Frontend Security 문서에 Checklist가 중요한 이유는?

A.
보안은 누락이 위험하므로 XSS, CSRF, Token, Secret, CSP, CORS, 권한 검증을 반복 점검할 체크리스트가 필요하다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Frontend Security Principles Rules

## 4.1 보안 기본 원칙

### [개념]

Frontend Security 원칙은 클라이언트 코드를 신뢰하지 않고, 사용자 입력과 외부 데이터를 안전하게 처리하며, 민감정보가 브라우저에 노출되지 않도록 하는 기준이다.

---

### [핵심]

필수 원칙:

- Never Trust Client
- Defense in Depth
- Least Privilege
- Secure by Default
- Validate Input
- Encode Output
- Sanitize HTML
- Minimize Token Exposure
- Server-side Authorization
- No Secret in Bundle
- Safe Error Message
- Secure Defaults
- Privacy by Design
- Dependency Hygiene
- Monitor Security Events

---

### [실무]

설계 기준:

- 프론트엔드 검증은 UX용이고 서버 검증 필수
- 클라이언트에서 숨긴 버튼은 보안이 아님
- API 호출 전 권한 체크보다 API 서버 권한 검사가 우선
- Token / Secret / API Key를 브라우저에 노출하지 않음
- 사용자 입력은 렌더링 위치에 맞게 escaping / sanitization
- HTML 직접 삽입은 극도로 제한
- URL / redirect / file upload / download는 별도 보안 검토
- Third-party Script는 신뢰 경계로 취급
- 보안 헤더는 배포 설정과 함께 검토
- Error / Log / Observability에 민감정보 포함 금지

---

### [FAQ]

Q. Frontend Security에서 가장 중요한 원칙은?

A.
클라이언트를 신뢰하지 않는 것이다. 모든 중요한 권한과 데이터 검증은 서버에서 수행해야 한다.

Q. 프론트엔드 입력 검증은 의미 없나?

A.
의미 있다. UX 개선과 빠른 피드백에 유용하지만 보안 검증으로는 서버 검증이 필수이다.

Q. 버튼을 숨기면 권한 처리가 된 것인가?

A.
아니다. 버튼 숨김은 UX일 뿐이고 실제 API 권한 검사는 서버에서 수행해야 한다.

---

# 5. Threat Modeling Rules

## 5.1 프론트엔드 위협 모델링

### [개념]

Threat Modeling은 프론트엔드 기능이 어떤 공격면을 갖는지 사전에 식별하고 방어 기준을 정하는 과정이다.

---

### [핵심]

검토 대상:

- User Input
- URL Parameter
- Search Parameter
- Query String
- Hash Fragment
- Local Storage
- Session Storage
- Cookie
- API Response
- Third-party Script
- Markdown / Rich Text
- File Upload
- Redirect URL
- OAuth Callback
- Payment Callback
- Admin UI
- Feature Flag
- Source Map
- Error Log

기본 Flow:

```text
Feature 분석
→ 입력 지점 확인
→ 신뢰 경계 확인
→ 민감 데이터 확인
→ 공격 시나리오 확인
→ 방어 기준 지정
→ 리뷰 체크리스트 반영
```

---

### [실무]

위험 질문:

- 사용자가 입력한 값이 HTML로 렌더링되는가?
- URL 파라미터가 redirect나 API 요청에 사용되는가?
- API 응답을 신뢰하고 바로 렌더링하는가?
- Token이 JavaScript에서 접근 가능한 저장소에 있는가?
- 관리자 기능을 클라이언트에서만 제한하는가?
- Third-party Script가 민감 페이지에서 실행되는가?
- 파일 업로드 결과를 미리보기로 렌더링하는가?
- Source Map이 공개되어 코드 구조가 노출되는가?
- Error log에 개인정보가 들어가는가?

---

### [FAQ]

Q. Frontend Threat Modeling은 언제 해야 하나?

A.
로그인, 결제, 파일 업로드, 관리자 기능, 외부 HTML 렌더링, redirect, token 처리 기능을 만들 때 반드시 해야 한다.

Q. 프론트엔드에서 가장 위험한 입력 지점은?

A.
URL parameter, rich text / markdown, file upload, API response, third-party script, OAuth callback이 위험하다.

Q. Threat Modeling은 문서만 만들면 끝인가?

A.
아니다. 코드 리뷰, 테스트, 보안 헤더, 서버 검증까지 연결되어야 한다.

---

# 6. XSS Prevention Rules

## 6.1 XSS 방어 기준

### [개념]

XSS는 공격자가 악성 스크립트를 웹 페이지에 삽입해 사용자의 브라우저에서 실행시키는 취약점이다.

Frontend Security에서 XSS는 가장 중요한 위험 중 하나이며, 사용자 입력, API 응답, HTML 렌더링, Markdown, URL, DOM API, Third-party Script를 모두 검토해야 한다.

OWASP DOM Based XSS Prevention Cheat Sheet는 DOM 기반 XSS를 별도 범주로 다루며, reflected / stored XSS와 함께 XSS의 주요 형태로 설명한다.

---

### [핵심]

XSS 유형:

- Stored XSS
- Reflected XSS
- DOM-based XSS
- HTML Injection
- Script Injection
- Attribute Injection
- URL-based XSS
- Markdown XSS
- Rich Text XSS

방어 기준:

- Output Encoding
- HTML Sanitization
- Avoid Dangerous HTML
- Safe URL Handling
- CSP
- Trusted Types
- No Inline Script
- No Dangerous DOM API
- Validate Untrusted Data
- Escape User Content

---

### [실무]

React / Next.js 기준:

- JSX 텍스트 렌더링은 기본 escaping을 활용
- `dangerouslySetInnerHTML` 사용 금지 또는 엄격 제한
- Markdown / Rich Text는 sanitizer 적용
- URL은 허용 scheme만 사용
- `javascript:` URL 차단
- user input을 HTML attribute에 직접 넣을 때 주의
- DOM API의 `innerHTML`, `outerHTML`, `insertAdjacentHTML` 사용 제한
- Third-party HTML widget은 sandbox / iframe / CSP 검토
- CSP를 추가 방어층으로 사용
- 사용자 입력을 Server Component에서 렌더링하더라도 동일하게 검토

위험 예시:

```tsx
<div dangerouslySetInnerHTML={{ __html: userProvidedHtml }} />
```

대안 예시:

```tsx
<p>{userProvidedText}</p>
```

---

### [FAQ]

Q. XSS는 프론트엔드에서 가장 중요하게 봐야 하나?

A.
그렇다. 브라우저에서 실행되는 공격이므로 Token 탈취, 사용자 행동 위조, 개인정보 노출로 이어질 수 있다.

Q. React JSX에 `{value}`로 출력하면 안전한가?

A.
일반 텍스트 렌더링은 React escaping으로 비교적 안전하지만 HTML 삽입, URL, DOM API 사용은 별도 검토가 필요하다.

Q. `dangerouslySetInnerHTML`은 절대 쓰면 안 되나?

A.
가능하면 피해야 한다. 꼭 필요하면 신뢰 가능한 sanitizer, CSP, 허용 태그 / 속성 정책을 함께 적용해야 한다.

---

# 7. DOM XSS Rules

## 7.1 DOM 기반 XSS 방어

### [개념]

DOM XSS는 클라이언트 JavaScript가 URL, hash, localStorage, postMessage, API 응답 등 신뢰할 수 없는 값을 읽어 DOM에 위험하게 삽입할 때 발생한다.

---

### [핵심]

위험 Source:

- `location.href`
- `location.search`
- `location.hash`
- `document.referrer`
- `localStorage`
- `sessionStorage`
- `postMessage`
- API Response
- Third-party Data

위험 Sink:

- `innerHTML`
- `outerHTML`
- `insertAdjacentHTML`
- `document.write`
- `eval`
- `new Function`
- `setTimeout(string)`
- `setInterval(string)`
- HTML attribute injection
- URL assignment

---

### [실무]

방어 기준:

- URL / hash 값을 HTML로 직접 삽입하지 않기
- DOM sink 사용 전 sanitizer 적용
- `eval`, `new Function` 금지
- `postMessage`는 origin 검증
- localStorage 값을 신뢰하지 않기
- DOMPurify 같은 sanitizer 사용 시 설정 검토
- sanitizer 적용 후에도 URL scheme 확인
- HTML 대신 textContent / JSX text 사용
- Trusted Types 적용 검토

예시:

```ts
const message = new URLSearchParams(location.search).get("message") ?? "";
element.textContent = message;
```

금지 예시:

```ts
element.innerHTML = location.hash;
```

---

### [FAQ]

Q. DOM XSS는 왜 발생하나?

A.
클라이언트 코드가 URL, localStorage, API 응답 같은 신뢰할 수 없는 값을 위험한 DOM API에 넣을 때 발생한다.

Q. `innerHTML`을 쓰면 항상 위험한가?

A.
사용자나 외부에서 온 값을 넣으면 매우 위험하다. 가능하면 text 렌더링을 사용해야 한다.

Q. URL query 값을 화면에 보여줄 때 어떻게 해야 하나?

A.
HTML로 삽입하지 말고 텍스트로 렌더링하거나 안전하게 escaping해야 한다.

---

# 8. HTML Sanitization Rules

## 8.1 Rich Text / Markdown Sanitization

### [개념]

HTML Sanitization은 사용자가 작성한 HTML, Markdown, Rich Text에서 위험한 태그와 속성을 제거해 안전하게 렌더링하는 과정이다.

---

### [핵심]

검토 대상:

- Markdown Preview
- Rich Text Editor
- CMS Content
- User Bio
- Comment
- Review
- Admin Notice
- Email Template Preview
- External HTML
- Embedded Widget

방어 기준:

- Allowlist Sanitization
- Remove Script Tag
- Remove Event Handler Attribute
- Remove Dangerous URL Scheme
- Limit iframe
- Sandbox iframe
- CSP
- Server-side Sanitization
- Client-side Sanitization
- Re-sanitize on Render

---

### [실무]

작성 기준:

- HTML 허용이 필요한 이유를 명확히 함
- 가능한 Markdown → safe HTML 변환 사용
- sanitizer allowlist를 명시
- `script`, `style`, event handler 속성 제거
- `href`, `src`의 scheme 검증
- iframe은 도메인 allowlist와 sandbox 적용
- 서버 저장 전 sanitization + 렌더링 전 sanitization 검토
- sanitizer library 업데이트 관리
- Sanitized HTML도 CSP와 함께 보호
- 관리자 입력도 무조건 신뢰하지 않음

주의:

- blacklist 방식은 우회 위험이 큼
- sanitizer 설정 오류는 XSS로 이어질 수 있음
- Markdown library plugin이 HTML을 허용하는지 확인
- 이미지 / 링크 preview도 URL 검증 필요

---

### [FAQ]

Q. Markdown은 안전한가?

A.
항상 안전하지 않다. Markdown 렌더러가 HTML을 허용하거나 plugin이 있으면 XSS 위험이 생길 수 있다.

Q. Sanitization은 클라이언트에서만 하면 되나?

A.
아니다. 저장 전 서버에서 처리하고 렌더링 시에도 안전성을 확인하는 것이 좋다.

Q. iframe을 허용해도 되나?

A.
가능하지만 허용 도메인, sandbox, CSP, 권한 제한을 반드시 검토해야 한다.

---

# 9. CSP and Security Headers Rules

## 9.1 CSP / 보안 헤더 기준

### [개념]

CSP는 브라우저가 페이지에서 로드하고 실행할 수 있는 리소스를 제한해 XSS와 데이터 주입 공격 피해를 줄이는 보안 헤더이다.

MDN은 CSP가 웹사이트가 브라우저에 코드가 수행할 수 있는 일을 제한하도록 지시하는 기능이며, 특정 보안 위협을 방지하거나 최소화하는 데 도움을 준다고 설명한다.

---

### [핵심]

필수 Header:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- Cross-Origin-Opener-Policy
- Cross-Origin-Embedder-Policy
- Cross-Origin-Resource-Policy

CSP 주요 Directive:

- `default-src`
- `script-src`
- `style-src`
- `img-src`
- `connect-src`
- `font-src`
- `frame-src`
- `object-src`
- `base-uri`
- `form-action`
- `frame-ancestors`
- `upgrade-insecure-requests`
- `report-uri`
- `report-to`

OWASP CSP Cheat Sheet는 엄격한 CSP가 stored / reflected / 일부 DOM XSS 공격 방어에 도움을 주며, strict policy를 목표로 삼을 수 있다고 설명한다.

---

### [실무]

CSP 작성 기준:

- `default-src 'self'` 기준 검토
- `object-src 'none'` 적용 검토
- `base-uri 'self'` 적용 검토
- inline script 금지 또는 nonce / hash 사용
- 외부 script 도메인 allowlist 최소화
- `connect-src`에 API / observability endpoint 명시
- `img-src`에 필요한 이미지 도메인만 허용
- `frame-ancestors`로 clickjacking 방어
- CSP Report-Only로 먼저 검증 가능
- Third-party Script 도입 시 CSP 업데이트 리뷰
- dev 환경과 production CSP 차이 관리

예시:

```http
Content-Security-Policy: default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none';
```

주의:

- CSP는 XSS 방어의 보조층이지 sanitization 대체가 아님
- `unsafe-inline`, `unsafe-eval` 남용 금지
- CSP가 너무 느슨하면 효과가 약함
- CSP가 너무 엄격하면 정상 리소스 차단 가능
- violation report에 개인정보가 포함되지 않게 주의

---

### [FAQ]

Q. CSP는 왜 필요한가?

A.
XSS가 발생하더라도 스크립트 실행과 외부 전송을 제한해 피해를 줄이는 방어층으로 필요하다.

Q. CSP만 있으면 XSS가 해결되나?

A.
아니다. 입력 검증, 출력 encoding, HTML sanitization, 안전한 DOM API 사용이 함께 필요하다.

Q. `unsafe-inline`을 써도 되나?

A.
권장하지 않는다. 필요한 경우 nonce나 hash 기반 정책을 검토해야 한다.

---

# 10. Trusted Types Rules

## 10.1 Trusted Types 적용 기준

### [개념]

Trusted Types는 DOM XSS를 줄이기 위해 위험한 DOM sink에 문자열을 직접 넣는 것을 제한하고, 신뢰된 정책을 통해 생성된 값만 허용하는 브라우저 보안 기능이다.

---

### [핵심]

필수 포함:

- Trusted Types
- DOM XSS
- TrustedHTML
- TrustedScript
- TrustedScriptURL
- Policy
- CSP `require-trusted-types-for`
- Dangerous Sink
- Sanitizer Integration

---

### [실무]

적용 기준:

- 대규모 앱에서 DOM XSS 위험이 높을 때 검토
- `innerHTML` 같은 sink 사용이 많은 코드베이스에서 유용
- sanitizer와 Trusted Types policy를 연결
- report-only로 먼저 적용 가능
- Third-party library 호환성 확인
- React 앱에서도 직접 DOM 조작 코드가 있으면 검토
- CSP와 함께 구성
- 우회 policy 남발 금지

주의:

- 모든 브라우저 지원 상황 확인 필요
- Trusted Types는 sanitization 자체가 아니라 sink 제어 장치
- 잘못된 policy는 효과를 약화시킴
- Legacy library 호환 문제가 발생할 수 있음

---

### [FAQ]

Q. Trusted Types는 무엇을 막는가?

A.
문자열이 위험한 DOM sink에 직접 들어가는 것을 제한해 DOM XSS 위험을 줄인다.

Q. Trusted Types를 쓰면 sanitization이 필요 없나?

A.
아니다. Trusted Types는 sink 접근을 제어하고, 실제 HTML 안전화는 sanitizer 정책이 담당해야 한다.

Q. React 앱에서도 Trusted Types가 필요한가?

A.
직접 DOM 조작이나 `dangerouslySetInnerHTML` 사용이 있으면 검토할 수 있다.

---

# 11. CSRF Rules

## 11.1 CSRF 방어 기준

### [개념]

CSRF는 사용자가 로그인된 상태를 악용해 공격자가 원치 않는 요청을 보내게 만드는 공격이다.

Cookie 기반 인증에서는 CSRF 방어가 중요하며, SameSite Cookie, CSRF Token, Origin / Referer 검증을 함께 고려해야 한다.

---

### [핵심]

방어 기준:

- SameSite Cookie
- CSRF Token
- Double Submit Cookie
- Origin Check
- Referer Check
- Custom Header
- Idempotent Method
- Safe Method
- State-changing Request Protection
- Server-side Validation

---

### [실무]

Cookie 기반 인증 기준:

- 상태 변경 요청은 CSRF 방어 적용
- SameSite=Lax 또는 Strict 검토
- Cross-site 요청이 필요하면 SameSite=None + Secure 필요
- CSRF Token을 서버에서 검증
- Origin / Referer 검증 추가 가능
- GET 요청으로 상태 변경 금지
- Form POST / Server Action / Route Handler도 검토
- CORS 허용과 CSRF 방어를 혼동하지 않기

Bearer Token 기반 인증 기준:

- Authorization header에 token을 넣는 방식은 일반적인 CSRF 위험은 낮지만 XSS 위험이 커질 수 있음
- Token 저장 위치와 XSS 방어를 함께 고려
- Token 자동 첨부 여부에 따라 위험 모델이 달라짐

---

### [FAQ]

Q. CSRF는 언제 특히 중요하나?

A.
브라우저가 자동으로 Cookie를 첨부하는 Cookie 기반 인증에서 상태 변경 요청을 처리할 때 중요하다.

Q. SameSite Cookie만 있으면 CSRF가 완전히 막히나?

A.
도움이 되지만 모든 상황을 대체하지는 않는다. 중요한 요청은 CSRF Token과 Origin 검증도 고려한다.

Q. CORS를 막으면 CSRF도 막히나?

A.
아니다. CORS는 응답 접근 제어이고 CSRF는 요청 발생 자체를 악용하는 공격이다.

---

# 12. Cookie Security Rules

## 12.1 Cookie 보안 기준

### [개념]

Cookie Security는 세션 쿠키와 인증 관련 쿠키가 HTTPS에서만 전송되고, JavaScript 접근이 제한되며, cross-site 전송 범위가 통제되도록 설정하는 기준이다.

MDN의 Secure Cookie Configuration 가이드는 `Secure` 속성으로 HTTPS에서만 전송되도록 하고, `HttpOnly` 속성으로 JavaScript 접근을 제한할 것을 안내한다.

---

### [핵심]

Cookie 속성:

- HttpOnly
- Secure
- SameSite
- Path
- Domain
- Max-Age
- Expires
- Priority
- Partitioned
- `__Host-` Prefix
- `__Secure-` Prefix

---

### [실무]

작성 기준:

- 인증 쿠키는 HttpOnly 권장
- 운영 환경에서는 Secure 필수
- SameSite=Lax 또는 Strict 기본 검토
- cross-site 필요 시 SameSite=None + Secure
- Domain 범위 최소화
- Path 범위 최소화
- 만료 시간 명확화
- `__Host-` prefix 검토
- JavaScript에서 접근해야 하는 값과 인증 쿠키 분리
- Cookie에 민감 데이터를 과도하게 저장하지 않기

주의:

- HttpOnly Cookie는 JS에서 읽을 수 없으므로 UX 상태는 별도 current user API 필요
- SameSite 설정이 OAuth / 결제 redirect에 영향을 줄 수 있음
- Cookie 크기 제한 고려
- Cookie는 요청마다 전송되어 네트워크 비용이 생길 수 있음
- local 개발 환경과 production cookie 설정 차이 주의

---

### [FAQ]

Q. 인증 쿠키에는 어떤 속성이 필요한가?

A.
일반적으로 HttpOnly, Secure, SameSite, 적절한 Path / Domain / Expiration 설정이 필요하다.

Q. HttpOnly Cookie를 쓰면 XSS에 완전히 안전한가?

A.
Token 탈취 위험은 줄지만 XSS 자체를 막지는 못한다. 공격자가 사용자 권한으로 요청을 보낼 수 있으므로 XSS 방어는 여전히 필요하다.

Q. SameSite=None은 언제 쓰나?

A.
cross-site iframe, OAuth / 외부 도메인 연동 등 cross-site cookie 전송이 필요한 경우에만 Secure와 함께 사용한다.

---

# 13. Token Storage Rules

## 13.1 Token 저장 위치 판단

### [개념]

Token Storage는 access token, refresh token, session id를 어디에 저장할지 결정하는 보안 설계이다.

브라우저 저장소는 각각 XSS, CSRF, UX, 만료 처리, API 호출 방식에 다른 위험을 갖는다.

---

### [핵심]

저장 위치 비교:

| 저장 위치           | 장점               | 위험                |
| ------------------- | ------------------ | ------------------- |
| HttpOnly Cookie     | JS 탈취 어려움     | CSRF 고려 필요      |
| Memory              | 새로고침 시 사라짐 | UX 복잡             |
| LocalStorage        | 구현 쉬움          | XSS 시 탈취 위험    |
| SessionStorage      | 탭 단위 저장       | XSS 시 탈취 위험    |
| Non-HttpOnly Cookie | 자동 전송 가능     | JS 접근 / CSRF 위험 |

---

### [실무]

판단 기준:

- Refresh Token은 HttpOnly Cookie 우선 검토
- Access Token을 JS에서 다뤄야 한다면 만료 시간 짧게 유지
- LocalStorage token 저장은 XSS 위험을 명시
- SessionStorage도 XSS에는 안전하지 않음
- Memory token은 보안상 유리하지만 새로고침 UX 처리 필요
- Token rotation / refresh flow와 함께 설계
- Logout 시 client cache와 token 상태 정리
- Token을 log / error / URL에 남기지 않기
- Token을 query string에 넣지 않기
- Token 저장 방식은 backend 인증 구조와 함께 결정

---

### [FAQ]

Q. Access Token을 LocalStorage에 저장해도 되나?

A.
가능은 하지만 XSS 시 탈취 위험이 크다. 보안 요구가 높으면 HttpOnly Cookie나 memory 저장 전략을 검토한다.

Q. SessionStorage는 LocalStorage보다 안전한가?

A.
탭 종료 시 사라지는 차이는 있지만 XSS로 읽힐 수 있다는 점은 같다.

Q. Token을 URL query에 넣어도 되나?

A.
권장하지 않는다. browser history, referrer, log, analytics에 노출될 수 있다.

---

# 14. Authentication Flow Rules

## 14.1 인증 흐름 보안

### [개념]

Authentication Flow는 사용자가 로그인하고 세션을 유지하며 로그아웃하는 과정에서 token, cookie, redirect, current user 상태를 안전하게 관리하는 구조이다.

---

### [핵심]

필수 포함:

- Login Flow
- Logout Flow
- Session Check
- Current User
- Refresh Flow
- Token Rotation
- Auth Callback
- Redirect URL
- OAuth Callback
- MFA Flow
- Session Expiration
- Re-authentication
- Secure Logout

Flow:

```text
Login Submit
→ Server Authentication
→ Session / Token Issued
→ Current User Fetch
→ Protected UI Render
→ Refresh / Expire / Logout
```

---

### [실무]

작성 기준:

- 로그인 실패 메시지는 과도한 계정 정보 노출 금지
- current user API로 세션 상태 확인
- refresh 실패 시 안전하게 logout 처리
- logout 시 client cache / memory state 정리
- redirect URL은 allowlist 검증
- OAuth state parameter 검증
- callback URL에 token 노출 금지
- 로그인 후 권한별 redirect는 서버 검증과 연결
- 인증 상태 loading / expired / unauthenticated 처리
- 다중 탭 logout 동기화 검토

주의:

- “로그인됨” client state만 믿지 않기
- JWT payload는 서명 검증 없이 신뢰하지 않기
- token 만료 시간을 클라이언트 UX에 활용할 수 있지만 보안 판단은 서버 기준
- OAuth callback에서 open redirect 주의

---

### [FAQ]

Q. 프론트엔드에서 로그인 상태는 어떻게 확인하나?

A.
서버 세션이나 token을 기준으로 current user API를 호출해 확인하고, client state는 UX 표시용으로 사용한다.

Q. JWT payload를 decode해서 권한을 판단해도 되나?

A.
UI 표시에는 참고할 수 있지만 실제 권한 판단은 서버에서 서명과 권한을 검증해야 한다.

Q. 로그인 후 redirect URL은 어떻게 검증하나?

A.
상대 경로나 허용된 도메인 allowlist만 허용하고 외부 URL은 차단해야 한다.

---

# 15. Authorization UI Rules

## 15.1 권한 UI와 서버 권한 검증

### [개념]

Authorization UI는 사용자의 role, permission, plan에 따라 버튼, 메뉴, 페이지 접근을 다르게 보여주는 UI 처리이다.

하지만 클라이언트 권한 UI는 보안 경계가 아니며 실제 권한 검증은 서버에서 수행해야 한다.

---

### [핵심]

필수 포함:

- Role-based UI
- Permission-based UI
- Feature Flag
- Protected Route
- Admin UI
- Server-side Authorization
- API Authorization
- Server Action Authorization
- Route Handler Authorization
- UI Guard
- Auth Guard
- Defense in Depth

---

### [실무]

작성 기준:

- 권한별 메뉴 숨김은 UX용
- API / Server Action / Route Handler에서 권한 재검증
- 관리자 route는 서버에서 role 확인
- 권한 없는 사용자는 403 처리
- 401과 403 구분
- Feature flag는 보안 권한 대체 불가
- 숨겨진 버튼도 API를 직접 호출할 수 있음을 가정
- Client bundle에 민감한 관리자 데이터 포함 금지
- 권한 정책은 중앙화된 helper / server utility로 관리
- 권한 변화 시 client cache invalidation 고려

금지 예시:

```ts
if (user.role === "admin") {
  showDeleteButton();
}
// API 서버에서 권한 검증이 없으면 취약
```

---

### [FAQ]

Q. 버튼을 숨기면 API를 못 쓰게 막은 것인가?

A.
아니다. 사용자는 직접 API를 호출할 수 있으므로 서버에서 반드시 권한을 검증해야 한다.

Q. 401과 403은 어떻게 구분하나?

A.
401은 인증되지 않은 상태이고, 403은 인증은 되었지만 권한이 없는 상태이다.

Q. Feature Flag를 권한처럼 써도 되나?

A.
안 된다. Feature Flag는 기능 노출 제어이고 보안 권한 검증을 대체할 수 없다.

---

# 16. Secret and Environment Variable Rules

## 16.1 Secret 노출 방지

### [개념]

Frontend Secret Exposure는 API secret, private key, server-only token, database URL 같은 값이 브라우저 bundle에 포함되어 사용자에게 노출되는 문제이다.

---

### [핵심]

보호 대상:

- API Secret
- Private Key
- Database URL
- Server Token
- Service Role Key
- Payment Secret Key
- OAuth Client Secret
- Webhook Secret
- Admin API Key
- Internal Endpoint Key

환경변수 기준:

- Public Environment Variable
- Server-only Environment Variable
- Build-time Environment Variable
- Runtime Environment Variable
- `NEXT_PUBLIC_`
- `.env.local`
- Secret Manager

---

### [실무]

작성 기준:

- Frontend bundle에 secret 포함 금지
- `NEXT_PUBLIC_` 변수는 공개 값으로 취급
- OAuth Client Secret은 서버에서만 사용
- 결제 secret key는 서버에서만 사용
- Webhook secret은 Route Handler / Backend에서만 사용
- `.env.local`은 Git에 커밋 금지
- secret이 source map / log / error report에 포함되지 않게 점검
- public API key라도 권한 제한과 origin 제한 검토
- 환경변수 접근을 config 파일로 중앙화
- 배포 플랫폼 환경변수 권한 관리

예시:

```ts
export const publicEnv = {
  appBaseUrl: process.env.NEXT_PUBLIC_APP_BASE_URL,
};
```

금지 예시:

```ts
const paymentSecret = process.env.NEXT_PUBLIC_PAYMENT_SECRET_KEY;
```

---

### [FAQ]

Q. `NEXT_PUBLIC_`에 secret을 넣어도 되나?

A.
안 된다. `NEXT_PUBLIC_` 값은 브라우저 bundle에 포함되어 사용자에게 노출될 수 있다.

Q. 카카오맵 JavaScript Key 같은 public key는 secret인가?

A.
일반적으로 브라우저에서 사용하는 public key는 secret이 아니다. 대신 허용 도메인, 사용량 제한, API 권한 제한을 설정해야 한다.

Q. `.env.local`은 안전한가?

A.
로컬 파일 자체는 편리하지만 Git에 커밋하면 위험하다. `.gitignore`와 secret 관리 정책이 필요하다.

---

# 17. CORS Rules

## 17.1 CORS 이해와 오해 방지

### [개념]

CORS는 브라우저가 다른 Origin의 리소스에 접근할 수 있는지 서버 응답 헤더를 기준으로 제한하는 브라우저 보안 정책이다.

CORS는 서버 인증 / 권한 검증을 대체하지 않으며, CSRF 방어도 완전히 대체하지 않는다.

---

### [핵심]

필수 포함:

- Same-Origin Policy
- CORS
- Origin
- Preflight Request
- `Access-Control-Allow-Origin`
- `Access-Control-Allow-Credentials`
- `Access-Control-Allow-Headers`
- `Access-Control-Allow-Methods`
- Credentialed Request
- Exposed Headers
- CSRF Difference
- Server-side Authorization

---

### [실무]

작성 기준:

- CORS는 서버에서 설정
- 허용 Origin은 최소화
- `Access-Control-Allow-Origin: *`와 credentials 조합 금지
- Credentialed request는 정확한 origin allowlist 필요
- Authorization header 사용 시 preflight 고려
- custom trace header 사용 시 allowed headers 필요
- response header를 JS에서 읽으려면 exposed headers 필요
- 개발 환경 proxy와 운영 CORS를 구분
- CORS 에러를 보안 검증 실패와 혼동하지 않기
- CORS 허용이 API 권한 허용을 의미하지 않음

주의:

- CORS는 브라우저 정책이므로 서버 간 요청은 별도
- CORS를 열어도 서버 권한 검증은 필수
- CORS를 닫아도 CSRF 요청 자체가 완전히 사라지는 것은 아님
- Origin 검증과 인증 / 권한 검증은 별개

---

### [FAQ]

Q. CORS를 설정하면 보안이 끝나나?

A.
아니다. CORS는 브라우저 접근 제어이고 인증 / 권한 검증은 서버에서 별도로 해야 한다.

Q. `Access-Control-Allow-Origin: *`를 써도 되나?

A.
공개 API가 아니면 권장하지 않는다. credentials를 사용하는 요청에서는 사용할 수 없다.

Q. CORS와 CSRF는 같은 문제인가?

A.
아니다. CORS는 응답 접근 제어이고 CSRF는 사용자의 인증 상태를 악용해 요청을 보내는 공격이다.

---

# 18. Input Validation Rules

## 18.1 사용자 입력 검증

### [개념]

Input Validation은 사용자가 입력하거나 URL / API / 파일에서 들어온 값을 기대하는 형식, 길이, 범위, 타입으로 제한하는 과정이다.

프론트엔드 입력 검증은 UX 개선과 오류 예방에 유용하지만 보안 최종 검증은 서버에서 수행해야 한다.

---

### [핵심]

검증 대상:

- Form Input
- Search Query
- URL Params
- Route Params
- Query String
- File Name
- File Type
- File Size
- Rich Text
- JSON Payload
- Date Range
- Number Range
- Enum Value
- Redirect URL

---

### [실무]

작성 기준:

- 클라이언트 검증과 서버 검증을 모두 수행
- schema validation 사용 검토
- 길이 제한 적용
- enum 값 allowlist 검증
- 숫자 범위 검증
- 날짜 범위 검증
- 파일 확장자와 MIME type 검증
- URL은 allowlist 기반 검증
- 입력값을 trim / normalize
- 에러 메시지는 안전하게 표시
- validation error를 HTML로 렌더링하지 않기

예시:

```ts
type LoginInput = {
  email: string;
  password: string;
};
```

주의:

- 프론트엔드 검증은 우회 가능
- blacklist보다 allowlist 우선
- 정규식이 과도하게 복잡하면 ReDoS 위험 검토
- validation과 sanitization을 혼동하지 않기

---

### [FAQ]

Q. 프론트엔드 입력 검증은 왜 필요한가?

A.
사용자에게 빠른 피드백을 주고 잘못된 요청을 줄이기 위해 필요하다. 하지만 서버 검증을 대체하지는 못한다.

Q. allowlist와 blacklist 중 무엇이 좋은가?

A.
가능하면 허용 가능한 값만 통과시키는 allowlist 방식이 안전하다.

Q. validation과 sanitization은 같은가?

A.
아니다. validation은 값이 규칙에 맞는지 검사하고, sanitization은 위험한 내용을 제거하거나 안전하게 변환한다.

---

# 19. Output Encoding Rules

## 19.1 출력 Encoding 기준

### [개념]

Output Encoding은 데이터를 렌더링하는 위치에 맞게 안전한 문자 표현으로 바꾸는 과정이다.

XSS 방어는 입력 검증만으로 충분하지 않으며, HTML body, attribute, URL, JavaScript context마다 다른 encoding 기준이 필요하다.

---

### [핵심]

Encoding Context:

- HTML Text
- HTML Attribute
- URL
- JavaScript String
- CSS
- JSON
- Markdown Output

React 기준:

- JSX text escaping
- Attribute escaping
- Dangerous HTML 금지
- URL scheme validation
- JSON serialization 주의

---

### [실무]

작성 기준:

- HTML text는 React JSX escaping 사용
- HTML attribute에는 신뢰할 수 없는 값 삽입 주의
- URL은 scheme allowlist 검증
- JSON을 script 태그에 직접 삽입하지 않기
- 사용자 데이터를 JavaScript string으로 직접 조합하지 않기
- CSS style 값에 사용자 입력 사용 제한
- Markdown / HTML 출력은 sanitization과 encoding 병행
- i18n 메시지에 HTML 삽입 주의
- error message도 safe text로 렌더링

예시:

```tsx
<p>{safeMessage}</p>
```

금지 예시:

```tsx
<script>{`window.message = "${userInput}"`}</script>
```

---

### [FAQ]

Q. Output Encoding은 왜 필요한가?

A.
사용자 입력이 HTML이나 Script로 해석되지 않고 텍스트로 표시되도록 하기 위해 필요하다.

Q. React가 encoding을 해주면 더 할 게 없나?

A.
일반 JSX text는 안전하지만 HTML 직접 삽입, URL, script, style context는 별도 검토가 필요하다.

Q. URL도 encoding만 하면 안전한가?

A.
아니다. `javascript:` 같은 위험 scheme을 차단하는 URL validation도 필요하다.

---

# 20. Safe URL and Redirect Rules

## 20.1 URL / Redirect 보안

### [개념]

Safe URL and Redirect는 URL query, callback, redirect parameter, external link를 안전하게 처리해 open redirect, phishing, XSS, token leakage를 방지하는 기준이다.

---

### [핵심]

위험 요소:

- Open Redirect
- External Redirect
- OAuth Redirect
- Login Redirect
- Callback URL
- `returnUrl`
- `next`
- `redirect_uri`
- URL Scheme
- `javascript:` URL
- Token in URL
- Referrer Leakage

---

### [실무]

작성 기준:

- redirect 대상은 상대 경로 또는 allowlist 도메인만 허용
- `javascript:`, `data:` scheme 차단
- URL query로 token 전달 금지
- OAuth redirect_uri는 서버 allowlist 검증
- 로그인 후 redirect는 내부 경로만 허용
- 외부 링크는 사용자에게 명확히 표시 가능
- 새 탭 링크는 `rel="noopener noreferrer"` 검토
- URL parsing은 `new URL()` 사용
- query string log / analytics에 민감정보 노출 주의
- referrer policy 적용 검토

예시:

```ts
function isSafeInternalPath(path: string) {
  return path.startsWith("/") && !path.startsWith("//");
}
```

---

### [FAQ]

Q. Open Redirect는 왜 위험한가?

A.
공식 도메인을 거쳐 공격자 사이트로 이동시켜 phishing이나 token 탈취에 악용될 수 있다.

Q. 로그인 후 redirect는 어떻게 처리해야 하나?

A.
상대 경로만 허용하거나 허용된 도메인 allowlist를 사용해야 한다.

Q. URL에 token을 넣으면 왜 위험한가?

A.
브라우저 history, server log, referrer, analytics, screenshot에 노출될 수 있다.

---

# 21. File Upload and Download Security Rules

## 21.1 파일 업로드 / 다운로드 보안

### [개념]

File Upload Security는 사용자가 업로드하는 파일이 악성 스크립트, 잘못된 MIME type, 과도한 크기, 위험한 파일명, XSS payload를 포함하지 않도록 제한하는 기준이다.

---

### [핵심]

검토 대상:

- File Size
- File Type
- MIME Type
- Extension
- File Name
- Image Preview
- SVG Upload
- PDF Preview
- HTML Upload
- Malware Scan
- Content Disposition
- Download Filename
- Object URL
- File URL Access Control

---

### [실무]

Frontend 기준:

- 파일 크기 client validation
- 확장자 allowlist
- MIME type 확인
- 이미지 미리보기 시 object URL cleanup
- SVG 업로드는 XSS 위험 검토
- HTML 파일 미리보기 금지 또는 sandbox
- 파일명 화면 출력 시 escaping
- 다운로드 링크 권한 확인은 서버 기준
- private file URL 노출 주의
- 업로드 실패 / 진행률 UI 제공
- 클라이언트 검증은 UX용이며 서버 검증 필수

예시:

```ts
const allowedTypes = ["image/png", "image/jpeg", "image/webp"];
```

주의:

- MIME type은 조작 가능하므로 서버 검증 필요
- SVG는 script / external resource 위험
- object URL revoke 누락 시 memory leak
- 파일명에 HTML이 포함될 수 있음
- 다운로드 응답 header는 서버에서 안전하게 설정

---

### [FAQ]

Q. 파일 업로드 검증은 프론트에서만 하면 되나?

A.
아니다. 프론트 검증은 UX용이고 서버에서 파일 크기, MIME, 확장자, 내용 검사를 다시 해야 한다.

Q. SVG 업로드는 왜 위험한가?

A.
SVG는 스크립트나 외부 리소스를 포함할 수 있어 XSS 위험이 있다.

Q. 파일명도 escaping해야 하나?

A.
그렇다. 파일명에 HTML이나 특수문자가 포함될 수 있으므로 화면 출력 시 안전하게 처리해야 한다.

---

# 22. Third-party Script Security Rules

## 22.1 외부 스크립트 보안

### [개념]

Third-party Script Security는 분석, 광고, 지도, 결제, 채팅, 소셜 위젯 같은 외부 스크립트가 페이지 권한으로 실행되면서 발생하는 보안 위험을 관리하는 기준이다.

---

### [핵심]

위험 요소:

- Third-party Script
- Supply Chain Risk
- Data Exfiltration
- Script Injection
- Payment SDK
- Analytics SDK
- Map SDK
- Chat Widget
- Tag Manager
- CSP Allowlist
- Subresource Integrity
- Consent Management
- Least Privilege

---

### [실무]

작성 기준:

- 필요한 외부 스크립트만 로드
- 민감 페이지에서 Third-party Script 제한
- 결제 / 인증 SDK는 공식 script source만 사용
- Tag Manager로 임의 script 삽입 권한 관리
- CSP `script-src` allowlist 최소화
- SRI 적용 가능 여부 검토
- 사용자 동의 필요한 script는 consent 후 로드
- 외부 SDK에 개인정보 전달 최소화
- SDK 로딩 실패 fallback 처리
- 외부 script 변경은 보안 리뷰 대상

주의:

- Third-party Script는 페이지의 JavaScript 권한을 가질 수 있음
- CSP에 외부 도메인을 추가하면 공격면이 늘어남
- Tag Manager 권한 관리 부실은 큰 위험
- 광고 / 분석 script가 민감 데이터에 접근하지 않도록 설계

---

### [FAQ]

Q. Third-party Script는 왜 위험한가?

A.
브라우저에서 앱과 같은 권한으로 실행되어 DOM, Cookie 접근 가능 범위, 사용자 행동, 네트워크 요청에 영향을 줄 수 있기 때문이다.

Q. Tag Manager는 편리하니까 아무 스크립트나 넣어도 되나?

A.
안 된다. Tag Manager는 강력한 script injection 경로가 될 수 있으므로 권한과 변경 리뷰가 필요하다.

Q. 외부 SDK에 사용자 정보를 넘겨도 되나?

A.
필요 최소한만 전달하고 개인정보, token, 결제 정보는 전달하지 않아야 한다.

---

# 23. Dependency and Supply Chain Security Rules

## 23.1 의존성 / 공급망 보안

### [개념]

Dependency Security는 npm package, build tool, bundler plugin, UI library, polyfill, third-party SDK가 취약점이나 악성 코드를 포함하지 않도록 관리하는 기준이다.

---

### [핵심]

검토 대상:

- npm Package
- Transitive Dependency
- Lockfile
- Package Script
- Postinstall Script
- Typosquatting
- Dependency Confusion
- Vulnerability Audit
- License Risk
- Maintainer Risk
- Package Update
- SCA
- SBOM

---

### [실무]

작성 기준:

- dependency 추가는 리뷰 대상
- 큰 dependency는 필요성과 대체안 검토
- lockfile 변경 리뷰
- 보안 취약점 audit 수행
- postinstall script 주의
- package name typosquatting 확인
- 내부 package와 외부 package 이름 충돌 주의
- 오래된 package / 유지보수 중단 package 확인
- version pinning 전략 검토
- CI에서 dependency audit 실행 가능
- source map / bundle analyzer로 포함 여부 확인

주의:

- frontend dependency는 browser bundle에 포함될 수 있음
- dev dependency도 build pipeline에서 실행되므로 위험할 수 있음
- lockfile 충돌 해결 과정에서 의도치 않은 버전 변경 주의
- npm token / registry 권한 관리 필요

---

### [FAQ]

Q. 프론트엔드 의존성도 보안 위험인가?

A.
그렇다. 브라우저 bundle에 포함되거나 build 과정에서 실행되어 XSS, 데이터 유출, 공급망 공격으로 이어질 수 있다.

Q. Lockfile은 왜 리뷰해야 하나?

A.
의존성 버전과 transitive dependency 변경이 실제 보안과 빌드 결과에 영향을 주기 때문이다.

Q. devDependency는 안전한가?

A.
항상 안전하지 않다. 빌드나 install 과정에서 실행될 수 있으므로 보안 검토가 필요하다.

---

# 24. Source Map and Bundle Exposure Rules

## 24.1 Source Map / Bundle 노출

### [개념]

Source Map and Bundle Exposure는 production bundle과 source map을 통해 내부 코드, API endpoint, feature flag, secret, business logic이 노출되는 위험을 관리하는 기준이다.

---

### [핵심]

검토 대상:

- Production Bundle
- Source Map
- Hidden Source Map
- Public Source Map
- API Endpoint Exposure
- Internal Logic Exposure
- Feature Flag Exposure
- Dead Code
- Debug Code
- Console Log
- Secret in Bundle
- Build Artifact

---

### [실무]

작성 기준:

- production source map 공개 여부 정책 결정
- observability 도구에 비공개 업로드 검토
- source map과 release version 연결
- bundle에 secret 포함 여부 점검
- debug 코드 제거
- console log 제거
- feature flag 값 노출 영향 검토
- 내부 endpoint 노출은 권한 검증으로 보호
- client bundle은 사용자가 볼 수 있다고 가정
- minification은 보안 기능으로 간주하지 않기

주의:

- 숨겼다고 보안이 되는 것은 아님
- 브라우저로 내려간 코드는 분석 가능
- source map 공개는 코드 이해를 쉽게 만듦
- secret은 source map뿐 아니라 bundle에도 들어가면 안 됨

---

### [FAQ]

Q. Source Map을 production에 공개해도 되나?

A.
가능은 하지만 코드 노출 위험이 있으므로 비공개 업로드나 접근 제한을 검토해야 한다.

Q. Minification이 보안인가?

A.
아니다. 코드를 읽기 어렵게 만들 뿐 보안 검증을 대체하지 못한다.

Q. API endpoint가 bundle에 보이면 위험한가?

A.
endpoint 자체 노출보다 서버 인증 / 권한 검증이 없는 것이 위험하다. API는 공개될 수 있다고 보고 보호해야 한다.

---

# 25. Next.js App Router Security Rules

## 25.1 Next.js App Router 보안

### [개념]

Next.js App Router Security는 Server Component, Client Component, Server Action, Route Handler, Middleware / Proxy, Environment Variable, Cache 정책에서 발생할 수 있는 보안 위험을 관리하는 기준이다.

---

### [핵심]

검토 대상:

- Server Component
- Client Component
- Server Action
- Route Handler
- Middleware / Proxy
- `use client`
- Environment Variable
- Server-only Code
- Client Bundle
- Cache
- Revalidation
- Dynamic Rendering
- Static Rendering
- Data Leakage
- Auth Check
- Authorization Check

---

### [실무]

작성 기준:

- Server Component에서 가져온 민감 데이터를 Client Component props로 넘기지 않기
- Client Component는 브라우저 bundle로 내려간다고 가정
- Server Action 내부에서 인증 / 권한 재검증
- Route Handler는 일반 API처럼 인증 / 권한 검증
- Middleware / Proxy는 보조 guard이며 최종 권한 검증 대체 불가
- `NEXT_PUBLIC_` env는 공개 값
- server-only secret은 client import 경계에서 차단
- 사용자별 데이터는 public cache 금지
- static rendering에 사용자별 데이터 섞임 주의
- revalidation endpoint 보안 검증

위험 예시:

```tsx
<ClientProfile user={{ email: user.email, internalRole: user.internalRole }} />
```

안전 기준:

```text
Client Component에는 화면에 필요한 최소 데이터만 전달
권한 검증은 Server Action / Route Handler / Backend에서 재수행
```

---

### [FAQ]

Q. Server Component에서 가져온 데이터는 모두 안전한가?

A.
아니다. Client Component props로 전달되는 순간 브라우저에 노출될 수 있으므로 필요한 최소 데이터만 전달해야 한다.

Q. Server Action은 안전한 서버 함수인가?

A.
서버에서 실행되지만 public endpoint처럼 취급해야 하며 내부에서 인증 / 권한 검증이 필요하다.

Q. Middleware만으로 보호 route 보안이 충분한가?

A.
아니다. Middleware는 보조 방어층이고 실제 데이터 접근 지점에서 권한 검증이 필요하다.

---

# 26. Server Action Security Rules

## 26.1 Server Action 보안 기준

### [개념]

Server Action은 서버에서 실행되는 mutation 함수이지만 클라이언트에서 호출될 수 있으므로 일반 API endpoint와 같은 보안 기준으로 검토해야 한다.

---

### [핵심]

필수 포함:

- Server Action
- Public Endpoint Assumption
- Authentication Check
- Authorization Check
- Input Validation
- CSRF Consideration
- Rate Limit
- Error Sanitization
- Revalidation
- Audit Log
- Sensitive Mutation
- Idempotency

---

### [실무]

작성 기준:

- Action 내부에서 current user 확인
- Action 내부에서 role / permission 검증
- 입력값 schema validation
- 서버에서 business rule 검증
- 민감 mutation은 rate limit / audit log 검토
- 에러 메시지는 안전하게 반환
- mutation 후 필요한 revalidation 수행
- request origin / CSRF 위험 검토
- action 함수를 client에서 호출 가능하다고 가정
- 페이지에서 이미 인증 확인했어도 action에서 재검증

예시:

```ts
"use server";

export async function deletePostAction(postId: string) {
  const user = await requireUser();
  await assertCanDeletePost(user.id, postId);

  await deletePost(postId);
}
```

주의:

- 숨겨진 form field를 신뢰하지 않기
- client에서 전달된 userId / role 신뢰 금지
- action error에 내부 정보 노출 금지
- 관리자 action은 특히 권한 검증 필수

---

### [FAQ]

Q. Server Action 내부에서도 권한 검증을 해야 하나?

A.
반드시 해야 한다. 페이지에서 인증을 확인했더라도 Server Action은 별도의 호출 지점으로 취급해야 한다.

Q. Client가 보낸 userId를 믿어도 되나?

A.
안 된다. 현재 사용자는 서버 세션에서 확인해야 한다.

Q. Server Action 에러를 그대로 반환해도 되나?

A.
권장하지 않는다. 사용자에게는 안전한 메시지를 반환하고 상세 오류는 서버 로그에 남긴다.

---

# 27. Route Handler and API Client Security Rules

## 27.1 Route Handler / API Client 보안

### [개념]

Route Handler는 Next.js App Router에서 API endpoint 역할을 수행하며, API Client는 프론트엔드에서 Backend API와 통신하는 계층이다.

둘 다 인증, 권한, 입력 검증, 에러 처리, 민감정보 보호 기준이 필요하다.

---

### [핵심]

Route Handler 기준:

- Authentication
- Authorization
- Input Validation
- Rate Limit
- Method Check
- Error Sanitization
- CSRF Check
- CORS Check
- Audit Log
- Secure Response

API Client 기준:

- Auth Header
- Token Refresh
- Error Normalization
- Sensitive Data Masking
- Timeout
- Retry Policy
- Trace ID
- 401 / 403 Handling

---

### [실무]

작성 기준:

- Route Handler는 Backend API처럼 검증
- HTTP method별 허용 작업 명확화
- 상태 변경 요청은 인증 / 권한 필수
- request body schema validation
- 응답에 민감정보 포함 금지
- API Client는 token을 log하지 않음
- Authorization header masking
- 401 / 403 처리 분리
- refresh token 중복 요청 방지
- retry는 idempotent 요청 중심
- timeout 설정
- error response를 사용자용 메시지로 변환

---

### [FAQ]

Q. Route Handler도 서버니까 안전한가?

A.
서버에서 실행되지만 외부에서 호출 가능한 endpoint이므로 인증, 권한, 입력 검증이 필요하다.

Q. API Client에서 에러를 그대로 보여줘도 되나?

A.
권장하지 않는다. 서버 내부 메시지는 사용자에게 노출하지 않고 안전한 메시지로 변환해야 한다.

Q. Retry는 모든 API에 적용해도 되나?

A.
아니다. 중복 결제나 중복 생성 같은 위험이 있으므로 idempotent 요청 중심으로 적용해야 한다.

---

# 28. Logging and Observability Security Rules

## 28.1 로그 / 관측 데이터 보안

### [개념]

Logging and Observability Security는 Error Monitoring, Session Replay, Web Vitals, API Logging 과정에서 개인정보와 민감정보가 수집되지 않도록 제한하는 기준이다.

---

### [핵심]

보호 대상:

- Token
- Cookie
- Authorization Header
- Password
- Email
- Phone Number
- Address
- Payment Info
- Personal Identifier
- Search Query
- Form Input
- Session Replay DOM
- API Request Body
- API Response Body

---

### [실무]

작성 기준:

- Authorization header logging 금지
- request / response body 전체 logging 금지
- error context에 raw object 넣지 않기
- 사용자 입력값 masking
- URL query sanitization
- session replay input masking
- 결제 / 개인정보 페이지 replay 제외 검토
- source map 비공개 업로드
- release / route / status code 중심 수집
- 개인정보 수집 동의 / 보관 기간 검토
- observability tool 접근 권한 제한

예시:

```ts
function redact(value: string) {
  return value.replace(/Bearer\s+[A-Za-z0-9._-]+/g, "Bearer [REDACTED]");
}
```

---

### [FAQ]

Q. API 요청 body를 Observability에 저장해도 되나?

A.
권장하지 않는다. 개인정보와 민감정보가 포함될 가능성이 높으므로 최소 정보만 수집해야 한다.

Q. Session Replay는 보안 위험이 있나?

A.
그렇다. 화면에 표시된 개인정보가 기록될 수 있으므로 masking, sampling, 접근 제한이 필요하다.

Q. Error context에 user 객체를 통째로 넣어도 되나?

A.
안 된다. 필요한 최소 식별자만 넣고 개인정보는 제거해야 한다.

---

# 29. Privacy Rules

## 29.1 개인정보 보호 기준

### [개념]

Privacy는 사용자의 개인정보와 민감 정보가 프론트엔드 코드, 로그, URL, 저장소, third-party SDK, analytics, session replay로 과도하게 수집되거나 노출되지 않도록 하는 기준이다.

---

### [핵심]

검토 대상:

- PII
- Sensitive Data
- Consent
- Data Minimization
- Purpose Limitation
- Retention
- Masking
- Redaction
- Analytics Event
- Session Replay
- Third-party SDK
- URL Query
- Browser Storage
- Clipboard
- Download

---

### [실무]

작성 기준:

- 필요한 데이터만 수집
- 수집 목적이 명확한 데이터만 사용
- 개인정보는 localStorage에 저장하지 않기
- URL query에 개인정보 넣지 않기
- analytics event에 email / phone / address 넣지 않기
- third-party SDK에 전달하는 user 정보 최소화
- session replay masking 적용
- 클립보드 복사 기능은 사용자 의도 기반
- 민감정보 화면은 screenshot / replay / logging 주의
- 데이터 보관 기간과 접근 권한 정의

주의:

- 개인정보는 보안뿐 아니라 법적 / 정책적 문제
- 내부 관리자도 필요한 범위만 접근
- 개발 / 테스트 데이터에도 실제 개인정보 사용 금지
- 사용자 동의가 필요한 추적은 동의 전 수집 금지

---

### [FAQ]

Q. Analytics event에 사용자 이메일을 넣어도 되나?

A.
권장하지 않는다. 내부 익명 ID나 hash를 사용하고 직접 식별 정보는 피해야 한다.

Q. URL에 검색어를 넣는 것은 괜찮나?

A.
일반 검색어는 가능하지만 개인정보나 민감한 검색어가 될 수 있으므로 logging / analytics / referrer 노출을 고려해야 한다.

Q. 개인정보 보호는 프론트엔드에서도 중요한가?

A.
매우 중요하다. 브라우저 저장소, URL, 로그, analytics, session replay에서 개인정보가 쉽게 노출될 수 있다.

---

# 30. Security Testing Rules

## 30.1 프론트엔드 보안 테스트

### [개념]

Frontend Security Testing은 XSS, 인증 흐름, 권한 UI, token 저장, CSP, dependency, redirect, file upload, error leakage를 검증하는 과정이다.

---

### [핵심]

테스트 대상:

- XSS Rendering Test
- DOM XSS Test
- Sanitization Test
- CSP Violation Test
- Auth Flow Test
- Protected Route Test
- Authorization UI Test
- Server Action Authorization Test
- CSRF Scenario Test
- Safe Redirect Test
- File Upload Validation Test
- Dependency Audit
- Secret Scan
- Source Map Exposure Check
- Security Header Check

---

### [실무]

테스트 기준:

- 사용자 입력이 텍스트로 렌더링되는지 확인
- `dangerouslySetInnerHTML` 사용처 리뷰
- Markdown / Rich Text sanitizer 테스트
- unauthorized user가 API / action 호출 가능한지 테스트
- role 없는 사용자가 admin action 호출 가능한지 테스트
- redirect URL allowlist 테스트
- file type / size validation 테스트
- CSP report 확인
- dependency audit 실행
- bundle에 secret 포함 여부 검사
- error message에 내부 정보 노출 여부 확인
- e2e에서 인증 만료 / 권한 없음 flow 테스트

주의:

- 클라이언트 테스트만으로 보안 검증 완료 아님
- 서버 권한 테스트와 함께 수행
- 테스트에 실제 token / secret 사용 금지
- 공격 payload 예시는 안전하고 최소화된 수준으로만 사용

---

### [FAQ]

Q. 프론트엔드 보안 테스트는 무엇부터 해야 하나?

A.
XSS 위험 렌더링, 인증 / 권한 flow, token 저장, redirect, CSP, dependency audit, secret scan부터 확인한다.

Q. 권한 테스트는 프론트에서만 하면 되나?

A.
아니다. UI 숨김 테스트와 함께 API / Server Action 직접 호출 권한 테스트가 필요하다.

Q. CSP는 어떻게 테스트하나?

A.
Report-Only 모드로 위반 리포트를 확인하고 정상 리소스 차단 여부를 점검한 뒤 enforce할 수 있다.

---

# 31. Troubleshooting Rules

## 31.1 자주 발생하는 보안 문제

### [개념]

Troubleshooting 문서는 Agent가 Frontend Security 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- XSS 가능성 발견
- DOM XSS 발생
- CSP 위반 발생
- CSP 적용 후 리소스 차단
- Token이 LocalStorage에 노출
- Secret이 Bundle에 포함됨
- `NEXT_PUBLIC_`에 Secret 포함
- CORS Error 발생
- CSRF 방어 누락
- 권한 없는 API 호출 성공
- Server Action 권한 검증 누락
- Open Redirect 가능
- File Upload Preview XSS
- Source Map 공개 노출
- Error Log에 개인정보 포함
- Session Replay에 민감정보 노출
- Dependency 취약점 발견
- Third-party Script 위험 증가

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

- 사용자 입력이 HTML로 실행될 가능성이 있음

원인:

- dangerouslySetInnerHTML 사용
- Markdown sanitizer 누락
- API 응답 HTML을 그대로 렌더링

해결:

- HTML 렌더링 제거
- 필요한 경우 allowlist 기반 sanitizer 적용
- CSP 추가
- 서버 저장 전 sanitization 검토
```

예시:

```md
문제:

- Secret이 frontend bundle에 포함됨

원인:

- NEXT*PUBLIC* 환경변수에 secret 저장
- client component에서 server-only env import
- build-time config에 secret 포함

해결:

- secret을 server-only 환경변수로 이동
- Route Handler / Backend에서 secret 사용
- bundle analyzer / secret scan 실행
```

예시:

```md
문제:

- 권한 없는 사용자가 Server Action을 호출할 수 있음

원인:

- 페이지에서만 권한 체크
- Server Action 내부 권한 검증 누락
- client에서 전달한 userId를 신뢰

해결:

- Server Action 내부에서 requireUser 호출
- 서버 세션 기준으로 권한 검증
- client-provided role / userId 신뢰 금지
```

---

### [FAQ]

Q. CORS 에러가 나면 보안이 강화된 것인가?

A.
그렇게 단정할 수 없다. CORS 설정 문제일 수 있으며 인증 / 권한 검증과는 별개이다.

Q. CSP 적용 후 이미지가 안 나오면 어떻게 하나?

A.
`img-src` directive에 필요한 이미지 도메인이 포함되어 있는지 확인한다.

Q. Secret이 bundle에 들어갔으면 어떻게 해야 하나?

A.
즉시 secret rotate, bundle에서 제거, server-only로 이동, 배포 이력과 로그 노출 범위 확인이 필요하다.

---

# 32. Code Example Rules

## 32.1 코드 예제 작성 기준

### [개념]

Frontend Security 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 안전해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React / Next.js 기준 예제 우선
- 방어 코드 중심
- 공격 payload 상세 예제 최소화
- Secret 하드코딩 금지
- Token logging 금지
- 개인정보 포함 금지
- `dangerouslySetInnerHTML`은 위험 예시로만 제한
- Server Action 권한 검증 예제 포함 권장
- Safe Redirect 예제 포함 권장
- Sanitization / Validation 예제 포함 권장
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Safe text rendering
- URL allowlist validation
- Safe redirect helper
- Server Action authorization
- API Client error redaction
- Cookie security 설명
- CSP header 예시
- File type allowlist
- PII redaction helper
- Auth guard + server verification flow
- `postMessage` origin check
- Source Map private upload flow 요약

금지 예제:

- 실제 XSS payload 실행 예제
- token / password / API key 하드코딩
- LocalStorage token 저장을 기본 권장하는 예제
- 권한 검증 없는 Server Action
- 사용자 HTML을 그대로 렌더링하는 예제
- 모든 origin을 허용하는 CORS 예제
- CSRF 방어 없는 cookie mutation 예제
- request body 전체 logging 예제

---

### [FAQ]

Q. Frontend Security 코드 예제는 공격 예제를 자세히 넣어야 하나?

A.
아니다. 방어 기준과 안전한 구현 예제를 중심으로 작성하고 공격 payload는 최소화한다.

Q. LocalStorage token 예제를 넣어도 되나?

A.
넣을 수는 있지만 위험과 대안을 함께 명시해야 하며 기본 권장 패턴처럼 작성하면 안 된다.

---

# 33. Comparison Rules

## 33.1 필수 비교 대상

### [개념]

Frontend Security 문서는 Agent의 보안 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- XSS vs CSRF
- Stored XSS vs Reflected XSS vs DOM XSS
- Validation vs Sanitization vs Encoding
- LocalStorage vs SessionStorage vs HttpOnly Cookie
- Access Token vs Refresh Token
- Cookie Auth vs Bearer Token Auth
- Authentication vs Authorization
- 401 vs 403
- CORS vs CSRF
- CSP Report-Only vs Enforced CSP
- Public Env vs Server-only Env
- Client Guard vs Server Authorization
- Server Component vs Client Component Security
- Server Action vs Route Handler
- SameSite Lax vs Strict vs None
- Public Cache vs Private Cache
- Source Map Public vs Private Upload
- Analytics Event vs Security Log
- Third-party Script vs First-party Script

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 위험 / 사용 시점 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. XSS와 CSRF 차이는?

A.
XSS는 브라우저에서 악성 스크립트를 실행시키는 공격이고, CSRF는 사용자의 인증 상태를 악용해 원치 않는 요청을 보내는 공격이다.

Q. Authentication과 Authorization 차이는?

A.
Authentication은 사용자가 누구인지 확인하는 것이고, Authorization은 해당 사용자가 어떤 작업을 할 수 있는지 확인하는 것이다.

Q. Validation과 Sanitization 차이는?

A.
Validation은 입력이 규칙에 맞는지 검사하는 것이고, Sanitization은 위험한 내용을 제거하거나 안전하게 변환하는 것이다.

---

# 34. Checklist Rules

## 34.1 문서 품질 체크리스트

### [개념]

Frontend Security RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Security 목적이 명확한가?
- [ ] OWASP / Web Security 기준을 반영했는가?
- [ ] XSS / DOM XSS 방어 기준을 포함했는가?
- [ ] HTML Sanitization 기준을 포함했는가?
- [ ] CSP / Security Header 기준을 포함했는가?
- [ ] CSRF 기준을 포함했는가?
- [ ] Cookie Security 기준을 포함했는가?
- [ ] Token Storage 비교 기준을 포함했는가?
- [ ] Authentication Flow 기준을 포함했는가?
- [ ] Authorization UI와 Server Authorization 차이를 포함했는가?
- [ ] Secret / Environment Variable 노출 방지 기준을 포함했는가?
- [ ] CORS 오해 방지 기준을 포함했는가?
- [ ] Input Validation / Output Encoding 기준을 포함했는가?
- [ ] Safe Redirect 기준을 포함했는가?
- [ ] File Upload 보안 기준을 포함했는가?
- [ ] Third-party Script 보안 기준을 포함했는가?
- [ ] Dependency / Supply Chain 보안 기준을 포함했는가?
- [ ] Source Map / Bundle 노출 기준을 포함했는가?
- [ ] Next.js App Router Security 기준을 포함했는가?
- [ ] Server Action Security 기준을 포함했는가?
- [ ] Logging / Observability Security 기준을 포함했는가?
- [ ] Privacy 기준을 포함했는가?
- [ ] Security Testing 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 공격 payload를 불필요하게 상세히 제공하지 않았는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Frontend Architecture / Next.js / Observability 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- 보안 문서는 안전한 방어 기준 중심으로 작성
- App Router / Architecture / Observability / Performance 문서와 연계 가능해야 함

---

### [FAQ]

Q. Frontend Security 문서 품질에서 가장 중요한 것은?

A.
XSS, CSRF, Token, Secret, CSP, 권한 검증, 개인정보, Next.js Server Action 보안 기준이 명확해야 한다.

---

# 35. Retrieval Optimization Rules

## 35.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Security
- Web Security
- OWASP Top 10
- XSS
- DOM XSS
- Cross-site Scripting
- CSRF
- Content Security Policy
- CSP
- Trusted Types
- Security Headers
- Cookie Security
- HttpOnly Cookie
- Secure Cookie
- SameSite Cookie
- Token Storage
- LocalStorage Token
- SessionStorage Token
- Memory Token
- Access Token
- Refresh Token
- JWT
- Authentication Flow
- Authorization UI
- Server-side Authorization
- Protected Route
- Secret Exposure
- Environment Variable
- `NEXT_PUBLIC_`
- CORS
- Same-Origin Policy
- Input Validation
- Output Encoding
- HTML Sanitization
- Safe Redirect
- Open Redirect
- File Upload Security
- Third-party Script Security
- Dependency Security
- Supply Chain Security
- Source Map Exposure
- Next.js Security
- Server Action Security
- Route Handler Security
- Privacy
- PII Masking
- Security Review

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Frontend Security는 뭐야?
- React에서 XSS 막는 방법
- dangerouslySetInnerHTML 안전하게 쓰는 법
- DOM XSS는 어떻게 막아?
- CSP는 왜 필요해?
- CSRF는 언제 발생해?
- CORS와 CSRF 차이
- Token은 어디에 저장해야 해?
- LocalStorage에 JWT 저장해도 돼?
- HttpOnly Cookie가 안전해?
- SameSite Cookie는 뭐야?
- NEXT_PUBLIC에 secret 넣어도 돼?
- 프론트엔드에 API Secret 넣어도 돼?
- 버튼 숨기면 권한 처리 된 거야?
- Server Action 권한 검증 해야 해?
- Route Handler 보안은 어떻게 해?
- 사용자별 데이터 cache해도 돼?
- Open Redirect 어떻게 막아?
- 파일 업로드 보안 어떻게 해?
- Source Map 공개해도 돼?
- Session Replay 개인정보 어떻게 막아?
- Third-party Script는 왜 위험해?
- Frontend Security 코드 리뷰 기준은?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 36. Version Rules

## 36.1 기준 버전

### [개념]

Frontend Security 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern Web Security
- OWASP Top 10 2025
- React 19+
- Next.js App Router
- TypeScript
- Server Component
- Client Component
- Server Action
- Route Handler
- CSP
- Trusted Types
- Secure Cookie
- SameSite Cookie
- HttpOnly Cookie
- Privacy-first Logging
- Dependency Security
- Supply Chain Security

Legacy 제외:

- jQuery 기반 DOM 조작 중심 보안
- Client-only Authorization
- LocalStorage Token을 무조건 권장하는 방식
- Secret을 Frontend Bundle에 포함하는 구조
- CORS를 권한 검증으로 오해하는 설명
- CSP 없이 HTML 삽입 허용
- 서버 검증 없는 Form / Server Action
- 공격 payload 상세 나열 중심 문서
- 개인정보를 log / analytics에 직접 저장하는 방식
- Source Map 공개를 기본값으로 권장하는 방식

---

### [실무]

문서 작성 시 주의:

- OWASP / MDN / Next.js 공식 문서 기준을 우선
- 브라우저 보안 정책과 프레임워크 동작은 버전별 변화 가능성 있음
- Next.js App Router의 Server Action / Cache / Server Component 보안 기준은 최신 문서 확인 필요
- Frontend Security는 Backend Security와 함께 설계해야 함
- 공격 방법 상세보다 방어 기준과 리뷰 기준 중심
- 프로젝트 보안 정책 / 법적 요구사항 / 개인정보 정책 확인 필요

---

### [FAQ]

Q. Frontend Security 문서는 최신성이 중요한가?

A.
중요하다. 브라우저 보안 정책, Next.js 보안 모델, OWASP 기준, dependency 취약점은 계속 변하므로 최신 공식 문서 확인이 필요하다.

Q. 특정 보안 도구 기준으로 작성해야 하나?

A.
아니다. 도구보다 XSS, CSRF, Token, Cookie, CSP, 권한 검증, 개인정보 보호 기준을 중심으로 작성한다.

---

# 37. Common Mistakes

## 37.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Frontend Security 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- React가 모든 XSS를 막는다고 오해
- `dangerouslySetInnerHTML`에 사용자 HTML 삽입
- Markdown / Rich Text sanitizer 누락
- URL query 값을 HTML로 직접 삽입
- `innerHTML`에 외부 데이터 삽입
- CSP 미적용
- `unsafe-inline` / `unsafe-eval` 남용
- Token을 LocalStorage에 저장하고 XSS 방어 없음
- Token을 URL query로 전달
- `NEXT_PUBLIC_`에 secret 저장
- client bundle에 server secret 포함
- 버튼 숨김만으로 권한 처리
- Server Action 내부 권한 검증 누락
- Route Handler 입력 검증 누락
- CORS를 권한 검증으로 오해
- CSRF 방어 없이 Cookie 기반 mutation 처리
- Open Redirect 검증 누락
- 파일명 / 업로드 preview escaping 누락
- SVG 업로드 위험 무시
- Third-party Script 무분별 로드
- Source Map 공개 노출
- Error log에 개인정보 포함
- Session Replay masking 누락
- Dependency audit 미수행
- Client에서 role / userId를 신뢰

---

### [실무]

리뷰 기준:

- 사용자 입력 렌더링 위치 확인
- HTML 삽입 여부 확인
- Sanitizer 적용 여부 확인
- CSP / Security Header 확인
- Token 저장 위치 확인
- Cookie 속성 확인
- Secret bundle 포함 여부 확인
- 인증 / 권한 서버 검증 확인
- Server Action / Route Handler 권한 확인
- CORS / CSRF 구분 확인
- Redirect allowlist 확인
- File Upload validation 확인
- Third-party Script allowlist 확인
- Dependency audit 확인
- Log / Observability PII 확인

---

### [FAQ]

Q. Frontend Security에서 가장 흔한 실수는?

A.
클라이언트를 신뢰하고, 버튼 숨김이나 프론트 검증만으로 보안이 된다고 생각하는 것이다.

Q. React 프로젝트에서 가장 조심할 XSS 지점은?

A.
`dangerouslySetInnerHTML`, Markdown / Rich Text 렌더링, URL 기반 DOM 조작, Third-party Script이다.

Q. Next.js 프로젝트에서 자주 하는 보안 실수는?

A.
Server Action 내부 권한 검증 누락, `NEXT_PUBLIC_` secret 노출, 사용자별 데이터 cache 오용이다.

---

# 38. Final Goal

## 38.1 최종 목표

### [개념]

Frontend Security RAG 문서는 Agent가 React / Next.js 기반 프론트엔드 프로젝트의 보안 위험을 설계, 생성, 검토, 진단할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Frontend Threat Modeling 수행
- XSS / DOM XSS 위험 진단
- HTML Sanitization 기준 제안
- CSP / Security Header 기준 제안
- CSRF 위험 판단
- Cookie Security 검토
- Token Storage 전략 비교
- Authentication Flow 보안 리뷰
- Authorization UI와 Server Authorization 경계 검토
- Secret / Environment Variable 노출 진단
- CORS 오해 방지
- Input Validation / Output Encoding 리뷰
- Safe Redirect 검토
- File Upload 보안 리뷰
- Third-party Script 보안 리뷰
- Dependency / Supply Chain 보안 리뷰
- Source Map / Bundle 노출 검토
- Next.js App Router Security 리뷰
- Server Action 권한 검증 리뷰
- Route Handler 보안 리뷰
- Logging / Observability 개인정보 노출 검토
- Security Testing 기준 제안
- Frontend Security 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- 공격 payload 상세 제공 지양
- XSS / CSRF / Token / Secret / 권한 / 개인정보 경계 명확화
- Next.js App Router / Frontend Architecture / Observability 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Security Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 XSS, CSRF, Token, Secret, 인증 / 권한, CSP, CORS, 개인정보, Next.js Server Action 보안 문제를 설계 단계와 코드 리뷰 단계에서 발견하고 방어 기준을 제안하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Security 문서는 어떤 기준으로 작성해야 해?

A.
XSS, DOM XSS, CSRF, Token Storage, Cookie Security, CSP, Secret 노출, 인증 / 권한, CORS, 개인정보, Next.js Server Action 보안 중심으로 작성해야 한다.

Q. Frontend Security는 뭐야?

A.
브라우저에서 실행되는 프론트엔드 코드와 UI 흐름에서 XSS, CSRF, Token 노출, Secret 노출, 권한 오류, 개인정보 노출을 줄이는 보안 영역이다.

Q. 프론트엔드 보안만 잘하면 서버 보안 필요 없어?

A.
아니다. 프론트엔드 보안은 공격면을 줄이고 UX를 보호하는 것이며 실제 데이터와 권한은 서버에서 검증해야 한다.

Q. React에서 XSS 막는 방법은?

A.
일반 텍스트는 JSX escaping을 사용하고, HTML 직접 삽입을 피하며, Markdown / Rich Text는 sanitizer를 적용하고, CSP를 함께 사용한다.

Q. React를 쓰면 XSS가 자동으로 다 막혀?

A.
아니다. `dangerouslySetInnerHTML`, URL 삽입, DOM API, Markdown 렌더링, Third-party Script는 별도 검토가 필요하다.

Q. dangerouslySetInnerHTML 안전하게 쓰는 법은?

A.
가능하면 피하고, 꼭 필요하면 allowlist 기반 sanitizer, URL scheme 검증, CSP, 입력 출처 제한을 함께 적용한다.

Q. DOM XSS는 어떻게 막아?

A.
URL, localStorage, postMessage, API 응답을 `innerHTML` 같은 위험 sink에 넣지 말고 text rendering, sanitizer, Trusted Types를 사용한다.

Q. innerHTML은 왜 위험해?

A.
신뢰할 수 없는 값이 HTML로 해석되어 스크립트 실행이나 DOM 변조로 이어질 수 있기 때문이다.

Q. Markdown은 안전해?

A.
항상 안전하지 않다. HTML 허용 옵션이나 plugin 때문에 XSS 위험이 생길 수 있으므로 sanitizer가 필요하다.

Q. HTML Sanitization은 언제 필요해?

A.
사용자 작성 HTML, Markdown, Rich Text, CMS 콘텐츠, 외부 HTML을 렌더링할 때 필요하다.

Q. CSP는 왜 필요해?

A.
XSS가 발생하더라도 스크립트 실행과 외부 전송을 제한해 피해를 줄이는 방어층으로 필요하다.

Q. CSP만 있으면 XSS가 해결돼?

A.
아니다. 입력 검증, 출력 encoding, sanitization, 안전한 DOM API 사용이 함께 필요하다.

Q. unsafe-inline 써도 돼?

A.
권장하지 않는다. 가능하면 nonce나 hash 기반 정책을 검토해야 한다.

Q. Trusted Types는 뭐야?

A.
위험한 DOM sink에 문자열을 직접 넣는 것을 제한해 DOM XSS 위험을 줄이는 브라우저 보안 기능이다.

Q. CSRF는 언제 발생해?

A.
Cookie 기반 인증에서 사용자의 인증 상태를 악용해 공격자가 상태 변경 요청을 보내게 할 때 발생할 수 있다.

Q. CSRF는 어떻게 막아?

A.
SameSite Cookie, CSRF Token, Origin / Referer 검증, GET 상태 변경 금지, 서버 검증을 사용한다.

Q. CORS와 CSRF 차이는?

A.
CORS는 브라우저의 응답 접근 제어이고, CSRF는 사용자의 인증 상태를 악용해 요청을 보내는 공격이다.

Q. CORS 설정하면 보안 끝이야?

A.
아니다. CORS는 권한 검증이 아니며 API 서버의 인증 / 권한 검증이 필수이다.

Q. Token은 어디에 저장해야 해?

A.
보안 요구에 따라 HttpOnly Cookie, memory, localStorage, sessionStorage를 비교해야 하며 Refresh Token은 HttpOnly Cookie를 우선 검토한다.

Q. LocalStorage에 JWT 저장해도 돼?

A.
가능은 하지만 XSS 시 탈취 위험이 크다. 보안 요구가 높으면 HttpOnly Cookie나 memory 저장 전략을 검토한다.

Q. SessionStorage는 LocalStorage보다 안전해?

A.
탭 종료 시 사라지는 차이는 있지만 XSS로 읽힐 수 있다는 점은 같다.

Q. HttpOnly Cookie가 안전해?

A.
JS 탈취 위험을 줄이지만 XSS 자체를 막지는 못하며 Cookie 기반 인증에서는 CSRF도 고려해야 한다.

Q. SameSite Cookie는 뭐야?

A.
Cross-site 요청에서 Cookie가 전송되는 범위를 제한해 CSRF 위험을 줄이는 Cookie 속성이다.

Q. 인증 쿠키에는 어떤 속성이 필요해?

A.
일반적으로 HttpOnly, Secure, SameSite, 적절한 Path / Domain / Expiration 설정이 필요하다.

Q. Access Token과 Refresh Token은 어떻게 다뤄?

A.
Access Token은 짧게, Refresh Token은 더 안전한 저장소에 두고 rotation과 만료 처리를 서버 기준으로 설계한다.

Q. Token을 URL에 넣어도 돼?

A.
안 된다. browser history, referrer, log, analytics에 노출될 수 있다.

Q. NEXT_PUBLIC에 secret 넣어도 돼?

A.
안 된다. `NEXT_PUBLIC_` 값은 브라우저 bundle에 포함되어 사용자에게 노출될 수 있다.

Q. 프론트엔드에 API Secret 넣어도 돼?

A.
안 된다. API Secret, private key, payment secret, OAuth client secret은 서버에서만 사용해야 한다.

Q. Public API Key는 secret이야?

A.
브라우저에서 쓰도록 설계된 key는 secret이 아닐 수 있지만 허용 도메인, 사용량 제한, 권한 제한을 설정해야 한다.

Q. 버튼 숨기면 권한 처리 된 거야?

A.
아니다. 버튼 숨김은 UX이고 실제 권한 검사는 서버 API, Server Action, Route Handler에서 수행해야 한다.

Q. Authentication과 Authorization 차이는?

A.
Authentication은 사용자가 누구인지 확인하는 것이고, Authorization은 어떤 작업을 할 수 있는지 확인하는 것이다.

Q. 401과 403 차이는?

A.
401은 인증되지 않은 상태이고, 403은 인증은 되었지만 권한이 없는 상태이다.

Q. JWT payload를 decode해서 권한 판단해도 돼?

A.
UI 표시에는 참고할 수 있지만 실제 권한 판단은 서버에서 서명과 권한을 검증해야 한다.

Q. Server Action 권한 검증 해야 해?

A.
반드시 해야 한다. Server Action은 public endpoint처럼 취급하고 내부에서 인증 / 권한 / 입력 검증을 수행해야 한다.

Q. Server Action에서 client가 보낸 userId 믿어도 돼?

A.
안 된다. 현재 사용자는 서버 세션에서 확인해야 한다.

Q. Route Handler 보안은 어떻게 해?

A.
일반 API처럼 인증, 권한, 입력 검증, method 검증, error sanitization, rate limit을 적용한다.

Q. Middleware만으로 protected route 보안 충분해?

A.
아니다. Middleware는 보조 방어층이고 실제 데이터 접근 지점에서 권한 검증이 필요하다.

Q. 사용자별 데이터 cache해도 돼?

A.
public cache는 금지해야 한다. private cache, no-store, Dynamic Rendering을 고려해야 한다.

Q. Input Validation은 프론트에서만 해도 돼?

A.
아니다. 프론트 검증은 UX용이고 서버 검증이 보안 기준이다.

Q. Validation과 Sanitization 차이는?

A.
Validation은 규칙 검증이고, Sanitization은 위험한 내용을 제거하거나 안전하게 변환하는 것이다.

Q. Output Encoding은 왜 필요해?

A.
사용자 입력이 HTML이나 Script로 해석되지 않고 안전한 텍스트로 표시되도록 하기 위해 필요하다.

Q. URL도 검증해야 해?

A.
그렇다. `javascript:`, `data:` 같은 위험 scheme을 차단하고 허용된 URL만 사용해야 한다.

Q. Open Redirect 어떻게 막아?

A.
redirect 대상은 상대 경로 또는 허용된 도메인 allowlist만 허용하고 외부 URL은 차단한다.

Q. 로그인 후 returnUrl은 어떻게 처리해?

A.
내부 상대 경로만 허용하거나 allowlist 도메인만 허용해야 한다.

Q. 파일 업로드 보안 어떻게 해?

A.
프론트에서 파일 크기, 확장자, MIME type을 검증하고 서버에서 다시 검증하며 SVG / HTML preview는 특히 주의한다.

Q. SVG 업로드는 왜 위험해?

A.
SVG는 script나 외부 리소스를 포함할 수 있어 XSS 위험이 있다.

Q. 파일명도 escaping해야 해?

A.
그렇다. 파일명에 HTML이나 특수문자가 포함될 수 있으므로 화면 출력 시 안전하게 처리해야 한다.

Q. Third-party Script는 왜 위험해?

A.
브라우저에서 앱과 같은 권한으로 실행되어 DOM, 사용자 행동, 네트워크 요청에 영향을 줄 수 있기 때문이다.

Q. Tag Manager에 아무 스크립트나 넣어도 돼?

A.
안 된다. Tag Manager는 강력한 script injection 경로가 될 수 있으므로 권한과 변경 리뷰가 필요하다.

Q. 외부 SDK에 사용자 정보를 넘겨도 돼?

A.
필요 최소한만 전달하고 개인정보, token, 결제 정보는 전달하지 않아야 한다.

Q. Dependency 보안은 왜 중요해?

A.
프론트엔드 의존성은 브라우저 bundle이나 build 과정에 포함되어 공급망 공격과 취약점 위험을 만들 수 있다.

Q. Lockfile은 왜 리뷰해?

A.
의존성 버전과 transitive dependency 변경이 실제 보안과 빌드 결과에 영향을 주기 때문이다.

Q. devDependency는 안전해?

A.
항상 안전하지 않다. install이나 build 과정에서 실행될 수 있으므로 보안 검토가 필요하다.

Q. Source Map 공개해도 돼?

A.
가능은 하지만 코드 노출 위험이 있으므로 비공개 업로드나 접근 제한을 검토해야 한다.

Q. Minification은 보안이야?

A.
아니다. 코드를 읽기 어렵게 만들 뿐 보안 검증을 대체하지 못한다.

Q. API endpoint가 bundle에 보이면 위험해?

A.
endpoint 노출 자체보다 서버 인증 / 권한 검증이 없는 것이 위험하다. API는 공개될 수 있다고 보고 보호해야 한다.

Q. Error log에 개인정보 넣어도 돼?

A.
안 된다. token, password, email, phone, address, 결제 정보, request body는 masking하거나 수집하지 않아야 한다.

Q. Session Replay 개인정보 어떻게 막아?

A.
input masking, text masking, 민감 페이지 제외, 접근 권한 제한, 보관 기간 제한을 적용한다.

Q. Analytics event에 이메일 넣어도 돼?

A.
권장하지 않는다. 내부 익명 ID나 hash를 사용하고 직접 식별 정보는 피해야 한다.

Q. URL query에 개인정보 넣어도 돼?

A.
권장하지 않는다. log, referrer, analytics, history에 노출될 수 있다.

Q. 프론트엔드 보안 테스트는 무엇부터 해?

A.
XSS 렌더링, 인증 / 권한 flow, token 저장, redirect, CSP, dependency audit, secret scan부터 확인한다.

Q. CSP는 어떻게 테스트해?

A.
Report-Only 모드로 위반 리포트를 확인하고 정상 리소스 차단 여부를 점검한 뒤 enforce할 수 있다.

Q. Secret이 bundle에 들어갔으면 어떻게 해?

A.
즉시 secret rotate, bundle에서 제거, server-only로 이동, 배포 이력과 로그 노출 범위 확인이 필요하다.

Q. Frontend Security 코드 리뷰 기준은?

A.
사용자 입력 렌더링, HTML 삽입, token 저장, secret 노출, 권한 서버 검증, CSP, CORS / CSRF, redirect, file upload, logging PII를 확인한다.

Q. Frontend Security RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 XSS, CSRF, Token, Secret, 인증 / 권한, CSP, CORS, 개인정보, Next.js Server Action 보안 문제를 설계 단계와 코드 리뷰 단계에서 발견하고 방어 기준을 제안하게 만드는 것이다.
