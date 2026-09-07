import json
import unittest

import agents.nodes as nodes


DB_RESULT = """# DB Agent Output

## Design
REMOVE_DB_DESIGN

## SQL DDL

```sql
CREATE TABLE members (
    id BIGINT PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);
```

## Notes
REMOVE_DB_NOTES

## Backend Handoff
REMOVE_DB_BACKEND_HANDOFF
"""

BACKEND_RESULT = """# Backend Agent Output

## Implementation

### Entity
```java
class Member {
    private String password;
}
```

### Repository
```java
interface MemberRepository {}
```

### DTO
```java
class SignupRequest {
    private String password;
}
```

### Service
```java
class MemberService {
    void signup(SignupRequest request) {
        member.setPassword(passwordEncoder.encode(request.getPassword()));
    }
}
```

### Controller
```java
@PostMapping("/api/signup")
class MemberController {}
```

## Notes
REMOVE_BACKEND_NOTES
ORIGINAL_ONLY_BACKEND_QUOTE

## Frontend Handoff
- KEEP_BACKEND_FRONTEND_HANDOFF
- POST /api/signup
- Success: 200
"""

FRONTEND_RESULT = """# Frontend Implementation

## Files

### src/SignupPage.tsx
```tsx
import './styles.css';
export default function SignupPage() {
  return <form>Signup</form>;
}
```

### src/api.ts
```ts
export async function signup() {
  return fetch('/api/signup', { method: 'POST' });
}
```

### src/Legacy.jsx
```jsx
export default function Legacy() { return <div />; }
```

### src/helper.js
```js
export const helper = () => true;
```

### src/styles.css
```css
form { display: grid; }
```

## API Clarification
- KEEP_API_CLARIFICATION
- Endpoint: /api/signup

## Verification Notes
REMOVE_VERIFICATION_NOTES
"""


def base_state() -> dict:
    return {
        "user_request": "회원가입 기능 구현",
        "required_agents": ["db", "backend", "frontend"],
        "project_plan": "",
        "db_result": DB_RESULT,
        "db_validation": {"status": "PASS", "issues": []},
        "db_fix_count": 0,
        "backend_result": BACKEND_RESULT,
        "backend_validation": {"status": "PASS", "issues": []},
        "backend_fix_count": 0,
        "frontend_result": FRONTEND_RESULT,
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "PASS", "issues": []},
        "integration_fix_count": 0,
        "review_result": "",
        "review_status": "",
        "review_count": 0,
        "final_result": "",
        "llm_metrics": [],
    }


def run_review(state: dict, raw_result: dict | str) -> tuple[dict, str]:
    captured = {}
    original_invoke_agent = nodes.invoke_agent
    serialized = (
        json.dumps(raw_result, ensure_ascii=False)
        if isinstance(raw_result, dict)
        else raw_result
    )

    def fake_invoke(llm, system_prompt, user_prompt):
        del llm, system_prompt
        captured["prompt"] = user_prompt
        return serialized

    nodes.invoke_agent = fake_invoke
    try:
        result = nodes.review_agent(state)
    finally:
        nodes.invoke_agent = original_invoke_agent
    return result, captured["prompt"]


def pass_review() -> dict:
    return {
        "status": "PASS",
        "summary": "원래 요약",
        "issues": [],
        "rag_update_candidates": [],
    }


def test_db_projection_keeps_sql_heading_and_removes_explanations() -> None:
    projection = nodes.project_db_result_for_review(DB_RESULT)
    assert "## SQL DDL" in projection
    assert "CREATE TABLE members" in projection
    assert "REMOVE_DB_DESIGN" not in projection
    assert "REMOVE_DB_NOTES" not in projection
    assert "REMOVE_DB_BACKEND_HANDOFF" not in projection


def test_db_projection_falls_back_for_malformed_or_ambiguous_sql() -> None:
    malformed = "## SQL DDL\n```sql\nCREATE TABLE members (id BIGINT);"
    ambiguous = "# DB Output\n```sql\nSELECT 1;\n```"
    assert nodes.project_db_result_for_review(malformed) == malformed
    assert nodes.project_db_result_for_review(ambiguous) == ambiguous


def test_backend_projection_keeps_all_java_sections_and_handoff() -> None:
    projection = nodes.project_backend_result_for_review(BACKEND_RESULT)
    for heading in (
        "### Entity",
        "### Repository",
        "### DTO",
        "### Service",
        "### Controller",
    ):
        assert heading in projection
    for code in (
        "class Member",
        "interface MemberRepository",
        "class SignupRequest",
        "passwordEncoder.encode",
        '@PostMapping("/api/signup")',
    ):
        assert code in projection
    assert "KEEP_BACKEND_FRONTEND_HANDOFF" in projection
    assert "REMOVE_BACKEND_NOTES" not in projection
    assert "ORIGINAL_ONLY_BACKEND_QUOTE" not in projection


