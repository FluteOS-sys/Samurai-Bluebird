### tri_agent.py

from samurai_bluebird_custos.symbolic.recursive_memory_lattice import RecursiveSymbolicMemoryLattice

# Simulated Tri-Agent cognitive lenses
class TriAgent:
    def __init__(self):
        self.memory = RecursiveSymbolicMemoryLattice("memory/recursive_symbolic_memory.json")

    def reason_over_batch(self, snapshot):
        """
        Multi-mind interpretation from logical, emotional, and narrative lenses.
        Keeps language grounded and companion-like while still surfacing growth signals.
        Returns a narrative + symbolic hooks suitable for AMS integration.
        """
        memory_state = self.memory.fetch_recent_symbols()

        # Phase 1: Lens-based analysis
        logic_analysis = self.logic_lens(snapshot, memory_state)
        emotion_analysis = self.emotion_lens(snapshot, memory_state)
        narrative_analysis = self.narrative_lens(snapshot, memory_state)

        # Phase 2: Integrate lenses into unified interpretation
        narrative = self.integrate_lenses(logic_analysis, emotion_analysis, narrative_analysis)

        raw_enriched = {
            "tags": list(
                set(
                    logic_analysis["tags"]
                    + emotion_analysis["tags"]
                    + narrative_analysis["tags"]
                )
            ),
            "emotional_tone": emotion_analysis["tone"],
            "resonance_score": logic_analysis.get("resonance", 0.5),
        }

        enriched_output = {
            "narrative": narrative,
            "raw_enriched": raw_enriched,
            "ams_output": self.build_ams_bridge(narrative, raw_enriched),
        }
        return enriched_output

    def logic_lens(self, snapshot, memory):
        tags = snapshot.get("tags", [])
        focus_tag = tags[0].lower() if tags else "current work"
        resonance_score = snapshot.get("weights", {}).get(tags[0], 0.5) if tags else 0.5
        resonance_score = max(0.0, min(1.0, resonance_score))
        return {"tags": [focus_tag], "resonance": resonance_score, "focus": focus_tag}

    def emotion_lens(self, snapshot, memory):
        weights = snapshot.get("weights", {})
        high_valence = [tag for tag, weight in weights.items() if weight >= 1.1]
        tone = "steady" if not high_valence else "uplifted"
        emotion_tag = high_valence[0].lower() if high_valence else "calm"
        return {"tags": [emotion_tag], "tone": tone}

    def narrative_lens(self, snapshot, memory):
        hooks = memory.get("narrative_hooks", [])
        recent_themes = ", ".join(hooks[:2]) if hooks else "steady progress"
        return {
            "tags": hooks if hooks else ["growth"],
            "summary": f"Carrying forward themes of {recent_themes}.",
        }

    def integrate_lenses(self, logic, emotion, narrative):
        thematic_tags = narrative["tags"] if narrative.get("tags") else ["growth"]
        themes_preview = ", ".join(thematic_tags[:2])
        return (
            f"Noticing focus on {logic['focus']} with a {emotion['tone']} tone. "
            f"Recent themes like {themes_preview} are showing up. "
            f"I'll keep the language plain and supportive while tracking growth."
        )

    def build_ams_bridge(self, narrative, raw_enriched):
        return {
            "narrative": narrative,
            "signals": {
                "resonance": raw_enriched.get("resonance_score", 0.5),
                "emotional_tone": raw_enriched.get("emotional_tone", "neutral"),
                "tags": raw_enriched.get("tags", []),
            },
        }
