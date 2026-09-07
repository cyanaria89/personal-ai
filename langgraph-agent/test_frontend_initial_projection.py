import unittest

import agents.nodes as nodes


PROJECT_PLAN = """REQUIRED_AGENTS: backend, frontend

REQUEST_SUMMARY:
로그인 기능 추가

EXECUTION_ORDER:
REMOVE_EXECUTION_ORDER

DB_HANDOFF:
REMOVE_DB_HANDOFF

BACKEND_HANDOFF:
REMOVE_BACKEND_HANDOFF

FRONTEND_HANDOFF:
- POST /api/members/login 사용
"""

BACKEND_RESULT = """# Backend Agent Output

## Implementation

### Entity

```java
class REMOVE_ENTITY {
    %s
}
```

### Repository

```java
interface REMOVE_REPOSITORY {}
```

### DTO

#### LoginRequest.java

```java
record LoginRequest(String loginId, String password) {}
```

#### LoginResponse.java

```java
record LoginResponse(Long id, String loginId) {}
```

### Service

```java
class REMOVE_SERVICE {
    %s
}
```

### Controller

```java
@RequestMapping("/api/members")
public class MemberController {
    private final REMOVE_CONTROLLER_IMPLEMENTATION dependency;

    @PostMapping("/login")
    @ResponseStatus(HttpStatus.OK)
    public LoginResponse login(LoginRequest request) {
        return REMOVE_CONTROLLER_IMPLEMENTATION.login(request);
    }
}
```

### SecurityConfig

```java
class REMOVE_SECURITY_CONFIG {}
```

## Notes

REMOVE_NOTES

## Frontend Handoff

- POST /api/members/login
- Success: 200
""" % ("private String field;\n" * 120, "void implementation() {}\n" * 120)


def context() -> dict:
    return {
        "schema_version": 1,
        "status": "READY",
        "root": "/fixture",
        "detected_stack": ["react", "typescript"],
        "tree_summary": ["frontend/src/pages/SignupPage.tsx"],
        "selected_files": [{
            "path": "frontend/src/pages/SignupPage.tsx",
            "category": "frontend",
            "language": "tsx",
            "score": 100,
            "reasons": ["filename-keyword:signup"],
            "size_bytes": 45,
            "content": "export function SignupPage() { return <form />; }",
            "truncated": False,
        }],
        "warnings": [],
        "stats": {
            "scanned_file_count": 1,
            "eligible_file_count": 1,
            "selected_file_count": 1,
            "selected_char_count": 52,
            "excluded_count": 0,
            "truncated_file_count": 0,
        },
    }


def state() -> dict:
    return {
        "user_request": "로그인 페이지 추가해줘",
        "required_agents": ["backend", "frontend"],
        "project_plan": PROJECT_PLAN,
        "backend_result": BACKEND_RESULT,
        "frontend_result": "",
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "NOT_RUN", "issues": []},
        "integration_fix_count": 0,
        "project_context": context(),
        "llm_metrics": [],
    }


def capture_initial_prompt() -> str:
    captured = {}
    original = nodes.invoke_agent

    def fake_invoke(llm, system_prompt, user_prompt):
        del llm, system_prompt
        captured["prompt"] = user_prompt
        return "FRONTEND_RESULT"

    nodes.invoke_agent = fake_invoke
    try:
        nodes.frontend_agent(state())
    finally:
        nodes.invoke_agent = original
    return captured["prompt"]


class FrontendInitialProjectionTest(unittest.TestCase):
    def test_backend_projection_keeps_contract_only(self) -> None:
        projected = nodes.extract_frontend_initial_backend_context(BACKEND_RESULT)
        self.assertIn("### DTO", projected)
        self.assertIn("LoginRequest", projected)
        self.assertIn("LoginResponse", projected)
        self.assertIn('@RequestMapping("/api/members")', projected)
        self.assertIn('@PostMapping("/login")', projected)
        self.assertIn("@ResponseStatus(HttpStatus.OK)", projected)
        self.assertIn("public LoginResponse login", projected)
        self.assertIn("## Frontend Handoff", projected)
        for removed in (
            "REMOVE_ENTITY", "REMOVE_REPOSITORY", "REMOVE_SERVICE",
            "REMOVE_SECURITY_CONFIG", "REMOVE_NOTES", "REMOVE_CONTROLLER_IMPLEMENTATION",
        ):
            self.assertNotIn(removed, projected)

    def test_pm_projection_keeps_frontend_sections_only(self) -> None:
        projected = nodes.extract_frontend_fix_project_context(PROJECT_PLAN)
        self.assertIn("REQUEST_SUMMARY:", projected)
        self.assertIn("FRONTEND_HANDOFF:", projected)
        self.assertNotIn("BACKEND_HANDOFF:", projected)
        self.assertNotIn("DB_HANDOFF:", projected)
        self.assertNotIn("EXECUTION_ORDER:", projected)

    def test_unsafe_backend_structures_fall_back_to_full_input(self) -> None:
        missing_dto = "## Controller\n\n```java\n@PostMapping(\"/login\")\npublic void login() {}\n```\n\n## Frontend Handoff\n\n- API"
        broken_fence = BACKEND_RESULT + "\n```java\nunclosed"
        ambiguous = BACKEND_RESULT + "\n### API Controller\n\nSECOND"
        self.assertEqual(nodes.extract_frontend_initial_backend_context(missing_dto), missing_dto)
        self.assertEqual(nodes.extract_frontend_initial_backend_context(broken_fence), broken_fence)
        self.assertEqual(nodes.extract_frontend_initial_backend_context(ambiguous), ambiguous)

    def test_initial_prompt_uses_projections_and_keeps_project_context(self) -> None:
        prompt = capture_initial_prompt()
        self.assertIn("SignupPage.tsx", prompt)
        self.assertIn("LoginRequest", prompt)
        self.assertIn('@PostMapping("/login")', prompt)
        self.assertIn("REQUEST_SUMMARY:", prompt)
        self.assertIn("FRONTEND_HANDOFF:", prompt)
        self.assertNotIn("REMOVE_ENTITY", prompt)
        self.assertNotIn("REMOVE_SERVICE", prompt)
        self.assertNotIn("REMOVE_BACKEND_HANDOFF", prompt)

    def test_runtime_character_reduction_exceeds_target(self) -> None:
        prompt = capture_initial_prompt()
        projected_pm = nodes.extract_frontend_fix_project_context(PROJECT_PLAN)
        projected_backend = nodes.extract_frontend_initial_backend_context(BACKEND_RESULT)
        prior_prompt_size = (
            len(prompt)
            + len(PROJECT_PLAN) - len(projected_pm)
            + len(BACKEND_RESULT) - len(projected_backend)
        )
        reduction = prior_prompt_size - len(prompt)
        self.assertGreaterEqual(reduction, 3_000)
        self.assertLess(len(prompt), prior_prompt_size)


if __name__ == "__main__":
    unittest.main(verbosity=2)
