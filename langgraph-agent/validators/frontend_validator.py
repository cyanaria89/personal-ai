import posixpath
import re
from validators.artifacts import _fenced_code_blocks


IMPLEMENTATION_REQUEST_PATTERNS = [
    r"구현",
    r"작성",
    r"만들어\s*줘",
    r"만들어",
    r"개발",
    r"\bimplement\b",
    r"\bbuild\b",
    r"\bcreate\b",
]

GLOBAL_CSS_FILES = {
    "global.css",
    "index.css",
    "reset.css",
}


def _normalize_output_path(path: str) -> str:
    normalized = path.strip().strip("`").replace("\\", "/")
    return posixpath.normpath(normalized).lstrip("./")


def _extract_section(
    text: str,
    heading: str,
) -> str:
    pattern = re.compile(
        rf"^[ \t]*##\s+{re.escape(heading)}\s*$\n"
        rf"(.*?)(?=^[ \t]*##\s+|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


def _extract_output_files(frontend_result: str) -> dict[str, dict[str, str]]:
    files_section = _extract_section(frontend_result, "Files")
    file_pattern = re.compile(
        r"^[ \t]*###\s+([^\n]+?)\s*$\s*"
        r"[ \t]*```([\w+-]*)\s*\n"
        r"(.*?)^[ \t]*```\s*$",
        re.MULTILINE | re.DOTALL,
    )
    files: dict[str, dict[str, str]] = {}

    for match in file_pattern.finditer(files_section):
        path = _normalize_output_path(match.group(1))

        if not path:
            continue

        files[path] = {
            "language": {"typescript": "ts", "javascript": "js"}.get(match.group(2).strip().lower(), match.group(2).strip().lower()),
            "content": match.group(3).strip(),
        }

    return files


def _is_implementation_request(user_request: str) -> bool:
    return any(
        re.search(pattern, user_request, re.IGNORECASE)
        for pattern in IMPLEMENTATION_REQUEST_PATTERNS
    )


def _extract_css_imports(
    source_path: str,
    content: str,
) -> set[str]:
    import_pattern = re.compile(
        r"\bimport\s+(?:[^;\n]*?\s+from\s+)?"
        r"[\"'](\.[^\"']+\.css)[\"']\s*;?"
    )
    source_directory = posixpath.dirname(source_path)

    return {
        _normalize_output_path(
            posixpath.join(source_directory, match.group(1))
        )
        for match in import_pattern.finditer(content)
    }


def _self_import_issues(
    files: dict[str, dict[str, str]],
) -> list[dict]:
    supported_extensions = (".ts", ".tsx", ".js", ".jsx")
    issues = []

    for source_path, data in sorted(files.items()):
        if not source_path.lower().endswith(supported_extensions):
            continue
        source = re.sub(r"/\*.*?\*/", "", data["content"], flags=re.DOTALL)
        source = re.sub(r"(?m)^\s*//.*$", "", source)
        import_pattern = re.compile(
            r"(?m)^\s*import\s+(?:[^;\n]*?\s+from\s+)?"
            r"[\"'](\.[^\"']*)[\"']\s*;?"
        )
        source_directory = posixpath.dirname(source_path)

        for match in import_pattern.finditer(source):
            specifier = match.group(1)
            resolved = _normalize_output_path(
                posixpath.join(source_directory, specifier)
            )
            candidates = {resolved}
            if not resolved.lower().endswith(supported_extensions):
                candidates.update(resolved + extension for extension in supported_extensions)
                candidates.update(
                    posixpath.join(resolved, "index" + extension)
                    for extension in supported_extensions
                )
            if source_path not in candidates:
                continue
            issues.append({
                "severity": "Major",
                "rule": "SELF_IMPORT",
                "message": (
                    f"{source_path}이 relative import {specifier}로 자기 자신을 import합니다."
                ),
                "required_fix": (
                    "현재 파일에 선언된 타입/함수는 self-import 없이 직접 사용하고, "
                    "외부 타입이면 실제 선언 파일에서 import하세요."
                ),
            })
            break

    return issues


def _user_provided_endpoint(user_request: str) -> bool:
    endpoint_pattern = re.compile(
        r"https?://[^\s]+"
        r"|\b(?:GET|POST|PUT|PATCH|DELETE)\s+/[^\s]+"
        r"|/api/[A-Za-z0-9_./{}:-]+",
        re.IGNORECASE,
    )
    return bool(endpoint_pattern.search(user_request))


def _is_unknown_contract_value(value: str) -> bool:
    normalized = value.strip().strip("`*- ").lower()
    return (
        not normalized
        or "unknown" in normalized
        or "미확정" in normalized
        or normalized in {"없음", "none", "not provided"}
    )


def _has_unconfirmed_api_contract(frontend_result: str) -> bool:
    clarification = _extract_section(frontend_result, "API Clarification")

    endpoint_match = re.search(
        r"^\s*[-*]?\s*Endpoint\s*:\s*(.+)$",
        clarification,
        re.MULTILINE | re.IGNORECASE,
    )

    if (
        endpoint_match
        and not _is_unknown_contract_value(endpoint_match.group(1))
    ):
        return True

    dto_pattern = re.compile(
        r"^\s*[-*]?\s*(?:Request|Response)\s+DTO\s*:\s*(.*)$",
        re.MULTILINE | re.IGNORECASE,
    )
    dto_matches = list(dto_pattern.finditer(clarification))

    for index, match in enumerate(dto_matches):
        value = match.group(1)

        if value.strip():
            if not _is_unknown_contract_value(value):
                return True
            continue

        next_start = (
            dto_matches[index + 1].start()
            if index + 1 < len(dto_matches)
            else len(clarification)
        )
        following_content = clarification[match.end():next_start]

        if re.search(
            r"```(?:json)?\s*\n\s*\{|^\s*\{",
            following_content,
            re.MULTILINE | re.IGNORECASE,
        ):
            return True

    code_endpoint_pattern = re.compile(
        r"\b(?:fetch|axios\.(?:get|post|put|patch|delete))\s*\(\s*"
        r"[\"'](?:https?://[^\"']+|/api/[^\"']+)[\"']",
        re.IGNORECASE,
    )
    return bool(code_endpoint_pattern.search(frontend_result))


def _mask_non_code(source: str) -> str:
    """문자열과 주석을 공백으로 바꾸되 위치와 줄바꿈은 유지한다."""
    masked = list(source)
    index = 0
    state = "code"
    quote = ""

    while index < len(source):
        char = source[index]
        next_char = source[index + 1] if index + 1 < len(source) else ""

        if state == "code":
            if char == "/" and next_char == "/":
                masked[index] = masked[index + 1] = " "
                index += 2
                state = "line_comment"
                continue
            if char == "/" and next_char == "*":
                masked[index] = masked[index + 1] = " "
                index += 2
                state = "block_comment"
                continue
            if char in {"'", '"', "`"}:
                quote = char
                masked[index] = " "
                index += 1
                state = "string"
                continue
        elif state == "line_comment":
            if char == "\n":
                state = "code"
            else:
                masked[index] = " "
            index += 1
            continue
        elif state == "block_comment":
            if char == "*" and next_char == "/":
                masked[index] = masked[index + 1] = " "
                index += 2
                state = "code"
                continue
            if char != "\n":
                masked[index] = " "
            index += 1
            continue
        elif state == "string":
            if char == "\\":
                masked[index] = " "
                if index + 1 < len(source):
                    if source[index + 1] != "\n":
                        masked[index + 1] = " "
                    index += 2
                    continue
            if char == quote:
                masked[index] = " "
                index += 1
                state = "code"
                continue
            if char != "\n":
                masked[index] = " "
            index += 1
            continue

        index += 1

    return "".join(masked)


def _matching_brace(source: str, opening_index: int) -> int | None:
    depth = 0
    for index in range(opening_index, len(source)):
        if source[index] == "{":
            depth += 1
        elif source[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    return None


def _guard_ranges(
    masked_source: str,
    catch_start: int,
    catch_end: int,
    variable_name: str,
) -> list[tuple[int, int]] | None:
    variable = re.escape(variable_name)
    guard_pattern = re.compile(
        rf"\bif\s*\(\s*(?:"
        rf"{variable}\s+instanceof\s+Error"
        rf"|axios\.isAxiosError\s*\(\s*{variable}\s*\)"
        rf")\s*\)\s*\{{"
    )
    ranges = []

    for match in guard_pattern.finditer(masked_source, catch_start, catch_end):
        opening_index = match.end() - 1
        closing_index = _matching_brace(masked_source, opening_index)
        if closing_index is None or closing_index > catch_end:
            return None
        ranges.append((opening_index + 1, closing_index))

    return ranges


def _unsafe_catch_issues(source_path: str, content: str) -> list[dict]:
    masked = _mask_non_code(content)
    catch_pattern = re.compile(
        r"\bcatch\s*\(\s*([A-Za-z_$][\w$]*)\s*\)\s*\{"
    )
    issues = []

    for catch_match in catch_pattern.finditer(masked):
        variable_name = catch_match.group(1)
        opening_index = catch_match.end() - 1
        closing_index = _matching_brace(masked, opening_index)
        if closing_index is None:
            continue

        guards = _guard_ranges(
            masked,
            opening_index + 1,
            closing_index,
            variable_name,
        )
        if guards is None:
            continue

        access_pattern = re.compile(
            rf"\b{re.escape(variable_name)}\s*\.\s*([A-Za-z_$][\w$]*)"
        )
        unsafe_accesses = set()
        for access in access_pattern.finditer(
            masked,
            opening_index + 1,
            closing_index,
        ):
            if any(start <= access.start() < end for start, end in guards):
                continue
            unsafe_accesses.add(
                f"{variable_name}.{access.group(1)}"
            )

        if unsafe_accesses:
            accesses = ", ".join(sorted(unsafe_accesses))
            issues.append({
                "severity": "Major",
                "rule": "UNSAFE_CATCH_ERROR_ACCESS",
                "message": (
                    f"TypeScript catch 변수 {variable_name}에 타입 확인 없이 "
                    f"property를 접근했습니다: {accesses}"
                ),
                "required_fix": (
                    "catch 값을 instanceof Error 또는 라이브러리 타입 가드로 "
                    "확인한 뒤 접근하거나 안전하게 문자열로 변환하세요."
                ),
            })

    return issues


def validate_frontend_result(
    frontend_result: str,
    user_request: str = "",
    required_agents: list[str] | None = None,
    backend_result: str = "",
) -> dict:
    issues = []
    files = _extract_output_files(frontend_result)
    blocks = _fenced_code_blocks(frontend_result)
    if files and blocks is not None:
        for marker in re.finditer(
            r'(?m)^\[(?:현재 Backend 관련 API 계약|반드시 해결할 (?:Frontend|Integration) Validator Issues|Frontend (?:Validator|Integration) Fix Mode 수정 규칙)\]\s*$',
            frontend_result,
        ):
            if not any(b['start'] <= marker.start() < b['end'] for b in blocks):
                issues.append({
                    'severity': 'Major', 'rule': 'COPIED_REFERENCE_OUTPUT',
                    'message': 'Frontend 산출물에 입력 참고 계약/Issue/Fix 지침이 복사되었습니다.',
                    'required_fix': 'Files의 모든 실제 Frontend 코드와 필수 계약 설명은 보존하고 입력 참고 영역의 재출력만 제거하세요.',
                })
                break
    frontend_files = {
        path: data
        for path, data in files.items()
        if path.lower().endswith((".tsx", ".jsx"))
    }
    typescript_files = {
        path: data
        for path, data in files.items()
        if path.lower().endswith((".ts", ".tsx"))
        and data["language"] in {"ts", "tsx"}
    }

    issues.extend(_self_import_issues(files))

    if _is_implementation_request(user_request):
        has_implementation = any(
            data["content"]
            and data["language"] in {"tsx", "jsx"}
            for data in frontend_files.values()
        )

        if not has_implementation:
            issues.append({
                "severity": "Major",
                "rule": "MISSING_FRONTEND_IMPLEMENTATION",
                "message": "구현 요청이지만 TSX/JSX 구현 코드가 없습니다.",
                "required_fix": "실행 가능한 TSX 또는 JSX 파일 코드를 작성하세요.",
            })

    imported_css_files: set[str] = set()

    for source_path, data in frontend_files.items():
        css_imports = _extract_css_imports(
            source_path,
            data["content"],
        )
        imported_css_files.update(css_imports)

        for css_path in sorted(css_imports):
            if css_path not in files:
                issues.append({
                    "severity": "Major",
                    "rule": "MISSING_IMPORTED_CSS_FILE",
                    "message": (
                        f"{source_path}에서 import한 CSS 파일 "
                        f"{css_path}이 Files 출력에 없습니다."
                    ),
                    "required_fix": (
                        f"{css_path} 파일을 출력하거나 해당 import를 제거하세요."
                    ),
                })

    for css_path in sorted(
        path
        for path in files
        if path.lower().endswith(".css")
    ):
        if posixpath.basename(css_path).lower() in GLOBAL_CSS_FILES:
            continue

        if css_path not in imported_css_files:
            issues.append({
                "severity": "Major",
                "rule": "UNUSED_OUTPUT_CSS_FILE",
                "message": (
                    f"Files에 출력한 CSS 파일 {css_path}을 "
                    "어떤 TSX/JSX 파일에서도 import하지 않았습니다."
                ),
                "required_fix": (
                    f"{css_path}을 사용하는 TSX/JSX 파일에서 import하거나 "
                    "불필요한 CSS 출력을 제거하세요."
                ),
            })

    agents = set(required_agents or [])
    is_frontend_only = "frontend" in agents and "backend" not in agents

    if (
        is_frontend_only
        and not backend_result.strip()
        and not _user_provided_endpoint(user_request)
        and _has_unconfirmed_api_contract(frontend_result)
    ):
        issues.append({
            "severity": "Major",
            "rule": "UNCONFIRMED_API_CONTRACT",
            "message": (
                "근거가 없는 Frontend-only 요청에서 실제 API 계약을 "
                "임의로 확정했습니다."
            ),
            "required_fix": (
                "Endpoint와 DTO를 UNKNOWN(미확정)으로 표시하고 "
                "API 호출부를 callback/prop 또는 계약 비의존 방식으로 분리하세요."
            ),
        })

    for source_path, data in typescript_files.items():
        issues.extend(_unsafe_catch_issues(source_path, data["content"]))

    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
    }
