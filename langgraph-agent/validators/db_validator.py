import re


def classify_db_task_types(user_request: str) -> set[str]:
    """사용자 요청에서 필요한 DB 작업 유형을 분류한다."""

    request = user_request.strip()
    task_types: set[str] = set()

    patterns = {
        "CREATE_TABLE": [
            r"\bCREATE\s+TABLE\b",
            r"테이블\s*(?:을\s*)?(?:생성|만들)",
        ],
        "SELECT": [
            r"\bSELECT",
            r"(?:데이터|목록|정보|결과|레코드|행)\s*(?:를|을)?\s*(?:조회|검색|집계)",
            r"(?:조회|검색|집계)\s*(?:쿼리|SQL)",
        ],
        "ALTER_TABLE": [
            r"\bALTER\s+TABLE\b",
            r"(?:테이블|컬럼|칼럼)\s*(?:을|를)?\s*(?:변경|수정)",
            r"(?:컬럼|칼럼)\s*(?:을|를)?\s*(?:추가|삭제)",
        ],
        "INDEX": [
            r"\bCREATE\s+(?:UNIQUE\s+)?INDEX",
            r"\b(?:ADD|DROP)\s+INDEX",
            r"인덱스\s*(?:를|을)?\s*(?:생성|추가|삭제|변경)",
        ],
    }

    for task_type, task_patterns in patterns.items():
        if any(
            re.search(pattern, request, re.IGNORECASE)
            for pattern in task_patterns
        ):
            task_types.add(task_type)

    if len(task_types) > 1:
        task_types.add("MIXED")

    if not task_types:
        task_types.add("UNKNOWN")

    return task_types


