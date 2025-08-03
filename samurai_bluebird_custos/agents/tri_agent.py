### tri_agent.py

from samurai_bluebird_custos.frameworks import blue_box


def reason_over_batch(snapshot):
    """
    Tri-Agent Multi-Mind: interprets a snapshot using BlueBox and returns a narrative and symbolic enrichment
    """
    symbolic_data = blue_box.process(snapshot)  # Symbolic cognition pipeline
    narrative = generate_narrative_hook(symbolic_data)  # Human-facing interpretation

    enriched_output = {
        "narrative": narrative,
        "enriched_batch": symbolic_data
    }
    return enriched_output


def generate_narrative_hook(symbolic_data):
    tone = symbolic_data.get("emotional_tone", "neutral")
    tags = symbolic_data.get("tags", [])
    domains = symbolic_data.get("context_domains", [])

    summary = (
        f"Detected emotional tone: {tone}. "
        f"Tagged symbolic patterns: {', '.join(tags)}. "
        f"Active context domains: {', '.join(domains)}."
    )
    return summary
