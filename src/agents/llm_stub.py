"""Tiny LLM stub so the graph runs without API keys.

Swap `stub_complete` for a real chat model when OPENAI_API_KEY is set
and USE_STUB_LLM=false.
"""

from __future__ import annotations

import os


def stub_complete(role: str, prompt: str) -> str:
    """Deterministic placeholder response per agent role."""
    prompt = (prompt or "").strip()
    snippet = prompt[:180] + ("…" if len(prompt) > 180 else "")
    if role == "research":
        return (
            f"[research-agent stub] Findings for: {snippet}\n"
            "- Point A: relevant background (stub)\n"
            "- Point B: constraint / trade-off (stub)\n"
            "- Point C: suggested next dig (stub)"
        )
    if role == "writer":
        return (
            f"[writer-agent stub] Draft based on research notes:\n\n"
            f"{snippet}\n\n"
            "Intro → 2 body bullets → short closing CTA. "
            "(Replace this stub with a real LLM call.)"
        )
    return f"[orchestrator stub] Routed task: {snippet}"


def complete(role: str, prompt: str) -> str:
    use_stub = os.getenv("USE_STUB_LLM", "true").lower() in {"1", "true", "yes"}
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if use_stub or not api_key:
        return stub_complete(role, prompt)

    # Optional real path — kept minimal so the skeleton stays small.
    try:
        from langchain_core.messages import HumanMessage, SystemMessage
        from langchain_openai import ChatOpenAI  # type: ignore

        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        llm = ChatOpenAI(model=model, temperature=0.2)
        system = {
            "research": "You are a concise research agent. Return bullet findings only.",
            "writer": "You are a concise writer agent. Turn research notes into a short draft.",
            "orchestrator": "You are an orchestrator. Summarize routing decisions briefly.",
        }.get(role, "You are a helpful assistant.")
        msg = llm.invoke([SystemMessage(content=system), HumanMessage(content=prompt)])
        return str(msg.content)
    except Exception as exc:  # pragma: no cover - fallback for missing optional dep
        return stub_complete(role, prompt) + f"\n\n(real LLM unavailable: {exc})"
