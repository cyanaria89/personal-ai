import json
import unittest

import agents.nodes as nodes


def make_issue(source: str, quote: str, name: str = "issue") -> dict:
    return {
        "severity": "Major",
        "area": "Test",
        "issue": name,
        "evidence": {
            "source": source,
            "quote": quote,
        },
        "required_fix": "fix",
    }


def base_state() -> dict:
    return {
        "user_request": "테스트 구현",
        "required_agents": ["db", "backend", "frontend"],
        "db_result": "CREATE TABLE member (id BIGINT PRIMARY KEY);",
        "db_validation": {"status": "PASS", "issues": []},
        "db_fix_count": 0,
        "backend_result": (
            "member.setPassword("
            "passwordEncoder.encode(request.getPassword()));"
        ),
        "backend_validation": {"status": "PASS", "issues": []},
        "backend_fix_count": 0,
        "frontend_result": "await onRegister?.(formData);",
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "PASS", "issues": []},
        "review_count": 0,
    }


def filter_issues(issues: list, state: dict | None = None) -> list[dict]:
    valid, _ = nodes.validate_review_evidence_issues(
        issues,
        state or base_state(),
    )
    return valid


def run_review(raw_result: str, state: dict | None = None) -> dict:
    original_invoke_agent = nodes.invoke_agent
    nodes.invoke_agent = lambda *args: raw_result
    try:
        result = nodes.review_agent(state or base_state())
    finally:
        nodes.invoke_agent = original_invoke_agent
    return {
        "state": result,
        "json": json.loads(result["review_result"]),
    }


def review_json(issues: list, status: str = "FAIL") -> str:
    return json.dumps({
        "status": status,
        "summary": "test",
        "issues": issues,
        "rag_update_candidates": [],
    }, ensure_ascii=False)


def test_backend_exact_quote_is_kept() -> None:
    issue = make_issue(
        "Backend",
        "passwordEncoder.encode(request.getPassword())",
    )
    assert filter_issues([issue]) == [issue]


def test_db_exact_quote_is_kept() -> None:
    issue = make_issue("DB", "CREATE TABLE member")
    assert filter_issues([issue]) == [issue]


def test_frontend_exact_quote_is_kept() -> None:
    issue = make_issue("Frontend", "await onRegister?.(formData);")
    assert filter_issues([issue]) == [issue]


def test_whitespace_normalized_quote_is_kept() -> None:
    state = base_state()
    state["backend_result"] = "service.call(\n    first,\n    second\n);"
    issue = make_issue("Backend", "service.call( first, second );")
    assert filter_issues([issue], state) == [issue]


def test_quote_not_in_source_is_removed() -> None:
    issue = make_issue("Backend", "missing.call();")
    assert filter_issues([issue]) == []


def test_nonexistent_plain_password_storage_quote_is_removed() -> None:
    issue = make_issue(
        "Backend",
        "member.setPassword(request.getPassword());",
    )
    assert filter_issues([issue]) == []


def test_unknown_source_is_removed() -> None:
    assert filter_issues([make_issue("Server", "anything")]) == []


def test_empty_source_and_empty_quote_are_removed() -> None:
    issues = [make_issue("", "anything"), make_issue("Backend", "  ")]
    assert filter_issues(issues) == []


def test_non_dict_evidence_is_removed() -> None:
    issue = make_issue("Backend", "passwordEncoder")
    issue["evidence"] = "Backend evidence"
    assert filter_issues([issue]) == []


def test_valid_and_invalid_issues_are_filtered_independently() -> None:
    valid = make_issue("DB", "CREATE TABLE member", "valid")
    invalid = make_issue("Backend", "not.present()", "invalid")
    assert filter_issues([valid, invalid]) == [valid]


def test_review_fail_with_only_invalid_issue_becomes_pass() -> None:
    invalid = make_issue("Backend", "not.present()")
    result = run_review(review_json([invalid]))
    assert result["state"]["review_status"] == "PASS"
    assert result["json"]["issues"] == []
    assert result["json"]["summary"] == (
        "요구사항을 충족하며 수정이 필요한 문제가 없습니다."
    )


def test_integration_validator_failure_is_merged() -> None:
    state = base_state()
    state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "SUCCESS_STATUS_MISMATCH",
            "message": "Backend 200과 Frontend 201이 일치하지 않습니다.",
            "required_fix": "성공 status를 일치시키세요.",
        }],
    }
    result = run_review(review_json([], status="PASS"), state)
    assert result["state"]["review_status"] == "FAIL"
    assert len(result["json"]["issues"]) == 1
    issue = result["json"]["issues"][0]
    assert "SUCCESS_STATUS_MISMATCH" in issue["issue"]
    assert "evidence" not in issue


def test_validator_failure_is_merged_after_invalid_llm_issue() -> None:
    state = base_state()
    state["backend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "FIELD_INJECTION",
            "message": "Field Injection이 사용되었습니다.",
            "required_fix": "생성자 주입을 사용하세요.",
        }],
    }
    invalid = make_issue("Backend", "not.present()")
    result = run_review(review_json([invalid]), state)
    assert result["state"]["review_status"] == "FAIL"
    assert len(result["json"]["issues"]) == 1
    assert "FIELD_INJECTION" in result["json"]["issues"][0]["issue"]


def test_validator_issue_without_evidence_is_kept() -> None:
    state = base_state()
    state["frontend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "TEST_RULE",
            "message": "validator issue",
            "required_fix": "fix validator issue",
        }],
    }
    result = run_review(review_json([], status="PASS"), state)
    issue = result["json"]["issues"][0]
    assert result["state"]["review_status"] == "FAIL"
    assert "evidence" not in issue
    assert "TEST_RULE" in issue["issue"]


def test_json_parse_failure_issue_is_kept_and_fails() -> None:
    result = run_review("not valid json")
    assert result["state"]["review_status"] == "FAIL"
    assert result["json"]["issues"][0]["issue"] == "JSON 형식 오류"


def test_fuzzy_similar_quote_is_removed() -> None:
    issue = make_issue(
        "Backend",
        "member.setPassword(passwordEncoder.hash(request.getPassword()));",
    )
    assert filter_issues([issue]) == []


def test_quote_existing_only_in_other_agent_is_removed() -> None:
    issue = make_issue("DB", "passwordEncoder.encode")
    assert filter_issues([issue]) == []


def load_tests(
    loader: unittest.TestLoader,
    tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)
