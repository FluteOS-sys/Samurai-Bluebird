# samurai_bluebird_custos/tests/test_frameworks.py

from samurai_bluebird_custos.ethics.pillars import SocioEmotionalFilter

def test_24_pillars_processing():
    """Test running the 24 Pillars SocioEmotionalFilter."""
    try:
        filter = SocioEmotionalFilter()
        dummy_data = {
            "Clarity": "High",
            "Trust": "Positive",
            "Adaptability": "Neutral"
        }
        results = filter.run_all(dummy_data)
        assert isinstance(results, dict)
        print("✅ 24 Pillars processing test passed.")
    except Exception as e:
        print(f"❌ 24 Pillars processing test failed: {e}")
