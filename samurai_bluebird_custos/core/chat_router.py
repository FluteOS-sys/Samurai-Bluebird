"""Entry point for user chat routed through TriAgent + LLM bridge."""

from typing import Any, Dict

from samurai_bluebird_custos.agents.tri_agent import TriAgent


def route_user_chat(user_message: str, snapshot: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Return an LLM-informed reply grounded in the latest symbolic context."""

    tri_agent = TriAgent()
    return tri_agent.respond_to_user_chat(user_message, snapshot)
