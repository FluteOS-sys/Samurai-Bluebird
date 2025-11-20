"""FastAPI server exposing Samurai Bluebird runtime controls and logs."""

from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from samurai_bluebird_custos.core.cognitive_pipeline import CognitivePipeline
from samurai_bluebird_custos.core.resonance_logger import tail_log
from samurai_bluebird_custos.core.runtime_manager import KernelManager


pipeline = CognitivePipeline()
manager = KernelManager(pipeline=pipeline, interval_seconds=300)

app = FastAPI(title="Samurai Bluebird Control Panel")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/status")
def get_status():
    """Return runtime state for the front-end."""

    return manager.status()


@app.post("/api/kernel/start")
def start_kernel(interval_seconds: Optional[int] = Body(default=None)):
    manager.start(interval_seconds=interval_seconds)
    return {"running": manager.running, "interval_seconds": manager.interval_seconds}


@app.post("/api/kernel/stop")
def stop_kernel():
    manager.stop()
    return {"running": manager.running}


@app.post("/api/passive/toggle")
def toggle_passive(enabled: bool = Body(..., embed=True)):
    manager.toggle_passive_capture(enabled)
    return {"passive_capture_enabled": manager.passive_capture_enabled}


@app.get("/api/logs")
def fetch_logs(date: Optional[str] = None, filename: str = "output_resonance_log.txt", limit: int = 50):
    """Return the last ``limit`` lines from a dated log file."""

    date_str = date or datetime.now().strftime("%Y-%m-%d")
    lines = tail_log(date_str, filename, limit=limit)
    return {"date": date_str, "filename": filename, "entries": lines}


@app.post("/api/prompt")
def submit_prompt(prompt: str = Body(..., embed=True)):
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")
    payload = manager.process_prompt(prompt)
    return payload


@app.get("/api/narratives")
def get_narratives(limit: int = 50):
    status = manager.status()
    return {"narratives": status.get("recent_narratives", [])[-limit:]}


STATIC_DIR = Path(__file__).parent / "static"


@app.get("/")
def root_index():
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse("<h1>Samurai Bluebird</h1><p>UI not found.</p>", status_code=200)
    return FileResponse(index_path)


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
