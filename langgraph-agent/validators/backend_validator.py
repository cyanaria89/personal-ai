import re


JAVA_BLOCK_PATTERN = re.compile(r"```java\s*\n(.*?)```", re.DOTALL | re.IGNORECASE)

VALIDATION_CONSTRAINTS = {
    "NotBlank",
    "NotNull",
    "NotEmpty",
    "Email",
    "Size",
    "Pattern",
    "Min",
    "Max",
    "Positive",
    "Negative",
}


def _missing_dto_import_issues(
    backend_result: str,
    project_context: dict | None = None,
) -> list[dict]:
    """명시적인 dto package 정의와 다른 package의 사용만 연결한다."""
    definitions: dict[str, set[str]] = {}
    blocks = JAVA_BLOCK_PATTERN.findall(backend_result)
    definition_sources = [*blocks]
    if isinstance(project_context, dict):
        for file_context in project_context.get("selected_files", []):
            if (
                isinstance(file_context, dict)
                and file_context.get("language") == "java"
                and isinstance(file_context.get("content"), str)
            ):
                definition_sources.append(file_context["content"])

    for block in definition_sources:
        package_match = re.search(
            r"(?m)^\s*package\s+([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)\s*;",
            block,
        )
        if package_match is None or not re.search(
            r"(?:^|\.)dto(?:\.|$)",
            package_match.group(1),
            re.IGNORECASE,
        ):
            continue
        for type_name in re.findall(
            r"\b(?:public\s+)?(?:class|record|interface|enum)\s+"
            r"([A-Z][A-Za-z0-9_]*)\b",
            block,
        ):
            definitions.setdefault(type_name, set()).add(package_match.group(1))

    unambiguous_definitions = {
        type_name: next(iter(packages))
        for type_name, packages in definitions.items()
        if len(packages) == 1
    }
    missing: set[tuple[str, str, str]] = set()

    for block in blocks:
        package_match = re.search(
            r"(?m)^\s*package\s+([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*)\s*;",
            block,
        )
        if package_match is None:
            continue
        current_package = package_match.group(1)
        code_without_imports = re.sub(
            r"(?m)^\s*(?:package|import)\s+[^;]+;\s*$",
            "",
            block,
        )

        for type_name, dto_package in unambiguous_definitions.items():
            if current_package == dto_package:
                continue
            if not re.search(rf"\b{re.escape(type_name)}\b", code_without_imports):
                continue
            if re.search(
                rf"\b{re.escape(dto_package)}\.{re.escape(type_name)}\b",
                code_without_imports,
            ):
                continue
            has_direct_import = re.search(
                rf"(?m)^\s*import\s+{re.escape(dto_package)}\."
                rf"{re.escape(type_name)}\s*;",
                block,
            )
            has_wildcard_import = re.search(
                rf"(?m)^\s*import\s+{re.escape(dto_package)}\.\*\s*;",
                block,
            )
            if has_direct_import or has_wildcard_import:
                continue
            owner_match = re.search(
                r"\b(?:class|record|interface|enum)\s+([A-Z][A-Za-z0-9_]*)",
                block,
            )
            owner = owner_match.group(1) if owner_match else current_package
            missing.add((owner, type_name, dto_package))

    return [
        {
            "severity": "Major",
            "rule": "MISSING_DTO_IMPORT",
            "target_java_type": owner,
            "missing_type": type_name,
            "target_package": dto_package,
            "message": (
                f"{owner}에서 다른 package의 DTO {type_name}을 사용하지만 "
                "명시적인 import가 없습니다."
            ),
            "required_fix": f"import {dto_package}.{type_name}; 를 추가하세요.",
        }
        for owner, type_name, dto_package in sorted(missing)
    ]