def test_backend_projection_falls_back_for_unsafe_structure() -> None:
    malformed = BACKEND_RESULT + "\n```java\nunclosed"
    missing_handoff = "## Entity\n```java\nclass Member {}\n```"
    ambiguous = (
        BACKEND_RESULT
        + "\n## Handoff to Frontend\nSECOND_FRONTEND_HANDOFF"
    )
    generic_heading = (
        "# Backend Output\n```java\nclass Unknown {}\n```\n"
        "## Frontend Handoff\ncontract"
    )
    assert nodes.project_backend_result_for_review(malformed) == malformed
    assert nodes.project_backend_result_for_review(missing_handoff) == missing_handoff
    assert nodes.project_backend_result_for_review(ambiguous) == ambiguous
    assert nodes.project_backend_result_for_review(generic_heading) == generic_heading


def test_frontend_projection_keeps_files_code_and_api_only() -> None:
    projection = nodes.project_frontend_result_for_review(FRONTEND_RESULT)
    for path in (
        "src/SignupPage.tsx",
        "src/api.ts",
        "src/Legacy.jsx",
        "src/helper.js",
        "src/styles.css",
    ):
        assert path in projection
    for code in ("fetch('/api/signup'", "<form>", "display: grid"):
        assert code in projection
    assert "KEEP_API_CLARIFICATION" in projection
    assert "REMOVE_VERIFICATION_NOTES" not in projection


def test_frontend_projection_falls_back_for_unsafe_structure() -> None:
    malformed = FRONTEND_RESULT + "\n```tsx\nunclosed"
    missing_path = (
        "## Files\n```tsx\nexport default function App() {}\n```\n"
        "## API Clarification\nUNKNOWN"
    )
    missing_api = "### src/App.tsx\n```tsx\nexport default function App() {}\n```"
    assert nodes.project_frontend_result_for_review(malformed) == malformed
    assert nodes.project_frontend_result_for_review(missing_path) == missing_path
    assert nodes.project_frontend_result_for_review(missing_api) == missing_api


def test_review_prompt_uses_projection_but_evidence_uses_original_state() -> None:
    result, prompt = run_review(base_state(), pass_review())
    assert "CREATE TABLE members" in prompt
    assert "passwordEncoder.encode" in prompt
    assert "fetch('/api/signup'" in prompt
    assert "KEEP_API_CLARIFICATION" in prompt
    assert "REMOVE_DB_DESIGN" not in prompt
    assert "REMOVE_BACKEND_NOTES" not in prompt
    assert "REMOVE_VERIFICATION_NOTES" not in prompt
    assert json.loads(result["review_result"])["status"] == "PASS"

    state = base_state()
    valid, removed = nodes.validate_review_evidence_issues([{
        "evidence": {
            "source": "Backend",
            "quote": "ORIGINAL_ONLY_BACKEND_QUOTE",
        }
    }], state)
    assert len(valid) == 1
    assert removed == []

    valid, removed = nodes.validate_review_evidence_issues([{
        "evidence": {
            "source": "Backend",
            "quote": "member.setPassword(request.getPassword());",
        }
    }], state)
    assert valid == []
    assert removed[0]["reason"] == "QUOTE_NOT_FOUND"


def test_review_postprocessing_and_pass_summary_are_unchanged() -> None:
    pass_result, _ = run_review(base_state(), {
        "status": "FAIL",
        "summary": "수정이 필요한 문제가 발견되었습니다.",
        "issues": [{
            "severity": "Major",
            "area": "Backend",
            "issue": "hallucinated",
            "evidence": {
                "source": "Backend",
                "quote": "member.setPassword(request.getPassword());",
            },
            "required_fix": "fix",
        }],
        "rag_update_candidates": [],
    })
    pass_data = json.loads(pass_result["review_result"])
    assert pass_data["status"] == "PASS"
    assert pass_data["issues"] == []
    assert pass_data["summary"] == "요구사항을 충족하며 수정이 필요한 문제가 없습니다."

    fail_state = base_state()
    fail_state["backend_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "MISSING_GETTER",
            "message": "getter missing",
            "required_fix": "getter 제공",
        }],
    }
    fail_state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "severity": "Major",
            "rule": "SUCCESS_STATUS_MISMATCH",
            "message": "status mismatch",
            "required_fix": "status 일치",
        }],
    }
    fail_result, _ = run_review(fail_state, pass_review())
    fail_data = json.loads(fail_result["review_result"])
    assert fail_data["status"] == "FAIL"
    assert any("MISSING_GETTER" in issue["issue"] for issue in fail_data["issues"])
    assert any(
        "SUCCESS_STATUS_MISMATCH" in issue["issue"]
        for issue in fail_data["issues"]
    )


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)
