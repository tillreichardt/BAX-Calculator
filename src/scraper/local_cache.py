import json
import os
from datetime import datetime, timedelta

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE_FILE = os.path.join(_PROJECT_ROOT, "bax_cache.json")
# Wie lange sollen die Daten gültig sein? (z.B. 7 Tage)
CACHE_EXPIRATION_DAYS = 200

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_to_cache(key, data):
    cache = load_cache()
    cache[key] = {
        "timestamp": datetime.now().isoformat(),
        "data": data
    }
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)

def get_from_cache(key):
    cache = load_cache()
    if key in cache:
        entry = cache[key]
        cached_date = datetime.fromisoformat(entry["timestamp"])
        # Prüfen, ob der Cache zu alt ist
        if datetime.now() - cached_date < timedelta(days=CACHE_EXPIRATION_DAYS):
            return entry["data"]
    return None