import re


JAVA_BLOCK_PATTERN = re.compile(
    r"```java\s*\n(.*?)```",
    re.DOTALL | re.IGNORECASE,
)
FRONTEND_BLOCK_PATTERN = re.compile(
    r"```(?:tsx|ts|jsx|js)\s*\n(.*?)```",
    re.DOTALL | re.IGNORECASE,
)

HTTP_STATUS_CODES = {
    "OK": 200,
    "CREATED": 201,
    "ACCEPTED": 202,
    "NO_CONTENT": 204,
}


def _matching_brace(source: str, opening_index: int) -> int | None:
    depth = 0
    index = opening_index
    state = "code"
    quote = ""

    while index < len(source):
        char = source[index]
        next_char = source[index + 1] if index + 1 < len(source) else ""

        if state == "code":
            if char == "/" and next_char == "/":
                state = "line_comment"
                index += 2
                continue
            if char == "/" and next_char == "*":
                state = "block_comment"
                index += 2
                continue
            if char in {"'", '"'}:
                state = "string"
                quote = char
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return index
        elif state == "line_comment":
            if char == "\n":
                state = "code"
        elif state == "block_comment":
            if char == "*" and next_char == "/":
                state = "code"
                index += 2
                continue
        elif state == "string":
            if char == "\\":
                index += 2
                continue
            if char == quote:
                state = "code"

        index += 1

    return None


def _normalize_path(path: str) -> str:
    parts = [part for part in path.strip().split("/") if part]
    return "/" + "/".join(parts) if parts else "/"


def _literal_mapping_path(annotation: str) -> str | None:
    arguments = re.search(r"\((.*?)\)", annotation, re.DOTALL)
    if arguments is None:
        return ""

    content = arguments.group(1).strip()
    literal = re.search(
        r"(?:^|\b(?:value|path)\s*=\s*)[\"']([^\"']*)[\"']",
        content,
    )
    return literal.group(1) if literal else None


def _mapping_from_annotations(annotations: str) -> tuple[str, str] | None:
    shortcut = re.findall(
        r"@(Get|Post|Put|Patch|Delete)Mapping\s*(\([^\n]*\))?",
        annotations,
        re.IGNORECASE,
    )
    request_mappings = re.findall(
        r"@RequestMapping\s*(\([^\n]*\))?",
        annotations,
        re.IGNORECASE,
    )

    if len(shortcut) + len(request_mappings) != 1:
        return None

    if shortcut:
        method_name, arguments = shortcut[0]
        path = _literal_mapping_path(f"Mapping{arguments}")
        if path is None:
            return None
        return method_name.upper(), path

    arguments = request_mappings[0]
    method_match = re.search(
        r"\bmethod\s*=\s*RequestMethod\.(GET|POST|PUT|PATCH|DELETE)\b",
        arguments,
        re.IGNORECASE,
    )
    path = _literal_mapping_path(f"RequestMapping{arguments}")
    if method_match is None or path is None:
        return None
    return method_match.group(1).upper(), path


def _class_base_path(annotations: str) -> str | None:
    mappings = re.findall(
        r"@RequestMapping\s*(\([^\n]*\))?",
        annotations,
        re.IGNORECASE,
    )
    if not mappings:
        return ""
    if len(mappings) != 1:
        return None
    return _literal_mapping_path(f"RequestMapping{mappings[0]}")


def _status_value(value: str) -> int | None:
    normalized = value.strip().upper()
    if normalized.isdigit():
        return int(normalized)
    normalized = normalized.removeprefix("HTTPSTATUS.")
    return HTTP_STATUS_CODES.get(normalized)


def _backend_success_status(
    class_annotations: str,
    method_annotations: str,
    return_type: str,
    method_body: str,
) -> int | None:
    response_statuses = re.findall(
        r"@ResponseStatus\s*\(\s*(?:(?:value|code)\s*=\s*)?"
        r"(?:HttpStatus\.)?([A-Z_]+)\s*\)",
        f"{class_annotations}\n{method_annotations}",
        re.IGNORECASE,
    )
    if len(response_statuses) == 1:
        return _status_value(response_statuses[0])
    if len(response_statuses) > 1:
        return None

    if re.search(r"\bResponseEntity\.created\s*\(", method_body):
        return 201

    explicit_statuses = re.findall(
        r"\bResponseEntity\.status\s*\(\s*"
        r"(?:HttpStatus\.)?([A-Z_]+|\d+)\s*\)",
        method_body,
        re.IGNORECASE,
    )
    if len(explicit_statuses) == 1:
        return _status_value(explicit_statuses[0])
    if len(explicit_statuses) > 1:
        return None

    if "ResponseEntity" not in return_type and re.search(r"\breturn\s+", method_body):
        return 200
    return None


