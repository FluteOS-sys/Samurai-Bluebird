"""Adapter for routing symbolic context through an LLM provider."""

import importlib.util
import json
import os
from typing import Any, Dict, List, Optional

from samurai_bluebird_custos.utils import config


class LLMBridge:
    """Wrap a chosen LLM provider with Samurai Bluebird context packing."""

    def __init__(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        self.provider = (provider or os.getenv("LLM_PROVIDER", config.LLM_PROVIDER)).lower()
        self.model = model or os.getenv("LLM_MODEL", config.LLM_MODEL)
        self.api_key = api_key or os.getenv(config.LLM_API_KEY_ENV_VAR, "")
        self.client = self._initialize_client()

    def generate_response(
        self, snapshot: Dict[str, Any], memory_state: Dict[str, Any], narrative_hint: str
    ) -> Dict[str, Any]:
        prompt = self._build_prompt(snapshot, memory_state, narrative_hint)
        return self._run_inference(prompt, snapshot, memory_state)

    def chat_reply(
        self,
        user_message: str,
        snapshot: Optional[Dict[str, Any]] = None,
        memory_state: Optional[Dict[str, Any]] = None,
        narrative_hint: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Route a user-facing chat message through the same contextual lens."""

        snapshot = snapshot or {}
        memory_state = memory_state or {}
        prompt = self._build_prompt(snapshot, memory_state, narrative_hint or "")
        prompt += "\nUser message:\n" + user_message.strip()
        llm_output = self._run_inference(prompt, snapshot, memory_state)
        llm_output["user_reply"] = llm_output.get("narrative", "")
        return llm_output

    def _initialize_client(self):
        if self.provider == "openai" and self.api_key:
            if importlib.util.find_spec("openai"):
                import openai

                openai.api_key = self.api_key
                return openai
        return None

    def _build_prompt(
        self, snapshot: Dict[str, Any], memory_state: Dict[str, Any], narrative_hint: str
    ) -> str:
        snapshot_block = json.dumps(snapshot, indent=2)
        memory_block = json.dumps(memory_state, indent=2)
        hint = narrative_hint or ""
        return (
            "You are the Samurai Bluebird reasoning bridge. Blend symbolic memory with live inputs to craft a concise "
            "narrative and suggest two follow-up investigations.\n"
            "Snapshot (recent sensorium):\n" + snapshot_block + "\n" +
            "Symbolic memory (recent lattice nodes):\n" + memory_block + "\n" +
            "Existing narrative hints or hooks:\n" + hint + "\n"
            "Respond with short paragraphs and bullet suggestions."
        )

    def _run_inference(
        self, prompt: str, snapshot: Dict[str, Any], memory_state: Dict[str, Any]
    ) -> Dict[str, Any]:
        if self.client:
            try:
                completion = self.client.ChatCompletion.create(
                    model=self.model,
                    messages=[{"role": "system", "content": prompt}],
                    temperature=0.3,
                )
                content = completion["choices"][0]["message"]["content"]
                return self._parse_response(content, snapshot, memory_state)
            except Exception as exc:  # pragma: no cover - provider failures fall back to offline
                print(f"⚠️ LLM call failed, using offline heuristic: {exc}")
        return self._offline_response(snapshot, memory_state, prompt)

    def _parse_response(
        self, content: str, snapshot: Dict[str, Any], memory_state: Dict[str, Any]
    ) -> Dict[str, Any]:
        suggestions: List[str] = []
        for line in content.splitlines():
            if line.strip().startswith("-"):
                suggestions.append(line.strip("- "))
        suggestions = suggestions or ["Reflect on resonance drift", "Collect richer passive input"]
        return {
            "narrative": content.strip(),
            "follow_ups": suggestions,
            "symbolic_context": {"snapshot": snapshot, "memory": memory_state},
        }

    def _offline_response(
        self, snapshot: Dict[str, Any], memory_state: Dict[str, Any], prompt: str
    ) -> Dict[str, Any]:
        window = snapshot.get("active_window", "an unknown window")
        keystrokes = snapshot.get("keystroke_burst", "?")
        memory_keys = list(memory_state.keys()) if isinstance(memory_state, dict) else []
        narrative = (
            f"Observing {window} with {keystrokes} recent keystrokes, the agent cross-references "
            f"{len(memory_keys)} symbolic threads to maintain continuity."
        )
        follow_ups = [
            "Log nuanced cues from the current window to extend the lattice",
            "Ask the user for intent to align symbolic resonance",
        ]
        return {
            "narrative": narrative,
            "follow_ups": follow_ups,
            "symbolic_context": {"snapshot": snapshot, "memory": memory_state, "prompt": prompt},
        }
