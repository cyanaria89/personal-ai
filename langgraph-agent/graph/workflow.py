import os
from typing import Literal

from langgraph.graph import END, START, StateGraph

from agents.nodes import (
    project_context_node,
    pm_agent,
    db_agent,
    db_validator,
    backend_agent,
    backend_validator,
    frontend_agent,
    frontend_validator,
    integration_validator,
    review_agent,
    final_agent,
)
from state import AgentState


def get_max_agent_fix_count() -> int:
    return int(
        os.getenv("MAX_AGENT_FIX_COUNT", "2")
    )


def get_max_integration_fix_count() -> int:
    return int(
        os.getenv("MAX_INTEGRATION_FIX_COUNT", "2")
    )


def integration_targets(state: AgentState) -> set[str]:
    validation = state.get(
        "integration_validation",
        {"status": "NOT_RUN", "issues": []},
    )
    return {
        str(issue.get("target_agent", "UNKNOWN"))
        for issue in validation.get("issues", [])
        if isinstance(issue, dict)
    }


def route_after_pm(
    state: AgentState,
) -> Literal["db", "backend", "frontend", "review"]:
    """PM이 선택한 Agent 목록에 따라 첫 작업을 결정한다."""

    required_agents = state.get(
        "required_agents",
        [],
    )

    if "db" in required_agents:
        print("[Graph] DB Agent로 이동합니다.")
        return "db"

    if "backend" in required_agents:
        print("[Graph] Backend Agent로 이동합니다.")
        return "backend"

    if "frontend" in required_agents:
        print("[Graph] Frontend Agent로 이동합니다.")
        return "frontend"

    print("[Graph] 실행할 작업 Agent가 없어 Review로 이동합니다.")
    return "review"


def route_after_db(
    state: AgentState,
) -> Literal["db", "backend", "frontend", "review"]:
    """DB 작업 후 Backend가 필요한지 확인한다."""

    validation = state.get(
        "db_validation",
        {"status": "NOT_RUN", "issues": []},
    )

    if validation.get("status") == "FAIL":
        if validation.get("fix", {}).get("status") == "NO_PROGRESS":
            print("[Graph] DB Fix NO_PROGRESS: FAIL을 유지하고 Review로 이동합니다.")
            return "review"
        if state.get("db_fix_count", 0) < get_max_agent_fix_count():
            print("[Graph] DB Validator 실패: DB Agent를 재실행합니다.")
            return "db"

        print("[Graph] DB 최대 재작업 횟수 도달: Review로 이동합니다.")
        return "review"

    required_agents = state.get(
        "required_agents",
        [],
    )

    if "backend" in required_agents:
        print("[Graph] Backend Agent로 이동합니다.")
        return "backend"

    if "frontend" in required_agents:
        print("[Graph] Frontend Agent로 이동합니다.")
        return "frontend"

    print("[Graph] Backend가 필요하지 않아 Review로 이동합니다.")
    return "review"


def route_after_backend_validator(
    state: AgentState,
) -> Literal["backend", "frontend", "integration", "review"]:
    """Backend 검증 후 Frontend가 필요한지 확인한다."""

    validation = state.get(
        "backend_validation",
        {"status": "NOT_RUN", "issues": []},
    )

    if validation.get("status") == "FAIL":
        if validation.get('fix', {}).get('status') == 'BLOCKED':
            print('[Graph] Backend Fix BLOCKED: FAIL을 유지하고 Review로 이동합니다.')
            return 'review'
        if (
            state.get("backend_fix_count", 0)
            < get_max_agent_fix_count()
        ):
            print(
                "[Graph] Backend Validator 실패: "
                "Backend Agent를 재실행합니다."
            )
            return "backend"

        print(
            "[Graph] Backend 최대 재작업 횟수 도달: "
            "Review로 이동합니다."
        )
        return "review"

    integration_validation = state.get(
        "integration_validation",
        {"status": "NOT_RUN", "issues": []},
    )
    if (
        integration_validation.get("status") == "FAIL"
        and integration_targets(state) == {"backend"}
    ):
        print(
            "[Graph] Backend Integration Fix 검증 완료: "
            "Integration Validator로 이동합니다."
        )
        return "integration"

    required_agents = state.get(
        "required_agents",
        [],
    )

    if "frontend" in required_agents:
        print("[Graph] Frontend Agent로 이동합니다.")
        return "frontend"

    print("[Graph] Frontend가 필요하지 않아 Review로 이동합니다.")
    return "review"


