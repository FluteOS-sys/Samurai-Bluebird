# samurai_bluebird_custos/ethics/krishna.py

from datetime import datetime, timedelta
from samurai_bluebird_custos.symbolic.recursive_memory_lattice import ResonanceLattice
from samurai_bluebird_custos.core.resonance_logger import log_all

WITNESS_LOG = "witness_log.txt"
META_ALERT_LOG = "meta_alert.txt"

lattice = ResonanceLattice("memory/resonance_lattice.json")


def extract_dominant_themes(snapshot):
    themes = []
    for category, neurons in snapshot.items():
        for neuron_id, node in neurons.items():
            hooks = node.get("narrative_hooks", [])
            themes.extend(hooks)
    return list(set(themes))


def generate_witness_log():
    snapshot = lattice.get_snapshot_json()
    reflection = lattice.get_daily_reflection()
    dominant_themes = extract_dominant_themes(snapshot)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = (
        f"\n🧿 Krishna Meta-Reflection – {now}\n"
        f"Dominant Themes: {', '.join(dominant_themes) or 'N/A'}\n"
        f"Symbolic Reflection: {reflection}\n"
    )
    log_all(log_entry, WITNESS_LOG)
    print("👁️ Witness log updated.")


def observe_symbolic_drift():
    snapshot = lattice.get_snapshot_json()
    now = datetime.now()
    cutoff = (now - timedelta(hours=6)).strftime("%Y-%m-%d %H:%M")

    drift_score = 0
    theme_count = {}

    for category, neurons in snapshot.items():
        for neuron_id, node in neurons.items():
            updated = node.get("last_updated", "")
            if updated < cutoff:
                continue
            hooks = node.get("narrative_hooks", [])
            for h in hooks:
                theme_count[h] = theme_count.get(h, 0) + 1

    if not theme_count:
        return  # No significant drift

    max_theme = max(theme_count, key=theme_count.get)
    drift_score = sum(theme_count.values())

    if drift_score > 6:
        alert = (
            f"\n🚨 Meta Alert – {now.strftime('%Y-%m-%d %H:%M')}\n"
            f"High symbolic activity detected around: {max_theme}\n"
            f"Total resonance spike: {drift_score} recent narrative hooks.\n"
        )
        log_all(alert, META_ALERT_LOG)
        print("⚠️ Meta alert triggered.")


class KrishnaMetaObserver:
    """Summarize the resonance lattice for dashboards."""

    def __init__(self, lattice_instance: ResonanceLattice | None = None):
        self.lattice = lattice_instance or lattice

    def process_lattice_reflection(self):
        snapshot = self.lattice.get_snapshot_json()
        reflection = self.lattice.get_daily_reflection()
        dominant_themes = extract_dominant_themes(snapshot)

        total_nodes = sum(len(nodes) for nodes in snapshot.values()) or 1
        unknown_nodes = sum(
            1 for nodes in snapshot.values() for node in nodes.values() if node.get("familiarity", 0) < 0.7
        )
        unknown_ratio = round(unknown_nodes / total_nodes, 3)

        payload = {
            "daily_reflection": reflection,
            "dominant_themes": dominant_themes,
            "unknown_ratio": unknown_ratio,
            "timestamp": datetime.utcnow().isoformat(),
        }
        log_all(payload, WITNESS_LOG, meta_notes="Krishna reflection")
        return payload
