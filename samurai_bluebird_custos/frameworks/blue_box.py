'''blue_box.py - The Sacred Lattice of Samurai Bluebird Custos

This module represents the Blue Box, where symbolic systems converge: 72 Sovereignties, 7 Chakras, 12 Context Domains. It synthesizes these multi-layered inputs into a unified resonance lattice, preparing data for AMS Core reasoning and the 12 Pillars Ethical Filter.
'''

from typing import Dict, Any
from samurai_bluebird_custos.frameworks.sovereignties import Sovereignties
from samurai_bluebird_custos.frameworks.chakra_mapping import ChakraMap
from samurai_bluebird_custos.frameworks.context_domains import ContextDomains

class BlueBox:
    '''The meta-lattice processor for symbolic convergence.'''

    def __init__(self):
        self.sovereignties = Sovereignties()
        self.chakra_map = ChakraMap()
        self.context_domains = ContextDomains()

    def process_input(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        '''Synthesizes input resonance across Sovereignties, Chakras, and Context Domains.'''
        print("[BlueBox] Processing input through symbolic frameworks...")

        sovereignties_resonance = self._map_sovereignties(input_data)
        chakra_resonance = self.chakra_map.map_input(input_data)
        domain_relevance = self.context_domains.map_input(input_data)

        lattice = self._synthesize_lattice(sovereignties_resonance, chakra_resonance, domain_relevance)
        print("[BlueBox] Lattice synthesis complete.")
        return lattice

    def _map_sovereignties(self, input_data: Dict[str, Any]) -> Dict[str, float]:
        '''Maps input tags to sovereignty resonance scores.'''
        resonance = {}
        tags = input_data.get('tags', [])
        weights = input_data.get('weights', {})

        for tag in tags:
            archetype = self.sovereignties.get_archetype(tag)
            if archetype:
                weight = weights.get(tag, 1.0)
                resonance[tag] = weight * 0.1

        max_score = max(resonance.values(), default=1.0)
        resonance = {k: min(v / max_score, 1.0) for k, v in resonance.items()}
        return resonance

    def _synthesize_lattice(self, sovereignties: Dict[str, float], chakras: Dict[str, float], domains: Dict[str, float]) -> Dict[str, Any]:
        '''Combines framework outputs into a unified resonance lattice.'''
        lattice = {
            "Sovereignties": sovereignties,
            "Chakras": chakras,
            "ContextDomains": domains,
            "MetaSummary": {
                "DominantChakra": max(chakras, key=chakras.get),
                "DominantDomain": max(domains, key=domains.get),
                "HighResonanceTags": [k for k, v in sovereignties.items() if v > 0.7]
            }
        }
        return lattice

if __name__ == "__main__":
    bb = BlueBox()
    test_input = {
        "tags": ["Compassion", "Innovation", "Trust"],
        "weights": {"Compassion": 1.2, "Innovation": 1.0, "Trust": 0.8}
    }
    lattice = bb.process_input(test_input)
    print("Unified Resonance Lattice:", lattice)

