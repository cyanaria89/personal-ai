import unittest

from validators.backend_auto_fixer import auto_fix_backend_result
from validators.backend_validator import validate_backend_result


def issue(rule: str) -> dict:
    return {"rule": rule}


def java_block(code: str) -> str:
    return f"```java\n{code.strip()}\n```"


def test_required_args_constructor_import_is_added() -> None:
    source = java_block("""
    import org.springframework.stereotype.Service;

    @Service
    @RequiredArgsConstructor
    public class MemberService {}
    """)
    fixed, applied = auto_fix_backend_result(
        source,
        [issue("MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT")],
    )

    assert "import lombok.RequiredArgsConstructor;" in fixed
    assert applied == ["MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT"]


def test_required_args_constructor_import_is_added_to_each_block() -> None:
    source = "\n\n".join([
        java_block("@RequiredArgsConstructor\npublic class Service {}"),
        java_block("@RequiredArgsConstructor\npublic class Controller {}"),
    ])
    fixed, _ = auto_fix_backend_result(
        source,
        [issue("MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT")],
    )

    assert fixed.count("import lombok.RequiredArgsConstructor;") == 2


def test_optional_import_is_added() -> None:
    source = java_block(
        "public interface Repository { Optional<Member> find(); }"
    )
    fixed, applied = auto_fix_backend_result(
        source,
        [issue("MISSING_OPTIONAL_IMPORT")],
    )

    assert "import java.util.Optional;" in fixed
    assert applied == ["MISSING_OPTIONAL_IMPORT"]


def test_timestamp_import_is_added() -> None:
    source = java_block(
        "public class Member { private Timestamp createdAt; }"
    )
    fixed, applied = auto_fix_backend_result(
        source,
        [issue("MISSING_TIMESTAMP_IMPORT")],
    )

    assert "import java.sql.Timestamp;" in fixed
    assert applied == ["MISSING_TIMESTAMP_IMPORT"]


def test_unused_autowired_import_is_removed() -> None:
    source = java_block("""
    import org.springframework.beans.factory.annotation.Autowired;

    public class MemberService {}
    """)
    fixed, applied = auto_fix_backend_result(source, [])

    assert "import org.springframework.beans.factory.annotation.Autowired;" not in fixed
    assert applied == ["UNUSED_AUTOWIRED_IMPORT"]


def test_autowired_import_is_kept_when_annotation_is_used() -> None:
    source = java_block("""
    import org.springframework.beans.factory.annotation.Autowired;

    public class MemberService {
        @Autowired
        private MemberRepository repository;
    }
    """)
    fixed, applied = auto_fix_backend_result(source, [])

    assert "import org.springframework.beans.factory.annotation.Autowired;" in fixed
    assert applied == []


def test_existing_import_is_not_duplicated() -> None:
    source = java_block("""
    import lombok.RequiredArgsConstructor;

    @RequiredArgsConstructor
    public class MemberService {}
    """)
    fixed, applied = auto_fix_backend_result(
        source,
        [issue("MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT")],
    )

    assert fixed.count("import lombok.RequiredArgsConstructor;") == 1
    assert applied == []


def test_import_is_not_added_without_related_issue() -> None:
    source = java_block("""
    @RequiredArgsConstructor
    public class MemberService {
        private Timestamp createdAt;
        private Optional<Member> member;
    }
    """)
    fixed, applied = auto_fix_backend_result(source, [])

    assert fixed == source
    assert applied == []


def test_markdown_outside_java_blocks_is_preserved() -> None:
    source = """
# Backend Agent Output

## Notes
Timestamp and @RequiredArgsConstructor 설명은 유지합니다.

```json
{"endpoint": "/api/members"}
```

```java
public class Member { private Timestamp createdAt; }
```

## Frontend Handoff
- Endpoint: /api/members
""".strip()
    fixed, _ = auto_fix_backend_result(
        source,
        [issue("MISSING_TIMESTAMP_IMPORT")],
    )

    before_java, after_java = source.split("```java", 1)
    fixed_before_java, fixed_after_java = fixed.split("```java", 1)
    assert fixed_before_java == before_java
    assert fixed_after_java.split("```", 1)[1] == after_java.split("```", 1)[1]
    assert '{"endpoint": "/api/members"}' in fixed


def test_combined_import_fixes_and_cleanup() -> None:
    source = java_block("""
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Service;

    @Service
    @RequiredArgsConstructor
    public class MemberService {
        private Optional<Member> member;
        private Timestamp createdAt;
    }
    """)
    first_validation = validate_backend_result(source)
    assert first_validation["status"] == "FAIL"

    fixed, applied = auto_fix_backend_result(
        source,
        first_validation["issues"],
    )
    second_validation = validate_backend_result(fixed)

    assert second_validation["status"] == "PASS"
    assert applied == [
        "MISSING_OPTIONAL_IMPORT",
        "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT",
        "MISSING_TIMESTAMP_IMPORT",
        "UNUSED_AUTOWIRED_IMPORT",
    ]


def test_field_injection_is_not_auto_fixed() -> None:
    source = java_block("""
    import org.springframework.beans.factory.annotation.Autowired;

    public class MemberService {
        @Autowired
        private MemberRepository repository;
    }
    """)
    first_validation = validate_backend_result(source)
    assert issue_rules(first_validation) == {"FIELD_INJECTION"}

    fixed, applied = auto_fix_backend_result(
        source,
        first_validation["issues"],
    )
    second_validation = validate_backend_result(fixed)

    assert fixed == source
    assert applied == []
    assert second_validation["status"] == "FAIL"
    assert issue_rules(second_validation) == {"FIELD_INJECTION"}


def issue_rules(result: dict) -> set[str]:
    return {item["rule"] for item in result["issues"]}


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
