import unittest

from validators.backend_validator import validate_backend_result


def issue_rules(result: dict) -> set[str]:
    return {issue["rule"] for issue in result["issues"]}


def test_valid_constructor_injection_with_required_imports_passes() -> None:
    backend_result = """
    import java.sql.Timestamp;
    import java.util.Optional;
    import lombok.RequiredArgsConstructor;
    import org.springframework.stereotype.Service;

    @Service
    @RequiredArgsConstructor
    public class MemberService {
        private final MemberRepository memberRepository;

        public Optional<Member> findMember(Long id) {
            Timestamp requestedAt = new Timestamp(System.currentTimeMillis());
            return memberRepository.findById(id);
        }
    }
    """

    result = validate_backend_result(backend_result)

    assert result["status"] == "PASS"
    assert result["issues"] == []


def test_autowired_field_injection_fails() -> None:
    result = validate_backend_result("""
    public class MemberService {
        @Autowired
        private MemberRepository memberRepository;
    }
    """)

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {"FIELD_INJECTION"}


def test_javax_persistence_fails() -> None:
    result = validate_backend_result(
        "import javax.persistence.Entity;"
    )

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {"JAVAX_PERSISTENCE"}


def test_javax_validation_fails() -> None:
    result = validate_backend_result(
        "import javax.validation.Valid;"
    )

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {"JAVAX_VALIDATION"}


def test_required_args_constructor_import_missing_fails() -> None:
    result = validate_backend_result("""
    @RequiredArgsConstructor
    public class MemberService {
        private final MemberRepository memberRepository;
    }
    """)

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {
        "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT"
    }


def test_optional_import_missing_fails() -> None:
    result = validate_backend_result(
        "Optional<Member> findByUsername(String username);"
    )

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {"MISSING_OPTIONAL_IMPORT"}


def test_timestamp_import_missing_fails() -> None:
    result = validate_backend_result(
        "private Timestamp createdAt;"
    )

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {"MISSING_TIMESTAMP_IMPORT"}


def test_multiple_issues_are_all_reported() -> None:
    backend_result = """
    import javax.persistence.Entity;
    import javax.validation.Valid;

    @RequiredArgsConstructor
    public class MemberService {
        @Autowired
        private MemberRepository memberRepository;

        private Optional<Member> member;
        private Timestamp createdAt;
    }
    """

    result = validate_backend_result(backend_result)

    assert result["status"] == "FAIL"
    assert issue_rules(result) == {
        "FIELD_INJECTION",
        "JAVAX_PERSISTENCE",
        "JAVAX_VALIDATION",
        "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT",
        "MISSING_OPTIONAL_IMPORT",
        "MISSING_TIMESTAMP_IMPORT",
    }
    assert len(result["issues"]) == 6


def setter_fixture(entity: str, service_body: str) -> str:
    return f"""
```java
{entity}
```

```java
public class MemberService {{
    public void update() {{
        Member member = new Member();
        {service_body}
    }}
}}
```
"""


def test_setter_call_without_accessor_fails() -> None:
    result = validate_backend_result(setter_fixture(
        "public class Member { private String username; }",
        'member.setUsername("user");',
    ))

    assert issue_rules(result) == {"MISSING_SETTER"}
    assert result["issues"][0]["severity"] == "Major"


def test_class_level_setter_passes() -> None:
    result = validate_backend_result(setter_fixture(
        """import lombok.Setter;
@Setter
public class Member { private String username; }""",
        'member.setUsername("user");',
    ))

    assert result["status"] == "PASS"


def test_direct_setter_method_passes() -> None:
    result = validate_backend_result(setter_fixture(
        """public class Member {
    private String username;
    public void setUsername(String username) { this.username = username; }
}""",
        'member.setUsername("user");',
    ))

    assert result["status"] == "PASS"


def test_field_level_setter_passes() -> None:
    result = validate_backend_result(setter_fixture(
        """import lombok.Setter;
public class Member {
    @Setter
    private String username;
}""",
        'member.setUsername("user");',
    ))

    assert result["status"] == "PASS"


def test_data_annotation_passes() -> None:
    result = validate_backend_result(setter_fixture(
        """import lombok.Data;
@Data
public class Member { private String username; }""",
        'member.setUsername("user");',
    ))

    assert result["status"] == "PASS"