def route_after_integration_validator(
    state: AgentState,
) -> Literal["backend", "frontend", "review"]:
    validation = state.get(
        "integration_validation",
        {"status": "NOT_RUN", "issues": []},
    )
    if validation.get("status") != "FAIL":
        print(f"[Graph] Integration Validator 판정={validation.get('status', 'NOT_RUN')}: Review로 이동합니다.")
        return "review"

    targets = integration_targets(state)
    if targets not in ({"backend"}, {"frontend"}):
        print(
            "[Graph] Integration 수정 대상이 불명확하거나 혼합됨: "
            "Review로 이동합니다."
        )
        return "review"

    if (
        state.get("integration_fix_count", 0)
        >= get_max_integration_fix_count()
    ):
        print(
            "[Graph] Integration 최대 재작업 횟수 도달: "
            "Review로 이동합니다."
        )
        return "review"

    target = next(iter(targets))
    print(
        f"[Graph] Integration Validator 실패: "
        f"{target.title()} Agent를 재실행합니다."
    )
    return target


def route_after_frontend_validator(
    state: AgentState,
) -> Literal["frontend", "integration", "review"]:
    """Frontend 검증 결과와 재작업 횟수에 따라 이동한다."""

    validation = state.get(
        "frontend_validation",
        {"status": "NOT_RUN", "issues": []},
    )

    if validation.get("status") == "FAIL":
        if (
            state.get("frontend_fix_count", 0)
            < get_max_agent_fix_count()
        ):
            print(
                "[Graph] Frontend Validator 실패: "
                "Frontend Agent를 재실행합니다."
            )
            return "frontend"

        print(
            "[Graph] Frontend 최대 재작업 횟수 도달: "
            "Review로 이동합니다."
        )
        return "review"

    required_agents = set(state.get("required_agents", []))
    if {"backend", "frontend"}.issubset(required_agents):
        print("[Graph] Integration Validator로 이동합니다.")
        return "integration"

    return "review"


def create_workflow():
    builder = StateGraph(AgentState)

    builder.add_node("project_context", project_context_node)
    builder.add_node("pm", pm_agent)
    builder.add_node("db", db_agent)
    builder.add_node("db_validator", db_validator)
    builder.add_node("backend", backend_agent)
    builder.add_node("backend_validator", backend_validator)
    builder.add_node("frontend", frontend_agent)
    builder.add_node("frontend_validator", frontend_validator)
    builder.add_node("integration_validator", integration_validator)
    builder.add_node("review", review_agent)
    builder.add_node("final", final_agent)

    builder.add_edge(START, "project_context")
    builder.add_edge("project_context", "pm")

    builder.add_conditional_edges(
        "pm",
        route_after_pm,
        {
            "db": "db",
            "backend": "backend",
            "frontend": "frontend",
            "review": "review",
        },
    )

    builder.add_edge("db", "db_validator")
    
    builder.add_conditional_edges(
        "db_validator",
        route_after_db,
        {
            "db": "db",
            "backend": "backend",
            "frontend": "frontend",
            "review": "review",
        },
    )

    builder.add_edge(
        "backend",
        "backend_validator",
    )
    
    builder.add_conditional_edges(
        "backend_validator",
        route_after_backend_validator,
        {
            "backend": "backend",
            "frontend": "frontend",
            "integration": "integration_validator",
            "review": "review",
        },
    )

    builder.add_edge("frontend", "frontend_validator")
    builder.add_conditional_edges(
        "frontend_validator",
        route_after_frontend_validator,
        {
            "frontend": "frontend",
            "integration": "integration_validator",
            "review": "review",
        },
    )

    builder.add_conditional_edges(
        "integration_validator",
        route_after_integration_validator,
        {
            "backend": "backend",
            "frontend": "frontend",
            "review": "review",
        },
    )

    # 이번 단계에서는 Review 재작업 루프를 사용하지 않음
    builder.add_edge(
        "review",
        "final",
    )

    builder.add_edge(
        "final",
        END,
    )

    return builder.compile()
