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
    assert "ams_output" in result, "AMS output missing in Tri-Agent result"
    print("✅ Tri-Agent reasoning test passed.")
