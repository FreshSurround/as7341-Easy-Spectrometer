import json
import time
from datetime import datetime


def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sleep_ms(ms):
    time.sleep(ms / 1000)


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def log(msg):
    print(f"[{now_str()}] {msg}")