def validate_db_result(
    db_result: str,
    user_request: str = "",
) -> dict:
    issues = []
    task_types = classify_db_task_types(user_request)

    if "CREATE_TABLE" in task_types:
        # 1. CREATE TABLE 존재 여부
        if not re.search(
            r"\bCREATE\s+TABLE\b",
            db_result,
            re.IGNORECASE,
        ):
            issues.append({
                "severity": "Major",
                "rule": "MISSING_CREATE_TABLE",
                "message": "DB 결과에 CREATE TABLE DDL이 없습니다.",
                "required_fix": "실행 가능한 CREATE TABLE DDL을 작성하세요.",
            })

        # 2. PRIMARY KEY 존재 여부
        if not re.search(
            r"\bPRIMARY\s+KEY\b",
            db_result,
            re.IGNORECASE,
        ):
            issues.append({
                "severity": "Major",
                "rule": "MISSING_PRIMARY_KEY",
                "message": "테이블 정의에 PRIMARY KEY가 없습니다.",
                "required_fix": "적절한 PRIMARY KEY를 정의하세요.",
            })

    if (
        "SELECT" in task_types
        and not re.search(
            r"\bSELECT\b",
            db_result,
            re.IGNORECASE,
        )
    ):
        issues.append({
            "severity": "Major",
            "rule": "MISSING_SELECT",
            "message": "SELECT 요청이지만 DB 결과에 SELECT 구문이 없습니다.",
            "required_fix": "요청에 맞는 실행 가능한 SELECT 구문을 작성하세요.",
        })

    index_statement_pattern = (
        r"\bCREATE\s+(?:UNIQUE\s+)?INDEX\b"
        r"|\bALTER\s+TABLE\b[\s\S]*?\bADD\s+INDEX\b"
    )

    if (
        "INDEX" in task_types
        and not re.search(
            index_statement_pattern,
            db_result,
            re.IGNORECASE,
        )
    ):
        issues.append({
            "severity": "Major",
            "rule": "MISSING_INDEX_STATEMENT",
            "message": "INDEX 요청이지만 DB 결과에 인덱스 생성 또는 추가 구문이 없습니다.",
            "required_fix": (
                "CREATE INDEX, CREATE UNIQUE INDEX 또는 "
                "ALTER TABLE ... ADD INDEX 구문을 작성하세요."
            ),
        })
        issues.append({
            "severity": "Major",
            "rule": "MISSING_INDEX",
            "message": "INDEX 요청에 필요한 인덱스 구문이 누락되었습니다.",
            "required_fix": "인덱스 생성 또는 추가 구문을 작성하세요.",
        })

    # 3. AUTO_INCREMENT 문법 검사
    # MySQL 기준에서 흔한 오타만 잡는다.
    if re.search(
        r"\bAUTO\s+INCREMENT\b",
        db_result,
        re.IGNORECASE,
    ):
        issues.append({
            "severity": "Major",
            "rule": "INVALID_AUTO_INCREMENT",
            "message": "AUTO_INCREMENT 문법이 잘못 작성되었습니다.",
            "required_fix": "MySQL에서는 AUTO_INCREMENT를 사용하세요.",
        })

    # 4. VARCHAR 길이 누락 검사
    # 예: VARCHAR NOT NULL 같은 잘못된 형태
    if re.search(
        r"\bVARCHAR\s+(?:NOT|NULL|UNIQUE|DEFAULT|,|\))",
        db_result,
        re.IGNORECASE,
    ):
        issues.append({
            "severity": "Major",
            "rule": "VARCHAR_LENGTH_MISSING",
            "message": "VARCHAR 타입에 길이 값이 누락된 컬럼이 있습니다.",
            "required_fix": "VARCHAR(50)처럼 적절한 길이를 지정하세요.",
        })

    # 5. TIMESTAMP 기본값 오타 검사
    if re.search(
        r"\bCURRENT_TIMESTAMP\s*\(\s*\)",
        db_result,
        re.IGNORECASE,
    ):
        # MySQL에서는 CURRENT_TIMESTAMP()도 허용되므로
        # 이 항목은 오류로 잡지 않는다.
        pass

    # 6. updated_at 자동 갱신 문법의 명백한 오타 검사
    if re.search(
        r"\bON\s+UPDATE\s+CURRENT\s+TIMESTAMP\b",
        db_result,
        re.IGNORECASE,
    ):
        issues.append({
            "severity": "Major",
            "rule": "INVALID_CURRENT_TIMESTAMP",
            "message": "ON UPDATE CURRENT_TIMESTAMP 문법이 잘못 작성되었습니다.",
            "required_fix": (
                "ON UPDATE CURRENT_TIMESTAMP 형태로 작성하세요."
            ),
        })

    # 7. FOREIGN KEY가 있는데 REFERENCES가 없는 경우
    if (
        re.search(
            r"\bFOREIGN\s+KEY\b",
            db_result,
            re.IGNORECASE,
        )
        and not re.search(
            r"\bREFERENCES\b",
            db_result,
            re.IGNORECASE,
        )
    ):
        issues.append({
            "severity": "Major",
            "rule": "FOREIGN_KEY_WITHOUT_REFERENCES",
            "message": "FOREIGN KEY가 있지만 REFERENCES 정의가 없습니다.",
            "required_fix": (
                "FOREIGN KEY 대상 테이블과 컬럼을 REFERENCES로 지정하세요."
            ),
        })

    # 8. CREATE TABLE 요청에서 DROP TABLE만 출력되는 경우 방지
    if "CREATE_TABLE" in task_types:
        if (
            re.search(
                r"\bDROP\s+TABLE\b",
                db_result,
                re.IGNORECASE,
            )
            and not re.search(
                r"\bCREATE\s+TABLE\b",
                db_result,
                re.IGNORECASE,
            )
        ):
            issues.append({
                "severity": "Major",
                "rule": "DROP_WITHOUT_CREATE",
                "message": "DROP TABLE만 존재하고 CREATE TABLE이 없습니다.",
                "required_fix": "요청된 테이블 생성 DDL을 포함하세요.",
            })

    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
    }
