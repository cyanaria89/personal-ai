import re


JAVA_BLOCK_PATTERN = re.compile(
    r"```java\s*\n(.*?)```",
    re.DOTALL | re.IGNORECASE,
)
FRONTEND_BLOCK_PATTERN = re.compile(
    r"```(?:typescript|javascript|tsx|ts|jsx|js)[ \t]*\r?\n(.*?)```",
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
    opening = source[opening_index]
    closing = {"{": "}", "(": ")"}[opening]

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
            if char in {"'", '"', "`"}:
                state = "string"
                quote = char
            elif char == opening:
                depth += 1
            elif char == closing:
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
        r"(?:^|\b(?:value|path)\s*=\s*)[\"']([^\"']*)[\"']\s*(?=,|$)",
        content,
    )
    return literal.group(1) if literal else None


def _mapping_from_annotations(annotations: str) -> tuple[str, str] | None:
    shortcut = re.findall(
        r"@(Get|Post|Put|Patch|Delete|Head|Options)Mapping\s*(\([^\n]*\))?",
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
        r"\bmethod\s*=\s*RequestMethod\.(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\b",
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


def _extract_backend_routes(backend_result: str, unverified=None) -> list[dict]:
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
        r"[A-Za-z_]\w*\s*\("
    )

    for block in JAVA_BLOCK_PATTERN.findall(backend_result):
        block = _mask_non_code(block, strings=False)
        route_start = len(routes)
        mapping_count = len(re.findall(
            r"@(?:Get|Post|Put|Patch|Delete|Head|Options)Mapping\b|"
            r"@RequestMapping\b", block, re.IGNORECASE,
        ))
        for class_match in class_pattern.finditer(block):
            class_open = class_match.end() - 1
            class_close = _matching_brace(block, class_open)
            if class_close is None:
                continue
            class_annotations = class_match.group("annotations") or ""
            mapping_count -= len(re.findall(r"@RequestMapping\b", class_annotations))
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
                parameters_close = _matching_brace(class_body, method_match.end() - 1)
                if parameters_close is None:
                    continue
                body_start = re.match(r"\s*\{", class_body[parameters_close + 1:])
                if body_start is None:
                    continue
                method_open = parameters_close + 1 + body_start.end() - 1
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
        if unverified is not None and len(routes) - route_start != mapping_count:
            unverified.append("일부 Backend mapping을 추출하지 못했습니다.")
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


def _mask_non_code(source: str, *, strings: bool = True) -> str:
    """Preserve offsets while ignoring comments and quoted examples."""
    result = list(source)
    index = 0
    while index < len(source):
        if source.startswith("//", index):
            end = source.find("\n", index)
            end = len(source) if end < 0 else end
        elif source.startswith("/*", index):
            closing = source.find("*/", index + 2)
            end = len(source) if closing < 0 else closing + 2
        elif source[index] in "\"'`":
            quote = source[index]
            end = index + 1
            while end < len(source):
                if source[end] == "\\":
                    end += 2
                elif source[end] == quote:
                    end += 1
                    break
                else:
                    end += 1
            if not strings:
                index = end
                continue
        else:
            index += 1
            continue
        result[index:end] = ["\n" if c == "\n" else " " for c in source[index:end]]
        index = end
    return "".join(result)


def _request_path(value: str) -> str | None:
    # Support root-relative literals and whole-segment template parameters only.
    if not value.startswith("/"):
        return None
    value = re.sub(r"\$\{[^{}]+\}", "{param}", value)
    if "$" in value or re.search(r"[^/]\{param\}|\{param\}[^/?#]", value):
        return None
    return _normalize_path(re.split(r"[?#]", value, maxsplit=1)[0])


def _extract_frontend_requests(frontend_result: str, unverified=None) -> list[dict]:
    requests = []
    call_pattern = re.compile(r"\b(fetch|axios(?:\.[A-Za-z_]\w*)?)\s*\(")
    for content in FRONTEND_BLOCK_PATTERN.findall(frontend_result):
        code = _mask_non_code(content)
        for match in call_pattern.finditer(code):
            args = content[match.end():]
            literal = re.match(r"\s*([\"'`])([^\"'`\r\n]*)\1\s*(?=[,)])", args)
            path = _request_path(literal.group(2)) if literal else None
            if literal and literal.group(1) != "`" and "${" in literal.group(2):
                path = None
            method = None
            if match.group(1).startswith("axios"):
                candidate = match.group(1).partition(".")[2].upper()
                if candidate in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}:
                    method = candidate
            elif literal:
                after_url = args[literal.end():]
                if after_url.startswith(")"):
                    method = "GET"
                else:
                    options = re.match(r",\s*\{", after_url)
                    if options:
                        opening = match.end() + literal.end() + options.end() - 1
                        closing = _matching_brace(content, opening)
                        if closing is not None:
                            options_text = _mask_non_code(content[opening + 1:closing], strings=False)
                            method_matches = list(re.finditer(
                                r"\bmethod\s*:\s*([\"'])(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\1\s*(?=,|$)",
                                options_text, re.IGNORECASE,
                            ))
                            if len(method_matches) == 1 and not re.search(r"\.\.\.", options_text):
                                method = method_matches[0].group(2).upper()
                            elif not re.search(r"\bmethod\b|\.\.\.", options_text):
                                method = "GET"
            if path is None or method is None:
                if unverified is not None:
                    unverified.append("Frontend HTTP 요청의 URL 또는 Method를 추출하지 못했습니다.")
                continue
            response_variable = _assigned_response_variable(content, match.start())
            # A common variable name in another request/function is a different
            # response. Do not mix its success condition into this request.
            end = len(code)
            if response_variable:
                next_assignment = re.search(
                    rf"\b(?:const|let|var)\s+{re.escape(response_variable)}\s*=",
                    code[match.end():],
                )
                if next_assignment:
                    end = match.end() + next_assignment.start()
            status_code = code[match.start():end]
            status = _forced_status(status_code, response_variable)
            if (response_variable and status is None and unverified is not None
                and re.search(rf"\b{re.escape(response_variable)}\.status\s*===|===\s*{re.escape(response_variable)}\.status", status_code)):
                unverified.append("Frontend 성공 status 조건을 확정하지 못했습니다.")
            requests.append({"method": method, "path": path,
                             "status": status})
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


