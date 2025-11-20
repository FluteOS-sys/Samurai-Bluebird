"""Utilities for running the cognitive pipeline on snapshots or user prompts."""

from datetime import datetime
from typing import Any, Dict

from samurai_bluebird_custos.agents.ams_core import AMSCore
from samurai_bluebird_custos.agents.tri_agent import TriAgent
from samurai_bluebird_custos.core.resonance_logger import log_all
from samurai_bluebird_custos.frameworks.blue_box import BlueBox


class CognitivePipeline:
    """Orchestrates TriAgent, BlueBox, and AMSCore."""

    def __init__(self):
        self.tri_agent = TriAgent()
        self.blue_box = BlueBox()
        self.ams_core = AMSCore()

    def process_snapshot(self, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        """Run a captured snapshot through the cognitive stack."""

        tri_output = self.tri_agent.reason_over_batch(snapshot)
        meaning_map_bundle = self.blue_box.process(tri_output)
        filtered_output = self.ams_core.process_batch(meaning_map_bundle)

        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "snapshot": snapshot,
            "tri_narrative": tri_output.get("narrative", ""),
            "meaning_map": meaning_map_bundle.get("meaning_map", {}),
            "filtered_output": filtered_output,
        }
        log_all(payload, "output_resonance_log.txt", meta_notes="Snapshot pipeline")
        return payload

    def process_prompt(self, prompt: str) -> Dict[str, Any]:
        """Process a user prompt as a synthetic snapshot."""

        snapshot = {"user_prompt": prompt}
        tri_output = self.tri_agent.reason_over_batch(snapshot)
        meaning_map_bundle = self.blue_box.process(tri_output)
        filtered_output = self.ams_core.process_batch(meaning_map_bundle)

        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "tri_narrative": tri_output.get("narrative", ""),
            "meaning_map": meaning_map_bundle.get("meaning_map", {}),
            "filtered_output": filtered_output,
        }
        log_all(payload, "input_resonance_log.txt", meta_notes="Prompt pipeline")
        return payload
