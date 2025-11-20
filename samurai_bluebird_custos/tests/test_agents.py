# samurai_bluebird_custos/tests/test_agents.py

from samurai_bluebird_custos.agents.tri_agent import TriAgent

def test_tri_agent_reason_over_batch():
    tri_agent = TriAgent()
    dummy_input = {
        "tags": ["Innovation", "Trust", "Compassion"],
        "weights": {"Innovation": 1.1, "Trust": 1.0, "Compassion": 1.3}
    }
    result = tri_agent.reason_over_batch(dummy_input)
    assert "narrative" in result, "Narrative missing in Tri-Agent output"
    assert result.get("follow_ups"), "Tri-Agent did not propose follow-up ideas"
    assert "raw_enriched" in result, "Adapter context missing in Tri-Agent result"
    print("✅ Tri-Agent reasoning test passed.")


def test_tri_agent_user_chat_bridge():
    tri_agent = TriAgent()
    reply = tri_agent.respond_to_user_chat("How should I prioritize tasks?", {"active_window": "Terminal"})
    assert reply.get("user_reply"), "User reply not generated via adapter"
    assert "symbolic_context" in reply, "Symbolic context missing from chat reply"
    print("✅ Tri-Agent chat bridging test passed.")