def _path_matches(backend_path: str, request_path: str) -> bool:
    backend_parts = backend_path.strip("/").split("/")
    request_parts = request_path.strip("/").split("/")
    return len(backend_parts) == len(request_parts) and all(
        re.fullmatch(r"\{[A-Za-z_]\w*\}", backend) is not None or backend == request
        for backend, request in zip(backend_parts, request_parts)
    )


def _issue(rule, message, required_fix, target="UNKNOWN"):
    return {"severity": "Major", "rule": rule, "target_agent": target,
            "message": message, "required_fix": required_fix}


def validate_integration_result(
    backend_result: str,
    frontend_result: str,
    user_request: str = "",
    project_plan: str = "",
) -> dict:
    """Verify every extracted request against the supported Backend contracts.

    PASS covers method/path/segment parameters and explicit success conditions,
    not DTO schemas, authentication behavior, or application runtime. Unsupported
    or incomplete extraction remains NOT_VERIFIED even if other pairs match.
    """
    del project_plan
    issues, unverified = [], []
    backend_routes = _extract_backend_routes(backend_result, unverified)
    backend_incomplete = bool(unverified)
    frontend_requests = _extract_frontend_requests(frontend_result, unverified)
    if not backend_routes:
        unverified.append("비교할 Backend endpoint를 추출하지 못했습니다.")
    if not frontend_requests:
        unverified.append("비교할 Frontend HTTP 요청을 추출하지 못했습니다.")
    usable_routes = []
    for route in backend_routes:
        # Regex/ant mappings require a richer Spring matcher; do not guess.
        without_parameters = re.sub(r"\{[A-Za-z_]\w*\}", "", route["path"])
        if any(c in without_parameters for c in "{}*?"):
            backend_incomplete = True
            unverified.append(f"지원하지 않는 Backend path 패턴: {route['path']}")
        else:
            usable_routes.append(route)

    checked = 0
    status_checked = 0
    for request in frontend_requests:
        label = f"{request['method']} {request['path']}"
        same_path = [r for r in usable_routes if _path_matches(r["path"], request["path"])]
        exact = [r for r in same_path if r["path"] == request["path"]]
        if exact:
            same_path = exact  # Spring literal paths take precedence over parameters.
        if not same_path:
            dynamic_literal = "{param}" in request["path"] and any(
                _path_matches(request["path"], r["path"]) for r in usable_routes
            )
            if not backend_routes or backend_incomplete or dynamic_literal:
                unverified.append(f"Backend 추출이 불완전하여 대응 여부를 확인할 수 없습니다: {label}")
            else:
                issues.append(_issue("ENDPOINT_PATH_MISMATCH",
                    f"Frontend 요청 {label}에 대응하는 Backend endpoint가 없습니다.",
                    "Frontend URL과 Backend endpoint path를 일치시키세요."))
            continue
        matches = [r for r in same_path if r["method"] == request["method"]]
        if not matches:
            if backend_incomplete:
                unverified.append(f"지원하는 Backend Method를 확정할 수 없습니다: {label}")
            else:
                issues.append(_issue("HTTP_METHOD_MISMATCH",
                    f"Frontend 요청 {label}의 Method가 Backend와 일치하지 않습니다.",
                    "Backend와 Frontend의 HTTP Method를 일치시키세요."))
            continue
        # Repeated identical code is harmless, conflicting contracts are not.
        signatures = {(r["path"], r["status"]) for r in matches}
        if len(signatures) != 1:
            unverified.append(f"대응 Backend 계약이 여러 개여서 확정할 수 없습니다: {label}")
            continue
        backend = matches[0]
        checked += 1
        if request["status"] is not None:
            if backend["status"] is None:
                unverified.append(f"Backend 성공 status를 확정할 수 없습니다: {label}")
            else:
                status_checked += 1
                if backend["status"] != request["status"]:
                    issues.append(_issue("SUCCESS_STATUS_MISMATCH",
                        f"{label}: Backend 성공 status는 {backend['status']}이지만 Frontend는 {request['status']}을 성공 조건으로 사용합니다.",
                        "Backend 성공 status와 Frontend 성공 조건을 일치시키세요.",
                        _success_status_target(backend["status"], request["status"], user_request, backend_result)))
    unverified = list(dict.fromkeys(unverified))
    failed = bool(issues)
    if unverified:
        issues.append(_issue("INTEGRATION_NOT_VERIFIED", " ".join(unverified),
            "비교 가능한 Backend endpoint와 Frontend HTTP 호출을 제공하고 미확인 계약을 검증하세요."))
    return {
        "status": "FAIL" if failed else "NOT_VERIFIED" if unverified else "PASS",
        "issues": issues,
        "coverage": {"backend_routes": len(backend_routes), "frontend_requests": len(frontend_requests),
                     "matched_requests": checked, "explicit_status_checks": status_checked,
                     "unverified": unverified},
    }
