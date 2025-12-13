# backend/services/storage_service.py

import json
from pathlib import Path

def save_raw_data(platform: str, username: str, data: dict):
    path = Path(f"../data/raw/{platform}")
    path.mkdir(parents=True, exist_ok=True)

    file = path / f"{username}.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return str(file)
