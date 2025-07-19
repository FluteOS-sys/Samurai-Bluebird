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
from typing import List, Dict, Optional


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