def test_no_setter_call_passes() -> None:
    result = validate_backend_result(setter_fixture(
        "public class Member { private String username; }",
        "member.toString();",
    ))

    assert result["status"] == "PASS"


def test_missing_target_field_is_skipped() -> None:
    result = validate_backend_result(setter_fixture(
        "public class Member { private String email; }",
        'member.setUsername("user");',
    ))

    assert result["status"] == "PASS"


def test_external_class_is_skipped() -> None:
    result = validate_backend_result("""
```java
public class MemberService {
    public void update() {
        Member member = new Member();
        member.setUsername("user");
    }
}
```
""")

    assert result["status"] == "PASS"


def test_extends_class_is_skipped() -> None:
    result = validate_backend_result(setter_fixture(
        "public class Member extends BaseMember { private String username; }",
        'member.setUsername("user");',
    ))

    assert result["status"] == "PASS"


def test_duplicate_class_name_is_skipped() -> None:
    result = validate_backend_result("""
```java
public class Member { private String username; }
```
```java
public class Member { private String username; }
```
```java
public class MemberService {
    public void update() {
        Member member = new Member();
        member.setUsername("user");
    }
}
```
""")

    assert result["status"] == "PASS"


def test_multiple_missing_setters_are_grouped_by_class() -> None:
    result = validate_backend_result(setter_fixture(
        """public class Member {
    private String username;
    private String email;
    private String password;
}""",
        """member.setUsername("user");
        member.setEmail("user@example.com");
        member.setPassword("secret");""",
    ))

    setter_issues = [
        issue for issue in result["issues"]
        if issue["rule"] == "MISSING_SETTER"
    ]
    assert len(setter_issues) == 1
    assert all(
        setter in setter_issues[0]["message"]
        for setter in ("setUsername", "setEmail", "setPassword")
    )


def test_setter_annotation_without_lombok_import_does_not_pass() -> None:
    result = validate_backend_result(setter_fixture(
        """@Setter
public class Member { private String username; }""",
        'member.setUsername("user");',
    ))

    assert "MISSING_SETTER" in issue_rules(result)


def getter_fixture(dto: str, method_body: str, parameter: str = "SignupRequest request") -> str:
    return f"""
```java
{dto}
```

```java
public class SignupService {{
    public SignupResponse signup({parameter}) {{
        {method_body}
        return new SignupResponse();
    }}
}}
```
"""


def test_parameter_getter_call_without_accessor_fails() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private String username; }",
        "request.getUsername();",
    ))
    assert issue_rules(result) == {"MISSING_GETTER"}
    assert result["issues"][0]["severity"] == "Major"


def test_class_level_getter_passes() -> None:
    result = validate_backend_result(getter_fixture(
        """import lombok.Getter;
@Getter
public class SignupRequest { private String username; }""",
        "request.getUsername();",
    ))
    assert result["status"] == "PASS"


def test_direct_getter_method_passes() -> None:
    result = validate_backend_result(getter_fixture(
        """public class SignupRequest {
    private String username;
    public String getUsername() { return username; }
}""",
        "request.getUsername();",
    ))
    assert result["status"] == "PASS"


def test_field_level_getter_passes() -> None:
    result = validate_backend_result(getter_fixture(
        """import lombok.Getter;
public class SignupRequest {
    @Getter
    private String username;
}""",
        "request.getUsername();",
    ))
    assert result["status"] == "PASS"


def test_data_getter_passes() -> None:
    result = validate_backend_result(getter_fixture(
        """import lombok.Data;
@Data
public class SignupRequest { private String username; }""",
        "request.getUsername();",
    ))
    assert result["status"] == "PASS"


def test_no_getter_call_passes() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private String username; }",
        "request.toString();",
    ))
    assert result["status"] == "PASS"


def test_getter_missing_target_field_is_skipped() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private String email; }",
        "request.getUsername();",
    ))
    assert result["status"] == "PASS"


def test_getter_external_class_is_skipped() -> None:
    result = validate_backend_result("""
```java
public class SignupService {
    public void signup(SignupRequest request) {
        request.getUsername();
    }
}
```
""")
    assert result["status"] == "PASS"


