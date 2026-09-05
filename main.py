#!/usr/bin/env python3
"""Run the multi-agent LangGraph stub from the CLI."""

from __future__ import annotations

import argparse
import json
import sys

from dotenv import load_dotenv

load_dotenv()

from src.graph.workflow import build_graph  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="LangGraph multi-agent demo (orchestrator + research + writer)")
    parser.add_argument(
        "topic",
        nargs="?",
        default="How to structure a small LangGraph multi-agent pipeline for Upwork demos",
        help="Topic for the research → writer pipeline",
    )
    args = parser.parse_args()

    app = build_graph()
    result = app.invoke({"topic": args.topic})

    print("=== status ===")
    print(result.get("status"))
    print("\n=== research_notes ===")
    print(result.get("research_notes"))
    print("\n=== draft ===")
    print(result.get("draft"))
    print("\n=== json ===")
    print(json.dumps({k: result.get(k) for k in ("topic", "status")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
