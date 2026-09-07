import unittest

from graph.workflow import route_after_frontend_validator
from validators.integration_validator import validate_integration_result


def backend_fixture(
    mapping: str = '@PostMapping("/signup")',
    return_type: str = "SignupResponse",
    body: str = "return memberService.signup(request);",
    class_mapping: str = "",
    method_annotation: str = "",
) -> str:
    return f"""
```java
import org.springframework.web.bind.annotation.*;
{class_mapping}
@RestController
public class SignupController {{
    {method_annotation}
    {mapping}
    public {return_type} signup(SignupRequest request) {{
        {body}
    }}
}}
```
"""


def frontend_fixture(
    call: str = 'const response = await fetch("/signup", { method: "POST" });',
    condition: str = "",
) -> str:
    return f"""
```tsx
export async function signup() {{
    {call}
    {condition}
}}
```
"""


def issue_rules(result: dict) -> set[str]:
    return {issue["rule"] for issue in result["issues"]}


def issue_for(result: dict, rule: str) -> dict:
    return next(issue for issue in result["issues"] if issue["rule"] == rule)


def test_post_signup_matches() -> None:
    result = validate_integration_result(backend_fixture(), frontend_fixture())
    assert result["status"] == "PASS"


def test_http_method_mismatch_fails() -> None:
    frontend = frontend_fixture('const response = await axios.get("/signup");')
    result = validate_integration_result(backend_fixture(), frontend)
    assert "HTTP_METHOD_MISMATCH" in issue_rules(result)
    assert issue_for(result, "HTTP_METHOD_MISMATCH")["target_agent"] == "UNKNOWN"


def test_same_endpoint_passes() -> None:
    result = validate_integration_result(backend_fixture(), frontend_fixture())
    assert "ENDPOINT_PATH_MISMATCH" not in issue_rules(result)


def test_class_and_method_paths_are_combined() -> None:
    backend = backend_fixture(class_mapping='@RequestMapping("/api")')
    frontend = frontend_fixture(
        'const response = await axios.post("/api/signup", {});'
    )
    assert validate_integration_result(backend, frontend)["status"] == "PASS"


def test_endpoint_path_mismatch_fails() -> None:
    backend = backend_fixture(class_mapping='@RequestMapping("/api")')
    frontend = frontend_fixture(
        'const response = await axios.post("/api/register", {});'
    )
    result = validate_integration_result(backend, frontend)
    assert "ENDPOINT_PATH_MISMATCH" in issue_rules(result)
    assert issue_for(result, "ENDPOINT_PATH_MISMATCH")["target_agent"] == "UNKNOWN"


def test_default_200_matches_frontend_200() -> None:
    frontend = frontend_fixture(condition="if (response.status === 200) {}")
    assert validate_integration_result(backend_fixture(), frontend)["status"] == "PASS"


def test_default_200_and_frontend_201_fail() -> None:
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    result = validate_integration_result(backend_fixture(), frontend)
    assert "SUCCESS_STATUS_MISMATCH" in issue_rules(result)
    assert issue_for(result, "SUCCESS_STATUS_MISMATCH")["target_agent"] == "frontend"


def test_user_201_targets_backend_when_frontend_matches() -> None:
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    result = validate_integration_result(
        backend_fixture(),
        frontend,
        user_request="회원가입 성공 시 HTTP 201로 응답해줘",
    )
    assert issue_for(result, "SUCCESS_STATUS_MISMATCH")["target_agent"] == "backend"


def test_user_201_targets_frontend_when_backend_matches() -> None:
    backend = backend_fixture(
        return_type="ResponseEntity<SignupResponse>",
        body="return ResponseEntity.created(location).body(response);",
    )
    frontend = frontend_fixture(condition="if (response.status === 200) {}")
    result = validate_integration_result(
        backend,
        frontend,
        user_request="status 201로 응답",
    )
    assert issue_for(result, "SUCCESS_STATUS_MISMATCH")["target_agent"] == "frontend"


def test_user_status_missed_by_both_targets_unknown() -> None:
    frontend = frontend_fixture(condition="if (response.status === 202) {}")
    result = validate_integration_result(
        backend_fixture(),
        frontend,
        user_request="201 Created로 응답",
    )
    assert issue_for(result, "SUCCESS_STATUS_MISMATCH")["target_agent"] == "UNKNOWN"


def test_multiple_user_success_statuses_target_unknown() -> None:
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    result = validate_integration_result(
        backend_fixture(),
        frontend,
        user_request="환경에 따라 status 200 또는 status 201",
    )
    assert issue_for(result, "SUCCESS_STATUS_MISMATCH")["target_agent"] == "UNKNOWN"


def test_backend_handoff_status_conflict_targets_unknown() -> None:
    backend = backend_fixture() + """
## Frontend Handoff

- Success Status: 201 Created
"""
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    result = validate_integration_result(backend, frontend)
    assert issue_for(result, "SUCCESS_STATUS_MISMATCH")["target_agent"] == "UNKNOWN"


def test_response_entity_created_matches_201() -> None:
    backend = backend_fixture(
        return_type="ResponseEntity<SignupResponse>",
        body="return ResponseEntity.created(location).body(response);",
    )
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    assert validate_integration_result(backend, frontend)["status"] == "PASS"


def test_response_entity_status_created_matches_201() -> None:
    backend = backend_fixture(
        return_type="ResponseEntity<SignupResponse>",
        body=(
            "return ResponseEntity.status(HttpStatus.CREATED)"
            ".body(response);"
        ),
    )
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    assert validate_integration_result(backend, frontend)["status"] == "PASS"


def test_response_status_created_matches_201() -> None:
    backend = backend_fixture(method_annotation="@ResponseStatus(HttpStatus.CREATED)")
    frontend = frontend_fixture(condition="if (response.status === 201) {}")
    assert validate_integration_result(backend, frontend)["status"] == "PASS"


def test_response_ok_skips_status_check() -> None:
    frontend = frontend_fixture(condition="if (response.ok) {}")
    assert validate_integration_result(backend_fixture(), frontend)["status"] == "PASS"


def test_callback_prop_style_is_skipped() -> None:
    frontend = frontend_fixture("await onSignup?.(formData);")
    assert validate_integration_result(backend_fixture(), frontend)["status"] == "PASS"


def test_dynamic_endpoint_is_skipped() -> None:
    frontend = frontend_fixture(
        "const response = await fetch(`${apiBase}/signup`, { method: 'POST' });"
    )
    assert validate_integration_result(backend_fixture(), frontend)["status"] == "PASS"


def test_multiple_backend_mappings_are_skipped() -> None:
    backend = backend_fixture() + backend_fixture(mapping='@PostMapping("/other")')
    assert validate_integration_result(backend, frontend_fixture())["status"] == "PASS"


def test_backend_only_and_frontend_only_skip_integration_route() -> None:
    common = {
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
    }
    assert route_after_frontend_validator({
        **common,
        "required_agents": ["backend"],
    }) == "review"
    assert route_after_frontend_validator({
        **common,
        "required_agents": ["frontend"],
    }) == "review"
    assert route_after_frontend_validator({
        **common,
        "required_agents": ["backend", "frontend"],
    }) == "integration"


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)