def test_getter_extends_class_is_skipped() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest extends BaseRequest { private String username; }",
        "request.getUsername();",
    ))
    assert result["status"] == "PASS"


def test_getter_duplicate_class_name_is_skipped() -> None:
    result = validate_backend_result("""
```java
public class SignupRequest { private String username; }
```
```java
public class SignupRequest { private String username; }
```
```java
public class SignupService {
    public void signup(SignupRequest request) {
        request.getUsername();
    }
}
```
""")
    assert result["status"] == "PASS"


def test_multiple_missing_getters_are_grouped_by_class() -> None:
    result = validate_backend_result(getter_fixture(
        """public class SignupRequest {
    private String username;
    private String email;
    private String password;
}""",
        """request.getUsername();
        request.getEmail();
        request.getPassword();""",
    ))
    getter_issues = [
        issue for issue in result["issues"]
        if issue["rule"] == "MISSING_GETTER"
    ]
    assert len(getter_issues) == 1
    assert all(
        getter in getter_issues[0]["message"]
        for getter in ("getUsername", "getEmail", "getPassword")
    )


def test_getter_annotation_without_lombok_import_fails() -> None:
    result = validate_backend_result(getter_fixture(
        """@Getter
public class SignupRequest { private String username; }""",
        "request.getUsername();",
    ))
    assert "MISSING_GETTER" in issue_rules(result)


def test_request_body_parameter_is_connected() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private String username; }",
        "request.getUsername();",
        parameter="@RequestBody SignupRequest request",
    ))
    assert "MISSING_GETTER" in issue_rules(result)


def test_final_parameter_forms_are_connected() -> None:
    dto = "public class SignupRequest { private String username; }"
    for parameter in (
        "final SignupRequest request",
        "@RequestBody final SignupRequest request",
    ):
        result = validate_backend_result(getter_fixture(
            dto,
            "request.getUsername();",
            parameter=parameter,
        ))
        assert "MISSING_GETTER" in issue_rules(result)


def test_inferred_getter_receiver_is_skipped() -> None:
    result = validate_backend_result("""
```java
public class SignupRequest { private String username; }
```
```java
public class SignupService {
    public void signup() {
        var request = requestFactory.create();
        request.getUsername();
        requestFactory.create().getUsername();
        ((SignupRequest) value).getUsername();
    }
}
```
""")
    assert result["status"] == "PASS"


def test_chained_getter_call_is_skipped() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private String username; }",
        "request.getUsername().trim();",
    ))
    assert result["status"] == "PASS"


def test_boolean_is_accessor_is_skipped() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private boolean active; }",
        "request.isActive();",
    ))
    assert result["status"] == "PASS"


def test_acronym_getter_is_skipped() -> None:
    result = validate_backend_result(getter_fixture(
        "public class SignupRequest { private String URL; }",
        "request.getURL();",
    ))
    assert result["status"] == "PASS"


def test_getter_call_in_different_scope_is_not_connected() -> None:
    result = validate_backend_result("""
```java
public class SignupRequest { private String username; }
```
```java
public class SignupService {
    public void first(SignupRequest request) {
        request.toString();
    }

    public void second() {
        request.getUsername();
    }
}
```
""")
    assert result["status"] == "PASS"


def test_same_variable_name_in_multiple_methods_is_connected_per_scope() -> None:
    result = validate_backend_result("""
```java
public class SignupRequest { private String username; }
```
```java
public class ProfileRequest { private String email; }
```
```java
public class AccountService {
    public void signup(SignupRequest request) {
        request.getUsername();
    }

    public void profile(ProfileRequest request) {
        request.getEmail();
    }
}
```
""")
    getter_issues = [
        issue for issue in result["issues"]
        if issue["rule"] == "MISSING_GETTER"
    ]
    assert len(getter_issues) == 2
    assert any("SignupRequest" in issue["message"] for issue in getter_issues)
    assert any("ProfileRequest" in issue["message"] for issue in getter_issues)


