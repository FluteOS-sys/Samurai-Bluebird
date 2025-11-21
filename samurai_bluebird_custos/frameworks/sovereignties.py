'''sovereignties.py - Part of Samurai Bluebird Custos Frameworks

Handles the 72 Sovereignties of Human Agency dataset and provides duality mapping.
This module serves as the archetypal backbone for Chakra Mapping, Context Domains,
and the Blue Box lattice processor.

Philosophy:
Each Sovereignty represents a fundamental freedom of human agency.
Light/Dark dualities reflect the shadow work of organizational and personal dynamics.
'''

import json
from pathlib import Path
from typing import List, Dict, Optional, Any


class Sovereignties:
    '''
    Manages the 72 Sovereignties of Human Agency.

    Provides access to archetype metadata, light/dark dualities,
    and utility functions for framework integrations.
    '''

    def __init__(self, dataset_path: Optional[Path] = None):
        '''
        Initializes the Sovereignties dataset.
        If no dataset_path is provided, loads the default internal dataset.

        :param dataset_path: Optional path to a custom JSON dataset.
        '''
        self.dataset_path = dataset_path or Path(__file__).parent / 'sovereignties_dataset.json'
        self.archetypes: Dict[str, Dict] = {}
        self.load_dataset()

    def load_dataset(self) -> None:
        '''Loads the 72 Sovereignties dataset into memory.'''
        try:
            with open(self.dataset_path, 'r', encoding='utf-8') as f:
                self.archetypes = json.load(f)
            print(f"[Sovereignties] Loaded dataset from {self.dataset_path}")
        except FileNotFoundError:
            print(f"[Sovereignties] ERROR: Dataset file not found at {self.dataset_path}")
            self.archetypes = {}
        except json.JSONDecodeError:
            print(f"[Sovereignties] ERROR: Invalid JSON format in dataset file.")
            self.archetypes = {}

    def get_archetype(self, name: str) -> Optional[Dict]:
        '''
        Retrieves metadata for a specific Sovereignty.

        :param name: Name of the archetype.
        :return: Dict of archetype data or None if not found.
        '''
        return self.archetypes.get(name)

    def get_duality(self, name: str) -> Optional[Dict[str, str]]:
        '''
        Retrieves the light/dark duality pair for a Sovereignty.

        :param name: Name of the archetype.
        :return: Dict with 'light' and 'dark' keys or None if not found.
        '''
        archetype = self.get_archetype(name)
        if archetype and 'duality' in archetype:
            return archetype['duality']
        return None

    def match_tag(self, tag: str) -> Optional[str]:
        '''
        Attempts to match an arbitrary tag or emotion to a Sovereignty archetype.

        Matching is case-insensitive and will resolve against the sovereignty name
        as well as its light/dark expressions so we can gracefully route emotional
        language into the constellation map.
        '''
        normalized = tag.strip().lower()
        for name, data in self.archetypes.items():
            if normalized == name.lower():
                return name
            if normalized == str(data.get('light', '')).lower():
                return name
            if normalized == str(data.get('dark', '')).lower():
                return name
        return None

    @staticmethod
    def _resolve_valence(tag: str, archetype: Dict[str, Any]) -> str:
        '''
        Determine whether the provided tag is referencing the light, shadow, or
        neutral expression of the archetype for more human-readable plotting.
        '''
        lower_tag = tag.lower()
        if lower_tag == str(archetype.get("light", "")).lower():
            return "light"
        if lower_tag == str(archetype.get("dark", "")).lower():
            return "shadow"
        return "neutral"

    def route_affect_to_constellation(
        self, affect_tags: List[str], weights: Optional[Dict[str, float]] = None
    ) -> Dict[str, Any]:
        '''
        Projects reasoned emotions (sovereignties) onto the FluteOS Chakra-Pillar
        Sovereign Constellation Map.

        Returns a payload that includes the chakra row, symbolic spread coordinates,
        and aggregate chakra weighting so the UI or downstream reasoning layers can
        render the affect map directly.
        '''
        weights = weights or {}
        constellation_nodes: List[Dict[str, Any]] = []
        chakra_totals: Dict[str, float] = {}

        for tag in affect_tags:
            match = self.match_tag(tag)
            if not match:
                continue

            archetype = self.archetypes.get(match, {})
            chakra = archetype.get("chakra", "")
            spread = archetype.get("symbolic_spread", [0, 0])
            weight = float(weights.get(tag, 1.0))
            valence = self._resolve_valence(tag, archetype)

            constellation_nodes.append(
                {
                    "sovereignty": match,
                    "chakra": chakra,
                    "symbolic_spread": spread,
                    "weight": round(weight, 3),
                    "valence": valence,
                    "source_tag": tag,
                }
            )

            if chakra:
                chakra_totals[chakra] = chakra_totals.get(chakra, 0.0) + weight

        total_weight = sum(chakra_totals.values()) or 1.0
        chakra_affect = {
            chakra: round(weight / total_weight, 3) for chakra, weight in chakra_totals.items()
        }

        return {
            "nodes": constellation_nodes,
            "chakra_affect": chakra_affect,
            "matched_tags": [node["source_tag"] for node in constellation_nodes],
        }

    def list_all(self) -> List[str]:
        '''
        Returns a list of all Sovereignty names.

        :return: List of archetype names.
        '''
        return list(self.archetypes.keys())

    def list_dualities(self) -> Dict[str, Dict[str, str]]:
        '''
        Returns a dictionary of all archetypes with their light/dark dualities.

        :return: Dict mapping archetype names to their dualities.
        '''
        return {name: data['duality'] for name, data in self.archetypes.items() if 'duality' in data}


# Example usage (remove or comment out for production)
if __name__ == "__main__":
    s = Sovereignties()
    print("All Sovereignties:", s.list_all())
    print("Dualities for 'Trust':", s.get_duality('Trust'))

