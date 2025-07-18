# samurai_bluebird_custos/tests/test_krishna.py

from samurai_bluebird_custos.ethics.krishna import KrishnaMetaObserver

def test_krishna_process_lattice_reflection():
    krishna = KrishnaMetaObserver()
    result = krishna.process_lattice_reflection()
    assert "daily_reflection" in result, "Daily reflection missing in Krishna output"
    assert isinstance(result["unknown_ratio"], float), "Unknown ratio not a float"
    print("✅ Krishna lattice reflection test passed.")