def validation_fixture(
    dto_annotations: str = "@NotBlank",
    parameter_annotations: str = "@RequestBody",
    dto_imports: str = "import jakarta.validation.constraints.NotBlank;",
    controller_imports: str = "",
    class_annotations: str = "",
) -> str:
    return f"""
```java
{dto_imports}
public class SignupRequest {{
    {dto_annotations}
    private String username;
}}
```
```java
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
{controller_imports}
{class_annotations}
@RestController
public class SignupController {{
    public void signup({parameter_annotations} SignupRequest request) {{}}
}}
```
"""


def test_constraint_request_body_without_trigger_fails() -> None:
    result = validate_backend_result(validation_fixture())
    assert "MISSING_VALIDATION_TRIGGER" in issue_rules(result)


def test_valid_jakarta_valid_trigger_passes() -> None:
    result = validate_backend_result(validation_fixture(
        parameter_annotations="@RequestBody @Valid",
        controller_imports="import jakarta.validation.Valid;",
    ))
    assert result["status"] == "PASS"


def test_valid_parameter_validated_trigger_passes() -> None:
    result = validate_backend_result(validation_fixture(
        parameter_annotations="@RequestBody @Validated",
        controller_imports=(
            "import org.springframework.validation.annotation.Validated;"
        ),
    ))
    assert result["status"] == "PASS"


def test_valid_without_import_does_not_trigger_validation() -> None:
    result = validate_backend_result(validation_fixture(
        parameter_annotations="@RequestBody @Valid",
    ))
    assert "MISSING_VALIDATION_TRIGGER" in issue_rules(result)


def test_constraint_without_import_is_skipped() -> None:
    result = validate_backend_result(validation_fixture(dto_imports=""))
    assert result["status"] == "PASS"


def test_dto_without_constraint_passes() -> None:
    result = validate_backend_result(validation_fixture(
        dto_annotations="",
        dto_imports="",
    ))
    assert result["status"] == "PASS"


def test_external_constrained_dto_is_skipped() -> None:
    result = validate_backend_result("""
```java
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;
@RestController
public class SignupController {
    public void signup(@RequestBody SignupRequest request) {}
}
```
""")
    assert result["status"] == "PASS"


def test_duplicate_constrained_dto_is_skipped() -> None:
    dto = """
```java
import jakarta.validation.constraints.NotBlank;
public class SignupRequest {
    @NotBlank
    private String username;
}
```
"""
    controller = validation_fixture().split("```java", 2)[-1]
    result = validate_backend_result(dto + dto + "```java" + controller)
    assert result["status"] == "PASS"


def test_non_request_body_parameter_is_skipped() -> None:
    result = validate_backend_result(validation_fixture(
        parameter_annotations="",
    ))
    assert result["status"] == "PASS"


def test_validation_group_is_skipped() -> None:
    result = validate_backend_result(validation_fixture(
        dto_annotations="@NotBlank(groups = Create.class)",
    ))
    assert result["status"] == "PASS"


def test_multiple_constraints_create_one_validation_trigger_issue() -> None:
    result = validate_backend_result(validation_fixture(
        dto_annotations="""@NotBlank
    @Email
    @Size(min = 8)""",
        dto_imports="""import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.Size;""",
    ))
    issues = [
        issue for issue in result["issues"]
        if issue["rule"] == "MISSING_VALIDATION_TRIGGER"
    ]
    assert len(issues) == 1


def test_javax_valid_keeps_existing_rule() -> None:
    result = validate_backend_result(validation_fixture(
        parameter_annotations="@RequestBody @Valid",
        controller_imports="import javax.validation.Valid;",
    ))
    assert "JAVAX_VALIDATION" in issue_rules(result)
    assert "MISSING_VALIDATION_TRIGGER" in issue_rules(result)


def test_fully_qualified_jakarta_annotations_are_recognized() -> None:
    result = validate_backend_result(validation_fixture(
        dto_annotations="@jakarta.validation.constraints.NotBlank",
        dto_imports="",
        parameter_annotations="@RequestBody @jakarta.validation.Valid",
    ))
    assert result["status"] == "PASS"


def test_class_level_validated_is_skipped() -> None:
    result = validate_backend_result(validation_fixture(
        class_annotations="@Validated",
        controller_imports=(
            "import org.springframework.validation.annotation.Validated;"
        ),
    ))
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
