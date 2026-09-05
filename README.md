# langgraph-multi-agent-demo

Hi — I am Md Tanvir Alam ([tanvir-ux](https://github.com/tanvir-ux)). This is a **small LangGraph multi-agent skeleton**: an orchestrator plus two worker agents (research + writer). It runs offline with a stub LLM so you can see the graph topology without burning API keys.

## Architecture

```
topic → [orchestrator] → [research agent] → [writer agent] → END
```

| Node | Role |
|------|------|
| `orchestrator` | Accepts the topic, sets status, routes to research |
| `research` | Stub “findings” bullets for the topic |
| `writer` | Stub short draft from those notes |

Swap `src/agents/llm_stub.py` for a real model when `OPENAI_API_KEY` is set and `USE_STUB_LLM=false`.

## Quick start

```bash
cd langgraph-multi-agent-demo
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
python main.py "Compare RAG vs fine-tuning for a support bot"
```

You should see `status`, `research_notes`, and `draft` printed to the terminal.

## Layout

```
main.py                 CLI entry
src/
  agents/
    llm_stub.py         Offline stub (+ optional OpenAI path)
    research.py
    writer.py
  graph/
    state.py            TypedDict AgentState
    workflow.py         StateGraph wiring
requirements.txt
.env.example
```

## Env

| Variable | Default | Notes |
|----------|---------|-------|
| `USE_STUB_LLM` | `true` | Keep `true` for offline demos |
| `OPENAI_API_KEY` | empty | Needed only for the real path |
| `OPENAI_MODEL` | `gpt-4o-mini` | Used when stub is off |

Optional real LLM also needs `pip install langchain-openai` (not pinned here so the stub path stays light).

## Why this shape

Clients who ask for “multi-agent LangGraph” usually want clear ownership of nodes, shared state, and a place to plug tools/LLMs. This repo is that skeleton — tiny enough to read in one sitting, runnable without secrets.

## Author

Md Tanvir Alam — [github.com/tanvir-ux](https://github.com/tanvir-ux)

MIT License.
