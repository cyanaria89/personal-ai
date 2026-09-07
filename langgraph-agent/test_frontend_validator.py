import unittest

from validators.frontend_validator import validate_frontend_result


VALID_FRONTEND_RESULT = """
# Frontend Implementation

## Files

### src/pages/RegisterPage.tsx

```tsx
import React, { useState } from 'react';
import './RegisterPage.css';

type RegisterData = {
  username: string;
  email: string;
  password: string;
};

type RegisterPageProps = {
  onRegister?: (data: RegisterData) => Promise<void>;
};

const RegisterPage: React.FC<RegisterPageProps> = ({ onRegister }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError('');

    try {
      await onRegister?.({ username, email, password });
    } catch {
      setError('회원가입에 실패했습니다.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className="register-page" onSubmit={handleSubmit}>
      <label htmlFor="email">이메일</label>
      <input
        id="email"
        type="email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
        required
      />
      {error && <p role="alert">{error}</p>}
      <button disabled={loading} type="submit">
        {loading ? '처리 중...' : '회원가입'}
      </button>
    </form>
  );
};

export default RegisterPage;
```

### src/pages/RegisterPage.css

```css
.register-page {
  display: grid;
  gap: 1rem;
}
```

## API Clarification

- Endpoint: UNKNOWN (미확정)
- Request DTO: UNKNOWN (미확정)
- Response DTO: UNKNOWN (미확정)

## Verification Notes

- CSS import 확인
"""


def issue_rules(result: dict) -> set[str]:
    return {issue["rule"] for issue in result["issues"]}


def validate(result: str, user_request: str = "회원가입 페이지를 React로 구현해줘") -> dict:
    return validate_frontend_result(
        result,
        user_request=user_request,
        required_agents=["frontend"],
        backend_result="",
    )


def test_recent_frontend_only_result_passes() -> None:
    result = validate(VALID_FRONTEND_RESULT)

    assert result["status"] == "PASS"
    assert result["issues"] == []


def test_missing_frontend_implementation_fails() -> None:
    result = validate("""
    # Frontend Implementation
    ## Files
    구현 계획만 작성합니다.
    """)

    assert result["status"] == "FAIL"
    assert "MISSING_FRONTEND_IMPLEMENTATION" in issue_rules(result)


def test_missing_imported_css_file_fails() -> None:
    result = validate("""
    # Frontend Implementation
    ## Files
    ### src/pages/RegisterPage.tsx
    ```tsx
    import './RegisterPage.css';
    export default function RegisterPage() {
      return <main>회원가입</main>;
    }
    ```
    ## API Clarification
    - Endpoint: UNKNOWN (미확정)
    - Request DTO: UNKNOWN (미확정)
    - Response DTO: UNKNOWN (미확정)
    """)

    assert result["status"] == "FAIL"
    assert "MISSING_IMPORTED_CSS_FILE" in issue_rules(result)


def test_unused_output_css_file_fails() -> None:
    result = validate("""
    # Frontend Implementation
    ## Files
    ### src/pages/RegisterPage.tsx
    ```tsx
    export default function RegisterPage() {
      return <main>회원가입</main>;
    }
    ```
    ### src/pages/RegisterPage.css
    ```css
    .register-page { display: grid; }
    ```
    ## API Clarification
    - Endpoint: UNKNOWN (미확정)
    - Request DTO: UNKNOWN (미확정)
    - Response DTO: UNKNOWN (미확정)
    """)

    assert result["status"] == "FAIL"
    assert "UNUSED_OUTPUT_CSS_FILE" in issue_rules(result)


def test_global_css_is_excluded_from_unused_check() -> None:
    result = validate("""
    # Frontend Implementation
    ## Files
    ### src/pages/RegisterPage.tsx
    ```tsx
    export default function RegisterPage() {
      return <main>회원가입</main>;
    }
    ```
    ### src/global.css
    ```css
    body { margin: 0; }
    ```
    ## API Clarification
    - Endpoint: UNKNOWN (미확정)
    - Request DTO: UNKNOWN (미확정)
    - Response DTO: UNKNOWN (미확정)
    """)

    assert result["status"] == "PASS"


def test_unconfirmed_api_contract_fails() -> None:
    result = validate(
        VALID_FRONTEND_RESULT.replace(
            "- Endpoint: UNKNOWN (미확정)\n"
            "- Request DTO: UNKNOWN (미확정)\n"
            "- Response DTO: UNKNOWN (미확정)",
            "- Endpoint: `/api/signup`\n"
            "- Request DTO: `{ email: string }`\n"
            "- Response DTO: `{ message: string }`",
        )
    )

    assert result["status"] == "FAIL"
    assert "UNCONFIRMED_API_CONTRACT" in issue_rules(result)


