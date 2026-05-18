import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MUSIC_PATH = ROOT / "music.json"
SCENE_DIR = ROOT / "static" / "images" / "scenes"


def request_json(url, headers=None):
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def safe_slug(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "scene"


def download_scene_image(url, track_id, provider):
    SCENE_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{safe_slug(track_id)}-{provider}.jpg"
    destination = SCENE_DIR / filename

    request = urllib.request.Request(url, headers={"User-Agent": "PulseScape scene image fetcher"})
    with urllib.request.urlopen(request, timeout=30) as response:
        destination.write_bytes(response.read())

    return f"images/scenes/{filename}"


def search_pexels(query):
    api_key = os.environ.get("PEXELS_API_KEY")
    if not api_key:
        return None

    params = urllib.parse.urlencode({"query": query, "orientation": "landscape", "per_page": 1})
    data = request_json(
        f"https://api.pexels.com/v1/search?{params}",
        headers={"Authorization": api_key},
    )
    photos = data.get("photos", [])
    if not photos:
        return None

    photo = photos[0]
    return {
        "scene_image_url": photo["src"].get("large") or photo["src"]["large2x"],
        "scene_source_url": photo["url"],
        "scene_attribution": f"Photo by {photo['photographer']} on Pexels",
        "scene_license": "Pexels License",
    }


def search_pixabay(query):
    api_key = os.environ.get("PIXABAY_API_KEY")
    if not api_key:
        return None

    params = urllib.parse.urlencode(
        {
            "key": api_key,
            "q": query,
            "image_type": "photo",
            "orientation": "horizontal",
            "safesearch": "true",
            "per_page": 3,
        }
    )
    data = request_json(f"https://pixabay.com/api/?{params}")
    hits = data.get("hits", [])
    if not hits:
        return None

    image = hits[0]
    return {
        "scene_image_url": image.get("largeImageURL") or image.get("webformatURL"),
        "scene_source_url": image.get("pageURL"),
        "scene_attribution": f"Image by {image.get('user', 'Pixabay creator')} on Pixabay",
        "scene_license": "Pixabay Content License",
    }


def main():
    provider = (sys.argv[1] if len(sys.argv) > 1 else "pexels").lower()
    if provider not in {"pexels", "pixabay"}:
        raise SystemExit("Usage: python scripts/fetch_scene_images.py [pexels|pixabay]")

    tracks = json.loads(MUSIC_PATH.read_text(encoding="utf-8"))
    search = search_pexels if provider == "pexels" else search_pixabay

    updated = 0
    for track in tracks:
        query = track.get("scene_query") or track.get("scene_theme") or track.get("genre") or track["title"]
        result = search(query)
        if not result:
            continue
        image_url = result.pop("scene_image_url")
        result["scene_image"] = download_scene_image(image_url, track.get("id", track["title"]), provider)
        track.update(result)
        track["scene_query"] = query
        updated += 1

    MUSIC_PATH.write_text(
        json.dumps(tracks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Updated {updated} tracks with {provider} scene images.")


if __name__ == "__main__":
    main()
