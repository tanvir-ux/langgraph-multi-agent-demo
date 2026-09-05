from __future__ import annotations

from typing import TypedDict


class AgentState(TypedDict, total=False):
    topic: str
    research_notes: str
    draft: str
    status: str
