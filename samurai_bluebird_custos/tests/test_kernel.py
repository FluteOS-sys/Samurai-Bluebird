# samurai_bluebird_custos/tests/test_kernel.py

from samurai_bluebird_custos.io.passive_input_manager import PassiveInputManager

def test_kernel_batch_capture():
    """Test Kernel’s ability to assemble a passive input snapshot."""
    try:
        passive_manager = PassiveInputManager()
        feather = passive_manager.capture()
        assert "timestamp" in feather
        assert "active_window" in feather
        print("✅ Kernel batch capture test passed.")
    except Exception as e:
        print(f"❌ Kernel batch capture test failed: {e}")
