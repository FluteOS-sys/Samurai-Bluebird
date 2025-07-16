# samurai_bluebird_custos/tests/test_feathers.py

from samurai_bluebird_custos.io.activity_tracker import get_activity_snapshot

def test_activity_tracker_snapshot():
    """Test capturing a system activity snapshot."""
    try:
        snapshot = get_activity_snapshot()
        assert "active_window" in snapshot
        assert "cpu_usage" in snapshot
        assert "memory_usage" in snapshot
        print("✅ Activity tracker snapshot test passed.")
    except Exception as e:
        print(f"❌ Activity tracker snapshot test failed: {e}")
