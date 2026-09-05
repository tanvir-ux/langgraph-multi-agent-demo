"""Research worker agent — gathers stub findings for a topic."""

from __future__ import annotations

from src.agents.llm_stub import complete


def run_research(topic: str) -> str:
    return complete("research", f"Research the following topic and list key findings:\n{topic}")
