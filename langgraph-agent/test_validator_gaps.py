import unittest

import agents.nodes as nodes
from graph.workflow import route_after_frontend_validator
from validators.backend_validator import validate_backend_result
from validators.frontend_validator import validate_frontend_result


DTO_BLOCKS = """## DTO

### SignupRequest.java
```java
package com.example.demo.dto;
public record SignupRequest(String loginId, String password) {}
```

### SignupResponse.java
```java
package com.example.demo.dto;
public record SignupResponse(Long id, String loginId) {}
```
"""

SERVICE_WITHOUT_IMPORTS = """## Service

### MemberService.java
```java
package com.example.demo.service;

public class MemberService {
    public SignupResponse signup(SignupRequest request) {
        return new SignupResponse(1L, request.loginId());
    }
}
```
"""

SERVICE_WITH_IMPORTS = """## Service

### MemberService.java
```java
package com.example.demo.service;

import com.example.demo.dto.SignupRequest;
import com.example.demo.dto.SignupResponse;

public class MemberService {
    public SignupResponse signup(SignupRequest request) {
        return new SignupResponse(1L, request.loginId());
    }
}
```
"""

VALID_FRONTEND = """# Frontend Implementation

## Files

### frontend/src/pages/LoginPage.tsx
```tsx
export function LoginPage() { return <main>Login</main>; }
```

## API Clarification

- Endpoint: /api/members/login
"""


def issue_rules(validation: dict) -> set[str]:
    return {issue["rule"] for issue in validation["issues"]}


class FakeResponse:
    def __init__(self, done_reason: str):
        self.content = VALID_FRONTEND
        self.response_metadata = {"done_reason": done_reason}


class FakeLlm:
    model = "fake"
    num_ctx = 10240
    num_predict = 2048

    def __init__(self, done_reason: str):
        self.done_reason = done_reason

    def invoke(self, messages):
        del messages
        return FakeResponse(self.done_reason)


def frontend_state(result: str, metrics: list[dict]) -> dict:
    return {
        "user_request": "로그인 페이지 구현",
        "required_agents": ["backend", "frontend"],
        "backend_result": "BACKEND",
        "frontend_result": result,
        "frontend_validation": {"status": "NOT_RUN", "issues": []},
        "frontend_fix_count": 0,
        "llm_metrics": metrics,
    }


class ValidatorGapTest(unittest.TestCase):
    def test_missing_dto_imports_fail_and_valid_imports_pass(self) -> None:
        missing = validate_backend_result(DTO_BLOCKS + SERVICE_WITHOUT_IMPORTS)
        valid = validate_backend_result(DTO_BLOCKS + SERVICE_WITH_IMPORTS)
        self.assertEqual(missing["status"], "FAIL")
        self.assertEqual(issue_rules(missing), {"MISSING_DTO_IMPORT"})
        self.assertEqual(len(missing["issues"]), 2)
        self.assertEqual(valid["status"], "PASS")

    def test_existing_project_dto_definition_can_drive_import_check(self) -> None:
        generated_service = SERVICE_WITHOUT_IMPORTS
        project_context = {
            "selected_files": [
                {
                    "language": "java",
                    "content": "package com.example.demo.dto; public record SignupRequest(String loginId) {}",
                },
                {
                    "language": "java",
                    "content": "package com.example.demo.dto; public record SignupResponse(Long id) {}",
                },
            ]
        }
        validation = validate_backend_result(
            generated_service,
            project_context=project_context,
        )
        self.assertEqual(issue_rules(validation), {"MISSING_DTO_IMPORT"})

    def test_dto_import_rule_allows_same_package_fqcn_and_wildcard(self) -> None:
        same_package = DTO_BLOCKS + """```java
package com.example.demo.dto;
class Mapper { SignupResponse map(SignupRequest value) { return null; } }
```"""
        fqcn = DTO_BLOCKS + """```java
package com.example.demo.service;
class Mapper { com.example.demo.dto.SignupResponse map(
    com.example.demo.dto.SignupRequest value) { return null; } }
```"""
        wildcard = DTO_BLOCKS + """```java
package com.example.demo.service;
import com.example.demo.dto.*;
class Mapper { SignupResponse map(SignupRequest value) { return null; } }
```"""
        for source in (same_package, fqcn, wildcard):
            self.assertNotIn("MISSING_DTO_IMPORT", issue_rules(validate_backend_result(source)))

    def test_frontend_self_import_fails_but_sibling_import_passes(self) -> None:
        self_import = """# Frontend Implementation
## Files
### frontend/src/api/authApi.ts
```ts
import { SignupPayload } from "./authApi";
export interface SignupPayload { loginId: string }
```
"""
        explicit_self_import = self_import.replace('"./authApi"', '"./authApi.ts"')
        sibling_import = self_import.replace('"./authApi"', '"./types"')
        for source in (self_import, explicit_self_import):
            validation = validate_frontend_result(source)
            self.assertIn("SELF_IMPORT", issue_rules(validation))
        self.assertNotIn("SELF_IMPORT", issue_rules(validate_frontend_result(sibling_import)))

    def test_commented_or_alias_import_is_not_treated_as_self_import(self) -> None:
        source = """# Frontend Implementation
## Files
### frontend/src/api/authApi.ts
```ts
/* import { A } from "./authApi"; */
// import { B } from "./authApi";
import { C } from "@/api/authApi";
export const value = 1;
```
"""
        self.assertNotIn("SELF_IMPORT", issue_rules(validate_frontend_result(source)))

    def test_length_metadata_forces_fail_and_existing_fix_route(self) -> None:
        metrics = []
        result = nodes.invoke_agent(
            FakeLlm("length"),
            "SYSTEM",
            "USER",
            metric_context={"agent": "frontend", "mode": "initial", "call_index": 1},
            metrics_sink=metrics,
        )
        state = frontend_state(result, metrics)
        validation = nodes.frontend_validator(state)["frontend_validation"]
        state["frontend_validation"] = validation
        self.assertEqual(validation["status"], "FAIL")
        self.assertIn("TRUNCATED_LLM_OUTPUT", issue_rules(validation))
        self.assertEqual(route_after_frontend_validator(state), "frontend")

    def test_stop_or_missing_metadata_keeps_existing_validation(self) -> None:
        metrics = []
        result = nodes.invoke_agent(
            FakeLlm("stop"),
            "SYSTEM",
            "USER",
            metric_context={"agent": "frontend", "mode": "initial", "call_index": 1},
            metrics_sink=metrics,
        )
        stopped = nodes.frontend_validator(frontend_state(result, metrics))[
            "frontend_validation"
        ]
        missing = nodes.frontend_validator(frontend_state(result, []))[
            "frontend_validation"
        ]
        self.assertEqual(stopped["status"], "PASS")
        self.assertEqual(missing["status"], "PASS")

    def test_db_and_backend_length_metrics_also_fail(self) -> None:
        db_state = {
            "db_result": "",
            "user_request": "설명해줘",
            "llm_metrics": [{"agent": "db", "done_reason": "length"}],
        }
        backend_state = {
            "backend_result": "",
            "llm_metrics": [{"agent": "backend", "done_reason": "length"}],
        }
        self.assertIn(
            "TRUNCATED_LLM_OUTPUT",
            issue_rules(nodes.db_validator(db_state)["db_validation"]),
        )
        self.assertIn(
            "TRUNCATED_LLM_OUTPUT",
            issue_rules(nodes.backend_validator(backend_state)["backend_validation"]),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
