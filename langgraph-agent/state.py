from typing import TypedDict

from project_context.loader import ProjectContext


class AgentState(TypedDict):
    user_request: str
    project_root: str
    project_context: ProjectContext
    llm_metrics: list[dict]

    # PM이 선택한 실행 Agent 목록
    required_agents: list[str]

    project_plan: str
    pm_validation: dict
    
    db_result: str
    db_validation: dict
    db_fix_count: int
    
    backend_result: str
    backend_validation: dict
    backend_fix_count: int

    frontend_result: str
    frontend_validation: dict
    frontend_fix_count: int

    integration_validation: dict
    integration_fix_count: int

    review_result: str
    review_status: str
    review_count: int

    final_result: str
