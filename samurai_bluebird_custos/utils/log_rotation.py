# samurai_bluebird_custos/utils/log_rotation.py

import os
import shutil
from datetime import datetime

def rotate_logs(base_dir="logs", days_to_keep=7):
    """Rotate log folders, keeping only the most recent N days."""
    all_folders = sorted(
        [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    )
    while len(all_folders) > days_to_keep:
        oldest = all_folders.pop(0)
        full_path = os.path.join(base_dir, oldest)
        shutil.rmtree(full_path)
        print(f"🗑 Removed old log folder: {full_path}")
