'''context_domains.py - Part of Samurai Bluebird Custos Frameworks

Maps behavioral patterns into 12 Contextual Life Domains.
This module provides situational anchoring for resonance tagging
and narrative flow within the Blue Box lattice processor.

Philosophy:
The 12 Contextual Domains represent arenas of human life where patterns emerge.
They help anchor symbolic cognition in situational relevance.
'''

from typing import Dict, Any, Optional
from pathlib import Path
import json


class ContextDomains:
    '''
    Handles 12 Contextual Life Domains.

    Provides tagging of input patterns to situational domains
    (e.g., Creativity, Foundations, Partnerships, etc.).
    '''

    def __init__(self, domains_file: Optional[Path] = None):
        '''
        Initializes ContextDomains with optional custom domains dataset.

        :param domains_file: Optional path to a JSON file defining domains.
        '''
        self.domains_file = domains_file or Path(__file__).parent / 'context_domains.json'
        self.domains: Dict[str, Dict[str, Any]] = {}
        self.load_domains()

    def load_domains(self) -> None:
        '''Loads context domains from JSON into memory.'''
        try:
            with open(self.domains_file, 'r', encoding='utf-8') as f:
                self.domains = json.load(f)
            print(f"[ContextDomains] Loaded domains from {self.domains_file}")
        except FileNotFoundError:
            print(f"[ContextDomains] WARNING: Domains file not found at {self.domains_file}. Using default domains.")
            self._load_default_domains()
        except json.JSONDecodeError:
            print(f"[ContextDomains] ERROR: Invalid JSON format in domains file.")
            self._load_default_domains()

    def _load_default_domains(self) -> None:
        '''Fallback to hardcoded domains if file missing or invalid.'''
        self.domains = {
            "Foundations": {"index": 1, "themes": ["Stability", "Survival", "Resources"]},
            "Creativity": {"index": 2, "themes": ["Innovation", "Artistry", "Flow"]},
            "Partnerships": {"index": 3, "themes": ["Relationships", "Trust", "Communication"]},
            "Community": {"index": 4, "themes": ["Belonging", "Support", "Cooperation"]},
            "Health": {"index": 5, "themes": ["Wellness", "Healing", "Vitality"]},
            "Work": {"index": 6, "themes": ["Career", "Purpose", "Contribution"]},
            "Learning": {"index": 7, "themes": ["Growth", "Wisdom", "Perspective"]},
            "Expression": {"index": 8, "themes": ["Voice", "Creativity", "Truth"]},
            "Play": {"index": 9, "themes": ["Joy", "Ease", "Exploration"]},
            "Spirituality": {"index": 10, "themes": ["Transcendence", "Meaning", "Connection"]},
            "Legacy": {"index": 11, "themes": ["Impact", "Teaching", "Story"]},
            "Adaptation": {"index": 12, "themes": ["Change", "Resilience", "Flexibility"]}
        }

    def map_input(self, input_data: Dict[str, Any]) -> Dict[str, float]:
        '''
        Maps input data tags to relevance scores across 12 domains.

        :param input_data: Dict with symbolic tags and weights.
        :return: Dict mapping domain names to relevance scores (0.0–1.0)
        '''
        relevance = {domain: 0.0 for domain in self.domains}
        tags = input_data.get('tags', [])
        weights = input_data.get('weights', {})

        for tag in tags:
            for domain, data in self.domains.items():
                if tag in data['themes']:
                    weight = weights.get(tag, 1.0)
                    relevance[domain] += weight * 0.1  # Scale factor

        # Normalize scores
        max_score = max(relevance.values()) or 1.0
        relevance = {k: min(v / max_score, 1.0) for k, v in relevance.items()}

        return relevance

    def get_domain_profile(self) -> Dict[str, Dict[str, Any]]:
        '''
        Returns metadata for all context domains.

        :return: Dict of domain names and their attributes.
        '''
        return self.domains


# Example usage (remove for production)
if __name__ == "__main__":
    cd = ContextDomains()
    test_input = {
        "tags": ["Healing", "Growth", "Voice"],
        "weights": {"Healing": 1.2, "Growth": 1.0, "Voice": 0.8}
    }
    scores = cd.map_input(test_input)
    print("Context Domain Relevance Scores:", scores)
