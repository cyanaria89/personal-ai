import re


JAVA_BLOCK_PATTERN = re.compile(
    r"(```java[ \t]*\r?\n)(.*?)(^[ \t]*```[ \t]*$)",
    re.MULTILINE | re.DOTALL | re.IGNORECASE,
)

AUTOWIRED_IMPORT = (
    "import org.springframework.beans.factory.annotation.Autowired;"
)

SUPPORTED_IMPORT_FIXES = {
    "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT": (
        "import lombok.RequiredArgsConstructor;"
    ),
    "MISSING_OPTIONAL_IMPORT": "import java.util.Optional;",
    "MISSING_TIMESTAMP_IMPORT": "import java.sql.Timestamp;",
}


def _has_import(code: str, import_statement: str) -> bool:
    return bool(
        re.search(
            rf"^[ \t]*{re.escape(import_statement)}[ \t]*$",
            code,
            re.MULTILINE,
        )
    )


def _code_without_imports(code: str) -> str:
    return re.sub(
        r"^[ \t]*import\s+[^;]+;[ \t]*$",
        "",
        code,
        flags=re.MULTILINE,
    )


def _insert_imports(
    code: str,
    imports_to_add: list[str],
) -> str:
    if not imports_to_add:
        return code

    lines = code.splitlines(keepends=True)
    import_line_indexes = [
        index
        for index, line in enumerate(lines)
        if re.match(r"^[ \t]*import\s+[^;]+;[ \t]*(?:\r?\n)?$", line)
    ]

    if import_line_indexes:
        insert_at = import_line_indexes[-1] + 1
    else:
        package_line_indexes = [
            index
            for index, line in enumerate(lines)
            if re.match(
                r"^[ \t]*package\s+[\w.]+;[ \t]*(?:\r?\n)?$",
                line,
            )
        ]

        if package_line_indexes:
            insert_at = package_line_indexes[-1] + 1
        else:
            insert_at = next(
                (
                    index
                    for index, line in enumerate(lines)
                    if re.match(
                        r"^[ \t]*(?:@|(?:public\s+|protected\s+|private\s+)?"
                        r"(?:class|interface|record|enum)\b)",
                        line,
                    )
                ),
                0,
            )

    newline = "\r\n" if "\r\n" in code else "\n"
    new_import_lines = [
        f"{import_statement}{newline}"
        for import_statement in imports_to_add
    ]
    lines[insert_at:insert_at] = new_import_lines

    return "".join(lines)


def _fix_java_block(
    code: str,
    issue_rules: set[str],
    dto_imports: list[tuple[str, str]],
) -> tuple[str, set[str]]:
    fixed_code = code
    applied_fixes: set[str] = set()
    code_without_imports = _code_without_imports(fixed_code)

    if (
        _has_import(fixed_code, AUTOWIRED_IMPORT)
        and not re.search(r"@Autowired\b", code_without_imports)
    ):
        fixed_code = re.sub(
            rf"^[ \t]*{re.escape(AUTOWIRED_IMPORT)}[ \t]*(?:\r?\n)?",
            "",
            fixed_code,
            count=1,
            flags=re.MULTILINE,
        )
        applied_fixes.add("UNUSED_AUTOWIRED_IMPORT")
        code_without_imports = _code_without_imports(fixed_code)

    imports_to_add: list[tuple[str, str]] = []

    if (
        "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT" in issue_rules
        and re.search(r"@RequiredArgsConstructor\b", code_without_imports)
        and not _has_import(
            fixed_code,
            SUPPORTED_IMPORT_FIXES[
                "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT"
            ],
        )
    ):
        imports_to_add.append((
            "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT",
            SUPPORTED_IMPORT_FIXES[
                "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT"
            ],
        ))

    package_match = re.search(
        r"(?m)^\s*package\s+([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)\s*;",
        fixed_code,
    )
    current_package = package_match.group(1) if package_match else None
    code_without_imports = _code_without_imports(fixed_code)

    for dto_package, type_name in sorted(set(dto_imports)):
        import_statement = f"import {dto_package}.{type_name};"
        if (
            current_package is None
            or current_package == dto_package
            or not re.search(rf"\b{re.escape(type_name)}\b", code_without_imports)
            or re.search(
                rf"\b{re.escape(dto_package)}\.{re.escape(type_name)}\b",
                code_without_imports,
            )
            or _has_import(fixed_code, import_statement)
            or re.search(
                rf"(?m)^\s*import\s+{re.escape(dto_package)}\.\*\s*;",
                fixed_code,
            )
        ):
            continue
        imports_to_add.append((
            f"MISSING_DTO_IMPORT:{dto_package}.{type_name}",
            import_statement,
        ))

    if (
        "MISSING_OPTIONAL_IMPORT" in issue_rules
        and re.search(r"\bOptional\s*<", code_without_imports)
        and not _has_import(
            fixed_code,
            SUPPORTED_IMPORT_FIXES["MISSING_OPTIONAL_IMPORT"],
        )
    ):
        imports_to_add.append((
            "MISSING_OPTIONAL_IMPORT",
            SUPPORTED_IMPORT_FIXES["MISSING_OPTIONAL_IMPORT"],
        ))

    if (
        "MISSING_TIMESTAMP_IMPORT" in issue_rules
        and re.search(r"\bTimestamp\b", code_without_imports)
        and not _has_import(
            fixed_code,
            SUPPORTED_IMPORT_FIXES["MISSING_TIMESTAMP_IMPORT"],
        )
    ):
        imports_to_add.append((
            "MISSING_TIMESTAMP_IMPORT",
            SUPPORTED_IMPORT_FIXES["MISSING_TIMESTAMP_IMPORT"],
        ))

    fixed_code = _insert_imports(
        fixed_code,
        [import_statement for _, import_statement in imports_to_add],
    )
    applied_fixes.update(rule for rule, _ in imports_to_add)

    return fixed_code, applied_fixes


