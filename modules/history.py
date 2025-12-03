import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_emotion(emotion):
    history = load_history()
    history.append({"emotion": emotion, "time": datetime.now().isoformat()})

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def get_recent_emotions(n=7):
    return load_history()[-n:]

def get_history_list():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except:
        return []