def test_user_provided_endpoint_does_not_fail_contract_check() -> None:
    result = validate_frontend_result(
        VALID_FRONTEND_RESULT.replace(
            "- Endpoint: UNKNOWN (미확정)",
            "- Endpoint: `/api/signup`",
        ),
        user_request="POST /api/signup을 호출하는 회원가입 페이지를 구현해줘",
        required_agents=["frontend"],
        backend_result="",
    )

    assert result["status"] == "PASS"


def catch_fixture(
    code: str,
    path: str = "src/CatchExample.tsx",
    language: str = "tsx",
) -> str:
    return f"""
# Frontend Implementation
## Files
### {path}
```{language}
export async function run() {{
  {code}
}}
```
## API Clarification
- Endpoint: UNKNOWN (미확정)
- Request DTO: UNKNOWN (미확정)
- Response DTO: UNKNOWN (미확정)
"""


def test_tsx_unsafe_catch_property_access_fails() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  console.log(error.message);
}
"""))

    assert "UNSAFE_CATCH_ERROR_ACCESS" in issue_rules(result)


def test_ts_unsafe_catch_property_access_fails() -> None:
    result = validate(catch_fixture(
        "try {} catch (error) { console.log(error.message); }",
        path="src/error.ts",
        language="ts",
    ))

    assert "UNSAFE_CATCH_ERROR_ACCESS" in issue_rules(result)


def test_instanceof_error_guarded_access_passes() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  if (error instanceof Error) {
    console.log(error.message);
  }
}
"""))

    assert result["status"] == "PASS"


def test_access_outside_instanceof_guard_fails() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  if (error instanceof Error) {
    console.log(error.message);
  }
  console.log(error.message);
}
"""))

    assert "UNSAFE_CATCH_ERROR_ACCESS" in issue_rules(result)


def test_any_typed_catch_variable_is_skipped() -> None:
    result = validate(catch_fixture("""
try {} catch (error: any) {
  console.log(error.message);
}
"""))

    assert result["status"] == "PASS"


def test_string_conversion_without_property_access_passes() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  console.log(String(error));
}
"""))

    assert result["status"] == "PASS"


def test_axios_guarded_access_passes() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  if (axios.isAxiosError(error)) {
    console.log(error.message);
  }
}
"""))

    assert result["status"] == "PASS"


def test_jsx_unsafe_catch_access_is_skipped() -> None:
    result = validate(catch_fixture(
        "try {} catch (error) { console.log(error.message); }",
        path="src/CatchExample.jsx",
        language="jsx",
    ))

    assert result["status"] == "PASS"


def test_js_unsafe_catch_access_is_skipped() -> None:
    result = validate(
        catch_fixture(
            "try {} catch (error) { console.log(error.message); }",
            path="src/error.js",
            language="js",
        ),
        user_request="Frontend 코드를 검토해줘",
    )

    assert result["status"] == "PASS"


def test_non_catch_object_message_access_passes() -> None:
    result = validate(catch_fixture("""
const response = { message: 'ok' };
console.log(response.message);
"""))

    assert result["status"] == "PASS"


def test_catch_without_property_access_passes() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  console.log('failed');
}
"""))

    assert result["status"] == "PASS"


def test_multiple_catch_variable_names_are_checked() -> None:
    result = validate(catch_fixture("""
try {} catch (error) {
  console.log(error.message);
}
try {} catch (reason) {
  console.log(reason.name);
}
"""))

    unsafe_issues = [
        issue for issue in result["issues"]
        if issue["rule"] == "UNSAFE_CATCH_ERROR_ACCESS"
    ]
    assert len(unsafe_issues) == 2
    assert any("error.message" in issue["message"] for issue in unsafe_issues)
    assert any("reason.name" in issue["message"] for issue in unsafe_issues)


def test_incomplete_catch_brace_is_skipped() -> None:
    result = validate("""
# Frontend Implementation
## Files
### src/CatchExample.tsx
```tsx
try {} catch (error) {
  console.log(error.message);
```
## API Clarification
- Endpoint: UNKNOWN (미확정)
- Request DTO: UNKNOWN (미확정)
- Response DTO: UNKNOWN (미확정)
""")

    assert result["status"] == "PASS"


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
