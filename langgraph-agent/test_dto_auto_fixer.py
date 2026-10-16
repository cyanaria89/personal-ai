import unittest

from agents.nodes import backend_validator
from graph.workflow import route_after_backend_validator
from validators.backend_auto_fixer import auto_fix_backend_result
from validators.backend_validator import validate_backend_result


BACKEND = """## Service
### MemberService.java
```java
package com.example.demo.service;

import com.example.demo.dto.LoginRequest;

public class MemberService {
    public SignupResponse signup(SignupRequest request) {
        return new SignupResponse(1L, request.loginId());
    }
}
```
"""


def project_context(packages: tuple[str, ...] = ("com.example.demo.dto",)) -> dict:
    files = []
    for package in packages:
        for type_name in ("SignupRequest", "SignupResponse"):
            files.append({
                "language": "java",
                "content": (
                    f"package {package};\n"
                    f"public record {type_name}(String value) {{}}"
                ),
            })
    return {"selected_files": files}


def rules(validation: dict) -> list[str]:
    return [issue["rule"] for issue in validation["issues"]]


class DtoAutoFixerTest(unittest.TestCase):
    def test_two_missing_dto_imports_are_fixed_in_one_pass(self) -> None:
        context = project_context()
        first = validate_backend_result(BACKEND, project_context=context)
        fixed, applied = auto_fix_backend_result(BACKEND, first["issues"])
        second = validate_backend_result(fixed, project_context=context)

        self.assertEqual(rules(first), ["MISSING_DTO_IMPORT", "MISSING_DTO_IMPORT"])
        self.assertIn("import com.example.demo.dto.SignupRequest;", fixed)
        self.assertIn("import com.example.demo.dto.SignupResponse;", fixed)
        self.assertEqual(len(applied), 2)
        self.assertEqual(second["status"], "PASS")
        self.assertIn("return new SignupResponse(1L, request.loginId());", fixed)

    def test_backend_validator_auto_fix_passes_without_llm_fix_route(self) -> None:
        state = {
            "user_request": "기존 회원가입 Service의 DTO import를 수정해줘",
            "backend_result": BACKEND,
            "project_context": project_context(),
            "backend_validation": {"status": "NOT_RUN", "issues": []},
            "backend_fix_count": 0,
            "integration_validation": {"status": "NOT_RUN", "issues": []},
            "required_agents": ["backend", "frontend"],
            "llm_metrics": [{"agent": "backend", "done_reason": "stop"}],
        }
        result = backend_validator(state)
        routed_state = {**state, **result}
        self.assertEqual(result["backend_validation"]["status"], "PASS")
        self.assertEqual(route_after_backend_validator(routed_state), "frontend")
        self.assertIn("import com.example.demo.dto.SignupRequest;", result["backend_result"])

    def test_ambiguous_or_incomplete_issue_payload_is_not_fixed(self) -> None:
        ambiguous = [
            {"rule": "MISSING_DTO_IMPORT", "target_java_type": "MemberService", "missing_type": "SignupRequest", "target_package": "a.dto"},
            {"rule": "MISSING_DTO_IMPORT", "target_java_type": "MemberService", "missing_type": "SignupRequest", "target_package": "b.dto"},
        ]
        incomplete = [{"rule": "MISSING_DTO_IMPORT", "missing_type": "SignupRequest"}]
        for issues in (ambiguous, incomplete):
            fixed, applied = auto_fix_backend_result(BACKEND, issues)
            self.assertEqual(fixed, BACKEND)
            self.assertEqual(applied, [])

    def test_duplicate_owner_or_malformed_fence_is_not_fixed(self) -> None:
        issue = [{
            "rule": "MISSING_DTO_IMPORT",
            "target_java_type": "MemberService",
            "missing_type": "SignupRequest",
            "target_package": "com.example.demo.dto",
        }]
        duplicate_owner = BACKEND + BACKEND
        malformed = BACKEND + "\n```java\nunclosed"
        for source in (duplicate_owner, malformed):
            fixed, applied = auto_fix_backend_result(source, issue)
            self.assertEqual(fixed, source)
            self.assertEqual(applied, [])

    def test_same_package_wildcard_and_fully_qualified_are_not_changed(self) -> None:
        issue = [{
            "rule": "MISSING_DTO_IMPORT",
            "target_java_type": "MemberService",
            "missing_type": "SignupRequest",
            "target_package": "com.example.demo.dto",
        }]
        same_package = BACKEND.replace("package com.example.demo.service;", "package com.example.demo.dto;")
        wildcard = BACKEND.replace(
            "import com.example.demo.dto.LoginRequest;",
            "import com.example.demo.dto.*;",
        )
        qualified = BACKEND.replace(
            "SignupRequest request",
            "com.example.demo.dto.SignupRequest request",
        )
        for source in (same_package, wildcard, qualified):
            fixed, applied = auto_fix_backend_result(source, issue)
            self.assertEqual(fixed, source)
            self.assertEqual(applied, [])

    def test_truncated_output_skips_dto_auto_fix(self) -> None:
        state = {
            "backend_result": BACKEND,
            "project_context": project_context(),
            "llm_metrics": [{"agent": "backend", "done_reason": "length"}],
        }
        result = backend_validator(state)
        self.assertEqual(result["backend_result"], BACKEND)
        self.assertEqual(result["backend_validation"]["status"], "FAIL")
        self.assertIn("TRUNCATED_LLM_OUTPUT", rules(result["backend_validation"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