def auto_fix_backend_result(
    backend_result: str,
    issues: list[dict],
) -> tuple[str, list[str]]:
    """Java 코드 블록의 결정적인 import 문제만 수정한다."""

    issue_rules = {
        str(issue.get("rule", ""))
        for issue in issues
        if isinstance(issue, dict)
    }
    applied_fixes: set[str] = set()

    fence_marker = None
    for line in backend_result.splitlines():
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match is None:
            continue
        marker = fence_match.group(1)[0]
        if fence_marker is None:
            fence_marker = marker
        elif marker == fence_marker:
            fence_marker = None
    if fence_marker is not None:
        return backend_result, []

    java_matches = list(JAVA_BLOCK_PATTERN.finditer(backend_result))
    owners_by_block: list[set[str]] = []
    owner_counts: dict[str, int] = {}
    for match in java_matches:
        owners = set(re.findall(
            r"\b(?:class|record|interface|enum)\s+([A-Z][A-Za-z0-9_]*)",
            match.group(2),
        ))
        owners_by_block.append(owners)
        for owner in owners:
            owner_counts[owner] = owner_counts.get(owner, 0) + 1

    packages_by_type: dict[str, set[str]] = {}
    dto_fixes_by_owner: dict[str, list[tuple[str, str]]] = {}
    for issue in issues:
        if not isinstance(issue, dict) or issue.get("rule") != "MISSING_DTO_IMPORT":
            continue
        owner = issue.get("target_java_type")
        type_name = issue.get("missing_type")
        dto_package = issue.get("target_package")
        if not all(
            isinstance(value, str)
            and re.fullmatch(r"[A-Za-z_]\w*", value)
            for value in (owner, type_name)
        ) or not isinstance(dto_package, str) or not re.fullmatch(
            r"[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*",
            dto_package,
        ):
            continue
        packages_by_type.setdefault(type_name, set()).add(dto_package)
        dto_fixes_by_owner.setdefault(owner, []).append((dto_package, type_name))

    safe_dto_fixes_by_owner = {
        owner: [
            (dto_package, type_name)
            for dto_package, type_name in candidates
            if len(packages_by_type.get(type_name, set())) == 1
        ]
        for owner, candidates in dto_fixes_by_owner.items()
        if owner_counts.get(owner) == 1
    }

    block_index = 0

    def replace_java_block(match: re.Match) -> str:
        nonlocal block_index
        owners = owners_by_block[block_index]
        block_index += 1
        dto_imports = []
        for owner in owners:
            dto_imports.extend(safe_dto_fixes_by_owner.get(owner, []))
        fixed_code, block_fixes = _fix_java_block(
            match.group(2),
            issue_rules,
            dto_imports,
        )
        applied_fixes.update(block_fixes)

        return "".join([
            match.group(1),
            fixed_code,
            match.group(3),
        ])

    fixed_result = JAVA_BLOCK_PATTERN.sub(
        replace_java_block,
        backend_result,
    )

    return fixed_result, sorted(applied_fixes)
