"""LangGraph workflow: orchestrator → research → writer → END."""

from __future__ import annotations

from langgraph.graph import END, StateGraph

from src.agents.research import run_research
from src.agents.writer import run_writer
from src.graph.state import AgentState


def orchestrator_node(state: AgentState) -> AgentState:
    topic = state.get("topic") or "untitled topic"
    return {
        "topic": topic,
        "status": f"orchestrator accepted topic ({len(topic)} chars) → research",
    }


def research_node(state: AgentState) -> AgentState:
    notes = run_research(state.get("topic", ""))
    return {"research_notes": notes, "status": "research done → writer"}


def writer_node(state: AgentState) -> AgentState:
    draft = run_writer(state.get("research_notes", ""))
    return {"draft": draft, "status": "writer done → END"}


def build_graph():
    g = StateGraph(AgentState)
    g.add_node("orchestrator", orchestrator_node)
    g.add_node("research", research_node)
    g.add_node("writer", writer_node)
    g.set_entry_point("orchestrator")
    g.add_edge("orchestrator", "research")
    g.add_edge("research", "writer")
    g.add_edge("writer", END)
    return g.compile()
