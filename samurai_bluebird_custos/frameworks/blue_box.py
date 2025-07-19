# samurai_bluebird_custos/frameworks/blue_box.py

from typing import Dict, Any
from samurai_bluebird_custos.frameworks.sovereignties import Sovereignties
from samurai_bluebird_custos.frameworks.context_domains import ContextDomains
from samurai_bluebird_custos.frameworks.chakra_mapping import ChakraMap
from samurai_bluebird_custos.utils.planetary_metadata import get_planetary_positions
from datetime import datetime
import pytz

class BlueBox:
    """
    Blue Box – Resonance Genesis v0.2.1
    Central lattice for symbolic framework integration (Sovereignties, Chakras, Context Domains).
    """

    def __init__(self, timezone: str = "America/Detroit"):
        self.sovereignties = Sovereignties()
        self.context_domains = ContextDomains()
        self.chakras = ChakraMap()
        self.timezone = pytz.timezone(timezone)

    def process_input(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process input data through symbolic frameworks and tag accordingly.
        """
        print("📦 BlueBox: Processing input through frameworks...")

        processed = {}
        planetary_signature = get_planetary_positions(self._current_time())

        for tag, weight in zip(input_data.get("tags", []), input_data.get("weights", {}).values()):
            sovereignty = self.sovereignties.get_archetype(tag) or "Unknown"
            context_domain = self.context_domains.get_domain(tag) or "General"
            chakra = self.chakras.get_chakra(tag) or "Neutral"

            processed[tag] = {
                "sovereignty": sovereignty,
                "context_domain": context_domain,
                "chakra": chakra,
                "weight": round(weight, 2),
                "planetary_metadata": planetary_signature
            }
            print(f"🔖 Processed tag: {tag} -> {processed[tag]}")

        return {"BlueBoxProcessed": processed}

    def _current_time(self) -> str:
        return datetime.now(self.timezone).strftime('%Y-%m-%d %H:%M:%S %Z')

if __name__ == "__main__":
    blue_box = BlueBox()
    dummy_input = {
        "tags": ["Compassion", "Trust", "Innovation"],
        "weights": {"Compassion": 1.2, "Trust": 1.0, "Innovation": 1.1}
    }
    result = blue_box.process_input(dummy_input)
    print("BlueBox Result:", result)