def _matching_brace(text: str, opening_index: int) -> int | None:
    depth = 0
    for index in range(opening_index, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    return None


def _lombok_annotation_available(
    java_block: str,
    annotation: str,
) -> bool:
    return bool(
        re.search(
            rf"import\s+lombok\.{re.escape(annotation)}\s*;",
            java_block,
        )
        or re.search(r"import\s+lombok\.\*\s*;", java_block)
    )


def _has_valid_annotation(
    annotation_text: str,
    java_block: str,
    annotation: str,
) -> bool:
    if re.search(rf"@lombok\.{re.escape(annotation)}\b", annotation_text):
        return True
    return bool(
        re.search(rf"@{re.escape(annotation)}\b", annotation_text)
        and _lombok_annotation_available(java_block, annotation)
    )


def _extract_classes(java_blocks: list[str]) -> dict[str, list[dict]]:
    classes: dict[str, list[dict]] = {}
    class_pattern = re.compile(
        r"(?P<annotations>(?:\s*@(?:[\w.]+)(?:\([^\n]*\))?\s*)*)"
        r"(?:(?:public|protected|private|abstract|final|static)\s+)*"
        r"class\s+(?P<name>[A-Za-z_]\w*)"
        r"(?P<extends>\s+extends\s+[\w.<>, ?]+)?[^\{]*\{"
    )

    for block in java_blocks:
        for match in class_pattern.finditer(block):
            opening_index = match.end() - 1
            closing_index = _matching_brace(block, opening_index)
            if closing_index is None:
                continue
            classes.setdefault(match.group("name"), []).append({
                "annotations": match.group("annotations") or "",
                "body": block[opening_index + 1:closing_index],
                "extends": bool(match.group("extends")),
                "block": block,
            })
    return classes


def _field_declaration(class_body: str, field_name: str) -> re.Match | None:
    return re.search(
        rf"(?m)^(?P<annotations>(?:\s*@(?:[\w.]+)(?:\([^\n]*\))?\s*)*)"
        rf"\s*(?:private|protected|public)\s+"
        rf"(?:final\s+)?(?:static\s+)?[\w.<>, ?\[\]]+\s+"
        rf"{re.escape(field_name)}\s*(?:=[^;]*)?;",
        class_body,
    )


def _missing_setter_issues(backend_result: str) -> list[dict]:
    java_blocks = JAVA_BLOCK_PATTERN.findall(backend_result)
    classes = _extract_classes(java_blocks)
    missing_by_class: dict[str, set[str]] = {}

    for block in java_blocks:
        declarations = re.findall(
            r"\b([A-Z][A-Za-z0-9_]*)\s+([a-zA-Z_]\w*)\s*=\s*"
            r"new\s+\1\s*\(",
            block,
        )
        variable_types: dict[str, set[str]] = {}
        for type_name, variable_name in declarations:
            variable_types.setdefault(variable_name, set()).add(type_name)

        for variable_name, type_names in variable_types.items():
            if len(type_names) != 1:
                continue
            type_name = next(iter(type_names))
            definitions = classes.get(type_name, [])
            if len(definitions) != 1 or definitions[0]["extends"]:
                continue

            definition = definitions[0]
            class_has_setter = _has_valid_annotation(
                definition["annotations"], definition["block"], "Setter"
            )
            class_has_data = _has_valid_annotation(
                definition["annotations"], definition["block"], "Data"
            )

            called_setters = set(re.findall(
                rf"\b{re.escape(variable_name)}\.set([A-Z]\w*)\s*\(",
                block,
            ))
            for property_suffix in called_setters:
                field_name = property_suffix[0].lower() + property_suffix[1:]
                field_match = _field_declaration(definition["body"], field_name)
                if field_match is None:
                    continue
                field_has_setter = _has_valid_annotation(
                    field_match.group("annotations") or "",
                    definition["block"],
                    "Setter",
                )
                direct_setter = re.search(
                    rf"\b(?:public|protected|private)\s+"
                    rf"(?:[\w.<>, ?\[\]]+\s+)?set{re.escape(property_suffix)}"
                    rf"\s*\([^)]*\)\s*\{{",
                    definition["body"],
                )
                if not (class_has_setter or class_has_data or field_has_setter or direct_setter):
                    missing_by_class.setdefault(type_name, set()).add(
                        f"set{property_suffix}"
                    )

    issues = []
    for class_name, setters in sorted(missing_by_class.items()):
        setter_names = ", ".join(sorted(setters))
        issues.append({
            "severity": "Major",
            "rule": "MISSING_SETTER",
            "message": (
                f"{class_name} 타입에서 호출된 setter가 제공되지 않습니다: "
                f"{setter_names}"
            ),
            "required_fix": (
                f"{class_name}의 변경 정책을 유지하면서 필요한 setter를 "
                "실제 코드에 제공하세요."
            ),
        })
    return issues


def _method_parameters(parameters: str) -> dict[str, set[str]]:
    variable_types: dict[str, set[str]] = {}
    if not parameters.strip():
        return variable_types

    parameter_pattern = re.compile(
        r"^(?:@[\w.]+(?:\([^)]*\))?\s+)*"
        r"(?:final\s+)?"
        r"([A-Z][A-Za-z0-9_]*)\s+([A-Za-z_]\w*)$"
    )

    for parameter in parameters.split(","):
        match = parameter_pattern.fullmatch(parameter.strip())
        if match is None:
            continue
        type_name, variable_name = match.groups()
        variable_types.setdefault(variable_name, set()).add(type_name)

    return variable_types


def _extract_methods(java_block: str) -> list[dict]:
    methods = []
    method_pattern = re.compile(
        r"(?:(?:public|protected|private|static|final|synchronized|default)\s+)+"
        r"[\w.<>, ?\[\]]+\s+[A-Za-z_]\w*\s*"
        r"\((?P<parameters>[^()]*)\)\s*"
        r"(?:throws\s+[^\{]+)?\{"
    )

    for match in method_pattern.finditer(java_block):
        opening_index = match.end() - 1
        closing_index = _matching_brace(java_block, opening_index)
        if closing_index is None:
            continue
        methods.append({
            "parameters": match.group("parameters"),
            "body": java_block[opening_index + 1:closing_index],
        })
    return methods


def _direct_getter_exists(class_body: str, getter_name: str) -> bool:
    return bool(re.search(
        rf"(?m)^\s*"
        rf"(?:(?:public|protected|private|static|final|synchronized|abstract)\s+)*"
        rf"[\w.<>, ?\[\]]+\s+{re.escape(getter_name)}"
        rf"\s*\(\s*\)\s*(?:throws\s+[^\{{;]+)?[\{{;]",
        class_body,
    ))


def _missing_getter_issues(backend_result: str) -> list[dict]:
    java_blocks = JAVA_BLOCK_PATTERN.findall(backend_result)
    classes = _extract_classes(java_blocks)
    missing_by_class: dict[str, set[str]] = {}

    for block in java_blocks:
        for method in _extract_methods(block):
            variable_types = _method_parameters(method["parameters"])

            for variable_name, type_names in variable_types.items():
                if len(type_names) != 1:
                    continue
                type_name = next(iter(type_names))
                definitions = classes.get(type_name, [])
                if len(definitions) != 1 or definitions[0]["extends"]:
                    continue

                definition = definitions[0]
                class_has_getter = _has_valid_annotation(
                    definition["annotations"], definition["block"], "Getter"
                )
                class_has_data = _has_valid_annotation(
                    definition["annotations"], definition["block"], "Data"
                )
                getter_pattern = re.compile(
                    rf"\b{re.escape(variable_name)}\.get([A-Z]\w*)"
                    rf"\s*\(\s*\)(?!\s*\.)"
                )

                for getter_match in getter_pattern.finditer(method["body"]):
                    property_suffix = getter_match.group(1)
                    if (
                        len(property_suffix) >= 2
                        and property_suffix[:2].isupper()
                    ):
                        continue

                    field_name = (
                        property_suffix[0].lower()
                        + property_suffix[1:]
                    )
                    field_match = _field_declaration(
                        definition["body"],
                        field_name,
                    )
                    if field_match is None:
                        continue

                    field_has_getter = _has_valid_annotation(
                        field_match.group("annotations") or "",
                        definition["block"],
                        "Getter",
                    )
                    getter_name = f"get{property_suffix}"
                    direct_getter = _direct_getter_exists(
                        definition["body"],
                        getter_name,
                    )

                    if not (
                        class_has_getter
                        or class_has_data
                        or field_has_getter
                        or direct_getter
                    ):
                        missing_by_class.setdefault(type_name, set()).add(
                            getter_name
                        )

    issues = []
    for class_name, getters in sorted(missing_by_class.items()):
        getter_names = ", ".join(sorted(getters))
        issues.append({
            "severity": "Major",
            "rule": "MISSING_GETTER",
            "message": (
                f"{class_name} 타입에서 호출된 getter가 제공되지 않습니다: "
                f"{getter_names}"
            ),
            "required_fix": (
                f"{class_name}의 노출 정책을 유지하면서 필요한 getter를 "
                "실제 코드에 제공하세요."
            ),
        })
    return issues


def _annotation_available(
    java_block: str,
    package_name: str,
    annotation: str,
) -> bool:
    return bool(
        re.search(
            rf"import\s+{re.escape(package_name)}\."
            rf"{re.escape(annotation)}\s*;",
            java_block,
        )
        or re.search(
            rf"import\s+{re.escape(package_name)}\.\*\s*;",
            java_block,
        )
    )


def _has_valid_imported_annotation(
    annotation_text: str,
    java_block: str,
    package_name: str,
    annotation: str,
) -> bool:
    if re.search(
        rf"@{re.escape(package_name)}\.{re.escape(annotation)}\b",
        annotation_text,
    ):
        return True
    return bool(
        re.search(rf"@{re.escape(annotation)}\b", annotation_text)
        and _annotation_available(java_block, package_name, annotation)
    )


def _split_parameters(parameters: str) -> list[str]:
    parts = []
    start = 0
    depth = 0
    for index, char in enumerate(parameters):
        if char in "(<[{":
            depth += 1
        elif char in ")>]}":
            depth = max(0, depth - 1)
        elif char == "," and depth == 0:
            parts.append(parameters[start:index].strip())
            start = index + 1
    final_part = parameters[start:].strip()
    if final_part:
        parts.append(final_part)
    return parts


def _matching_parenthesis(text: str, opening_index: int) -> int | None:
    depth = 0
    for index in range(opening_index, len(text)):
        if text[index] == "(":
            depth += 1
        elif text[index] == ")":
            depth -= 1
            if depth == 0:
                return index
    return None


def _controller_methods(class_body: str) -> list[dict]:
    methods = []
    method_start_pattern = re.compile(
        r"(?P<annotations>(?:\s*@[\w.]+(?:\([^\n]*\))?\s*)*)"
        r"(?:(?:public|protected|private|static|final|synchronized)\s+)+"
        r"[\w.<>, ?\[\]]+\s+[A-Za-z_]\w*\s*\("
    )

    for match in method_start_pattern.finditer(class_body):
        parameter_open = match.end() - 1
        parameter_close = _matching_parenthesis(class_body, parameter_open)
        if parameter_close is None:
            continue
        suffix = class_body[parameter_close + 1:]
        body_match = re.match(r"\s*(?:throws\s+[^\{]+)?\{", suffix)
        if body_match is None:
            continue
        methods.append({
            "annotations": match.group("annotations") or "",
            "parameters": class_body[parameter_open + 1:parameter_close],
        })
    return methods


def _parameter_parts(parameter: str) -> tuple[str, str, str] | None:
    match = re.fullmatch(
        r"(?P<annotations>(?:@[\w.]+(?:\([^)]*\))?\s+)*)"
        r"(?:final\s+)?"
        r"(?P<type>[A-Z][A-Za-z0-9_]*)\s+"
        r"(?P<variable>[A-Za-z_]\w*)",
        parameter.strip(),
    )
    if match is None:
        return None
    return (
        match.group("annotations") or "",
        match.group("type"),
        match.group("variable"),
    )


def _has_validation_group(annotation_text: str) -> bool:
    if re.search(r"\bgroups\s*=", annotation_text):
        return True
    for match in re.finditer(
        r"@(?:org\.springframework\.validation\.annotation\.)?"
        r"Validated\s*\(([^)]*)\)",
        annotation_text,
    ):
        if match.group(1).strip():
            return True
    return False


def _class_has_valid_constraints(definition: dict) -> tuple[bool, bool]:
    field_pattern = re.compile(
        r"(?m)^(?P<annotations>(?:\s*@[\w.]+(?:\([^\n]*\))?\s*)+)"
        r"\s*(?:private|protected|public)\s+"
        r"(?:final\s+)?(?:static\s+)?[\w.<>, ?\[\]]+\s+"
        r"[A-Za-z_]\w*\s*(?:=[^;]*)?;"
    )
    has_constraint = False

    for field_match in field_pattern.finditer(definition["body"]):
        annotations = field_match.group("annotations") or ""
        for constraint in VALIDATION_CONSTRAINTS:
            if not _has_valid_imported_annotation(
                annotations,
                definition["block"],
                "jakarta.validation.constraints",
                constraint,
            ):
                continue
            has_constraint = True
            if _has_validation_group(annotations):
                return True, True

    return has_constraint, False


def _is_controller(definition: dict) -> bool:
    annotations = definition["annotations"]
    block = definition["block"]
    return (
        _has_valid_imported_annotation(
            annotations,
            block,
            "org.springframework.web.bind.annotation",
            "RestController",
        )
        or _has_valid_imported_annotation(
            annotations,
            block,
            "org.springframework.stereotype",
            "Controller",
        )
    )


def _missing_validation_trigger_issues(backend_result: str) -> list[dict]:
    java_blocks = JAVA_BLOCK_PATTERN.findall(backend_result)
    classes = _extract_classes(java_blocks)
    constrained_classes: dict[str, dict] = {}

    for class_name, definitions in classes.items():
        if len(definitions) != 1:
            continue
        definition = definitions[0]
        has_constraint, has_group = _class_has_valid_constraints(definition)
        if has_constraint and not has_group:
            constrained_classes[class_name] = definition

    missing_classes = set()
    for definitions in classes.values():
        if len(definitions) != 1:
            continue
        controller = definitions[0]
        if not _is_controller(controller):
            continue

        if _has_valid_imported_annotation(
            controller["annotations"],
            controller["block"],
            "org.springframework.validation.annotation",
            "Validated",
        ):
            continue

        for method in _controller_methods(controller["body"]):
            if _has_valid_imported_annotation(
                method["annotations"],
                controller["block"],
                "org.springframework.validation.annotation",
                "Validated",
            ):
                continue

            for parameter in _split_parameters(method["parameters"]):
                parts = _parameter_parts(parameter)
                if parts is None:
                    continue
                annotations, type_name, _ = parts
                if type_name not in constrained_classes:
                    continue
                if not _has_valid_imported_annotation(
                    annotations,
                    controller["block"],
                    "org.springframework.web.bind.annotation",
                    "RequestBody",
                ):
                    continue
                if _has_validation_group(annotations):
                    continue

                has_valid = _has_valid_imported_annotation(
                    annotations,
                    controller["block"],
                    "jakarta.validation",
                    "Valid",
                )
                has_validated = _has_valid_imported_annotation(
                    annotations,
                    controller["block"],
                    "org.springframework.validation.annotation",
                    "Validated",
                )
                if not has_valid and not has_validated:
                    missing_classes.add(type_name)

    return [
        {
            "severity": "Major",
            "rule": "MISSING_VALIDATION_TRIGGER",
            "message": (
                f"{class_name}에 Jakarta Validation constraint가 선언되어 있지만 "
                "@RequestBody parameter에서 이를 실행할 validation trigger가 없습니다."
            ),
            "required_fix": (
                "해당 요청 DTO의 Validation 정책을 유지하면서 "
                "@RequestBody parameter에서 Jakarta Validation constraint가 "
                "실행되도록 구성하세요."
            ),
        }
        for class_name in sorted(missing_classes)
    ]


def validate_backend_result(
    backend_result: str,
    project_context: dict | None = None,
) -> dict:
    issues = []

    # 1. Field Injection 검사
    field_injection_pattern = (
        r"@Autowired\s+"
        r"(?:private|protected|public)\s+"
        r"[\w<>?,. ]+\s+\w+\s*;"
    )

    if re.search(field_injection_pattern, backend_result):
        issues.append({
            "severity": "Major",
            "rule": "FIELD_INJECTION",
            "message": "@Autowired Field Injection이 사용되었습니다.",
            "required_fix": (
                "private final 필드와 생성자 주입 또는 "
                "@RequiredArgsConstructor를 사용하세요."
            ),
        })

    # 2. javax 사용 검사
    if "javax.persistence" in backend_result:
        issues.append({
            "severity": "Major",
            "rule": "JAVAX_PERSISTENCE",
            "message": "javax.persistence가 사용되었습니다.",
            "required_fix": "Spring Boot 3.x 기준 jakarta.persistence를 사용하세요.",
        })

    if "javax.validation" in backend_result:
        issues.append({
            "severity": "Major",
            "rule": "JAVAX_VALIDATION",
            "message": "javax.validation이 사용되었습니다.",
            "required_fix": "Spring Boot 3.x 기준 jakarta.validation을 사용하세요.",
        })

    # 3. RequiredArgsConstructor import 검사
    if (
        "@RequiredArgsConstructor" in backend_result
        and "import lombok.RequiredArgsConstructor;" not in backend_result
    ):
        issues.append({
            "severity": "Major",
            "rule": "MISSING_REQUIRED_ARGS_CONSTRUCTOR_IMPORT",
            "message": "@RequiredArgsConstructor를 사용하지만 import가 없습니다.",
            "required_fix": (
                "import lombok.RequiredArgsConstructor; 를 추가하세요."
            ),
        })

    # 4. Optional import 검사
    if (
        "Optional<" in backend_result
        and "import java.util.Optional;" not in backend_result
    ):
        issues.append({
            "severity": "Major",
            "rule": "MISSING_OPTIONAL_IMPORT",
            "message": "Optional을 사용하지만 java.util.Optional import가 없습니다.",
            "required_fix": "import java.util.Optional; 을 추가하세요.",
        })

    # 5. Timestamp import 검사
    if (
        re.search(r"\bTimestamp\b", backend_result)
        and "import java.sql.Timestamp;" not in backend_result
    ):
        issues.append({
            "severity": "Major",
            "rule": "MISSING_TIMESTAMP_IMPORT",
            "message": "Timestamp를 사용하지만 java.sql.Timestamp import가 없습니다.",
            "required_fix": "import java.sql.Timestamp; 를 추가하세요.",
        })

    # 6. 명시적으로 타입 연결 가능한 setter 호출의 제공 여부 검사
    issues.extend(_missing_setter_issues(backend_result))

    # 7. 메서드 parameter로 타입 연결 가능한 getter 호출의 제공 여부 검사
    issues.extend(_missing_getter_issues(backend_result))

    # 8. Request DTO Jakarta Validation constraint 실행 trigger 검사
    issues.extend(_missing_validation_trigger_issues(backend_result))

    # 9. 출력 안에서 package가 명확한 DTO의 누락 import 검사
    issues.extend(_missing_dto_import_issues(backend_result, project_context))

    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
    }
