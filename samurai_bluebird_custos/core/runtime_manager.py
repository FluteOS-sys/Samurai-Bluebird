"""Background runtime management for the Kernel and passive capture."""

import threading
import time
from typing import Any, Dict, List

from samurai_bluebird_custos.core.cognitive_pipeline import CognitivePipeline
from samurai_bluebird_custos.core.kernel import Kernel


class KernelManager:
    def __init__(self, pipeline: CognitivePipeline | None = None, interval_seconds: int = 300):
        self.kernel = Kernel()
        self.pipeline = pipeline or CognitivePipeline()
        self.interval_seconds = interval_seconds
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        self.passive_capture_enabled = True
        self.recent_snapshots: List[Dict[str, Any]] = []
        self.recent_narratives: List[Dict[str, Any]] = []

    @property
    def running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    def start(self, interval_seconds: int | None = None) -> None:
        if self.running:
            return
        if interval_seconds:
            self.interval_seconds = interval_seconds
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=1.0)
        self._thread = None

    def toggle_passive_capture(self, enabled: bool) -> None:
        with self._lock:
            self.passive_capture_enabled = enabled

    def _run_loop(self) -> None:
        while not self._stop_event.is_set():
            with self._lock:
                active = self.passive_capture_enabled
            if active:
                snapshot = self.kernel.feathers.capture()
                payload = self.pipeline.process_snapshot(snapshot)
                self._record_snapshot(payload)
            time.sleep(self.interval_seconds)

    def _record_snapshot(self, payload: Dict[str, Any]) -> None:
        with self._lock:
            self.recent_snapshots.append(payload)
            narrative = {
                "timestamp": payload.get("timestamp"),
                "source": payload.get("snapshot", {}).get("active_window", "passive-capture"),
                "text": payload.get("tri_narrative", ""),
            }
            self.recent_narratives.append(narrative)
            self.recent_snapshots = self.recent_snapshots[-50:]
            self.recent_narratives = self.recent_narratives[-100:]

    def process_prompt(self, prompt: str) -> Dict[str, Any]:
        payload = self.pipeline.process_prompt(prompt)
        with self._lock:
            narrative = {
                "timestamp": payload.get("timestamp"),
                "source": "user-prompt",
                "text": payload.get("tri_narrative", ""),
            }
            self.recent_narratives.append(narrative)
            self.recent_narratives = self.recent_narratives[-100:]
        return payload

    def status(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "running": self.running,
                "passive_capture_enabled": self.passive_capture_enabled,
                "interval_seconds": self.interval_seconds,
                "recent_snapshots": list(self.recent_snapshots[-5:]),
                "recent_narratives": list(self.recent_narratives[-20:]),
            }
