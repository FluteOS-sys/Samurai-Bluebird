# samurai_bluebird_custos/ethics/ethical_gatekeeper.py

import json
import glob
import os
from typing import Dict, Any
from samurai_bluebird_custos.ethics.pillars import SocioEmotionalFilter

class EthicalGatekeeper:
    """Measures reasoning over time using the 12 Pillars filter for self-reflection."""

    def __init__(self):
        self.se_filter = SocioEmotionalFilter()
        self.logs_dir = "logs/"

    def evaluate_recent_reasoning(self) -> Dict[str, Any]:
        print("🛡 EthicalGatekeeper: Evaluating past reasoning...")

        # Get paths to last 7 input_resonance_log.txt files
        recent_logs = sorted(
            glob.glob(os.path.join(self.logs_dir, "input_resonance_log.txt")),
            key=os.path.getmtime, reverse=True
        )[:7]

        past_reasonings = []
        for log_file in recent_logs:
            with open(log_file, "r") as f:
                past_reasonings.append(json.load(f))

        # Aggregate socio-emotional and ethical patterns
        aggregated_results = {}
        for reasoning in past_reasonings:
            result = self.se_filter.run_all(reasoning["combined_data"]["resonance_lattice"])
            for k, v in result.items():
                aggregated_results.setdefault(k, []).append(v)

        # Summarize trends
        trends = {k: self._summarize_trend(v) for k, v in aggregated_results.items()}

        # Evaluate current dashboard log
        with open(os.path.join(self.logs_dir, "dashboard_log.txt"), "r") as f:
            current_narrative = f.read()

        meta_analysis = self._generate_meta_analysis(trends, current_narrative)

        # Write to output_resonance_log.txt
        with open(os.path.join(self.logs_dir, "output_resonance_log.txt"), "w") as f:
            f.write(meta_analysis)
        print("📝 output_resonance_log.txt updated.")

        return {"trends": trends, "meta_analysis": meta_analysis}

    def _summarize_trend(self, values):
        if values.count("High") > len(values) / 2:
            return "Consistently High"
        elif values.count("Neutral") > len(values) / 2:
            return "Stable"
        else:
            return "Needs Attention"

    def _generate_meta_analysis(self, trends, current_narrative):
        return (
            "Output Resonance Meta-Analysis:\n"
            "Past Reasoning Trends:\n"
            + "\n".join([f"  - {k}: {v}" for k, v in trends.items()]) + "\n\n"
            "Current Narrative:\n"
            f"{current_narrative}\n"
        )

