# samurai_bluebird_custos/frameworks/blue_box.py

import json
import os

class BlueBox:
    def __init__(self):
        print("🔷 BlueBox initialized.")
        self.sovereignties = self._load_dataset("frameworks/sovereignties_dataset.json")
        self.chakras = self._load_dataset("frameworks/chakra_definitions.json")
        self.context_domains = self._load_dataset("frameworks/context_domains.json")

    def _load_dataset(self, relative_path: str) -> dict:
        """
        Load a dataset JSON from the frameworks directory.
        """
        try:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            dataset_path = os.path.join(project_root, "samurai_bluebird_custos", relative_path)
            with open(dataset_path, "r", encoding="utf-8") as f:
                print(f"📦 Loaded dataset from {dataset_path}")
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️ Dataset not found: {relative_path}")
            return {}

    def process(self, batch_data: dict) -> dict:
        """
        Process incoming batch data through Sovereignties, Chakras, and Context Domains.
        """
        print("🔷 BlueBox: Processing batch data...")

        # Sovereignties mapping (placeholder logic)
        sovereigns_hit = [s for s in self.sovereignties.keys() if s.lower() in str(batch_data).lower()]

        # Chakra mapping (placeholder logic)
        chakras_hit = [c for c in self.chakras.keys() if c.lower() in str(batch_data).lower()]

        # Context Domains tagging (placeholder logic)
        domains_hit = [d for d in self.context_domains.keys() if d.lower() in str(batch_data).lower()]

        framework_output = batch_data.copy()
        framework_output["bluebox_metadata"] = {
            "sovereignties_matched": sovereigns_hit or ["None"],
            "chakras_activated": chakras_hit or ["None"],
            "context_domains_tagged": domains_hit or ["None"]
        }

        print(f"🔷 Sovereignties matched: {sovereigns_hit}")
        print(f"🔷 Chakras activated: {chakras_hit}")
        print(f"🔷 Context Domains tagged: {domains_hit}")

        return framework_output