def _extract_backend_routes(backend_result: str) -> list[dict]:
    routes = []
    class_pattern = re.compile(
        r"(?P<annotations>(?:\s*@[\w.]+(?:\([^\n]*\))?\s*)*)"
        r"(?:(?:public|protected|private|abstract|final|static)\s+)*"
        r"class\s+[A-Za-z_]\w*[^\{]*\{"
    )
    method_pattern = re.compile(
        r"(?P<annotations>(?:\s*@[\w.]+(?:\([^\n]*\))?\s*)+)"
        r"(?:(?:public|protected|private|static|final|synchronized)\s+)+"
        r"(?P<return_type>[\w.<>, ?\[\]]+)\s+"
        r"[A-Za-z_]\w*\s*\([^)]*\)\s*\{"
    )

    for block in JAVA_BLOCK_PATTERN.findall(backend_result):
        for class_match in class_pattern.finditer(block):
            class_open = class_match.end() - 1
            class_close = _matching_brace(block, class_open)
            if class_close is None:
                continue
            class_annotations = class_match.group("annotations") or ""
            base_path = _class_base_path(class_annotations)
            if base_path is None:
                continue
            class_body = block[class_open + 1:class_close]

            for method_match in method_pattern.finditer(class_body):
                method_annotations = method_match.group("annotations") or ""
                mapping = _mapping_from_annotations(method_annotations)
                if mapping is None:
                    continue
                method, method_path = mapping
                method_open = method_match.end() - 1
                method_close = _matching_brace(class_body, method_open)
                if method_close is None:
                    continue
                method_body = class_body[method_open + 1:method_close]
                routes.append({
                    "method": method,
                    "path": _normalize_path(f"{base_path}/{method_path}"),
                    "status": _backend_success_status(
                        class_annotations,
                        method_annotations,
                        method_match.group("return_type"),
                        method_body,
                    ),
                })
    return routes


def _assigned_response_variable(content: str, call_start: int) -> str | None:
    prefix = content[max(0, call_start - 120):call_start]
    match = re.search(
        r"(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*"
        r"(?:await\s*)?$",
        prefix,
    )
    return match.group(1) if match else None


def _forced_status(content: str, variable_name: str | None) -> int | None:
    if not variable_name:
        return None
    variable = re.escape(variable_name)
    statuses = {
        int(value)
        for value in re.findall(
            rf"(?:\b{variable}\.status\s*===\s*(\d{{3}})\b"
            rf"|\b(\d{{3}})\s*===\s*{variable}\.status\b)",
            content,
        )
        for value in value
        if value
    }
    return next(iter(statuses)) if len(statuses) == 1 else None


def _extract_frontend_requests(frontend_result: str) -> list[dict]:
    requests = []
    axios_pattern = re.compile(
        r"\baxios\.(get|post|put|patch|delete)\s*\(\s*"
        r"([\"'])(/[^\"']*)\2",
        re.IGNORECASE,
    )
    fetch_pattern = re.compile(
        r"\bfetch\s*\(\s*([\"'])(/[^\"']*)\1\s*,\s*\{",
        re.IGNORECASE,
    )

    for content in FRONTEND_BLOCK_PATTERN.findall(frontend_result):
        for match in axios_pattern.finditer(content):
            response_variable = _assigned_response_variable(content, match.start())
            requests.append({
                "method": match.group(1).upper(),
                "path": _normalize_path(match.group(3)),
                "status": _forced_status(content, response_variable),
            })

        for match in fetch_pattern.finditer(content):
            options_open = match.end() - 1
            options_close = _matching_brace(content, options_open)
            if options_close is None:
                continue
            options = content[options_open + 1:options_close]
            method_match = re.search(
                r"\bmethod\s*:\s*([\"'])(GET|POST|PUT|PATCH|DELETE)\1",
                options,
                re.IGNORECASE,
            )
            if method_match is None:
                continue
            response_variable = _assigned_response_variable(content, match.start())
            requests.append({
                "method": method_match.group(2).upper(),
                "path": _normalize_path(match.group(2)),
                "status": _forced_status(content, response_variable),
            })
    return requests


