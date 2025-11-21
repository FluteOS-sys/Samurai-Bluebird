### blue_box.py

"""
BlueBox – Framework Integration Module
This module applies cognitive frameworks to a narrative interpretation to generate a structured symbolic map of meaning.
"""

from typing import Dict, Any
from samurai_bluebird_custos.frameworks.chakra_mapping import ChakraMap
from samurai_bluebird_custos.frameworks.context_domains import ContextDomains
from samurai_bluebird_custos.frameworks.sovereignties import Sovereignties

class BlueBox:
    def __init__(self):
        self.chakra = ChakraMap()
        self.context = ContextDomains()
        self.sovereignty = Sovereignties()

    def process(self, enriched_narrative: Dict[str, Any]) -> Dict[str, Any]:
        """
        Accepts enriched narrative output from Tri-Agent and applies symbolic frameworks
        Returns symbolic meaning_map for RSML.
        """
        narrative = enriched_narrative.get("narrative", "")
        meta = enriched_narrative.get("raw_enriched", {})

        # Framework-level tagging
        chakra_signals = self.chakra.map_input(meta)
        context_domains = self.context.map_input(meta)
        sovereign_keys = self.sovereignty.list_all()
        sovereignty_constellation = self.sovereignty.route_affect_to_constellation(
            meta.get("tags", []), meta.get("weights", {})
        )

        meaning_map = {
            "chakra_signals": chakra_signals,
            "context_domains": context_domains,
            "sovereignties": sovereign_keys,
            "sovereignty_constellation": sovereignty_constellation,
            "tags": meta.get("tags", []),
            "emotional_tone": meta.get("emotional_tone", "neutral"),
            "resonance_score": meta.get("resonance_score", 0.0),
            "narrative": narrative
        }

        return {"meaning_map": meaning_map}
