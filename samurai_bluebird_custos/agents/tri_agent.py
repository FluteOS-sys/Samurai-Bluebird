### tri_agent.py

from samurai_bluebird_custos.symbolic.recursive_memory_lattice import RecursiveSymbolicMemoryLattice
from samurai_bluebird_custos.agents.llm_bridge import LLMBridge

# Simulated Tri-Agent cognitive lenses
class TriAgent:
    def __init__(self, llm_bridge: LLMBridge | None = None):
        self.memory = RecursiveSymbolicMemoryLattice("memory/recursive_symbolic_memory.json")
        self.llm_bridge = llm_bridge or LLMBridge()

    def reason_over_batch(self, snapshot):
        """Use the LLM bridge to craft a narrative and suggested actions."""

        memory_state = self.memory.fetch_recent_symbols()
        narrative_hint = self._describe_symbolic_state(snapshot, memory_state)
        llm_payload = self.llm_bridge.generate_response(snapshot, memory_state, narrative_hint)

        enriched_output = {
            "narrative": llm_payload.get("narrative", ""),
            "follow_ups": llm_payload.get("follow_ups", []),
            "raw_enriched": {
                "symbolic_context": llm_payload.get("symbolic_context", {}),
                "narrative_hint": narrative_hint,
            },
        }
        return enriched_output

    def respond_to_user_chat(self, user_message: str, snapshot: dict | None = None) -> dict:
        """Route user chat through the adapter while preserving symbolic context."""

        snapshot = snapshot or {}
        memory_state = self.memory.fetch_recent_symbols()
        narrative_hint = self._describe_symbolic_state(snapshot, memory_state)
        return self.llm_bridge.chat_reply(
            user_message=user_message,
            snapshot=snapshot,
            memory_state=memory_state,
            narrative_hint=narrative_hint,
        )

    def _describe_symbolic_state(self, snapshot, memory_state) -> str:
        recent_keys = list(memory_state.keys()) if isinstance(memory_state, dict) else []
        snapshot_tags = []
        for key, value in snapshot.items():
            if isinstance(value, str) and value:
                snapshot_tags.append(f"{key}: {value[:40]}")
            elif value:
                snapshot_tags.append(f"{key}: {value}")
        tag_summary = ", ".join(snapshot_tags[:5]) if snapshot_tags else "No live sensory data"
        return (
            f"Symbolic threads referenced: {recent_keys[:5]}. "
            f"Snapshot cues: {tag_summary}."
        )