def _explicit_success_statuses(text: str) -> set[int]:
    return {
        int(value)
        for value in re.findall(r"(?<!\d)(2\d{2})(?!\d)", text)
    }


def _backend_handoff_success_statuses(backend_result: str) -> set[int]:
    without_java = JAVA_BLOCK_PATTERN.sub("", backend_result)
    section_pattern = re.compile(
        r"^#{1,4}\s+[^\n]*(?:handoff|api\s+contract)[^\n]*$\n"
        r"(.*?)(?=^#{1,4}\s+|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    statuses = set()

    for section in section_pattern.findall(without_java):
        for line in section.splitlines():
            if not re.search(r"\bsuccess\b|성공", line, re.IGNORECASE):
                continue
            statuses.update(
                int(value)
                for value in re.findall(r"(?<!\d)(2\d{2})(?!\d)", line)
            )

    return statuses


def _success_status_target(
    backend_status: int,
    frontend_status: int,
    user_request: str,
    backend_result: str,
) -> str:
    handoff_statuses = _backend_handoff_success_statuses(backend_result)
    if len(handoff_statuses) > 1:
        return "UNKNOWN"
    if handoff_statuses and next(iter(handoff_statuses)) != backend_status:
        return "UNKNOWN"

    user_statuses = _explicit_success_statuses(user_request)
    if len(user_statuses) > 1:
        return "UNKNOWN"
    if not user_statuses:
        return "frontend"
    user_status = next(iter(user_statuses))

    backend_matches = backend_status == user_status
    frontend_matches = frontend_status == user_status
    if frontend_matches and not backend_matches:
        return "backend"
    if backend_matches and not frontend_matches:
        return "frontend"
    return "UNKNOWN"


def validate_integration_result(
    backend_result: str,
    frontend_result: str,
    user_request: str = "",
    project_plan: str = "",
) -> dict:
    del project_plan
    issues = []
    backend_routes = _extract_backend_routes(backend_result)
    frontend_requests = _extract_frontend_requests(frontend_result)

    if len(backend_routes) != 1 or len(frontend_requests) != 1:
        return {"status": "PASS", "issues": []}

    backend = backend_routes[0]
    frontend = frontend_requests[0]

    if backend["method"] != frontend["method"]:
        issues.append({
            "severity": "Major",
            "rule": "HTTP_METHOD_MISMATCH",
            "target_agent": "UNKNOWN",
            "message": (
                f"Backend는 {backend['method']}이지만 Frontend는 "
                f"{frontend['method']}를 사용합니다."
            ),
            "required_fix": "Backend와 Frontend의 HTTP Method를 일치시키세요.",
        })

    if backend["path"] != frontend["path"]:
        issues.append({
            "severity": "Major",
            "rule": "ENDPOINT_PATH_MISMATCH",
            "target_agent": "UNKNOWN",
            "message": (
                f"Backend endpoint는 {backend['path']}이지만 Frontend는 "
                f"{frontend['path']}를 호출합니다."
            ),
            "required_fix": "Backend와 Frontend의 endpoint path를 일치시키세요.",
        })

    if (
        backend["status"] is not None
        and frontend["status"] is not None
        and backend["status"] != frontend["status"]
    ):
        issues.append({
            "severity": "Major",
            "rule": "SUCCESS_STATUS_MISMATCH",
            "target_agent": _success_status_target(
                backend["status"],
                frontend["status"],
                user_request,
                backend_result,
            ),
            "message": (
                f"Backend 성공 status는 {backend['status']}이지만 Frontend는 "
                f"{frontend['status']}을 성공 조건으로 사용합니다."
            ),
            "required_fix": "Backend 성공 status와 Frontend 성공 조건을 일치시키세요.",
        })

    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": issues,
    }
