"""기존 Graph 회귀의 정상 PM 대역. 검증 생략 없이 완전한 계약을 제공한다."""


def valid_pm_plan(*agents):
    selected = ", ".join(agents) if agents else "none"
    order = " -> ".join([a for a in ("db", "backend", "frontend") if a in agents] + ["review"])
    return (
        f"REQUIRED_AGENTS: {selected}\nREQUEST_SUMMARY:\n사용자 요청 범위의 작업을 수행한다.\n"
        f"EXECUTION_ORDER:\n{order}\n"
        + "".join(f"{a.upper()}_HANDOFF:\n- 사용자 요청의 {a} 작업과 제외 조건을 보존한다.\n" for a in agents)
    ).strip()
