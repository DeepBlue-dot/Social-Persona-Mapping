# ml_engine/pipeline/preprocess.py

import json
from pathlib import Path
import re
from PIL import Image
import requests
from io import BytesIO


def clean_text(text: str):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z0-9\s.,?!]", "", text)  # Remove special chars
    text = text.strip()
    return text


def normalize_image(image_url: str, username: str, platform: str):
    folder = Path(f"data/processed/{platform}/images")
    folder.mkdir(parents=True, exist_ok=True)

    if not image_url:
        return None

    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((256, 256))
        path = folder / f"{username}.png"
        img.save(path)
        return str(path)
    except:
        return None


def preprocess_raw(platform: str, username: str):
    raw_file = Path(f"data/raw/{platform}/{username}.json")
    if not raw_file.exists():
        return {"error": "Raw file not found"}

    data = json.loads(raw_file.read_text())

    # Clean text posts
    processed_posts = []
    for post in data.get("posts", []):
        processed_posts.append({
            "text": clean_text(post["text"]),
            "timestamp": post["timestamp"]
        })

    # Normalize profile image
    normalized_img_path = normalize_image(
        data["profile"].get("profile_image"),
        username,
        platform,
    )

    processed = {
        "username": username,
        "platform": platform,
        "bio": clean_text(data["profile"].get("bio", "")),
        "join_date": data["profile"].get("join_date"),
        "image_path": normalized_img_path,
        "posts": processed_posts
    }

    # Save processed output
    out_dir = Path(f"data/processed/{platform}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{username}.json"
    out_file.write_text(json.dumps(processed, indent=4))

    return {"processed_file": str(out_file)}
