"""Writer worker agent — turns research notes into a short draft."""

from __future__ import annotations

from src.agents.llm_stub import complete


def run_writer(research_notes: str) -> str:
    return complete(
        "writer",
        f"Write a short, client-ready draft from these research notes:\n{research_notes}",
    )
