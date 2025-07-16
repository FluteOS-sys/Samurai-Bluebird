'''chakra_mapping.py - Part of Samurai Bluebird Custos Frameworks

Maps inputs into the 7 chakra-coded energetic dimensions. This module interfaces with
Sovereignties and Context Domains to provide symbolic resonance tagging.

Philosophy:
The chakras represent layers of human experience from root survival instincts
to crown-level transpersonal awareness. Each mapped input carries multi-dimensional
weighting for resonance analysis in the Blue Box lattice.
'''

from typing import Dict, Any, Optional
from pathlib import Path
import json


class ChakraMap:
    '''
    Maps inputs into 7 chakra dimensions (Root → Crown).
    Provides resonance scores for use in downstream frameworks.
    '''

    def __init__(self, mapping_file: Optional[Path] = None):
        '''
        Initializes ChakraMap with optional custom mapping dataset.

        :param mapping_file: Optional path to a JSON file defining chakra weights and metadata.
        '''
        self.mapping_file = mapping_file or Path(__file__).parent / 'chakra_definitions.json'
        self.chakras: Dict[str, Dict[str, Any]] = {}
        self.load_chakra_definitions()

    def load_chakra_definitions(self) -> None:
        '''Loads chakra definitions from JSON into memory.'''
        try:
            with open(self.mapping_file, 'r', encoding='utf-8') as f:
                self.chakras = json.load(f)
            print(f"[ChakraMap] Loaded chakra definitions from {self.mapping_file}")
        except FileNotFoundError:
            print(
                f"[ChakraMap] WARNING: Chakra definitions file not found at {self.mapping_file}. Using default mapping.")
            self._load_default_chakras()
        except json.JSONDecodeError:
            print(f"[ChakraMap] ERROR: Invalid JSON format in chakra definitions file.")
            self._load_default_chakras()

    def _load_default_chakras(self) -> None:
        '''Fallback to hardcoded chakra mappings if file is missing or invalid.'''
        self.chakras = {
            "Root": {"index": 1, "qualities": ["Stability", "Grounding", "Survival"]},
            "Sacral": {"index": 2, "qualities": ["Creativity", "Emotion", "Flow"]},
            "Solar Plexus": {"index": 3, "qualities": ["Power", "Will", "Identity"]},
            "Heart": {"index": 4, "qualities": ["Love", "Connection", "Compassion"]},
            "Throat": {"index": 5, "qualities": ["Communication", "Expression", "Truth"]},
            "Third Eye": {"index": 6, "qualities": ["Intuition", "Clarity", "Insight"]},
            "Crown": {"index": 7, "qualities": ["Transcendence", "Awareness", "Unity"]}
        }

    def map_input(self, input_data: Dict[str, Any]) -> Dict[str, float]:
        '''
        Processes input data and returns resonance scores across 7 chakras.

        :param input_data: Dict containing symbolic tags and metadata.
        :return: Dict mapping chakra names to resonance scores (0.0–1.0)
        '''
        resonance = {chakra: 0.0 for chakra in self.chakras}
        tags = input_data.get('tags', [])
        weights = input_data.get('weights', {})

        for tag in tags:
            for chakra, data in self.chakras.items():
                if tag in data['qualities']:
                    weight = weights.get(tag, 1.0)
                    resonance[chakra] += weight * 0.1  # Scaling factor

        # Normalize scores to max of 1.0
        max_score = max(resonance.values()) or 1.0
        resonance = {k: min(v / max_score, 1.0) for k, v in resonance.items()}

        return resonance

    def get_chakra_profile(self) -> Dict[str, Dict[str, Any]]:
        '''
        Returns metadata for all chakras.

        :return: Dict of chakra names and their attributes.
        '''
        return self.chakras


# Example usage (remove for production)
if __name__ == "__main__":
    cm = ChakraMap()
    test_input = {
        "tags": ["Compassion", "Insight", "Expression"],
        "weights": {"Compassion": 1.5, "Insight": 1.0, "Expression": 0.8}
    }
    scores = cm.map_input(test_input)
    print("Chakra Resonance Scores:", scores)
