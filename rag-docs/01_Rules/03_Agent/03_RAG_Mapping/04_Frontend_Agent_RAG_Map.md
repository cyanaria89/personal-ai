# 04. Frontend Agent RAG Map

## 1. 목적

Frontend Agent는 React 기반 화면 구조, 컴포넌트 설계, 라우팅, 상태 관리, API 연동, 폼/검증, UX 처리를 담당한다.

Backend API와 연결되는 경우 Backend Agent의 API Contract를 우선 확인한다.

## 2. Required Master Documents

```text
01_Master/Agent_Build_Context.md
01_Master/Master_RAG_Rules.md
01_Master/Project_Progress.md
01_Master/RAG_Document_Operation_Rules_Addendum.md
```

## 3. Required Agent Documents

```text
Agent_Rules_v1/00_Common_Agent_Rules.md
Agent_Rules_v1/04_Frontend_Agent_Rules.md
Agent_System_Prompts_v1/00_Common_System_Prompt.md
Agent_System_Prompts_v1/04_Frontend_Agent_System_Prompt.md
```

## 4. Primary Domain Rules

```text
03_Frontend/01_HTML_CSS_Foundation_Domain_Rules.md
03_Frontend/02_JavaScript_Foundation_Domain_Rules.md
03_Frontend/03_TypeScript_Foundation_Domain_Rules.md
03_Frontend/04_React_Core_Domain_Rules.md
03_Frontend/05_React_Component_Design_Domain_Rules.md
03_Frontend/06_React_Router_Domain_Rules.md
03_Frontend/07_State_Management_Domain_Rules.md
03_Frontend/08_Data_Fetching_REST_API_Integration_Domain_Rules.md
03_Frontend/09_Form_Handling_Validation_Domain_Rules.md
03_Frontend/10_Authentication_Frontend_Flow_Domain_Rules.md
03_Frontend/11_Error_Handling_Loading_UX_Domain_Rules.md
03_Frontend/12_UI_Component_Pattern_Domain_Rules.md
03_Frontend/13_Frontend_Testing_Domain_Rules.md
03_Frontend/14_Frontend_Accessibility_Domain_Rules.md
03_Frontend/15_Frontend_Build_Deploy_Domain_Rules.md
03_Frontend/16_Frontend_Code_Review_Domain_Rules.md
03_Frontend/17_Styling_Architecture_Domain_Rules.md
03_Frontend/18_Design_System_Foundation_Domain_Rules.md
```

## 5. Secondary Domain Rules

```text
01_Backend/12_API_Design_Domain_Rules.md
01_Backend/05_Security_Advanced_Domain_Rules.md
01_Backend/10_Git_GitHub_Domain_Rules.md
01_Backend/11_Docker_Domain_Rules.md
```

## 6. Reference-only Domain Rules

```text
01_Backend/01_SQL_Domain_Rules.md
01_Backend/03_Spring_Boot_Domain_Rules.md
01_Backend/04_JPA_Advanced_Domain_Rules.md
```

## 7. 작업 유형별 참조

| 작업 유형 | 우선 참조 |
|---|---|
| 화면 구조 | React Core + Component Design + UI Component Pattern |
| 라우팅 | React Router |
| 상태 관리 | State Management |
| API 호출 | Data Fetching REST API Integration + API Design |
| 폼 입력/검증 | Form Handling Validation |
| 로그인/권한 흐름 | Authentication Frontend Flow + Security Reference |
| 로딩/에러 UX | Error Handling Loading UX |
| 접근성 | Accessibility |
| 테스트 | Frontend Testing |
| 빌드/배포 | Frontend Build Deploy |
| 스타일 구조 | Styling Architecture + Design System Foundation |
| 코드 리뷰 | Frontend Code Review |

## 8. Frontend Agent Output Handoff Format

```text
[Frontend Analysis]
- Request Summary:
- API Dependency:
- Page/Route Scope:
- Component Scope:
- State Scope:
- Auth/Permission Scope:

[Implementation Plan]
1.
2.
3.

[Files to Create/Modify]
- Pages:
- Components:
- Hooks:
- API Modules:
- State:
- Styles:
- Tests:

[Code Draft]
```tsx
// code here
```

[API Usage]
- Method:
- URL:
- Request Params/Body:
- Response Shape:
- Error Handling:

[UX Notes]
- Loading:
- Empty:
- Error:
- Permission Denied:

[Handoff to Review Agent]
- 검토 포인트

[RAG Update Candidate]
- 필요한 경우에만 작성
```

## 9. Backend Agent 결과 수신 시 확인 항목

```text
- API URL
- HTTP Method
- Request Body / Query Params
- Response Body
- Error Response 형식
- 인증/인가 필요 여부
- Pagination 여부
- Loading/Empty/Error 처리 필요 여부
```

## 10. Future Split Support

| 분리 후보 | 현재 위치 | 분리 기준 |
|---|---|---|
| Design System Agent | Design System / Styling | 디자인 시스템 문서가 Expert로 확장될 때 |
| Frontend Test Agent | Frontend Testing | 테스트 전략/코드 요청이 많아질 때 |
| Accessibility Agent | Accessibility | 접근성 요구사항이 별도 품질 기준이 될 때 |
| Frontend Performance Agent | React/Core/State | 성능 최적화 Expert 문서 제작 후 |
| Frontend DevOps Agent | Build/Deploy | FE 배포/빌드 파이프라인이 복잡해질 때 |

