"""Read-only, deterministic context extraction for target projects."""

from .loader import (
    ProjectContext,
    ProjectFileContext,
    format_project_context_for_agent,
    load_project_context,
)

__all__ = [
    "ProjectContext",
    "ProjectFileContext",
    "format_project_context_for_agent",
    "load_project_context",
]
