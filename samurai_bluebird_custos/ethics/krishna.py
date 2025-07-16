# samurai_bluebird_custos/ethics/krishna.py

from typing import Dict, Any
from samurai_bluebird_custos.ethics.pillars import EI_DIMENSIONS
import os
import json

class KrishnaMetaObserver:
    """Krishna reflects on system emotional and ethical patterns, aligned with EthicalGatekeeper outputs."""

    def __init__(self):
        self.EI_DIMENSIONS = EI_DIMENSIONS
        self.logs_dir = "logs/"

    def process_logs(self) -> Dict[str, Any]:
        print("👁 Krishna: Observing output resonance and ethical patterns...")

        # Load the latest output_resonance_log.txt
        output_log_path = os.path.join(self.logs_dir, 'output_resonance_log.txt')
        with open(output_log_path, 'r') as f:
            output_analysis = f.read()

        # Map the EI dimensions from the output analysis
        socio_emotional_metrics = self._apply_emotional_filter_from_text(output_analysis)
        narrative = self._generate_narrative(socio_emotional_metrics, output_analysis)

        # Write to witness_log.txt
        witness_log_path = os.path.join(self.logs_dir, 'witness_log.txt')
        with open(witness_log_path, 'w') as f:
            f.write(narrative)
        print("📝 witness_log.txt updated.")

        # Trigger meta_alert.txt if negative trends detected
        if "Needs Attention" in socio_emotional_metrics.values():
            with open(os.path.join(self.logs_dir, 'meta_alert.txt'), 'w') as f:
                f.write("⚠️ Meta Alert: Emerging ethical or emotional misalignment detected.")
            print("⚠️ meta_alert.txt triggered.")

        return socio_emotional_metrics

    def _apply_emotional_filter_from_text(self, text: str) -> Dict[str, str]:
        ei_mapped = {}
        for dimension, metrics in self.EI_DIMENSIONS.items():
            if any(metric in text for metric in metrics):
                ei_mapped[dimension] = "Positive" if "Consistently High" in text else "Needs Attention"
        return ei_mapped

    def _generate_narrative(self, metrics: Dict[str, str], output_analysis: str) -> str:
        positive = [k for k, v in metrics.items() if v == "Positive"]
        attention = [k for k, v in metrics.items() if v == "Needs Attention"]

        return (
            f"Krishna Witness Log:\n"
            f"Review of Output Resonance:\n{output_analysis}\n\n"
            f"🌱 Positive EI Dimensions: {', '.join(positive)}\n"
            f"⚠️ Needs Attention: {', '.join(attention)}\n"
            f"Meta-Reflection: System shows growing self-awareness and ethical reasoning capacity.\n"
        )
