import unittest

from validators.db_validator import validate_db_result


def issue_rules(result: dict) -> set[str]:
    return {issue["rule"] for issue in result["issues"]}


def test_existing_invalid_create_table_case() -> None:
    db_result = """
    CREATE TABLE members (
        id BIGINT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR NOT NULL,
        email VARCHAR(100) NOT NULL,
        role VARCHAR(20),
        team_id BIGINT,
        FOREIGN KEY (team_id)
    );
    """
    result = validate_db_result(db_result, "members 테이블을 생성해줘")

    assert result["status"] == "FAIL"
    assert "VARCHAR_LENGTH_MISSING" in issue_rules(result)
    assert "FOREIGN_KEY_WITHOUT_REFERENCES" in issue_rules(result)


def test_valid_create_table_passes() -> None:
    result = validate_db_result(
        "CREATE TABLE members (id BIGINT PRIMARY KEY, username VARCHAR(100));",
        "members 테이블을 생성해줘",
    )
    assert result["status"] == "PASS"


def test_create_table_without_varchar_length_fails() -> None:
    result = validate_db_result(
        "CREATE TABLE members (id BIGINT PRIMARY KEY, username VARCHAR NOT NULL);",
        "members 테이블을 생성해줘",
    )
    assert result["status"] == "FAIL"
    assert "VARCHAR_LENGTH_MISSING" in issue_rules(result)


def test_valid_select_passes() -> None:
    result = validate_db_result(
        "SELECT id, username FROM members WHERE id = 1;",
        "회원 정보를 SELECT로 조회해줘",
    )
    assert result["status"] == "PASS"


def test_select_request_without_select_fails() -> None:
    result = validate_db_result(
        "회원 정보 조회 방법을 설명합니다.",
        "회원 정보를 SELECT로 조회해줘",
    )
    assert result["status"] == "FAIL"
    assert "MISSING_SELECT" in issue_rules(result)


def test_valid_alter_table_passes() -> None:
    result = validate_db_result(
        "ALTER TABLE members ADD COLUMN nickname VARCHAR(50);",
        "members 테이블에 nickname 컬럼을 추가해줘",
    )
    assert result["status"] == "PASS"


def test_valid_index_creation_passes() -> None:
    result = validate_db_result(
        "CREATE INDEX idx_members_username ON members (username);",
        "members username 인덱스를 생성해줘",
    )
    assert result["status"] == "PASS"


def test_mixed_request_requires_create_table() -> None:
    result = validate_db_result(
        "CREATE INDEX idx_members_username ON members (username);",
        "members 테이블을 생성하고 username 인덱스를 추가해줘",
    )
    assert result["status"] == "FAIL"
    assert "MISSING_CREATE_TABLE" in issue_rules(result)


def test_mixed_request_requires_index() -> None:
    result = validate_db_result(
        "CREATE TABLE members (id BIGINT PRIMARY KEY, username VARCHAR(100));",
        "members 테이블을 생성하고 username 인덱스를 추가해줘",
    )
    assert result["status"] == "FAIL"
    assert "MISSING_INDEX" in issue_rules(result)


def test_unknown_request_does_not_require_create_table_or_primary_key() -> None:
    result = validate_db_result(
        "DB 작업 결과를 검토했습니다.",
        "DB 작업 결과를 검토해줘",
    )
    assert result["status"] == "PASS"
    assert "MISSING_CREATE_TABLE" not in issue_rules(result)
    assert "MISSING_PRIMARY_KEY" not in issue_rules(result)


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
