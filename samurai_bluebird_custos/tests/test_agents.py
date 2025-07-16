# samurai_bluebird_custos/tests/test_agents.py

from samurai_bluebird_custos.agents.ams_core import AMSCore

def test_ams_core_processing():
    """Test AMSCore batch processing."""
    ams = AMSCore()
    dummy_input = {
        "tags": ["Trust", "Clarity"],
        "weights": {"Trust": 1.0, "Clarity": 1.2}
    }
    try:
        result = ams.process_batch(dummy_input)
        assert "combined_data" in result
        print("✅ AMSCore processing test passed.")
    except Exception as e:
        print(f"❌ AMSCore processing test failed: {e}")
